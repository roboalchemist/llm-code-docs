# 0G Compute Inference

0G Compute Network provides decentralized AI inference services, supporting various AI models including Large Language Models (LLM), text-to-image generation, and speech-to-text processing.

## Prerequisites

- Node.js >= 22.0.0
- A wallet with 0G tokens (either testnet or mainnet)
- EVM compatible wallet (for Web UI)

## Supported Service Types

- **Chatbot Services**: Conversational AI with models like GPT, DeepSeek, and others
- **Text-to-Image**: Generate images from text descriptions using Stable Diffusion and similar models
- **Speech-to-Text**: Transcribe audio to text using Whisper and other speech recognition models

## Available Services

:::info Testnet Services

<details>
<summary>View Testnet Services (2 Available)</summary>

| # | Model | Type | Provider | Input (per 1M tokens) | Output (per 1M tokens) |
|---|-------|------|----------|----------------------|------------------------|
| 1 | `qwen-2.5-7b-instruct` | Chatbot | `0xa48f01...` | 0.05 0G | 0.10 0G |
| 2 | `qwen-image-edit-2511` | Image-Edit | `0x4b2a9...` | - | 0.005 0G/image |

**Available Models by Type:**

**Chatbots (1 model):**
- **Qwen 2.5 7B Instruct**: Fast and efficient conversational model

**Image-Edit (1 model):**
- **Qwen Image Edit 2511**: Advanced image editing and manipulation model

All testnet services feature TeeML verifiability and are ideal for development and testing.

</details>

:::

:::tip Mainnet Services

<details>
<summary>View Mainnet Services (6 Available)</summary>

| # | Model | Type | Provider | Input (per 1M tokens) | Output (per 1M tokens) |
|---|-------|------|----------|----------------------|------------------------|
| 1 | `GLM-5-FP8` | Chatbot | `0xd9966e...` | 1 0G | 3.2 0G |
| 2 | `deepseek-chat-v3-0324` | Chatbot | `0x1B3AAe...` | 0.30 0G | 1.00 0G |
| 3 | `gpt-oss-120b` | Chatbot | `0xBB3f5b...` | 0.10 0G | 0.49 0G |
| 4 | `qwen3-vl-30b-a3b-instruct` | Chatbot | `0x4415ef...` | 0.49 0G | 0.49 0G |
| 5 | `whisper-large-v3` | Speech-to-Text | `0x36aCff...` | 0.05 0G | 0.11 0G |
| 6 | `z-image` | Text-to-Image | `0xE29a72...` | - | 0.003 0G/image |

**Available Models by Type:**

**Chatbots (4 models):**
- **GLM-5-FP8**: High-performance reasoning model (FP8 quantized)
- **GPT-OSS-120B**: Large-scale open-source GPT model
- **Qwen3 VL 30B A3B Instruct**: Vision-language multimodal model
- **DeepSeek Chat V3**: Optimized conversational model

**Speech-to-Text (1 model):**
- **Whisper Large V3**: OpenAI's state-of-the-art transcription model

**Text-to-Image (1 model):**
- **Z-Image**: Fast high-quality image generation

All mainnet services feature TeeML verifiability for trusted execution in production environments.

</details>

:::

## Choose Your Interface

| Feature | Web UI | CLI | SDK |
|---------|--------|-----|-----|
| Setup time | ~1 min | ~2 min | ~5 min |
| Interactive chat | ✅ | ❌ | ❌ |
| Automation | ❌ | ✅ | ✅ |
| App integration | ❌ | ❌ | ✅ |
| Direct API access | ❌ | ❌ | ✅ |

<Tabs>
<TabItem value="web-ui" label="Web UI" default>

**Best for:** Quick testing, experimentation and direct frontend integration.

### Option 1: Use the Hosted Web UI

Visit the official 0G Compute Marketplace directly — no installation required:

