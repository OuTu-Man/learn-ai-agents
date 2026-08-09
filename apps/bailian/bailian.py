from openai import OpenAI

from apps.common.utils import load_api_key


def main() -> None:
    client = OpenAI(
        api_key=load_api_key(key_name="BAILIAN_API_KEY"),
        base_url=load_api_key(key_name="BAILIAN_API_URL"),
    )

    messages = [{"role": "user", "content": "你是谁"}]
    completion = client.chat.completions.create(
        model=load_api_key(key_name="MODEL_NAME_QWEN36"),
        messages=messages,
        extra_body={"enable_thinking": True},
        stream=True,
    )
    is_answering = False  # 是否进入回复阶段
    print("\n" + "=" * 20 + "思考过程" + "=" * 20)
    for chunk in completion:
        if not chunk.choices:
            continue
        delta = chunk.choices[0].delta
        if hasattr(delta, "reasoning_content") and delta.reasoning_content is not None and not is_answering:
            print(delta.reasoning_content, end="", flush=True)
        if hasattr(delta, "content") and delta.content:
            if not is_answering:
                print("\n" + "=" * 20 + "完整回复" + "=" * 20)
                is_answering = True
            print(delta.content, end="", flush=True)


if __name__ == "__main__":
    main()
