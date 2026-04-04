# Source: https://docs.livekit.io/transport/self-hosting.md

LiveKit docs › Self-hosting › Overview

---

# Self-hosting overview

> An overview of self-hosting options for LiveKit servers.

## Overview

Self-host LiveKit servers for full control over your infrastructure, data, and configuration. Self-hosting enables you to deploy LiveKit on your own infrastructure, whether for local development, production deployments on virtual machines or Kubernetes, or distributed multi-region setups.

Self-hosting gives you complete control over your deployment, allowing you to customize configuration, manage your own data, and scale according to your specific needs. You can deploy LiveKit servers on a variety of platforms, from local development environments to production-grade infrastructure. You can also deploy LiveKit Agents to your own infrastructure, connecting them to your self-hosted LiveKit server.

### Comparing self-hosted to LiveKit Cloud

When building with LiveKit, you can either self-host the open-source server or use the managed LiveKit Cloud service:

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

## Self-hosting topics

When self-hosting LiveKit, you can deploy agents to your own infrastructure alongside your LiveKit server. Agents connect to your self-hosted server and run on your own resources. See [Custom agent deployments](https://docs.livekit.io/deploy/custom/deployments.md) for details on deploying agents to Kubernetes, Render, or other container orchestration systems.

Manage your self-hosted LiveKit deployment with these topics.

| Topic | Description | Use cases |
| **Running locally** | Get LiveKit running locally for development and testing with minimal setup. | Local development, testing, and prototyping. |
| **Deployment** | Deploy LiveKit servers to production with SSL, load balancing, and TURN configuration. | Production deployments, secure configurations, and network setup. |
| **Virtual machines** | Deploy LiveKit servers on virtual machines for production use. | VM-based deployments, cloud infrastructure, and traditional server setups. |
| **Kubernetes** | Deploy LiveKit servers on Kubernetes clusters for scalable, containerized deployments. | Container orchestration, scalable deployments, and cloud-native infrastructure. |
| **Distributed multi-region** | Deploy LiveKit servers across multiple regions for global distribution. | Global deployments, low-latency access, and multi-region redundancy. |
| **Firewall configuration** | Configure firewalls and network settings for your LiveKit deployment. | Network security, port management, and access control. |
| **Benchmarks** | Measure and optimize performance of your self-hosted LiveKit deployment. | Performance testing, capacity planning, and optimization. |
| **Egress** | Set up egress services for recording and streaming from your self-hosted deployment. | Recording rooms, streaming to platforms, and media export. |
| **Ingress** | Set up ingress services to bring external media sources into your LiveKit rooms. | RTMP ingest, WHIP streams, and external media integration. |
| **SIP server** | Deploy and configure SIP servers for telephony integration with your self-hosted LiveKit. | Phone call integration, SIP trunking, and telephony features. |

## In this section

Learn how to self-host LiveKit servers:

- **[Running locally](https://docs.livekit.io/transport/self-hosting/local.md)**: Get LiveKit running locally for development and testing.

- **[Deployment](https://docs.livekit.io/transport/self-hosting/deployment.md)**: Deploy LiveKit servers to production with SSL, load balancing, and TURN configuration.

- **[Virtual machines](https://docs.livekit.io/transport/self-hosting/vm.md)**: Deploy LiveKit servers on virtual machines for production use.

- **[Kubernetes](https://docs.livekit.io/transport/self-hosting/kubernetes.md)**: Deploy LiveKit servers on Kubernetes clusters for scalable, containerized deployments.

- **[Distributed multi-region](https://docs.livekit.io/transport/self-hosting/distributed.md)**: Deploy LiveKit servers across multiple regions for global distribution.

- **[Firewall configuration](https://docs.livekit.io/transport/self-hosting/ports-firewall.md)**: Configure firewalls and network settings for your LiveKit deployment.

- **[Benchmarks](https://docs.livekit.io/transport/self-hosting/benchmark.md)**: Measure and optimize performance of your self-hosted LiveKit deployment.

- **[Egress](https://docs.livekit.io/transport/self-hosting/egress.md)**: Set up egress services for recording and streaming from your self-hosted deployment.

- **[Ingress](https://docs.livekit.io/transport/self-hosting/ingress.md)**: Set up ingress services to bring external media sources into your LiveKit rooms.

- **[SIP server](https://docs.livekit.io/transport/self-hosting/sip-server.md)**: Deploy and configure SIP servers for telephony integration with your self-hosted LiveKit.

---

This document was rendered at 2026-02-03T03:25:19.997Z.
For the latest version of this document, see [https://docs.livekit.io/transport/self-hosting.md](https://docs.livekit.io/transport/self-hosting.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).