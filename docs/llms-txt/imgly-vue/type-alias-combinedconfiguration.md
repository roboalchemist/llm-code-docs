# Type Alias: CombinedConfiguration

```
type CombinedConfiguration = CESDKConfiguration & Omit<_EngineConfiguration, "presets"> & DeprecatedKeys;
```

Represents the combined configuration for the Creative Editor SDK. This type combines the `CESDKConfiguration` with the `EngineConfiguration` while omitting the `presets` key. It also includes deprecated keys from the `CESDKConfiguration`.

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/callbacks)