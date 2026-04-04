# Source: https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/events/index.md

---

title: Events · Cloudflare Realtime docs
description: This page provides an overview of the events emitted by
  meeting.participants and related participant maps, which you can use to keep
  your UI in sync with changes such as participants joining or leaving, pinning
  updates, active speaker changes, and grid view mode or page changes.
lastUpdated: 2026-01-20T03:13:13.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/events/
  md: https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/events/index.md
---

This page provides an overview of the events emitted by `meeting.participants` and related participant maps, which you can use to keep your UI in sync with changes such as participants joining or leaving, pinning updates, active speaker changes, and grid view mode or page changes.

Prerequisites

This page assumes you have already initialized the SDK and understand the meeting object structure. Refer to [Initialize SDK](https://developers.cloudflare.com/realtime/realtimekit/core/) and [Meeting Object Explained](https://developers.cloudflare.com/realtime/realtimekit/core/meeting-object-explained/) if needed.

## Grid events

These events allow you to monitor changes to the grid.

### View mode change

### Page change

### Active speaker

Triggered when a participant starts speaking.

## Participant map events

These events allow you to monitor changes to remote participant maps. Use them to get notified when a participant joins or leaves the meeting, is pinned, or moves out of the grid.

### Participant joined

Triggered when any participant joins the meeting.

### Participant left

Triggered when any participant leaves the meeting.

### Active participants changed

### Participant pinned

Triggered when a participant is pinned.

### Participant unpinned

Triggered when a participant is unpinned.

## Participant events

You can monitor changes to a specific participant using the following events.

### Video update

Triggered when any participant starts or stops video.

### Audio update

Triggered when any participant starts or stops audio.

### Screen share update

Triggered when any participant starts or stops screen share.

### Network quality score

## Listen to participant events
