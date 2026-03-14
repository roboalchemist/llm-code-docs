# Source: https://plivo.com/docs/voice-agents/sip-trunking/integration-guides/elevenlabs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# ElevenLabs Integration

> Connect Plivo SIP trunking with ElevenLabs Conversational AI agents

Connect Plivo SIP trunking to ElevenLabs to enable your AI agents to make and receive phone calls through Plivo's global voice network.

***

## Prerequisites

| Requirement            | Description                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------- |
| **Plivo Account**      | [Sign up](https://www.plivo.com/request-trial/) with SIP trunking enabled                      |
| **Phone Number**       | [Purchase a voice-enabled number](https://cx.plivo.com/phone-numbers)                          |
|                        | - **India:** Requires KYC verification. See [Rent India Numbers](/numbers/rent-india-numbers). |
| **ElevenLabs Account** | Account with Conversational AI access - [Create account](https://elevenlabs.io/)               |

<Warning>
  **India regional requirement:** If handling calls to/from India, your ElevenLabs deployment must be in India. Contact ElevenLabs sales team to set this up. Calls will fail with "Domestic Anchored Terms not met" error otherwise.
</Warning>

<Tip>
  **Optimize for latency:** For best call quality, deploy your ElevenLabs server in a region closest to your call traffic. This minimizes audio delay and improves conversation flow.
</Tip>

***

## Part 1: Receive Incoming Calls

Route calls from your Plivo phone number to an ElevenLabs AI agent.

### Step 1: Create an Inbound Trunk in Plivo

1. Go to [SIP Trunking → Inbound Trunks](https://cx.plivo.com/sip-trunking)
2. Click **Create New Inbound Trunk**
3. Enter a name (e.g., `ElevenLabs-Inbound`)
4. Click **Add New URI** and configure:

| Field   | Value                                      |
| ------- | ------------------------------------------ |
| Name    | `ElevenLabs-Primary`                       |
| SIP URI | `sip.rtc.elevenlabs.io:5060;transport=tcp` |

For TLS: `sip.rtc.elevenlabs.io:5061;transport=tls`

For India: `sip.rtc.in.residency.elevenlabs.io:5060;transport=tcp`

5. Click **Create Trunk**

### Step 2: Connect Your Phone Number

1. Go to [Your Numbers](https://cx.plivo.com/phone-numbers)
2. Click on your phone number
3. Set **Application Type** to `Zentrunk`
4. Set **Trunk** to your inbound trunk
5. Click **Update Number**

### Step 3: Configure ElevenLabs

Import your Plivo number in ElevenLabs to accept incoming calls. See [ElevenLabs SIP Trunking documentation](https://elevenlabs.io/docs/agents-platform/phone-numbers/sip-trunking) for detailed steps.

***

## Part 2: Make Outgoing Calls

Enable ElevenLabs to make outbound calls through Plivo.

### Step 1: Create an Outbound Trunk in Plivo

1. Go to [SIP Trunking → Outbound Trunks](https://cx.plivo.com/sip-trunking)
2. Click **Create New Outbound Trunk**
3. Click **Add New Credentials List** and create credentials:
   * Username: `elevenlabs_trunk` (or your preferred username)
   * Password: Generate a strong password
4. Enter a trunk name (e.g., `ElevenLabs-Outbound`)
5. Enable **Secure Trunking** (recommended)
6. Click **Create Trunk**
7. Copy your **Termination SIP Domain** (e.g., `XXXXXXXXXXXX.zt.plivo.com`)

### Step 2: Configure ElevenLabs

Use the credentials and termination domain from Plivo to configure outbound calling in ElevenLabs. See [ElevenLabs Plivo integration guide](https://elevenlabs.io/docs/agents-platform/phone-numbers/telephony/plivo) for detailed steps.

***

## Troubleshooting

| Issue                 | Solution                                                                                |
| --------------------- | --------------------------------------------------------------------------------------- |
| Call doesn't connect  | Verify SIP URI includes `transport=tcp`. Check phone number is mapped to correct trunk. |
| Authentication errors | Verify credentials match exactly in both Plivo and ElevenLabs.                          |
| India calls failing   | Ensure ElevenLabs deployment is in India region. Use India-specific SIP URI.            |

**Debug logs:**

* Inbound issues: Check [Plivo logs](https://cx.plivo.com/sip-trunking) first
* Outbound issues: Check ElevenLabs logs first

For error codes, see [Plivo hangup codes](/voice-agents/sip-trunking/troubleshooting/hangup-codes).

***

## Related

* [ElevenLabs SIP Trunking docs](https://elevenlabs.io/docs/agents-platform/phone-numbers/sip-trunking) - Detailed ElevenLabs configuration
* [ElevenLabs Plivo guide](https://elevenlabs.io/docs/agents-platform/phone-numbers/telephony/plivo) - ElevenLabs' official Plivo integration guide
* [SIP Trunking Overview](/sip-trunking) - Plivo SIP trunking documentation
