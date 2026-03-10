# Configuration

Set up CE.SDK with license keys, asset base URLs, user IDs, and runtime configuration options to match your application requirements.

![Configuration example showing CE.SDK editor with theme toggle in navigation bar](/docs/cesdk/_astro/browser.hero.GiFLXRcK_ZxJfwa.webp)

10 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-configuration-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-configuration-browser)

`CreativeEditorSDK.create()` initializes the full CE.SDK editor with UI components. The configuration object controls license validation, asset loading, user tracking, and UI behavior.

```
import CreativeEditorSDK from '@cesdk/cesdk-js';import Example from './browser';
const config = {  // License key removes watermarks from exports  // Get a free trial at https://img.ly/forms/free-trial  // license: 'YOUR_CESDK_LICENSE_KEY',
  // User ID for accurate MAU tracking across devices  userId: 'guides-user',
  // Custom logger for debugging and monitoring  logger: (message: string, level?: string) => {    console.log(`[CE.SDK ${level ?? 'Info'}] ${message}`);  },
  // Enable developer mode for diagnostics  devMode: false,
  // Accessibility settings  a11y: {    headingsHierarchyStart: 1 as const  },
  // Location of core engine assets (WASM, data files)  // Default: IMG.LY CDN. For production, host assets yourself.  // baseURL: 'https://your-cdn.com/cesdk-assets/',
  // Use local assets when developing with local packages  ...(import.meta.env.CESDK_USE_LOCAL && {    baseURL: '/assets/'  })};
CreativeEditorSDK.create('#cesdk_container', config)  .then(async (cesdk: CreativeEditorSDK) => {
    // Expose cesdk for debugging and hero screenshot generation    (window as any).cesdk = cesdk;
    // Load the example plugin    await cesdk.addPlugin(new Example());  })  .catch((error: Error) => {    console.error('Failed to initialize CE.SDK:', error);  });
```

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
class Example implements EditorPlugin {  name = packageJson.name;  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    // Load default asset sources for editing    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Design',      withUploadAssetSources: true    });
    const engine = cesdk.engine;
    // Create a Scene    engine.scene.create('VerticalStack', {      page: { size: { width: 800, height: 600 } }    });
    const pages = engine.block.findByType('page');    const page = pages[0];
    // ========================================    // Setup: Gradient Background with Title    // ========================================    // Create gradient background    const gradientFill = engine.block.createFill('gradient/linear');    engine.block.setGradientColorStops(gradientFill, 'fill/gradient/colors', [      { color: { r: 0.15, g: 0.1, b: 0.35, a: 1.0 }, stop: 0 },      { color: { r: 0.4, g: 0.2, b: 0.5, a: 1.0 }, stop: 0.5 },      { color: { r: 0.6, g: 0.3, b: 0.4, a: 1.0 }, stop: 1 }    ]);    engine.block.setFill(page, gradientFill);
    // Add centered title text    const pageWidth = engine.block.getWidth(page);    const pageHeight = engine.block.getHeight(page);
    const titleText = engine.block.create('text');    engine.block.replaceText(titleText, 'Configure your Editor');    engine.block.setFloat(titleText, 'text/fontSize', 12);    engine.block.setTextColor(titleText, { r: 1.0, g: 1.0, b: 1.0, a: 1.0 });    engine.block.setWidthMode(titleText, 'Auto');    engine.block.setHeightMode(titleText, 'Auto');    engine.block.appendChild(page, titleText);
    // Add IMG.LY subtext    const subtitleText = engine.block.create('text');    engine.block.replaceText(subtitleText, 'Powered by IMG.LY');    engine.block.setFloat(subtitleText, 'text/fontSize', 6);    engine.block.setTextColor(subtitleText, { r: 0.9, g: 0.9, b: 0.9, a: 0.8 });    engine.block.setWidthMode(subtitleText, 'Auto');    engine.block.setHeightMode(subtitleText, 'Auto');    engine.block.appendChild(page, subtitleText);
    // Center both texts    const titleWidth = engine.block.getFrameWidth(titleText);    const titleHeight = engine.block.getFrameHeight(titleText);    const subtitleWidth = engine.block.getFrameWidth(subtitleText);    const subtitleHeight = engine.block.getFrameHeight(subtitleText);
    const spacing = 12;    const totalHeight = titleHeight + spacing + subtitleHeight;    const startY = (pageHeight - totalHeight) / 2;
    engine.block.setPositionX(titleText, (pageWidth - titleWidth) / 2);    engine.block.setPositionY(titleText, startY);    engine.block.setPositionX(subtitleText, (pageWidth - subtitleWidth) / 2);    engine.block.setPositionY(subtitleText, startY + titleHeight + spacing);
    // ========================================    // Runtime Configuration: Theme    // ========================================    cesdk.ui.setTheme('light');    const currentTheme = cesdk.ui.getTheme();    console.log('Current theme:', currentTheme);
    // ========================================    // Runtime Configuration: Scale    // ========================================    cesdk.ui.setScale('modern');    const currentScale = cesdk.ui.getScale();    console.log('Current scale:', currentScale);
    // ========================================    // Runtime Configuration: Actions    // ========================================    cesdk.actions.register('customSave', async () => {      const sceneBlob = await engine.scene.saveToArchive();      await cesdk.utils.downloadFile(sceneBlob, 'application/zip');    });
    // ========================================    // Built-in Actions    // ========================================    // Add built-in export and import actions to the navigation bar    cesdk.ui.insertNavigationBarOrderComponent('last', {      id: 'ly.img.actions.navigationBar',      children: [        'ly.img.saveScene.navigationBar',        'ly.img.exportImage.navigationBar',        'ly.img.exportPDF.navigationBar',        'ly.img.exportScene.navigationBar',        'ly.img.exportArchive.navigationBar',        'ly.img.importScene.navigationBar',        'ly.img.importArchive.navigationBar'      ]    });
    // ========================================    // Engine Settings    // ========================================    engine.editor.setSetting('doubleClickToCropEnabled', true);    engine.editor.setSetting('highlightColor', { r: 0, g: 0.5, b: 1, a: 1 });    const cropEnabled = engine.editor.getSetting('doubleClickToCropEnabled');    console.log('Double-click crop enabled:', cropEnabled);
    // ========================================    // Internationalization: Locale    // ========================================    cesdk.i18n.setLocale('en');    const currentLocale = cesdk.i18n.getLocale();    console.log('Current locale:', currentLocale);
    // ========================================    // Internationalization: Translations    // ========================================    cesdk.i18n.setTranslations({      en: {        'common.back': 'Go Back',        'common.apply': 'Apply Changes'      }    });
    // Enable Auto-Fit Zoom    engine.scene.zoomToBlock(page);    engine.scene.enableZoomAutoFit(page, 'Horizontal', 40, 40);  }}
export default Example;
```

## Required Configuration[#](#required-configuration)

The `license` property is the only required configuration. All other properties have sensible defaults.

| Property | Type | Purpose |
| --- | --- | --- |
| `license` | `string` | License key to remove export watermarks |

The license key validates your CE.SDK subscription and removes watermarks from exports. Get a free trial license at [https://img.ly/forms/free-trial](https://img.ly/forms/free-trial).

## Optional Configuration[#](#optional-configuration)

These properties customize engine behavior and are all optional.

### Engine Properties[#](#engine-properties)

| Property | Type | Purpose |
| --- | --- | --- |
| `baseURL` | `string` | Location of core engine assets (WASM, data files) |
| `userId` | `string` | User identifier for MAU tracking |
| `logger` | `function` | Custom logging function |
| `role` | `'Creator'` | `'Adopter'` | `'Viewer'` | `'Presenter'` | User role for feature access |
| `featureFlags` | `object` | Experimental feature toggles |

### Editor Properties[#](#editor-properties)

| Property | Type | Purpose |
| --- | --- | --- |
| `devMode` | `boolean` | Enable developer diagnostics |
| `a11y` | `object` | Accessibility settings |
| `ui` | `object` | User interface customization |

## Configuration Properties[#](#configuration-properties)

### License Key[#](#license-key)

The license key validates your CE.SDK subscription and removes watermarks from exports. Without a valid license, exports include a watermark.

```
// License key removes watermarks from exports// Get a free trial at https://img.ly/forms/free-trial// license: 'YOUR_CESDK_LICENSE_KEY',
```

### User ID[#](#user-id)

Provide a unique user identifier for accurate Monthly Active User (MAU) tracking. This helps count users correctly when the same person accesses your application from multiple devices.

```
// User ID for accurate MAU tracking across devicesuserId: 'guides-user',
```

### Custom Logger[#](#custom-logger)

Replace the default console logging with a custom logger function. The logger receives a message string and an optional log level (`'Info'`, `'Warning'`, or `'Error'`).

```
// Custom logger for debugging and monitoringlogger: (message: string, level?: string) => {  console.log(`[CE.SDK ${level ?? 'Info'}] ${message}`);},
```

### Developer Mode[#](#developer-mode)

Enable developer mode to get additional diagnostics and debugging information in the console.

```
// Enable developer mode for diagnosticsdevMode: false,
```

### Accessibility Settings[#](#accessibility-settings)

Configure accessibility options like heading hierarchy for screen readers. The `headingsHierarchyStart` property sets which heading level (1-6) the editor should start from.

```
// Accessibility settingsa11y: {  headingsHierarchyStart: 1 as const},
```

### Asset Base URL[#](#asset-base-url)

The `baseURL` property specifies the location of core engine assets, including WASM files, data files, and JavaScript workers. By default, these load from the IMG.LY CDN. For production deployments, host these assets yourself by copying the `assets` folder from `node_modules/@cesdk/engine/assets` to your server.

Content assets like stickers and filters are loaded separately via `engine.addDefaultAssetSources()`, which has its own `baseURL` parameter defaulting to `https://cdn.img.ly/assets/v4`.

```
// Location of core engine assets (WASM, data files)// Default: IMG.LY CDN. For production, host assets yourself.// baseURL: 'https://your-cdn.com/cesdk-assets/',
```

### Initialization[#](#initialization)

Pass the configuration object to `CreativeEditorSDK.create()` along with a container element selector.

```
CreativeEditorSDK.create('#cesdk_container', config)  .then(async (cesdk: CreativeEditorSDK) => {
```

## Runtime Configuration[#](#runtime-configuration)

After initialization, use dedicated APIs to modify settings dynamically.

### Internationalization[#](#internationalization)

#### Locale[#](#locale)

Change the UI language using `cesdk.i18n.setLocale()`.

```
cesdk.i18n.setLocale('en');const currentLocale = cesdk.i18n.getLocale();console.log('Current locale:', currentLocale);
```

#### Translations[#](#translations)

Add or override UI text strings using `cesdk.i18n.setTranslations()`.

```
cesdk.i18n.setTranslations({  en: {    'common.back': 'Go Back',    'common.apply': 'Apply Changes'  }});
```

For complete localization including custom translations and RTL support, see [Localization](vue/user-interface/localization-508e20/) .

### Theme[#](#theme)

Set the UI theme using `cesdk.ui.setTheme()`. Options: `'light'`, `'dark'`, or `'system'`.

```
cesdk.ui.setTheme('light');const currentTheme = cesdk.ui.getTheme();console.log('Current theme:', currentTheme);
```

For advanced theming including custom CSS variables and color schemes, see [Theming](vue/user-interface/appearance/theming-4b0938/) .

### Actions[#](#actions)

Register custom actions for user interactions like save and export.

```
cesdk.actions.register('customSave', async () => {  const sceneBlob = await engine.scene.saveToArchive();  await cesdk.utils.downloadFile(sceneBlob, 'application/zip');});
```

### Built-in Actions[#](#built-in-actions)

CE.SDK provides built-in actions for common operations like saving, exporting, and importing. Add them to the navigation bar using `insertNavigationBarOrderComponent()`:

```
// Add built-in export and import actions to the navigation barcesdk.ui.insertNavigationBarOrderComponent('last', {  id: 'ly.img.actions.navigationBar',  children: [    'ly.img.saveScene.navigationBar',    'ly.img.exportImage.navigationBar',    'ly.img.exportPDF.navigationBar',    'ly.img.exportScene.navigationBar',    'ly.img.exportArchive.navigationBar',    'ly.img.importScene.navigationBar',    'ly.img.importArchive.navigationBar'  ]});
```

**Available built-in actions:**

| Action ID | Purpose |
| --- | --- |
| `ly.img.saveScene.navigationBar` | Save scene to cloud |
| `ly.img.exportImage.navigationBar` | Export as image (PNG/JPEG) |
| `ly.img.exportPDF.navigationBar` | Export as PDF |
| `ly.img.exportScene.navigationBar` | Export scene file |
| `ly.img.exportArchive.navigationBar` | Export as archive (ZIP) |
| `ly.img.importScene.navigationBar` | Import scene file |
| `ly.img.importArchive.navigationBar` | Import archive (ZIP) |

For detailed navigation bar customization including adding buttons and rearranging elements, see [Navigation Bar](vue/user-interface/customization/navigation-bar-4e5d39/) .

For a complete guide on registering and managing actions, see [Actions](vue/actions-6ch24x/) .

### Scale[#](#scale)

Adjust UI scale for different device types. Options: `'normal'`, `'large'`, or `'modern'`.

```
cesdk.ui.setScale('modern');const currentScale = cesdk.ui.getScale();console.log('Current scale:', currentScale);
```

For advanced scale configuration including responsive callbacks, see [Theming](vue/user-interface/appearance/theming-4b0938/) .

### Engine Settings[#](#engine-settings)

Configure engine behavior using `engine.editor.setSetting()`.

```
engine.editor.setSetting('doubleClickToCropEnabled', true);engine.editor.setSetting('highlightColor', { r: 0, g: 0.5, b: 1, a: 1 });const cropEnabled = engine.editor.getSetting('doubleClickToCropEnabled');console.log('Double-click crop enabled:', cropEnabled);
```

For a complete reference of available engine settings, see [Engine Interface](vue/engine-interface-6fb7cf/) .

## API Reference[#](#api-reference)

| Method | Purpose |
| --- | --- |
| `CreativeEditorSDK.create()` | Initialize editor |
| `cesdk.ui.setTheme()` | Set UI theme |
| `cesdk.i18n.setLocale()` | Set UI locale |
| `cesdk.i18n.setTranslations()` | Add translations |
| `cesdk.ui.setScale()` | Set UI scale |
| `cesdk.actions.register()` | Register custom actions |
| `cesdk.ui.insertNavigationBarOrderComponent()` | Add built-in actions to navigation bar |
| `cesdk.utils.downloadFile()` | Download blob as file |
| `engine.editor.setSetting()` | Set engine setting |

## Next Steps[#](#next-steps)

*   [Headless Mode](vue/concepts/headless-mode/browser-24ab98/) \- Use CE.SDK without the UI

---



[Source](https:/img.ly/docs/cesdk/vue/concepts-c9ff51)