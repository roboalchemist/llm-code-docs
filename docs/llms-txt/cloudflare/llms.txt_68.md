# Source: https://developers.cloudflare.com/images/llms.txt

# Cloudflare Images

Store, transform, optimize, and deliver images at scale

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/images/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [Cloudflare Images llms-full.txt](https://developers.cloudflare.com/images/llms-full.txt) for the complete Cloudflare Images documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Cloudflare Images](https://developers.cloudflare.com/images/index.md): Streamline your image infrastructure with Cloudflare Images. Store, transform, and deliver images efficiently using Cloudflare's global network.

## Getting started

- [Getting started](https://developers.cloudflare.com/images/get-started/index.md)

## Upload images

- [Upload images](https://developers.cloudflare.com/images/upload-images/index.md)
- [Accept user-uploaded images](https://developers.cloudflare.com/images/upload-images/direct-creator-upload/index.md)
- [Upload via batch API](https://developers.cloudflare.com/images/upload-images/images-batch/index.md)
- [Upload via Sourcing Kit](https://developers.cloudflare.com/images/upload-images/sourcing-kit/index.md)
- [Credentials](https://developers.cloudflare.com/images/upload-images/sourcing-kit/credentials/index.md)
- [Edit sources](https://developers.cloudflare.com/images/upload-images/sourcing-kit/edit/index.md)
- [Enable Sourcing Kit](https://developers.cloudflare.com/images/upload-images/sourcing-kit/enable/index.md)
- [Upload via custom path](https://developers.cloudflare.com/images/upload-images/upload-custom-path/index.md)
- [Upload via dashboard](https://developers.cloudflare.com/images/upload-images/upload-dashboard/index.md)
- [Upload via a Worker](https://developers.cloudflare.com/images/upload-images/upload-file-worker/index.md): Learn how to upload images to Cloudflare using Workers. This guide provides code examples for uploading both standard and AI-generated images efficiently.
- [Upload via URL](https://developers.cloudflare.com/images/upload-images/upload-url/index.md)

## Transform images

- [Transform images](https://developers.cloudflare.com/images/transform-images/index.md)
- [Bind to Workers API](https://developers.cloudflare.com/images/transform-images/bindings/index.md)
- [Control origin access](https://developers.cloudflare.com/images/transform-images/control-origin-access/index.md)
- [Draw overlays and watermarks](https://developers.cloudflare.com/images/transform-images/draw-overlays/index.md)
- [Integrate with frameworks](https://developers.cloudflare.com/images/transform-images/integrate-with-frameworks/index.md)
- [Make responsive images](https://developers.cloudflare.com/images/transform-images/make-responsive-images/index.md): Learn how to serve responsive images using HTML srcset and width=auto for optimal display on various devices. Ideal for high-DPI and fluid layouts.
- [Preserve Content Credentials](https://developers.cloudflare.com/images/transform-images/preserve-content-credentials/index.md)
- [Serve images from custom paths](https://developers.cloudflare.com/images/transform-images/serve-images-custom-paths/index.md)
- [Define source origin](https://developers.cloudflare.com/images/transform-images/sources/index.md)
- [Transform via URL](https://developers.cloudflare.com/images/transform-images/transform-via-url/index.md)
- [Transform via Workers](https://developers.cloudflare.com/images/transform-images/transform-via-workers/index.md)

## Demos and architectures

- [Demos and architectures](https://developers.cloudflare.com/images/demos/index.md)

## Pricing

- [Pricing](https://developers.cloudflare.com/images/pricing/index.md)

## Cloudflare Polish

- [Cloudflare Polish](https://developers.cloudflare.com/images/polish/index.md)
- [Activate Polish](https://developers.cloudflare.com/images/polish/activate-polish/index.md)
- [Cf-Polished statuses](https://developers.cloudflare.com/images/polish/cf-polished-statuses/index.md): Learn about Cf-Polished statuses in Cloudflare Images. Understand how to handle missing headers, optimize image formats, and troubleshoot common issues.
- [Polish compression](https://developers.cloudflare.com/images/polish/compression/index.md): Learn about Cloudflare's Polish compression options, including Lossless, Lossy, and WebP, to optimize image file sizes while managing metadata effectively.
- [WebP may be skipped](https://developers.cloudflare.com/images/polish/no-webp/index.md)

## Images API Reference

- [Images API Reference](https://developers.cloudflare.com/images/images-api/index.md)

## Examples

- [Examples](https://developers.cloudflare.com/images/examples/index.md)
- [Transcode images](https://developers.cloudflare.com/images/examples/transcode-from-workers-ai/index.md): Transcode an image from Workers AI before uploading to R2
- [Watermarks](https://developers.cloudflare.com/images/examples/watermark-from-kv/index.md): Draw a watermark from KV on an image from R2

## manage-images

- [Apply blur](https://developers.cloudflare.com/images/manage-images/blur-variants/index.md)
- [Browser TTL](https://developers.cloudflare.com/images/manage-images/browser-ttl/index.md)
- [Configure webhooks](https://developers.cloudflare.com/images/manage-images/configure-webhooks/index.md)
- [Create variants](https://developers.cloudflare.com/images/manage-images/create-variants/index.md)
- [Delete images](https://developers.cloudflare.com/images/manage-images/delete-images/index.md)
- [Delete variants](https://developers.cloudflare.com/images/manage-images/delete-variants/index.md)
- [Edit images](https://developers.cloudflare.com/images/manage-images/edit-images/index.md)
- [Enable flexible variants](https://developers.cloudflare.com/images/manage-images/enable-flexible-variants/index.md)
- [Export images](https://developers.cloudflare.com/images/manage-images/export-images/index.md)
- [Serve images from custom domains](https://developers.cloudflare.com/images/manage-images/serve-images/serve-from-custom-domains/index.md)
- [Serve private images](https://developers.cloudflare.com/images/manage-images/serve-images/serve-private-images/index.md)
- [Serve uploaded images](https://developers.cloudflare.com/images/manage-images/serve-images/serve-uploaded-images/index.md)

## platform

- [Changelog](https://developers.cloudflare.com/images/platform/changelog/index.md)

## reference

- [Security](https://developers.cloudflare.com/images/reference/security/index.md)
- [Troubleshooting](https://developers.cloudflare.com/images/reference/troubleshooting/index.md)

## tutorials

- [Optimize mobile viewing](https://developers.cloudflare.com/images/tutorials/optimize-mobile-viewing/index.md): Lazy loading is an easy way to optimize the images on your webpages for mobile devices, with faster page load times and lower costs.
- [Transform user-uploaded images before uploading to R2](https://developers.cloudflare.com/images/tutorials/optimize-user-uploaded-image/index.md): Set up bindings to connect Images, R2, and Assets to your Worker