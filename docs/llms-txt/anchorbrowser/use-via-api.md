# Source: https://docs.anchorbrowser.io/quickstart/use-via-api.md

# API Quick Start

Our APIs can be used directly (See our [API Reference](/api-reference)) or through integrations to automation platforms. We've created modules for our most commonly used API routes in each of the supported platforms.

Pick your preferred platform to view a quick-start for its usage:

<CardGroup cols={2}>
  <Card title="Direct API Usage" icon="code" href="/api-reference">
    Use the API directly as you like, See our [API Reference](/api-reference) for more details.
  </Card>

  <Card title="Browser-use Integration" icon="atom-simple" href="/integrations/browseruse-deployment">
    Enhance Browser-Use capabilities with Anchor tools and cloud-based browser sessions
  </Card>

  <Card title="Make Integration" icon="grid-round-2-plus" href="/integrations/make">
    Integrate with Make (formerly Integromat) for no-code automation
  </Card>

  <Card title="CrewAI Integration" icon="people-group" href="/agent-frameworks/crewai">
    Integrate with CrewAI to gain robust qualities of Anchor Browser implementing no-code automation.
  </Card>

  <Card title="Langchain Integration" icon="crow" href="/agent-frameworks/langchain">
    Integrate with Langchain to leverage Anchor Browser's browser tools in your LLM workflows.
  </Card>

  <Card title="Custom Integration" icon="palette" href="/agent-frameworks/custom-agent-framework">
    Integrate with your own platform to leverage Anchor Browser's in your automations.
  </Card>
</CardGroup>

## Quick API Examples

### Single Step Browser Tool Call

The easiest way to utilize Anchor Browser is through browser tools. Browser tools are API endpoints that wrap end-to-end browser functionality in a single API call.

<CodeGroup>
  ```bash curl theme={null}
  curl -X POST "https://api.anchorbrowser.io/v1/tools/perform-web-task" \
    -H "anchor-api-key: YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "task": "Go to anchorbrowser.io and click the Get Started button",
      "headless": false
    }'
  ```

  ```javascript node.js theme={null}
  const axios = require('axios');

  const response = await axios.post('https://api.anchorbrowser.io/v1/tools/perform-web-task', {
    task: 'Go to anchorbrowser.io and click the Get Started button',
    headless: false
  }, {
    headers: {
      'anchor-api-key': process.env.ANCHOR_API_KEY,
      'Content-Type': 'application/json'
    }
  });

  console.log(response.data);
  ```

  ```python python theme={null}
  import requests

  response = requests.post('https://api.anchorbrowser.io/v1/tools/perform-web-task', 
    json={
      'task': 'Go to anchorbrowser.io and click the Get Started button',
      'headless': False
    },
    headers={
      'anchor-api-key': os.getenv('ANCHOR_API_KEY'),
      'Content-Type': 'application/json'
    }
  )

  print(response.json())
  ```
</CodeGroup>

### Multi-Step Browser Flow

For use cases where a custom browser configuration is required, or a multi-step browser flow is needed:

<Steps>
  <Step title="Fetch API Key">
    In [Anchor UI](https://app.anchorbrowser.io/api-key), copy your API key
  </Step>

  <Step title="Create a session">
    [Create a session](/api-reference/browser-sessions/start-browser-session) with the desired configuration
  </Step>

  <Step title="Use tools on the created session">
    Perform [tool calls](/tools-api-reference/ai-tools/ask-webpage) while referencing the created session ID
  </Step>
</Steps>
