# Create versioned directory and extract assetsmkdir -p public/cesdk/1.67.0unzip imgly-assets.zip -d public/cesdk/1.67.0/rm imgly-assets.zip
```

Then configure CE.SDK to use your self-hosted assets:

```
import CreativeEditorSDK from '@cesdk/cesdk-js';
const config = {  license: 'YOUR_CESDK_LICENSE_KEY',  baseURL: `https://cdn.yourdomain.com/cesdk/${CreativeEditorSDK.version}/`,};
CreativeEditorSDK.create(container, config).then(cesdk => {  cesdk.addDefaultAssetSources({    baseURL: `https://cdn.yourdomain.com/cesdk/${CreativeEditorSDK.version}/`,  });});
```

**Versioned paths recommended**: Using version-specific paths like `/cesdk/${CreativeEditorSDK.version}/` allows you to run multiple SDK versions in parallel, simplifies rollbacks, and ensures clean cache invalidation during upgrades.

## Understanding CE.SDK Assets[#](#understanding-cesdk-assets)

CE.SDK assets are distributed in an `imgly-assets.zip` file available for download from the IMG.LY CDN. Understanding what’s in this archive helps you decide which assets to host and how to keep them updated.

### Asset Categories[#](#asset-categories)

The ZIP file contains directories organized by function:

| Directory | Contents | Version-Locked? | Required? |
| --- | --- | --- | --- |
| `core/` | WASM engine files (`.wasm`, `.data`, `worker-host.js`) | **Yes** | **Yes** |
| `ui/` | UI resources (audio waveform, fonts, stylesheets) | **Yes** | **Yes** |
| `emoji/` | Emoji assets | **Yes** | **Yes** |
| `fonts/` | System fonts | **Yes** | **Yes** |
| `i18n/` | Translations | **Yes** | No (bundled in SDK) |
| `ly.img.sticker/` | Stickers | No | If using default assets |
| `ly.img.sticker.misc/` | Additional stickers | No | If using default assets |
| `ly.img.vectorpath/` | Shapes and arrows | No | If using default assets |
| `ly.img.typeface/` | Font definitions | No | If using default assets |
| `ly.img.filter.lut/` | LUT filter effects | No | If using default assets |
| `ly.img.filter.duotone/` | Duotone effects | No | If using default assets |
| `ly.img.effect/` | Visual effects | No | If using default assets |
| `ly.img.blur/` | Blur presets | No | If using default assets |
| `ly.img.colors.defaultPalette/` | Color palettes | No | If using default assets |
| `ly.img.crop.presets/` | Crop aspect ratios | No | If using default assets |
| `ly.img.page.presets/` | Page format presets | No | If using default assets |
| `ly.img.page.presets.video/` | Video page presets | No | If using default assets |
| `ly.img.captionPresets/` | Caption formatting presets | No | If using default assets |
| `ly.img.animation/` | Animation presets | No | If using default assets |
| `ly.img.animation.text/` | Text animation presets | No | If using default assets |
| `ly.img.image/` | Sample images (demo content) | No | No |
| `ly.img.video/` | Sample videos (demo content) | No | No |
| `ly.img.audio/` | Sample audio (demo content) | No | No |
| `ly.img.template/` | Design templates (demo content) | No | No |
| `ly.img.video.template/` | Video templates (demo content) | No | No |
| `ly.img.textComponents/` | Text components (demo content) | No | No |

For most integrations, you need `core/`, `ui/`, `emoji/`, `fonts/`, and the `ly.img.*` asset sources you use.

### Version-Locked vs. Independent Assets[#](#version-locked-vs-independent-assets)

**Version-locked assets** (`core/`, `ui/`, `i18n/`) must match your SDK version. Mismatched versions cause load errors—the engine will fail to initialize if core files don’t match.

**Independent assets** (`ly.img.*` directories) can be updated separately. Configure these via `addDefaultAssetSources({ baseURL })` and `addDemoAssetSources({ baseURL })`. Check the changelog when upgrading to see if asset versions have changed.

### Default Asset Sources[#](#default-asset-sources)

Calling `addDefaultAssetSources()` registers these asset sources:

*   `ly.img.sticker` - Stickers
*   `ly.img.sticker.misc` - Additional stickers
*   `ly.img.vectorpath` - Shapes and arrows
*   `ly.img.typeface` - Font definitions
*   `ly.img.colors.defaultPalette` - Color palettes
*   `ly.img.filter.lut` - LUT effects
*   `ly.img.filter.duotone` - Duotone effects
*   `ly.img.effect` - Visual effects
*   `ly.img.blur` - Blur presets
*   `ly.img.crop.presets` - Crop aspect ratios
*   `ly.img.page.presets` - Page format presets
*   `ly.img.page.presets.video` - Video page presets
*   `ly.img.captionPresets` - Caption formatting
*   `ly.img.animation` - Animation presets
*   `ly.img.animation.text` - Text animation presets

### Demo Asset Sources[#](#demo-asset-sources)

Calling `addDemoAssetSources()` registers sample content sources for development:

*   `ly.img.image` - Sample images
*   `ly.img.video` - Sample videos
*   `ly.img.audio` - Sample audio
*   `ly.img.template` - Design templates
*   `ly.img.video.template` - Video templates
*   `ly.img.textComponents` - Text components
*   `ly.img.image.upload`, `ly.img.video.upload`, `ly.img.audio.upload` - Upload sources

These are intended for development and prototyping—replace them with your own content in production.

## Configuration Options[#](#configuration-options)

Browser configuration involves three settings: `baseURL`, `core.baseURL`, and the `baseURL` option for asset sources.

### Editor Configuration[#](#editor-configuration)

Pass configuration to `CreativeEditorSDK.create()`:

```
import CreativeEditorSDK from '@cesdk/cesdk-js';
const config = {  baseURL: `https://cdn.yourdomain.com/cesdk/${CreativeEditorSDK.version}/`,  core: {    baseURL: 'core/',  },};
CreativeEditorSDK.create(container, config).then(cesdk => {  // Editor initialized with self-hosted assets});
```

**`baseURL`** — Base path for all engine assets. Can be an absolute URL or a relative path. Relative paths resolve against `window.location.href`. Defaults to the IMG.LY CDN.

**`core.baseURL`** — Path to WASM files. Defaults to `core/` relative to `baseURL`. Usually you don’t need to change this unless hosting WASM files separately.

### Asset Sources Configuration[#](#asset-sources-configuration)

Configure asset sources after initializing the editor:

```
CreativeEditorSDK.create(container, config).then(cesdk => {  // Point default assets to your server  cesdk.addDefaultAssetSources({    baseURL: `https://cdn.yourdomain.com/cesdk/${CreativeEditorSDK.version}/`,  });
  // Optional: Add demo assets for development  cesdk.addDemoAssetSources({    baseURL: `https://cdn.yourdomain.com/cesdk/${CreativeEditorSDK.version}/`,  });});
```

The `baseURL` for asset sources must be an absolute URL. The engine looks up asset definitions at `{baseURL}/{sourceId}/content.json` and references files like `{baseURL}/{sourceId}/images/example.png`.

## Excluding Unused Asset Sources[#](#excluding-unused-asset-sources)

If you only need a subset of default assets, use `excludeAssetSourceIds` to skip loading sources you don’t use:

```
cesdk.addDefaultAssetSources({  baseURL: `https://cdn.yourdomain.com/cesdk/${CreativeEditorSDK.version}/`,  excludeAssetSourceIds: ['ly.img.sticker', 'ly.img.page.presets.video'],});
```

This reduces initial load time by not fetching unused asset definitions.

## Troubleshooting[#](#troubleshooting)

### WASM Load Errors[#](#wasm-load-errors)

If the engine fails to initialize with missing `.wasm` or `.data` errors, verify:

1.  The assets ZIP version matches your SDK version
2.  The `core.baseURL` points to the correct directory
3.  Your server returns correct MIME types for `.wasm` files (`application/wasm`)

### 404 Errors for Assets[#](#404-errors-for-assets)

If the console shows 404 errors for `content.json` files:

1.  Verify the `baseURL` in `addDefaultAssetSources()` is correct
2.  Check that asset directories exist at the expected paths
3.  Configure CORS headers if serving assets from a different domain

### CDN Warning in Console[#](#cdn-warning-in-console)

The warning “You’re using the IMG.LY CDN” appears when using default configuration. Set `baseURL` in your config to use self-hosted assets and remove the warning.

## API Reference[#](#api-reference)

| Method/Config | Purpose |
| --- | --- |
| `CreativeEditorSDK.create(container, config)` | Initialize editor with configuration |
| `config.baseURL` | Base path for all engine assets |
| `config.core.baseURL` | Path to WASM/core files (relative to baseURL) |
| `cesdk.addDefaultAssetSources(options)` | Register default asset sources |
| `cesdk.addDemoAssetSources(options)` | Register demo asset sources |
| `CreativeEditorSDK.version` | Get current SDK version string |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/settings-970c98)