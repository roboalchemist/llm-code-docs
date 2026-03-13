# Apple Safari

There are two main implementations of the Safari browser: the Desktop edition which can be found in Mac OS workstations and laptops, and the iOS edition which comes installed as part of the iOS Operating System in mobile devices such as iPhone or iPad.

## Codec issues

Safari (both Desktop and iOS editions) included a half-baked implementation of the WebRTC standard, at the least with regards to the codecs compatibility. The WebRTC specs state that both VP8 and H.264 video codecs MUST be implemented in all WebRTC endpoints *, but Apple only added VP8 support starting from Safari Release 68 [https://developer.apple.com/safari/technology-preview/release-notes/#r68]. Older versions of the browser won’t be able to decode VP8 video, so if the source video isn’t already in H.264 format, Kurento Media Server will need to transcode the input video so they can be received by Safari.

*

RFC 7742, Section 5. Mandatory-to-Implement Video Codec [https://tools.ietf.org/html/rfc7742#section-5]:
| WebRTC Browsers MUST implement the VP8 video codec as described in **RFC 6386** [https://datatracker.ietf.org/doc/html/rfc6386.html]
| and H.264 Constrained Baseline as described in H264 [https://www.itu.int/rec/T-REC-H.264].
|
| WebRTC Non-Browsers that support transmitting and/or receiving video
| MUST implement the VP8 video codec as described in **RFC 6386** [https://datatracker.ietf.org/doc/html/rfc6386.html] and
| H.264 Constrained Baseline as described in H264 [https://www.itu.int/rec/T-REC-H.264].

In order to ensure compatibility with Safari browsers, also caring to not trigger on-the-fly transcoding between video codecs, it is important to make sure that Kurento has been configured with support for H.264, and it is also important to check that the SDP negotiations are actually choosing this as the preferred codec.

If you are targeting Safari version 68+, then this won’t pose any problem, as now both H.264 and VP8 can be used for WebRTC.

## HTML policies for video playback

Until recently, this has been the recommended way of inserting a video element in any HTML document:

```
<video id="myVideo" autoplay></video>

```