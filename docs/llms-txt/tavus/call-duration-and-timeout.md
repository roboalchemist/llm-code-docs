# Source: https://docs.tavus.io/sections/conversational-video-interface/conversation/customizations/call-duration-and-timeout.md

# Call Duration and Timeout

> Configure call duration and timeout behavior to manage how and when a conversation ends.

## Create a Conversation with Custom Duration and Timeout

<Steps>
  <Step title="Step 1: Create Your Conversation" titleSize="h3">
    <Note>
      In this example, we will use stock replica ID ***rfe12d8b9597*** (Nathan) and stock persona ID ***pdced222244b*** (Sales Coach).
    </Note>

    Use the following request body example:

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
        "max_call_duration": 1800,
        "participant_left_timeout": 60,
        "participant_absent_timeout": 120
       }
    }'

    ```

    <Note>
      Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys" target="_blank">Developer Portal</a>.
    </Note>

    The request example above includes the following customizations:

    | Parameter                    | Description                                                                                     |
    | :--------------------------- | :---------------------------------------------------------------------------------------------- |
    | `max_call_durations`         | Sets the maximum call length in seconds. Maximum: 3600 seconds.                                 |
    | `participant_left_timeout`   | Time (in seconds) to wait before ending the call after the last participant leaves. Default: 0. |
    | `participant_absent_timeout` | Time (in seconds) to end the call if no one joins after it's created. Default: 300.             |
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

    Based on the call duration and timeout settings above:

    * The conversation will automatically end after 1800 seconds (30 minutes), regardless of activity.
    * If the participant leaves the conversation, it will end 60 seconds after they disconnect.
    * If the participant is present but inactive (e.g., not speaking or engaging), the conversation ends after 120 seconds of inactivity.
  </Step>
</Steps>
