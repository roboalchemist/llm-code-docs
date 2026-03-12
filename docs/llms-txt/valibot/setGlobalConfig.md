# Source: https://valibot.dev/api/setGlobalConfig.md

# setGlobalConfig

Sets the global configuration.

```ts
v.setGlobalConfig(merge);
```

## Parameters

- `config` <Property {...properties.config} />

### Explanation

The properties specified by `config` are merged with the existing global configuration. If a property is already set, it will be overwritten.
