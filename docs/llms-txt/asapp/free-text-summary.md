# Source: https://docs.asapp.com/ai-productivity/ai-summary/free-text-summary.md

# Free text Summary

> Generate conversation summaries with Free text summary

A Free text summary is a generated summary or description from a conversation.

AI Summary generates high-quality, free-text summaries that are fully configurable in both format and content. You have the flexibility to include or exclude targeted elements based on your needs.

This eliminates the need for agents to take notes during, or after calls, and to minimize post-call forms.

## How it works

To help understand how free-text summary works, let's use an example conversation:

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
> **Agent**: You’re welcome! Is there anything else I can assist you with?\
> **Customer**: No, that's all. Have a nice day.\
> **Agent**: You too. Goodbye!

Each word in a paragraph summary is selected uniquely for a given conversation transcript, rather than using predefined tags. The paragraph incorporates language used by the customer and agent in order to create a faithful representation of what was discussed in the conversation.

<Info>Since the summary is generated, there may be minor variations in grammar if you repeatedly generate  summaries for the same conversation.</Info>

Here is an example summary generated from the above conversation:

> The customer inquired about the status of a payout for an approved claim. The agent confirmed that the claim was approved and the payout has been processed and will be credited within 3-5 business days.

For conversations that involve transfers or multiple agents, AI Summary can generate summaries for both the entire multi-leg conversation and specific legs.

## Generate a free text summary

To generate a free text summary, provide the conversation transcript into ASAPP first.

This example uses our conversation API, but you have options to use AI Transcribe or batch integration options.

### Step 1: Create a conversation

To create a **`conversation`**. Provide your Ids for the conversation and customer.

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

A successfully created conversation returns a status code of 200 and a conversation Id.

### Step 2: Add messages

You need to add the messages for the conversation.

In this example, we are using the `/messages/batch` endpoint to add the whole example conversation.

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

### Step 3: Generate free text summary

Now that you have a conversation with messages, you can generate a free text summary.

To generate the summary, provide the id of the conversation.

```javascript  theme={null}
curl -X GET 'https://api.sandbox.asapp.com/autosummary/v1/free-text-summaries/5544332211' \
--header 'asapp-api-id: <API KEY ID>' \
--header 'asapp-api-secret: <API TOKEN>'
```

A successful free text summary generation returns 200 and the summary.

```javascript  theme={null}
{
  "conversationId": "5544332211",
  "summaryId": "0992d936-ff70-49fc-ac88-76f1246d8t27",
  "summaryText": "The customer inquired about the status of a payout for an approved claim. The agent confirmed that the claim was approved and the payout has been processed and will be credited within 3-5 business days."
}
```

This summary is for the entire conversation, regardless of the number of agents.

## Multi-leg summaries

You may have a conversation where one end user talks to multiple agents about different topics. With AI Summary, you can generate summaries for a conversation based on which agent you want to summarize.

To generate a summary for one leg, provide the id of the conversation in the path, and the agent id as a query parameter.

```javascript  theme={null}
curl -X GET 'https://api.sandbox.asapp.com/autosummary/v1/free-text-summaries/5544332211?agentExternalId=agent_1234 \
--header 'asapp-api-id: <API KEY ID>' \
--header 'asapp-api-secret: <API TOKEN>'
```

This generates a summary for the conversation, only for the parts of conversation that specific agent participated in.

## Customization

AI Summary allows for extensive customization for the free text summary to meet your specific needs. Whether you want to highlight particular aspects of conversations or adhere to industry-specific standards, this feature provides the flexibility to tailor summaries in a way that aligns with your operational goals.

To customize your free text summaries, work with your ASAPP account team to refine what you want from your summaries.

As an example, using the sample conversation, you may want summaries to be specific about dates and amounts mentioned. Here is an example with that customization:

> The customer inquired about the status of a payout for an approved claim. The agent confirmed that the claim was approved on **June 10, 2024**, for **\$5,000**, and the payout has been processed and will be credited within 3-5 business days.
