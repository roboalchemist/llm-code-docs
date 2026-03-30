# Integrate Third-Party APIs

CE.SDK makes it easy to integrate any third-party API using the custom asset source mechanism, allowing you to import media directly into your creative applications.

## Custom Asset Sources[#](#custom-asset-sources)

CE.SDK’s asset source system provides a flexible way to connect to any third-party API. Whether you’re working with stock images, audio libraries, or custom data sources, the asset source mechanism handles search, pagination, and asset management automatically. The system works with any REST API, giving you complete control over how media is fetched and displayed.

## Available Integration Examples[#](#available-integration-examples)

We’ve created detailed implementation guides for popular third-party services that demonstrate how to build custom asset sources:

### Stock Images[#](#stock-images)

*   **[Unsplash](vue/import-media/from-remote-source/unsplash-8f31f0/)** \- High-quality royalty-free photos with powerful search capabilities
*   **[Pexels](vue/import-media/from-remote-source/pexels-90d5df/)** \- Royalty-free stock photography with curated collections
*   **[Getty Images](vue/import-media/from-remote-source/getty-images-a3931c/)** \- Premium stock photography using a secure proxy server architecture

### Audio Libraries[#](#audio-libraries)

*   **[Soundstripe](vue/import-media/from-remote-source/soundstripe-9a42a9/)** \- Royalty-free music and audio tracks for video projects

Each guide includes working code examples, API authentication setup, and best practices for integrating that specific service.

## Common Integration Patterns[#](#common-integration-patterns)

Most third-party integrations share similar patterns:

*   **Search functionality** - Enable users to search the third-party library
*   **Pagination** - Handle large result sets with infinite scroll or page-based navigation
*   **Asset preview** - Display thumbnails and metadata before importing
*   **Authentication** - Manage API keys securely (client-side or via proxy server)

## Next Steps[#](#next-steps)

Choose the integration guide that matches your needs to see a complete implementation. The patterns shown in these guides can be adapted to integrate virtually any third-party API into CE.SDK.

---



[Source](https:/img.ly/docs/cesdk/vue/import-media/from-remote-source/soundstripe-9a42a9)