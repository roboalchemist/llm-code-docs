# Interface: ButtonOptions

Represents options for a button.

The `ButtonOptions` interface provides a set of properties that control the behavior and appearance of a button. These options include settings for the input label, input label position, label, label alignment, tooltip, click handler, variant, color, size, icon, trailing icon, active state, selected state, disabled state, loading state, loading progress, suffix, and keyboard shortcut.

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| `inputLabel?` | `string` | `string`\[\] |
| `inputLabelPosition?` | `"top"` | `"left"` |
| `label?` | `string` | `string`\[\] |
| `labelAlignment?` | `"left"` | `"center"` |
| `tooltip?` | `string` | `string`\[\] |
| `onClick?` | () => `void` | \- |
| `variant?` | `"regular"` | `"plain"` |
| `color?` | `"accent"` | `"danger"` |
| `size?` | `"normal"` | `"large"` |
| `icon?` | [`CustomIcon`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/type-aliases/customicon/) | \- |
| `trailingIcon?` | [`CustomIcon`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/type-aliases/customicon/) | \- |
| `isActive?` | `boolean` | \- |
| `isSelected?` | `boolean` | \- |
| `isDisabled?` | `boolean` | \- |
| `isLoading?` | `boolean` | \- |
| `loadingProgress?` | `number` | \- |
| `suffix?` | `Partial` | \- |
| `shortcut?` | `string` | Keyboard shortcut to display (e.g., ‘Meta+C’, ‘Meta+V’, ‘Alt+D’). Automatically renders OS-appropriate modifiers (⌘ on macOS, Ctrl on Windows/Linux). Hidden on small viewports. |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/buttongroupoptions)