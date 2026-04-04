# Source: https://img.ly/docs/cesdk/mac-catalyst/compatibility-139ef9/

---
title: "System Compatibility"
description: "Learn how device performance and hardware limits affect CE.SDK editing, rendering, and export capabilities."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/compatibility-139ef9/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

**Navigation:** [Compatibility & Security](https://img.ly/docs/cesdk/mac-catalyst/compatibility-fef719/) > [System Compatibility](https://img.ly/docs/cesdk/mac-catalyst/compatibility-139ef9/)

---

## Targets

On Apple platforms, CE.SDK makes use of system-frameworks to benefit from hardware acceleration and platform native performance. The following targets are supported:

- iOS & iPadOS 14 or later
- macOS 12 or later

## Recommended Hardware

- iPhone 8 or later
- iPad (6th gen) or later
- Macs released in the last 7 years

## Video

Playback and exporting is **supported for all codecs** mentioned in the general section.

However, mobile devices have stricter limits around the number of parallel encoders and decoders compared to fully fledged desktop machines. This means, that very large scenes with more than 10 videos shown in parallel may fail to play all videos at the same time and can’t be exported.

## Export Limitations

The export size is limited by the hardware capabilities of the device, e.g., due to the maximum texture size that can be allocated. The maximum possible export size can be queried via API, see [export guide](https://img.ly/docs/cesdk/mac-catalyst/export-save-publish/export/overview-9ed3a8/).



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
