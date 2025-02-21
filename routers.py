import logging
import os
from typing import Dict, List, Optional

import starlette.responses
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
from fastapi import APIRouter
from pydantic import BaseModel, Field

from global_exception_handler import throw_unauthorized_exception, throw_paid_model_unauthorized_exception, \
    throw_paid_model_usage_limit_exception
from services import generate_response, generate_sync_response

router = APIRouter(prefix="")

paid_model_usage = 0
MODEL_DESCRIPTION = """
    \n- llm_type: LLM 모델 유형 (미입력 시 기본 모델 사용)
    \n  - mistral (현재 기본 모델)
    \n  - clovax
    \n  - gemini
    \n  - llama
    \n  - gpt (유료 모델: 관리자로부터 Secret Key 발급 필요)
    \n  - claude (유료 모델: 관리자로부터 Secret Key 발급 필요)
    \n  - deepseek (유료 모델: 관리자로부터 Secret Key 발급 필요)
    \n- template: 요청 프롬프트(요구사항)
    \n- options: 요청 프롬프트에 적용할 조건들(선택사항)
    \n  - Key: Array Value 형태로 전송
    \n- Secret Key: 사용자 인증을 위한 비밀 키
"""

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("gpt_logger")


class LLMRequest(BaseModel):
    llm_type: Optional[str] = Field(default=None,
                                    description="LLM 모델 유형(mistral, gemini, llama, clovax, gpt, claude, deepseek): 미입력 시 기본 모델 사용",
                                    examples=["mistral", "gemini", "llama", "clovax", "gpt", "claude", "deepseek"])
    template: str = Field(..., description="요청 프롬프트(요구사항)", examples=["레시피 추천해 줘"])
    options: Optional[Dict[str, List[str]]] = Field(
        default=None,
        description="요청 프롬프트에 적용할 조건들(선택사항)",
        examples=[
            {
                "재료": ["토마토", "밀가루", "양파"],
                "조리 도구": ["프라이팬", "오븐", "믹서기"],
                "조리 시간": ["30분"],
                "요리 유형": ["이탈리안"],
                "식사 유형": ["아침"]
            }
        ]
    )
    secret_key: str = Field(..., description="사용자 인증을 위한 비밀 키", examples=["abcde"])

    class Config:
        title = "LLM 서비스 요청 파라미터"


from fastapi.responses import StreamingResponse


@router.post(
    "/sync",
    summary="LLM 서비스 이용",
    description="다음 파라미터를 전송해 LLM 서비스를 이용할 수 있습니다. 전체 응답이 한 번에 제공됩니다." + MODEL_DESCRIPTION
)
def invoke_llm(request: LLMRequest):
    load_dotenv()
    authenticate(request.llm_type.lower(), request.secret_key)

    llm_type = request.llm_type if request.llm_type else ""
    options = request.options if request.options else {"Not necessary"}

    response_content = generate_sync_response(llm_type, request.template, options)

    if isinstance(response_content, set):
        response_content = list(response_content)

    return starlette.responses.JSONResponse(content=response_content)


@router.post(
    "/streaming",
    summary="LLM 스트리밍 서비스 이용",
    description="다음 파라미터를 전송해 LLM 서비스를 이용할 수 있습니다. 응답은 토큰화하여 Stream 형태로 제공됩니다." + MODEL_DESCRIPTION
)
def invoke_llm(request: LLMRequest):
    load_dotenv()
    authenticate(request.llm_type.lower(), request.secret_key)

    llm_type = request.llm_type if request.llm_type else ""
    options = request.options if request.options else {"Not necessary"}

    def response_generator():
        for chunk in generate_response(
                llm_type, request.template, options
        ):
            yield chunk

    return StreamingResponse(response_generator(), media_type="text/plain")


@router.post(
    "/streaming/sse",
    summary="LLM 스트리밍 SSE 서비스 이용",
    description="다음 파라미터를 전송해 LLM 서비스를 이용할 수 있습니다. 응답은 최소 단위로 토큰화하여 SSE를 통한 Stream 형태로 제공됩니다." + MODEL_DESCRIPTION
)
def invoke_llm_sse(request: LLMRequest):
    load_dotenv()
    authenticate(request.llm_type.lower(), request.secret_key)

    llm_type = request.llm_type if request.llm_type else ""
    options = request.options if request.options else {"Not necessary"}

    def response_generator():
        for chunk in generate_response(
                llm_type, request.template, options
        ):
            yield f"data: {chunk}\n\n"

    return StreamingResponse(response_generator(), media_type="text/event-stream")


def authenticate(input_llm_type, input_secret_key):
    if is_paid_model(input_llm_type):
        authorize_paid_model(input_llm_type, input_secret_key)
    elif input_secret_key != os.environ.get("SECRET_KEY"):
        throw_unauthorized_exception()


def is_paid_model(llm_type):
    return llm_type == "gpt" or llm_type == "claude" or llm_type == "deepseek"


def authorize_paid_model(input_llm_type, input_secret_key):
    global paid_model_usage

    if (input_secret_key != os.environ.get("SECRET_KEY_FOR_PAID_MODEL")):
        throw_paid_model_unauthorized_exception(input_llm_type)
    else:
        paid_model_usage += 1

        # 유료 모델 일일 사용 한도를 10,000회로 제한
        if (paid_model_usage > 10_000):
            throw_paid_model_usage_limit_exception(input_llm_type)
        logger.info("%s API가 호출되었습니다. 일일 사용량: %d", input_llm_type, paid_model_usage)


def reset_gpt_usage():
    global paid_model_usage
    paid_model_usage = 0


logger.info("유료 모델 사용량이 초기화 되었습니다. 일일 사용량: %d", paid_model_usage)

scheduler = BackgroundScheduler()

# 매일 자정마다 유료 모델 사용량 초기화
scheduler.add_job(reset_gpt_usage, "cron", hour=0, minute=0)
scheduler.start()
