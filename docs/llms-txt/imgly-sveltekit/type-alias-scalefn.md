# Type Alias: ScaleFn

```
type ScaleFn = ({ containerWidth, isTouch }) => Scale;
```

A function that returns a scale value based on viewport properties. This allows for dynamic scale selection based on runtime conditions.

## Parameters[#](#parameters)

| Parameter | Type |
| --- | --- |
| `{ containerWidth, isTouch }` | { `containerWidth?`: `number`; `isTouch?`: `boolean`; } |
| `{ containerWidth, isTouch }.containerWidth?` | `number` |
| `{ containerWidth, isTouch }.isTouch?` | `boolean` |

## Returns[#](#returns)

[`Scale`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/scale/)

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/scaleconfig)