# Interface: UserInterfaceInspectorBlocks

Interface representing the blocks in the user interface inspector.

*   `opacity`: Optional element or boolean indicating whether the opacity block should be shown.
*   `transform`: Optional element or boolean indicating whether the transform block should be shown.
*   `trim`: Optional element or boolean indicating whether the trim block should be shown.
*   `//ly.img.ubq/text`: Optional text block configuration.
*   `//ly.img.ubq/page`: Optional page block configuration.
*   `//ly.img.ubq/graphic`: Optional graphic block configuration.

## Deprecated[#](#deprecated)

Use `cesdk.feature.enable()` instead.

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| ~`opacity?`~ |  | `boolean` |
| ~`transform?`~ |  | `boolean` |
| ~`trim?`~ |  | `boolean` |
| ~`//ly.img.ubq/text?`~ | [`UserInterfaceInspectorBlockText`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/userinterfaceinspectorblocktext/) | **Deprecated** Use `cesdk.feature.enable()` for text-related features instead. |
| ~`//ly.img.ubq/page?`~ | [`UserInterfaceInspectorBlockPage`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/userinterfaceinspectorblockpage/) | **Deprecated** Use `cesdk.feature.enable()` for page-related features instead. |
| ~`//ly.img.ubq/graphic?`~ | [`UserInterfaceInspectorBlockGraphic`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/userinterfaceinspectorblockgraphic/) | **Deprecated** Use `cesdk.feature.enable()` for graphic-related features instead. |

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/userinterfaceinspectorblockrectshape)