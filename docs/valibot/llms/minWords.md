# Source: https://valibot.dev/api/minWords.md

# minWords

Creates a min [words](https://en.wikipedia.org/wiki/Word) validation action.

```ts
const Action = v.minWords<TInput, TLocales, TRequirement, TMessage>(
  locales,
  requirement,
  message
);
```

## Generics

- `TInput` <Property {...properties.TInput} />
- `TLocales` <Property {...properties.TLocales} />
- `TRequirement` <Property {...properties.TRequirement} />
- `TMessage` <Property {...properties.TMessage} />

## Parameters

- `locales` <Property {...properties.locales} />
- `requirement` <Property {...properties.requirement} />
- `message` <Property {...properties.message} />

### Explanation

With `minWords` you can validate the words of a string based on the specified `locales`. If the input does not match the `requirement`, you can use `message` to customize the error message.

## Returns

- `Action` <Property {...properties.Action} />

## Examples

The following examples show how `minWords` can be used.

### Min words schema

Schema to validate a string with a minimum of 50 words.

```ts
const MinWordsSchema = v.pipe(
  v.string(),
  v.minWords('en', 50, 'The string must contain at least 50 words.')
);
```

## Related

The following APIs can be combined with `minWords`.

### Schemas

<ApiList items={['any', 'custom', 'string']} />

### Methods

<ApiList items={['pipe']} />

### Utils

<ApiList items={['isOfKind', 'isOfType']} />
