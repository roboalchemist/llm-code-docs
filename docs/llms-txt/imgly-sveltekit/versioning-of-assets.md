# Versioning of Assets

Manage how CE.SDK stores and resolves asset URLs in saved designs, ensuring designs remain functional when assets are updated or moved.

![Asset versioning example showing CE.SDK editor with image blocks](/docs/cesdk/_astro/browser.hero.BEzND5cR_Z45Cut.webp)

10 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-import-media-from-remote-source-asset-versioning-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-import-media-from-remote-source-asset-versioning-browser)

CE.SDK references assets via URIs rather than embedding files directly into designs. When you save a design with `engine.scene.saveToString()`, asset URLs are stored as strings. On load, CE.SDK fetches assets from those URLs. This approach keeps saved designs small but means URL changes can break existing designs. This guide explains how CE.SDK stores asset references and strategies for managing asset URLs over time.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
/** * CE.SDK Plugin: Asset Versioning Guide * * Demonstrates how CE.SDK handles asset URLs in saved designs: * - How assets are stored as URL references * - Scene serialization vs archive export * - Inspecting and modifying asset URLs * - Strategies for versioned asset URLs */class Example implements EditorPlugin {  name = packageJson.name;
  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    // Load assets and create a design scene    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Design',      withUploadAssetSources: true    });    await cesdk.createDesignScene();
    const engine = cesdk.engine;    const page = engine.block.findByType('page')[0];
    // Set up page dimensions    engine.block.setWidth(page, 800);    engine.block.setHeight(page, 600);
    // Create an image block with a remote URL    const imageUri = 'https://img.ly/static/ubq_samples/sample_1.jpg';
    const imageBlock = await engine.block.addImage(imageUri, {      x: 50,      y: 50,      size: { width: 300, height: 200 }    });
    // Get the fill block that contains the image URI    const fill = engine.block.getFill(imageBlock);
    // Inspect the stored URI - this is exactly what gets saved in the scene    const storedUri = engine.block.getString(fill, 'fill/image/imageFileURI');    console.log('Stored image URI:', storedUri);
    // Save the scene to a string - URLs are preserved as references    const sceneString = await engine.scene.saveToString();    console.log('Scene saved to string, length:', sceneString.length);
    // The scene string contains the URL reference, not the image data itself    // This keeps the saved scene small and loads quickly
    // Alternatively, save as an archive with embedded assets    const archiveBlob = await engine.scene.saveToArchive();    console.log('Archive created, size:', archiveBlob.size, 'bytes');
    // Archives are self-contained - they include all asset data    // Use archives when designs need to work offline or across environments
    // Programmatically update an asset URL (e.g., for CDN migration)    const newUri = 'https://img.ly/static/ubq_samples/sample_2.jpg';    engine.block.setString(fill, 'fill/image/imageFileURI', newUri);
    // Verify the change    const updatedUri = engine.block.getString(fill, 'fill/image/imageFileURI');    console.log('Updated image URI:', updatedUri);
    // Find all graphic blocks to batch update their asset URLs    const graphicBlocks = engine.block.findByType('graphic');    console.log('Found graphic blocks:', graphicBlocks.length);
    // Iterate through blocks to inspect or update their fills    for (const blockId of graphicBlocks) {      const blockFill = engine.block.getFill(blockId);      const fillType = engine.block.getType(blockFill);
      if (fillType === '//ly.img.ubq/fill/image') {        const uri = engine.block.getString(          blockFill,          'fill/image/imageFileURI'        );        console.log('Image block found with URI:', uri);
        // Example: migrate from old CDN to new CDN        if (uri.includes('old-cdn.example.com')) {          const migratedUri = uri.replace(            'old-cdn.example.com',            'new-cdn.example.com'          );          engine.block.setString(            blockFill,            'fill/image/imageFileURI',            migratedUri          );        }      }    }
    // Demonstrate versioned URL patterns
    // Path-based versioning: include version in the URL path    const pathVersionedUrl = 'https://cdn.example.com/assets/v2/logo.png';    console.log('Path-versioned URL:', pathVersionedUrl);
    // Hash-based versioning: include content hash in filename    const hashVersionedUrl = 'https://cdn.example.com/assets/logo-a1b2c3d4.png';    console.log('Hash-versioned URL:', hashVersionedUrl);
    // Query parameter versioning: append version as query string    const queryVersionedUrl = 'https://cdn.example.com/assets/logo.png?v=2';    console.log('Query-versioned URL:', queryVersionedUrl);
    // Add a second image to make the scene more visually interesting    const secondImageUri = 'https://img.ly/static/ubq_samples/sample_3.jpg';    await engine.block.addImage(secondImageUri, {      x: 400,      y: 50,      size: { width: 300, height: 200 }    });
    // Select the first image block to show it in the canvas inspector    engine.block.select(imageBlock);
    console.log(      'Asset versioning guide initialized. Check console for URL inspection results.'    );  }}
