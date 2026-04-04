# Source: https://docs.asapp.com/generativeagent/integrate/sip-transfers-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# API-based SIP Transfers

> Use REST API calls to pass rich context data for SIP transfers with unlimited complexity

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

API-based SIP transfers use REST API calls to create call transfers with rich context input and output. This approach provides unlimited complexity for context data but requires API integration in your system.

<RunInPostman src="https://www.postman.com/asapp-api/workspace/asapp/folder/27609804-739e750d-7bd2-4b43-a564-ffa341816a94" />

## How it works

At a high level, API-based SIP transfers work by:

1. **Request a SIP URI**: Your system requests a destination SIP URI from ASAPP via API call. You can provide complex context to the call.
2. **GenerativeAgent handles the conversation**: Transfer the call to GenerativeAgent via the SIP URI so it can talk directly to the customer.
3. **Return control**: When GenerativeAgent has completed the call, it will transfer the call back to your specified return URI and your system will fetch the resulting context and handle the rest of the call flow.

<Accordion title="Detailed Flow">
  <Frame>
    <img src="https://mintcdn.com/asapp/Fr9Eg6nQ_TuUVRmN/images/generativeagent/integrate/sip-transfer-overview.png?fit=max&auto=format&n=Fr9Eg6nQ_TuUVRmN&q=85&s=5dd4d45297ba00742ac8cc48b1d74455" alt="SIP Transfer Flow" data-og-width="1372" width="1372" data-og-height="1229" height="1229" data-path="images/generativeagent/integrate/sip-transfer-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/Fr9Eg6nQ_TuUVRmN/images/generativeagent/integrate/sip-transfer-overview.png?w=280&fit=max&auto=format&n=Fr9Eg6nQ_TuUVRmN&q=85&s=5a7b7ed1ff679495ccb1266e6781ee6f 280w, https://mintcdn.com/asapp/Fr9Eg6nQ_TuUVRmN/images/generativeagent/integrate/sip-transfer-overview.png?w=560&fit=max&auto=format&n=Fr9Eg6nQ_TuUVRmN&q=85&s=b17324a414357adeffc1e1c2c4c01c4c 560w, https://mintcdn.com/asapp/Fr9Eg6nQ_TuUVRmN/images/generativeagent/integrate/sip-transfer-overview.png?w=840&fit=max&auto=format&n=Fr9Eg6nQ_TuUVRmN&q=85&s=e7c159a084ea6bc228339e3371cabd5c 840w, https://mintcdn.com/asapp/Fr9Eg6nQ_TuUVRmN/images/generativeagent/integrate/sip-transfer-overview.png?w=1100&fit=max&auto=format&n=Fr9Eg6nQ_TuUVRmN&q=85&s=7a1a40c871523e3efad6bc4b24459dc7 1100w, https://mintcdn.com/asapp/Fr9Eg6nQ_TuUVRmN/images/generativeagent/integrate/sip-transfer-overview.png?w=1650&fit=max&auto=format&n=Fr9Eg6nQ_TuUVRmN&q=85&s=45131970249f510d5a1540f34d0b7a10 1650w, https://mintcdn.com/asapp/Fr9Eg6nQ_TuUVRmN/images/generativeagent/integrate/sip-transfer-overview.png?w=2500&fit=max&auto=format&n=Fr9Eg6nQ_TuUVRmN&q=85&s=2018c08568a4fc07bd658f7341e22103 2500w" />
  </Frame>

  1. **Incoming Call**: A customer calls your existing phone number
  2. **IVR Processing**: Your existing IVR system processes the call and determines when to transfer to GenerativeAgent
  3. **Request a SIP URI**: Your system requests a destination SIP URI from ASAPP via API call. You can provide complex context to the call.
  4. **Transfer the call**: Your system transfers the call to the destination SIP URI via SIP protocol.
  5. **Detect call completion**: When GenerativeAgent has completed the call, it will transfer the call back to your return URI.
  6. **Fetch the call context**: Your system will fetch the context, which includes the transfer type, from the call via API call.
  7. **Handle the call**: Using the context and transfer type, your system handles the agent escalation, call disposition, or any other steps in your call flow.
</Accordion>

## Before you Begin

Before implementing API-based SIP Transfers, you need:

