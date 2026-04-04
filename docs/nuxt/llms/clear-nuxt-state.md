# Source: https://nuxt.com/raw/docs/3.x/api/utils/clear-nuxt-state.md

# Source: https://nuxt.com/raw/docs/4.x/api/utils/clear-nuxt-state.md

# clearNuxtState

> Delete the cached state of useState.

<note>

This method is useful if you want to invalidate the state of `useState`.

</note>

## Type

```ts [Signature]
export function clearNuxtState (keys?: string | string[] | ((key: string) => boolean)): void
```

## Parameters

- `keys`: One or an array of keys that are used in [`useState`](/docs/4.x/api/composables/use-state) to delete their cached state. If no keys are provided, **all state** will be invalidated.
