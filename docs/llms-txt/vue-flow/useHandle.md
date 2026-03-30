# Source: https://vueflow.dev/typedocs/functions/useHandle.md

---
url: /typedocs/functions/useHandle.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Function: useHandle()

> **useHandle**(`__namedParameters`): `object`

This composable provides listeners for handle events

Generally it's recommended to use the `<Handle />` component instead of this composable.

## Parameters

• **\_\_namedParameters**: `UseHandleProps`

## Returns

`object`

### handleClick()

> **handleClick**: (`event`) => `void`

#### Parameters

• **event**: `MouseEvent`

#### Returns

`void`

### handlePointerDown()

> **handlePointerDown**: (`event`) => `void`

#### Parameters

• **event**: [`MouseTouchEvent`](../type-aliases/MouseTouchEvent.md)

#### Returns

`void`
