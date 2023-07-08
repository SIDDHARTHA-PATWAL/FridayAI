import os
import openai
from config import apikey

#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key=apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email to my boss for resignation?",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)