**[https://compute-marketplace.0g.ai/inference](https://compute-marketplace.0g.ai/inference)**

### Option 2: Run Locally

#### Installation

```bash
pnpm add @0glabs/0g-serving-broker -g
```

#### Launch Web UI

```bash
0g-compute-cli ui start-web
```

Open `http://localhost:3090` in your browser.

### Getting Started

#### 1. Connect & Fund

1. **Connect your wallet** (MetaMask recommended)
2. **Deposit some 0G tokens** using the account dashboard
3. **Browse available AI models** and their pricing

#### 2. Start Using AI Services

**Option A: Chat Interface**
- Click "Chat" on any chatbot provider
- Start conversations immediately
- Perfect for testing and experimentation

**Option B: Get API Integration**
- Click "Build" on any provider
- Get step-by-step integration guides
- Copy-paste ready code examples

</TabItem>
<TabItem value="cli" label="CLI">

**Best for:** Automation, scripting, and server environments

### Installation

```bash
pnpm add @0glabs/0g-serving-broker -g
```

### Setup Environment

#### Choose Network

```bash
0g-compute-cli setup-network
```

#### Login with Wallet

Enter your wallet private key when prompted. This will be used for account management and service payments.

```bash
0g-compute-cli login
```

### Create Account & Add Funds

Before using inference services, you need to fund your account. For detailed account management, see [Account Management](./account-management).

```bash
0g-compute-cli deposit --amount 10
0g-compute-cli get-account
0g-compute-cli transfer-fund --provider <PROVIDER_ADDRESS> --amount 5
```

### CLI Commands

#### List Providers
```bash
0g-compute-cli inference list-providers
```

#### Verify Provider
Check provider's TEE attestation and reliability before using:
```bash
0g-compute-cli inference verify --provider <PROVIDER_ADDRESS>
```

This command outputs the provider's report and verifies their Trusted Execution Environment (TEE) status.

#### Acknowledge Provider
Before using a provider, acknowledge them on-chain:
```bash
0g-compute-cli inference acknowledge-provider --provider <PROVIDER_ADDRESS>
```

#### Direct API Access
Generate an authentication token for direct API calls:
```bash
0g-compute-cli inference get-secret --provider <PROVIDER_ADDRESS>
```

This generates a Bearer token in the format `app-sk-<SECRET>` that you can use for direct API calls.

### API Usage Examples

<Tabs>
<TabItem value="chatbot" label="Chatbot" default>

Use for conversational AI and text generation.

<Tabs>
<TabItem value="curl-chat" label="cURL" default>

```bash
curl <service_url>/v1/proxy/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer app-sk-<YOUR_SECRET>" \
  -d '{
    "model": <service.model>,
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Hello!"
      }
    ]
  }`
```

</TabItem>
<TabItem value="js-chat" label="JavaScript">

```javascript
const OpenAI = require('openai');

const client = new OpenAI({
  baseURL: `${service.url}/v1/proxy`,
  apiKey: 'app-sk-<YOUR_SECRET>'
});

const completion = await client.chat.completions.create({
  model: service.model,
  messages: [
    {
      role: 'system',
      content: 'You are a helpful assistant.'
    },
    {
      role: 'user',
      content: 'Hello!'
    }
  ]
});

console.log(completion.choices[0].message);
```

</TabItem>
<TabItem value="python-chat" label="Python">

```python
from openai import OpenAI

client = OpenAI(
    base_url=`${service.url}/v1/proxy`,
    api_key='app-sk-<YOUR_SECRET>'
)

completion = client.chat.completions.create(
    model=service.model,
    messages=[
        {
            'role': 'system',
            'content': 'You are a helpful assistant.'
        },
        {
            'role': 'user',
            'content': 'Hello!'
        }
    ]
)

print(completion.choices[0].message)
```

</TabItem>
</Tabs>

</TabItem>
<TabItem value="text-to-image" label="Text-to-Image">

Generate images from text descriptions.

<Tabs>
<TabItem value="curl-image" label="cURL" default>

```bash
curl <service_url>/v1/proxy/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer app-sk-<YOUR_SECRET>" \
  -d '{
    "model": <service.model>,
    "prompt": "A cute baby sea otter playing in the water",
    "n": 1,
    "size": "1024x1024"
  }'
```

</TabItem>
<TabItem value="js-image" label="JavaScript">

```javascript
const OpenAI = require('openai');

const client = new OpenAI({
  baseURL: `${service.url}/v1/proxy`,
  apiKey: 'app-sk-<YOUR_SECRET>'
});

const response = await client.images.generate({
  model: service.model,
  prompt: 'A cute baby sea otter playing in the water',
  n: 1,
  size: '1024x1024'
});

console.log(response.data);
```

</TabItem>
<TabItem value="python-image" label="Python">

```python
from openai import OpenAI

client = OpenAI(
    base_url=`${service.url}/v1/proxy`,
    api_key='app-sk-<YOUR_SECRET>'
)

response = client.images.generate(
    model=service.model,
    prompt='A cute baby sea otter playing in the water',
    n=1,
    size='1024x1024'
)

print(response.data)
```

</TabItem>
</Tabs>

</TabItem>
<TabItem value="speech-to-text" label="Speech-to-Text">

Transcribe audio files to text.

<Tabs>
<TabItem value="curl-audio" label="cURL" default>

```bash
curl <service_url>/v1/proxy/audio/transcriptions \
  -H "Authorization: Bearer app-sk-<YOUR_SECRET>" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@audio.ogg" \
  -F "model=whisper-large-v3" \
  -F "response_format=json"
```

</TabItem>
<TabItem value="js-audio" label="JavaScript">

```javascript
const OpenAI = require('openai');
const fs = require('fs');

const client = new OpenAI({
  baseURL: `${service.url}/v1/proxy`,
  apiKey: 'app-sk-<YOUR_SECRET>'
});

const transcription = await client.audio.transcriptions.create({
  file: fs.createReadStream('audio.ogg'),
  model: 'whisper-large-v3',
  response_format: 'json'
});

console.log(transcription.text);
```

</TabItem>
<TabItem value="python-audio" label="Python">

```python
from openai import OpenAI

client = OpenAI(
    base_url=`${service.url}/v1/proxy`,
    api_key='app-sk-<YOUR_SECRET>'
)

with open('audio.ogg', 'rb') as audio_file:
    transcription = client.audio.transcriptions.create(
        file=audio_file,
        model='whisper-large-v3',
        response_format='json'
    )

print(transcription.text)
```

</TabItem>
</Tabs>

</TabItem>
</Tabs>

### Start Local Proxy Server

Run a local OpenAI-compatible server:
```bash