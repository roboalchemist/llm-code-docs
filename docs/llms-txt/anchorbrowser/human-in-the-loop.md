# Source: https://docs.anchorbrowser.io/agentic-browser-control/human-in-the-loop.md

# Human-in-the-Loop

> Enable human intervention during AI agent task execution

Enabling Human-in-the-loop (HITL) allows the AI agent to pause execution and request human intervention when needed. This feature is essential for tasks that require human judgment, approval, or handling of unexpected situations.

## Basic Usage

### How It Works

When HITL is enabled, the agent sends its intervention requests to a session-specific queue. The agent then continues execution based on your instructions.

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  (async () => {
    const anchorClient = new Anchorbrowser({
      apiKey: process.env.ANCHOR_API_KEY
    });

    const response = await anchorClient.agent.task(
      'Research information about Python programming on Wikipedia and create a summary. Ask for human verification if you find any controversial or disputed information.',
      {
        taskOptions: {
          url: 'https://en.wikipedia.org/wiki/Python_(programming_language)',
          humanIntervention: true,
          extendedSystemMessage: 'Request human intervention when you encounter disputed or controversial claims about Python'
        }
      }
    );

    console.log(response);
  })();
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  anchor_client = Anchorbrowser(api_key=os.environ.get("ANCHOR_API_KEY"))

  response = anchor_client.agent.task(
      'Research information about Python programming on Wikipedia and create a summary. Ask for human verification if you find any controversial or disputed information.',
      task_options={
          'url': 'https://en.wikipedia.org/wiki/Python_(programming_language)',
          'human_intervention': True,
          'extended_system_message': 'Request human intervention when you encounter disputed or controversial claims about Python'
      }
  )

  print(response)
  ```
</CodeGroup>

<Tip>
  Human-in-the-loop is most effective when combined with clear system messages that define specific intervention triggers and provide context for decision-making.
</Tip>

## Get Pending Requests

To retrieve pending human intervention requests from the agent, use the GET endpoint:

<CodeGroup>
  ```javascript node.js theme={null}
  (async () => {
    const response = await fetch(`https://api.anchorbrowser.io/v1/sessions/${sessionId}/agent/requested-human-intervention`, {
      method: 'GET',
      headers: {
        'anchor-api-key': process.env.ANCHOR_API_KEY
      }
    });

    const data = await response.json();
    console.log('Intervention requests:', data.data.requests);
  })();
  ```

  ```python python theme={null}
  import requests
  import os

  response = requests.get(
      f'https://api.anchorbrowser.io/v1/sessions/{session_id}/agent/requested-human-intervention',
      headers={
          'anchor-api-key': os.getenv('ANCHOR_API_KEY')
      }
  )

  data = response.json()
  print('Intervention requests:', data['data']['requests'])
  ```
</CodeGroup>

## Send Intervention Response

To send a response to a pending human intervention request, use the POST endpoint:

<CodeGroup>
  ```javascript node.js theme={null}
  (async () => {
    const response = await fetch(`https://api.anchorbrowser.io/v1/sessions/${sessionId}/agent/respond-to-human-intervention`, {
      method: 'POST',
      headers: {
        'anchor-api-key': process.env.ANCHOR_API_KEY,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        requestId: 'request-id-from-intervention-request',
        response: 'Your response to the agent\'s request'
      })
    });

    const data = await response.json();
    console.log('Response:', data);
  })();
  ```

  ```python python theme={null}
  import requests
  import os

  response = requests.post(
      f'https://api.anchorbrowser.io/v1/sessions/{session_id}/agent/respond-to-human-intervention',
      headers={
          'anchor-api-key': os.getenv('ANCHOR_API_KEY'),
          'Content-Type': 'application/json'
      },
      json={
          'requestId': 'request-id-from-intervention-request',
          'response': 'Your response to the agent\'s request'
      }
  )

  data = response.json()
  print('Response:', data)
  ```
</CodeGroup>
