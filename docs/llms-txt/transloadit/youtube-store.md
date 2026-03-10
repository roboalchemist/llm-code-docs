# Source: https://transloadit.com/docs/robots/youtube-store.md

###### Note

This Robot only accepts videos.

## Installation

Since YouTube works with OAuth, you will need to generate [Template Credentials](/c/template-credentials/) to use this Robot.

To change the `title`, `description`, `category`, or `keywords` per video, we recommend to [inject variables into your Template](/docs/topics/templates.md).

## Adding a thumbnail image to your video

You can add a custom thumbnail to your video on YouTube by using our `"as"` syntax for the `"use"` parameter to supply both a video and an image to the step:

![](/_next/static/media/copy.8f7d2926.svg?dpl=dpl_GAEaNRfbaNgVy6q3c3ke5o1s9Xtk)

```json
"exported": {
  "use": [
    { "name": "video_encode_step", "as": "video" },
    { "name": "image_resize_step", "as": "image" },
  ],
  ...
},

```

If you encounter an error such as "The authenticated user doesnʼt have permissions to upload and set custom video thumbnails", you should go to your YouTube account and try adding a custom thumbnail to one of your existing videos. Youʼll be prompted to add your phone number. Once youʼve added it, the error should go away.
