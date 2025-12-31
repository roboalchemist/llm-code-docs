# Source: https://docs.livekit.io/deploy/admin/regions.md

LiveKit docs › Administration › Regions › Overview

---

# Regions

> Configure and manage regional deployments or restrictions.

## Overview

LiveKit is a globally distributed service and regions represent geographic locations where services run. Users of LiveKit apps connect to the closest server, or _edge_, to minimize latency and improve the overall realtime experience.

Using default regions and allowing LiveKit to route traffic to the closest server is typically the best approach. However, in some cases, you might need to make explicit decisions about region assignment, or restrict traffic to a specific region.

## Regions topics

Learn more about managing regions for your LiveKit apps with these topics.

| Component | Description | Use cases |
| **Region pinning** | Isolate traffic to a specific region to comply with local regulatory restrictions or meet data residency requirements. | Meeting data residency requirements and isolating data to specific regions. |
| **Agent deployment** | Configure and manage agent deployments across multiple regions. | Deploying agents in multiple regions, optimizing latency, and managing regional deployments. |
| **Region pinning for telephony** | Isolate telephony traffic to a specific region to comply with local regulatory restrictions. To learn more, see the [Region pinning for telephony](https://docs.livekit.io/telephony/features/region-pinning.md) topic. | Complying with local telephony regulations and isolating data to specific regions. |

## In this section

Limit regional traffic, or deploy your agents to specific regions, to meet your application needs.

- **[Region pinning](https://docs.livekit.io/deploy/admin/regions/region-pinning.md)**: Limit network traffic and isolate data to specific regions.

- **[Agent deployment](https://docs.livekit.io/deploy/admin/regions/agent-deployment.md)**: Deploy agents to specific regions to optimize latency and manage regional deployments.

---

This document was rendered at 2025-12-31T18:29:39.015Z.
For the latest version of this document, see [https://docs.livekit.io/deploy/admin/regions.md](https://docs.livekit.io/deploy/admin/regions.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).