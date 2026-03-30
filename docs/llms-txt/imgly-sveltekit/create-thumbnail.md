# Create Thumbnail

Generate thumbnail preview images from CE.SDK scenes by exporting with target dimensions for galleries and design management.

![Create Thumbnail hero image](/docs/cesdk/_astro/browser.hero.Digz9ahH_AG98A.webp)

5 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-export-save-publish-create-thumbnail-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-export-save-publish-create-thumbnail-browser)

Thumbnails provide visual previews of designs without loading the full editor. Use `engine.block.export()` with `targetWidth` and `targetHeight` options to scale content while maintaining aspect ratio. Supported formats include PNG, JPEG, and WebP.

```
import type CreativeEditorSDK from '@cesdk/cesdk-js';import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
class Example implements EditorPlugin {  name = packageJson.name;
  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    const engine = cesdk.engine;
    await engine.scene.loadFromURL(      'https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene'    );    const page = engine.scene.getCurrentPage();    if (!page) throw new Error('No page found');    await engine.scene.zoomToBlock(page, { padding: 40 });
    // Setup thumbnail export functionality    await this.setupThumbnailActions(cesdk, page);  }
  private async setupThumbnailActions(    cesdk: CreativeEditorSDK,    page: number  ): Promise<void> {    const engine = cesdk.engine;
    // Add thumbnail export buttons to navigation bar    cesdk.ui.insertNavigationBarOrderComponent('last', {      id: 'ly.img.actions.navigationBar',      children: [        {          id: 'ly.img.action.navigationBar',          key: 'export-thumbnail-small',          label: 'Small Thumbnail',          icon: '@imgly/Save',          onClick: async () => {            const blob = await engine.block.export(page, {              mimeType: 'image/jpeg',              targetWidth: 150,              targetHeight: 150,              jpegQuality: 0.8            });
            await cesdk.utils.downloadFile(blob, 'image/jpeg');            console.log(              `✓ Small thumbnail: ${(blob.size / 1024).toFixed(1)} KB`            );          }        },        {          id: 'ly.img.action.navigationBar',          key: 'export-thumbnail-medium',          label: 'Medium Thumbnail',          icon: '@imgly/Save',          onClick: async () => {            const blob = await engine.block.export(page, {              mimeType: 'image/jpeg',              targetWidth: 400,              targetHeight: 300,              jpegQuality: 0.85            });
            await cesdk.utils.downloadFile(blob, 'image/jpeg');            console.log(              `✓ Medium thumbnail: ${(blob.size / 1024).toFixed(1)} KB`            );          }        },        {          id: 'ly.img.action.navigationBar',          key: 'export-thumbnail-png',          label: 'PNG Thumbnail',          icon: '@imgly/Save',          onClick: async () => {            const blob = await engine.block.export(page, {              mimeType: 'image/png',              targetWidth: 400,              targetHeight: 300,              pngCompressionLevel: 6            });
            await cesdk.utils.downloadFile(blob, 'image/png');            console.log(`✓ PNG thumbnail: ${(blob.size / 1024).toFixed(1)} KB`);          }        },        {          id: 'ly.img.action.navigationBar',          key: 'export-thumbnail-webp',          label: 'WebP Thumbnail',          icon: '@imgly/Save',          onClick: async () => {            const blob = await engine.block.export(page, {              mimeType: 'image/webp',              targetWidth: 400,              targetHeight: 300,              webpQuality: 0.8            });
            await cesdk.utils.downloadFile(blob, 'image/webp');            console.log(              `✓ WebP thumbnail: ${(blob.size / 1024).toFixed(1)} KB`            );          }        }      ]    });  }}
export default Example;
```

This guide covers exporting thumbnails at specific dimensions, choosing formats, optimizing quality and file size, and generating multiple thumbnail sizes.

## Export a Thumbnail[#](#export-a-thumbnail)

Call `engine.block.export()` with target dimensions to create a scaled thumbnail. Both `targetWidth` and `targetHeight` must be set together for scaling to work.

```
const blob = await engine.block.export(page, {  mimeType: 'image/jpeg',  targetWidth: 150,  targetHeight: 150,  jpegQuality: 0.8});
```

The block renders large enough to fill the target size while maintaining aspect ratio. If aspect ratios differ, the output extends beyond the target on one axis.

## Choose Thumbnail Format[#](#choose-thumbnail-format)

Select the format via the `mimeType` option based on your needs:

*   **`'image/jpeg'`** — Smaller files, good for photos, no transparency
*   **`'image/png'`** — Lossless quality, supports transparency
*   **`'image/webp'`** — Best compression, modern browsers only

### JPEG Thumbnails[#](#jpeg-thumbnails)

JPEG works well for photographic content. Control file size with `jpegQuality` (0-1, default 0.9). Values between 0.75-0.85 balance quality and size for thumbnails.

```
const blob = await engine.block.export(page, {  mimeType: 'image/jpeg',  targetWidth: 400,  targetHeight: 300,  jpegQuality: 0.85});
```

### PNG Thumbnails[#](#png-thumbnails)

PNG provides lossless quality with transparency support. Control encoding speed vs. file size with `pngCompressionLevel` (0-9, default 5).

```
const blob = await engine.block.export(page, {  mimeType: 'image/png',  targetWidth: 400,  targetHeight: 300,  pngCompressionLevel: 6});
```

### WebP Thumbnails[#](#webp-thumbnails)

WebP offers the best compression for modern browsers. Control quality with `webpQuality` (0-1, default 1.0 for lossless).

```
const blob = await engine.block.export(page, {  mimeType: 'image/webp',  targetWidth: 400,  targetHeight: 300,  webpQuality: 0.8});
```

## Common Thumbnail Sizes[#](#common-thumbnail-sizes)

Standard sizes for different use cases:

| Size | Dimensions | Use Case |
| --- | --- | --- |
| Small | 150×150 | Grid galleries, file browsers |
| Medium | 400×300 | Preview panels, cards |
| Large | 800×600 | Full previews, detail views |

## Optimize Thumbnail Quality[#](#optimize-thumbnail-quality)

Balance quality with file size using format-specific options:

| Format | Option | Range | Default | Notes |
| --- | --- | --- | --- | --- |
| JPEG | `jpegQuality` | 0-1 | 0.9 | Lower = smaller files, visible artifacts |
| PNG | `pngCompressionLevel` | 0-9 | 5 | Higher = smaller files, slower encoding |
| WebP | `webpQuality` | 0-1 | 1.0 | 1.0 = lossless, lower = lossy compression |

For thumbnails, JPEG quality of 0.8 or WebP quality of 0.75-0.85 typically provides good results with small file sizes.

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `engine.block.export(blockId, options)` | Export a block as image with format and dimension options |
| `engine.scene.getCurrentPage()` | Get the current page block ID |
| `cesdk.utils.downloadFile(blob, mimeType)` | Download a blob to the user’s device |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/edit-video/trim-4f688b)