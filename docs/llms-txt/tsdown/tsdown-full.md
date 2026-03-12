# Tsdown Documentation

Source: https://tsdown.dev/llms-full.txt

---

---
url: /options/package-exports.md
---
# Auto-Generating Package Exports

`tsdown` provides an experimental feature to automatically infer and generate the `exports`, `main`, `module`, and `types` fields in your `package.json`. This helps ensure your package exports are always up-to-date and correctly reflect your build outputs.

## Enabling Auto Exports

You can enable this feature by setting the `exports: true` option in your `tsdown` configuration file:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  exports: true,
})
```

This will automatically analyze your entry points and output files, and update your `package.json` accordingly.

> \[!WARNING]
> Please review the generated fields before publishing your package, or enable publint for validation.

## Exporting All Files

By default, only entry files are exported. If you want to export all files (including those not listed as entry points), you can enable the `exports.all` option:

```ts
export default defineConfig({
  exports: {
    all: true,
  },
})
```

This will include all relevant files in the generated `exports` field.

## Dev-Time Source Linking

### Dev Exports {#dev-exports}

During development, you may want your `exports` to point directly to your source files for better debugging and editor support. You can enable this by setting `exports.devExports` to `true`:

```ts
export default defineConfig({
  exports: {
    devExports: true,
  },
})
```

With this setting, the generated `exports` in your `package.json` will link to your source code. The exports for the built output will be written to `publishConfig`, which will override the top-level `exports` field when using `yarn` or `pnpm`'s `pack`/`publish` commands (note: this is **not supported by npm**).

### Conditional Dev Exports

You can also set `exports.devExports` to a string to only link to source code under a specific [condition](https://nodejs.org/api/packages.html#conditional-exports):

```ts
export default defineConfig({
  exports: {
    devExports: 'development',
  },
})
```

This is especially useful when combined with TypeScript's [`customConditions`](https://www.typescriptlang.org/tsconfig/#customConditions) option, allowing you to control which conditions use the source code.

## CSS Exports

When `css.splitting` is `false`, the bundled CSS file is automatically added to `exports`:

```ts
export default defineConfig({
  css: {
    splitting: false,
  },
  exports: true,
})
```

The CSS filename defaults to `style.css` and can be customized via `css.fileName`.

## Customizing Exports

If you need more control over the generated exports, you can provide an object or a custom function via `exports.customExports`:

```ts
export default defineConfig({
  exports: {
    customExports: {
      './foo': './foo.js',
    },
  },
})
```

```ts
export default defineConfig({
  exports: {
    customExports(pkg, context) {
      pkg['./foo'] = './foo.js'
      return pkg
    },
  },
})
```

---

---
url: /advanced/benchmark.md
---
# Benchmark

`tsdown` delivers exceptional performance compared to other popular bundlers. In most cases, it is approximately **2 times faster** than `tsup` for standard builds, and up to **8 times faster** when generating TypeScript declaration files.

For detailed comparisons and real-world results, see [bundler-benchmark](https://gugustinette.github.io/bundler-benchmark/).

---

---
url: /advanced/ci.md
---
# CI Environment Support

tsdown automatically detects CI environments and allows you to enable or disable specific features depending on whether the build runs locally or in CI.

## CI Detection

tsdown uses the [`is-in-ci`](https://www.npmjs.com/package/is-in-ci) package to detect CI environments. This covers all major CI providers including GitHub Actions, GitLab CI, Jenkins, CircleCI, Travis CI, and more.

## CI-Aware Options

Several options support CI-aware behavior through the `'ci-only'` and `'local-only'` values:

| Value          | Behavior                             |
| -------------- | ------------------------------------ |
| `true`         | Always enabled                       |
| `false`        | Always disabled                      |
| `'ci-only'`    | Enabled only in CI, disabled locally |
| `'local-only'` | Enabled only locally, disabled in CI |

### Supported Options

The following options accept CI-aware values:

* [`dts`](/options/dts) — TypeScript declaration file generation
* [`publint`](/options/lint) — Package lint validation
* [`attw`](/options/lint) — "Are the types wrong" validation
* `report` — Bundle size reporting
* [`exports`](/options/package-exports) — Auto-generate `package.json` exports
* `unused` — Unused dependency check
* `devtools` — DevTools integration
* `failOnWarn` — Fail on warnings (defaults to `false`)

### Basic Usage

Pass a CI option string directly:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  // Only generate declaration files locally (skip in CI for faster builds)
  dts: 'local-only',
  // Only run publint in CI
  publint: 'ci-only',
  // Fail on warnings in CI only
  failOnWarn: 'ci-only',
})
```

### Object Form

When an option takes a configuration object, you can set the `enabled` property to a CI-aware value:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  publint: {
    enabled: 'ci-only',
    level: 'error',
  },
  attw: {
    enabled: 'ci-only',
    profile: 'node16',
  },
})
```

## Config Function

The config function receives a `ci` boolean in its context, allowing dynamic configuration:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig((_, { ci }) => ({
  minify: ci,
  sourcemap: !ci,
}))
```

## Example: CI Pipeline

A typical CI-optimized configuration:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: 'src/index.ts',
  format: ['esm', 'cjs'],
  dts: true,
  // Fail on warnings in CI (opt-in)
  failOnWarn: 'ci-only',
  // Run package validators in CI
  publint: 'ci-only',
  attw: 'ci-only',
})
```

---

---
url: /options/cjs-default.md
---
# CJS Default Export

The `cjsDefault` option helps improve compatibility when generating CommonJS (CJS) modules. This option is **enabled by default**.

## How It Works

When your module has **only a single default export** and the output format is set to CJS, `tsdown` will automatically transform:

* `export default ...`
  into
  `module.exports = ...` in the generated JavaScript file.

For TypeScript declaration files (`.d.ts`), it will transform:

* `export default ...`
  into
  `export = ...`

This ensures that consumers using CommonJS require syntax (`require('your-module')`) will receive the default export directly, improving interoperability with tools and environments that expect this behavior.

## Example

**Source Module:**

```ts
// src/index.ts
export default function greet() {
  console.log('Hello, world!')
}
```

**Generated CJS Output:**

```js
// dist/index.cjs
function greet() {
  console.log('Hello, world!')
}
module.exports = greet
```

**Generated Declaration File:**

```ts
// dist/index.d.cts
declare function greet(): void
export = greet
```

---

---
url: /options/cleaning.md
---
# Cleaning

By default, `tsdown` will **clean the output directory** (`outDir`) before each build. This ensures that any files from previous builds are removed, preventing outdated or unused files from remaining in your output.

If you want to disable this behavior and keep existing files in the output directory, you can use the `--no-clean` option:

```bash
tsdown --no-clean
```

> \[!NOTE]
> By default, all files in the output directory will be removed before the build process begins. Make sure this behavior aligns with your project requirements to avoid accidentally deleting important files.

---

---
url: /reference/cli.md
---
# Command Line Interface

All CLI flags can also be set in the configuration file, which improves reusability and maintainability for complex projects. Conversely, any option can be overridden by CLI flags, even if not explicitly listed on this page. For more details, see the [Config File](../options/config-file.md) documentation.

## CLI Flag Patterns

The mapping between CLI flags and configuration options follows these rules:

* `--foo` sets `foo: true`
* `--no-foo` sets `foo: false`
* `--foo.bar` sets `foo: { bar: true }`
* `--format esm --format cjs` sets `format: ['esm', 'cjs']`

CLI flags support both camelCase and kebab-case. For example, `--outDir` and `--out-dir` are equivalent.

This flexible pattern allows you to easily control and override configuration options directly from the command line.

## `[...files]`

Specify entry files as command arguments. This is equivalent to setting the `entry` option in the configuration file. For example:

```bash
tsdown src/index.ts src/util.ts
```

This will bundle `src/index.ts` and `src/util.ts` as separate entry points. See the [Entry](../options/entry.md) documentation for more details.

## `-c, --config <filename>`

Specify a custom configuration file. Use this option to define the path to the configuration file you want to use.

See also [Config File](../options/config-file.md).

## `--config-loader <loader>`

Specifies which config loader to use.

See also [Config File](../options/config-file.md).

## `--no-config`

Disable loading a configuration file. This is useful if you want to rely solely on command-line options or default settings.

See also [Disabling the Config File](../options/config-file.md#disable-config-file).

## `--tsconfig <tsconfig>`

Specify the path or filename of your `tsconfig` file. `tsdown` will search upwards from the current directory to find the specified file. By default, it uses `tsconfig.json`.

```bash
tsdown --tsconfig tsconfig.build.json
```

## `--format <format>`

Define the bundle format. Supported formats include:

* `esm` (ECMAScript Modules)
* `cjs` (CommonJS)
* `iife` (Immediately Invoked Function Expression)
* `umd` (Universal Module Definition)

See also [Output Format](../options/output-format.md).

## `--clean`

Clean the output directory before building. This removes all files in the output directory to ensure a fresh build.

See also [Cleaning](../options/cleaning.md).

## `--deps.never-bundle <module>`

Mark a module as external. This prevents the specified module from being included in the bundle.

See also [Dependencies](../options/dependencies.md).

## `--deps.skip-node-modules-bundle`

Skip resolving and bundling all dependencies from `node_modules`.

See also [Dependencies](../options/dependencies.md).

## `--external <module>` {#external}

::: warning Deprecated
Use `--deps.never-bundle` instead.
:::

Alias for `--deps.never-bundle`.

## `--minify`

Enable minification of the output bundle to reduce file size. Minification removes unnecessary characters and optimizes the code for production.

See also [Minification](../options/minification.md).

## `--target <target>`

Specify the JavaScript target version for the bundle. Examples include:

* `es2015`
* `esnext`
* `chrome100`
* `node18`

You can also disable all syntax transformations by using `--no-target` or by setting the target to `false` in your configuration file.

See also [Target](../options/target.md).

## `--log-level <level>`

Set the log level to control the verbosity of logs during the build process.

See also [Log Level](../options/log-level.md).

### ~~`--silent`~~

::: warning Deprecated
Please use `--log-level error` instead.
:::

Suppress non-error logs during the build process. Only error messages will be displayed.

## `-d, --out-dir <dir>`

Specify the output directory for the bundled files. Use this option to customize where the output files are written.

See also [Output Directory](../options/output-directory.md).

## `--treeshake`, `--no-treeshake`

Enable or disable tree shaking. Tree shaking removes unused code from the final bundle, reducing its size and improving performance.

See also [Tree Shaking](../options/tree-shaking.md).

## `--sourcemap`

Generate source maps for the bundled files. Source maps help with debugging by mapping the output code back to the original source files.

See also [Source Maps](../options/sourcemap.md).

## `--shims`

Enable CommonJS (CJS) and ECMAScript Module (ESM) shims. This ensures compatibility between different module systems.

See also [Shims](../options/shims.md).

## `--platform <platform>`

Specify the target platform for the bundle. Supported platforms include:

* `node` (Node.js)
* `browser` (Web browsers)
* `neutral` (Platform-agnostic)

See also [Platform](../options/platform.md).

## `--dts`

Generate TypeScript declaration (`.d.ts`) files for the bundled code. This is useful for libraries that need to provide type definitions.

See also [Declaration Files](../options/dts.md).

## `--publint`

Enable `publint` to validate your package for publishing. This checks for common issues in your package configuration, ensuring it meets best practices.

See also [Package Validation](../options/lint.md).

## `--attw`

Enable [Are the types wrong?](https://github.com/arethetypeswrong/arethetypeswrong.github.io) integration to check your package's TypeScript types for compatibility issues.

See also [Package Validation](../options/lint.md).

## `--unused`

Enable unused dependencies checking. This helps identify dependencies in your project that are not being used, allowing you to clean up your `package.json`.

## `-w, --watch [path]`

Enable watch mode to automatically rebuild your project when files change. Optionally, specify a path to watch for changes.

See also [Watch Mode](../options/watch-mode.md).

## `--ignore-watch <path>`

Ignore custom paths in watch mode.

## `--from-vite [vitest]`

Reuse configuration from Vite or Vitest. This allows you to extend or integrate with existing Vite or Vitest configurations seamlessly.

See also [Extending Vite or Vitest Config](../options/config-file.md#extending-vite-or-vitest-config-experimental).

## `--report`, `--no-report`

Enable or disable the generation of a build report. By default, the report is enabled and outputs the list of build artifacts along with their sizes to the console. This provides a quick overview of the build results, helping you analyze the output and identify potential optimizations. Disabling the report can be useful in scenarios where minimal console output is desired.

## `--env.* <value>`

Define compile-time environment variables, for example:

```bash
tsdown --env.NODE_ENV=production
```

Note that environment variables defined with `--env.VAR_NAME` can only be accessed as `import.meta.env.VAR_NAME` or `process.env.VAR_NAME`.

## `--env-file <file>`

Load environment variables from a file. When used together with `--env`, variables in `--env` take precedence.

:::tip
To prevent accidental exposure of sensitive information, only environment variables prefixed with `TSDOWN_` are injected by default. You can customize this behavior using the [`--env-prefix`](#env-prefix) flag.
:::

```bash
tsdown --env-file .env.production
```

## `--env-prefix <prefix>` {#env-prefix}

When loading environment variables from a file via `--env-file`, only include variables that start with these prefixes.

* **Default:** `TSDOWN_`

```bash
tsdown --env-file .env --env-prefix APP_ --env-prefix TSDOWN_
```

## `--debug [feat]`

Show debug logs.

## `--on-success <command>`

Specify a command to run after a successful build. This is especially useful in watch mode to trigger additional scripts or actions automatically after each build completes.

```bash
tsdown --on-success "echo Build finished!"
```

## `--copy <dir>`

Copies all files from the specified directory to the output directory. This is useful for including static assets such as images, stylesheets, or other resources in your build output.

```bash
tsdown --copy public
```

All contents of the `public` directory will be copied to your output directory (e.g., `dist`).

## `--public-dir <dir>`

::: warning Deprecated
Please use `--copy` instead.
:::

An alias for `--copy`.

## `--exe`

**\[experimental]** Bundle as a standalone executable using [Node.js Single Executable Applications](https://nodejs.org/api/single-executable-applications.html).

This will bundle the output into a single executable file. Requires Node.js 25.7.0 or later, and is not supported in Bun or Deno. Cross-platform builds are supported via the `@tsdown/exe` package.

When `exe` is enabled:

* Declaration file generation (`dts`) is disabled by default.
* Code splitting is disabled.
* Only single entry points are supported.

See also [Executable](../options/exe.md).

## `-W, --workspace [dir]`

Enable workspace mode for building multiple packages in a monorepo. Optionally specify the workspace root directory.

## `-F, --filter <pattern>`

Filter configs by working directory or name. Supports string matching and regex patterns (e.g., `/pkg-name$/` or `pkg-name`).

## `--unbundle`

Enable unbundle (bundleless) mode. Each source file is compiled individually, preserving the source directory structure in the output.

See also [Unbundle](../options/unbundle.md).

## `--fail-on-warn`

Fail the build when warnings are encountered. Enabled by default.

See also [CI Environment](../advanced/ci.md).

## `--exports`

Generate the `exports`, `main`, `module`, and `types` fields in your `package.json`.

See also [Package Exports](../options/package-exports.md).

---

---
url: /options/config-file.md
---
# Config File

By default, `tsdown` will search for a configuration file by looking in the current working directory and traversing upward through parent directories until it finds one. It supports the following file names:

* `tsdown.config.ts`
* `tsdown.config.mts`
* `tsdown.config.cts`
* `tsdown.config.js`
* `tsdown.config.mjs`
* `tsdown.config.cjs`
* `tsdown.config.json`
* `tsdown.config`

Additionally, you can define your configuration directly in the `tsdown` field of your `package.json` file.

## Writing a Config File

The configuration file allows you to define and customize your build settings in a centralized and reusable way. Below is a simple example of a `tsdown` configuration file:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: 'src/index.ts',
})
```

### Building Multiple Outputs

`tsdown` also supports returning an **array of configurations** from the config file. This allows you to build multiple outputs with different settings in a single run. For example:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig([
  {
    entry: 'src/entry1.ts',
    platform: 'node',
  },
  {
    entry: 'src/entry2.ts',
    platform: 'browser',
  },
])
```

## Specifying a Custom Config File

If your configuration file is located elsewhere or has a different name, you can specify its path using the `--config` (or `-c`) option:

```bash
tsdown --config ./path/to/config
```

## Disabling the Config File {#disable-config-file}

To disable loading a configuration file entirely, use the `--no-config` option:

```bash
tsdown --no-config
```

This is useful if you want to rely solely on command-line options or default settings.

## Config Loaders

`tsdown` supports multiple config loaders to accommodate various file formats. You can select a config loader using the `--config-loader` option. The available loaders are:

* `auto` (default): Utilizes native runtime loading for TypeScript if supported; otherwise, defaults to `unrun`.
* `native`: Loads TypeScript configuration files using native runtime support. Requires a compatible environment, such as the latest Node.js, Deno, or Bun.
* `unrun`: Loads configuration files using the [`unrun`](https://gugustinette.github.io/unrun/) library. It provides more powerful and flexible loading capabilities.

> \[!TIP]
> Node.js does not natively support importing TypeScript files without specifying the file extension. If you are using Node.js and want to load a TypeScript config file without including the `.ts` extension, consider using the `unrun` loader for seamless compatibility.

## Extending Vite or Vitest Config (Experimental)

`tsdown` provides an **experimental** feature to extend your existing Vite or Vitest configuration files. This allows you to reuse specific configuration options, such as `resolve` and `plugins`, while ignoring others that are not relevant to `tsdown`.

To enable this feature, use the `--from-vite` option:

```bash
tsdown --from-vite        # Load vite.config.*
tsdown --from-vite vitest # Load vitest.config.*
```

> \[!WARNING]
> This feature is **experimental** and may not support all Vite or Vitest configuration options. Only specific options, such as `resolve` and `plugins`, are reused. Use with caution and test thoroughly in your project.

> \[!TIP]
> Extending Vite or Vitest configurations can save time and effort if your project already uses these tools, allowing you to build upon your existing setup without duplicating configuration.

## Reference

For a full list of available configuration options, refer to the [Config Options Reference](../reference/api/Interface.UserConfig.md). This includes detailed explanations of all supported fields and their usage.

---

---
url: /options/css.md
---
# CSS Support

CSS support in `tsdown` is still an experimental feature. While it covers the core use cases, the API and behavior may change in future releases.

> \[!WARNING] Experimental Feature
> CSS support is experimental. Please test thoroughly and report any issues you encounter. The API and behavior may change as the feature matures.

## Getting Started

All CSS support in `tsdown` is provided by the `@tsdown/css` package. Install it to enable CSS handling:

```bash
npm install -D @tsdown/css
```

When `@tsdown/css` is installed, CSS processing is automatically enabled.

## CSS Import

Importing `.css` files from your TypeScript or JavaScript entry points is supported. The CSS content is extracted and emitted as a separate `.css` asset file:

```ts
// src/index.ts
import './style.css'

export function greet() {
  return 'Hello'
}
```

This produces both `index.mjs` and `index.css` in the output directory.

### `@import` Inlining

CSS `@import` statements are automatically resolved and inlined into the output. This means you can use `@import` to organize your CSS across multiple files without producing separate output files:

```css
/* style.css */
@import './reset.css';
@import './theme.css';

.main {
  color: red;
}
```

All imported CSS is bundled into a single output file with `@import` statements removed.

### Inline CSS (`?inline`)

Appending `?inline` to a CSS import returns the fully processed CSS as a JavaScript string instead of emitting a separate `.css` file. This aligns with [Vite's `?inline` behavior](https://vite.dev/guide/features#disabling-css-injection-into-the-page):

```ts
import css from './theme.css?inline' // Returns processed CSS as a string
import './style.css' // Extracted to a .css file
console.log(css) // ".theme { color: red; }\n"
```

The `?inline` CSS goes through the full processing pipeline — preprocessors, `@import` inlining, syntax lowering, and minification — just like regular CSS. The only difference is the output format: a JavaScript string export instead of a CSS asset file.

This also works with preprocessors:

```ts
import css from './theme.scss?inline'
```

When `?inline` is used, the CSS is not included in the emitted `.css` files and the import is tree-shakeable (`moduleSideEffects: false`).

## CSS Pre-processors

`tsdown` provides built-in support for `.scss`, `.sass`, `.less`, `.styl`, and `.stylus` files. The corresponding pre-processor must be installed as a dev dependency:

::: code-group

```sh [Sass]
# Either sass-embedded (recommended, faster) or sass
npm install -D sass-embedded
# or
npm install -D sass
```

```sh [Less]
npm install -D less
```

```sh [Stylus]
npm install -D stylus
```

:::

Once installed, you can import preprocessor files directly:

```ts
import './style.scss'
import './theme.less'
import './global.styl'
```

### Preprocessor Options

You can pass options to each preprocessor via `css.preprocessorOptions`:

```ts
export default defineConfig({
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `$brand-color: #ff7e17;`,
      },
      less: {
        math: 'always',
      },
    },
  },
})
```

#### `additionalData`

Each preprocessor supports an `additionalData` option to inject extra code at the beginning of every processed file. This is useful for global variables or mixins:

```ts
export default defineConfig({
  css: {
    preprocessorOptions: {
      scss: {
        // String — prepended to every .scss file
        additionalData: `@use "src/styles/variables" as *;`,
      },
    },
  },
})
```

You can also use a function for dynamic injection:

```ts
export default defineConfig({
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: (source, filename) => {
          if (filename.includes('theme')) return source
          return `@use "src/styles/variables" as *;\n${source}`
        },
      },
    },
  },
})
```

## CSS Minification

Enable CSS minification via `css.minify`:

```ts
export default defineConfig({
  css: {
    minify: true,
  },
})
```

Minification is powered by [Lightning CSS](https://lightningcss.dev/).

## CSS Target

By default, CSS syntax lowering uses the top-level [`target`](/options/target) option. You can override this specifically for CSS with `css.target`:

```ts
export default defineConfig({
  target: 'node18',
  css: {
    target: 'chrome90', // CSS-specific target
  },
})
```

Set `css.target: false` to disable CSS syntax lowering entirely, even when a top-level `target` is set:

```ts
export default defineConfig({
  target: 'chrome90',
  css: {
    target: false, // Preserve modern CSS syntax
  },
})
```

## CSS Transformer

The `css.transformer` option controls how CSS is processed. PostCSS and Lightning CSS are **mutually exclusive** processing paths:

* **`'lightningcss'`** (default): `@import` is resolved by Lightning CSS's `bundleAsync()`, and PostCSS is **not used at all**.
* **`'postcss'`**: `@import` is resolved by [`postcss-import`](https://github.com/postcss/postcss-import), PostCSS plugins are applied, then Lightning CSS is used only for final syntax lowering and minification.

```ts
export default defineConfig({
  css: {
    transformer: 'postcss', // Use PostCSS for @import and plugins
  },
})
```

When using the `'postcss'` transformer, install `postcss` and optionally `postcss-import` for `@import` resolution:

```bash
npm install -D postcss postcss-import
```

### PostCSS Options

Configure PostCSS inline or point to a config file:

```ts
export default defineConfig({
  css: {
    transformer: 'postcss',
    postcss: {
      plugins: [require('autoprefixer')],
    },
  },
})
```

Or specify a directory path to search for a PostCSS config file (`postcss.config.js`, etc.):

```ts
export default defineConfig({
  css: {
    transformer: 'postcss',
    postcss: './config', // Search for postcss.config.js in ./config/
  },
})
```

When `css.postcss` is omitted and `transformer` is `'postcss'`, tsdown auto-detects PostCSS config from the project root.

## Lightning CSS

`tsdown` uses [Lightning CSS](https://lightningcss.dev/) for CSS syntax lowering — transforming modern CSS features into syntax compatible with older browsers based on your `target` setting.

To enable CSS syntax lowering, install `lightningcss`:

::: code-group

```sh [npm]
npm install -D lightningcss
```

```sh [pnpm]
pnpm add -D lightningcss
```

```sh [yarn]
yarn add -D lightningcss
```

```sh [bun]
bun add -D lightningcss
```

:::

Once installed, CSS lowering is enabled automatically when a `target` is set. For example, with `target: 'chrome108'`, CSS nesting `&` selectors will be flattened:

```css
/* Input */
.foo {
  & .bar {
    color: red;
  }
}

