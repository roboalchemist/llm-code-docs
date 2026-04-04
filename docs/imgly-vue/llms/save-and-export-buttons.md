# Save and Export Buttons

This guide shows you how to add, customize, and configure save and export buttons in the CE.SDK navigation bar. You’ll learn how to use the Navigation Bar Order API to display built-in action buttons and the Actions API to implement custom save and export workflows.

![Save and Export Buttons](/docs/cesdk/_astro/browser.hero.DFAdDEGz_Z6y62k.webp)

10 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples)[

GitHub](https://github.com/imgly/cesdk-web-examples)

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
/** * Save and Export Buttons Example * * Demonstrates adding save/export buttons to the navigation bar * and overriding their default behavior with custom handlers. */class Example implements EditorPlugin {  name = packageJson.name;  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Design',      withUploadAssetSources: true    });    await cesdk.createDesignScene();
    const engine = cesdk.engine;    const page = engine.block.findByType('page')[0];    const pageWidth = engine.block.getWidth(page);    const pageHeight = engine.block.getHeight(page);
    // Create gradient fill for page background (purple to violet to cyan diagonal)    const gradientFill = engine.block.createFill('gradient/linear');    engine.block.setGradientColorStops(gradientFill, 'fill/gradient/colors', [      { color: { r: 0.388, g: 0.4, b: 0.945, a: 1 }, stop: 0 }, // #6366f1 indigo      { color: { r: 0.545, g: 0.361, b: 0.965, a: 1 }, stop: 0.5 }, // #8b5cf6 violet      { color: { r: 0.024, g: 0.714, b: 0.831, a: 1 }, stop: 1 } // #06b6d4 cyan    ]);    // Diagonal gradient from top-left to bottom-right    engine.block.setFloat(gradientFill, 'fill/gradient/linear/startPointX', 0);    engine.block.setFloat(gradientFill, 'fill/gradient/linear/startPointY', 0);    engine.block.setFloat(gradientFill, 'fill/gradient/linear/endPointX', 1);    engine.block.setFloat(gradientFill, 'fill/gradient/linear/endPointY', 1);    engine.block.setFill(page, gradientFill);
    // Create centered text with title and subtitle    const titleText = engine.block.create('text');    engine.block.appendChild(page, titleText);    engine.block.replaceText(titleText, 'Save and Export Buttons\n\nimg.ly');    engine.block.setWidth(titleText, pageWidth);    engine.block.setHeightMode(titleText, 'Auto');    engine.block.setPositionX(titleText, 0);    engine.block.setPositionY(titleText, pageHeight * 0.35);    engine.block.setEnum(titleText, 'text/horizontalAlignment', 'Center');    engine.block.setFloat(titleText, 'text/fontSize', 24);    engine.block.setTextColor(titleText, { r: 1, g: 1, b: 1, a: 1 });
    // Deselect all blocks for clean hero image    engine.block.findAllSelected().forEach((block) => {      engine.block.setSelected(block, false);    });
    // Select the page to show the page toolbar (looks better in hero)    engine.block.select(page);
    // Override the saveScene action with custom logic    cesdk.actions.register('saveScene', async () => {      // Replace with your backend upload logic      console.trace('saveScene action triggered');      const archive = await cesdk.engine.scene.saveToArchive();      cesdk.utils.downloadFile(archive, 'application/zip');    });
    // Add all save and export buttons to the navigation bar    cesdk.ui.insertNavigationBarOrderComponent('last', {      id: 'ly.img.actions.navigationBar',      children: [        'ly.img.saveScene.navigationBar',        'ly.img.exportImage.navigationBar',
        {          // Override the PDF export button's onClick callback          id: 'ly.img.exportPDF.navigationBar',          onClick: async () => {            const { blobs } = await cesdk.utils.export({              mimeType: 'application/pdf'            });            cesdk.utils.downloadFile(blobs[0], 'application/pdf');            cesdk.ui.showNotification({              message: 'PDF exported successfully!',              type: 'success',              duration: 'short'            });          }        },        'ly.img.exportScene.navigationBar',        'ly.img.exportArchive.navigationBar'      ]    });  }}
export default Example;
```

This guide demonstrates how to add save and export buttons to your CE.SDK editor’s navigation bar and customize their behavior with custom action handlers. Use the built-in actions to get started quickly, then override them to fully fit your workflows.

## Available Save and Export Buttons[#](#available-save-and-export-buttons)

CE.SDK provides several built-in action buttons for the navigation bar. Each button triggers an action when clicked:

| Button ID | Action | Default Behavior |
| --- | --- | --- |
| `ly.img.saveScene.navigationBar` | `saveScene` | Downloads scene as `.scene` file |
| `ly.img.exportImage.navigationBar` | `exportDesign` with PNG | Downloads PNG image |
| `ly.img.exportPDF.navigationBar` | `exportDesign` with PDF | Downloads PDF document |
| `ly.img.exportVideo.navigationBar` | `exportDesign` with MP4 | Downloads MP4 video |
| `ly.img.exportScene.navigationBar` | `exportScene` | Downloads scene file |
| `ly.img.exportArchive.navigationBar` | `exportScene` (archive) | Downloads scene archive |

## Adding Buttons to the Navigation Bar[#](#adding-buttons-to-the-navigation-bar)

Use `cesdk.ui.setNavigationBarOrder()` to configure the navigation bar with save and export buttons. The buttons must be wrapped in the `ly.img.actions.navigationBar` container:

```
// Add all save and export buttons to the navigation barcesdk.ui.insertNavigationBarOrderComponent('last', {  id: 'ly.img.actions.navigationBar',  children: [    'ly.img.saveScene.navigationBar',    'ly.img.exportImage.navigationBar',
```

For complete control over the navigation bar layout, see the [Navigation Bar](vue/user-interface/customization/navigation-bar-4e5d39/) guide which covers `setNavigationBarOrder()` and other customization options.

## Overriding Actions[#](#overriding-actions)

By default, each button triggers a built-in action. To implement custom logic like uploading to a backend, register a custom handler using `cesdk.actions.register()`:

```
// Override the saveScene action with custom logiccesdk.actions.register('saveScene', async () => {  // Replace with your backend upload logic  console.trace('saveScene action triggered');  const archive = await cesdk.engine.scene.saveToArchive();  cesdk.utils.downloadFile(archive, 'application/zip');});
```

The `saveScene` action receives no arguments. Use `cesdk.engine.scene.saveToString()` to serialize the scene, or `cesdk.engine.scene.saveToArchive()` if you need to include referenced assets.

## Overriding Export Buttons[#](#overriding-export-buttons)

Instead of overriding the global `exportDesign` action, you can provide a custom `onClick` callback directly on individual buttons. This approach gives you fine-grained control over each button’s behavior:

```
// Override the PDF export button's onClick callbackid: 'ly.img.exportPDF.navigationBar',onClick: async () => {  const { blobs } = await cesdk.utils.export({    mimeType: 'application/pdf'  });  cesdk.utils.downloadFile(blobs[0], 'application/pdf');  cesdk.ui.showNotification({    message: 'PDF exported successfully!',    type: 'success',    duration: 'short'  });}
```

The `onClick` callback completely replaces the button’s default behavior. Use `cesdk.ui.showNotification()` to display feedback after the export completes. The notification accepts `type` values of `'success'`, `'error'`, `'info'`, `'warning'`, or `'loading'`.

## Troubleshooting[#](#troubleshooting)

### Button Not Appearing[#](#button-not-appearing)

*   Verify the button ID is spelled correctly
*   Ensure buttons are wrapped in the `ly.img.actions.navigationBar` container
*   Check that the scene mode supports the export type (video export requires Video mode)

### Export Produces Empty Result[#](#export-produces-empty-result)

*   Ensure a page exists in the scene
*   Check that the page has visible content
*   Verify export dimensions are valid

### Save Action Not Triggered[#](#save-action-not-triggered)

*   Confirm the `saveScene` action is registered before the button is clicked
*   Check the browser console for errors in your action handler

## API Reference[#](#api-reference)

| Method | Purpose |
| --- | --- |
| `cesdk.actions.register(actionId, callback)` | Register a custom action handler |
| `cesdk.actions.run(actionId, ...args)` | Programmatically trigger a registered action |
| `cesdk.ui.setNavigationBarOrder(order)` | Set the navigation bar component order |
| `cesdk.utils.export(options)` | Export with automatic loading dialog |
| `cesdk.utils.downloadFile(blob, mimeType)` | Download a blob as a file |
| `cesdk.ui.showNotification(notification)` | Display a notification message |
| `cesdk.engine.scene.saveToString()` | Serialize scene to string |

## Next Steps[#](#next-steps)

*   [Navigation Bar](vue/user-interface/customization/navigation-bar-4e5d39/) \- Complete navigation bar customization
*   [Actions](vue/actions-6ch24x/) \- Register and customize action handlers
*   [Export Options](vue/export-save-publish/export/overview-9ed3a8/) \- Export configuration and format options

---



[Source](https:/img.ly/docs/cesdk/vue/user-interface/customization/rearrange-buttons-97022a)