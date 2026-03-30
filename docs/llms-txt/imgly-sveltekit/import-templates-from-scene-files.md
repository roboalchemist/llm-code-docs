# Import Templates from Scene Files

CE.SDK lets you load complete design templates from scene files to start projects from pre-designed templates, implement template galleries, and build template management systems.

![Import Templates from Scene Files example showing CE.SDK interface with loaded template](/docs/cesdk/_astro/browser.hero.C0fFNNlc_1piBaU.webp)

10 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-create-templates-import-from-scene-file-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-create-templates-import-from-scene-file-browser)

Scene files are portable design templates that preserve the entire design structure including blocks, assets, styles, and layout.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
/** * CE.SDK Plugin: Import Templates from Scene Files * * This example demonstrates: * - Loading scenes from .scene file URLs * - Loading scenes from .archive (ZIP) URLs * - Applying templates while preserving page dimensions * - Understanding the difference between loading and applying templates */class Example implements EditorPlugin {  name = packageJson.name;  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    const engine = cesdk.engine;
    // ===== Example: Load Scene from Archive URL =====    // This is the recommended approach for loading complete templates    // with all their assets embedded in a ZIP file
    // Load a complete template from an archive (ZIP) file    // This loads both the scene structure and all embedded assets    await engine.scene.loadFromArchiveURL(      'https://cdn.img.ly/assets/templates/starterkits/16-9-fashion-ad.zip'    );
    // Alternative: Load scene from URL (.scene file)    // This loads only the scene structure - assets must be accessible via URLs    // Uncomment to try:    // await engine.scene.loadFromURL(    //   'https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene'    // );
    // Alternative: Apply template while preserving current page dimensions    // This is useful when you want to load template content into an existing scene    // with specific dimensions    // Uncomment to try:    // // First create a scene with specific dimensions    // await cesdk.createDesignScene();    // const page = engine.block.findByType('page')[0];    // engine.block.setWidth(page, 1920);    // engine.block.setHeight(page, 1080);    //    // // Now apply template - content will be adjusted to fit    // await engine.scene.applyTemplateFromURL(    //   'https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_instagram_photo_1.scene'    // );
    // Get the loaded scene    const scene = engine.scene.get();    if (scene) {      console.log('Scene loaded successfully:', scene);
      // Get information about the loaded scene      const pages = engine.scene.getPages();      console.log(`Scene has ${pages.length} page(s)`);
      // Get scene mode      const sceneMode = engine.scene.getMode();      console.log('Scene mode:', sceneMode);
      // Get design unit      const designUnit = engine.scene.getDesignUnit();      console.log('Design unit:', designUnit);    }
    // Zoom to fit the loaded content    if (scene) {      await engine.scene.zoomToBlock(scene, {        padding: 40      });    }  }}
export default Example;
```

This guide covers loading scenes from archives, loading from URLs, applying templates while preserving dimensions, and understanding scene file formats.

## Scene File Formats[#](#scene-file-formats)

CE.SDK supports two scene file formats for importing templates:

### Scene Format (.scene)[#](#scene-format-scene)

Scene files are JSON-based representations of design structures. They reference external assets via URLs, making them lightweight and suitable for database storage. However, the referenced assets must remain accessible at their URLs.

**When to use:**

*   Templates stored in databases
*   Templates with hosted assets
*   Lightweight transmission

### Archive Format (.archive or .zip)[#](#archive-format-archive-or-zip)

Archive files are self-contained packages that bundle the scene structure with all referenced assets in a ZIP file. This makes them portable and suitable for offline use.

**When to use:**

*   Template distribution
*   Offline-capable templates
*   Complete portability
*   **Recommended for most use cases**

## Load Scene from Archive[#](#load-scene-from-archive)

The most common way to load templates is from archive URLs. This method loads both the scene structure and all embedded assets:

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
/** * CE.SDK Plugin: Import Templates from Scene Files * * This example demonstrates: * - Loading scenes from .scene file URLs * - Loading scenes from .archive (ZIP) URLs * - Applying templates while preserving page dimensions * - Understanding the difference between loading and applying templates */class Example implements EditorPlugin {  name = packageJson.name;  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    const engine = cesdk.engine;
    // ===== Example: Load Scene from Archive URL =====    // This is the recommended approach for loading complete templates    // with all their assets embedded in a ZIP file
    // Load a complete template from an archive (ZIP) file    // This loads both the scene structure and all embedded assets    await engine.scene.loadFromArchiveURL(      'https://cdn.img.ly/assets/templates/starterkits/16-9-fashion-ad.zip'    );
    // Alternative: Load scene from URL (.scene file)    // This loads only the scene structure - assets must be accessible via URLs    // Uncomment to try:    // await engine.scene.loadFromURL(    //   'https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene'    // );
    // Alternative: Apply template while preserving current page dimensions    // This is useful when you want to load template content into an existing scene    // with specific dimensions    // Uncomment to try:    // // First create a scene with specific dimensions    // await cesdk.createDesignScene();    // const page = engine.block.findByType('page')[0];    // engine.block.setWidth(page, 1920);    // engine.block.setHeight(page, 1080);    //    // // Now apply template - content will be adjusted to fit    // await engine.scene.applyTemplateFromURL(    //   'https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_instagram_photo_1.scene'    // );
    // Get the loaded scene    const scene = engine.scene.get();    if (scene) {      console.log('Scene loaded successfully:', scene);
      // Get information about the loaded scene      const pages = engine.scene.getPages();      console.log(`Scene has ${pages.length} page(s)`);
      // Get scene mode      const sceneMode = engine.scene.getMode();      console.log('Scene mode:', sceneMode);
      // Get design unit      const designUnit = engine.scene.getDesignUnit();      console.log('Design unit:', designUnit);    }
    // Zoom to fit the loaded content    if (scene) {      await engine.scene.zoomToBlock(scene, {        padding: 40      });    }  }}
export default Example;
```

```
// Load a complete template from an archive (ZIP) file// This loads both the scene structure and all embedded assetsawait engine.scene.loadFromArchiveURL(  'https://cdn.img.ly/assets/templates/starterkits/16-9-fashion-ad.zip');
```

When you load from an archive:

*   The ZIP file is fetched and extracted
*   All assets are registered with CE.SDK
*   The scene structure is loaded
*   Asset paths are automatically resolved

## Load Scene from URL[#](#load-scene-from-url)

You can also load scenes directly from .scene file URLs. This approach requires that all referenced assets remain accessible at their original URLs:

```
// await engine.scene.loadFromURL(//   'https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene'// );
```

**Important:** With this method, if asset URLs become unavailable (404 errors, CORS issues, etc.), those assets won’t load and your template may appear incomplete.

## Apply Template vs Load Scene[#](#apply-template-vs-load-scene)

CE.SDK provides two approaches for working with templates, each serving different purposes:

### Load Scene[#](#load-scene)

When you use `loadFromURL()` or `loadFromArchiveURL()`, CE.SDK:

*   Replaces the entire current scene
*   Adopts the template’s page dimensions
*   Loads all content as-is

This is appropriate when starting a new project from a template.

### Apply Template[#](#apply-template)

When you use `applyTemplateFromURL()` or `applyTemplateFromString()`, CE.SDK:

*   Keeps your current page dimensions
*   Adjusts template content to fit
*   Preserves your scene structure

This is useful when you want to load template content into an existing scene with specific dimensions:

```
// // First create a scene with specific dimensions// await cesdk.createDesignScene();// const page = engine.block.findByType('page')[0];// engine.block.setWidth(page, 1920);// engine.block.setHeight(page, 1080);//// // Now apply template - content will be adjusted to fit// await engine.scene.applyTemplateFromURL(//   'https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_instagram_photo_1.scene'// );
```

## Error Handling[#](#error-handling)

When loading templates, several issues can occur:

### Network Errors[#](#network-errors)

Template URLs might be unreachable:

```
try {  await engine.scene.loadFromArchiveURL(templateUrl);} catch (error) {  console.error('Failed to load template:', error);  // Show error message to user  // Fall back to default template or empty scene}
```

### Invalid Scene Format[#](#invalid-scene-format)

The file might not be a valid scene:

```
try {  await engine.scene.loadFromURL(sceneUrl);} catch (error) {  if (error.message.includes('parse')) {    console.error('Invalid scene file format');  }}
```

### Missing Assets[#](#missing-assets)

For .scene files, referenced assets might be unavailable. The scene loads but assets appear missing. Consider using archives to avoid this issue.

## Performance Considerations[#](#performance-considerations)

### Loading Time[#](#loading-time)

Archive size directly impacts loading time:

*   Small archives (< 1MB): Nearly instant
*   Medium archives (1-5MB): 1-2 seconds
*   Large archives (> 5MB): Several seconds

Show loading indicators for better user experience.

## CORS Considerations[#](#cors-considerations)

When loading templates from external URLs, ensure proper CORS headers are set on the server hosting the files. Archives must be accessible with appropriate CORS policies.

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `engine.scene.loadFromArchiveURL()` | Loads a complete scene from an archive (ZIP) file |
| `engine.scene.loadFromURL()` | Loads a scene from a .scene file URL |
| `engine.scene.applyTemplateFromURL()` | Applies a template while preserving page dimensions |
| `engine.scene.get()` | Returns the current scene block ID |
| `engine.scene.getPages()` | Returns all page IDs in the scene |
| `engine.scene.getMode()` | Returns the scene mode (Design or Video) |
| `engine.scene.getDesignUnit()` | Returns the measurement unit |
| `engine.scene.zoomToBlock()` | Zooms the viewport to fit a specific block |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/create-templates/add-dynamic-content/text-variables-7ecb50)