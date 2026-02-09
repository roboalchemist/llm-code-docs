# Source: https://docs.livekit.io/deploy/observability/data.md

# Source: https://docs.livekit.io/transport/data.md

LiveKit docs › Data › Overview

---

# Data overview

> An overview of realtime text and data features for LiveKit.

## Overview

LiveKit provides realtime data exchange between participants using text streams, byte streams, remote procedure calls (RPCs), and data packets. Exchange text messages, files, images, and custom data, or execute methods on other participants in the room.

## Realtime data components

Send and receive data between participants using streams, RPCs, or low-level data packets.

| Component | Description | Use cases |
| **Sending text** | Use text streams to send any amount of text between participants, with automatic chunking and topic-based routing. | Chat messages, streamed LLM responses, and realtime text communication. |
| **Sending files & bytes** | Use byte streams to transfer files, images, or any other binary data between participants with progress tracking. | File sharing, image transfer, and binary data exchange. |
| **Remote method calls** | Execute custom methods on other participants in the room and await a response, enabling app-specific coordination and data access. | Tool calls from AI agents, UI manipulation, and coordinated state management. |
| **Data packets** | Low-level API for sending individual packets with reliable or lossy delivery, providing advanced control over packet behavior. | High-frequency updates, custom protocols, and scenarios requiring precise packet control. |
| **State synchronization** | Synchronize participant attributes and room metadata across all participants in realtime. | User presence, room configuration, and shared state management. |

## In this section

Learn how to exchange data between participants.

- **[Sending text](https://docs.livekit.io/transport/data/text-streams.md)**: Use text streams to send and receive text data, such as LLM responses or chat messages.

- **[Sending files & bytes](https://docs.livekit.io/transport/data/byte-streams.md)**: Use byte streams to transfer files, images, or any other binary data.

- **[Remote method calls](https://docs.livekit.io/transport/data/rpc.md)**: Use RPC to execute custom methods on other participants in the room and await a response.

- **[Data packets](https://docs.livekit.io/transport/data/packets.md)**: Low-level API for high frequency or advanced use cases.

- **[State synchronization](https://docs.livekit.io/transport/data/state.md)**: Synchronize participant attributes and room metadata across all participants.

---

This document was rendered at 2026-02-03T03:25:18.565Z.
For the latest version of this document, see [https://docs.livekit.io/transport/data.md](https://docs.livekit.io/transport/data.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).