# Source: https://docs.anchorbrowser.io/agentic-browser-control/computer-use-agents/gemini.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Gemini Computer Use

> Use Google Gemini models for screenshot-based browser automation

Google's Gemini Computer Use agent (`gemini-computer-use`) enables AI-powered browser automation through visual understanding and multi-turn interactions.

## Overview

Gemini Computer Use leverages Google's multimodal AI capabilities to:

* Process and understand web page screenshots
* Plan and execute multi-step browser interactions
* Handle complex visual layouts and dynamic content
* Integrate with Google's AI ecosystem

## Supported Models

| Model                   | Model ID                                  | Best For                                  |
| ----------------------- | ----------------------------------------- | ----------------------------------------- |
| Gemini 2.5 Computer Use | `gemini-2.5-computer-use-preview-10-2025` | Screenshot-based automation **(default)** |

## Code Example

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  const anchorClient = new Anchorbrowser({
    apiKey: process.env.ANCHORBROWSER_API_KEY
  });

  const response = await anchorClient.agent.task(
    'Search for the latest AI news and summarize the top 3 articles',
    {
      taskOptions: {
        url: 'https://news.google.com',
        agent: 'gemini-computer-use',
        // model: 'gemini-2.5-computer-use-preview-10-2025',  // Default model
        maxSteps: 25,
        outputSchema: {
          type: 'object',
          properties: {
            articles: {
              type: 'array',
              items: {
                type: 'object',
                properties: {
                  title: { type: 'string' },
                  summary: { type: 'string' },
                  source: { type: 'string' }
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
      'Search for the latest AI news and summarize the top 3 articles',
      task_options={
          'url': 'https://news.google.com',
          'agent': 'gemini-computer-use',
          # 'model': 'gemini-2.5-computer-use-preview-10-2025',  # Default model
          'max_steps': 25,
          'output_schema': {
              'type': 'object',
              'properties': {
                  'articles': {
                      'type': 'array',
                      'items': {
                          'type': 'object',
                          'properties': {
                              'title': {'type': 'string'},
                              'summary': {'type': 'string'},
                              'source': {'type': 'string'}
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
| `agent`         | string  | Must be `gemini-computer-use`                                                    |
| `model`         | string  | Gemini model to use (default: `gemini-2.5-computer-use-preview-10-2025`)         |
| `url`           | string  | Starting URL for the task                                                        |
| `max_steps`     | integer | Maximum actions the agent can take                                               |
| `output_schema` | object  | JSON Schema for structured output                                                |
| `secret_values` | object  | Secure credentials (see [Secret Values](/agentic-browser-control/secret-values)) |

## Secure Credentials with Secret Values

Gemini Computer Use fully supports secret values for secure credential handling. Secrets are never exposed to the AI model.

<CodeGroup>
  ```javascript node.js theme={null}
  const response = await anchorClient.agent.task(
    'Login to the dashboard and download my latest report',
    {
      taskOptions: {
        url: 'https://app.example.com/login',
        agent: 'gemini-computer-use',
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
          'agent': 'gemini-computer-use',
          'secret_values': {
              'EMAIL': os.environ.get('APP_EMAIL'),
              'PASSWORD': os.environ.get('APP_PASSWORD')
          }
      }
  )
  ```
</CodeGroup>

Learn more about [domain-scoped secrets and TOTP support](/agentic-browser-control/secret-values).

## Best Practices

* **gemini-2.5-computer-use-preview is the default** - optimized for screenshot-based automation
* **Leverage structured output** with `output_schema` for reliable data extraction
* **Provide clear, specific prompts** describing the exact task to complete
