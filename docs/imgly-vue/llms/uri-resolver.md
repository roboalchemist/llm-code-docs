# URI Resolver

Learn how to intercept and transform asset URIs in CE.SDK, enabling authentication and custom resolution logic.

![CE.SDK URI Resolver demonstration showing custom resolution behavior](/docs/cesdk/_astro/browser.hero.DcGG2Jzb_9e91B.webp)

5 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-open-the-editor-uri-resolver-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-open-the-editor-uri-resolver-browser)

When CE.SDK loads an asset, it resolves the URI to an absolute path before fetching. You can intercept this process to add authentication tokens or transform URIs based on your application’s needs.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
/** * CE.SDK Plugin: URI Resolver Guide * * This example demonstrates: * - Understanding default URI resolution behavior * - Setting custom URI resolvers * - Adding authentication tokens * - Removing custom resolvers */class Example implements EditorPlugin {  name = packageJson.name;
  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    // Create a design scene    await cesdk.createDesignScene();
    const engine = cesdk.engine;
    // Get the page    const pages = engine.block.findByType('page');    const page = pages[0];    if (!page) {      throw new Error('No page found');    }
    // Set page dimensions    engine.block.setWidth(page, 800);    engine.block.setHeight(page, 600);
    // Set page background to light gray    const pageFill = engine.block.getFill(page);    engine.block.setColor(pageFill, 'fill/color/value', {      r: 0.96,      g: 0.96,      b: 0.96,      a: 1.0    });
    // ========================================    // Section 1: Understanding Default URI Resolution    // ========================================
    // Test resolution without loading assets    const relativeURI = '/images/photo.jpg';    const resolvedURI = engine.editor.getAbsoluteURI(relativeURI);    console.log('Default resolution:');    console.log(`  Input:  ${relativeURI}`);    console.log(`  Output: ${resolvedURI}`);
    // ========================================    // Section 2: Setting a Custom URI Resolver    // ========================================
    // Set a custom resolver that transforms specific file types    engine.editor.setURIResolver((uri, defaultURIResolver) => {      // Transform JPG files to a watermarked version      if (uri.endsWith('.jpg')) {        console.log(`Custom resolver: Transforming ${uri}`);        return 'https://img.ly/static/ubq_samples/sample_1.jpg';      }      // Use default resolver for all other URIs      return defaultURIResolver(uri);    });
    // Test the custom resolver    // ========================================    // Section 2: Adding Authentication with JWT Tokens    // ========================================
    // Pre-generate token BEFORE setting the resolver (must be synchronous)    const authToken = 'demo-jwt-token-123';
    // Set resolver that adds authentication to specific endpoints    engine.editor.setURIResolver((uri, defaultURIResolver) => {      // Only add auth token to URIs pointing to your stable link endpoint      if (uri.includes('your-server/image-stable-links/')) {        const authenticatedURI = `${uri}?auth=${authToken}`;        console.log(`\nAuth resolver: Adding token to ${uri}`);        console.log(`  Result: ${authenticatedURI}`);        return authenticatedURI;      }      // Use default resolver for all other URIs      return defaultURIResolver(uri);    });
    // Test authentication with a protected URI    const protectedURI = 'https://your-server/image-stable-links/abc123';    engine.editor.getAbsoluteURI(protectedURI);
    // ========================================    // Section 3: Removing a Custom Resolver    // ========================================
    // Remove the custom resolver to restore default behavior    engine.editor.setURIResolver((uri, defaultURIResolver) =>      defaultURIResolver(uri)    );    console.log('\n✓ Removed custom resolver - back to default behavior');
    // ========================================    // Visual Demonstration: Load Images    // ========================================
    // Create a visual demonstration with actual image loading    // This shows that the resolver affects actual asset loading, not just getAbsoluteURI()
    // Set a simple resolver for the demo    engine.editor.setURIResolver((uri, defaultURIResolver) => {      // For this demo, ensure all images resolve to valid URLs      if (uri.includes('sample')) {        return uri;      }      return defaultURIResolver(uri);    });
    // Create three image blocks to demonstrate URI resolution in action    const imageSize = { width: 200, height: 150 };    const spacing = 40;    const startX = (800 - (imageSize.width * 3 + spacing * 2)) / 2;    const startY = (600 - imageSize.height) / 2;
    // Image 1: Standard resolution    const image1 = await engine.block.addImage(      'https://img.ly/static/ubq_samples/sample_1.jpg',      { size: imageSize }    );    engine.block.setPositionX(image1, startX);    engine.block.setPositionY(image1, startY);    engine.block.appendChild(page, image1);
    // Image 2: Another sample    const image2 = await engine.block.addImage(      'https://img.ly/static/ubq_samples/sample_2.jpg',      { size: imageSize }    );    engine.block.setPositionX(image2, startX + imageSize.width + spacing);    engine.block.setPositionY(image2, startY);    engine.block.appendChild(page, image2);
    // Image 3: Third sample    const image3 = await engine.block.addImage(      'https://img.ly/static/ubq_samples/sample_3.jpg',      { size: imageSize }    );    engine.block.setPositionX(image3, startX + (imageSize.width + spacing) * 2);    engine.block.setPositionY(image3, startY);    engine.block.appendChild(page, image3);
    // Zoom to fit all content    await engine.scene.zoomToBlock(page, {      padding: {        left: 40,        top: 40,        right: 40,        bottom: 40      }    });
    console.log('\n✓ URI Resolver guide loaded successfully!');  }}
