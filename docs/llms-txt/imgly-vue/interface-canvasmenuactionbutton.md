# Interface: CanvasMenuActionButton

Base interface for action buttons in the canvas menu. Contains common properties shared across all canvas menu button types.

*   `onClick`: Handler invoked when the button is clicked.
*   `label`: Optional label for the button.
*   `icon`: Optional icon name to display on the button.
*   `variant`: Optional style variant of the button, either ‘regular’ or ‘plain’.
*   `isDisabled`: Optional disabled property.
*   `shortcut`: Optional keyboard shortcut displayed alongside the action.

## Extends[#](#extends)

*   [`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)

## Indexable[#](#indexable)

```
[key: string]: unknown
```

## Properties[#](#properties)

| Property | Type | Overrides | Inherited from |
| --- | --- | --- | --- |
| `id` |  | `"ly.img.flipX.canvasMenu"` | `"ly.img.flipY.canvasMenu"` |
| `onClick?` | () => `void` | `Promise`<`void`\> | \- |
| `label?` | `string` | \- | \- |
| `icon?` | `string` | \- | \- |
| `variant?` | `"regular"` | `"plain"` | \- |
| `isDisabled?` | `boolean` | \- | \- |
| `shortcut?` | `string` | \- | \- |
| `key?` | `string` | \- | [`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/).[`key`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/) |

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/buttonoptions)