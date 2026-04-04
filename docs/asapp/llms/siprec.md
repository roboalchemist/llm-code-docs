# Source: https://docs.asapp.com/ai-productivity/ai-transcribe/siprec.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy AI Transcribe into SIPREC via Media Gateway

> Integrate AI Transcribe into your SIPREC system using ASAPP Media Gateway

This guide covers the **SIPREC Media Gateway** solution pattern, which consists of the following components to receive speech audio and call signals, and return call transcripts:

* Session border controllers and media gateways for receiving call audio from your session border controllers (SBCs)
* HTTPS API to receive requests to start and stop call transcription
* Webhook to POST real-time transcripts to a designated URL of your choosing, alongside two additional APIs to retrieve transcripts after-call for one or a batch of conversations

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1dced95e-7af4-160d-04a5-fa44d60214ee.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=01799c860fc31c1bc74701ec31bf9062" data-og-width="1830" width="1830" data-og-height="1027" height="1027" data-path="image/uuid-1dced95e-7af4-160d-04a5-fa44d60214ee.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1dced95e-7af4-160d-04a5-fa44d60214ee.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=e607af4b342bbc75187db784c388c73e 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1dced95e-7af4-160d-04a5-fa44d60214ee.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=1306884a2c56469ea8c15fe1009cea6c 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1dced95e-7af4-160d-04a5-fa44d60214ee.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=e21ec47327bb035d3c8b2f1604cc1959 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1dced95e-7af4-160d-04a5-fa44d60214ee.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=b014a3d65ad0cb591c51e4a47e358475 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1dced95e-7af4-160d-04a5-fa44d60214ee.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=fc6667be64c4eb21842620f37c5780f4 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1dced95e-7af4-160d-04a5-fa44d60214ee.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=0f2465b5214acaf359bc709aa77796df 2500w" />
</Frame>

ASAPP works with you to understand your current telephony infrastructure and ecosystem, including the type of voice work assignment platform(s) and other capabilities available, such as SIPREC.

Your ASAPP account team will also determine the main use case(s) for the transcript data to determine where and how call transcripts should be sent.

ASAPP then completes the architecture definition, including integration points into the existing infrastructure.

### Integration Steps

There are three steps to integrate AI Transcribe into SIPREC:

1. Send Audio to Media Gateway
2. Send Start and Stop Requests
3. Receiving Transcript Outputs

### Requirements

**Audio Stream Codec**

With SIPREC, the customer SBC and the ASAPP media gateway negotiate the media attributes via the SDP offer/answer exchange during the establishment of the session. The codecs in use today are as follows:

* G.711
* G.729

