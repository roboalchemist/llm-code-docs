# Source: https://valibot.dev/api/promise.md

# promise

Creates a promise schema.

```ts
const Schema = v.promise<TMessage>(message);
```

## Generics

- `TMessage` <Property {...properties.TMessage} />

## Parameters

- `message` <Property {...properties.message} />

### Explanation

With `promise` you can validate the data type of the input. If the input is not a promise, you can use `message` to customize the error message.

## Returns

- `Schema` <Property {...properties.Schema} />

## Examples

The following examples show how `promise` can be used.

### Number promise

Schema to validate a promise that resolves to a number.

```ts
const NumberPromiseSchema = v.pipeAsync(
  v.promise(),
  v.awaitAsync(),
  v.number()
);
```

## Related

The following APIs can be combined with `promise`.

### Schemas

<ApiList
  items={[
    'array',
    'exactOptional',
    'intersect',
    'lazy',
    'looseObject',
    'looseTuple',
    'map',
    'nonNullable',
    'nonNullish',
    'nonOptional',
    'nullable',
    'nullish',
    'object',
    'objectWithRest',
    'optional',
    'record',
    'set',
    'strictObject',
    'strictTuple',
    'tuple',
    'tupleWithRest',
    'undefinedable',
    'union',
  ]}
/>

### Methods

<ApiList
  items={[
    'assert',
    'config',
    'fallback',
    'getDefault',
    'getDefaults',
    'getFallback',
    'getFallbacks',
    'is',
    'message',
    'parse',
    'parser',
    'pipe',
    'safeParse',
    'safeParser',
  ]}
/>

### Actions

<ApiList
  items={[
    'awaitAsync',
    'check',
    'brand',
    'description',
    'flavor',
    'guard',
    'metadata',
    'rawCheck',
    'rawTransform',
    'readonly',
    'title',
    'transform',
  ]}
/>

### Utils

<ApiList items={['entriesFromList', 'isOfKind', 'isOfType']} />
