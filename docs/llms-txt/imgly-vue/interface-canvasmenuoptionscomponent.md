# Interface: CanvasMenuOptionsComponent

Interface representing the canvas menu options dropdown component. This component can contain children components that are rendered in a dropdown menu.

*   `children`: Optional array of child component IDs or components to render in the dropdown.
*   `icon`: Optional icon name to display on the dropdown button.
*   `variant`: Optional style variant of the dropdown button, either ‘regular’ or ‘plain’.
*   `tooltip`: Optional tooltip text to display when hovering over the dropdown button.

## Extends[#](#extends)

*   [`OrderComponentWithChildren`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponentwithchildren/)<[`CanvasMenuComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasmenucomponentid/), [`CanvasMenuActionButton`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/canvasmenuactionbutton/)\>

## Indexable[#](#indexable)

```
[key: string]: unknown
```

## Properties[#](#properties)

| Property | Type | Description | Overrides | Inherited from |
| --- | --- | --- | --- | --- |
| `id` | `"ly.img.options.canvasMenu"` | \- | [`OrderComponentWithChildren`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponentwithchildren/).[`id`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponentwithchildren/) | \- |
| `icon?` | `string` | \- | \- | \- |
| `variant?` | `"regular"` | `"plain"` | \- | \- |
| `tooltip?` | `string` | \- | \- | \- |
| `key?` | `string` | \- | \- | [`OrderComponentWithChildren`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponentwithchildren/).[`key`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponentwithchildren/) |
| `children?` | ( | [`CanvasMenuActionButton`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/canvasmenuactionbutton/) | [`CanvasMenuComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasmenucomponentid/) | [`OrderComponentWithChildren`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponentwithchildren/)<[`CanvasMenuComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasmenucomponentid/), [`CanvasMenuActionButton`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/canvasmenuactionbutton/)\>)\[\] |

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/canvasmenucustomactionbutton)