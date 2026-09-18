# PowerTokens Python Examples

Python examples for building AI applications with the **PowerTokens unified AI API**.

**Unified API for Chinese AI models — no Chinese account required.** OpenAI-compatible.

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

## FAQ (common search questions)

### How do I call Qwen API without a Chinese account?

Use PowerTokens as an OpenAI-compatible gateway: set `base_url` to `https://api.powertokens.ai/v1`, use your PowerTokens API key, and pick a Qwen model id from the catalog (for example `qwen3-max`). You do **not** need a mainland China phone / Alibaba account.

- Code: [`chat/qwen3_max.py`](chat/qwen3_max.py)
- Docs: [Quickstart](https://docs.powertokens.ai/en/guides/powertokens-quickstart?utm_source=github&utm_medium=readme&utm_campaign=sdk-python-faq)
- Model page: [Models](https://www.powertokens.ai/en/models?utm_source=github&utm_medium=readme&utm_campaign=sdk-python-faq)

### What is the OpenAI-compatible base URL for GLM / MiniMax / DeepSeek?

```text
https://api.powertokens.ai/v1
```

Example model ids (always confirm in the live catalog):

- GLM: `glm-5.2`
- MiniMax: `MiniMax-M3`
- DeepSeek: `deepseek-v4-flash` or `deepseek-v3-2-251201` (prefer Flash / V3.2)

```python
client = OpenAI(
    api_key=os.environ["POWERTOKENS_API_KEY"],
    base_url="https://api.powertokens.ai/v1",
)
resp = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "Hello"}],
)
```

- Docs: [API key and model call](https://docs.powertokens.ai/en/guides/api-key-and-model-call?utm_source=github&utm_medium=readme&utm_campaign=sdk-python-faq)
- Protocols: [Text model protocols](https://docs.powertokens.ai/en/ecosystem-tools/text-model-protocols?utm_source=github&utm_medium=readme&utm_campaign=sdk-python-faq)

### PowerTokens vs OpenRouter for China-origin models?

Both can be OpenAI-compatible gateways. PowerTokens focuses on **China-origin model families** (Qwen, GLM, MiniMax, DeepSeek, Seed, video stacks) with **no Chinese mainland account** required and one unified key. Use the [model catalog](https://www.powertokens.ai/en/models?utm_source=github&utm_medium=readme&utm_campaign=sdk-python-faq) for current ids and pricing; see also [awesome-chinese-model-apis](https://github.com/PowerTokens/awesome-chinese-model-apis) for a neutral gateway comparison.

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
