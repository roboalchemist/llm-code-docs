# Replace Colors

Transform images by swapping specific colors using the Recolor effect or remove backgrounds with the Green Screen effect in CE.SDK.

![Replace Colors example showing color replacement and background removal](/docs/cesdk/_astro/browser.hero.CiWZDZK-_ZLQEXi.webp)

8 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-edit-image-replace-colors-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-edit-image-replace-colors-browser)

CE.SDK offers two color replacement effects. The **Recolor** effect swaps one color for another while preserving image details. The **Green Screen** effect removes background colors with transparency. Both effects provide precise control over color matching, edge smoothness, and intensity.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';import { calculateGridLayout } from './utils';
/** * CE.SDK Plugin: Replace Colors Guide * * Demonstrates color replacement using Recolor and Green Screen effects: * - Using the built-in effects UI * - Creating and applying Recolor effects * - Creating and applying Green Screen effects * - Configuring effect properties * - Managing multiple effects */class Example implements EditorPlugin {  name = packageJson.name;
  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    // Initialize CE.SDK with Design mode and load asset sources    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Design',      withUploadAssetSources: true    });    await cesdk.createDesignScene();
    const engine = cesdk.engine;    const page = engine.block.findByType('page')[0];
    // Set page dimensions    engine.block.setWidth(page, 800);    engine.block.setHeight(page, 600);
    const pageWidth = engine.block.getWidth(page);    const pageHeight = engine.block.getHeight(page);
    // Enable effects in the inspector panel using the Feature API    cesdk.feature.enable('ly.img.effect'); // Enable all effects including recolor and green screen
    // Calculate responsive grid layout for 6 examples    const layout = calculateGridLayout(pageWidth, pageHeight, 6);    const { blockWidth, blockHeight, getPosition } = layout;
    // Use sample images for demonstrations    const imageUri = 'https://img.ly/static/ubq_samples/sample_1.jpg';    const blockSize = { width: blockWidth, height: blockHeight };
    // Create a Recolor effect to swap red colors to blue    const block1 = await engine.block.addImage(imageUri, { size: blockSize });    engine.block.appendChild(page, block1);
    const recolorEffect = engine.block.createEffect('recolor');    engine.block.setColor(recolorEffect, 'effect/recolor/fromColor', {      r: 1.0,      g: 0.0,      b: 0.0,      a: 1.0    }); // Red source color    engine.block.setColor(recolorEffect, 'effect/recolor/toColor', {      r: 0.0,      g: 0.5,      b: 1.0,      a: 1.0    }); // Blue target color    engine.block.appendEffect(block1, recolorEffect);
    // Select this block to show the effects panel    engine.block.setSelected(block1, true);
    // Configure color matching precision for Recolor effect    const block2 = await engine.block.addImage(imageUri, { size: blockSize });    engine.block.appendChild(page, block2);
    const recolorEffect2 = engine.block.createEffect('recolor');    engine.block.setColor(recolorEffect2, 'effect/recolor/fromColor', {      r: 0.8,      g: 0.6,      b: 0.4,      a: 1.0    }); // Skin tone source    engine.block.setColor(recolorEffect2, 'effect/recolor/toColor', {      r: 0.3,      g: 0.7,      b: 0.3,      a: 1.0    }); // Green tint    // Adjust color match tolerance (0-1, higher = more inclusive)    engine.block.setFloat(recolorEffect2, 'effect/recolor/colorMatch', 0.3);    // Adjust brightness match tolerance    engine.block.setFloat(      recolorEffect2,      'effect/recolor/brightnessMatch',      0.2    );    // Adjust edge smoothness    engine.block.setFloat(recolorEffect2, 'effect/recolor/smoothness', 0.1);    engine.block.appendEffect(block2, recolorEffect2);
    // Create a Green Screen effect to remove green backgrounds    const block3 = await engine.block.addImage(imageUri, { size: blockSize });    engine.block.appendChild(page, block3);
    const greenScreenEffect = engine.block.createEffect('green_screen');    // Specify the color to remove (green)    engine.block.setColor(greenScreenEffect, 'effect/green_screen/fromColor', {      r: 0.0,      g: 1.0,      b: 0.0,      a: 1.0    });    engine.block.appendEffect(block3, greenScreenEffect);
    // Fine-tune Green Screen removal parameters    const block4 = await engine.block.addImage(imageUri, { size: blockSize });    engine.block.appendChild(page, block4);
    const greenScreenEffect2 = engine.block.createEffect('green_screen');    engine.block.setColor(greenScreenEffect2, 'effect/green_screen/fromColor', {      r: 0.2,      g: 0.8,      b: 0.3,      a: 1.0    }); // Specific green shade    // Adjust color match tolerance    engine.block.setFloat(      greenScreenEffect2,      'effect/green_screen/colorMatch',      0.4    );    // Adjust edge smoothness for cleaner removal    engine.block.setFloat(      greenScreenEffect2,      'effect/green_screen/smoothness',      0.2    );    // Reduce color spill from green background    engine.block.setFloat(greenScreenEffect2, 'effect/green_screen/spill', 0.5);    engine.block.appendEffect(block4, greenScreenEffect2);
    // Demonstrate managing multiple effects on a block    const block5 = await engine.block.addImage(imageUri, { size: blockSize });    engine.block.appendChild(page, block5);
    // Add multiple effects to the same block    const recolor1 = engine.block.createEffect('recolor');    engine.block.setColor(recolor1, 'effect/recolor/fromColor', {      r: 1.0,      g: 0.0,      b: 0.0,      a: 1.0    });    engine.block.setColor(recolor1, 'effect/recolor/toColor', {      r: 0.0,      g: 0.0,      b: 1.0,      a: 1.0    });    engine.block.appendEffect(block5, recolor1);
    const recolor2 = engine.block.createEffect('recolor');    engine.block.setColor(recolor2, 'effect/recolor/fromColor', {      r: 0.0,      g: 1.0,      b: 0.0,      a: 1.0    });    engine.block.setColor(recolor2, 'effect/recolor/toColor', {      r: 1.0,      g: 0.5,      b: 0.0,      a: 1.0    });    engine.block.appendEffect(block5, recolor2);
    // Get all effects on the block    const effects = engine.block.getEffects(block5);    console.log('Number of effects:', effects.length); // 2
    // Disable the first effect without removing it    engine.block.setEffectEnabled(effects[0], false);
    // Check if effect is enabled    const isEnabled = engine.block.isEffectEnabled(effects[0]);    console.log('First effect enabled:', isEnabled); // false
    // Apply consistent color replacement across multiple blocks    const block6 = await engine.block.addImage(imageUri, { size: blockSize });    engine.block.appendChild(page, block6);
    // Find all image blocks in the scene    const allBlocks = engine.block.findByType('//ly.img.ubq/graphic');
    // Apply a consistent recolor effect to each block    allBlocks.forEach((blockId) => {      // Skip if block already has effects      if (engine.block.getEffects(blockId).length > 0) {        return;      }
      const batchRecolor = engine.block.createEffect('recolor');      engine.block.setColor(batchRecolor, 'effect/recolor/fromColor', {        r: 0.8,        g: 0.7,        b: 0.6,        a: 1.0      });      engine.block.setColor(batchRecolor, 'effect/recolor/toColor', {        r: 0.6,        g: 0.7,        b: 0.9,        a: 1.0      });      engine.block.setFloat(batchRecolor, 'effect/recolor/colorMatch', 0.25);      engine.block.appendEffect(blockId, batchRecolor);    });
    // Position all blocks in a grid layout    const blocks = [block1, block2, block3, block4, block5, block6];    blocks.forEach((block, index) => {      const pos = getPosition(index);      engine.block.setPositionX(block, pos.x);      engine.block.setPositionY(block, pos.y);    });
    // Zoom to show all blocks    engine.block.setSelected(block1, true);    cesdk.engine.scene.zoomToBlock(page);  }}
