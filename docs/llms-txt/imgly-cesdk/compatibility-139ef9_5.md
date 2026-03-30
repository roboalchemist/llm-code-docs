# Source: https://img.ly/docs/cesdk/js/compatibility-139ef9/

---
title: "System Compatibility"
description: "Learn how device performance and hardware limits affect CE.SDK editing, rendering, and export capabilities."
platform: vanilla-js
url: "https://img.ly/docs/cesdk/js/compatibility-139ef9/"
---

> This is one page of the CE.SDK Vanilla JS/TS documentation. For a complete overview, see the [Vanilla JS/TS Documentation Index](https://img.ly/docs/cesdk/js.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/js/llms-full.txt).

**Navigation:** [Compatibility & Security](https://img.ly/docs/cesdk/js/compatibility-fef719/) > [System Compatibility](https://img.ly/docs/cesdk/js/compatibility-139ef9/)

---

## Recommended Hardware

| Platform         | Hardware                                                                       |
| ---------------- | ------------------------------------------------------------------------------ |
| Desktop          | A notebook or desktop released in the last 7 years and at least 4GB of memory. |
| Mobile (Apple)   | iPhone 8, iPad (6th gen) or newer                                              |
| Mobile (Android) | Phones & tablets released in the last 4 years                                  |

## Video

Our video feature introduces additional requirements and we generally distinguish playback (decoding) and export (encoding) capabilities. On the web, certain browser features directly depend on the host operating system. For video, this currently introduces the following limitations:

- Transparency in H.265 videos is **not supported** on Windows hosts.
- **Chrome on Linux** generally doesn't ship with encoder support for H.264 & AAC, which can cause video exports to fail even though decoding of non-free codecs is supported.
- **Firefox** supports video editing (decoding) starting with version 130 via the WebCodecs API. However, video export is **not supported** because Firefox does not include the patent-encumbered H.264 and AAC codecs required for encoding.
- **Chromium** although technically the base of Chrome doesn't include any codecs for licensing reasons and therefore can't be used for video editing. It does fall back to system-provided media libraries on e.g. macOS, but support is not guaranteed in any way.
- **Linux browsers** generally have limited video support due to codec licensing. Video editing may work if the browser can decode H.264/AAC, but video export typically fails because open-source browser builds do not include the required encoders.
- Video is **not supported** on mobile browsers on any platform due to technical limitations which result in performance issues.

To detect these limitations at runtime, use the `video.decode.checkSupport` and `video.encode.checkSupport` actions, or the `cesdk.utils.supportsVideoDecode()` and `cesdk.utils.supportsVideoEncode()` utilities.

## Export Limitations

The export size is limited by the hardware capabilities of the device, e.g., due to the maximum texture size that can be allocated. The maximum possible export size can be queried via API, see [export guide](https://img.ly/docs/cesdk/js/export-save-publish/export/overview-9ed3a8/).



---

## More Resources

- **[Vanilla JS/TS Documentation Index](https://img.ly/docs/cesdk/js.md)** - Browse all Vanilla JS/TS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/js/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/js/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
