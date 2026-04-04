# Type Alias: AddImageOptions

```
type AddImageOptions = object;
```

Options for adding images to the scene.

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| `sizeMode?` | [`SizeMode`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/sizemode/) | How the image should be sized and positioned |
| `positionMode?` | [`PositionMode`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/positionmode/) | How the position should be interpreted |
| `x?` | `number` | X position in scene design units |
| `y?` | `number` | Y position in scene design units |
| `cornerRadius?` | `number` | Corner radius for rounded corners in scene design units |
| `size?` |  | `number` |
| `timeline?` | `object` | Timeline configuration for video scenes |
| `timeline.timeOffset?` | `number` | Start time offset in seconds |
| `timeline.duration?` | `number` | Duration in seconds |
| `shadow?` | [`DropShadowOptions`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/dropshadowoptions/) | Drop shadow configuration |
| `animation?` | [`AnimationOptions`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/animationoptions/) | Animation configuration |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements)