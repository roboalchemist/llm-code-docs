# Source: https://transloadit.com/docs/robots/image-generate.md

Allows you to specify a set of metadata that is more expensive on CPU power to calculate, and thus is disabled by default to keep your Assemblies processing fast.

For images, you can add `"has_transparency": true` in this object to extract if the image contains transparent parts and `"dominant_colors": true` to extract an array of hexadecimal color codes from the image.

For images, you can also add `"blurhash": true` to extract a [BlurHash](https://blurha.sh) string — a compact representation of a placeholder for the image, useful for showing a blurred preview while the full image loads.

For videos, you can add the `"colorspace: true"` parameter to extract the colorspace of the output video.

For audio, you can add `"mean_volume": true` to get a single value representing the mean average volume of the audio file.

You can also set this to `false` to skip metadata extraction and speed up transcoding.
