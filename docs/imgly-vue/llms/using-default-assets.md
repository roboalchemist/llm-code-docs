# Using Default Assets

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
/** * CE.SDK Plugin: Using Default Assets Guide * * Demonstrates loading all asset sources from IMG.LY's CDN using * addLocalAssetSourceFromJSONURI and creating a scene with * a star shape, sticker, and image. */class Example implements EditorPlugin {  name = packageJson.name;
  version = packageJson.version;
  async initialize({ cesdk, engine }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    // Versioned CDN URLs using the SDK package (recommended)    // For production, self-host these assets - see the Serve Assets guide    const PACKAGE_BASE = `https://cdn.img.ly/packages/imgly/cesdk-js/${cesdk.version}/assets`;    const DEFAULT_ASSETS_URL = `${PACKAGE_BASE}/v4/`;    const DEMO_ASSETS_URL = `${PACKAGE_BASE}/demo/v2/`;
    // Load default asset sources (core editor components)    await engine.asset.addLocalAssetSourceFromJSONURI(      `${DEFAULT_ASSETS_URL}ly.img.sticker/content.json`    );    await engine.asset.addLocalAssetSourceFromJSONURI(      `${DEFAULT_ASSETS_URL}ly.img.vectorpath/content.json`    );    await engine.asset.addLocalAssetSourceFromJSONURI(      `${DEFAULT_ASSETS_URL}ly.img.colors.defaultPalette/content.json`    );    await engine.asset.addLocalAssetSourceFromJSONURI(      `${DEFAULT_ASSETS_URL}ly.img.filter.lut/content.json`    );    await engine.asset.addLocalAssetSourceFromJSONURI(      `${DEFAULT_ASSETS_URL}ly.img.filter.duotone/content.json`    );    await engine.asset.addLocalAssetSourceFromJSONURI(      `${DEFAULT_ASSETS_URL}ly.img.effect/content.json`    );    await engine.asset.addLocalAssetSourceFromJSONURI(      `${DEFAULT_ASSETS_URL}ly.img.blur/content.json`    );    await engine.asset.addLocalAssetSourceFromJSONURI(      `${DEFAULT_ASSETS_URL}ly.img.typeface/content.json`    );    await engine.asset.addLocalAssetSourceFromJSONURI(      `${DEFAULT_ASSETS_URL}ly.img.crop.presets/content.json`    );    await engine.asset.addLocalAssetSourceFromJSONURI(      `${DEFAULT_ASSETS_URL}ly.img.page.presets/content.json`    );    await engine.asset.addLocalAssetSourceFromJSONURI(      `${DEFAULT_ASSETS_URL}ly.img.page.presets.video/content.json`    );
    // Load demo asset sources (sample content for testing)    await engine.asset.addLocalAssetSourceFromJSONURI(      `${DEMO_ASSETS_URL}ly.img.image/content.json`    );    await engine.asset.addLocalAssetSourceFromJSONURI(      `${DEMO_ASSETS_URL}ly.img.video/content.json`    );    await engine.asset.addLocalAssetSourceFromJSONURI(      `${DEMO_ASSETS_URL}ly.img.audio/content.json`    );    await engine.asset.addLocalAssetSourceFromJSONURI(      `${DEMO_ASSETS_URL}ly.img.template/content.json`    );    await engine.asset.addLocalAssetSourceFromJSONURI(      `${DEMO_ASSETS_URL}ly.img.video.template/content.json`    );    await engine.asset.addLocalAssetSourceFromJSONURI(      `${DEMO_ASSETS_URL}ly.img.textComponents/content.json`    );
    // Update asset library entries to show the loaded sources in the UI    cesdk.ui.updateAssetLibraryEntry('ly.img.sticker', {      sourceIds: ({ currentIds }) => [        ...new Set([...currentIds, 'ly.img.sticker'])      ]    });    cesdk.ui.updateAssetLibraryEntry('ly.img.vectorpath', {      sourceIds: ({ currentIds }) => [        ...new Set([...currentIds, 'ly.img.vectorpath'])      ]    });    cesdk.ui.updateAssetLibraryEntry('ly.img.colors.defaultPalette', {      sourceIds: ({ currentIds }) => [        ...new Set([...currentIds, 'ly.img.colors.defaultPalette'])      ]    });    cesdk.ui.updateAssetLibraryEntry('ly.img.filter.lut', {      sourceIds: ({ currentIds }) => [        ...new Set([...currentIds, 'ly.img.filter.lut'])      ]    });    cesdk.ui.updateAssetLibraryEntry('ly.img.filter.duotone', {      sourceIds: ({ currentIds }) => [        ...new Set([...currentIds, 'ly.img.filter.duotone'])      ]    });    cesdk.ui.updateAssetLibraryEntry('ly.img.effect', {      sourceIds: ({ currentIds }) => [        ...new Set([...currentIds, 'ly.img.effect'])      ]    });    cesdk.ui.updateAssetLibraryEntry('ly.img.blur', {      sourceIds: ({ currentIds }) => [        ...new Set([...currentIds, 'ly.img.blur'])      ]    });    cesdk.ui.updateAssetLibraryEntry('ly.img.typeface', {      sourceIds: ({ currentIds }) => [        ...new Set([...currentIds, 'ly.img.typeface'])      ]    });    cesdk.ui.updateAssetLibraryEntry('ly.img.crop.presets', {      sourceIds: ({ currentIds }) => [        ...new Set([...currentIds, 'ly.img.crop.presets'])      ]    });    cesdk.ui.updateAssetLibraryEntry('ly.img.page.presets', {      sourceIds: ({ currentIds }) => [        ...new Set([...currentIds, 'ly.img.page.presets'])      ]    });    cesdk.ui.updateAssetLibraryEntry('ly.img.page.presets.video', {      sourceIds: ({ currentIds }) => [        ...new Set([...currentIds, 'ly.img.page.presets.video'])      ]    });    cesdk.ui.updateAssetLibraryEntry('ly.img.image', {      sourceIds: ({ currentIds }) => [        ...new Set([...currentIds, 'ly.img.image'])      ]    });    cesdk.ui.updateAssetLibraryEntry('ly.img.video', {      sourceIds: ({ currentIds }) => [        ...new Set([...currentIds, 'ly.img.video'])      ]    });    cesdk.ui.updateAssetLibraryEntry('ly.img.audio', {      sourceIds: ({ currentIds }) => [        ...new Set([...currentIds, 'ly.img.audio'])      ]    });    cesdk.ui.updateAssetLibraryEntry('ly.img.template', {      sourceIds: ({ currentIds }) => [        ...new Set([...currentIds, 'ly.img.template'])      ]    });    cesdk.ui.updateAssetLibraryEntry('ly.img.video.template', {      sourceIds: ({ currentIds }) => [        ...new Set([...currentIds, 'ly.img.video.template'])      ]    });    cesdk.ui.updateAssetLibraryEntry('ly.img.textComponents', {      sourceIds: ({ currentIds }) => [        ...new Set([...currentIds, 'ly.img.textComponents'])      ]    });
    // Create the design scene    await cesdk.createDesignScene();
    // Get the page to add content to    const pages = engine.block.findByType('page');    const page = pages[0];    if (page == null) return;
    const pageWidth = engine.block.getWidth(page);    const pageHeight = engine.block.getHeight(page);
    // Define the three assets to add: star shape, sticker, and image    const assetsToAdd = [      {        sourceId: 'ly.img.vectorpath',        assetId: '//ly.img.ubq/shapes/star/filled'      },      {        sourceId: 'ly.img.sticker',        assetId: '//ly.img.cesdk.stickers.emoticons/alien'      },      {        sourceId: 'ly.img.image',        assetId: 'ly.img.cesdk.images.samples/sample.1'      }    ];
    // Calculate layout for 3 centered blocks    const blockSize = Math.min(pageWidth, pageHeight) * 0.2;    const spacing = blockSize * 0.3;    const totalWidth =      assetsToAdd.length * blockSize + (assetsToAdd.length - 1) * spacing;    const startX = (pageWidth - totalWidth) / 2;    const centerY = (pageHeight - blockSize) / 2;
    // Create and position each block    for (let i = 0; i < assetsToAdd.length; i++) {      const { sourceId, assetId } = assetsToAdd[i];      const asset = await engine.asset.fetchAsset(sourceId, assetId);
      if (asset != null) {        const block = await engine.asset.apply(sourceId, asset);
        if (block != null) {          engine.block.setWidth(block, blockSize);          engine.block.setHeight(block, blockSize);          engine.block.setPositionX(block, startX + i * (blockSize + spacing));          engine.block.setPositionY(block, centerY);        }      }    }
    // Clear selection for cleaner visual    for (const block of engine.block.findAllSelected()) {      engine.block.setSelected(block, false);    }
    // Open the Elements panel to showcase all loaded asset sources    cesdk.ui.openPanel('//ly.img.panel/assetLibrary', {      payload: {        entries: ['ly.img.image', 'ly.img.vectorpath', 'ly.img.sticker']      }    });  }}
export default Example;
```

Load all asset sources from IMG.LY’s CDN to populate your CE.SDK editor with shapes, stickers, filters, effects, fonts, images, and other media using the Asset API.

![Using Default Assets example showing the CE.SDK editor with a star shape, sticker, and image centered on the canvas](/docs/cesdk/_astro/browser.hero.DUxQNRHE_ZSbHaM.webp)

5 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-import-media-default-assets-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-import-media-default-assets-browser)

CE.SDK provides built-in asset sources for shapes, stickers, filters, effects, fonts, and sample media. This guide demonstrates loading all available asset sources from IMG.LY’s CDN and applying them to create a scene with a star shape, a sticker, and an image.

The IMG.LY CDN is for development and prototyping only. For production, download and self-host assets from your own server. See the [Serve Assets](vue/serve-assets-b0827c/) guide for instructions.

## What Are Default and Demo Assets?[#](#what-are-default-and-demo-assets)

IMG.LY provides two categories of asset sources hosted on the IMG.LY CDN for development and prototyping:

**Default Assets** are core editor components:

| Source ID | Description |
| --- | --- |
| `ly.img.sticker` | Emojis, emoticons, decorations |
| `ly.img.vectorpath` | Shapes: stars, arrows, polygons |
| `ly.img.colors.defaultPalette` | Default color palette |
| `ly.img.filter.lut` | LUT-based color filters |
| `ly.img.filter.duotone` | Duotone color effects |
| `ly.img.effect` | Visual effects |
| `ly.img.blur` | Blur effects |
| `ly.img.typeface` | Font families |
| `ly.img.crop.presets` | Crop presets |
| `ly.img.page.presets` | Page size presets |
| `ly.img.page.presets.video` | Video page presets |

**Demo Assets** are sample content for development:

| Source ID | Description |
| --- | --- |
| `ly.img.image` | Sample images |
| `ly.img.video` | Sample videos |
| `ly.img.audio` | Sample audio tracks |
| `ly.img.template` | Design templates |
| `ly.img.video.template` | Video templates |
| `ly.img.textComponents` | Text component presets |

## Loading Assets from URL[#](#loading-assets-from-url)

Use `addLocalAssetSourceFromJSONURI()` to load an asset source directly from a JSON URL:

```
const baseURL = `https://cdn.img.ly/packages/imgly/cesdk-js/${cesdk.version}/assets/v4/`;await engine.asset.addLocalAssetSourceFromJSONURI(  `${baseURL}ly.img.vectorpath/content.json`);
```

## Versioned CDN URLs[#](#versioned-cdn-urls)

Use the SDK version to construct versioned CDN URLs. This ensures assets are compatible with your SDK version. For production deployments, see the [Serve Assets](vue/serve-assets-b0827c/) guide to self-host assets.

```
// Versioned CDN URLs using the SDK package (recommended)// For production, self-host these assets - see the Serve Assets guideconst PACKAGE_BASE = `https://cdn.img.ly/packages/imgly/cesdk-js/${cesdk.version}/assets`;const DEFAULT_ASSETS_URL = `${PACKAGE_BASE}/v4/`;const DEMO_ASSETS_URL = `${PACKAGE_BASE}/demo/v2/`;
```

## Loading Default Asset Sources[#](#loading-default-asset-sources)

Load a default asset source from the CDN. Repeat this pattern for each source you need:

```
// Load default asset sources (core editor components)await engine.asset.addLocalAssetSourceFromJSONURI(  `${DEFAULT_ASSETS_URL}ly.img.sticker/content.json`);
```

## Loading Demo Asset Sources[#](#loading-demo-asset-sources)

Load a demo asset source from the CDN. Repeat this pattern for each source you need:

```
// Load demo asset sources (sample content for testing)await engine.asset.addLocalAssetSourceFromJSONURI(  `${DEMO_ASSETS_URL}ly.img.image/content.json`);
```

## Updating the Asset Library[#](#updating-the-asset-library)

After loading asset sources, update the asset library entries to display them in the UI. Repeat this pattern for each source:

```
// Update asset library entries to show the loaded sources in the UIcesdk.ui.updateAssetLibraryEntry('ly.img.sticker', {  sourceIds: ({ currentIds }) => [    ...new Set([...currentIds, 'ly.img.sticker'])  ]});
```

## Filtering Assets with Matcher[#](#filtering-assets-with-matcher)

Use the `matcher` option to load only specific assets from a source:

```
const baseURL = `https://cdn.img.ly/packages/imgly/cesdk-js/${cesdk.version}/assets/v4/`;
// Load only star and arrow shapesawait engine.asset.addLocalAssetSourceFromJSONURI(  `${baseURL}ly.img.vectorpath/content.json`,  { matcher: ['*star*', '*arrow*'] });
// Load only emoji stickersawait engine.asset.addLocalAssetSourceFromJSONURI(  `${baseURL}ly.img.sticker/content.json`,  { matcher: ['*emoji*'] });
```

An asset is included if it matches ANY pattern in the array. Patterns support `*` wildcards.

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `engine.asset.addLocalAssetSourceFromJSONURI(contentURI, options?)` | Load an asset source from a JSON URL |

**Parameters for `addLocalAssetSourceFromJSONURI`:**

| Parameter | Type | Description |
| --- | --- | --- |
| `contentURI` | `string` | Full URL to the content.json file |
| `options.matcher` | `string[]` | Optional wildcard patterns to filter assets |

**Returns:** `Promise<string>` — The asset source ID from the JSON

## Next Steps[#](#next-steps)

*   [Serve Assets](vue/serve-assets-b0827c/) — Self-host assets for production deployments
*   [Customize Asset Library](vue/import-media/asset-panel/customize-c9a4de/) — Configure the asset library UI and entries
*   [Asset Library Basics](vue/import-media/asset-panel/basics-f29078/) — Understand asset library structure and concepts
*   [Import From Remote Source](vue/import-media/from-remote-source-b65faf/) — Load assets from external URLs

---



[Source](https:/img.ly/docs/cesdk/vue/import-media/concepts-5e6197)