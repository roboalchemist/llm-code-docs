# Interface: OrderComponentWithChildren

Represents a custom dock component.

The CustomDockComponent interface defines the structure of a custom dock component. It includes properties for the ID and payload.

## Extends[#](#extends)

*   [`OrderComponent`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/ordercomponent/)<`I`\>

## Extended by[#](#extended-by)

*   [`CanvasMenuOptionsComponent`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/canvasmenuoptionscomponent/)

## Type Parameters[#](#type-parameters)

| Type Parameter | Default type |
| --- | --- |
| `I` _extends_ [`ComponentId`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/componentid/) | \- |
| `C` | [`OrderComponent`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/ordercomponent/)<`I`\> |

## Indexable[#](#indexable)

```
[key: string]: unknown
```

## Properties[#](#properties)

| Property | Type | Description | Inherited from |
| --- | --- | --- | --- |
| `id` | `I` | \- | [`OrderComponent`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/ordercomponent/).[`id`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/ordercomponent/) |
| `key?` | `string` | \- | [`OrderComponent`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/ordercomponent/).[`key`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/ordercomponent/) |
| `children?` | (`OrderComponentWithChildren`<`I`, `C`\> | `I` | `C`)\[\] |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/ordercomponent)