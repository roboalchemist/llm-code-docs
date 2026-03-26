# Source: https://momentic.ai/docs/browsers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Browsers

> Supported browser types

## Chromium

Chromium is the default browser option for Momentic. It is a fast and
lightweight browser optimized for testing needs. However, it does not support
all the features of Google Chrome such as video playback. Chromium is known to
be unstable when used to automate sites with graphics-heavy scripts.

## Google Chrome

Google Chrome is a full-fledged browser that offers the broadest feature
support, including H.264 video playback, media streaming, WebGL, and more. It
may consume more resources than Chromium and execute tests more slowly.

## Chrome for Testing

[Chrome for Testing](https://developer.chrome.com/blog/chrome-for-testing/) is a
browser version newly released in 2025, maintained by Google specifically for
testing purposes.

## Browser behavior

To ensure consistent test results, Momentic overrides certain browser behaviors.

| Setting                   | Value                                                                                                               |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| User agent                | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.31 Safari/537.36 |
| Location                  | 37.7749 by -122.4194 (San Francisco)                                                                                |
| Video auto-play           | Disabled                                                                                                            |
| Chrome browser onboarding | Disabled                                                                                                            |
| Desktop notifications     | Disabled                                                                                                            |


Built with [Mintlify](https://mintlify.com).