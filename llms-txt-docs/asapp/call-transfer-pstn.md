# Source: https://docs.asapp.com/generativeagent/integrate/call-transfer-pstn.md

# Call Transfer over PSTN

> Learn how to use call transfers to handle GA calls with any platform

export const RunInPostman = ({src = "https://app.getpostman.com/run-collection/27609804-1acf7781-5fd8-4597-acd8-c25c6f1ad05d?action=collection%2Ffork&collection-url=entityId%3D27609804-1acf7781-5fd8-4597-acd8-c25c6f1ad05d%26entityType%3Dcollection%26workspaceId%3D09b1436a-4dfa-4357-92b9-1234692de2b1"}) => {
  return <div>
      <a href={src} target="_blank" rel="noopener noreferrer" className="inline-block hover:opacity-80 transition-opacity" style={{
    borderBottom: 'none'
  }}>
        <img src="https://run.pstmn.io/button.svg" alt="Run In Postman" noZoom style={{
    width: '128px',
    height: '32px',
    marginTop: '0px',
    marginBottom: '0px'
  }} className="w-32 h-8" />
      </a>
    </div>;
};

ASAPP's Call Transfer over PSTN enables businesses to integrate GenerativeAgent Voice without being constrained by their existing telephony infrastructure.

We have dedicated connector integrations for some platforms ([Genesys](/generativeagent/integrate/genesys-audiohook), [Amazon Connect](/generativeagent/integrate/amazon-connect)), but not every platform allows native integrations. Call transfers allow you to use PSTN (dialing a number) to connect your users to GenerativeAgent while keeping you in control of the call the entire time.

<RunInPostman src="https://www.postman.com/asapp-api/workspace/asapp/folder/27609804-739e750d-7bd2-4b43-a564-ffa341816a94" />

## How it works

At a high level, call transfer over PSTN works by assigning a temporary phone number for a given customer that you can dial in for GenerativeAgent:

1. **Request a number**: Your system requests a temporary phone number from ASAPP. Optionally you can provide context to the call.
2. **GenerativeAgent handles the conversation**: Dial in GenerativeAgent via the temporary phone number so it can talk directly to the customer.
3. **Return control**: When GenerativeAgent has completed the call, it will disconnect the call and your system will fetch the resulting context and handle the rest of the call flow.

<Accordion title="Detailed Flow">
  <Frame>
    <img src="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/integrate/call-transfer-overview.png?fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=1e7b0dc9eb96521e4ee7bf1da272d05c" alt="PSTN Call Transfer Flow" data-og-width="1231" width="1231" data-og-height="1224" height="1224" data-path="images/generativeagent/integrate/call-transfer-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/integrate/call-transfer-overview.png?w=280&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=5f561b9ee1078c79849a489cc6a7b0ea 280w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/integrate/call-transfer-overview.png?w=560&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=8ec7d87bfeb473b43a62eaccaed39d8a 560w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/integrate/call-transfer-overview.png?w=840&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=85abfc114aa85b24592dadf2469fea38 840w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/integrate/call-transfer-overview.png?w=1100&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=3bc8b2f308c2bba14a6607cc84760307 1100w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/integrate/call-transfer-overview.png?w=1650&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=1ddf946c124b868a935aece1c2f0f94f 1650w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/integrate/call-transfer-overview.png?w=2500&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=a778c6fda6bcc1a70443fbc58057dbca 2500w" />
  </Frame>

  1. **Incoming Call**: A customer calls your existing phone number
  2. **IVR Processing**: Your existing IVR system processes the call and determines when to transfer to GenerativeAgent
  3. **Request a number**: Your system requests a temporary phone number from ASAPP. Optionally you can provide context to the call.
  4. **Dial the number (Supervised transfer)**: Your system dials the temporary phone number via a Supervised transfer.

     With the supervised transfer, you can monitor the call and control the call flow while GenerativeAgent is talking to the user.
  5. **Detect GenerativeAgent disconnect**: When GenerativeAgent has completed the call, it will disconnect the call and your system will detect the disconnect.
  6. **Fetch the call context**: Your system will fetch the context, which includes the transfer type, from the call.
  7. **Handle the call**: Using the context and transfer type, your system handles the agent escalation, call disposition, or any other steps in your call flow.
</Accordion>

## Before you Begin

Before implementing PSTN Call Transfer, you need:

