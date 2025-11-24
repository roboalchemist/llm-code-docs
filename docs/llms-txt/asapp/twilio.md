# Source: https://docs.asapp.com/autotranscribe/twilio.md

# Deploying AutoTranscribe for Twilio

> Use AutoTranscribe with Twilio

This guide covers the **Twilio Media Gateway** solution pattern, which consists of the following components to receive speech audio from Twilio, receive call signals, and return call transcripts:

* Media gateways for receiving call audio from Twilio
* HTTPS API which enables the customer to GET a streaming URL to which call audio is sent and POST requests to start and stop call transcription
* Webhook to POST real-time transcripts to a designated URL of your choosing, alongside two additional APIs to retrieve transcripts after-call for one or a batch of conversations

ASAPP works with you to understand your current telephony infrastructure and ecosystem.

Your ASAPP account team will also determine the main use case(s) for the transcript data to determine where and how call transcripts should be sent.

ASAPP then completes the architecture definition, including integration points into the existing infrastructure.

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7d518252-d6a2-da98-a595-edc3b3640295.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=3253cdd1c3875e4d1c2b6f204c6318f7" data-og-width="1245" width="1245" data-og-height="711" height="711" data-path="image/uuid-7d518252-d6a2-da98-a595-edc3b3640295.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7d518252-d6a2-da98-a595-edc3b3640295.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=b7d47725c776ed027a5bbd3fd0685fe3 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7d518252-d6a2-da98-a595-edc3b3640295.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=6c2e23823c3fdc7d8f6e231aa2edda9b 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7d518252-d6a2-da98-a595-edc3b3640295.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=d8274fc1d11ff37e3f12542289c2aa74 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7d518252-d6a2-da98-a595-edc3b3640295.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=a8c0c152ba8b11d98aafa84c2034e78c 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7d518252-d6a2-da98-a595-edc3b3640295.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=000e667b475563e31ce42218a952bb33 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7d518252-d6a2-da98-a595-edc3b3640295.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=2290f324fe983fb73ab142417b741b1c 2500w" />
</Frame>

### Integration Steps

There are four steps to integrate AutoTranscribe into Twilio:

1. Authenticate with ASAPP and Obtain a Twilio Media Stream URL
2. Send Audio to Media Gateway
3. Send Start and Stop Requests
4. Receive Transcript Outputs

### Requirements

**Audio Stream Codec**

Twilio provides audio in the mu-law format with 8000 sample rate, which is supported by ASAPP. No modification or additional transcoding is needed when forking audio to ASAPP.

<Note>
  When supplying recorded audio to ASAPP for AutoTranscribe model training prior to implementation, send uncompressed .WAV media files with speaker-separated channels.
</Note>

Recordings for training should have a sample rate of 8000 and 16-bit PCM audio encoding.

