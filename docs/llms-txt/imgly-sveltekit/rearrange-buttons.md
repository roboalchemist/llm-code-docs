# Rearrange Buttons

Control the layout of CE.SDK’s UI areas by rearranging, inserting, and removing components using the Ordering APIs. You can customize the navigation bar, canvas menu, canvas bar, dock, and inspector bar to match your application’s workflow.

![Rearrange Buttons Example](/docs/cesdk/_astro/browser.hero.Cjb9JWPa_Z2dOGk2.webp)

10 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples)[

GitHub](https://github.com/imgly/cesdk-web-examples)

CE.SDK provides Ordering APIs to control which components appear in each UI area and in what order. Each area has `get`, `set`, `insert`, `update`, and `remove` methods for flexible customization. Components use identifiers like `'ly.img.undoRedo.navigationBar'`, and you can add separators (`'ly.img.separator'`) and spacers (`'ly.img.spacer'`) to organize groups.

This guide covers getting the current order, setting a complete new order, inserting components at specific positions, updating component properties, removing components, and applying context-specific orderings.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
class Example implements EditorPlugin {  name = packageJson.name;  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    // Get the current navigation bar order    const currentOrder = cesdk.ui.getNavigationBarOrder();    console.log('Current navigation bar order:', currentOrder);
    // Set a custom navigation bar with fewer buttons    cesdk.ui.setNavigationBarOrder([      'ly.img.zoom.navigationBar',      'ly.img.actions.navigationBar',      'ly.img.undoRedo.navigationBar',      'ly.img.spacer',      'ly.img.back.navigationBar'    ]);
    // Remove flip options from the canvas menu    cesdk.ui.removeCanvasMenuOrderComponent('ly.img.flipX.canvasMenu');    cesdk.ui.removeCanvasMenuOrderComponent('ly.img.flipY.canvasMenu');
    // Configure a custom dock with asset library buttons    cesdk.ui.setDockOrder([      {        id: 'ly.img.assetLibrary.dock',        key: 'shapes',        label: 'Shapes',        icon: '@imgly/Shapes',        entries: ['ly.img.vectorpath']      },      'ly.img.separator',      {        id: 'ly.img.assetLibrary.dock',        key: 'images',        label: 'Images',        icon: '@imgly/Image',        entries: ['ly.img.image']      },      {        id: 'ly.img.assetLibrary.dock',        key: 'text',        label: 'Text',        icon: '@imgly/Text',        entries: ['ly.img.text']      }    ]);
    // Insert a separator before the export actions button    cesdk.ui.insertNavigationBarOrderComponent(      'ly.img.actions.navigationBar',      'ly.img.separator',      'before'    );
    // Update a component's properties without changing its position    cesdk.ui.updateDockOrderComponent(      { id: 'ly.img.assetLibrary.dock', key: 'images' },      { label: 'Photos' }    );
    // Set a different canvas menu order for Text edit mode    cesdk.ui.setCanvasMenuOrder(      [        'ly.img.text.bold.canvasMenu',        'ly.img.text.italic.canvasMenu',        'ly.img.separator',        'ly.img.copy.canvasMenu',        'ly.img.paste.canvasMenu',        'ly.img.delete.canvasMenu'      ],      { editMode: 'Text' }    );
    // Load assets and create design scene    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Design',      withUploadAssetSources: true    });    await cesdk.createDesignScene();
    console.log('Rearrange buttons example loaded successfully!');  }}
