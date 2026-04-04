# Source: https://novita.ai/docs/guides/portkey.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Portkey

> Streamline AI development by using Portkey AI Gateway with Novita AI for fast, secure, and reliable performance.

Portkey AI Gateway transforms how developers work with AI models like Novita AI, providing a unified interface for seamless access to multiple language models with fast, secure, and reliable routing. This integration simplifies AI development and improves application performance.

This guide will walk you through setting up Portkey AI Gateway and then integrating Novita AI API with Portkey.

## How to Set Up Portkey AI Gateway

Setting up Portkey AI Gateway is simple and efficient, requiring just three key steps: configuring the gateway, sending your first request, and optimizing routing and guardrails for seamless performance.

### Step 1: Setup your AI Gateway

To run the gateway locally, ensure Node.js and npm are installed on your system. Once ready, execute the following command:

```jason  theme={"system"}
npx @portkey-ai/gateway
```

After the gateway starts, two key URLs will be displayed:

* The Gateway: `http://localhost:8787/v1`
* The Gateway Console: `http://localhost:8787/public/`

### Step 2: Make your first request

Begin by installing the Portkey AI Python library:

```python  theme={"system"}
pip install -qU portkey-ai
```

Next, execute the following Python code to send your first request:

```python  theme={"system"}
from portkey_ai import Portkey

# OpenAI compatible client
client = Portkey(
    provider="openai", # or 'anthropic', 'bedrock', 'groq', etc
    Authorization="sk-***" # the provider API key
)

# Make a request through your AI Gateway
client.chat.completions.create(
    messages=[{"role": "user", "content": "What's the weather like?"}],
    model="gpt-4o-mini"
)
```

Effortlessly monitor all your local logs in one centralized location using the Gateway Console at: `http://localhost:8787/public/`.

### Step 3: Routing & Guardrails

Portkey AI Gateway enables you to configure routing rules, add reliability features, and enforce guardrails. Below is an example configuration:

```python  theme={"system"}
config = {
  "retry": {"attempts": 5},

  "output_guardrails": [{
    "default.contains": {"operator": "none", "words": ["Apple"]},
    "deny": True
  }]
}

# Attach the config to the client
client = client.with_options(config=config)

client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Reply randomly with Apple or Bat"}]
)

# In this example, the guardrail denies all replies containing "Apple", so the response would always be "Bat". The retry configuration would attempt the request up to 5 times before giving up.
```

<Frame>
    <img src="https://mintcdn.com/novitaai/AUzGFUdz_qhrXjaJ/images/third-party/portkey-gateway.png?fit=max&auto=format&n=AUzGFUdz_qhrXjaJ&q=85&s=f871cd472dd92dfd665afc2a6889f4c8" alt="" width="1210" height="412" data-path="images/third-party/portkey-gateway.png" />
</Frame>

## How to Integrate Novita AI API with Portkey

To access the Novita AI API via the Portkey AI Gateway, follow these steps:

### Step 1: Install the Portkey SDK

Integrate the Portkey SDK into your application to seamlessly interact with Novita AI’s API through Portkey’s gateway.

**Node.JS**

```jason  theme={"system"}
npm install --save portkey-ai
```

**Python**

```python  theme={"system"}
pip install portkey-ai
```

### Step 2: Initialize Portkey with the Virtual Key

To integrate Novita AI with Portkey, retrieve your LLM API key from[ Novita AI ](https://novita.ai/settings/key-management)and add it to Portkey to generate the virtual key.

**Node.JS SDK**

```jason  theme={"system"}
import Portkey from 'portkey-ai'

const portkey = new Portkey({
  apiKey: "PORTKEY_API_KEY",  // Replace with your Portkey API key
  virtualKey: "VIRTUAL_KEY"   // Replace with your virtual key for Novita AI
})
```

**Python SDK**

```python  theme={"system"}
from portkey_ai import Portkey

portkey = Portkey(
    api_key="PORTKEY_API_KEY",  # Replace with your Portkey API key
    virtual_key="VIRTUAL_KEY"   # Replace with your virtual key for Novita AI
)
```

### Step 3: Invoke Chat Completions with Novita AI

Utilize the Portkey instance to send requests to Novita AI. If necessary, you can override the virtual key directly within the API call.

**Node.JS SDK**

```jason  theme={"system"}
const chatCompletion = await portkey.chat.completions.create({
  messages: [{ role: 'user', content: 'Say this is a test' }],
  model: 'Nous-Hermes-2-Mixtral-8x7B-DPO'
});

console.log(chatCompletion.choices);
```

**Python SDK**

```python  theme={"system"}
completion = portkey.chat.completions.create(
    messages= [{ "role": 'user', "content": 'Say this is a test' }],
    model= 'reka-core'
)

print(completion)
```


Built with [Mintlify](https://mintlify.com).