# Vue.js Photo Editor SDK

The CreativeEditor SDK provides a powerful and intuitive solution designed for seamless photo editing directly in the browser.

This CE.SDK configuration is fully customizable and offers a range of features that cater to various use cases, from simple photo adjustments and image compositions with background removal to programmatic editing at scale.

Whether you are building a photo editing application for social media, e-commerce, or any other platform, the CE.SDK Vue.js Image Editor provides the tools you need to deliver a best-in-class user experience.

[

Launch Web Demo

](https://img.ly/showcases/cesdk/photo-editor-ui/web)[

View on GitHub

](https://github.com/imgly/cesdk-web-examples/tree/main/showcase-photo-editor-ui/src/components/case/CaseComponent.jsx)

## Key Capabilities of the Vue.js image Editor[#](#key-capabilities-of-the-vuejs-image-editor)

![Transform](/docs/cesdk/_astro/Transform.By5kJRew_2acCrV.webp)

### Transform

Easily perform operations like cropping, rotating, and resizing your design elements to achieve the perfect composition.

![Asset Management](/docs/cesdk/_astro/AssetLibraries.Ce9MfYvX_HmsaC.webp)

### Asset Management

Import and manage stickers, images, shapes, and other assets to build intricate and visually appealing designs.

![Text Editing](/docs/cesdk/_astro/TextEditing.B8Ra1KOE_2lGC8C.webp)

### Text Editing

Add and style text blocks with a variety of fonts, colors, and effects, giving users the creative freedom to express themselves.

![Client-Side Processing](/docs/cesdk/_astro/ClientSide.CECpQO_1_c6mBh.webp)

### Client-Side Processing

All editing operations are performed directly in the browser, ensuring fast performance without the need for server dependencies.

![Headless & Automation](/docs/cesdk/_astro/Headless.qEVopH3n_20CWbD.webp)

### Headless & Automation

Programmatically edit designs using the engine API, allowing for automated workflows and advanced integrations within your application.

![Extendible](/docs/cesdk/_astro/Extendible.CRYmRihj_BmNTE.webp)

### Extendible

Enhance functionality with plugins and custom scripts, making it easy to tailor the editor to specific needs and use cases.

![Customizable UI](/docs/cesdk/_astro/CustomizableUI.DtHv9rY-_2fNrB2.webp)

### Customizable UI

Design and integrate custom user interfaces that align with your application’s branding and user experience requirements.

![Background Removal](/docs/cesdk/_astro/GreenScreen.CI2APgl0_Z8GtPY.webp)

### Background Removal

Utilize the powerful background removal plugin to allow users to effortlessly remove backgrounds from images, entirely on the Client-Side.

![Filters & Effects](/docs/cesdk/_astro/Filters.D0Iue_r-_Z1VcFlR.webp)

### Filters & Effects

Choose from a wide range of filters and effects to add professional-grade finishing touches to photos, enhancing their visual appeal.

![Size Presets](/docs/cesdk/_astro/SizePresets.C8w0tA1Y_ZN1zMC.webp)

### Size Presets

Access a variety of size presets tailored for different use cases, including social media formats and print-ready dimensions.

## What is the Photo Editor Solution?[#](#what-is-the-photo-editor-solution)

The Photo Editor is a fully customizable CE.SDK configuration focused on photo-centric use cases. It strips down the editor interface to include only the most relevant features for image adjustments — giving users a focused and responsive experience. Whether your users need to fine-tune selfies, prepare product photos, or create profile images, this solution makes it easy.

Get a powerful photo editor into your app with minimal setup. The Photo Editor runs entirely client-side — which helps reduce cloud computing costs and improve privacy.

## Browser Support[#](#browser-support)

The CE.SDK Photo Editor is optimized for use in modern web browsers, ensuring compatibility with the latest versions of Chrome, Firefox, Edge, and Safari.

## Prerequisites[#](#prerequisites)

To get started with the CE.SDK Photo Editor, ensure you have the latest versions of **Node.js** and **NPM** installed.

## Supported File Types[#](#supported-file-types)

The CE.SDK Photo Editor supports loading, editing, and saving various image formats directly in the browser.

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

If you’re ready to start integrating CE.SDK into your Vue.js application, check out the CE.SDK [Getting Started guide](vue/get-started/overview-e18f40/).

In order to configure the editor for an image editing use case consult our [photo editor UI showcase](https://img.ly/showcases/cesdk/photo-editor-ui/web#c) and its [reference implementation](https://github.com/imgly/cesdk-web-examples/tree/main/showcase-photo-editor-ui/src/components/case/CaseComponent.jsx).

## Understanding CE.SDK Architecture & API[#](#understanding-cesdk-architecture--api)

The following sections provide an overview of the key components of the CE.SDK photo editor UI and its API architecture.

If you’re ready to start integrating CE.SDK into your Vue.js application, check out our [Getting Started guide](vue/get-started/overview-e18f40/) or explore the Essential Guides.

### CreativeEditor Photo UI[#](#creativeeditor-photo-ui)

The CE.SDK photo editor UI is a specific configuration of the CE.SDK that focuses the Editor UI on essential photo editing features.

It also includes our powerful background removal plugin that runs entirely on the user’s device, saving on computing costs.

This configuration can be further modified to suit your needs.

Key components include:

![](/docs/cesdk/_astro/CESDK-UI.BD2Iwmum_2gw9UM.webp)

*   **Canvas:** The primary workspace where users interact with their photo content.
*   **Dock:** Provides access to tools and assets that are not directly related to the selected image or block, often used for adding or managing assets.
*   **Inspector Bar:** Controls properties specific to the selected block, such as size, rotation, and other adjustments.
*   **Canvas Menu:** Provides block-specific settings and actions such as deletion or duplication.
*   **Navigation Bar:** Offers global actions such as undo/redo, zoom controls, and access to export options.
*   **Canvas Bar:** For actions affecting the canvas or scene as a whole, such as adding pages or controlling zoom. This is an alternative place for actions like zoom or undo/redo.

Learn more about interacting with and customizing the photo editor UI in our design editor UI guide.

### CreativeEngine[#](#creativeengine)

At the heart of CE.SDK is the CreativeEngine, which powers all rendering and design manipulation tasks.

It can be used in headless mode or integrated with the CreativeEditor UI.

Key features and APIs provided by CreativeEngine include:

*   **Scene Management:** Create, load, save, and manipulate design scenes programmatically.
*   **Block Manipulation:** Create and manage elements such as images, text, and shapes within the scene.
*   **Asset Management:** Load and manage assets like images and SVGs from URLs or local sources.
*   **Variable Management:** Define and manipulate variables for dynamic content within scenes.
*   **Event Handling:** Subscribe to events such as block creation or selection changes for dynamic interaction.

## API Overview[#](#api-overview)

CE.SDK’s APIs are organized into several categories, each addressing different aspects of scene and content management.

The engine API is relevant if you want to programmatically manipulate images to create or modify them at scale.

[**Scene API:**](vue/concepts/scenes-e8596d/)\- **Creating and Loading Scenes**:

```
engine.scene.create();engine.scene.loadFromURL(url);
```

*   **Zoom Control**:

```
engine.scene.setZoomLevel(1.0);engine.scene.zoomToBlock(blockId);
```

[**Block API:**](vue/concepts/blocks-90241e/):- **Creating Blocks**:

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

[**Variable API:**](vue/create-templates/add-dynamic-content/text-variables-7ecb50/)\- **Managing Variables**:

```
engine.variable.setString('myVariable', 'value');const value = engine.variable.getString('myVariable');
```

[**Asset API:**](vue/import-media/concepts-5e6197/) :- **Managing Assets**:

```
engine.asset.add('image', 'https://example.com/image.png');
```

[**Event API:**](vue/concepts/events-353f97/):- **Subscribing to Events**:

```
// Subscribe to scene changesengine.scene.onActiveChanged(() => {  const newActiveScene = engine.scene.get();});
```

### Basic Automation Example[#](#basic-automation-example)

The following automation example shows how to turn an image block into a square format for a platform such as Instagram:

```
// Assuming you have an initialized engine and a selected block (which is an image block)
const newWidth = 1080; // Width in pixelsconst newHeight = 1080; // Height in pixels
const imageBlockId = engine.block.findByType('image')[0];
engine.block.setWidth(imageBlockId, newWidth);engine.block.setHeight(imageBlockId, newHeight);
engine.block.setContentFillMode(imageBlockId, 'Cover');
```

## Customizing the CE.SDK Photo Editor[#](#customizing-the-cesdk-photo-editor)

CE.SDK provides extensive customization options, allowing you to tailor the UI and functionality to meet your specific needs.

This can range from basic configuration settings to more advanced customizations involving callbacks and custom elements.

### Basic Customizations[#](#basic-customizations)

*   **Configuration Object:** Customize the editor’s appearance and functionality by passing a configuration object during initialization.

```
const config = {  baseURL:    'https://cdn.img.ly/packages/imgly/cesdk-engine/1.67.0/assets',  // license: 'YOUR_CESDK_LICENSE_KEY',};
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

For deeper customization, [explore the range of APIs](vue/user-interface-5a089a/) available for extending the functionality of the photo editor.

You can customize the order of components, add new UI elements, and even develop your own plugins to introduce new features.

## Plugins[#](#plugins)

For cases where encapsulating functionality for reuse is necessary, plugins provide an effective solution.

Use our [guide on building plugins](vue/user-interface/ui-extensions/add-custom-feature-2a26b6/) to get started, or explore existing plugins like **Background Removal** and **Vectorizer**.

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



[Source](https:/img.ly/docs/cesdk/vue/prebuilt-solutions/multi-image-generation-163d37)