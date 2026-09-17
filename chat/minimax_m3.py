"""Chat example: MiniMax-M3 via the OpenAI-compatible PowerTokens API."""

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["POWERTOKENS_API_KEY"],
    base_url="https://api.powertokens.ai/v1",
)

resp = client.chat.completions.create(
    model="MiniMax-M3",
    messages=[
        {"role": "system", "content": "You are a concise assistant."},
        {"role": "user", "content": "Describe Paris in one sentence."},
    ],
    temperature=0.3,
)
print(resp.choices[0].message.content)