export default Example;
```

This guide shows how to enable the built-in effects UI for interactive color replacement and apply effects programmatically using the block API.

## Using the Built-in Effects UI[#](#using-the-built-in-effects-ui)

### Enable Effects Panel[#](#enable-effects-panel)

We enable the effects feature using CE.SDK’s Feature API. The effects panel appears in the inspector when users select a compatible graphic block.

```
// Enable effects in the inspector panel using the Feature APIcesdk.feature.enable('ly.img.effect'); // Enable all effects including recolor and green screen
```

Enabling `ly.img.effect` makes all effect options available in the inspector panel, including Recolor and Green Screen.

### User Workflow[#](#user-workflow)

With effects enabled, users can replace colors through the inspector panel:

1.  **Select an image block** - Click an image or graphic block on the canvas
2.  **Open inspector** - The inspector shows available options for the selected element
3.  **Find effects section** - Scroll to the effects section
4.  **Choose Recolor or Green Screen** - Click the desired effect
5.  **Select colors** - Use the color picker to specify source and target colors
6.  **Adjust parameters** - Fine-tune color matching, smoothness, and intensity
7.  **Toggle effects** - Enable or disable effects to compare results

Users can experiment with color replacements and see results immediately.

## Programmatic Color Replacement[#](#programmatic-color-replacement)

### Initialize CE.SDK[#](#initialize-cesdk)

To apply color replacement programmatically, we set up CE.SDK with the proper configuration.

```
// Initialize CE.SDK with Design mode and load asset sourcesawait cesdk.addDefaultAssetSources();await cesdk.addDemoAssetSources({  sceneMode: 'Design',  withUploadAssetSources: true});await cesdk.createDesignScene();
const engine = cesdk.engine;const page = engine.block.findByType('page')[0];
// Set page dimensionsengine.block.setWidth(page, 800);engine.block.setHeight(page, 600);
const pageWidth = engine.block.getWidth(page);const pageHeight = engine.block.getHeight(page);
```

This initializes CE.SDK with the effects panel enabled, providing both UI and API access.

### Creating and Applying Recolor Effects[#](#creating-and-applying-recolor-effects)

The Recolor effect swaps one color for another throughout an image. We create a Recolor effect using `engine.block.createEffect('recolor')` and specify the source and target colors.

```
// Create a Recolor effect to swap red colors to blueconst block1 = await engine.block.addImage(imageUri, { size: blockSize });engine.block.appendChild(page, block1);
const recolorEffect = engine.block.createEffect('recolor');engine.block.setColor(recolorEffect, 'effect/recolor/fromColor', {  r: 1.0,  g: 0.0,  b: 0.0,  a: 1.0}); // Red source colorengine.block.setColor(recolorEffect, 'effect/recolor/toColor', {  r: 0.0,  g: 0.5,  b: 1.0,  a: 1.0}); // Blue target colorengine.block.appendEffect(block1, recolorEffect);
// Select this block to show the effects panelengine.block.setSelected(block1, true);
```

The Recolor effect identifies pixels matching the source color (fromColor) and replaces them with the target color (toColor). Color values use RGBA format with values from 0.0 to 1.0.

The example code uses the `engine.block.addImage()` convenience API. This simplifies image block creation compared to manually constructing graphic blocks with image fills.

### Configuring Color Matching[#](#configuring-color-matching)

We adjust the matching tolerance and smoothness parameters to control how precisely colors must match before replacement.

```
// Configure color matching precision for Recolor effectconst block2 = await engine.block.addImage(imageUri, { size: blockSize });engine.block.appendChild(page, block2);
const recolorEffect2 = engine.block.createEffect('recolor');engine.block.setColor(recolorEffect2, 'effect/recolor/fromColor', {  r: 0.8,  g: 0.6,  b: 0.4,  a: 1.0}); // Skin tone sourceengine.block.setColor(recolorEffect2, 'effect/recolor/toColor', {  r: 0.3,  g: 0.7,  b: 0.3,  a: 1.0}); // Green tint// Adjust color match tolerance (0-1, higher = more inclusive)engine.block.setFloat(recolorEffect2, 'effect/recolor/colorMatch', 0.3);// Adjust brightness match toleranceengine.block.setFloat(  recolorEffect2,  'effect/recolor/brightnessMatch',  0.2);// Adjust edge smoothnessengine.block.setFloat(recolorEffect2, 'effect/recolor/smoothness', 0.1);engine.block.appendEffect(block2, recolorEffect2);
```

The Recolor effect provides these parameters:

*   **colorMatch** (0-1) - How closely colors must match the source. Lower values match exact colors, higher values match broader ranges
*   **brightnessMatch** (0-1) - Tolerance for brightness variations
*   **smoothness** (0-1) - Edge blending to reduce artifacts

These parameters help handle images where colors vary due to lighting, shadows, or compression.

### Creating and Applying Green Screen Effects[#](#creating-and-applying-green-screen-effects)

The Green Screen effect removes backgrounds by making specific colors transparent.

```
// Create a Green Screen effect to remove green backgroundsconst block3 = await engine.block.addImage(imageUri, { size: blockSize });engine.block.appendChild(page, block3);
const greenScreenEffect = engine.block.createEffect('green_screen');// Specify the color to remove (green)engine.block.setColor(greenScreenEffect, 'effect/green_screen/fromColor', {  r: 0.0,  g: 1.0,  b: 0.0,  a: 1.0});engine.block.appendEffect(block3, greenScreenEffect);
```

The Green Screen effect identifies pixels matching the specified color (fromColor) and makes them transparent. This works best with solid-color backgrounds like green screens or blue screens.

### Fine-Tuning Green Screen Removal[#](#fine-tuning-green-screen-removal)

We adjust the color matching tolerance, edge smoothness, and spill suppression parameters.

```
// Fine-tune Green Screen removal parametersconst block4 = await engine.block.addImage(imageUri, { size: blockSize });engine.block.appendChild(page, block4);
const greenScreenEffect2 = engine.block.createEffect('green_screen');engine.block.setColor(greenScreenEffect2, 'effect/green_screen/fromColor', {  r: 0.2,  g: 0.8,  b: 0.3,  a: 1.0}); // Specific green shade// Adjust color match toleranceengine.block.setFloat(  greenScreenEffect2,  'effect/green_screen/colorMatch',  0.4);// Adjust edge smoothness for cleaner removalengine.block.setFloat(  greenScreenEffect2,  'effect/green_screen/smoothness',  0.2);// Reduce color spill from green backgroundengine.block.setFloat(greenScreenEffect2, 'effect/green_screen/spill', 0.5);engine.block.appendEffect(block4, greenScreenEffect2);
```

The Green Screen effect provides these parameters:

*   **colorMatch** (0-1) - Tolerance for color variations in the background
*   **smoothness** (0-1) - Edge feathering for natural transitions
*   **spill** (0-1) - Reduces color spill from the background onto foreground objects

These parameters help create clean composites without harsh edges or color artifacts.

## Managing Multiple Effects[#](#managing-multiple-effects)

We can apply multiple color replacement effects to the same block. CE.SDK maintains an effect stack for each block, applying effects in the order they were added.

```
// Demonstrate managing multiple effects on a blockconst block5 = await engine.block.addImage(imageUri, { size: blockSize });engine.block.appendChild(page, block5);
// Add multiple effects to the same blockconst recolor1 = engine.block.createEffect('recolor');engine.block.setColor(recolor1, 'effect/recolor/fromColor', {  r: 1.0,  g: 0.0,  b: 0.0,  a: 1.0});engine.block.setColor(recolor1, 'effect/recolor/toColor', {  r: 0.0,  g: 0.0,  b: 1.0,  a: 1.0});engine.block.appendEffect(block5, recolor1);
const recolor2 = engine.block.createEffect('recolor');engine.block.setColor(recolor2, 'effect/recolor/fromColor', {  r: 0.0,  g: 1.0,  b: 0.0,  a: 1.0});engine.block.setColor(recolor2, 'effect/recolor/toColor', {  r: 1.0,  g: 0.5,  b: 0.0,  a: 1.0});engine.block.appendEffect(block5, recolor2);
// Get all effects on the blockconst effects = engine.block.getEffects(block5);console.log('Number of effects:', effects.length); // 2
// Disable the first effect without removing itengine.block.setEffectEnabled(effects[0], false);
// Check if effect is enabledconst isEnabled = engine.block.isEffectEnabled(effects[0]);console.log('First effect enabled:', isEnabled); // false
```

Effect management capabilities:

*   **Get effects** - Retrieve all effects with `engine.block.getEffects()`
*   **Enable/disable** - Toggle effects with `engine.block.setEffectEnabled()` without removing them
*   **Check status** - Query effect state with `engine.block.isEffectEnabled()`
*   **Remove effects** - Delete effects by index with `engine.block.removeEffect()`

Disabling effects is useful for before/after comparisons or performance optimization.

## Batch Processing Multiple Images[#](#batch-processing-multiple-images)

We can loop through all image blocks in a scene and apply the same effect configuration to each.

```
// Apply consistent color replacement across multiple blocksconst block6 = await engine.block.addImage(imageUri, { size: blockSize });engine.block.appendChild(page, block6);
// Find all image blocks in the sceneconst allBlocks = engine.block.findByType('//ly.img.ubq/graphic');
// Apply a consistent recolor effect to each blockallBlocks.forEach((blockId) => {  // Skip if block already has effects  if (engine.block.getEffects(blockId).length > 0) {    return;  }
  const batchRecolor = engine.block.createEffect('recolor');  engine.block.setColor(batchRecolor, 'effect/recolor/fromColor', {    r: 0.8,    g: 0.7,    b: 0.6,    a: 1.0  });  engine.block.setColor(batchRecolor, 'effect/recolor/toColor', {    r: 0.6,    g: 0.7,    b: 0.9,    a: 1.0  });  engine.block.setFloat(batchRecolor, 'effect/recolor/colorMatch', 0.25);  engine.block.appendEffect(blockId, batchRecolor);});
