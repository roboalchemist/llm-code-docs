# Vue.js Creative Editor

The CreativeEditor SDK delivers a powerful Vue.js library designed for crafting and editing rich visual designs directly within the browser.

### What is CE.SDK?[#](#what-is-cesdk)

This CE.SDK configuration is fully customizable and extendable, offering a comprehensive range of design editing capabilities, including templating, layout management, asset integration, and more, as well as advanced features like background removal.

[Launch Web Demo](https://img.ly/showcases/cesdk)[

Get Started

](vue/get-started/overview-e18f40/)

## Key Features of the Vue.js Creative Editor SDK[#](#key-features-of-the-vuejs-creative-editor-sdk)

![Transformations](/docs/cesdk/_astro/Transform.By5kJRew_2acCrV.webp)

### Transformations

Execute operations like cropping, rotating, and resizing design components.

![Templating](/docs/cesdk/_astro/Templating.eMNm9_jD_ycnVt.webp)

### Templating

Build and apply design templates with placeholders and text variables for dynamic content.

![Placeholders & Lockable Design](/docs/cesdk/_astro/Placeholders.DzG3E33B_bmQxQ.webp)

### Placeholders & Lockable Design

Constrain templates to guide your users’ design and ensure brand consistency.

![Asset Handling](/docs/cesdk/_astro/AssetLibraries.Ce9MfYvX_HmsaC.webp)

### Asset Handling

Import and manage images, shapes, and other assets for your design projects.

![Design Collages](/docs/cesdk/_astro/VideoCollage.23LDUE8e_1VDFAj.webp)

### Design Collages

Arrange multiple elements on a single canvas to create intricate layouts.

![Text Editing](/docs/cesdk/_astro/TextEditing.B8Ra1KOE_2lGC8C.webp)

### Text Editing

Incorporate and style text blocks using various fonts, colors, and effects.

![Client-Side Operations](/docs/cesdk/_astro/ClientSide.CECpQO_1_c6mBh.webp)

### Client-Side Operations

All design editing tasks are performed directly in the browser, eliminating the need for server dependencies.

![Headless & Automation](/docs/cesdk/_astro/Headless.qEVopH3n_20CWbD.webp)

### Headless & Automation

Programmatically edit designs within your React application using the engine API.

![Extendible](/docs/cesdk/_astro/Extendible.CRYmRihj_BmNTE.webp)

### Extendible

Easily enhance functionality with plugins and custom scripts.

![Customizable UI](/docs/cesdk/_astro/CustomizableUI.DtHv9rY-_2fNrB2.webp)

### Customizable UI

Develop and integrate custom UIs tailored to your application’s design requirements.

![Background Removal](/docs/cesdk/_astro/GreenScreen.CI2APgl0_Z8GtPY.webp)

### Background Removal

This plugin simplifies the process of removing backgrounds from images entirely within the browser.

![Print Optimization](/docs/cesdk/_astro/CutoutLines.kN4c7WBK_lB3LB.webp)

### Print Optimization

Ideal for web-to-print scenarios, supporting spot colors and cut-outs.

## Browser Support[#](#browser-support)

The CE.SDK Design Editor is optimized for use in modern web browsers, ensuring compatibility with the latest versions of Chrome, Firefox, Edge, and Safari. See the full list of [supported browsers here](vue/browser-support-28c1b0/) .

## Supported Formats[#](#supported-formats)

CE.SDK supports a wide range of file types to ensure maximum flexibility for developers:

### Importing Media[#](#importing-media)

| Category | Supported Formats |
| --- | --- |
| **Images** | `.png`, `.jpeg`, `.jpg`, `.gif`, `.webp`, `.svg`, `.bmp` |
| **Video** | `.mp4` (H.264/AVC, H.265/HEVC), `.mov` (H.264/AVC, H.265/HEVC), `.webm` (VP8, VP9, AV1) |
| **Audio** | `.mp3`, `.m4a`, `.mp4` (AAC or MP3), `.mov` (AAC or MP3) |
| **Animation** | `.json` (Lottie) |

Need to import a format not listed here? CE.SDK allows you to create custom importers for any file type by using our Scene and Block APIs programmatically.

### Exporting Media[#](#exporting-media)

| Category | Supported Formats |
| --- | --- |
| **Images** | `.png` (with transparency), `.jpeg`, `.webp`, `.tga` |
| **Video** | `.mp4` (H.264 or H.265 on supported platforms with limited transparency support) |
| **Print** | `.pdf` (supports underlayer printing and spot colors) |
| **Scene** | `.scene` (description of the scene without any assets) |
| **Archive** | `.zip` (fully self-contained archive that bundles the `.scene` file with all assets) |

