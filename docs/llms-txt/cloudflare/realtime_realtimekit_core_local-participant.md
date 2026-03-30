# Source: https://developers.cloudflare.com/realtime/realtimekit/core/local-participant/index.md

---

title: Local Participant · Cloudflare Realtime docs
description: Manage local user media devices, control audio, video, and
  screenshare, and handle events in RealtimeKit meetings.
lastUpdated: 2026-01-13T15:01:55.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/core/local-participant/
  md: https://developers.cloudflare.com/realtime/realtimekit/core/local-participant/index.md
---

Manage local user media devices, control audio, video, and screenshare, and handle events in RealtimeKit meetings.

Prerequisites

Initialize the SDK and understand the meeting object structure. Refer to [Initialize SDK](https://developers.cloudflare.com/realtime/realtimekit/core/) and [Meeting Object Explained](https://developers.cloudflare.com/realtime/realtimekit/core/meeting-object-explained/).

## Introduction

The local user is accessible via `meeting.self` and contains all information and methods related to the current participant. This includes media controls, device management, participant metadata, and state information.

## Properties

### Metadata Properties

Access participant identifiers and display information:

### Media Properties

Access the local user's media tracks and states:

### State Properties

Access room state and participant status:

## Media Controls

### Audio control

Mute and unmute the microphone:

### Video control

Enable and disable the camera:

### Screen share control

Start and stop screen sharing:

### Change display name

Update the display name before joining the meeting:

## Manage media devices

### Get available devices

### Change device

Switch to a different media device:

## Display local video

## Screen share setup (iOS)

## Events

### Room joined

Fires when the local user joins the meeting:

### Room left

Fires when the local user leaves the meeting:

### Video update

Fires when video is enabled or disabled:

### Audio update

Fires when audio is enabled or disabled:

### Screen share update

Fires when screen sharing starts or stops:

### Device update

Fires when the active device changes:

### Device List Update

Triggered when the list of available devices changes (device plugged in or out):

### Network Quality Score

Monitor your own network quality:

### Permission Updates

Triggered when permissions are updated dynamically:

### Media Permission Errors

Triggered when media permissions are denied or media capture fails:

### Waitlist Status

For meetings with waiting room enabled:

### iOS-Specific Events

The iOS SDK provides additional platform-specific events:

## Pin and Unpin

Pin or unpin yourself in the meeting (requires appropriate permissions):

## Update Media Constraints

Update video or screenshare resolution at runtime:
