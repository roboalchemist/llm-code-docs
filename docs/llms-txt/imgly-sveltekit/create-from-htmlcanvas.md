# Create From HTMLCanvas

Create a CE.SDK scene from an HTMLCanvas element’s rendered content, enabling editing of canvas-based graphics.

![Create From HTMLCanvas example showing canvas content loaded in CE.SDK](/docs/cesdk/_astro/browser.hero.CuDoP4gv_Z1zV3a3.webp)

5 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-open-the-editor-from-htmlcanvas-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-open-the-editor-from-htmlcanvas-browser)

You can capture any graphics rendered to a canvas—2D drawings, WebGL content, or programmatically generated visuals—and use them as the starting point for editing in CE.SDK. The workflow extracts canvas content as a data URL and passes it to the scene API.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
class Example implements EditorPlugin {  name = packageJson.name;  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (cesdk == null) {      throw new Error('CE.SDK instance is required for this plugin');    }
    const engine = cesdk.engine;
    const canvas = document.createElement('canvas');    canvas.width = 512;    canvas.height = 512;
    const ctx = canvas.getContext('2d');    if (ctx == null) {      throw new Error('Could not get 2D context');    }
    // Draw a gradient background    const gradient = ctx.createLinearGradient(0, 0, 512, 512);    gradient.addColorStop(0, '#4158D0');    gradient.addColorStop(0.5, '#C850C0');    gradient.addColorStop(1, '#FFCC70');    ctx.fillStyle = gradient;    ctx.fillRect(0, 0, 512, 512);
    // Draw "img.ly" text    ctx.fillStyle = '#FFFFFF';    ctx.font = 'bold 72px Arial, sans-serif';    ctx.textAlign = 'center';    ctx.textBaseline = 'middle';    ctx.fillText('img.ly', 256, 256);
    const dataURL = canvas.toDataURL();
    // Second parameter is DPI: 72 for screen, 300 for print (default)    await engine.scene.createFromImage(dataURL);
    // Enable auto-fit zoom on the page    const pages = engine.block.findByType('page');    if (pages.length > 0) {      engine.scene.enableZoomAutoFit(pages[0], 'Both', 40, 40, 40, 40);    }  }}
export default Example;
```

This guide covers how to create a canvas element, draw content to it, extract that content as a data URL, and create an editable CE.SDK scene from the result.

## Create the Canvas[#](#create-the-canvas)

Start by creating a canvas element with specific dimensions. These dimensions determine the resulting scene size.

```
const canvas = document.createElement('canvas');canvas.width = 512;canvas.height = 512;
```

The canvas `width` and `height` attributes set the actual pixel dimensions, not CSS styling.

## Get the Drawing Context[#](#get-the-drawing-context)

Obtain the 2D rendering context from the canvas to draw content.

```
const ctx = canvas.getContext('2d');if (ctx == null) {  throw new Error('Could not get 2D context');}
```

Use the context to render any graphics—2D drawings, chart visualizations, or programmatic visuals.

## Extract as Data URL[#](#extract-as-data-url)

Extract the canvas content as a base64-encoded data URL using `toDataURL()`.

```
const dataURL = canvas.toDataURL();
```

The default format is PNG. For JPEG with compression, use `canvas.toDataURL('image/jpeg', 0.9)`.

## Create Scene from Data URL[#](#create-scene-from-data-url)

Pass the data URL to `engine.scene.createFromImage()` to create an editable scene. The page dimensions automatically match the source image.

```
// Second parameter is DPI: 72 for screen, 300 for print (default)await engine.scene.createFromImage(dataURL);
```

The second parameter controls DPI: use 72 for screen display or 300 (default) for print output.

## Common Canvas Sources[#](#common-canvas-sources)

The `createFromImage()` method accepts any valid image data URL, making it compatible with various canvas sources:

*   **Chart Libraries** — D3.js, Chart.js, and Plotly render visualizations to canvas
*   **WebGL Content** — 3D renders, games, and complex visualizations
*   **Drawing Applications** — Capture user-created sketches and annotations
*   **QR Code Generators** — Libraries like `qrcode.js` render directly to canvas
*   **Generative Art** — p5.js and Processing.js output to canvas elements
*   **Video Frames** — Draw video frames to canvas with `drawImage(video, 0, 0)`

Each source follows the same pattern: render to canvas, extract with `toDataURL()`, and pass to CE.SDK.

## Troubleshooting[#](#troubleshooting)

**Canvas content not appearing**

Verify the canvas has content before calling `toDataURL()`. Async rendering can produce blank exports. For WebGL canvases, set `preserveDrawingBuffer: true` in the context options.

**Tainted canvas errors**

Cross-origin images drawn to the canvas taint it, preventing `toDataURL()` calls. Use `crossOrigin="anonymous"` when loading images, and ensure the server sends proper CORS headers.

**Scene dimensions incorrect**

Canvas `width` and `height` attributes determine the actual pixel dimensions, not CSS styling. The data URL captures attribute dimensions, not the displayed size.

**WebGL context lost**

WebGL contexts can be lost due to GPU resource limits. Listen for the `webglcontextlost` event and handle gracefully by recreating the context or notifying the user.

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `engine.scene.createFromImage(url, dpi?, pixelScaleFactor?)` | Creates a scene from an image URL or data URL. Default DPI is 300. |
| `engine.scene.get()` | Returns the current scene block ID, or `null` if no scene exists. |
| `engine.scene.enableZoomAutoFit(id, axis, ...padding)` | Enables automatic zoom to fit the specified block. |
| `engine.block.findByType(type)` | Finds all blocks of the specified type. |
| `canvas.toDataURL(type?, quality?)` | Exports canvas content as a base64 data URL. Default type is `image/png`. |
| `canvas.getContext('2d')` | Returns the 2D rendering context for drawing operations. |

## Next Steps[#](#next-steps)

[Create From Image](sveltekit/open-the-editor/from-image-ad9b5e/) shows how to load scenes from image URLs directly.

[Start With Blank Canvas](sveltekit/open-the-editor/blank-canvas-18ff05/) covers starting with an empty scene for new designs.

[Save a Scene](sveltekit/export-save-publish/save-c8b124/) explains how to save your edited scene for later use.

[Load a Scene](sveltekit/open-the-editor/load-scene-478833/) demonstrates loading previously saved scenes.

---



[Source](https:/img.ly/docs/cesdk/sveltekit/open-the-editor/blank-canvas-18ff05)