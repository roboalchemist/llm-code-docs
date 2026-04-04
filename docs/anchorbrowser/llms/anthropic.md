# Source: https://docs.anchorbrowser.io/agentic-browser-control/computer-use-agents/anthropic.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Anthropic Computer Use

> Use Claude models with native computer use capabilities for browser automation

Anthropic's Claude models with Computer Use capabilities enable AI agents to interact with web browsers through screenshots and native computer control actions.

## Overview

Anthropic Computer Use (`anthropic-cua`) leverages Claude's vision and reasoning capabilities to:

* Analyze screenshots of web pages
* Identify interactive elements
* Execute precise mouse and keyboard actions
* Complete complex multi-step workflows

## Supported Models

| Model             | Model ID                     | Best For                                                 |
| ----------------- | ---------------------------- | -------------------------------------------------------- |
| Claude Opus 4.5   | `claude-opus-4-5-20251101`   | Most advanced reasoning, complex workflows **(default)** |
| Claude Sonnet 4.5 | `claude-sonnet-4-5-20250929` | Balanced performance, general automation                 |
| Claude Opus 4     | `claude-opus-4-20250514`     | Advanced coding and agentic tasks                        |
| Claude Sonnet 4   | `claude-sonnet-4-20250514`   | Fast, reliable automation                                |

## Code Example

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  const anchorClient = new Anchorbrowser({
    apiKey: process.env.ANCHORBROWSER_API_KEY
  });

  const response = await anchorClient.agent.task(
    'Navigate to GitHub and find the anchorbrowser repository',
    {
      taskOptions: {
        url: 'https://github.com',
        agent: 'anthropic-cua',
        // model: 'claude-opus-4-5-20251101',  // Default model
        maxSteps: 30
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
      'Navigate to GitHub and find the anchorbrowser repository',
      task_options={
          'url': 'https://github.com',
          'agent': 'anthropic-cua',
          # 'model': 'claude-opus-4-5-20251101',  # Default model
          'max_steps': 30
      }
  )

  print(response)
  ```
</CodeGroup>

## Configuration Options

| Parameter       | Type    | Description                                                                      |
| --------------- | ------- | -------------------------------------------------------------------------------- |
| `agent`         | string  | Must be `anthropic-cua`                                                          |
| `model`         | string  | Claude model to use (default: `claude-opus-4-5-20251101`)                        |
| `url`           | string  | Starting URL for the task                                                        |
| `max_steps`     | integer | Maximum actions the agent can take                                               |
| `output_schema` | object  | JSON Schema for structured output                                                |
| `secret_values` | object  | Secure credentials (see [Secret Values](/agentic-browser-control/secret-values)) |

## Secure Credentials with Secret Values

Anthropic CUA fully supports secret values for secure credential handling. Secrets are never exposed to the AI model.

<CodeGroup>
  ```javascript node.js theme={null}
  const response = await anchorClient.agent.task(
    'Login to the dashboard and download my latest report',
    {
      taskOptions: {
        url: 'https://app.example.com/login',
        agent: 'anthropic-cua',
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
          'agent': 'anthropic-cua',
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

* **Opus 4.5 is the default** - most capable model for complex workflows
* **Use Sonnet 4.5** for faster automation when speed is important
* **Provide clear, specific prompts** describing the exact task to complete
