# Source: https://plivo.com/docs/sip-trunking/concepts/technical-specifications.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Technical Specifications

> SIP methods, codecs, data centers, limits, and networking requirements for Zentrunk

This page covers the technical specifications and requirements for Plivo's Zentrunk SIP trunking service.

***

## What is Zentrunk?

Zentrunk is Plivo's cloud-based SIP trunking service that connects IP PBX systems to PSTN and mobile networks.

***

## Supported SIP Methods

| Status            | Methods                                                    |
| ----------------- | ---------------------------------------------------------- |
| **Supported**     | ACK, BYE, CANCEL, INVITE, OPTIONS, REFER, UPDATE           |
| **Not supported** | INFO, MESSAGE, NOTIFY, PRACK, PUBLISH, REGISTER, SUBSCRIBE |

### SIP REFER (Call Transfer)

Plivo supports SIP REFER for call transfers. This enables:

* **Blind transfers**: Transfer a call to another destination without consultation
* **Attended transfers**: Consult with the transfer target before completing the transfer

SIP REFER allows your PBX or SIP endpoint to initiate call transfers using standard SIP signaling.

***

## Codecs and Encryption

| Feature                  | Supported       |
| ------------------------ | --------------- |
| **Codecs**               | PCMA, PCMU      |
| **Signaling encryption** | TLS             |
| **Media encryption**     | SRTP            |
| **DTMF**                 | RFC-2833 format |

<Note>
  Call recording and T.38 fax are not supported.
</Note>

***

## Data Center Locations

| Region        | Location                   |
| ------------- | -------------------------- |
| North America | North California, Virginia |
| Europe        | Frankfurt                  |
| South America | São Paulo                  |
| Asia Pacific  | Singapore, Sydney, Mumbai  |

***

## Calls Per Second (CPS) Limits

| Level         | Default      | Description                              |
| ------------- | ------------ | ---------------------------------------- |
| Account-level | 2 CPS        | Total calls per second across all trunks |
| Trunk-level   | Configurable | Allocated per trunk from account pool    |

**Call queuing behavior:**

* Calls exceeding trunk CPS fail immediately
* Calls exceeding account CPS queue for processing

Contact [Plivo Sales](https://www.plivo.com/contact/sales/) to increase your CPS allocation.

***

## Resource Limits

| Resource            | Limit                       |
| ------------------- | --------------------------- |
| Trunks per account  | 100 (recommended)           |
| IP ACLs per account | Unlimited                   |
| Concurrent calls    | Unlimited (elastic scaling) |

***

## IP Whitelisting Requirements

Whitelist these CIDR blocks for Zentrunk connectivity:

| Region           | CIDR Blocks                                                 |
| ---------------- | ----------------------------------------------------------- |
| North California | `13.52.9.0/25`, `216.120.187.128/26`                        |
| Virginia         | `18.214.109.128/25`, `18.215.142.0/26`, `204.89.148.128/26` |
| Frankfurt        | `3.120.121.128/26`                                          |
| São Paulo        | `18.228.70.64/26`                                           |
| Sydney           | `13.238.202.192/26`                                         |

**Required ports:**

* **Signaling:** 5060 (UDP/TCP), 5061 (TLS)
* **Media:** 10000-30000 (UDP/TCP)

***

## Authentication Methods

* IP Access Control Lists
* Username/password credentials
* Both combined

***

## SIP OPTIONS Pings

* Send pings to the outbound trunk URI only
* Maximum frequency: 1 ping per 10-15 seconds
* Higher frequency may trigger blocking

***

## Caller ID Requirements

Plivo numbers are required as caller ID for all outbound calls. Using non-Plivo numbers results in an `unknown_caller_id` hangup.

**Options:**

* Rent numbers through the Plivo console
* Port existing numbers to Plivo
* Contact [Plivo Support](https://support.plivo.com) for special cases

**Countries with guaranteed domestic CLI:** US, Canada, UK, Australia, Italy, Peru, and France (beta).

***

## Premium Number Restrictions

Zentrunk blocks calls to premium-rate numbers to prevent toll fraud (IRSF - International Revenue Share Fraud).

To enable premium number calling:

1. Contact [Plivo Support](https://support.plivo.com)
2. Provide use case details
3. Wait for validation (48+ hours)

***

## Pricing

Call rates vary by originating country, not just destination. For example, calls to Germany from Europe cost less than from outside Europe.

Check [Zentrunk Pricing](https://www.plivo.com/pricing/zentrunk/) for current rates.

### Short Duration Call Charges

| Type                        | Threshold     | Surcharge                |
| --------------------------- | ------------- | ------------------------ |
| Abandoned calls (0 seconds) | > 20% monthly | \$0.005 per excess call  |
| Short calls (≤6 seconds)    | > 20% monthly | \$0.0025 per excess call |

***

## Country-Specific Requirements

### Australia

Per ACMA regulations, these CLI prefixes are blocked: `+6113`, `+611300`, `+611800`, `+611900`

### China

**Prohibited traffic:**

* Gambling, financial services, cryptocurrency
* Marketing/spam calls
* Fraudulent calls
* Politically sensitive content

**Outbound requirements:**

* Cannot use Chinese caller IDs
* Maintain average call duration over 3 minutes
* Avoid high unanswered rates
* Don't use toll-free numbers

**Inbound requirements:**

* Chinese numbers can only receive calls from within China

***

## Compatible Systems

| Type                           | Examples                                      |
| ------------------------------ | --------------------------------------------- |
| **IP PBX**                     | FreeSWITCH, Asterisk, FreePBX, 3CX, FusionPBX |
| **Session Border Controllers** | Various vendors                               |
| **Softphones**                 | Zoiper, X-Lite/Bria                           |

### Softphone Setup

1. Create an account in your softphone
2. Uncheck "register with domain and receive calls"
3. Configure with your Zentrunk SIP URI

***

## Call Detail Records

Access CDRs in the Plivo console:

1. Navigate to **Zentrunk > Logs**
2. Filter CDRs as needed
3. Click **Export** to download

Debug information available (no charge):

* Call details (basic info)
* Call stats (origination, termination, trunk info)
* SIP logs (PCAP, last response, codec)

***

## Related

* [Geo Permissions](/sip-trunking/concepts/geo-permissions)
* [STIR/SHAKEN](/sip-trunking/concepts/stir-shaken)
* [Troubleshooting](/sip-trunking/troubleshooting/zentrunk-hangup-codes)
