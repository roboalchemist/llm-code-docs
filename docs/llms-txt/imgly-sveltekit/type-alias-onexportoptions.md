# Type Alias: OnExportOptions

```
type OnExportOptions = EngineExportOptions & object;
```

This interface extends the base ExportOptions with additional information about the export, including which design blocks were exported and the mimeType.

## Type declaration[#](#type-declaration)

| Name | Type |
| --- | --- |
| `mimeType` | `Required`<[`EngineExportOptions`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/engineexportoptions/)\>\[`"mimeType"`\] |
| `exportedBlocks?` | [`DesignBlockId`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/designblockid/)\[\] |

## See[#](#see)

*   ExportOptions For base export configuration options
*   DesignBlockId For design block identifier type

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/offscreencanvas)