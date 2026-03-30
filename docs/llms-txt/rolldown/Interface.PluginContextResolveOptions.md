# Source: https://rolldown.rs/reference/Interface.PluginContextResolveOptions.md

---
url: /reference/Interface.PluginContextResolveOptions.md
---
# Interface: PluginContextResolveOptions

## Properties

### custom?

* **Type**: [`CustomPluginOptions`](Interface.CustomPluginOptions.md)
* **Optional**

Plugin-specific options.

See [Custom resolver options section](/apis/plugin-api/inter-plugin-communication#custom-resolver-options) for more details.

***

### isEntry?

* **Type**: `boolean`
* **Optional**

The value for [`isEntry`](Interface.ResolveIdExtraOptions.md#isentry) passed to
[`resolveId`](Interface.Plugin.md#resolveid) hooks.

#### Default

`false` if there's an importer, `true` otherwise.

***

### kind?

* **Type**: `"import-statement"` | `"dynamic-import"` | `"require-call"` | `"import-rule"` | `"url-token"` | `"new-url"` | `"hot-accept"`
* **Optional**

The value for [`kind`](Interface.ResolveIdExtraOptions.md#kind) passed to
[`resolveId`](Interface.Plugin.md#resolveid) hooks.

***

### skipSelf?

* **Type**: `boolean`
* **Optional**

Whether the [`resolveId`](Interface.Plugin.md#resolveid) hook of the plugin from
which [`this.resolve`](Interface.PluginContext.md#resolve) is called will be skipped
when resolving.

When other plugins themselves also call `this.resolve` in their `resolveId` hooks with the exact same `source` and `importer` while handling the original `this.resolve` call, then the `resolveId` hook of the original plugin will be skipped for those calls as well. The rationale here is that the plugin already stated that it "does not know" how to resolve this particular combination of source and importer at this point in time. If you do not want this behavior, set `skipSelf` to `false` and implement your own infinite loop prevention mechanism if necessary.

#### Default

```ts
true
```
