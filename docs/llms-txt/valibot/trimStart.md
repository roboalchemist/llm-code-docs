# Source: https://valibot.dev/api/trimStart.md

# trimStart

Creates a trim start transformation action.

```ts
const Action = v.trimStart();
```

## Returns

- `Action` <Property {...properties.Action} />

## Examples

The following examples show how `trimStart` can be used.

### Trimmed string

Schema to trimStart the start of a string.

```ts
const StringSchema = v.pipe(v.string(), v.trimStart());
```

## Related

The following APIs can be combined with `trimStart`.

### Schemas

<ApiList items={['any', 'custom', 'string']} />

### Methods

<ApiList items={['pipe']} />

### Utils

<ApiList items={['isOfKind', 'isOfType']} />
