# ![ai](https://github.com/user-attachments/assets/0183c7fc-c7a7-479b-8108-4c68de3dffa7) 생성형 AI Streaming Server <img src="https://img.shields.io/badge/v3.2-6DB33F?style=flat-square&logo=Adobe&logoColor=white"><br><br>

## 📋 프로젝트 설명

### 다양한 생성형 AI 모델의 스트리밍 서비스를 제공하는 서버
- Mistral Large
- HCX-003
- Gemini 1.5 Pro
- Llama 3.3
- GPT 4o Mini
- Claude Haiku
- DeepSeek V3
<br><br>

## 📼 서비스 시연
![hyobin-llm](https://github.com/user-attachments/assets/f62ff497-d639-4176-b21a-e29d6cda76bd)
<br><br>

## 📅 프로젝트 기간
<b>2025. 01. 26 ~ 2025. 01. 28</b>
<br><br>

## ![Image](https://github.com/user-attachments/assets/1838d6b9-69ff-43fe-80b1-b1e39709cef9) 모델 추가 및 리팩터링
<b>2025. 01. 30, 2025. 02. 10, 2025. 02. 21, 2025. 02. 22</b>
<br><br>

## 👫 구성원

### 성효빈
- 서버 개발, 배포 및 관리
  <br>

## 📚 관련 URL
- [서비스 URL](https://hyobin-llm.vercel.app)
- [LLM Streaming 서버 API](https://hyobin-llm.duckdns.org/docs)
- [LLM Spring API 클라이언트 서버 API](https://hyobin-llm-spring.duckdns.org/swagger-ui/index.html)
- [LLM Nest.js API 클라이언트 서버 API](https://hyobin-llm-nest.duckdns.org/api)
- [LLM 클라이언트 Repository](https://github.com/hellmir/LLM-Streaming-Client)
- [LLM Spring API 클라이언트 서버 Repository](https://github.com/hellmir/LLM-Spring-API-Client)
- [LLM Nest API 클라이언트 서버 Repository](https://github.com/hellmir/LLM-Nest-API-Client)
  <br><br>

## 🗼 Architecture
![llm-service](https://github.com/user-attachments/assets/e12f5131-d55a-4142-bae1-f58b40b91784)

## 🛠️ Skills

## Back-End
- Python
- LangChain
- FastAPI
- Starlette
  <br>

## AI Model Packages
- ChatMistralAI
- ChatClovaX
- ChatGoogleGenerativeAI
- SambaNovaCloud
- ChatOpenAI
- ChatAnthropic
- ChatDeepSeek

## DevOps

### Interpretation
- Pipenv

### WAS
- Uvicorn

### Server
- NCP Server
  <br>

## Tools

### IDE
- PyCharm

### Issue Tracking
- Jira

<br>

## 릴리스 정보 - LangChain Service - LlmApiServerRelease01/27

### 하위 작업

[LCSV-3](https://langchain.atlassian.net/browse/LCSV-3) Pipfile 생성

[LCSV-4](https://langchain.atlassian.net/browse/LCSV-4) LangChain 설치

[LCSV-5](https://langchain.atlassian.net/browse/LCSV-5) LangChain OpenAI 패키지 설치

[LCSV-6](https://langchain.atlassian.net/browse/LCSV-6) LangChain Llama3.2 패키지 설치

[LCSV-7](https://langchain.atlassian.net/browse/LCSV-7) LangChain HCX-003 패키지 설치

[LCSV-8](https://langchain.atlassian.net/browse/LCSV-8) LangChain Community 패키지 설치

[LCSV-9](https://langchain.atlassian.net/browse/LCSV-9) Formatter 패키지 설치

[LCSV-10](https://langchain.atlassian.net/browse/LCSV-10) Dotenv 패키지 설치

[LCSV-11](https://langchain.atlassian.net/browse/LCSV-11) .env 파일 추가

[LCSV-12](https://langchain.atlassian.net/browse/LCSV-12) uvicorn 패키지 설치

[LCSV-13](https://langchain.atlassian.net/browse/LCSV-13) fastapi 패키지 설치

[LCSV-14](https://langchain.atlassian.net/browse/LCSV-14) app.py 추가

[LCSV-16](https://langchain.atlassian.net/browse/LCSV-16) LLM 타입과 템플릿, 변수 목록, 시크릿 키를 통한 클라이언트 요청

[LCSV-17](https://langchain.atlassian.net/browse/LCSV-17) 클라이언트 시크릿 키 인증

[LCSV-18](https://langchain.atlassian.net/browse/LCSV-18) LLM 서비스 요청 비즈니스 로직

[LCSV-19](https://langchain.atlassian.net/browse/LCSV-19) 200 status code 응답

[LCSV-21](https://langchain.atlassian.net/browse/LCSV-21) 서버 API 설명

[LCSV-22](https://langchain.atlassian.net/browse/LCSV-22) 엔드포인트 설명

[LCSV-23](https://langchain.atlassian.net/browse/LCSV-23) 파라미터 샘플값 적용

[LCSV-25](https://langchain.atlassian.net/browse/LCSV-25) 네이버 클라우드에 서버 인스턴스 생성

[LCSV-26](https://langchain.atlassian.net/browse/LCSV-26) 서버 인스턴스에 애플리케이션 클론

[LCSV-27](https://langchain.atlassian.net/browse/LCSV-27) .env의 key 업데이트

[LCSV-28](https://langchain.atlassian.net/browse/LCSV-28) pyenv 설치

[LCSV-29](https://langchain.atlassian.net/browse/LCSV-29) pyenv 환경변수 설정

[LCSV-30](https://langchain.atlassian.net/browse/LCSV-30) python 3.9.6 설치

[LCSV-31](https://langchain.atlassian.net/browse/LCSV-31) pip 설치

[LCSV-32](https://langchain.atlassian.net/browse/LCSV-32) pipenv 설치

[LCSV-33](https://langchain.atlassian.net/browse/LCSV-33) pipenv 의존성 업데이트

[LCSV-34](https://langchain.atlassian.net/browse/LCSV-34) 배포 서버에 Llama3.2 설치

[LCSV-35](https://langchain.atlassian.net/browse/LCSV-35) Fast API 서버 실행

[LCSV-37](https://langchain.atlassian.net/browse/LCSV-37) SSL/TLS 인증서 발급

[LCSV-38](https://langchain.atlassian.net/browse/LCSV-38) FastAPI 애플리케이션 실행 시 인증서 적용

### 스토리

[LCSV-15](https://langchain.atlassian.net/browse/LCSV-15) 클라이언트는 LLM 타입과 템플릿, 변수 목록, 시크릿 키를 전송해 LLM 서버를 이용할 수 있다

[LCSV-20](https://langchain.atlassian.net/browse/LCSV-20) 클라이언트는 Swagger 문서를 통해 LLM 서버 이용 가이드를 확인할 수 있다

[LCSV-24](https://langchain.atlassian.net/browse/LCSV-24) 클라이언트는 공용 엔드포인트를 통해 LLM 서버를 이용할 수 있다

[LCSV-36](https://langchain.atlassian.net/browse/LCSV-36) 클라이언트는 LLM 서버를 신뢰하고 요청을 암호화해 전송할 수 있다

### 에픽

[LCSV-1](https://langchain.atlassian.net/browse/LCSV-1) LLM API Server 구현

### 작업

[LCSV-2](https://langchain.atlassian.net/browse/LCSV-2) 초기 환경 설정

[LCSV-39](https://langchain.atlassian.net/browse/LCSV-39) README.md 추가
<br><br>

## 릴리스 정보 - LangChain Service - LlmApiServerRelease01/27-2

### 하위 작업

[LCSV-41](https://langchain.atlassian.net/browse/LCSV-41) LLM 서비스 응답을 토큰화하여 수신

[LCSV-42](https://langchain.atlassian.net/browse/LCSV-42) LLM 서비스 요청과 클라이언트 응답을 Streaming 방식으로 변경

### 에픽

[LCSV-1](https://langchain.atlassian.net/browse/LCSV-1) LLM API Server 구현

### 작업

[LCSV-39](https://langchain.atlassian.net/browse/LCSV-39) README.md 추가

[LCSV-40](https://langchain.atlassian.net/browse/LCSV-40) 클라이언트는 스트리밍을 통한 빠른 응답을 제공받을 수 있다
<br><br>

## 릴리스 정보 - LangChain Service - LlmApiServerRelease01/28

### 하위 작업

[LCSV-44](https://langchain.atlassian.net/browse/LCSV-44) SSE를 통해 서버로부터 토큰을 지속적으로 Push 받을 수 있는 엔드포인트\(/streaming/sse\) 추가

[LCSV-45](https://langchain.atlassian.net/browse/LCSV-45) 기존 엔드포인트의 리소스명을 streaming으로 변경

[LCSV-46](https://langchain.atlassian.net/browse/LCSV-46) 기존 엔드포인트와 추가된 엔드포인트의 공통 예외를 처리하기 위한 global\_exception\_handler 추가

[LCSV-48](https://langchain.atlassian.net/browse/LCSV-48) CORS 활성화

### 스토리

[LCSV-43](https://langchain.atlassian.net/browse/LCSV-43) 클라이언트는 엔드포인트로부터 최소 토큰 단위의 Stream 데이터를 지속적으로 Push 받을 수 있다

[LCSV-47](https://langchain.atlassian.net/browse/LCSV-47) 클라이언트는 브라우저를 통해 LLM 서버 엔드포인트를 이용할 수 있다

### 에픽

[LCSV-1](https://langchain.atlassian.net/browse/LCSV-1) LLM API Server 구현

### 작업

[LCSV-39](https://langchain.atlassian.net/browse/LCSV-39) README.md 추가
<br><br>

## 릴리스 정보 - LangChain Service - LlmApiServerRelease01/30

### 하위 작업

[LCSV-50](https://langchain.atlassian.net/browse/LCSV-50) API 키 발급

[LCSV-51](https://langchain.atlassian.net/browse/LCSV-51) ChatGoogle 패키지 설치

[LCSV-52](https://langchain.atlassian.net/browse/LCSV-52) gemini-1.5-pro 모델 적용

[LCSV-54](https://langchain.atlassian.net/browse/LCSV-54) API 키 발급

[LCSV-55](https://langchain.atlassian.net/browse/LCSV-55) SambaNovaCloud 패키지 설치

[LCSV-56](https://langchain.atlassian.net/browse/LCSV-56) Llama-3.3-70B-Instruct 모델 적용

[LCSV-57](https://langchain.atlassian.net/browse/LCSV-57) ChatOllama 패키지 제거

[LCSV-58](https://langchain.atlassian.net/browse/LCSV-58) ChatOllama 기반 Llama3.2 서비스 제거

[LCSV-59](https://langchain.atlassian.net/browse/LCSV-59) 기본 모델을 HCX-003에서 Llama3.3으로 변경

[LCSV-61](https://langchain.atlassian.net/browse/LCSV-61) LLM 서비스 인스턴스 생성 모듈 분리 -> llm\_generator

[LCSV-62](https://langchain.atlassian.net/browse/LCSV-62) 기본 모델 설정 함수 분리

[LCSV-63](https://langchain.atlassian.net/browse/LCSV-63) .env 파일의 환경변수 순서 정리

[LCSV-65](https://langchain.atlassian.net/browse/LCSV-65) API 키 발급

[LCSV-66](https://langchain.atlassian.net/browse/LCSV-66) ChatMistralAI 패키지 설치

[LCSV-67](https://langchain.atlassian.net/browse/LCSV-67) mistral-large-latest 모델 적용

[LCSV-68](https://langchain.atlassian.net/browse/LCSV-68) mistral-large-latest를 기본 모델로 사용하도록 변경

[LCSV-69](https://langchain.atlassian.net/browse/LCSV-69) Swagger 문서 업데이트

[LCSV-71](https://langchain.atlassian.net/browse/LCSV-71) variables 키를 options로 변경

[LCSV-72](https://langchain.atlassian.net/browse/LCSV-72) 0 ~ n 개의 여러 옵션들을 각각 키와 배열값 형태로 제공할 수 있도록 변경

[LCSV-73](https://langchain.atlassian.net/browse/LCSV-73) LLM 모델과 옵션을 전송하지 않아도 작동하도록 변경

[LCSV-74](https://langchain.atlassian.net/browse/LCSV-74) Swagger 문서 업데이트

### 스토리

[LCSV-49](https://langchain.atlassian.net/browse/LCSV-49) 클라이언트는 gemini-1.5-pro 모델 API를 사용할 수 있다

[LCSV-53](https://langchain.atlassian.net/browse/LCSV-53) 클라이언트는 ChatOllama 대신 SambaNovaCloud를 통해 Llama3.3 모델 API를 사용할 수 있다

[LCSV-64](https://langchain.atlassian.net/browse/LCSV-64) 클라이언트는 mistral-large 모델 API를 사용할 수 있다

[LCSV-70](https://langchain.atlassian.net/browse/LCSV-70) 사용자는 LLM 서비스 요청 시 여러 옵션들을 Key: Array Value 형태로 전송할 수 있다

### 에픽

[LCSV-1](https://langchain.atlassian.net/browse/LCSV-1) LLM API Server 구현

### 작업

[LCSV-39](https://langchain.atlassian.net/browse/LCSV-39) README.md 추가

[LCSV-60](https://langchain.atlassian.net/browse/LCSV-60) llm\_picker 모듈 리팩터링
<br><br>

## 릴리스 정보 - LangChain Service - LlmApiServerRelease02/10

### 하위 작업

[LCSV-77](https://langchain.atlassian.net/browse/LCSV-77) API 키 발급

[LCSV-78](https://langchain.atlassian.net/browse/LCSV-78) ChatAnthropic 패키지 설치

[LCSV-79](https://langchain.atlassian.net/browse/LCSV-79) claude-3-haiku 모델 적용

[LCSV-80](https://langchain.atlassian.net/browse/LCSV-80) Swagger 문서 업데이트

[LCSV-82](https://langchain.atlassian.net/browse/LCSV-82) API 키 발급

[LCSV-83](https://langchain.atlassian.net/browse/LCSV-83) ChatDeepSeek 패키지 설치

[LCSV-84](https://langchain.atlassian.net/browse/LCSV-84) deepseek-chat 모델 적용

[LCSV-85](https://langchain.atlassian.net/browse/LCSV-85) Swagger 문서 업데이트

[LCSV-87](https://langchain.atlassian.net/browse/LCSV-87) 모델 순서 변경

[LCSV-88](https://langchain.atlassian.net/browse/LCSV-88) Swagger 문서의 모델 목록 업데이트

[LCSV-89](https://langchain.atlassian.net/browse/LCSV-89) 일부 모델의 온도를 0.7로 조정

[LCSV-90](https://langchain.atlassian.net/browse/LCSV-90) 모든 모델의 최대 토큰 제한을 2,048개로 조정

[LCSV-91](https://langchain.atlassian.net/browse/LCSV-91) 클라이언트의 모델명 대소문자 입력에 영향 받지 않도록 변경

### 스토리

[LCSV-76](https://langchain.atlassian.net/browse/LCSV-76) 클라이언트는 Claude Haiku 모델 API를 사용할 수 있다

[LCSV-81](https://langchain.atlassian.net/browse/LCSV-81) 클라이언트는 DeepSeek V3 모델 API를 사용할 수 있다

[LCSV-86](https://langchain.atlassian.net/browse/LCSV-86) 전반적인 리팩터링

### 작업

[LCSV-39](https://langchain.atlassian.net/browse/LCSV-39) README.md 추가
<br><br>

## 릴리스 정보 - LangChain Service - LlmApiServerRelease02/21

### 하위 작업

[LCSV-93](https://langchain.atlassian.net/browse/LCSV-93) GPT API 유료 Product Key 발급

[LCSV-94](https://langchain.atlassian.net/browse/LCSV-94) GPT 유료 Product Key 적용

[LCSV-95](https://langchain.atlassian.net/browse/LCSV-95) gpt-3.5-turbo 모델 요청을 gpt-4o-mini 모델 요청으로 변경

[LCSV-96](https://langchain.atlassian.net/browse/LCSV-96) 유료 모델인 GPT 4o Mini 모델의 Secret Key 변경 \(SHA-256, Hash Value, 임의 시간의 nano second 변환\)

[LCSV-97](https://langchain.atlassian.net/browse/LCSV-97) GPT 모델 Secret Key 인증 실패에 대한 예외 처리 추가

[LCSV-98](https://langchain.atlassian.net/browse/LCSV-98) APScheduler 의존성 추가

[LCSV-99](https://langchain.atlassian.net/browse/LCSV-99) APScheduler를 통해 GPT 4o Mini 모델의 하루 이용 횟수를 1만 회로 제한

[LCSV-100](https://langchain.atlassian.net/browse/LCSV-100) GPT 모델 일일 사용량 한도 초과에 대한 예외 처리 추가

[LCSV-101](https://langchain.atlassian.net/browse/LCSV-101) GPT모델  사용 요청에 대한 로깅 추가

[LCSV-102](https://langchain.atlassian.net/browse/LCSV-102) Swagger 문서 업데이트

[LCSV-103](https://langchain.atlassian.net/browse/LCSV-103) 함수 구조 및 소스 재사용 관련한 전반적인 리팩터링

[LCSV-105](https://langchain.atlassian.net/browse/LCSV-105) 전체  LLM 응답을 반환하는 엔드포인트 추가

[LCSV-106](https://langchain.atlassian.net/browse/LCSV-106) 전체 LLM 응답 수신 시 문자열 데이터를 파싱해 클라이언트에게 JSON 포맷으로 응답하도록 설정

[LCSV-107](https://langchain.atlassian.net/browse/LCSV-107) 새로운 엔드포인트에 대한 Swagger 문서 추가

### 스토리

[LCSV-92](https://langchain.atlassian.net/browse/LCSV-92) 클라이언트는 GPT 4o Mini 모델 API를 사용할 수 있다

[LCSV-104](https://langchain.atlassian.net/browse/LCSV-104) 클라이언트는 요청에 대한 전체 LLM 데이터 응답을 반환하는 엔드포인트를 이용할 수 있다

### 에픽

[LCSV-1](https://langchain.atlassian.net/browse/LCSV-1) LLM API Server 구현

### 작업

[LCSV-39](https://langchain.atlassian.net/browse/LCSV-39) README.md 추가
<br><br>

## 릴리스 정보 - LangChain Service - LlmApiServerRelease02/22

### 하위 작업

[LCSV-109](https://langchain.atlassian.net/browse/LCSV-109) Google Cloud API Key 발급

[LCSV-110](https://langchain.atlassian.net/browse/LCSV-110) Google Custom Search Engine 생성

[LCSV-111](https://langchain.atlassian.net/browse/LCSV-111) 각 LLM 수신 데이터의 name 파라미터를 기반으로 Google Custom Search API 호출

[LCSV-112](https://langchain.atlassian.net/browse/LCSV-112) 수신한 이미지 URL을 원본 JSON 데이터의 파라미터로 각각 삽입

[LCSV-113](https://langchain.atlassian.net/browse/LCSV-113) 이미지 검색의 일일 이용 횟수를 100 회로 제한

[LCSV-114](https://langchain.atlassian.net/browse/LCSV-114) APScheduler를 통해 매일 자정에 일일 이용 횟수를 초기화하도록 설정

[LCSV-115](https://langchain.atlassian.net/browse/LCSV-115) 일일 사용 한도 초과 시 대체 이미지 삽입 후 전송하도록 설정

[LCSV-116](https://langchain.atlassian.net/browse/LCSV-116) GOOGLE\_IMAGE\_API\_KEY 환경변수 추가

[LCSV-117](https://langchain.atlassian.net/browse/LCSV-117) CUSTOM\_SEARCH\_ENGINE\_ID 환경변수 추가

[LCSV-118](https://langchain.atlassian.net/browse/LCSV-118) SEARCH\_URL 환경변수 추가

[LCSV-119](https://langchain.atlassian.net/browse/LCSV-119) DEFAULT\_IMAGE\_URL 환경변수 추가

[LCSV-122](https://langchain.atlassian.net/browse/LCSV-122) 스케줄러 모듈 분리 및 GPT와 이미지 일일 사용 한도 초기화 호출 로직 통합

[LCSV-123](https://langchain.atlassian.net/browse/LCSV-123) 전체 프로젝트의 importing 형식을 from ~ import 방식에서 상위 모듈 import 후 디렉토리 구조를 통해 참조하는 방식으로 변경

[LCSV-124](https://langchain.atlassian.net/browse/LCSV-124) .env 파일의 환경변수 정리

[LCSV-125](https://langchain.atlassian.net/browse/LCSV-125) routers 모듈의 로깅 인스턴스 변수명을 logger에서 log로 변경

[LCSV-126](https://langchain.atlassian.net/browse/LCSV-126) 스케줄러의 일일 사용량 초기화 시간을 Google Cloud 서버\(미국 서부\)의 초기화 시간에 맞춰 17시로 조정

### 스토리

[LCSV-108](https://langchain.atlassian.net/browse/LCSV-108) 클라이언트는 LLM의 응답과 해당 응답에 대한 이미지를 함께 수신할 수 있다

### 에픽

[LCSV-1](https://langchain.atlassian.net/browse/LCSV-1) LLM API Server 구현

### 작업

[LCSV-39](https://langchain.atlassian.net/browse/LCSV-39) README.md 추가

[LCSV-121](https://langchain.atlassian.net/browse/LCSV-121) 전반적인 리팩터링
