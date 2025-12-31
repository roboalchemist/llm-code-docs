# Source: https://developers.google.com/youtube/v3/live/guides/encoding-with-dash.md.txt

# Delivering Live YouTube Content via DASH

This document provides guidelines for using the Dynamic Adaptive Streaming over HTTP (DASH) Delivery format to stream live data on YouTube from an encoder. It is intended to help encoder vendors add DASH delivery support to their products.

## Understanding DASH

The list below lists some key DASH features and attributes:

- Based on open standards.
- HTTP-based. As a result, DASH is internet infrastructure friendly and can traverse firewalls.
- Supports high transfer bitrate. DASH supports multiple, simultaneous HTTP sessions and nonsequential segment delivery, providing greater resiliency than protocols that rely on a single TCP connection.
- Secure delivery through HTTPS.
- Lossless delivery through HTTP and HTTPS.
- Codec agnostic.
- Supports MP4 containing H264 and AAC as well as WebM containing VP8/VP9 and Vorbis/Opus.

### Specifications

- DASH is described in [ISO/IEC 23009-1:2014 Information technology -- Dynamic adaptive streaming over HTTP (DASH)](http://www.iso.org/iso/home/store/catalogue_tc/catalogue_detail.htm?csnumber=65274).
- WebM over DASH is described in the [WebM DASH specification](http://wiki.webmproject.org/adaptive-streaming/webm-dash-specification).

## Requirements

The following subsections explain requirements for using DASH to deliver live streams to YouTube.

### Timing

The YouTube DASH endpoint behaves as a passive HTTP server, recording PUT method calls sent by an encoder.

- The DASH endpoint supports simultaneous TCP connections. You can reuse connections as per HTTP/1.1.
- The MPD and Initialization segments should be PUT within 3 seconds of the first media segment. (We recommend that you [include the Initialization segment in the MPD](https://developers.google.com/youtube/v3/live/guides/encoding-with-dash#initialization-segments-in-mpd).)
- Each segment or MPD must use a separate PUT request; multi-part upload of multiple segments is not supported.
- PUT operations for media segments may overlap in time to improve upload bandwidth.
- Segments can be provided in nonsequential order within a time window of approximately 3 seconds.
- The MPD and Initialization segments should be updated at least every 60 seconds with an updated `availabilityStartTime` and `startNumber`. (As noted above, the Initialization segment can be [included in the MPD](https://developers.google.com/youtube/v3/live/guides/encoding-with-dash#initialization-segments-in-mpd). In that case, one PUT request can update both segments.)

### URL structure

Your encoder must form PUT URLs by appending a string to the YouTube endpoint base URL. You need to create the DASH ingestion endpoint by using the [YouTube Live Streaming API](https://developers.google.com/youtube/v3/live/getting-started).

The encoder can subsequently obtain the endpoint's base URL programmatically via the [YouTube Live Streaming API](https://developers.google.com/youtube/v3/live/getting-started). The base URL is also visible in the YouTube Live Events UI if you want to provide the URL to the encoder manually.

The string appended to the base URL can contain the following set of ASCII characters:

<br />

- Lowercase letters: a-z
- Uppercase letters: A-Z
- Digits: 0-9
- Special characters: _ (underscore), - (hyphen), . (period)

#### MPD URLs

In addition to the requirement above, the MPD URL must end with `.mpd`, enabling the YouTube server to easily identify the MPD. Other segment URLs must not end with `.mpd`.

#### Initialization and media segment URLs

The Initialization segment URL and all media segment URLs must end with `.mp4` if the data is in an ISO BMFF container or with `.webm` if the data is in a WebM container.

### MPD contents

The MPD must be complete and conformant with the DASH standard. It must contain exactly one of each of the following elements. This list identifies elements specifically required by YouTube, and the DASH standard might identify additional required elements. The elements are represented using XPath syntax and are consistent with the DASH standard.

- `/mpd:MPD/attribute::type`
- `/mpd:MPD/mpd:Period`
- `/mpd:MPD/mpd:Period/mpd:AdaptationSet`
- `/mpd:MPD/mpd:Period/mpd:AdaptationSet/attribute::mimeType (video/mp4 or video/webm)`
- `/mpd:MPD/mpd:Period/mpd:AdaptationSet/mpd:SegmentTemplate`
- `/mpd:MPD/mpd:Period/mpd:AdaptationSet/mpd:SegmentTemplate/attribute::media`
- `/mpd:MPD/mpd:Period/mpd:AdaptationSet/mpd:SegmentTemplate/attribute::initialization`
- `/mpd:MPD/mpd:Period/mpd:AdaptationSet/mpd:SegmentTemplate/attribute::startNumber`

Please note the following requirements for element values:

- The `<MPD>` element's `minimumUpdatePeriod` attribute must be set to a value equal to or less than 60 seconds (`PT60S`).
- The `<SegmentTemplate>` element's `media` attribute must specify that media segment URLs are generated using `$Number$`. (The `startNumber` attribute identifies the number that will be assigned to the first media segment.)

### Initialization segment length

The Initialization segment must not be longer than 100kb. (Typically, an Initialization segment is much smaller than that.) If the Initialization segment is included in the MPD, then the `data:` URL, which contains the segment, must not be longer than 100kb.

### Encoder output

The Initialization segment and media segments must constitute a multiplexed ISO BMFF or WebM file stream with closed GOPs (groups of pictures).

- The GOP size should be about 2 seconds and must be less than 8 seconds.
- The multiplexed stream must contain both audio and video tracks.

## Additional best practices

### Encryption

YouTube supports stream encryption via HTTPS. We strongly recommend that you use this feature.

### Initialization segments in MPD

You can represent the Initialization segment directly in the MPD using a `data:` URL, per [RFC 2397](https://www.ietf.org/rfc/rfc2397.txt). This simplifies your stream setup and reduces the possibility that the Initialization segment will not correspond to the rest of the stream.

The XPath for this element is:  

```
/mpd:MPD/mpd:Period/mpd:AdaptationSet/mpd:SegmentTemplate/attribute:data
```
| **Note:** The `data:` URL must not be longer than 100k bytes.

### Target segment durations

For good ingestion performance and a good trade-off between throughput and latency, the length of your media segments should be between 1 and 5 seconds. We strongly recommend that you communicate the target duration of those segments in the MPD using these two elements:

- `/mpd:MPD/mpd:Period/mpd:AdaptationSet/mpd:SegmentTemplate/attribute::duration`
- `/mpd:MPD/mpd:Period/mpd:AdaptationSet/mpd:SegmentTemplate/attribute::timescale`

The calculated duration from those attributes should be within a factor of 2 of all actual segment durations or streaming performance may suffer.

Note that the target duration for the ingestion does not equal the chunk duration for the live stream that YouTube produces. YouTube transcodes and re-chunks the input, and the output target duration depends on whether a stream is optimized for streaming quality or for latency.

### Retries and exponential backoff

All HTTP PUT requests should be performed with a timeout, which we recommend setting to a value 500 milliseconds greater than the segment duration.

A media segment PUT request that fails, whether due to timeout or other errors, corresponds to a gap in the video stream. As such, you should retry any such request using a randomized [binary exponential backoff](http://en.wikipedia.org/wiki/Exponential_backoff#Binary_exponential_backoff_.2F_truncated_exponential_backoff):

1. After a failure, wait a random period between `[0 ... 100]` milliseconds and retry the request.
2. If the request fails again, wait a random period between `[0 ... 200]` milliseconds and retry the request.
3. If the request fails again, wait a random period between `[0 ... 400]` milliseconds and retry the request.
4. etc.

Note that repeated failures should be signaled to the encoder operator since they correspond to a failing broadcast.

## HTTP Response codes

The following sections explain the response codes that YouTube returns in response to segments delivered via DASH.

#### 200 (OK)

An HTTP 200 (OK) response indicates that the YouTube server received an expected operation and handled it successfully.

#### 202 (Accepted)

An HTTP 202 (Accepted) response to any PUT or POST operation indicates that the operation was unexpected and accepted for deferred processing. However, the deferred operation could succeed or fail, so the response does not guarantee that YouTube will actually be able to successfully process the operation.

This response occurs most frequently when a segment is delivered non-sequentially. Usually, YouTube can correctly process the accepted segment after receiving the preceding segments, and you do not need to resend the segment.

For example, YouTube can return a 202 response in any of the following cases:

- An initialization segment is received before the MPD.
- Media segments are received before the MPD and Initialization segments.
- A media segment is received before an earlier segment, such as segment 3 being received before segment 2.

However, a 202 response can also indicate that the item identifier is incorrect if YouTube cannot fully validate the identifier upon receipt of the POST or PUT request. For example, one of the times that this occurs is when YouTube receives and accepts an initialization segment before receiving the MPD, but the initialization segment turns out to be invalid. In this case, YouTube accepts the initialization segment and returns a 202, then determines whether the segment is valid upon receipt of the MPD. You can avoid this particular scenario by [including the Initialization segment in the MPD](https://developers.google.com/youtube/v3/live/guides/encoding-with-dash#initialization-segments-in-mpd).

#### 400 (Bad Request)

An HTTP 400 (Bad Request) response indicates one of the following problems occurred:

- The URL is malformed.
- The post is too large (\> 10MB).
- The MPD cannot be parsed.
- The Initialization segment in the MPD is corrupt.

#### 401 (Unauthorized)

An HTTP 401 (Unauthorized) response indicates that the base URL for the YouTube DASH endpoint is corrupted or expired.

#### 405 (Method Not Allowed)

An HTTP 405 (Method Not Allowed) response indicates that a request other than `POST` or `PUT` was sent.

#### 409 (Conflict)

An HTTP 409 (Conflict) response to any PUT or POST operation indicates that YouTube cannot process the request. For example, this response might occur if the requester has sent numerous media segments, but YouTube still does not have the MPD, the Initialization segment, or both. In that example, the encoder would need to retransmit the MPD and Initialization segments before retrying the failed request.
| **Important:** An encoder MUST handle this response code correctly because it can be returned at any time, including during normal operations. Although there is no limit on the number of retries, repeated failures should be signalled to the encoder operator that the broadcast is failing.

#### 500 (Internal Server Error)

An HTTP 500 (Internal Server Error) response indicates that the server was unable to process the request. For this error, we recommend that you retry the request with [exponential backoff](https://developers.google.com/youtube/v3/live/guides/encoding-with-dash#retries-and-exponential-backoff).

## Examples

### URL Sequence

The URL sequence below shows a series of PUT requests that would be made to deliver content via DASH. The sequence assumes that the base URL for the YouTube DASH endpoint is:  

```
http://upload.youtube.com/dash_upload?cid=xxxx-xxxx-xxxx-xxxx&copy=0&file=
```

The sequence shows the MPD and Initialization segments sent separately. However, the Initialization segment can be [represented directly in the MPD](https://developers.google.com/youtube/v3/live/guides/encoding-with-dash#initialization-segments-in-mpd), and that practice is recommended. In addition, the MPD and Initialization segments should be [updated at least every 60 seconds](https://developers.google.com/youtube/v3/live/guides/encoding-with-dash#timing). So, eventually, the URLs for those segements would occur again in this sequence, and they would then be followed by URLs for more media segments.  

```
PUT upload.youtube.com/dash_upload?cid=xxxx-xxxx-xxxx-xxxx&copy=0&file=dash.mpd
PUT upload.youtube.com/dash_upload?cid=xxxx-xxxx-xxxx-xxxx&copy=0&file=init.mp4
PUT upload.youtube.com/dash_upload?cid=xxxx-xxxx-xxxx-xxxx&copy=0&file=media001.mp4
PUT upload.youtube.com/dash_upload?cid=xxxx-xxxx-xxxx-xxxx&copy=0&file=media002.mp4
PUT upload.youtube.com/dash_upload?cid=xxxx-xxxx-xxxx-xxxx&copy=0&file=media003.mp4
...
```

### WebM segments

#### MPD with embedded Initialization segment

The following sample MPD has an embedded Initialization segment in an RFC 2397 data URL. We recommend that you embed the Initialization segment in this manner rather than sending it separately.

This example is conformant for WebM (VP8 or VP9, Opus) ingestion to YouTube. The majority of the data URL has been elided for readability:  

```xml
<?xml version="1.0" encoding="UTF-8"?>
<MPD xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xmlns="urn:mpeg:dash:schema:mpd:2011"
     xsi:schemaLocation="urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd"
     type="dynamic" 
     profiles="urn:mpeg:dash:profile:isoff-live:2011" 
     minimumUpdatePeriod="PT60S"
     minBufferTime="PT12S"
     availabilityStartTime="2016-04-13T20:52:58" >
  <Period start="PT0S" id="1">
    <AdaptationSet mimeType="video/webm">
      <ContentComponent contentType="video" id="1"/>
      <SegmentTemplate timescale="1000"
           duration="2000"
           startNumber="1"
           initialization="data:video/mp4;base64,AAAAGGZ0eXBpc...AAA"
           media="/dash_upload?cid=xxxx-xxxx-xxxx-xxxx&copy=0&file=media-$Number%09d$.webm"/>
      <Representation id="1" width="1920" height="1080">
        <SubRepresentation contentComponent="1"/>
      </Representation>
    </AdaptationSet>
  </Period>
</MPD>
```

#### MPD

The following sample MPD, which does not have an embedded Initialization segment, is also conformant for WebM (VP8 or VP9, Opus) ingestion to YouTube:  

```xml
<?xml version="1.0" encoding="UTF-8"?>
<MPD xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xmlns="urn:mpeg:dash:schema:mpd:2011"
     xsi:schemaLocation="urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd"
     type="dynamic" 
     profiles="urn:mpeg:dash:profile:isoff-live:2011" 
     minimumUpdatePeriod="PT60S"
     minBufferTime="PT12S"
     availabilityStartTime="2016-04-13T20:52:58" >
  <Period start="PT0S" id="1">
    <AdaptationSet mimeType="video/webm">
      <ContentComponent contentType="video" id="1"/>
      <SegmentTemplate timescale="1000"
           duration="2000"
           startNumber="1"
           initialization="/dash_upload?cid=xxxx-xxxx-xxxx-xxxx&copy=0&file=init.webm"
           media="/dash_upload?cid=xxxx-xxxx-xxxx-xxxx&copy=0&file=media-$Number%09d$.webm"/>
      <Representation id="1" width="1920" height="1080">
        <SubRepresentation contentComponent="1"/>
      </Representation>
    </AdaptationSet>
  </Period>
</MPD>
```

#### Initialization

The following shows the layout of a sample WebM Initialization segment. It consists of the portion of the WebM stream up to but not including the first cluster.
![](https://developers.google.com/static/youtube/images/live/dash-multiplexed-webm-init-segment.png)

#### Media

The following shows the layout of a sample WebM media segment. It consists of a single WebM cluster. As with an ISO BMFF stream, the Initialization segment prepended to a series of clusters should produce a valid WebM stream.
![](https://developers.google.com/static/youtube/images/live/dash-multiplexed-webm-media-segment.png)

### ISO BMFF segments

#### MPD with embedded Initialization segment

The following sample MPD has an embedded Initialization segment in an RFC 2397 data URL. We recommend that you embed the Initialization segment in this manner rather than sending it separately.

This example is conformant for ISO BMFF (H.264, AAC) ingestion to YouTube. The majority of the data URL has been elided for readability:  

```xml
<?xml version="1.0" encoding="UTF-8"?>
<MPD xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns="urn:mpeg:dash:schema:mpd:2011"   
    xsi:schemaLocation="urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd" 
    type="dynamic"
    minimumUpdatePeriod="PT30S" 
    availabilityStartTime="2016-05-04T20:47:25" 
    minBufferTime="PT12S" 
    profiles="urn:mpeg:dash:profile:isoff-live:2011">
  <Period start="PT0S" id="1">
    <AdaptationSet mimeType="video/mp4" codecs="avc1.4d401e,mp4a.40.2">
      <ContentComponent contentType="video" id="1"/>
      <ContentComponent contentType="audio" id="2"/>
      <SegmentTemplate timescale="600"
             media="/dash_upload?cid=ug50-xg26-cbc1-2p0h&staging=1&copy=0&file=media$Number%09d$.mp4"
             initialization="data:video/mp4;base64,AAAAGGZ0eXBpc281AA...AA"
             duration="306"
             startNumber="1"/>
      <Representation id="1" width="640" height="360" bandwidth="526952">
        <SubRepresentation contentComponent="1" bandwidth="526952" 
codecs="avc1.4d401e"/>
        <SubRepresentation contentComponent="2" bandwidth="125584" codecs="mp4a.40.2"/>
      </Representation>
    </AdaptationSet>
  </Period>
</MPD>
```

#### MPD

The following sample MPD, which does not have an embedded Initialization segment, is also conformant for ISO BMFF (H.264, AAC) ingestion to YouTube:  

```xml
<?xml version="1.0" encoding="UTF-8"?>
<MPD xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xmlns="urn:mpeg:dash:schema:mpd:2011"
     xsi:schemaLocation="urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd"
     type="dynamic"
     profiles="urn:mpeg:dash:profile:isoff-live:2011"
     minimumUpdatePeriod="PT60S" 
     minBufferTime="PT12S"
     availabilityStartTime="2016-04-13T20:51:31" >
  <Period start="PT0S" id="1">
    <AdaptationSet mimeType="video/mp4" codecs="avc1.4d401e,mp4a.40.2">
      <ContentComponent contentType="video" id="1"/>
      <ContentComponent contentType="audio" id="2"/>
      <SegmentTemplate timescale="600"
           duration="1200"
           startNumber="1"
           initialization="/dash_upload?cid=xxxx-xxxx-xxxx-xxxx&copy=0&file=init.mp4"
           media="/dash_upload?cid=xxxx-xxxx-xxxx-xxxx&copy=0&file=media$Number%09d$.mp4"/>
      <Representation id="1" width="640" height="360" bandwidth="526952">
        <SubRepresentation contentComponent="1" bandwidth="526952" codecs="avc1.4d401e"/>
        <SubRepresentation contentComponent="2" bandwidth="125584" codecs="mp4a.40.2"/>
      </Representation>
    </AdaptationSet>
  </Period>
</MPD>
```

#### Initialization

The following diagram shows the layout of a sample multiplexed ISO BMFF Initialization segment. YouTube does not necessarily use of the atoms, but this is a conforming example. In particular, both audio and video tracks are represented.
![](https://developers.google.com/static/youtube/images/live/dash-multiplexed-iso-bmff-init-segment.png)

#### Media

The following diagram shows the layout of a sample multiplexed ISO BMFF media segment. YouTube does not necessarily use all of the atoms, but this is a conforming example. In particular, both audio and video tracks are represented. A series of these segments can be appended to an Initialization segment to produce a valid and complete multiplexed ISO BMFF stream.
![](https://developers.google.com/static/youtube/images/live/dash-multiplexed-iso-bmff-media-segment.png)

## Known Limitations

### RTMP and DASH ingestions

It is not possible to mix RTMP and DASH ingestions to YouTube. This applies to switching between the two during a broadcast as well as to using one as a primary ingestion method and the other for backup ingestion.