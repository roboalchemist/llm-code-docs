# Source: https://docs.slatejs.org/v0.47/other-packages/index-2.md

# slate-plain-serializer

```javascript
import Plain from 'slate-plain-serializer'
```

A serializer that converts a Slate [`Value`](https://docs.slatejs.org/v0.47/slate-core/value) to and from a plain text string.

## Example

```
The Slate editor gives you full control over the logic you can add.\n
In its simplest form, when representing plain text, Slate is a glorified <textarea>. But you can augment it to be much more than that.\n
Check out http://slatejs.org for examples!
```

## Methods

### `Plain.deserialize`

`Plain.deserialize(string: String, [options: Object]) => Value`

Deserialize a plain text `string` into a [`Value`](https://docs.slatejs.org/v0.47/slate-core/value). A series of blocks will be created by splitting the input string on `\n` characters. Each block is given a type of `'line'`.

If you pass `toJSON: true` as an option, the return value will be a JSON object instead of a [`Value`](https://docs.slatejs.org/v0.47/slate-core/value) object.

### `Plain.serialize`

`Plain.serialize(value: Value) => String`

Serialize a `value` into a plain text string. Each direct child block of the document will be separated by a `\n` character.
