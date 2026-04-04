# Source: https://tsdown.dev/reference/api/Interface.AttwOptions.md

---
url: /reference/api/Interface.AttwOptions.md
---
# Interface: AttwOptions

Defined in: [src/features/pkg/attw.ts:31](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/pkg/attw.ts#L31)

## Extends

* `CheckPackageOptions`

## Properties

### entrypoints?

```ts
optional entrypoints: string[];
```

Defined in: node\_modules/.pnpm/@arethetypeswrong+core@0.18.2/node\_modules/@arethetypeswrong/core/dist/checkPackage.d.ts:9

Exhaustive list of entrypoints to check. The package root is `"."`.
Specifying this option disables automatic entrypoint discovery,
and overrides the `includeEntrypoints` and `excludeEntrypoints` options.

#### Inherited from

```ts
CheckPackageOptions.entrypoints
```

***

### entrypointsLegacy?

```ts
optional entrypointsLegacy: boolean;
```

Defined in: node\_modules/.pnpm/@arethetypeswrong+core@0.18.2/node\_modules/@arethetypeswrong/core/dist/checkPackage.d.ts:22

Whether to automatically consider all published files as entrypoints
in the absence of any other detected or configured entrypoints.

#### Inherited from

```ts
CheckPackageOptions.entrypointsLegacy
```

***

### excludeEntrypoints?

```ts
optional excludeEntrypoints: (string | RegExp)[];
```

Defined in: node\_modules/.pnpm/@arethetypeswrong+core@0.18.2/node\_modules/@arethetypeswrong/core/dist/checkPackage.d.ts:17

Entrypoints to exclude from checking.

#### Inherited from

```ts
CheckPackageOptions.excludeEntrypoints
```

***

### ignoreRules?

```ts
optional ignoreRules: string[];
```

Defined in: [src/features/pkg/attw.ts:80](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/pkg/attw.ts#L80)

List of problem types to ignore by rule name.

The available values are:

* `no-resolution`
* `untyped-resolution`
* `false-cjs`
* `false-esm`
* `cjs-resolves-to-esm`
* `fallback-condition`
* `cjs-only-exports-default`
* `named-exports`
* `false-export-default`
* `missing-export-equals`
* `unexpected-module-syntax`
* `internal-resolution-error`

#### Example

```ts
ignoreRules: ['no-resolution', 'false-cjs']
```

***

### includeEntrypoints?

```ts
optional includeEntrypoints: string[];
```

Defined in: node\_modules/.pnpm/@arethetypeswrong+core@0.18.2/node\_modules/@arethetypeswrong/core/dist/checkPackage.d.ts:13

Entrypoints to check in addition to automatically discovered ones.

#### Inherited from

```ts
CheckPackageOptions.includeEntrypoints
```

***

### level?

```ts
optional level: "error" | "warn";
```

Defined in: [src/features/pkg/attw.ts:56](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/pkg/attw.ts#L56)

The level of the check.

The available levels are:

* `error`: fails the build
* `warn`: warns the build

#### Default

```ts
'warn'
```

***

### profile?

```ts
optional profile: "strict" | "node16" | "esm-only";
```

Defined in: [src/features/pkg/attw.ts:46](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/pkg/attw.ts#L46)

Profiles select a set of resolution modes to require/ignore. All are evaluated but failures outside
of those required are ignored.

The available profiles are:

* `strict`: requires all resolutions
* `node16`: ignores node10 resolution failures
* `esm-only`: ignores CJS resolution failures

#### Default

```ts
'strict'
```
