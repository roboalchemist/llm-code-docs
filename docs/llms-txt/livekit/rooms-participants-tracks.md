# Source: https://docs.livekit.io/intro/basics/rooms-participants-tracks.md

LiveKit docs › Understanding LiveKit › Rooms, participants, & tracks › Overview

---

# Rooms, participants, and tracks overview

> Understand the core building blocks of LiveKit applications.

## Overview

Rooms, participants, and tracks are the fundamental building blocks of every LiveKit app.

- A **room** is a virtual space where realtime communication happens.
- **Participants** are the users, agents, or services that join rooms to communicate.
- **Tracks** are the media streams—audio, video, or data—that participants publish and subscribe to within a room.

Together, these concepts form the foundation of LiveKit's realtime communication model. Understanding how they work together helps you build effective apps that handle multiple users, manage media streams, and coordinate realtime interactions.

## Core concepts

LiveKit's architecture is built around three core concepts that work together to enable realtime communication:

| Concept | Description | Key capabilities |
| **Rooms** | Virtual spaces where participants connect and communicate. Each room has a unique name and can be configured with settings like maximum participants and empty timeout. | Create, list, and delete rooms. |
| **Participants** | The entities that join rooms—users from frontend apps, AI agents, SIP callers, or any service that connects to LiveKit. Each participant has an identity and can publish and subscribe to tracks. | List, remove, and mute participants. |
| **Tracks** | Media streams that participants publish and subscribe to. LiveKit supports audio tracks, video tracks, and data tracks. Participants can publish multiple tracks simultaneously. | Publish camera, microphone, and screen share tracks. |

Use [webhooks and events](https://docs.livekit.io/intro/basics/rooms-participants-tracks/webhooks-events.md) to monitor and respond to changes in rooms, participants, and tracks.

## In this section

Learn how to manage rooms, participants, and tracks in your application:

- **[Room management](https://docs.livekit.io/intro/basics/rooms-participants-tracks/rooms.md)**: Create, list, and delete rooms from your backend server.

- **[Participant management](https://docs.livekit.io/intro/basics/rooms-participants-tracks/participants.md)**: List, remove, and mute participants from your backend server.

- **[Track management](https://docs.livekit.io/intro/basics/rooms-participants-tracks/tracks.md)**: Understand tracks and track publications in LiveKit applications.

- **[Webhooks & events](https://docs.livekit.io/intro/basics/rooms-participants-tracks/webhooks-events.md)**: Configure webhooks and handle events to monitor and respond to changes in rooms, participants, and tracks.

---

This document was rendered at 2025-12-31T18:29:31.771Z.
For the latest version of this document, see [https://docs.livekit.io/intro/basics/rooms-participants-tracks.md](https://docs.livekit.io/intro/basics/rooms-participants-tracks.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).