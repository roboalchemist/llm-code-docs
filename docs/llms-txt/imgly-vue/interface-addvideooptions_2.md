# Interface: AddVideoOptions

Options for adding videos to the scene.

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| `sizeMode?` | [`SizeMode`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/sizemode/) | How the video should be sized and positioned |
| `positionMode?` | [`PositionMode`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/positionmode/) | How the position should be interpreted |
| `x?` | `number` | X position in scene design units |
| `y?` | `number` | Y position in scene design units |
| `cornerRadius?` | `number` | Corner radius for rounded corners in scene design units |
| `timeline?` | `object` | Timeline configuration |
| `timeline.timeOffset?` | `number` | Start time offset in seconds |
| `timeline.duration?` | `number` | Duration in seconds |
| `shadow?` | [`DropShadowOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dropshadowoptions/) | Drop shadow configuration |
| `animation?` | [`AnimationOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/animationoptions/) | Animation configuration |

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/zoomtopageaction)