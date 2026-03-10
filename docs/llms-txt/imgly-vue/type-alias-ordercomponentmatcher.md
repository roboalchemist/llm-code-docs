# Type Alias: OrderComponentMatcher

```
type OrderComponentMatcher<C> =  | "first"  | "last"  | number  | C["id"]  | Partial<C>  | (component, index) => boolean;
```

Represents a matcher for order components.

The OrderComponentMatcher type defines the possible matchers for order components. It includes predefined matchers for component IDs, partial components, and custom matchers.

## Type Parameters[#](#type-parameters)

| Type Parameter |
| --- |
| `C` _extends_ [`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/) |

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/optional)