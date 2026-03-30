# Troubleshooting Issues

If you are facing an issue with Kurento Media Server, follow this basic check list:

- 

**Step 1**: Test with the **latest version** of Kurento Media Server: **7.3.0**. Follow the installation instructions here: Installation Guide.

- 

**Step 2**: Test with the latest (unreleased) changes by installing a nightly version: Installing Nightly Builds.

- 

**Step 3**: Search for your issue in our GitHub bugtracker [https://github.com/Kurento/kurento/issues] and the Kurento Public Mailing List [https://groups.google.com/forum/#!forum/kurento].

- 

**Step 4**: If you want full attention from the Kurento team, get in contact with us to request Commercial Support.

For more information about how to request support, and how to submit bug reports and commercial enquiries, have a look at the Support page.

**My Kurento Media Server doesn’t work, what should I do?**

This document outlines several bits of knowledge that can prove very useful when studying a failure or error in KMS:

Table of Contents

- 

Troubleshooting Issues

  - 

Media Server Crashes

  - 

Corrupted Video

    - 

About sender video encoding

    - 

About H.264 & VP8 color encoding

  - 

Other Media Server issues

    - 

Reached limit / Resource temporarily unavailable

    - 

`GStreamer-CRITICAL` messages in the log

    - 

CPU usage grows too high

    - 

Memory usage grows too high

    - 

Service init doesn’t work

    - 

OpenH264 not found

    - 

Missing audio or video streams

  - 

Application Server

    - 

KMS is not running

    - 

KMS became unresponsive (due to network error or crash)

    - 

Node.js / NPM failures

    - 

Connection ends exactly after 60 seconds

    - 

“Expects at least 4 fields”

    - 

“Error: ‘operationParams’ is required”

  - 

WebRTC failures

    - 

ICE connection problems

    - 

mDNS ICE candidate fails: Name or service not known

  - 

Docker issues

    - 

Publishing Docker ports eats memory

    - 

Multicast fails in Docker

  - 

Element-specific info

    - 

PlayerEndpoint

      - 

RTSP broken audio

      - 

RTSP broken video

      - 

RTSP Video stuttering

    - 

RecorderEndpoint

      - 

Zero-size video files

      - 

Smaller or low quality video files

  - 

Browser

    - 

Safari doesn’t work