* [Get your API Key Id and Secret](/getting-started/developers#access-api-credentials)
  * Ensure your API key has been configured to access GenerativeAgent APIs. Reach out to your ASAPP team if you need access enabled.
* [Configure Tasks and Functions](/generativeagent/configuring)
* Contact your ASAPP account team to enable SIP transfers
  * This includes determining how many concurrent calls you need to support, SIP infrastructure requirements, etc.
* **Configure SIP server authentication**: ASAPP requires authentication for all incoming SIP requests to ensure security. You must provide one or both of the following authentication methods:
  * **IP whitelist**: The IP address(es) of your SIP server(s) that ASAPP will allow to make SIP requests
  * **Username and password**: SIP authentication credentials that ASAPP will use to validate your SIP requests
  <Warning>
    **Security requirement**: ASAPP cannot accept unauthenticated SIP requests. You must provide at least one authentication method (IP whitelist and/or username/password) during setup.
  </Warning>
* **Get your SIP URI for transfers**: Obtain the static SIP URI from ASAPP that you'll use to route calls to GenerativeAgent
* **Configure transfer settings**: Set up your default [transfer type](#transfer-types) and authentication credentials (for INVITE transfers) with your ASAPP account team

### Transfer Types

Your transfer type is configured as part of your static setup with ASAPP. Choose the appropriate transfer type based on your call flow needs:

| Transfer Type | Behavior                                                         | Use Case                                                                        |
| ------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **BYE**       | GenerativeAgent disconnects when done                            | Your system handles the disconnect (lower cost)                                 |
| **REFER**     | Standard blind transfer - sends REFER message to your return URI | Transfer to another system after ASAPP completes (higher cost)                  |
| **INVITE**    | Keeps ASAPP in call flow for continued transcription             | Provide end-to-end conversation understanding for GenerativeAgent (higher cost) |

<Warning>
  **Cost Implications**: REFER and INVITE transfer types have higher cost implications that need to be aligned with your sales team before implementation. Contact your ASAPP representative to discuss pricing for these transfer types.
</Warning>

<Note>
  For INVITE transfers, you can provide authentication credentials (username/password) as part of your static configuration with ASAPP.
</Note>

## Step 1: Create a call transfer

To transfer a call to GenerativeAgent, you need to create a `call-transfer`. A call transfer is the attempt to transfer a call to GenerativeAgent. This resource will include context and configuration for the transfer, but you'll route the call to the static SIP URI provided by ASAPP.

To [create a call transfer](/apis/generativeagent/create-call-transfer), you need to specify:

|                Parameter | Description                                                                                                                                                                                                                                                                                                     |
| -----------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                     `id` | Your unique identifier for the call transfer. You will use this later to fetch the call transfer result.                                                                                                                                                                                                        |
| `externalConversationId` | Your unique identifier for the conversation. This allows you to reconnect the customer to the same conversation and is used in reporting.                                                                                                                                                                       |
|                   `type` | Specify a type of **SIP**.                                                                                                                                                                                                                                                                                      |
|          `sip.returnURI` | Only used for REFER and INVITE transfer types.<br /><br />The SIP URI to transfer the call back to when the conversation ends. You can include any parameters in the URI (e.g., User-to-User headers, custom parameters) and ASAPP will send the URI back exactly as provided. Maximum length: 1024 characters. |
|           `inputContext` | Optionally specify the [`taskName`](/generativeagent/configuring/tasks-and-functions/enter-specific-task) and [`inputVariables`](/generativeagent/configuring/tasks-and-functions/input-variables) to trigger GenerativeAgent with specific task information and variables.                                     |

<CodeGroup>
  ```shell REFER/INVITE Example theme={null}
  curl --location 'https://api.sandbox.asapp.com/generativeagent/v1/call-transfers' \
  --header 'asapp-api-id: <API KEY ID>' \
  --header 'asapp-api-secret: <API TOKEN>' \
  --header 'Content-Type: application/json' \
  --data '{
      "id":"[Your Transfer Id]",
      "externalConversationId":"[Your Conversation Id]",
      "type": "SIP",
      "sip": {
          "returnURI": "sip:user@customer-sbc.example.com;User-to-User=UUI-12345"
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

  ```shell BYE Example theme={null}
  curl --location 'https://api.sandbox.asapp.com/generativeagent/v1/call-transfers' \
  --header 'asapp-api-id: <API KEY ID>' \
  --header 'asapp-api-secret: <API TOKEN>' \
  --header 'Content-Type: application/json' \
  --data '{
      "id":"[Your Transfer Id]",
      "externalConversationId":"[Your Conversation Id]",
      "type": "SIP",
      "inputContext": {
          "taskName":"call_routing",
          "inputVariables":{
              "accountNumber":"3434",
              "name": "John Doe"
          }
      }
  }'
  ```
</CodeGroup>

A successful request returns 200 with the call transfer data:

```json  theme={null}
{
    "id": "[Your Transfer Id]",
    "externalConversationId": "[Your Conversation Id]",
    "status": "ACTIVE",
    "type": "SIP",
    "inputContext": {
        "taskName": "call_routing",
        "inputVariables": {
            "accountNumber": "3434",
            "name": "John Doe"
        }
    },
    "sip": {
        "returnURI": "sip:user@customer-sbc.example.com;User-to-User=UUI-12345"
    },
    "createdAt": "2025-01-15T13:06:00Z"
}
```

**Save** the `id` from the response; you will need it to pass as the `X-ASAPP-CallTransferId` header when transferring the call and to query the call transfer result in Step 3.

## Step 2: Transfer the call and handle the response

Once you've created the call transfer, you need to route the call to GenerativeAgent and handle the return transfer when the conversation ends.

<Steps>
  <Step title="Send the call to ASAPP">
    Transfer the call to the static SIP URI provided by ASAPP during setup. Include the call transfer `id` as the `X-ASAPP-CallTransferId` header in your SIP transfer.

    <Warning>
      **Authentication required**: ASAPP will authenticate your SIP request using the IP whitelist and/or username/password credentials you provided during setup. Your SIP request must pass authentication or it will be rejected.
    </Warning>

    Once you transfer the call, GenerativeAgent is given the input context, if provided, and talks to the customer.

    The specific implementation on how to perform a SIP transfer depends on your call center system.

    <Note>
      With SIP transfers, the customer is calling into your phone number so your SBC/PBX is handling the inbound call. Your system maintains visibility and ultimate ownership of the call the entire time.
    </Note>
  </Step>

  <Step title="Handle the return transfer and detect call completion">
    Two scenarios are possible during the conversation that you must handle accordingly:

    1. **GenerativeAgent completes the conversation with an agent escalation or a system transfer**
       * GenerativeAgent has determined it needs to return the call to your system, either to an agent escalation or a system transfer.
       * GenerativeAgent handles the call return based on your transfer type:
         * **BYE Transfer**: GenerativeAgent disconnects the call. Your system needs to detect the disconnect and proceed to fetch the call context.
         * **REFER Transfer**: GenerativeAgent sends a SIP REFER message to your return URI. Your system should accept and handle the REFER, and then fetch the call context.
         * **INVITE Transfer**: GenerativeAgent sends a SIP INVITE to your return URI. Your system should accept the INVITE and then fetch the call context. ASAPP will continue to transcribe the call until the call is ended.
       * The output context of the conversation can be retrieved.

    2. **Customer hangs up the phone call**
       * When the customer hangs up, there are no output variables since GenerativeAgent didn't close out the conversation.
       * No transfer is performed and no output context will be available for fetching.

    <Note>
      The call completion detection is crucial for maintaining proper call flow control and ensuring you can fetch the conversation context before handling the next steps.
    </Note>
  </Step>
</Steps>

## Step 3: Fetch the call context

After handling the return transfer in Step 2, retrieve the call transfer result and outputContext to understand what happened during the conversation.

<Note>
  **Only fetch call context when GenerativeAgent handed back the call**: You can only retrieve meaningful output context when GenerativeAgent completed the conversation and transferred the call back to your system. If the customer hung up during the conversation, there will be no output context available for fetching.
</Note>

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
    "createdAt": "2025-01-15T13:06:00Z",
    "callReceivedAt": "2025-01-15T13:06:30Z",
    "completedAt": "2025-01-15T13:09:45Z",
    "inputContext": {
        "taskName": "call_routing",
        "inputVariables": {
            "accountNumber": "3434",
            "name": "John Doe"
        }
    },
    "type": "SIP",
    "outputContext": {
        "transferType": "SYSTEM",
        "currentTaskName": "AccountInquiry",
        "referenceVariables": {
            "account_balance": "1250.00",
            "last_payment_date": "2025-01-10"
        },
        "transferVariables": {
            "next_action": "schedule_callback",
            "priority": "high"
        }
    },
    "sip": {
        "returnURI": "sip:user@customer-sbc.example.com;User-to-User=UUI-12345"
    }
}
```

**Extract the key information:**

* **Status**: Indicates if the call was completed successfully.

  <Accordion title="Call transfer status">
    | Status        | Description                                                                                         |
    | ------------- | --------------------------------------------------------------------------------------------------- |
    | **ACTIVE**    | The call transfer is active and the destination SIP URI is waiting to be connected.                 |
    | **ONGOING**   | The call was connected and GenerativeAgent is talking to the customer.                              |
    | **COMPLETED** | The call transfer has completed.                                                                    |
    | **EXPIRED**   | The call transfer has expired and the destination SIP URI is no longer valid for that conversation. |
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
    "type": "SIP",
    "sip": {
        "returnURI": "sip:user@customer-sbc.example.com;User-to-User=UUI-12345",
        "returnTransferType": "REFER"
    }
}'
```

## Dynamic Transfer Configuration

By default, your transfer type is configured as part of your static setup with ASAPP. However, you can optionally override the transfer type for specific calls by including the `sip.returnTransferType` parameter in your call transfer request.

### Override Transfer Type

To use a different transfer type for a specific call, include the `sip.returnTransferType` parameter:

|                                 Parameter | Description                                                                              |
| ----------------------------------------: | :--------------------------------------------------------------------------------------- |
|                  `sip.returnTransferType` | Override the default transfer type for this specific call (`BYE`, `REFER`, or `INVITE`). |
| `sip.returnInviteAuthentication.username` | Username for authentication (optional for INVITE transfers).                             |
| `sip.returnInviteAuthentication.password` | Password for authentication (optional for INVITE transfers).                             |

<CodeGroup>
  ```shell INVITE with authentication example theme={null}
  curl --location 'https://api.sandbox.asapp.com/generativeagent/v1/call-transfers' \
  --header 'asapp-api-id: <API KEY ID>' \
  --header 'asapp-api-secret: <API TOKEN>' \
  --header 'Content-Type: application/json' \
  --data '{
      "id":"[Your Transfer Id]",
      "externalConversationId":"[Your Conversation Id]",
      "type": "SIP",
      "sip": {
          "returnURI": "sip:user@customer-sbc.example.com;User-to-User=UUI-12345",
          "returnTransferType": "INVITE",
          "returnInviteAuthentication": {
              "username": "your_username",
              "password": "your_password"
          }
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

  ```shell REFER example theme={null}
  curl --location 'https://api.sandbox.asapp.com/generativeagent/v1/call-transfers' \
  --header 'asapp-api-id: <API KEY ID>' \
  --header 'asapp-api-secret: <API TOKEN>' \
  --header 'Content-Type: application/json' \
  --data '{
      "id":"[Your Transfer Id]",
      "externalConversationId":"[Your Conversation Id]",
      "type": "SIP",
      "sip": {
          "returnURI": "sip:user@customer-sbc.example.com;User-to-User=UUI-12345",
          "returnTransferType": "REFER"
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

  ```shell BYE example theme={null}
  curl --location 'https://api.sandbox.asapp.com/generativeagent/v1/call-transfers' \
  --header 'asapp-api-id: <API KEY ID>' \
  --header 'asapp-api-secret: <API TOKEN>' \
  --header 'Content-Type: application/json' \
  --data '{
      "id":"[Your Transfer Id]",
      "externalConversationId":"[Your Conversation Id]",
      "type": "SIP",
      "sip": {
          "returnTransferType": "BYE"
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
</CodeGroup>

<Note>
  When using dynamic transfer configuration:

  * The `sip.returnURI` is required for REFER and INVITE transfer types, but not for BYE transfers
  * For INVITE transfers, you may provide `sip.returnInviteAuthentication.username` and `sip.returnInviteAuthentication.password` for authentication
</Note>

## Next Steps

Now that you have successfully implemented API-based SIP Transfers with GenerativeAgent, here are some important next steps to consider:

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
