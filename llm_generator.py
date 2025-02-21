from langchain_anthropic import ChatAnthropic
from langchain_community.chat_models import ChatClovaX
from langchain_community.llms.sambanova import SambaNovaCloud
from langchain_deepseek import ChatDeepSeek
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai import ChatMistralAI
from langchain_openai import ChatOpenAI


def generate_samba_nova_cloud():
    return SambaNovaCloud(
        model="Meta-Llama-3.3-70B-Instruct",
        max_tokens=2_048,
        temperature=0.7,
        top_p=0.9,
        top_k=40
    )


def generate_chat_clova_x():
    return ChatClovaX(
        model="HCX-003",
        temperature=0.7,
        max_tokens=2_048,
        disable_streaming=False
    )


def generate_chat_google_generative_ai():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0.7,
        max_output_tokens=2_048
    )


def generate_chat_open_ai():
    return ChatOpenAI(
        temperature=0,
        model_name="gpt-4o-mini",
        streaming=True,
        max_tokens=2_048
    )


def generate_chat_anthropic():
    return ChatAnthropic(
        model='claude-3-haiku',
        temperature=0,
        max_tokens=2_048
    )


def generate_chat_deep_seek():
    return ChatDeepSeek(
        model="deepseek-chat",
        temperature=0,
        max_tokens=2_048,
        timeout=None,
        max_retries=2
    )


def generate_chat_mistral_ai():
    return ChatMistralAI(
        model="mistral-large-latest",
        temperature=0.7,
        max_tokens=2_048,
        max_retries=2
    )
