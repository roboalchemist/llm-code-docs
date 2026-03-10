# Interface: \_Source

A source that can emit values to subscribed listeners

## Type Parameters[#](#type-parameters)

| Type Parameter |
| --- |
| `T` |

```
_Source(listener): _Unsubscribe;
```

A source that can emit values to subscribed listeners

## Parameters[#](#parameters)

| Parameter | Type |
| --- | --- |
| `listener` | [`_Listener`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/listener/)<`T`\> |

## Returns[#](#returns)

[`_Unsubscribe`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/unsubscribe/)

## Properties[#](#properties)

| Property | Type |
| --- | --- |
| `emit` | (`value`) => `void` |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/engine/interfaces/source)