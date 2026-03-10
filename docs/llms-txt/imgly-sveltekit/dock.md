# Dock

Customize the dock to control which asset libraries appear and how they are organized for your users.

![Dock Customization example showing a customized dock with modified libraries](/docs/cesdk/_astro/browser.hero.BX-kXOhj_ZSl0d8.webp)

10 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-user-interface-customization-dock-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-user-interface-customization-dock-browser)

The dock is the vertical bar on the left side of the editor that provides quick access to asset libraries. You can configure dock appearance, rearrange components, and add or remove library entries programmatically using the Dock Order API.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
/** * Dock Customization Example * * This example demonstrates how to use CE.SDK's Dock Order API to: * - Configure dock appearance (icon size, labels) * - Retrieve the current dock order * - Remove dock components (hide libraries) * - Update existing dock components * - Insert new dock components * - Use separators and spacers for visual organization * - Add custom components to the dock */class Example implements EditorPlugin {  name = packageJson.name;  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    // Load assets and create scene    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Design',      withUploadAssetSources: true    });    await cesdk.createDesignScene();
    // Configure dock appearance with large icons    cesdk.engine.editor.setSetting('dock/iconSize', 'large');    cesdk.engine.editor.setSetting('dock/hideLabels', false);
    // Get the current dock order to see all default components    const currentOrder = cesdk.ui.getDockOrder();    console.log(      'Default dock order:',      currentOrder.map((c) => c.key ?? c.id)    );
    // Remove stickers library from the dock    cesdk.ui.removeDockOrderComponent({ key: 'ly.img.sticker' });
    // Update the image library with a custom label    cesdk.ui.updateDockOrderComponent(      { key: 'ly.img.image' },      { label: 'Photos' }    );
    // Insert a custom featured library after images    cesdk.ui.insertDockOrderComponent(      { key: 'ly.img.image' },      {        id: 'ly.img.assetLibrary.dock',        key: 'custom.featured',        label: 'Featured',        icon: '@imgly/ShapeStar',        entries: ['ly.img.sticker']      },      'after'    );
    // Insert a separator before the upload library    cesdk.ui.insertDockOrderComponent(      { key: 'ly.img.upload' },      { id: 'ly.img.separator' },      'before'    );
    // Register a custom theme toggle component    cesdk.ui.registerComponent('custom.themeToggle', ({ builder }) => {      const currentTheme = cesdk.ui.getTheme();      builder.Button('theme-toggle', {        label: currentTheme === 'dark' ? 'Light Mode' : 'Dark Mode',        icon: '@imgly/Appearance',        onClick: () => {          cesdk.ui.setTheme(currentTheme === 'dark' ? 'light' : 'dark');        }      });    });
    // Add a spacer and the theme toggle at the bottom of the dock    cesdk.ui.insertDockOrderComponent('last', { id: 'ly.img.spacer' }, 'after');    cesdk.ui.insertDockOrderComponent(      'last',      { id: 'custom.themeToggle' },      'after'    );
    // Log the updated dock order    const updatedOrder = cesdk.ui.getDockOrder();    console.log(      'Updated dock order:',      updatedOrder.map((c) => c.key ?? c.id)    );  }}
export default Example;
```

This guide covers configuring dock appearance, retrieving the current dock order, removing and updating dock components, inserting new components, adding custom components, and using layout helpers for visual organization.

## Configuring Dock Appearance[#](#configuring-dock-appearance)

You can configure dock appearance using the editor settings API. Two settings control how dock buttons look:

*   `dock/iconSize` - Sets button icon size to `'large'` (24px) or `'normal'` (16px)
*   `dock/hideLabels` - Shows or hides button labels (`true` to hide, `false` to show)

```
// Configure dock appearance with large iconscesdk.engine.editor.setSetting('dock/iconSize', 'large');cesdk.engine.editor.setSetting('dock/hideLabels', false);
```

## Retrieving the Dock Order[#](#retrieving-the-dock-order)

Use `cesdk.ui.getDockOrder()` to get the current dock configuration. This returns an array of dock components, each with properties like `id`, `key`, `icon`, `label`, and `entries`.

```
// Get the current dock order to see all default componentsconst currentOrder = cesdk.ui.getDockOrder();console.log(  'Default dock order:',  currentOrder.map((c) => c.key ?? c.id));
```

The dock order changes based on the current [edit mode](sveltekit/concepts/edit-modes-1f5b6c/) (`'Transform'` (default), `'Text'`, `'Crop'`, `'Trim'`, or a custom value). All Dock Order APIs accept an optional `orderContext` parameter to specify which mode to configure.

## Removing Dock Components[#](#removing-dock-components)

Use `cesdk.ui.removeDockOrderComponent()` to hide specific libraries from the dock. The matcher parameter locates which component to remove.

```
// Remove stickers library from the dockcesdk.ui.removeDockOrderComponent({ key: 'ly.img.sticker' });
```

Matcher options include:

*   `'first'` or `'last'` - matches the first or last component
*   A number - matches the component at that index
*   A partial object like `{ key: 'ly.img.sticker' }` - matches by properties
*   A function `(component, index) => boolean` - custom matching logic

## Updating Dock Components[#](#updating-dock-components)

Use `cesdk.ui.updateDockOrderComponent()` to modify existing dock components. You can change their label, icon, entries, or other properties.

```
// Update the image library with a custom labelcesdk.ui.updateDockOrderComponent(  { key: 'ly.img.image' },  { label: 'Photos' });
```

The update parameter can be:

*   A partial object with the properties to update
*   A function that receives the current component and returns the updated values

## Inserting Dock Components[#](#inserting-dock-components)

Use `cesdk.ui.insertDockOrderComponent()` to add new dock components. You specify a matcher to find the position, the new component, and optionally the location (`'before'`, `'after'`, or `'replace'`).

```
// Insert a custom featured library after imagescesdk.ui.insertDockOrderComponent(  { key: 'ly.img.image' },  {    id: 'ly.img.assetLibrary.dock',    key: 'custom.featured',    label: 'Featured',    icon: '@imgly/ShapeStar',    entries: ['ly.img.sticker']  },  'after');
```

The following example adds a separator before the upload library for visual organization:

```
// Insert a separator before the upload librarycesdk.ui.insertDockOrderComponent(  { key: 'ly.img.upload' },  { id: 'ly.img.separator' },  'before');
```

## Adding Custom Components[#](#adding-custom-components)

You can register custom components and add them to the dock. Use `cesdk.ui.registerComponent()` to define a component with the builder pattern, then insert it into the dock order. The following example creates a theme toggle button and places it at the bottom of the dock using a spacer:

```
// Register a custom theme toggle componentcesdk.ui.registerComponent('custom.themeToggle', ({ builder }) => {  const currentTheme = cesdk.ui.getTheme();  builder.Button('theme-toggle', {    label: currentTheme === 'dark' ? 'Light Mode' : 'Dark Mode',    icon: '@imgly/Appearance',    onClick: () => {      cesdk.ui.setTheme(currentTheme === 'dark' ? 'light' : 'dark');    }  });});
// Add a spacer and the theme toggle at the bottom of the dockcesdk.ui.insertDockOrderComponent('last', { id: 'ly.img.spacer' }, 'after');cesdk.ui.insertDockOrderComponent(  'last',  { id: 'custom.themeToggle' },  'after');
```

## Setting a Complete Dock Order[#](#setting-a-complete-dock-order)

For full control over the dock, use `cesdk.ui.setDockOrder()` to replace the entire dock order with a custom arrangement:

```
cesdk.ui.setDockOrder([  {    id: 'ly.img.assetLibrary.dock',    key: 'ly.img.image',    icon: '@imgly/Image',    label: 'libraries.ly.img.image.label',    entries: ['ly.img.image'],  },]);
```

## Dock Components Reference[#](#dock-components-reference)

### Layout Helpers[#](#layout-helpers)

| Component ID | Description |
| --- | --- |
| `ly.img.separator` | Adds a small space in the dock to help visual separation. Separators follow special rules: adjacent separators collapse to one, separators at dock edges are hidden, and separators above a spacer are hidden. |
| `ly.img.spacer` | Adds vertical spacing in the dock. Spacers distribute available whitespace evenly. |

### Asset Library Component[#](#asset-library-component)

| Component ID | Description |
| --- | --- |
| `ly.img.assetLibrary.dock` | A button that opens the Asset Library Panel, showing the content of one or more associated asset entries. |

#### Payload Properties[#](#payload-properties)

| Key | Type | Description |
| --- | --- | --- |
| `key` | `string` | Unique identifier within the dock. |
| `label` | `string` | Button label. If a matching I18N key is found, it is localized. |
| `icon` | `CustomIcon` | A URL string pointing to an SVG, a built-in icon ID (see [Icons](sveltekit/user-interface/appearance/icons-679e32/) ), or a callback returning a URL. |
| `entries` | `string[]` | Asset entries shown when the button is pressed. A single entry opens directly; multiple entries show a group overview. |

## Edit Mode Context[#](#edit-mode-context)

The dock order can vary based on the current edit mode. Pass an `orderContext` parameter to configure different dock orders for Transform, Text, Crop, Trim, or custom edit modes:

```
// Set dock order for Text edit modecesdk.ui.setDockOrder(components, { editMode: 'Text' });
// Get dock order for Crop edit modeconst cropOrder = cesdk.ui.getDockOrder({ editMode: 'Crop' });
```

## API Reference[#](#api-reference)

| Method | Purpose |
| --- | --- |
| `cesdk.ui.getDockOrder()` | Get current dock component order |
| `cesdk.ui.setDockOrder()` | Set complete dock component order |
| `cesdk.ui.updateDockOrderComponent()` | Update existing dock components |
| `cesdk.ui.removeDockOrderComponent()` | Remove dock components |
| `cesdk.ui.insertDockOrderComponent()` | Insert new dock components |
| `cesdk.ui.registerComponent()` | Register custom components for dock use |
| `cesdk.engine.editor.setSetting()` | Configure dock appearance settings |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/user-interface/customization/crop-presets-f94f26)