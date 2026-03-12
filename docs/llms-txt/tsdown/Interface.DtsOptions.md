# Source: https://tsdown.dev/reference/api/Interface.DtsOptions.md

---
url: /reference/api/Interface.DtsOptions.md
---
# Interface: DtsOptions

Defined in: node\_modules/.pnpm/rolldown-plugin-dts@0.22.5\_@typescript+native-preview@7.0.0-dev.20260311.1\_rolldown@1.0\_78faf893e434ce5b3a5dd8c603cf305e/node\_modules/rolldown-plugin-dts/dist/index.d.mts:154

## Extends

* `GeneralOptions`.`TscOptions`

## Properties

### build?

```ts
optional build: boolean;
```

Defined in: node\_modules/.pnpm/rolldown-plugin-dts@0.22.5\_@typescript+native-preview@7.0.0-dev.20260311.1\_rolldown@1.0\_78faf893e434ce5b3a5dd8c603cf305e/node\_modules/rolldown-plugin-dts/dist/index.d.mts:83

Build mode for the TypeScript compiler:

* If `true`, the plugin will use [`tsc -b`](https://www.typescriptlang.org/docs/handbook/project-references.html#build-mode-for-typescript) to build the project and all referenced projects before emitting `.d.ts` files.
* If `false`, the plugin will use [`tsc`](https://www.typescriptlang.org/docs/handbook/compiler-options.html) to emit `.d.ts` files without building referenced projects.

#### Default

```ts
false
```

#### Inherited from

```ts
TscOptions.build
```

***

### cjsDefault?

```ts
optional cjsDefault: boolean;
```

Defined in: node\_modules/.pnpm/rolldown-plugin-dts@0.22.5\_@typescript+native-preview@7.0.0-dev.20260311.1\_rolldown@1.0\_78faf893e434ce5b3a5dd8c603cf305e/node\_modules/rolldown-plugin-dts/dist/index.d.mts:64

Determines how the default export is emitted.

If set to `true`, and you are only exporting a single item using `export default ...`,
the output will use `export = ...` instead of the standard ES module syntax.
This is useful for compatibility with CommonJS.

#### Inherited from

```ts
GeneralOptions.cjsDefault
```

***

### compilerOptions?

```ts
optional compilerOptions: CompilerOptions;
```

Defined in: node\_modules/.pnpm/rolldown-plugin-dts@0.22.5\_@typescript+native-preview@7.0.0-dev.20260311.1\_rolldown@1.0\_78faf893e434ce5b3a5dd8c603cf305e/node\_modules/rolldown-plugin-dts/dist/index.d.mts:43

Override the `compilerOptions` specified in `tsconfig.json`.

#### See

https://www.typescriptlang.org/tsconfig/#compilerOptions

#### Inherited from

```ts
GeneralOptions.compilerOptions
```

***

### cwd?

```ts
optional cwd: string;
```

Defined in: node\_modules/.pnpm/rolldown-plugin-dts@0.22.5\_@typescript+native-preview@7.0.0-dev.20260311.1\_rolldown@1.0\_78faf893e434ce5b3a5dd8c603cf305e/node\_modules/rolldown-plugin-dts/dist/index.d.mts:10

The directory in which the plugin will search for the `tsconfig.json` file.

#### Inherited from

```ts
GeneralOptions.cwd
```

***

### dtsInput?

```ts
optional dtsInput: boolean;
```

Defined in: node\_modules/.pnpm/rolldown-plugin-dts@0.22.5\_@typescript+native-preview@7.0.0-dev.20260311.1\_rolldown@1.0\_78faf893e434ce5b3a5dd8c603cf305e/node\_modules/rolldown-plugin-dts/dist/index.d.mts:16

Set to `true` if your entry files are `.d.ts` files instead of `.ts` files.

When enabled, the plugin will skip generating a `.d.ts` file for the entry point.

#### Inherited from

```ts
GeneralOptions.dtsInput
```

***

### eager?

```ts
optional eager: boolean;
```

Defined in: node\_modules/.pnpm/rolldown-plugin-dts@0.22.5\_@typescript+native-preview@7.0.0-dev.20260311.1\_rolldown@1.0\_78faf893e434ce5b3a5dd8c603cf305e/node\_modules/rolldown-plugin-dts/dist/index.d.mts:132

If `true`, the plugin will prepare all files listed in `tsconfig.json` for `tsc` or `vue-tsc`.

This is especially useful when you have a single `tsconfig.json` for multiple projects in a monorepo.

#### Inherited from

```ts
TscOptions.eager
```

***

### emitDtsOnly?

```ts
optional emitDtsOnly: boolean;
```

Defined in: node\_modules/.pnpm/rolldown-plugin-dts@0.22.5\_@typescript+native-preview@7.0.0-dev.20260311.1\_rolldown@1.0\_78faf893e434ce5b3a5dd8c603cf305e/node\_modules/rolldown-plugin-dts/dist/index.d.mts:22

If `true`, the plugin will emit only `.d.ts` files and remove all other output chunks.

This is especially useful when generating `.d.ts` files for the CommonJS format as part of a separate build step.

#### Inherited from

```ts
GeneralOptions.emitDtsOnly
```

***

### emitJs?

```ts
optional emitJs: boolean;
```

Defined in: node\_modules/.pnpm/rolldown-plugin-dts@0.22.5\_@typescript+native-preview@7.0.0-dev.20260311.1\_rolldown@1.0\_78faf893e434ce5b3a5dd8c603cf305e/node\_modules/rolldown-plugin-dts/dist/index.d.mts:152

If `true`, the plugin will emit `.d.ts` files for `.js` files as well.
This is useful when you want to generate type definitions for JavaScript files with JSDoc comments.

Enabled by default when `allowJs` in compilerOptions is `true`.
This option is only used when [Options.oxc](#oxc) is
`false`.

#### Inherited from

```ts
TscOptions.emitJs
```

***

### incremental?

```ts
optional incremental: boolean;
```

Defined in: node\_modules/.pnpm/rolldown-plugin-dts@0.22.5\_@typescript+native-preview@7.0.0-dev.20260311.1\_rolldown@1.0\_78faf893e434ce5b3a5dd8c603cf305e/node\_modules/rolldown-plugin-dts/dist/index.d.mts:113

If your tsconfig.json has
[`references`](https://www.typescriptlang.org/tsconfig/#references) option,
`rolldown-plugin-dts` will use [`tsc
-b`](https://www.typescriptlang.org/docs/handbook/project-references.html#build-mode-for-typescript)
to build the project and all referenced projects before emitting `.d.ts`
files.

In such case, if this option is `true`, `rolldown-plugin-dts` will write
down all built files into your disk, including
[`.tsbuildinfo`](https://www.typescriptlang.org/tsconfig/#tsBuildInfoFile)
and other built files. This is equivalent to running `tsc -b` in your
project.

Otherwise, if this option is `false`, `rolldown-plugin-dts` will write
built files only into memory and leave a small footprint in your disk.

Enabling this option will decrease the build time by caching previous build
results. This is helpful when you have a large project with multiple
referenced projects.

By default, `incremental` is `true` if your tsconfig has
[`incremental`](https://www.typescriptlang.org/tsconfig/#incremental) or
[`tsBuildInfoFile`](https://www.typescriptlang.org/tsconfig/#tsBuildInfoFile)
enabled.

This option is only used when [Options.oxc](#oxc) is
`false`.

#### Inherited from

```ts
TscOptions.incremental
```

***

### newContext?

```ts
optional newContext: boolean;
```

Defined in: node\_modules/.pnpm/rolldown-plugin-dts@0.22.5\_@typescript+native-preview@7.0.0-dev.20260311.1\_rolldown@1.0\_78faf893e434ce5b3a5dd8c603cf305e/node\_modules/rolldown-plugin-dts/dist/index.d.mts:143

If `true`, the plugin will create a new isolated context for each build,
ensuring that previously generated `.d.ts` code and caches are not reused.

By default, the plugin may reuse internal caches or incremental build artifacts
to speed up repeated builds. Enabling this option forces a clean context,
guaranteeing that all type definitions are generated from scratch.

#### Default

```ts
false
```

#### Inherited from

```ts
TscOptions.newContext
```

***

### oxc?

```ts
optional oxc: boolean | Omit<IsolatedDeclarationsOptions, "sourcemap">;
```

Defined in: node\_modules/.pnpm/rolldown-plugin-dts@0.22.5\_@typescript+native-preview@7.0.0-dev.20260311.1\_rolldown@1.0\_78faf893e434ce5b3a5dd8c603cf305e/node\_modules/rolldown-plugin-dts/dist/index.d.mts:161

If `true`, the plugin will generate `.d.ts` files using Oxc,
which is significantly faster than the TypeScript compiler.

This option is automatically enabled when `isolatedDeclarations` in `compilerOptions` is set to `true`.

***

### parallel?

```ts
optional parallel: boolean;
```

Defined in: node\_modules/.pnpm/rolldown-plugin-dts@0.22.5\_@typescript+native-preview@7.0.0-dev.20260311.1\_rolldown@1.0\_78faf893e434ce5b3a5dd8c603cf305e/node\_modules/rolldown-plugin-dts/dist/index.d.mts:126

If `true`, the plugin will launch a separate process for `tsc` or `vue-tsc`.
This enables processing multiple projects in parallel.

#### Inherited from

```ts
TscOptions.parallel
```

***

### resolver?

```ts
optional resolver: "oxc" | "tsc";
```

Defined in: node\_modules/.pnpm/rolldown-plugin-dts@0.22.5\_@typescript+native-preview@7.0.0-dev.20260311.1\_rolldown@1.0\_78faf893e434ce5b3a5dd8c603cf305e/node\_modules/rolldown-plugin-dts/dist/index.d.mts:56

Specifies a resolver to resolve type definitions, especially for `node_modules`.

* `'oxc'`: Uses Oxc's module resolution, which is faster and more efficient.
* `'tsc'`: Uses TypeScript's native module resolution, which may be more compatible with complex setups, but slower.

#### Default

```ts
'oxc'
```

#### Inherited from

```ts
GeneralOptions.resolver
```

***

### sideEffects?

```ts
optional sideEffects: boolean;
```

Defined in: node\_modules/.pnpm/rolldown-plugin-dts@0.22.5\_@typescript+native-preview@7.0.0-dev.20260311.1\_rolldown@1.0\_78faf893e434ce5b3a5dd8c603cf305e/node\_modules/rolldown-plugin-dts/dist/index.d.mts:72

Indicates whether the generated `.d.ts` files have side effects.

* If set to `true`, Rolldown will treat the `.d.ts` files as having side effects during tree-shaking.
* If set to `false`, Rolldown may consider the `.d.ts` files as side-effect-free, potentially removing them if they are not imported.

#### Default

```ts
false
```

#### Inherited from

```ts
GeneralOptions.sideEffects
```

***

### sourcemap?

```ts
optional sourcemap: boolean;
```

Defined in: node\_modules/.pnpm/rolldown-plugin-dts@0.22.5\_@typescript+native-preview@7.0.0-dev.20260311.1\_rolldown@1.0\_78faf893e434ce5b3a5dd8c603cf305e/node\_modules/rolldown-plugin-dts/dist/index.d.mts:47

If `true`, the plugin will generate declaration maps (`.d.ts.map`) for `.d.ts` files.

#### Inherited from

```ts
GeneralOptions.sourcemap
```

***

### tsconfig?

```ts
optional tsconfig: string | boolean;
```

Defined in: node\_modules/.pnpm/rolldown-plugin-dts@0.22.5\_@typescript+native-preview@7.0.0-dev.20260311.1\_rolldown@1.0\_78faf893e434ce5b3a5dd8c603cf305e/node\_modules/rolldown-plugin-dts/dist/index.d.mts:31

The path to the `tsconfig.json` file.

If set to `false`, the plugin will ignore any `tsconfig.json` file.
You can still specify `compilerOptions` directly in the options.

#### Default

```ts
'tsconfig.json'
```

#### Inherited from

```ts
GeneralOptions.tsconfig
```

***

### tsconfigRaw?

```ts
optional tsconfigRaw: Omit<TsConfigJson, "compilerOptions">;
```

Defined in: node\_modules/.pnpm/rolldown-plugin-dts@0.22.5\_@typescript+native-preview@7.0.0-dev.20260311.1\_rolldown@1.0\_78faf893e434ce5b3a5dd8c603cf305e/node\_modules/rolldown-plugin-dts/dist/index.d.mts:37

Pass a raw `tsconfig.json` object directly to the plugin.

#### See

https://www.typescriptlang.org/tsconfig

#### Inherited from

```ts
GeneralOptions.tsconfigRaw
```

***

### tsgo?

```ts
optional tsgo: boolean | TsgoOptions;
```

Defined in: node\_modules/.pnpm/rolldown-plugin-dts@0.22.5\_@typescript+native-preview@7.0.0-dev.20260311.1\_rolldown@1.0\_78faf893e434ce5b3a5dd8c603cf305e/node\_modules/rolldown-plugin-dts/dist/index.d.mts:180

**\[Experimental]** Enables DTS generation using `tsgo`.

To use this option, make sure `@typescript/native-preview` is installed as a dependency,
or provide a custom path to the `tsgo` binary using the `path` option.

**Note:** This option is not yet recommended for production environments.
`tsconfigRaw` and `isolatedDeclarations` options will be ignored when this option is enabled.

```ts
// Use tsgo from `@typescript/native-preview` dependency
tsgo: true

// Use custom tsgo path (e.g., managed by Nix)
tsgo: {
  path: '/path/to/tsgo'
}
```

***

### tsMacro?

```ts
optional tsMacro: boolean;
```

Defined in: node\_modules/.pnpm/rolldown-plugin-dts@0.22.5\_@typescript+native-preview@7.0.0-dev.20260311.1\_rolldown@1.0\_78faf893e434ce5b3a5dd8c603cf305e/node\_modules/rolldown-plugin-dts/dist/index.d.mts:121

If `true`, the plugin will generate `.d.ts` files using `@ts-macro/tsc`.

#### Inherited from

```ts
TscOptions.tsMacro
```

***

### vue?

```ts
optional vue: boolean;
```

Defined in: node\_modules/.pnpm/rolldown-plugin-dts@0.22.5\_@typescript+native-preview@7.0.0-dev.20260311.1\_rolldown@1.0\_78faf893e434ce5b3a5dd8c603cf305e/node\_modules/rolldown-plugin-dts/dist/index.d.mts:117

If `true`, the plugin will generate `.d.ts` files using `vue-tsc`.

#### Inherited from

```ts
TscOptions.vue
```
