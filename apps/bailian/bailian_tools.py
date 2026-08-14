from urllib import response

from langchain_core.tools import Tool
from langchain_core.prompts import ChatPromptTemplate
from apps.bailian.common import llm, chat_prompt

def add(a, b):
    return a + b

add_tool = Tool.from_function(
    func=add,
    name="add",
    description="将两个数字相加",
)

llm_with_tools = llm.bind_tools([add_tool])

chain = chat_prompt | llm_with_tools
response = chain.invoke(input={"role": "数学", "domain": "数学计算", "question": "100+100等于多少"})
# print(response)  # 输出: 200

for tool_calls in response.tool_calls:
    print(f"{tool_calls=}")
