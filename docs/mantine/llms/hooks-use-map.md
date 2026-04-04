# Source: https://mantine.dev/llms/hooks-use-map.md

# useMap
Package: @mantine/hooks
Import: import { UseMap } from '@mantine/hooks';

## Usage

`useMap` returns [Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
object that can be used as React state – `set`, `clear` and `delete` methods update state and trigger rerender.



## Definition

```tsx
function useMap<T, V>(initialState?: [T, V][]): Map<T, V>;
```
