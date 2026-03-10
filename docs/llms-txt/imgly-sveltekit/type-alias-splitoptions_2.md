# Type Alias: SplitOptions

```
type SplitOptions = object;
```

Options for configuring block split operations.

## Properties[#](#properties)

| Property | Type | Default value | Description |
| --- | --- | --- | --- |
| `attachToParent?` | `boolean` | `true` | Whether or not the new block will be attached to the same parent as the original. |
| `createParentTrackIfNeeded?` | `boolean` | `false` | Whether to create a parent track if needed and add both blocks to it. Only used when attachToParent is true. |
| `selectNewBlock?` | `boolean` | `true` | Whether to select the newly created block after splitting. |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/sourcesetpropertyname)