# Source: https://docs.asapp.com/ai-productivity/ai-transcribe/amazon-connect.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploying AI Transcribe for Amazon Connect

> Use AI Transcribe in your Amazon Connect solution

## Overview

This guide covers the **Amazon Connect** solution pattern, which consists of the following components to receive speech audio and call signals, and return call transcripts:

* Media gateways for receiving call audio from Amazon Kinesis Video Streams
* Start/Stop API for Lambda functions to provide call data and signals for when to start and stop transcribing call audio

<Note>
  ASAPP can also accept requests to start and stop transcription via API from other call-state aware services. AWS Lambda functions are the approach outlined in this guide.
</Note>

* Required AWS IAM role to allow access to Kinesis Video Streams
* Webhook to POST real-time transcripts to a designated URL of your choosing, alongside two additional APIs to retrieve transcripts after-call

ASAPP works with you to understand your current telephony infrastructure and ecosystem.

Your ASAPP account team will also determine the main use case(s) for the transcript data to determine where and how call transcripts should be sent.

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cfc26616-6fec-757a-6bd9-91a8175d30ab.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=30046a84dff8a0d3b6ef1c2e95a63113" data-og-width="1888" width="1888" data-og-height="1092" height="1092" data-path="image/uuid-cfc26616-6fec-757a-6bd9-91a8175d30ab.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cfc26616-6fec-757a-6bd9-91a8175d30ab.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=247e09bbc3776ee12073e6ecad97ae90 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cfc26616-6fec-757a-6bd9-91a8175d30ab.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=045d9d1e2acc07304ff5c497b4869f7a 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cfc26616-6fec-757a-6bd9-91a8175d30ab.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=f8f594088dbe814d53b55f093c6170c8 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cfc26616-6fec-757a-6bd9-91a8175d30ab.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=701ae6d46b8d0e742aeda0a37d31d218 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cfc26616-6fec-757a-6bd9-91a8175d30ab.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=a56f3cb8fbc9eda2bf602b39571d6c07 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cfc26616-6fec-757a-6bd9-91a8175d30ab.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=5fbd2311c16f1dc6e22983dc704cba35 2500w" />
</Frame>

### Integration Steps

There are five parts of the integration process:

1. Setup Authentication for Kinesis Video Streams
2. Enable Audio Streaming to Kinesis Video Streams
3. Add Start Media and Stop Media To Flows
4. Send Start and Stop Requests to ASAPP
5. Receive Transcript Outputs

### Requirements

**Audio Stream Codec**

AWS Kinesis Video Streams provides MKV format, which ASAPP supports. You do not need any modification or additional transcoding when forking audio to ASAPP.

<Note>
  When supplying recorded audio to ASAPP for AI Transcribe model training prior to implementation, send uncompressed .WAV media files with speaker-separated channels.
</Note>

Recordings for training should have a sample rate of 8000 and 16-bit PCM audio encoding.

