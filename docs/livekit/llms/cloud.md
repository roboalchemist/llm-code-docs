# Source: https://docs.livekit.io/intro/cloud.md

LiveKit docs › Understanding LiveKit › LiveKit Cloud

---

# LiveKit Cloud

> An end-to-end platform for building, deploying, and operating AI agent applications.

## Overview

LiveKit Cloud is a fully managed, globally distributed platform for building, hosting, and operating AI agent applications at scale.

While LiveKit's open-source server provides the realtime media foundation, LiveKit Cloud extends beyond managed infrastructure. It combines realtime audio, video, and data streaming with agent development tools, managed agent hosting, built-in inference, native telephony, and production-grade observability in a single, cohesive platform.

## What LiveKit Cloud includes

**Realtime communication core**: A fully managed, globally distributed mesh of LiveKit servers that powers low-latency audio, video, and data streaming for realtime applications.

**Agent Builder**: Design, test, and iterate on AI agents using a purpose-built development experience. Agent Builder streamlines prompt design, tool configuration, and interaction flows.

**Managed agent hosting**: Deploy and run agents directly on LiveKit Cloud without managing servers or orchestration. LiveKit handles scaling, lifecycle management, isolation, and upgrades.

**Built-in inference**: LiveKit Inference lets you run supported AI models directly within the LiveKit Cloud environment without requiring API keys.

**Native telephony**: LiveKit Phone Numbers lets you provision phone numbers and connect PSTN calls directly into LiveKit rooms without setting up trunks.

**Observability and operations**: Production-grade analytics, logs, and quality metrics are built into the LiveKit Cloud dashboard, giving visibility into agent behavior, media quality, usage, and performance across your deployment.

- **[Dashboard](https://cloud.livekit.io)**: Sign up for LiveKit Cloud to manage projects, configure agents and telephony, and view detailed analytics.

- **[Pricing](https://livekit.io/pricing)**: View LiveKit Cloud pricing plans and choose the right option for your application's needs.

### Why choose LiveKit Cloud?

- **End-to-end platform**: Build, deploy, and operate AI agents, realtime media, inference, and telephony in one system.
- **Zero operational overhead**: No need to manage servers, scaling, or infrastructure.
- **Global edge network**: Users connect to the closest region for minimal latency.
- **Elastic, unlimited scale**: Support for rooms with unlimited participants using LiveKit's global mesh architecture.
- **Enterprise-grade reliability**: 99.99% uptime guarantee with redundant infrastructure.
- **Comprehensive analytics**: Monitor usage, performance, and quality metrics through the LiveKit Cloud dashboard.
- **Seamless developer experience**: Use the same APIs and SDKs as open source, with additional cloud-native capabilities.

### Open source compatible, platform complete

LiveKit Cloud runs the same open-source LiveKit server available on [GitHub](https://github.com/livekit/livekit) and supports the same APIs and SDKs. This means:

- You can start on open source and migrate to LiveKit Cloud without rewriting application code.
- You can move from LiveKit Cloud to self-hosted if your requirements change.
- Your client and agent code remains portable—the connection endpoint is the primary difference.

What does differ is everything around the server: agent tooling, hosting, inference, telephony, global scaling, and observability, all of which are native features of LiveKit Cloud.

### Comparing LiveKit Cloud to self-hosted

When building with LiveKit, you can run the open-source server yourself or use LiveKit Cloud as a fully managed, end-to-end platform:

|  | Self-hosted | LiveKit Cloud |
| **Realtime media (audio, video, data)** | Full support | Full support |
| **Egress (recording, streaming)** | Full support | Full support |
| **Ingress (RTMP, WHIP, SRT ingest)** | Full support | Full support |
| **SIP & telephony** | Full support | Full support including native telephony support for fully managed LiveKit Phone Numbers |
| **Agents framework** | Full support | Full support, including managed agent hosting. |
| **Agent Builder** | N/A | Included |
| **Built-in inference** | N/A | Included |
| **Who manages it** | You | LiveKit |
| **Architecture** | Single-home SFU | Global mesh SFU |
| **Connection model** | Single server per room | Each user connects to the nearest edge. |
| **Max users per room** | Up to ~3,000 | No limit |
| **Analytics & telemetry** | Custom / external. | LiveKit Cloud dashboard |
| **Uptime guarantees** | N/A | 99.99% |

## LiveKit Cloud administration

For information about LiveKit Cloud architecture, administration, and configuration, see the [Administration](https://docs.livekit.io/deploy/admin.md) section.

## Next steps

Ready to deploy your agents? Get started with the [Agent deployment guide](https://docs.livekit.io/deploy/agents.md).

---

This document was rendered at 2026-02-03T03:24:52.329Z.
For the latest version of this document, see [https://docs.livekit.io/intro/cloud.md](https://docs.livekit.io/intro/cloud.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).