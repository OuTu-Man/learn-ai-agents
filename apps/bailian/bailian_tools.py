import sys
from pathlib import Path

from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from apps.common.utils import load_api_key

llm = ChatOpenAI(
    model = load_api_key(key_name="MODEL_NAME_QWEN38_MAX"),  # 您可以按需更换为其它深度思考模型
    base_url=load_api_key(key_name="BAILIAN_API_URL"),
    api_key=SecretStr(load_api_key(key_name="BAILIAN_API_KEY")),
    streaming=True,
)
print("llm:", llm)