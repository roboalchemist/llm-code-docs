# Custom port
0g-compute-cli inference serve --provider <PROVIDER_ADDRESS> --port 8080
```

Then use any OpenAI-compatible client to connect to `http://localhost:3000`.

</TabItem>
<TabItem value="sdk" label="SDK">

**Best for:** Application integration and programmatic access

### Installation

```bash
pnpm add @0glabs/0g-serving-broker
```

:::tip Starter Kits Available
Get up and running quickly with our comprehensive TypeScript starter kit within minutes.

- **[TypeScript Starter Kit](https://github.com/0gfoundation/0g-compute-ts-starter-kit)** - Complete examples with TypeScript and CLI tool
:::

### Initialize the Broker

<Tabs>
<TabItem value="nodejs" label="Node.js" default>

```typescript
import { ethers } from "ethers";
import { createZGComputeNetworkBroker } from "@0glabs/0g-serving-broker";

// Choose your network
const RPC_URL = process.env.NODE_ENV === 'production'
  ? "https://evmrpc.0g.ai"  // Mainnet
  : "https://evmrpc-testnet.0g.ai";  // Testnet

const provider = new ethers.JsonRpcProvider(RPC_URL);
const wallet = new ethers.Wallet(process.env.PRIVATE_KEY!, provider);
const broker = await createZGComputeNetworkBroker(wallet);
```

</TabItem>
<TabItem value="browser" label="Browser">

```typescript
import { BrowserProvider } from "ethers";
import { createZGComputeNetworkBroker } from "@0glabs/0g-serving-broker";

// Check if MetaMask is installed
if (typeof window.ethereum === "undefined") {
  throw new Error("Please install MetaMask");
}

const provider = new BrowserProvider(window.ethereum);
const signer = await provider.getSigner();
const broker = await createZGComputeNetworkBroker(signer);
```

:::caution Browser Compatibility
`@0glabs/0g-serving-broker` requires polyfills for Node.js built-in modules.

**Vite example:**
```bash
pnpm add -D vite-plugin-node-polyfills
```

```javascript
// vite.config.js
import { nodePolyfills } from 'vite-plugin-node-polyfills';

export default {
  plugins: [
    nodePolyfills({
      include: ['crypto', 'stream', 'util', 'buffer', 'process'],
      globals: { Buffer: true, global: true, process: true }
    })
  ]
};
```
:::

</TabItem>
</Tabs>

### Discover Services

```typescript
// List all available services
const services = await broker.inference.listService();

// Filter by service type
const chatbotServices = services.filter(s => s.serviceType === 'chatbot');
const imageServices = services.filter(s => s.serviceType === 'text-to-image');
const speechServices = services.filter(s => s.serviceType === 'speech-to-text');
```

### Account Management

For detailed account operations, see [Account Management](./account-management).

```typescript
const account = await broker.ledger.getLedger();
await broker.ledger.depositFund(10);
// Required before first use of a provider
await broker.inference.acknowledgeProviderSigner(providerAddress);
```

### Make Inference Requests

<Tabs>
<TabItem value="chatbot-sdk" label="Chatbot" default>

```typescript
const messages = [{ role: "user", content: "Hello!" }];

// Get service metadata
const { endpoint, model } = await broker.inference.getServiceMetadata(providerAddress);

// Generate auth headers
const headers = await broker.inference.getRequestHeaders(
  providerAddress
);

// Make request
const response = await fetch(`${endpoint}/chat/completions`, {
  method: "POST",
  headers: { "Content-Type": "application/json", ...headers },
  body: JSON.stringify({ messages, model })
});

const data = await response.json();
const answer = data.choices[0].message.content;
```

</TabItem>
<TabItem value="text-to-image-sdk" label="Text-to-Image">

```typescript
const prompt = "A cute baby sea otter";

const body = JSON.stringify({
    model,
    prompt,
    n: 1,
    size: "1024x1024"
  });

// Get service metadata
const { endpoint, model } = await broker.inference.getServiceMetadata(providerAddress);

// Generate auth headers
const headers = await broker.inference.getRequestHeaders(
  providerAddress,
  body
);

// Make request
const response = await fetch(`${endpoint}/images/generations`, {
  method: "POST",
  headers: { "Content-Type": "application/json", ...headers },
  body: JSON.stringify({
    model,
    prompt,
    n: 1,
    size: "1024x1024"
  })
});

const data = await response.json();
const imageUrl = data.data[0].url;
```

</TabItem>
<TabItem value="speech-to-text-sdk" label="Speech-to-Text">

```typescript
const formData = new FormData();
formData.append('file', audioFile); // audioFile is a File or Blob
formData.append('model', model);
formData.append('response_format', 'json');

// Get service metadata
const { endpoint, model } = await broker.inference.getServiceMetadata(providerAddress);

// Generate auth headers
const headers = await broker.inference.getRequestHeaders(
  providerAddress
);

// Make request
const response = await fetch(`${endpoint}/audio/transcriptions`, {
  method: "POST",
  headers: { ...headers },
  body: formData
});

const data = await response.json();
const transcription = data.text;
```

</TabItem>
</Tabs>

### Response Verification

The `processResponse` method handles response verification and automatic fee management. Both parameters are optional:

- **`receivedContent`**: The usage data from the service response. When provided, the SDK caches accumulated usage and automatically transfers funds from your main account to the provider's sub-account to prevent service interruptions.
- **`chatID`**: Response identifier for verifiable TEE services. Different service types handle this differently.

<Tabs>
<TabItem value="chatbot-verify" label="Chatbot" default>

For chatbot services, pass the usage data from the response to enable automatic fee management:

```typescript
// Standard chat completion
const response = await fetch(`${endpoint}/chat/completions`, {
  method: "POST",
  headers: { "Content-Type": "application/json", ...headers },
  body: JSON.stringify({ messages, model })
});

const data = await response.json();

// Process response for automatic fee management
if (data.usage) {
  await broker.inference.processResponse(
    providerAddress,
    undefined,              // chatID is undefined for non-verifiable responses
    JSON.stringify(data.usage)  // Pass usage data for fee calculation
  );
}

// For verifiable TEE services with chatID
// Check response headers first
let chatID = response.headers.get("ZG-Res-Key") || response.headers.get("zg-res-key");

// If not found in response headers, check response body
if (!chatID) {
  chatID = data.id || data.chatID;
}

if (chatID) {
  const isValid = await broker.inference.processResponse(
    providerAddress,
    chatID,           // Verify the response integrity
    JSON.stringify(data.usage)  // Also manage fees
  );
}
```

</TabItem>
<TabItem value="text-to-image-verify" label="Text-to-Image">

For text-to-image services, pass the original request data for input-based fee calculation:

```typescript
const requestBody = {
  model,
  prompt: "A cute baby sea otter",
  size: "1024x1024",
  n: 1
};

const response = await fetch(`${endpoint}/images/generations`, {
  method: "POST",
  headers: { "Content-Type": "application/json", ...headers },
  body: JSON.stringify(requestBody)
});

const data = await response.json();

// Get chatID from response headers for verification
const chatID = response.headers.get("ZG-Res-Key") || response.headers.get("zg-res-key");

if (chatID) {
  // Process response with chatID for verification and fee calculation
  const isValid = await broker.inference.processResponse(
    providerAddress,
    chatID                        // Verify the response integrity
  );
  console.log("Response valid:", isValid);
} else {
  // Fallback: process without verification if no chatID
  await broker.inference.processResponse(
    providerAddress,
    undefined                     // No chatID available
  );
}
```

</TabItem>
<TabItem value="speech-to-text-verify" label="Speech-to-Text">

For speech-to-text services, pass the usage data if available:

```typescript
const formData = new FormData();
formData.append('file', audioFile);
formData.append('model', model);

const response = await fetch(`${endpoint}/audio/transcriptions`, {
  method: "POST",
  headers: { ...headers },
  body: formData
});

const data = await response.json();

// Get chatID from response headers for verification
const chatID = response.headers.get("ZG-Res-Key") || response.headers.get("zg-res-key");

if (chatID) {
  // Process response with chatID for verification and fee calculation
  const isValid = await broker.inference.processResponse(
    providerAddress,
    chatID,                      // Verify the response integrity
    JSON.stringify(data.usage || {}) // Pass usage for fee calculation
  );
  console.log("Response valid:", isValid);
} else if (data.usage) {
  // Fallback: process without verification if no chatID but usage available
  await broker.inference.processResponse(
    providerAddress,
    undefined,                   // No chatID available
    JSON.stringify(data.usage)   // Pass usage for fee calculation
  );
}
```

</TabItem>
<TabItem value="streaming-verify" label="Streaming Responses">

For streaming responses, handle chatID differently based on service type:

<Tabs>
<TabItem value="chatbot-stream" label="Chatbot Streaming" default>

```typescript
// For chatbot streaming, first check headers then try to get ID from stream
let chatID = response.headers.get("ZG-Res-Key") || response.headers.get("zg-res-key");

let usage = null;
let streamChatID = null; // Will try to get from stream data
const decoder = new TextDecoder();
const reader = response.body.getReader();

// Process stream
let rawBody = '';
while (true) {
  const { done, value } = await reader.read();
  if (done) break;

  rawBody += decoder.decode(value, { stream: true });
}

// Parse usage and chatID from stream data
for (const line of rawBody.split('\n')) {
  const trimmed = line.trim();
  if (!trimmed || trimmed === 'data: [DONE]') continue;

  try {
    const jsonStr = trimmed.startsWith('data:')
      ? trimmed.slice(5).trim()
      : trimmed;
    const message = JSON.parse(jsonStr);

    // For chatbot, try to get ID from stream data
    if (!streamChatID && (message.id || message.chatID)) {
      streamChatID = message.id || message.chatID;
    }

    if (message.usage) {
      usage = message.usage;
    }
  } catch {}
}

// Use chatID from header if available, otherwise use chatID from stream data
const finalChatID = chatID || streamChatID;

// Process with chatID for verification if available
if (finalChatID) {
  const isValid = await broker.inference.processResponse(
    providerAddress,
    finalChatID,
    JSON.stringify(usage || {})
  );
  console.log("Chatbot streaming response valid:", isValid);
} else if (usage) {
  // Fallback: process without verification
  await broker.inference.processResponse(
    providerAddress,
    undefined,
    JSON.stringify(usage)
  );
}
```

</TabItem>
<TabItem value="audio-stream" label="Speech-to-Text Streaming">

```typescript
// For speech-to-text streaming, get chatID from headers
const chatID = response.headers.get("ZG-Res-Key") || response.headers.get("zg-res-key");

let usage = null;
const decoder = new TextDecoder();
const reader = response.body.getReader();

// Process stream
let rawBody = '';
while (true) {
  const { done, value } = await reader.read();
  if (done) break;

  rawBody += decoder.decode(value, { stream: true });
}

// Parse usage from stream data
for (const line of rawBody.split('\n')) {
  const trimmed = line.trim();
  if (!trimmed || trimmed === 'data: [DONE]') continue;

  try {
    const jsonStr = trimmed.startsWith('data:')
      ? trimmed.slice(5).trim()
      : trimmed;
    const message = JSON.parse(jsonStr);
    if (message.usage) {
      usage = message.usage;
    }
  } catch {}
}

// Process with chatID for verification if available
if (chatID) {
  const isValid = await broker.inference.processResponse(
    providerAddress,
    chatID,
    JSON.stringify(usage || {})
  );
  console.log("Audio streaming response valid:", isValid);
} else if (usage) {
  // Fallback: process without verification
  await broker.inference.processResponse(
    providerAddress,
    undefined,
    JSON.stringify(usage)
  );
}
```

</TabItem>
</Tabs>

</TabItem>
</Tabs>

**Key Points:**
- Always call `processResponse` after receiving responses to maintain proper fee management
- The SDK automatically handles fund transfers to prevent service interruptions
- For verifiable TEE services, the method also validates response integrity
- **chatID retrieval principle**: Always prioritize `ZG-Res-Key` from response headers. Only use fallback methods when header is not present.
- **chatID retrieval varies by service type:**
  - **Chatbot**: First try `ZG-Res-Key` header, then check `data.id` (completion ID from response body) as fallback
  - **Text-to-Image & Speech-to-Text**: Always get chatID from `ZG-Res-Key` response header
  - **Streaming responses**:
    - **Chatbot streaming**: Check headers first, then try to get `id` from stream data as fallback
    - **Speech-to-text streaming**: Get chatID from `ZG-Res-Key` header immediately
- Usage data format varies by service type but typically includes token counts or request metrics

</TabItem>
</Tabs>

---

## Troubleshooting

### Common Issues

<details>
<summary>Error: Insufficient balance</summary>

Your account doesn't have enough funds. Add more using CLI or SDK:

CLI:

#### Deposit to Main Account
```bash
0g-compute-cli deposit --amount 5
```

#### Transfer to Provider Sub-Account
```bash
0g-compute-cli transfer-fund --provider <PROVIDER_ADDRESS> --amount 5
```

SDK:
```typescript
await broker.ledger.depositFund(1);
```
</details>

<details>
<summary>Error: Provider not acknowledged</summary>

You need to acknowledge the provider before using their service:

CLI:
```bash
0g-compute-cli inference acknowledge-provider --provider <PROVIDER_ADDRESS>
```

SDK:
```typescript
await broker.inference.acknowledgeProviderSigner(providerAddress);
```
</details>

<details>
<summary>Error: No funds in provider sub-account</summary>

Transfer funds to the specific provider sub-account:
```bash
0g-compute-cli transfer-fund --provider <PROVIDER_ADDRESS> --amount 5
```

Check your account balance:
```bash
0g-compute-cli get-account
```
</details>

<details>
<summary>Web UI not starting</summary>

If the web UI fails to start:

1. Check if another service is using port 3090:
```bash
0g-compute-cli ui start-web --port 3091
```

2. Ensure the package was installed globally:
```bash
pnpm add @0glabs/0g-serving-broker -g
```
</details>

## Next Steps

- **Manage Accounts** → [Account Management Guide](./account-management)
- **Fine-tune Models** → [Fine-tuning Guide](./fine-tuning)
- **Become a Provider** → [Provider Setup](./inference-provider)
- **View Examples** → [GitHub](https://github.com/0glabs/0g-compute-ts-starter-kit)

---

*Questions? Join our [Discord](https://discord.gg/0glabs) for support.*

---

## Marketplace (coming soon)

Coming soon

---

## Overview