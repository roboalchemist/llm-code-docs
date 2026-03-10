# Source: https://img.ly/docs/cesdk/renderer/get-started/benchmarks-b3n4ch/

---
title: "Benchmarks"
description: "Performance benchmarks and metrics for CE.SDK Renderer"
platform: renderer
url: "https://img.ly/docs/cesdk/renderer/get-started/benchmarks-b3n4ch/"
---

> This is one page of the CE.SDK Renderer documentation. For a complete overview, see the [Renderer Documentation Index](https://img.ly/docs/cesdk/renderer.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/renderer/llms-full.txt).

**Navigation:** [Get Started](https://img.ly/docs/cesdk/renderer/get-started/overview-e18f40/) > [Benchmarks](https://img.ly/docs/cesdk/renderer/get-started/benchmarks-b3n4ch/)

---

To better gauge the capabilities of CE.SDK Renderer we provide a set of benchmarks covering both our evaluation and production variants.

## Pipeline Options

| Pipeline       | Use Case                  | License                   |
| -------------- | ------------------------- | ------------------------- |
| **Evaluation** | Testing, prototypes, POCs | Open-source, free         |
| **Production** | Commercial deployments    | Commercial with AV codecs |

> **Note:** **Production Pipeline required for all commercial use, see
> [Patents & Acknowledgements](https://img.ly/docs/cesdk/renderer/get-started/patents-acknowledgements-9k2p4m/) for details.**

## Performance Factors

Rendering performance depends on:

- **Scene complexity**: Video duration, asset count, effects, transitions
- **Archive size**: Larger files with high-resolution assets take longer
- **Network speed**: Asset download and result upload times
- **Hardware**: GPU acceleration and CPU cores available
- **Output settings**: Resolution, bitrate, codec settings

## Benchmarks

| Scene                                                                                                                   | Output Resolution | Archive Size | Duration | Evaluation | Production |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------- | ------------ | -------- | ---------- | ---------- |
| [template-red-dot](https://cdn.img.ly/assets/demo/v3/ly.img.video.template/templates/red-dot.scene)                     | 1080x1920         | 27.5 MB      | 17.7s    | 9.6s       | 12.7s      |
| [template-milli-surf-school](https://cdn.img.ly/assets/demo/v3/ly.img.video.template/templates/milli-surf-school.scene) | 1080x1920         | 22.6 MB      | 20.5s    | 7.0s       | 12.6s      |
| [template-monthly-review](https://cdn.img.ly/assets/demo/v3/ly.img.video.template/templates/monthly-review.scene)       | 1080x1920         | 30.6 MB      | 13.5s    | 5.6s       | 8.8s       |
| [template-my-plants](https://cdn.img.ly/assets/demo/v3/ly.img.video.template/templates/my-plants.scene)                 | 1080x1920         | 39.2 MB      | 15.2s    | 5.7s       | 9.8s       |
| [template-milli-surf-school](https://cdn.img.ly/assets/demo/v3/ly.img.video.template/templates/milli-surf-school.scene) | 2160x3840 (4K)    | 22.6 MB      | 20.5s    | 66.3s      | 33.2s      |

Tested on a fal.ai cloud GPU instance with an Nvidia L4. Additional license handshakes currently slightly decrease production execution time.

## Expected Processing Times

| Scene Type                                  | Estimated Time |
| ------------------------------------------- | -------------- |
| Simple template, \<15s, minimal assets      | 5-10s          |
| Medium complexity, 15-30s, some clips       | 10-15s         |
| High complexity, 30-60s, many clips/effects | 15-30s         |
| Very complex, 60s+, heavy effects           | 30s+           |

## Optimization Tips

1. **Assets**: Host on fast CDNs, compress files, use appropriate resolutions
2. **Scene Design**: Minimize layers, optimize effects, avoid over-resolution
3. **Output**: Choose appropriate resolution/bitrate for your use case
4. **Network**: Ensure stable, high-bandwidth connection

## Getting Started

### Evaluation

1. Sign up for CE.SDK trial or use with watermark
2. Use public Docker deployment (hub.docker.com/imgly/cesdk-renderer)
3. Test with your scenes

### Production

1. Contact sales@img.ly for licensing
2. Receive production image access details
3. Test with your scenes

***

*Benchmarks: October 2025, Nvidia L4 on fal.ai. Contact sales@img.ly for licensing or custom testing.*



---

## More Resources

- **[Renderer Documentation Index](https://img.ly/docs/cesdk/renderer.md)** - Browse all Renderer documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/renderer/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/renderer/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
