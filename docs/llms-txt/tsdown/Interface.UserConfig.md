# Source: https://tsdown.dev/reference/api/Interface.UserConfig.md

---
url: /reference/api/Interface.UserConfig.md
---
# Interface: UserConfig

Defined in: [src/config/types.ts:140](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L140)

Options for tsdown.

## Extended by

* [`InlineConfig`](Interface.InlineConfig.md)

## Properties

### alias?

```ts
optional alias: Record<string, string>;
```

Defined in: [src/config/types.ts:178](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L178)

***

### attw?

```ts
optional attw: WithEnabled<AttwOptions>;
```

Defined in: [src/config/types.ts:529](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L529)

Run `arethetypeswrong` after bundling.
Requires `@arethetypeswrong/core` to be installed.

#### Default

```ts
false
```

#### See

https://github.com/arethetypeswrong/arethetypeswrong.github.io

***

### banner?

```ts
optional banner: ChunkAddon;
```

Defined in: [src/config/types.ts:370](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L370)

***

### ~~bundle?~~

```ts
optional bundle: boolean;
```

Defined in: [src/config/types.ts:393](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L393)

#### Deprecated

Use `unbundle` instead.

#### Default

```ts
true
```

***

### checks?

```ts
optional checks: ChecksOptions & object;
```

Defined in: [src/config/types.ts:303](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L303)

Controls which warnings are emitted during the build process. Each option can be set to `true` (emit warning) or `false` (suppress warning).

#### Type Declaration

##### legacyCjs?

```ts
optional legacyCjs: boolean;
```

If the config includes the `cjs` format and
one of its target >= node 20.19.0 / 22.12.0,
warn the user about the deprecation of CommonJS.

###### Default

```ts
true
```

***

### cjsDefault?

```ts
optional cjsDefault: boolean;
```

Defined in: [src/config/types.ts:419](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L419)

#### Default

```ts
true
```

***

### clean?

```ts
optional clean: boolean | string[];
```

Defined in: [src/config/types.ts:364](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L364)

Clean directories before build.

Default to output directory.

#### Default

```ts
true
```

***

### copy?

```ts
optional copy:
  | CopyOptions
  | CopyOptionsFn;
```

Defined in: [src/config/types.ts:581](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L581)

Copy files to another directory.

#### Example

```ts
;[
  'src/assets',
  'src/env.d.ts',
  'src/styles/**/*.css',
  { from: 'src/assets', to: 'dist/assets' },
  { from: 'src/styles/**/*.css', to: 'dist', flatten: true },
]
```

***

### css?

```ts
optional css: CssOptions;
```

Defined in: [src/config/types.ts:556](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L556)

**\[experimental]** CSS options.
Requires `@tsdown/css` to be installed.

***

### customLogger?

```ts
optional customLogger: Logger;
```

Defined in: [src/config/types.ts:461](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L461)

Custom logger.

***

### cwd?

```ts
optional cwd: string;
```

Defined in: [src/config/types.ts:439](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L439)

The working directory of the config file.

* Defaults to `process.cwd()` for root config.
* Defaults to the package directory for workspace config.

***

### define?

```ts
optional define: Record<string, string>;
```

Defined in: [src/config/types.ts:247](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L247)

***

### deps?

```ts
optional deps: DepsConfig;
```

Defined in: [src/config/types.ts:158](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L158)

Dependency handling options.

***

### devtools?

```ts
optional devtools: WithEnabled<DevtoolsOptions>;
```

Defined in: [src/config/types.ts:487](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L487)

**\[experimental]** Enable devtools.

DevTools is still under development, and this is for early testers only.

This may slow down the build process significantly.

#### Default

```ts
false
```

***

### dts?

```ts
optional dts: WithEnabled<DtsOptions>;
```

Defined in: [src/config/types.ts:506](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L506)

Enables generation of TypeScript declaration files (`.d.ts`).

By default, this option is auto-detected based on your project's `package.json`:

