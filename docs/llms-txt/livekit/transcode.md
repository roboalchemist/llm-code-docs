# Source: https://docs.livekit.io/transport/media/ingress-egress/ingress/transcode.md

LiveKit docs › Media › Stream export & import › Ingress › Transcoding configuration

---

# Transcoding configuration

> Configure video and audio encoding settings for LiveKit Ingress, including presets and custom encoding options.

## Overview

The Ingress service can transcode the media being received. This is the only supported behavior for RTMP and URL inputs. WHIP ingresses are not transcoded by default, but transcoding can be enabled by setting the `enable_transcoding` parameter. When transcoding is enabled, the default settings enable [video simulcast](https://blog.livekit.io/an-introduction-to-webrtc-simulcast-6c5f1f6402eb/) to ensure media can be consumed by all viewers, and should be suitable for most use cases.

In some situations however, you may want to adjust these settings to match source content or the viewer conditions better. For this purpose, LiveKit Ingress defines several presets, both for audio and video. Presets define both the characteristics of the media (codec, dimensions, framerate, channel count, sample rate) and the bitrate. For video, a single preset defines the full set of simulcast layers.

## Using video presets

A preset can be chosen at Ingress creation time from the [constants in the Ingress protocol definition](https://github.com/livekit/protocol/blob/main/protobufs/livekit_ingress.proto):

**LiveKit CLI**:

Create a file at `ingress.json` with the following content:

```json
{
    "name": "Name of the egress goes here",
    "room_name": "Name of the room to connect to",
    "participant_identity": "Unique identity for the room participant the Ingress service will connect as",
    "participant_name": "Name displayed in the room for the participant"
    "video": {
        "name": "track name",
        "source": "SCREEN_SHARE",
        "preset": "Video preset enum value"
    },
    "audio": {
        "name": "track name",
        "source": "SCREEN_SHARE_AUDIO",
        "preset": "Audio preset enum value"
    }
}

```

Then create the ingress using `lk`:

```shell
lk ingress create ingress.json

```

---

**JavaScript**:

```ts
const ingress: CreateIngressOptions = {
  name: 'my-ingress',
  roomName: 'my-room',
  participantIdentity: 'my-participant',
  participantName: 'My Participant',
  video: new IngressVideoOptions({
    source: TrackSource.SCREEN_SHARE,
    encodingOptions: {
      case: 'preset',
      value: IngressVideoEncodingPreset.H264_1080P_30FPS_3_LAYERS,
    },
  }),
  audio: new IngressAudioOptions({
    source: TrackSource.SCREEN_SHARE_AUDIO,
    encodingOptions: {
      case: 'preset',
      value: IngressAudioEncodingPreset.OPUS_MONO_64KBS,
    },
  }),
};

await ingressClient.createIngress(IngressInput.RTMP_INPUT, ingress);

```

---

**Go**:

```go
ingressRequest := &livekit.CreateIngressRequest{
    Name:                "my-ingress",
    RoomName:            "my-room",
    ParticipantIdentity: "my-participant",
    ParticipantName:     "My Participant",
    Video: &livekit.IngressVideoOptions{
        EncodingOptions: &livekit.IngressVideoOptions_Preset{
            Preset: livekit.IngressVideoEncodingPreset_H264_1080P_30FPS_3_LAYERS,
        },
    },
    Audio: &livekit.IngressAudioOptions{
        EncodingOptions: &livekit.IngressAudioOptions_Preset{
            Preset: livekit.IngressAudioEncodingPreset_OPUS_MONO_64KBS,
        },
    },
}

info, err := ingressClient.CreateIngress(ctx, ingressRequest)
ingressID := info.IngressId

```

---

**Ruby**:

```ruby
video_options = LiveKit::Proto::IngressVideoOptions.new(
  name: "track name",
  source: :SCREEN_SHARE,
  preset: :H264_1080P_30FPS_3_LAYERS
)
audio_options = LiveKit::Proto::IngressAudioOptions.new(
  name: "track name",
  source: :SCREEN_SHARE_AUDIO,
  preset: :OPUS_STEREO_96KBPS
)
info = ingressClient.create_ingress(:RTMP_INPUT,
  name: 'dz-test',
  room_name: 'davids-room',
  participant_identity: 'ingress',
  video: video_options,
  audio: audio_options,
)
puts info.ingress_id

```

## Custom settings

For specialized use cases, it is also possible to specify fully custom encoding parameters. In this case, all video layers need to be defined if simulcast is desired.

**LiveKit CLI**:

Create a file at `ingress.json` with the following content:

```json
{
  "name": "Name of the egress goes here",
  "room_name": "Name of the room to connect to",
  "participant_identity": "Unique identity for the room participant the Ingress service will connect as",
  "participant_name": "Name displayed in the room for the participant",
  "video": {
    "options": {
"video_codec": "video codec ID from the [VideoCodec enum](https://github.com/livekit/protocol/blob/main/protobufs/livekit_models.proto)",
      "frame_rate": "desired framerate in frame per second",
      "layers": [
        {
          "quality": "ID for one of the LOW, MEDIUM or HIGH VideoQualitu definitions",
          "witdh": "width of the layer in pixels",
          "height": "height of the layer in pixels",
          "bitrate": "video bitrate for the layer in bit per second"
        }
      ]
    }
  },
  "audio": {
    "options": {
"audio_codec": "audio codec ID from the [AudioCodec enum](https://github.com/livekit/protocol/blob/main/protobufs/livekit_models.proto)",
      "bitrate": "audio bitrate for the layer in bit per second",
      "channels": "audio channel count, 1 for mono, 2 for stereo",
      "disable_dtx": "wether to disable the [DTX feature](https://www.rfc-editor.org/rfc/rfc6716#section-2.1.9) for the OPUS codec"
    }
  }
}

```

Then create the ingress using `lk`:

```shell
lk ingress create ingress.json

```

---

**JavaScript**:

```ts
const ingress: CreateIngressOptions = {
  name: 'my-ingress',
  roomName: 'my-room',
  participantIdentity: 'my-participant',
  participantName: 'My Participant',
  enableTranscoding: true,
  video: new IngressVideoOptions({
    name: 'my-video',
    source: TrackSource.CAMERA,
    encodingOptions: {
      case: 'options',
      value: new IngressVideoEncodingOptions({
        videoCodec: VideoCodec.H264_BASELINE,
        frameRate: 30,
        layers: [
          {
            quality: VideoQuality.HIGH,
            width: 1920,
            height: 1080,
            bitrate: 4500000,
          },
        ],
      }),
    },
  }),
  audio: new IngressAudioOptions({
    name: 'my-audio',
    source: TrackSource.MICROPHONE,
    encodingOptions: {
      case: 'options',
      value: new IngressAudioEncodingOptions({
        audioCodec: AudioCodec.OPUS,
        bitrate: 64000,
        channels: 1,
      }),
    },
  }),
};

await ingressClient.createIngress(IngressInput.RTMP_INPUT, ingress);

```

---

**Go**:

```go
ingressRequest := &livekit.CreateIngressRequest{
    Name:                "my-ingress",
    RoomName:            "my-room:",
    ParticipantIdentity: "my-participant",
    ParticipantName:     "My Participant",
    Video: &livekit.IngressVideoOptions{
        EncodingOptions: &livekit.IngressVideoOptions_Options{
            Options: &livekit.IngressVideoEncodingOptions{
                VideoCodec: livekit.VideoCodec_H264_BASELINE,
                FrameRate:  30,
                Layers: []*livekit.VideoLayer{
                    &livekit.VideoLayer{
                        Quality: livekit.VideoQuality_HIGH,
                        Width:   1920,
                        Height:  1080,
                        Bitrate: 4_500_000,
                    },
                },
            },
        },
    },
    Audio: &livekit.IngressAudioOptions{
        EncodingOptions: &livekit.IngressAudioOptions_Options{
            Options: &livekit.IngressAudioEncodingOptions{
                AudioCodec: livekit.AudioCodec_OPUS,
                Bitrate:    64_000,
                Channels:   1,
            },
        },
    },
}

info, err := ingressClient.CreateIngress(ctx, ingressRequest)
ingressID := info.IngressId


```

---

**Ruby**:

```ruby
video_encoding_opts = LiveKit::Proto::IngressVideoEncodingOptions.new(
  frame_rate: 30,
)
# add layers as array
video_encoding_opts.layers += [
  LiveKit::Proto::VideoLayer.new(
    quality: :HIGH,
    width: 1920,
    height: 1080,
    bitrate: 4_500_000,
  )
]
video_options = LiveKit::Proto::IngressVideoOptions.new(
  name: "track name",
  source: :SCREEN_SHARE,
  options: video_encoding_opts,
)
audio_options = LiveKit::Proto::IngressAudioOptions.new(
  name: "track name",
  source: :SCREEN_SHARE_AUDIO,
  options: LiveKit::Proto::IngressAudioEncodingOptions.new(
    bitrate: 64000,
    disable_dtx: true,
    channels: 1,
  )
)
info = ingressClient.create_ingress(:RTMP_INPUT,
  name: 'dz-test',
  room_name: 'davids-room',
  participant_identity: 'ingress',
  video: video_options,
  audio: audio_options,
)
puts info.ingress_id

```

## Enabling transcoding for WHIP sessions

By default, WHIP ingress sessions forward incoming audio and video media unmodified from the source to LiveKit clients. This behavior allows the lowest possible end to end latency between the media source and the viewers. This however requires the source encoder to be configured with settings that are compatible with all the subscribers, and ensure the right trade offs between quality and reach for clients with variable connection quality. This is best achieved when the source encoder is configured with simulcast enabled.

If the source encoder cannot be setup easily to achieve such tradeoffs, or if the available uplink bandwidth is insufficient to send all required simulcast layers, WHIP ingresses can be configured to transcode the source media similarly to other source types. This is done by setting the `enable_transcoding` option on the ingress. The encoder settings can then be configured in the `audio` and `video` settings in the same manner as for other inputs types.

**LiveKit CLI**:

Create a file at `ingress.json` with the following content:

```json
{
    "input_type": 1 (WHIP only)
    "name": "Name of the egress goes here",
    "room_name": "Name of the room to connect to",
    "participant_identity": "Unique identity for the room participant the Ingress service will connect as",
    "participant_name": "Name displayed in the room for the participant",
    "enable_transcoding": true
    "video": {
        "name": "track name",
        "source": "SCREEN_SHARE",
        "preset": "Video preset enum value"
    },
    "audio": {
        "name": "track name",
        "source": "SCREEN_SHARE_AUDIO",
        "preset": "Audio preset enum value"
    }
}

```

Then create the Ingress using `lk`:

```shell
lk ingress create ingress.json

```

---

**JavaScript**:

```ts
const ingress: CreateIngressOptions = {
  name: 'my-ingress',
  roomName: 'my-room',
  participantIdentity: 'my-participant',
  participantName: 'My Participant',
  enableTranscoding: true,
  video: new IngressVideoOptions({
    source: TrackSource.SCREEN_SHARE,
    encodingOptions: {
      case: 'options',
      value: new IngressVideoEncodingOptions({
        videoCodec: VideoCodec.H264_BASELINE,
        frameRate: 30,
        layers: [
          {
            quality: VideoQuality.HIGH,
            width: 1920,
            height: 1080,
            bitrate: 4500000,
          },
        ],
      }),
    },
  }),
  audio: new IngressAudioOptions({
    source: TrackSource.MICROPHONE,
    encodingOptions: {
      case: 'options',
      value: new IngressAudioEncodingOptions({
        audioCodec: AudioCodec.OPUS,
        bitrate: 64000,
        channels: 1,
      }),
    },
  }),
};

await ingressClient.createIngress(IngressInput.WHIP_INPUT, ingress);

```

---

**Go**:

```go
t := true

ingressRequest := &livekit.CreateIngressRequest{
    InputType:           livekit.IngressInput_WHIP_INPUT
    Name:                "my-ingress",
    RoomName:            "my-room:",
    ParticipantIdentity: "my-participant",
    ParticipantName:     "My Participant",
    EnableTranscoding:   &t,
    Video: &livekit.IngressVideoOptions{
        EncodingOptions: &livekit.IngressVideoOptions_Options{
            Options: &livekit.IngressVideoEncodingOptions{
                VideoCodec: livekit.VideoCodec_H264_BASELINE,
                FrameRate:  30,
                Layers: []*livekit.VideoLayer{
                    &livekit.VideoLayer{
                        Quality: livekit.VideoQuality_HIGH,
                        Width:   1920,
                        Height:  1080,
                        Bitrate: 4_500_000,
                    },
                },
            },
        },
    },
    Audio: &livekit.IngressAudioOptions{
        EncodingOptions: &livekit.IngressAudioOptions_Options{
            Options: &livekit.IngressAudioEncodingOptions{
                AudioCodec: livekit.AudioCodec_OPUS,
                Bitrate:    64_000,
                Channels:   1,
            },
        },
    },
}

info, err := ingressClient.CreateIngress(ctx, ingressRequest)
ingressID := info.IngressId


```

---

**Ruby**:

```ruby
video_encoding_opts = LiveKit::Proto::IngressVideoEncodingOptions.new(
  frame_rate: 30,
)
# add layers as array
video_encoding_opts.layers += [
  LiveKit::Proto::VideoLayer.new(
    quality: :HIGH,
    width: 1920,
    height: 1080,
    bitrate: 4_500_000,
  )
]
video_options = LiveKit::Proto::IngressVideoOptions.new(
  name: "track name",
  source: :SCREEN_SHARE,
  options: video_encoding_opts,
)
audio_options = LiveKit::Proto::IngressAudioOptions.new(
  name: "track name",
  source: :SCREEN_SHARE_AUDIO,
  options: LiveKit::Proto::IngressAudioEncodingOptions.new(
    bitrate: 64000,
    disable_dtx: true,
    channels: 1,
  )
)

info = ingressClient.create_ingress(:WHIP_INPUT,
  name: 'dz-test',
  room_name: 'davids-room',
  participant_identity: 'ingress',
  enable_transcoding: true,
  video: video_options,
  audio: audio_options,
)
puts info.ingress_id

```

---

This document was rendered at 2025-12-31T18:29:37.812Z.
For the latest version of this document, see [https://docs.livekit.io/transport/media/ingress-egress/ingress/transcode.md](https://docs.livekit.io/transport/media/ingress-egress/ingress/transcode.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).