```

Batch processing use cases:

*   **Product variations** - Generate multiple color variants
*   **Brand consistency** - Apply consistent color corrections
*   **Automated workflows** - Process multiple images with the same adjustments

The `engine.block.findByType()` method locates all graphic blocks in the scene.

## Troubleshooting[#](#troubleshooting)

Common issues and solutions when working with color replacement effects:

**Effect not visible**

*   Verify the effect is enabled with `engine.block.isEffectEnabled()`
*   Check that the effect is attached to the correct block using `engine.block.getEffects()`
*   Ensure the block type supports effects with `engine.block.supportsEffects()`

**Wrong colors being replaced**

*   Decrease `colorMatch` for more precise matching
*   Increase `colorMatch` to capture broader color ranges
*   Adjust `brightnessMatch` for Recolor effects with lighting variations

**Harsh edges or artifacts**

*   Increase `smoothness` to blend edges more gradually
*   For Green Screen, adjust `spill` to reduce color contamination
*   Use higher resolution images for smoother results

**Performance issues**

*   Limit active effects on a single block
*   Use `engine.block.setEffectEnabled(false)` to disable effects during editing
*   Process effects sequentially rather than simultaneously

## API Reference[#](#api-reference)

| Method | Category | Purpose |
| --- | --- | --- |
| `engine.block.createEffect()` | Block | Create a new Recolor or Green Screen effect block |
| `engine.block.appendEffect()` | Block | Attach an effect to an image block |
| `engine.block.insertEffect()` | Block | Insert an effect at a specific position in the effect stack |
| `engine.block.removeEffect()` | Block | Remove an effect from a block by index |
| `engine.block.getEffects()` | Block | Get all effects attached to a block |
| `engine.block.supportsEffects()` | Block | Check if a block can render effects |
| `engine.block.setColor()` | Block | Set color properties on effect blocks |
| `engine.block.getColor()` | Block | Get color properties from effect blocks |
| `engine.block.setFloat()` | Block | Set numeric effect properties |
| `engine.block.getFloat()` | Block | Get numeric effect properties |
| `engine.block.setEffectEnabled()` | Block | Enable or disable an effect |
| `engine.block.isEffectEnabled()` | Block | Check if an effect is enabled |
| `engine.block.findByType()` | Block | Find all blocks of a specific type |

## Next Steps[#](#next-steps)

*   [Apply Filters and Effects](sveltekit/filters-and-effects/apply-2764e4/) — Explore other visual effects available in CE.SDK
*   [Export Designs](sveltekit/export-save-publish/export-82f968/) — Save your color-replaced images in various formats

---



[Source](https:/img.ly/docs/cesdk/sveltekit/edit-image/remove-bg-9dfcf7)