* If [exe](#exe) is enabled, declaration file generation is disabled by default.
* If the `types` field is present, or if the main `exports` contains a `types` entry, declaration file generation is enabled by default.
* Otherwise, declaration file generation is disabled by default.

***

### entry?

```ts
optional entry: TsdownInputOption;
```

Defined in: [src/config/types.ts:153](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L153)

Defaults to `'src/index.ts'` if it exists.

Supports glob patterns with negation to exclude files:

#### Example

```ts
entry: {
  "hooks/*": ["./src/hooks/*.ts", "!./src/hooks/index.ts"],
}
```

***

### env?

```ts
optional env: Record<string, any>;
```

Defined in: [src/config/types.ts:235](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L235)

Compile-time env variables, which can be accessed via `import.meta.env` or `process.env`.

#### Example

```json
{
  "DEBUG": true,
  "NODE_ENV": "production"
}
```

***

### envFile?

```ts
optional envFile: string;
```

Defined in: [src/config/types.ts:241](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L241)

Path to env file providing compile-time env variables.

#### Example

```ts
`.env`, `.env.production`, etc.
```

***

### envPrefix?

```ts
optional envPrefix: string | string[];
```

Defined in: [src/config/types.ts:246](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L246)

When loading env variables from `envFile`, only include variables with these prefixes.

#### Default

```ts
'TSDOWN_'
```

***

### exe?

```ts
optional exe: WithEnabled<ExeOptions>;
```

Defined in: [src/config/types.ts:593](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L593)

**\[experimental]** Bundle as executable using Node.js SEA (Single Executable Applications).

This will bundle the output into a single executable file using Node.js SEA.
Note that this is only supported on Node.js 25.7.0 and later, and is not supported in Bun or Deno.

***

### exports?

```ts
optional exports: WithEnabled<ExportsOptions>;
```

Defined in: [src/config/types.ts:550](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L550)

Generate package exports for `package.json`.

This will set the `main`, `module`, `types`, `exports` fields in `package.json`
to point to the generated files.

***

### ~~external?~~

```ts
optional external: string | RegExp | (string | RegExp)[] | ExternalOptionFunction;
```

Defined in: [src/config/types.ts:163](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L163)

#### Deprecated

Use `deps.neverBundle` instead.

***

### failOnWarn?

```ts
optional failOnWarn: boolean | CIOption;
```

Defined in: [src/config/types.ts:457](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L457)

If true, fails the build on warnings.

#### Default

```ts
false
```

***

### fixedExtension?

```ts
optional fixedExtension: boolean;
```

Defined in: [src/config/types.ts:402](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L402)

Use a fixed extension for output files.
The extension will always be `.cjs` or `.mjs`.
Otherwise, it will depend on the package type.

Defaults to `true` if `platform` is set to `node`, `false` otherwise.

***

### footer?

```ts
optional footer: ChunkAddon;
```

Defined in: [src/config/types.ts:369](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L369)

***

### format?

```ts
optional format:
  | "es" | "cjs" | "iife" | "umd" | "commonjs" | "module" | "esm"
  | ("es" | "cjs" | "iife" | "umd" | "commonjs" | "module" | "esm")[]
| Partial<Record<"es" | "cjs" | "iife" | "umd" | "commonjs" | "module" | "esm", Partial<ResolvedConfig>>>;
```

Defined in: [src/config/types.ts:338](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L338)

Output format(s). Available formats are

* `esm`: ESM
* `cjs`: CommonJS
* `iife`: IIFE
* `umd`: UMD

Defaults to ESM.

***

### fromVite?

```ts
optional fromVite: boolean | "vitest";
```

Defined in: [src/config/types.ts:467](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L467)

Reuse config from Vite or Vitest (experimental)

#### Default

```ts
false
```

***

### globalName?

```ts
optional globalName: string;
```

Defined in: [src/config/types.ts:339](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L339)

***

### globImport?

```ts
optional globImport: boolean;
```

Defined in: [src/config/types.ts:542](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L542)

`import.meta.glob` support.

#### See

https://vite.dev/guide/features.html#glob-import

#### Default

```ts
true
```

***

### hash?

```ts
optional hash: boolean;
```

Defined in: [src/config/types.ts:414](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L414)

If enabled, appends hash to chunk filenames.

#### Default

```ts
true
```

***

### hooks?

```ts
optional hooks:
  | Partial<TsdownHooks>
| (hooks) => Awaitable<void>;
```

Defined in: [src/config/types.ts:583](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L583)

***

### ignoreWatch?

```ts
optional ignoreWatch: Arrayable<string | RegExp>;
```

Defined in: [src/config/types.ts:476](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L476)

Files or patterns to not watch while in watch mode.

***

### ~~injectStyle?~~

```ts
optional injectStyle: boolean;
```

Defined in: [src/config/types.ts:561](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L561)

#### Deprecated

Use `css.inject` instead.

***

### ~~inlineOnly?~~

```ts
optional inlineOnly: false | Arrayable<string | RegExp>;
```

Defined in: [src/config/types.ts:171](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L171)

#### Deprecated

Use `deps.onlyBundle` instead.

***

### inputOptions?

```ts
optional inputOptions:
  | InputOptions
| (options, format, context) => Awaitable<void | InputOptions | null>;
```

Defined in: [src/config/types.ts:319](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L319)

Use with caution; ensure you understand the implications.

***

### loader?

```ts
optional loader: ModuleTypes;
```

Defined in: [src/config/types.ts:268](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L268)

Sets how input files are processed.
For example, use 'js' to treat files as JavaScript or 'base64' for images.
Lets you import or require files like images or fonts.

#### Example

```json
{ ".jpg": "asset", ".png": "base64" }
```

***

### logLevel?

```ts
optional logLevel: LogLevel;
```

Defined in: [src/config/types.ts:452](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L452)

Log level.

#### Default

```ts
'info'
```

***

### minify?

```ts
optional minify: boolean | "dce-only" | MinifyOptions;
```

Defined in: [src/config/types.ts:368](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L368)

#### Default

```ts
false
```

***

### name?

```ts
optional name: string;
```

Defined in: [src/config/types.ts:446](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L446)

The name to show in CLI output. This is useful for monorepos or workspaces.
When using workspace mode, this option defaults to the package name from package.json.
In non-workspace mode, this option must be set explicitly for the name to show in the CLI output.

***

### nodeProtocol?

```ts
optional nodeProtocol: boolean | "strip";
```

Defined in: [src/config/types.ts:298](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L298)

* If `true`, add `node:` prefix to built-in modules.
* If `'strip'`, strips the `node:` protocol prefix from import source.
* If `false`, does not modify the import source.

#### Default

```ts
false
```

#### Example

```ts
// With nodeProtocol enabled:
import('fs') // becomes import('node:fs')
// With nodeProtocol set to 'strip':
import('node:fs') // becomes import('fs')
// With nodeProtocol set to false:
import('node:fs') // remains import('node:fs')
```

***

### ~~noExternal?~~

```ts
optional noExternal:
  | Arrayable<string | RegExp>
  | NoExternalFn;
```

Defined in: [src/config/types.ts:167](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L167)

#### Deprecated

Use `deps.alwaysBundle` instead.

***

### onSuccess?

```ts
optional onSuccess: string | (config, signal) => void | Promise<void>;
```

Defined in: [src/config/types.ts:494](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L494)

You can specify command to be executed after a successful build, specially useful for Watch mode

***

### outDir?

```ts
optional outDir: string;
```

Defined in: [src/config/types.ts:341](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L341)

#### Default

```ts
'dist'
```

***

### outExtensions?

```ts
optional outExtensions: OutExtensionFactory;
```

Defined in: [src/config/types.ts:408](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L408)

Custom extensions for output files.
`fixedExtension` will be overridden by this option.

***

### outputOptions?

```ts
optional outputOptions:
  | OutputOptions
| (options, format, context) => Awaitable<void | OutputOptions | null>;
```

Defined in: [src/config/types.ts:424](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L424)

Use with caution; ensure you understand the implications.

***

### platform?

```ts
optional platform: "node" | "neutral" | "browser";
```

Defined in: [src/config/types.ts:192](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L192)

Specifies the target runtime platform for the build.

* `node`: Node.js and compatible runtimes (e.g., Deno, Bun).
  For CJS format, this is always set to `node` and cannot be changed.
* `neutral`: A platform-agnostic target with no specific runtime assumptions.
* `browser`: Web browsers.

#### Default

```ts
'node'
```

#### See

https://tsdown.dev/options/platform

***

### plugins?

```ts
optional plugins: RolldownPluginOption<any>;
```

Defined in: [src/config/types.ts:314](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L314)

***

### ~~publicDir?~~

```ts
optional publicDir:
  | CopyOptions
  | CopyOptionsFn;
```

Defined in: [src/config/types.ts:566](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L566)

#### Deprecated

Alias for `copy`, will be removed in the future.

***

### publint?

```ts
optional publint: WithEnabled<PublintOptions>;
```

Defined in: [src/config/types.ts:520](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L520)

Run publint after bundling.
Requires `publint` to be installed.

#### Default

```ts
false
```

***

### ~~removeNodeProtocol?~~

```ts
optional removeNodeProtocol: boolean;
```

Defined in: [src/config/types.ts:280](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L280)

If enabled, strips the `node:` protocol prefix from import source.

#### Default

```ts
false
```

#### Deprecated

Use `nodeProtocol: 'strip'` instead.

#### Example

```ts
// With removeNodeProtocol enabled:
import('node:fs') // becomes import('fs')
```

***

### report?

```ts
optional report: WithEnabled<ReportOptions>;
```

Defined in: [src/config/types.ts:535](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L535)

Enable size reporting after bundling.

#### Default

```ts
true
```

***

### root?

```ts
optional root: string;
```

Defined in: [src/config/types.ts:387](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L387)

Specifies the root directory of input files, similar to TypeScript's `rootDir`.
This determines the output directory structure.

By default, the root is computed as the common base directory of all entry files.

#### See

https://www.typescriptlang.org/tsconfig/#rootDir

***

### shims?

```ts
optional shims: boolean;
```

Defined in: [src/config/types.ts:250](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L250)

#### Default

```ts
false
```

***

### ~~skipNodeModulesBundle?~~

```ts
optional skipNodeModulesBundle: boolean;
```

Defined in: [src/config/types.ts:176](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L176)

#### Deprecated

Use `deps.skipNodeModulesBundle` instead.

#### Default

```ts
false
```

***

### sourcemap?

```ts
optional sourcemap: Sourcemap;
```

Defined in: [src/config/types.ts:357](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L357)

Whether to generate source map files.

Note that this option will always be `true` if you have
[`declarationMap`](https://www.typescriptlang.org/tsconfig/#declarationMap)
option enabled in your `tsconfig.json`.

#### Default

```ts
false
```

***

### target?

```ts
optional target: string | false | string[];
```

Defined in: [src/config/types.ts:223](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L223)

Specifies the compilation target environment(s).

Determines the JavaScript version or runtime(s) for which the code should be compiled.
If not set, defaults to the value of `engines.node` in your project's `package.json`.
If no `engines.node` field exists, no syntax transformations are applied.

Accepts a single target (e.g., `'es2020'`, `'node18'`), an array of targets, or `false` to disable all transformations.

#### See

<https://tsdown.dev/options/target#supported-targets> for a list of valid targets and more details.

#### Examples

```jsonc
// Target a single environment
{ "target": "node18" }
```

```jsonc
// Target multiple environments
{ "target": ["node18", "es2020"] }
```

```jsonc
// Disable all syntax transformations
{ "target": false }
```

***

### treeshake?

```ts
optional treeshake: boolean | TreeshakingOptions;
```

Defined in: [src/config/types.ts:257](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L257)

Configure tree shaking options.

#### See

<https://rolldown.rs/options/treeshake> for more details.

#### Default

```ts
true
```

***

### tsconfig?

```ts
optional tsconfig: string | boolean;
```

Defined in: [src/config/types.ts:179](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L179)

***

### unbundle?

```ts
optional unbundle: boolean;
```

Defined in: [src/config/types.ts:377](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L377)

Determines whether unbundle mode is enabled.
When set to true, the output files will mirror the input file structure.

#### Default

```ts
false
```

***

### unused?

```ts
optional unused: WithEnabled<UnusedOptions>;
```

Defined in: [src/config/types.ts:513](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L513)

Enable unused dependencies check with `unplugin-unused`
Requires `unplugin-unused` to be installed.

#### Default

```ts
false
```

***

### watch?

```ts
optional watch: boolean | Arrayable<string>;
```

Defined in: [src/config/types.ts:472](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L472)

#### Default

```ts
false
```

***

### workspace?

```ts
optional workspace: true | Arrayable<string> | Workspace;
```

Defined in: [src/config/types.ts:599](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L599)

**\[experimental]** Enable workspace mode.
This allows you to build multiple packages in a monorepo.

***

### write?

```ts
optional write: boolean;
```

Defined in: [src/config/types.ts:347](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L347)

Whether to write the files to disk.
This option is incompatible with watch mode.

#### Default

```ts
true
```
