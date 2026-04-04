# Hide Elements

CE.SDK provides flexible APIs to control the visibility of every UI element. You can hide elements using the Feature API (which completely removes features from the UI), ordering APIs (which control what appears in ordered lists like navigation bars), or panel management APIs (which control panel state). This guide demonstrates how to hide and show different UI elements to create custom editing experiences tailored to your application’s needs.

![Hide Elements example showing CE.SDK with various UI elements hidden](/docs/cesdk/_astro/browser.hero.B9eelvQX_215CXi.webp)

10 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples)[

GitHub](https://github.com/imgly/cesdk-web-examples)

## Understanding UI Element Hiding Approaches[#](#understanding-ui-element-hiding-approaches)

CE.SDK provides three methods to control UI visibility: the Feature API for disabling features entirely, ordering APIs for controlling component layout, and panel management for dynamic show/hide behavior.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
class Example implements EditorPlugin {  name = packageJson.name;  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    // ===== Hide Elements Examples =====    // Configure UI visibility before loading assets and creating scene    // Show only navigation bar and inspector bar, hide everything else
    // Hide canvas bar and canvas menu using Feature API    cesdk.feature.disable(['ly.img.canvas.bar', 'ly.img.canvas.menu']);
    // Hide the entire dock using Feature API    cesdk.feature.disable('ly.img.dock');
    // Hide UI elements using ordering APIs (alternative method)    // Setting empty array removes all components    cesdk.ui.setDockOrder([]);    cesdk.ui.setCanvasBarOrder([], 'top');    cesdk.ui.setCanvasMenuOrder([]);
    // Close all panels using wildcard pattern    cesdk.ui.closePanel('//ly.img.panel/*');
    // Check if panels are open    const inspectorPanelId = '//ly.img.panel/inspector';    const isInspectorOpen = cesdk.ui.isPanelOpen(inspectorPanelId);    console.log('Inspector panel open:', isInspectorOpen);
    // Find all panels    const allPanels = cesdk.ui.findAllPanels();    console.log('All panels:', allPanels);
    // Using glob patterns to control multiple features    const navigationFeatures = cesdk.feature.list({      matcher: 'ly.img.navigation.*'    });    console.log('Navigation features:', navigationFeatures);
    // Disable all navigation features at once using wildcard pattern    // cesdk.feature.disable('ly.img.navigation.*');
    // Check if features are enabled    const isDockEnabled = cesdk.feature.isEnabled('ly.img.dock');    const isNavBarEnabled = cesdk.feature.isEnabled('ly.img.navigation.bar');    console.log('Dock enabled:', isDockEnabled);    console.log('Navigation bar enabled:', isNavBarEnabled);
    // Hide notification toasts    cesdk.feature.disable('ly.img.notifications');    // Or hide specific notification types:    // cesdk.feature.disable('ly.img.notifications.undo');    // cesdk.feature.disable('ly.img.notifications.redo');
    // ===== Load Assets and Create Scene =====    // Now that UI is configured, load assets and create scene    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Design',      withUploadAssetSources: true    });    await cesdk.createDesignScene();
    const engine = cesdk.engine;    const page = engine.block.findByType('page')[0];
    // Add a single image to the canvas    const imageUri = 'https://img.ly/static/ubq_samples/sample_1.jpg';    const imageBlock = await engine.block.addImage(imageUri);    engine.block.appendChild(page, imageBlock);
    // Center and fit the image on the page    const pageWidth = engine.block.getWidth(page);    const pageHeight = engine.block.getHeight(page);    const imageWidth = engine.block.getWidth(imageBlock);    const imageHeight = engine.block.getHeight(imageBlock);
    // Calculate scale to fit image within page    const scaleX = pageWidth / imageWidth;    const scaleY = pageHeight / imageHeight;    const scale = Math.min(scaleX, scaleY) * 0.8; // 80% of page size
    // Apply scale and center    engine.block.setWidth(imageBlock, imageWidth * scale);    engine.block.setHeight(imageBlock, imageHeight * scale);
    const scaledWidth = engine.block.getWidth(imageBlock);    const scaledHeight = engine.block.getHeight(imageBlock);    engine.block.setPositionX(imageBlock, (pageWidth - scaledWidth) / 2);    engine.block.setPositionY(imageBlock, (pageHeight - scaledHeight) / 2);
    // Select the image to show the inspector    engine.block.setSelected(imageBlock, true);
    console.log('Hide elements example loaded successfully!');  }}
