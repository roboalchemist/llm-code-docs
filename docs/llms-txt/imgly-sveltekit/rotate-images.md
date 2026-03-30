# Rotate Images

Rotate images to adjust orientation, correct crooked photos, or create creative effects using CE.SDK’s rotation APIs.

![Rotate images example showing images at different rotation angles](/docs/cesdk/_astro/browser.hero.BrdivI9-_Z1mglSz.webp)

8 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-edit-image-transform-rotate-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-edit-image-transform-rotate-browser)

Rotation uses radians where `Math.PI / 2` equals 90°, `Math.PI` equals 180°, and negative values rotate clockwise. Values are relative to the block’s center point.

```
import CreativeEditorSDK, {  type EditorPlugin,  type EditorPluginContext} from '@cesdk/cesdk-js';
class Example implements EditorPlugin {  name = 'guides-edit-image-transform-rotate-browser';
  version = CreativeEditorSDK.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    // Setup: Load assets and create scene    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Design',      withUploadAssetSources: true    });    await cesdk.createDesignScene();
    const engine = cesdk.engine;    const page = engine.block.findByType('page')[0];
    // Set page dimensions    engine.block.setWidth(page, 800);    engine.block.setHeight(page, 500);
    // Demo 1: Original image (no rotation)    const originalImage = await engine.block.addImage(      'https://img.ly/static/ubq_samples/sample_3.jpg',      {        size: { width: 150, height: 150 }      }    );    engine.block.appendChild(page, originalImage);    engine.block.setPositionX(originalImage, 50);    engine.block.setPositionY(originalImage, 50);
    const text1 = engine.block.create('text');    engine.block.setString(text1, 'text/text', 'Original');    engine.block.setFloat(text1, 'text/fontSize', 24);    engine.block.setEnum(text1, 'text/horizontalAlignment', 'Center');    engine.block.setWidth(text1, 150);    engine.block.setPositionX(text1, 50);    engine.block.setPositionY(text1, 210);    engine.block.appendChild(page, text1);
    // Demo 2: Rotate 45 degrees    const rotated45Image = await engine.block.addImage(      'https://img.ly/static/ubq_samples/sample_3.jpg',      {        size: { width: 150, height: 150 }      }    );    engine.block.appendChild(page, rotated45Image);    engine.block.setPositionX(rotated45Image, 225);    engine.block.setPositionY(rotated45Image, 50);
    // Rotate the block by 45 degrees (π/4 radians)    engine.block.setRotation(rotated45Image, Math.PI / 4);
    const text2 = engine.block.create('text');    engine.block.setString(text2, 'text/text', '45°');    engine.block.setFloat(text2, 'text/fontSize', 24);    engine.block.setEnum(text2, 'text/horizontalAlignment', 'Center');    engine.block.setWidth(text2, 150);    engine.block.setPositionX(text2, 225);    engine.block.setPositionY(text2, 210);    engine.block.appendChild(page, text2);
    // Demo 3: Rotate 90 degrees    const rotated90Image = await engine.block.addImage(      'https://img.ly/static/ubq_samples/sample_3.jpg',      {        size: { width: 150, height: 150 }      }    );    engine.block.appendChild(page, rotated90Image);    engine.block.setPositionX(rotated90Image, 400);    engine.block.setPositionY(rotated90Image, 50);
    // Rotate the block by 90 degrees (π/2 radians)    engine.block.setRotation(rotated90Image, Math.PI / 2);
    const text3 = engine.block.create('text');    engine.block.setString(text3, 'text/text', '90°');    engine.block.setFloat(text3, 'text/fontSize', 24);    engine.block.setEnum(text3, 'text/horizontalAlignment', 'Center');    engine.block.setWidth(text3, 150);    engine.block.setPositionX(text3, 400);    engine.block.setPositionY(text3, 210);    engine.block.appendChild(page, text3);
    // Demo 4: Rotate 180 degrees    const rotated180Image = await engine.block.addImage(      'https://img.ly/static/ubq_samples/sample_3.jpg',      {        size: { width: 150, height: 150 }      }    );    engine.block.appendChild(page, rotated180Image);    engine.block.setPositionX(rotated180Image, 575);    engine.block.setPositionY(rotated180Image, 50);
    // Rotate the block by 180 degrees (π radians)    engine.block.setRotation(rotated180Image, Math.PI);
    const text4 = engine.block.create('text');    engine.block.setString(text4, 'text/text', '180°');    engine.block.setFloat(text4, 'text/fontSize', 24);    engine.block.setEnum(text4, 'text/horizontalAlignment', 'Center');    engine.block.setWidth(text4, 150);    engine.block.setPositionX(text4, 575);    engine.block.setPositionY(text4, 210);    engine.block.appendChild(page, text4);
    // Demo 5: Grouped rotation    const groupedImage1 = await engine.block.addImage(      'https://img.ly/static/ubq_samples/sample_5.jpg',      {        size: { width: 100, height: 100 }      }    );    engine.block.appendChild(page, groupedImage1);    engine.block.setPositionX(groupedImage1, 150);    engine.block.setPositionY(groupedImage1, 300);
    const groupedImage2 = await engine.block.addImage(      'https://img.ly/static/ubq_samples/sample_6.jpg',      {        size: { width: 100, height: 100 }      }    );    engine.block.appendChild(page, groupedImage2);    engine.block.setPositionX(groupedImage2, 260);    engine.block.setPositionY(groupedImage2, 300);
    // Group blocks and rotate them together    const groupId = engine.block.group([groupedImage1, groupedImage2]);    engine.block.setRotation(groupId, Math.PI / 8);
    const text5 = engine.block.create('text');    engine.block.setString(text5, 'text/text', 'Grouped');    engine.block.setFloat(text5, 'text/fontSize', 24);    engine.block.setEnum(text5, 'text/horizontalAlignment', 'Center');    engine.block.setWidth(text5, 200);    engine.block.setPositionX(text5, 150);    engine.block.setPositionY(text5, 440);    engine.block.appendChild(page, text5);
    // Demo 6: Locked rotation    const lockedImage = await engine.block.addImage(      'https://img.ly/static/ubq_samples/sample_3.jpg',      {        size: { width: 150, height: 150 }      }    );    engine.block.appendChild(page, lockedImage);    engine.block.setPositionX(lockedImage, 500);    engine.block.setPositionY(lockedImage, 300);    engine.block.setRotation(lockedImage, Math.PI / 6);
    // Lock rotation for a single block    engine.block.setScopeEnabled(lockedImage, 'layer/rotate', false);
    const text6 = engine.block.create('text');    engine.block.setString(text6, 'text/text', 'Locked');    engine.block.setFloat(text6, 'text/fontSize', 24);    engine.block.setEnum(text6, 'text/horizontalAlignment', 'Center');    engine.block.setWidth(text6, 150);    engine.block.setPositionX(text6, 500);    engine.block.setPositionY(text6, 460);    engine.block.appendChild(page, text6);
    // Get current rotation value    const currentRotation = engine.block.getRotation(rotated45Image);    console.log('Current rotation (radians):', currentRotation);    console.log(      'Current rotation (degrees):',      (currentRotation * 180) / Math.PI    );
    // Helpers for degree/radian conversion    const toRadians = (degrees: number) => (degrees * Math.PI) / 180;    const toDegrees = (radians: number) => (radians * 180) / Math.PI;
    // Example: rotate by 30 degrees using helper    const targetRadians = toRadians(30);    console.log('30 degrees in radians:', targetRadians);    console.log('Converted back to degrees:', toDegrees(targetRadians));  }}
export default Example;
```

