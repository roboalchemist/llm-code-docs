# Using Strokes

Add outlines around shapes, text, and graphics to enhance visual definition and create decorative effects.

![Using Strokes example showing a rectangle with a styled blue dashed stroke](/docs/cesdk/_astro/browser.hero.Dodeilsm_xLEU0.webp)

5 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-outlines-stroke-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-outlines-stroke-browser)

Strokes add visual outlines that define block boundaries. You can customize their color, width, line style (solid, dashed, dotted), position relative to the block edge, and corner treatment. CE.SDK provides both built-in UI controls and programmatic APIs for stroke management.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';
class Example implements EditorPlugin {  name = 'guides-outlines-stroke-browser';  version = '1.0.0';
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    // Load assets and create scene    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Design',      withUploadAssetSources: true    });
    await cesdk.createDesignScene();
    const engine = cesdk.engine;    const page = engine.block.findByType('page')[0]!;
    // Set page dimensions    engine.block.setWidth(page, 800);    engine.block.setHeight(page, 600);
    // Create a graphic block with a rectangle shape    const block = engine.block.create('graphic');    engine.block.setShape(block, engine.block.createShape('rect'));    engine.block.appendChild(page, block);
    // Position and size the block    engine.block.setPositionX(block, 200);    engine.block.setPositionY(block, 150);    engine.block.setWidth(block, 400);    engine.block.setHeight(block, 300);
    // Add a fill so the shape is visible    const solidFill = engine.block.createFill('color');    engine.block.setFill(block, solidFill);    engine.block.setColor(solidFill, 'fill/color/value', {      r: 0.95,      g: 0.95,      b: 0.95,      a: 1.0    });
    // Check if block supports strokes    const canHaveStroke = engine.block.supportsStroke(block);    console.log('Block supports stroke:', canHaveStroke);
    if (canHaveStroke) {      // Enable stroke on the block      engine.block.setStrokeEnabled(block, true);      const strokeIsEnabled = engine.block.isStrokeEnabled(block);      console.log('Stroke enabled:', strokeIsEnabled);
      // Set stroke color to blue      engine.block.setStrokeColor(block, { r: 0.0, g: 0.4, b: 0.9, a: 1.0 });      const strokeColor = engine.block.getStrokeColor(block);      console.log('Stroke color:', strokeColor);
      // Set stroke width      engine.block.setStrokeWidth(block, 8);      const strokeWidth = engine.block.getStrokeWidth(block);      console.log('Stroke width:', strokeWidth);
      // Apply a dashed stroke style      engine.block.setStrokeStyle(block, 'Dashed');      const strokeStyle = engine.block.getStrokeStyle(block);      console.log('Stroke style:', strokeStyle);
      // Set stroke position to outer      engine.block.setStrokePosition(block, 'Outer');      const strokePosition = engine.block.getStrokePosition(block);      console.log('Stroke position:', strokePosition);
      // Set corner geometry to round      engine.block.setStrokeCornerGeometry(block, 'Round');      const strokeCornerGeometry = engine.block.getStrokeCornerGeometry(block);      console.log('Stroke corner geometry:', strokeCornerGeometry);    }
    // Select the block to show it in the inspector    engine.block.select(block);  }}
export default Example;
```

This guide covers how to use the stroke inspector panel for interactive editing and how to apply and manage strokes programmatically using the block API.

## Using the Built-in Stroke UI[#](#using-the-built-in-stroke-ui)

The CE.SDK editor includes a stroke inspector panel for interactive stroke editing. When you select a block that supports strokes, the inspector displays stroke controls:

*   **Enable toggle** - Turn strokes on or off for the selected block
*   **Color picker** - Choose the stroke color with full RGBA support
*   **Width control** - Adjust stroke thickness using a slider or input field
*   **Style dropdown** - Select from solid, dashed, or dotted line patterns
*   **Position options** - Choose where the stroke renders relative to the block edge (inner, center, or outer)

These controls provide a visual interface for users to customize strokes without writing code.

## Checking Stroke Support[#](#checking-stroke-support)

Before applying strokes programmatically, verify the block supports them using `supportsStroke()`. Not all block types have stroke capabilities.

```
// Check if block supports strokesconst canHaveStroke = engine.block.supportsStroke(block);console.log('Block supports stroke:', canHaveStroke);
```

## Enabling Strokes[#](#enabling-strokes)

Enable strokes on a block using `setStrokeEnabled()`. You can check the current state with `isStrokeEnabled()`.

```
// Enable stroke on the blockengine.block.setStrokeEnabled(block, true);const strokeIsEnabled = engine.block.isStrokeEnabled(block);console.log('Stroke enabled:', strokeIsEnabled);
```

## Setting Stroke Color[#](#setting-stroke-color)

Control stroke color using `setStrokeColor()` with an RGBA color object. Color values range from 0.0 to 1.0. Retrieve the current color with `getStrokeColor()`.

```
// Set stroke color to blueengine.block.setStrokeColor(block, { r: 0.0, g: 0.4, b: 0.9, a: 1.0 });const strokeColor = engine.block.getStrokeColor(block);console.log('Stroke color:', strokeColor);
```

## Setting Stroke Width[#](#setting-stroke-width)

Set stroke thickness in design units using `setStrokeWidth()`. Larger values create more prominent outlines. Get the current width with `getStrokeWidth()`.

```
// Set stroke widthengine.block.setStrokeWidth(block, 8);const strokeWidth = engine.block.getStrokeWidth(block);console.log('Stroke width:', strokeWidth);
```

## Stroke Styles[#](#stroke-styles)

Control the line pattern using `setStrokeStyle()`. Available styles include:

*   **Solid** - Continuous line
*   **Dashed** - Square-ended dashes with gaps
*   **DashedRound** - Round-ended dashes with gaps
*   **Dotted** - Circular dots
*   **LongDashed** - Longer square-ended dashes
*   **LongDashedRound** - Longer round-ended dashes

```
// Apply a dashed stroke styleengine.block.setStrokeStyle(block, 'Dashed');const strokeStyle = engine.block.getStrokeStyle(block);console.log('Stroke style:', strokeStyle);
```

## Stroke Position[#](#stroke-position)

Control where the stroke renders relative to the block edge using `setStrokePosition()`:

*   **Center** - Stroke centered on the edge (default)
*   **Inner** - Stroke rendered inside the block boundary
*   **Outer** - Stroke rendered outside the block boundary

Position affects how strokes interact with adjacent elements and overall layout dimensions. Inner strokes stay within the block bounds, while outer strokes extend beyond them.

```
// Set stroke position to outerengine.block.setStrokePosition(block, 'Outer');const strokePosition = engine.block.getStrokePosition(block);console.log('Stroke position:', strokePosition);
```

## Stroke Corner Geometry[#](#stroke-corner-geometry)

Control how stroke corners are rendered using `setStrokeCornerGeometry()`. This is particularly visible on rectangular shapes:

*   **Miter** - Sharp pointed corners (default)
*   **Round** - Smoothly curved corners
*   **Bevel** - Flat cut corners

```
// Set corner geometry to roundengine.block.setStrokeCornerGeometry(block, 'Round');const strokeCornerGeometry = engine.block.getStrokeCornerGeometry(block);console.log('Stroke corner geometry:', strokeCornerGeometry);
```

## Troubleshooting[#](#troubleshooting)

If strokes don’t appear as expected, check these common issues:

*   **Stroke not visible** - Verify stroke is enabled with `isStrokeEnabled()` and width is greater than 0
*   **Stroke color appears wrong** - Ensure color values are in the 0.0-1.0 range, not 0-255
*   **Stroke affects layout unexpectedly** - Use Inner position to keep strokes within bounds, or Outer if you want strokes to extend beyond the block
*   **Block doesn’t support strokes** - Use `supportsStroke()` to verify capability before applying stroke properties

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `block.supportsStroke(block)` | Check if a block supports strokes |
| `block.setStrokeEnabled(block, enabled)` | Enable or disable stroke on a block |
| `block.isStrokeEnabled(block)` | Check if stroke is enabled |
| `block.setStrokeColor(block, color)` | Set stroke color (RGBA, values 0.0-1.0) |
| `block.getStrokeColor(block)` | Get current stroke color |
| `block.setStrokeWidth(block, width)` | Set stroke thickness in design units |
| `block.getStrokeWidth(block)` | Get current stroke width |
| `block.setStrokeStyle(block, style)` | Set line pattern (Solid, Dashed, Dotted, etc.) |
| `block.getStrokeStyle(block)` | Get current stroke style |
| `block.setStrokePosition(block, position)` | Set stroke position (Center, Inner, Outer) |
| `block.getStrokePosition(block)` | Get current stroke position |
| `block.setStrokeCornerGeometry(block, type)` | Set corner rendering (Miter, Round, Bevel) |
| `block.getStrokeCornerGeometry(block)` | Get current corner geometry |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/outlines/shadows-and-glows-6610fa)