/* Output (chrome108) */
.foo .bar {
  color: red;
}
```

### Lightning CSS Options

You can pass additional options to Lightning CSS via `css.lightningcss`:

```ts
import { Features } from 'lightningcss'

export default defineConfig({
  css: {
    lightningcss: {
      // Override browser targets directly (instead of using `target`)
      targets: { chrome: 100 << 16 },
      // Include/exclude specific features
      include: Features.Nesting,
    },
  },
})
```

> \[!TIP]
> When `css.lightningcss.targets` is set, it takes precedence over both the top-level `target` and `css.target` options for CSS transformations.

For more information on available options, refer to the [Lightning CSS documentation](https://lightningcss.dev/).

## Preserving CSS Imports (`css.inject`) {#css-inject}

By default, CSS import statements are removed from JS output after extracting the CSS into separate files. When `css.inject` is enabled, the JS output preserves `import` statements pointing to the emitted CSS files, so consumers of your library will automatically import the CSS alongside the JS:

```ts
export default defineConfig({
  css: {
    inject: true,
  },
})
```

With `css.inject: true`, the output JS will contain:

```js
// dist/index.mjs
import './style.css'

export function greet() {
  return 'Hello'
}
```

This is useful for component libraries where you want CSS to be automatically included when users import your components.

## CSS Code Splitting

### Merged Mode (Default)

By default, all CSS is merged into a single file (default: `style.css`):

```
dist/
  index.mjs
  style.css  ← all CSS merged
```

### Custom File Name

You can customize the merged CSS file name:

```ts
export default defineConfig({
  css: {
    fileName: 'my-library.css',
  },
})
```

### Splitting Mode

To split CSS per chunk — so each JavaScript chunk that imports CSS has a corresponding `.css` file — enable splitting:

```ts
export default defineConfig({
  css: {
    splitting: true,
  },
})
```

```
dist/
  index.mjs
  index.css        ← CSS from index.ts
  async-abc123.mjs
  async-abc123.css ← CSS from async chunk
```

## Options Reference

| Option                    | Type                          | Default          | Description                                                 |
| ------------------------- | ----------------------------- | ---------------- | ----------------------------------------------------------- |
| `css.transformer`         | `'postcss' \| 'lightningcss'` | `'lightningcss'` | CSS processing pipeline                                     |
| `css.splitting`           | `boolean`                     | `false`          | Enable CSS code splitting per chunk                         |
| `css.fileName`            | `string`                      | `'style.css'`    | File name for the merged CSS file (when `splitting: false`) |
| `css.minify`              | `boolean`                     | `false`          | Enable CSS minification                                     |
| `css.target`              | `string \| string[] \| false` | *from `target`*  | CSS-specific syntax lowering target                         |
| `css.postcss`             | `string \| object`            | —                | PostCSS config path or inline options                       |
| `css.preprocessorOptions` | `object`                      | —                | Options for CSS preprocessors                               |
| `css.inject`              | `boolean`                     | `false`          | Preserve CSS import statements in JS output                 |
| `css.lightningcss`        | `object`                      | —                | Options passed to Lightning CSS for syntax lowering         |

---

---
url: /advanced/rolldown-options.md
---
# Customizing Rolldown Options

`tsdown` uses [Rolldown](https://rolldown.rs) as its core bundling engine. This allows you to easily pass or override options directly to Rolldown, giving you fine-grained control over the bundling process.

For a full list of available Rolldown options, refer to the [Rolldown Config Options](https://rolldown.rs/options/input) documentation.

> \[!WARNING]
> You should be familiar with the behavior of the Rolldown options you are overriding and ensure you have read the Rolldown documentation.

## Overriding `inputOptions`

You can override the `inputOptions` generated by `tsdown` to customize how Rolldown processes your input files. There are two ways to do this:

### Using an Object

You can directly pass an object to override specific `inputOptions`:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  inputOptions: {
    cwd: './custom-directory',
  },
})
```

In this example, the `cwd` (current working directory) option is set to `./custom-directory`.

### Using a Function

Alternatively, you can use a function to dynamically modify the `inputOptions`. The function receives the generated `inputOptions` and the current `format` as arguments:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  inputOptions(inputOptions, format) {
    inputOptions.cwd = './custom-directory'
    return inputOptions
  },
})
```

This approach is useful when you need to customize options based on the output format or other dynamic conditions.

## Overriding `outputOptions`

The `outputOptions` can be customized in the same way as `inputOptions`. For example:

### Using an Object

You can directly pass an object to override specific `outputOptions`:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  outputOptions: {
    legalComments: 'inline',
  },
})
```

In this example, the `legalComments: 'inline'` option ensures that legal comments (e.g., license headers) are preserved in the output files.

### Using a Function

You can also use a function to dynamically modify the `outputOptions`. The function receives the generated `outputOptions` and the current `format` as arguments:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  outputOptions(outputOptions, format) {
    if (format === 'esm') {
      outputOptions.legalComments = 'inline'
    }
    return outputOptions
  },
})
```

This ensures that legal comments are preserved only for the `esm` format.

## When to Use Custom Options

While `tsdown` exposes many common options directly, there may be cases where certain Rolldown options are not exposed. In such cases, you can use the `inputOptions` and `outputOptions` overrides to directly set these options in Rolldown.

> \[!TIP]
> Using `inputOptions` and `outputOptions` gives you full access to Rolldown's powerful configuration system, allowing you to customize your build process beyond what `tsdown` exposes directly.

---

---
url: /options/dts.md
---
# Declaration Files (dts)

Declaration files (`.d.ts`) are an essential part of TypeScript libraries, providing type definitions that allow consumers of your library to benefit from TypeScript's type checking and IntelliSense.

`tsdown` makes it easy to generate and bundle declaration files for your library, ensuring a seamless developer experience for your users.

> \[!NOTE]
> You must install `typescript` in your project for declaration file generation to work properly.

## How dts Works in tsdown

`tsdown` uses [rolldown-plugin-dts](https://github.com/sxzz/rolldown-plugin-dts) internally to generate and bundle `.d.ts` files. This plugin is specifically designed to handle declaration file generation efficiently and integrates seamlessly with `tsdown`.

If you encounter any issues related to `.d.ts` generation, please report them directly to the [rolldown-plugin-dts repository](https://github.com/sxzz/rolldown-plugin-dts/issues).

## Enabling dts Generation

If your `package.json` contains a `types` or `typings` field, declaration file generation will be **enabled by default** in `tsdown`.

You can also explicitly enable `.d.ts` generation using the `--dts` option in the CLI or by setting `dts: true` in your configuration file.

### CLI

```bash
tsdown --dts
```

### Config File

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  dts: true,
})
```

## Declaration Map

Declaration maps allow `.d.ts` files to be mapped back to their original `.ts` sources, which is especially useful in monorepo setups for improved navigation and debugging. Learn more in the [TypeScript documentation](https://www.typescriptlang.org/tsconfig/#declarationMap).

You can enable declaration maps in either of the following ways (no need to set both):

### Enable in `tsconfig.json`

Enable the `declarationMap` option under `compilerOptions`:

```json [tsconfig.json]
{
  "compilerOptions": {
    "declarationMap": true
  }
}
```

### Enable in tsdown Config

Set the `dts.sourcemap` option to `true` in your tsdown config file:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  dts: {
    sourcemap: true,
  },
})
```

## Performance Considerations

The performance of `.d.ts` generation depends on your `tsconfig.json` configuration:

### With `isolatedDeclarations`

If your `tsconfig.json` has the `isolatedDeclarations` option enabled, `tsdown` will use **oxc-transform** for `.d.ts` generation. This method is **extremely fast** and highly recommended for optimal performance.

```json [tsconfig.json]
{
  "compilerOptions": {
    "isolatedDeclarations": true
  }
}
```

### Without `isolatedDeclarations`

If `isolatedDeclarations` is not enabled, `tsdown` will fall back to using the TypeScript compiler for `.d.ts` generation. While this approach is reliable, it is relatively slower compared to `oxc-transform`.

> \[!TIP]
> If speed is critical for your workflow, consider enabling `isolatedDeclarations` in your `tsconfig.json`.

## Build Process for dts

* **For ESM Output**: Both `.js` and `.d.ts` files are generated in the **same build process**. If you encounter compatibility issues, please report them.
* **For CJS Output**: A **separate build process** is used exclusively for `.d.ts` generation to ensure compatibility.

## Advanced Options

`rolldown-plugin-dts` provides several advanced options to customize `.d.ts` generation. For a detailed explanation of these options, refer to the [plugin's documentation](https://github.com/sxzz/rolldown-plugin-dts#options).

---

---
url: /options/dependencies.md
---
# Dependencies

When bundling with `tsdown`, dependencies are handled intelligently to ensure your library remains lightweight and easy to consume. Here's how `tsdown` processes different types of dependencies and how you can customize this behavior.

## Default Behavior

### `dependencies` and `peerDependencies`

By default, `tsdown` **does not bundle dependencies** listed in your `package.json` under `dependencies` and `peerDependencies`:

* **`dependencies`**: These are treated as external and will not be included in the bundle. Instead, they will be installed automatically by npm (or other package managers) when your library is installed.
* **`peerDependencies`**: These are also treated as external. Users of your library are expected to install these dependencies manually, although some package managers may handle this automatically.

### `devDependencies` and Phantom Dependencies

* **`devDependencies`**: Dependencies listed under `devDependencies` in your `package.json` will **only be bundled if they are actually imported or required by your source code**.
* **Phantom Dependencies**: Dependencies that exist in your `node_modules` folder but are not explicitly listed in your `package.json` will **only be bundled if they are actually used in your code**.

In other words, only the `devDependencies` and phantom dependencies that are actually referenced in your project will be included in the bundle.

## The `deps` Option

All dependency-related options are configured under the `deps` field:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  deps: {
    neverBundle: ['lodash', /^@my-scope\//],
    alwaysBundle: ['some-package'],
    onlyBundle: ['cac', 'bumpp'],
    skipNodeModulesBundle: true,
  },
})
```

### `deps.skipNodeModulesBundle`

If you want to **skip resolving and bundling all dependencies from `node_modules`**, you can enable `skipNodeModulesBundle`:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  deps: {
    skipNodeModulesBundle: true,
  },
})
```

This will prevent `tsdown` from parsing and bundling any dependencies from `node_modules`, regardless of how they are referenced in your code.

::: warning
`skipNodeModulesBundle` cannot be used together with `alwaysBundle`. These options are mutually exclusive.
:::

### `deps.onlyBundle`

The `onlyBundle` option acts as a whitelist for dependencies that are allowed to be bundled from `node_modules`. If any dependency not in the list is found in the bundle, tsdown will throw an error. This is useful for preventing unexpected dependencies from being silently inlined into your output, especially in large projects.

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  deps: {
    onlyBundle: ['cac', 'bumpp'],
  },
})
```

In this example, only `cac` and `bumpp` are allowed to be bundled. If any other `node_modules` dependency is imported, tsdown will throw an error with a message indicating which dependency was unexpectedly bundled and which files imported it.

#### Behavior

* **`onlyBundle` is an array** (e.g., `['cac', /^my-/]`): Only dependencies matching the list are allowed to be bundled. An error is thrown for any others. Unused patterns in the list will also be reported.
* **`onlyBundle` is `false`**: All warnings and checks about bundled dependencies are suppressed.
* **`onlyBundle` is not set** (default): A warning is shown if any `node_modules` dependencies are bundled, suggesting you add the `onlyBundle` option or set it to `false` to suppress warnings.

::: tip
Make sure to include all required sub-dependencies in the `onlyBundle` list as well, not just the top-level packages you directly import.
:::

### `deps.neverBundle`

The `neverBundle` option allows you to explicitly mark certain dependencies as external, ensuring they are not bundled into your library. For example:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  deps: {
    neverBundle: ['lodash', /^@my-scope\//],
  },
})
```

In this example, `lodash` and all packages under the `@my-scope` namespace will be treated as external.

### `deps.alwaysBundle`

The `alwaysBundle` option allows you to force certain dependencies to be bundled, even if they are listed in `dependencies` or `peerDependencies`. For example:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  deps: {
    alwaysBundle: ['some-package'],
  },
})
```

Here, `some-package` will be bundled into your library.

## Handling Dependencies in Declaration Files

The bundling logic for declaration files is consistent with JavaScript: dependencies are bundled or marked as external according to the same rules and options.

### Resolver Option

When bundling complex third-party types, you may encounter cases where the default resolver (Oxc) cannot handle certain scenarios. For example, the types for `@babel/generator` are located in the `@types/babel__generator` package, which may not be resolved correctly by Oxc.

To address this, you can set the `resolver` option to `tsc` in your configuration. This uses the native TypeScript resolver, which is slower but much more compatible with complex type setups:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  dts: {
    resolver: 'tsc',
  },
})
```

## Migration from Deprecated Options

The following top-level options are deprecated. Please migrate to the `deps` namespace:

| Deprecated Option       | New Option                   |
| ----------------------- | ---------------------------- |
| `external`              | `deps.neverBundle`           |
| `noExternal`            | `deps.alwaysBundle`          |
| `inlineOnly`            | `deps.onlyBundle`            |
| `deps.onlyAllowBundle`  | `deps.onlyBundle`            |
| `skipNodeModulesBundle` | `deps.skipNodeModulesBundle` |

## Summary

* **Default Behavior**:
  * `dependencies` and `peerDependencies` are treated as external and not bundled.
  * `devDependencies` and phantom dependencies are only bundled if they are actually used in your code.
* **Customization**:
  * Use `deps.onlyBundle` to whitelist dependencies allowed to be bundled, and throw an error for any others.
  * Use `deps.neverBundle` to mark specific dependencies as external.
  * Use `deps.alwaysBundle` to force specific dependencies to be bundled.
  * Use `deps.skipNodeModulesBundle` to skip resolving and bundling all dependencies from `node_modules`.
* **Declaration Files**:
  * The bundling logic for declaration files is now the same as for JavaScript.
  * Use `resolver: 'tsc'` for better compatibility with complex third-party types.

By understanding and customizing dependency handling, you can ensure your library is optimized for both size and usability.

---

---
url: /options/entry.md
---
# Entry

The `entry` option specifies the entry files for your project. These files serve as the starting points for the bundling process. You can define entry files either via the CLI or in the configuration file.

## Using the CLI

You can specify entry files directly as command arguments when using the CLI. For example:

```bash
tsdown src/entry1.ts src/entry2.ts
```

This command will bundle `src/entry1.ts` and `src/entry2.ts` as separate entry points.

## Using the Config File

In the configuration file, the `entry` option allows you to define entry files in various formats:

### Single Entry File

Specify a single entry file as a string:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: 'src/index.ts',
})
```

### Multiple Entry Files

Define multiple entry files as an array of strings:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: ['src/entry1.ts', 'src/entry2.ts'],
})
```

### Entry Files with Aliases

Use an object to define entry files with aliases. The keys represent alias names, and the values represent file paths:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: {
    main: 'src/index.ts',
    utils: 'src/utils.ts',
  },
})
```

This configuration will create two bundles: one for `src/index.ts` (output as `dist/main.js`) and one for `src/utils.ts` (output as `dist/utils.js`).

## Using Glob Patterns

The `entry` option supports [glob patterns](https://code.visualstudio.com/docs/editor/glob-patterns), enabling you to match multiple files dynamically. For example:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: 'src/**/*.ts',
})
```

This configuration will include all `.ts` files in the `src` directory and its subdirectories as entry points.

You can also use glob patterns in arrays, with negation patterns to exclude specific files:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: ['src/*.ts', '!src/*.test.ts'],
})
```

### Object Entries with Glob Patterns

When using the object form, you can use glob wildcards (`*`) in both keys and values. The `*` in the key acts as a placeholder that gets replaced with the matched file name (without extension):

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: {
    // Maps src/foo.ts → dist/lib/foo.js, src/bar.ts → dist/lib/bar.js
    'lib/*': 'src/*.ts',
  },
})
```

This is useful for creating output structures that differ from the source layout.

#### Negation Patterns

When using glob keys, values can be an array of patterns including negation patterns (prefixed with `!`) to exclude specific files:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: {
    // Include all hooks except the index file
    'hooks/*': ['src/hooks/*.ts', '!src/hooks/index.ts'],
  },
})
```

#### Multiple Patterns

