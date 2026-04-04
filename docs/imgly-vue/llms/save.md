# Save

Save and serialize designs in CE.SDK for later retrieval, sharing, or storage using string or archive formats.

![Save designs showing different save format options](/docs/cesdk/_astro/browser.hero.DorB6Lk1_LBkkq.webp)

8 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples)[

GitHub](https://github.com/imgly/cesdk-web-examples)

CE.SDK provides two formats for persisting designs. Choose the format based on your storage and portability requirements.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
/** * CE.SDK Plugin: Save Designs Guide * * Demonstrates how to save and serialize designs in CE.SDK: * - Saving scenes to string format for database storage * - Saving scenes to archive format with embedded assets * - Using built-in save actions and customization */class Example implements EditorPlugin {  name = packageJson.name;
  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (cesdk == null) {      throw new Error('CE.SDK instance is required');    }
    const engine = cesdk.engine;
    await engine.scene.loadFromURL(      'https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene'    );
    const page = engine.scene.getCurrentPage();    if (page == null) {      throw new Error('No page found in scene');    }    engine.scene.zoomToBlock(page, { padding: 40 });
    cesdk.actions.register('saveScene', async () => {      const sceneString = await engine.scene.saveToString();      // Send to your backend API      console.log('Custom save:', sceneString.length, 'bytes');    });
    // Button: Save Scene & Download    const handleSaveScene = async () => {      const sceneString = await engine.scene.saveToString();      const sceneBlob = new Blob([sceneString], {        type: 'application/octet-stream'      });      await cesdk.utils.downloadFile(sceneBlob, 'application/octet-stream');      cesdk.ui.showNotification({        message: `Scene downloaded (${(sceneString.length / 1024).toFixed(1)} KB)`,        type: 'success'      });    };
    // Button: Save to Archive & Download    const handleSaveToArchive = async () => {      const archiveBlob = await engine.scene.saveToArchive();      await cesdk.utils.downloadFile(archiveBlob, 'application/zip');      cesdk.ui.showNotification({        message: `Archive downloaded (${(archiveBlob.size / 1024).toFixed(1)} KB)`,        type: 'success'      });    };
    const handleLoadScene = async () => {      await cesdk.actions.run('importScene', { format: 'scene' });    };
    const handleLoadArchive = async () => {      await cesdk.actions.run('importScene', { format: 'archive' });      const loadedPage = engine.scene.getCurrentPage();      if (loadedPage != null) {        engine.scene.zoomToBlock(loadedPage, { padding: 40 });      }    };
    cesdk.ui.insertNavigationBarOrderComponent('last', {      id: 'ly.img.actions.navigationBar',      children: [        {          id: 'ly.img.action.navigationBar',          key: 'save-scene',          label: 'Save Scene',          icon: '@imgly/Save',          onClick: handleSaveScene        },        {          id: 'ly.img.action.navigationBar',          key: 'save-archive',          label: 'Save Archive',          icon: '@imgly/Download',          onClick: handleSaveToArchive        },        {          id: 'ly.img.action.navigationBar',          key: 'load-scene',          label: 'Load Scene',          icon: '@imgly/Upload',          onClick: handleLoadScene        },        {          id: 'ly.img.action.navigationBar',          key: 'load-archive',          label: 'Load Archive',          icon: '@imgly/Upload',          onClick: handleLoadArchive        }      ]    });  }}
export default Example;
```

## Save Format Comparison[#](#save-format-comparison)

| Format | Method | Assets | Best For |
| --- | --- | --- | --- |
| String | `saveToString()` | Referenced by URL | Database storage, cloud sync |
| Archive | `saveToArchive()` | Embedded in ZIP | Offline use, file sharing |

**String format** produces a lightweight Base64-encoded string where assets remain as URL references. Use this when asset URLs will remain accessible.

**Archive format** creates a self-contained ZIP with all assets embedded. Use this for portable designs that work offline.

## Save to String[#](#save-to-string)

Serialize the current scene to a Base64-encoded string suitable for database storage.

```
const sceneString = await engine.scene.saveToString();
```

The string contains the complete scene structure but references assets by their original URLs.

## Save to Archive[#](#save-to-archive)

Create a self-contained ZIP file with the scene and all embedded assets.

```
const archiveBlob = await engine.scene.saveToArchive();
```

The archive includes all pages, elements, and asset data in a single portable file.

## Download to User Device[#](#download-to-user-device)

Use `cesdk.utils.downloadFile()` to trigger a browser download with the correct MIME type.

For scene strings, convert to a Blob first:

```
const sceneBlob = new Blob([sceneString], {  type: 'application/octet-stream'});await cesdk.utils.downloadFile(sceneBlob, 'application/octet-stream');
```

For archive blobs, pass directly to the download utility:

```
await cesdk.utils.downloadFile(archiveBlob, 'application/zip');
```

This utility handles creating and revoking object URLs automatically.

## Load Scene from File[#](#load-scene-from-file)

Use the built-in `importScene` action to open a file picker for `.scene` files. This restores a previously saved design from its serialized string format.

```
const handleLoadScene = async () => {  await cesdk.actions.run('importScene', { format: 'scene' });};
```

Scene files are lightweight but require the original asset URLs to remain accessible.

## Load Archive from File[#](#load-archive-from-file)

Load a self-contained `.zip` archive that includes all embedded assets.

```
const handleLoadArchive = async () => {  await cesdk.actions.run('importScene', { format: 'archive' });
```

Archives are portable and work offline since all assets are bundled within the file.

## Built-in Save Action[#](#built-in-save-action)

CE.SDK includes a built-in `saveScene` action that integrates with the navigation bar.

### Running an Action[#](#running-an-action)

Trigger the default save behavior programmatically using `actions.run()`:

```
await cesdk.actions.run('saveScene');
```

This executes the registered handler for `saveScene`, which by default downloads the scene file.

### Customizing an Action[#](#customizing-an-action)

Override the default behavior by registering a custom handler:

```
cesdk.actions.register('saveScene', async () => {  const sceneString = await engine.scene.saveToString();  // Send to your backend API  console.log('Custom save:', sceneString.length, 'bytes');});
```

The registered handler runs when the built-in save button is clicked or when the action is triggered via `actions.run()`.

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `engine.scene.saveToString()` | Serialize scene to Base64 string |
| `engine.scene.saveToArchive()` | Save scene with assets as ZIP blob |
| `engine.scene.loadFromString()` | Load scene from serialized string |
| `engine.scene.loadFromArchive()` | Load scene from archive blob |
| `engine.scene.loadFromURL()` | Load scene from remote URL |
| `engine.scene.loadFromArchiveURL()` | Load scene from remote ZIP archive |
| `cesdk.utils.downloadFile()` | Download blob or string to user device |
| `cesdk.actions.run()` | Execute a registered action with parameters |
| `cesdk.actions.register()` | Register or override an action handler |

## Next Steps[#](#next-steps)

*   [Export Overview](vue/export-save-publish/export/overview-9ed3a8/) \- Export designs to image, PDF, and video formats
*   [Load Scene](vue/open-the-editor/load-scene-478833/) \- Load scenes from remote URLs and archives
*   [Store Custom Metadata](vue/export-save-publish/store-custom-metadata-337248/) \- Attach metadata like tags or version info to designs
*   [Partial Export](vue/export-save-publish/export/partial-export-89aaf6/) \- Export individual blocks or selections

---



[Source](https:/img.ly/docs/cesdk/vue/export-save-publish/for-social-media-0e8a92)