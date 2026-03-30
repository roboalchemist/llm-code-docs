# Source: https://valibot.dev/api/toLowerCase.md

# toLowerCase

Creates a to lower case transformation action.

```ts
const Action = v.toLowerCase();
```

## Returns

- `Action` <Property {...properties.Action} />

## Examples

The following examples show how `toLowerCase` can be used.

### Lower case string

Schema that transforms a string to lower case.

```ts
const StringSchema = v.pipe(v.string(), v.toLowerCase());
```

## Related

The following APIs can be combined with `toLowerCase`.

### Schemas

<ApiList items={['any', 'custom', 'string']} />

### Methods

<ApiList items={['pipe']} />

### Utils

<ApiList items={['isOfKind', 'isOfType']} />
