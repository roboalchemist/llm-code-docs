# Source: https://docs.asapp.com/generativeagent/integrate/sip-transfers-headers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SIP Headers Transfer

> Use SIP headers to pass context directly in transfers without API calls

SIP Headers Transfer enables you to integrate GenerativeAgent with your existing SIP telephony infrastructure by passing context directly in SIP headers. This approach eliminates the need for API calls during the transfer process, making it simpler to implement but with limited context complexity due to SIP header size constraints.

## How it works

At a high level, SIP Headers Transfer works by:

1. **Transfer to ASAPP**: You transfer the call to ASAPP using SIP with context passed in headers
2. **GenerativeAgent handles the conversation**: Transfer the call to GenerativeAgent via SIP so it can talk directly to the customer
3. **Return control**: When GenerativeAgent has completed the call, it will transfer the call back to your system over SIP with return and transfer variables

<Accordion title="Detailed Flow">
  <Frame>
    <img src="https://mintcdn.com/asapp/Fr9Eg6nQ_TuUVRmN/images/generativeagent/integrate/sip-transfer-headers-overview.png?fit=max&auto=format&n=Fr9Eg6nQ_TuUVRmN&q=85&s=9bd7fe7a7617d55ab99c6c2a62ed2fae" alt="SIP Headers Transfer Flow" data-og-width="1672" width="1672" data-og-height="1145" height="1145" data-path="images/generativeagent/integrate/sip-transfer-headers-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/Fr9Eg6nQ_TuUVRmN/images/generativeagent/integrate/sip-transfer-headers-overview.png?w=280&fit=max&auto=format&n=Fr9Eg6nQ_TuUVRmN&q=85&s=337f188b3f32d714db4c7a85d75f3378 280w, https://mintcdn.com/asapp/Fr9Eg6nQ_TuUVRmN/images/generativeagent/integrate/sip-transfer-headers-overview.png?w=560&fit=max&auto=format&n=Fr9Eg6nQ_TuUVRmN&q=85&s=b3d36de78144cd7b352e85236ba3455f 560w, https://mintcdn.com/asapp/Fr9Eg6nQ_TuUVRmN/images/generativeagent/integrate/sip-transfer-headers-overview.png?w=840&fit=max&auto=format&n=Fr9Eg6nQ_TuUVRmN&q=85&s=e990875a70511fdd2e8bf4a4c56a190a 840w, https://mintcdn.com/asapp/Fr9Eg6nQ_TuUVRmN/images/generativeagent/integrate/sip-transfer-headers-overview.png?w=1100&fit=max&auto=format&n=Fr9Eg6nQ_TuUVRmN&q=85&s=ad027203d8cccce78a87be599d7e131a 1100w, https://mintcdn.com/asapp/Fr9Eg6nQ_TuUVRmN/images/generativeagent/integrate/sip-transfer-headers-overview.png?w=1650&fit=max&auto=format&n=Fr9Eg6nQ_TuUVRmN&q=85&s=e852f0d439abc503787d33937f4e8ded 1650w, https://mintcdn.com/asapp/Fr9Eg6nQ_TuUVRmN/images/generativeagent/integrate/sip-transfer-headers-overview.png?w=2500&fit=max&auto=format&n=Fr9Eg6nQ_TuUVRmN&q=85&s=34ef631ba1af96431d87ec3272971ca2 2500w" />
  </Frame>

  1. **Incoming Call**: A customer calls your existing phone number
  2. **IVR Processing**: Your existing IVR system processes the call and determines when to transfer to GenerativeAgent
  3. **Transfer the call**: Your system transfers the call to ASAPP's static SIP domain with context passed in SIP headers
  4. **Receive the returned SIP transfer**: When GenerativeAgent has completed the call, it will transfer the call back to your return URI
  5. **Process the return data**: Your system extracts the context from the Refer-To URI parameters and handles the call flow
</Accordion>

## Prerequisites

Before implementing SIP Headers Transfer, you need:

* [Configure Tasks and Functions](/generativeagent/configuring)
* Contact your ASAPP account team to enable SIP transfers
  * This includes determining how many concurrent calls you need to support, SIP infrastructure requirements, etc.
* **Configure SIP server authentication**: ASAPP requires authentication for all incoming SIP requests to ensure security. You must provide one or both of the following authentication methods:
  * **IP whitelist**: The IP address(es) of your SIP server(s) that ASAPP will allow to make SIP requests
  * **Username and password**: SIP authentication credentials that ASAPP will use to validate your SIP requests
  <Warning>
    **Security requirement**: ASAPP cannot accept unauthenticated SIP requests. You must provide at least one authentication method (IP whitelist and/or username/password) during setup.
  </Warning>
* ASAPP will provide a static SIP domain for you to transfer to
* **Provide your SIP return URI**: You must provide ASAPP with your SIP URI for return transfers

<Note>
  Unlike API-based transfers, SIP Headers Transfer does not require API credentials as context is passed directly in the SIP headers.
</Note>

## SIP Return URI Configuration

You need to provide ASAPP with your SIP return URI configuration to enable return transfers. This includes:

### Return Transfer Methods

Choose the appropriate return transfer method based on your call flow needs:

| Transfer Method | Behavior                                                         | Use Case                                                          |
| --------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------- |
| **REFER**       | Standard blind transfer - sends REFER message to your return URI | Transfer back to you after ASAPP completes                        |
| **INVITE**      | Keeps ASAPP in call flow for continued transcription             | Provide end-to-end conversation understanding for GenerativeAgent |

<Warning>
  **Cost Implications**: INVITE transfer method has higher cost implications that need to be aligned with your sales team before implementation. Contact your ASAPP representative to discuss pricing for this transfer method.
</Warning>

### Required Configuration

