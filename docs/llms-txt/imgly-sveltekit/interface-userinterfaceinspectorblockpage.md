# Interface: UserInterfaceInspectorBlockPage

Interface representing a page block in the user interface inspector.

*   `format`: Optional element or boolean indicating whether the format section should be shown.
*   `manage`: Optional element or boolean indicating whether the manage section should be shown.
*   `maxDuration`: Optional number controlling the maximum allowed duration of a page, if in video mode.
*   `crop`: Optional element or boolean indicating whether the crop section should be shown.
*   `filters`: Optional element or boolean indicating whether the filters section should be shown.
*   `adjustments`: Optional element or boolean indicating whether the adjustments section should be shown.
*   `effects`: Optional element or boolean indicating whether the effects section should be shown.
*   `blur`: Optional element or boolean indicating whether the blur section should be shown.

## Deprecated[#](#deprecated)

Use `cesdk.feature.enable()` for page-related features instead.

## Extends[#](#extends)

*   [`UserInterfaceInspectorBlock`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/userinterfaceinspectorblock/)

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| ~`format?`~ |  | `boolean` |
| ~`manage?`~ |  | `boolean` |
| ~`maxDuration?`~ | `number` | **Deprecated** Use feature API instead. Controls the maximum allowed duration of a page, if in video mode. |
| ~`crop?`~ |  | `boolean` |
| ~`filters?`~ |  | `boolean` |
| ~`adjustments?`~ |  | `boolean` |
| ~`effects?`~ |  | `boolean` |
| ~`blur?`~ |  | `boolean` |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/userinterfaceinspectorblockimage)