# Import Templates

Load design templates into CE.SDK from archive URLs, scene URLs, and serialized strings.

![Import Templates](/docs/cesdk/_astro/browser.hero.D5xXl9Ck_ZnAA.webp)

5 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-create-templates-import-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-create-templates-import-browser)

Templates are pre-designed scenes that provide starting points for user projects. CE.SDK supports loading templates from archive URLs with bundled assets, remote scene URLs, or serialized strings stored in databases.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
// Import scene file as string for loadFromString demonstrationimport businessCardSceneString from './assets/business-card.scene?raw';
// Template sourcesconst fashionAdArchiveUrl =  'https://cdn.img.ly/assets/templates/starterkits/16-9-fashion-ad.zip';
const postcardSceneUrl =  'https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene';
/** * CE.SDK Plugin: Import Templates * * Demonstrates loading templates from different sources: * - Archive URLs (.zip files with bundled assets) * - Scene URLs (.scene files) * - Serialized strings (imported scene content) */class Example implements EditorPlugin {  name = packageJson.name;  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (cesdk == null) {      throw new Error('CE.SDK instance is required for this plugin');    }
    const engine = cesdk.engine;
    // Load template from a scene file URL    await engine.scene.loadFromURL(postcardSceneUrl);
    // Zoom viewport to fit the loaded scene    const scene = engine.scene.get();    if (scene != null) {      await engine.scene.zoomToBlock(scene, { padding: 40 });    }
    // Verify the loaded scene    const loadedScene = engine.scene.get();    if (loadedScene != null) {      const pages = engine.scene.getPages();      console.log(`Template loaded with ${pages.length} page(s)`);    }
    // Configure navigation bar with template loading buttons    cesdk.ui.setNavigationBarOrder([      'ly.img.undoRedo.navigationBar',      'ly.img.spacer',      {        id: 'ly.img.action.navigationBar',        key: 'load-archive',        label: 'Import Archive',        icon: '@imgly/Download',        variant: 'regular',        onClick: async () => {          // Load template from archive URL (bundled assets)          await engine.scene.loadFromArchiveURL(fashionAdArchiveUrl);          const s = engine.scene.get();          if (s != null) {            await engine.scene.zoomToBlock(s, { padding: 40 });          }        }      },      {        id: 'ly.img.action.navigationBar',        key: 'load-url',        label: 'Import URL',        icon: '@imgly/Download',        variant: 'regular',        onClick: async () => {          // Load template from scene URL          await engine.scene.loadFromURL(postcardSceneUrl);          const s = engine.scene.get();          if (s != null) {            await engine.scene.zoomToBlock(s, { padding: 40 });          }        }      },      {        id: 'ly.img.action.navigationBar',        key: 'load-string',        label: 'Import String',        icon: '@imgly/Download',        variant: 'regular',        onClick: async () => {          // Load template from serialized string          await engine.scene.loadFromString(businessCardSceneString);          const s = engine.scene.get();          if (s != null) {            await engine.scene.zoomToBlock(s, { padding: 40 });          }        }      }    ]);  }}
export default Example;
```

This guide covers how to load templates from archives, URLs, and strings, and work with the loaded content.

## Load from Archive[#](#load-from-archive)

Load a template from an archive URL using `loadFromArchiveURL()`. Archives are `.zip` files that bundle the scene with all its assets, making them portable and self-contained.

```
// Load template from archive URL (bundled assets)await engine.scene.loadFromArchiveURL(fashionAdArchiveUrl);
```

## Load from URL[#](#load-from-url)

Load a template from a remote `.scene` file URL using `loadFromURL()`. The scene file is a JSON-based format that references assets via URLs.

```
// Load template from a scene file URLawait engine.scene.loadFromURL(postcardSceneUrl);
```

## Load from String[#](#load-from-string)

For templates stored in databases or received from APIs, load from a serialized string using `loadFromString()`. This method works with content previously saved using `engine.scene.saveToString()`.

```
// Load template from serialized stringawait engine.scene.loadFromString(businessCardSceneString);
```

## Working with the Loaded Scene[#](#working-with-the-loaded-scene)

After loading a template, you can verify its contents and adjust the viewport.

### Verify the Scene[#](#verify-the-scene)

Use `engine.scene.get()` to retrieve the scene block and `engine.scene.getPages()` to inspect its pages.

```
// Verify the loaded sceneconst loadedScene = engine.scene.get();if (loadedScene != null) {  const pages = engine.scene.getPages();  console.log(`Template loaded with ${pages.length} page(s)`);}
```

### Zoom to Content[#](#zoom-to-content)

Fit the loaded template in the viewport using `zoomToBlock()` with optional padding.

```
// Zoom viewport to fit the loaded sceneconst scene = engine.scene.get();if (scene != null) {  await engine.scene.zoomToBlock(scene, { padding: 40 });}
```

---



[Source](https:/img.ly/docs/cesdk/vue/create-templates/from-scratch-663cda)