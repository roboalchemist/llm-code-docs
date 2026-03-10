# Add a New Button

Add custom buttons to the CE.SDK editor to trigger actions, control panels, or implement custom workflows.

![Add a New Button example showing theme and favorite toggle buttons in navigation bar](/docs/cesdk/_astro/browser.hero.SYo7VW8-_Er46S.webp)

5 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-user-interface-ui-extensions-add-new-button-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-user-interface-ui-extensions-add-new-button-browser)

CE.SDK provides a component registration system for adding custom UI elements. The builder API ensures buttons match the editor’s look and feel while giving full control over behavior.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';
class Example implements EditorPlugin {  name = 'guides-user-interface-ui-extensions-add-new-button-browser';  version = '1.0.0';
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    const engine = cesdk.engine;
    // Load assets and create scene    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Design',      withUploadAssetSources: true    });    await cesdk.createDesignScene();
    // Setup the page with a gradient background and centered text    const page = engine.block.findByType('page')[0];    if (page) {      // Add gradient background      const gradientFill = engine.block.createFill('gradient/linear');      engine.block.setGradientColorStops(gradientFill, 'fill/gradient/colors', [        { color: { r: 0.15, g: 0.1, b: 0.35, a: 1.0 }, stop: 0 },        { color: { r: 0.4, g: 0.2, b: 0.5, a: 1.0 }, stop: 0.5 },        { color: { r: 0.6, g: 0.3, b: 0.4, a: 1.0 }, stop: 1 }      ]);      engine.block.setFill(page, gradientFill);
      // Add centered text elements      const pageWidth = engine.block.getWidth(page);      const pageHeight = engine.block.getHeight(page);
      // Create title text "Create custom buttons"      const titleText = engine.block.create('text');      engine.block.replaceText(titleText, 'Create custom buttons');      engine.block.setFloat(titleText, 'text/fontSize', 20);      engine.block.setTextColor(titleText, { r: 1.0, g: 1.0, b: 1.0, a: 1.0 });      engine.block.setWidthMode(titleText, 'Auto');      engine.block.setHeightMode(titleText, 'Auto');      engine.block.appendChild(page, titleText);
      // Create "IMG.LY" text      const imglyText = engine.block.create('text');      engine.block.replaceText(imglyText, 'IMG.LY');      engine.block.setFloat(imglyText, 'text/fontSize', 14);      engine.block.setTextColor(imglyText, { r: 1.0, g: 1.0, b: 1.0, a: 1.0 });      engine.block.setWidthMode(imglyText, 'Auto');      engine.block.setHeightMode(imglyText, 'Auto');      engine.block.appendChild(page, imglyText);
      // Get dimensions and center both texts      const titleWidth = engine.block.getFrameWidth(titleText);      const titleHeight = engine.block.getFrameHeight(titleText);      const imglyWidth = engine.block.getFrameWidth(imglyText);      const imglyHeight = engine.block.getFrameHeight(imglyText);
      const spacing = 8;      const totalHeight = titleHeight + spacing + imglyHeight;      const startY = (pageHeight - totalHeight) / 2;
      // Position title text      engine.block.setPositionX(titleText, (pageWidth - titleWidth) / 2);      engine.block.setPositionY(titleText, startY);
      // Position IMG.LY text below title      engine.block.setPositionX(imglyText, (pageWidth - imglyWidth) / 2);      engine.block.setPositionY(imglyText, startY + titleHeight + spacing);    }
    cesdk.ui.registerComponent('theme.toggle', ({ builder }) => {      const isDark = cesdk.ui.getTheme() === 'dark';
      builder.Button('toggle-theme', {        label: 'Dark Mode',        icon: isDark ? '@imgly/ToggleIconOn' : '@imgly/ToggleIconOff',        variant: 'regular',        isActive: isDark,        onClick: () => {          cesdk.ui.setTheme(isDark ? 'light' : 'dark');        }      });    });
    cesdk.ui.registerComponent('favorite.toggle', ({ builder, state }) => {      const { value: isFavorite, setValue: setIsFavorite } = state(        'isFavorite',        false      );
      builder.Button('toggle-favorite', {        label: 'Favorite',        icon: '@imgly/ShapeStar',        variant: 'regular',        isActive: isFavorite,        onClick: () => {          setIsFavorite(!isFavorite);        }      });    });
    cesdk.ui.registerComponent('quick.export', ({ builder }) => {      builder.Button('quick-export', {        label: 'Export',        icon: '@imgly/Download',        variant: 'regular',        onClick: () => {          cesdk.actions.run('exportDesign');        }      });    });
    cesdk.ui.insertNavigationBarOrderComponent('last', 'favorite.toggle');    cesdk.ui.insertNavigationBarOrderComponent('last', 'quick.export');
    cesdk.ui.insertNavigationBarOrderComponent('last', 'theme.toggle');  }}