export default Example;
```

## Hiding Elements with the Feature API[#](#hiding-elements-with-the-feature-api)

The Feature API is the primary way to hide UI elements in CE.SDK. When you disable a feature, it’s completely removed from the interface. You can hide various UI components including:

*   **Navigation Bar** (`ly.img.navigation.bar`) - Contains buttons like back, close, undo/redo, and zoom controls
*   **Inspector Bar** (`ly.img.inspector.bar`) - Provides access to block properties and editing controls
*   **Dock** (`ly.img.dock`) - Sidebar that provides quick access to assets and tools
*   **Notifications** (`ly.img.notifications`) - Toast messages for actions like undo and redo

Here’s how to disable and hide the dock:

```
// Hide the entire dock using Feature APIcesdk.feature.disable('ly.img.dock');
```

And how to disable and hide canvas elements:

```
// Hide canvas bar and canvas menu using Feature APIcesdk.feature.disable(['ly.img.canvas.bar', 'ly.img.canvas.menu']);
```

By passing an array to `feature.disable()`, you can hide multiple features in a single call. The Feature API also supports glob patterns with wildcards (`*`) for batch operations, and you can check feature state with `isEnabled()` before making changes.

## Hiding Elements with Ordering APIs[#](#hiding-elements-with-ordering-apis)

Ordering APIs provide an alternative method for hiding UI elements by controlling what appears in component lists. Setting an empty order array removes all components from that area. This approach doesn’t disable features - it just controls layout.

```
// Hide UI elements using ordering APIs (alternative method)// Setting empty array removes all componentscesdk.ui.setDockOrder([]);cesdk.ui.setCanvasBarOrder([], 'top');cesdk.ui.setCanvasMenuOrder([]);
```

The key difference between ordering APIs and the Feature API is that ordering APIs only affect visual layout. The underlying features remain enabled and can still be accessed programmatically.

## Managing Panel Visibility[#](#managing-panel-visibility)

Panels in CE.SDK can be opened and closed dynamically using the panel management APIs. This allows you to create context-sensitive interfaces that show relevant panels based on user actions.

```
// Close all panels using wildcard patterncesdk.ui.closePanel('//ly.img.panel/*');
// Check if panels are openconst inspectorPanelId = '//ly.img.panel/inspector';const isInspectorOpen = cesdk.ui.isPanelOpen(inspectorPanelId);console.log('Inspector panel open:', isInspectorOpen);
// Find all panelsconst allPanels = cesdk.ui.findAllPanels();console.log('All panels:', allPanels);
```

## Using Glob Patterns[#](#using-glob-patterns)

The Feature API supports glob patterns for batch operations. This makes it easy to enable or disable groups of related features.

```
// Using glob patterns to control multiple featuresconst navigationFeatures = cesdk.feature.list({  matcher: 'ly.img.navigation.*'});console.log('Navigation features:', navigationFeatures);
```

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `cesdk.feature.enable(featureId)` | Enable a feature |
| `cesdk.feature.disable(featureId)` | Disable a feature or array of features |
| `cesdk.feature.isEnabled(featureId)` | Check if a feature is enabled |
| `cesdk.feature.list({ matcher })` | List features matching a glob pattern |
| `cesdk.ui.setNavigationBarOrder(order)` | Set navigation bar component order |
| `cesdk.ui.setCanvasBarOrder(order, position)` | Set canvas bar component order |
| `cesdk.ui.setCanvasMenuOrder(order)` | Set canvas menu component order |
| `cesdk.ui.setDockOrder(order)` | Set dock component order |
| `cesdk.ui.setInspectorBarOrder(order)` | Set inspector bar component order |
| `cesdk.ui.openPanel(panelId)` | Open a panel |
| `cesdk.ui.closePanel(panelId)` | Close a panel (supports wildcards) |
| `cesdk.ui.isPanelOpen(panelId)` | Check if a panel is open |
| `cesdk.ui.findAllPanels(options)` | Find all panels with optional filtering |

## Next Steps[#](#next-steps)

After mastering UI element hiding, explore these related guides:

*   [UI Overview](vue/user-interface/overview-41101a/) \- Understanding CE.SDK’s UI architecture
*   [Disable or Enable Features](vue/user-interface/customization/disable-or-enable-f058e2/) \- Feature API deep dive
*   [Customize Dock](vue/user-interface/customization/dock-cb916c/) \- Dock customization patterns
*   [Customize Panels](vue/user-interface/customization/panel-7ce1ee/) \- Panel management patterns

---



[Source](https:/img.ly/docs/cesdk/vue/user-interface/customization/force-crop-c2854e)