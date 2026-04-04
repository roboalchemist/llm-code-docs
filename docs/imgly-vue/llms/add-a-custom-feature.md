# Add a Custom Feature

Bundle custom functionality into reusable plugins for CE.SDK.

![Add a Custom Feature example showing CE.SDK with a custom canvas menu button](/docs/cesdk/_astro/browser.hero.BAOqBpZ7_m1uCE.webp)

10 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-user-interface-ui-extensions-add-custom-feature-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-user-interface-ui-extensions-add-custom-feature-browser)

Plugins provide a structured way to package UI components, event handlers, actions, and configuration into a single unit. While you can customize CE.SDK without plugins by calling APIs directly after initialization, plugins help organize code for sharing across projects or publishing for others to use.

**Do I Need to Create a Plugin to Customize the Editor?**

**Short answer: No.** Keep in mind that you neither have to create a plugin to customize the CE.SDK, nor do you have to publish it. Feel free to use all APIs directly after initializing the CE.SDK. This is completely fine. Even if you decide to bundle everything into a plugin, you can still keep it private and use it only for your own integration.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';
interface CustomFeaturePluginConfig {  ui?: {    locations?: ('canvasMenu' | 'inspectorBar')[];  };}
const DEFAULT_CONFIG: CustomFeaturePluginConfig = {  ui: {    locations: []  }};
const CustomFeaturePlugin = (  userConfig: CustomFeaturePluginConfig = {}): EditorPlugin => {  // Merge user config with defaults  const config: CustomFeaturePluginConfig = {    ...DEFAULT_CONFIG,    ui: {      ...DEFAULT_CONFIG.ui,      ...userConfig.ui    }  };
  return {    name: 'CustomFeaturePlugin',    version: '1.0.0',
    async initialize({ cesdk, engine }: EditorPluginContext): Promise<void> {      if (!cesdk) {        console.log('Plugin initialized in engine-only mode');        return;      }
      console.log('CustomFeaturePlugin initialized');
      // Load default assets and create a design scene      await cesdk.addDefaultAssetSources();      await cesdk.addDemoAssetSources({        sceneMode: 'Design',        withUploadAssetSources: true      });      await cesdk.createDesignScene();
      const page = engine.block.findByType('page')[0];      if (page) {        // Set page dimensions        engine.block.setWidth(page, 800);        engine.block.setHeight(page, 600);
        // Create gradient background fill        const gradientFill = engine.block.createFill('gradient/linear');        engine.block.setGradientColorStops(gradientFill, 'fill/gradient/colors', [          { color: { r: 0.1, g: 0.1, b: 0.2, a: 1.0 }, stop: 0 },          { color: { r: 0.3, g: 0.2, b: 0.5, a: 1.0 }, stop: 0.5 },          { color: { r: 0.1, g: 0.3, b: 0.4, a: 1.0 }, stop: 1 }        ]);        engine.block.setFloat(gradientFill, 'fill/gradient/linear/startPointX', 0);        engine.block.setFloat(gradientFill, 'fill/gradient/linear/startPointY', 0);        engine.block.setFloat(gradientFill, 'fill/gradient/linear/endPointX', 1);        engine.block.setFloat(gradientFill, 'fill/gradient/linear/endPointY', 1);        engine.block.setFill(page, gradientFill);
        // Create centered "IMG.LY" text        const textBlock = engine.block.create('text');        engine.block.replaceText(textBlock, 'IMG.LY');        engine.block.setTextFontSize(textBlock, 80);        engine.block.setTextColor(textBlock, { r: 1.0, g: 1.0, b: 1.0, a: 1.0 });        engine.block.setWidthMode(textBlock, 'Auto');        engine.block.setHeightMode(textBlock, 'Auto');        engine.block.appendChild(page, textBlock);
        // Center the text on the page        const pageWidth = engine.block.getWidth(page);        const pageHeight = engine.block.getHeight(page);        const textWidth = engine.block.getFrameWidth(textBlock);        const textHeight = engine.block.getFrameHeight(textBlock);        engine.block.setPositionX(textBlock, (pageWidth - textWidth) / 2);        engine.block.setPositionY(textBlock, (pageHeight - textHeight) / 2);
        // Select the text block to show the canvas menu        engine.block.select(textBlock);
        engine.block.findAllSelected().forEach(b => engine.block.setSelected(b, false));        engine.block.setSelected(engine.scene.getCurrentPage(), true);      }
      // Register a custom button component      cesdk.ui.registerComponent(        'customFeaturePlugin.action.canvasMenu',        (context) => {          context.builder.Button('custom-action', {            label: 'Custom Action',            icon: '@imgly/Apps',            onClick: () => {              cesdk.ui.showNotification({                message: 'Custom action triggered!',                type: 'success',                duration: 'short'              });              console.log('Custom action executed');            }          });        }      );
      // Only add to canvas menu if configured      const locations = config.ui?.locations ?? [];      if (locations.includes('canvasMenu')) {        const currentOrder = cesdk.ui.getCanvasMenuOrder();        cesdk.ui.setCanvasMenuOrder([          'customFeaturePlugin.action.canvasMenu',          ...currentOrder        ]);        console.log('Custom action added to canvas menu');      }
      // Subscribe to block events for demonstration      const unsubscribe = engine.event.subscribe([], (events) => {        events.forEach((event) => {          if (event.type === 'Created') {            console.log(`Block created: ${event.block}`);          }        });      });
      // Store unsubscribe for potential cleanup      (window as any).unsubscribeCustomFeature = unsubscribe;    }  };};
export default CustomFeaturePlugin;
```

This guide covers creating plugins with the factory function pattern, registering custom components during initialization, and letting integrators control where your plugin’s UI elements appear.

## Plugin Types[#](#plugin-types)

Two plugin interfaces exist: `EditorPlugin` for full editor integration and `EnginePlugin` for headless engine use. Editor plugins receive both `cesdk` and `engine` in their context; engine plugins receive only `engine`. Structure your plugins to handle both contexts for maximum flexibility.

## Creating a Plugin[#](#creating-a-plugin)

### The Plugin Interface[#](#the-plugin-interface)

Plugins implement an interface with `name`, `version`, and `initialize` properties. The `initialize` method executes when you call `cesdk.addPlugin()` or `engine.addPlugin()`. Return a promise from `initialize` for async setup operations.

```
const CustomFeaturePlugin = (  userConfig: CustomFeaturePluginConfig = {}): EditorPlugin => {  // Merge user config with defaults  const config: CustomFeaturePluginConfig = {    ...DEFAULT_CONFIG,    ui: {      ...DEFAULT_CONFIG.ui,      ...userConfig.ui    }  };
  return {    name: 'CustomFeaturePlugin',    version: '1.0.0',
    async initialize({ cesdk, engine }: EditorPluginContext): Promise<void> {
```

### Adding a Plugin to the Editor[#](#adding-a-plugin-to-the-editor)

Call `cesdk.addPlugin()` after creating the editor instance. Pass a plugin object directly or call a factory function that returns one.

```
// Add the plugin with configurationawait cesdk.addPlugin(  CustomFeaturePlugin({    ui: {      locations: ['canvasMenu']    }  }));
```

## Making Plugins Configurable[#](#making-plugins-configurable)

### The Factory Function Pattern[#](#the-factory-function-pattern)

Export a function that returns the plugin object rather than the object directly. This allows integrators to pass configuration options. Even without current configuration needs, this pattern prevents breaking changes when adding options later.

```
interface CustomFeaturePluginConfig {  ui?: {    locations?: ('canvasMenu' | 'inspectorBar')[];  };}
const DEFAULT_CONFIG: CustomFeaturePluginConfig = {  ui: {    locations: []  }};
```

The factory function merges user-provided configuration with sensible defaults. Document available options so integrators understand how to customize behavior.

## Plugin Initialization[#](#plugin-initialization)

### Registering Components[#](#registering-components)

Use `cesdk.ui.registerComponent()` to add custom UI components. Components become available for placement in canvas menus, inspector bars, and other locations. The builder API creates buttons, inputs, and other controls.

```
// Register a custom button componentcesdk.ui.registerComponent(  'customFeaturePlugin.action.canvasMenu',  (context) => {    context.builder.Button('custom-action', {      label: 'Custom Action',      icon: '@imgly/Apps',      onClick: () => {        cesdk.ui.showNotification({          message: 'Custom action triggered!',          type: 'success',          duration: 'short'        });        console.log('Custom action executed');      }    });  });
```

### Subscribing to Events[#](#subscribing-to-events)

Use `engine.event.subscribe()` to react to block changes. Store the unsubscribe function for cleanup when needed. Event subscriptions set up reactive behavior without executing immediate actions.

```
// Subscribe to block events for demonstrationconst unsubscribe = engine.event.subscribe([], (events) => {  events.forEach((event) => {    if (event.type === 'Created') {      console.log(`Block created: ${event.block}`);    }  });});
// Store unsubscribe for potential cleanup(window as any).unsubscribeCustomFeature = unsubscribe;
```

## Controlling Component Placement[#](#controlling-component-placement)

Offer a configuration option for default locations. Check this option during initialization and only modify order when explicitly requested by the integrator.

```
// Only add to canvas menu if configuredconst locations = config.ui?.locations ?? [];if (locations.includes('canvasMenu')) {  const currentOrder = cesdk.ui.getCanvasMenuOrder();  cesdk.ui.setCanvasMenuOrder([    'customFeaturePlugin.action.canvasMenu',    ...currentOrder  ]);  console.log('Custom action added to canvas menu');}
```

This approach lets integrators decide whether to use default placement or handle positioning themselves.

## Troubleshooting[#](#troubleshooting)

### Plugin Not Initializing[#](#plugin-not-initializing)

Verify `addPlugin()` is called after the editor or engine is created. Check for errors thrown during `initialize` - exceptions prevent plugin setup. Ensure async `initialize` functions return promises properly.

### Components Not Appearing[#](#components-not-appearing)

Confirm components are registered with unique IDs. Check that component IDs match exactly when setting order. Verify the location is configured in the plugin options if using optional placement.

### Context Arguments Missing[#](#context-arguments-missing)

For editor plugins, `cesdk` is undefined when added via `engine.addPlugin()`. Always check if `cesdk` exists before calling editor-specific APIs. Structure code to work with engine-only contexts when needed.

### Configuration Not Applied[#](#configuration-not-applied)

Verify the factory function pattern is used and called with parentheses: `MyPlugin()` not `MyPlugin`. Check that configuration is passed to the factory: `MyPlugin({ option: value })`.

## API Reference[#](#api-reference)

| Method | Purpose |
| --- | --- |
| `cesdk.addPlugin()` | Add and initialize a plugin to the editor |
| `engine.addPlugin()` | Add and initialize a plugin to the engine |
| `cesdk.ui.registerComponent()` | Register a custom UI component |
| `cesdk.ui.setCanvasMenuOrder()` | Set component order in canvas menu |
| `cesdk.ui.getCanvasMenuOrder()` | Get current canvas menu component order |
| `engine.event.subscribe()` | Subscribe to block lifecycle events |

## Next Steps[#](#next-steps)

*   [Register New Component](vue/user-interface/ui-extensions/register-new-component-b04a04/) — Learn component registration in detail
*   [Customize UI Behavior](vue/user-interface/ui-extensions/customize-behaviour-c09cb2/) — React to events and control UI programmatically
*   [Create Custom Panel](vue/user-interface/ui-extensions/create-custom-panel-d87b83/) — Build custom panels for your plugin
*   [Disable or Enable Features](vue/user-interface/customization/disable-or-enable-f058e2/) — Control feature availability

---



[Source](https:/img.ly/docs/cesdk/vue/user-interface/customization/save-export-buttons-96018b)