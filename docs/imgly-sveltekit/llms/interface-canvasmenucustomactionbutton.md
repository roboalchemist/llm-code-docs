# Interface: CanvasMenuCustomActionButton

Interface representing a custom canvas menu action button. Note: This component requires a key and has a required label, unlike other action buttons.

## Extends[#](#extends)

*   [`OrderComponent`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/ordercomponent/)

## Indexable[#](#indexable)

```
[key: string]: unknown
```

## Properties[#](#properties)

| Property | Type | Overrides |
| --- | --- | --- |
| `id` | `"ly.img.action.canvasMenu"` | [`OrderComponent`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/ordercomponent/).[`id`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/ordercomponent/) |
| `key` | `string` | [`OrderComponent`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/ordercomponent/).[`key`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/ordercomponent/) |
| `onClick` | () => `void` | `Promise`<`void`\> |
| `label` | `string` | \- |
| `icon?` | `string` | \- |
| `variant?` | `"regular"` | `"plain"` |
| `isDisabled?` | `boolean` | \- |
| `shortcut?` | `string` | \- |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/canvasmenuactionbutton)