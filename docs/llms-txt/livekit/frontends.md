# Source: https://docs.livekit.io/frontends/start/frontends.md

# Source: https://docs.livekit.io/frontends.md

# Source: https://docs.livekit.io/frontends/start/frontends.md

# Source: https://docs.livekit.io/frontends.md

LiveKit docs › Get Started › Introduction

---

# Introduction

> Build frontends for your LiveKit Agents across web, mobile, hardware, and telephony platforms.

## Overview

Frontends are the user-facing interfaces that connect to your LiveKit Agents, enabling realtime communication over audio, video, text, and data streams. LiveKit provides SDKs and tooling to build responsive, production-ready frontends for web, mobile, and telephony apps, as well as hardware, embedded systems, and robotics.

Agents communicate with frontends through LiveKit rooms using WebRTC, which delivers fast and reliable realtime connectivity. LiveKit SDKs handle media transport, connection management, and state synchronization ensuring your frontends stay reliable and performant.

## Frontend types

LiveKit Agents support multiple frontend platforms and use cases:

- **[Web & mobile frontends](https://docs.livekit.io/frontends/start/frontends.md)**: Build frontends that connect to your agents using JavaScript, Swift, Android, Flutter, React Native, and more.

- **[Hardware & devices](https://docs.livekit.io/frontends/start/hardware.md)**: Integrate your agents with embedded devices, ESP32 microcontrollers, and other hardware platforms.

- **[Telephony integration](https://docs.livekit.io/frontends/telephony.md)**: Integrate your agents with traditional and IP-based telephony systems to make and receive phone calls.

## Key concepts

Understand these core concepts to build effective frontends for your LiveKit Agents.

### UI components

LiveKit provides prebuilt UI component libraries for popular frontend frameworks that simplify building realtime audio and video applications:

- **React components**: Prebuilt React components with automatic state management
- **Swift components**: SwiftUI components for iOS, macOS, visionOS, and tvOS
- **Android components**: Jetpack Compose components with Material Design
- **Flutter components**: Cross-platform widgets for mobile and desktop

- **[UI components overview](https://docs.livekit.io/frontends/components.md)**: Learn about the available UI component libraries and how to use them.

### Authentication

All LiveKit frontends require JWT-based access tokens to connect to rooms. Tokens encode participant identity, room permissions, and capabilities, and are generated on your backend server.

- **[Authentication guide](https://docs.livekit.io/frontends/authentication.md)**: Learn how to generate tokens, configure grants, and manage permissions for your frontends.

### Telephony

Integrate your frontends with telephony-based communication systems to enable voice AI agents to make and receive phone calls. LiveKit telephony enables callers to join LiveKit rooms as SIP participants and your frontend can display call status and handle call controls.

- **[Telephony overview](https://docs.livekit.io/frontends/telephony.md)**: Learn how to build frontends that work with voice AI agents handling phone calls.

### Hardware & devices

Build frontends for embedded devices and hardware platforms, including ESP32 microcontrollers and Embedded Linux systems. These frontends enable your agents to run on physical devices for IoT and edge computing use cases.

- **[Hardware & devices overview](https://docs.livekit.io/frontends/hardware.md)**: Learn how to integrate your agents with hardware devices and embedded systems.

## Getting started

Choose your platform to get started building a frontend for your agent:

- **[Web & mobile quickstart](https://docs.livekit.io/frontends/start/frontends.md)**: Get started with web and mobile frontends using starter apps and platform-specific guides.

- **[Hardware quickstart](https://docs.livekit.io/frontends/start/hardware.md)**: Begin building hardware integrations for your agents.

- **[Telephony quickstart](https://docs.livekit.io/frontends/telephony/agents.md)**: Enable your agent to handle phone calls through SIP integration.

## Additional resources

For complete SDK documentation, API references, and advanced topics, see the [Reference](https://docs.livekit.io/reference.md) section.

- **[LiveKit SDKs](https://docs.livekit.io/reference.md#livekit-sdks)**: Complete documentation for all LiveKit client SDKs.

- **[UI components reference](https://docs.livekit.io/reference.md#ui-components)**: API references and examples for React, Swift, Android, and Flutter components.

---

This document was rendered at 2025-12-31T18:29:33.651Z.
For the latest version of this document, see [https://docs.livekit.io/frontends.md](https://docs.livekit.io/frontends.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).