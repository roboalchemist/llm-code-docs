# Source: https://docs.livekit.io/transport/data/state/room-metadata.md

LiveKit docs › Data › State synchronization › Room metadata

---

# Room metadata

> Share application-specific state with all participants.

## Overview

Similar to [Participant metadata](https://docs.livekit.io/transport/data/state/participant-attributes.md), Rooms also feature a metadata field for application-specific data which is visible to all participants.

Room metadata can only be set using the server APIs, but can be accessed by all participants in the room using the LiveKit SDKs.

To set room metadata, use the [CreateRoom](https://docs.livekit.io/intro/basics/rooms-participants-tracks/rooms.md#create-a-room) and [UpdateRoomMetadata](https://docs.livekit.io/reference/other/roomservice-api.md#updateroommetadata) APIs.

To subscribe to updates, you must [handle](https://docs.livekit.io/intro/basics/rooms-participants-tracks/webhooks-events.md#sdk-events) the `RoomMetadataChanged` event.

### Size limits

Room metadata is limited to 64 KiB.

---

This document was rendered at 2026-02-03T03:25:19.664Z.
For the latest version of this document, see [https://docs.livekit.io/transport/data/state/room-metadata.md](https://docs.livekit.io/transport/data/state/room-metadata.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).