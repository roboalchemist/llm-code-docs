# Source: https://docs.tavus.io/sections/conversational-video-interface/conversation/customizations/closed-captions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Closed Captions

> Enable closed captions for accessibility or live transcription during conversations.

## Enable Captions in Real Time During the Conversation

<Steps>
  <Step title="Step 1: Create Your Conversation" titleSize="h3">
    <Note>
      In this example, we will use stock replica ID ***rfe12d8b9597*** (Nathan) and stock persona ID ***pdced222244b*** (Sales Coach).
    </Note>

    To enable closed captions, set the `enable_closed_captions` parameter to `true` when creating the conversation:

    ```shell cURL theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
      "persona_id": "pdced222244b",
      "replica_id": "rfe12d8b9597",
      "callback_url": "https://yourwebsite.com/webhook",
      "conversation_name": "Improve Sales Technique",
      "conversational_context": "I want to improve my sales techniques. Help me practice handling common objections from clients and closing deals more effectively.",
      "properties": {
        "enable_closed_captions": true
       }
    }'

    ```

    <Note>
      Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys" target="_blank">Developer Portal</a>.
    </Note>
  </Step>

  <Step title="Step 2: Join the Conversation" titleSize="h3">
    To join the conversation, click the link in the ***conversation\_url*** field from the response:

    ```json  theme={null}
    {
      "conversation_id": "ca4301628cb9",
      "conversation_name": "Improve Sales Technique",
      "conversation_url": "<conversation_link>",
      "status": "active",
      "callback_url": "https://yourwebsite.com/webhook",
      "created_at": "2025-05-13T06:42:58.291561Z"
    }
    ```

    Closed captions will appear during the conversation whenever you or the replica speaks.
  </Step>
</Steps>
