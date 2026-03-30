# Source: https://img.ly/docs/cesdk/electron/browser-support-28c1b0/

---
title: "Browser Support"
description: "Find out which browsers and versions fully support CE.SDK features, including editing and video capabilities."
platform: electron
url: "https://img.ly/docs/cesdk/electron/browser-support-28c1b0/"
---

> This is one page of the CE.SDK Electron documentation. For a complete overview, see the [Electron Documentation Index](https://img.ly/docs/cesdk/electron.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/electron/llms-full.txt).

**Navigation:** [Compatibility & Security](https://img.ly/docs/cesdk/electron/compatibility-fef719/) > [Browser Support](https://img.ly/docs/cesdk/electron/browser-support-28c1b0/)

---

The CreativeEditor SDK requires specific APIs to fully function.
For video-related features, the required APIs are only supported in certain browsers.
As a result, the list of supported browsers is currently limited to the following:

| Supported Browser | Graphics Editing                              | Video Editing     | Video Export      |
| ----------------- | --------------------------------------------- | ----------------- | ----------------- |
| Chrome            | **114** or newer                              | **114** or newer  | **114** or newer  |
| Chrome Android    | **114** or newer                              | not supported     | not supported     |
| Chrome iOS        | **114** or newer (on iOS/iPadOS 15 or newer)  | not supported     | not supported     |
| Edge              | **114** or newer                              | **114** or newer  | **114** or newer  |
| Firefox           | **115** or newer                              | **130** or newer  | not supported     |
| Safari            | **15.6** or newer                             | **26.0** or newer | **26.0** or newer |
| Safari iOS        | **15.6** or newer (on iOS/iPadOS 15 or newer) | not supported     | not supported     |

**Note:** Firefox supports video editing (decoding) starting with version 130 via the WebCodecs API. However, video export (encoding) is not supported because Firefox does not include the patent-encumbered H.264 and AAC codecs required for video encoding.

For video features, CE.SDK automatically shows warning dialogs when unsupported browsers try to use video functionality. You can also detect video support programmatically using the `video.decode.checkSupport` and `video.encode.checkSupport` actions, or the silent `cesdk.utils.supportsVideoDecode()` and `cesdk.utils.supportsVideoEncode()` utilities. See the [Actions API](https://img.ly/docs/cesdk/electron/actions-6ch24x/) for implementation details.

While other browsers based on the Chromium project might work fine (Arc, Brave, Opera, Vivaldi etc.) they are not officially supported.

## Host Platform Restrictions

All supported browsers rely on the host's platform APIs for different kind of functionality (e.g. video support). Check our [known editor limitations](https://img.ly/docs/cesdk/electron/compatibility-139ef9/) for more details on these.



---

## More Resources

- **[Electron Documentation Index](https://img.ly/docs/cesdk/electron.md)** - Browse all Electron documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/electron/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/electron/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
