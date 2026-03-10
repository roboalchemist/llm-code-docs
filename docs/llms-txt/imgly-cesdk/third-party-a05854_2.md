# Source: https://img.ly/docs/cesdk/electron/import-media/from-remote-source/third-party-a05854/

---
title: "Integrate Third-Party APIs"
description: "Import media from any third-party service into CE.SDK using custom asset sources."
platform: electron
url: "https://img.ly/docs/cesdk/electron/import-media/from-remote-source/third-party-a05854/"
---

> This is one page of the CE.SDK Electron documentation. For a complete overview, see the [Electron Documentation Index](https://img.ly/docs/cesdk/electron.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/electron/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/electron/guides-8d8b00/) > [Import Media Assets](https://img.ly/docs/cesdk/electron/import-media-4e3703/) > [Import From Remote Source](https://img.ly/docs/cesdk/electron/import-media/from-remote-source-b65faf/) > [From Third-Party](https://img.ly/docs/cesdk/electron/import-media/from-remote-source/third-party-a05854/)

---

CE.SDK makes it easy to integrate any third-party API using the custom asset
source mechanism, allowing you to import media directly into your creative
applications.

## Custom Asset Sources

CE.SDK's asset source system provides a flexible way to connect to any third-party API. Whether you're working with stock images, audio libraries, or custom data sources, the asset source mechanism handles search, pagination, and asset management automatically. The system works with any REST API, giving you complete control over how media is fetched and displayed.

## Available Integration Examples

We've created detailed implementation guides for popular third-party services that demonstrate how to build custom asset sources:

### Stock Images

- **[Unsplash](https://img.ly/docs/cesdk/electron/import-media/from-remote-source/unsplash-8f31f0/)** - High-quality royalty-free photos with powerful search capabilities
- **[Pexels](https://img.ly/docs/cesdk/electron/import-media/from-remote-source/pexels-90d5df/)** - Royalty-free stock photography with curated collections
- **[Getty Images](https://img.ly/docs/cesdk/electron/import-media/from-remote-source/getty-images-a3931c/)** - Premium stock photography using a secure proxy server architecture

### Audio Libraries

- **[Soundstripe](https://img.ly/docs/cesdk/electron/import-media/from-remote-source/soundstripe-9a42a9/)** - Royalty-free music and audio tracks for video projects

Each guide includes working code examples, API authentication setup, and best practices for integrating that specific service.

## Common Integration Patterns

Most third-party integrations share similar patterns:

- **Search functionality** - Enable users to search the third-party library
- **Pagination** - Handle large result sets with infinite scroll or page-based navigation
- **Asset preview** - Display thumbnails and metadata before importing
- **Authentication** - Manage API keys securely (client-side or via proxy server)

## Next Steps

Choose the integration guide that matches your needs to see a complete implementation. The patterns shown in these guides can be adapted to integrate virtually any third-party API into CE.SDK.



---

## More Resources

- **[Electron Documentation Index](https://img.ly/docs/cesdk/electron.md)** - Browse all Electron documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/electron/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/electron/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