This guide covers rotating images by specific angles, reading rotation values, converting between degrees and radians, rotating grouped elements together, and locking rotation on blocks.

## Initialize the Editor[#](#initialize-the-editor)

Set up the editor with default assets and create a design scene:

```
// Setup: Load assets and create sceneawait cesdk.addDefaultAssetSources();await cesdk.addDemoAssetSources({  sceneMode: 'Design',  withUploadAssetSources: true});await cesdk.createDesignScene();
```

## Rotate an Image[#](#rotate-an-image)

Rotate blocks using `engine.block.setRotation()` with angle values in radians. Use `Math.PI` for 180° or divide for smaller increments:

```
// Rotate the block by 45 degrees (π/4 radians)engine.block.setRotation(rotated45Image, Math.PI / 4);
```

## Rotate by 90 Degrees[#](#rotate-by-90-degrees)

Rotate a block by 90 degrees using `Math.PI / 2`:

```
// Rotate the block by 90 degrees (π/2 radians)engine.block.setRotation(rotated90Image, Math.PI / 2);
```

## Rotate by 180 Degrees[#](#rotate-by-180-degrees)

Flip a block upside down by rotating 180 degrees using `Math.PI`:

```
// Rotate the block by 180 degrees (π radians)engine.block.setRotation(rotated180Image, Math.PI);
```

