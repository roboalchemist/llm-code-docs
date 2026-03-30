# Type Alias: TypefaceDefinition

```
type TypefaceDefinition = object;
```

Represents a typeface definition used in the editor.

## Deprecated[#](#deprecated)

This type definition is not used anymore and will be removed.

Defines the structure of a typeface definition, including metadata, family name, and font details.

*   ‘meta’: Optional metadata for the typeface, including default status, library, and categories.
*   ‘family’: The name of the typeface family.
*   ‘fonts’: An array of font definitions, each containing a font URL, weight, and style.

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| ~`meta?`~ | `object` | **Deprecated** The meta field is not used anymore |
| `meta.default?` | `boolean` | \- |
| `meta.library?` | `string` | \- |
| `meta.categories?` | `string`\[\] | \- |
| ~`family`~ | `string` | \- |
| ~`fonts`~ | `object`\[\] | \- |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/timelinezoomtolevelaction)