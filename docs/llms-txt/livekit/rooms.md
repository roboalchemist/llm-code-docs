# Source: https://docs.livekit.io/intro/basics/rooms-participants-tracks/rooms.md

LiveKit docs › Understanding LiveKit › Rooms, participants, & tracks › Room management

---

# Room management

> Create, list, and delete Rooms from your backend server.

## Overview

A `Room` is a container object representing a LiveKit session. An app, for example an AI agent, a web client, or a mobile app, etc., connects to LiveKit via a room. Any number of participants can join a room and publish audio, video, or data to the room.

Each participant in a room receives updates about changes to other participants in the same room. For example, when a participant adds, removes, or modifies the state (for example, mute) of a track, other participants are notified of this change. This is a powerful mechanism for synchronizing state and fundamental to building any realtime experience.

A room can be created manually via [server API](https://docs.livekit.io/intro/basics/rooms-participants-tracks/rooms.md#create-a-room), or automatically, when the first participant joins it. Once the last participant leaves a room, it closes after a short delay.

## Initialize RoomServiceClient

Room management is done with a RoomServiceClient, created like so:

**Go**:

```go
import (
  lksdk "github.com/livekit/server-sdk-go"
  livekit "github.com/livekit/protocol/livekit"
)

// ...

host := "https://my.livekit.host"
roomClient := lksdk.NewRoomServiceClient(host, "api-key", "secret-key")

```

---

**Python**:

```shell
uv add livekit-api

```

```python
from livekit.api import LiveKitAPI

# Will read LIVEKIT_URL, LIVEKIT_API_KEY, and LIVEKIT_API_SECRET from environment variables
async with api.LiveKitAPI() as lkapi:
  # ... use your client with `lkapi.room` ...

```

---

**Node.js**:

```js
import { Room, RoomServiceClient } from 'livekit-server-sdk';

const livekitHost = 'https://my.livekit.host';
const roomService = new RoomServiceClient(livekitHost, 'api-key', 'secret-key');

```

## Create a room

**Go**:

```go
room, _ := roomClient.CreateRoom(context.Background(), &livekit.CreateRoomRequest{
  Name:            "myroom",
  EmptyTimeout:    10 * 60, // 10 minutes
  MaxParticipants: 20,
})

```

---

**Python**:

```python
from livekit.api import CreateRoomRequest

room = await lkapi.room.create_room(CreateRoomRequest(
  name="myroom",
  empty_timeout=10 * 60,
  max_participants=20,
))

```

---

**Node.js**:

```js
const opts = {
  name: 'myroom',
  emptyTimeout: 10 * 60, // 10 minutes
  maxParticipants: 20,
};
roomService.createRoom(opts).then((room: Room) => {
  console.log('room created', room);
});

```

---

**LiveKit CLI**:

```shell
lk room create --empty-timeout 600 myroom

```

## List rooms

**Go**:

```go
rooms, _ := roomClient.ListRooms(context.Background(), &livekit.ListRoomsRequest{})

```

---

**Python**:

```python
from livekit.api import ListRoomsRequest

rooms = await lkapi.room.list_rooms(ListRoomsRequest())

```

---

**Node.js**:

```js
roomService.listRooms().then((rooms: Room[]) => {
  console.log('existing rooms', rooms);
});

```

---

**LiveKit CLI**:

```shell
lk room list

```

## Delete a room

Deleting a room causes all Participants to be disconnected.

**Go**:

```go
_, _ = roomClient.DeleteRoom(context.Background(), &livekit.DeleteRoomRequest{
  Room: "myroom",
})

```

---

**Python**:

```python
from livekit.api import DeleteRoomRequest

await lkapi.room.delete_room(DeleteRoomRequest(
  room="myroom",
))

```

---

**Node.js**:

```js
// Delete a room
roomService.deleteRoom('myroom').then(() => {
  console.log('room deleted');
});

```

---

**LiveKit CLI**:

```shell
lk room delete myroom

```

---

This document was rendered at 2026-02-03T03:24:52.667Z.
For the latest version of this document, see [https://docs.livekit.io/intro/basics/rooms-participants-tracks/rooms.md](https://docs.livekit.io/intro/basics/rooms-participants-tracks/rooms.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).