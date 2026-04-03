# Source: https://developers.cloudflare.com/stream/llms.txt

# Stream

Store, encode, deliver, and play videos on sites and applications

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/stream/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [Stream llms-full.txt](https://developers.cloudflare.com/stream/llms-full.txt) for the complete Stream documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Cloudflare Stream](https://developers.cloudflare.com/stream/index.md)

## Get started

- [Get started](https://developers.cloudflare.com/stream/get-started/index.md)

## Upload videos

- [Upload videos](https://developers.cloudflare.com/stream/uploading-videos/index.md)
- [Direct creator uploads](https://developers.cloudflare.com/stream/uploading-videos/direct-creator-uploads/index.md)
- [Player API](https://developers.cloudflare.com/stream/uploading-videos/player-api/index.md)
- [Resumable and large files (tus)](https://developers.cloudflare.com/stream/uploading-videos/resumable-uploads/index.md)
- [Upload with a link](https://developers.cloudflare.com/stream/uploading-videos/upload-via-link/index.md)
- [Basic video uploads](https://developers.cloudflare.com/stream/uploading-videos/upload-video-file/index.md)

## Stream live video

- [Stream live video](https://developers.cloudflare.com/stream/stream-live/index.md)
- [Add custom ingest domains](https://developers.cloudflare.com/stream/stream-live/custom-domains/index.md)
- [Download live stream videos](https://developers.cloudflare.com/stream/stream-live/download-stream-live-videos/index.md)
- [DVR for Live](https://developers.cloudflare.com/stream/stream-live/dvr-for-live/index.md)
- [Live Instant Clipping](https://developers.cloudflare.com/stream/stream-live/live-instant-clipping/index.md)
- [Record and replay live streams](https://developers.cloudflare.com/stream/stream-live/replay-recordings/index.md)
- [Simulcast (restream) videos](https://developers.cloudflare.com/stream/stream-live/simulcasting/index.md)
- [Start a live stream](https://developers.cloudflare.com/stream/stream-live/start-stream-live/index.md)
- [Stream Live API docs](https://developers.cloudflare.com/stream/stream-live/stream-live-api/index.md)
- [Troubleshooting a live stream](https://developers.cloudflare.com/stream/stream-live/troubleshooting/index.md)
- [Watch a live stream](https://developers.cloudflare.com/stream/stream-live/watch-live-stream/index.md)
- [Receive Live Webhooks](https://developers.cloudflare.com/stream/stream-live/webhooks/index.md)

## Transform videos

- [Transform videos](https://developers.cloudflare.com/stream/transform-videos/index.md)
- [Bind to Workers API](https://developers.cloudflare.com/stream/transform-videos/bindings/index.md)
- [Define source origin](https://developers.cloudflare.com/stream/transform-videos/sources/index.md)
- [Troubleshooting](https://developers.cloudflare.com/stream/transform-videos/troubleshooting/index.md)

## Manage videos

- [Manage videos](https://developers.cloudflare.com/stream/manage-video-library/index.md)
- [Manage creators](https://developers.cloudflare.com/stream/manage-video-library/creator-id/index.md)
- [Search for videos](https://developers.cloudflare.com/stream/manage-video-library/searching/index.md)
- [Use webhooks](https://developers.cloudflare.com/stream/manage-video-library/using-webhooks/index.md)

## Analytics

- [Analytics](https://developers.cloudflare.com/stream/getting-analytics/index.md)
- [GraphQL Analytics API](https://developers.cloudflare.com/stream/getting-analytics/fetching-bulk-analytics/index.md)
- [Get live viewer counts](https://developers.cloudflare.com/stream/getting-analytics/live-viewer-count/index.md)

## WebRTC

- [WebRTC](https://developers.cloudflare.com/stream/webrtc-beta/index.md)

## Examples

- [Examples](https://developers.cloudflare.com/stream/examples/index.md)
- [Android (ExoPlayer)](https://developers.cloudflare.com/stream/examples/android/index.md): Example of video playback on Android using ExoPlayer
- [dash.js](https://developers.cloudflare.com/stream/examples/dash-js/index.md): Example of video playback with Cloudflare Stream and the DASH reference player (dash.js)
- [hls.js](https://developers.cloudflare.com/stream/examples/hls-js/index.md): Example of video playback with Cloudflare Stream and the HLS reference player (hls.js)
- [iOS (AVPlayer)](https://developers.cloudflare.com/stream/examples/ios/index.md): Example of video playback on iOS using AVPlayer
- [First Live Stream with OBS](https://developers.cloudflare.com/stream/examples/obs-from-scratch/index.md): Set up and start your first Live Stream using OBS (Open Broadcaster Software) Studio
- [RTMPS playback](https://developers.cloudflare.com/stream/examples/rtmps_playback/index.md): Example of sub 1s latency video playback using RTMPS and ffplay
- [Shaka Player](https://developers.cloudflare.com/stream/examples/shaka-player/index.md): Example of video playback with Cloudflare Stream and Shaka Player
- [SRT playback](https://developers.cloudflare.com/stream/examples/srt_playback/index.md): Example of sub 1s latency video playback using SRT and ffplay
- [Stream Player](https://developers.cloudflare.com/stream/examples/stream-player/index.md): Example of video playback with the Cloudflare Stream Player
- [Test webhooks locally](https://developers.cloudflare.com/stream/examples/test-webhooks-locally/index.md): Test Cloudflare Stream webhook notifications locally using a Cloudflare Worker and Cloudflare Tunnel.
- [Video.js](https://developers.cloudflare.com/stream/examples/video-js/index.md): Example of video playback with Cloudflare Stream and Video.js
- [Vidstack](https://developers.cloudflare.com/stream/examples/vidstack/index.md): Example of video playback with Cloudflare Stream and Vidstack

## Stream API Reference

- [Stream API Reference](https://developers.cloudflare.com/stream/stream-api/index.md)

## Changelog

- [Changelog](https://developers.cloudflare.com/stream/changelog/index.md)

## FAQ

- [FAQ](https://developers.cloudflare.com/stream/faq/index.md)

## Pricing

- [Pricing](https://developers.cloudflare.com/stream/pricing/index.md)

## edit-videos

- [Add additional audio tracks](https://developers.cloudflare.com/stream/edit-videos/adding-additional-audio-tracks/index.md)
- [Add captions](https://developers.cloudflare.com/stream/edit-videos/adding-captions/index.md)
- [Apply watermarks](https://developers.cloudflare.com/stream/edit-videos/applying-watermarks/index.md)
- [Add player enhancements](https://developers.cloudflare.com/stream/edit-videos/player-enhancements/index.md)
- [Clip videos](https://developers.cloudflare.com/stream/edit-videos/video-clipping/index.md)

## viewing-videos

- [Display thumbnails](https://developers.cloudflare.com/stream/viewing-videos/displaying-thumbnails/index.md)
- [Download video or audio](https://developers.cloudflare.com/stream/viewing-videos/download-videos/index.md)
- [Secure your Stream](https://developers.cloudflare.com/stream/viewing-videos/securing-your-stream/index.md)
- [Use your own player](https://developers.cloudflare.com/stream/viewing-videos/using-own-player/index.md)
- [Android](https://developers.cloudflare.com/stream/viewing-videos/using-own-player/android/index.md)
- [iOS](https://developers.cloudflare.com/stream/viewing-videos/using-own-player/ios/index.md)
- [Web](https://developers.cloudflare.com/stream/viewing-videos/using-own-player/web/index.md)
- [Use the Stream Player](https://developers.cloudflare.com/stream/viewing-videos/using-the-stream-player/index.md)
- [Stream Player API](https://developers.cloudflare.com/stream/viewing-videos/using-the-stream-player/using-the-player-api/index.md)