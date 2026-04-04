# Store Custom Metadata

Attach custom key-value metadata to design blocks in CE.SDK for tracking asset origins, storing application state, or linking to external systems.

![Store Custom Metadata example showing an image block with metadata](/docs/cesdk/_astro/browser.hero.D7VjuxYX_Z1280Ny.webp)

5 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-export-save-publish-store-custom-metadata-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-export-save-publish-store-custom-metadata-browser)

Metadata lets you attach arbitrary string key-value pairs to any design block. This data is invisible to end users but persists with the scene through save/load operations. Common use cases include tracking asset origins, storing application-specific state, and linking blocks to external databases or content management systems.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
/** * CE.SDK Plugin: Store Custom Metadata Guide * * Demonstrates how to attach, retrieve, and manage custom metadata on design blocks: * - Setting metadata key-value pairs * - Getting metadata values by key * - Checking if metadata exists * - Listing all metadata keys * - Removing metadata * - Storing structured data as JSON */class Example implements EditorPlugin {  name = packageJson.name;
  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    // Initialize CE.SDK with Design mode    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Design',      withUploadAssetSources: true    });    await cesdk.createDesignScene();
    const engine = cesdk.engine;    const page = engine.block.findByType('page')[0];
    // Set page dimensions    engine.block.setWidth(page, 800);    engine.block.setHeight(page, 600);
    // Create an image block to attach metadata to    const imageBlock = await engine.block.addImage(      'https://img.ly/static/ubq_samples/sample_1.jpg',      { size: { width: 400, height: 300 } }    );    engine.block.appendChild(page, imageBlock);    engine.block.setPositionX(imageBlock, 200);    engine.block.setPositionY(imageBlock, 150);
    // Set metadata key-value pairs on the block    engine.block.setMetadata(imageBlock, 'externalId', 'asset-12345');    engine.block.setMetadata(imageBlock, 'source', 'user-upload');    engine.block.setMetadata(imageBlock, 'uploadedBy', 'user@example.com');    console.log('Set metadata: externalId, source, uploadedBy');
    // Retrieve a metadata value by key    if (engine.block.hasMetadata(imageBlock, 'externalId')) {      const externalId = engine.block.getMetadata(imageBlock, 'externalId');      console.log('External ID:', externalId);    }
    // List all metadata keys on the block    const allKeys = engine.block.findAllMetadata(imageBlock);    console.log('All metadata keys:', allKeys);
    // Log all key-value pairs    for (const key of allKeys) {      const value = engine.block.getMetadata(imageBlock, key);      console.log(`  ${key}: ${value}`);    }
    // Store structured data as JSON    const generationInfo = {      source: 'ai-generated',      model: 'stable-diffusion',      timestamp: Date.now()    };    engine.block.setMetadata(      imageBlock,      'generationInfo',      JSON.stringify(generationInfo)    );
    // Retrieve and parse structured data    const retrievedJson = engine.block.getMetadata(      imageBlock,      'generationInfo'    );    const parsedInfo = JSON.parse(retrievedJson);    console.log('Parsed generation info:', parsedInfo);
    // Remove a metadata key    engine.block.removeMetadata(imageBlock, 'uploadedBy');    console.log('Removed metadata key: uploadedBy');
    // Verify the key was removed    const hasUploadedBy = engine.block.hasMetadata(imageBlock, 'uploadedBy');    console.log('Has uploadedBy after removal:', hasUploadedBy);
    // List remaining keys    const remainingKeys = engine.block.findAllMetadata(imageBlock);    console.log('Remaining metadata keys:', remainingKeys);
    // Select the image block to show it in focus    engine.block.select(imageBlock);
    console.log(      'Metadata guide initialized. Check the console for metadata operations.'    );  }}
