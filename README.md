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
- DeepSeek: `deepseek-v3-2-251201`

```python
client = OpenAI(
    api_key=os.environ["POWERTOKENS_API_KEY"],
    base_url="https://api.powertokens.ai/v1",
)
resp = client.chat.completions.create(
    model="deepseek-v3-2-251201",
    messages=[{"role": "user", "content": "Hello"}],
)
```

- Docs: [API key and model call](https://docs.powertokens.ai/en/guides/api-key-and-model-call?utm_source=github&utm_medium=readme&utm_campaign=sdk-python-faq)
- Protocols: [Text model protocols](https://docs.powertokens.ai/en/ecosystem-tools/text-model-protocols?utm_source=github&utm_medium=readme&utm_campaign=sdk-python-faq)

### PowerTokens vs OpenRouter for China-origin models?

Both can be OpenAI-compatible gateways. PowerTokens focuses on **China-origin model families** (Qwen, GLM, MiniMax, DeepSeek, Seed, video stacks) with **no Chinese mainland account** required and one unified key. Use the [model catalog](https://www.powertokens.ai/en/models?utm_source=github&utm_medium=readme&utm_campaign=sdk-python-faq) for current ids and pricing; see also [awesome-chinese-model-apis](https://github.com/PowerTokens/awesome-chinese-model-apis) for a neutral gateway comparison.

### How do I call DeepSeek V3.2 with the OpenAI Python SDK?

Run `pip install openai`, create the client with your PowerTokens API key and `base_url="https://api.powertokens.ai/v1"`, then pass `model="deepseek-v3-2-251201"` to `chat.completions.create`. The code is the same as [`chat/qwen3_max.py`](chat/qwen3_max.py) with only the model id changed.

### Do I need a separate API key for each model?

No. One PowerTokens API key works for every model in the catalog, with no per-model binding, so switching between Qwen, GLM, MiniMax and DeepSeek V3.2 only means changing the `model` string ([create a key](https://docs.powertokens.ai/en/guides/api-key-and-model-call?utm_source=github&utm_medium=readme&utm_campaign=faq)).

### Does PowerTokens work with Claude Code or Codex?

Yes. Besides OpenAI Chat Completions (`/v1/chat/completions`), PowerTokens serves the Anthropic Messages format (`/v1/messages`) used by Claude Code and the OpenAI Responses format (`/v1/responses`) used by Codex; GLM models are not available on the Responses path ([protocol guide](https://docs.powertokens.ai/en/ecosystem-tools/text-model-protocols?utm_source=github&utm_medium=readme&utm_campaign=faq)). The docs have setup guides for [Claude Code](https://docs.powertokens.ai/en/ecosystem-tools/claude-code?utm_source=github&utm_medium=readme&utm_campaign=faq), [opencode](https://docs.powertokens.ai/en/ecosystem-tools/opencode?utm_source=github&utm_medium=readme&utm_campaign=faq), [Kilo Code](https://docs.powertokens.ai/en/ecosystem-tools/kilo-code?utm_source=github&utm_medium=readme&utm_campaign=faq), [Hermes Agent](https://docs.powertokens.ai/en/ecosystem-tools/hermes-agent?utm_source=github&utm_medium=readme&utm_campaign=faq) and [OpenClaw](https://docs.powertokens.ai/en/ecosystem-tools/openclaw?utm_source=github&utm_medium=readme&utm_campaign=faq).

### How do I pay for PowerTokens?

Add Credits on the Billing page with a credit card or PayPal; no Chinese bank account or payment app is needed. See the [quickstart](https://docs.powertokens.ai/en/guides/powertokens-quickstart?utm_source=github&utm_medium=readme&utm_campaign=faq).

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

**Start building** — [powertokens.ai](https://www.powertokens.ai/?utm_source=github&utm_medium=readme&utm_campaign=sdk-python). New-user bonus Credits are offered only while a promotion is running; otherwise add Credits on the Billing page.

Maintained by [@uselesssoso](https://github.com/uselesssoso) for [PowerTokens](https://powertokens.ai).
