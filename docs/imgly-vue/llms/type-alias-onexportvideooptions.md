# Type Alias: OnExportVideoOptions

```
type OnExportVideoOptions = VideoExportOptions & object;
```

This interface extends the base VideoExportOptions with additional information about the export, including which design blocks were exported and the mimeType.

## Type declaration[#](#type-declaration)

| Name | Type |
| --- | --- |
| `mimeType` | [`VideoMimeType`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/videomimetype/) |
| `exportedBlocks?` | [`DesignBlockId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/designblockid/)\[\] |

## See[#](#see)

*   VideoExportOptions For base export configuration options
*   DesignBlockId For design block identifier type

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/onexportoptions)