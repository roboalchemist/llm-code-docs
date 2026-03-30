# Create Cutout

Create cutout paths for cutting printers to produce die-cut stickers, iron-on decals, and custom-shaped prints programmatically.

![Cutout paths demonstration showing circular and square cutouts combined](/docs/cesdk/_astro/browser.hero.D_qAtTKo_ZnSzEC.webp)

8 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-stickers-and-shapes-create-cutout-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-stickers-and-shapes-create-cutout-browser)

Cutouts define outline paths that cutting printers cut with a blade rather than print with ink. CE.SDK supports creating cutouts from SVG paths, generating them from block contours, and combining them with boolean operations.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import CutoutLibraryPlugin from '@imgly/plugin-cutout-library-web';import packageJson from './package.json';
class Example implements EditorPlugin {  name = packageJson.name;  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    // Load assets and create scene    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Design',      withUploadAssetSources: true,    });
    // Add cutout library plugin for UI-based cutout creation    await cesdk.addPlugin(      CutoutLibraryPlugin({        ui: { locations: ['canvasMenu'] },      }),    );
    // Add cutout library to dock as the last entry    const cutoutAssetEntry = cesdk.ui.getAssetLibraryEntry(      'ly.img.cutout.entry',    );    cesdk.ui.setDockOrder([      ...cesdk.ui        .getDockOrder()        .filter(({ key }) => key !== 'ly.img.template'),      {        id: 'ly.img.assetLibrary.dock',        label: 'Cutouts',        key: 'ly.img.assetLibrary.dock',        icon: cutoutAssetEntry?.icon,        entries: ['ly.img.cutout.entry'],      },    ]);
    // Open cutout library panel on startup    cesdk.ui.openPanel('//ly.img.panel/assetLibrary', {      payload: {        entries: ['ly.img.cutout.entry'],      },    });
    await cesdk.createDesignScene();
    const engine = cesdk.engine;    const page = engine.block.findByType('page')[0];
    // Set page dimensions    engine.block.setWidth(page, 800);    engine.block.setHeight(page, 600);
    // Create a circular cutout from SVG path (scaled up for visibility)    const circle = engine.block.createCutoutFromPath(      'M 0,75 a 75,75 0 1,1 150,0 a 75,75 0 1,1 -150,0 Z',    );    engine.block.appendChild(page, circle);    engine.block.setPositionX(circle, 200);    engine.block.setPositionY(circle, 225);
    // Set cutout type to Dashed for perforated cut line    engine.block.setEnum(circle, 'cutout/type', 'Dashed');
    // Set cutout offset distance from source path    engine.block.setFloat(circle, 'cutout/offset', 5.0);
    // Create a square cutout with solid type (scaled up for visibility)    const square = engine.block.createCutoutFromPath(      'M 0,0 H 150 V 150 H 0 Z',    );    engine.block.appendChild(page, square);    engine.block.setPositionX(square, 450);    engine.block.setPositionY(square, 225);    engine.block.setFloat(square, 'cutout/offset', 8.0);
    // Combine cutouts using Union operation    const combined = engine.block.createCutoutFromOperation(      [circle, square],      'Union',    );    engine.block.appendChild(page, combined);    engine.block.setPositionX(combined, 200);    engine.block.setPositionY(combined, 225);
    // Destroy original cutouts to avoid duplicate cuts    engine.block.destroy(circle);    engine.block.destroy(square);
    // Customize spot color RGB for rendering (bright blue for visibility)    engine.editor.setSpotColorRGB('CutContour', 0.0, 0.4, 0.9);
    // Zoom to fit all cutouts    await engine.scene.zoomToBlock(page, { padding: 40 });  }}
export default Example;
```

This guide covers creating cutouts programmatically from SVG paths, configuring cutout types and offsets, combining cutouts with boolean operations, customizing spot colors for printer compatibility, and integrating the cutout library plugin for interactive creation.

## Understanding Cutouts[#](#understanding-cutouts)

Cutouts are special blocks that contain SVG paths interpreted by cutting printers as cut lines. Printers recognize cutouts through specially named spot colors: `CutContour` for solid continuous cuts and `PerfCutContour` for dashed perforated cuts.

The spot color RGB values affect on-screen rendering but not printer behavior. By default, solid cutouts render as magenta and dashed cutouts render as green.

Cutouts export to PDF format with spot color information preserved. Cutting printers read the spot colors to identify cut paths.

## Creating Cutouts from SVG Paths[#](#creating-cutouts-from-svg-paths)

Create cutouts using `engine.block.createCutoutFromPath(path)` with standard SVG path syntax. The path coordinates define the cutout dimensions.

```
// Create a circular cutout from SVG path (scaled up for visibility)const circle = engine.block.createCutoutFromPath(  'M 0,75 a 75,75 0 1,1 150,0 a 75,75 0 1,1 -150,0 Z',);engine.block.appendChild(page, circle);engine.block.setPositionX(circle, 200);engine.block.setPositionY(circle, 225);
```

The method accepts standard SVG path commands: `M` (move), `L` (line), `H` (horizontal), `V` (vertical), `C` (cubic curve), `Q` (quadratic curve), `A` (arc), and `Z` (close path).

## Configuring Cutout Type[#](#configuring-cutout-type)

Set the cutout type using `engine.block.setEnum()` to control whether the printer creates a continuous or perforated cut line.

```
// Set cutout type to Dashed for perforated cut lineengine.block.setEnum(circle, 'cutout/type', 'Dashed');
```

`Solid` creates a continuous cutting line (default), while `Dashed` creates a perforated cutting line for tear-away edges.

## Configuring Cutout Offset[#](#configuring-cutout-offset)

Adjust the distance between the cutout line and the source path using `engine.block.setFloat()`.

```
// Set cutout offset distance from source pathengine.block.setFloat(circle, 'cutout/offset', 5.0);
```

Positive offset values expand the cutout outward from the path. Use offset to add bleed or margin around designs for cleaner cuts.

## Creating Multiple Cutouts[#](#creating-multiple-cutouts)

Create additional cutouts with different properties to demonstrate various shapes and configurations.

```
// Create a square cutout with solid type (scaled up for visibility)const square = engine.block.createCutoutFromPath(  'M 0,0 H 150 V 150 H 0 Z',);engine.block.appendChild(page, square);engine.block.setPositionX(square, 450);engine.block.setPositionY(square, 225);engine.block.setFloat(square, 'cutout/offset', 8.0);
```

Each cutout can have independent type and offset settings based on your production requirements.

## Combining Cutouts with Boolean Operations[#](#combining-cutouts-with-boolean-operations)

Combine multiple cutouts into compound shapes using `engine.block.createCutoutFromOperation(ids, operation)`. Available operations are `Union`, `Difference`, `Intersection`, and `XOR`.

```
// Combine cutouts using Union operationconst combined = engine.block.createCutoutFromOperation(  [circle, square],  'Union',);engine.block.appendChild(page, combined);engine.block.setPositionX(combined, 200);engine.block.setPositionY(combined, 225);
// Destroy original cutouts to avoid duplicate cutsengine.block.destroy(circle);engine.block.destroy(square);
```

The combined cutout inherits the type from the first cutout in the array and has an offset of 0. Destroy the original cutouts after combining to avoid duplicate cuts.

When using `Difference`, the first cutout is the base that others subtract from. For other operations, the order affects which cutout’s type is inherited.

## Customizing Spot Colors[#](#customizing-spot-colors)

Modify the spot color RGB approximation using `engine.editor.setSpotColorRGB()` to change how cutouts render without affecting printer behavior.

```
// Customize spot color RGB for rendering (bright blue for visibility)engine.editor.setSpotColorRGB('CutContour', 0.0, 0.4, 0.9);
```

Spot color names (`CutContour`, `PerfCutContour`) are what printers recognize. Adjust the names if your printer uses different conventions.

## Using the Cutout Library Plugin[#](#using-the-cutout-library-plugin)

The `@imgly/plugin-cutout-library-web` plugin provides an interactive UI for creating cutouts directly in the editor. Users can add rectangular or elliptical cutouts from the asset library dock, or generate cutouts from selected shapes via the canvas menu.

Install the plugin:

[

npm

](#tab-panel-484)[

yarn

](#tab-panel-485)[

pnpm

](#tab-panel-486)

Terminal window

```
npm install @imgly/plugin-cutout-library-web
```

Terminal window

```
yarn add @imgly/plugin-cutout-library-web
```

Terminal window

```
pnpm add @imgly/plugin-cutout-library-web
```

Import and register the plugin:

```
import CutoutLibraryPlugin from '@imgly/plugin-cutout-library-web';
```

Add the plugin to your editor instance with canvas menu support:

```
// Add cutout library plugin for UI-based cutout creationawait cesdk.addPlugin(  CutoutLibraryPlugin({    ui: { locations: ['canvasMenu'] },  }),);
```

Configure the dock to display the cutout library and open it by default:

```
// Add cutout library to dock as the last entryconst cutoutAssetEntry = cesdk.ui.getAssetLibraryEntry(  'ly.img.cutout.entry',);cesdk.ui.setDockOrder([  ...cesdk.ui    .getDockOrder()    .filter(({ key }) => key !== 'ly.img.template'),  {    id: 'ly.img.assetLibrary.dock',    label: 'Cutouts',    key: 'ly.img.assetLibrary.dock',    icon: cutoutAssetEntry?.icon,    entries: ['ly.img.cutout.entry'],  },]);
// Open cutout library panel on startupcesdk.ui.openPanel('//ly.img.panel/assetLibrary', {  payload: {    entries: ['ly.img.cutout.entry'],  },});
```

The `setDockOrder` method adds a “Cutouts” entry to the dock panel with the plugin’s icon. The `openPanel` call displays the cutout library immediately when the editor loads, giving users instant access to cutout creation tools.

The plugin provides three cutout options: generate from selection (creates cutout from selected blocks), rectangle, and circle. The canvas menu button appears when blocks are selected for quick cutout generation.

## Troubleshooting[#](#troubleshooting)

### Cutout Not Visible[#](#cutout-not-visible)

Cutouts render using spot color RGB approximations. Verify the cutout is appended to the page hierarchy and positioned within the visible canvas area.

### Printer Not Cutting[#](#printer-not-cutting)

Check that spot color names match your printer’s requirements. Some printers need specific names like `CutContour` or `Thru-cut`. Consult your printer documentation.

### Combined Cutout Has Wrong Type[#](#combined-cutout-has-wrong-type)

Combined cutouts inherit the type from the first cutout in the array. Reorder the array or set the type explicitly after combination.

## API Reference[#](#api-reference)

| Method | Category | Purpose |
| --- | --- | --- |
| `cesdk.addPlugin(CutoutLibraryPlugin(config))` | Plugin | Register cutout library plugin |
| `cesdk.ui.getAssetLibraryEntry(id)` | UI | Get asset library entry for dock |
| `cesdk.ui.setDockOrder(entries)` | UI | Configure dock panel order |
| `cesdk.ui.openPanel(id, options)` | UI | Open panel programmatically |
| `engine.block.createCutoutFromPath(path)` | Cutout | Create cutout from SVG path string |
| `engine.block.createCutoutFromBlocks(ids, vThresh, sThresh, useShape)` | Cutout | Create cutout from block contours |
| `engine.block.createCutoutFromOperation(ids, op)` | Cutout | Combine cutouts with boolean operation |
| `engine.block.setEnum(id, 'cutout/type', value)` | Property | Set cutout type (Solid/Dashed) |
| `engine.block.setFloat(id, 'cutout/offset', value)` | Property | Set cutout offset distance |
| `engine.block.setFloat(id, 'cutout/smoothing', value)` | Property | Set corner smoothing threshold |
| `engine.block.appendChild(parent, child)` | Hierarchy | Add cutout to scene |
| `engine.block.setPositionX/Y(id, value)` | Transform | Position cutout on canvas |
| `engine.block.destroy(id)` | Lifecycle | Remove cutout from scene |
| `engine.editor.setSpotColorRGB(name, r, g, b)` | Editor | Customize spot color rendering |

## Next Steps[#](#next-steps)

*   **[Combine Shapes](sveltekit/stickers-and-shapes/combine-2a9e26/)** \- Boolean operations on graphic blocks
*   **[Create Shapes](sveltekit/stickers-and-shapes/create-edit/create-shapes-64acc0/)** \- Create geometric shapes programmatically
*   **[Export for Printing](sveltekit/export-save-publish/for-printing-bca896/)** \- Export print-ready PDFs with spot colors

---



[Source](https:/img.ly/docs/cesdk/sveltekit/stickers-and-shapes/combine-2a9e26)