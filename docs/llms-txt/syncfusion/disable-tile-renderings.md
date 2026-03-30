# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/javascript-es5/how-to/disable-tile-renderings.md

# Disable tile rendering in JavaScript PDF Viewer

Use the `enableTileRendering` property to enable or disable tile rendering. Tile rendering is enabled by default and typically improves performance for large documents. Set `enableTileRendering` to `false` to disable tile rendering when it is not required.

- Include the JavaScript PDF Viewer script and the `ThumbnailView`/`Navigation` modules if using related features.
- Initialize the viewer instance before changing tile rendering settings at runtime.

Example: disable tile rendering with a button

```
<button id="disable">Disable tile rendering</button>

```

```javascript
// Disable tile rendering at runtime
document.getElementById('disable').addEventListener('click', () => {
  viewer.tileRenderingSettings.enableTileRendering = false;
});

```

Sample: [How to disable tile rendering](https://stackblitz.com/edit/7fefpj-n7pyna?file=index.js)