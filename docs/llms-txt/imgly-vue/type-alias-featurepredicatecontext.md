# Type Alias: FeaturePredicateContext

```
type FeaturePredicateContext = IsEnabledFeatureContext & object;
```

Represents the context for enabling a feature. This type extends `IsEnabledFeatureContext` and includes a function to check the previous enable state and a function to get the default predicate.

## Type declaration[#](#type-declaration)

| Name | Type |
| --- | --- |
| `isPreviousEnable()` | () => `boolean` |
| `defaultPredicate()` | () => `boolean` |

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/featurepredicate)