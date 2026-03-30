# Create From Template

Load pre-designed templates to give users a professional starting point instead of a blank canvas.

![Create From Template example showing a postcard template loaded in the editor](/docs/cesdk/_astro/browser.hero.CU3x7gwE_Zk4D8F.webp)

5 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-open-the-editor-from-template-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-open-the-editor-from-template-browser)

Templates provide consistent layouts and styling that users can customize for their needs. CE.SDK supports loading templates from remote URLs, local strings, and applying template content to existing scenes while preserving page dimensions.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';import businessCardSceneString from './assets/business-card.scene?raw';
class Example implements EditorPlugin {  name = packageJson.name;  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (cesdk == null) {      throw new Error('CE.SDK instance is required for this plugin');    }
    const engine = cesdk.engine;
    // Add default asset sources for template resources    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Design',      withUploadAssetSources: true    });
    const templateUrl =      'https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene';    await engine.scene.loadFromURL(templateUrl);
    const textBlocks = engine.block.findByType('text');    if (textBlocks.length > 0) {      engine.block.replaceText(textBlocks[0], 'Welcome to CE.SDK');    }
    // Zoom to fit the page in view    const pages = engine.block.findByType('page');    if (pages.length > 0) {      engine.scene.zoomToBlock(pages[0]);    }
    // Add custom navigation bar actions for template operations    cesdk.ui.insertNavigationBarOrderComponent('last', {      id: 'ly.img.actions.navigationBar',      children: [        {          id: 'ly.img.action.navigationBar',          key: 'load-from-string-action',          label: 'Load from String',          iconName: '@imgly/icons/Essentials/Download',          onClick: async () => {            await engine.scene.loadFromString(businessCardSceneString);            const scene = engine.scene.get();            if (scene != null) {              await engine.scene.zoomToBlock(scene, { padding: 40 });            }          }        },        {          id: 'ly.img.action.navigationBar',          key: 'apply-template-action',          label: 'Apply Template',          iconName: '@imgly/icons/Essentials/TemplateLibrary',          onClick: async () => {            const applyTemplateUrl =              'https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_instagram_photo_1.scene';            await engine.scene.applyTemplateFromURL(applyTemplateUrl);            const scene = engine.scene.get();            if (scene != null) {              await engine.scene.zoomToBlock(scene, { padding: 40 });            }          }        }      ]    });  }}
export default Example;
```

This guide covers how to load templates from URLs and strings, and how to apply templates to existing scenes.

## Load a Template from URL[#](#load-a-template-from-url)

The most common approach is loading templates from a remote URL. The engine replaces any existing scene with the loaded template.

```
const templateUrl =  'https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene';await engine.scene.loadFromURL(templateUrl);
```

The template URL should point to a valid `.scene` file hosted on a server with appropriate CORS headers.

## Load a Template from String[#](#load-a-template-from-string)

When templates are stored in a database or retrieved from custom storage, use `engine.scene.loadFromString()`. This accepts the scene data as a string, typically from a previous `engine.scene.saveToString()` call.

```
await engine.scene.loadFromString(businessCardSceneString);
```

This approach is useful for loading templates from your backend API, restoring saved user designs, or working with templates stored in databases.

## Apply a Template to an Existing Scene[#](#apply-a-template-to-an-existing-scene)

To apply template content while preserving the current page dimensions, use `engine.scene.applyTemplateFromURL()`. The template content automatically adjusts to fit the existing page size.

```
await engine.scene.applyTemplateFromURL(applyTemplateUrl);
```

This is useful when users have already set up a canvas size and you want to populate it with template content without changing the dimensions.

## Modify Template Content[#](#modify-template-content)

After loading a template, customize the content using block APIs. Find elements and modify them as needed.

```
const textBlocks = engine.block.findByType('text');if (textBlocks.length > 0) {  engine.block.replaceText(textBlocks[0], 'Welcome to CE.SDK');}
```

Common modifications include:

*   **Updating text content**: `engine.block.replaceText(blockId, 'New text')`
*   **Swapping images**: `engine.block.setString(fill, 'fill/image/imageFileURI', newUrl)`
*   **Adjusting colors**: `engine.block.setColor(blockId, 'fill/solid/color', newColor)`

## Troubleshooting[#](#troubleshooting)

### Template Fails to Load[#](#template-fails-to-load)

*   Verify the template URL is accessible and returns a valid scene file
*   Check CORS headers allow fetching from the template source
*   Ensure the template format is compatible with your CE.SDK version

### Assets Not Displaying After Load[#](#assets-not-displaying-after-load)

*   Template scene files store asset references as URLs; ensure those URLs remain accessible
*   Use archives (`.zip`) for self-contained templates with bundled assets
*   Configure a URI resolver if assets are hosted on different servers

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `engine.scene.loadFromURL()` | Load a scene from a remote URL |
| `engine.scene.loadFromString()` | Load a scene from a string |
| `engine.scene.applyTemplateFromURL()` | Apply template to existing scene from URL |
| `engine.scene.applyTemplateFromString()` | Apply template to existing scene from string |
| `engine.block.findByType()` | Find blocks by type |
| `engine.block.findByKind()` | Find blocks by kind |
| `engine.block.replaceText()` | Replace text content in a text block |

## Next Steps[#](#next-steps)

*   [Load a Scene](vue/open-the-editor/load-scene-478833/) \- Load saved scenes from various sources
*   [Save a Design](vue/export-save-publish/save-c8b124/) \- Save your customized template
*   [Import a Design](vue/open-the-editor/import-design-73b9c5/) \- Import designs from archives or other formats

---



[Source](https:/img.ly/docs/cesdk/vue/open-the-editor/from-htmlcanvas-2adf30)