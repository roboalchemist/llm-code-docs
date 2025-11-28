# Source: https://developers.google.com/youtube/v3/live/guides/hls-ingestion.md.txt

# Delivering Live YouTube Content via HLS

This document explains how to use the HTTP Live Streaming (HLS) protocol to
stream live data on YouTube from an encoder. This document is intended for
encoder vendors who want to add HLS ingestion support to their products. HLS
ingestion is a good choice for premium content that requires high
quality and high resolution at a relatively higher latency. For a brief
comparison of different ingestion protocols that YouTube Live
Streaming supports, see [YouTube Live Streaming Ingestion Protocol Comparison](https://developers.google.com/youtube/v3/live/guides/ingestion-protocol-comparison).

To stream live data using HLS, the encoder should send a series of Media
Playlists and Media Segments to YouTube's HLS endpoint using `HTTP PUT` or
`POST` requests. From the encoder's perspective, the YouTube HLS endpoint
appears to be a passive HTTP server.

Each Media Segment represents the actual multimedia content for a brief portion
of the stream lasting between one and four seconds. Each Media Playlist
describes how to reassemble the Media Segments in correct stream order.

## Media Format Requirements

YouTube HLS ingestion has the following requirements for video and audio
content:

- Video and audio must be muxed in M2TS format.
- Supported video codecs are H.264 and HEVC.
- Frame rates up to 60fps are supported.
- Only closed GOP is supported.
- The supported audio codec is AAC, and only single-track audio is supported.

See more detailed requirements on [Media Segments](https://developers.google.com/youtube/v3/live/guides/hls-ingestion#media_segments) section.

### HDR

High Dynamic Range (HDR) video is supported using the HEVC codec and has the
following additional requirements:

- Supported color standards are 10-bit PQ and HLG with non-constant luminance. More specifically:
  - Chroma format must be YUV 4:2:0 10-bit.
  - Transfer function must be PQ (also known as SMPTE ST 2084) or HLG (also known as ARIB STD-B67).
  - Color primaries must be Rec. 2020.
  - Matrix coefficients must be Rec. 2020 non-constant luminance.
- Both limited-range (or MPEG-range) and full-range (or JPEG-range) sample values are supported. It is important that the range is set according to the sample value range that the content uses. Limited-range sample values are recommended.

## Obtaining an HLS Ingestion URL

### Obtaining an HLS Ingestion URL from the YouTube API

To obtain the full ingestion URL, encoders can use the [YouTube Live Streaming
API](https://developers.google.com/youtube/v3/live/getting-started) to [insert a liveStream
resource](https://developers.google.com/youtube/v3/live/docs/liveStreams/insert) with the following
properties:  

    "cdn": {
      "ingestionType": "hls",
      "frameRate": "variable",
      "resolution": "variable"
    }

In the API response, the `cdn.ingestionInfo.ingestionAddress` field specifies
the primary ingestion URL, and `cdn.ingestionInfo.backupIngestionAddress` field
specifies the backup ingestion URL. For more details, see the documentation for
the [`liveStreams` resource](https://developers.google.com/youtube/v3/live/docs/liveStreams).

### Obtaining an HLS Ingestion URL from YouTube Creator Studio

| **Caution:** This method of obtaining HLS ingestion URLs is a beta feature and may change in the future.

In the [YouTube Creator Studio web interface](https://www.youtube.com/livestreaming), after the creator clicks "Create
Stream", YouTube displays a "Stream Key" consisting of alphanumeric
characters and hyphens. This secret key identifies both the creator and the
stream to YouTube.

You can construct an HLS URL from this stream key, as follows:  

    https://a.upload.youtube.com/http_upload_hls?cid=<var label="stream key" translate="no">$</var>STREAM_KEY&copy=0&file=

... where <var translate="no">$STREAM_KEY</var> is the Stream Key displayed in the
web interface.
For example:
`https://a.upload.youtube.com/http_upload_hls?cid=abcd-efgh-ijkl-mnop-qrst&copy=0&file=`

For added reliability, you can transmit a redundant second copy of the ingestion
to this backup URL:  

    https://b.upload.youtube.com/http_upload_hls?cid=<var label="stream key" translate="no">$</var>STREAM_KEY&copy=1&file=

Note the backup has two differences from the primary URL: both the hostname
and the `copy=` parameter have changed. The backup ingestion **must** send
a different `copy=` parameter value than the primary ingestion to avoid
corrupting the stream.

## Completing the HLS Ingestion URL

URLs obtained using either methods are incomplete templates; each ends
with an empty `file=` query parameter. To form the final URL, the encoder must
append the filename of a Media Playlist or Media Segment to the end of the URL,
thus completing the `file=` parameter.

The following rules apply to the `file=` parameter's value:

- The encoder may construct a Media Playlist or Media Segment filename from alphanumeric characters, underscores, forward slashes, hyphens, and periods; no other characters are supported.
- The encoder must not URL-encode the filename.
- The encoder may include relative or absolute path components in filenames, though this is never required. If the encoder includes a path component within a Media Segment filename, it must reference the same path in the corresponding playlist entry.

## HLS Protocol Requirements

The Media Playlists and the Media Segments sent by the encoder must conform to
the [HTTP Live Streaming 2nd Edition
Specification](https://tools.ietf.org/html/draft-pantos-hls-rfc8216bis).

The HLS specification defines two types of playlist: Media Playlist and Master
Playlist. Since YouTube transcodes streamed content to different resolutions and
bitrates, the encoder does not need to send content with different bitrates to
YouTube. As a result, YouTube supports only Media Playlists for HLS ingestion,
and Master Playlists are ignored. (A Master Playlist provides a set of Variant
Streams, each of which describes a different version of the same content.)

The encoder must:

- send exactly one encoded stream with the highest resolution that you want to serve to users (single resolution and codec).
- mux audio and video.
- use HTTPS and a persistent connection for all requests.

The following sections contain more specific requirements for Media Playlists
and Media Segments.

### Media Playlists

A Media Playlist contains a list of Media Segments that can be concatenated to
represent a continuous, decodable multimedia stream. The Media Playlist tells
the server which Media Segments to expect and how to order them properly in the
reassembled stream.

#### Requirements

- The Media Playlist file name must end with either `.m3u8` or `.m3u`.

- The first Media Playlist sent for a stream must start at sequence number
  **`0`** and the sequence number must increase monotonically.

- The `EXT-X-MEDIA-SEQUENCE` tag must identify the sequence number of the
  first Media Segment listed in the playlist.

- A Media Playlist must not contain more than five outstanding segments. A
  segment is outstanding if the server has not received it or acknowledged
  receipt of it.

  In addition to the outstanding segments, also include a few acknowledged
  segments in each Media Playlist. This practice makes it less likely for a
  segment to be skipped if a Media Playlist is lost on the server side. For
  example, you could include up to two acknowledged segments and up to five
  outstanding segments in each Media Playlist.

  Note that the server acknowledges receipt of a Media Segment by returning a
  `200` (`OK`) or `202` (`Accepted`) response on the upload of that segment. A
  `202` response indicates that the server received the segment before a
  playlist identifying that segment.
- Send an updated Media Playlist for **every** Media Segment so that the
  server can recover quickly if a Media Playlist is lost.

- As the server acknowledges receipt of Media Segments, you can increment the
  `EXT-X-MEDIA-SEQUENCE` tag value to prevent the Media Playlist from becoming
  too long. For example, if the server has already acknowledged receipt of the
  first nine Media Segments, the next Media Playlist might list the eighth,
  ninth, and tenth Media Segments.

- `EXT-X-KEY` and `EXT-X-SESSION-KEY` tags are not supported.

#### Examples

The following list shows an example of the files that the encoder is expected to
send:  

    Media Playlist file with seqnum #0
    Media Segment file #0
    Media Playlist file with seqnum #0-#1
    Media Segment file #1
    Media Playlist file with seqnum #0-#2
    Media Segment file #2
    Media Playlist file with seqnum #1-#3
    Media Segment file #3
    ...

The following example shows a Media Playlist sent in the middle of a live video
stream. Since the example is from the middle of a stream, the
`EXT-X-MEDIA-SEQUENCE` tag has a nonzero value.  

    #EXTM3U
    #EXT-X-VERSION:3
    #EXT-X-TARGETDURATION:4
    #EXT-X-MEDIA-SEQUENCE:2680

    #EXTINF:3.975,
    fileSequence2680.ts
    #EXTINF:3.941,
    fileSequence2681.ts
    #EXTINF:3.975,
    fileSequence2682.ts

### Media Segments

The following list identifies requirements for Media Segments:

- **Filenames**
  - Media Segment file names in the URL must have the `.ts` filename extension and must match the filenames in the playlist.
  - Media Segment file names must be unique across encoder reboots and stream restarts.
- **Format**
  - Media Segments must be in M2TS format and should be self-initializing.
  - Each M2TS Segment must contain a single MPEG-2 Program.
  - The M2TS Segment must contain a PAT and a PMT, and the first two Transport Stream packets in a Segment should be a PAT and a PMT.
- **Content**
  - Video and audio must be muxed.
  - Supported video codecs are H.264 and HEVC.
  - HDR with HEVC is supported (see [HDR requirements](https://developers.google.com/youtube/v3/live/guides/hls-ingestion#hdr)).
  - Frame rates up to 60fps are supported.
  - Only closed GOP is supported.
  - The supported audio codec is AAC, and only single-track audio is supported.
  - Media Segments are recommended to have a duration between one and four seconds, as discussed in the following section. Media Segments must not have a duration longer than 5 seconds.
  - Media segments must only be encrypted in the TLS/SSL layer with HTTPS. Other encryption mechanisms are not supported.

#### Media Segment duration

We expect HLS ingestion to be used for premium content that requires high
quality and high resolution. HLS ingestion usually has higher latency than RTMP-
and WebRTC-based ingestions because HLS ingestion is segment-based.

We recommend a Media Segment duration of one to four seconds because having
smaller Media Segments can result in lower latency, albeit at a cost of a higher
rebuffer rate and lower encoding efficiency. As noted in the previous section,
Media Segments must not be longer than 5 seconds.

#### Bitrates

The [YouTube Help
Center](https://support.google.com/youtube/answer/2853702?ref_topic=6136989)
provides guidelines for bitrate settings.

Note that HEVC generally yields 25% to 50% more data compression at the same
video quality compared to H.264. As such, bitrate values in the lower end of the
suggested ranges can be used with HEVC to save bandwidth, which is especially
useful for 4K content.

### Other Requirements

- Encoders should set the `User-Agent` header in the HTTP request using the
  following syntax, which includes the manufacturer's name, model name, and
  version:

      User-Agent: <manufacturer> / <model> / <version>

  | **Note:** This information will only be used for debugging purposes. It won't be used for functional decisions in stream handling.

## Closed captions

HLS ingestion supports two options for sending closed captions:

- Send closed captions using separate HTTP POST requests. This works for all HLS ingestions.
- Embedded 608/708 closed captions work with HLS ingestions that use the H264 video codec but not with ingestions that use the HEVC video codec. For more details, see the [Live Caption Requirements](https://support.google.com/youtube/answer/3068031) in YouTube Help Center.

## HTTP response codes

The following sections explain the response codes that YouTube returns in
response to Media Segments and Media Playlists delivered using HLS.

200 (OK)

:   In response to a PUT or POST request, an HTTP 200 (OK) response indicates
    that the YouTube server received an expected operation and handled it
    successfully.

    In response to a DELETE request, an HTTP 200 (OK) response indicates that
    the YouTube server received and ignored the request. The YouTube server does
    not require the client to DELETE any resource in the stream, and it ignores
    DELETE requests. For performance reasons, YouTube recommends clients
    don't send DELETEs.

202 (Accepted)

:   An HTTP 202 (Accepted) response indicates that the YouTube server received the
    Media Segment before receiving a Media Playlist containing that Media Segment.
    This indicates to the client that it should send the Media Playlist containing
    that Media Segment as soon as possible to prevent a delay in processing that
    segment. Note that this won't be an issue if the encoder sends an updated
    Media Playlist for every Media Segment.

400 (Bad Request)

:   An HTTP 400 (Bad Request) response indicates one of the following problems
    occurred:

    - The URL is malformed
    - The Playlist cannot be parsed or contains unsupported tags

401 (Unauthorized)

:   An HTTP 401 (Unauthorized) response indicates that the cid parameter in the
    base URL for the YouTube HLS endpoint is corrupted or expired. The client
    should update the `cid` parameter in order to proceed.

405 (Method Not Allowed)

:   An HTTP 405 (Method Not Allowed) response indicates that the request was
    not a POST, PUT, or DELETE request.

500 (Internal Server Error)

:   An HTTP 500 (Internal Server Error) response indicates that the server was
    unable to process the request. For this error, we recommend that you retry the
    request with [exponential
    backoff](https://developers.google.com/youtube/v3/live/guides/encoding-with-dash#retries-and-exponential-backoff).