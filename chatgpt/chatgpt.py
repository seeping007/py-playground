#!/usr/bin/python3

import tiktoken
import openai
import os
import common_util

DEFAULT_MODEL = "gpt-3.5-turbo-0301"


def chat_completion(messages):

    api_key = os.environ.get('OPENAI_API_KEY')
    if api_key is None:
        raise Exception('Invalid api_key')

    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model=DEFAULT_MODEL,
        messages=messages,
        temperature=0,
    )

    print(f'result: {handle_response(response)}')


def test_handle_response():
    resp = common_util.read_file_json('./mock/chatgpt_response.json')
    result = handle_response(resp)
    print(result)


######


def handle_response(response):
    message_list = []
    choices = response["choices"]
    for i in range(len(choices)):
        message = choices[i]['message']
        message_list.append(message)

    return {'usage': response['usage'], 'messages': message_list}


# https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301"):
    """Returns the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")

    if model == "gpt-3.5-turbo-0301":  # note: future models may deviate from this
        num_tokens = 0
        for message in messages:
            num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
                if key == "name":  # if there's a name, the role is omitted
                    num_tokens += -1  # role is always required and always 1 token
        num_tokens += 2  # every reply is primed with <im_start>assistant
        return num_tokens
    else:
        raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.
See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")
