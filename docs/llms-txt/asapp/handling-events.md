# Source: https://docs.asapp.com/generativeagent/integrate/handling-events.md

# Handling GenerativeAgent Events

While analyzing a conversation, GenerativeAgent communicates back to you via events. These events are sent via a [Server-Sent-Event](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) stream.

The **single SSE stream** contain events for **all conversations** that are processed by GenerativeAgent.

Each event contains the id of the conversation it relates to, and the type of event.

Handling these events has 2 main steps:

1. Create SSE Stream
2. Handle the event

## Step 1: Create SSE Stream

To create an SSE stream for GenerativeAgent, first generate a streaming URL, and then initiate the SSE stream with that URL

To create the SSE stream URL, POST to `/streams`:

```bash  theme={null}
curl -X POST 'https://api.sandbox.asapp.com/generativeagent/v1/streams' \
--header 'asapp-api-id: <API KEY ID>' \
--header 'asapp-api-secret: <API TOKEN>' \
--header 'Content-Type: application/json' \
--data '{}'
```

A successful request returns 200 and the `streamingUrl` to use to create the SSE stream. Additionally it returns a `streamId`. Save this Id and use it to [reconnect SSE](#handle-sse-disconnects "Handle SSE disconnects") in-case the stream disconnects.

```json  theme={null}
{
    "streamId": "01ARZ3NDEKTSV4RRFFQ69G5FAV",
    "streamingUrl": "https://ws-coradnor.asapp.com/push-api/connect/sse?token=token",
    "messageTypes": [
        "generative-agent-message"
    ]
}
```

The streaming URL is only valid for 30 seconds. After that time, the connection will be rejected and you will need to request a new URL.

Initiate the SSE stream by connecting to the URL and handle the events. How you connect to an SSE stream depends on the language you use and what are your preferred libraries. We include an [example in NodeJS](#code-sample "Code sample") below.

### Handle SSE disconnects

If your SSE connection breaks, reestablish the stream using the `streamId` returned in the original request.

```bash  theme={null}
curl -X POST 'https://api.sandbox.asapp.com/generativgeagent/v1/streams' \
--header 'asapp-api-id: <API KEY ID>' \
--header 'asapp-api-secret: <API TOKEN>' \
--header 'Content-Type: application/json' \
--data '{ "streamId": "01ARZ3NDEKTSV4RRFFQ69G5FAV",
}
```

A successful request returns 200 and the streaming URL you will reconnect with.

```json  theme={null}
{
  "streamId": "01ARZ3NDEKTSV4RRFFQ69G5FAV",
  "streamingUrl": "https://ws-coradnor.asapp.com/push-api/connect/sse?token=token", 
  "messageTypes": [
    "generative-agent-message"
  ]
}
```

Save the `streamId` to use in your `/analyze` requests. This will send all the GenerativeAgent messages for that analyze request, to this SSE stream.

## Step 2: Handle events

You need to process each event from GenerativeAgent. The data sent via SSE needs to be parsed into a JSON, and then handled accordingly.

Determining the conversation the event pertains to and take the necessary action depending on the event `type`.

For a given analyze request on a conversation, you may receive any of the following event types:

* **`processingStart`**: The bot started processing. This can be used to trigger user feedback such as showing a "typing" indicator.
* **`authenticationRequired`**: Some API Connections require additional User authentication. Refer to [User authentication required](#user-authentication-required "User Authentication Required") for more information.
* **`reply`**: The bot has a reply for the conversation. We will automatically create a message for the bot, but you will need to send back the response to your user. This can be text directly when on a text based system, or your TTS for voice channels.
* **`processingEnd`**: The bot finished processing. This indicates there will be no further events until analyze is called again.
* **`transferToAgent`**: The bot could not handle the request and the conversation should be transferred to an agent.
* **`transferToSystem`**: The bot is transferring control to an external system. This is a system transfer function.

Here is an example set of events where analyze is called:

```json  theme={null}
{
  "generativeAgentMessageId": "116aaf51-8180-47b7-9205-9f61c8799c52",
  "externalConversationId": "33411121",
  "conversationId": "01HMVXRVSA1EGC0CHQTF1X2RN3",
  "type": "processingStart"
}
{
  "generativeAgentMessageId": "5c020ad9-4a25-4746-a345-017bb9711dbe",
  "externalConversationId": "33411121",
  "conversationId": "01HMVXRVSA1EGC0CHQTF1X2RN3",
  "type": "reply",
  "reply": {
    "messageId": "01HMVXSZANHNGJ49R83HENDAJB",
    "text": "I'm happy to help you! One moment please."
  }
}
{
  "generativeAgentMessageId": "d566fda8-3b7c-42a2-ae39-d08b66397238",
  "externalConversationId": "33411121",
  "conversationId": "01HMVXRVSA1EGC0CHQTF1X2RN3",
  "type": "reply",
  "reply": {
    "messageId": "01HMVXTDR1AT9CNQXPYKKBPJ7F",
    "text": "You can pay your bill by calling (XXX) XXX-6094, using the Mobile App, or with a customer service agent over the phone (with a $5 fee)."
  }
}
{
  "generativeAgentMessageId": "bba4320f-de53-4874-83b4-6c8704d3620c",
  "externalConversationId": "33411121",
  "conversationId": "01HMVXRVSA1EGC0CHQTF1X2RN3",
  "type": "processingEnd"
}
```

## User Authentication Required

A key power of GenerativeAgent is it's ability to call your APIs to look up information or perform an action. These are determined by the [API Connections](/generativeagent/configuring/connect-apis) you create.

Some APIs require end user authentication. When this is the case, we sent the `authenticationRequested` event. Work with your ASAPP team to determine those authentication needs and what needs to passed back to ASAPP.

Based on the specifics of your API, you will need to gather the end user authentication information and call [`/authenticate`](/apis/conversations/authenticate-a-user-in-a-conversation) on the conversation:

```bash  theme={null}
curl -X POST 'https://api.sandbox.asapp.com/conversation/v1/conversations/[conversation Id]/authenticate' \
--header 'asapp-api-id: <API KEY ID>' \
--header 'asapp-api-secret: <API TOKEN>' \
--header 'Content-Type: application/json' \
--data '{
    "customerExternalId": "[Your Id of the customer]",
    "auth": {
        {{Your predetermined authentication payload}}
    }
}'
```

A successful response returns a 204 response and no body. GenerativeAgent will continue processing and send you subsequent events.

## Code sample

Here is an example of initiate the SSE stream and listening for the events using nodeJS. This uses [axios](https://www.npmjs.com/package/axios) to get the URL and the [EventSource](https://www.npmjs.com/package/eventsource) package for handling the events:

```javascript  theme={null}
import axios from 'axios';
import EventSource from 'eventsource';
const response = await axios.post('https://api.sandbox.asapp.com/generativeagent/v1/streams', {}, {
    headers: {
        'asapp-api-id': '[Your API key id]',
        'asapp-api-secret': '[Your API secret]',
        'Content-Type': 'application/json'
    }
});
console.log('Using streaming URL:', response.data.streamingUrl);
const eventSource = new EventSource(response.data.streamingUrl);
eventSource.onopen = (event) => {
    console.log('Connection opened:', event.type);
};
eventSource.onerror = (error) => {
    console.error('EventSource failed:', error);
    eventSource.close();
};
eventSource.onmessage = (event) => {
    console.log('Received uncategorized data:', event.data);
};
eventSource.addEventListener('status', (event) => {
    console.log('Received status ping:', event.data);
})
eventSource.addEventListener('generative-agent-message', (event) => {
    console.log('Received generative-agent-message:', event.data);
    try {
        const parsedData = JSON.parse(event.data);
        console.log('Parsed data:', parsedData);
        // Handle different event types here
        switch (parsedData.type) {
            case "processingStart":
                console.log("Bot started processing.");
                break;
            case "authenticationRequired":
                console.log("Initiate customer authentication.");
                break;
            case "reply":
                console.log("GenerativeAgent responded:", parsedData.content);
                break;
            case "processingEnd":
                console.log("Bot finished processing");
                break;
            case "transferToAgent":
                console.log("Bot could not handle request, transfer to a live agent.");
                break;
            default:
                console.log("Unknown event type:", parsedData.type);
        }
    } catch (error) {
        console.error('Error parsing event data:', error);
    }
})
```

This example is intended to be illustrative only.

## Event Schema

Each event is a json format with several fields with the following specification:

| Field Name                          | Type         | Description                                                                                                                                                                                                                  |
| :---------------------------------- | :----------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| generativeAgentMessageId            | string       | A unique identifier for this webhook request.                                                                                                                                                                                |
| conversationId                      | string       | The internal identifier for the conversation from the ASAPP system.                                                                                                                                                          |
| externalConversationId              | string       | The external identifier for the conversation from your external system.                                                                                                                                                      |
| type                                | string, enum | The type of bot response. It can be one of the following: <ul><li> reply </li><li>  processingStart </li><li> processingEnd </li><li> authenticationRequired </li><li> transferToAgent </li><li> transferToSystem </li></ul> |
| reply.\*                            | object       | If the `type` is **reply** then the bot's reply is contained in this object.                                                                                                                                                 |
| reply.messageId                     | string       | The identifier of the message sent in the reply                                                                                                                                                                              |
| reply.text                          | string       | The message text of the reply                                                                                                                                                                                                |
| transferToSystem.\*                 | object       | If the `type` is **transferToSystem** then the variables to be transferred to the external system are contained in this object.                                                                                              |
| transferToSystem.referenceVariables | object       | A Hash map of reference variables to be transferred to the external system.                                                                                                                                                  |
| transferToSystem.transferVariables  | object       | A Hash map of transfer variables to be transferred to the external system.                                                                                                                                                   |
| transferToSystem.currentTaskName    | string       | The name of the current task that is being transferred to the external system.                                                                                                                                               |

<Tabs>
  <Tab title="reply">
    ```json  theme={null}
    {
      "generativeAgentMessageId": "d566fda8-3b7c-42a2-ae39-d08b66397238",
      "externalConversationId": "33411121",
      "conversationId": "01HMVXRVSA1EGC0CHQTF1X2RN3",
      "type": "reply",
      "reply": {
        "messageId": "01HMVXTDR1AT9CNQXPYKKBPJ7F",
        "text": "You can pay your bill by calling (XXX) XXX-6094, using the Mobile App, or with a customer service agent over the phone (with a $5 fee)."
      }
    }
    ```
  </Tab>

  <Tab title="processingStart">
    ```json  theme={null}
    {
      "generativeAgentMessageId": "116aaf51-8180-47b7-9205-9f61c8799c52",
      "externalConversationId": "33411121",
      "conversationId": "01HMVXRVSA1EGC0CHQTF1X2RN3",
      "type": "processingStart"
    }
    ```
  </Tab>

  <Tab title="processingEnd">
    ```json  theme={null}
    {
      "generativeAgentMessageId": "bba4320f-de53-4874-83b4-6c8704d3620c",
      "externalConversationId": "33411121",
      "conversationId": "01HMVXRVSA1EGC0CHQTF1X2RN3",
      "type": "processingEnd"
    }
    ```
  </Tab>

  <Tab title="authenticationRequired">
    ```json  theme={null}
    {
      "generativeAgentMessageId": "7d9e4f12-b3a8-4c91-95d6-8ef2a7c31b59",
      "externalConversationId": "33411121",
      "conversationId": "01HMVXRVSA1EGC0CHQTF1X2RN3",
      "type": "authenticationRequired"
    } 
    ```
  </Tab>

  <Tab title="transferToAgent">
    ```json  theme={null}
    {
      "generativeAgentMessageId": "9f47d8e3-c612-4b9a-8d5f-e31a2c4b6789",
      "externalConversationId": "33411121",
      "conversationId": "01HMVXRVSA1EGC0CHQTF1X2RN3",
      "type": "transferToAgent"
    }
    ```
  </Tab>

  <Tab title="transferToSystem">
    ```json  theme={null}
    {
      "generativeAgentMessageId": "bba4320f-de53-4874-83b4-6c8704d3620c",
      "externalConversationId": "33411121",
      "conversationId": "01HMVXRVSA1EGC0CHQTF1X2RN3",
      "type": "transferToSystem",
      "transferToSystem": {
        "referenceVariables": {
          "customerName": "John Smith",
          "accountNumber": "12345",
          "isActive": true
        },
        "transferVariables": {
          "department": "billing",
          "priority": "high",
          "notes": ["Payment pending", "Requires callback"]
        },
        "currentTaskName": "billing_transfer"
      }
    }
    ```
  </Tab>
</Tabs>

## Next Steps

After handling Events from GenerativeAgents, you have control over what is happening during conversations.

You may find one of the following sections helpful in advancing your integration:

<CardGroup>
  <Card title="AutoTranscribe Websocket" href="/generativeagent/integrate/autotranscribe-websocket" />

  <Card title="Example Interactions" href="/generativeagent/integrate/example-interactions" />

  <Card title="Integrate GenerativeAgent" href="/generativeagent/integrate" />
</CardGroup>