See the [Customization section of the AI Transcribe Product Guide](/ai-productivity/ai-transcribe/product-guide#customization) for more on data requirements for transcription model training.

**Developer Portal**

ASAPP provides an AI Services [Developer Portal](/getting-started/developers). Within the portal, developers can do the following:

* Access relevant API documentation (e.g. OpenAPI reference schemas)
* Access API keys for authorization
* Manage user accounts and apps

<Tip>
  Visit the [Get Started](/getting-started/developers) for instructions on creating a developer account, managing teams and apps, and setting up AI Service APIs.
</Tip>

## Integrate with Amazon Connect

### 1. Set Up Authentication for Kinesis Video Streams

The audio streams for Amazon Connect are stored in the Amazon Kinesis Video Streams service in your AWS account where the Amazon Connect instance resides. [IAM policies control](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-iam) the access to the Kinesis Video Streams service.

ASAPP will use [IAM Roles for Service accounts (IRSA)](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts) to receive a specific IAM role in the ASAPP account, for example `asapp-prod-mg-amazonconnect-role`.

Setup your account's IAM role (e.g., `kinesis-connect-access-role-for-asapp`) to trust `asapp-prod-mg-amazonconnect-role` to assume it and create a policy permitting list/read operations on appropriate Kinesis Video Streams associated with Amazon Connect instance.

### 2. Enable Audio Streaming to Kinesis Video Streams

ASAPP retrieves streaming audio by sending requests to Kinesis Video Streams. Streaming media is not enabled by default and you must turn it on manually.

Enable live media streaming for applicable instances in your Amazon Connect console to ensure audio is available when ASAPP sends requests to Kinesis Video Streams.

<Note>
  If you choose to use a non-default KMS key, ensure that the IAM role for Service Accounts (IRSA) created for ASAPP has access to this KMS key.

  Amazon provides [documentation to guide enabling live media streaming to Kinesis Video Streams](https://docs.aws.amazon.com/connect/latest/adminguide/enable-live-media-streams).
</Note>

### 3. Add Start Media and Stop Media To Flows

Sending streaming media to Kinesis Video Streams is initiated and stopped by inserting preset blocks - called **Start media streaming** and **Stop media streaming** - into Amazon Connect flows. Place these blocks into your flows to programmatically set when the system will stream and stop media - this determines what audio will be available for transcription.

Typically for ASAPP, audio streaming begins as close as possible to when the agent is assigned. Audio streaming typically stops ahead of parts of calls that should not be transcribed such as holds, transfers, and post-call surveys.

<Note>
  When placing the **Start media streaming** block, ensure **From the customer** and **To the customer** menu boxes are checked so that both participants' call media streams are available for transcription.
</Note>

Amazon provides [documentation on adding Start media streaming and Stop media streaming blocks](https://docs.aws.amazon.com/connect/latest/adminguide/use-media-streams-blocks) to Amazon Connect flows.

### 4. Send Start and Stop Requests to ASAPP

AWS Lambda functions can be inserted into Amazon Connect flows in order to send requests directly to ASAPP APIs to start and stop transcription.

<Note>
  ASAPP can also accept requests to start and stop transcription via API from other call-state aware services. If you are using another service to interact with ASAPP APIs, you can use AWS Lambda functions to send important call metadata to your other services before they send requests to ASAPP.

  The approach outlined in this guide is to call ASAPP APIs directly using AWS Lambda functions.
</Note>

As outlined in [Requirements](#requirements "Requirements"), user accounts must be created in the developer portal in order to enroll apps and receive API keys to interact with ASAPP endpoints.

Lambda functions (or any other service you use to interact with ASAPP APIs) require these API keys to send requests to start and stop transcription. See the [Endpoints](#endpoints "Endpoints") section to learn how to interact with them, including what you need to include in requests to each endpoint.

ASAPP will not begin transcribing call audio until you request it to, at which point we will request the audio from Kinesis Video Streams and begin transcribing.

With AWS Kinesis Video streams, there are 2 supported selectorTypes to start-streaming:

* **NOW**: NOW will start transcribing from the most recent audio data in the Kinesis stream.
* **FRAGMENT\_NUMBER**: FRAGMENT\_NUMBER will require another parameter afterFragmentNumber to be populated and would be the fragment within the media stream to start (for example, the start fragment number to capture all transcripts in the stream prior to start-streaming being called).

<Note>
  The `/start-streaming` endpoint request requires several fields, but three specific attributes must come from Amazon:

  * Amazon Connect Contact Id (multiple possible sources)
    JSONPath formats: `$.ContactId`, `$.InitialContactId`, `$.PreviousContactId`
  * Audio Stream ARN
    JSONPath format: `$.MediaStreams.Customer.Audio.StreamARN`
  * \[OPTIONAL] Start Fragment Number
    JSONPath format: `$.MediaStreams.Customer.Audio.StartFragmentNumber`
    Requests to `/start-streaming` also require agent and customer identifiers. These identifiers can be sourced from Amazon Connect but may also originate from other systems if your use case requires it.
</Note>

Stop requests pause or end transcription for any needed reason. For example, you could use a stop request when the agent initiates a transfer to another agent or queue or at the end of the call to prevent transcribing post-call interactions such as satisfaction surveys.

<Note>
  AI Transcribe is only meant to transcribe conversations between customers and agents - you should implement start and stop requests to ensure the system does not transcribe non-conversation audio (e.g., hold music, IVR menus, surveys). Attempted transcription of non-conversation audio will negatively impact other services meant to consume conversation transcripts, such as ASAPP AI Summary.
</Note>

#### Adding Lambda Functions to Flows

First, create and deploy two new Lambda functions in the AWS Lambda console: one for  sending a request to ASAPP's `/start-streaming` endpoint and another for sending a request to ASAPP's `/stop-streaming` endpoint.

<Note>
  Refer to the [API Reference in ASAPP's Developer Portal](/apis/autotranscribe-media-gateway/start-streaming) for detailed specifications for sending requests to each endpoint.
</Note>

Once Lambda functions are deployed and configured, add the Lambda functions to your Amazon Connect instance using the Amazon Connect console. Once added, the Lambda functions will be available for use in your existing applicable flows.

In Amazon Connect's flow tool, add an Invoke **AWS Lambda function** where you want to make a request to ASAPP's APIs.

* For requests to `/start-streaming` endpoint, place the Lambda block following the **Start media streaming** flow block
* For requests to `/stop-streaming` endpoint, place the Lambda block immediately before the **Stop media streaming** flow block.

Amazon provides [documentation on invoking AWS Lambda functions](https://docs.aws.amazon.com/connect/latest/adminguide/connect-lambda-functions).

### 5. Receive Transcript Outputs

AI Transcribe outputs transcripts using three separate mechanisms, each corresponding to a different temporal use case:

* **[Real-time](#real-time-via-webhook "Real-Time via Webhook")**: Webhook posts complete utterances to your target endpoint as they are transcribed during the live conversation
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

For reference, an average live call sends approximately 10 messages per minute. At that rate, 50 concurrent live calls represents approximately 8 messages per second.

Please ensure the selected target server is load tested to support anticipated peaks in concurrent call volume.

Transcript Timing and Format

Once you have started transcription for a given call stream using the `/start-streaming` endpoint, AI Transcribe begins to publish `transcript` messages, each of which contains a full utterance for a single call participant.

The expected latency between when ASAPP receives audio for a completed utterance and provides a transcription of that same utterance is 200-600ms.

<Note>
  Perceived latency will also be influenced by any network delay sending audio to ASAPP and receiving transcription messages in return.
</Note>

Though we send messages in the order they are transcribed, network latency may impact the order in which they arrive or cause messages to be dropped due to timeouts. Where latency causes timeouts, the system will drop the oldest pending messages first; AI Transcribe does not retry to deliver dropped messages.

The message body for `transcript` type messages is JSON encoded with these fields:

| Field                  | Subfield   | Description                                                                                                                             | Example Value                        |
| :--------------------- | :--------- | :-------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------- |
| externalConversationId |            | Unique identifier with the Amazon Connect Contact Id for the call                                                                       | 8c259fea-8764-4a92-adc4-73572e9cf016 |
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
  "externalConversationId": "<Amazon Connect Contact Id>",
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

### Message Limit

This endpoint responds with up to 1,000 transcribed messages per conversation, approximately a two-hour continuous call. You receive all messages in a single response without any pagination.

To retrieve all messages for calls that exceed this limit, use either a real-time mechanism or File Exporter for transcript retrieval.

<Note>
  You set transcription settings (e.g., language, detailed tokens, redaction) for a given call with the Start/Stop API when you initiate call transcription. All transcripts retrieved after the call will reflect the initially requested settings with the Start/Stop API.
</Note>

See the [Endpoints](#endpoints "Endpoints") section to learn how to interact with this API.

#### Batch via File Exporter

AI Transcribe makes full transcripts for batches of calls available using the File Exporter service's `utterances` data feed.

The File Exporter service is meant to be used as a batch mechanism for exporting data to your data warehouse, either on a scheduled basis (e.g. nightly, weekly) or for ad hoc analyses. Data that populates feeds for the File Exporter service updates once daily at 2:00AM UTC.

Visit [Retrieving Data from ASAPP Messaging](/reporting/file-exporter) for a guide on how to interact with the File Exporter service.

## Use Case Example

Real-Time Transcription

This real-time transcription use case example consists of an English language call between an agent and customer with redaction enabled, ending with a hold. Note that redaction is enabled by default and does not need to be requested explicitly.

1. When the customer and agent are connected, send ASAPP a request to start transcription for the call:
   **POST** `/mg-autotranscribe/v1/start-streaming`
   **Request**

   ```json  theme={null}
   {
     "namespace": "amazonconnect",
     "guid": "8c259fea-8764-4a92-adc4-73572e9cf016",
     "customerId": "TT9833237",
     "agentId": "RE223444211993",
     "autotranscribeParams": {
       "language": "en-US"
     },
     "amazonConnectParams": {
       "streamArn": arn:aws:kinesisvideo:us-east-1:145051540001:stream/streamtest-connect-asappconnect-contact-cccaa6b8-12e4-44a6-90d5-829c4fdf68e4/1696422764859TBD,
       "startSelectorType":"NOW"
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

2. The agent and customer begin their conversation and separate HTTPS POST `transcript` messages are sent for each participant from ASAPP's webhook publisher to a target endpoint configured to receive the messages.

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

3. Later in the conversation, the agent puts the customer on hold. This triggers a request to the `/stop-streaming` endpoint to pause transcription and prevents hold music and promotional messages from being transcribed.

   **POST** `/mg-autotranscribe/v1/stop-streaming`

   **Request**

   ```json  theme={null}
   {
    "namespace": "amazonconnect",
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

ASAPP's security protocols protect data at each point of transmission, from first user authentication to secure communications to our auditing and logging system (which includes hashing of data in transit) all the way to securing the environment when data is at rest in the data logging system. The teams at ASAPP are also under tight restraints in terms of access to data. These security protocols protect both ASAPP and its customers.
