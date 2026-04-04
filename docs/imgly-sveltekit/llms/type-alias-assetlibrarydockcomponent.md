# Type Alias: AssetLibraryDockComponent

```
type AssetLibraryDockComponent = object;
```

Represents an asset library dock component.

The AssetLibraryDockComponent interface defines the structure of an asset library dock component. It includes properties for the ID, key, label, icon, entries, and optional button styling/behavior.

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| `id` | `"ly.img.assetLibrary.dock"` | \- |
| `key?` | `string` | Individual and optional key for the component. |
| `label?` | `string` | Label to display on the button. |
| `icon?` | `string` | Icon to display on the button. |
| `entries` | `string`\[\] | Determines with what entries the asset library is opened. |
| `onClick?` | () => `void` | Custom onClick handler. If provided, overrides the default asset library toggle behavior. |
| `selected?` | `boolean` | Controls the selected state of the button. If provided, overrides the automatic detection. |
| `disabled?` | `boolean` | Controls the disabled state of the button. If provided, overrides the automatic detection. |
| `size?` | `"normal"` | `"large"` |
| `variant?` | `"regular"` | `"plain"` |
| `color?` | `"accent"` | `"danger"` |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/assetgroups)