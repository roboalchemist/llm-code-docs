# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/custom-channel.md

# Source: https://docs.avaamo.com/user-guide/llamb/custom-channel.md

# Custom channel

After building and testing your LLaMB agent, the next step is to select the deployment channel. The Avaamo Platform offers several pre-built channels, including Web, iOS, Android, and MS Teams, for deploying agents with LLaMB. If you need to deploy agents to a channel not listed, you can configure and deploy agents to a custom channel.

Deploying LLaMB agents in a custom channel enhances the ability to seamlessly integrate LLaMB with any enterprise application, increasing accessibility for users.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FwNQXwT0tuuipxFpTrIeR%2Fimage.png?alt=media&#x26;token=c74e7f2b-2de6-4e9b-b841-2620542cbd7c" alt=""><figcaption></figcaption></figure>

### How does it work?

Custom channel support has been a core feature for all agents within the Avaamo Platform since its inception. This capability now includes agents with LLaMB skills.&#x20;

The overview, concept, configuration, incoming request payload, and testing for Custom channels remain unchanged when enabling them for agents with LLaMB skills. See [Custom channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/custom-channel), for more information.

The only modification is in the payload of the outgoing message sent by the Avaamo platform to the Webhook URL for requests from the custom channel. The rest of the payload parameters and their usage remain unchanged. See [Outgoing request](#outgoing-request), for more information.

### Outgoing request

An outgoing request indicates the payload response sent by the Avaamo platform to the Webhook URL for the request received from the custom channel. The interface hosting the URL must be able to consume this payload structure.&#x20;

The following is a simple payload response of an outgoing request for an agent with a `text` response (Here the response is from Greeting skill which is a simple `text` response):

{% code overflow="wrap" %}

```json
{
  "bot_uuid": "7316833d-xxxx-xxxx-xxxx-b68aec69da8f",
  "channel_uuid": "b9bf302a-xxxx-xxxx-xxxx-730f645968b6",
  "event_type": "MESSAGE",
  "user": {
    "uuid": "9ac15843-xxxx-xxxx-xxxx-930b89ce797e",
    "first_name": "Will",
    "last_name": "Smith",
    "layer_id": "2212b3a0-xxxx-xxxx-xxxx-c21734a9c47b",
    "custom_properties": {
      "first_name": "Will",
      "last_name": "Smith",
      "client_uuid": "9ac15843-xxxx-xxxx-xxxx-930b89ce797e"
    },
    "client_uuid": "9ac15843-xxxx-xxxx-xxxx-930b89ce797e"
  },
  "conversation": {
    "uuid": "d5exxxxxxxxxxxx29c2817b69fdea5f9"
  },
  "sender": "BOT",
  "message": {
    "text": "Hello, I am Leena, your healthcare assistant. I can help with appointment booking or any canceling and rescheduling. I can also answer a few common FAQs on healthcare policies. How can I assist you today?",
    "request_message_uuid": "b08d9d57-xxxx-xxxx-xxxx-7ad017c0a8f0",
    "sequence": 1,
    "total_messages": 1
  },
  "status_callback_url": null
}
```

{% endcode %}

When the response is from the LLaMB skill, instead of a `text` response, a `stream`  response is sent by the Avaamo Platform that contains a `URL.`

You can consume the payload and use the streaming URL to get chunks of responses and then process the request as required. The following is a simple  payload response of an outgoing asynchronous request where the response is from the LLaMB skill:

```json
{
  "bot_uuid": "7316833d-xxxx-xxxx-xxxx-b68aec69da8f",
  "channel_uuid": "b9bf302a-xxxx-xxxx-xxxx-730f645968b6",
  "event_type": "MESSAGE",
  "user": {
    "uuid": "9ac15843-xxxx-xxxx-xxxx-930b89ce797e",
    "first_name": "Will",
    "last_name": "Smith",
    "layer_id": "2212b3a0-xxxx-xxxx-xxxx-c21734a9c47b",
    "custom_properties": {
      "first_name": "Will",
      "last_name": "Smith",
      "client_uuid": "9ac15843-xxxx-xxxx-xxxx-930b89ce797e"
    },
    "client_uuid": "9ac15843-xxxx-xxxx-xxxx-930b89ce797e"
  },
  "conversation": {
    "uuid": "d5exxxxxxxxxxxx29c2817b69fdea5f9"
  },
  "sender": "BOT",
  "message": {
    "stream": {
      "url": "<<stream_url>>"
    },
    "request_message_uuid": "67c2c017-xxxx-xxxx-xxxx-1f826b5e596e",
    "sequence": 2,
    "total_messages": 2
  },
  "status_callback_url": null
}
```

See [Outgoing request in the Custom channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/custom-channel#outgoing-request) for more information on all the other parameters in the payload.

{% hint style="info" %}
**Notes**:

* Currently, there is no set expiration date for the streaming URL.
* All the other functionality of the custom channel remains the same as applicable to the agents without LLaMB skills, including custom user properties. See [Custom channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/custom-channel), for more information.
  {% endhint %}
