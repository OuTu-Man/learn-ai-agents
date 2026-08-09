from langchain_ollama.chat_models import ChatOllama

if __name__ == "__main__":
    print("Running Ollama script...")
    llm = ChatOllama(model="llama3.1:latest")
    msg = [
        ("system", "You are a helpful assistant."),
        ("human", "I love programming in Python. Can you give me some tips?"),
    ]
    resp = llm.invoke(input=msg)
    print(resp)
    # resp = llm.stream(messages=msg)
    # for item in resp:
    #     print(item.content, end="")