export default Example;
```

## Default URI Resolution[#](#default-uri-resolution)

By default, CE.SDK resolves URIs relative to the `basePath` setting. Absolute URIs (with http://, https://, data:) pass through unchanged, while relative paths get prepended with `basePath`.

Use `getAbsoluteURI()` to test how URIs resolve without loading assets:

```
// Test resolution without loading assetsconst relativeURI = '/images/photo.jpg';const resolvedURI = engine.editor.getAbsoluteURI(relativeURI);console.log('Default resolution:');console.log(`  Input:  ${relativeURI}`);console.log(`  Output: ${resolvedURI}`);
```

## Custom URI Resolver[#](#custom-uri-resolver)

Set a custom resolver to intercept and transform URIs. The resolver receives the URI and a `defaultURIResolver` function for fallback behavior:

```
// Set a custom resolver that transforms specific file typesengine.editor.setURIResolver((uri, defaultURIResolver) => {  // Transform JPG files to a watermarked version  if (uri.endsWith('.jpg')) {    console.log(`Custom resolver: Transforming ${uri}`);    return 'https://img.ly/static/ubq_samples/sample_1.jpg';  }  // Use default resolver for all other URIs  return defaultURIResolver(uri);});
```

**Important:** The resolver must be synchronous—no `async`/`await` or Promises. Pre-compute any tokens or transformations before setting the resolver.

## Adding Authentication[#](#adding-authentication)

A common use case is adding authentication tokens to asset URIs. Generate the token before setting the resolver, then append it as a query parameter:

```
// Pre-generate token BEFORE setting the resolver (must be synchronous)const authToken = 'demo-jwt-token-123';
// Set resolver that adds authentication to specific endpointsengine.editor.setURIResolver((uri, defaultURIResolver) => {  // Only add auth token to URIs pointing to your stable link endpoint  if (uri.includes('your-server/image-stable-links/')) {    const authenticatedURI = `${uri}?auth=${authToken}`;    console.log(`\nAuth resolver: Adding token to ${uri}`);    console.log(`  Result: ${authenticatedURI}`);    return authenticatedURI;  }  // Use default resolver for all other URIs  return defaultURIResolver(uri);});
// Test authentication with a protected URIconst protectedURI = 'https://your-server/image-stable-links/abc123';engine.editor.getAbsoluteURI(protectedURI);
```

Your server validates the token and redirects to the actual asset (e.g., pre-signed S3 URL). CE.SDK follows redirects automatically.

## Removing a Resolver[#](#removing-a-resolver)

Restore default behavior by setting a resolver that delegates to `defaultURIResolver`:

```
// Remove the custom resolver to restore default behaviorengine.editor.setURIResolver((uri, defaultURIResolver) =>  defaultURIResolver(uri));console.log('\n✓ Removed custom resolver - back to default behavior');
```

## Key Constraints[#](#key-constraints)

*   **Synchronous only**: No `async`/`await` or Promises
*   **Must return absolute URIs**: Include scheme (http://, https://, data:)
*   **One resolver at a time**: New calls overwrite previous resolvers
*   **Delegate unmatched URIs**: Pass to `defaultURIResolver()` for unchanged paths

## Next Steps[#](#next-steps)

*   [Configuration](vue/configuration-2c1c3d/) — CE.SDK initialization and baseURL settings
*   [Load Assets from Remote](vue/import-media/from-remote-source-b65faf/) — Load assets from remote URLs and servers

---



[Source](https:/img.ly/docs/cesdk/vue/open-the-editor/set-zoom-level-d31896)