# Source: https://transloadit.com/docs/robots/video-adaptive.md

This Robot accepts all types of video files and audio files. Do not forget to use Step bundling in your `use` parameter to make the Robot work on several input files at once.

This Robot is normally used in combination with [🤖/video/encode](/docs/robots/video-encode.md). We have implemented video and audio encoding presets specifically for MPEG-Dash and HTTP Live Streaming support. These presets are prefixed with `"dash/"` and `"hls/"`. [View a HTTP Live Streaming demo here](/demos/video-encoding/implement-http-live-streaming/).

### Required CORS settings for MPEG-Dash and HTTP Live Streaming

Playing back MPEG-Dash Manifest or HLS playlist files requires a proper CORS setup on the server-side. The file-serving server should be configured to add the following header fields to responses:

![](/_next/static/media/copy.8f7d2926.svg?dpl=dpl_GAEaNRfbaNgVy6q3c3ke5o1s9Xtk)

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET
Access-Control-Allow-Headers: *

```

If the files are stored in an Amazon S3 Bucket, you can use the following [CORS definition](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ManageCorsUsing.html) to ensure the CORS header fields are set correctly:

![](/_next/static/media/copy.8f7d2926.svg?dpl=dpl_GAEaNRfbaNgVy6q3c3ke5o1s9Xtk)

```json
[
  {
    "AllowedHeaders": ["*"],
    "AllowedMethods": ["GET"],
    "AllowedOrigins": ["*"],
    "ExposeHeaders": []
  }
]

```

To set up CORS for your S3 bucket:

1. Visit <https://s3.console.aws.amazon.com/s3/buckets/>
2. Click on your bucket
3. Click "Permissions"
4. Edit "Cross-origin resource sharing (CORS)"

### Storing Segments and Playlist files

The Robot gives its result files (segments, initialization segments, MPD manifest files and M3U8 playlist files) the right metadata property `relative_path`, so that you can store them easily using one of our storage Robots.

In the `path` parameter of the storage Robot of your choice, use the Assembly Variable `${file.meta.relative_path}` to store files in the proper paths to make the playlist files work.
