# Source: https://docs.anchorbrowser.io/agentic-browser-control/computer-use-agents/openai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI Computer Use

> Use OpenAI models with computer use capabilities for browser automation

OpenAI's Computer Use Agent (`openai-cua`) leverages GPT models with vision and reasoning capabilities for screenshot-based browser automation.

## Overview

OpenAI Computer Use provides:

* **Screenshot-based interactions** for visual understanding of web pages
* **Advanced reasoning** powered by GPT models
* **High accuracy** for complex web interactions
* **Structured outputs** for reliable data extraction

## Supported Models

| Model                | Model ID               | Best For                                  |
| -------------------- | ---------------------- | ----------------------------------------- |
| Computer Use Preview | `computer-use-preview` | Screenshot-based automation **(default)** |

## Code Example

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  const anchorClient = new Anchorbrowser({
    apiKey: process.env.ANCHORBROWSER_API_KEY
  });

  const response = await anchorClient.agent.task(
    'Find the pricing information and extract the plan details',
    {
      taskOptions: {
        url: 'https://example.com/pricing',
        agent: 'openai-cua',
        // model: 'computer-use-preview',  // Default model
        maxSteps: 25,
        outputSchema: {
          type: 'object',
          properties: {
            plans: {
              type: 'array',
              items: {
                type: 'object',
                properties: {
                  name: { type: 'string' },
                  price: { type: 'string' },
                  features: { type: 'array', items: { type: 'string' } }
                }
              }
            }
          }
        }
      }
    }
  );

  console.log(response);
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  anchor_client = Anchorbrowser(api_key=os.environ.get("ANCHORBROWSER_API_KEY"))

  response = anchor_client.agent.task(
      'Find the pricing information and extract the plan details',
      task_options={
          'url': 'https://example.com/pricing',
          'agent': 'openai-cua',
          # 'model': 'computer-use-preview',  # Default model
          'max_steps': 25,
          'output_schema': {
              'type': 'object',
              'properties': {
                  'plans': {
                      'type': 'array',
                      'items': {
                          'type': 'object',
                          'properties': {
                              'name': {'type': 'string'},
                              'price': {'type': 'string'},
                              'features': {'type': 'array', 'items': {'type': 'string'}}
                          }
                      }
                  }
              }
          }
      }
  )

  print(response)
  ```
</CodeGroup>

## Configuration Options

| Parameter       | Type    | Description                                                                      |
| --------------- | ------- | -------------------------------------------------------------------------------- |
| `agent`         | string  | Must be `openai-cua`                                                             |
| `model`         | string  | OpenAI model to use (default: `computer-use-preview`)                            |
| `url`           | string  | Starting URL for the task                                                        |
| `max_steps`     | integer | Maximum actions the agent can take                                               |
| `output_schema` | object  | JSON Schema for structured output                                                |
| `secret_values` | object  | Secure credentials (see [Secret Values](/agentic-browser-control/secret-values)) |

## Secure Credentials with Secret Values

OpenAI CUA fully supports secret values for secure credential handling. Secrets are never exposed to the AI model.

<CodeGroup>
  ```javascript node.js theme={null}
  const response = await anchorClient.agent.task(
    'Login to the dashboard and download my latest report',
    {
      taskOptions: {
        url: 'https://app.example.com/login',
        agent: 'openai-cua',
        secretValues: {
          EMAIL: process.env.APP_EMAIL,
          PASSWORD: process.env.APP_PASSWORD
        }
      }
    }
  );
  ```

  ```python python theme={null}
  response = anchor_client.agent.task(
      'Login to the dashboard and download my latest report',
      task_options={
          'url': 'https://app.example.com/login',
          'agent': 'openai-cua',
          'secret_values': {
              'EMAIL': os.environ.get('APP_EMAIL'),
              'PASSWORD': os.environ.get('APP_PASSWORD')
          }
      }
  )
  ```
</CodeGroup>

Learn more about [domain-scoped secrets and TOTP support](/agentic-browser-control/secret-values).