Our custom cross-platform C++ based rendering and layout engine ensures consistent output quality across devices.

### Importing Templates[#](#importing-templates)

| Format | Description |
| --- | --- |
| `.idml` | InDesign |
| `.psd` | Photoshop |
| `.scene` | CE.SDK Native |

Need to import a format not listed here? CE.SDK allows you to create custom importers for any file type by using our Scene and Block APIs to generate scenes programmatically.

For detailed information, see the [full file format support list](vue/file-format-support-3c4b2a/) .

## Understanding CE.SDK Architecture & API[#](#understanding-cesdk-architecture--api)

The following sections provide an overview of the key components of the CE.SDK design editor UI and its API architecture. If you’re ready to start integrating CE.SDK into your Vue.js application, refer to our [Getting Started guide](vue/get-started/overview-e18f40/) or explore the Essential Guides.

### CreativeEditor Design UI[#](#creativeeditor-design-ui)

The CE.SDK design UI is designed for intuitive design creation and editing. Key components and customizable elements within the UI include:

![](/docs/cesdk/_astro/CESDK-UI.BD2Iwmum_2gw9UM.webp)

*   **Canvas:** The main interaction area for design content.
*   **Dock:** An entry point for interactions not directly related to the selected design block, often used for accessing asset libraries.
*   **Canvas Menu:** Access block-specific settings like duplication or deletion.
*   **Inspector Bar:** Manage block-specific functionalities, such as adjusting properties of the selected block.
*   **Navigation Bar:** Handles global scene actions like undo/redo and zoom.
*   **Canvas Bar:** Provides tools for managing the overall canvas, such as adding pages or controlling zoom.
*   **Layer Panel:** Manage the stacking order and visibility of design elements.

Learn more about interacting with and manipulating design controls in our design editor UI guide.

### CreativeEngine[#](#creativeengine)

The CreativeEngine is the core of CE.SDK, responsible for rendering and manipulating design scenes. It can operate in headless mode or be integrated with the CreativeEditor UI. Key features and APIs provided by CreativeEngine include:

*   **Scene Management:** Create, load, save, and modify design scenes programmatically.
*   **Block Manipulation:** Create and manage design elements, such as shapes, text, and images.
*   **Asset Management:** Load assets like images and SVGs from URLs or local sources.
*   **Variable Management:** Define and manipulate variables within scenes for dynamic content.
*   **Event Handling:** Subscribe to events like block creation or updates for dynamic interaction.

## API Overview[#](#api-overview)

CE.SDK’s APIs are categorized into several groups, reflecting different aspects of scene management and manipulation.

[**Scene API:**](vue/concepts/scenes-e8596d/) \- **Creating and Loading Scenes**:

```
engine.scene.create();engine.scene.loadFromURL(url);
```

*   **Zoom Control**:
    
    ```
    engine.scene.setZoomLevel(1.0);engine.scene.zoomToBlock(blockId);
    ```
    

[**Block API:**](vue/concepts/blocks-90241e/) : - **Creating Blocks**:

```
const block = engine.block.create('shapes/rectangle');
```

*   **Setting Properties**:
    
    ```
    engine.block.setColor(blockId, 'fill/color', { r: 1, g: 0, b: 0, a: 1 });engine.block.setString(blockId, 'text/content', 'Hello World');
    ```
    
*   **Querying Properties**:
    
    ```
    const color = engine.block.getColor(blockId, 'fill/color');const text = engine.block.getString(blockId, 'text/content');
    ```
    

[**Variable API:**](vue/create-templates/add-dynamic-content/text-variables-7ecb50/) Variables allow dynamic content within scenes, enabling programmatic creation of design variations.

*   **Managing Variables**:
    
    ```
    engine.variable.setString('myVariable', 'value');const value = engine.variable.getString('myVariable');
    ```
    

[**Asset API:**](vue/import-media/concepts-5e6197/) : - **Managing Assets**:

```
engine.asset.add('image', 'https://example.com/image.png');
```

[**Event API:**](vue/concepts/events-353f97/) : - **Subscribing to Events**:

```
// Subscribe to scene changesengine.scene.onActiveChanged(() => {  const newActiveScene = engine.scene.get();});
```

## Customizing the Vue.js Creative Editor[#](#customizing-the-vuejs-creative-editor)

CE.SDK provides extensive customization options to tailor the UI to various use cases. These options range from simple configuration changes to more advanced customizations involving callbacks and custom elements.

### Basic Customizations[#](#basic-customizations)

