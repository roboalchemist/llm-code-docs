# Type Alias: ActionFunction

```
type ActionFunction<T, C> = T extends keyof RegisteredActions ? RegisteredActions[T] : C;
```

Type helper for retrieving the correct action function type based on the action ID. Returns the strongly-typed action for known actions, or a custom action type for unknown IDs.

## Type Parameters[#](#type-parameters)

| Type Parameter | Default type | Description |
| --- | --- | --- |
| `T` _extends_ [`ActionId`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/actionid/) | \- | The action ID type |
| `C` | [`CustomActionFunction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/customactionfunction/) | The custom action function type (defaults to CustomActionFunction) |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/zoomoptions)