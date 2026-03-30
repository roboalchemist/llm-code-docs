# Vue.js Video Editor SDK

CreativeEditor SDK provides a powerful Vue.js library designed for creating and editing videos directly within the browser.

This CE.SDK configuration is highly customizable and extendible, offering a full suite of video editing features such as splitting, cropping, and composing clips on a timeline.

[

Launch Web Demo

](https://img.ly/showcases/cesdk/video-ui/web)[

View on GitHub

](https://github.com/imgly/cesdk-web-examples/tree/main/showcase-video-ui/src/components/case/CaseComponent.jsx)

## Key Capabilities of the Vue.js Video Editor SDK[#](#key-capabilities-of-the-vuejs-video-editor-sdk)

![Transform](/docs/cesdk/_astro/Transform.By5kJRew_2acCrV.webp)

### Transform

Perform operations like video cropping, flipping, and rotating.

![Trim & Split](/docs/cesdk/_astro/TrimSplit.B8YkfyMB_FmGKM.webp)

### Trim & Split

Easily set start and end times, and split videos as needed.

![Merge Videos](/docs/cesdk/_astro/MergeVideos.CdDxNUiO_ZRxgsd.webp)

### Merge Videos

Edit and combine multiple video clips into a single sequence.

![Video Collage](/docs/cesdk/_astro/VideoCollage.23LDUE8e_1VDFAj.webp)

### Video Collage

Arrange multiple clips on one canvas.

![Client-Side Processing](/docs/cesdk/_astro/ClientSide.CECpQO_1_c6mBh.webp)

### Client-Side Processing

Execute all video editing operations directly in the browser, with no need for server dependencies.

![Headless & Automation](/docs/cesdk/_astro/Headless.qEVopH3n_20CWbD.webp)

### Headless & Automation

Programmatically edit videos within your Vue.js application.

![Extendible](/docs/cesdk/_astro/Extendible.CRYmRihj_BmNTE.webp)

### Extendible

Add new functionalities seamlessly using the plugins and engine API.

![Customizable UI](/docs/cesdk/_astro/CustomizableUI.DtHv9rY-_2fNrB2.webp)

### Customizable UI

Design and integrate custom UIs tailored to your application.

![Asset Libraries](/docs/cesdk/_astro/AssetLibraries.Ce9MfYvX_HmsaC.webp)

### Asset Libraries

Incorporate custom assets like filters, stickers, images, and videos.

![Green Screen Support](/docs/cesdk/_astro/GreenScreen.CI2APgl0_Z8GtPY.webp)

### Green Screen Support

Apply chroma keying for background removal.

![Templating](/docs/cesdk/_astro/Templating.eMNm9_jD_ycnVt.webp)

### Templating

Create design templates with placeholders and text variables for dynamic content.

## What is the Video Editor Solution?[#](#what-is-the-video-editor-solution)

The Video Editor is a prebuilt solution powered by the CreativeEditor SDK (CE.SDK) that enables fast integration of high-performance video editing into web, mobile, and desktop applications. It’s designed to help your users create professional-grade videos—from short social clips to long-form stories—directly within your app.

Skip building a video editor from scratch. This fully client-side solution provides a solid foundation with an extensible UI and a robust engine API to power video editing in any use case.

## Browser Support[#](#browser-support)

Video editing mode relies on modern web codecs, supported only in the latest versions of Google Chrome, Microsoft Edge, or other Chromium-based browsers.

## Prerequisites[#](#prerequisites)

[Ensure you have the latest stable version of **Node.js & NPM** installed](https://www.npmjs.com/get-npm)

## Supported File Types[#](#supported-file-types)

Creative Editor SDK supports loading, editing, and saving **MP4 files** directly in the browser.

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

For detailed information, see the [full file format support list](vue/file-format-support-3c4b2a/).

## Getting Started[#](#getting-started)

If you’re ready to start integrating CE.SDK into your Vue.js application, check out the CE.SDK [Getting Started guide](vue/get-started/overview-e18f40/). In order to configure the editor for a video editing use case consult our [video editor UI showcase](https://img.ly/showcases/cesdk/video-ui/web) and its [reference implementation](https://github.com/imgly/cesdk-web-examples/blob/main/showcase-video-ui/src/components/case/CaseComponent.jsx).

## Understanding CE.SDK Architecture & API[#](#understanding-cesdk-architecture--api)

The sections below provide an overview of the key components of the CE.SDK video editor UI and its API architecture.

If you’re ready to start integrating CE.SDK into your Vue.js application, check out our [Getting Started guide](vue/get-started/overview-e18f40/) or explore the Essential Guides.

### CreativeEditor Video UI[#](#creativeeditor-video-ui)

The CE.SDK video UI is designed for intuitive video creation and editing. Below are the main components and customizable elements within the UI: ![](/docs/cesdk/_astro/Simple-Timeline-Mono.D4wteAxE_Z2ggWA9.webp)

*   **Canvas:** The main interaction area for video content.
*   **Dock:** Entry point for interactions not directly related to the selected video block, often used for accessing asset libraries.
*   **Canvas Menu:** Access block-specific settings such as duplication or deletion.
*   **Inspector Bar:** Manage block-specific functionalities, like adjusting properties of the selected block.
*   **Navigation Bar:** Handles global scene actions like undo/redo and zoom.
*   **Canvas Bar:** Provides tools for managing the overall canvas, such as adding pages or controlling zoom.
*   **Timeline:** The core video editing control, where clips and audio are arranged over time.

### CreativeEngine[#](#creativeengine)

CreativeEngine is the core of CE.SDK, responsible for managing the rendering and manipulation of video scenes. It can be used in headless mode or integrated with the CreativeEditor UI. Below are key features and APIs provided by the CreativeEngine:

*   **Scene Management:** Programmatically create, load, save, and modify video scenes.
*   **Block Manipulation:** Create and manage video elements such as shapes, text, and images.
*   **Asset Management:** Load assets like videos and images from URLs or local sources.
*   **Variable Management:** Define and manipulate variables within scenes for dynamic content.
*   **Event Handling:** Subscribe to events such as block creation or updates for dynamic interaction.

## API Overview[#](#api-overview)

The APIs of CE.SDK are grouped into several categories, reflecting different aspects of scene management and manipulation.

[**Scene API:**](vue/concepts/scenes-e8596d/)\- **Creating and Loading Scenes**:

```
engine.scene.create();engine.scene.loadFromURL(url);
```

*   **Zoom Control**:
    
    ```
    engine.scene.setZoomLevel(1.0);engine.scene.zoomToBlock(blockId);
    ```
    
    [**Block API:**](vue/concepts/blocks-90241e/)
*   **Creating Blocks**:
    
    ```
    const block = engine.block.create('shapes/star');
    ```
    
*   **Setting Properties**:
    
    ```
    engine.block.setColor(blockId, 'fill/color', { r: 1, g: 0, b: 0, a: 1 });engine.block.setString(blockId, 'text/content', 'Hello World');
    ```
    
*   **Querying Properties**:
    
    ```
    const color = engine.block.getColor(blockId, 'fill/color');const text = engine.block.getString(blockId, 'text/content');
    ```
    
    [**Variable API:**](vue/create-templates/add-dynamic-content/text-variables-7ecb50/) Variables allow dynamic content within scenes to programmatically create variations of a design.
    
*   **Managing Variables**:
    
    ```
    engine.variable.setString('myVariable', 'value');const value = engine.variable.getString('myVariable');
    ```
    
    [**Asset API:**](vue/import-media/concepts-5e6197/)
*   **Managing Assets**:
    
    ```
    engine.asset.add('image', 'https://example.com/image.png');
    ```
    
    [**Event API**](vue/concepts/events-353f97/)
*   **Subscribing to Events**:
    
    ```
    // Subscribe to scene changesengine.scene.onActiveChanged(() => {  const newActiveScene = engine.scene.get();});
    ```
    

## Customizing the Vue.js Video Editor[#](#customizing-the-vuejs-video-editor)

CE.SDK provides extensive customization options to adapt the UI to various use cases. These options range from simple configuration changes to more advanced customizations involving callbacks and custom elements.

### Basic Customizations[#](#basic-customizations)

*   **Configuration Object**: When initializing the CreativeEditor, you can pass a configuration object that defines basic settings such as the base URL for assets, the language, theme, and license key.
    
    ```
    const config = {  baseURL:    'https://cdn.img.ly/packages/imgly/cesdk-engine/1.67.0/assets',  // license: 'YOUR_CESDK_LICENSE_KEY',};
    ```
    
*   **Localization**: Customize the language and labels used in the editor to support different locales.
    
    ```
    const config = {};
    CreativeEditorSDK.create('#cesdk_container', config).then(async cesdk => {  // Set theme using the UI API  cesdk.ui.setTheme('light'); // 'dark' | 'system'  cesdk.i18n.setLocale('en');  cesdk.i18n.setTranslations({    en: {      variables: {        my_custom_variable: {          label: 'Custom Label',        },      },    },  });});
    ```
    
*   [Custom Asset Sources](vue/import-media/concepts-5e6197/) : Serve custom video or image assets from a remote URL.
    

### UI Customization Options[#](#ui-customization-options)

*   **Theme**: Choose between predefined themes such as ‘dark’, ‘light’, or ‘system’.
    
    ```
    CreativeEditorSDK.create('#cesdk_container', config).then(async cesdk => {  // Set theme using the UI API  cesdk.ui.setTheme('dark'); // 'light' | 'system'});
    ```
    
*   **UI Components**: Enable or disable specific UI components based on your requirements.
    
    ```
    const config = {  ui: {    elements: {      toolbar: true,      inspector: false,    },  },};
    ```
    

## Advanced Customizations[#](#advanced-customizations)

Learn more about extending editor functionality and customizing its UI to your use case by consulting our in-depth [customization guide](vue/user-interface/ui-extensions-d194d1/). Here is an overview of the APIs and components available to you.

### Order APIs[#](#order-apis)

Customization of the web editor’s components and their order within these locations is managed through specific Order APIs, allowing the addition, removal, or reordering of elements. Each location has its own Order API, e.g., `setDockOrder`, `setCanvasMenuOrder`, `setInspectorBarOrder`, `setNavigationBarOrder`, and `setCanvasBarOrder`.

### Layout Components[#](#layout-components)

CE.SDK provides special components for layout control, such as `ly.img.separator` for separating groups of components and `ly.img.spacer` for adding space between components.

### Registration of New Components[#](#registration-of-new-components)

Custom components can be registered and integrated into the web editor using builder components like buttons, dropdowns, and inputs. These components can replace default ones or introduce new functionalities, deeply integrating custom logic into the editor.

### Feature API[#](#feature-api)

The Feature API enables conditional display and functionality of components based on the current context, allowing for dynamic customization. For example, you can hide certain buttons for specific block types.

## Plugins[#](#plugins)

Customize the CE.SDK web editor during initialization using the outlined APIs. For many use cases, this is sufficient, but for more advanced scenarios, plugins are useful. Follow our [guide on building plugins](vue/user-interface/ui-extensions/add-custom-feature-2a26b6/) or explore existing plugins like:

[**Background Removal**](vue/edit-image/remove-bg-9dfcf7/): Adds a button to the canvas menu to remove image backgrounds. [**Vectorizer**](vue/edit-image/vectorize-2b4c7f/): Adds a button to the canvas menu to quickly vectorize a graphic.

## Framework Support[#](#framework-support)

CreativeEditor SDK’s video editing library is compatible with any Javascript including, React, Angular, Vue.js, Svelte, Blazor, Next.js, Typescript. It is also compatible with desktop and server-side technologies such as electron, PHP, Laravel and Rails.

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



[Source](https:/img.ly/docs/cesdk/vue/prebuilt-solutions/t-shirt-designer-02b48f)