<Note>
  When supplying recorded audio to ASAPP for AI Transcribe model training prior to implementation, send uncompressed `.WAV` media files with speaker-separated channels.
  Recordings for training and real-time streams should have both the same sample rate (8000 samples/sec) and audio encoding (16-bit PCM).
  See the [Customization section of the AI Transcribe Product Guide](/ai-productivity/ai-transcribe/product-guide#customization) for more on data requirements for transcription model training.
</Note>

**Developer Portal**

ASAPP provides an AI Services [Developer Portal](/getting-started/developers). Within the portal, developers can do the following:

* Access relevant API documentation (e.g. OpenAPI reference schemas)
* Access API keys for authorization
* Manage user accounts and apps

<Tip>
  Visit the [Get Started](/getting-started/developers) for instructions on creating a developer account, managing teams and apps, and setting up AI Service APIs.
</Tip>

## Integrate to the Media Gateway

### 1. Send Audio to Media Gateway

Media Gateway (MG) and Media Gateway Proxy (MG Proxy) components receive real-time audio via SIPREC protocol (acting as Session Recording Servers) along with metadata and send it to AI Transcribe.

ASAPP offers a software-as-a-service approach to hosting MGs and MG Proxies at ASAPP's VPC in the PCI-scoped zone.

**Network Connectivity**

ASAPP will determine the network connectivity between your infrastructure and the ASAPP AWS Virtual Private Cloud (VPC) based on the architecture; however, we will deploy secure connections between your data centers and the ASAPP VPC.

* **Edge layer**: ASAPP has built an edge layer utilizing public IPv4 addresses registered to ASAPP. These IP addresses are NOT routed over the Internet, but they guarantee uniqueness across all IP networks. The edge layer houses firewalls and session border controllers that properly handle full NAT for both SIP and non-SIP traffic.
* **Customer connection aggregation**: ASAPP connects to customers via AWS Transit Gateway, which allows establishment of multiple route-based VPN connections to customers. Sample configuration for various customer devices is available on request.

**Port Details**

Ports and protocols in use for the AI Transcribe implementations are shown below. These definitions provide visibility to your security teams for the provisioning of firewalls and ACLs.

* **SIP/SIPREC:** TCP 5070 and above; your ASAPP account team will specify a value for your implementation
* **Audio Streams:** UDP \<RTP/RTCP port range>; your ASAPP account team will specify a value for your implementation
* **API Endpoints:** TCP 443

In customer firewalls, you must disable the SIP Application Layer Gateway (ALG) and any 'Threat Detection' features, as they typically interfere with the SIP dialogs and the re-INVITE process.

#### Generating Call Identifiers

AI Transcribe uses your call identifier to ensure a given call can be referenced in subsequent start and stop requests and associated with transcripts.

To ensure ASAPP receives your call identifiers properly, configure the SBC to create a universal call identifier (UCID or equivalent identifier).

<Note>
  UCID generation is a native feature for session border controller platforms.

  For example, the Oracle/Acme Packet session border controller platform provides documentation on UCID generation as part of its [configuration guide](https://docs.oracle.com/en/industries/communications/enterprise-session-border-controller/8.4.0/configuration/universal-call-identifier-spl). 

  Other session border controller vendors have similar features, so please refer to the vendor documentation for guidance.
</Note>

### 2. Send Start and Stop Requests

As outlined above in requirements, you must create user accounts in the developer portal to enroll apps and receive API keys to interact with ASAPP endpoints.

The `/start-streaming` and `/stop-streaming` endpoints of the Start/Stop API control when transcription occurs for every call media stream (identified by the GUID/UCID) sent to ASAPP's media gateway.

See the [Endpoints](#endpoints) section to learn how to interact with them.

ASAPP will not begin transcribing call audio until you request it to, thus preventing transcription of audio at the very beginning of the SIPREC session such as standard IVR menus and hold music.

Stop requests pause or end transcription for any needed reason. For example, you could use a stop request mid-call when the agent places the call on hold or at the end of the call to prevent transcribing post-call interactions such as satisfaction surveys.

<Note>
  AI Transcribe is only meant to transcribe conversations between customers and agents - you should implement start and stop requests to ensure the system does not transcribe non-conversation audio (e.g., hold music, IVR menus, surveys). Attempted transcription of non-conversation audio will negatively impact other services meant to consume conversation transcripts, such as ASAPP AI Summary.
</Note>

### 3. Receiving Transcript Outputs

AI Transcribe outputs transcripts using three separate mechanisms, each corresponding to a different temporal use case:

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

**Expected Load**

Target servers should be able to support receiving transcript POST messages for each utterance of every live conversation on which AI Transcribe is active.

For reference, an average live call sends approximately 10 messages per minute. At that rate, 50 concurrent live calls represent approximately 8 messages per second.

Please ensure you load test the selected target server to support anticipated peaks in concurrent call volume.

**Transcript Timing and Format**

See the [API Reference](/apis/overview)  to learn how to interact with this API.

The expected latency between when ASAPP receives audio for a completed utterance and provides a transcription of that same utterance is 200-600ms.

<Note>
  Perceived latency will also be influenced by any network delay sending audio to ASAPP and receiving transcription messages in return.
</Note>

Though we send messages in the order they are transcribed, network latency may impact the order in which they arrive or cause the system to drop messages due to timeouts. Where latency causes timeouts, the system will drop the oldest pending messages first; AI Transcribe does not retry to deliver dropped messages.

The message body for `transcript` type messages is JSON encoded with these fields:

| Field                  | Sub field  | Description                                                                                                                             | Example Value                                |                 |
| :--------------------- | :--------- | :-------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------- | --------------- |
| externalConversationId |            | Unique identifier with the GUID/UCID of the SIPREC call                                                                                 | 00002542391662063156                         |                 |
| streamId               |            | Unique identifier that ASAPP assigns to each call participant's stream returned in response to `/start-streaming` and `/stop-streaming` | 5ce2b755-3f38-11ed-b755-7aed4b5c38d5         |                 |
| sender                 | externalId | Customer or agent identifier as provided in request to `/start-streaming`                                                               | ef53245                                      |                 |
|                        | role       |                                                                                                                                         | A participant role, either customer or agent | customer, agent |
| autotranscribeResponse | message    | Type of message                                                                                                                         | transcript                                   |                 |
|                        | start      | The start ms of the utterance                                                                                                           | 0                                            |                 |
|                        | end        | Elapsed ms since the start of the utterance                                                                                             | 1000                                         |                 |
|                        | utterance  | text                                                                                                                                    | Transcribed utterance text                   | Are you there?  |

Expected `transcript` message format:

```json  theme={null}
{
  "type": "transcript",
  "externalConversationId": "<guid>",
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

**Error Handling**

Should your target server return an error in response to a POST request, ASAPP will record the error details for the failed message delivery and drop the message.

#### After-Call via GET Request

AI Transcribe makes a full transcript available at the following endpoint for a given completed call:

`GET /conversation/v1/conversation/messages`
Once a conversation is complete, make a request to the endpoint using a conversation identifier and the system returns every message in the conversation.

**Message Limit**

This endpoint responds with up to 1,000 transcribed messages per conversation, approximately a two-hour continuous call. You receive all messages in a single response without any pagination.

To retrieve all messages for calls that exceed this limit, use either a real-time mechanism or File Exporter for transcript retrieval.

<Note>
  You set transcription settings (e.g., language, detailed tokens, redaction) for a given call with the Start/Stop API when you initiate call transcription.

  All transcripts retrieved after the call will reflect the initially requested settings with the Start/Stop API.
</Note>

See the [Endpoints](#endpoints) section to learn how to interact with this API.

#### Batch via File Exporter

AI Transcribe makes full transcripts for batches of calls available using the File Exporter service's `utterances` data feed.

You can use the File Exporter service as a batch mechanism for exporting data to your data warehouse, either on a scheduled basis (e.g., nightly, weekly) or for ad hoc analyses. Data that populates feeds for the File Exporter service updates once daily at 2:00AM UTC.

Visit [Retrieving Data for AI Services](/reporting/file-exporter) for a guide on how to interact with the File Exporter service.

## Usage

### Endpoints

ASAPP receives start/stop requests to signal when transcription for a given call should occur. You can send start and stop requests multiple times during a single call (for example, stopped when an agent places the call on hold and resumed when the agent resumes the call).

<Note>
  For all requests, you must provide a header containing the `asapp-api-id` API Key and the `asapp-api-secret`. You can find them under your Apps in the [AI Services Developer Portal](https://developer.asapp.com/).

  All requests to ASAPP sandbox and production APIs must use `HTTPS` protocol. Traffic using `HTTP` will not be redirected to `HTTPS`.
</Note>

[`POST /mg-autotranscribe/v1/start-streaming/`](/apis/autotranscribe-media-gateway/start-streaming)

Use this endpoint to tell ASAPP to start or resume transcription for a given call.

**When to Call**

Transcription can be started (or resumed after a [`/stop-streaming`](/apis/autotranscribe-media-gateway/stop-streaming) request) at any point during a call.

**Request Details**

Requests must include a call identifier with the GUID/UCID of the SIPREC call, a namespace (e.g., `siprec`), and an identifier from your system(s) for each of the customer and agent participants on the call.

Agent identifiers provided here can tell ASAPP whether agents have changed, indicating a new leg of the call has begun. This agent information enables other services to target specific legs of calls rather than only the higher-level call.

<Note>
  The `guid` field expects the decimal formatting of the identifier.

  Cisco example: `0867617078-0032318833-2221801472-0002236962`

  Avaya example: `00002542391662063156`
</Note>

Requests also include a parameter to indicate the mapping of media lines (m-lines) in the SDP of SIPREC protocol; the parameter specifies whether the top m-line is mapped to the agent or customer participant. The top m-line is typically reversed for outbound calls vs. inbound calls.

Requests may also include optional parameters for transcription including:

* Language (e.g., `en-us` for English or `es-us` for Spanish)
* Whether detailed tokens are requested
* Whether call audio recording is permitted
* Whether transcribed outputs should be redacted, unredacted, or both redacted and unredacted outputs should be returned

<Note>
  AI Transcribe can immediately redact audio for sensitive information, returning utterances with sensitive information denoted in hashmarks. Visit [Redaction Policies](/security/data-redaction/redaction-policies) to learn more.
</Note>

**Response Details**

When successful, this endpoint responds with a boolean indicating whether the stream has started successfully along with a `customer` and `agent` object. Each object contains a stream identifier (`streamId`), status code and status description.

[`POST /mg-autotranscribe/v1/stop-streaming/`](/apis/autotranscribe-media-gateway/stop-streaming)

Use this endpoint to tell ASAPP to pause or end transcription for a given call.

**When to Call**

Transcription can be stopped at any point during a call.

**Request Details**

Requests must include a call identifier with the GUID/UCID of the SIPREC call and a namespace (e.g., `siprec`).

<Note>
  The `guid` field expects the decimal formatting of the identifier.

  Cisco example: `0867617078-0032318833-2221801472-0002236962`

  Avaya example: `00002542391662063156`
</Note>

**Response Details**

When successful, this endpoint responds with a boolean indicating whether the stream has stopped successfully along with a `customer` and `agent` object. Each object contains a stream identifier (`streamId`), status code and status description. Each object also contains a `summary` object of transcription stats related to that participant's stream.

[`GET /conversation/v1/conversation/messages`](/apis/messages/list-messages-with-an-externalid)

Use this endpoint to retrieve all the transcript messages for a completed call.

**When to Call**

Once the conversation is complete. Conversation transcripts are available for seven days after they are completed.

<Note>
  For conversations that include transfers, the endpoint will provide transcript messages for all call legs that correspond to the call's identifier.
</Note>

**Request Details**

Requests must include a call identifier with the GUID/UCID of the SIPREC call.

**Response Details**

When successful, this endpoint responds with an array of objects, each of which corresponds to a single message. Each object contains the text of the message, the sender's role and identifier, a unique message identifier, and timestamps.

#### Error Handling

ASAPP uses HTTP status codes to communicate the success or failure of an API Call.

* 2XX HTTP status codes are for successful API calls.
* 4XX and 5XX HTTP status codes are for errored API calls.

ASAPP errors are returned in the following structure:

```json  theme={null}
{
    "error": {
        "requestId": "67441da5-dd2b-4820-b47d-441998f066e9",
        "message": "Bad request",
        "code": "400-02"
    }
}
```

When using the `/start-streaming` and `/stop-streaming` endpoints, the system may return the following error codes:

| Code      | Description                                           |
| :-------- | :---------------------------------------------------- |
| `400-201` | MG AI Transcribe API parameter incorrect              |
| `400-202` | AI Transcribe parameter or combination incorrect      |
| `400-203` | No call with specified guid found                     |
| `409-201` | Call transcription already started or already stopped |
| `409-202` | Another API request for same guid is pending          |
| `409-203` | SIPREC BYE being processed                            |
| `500-201` | MG AI Transcribe or AI Transcribe internal error      |

#### Data Security

ASAPP's security protocols protect data at each point of transmission from first user authentication, to secure communications, to our auditing and logging system, all the way to securing the environment when data is at rest in the data logging system. Access to data by ASAPP teams is tightly constrained and monitored. Strict security protocols protect both ASAPP and our customers.

## Use Case Example

### Real-Time Transcription

This real-time transcription use case example consists of an English language call between an agent and customer with redaction enabled, ending with a hold. Note that redaction is enabled by default and does not need to be requested explicitly.

1. When the call record is created, ASAPP media gateway components receive real-time audio via SIPREC protocol along with metadata, most notably the call's Avaya-formatted UCID/GUID: `00002542391662063156`
2. When the customer and agent are connected, ASAPP is sent a request to start transcription for the call:

**POST** `/mg-autotranscribe/v1/start-streaming`

**Request**

```json  theme={null}
    {
     "namespace": "siprec",
     "guid": "00002542391662063156",
     "customerId": "TT9833237",
     "agentId": "RE223444211993",
     "autotranscribeParams": {
       "language": "en-US"
     },
     "siprecParams": {
       "mediaLineOrder": "CUSTOMER_FIRST"
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

**HTTPS POST for Customer Utterance**

```json  theme={null}
    {
      type: "transcript",
      externalConversationId: "00002542391662063156",
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

**HTTPS POST for Agent Utterance**

```json  theme={null}
    {
      type: "transcript",
      externalConversationId: "00002542391662063156",
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
     "namespace": "siprec",
     "guid": "00002542391662063156",
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
