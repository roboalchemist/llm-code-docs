# Basics

CE.SDK treats all insertable content as assets—images, videos, audio, stickers, shapes, templates, and text presets flow through a unified asset system.

![Asset Library Basics example showing the CE.SDK editor with a custom asset library entry in the dock](/docs/cesdk/_astro/browser.hero.vxyZgRk9_Z1xRw4S.webp)

5 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-import-media-asset-library-basics-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-import-media-asset-library-basics-browser)

The asset library connects the engine to the user interface through three layers:

```
┌─────────────────────────────────────────────────────────────┐│  User Interface                                             ││  ┌─────────────┐    references    ┌──────────────────────┐  ││  │  Dock Entry │ ───────────────▶ │ Asset Library Entry  │  ││  │  (Button)   │                  │ (Display Config)     │  ││  └─────────────┘                  └──────────┬───────────┘  ││                                              │ queries      │├──────────────────────────────────────────────│──────────────┤│  Engine                                      ▼              ││                                   ┌──────────────────────┐  ││                                   │    Asset Source      │  ││                                   │    (Data Provider)   │  ││                                   └──────────────────────┘  │└─────────────────────────────────────────────────────────────┘
```

The following example demonstrates all three layers working together:

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
/** * CE.SDK Plugin: Asset Library Basics Guide * * Demonstrates the asset library architecture: * - Creating a custom asset source (engine layer) * - Creating an asset library entry (UI configuration layer) * - Connecting the entry to the dock (UI interaction layer) */class Example implements EditorPlugin {  name = packageJson.name;
  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({ sceneMode: 'Design' });    await cesdk.createDesignScene();
    // Layer 1: Asset Source - provides assets to the UI    cesdk.engine.asset.addSource({      id: 'my-custom-images',      findAssets: async () => ({        assets: [          {            id: 'sample-1',            meta: {              uri: 'https://img.ly/static/ubq_samples/sample_1.jpg',              thumbUri: 'https://img.ly/static/ubq_samples/sample_1.jpg',              width: 1920,              height: 1280            }          },          {            id: 'sample-2',            meta: {              uri: 'https://img.ly/static/ubq_samples/sample_2.jpg',              thumbUri: 'https://img.ly/static/ubq_samples/sample_2.jpg',              width: 1920,              height: 1280            }          },          {            id: 'sample-3',            meta: {              uri: 'https://img.ly/static/ubq_samples/sample_3.jpg',              thumbUri: 'https://img.ly/static/ubq_samples/sample_3.jpg',              width: 1920,              height: 1280            }          }        ],        total: 3,        currentPage: 1,        nextPage: undefined      }),      applyAsset: async (assetResult) =>        cesdk.engine.asset.defaultApplyAsset(assetResult)    });
    // Layer 2: Asset Library Entry - connects sources to display settings    cesdk.ui.addAssetLibraryEntry({      id: 'my-images-entry',      sourceIds: ['my-custom-images'],      previewLength: 3,      gridColumns: 3,      gridItemHeight: 'square'    });
    // Layer 3: Dock - adds button to access the entry    cesdk.ui.setDockOrder([      {        id: 'ly.img.assetLibrary.dock',        key: 'my-images-entry',        label: 'libraries.my-images-entry.label',        entries: ['my-images-entry']      },      ...cesdk.ui.getDockOrder()    ]);    cesdk.i18n.setTranslations({      en: { 'libraries.my-images-entry.label': 'My Images' }    });
    // Query registered entries    const allEntries = cesdk.ui.findAllAssetLibraryEntries();    console.log('Registered entries:', allEntries);
    const myEntry = cesdk.ui.getAssetLibraryEntry('my-images-entry');    console.log('My entry:', myEntry);
    // Open the panel to show the custom assets immediately    cesdk.ui.openPanel('//ly.img.panel/assetLibrary', {      payload: { entries: ['my-images-entry'] }    });  }}
export default Example;
```

This guide covers:

*   Registering asset sources with the engine
*   Creating asset library entries to configure display settings
*   Adding entries to the dock for user access

## Layer 1: Asset Source[#](#layer-1-asset-source)

Asset sources provide data through `findAssets` and handle insertion through `applyAsset`. Register them with `engine.asset.addSource()`.

```
// Layer 1: Asset Source - provides assets to the UIcesdk.engine.asset.addSource({  id: 'my-custom-images',  findAssets: async () => ({    assets: [      {        id: 'sample-1',        meta: {          uri: 'https://img.ly/static/ubq_samples/sample_1.jpg',          thumbUri: 'https://img.ly/static/ubq_samples/sample_1.jpg',          width: 1920,          height: 1280        }      },      {        id: 'sample-2',        meta: {          uri: 'https://img.ly/static/ubq_samples/sample_2.jpg',          thumbUri: 'https://img.ly/static/ubq_samples/sample_2.jpg',          width: 1920,          height: 1280        }      },      {        id: 'sample-3',        meta: {          uri: 'https://img.ly/static/ubq_samples/sample_3.jpg',          thumbUri: 'https://img.ly/static/ubq_samples/sample_3.jpg',          width: 1920,          height: 1280        }      }    ],    total: 3,    currentPage: 1,    nextPage: undefined  }),  applyAsset: async (assetResult) =>    cesdk.engine.asset.defaultApplyAsset(assetResult)});
```

For details on asset source configuration, see the [Asset Sources concept](sveltekit/import-media/concepts-5e6197/) .

## Layer 2: Asset Library Entry[#](#layer-2-asset-library-entry)

Entries connect asset sources to display settings. Create them with `cesdk.ui.addAssetLibraryEntry()`.

```
// Layer 2: Asset Library Entry - connects sources to display settingscesdk.ui.addAssetLibraryEntry({  id: 'my-images-entry',  sourceIds: ['my-custom-images'],  previewLength: 3,  gridColumns: 3,  gridItemHeight: 'square'});
```

For display properties like `gridColumns` and `previewLength`, see the [Thumbnails](sveltekit/import-media/asset-panel/thumbnails-c23949/) guide.

## Layer 3: Dock[#](#layer-3-dock)

Add entries to the dock with `cesdk.ui.setDockOrder()` using the `ly.img.assetLibrary.dock` component type.

```
// Layer 3: Dock - adds button to access the entrycesdk.ui.setDockOrder([  {    id: 'ly.img.assetLibrary.dock',    key: 'my-images-entry',    label: 'libraries.my-images-entry.label',    entries: ['my-images-entry']  },  ...cesdk.ui.getDockOrder()]);cesdk.i18n.setTranslations({  en: { 'libraries.my-images-entry.label': 'My Images' }});
```

## Managing Entries[#](#managing-entries)

Query and inspect registered entries:

```
// Query registered entriesconst allEntries = cesdk.ui.findAllAssetLibraryEntries();console.log('Registered entries:', allEntries);
const myEntry = cesdk.ui.getAssetLibraryEntry('my-images-entry');console.log('My entry:', myEntry);
```

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `findAllAssetLibraryEntries()` | List all registered entry IDs |
| `getAssetLibraryEntry(id)` | Get entry configuration |
| `addAssetLibraryEntry(entry)` | Register a new entry |
| `removeAssetLibraryEntry(id)` | Remove an entry |

## Next Steps[#](#next-steps)

*   [Customize](sveltekit/import-media/asset-panel/customize-c9a4de/) — Icons, i18n, replace libraries
*   [Thumbnails](sveltekit/import-media/asset-panel/thumbnails-c23949/) — Thumbnail URIs, display settings
*   [Refresh Assets](sveltekit/import-media/asset-panel/refresh-assets-382060/) — Trigger asset reloads
*   [Asset Sources](sveltekit/import-media/concepts-5e6197/) — Creating asset sources

---



[Source](https:/img.ly/docs/cesdk/sveltekit/export-save-publish/export/with-color-mask-4f868f)