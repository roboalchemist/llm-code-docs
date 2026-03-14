# Source: https://plivo.com/docs/voice-agents/sip-trunking/integration-guides/vapi.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vapi Integration

> Connect Plivo SIP trunking with Vapi for voice AI assistants

Connect Plivo SIP trunking to Vapi to enable your voice AI assistants to make and receive phone calls through Plivo's global voice network.

***

## Prerequisites

| Requirement       | Description                                                               |
| ----------------- | ------------------------------------------------------------------------- |
| **Plivo Account** | [Sign up](https://www.plivo.com/request-trial/) with SIP trunking enabled |
| **Phone Number**  | [Purchase a voice-enabled number](https://cx.plivo.com/phone-numbers)     |
| **Vapi Account**  | [Create account](https://dashboard.vapi.ai/)                              |

<Warning>
  **India not supported:** Indian phone numbers are not compatible with Vapi due to TRAI regulations requiring SIP termination on Indian servers. Vapi does not currently support this requirement.
</Warning>

<Tip>
  **Optimize for latency:** For best call quality, ensure your Vapi deployment is in a region closest to your call traffic. This minimizes audio delay and improves conversation flow.
</Tip>

***

## Part 1: Make Outgoing Calls

Enable Vapi to make outbound calls through Plivo.

### Step 1: Create IP Access Control List in Plivo

Vapi uses IP-based authentication for outbound calls.

1. Go to [SIP Trunking → Outbound Trunks → IP Access Control List](https://cx.plivo.com/sip-trunking)
2. Click **Create New IP Access Control List**
3. Enter a name (e.g., `Vapi-IPs`)
4. Add the following Vapi IP addresses:
   * `44.229.228.186/32`
   * `44.238.177.138/32`
5. Click **Create**

### Step 2: Create an Outbound Trunk in Plivo

1. Go to [SIP Trunking → Outbound Trunks](https://cx.plivo.com/sip-trunking)
2. Click **Create New Outbound Trunk**
3. Enter a name (e.g., `Vapi-Outbound`)
4. Select the **IP Access Control List** you created
5. Click **Create Trunk**
6. Copy your **Termination SIP Domain** (e.g., `XXXXXXXXXXXX.zt.plivo.com`)

### Step 3: Configure Vapi

Use the termination domain from Plivo to configure outbound calling in Vapi. See [Vapi Plivo integration guide](https://docs.vapi.ai/advanced/sip/plivo) for detailed steps.

***

## Part 2: Receive Incoming Calls

Route calls from your Plivo phone number to Vapi.

### Step 1: Create an Inbound Trunk in Plivo

1. Go to [SIP Trunking → Inbound Trunks](https://cx.plivo.com/sip-trunking)
2. Click **Create New Inbound Trunk**
3. Enter a name (e.g., `Vapi-Inbound`)
4. Click **Add New URI** and configure:

| Field   | Value                       |
| ------- | --------------------------- |
| Name    | `Vapi-Primary`              |
| SIP URI | `sip.vapi.ai;transport=udp` |

5. Click **Create Trunk**

### Step 2: Connect Your Phone Number

1. Go to [Your Numbers](https://cx.plivo.com/phone-numbers)
2. Click on your phone number
3. Set **Application Type** to `Zentrunk`
4. Set **Trunk** to your inbound trunk
5. Click **Update Number**

### Step 3: Configure Vapi

Register your phone number in Vapi to accept incoming calls. See [Vapi Plivo integration guide](https://docs.vapi.ai/advanced/sip/plivo) for detailed steps.

***

## Troubleshooting

| Issue                  | Solution                                                                    |
| ---------------------- | --------------------------------------------------------------------------- |
| Call doesn't connect   | Verify SIP URI uses `transport=udp` for inbound. Check IP ACL for outbound. |
| Outbound calls failing | Verify Vapi IP addresses are correctly whitelisted in IP ACL.               |

**Debug logs:**

* Inbound issues: Check [Plivo logs](https://cx.plivo.com/sip-trunking) first
* Outbound issues: Check Vapi logs first

For error codes, see [Plivo hangup codes](/voice-agents/sip-trunking/troubleshooting/hangup-codes).

***

## Related

* [Vapi Plivo guide](https://docs.vapi.ai/advanced/sip/plivo) - Vapi's official Plivo integration guide
* [Vapi documentation](https://docs.vapi.ai/) - Complete Vapi documentation
* [SIP Trunking Overview](/sip-trunking) - Plivo SIP trunking documentation
