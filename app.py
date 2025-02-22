import os

import dotenv
import fastapi
import starlette.middleware.cors
import uvicorn

import routers

dotenv.load_dotenv()
app = fastapi.FastAPI(
    title="생성형 AI 서버 API",
    description="""
    \n ## 다양한 생성형 AI 서비스를 제공하는 서버 API입니다.
    \n ### 제공 모델
    \n <b>
    \n  - Mistral
    \n  - ClovaX
    \n  - Gemini
    \n  - Llama
    \n  - GPT
    \n  - Claude 
    \n  - DeepSeek
    \n </b>
    """,
    version="3.2"
)

app.add_middleware(
    starlette.middleware.cors.CORSMiddleware,
    allow_origins=[os.environ.get("FRONTEND_URL")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
