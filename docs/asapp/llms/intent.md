# Source: https://docs.asapp.com/ai-productivity/ai-summary/intent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Intent

> Generate intents from your conversations

An intent is a topic-level descriptor—a single word or short phrase—that reflects the customer's main issue or question at the beginning of a conversation.

Intents come out-of-the-box with support for common intents, but you can customize them to match your unique use cases.

Intents enable you to optimize operations by analyzing contact reasons, route conversations more effectively, and contribute to your larger analysis activities.

## How it works

To help understand how intent identification works, let's use an example conversation:

> **Agent**: Hello, thank you for contacting XYZ Insurance. How can I assist you today?\
> **Customer**: Hi, I want to check the status of my payout for my claim.\
> **Agent**: Sure, can you please provide me with the claim number?\
> **Customer**: It's H123456789.\
> **Agent**: Thank you. Could you also provide the last 4 digits of your account number?\
> **Customer**: 6789\
> **Agent**: Let me check the details for you. One moment, please.\
> **Agent**: I see that your claim was approved on June 10, 2024, for \$5000. The payout has been processed.\
> **Customer**: Great! When will I receive the money?\
> **Agent**: The payout will be credited to your account within 3-5 business days.\
> **Customer**: Perfect, thank you so much for your help.\
> **Agent**: You're welcome! Is there anything else I can assist you with?\
> **Customer**: No, that's all. Have a nice day.\
> **Agent**: You too. Goodbye!

AI Summary analyzes the conversation, focusing primarily on the initial exchanges, to determine the customer's main reason for contact. This is represented by the `name` of the intent and the `code`, a machine readable identifier for that intent.

In this case, the intent might be identified as:

```javascript  theme={null}
{
  "code": "Payouts",
  "name": "Payouts"
}
```

The system determines the intent based on the customer's initial statement about checking the status of their payout, which is the primary reason for their contact.

## Generate an Intent

To generate an intent, provide the conversation transcript to ASAPP.

This example uses our **Conversation API** to provide the transcript, but you have options to use [AI Transcribe](/ai-productivity/ai-transcribe) integration if you have voice conversations you want to send to ASAPP.

### Step 1: Create a conversation

To create a `conversation`, provide your IDs for the conversation and customer.

```javascript  theme={null}
curl -X POST 'https://api.sandbox.asapp.com/conversation/v1/conversations' \
--header 'asapp-api-id: <API KEY ID>' \
--header 'asapp-api-secret: <API TOKEN>' \
--header 'Content-Type: application/json' \
--data '{
  "externalId": "[Your id for the conversation]",
  "customer": {
    "externalId": "[Your id for the customer]",
    "name": "customer name"
  },
  "timestamp": "2024-01-23T11:42:42Z"
}'
```

A successfully created conversation returns a status code of 200 and a conversation ID.

### Step 2: Add messages

You need to add the messages for the conversation.

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

### Step 3: Generate Intent

With a conversation containing messages, you can generate an intent.

To generate the intent, provide the ID of the conversation:

```javascript  theme={null}
curl -X GET 'https://api.sandbox.asapp.com/autosummary/v1/intent/5544332211' \
--header 'asapp-api-id: <API KEY ID>' \
--header 'asapp-api-secret: <API TOKEN>'
```

A successful intent generation returns 200 and the intent:

```javascript  theme={null}
{
  "conversationId": "5544332211",
  "intent": {
    "code": "Payouts",
    "name": "Payouts"
  }
}
```

This intent represents the primary reason for the customer's contact, regardless of the number of agents involved in the conversation.

## Customization

AI Summary provides extensive customization options for intent identification to meet your specific needs. Whether you want to use industry-specific intents or adhere to your company's unique categorization, this feature provides the flexibility to tailor intents in a way that aligns with your operational goals.

To customize your intents, you can use the Self-Service Configuration tool in ASAPP's AI Console. This tool allows you to:

1. Upload, create, or modify intent labels
2. Expand intent classifications by adding as many intents as needed
3. Configure the system to align with your specific operational requirements

For more advanced customization, work with your ASAPP account team to refine and implement a custom set of intents that perfectly suit your business needs.
