# To PDF

Export your designs as PDF documents with high compatibility mode and underlayer support for special media printing.

![Export to PDF hero image](/docs/cesdk/_astro/browser.hero.gLoq3CwE_1cunaU.webp)

10 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-export-save-publish-export-to-pdf-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-export-save-publish-export-to-pdf-browser)

PDF provides a universal document format for sharing and printing designs. CE.SDK exports PDF files that preserve vector graphics, support multi-page documents, and include options for print compatibility. You can configure high compatibility mode to ensure consistent rendering across different PDF viewers, and generate underlayers for special media printing like fabric, glass, or DTF transfers.

```
import {  MimeType,  type EditorPlugin,  type EditorPluginContext} from '@cesdk/cesdk-js';import packageJson from './package.json';
/** * CE.SDK Plugin: Export to PDF Guide * * This example demonstrates: * - Exporting designs as PDF documents * - Configuring high compatibility mode for consistent rendering * - Generating underlayers for special media printing * - Controlling output dimensions * - Using the built-in export action */class Example implements EditorPlugin {  name = packageJson.name;
  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    const engine = cesdk.engine;
    // Load a template scene and zoom to fit    await engine.scene.loadFromURL(      'https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene'    );    const page = engine.scene.getCurrentPage();    if (!page) throw new Error('No page found');
    await engine.scene.zoomToBlock(page, { padding: 40 });
    // Register a custom export action with PDF-specific options    cesdk.actions.register('exportDesign', async () => {      // Export the scene block to include all pages in the PDF      const scene = engine.scene.get()!;
      // Merge PDF-specific defaults with provided options      const blob = await engine.block.export(scene, {        mimeType: 'application/pdf',        exportPdfWithHighCompatibility: true      });
      await cesdk.utils.downloadFile(blob, 'application/pdf');    });
    // Configure navigation bar with export buttons using insertNavigationBarOrderComponent    cesdk.ui.insertNavigationBarOrderComponent('last', {      id: 'ly.img.actions.navigationBar',      children: [        {          id: 'ly.img.action.navigationBar',          key: 'export-pdf',          label: 'PDF',          icon: '@imgly/Download',          onClick: async () => {            // Export scene to include all pages in the PDF            const scene = engine.scene.get()!;            // Export scene as PDF (includes all pages)            const pdfBlob = await engine.block.export(scene, {              mimeType: 'application/pdf'            });            // Download using CE.SDK utils            await cesdk.utils.downloadFile(pdfBlob, 'application/pdf');          }        },        {          id: 'ly.img.action.navigationBar',          key: 'export-high-compat',          label: 'High Compat',          icon: '@imgly/Download',          onClick: async () => {            // Export scene to include all pages in the PDF            const scene = engine.scene.get()!;            // Enable high compatibility mode for consistent rendering across PDF viewers            // This rasterizes complex elements like gradients with transparency at scene DPI            const pdfBlob = await engine.block.export(scene, {              mimeType: 'application/pdf',              exportPdfWithHighCompatibility: true            });            await cesdk.utils.downloadFile(pdfBlob, 'application/pdf');          }        },        {          id: 'ly.img.action.navigationBar',          key: 'export-underlayer',          label: 'Underlayer',          icon: '@imgly/Download',          onClick: async () => {            // Export scene to include all pages in the PDF            const scene = engine.scene.get()!;            // Define the underlayer spot color before export            // RGB values (0.8, 0.8, 0.8) provide a preview representation            engine.editor.setSpotColorRGB('RDG_WHITE', 0.8, 0.8, 0.8);
            // Export with underlayer for special media printing            const pdfBlob = await engine.block.export(scene, {              mimeType: 'application/pdf',              exportPdfWithHighCompatibility: true,              exportPdfWithUnderlayer: true,              underlayerSpotColorName: 'RDG_WHITE',              // Negative offset shrinks underlayer to prevent visible edges              underlayerOffset: -2.0            });            await cesdk.utils.downloadFile(pdfBlob, 'application/pdf');          }        },        {          id: 'ly.img.action.navigationBar',          key: 'export-a4',          label: 'A4 @ 300 DPI',          icon: '@imgly/Download',          onClick: async () => {            // Export scene to include all pages in the PDF            const scene = engine.scene.get()!;            // Export with specific dimensions for print output            const pdfBlob = await engine.block.export(scene, {              mimeType: 'application/pdf',              targetWidth: 2480, // A4 at 300 DPI (210mm)              targetHeight: 3508 // A4 at 300 DPI (297mm)            });            await cesdk.utils.downloadFile(pdfBlob, 'application/pdf');          }        },        {          id: 'ly.img.action.navigationBar',          key: 'export-action',          label: 'Export',          icon: '@imgly/Download',          onClick: () => {            // Run built-in export with PDF format            cesdk.actions.run('exportDesign', { mimeType: 'application/pdf' });          }        }      ]    });  }}
export default Example;
```

