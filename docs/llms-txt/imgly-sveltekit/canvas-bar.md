# Canvas Bar

Customize the Canvas Bar to add, remove, or rearrange components for your specific workflow.

![Canvas Bar customization example showing a customized toolbar above the canvas](/docs/cesdk/_astro/browser.hero.CFSGNAQ3_Z1T72ey.webp)

10 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-user-interface-customization-canvas-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-user-interface-customization-canvas-browser)

The Canvas Bar is a floating toolbar that appears above the canvas, providing quick access to document-level actions like adding pages or opening settings. It can appear at the top or bottom of the canvas, with each position maintaining independent component orders.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
class Example implements EditorPlugin {  name = packageJson.name;  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    // Load assets and create scene first    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Design',      withUploadAssetSources: true    });    await cesdk.createDesignScene();
    // ===== Canvas Bar Customization Examples =====
    // Register custom components before using them in the Canvas Bar    // The component can read properties from its payload for customization    cesdk.ui.registerComponent(      'ly.img.export.canvasBar',      ({ builder, payload }) => {        // Read custom properties from payload with defaults        const label = (payload?.label as string) ?? 'Export';        const icon = (payload?.icon as string) ?? '@imgly/Download';
        builder.Button('ly.img.export.canvasBar.button', {          label,          icon,          onClick: async () => {            // Use the built-in export action            await cesdk.actions.run('exportDesign', {              mimeType: 'image/png'            });          }        });      }    );
    cesdk.ui.registerComponent(      'ly.img.themeSwitcher.canvasBar',      ({ builder }) => {        // Get current theme to show appropriate icon        const currentTheme = cesdk.ui.getTheme();        const isDark = currentTheme === 'dark';
        builder.Button('ly.img.themeSwitcher.canvasBar.button', {          label: isDark ? 'Light Mode' : 'Dark Mode',          icon: isDark ? '@imgly/Sun' : '@imgly/Moon',          onClick: () => {            // Toggle between light and dark themes            const theme = cesdk.ui.getTheme();            cesdk.ui.setTheme(theme === 'dark' ? 'light' : 'dark');          }        });      }    );
    cesdk.ui.registerComponent(      'ly.img.boldText.canvasBar',      ({ builder, engine: eng }) => {        builder.Button('ly.img.boldText.canvasBar.button', {          label: 'Bold',          icon: '@imgly/Bold',          onClick: () => {            const selection = eng.block.findAllSelected();            selection.forEach((blockId) => {              if (eng.block.getType(blockId) === '//ly.img.ubq/text') {                const [currentWeight] = eng.block.getTextFontWeights(blockId);                const newWeight = currentWeight === 'bold' ? 'normal' : 'bold';                eng.block.setTextFontWeight(blockId, newWeight);              }            });          }        });      }    );
    // Register a zoom button for the top bar    cesdk.ui.registerComponent('ly.img.zoomFit.canvasBar', ({ builder }) => {      builder.Button('ly.img.zoomFit.canvasBar.button', {        label: 'Fit Page',        icon: '@imgly/Fit',        onClick: async () => {          const currentPage = cesdk.engine.scene.getCurrentPage();          if (currentPage) {            await cesdk.engine.scene.zoomToBlock(currentPage, {              padding: 40            });          }        }      });    });
    // Register an undo button for the top bar    cesdk.ui.registerComponent('ly.img.undo.canvasBar', ({ builder }) => {      const canUndo = cesdk.engine.editor.canUndo();      builder.Button('ly.img.undo.canvasBar.button', {        label: 'Undo',        icon: '@imgly/Undo',        isDisabled: !canUndo,        onClick: () => {          cesdk.engine.editor.undo();        }      });    });
    // Register a redo button for the top bar    cesdk.ui.registerComponent('ly.img.redo.canvasBar', ({ builder }) => {      const canRedo = cesdk.engine.editor.canRedo();      builder.Button('ly.img.redo.canvasBar.button', {        label: 'Redo',        icon: '@imgly/Redo',        isDisabled: !canRedo,        onClick: () => {          cesdk.engine.editor.redo();        }      });    });
    // Get the current Canvas Bar order for the bottom position    const currentOrder = cesdk.ui.getCanvasBarOrder('bottom');    console.log('Current bottom Canvas Bar order:', currentOrder);
    // Get the order for a specific edit mode    const textModeOrder = cesdk.ui.getCanvasBarOrder('bottom', {      editMode: 'Text'    });    console.log('Text mode Canvas Bar order:', textModeOrder);
    // Insert the registered export button after the settings button    cesdk.ui.insertCanvasBarOrderComponent(      'ly.img.settings.canvasBar',      'ly.img.export.canvasBar',      'bottom',      'after'    );
    // Remove the add page button for a single-page workflow    cesdk.ui.removeCanvasBarOrderComponent(      'ly.img.page.add.canvasBar',      'bottom'    );
    // Update the export button with custom properties    // Components that read from payload can be customized this way    cesdk.ui.updateCanvasBarOrderComponent(      'ly.img.export.canvasBar',      {        label: 'Export PNG',        icon: '@imgly/Image'      },      'bottom'    );
    // Set a completely custom Canvas Bar order for the bottom position    // Reference the registered components by their IDs    // Use spacers on both sides of the theme toggle to center it    cesdk.ui.setCanvasBarOrder(      [        'ly.img.settings.canvasBar',        'ly.img.separator',        'ly.img.export.canvasBar',        'ly.img.spacer',        'ly.img.themeSwitcher.canvasBar',        'ly.img.spacer'      ],      'bottom'    );
    // Also customize the top Canvas Bar with undo/redo and zoom controls    cesdk.ui.setCanvasBarOrder(      [        'ly.img.undo.canvasBar',        'ly.img.redo.canvasBar',        'ly.img.spacer',        'ly.img.zoomFit.canvasBar'      ],      'top'    );
    // Configure different Canvas Bar for Text edit mode    // Reference the registered bold button by its ID    cesdk.ui.setCanvasBarOrder(      [        'ly.img.settings.canvasBar',        'ly.img.separator',        'ly.img.boldText.canvasBar',        'ly.img.spacer',        'ly.img.export.canvasBar'      ],      'bottom',      { editMode: 'Text' }    );
    // Using layout helpers: spacers and separators    const updatedOrder = cesdk.ui.getCanvasBarOrder('bottom');    console.log('Updated bottom Canvas Bar order:', updatedOrder);
    // Insert a separator before the export button    cesdk.ui.insertCanvasBarOrderComponent(      'ly.img.export.canvasBar',      'ly.img.separator',      'bottom',      'before'    );
    // Log final Canvas Bar configuration    const finalOrder = cesdk.ui.getCanvasBarOrder('bottom');    console.log('Final bottom Canvas Bar order:', finalOrder);
    const topOrder = cesdk.ui.getCanvasBarOrder('top');    console.log('Top Canvas Bar order:', topOrder);
    console.log('Canvas Bar customization example loaded successfully!');  }}
export default Example;
```

This guide covers how to retrieve the component order, remove or update existing components, insert new ones, and configure different layouts for each edit mode.

## Retrieving the Canvas Bar Order[#](#retrieving-the-canvas-bar-order)

We can retrieve the current Canvas Bar component order using `cesdk.ui.getCanvasBarOrder()`. This returns an array of component configurations for the specified position.

```
// Get the current Canvas Bar order for the bottom positionconst currentOrder = cesdk.ui.getCanvasBarOrder('bottom');console.log('Current bottom Canvas Bar order:', currentOrder);
// Get the order for a specific edit modeconst textModeOrder = cesdk.ui.getCanvasBarOrder('bottom', {  editMode: 'Text'});console.log('Text mode Canvas Bar order:', textModeOrder);
```

The returned array contains objects with component IDs and any additional configuration. We log both the default Transform mode order and the Text edit mode order to see how they differ.

## Removing Components[#](#removing-components)

We can remove components from the Canvas Bar using `cesdk.ui.removeCanvasBarOrderComponent()`. This is useful for creating focused editing experiences.

```
// Remove the add page button for a single-page workflowcesdk.ui.removeCanvasBarOrderComponent(  'ly.img.page.add.canvasBar',  'bottom');
```

Here we remove the add page button for a single-page document workflow. The matcher can be a component ID string, an index number, `'first'`, `'last'`, a partial object, or a predicate function.

## Updating Components[#](#updating-components)

We can modify existing components using `cesdk.ui.updateCanvasBarOrderComponent()`. This allows changing properties like icons, labels, or click handlers without removing and reinserting.

```
// Update the export button with custom properties// Components that read from payload can be customized this waycesdk.ui.updateCanvasBarOrderComponent(  'ly.img.export.canvasBar',  {    label: 'Export PNG',    icon: '@imgly/Image'  },  'bottom');
```

In this example, we update the custom export button’s label and icon. Custom components that read from their payload can be dynamically updated this way.

## Inserting Components[#](#inserting-components)

We can add new components to the Canvas Bar using `cesdk.ui.insertCanvasBarOrderComponent()`. The method accepts a matcher to find the reference component, the new component to insert, the position, and optionally the location relative to the matched component.

```
// Insert the registered export button after the settings buttoncesdk.ui.insertCanvasBarOrderComponent(  'ly.img.settings.canvasBar',  'ly.img.export.canvasBar',  'bottom',  'after');
```

In this example, we insert a custom export button after the settings button by referencing its component ID. The location options are:

*   `'before'` - Insert before the matched component
*   `'after'` - Insert after the matched component (default)
*   `'replace'` - Replace the matched component

## Setting a Complete Order[#](#setting-a-complete-order)

For complete control over the Canvas Bar, we can replace the entire order using `cesdk.ui.setCanvasBarOrder()`. Pass an array of component IDs.

```
// Set a completely custom Canvas Bar order for the bottom position// Reference the registered components by their IDs// Use spacers on both sides of the theme toggle to center itcesdk.ui.setCanvasBarOrder(  [    'ly.img.settings.canvasBar',    'ly.img.separator',    'ly.img.export.canvasBar',    'ly.img.spacer',    'ly.img.themeSwitcher.canvasBar',    'ly.img.spacer'  ],  'bottom');
// Also customize the top Canvas Bar with undo/redo and zoom controlscesdk.ui.setCanvasBarOrder(  [    'ly.img.undo.canvasBar',    'ly.img.redo.canvasBar',    'ly.img.spacer',    'ly.img.zoomFit.canvasBar'  ],  'top');
```

Here we create a custom Canvas Bar for the bottom position with the settings button, a separator, the export button, spacers, and a theme switcher button.

## Layout Helpers[#](#layout-helpers)

CE.SDK provides two layout helper components to organize Canvas Bar content:

```
// Using layout helpers: spacers and separatorsconst updatedOrder = cesdk.ui.getCanvasBarOrder('bottom');console.log('Updated bottom Canvas Bar order:', updatedOrder);
// Insert a separator before the export buttoncesdk.ui.insertCanvasBarOrderComponent(  'ly.img.export.canvasBar',  'ly.img.separator',  'bottom',  'before');
```

**`ly.img.separator`** adds a vertical divider line with smart rendering rules:

*   Adjacent separators render as one
*   Separators at edges are hidden
*   Separators adjacent to spacers (on the left) are hidden

**`ly.img.spacer`** distributes horizontal space evenly. Multiple spacers share the available space proportionally.

## Edit Mode Context[#](#edit-mode-context)

The content of the Canvas Bar changes based on the current [edit mode](sveltekit/concepts/edit-modes-1f5b6c/) (`'Transform'` (the default), `'Text'`, `'Crop'`, `'Trim'`, or a custom value), so all APIs accept an `orderContext` argument to specify the mode.

Each Canvas Bar position (`'top'` or `'bottom'`) has its own component order. All ordering APIs require a `position` parameter and accept an optional `orderContext` to target specific edit modes.

```
// Configure different Canvas Bar for Text edit mode// Reference the registered bold button by its IDcesdk.ui.setCanvasBarOrder(  [    'ly.img.settings.canvasBar',    'ly.img.separator',    'ly.img.boldText.canvasBar',    'ly.img.spacer',    'ly.img.export.canvasBar'  ],  'bottom',  { editMode: 'Text' });
```

In this example, we configure a different Canvas Bar for Text edit mode that includes a bold button relevant for text editing.

## API Reference[#](#api-reference)

| Method | Purpose |
| --- | --- |
| `cesdk.ui.registerComponent(id, renderFunction)` | Register a custom component |
| `cesdk.ui.getCanvasBarOrder(position, orderContext?)` | Get current component order |
| `cesdk.ui.setCanvasBarOrder(order, position, orderContext?)` | Set complete component order |
| `cesdk.ui.updateCanvasBarOrderComponent(matcher, update, position, orderContext?)` | Update matched components |
| `cesdk.ui.removeCanvasBarOrderComponent(matcher, position, orderContext?)` | Remove matched components |
| `cesdk.ui.insertCanvasBarOrderComponent(matcher, component, position, location?, orderContext?)` | Insert components |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/user-interface/appearance/theming-4b0938)