export default Example;
```

This guide demonstrates adding custom buttons to the navigation bar: a theme toggle, a favorite button with local state, and an export button that triggers a built-in action.

## Register a Button Component[#](#register-a-button-component)

Use `cesdk.ui.registerComponent()` to create the theme toggle button. The render function receives a `builder` object for creating UI elements. Use `cesdk.ui.getTheme()` to read the current theme and `cesdk.ui.setTheme()` to change it.

```
cesdk.ui.registerComponent('theme.toggle', ({ builder }) => {  const isDark = cesdk.ui.getTheme() === 'dark';
  builder.Button('toggle-theme', {    label: 'Dark Mode',    icon: isDark ? '@imgly/ToggleIconOn' : '@imgly/ToggleIconOff',    variant: 'regular',    isActive: isDark,    onClick: () => {      cesdk.ui.setTheme(isDark ? 'light' : 'dark');    }  });});
```

The render function re-runs when relevant state changes. Calling `cesdk.ui.getTheme()` tracks the theme state, so the component automatically re-renders when `setTheme()` is called.

## Use Component State[#](#use-component-state)

For buttons that need to maintain their own state, use the `state()` function provided in the render context. This creates reactive state that persists across re-renders and automatically triggers updates when changed.

```
cesdk.ui.registerComponent('favorite.toggle', ({ builder, state }) => {  const { value: isFavorite, setValue: setIsFavorite } = state(    'isFavorite',    false  );
  builder.Button('toggle-favorite', {    label: 'Favorite',    icon: '@imgly/ShapeStar',    variant: 'regular',    isActive: isFavorite,    onClick: () => {      setIsFavorite(!isFavorite);    }  });});
```

The `state()` function returns an object with `value` (the current state) and `setValue` (a function to update it). When `setValue` is called, the component re-renders with the new value. The `isActive` property provides visual feedback when the button state is active.

## Trigger Built-in Actions[#](#trigger-built-in-actions)

Combine custom buttons with built-in actions to create streamlined workflows. Use `cesdk.actions.run()` to execute registered actions like export, save, or zoom operations.

```
cesdk.ui.registerComponent('quick.export', ({ builder }) => {  builder.Button('quick-export', {    label: 'Export',    icon: '@imgly/Download',    variant: 'regular',    onClick: () => {      cesdk.actions.run('exportDesign');    }  });});
```

The [Actions API](sveltekit/actions-6ch24x/) provides access to built-in operations (`exportDesign`, `saveScene`, `zoom.in`, etc.) and supports custom actions you register yourself.

## Add to the Navigation Bar[#](#add-to-the-navigation-bar)

Use `insertNavigationBarOrderComponent()` to add buttons to the navigation bar. The first argument is a matcher (`'first'`, `'last'`, a number, component ID, or function), and the second is your component ID.

```
cesdk.ui.insertNavigationBarOrderComponent('last', 'theme.toggle');
```

You can add buttons to other UI locations using similar APIs:

| Location | Insert API | Set Order API |
| --- | --- | --- |
| Navigation Bar | `insertNavigationBarOrderComponent()` | `setNavigationBarOrder()` |
| Dock | `insertDockOrderComponent()` | `setDockOrder()` |
| Canvas Menu | `insertCanvasMenuOrderComponent()` | `setCanvasMenuOrder()` |
| Inspector Bar | `insertInspectorBarOrderComponent()` | `setInspectorBarOrder()` |
| Canvas Bar | `insertCanvasBarOrderComponent()` | `setCanvasBarOrder()` |

## Button Properties[#](#button-properties)

The builder’s `Button` method accepts these configuration options:

| Property | Type | Description |
| --- | --- | --- |
| `label` | `string | string[]` | Button text, supports i18n keys |
| `icon` | `CustomIcon` | Icon from the icon set |
| `onClick` | `() => void` | Click handler function |
| `isSelected` | `boolean` | Highlight as selected |
| `isActive` | `boolean` | Show active state styling |
| `isDisabled` | `boolean` | Disable interaction |
| `isLoading` | `boolean` | Show loading indicator |
| `loadingProgress` | `number` | Loading progress (0-1) |
| `color` | `'accent' | 'danger'` | Color variant |
| `variant` | `'regular' | 'plain'` | Style variant |
| `tooltip` | `string | string[]` | Hover tooltip text |
| `shortcut` | `string` | Keyboard shortcut display |

## API Reference[#](#api-reference)

| API | Description |
| --- | --- |
| `registerComponent()` | Register a custom component with a render function |
| `state()` | Create reactive component state that persists across re-renders |
| `insertNavigationBarOrderComponent()` | Insert a component into the navigation bar |
| `getTheme()` | Get the current editor theme (`'light'` or `'dark'`) |
| `setTheme()` | Set the editor theme |
| `actions.run()` | Execute a registered action by ID |
| `actions.list()` | List all available action IDs |

## Next Steps[#](#next-steps)

*   [Register a New Component](sveltekit/user-interface/ui-extensions/register-new-component-b04a04/) — Learn the full component registration API for building complex UI elements
*   [Create a Custom Panel](sveltekit/user-interface/ui-extensions/create-custom-panel-d87b83/) — Build panels with multiple interactive elements
*   [Configure the Panel](sveltekit/user-interface/customization/panel-7ce1ee/) — Control panel visibility and behavior

---



[Source](https:/img.ly/docs/cesdk/sveltekit/user-interface/ui-extensions/add-custom-feature-2a26b6)