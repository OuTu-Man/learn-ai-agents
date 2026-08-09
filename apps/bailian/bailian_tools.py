from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from pydantic import SecretStr

from apps.common.utils import load_api_key

llm = ChatOpenAI(
    model=load_api_key(key_name="MODEL_NAME_QWEN38_MAX"),
    base_url=load_api_key(key_name="BAILIAN_API_URL"),
    api_key=SecretStr(load_api_key(key_name="BAILIAN_API_KEY")),
    streaming=True,
)

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful assistant."),
#     ("user", "{input}"),
# ])

# template_prompt = PromptTemplate.from_template("今天{sth}真不错")
# formatted_prompt = template_prompt.format(sth="天气")
# print(formatted_prompt)

system_message = "你是一位{role}专家，擅长回答{domain}领域的问题。"
human_message = "{question}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", system_message),
    ("human", human_message)
])

# 格式化消息
formatted_messages = chat_prompt.format_messages(
    role="技术",
    domain="自动化测试",
    question="如何提高自动化测试的效率？"
)
print(formatted_messages)