# Source: https://docs.tavus.io/sections/conversational-video-interface/conversation/customizations/audio-only.md

# Audio-Only Conversation

> Start a conversation in audio-only mode, perfect for voice-only or low-bandwidth environments.

## Create an Audio Only Conversation

<Note>
  All features in the persona's pipeline, including STT, Perception, and TTS, remain fully active in audio-only mode. The only change is that replica video rendering is not included.
</Note>

<Steps>
  <Step title="Step 1: Create your Audio Only Conversation" titleSize="h3">
    <Note>
      In this example, we will use stock persona ID ***pdced222244b*** (Sales Coach).
    </Note>

    To enable audio-only mode, set the `audio_only` parameter to `true` when creating the conversation:

    ```shell cURL theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
      "persona_id": "pdced222244b",
      "audio_only" true
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
        "conversation_id": "cd7e3eac05ede40c",
        "conversation_name": "New Conversation 1751268887110",
        "conversation_url": "<conversation_link>",
        "status": "active",
        "callback_url": "",
        "created_at": "2025-06-30T07:34:47.131571Z"
    }
    ```
  </Step>
</Steps>
