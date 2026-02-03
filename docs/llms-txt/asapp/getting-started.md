# Source: https://docs.asapp.com/generativeagent/getting-started.md

# Source: https://docs.asapp.com/ai-productivity/ai-summary/getting-started.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started

> Learn how to get started with AI Summary

To start using AI Summary, choose your integration method:

<AccordionGroup>
  <Accordion title="API (Real Time)">
    * Upload transcripts or use a conversation from AI Transcribe and receive the insights instantly.
    * You can use this approach for real-time experiences like conversation routing and form pre-filling.
    * For digital channels: Provide the chat messages directly.
    * For voice channels: Use AI Transcribe or your own transcription service.

    This integration is covered in this Getting Started guide.
  </Accordion>

  <Accordion title="Salesforce plugin">
    * Supports only Salesforce Chat.
    * Inserts free-text summaries into conversation objects.

    <Card horizontal={true} title="Salesforce Plugin" href="/ai-productivity/ai-summary/salesforce-plugin">Learn how to use the Salesforce Plugin</Card>
  </Accordion>
</AccordionGroup>

The following instructions cover the **API (Real Time) Integration** as it is the most common method.

To use AI Summary via API:

1. Provide transcripts
2. Extract insights with AI Summary API

## Before you Begin

Before you start integrating AI Summary, you need to:

* Get your API Key Id and Secret
* Ensure your account and API key can access AI Summary. Reach out to your ASAPP team if you are unsure.

## Step 1: Provide transcripts

How you provide transcripts depends on the conversation channel.

**For digital channels:**

* Use the **conversation API** to upload the messages directly.

**For voice channels:**

* Use **AI Transcribe** Service to transcribe the audio, or
* Upload utterances via Conversation API if using your own transcription service.

