# Source: https://transloadit.com/docs/robots/image-optimize.md

With this Robot it's possible to reduce the file size of your JPEG, PNG, GIF, WEBP and SVG images by up to 80% for big images and 65% for small to medium sized ones — while keeping their original quality!

This Robot enables you to lower your storage and bandwidth costs, and improves your user experience and monetization by reducing the load time of image-intensive web pages.

It works well together with [🤖/image/resize](/docs/robots/image-resize.md) to bring the full power of resized and optimized images to your website or app.

###### Note

This Robot accepts all image types and will just pass on unsupported image types unoptimized. Hence, there is no need to set up [🤖/file/filter](/docs/robots/file-filter.md) workflows for this.

###### Note

PNG optimization uses only lossless (optipng) compressors by default. To also enable lossy compression (pngquant), set `lossy: true`. When enabled, both lossy and lossless compressors compete and the smallest result wins, which may cause color shifts in some images.
