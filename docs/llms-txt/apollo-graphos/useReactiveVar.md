# Source: https://www.apollographql.com/docs/react/api/react/useReactiveVar.md

# useReactiveVar

## [`useReactiveVar`](https://www.apollographql.com/docs/react/api/react/useReactiveVar.md#usereactivevar)

Reads the value of a [reactive variable](https://www.apollographql.com/docs/react/local-state/reactive-variables.md) and re-renders the containing component whenever that variable's value changes. This enables a reactive variable to trigger changes *without* relying on the `useQuery` hook.

### [Example](https://www.apollographql.com/docs/react/api/react/useReactiveVar.md#usereactivevar-example)

JavaScript

```
 import { makeVar } from "@apollo/client";
 import { useReactiveVar } from "@apollo/client/react";
 export const cartItemsVar = makeVar([]);

 export function Cart() {
   const cartItems = useReactiveVar(cartItemsVar);
   // ...
 }
```

### [Signature](https://www.apollographql.com/docs/react/api/react/useReactiveVar.md#usereactivevar-signature)

TypeScript

```
useReactiveVar<T>(
  rv: ReactiveVar<T>
): T
```

[(src/react/hooks/useReactiveVar.ts)](https://github.com/apollographql/apollo-client/blob/main/src/react/hooks/useReactiveVar.ts)

### [Parameters](https://www.apollographql.com/docs/react/api/react/useReactiveVar.md#usereactivevar-parameters)

Name / Type

Description

[`rv`](https://www.apollographql.com/docs/react/api/react/useReactiveVar.md#usereactivevar-parameters-rv)\
`ReactiveVar<T>`

A reactive variable.

Show/hide child attributes

### [Result](https://www.apollographql.com/docs/react/api/react/useReactiveVar.md#usereactivevar-result)

The current value of the reactive variable.

```
T
```
