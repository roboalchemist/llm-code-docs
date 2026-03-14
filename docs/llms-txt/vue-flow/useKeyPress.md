# Source: https://vueflow.dev/typedocs/functions/useKeyPress.md

---
url: /typedocs/functions/useKeyPress.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Function: useKeyPress()

> **useKeyPress**(`keyFilter`, `options`?): `ShallowRef`<`boolean`>

Composable that returns a boolean value if a key is pressed

## Parameters

• **keyFilter**: `MaybeRefOrGetter`<`null` | `false` | `KeyFilter`>

Can be a boolean, a string, an array of strings or a function that returns a boolean. If it's a boolean, it will act as if the key is always pressed. If it's a string, it will return true if a key matching that string is pressed. If it's an array of strings, it will return true if any of the strings match a key being pressed, or a combination (e.g. \['ctrl+a', 'ctrl+b'])

• **options?**: `UseKeyPressOptions`

Options object

## Returns

`ShallowRef`<`boolean`>