See the [Customization section of the AutoTranscribe Product Guide](/autotranscribe/product-guide#customization) for more on data requirements for transcription model training.

**Developer Portal**

ASAPP provides an AI Services [Developer Portal](/getting-started/developers). Within the portal, developers can do the following:

* Access relevant API documentation (e.g. OpenAPI reference schemas)
* Access API keys for authorization
* Manage user accounts and apps

<Tip>
  Visit the [Get Started](/getting-started/developers) for instructions on creating a developer account, managing teams and apps, and setup for using AI Service APIs.
</Tip>

## Integrate with Twilio

### 1. Authenticate with ASAPP and Obtain a Twilio Media Stream URL

A Twilio media stream URL is required to start streaming audio. Begin by authenticating with ASAPP to obtain this URL.

<Note>
  All requests to ASAPP sandbox and production APIs must use `HTTPS` protocol. Traffic using `HTTP` will not be redirected to `HTTPS`.
</Note>

The following HTTPS REST API enables authentication with the ASAPP API Gateway:

[`GET /mg-autotranscribe/v1/twilio-media-stream-url`](/apis/autotranscribe-media-gateway/get-twilio-media-stream-url)

HTTP headers (required):

```json  theme={null}
{
    "asapp-api-id": <asapp provided api id>,
    "asapp-api-secret": <asapp provided api secret>
}
```

Header parameters are required and are provided to you by ASAPP in the [Developer Portal](https://developer.asapp.com/).
HTTP response body:

```json  theme={null}
{
   "streamingUrl": "<short-lived URL for twilio media stream>"
}
```

If the authentication succeeds, a secure WebSocket short-lived access URL will be returned in the HTTP response body. TTL (time-to-live) for this URL is 5 minutes.  Validity of the short-lived URL is checked only at the beginning of the WebSocket connection, so duration of the sessions can be as long as needed.  The same short-lived access URL can be used to start as many unique sessions as desired in the 5 minute TTL.

For example, if the call center has an average rate of 1 new call per second, the same short-lived access URL can be used to initiate 300 total calls (60 calls per minute \* 5 minutes).  And each call can last as long as needed, regardless if it's 2 minutes long or longer than 30 minutes.  But after the five minute TTL, a new short-lived access URL will need to be obtained to start any new calls.  It is recommended to obtain a new short-lived URL in less than 5 minutes to always have a valid URL.

### 2. Send Audio to Media Gateway

With the URL obtained in the previous step, instruct Twilio to start sending Media Stream to ASAPP Media Gateway components.  Media Gateway (MG) components are responsible for receiving real-time audio along with Call SID metadata.

<Note>
  Twilio provides multiple ways to initiate Media Stream, which are described in [their documentation](https://www.twilio.com/docs/voice/api/media-streams#startstop-media-streams).
</Note>

While instructing Twilio to send Media Streams, it's highly recommended to provide a `statusCallback` URL. Twilio will use this URL in the event connectivity is lost or has an error.  It will be up to the customer call center to process this callback and instruct Twilio to again start new Media Streams, assuming transcriptions are still desired. 

<Tip>
  See Handling Failures for Twilio Media Streams for details below.
</Tip>

ASAPP offers a software-as-a-service approach to hosting MGs at ASAPP's VPC in the PCI-scoped zone.

**Network Connectivity**

Audio will be sent from Twilio cloud to ASAPP cloud via secure (TLS 1.2) WebSocket connections over the internet.  No additional or custom networking is required.

**Port Details**

Ports and protocols in use for the AutoTranscribe implementations are shown below:

* **Audio Streams**: Secure WebSocket with destination port 443
* **API Endpoints**: TCP 443

**Handling Failures for Twilio Media Streams**

There are multiple reasons (e.g. intermediate internet failures, scheduled maintenance) why Twilio Media Stream could be interrupted mid-call. The only way to know that the Media Stream was interrupted is to utilize the `statusCallback` parameter (along with `statusCallbackMethod` if needed) of the Twilio API. Should a failure occur, the URL specified in `statusCallback` parameter will receive the HTTP request informing of a failure.

If a failure notification is received, it means ASAPP has stopped receiving audio from Twilio and no more transcriptions for that call will take place. To restart transcriptions:

* Obtain a Twilio Media Stream URL - unless failure occurred within 5 minutes of the start of the call, you won't be able to reuse the original call streaming URL.
* Send Audio to Media Gateway - instruct Twilio through their API to start a new media stream to the Twilio Media Stream URL provided by ASAPP.
* Send Start request (see [3. Sending Start and Stop Requests](#3-send-start-and-stop-requests) for details).

**Generating Call Identifiers**

AutoTranscribe uses your call identifier to ensure a given call can be referenced in subsequent [start and stop requests](#3-send-start-and-stop-requests) and associated with transcripts.

Twilio will automatically generate a unique Call SID identifier for the call.

### 3. Send Start and Stop Requests

As outlined in [requirements](#requirements), user accounts must be created in the developer portal in order to enroll apps and receive API keys to interact with ASAPP endpoints.

The `/start-streaming` and `/stop-streaming` endpoints of the Start/Stop API are used to control when transcription occurs for every call.

See the [API Reference](/apis/overview)  to learn how to interact with this API.

ASAPP will not begin transcribing call audio until requested to, thus preventing transcription of audio at the very beginning of the audio streaming session, which may include IVR, hold music, or queueing.

Stop requests are used to pause or end transcription for any needed reason. For example, a stop request could be used mid-call when the agent places the call on hold or at the end of the call to prevent transcribing post-call interactions such as satisfaction surveys.

<note>
  AutoTranscribe is only meant to transcribe conversations between customers and agents - start and stop requests should be implemented to ensure non-conversation audio (e.g. hold music, IVR menus, surveys) is not being transcribed. Attempted transcription of non-conversation audio will negatively impact other services meant to consume conversation transcripts, such as ASAPP AutoSummary.
</note>

### 4. Receive Transcript Outputs

AutoTranscribe outputs transcripts using three separate mechanisms, each corresponding to a different temporal use case:

* **[Real-time](#real-time-via-webhook)**: Webhook posts complete utterances to your target endpoint as they are transcribed during the live conversation
* **[After-call](#after-call-via-get-request)**: GET endpoint responds to your requests for a designated call with the full set of utterances from that completed conversation
* **[Batch](#batch-via-file-exporter)**: File Exporter service responds to your request for a designated time interval with a link to a data feed file that includes all utterances from that interval's conversations

#### Real-Time via Webhook

ASAPP sends transcript outputs in real-time via HTTPS POST requests to a target URL of your choosing.

Authentication

Once the target is selected, work with your ASAPP account team to implement one of the following supported authentication mechanisms:

* **Custom CAs:** Custom CA certificates for regular TLS (1.2 or above).
* **mTLS:** Mutual TLS using custom certificates provided by the customer.
* **Secrets:** A secret token. The secret name is configurable as is whether it appears in the HTTP header or as a URL parameter.
* **OAuth2 (client\_credentials):** Client credentials to fetch tokens from an authentication server.

Expected Load

Target servers should be able to support receiving transcript POST messages for each utterance of every live conversation on which AutoTranscribe is active.

For reference, an average live call sends approximately 10 messages per minute. At that rate, 50 concurrent live calls represents approximately 8 messages per second.

Please ensure the selected target server is load tested to support anticipated peaks in concurrent call volume.

Transcript Timing and Format

Once you have started transcription for a given call stream using the `/start-streaming` endpoint, AutoTranscribe begins to publish `transcript` messages, each of which contains a full utterance for a single call participant.

The expected latency between when ASAPP receives audio for a completed utterance and provides a transcription of that same utterance is 200-600ms.

<Note>
  Perceived latency will also be influenced by any network delay sending audio to ASAPP and receiving transcription messages in return.
</Note>

Though messages are sent in the order they are transcribed, network latency may impact the order in which they arrive or cause messages to be dropped due to timeouts. Where latency causes timeouts, the oldest pending messages will be dropped first; AutoTranscribe does not retry to deliver dropped messages.

The message body for `transcript` type messages is JSON encoded with these fields:

| Field                  | Subfield   | Description                                                                                                                            | Example Value                        |
| :--------------------- | :--------- | :------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------- |
| externalConversationId |            | Unique identifier with the Amazon Connect Contact Id for the call                                                                      | 8c259fea-8764-4a92-adc4-73572e9cf016 |
| streamId               |            | Unique identifier assigned by ASAPP to each call participant's stream returned in response to `/start-streaming` and `/stop-streaming` | 5ce2b755-3f38-11ed-b755-7aed4b5c38d5 |
| sender                 | externalId | Customer or agent identifier as provided in request to `/start-streaming`                                                              | ef53245                              |
| sender                 | role       | A participant role, either customer or agent                                                                                           | customer, agent                      |
| autotranscribeResponse | message    | Type of message                                                                                                                        | transcript                           |
| autotranscribeResponse | start      | The start ms of the utterance                                                                                                          | 0                                    |
| autotranscribeResponse | end        | Elapsed ms since the start of the utterance                                                                                            | 1000                                 |
| autotranscribeResponse | utterance  | Transcribed utterance text                                                                                                             | Are you there?                       |

Expected `transcript` message format:

```json  theme={null}
{
  "type": "transcript",
  "externalConversationId": "<twilio call SID>",
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

Error Handling

Should your target server return an error in response to a POST request, ASAPP will record the error details for the failed message delivery and drop the message.

#### After-Call via GET Request

AutoTranscribe makes a full transcript available at the following endpoint for a given completed call:

`GET /conversation/v1/conversation/messages`

Once a conversation is complete, make a request to the endpoint using a conversation identifier and receive back every message in the conversation.

Message Limit

This endpoint will respond with up to 1,000 transcribed messages per conversation, approximately a two-hour continuous call. All messages are received in a single response without any pagination.

To retrieve all messages for calls that exceed this limit, use either a real-time mechanism or File Exporter for transcript retrieval.

<Note>
  Transcription settings (e.g. language, detailed tokens, redaction), for a given call are set with the Start/Stop API, when call transcription is initiated. All transcripts retrieved after the call will reflect the initially requested settings with the Start/Stop API.
</Note>

See the [API Reference](/apis/overview)  to learn how to interact with this API.

#### Batch via File Exporter

AutoTranscribe makes full transcripts for batches of calls available using the File Exporter service's `utterances` data feed.

The File Exporter service is meant to be used as a batch mechanism for exporting data to your data warehouse, either on a scheduled basis (e.g. nightly, weekly) or for ad hoc analyses. Data that populates feeds for the File Exporter service updates once daily at 2:00AM UTC.

Visit [Retrieving Data from ASAPP](https://asapp.mintlify.app/reporting/data-from-messaging-platform) for a guide on how to interact with the File Exporter service.

## Use Case Example

Real-Time Transcription

This real-time transcription use case example consists of an English language call between an agent and customer with redaction enabled, ending with a hold. Note that redaction is enabled by default and does not need to be requested explicitly.

1. Obtain a Twilio media streaming URL destination by authenticating with ASAPP.

   **GET** `/mg-autotranscribe/v1/twilio-media-stream-url`
   **Response**

   *STATUS 200: OK - Twilio media stream url in the response body*

```json  theme={null}
    {
      "streamingUrl": "wss://localhost/twilio-media?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    }
```

2. With the URL obtained in the previous step, instruct Twilio to start Media Stream to ASAPP media gateway components.  ASAPP will now receive real-time audio via Twilio Stream along with metadata, most notably the call's SID: `CA5b040e075515c424391012acc5a870cf`

3. When the customer and agent are connected, send ASAPP a request to start transcription for the call:

   **POST** `/mg-autotranscribe/v1/start-streaming`
   **Request**

```json  theme={null}
    {
     "namespace": "twilio",
     "guid": "CA5b040e075515c424391012acc5a870cf",
     "customerId": "TT9833237",
     "agentId": "RE223444211993",
     "autotranscribeParams": {
       "language": "en-US"
     },
     "twilioParams": {
       "trackMap": {
         "inbound": "customer",
         "outbound": "agent"
       }
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

4. The agent and customer begin their conversation and separate HTTPS POST `transcript` messages are sent for each participant from ASAPP's webhook publisher to a target endpoint configured to receive the messages.

   HTTPS **POST** for Customer Utterance

```json  theme={null}
    {
      type: "transcript",
      externalConversationId: "CA5b040e075515c424391012acc5a870cf",
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
      externalConversationId: "CA5b040e075515c424391012acc5a870cf",
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

5. Later in the conversation, the agent puts the customer on hold. This triggers a request to the `/stop-streaming` endpoint to pause transcription and prevents hold music and promotional messages from being transcribed.

   **POST** `/mg-autotranscribe/v1/stop-streaming`

   **Request**

```json  theme={null}
    {
     "namespace": "twilio",
     "guid": "CA5b040e075515c424391012acc5a870cf",
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

ASAPP's security protocols protect data at each point of transmission, from first user authentication to secure communications to our auditing and logging system (which includes hashing of data in transit) all the way to securing the environment when data is at rest in the data logging system. The teams at ASAPP are also under tight restraints in terms of access to data. These security protocols protect both ASAPP and its customers.
