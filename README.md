# PowerTokens Python Examples

Python examples for building AI applications with the **PowerTokens unified AI API**.

PowerTokens provides an OpenAI-compatible API for accessing multiple AI model families through one API endpoint.

[Get started](https://www.powertokens.ai/?utm_source=github&utm_medium=readme&utm_campaign=sdk-python) · [Docs](https://docs.powertokens.ai/en/guides/powertokens-quickstart?utm_source=github&utm_medium=readme&utm_campaign=sdk-python) · [Models](https://www.powertokens.ai/en/models?utm_source=github&utm_medium=readme&utm_campaign=sdk-python)

## What you can build

- LLM and chat applications
- AI agents and developer tools
- Multi-model applications
- AI applications that use OpenAI-compatible SDKs

## Requirements

- Python 3.9+
- A PowerTokens API key
- The OpenAI Python SDK

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

- One API: access multiple AI model families through a unified API
- OpenAI-compatible: reuse familiar OpenAI SDK patterns
- Developer-focused: build and test applications without maintaining separate integrations for every provider

## Useful links

- Website: https://www.powertokens.ai
- Documentation: https://docs.powertokens.ai
- Model catalog: https://www.powertokens.ai/en/models
- API keys: https://www.powertokens.ai/en/api-keys
- Discord: https://discord.gg/JtgtRdhJVS