export default Example;
```

This guide covers how to set, retrieve, list, and remove metadata on blocks, as well as how to store structured data as JSON strings.

## Initialize CE.SDK[#](#initialize-cesdk)

We start by initializing CE.SDK with a basic configuration. The metadata APIs are available on the `engine.block` namespace.

```
// Initialize CE.SDK with Design modeawait cesdk.addDefaultAssetSources();await cesdk.addDemoAssetSources({  sceneMode: 'Design',  withUploadAssetSources: true});await cesdk.createDesignScene();
const engine = cesdk.engine;const page = engine.block.findByType('page')[0];
// Set page dimensionsengine.block.setWidth(page, 800);engine.block.setHeight(page, 600);
// Create an image block to attach metadata toconst imageBlock = await engine.block.addImage(  'https://img.ly/static/ubq_samples/sample_1.jpg',  { size: { width: 400, height: 300 } });engine.block.appendChild(page, imageBlock);engine.block.setPositionX(imageBlock, 200);engine.block.setPositionY(imageBlock, 150);
```

## Set Metadata[#](#set-metadata)

Use `engine.block.setMetadata()` to attach a key-value pair to a block. Both the key and value must be strings. If the key already exists, the value is overwritten.

```
// Set metadata key-value pairs on the blockengine.block.setMetadata(imageBlock, 'externalId', 'asset-12345');engine.block.setMetadata(imageBlock, 'source', 'user-upload');engine.block.setMetadata(imageBlock, 'uploadedBy', 'user@example.com');console.log('Set metadata: externalId, source, uploadedBy');
```

You can attach multiple metadata entries to a single block. Each entry is independent and can be accessed, modified, or removed separately.

## Get Metadata[#](#get-metadata)

Use `engine.block.getMetadata()` to retrieve a value by its key. This method throws an error if the key doesn’t exist, so always check with `hasMetadata()` first for conditional access.

```
// Retrieve a metadata value by keyif (engine.block.hasMetadata(imageBlock, 'externalId')) {  const externalId = engine.block.getMetadata(imageBlock, 'externalId');  console.log('External ID:', externalId);}
```

The `hasMetadata()` method returns `true` if the block has metadata for the specified key, and `false` otherwise. This pattern prevents runtime errors when accessing metadata that may not be set.

## List All Metadata Keys[#](#list-all-metadata-keys)

Use `engine.block.findAllMetadata()` to get an array of all metadata keys stored on a block.

```
// List all metadata keys on the blockconst allKeys = engine.block.findAllMetadata(imageBlock);console.log('All metadata keys:', allKeys);
// Log all key-value pairsfor (const key of allKeys) {  const value = engine.block.getMetadata(imageBlock, key);  console.log(`  ${key}: ${value}`);}
```

This is useful for iterating through all metadata on a block or debugging what metadata is attached.

## Store Structured Data[#](#store-structured-data)

Since metadata values must be strings, you can store structured data by serializing it to JSON. Parse the JSON when retrieving the data.

```
// Store structured data as JSONconst generationInfo = {  source: 'ai-generated',  model: 'stable-diffusion',  timestamp: Date.now()};engine.block.setMetadata(  imageBlock,  'generationInfo',  JSON.stringify(generationInfo));
// Retrieve and parse structured dataconst retrievedJson = engine.block.getMetadata(  imageBlock,  'generationInfo');const parsedInfo = JSON.parse(retrievedJson);console.log('Parsed generation info:', parsedInfo);
```

This pattern lets you store complex objects like configuration settings, generation parameters, or any structured information that can be serialized to JSON.

## Remove Metadata[#](#remove-metadata)

Use `engine.block.removeMetadata()` to delete a key-value pair from a block. This method does not throw an error if the key doesn’t exist.

```
// Remove a metadata keyengine.block.removeMetadata(imageBlock, 'uploadedBy');console.log('Removed metadata key: uploadedBy');
```

After removal, you can verify the key was deleted by checking with `hasMetadata()`.

```
// Verify the key was removedconst hasUploadedBy = engine.block.hasMetadata(imageBlock, 'uploadedBy');console.log('Has uploadedBy after removal:', hasUploadedBy);
// List remaining keysconst remainingKeys = engine.block.findAllMetadata(imageBlock);console.log('Remaining metadata keys:', remainingKeys);
```

## Metadata Persistence[#](#metadata-persistence)

Metadata is automatically preserved when saving scenes with `engine.scene.saveToString()` or `engine.scene.saveToArchive()`. When loading a saved scene, all metadata is restored to the blocks.

Metadata is only preserved when saving the scene data. Exporting to image or video formats (PNG, JPEG, MP4) does not include metadata since these are final output formats.

## Troubleshooting[#](#troubleshooting)

### getMetadata Throws Error[#](#getmetadata-throws-error)

If `getMetadata()` throws an error, the key doesn’t exist on the block. Always use `hasMetadata()` to check before retrieving:

```
if (engine.block.hasMetadata(block, 'myKey')) {  const value = engine.block.getMetadata(block, 'myKey');}
```

### Metadata Lost After Load[#](#metadata-lost-after-load)

Ensure you’re saving with `saveToString()` or `saveToArchive()`, not exporting to image/video formats. Only scene saves preserve metadata.

### Large Metadata Values[#](#large-metadata-values)

Metadata is designed for small strings. Very large values may impact performance during save/load operations. For large data, consider storing a reference (like a URL or ID) rather than the data itself.

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `engine.block.setMetadata(block, key, value)` | Set a metadata key-value pair on a block |
| `engine.block.getMetadata(block, key)` | Get the value for a metadata key |
| `engine.block.hasMetadata(block, key)` | Check if a metadata key exists |
| `engine.block.findAllMetadata(block)` | List all metadata keys on a block |
| `engine.block.removeMetadata(block, key)` | Remove a metadata key-value pair |

---



[Source](https:/img.ly/docs/cesdk/vue/export-save-publish/save-c8b124)