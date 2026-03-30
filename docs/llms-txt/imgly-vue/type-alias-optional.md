# Type Alias: Optional

```
type Optional<T, K> = Omit<T, K> & Partial<T>;
```

Turn value at K of T into a Partial

## Type Parameters[#](#type-parameters)

| Type Parameter |
| --- |
| `T` |
| `K` _extends_ keyof `T` |

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/onunsupportedbrowseraction)