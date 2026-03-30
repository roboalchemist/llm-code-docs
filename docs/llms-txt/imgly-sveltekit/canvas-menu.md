# Canvas Menu

Customize the canvas menu - the context menu that appears when clicking elements on the canvas - to create tailored editing experiences with custom actions and context-specific controls.

![Canvas Menu example showing CE.SDK with customized canvas menu](/docs/cesdk/_astro/browser.hero.DPNLIhMF_iOJCC.webp)

10 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-user-interface-customization-canvas-menu-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-user-interface-customization-canvas-menu-browser)

The canvas menu supports different configurations for different edit modes (Transform, Text, Crop), allowing you to show context-specific controls based on what the user is editing. CE.SDK provides five ordering APIs to get, set, remove, insert, and update components in this menu.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
class Example implements EditorPlugin {  name = packageJson.name;  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    const engine = cesdk.engine;
    // Get the current canvas menu order for Transform mode (default)    const currentOrder = cesdk.ui.getCanvasMenuOrder();    console.log('Canvas menu order:', currentOrder);
    // Get order for a specific edit mode    const textModeOrder = cesdk.ui.getCanvasMenuOrder({ editMode: 'Text' });    console.log('Text mode order:', textModeOrder);
    // Remove a component from the canvas menu    cesdk.ui.removeCanvasMenuOrderComponent('ly.img.placeholder.canvasMenu');
    // Update an existing component to add custom properties    cesdk.ui.updateCanvasMenuOrderComponent('ly.img.delete.canvasMenu', {      variant: 'regular'    });
    // Register a custom component for the canvas menu    cesdk.ui.registerComponent(      'ly.img.download.canvasMenu',      ({ builder, engine }) => {        const selectedBlocks = engine.block.findAllSelected();        const hasSelection = selectedBlocks.length > 0;
        builder.Button('download-button', {          label: 'Download',          icon: '@imgly/Download',          isDisabled: !hasSelection,          onClick: async () => {            if (selectedBlocks.length === 0) return;            const block = selectedBlocks[0];            const blob = await engine.block.export(block, {              mimeType: 'image/png'            });            await cesdk.utils.downloadFile(blob, 'image/png');          }        });      }    );
    // Insert the custom component after duplicate    cesdk.ui.insertCanvasMenuOrderComponent(      'ly.img.duplicate.canvasMenu',      'ly.img.download.canvasMenu',      'after'    );
    // Add a custom action to the options dropdown    cesdk.ui.insertCanvasMenuOrderComponent(      'ly.img.options.canvasMenu',      {        id: 'ly.img.action.canvasMenu',        key: 'export-jpeg',        label: 'Export JPEG',        onClick: async () => {          const selectedBlocks = engine.block.findAllSelected();          if (selectedBlocks.length === 0) return;          const block = selectedBlocks[0];          const blob = await engine.block.export(block, {            mimeType: 'image/jpeg'          });          await cesdk.utils.downloadFile(blob, 'image/jpeg');        }      },      'asChild'    );
    // Set a complete order for Text edit mode    cesdk.ui.setCanvasMenuOrder(      [        'ly.img.text.color.canvasMenu',        'ly.img.text.bold.canvasMenu',        'ly.img.text.italic.canvasMenu',        'ly.img.separator',        'ly.img.delete.canvasMenu'      ],      { editMode: 'Text' }    );
    // Load assets and create scene    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Design',      withUploadAssetSources: true    });    await cesdk.createDesignScene();  }}
