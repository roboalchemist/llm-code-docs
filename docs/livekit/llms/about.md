# Source: https://docs.livekit.io/intro/about.md

LiveKit docs › Get Started › About LiveKit

---

# About LiveKit

> An overview of the LiveKit ecosystem.

## What is LiveKit?

LiveKit is an open source framework and cloud platform for building voice, video, and physical AI agents. It provides the tools you need to build agents that interact with users in realtime over audio, video, and data streams. Agents run on the LiveKit server, which supplies the low-latency infrastructure—including transport, routing, synchronization, and session management—built on a production-grade WebRTC stack. This architecture enables reliable and performant agent workloads.

### About WebRTC

The internet's core protocols weren't designed for realtime media. Hypertext Transfer Protocol (HTTP) is optimized for request-response communication, which is effective for the web's client-server model, but not for continuous audio and video streams. Historically, developers building realtime media applications had to work directly with the complexities of WebRTC.

WebRTC is a browser-native technology for transmitting audio and video in realtime. Unlike general-purpose transports such as websockets, WebRTC is optimized for media delivery, providing efficient codecs and automatically adapting to unreliable network conditions. Because all major browsers support WebRTC, it works consistently across platforms. LiveKit manages the operational and scaling challenges of WebRTC and extends its use to mobile applications, backend services, and telephony integrations.

## Why use LiveKit?

LiveKit differentiates itself through several key advantages:

**Build faster with high-level abstractions:** Use the LiveKit Agents framework to quickly build production-ready AI agents with built-in support for speech processing, turn-taking, multimodal events, and LLM integration. When you need custom behavior, access lower-level WebRTC primitives for complete control.

**Write once, deploy everywhere:** Both human clients and AI agents use the same SDKs and APIs, so you can write agent logic once and deploy it across Web, iOS, Android, Flutter, Unity, and backend environments. Agents and clients interact seamlessly regardless of platform.

**Focus on building, not infrastructure:** LiveKit handles the operational complexity of WebRTC so developers can focus on building agents. Choose between fully managed LiveKit Cloud or self-hosted deployment—both offer identical APIs and core capabilities.

**Connect to any system:** Extend LiveKit with egress, ingress, telephony, and server APIs to build end-to-end workflows that span web, mobile, phone networks, and physical devices.

## What can I build?

LiveKit supports a wide range of applications:

- **AI assistants:** Multimodal AI assistants and avatars that interact through voice, video, and text.
- **Video conferencing:** Secure, private meetings for teams of any size.
- **Interactive livestreaming:** Broadcast to audiences with realtime engagement.
- **Customer service:** Flexible and observable web, mobile, and telephone support options.
- **Healthcare:** HIPAA-compliant telehealth with AI and humans in the loop.
- **Robotics:** Integrate realtime video and powerful AI models into real-world devices.

LiveKit provides the realtime foundation—low latency, scalable performance, and flexible tools—needed to run production-ready AI experiences.

## How does LiveKit work?

LiveKit's architecture consists of several key components that work together.

### LiveKit server

LiveKit server is an open source [WebRTC](#webrtc) Selective Forwarding Unit (SFU) that orchestrates realtime communication between participants and agents. The server handles signaling, network address translation (NAT) traversal, RTP routing, adaptive degradation, and quality-of-service controls. You can use [LiveKit Cloud](https://livekit.io/cloud), a fully managed cloud service, or self-host LiveKit server on your own infrastructure.

### LiveKit Agents framework

The [LiveKit Agents framework](https://docs.livekit.io/agents.md) provides high-level tools for building AI agents, including speech processing, turn-taking, multimodal events, and LLM integration. Agents join rooms as participants and can process incoming media, synthesize output, and interact with users through the same infrastructure that powers all LiveKit applications. For lower-level control over raw media tracks, you can use the SDKs and clients.

### SDKs and clients

Native SDKs for Web, iOS, Android, Flutter, Unity, and backend environments provide a consistent programming model. Both human clients and AI agents use the same SDKs to join rooms, publish and subscribe to media tracks, and exchange data.

### Integration services

LiveKit provides additional services that enable you to connect to any system. LiveKit supports recording and streaming (Egress), external media streams (Ingress), integration with SIP, PSTN, and other communication systems (Telephony), and server APIs for programmatic session management.

## How can I learn more?

This documentation site is organized into several main sections:

- [**Introduction:**](https://docs.livekit.io/intro/basics.md) Start here to understand LiveKit's core concepts and get set up.
- [**Build Agents:**](https://docs.livekit.io/agents.md) Learn how to build AI agents using the LiveKit Agents framework.
- [**Agent Frontends:**](https://docs.livekit.io/frontends.md) Build web, mobile, and hardware interfaces for agents.
- [**Telephony:**](https://docs.livekit.io/telephony.md) Connect agents to phone networks and traditional communication systems.
- [**WebRTC Transport:**](https://docs.livekit.io/transport.md) Deep dive into WebRTC concepts and low-level transport details.
- [**Manage & Deploy:**](https://docs.livekit.io/deploy.md) Deploy and manage LiveKit agents and infrastructure, and learn how to test, evaluate, and observe agent performance.
- [**Reference:**](https://docs.livekit.io/reference.md) API references, SDK documentation, and component libraries.

Use the sidebar navigation to explore topics within each section. Each page includes code examples, guides, and links to related concepts. Start with [Understanding LiveKit overview](https://docs.livekit.io/intro/basics.md) to learn core concepts, then follow the guides that match your use case.

---

This document was rendered at 2026-02-03T03:24:50.873Z.
For the latest version of this document, see [https://docs.livekit.io/intro/about.md](https://docs.livekit.io/intro/about.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).