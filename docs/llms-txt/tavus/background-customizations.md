# Source: https://docs.tavus.io/sections/video/background-customizations.md

# Source: https://docs.tavus.io/sections/conversational-video-interface/conversation/customizations/background-customizations.md

# Source: https://docs.tavus.io/sections/video/background-customizations.md

# Source: https://docs.tavus.io/sections/conversational-video-interface/conversation/customizations/background-customizations.md

# Background Customizations

> Apply a green screen or custom background for a personalized visual experience.

## Customize Background in Conversation Setup

<Steps>
  <Step title="Step 1: Create Your Conversation" titleSize="h3">
    <Note>
      In this example, we will use stock replica ID ***rfe12d8b9597*** (Nathan) and stock persona ID ***pdced222244b*** (Sales Coach).
    </Note>

    To apply the green screen background, set the `apply_greenscreen` parameter to `true` when creating the conversation:

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
        "apply_greenscreen": true
       }
    }'

    ```

    <Note>
      Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys" target="_blank">Developer Portal</a>.
    </Note>
  </Step>

  <Step title="Step 2: Customize the Background" titleSize="h3">
    The above request will return the following response:

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

    The replica will appear with a green background. You can customize it using a WebGL-based on the front-end. This allows you to apply a different color or add a custom image.

    <Tip>
      To preview this feature, try our <a href="https://andy-tavus.github.io/CVI-greenscreen-webGL/" target="_blank">Green Screen Sample App</a>. Paste the conversation URL to modify the background.
    </Tip>
  </Step>
</Steps>
