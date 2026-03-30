# Source: https://img.ly/docs/cesdk/vue/open-the-editor/from-template-46c096/

---
title: "Create From Template"
description: "Start the editor with a pre-designed template for faster editing and consistent output."
platform: vue
url: "https://img.ly/docs/cesdk/vue/open-the-editor/from-template-46c096/"
---

> This is one page of the CE.SDK Vue documentation. For a complete overview, see the [Vue Documentation Index](https://img.ly/docs/cesdk/vue.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/vue/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/vue/guides-8d8b00/) > [Open the Editor](https://img.ly/docs/cesdk/vue/open-the-editor-23a1db/) > [Create From Template](https://img.ly/docs/cesdk/vue/open-the-editor/from-template-46c096/)

---

Load pre-designed templates to give users a professional starting point instead of a blank canvas.

![Create From Template example showing a postcard template loaded in the editor](./assets/browser.hero.webp)

> **Reading time:** 5 minutes
>
> **Resources:**
>
> - [Download examples](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)
>
> - [View source on GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-open-the-editor-from-template-browser)
>
> - [Open in StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-open-the-editor-from-template-browser)
>
> - [Live demo](https://img.ly/docs/cesdk/examples/guides-open-the-editor-from-template-browser/)

Templates provide consistent layouts and styling that users can customize for their needs. CE.SDK supports loading templates from remote URLs, local strings, and applying template content to existing scenes while preserving page dimensions.

```typescript file=@cesdk_web_examples/guides-open-the-editor-from-template-browser/browser.ts reference-only
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';

import {
  BlurAssetSource,
  ColorPaletteAssetSource,
  CropPresetsAssetSource,
  DemoAssetSources,
  EffectsAssetSource,
  FiltersAssetSource,
  PagePresetsAssetSource,
  StickerAssetSource,
  TextAssetSource,
  TextComponentAssetSource,
  TypefaceAssetSource,
  UploadAssetSources,
  VectorShapeAssetSource
} from '@cesdk/cesdk-js/plugins';
import { DesignEditorConfig } from './design-editor/plugin';
import packageJson from './package.json';
import businessCardSceneString from './assets/business-card.scene?raw';

class Example implements EditorPlugin {
  name = packageJson.name;
  version = packageJson.version;

  async initialize({ cesdk }: EditorPluginContext): Promise<void> {
    if (cesdk == null) {
      throw new Error('CE.SDK instance is required for this plugin');
    }

    const engine = cesdk.engine;
    const templateUrl =
      'https://cdn.img.ly/assets/demo/v3/ly.img.template/templates/cesdk_postcard_1.scene';
    await engine.scene.loadFromURL(templateUrl);

    const textBlocks = engine.block.findByType('text');
    if (textBlocks.length > 0) {
      engine.block.replaceText(textBlocks[0], 'Welcome to CE.SDK');
    }

    // Zoom to fit the page in view
    const pages = engine.block.findByType('page');
    if (pages.length > 0) {
      engine.scene.zoomToBlock(pages[0]);
    }

    // Add custom navigation bar actions for template operations
    cesdk.ui.insertOrderComponent({ in: 'ly.img.navigation.bar', position: 'end' }, {
      id: 'ly.img.actions.navigationBar',
      children: [
        {
          id: 'ly.img.action.navigationBar',
          key: 'load-from-string-action',
          label: 'Load from String',
          iconName: '@imgly/icons/Essentials/Download',
          onClick: async () => {
            await engine.scene.loadFromString(businessCardSceneString);
            const scene = engine.scene.get();
            if (scene != null) {
              await engine.scene.zoomToBlock(scene, { padding: 40 });
            }
          }
        },
        {
          id: 'ly.img.action.navigationBar',
          key: 'apply-template-action',
          label: 'Apply Template',
          iconName: '@imgly/icons/Essentials/TemplateLibrary',
          onClick: async () => {
            const applyTemplateUrl =
              'https://cdn.img.ly/assets/demo/v3/ly.img.template/templates/cesdk_instagram_photo_1.scene';
            await engine.scene.applyTemplateFromURL(applyTemplateUrl);
            const scene = engine.scene.get();
            if (scene != null) {
              await engine.scene.zoomToBlock(scene, { padding: 40 });
            }
          }
        }
      ]
    });
  }
}

export default Example;
```

This guide covers how to load templates from URLs and strings, and how to apply templates to existing scenes.

## Load a Template from URL

The most common approach is loading templates from a remote URL. The engine replaces any existing scene with the loaded template.

```typescript highlight-load-from-url
const templateUrl =
  'https://cdn.img.ly/assets/demo/v3/ly.img.template/templates/cesdk_postcard_1.scene';
await engine.scene.loadFromURL(templateUrl);
```

The template URL should point to a valid `.scene` file hosted on a server with appropriate CORS headers.

## Load a Template from String

When templates are stored in a database or retrieved from custom storage, use `engine.scene.loadFromString()`. This accepts the scene data as a string, typically from a previous `engine.scene.saveToString()` call.

```typescript highlight-load-from-string
await engine.scene.loadFromString(businessCardSceneString);
```

This approach is useful for loading templates from your backend API, restoring saved user designs, or working with templates stored in databases.

## Apply a Template to an Existing Scene

To apply template content while preserving the current page dimensions, use `engine.scene.applyTemplateFromURL()`. The template content automatically adjusts to fit the existing page size.

```typescript highlight-apply-template
await engine.scene.applyTemplateFromURL(applyTemplateUrl);
```

This is useful when users have already set up a canvas size and you want to populate it with template content without changing the dimensions.

## Modify Template Content

After loading a template, customize the content using block APIs. Find elements and modify them as needed.

```typescript highlight-modify-content
const textBlocks = engine.block.findByType('text');
if (textBlocks.length > 0) {
  engine.block.replaceText(textBlocks[0], 'Welcome to CE.SDK');
}
```

Common modifications include:

- **Updating text content**: `engine.block.replaceText(blockId, 'New text')`
- **Swapping images**: `engine.block.setString(fill, 'fill/image/imageFileURI', newUrl)`
- **Adjusting colors**: `engine.block.setColor(blockId, 'fill/solid/color', newColor)`

## Troubleshooting

### Template Fails to Load

- Verify the template URL is accessible and returns a valid scene file
- Check CORS headers allow fetching from the template source
- Ensure the template format is compatible with your CE.SDK version

### Assets Not Displaying After Load

- Template scene files store asset references as URLs; ensure those URLs remain accessible
- Use archives (`.zip`) for self-contained templates with bundled assets
- Configure a URI resolver if assets are hosted on different servers

## API Reference

| Method | Description |
| ------ | ----------- |
| `engine.scene.loadFromURL()` | Load a scene from a remote URL |
| `engine.scene.loadFromString()` | Load a scene from a string |
| `engine.scene.applyTemplateFromURL()` | Apply template to existing scene from URL |
| `engine.scene.applyTemplateFromString()` | Apply template to existing scene from string |
| `engine.block.findByType()` | Find blocks by type |
| `engine.block.findByKind()` | Find blocks by kind |
| `engine.block.replaceText()` | Replace text content in a text block |

## Next Steps

- [Load a Scene](https://img.ly/docs/cesdk/vue/open-the-editor/load-scene-478833/) - Load saved scenes from various sources
- [Save a Design](https://img.ly/docs/cesdk/vue/export-save-publish/save-c8b124/) - Save your customized template
- [Import a Design](https://img.ly/docs/cesdk/vue/open-the-editor/import-design-73b9c5/) - Import designs from archives or other formats



---

## More Resources

- **[Vue Documentation Index](https://img.ly/docs/cesdk/vue.md)** - Browse all Vue documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/vue/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/vue/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
