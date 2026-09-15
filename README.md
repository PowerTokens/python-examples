# PowerTokens Python examples

> Unified API for Chinese AI models — **no Chinese account required**. OpenAI-compatible.

[Get started](https://www.powertokens.ai/?utm_source=github&utm_medium=readme&utm_campaign=sdk-python) · [Docs](https://docs.powertokens.ai/en/guides/powertokens-quickstart?utm_source=github&utm_medium=readme&utm_campaign=sdk-python) · [Models](https://www.powertokens.ai/en/models?utm_source=github&utm_medium=readme&utm_campaign=sdk-python)

## Install

```bash
pip install openai
```

## Quickstart

Base URL for OpenAI-compatible SDKs: `https://api.powertokens.ai/v1`  
(Platform docs list the host as `https://api.powertokens.ai`; chat calls go to `/v1/chat/completions`.)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["POWERTOKENS_API_KEY"],
    base_url="https://api.powertokens.ai/v1",
)

resp = client.chat.completions.create(
    model="MiniMax-M3",  # or qwen3-max, glm-5.2, etc. — see model catalog
    messages=[
        {"role": "system", "content": "You are a concise assistant."},
        {"role": "user", "content": "Describe Paris in one sentence."},
    ],
    temperature=0.3,
)
print(resp.choices[0].message.content)
```

Create an API key in the [dashboard](https://www.powertokens.ai/en/api-keys?utm_source=github&utm_medium=readme&utm_campaign=sdk-python).

## Why PowerTokens

- One API for Qwen, MiniMax, GLM, Seed, Kling-class video, and more
- No mainland China account required
- OpenAI-compatible — drop in existing SDKs / agents

## Links

- Website: https://www.powertokens.ai
- Docs: https://docs.powertokens.ai
- Discord: https://discord.gg/JtgtRdhJVS