*   **Configuration Object:** When initializing the CreativeEditor, pass a configuration object that defines basic settings such as the base URL for assets, language, theme, and license key.
    
    ```
    const config = {  baseURL: `https://cdn.img.ly/packages/imgly/cesdk-js/${CreativeEditorSDK.version}/assets`,  // license: 'YOUR_CESDK_LICENSE_KEY',};
    ```
    
*   **Localization:** Customize the language and labels used in the editor to support different locales.
    
    ```
    const config = {};
    CreativeEditorSDK.create('#cesdk_container', config).then(async cesdk => {  // Set theme using the UI API  cesdk.ui.setTheme('light'); // 'dark' | 'system'  cesdk.i18n.setLocale('en');  cesdk.i18n.setTranslations({    en: {      variables: {        my_custom_variable: {          label: 'Custom Label',        },      },    },  });});
    ```
    
*   [Custom Asset Sources](vue/import-media/concepts-5e6197/) : Serve custom image or SVG assets from a remote URL.
    

### UI Customization Options[#](#ui-customization-options)

*   **Theme:** Select from predefined themes like ‘dark’, ‘light’, or ‘system’.
    
    ```
    CreativeEditorSDK.create('#cesdk_container', config).then(async cesdk => {  // Set theme using the UI API  cesdk.ui.setTheme('dark'); // 'light' | 'system'});
    ```
    
*   **UI Components:** Enable or disable specific UI components as needed.
    
    ```
    const config = {  ui: {    elements: {      toolbar: true,      inspector: false,    },  },};
    ```
    

## Advanced Customizations[#](#advanced-customizations)

Explore more ways to extend editor functionality and customize its UI to your specific needs by consulting our detailed [customization guide](vue/user-interface-5a089a/) . Below is an overview of the available APIs and components.

### Order APIs[#](#order-apis)

The Order APIs manage the customization of the web editor’s components and their order within these locations, allowing the addition, removal, or reordering of elements. Each location has its own Order API, such as `setDockOrder`, `setCanvasMenuOrder`, `setInspectorBarOrder`, `setNavigationBarOrder`, and `setCanvasBarOrder`.

### Layout Components[#](#layout-components)

CE.SDK offers special components for layout control, such as `ly.img.separator` for separating groups of components and `ly.img.spacer` for adding space between components.

### Registration of New Components[#](#registration-of-new-components)

Custom components can be registered and integrated into the web editor using builder components like buttons, dropdowns, and inputs. These components can replace default ones or introduce new functionalities, seamlessly integrating custom logic into the editor.

### Feature API[#](#feature-api)

The Feature API allows for the conditional display and functionality of components based on the current context, enabling dynamic customization. For instance, certain buttons can be hidden for specific block types.

## Plugins[#](#plugins)

Customizing the CE.SDK web editor during its initialization is possible through the APIs outlined above. For many use cases, this will be sufficient. However, there are situations where encapsulating functionality for reuse is necessary. Plugins come in handy here. Follow our [guide on building your own plugins](vue/user-interface-5a089a/) to learn more or explore some of the plugins we’ve created using this API:

*   **Background Removal**: Adds a button to the canvas menu to remove image backgrounds.
*   **Vectorizer**: Adds a button to the canvas menu to quickly vectorize a graphic.

## Ready to get started?

With a free trial and pricing that fits your needs, it's easy to find the best solution for your product.

[Free Trial](https://img.ly/forms/free-trial)

### 500M+

video and photo creations are powered by IMG.LY every month

![HP logo](/docs/cesdk/_astro/HP.BZ1qDNii_ZpK5Lk.webp)

![Shopify logo](/docs/cesdk/_astro/Shopify.Dmyk4png_ZRKWXF.webp)

![Reuters logo](/docs/cesdk/_astro/Reuters.B8BV2Fek_ZLrHFJ.webp)

![Hootsuite logo](/docs/cesdk/_astro/Hootsuite.C94d5fhs_Zsc4gx.webp)

![Semrush logo](/docs/cesdk/_astro/Semrush.B2YsPaIn_23cDNx.webp)

![Shutterfly logo](/docs/cesdk/_astro/Shutterfly.Cc7Sw48y_Z3TjCs.webp)

![Sprout Social logo](/docs/cesdk/_astro/Sprout-Social.VxlY6_Tc_E0Dzh.webp)

![One.com logo](/docs/cesdk/_astro/Onecom.BQ_oPnlz_Z1btrtu.webp)

![Constant Contact logo](/docs/cesdk/_astro/Constant-Contact.1rh975Q__Z2ob7wU.webp)

---



[Source](https:/img.ly/docs/cesdk/vue/upgrade-4f8715)