This guide covers exporting designs to PDF format, configuring high compatibility mode, generating underlayers with spot colors, and controlling output dimensions.

## Export to PDF[#](#export-to-pdf)

Call `engine.block.export()` with `mimeType: 'application/pdf'` to export any block as a PDF document. The method returns a Blob containing the PDF data.

```
// Export scene as PDF (includes all pages)const pdfBlob = await engine.block.export(scene, {  mimeType: 'application/pdf'});
```

Pass the scene ID from `engine.scene.get()` to export all pages as a multi-page PDF. You can also pass a single page ID from `engine.scene.getCurrentPage()` if you only need to export one page.

## Configure High Compatibility Mode[#](#configure-high-compatibility-mode)

Enable `exportPdfWithHighCompatibility` to rasterize complex elements like gradients with transparency at the scene’s DPI. This ensures consistent rendering across all PDF viewers.

```
// Enable high compatibility mode for consistent rendering across PDF viewers// This rasterizes complex elements like gradients with transparency at scene DPIconst pdfBlob = await engine.block.export(scene, {  mimeType: 'application/pdf',  exportPdfWithHighCompatibility: true});
```

Use high compatibility mode when:

*   Designs contain gradients with transparency
*   Effects or blend modes render inconsistently across viewers
*   Maximum compatibility matters more than vector precision

High compatibility mode increases file size because complex elements are converted to raster images rather than remaining as vectors.

## Generate Underlayers for Special Media[#](#generate-underlayers-for-special-media)

Underlayers provide a base ink layer (typically white) for printing on transparent or non-white substrates like fabric, glass, or acrylic. The underlayer sits behind your design elements and provides opacity on transparent materials.

### Define the Underlayer Spot Color[#](#define-the-underlayer-spot-color)

Before exporting, define a spot color that represents the underlayer ink. The RGB values provide a preview representation in PDF viewers.

```
// Define the underlayer spot color before export// RGB values (0.8, 0.8, 0.8) provide a preview representationengine.editor.setSpotColorRGB('RDG_WHITE', 0.8, 0.8, 0.8);
```

The spot color name (e.g., `'RDG_WHITE'`) must match your print provider’s requirements. Common names include `RDG_WHITE` for Roland DG printers and `White` for other systems.

### Export with Underlayer Options[#](#export-with-underlayer-options)

Configure the underlayer spot color name and optional offset. The `underlayerOffset` adjusts the underlayer size in design units—negative values shrink it inward to prevent visible edges from print misalignment (trapping).

```
// Export with underlayer for special media printingconst pdfBlob = await engine.block.export(scene, {  mimeType: 'application/pdf',  exportPdfWithHighCompatibility: true,  exportPdfWithUnderlayer: true,  underlayerSpotColorName: 'RDG_WHITE',  // Negative offset shrinks underlayer to prevent visible edges  underlayerOffset: -2.0});
```

The underlayer is generated automatically from the contours of all design elements on the page. Elements with transparency will have proportionally reduced underlayer opacity.

## Export at Target Dimensions[#](#export-at-target-dimensions)

