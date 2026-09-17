# PowerTokens Python Examples

Python examples for building AI applications with the **PowerTokens unified AI API**.

**Unified API for video, image, audio, and LLMs — no Chinese account required.** OpenAI-compatible.

[Get started](https://www.powertokens.ai/?utm_source=github&utm_medium=readme&utm_campaign=sdk-python) · [Docs](https://docs.powertokens.ai/en/guides/powertokens-quickstart?utm_source=github&utm_medium=readme&utm_campaign=sdk-python) · [Models](https://www.powertokens.ai/en/models?utm_source=github&utm_medium=readme&utm_campaign=sdk-python)

## Examples

| Example | Model | Path |
|---------|-------|------|
| MiniMax chat | `MiniMax-M3` | [`chat/minimax_m3.py`](chat/minimax_m3.py) |
| Qwen chat | `qwen3-max` | [`chat/qwen3_max.py`](chat/qwen3_max.py) |
| GLM chat | `glm-5.2` | [`chat/glm_5_2.py`](chat/glm_5_2.py) |

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

```bash
export POWERTOKENS_API_KEY=your_key
python chat/minimax_m3.py
# or: python chat/qwen3_max.py
# or: python chat/glm_5_2.py
```

Equivalent SDK snippet:

```python
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
```

Create an API key in the [dashboard](https://www.powertokens.ai/en/api-keys?utm_source=github&utm_medium=readme&utm_campaign=sdk-python).

## Why PowerTokens

- One API: video, image, audio, and LLM model families
- OpenAI-compatible: reuse familiar OpenAI SDK patterns
- No Chinese mainland account required

## Useful links

- Website: [powertokens.ai](https://www.powertokens.ai/?utm_source=github&utm_medium=readme&utm_campaign=sdk-python)
- Documentation: [docs.powertokens.ai](https://docs.powertokens.ai/?utm_source=github&utm_medium=readme&utm_campaign=sdk-python)
- Model catalog: [Models](https://www.powertokens.ai/en/models?utm_source=github&utm_medium=readme&utm_campaign=sdk-python)
- API keys: [API keys](https://www.powertokens.ai/en/api-keys?utm_source=github&utm_medium=readme&utm_campaign=sdk-python)
- Discord: https://discord.gg/JtgtRdhJVS

**Get free credits to start building** — [powertokens.ai](https://www.powertokens.ai/?utm_source=github&utm_medium=readme&utm_campaign=sdk-python)
