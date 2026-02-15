# Source: https://developers.cloudflare.com/realtime/realtimekit/core/waiting-room/index.md

---

title: Waiting Room · Cloudflare Realtime docs
description: The waiting room feature allows hosts to control who can join a
  meeting. When enabled, participants must wait for approval before entering the
  meeting.
lastUpdated: 2026-01-13T15:01:55.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/core/waiting-room/
  md: https://developers.cloudflare.com/realtime/realtimekit/core/waiting-room/index.md
---

Prerequisites

This page assumes you've already initialized the SDK and understand the meeting object structure. Refer to [Initialize SDK](https://developers.cloudflare.com/realtime/realtimekit/core/) and [Meeting Object Explained](https://developers.cloudflare.com/realtime/realtimekit/core/meeting-object-explained/) if needed.

The waiting room feature allows hosts to control who can join a meeting. When enabled, participants must wait for approval before entering the meeting.

## How the Waiting Room Works

After you call `meeting.join()`, one of two events will occur:

* **`roomJoined`** - You are allowed to join the meeting immediately
* **`waitlisted`** - You are placed in the waiting room and must wait for host approval

Use `meeting.self.roomState` to track the user's state in the meeting.

Note

The diagram below represents only waiting room-related states. The `roomState` property also transitions through other states like `'disconnected'`, `'left'`, `'kicked'`, and `'ended'`.

## Waiting Room States

### State Flow

```plaintext
        join()
          ↓
    [waitlisted]  ←------ (host rejects)
          ↓                     ↓
   (host accepts)           [rejected]
          ↓
      [joined]
```

## Listening to State Changes

### Joined Event

Triggered when the local user successfully joins the meeting.

### Waitlisted Event

Triggered when the local user is placed in the waiting room.

### Rejected Event

Triggered when the host rejects the entry request.

### Monitor State with roomState

You can also directly check the current room state.

## Host Actions

Hosts can manage waiting room requests using participant management methods. See [Remote Participants](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/) for details on:

* **`acceptWaitingRoomRequest(participantId)`** - Accept a participant from the waiting room
* **`rejectWaitingRoomRequest(participantId)`** - Reject a participant's entry request

### Example: Host Accepting Participants

## Best Practices

* **Provide Clear Feedback** - Show users when they're in the waiting room and that they're waiting for approval
* **Set Expectations** - Let users know their request is being reviewed
* **Handle Rejection Gracefully** - Provide a friendly message if entry is rejected
* **Monitor State Changes** - Subscribe to room state changes to update your UI accordingly
* **Check Permissions** - Ensure your app has appropriate permissions configured in the preset to use waiting room features
