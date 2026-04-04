# Interface: \_UBQExportOptions

Specifies options for exporting design blocks to various formats.

The `UBQExportOptions` interface provides a set of properties that control the behavior and quality of the exported content. These options include settings for JPEG, WebP, PNG, and PDF exports, as well as options for resizing and adding underlayers.

## Properties[#](#properties)

| Property | Type |
| --- | --- |
| `jpegQuality` | `number` |
| `webpQuality` | `number` |
| `pngCompressionLevel` | `number` |
| `useTargetSize` | `boolean` |
| `targetWidth` | `number` |
| `targetHeight` | `number` |
| `exportPdfWithHighCompatibility` | `boolean` |
| `exportPdfWithUnderlayer` | `boolean` |
| `underlayerSpotColorName` | `string` |
| `underlayerOffset` | `number` |
| `allowTextOverhang` | `boolean` |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/engine/interfaces/ubqexportaudiooptions)