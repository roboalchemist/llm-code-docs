# Apply a Template

Apply template content to an existing scene while preserving your canvas dimensions and design unit.

5 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-use-templates-apply-template-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-use-templates-apply-template-browser)

![Apply a Template](/docs/cesdk/_astro/browser.hero.BO8IfWX3_Zqs5kc.webp)

Unlike loading a scene which replaces everything, applying a template merges template content into your current scene. CE.SDK preserves the current page dimensions and design unit while automatically adjusting template content to fit. This approach is ideal for template switching workflows where users explore different layouts without changing canvas dimensions, or for automation pipelines that standardize output sizes across varying template sources.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
/** * CE.SDK Plugin: Apply a Template * * This example demonstrates how to apply template content to an existing scene: * 1. Creating a scene with specific dimensions * 2. Applying a template from a URL while preserving dimensions * 3. Switching between templates */class Example implements EditorPlugin {  name = packageJson.name;  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Design',      withUploadAssetSources: true    });
    // Create a design scene with specific dimensions    await cesdk.createDesignScene();
    const engine = cesdk.engine;    const page = engine.block.findByType('page')[0];    if (!page) {      throw new Error('No page found');    }
    // Set custom page dimensions - these will be preserved when applying templates    engine.block.setWidth(page, 1080);    engine.block.setHeight(page, 1920);
    // Apply a template from URL - content adjusts to fit current page dimensions    const templateUrl =      'https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene';
    await engine.scene.applyTemplateFromURL(templateUrl);
    // Auto-fit zoom to page    await cesdk.actions.run('zoom.toPage', { autoFit: true });
    console.log('Template applied from URL');
    // Verify that page dimensions are preserved after applying template    const width = engine.block.getWidth(page);    const height = engine.block.getHeight(page);    console.log(`Page dimensions preserved: ${width}x${height}`);
    // Demonstrate template switching - apply a different template    // The page dimensions remain the same while content changes    const alternativeTemplateUrl =      'https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_2.scene';
    // Uncomment to switch templates:    // await engine.scene.applyTemplateFromURL(alternativeTemplateUrl);    // console.log('Switched to alternative template');
    // Store for potential use    console.log('Alternative template URL:', alternativeTemplateUrl);
    console.log('Apply template example completed');  }}
export default Example;
```

This guide covers how to apply templates from URLs and strings while preserving page dimensions, and how to implement template switching functionality.

## When to Use Apply vs Load[#](#when-to-use-apply-vs-load)

Use `applyTemplateFromURL()` or `applyTemplateFromString()` when you want to:

*   **Switch templates**: Let users preview different templates while keeping a consistent canvas size
*   **Standardize output dimensions**: Generate content with fixed sizes (e.g., social media formats, print sizes)
*   **Batch process with templates**: Apply various templates to a pre-configured scene without dimension drift

Use `loadFromString()` or `loadFromURL()` when you need the template’s original dimensions.

**Key distinction**: Loading replaces everything; applying preserves dimensions and merges content.

## Apply a Template from URL[#](#apply-a-template-from-url)

We first create a scene with specific dimensions. These dimensions will be preserved when we apply the template.

```
await cesdk.addDefaultAssetSources();await cesdk.addDemoAssetSources({  sceneMode: 'Design',  withUploadAssetSources: true});
// Create a design scene with specific dimensionsawait cesdk.createDesignScene();
const engine = cesdk.engine;const page = engine.block.findByType('page')[0];if (!page) {  throw new Error('No page found');}
// Set custom page dimensions - these will be preserved when applying templatesengine.block.setWidth(page, 1080);engine.block.setHeight(page, 1920);
```

To apply a template from a URL, call `engine.scene.applyTemplateFromURL()` with the template URL. The template content adjusts automatically to fit the current page dimensions.

```
// Apply a template from URL - content adjusts to fit current page dimensionsconst templateUrl =  'https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene';
await engine.scene.applyTemplateFromURL(templateUrl);
// Auto-fit zoom to pageawait cesdk.actions.run('zoom.toPage', { autoFit: true });
console.log('Template applied from URL');
```

## Verify Preserved Dimensions[#](#verify-preserved-dimensions)

After applying the template, the page dimensions remain unchanged. You can verify this by checking the width and height of the page.

```
// Verify that page dimensions are preserved after applying templateconst width = engine.block.getWidth(page);const height = engine.block.getHeight(page);console.log(`Page dimensions preserved: ${width}x${height}`);
```

## Template Switching[#](#template-switching)

You can apply multiple templates to the same scene. Each application replaces the content while preserving the page setup. This enables “preview” functionality where users explore different templates without affecting their canvas dimensions.

```
// Demonstrate template switching - apply a different template// The page dimensions remain the same while content changesconst alternativeTemplateUrl =  'https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_2.scene';
// Uncomment to switch templates:// await engine.scene.applyTemplateFromURL(alternativeTemplateUrl);// console.log('Switched to alternative template');
// Store for potential useconsole.log('Alternative template URL:', alternativeTemplateUrl);
```

## Apply a Template from String[#](#apply-a-template-from-string)

For templates stored in databases or received from APIs, use `engine.scene.applyTemplateFromString()` with a base64-encoded scene string:

```
// Scene string typically retrieved from storage or APIconst templateString = 'UBQ1ewoiZm9ybWF0Ij...';
// Apply template content to current sceneawait engine.scene.applyTemplateFromString(templateString);
```

## Troubleshooting[#](#troubleshooting)

### No Scene Loaded[#](#no-scene-loaded)

`applyTemplateFromString()` and `applyTemplateFromURL()` require an existing scene. Create one first with `cesdk.createDesignScene()` or `engine.scene.create()`.

### Template URL Not Accessible[#](#template-url-not-accessible)

Verify CORS configuration allows fetching from the template URL. Check network connectivity and URL validity.

### Content Not Scaling as Expected[#](#content-not-scaling-as-expected)

Template content scales to fit the current page dimensions. Verify page dimensions are set before applying the template.

## Related Guides[#](#related-guides)

*   [Use Templates Programmatically](vue/use-templates/programmatic-9349f3/) — Comprehensive programmatic template workflows
*   [Templates Overview](vue/use-templates/overview-ae74e1/) — Understanding templates in CE.SDK
*   [Headless Mode](vue/concepts/headless-mode/browser-24ab98/) — Server-side template processing

---



[Source](https:/img.ly/docs/cesdk/vue/text/overview-0bd620)