Use `targetWidth` and `targetHeight` to control the exported PDF dimensions in pixels. The block renders large enough to fill the target size while maintaining aspect ratio.

```
// Export with specific dimensions for print outputconst pdfBlob = await engine.block.export(scene, {  mimeType: 'application/pdf',  targetWidth: 2480, // A4 at 300 DPI (210mm)  targetHeight: 3508 // A4 at 300 DPI (297mm)});
```

For print output, calculate the target dimensions based on your desired DPI:

*   A4 at 300 DPI: 2480 × 3508 pixels
*   Letter at 300 DPI: 2550 × 3300 pixels

## Built-in Export Action[#](#built-in-export-action)

Run the `exportDesign` action to execute the default export flow programmatically.

```
// Run built-in export with PDF formatcesdk.actions.run('exportDesign', { mimeType: 'application/pdf' });
```

This executes the registered export action, which handles the complete export process including format selection and file download.

## Customize Export Action[#](#customize-export-action)

Register a custom `exportDesign` action to apply PDF-specific options automatically. This lets you set defaults like high compatibility mode that apply whenever the export action runs.

```
// Register a custom export action with PDF-specific optionscesdk.actions.register('exportDesign', async () => {  // Export the scene block to include all pages in the PDF  const scene = engine.scene.get()!;
  // Merge PDF-specific defaults with provided options  const blob = await engine.block.export(scene, {    mimeType: 'application/pdf',    exportPdfWithHighCompatibility: true  });
  await cesdk.utils.downloadFile(blob, 'application/pdf');});
```

The custom action merges your PDF defaults with any options passed when the action runs. This approach centralizes export configuration and ensures consistent behavior across your application.

## Download Export[#](#download-export)

Use `cesdk.utils.downloadFile()` to trigger the browser’s download dialog for the exported blob.

```
// Download using CE.SDK utilsawait cesdk.utils.downloadFile(pdfBlob, 'application/pdf');
```

Pass the blob and MIME type to prompt the user to save the file locally.

## PDF Export Options[#](#pdf-export-options)

| Option | Description |
| --- | --- |
| `mimeType` | Output format. Must be `'application/pdf'`. |
| `exportPdfWithHighCompatibility` | Rasterize complex elements at scene DPI for consistent rendering. Defaults to `true`. |
| `exportPdfWithUnderlayer` | Generate an underlayer from design contours. Defaults to `false`. |
| `underlayerSpotColorName` | Spot color name for the underlayer ink. Required when `exportPdfWithUnderlayer` is true. |
| `underlayerOffset` | Size adjustment in design units. Negative values shrink the underlayer inward. |
| `targetWidth` | Target output width in pixels. Must be used with `targetHeight`. |
| `targetHeight` | Target output height in pixels. Must be used with `targetWidth`. |
| `abortSignal` | Signal to cancel the export operation. |

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `engine.block.export(blockId, options)` | Export a block as PDF with format and compatibility options |
| `engine.editor.setSpotColorRGB(name, r, g, b)` | Define a spot color for underlayer ink |
| `engine.scene.get()` | Get the scene for multi-page PDF export |
| `engine.scene.getCurrentPage()` | Get the current page for single-page export |
| `cesdk.actions.run()` | Runs a built-in action like `exportDesign` |
| `cesdk.actions.register()` | Registers a custom action to override default behavior |
| `cesdk.utils.downloadFile()` | Triggers browser download dialog for a blob |

## Next Steps[#](#next-steps)

*   [Export Overview](vue/export-save-publish/export/overview-9ed3a8/) \- Compare all supported export formats
*   [Export for Printing](vue/export-save-publish/for-printing-bca896/) \- Print workflows with DPI and color management
*   [Spot Colors](vue/colors/for-print/spot-c3a150/) \- Define and use spot colors in designs
*   [Export Size Limits](vue/export-save-publish/export/size-limits-6f0695/) \- Check device limits before exporting large designs

---



[Source](https:/img.ly/docs/cesdk/vue/export-save-publish/export/to-mp4-c998a8)