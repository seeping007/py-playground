#!/usr/bin/python3

import chatgpt
import os


def main():
    model = "gpt-3.5-turbo-0301"
    messages = [
        {"role": "user", "content": "What is the OpenAI mission? Response with one short sentence."}
    ]

    # token_count = chatgpt.num_tokens_from_messages(messages, model)
    # print(f"prompt tokens count: {token_count}")

    # chatgpt.chat_completion(messages)

    print(os.environ.get('OPENAI_API_KEY'))
    # chatgpt.test_handle_response()


if __name__ == '__main__':
    main()