* [Get your API Key Id and Secret](/getting-started/developers#access-api-credentials)
  * Ensure your API key has been configured to access GenerativeAgent APIs. Reach out to your ASAPP team if you need access enabled.
* [Configure Tasks and Functions](/generativeagent/configuring)
* Contact your ASAPP account team to enable call transfer over PSTN
  * This includes determining how many concurrent calls you need to support, phone number countries to support, etc.

## Step 1: Request a temporary number

To transfer a call to GenerativeAgent, you need to create a `call-transfer`. A call transfer is the attempt to transfer a call to GenerativeAgent. This resource will include a temporary phone number from ASAPP that you can connect the customer to. This number will be assigned specifically for this customer interaction and will expire after a set time period, by default 1 minute.

To [create a call transfer](/apis/generativeagent/create-call-transfer), you need to specify:

|                Parameter | Description                                                                                                                                                                                                                                                                 |
| -----------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                     `id` | Your unique identifier for the call transfer. You will use this later to fetch the call transfer result.                                                                                                                                                                    |
| `externalConversationId` | Your unique identifier for the conversation. This allows you to reconnect the customer to the same conversation and is used in reporting.                                                                                                                                   |
|                   `type` | Specify a type of **PHONE\_NUMBER**.                                                                                                                                                                                                                                        |
|    `phoneNumber.country` | The country code for the phone number.                                                                                                                                                                                                                                      |
|           `inputContext` | Optionally specify the [`taskName`](/generativeagent/configuring/tasks-and-functions/enter-specific-task) and [`inputVariables`](/generativeagent/configuring/tasks-and-functions/input-variables) to trigger GenerativeAgent with specific task information and variables. |

```shell  theme={null}
curl --location 'https://api.sandbox.asapp.com/generativeagent/v1/call-transfers' \
--header 'asapp-api-id: <API KEY ID>' \
--header 'asapp-api-secret: <API TOKEN>' \
--header 'Content-Type: application/json' \
--data '{
    "id":"[Your Transfer Id]",
    "externalConversationId":"[Your Conversation Id]",
    "type": "PHONE_NUMBER",
    "phoneNumber":{
        "country": "US"
    },
    "inputContext": {
        "taskName":"call_routing",
        "inputVariables":{
            "accountNumber":"3434",
            "name": "John Doe"
        }
    }
}'
```

A successful request returns 200 with the call transfer data:

```json  theme={null}
{
    "id": "[Your Transfer Id]",
    "externalConversationId": "[Your Conversation Id]",
    "status": "ACTIVE",
    "type": "PHONE_NUMBER",
    "inputContext": {
        "taskName": "AsappDemo",
        "inputVariables": {
            "accountNumber": "3434",
            "name": "sample_name"
        }
    },
    "phoneNumber": {
        "transferNumber": "+19991234",
        "country": "US",
        "expireAt": "2025-06-19T13:39:40Z"
    }
}
```

**Save** the `phoneNumber.transferNumber`; you will need to transfer to it before the `phoneNumber.expireAt` time. This is 1 minute by default.

## Step 2: Make a supervised transfer

Perform a supervised transfer to the `phoneNumber.transferNumber` in the call transfer resource. Once you dial the number, GenerativeAgent is given the input context, if provided, and talks to the customer.

Once connected or expired, the number will be released and can be used by a subsequent call transfer.

The specific implementation on how to perform a supervised transfer depends on your call center system, but you must maintain call control throughout the transfer.

<Note>
  With the supervised transfer, your system is on the call the entire time. You can monitor the call and control the call flow while GenerativeAgent is talking to the user.
</Note>

## Step 3: Detect disconnect

With the supervised transfer, your system will be monitoring the call and two scenarios are possible during the conversation that you must handle accordingly:

1. **GenerativeAgent completes the conversation with an agent escalation or a system transfer**

   * GenerativeAgent has determined it needs to return the call to your system, either to an agent escalation or a system transfer.
   * GenerativeAgent disconnects from the call and the output context of the conversation can be retrieved; this is covered in the next step.

2. **Customer hangs up the phone call**
   * When the customer hangs up, there are no output variables since GenerativeAgent didn't close out the conversation.

<Note>
  The disconnect detection is crucial for maintaining proper call flow control and ensuring you can fetch the conversation context before handling the next steps.
</Note>

## Step 4: Fetch the call context

Once you detect the disconnect, you need to retrieve the call transfer result and resulting outputContext.

To retrieve the call transfer result, you need to [fetch the `call-transfers`](/apis/generativeagent/get-call-transfer) with the `id` of the original call transfer:

```shell  theme={null}
curl --location 'https://api.sandbox.asapp.com/generativeagent/v1/call-transfers/[Your Transfer Id]' \
--header 'asapp-api-id: <API KEY ID>' \
--header 'asapp-api-secret: <API TOKEN>'
```

A successful request returns 200 with call transfer data:

```json  theme={null}
{
    "id": "[Your Transfer Id]",
    "externalConversationId": "[Your Conversation Id]",
    "status": "COMPLETED",
    "createdAt": "2025-06-19T13:38:40Z",
    "callReceivedAt": "2025-06-19T13:38:45Z",
    "completedAt": "2025-06-19T13:39:12Z",
    "inputContext": {
        "taskName": "AsappDemo",
        "inputVariables": {
            "accountNumber": "3434",
            "name": "sample_name"
        }
    },
    "type": "PHONE_NUMBER",
    "outputContext": {
        "transferType": "SYSTEM",
        "currentTaskName": "currentTaskName",
        "referenceVariables": {
            "reference_variable_1": "4343"
        },
        "transferVariables": {
            "transfer_variable_": "4343"
        }
    },
    "phoneNumber": {
        "transferNumber": "+19991234",
        "country": "US",
        "expireAt": "2025-06-19T13:39:40Z"
    }
}
```

**Extract the key information:**

* **Status**: Indicates if the call was completed successfully.

  <Accordion title="Call transfer status">
    | Status        | Description                                                                                            |
    | ------------- | ------------------------------------------------------------------------------------------------------ |
    | **ACTIVE**    | The call transfer is active and the temporary phone number is waiting to be connected.                 |
    | **ONGOING**   | The call was connected and GenerativeAgent is talking to the customer.                                 |
    | **COMPLETED** | The call transfer has completed.                                                                       |
    | **EXPIRED**   | The call transfer has expired and the temporary phone number is no longer valid for that conversation. |
  </Accordion>

* **outputContext**: Contains the conversation results and any transfer variables
  * **transferType**: Indicates the type of transfer that occurred. This can be either `AGENT` or [`SYSTEM`](/generativeagent/configuring/tasks-and-functions/system-transfer).
  * **referenceVariables**: Context information about the customer and conversation
  * **transferVariables**: Data that should be passed to the next system or agent

With this information, handle the call according to your own business logic, such as routing the call to an agent or handling call disposition.

### Handling customer reconnections

There may be scenarios where you want to reconnect a customer directly to where they left off with GenerativeAgent. For example, if the customer hangs up the phone, or after transferring back to your system, you want to transfer them back again to GenerativeAgent.

To do this, ensure you use the same `externalConversationId` to reconnect the customer to the same conversation. GenerativeAgent will resume the conversation where it left off.

```shell  theme={null}
curl --location 'https://api.sandbox.asapp.com/generativeagent/v1/call-transfers' \
--header 'asapp-api-id: <API KEY ID>' \
--header 'asapp-api-secret: <API TOKEN>' \
--header 'Content-Type: application/json' \
--data '{
    "id":"[Your New Transfer Id for this transfer attempt]",
    "externalConversationId":"[Your Original Conversation Id from the first conversation leg]",
    "type": "PHONE_NUMBER",
    "phoneNumber":{
        "country": "US"
    }
}'
```

## Next Steps

Now that you have successfully implemented PSTN Call Transfer with GenerativeAgent, here are some important next steps to consider:

<CardGroup>
  <Card title="Configuration Overview" href="/generativeagent/configuring">
    Learn how to configure GenerativeAgent's behaviors, tasks, and communication style
  </Card>

  <Card title="Connect your APIs" href="/generativeagent/configuring/connect-apis">
    Configure your APIs to allow GenerativeAgent to access necessary data and perform actions
  </Card>

  <Card title="Review Knowledge Base" href="/generativeagent/configuring/connecting-your-knowledge-base">
    Connect and optimize your knowledge base to improve GenerativeAgent's responses
  </Card>

  <Card title="Go Live" href="/generativeagent/go-live">
    Follow the deployment checklist to launch GenerativeAgent in your production environment
  </Card>
</CardGroup>
