# Source: https://docs.tavus.io/sections/conversational-video-interface/conversation/customizations/private-rooms.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Private Rooms

> Create authenticated conversations with meeting tokens for enhanced security.

## Create a Private Conversation

<Steps>
  <Step title="Step 1: Create Your Conversation" titleSize="h3">
    To create a private room, set `require_auth` to `true`:

    ```shell cURL theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
      "persona_id": "pdced222244b",
      "replica_id": "rfe12d8b9597",
      "require_auth": true
    }'
    ```
  </Step>

  <Step title="Step 2: Join the Conversation" titleSize="h3">
    The response includes a `meeting_token`:

    ```json  theme={null}
    {
      "conversation_id": "ca4301628cb9",
      "conversation_url": "https://tavus.daily.co/ca4301628cb9",
      "meeting_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
      "status": "active"
    }
    ```

    Use the token by appending it to the URL:

    ```
    https://tavus.daily.co/ca4301628cb9?t=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
    ```

    Or pass it to the Daily SDK:

    ```javascript  theme={null}
    callFrame.join({ url: conversation_url, token: meeting_token });
    ```
  </Step>
</Steps>
