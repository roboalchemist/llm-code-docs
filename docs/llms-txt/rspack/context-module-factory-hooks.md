# Source: https://rspack.dev/api/plugin-api/context-module-factory-hooks.md

# ContextModuleFactory

The `ContextModuleFactory` module is used by the `Compiler` to generate dependencies from [require.context](/api/runtime-api/module-methods.md#requirecontext) API. It resolves the requested directory, generates requests for each file and filters against passed regExp. Matching dependencies then passes through [NormalModuleFactory](/api/plugin-api/normal-module-factory-hooks.md).

## `beforeResolve`

`AsyncSeriesBailHook<[BeforeResolveResult]>`

Called before resolving the requested directory. The request can be ignored by returning `false`.

BeforeResolveResult.ts
## `afterResolve`

`AsyncSeriesBailHook<[AfterResolveResult]>`

Called after the requested directory resolved.

AfterResolveResult.ts