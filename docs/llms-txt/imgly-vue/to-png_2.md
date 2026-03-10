# To PNG

Export your designs as PNG images with full transparency support and configurable compression.

![Export to PNG hero image](/docs/cesdk/_astro/browser.hero.BDk8dEHt_IQeIB.webp)

5 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-export-save-publish-export-to-png-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-export-save-publish-export-to-png-browser)

PNG (Portable Network Graphics) provides lossless compression with full alpha channel support. It’s ideal for web graphics, UI elements, and content requiring crisp edges or transparency.

```
import type CreativeEditorSDK from '@cesdk/cesdk-js';import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
class Example implements EditorPlugin {  name = packageJson.name;
  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    const engine = cesdk.engine;
    await engine.scene.loadFromURL(      'https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene'    );    const page = engine.scene.getCurrentPage();    if (!page) throw new Error('No page found');    await engine.scene.zoomToBlock(page, { padding: 40 });
    // Setup export functionality    await this.setupExportActions(cesdk, page);  }
  private async setupExportActions(    cesdk: CreativeEditorSDK,    page: number  ): Promise<void> {    const engine = cesdk.engine;
    // Add export button to navigation bar    cesdk.ui.insertNavigationBarOrderComponent('last', {      id: 'ly.img.actions.navigationBar',      children: [        {          id: 'ly.img.action.navigationBar',          key: 'export-design',          label: 'Export PNG',          icon: '@imgly/Save',          onClick: async () => {            const blob = await engine.block.export(page, {              mimeType: 'image/png'            });
            await cesdk.utils.downloadFile(blob, 'image/png');          }        },        {          id: 'ly.img.action.navigationBar',          key: 'export-design',          label: 'Export PNG (default)',          icon: '@imgly/Save',          onClick: () => cesdk.actions.run('exportDesign')        },        {          id: 'ly.img.action.navigationBar',          key: 'export-design',          label: 'Export PNG (compressed)',          icon: '@imgly/Save',          onClick: async () => {            // Export with compression            const compressedBlob = await engine.block.export(page, {              mimeType: 'image/png',              pngCompressionLevel: 9            });
            await cesdk.utils.downloadFile(compressedBlob, 'image/png');          }        },        {          id: 'ly.img.action.navigationBar',          key: 'export-design',          label: 'Export PNG (hd)',          icon: '@imgly/Save',          onClick: async () => {            const hdBlob = await engine.block.export(page, {              mimeType: 'image/png',              targetWidth: 1920,              targetHeight: 1080            });
            await cesdk.utils.downloadFile(hdBlob, 'image/png');          }        }      ]    });  }}
export default Example;
```

This guide covers exporting designs to PNG, configuring compression, controlling output dimensions, and using built-in export actions.

## Export to PNG[#](#export-to-png)

Call `engine.block.export()` with `mimeType: 'image/png'` to export any block as a PNG image. The method returns a Blob containing the image data.

```
const blob = await engine.block.export(page, {  mimeType: 'image/png'});
```

Pass the page ID from `engine.scene.getCurrentPage()` or any block ID to export specific elements.

## Export Options[#](#export-options)

PNG export supports several configuration options for compression, dimensions, and text rendering.

### Compression Level[#](#compression-level)

The `pngCompressionLevel` option (0-9) controls file size vs. encoding speed. Higher values produce smaller files but take longer to encode. PNG compression is lossless, so quality remains unchanged.

```
const compressedBlob = await engine.block.export(page, {  mimeType: 'image/png',  pngCompressionLevel: 9});
```

*   **0**: No compression, fastest encoding
*   **5**: Balanced (default)
*   **9**: Maximum compression, slowest encoding

### Target Dimensions[#](#target-dimensions)

Use `targetWidth` and `targetHeight` together to export at specific dimensions. The block renders large enough to fill the target size while maintaining aspect ratio.

```
const hdBlob = await engine.block.export(page, {  mimeType: 'image/png',  targetWidth: 1920,  targetHeight: 1080});
```

If the target aspect ratio differs from the block’s aspect ratio, the output extends beyond the target on one axis to preserve proportions.

### All PNG Export Options[#](#all-png-export-options)

| Option | Description |
| --- | --- |
| `mimeType` | Output format. Defaults to `'image/png'`. |
| `pngCompressionLevel` | Compression level (0-9). Higher values produce smaller files but take longer to encode. Quality is unaffected. Defaults to `5`. |
| `targetWidth` | Target output width in pixels. Must be used with `targetHeight`. |
| `targetHeight` | Target output height in pixels. Must be used with `targetWidth`. |
| `allowTextOverhang` | When `true`, text blocks with glyphs extending beyond their frame export with full glyph bounds visible. Defaults to `false`. |
| `abortSignal` | Signal to cancel the export operation. |

## Built-in Export Action[#](#built-in-export-action)

CE.SDK provides a built-in `exportDesign` action that handles export with a progress dialog and automatic download. Trigger it with `cesdk.actions.run()`:

```
onClick: () => cesdk.actions.run('exportDesign')
```

The built-in action exports the current page as PNG and prompts the user to download the result. Add an export button to the navigation bar to let users trigger this action from the UI.

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `engine.block.export(blockId, options)` | Export a block as PNG with format and quality options |
| `cesdk.actions.run('exportDesign')` | Run the built-in export action with progress dialog |
| `cesdk.utils.downloadFile(blob, mimeType)` | Download a blob to the user’s device |

## Next Steps[#](#next-steps)

*   [Export Overview](vue/export-save-publish/export/overview-9ed3a8/) \- Compare all supported export formats
*   [Export Size Limits](vue/export-save-publish/export/size-limits-6f0695/) \- Check device limits before exporting large designs
*   [Export with Color Mask](vue/export-save-publish/export/with-color-mask-4f868f/) \- Remove specific colors and generate alpha masks
*   [Partial Export](vue/export-save-publish/export/partial-export-89aaf6/) \- Export specific blocks or regions

---



[Source](https:/img.ly/docs/cesdk/vue/export-save-publish/export/to-pdf-95e04b)