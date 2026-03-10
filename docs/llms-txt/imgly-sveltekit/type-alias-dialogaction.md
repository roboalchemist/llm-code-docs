# Type Alias: DialogAction

```
type DialogAction = object;
```

Represents an action in the dialog.

The DialogAction type defines the structure of an action that can be performed within a dialog. It includes properties for the variant, color, label, and a callback function to handle the action when clicked, providing flexibility in how user interactions are managed.

## Properties[#](#properties)

| Property | Type |
| --- | --- |
| `variant?` | `"regular"` |
| `color?` | `"accent"` |
| `label` | `string` |
| `onClick` | (`context`) => `void` |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/designunit)