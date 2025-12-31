# Source: https://docs.livekit.io/transport.md

LiveKit docs › Get Started › Introduction

---

# Introduction

> Build realtime applications with LiveKit's WebRTC transport layer, SDKs, and media handling capabilities.

## Overview

LiveKit transport provides the foundation for building realtime applications using WebRTC. It includes client and server SDKs for multiple platforms, comprehensive media and data handling, stream export and import services, and hardware integration capabilities. Together, these components enable you to build production-ready realtime applications that work across web, mobile, hardware, and embedded devices.

LiveKit's transport layer handles the complexity of WebRTC connections, media encoding and decoding, network adaptation, and state synchronization. The SDKs provide a unified API across all platforms, ensuring consistent behavior whether you're building for web browsers, mobile apps, or embedded devices.

## Key concepts

Understand these core concepts to build effective realtime applications with LiveKit.

### SDK platforms

LiveKit provides a comprehensive ecosystem of SDKs for building realtime applications, including [realtime SDKs](#realtime-sdks) for building user-facing applications, and [server-side SDKs](#server-side-sdks) for backend operations and media processing. The SDKs are designed to work together, and support multiple platforms and languages.

All SDKs provide consistent APIs and features across platforms, ensuring that your applications work reliably regardless of the target platform. These core capabilities are designed to handle the complexities of realtime communication while providing a simple, unified API.

These capabilities include:

- **Unified room model**: Same room concepts across all platforms.
- **Consistent track handling**: Standardized audio and video track management.
- **Shared data APIs**: Common data channel and messaging patterns.
- **Quality adaptation**: Automatic quality adjustment based on network conditions.

- **[SDK platform quickstarts](https://docs.livekit.io/transport/sdk-platforms.md)**: Get started with LiveKit SDKs for React, Swift, Android, Flutter, React Native, Expo, Unity, and more.

#### Realtime SDKs

Realtime SDKs let you build applications that connect to LiveKit rooms and participate in realtime communication. These SDKs handle WebRTC connections, media capture, and room management.

- **Media capture**: Camera, microphone, and screen sharing.
- **Room management**: Join, leave, and manage room participants.
- **Track handling**: Subscribe to and publish audio and video tracks.
- **Data channels**: Realtime messaging between participants.
- **Connection management**: Automatic reconnection and quality adaptation.

- **[JavaScript SDK](https://github.com/livekit/client-sdk-js)**: JavaScript/TypeScript SDK for web browsers. Supports all major browsers and provides React hooks for easy integration.

- **[iOS/macOS/visionOS](https://github.com/livekit/client-sdk-swift)**: Native Swift SDK for Apple platforms including iOS, macOS, and visionOS. Optimized for Apple's ecosystem.

- **[Android](https://github.com/livekit/client-sdk-android)**: Native Kotlin SDK for Android applications. Provides comprehensive media handling and room management.

- **[Flutter](https://github.com/livekit/client-sdk-flutter)**: Cross-platform SDK for Flutter applications. Write once, run on iOS, Android, web, and desktop.

- **[React Native](https://github.com/livekit/client-sdk-react-native)**: React Native SDK for building cross-platform mobile applications with JavaScript/TypeScript.

- **[Unity](https://github.com/livekit/client-sdk-unity)**: Unity SDK for game development and virtual reality applications. Supports both native and WebGL builds.

LiveKit also supports specialized platforms and use cases beyond the main web and mobile platforms:

- **[Rust SDK](https://github.com/livekit/rust-sdks)**: For systems programming and embedded applications.
- **[Unity WebGL](https://github.com/livekit/client-sdk-unity-web)**: For web-based Unity applications.
- **[ESP32](https://github.com/livekit/client-sdk-esp32)**: For IoT and embedded devices.

#### Server-side SDKs

Server-side SDKs provide the infrastructure and control needed to manage LiveKit rooms and participants. These capabilities enable backend applications to orchestrate realtime sessions and process media streams.

- **Room control**: Create, manage, and monitor rooms.
- **Participant management**: Control participant permissions and behavior.
- **Media processing**: Subscribe to and process media streams.
- **Webhook handling**: Respond to room and participant events.
- **Recording**: Capture and store room sessions.

> ℹ️ **Info**
> 
> The Go SDK additionally offers client capabilities, allowing you to build automations that act like end users.

- **[Node.js](https://github.com/livekit/node-sdks)**: JavaScript SDK for Node.js applications. Includes room management, participant control, and webhook handling.

- **[Python](https://github.com/livekit/python-sdks)**: Python SDK for backend applications. Provides comprehensive media processing and room management capabilities.

- **[Golang](https://github.com/livekit/server-sdk-go)**: Go SDK for high-performance server applications. Optimized for scalability and low latency. Includes client capabilities.

- **[Ruby](https://github.com/livekit/server-sdk-ruby)**: Ruby SDK for Ruby on Rails and other Ruby applications. Full-featured server integration.

- **[Java/Kotlin](https://github.com/livekit/server-sdk-kotlin)**: Java and Kotlin SDK for JVM-based applications. Enterprise-ready with comprehensive features.

- **[Rust](https://github.com/livekit/rust-sdks)**: Rust SDK for systems programming and high-performance applications. Memory-safe and fast.

There are also community-maintained SDKs for other languages:

- **[PHP](https://github.com/agence104/livekit-server-sdk-php)**: Community-maintained SDK for PHP applications.
- **[.NET](https://github.com/pabloFuente/livekit-server-sdk-dotnet)**: Community-maintained SDK for .NET applications.

### Media

LiveKit enables realtime exchange of audio and video streams between participants. You can publish and subscribe to tracks, process raw media, apply noise cancellation, and export or import streams.

- **[Media overview](https://docs.livekit.io/transport/media.md)**: Learn how to handle realtime media tracks, screen sharing, and stream export/import in your applications.

### Data

LiveKit provides realtime data exchange between participants using text streams, byte streams, remote procedure calls, and data packets. You can also synchronize state across all participants in a room.

- **[Data overview](https://docs.livekit.io/transport/data.md)**: Learn how to send text, files, and custom data, and synchronize state between participants.

### Encryption

Secure your realtime media and data with end-to-end encryption. LiveKit provides built-in E2EE support for both media tracks and data channels.

- **[Encryption overview](https://docs.livekit.io/transport/encryption.md)**: Learn how to enable end-to-end encryption for media and data in your applications.

### Self-hosting

Self-host LiveKit servers for full control over your WebRTC infrastructure, data, and configuration. Deploy LiveKit servers on local development environments, virtual machines, Kubernetes clusters, or distributed multi-region setups.

- **[Self-hosting overview](https://docs.livekit.io/transport/self-hosting.md)**: Learn how to self-host LiveKit servers for full control over your infrastructure.

### Hardware

Build realtime applications for embedded devices, ESP32 microcontrollers, and other hardware platforms. LiveKit provides specialized SDKs and tools for integrating with physical devices for IoT and edge computing use cases.

- **[Hardware overview](https://docs.livekit.io/transport/hardware.md)**: Learn how to integrate LiveKit with hardware devices and embedded systems.

## Getting started

Choose your platform to get started building your application:

- **[SDK platform quickstarts](https://docs.livekit.io/transport/sdk-platforms.md)**: Get started with LiveKit SDKs for your target platform with step-by-step guides.

---

This document was rendered at 2025-12-31T18:29:36.691Z.
For the latest version of this document, see [https://docs.livekit.io/transport.md](https://docs.livekit.io/transport.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).