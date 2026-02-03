# Source: https://humanloop.com/docs/v4/api.md

# Source: https://humanloop.com/docs/api.md

# API

The Humanloop API allows you to interact with Humanloop and model providers programmatically.

You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.

<Accordion title="Install and initialize the SDK">

First you need to install and initialize the SDK. If you have already done this, skip to the next section.

Open up your terminal and follow these steps:

1. Install the Humanloop SDK:
<CodeBlock>
```python
pip install humanloop
```

```typescript
npm install humanloop
```
</CodeBlock>

2. Initialize the SDK with your Humanloop API key (you can get it from the [Organization Settings page](https://app.humanloop.com/account/api-keys)).
<CodeBlock>
```python
from humanloop import Humanloop
humanloop = Humanloop(api_key="<YOUR HUMANLOOP KEY>")

# Check that the authentication was successful
print(humanloop.prompts.list())
```

```typescript
import { HumanloopClient, Humanloop } from "humanloop";

const humanloop = new HumanloopClient({ apiKey: "YOUR_API_KEY" });

// Check that the authentication was successful
console.log(await humanloop.prompts.list());
```
</CodeBlock>

</Accordion>


Guides and further details about key concepts can be found in [our docs](/docs/getting-started/overview).
