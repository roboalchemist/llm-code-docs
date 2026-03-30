# Source: https://img.ly/docs/cesdk/renderer/compatibility-139ef9/

---
title: "System Compatibility"
description: "Learn how device performance and hardware limits affect CE.SDK editing, rendering, and export capabilities."
platform: renderer
url: "https://img.ly/docs/cesdk/renderer/compatibility-139ef9/"
---

> This is one page of the CE.SDK Renderer documentation. For a complete overview, see the [Renderer Documentation Index](https://img.ly/docs/cesdk/renderer.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/renderer/llms-full.txt).

**Navigation:** [Compatibility & Security](https://img.ly/docs/cesdk/renderer/compatibility-fef719/) > [System Compatibility](https://img.ly/docs/cesdk/renderer/compatibility-139ef9/)

---

## Recommended Platform

| Component             | Recommended specifications                                               |
| --------------------- | ------------------------------------------------------------------------ |
| Processor (CPU)       | x86-64 Server CPU with SSE4.1 support                                    |
| System Memory (RAM)   | 4 GiB minimum, more depending on scene complexity and output resolution  |
| Graphics Card (GPU)   | NVIDIA GPU, optionally with H264 video codec support for further speedup |
| Operating System (OS) | Ubuntu Server 24.04 LTS                                                  |

A NVIDIA GPU is highly recommended for making graphics exports faster, and required for video export.
NVIDIA L4 is an affordable data center model available from many infrastructure and cloud providers that fits the system recommendations.

## Export Limitations

The export size is limited by the hardware capabilities of the device, specifically the available RAM and GPU framebuffer size.

CE.SDK makes use of hardware acceleration provided within that environment. Therefore, the hardware always acts as an upper bound of what’s achievable.

Unlike the client-side rendering done by the other platforms, CE.SDK Renderer can make use of server hardware and is not limited by interactivity performance constraints.
Therefore scenes of any complexity should be supported, limited only by the memory and GPU limits of the host hardware.



---

## More Resources

- **[Renderer Documentation Index](https://img.ly/docs/cesdk/renderer.md)** - Browse all Renderer documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/renderer/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/renderer/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
