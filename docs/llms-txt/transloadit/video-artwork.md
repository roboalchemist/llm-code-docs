# Source: https://transloadit.com/docs/robots/video-artwork.md

This Robot extracts or inserts cover artwork in video files.

For extraction, it uses the image format embedded within the video file — most often, this is JPEG. If you need the image in a different format, pipe the result into [🤖/image/resize](/docs/robots/image-resize.md).

For insertion, provide both a video file (as `"video"`) and an image file (as `"image"`) via the `use` parameter, and set `method` to `"insert"`. The image will be embedded as the cover artwork of the video file.
