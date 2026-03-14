# Source: https://plivo.com/docs/voice/use-cases/participant-level-recording.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Participant-Level Recording

> Record individual audio tracks for each participant in a multiparty call

## Overview

The participant-level recording feature enables you to generate individual audio recordings for each participant in an MPC. This is useful for scenarios where you need clear, isolated audio tracks for each participant, such as in interviews, conferences, or any multi-party communication.

## Example Use Case

**Scenario: Conduct Sentiment Analysis on Customer-Support Agent Interaction**

An organization may seek to conduct sentiment analysis on interactions between customers and support agents. To achieve this, the organization requires separate recording files of both the customer and the agent.

Here's how the process unfolds:

<ol>
  <li>The customer initiates a call to the support toll-free number.</li>
  <li>Upon initiation, an application is triggered, which adds the customer to the MPC bridge and initiates participant-level recording.</li>
  <li>Simultaneously, the support agent joins the MPC bridge, also with participant-level recording activated.</li>
  <li>During the call, both the customer and the support agent's interactions are recorded separately.</li>
  <li>Upon call completion, two distinct recording files are generated: one containing the audio of the customer and the other of the support agent.</li>
  <li>These recording files are then utilized for sentiment analysis, providing valuable insights into customer-agent interactions.</li>
</ol>

## Step-by-Step Guide

Participant-level recording can be achieved using both [API](/voice/api/multiparty-call/participants#add-a-participant) and [XML](/voice/xml/multipartycall/)

### Starting single-track or participant-level recording when adding a participant to the MPC

Use the following request to add a participant to the MPC and initiate a single-track recording.  Please refer to the [API documentation](/voice/api/multiparty-call/participants#add-a-participant) for more details.

```sh  theme={null}
curl -i --user \
 AUTH_ID:AUTH_TOKEN \
    -H \
 "Content-Type: application/json" \
    -d '{"to": "+12025551111","from": "+12025550000", "role": "Agent", "start_mpc_on_enter": true, "recordParticipantTrack": true}' \
    https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Participant/
```

### Start single-track or participant-level recording for any member in the MPC

Use the following request to initiate participant-level recording for an existing member on the MPC bridge. Please refer to the [API documentation](/voice/api/multiparty-call/participants/participant-level-recording#start-recording) for more details.

```sh  theme={null}
curl -i --user \
 AUTH_ID:AUTH_TOKEN \
    -H \
 "Content-Type: application/json" \
    -d '{"file_format": "mp3","record_track_type":"participant"}' \
    https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/{mpc_name/UUID}/Participant/{Member_Id}/Record/
```

### Initiate MPC with participant level recording using XML

Here is a sample XML to start participant-level recording. Please refer to the [XML documentation](/voice/xml/multipartycall/) for more details.

```
<Response>
	<MultiPartyCall role="customer" recordParticipantTrack="true">mpc_customer</MultiPartyCall>
</Response>
```
