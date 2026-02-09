# Source: https://docs.anchorbrowser.io/agentic-browser-control/secret-values.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Secret Values

> Securely pass credentials and sensitive data to AI agents

Secret values allow you to securely pass credentials, API keys, and other sensitive data to AI agents during task execution. These values are automatically handled at type-time, never logged, and never exposed to the AI model.

Secret values work with all agent types: `browser-use`, `openai-cua`, `anthropic-cua`, and `gemini-computer-use`.

## Basic Usage

Pass credentials as key-value pairs in `secretValues`. The agent will securely use these values when logging into websites or filling forms.

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  const anchorClient = new Anchorbrowser({
    apiKey: process.env.ANCHORBROWSER_API_KEY
  });

  const response = await anchorClient.agent.task(
    'Login to LinkedIn and send a connection request to the Anchorbrowser team',
    {
      taskOptions: {
        url: 'https://linkedin.com',
        secretValues: {
          LINKEDIN_EMAIL: process.env.LINKEDIN_EMAIL,
          LINKEDIN_PASSWORD: process.env.LINKEDIN_PASSWORD
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
      'Login to LinkedIn and send a connection request to the Anchorbrowser team',
      task_options={
          'url': 'https://linkedin.com',
          'secret_values': {
              'LINKEDIN_EMAIL': os.environ.get('LINKEDIN_EMAIL'),
              'LINKEDIN_PASSWORD': os.environ.get('LINKEDIN_PASSWORD')
          }
      }
  )

  print(response)
  ```
</CodeGroup>

<Tip>
  Secret values are the recommended way to handle any sensitive data in AI agent tasks. Never include credentials directly in prompts.
</Tip>

## Domain-Scoped Secrets

For enhanced security, you can scope secrets to specific domains. Secrets will only be available when the browser is on a matching domain - preventing credential exposure on the wrong site.

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  const anchorClient = new Anchorbrowser({
    apiKey: process.env.ANCHORBROWSER_API_KEY
  });

  const response = await anchorClient.agent.task(
    'Login to LinkedIn, then login to Gmail and check my inbox',
    {
      taskOptions: {
        url: 'https://linkedin.com',
        agent: 'anthropic-cua',
        secretValues: {
          // Only available on linkedin.com
          '*.linkedin.com': {
            LINKEDIN_EMAIL: process.env.LINKEDIN_EMAIL,
            LINKEDIN_PASSWORD: process.env.LINKEDIN_PASSWORD
          },
          // Only available on google.com
          '*.google.com': {
            GOOGLE_EMAIL: process.env.GOOGLE_EMAIL,
            GOOGLE_PASSWORD: process.env.GOOGLE_PASSWORD
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
      'Login to LinkedIn, then login to Gmail and check my inbox',
      task_options={
          'url': 'https://linkedin.com',
          'agent': 'anthropic-cua',
          'secret_values': {
              # Only available on linkedin.com
              '*.linkedin.com': {
                  'LINKEDIN_EMAIL': os.environ.get('LINKEDIN_EMAIL'),
                  'LINKEDIN_PASSWORD': os.environ.get('LINKEDIN_PASSWORD')
              },
              # Only available on google.com
              '*.google.com': {
                  'GOOGLE_EMAIL': os.environ.get('GOOGLE_EMAIL'),
                  'GOOGLE_PASSWORD': os.environ.get('GOOGLE_PASSWORD')
              }
          }
      }
  )

  print(response)
  ```
</CodeGroup>

### Domain Pattern Examples

| Pattern                | Matches                                  |
| ---------------------- | ---------------------------------------- |
| `*.linkedin.com`       | `www.linkedin.com`, `login.linkedin.com` |
| `linkedin.com`         | `linkedin.com`, `www.linkedin.com`       |
| `https://*.google.com` | Only HTTPS Google subdomains             |
| `*`                    | All domains (use sparingly)              |

<Warning>
  Domain-scoped secrets are only available when the browser URL matches the pattern. If the agent navigates to a different domain, those secrets won't be accessible.
</Warning>

## TOTP / Two-Factor Authentication

Secret values support automatic TOTP code generation for 2FA. Use the `bu_2fa_code` suffix for your TOTP secret key:

<CodeGroup>
  ```javascript node.js theme={null}
  const response = await anchorClient.agent.task(
    'Login to the app and complete 2FA verification',
    {
      taskOptions: {
        url: 'https://secure-app.example.com/login',
        secretValues: {
          EMAIL: process.env.APP_EMAIL,
          PASSWORD: process.env.APP_PASSWORD,
          // TOTP secret - generates a fresh 6-digit code automatically
          APP_2FA_bu_2fa_code: process.env.APP_TOTP_SECRET
        }
      }
    }
  );
  ```

  ```python python theme={null}
  response = anchor_client.agent.task(
      'Login to the app and complete 2FA verification',
      task_options={
          'url': 'https://secure-app.example.com/login',
          'secret_values': {
              'EMAIL': os.environ.get('APP_EMAIL'),
              'PASSWORD': os.environ.get('APP_PASSWORD'),
              # TOTP secret - generates a fresh 6-digit code automatically
              'APP_2FA_bu_2fa_code': os.environ.get('APP_TOTP_SECRET')
          }
      }
  )
  ```
</CodeGroup>

## Best Practices

<CardGroup cols={2}>
  <Card title="Use Environment Variables" icon="leaf">
    Never hardcode secrets in your code. Always load from environment variables or a secrets manager.
  </Card>

  <Card title="Scope to Domains" icon="lock">
    Use domain-scoped secrets for multi-site tasks to prevent credential leakage.
  </Card>

  <Card title="Meaningful Key Names" icon="tag">
    Use clear, descriptive key names like `LINKEDIN_PASSWORD` instead of `PASS1`.
  </Card>

  <Card title="Minimal Exposure" icon="eye-slash">
    Only include secrets that the task actually needs.
  </Card>
</CardGroup>

## Security Guarantees

| Guarantee                 | Description                                               |
| ------------------------- | --------------------------------------------------------- |
| **Never logged**          | Secret values are excluded from all logs and telemetry    |
| **Never sent to AI**      | Real values are never visible to the AI model             |
| **Type-time replacement** | Secrets are only used at the moment of typing             |
| **Domain isolation**      | Domain-scoped secrets are only available on matching URLs |
| **No storage**            | Secrets are processed in-memory and never persisted       |
