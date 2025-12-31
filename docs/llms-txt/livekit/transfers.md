# Source: https://docs.livekit.io/telephony/features/transfers.md

LiveKit docs › Features › Transfers › Overview

---

# Transfers overview

> An overview of call transfer features for LiveKit telephony.

## Overview

Transfer calls between participants, phone numbers, and SIP endpoints. Use cold transfers to forward calls directly, or warm transfers with agent assistance to provide context and handle transfer failures gracefully.

## Transfer types

Transfer calls using different methods depending on your use case and whether you need agent assistance.

| Transfer type | Description | Use cases |
| **Call forwarding** (cold transfer) | Forward calls to another phone number or SIP endpoint using SIP REFER, closing the caller's LiveKit session. | Direct call forwarding, transferring to external numbers, and simple call routing without agent involvement. |
| **Agent-assisted transfer** (warm transfer) | Transfer calls with agent assistance, allowing the agent to provide context, handle transfer failures, and return to the caller if needed. | Escalating to human operators, providing call summaries during transfer, and handling transfer failures gracefully. |

## In this section

Read more about each transfer type.

- **[Call forwarding](https://docs.livekit.io/telephony/features/transfers/cold.md)**: Transfer calls to another number or SIP endpoint using SIP REFER.

- **[Agent-assisted transfer](https://docs.livekit.io/telephony/features/transfers/warm.md)**: Transfer calls with agent assistance and context.

---

This document was rendered at 2025-12-31T18:29:35.254Z.
For the latest version of this document, see [https://docs.livekit.io/telephony/features/transfers.md](https://docs.livekit.io/telephony/features/transfers.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).