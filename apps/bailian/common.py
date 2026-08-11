
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate, ChatPromptTemplate, FewShotPromptTemplate
from pydantic import SecretStr

from apps.common.utils import load_api_key


llm = ChatOpenAI(
    model=load_api_key(key_name="MODEL_NAME_QWEN38_MAX"),
    base_url=load_api_key(key_name="BAILIAN_API_URL"),
    api_key=SecretStr(load_api_key(key_name="BAILIAN_API_KEY")),
    streaming=True,
)


template_prompt = PromptTemplate.from_template("今天{something}真不错")

formatted_prompt = template_prompt.format(something="天气")

system_template = ChatPromptTemplate.from_template(template="你是一位{role}专家，擅长回答{domain}领域的问题。", role="system")
human_template = ChatPromptTemplate.from_template(template="用户问题：{question}", role="human")

chat_prompt = ChatPromptTemplate.from_messages([
    system_template,
    human_template
])