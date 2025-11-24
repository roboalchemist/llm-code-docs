# Source: https://docs.asapp.com/generativeagent/integrate/example-interactions.md

# Example Interactions

While each type of integration may have some subtle differences on how replies are handled and sent to back to end users. They all still follow the same basic interaction pattern. These examples show some example scenarios, the API calls you would make, and the events you would receive.

* **[Simple Interaction](#simple-interaction "Simple interaction")**
* **[Conversation with an action that requires confirmation](#conversation-with-an-action-that-requires-confirmation "Conversation with an action that requires confirmation")**
* **[Conversation with authentication](#conversation-with-authentication "Conversation with authentication")**
* **[Conversation with transfer to an agent](#conversation-with-transfer-to-an-agent "Conversation with transfer to an agent")**

## Simple interaction

The example below shows a simple interaction with the GenerativeAgent. We first use the Conversation API to create a conversation, and then call the GenerativeAgent API to analyze a message from the customer.

**Request**
`POST /conversation/v1/conversations`

```json  theme={null}
{
 "externalId": "33411121",
 "agent": {
   "externalId": "671",
   "name": "agentname"
 },
 "customer": {
   "externalId": "11462",
   "name": "customername"
 },
 "metadata": {
   "queue": "some-queue"
 },
 "timestamp": "2024-01-23T13:41:20Z"
}
```

**Response**

Status 200: Successfully created the conversation.

```json  theme={null}
{
    "id": "01HMVXRVSA1EGC0CHQTF1X2RN3"
}
```

Now that we have a Conversation ID, we can use it to analyze a new message from our user, like the following:

**Request**

`POST /generativeagent/v1/analyze`

```json  theme={null}
{   
    "conversationId": "01HMVXRVSA1EGC0CHQTF1X2RN3",
    "message": {
        "text": "How can I pay my bill?",
        "sender": {
            "externalId": "11462",
            "role": "customer"
        },
        "timestamp": "2024-01-23T13:43:04Z"
    }
}
```

**Response**

Status 200: Successfully sent the analyze request and created the new message.

```json  theme={null}
{
    "conversationId": "01HMVXRVSA1EGC0CHQTF1X2RN3",
    "messageId": "01HMVXSWK8J9RR0PNGNN7Z4FVM"
}
```

**GenerativeAgent Events**

As a result of the analyze request, the following sequence of events will be sent to via the SSE stream:

```json  theme={null}
{
  generativeAgentMessageId: '116aaf51-8180-47b7-9205-9f61c8799c52',
  externalConversationId: '33411121',
  conversationId: '01HMVXRVSA1EGC0CHQTF1X2RN3',
  type: 'processingStart'
}
{
  generativeAgentMessageId: '5c020ad9-4a25-4746-a345-017bb9711dbe',
  externalConversationId: '33411121',
  conversationId: '01HMVXRVSA1EGC0CHQTF1X2RN3',
  type: 'reply',
  reply: {
    messageId: '01HMVXSZANHNGJ49R83HENDAJB',
    text: "I'm happy to help you! One moment please."
  }
}
{
  generativeAgentMessageId: 'd566fda8-3b7c-42a2-ae39-d08b66397238',
  externalConversationId: '33411121',
  conversationId: '01HMVXRVSA1EGC0CHQTF1X2RN3',
  type: 'reply',
  reply: {
    messageId: '01HMVXTDR1AT9CNQXPYKKBPJ7F',
    text: 'You can pay your bill by calling (XXX) XXX-6094, using the Mobile App, or with a customer service agent over the phone (with a $5 fee).'
  }
}
{
  generativeAgentMessageId: 'bba4320f-de53-4874-83b4-6c8704d3620c',
  externalConversationId: '33411121',
  conversationId: '01HMVXRVSA1EGC0CHQTF1X2RN3',
  type: 'processingEnd'
}
```

## Conversation with an action that requires confirmation

In this use case, we go through a scenario that requires confirmation before the GenerativeAgent can execute a task on the user's behalf. Besides showing the payload of the GenerativeAgent Events that are sent from the GenerativeAgent, we also check the conversation state.

We assume there is an existing conversation with ID 01HMSHT9KKHHBRMRKJTFZYRCKZ.

**Request**

`POST /generativeagent/v1/analyze`

```json  theme={null}
{   
    "conversationId": "01HMSHT9KKHHBRMRKJTFZYRCKZ",
    "message": {
        "text": "hello, how can I reset my router?",
        "sender": {
            "externalId": "11462",
            "role": "customer"
        },
        "timestamp": "2024-01-21T15:08:50Z"
    }
}
```

**Response**

Status 200: Successfully sent the analyze request and created the new message.

```json  theme={null}
{
    "conversationId": "01HMSHT9KKHHBRMRKJTFZYRCKZ",
    "messageId": "01HMSHVZGHAXDZMS722JS1JJJK"
}
```

**GenerativeAgent events**

As a result of the analyze request, the following sequence of events will be sent via the SSE stream:

```json  theme={null}
{
  generativeAgentMessageId: '33843eb0-10f6-4531-a645-ed9481833301',
  externalConversationId: '33411121',
  conversationId: '01HMSHT9KKHHBRMRKJTFZYRCKZ',
  type: 'processingStart'
}
{
  generativeAgentkMessageId: '0ed65d99-215d-48b4-be28-fee936f4757e',
  externalConversationId: '33411121',
  conversationId: '01HMSHT9KKHHBRMRKJTFZYRCKZ',
  type: 'reply',
  reply: {
    messageId: '01HMSQ946T9E3RCXHPNH1B65ZE',
    text: "I'm happy to help you! One moment please."
  }
}
{
  generativeAgentMessageId: '1121411d-e68e-45d3-bf9e-f2a3db73e7ca',
  externalConversationId: '33411121',
  conversationId: '01HMSHT9KKHHBRMRKJTFZYRCKZ',
  type: 'reply',
  reply: {
    messageId: '01HMSQ96TWXB5DT4T259FP76RX',
    text: "Please say 'CONFIRM' to confirm the router reset. This action cannot be undone."
  }
}
{
  generativeAgentMessageId: '3c4b0f55-c702-453c-9a76-db591f685213',
  externalConversationId: '33411121',
  conversationId: '01HMSHT9KKHHBRMRKJTFZYRCKZ',
  type: 'processingEnd'
}
```

From the events above, we can see the GenerativeAgent requires user confirmation before it can proceed.

This can be done through another customer message (analyze API call). Optionally, we can check the current conversation state by calling the GET /state API, before the confirmation is sent:

**Request**

`GET /generativeagent/v1/state?conversationId=01HMSHT9KKHHBRMRKJTFZYRCKZ`

**Response**

Status 200. We see the GenerativeAgent is waiting for confirmation for this conversation.

```json  theme={null}
{
    "state": "waitingForConfirmation",
    "lastGenerativeAgentMessageId": "3c4b0f55-c702-453c-9a76-db591f685213"
}
```

Now, the user sends the confirmation message:

**Request**

`POST /generativeagent/v1/analyze`

```json  theme={null}
{   
    "conversationId": "01HMSHT9KKHHBRMRKJTFZYRCKZ",
    "message": {
        "text": "CONFIRM",
        "sender": {
            "externalId": "11462",
            "role": "customer"
        },
        "timestamp": "2024-01-21T15:09:10Z"
    }
}
```

**Response**

Status 200: Successfully sent the analyze request and created the new message.

```json  theme={null}
{
    "conversationId": "01HMSHT9KKHHBRMRKJTFZYRCKZ",
    "messageId": "01HMVJTR2CPABZ46DM0QK1NS3T"
}
```

The analyze request triggers the following events:

```json  theme={null}
{
  generativeAgentMessageId: 'bae280e8-26c7-4333-ae8f-018e5f7140e9',
  externalConversationId: '33411121',
  conversationId: '01HMSHT9KKHHBRMRKJTFZYRCKZ',
  type: 'processingStart'
}
{
  generativeAgentMessageId: '7bcbab42-e64f-4e1b-9ec8-5db343d471e3',
  externalConversationId: '33411121',
  conversationId: '01HMSHT9KKHHBRMRKJTFZYRCKZ',
  type: 'reply',
  reply: {
    messageId: '01HMSQ946T9E3RCXHPNH1B65ZE',
    text: "Please wait while your router is being reset..."
  }
}
{
  generativeAgentMessageId: 'd0e3cb51-79e4-4b90-8c05-3f345090fbdf',
  externalConversationId: '33411121',
  conversationId: '01HMSHT9KKHHBRMRKJTFZYRCKZ',
  type: 'reply',
  reply: {
    messageId: '01HMSQ96TWXB5DT4T259FP76RX',
    text: "Router successfully reset."
  }
}
{
  generativeAgentMessageId: '6af4172c-7bb7-4fa7-a338-b73a35be5d1c',
  externalConversationId: '33411121',
  conversationId: '01HMSHT9KKHHBRMRKJTFZYRCKZ',
  type: 'reply',
  reply: {
    messageId: '01HMSQ96TWXB5DT4T259FP76RX',
    text: "If you have any other questions or need further assistance, please don't hesitate to ask."
  }
}
{
  generativeAgentMessageId: '008a21a0-af04-4ece-8f58-b7a0c82a1115',
  externalConversationId: '33411121',
  conversationId: '01HMSHT9KKHHBRMRKJTFZYRCKZ',
  type: 'processingEnd'
}
```

Finally, we can optionally check the state again. We see it changed back into "ready".

**Request**

`GET /generativeagent/v1/state?conversationId=01HMSHT9KKHHBRMRKJTFZYRCKZ`

**Response**

```json  theme={null}
{
    "state": "ready",
    "lastGenerativeAgentMessageId": "008a21a0-af04-4ece-8f58-b7a0c82a1115"
}
```

## Conversation with authentication

In this scenario, the user tries to take an action that requires authentication first. GenerativeAgent will then ask for authentication via the GenerativeAgent event, which we can also confirm via the State API call. We'll authenticate and see the GenerativeAgent resuming the task.

We assume there is an existing conversation with ID *01HMW15N6V27Y4V2HRCE0CBZJQ*. Please see the first use case to understand how to create a new conversation.

**Request**

`POST /generativeagent/v1/analyze`

```json  theme={null}
{   
    "conversationId": "01HMW15N6V27Y4V2HRCE0CBZJQ",
    "message": {
        "text": "How much do I owe for my mobile?",
        "sender": {
            "externalId": "11462",
            "role": "customer"
        },
        "timestamp": "2024-01-23T15:49:37Z"
    }
}
```

**Response**

Status 200: Successfully sent the analyze request and created the new message.

```json  theme={null}
{
    "conversationId": "01HMW15N6V27Y4V2HRCE0CBZJQ",
    "messageId": "01HMSHT9KKHHBRMRKJTFZYRCKZ"
}
```

**GenerativeAgent events**

As a result of the analyze request, the following sequence of messages will be sent via the SSE stream:

```json  theme={null}
{
  generativeAgentMessageId: '309181fd-be58-46fa-91b3-ea49f5f4b3d9',
  externalConversationId: '33411121',
  conversationId: '01HMW15N6V27Y4V2HRCE0CBZJQ',
  type: 'processingStart'
}
{
  generativeAgentMessageId: '3122535a-3d0b-4bb5-a0ff-6c26616d2325',
  externalConversationId: '33411121',
  conversationId: '01HMW15N6V27Y4V2HRCE0CBZJQ',
  type: 'reply',
  reply: {
    messageId: '01HMW172YTTESK1EG6A9Y8QRFZ',
    text: "I'm happy to help you! One moment please."
  }
}
{
  generativeAgentMessageId: '49771949-c26e-49ab-86aa-5259d1a249ab',
  externalConversationId: '33411121',
  conversationId: '01HMW15N6V27Y4V2HRCE0CBZJQ',
  type: 'authenticationRequested'
}
{
  generativeAgentMessageId: 'd2d43ac5-e160-40fd-9c5b-773c8f7417e0',
  externalConversationId: '33411121',
  conversationId: '01HMW15N6V27Y4V2HRCE0CBZJQ',
  type: 'processingEnd'
}
```

We can see the second-to-last message is of type authenticationRequested. This tells us that the GenerativeAgent needs authentication in order to continue.

Additionally, we can check the conversation state, which is waitingForAuth:

**Request**

`GET /generativeagent/v1/state?conversationId=01HMW15N6V27Y4V2HRCE0CBZJQ`

**Response**

Status 200. We see the GenerativeAgent is waiting for confirmation for this conversation.

```json  theme={null}
{
  "state": "waitingForAuth",
  "lastGenerativeAgentMessageId": "d2d43ac5-e160-40fd-9c5b-773c8f7417e0"
}
```

Now let's call the authentication endpoint. Note that the specific format and content of the user credentials must be agreed upon between your organization and your ASAPP account team.

**Request**

`POST /conversation/v1/conversations/01HMW15N6V27Y4V2HRCE0CBZJQ/authenticate`

```json  theme={null}
{
    "customerExternalId": "33411121",
    "auth": {
        {{authentication payload}}
    }
}
```

**Response**

Status 204: Successfully sent the authenticate request no response body is expected.

**GenerativeAgent Events**

After a successful authenticate request, the GenerativeAgent will resume if it was waiting for auth. In this case, the following sequence of messages is sent via the SSE Stream:

```json  theme={null}
{
  generativeAgentMessageId: '07df33e7-8603-4393-8ea2-ac29e35197c9',
  externalConversationId: '33411121',
  conversationId: '01HMW15N6V27Y4V2HRCE0CBZJQ',
  type: 'processingStart'
}
{
  generativeAgentMessageId: 'adfe3156-18fe-457b-b726-90c489478c80',
  externalConversationId: '33411121',
  conversationId: '01HMW15N6V27Y4V2HRCE0CBZJQ',
  type: 'reply',
  reply: {
    messageId: '01HMY19BT31Z4AR05S0M5237EK',
    text: "Your current balance for your mobile account is $415.38, with no overdue amount and a past due amount of $10."
  }
}
{
  generativeAgentMessageId: '3325ea14-5b73-4c7a-9511-a6faebc5c98c',
  externalConversationId: '33411121',
  conversationId: '01HMW15N6V27Y4V2HRCE0CBZJQ',
  type: 'reply',
  reply: {
    messageId: '01HMY19CCJ9E8ENS34WNTQ29E2',
    text: 'There are 26 days remaining in your billing cycle.'
  }
}
{
  generativeAgentMessageId: '3325ea14-5b73-4c7a-9511-a6faebc5c98c',
  externalConversationId: '33411121',
  conversationId: '01HMW15N6V27Y4V2HRCE0CBZJQ',
  type: 'reply',
  reply: {
    messageId: '01HMY15DGHYHVHZ5GYAXR1TDWS',
    text: 'For more information on your mobile billing, you can visit https://website.com'
  }
}
{
  generativeAgentMessageId: 'd8785903-a680-4db5-a95f-ba9ed64a7aaa',
  externalConversationId: '33411121',
  conversationId: '01HMW15N6V27Y4V2HRCE0CBZJQ',
  type: 'processingEnd'
}
```

## Conversation with transfer to an agent

This example showcases the bot transferring the conversation to an agent (a.k.a. agent escalation). 

We assume there is an existing conversation with ID *01HMY50MM3D5JP23NPWXKPQVD4*. Please see the first use case to understand how to create a new conversation.

**Request**

`POST /generativeagent/v1/analyze`

```json  theme={null}
{   
    "conversationId": "01HMY50MM3D5JP23NPWXKPQVD4",
    "message": {
        "text": "Can I talk to a real human?",
        "sender": {
            "externalId": "11462",
            "role": "customer"
        },
        "timestamp": "2024-01-24T11:35:23Z"
    }
}
```

**Response**

Status 200: Successfully sent the analyze request and created the new message.

```json  theme={null}
{
    "conversationId": "01HMY50MM3D5JP23NPWXKPQVD4",
    "messageId": "01HMY5FRHW3B76JSS3BVP1VJJX"
}
```

**GenerativeAgent Events**
As a result of the analyze request, the following sequence of messages will be sent via the SSE Stream:

```json  theme={null}
{
  generativeAgentMessageId: '233e206d-a444-4736-9a66-1fde75e46df7',
  externalConversationId: '33411121',
  conversationId: '01HMY50MM3D5JP23NPWXKPQVD4',
  type: 'processingStart'
}
{
  generativeAgentMessageId: '2925b18f-4140-4312-b071-b56feac86d5a',
  externalConversationId: '33411121',
  conversationId: '01HMY50MM3D5JP23NPWXKPQVD4',
  type: 'reply',
  reply: {
    messageId: '01HMY5FWAMR5DF3DABGNB5118D',
    text: 'Sure, connecting you with an agent.'
  }
}
{
  generativeAgentMessageId: '42ec4212-02aa-4ac6-94e2-4c8fee24352f',
  externalConversationId: '33411121',
  conversationId: '01HMY50MM3D5JP23NPWXKPQVD4',
  type: 'transferToAgent'
}
{
  generativeAgentMessageId: '0deb0eb0-dc75-48e5-80ed-805f14d95e0c',
  externalConversationId: '33411121',
  conversationId: '01HMY50MM3D5JP23NPWXKPQVD4',
  type: 'processingEnd'
}
```

The second-to-last message is of type transferToAgent. We can also optionally verify the conversation state by calling the state API:

**Request**

`GET /generativeagent/v1/state?conversationId=01HMY50MM3D5JP23NPWXKPQVD4`

**Response**

Status 200. We see the GenerativeAgent is waiting for confirmation for this conversation.

```json  theme={null}
{
  "state": "transferredToAgent",
  "lastGenerativeAgentMessageId": "0deb0eb0-dc75-48e5-80ed-805f14d95e0c"
}
```