<Tabs>
  <Tab title="Use Conversation API">
    To send transcripts via the Conversation API, you need to:

    1. Create a `conversation`.
    2. Add `messages` to the `conversation`.

    To create a `conversation`, provide your IDs for the conversation and customer.

    ```bash  theme={null}
    curl -X POST 'https://api.sandbox.asapp.com/conversation/v1/conversations' \
    --header 'asapp-api-id: \<API KEY ID\>' \
    --header 'asapp-api-secret: \<API TOKEN\>' \
    --header 'Content-Type: application/json' \
    --data '{ 
      "externalId": "\[Your id for the conversation\]",
      "customer": {   
        "externalId": "\[Your id for the customer\]",
        "name": "customer name" 
      },
      "timestamp": "2024-01-23T11:42:42Z"
    }'
    ```

    This conversation represents a thread of messages between an end user and one or more agents. A successfully created conversation returns a status code of 200 and provides the `id` of the conversation.

    ```json  theme={null}
    {"id":"01HNE48VMKNZ0B0SG3CEFV24WM"}
    ```

    Each time your end user or an agent sends a message, you need to add the messages to the conversation by creating a `message` on the `conversation`. This may be either the chat messages in digital channels or the audio transcript from your transcription service.

    You have the choice to add a **single message** for each turn of the conversation, or you can upload a **batch of messages** for a conversation.

    <Tabs>
      <Tab title="Single message">
        ```bash  theme={null}
        curl -X POST 'https://api.sandbox.asapp.com/conversation/v1/conversations/01HNE48VMKNZ0B0SG3CEFV24WM/messages' \
        --header 'asapp-api-id: \<API KEY ID\>' \
        --header 'asapp-api-secret: \<API TOKEN\>' \
        --header 'Content-Type: application/json' \
        --data '{ 
          "text": "Hello, I would like to upgrade my internet plan to GOLD.",
          "sender": {   
            "role": "customer",
            "externalId": "\[Your id for the customer\]" 
          },
          "timestamp": "2024-01-23T11:42:42Z"
        }'
        ```

        A successfully created message returns a status code of 200 and the id of the message.

        <Warning>We only show one message as an example, though you would create many messages over the course of the conversation.</Warning>
      </Tab>

      <Tab title="Batched messages">
        Use the `/messages/batch` endpoint to send multiple messages at once for a given conversation.

        ```javascript  theme={null}
        curl -X POST 'https://api.sandbox.asapp.com/conversation/v1/conversations/5544332211/messages/batch' \
        --header 'asapp-api-id: <API KEY ID>' \
        --header 'asapp-api-secret: <API TOKEN>' \
        --header 'Content-Type: application/json' \
        --data '{
          "messages": [
            {
              "text": "Hello, thank you for contacting XYZ Insurance. How can I assist you today?",
              "sender": {"role": "agent", "externalId": "agent_1234"},
              "timestamp": "2024-09-09T10:00:00Z"
            },
            {
              "text": "Hi, I want to check the status of my payout for my claim.",
              "sender": {"role": "customer", "externalId": "cust_1234"},
              "timestamp": "2024-09-09T10:01:00Z"
            },
            {
              "text": "Sure, can you please provide me with the claim number?",
              "sender": {"role": "agent", "externalId": "agent_1234"},
              "timestamp": "2024-09-09T10:02:00Z"
            },
            {
              "text": "It\'s H123456789.",
              "sender": {"role": "customer", "externalId": "cust_1234"},
              "timestamp": "2024-09-09T10:03:00Z"
            },
            {
              "text": "Thank you. Could you also provide the last 4 digits of your account number?",
              "sender": {"role": "agent", "externalId": "agent_1234"},
              "timestamp": "2024-09-09T10:04:00Z"
            },
            {
              "text": "****",
              "sender": {"role": "customer", "externalId": "cust_1234"},
              "timestamp": "2024-09-09T10:05:00Z"
            },
            {
              "text": "Let me check the details for you. One moment, please.",
              "sender": {"role": "agent", "externalId": "agent_1234"},
              "timestamp": "2024-09-09T10:06:00Z"
            },
            {
              "text": "I see that your claim was approved on June 10, ****, for ****. The payout has been processed.",
              "sender": {"role": "agent", "externalId": "agent_1234"},
              "timestamp": "2024-09-09T10:07:00Z"
            },
            {
              "text": "Great! When will I receive the money?",
              "sender": {"role": "customer", "externalId": "cust_1234"},
              "timestamp": "2024-09-09T10:08:00Z"
            },
            {
              "text": "The payout will be credited to your account within 3-5 business days.",
              "sender": {"role": "agent", "externalId": "agent_1234"},
              "timestamp": "2024-09-09T10:09:00Z"
            },
            {
              "text": "Perfect, thank you so much for your help.",
              "sender": {"role": "customer", "externalId": "cust_1234"},
              "timestamp": "2024-09-09T10:10:00Z"
            },
            {
              "text": "You\'re welcome! Is there anything else I can assist you with?",
              "sender": {"role": "agent", "externalId": "agent_1234"},
              "timestamp": "2024-09-09T10:11:00Z"
            },
            {
              "text": "No, that\'s all. Have a nice day.",
              "sender": {"role": "customer", "externalId": "cust_1234"},
              "timestamp": "2024-09-09T10:12:00Z"
            },
            {
              "text": "You too. Goodbye!",
              "sender": {"role": "agent", "externalId": "agent_1234"},
              "timestamp": "2024-09-09T10:13:00Z"
            }
          ]
        }'
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Use AI Transcribe">
    AI Transcribe converts audio streams into real-time transcripts. Regardless of the platform you use:

    1. AI Transcribe generates a `conversation` object for each transcribed interaction.
    2. You'll receive a unique `conversation` ID.
    3. Use this `conversation` ID to extract insights via the AI Summary API.

    Platform-specific integration steps vary. Refer to the AI Transcribe documentation for detailed instructions for your chosen platform.
  </Tab>
</Tabs>

## Step 2: Extract Insights

AI Summary offers three types of insights, each with its own API endpoint:

* **Free text summary**
* **Intent**
* **Structured Data**

All APIs require the conversation ID to extract the relevant insight.

### Example: Generate a free text summary

To generate a free text summary, use the following API call:

```javascript  theme={null}
curl -X GET 'https://api.sandbox.asapp.com/autosummary/v1/free-text-summaries/[conversationId]' \
--header 'asapp-api-id: <API KEY ID>' \
--header 'asapp-api-secret: <API TOKEN>'
```

A successful free text summary generation returns 200 and the summary:

```javascript  theme={null}
{
  "conversationId": "5544332211",
  "summaryId": "0992d936-ff70-49fc-ac88-76f1246d8t27",
  "summaryText": "Customer called in saying their internet was slow. Customer wasn't home so couldn't run a speed test. Agent recommended calling back once they could run the speed test."
}
```

## Next Steps

Now that you understand the fundamentals of using AI Summary, explore further:

<CardGroup>
  <Card title="Example Use Cases" href="/ai-productivity/ai-summary/example-use-cases" />

  <Card title="Free Text Summary" href="/ai-productivity/ai-summary/free-text-summary" />

  <Card title="Intent" href="/ai-productivity/ai-summary/intent" />

  <Card title="Structured Data" href="/ai-productivity/ai-summary/structured-data" />
</CardGroup>
