# 6.11.0 (July 2019)

Kurento Media Server **6.11** has been released! This new version brings several improvements and fixes that have happened while we work on moving KMS to use the newer GStreamer 1.14 in Ubuntu Bionic.

To install it: Installation Guide.

## New SDP syntax for WebRTC DataChannels

Firefox moved to the newer SDP syntax for SCTP (WebRTC DataChannels), and soon enough Chrome will also do the same. It was just a matter of time until support for DataChannels was totally broken (and it already started to be with Firefox), so this was a much needed update in Kurento.

This article explains the change: How to avoid Data Channel breaking [https://blog.mozilla.org/webrtc/how-to-avoid-data-channel-breaking/].

Old style SDP syntax was like this:

```
m=application 54111 DTLS/SCTP 5000
a=sctpmap:5000 webrtc-datachannel 16

```