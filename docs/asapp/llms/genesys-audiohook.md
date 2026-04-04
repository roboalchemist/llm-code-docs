# Source: https://docs.asapp.com/generativeagent/integrate/genesys-audiohook.md

# Source: https://docs.asapp.com/ai-productivity/ai-transcribe/genesys-audiohook.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploying AI Transcribe for Genesys AudioHook

> Use AI Transcribe in your Genesys Audiohook application

This guide covers the **Genesys AudioHook Media Gateway** solution pattern, which consists of the following components to receive speech audio and call signals, and return call transcripts:

* Media gateways for receiving call audio from Genesys Cloud
* HTTPS API which enables the customer to POST requests to start and stop call transcription
* Webhook to POST real-time transcripts to a designated URL of your choosing, alongside two additional APIs to retrieve transcripts after-call for one or a batch of conversations

ASAPP works with you to understand your current telephony infrastructure and ecosystem.

Your ASAPP account team will also determine the main use case(s) for the transcript data to determine where and how call transcripts should be sent.

ASAPP then completes the architecture definition, including integration points into the existing infrastructure.

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dbc58832-5f3c-fb5c-3327-7108f4abf265.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=151fbf1adbbced0ba6f68ec7680dca98" data-og-width="1469" width="1469" data-og-height="868" height="868" data-path="image/uuid-dbc58832-5f3c-fb5c-3327-7108f4abf265.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dbc58832-5f3c-fb5c-3327-7108f4abf265.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=3971c4287671888087dcc5539c4ff2e9 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dbc58832-5f3c-fb5c-3327-7108f4abf265.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=ed58207ee50eb9bc2c870e0bab03dcf2 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dbc58832-5f3c-fb5c-3327-7108f4abf265.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=d746d193a62e908eee13bb665b05b17b 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dbc58832-5f3c-fb5c-3327-7108f4abf265.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=3ecd352c6427c1b175d5b49c14f61ac3 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dbc58832-5f3c-fb5c-3327-7108f4abf265.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=5fbc9b07a01caf2b9fb8cd267720944b 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dbc58832-5f3c-fb5c-3327-7108f4abf265.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=6a6a8ac9797fd69640c34fc20d8d3b1d 2500w" />
</Frame>

### Integration Steps

There are three steps to integrate AI Transcribe into Genesys Audiohook:

1. Enable AudioHook and Configure for ASAPP
2. Send Start and Stop Requests
3. Receive Transcript Outputs

### Requirements

**Audio Stream Codec**

Genesys AudioHook provides audio in the mu-law format with 8000 sample rate, which ASAPP supports.

You do not need any modification or additional transcoding when forking audio to ASAPP.

<Note>
  When supplying recorded audio to ASAPP for AI Transcribe model training prior to implementation, send uncompressed .WAV media files with speaker-separated channels.
</Note>

Recordings for training should have a sample rate of 8000 and 16-bit PCM audio encoding.

