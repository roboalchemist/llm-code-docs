# Source: https://docs.tavus.io/sections/conversational-video-interface/quickstart/use-the-full-pipeline.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Use the Full Pipeline

> Create your first persona using the full pipeline and start a conversation in seconds.

Use the full pipeline to unlock the complete range of replica capabilities—including perception and speech recognition.

<Steps>
  <Step title="Step 1: Create a Persona" titleSize="h3">
    <Note>
      In this example, we’ll create an interviewer persona with the following settings:

      * A Phoenix-3 stock replica.
      * `raven-0` as the perception model to enable screen sharing.
      * `smart_turn_detection` enabled using the Sparrow model.
    </Note>

    Use the following request body example:

    ```shell cURL theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/personas \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
        "persona_name": "Interviewer",
        "system_prompt": "As an Interviewer, you are a skilled professional who conducts thoughtful and structured interviews. Your aim is to ask insightful questions, listen carefully, and assess responses objectively to identify the best candidates.",
        "pipeline_mode": "full",
        "context": "You have a track record of conducting interviews that put candidates at ease, draw out their strengths, and help organizations make excellent hiring decisions.",
        "default_replica_id": "rfe12d8b9597",
        "layers": {
          "perception": {
            "perception_model": "raven-0"
          },
          "stt": {
            "smart_turn_detection": true
          }
        }
      }'
    ```

    <Note>
      Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys" target="_blank">Developer Portal</a>.
    </Note>

    Tavus offers full layer customizations for your persona. Please see the following for each layer configurations:

    * [Large Language Model (LLM)](/sections/conversational-video-interface/persona/llm)
    * [Perception](/sections/conversational-video-interface/persona/perception)
    * [Text-to-Speech (TTS)](/sections/conversational-video-interface/persona/tts)
    * [Speech-to-Text (STT)](/sections/conversational-video-interface/persona/stt)
  </Step>

  <Step title="Step 2: Create Your Conversation" titleSize="h3">
    Create a new conversation using your newly created `persona_id`:

    ```shell cURL theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
      "persona_id": "<your_persona_id>",
      "conversation_name": "Interview User"
    }'

    ```

    <Note>
      * Replace `<api_key>` with your actual API key.
      * Replace `<your_persona_id>` with your newly created Persona ID.
    </Note>
  </Step>

  <Step title="Step 3: Join the Conversation" titleSize="h3">
    To join the conversation, click the link in the `conversation_url` field from the response:

    ```json  theme={null}
    {
      "conversation_id": "c477c9dd7aa6e4fe",
      "conversation_name": "Interview User",
      "conversation_url": "<conversation_link>",
      "status": "active",
      "callback_url": "",
      "created_at": "2025-05-13T06:42:58.291561Z"
    }
    ```
  </Step>
</Steps>

## Echo Mode

Tavus also supports an [Echo mode](/sections/conversational-video-interface/echo-mode) pipeline. It lets you send text or audio input directly to the persona for playback, bypassing most of the CVI pipeline.

<Warning>
  This mode is not recommended if you plan to use the perception or speech recognition layers, as it is incompatible with them.
</Warning>
