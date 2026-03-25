# 6.18.0 (September 2022)

One of the latest (if not the last) releases of the 6.x branch of Kurento; this one brings several deprecations that pave the way for introduction of the upcoming Kurento 7.0.

To install Kurento Media Server: Installation Guide.

Table of Contents

- 

6.18.0 (September 2022)

  - 

Added

    - 

FLV Recording Profile for RTMP

    - 

Explicit network interface for WebSocket

    - 

Differentiated Services Code Point (DSCP) for WebRTC QoS

  - 

Changed

    - 

WebRTC DTLS Quick Connection

  - 

Deprecated: OpenCV extra modules

  - 

Deprecated: Renamed API methods

    - 

timestamp -> timestampMillis

    - 

MediaObject and MediaElement

      - 

Media Events

      - 

childs -> children

      - 

setOutputBitrate -> minOutputBitrate, maxOutputBitrate

      - 

minOuputBitrate, maxOuputBitrate -> minOutputBitrate, maxOutputBitrate

    - 

WebRtcEndpoint

      - 

ICE Events

      - 

externalAddress -> externalIPv4, externalIPv6

    - 

IceCandidatePair

    - 

Stats

      - 

inputAudioLatency, inputVideoLatency -> inputLatency

      - 

audioE2ELatency, videoE2ELatency -> E2ELatency

  - 

Fixed

  - 

Other changes