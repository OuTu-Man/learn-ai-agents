
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate, FewShotPromptTemplate
from pydantic import SecretStr

from apps.common.utils import load_api_key


llm = ChatOpenAI(
    model=load_api_key(key_name="MODEL_NAME_QWEN38_MAX"),
    base_url=load_api_key(key_name="BAILIAN_API_URL"),
    api_key=SecretStr(load_api_key(key_name="BAILIAN_API_KEY")),
    streaming=True,
)

# Prompt templates
template_prompt = PromptTemplate.from_template("今天{something}真不错")
formatted_prompt = template_prompt.format(something="天气")
print(formatted_prompt)  # 输出: 今天天气真不错

# Chat prompt templates
system_template = ChatPromptTemplate.from_template(template="你是一位{role}专家，擅长回答{domain}领域的问题。", role="system")
human_template = ChatPromptTemplate.from_template(template="用户问题：{question}", role="human")
chat_prompt = ChatPromptTemplate.from_messages([
    system_template,
    human_template
])
chat_prompt_messages = chat_prompt.format_messages(
    role="技术",
    domain="Web开发",
    question="如何构建一个基于Vue的前端应用?"
)
print(chat_prompt_messages)

# Few-shot prompt templates
example_template = "输入： {input}\n输出: {output}"
examples = [
    {"input": "将'Hello'翻译成中文", "output": "你好"},
    {"input": "将'Goodbye'翻译成中文", "output": "再见"},
]
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=PromptTemplate.from_template(example_template),
    prefix="你是一位翻译专家，请根据以下示例进行翻译：",
    suffix="输入：{input}\n输出: ",
    input_variables=["input"],
)
formatted_prompt = few_shot_prompt.format(input="将'Good morning'翻译成中文")
print(formatted_prompt)

chain = few_shot_prompt | llm
resp = chain.invoke({"input": "将'Good morning'翻译成中文"})
print(resp.content)  # 输出: 早上好
