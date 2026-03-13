# Source: https://plivo.com/docs/voice-agents/sip-trunking/integration-guides/livekit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LiveKit Integration

> Connect Plivo SIP trunking with LiveKit for real-time voice AI applications

Connect Plivo SIP trunking to LiveKit to enable your voice AI applications to make and receive phone calls through Plivo's global voice network.

***

## Prerequisites

| Requirement               | Description                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------------- |
| **Plivo Account**         | [Sign up](https://www.plivo.com/request-trial/) with SIP trunking enabled                      |
| **Phone Number**          | [Purchase a voice-enabled number](https://cx.plivo.com/phone-numbers)                          |
|                           | - **India:** Requires KYC verification. See [Rent India Numbers](/numbers/rent-india-numbers). |
| **LiveKit Cloud Account** | [Create account](https://cloud.livekit.io)                                                     |

<Warning>
  **India regional requirement:** If handling calls to/from India, you must select India as your LiveKit region. This is a regulatory requirement - calls will fail otherwise.
</Warning>

<Tip>
  **Optimize for latency:** For best call quality, select a LiveKit region closest to your call traffic. This minimizes audio delay and improves conversation flow.
</Tip>

***

## Part 1: Receive Incoming Calls

Route calls from your Plivo phone number to LiveKit.

### Step 1: Create an Inbound Trunk in Plivo

1. Go to [SIP Trunking → Inbound Trunks](https://cx.plivo.com/sip-trunking)
2. Click **Create New Inbound Trunk**
3. Enter a name (e.g., `LiveKit-Inbound`)
4. Click **Add New URI** and configure:

| Field   | Value                                |
| ------- | ------------------------------------ |
| Name    | `LiveKit-Primary`                    |
| SIP URI | `your-project-SIP-URI;transport=tcp` |

Replace `your-project-SIP-URI` with your LiveKit SIP URI from **LiveKit Dashboard → Settings → Project**.

For TLS, use `;transport=tls` instead.

5. Click **Create Trunk**

### Step 2: Connect Your Phone Number

1. Go to [Your Numbers](https://cx.plivo.com/phone-numbers)
2. Click on your phone number
3. Set **Application Type** to `Zentrunk`
4. Set **Trunk** to your inbound trunk
5. Click **Update Number**

### Step 3: Configure LiveKit

Set up an inbound trunk and dispatch rules in LiveKit. See [LiveKit SIP documentation](https://docs.livekit.io/sip/) for detailed steps.

***

## Part 2: Make Outgoing Calls

Enable LiveKit to make outbound calls through Plivo.

### Step 1: Create an Outbound Trunk in Plivo

1. Go to [SIP Trunking → Outbound Trunks](https://cx.plivo.com/sip-trunking)
2. Click **Create New Outbound Trunk**
3. Click **Add New Credentials List** and create credentials:
   * Username: `livekit_trunk` (or your preferred username)
   * Password: Generate a strong password
4. Enter a trunk name (e.g., `LiveKit-Outbound`)
5. Enable **Secure Trunking** (recommended)
6. Click **Create Trunk**
7. Copy your **Termination SIP Domain** (e.g., `XXXXXXXXXXXX.zt.plivo.com`)

### Step 2: Configure LiveKit

Use the credentials and termination domain from Plivo to configure outbound calling in LiveKit. See [LiveKit outbound calls documentation](https://docs.livekit.io/sip/outbound-calls/) for detailed steps.

***

## Troubleshooting

| Issue                 | Solution                                                                                 |
| --------------------- | ---------------------------------------------------------------------------------------- |
| Call doesn't connect  | Verify SIP URI includes `;transport=tcp`. Check phone number is mapped to correct trunk. |
| Authentication errors | Verify credentials match exactly in both Plivo and LiveKit.                              |
| India calls failing   | Ensure LiveKit region is set to India.                                                   |

**Debug logs:**

* Inbound issues: Check [Plivo logs](https://cx.plivo.com/sip-trunking) first
* Outbound issues: Check LiveKit logs first

For error codes, see [Plivo hangup codes](/voice-agents/sip-trunking/troubleshooting/hangup-codes).

***

## Related

* [LiveKit SIP documentation](https://docs.livekit.io/sip/) - Complete LiveKit SIP configuration
* [LiveKit Plivo guide](https://docs.livekit.io/telephony/start/providers/plivo/) - LiveKit's official Plivo integration guide
* [SIP Trunking Overview](/sip-trunking) - Plivo SIP trunking documentation
