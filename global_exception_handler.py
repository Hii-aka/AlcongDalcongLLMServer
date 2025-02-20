from fastapi import HTTPException


def throw_unauthorized_exception():
    raise HTTPException(
        status_code=401,
        detail="[인증 실패] Secret Key가 일치하지 않습니다. 확인 후 다시 시도해 주세요."
    )


def throw_paid_model_unauthorized_exception(llm_type):
    raise HTTPException(
        status_code=401,
        detail=f"[인증 실패] Secret Key가 일치하지 않습니다. {llm_type}는 유료 모델이므로 관리자로부터 Secret Key를 직접 제공받아야 사용할 수 있습니다."
    )


def throw_paid_model_usage_limit_exception(llm_type):
    raise HTTPException(
        status_code=403,
        detail=f"[한도 초과] {llm_type} 유료 모델의 일일 사용 한도를 초과했습니다. 일일 사용량은 자정에 초기화됩니다."
    )