You can combine multiple positive patterns and multiple negation patterns:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: {
    'utils/*': [
      'src/utils/*.ts',
      'src/utils/*.tsx',
      '!src/utils/index.ts',
      '!src/utils/internal.ts',
    ],
  },
})
```

> \[!WARNING]
> When using multiple positive patterns in an array value, all patterns must share the same base directory. For example, mixing `src/hooks/*.ts` and `src/utils/*.ts` in a single entry key will throw an error.

#### Mixed Entries

You can mix strings, glob patterns, and object entries in an array:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: [
    'src/*',
    '!src/foo.ts',
    { main: 'index.ts' },
    { 'lib/*': ['src/*.ts', '!src/bar.ts'] },
  ],
})
```

When the same output name appears in both array entries and object entries, the object entry takes precedence.

> \[!TIP]
>
> On **Windows**, you must use forward slashes (`/`) instead of backslashes (`\`) in file paths when using glob patterns.

---

---
url: /options/exe.md
---
# Executable

:::warning Experimental
The `exe` option is experimental and may change in future releases.
:::

tsdown can bundle your TypeScript/JavaScript code into a standalone executable using [Node.js Single Executable Applications](https://nodejs.org/api/single-executable-applications.html). The output is a native binary that runs without requiring Node.js to be installed.

## Requirements

* Node.js >= 25.7.0
* Not supported in Bun or Deno

## Basic Usage

```bash
tsdown src/cli.ts --exe
```

Or in your config file:

```ts [tsdown.config.ts]
export default defineConfig({
  entry: ['src/cli.ts'],
  exe: true,
})
```

When `exe` is enabled:

* Declaration file generation (`dts`) is disabled by default
* Code splitting is disabled
* Only single entry points are supported

## Advanced Configuration

You can pass an object to `exe` for more control:

```ts [tsdown.config.ts]
export default defineConfig({
  entry: ['src/cli.ts'],
  exe: {
    fileName: 'my-tool',
    seaConfig: {
      disableExperimentalSEAWarning: true,
      useCodeCache: true,
    },
  },
})
```

### `fileName`

Custom output file name for the executable. Do not include `.exe`, platform suffixes, or architecture suffixes — they are added automatically.

Can be a string or a function:

```ts [tsdown.config.ts]
export default defineConfig({
  entry: ['src/cli.ts'],
  // string
  exe: { fileName: 'my-tool' },
  // or function
  // exe: { fileName: (chunk) => `my-tool-${chunk.name}` },
})
```

### `seaConfig`

Passes options directly to Node.js. See the [Node.js documentation](https://nodejs.org/api/single-executable-applications.html) for full details.

| Option                          | Type                       | Default | Description                          |
| ------------------------------- | -------------------------- | ------- | ------------------------------------ |
| `disableExperimentalSEAWarning` | `boolean`                  | `true`  | Disable the experimental warning     |
| `useSnapshot`                   | `boolean`                  | `false` | Use V8 snapshot for faster startup   |
| `useCodeCache`                  | `boolean`                  | `false` | Use V8 code cache for faster startup |
| `execArgv`                      | `string[]`                 | —       | Extra Node.js CLI arguments          |
| `execArgvExtension`             | `'none' \| 'env' \| 'cli'` | `'env'` | How to extend execArgv at runtime    |
| `assets`                        | `Record<string, string>`   | —       | Assets to embed into the executable  |

## Cross-Platform Builds

By default, `exe` builds for the current platform. To build executables for multiple platforms from a single machine, install the `@tsdown/exe` package and use the `targets` option:

::: code-group

```bash [pnpm]
pnpm add -D @tsdown/exe
```

```bash [npm]
npm install -D @tsdown/exe
```

```bash [yarn]
yarn add -D @tsdown/exe
```

:::

```ts [tsdown.config.ts]
export default defineConfig({
  entry: ['src/cli.ts'],
  exe: {
    targets: [
      { platform: 'linux', arch: 'x64', nodeVersion: '25.7.0' },
      { platform: 'darwin', arch: 'arm64', nodeVersion: '25.7.0' },
      { platform: 'win', arch: 'x64', nodeVersion: '25.7.0' },
    ],
  },
})
```

This downloads the target platform's Node.js binary from nodejs.org, caches it locally, and uses it to build the executable. The output files are named with platform and architecture suffixes:

```
dist/
  cli-linux-x64
  cli-darwin-arm64
  cli-win-x64.exe
```

### Target Options

Each target in the `targets` array accepts:

| Field         | Type                           | Description                                              |
| ------------- | ------------------------------ | -------------------------------------------------------- |
| `platform`    | `'win' \| 'darwin' \| 'linux'` | Target operating system (aligned with nodejs.org naming) |
| `arch`        | `'x64' \| 'arm64'`             | Target CPU architecture                                  |
| `nodeVersion` | `string`                       | Node.js version to use (must be `>=25.7.0`)              |

:::warning
When `targets` is specified, the `seaConfig.executable` option is ignored — the downloaded Node.js binary is used instead.
:::

:::tip Note
When generating cross-platform executables (e.g., generating an executable for linux-x64 on darwin-arm64), `useCodeCache` and `useSnapshot` must be set to `false` to avoid generating incompatible executables. Since code cache and snapshots can only be loaded on the same platform where they are compiled, the generated executable might crash on startup when trying to load code cache or snapshots built on a different platform.
:::

### Caching

Downloaded Node.js binaries are cached in the system cache directory:

* **macOS:** `~/Library/Caches/tsdown/node/`
* **Linux:** `~/.cache/tsdown/node/` (or `$XDG_CACHE_HOME/tsdown/node/`)
* **Windows:** `%LOCALAPPDATA%/tsdown/Caches/node/`

Subsequent builds reuse cached binaries without re-downloading.

## Platform Notes

* On **macOS**, the executable is automatically codesigned (ad-hoc) for Gatekeeper compatibility. When cross-compiling for macOS from a non-macOS host, codesigning will be skipped with a warning.
* On **Windows**, the `.exe` extension is automatically appended.

---

---
url: /guide/faq.md
---
# Frequently Asked Questions

## Why tsdown Does Not Support Stub Mode {#stub-mode}

`tsdown` does **not** support stub mode due to several limitations and design considerations:

* **Stub mode requires manual intervention:**
  Whenever you change named exports, you must re-run the stub command to update the stubs. This disrupts the development workflow and can lead to inconsistencies.
* **Stub mode is incompatible with plugins:**
  Stub mode cannot support plugin functionality, which is essential for many advanced use cases and custom build logic.

### Recommended Alternatives

Instead of stub mode, we recommend more reliable and flexible approaches:

1. **Use [Watch Mode](../options/watch-mode.md):**
   The simplest solution is to run `tsdown` in watch mode. This keeps your build up-to-date automatically as you make changes, though it requires you to keep the process running in the background.

2. **Use [`exports.devExports`](../options/package-exports.md#dev-exports) for Dev/Prod Separation:**
   For a more advanced and robust setup, use the `exports.devExports` option to specify different export paths for development and production. This allows you to point to source files during development and built files for production.
   * **If you use plugins:**
     Consider using [vite-node](https://github.com/antfu-collective/vite-node) to run your code directly with plugin support.
   * **If you do not use plugins:**
     You can use lightweight TypeScript runners such as [tsx](https://github.com/privatenumber/tsx), [jiti](https://github.com/unjs/jiti), or [unrun](https://github.com/Gugustinette/unrun).
   * **If you do not use plugins and your code is compatible with Node.js's built-in TypeScript support:**
     With Node.js v22.18.0 and above, you can run TypeScript files directly without any additional runners.

These alternatives provide a smoother and more reliable development experience compared to stub mode, especially as your project grows or requires plugin support. For a more detailed explanation of this decision, please see [this GitHub comment](https://github.com/rolldown/tsdown/pull/164#issuecomment-2849720617).

## How does tsdown differ from tsup? {#tsdown-vs-tsup}

tsdown is the spiritual successor to tsup, powered by Rolldown instead of esbuild. Key differences:

* **Faster builds**: Rolldown provides significantly better performance, especially for large projects.
* **Richer plugin ecosystem**: tsdown supports Rolldown, Rollup, and unplugin plugins.
* **More features**: CSS support, executable bundling, workspace mode, and package validation are built in.

For a detailed comparison and migration guide, see [Migrate from tsup](./migrate-from-tsup.md).

## Can I use tsdown in a monorepo? {#monorepo}

Yes. tsdown has built-in workspace support. Use `--workspace` (or `-W`) to enable workspace mode, which auto-detects packages in your monorepo. You can filter specific packages with `--filter` (or `-F`):

```bash
tsdown -W -F my-package
```

Root-level configuration is automatically inherited by workspace packages.

## Why are my dependencies being bundled? {#dependencies-bundled}

By default, tsdown bundles all imported modules. To exclude dependencies (e.g., those listed in `package.json`), use the `deps` configuration:

```ts
export default defineConfig({
  deps: {
    skipNodeModulesBundle: true,
  },
})
```

See [Dependencies](../options/dependencies.md) for more options.

## How do I generate type declarations? {#dts}

Use the `dts` option:

```ts
export default defineConfig({
  dts: true,
})
```

tsdown auto-enables DTS generation when your `package.json` includes `types` or `typings` fields, or when `exports` entries contain type conditions. See [Declaration Files](../options/dts.md) for advanced options.

---

---
url: /reference/api/Function.build.md
---
# Function: build()

```ts
function build(inlineConfig?): Promise<TsdownBundle[]>
```

Defined in: [src/build.ts:43](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/build.ts#L43)

Build with tsdown.

## Parameters

### inlineConfig?

[`InlineConfig`](Interface.InlineConfig.md) = `{}`

## Returns

`Promise`<[`TsdownBundle`](Interface.TsdownBundle.md)\[]>

---

---
url: /reference/api/Function.defineConfig.md
---
# Function: defineConfig()

## Call Signature

```ts
function defineConfig(options): UserConfig
```

Defined in: [src/config.ts:9](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config.ts#L9)

Defines the configuration for tsdown.

### Parameters

#### options

[`UserConfig`](Interface.UserConfig.md)

### Returns

[`UserConfig`](Interface.UserConfig.md)

## Call Signature

```ts
function defineConfig(options): UserConfig[]
```

Defined in: [src/config.ts:10](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config.ts#L10)

Defines the configuration for tsdown.

### Parameters

#### options

[`UserConfig`](Interface.UserConfig.md)\[]

### Returns

[`UserConfig`](Interface.UserConfig.md)\[]

## Call Signature

```ts
function defineConfig(options): UserConfigFn
```

Defined in: [src/config.ts:11](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config.ts#L11)

Defines the configuration for tsdown.

### Parameters

#### options

[`UserConfigFn`](TypeAlias.UserConfigFn.md)

### Returns

[`UserConfigFn`](TypeAlias.UserConfigFn.md)

## Call Signature

```ts
function defineConfig(options): UserConfigExport
```

Defined in: [src/config.ts:12](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config.ts#L12)

Defines the configuration for tsdown.

### Parameters

#### options

[`UserConfigExport`](TypeAlias.UserConfigExport.md)

### Returns

[`UserConfigExport`](TypeAlias.UserConfigExport.md)

---

---
url: /reference/api/Function.enableDebug.md
---
# Function: enableDebug()

```ts
function enableDebug(debug?): void
```

Defined in: [src/features/debug.ts:7](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/debug.ts#L7)

## Parameters

### debug?

`boolean` | `Arrayable`<`string`>

## Returns

`void`

---

---
url: /reference/api/Function.mergeConfig.md
---
# Function: mergeConfig()

## Call Signature

```ts
function mergeConfig(defaults, overrides): UserConfig
```

Defined in: [src/config/options.ts:362](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/options.ts#L362)

### Parameters

#### defaults

[`UserConfig`](Interface.UserConfig.md)

#### overrides

[`UserConfig`](Interface.UserConfig.md)

### Returns

[`UserConfig`](Interface.UserConfig.md)

## Call Signature

```ts
function mergeConfig(defaults, overrides): InlineConfig
```

Defined in: [src/config/options.ts:366](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/options.ts#L366)

### Parameters

#### defaults

[`InlineConfig`](Interface.InlineConfig.md)

#### overrides

[`InlineConfig`](Interface.InlineConfig.md)

### Returns

[`InlineConfig`](Interface.InlineConfig.md)

---

---
url: /guide/getting-started.md
---
# Getting Started

:::warning 🚧 Beta Software
[Rolldown](https://rolldown.rs) is currently in beta status. While it can already handle most production use cases, there may still be bugs and rough edges.
:::

## Installation

There are several ways to get started with `tsdown`. You can:

* [Manually install](#manual-installation) it as a development dependency in your project.
* Use the [starter templates](#starter-templates) to quickly scaffold a new project.
* Try it online using [StackBlitz](#try-online).

### Manual Installation {#manual-installation}

Install `tsdown` as a development dependency using your preferred package manager:

::: code-group

```sh [npm]
npm install -D tsdown
```

```sh [pnpm]
pnpm add -D tsdown
```

```sh [yarn]
yarn add -D tsdown
```

```sh [bun]
bun add -D tsdown
```

:::

Optionally, if you're not using [`isolatedDeclarations`](https://www.typescriptlang.org/tsconfig/#isolatedDeclarations), you should also install TypeScript as a development dependency:

::: code-group

```sh [npm]
npm install -D typescript
```

```sh [pnpm]
pnpm add -D typescript
```

```sh [yarn]
yarn add -D typescript
```

```sh [bun]
bun add -D typescript
```

:::

:::tip Compatibility Note
`tsdown` requires Node.js version 20.19 or higher. Please ensure your development environment meets this requirement before installing. While `tsdown` is primarily tested with Node.js, support for Deno and Bun is experimental and may not work as expected.
:::

:::warning Node.js Deprecation
Node.js versions below 22.18.0 are deprecated and support will be removed in the next minor release. Please upgrade to Node.js 22.18.0 or later.
:::

### Starter Templates {#starter-templates}

To get started even faster, you can use the [create-tsdown](https://github.com/rolldown/tsdown/tree/main/packages/create-tsdown) CLI, which provides a set of starter templates for building pure TypeScript libraries, as well as frontend libraries like React and Vue.

::: code-group

```sh [npm]
npm create tsdown@latest
```

```sh [pnpm]
pnpm create tsdown@latest
```

```sh [yarn]
yarn create tsdown@latest
```

```sh [bun]
bun create tsdown@latest
```

:::

These templates include ready-to-use configurations and best practices for building, testing, and linting TypeScript projects.

### Try Online {#try-online}

You can try tsdown directly in your browser using StackBlitz:

[![tsdown-starter-stackblitz](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://stackblitz.com/github/rolldown/tsdown-starter-stackblitz)

This template is preconfigured for tsdown, so you can experiment and get started quickly—no local setup required.

## Using the CLI

To verify that `tsdown` is installed correctly, run the following command in your project directory:

```sh
./node_modules/.bin/tsdown --version
```

You can also explore the available CLI options and examples with:

```sh
./node_modules/.bin/tsdown --help
```

### Your First Bundle

Let's create two source TypeScript files:

```ts [src/index.ts]
import { hello } from './hello.ts'

hello()
```

```ts [src/hello.ts]
export function hello() {
  console.log('Hello tsdown!')
}
```

Next, initialize the `tsdown` configuration file:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: ['./src/index.ts'],
})
```

Now, run the following command to bundle your code:

```sh
./node_modules/.bin/tsdown
```

You should see the bundled output written to `dist/index.mjs`. To verify it works, run the output file:

```sh
node dist/index.mjs
```

You should see the message `Hello tsdown!` printed to the console.

### Using the CLI in npm Scripts

To simplify the command, you can add it to your `package.json` scripts:

```json{5} [package.json]
{
  "name": "my-tsdown-project",
  "type": "module",
  "scripts": {
    "build": "tsdown"
  },
  "devDependencies": {
    "tsdown": "^0.9.0"
  }
}
```

Now, you can build your project with:

```sh
npm run build
```

## Using the Config File

While you can use the CLI directly, it's recommended to use a configuration file for more complex projects. This allows you to define and manage your build settings in a centralized and reusable way.

For more details, refer to the [Config File](../options/config-file.md) documentation.

## Using Plugins

`tsdown` supports plugins to extend its functionality. You can use Rolldown plugins, Unplugin plugins, and most Rollup plugins seamlessly. To use plugins, add them to the `plugins` array in your configuration file. For example:

```ts [tsdown.config.ts]
import SomePlugin from 'some-plugin'
import { defineConfig } from 'tsdown'

export default defineConfig({
  plugins: [SomePlugin()],
})
```

For more details, refer to the [Plugins](../advanced/plugins.md) documentation.

## Using Watch Mode

You can enable watch mode to automatically rebuild your project whenever files change. This is particularly useful during development to streamline your workflow. Use the `--watch` (or `-w`) option:

```bash
tsdown --watch
```

For more details, refer to the [Watch Mode](../options/watch-mode.md) documentation.

---

---
url: /advanced/hooks.md
---
# Hooks

Inspired by [unbuild](https://github.com/unjs/unbuild), `tsdown` supports a flexible hooks system that allows you to extend and customize the build process. While we recommend using the [plugin system](./plugins.md) for most build-related extensions, hooks provide a convenient way to inject Rolldown plugins or perform additional tasks at specific stages of the build lifecycle.

## Usage

You can define hooks in your configuration file in two ways:

### Passing an Object

Define your hooks as an object, where each key is a hook name and the value is a function:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  hooks: {
    'build:done': async () => {
      await doSomething()
    },
  },
})
```

### Passing a Function

Alternatively, you can pass a function that receives the hooks object, allowing you to register hooks programmatically:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  hooks(hooks) {
    hooks.hook('build:prepare', () => {
      console.log('Hello World')
    })
  },
})
```

For more details on how to use the hooks, refer to the [hookable](https://github.com/unjs/hookable) documentation.

## Available Hooks

For detailed type definitions, see [`src/features/hooks.ts`](https://github.com/rolldown/tsdown/blob/main/src/features/hooks.ts).

### `build:prepare`

Invoked before each tsdown build starts. Use this hook to perform setup or preparation tasks.

### `build:before`

Invoked before each Rolldown build. For dual-format builds, this hook is called for each format. Useful for configuring or modifying the build context before bundling.

### `build:done`

Invoked after each tsdown build completes. Use this hook for cleanup or post-processing tasks.

---

---
url: /guide/how-it-works.md
---
# How It Works

This page gives a high-level overview of what tsdown does out of the box and which options let you adjust each behavior. For full details, follow the links to the dedicated option pages.

## Smart Defaults at a Glance {#smart-defaults}

tsdown reads your `package.json` and `tsconfig.json` to infer sensible defaults. Here's what happens automatically:

| When tsdown detects...                                        | It will...                                                             |
| ------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `dependencies` / `peerDependencies` in package.json           | Externalize them (not bundled)                                         |
| A `devDependency` imported in your code                       | Bundle it into the output                                              |
| `types` or `typings` field in package.json                    | Enable `.d.ts` generation                                              |
| `isolatedDeclarations` in tsconfig.json                       | Use the fast **oxc-transform** path for dts                            |
| `engines.node` in package.json                                | Infer the compilation [target](../options/target.md) from it           |
| `type: "module"` in package.json                              | Use `.js` extension for ESM output (instead of `.mjs`)                 |
| No `entry` specified, but `src/index.ts` exists               | Use it as the default entry point                                      |
| `platform: "node"` (the default)                              | Enable [`fixedExtension`](../options/output-format.md) (`.mjs`/`.cjs`) |
| Dual-format build with `exports: true`                        | Generate `main`/`module` legacy fields in package.json                 |
| Config file changes in [watch mode](../options/watch-mode.md) | Restart the entire build                                               |

The sections below explain each area in more detail.

## Dependencies {#dependencies}

When you publish a library, your consumers install its `dependencies` and `peerDependencies` alongside it. There's no need to bundle those packages into your output — they'll already be available at runtime.

**Default behavior:**

* **`dependencies` and `peerDependencies`** are **externalized** — they appear as `import` / `require` statements in the output and are not included in the bundle.
* **`devDependencies`** are **bundled if imported**. Since they won't be installed by consumers, any code you import from a devDependency is inlined into your output automatically.
* **Phantom dependencies** (installed in `node_modules` but not listed in your `package.json`) follow the same rule as devDependencies — bundled only if used.

**Key options:**

| Option                                                                               | What it does                                                                                                                                                                    |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`deps.onlyBundle`](../options/dependencies.md#deps-onlybundle)                      | Whitelist of dependencies allowed to be bundled. Any unlisted dependency that ends up in the bundle causes an error. Useful for catching accidental inlining in large projects. |
| [`deps.neverBundle`](../options/dependencies.md#deps-neverbundle)                    | Explicitly mark additional packages as external (never bundled).                                                                                                                |
| [`deps.alwaysBundle`](../options/dependencies.md#deps-alwaysbundle)                  | Force specific packages to be bundled, even if they're in `dependencies`.                                                                                                       |
| [`deps.skipNodeModulesBundle`](../options/dependencies.md#deps-skipnodemodulebundle) | Skip resolving and bundling everything from `node_modules`.                                                                                                                     |

See [Dependencies](../options/dependencies.md) for details.

## Output Format {#output-format}

tsdown produces **ESM** output by default. You can generate multiple formats in a single build, and even override options per format.

**Key options:**

| Option                                  | What it does                                                                                                        |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| [`format`](../options/output-format.md) | Set to `esm`, `cjs`, `iife`, or `umd`. Pass multiple values (e.g. `format: ['esm', 'cjs']`) for dual-format builds. |
| [`shims`](../options/shims.md)          | Inject compatibility shims (e.g. `__dirname` for ESM, `import.meta` for CJS).                                       |

See [Output Format](../options/output-format.md) for details.

## Declaration Files (dts) {#dts}

tsdown generates `.d.ts` files so consumers get full TypeScript support.

**Default behavior:**

* If your `package.json` has a `types` or `typings` field, dts generation is **enabled automatically**.
* With [`isolatedDeclarations`](https://www.typescriptlang.org/tsconfig/#isolatedDeclarations) enabled in your `tsconfig.json`, tsdown uses the fast **oxc-transform** path. Otherwise, it falls back to the TypeScript compiler.

**Key options:**

| Option                     | What it does                                                                                 |
| -------------------------- | -------------------------------------------------------------------------------------------- |
| [`dts`](../options/dts.md) | Enable/disable dts, or pass an object for advanced settings like `resolver` and `sourcemap`. |

See [Declaration Files](../options/dts.md) for details.

## Package Exports {#package-exports}

When publishing a library, the `exports` field in `package.json` tells consumers and bundlers how to resolve your package's entry points.

**Default behavior:**

* Auto-generation of `exports` is **off by default**. You manage the `exports` field in your `package.json` yourself.

**With `exports: true`:**

* tsdown analyzes your entry points and output files, then writes the `exports`, `main`, `module`, and `types` fields in your `package.json` automatically.
* For dual-format builds (ESM + CJS), it generates conditional exports with `import` and `require` conditions.

**Key options:**

| Option                                                                       | What it does                                                                |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| [`exports`](../options/package-exports.md)                                   | Set to `true` to enable auto-generation, or pass an object for fine-tuning. |
| [`exports.all`](../options/package-exports.md#exporting-all-files)           | Export all output files, not just entry points.                             |
| [`exports.devExports`](../options/package-exports.md#dev-exports)            | Point exports to source files during development for better editor support. |
| [`exports.customExports`](../options/package-exports.md#customizing-exports) | A function that lets you modify or extend the generated exports.            |

See [Package Exports](../options/package-exports.md) for details.

## Package Validation {#package-validation}

tsdown integrates with [publint](https://publint.dev/) and [attw](https://arethetypeswrong.github.io/) to catch publishing mistakes before they reach npm.

**Default behavior:**

* Both tools are **disabled by default** and are optional peer dependencies.

**What they check:**

* **publint** validates your `package.json` configuration — it checks that `exports`, `main`, `module`, and `types` point to files that actually exist, that module formats are correct, and flags common misconfigurations.
* **attw** (Are the types wrong?) verifies that your TypeScript declarations resolve correctly under different module resolution strategies (`node10`, `node16`, `bundler`), catching issues like false ESM/CJS type declarations.

**Key options:**

| Option                                                | What it does                                                                |
| ----------------------------------------------------- | --------------------------------------------------------------------------- |
| [`publint`](../options/lint.md#publint)               | Set to `true` or `'ci-only'` to enable.                                     |
| [`attw`](../options/lint.md#attw-are-the-types-wrong) | Set to `true` or pass an object with `profile`, `level`, and `ignoreRules`. |

See [Package Validation](../options/lint.md) for details.

## Other Defaults {#other-defaults}

A few more things tsdown handles for you:

* **Output directory** — Defaults to `dist/`. The output directory is **cleaned before each build**. Use `--no-clean` to keep existing files. See [Cleaning](../options/cleaning.md).
* **Tree-shaking** — Enabled by default. Dead code is removed from the output. See [Tree-shaking](../options/tree-shaking.md).
* **Platform** — Defaults to `node`. See [Platform](../options/platform.md).
* **Target** — Inferred from your `package.json` `engines` field, or defaults to the latest stable Node.js version. See [Target](../options/target.md).

---

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

---

---
url: /reference/api/Interface.BuildContext.md
---
# Interface: BuildContext

Defined in: [src/features/hooks.ts:8](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/hooks.ts#L8)

## Properties

### hooks

```ts
hooks: Hookable<TsdownHooks>
```

Defined in: [src/features/hooks.ts:10](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/hooks.ts#L10)

***

### options

```ts
options: ResolvedConfig
```

Defined in: [src/features/hooks.ts:9](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/hooks.ts#L9)

---

---
url: /reference/api/Interface.ChunkAddonObject.md
---
# Interface: ChunkAddonObject

Defined in: [src/features/output.ts:90](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/output.ts#L90)

## Properties

### css?

```ts
optional css: string;
```

Defined in: [src/features/output.ts:92](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/output.ts#L92)

***

### dts?

```ts
optional dts: string;
```

Defined in: [src/features/output.ts:93](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/output.ts#L93)

***

### js?

```ts
optional js: string;
```

Defined in: [src/features/output.ts:91](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/output.ts#L91)

---

---
url: /reference/api/Interface.CopyEntry.md
---
# Interface: CopyEntry

Defined in: [src/features/copy.ts:8](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/copy.ts#L8)

## Properties

### flatten?

```ts
optional flatten: boolean;
```

Defined in: [src/features/copy.ts:23](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/copy.ts#L23)

Whether to flatten the copied files (not preserving directory structure).

#### Default

```ts
true
```

***

### from

```ts
from: string | string[];
```

Defined in: [src/features/copy.ts:12](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/copy.ts#L12)

Source path or glob pattern.

***

### rename?

```ts
optional rename: string | (name, extension, fullPath) => string;
```

Defined in: [src/features/copy.ts:32](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/copy.ts#L32)

Change destination file or folder name.

***

### to?

```ts
optional to: string;
```

Defined in: [src/features/copy.ts:17](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/copy.ts#L17)

Destination path.
If not specified, defaults to the output directory ("outDir").

***

### verbose?

```ts
optional verbose: boolean;
```

Defined in: [src/features/copy.ts:28](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/copy.ts#L28)

Output copied items to console.

#### Default

```ts
false
```

---

---
url: /reference/api/Interface.DepsConfig.md
---
# Interface: DepsConfig

Defined in: [src/features/deps.ts:35](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L35)

## Properties

### alwaysBundle?

```ts
optional alwaysBundle:
  | Arrayable<string | RegExp>
  | NoExternalFn;
```

Defined in: [src/features/deps.ts:44](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L44)

Force dependencies to be bundled, even if they are in `dependencies` or `peerDependencies`.

***

### neverBundle?

```ts
optional neverBundle: string | RegExp | (string | RegExp)[] | ExternalOptionFunction;
```

Defined in: [src/features/deps.ts:40](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L40)

Mark dependencies as external (not bundled).
Accepts strings, regular expressions, or Rolldown's `ExternalOption`.

***

### ~~onlyAllowBundle?~~

```ts
optional onlyAllowBundle: false | Arrayable<string | RegExp>;
```

Defined in: [src/features/deps.ts:58](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L58)

#### Deprecated

Use [onlyBundle](#onlybundle) instead.

***

### onlyBundle?

```ts
optional onlyBundle: false | Arrayable<string | RegExp>;
```

Defined in: [src/features/deps.ts:54](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L54)

Whitelist of dependencies allowed to be bundled from `node_modules`.
Throws an error if any unlisted dependency is bundled.

* `undefined` (default): Show warnings for bundled dependencies.
* `false`: Suppress all warnings about bundled dependencies.

Note: Be sure to include all required sub-dependencies as well.

***

### skipNodeModulesBundle?

```ts
optional skipNodeModulesBundle: boolean;
```

Defined in: [src/features/deps.ts:66](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L66)

Skip bundling all `node_modules` dependencies.

**Note:** This option cannot be used together with `alwaysBundle`.

#### Default

```ts
false
```

---

---
url: /reference/api/Interface.DevtoolsOptions.md
---
# Interface: DevtoolsOptions

Defined in: [src/features/devtools.ts:5](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/devtools.ts#L5)

## Extends

* `NonNullable`<`InputOptions`\[`"devtools"`]>

## Properties

### clean?

```ts
optional clean: boolean;
```

Defined in: [src/features/devtools.ts:18](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/devtools.ts#L18)

Clean devtools stale sessions.

#### Default

```ts
true
```

***

### sessionId?

```ts
optional sessionId: string;
```

Defined in: node\_modules/.pnpm/rolldown@1.0.0-rc.9/node\_modules/rolldown/dist/shared/define-config-cG45vHwf.d.mts:3700

#### Inherited from

```ts
NonNullable.sessionId
```

***

### ui?

```ts
optional ui: boolean | Partial<StartOptions>;
```

Defined in: [src/features/devtools.ts:11](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/devtools.ts#L11)

**\[experimental]** Enable devtools integration. `@vitejs/devtools` must be installed as a dependency.

Defaults to true, if `@vitejs/devtools` is installed.

---

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

---

---
url: /reference/api/Interface.ExeOptions.md
---
# Interface: ExeOptions

Defined in: [src/features/exe.ts:16](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L16)

## Extends

* `ExeExtensionOptions`

## Properties

### fileName?

```ts
optional fileName: string | (chunk) => string;
```

Defined in: [src/features/exe.ts:22](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L22)

Output file name without any suffix or extension.
For example, do not include `.exe`, platform suffixes, or architecture suffixes.

***

### outDir?

```ts
optional outDir: string;
```

Defined in: [src/features/exe.ts:27](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L27)

Output directory for executables.

#### Default

```ts
'build'
```

***

### seaConfig?

```ts
optional seaConfig: Omit<SeaConfig, "main" | "output" | "mainFormat">;
```

Defined in: [src/features/exe.ts:17](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L17)

***

### targets?

```ts
optional targets: ExeTarget[];
```

Defined in: [packages/exe/src/platform.ts:41](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/packages/exe/src/platform.ts#L41)

Cross-platform targets for building executables.
Requires `@tsdown/exe` to be installed.
When specified, builds an executable for each target platform/arch combination.

#### Example

```ts
targets: [
  { platform: 'linux', arch: 'x64', nodeVersion: '25.7.0' },
  { platform: 'darwin', arch: 'arm64', nodeVersion: '25.7.0' },
  { platform: 'win', arch: 'x64', nodeVersion: '25.7.0' },
]
```

#### Inherited from

```ts
ExeExtensionOptions.targets
```

---

---
url: /reference/api/Interface.ExportsOptions.md
---
# Interface: ExportsOptions

Defined in: [src/features/pkg/exports.ts:16](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/pkg/exports.ts#L16)

## Properties

### all?

```ts
optional all: boolean;
```

Defined in: [src/features/pkg/exports.ts:33](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/pkg/exports.ts#L33)

Exports for all files.

***

### customExports?

```ts
optional customExports:
  | Record<string, any>
| (exports, context) => Awaitable<Record<string, any>>;
```

Defined in: [src/features/pkg/exports.ts:78](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/pkg/exports.ts#L78)

Specifies custom exports to add to the package exports in addition to the ones generated by tsdown.
Use this to add additional exports in the exported package, such as workers or assets.

#### Examples

```ts
customExports(exports) {
  exports['./worker.js'] = './dist/worker.js';
  return exports;
}
```

```jsonc
{
  "customExports": {
    "./worker.js": {
      "types": "./dist/worker.d.ts",
      "default": "./dist/worker.js",
    },
  },
}
```

***

### devExports?

```ts
optional devExports: string | boolean;
```

Defined in: [src/features/pkg/exports.ts:22](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/pkg/exports.ts#L22)

Generate exports that link to source code during development.

* string: add as a custom condition.
* true: all conditions point to source files, and add dist exports to `publishConfig`.

***

### exclude?

```ts
optional exclude: (string | RegExp)[];
```

Defined in: [src/features/pkg/exports.ts:44](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/pkg/exports.ts#L44)

Specifies file patterns (as glob patterns or regular expressions) to exclude from package exports.
Use this to prevent certain files from being included in the exported package, such as test files, binaries, or internal utilities.

**Note:** Do not include file extensions, and paths should be relative to the dist directory.

#### Example

```ts
exclude: ['cli', '**/*.test', /internal/]
```

***

### inlinedDependencies?

```ts
optional inlinedDependencies: boolean;
```

Defined in: [src/features/pkg/exports.ts:96](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/pkg/exports.ts#L96)

Generate `inlinedDependencies` field in package.json.
Lists dependencies that are physically inlined into the bundle with their exact versions.

#### Default

```ts
true
```

#### See

<https://github.com/e18e/ecosystem-issues/issues/237>

***

### legacy?

```ts
optional legacy: boolean;
```

Defined in: [src/features/pkg/exports.ts:54](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/pkg/exports.ts#L54)

Generate legacy fields (`main` and `module`) for older Node.js and bundlers
that do not support package `exports` field.

Defaults to false, if only ESM builds are included, true otherwise.

#### See

<https://github.com/publint/publint/issues/24>

***

### packageJson?

```ts
optional packageJson: boolean;
```

Defined in: [src/features/pkg/exports.ts:28](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/pkg/exports.ts#L28)

Exports for package.json file.

#### Default

```ts
true
```

---

---
url: /reference/api/Interface.InlineConfig.md
---
# Interface: InlineConfig

Defined in: [src/config/types.ts:602](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L602)

Options for tsdown.

## Extends

* [`UserConfig`](Interface.UserConfig.md)

## Properties

### alias?

```ts
optional alias: Record<string, string>;
```

Defined in: [src/config/types.ts:178](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L178)

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`alias`](Interface.UserConfig.md#alias)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`attw`](Interface.UserConfig.md#attw)

***

### banner?

```ts
optional banner: ChunkAddon;
```

Defined in: [src/config/types.ts:370](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L370)

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`banner`](Interface.UserConfig.md#banner)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`bundle`](Interface.UserConfig.md#bundle)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`checks`](Interface.UserConfig.md#checks)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`cjsDefault`](Interface.UserConfig.md#cjsdefault)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`clean`](Interface.UserConfig.md#clean)

***

### config?

```ts
optional config: string | boolean;
```

Defined in: [src/config/types.ts:606](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L606)

Config file path

***

### configLoader?

```ts
optional configLoader: "auto" | "native" | "unrun";
```

Defined in: [src/config/types.ts:612](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L612)

Config loader to use. It can only be set via CLI or API.

#### Default

```ts
'auto'
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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`copy`](Interface.UserConfig.md#copy)

***

### css?

```ts
optional css: CssOptions;
```

Defined in: [src/config/types.ts:556](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L556)

**\[experimental]** CSS options.
Requires `@tsdown/css` to be installed.

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`css`](Interface.UserConfig.md#css)

***

### customLogger?

```ts
optional customLogger: Logger;
```

Defined in: [src/config/types.ts:461](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L461)

Custom logger.

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`customLogger`](Interface.UserConfig.md#customlogger)

***

### cwd?

```ts
optional cwd: string;
```

Defined in: [src/config/types.ts:439](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L439)

The working directory of the config file.

* Defaults to `process.cwd()` for root config.
* Defaults to the package directory for workspace config.

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`cwd`](Interface.UserConfig.md#cwd)

***

### define?

```ts
optional define: Record<string, string>;
```

Defined in: [src/config/types.ts:247](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L247)

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`define`](Interface.UserConfig.md#define)

***

### deps?

```ts
optional deps: DepsConfig;
```

Defined in: [src/config/types.ts:158](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L158)

Dependency handling options.

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`deps`](Interface.UserConfig.md#deps)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`devtools`](Interface.UserConfig.md#devtools)

***

### dts?

```ts
optional dts: WithEnabled<DtsOptions>;
```

Defined in: [src/config/types.ts:506](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L506)

Enables generation of TypeScript declaration files (`.d.ts`).

By default, this option is auto-detected based on your project's `package.json`:

* If [exe](Interface.UserConfig.md#exe) is enabled, declaration file generation is disabled by default.
* If the `types` field is present, or if the main `exports` contains a `types` entry, declaration file generation is enabled by default.
* Otherwise, declaration file generation is disabled by default.

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`dts`](Interface.UserConfig.md#dts)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`entry`](Interface.UserConfig.md#entry)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`env`](Interface.UserConfig.md#env)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`envFile`](Interface.UserConfig.md#envfile)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`envPrefix`](Interface.UserConfig.md#envprefix)

***

### exe?

```ts
optional exe: WithEnabled<ExeOptions>;
```

Defined in: [src/config/types.ts:593](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L593)

**\[experimental]** Bundle as executable using Node.js SEA (Single Executable Applications).

This will bundle the output into a single executable file using Node.js SEA.
Note that this is only supported on Node.js 25.7.0 and later, and is not supported in Bun or Deno.

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`exe`](Interface.UserConfig.md#exe)

***

### exports?

```ts
optional exports: WithEnabled<ExportsOptions>;
```

Defined in: [src/config/types.ts:550](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L550)

Generate package exports for `package.json`.

This will set the `main`, `module`, `types`, `exports` fields in `package.json`
to point to the generated files.

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`exports`](Interface.UserConfig.md#exports)

***

### ~~external?~~

```ts
optional external: string | RegExp | (string | RegExp)[] | ExternalOptionFunction;
```

Defined in: [src/config/types.ts:163](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L163)

#### Deprecated

Use `deps.neverBundle` instead.

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`external`](Interface.UserConfig.md#external)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`failOnWarn`](Interface.UserConfig.md#failonwarn)

***

### filter?

```ts
optional filter: RegExp | Arrayable<string>;
```

Defined in: [src/config/types.ts:617](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L617)

Filter configs by cwd or name.

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`fixedExtension`](Interface.UserConfig.md#fixedextension)

***

### footer?

```ts
optional footer: ChunkAddon;
```

Defined in: [src/config/types.ts:369](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L369)

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`footer`](Interface.UserConfig.md#footer)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`format`](Interface.UserConfig.md#format)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`fromVite`](Interface.UserConfig.md#fromvite)

***

### globalName?

```ts
optional globalName: string;
```

Defined in: [src/config/types.ts:339](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L339)

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`globalName`](Interface.UserConfig.md#globalname)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`globImport`](Interface.UserConfig.md#globimport)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`hash`](Interface.UserConfig.md#hash)

***

### hooks?

```ts
optional hooks:
  | Partial<TsdownHooks>
| (hooks) => Awaitable<void>;
```

Defined in: [src/config/types.ts:583](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L583)

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`hooks`](Interface.UserConfig.md#hooks)

***

### ignoreWatch?

```ts
optional ignoreWatch: Arrayable<string | RegExp>;
```

Defined in: [src/config/types.ts:476](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L476)

Files or patterns to not watch while in watch mode.

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`ignoreWatch`](Interface.UserConfig.md#ignorewatch)

***

### ~~injectStyle?~~

```ts
optional injectStyle: boolean;
```

Defined in: [src/config/types.ts:561](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L561)

#### Deprecated

Use `css.inject` instead.

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`injectStyle`](Interface.UserConfig.md#injectstyle)

***

### ~~inlineOnly?~~

```ts
optional inlineOnly: false | Arrayable<string | RegExp>;
```

Defined in: [src/config/types.ts:171](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L171)

#### Deprecated

Use `deps.onlyBundle` instead.

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`inlineOnly`](Interface.UserConfig.md#inlineonly)

***

### inputOptions?

```ts
optional inputOptions:
  | InputOptions
| (options, format, context) => Awaitable<void | InputOptions | null>;
```

Defined in: [src/config/types.ts:319](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L319)

Use with caution; ensure you understand the implications.

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`inputOptions`](Interface.UserConfig.md#inputoptions)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`loader`](Interface.UserConfig.md#loader)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`logLevel`](Interface.UserConfig.md#loglevel)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`minify`](Interface.UserConfig.md#minify)

***

### name?

```ts
optional name: string;
```

Defined in: [src/config/types.ts:446](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L446)

The name to show in CLI output. This is useful for monorepos or workspaces.
When using workspace mode, this option defaults to the package name from package.json.
In non-workspace mode, this option must be set explicitly for the name to show in the CLI output.

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`name`](Interface.UserConfig.md#name)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`nodeProtocol`](Interface.UserConfig.md#nodeprotocol)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`noExternal`](Interface.UserConfig.md#noexternal)

***

### onSuccess?

```ts
optional onSuccess: string | (config, signal) => void | Promise<void>;
```

Defined in: [src/config/types.ts:494](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L494)

You can specify command to be executed after a successful build, specially useful for Watch mode

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`onSuccess`](Interface.UserConfig.md#onsuccess)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`outDir`](Interface.UserConfig.md#outdir)

***

### outExtensions?

```ts
optional outExtensions: OutExtensionFactory;
```

Defined in: [src/config/types.ts:408](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L408)

Custom extensions for output files.
`fixedExtension` will be overridden by this option.

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`outExtensions`](Interface.UserConfig.md#outextensions)

***

### outputOptions?

```ts
optional outputOptions:
  | OutputOptions
| (options, format, context) => Awaitable<void | OutputOptions | null>;
```

Defined in: [src/config/types.ts:424](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L424)

Use with caution; ensure you understand the implications.

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`outputOptions`](Interface.UserConfig.md#outputoptions)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`platform`](Interface.UserConfig.md#platform)

***

### plugins?

```ts
optional plugins: RolldownPluginOption<any>;
```

Defined in: [src/config/types.ts:314](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L314)

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`plugins`](Interface.UserConfig.md#plugins)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`publicDir`](Interface.UserConfig.md#publicdir)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`publint`](Interface.UserConfig.md#publint)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`removeNodeProtocol`](Interface.UserConfig.md#removenodeprotocol)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`report`](Interface.UserConfig.md#report)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`root`](Interface.UserConfig.md#root)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`shims`](Interface.UserConfig.md#shims)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`skipNodeModulesBundle`](Interface.UserConfig.md#skipnodemodulesbundle)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`sourcemap`](Interface.UserConfig.md#sourcemap)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`target`](Interface.UserConfig.md#target)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`treeshake`](Interface.UserConfig.md#treeshake)

***

### tsconfig?

```ts
optional tsconfig: string | boolean;
```

Defined in: [src/config/types.ts:179](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L179)

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`tsconfig`](Interface.UserConfig.md#tsconfig)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`unbundle`](Interface.UserConfig.md#unbundle)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`unused`](Interface.UserConfig.md#unused)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`watch`](Interface.UserConfig.md#watch)

***

### workspace?

```ts
optional workspace: true | Arrayable<string> | Workspace;
```

Defined in: [src/config/types.ts:599](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L599)

**\[experimental]** Enable workspace mode.
This allows you to build multiple packages in a monorepo.

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`workspace`](Interface.UserConfig.md#workspace)

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

#### Inherited from

[`UserConfig`](Interface.UserConfig.md).[`write`](Interface.UserConfig.md#write)

---

---
url: /reference/api/Interface.Logger.md
---
# Interface: Logger

Defined in: [src/utils/logger.ts:24](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/logger.ts#L24)

## Properties

### clearScreen()

```ts
clearScreen: (type) => void;
```

Defined in: [src/utils/logger.ts:32](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/logger.ts#L32)

#### Parameters

##### type

`LogType`

#### Returns

`void`

***

### error()

```ts
error: (...args) => void;
```

Defined in: [src/utils/logger.ts:30](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/logger.ts#L30)

#### Parameters

##### args

...`any`\[]

#### Returns

`void`

***

### info()

```ts
info: (...args) => void;
```

Defined in: [src/utils/logger.ts:27](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/logger.ts#L27)

#### Parameters

##### args

...`any`\[]

#### Returns

`void`

***

### level

```ts
level: LogLevel
```

Defined in: [src/utils/logger.ts:25](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/logger.ts#L25)

***

### options?

```ts
optional options: LoggerOptions;
```

Defined in: [src/utils/logger.ts:26](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/logger.ts#L26)

***

### success()

```ts
success: (...args) => void;
```

Defined in: [src/utils/logger.ts:31](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/logger.ts#L31)

#### Parameters

##### args

...`any`\[]

#### Returns

`void`

***

### warn()

```ts
warn: (...args) => void;
```

Defined in: [src/utils/logger.ts:28](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/logger.ts#L28)

#### Parameters

##### args

...`any`\[]

#### Returns

`void`

***

### warnOnce()

```ts
warnOnce: (...args) => void;
```

Defined in: [src/utils/logger.ts:29](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/logger.ts#L29)

#### Parameters

##### args

...`any`\[]

#### Returns

`void`

---

---
url: /reference/api/Interface.OutExtensionContext.md
---
# Interface: OutExtensionContext

Defined in: [src/features/output.ts:15](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/output.ts#L15)

## Properties

### format

```ts
format: InternalModuleFormat
```

Defined in: [src/features/output.ts:17](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/output.ts#L17)

***

### options

```ts
options: InputOptions
```

Defined in: [src/features/output.ts:16](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/output.ts#L16)

***

### pkgType?

```ts
optional pkgType: PackageType;
```

Defined in: [src/features/output.ts:19](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/output.ts#L19)

"type" field in project's package.json

---

---
url: /reference/api/Interface.OutExtensionObject.md
---
# Interface: OutExtensionObject

Defined in: [src/features/output.ts:21](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/output.ts#L21)

## Properties

### dts?

```ts
optional dts: string;
```

Defined in: [src/features/output.ts:23](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/output.ts#L23)

***

### js?

```ts
optional js: string;
```

Defined in: [src/features/output.ts:22](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/output.ts#L22)

---

---
url: /reference/api/Interface.PackageJsonWithPath.md
---
# Interface: PackageJsonWithPath

Defined in: [src/utils/package.ts:9](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/package.ts#L9)

## Extends

* `PackageJson`

## Indexable

```ts
[key: string]: any
```

## Properties

### author?

```ts
optional author: PackageJsonPerson;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:175

The “author” is one person.

#### Inherited from

```ts
PackageJson.author
```

***

### bin?

```ts
optional bin: string | Record<string, string>;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:207

A map of command name to local file name. On install, npm will symlink that file into `prefix/bin` for global installs, or `./node_modules/.bin/` for local installs.

#### Inherited from

```ts
PackageJson.bin
```

***

### browser?

```ts
optional browser: string | Record<string, string | false>;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:199

If your module is meant to be used client-side the browser field should be used instead of the main field. This is helpful to hint users that it might rely on primitives that aren’t available in Node.js modules. (e.g. window)

#### Inherited from

```ts
PackageJson.browser
```

***

### bugs?

```ts
optional bugs:
  | string
  | {
  email?: string;
  url?: string;
};
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:144

The url to your project’s issue tracker and / or the email address to which issues should be reported. These are helpful for people who encounter issues with your package.

#### Inherited from

```ts
PackageJson.bugs
```

***

### contributors?

```ts
optional contributors: PackageJsonPerson[];
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:179

“contributors” is an array of people.

#### Inherited from

```ts
PackageJson.contributors
```

***

### cpu?

```ts
optional cpu: string[];
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:325

If your code only runs on certain cpu architectures, you can specify which ones.

```json
{
  "cpu": ["x64", "ia32"]
}
```

Like the `os` option, you can also block architectures:

```json
{
  "cpu": ["!arm", "!mips"]
}
```

The host architecture is determined by `process.arch`

#### Inherited from

```ts
PackageJson.cpu
```

***

### dependencies?

```ts
optional dependencies: Record<string, string>;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:215

Dependencies are specified in a simple object that maps a package name to a version range. The version range is a string which has one or more space-separated descriptors. Dependencies can also be identified with a tarball or git URL.

#### Inherited from

```ts
PackageJson.dependencies
```

***

### description?

```ts
optional description: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:132

Put a description in it. It’s a string. This helps people discover your package, as it’s listed in `npm search`.

#### Inherited from

```ts
PackageJson.description
```

***

### devDependencies?

```ts
optional devDependencies: Record<string, string>;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:220

If someone is planning on downloading and using your module in their program, then they probably don’t want or need to download and build the external test or documentation framework that you use.
In this case, it’s best to map these additional items in a `devDependencies` object.

#### Inherited from

```ts
PackageJson.devDependencies
```

***

### exports?

```ts
optional exports: PackageJsonExports;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:262

Alternate and extensible alternative to "main" entry point.

When using `{type: "module"}`, any ESM module file MUST end with `.mjs` extension.

Docs:

* https://nodejs.org/docs/latest-v14.x/api/esm.html#esm\_exports\_sugar

#### Since

Node.js v12.7

#### Inherited from

```ts
PackageJson.exports
```

***

### files?

```ts
optional files: string[];
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:189

The optional `files` field is an array of file patterns that describes the entries to be included when your package is installed as a dependency. File patterns follow a similar syntax to `.gitignore`, but reversed: including a file, directory, or glob pattern (`*`, `**/*`, and such) will make it so that file is included in the tarball when it’s packed. Omitting the field will make it default to `["*"]`, which means it will include all files.

#### Inherited from

```ts
PackageJson.files
```

***

### funding?

```ts
optional funding: PackageJsonFunding | PackageJsonFunding[];
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:185

An object containing a URL that provides up-to-date information
about ways to help fund development of your package,
a string URL, or an array of objects and string URLs

#### Inherited from

```ts
PackageJson.funding
```

***

### homepage?

```ts
optional homepage: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:140

The url to the project homepage.

#### Inherited from

```ts
PackageJson.homepage
```

***

### imports?

```ts
optional imports: Record<string, string | Record<string, string>>;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:267

Docs:

* https://nodejs.org/api/packages.html#imports

#### Inherited from

```ts
PackageJson.imports
```

***

### keywords?

```ts
optional keywords: string[];
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:136

Put keywords in it. It’s an array of strings. This helps people discover your package as it’s listed in `npm search`.

#### Inherited from

```ts
PackageJson.keywords
```

***

### license?

```ts
optional license: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:151

You should specify a license for your package so that people know how they are permitted to use it, and any restrictions you’re placing on it.

#### Inherited from

```ts
PackageJson.license
```

***

### main?

```ts
optional main: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:195

The main field is a module ID that is the primary entry point to your program. That is, if your package is named `foo`, and a user installs it, and then does `require("foo")`, then your main module’s exports object will be returned.
This should be a module ID relative to the root of your package folder.
For most modules, it makes the most sense to have a main script and often not much else.

#### Inherited from

```ts
PackageJson.main
```

***

### man?

```ts
optional man: string | string[];
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:211

Specify either a single file or an array of filenames to put in place for the `man` program to find.

#### Inherited from

```ts
PackageJson.man
```

***

### module?

```ts
optional module: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:241

Non-Standard Node.js alternate entry-point to main.
An initial implementation for supporting CJS packages (from main), and use module for ESM modules.

#### Inherited from

```ts
PackageJson.module
```

***

### name?

```ts
optional name: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:124

The name is what your thing is called.
Some rules:

* The name must be less than or equal to 214 characters. This includes the scope for scoped packages.
* The name can’t start with a dot or an underscore.
* New packages must not have uppercase letters in the name.
* The name ends up being part of a URL, an argument on the command line, and a folder name. Therefore, the name can’t contain any non-URL-safe characters.

#### Inherited from

```ts
PackageJson.name
```

***

### optionalDependencies?

```ts
optional optionalDependencies: Record<string, string>;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:224

If a dependency can be used, but you would like npm to proceed if it cannot be found or fails to install, then you may put it in the `optionalDependencies` object. This is a map of package name to version or url, just like the `dependencies` object. The difference is that build failures do not cause installation to fail.

#### Inherited from

```ts
PackageJson.optionalDependencies
```

***

### os?

```ts
optional os: string[];
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:309

You can specify which operating systems your module will run on:

```json
{
  "os": ["darwin", "linux"]
}
```

You can also block instead of allowing operating systems, just prepend the blocked os with a '!':

```json
{
  "os": ["!win32"]
}
```

The host operating system is determined by `process.platform`
It is allowed to both block and allow an item, although there isn't any good reason to do this.

#### Inherited from

```ts
PackageJson.os
```

***

### packageJsonPath

```ts
packageJsonPath: string
```

Defined in: [src/utils/package.ts:10](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/package.ts#L10)

***

### packageManager?

```ts
optional packageManager: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:376

See: https://nodejs.org/api/packages.html#packagemanager
This field defines which package manager is expected to be used when working on the current project.
Should be of the format: `<name>@<version>[#hash]`

#### Inherited from

```ts
PackageJson.packageManager
```

***

### peerDependencies?

```ts
optional peerDependencies: Record<string, string>;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:228

In some cases, you want to express the compatibility of your package with a host tool or library, while not necessarily doing a `require` of this host. This is usually referred to as a plugin. Notably, your module may be exposing a specific interface, expected and specified by the host documentation.

#### Inherited from

```ts
PackageJson.peerDependencies
```

***

### private?

```ts
optional private: boolean;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:171

If you set `"private": true` in your package.json, then npm will refuse to publish it.

#### Inherited from

```ts
PackageJson.private
```

***

### publishConfig?

```ts
optional publishConfig: object & Pick<PackageJson,
  | "exports"
  | "browser"
  | "main"
  | "module"
  | "unpkg"
  | "bin"
  | "types"
  | "typings"
  | "typesVersions"
  | "os"
| "cpu">;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:329

This is a set of config values that will be used at publish-time.

#### Type Declaration

##### access?

```ts
optional access: "public" | "restricted";
```

The access level that will be used if the package is published.

##### directory?

```ts
optional directory: string;
```

**pnpm-only**

You also can use the field `publishConfig.directory` to customize
the published subdirectory relative to the current `package.json`.

It is expected to have a modified version of the current package in
the specified directory (usually using third party build tools).

##### executableFiles?

```ts
optional executableFiles: string[];
```

**pnpm-only**

By default, for portability reasons, no files except those listed in
the bin field will be marked as executable in the resulting package
archive. The executableFiles field lets you declare additional fields
that must have the executable flag (+x) set even if
they aren't directly accessible through the bin field.

##### linkDirectory?

```ts
optional linkDirectory: boolean;
```

**pnpm-only**

When set to `true`, the project will be symlinked from the
`publishConfig.directory` location during local development.

###### Default

```ts
true
```

##### registry?

```ts
optional registry: string;
```

The registry that will be used if the package is published.

##### tag?

```ts
optional tag: string;
```

The tag that will be used if the package is published.

#### Inherited from

```ts
PackageJson.publishConfig
```

***

### repository?

```ts
optional repository:
  | string
  | {
  directory?: string;
  type: string;
  url: string;
};
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:156

Specify the place where your code lives. This is helpful for people who want to contribute. If the git repo is on GitHub, then the `npm docs` command will be able to find you.
For GitHub, GitHub gist, Bitbucket, or GitLab repositories you can use the same shortcut syntax you use for npm install:

#### Type Declaration

`string`

```ts
{
  directory?: string;
  type: string;
  url: string;
}
```

#### directory?

```ts
optional directory: string;
```

If the `package.json` for your package is not in the root directory (for example if it is part of a monorepo), you can specify the directory in which it lives:

#### type

```ts
type: string
```

#### url

```ts
url: string
```

#### Inherited from

```ts
PackageJson.repository
```

***

### scripts?

```ts
optional scripts: PackageJsonScripts;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:167

The `scripts` field is a dictionary containing script commands that are run at various times in the lifecycle of your package.

#### Inherited from

```ts
PackageJson.scripts
```

***

### type?

```ts
optional type: "commonjs" | "module";
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:251

Make main entry-point be loaded as an ESM module, support "export" syntax instead of "require"

Docs:

* https://nodejs.org/docs/latest-v14.x/api/esm.html#esm\_package\_json\_type\_field

#### Default

```ts
'commonjs'
```

#### Since

Node.js v14

#### Inherited from

```ts
PackageJson.type
```

***

### types?

```ts
optional types: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:232

TypeScript typings, typically ending by `.d.ts`.

#### Inherited from

```ts
PackageJson.types
```

***

### typesVersions?

```ts
optional typesVersions: Record<string, Record<string, string[]>>;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:292

The field is used to specify different TypeScript declaration files for
different versions of TypeScript, allowing for version-specific type definitions.

#### Inherited from

```ts
PackageJson.typesVersions
```

***

### typings?

```ts
optional typings: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:236

This field is synonymous with `types`.

#### Inherited from

```ts
PackageJson.typings
```

***

### unpkg?

```ts
optional unpkg: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:203

The `unpkg` field is used to specify the URL to a UMD module for your package. This is used by default in the unpkg.com CDN service.

#### Inherited from

```ts
PackageJson.unpkg
```

***

### version?

```ts
optional version: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:128

Version must be parseable by `node-semver`, which is bundled with npm as a dependency. (`npm install semver` to use it yourself.)

#### Inherited from

```ts
PackageJson.version
```

***

### workspaces?

```ts
optional workspaces:
  | string[]
  | {
  nohoist?: string[];
  packages?: string[];
};
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:274

The field is used to define a set of sub-packages (or workspaces) within a monorepo.

This field is an array of glob patterns or an object with specific configurations for managing
multiple packages in a single repository.

#### Type Declaration

`string`\[]

```ts
{
  nohoist?: string[];
  packages?: string[];
}
```

#### nohoist?

```ts
optional nohoist: string[];
```

Packages to block from hoisting to the workspace root.
Uses glob patterns to match module paths in the dependency tree.

Docs:

* https://classic.yarnpkg.com/blog/2018/02/15/nohoist/

#### packages?

```ts
optional packages: string[];
```

Workspace package paths. Glob patterns are supported.

#### Inherited from

```ts
PackageJson.workspaces
```

---

---
url: /reference/api/Interface.PublintOptions.md
---
# Interface: PublintOptions

Defined in: [src/features/pkg/publint.ts:11](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/pkg/publint.ts#L11)

## Extends

* `Omit`<`Options`, `"pack"` | `"pkgDir"`>

## Properties

### level?

```ts
optional level: "error" | "suggestion" | "warning";
```

Defined in: node\_modules/.pnpm/publint@0.3.18/node\_modules/publint/src/index.d.ts:159

The level of messages to log (default: `'suggestion'`).

* `suggestion`: logs all messages
* `warning`: logs only `warning` and `error` messages
* `error`: logs only `error` messages

#### Inherited from

```ts
Omit.level
```

***

### strict?

```ts
optional strict: boolean;
```

Defined in: node\_modules/.pnpm/publint@0.3.18/node\_modules/publint/src/index.d.ts:193

Report warnings as errors. This runs before `level` filters the result, which means that if
`level` is set to `'error'`, all warnings (elevated as errors) will still be reported.

#### Inherited from

```ts
Omit.strict
```

---

---
url: /reference/api/Interface.ReportOptions.md
---
# Interface: ReportOptions

Defined in: [src/features/report.ts:30](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/report.ts#L30)

## Properties

### brotli?

```ts
optional brotli: boolean;
```

Defined in: [src/features/report.ts:45](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/report.ts#L45)

Enable/disable brotli-compressed size reporting.
Compressing large output files can be slow, so disabling this may increase build performance for large projects.

#### Default

```ts
false
```

***

### gzip?

```ts
optional gzip: boolean;
```

Defined in: [src/features/report.ts:37](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/report.ts#L37)

Enable/disable gzip-compressed size reporting.
Compressing large output files can be slow, so disabling this may increase build performance for large projects.

#### Default

```ts
true
```

***

### maxCompressSize?

```ts
optional maxCompressSize: number;
```

Defined in: [src/features/report.ts:51](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/report.ts#L51)

Skip reporting compressed size for files larger than this size.

#### Default

```ts
1_000_000 // 1MB
```

---

---
url: /reference/api/Interface.ResolvedDepsConfig.md
---
# Interface: ResolvedDepsConfig

Defined in: [src/features/deps.ts:69](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L69)

## Properties

### alwaysBundle?

```ts
optional alwaysBundle: NoExternalFn;
```

Defined in: [src/features/deps.ts:71](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L71)

***

### neverBundle?

```ts
optional neverBundle: string | RegExp | (string | RegExp)[] | ExternalOptionFunction;
```

Defined in: [src/features/deps.ts:70](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L70)

***

### onlyBundle?

```ts
optional onlyBundle: false | (string | RegExp)[];
```

Defined in: [src/features/deps.ts:72](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L72)

***

### skipNodeModulesBundle

```ts
skipNodeModulesBundle: boolean
```

Defined in: [src/features/deps.ts:73](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L73)

---

---
url: /reference/api/Interface.RolldownContext.md
---
# Interface: RolldownContext

Defined in: [src/features/hooks.ts:13](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/hooks.ts#L13)

## Properties

### buildOptions

```ts
buildOptions: BuildOptions
```

Defined in: [src/features/hooks.ts:14](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/hooks.ts#L14)

---

---
url: /reference/api/Interface.SeaConfig.md
---
# Interface: SeaConfig

Defined in: [src/features/exe.ts:35](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L35)

See also [Node.js SEA Documentation](https://nodejs.org/api/single-executable-applications.html#generating-single-executable-applications-with---build-sea)

Note some default values are different from Node.js defaults to optimize for typical use cases (e.g. disabling experimental warning, enabling code cache). These can be overridden.

## Properties

### assets?

```ts
optional assets: Record<string, string>;
```

Defined in: [src/features/exe.ts:50](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L50)

***

### disableExperimentalSEAWarning?

```ts
optional disableExperimentalSEAWarning: boolean;
```

Defined in: [src/features/exe.ts:42](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L42)

#### Default

```ts
true
```

***

### execArgv?

```ts
optional execArgv: string[];
```

Defined in: [src/features/exe.ts:47](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L47)

***

### execArgvExtension?

```ts
optional execArgvExtension: "env" | "none" | "cli";
```

Defined in: [src/features/exe.ts:49](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L49)

#### Default

```ts
'env'
```

***

### executable?

```ts
optional executable: string;
```

Defined in: [src/features/exe.ts:38](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L38)

Optional, if not specified, uses the current Node.js binary

***

### main?

```ts
optional main: string;
```

Defined in: [src/features/exe.ts:36](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L36)

***

### mainFormat?

```ts
optional mainFormat: "commonjs" | "module";
```

Defined in: [src/features/exe.ts:40](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L40)

***

### output?

```ts
optional output: string;
```

Defined in: [src/features/exe.ts:39](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L39)

***

### useCodeCache?

```ts
optional useCodeCache: boolean;
```

Defined in: [src/features/exe.ts:46](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L46)

#### Default

```ts
false
```

***

### useSnapshot?

```ts
optional useSnapshot: boolean;
```

Defined in: [src/features/exe.ts:44](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L44)

#### Default

```ts
false
```

---

---
url: /reference/api/Interface.TsdownBundle.md
---
# Interface: TsdownBundle

Defined in: [src/utils/chunks.ts:7](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/chunks.ts#L7)

## Extends

* `AsyncDisposable`

## Properties

### chunks

```ts
chunks: RolldownChunk[];
```

Defined in: [src/utils/chunks.ts:8](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/chunks.ts#L8)

***

### config

```ts
config: ResolvedConfig
```

Defined in: [src/utils/chunks.ts:9](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/chunks.ts#L9)

***

### inlinedDeps

```ts
inlinedDeps: Map<string, Set<string>>
```

Defined in: [src/utils/chunks.ts:10](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/chunks.ts#L10)

## Methods

### \[asyncDispose]\()

```ts
asyncDispose: PromiseLike<void>
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.esnext.disposable.d.ts:40

#### Returns

`PromiseLike`<`void`>

#### Inherited from

```ts
AsyncDisposable.[asyncDispose]
```

---

---
url: /reference/api/Interface.TsdownHooks.md
---
# Interface: TsdownHooks

Defined in: [src/features/hooks.ts:20](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/hooks.ts#L20)

Hooks for tsdown.

## Properties

### build:before()

```ts
build:before: (ctx) => void | Promise<void>;
```

Defined in: [src/features/hooks.ts:31](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/hooks.ts#L31)

Invoked before each Rolldown build.
For dual-format builds, this hook is called for each format.
Useful for configuring or modifying the build context before bundling.

#### Parameters

##### ctx

[`BuildContext`](Interface.BuildContext.md) & [`RolldownContext`](Interface.RolldownContext.md)

#### Returns

`void` | `Promise`<`void`>

***

### build:done()

```ts
build:done: (ctx) => void | Promise<void>;
```

Defined in: [src/features/hooks.ts:36](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/hooks.ts#L36)

Invoked after each tsdown build completes.
Use this hook for cleanup or post-processing tasks.

#### Parameters

##### ctx

[`BuildContext`](Interface.BuildContext.md) & `object`

#### Returns

`void` | `Promise`<`void`>

***

### build:prepare()

```ts
build:prepare: (ctx) => void | Promise<void>;
```

Defined in: [src/features/hooks.ts:25](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/hooks.ts#L25)

Invoked before each tsdown build starts.
Use this hook to perform setup or preparation tasks.

#### Parameters

##### ctx

[`BuildContext`](Interface.BuildContext.md)

#### Returns

`void` | `Promise`<`void`>

---

---
url: /reference/api/Interface.UnusedOptions.md
---
# Interface: UnusedOptions

Defined in: node\_modules/.pnpm/unplugin-unused@0.5.7/node\_modules/unplugin-unused/dist/options-DC5dXKG8.d.mts:5

## Properties

### depKinds?

```ts
optional depKinds: DepKind[];
```

Defined in: node\_modules/.pnpm/unplugin-unused@0.5.7/node\_modules/unplugin-unused/dist/options-DC5dXKG8.d.mts:22

#### Default

```ts
;['dependencies', 'peerDependencies']
```

***

### exclude?

```ts
optional exclude: FilterPattern;
```

Defined in: node\_modules/.pnpm/unplugin-unused@0.5.7/node\_modules/unplugin-unused/dist/options-DC5dXKG8.d.mts:8

***

### ignore?

```ts
optional ignore: string[] | Partial<Record<DepKind, string[]>>;
```

Defined in: node\_modules/.pnpm/unplugin-unused@0.5.7/node\_modules/unplugin-unused/dist/options-DC5dXKG8.d.mts:9

***

### include?

```ts
optional include: FilterPattern;
```

Defined in: node\_modules/.pnpm/unplugin-unused@0.5.7/node\_modules/unplugin-unused/dist/options-DC5dXKG8.d.mts:7

***

### level?

```ts
optional level: "error" | "warning";
```

Defined in: node\_modules/.pnpm/unplugin-unused@0.5.7/node\_modules/unplugin-unused/dist/options-DC5dXKG8.d.mts:18

Specifies the severity level of the check.

* `'error'`: Causes the build to fail.
* `'warning'`: Displays a warning in the console.

#### Default

```ts
'warning'
```

***

### root?

```ts
optional root: string;
```

Defined in: node\_modules/.pnpm/unplugin-unused@0.5.7/node\_modules/unplugin-unused/dist/options-DC5dXKG8.d.mts:6

---

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

---

---
url: /reference/api/Interface.Workspace.md
---
# Interface: Workspace

Defined in: [src/config/types.ts:107](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L107)

## Properties

### config?

```ts
optional config: string | boolean;
```

Defined in: [src/config/types.ts:123](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L123)

Path to the workspace configuration file.

***

### exclude?

```ts
optional exclude: Arrayable<string>;
```

Defined in: [src/config/types.ts:118](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L118)

Exclude directories from workspace.
Defaults to all `node_modules`, `dist`, `test`, `tests`, `temp`, and `tmp` directories.

***

### include?

```ts
optional include: Arrayable<string>;
```

Defined in: [src/config/types.ts:113](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L113)

Workspace directories. Glob patterns are supported.

* `auto`: Automatically detect `package.json` files in the workspace.

#### Default

```ts
'auto'
```

---

---
url: /guide.md
---
# Introduction

**tsdown** is *The Elegant Library Bundler*. Designed with simplicity and speed in mind, it provides a seamless and efficient way to bundle your TypeScript and JavaScript libraries. Whether you're building a small utility or a complex library, `tsdown` empowers you to focus on your code while it handles the bundling process with elegance.

## Why tsdown?

`tsdown` is built on top of [Rolldown](https://rolldown.rs), a cutting-edge bundler written in Rust. While Rolldown is a powerful and general-purpose tool, `tsdown` takes it a step further by providing a **complete out-of-the-box solution** for library authors.

### Key Differences Between tsdown and Rolldown

* **Simplified Configuration**: `tsdown` minimizes the need for complex configurations by offering sensible defaults tailored for library development. It provides a streamlined experience, so you can focus on your code rather than the bundling process.
* **Library-Specific Features**: Unlike Rolldown, which is designed as a general-purpose bundler, `tsdown` is optimized specifically for building libraries. It includes features like automatic TypeScript declaration generation and multiple output formats.
* **Future-Ready**: As an **official project of Rolldown**, `tsdown` is deeply integrated into its ecosystem and will continue to evolve alongside it. By leveraging Rolldown's latest advancements, `tsdown` aims to explore new possibilities for library development. Furthermore, `tsdown` is positioned to become the **foundation for [Rolldown Vite](https://github.com/vitejs/rolldown-vite)'s Library Mode**, ensuring a cohesive and robust experience for library authors in the long term.

## Plugin Ecosystem

`tsdown` supports the entire Rolldown plugin ecosystem, making it easy to extend and customize your build process. Additionally, it is compatible with most Rollup plugins, giving you access to a vast library of existing tools.

For more details, refer to the [Plugins](../advanced/plugins.md) documentation.

## What Can It Bundle?

`tsdown` is designed to handle all the essentials for modern library development:

* **TypeScript and JavaScript**: Seamlessly bundle `.ts` and `.js` files with support for modern syntax and features.
* **TypeScript Declarations**: Automatically generate declaration files (`.d.ts`) for your library.
* **Multiple Output Formats**: Generate `esm`, `cjs`, `iife`, and `umd` bundles to ensure compatibility across different environments.
* **Assets**: Include and process non-code assets like `.json` or `.wasm` files.

With its built-in support for [tree shaking](../options/tree-shaking.md), [minification](../options/minification.md), and [source maps](../options/sourcemap.md), `tsdown` ensures your library is optimized for production.

## Fast and Elegant

`tsdown` is built to be **fast**. Leveraging Rolldown's Rust-based performance, it delivers blazing-fast builds even for large projects. At the same time, it is **elegant**—offering a clean and intuitive configuration system that minimizes boilerplate and maximizes productivity.

## Getting Started

Ready to dive in? Check out the [Getting Started](./getting-started.md) guide to set up your first project with `tsdown`.

Want to use tsdown from your own scripts? See [Programmatic Usage](../advanced/programmatic-usage.md).

## Credits

`tsdown` is made possible by the open-source community and the many innovative tools in the JavaScript and TypeScript ecosystem. We extend our gratitude to all contributors and maintainers whose work has laid the foundation for this project.

### Prior Arts

* **Rollup**: Provided the original inspiration for modern JavaScript bundling and a robust plugin system.
* **esbuild**: Demonstrated the power of fast, native bundling and influenced the pursuit of performance in build tools.
* **tsup**: Inspired the out-of-the-box developer experience and many CLI options, as well as some implementation details.
* **unbuild**: Inspired the flexible hooks system now available in tsdown.
* **Rolldown**: Serves as the high-performance, Rust-based core engine that powers tsdown and enables many of its advanced features.

---

---
url: /options/log-level.md
---
# Log Level

Controlling the verbosity of logs during the bundling process helps you focus on what matters most. The recommended way to manage log output in `tsdown` is by using the `--log-level` option.

## Usage

To suppress all logs—including errors—set the log level to `silent`:

```bash
tsdown --log-level silent
```

To display only error messages, set the log level to `error`:

```bash
tsdown --log-level error
```

This is useful for CI/CD pipelines or scenarios where you want minimal or no console output.

## Available Log Levels

* `silent`: No logs are shown, including errors.
* `error`: Only error messages are shown.
* `warn`: Warnings and errors are logged.
* `info`: Informational messages, warnings, and errors are logged (default).

Choose the log level that best fits your workflow to control the amount of information displayed during the build process.

## Fail on Warnings

The `failOnWarn` option controls whether warnings cause the build to exit with a non-zero code.

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  // Always fail on warnings
  failOnWarn: true,
  // Fail on warnings only in CI
  failOnWarn: 'ci-only',
})
```

See [CI Environment](/advanced/ci) for more about CI-aware options.

---

---
url: /guide/migrate-from-tsup.md
---
# Migrate from tsup

[tsup](https://tsup.egoist.dev/) is a powerful and widely-used bundler that shares many similarities with `tsdown`. While `tsup` is built on top of [esbuild](https://esbuild.github.io/), `tsdown` leverages the power of [Rolldown](https://rolldown.rs/) to deliver a **faster** and more **powerful** bundling experience.

## Migration Guide

If you're currently using `tsup` and want to migrate to `tsdown`, the process is straightforward thanks to the dedicated `migrate` command:

```bash
npx tsdown-migrate
```

For monorepos, you can specify directories using glob patterns:

```bash
npx tsdown-migrate packages/*
```

Or specify multiple directories explicitly:

```bash
npx tsdown-migrate packages/foo packages/bar
```

> \[!WARNING]
> Please save your changes before migration. The migration process may modify your configuration files, so it's important to ensure all your changes are committed or backed up beforehand.

> \[!TIP]
> The migration tool will automatically install dependencies after migration. Make sure to run the command from within your project directory.

### Migration Options

The `migrate` command supports the following options to customize the migration process:

* `[...dirs]`: Specify directories to migrate. Supports glob patterns (e.g., `packages/*`). Defaults to the current directory if not specified.
* `--dry-run` (or `-d`): Perform a dry run to preview the migration without making any changes.

With these options, you can easily tailor the migration process to fit your specific project setup.

## Differences from tsup

While `tsdown` aims to be highly compatible with `tsup`, there are some differences to be aware of:

### Default Values

* **`format`**: Defaults to `esm`.
* **`clean`**: Enabled by default and will clean the `outDir` before each build.
* **`dts`**: Automatically enabled if your `package.json` contains a `typings` or `types` field.
* **`target`**: By default, reads from the `engines.node` field in your `package.json` if available.

### Feature Gaps

Some features available in `tsup` are not yet implemented in `tsdown`. If you find an option missing that you need, please [open an issue](https://github.com/rolldown/tsdown/issues) to let us know your requirements.

### New Features in tsdown

`tsdown` also introduces new features not available in `tsup`:

* **`nodeProtocol`**: Control how Node.js built-in module imports are handled:
  * `true`: Add `node:` prefix to built-in modules (e.g., `fs` → `node:fs`)
  * `'strip'`: Remove `node:` prefix from imports (e.g., `node:fs` → `fs`)
  * `false`: Keep imports as-is (default)

Please review your configuration after migration to ensure it matches your expectations.

## Acknowledgements

`tsdown` would not have been possible without the inspiration and contributions of the open-source community. We would like to express our heartfelt gratitude to the following:

* **[tsup](https://tsup.egoist.dev/)**: `tsdown` was heavily inspired by `tsup`, and even incorporates parts of its codebase. The simplicity and efficiency of `tsup` served as a guiding light during the development of `tsdown`.
* **[@egoist](https://github.com/egoist)**: The creator of `tsup`, whose work has significantly influenced the JavaScript and TypeScript tooling ecosystem. Thank you for your dedication and contributions to the community.

---

---
url: /options/minification.md
---
# Minification

Minification is the process of compressing your code to reduce its size and improve performance by removing unnecessary characters, such as whitespace, comments, and unused code.

You can enable minification in `tsdown` using the `--minify` option:

```bash
tsdown --minify
```

> \[!NOTE]
> The minification feature is based on [Oxc](https://oxc.rs/docs/contribute/minifier), which is currently in alpha and can still have bugs. We recommend thoroughly testing your output in production environments.

### Example

Given the following input code:

```ts [src/index.ts]
const x = 1

function hello(x: number) {
  console.log('Hello World')
  console.log(x)
}

hello(x)
```

Here are the two possible outputs, depending on whether minification is enabled:

::: code-group

```js [dist/index.mjs (without --minify)]
//#region src/index.ts
const x = 1
function hello(x$1) {
  console.log('Hello World')
  console.log(x$1)
}
hello(x)

//#endregion
```

```js [dist/index.mjs (with --minify)]
const e=1;function t(e){console.log(`Hello World`),console.log(e)}t(e);
```

:::

---

---
url: /options/output-directory.md
---
# Output Directory

By default, `tsdown` bundles your code into the `dist` directory located in the current working folder.

If you want to customize the output directory, you can use the `--out-dir` (or `-d`) option:

```bash
tsdown -d ./custom-output
```

### Example

```bash
# Default behavior: outputs to ./dist
tsdown

# Custom output directory: outputs to ./build
tsdown -d ./build
```

> \[!NOTE]
> The specified output directory will be created if it does not already exist. Ensure the directory path aligns with your project structure to avoid overwriting unintended files.

---

---
url: /options/output-format.md
---
# Output Format

By default, `tsdown` generates JavaScript code in the [ESM](https://nodejs.org/api/esm.html) (ECMAScript Module) format. However, you can specify the desired output format using the `--format` option:

```bash
tsdown --format esm # default
```

## Available Formats

* [`esm`](https://nodejs.org/api/esm.html): ECMAScript Module format, ideal for modern JavaScript environments, including browsers and Node.js.
* [`cjs`](https://nodejs.org/api/modules.html): CommonJS format, commonly used in Node.js projects.
* [`iife`](https://developer.mozilla.org/en-US/docs/Glossary/IIFE): Immediately Invoked Function Expression, suitable for embedding in `<script>` tags or standalone browser usage.
* [`umd`](https://github.com/umdjs/umd): Universal Module Definition, a format that works on AMD, CommonJS, and global variables.

### Example

```bash
# Generate ESM output (default)
tsdown --format esm

# Generate both ESM and CJS outputs
tsdown --format esm --format cjs

# Generate IIFE output for browser usage
tsdown --format iife
```

> \[!TIP]
> You can specify multiple formats in a single command to generate outputs for different environments. For example, combining `esm` and `cjs` ensures compatibility with both modern and legacy systems.

## Overriding Configuration by Format

You can override specific configuration options for each output format by setting `format` as an object in your config file. This allows you to tailor settings such as `target` or other options for each format individually.

```ts
export default defineConfig({
  entry: ['./src/index.js'],
  format: {
    esm: {
      target: ['es2015'],
    },
    cjs: {
      target: ['node20'],
    },
  },
})
```

In this example, the ESM output will target ES2015, while the CJS output will target Node.js 20. This approach gives you fine-grained control over the build process for different module formats.

---

---
url: /options/lint.md
---
# Package Validation (publint & attw)

tsdown integrates with [publint](https://publint.dev/) and [Are the types wrong?](https://arethetypeswrong.github.io/) (attw) to validate your package before publishing. These tools check for common issues in your `package.json` configuration and type definitions.

## Installation

Both tools are **optional dependencies** — you only need to install them if you want to use them:

::: code-group

```bash [publint]
npm install -D publint
```

```bash [attw]
npm install -D @arethetypeswrong/core
```

```bash [both]
npm install -D publint @arethetypeswrong/core
```

:::

## publint

[publint](https://publint.dev/) checks that your package is correctly configured for publishing. It validates `package.json` fields like `exports`, `main`, `module`, and `types` against your actual output files.

### Enable publint

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  publint: true,
})
```

### Configuration

Pass options directly to customize publint's behavior:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  publint: {
    level: 'error', // 'warning' | 'error' | 'suggestion'
  },
})
```

### CLI

```bash
tsdown --publint
```

## attw (Are the types wrong?)

[attw](https://arethetypeswrong.github.io/) verifies that your TypeScript declaration files are correct across different module resolution strategies (`node10`, `node16`, `bundler`). It catches issues like false ESM/CJS type declarations that can cause runtime errors for consumers.

### Enable attw

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  attw: true,
})
```

### Configuration

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  attw: {
    // Resolution profile:
    //   'strict'   - requires all resolutions (default)
    //   'node16'   - ignores node10 resolution failures
    //   'esm-only' - ignores CJS resolution failures
    profile: 'node16',

    // Level: 'warn' (default) or 'error' (fails the build)
    level: 'error',

    // Ignore specific problem types
    ignoreRules: ['false-cjs', 'cjs-resolves-to-esm'],
  },
})
```

### Profiles

| Profile    | Description                                           |
| ---------- | ----------------------------------------------------- |
| `strict`   | Requires all resolutions to pass (default)            |
| `node16`   | Ignores `node10` resolution failures                  |
| `esm-only` | Ignores `node10` and `node16-cjs` resolution failures |

### Ignore Rules

You can suppress specific problem types using `ignoreRules`:

| Rule                        | Description                                             |
| --------------------------- | ------------------------------------------------------- |
| `no-resolution`             | Module could not be resolved                            |
| `untyped-resolution`        | Resolution succeeded but has no types                   |
| `false-cjs`                 | Types indicate CJS but implementation is ESM            |
| `false-esm`                 | Types indicate ESM but implementation is CJS            |
| `cjs-resolves-to-esm`       | CJS resolution points to an ESM module                  |
| `fallback-condition`        | A fallback/wildcard condition was used                  |
| `cjs-only-exports-default`  | CJS module only exports a default                       |
| `named-exports`             | Named exports mismatch between types and implementation |
| `false-export-default`      | Types declare a default export that doesn't exist       |
| `missing-export-equals`     | Types are missing `export =` for CJS                    |
| `unexpected-module-syntax`  | File uses unexpected module syntax                      |
| `internal-resolution-error` | Internal resolution error in type checking              |

### CLI

```bash
tsdown --attw
```

## CI Integration

Both `publint` and `attw` support [CI-aware options](/advanced/ci). This is useful for running package validation only in CI:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  publint: 'ci-only',
  attw: {
    enabled: 'ci-only',
    profile: 'node16',
    level: 'error',
  },
})
```

> \[!NOTE]
> Both tools require a `package.json` in your project directory. If no `package.json` is found, a warning is logged and the check is skipped.

---

---
url: /options/platform.md
---
# Platform

The platform specifies the target runtime environment for the bundled JavaScript code.

By default, `tsdown` bundles for the `node` runtime, but you can customize it using the `--platform` option:

```bash
tsdown --platform node    # default
tsdown --platform browser
tsdown --platform neutral
```

### Available Platforms

* **`node`:** Targets the [Node.js](https://nodejs.org/) runtime and compatible environments such as Deno and Bun. This is the default platform, and Node.js built-in modules (e.g., `fs`, `path`) will be resolved automatically. Ideal for toolchains or server-side projects.
* **`browser`:** Targets web browsers (e.g., Chrome, Firefox). This is suitable for front-end projects. If your code uses Node.js built-in modules, a warning will be displayed, and you may need to use polyfills or shims to ensure compatibility.
* **`neutral`:** A platform-agnostic target with no specific runtime assumptions. Use this if your code is intended to run in multiple environments or you want full control over runtime behavior. This is particularly useful for libraries or shared code that may be used in both Node.js and browser environments.

> \[!NOTE]
> For the CJS format, the platform is always set to `'node'` and cannot be changed. [Why?](https://github.com/rolldown/rolldown/pull/4693#issuecomment-2912229545)

### Example

```bash
# Bundle for Node.js (default)
tsdown --platform node

# Bundle for browsers
tsdown --platform browser

# Bundle for a neutral platform
tsdown --platform neutral
```

> \[!TIP]
> Choosing the right platform ensures your code is optimized for its intended runtime. For example, use `browser` for front-end projects, `node` for server-side applications, and `neutral` for universal libraries.

### Module Resolution

Different platforms use different resolve strategies for package entry points. The `mainFields` option determines which fields in `package.json` are checked:

* **`node`:** `['main', 'module']`
* **`browser`:** `['browser', 'module', 'main']`
* **`neutral`:** `[]` (relies solely on the `exports` field)

When using the `neutral` platform, packages without an `exports` field may cause resolution issues. If you encounter warnings like:

```
Help: The "main" field here was ignored. Main fields must be configured explicitly when using the "neutral" platform.
```

Configure `mainFields` explicitly in `inputOptions.resolve`:

```ts
export default defineConfig({
  platform: 'neutral',
  inputOptions: {
    resolve: {
      mainFields: ['module', 'main'],
    },
  },
})
```

See the [Rolldown resolve options documentation](https://rolldown.rs/options/resolve#mainfields) for more details.

---

---
url: /advanced/plugins.md
---
# Plugins

`tsdown` uses [Rolldown](https://rolldown.rs) as its core engine, which means it seamlessly supports Rolldown plugins. Plugins are a powerful way to extend and customize the bundling process, enabling features like code transformation, asset handling, and more.

## Supported Plugin Ecosystems

### Rolldown Plugins

Since `tsdown` is built on Rolldown, it supports all Rolldown plugins. You can use any plugin designed for Rolldown to enhance your build process.

### Unplugin

[Unplugin](https://unplugin.unjs.io/) is a modern plugin framework that supports multiple bundlers, including Rolldown. Most Unplugin plugins (commonly named with the `unplugin-` prefix) work seamlessly with `tsdown`.

### Rollup Plugins

Rolldown is highly compatible with Rollup's plugin API, so `tsdown` can use most Rollup plugins without modification. This gives you access to a wide range of existing plugins in the Rollup ecosystem.

> \[!NOTE] Type Compatibility
> Rollup plugins may sometimes cause TypeScript type errors because the Rollup and Rolldown plugin APIs are not 100% compatible. If you encounter type errors when using Rollup plugins, you can safely ignore them by using `// @ts-expect-error` or casting the plugin as `any`:
>
> ```ts
> import SomeRollupPlugin from 'some-rollup-plugin'
> export default defineConfig({
>   plugins: [SomeRollupPlugin() as any],
> })
> ```

### Vite Plugins

Vite plugins may work with `tsdown` if they do not rely on Vite-specific internal APIs or behaviors. However, plugins that depend heavily on Vite's internals may not be compatible. We plan to improve support for Vite plugins in the future.

> \[!NOTE] Type Compatibility
> Similarly, Vite plugins may also cause type errors due to API differences. You can use `// @ts-expect-error` or `as any` to suppress these errors if needed.

## How to Use Plugins

To use plugins in `tsdown`, you need to add them to the `plugins` array in your configuration file. Plugins **cannot** be added via the CLI.

Here’s an example of how to use a plugin:

```ts [tsdown.config.ts]
import SomePlugin from 'some-plugin'
import { defineConfig } from 'tsdown'

export default defineConfig({
  plugins: [SomePlugin()],
})
```

For specific plugin usage, refer to the plugin's own documentation.

## Writing Your Own Plugins

If you want to create a custom plugin for `tsdown`, you can follow Rolldown's plugin development guide. Rolldown's plugin API is highly flexible and similar to Rollup's, making it easy to get started.

Refer to the [Rolldown Plugin Development Guide](https://rolldown.rs/guide/plugin-development) for detailed instructions on writing your own plugins.

> \[!TIP]
> Plugins are a great way to extend `tsdown`'s functionality. Whether you're using existing plugins or creating your own, they allow you to tailor the bundling process to your project's specific needs.

---

---
url: /advanced/programmatic-usage.md
---
# Programmatic Usage

You can use `tsdown` directly from your JavaScript or TypeScript code. This is useful for custom build scripts, integrations, or advanced automation.

## Example

```ts twoslash
import { build } from 'tsdown'

await build({
  entry: ['src/index.ts'],
  format: ['esm', 'cjs'],
  outDir: 'dist',
  dts: true,
  // ...any other options
})
```

All CLI options are available as properties in the options object. See [Config Options](../reference/api/Interface.UserConfig.md) for the full list.

---

---
url: /recipes/react-support.md
---
# React Support

`tsdown` provides first-class support for building React component libraries. As [Rolldown](https://rolldown.rs/) natively supports bundling JSX/TSX files, you don't need any additional plugins to get started.

## Quick Start

For the fastest way to get started, use the React component starter template. This starter project comes pre-configured for React library development, so you can focus on building components right away.

```bash
npx create-tsdown@latest -t react
```

To use React Compiler, you can quickly set up a project with the dedicated template:

```bash
npx create-tsdown@latest -t react-compiler
```

## Minimal Example

To configure `tsdown` for a React library, you can just use a standard `tsdown.config.ts`:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: ['./src/index.ts'],
  platform: 'neutral',
  dts: true,
})
```

Create your typical React component:

```tsx [MyButton.tsx]
import React from 'react'

interface MyButtonProps {
  type?: 'primary'
}

export const MyButton: React.FC<MyButtonProps> = ({ type }) => {
  return <button className="my-button">my button: type {type}</button>
}
```

And export it in your entry file:

```ts [index.ts]
export { MyButton } from './MyButton'
```

::: warning

There are 2 ways of transforming JSX/TSX files in `tsdown`:

* **classic**
* **automatic** (default)

If you need to use classic JSX transformation, you can configure Rolldown's [`inputOptions.jsx`](https://rolldown.rs/reference/config-options#jsx) option in your configuration file:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  inputOptions: {
    transform: {
      jsx: 'react', // Use classic JSX transformation
    },
  },
})
```

:::

## Enabling React Compiler

React Compiler is an innovative build-time tool that automatically optimizes your React applications. React recommends that library authors use React Compiler to precompile their code for improved performance.

Currently, React Compiler is available only as a Babel plugin. To get started, you can either scaffold the `react-compiler` template as shown above, or integrate it manually:

```bash
pnpm add -D @rollup/plugin-babel babel-plugin-react-compiler
```

```ts [tsdown.config.ts]
import pluginBabel from '@rollup/plugin-babel'
import { defineConfig } from 'tsdown'

export default defineConfig({
  plugins: [
    pluginBabel({
      babelHelpers: 'bundled',
      parserOpts: {
        sourceType: 'module',
        plugins: ['jsx', 'typescript'],
      },
      plugins: ['babel-plugin-react-compiler'],
      extensions: ['.js', '.jsx', '.ts', '.tsx'],
    }),
  ],
})
```

---

---
url: /options/root.md
---
# Root Directory

The `root` option specifies the root directory of your input files, similar to TypeScript's [`rootDir`](https://www.typescriptlang.org/tsconfig/#rootDir). It determines how the output directory structure is computed from your entry files.

## Default Behavior

By default, `root` is automatically computed as the **common base directory** of all entry files. For example, if your entries are `src/a.ts` and `src/b.ts`, the root will be `src/`.

## How to Configure

```ts
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: ['src/index.ts', 'src/utils/helper.ts'],
  root: 'src',
})
```

Or via CLI:

```bash
tsdown --root src
```

## How It Works

The `root` option affects two behaviors:

1. **Entry name resolution**: When using array entries, file paths relative to `root` determine the output filenames.
2. **Unbundle mode**: In unbundle mode, `root` is used as the `preserveModulesRoot`, controlling the output directory structure.

### Example

Given the following project structure:

```
project/
  src/
    index.ts
    utils/
      helper.ts
```

#### Without `root` (default behavior)

```ts
export default defineConfig({
  entry: ['src/index.ts', 'src/utils/helper.ts'],
})
```

The common base directory is `src/`, so the output will be:

```
dist/
  index.js
  utils/
    helper.js
```

#### With explicit `root`

```ts
export default defineConfig({
  entry: ['src/index.ts', 'src/utils/helper.ts'],
  root: '.',
})
```

Now the root is the project directory, so the output preserves the `src/` prefix:

```
dist/
  src/
    index.js
    utils/
      helper.js
```

## When to Use

* When the auto-computed common base directory doesn't produce the desired output structure.
* When you want output paths to include or exclude certain directory prefixes.
* When using unbundle mode and need fine-grained control over the output directory mapping.

---

---
url: /options/shims.md
---
# Shims

Shims are small pieces of code that provide compatibility between different module systems, such as CommonJS (CJS) and ECMAScript Modules (ESM). In `tsdown`, shims are used to bridge the gap between these systems, ensuring your code runs smoothly across different environments.

## CommonJS Variables in ESM

In CommonJS, `__dirname` and `__filename` are built-in variables that provide the directory and file path of the current module. However, these variables are **not available in ESM** by default.

To improve compatibility, when the `shims` option is enabled, `tsdown` will automatically generate these variables for ESM output. For example:

```js
console.log(__dirname) // Available in ESM when shims are enabled
console.log(__filename) // Available in ESM when shims are enabled
```

### Runtime Overhead

The generated shims for `__dirname` and `__filename` introduce a very small runtime overhead. However, if these variables are not used in your code, they will be automatically removed during the bundling process, ensuring no unnecessary code is included.

## The `require` Function in ESM

When using the `require` function in ESM output and the `platform` is set to `node`, `tsdown` will **automatically inject a `require` shim using Node.js's `createRequire`**, regardless of the `shims` option. This ensures that you can use `require` in ESM modules in a Node.js environment without manual setup.

For example:

```js
// const require = createRequire(import.meta.url) [auto injected]

const someModule = require('some-module')
```

This behavior is always enabled for ESM output targeting Node.js, so you don't need to configure anything extra to use `require` in this scenario.

## ESM Variables in CommonJS

Even if the `shims` option is **not enabled**, `tsdown` will automatically shim the following ESM-specific variables in CommonJS output:

* `import.meta.url`
* `import.meta.dirname`
* `import.meta.filename`

These variables are provided to ensure compatibility when using ESM-like features in CommonJS environments. For example:

```js
console.log(import.meta.url)
console.log(import.meta.dirname)
console.log(import.meta.filename)
```

This behavior is always enabled for CommonJS output, so you don't need to configure anything to use these variables.

## Enabling Shims

To enable shims for `__dirname` and `__filename` in ESM output, use the `--shims` option in the CLI or set `shims: true` in the configuration file:

### CLI

```bash
tsdown --shims
```

### Config File

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  shims: true,
})
```

---

---
url: /recipes/solid-support.md
---
# Solid Support

`tsdown` streamlines the development of Solid component libraries by integrating with [`rolldown-plugin-solid`](https://github.com/g-mero/rolldown-plugin-solid) or [`unplugin-solid`](https://github.com/unplugin/unplugin-solid). This integration allows you to bundle Solid components and automatically generate type declarations using modern TypeScript tools.

## Quick Start

For the fastest way to get started, use the Solid component starter template. This starter project comes pre-configured for Solid library development, so you can focus on building components right away.

```bash
npx create-tsdown@latest -t solid
```

## Minimal Example

To configure `tsdown` for a Solid library, use the following setup in your `tsdown.config.ts`:

```ts [tsdown.config.ts]
import solid from 'rolldown-plugin-solid' // or use 'unplugin-solid/rolldown'
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: ['./src/index.ts'],
  platform: 'neutral',
  dts: true,
  plugins: [solid()],
})
```

Create your typical Solid component:

```tsx [MyButton.tsx]
import type { Component } from 'solid-js'

interface MyButtonProps {
  type?: 'primary'
}

export const MyButton: Component<MyButtonProps> = ({ type }) => {
  return (
    <button class="my-button">
      my button: type
      {type}
    </button>
  )
}
```

And export it in your entry file:

```ts [index.ts]
export { MyButton } from './MyButton'
```

Install the required dependencies:

::: code-group

```sh [npm]
npm install -D rolldown-plugin-solid
```

```sh [pnpm]
pnpm add -D rolldown-plugin-solid
```

```sh [yarn]
yarn add -D rolldown-plugin-solid
```

```sh [bun]
bun add -D rolldown-plugin-solid
```

:::

or, if you prefer to use `unplugin-solid`:

::: code-group

```sh [npm]
npm install -D unplugin-solid
```

```sh [pnpm]
pnpm add -D unplugin-solid
```

```sh [yarn]
yarn add -D unplugin-solid
```

```sh [bun]
bun add -D unplugin-solid
```

:::

---

---
url: /options/sourcemap.md
---
# Source Maps

Source maps bridge the gap between your original development code and the optimized code that runs in the browser or other environments, making debugging significantly easier. They allow you to trace errors and logs back to the original source files, even if the code has been minified or bundled.

For example, source maps enable you to identify which line in your React or Vue component caused an error, even though the runtime environment only sees the bundled or minified code.

## Enabling Source Maps

You can instruct `tsdown` to generate source maps by using the `--sourcemap` option:

```bash
tsdown --sourcemap
```

Or in the config file:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  sourcemap: true,
})
```

> \[!NOTE]
> Source maps will always be enabled if you have [`declarationMap`](https://www.typescriptlang.org/tsconfig/#declarationMap) option enabled in your `tsconfig.json`.

## Source Map Modes

The `sourcemap` option accepts the following values:

| Value      | Description                                                                                                                                                                                                                         |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `false`    | Disable source maps (default)                                                                                                                                                                                                       |
| `true`     | Generate separate `.map` files alongside the output. A `//# sourceMappingURL` comment is appended to each output file pointing to the `.map` file.                                                                                  |
| `'inline'` | Embed the source map directly in the output file as a base64-encoded data URL. No separate `.map` file is generated. Similar to TypeScript's [`inlineSourceMap`](https://www.typescriptlang.org/tsconfig/#inlineSourceMap).         |
| `'hidden'` | Generate separate `.map` files but **do not** append the `//# sourceMappingURL` comment to the output. Useful when you want source maps available for error monitoring services but don't want browsers to load them automatically. |

### Using the CLI

```bash
# Enable source maps (separate .map files)
tsdown --sourcemap

# Inline source maps
tsdown --sourcemap inline

# Hidden source maps
tsdown --sourcemap hidden
```

### Using the Config File

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  // Inline source maps into output files
  sourcemap: 'inline',
})
```

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'

export default defineConfig({
  // Generate .map files without sourceMappingURL comments
  sourcemap: 'hidden',
})
```

---

---
url: /recipes/svelte-support.md
---
# Svelte Support

`tsdown` supports building Svelte component libraries by integrating [`rollup-plugin-svelte`](https://github.com/sveltejs/rollup-plugin-svelte). This setup compiles `.svelte` components and bundles them alongside your TypeScript sources.

## Quick Start

For the fastest way to get started, use the Svelte component starter template. This starter project comes pre-configured for Svelte library development.

```bash
npx create-tsdown@latest -t svelte
```

## Minimal Example

Configure `tsdown` for a Svelte library with the following `tsdown.config.ts`:

```ts [tsdown.config.ts]
import svelte from 'rollup-plugin-svelte'
import { sveltePreprocess } from 'svelte-preprocess'
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: ['./src/index.ts'],
  platform: 'neutral',
  plugins: [svelte({ preprocess: sveltePreprocess() })],
})
```

Install the required dependencies:

::: code-group

```sh [npm]
npm install -D rollup-plugin-svelte svelte svelte-preprocess
```

```sh [pnpm]
pnpm add -D rollup-plugin-svelte svelte svelte-preprocess
```

```sh [yarn]
yarn add -D rollup-plugin-svelte svelte svelte-preprocess
```

```sh [bun]
bun add -D rollup-plugin-svelte svelte svelte-preprocess
```

:::

## How It Works

* **`rollup-plugin-svelte`** compiles `.svelte` single-file components.
* **`tsdown`** bundles the compiled output with your TypeScript sources.

:::info

Generating `.d.ts` for Svelte components typically requires integrating [`svelte2tsx`](https://www.npmjs.com/package/svelte2tsx). We recommend using the dedicated Svelte template, which includes an emission step based on `svelte2tsx` to generate declarations after bundling.

:::

## Distribution

In line with community practice and SvelteKit’s [Packaging](https://svelte.dev/docs/kit/packaging) guide, avoid publishing precompiled JS components. Prefer shipping `.svelte` sources and let consumers’ Svelte tooling (e.g. Vite + `@sveltejs/vite-plugin-svelte`) compile them in their apps.

Reasons not to precompile to JS:

* Version compatibility: precompiled output ties to a specific compiler and `svelte/internal` version; mismatches can cause runtime or SSR/hydration issues.
* SSR/hydration consistency: differing compile options (`generate`, `hydratable`, `dev`, etc.) between library and app can lead to hydration mismatches.
* Tooling and optimization: source form benefits from better HMR, diagnostics, CSS handling, and tree-shaking; precompiled JS may lose these advantages.
* Maintenance: fewer republish cycles when Svelte upgrades, since consumers compile with their chosen versions.

When shipping JS can make sense (exceptions):

* You provide artifacts usable outside Svelte (e.g. `customElement` Web Components).
* CDN direct-load scenarios without a consumer build step.

For detailed packaging configuration (e.g. `exports`, `types`, `files`, `sideEffects`, subpath exports and types, declaration maps), see the official guide.

::: tip
tsdown essentials:

* Mark `svelte`/`svelte/*` as external in `tsdown` and declare `svelte` in `peerDependencies`.
* Use `rollup-plugin-svelte` for preprocessing/integration and keep `.svelte` in source form for distribution.
* Use `svelte2tsx` to emit `.d.ts` aligned with your `exports` subpath exports.
  :::

---

---
url: /options/target.md
---
# Target

The `target` setting determines which JavaScript and CSS features are downleveled (transformed to older syntax) and which are left intact in the output. This allows you to control the compatibility of your bundled code with specific environments or JavaScript versions.

For example, a logical assignment `a ||= b` will be transformed into an equivalent `a || (a = b)` expression if the target is `es2015`.

> \[!WARNING] Syntax Downgrade Only
> The `target` option only affects syntax transformations. It does not include runtime polyfills or shims for APIs that may not exist in the target environment. For example, if your code uses `Promise`, it will not be polyfilled for environments that lack native `Promise` support.

## Default Target Behavior

By default, `tsdown` will read the `engines.node` field from your `package.json` and automatically set the target to the minimum compatible Node.js version specified. This ensures your output is compatible with the environments you declare for your package.

For example, if your `package.json` contains:

```json
{
  "engines": {
    "node": ">=18.0.0"
  }
}
```

Then `tsdown` will automatically set the target to `node18.0.0`.

If you want to override this behavior, you can specify the target explicitly using the CLI or configuration file.

## Disabling Target Transformations

You can disable all syntax transformations by setting the target to `false`. This will preserve modern JavaScript and CSS syntax in the output, regardless of the environment specified in your `package.json`.

```json
{
  "target": false
}
```

When `target` is set to `false`:

* No JavaScript syntax downleveling occurs (modern features like optional chaining `?.`, nullish coalescing `??`, etc. are preserved)
* No CSS syntax transformations are applied (modern CSS features like nesting are preserved)
* No runtime helper plugins are loaded
* The output will use the exact syntax from your source code

This is particularly useful when:

* You're targeting modern environments that support the latest JavaScript/CSS features
* You want to handle syntax transformations in a different build step
* You're building a library that will be further processed by the consuming application

> \[!NOTE] No Target Resolution
> If you don't specify a `target` and your `package.json` doesn't have an `engines.node` field, `tsdown` will behave as if `target: false` was set, preserving all modern syntax.

## Customizing the Target

You can specify the target using the `--target` option:

```bash
tsdown --target <target>
```

### Supported Targets

* ECMAScript versions: `es2015`, `es2020`, `esnext`, etc.
* Browser versions: `chrome100`, `safari18`, `firefox110`, etc.
* Node.js versions: `node20.18`, `node16`, etc.

### Example

```bash
tsdown --target es2020
```

You can also pass an array of targets to ensure compatibility across multiple environments:

```bash
tsdown --target chrome100 --target node20.18
```

### Decorator Support

There are currently two major implementations of decorators in the JavaScript ecosystem:

* **Stage 2 (Legacy) Decorators**: The older, experimental implementation, often referred to as "legacy decorators."
* **Stage 3 Decorators**: The latest official proposal, which is significantly different from the legacy version.

If you are using **stage 2 (legacy) decorators**, make sure to enable the `experimentalDecorators` option in your `tsconfig.json`:

```json
{
  "compilerOptions": {
    "experimentalDecorators": true
  }
}
```

If you need to use the **latest TC39 Stage 3 decorators**, please note that `tsdown` (and its underlying engines, Rolldown/Oxc) **do not currently support this feature**. For more information and updates on Stage 3 decorator support, see [this GitHub issue](https://github.com/oxc-project/oxc/issues/9170#issuecomment-3354571325).

> **Note:**
> The two decorator implementations are very different. Make sure you are using the correct configuration and syntax for your chosen decorator version.

## CSS Targeting

`tsdown` can also downlevel CSS features to match your specified browser targets. By default, the top-level `target` is used for CSS, but you can override it with `css.target` or disable CSS lowering independently with `css.target: false`.

For full details on CSS syntax lowering, minification, and Lightning CSS options, see the [CSS documentation](/options/css.md#css-target).

---

---
url: /options/tree-shaking.md
---
# Tree-shaking

Tree shaking is a process that eliminates unused (dead) code from your final bundle, reducing its size and improving performance. It ensures that only the code you actually use is included in the output.

Tree shaking is **enabled by default** in `tsdown`, but you can disable it if needed:

```bash
tsdown --no-treeshake
```

### Example

Given the following input code:

::: code-group

```ts [src/index.ts]
import { hello } from './util'

const x = 1

hello(x)
```

```ts [src/util.ts]
export function unused() {
  console.log("I'm unused.")
}

export function hello(x: number) {
  console.log('Hello World')
  console.log(x)
}
```

:::

Here are the two possible outputs, depending on whether tree shaking is enabled:

::: code-group

```js [dist/index.mjs (with tree shaking)]
function hello(x$1) {
  console.log('Hello World')
  console.log(x$1)
}

const x = 1
hello(x)
```

```js [dist/index.mjs (without tree shaking)]
function unused() {
  console.log("I'm unused.")
}
function hello(x$1) {
  console.log('Hello World')
  console.log(x$1)
}

const x = 1
hello(x)
```

:::

### Explanation

* **With Tree Shaking:** The `unused` function is removed from the final bundle because it is not called anywhere in the source code.
* **Without Tree Shaking:** The `unused` function is included in the bundle, even though it is not used, resulting in a larger output.

> \[!TIP]
> Tree shaking is particularly useful for optimizing libraries or large projects with many unused exports. However, if you need to include all code (e.g., for debugging or testing), you can disable it with `--no-treeshake`.

---

---
url: /reference/api/globals.md
---
# tsdown v0.21.2

## Interfaces

* [AttwOptions](Interface.AttwOptions.md)
* [BuildContext](Interface.BuildContext.md)
* [ChunkAddonObject](Interface.ChunkAddonObject.md)
* [CopyEntry](Interface.CopyEntry.md)
* [DepsConfig](Interface.DepsConfig.md)
* [DevtoolsOptions](Interface.DevtoolsOptions.md)
* [DtsOptions](Interface.DtsOptions.md)
* [ExeOptions](Interface.ExeOptions.md)
* [ExportsOptions](Interface.ExportsOptions.md)
* [InlineConfig](Interface.InlineConfig.md)
* [Logger](Interface.Logger.md)
* [OutExtensionContext](Interface.OutExtensionContext.md)
* [OutExtensionObject](Interface.OutExtensionObject.md)
* [PackageJsonWithPath](Interface.PackageJsonWithPath.md)
* [PublintOptions](Interface.PublintOptions.md)
* [ReportOptions](Interface.ReportOptions.md)
* [ResolvedDepsConfig](Interface.ResolvedDepsConfig.md)
* [RolldownContext](Interface.RolldownContext.md)
* [SeaConfig](Interface.SeaConfig.md)
* [TsdownBundle](Interface.TsdownBundle.md)
* [TsdownHooks](Interface.TsdownHooks.md)
* [UnusedOptions](Interface.UnusedOptions.md)
* [UserConfig](Interface.UserConfig.md)
* [Workspace](Interface.Workspace.md)

## Type Aliases

* [ChunkAddon](TypeAlias.ChunkAddon.md)
* [ChunkAddonFunction](TypeAlias.ChunkAddonFunction.md)
* [CIOption](TypeAlias.CIOption.md)
* [CopyOptions](TypeAlias.CopyOptions.md)
* [CopyOptionsFn](TypeAlias.CopyOptionsFn.md)
* [Format](TypeAlias.Format.md)
* [NoExternalFn](TypeAlias.NoExternalFn.md)
* [NormalizedFormat](TypeAlias.NormalizedFormat.md)
* [OutExtensionFactory](TypeAlias.OutExtensionFactory.md)
* [PackageType](TypeAlias.PackageType.md)
* [ResolvedConfig](TypeAlias.ResolvedConfig.md)
* [RolldownChunk](TypeAlias.RolldownChunk.md)
* [Sourcemap](TypeAlias.Sourcemap.md)
* [TreeshakingOptions](TypeAlias.TreeshakingOptions.md)
* [TsdownInputOption](TypeAlias.TsdownInputOption.md)
* [UserConfigExport](TypeAlias.UserConfigExport.md)
* [UserConfigFn](TypeAlias.UserConfigFn.md)
* [WithEnabled](TypeAlias.WithEnabled.md)

## Variables

* [globalLogger](Variable.globalLogger.md)

## Functions

* [build](Function.build.md)
* [defineConfig](Function.defineConfig.md)
* [enableDebug](Function.enableDebug.md)
* [mergeConfig](Function.mergeConfig.md)

---

---
url: /reference/api/TypeAlias.ChunkAddon.md
---
# Type Alias: ChunkAddon

```ts
type ChunkAddon = ChunkAddonObject | ChunkAddonFunction | string
```

Defined in: [src/features/output.ts:99](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/output.ts#L99)

---

---
url: /reference/api/TypeAlias.ChunkAddonFunction.md
---
# Type Alias: ChunkAddonFunction()

```ts
type ChunkAddonFunction = (ctx) => ChunkAddonObject | string | undefined
```

Defined in: [src/features/output.ts:95](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/output.ts#L95)

## Parameters

### ctx

#### fileName

`string`

#### format

[`Format`](TypeAlias.Format.md)

## Returns

[`ChunkAddonObject`](Interface.ChunkAddonObject.md) | `string` | `undefined`

---

---
url: /reference/api/TypeAlias.CIOption.md
---
# Type Alias: CIOption

```ts
type CIOption = 'ci-only' | 'local-only'
```

Defined in: [src/config/types.ts:126](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L126)

---

---
url: /reference/api/TypeAlias.CopyOptions.md
---
# Type Alias: CopyOptions

```ts
type CopyOptions = Arrayable<string | CopyEntry>
```

Defined in: [src/features/copy.ts:36](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/copy.ts#L36)

---

---
url: /reference/api/TypeAlias.CopyOptionsFn.md
---
# Type Alias: CopyOptionsFn()

```ts
type CopyOptionsFn = (options) => Awaitable<CopyOptions>
```

Defined in: [src/features/copy.ts:37](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/copy.ts#L37)

## Parameters

### options

[`ResolvedConfig`](TypeAlias.ResolvedConfig.md)

## Returns

`Awaitable`<[`CopyOptions`](TypeAlias.CopyOptions.md)>

---

---
url: /reference/api/TypeAlias.Format.md
---
# Type Alias: Format

```ts
type Format = ModuleFormat
```

Defined in: [src/config/types.ts:51](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L51)

---

---
url: /reference/api/TypeAlias.NoExternalFn.md
---
# Type Alias: NoExternalFn()

```ts
type NoExternalFn = (id, importer) => boolean | null | undefined | void
```

Defined in: [src/features/deps.ts:30](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L30)

## Parameters

### id

`string`

### importer

`string` | `undefined`

## Returns

`boolean` | `null` | `undefined` | `void`

---

---
url: /reference/api/TypeAlias.NormalizedFormat.md
---
# Type Alias: NormalizedFormat

```ts
type NormalizedFormat = InternalModuleFormat
```

Defined in: [src/config/types.ts:52](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L52)

---

---
url: /reference/api/TypeAlias.OutExtensionFactory.md
---
# Type Alias: OutExtensionFactory()

```ts
type OutExtensionFactory = (context) => OutExtensionObject | undefined
```

Defined in: [src/features/output.ts:25](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/output.ts#L25)

## Parameters

### context

[`OutExtensionContext`](Interface.OutExtensionContext.md)

## Returns

[`OutExtensionObject`](Interface.OutExtensionObject.md) | `undefined`

---

---
url: /reference/api/TypeAlias.PackageType.md
---
# Type Alias: PackageType

```ts
type PackageType = 'module' | 'commonjs' | undefined
```

Defined in: [src/utils/package.ts:26](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/package.ts#L26)

---

---
url: /reference/api/TypeAlias.ResolvedConfig.md
---
# Type Alias: ResolvedConfig

```ts
type ResolvedConfig = Overwrite<
  MarkPartial<
    Omit<
      UserConfig,
      | 'workspace'
      | 'fromVite'
      | 'publicDir'
      | 'bundle'
      | 'injectStyle'
      | 'removeNodeProtocol'
      | 'external'
      | 'noExternal'
      | 'inlineOnly'
      | 'skipNodeModulesBundle'
      | 'logLevel'
      | 'failOnWarn'
      | 'customLogger'
      | 'envFile'
      | 'envPrefix'
    >,
    | 'globalName'
    | 'inputOptions'
    | 'outputOptions'
    | 'minify'
    | 'define'
    | 'alias'
    | 'onSuccess'
    | 'outExtensions'
    | 'hooks'
    | 'copy'
    | 'loader'
    | 'name'
    | 'banner'
    | 'footer'
    | 'checks'
    | 'css'
  >,
  {
    attw: false | AttwOptions
    clean: string[]
    deps: ResolvedDepsConfig
    devtools: false | DevtoolsOptions
    dts: false | DtsOptions
    entry: Record<string, string>
    exe: false | ExeOptions
    exports: false | ExportsOptions
    format: NormalizedFormat
    ignoreWatch: (string | RegExp)[]
    logger: Logger
    nameLabel: string | undefined
    nodeProtocol: 'strip' | boolean
    pkg?: PackageJsonWithPath
    publint: false | PublintOptions
    rawEntry?: TsdownInputOption
    report: false | ReportOptions
    root: string
    target?: string[]
    tsconfig: false | string
    unused: false | UnusedOptions
  }
>
```

Defined in: [src/config/types.ts:627](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L627)

---

---
url: /reference/api/TypeAlias.RolldownChunk.md
---
# Type Alias: RolldownChunk

```ts
type RolldownChunk = OutputChunk | (OutputAsset & object)
```

Defined in: [src/utils/chunks.ts:4](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/chunks.ts#L4)

## Type Declaration

### outDir

```ts
outDir: string
```

---

---
url: /reference/api/TypeAlias.Sourcemap.md
---
# Type Alias: Sourcemap

```ts
type Sourcemap = boolean | 'inline' | 'hidden'
```

Defined in: [src/config/types.ts:50](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L50)

---

---
url: /reference/api/TypeAlias.TreeshakingOptions.md
---
# Type Alias: TreeshakingOptions

```ts
type TreeshakingOptions = object
```

Defined in: node\_modules/.pnpm/rolldown@1.0.0-rc.9/node\_modules/rolldown/dist/shared/define-config-cG45vHwf.d.mts:2285

When passing an object, you can fine-tune the tree-shaking behavior.

## Properties

### annotations?

```ts
optional annotations: boolean;
```

Defined in: node\_modules/.pnpm/rolldown@1.0.0-rc.9/node\_modules/rolldown/dist/shared/define-config-cG45vHwf.d.mts:2361

Whether to respect `/*@__PURE__*/` annotations and other tree-shaking hints in the code.

See [related Oxc documentation](https://oxc.rs/docs/guide/usage/minifier/dead-code-elimination#pure-annotations) for more details.

#### Default

```ts
true
```

***

### commonjs?

```ts
optional commonjs: boolean;
```

Defined in: node\_modules/.pnpm/rolldown@1.0.0-rc.9/node\_modules/rolldown/dist/shared/define-config-cG45vHwf.d.mts:2410

Whether to enable tree-shaking for CommonJS modules. When `true`, unused exports from CommonJS modules can be eliminated from the bundle, similar to ES modules. When disabled, CommonJS modules will always be included in their entirety.

This option allows rolldown to analyze `exports.property` assignments in CommonJS modules and remove unused exports while preserving the module's side effects.

#### Example

```js
// source.js (CommonJS)
exports.used = 'This will be kept'
exports.unused = 'This will be tree-shaken away'

// main.js
import { used } from './source.js'
// With commonjs: true, only the 'used' export is included in the bundle
// With commonjs: false, both exports are included
```

#### Default

```ts
true
```

***

### invalidImportSideEffects?

```ts
optional invalidImportSideEffects: boolean;
```

Defined in: node\_modules/.pnpm/rolldown@1.0.0-rc.9/node\_modules/rolldown/dist/shared/define-config-cG45vHwf.d.mts:2391

Whether to assume that invalid import statements might have side effects.

See [related Oxc documentation](https://oxc.rs/docs/guide/usage/minifier/dead-code-elimination#ignoring-invalid-import-statement-side-effects) for more details.

#### Default

```ts
false
```

***

### manualPureFunctions?

```ts
optional manualPureFunctions: readonly string[];
```

Defined in: node\_modules/.pnpm/rolldown@1.0.0-rc.9/node\_modules/rolldown/dist/shared/define-config-cG45vHwf.d.mts:2375

Array of function names that should be considered pure (no side effects) even if they can't be automatically detected as pure.

See [related Oxc documentation](https://oxc.rs/docs/guide/usage/minifier/dead-code-elimination#define-pure-functions) for more details.

#### Example

```js
treeshake: {
  manualPureFunctions: ['console.log', 'debug.trace']
}
```

#### Default

```ts
;[]
```

***

### moduleSideEffects?

```ts
optional moduleSideEffects: ModuleSideEffectsOption;
```

Defined in: node\_modules/.pnpm/rolldown@1.0.0-rc.9/node\_modules/rolldown/dist/shared/define-config-cG45vHwf.d.mts:2353

**Values:**

* **`true`**: All modules are assumed to have side effects and will be included in the bundle even if none of their exports are used.
* **`false`**: No modules have side effects. This enables aggressive tree-shaking, removing any modules whose exports are not used.
* **`string[]`**: Array of module IDs that have side effects. Only modules in this list will be preserved if unused; all others can be tree-shaken when their exports are unused.
* **`'no-external'`**: Assumes no external modules have side effects while preserving the default behavior for local modules.
* **`ModuleSideEffectsRule[]`**: Array of rules with `test`, `external`, and `sideEffects` properties for fine-grained control.
* **`function`**: Function that receives `(id, external)` and returns whether the module has side effects.

**Important:** Setting this to `false` or using an array/string assumes that your modules and their dependencies have no side effects other than their exports. Only use this if you're certain that removing unused modules won't break your application.

> \[!NOTE]
> **Performance: Prefer `ModuleSideEffectsRule[]` over functions**
>
> When possible, use rule-based configuration instead of functions. Rules are processed entirely in Rust, while JavaScript functions require runtime calls between Rust and JavaScript, which can hurt CPU utilization during builds.
>
> **Functions should be a last resort**: Only use the function signature when your logic cannot be expressed with patterns or simple string matching.
>
> **Rule advantages**: `ModuleSideEffectsRule[]` provides better performance by avoiding Rust-JavaScript runtime calls, clearer intent, and easier maintenance.

#### Example

```js
// Assume no modules have side effects (aggressive tree-shaking)
treeshake: {
  moduleSideEffects: false
}

// Only specific modules have side effects (string array)
treeshake: {
  moduleSideEffects: [
    'lodash',
    'react-dom',
  ]
}

// Use rules for pattern matching and granular control
treeshake: {
  moduleSideEffects: [
    { test: /^node:/, sideEffects: true },
    { test: /\.css$/, sideEffects: true },
    { test: /some-package/, sideEffects: false, external: false },
  ]
}

// Custom function to determine side effects
treeshake: {
  moduleSideEffects: (id, external) => {
    if (external) return false; // external modules have no side effects
    return id.includes('/side-effects/') || id.endsWith('.css');
  }
}

// Assume no external modules have side effects
treeshake: {
  moduleSideEffects: 'no-external',
}
```

**Common Use Cases:**

* **CSS files**: `{ test: /\.css$/, sideEffects: true }` - preserve CSS imports
* **Polyfills**: Add specific polyfill modules to the array
* **Plugins**: Modules that register themselves globally on import
* **Library development**: Set to `false` for libraries where unused exports should be removed

#### Default

```ts
true
```

***

### propertyReadSideEffects?

```ts
optional propertyReadSideEffects: false | "always";
```

Defined in: node\_modules/.pnpm/rolldown@1.0.0-rc.9/node\_modules/rolldown/dist/shared/define-config-cG45vHwf.d.mts:2420

Controls whether reading properties from objects is considered to have side effects.

Set to `false` for more aggressive tree-shaking behavior.

See [related Oxc documentation](https://oxc.rs/docs/guide/usage/minifier/dead-code-elimination#ignoring-property-read-side-effects) for more details.

#### Default

```ts
'always'
```

***

### propertyWriteSideEffects?

```ts
optional propertyWriteSideEffects: false | "always";
```

Defined in: node\_modules/.pnpm/rolldown@1.0.0-rc.9/node\_modules/rolldown/dist/shared/define-config-cG45vHwf.d.mts:2428

Controls whether writing properties to objects is considered to have side effects.

Set to `false` for more aggressive behavior.

#### Default

```ts
'always'
```

***

### unknownGlobalSideEffects?

```ts
optional unknownGlobalSideEffects: boolean;
```

Defined in: node\_modules/.pnpm/rolldown@1.0.0-rc.9/node\_modules/rolldown/dist/shared/define-config-cG45vHwf.d.mts:2383

Whether to assume that accessing unknown global properties might have side effects.

See [related Oxc documentation](https://oxc.rs/docs/guide/usage/minifier/dead-code-elimination#ignoring-global-variable-access-side-effects) for more details.

#### Default

```ts
true
```

---

---
url: /reference/api/TypeAlias.TsdownInputOption.md
---
# Type Alias: TsdownInputOption

```ts
type TsdownInputOption = Arrayable<string | Record<string, Arrayable<string>>>
```

Defined in: [src/config/types.ts:71](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L71)

Extended input option that supports glob negation patterns.

When using object form, values can be:

* A single glob pattern string
* An array of glob patterns, including negation patterns (prefixed with `!`)

## Example

```ts
entry: {
  // Single pattern
  "utils/*": "./src/utils/*.ts",
  // Array with negation pattern to exclude files
  "hooks/*": ["./src/hooks/*.ts", "!./src/hooks/index.ts"],
}
```

---

---
url: /reference/api/TypeAlias.UserConfigExport.md
---
# Type Alias: UserConfigExport

```ts
type UserConfigExport = Awaitable<Arrayable<UserConfig> | UserConfigFn>
```

Defined in: [src/config/types.ts:625](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L625)

---

---
url: /reference/api/TypeAlias.UserConfigFn.md
---
# Type Alias: UserConfigFn()

```ts
type UserConfigFn = (inlineConfig, context) => Awaitable<Arrayable<UserConfig>>
```

Defined in: [src/config/types.ts:620](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L620)

## Parameters

### inlineConfig

[`InlineConfig`](Interface.InlineConfig.md)

### context

#### ci

`boolean`

## Returns

`Awaitable`<`Arrayable`<[`UserConfig`](Interface.UserConfig.md)>>

---

---
url: /reference/api/TypeAlias.WithEnabled.md
---
# Type Alias: WithEnabled\<T>

```ts
type WithEnabled<T> = boolean | undefined | CIOption | (T & object)
```

Defined in: [src/config/types.ts:128](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L128)

## Type Parameters

### T

`T`

---

---
url: /options/unbundle.md
---
# Unbundle Mode

The **unbundle** mode in `tsdown` allows you to output files that closely mirror your source module structure, rather than producing a single bundled file for each entry. In this mode, each source file is compiled and transformed individually, and the output directory will contain a one-to-one mapping of your source files to output files. This approach is often referred to as a "bundleless" or "transpile-only" build, where the focus is on transforming code rather than bundling it together.

## How to Enable

You can enable unbundle mode by setting the `unbundle` option to `true` in your `tsdown` configuration:

```ts
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: ['src/index.ts'],
  unbundle: true,
})
```

## How It Works

When unbundle mode is enabled, every source file that is referenced (directly or indirectly) from your entry points will be compiled and output to the corresponding location in the output directory. This means that the output structure will closely match your source directory structure, making it easy to trace output files back to their original source files.

### Example

Suppose your project has the following files:

```
src/
  index.ts
  mod.ts
```

And `src/index.ts` imports `src/mod.ts`:

```ts [src/index.ts]
import { foo } from './mod'

foo()
```

```ts [src/mod.ts]
export function foo() {
  console.log('Hello from mod!')
}
```

With `unbundle: true`, even though only `src/index.ts` is listed as an entry, both `src/index.ts` and `src/mod.ts` will be compiled and output as separate files:

```
dist/
  index.js
  mod.js
```

Each output file corresponds directly to its source file, preserving the module structure of your original codebase.

## Controlling the Output Root

By default, the output directory structure is based on the common base directory of all entry files. You can use the [`root`](/options/root) option to override this behavior:

```ts
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: ['src/index.ts'],
  unbundle: true,
  root: '.', // Preserve `src/` prefix in output
})
```

## When to Use Unbundle Mode

Unbundle mode is ideal when you want to:

* Maintain a clear mapping between source and output files.
* Avoid bundling all modules together, for example in monorepo or library scenarios where consumers may want to import individual modules.
* Focus on code transformation (e.g., TypeScript to JavaScript) without combining files.

---

---
url: /reference/api/Variable.globalLogger.md
---
# Variable: globalLogger

```ts
const globalLogger: Logger
```

Defined in: [src/utils/logger.ts:128](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/logger.ts#L128)

---

---
url: /recipes/vue-support.md
---
# Vue Support

`tsdown` provides first-class support for building Vue component libraries by seamlessly integrating with [`unplugin-vue`](https://github.com/unplugin/unplugin-vue) and [`rolldown-plugin-dts`](https://github.com/sxzz/rolldown-plugin-dts). This setup enables you to bundle Vue components and generate type declarations with modern TypeScript tooling.

## Quick Start

For the fastest way to get started, use the Vue component starter template. This starter project comes pre-configured for Vue library development, so you can focus on building components right away.

```bash
npx create-tsdown@latest -t vue
```

## Minimal Example

To configure `tsdown` for a Vue library, use the following setup in your `tsdown.config.ts`:

```ts [tsdown.config.ts]
import { defineConfig } from 'tsdown'
import Vue from 'unplugin-vue/rolldown'

export default defineConfig({
  entry: ['./src/index.ts'],
  platform: 'neutral',
  plugins: [Vue({ isProduction: true })],
  dts: { vue: true },
})
```

Install the required dependencies:

::: code-group

```sh [npm]
npm install -D unplugin-vue vue-tsc
```

```sh [pnpm]
pnpm add -D unplugin-vue vue-tsc
```

```sh [yarn]
yarn add -D unplugin-vue vue-tsc
```

```sh [bun]
bun add -D unplugin-vue vue-tsc
```

:::

## How It Works

* **`unplugin-vue`** compiles `.vue` single-file components into JavaScript and extracts CSS, making them ready for bundling.
* **`rolldown-plugin-dts`** (with `vue: true`) and **`vue-tsc`** work together to generate accurate TypeScript declaration files for your Vue components, ensuring consumers of your library get full type support.

> \[!TIP]
> Set `platform: 'neutral'` to maximize compatibility for libraries that may be used in both browser and Node.js environments.

---

---
url: /recipes/wasm-support.md
---
# WASM Support

`tsdown` supports bundling WebAssembly (WASM) modules through [`rolldown-plugin-wasm`](https://github.com/sxzz/rolldown-plugin-wasm). This plugin allows you to import `.wasm` files directly in your TypeScript or JavaScript code, with support for both synchronous and asynchronous instantiation.

## Minimal Example

To configure `tsdown` for WASM support, add the plugin to your `tsdown.config.ts`:

```ts [tsdown.config.ts]
import { wasm } from 'rolldown-plugin-wasm'
import { defineConfig } from 'tsdown'

export default defineConfig({
  entry: ['./src/index.ts'],
  plugins: [wasm()],
})
```

Install the required dependency:

::: code-group

```sh [npm]
npm install -D rolldown-plugin-wasm
```

```sh [pnpm]
pnpm add -D rolldown-plugin-wasm
```

```sh [yarn]
yarn add -D rolldown-plugin-wasm
```

```sh [bun]
bun add -D rolldown-plugin-wasm
```

:::

## Importing WASM Modules

You can import WASM modules directly:

```ts
import { add } from './add.wasm'

add(1, 2)
```

### Asynchronous Init

Use the `?init` query to get an async initialization function:

```ts
import init from './add.wasm?init'

const instance = await init(
  imports, // optional
)

instance.exports.add(1, 2)
```

### Synchronous Init

Use the `?init&sync` query for synchronous initialization:

```ts
import initSync from './add.wasm?init&sync'

const instance = initSync(
  imports, // optional
)

instance.exports.add(1, 2)
```

## `wasm-bindgen` Support

### Target `bundler` (Default, Recommended)

```ts
import { add } from 'some-pkg'

add(1, 2)
```

### Target `web`

#### Node.js

```ts
import { readFile } from 'node:fs/promises'
import init, { add } from 'some-pkg'
import wasmUrl from 'some-pkg/add_bg.wasm?url'

await init({
  module_or_path: readFile(new URL(wasmUrl, import.meta.url)),
})

add(1, 2)
```

#### Browser

```ts
import init, { add } from 'some-pkg/add.js'
import wasmUrl from 'some-pkg/add_bg.wasm?url'

await init({
  module_or_path: wasmUrl,
})

add(1, 2)
```

> \[!NOTE]
> Other `wasm-bindgen` targets such as `nodejs` and `no-modules` are not supported.

## TypeScript Support

To get type support for `.wasm` imports, add the type declarations to your `tsconfig.json`:

```jsonc [tsconfig.json]
{
  "compilerOptions": {
    "types": ["rolldown-plugin-wasm/types"],
  },
}
```

## Options

The plugin accepts an options object:

```ts
wasm({
  maxFileSize: 14 * 1024, // Max file size for inline (default: 14KB)
  fileName: '[hash][extname]', // Output file name pattern
  publicPath: '', // Prefix for non-inlined file paths
  targetEnv: 'auto', // 'auto' | 'auto-inline' | 'browser' | 'node'
})
```

| Option        | Default             | Description                                                                                                                                                                                                                                      |
| ------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `maxFileSize` | `14 * 1024`         | Maximum file size for inlining. Files exceeding this limit are copied to the output directory and loaded at runtime. Set to `0` to always copy.                                                                                                  |
| `fileName`    | `'[hash][extname]'` | Pattern for renaming emitted WASM files.                                                                                                                                                                                                         |
| `publicPath`  | —                   | Prefix added to file paths for non-inlined WASM files.                                                                                                                                                                                           |
| `targetEnv`   | `'auto'`            | Controls the generated instantiation code. `'auto'` detects the environment at runtime; `'auto-inline'` always inlines and decodes based on environment; `'browser'` omits Node.js builtins; `'node'` omits `fetch` (requires Node.js 20.16.0+). |

---

---
url: /options/watch-mode.md
---
# Watch Mode

Watch mode allows `tsdown` to automatically re-bundle your code whenever changes are detected in the specified files or directories. This is particularly useful during development to streamline the build process.

### Enabling Watch Mode

You can enable watch mode using the `--watch` (or `-w`) option:

```bash
tsdown --watch
```

### Watching Specific Paths

By default, `tsdown` watches the files in your project that are part of the build process. However, you can specify a custom path to watch for changes:

```bash
tsdown --watch <path>
```

### Example

```bash
# Watch all files in the project (default behavior)
tsdown --watch

# Watch a specific directory
tsdown --watch ./src

# Watch a specific file
tsdown --watch ./src/index.ts
```

> \[!TIP]
> Watch mode is ideal for development workflows, as it eliminates the need to manually rebuild your project after every change.

See also [Why tsdown Does Not Support Stub Mode](../guide/faq.md#stub-mode) for background on why watch mode is the recommended alternative to stub mode.

---

---
url: /guide/skills.md
---
# Work with AI

tsdown provides official [skills](https://agentskills.io/) for AI coding agents, enabling them to understand tsdown's configuration, features, and best practices when helping you build libraries.

## Installation

Install the tsdown skill to your AI coding agent:

```bash
npx skills add rolldown/tsdown
```

The source code of the skill is [here](https://github.com/rolldown/tsdown/tree/main/skills/tsdown).

## Example Prompts

Once installed, you can ask agents to help with various tsdown tasks:

```
Set up tsdown to build my TypeScript library with ESM and CJS formats
```

```
Configure tsdown to generate type declarations and bundle for browsers
```

```
Add React support to my tsdown config with Fast Refresh
```

```
Set up a monorepo build with tsdown workspace support
```

## What's Included

The tsdown skill provides knowledge about:

* Configuration file formats, options, and workspace support
* Entry points, output formats, and type declarations
* Dependency handling and auto-externalization
* Framework support (React, Vue, Solid, Svelte)
* Plugins, hooks, and programmatic API
* CLI commands and usage patterns
