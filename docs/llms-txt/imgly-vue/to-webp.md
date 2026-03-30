# To WebP

Export designs to WebP format for optimized web delivery with smaller file sizes than PNG or JPEG.

![Export to WebP showing the editor with export options](/docs/cesdk/_astro/browser.hero.bjzJKu7j_hgHtH.webp)

5 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-export-save-publish-export-to-webp-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-export-save-publish-export-to-webp-browser)

WebP delivers smaller file sizes than PNG and JPEG while preserving image quality and transparency support.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
/** * CE.SDK Plugin: Export to WebP Guide * * Demonstrates exporting designs to WebP format with: * - Built-in export action triggered programmatically * - Three export buttons showcasing different quality presets * - Lossy, lossless, and social media export options */class Example implements EditorPlugin {  name = packageJson.name;
  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required');    }
    const engine = cesdk.engine;
    // Load template and zoom to fit    await engine.scene.loadFromURL(      'https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene'    );    const page = engine.scene.getCurrentPage();    if (!page) throw new Error('No page found');
    await engine.scene.zoomToBlock(page, { padding: 40 });
    // Three export buttons with different WebP settings    cesdk.ui.insertNavigationBarOrderComponent('last', {      id: 'ly.img.actions.navigationBar',      children: [        {          id: 'ly.img.action.navigationBar',          key: 'webp-lossy',          label: 'Lossy',          icon: '@imgly/Download',          onClick: async () => {            const p = engine.scene.getCurrentPage()!;            // Export with lossy compression            const blob = await engine.block.export(p, {              mimeType: 'image/webp',              webpQuality: 0.8            });            // Download using CE.SDK utils            await cesdk.utils.downloadFile(blob, 'image/webp');          }        },        {          id: 'ly.img.action.navigationBar',          key: 'webp-lossless',          label: 'Lossless',          icon: '@imgly/Download',          onClick: async () => {            const p = engine.scene.getCurrentPage()!;            const blob = await engine.block.export(p, {              mimeType: 'image/webp',              webpQuality: 1.0            });            await cesdk.utils.downloadFile(blob, 'image/webp');          }        },        {          id: 'ly.img.action.navigationBar',          key: 'webp-social',          label: 'Social',          icon: '@imgly/Download',          onClick: async () => {            const p = engine.scene.getCurrentPage()!;            // Export with target dimensions for social media            const blob = await engine.block.export(p, {              mimeType: 'image/webp',              webpQuality: 0.9,              targetWidth: 1200,              targetHeight: 630            });            await cesdk.utils.downloadFile(blob, 'image/webp');          }        },        {          id: 'ly.img.action.navigationBar',          key: 'export-action',          label: 'Export',          icon: '@imgly/Download',          onClick: () => {            // Run built-in export with WebP format            cesdk.actions.run('exportDesign', { mimeType: 'image/webp' });          }        }      ]    });  }}
export default Example;
```

This guide covers exporting to WebP, configuring quality settings, and triggering downloads.

## Export to WebP[#](#export-to-webp)

Call `engine.block.export()` with `mimeType: 'image/webp'` and a `webpQuality` value between 0 and 1.

```
// Export with lossy compressionconst blob = await engine.block.export(p, {  mimeType: 'image/webp',  webpQuality: 0.8});
```

The `webpQuality` parameter controls compression. A value of 0.8 provides a good balance between file size and visual quality for most use cases.

## Export Options[#](#export-options)

WebP export supports these options:

| Option | Type | Description |
| --- | --- | --- |
| `mimeType` | `'image/webp'` | Required. Specifies WebP format |
| `webpQuality` | `number` | Quality from 0 to 1. Default 1.0 (lossless) |
| `targetWidth` | `number` | Optional resize width |
| `targetHeight` | `number` | Optional resize height |

Combine `targetWidth` and `targetHeight` to resize the output, useful for social media or thumbnail generation.

```
// Export with target dimensions for social mediaconst blob = await engine.block.export(p, {  mimeType: 'image/webp',  webpQuality: 0.9,  targetWidth: 1200,  targetHeight: 630});
```

Set `webpQuality` to 1.0 for lossless compression when pixel-perfect output is required.

## Built-in Export Action[#](#built-in-export-action)

Run the `exportDesign` action to execute the default export flow programmatically.

```
// Run built-in export with WebP formatcesdk.actions.run('exportDesign', { mimeType: 'image/webp' });
```

This executes the registered export action, which handles the complete export process including format selection and file download.

## Download Export[#](#download-export)

Use `cesdk.utils.downloadFile()` to trigger the browser’s download dialog for the exported blob.

```
// Download using CE.SDK utilsawait cesdk.utils.downloadFile(blob, 'image/webp');
```

Pass the blob and MIME type to prompt the user to save the file locally.

WebP is supported in all modern browsers. For older browsers, consider PNG or JPEG as fallback formats.

## API Reference[#](#api-reference)

| API | Description |
| --- | --- |
| `engine.block.export()` | Exports a block to an image blob with format and quality options |
| `cesdk.actions.run()` | Runs a built-in action like `exportDesign` |
| `cesdk.utils.downloadFile()` | Triggers browser download dialog for a blob |

## Next Steps[#](#next-steps)

[Export Overview](vue/export-save-publish/export/overview-9ed3a8/) \- Learn about all supported export formats and their options.

[Export to PDF](vue/export-save-publish/export/to-pdf-95e04b/) \- Generate print-ready PDF documents from your designs.

[Size Limits](vue/export-save-publish/export/size-limits-6f0695/) \- Understand export size constraints and optimization strategies.

[Partial Export](vue/export-save-publish/export/partial-export-89aaf6/) \- Export specific blocks or regions instead of the full design.

---



[Source](https:/img.ly/docs/cesdk/vue/export-save-publish/export/to-raw-data-abd7da)