export default Example;
```

## Understanding UI Areas[#](#understanding-ui-areas)

CE.SDK has five main UI areas you can customize:

*   **Navigation Bar**: Top bar with back, undo/redo, zoom, preview, and export actions
*   **Canvas Menu**: Context menu when right-clicking or long-pressing the canvas
*   **Canvas Bar**: Quick actions at the top or bottom of the canvas
*   **Dock**: Bottom or side panel for asset libraries and tools
*   **Inspector Bar**: Editing controls for the selected block

## Getting the Current Order[#](#getting-the-current-order)

Before rearranging, retrieve the current component arrangement to see what’s available.

```
// Get the current navigation bar orderconst currentOrder = cesdk.ui.getNavigationBarOrder();console.log('Current navigation bar order:', currentOrder);
```

The returned array contains component objects with `id` and optional properties. Common navigation bar components include:

*   `'ly.img.back.navigationBar'` - Back button
*   `'ly.img.undoRedo.navigationBar'` - Undo/redo buttons
*   `'ly.img.zoom.navigationBar'` - Zoom controls
*   `'ly.img.preview.navigationBar'` - Preview button
*   `'ly.img.actions.navigationBar'` - Export actions dropdown
*   `'ly.img.close.navigationBar'` - Close button
*   `'ly.img.title.navigationBar'` - Document title
*   `'ly.img.pageResize.navigationBar'` - Page resize button

## Setting a Complete Order[#](#setting-a-complete-order)

Replace the entire component order by passing an array of component IDs. Components not included in the array will be hidden.

```
// Set a custom navigation bar with fewer buttonscesdk.ui.setNavigationBarOrder([  'ly.img.zoom.navigationBar',  'ly.img.actions.navigationBar',  'ly.img.undoRedo.navigationBar',  'ly.img.spacer',  'ly.img.back.navigationBar']);
```

This creates a streamlined navigation bar with zoom controls and export actions on the left, undo/redo in the middle, a flexible spacer, and the back button pushed to the right.

## Using Separators and Spacers[#](#using-separators-and-spacers)

Use `'ly.img.separator'` to add visual dividers between groups of buttons. Use `'ly.img.spacer'` to create flexible space that pushes components apart. Multiple spacers distribute space evenly.

## Removing Components[#](#removing-components)

Remove specific components without replacing the entire order.

```
// Remove flip options from the canvas menucesdk.ui.removeCanvasMenuOrderComponent('ly.img.flipX.canvasMenu');cesdk.ui.removeCanvasMenuOrderComponent('ly.img.flipY.canvasMenu');
```

The `removeCanvasMenuOrderComponent` method returns an object with the `removed` count and updated `order` array.

## Configuring the Dock[#](#configuring-the-dock)

The dock uses an object format for asset library buttons. Each button specifies its entries, label, and icon.

```
// Configure a custom dock with asset library buttonscesdk.ui.setDockOrder([  {    id: 'ly.img.assetLibrary.dock',    key: 'shapes',    label: 'Shapes',    icon: '@imgly/Shapes',    entries: ['ly.img.vectorpath']  },  'ly.img.separator',  {    id: 'ly.img.assetLibrary.dock',    key: 'images',    label: 'Images',    icon: '@imgly/Image',    entries: ['ly.img.image']  },  {    id: 'ly.img.assetLibrary.dock',    key: 'text',    label: 'Text',    icon: '@imgly/Text',    entries: ['ly.img.text']  }]);
```

When adding multiple asset library buttons, include a unique `key` to distinguish them. The `entries` array specifies which asset sources appear when the button is clicked.

## Inserting at Specific Positions[#](#inserting-at-specific-positions)

Insert components relative to existing ones using matchers and location parameters.

```
// Insert a separator before the export actions buttoncesdk.ui.insertNavigationBarOrderComponent(  'ly.img.actions.navigationBar',  'ly.img.separator',  'before');
```

The third parameter specifies the location: `'before'`, `'after'`, or `'replace'`.

### Matcher Options[#](#matcher-options)

The insert, update, and remove methods accept various matcher types:

*   **String ID**: `'ly.img.duplicate.canvasMenu'` - Matches by component ID
*   **Object**: `{ id: 'ly.img.zoom.navigationBar' }` - Matches by partial properties
*   **Position**: `'first'` or `'last'` - Matches first or last component
*   **Index**: `0`, `1`, `2`, etc. - Matches by position index
*   **Function**: `(component, index) => boolean` - Custom matching logic

## Updating Component Properties[#](#updating-component-properties)

Modify properties of existing components without changing their position.

```
// Update a component's properties without changing its positioncesdk.ui.updateDockOrderComponent(  { id: 'ly.img.assetLibrary.dock', key: 'images' },  { label: 'Photos' });
```

The update can be a partial object with new properties or a function that returns updates based on current values.

## Context-Based Ordering[#](#context-based-ordering)

Apply different orderings for specific edit modes by passing an `orderContext` parameter.

```
// Set a different canvas menu order for Text edit modecesdk.ui.setCanvasMenuOrder(  [    'ly.img.text.bold.canvasMenu',    'ly.img.text.italic.canvasMenu',    'ly.img.separator',    'ly.img.copy.canvasMenu',    'ly.img.paste.canvasMenu',    'ly.img.delete.canvasMenu'  ],  { editMode: 'Text' });
```

Available edit modes include `'Transform'` (default), `'Text'`, `'Crop'`, and others. This lets you show different controls when editing text versus transforming shapes.

## API Reference[#](#api-reference)

| Method | Purpose |
| --- | --- |
| `cesdk.ui.getNavigationBarOrder(orderContext?)` | Get current navigation bar component order |
| `cesdk.ui.setNavigationBarOrder(order, orderContext?)` | Set navigation bar component order |
| `cesdk.ui.insertNavigationBarOrderComponent(matcher, component, location?, orderContext?)` | Insert component into navigation bar |
| `cesdk.ui.updateNavigationBarOrderComponent(matcher, update, orderContext?)` | Update component properties in navigation bar |
| `cesdk.ui.removeNavigationBarOrderComponent(matcher, orderContext?)` | Remove component from navigation bar |
| `cesdk.ui.getCanvasMenuOrder(orderContext?)` | Get current canvas menu component order |
| `cesdk.ui.setCanvasMenuOrder(order, orderContext?)` | Set canvas menu component order |
| `cesdk.ui.insertCanvasMenuOrderComponent(matcher, component, location?, orderContext?)` | Insert component into canvas menu |
| `cesdk.ui.updateCanvasMenuOrderComponent(matcher, update, orderContext?)` | Update component properties in canvas menu |
| `cesdk.ui.removeCanvasMenuOrderComponent(matcher, orderContext?)` | Remove component from canvas menu |
| `cesdk.ui.getCanvasBarOrder(position, orderContext?)` | Get canvas bar order for position (‘top’ or ‘bottom’) |
| `cesdk.ui.setCanvasBarOrder(order, position, orderContext?)` | Set canvas bar order for position |
| `cesdk.ui.getDockOrder(orderContext?)` | Get current dock component order |
| `cesdk.ui.setDockOrder(order, orderContext?)` | Set dock component order |
| `cesdk.ui.insertDockOrderComponent(matcher, component, location?, orderContext?)` | Insert component into dock |
| `cesdk.ui.updateDockOrderComponent(matcher, update, orderContext?)` | Update component properties in dock |
| `cesdk.ui.removeDockOrderComponent(matcher, orderContext?)` | Remove component from dock |
| `cesdk.ui.getInspectorBarOrder(orderContext?)` | Get current inspector bar component order |
| `cesdk.ui.setInspectorBarOrder(order, orderContext?)` | Set inspector bar component order |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/user-interface/customization/panel-7ce1ee)