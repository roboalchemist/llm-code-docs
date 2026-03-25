# Source: https://plivo.com/docs/voice-agents/sip-trunking/troubleshooting/hangup-codes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Hangup Codes

> Understanding SIP hangup codes for voice agent calls

When calls disconnect, Plivo returns hangup codes to help identify the cause.

***

## Hangup Sources

| Source       | Description                             |
| ------------ | --------------------------------------- |
| **Customer** | Hangup initiated by your infrastructure |
| **Carrier**  | Hangup initiated by the remote carrier  |
| **Zentrunk** | Hangup initiated by Plivo               |

***

## Common Hangup Codes

| Code | Cause                           | Solution                                          |
| ---- | ------------------------------- | ------------------------------------------------- |
| 4030 | Insufficient credits            | Add credits to your account                       |
| 4190 | Unknown caller ID               | Use a Plivo-rented number as caller ID            |
| 4590 | India media anchoring violation | Ensure server is located in India for India calls |
| 5180 | CPS limit reached               | Contact support to increase limits                |
| 5190 | Concurrent call limit exceeded  | Contact support to increase limits                |

***

## Full Hangup Code Reference

For the complete list of 60+ hangup codes with detailed descriptions, see [Zentrunk Hangup Codes](/sip-trunking/troubleshooting/zentrunk-hangup-codes).

***

## Debug Logs

Debug logs help troubleshoot connectivity issues during SIP trunking calls. Access them in the Plivo Console under Zentrunk → Logs.

### What's in Debug Logs

| Section          | Information                                                           |
| ---------------- | --------------------------------------------------------------------- |
| **Call Details** | Initiation time, from/to numbers, duration, charges, STIR attestation |
| **Call Stats**   | Trunk ID, domain, transport protocol, hangup cause/source             |
| **SIP Logs**     | Final SIP response, negotiated codec, downloadable SIP PCAP           |

### Full Debug Logs Guide

For detailed information on interpreting debug logs, see [Zentrunk Debug Logs](/sip-trunking/troubleshooting/zentrunk-debug-logs).
