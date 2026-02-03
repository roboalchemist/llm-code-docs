# Source: https://docs.livekit.io/transport/media/ingress-egress/egress/participant.md

LiveKit docs › Media › Stream export & import › Egress › Participant & TrackComposite egress

---

# Participant & TrackComposite egress

> Record participants individually with the egress API.

Some use cases require participants to be recorded individually instead of compositing them. LiveKit offers two options for recording participants individually. Both options support a wide range of [output options](https://docs.livekit.io/transport/media/ingress-egress/egress/outputs.md).

See the [Egress examples](https://docs.livekit.io/reference/other/egress/examples.md) page for example usage.

## Participant egress

Participant egress allows you to record a participant's audio and video tracks by providing the participant's identity. Participant egress is designed to simplify the workflow of recording participants in a realtime session, and handles the changes in track state, such as when a track is muted.

When a participant egress is requested, the Egress service joins the room and waits for the participant to join and publish tracks. Recording begins as soon as either audio or video tracks are published. The service automatically handles muted or unpublished tracks and stops recording when the participant leaves the room.

You can also record a participant's screen share along with the screen share's audio. To enable this, pass `screen_share=true` when starting the Egress. The Egress service identifies tracks based on their `source` setting.

## TrackComposite egress

TrackComposite combines an audio and video track together for output. It allows for more precise control than participant egress because it allows you to specify which tracks to record using track IDs.

A key difference between TrackComposite and participant egress is that tracks must be published _before_ starting the egress. As a result, there may be a slight delay between when the track is published and when recording begins.

## Examples

For examples on using participant or TrackComposite egress, please reference [Egress examples](https://docs.livekit.io/reference/other/egress/examples.md).

---

This document was rendered at 2026-02-03T03:25:17.309Z.
For the latest version of this document, see [https://docs.livekit.io/transport/media/ingress-egress/egress/participant.md](https://docs.livekit.io/transport/media/ingress-egress/egress/participant.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).