export default Example;
```

This guide covers how to retrieve the current order, modify components, insert custom actions, and configure edit mode-specific menus.

## Retrieving the Canvas Menu Order[#](#retrieving-the-canvas-menu-order)

Before making changes, inspect the current canvas menu order. The `cesdk.ui.getCanvasMenuOrder()` method returns an array of component IDs and configurations. Pass an `orderContext` parameter to get orders for specific edit modes.

```
// Get the current canvas menu order for Transform mode (default)const currentOrder = cesdk.ui.getCanvasMenuOrder();console.log('Canvas menu order:', currentOrder);
// Get order for a specific edit modeconst textModeOrder = cesdk.ui.getCanvasMenuOrder({ editMode: 'Text' });console.log('Text mode order:', textModeOrder);
```

The returned order includes built-in components like `ly.img.duplicate.canvasMenu`, `ly.img.delete.canvasMenu`, and layout helpers like `ly.img.separator`.

## Removing Components[#](#removing-components)

Remove components from the canvas menu using `cesdk.ui.removeCanvasMenuOrderComponent()`. The matcher can be a component ID string, index number, ‘first’, ‘last’, a partial object, or a predicate function.

```
// Remove a component from the canvas menucesdk.ui.removeCanvasMenuOrderComponent('ly.img.placeholder.canvasMenu');
```

Removing components only affects the layout. The underlying features remain enabled and accessible through other UI elements or APIs.

## Updating Components[#](#updating-components)

Modify existing components in the order using `cesdk.ui.updateCanvasMenuOrderComponent()`. The update can be a new component ID, partial properties, or an updater function that receives the current component and returns a modified version.

```
// Update an existing component to add custom propertiescesdk.ui.updateCanvasMenuOrderComponent('ly.img.delete.canvasMenu', {  variant: 'regular'});
```

This is useful for replacing default components with custom versions or adjusting component properties without removing and re-inserting.

## Inserting Components[#](#inserting-components)

Add components to the canvas menu using `cesdk.ui.insertCanvasMenuOrderComponent()`. The location parameter accepts ‘before’, ‘after’ (default), ‘replace’, or ‘asChild’.

Before inserting custom functionality, register a component using `cesdk.ui.registerComponent()`:

```
// Register a custom component for the canvas menucesdk.ui.registerComponent(  'ly.img.download.canvasMenu',  ({ builder, engine }) => {    const selectedBlocks = engine.block.findAllSelected();    const hasSelection = selectedBlocks.length > 0;
    builder.Button('download-button', {      label: 'Download',      icon: '@imgly/Download',      isDisabled: !hasSelection,      onClick: async () => {        if (selectedBlocks.length === 0) return;        const block = selectedBlocks[0];        const blob = await engine.block.export(block, {          mimeType: 'image/png'        });        await cesdk.utils.downloadFile(blob, 'image/png');      }    });  });
```

Then insert the registered component at the desired position:

```
// Insert the custom component after duplicatecesdk.ui.insertCanvasMenuOrderComponent(  'ly.img.duplicate.canvasMenu',  'ly.img.download.canvasMenu',  'after');
```

To add components to the options dropdown, use the ‘asChild’ location:

```
// Add a custom action to the options dropdowncesdk.ui.insertCanvasMenuOrderComponent(  'ly.img.options.canvasMenu',  {    id: 'ly.img.action.canvasMenu',    key: 'export-jpeg',    label: 'Export JPEG',    onClick: async () => {      const selectedBlocks = engine.block.findAllSelected();      if (selectedBlocks.length === 0) return;      const block = selectedBlocks[0];      const blob = await engine.block.export(block, {        mimeType: 'image/jpeg'      });      await cesdk.utils.downloadFile(blob, 'image/jpeg');    }  },  'asChild');
```

## Setting a Complete Order[#](#setting-a-complete-order)

Replace the entire canvas menu order using `cesdk.ui.setCanvasMenuOrder()`. Pass an array of component IDs or configurations to define the complete menu structure.

```
// Set a complete order for Text edit modecesdk.ui.setCanvasMenuOrder(  [    'ly.img.text.color.canvasMenu',    'ly.img.text.bold.canvasMenu',    'ly.img.text.italic.canvasMenu',    'ly.img.separator',    'ly.img.delete.canvasMenu'  ],  { editMode: 'Text' });
```

This is useful when you need full control over the menu composition rather than incremental modifications.

## Layout Helpers[#](#layout-helpers)

The canvas menu supports layout helper components for visual organization.

| Component ID | Description |
| --- | --- |
| `ly.img.separator` | Adds a vertical separator. Consecutive separators collapse to one. Separators at start/end or adjacent to spacers are hidden. |

## Edit Mode Context[#](#edit-mode-context)

Different canvas menu orders can be configured for each edit mode by passing an `orderContext` parameter. Transform mode is the default, but you can also configure Text, Crop, and Trim (for video editing) modes separately.

All ordering methods accept an optional `orderContext` parameter with an `editMode` property. This allows you to show relevant controls based on what the user is editing. For example, Text mode can display formatting buttons while Transform mode shows positioning and duplication controls.

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `cesdk.ui.getCanvasMenuOrder(orderContext?)` | Get current canvas menu component order |
| `cesdk.ui.setCanvasMenuOrder(order, orderContext?)` | Set complete canvas menu order |
| `cesdk.ui.updateCanvasMenuOrderComponent(matcher, update, orderContext?)` | Update existing component in order |
| `cesdk.ui.removeCanvasMenuOrderComponent(matcher, orderContext?)` | Remove component from order |
| `cesdk.ui.insertCanvasMenuOrderComponent(matcher, component, location?, orderContext?)` | Insert component at position |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/user-interface/customization/canvas-632c8e)