When setting up SIP Headers Transfer, provide ASAPP with:

* **SIP Return URI**: The complete SIP URI where ASAPP should transfer calls back to
* **Transfer Method**: Whether to use REFER or INVITE for return transfers
* **Authentication (INVITE only)**: If using INVITE method, specify whether to use username/password authentication

## Step 2: Transfer the call to ASAPP

Transfer the call to ASAPP using SIP. ASAPP will provide a static SIP domain for you to transfer to.

<Warning>
  **Authentication required**: ASAPP will authenticate your SIP request using the IP whitelist and/or username/password credentials you provided during setup. Your SIP request must pass authentication or it will be rejected.
</Warning>

You have several headers you can use to pass context to ASAPP:

| Header                   | Description                                                                                                                                                              |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `X-GA-taskName`          | The [entry task](/generativeagent/configuring/tasks-and-functions/enter-specific-task) for GenerativeAgent to handle the call                                            |
| `X-GA-extConversationId` | The external conversation ID for the call                                                                                                                                |
| `X-GA-customerId`        | The customer ID for the call                                                                                                                                             |
| `X-GA-iv-*`              | Add any number of [input variables](/generativeagent/configuring/tasks-and-functions/input-variables) with this prefix. These can be referenced in the task instructions |

<Note>
  For input variables, use the prefix `X-GA-iv-` followed by your variable name. For example, an input variable named `userName` would be passed as `X-GA-iv-userName`.
</Note>

```bash Example SIP Transfer theme={null}
INVITE sip:asapp-endpoint.com SIP/2.0
Via: SIP/2.0/UDP your-sbc.example.com:5060
From: <sip:customer@your-sbc.example.com>
To: <sip:asapp-endpoint.com>
Call-ID: call-12345@your-sbc.example.com
CSeq: 1 INVITE
X-GA-taskName: call_routing
X-GA-extConversationId: conv-12345
X-GA-customerId: cust-67890
X-GA-iv-accountNumber: 3434
X-GA-iv-name: John Doe
X-GA-iv-priority: high
```

After connecting, GenerativeAgent will handle the conversation using the provided context.

## Step 3: Handle the return transfer

To transfer back a call to your system, GenerativeAgent will perform a SIP transfer back to you using the method you configured (REFER or INVITE). The transfer method determines how the call is returned:

**REFER Transfer**: GenerativeAgent sends a SIP REFER message to your return URI. The transfer will send back the list of referenceVariables and transferVariables as query params in the Refer target (Refer-To).

**INVITE Transfer**: GenerativeAgent sends a SIP INVITE to your return URI. ASAPP will continue to transcribe the call to provide end-to-end conversation understanding for GenerativeAgent.

For **REFER transfers**, the following parameters are sent as query params in the Refer-To header:

| Parameter       | Description                                                                               |
| --------------- | ----------------------------------------------------------------------------------------- |
| `X-GA-extConId` | The conversation ID you provided                                                          |
| `X-GA-transfer` | Transfer type: **AGENT** (unable to help) or **SYSTEM** (called system transfer function) |
| `X-GA-rv-*`     | Each reference variable with this prefix                                                  |
| `X-GA-tv-*`     | Each transfer variable with this prefix                                                   |

These are defined as part of the [System Transfer](/generativeagent/configuring/tasks-and-functions/system-transfer) function within the GenerativeAgent configuration.

```bash Example REFER Return Transfer theme={null}
Refer-To: sip:your-sbc.example.com?X-GA-extConId=conv-12345&X-GA-transfer=SYSTEM&X-GA-tv-next_action=schedule_callback&X-GA-tv-priority=high&X-GA-rv-account_balance=1250.00&X-GA-rv-last_payment_date=2025-01-10
```

### Header Size Limit

There is a **1024 character limit** for all context data. Headers are added in this order:

1. **Transfer variables** (`X-GA-tv-*`) - added first
2. **Reference variables** (`X-GA-rv-*`) - added second

The system stops adding variables when it reaches the limit. Any remaining variables are dropped, so use shorter variable names and values to maximize the data you can transfer.

The [System Transfer function](/generativeagent/configuring/tasks-and-functions/system-transfer) determines which variables are included, so make sure the total size of the variables you pass does not exceed this limit.

## Step 4: Process the return data

The processing depends on the transfer method you configured:

**For REFER transfers**: When you receive the REFER message, extract the context from the Refer-To URI parameters:

1. **Parse the Refer-To URI** to extract all parameters

2. **Identify the transfer type** from `X-GA-transfer`:

   * `AGENT`: GenerativeAgent was unable to help and needs human agent escalation
   * `SYSTEM`: GenerativeAgent called a system transfer function to hand control back to your system

3. **Extract variables**:
   * Reference variables (`X-GA-rv-*`): Context information about the customer and conversation
   * Transfer variables (`X-GA-tv-*`): Data that should be passed to the next system or agent

Use this information to handle the call according to your business logic, such as routing to an agent or handling call disposition.

## Next Steps

Now that you understand how SIP Headers Transfer works, here are some important next steps to consider:

<CardGroup>
  <Card title="Configuration Overview" href="/generativeagent/configuring">
    Learn how to configure GenerativeAgent's behaviors, tasks, and communication style
  </Card>

  <Card title="System Transfer Functions" href="/generativeagent/configuring/tasks-and-functions/system-transfer">
    Configure system transfer functions to control what data is returned in transfer variables
  </Card>

  <Card title="Input Variables" href="/generativeagent/configuring/tasks-and-functions/input-variables">
    Learn how to structure input variables for optimal context passing
  </Card>

  <Card title="Go Live" href="/generativeagent/go-live">
    Follow the deployment checklist to launch GenerativeAgent in your production environment
  </Card>
</CardGroup>
