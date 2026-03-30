# Source: https://transloadit.com/docs/robots/audio-artwork.md

This Robot extracts or inserts cover artwork in audio files.

For extraction, it uses the image format embedded within the audio file — most often, this is JPEG. If you need the image in a different format, pipe the result into [🤖/image/resize](/docs/robots/image-resize.md).

For insertion, provide both an audio file (as `"audio"`) and an image file (as `"image"`) via the `use` parameter, and set `method` to `"insert"`. The image will be embedded as the cover artwork of the audio file.