## Get Current Rotation[#](#get-current-rotation)

Read the current rotation value using `engine.block.getRotation()`. The returned value is in radians:

```
// Get current rotation valueconst currentRotation = engine.block.getRotation(rotated45Image);console.log('Current rotation (radians):', currentRotation);console.log(  'Current rotation (degrees):',  (currentRotation * 180) / Math.PI);
```

## Convert Between Degrees and Radians[#](#convert-between-degrees-and-radians)

Create helper functions to convert between degrees and radians for more intuitive angle values:

```
// Helpers for degree/radian conversionconst toRadians = (degrees: number) => (degrees * Math.PI) / 180;const toDegrees = (radians: number) => (radians * 180) / Math.PI;
// Example: rotate by 30 degrees using helperconst targetRadians = toRadians(30);console.log('30 degrees in radians:', targetRadians);console.log('Converted back to degrees:', toDegrees(targetRadians));
```

## Rotate Groups Together[#](#rotate-groups-together)

Group multiple blocks and rotate them as a unit to maintain their relative positions:

```
// Group blocks and rotate them togetherconst groupId = engine.block.group([groupedImage1, groupedImage2]);engine.block.setRotation(groupId, Math.PI / 8);
```

## Lock Rotation[#](#lock-rotation)

Disable rotation for a specific block using `engine.block.setScopeEnabled()` with the `layer/rotate` scope:

```
// Lock rotation for a single blockengine.block.setScopeEnabled(lockedImage, 'layer/rotate', false);
```

## Troubleshooting[#](#troubleshooting)

### Rotation Has No Effect[#](#rotation-has-no-effect)

Ensure the block exists and is appended to a page before calling `setRotation()`. Verify the block ID is valid using `engine.block.isValid()`.

### Unexpected Rotation Direction[#](#unexpected-rotation-direction)

Positive values rotate counterclockwise, negative values rotate clockwise. Double-check your angle calculation if the rotation appears inverted.

### Block Appears Skewed After Rotation[#](#block-appears-skewed-after-rotation)

Rotation uses the block’s center as the pivot point. If the block appears off-center, check that no unexpected scaling or positioning was applied.

### Locked Block Won’t Rotate[#](#locked-block-wont-rotate)

Check if the block’s `layer/rotate` scope is disabled using `engine.block.isScopeEnabled()`. Re-enable with `engine.block.setScopeEnabled(block, 'layer/rotate', true)`.

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `engine.block.setRotation()` | Set rotation angle in radians |
| `engine.block.getRotation()` | Get current rotation angle in radians |
| `engine.block.group()` | Group blocks for collective transforms |
| `engine.block.setScopeEnabled()` | Enable or disable specific block scopes |
| `engine.block.isScopeEnabled()` | Check if a scope is enabled for a block |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/edit-image/transform/move-818dd9)