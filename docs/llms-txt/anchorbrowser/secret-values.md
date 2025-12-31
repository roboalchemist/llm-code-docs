# Source: https://docs.anchorbrowser.io/agentic-browser-control/secret-values.md

# Secret Values

> Securely pass credentials and sensitive data to AI agents

Secret values allow you to securely pass credentials, API keys, and other sensitive data to AI agents during task execution. These values are not logged or stored anywhere.

## Basic Usage

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  (async () => {
    const anchorClient = new Anchorbrowser({
      apiKey: process.env.ANCHORBROWSER_API_KEY
    });

    const response = await anchorClient.agent.task(
      'Login to linkedin, approve all friend requests, search for "Anchorbrowser" and send a connection request',
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
  })();
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  anchor_client = Anchorbrowser(api_key=os.environ.get("ANCHORBROWSER_API_KEY"))

  response = anchor_client.agent.task(
      'Login to linkedin, approve all friend requests, search for "Anchorbrowser" and send a connection request',
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
  Secret values are the recommended way to handle any sensitive data in AI agent tasks. Never include credentials directly in prompts or system messages.
</Tip>
