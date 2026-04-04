# Insert Images

Insert images into your designs programmatically using CE.SDK’s engine API.

![Insert Images example showing multiple images placed on a canvas](/docs/cesdk/_astro/browser.hero.Xbwy26ol_2ljJTO.webp)

10 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-insert-media-images-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-insert-media-images-browser)

Images in CE.SDK are graphic blocks with image fills attached. The engine supports multiple image formats including PNG, JPEG, WebP, GIF, and SVG. You can insert images using either the convenience API for quick setup or manual construction for fine-grained control over the image block components.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
/** * CE.SDK Plugin: Insert Images Guide * * Demonstrates inserting images into a scene programmatically: * - Using the convenience API (addImage) * - Manual construction with graphic blocks and image fills * - Configuring image sizing, positioning, and content fill mode * - Applying corner radius for rounded images * - Working with multiple images */class Example implements EditorPlugin {  name = packageJson.name;
  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    // Initialize CE.SDK with Design mode and load asset sources    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Design',      withUploadAssetSources: true    });    await cesdk.createDesignScene();
    const engine = cesdk.engine;    const page = engine.block.findByType('page')[0];
    // Set page dimensions    engine.block.setWidth(page, 800);    engine.block.setHeight(page, 600);
    // Sample image URL for demonstrations    const imageUrl = 'https://img.ly/static/ubq_samples/sample_1.jpg';
    // Add an image using the convenience API    // This automatically creates a graphic block with rect shape and image fill    const imageBlock = await engine.block.addImage(imageUrl, {      size: { width: 200, height: 150 },      x: 50,      y: 50    });    engine.block.appendChild(page, imageBlock);    console.log('✓ Added image using convenience API');
    // Manually construct an image block for more control    const manualBlock = engine.block.create('graphic');
    // Create and attach a rectangular shape    const shape = engine.block.createShape('rect');    engine.block.setShape(manualBlock, shape);
    // Create and configure the image fill    const fill = engine.block.createFill('image');    engine.block.setString(fill, 'fill/image/imageFileURI', imageUrl);    engine.block.setFill(manualBlock, fill);
    // Set dimensions and position    engine.block.setWidth(manualBlock, 200);    engine.block.setHeight(manualBlock, 150);    engine.block.setPositionX(manualBlock, 300);    engine.block.setPositionY(manualBlock, 50);    engine.block.appendChild(page, manualBlock);    console.log('✓ Added image using manual construction');
    // Set content fill mode to control how images scale within bounds    // 'Contain' preserves aspect ratio and fits within bounds    // 'Cover' preserves aspect ratio and fills bounds    const containBlock = await engine.block.addImage(imageUrl, {      size: { width: 200, height: 150 },      x: 550,      y: 50    });    engine.block.appendChild(page, containBlock);
    if (engine.block.supportsContentFillMode(containBlock)) {      engine.block.setContentFillMode(containBlock, 'Contain');      console.log('✓ Applied Contain fill mode');    }
    // Apply corner radius to create rounded corners on an image    const roundedBlock = await engine.block.addImage(imageUrl, {      size: { width: 200, height: 150 },      x: 50,      y: 250,      cornerRadius: 20    });    engine.block.appendChild(page, roundedBlock);    console.log('✓ Added image with rounded corners');
    // Insert multiple images with calculated positioning    const imageUrls = [      'https://img.ly/static/ubq_samples/sample_1.jpg',      'https://img.ly/static/ubq_samples/sample_2.jpg',      'https://img.ly/static/ubq_samples/sample_3.jpg'    ];
    for (let i = 0; i < imageUrls.length; i++) {      const block = await engine.block.addImage(imageUrls[i], {        size: { width: 150, height: 100 },        x: 300 + i * 160,        y: 250      });      engine.block.appendChild(page, block);    }    console.log('✓ Added multiple images');
    // Select the first image block to show it in the inspector    engine.block.setSelected(imageBlock, true);
    // Zoom to show all content    cesdk.engine.scene.zoomToBlock(page, {      padding: {        top: 40,        bottom: 40,        left: 40,        right: 40      }    });  }}
export default Example;
```

This guide covers how to add images using the convenience API, manually construct image blocks, configure content fill modes, apply corner radius, and work with multiple images.

## Initialize CE.SDK[#](#initialize-cesdk)

We start by initializing CE.SDK and creating a scene with a page to hold our images.

```
// Initialize CE.SDK with Design mode and load asset sourcesawait cesdk.addDefaultAssetSources();await cesdk.addDemoAssetSources({  sceneMode: 'Design',  withUploadAssetSources: true});await cesdk.createDesignScene();
const engine = cesdk.engine;const page = engine.block.findByType('page')[0];
// Set page dimensionsengine.block.setWidth(page, 800);engine.block.setHeight(page, 600);
```

## Using the Convenience API[#](#using-the-convenience-api)

The `addImage()` method provides a quick way to insert images. It automatically creates a graphic block with a rect shape and image fill. You can configure size, position, corner radius, and other properties through the options parameter.

```
// Add an image using the convenience API// This automatically creates a graphic block with rect shape and image fillconst imageBlock = await engine.block.addImage(imageUrl, {  size: { width: 200, height: 150 },  x: 50,  y: 50});engine.block.appendChild(page, imageBlock);console.log('✓ Added image using convenience API');
```

## Manual Image Construction[#](#manual-image-construction)

For control over individual components, we can manually construct a graphic block with a rect shape and image fill. This approach lets you configure each component separately.

We create a graphic block with `create('graphic')`, attach a rectangular shape with `createShape('rect')`, and create an image fill with `createFill('image')`. The image source is set using `setString()` with the `fill/image/imageFileURI` property.

```
// Manually construct an image block for more controlconst manualBlock = engine.block.create('graphic');
// Create and attach a rectangular shapeconst shape = engine.block.createShape('rect');engine.block.setShape(manualBlock, shape);
// Create and configure the image fillconst fill = engine.block.createFill('image');engine.block.setString(fill, 'fill/image/imageFileURI', imageUrl);engine.block.setFill(manualBlock, fill);
// Set dimensions and positionengine.block.setWidth(manualBlock, 200);engine.block.setHeight(manualBlock, 150);engine.block.setPositionX(manualBlock, 300);engine.block.setPositionY(manualBlock, 50);engine.block.appendChild(page, manualBlock);console.log('✓ Added image using manual construction');
```

## Set Content Fill Mode[#](#set-content-fill-mode)

The content fill mode controls how images scale within their bounds. Use `setContentFillMode()` to choose between different scaling behaviors:

*   **Contain**: Preserves aspect ratio and fits the image within the bounds
*   **Cover**: Preserves aspect ratio and fills the bounds completely
*   **Crop**: Allows custom crop area

Check `supportsContentFillMode()` before setting to ensure the block supports this feature.

```
// Set content fill mode to control how images scale within bounds// 'Contain' preserves aspect ratio and fits within bounds// 'Cover' preserves aspect ratio and fills boundsconst containBlock = await engine.block.addImage(imageUrl, {  size: { width: 200, height: 150 },  x: 550,  y: 50});engine.block.appendChild(page, containBlock);
if (engine.block.supportsContentFillMode(containBlock)) {  engine.block.setContentFillMode(containBlock, 'Contain');  console.log('✓ Applied Contain fill mode');}
```

## Apply Corner Radius[#](#apply-corner-radius)

Add rounded corners to image blocks using the `cornerRadius` option in the convenience API. This creates a visually softer appearance for your images.

```
// Apply corner radius to create rounded corners on an imageconst roundedBlock = await engine.block.addImage(imageUrl, {  size: { width: 200, height: 150 },  x: 50,  y: 250,  cornerRadius: 20});engine.block.appendChild(page, roundedBlock);console.log('✓ Added image with rounded corners');
```

## Working with Multiple Images[#](#working-with-multiple-images)

Insert multiple images by iterating over an array of image URLs. Each image gets its own graphic block with calculated positioning to arrange them on the page.

```
// Insert multiple images with calculated positioningconst imageUrls = [  'https://img.ly/static/ubq_samples/sample_1.jpg',  'https://img.ly/static/ubq_samples/sample_2.jpg',  'https://img.ly/static/ubq_samples/sample_3.jpg'];
for (let i = 0; i < imageUrls.length; i++) {  const block = await engine.block.addImage(imageUrls[i], {    size: { width: 150, height: 100 },    x: 300 + i * 160,    y: 250  });  engine.block.appendChild(page, block);}console.log('✓ Added multiple images');
```

## Next Steps[#](#next-steps)

After inserting an image, you can:

*   [Edit and transform](sveltekit/edit-image-c64912/) the image
*   [Apply filters and effects](sveltekit/filters-and-effects-6f88ac/)
*   [Export your design](sveltekit/export-save-publish/export-82f968/)

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `engine.block.addImage(url, options?)` | Convenience API to create an image block with automatic setup |
| `engine.block.create('graphic')` | Create a graphic block container for images |
| `engine.block.createShape('rect')` | Create a rectangular shape for the image |
| `engine.block.setShape(block, shape)` | Attach shape to graphic block |
| `engine.block.createFill('image')` | Create an image fill |
| `engine.block.setFill(block, fill)` | Apply fill to block |
| `engine.block.setString(fill, property, value)` | Set image source URI via `fill/image/imageFileURI` |
| `engine.block.setWidth(block, width)` | Set block width |
| `engine.block.setHeight(block, height)` | Set block height |
| `engine.block.setPositionX(block, x)` | Set horizontal position |
| `engine.block.setPositionY(block, y)` | Set vertical position |
| `engine.block.supportsContentFillMode(block)` | Check if block supports content fill mode |
| `engine.block.setContentFillMode(block, mode)` | Set content fill mode (`Contain`, `Cover`, `Crop`) |
| `engine.block.appendChild(parent, child)` | Add block to parent |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/insert-media/audio-c10f10)