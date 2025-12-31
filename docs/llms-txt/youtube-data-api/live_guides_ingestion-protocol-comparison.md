# Source: https://developers.google.com/youtube/v3/live/guides/ingestion-protocol-comparison.md.txt

# YouTube Live Streaming Ingestion Protocol Comparison

YouTube Live Streaming supports the following ingestion protocols for
third-party clients:

|                               Ingestion Protocol                                | Encrypted | Video Codecs Supported |                                               Comment                                               |
|---------------------------------------------------------------------------------|-----------|------------------------|-----------------------------------------------------------------------------------------------------|
| RTMP                                                                            | No        | H.264                  | Suitable for normal, low, or ultra-low latency live streaming.                                      |
| [RTMPS](https://developers.google.com/youtube/v3/live/guides/rtmps-ingestion)   | Yes       | H.264                  | Suitable for normal, low, or ultra-low latency live streaming.                                      |
| [HLS](https://developers.google.com/youtube/v3/live/guides/hls-ingestion)       | Yes       | H.264, H.265 (HEVC)    | Better for 4K resolution because of HEVC support. Supports HDR. Not suitable for ultra-low latency. |
| [DASH](https://developers.google.com/youtube/v3/live/guides/encoding-with-dash) | Yes       | H.264, VP9             | Better for 4K resolution because of VP9 support. Not suitable for ultra-low latency.                |

*Real Time Messaging Protocol (RTMPS)* is a widely-used protocol for video
streaming that YouTube Live has accepted since the service began.

*Real Time Messaging Protocol Secure (RTMPS)* is a secure extension to RTMP.
RTMPS benefits both content creators and viewers by preventing man-in-the-middle
attacks on the ingestion side of livestreams. This ensures that all of a
creator's live streaming data---including video, audio, and control signals---is
securely transmitted to YouTube's servers, protecting it from tampering or
interception in transit.

The *HTTP Live Streaming (HLS)* and *Dynamic Adaptive Streaming over HTTP
(DASH)* ingestion protocols are also encrypted, like RTMPS. They also support
codecs that RTMP and RTMPS don't. Next-generation video codecs such as VP9 and
*High Efficiency Video Coding (HEVC)* can offer much better compression relative
to H.264, allowing users to either stream with higher quality for a given
bitrate or stream with the same quality while using a lower bitrate, which could
decrease buffering. This makes HLS or DASH ingestion a good choice for premium
content that requires higher quality and higher resolution, albeit at a
relatively higher latency. Note that HLS and DASH ingestion typically incur
greater latency than RTMP because HLS and DASH are segment-based.