Read the [Customization section of the AI Transcribe Product Guide](/ai-productivity/ai-transcribe/product-guide#customization) for more on data requirements for transcription model training.

**Developer Portal**

ASAPP provides an AI Services [Developer Portal](/getting-started/developers). Within the portal, developers can do the following:

* Access relevant API documentation (e.g. OpenAPI reference schemas)
* Access API keys for authorization
* Manage user accounts and apps

<Tip>
  Visit the [Get Started](/getting-started/developers) for instructions on creating a developer account, managing teams and apps, and setting up AI Service APIs.
</Tip>

## Integrate with Genesys AudioHook

### 1. Enable AudioHook and Configure for ASAPP

To enable AudioHook within Genesys:

1. Access Genesys Cloud Admin, navigate to Integrations/Integrations and click "plus" in upper right to add more integrations.
2. Find [AudioHook](https://help.mypurecloud.com/articles/install-audiohook-monitor-from-genesys-appfoundry/) Monitor and Install.
3. [Configure AudioHook Monitor](https://help.mypurecloud.com/articles/configure-and-activate-audiohook-monitor-in-genesys-cloud/) Integration, using the Connection URI (i.e. wss\://ws-example.asapp.com/mg-genesysaudiohook-autotranscribe/) and credentials provided by ASAPP.
4. [Enable voice transcription](https://help.mypurecloud.com/articles/configure-voice-transcription/) on desired trunks and within desired Architect Flows. You do not need to select ASAPP as the transcription engine.

### 2. Send Start and Stop Requests

The `/start-streaming` and `/stop-streaming` endpoints of the Start/Stop API control when transcription occurs for every call media stream (identified by the Genesys conversationId) sent to ASAPP's media gateway. See the [Endpoints](#endpoints) section to learn how to interact with them.

ASAPP will not begin transcribing call audio until you request it to, thus preventing transcription of audio at the very beginning of the Genesys AudioHook audio streaming session, which may include IVR, hold music, or queueing.

Stop requests pause or end transcription for any needed reason. For example, you could use a stop request mid-call when the agent places the call on hold or at the end of the call to prevent transcribing post-call interactions such as satisfaction surveys.

<Note>
  AI Transcribe is only meant to transcribe conversations between customers and agents - you should implement start and stop requests to ensure the system does not transcribe non-conversation audio (e.g., hold music, IVR menus, surveys). Attempted transcription of non-conversation audio will negatively impact other services meant to consume conversation transcripts, such as ASAPP AI Summary.
</Note>

### 3. Receive Transcript Outputs

AI Transcribe outputs transcripts using three separate mechanisms, each corresponding to a different temporal use case:

* **[Real-time](#real-time-via-webhook)**: Webhook posts complete utterances to your target endpoint as they are transcribed during the live conversation
* **[After-call](#after-call-via-get-request "After-Call via GET Request")**: GET endpoint responds to your requests for a designated call with the full set of utterances from that completed conversation
* **[Batch](#batch-via-file-exporter "Batch via File Exporter")**: File Exporter service responds to your request for a designated time interval with a link to a data feed file that includes all utterances from that interval's conversations

#### Real-Time via Webhook

ASAPP sends transcript outputs in real-time via HTTPS POST requests to a target URL of your choosing.

Authentication

Once the target is selected, work with your ASAPP account team to implement one of the following supported authentication mechanisms:

* **Custom CAs:** Custom CA certificates for regular TLS (1.2 or above).
* **mTLS:** Mutual TLS using custom certificates provided by the customer.
* **Secrets:** A secret token. The secret name is configurable as is whether it appears in the HTTP header or as a URL parameter.
* **OAuth2 (client\_credentials):** Client credentials to fetch tokens from an authentication server.

Expected Load

Target servers should be able to support receiving transcript POST messages for each utterance of every live conversation on which AI Transcribe is active.

For reference, an average live call sends approximately 10 messages per minute. At that rate, 50 concurrent live calls represent approximately 8 messages per second.

Please ensure you load test the selected target server to support anticipated peaks in concurrent call volume.

Transcript Timing and Format

Once you have started transcription for a given call stream using the `/start-streaming` endpoint, AI Transcribe begins to publish `transcript` messages, each of which contains a full utterance for a single call participant.

The expected latency between when ASAPP receives audio for a completed utterance and provides a transcription of that same utterance is 200-600ms.

<Note>
  Perceived latency will also be influenced by any network delay sending audio to ASAPP and receiving transcription messages in return.
</Note>

Though we send messages in the order they are transcribed, network latency may impact the order in which they arrive or cause the system to drop messages due to timeouts. Where latency causes timeouts, the system will drop the oldest pending messages first; AI Transcribe does not retry to deliver dropped messages.

The message body for `transcript` type messages is JSON encoded with these fields:

| Field                  | Subfield   | Description                                                                                                                             | Example Value                        |
| :--------------------- | :--------- | :-------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------- |
| externalConversationId |            | Unique identifier with the Genesys conversation Id for the call                                                                         | 8c259fea-8764-4a92-adc4-73572e9cf016 |
| streamId               |            | Unique identifier that ASAPP assigns to each call participant's stream returned in response to `/start-streaming` and `/stop-streaming` | 5ce2b755-3f38-11ed-b755-7aed4b5c38d5 |
| sender                 | externalId | Customer or agent identifier as provided in request to `/start-streaming`                                                               | ef53245                              |
| sender                 | role       | A participant role, either customer or agent                                                                                            | customer, agent                      |
| autotranscribeResponse | message    | Type of message                                                                                                                         | transcript                           |
| autotranscribeResponse | start      | The start ms of the utterance                                                                                                           | 0                                    |
| autotranscribeResponse | end        | Elapsed ms since the start of the utterance                                                                                             | 1000                                 |
| autotranscribeResponse | utterance  | Transcribed utterance text                                                                                                              | Are you there?                       |

Expected `transcript` message format:

```json  theme={null}
{
  "type": "transcript",
  "externalConversationId": "<conversationId>",
  "streamId": "<streamId>",
  "sender": {
    "externalId": "<id>",
    "role": "customer",  // or "agent"
  },
  "autotranscribeResponse": {
    "message": "transcript",
    "start": 0,
    "end": 1000,
    "utterance": [
       {"text": "<transcript text>"}
      ]
  }
}
```

## Error Handling

Should your target server return an error in response to a POST request, ASAPP will record the error details for the failed message delivery and drop the message.

### After-Call via GET Request

AI Transcribe makes a full transcript available at the following endpoint for a given completed call:

`GET /conversation/v1/conversation/messages`

Once a conversation is complete, make a request to the endpoint using a conversation identifier and the system returns every message in the conversation.

Message Limit

This endpoint responds with up to 1,000 transcribed messages per conversation, approximately a two-hour continuous call. You receive all messages in a single response without any pagination.

To retrieve all messages for calls that exceed this limit, use either a real-time mechanism or File Exporter for transcript retrieval.

<Note>
  You set transcription settings (e.g., language, detailed tokens, redaction) for a given call with the Start/Stop API when you initiate call transcription. All transcripts retrieved after the call will reflect the initially requested settings with the Start/Stop API.
</Note>

See the [Endpoints](#endpoints) section to learn how to interact with this API.

### Batch via File Exporter

AI Transcribe makes full transcripts for batches of calls available using the File Exporter service's `utterances` data feed.

You can use the File Exporter service as a batch mechanism for exporting data to your data warehouse, either on a scheduled basis (e.g., nightly, weekly) or for ad hoc analyses. Data that populates feeds for the File Exporter service updates once daily at 2:00AM UTC.

## Use Case Example

Real-Time Transcription

This real-time transcription use case example consists of an English language call between an agent and customer with redaction enabled, ending with a hold. Note that redaction is enabled by default and does not need to be requested explicitly.

1. Ensure the Genesys AudioHook is enabled and configured on the desired trunk and flow.
2. When the customer and agent are connected, send ASAPP a request to start transcription for the call:

   **POST** `/mg-autotranscribe/v1/start-streaming`

   **Request**

```json  theme={null}
    {
      "namespace": "genesysaudiohook",
      "guid": "090eaa2f-72fa-480a-83e0-8667ff89c0ec",
      "customerId": "TT9833237",
      "agentId": "RE223444211993",
      "autotranscribeParams": {
        "language": "en-US"
      }
    }  
```

**Response**

*STATUS 200: Router processed the request, details are in the response body*

```json  theme={null}
    {
     "isOk": true,
     "autotranscribeResponse": {
       "customer": {
         "streamId": "5ce2b755-3f38-11ed-b755-7aed4b5c38d5",
         "status": {
           "code": 1000,
           "description": "OK"
         }
       },
       "agent": {
         "streamId": "cf31116-3f38-11ed-9116-7a0a36c763f1",
         "status": {
           "code": 1000,
           "description": "OK"
         }
       }
     }
    }
```

3. The agent and customer begin their conversation and ASAPP's webhook publisher sends separate HTTPS POST `transcript` messages for each participant to a target endpoint configured to receive the messages.

   HTTPS **POST** for Customer Utterance

```json  theme={null}
    {
      type: "transcript",
      externalConversationId: "8c259fea-8764-4a92-adc4-73572e9cf016",
      streamId: "5ce2b755-3f38-11ed-b755-7aed4b5c38d5",
      sender: {
        externalId: "TT9833237",
        role: "customer",
      },
      autotranscribeResponse: {
        message: 'transcript',
        start: 400,
        end: 3968,
        utterance: [
           {text: "I need help upgrading my streaming package and my PIN number is ####"}
          ]
      }
    }
```

HTTPS **POST** for Agent Utterance

```json  theme={null}
    {
      type: "transcript",
      externalConversationId: "8c259fea-8764-4a92-adc4-73572e9cf016",
      streamId: "cf31116-3f38-11ed-9116-7a0a36c763f1",
      sender: {
        externalId: "RE223444211993",
        role: "agent",
      },
      autotranscribeResponse: {
        message: 'transcript',
        start: 4744,
        end: 8031,
        utterance: [
           {text: "Thank you sir, let me pull up your account."}
          ]
      }
    }
```

4. Later in the conversation, the agent puts the customer on hold. This triggers a request to the `/stop-streaming` endpoint to pause transcription and prevents hold music and promotional messages from being transcribed.

   **POST** `/mg-autotranscribe/v1/stop-streaming`

   **Request**

```json  theme={null}
    {
     "namespace": "genesysaudiohook",
     "guid": "8c259fea-8764-4a92-adc4-73572e9cf016",
    }
```

**Response**

*STATUS 200: Router processed the request, details are in the response body*

```json  theme={null}
    {
     "isOk": true,
     "autotranscribeResponse": {
       "customer": {
         "streamId": "5ce2b755-3f38-11ed-b755-7aed4b5c38d5",
         "status": {
           "code": 1000,
           "description": "OK"
         },
         "summary": {
           "totalAudioBytes": 1334720,
           "audioDurationMs": 83420,
           "streamingSeconds": 84,
           "transcripts": 2
         },
       "agent": {
         "streamId": "cf31116-3f38-11ed-9116-7a0a36c763f1",
         "status": {
           "code": 1000,
           "description": "OK"
         },
         "summary": {
           "totalAudioBytes": 1334720,
           "audioDurationMs": 83420,
           "streamingSeconds": 84,
           "transcripts": 2
         },
       }
     }
    }
```

### Data Security

ASAPP's security protocols protect data at each point of transmission, from first user authentication to secure communications to our auditing and logging system (which includes hashing of data in transit) all the way to securing the environment when data is at rest in the data logging system. ASAPP teams also operate under tight restraints in terms of access to data. These security protocols protect both ASAPP and its customers.