export default Example;
```

This guide covers how to inspect asset URLs stored in designs, the difference between scene serialization and archive export, how to programmatically update asset URLs, and strategies for versioned URL schemes.

## How Asset URLs Are Stored[#](#how-asset-urls-are-stored)

Assets in a scene are blocks with fill properties containing URI strings. When you add an image or video to a design, CE.SDK creates a fill block that stores the source URL. We can use `engine.block.getFill()` to get the fill block and `engine.block.getString()` to inspect the stored URI.

```
// Create an image block with a remote URLconst imageUri = 'https://img.ly/static/ubq_samples/sample_1.jpg';
const imageBlock = await engine.block.addImage(imageUri, {  x: 50,  y: 50,  size: { width: 300, height: 200 }});
// Get the fill block that contains the image URIconst fill = engine.block.getFill(imageBlock);
// Inspect the stored URI - this is exactly what gets saved in the sceneconst storedUri = engine.block.getString(fill, 'fill/image/imageFileURI');console.log('Stored image URI:', storedUri);
```

The `fill/image/imageFileURI` property contains exactly what gets written to the saved scene. CE.SDK doesn’t transform or normalize these URLs—they’re stored and loaded as-is.

## Scene Serialization vs Archive Export[#](#scene-serialization-vs-archive-export)

CE.SDK provides two approaches for saving designs, each with different trade-offs for asset handling.

### Saving as a Scene String[#](#saving-as-a-scene-string)

The `saveToString()` method serializes the scene structure while keeping asset references as URLs. This produces small files that load quickly, but requires the original assets to remain available at their URLs.

```
// Save the scene to a string - URLs are preserved as referencesconst sceneString = await engine.scene.saveToString();console.log('Scene saved to string, length:', sceneString.length);
// The scene string contains the URL reference, not the image data itself// This keeps the saved scene small and loads quickly
```

Use scene strings when:

*   Assets are hosted on a stable CDN with reliable URLs
*   You want to keep storage costs low
*   Designs need to load quickly
*   You can guarantee asset availability

### Saving as an Archive[#](#saving-as-an-archive)

The `saveToArchive()` method bundles the scene with all referenced assets into a ZIP file. This creates a self-contained package that works without network access.

```
// Alternatively, save as an archive with embedded assetsconst archiveBlob = await engine.scene.saveToArchive();console.log('Archive created, size:', archiveBlob.size, 'bytes');
// Archives are self-contained - they include all asset data// Use archives when designs need to work offline or across environments
```

Use archives when:

*   Designs need to work offline
*   You’re migrating designs between environments
*   You can’t guarantee long-term URL availability
*   Portability is more important than file size

| Approach | Method | Assets | File Size | Portability |
| --- | --- | --- | --- | --- |
| Scene | `saveToString()` | Referenced by URL | Small | Requires URL availability |
| Archive | `saveToArchive()` | Embedded in ZIP | Larger | Self-contained |

## What Happens When URLs Change[#](#what-happens-when-urls-change)

When a design is loaded and an asset URL returns a 404 or is otherwise unavailable, the block appears empty or shows an error state. Browser caching may temporarily mask broken URLs—a user might see cached content while others see failures.

CE.SDK doesn’t provide automatic fallbacks or retries for failed asset loads. If some assets fail while others succeed, the design loads partially. To prevent broken designs, ensure assets remain available at their original URLs or migrate designs when URLs change.

## Updating Asset URLs Programmatically[#](#updating-asset-urls-programmatically)

When you need to migrate assets to a new location, you can load existing scenes, update the URLs, and save the modified scene. We use `engine.block.setString()` to update the fill property.

```
// Programmatically update an asset URL (e.g., for CDN migration)const newUri = 'https://img.ly/static/ubq_samples/sample_2.jpg';engine.block.setString(fill, 'fill/image/imageFileURI', newUri);
// Verify the changeconst updatedUri = engine.block.getString(fill, 'fill/image/imageFileURI');console.log('Updated image URI:', updatedUri);
```

For batch updates, iterate through all blocks of a given type and update their fills.

```
// Find all graphic blocks to batch update their asset URLsconst graphicBlocks = engine.block.findByType('graphic');console.log('Found graphic blocks:', graphicBlocks.length);
// Iterate through blocks to inspect or update their fillsfor (const blockId of graphicBlocks) {  const blockFill = engine.block.getFill(blockId);  const fillType = engine.block.getType(blockFill);
  if (fillType === '//ly.img.ubq/fill/image') {    const uri = engine.block.getString(      blockFill,      'fill/image/imageFileURI'    );    console.log('Image block found with URI:', uri);
    // Example: migrate from old CDN to new CDN    if (uri.includes('old-cdn.example.com')) {      const migratedUri = uri.replace(        'old-cdn.example.com',        'new-cdn.example.com'      );      engine.block.setString(        blockFill,        'fill/image/imageFileURI',        migratedUri      );    }  }}
```

This pattern is useful for CDN migrations or restructuring asset directories.

## Strategies for Versioned Asset URLs[#](#strategies-for-versioned-asset-urls)

Designing your URL scheme to support versioning prevents accidental overwrites and makes migrations easier. We recommend three approaches.

```
// Demonstrate versioned URL patterns
// Path-based versioning: include version in the URL pathconst pathVersionedUrl = 'https://cdn.example.com/assets/v2/logo.png';console.log('Path-versioned URL:', pathVersionedUrl);
// Hash-based versioning: include content hash in filenameconst hashVersionedUrl = 'https://cdn.example.com/assets/logo-a1b2c3d4.png';console.log('Hash-versioned URL:', hashVersionedUrl);
// Query parameter versioning: append version as query stringconst queryVersionedUrl = 'https://cdn.example.com/assets/logo.png?v=2';console.log('Query-versioned URL:', queryVersionedUrl);
```

### Path-Based Versioning[#](#path-based-versioning)

Include version in the URL path: `https://cdn.example.com/assets/v2/logo.png`. When you update assets, increment the version directory. Old designs reference old paths while new designs use new paths. Both versions can coexist on the same CDN.

### Hash-Based Filenames[#](#hash-based-filenames)

Use content hashes in filenames: `logo-a1b2c3d4.png`. The URL changes whenever content changes, ensuring automatic cache invalidation. Build tools like Webpack and Vite generate these automatically. This pattern works well for content-addressable storage.

### Query Parameter Versioning[#](#query-parameter-versioning)

Append version as query parameter: `logo.png?v=2`. The base URL stays the same but the version parameter forces cache invalidation. Note that some CDNs ignore query parameters for caching—verify your CDN configuration before relying on this approach.

## Best Practices[#](#best-practices)

When managing asset URLs in production:

*   **Use immutable URLs**: Content-addressed or versioned paths prevent accidental overwrites
*   **Keep old assets available**: Don’t delete assets that may be referenced by saved designs
*   **Use archives for portability**: Export as archive when designs need to work offline or across environments
*   **Plan CDN migrations carefully**: Update saved designs before decommissioning old URLs
*   **Set appropriate cache headers**: Balance performance with freshness requirements
*   **Document your URL scheme**: Make versioning strategy clear for your team

## Troubleshooting[#](#troubleshooting)

| Issue | Cause | Solution |
| --- | --- | --- |
| Asset shows old version | Browser cache | Clear cache or use cache-busting URL |
| Asset not loading | URL changed or deleted | Verify URL accessibility, update scene |
| Design partially loads | Some assets unavailable | Check all asset URLs, consider archive export |
| Archive too large | Many/large embedded assets | Optimize assets before archiving |

## Next Steps[#](#next-steps)

*   [Save Designs](sveltekit/export-save-publish/save-c8b124/) — Save and serialize designs
*   [Export Overview](sveltekit/export-save-publish/export/overview-9ed3a8/) — Export options including archives

---



[Source](https:/img.ly/docs/cesdk/sveltekit/import-media/from-local-source/user-upload-c6c7d9)