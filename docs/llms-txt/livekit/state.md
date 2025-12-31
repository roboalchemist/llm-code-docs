# Source: https://docs.livekit.io/transport/data/state.md

LiveKit docs › Data › State synchronization › Overview

---

# State synchronization overview

> An overview of state synchronization components for LiveKit.

## Overview

LiveKit includes multiple methods for synchronizing state within a room. Use participant attributes and room metadata to manage online status, user preferences, room configuration, and shared settings.

## State synchronization components

Synchronize participant-level and room-level state across all participants in a room.

| Component | Description | Use cases |
| **Participant attributes** | A key-value store for every participant that can be used for managing online status, user preferences, and more. | Online status indicators, user preferences, participant metadata, and per-participant configuration. |
| **Room metadata** | A freeform string for room-wide state, ideal for room configuration and shared settings. | Room configuration, shared settings, game state, and room-level data that applies to all participants. |

## In this section

Learn how to manage state synchronization.

- **[Participant attributes](https://docs.livekit.io/transport/data/state/participant-attributes.md)**: A key-value store for every participant that can be used for managing online status, user preferences, and more.

- **[Room metadata](https://docs.livekit.io/transport/data/state/room-metadata.md)**: A freeform string for room-wide state, ideal for room configuration and shared settings.

---

This document was rendered at 2025-12-31T18:29:37.956Z.
For the latest version of this document, see [https://docs.livekit.io/transport/data/state.md](https://docs.livekit.io/transport/data/state.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).