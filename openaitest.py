import os
import openai
from config import apikey
openai.api_key = apikey

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "hello"
    },
    {
      "role": "assistant",
      "content": "Hi there! How can I assist you today?"
    },
    {
        "role": "user",
      "content": "I will call you sukuna"
    },
    {
      "content": "Sure, you can call me Sukuna. How can I help you today?",
      "role": "assistant"
    },
    {
      "role": "user",
      "content": "what will i call you now?"
    },
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
"""
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "You can call me Sukuna, just as you mentioned earlier. Is there something specific you need assistance with?",
        "role": "assistant"
      }
    }
  ],
  "created": 1697547796,
  "id": "chatcmpl-8Ae16LOnQVL4s8nencqVzTajzboZz",
  "model": "gpt-3.5-turbo-0613",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 22,
    "prompt_tokens": 63,
    "total_tokens": 85
  }
}
"""
