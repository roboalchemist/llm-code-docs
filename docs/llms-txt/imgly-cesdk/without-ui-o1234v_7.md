# Source: https://img.ly/docs/cesdk/svelte/get-started/without-ui-o1234v/

---
title: "Vanilla JS Without UI (headless)"
description: "Using CE.SDK in Vanilla JS without a UI (Headless Engine Mode)"
platform: svelte
url: "https://img.ly/docs/cesdk/svelte/get-started/without-ui-o1234v/"
---

> This is one page of the CE.SDK Svelte documentation. For a complete overview, see the [Svelte Documentation Index](https://img.ly/docs/cesdk/svelte.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/svelte/llms-full.txt).

---

This guide shows you how to use CE.SDK's headless engine for programmatic content creation without a UI. You'll install the engine, initialize it, and create content through code. By the end, you'll be able to generate images and videos programmatically.

## Install CE.SDK Engine

<Tabs syncKey="package-manager">
  <TabItem label="npm">
    ```bash
    npm install @cesdk/engine
    ```
  </TabItem>

  <TabItem label="pnpm">
    ```bash
    pnpm add @cesdk/engine
    ```
  </TabItem>

  <TabItem label="yarn">
    ```bash
    yarn add @cesdk/engine
    ```
  </TabItem>

  <TabItem label="CDN">
    ```javascript
    import CreativeEngine from 'https://cdn.img.ly/packages/imgly/cesdk-engine/$UBQ_VERSION$/index.js';
    ```
  </TabItem>
</Tabs>

## Initialize the Engine

Initialize the engine and create content programmatically:

```typescript
const config = {
  license: 'YOUR_CESDK_LICENSE_KEY',
  userId: 'your-user-id',
};

const engine = await CreativeEngine.init(config);

// Create a scene programmatically
const scene = await engine.scene.create();

// Add blocks and manipulate content
const page = engine.block.create('page');
engine.block.setWidth(page, 800);
engine.block.setHeight(page, 600);
engine.block.appendChild(scene, page);

// Clean up
engine.dispose();
```

> **Note:** Learn more about programmatic content creation in the [Engine documentation](/js/engine/quickstart-a5d57f/).

## Key Features

The headless engine provides full access to CE.SDK's capabilities without rendering a UI:

- **Programmatic Scene Creation** - Build designs entirely through code
- **Server-Side Rendering** - Generate images and videos on the server
- **Batch Processing** - Automate content generation at scale
- **Asset Management** - Load and manipulate images, videos, and fonts
- **Export Capabilities** - Export to PNG, JPEG, PDF, MP4, and more

## API Reference

| Method                       | Description                                                |
| ---------------------------- | ---------------------------------------------------------- |
| `CreativeEngine.init()`      | Initializes the headless engine for programmatic creation |
| `engine.scene.create()`      | Creates a new scene programmatically                       |
| `engine.block.create()`      | Creates a new block of the specified type                  |
| `engine.block.setWidth()`    | Sets the width of a block                                  |
| `engine.block.setHeight()`   | Sets the height of a block                                 |
| `engine.block.appendChild()` | Adds a block as a child of another block                   |
| `engine.dispose()`           | Cleans up engine resources and releases memory             |

## Next Steps

- **[Engine Quickstart](/js/engine/quickstart-a5d57f/)** - Learn more about programmatic content creation
- **[Block API Guide](/js/engine/guides/blocks-a96ed5/)** - Understand blocks and the scene hierarchy
- **[Export Guide](/js/engine/guides/export-46afeb/)** - Learn about export formats and configuration



---

## More Resources

- **[Svelte Documentation Index](https://img.ly/docs/cesdk/svelte.md)** - Browse all Svelte documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/svelte/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/svelte/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
