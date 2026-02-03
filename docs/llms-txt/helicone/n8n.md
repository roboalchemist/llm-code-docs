# Source: https://docs.helicone.ai/gateway/integrations/n8n.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# n8n Integration

> Use the Helicone Chat Model node in n8n workflows to route LLM requests through the AI Gateway with full observability.

## Introduction

The Helicone Chat Model is a community node for [n8n](https://n8n.io/) that provides a LangChain-compatible interface for AI workflows. Route requests to any LLM provider through the Helicone AI Gateway.

<Note>
  This is an n8n community node that integrates seamlessly with n8n's AI chain functionality.
</Note>

## Prerequisites

* An n8n account (see [n8n installation docs](https://docs.n8n.io/hosting/) for setup options)
* A Helicone API key ([get one here](https://us.helicone.ai/settings/api-keys))

## Integration Steps

<Steps>
  <Step title="Install the Helicone community node">
    From your n8n interface:

    1. Click the **user menu** (bottom left corner)
    2. Select **Settings**
    3. Go to **Community Nodes**
    4. Click **Install a community node**
    5. Enter the package name: `n8n-nodes-helicone`
    6. Click **Install**

    Wait \~30 seconds for installation. The node will appear in your nodes panel.

    <Info>
      Learn more about installing community nodes in the [n8n documentation](https://docs.n8n.io/integrations/community-nodes/installation/).
    </Info>

        <img src="https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/install-node.webp?fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=fd158863923b5bc1f55f29c693590dcd" alt="n8n install community node" data-og-width="1216" width="1216" data-og-height="954" height="954" data-path="images/integrations/n8n/install-node.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/install-node.webp?w=280&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=b780385ccab5c1195d5d10c770a98031 280w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/install-node.webp?w=560&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=098db0df5da2cf22885de3362807075a 560w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/install-node.webp?w=840&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=c12ff38cca41d67f82a3ea33a8729463 840w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/install-node.webp?w=1100&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=e0f9157fb10a5d4e93f5b1241da74109 1100w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/install-node.webp?w=1650&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=32e15e1126c1e38cede61cbad27e4aed 1650w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/install-node.webp?w=2500&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=2185e7b3975e3bf3b9ff58b0368c909e 2500w" />
  </Step>

  <Step title="Configure Helicone credentials">
    Add your Helicone API key to n8n:

    1. Go to **Settings** → **Credentials**
    2. Click **Add Credential**
    3. Search for "Helicone" and select **Helicone LLM Observability**
    4. Enter your Helicone API key
    5. Click **Save**

        <img src="https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/credentials-tab.webp?fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=3872ecc182e76a01710d11184d828ecf" alt="n8n credentials tab" data-og-width="3172" width="3172" data-og-height="1654" height="1654" data-path="images/integrations/n8n/credentials-tab.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/credentials-tab.webp?w=280&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=33ae9efb35079672b9e06e3d50e02dcf 280w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/credentials-tab.webp?w=560&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=6ae0b62d9df132e36d3a437698f94fce 560w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/credentials-tab.webp?w=840&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=70dd0d698c71d99f114c2ea1c2ef7ef0 840w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/credentials-tab.webp?w=1100&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=654c2a69f694bbf061b04c3a3935a89b 1100w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/credentials-tab.webp?w=1650&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=29c67a6cc4a1860954d3e9f5330c6381 1650w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/credentials-tab.webp?w=2500&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=754e73f97a6da50af468ebbe6e9a9d7e 2500w" />
  </Step>

  <Step title="Add the Helicone Chat Model node to your workflow">
    1. Create a new workflow or open an existing one
    2. Click "+" to add a node
    3. Search for "Helicone Chat Model"
    4. Configure the node:
       * **Credentials**: Select your saved Helicone credentials
       * **Model**: Choose any model from the [model registry](https://helicone.ai/models) (e.g., `gpt-4.1-mini`, `claude-3-opus-20240229`)
       * **Options**: Configure temperature, max tokens, and other model parameters

        <img src="https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/search-node.webp?fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=d44f932a4fde7e43fa125363c285d92e" alt="n8n search for Helicone node" data-og-width="3162" width="3162" data-og-height="1852" height="1852" data-path="images/integrations/n8n/search-node.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/search-node.webp?w=280&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=e74db155ad359b6ffc7df7cb51b8c9fd 280w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/search-node.webp?w=560&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=a0f94d819ac2fcae74c9d6c766c97be5 560w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/search-node.webp?w=840&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=e88877e7902e59538ae0abe4934a10f2 840w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/search-node.webp?w=1100&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=082a5e1db12a1d877fef2d6189bed3dd 1100w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/search-node.webp?w=1650&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=225829ba88b7730353e7658378c5f6b7 1650w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/search-node.webp?w=2500&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=6fb62f2f5019823484ba1b32445fd3c7 2500w" />

    <Note>
      The Helicone Chat Model node outputs a LangChain-compatible model that can be used with other AI nodes in n8n.
    </Note>
  </Step>

  <Step title="Use in AI chains">
    The Helicone Chat Model node is designed to work with n8n's AI chain functionality:

    1. Connect the node to other AI nodes that accept `ai_languageModel` inputs
    2. Build complex AI workflows with Chat nodes, Chain nodes, and other AI processing nodes
    3. All requests are automatically logged to Helicone

    Example workflow:
    Chat Input → Helicone Chat Model → Chat Output

        <img src="https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/demo.webp?fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=84379c0b28b21cb73c57bdf267e14759" alt="n8n workflow example" data-og-width="3526" width="3526" data-og-height="2468" height="2468" data-path="images/integrations/n8n/demo.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/demo.webp?w=280&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=0102cabf9e07e229644e7091c86858d2 280w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/demo.webp?w=560&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=d55a61dbfec15238c9c82d6522cf736f 560w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/demo.webp?w=840&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=39e33e7107602192ccda79ab81f69312 840w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/demo.webp?w=1100&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=942cba0458647bd02fd136bed1f2bddd 1100w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/demo.webp?w=1650&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=01847acb9479b173e612db02e70bde35 1650w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/demo.webp?w=2500&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=7d695e0cbaef8547b1f43b75b7e0a902 2500w" />
  </Step>

  <Step title="View requests in Helicone dashboard">
    Open your [Helicone dashboard](https://us.helicone.ai/dashboard) to see:

    * All workflow requests logged automatically
    * Token usage and costs per request
    * Response time metrics
    * Full request/response bodies
    * Session tracking for multi-turn conversations
    * Custom properties for filtering and analysis

        <img src="https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/helicone-verify.webp?fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=51fa1b6b7be6534edd7c3669624f23fd" alt="Helicone dashboard verification" data-og-width="3094" width="3094" data-og-height="2464" height="2464" data-path="images/integrations/n8n/helicone-verify.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/helicone-verify.webp?w=280&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=b50e6747f4b36b8bc439adbb3fdc804b 280w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/helicone-verify.webp?w=560&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=6d0ddc1cb8c78177f74b4303ce186d3c 560w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/helicone-verify.webp?w=840&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=0b3d0bf03e31fa20e5bfce14a73ccedd 840w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/helicone-verify.webp?w=1100&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=297f6456174e626ed744723dab36d566 1100w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/helicone-verify.webp?w=1650&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=703f7c275c4b6d36971c66685a0419e3 1650w, https://mintcdn.com/helicone/cpApBw7nXGn2NYx2/images/integrations/n8n/helicone-verify.webp?w=2500&fit=max&auto=format&n=cpApBw7nXGn2NYx2&q=85&s=8c45fffa4d7cf4f6486ad2313100d26e 2500w" />

    <Tip>
      While you're here, why not <a href="https://github.com/helicone/helicone" target="_blank" rel="noreferrer">give us a star on GitHub</a>? It helps us a lot!
    </Tip>
  </Step>
</Steps>

## Node Configuration

### Required Parameters

* **Model**: Any model supported by Helicone AI Gateway.
  Examples: `gpt-4.1-mini`, `claude-opus-4-1`, `gemini-2.5-flash-lite`.
  See all models in the [Helicone's model registry](https://helicone.ai/models)

### Model Options

* **Temperature** (0-2): Controls randomness in responses
* **Max Tokens**: Maximum tokens to generate
* **Top P** (0-1): Nucleus sampling parameter
* **Frequency Penalty** (-2 to 2): Reduces repetition
* **Presence Penalty** (-2 to 2): Encourages new topics
* **Response Format**: Text or JSON
* **Timeout**: Request timeout in milliseconds
* **Max Retries**: Number of retry attempts on failure

## Example Workflows

### Basic Chat Workflow

```
[Chat Input] → [Helicone Chat Model] → [Chat Output]
```

1. Add a **Chat Input** node (triggers on user message)
2. Add the **Helicone Chat Model** node
   * Model: `gpt-4.1-mini`
   * Temperature: 0.7
3. Add a **Chat Output** node to display the response

### Multi-Step AI Chain

```
[Webhook] → [Helicone Chat Model] → [Extract Data] → [Helicone Chat Model] → [Response]
```

1. Receive data via webhook
2. First Helicone Chat Model analyzes the input
3. Extract structured data
4. Second Helicone Chat Model generates a response
5. Both requests appear in Helicone dashboard with session tracking

### Workflow with Custom Properties

Configure the node with custom properties to track workflow metadata:

1. Open the **Helicone Chat Model** node
2. Expand **Helicone Options** → **Custom Properties**
3. Add a JSON object:

```json  theme={null}
{
  "workflow_name": "customer-onboarding",
  "environment": "production",
  "version": "2.1.0"
}
```

All requests from this node will include these properties in Helicone.

## Troubleshooting

### Node Installation Issues

* **Node not appearing**: Wait 30 seconds after installation, then refresh n8n
* **Installation failed**: Check your n8n instance has internet access
* **Version conflicts**: Ensure you're running a compatible n8n version (>= 1.0)

### Authentication Errors

* **Invalid API key**: Verify your Helicone API key starts with `sk-helicone-`
* **403 Forbidden**: Ensure your API key has write access enabled
* **Provider not configured**: Check the name of the model is exactly the [model ID expected by the gateway](https://helicone.ai/models). If you've added your own provider keys, make sure they are correctly set in [your Helicone dashboard](https://us.helicone.ai/settings/providers)

### Model Errors

* **Model not found**: Check the exact model name at [Helicone's model registry](https://helicone.ai/models)
* **Model unavailable**: Verify provider access in your Helicone account
* **Different naming**: Providers use different conventions (e.g., OpenAI uses `gpt-4o-mini`, while the gateway uses `gpt-4.1-mini`)

### Getting Help

* [n8n Community Forum](https://community.n8n.io/)
* [Helicone Documentation](https://docs.helicone.ai)
* [Helicone Discord](https://discord.gg/7aSCGCGUeu)
* [GitHub Repository](https://github.com/Helicone/n8n-nodes-helicone)

<Note title="Request a Helicone Integration" type="info">
  Looking for a framework or tool not listed here? [Request it here!](https://forms.gle/E9GYKWevh6NGDdDj7)
</Note>

## Related Documentation

<CardGroup cols={2}>
  <Card title="AI Gateway Overview" icon="arrow-progress" href="/gateway/overview">
    Learn about Helicone's AI Gateway features and capabilities
  </Card>

  <Card title="Provider Routing" icon="route" href="/gateway/provider-routing">
    Configure intelligent routing and automatic failover
  </Card>

  <Card title="Model Registry" icon="database" href="https://helicone.ai/models">
    Browse all available models and providers
  </Card>

  <Card title="Gateway Features" icon="sparkles" href="/gateway/gateway-features">
    Explore caching, session tracking, and more
  </Card>

  <Card title="Custom Properties" icon="tags" href="/features/advanced-usage/custom-properties">
    Add metadata to track and filter your requests
  </Card>

  <Card title="Sessions" icon="link" href="/features/sessions">
    Track multi-turn conversations and user sessions
  </Card>
</CardGroup>
