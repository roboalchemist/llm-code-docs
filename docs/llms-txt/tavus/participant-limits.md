# Source: https://docs.tavus.io/sections/conversational-video-interface/conversation/customizations/participant-limits.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Participant Limits

> Control the maximum number of participants allowed in a conversation.

## Create a Conversation with Participant Limits

<Note>
  Replicas count as participants. For example, `max_participants: 2` allows one human participant plus one replica.
</Note>

<Steps>
  <Step title="Step 1: Create Your Conversation" titleSize="h3">
    Set `max_participants` to limit room capacity:

    ```shell cURL theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
      "persona_id": "pdced222244b",
      "replica_id": "rfe12d8b9597",
      "max_participants": 2
    }'
    ```
  </Step>

  <Step title="Step 2: Join the Conversation" titleSize="h3">
    ```json  theme={null}
    {
      "conversation_id": "ca4301628cb9",
      "conversation_url": "https://tavus.daily.co/ca4301628cb9",
      "status": "active"
    }
    ```

    When the limit is reached, additional users cannot join.
  </Step>
</Steps>
