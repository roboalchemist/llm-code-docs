# To PNG

Export designs to PNG format with lossless quality and optional transparency support.

![Export to PNG example showing CE.SDK with PNG export buttons](/docs/cesdk/_astro/browser.hero.BDk8dEHt_IQeIB.webp)

5 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-conversion-to-png-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-conversion-to-png-browser)

PNG is a lossless image format that preserves image quality and supports transparency. It’s ideal for designs requiring pixel-perfect fidelity, logos, graphics with transparent backgrounds, and any content where quality cannot be compromised.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
class Example implements EditorPlugin {  name = packageJson.name;
  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    const engine = cesdk.engine;
    await engine.scene.loadFromURL(      'https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene'    );    const page = engine.scene.getCurrentPage();    if (!page) throw new Error('No page found');    await engine.scene.zoomToBlock(page, { padding: 40 });
    // Export programmatically using the engine API    const exportProgrammatically = async () => {      const blob = await engine.block.export(page, {        mimeType: 'image/png'      });      await cesdk.utils.downloadFile(blob, 'image/png');    };
    // Export with compression level (0-9)    // Higher values produce smaller files but take longer    const exportWithCompression = async () => {      const blob = await engine.block.export(page, {        mimeType: 'image/png',        pngCompressionLevel: 9      });      await cesdk.utils.downloadFile(blob, 'image/png');    };
    // Export with target dimensions    // The block scales to fill the target while maintaining aspect ratio    const exportWithDimensions = async () => {      const blob = await engine.block.export(page, {        mimeType: 'image/png',        targetWidth: 1920,        targetHeight: 1080      });      await cesdk.utils.downloadFile(blob, 'image/png');    };
    // Trigger the built-in export action    const triggerExportAction = async () => {      await cesdk.actions.run('exportDesign', {        mimeType: 'image/png'      });    };
    // Override the default export action to customize behavior    cesdk.actions.register('exportDesign', async (options) => {      // Use the utils API to export with a loading dialog      const { blobs, options: exportOptions } =        await cesdk.utils.export(options);
      // Custom logic: log the export details      console.log(        `Exported ${blobs.length} file(s) as ${exportOptions.mimeType}`      );
      // Download the exported file      await cesdk.utils.downloadFile(blobs[0], exportOptions.mimeType);    });
    // Add export dropdown to navigation bar    cesdk.ui.insertNavigationBarOrderComponent('last', {      id: 'ly.img.actions.navigationBar',      children: [        {          id: 'ly.img.action.navigationBar',          key: 'export-png',          label: 'Export PNG',          icon: '@imgly/Save',          onClick: exportProgrammatically        },        {          id: 'ly.img.action.navigationBar',          key: 'export-png-action',          label: 'Export PNG (action)',          icon: '@imgly/Save',          onClick: triggerExportAction        },        {          id: 'ly.img.action.navigationBar',          key: 'export-png-compressed',          label: 'Export PNG (compressed)',          icon: '@imgly/Save',          onClick: exportWithCompression        },        {          id: 'ly.img.action.navigationBar',          key: 'export-png-hd',          label: 'Export PNG (HD)',          icon: '@imgly/Save',          onClick: exportWithDimensions        }      ]    });  }}
export default Example;
```

This guide covers how to export designs to PNG, configure export options, and integrate with the built-in export action.

## Export to PNG[#](#export-to-png)

Use `engine.block.export()` to export a design block to PNG. The method returns a Blob containing the image data.

```
// Export programmatically using the engine APIconst exportProgrammatically = async () => {  const blob = await engine.block.export(page, {    mimeType: 'image/png'  });  await cesdk.utils.downloadFile(blob, 'image/png');};
```

## Compression Level[#](#compression-level)

Control the file size versus export speed tradeoff using `pngCompressionLevel`. Valid values are 0-9, where higher values produce smaller files but take longer to export. Since PNG is lossless, image quality remains unchanged.

```
// Export with compression level (0-9)// Higher values produce smaller files but take longerconst exportWithCompression = async () => {  const blob = await engine.block.export(page, {    mimeType: 'image/png',    pngCompressionLevel: 9  });  await cesdk.utils.downloadFile(blob, 'image/png');};
```

The default compression level is 5, providing a good balance between file size and export speed.

## Target Dimensions[#](#target-dimensions)

Resize the output by setting `targetWidth` and `targetHeight`. The block scales to fill the target dimensions while maintaining its aspect ratio.

```
// Export with target dimensions// The block scales to fill the target while maintaining aspect ratioconst exportWithDimensions = async () => {  const blob = await engine.block.export(page, {    mimeType: 'image/png',    targetWidth: 1920,    targetHeight: 1080  });  await cesdk.utils.downloadFile(blob, 'image/png');};
```

## Trigger the Export Action[#](#trigger-the-export-action)

The built-in `exportDesign` action triggers the default export workflow with a loading dialog and automatically downloads the file.

```
// Trigger the built-in export actionconst triggerExportAction = async () => {  await cesdk.actions.run('exportDesign', {    mimeType: 'image/png'  });};
```

## Override the Export Action[#](#override-the-export-action)

Register a custom handler for the `exportDesign` action to customize behavior. This allows you to add custom logic such as uploading to a server or processing the exported file.

```
// Override the default export action to customize behaviorcesdk.actions.register('exportDesign', async (options) => {  // Use the utils API to export with a loading dialog  const { blobs, options: exportOptions } =    await cesdk.utils.export(options);
  // Custom logic: log the export details  console.log(    `Exported ${blobs.length} file(s) as ${exportOptions.mimeType}`  );
  // Download the exported file  await cesdk.utils.downloadFile(blobs[0], exportOptions.mimeType);});
```

The `cesdk.utils.export()` method handles the export with a loading dialog, while `cesdk.utils.downloadFile()` triggers the browser download.

## API Reference[#](#api-reference)

| API | Description |
| --- | --- |
| `engine.block.export(block, options)` | Exports a block to a Blob with the specified options |
| `cesdk.actions.run('exportDesign', options)` | Triggers the default export workflow |
| `cesdk.actions.register('exportDesign', handler)` | Overrides the default export action |
| `cesdk.utils.export(options)` | Exports with a loading dialog, returns `{ blobs, options }` |
| `cesdk.utils.downloadFile(blob, mimeType)` | Downloads a Blob as a file |

## Next Steps[#](#next-steps)

*   [Conversion Overview](sveltekit/conversion/overview-44dc58/) \- Learn about other export formats
*   [Export Overview](sveltekit/export-save-publish/export/overview-9ed3a8/) \- Understand the full export workflow
*   [To PDF](sveltekit/conversion/to-pdf-eb937f/) \- Export designs to PDF format

---



[Source](https:/img.ly/docs/cesdk/sveltekit/conversion/to-pdf-eb937f)