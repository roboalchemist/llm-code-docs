# Stylex Documentation

Source: https://www.stylexjs.com/llms-full.txt

---

# @stylexjs/babel-plugin (/docs/api/configuration/babel-plugin)

## Configuration options

### `aliases`

```ts
aliases: {[key: string]: string | Array<string>} // Default: undefined
```

`aliases` option allows you to alias project directories to absolute paths,
making it easier to import modules.

Example: `'@/components/*': [path.join(__dirname, './src/components/*')]`

***

### `classNamePrefix`

```ts
classNamePrefix: string; // Default: 'x'
```

Prefix to be applied to every generated className.

***

### `debug`

```ts
debug: boolean; // Default: false
```

When `true`, StyleX will use debug class names and insert `data-style-src` props
to help identify the source of the styles.

***

### `dev`

```ts
dev: boolean; // Default: false
```

When `true`, StyleX will insert function calls to inject the CSS rules at
runtime, making it possible to use StyleX without setting up CSS file
extraction.

***

### `importSources`

```ts
importSources: Array<string | { from: string; as: string }>; // Default: ['@stylexjs/stylex']
```

Override the package name where you can import stylex from. Used for setting up
custom module aliases.

Example: `importSources: ['stylex', { from: '@acme/ui', as: 'css' }]`

***

### `runtimeInjection`

```ts
runtimeInjection: boolean; // Default: false
```

Should StyleX generate code to inject styles at runtime? This may be useful
during development but should be disabled in production.

***

### `styleResolution`

```ts
styleResolution: // Default: 'property-specificity'
  | 'application-order'
  | 'property-specificity'
```

Strategy to use for merging styles.

* **application-order**: The last style applied wins. Consistent with how inline
  styles work on the web.
* **property-specificity**: More specific styles will win over less specific
  styles. Consistent with React Native. (`margin-top` wins over `margin`)

***

### `test`

```ts
test: boolean; // Default: false
```

When `true`, StyleX will only output debug classNames identifying the source of
the styles.

It will *not* generate any styles or functional classNames. This can be useful
for snapshot testing.

***

### `env`

```ts
env: { [key: string]: mixed }; // Default: {}
```

An object of compile-time constants and functions available as
[`stylex.env`](/docs/api/javascript/env). Values are substituted before other
StyleX APIs are compiled. Supports strings, numbers, objects, and functions.

***

### `treeshakeCompensation`

```ts
treeshakeCompensation: boolean; // Default: false
```

Named imports of StyleX variables are unused after compilation. Some bundlers
may remove them as dead code. Causing variables to be undefined. Enable this
option to prevent that by adding an import with no specifier. (e.g.
`import './my-vars.stylex.js'`)

***

### `unstable_moduleResolution`

```ts
unstable_moduleResolution: // Default: undefined
  | {
      // The module system to be used.
      // Use this value when using `ESModules`.
      type: 'commonJS',
      // The absolute path to the root directory of your project.
      // Only used as a fallback
      rootDir?: string,
      // Override `.stylex.js` with your own extension.
      themeFileExtension?: string,
    }
  | {
      // Use this when using the Haste module system
      // Where all files are imported by filename rather
      // than relative paths and all filenames must be unique.
      type: 'haste',
      // Override `.stylex.js` with your own extension.
      themeFileExtension?: string,
    }
```

Strategy to use for resolving variables defined with `defineVars`. This is
required if you plan to use StyleX's theming APIs.

**NOTE**: While theming APIs are stable, the shape of this configuration option
may change in the future.


# @stylexjs/eslint-plugin (/docs/api/configuration/eslint-plugin)

## Configuration options

### `@stylexjs/valid-styles` rule

```ts
type Options = {
  // Possible strings where you can import stylex from
  //
  // Default: ['stylex', '@stylexjs/stylex']
  validImports: Array<string | { from: string; as: string }>;

  // Custom limits for values of various properties
  propLimits?: PropLimits;

  // @deprecated
  // Allow At Rules and Pseudo Selectors outside of
  // style values.
  //
  // Default: false
  allowOuterPseudoAndMedia: boolean;

  // @deprecated
  // Disallow properties that are known to break
  // in 'legacy-expand-shorthands' style resolution mode.
  //
  // Default: false
  banPropsForLegacy: boolean;
};

type PropLimits = {
  // The property name as a string or a glob pattern
  [propertyName: string]: {
    limit: // Disallow the property
    | null
      // Allow any string value
      | 'string'
      // Allow any number value
      | 'number'
      // Any string other 'string' or 'number'
      // will be considered to be a valid constant
      // e.g. 'red' or '100px'.
      | string
      // You can also provide numeric constants
      // e.g. 100 or 0.5
      | number
      // You can also provide an array of valid
      // number or string constant values.
      | Array<string | number>;
    // The error message to show when a value doesn't
    // conform to the provided restriction.
    reason: string;
  };
};
```

#### Example

```json
{
  "rules": {
    "@stylexjs/valid-styles": [
      "error",
      {
        "propLimits": {
          "mask+([a-zA-Z])": {
            "limit": null,
            "reason": "Use the `mask` shorthand property instead."
          },
          "fontSize": {
            "limit": "number",
            "reason": "Only numeric font values are allowed"
          },
          "padding": {
            "limit": [0, 4, 8, 16, 32, 64],
            "reason": "Use a padding that conforms to the design system"
          }
        }
      }
    ]
  }
}
```

### `@stylexjs/sort-keys` rule

```ts
type Options = {
  // Possible strings where you can import stylex from
  //
  // Default: ['stylex', '@stylexjs/stylex']
  validImports: Array<string | { from: string; as: string }>;

  // Minimum number of keys required after which the rule is enforced
  //
  // Default: 2
  minKeys: number;

  // Sort groups of keys that have a blank line between them separately
  //
  // Default: false
  allowLineSeparatedGroups: boolean;
};
```

#### Example

```json
{
  "rules": {
    "@stylexjs/valid-styles": "error",
    "@stylexjs/sort-keys": [
      "warn",
      {
        "minKeys": 3,
        "allowLineSeparatedGroups": true
      }
    ]
  }
}
```

### `@stylexjs/valid-shorthands` rule

```ts
type Options = {
  // Possible strings where you can import stylex from
  //
  // Default: ['stylex', '@stylexjs/stylex']
  validImports: Array<string | { from: string; as: string }>;

  // Whether `!important` is allowed
  //
  // Default: false
  allowImportant: boolean;

  // Whether the expansion uses logical direction properties over physical
  //
  // Default: false
  preferInline: boolean;
};
```

### `@stylexjs/enforce-extension` rule

```ts
type Options = {
  // Possible strings where you can import stylex from
  //
  // Default: ['stylex', '@stylexjs/stylex']
  validImports: Array<string | { from: string; as: string }>;

  // The file extension to enforce for theme files
  //
  // Default: '.stylex.js'
  themeFileExtension: string;
};
```

### `@stylexjs/no-unused` rule

```ts
type Options = {
  // Possible strings where you can import stylex from
  //
  // Default: ['stylex', '@stylexjs/stylex']
  validImports: Array<string | { from: string; as: string }>;
};
```

### `@stylexjs/no-legacy-contextual-styles` rule

```ts
type Options = {
  // Possible strings where you can import stylex from
  //
  // Default: ['stylex', '@stylexjs/stylex']
  validImports: Array<string | { from: string; as: string }>;
};
```


# @stylexjs/postcss-plugin (/docs/api/configuration/postcss-plugin)

## Configuration options

### babelConfig

```js
babelConfig: object; // Default: {}
```

Options for Babel configuration. By default, the plugin reads the
`babel.config.js` in your project. For custom configurations, set
`babelrc: false` and specify desired options. Refer to
[Babel Config Options](https://babeljs.io/docs/options) for available options.

***

### cwd

```js
cwd: string; // Default: process.cwd()
```

Working directory for the plugin; defaults to `process.cwd()`.

***

### exclude

```js
exclude: string[] // Default: []
```

Array of paths or glob patterns to exclude from compilation. Paths in `exclude`
take precedence over `include`.

***

### importSources

```js
importSources: Array<string | { from: string, as: string }>; // Default: ['@stylexjs/stylex', 'stylex']
```

Possible strings where you can import stylex from. Files that do not match the
import sources may be skipped from being processed to speed up compilation.

***

### include

```js
include: string[] // Required
```

Array of paths or glob patterns to compile.

***

### useCSSLayers

```js
useCSSLayers: boolean; // Default: false
```

Enabling this option switches Stylex from using `:not(#\#)` to using `@layers`
for handling CSS specificity.


# @stylexjs/unplugin (/docs/api/configuration/unplugin)

Universal bundler plugin for StyleX built on top of
[`unplugin`](https://github.com/unjs/unplugin). It compiles StyleX modules,
aggregates the generated CSS, and appends the result to an emitted CSS asset (or
creates `stylex.css` as a fallback). Adapters are available for Vite/Rollup,
Webpack/Rspack, and esbuild.

## Install

<DevInstallExample dev={[`@stylexjs/unplugin`]} />

## Usage by bundler

### Vite

```ts title="vite.config.ts"
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import stylex from '@stylexjs/unplugin';

export default defineConfig({
  plugins: [stylex.vite({ useCSSLayers: true }), react()],
});
```

* Keep `stylex.vite()` before framework plugins to preserve Fast Refresh.
* Provide a CSS entry so Vite emits an asset for the plugin to append to.
* Dev virtual modules:
  * `/virtual:stylex.css` — aggregated CSS endpoint.
  * `virtual:stylex:runtime` — JS runtime for hot CSS reloads.
  * `virtual:stylex:css-only` — JS shim that only triggers CSS reloads. Add
    `<link rel="stylesheet" href="/virtual:stylex.css" />` and either a
    `<script type="module" src="/@id/virtual:stylex:runtime">` tag or a
    `import('virtual:stylex:runtime')` call from a client shim in dev.

### Webpack

```js title="webpack.config.js"
const stylex = require('@stylexjs/unplugin').default;
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  module: {
    rules: [
      // JS/TS loader here
      { test: /\.css$/, use: [MiniCssExtractPlugin.loader, 'css-loader'] },
    ],
  },
  plugins: [stylex.webpack({ useCSSLayers: true }), new MiniCssExtractPlugin()],
};
```

Use a CSS extractor so Webpack emits a stylesheet for StyleX to append to.

### Rspack

```js title="rspack.config.js"
const rspack = require('@rspack/core');
const stylex = require('@stylexjs/unplugin').default;

module.exports = {
  plugins: [
    stylex.rspack({}),
    new rspack.CssExtractRspackPlugin({ filename: 'index.css' }),
  ],
};
```

### Rollup

```js title="rollup.config.mjs"
import stylex from '@stylexjs/unplugin';

export default {
  plugins: [stylex.rollup({ useCSSLayers: true })],
};
```

### esbuild

```js
import esbuild from 'esbuild';
import stylex from '@stylexjs/unplugin';

esbuild.build({
  entryPoints: ['src/App.jsx'],
  bundle: true,
  metafile: true, // lets the plugin find CSS outputs
  plugins: [stylex.esbuild({ useCSSLayers: true })],
});
```

## Options (shared)

All options from [`@stylexjs/babel-plugin`](./babel-plugin.mdx) are forwarded.
The unplugin adds:

* `dev` (`boolean`): defaults to `NODE_ENV === 'development'`. Forces dev or
  prod transforms.
* `importSources` (`string[] | {from: string, as: string}[]`, default
  `['stylex', '@stylexjs/stylex']`): packages that export StyleX APIs. Also used
  to auto-exclude dependencies from Vite optimizeDeps/SSR.
* `useCSSLayers` (`boolean`, default `false`): wrap output in `@layer` blocks.
* `enableLTRRTLComments` (`boolean`): include `/* @ltr */` and `/* @rtl */`
  annotations when emitting directional CSS.
* `legacyDisableLayers` (`boolean`): disable layer usage when emitting CSS
  (legacy behavior).
* `lightningcssOptions` (`object`): passthrough options for `lightningcss`.
* `cssInjectionTarget` (`(fileName: string) => boolean`): pick which emitted CSS
  asset to append to. Defaults to preferring `index.css`/`style.css` or the
  first CSS asset; falls back to creating `stylex.css` if none exist.
* `externalPackages` (`string[]`, default `[]`): additional packages inside
  `node_modules` that should be transformed as if they were app code (useful if
  they ship StyleX).
* `devPersistToDisk` (`boolean`, default `false`, Vite): persist collected rules
  to `node_modules/.stylex/rules.json` so multiple dev environments (RSC/SSR)
  can share CSS.
* `devMode` (`'full' | 'css-only' | 'off'`, default `'full'`, Vite): controls
  which dev middleware/virtual modules are exposed.
* `treeshakeCompensation` (`boolean`): adds a safe side-effect import to prevent
  bundlers from removing StyleX themes/vars. Defaults to `true` for Vite/Rollup
  adapters.

## Notes

* Each output bundle receives its own aggregated StyleX CSS. When no CSS asset
  exists, the plugin emits `stylex.css` alongside the bundle.
* When using CSS extraction plugins (Webpack/Rspack), ensure they run so there
  is a concrete stylesheet to append to.
* For dev HMR, include the virtual stylesheet link in your HTML shell. If script
  tags are blocked by your framework’s asset handling, import the runtime from a
  tiny client shim instead of using a `<script src>` tag.


# API Reference (/docs/api)

## Configuration

* [`@stylexjs/babel-plugin`](/docs/api/configuration/babel-plugin)
* [`@stylexjs/eslint-plugin`](/docs/api/configuration/eslint-plugin)
* [`@stylexjs/unplugin`](/docs/api/configuration/unplugin)
* [`@stylexjs/postcss-plugin`](/docs/api/configuration/postcss-plugin)

## JavaScript API

* [`stylex.create()`](/docs/api/javascript/create)
* [`stylex.props()`](/docs/api/javascript/props)
* [`stylex.defineConsts()`](/docs/api/javascript/defineConsts)
* [`stylex.defineVars()`](/docs/api/javascript/defineVars)
* [`stylex.createTheme()`](/docs/api/javascript/createTheme)
* [`stylex.when.*()`](/docs/api/javascript/when)
* [`stylex.env.*`](/docs/api/javascript/env)
* [`stylex.keyframes()`](/docs/api/javascript/keyframes)
* [`stylex.viewTransitionClass()`](/docs/api/javascript/viewTransitionClass)
* [`stylex.positionTry()`](/docs/api/javascript/positionTry)
* [`stylex.firstThatWorks()`](/docs/api/javascript/firstThatWorks)
* [`stylex.types.*()`](/docs/api/javascript/types)

## Static types

* [`type StyleXStyles`](/docs/api/types/StyleXStyles)
* [`type StyleXStylesWithout`](/docs/api/types/StyleXStylesWithout)
* [`type StaticStyles`](/docs/api/types/StaticStyles)
* [`type Theme`](/docs/api/types/Theme)
* [`type VarGroup`](/docs/api/types/VarGroup)


# stylex.create (/docs/api/javascript/create)

Takes a map of style objects and returns an object of compiled StyleX styles.
The compiled StyleX styles are a mapping of keys to class names.

```ts
function create<T extends {[key: string]: RawStyles | (...any[]) => RawStyles}>(
  styles: T,
): {[Key in keyof T]: StyleXStyles<T[Key]>};
```

### Example use:

```ts
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  root: {
    backgroundColor: 'red',
    padding: '1rem',
    paddingInlineStart: '2rem',
  },
  dynamic: (r, g, b) => ({
    color: `rgb(${r}, ${g}, ${b})`,
  }),
});
```


# stylex.createTheme (/docs/api/javascript/createTheme)

Takes a variable set created with `defineVars()`, and an object used to override
the values of those variables. It returns a `StyleXStyles` object that can be
passed to `props()` to apply the theme to an element root.

```ts
function createTheme(
  vars: Vars,
  overrides: {
    [key: keyof Vars]: string;
  },
): StyleXStyles;
```

### Example use:

```ts
import * as stylex from '@stylexjs/stylex';
import { colors } from './vars.stylex.js';

const theme = stylex.createTheme(colors, {
  accentColor: 'red',
  backgroundColor: 'gray',
  lineColor: 'purple',
  textPrimaryColor: 'black',
  textSecondaryColor: 'brown',
});

function App() {
  return (
    <div {...stylex.props(theme /* , ... */)}>
      <ContentToBeThemed />
    </div>
  );
}
```


# stylex.defineConsts (/docs/api/javascript/defineConsts)

Defines static style constants that can be used directly in `create` calls
anywhere in the codebase. Unlike `defineVars`, these values are inlined at build
time and do not generate actual CSS variables.

*Note: `defineConsts` does not currently have `enableMediaQueryOrder` config
support.*

Common use cases include:

* Media queries
* Fixed z-index layers
* Animation durations or easing curves
* Static spacing, font sizes, or colors that don’t need theming

```ts
function defineConsts<Consts extends { [key: string]: string }>(
  consts: Consts,
): Consts<{ [key in keyof Consts]: string }>;
```

### Example use:

Like `defineVars`, you must define your constants as named exports in a
`.stylex.js` (or `.stylex.ts`) file. You can mix constants and variables in the
same file.

```tsx title="constants.stylex.js"
import * as stylex from '@stylexjs/stylex';

export const breakpoints = stylex.defineConsts({
  small: '@media (max-width: 600px)',
  medium: '@media (min-width: 601px) and (max-width: 1024px)',
  large: '@media (min-width: 1025px)',
});

export const zIndices = stylex.defineConsts({
  modal: '1000',
  tooltip: '1100',
  toast: '1200',
});

export const animations = stylex.defineConsts({
  easeInOut: 'cubic-bezier(0.4, 0, 0.2, 1)',
  fast: '150ms',
});
```

You can then import and use these constants in any `create` call:

```tsx
import * as stylex from '@stylexjs/stylex';
import { breakpoints, zIndices, animations } from './constants.stylex.js';

const styles = stylex.create({
  container: {
    position: 'relative',
    zIndex: zIndices.modal,
    transitionTimingFunction: animations.easeInOut,
    transitionDuration: animations.fast,
    color: {
      default: 'black',
      [breakpoints.small]: 'red',
      [breakpoints.medium]: 'blue',
      [breakpoints.large]: 'green',
    },
    padding: {
      default: 4,
      [breakpoints.medium]: 8,
      [breakpoints.large]: 16,
    },
  },
});
```


# stylex.defineVars (/docs/api/javascript/defineVars)

Creates global CSS Custom Properties (variables) that can be imported and used
within `create` calls anywhere within a codebase.

```ts
function defineVars<Styles extends { [key: string]: Value }>(
  styles: Styles,
): Vars<{ [key in keyof Styles]: string }>;
```

By default, `defineVars` will create unique, hashed variable names. To create
variables with custom names use a key that starts with `--`. These will generate
CSS custom properties with the provided name instead of generating a globally
unique name.

### Example use:

You must define your variables as named exports in a `.stylex.js` (or
`.stylex.ts`) file.

```tsx title="vars.stylex.js"
import * as stylex from '@stylexjs/stylex';

export const colors = stylex.defineVars({
  accent: 'blue',
  line: 'gray',
  '--background': 'black',
});
```

You can then import and use these variables in any `create` call.

```tsx
import * as stylex from '@stylexjs/stylex';
import { colors } from './vars.stylex.js';

const styles = stylex.create({
  container: {
    color: colors.accent,
    backgroundColor: colors['--background'],
  },
});
```


# stylex.env.* (/docs/api/javascript/env)

Allows the user to configure shareable tokens and functions to be used within StyleX APIs. Values are configured through the babel config.

<Callout type="info">
  `env` is an experimental API that is subject to change.
</Callout>

```ts
const env: { [key: string]: mixed };
```

Values are replaced before compilation, so identical values always
deduplicate into a single CSS rule. Unlike `defineConsts`, no additional CSS is
generated.

### Example use:

Configure env values in your
[babel plugin options](/docs/api/configuration/babel-plugin/#env):

```js title="babel.config.js"
module.exports = {
  plugins: [
    ['@stylexjs/babel-plugin', {
      env: {
        tokens: {
          colors: {
            primary: '#0066ff',
            secondary: '#ff6600',
            background: 'white',
            text: 'black',
          },
          spacing: {
            small: '4px',
            medium: '8px',
            large: '16px',
          },
        },
      },
    }],
  ],
};
```

Then use them in any StyleX call:

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  root: {
    color: stylex.env.tokens.colors.primary,
    backgroundColor: stylex.env.tokens.colors.background,
    padding: stylex.env.tokens.spacing.medium,
  },
});
```

Nested objects can be passed directly to other StyleX APIs:

```tsx title="tokens.stylex.js"
import * as stylex from '@stylexjs/stylex';

export const colors = stylex.defineVars(stylex.env.tokens.colors);
```

### Functions

Define shareable functions using the `env` API. Functions
must be pure and return strings or numbers.

```js title="babel.config.js"
module.exports = {
  plugins: [
    ['@stylexjs/babel-plugin', {
      env: {
        opacity: (color, pct) =>
          `color-mix(in srgb, ${color} ${pct * 100}%, transparent)`,
        colorMix: (c1, c2, pct) =>
          `color-mix(in srgb, ${c1} ${pct}%, ${c2})`,
      },
    }],
  ],
};
```

```tsx
import * as stylex from '@stylexjs/stylex';
import { colors } from './tokens.stylex';

const styles = stylex.create({
  root: {
    backgroundColor: stylex.env.colorMix(colors.primary, 'black', 80),
    boxShadow: `0 4px 4px ${stylex.env.opacity(colors.primary, 0.35)}`,
  },
});
```

### TypeScript usage

You can use *module declaration* to override the `env` type to match your exact
usage. You only need to do this once per project. As long as this file is
included by your `tsconfig` it'll override the `env` type in all other files in this
project.

*Note: This approach doesn't currently check whether this type matches what
you're passing to
[babel plugin options](/docs/api/configuration/babel-plugin/#env).*

```tsx
declare module '@stylexjs/stylex/lib/types/StyleXTypes' {
  interface Register {
    env: {
      tokens: {
        colors: {
          primary: string;
        };
      };
    };
  }
}

// Usage
stylex.env.tokens.colors.primary; // Type checks correctly and you get intellisense
```


# stylex.firstThatWorks (/docs/api/javascript/firstThatWorks)

Declare an ordered list of fallback values for a style property.

All of the fallbacks are included in the generated styles so that the first
supported style within the list takes effect within the browser.

```ts
function firstThatWorks<Values extends Array<string | number>>(
  ...styles: Values
): Values[number];
```

### Example use:

```js
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  header: {
    position: stylex.firstThatWorks('sticky', '-webkit-sticky', 'fixed'),
  },
});
```


# stylex.keyframes (/docs/api/javascript/keyframes)

Takes a keyframes definition, creates a `@keyframes` rule, and returns the
keyframe name.

```ts
function keyframes(frames: { [key: string]: RawStyles }): string;
```

You must declare your keyframes in the same file as where you use them.
Duplicate declarations will be deduplicated in the generated CSS output.

### Example use:

```tsx
import * as stylex from '@stylexjs/stylex';

const pulse = stylex.keyframes({
  '0%': { transform: 'scale(1)' },
  '50%': { transform: 'scale(1.1)' },
  '100%': { transform: 'scale(1)' },
});

const styles = stylex.create({
  pulse: {
    animationName: pulse,
    animationDuration: '1s',
    animationIterationCount: 'infinite',
  },
});
```

To chain multiple keyframes, provide comma-separated values to animation
properties:

```tsx
const expand = stylex.keyframes({
  from: { maxHeight: '0px' },
  to: { maxHeight: '1000px' },
});

const fadeIn = stylex.keyframes({
  from: { opacity: 0 },
  to: { opacity: 1 },
});

const styles = stylex.create({
  open: {
    animationName: `${fadeIn}, ${expand}`,
    animationDuration: '1s, 1s',
  },
});
```

To use `keyframes` return values in a separate file, you can use `defineVars` to
hold animation names:

```tsx title="animations.stylex.js"
import * as stylex from '@stylexjs/stylex';

const pulse = stylex.keyframes({
  '0%': { transform: 'scale(1)' },
  '50%': { transform: 'scale(1.1)' },
  '100%': { transform: 'scale(1)' },
});

const fadeIn = stylex.keyframes({
  '0%': { opacity: 0 },
  '100%': { opacity: 1 },
});

const fadeOut = stylex.keyframes({
  '0%': { opacity: 1 },
  '100%': { opacity: 0 },
});

export const animations = stylex.defineVars({
  pulse,
  fadeIn,
  fadeOut,
});
```

These variables can then be imported and used like any other variables created
with `defineVars`.


# stylex.positionTry (/docs/api/javascript/positionTry)

Creates a
[`@position-try`](https://developer.mozilla.org/en-US/docs/Web/CSS/@position-try)
rule used to define a custom position-try fallback option, which can be used to
define positioning and alignment for anchor-positioned elements. One or more
sets of position-try fallback options can be applied to the anchored element via
the `positionTryFallbacks` property.

```ts
function positionTry(descriptors: { [key: string]: RawStyles }): string;
```

The only properties allowed in a `positionTry` call are `positionAnchor`,
`positionArea`, inset properties (`top`, `left`, `insetInline`, etc.), margin
properties, size properties (`height`, `inlineSize`, etc.), and self-alignment
properties (`alignSelf`, `justifySelf`, `placeSelf`).

You must declare your position-try rules in the same file as where you use them.
Duplicate declarations will be deduplicated in the generated CSS output.

### Example use:

```tsx
import * as stylex from '@stylexjs/stylex';

const fallback = stylex.positionTry({
  positionAnchor: '--anchor',
  top: '0',
  left: '0',
  width: '100px',
  height: '100px',
});

const styles = stylex.create({
  anchor: {
    positionTryFallbacks: fallback,
  },
});
```

To use `positionTry` return values in a separate file, you can use `defineVars`
to hold position fallback values:

```tsx title="positionFallbacks.stylex.js"
import * as stylex from '@stylexjs/stylex';

const topLeftCorner = stylex.positionTry({
  positionAnchor: '--anchor',
  top: '0',
  left: '0',
  width: '100px',
  height: '100px',
});

export const positionFallbacks = stylex.defineVars({
  topLeftCorner,
});
```

These variables can then be imported and used like any other variables created
with `defineVars`.


# stylex.props (/docs/api/javascript/props)

Takes a StyleX style or array of StyleX styles, and returns a props object.
Values can also be `null`, `undefined`, or `false`.

The return value should be spread onto an element to apply the styles directly.

```ts
function props(styles: StyleXStyles | StyleXStyles[]): {
  className: string;
  style: { [key: string]: string };
};
```

### Example use:

```jsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  root: {
    backgroundColor: 'red',
    padding: '1rem',
    paddingInlineStart: '2rem',
  },
  conditional: {
    backgroundColor: 'blue',
  },
  dynamic: (opacity) => ({
    opacity,
  }),
});

<div
  {...stylex.props(
    styles.root,
    condition && styles.conditional,
    props.style,
    styles.dynamic(state.opacity),
  )}
/>;
```

### Not using React?

<Callout type="tip" title="For Solid, Svelte, Qwik, Vue">
  For frameworks that expect `class` instead of `className`, and expect `style` to
  be a string instead of an object, you can wrap use of the `props` API with the
  function below.

  ```js
  export function attrs({ className, 'data-style-src': dataStyleSrc, style }) {
    const result = {};
    // Convert className to class
    if (className != null && className !== '') {
      result.class = className;
    }
    // Convert style object to string
    if (style != null && Object.keys(style).length > 0) {
      result.style = Object.keys(style)
        .map((key) => `${key}:${style[key]};`)
        .join('');
    }
    if (dataStyleSrc != null && dataStyleSrc !== '') {
      result['data-style-src'] = dataStyleSrc;
    }
    return result;
  }
  ```

  Example use:

  ```js
  <div {...attrs(stylex.props(...styles))} />
  ```
</Callout>


# stylex.types.* (/docs/api/javascript/types)

A set of helper functions to be used within
[`defineVars`](/docs/api/javascript/defineVars) and
[`createTheme`](/docs/api/javascript/createTheme) to define CSS types for
variables.

These functions result in `@property` CSS rules for the variables with the
appropriate `syntax` value.

### Example use:

The `types.*` functions are compatible with all patterns that are supported by
`defineVars` and `createTheme` already.

For example, consider the following set of variables:

```tsx title="vars.stylex.js"
import * as stylex from '@stylexjs/stylex';

export const colors = stylex.defineVars({
  accent: {
    default: 'blue',
    '@media (prefers-color-scheme: dark)': 'lightblue',
  },
  sm: '4px',
});
```

You can give the two variables types like so:

```tsx title="vars.stylex.js"
import * as stylex from '@stylexjs/stylex';

export const colors = stylex.defineVars({
  accent: stylex.types.color({
    default: 'blue',
    '@media (prefers-color-scheme: dark)': 'lightblue',
  }),
  sm: stylex.types.length('4px'),
});
```

## Available types

The following types are available:

### `stylex.types.angle`

Generates a
[`@property` rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@property)
for the generated CSS variable with a
[`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/angle)
[syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/@property/syntax).

### `stylex.types.color`

Generates a
[`@property` rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@property)
for the generated CSS variable with a
[`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value)
[syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/@property/syntax).

### `stylex.types.url`

Generates a
[`@property` rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@property)
for the generated CSS variable with a
[`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/url)
[syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/@property/syntax).

### `stylex.types.image`

Generates a
[`@property` rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@property)
for the generated CSS variable with an
[`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/image)
[syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/@property/syntax).

### `stylex.types.integer`

Generates a
[`@property` rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@property)
for the generated CSS variable with an
[`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/integer)
[syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/@property/syntax).

### `stylex.types.lengthPercentage`

Generates a
[`@property` rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@property)
for the generated CSS variable with a
[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/length-percentage)
[syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/@property/syntax).

### `stylex.types.length`

Generates a
[`@property` rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@property)
for the generated CSS variable with a
[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/length)
[syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/@property/syntax).

### `stylex.types.percentage`

Generates a
[`@property` rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@property)
for the generated CSS variable with a
[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/percentage)
[syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/@property/syntax).

### `stylex.types.number`

Generates a
[`@property` rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@property)
for the generated CSS variable with a
[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/number)
[syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/@property/syntax).

### `stylex.types.resolution`

Generates a
[`@property` rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@property)
for the generated CSS variable with a
[`<resolution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/resolution)
[syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/@property/syntax).

### `stylex.types.time`

Generates a
[`@property` rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@property)
for the generated CSS variable with a
[`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/time)
[syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/@property/syntax).

### `stylex.types.transformFunction`

Generates a
[`@property` rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@property)
for the generated CSS variable with a
[`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function)
[syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/@property/syntax).

### `stylex.types.transformList`

Generates a
[`@property` rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@property)
for the generated CSS variable with a
[`<transform-list>`](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function)
[syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/@property/syntax).


# stylex.viewTransitionClass (/docs/api/javascript/viewTransitionClass)

Creates a set of `::view-transition` pseudo-element rules tied to a single class
name which can be utilized for customizing the animations in a
[View Transition](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API).

<Callout type="info">
  The styles that `viewTransitionClass` accepts don't currently support media
  queries but adding support for them is a planned enhancement.
</Callout>

```ts
type ViewTransitionClassOptions = Readonly<{
  group?: RawStyles;
  imagePair?: RawStyles;
  old?: RawStyles;
  new?: RawStyles;
}>;
function viewTransitionClass(options: ViewTransitionClassOptions): string;
```

The options object the `viewTransitionClass` function takes in accepts the
following keys which map to a corresponding View Transition pseudo-element:

* `group` -> `::view-transition-group(*.theGeneratedClass)`
* `imagePair` -> `::view-transition-image-pair(*.theGeneratedClass)`
* `old` -> `::view-transition-old(*.theGeneratedClass)`
* `new` -> `::view-transition-new(*.theGeneratedClass)`

This method returns the generated class name as a string which can be added
manually to the elements you want animations customized for, or if you're using
React can be passed into the experimental
[`<ViewTransition />`](https://react.dev/reference/react/ViewTransition)
component.

### Example use:

```tsx
import * as stylex from '@stylexjs/stylex';
import { unstable_ViewTransition as ViewTransition } from 'react';

const lingeringOldView = stylex.viewTransitionClass({
  new: {
    animationDuration: '1s',
  },
  old: {
    animationDuration: '2s',
  },
});

<ViewTransition default={lingeringOldView}>{/* ... */}</ViewTransition>;
```

`viewTransitionClass` calls can also accept
[`keyframes`](/docs/api/javascript/keyframes) output to customize the animations
even further:

```tsx
import * as stylex from '@stylexjs/stylex';

const fadeInUp = stylex.keyframes({
  from: {
    opacity: 0,
    transform: 'translateY(-30px)',
  },
  to: {
    opacity: 1,
    transform: 'translateY(0px)',
  },
});

const transitionCls = stylex.viewTransitionClass({
  new: {
    animationName: fadeInUp,
  },
});
```


# stylex.when.* (/docs/api/javascript/when)

A suite of APIs for creating descendant and sibling selectors. These let you
style an element based on the state of its ancestors, descendants, or siblings
in the DOM tree. You can observe pseudo-class states (`:hover`, `:focus`, etc.)
or attribute selectors (e.g., `[data-panel-state="open"]`) on an element that
has been marked with a marker class.

> Note: lookahead selectors (`stylex.when.siblingAfter`,
> `stylex.when.anySibling`, and `stylex.when.descendant`) rely on the CSS
> `:has()` selector, which does not yet have
> [wide browser support](https://caniuse.com/css-has).

## Using markers

To use descendant and sibling selectors, mark the ancestor, sibling, or
descendant node being observed by passing the `stylex.defaultMarker()` class
name.

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  foo: {
    backgroundColor: {
      default: 'blue',
      [stylex.when.ancestor(':hover')]: 'red',
    },
  },
});

<div {...stylex.props(stylex.defaultMarker())}>
  <div {...stylex.props(styles.foo)}>Some content</div>
</div>;
```

## Available selectors

### `stylex.when.ancestor`

Style an element based on the state of an ancestor element in the DOM tree.

```ts
function ancestor(pseudoSelector: string, marker?: Marker): string;
```

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  card: {
    transform: {
      default: 'translateX(0)',
      [stylex.when.ancestor(':hover')]: 'translateX(10px)',
    },
  },
});

<div {...stylex.props(stylex.defaultMarker())}>
  <div {...stylex.props(styles.card)}>Hover the parent to move me</div>
</div>;
```

### `stylex.when.descendant`

Style an element based on the state of a descendant element in the DOM tree.

```ts
function descendant(pseudoSelector: string, marker?: Marker): string;
```

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  container: {
    borderColor: {
      default: 'gray',
      [stylex.when.descendant(':focus')]: 'blue',
    },
  },
});

<div {...stylex.props(styles.container)}>
  <input {...stylex.props(stylex.defaultMarker())} />
</div>;
```

### `stylex.when.anySibling`

Style an element based on the state of any sibling element (before or after).

```ts
function anySibling(pseudoSelector: string, marker?: Marker): string;
```

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  tab: {
    opacity: {
      default: 1,
      [stylex.when.anySibling(':hover')]: 0.7,
    },
  },
});

<>
  <div {...stylex.props(styles.tab, stylex.defaultMarker())}>Tab 1</div>
  <div {...stylex.props(styles.tab, stylex.defaultMarker())}>Tab 2</div>
  <div {...stylex.props(styles.tab, stylex.defaultMarker())}>Tab 3</div>
</>;
```

### `stylex.when.siblingBefore`

Style an element based on the state of a preceding sibling element.

```ts
function siblingBefore(pseudoSelector: string, marker?: Marker): string;
```

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  item: {
    backgroundColor: {
      default: 'white',
      [stylex.when.siblingBefore(':focus')]: 'lightblue',
    },
  },
});

<>
  <button {...stylex.props(stylex.defaultMarker())}>Focus me</button>
  <div {...stylex.props(styles.item)}>I change when the button is focused</div>
</>;
```

### `stylex.when.siblingAfter`

Style an element based on the state of a following sibling element.

```ts
function siblingAfter(pseudoSelector: string, marker?: Marker): string;
```

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  label: {
    color: {
      default: 'black',
      [stylex.when.siblingAfter(':focus')]: 'blue',
    },
  },
});

<>
  <label {...stylex.props(styles.label)}>Name</label>
  <input {...stylex.props(stylex.defaultMarker())} />
</>;
```

## Using custom markers

Custom markers created with `stylex.defineMarker()` let you have multiple
independent sets of contextual selectors in the same component tree. For
example, a table cell could have different styling depending on whether
the cell itself is being hovered, or whether its row is being hovered:

```tsx
// markers.stylex.js
import * as stylex from "@stylexjs/stylex";
export const rowMarker = stylex.defineMarker();
export const cellMarker = stylex.defineMarker();

```

```tsx
import * as stylex from "@stylexjs/stylex";
import { cellMarker, rowMarker } from "./markers.stylex.js";

const styles = stylex.create({
  editButton: {
    visibility: {
      // Show button when row is hovered
      default: 'hidden',
      [stylex.when.ancestor(':hover', rowMarker)]: 'visible',
    },
    opacity: {
      // Dim the button unless the cell itself is hovered
      default: 0.4,
      [stylex.when.ancestor(':hover', cellMarker)]: 1,
    },
  },
});

function Row({ children }) {
  return <tr {...stylex.props(rowMarker)}>{children}</tr>;
}

function Cell({ children }) {
  return (<td {...stylex.props(cellMarker)}>{children}</td>);
}

function EditableContents({children}) {
  return (
    <>
      {children}
      <button {...stylex.props(styles.editButton)}>Edit</button>
    </>
  );
}

export default function App() {
  return (
    <table>
      <Row>
        <Cell><EditableContents>Daniel</EditableContents></Cell>
        <Cell>1234</Cell>
      </Row>
      <Row>
        <Cell><EditableContents>Test</EditableContents></Cell>
        <Cell>Two</Cell>
      </Row>
    </table>
  );
}

```

## Specificity ranking

`stylex.when.*` selectors have lower priority than regular pseudo-classes or
media queries. When multiple `stylex.when.*` selectors apply to the same
element, they are ordered by specificity:

1. `ancestor` (lowest specificity)
2. `descendant`
3. `anySibling`
4. `siblingBefore`
5. `siblingAfter` (highest specificity)


# StaticStyles<> (/docs/api/types/StaticStyles)

A type that allows only static styles generated by StyleX and disallows inline
styles. i.e. Dynamic styles defined using functions are not allowed.

It also allows the styles to be nested within arrays and be arbitrarily deep.
Further, `null`, `undefined` and `false` are always accepted.

Further, you can pass in an object type to constrain the styles to specific
properties and values:

```tsx
import type { StaticStyles } from '@stylexjs/stylex';

type Props = {
  // ...
  style?: StaticStyles<{
    color?: 'red' | 'blue' | 'green';
    padding?: 0 | 4 | 8 | 16 | 32;
    backgroundColor?: string;
    borderColor?: string;
    borderTopColor?: string;
    borderEndColor?: string;
    borderBottomColor?: string;
    borderStartColor?: string;
  }>;
};
```

Any key not defined in the object type will be disallowed.

<Callout type="danger" title="Only known keys are checked">
  Due to a
  [TypeScript limitation](https://github.com/Microsoft/TypeScript/issues/12936),
  any key not in your custom object type will only be disallowed if it's one of
  the known style properties in the internal StyleX types.

  TypeScript will not error if you pass an additional unknown key.
</Callout>


# StyleXStyles<> (/docs/api/types/StyleXStyles)

A type that allows any styles generated by StyleX.

It also allows the styles to be nested within arrays and be arbitrarily deep.
Further, `null`, `undefined` and `false` are always accepted.

Further, you can pass in an object type to constrain the styles to specific
properties and values:

```tsx
import type { StyleXStyles } from '@stylexjs/stylex';

type Props = {
  // ...
  style?: StyleXStyles<{
    color?: 'red' | 'blue' | 'green';
    padding?: 0 | 4 | 8 | 16 | 32;
    backgroundColor?: string;
    borderColor?: string;
    borderTopColor?: string;
    borderEndColor?: string;
    borderBottomColor?: string;
    borderStartColor?: string;
  }>;
};
```

Any key not defined in the object type will be disallowed.

<Callout type="danger" title="Only known keys are checked">
  Due to a
  [TypeScript limitation](https://github.com/Microsoft/TypeScript/issues/12936),
  any key not in your custom object type will only be disallowed if it's one of
  the known style properties in the internal StyleX types.

  TypeScript will not error if you pass an additional unknown key.
</Callout>


# StyleXStylesWithout<> (/docs/api/types/StyleXStylesWithout)

Allow any styles except for keys defined in the provided object type. It works
similarly to the `Omit<>` utility type.

```tsx
import type { StyleXStylesWithout } from '@stylexjs/stylex';

type Props = {
  // ...
  style?: StyleXStylesWithout<{
    position: unknown;
    display: unknown;
    top: unknown;
    start: unknown;
    end: unknown;
    bottom: unknown;
    border: unknown;
    borderWidth: unknown;
    borderBottomWidth: unknown;
    borderEndWidth: unknown;
    borderStartWidth: unknown;
    borderTopWidth: unknown;
    margin: unknown;
    marginBottom: unknown;
    marginEnd: unknown;
    marginStart: unknown;
    marginTop: unknown;
    padding: unknown;
    paddingBottom: unknown;
    paddingEnd: unknown;
    paddingStart: unknown;
    paddingTop: unknown;
    width: unknown;
    height: unknown;
    flexBasis: unknown;
    overflow: unknown;
    overflowX: unknown;
    overflowY: unknown;
  }>;
};
```

This type will disallow all the keys which are known to cause layout changes,
but will continue to allow all other style properties.


# Theme<> (/docs/api/types/Theme)

```tsx
type Theme<T extends VarGroup<unknown, symbol>>
```

A `Theme` is a type that represents a style that *themes* a set of variables in
a given `VarGroup`. It's the result of calling
[`createTheme`](/docs/api/javascript/createTheme).

```tsx
import type { VarGroup } from '@stylexjs/stylex';
import * as stylex from '@stylexjs/stylex';

import { vars } from './vars.stylex';

export const theme: Theme<typeof vars> = stylex.createTheme(vars, {
  color: 'red', // OK
  backgroundColor: 'blue', // OK
});
```

The most common use-case for `Theme` is to accept a theme for a particular set
of variables.

While it's not needed in most cases, `Theme` also accepts an optional second
type argument.

<Accordion title="Advanced use-case: unique type identity for a Theme">
  Two themes for the same `VarGroup` have the same type by default. In most cases,
  this is the desired behavior. However, in some cases, you may want each theme to
  have a unique type identity to constrain the themes that can be passed into a
  particular component.

  ```tsx
  import * as stylex from '@stylexjs/stylex';
  import type { Theme } from '@stylexjs/stylex';
  import { vars } from './vars.stylex';

  declare const Tag: unique symbol;
  export const theme1: Theme<typeof vars, Tag> = stylex.createTheme(vars, {
    color: 'red', // OK
    backgroundColor: 'blue', // OK
  });
  ```

  Now, `theme1` has a unique type identity and a different `Theme` for `vars`
  would not satisfy `typeof theme1`.

  This advanced use-case should be rarely needed, but it's available when it is.
</Accordion>


# VarGroup<> (/docs/api/types/VarGroup)

```tsx
type VarGroup<Tokens extends {}>
```

A `VarGroup` is the type of the object that is generated as a result of calling
[`defineVars`](/docs/api/javascript/defineVars). It maps keys to references to
CSS custom properties.

`VarGroup` is also the required type for the first argument to
[`createTheme`](/docs/api/javascript/createTheme)

Usually, `VarGroup` is not needed explicitly, as it can be inferred from the
argument to `defineVars`.

```tsx
import * as stylex from '@stylexjs/stylex';

export const vars = stylex.defineVars({
  color: 'red',
  backgroundColor: 'blue',
});

export type Vars = typeof vars;
/*
  Vars = VarGroup<{
    color: string,
    backgroundColor: string,
  }>
*/
```

In some cases, however, `VarGroup` may be needed explicitly, to constrain the
values of the variables within themes:

```tsx
import * as stylex from '@stylexjs/stylex';
import type { VarGroup } from '@stylexjs/stylex';

const vars: VarGroup<{
  color: 'red' | 'blue' | 'green' | 'yellow';
  backgroundColor: 'red' | 'blue' | 'green' | 'yellow';
}> = stylex.defineVars({
  color: 'red',
  backgroundColor: 'blue',
});
```

Now when a theme for `vars` is being created, the values for `color` and
`backgroundColor` can only be one of the specified values.

```tsx
import * as stylex from '@stylexjs/stylex';
import { vars } from './vars.stylex';

export const theme1 = stylex.createTheme(vars, {
  color: 'red', // OK
  backgroundColor: 'blue', // OK
});

export const theme2 = stylex.createTheme(vars, {
  // Error: 'orange' is not assignable to 'red' | 'blue' | 'green' | 'yellow'
  color: 'orange',
});
```

While it's not needed in most cases, `VarGroup` also accepts an optional second
type argument.

<Details>
  <Summary>
    Advanced use-case: unique type identity for a 

    `VarGroup`
  </Summary>

  TypeScript (and Flow) use structural typing, which means that two objects with
  the same shape are considered to be the same type. However, each usage of
  `defineVars` results in a new set of variables.

  It can be useful to have a unique type identity for each `VarGroup` created to
  be able to distinguish between them and accept themes for only a specific
  `VarGroup`. This is also known as "nominal typing" and can be achieved by using
  a unique symbol as the second type argument to `VarGroup`.

  The complete type signature of `VarGroup` is:

  ```tsx
  type VarGroup<Tokens extends {}, ID extends symbol = symbol>
  ```

  It can be used like this:

  ```tsx
  import * as stylex from '@stylexjs/stylex';
  import type { VarGroup } from '@stylexjs/stylex';

  type Shape = {
    color: string;
    backgroundColor: string;
  };

  declare const BaseColors: unique symbol;
  export const baseColors: VarGroup<Shape, typeof BaseColors> = stylex.defineVars(
    {
      color: 'red',
      backgroundColor: 'blue',
    },
  );

  declare const CardColors: unique symbol;
  export const cardColors: VarGroup<Shape, typeof CardColors> = stylex.defineVars(
    {
      color: 'red',
      backgroundColor: 'blue',
    },
  );
  ```

  Here `baseColors` and `cardColors` are `VarGroup` objects of the same shape, but
  with two distinct type identities. This ensures that a `Theme` for one can't be
  used with the other.

  It should be rare that two separate `VarGroup` objects are defined with the same
  shape and so this feature is not needed in most cases. In the rare cases where
  it *is* needed, it is available.
</Details>


# Documentation (/docs)

StyleX combines the ergonomics of authoring styles inline with the
predictability and performance of atomic CSS. These docs are now powered by
Fumadocs and include all of the learning material and API references from the
original site.

<Cards>
  <Card title="Start Learning" description="Guides that walk through core concepts, theming, recipes, and more." href="/docs/learn" />

  <Card title="API Reference" description="Detailed configuration, runtime, and typing APIs for StyleX." href="/docs/api" />
</Cards>


# Introduction (/docs/learn)

StyleX combines the strengths and avoids the weaknesses of both inline styles
and static CSS. Defining and using styles requires only local knowledge within a
component, and avoids specificity issues while retaining features like Media
Queries. StyleX builds optimized styles using collision-free atomic CSS which is
superior to what could be authored and maintained by hand.

## Features at a glance

<Cards>
  <Card
    title="Scalable"
    description={
    <ul>
      <li>Minimize CSS output with atomic CSS</li>
      <li>The CSS size plateaus as the codebase grows</li>
      <li>Styles remain maintainable within growing codebases</li>
    </ul>
  }
  />

  <Card
    title="Predictable"
    description={
  <ul>
    <li>No "style at a distance"</li>
    <li>No specificity issues</li>
    <li>“The last style applied always wins!”</li>
  </ul>
}
  />

  <Card
    title="Composable"
    description={
  <ul>
    <li>Apply styles conditionally</li>
    <li>Merge and compose arbitrary styles</li>
    <li>Pass around styles as props</li>
  </ul>
}
  />

  <Card
    title="Fast"
    description={
  <ul>
    <li>No runtime style injection</li>
    <li>Generate a static CSS file at compile-time</li>
    <li>Tiny and fast runtime for merging class names</li>
  </ul>
}
  />

  <Card
    title="Type-Safe"
    description={
  <ul>
    <li>Type-safe APIs</li>
    <li>Type-safe styles</li>
    <li>Type-safe themes</li>
  </ul>
}
  />
</Cards>

## Using StyleX

### Configure the compiler

See the [Installation](/docs/learn/installation) guide.

### Define styles

Styles are defined using an object syntax and the `create()` API.

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  root: {
    width: '100%',
    maxWidth: 800,
    minHeight: 40,
  },
});
```

Any number of rules can be created by using additional keys and additional calls
to `create()`:

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  root: {
    width: '100%',
    maxWidth: 800,
    minHeight: 40,
  },
  child: {
    backgroundColor: 'black',
    marginBlock: '1rem',
  },
});

const colorStyles = stylex.create({
  red: {
    backgroundColor: 'red',
    borderColor: 'darkred',
  },
  green: {
    backgroundColor: 'lightgreen',
    borderColor: 'darkgreen',
  },
});

function ReactDiv({ color, isActive, style }) {
  /* ... */
}
```

### Use styles

To use styles they must be passed to the `props()` function. Styles can be
combined and applied conditionally using standard JavaScript expressions.

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({ ... });
const colorStyles = stylex.create({ ... });

function ReactDiv({ color, isActive, style }) {
  return <div {...stylex.props(
    styles.main,
    // apply styles conditionally
    isActive && styles.active,
    // choose a style variant based on a prop
    colorStyles[color],
    // styles passed as props
    style,
  )} />;
}
```

The example above uses JSX. StyleX itself is framework agnostic. The same code
works with other frameworks that accept `className` strings and `style` objects
such as `SolidJS`, `Preact` or `Qwik`.

## Ideal use cases

StyleX works well in a wide variety of projects. However, it was designed to
meet the challenges of particular use cases.

### Authoring UI in JavaScript

StyleX is a CSS-in-JS library, which means that it is most useful when an app's
UI is authored in JavaScript. If an application uses a framework like React,
Preact, Solid, lit-html, or Angular, using StyleX should be a good fit.

Some frameworks, such as Svelte and Vue use custom file formats that are
compiled to JavaScript at build time. StyleX can still be used in these
frameworks, but may need some custom configuration.

### Large or growing projects

While StyleX works well for projects of all sizes, it really shines in larger
applications.

Since StyleX compiles to atomic class names, a big performance benefit is that
the size of the CSS bundle plateaus as a project grows.

### Reusable components

The benefits of StyleX are greatest when used alongside reusable UI components.

For years, we have had to choose between "Design System" components that come
with styles baked in but can be difficult to customize or "Headless" components
that are completely unstyled.

StyleX empowers developers to build UI components that can have default styles
*and* still be customizable.

Further, the consistency enables sharing these components by publishing them to
NPM. As long as the consumer of a component is also using StyleX, the styles
will be merged and composed correctly without any additional configuration.


# CLI (/docs/learn/installation/cli)

When none of the other integrations work, the StyleX CLI can be used to
pre-transform an entire directory of files to compile away StyleX and generate a
static CSS file which runs *before* the rest of your build pipeline.

The only requirement for using the CLI is that your bundler is able to handle
CSS imports, as the CLI inserts an import for the generated CSS file into every
file that was transformed.

## Install

Start by installing the StyleX CLI:

<DevInstallExample dev={[`@stylexjs/cli`]} />

## Configuration

Although all options for the CLI are available as command line arguments, using
a configuration file is recommended. The configuration file can be in either
JSON or JSON5 format. Using JSON5 lets you skip quotes around object keys, and
use comments and trailing commas.

```js
{
  input: ['./source'],           // Where your StyleX source lives
  output: ['./src'],             // Where compiled files + CSS bundle are written
  cssBundleName: 'stylex_bundle.css',
  babelPresets: [
    ['@babel/preset-typescript', { allExtensions: true, isTSX: true }],
  ],
  styleXConfig: {
    aliases: {
      '@/*': ['./source/*'],
    },
  },
  // watch: true, // enable for incremental rebuilds
}
```

The configuration file can be named anything, as it is always passed explicitly
to the CLI using the `--config` flag.

## Using the CLI

Run the compiler with:

```json
{
  "scripts": {
    "build": "stylex --config .stylex.json5",
    "watch": "stylex --config .stylex.json5 --watch"
  }
}
```

You can add additional command line arguments, such as `--watch` for incremental
rebuilds.

You can also define multiple configuration files for different environments.


# Esbuild (/docs/learn/installation/esbuild)

[`examples/example-esbuild`](https://github.com/facebook/stylex/tree/main/examples/example-esbuild)
bundles a React app with esbuild and compiles StyleX via `@stylexjs/unplugin`.
The unplugin extracts StyleX styles, aggregates them, and appends the output to
the CSS asset produced by esbuild.

## Install

<DevInstallExample dev={[`@stylexjs/unplugin`]} />

## Configure the build

Wire the unplugin into your esbuild script:

```js
import esbuild from 'esbuild';
import stylex from '@stylexjs/unplugin';

esbuild.build({
  entryPoints: ['src/App.jsx'],
  bundle: true,
  metafile: true, // lets StyleX find the emitted CSS asset
  plugins: [
    stylex.esbuild({
      useCSSLayers: true,
      importSources: ['@stylexjs/stylex'],
      unstable_moduleResolution: { type: 'commonJS' },
      // ... other StyleX configuration
    }),
  ],
});
```

Ensure `metafile: true` so the plugin can locate the CSS output.

## CSS entrypoint

Ensure that there is one CSS file that is imported from your root layout
component or JS entry point.


# Installation (/docs/learn/installation)

## Runtime

All uses of StyleX require the runtime package to be installed.

<DevInstallExample prod={[`@stylexjs/stylex`]} />

## ESLint

Use ESLint to catch mistakes. StyleX has a forgiving compiler that will compile
invalid styles. The StyleX ESLint plugin will flag invalid styles and provide
fixes for common errors.

<DevInstallExample dev={[`@stylexjs/eslint-plugin`]} />

```tsx title=".eslintrc.js"
module.exports = {
  plugins: ['@stylexjs'],
  rules: {
    '@stylexjs/valid-styles': 'error',
    '@stylexjs/no-unused': 'error',
    '@stylexjs/valid-shorthands': 'warn',
    '@stylexjs/sort-keys': 'warn',
  },
};
```

## Compiler

StyleX offers multiple ways to transform StyleX styles into CSS. Guides for
setting up the StyleX transformation pipeline for various bundler and framework
setups follow below:

* [Next.js](/docs/learn/installation/nextjs)
* [Vite](/docs/learn/installation/vite)
  * [React](/docs/learn/installation/vite/vite-react)
  * [React Server Components](/docs/learn/installation/vite/vite-rsc)
  * [React Router](/docs/learn/installation/vite/react-router)
  * [RedwoodSDK](/docs/learn/installation/vite/redwoodsdk)
  * [Waku](/docs/learn/installation/vite/waku)
* [Webpack](/docs/learn/installation/webpack)
* [Rspack](/docs/learn/installation/rspack)
* [Esbuild](/docs/learn/installation/esbuild)

You can also choose to use the [CLI](/docs/learn/installation/cli) or the
[PostCSS plugin](/docs/learn/installation/postcss), for more custom setups.

The recommended way to use StyleX in development and production is with the
build-time compiler. This can be done with any bundler that supports Babel -
using the metadata generated by the StyleX plugin - and with PostCSS.

<DevInstallExample dev={[`@stylexjs/babel-plugin`, `@stylexjs/postcss-plugin`, `postcss`]} />

Bundler- and framework-specific guides live under this Installation section. You
can also check the
[StyleX examples](https://github.com/facebook/stylex/tree/main/examples) to see
the same setups in runnable projects.

### Babel

You must configure your project's `.babelrc` file for StyleX to work as
expected. Please see the
[Babel plugin API reference](/docs/api/configuration/babel-plugin/) for more
details.

```tsx title=".babelrc.js"
module.exports = {
  presets: [
    ...
  ],
  plugins: [
    ...,
    [
      "@stylexjs/babel-plugin",
      {
        dev: process.env.NODE_ENV === "development",
        test: process.env.NODE_ENV === "test",
        runtimeInjection: false,
        treeshakeCompensation: true,
        unstable_moduleResolution: {
          type: "commonJS",
        },
      },
    ],
  ],
};
```

### PostCSS

PostCSS provides a versatile way to integrate StyleX into your project. Create a
`postcss.config.js` file in your project root and add the StyleX plugin to it.

```tsx title="postcss.config.js"
module.exports = {
  plugins: {
    '@stylexjs/postcss-plugin': {
      include: [
        './**/*.{js,jsx,ts,tsx}',
        // any other files that should be included
        // this should include NPM dependencies that use StyleX
      ],
      useCSSLayers: true,
    },
    autoprefixer: {},
  },
};
```

Finally, ensure that your app's entry file imports a global CSS file that
includes the following declaration:

```css
@stylex;
```

The PostCSS plugin will replace the declaration with the generated StyleX
styles. Make sure that you only include this declaration once in your app.


# Next.js (/docs/learn/installation/nextjs)

[`examples/example-nextjs`](https://github.com/facebook/stylex/tree/main/examples/example-nextjs)
configures StyleX for the Next.js App Router using the Babel and PostCSS
plugins. Babel compiles StyleX in JS/TS, and the PostCSS plugin replaces the
`@stylex` directive with the generated CSS.

## Install

<DevInstallExample dev={[`@stylexjs/babel-plugin`, `@stylexjs/postcss-plugin`]} />

## Babel Configuration

Create a `babel.config.js` file in your project root and add the StyleX Babel
plugin to it.

```js title="babel.config.js"
const path = require('path');
const dev = process.env.NODE_ENV !== 'production';

module.exports = {
  presets: ['next/babel'],
  plugins: [
    [
      '@stylexjs/babel-plugin',
      {
        dev,
        runtimeInjection: false,
        enableInlinedConditionalMerge: true,
        treeshakeCompensation: true,
        aliases: { '@/*': [path.join(__dirname, '*')] },
        unstable_moduleResolution: { type: 'commonJS' },
        // ... other StyleX configuration
      },
    ],
  ],
};
```

Ensure `next/babel` runs alongside the StyleX plugin so both app and component
code are transformed.

## CSS entrypoint

Import a CSS file in your root layout component file, so that your entire
application can have a single atomic CSS file.

Include the `@stylex` directive within this CSS file.

```css
/* app/globals.css */
@layer resets {
  * {
    box-sizing: border-box;
    padding: 0;
    margin: 0;
  }
}

@stylex;
```

## PostCSS Configuration

Next, create a `postcss.config.js` that imports the Babel configuration to
ensure that both the Babel and PostCSS plugins use the same configuration for
StyleX.

Configure the `include` option with glob patterns to look for all source files
that may contain StyleX styles.

```js title="postcss.config.js"
const babelConfig = require('./babel.config');

module.exports = {
  plugins: {
    '@stylexjs/postcss-plugin': {
      include: [
        // when using a src folder:
        'src/**/*.{js,jsx,ts,tsx}',
        // app router:
        'app/**/*.{js,jsx,ts,tsx}',
        // pages router:
        'pages/**/*.{js,jsx,ts,tsx}',
        // other top-level folders:
        'components/**/*.{js,jsx,ts,tsx}',
      ],
      babelConfig: {
        babelrc: false,
        parserOpts: { plugins: ['typescript', 'jsx'] },
        plugins: babelConfig.plugins,
      },
      useCSSLayers: true,
    },
    autoprefixer: {},
  },
};
```

You can skip Babel transforms for anything other than StyleX in your PostCSS
configuration to speed up CSS generation.

## Using the configurations

Once you define these configuration files, Next.js will automatically use Babel
and PostCSS without any changes to your `next.config.js` file. Since Next.js
16.0.3, this works with both Webpack and Turbopack.


# PostCSS (/docs/learn/installation/postcss)

With certain build pipelines, the StyleX unplugin package may not be feasible.
In such scenarios, the StyleX PostCSS plugin offers an easier and more
compatible alternative.

The PostCSS plugin lets you decouple the transformation of your JS files with
Babel and the generation of your CSS file.

## Install

Start by installing the StyleX babel and postcss plugins:

<DevInstallExample dev={[`@stylexjs/babel-plugin`, `@stylexjs/postcss-plugin`]} />

## Babel configuration

Create a `babel.config.js` file in your project root and add the StyleX Babel
plugin to it.

```js title="babel.config.js"
const path = require('path');
const dev = process.env.NODE_ENV !== 'production';

module.exports = {
  // ... other babel configuration
  plugins: [
    [
      '@stylexjs/babel-plugin',
      {
        dev,
        unstable_moduleResolution: { type: 'commonJS' },
        // ... other StyleX configuration
      },
    ],
  ],
};
```

Ensure that your JS source files are being transpiled by Babel using this
configuration.

## CSS entrypoint

Next, ensure that your application contains a single global CSS file that
includes the `@stylex` directive:

```css
@layer base {
  * {
    box-sizing: border-box;
    padding: 0;
    margin: 0;
  }
  /* other base styles */
}

@stylex;
```

If your build pipeline supports CSS imports, we recommend importing this in your
root layout component, so that it is included for all routes of your app.

## PostCSS configuration

Next, create a `postcss.config.js` that imports the Babel configuration to
ensure that both the Babel and PostCSS plugins use the same configuration.
Ensure that your build pipeline postprocesses your CSS with PostCSS using this
config file.

Other than the `babelConfig` option, define one or more glob patterns for the
`include` option to define all the files that may contain StyleX styles.

```js title="postcss.config.mjs"
import stylex from '@stylexjs/postcss-plugin';
import autoprefixer from 'autoprefixer';
import babelConfig from './babel.config.js';

export default {
  plugins: [
    stylex({
      include: ['src/**/*.{ts,tsx}'],
      useCSSLayers: true,
      babelConfig,
    }),
    // ... other plugins
    autoprefixer,
  ],
};
```

The PostCSS plugin will find all files that match the `include` glob patterns
and transform them with the Babel plugin, collect the styles from them all, and
replace the `@stylex` directive with the generated CSS. The PostCSS plugin uses
per-file caching to speed up subsequent builds.

## Examples

The
[storybook example](https://github.com/facebook/stylex/tree/main/examples/example-storybook)
in the StyleX repository shows one such usage of the PostCSS plugin.

The
[next.js example](https://github.com/facebook/stylex/tree/main/examples/example-nextjs)
uses the same setup to integrate StyleX with Turbopack, which doesn't yet have a
plugin API.


# Rspack (/docs/learn/installation/rspack)

[`examples/example-rspack`](https://github.com/facebook/stylex/tree/main/examples/example-rspack)
integrates StyleX into Rspack via `@stylexjs/unplugin`. The plugin compiles
StyleX modules and appends the aggregated CSS to the stylesheet emitted by
`CssExtractRspackPlugin`.

## Install

<DevInstallExample dev={[`@stylexjs/unplugin`]} />

## Rspack configuration

```js title="rspack.config.js"
const path = require('path');
const rspack = require('@rspack/core');
const stylex = require('@stylexjs/unplugin').default;

module.exports = {
  entry: { app: path.resolve(__dirname, 'src/main.jsx') },
  plugins: [
    stylex.rspack({
      useCSSLayers: true,
      // ... StyleX configuration
    }),
    new rspack.CssExtractRspackPlugin({ filename: 'index.css' }),
  ],
  module: {
    rules: [
      { test: /\.[jt]sx?$/, loader: 'builtin:swc-loader' },
      {
        test: /\.css$/,
        use: [rspack.CssExtractRspackPlugin.loader, 'css-loader'],
      },
    ],
  },
};
```

## CSS entrypoint

Ensure that there is one CSS file that is imported from your root layout
component or JS entry point.


# Vite (/docs/learn/installation/vite)

`@stylexjs/unplugin` integrates directly with Vite to compile StyleX code,
aggregate the generated CSS, and append it to the CSS assets Vite emits. How you
load the CSS/runtime in development depends on whether your entry point is an
HTML file or a React (JS/TS) module.

## Installation

Start by installing the StyleX unplugin package:

<DevInstallExample dev={[`@stylexjs/unplugin`]} />

## Configuration

Add the plugin to your Vite configuration and provider the StyleX configuration
options.

```ts title="vite.config.ts"
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import stylex from '@stylexjs/unplugin';

export default defineConfig({
  plugins: [
    stylex.vite({
      // StyleX configuration options
      useCSSLayers: true,
      dev: process.env.NODE_ENV === 'development',
      runtimeInjection: false,
      // ...
      lightningcssOptions: {
        // Options for lightningcss which postprocesses the generated CSS
      },
    }),
    react(),
  ],
});
```

## CSS entrypoint

In almost all cases, it is useful to have at least one CSS file that is imported
by a component that is part of every route, such as the root layout component.
The StyleX unplugin package's vite plugin will inject the generated CSS in the
existing CSS asset.

This CSS file is also a good place for any CSS resets or global styles that you
may want.

## Dev-server and Hot Reloading

If your Vite setup uses an HTML file as the entry point, you should not need any
further build setup. However, if your entry point is a React component, you may
need to load some virtual modules to enable hot reloading.

We recommend encapsulating this in a special client component file like this:

```tsx
// src/app/DevStyleXInject.tsx
'use client';

import { useEffect } from 'react';

function DevStyleXInjectImpl() {
  useEffect(() => {
    if (import.meta.env.DEV) {
      // @ts-ignore
      import('virtual:stylex:css-only');
    }
  }, []);
  return <link rel="stylesheet" href="/virtual:stylex.css" />;
}

export function DevStyleXInject({ cssHref }: { cssHref: string }) {
  return import.meta.env.DEV ? (
    <DevStyleXInjectImpl />
  ) : (
    <link rel="stylesheet" href={cssHref} />
  );
}
```

The dynamic `import` is wrapped in an additional check for `import.meta.env.DEV`
to ensure that it is not bundled in production.

And then, this component can be used in the `<head>` section of your document
layout component:

```tsx
// src/app/Document.tsx (excerpt)
import { DevStyleXInject } from './DevStyleXInject';

export function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html>
      <head>
        {/* ... */}
        <DevStyleXInject cssHref="/stylex.css" />
        {/* ... */}
      </head>

      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
);
```

The `virtual:stylex.css` file will load the generated CSS, and the
`virtual:stylex:runtime` file will refetch it on every HTML event to enable hot
reloading.

## Framework-specific guides

Documentation for specific Vite-based setups and frameworks is provided in the
following pages, along with smaller framework-specific details for each.


# React Router (RSC) (/docs/learn/installation/vite/react-router)

[`examples/example-react-router`](https://github.com/facebook/stylex/tree/main/examples/example-react-router)
uses Vite’s experimental React Server Components plugin with StyleX compiled by
`@stylexjs/unplugin`. The StyleX plugin runs before the RSC plugin so both
client and server bundles share the same aggregated CSS.

## Vite configuration

```ts title="vite.config.ts"
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import rsc from '@react-router/dev/vite';
import stylex from '@stylexjs/unplugin';

export default defineConfig({
  plugins: [stylex.vite({ useCSSLayers: true }), react(), rsc()],
});
```

* Keep `stylex.vite()` first to preserve Fast Refresh.

## CSS entrypoint

Ensure that there is one CSS file that is imported from your root layout
component or JS entry point.

## CSS Link and Hot Reloading during development

Ensure that the virtual CSS file and script for hot reloading styles are part of
your bundle to enable hot reloading during development.

The easiest way to do this is by using an encapsulated helper that can also be
used to insert a link tag for your production CSS.

```tsx
// src/DevStyleXInject.tsx
'use client';
import { useEffect } from 'react';

function DevStyleXInjectImpl() {
  useEffect(() => {
    if (import.meta.env.DEV) {
      import('virtual:stylex:runtime');
    }
  }, []);
  return <link rel="stylesheet" href="/virtual:stylex.css" />;
}

export function DevStyleXInject({ cssHref }: { cssHref: string }) {
  return import.meta.env.DEV ? (
    <DevStyleXInjectImpl />
  ) : (
    cssHref && <link rel="stylesheet" href={cssHref} />
  );
}
```

Render `<DevStyleXInject />` in your HTML shell component.

```tsx
// src/routes/root/client.tsx (excerpt)
import { DevStyleXInject } from './DevStyleXInject';

export function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <DevStyleXInject />
      </head>
      <body>{children}</body>
    </html>
  );
}
```


# RedwoodSDK (/docs/learn/installation/vite/redwoodsdk)

[`examples/example-redwoodsdk`](https://github.com/facebook/stylex/tree/main/examples/example-redwoodsdk)
shows how RedwoodSDK’s Vite-based toolchain works with `@stylexjs/unplugin`.
StyleX is compiled during both dev and build, and the aggregated CSS is appended
to the worker/client assets that Redwood emits.

## Vite configuration

```ts title="vite.config.mts"
import { defineConfig } from 'vite';
import { redwood } from 'rwsdk/vite';
import { cloudflare } from '@cloudflare/vite-plugin';
import stylex from '@stylexjs/unplugin';

export default defineConfig({
  plugins: [
    cloudflare({ viteEnvironment: { name: 'worker' } }),
    redwood(),
    stylex.vite({
      devMode: 'css-only',
      devPersistToDisk: true,
      dev: true,
      runtimeInjection: false,
    }),
  ],
});
```

* `devMode: 'css-only'` exposes the `/virtual:stylex.css` endpoint without the
  JS runtime (Redwood owns HTML injection).
* `devPersistToDisk` shares collected rules across multiple Vite environments
  (worker + client).

## CSS entrypoint

Ensure that there is one CSS file that is imported from your root layout
component or JS entry point.

## CSS Link and Hot Reloading during development

Ensure that the virtual CSS file and script for hot reloading styles are part of
your bundle to enable hot reloading during development.

The easiest way to do this is by using an encapsulated helper that can also be
used to insert a link tag for your production CSS.

```tsx
// src/app/DevStyleXInject.tsx
'use client';
import { useEffect } from 'react';

function DevStyleXInjectImpl() {
  useEffect(() => {
    if (import.meta.env.DEV) {
      import('virtual:stylex:runtime');
    }
  }, []);
  return <link rel="stylesheet" href="/virtual:stylex.css" />;
}

export function DevStyleXInject({ cssHref }: { cssHref: string }) {
  return import.meta.env.DEV ? (
    <DevStyleXInjectImpl />
  ) : (
    cssHref && <link rel="stylesheet" href={cssHref} />
  );
}
```

Render `<DevStyleXInject cssHref="/stylex.css" />` in your HTML shell component.

```tsx
// src/app/Document.tsx (excerpt)
import { DevStyleXInject } from './DevStyleXInject';

export const Document = ({ children }: { children: React.ReactNode }) => (
  <html lang="en">
    <head>
      <DevStyleXInject cssHref="/client/assets/stylex.css" />
    </head>
    <body>
      <div id="root">{children}</div>
    </body>
  </html>
);
```


# Vite + React (/docs/learn/installation/vite/vite-react)

Both
[`examples/example-vite`](https://github.com/facebook/stylex/tree/main/examples/example-vite)
(JavaScript) and
[`examples/example-vite-react`](https://github.com/facebook/stylex/tree/main/examples/example-vite-react)
(TypeScript) demonstrate wiring StyleX into a Vite + React app via
`@stylexjs/unplugin`. StyleX styles are compiled at build time and appended to
the CSS emitted by Vite.

## Vite configuration

```ts title="vite.config.ts"
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import stylex from '@stylexjs/unplugin';

export default defineConfig({
  plugins: [
    stylex.vite({
      useCSSLayers: true,
      // ... other StyleX configuration options
    }),
    react(),
  ],
});
```

Keep the StyleX plugin before `@vitejs/plugin-react` to preserve Fast Refresh.

## CSS entrypoint

Import a CSS file from the app root (for example `src/index.css`) so Vite emits
an asset. During `vite build` the StyleX plugin appends its aggregated output to
that CSS file, avoiding extra requests in production.

ESLint in the TypeScript example already includes the StyleX lint rules and
`tsconfigRootDir` configuration.


# Vite + React Server Components (/docs/learn/installation/vite/vite-rsc)

[`examples/example-vite-rsc`](https://github.com/facebook/stylex/tree/main/examples/example-vite-rsc)
layers `@vitejs/plugin-rsc` on top of React while `@stylexjs/unplugin` compiles
StyleX for each environment (RSC, SSR, client). Every build output receives a
single CSS asset with aggregated StyleX styles.

## Vite configuration

```ts title="vite.config.ts"
import rsc from '@vitejs/plugin-rsc';
import react from '@vitejs/plugin-react';
import { defineConfig } from 'vite';
import stylex from '@stylexjs/unplugin';

export default defineConfig({
  plugins: [
    rsc(),
    react(),
    stylex.vite({
      // ... StyleX configuration options
    }),
  ],
  environments: {
    rsc: {
      build: {
        rollupOptions: { input: { index: './src/framework/entry.rsc.tsx' } },
      },
    },
    ssr: {
      build: {
        rollupOptions: { input: { index: './src/framework/entry.ssr.tsx' } },
      },
    },
    client: {
      build: {
        rollupOptions: {
          input: { index: './src/framework/entry.browser.tsx' },
        },
      },
    },
  },
});
```

* `stylex.vite()` runs for every environment, so each bundle gets the correct
  CSS appended.
* Add options such as `useCSSLayers` if desired.

## CSS entrypoint

Ensure that there is one CSS file that is imported from your root layout
component or JS entry point.

## CSS Link and Hot Reloading during development

Ensure that the virtual CSS file and script for hot reloading styles are part of
your bundle to enable hot reloading during development.

The easiest way to do this is by using an encapsulated helper that can also be
used to insert a link tag for your production CSS.

```tsx
// src/DevStyleXInject.tsx
'use client';
import { useEffect } from 'react';

function DevStyleXInjectImpl() {
  useEffect(() => {
    if (import.meta.env.DEV) {
      import('virtual:stylex:runtime');
    }
  }, []);
  return <link rel="stylesheet" href="/virtual:stylex.css" />;
}

export function DevStyleXInject({ cssHref }: { cssHref: string }) {
  return import.meta.env.DEV ? (
    <DevStyleXInjectImpl />
  ) : (
    cssHref && <link rel="stylesheet" href={cssHref} />
  );
}
```

Render `<DevStyleXInject cssHref="/stylex.css" />` in your HTML shell component.

```tsx
// src/root.tsx (excerpt)
import { DevStyleXInject } from './DevStyleXInject';

export function Root(props: { url: URL }) {
  return (
    <html lang="en">
      <head>
        <DevStyleXInject cssHref="/stylex.css" />
      </head>
      <body>
        <App {...props} />
      </body>
    </html>
  );
}
```


# Waku (/docs/learn/installation/vite/waku)

[`examples/example-waku`](https://github.com/facebook/stylex/tree/main/examples/example-waku)
integrates StyleX into a Waku app through the Vite layer using
`@stylexjs/unplugin`. The plugin compiles StyleX modules, aggregates the
generated CSS, and appends it to the emitted CSS assets so the browser only
downloads one stylesheet.

## Waku/Vite configuration

```ts title="waku.config.ts"
import react from '@vitejs/plugin-react';
import stylex from '@stylexjs/unplugin';
import { defineConfig } from 'waku/config';

export default defineConfig({
  vite: {
    plugins: [
      stylex.vite({
        useCSSLayers: true,
        devMode: 'css-only',
        devPersistToDisk: true,
        runtimeInjection: false,
      }),
      react({ babel: { plugins: ['babel-plugin-react-compiler'] } }),
    ],
  },
});
```

* `devMode: 'css-only'` serves `/virtual:stylex.css` in dev without injecting
  the JS runtime.
* `devPersistToDisk` lets multiple Waku environments share collected rules while
  developing.

## CSS entrypoint

Ensure that there is one CSS file that is imported from your root layout
component or JS entry point.

## CSS Link and Hot Reloading during development

Ensure that the virtual CSS file and script for hot reloading styles are part of
your bundle to enable hot reloading during development.

The easiest way to do this is by using an encapsulated helper that can also be
used to insert a link tag for your production CSS.

```tsx
// src/DevStyleXInject.tsx
'use client';
import { useEffect } from 'react';

function DevStyleXInjectImpl() {
  useEffect(() => {
    if (import.meta.env.DEV) {
      import('virtual:stylex:runtime');
    }
  }, []);
  return <link rel="stylesheet" href="/virtual:stylex.css" />;
}

export function DevStyleXInject({ cssHref }: { cssHref: string }) {
  return import.meta.env.DEV ? (
    <DevStyleXInjectImpl />
  ) : (
    cssHref && <link rel="stylesheet" href={cssHref} />
  );
}
```

Render `<DevStyleXInject cssHref="/stylex.css" />` in your HTML shell component.

```tsx
// src/pages/_layout.tsx (excerpt)
import { DevStyleXInject } from '../components/DevStyleXInject';

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <>
    <head>
      <DevStyleXInject cssHref="/stylex.css" />
    </head>
    <body>
    <div>
      {children}
    </div>
    </>
  );
}
```


# Webpack (/docs/learn/installation/webpack)

[`examples/example-webpack`](https://github.com/facebook/stylex/tree/main/examples/example-webpack)
demonstrates using `@stylexjs/unplugin` with Webpack and `MiniCssExtractPlugin`.
StyleX is compiled at build time and the aggregated CSS is appended to the
extracted stylesheet.

## Install

<DevInstallExample dev={[`@stylexjs/unplugin`]} />

## Webpack configuration

```js title="webpack.config.js"
const fs = require('node:fs');
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const stylex = require('@stylexjs/unplugin').default;
const templatePath = path.resolve(__dirname, 'index.html');

module.exports = {
  // ...
  devServer: {
    watchFiles: [templatePath, path.resolve(__dirname, 'src/**/*')],
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: [{ loader: 'babel-loader' }],
      },
      { test: /\.css$/, use: [MiniCssExtractPlugin.loader, 'css-loader'] },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      inject: true,
      templateContent: () => fs.readFileSync(templatePath, 'utf-8'),
    }),
    stylex.webpack({
      useCSSLayers: true,
      // ... other StyleX configuration
    }),
    new MiniCssExtractPlugin(),
  ],
};
```

## CSS entrypoint

Ensure that there is one CSS file that is imported from your root layout
component or JS entry point.


# Context-driven styles (/docs/learn/recipes/context-driven-styles)

StyleX lets you apply styles conditionally. Any condition can be used to do so,
`Props`, `State` or `Context`.

The React Context API (and other similar APIs) can be used to avoid
prop-drilling and provide conditions that child components can read and apply
styles conditionally.

Context can help reduce prop-drilling by sharing state across components. This
can often be an alternative to using descendent selectors, as the same results
can be achieved *without* "styling at a distance".

For example, you can manage the open or closed state of a sidebar using React
Context and conditionally apply styles:

## Defining context and styles

This file sets up the `SidebarContext` and defines the styles for the sidebar in
one place. The context provides a way to share the open/closed state, and the
styles determine the appearance of the sidebar based on that state.

```tsx
import { createContext } from 'react';

export default createContext(false);
```

## Building the sidebar component

The `Sidebar` component uses the `SidebarContext` to determine its open or
closed state and conditionally applies the appropriate styles.

```tsx
import { useContext } from 'react';
import * as stylex from '@stylexjs/stylex';
import { SidebarContext } from './SidebarContext';

export default function Sidebar({ children }) {
  const isOpen = useContext(SidebarContext);

  return (
    <div {...stylex.props(styles.base, isOpen ? styles.open : styles.closed)}>
      {children}
    </div>
  );
}

const styles = stylex.create({
  base: {...},
  open: {
    width: 250,
  },
  closed: {
    width: 50,
  },
});
```

## Using the sidebar in a parent component

The `App` component manages the sidebar's open/closed state and provides it to
child components through `SidebarContext.Provider`. A button toggles the sidebar
state dynamically.

```tsx
import { useState } from 'react';
import SidebarContext from './SidebarContext';
import Sidebar from './Sidebar';

export default function App() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  return (
    <SidebarContext.Provider value={isSidebarOpen}>
      <button onClick={() => setIsSidebarOpen((open) => !open)}>
        Toggle Sidebar
      </button>
      <Sidebar>
        <p>Sidebar Content</p>
      </Sidebar>
    </SidebarContext.Provider>
  );
}
```


# Variables for descendant styles (/docs/learn/recipes/descendant-styles)

It is not uncommon to define styles on an element that are dependent on a parent
element's state, such as applying some styles conditionally when the parent
element is hovered.

StyleX doesn't allow arbitrary selectors or "styling at a distance". However,
variables can be used to achieve the same results in a safe and composable way.

## Example: Sidebar

Consider the case where the content within a sidebar needs to have contextual
styles applied when the sidebar as whole is hovered.

Using CSS variables, you can style descendants based on a parent's state, such
as `:hover`.

### Step 1

Define one or more variables using `defineVars`:

```tsx title="variables.stylex.ts"
import * as stylex from '@stylexjs/stylex';

export const vars = stylex.defineVars({
  childColor: 'black',
});
```

### Step 2

Define contextual styles setting the value for the variable in the ancestor
component.

```tsx title="Component.tsx"
import * as stylex from '@stylexjs/stylex';
import { vars } from './variables.stylex';

const styles = stylex.create({
  parent: {
    [vars.childColor]: {
      default: 'black',
      ':hover': 'blue',
    },
  },
});

function ParentWithHover({ children }) {
  return <div {...stylex.props(styles.parent)}>{children}</div>;
}
```

### Step 3

Use the variable to style the child component

```tsx title="Child.tsx"
import * as stylex from '@stylexjs/stylex';
import { vars } from './variables.stylex';

const styles = stylex.create({
  child: {
    color: vars.childColor,
  },
});

function Child() {
  return (
    <span {...stylex.props(styles.child)}>
      <Icon />A Row
    </span>
  );
}
```

This pattern makes it explicit what styles are being defined on an ancestor
element, while leaving the child element in control to use those styles
explicitly and to override it as needed.


# Light and Dark Themes (/docs/learn/recipes/light-dark-themes)

It is a common pattern to define separate `light`, `dark` and system themes to
provide the ability to switch between different color schemes.

This would typically be done by defining three separate `Theme`s:

```tsx
const lightVars = {
  primaryColor: 'black',
  ...
};
export const light = stylex.createTheme(vars, lightVars);

const darkVars = {
  primaryColor: 'white',
  ...
};
export const dark = stylex.createTheme(vars, darkVars);

const systemVars = {
  primaryColor: {
    default: 'black',
    '@media (prefers-color-scheme: dark)': 'white',
  },
  ...
};
export const system = stylex.createTheme(vars, systemVars);
```

This pattern is well supported and will work in all browsers that support CSS
variables.

## Using the `light-dark()` CSS function

In modern browsers, we suggest using the
[`light-dark()`](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/light-dark)
CSS function instead which will simplify the code and remove the need to define
themes.

```tsx
export const vars = stylex.defineVars({
  primaryColor: 'light-dark(black, white)',
  ...
});
```

You can now control the color scheme applied by using the `color-scheme` CSS
property.

```tsx
const styles = stylex.create({
  light: {
    colorScheme: 'light',
  },
  dark: {
    colorScheme: 'dark',
  },
  system: {
    colorScheme: 'light dark',
  },
});

<div {...stylex.props(styles[colorScheme])}>...</div>;
```

You *can* still define custom themes for other use-cases and use `light-dark()`
within them.

### Limitations

1. The `light-dark()` CSS function can only be used for color values.
2. The `light-dark()` function is not supported in older browsers.


# Merge Themes (/docs/learn/recipes/merge-themes)

`Theme`s for the *same* `VarGroup` are mutually exclusive and do not merge. Any
variable in a `VarGroup` that is not explicitly overridden in a `Theme` for that
`VarGroup` is set to its default value.

However, you can reuse common constants when defining multiple themes for a
particular `VarGroup` and avoid excessive repetition.

## Example

```tsx
import * as stylex from '@stylexjs/stylex';
import { vars } from './variables.stylex';

const themeBlueVars = {
  backgroundColor: 'blue',
};
const themeBlue = stylex.createTheme(vars, themeBlueVars);

const themeBigVars = {
  size: '128px',
};
const themeBig = stylex.createTheme(vars, themeBigVars);

const themeBigBlueVars = { ...themeBlueVars, ...themeBigVars };
const themeBigBlue = stylex.createTheme(vars, themeBigBlueVars);
```

The StyleX compiler is able to resolve local object constants and merge them.
This is useful to be able to define a `Theme` that merges the values of two or
more other `Theme`s without repetition.


# Reset Theme (/docs/learn/recipes/reset-themes)

The `defineVars` function is used to create a set of CSS variables, called
`VarGroup`s. Further, the `createTheme` function can be used to create `Theme`s,
that override the values of the variables defined within `VarGroup`s.

Many `VarGroup`s can be defined which can then be independently overridden with
`Theme`s. However, `Theme`s for the *same* `VarGroup` are mutually exclusive and
do not merge. Any variable in a `VarGroup` that is not explicitly overridden in
a `Theme` for that `VarGroup` is set to its default value.

This characteristic of `Theme`s can be used to define a "empty" theme that
resets all variables to their default values.

## Example

```tsx
import * as stylex from '@stylexjs/stylex';
import { vars } from './variables.stylex';

export const resetVars = stylex.createTheme(vars, {});
```


# Theme overrides (/docs/learn/recipes/shareable-tokens)

StyleX provides several patterns for sharing design tokens across your codebase
and creating themes that build on each other.

## Shareable tokens with `stylex.env`

Use `stylex.env` to define design tokens once in your babel config and
use them across your entire codebase. This avoids repeating token values in
every file.

```js title="babel.config.js"
module.exports = {
  plugins: [
    ['@stylexjs/babel-plugin', {
      env: {
        tokens: {
          colors: {
            primary: 'blue',
            secondary: 'green',
            background: 'white',
            text: 'black',
            border: 'gray',
          },
          spacing: {
            small: '4px',
            medium: '8px',
            large: '16px',
          },
          radii: {
            small: '4px',
            medium: '8px',
          },
        },
      },
    }],
  ],
};
```

These tokens can then be used in `defineVars`, `createTheme`, or `create` calls:

```tsx title="tokens.stylex.js"
import * as stylex from '@stylexjs/stylex';

export const colors = stylex.defineVars(stylex.env.tokens.colors);
export const spacing = stylex.defineVars(stylex.env.tokens.spacing);
export const radii = stylex.defineVars(stylex.env.tokens.radii);
```

## Partial overrides

`createTheme` accepts partial overrides. Tokens you don't specify are not
included in the generated CSS, so they inherit from the original `VarGroup`.

```tsx title="themes.js"
import * as stylex from '@stylexjs/stylex';
import { colors } from './tokens.stylex';

// Dark theme — only override what changes
export const darkTheme = stylex.createTheme(colors, {
  background: '#1a1a1a',
  text: 'white',
});

// High contrast — only override what changes
export const highContrastTheme = stylex.createTheme(colors, {
  primary: 'yellow',
  border: 'white',
});
```

Apply themes by nesting. Child themes inherit unspecified tokens from their
parent:

```tsx title="App.js"
import * as stylex from '@stylexjs/stylex';
import { darkTheme, highContrastTheme } from './themes';

// High contrast inherits background and text from dark
<div {...stylex.props(darkTheme)}>
  <div {...stylex.props(highContrastTheme)}>
    {children}
  </div>
</div>
```

## Composing theme overrides with `stylex.env` functions

For themes that share a common base, define a shareable `env` function to merge overrides. This avoids repeating the full token set in every theme.

```js title="babel.config.js"
module.exports = {
  plugins: [
    ['@stylexjs/babel-plugin', {
      env: {
        tokens: {
          colors: {
            primary: 'blue',
            secondary: 'green',
            background: 'white',
            text: 'black',
            border: 'gray',
          },
        },
        override: (base, overrides) => ({ ...base, ...overrides }),
      },
    }],
  ],
};
```

```tsx title="themes.js"
import * as stylex from '@stylexjs/stylex';
import { colors } from './tokens.stylex';

// Each theme specifies only its changes
export const darkTheme = stylex.createTheme(colors,
  stylex.env.override(stylex.env.tokens.colors, {
    background: '#1a1a1a',
    text: 'white',
  })
);

export const draculaTheme = stylex.createTheme(colors,
  stylex.env.override(stylex.env.tokens.colors, {
    primary: 'purple',
    secondary: 'pink',
    background: '#282a36',
    text: '#f8f8f2',
  })
);
```

The `override` function merges the base tokens with your changes through the function set in your config.


# Variants (/docs/learn/recipes/variants)

The "variants" pattern allows you to conditionally apply one of several
predefined styles based on a value. This is especially useful for theming or
dynamic component behavior.

It is common to have different styles for different "variants" of a component.
Some other styling solutions provide an explicit API for defining variants. In
StyleX, you can define variants with a simple pattern instead.

## Example: Button Variants

Here’s how you can create a button component with different visual styles based
on `variant` props:

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  base: {
    appearance: 'none',
    borderWidth: 0,
  },
});
const colorVariants = stylex.create({
  primary: {
    backgroundColor: {
      default: 'blue',
      ':hover': 'darkblue',
    },
    color: 'white',
  },
  secondary: {
    backgroundColor: {
      default: 'gray',
      ':hover': 'darkgray',
    },
    color: 'white',
  },
});
const sizeVariants = stylex.create({
  small: {
    fontSize: '1rem',
    paddingBlock: 4,
    paddingInline: 8
  },
  medium: {
    fontSize: '1.2rem',
    paddingBlock: 8,
    paddingInline: 16
  },
});

type Props = {
  color: keyof typeof colorVariants,
  size: keyof typeof sizeVariants,
  ...
};

function Button({
  color = 'primary',
  size = 'small',
  ...props
}: Props) {
  return (
    <button
      {...props}
      {...stylex.props(
        styles.base,
        colorVariants[color],
        sizeVariants[size],
        props.style
      )}
    />
  );
}

// Usage
<Button color="primary" size="medium">Primary</Button>
<Button color="secondary">Secondary</Button>
```

## Compound Variants

Sometimes variants are dependent on a combination of variants props.

In most cases, it's simpler to leverage StyleX’s deterministic style merging to
simplify this behaviour.

### Example: A `disabled` prop

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  base: {...},
  disabled: {
    backgroundColor: 'grey',
    color: 'rgb(204, 204, 204)',
    cursor: 'not-allowed',
  },
});
const colorVariants = stylex.create({
  primary: {
    backgroundColor: {
      default: 'blue',
      ':hover': 'darkblue',
    },
    color: 'white',
  },
  secondary: {
    backgroundColor: {
      default: 'gray',
      ':hover': 'darkgray',
    },
    color: 'white',
  },
});
const sizeVariants = stylex.create({...});

type Props = {
  color?: keyof typeof colorVariants,
  size?: keyof typeof sizeVariants,
  disabled?: boolean,
  ...
};

function Button({
  color = 'primary',
  size = 'small',
  disabled = false,
  ...props,
}: Props) {
  return (
    <button
      {...props}
      {...stylex.props(
        styles.base,
        colorVariants[color],
        sizeVariants[size],
        disabled && styles.disabled,
        props.style
      )}
    />
  );
}

// Usage
<Button color="primary" size="medium">Primary</Button>
<Button color="secondary">Secondary</Button>
```

There may be other scenarios where you need to be more explicit about the styles
that should be applied under various condition. You can do this by declaring
multiple style definitions for a particular variant.

### Example: Two definitions for `color` variant styles

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  base: {...},
});
const colorVariantsEnabled = stylex.create({
  primary: {
    backgroundColor: {
      default: 'blue',
      ':hover': 'darkblue',
    },
    color: 'white',
  },
  secondary: {
    backgroundColor: {
      default: 'gray',
      ':hover': 'darkgray',
    },
    color: 'white',
  },
});
const colorVariantsDisabled = stylex.create({
  primary: {
    backgroundColor: 'blue',
    color: 'white',
  },
  secondary: {
    backgroundColor: 'gray',
    color: 'white',
  },
});
const sizeVariants = stylex.create({...});

type Props = {
  color?: keyof (typeof colorVariantsEnabled | typeof colorVariantsDisabled),
  size?: keyof typeof sizeVariants,
  disabled?: boolean,
  ...
};

function Button({
  color = 'primary',
  size = 'small',
  disabled = false,
  ...props,
}: Props) {
  const colorVariants = disabled
    ? colorVariantsDisabled
    : colorVariantsEnabled;

  return (
    <button
      {...props}
      {...stylex.props(
        styles.base,
        colorVariants[color],
        sizeVariants[size],
        props.style
      )}
    />
  );
}

// Usage
<Button color="primary" size="medium">Primary</Button>
<Button color="secondary">Secondary</Button>
```


# Static types (/docs/learn/static-types)

## Types for style props

StyleX comes with full support for Static Types. The most common utility type is
`StyleXStyles` which is used to accept any arbitrary StyleX styles.

<Tabs defaultValue={0}>
  <TabItem label="TypeScript" default>
    ```tsx
    import type { StyleXStyles } from '@stylexjs/stylex';
    import * as stylex from '@stylexjs/stylex';

    type Props = {
      ...
      style?: StyleXStyles,
    };

    function MyComponent({style, ...otherProps}: Props) {
      return (
        <div
          {...stylex.props(localStyles.foo, localStyles.bar, style)}
        >
          {/* ... */}
        </div>
      );
    }
    ```
  </TabItem>

  <TabItem label="Flow">
    ```tsx
    import type { StyleXStyles } from '@stylexjs/stylex';
    import * as stylex from '@stylexjs/stylex';

    type Props = $ReadOnly<{
      ...
      style?: StyleXStyles<>,
    }>;

    function MyComponent({style, ...otherProps}: Props) {
      return (
        <div
          {...stylex.props(localStyles.foo, localStyles.bar, style)}
        >
          {/* ... */}
        </div>
      );
    }
    ```
  </TabItem>
</Tabs>

<Callout type="tip" title="Disallowing dynamic styles">
  `StaticStyles` can be used instead of `StyleXStyles` to accept arbitrary static
  styles, but disallow dynamic styles.
</Callout>

## Constraining accepted styles

Type arguments can be used with `StyleXStyles<{...}>` to limit the styles that
are accepted.

### Accepting from a set of style properties

To limit the accepted style properties to a given set, an object type with the
allowed properties can be used:

<Tabs defaultValue={0}>
  <TabItem label="TypeScript" default>
    ```tsx
    import type { StyleXStyles } from '@stylexjs/stylex';

    type Props = {
      // ...
      style?: StyleXStyles<{
        color?: string;
        backgroundColor?: string;
        borderColor?: string;
        borderTopColor?: string;
        borderEndColor?: string;
        borderBottomColor?: string;
        borderStartColor?: string;
      }>;
    };
    ```
  </TabItem>

  <TabItem label="Flow">
    ```tsx
    import type { StyleXStyles } from '@stylexjs/stylex';

    type Props = $ReadOnly<{
      // ...
      style?: StyleXStyles<{
        color?: string;
        backgroundColor?: string;
        borderColor?: string;
        borderTopColor?: string;
        borderEndColor?: string;
        borderBottomColor?: string;
        borderStartColor?: string;
      }>;
    }>;
    ```
  </TabItem>
</Tabs>

The `style` prop will now accept only the properties defined but disallow
anything else.

<Callout type="tip" title="Good default styles">
  It is a good practice to make the keys of the style types optional and have
  baseline styles in the component itself.
</Callout>

<Callout type="danger" title="TypeScript may not catch extra style properties">
  TypeScript object types don’t error when given objects with extra properties.
  We’ve taken steps to mitigate this issue, but there may be edge-cases where
  you’ll be able to pass in extra, disallowed styles without a type error.
</Callout>

### Limiting the possible values for styles

In addition to the accepted style properties, the values for those properties
can be constrained too.

<Tabs>
  <TabItem value="typescript" label="TypeScript" default>
    ```tsx
    import type { StyleXStyles } from '@stylexjs/stylex';

    type Props = {
      ...
      // Only accept styles for marginTop and nothing else.
      // The value for marginTop can only be 0, 4, 8 or 16.
      style?: StyleXStyles<{
        marginTop: 0 | 4 | 8 | 16
      }>,
    };
    ```
  </TabItem>

  <TabItem value="flow" label="Flow">
    ```tsx
    import type { StyleXStyles } from '@stylexjs/stylex';

    type Props = $ReadOnly<{
      ...
      // Only accept styles for marginTop and nothing else.
      // The value for marginTop can only be 0, 4, 8 or 16.
      style?: StyleXStyles<{
        marginTop: 0 | 4 | 8 | 16
      }>,
    }>;
    ```
  </TabItem>
</Tabs>

Now, this component only accepts styles that have a `marginTop` property and no
other properties. The value for `marginTop` can only be one of `0`, `4`, `8`, or
`16`.

## Disallowing properties

It is sometimes more convenient to define a blocklist instead of an allowlist.

<Tabs>
  <TabItem value="typescript" label="TypeScript" default>
    ```tsx
    import type { StyleXStylesWithout } from '@stylexjs/stylex';
    import * as stylex from '@stylexjs/stylex';

    type NoLayout = StyleXStylesWithout<{
      position: unknown,
      display: unknown,
      top: unknown,
      start: unknown,
      end: unknown,
      bottom: unknown,
      border: unknown,
      borderWidth: unknown,
      borderBottomWidth: unknown,
      borderEndWidth: unknown,
      borderStartWidth: unknown,
      borderTopWidth: unknown,
      margin: unknown,
      marginBottom: unknown,
      marginEnd: unknown,
      marginStart: unknown,
      marginTop: unknown,
      padding: unknown,
      paddingBottom: unknown,
      paddingEnd: unknown,
      paddingStart: unknown,
      paddingTop: unknown,
      width: unknown,
      height: unknown,
      flexBasis: unknown,
      overflow: unknown,
      overflowX: unknown,
      overflowY: unknown,
    }>;

    type Props = {
      // ...
      style?: NoLayout,
    };

    function MyComponent({style, ...otherProps}: Props) {
      return (
        <div
          {...stylex.props(localStyles.foo, localStyles.bar, style)}
        >
          {/* ... */}
        </div>
      );
    }
    ```
  </TabItem>

  <TabItem value="flow" label="Flow">
    ```tsx
    import type { StyleXStylesWithout } from '@stylexjs/stylex';
    import * as stylex from '@stylexjs/stylex';

    type NoLayout = StyleXStylesWithout<{
      position: mixed,
      display: mixed,
      top: mixed,
      start: mixed,
      end: mixed,
      bottom: mixed,
      border: mixed,
      borderWidth: mixed,
      borderBottomWidth: mixed,
      borderEndWidth: mixed,
      borderStartWidth: mixed,
      borderTopWidth: mixed,
      margin: mixed,
      marginBottom: mixed,
      marginEnd: mixed,
      marginStart: mixed,
      marginTop: mixed,
      padding: mixed,
      paddingBottom: mixed,
      paddingEnd: mixed,
      paddingStart: mixed,
      paddingTop: mixed,
      width: mixed,
      height: mixed,
      flexBasis: mixed,
      overflow: mixed,
      overflowX: mixed,
      overflowY: mixed,
    }>;

    type Props = $ReadOnly<{
      // ...
      style?: NoLayout,
    }>;

    function MyComponent({style, ...otherProps }: Props) {
      return (
        <div
          {...stylex.props(localStyles.foo, localStyles.bar, style)}
        >
          {/* ... */}
        </div>
      );
    }
    ```
  </TabItem>
</Tabs>

Here the listed properties in the object type will be disallowed, but all other
styles will still be accepted.


# Defining styles (/docs/learn/styling-ui/defining-styles)

StyleX uses an expressive JavaScript API that is similar to working with inline
styles in React DOM, or styles in React Native.

## Constraints

Since StyleX depends on ahead-of-time compilation, it is important for all your
styles to be statically analyzable. This means that every "Raw Style Object"
must only contain:

* Plain Object Literals
* String Literals
* Number Literals
* Array Literals
* `null` or `undefined`
* Constants, simple expressions, and built-in methods (e.g., `.toString()`) that
  resolve to one of the above.
* And arrow functions for dynamic styles

The following are **not** allowed:

* Function calls (except StyleX functions)
* Values imported from other modules (except for CSS Variables created using
  StyleX from a `.stylex.js` file.)
* Object spreads (e.g., `{...style}`)

## Creating styles

Styles must be created with the `create` function. You can define one or more
"namespaces", or objects of styles. In the example below, there are 2
"namespaces" - one called `base` and the other `highlighted`. The names are
arbitrary and represent the constant used to capture the result of the
`create()` function call.

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  base: {
    fontSize: 16,
    lineHeight: 1.5,
    color: 'rgb(60,60,60)',
  },
  highlighted: {
    color: 'rebeccapurple',
  },
});
```

## Pseudo-classes

Pseudo-classes represent different states of an element. In StyleX, declarations
for pseudo-classes are nested within properties. For example, let's say we have
a button that currently has a `lightblue` background.

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  button: {
    backgroundColor: 'lightblue',
  },
});
```

If we want to add pseudo-classes to change the background color for different
states, we replace the `lightblue` string literal with an object of
pseudo-states.

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  button: {
    backgroundColor: {
      default: 'lightblue',
      ':hover': 'blue',
      ':active': 'darkblue',
    },
  },
});
```

## Pseudo-elements

<Callout type="info" title="Avoid unnecessary pseudo elements">
  We recommend avoiding pseudo-elements when possible and relying on actual HTML
  elements instead, i.e., replace `::before` and `::after` with elements like
  `div` or `span`. This helps reduce the size of your CSS bundle.
</Callout>

Pseudo-elements are a way of targeting shadow DOM elements contained within the
native HTML elements provided by user agents. For example, `::placeholder`
references the element that contains placeholder text within an `input` or
`textarea` element. To target pseudo-elements in StyleX, they must be defined as
a top-level key within a namespace.

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  input: {
    // pseudo-element
    '::placeholder': {
      color: '#999',
    },
    color: {
      default: '#333',
      // pseudo-class
      ':invalid': 'red',
    },
  },
});
```

## Media queries (and other `@` rules)

Media Queries can, similarly, be as "conditions" within style values.

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  base: {
    width: {
      default: 800,
      '@media (max-width: 800px)': '100%',
      '@media (min-width: 1540px)': 1366,
    },
  },
});
```

## Combining conditions

Your Style Values can be nested more than one level deep when you need to
combine Media Queries and Pseudo Selectors

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  button: {
    color: {
      default: 'var(--blue-link)',
      ':hover': {
        default: null,
        '@media (hover: hover)': 'scale(1.1)',
      },
      ':active': 'scale(0.9)',
    },
  },
});
```

<Callout type="info">
  The `default` case is required when authoring contextual styles. If you don't
  want any style to be applied in the default case, you can use `null` as the
  value.

  Using `null` for a non-`default` condition has no effect and should be
  considered invalid.
</Callout>

## Fallback styles

There are situations in StyleX where, when you need fallback styles for browsers
that don't support a certain new style property.

In CSS you may do something like this:

```css
.header {
  position: fixed;
  position: -webkit-sticky;
  position: sticky;
}
```

This kind of syntax is not possible when using JavaScript objects. So in StyleX
you can use the `firstThatWorks` function to achieve the same thing.

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  header: {
    position: stylex.firstThatWorks('sticky', '-webkit-sticky', 'fixed'),
  },
});
```

## Keyframe animations

You can use the `keyframes` function to define keyframe animations.

```tsx
import * as stylex from '@stylexjs/stylex';

const fadeIn = stylex.keyframes({
  from: { opacity: 0 },
  to: { opacity: 1 },
});

const styles = stylex.create({
  base: {
    animationName: fadeIn,
    animationDuration: '1s',
  },
});
```

## Dynamic styles

<Callout type="warning" title="Use sparingly">
  Dynamic styles are an advanced feature and should be used sparingly. For the
  majority of use-cases,
  [conditional styles](/docs/learn/styling-ui/using-styles#conditional-styles)
  should be sufficient.
</Callout>

StyleX generates all styles at compile-time which means you need to *know* all
those styles ahead of time as well. But sometimes you just don't know what you
will need until runtime.

For such situations, you can define your styles as a function instead of an
object and pass in the dynamic components of the needed styles as parameters.

**NOTE**: The function body *must* be an object literal. You cannot use a
function body with multiple statements.

```tsx
import { useState } from 'react';
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  // Function arguments must be simple identifiers
  // -- No destructuring or default values
  bar: (height) => ({
    height,
    // The function body must be an object literal
    // -- { return {} } is not allowed
  }),
});

function MyComponent() {
  // The value of `height` cannot be known at compile time.
  const [height, setHeight] = useState(10);

  return <div {...stylex.props(styles.bar(height))} />;
}
```

Behind the scenes, StyleX will generate static styles that depend on a CSS
variable and set the value of that variable at runtime. This means, that any
part of your styles can be dynamic, including within Media Queries and
pseudo-classes.


# Using styles (/docs/learn/styling-ui/using-styles)

Once styles have been defined, they must be converted to `className` and
`styles` props that can be spread on HTML elements using the
[`props`](/docs/api/javascript/props) function.

```tsx
<div {...stylex.props(styles.base)} />
```

While this is the simplest case, it is trivial to merge multiple style objects,
use them conditionally, or even compose styles across module boundaries.

## Merging styles

The `props` function can take a list of styles and merge them in a deterministic
way, where the last style applied always wins. The order in which the styles are
defined does not affect the resulting styles, only the order in which they are
applied to the HTML element.

Using `props` is only required when styles are set on React DOM host elements
like `<div>`.

Consider styles that are defined as follows:

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  base: {
    fontSize: 16,
    lineHeight: 1.5,
    color: 'grey',
  },
  highlighted: {
    color: 'rebeccapurple',
  },
});

<div {...stylex.props(styles.base, styles.highlighted)} />;
```

The resulting HTML element will have purple text, because that style was applied
last. If instead the order of the styles were reversed, the text would be gray.

```tsx
<div {...stylex.props(styles.highlighted, styles.base)} />
```

A simple way to think about the `props` function is that it merges many objects and
the later objects have precedence over previous objects.

Each individual style object can be passed to `props` as a separate argument, or
passed in as an array of styles.

```tsx
<div {...stylex.props([styles.base, styles.highlighted])} />
```

## Conditional styles

Styles can be applied conditionally at runtime using common JavaScript patterns
such as ternary expressions and the `&&` operator. `props` ignores falsy values
such as `null`, `undefined`, or `false`.

```tsx
<div
  {...stylex.props(
    styles.base,
    props.isHighlighted && styles.highlighted,
    isActive ? styles.active : styles.inactive,
  )}
/>
```

## Style variants

A common styling pattern called "variants" lets you apply styles based on the
value of a specific prop, e.g., `variant`. StyleX supports this pattern without
an additional API. Instead, an object property lookup can be used to achieve the
same result.

First, each variant can be defined with the appropriate variant name for the
style object.

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  violet: {
    backgroundColor: {
      default: 'blueviolet',
      ':hover': 'darkviolet',
    },
    color: 'white',
  },
  gray: {
    backgroundColor: {
      default: 'gainsboro',
      ':hover': 'lightgray',
    },
  },
  // ... more variants here ...
});
```

The appropriate styles can then be applied by using the `variant` prop as a key
on the `styles` object.

```tsx
function Button({ variant, ...props }) {
  return <button {...props} {...stylex.props(styles[variant])} />;
}
```

## Styles as props

StyleX encourages co-locating styles, but it's also possible to pass and use
styles across file and component boundaries using component props.

### Passing style props to components

When using custom components, styles created with StyleX can be passed down as
props.

```tsx
<CustomComponent style={styles.base} />
```

StyleX will correctly merge nested arrays of styles, which means you can use the
same patterns described above to combine or conditionally apply styles.

```tsx
<CustomComponent style={[styles.base, isHighlighted && styles.highlighted]} />
```

When combining local styles with styles passed in as props, it's idiomatic to
apply the styles passed in as props *after* the local styles. Although, there's
nothing wrong with applying certain local styles last, if you require them to
always take priority over prop styles.

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  base: {
    /*...*/
  },
});

function CustomComponent({ style }) {
  return <div {...stylex.props(styles.base, style)} />;
}
```

In these examples the `style` prop name is arbitrary. You can use any prop name,
just like when passing any other types of data to React components.

## “Unsetting” styles

Sometimes, styles need to be removed rather than applied. While CSS provides
values such as `initial`, `inherit`, `unset`, and `revert`, the simplest
solution to do this in StyleX is to set the value to `null`.

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  base: {
    color: null,
  },
});
```

Setting a style property to `null` removes any previously applied style for it
by StyleX. And it doesn't result in additional generated CSS.


# Creating themes (/docs/learn/theming/creating-themes)

<Callout type="info" title="Note">
  The
  [`unstable_moduleResolution`](/docs/api/configuration/babel-plugin/#unstable_moduleresolution)
  option needs to be enabled in the StyleX Babel configuration to enable theming
  APIs.
</Callout>

Once variables have been defined, alternate “themes” can be created to override
the values of those variables for specific UI sub-trees.

## Creating Themes

Any variable group can be imported to create a theme like so:

```tsx title="themes.js"
import * as stylex from '@stylexjs/stylex';
import { colors, spacing } from './tokens.stylex';

// A constant can be used to avoid repeating the media query
const DARK = '@media (prefers-color-scheme: dark)';

// Dracula theme
export const dracula = stylex.createTheme(colors, {
  primaryText: { default: 'purple', [DARK]: 'lightpurple' },
  secondaryText: { default: 'pink', [DARK]: 'hotpink' },
  accent: 'red',
  background: { default: '#555', [DARK]: 'black' },
  lineColor: 'red',
});
```

## Applying Themes

A “theme” is a style object similar to the ones created with `create()`. They
can be applied to an element using `props()` to override variables for that
element and all its descendants.

```tsx title="components/MyComponent.js"
import * as stylex from '@stylexjs/stylex';
import { colors, spacing } from '../tokens.stylex';
import { dracula } from '../themes';

const styles = stylex.create({
  container: {
    color: colors.primaryText,
    backgroundColor: colors.background,
    padding: spacing.medium,
  },
});

<div {...stylex.props(dracula, styles.container)}>{children}</div>;
```

**NOTE:** Any variables that are not overridden will revert back to their
default value that was set in the `defineVars` declaration.

Unlike when defining and using variables, themes can be created with
`createTheme` anywhere in a codebase, and passed around across files or
components.

<Callout type="info">
  If multiple themes for the same variable group are applied on the same HTML
  element, the last applied theme wins.
</Callout>


# Defining variables (/docs/learn/theming/defining-variables)

<Callout type="info" title="Note">
  The
  [`unstable_moduleResolution`](/docs/api/configuration/babel-plugin/#unstable_moduleresolution)
  option needs to be enabled in the StyleX Babel configuration to enable theming
  APIs.
</Callout>

In addition to authoring styles for your components that generate atomic styles,
StyleX also has APIs for defining CSS Custom Properties (CSS variables) in a
reliable, predictable and type-safe way.

### Design inspiration

The design of the theming APIs in StyleX are directly inspired by React's
Context APIs. Variables are defined with default values similar to how React
Contexts are created, and themes can be created to “provide” different values
for these variables for UI sub-trees.

## Defining variables

A group of variables are defined using the `defineVars` function:

```tsx title="tokens.stylex.js"
import * as stylex from '@stylexjs/stylex';

export const tokens = stylex.defineVars({
  accent: 'blue',
  background: 'white',
  borderRadius: '4px',
  fontFamily: 'system-ui, sans-serif',
  fontSize: '16px',
  lineColor: 'gray',
  primaryText: 'black',
  secondaryText: '#333',
});
```

This function, too, is processed at compile-time and unique CSS variable names
are automatically generated. These values can then be imported and used within
`create` calls.

To create variables with custom stable names that match the exact strings
provided, use a key that starts with `--`. Doing so will mean that StyleX cannot
guarantee that those variables names are unique to a given `defineVars` call.

### Using Media Queries

Variables values can vary based on media queries:

```tsx title="tokens.stylex.js"
import * as stylex from '@stylexjs/stylex';

// A constant can be used to avoid repeating the media query
const DARK = '@media (prefers-color-scheme: dark)';

export const colors = stylex.defineVars({
  primaryText: { default: 'black', [DARK]: 'white' },
  secondaryText: { default: '#333', [DARK]: '#ccc' },
  accent: { default: 'blue', [DARK]: 'lightblue' },
  background: { default: 'white', [DARK]: 'black' },
  lineColor: { default: 'gray', [DARK]: 'lightgray' },
});
```

Similarly, `@supports` can be used as well.

## Rules when defining variables

Variables are the only type of non-local value that can be used within a
`create` call. This is made possible by enforcing a few rules:

#### 1. Variables must be defined in `.stylex.js` files

Variables must be in a file with one of the following extensions:

1. `.stylex.js`
2. `.stylex.mjs`
3. `.stylex.cjs`
4. `.stylex.ts`
5. `.stylex.tsx`
6. `.stylex.jsx`

#### 2. Variables must be named exports

Every `defineVars` call *must* be a named export.

##### Allowed:

```tsx
// ✅ - Named export
export const colors = stylex.defineVars({
  /* ... */
});

const sizeVars = { ... };
// ✅ - Another Named export
export const sizes = stylex.defineVars(sizeVars);
```

##### Not Allowed:

```tsx
// ❌ - Only named exports are allowed
export default stylex.defineVars({
  /* ... */
});

// ❌ - The variable must be exported directly
const x = stylex.defineVars({
  /* ... */
});
export const colors = x;

// ❌ - The variables cannot be nested within another object
export const colors = {
  foregrounds: stylex.defineVars({
    /* ... */
  }),
  backgrounds: stylex.defineVars({
    /* ... */
  }),
};
```

#### 3. No other exports are allowed in the file

For now, `.stylex.js` files are exclusively for defining CSS variables.


# Using variables (/docs/learn/theming/using-variables)

<Callout type="info" title="Note">
  The
  [`unstable_moduleResolution`](/docs/api/configuration/babel-plugin/#unstable_moduleresolution)
  option needs to be enabled in the StyleX Babel configuration to enable theming
  APIs.
</Callout>

Once [variables have been defined](/docs/learn/theming/defining-variables), they
can be imported and used to declare styles with `create`.

Assume the following variables have been defined in a file called
`tokens.stylex.js`:

```tsx title="tokens.stylex.js"
import * as stylex from '@stylexjs/stylex';

// A constant can be used to avoid repeating the media query
const DARK = '@media (prefers-color-scheme: dark)';

export const colors = stylex.defineVars({
  primaryText: { default: 'black', [DARK]: 'white' },
  secondaryText: { default: '#333', [DARK]: '#ccc' },
  accent: { default: 'blue', [DARK]: 'lightblue' },
  background: { default: 'white', [DARK]: 'black' },
  lineColor: { default: 'gray', [DARK]: 'lightgray' },
});

export const spacing = stylex.defineVars({
  none: '0px',
  xsmall: '4px',
  small: '8px',
  medium: '12px',
  large: '20px',
  xlarge: '32px',
  xxlarge: '48px',
  xxxlarge: '96px',
});
```

These styles can then be imported and used like so:

```tsx title="components/MyComponent.js"
import * as stylex from '@stylexjs/stylex';
import { colors, spacing } from '../tokens.stylex';

const styles = stylex.create({
  container: {
    color: colors.primaryText,
    backgroundColor: colors.background,
    padding: spacing.medium,
  },
});
```

## Rules when using variables

There are a few rules to keep in mind when using variables:

1. Named imports must be used for importing variables.
2. Variables must be imported directly from the `.stylex.js` files that define
   them.

<Callout type="tip">
  Remember that StyleX variables are comprised of CSS identifiers. They cannot be
  used as values within JavaScript code.
</Callout>


# Types for Variables (/docs/learn/theming/variable-types)

<Callout type="info" title="Note">
  The
  [`unstable_moduleResolution`](/docs/api/configuration/babel-plugin/#unstable_moduleresolution)
  option needs to be enabled in the StyleX Babel configuration to enable theming
  APIs.
</Callout>

<Callout type="warning" title="Advanced use-case">
  Declaring types for variables is an advanced use-case. It is not necessary for
  the majority of use-cases.
</Callout>

By default, variables values are strings. This is the correct choice for the
majority of use-cases. However, modern browsers support defining types for CSS
variables. A variable can be declared with an `@property` rule that specifies
the `<syntax>` type of the variable.

Doing so can enable some interesting use-cases that would otherwise not be
possible with CSS. Some examples include:

* Animating gradients by animating an angle or color variables
* Capturing the value of `1em` on an element and using it on a descendant
* Converting a floating point number to an integer

## API

To assign types to variables in StyleX, you can use the various functions, such
as `stylex.types.color` or `stylex.types.length`.

Reference the [API documentation](/docs/api/javascript/types) for a full list of
available functions.

## Usage

To assign types to variables, the value of the variable can be wrapped with
the appropriate type function.

For example, consider the following set of variables:

```tsx title="tokens.stylex.js"
import * as stylex from '@stylexjs/stylex';

export const tokens = stylex.defineVars({
  primaryText: 'black',
  secondaryText: '#333',
  borderRadius: '4px',
  angle: '0deg',
  int: '2',
});
```

Currently, all the values can be arbitrary strings. To assign types to the
variables, they can be wrapped with the appropriate type function:

```tsx title="tokens.stylex.js"
import * as stylex from '@stylexjs/stylex';

export const tokens = stylex.defineVars({
  primaryText: stylex.types.color('black'),
  secondaryText: stylex.types.color('#333'),
  borderRadius: stylex.types.length('4px'),
  angle: stylex.types.angle('0deg'),
  int: stylex.types.integer(2),
});
```

### Conditional Values

The usage remains unchanged even when at-rules are used within the values. The
following is completely valid:

```tsx title="tokens.stylex.js"
import * as stylex from '@stylexjs/stylex';

export const colors = stylex.defineVars({
  primaryText: stylex.types.color({ default: 'black', [DARK]: 'white' }),
});
```

## Type-safety in your source code

The primary utility of `stylex.types.*` functions is to enable functionality by
declaring types for variables in the generated CSS. However, the StyleX API also
enhances the type-safety within your own codebase.

When a variable is declared with a certain type within `defineVars`, the static
types will enforce that the same type function is used when the variable is
themed within a `createTheme` call.

```tsx title="theme.js"
import * as stylex from '@stylexjs/stylex';
import { tokens } from './tokens.stylex.js';

export const highContrast = stylex.createTheme(tokens, {
  primaryText: stylex.types.color('black'),
  secondaryText: stylex.types.color('#222'),
  borderRadius: stylex.types.length('8px'),
  angle: stylex.types.angle('0deg'),
  int: stylex.types.integer(4),
});
```

Since the types for the variables are already declared within the `defineVars`
call, the usage of type functions within `createTheme` is functionally a no-op, but
is required by the static types for type-safety.

## Example use-cases

### Simulating [`round()`](https://developer.mozilla.org/en-US/docs/Web/CSS/round)

Modern browsers are starting to support the
[`round()`](https://developer.mozilla.org/en-US/docs/Web/CSS/round) function in
CSS. However, the feature can be simulated with a variable with an `integer`
type:

```tsx
const styles = stylex.create({
  gradient: {
    // Math.floor
    [tokens.int]: `calc(16 / 9)`,

    // Math.round
    [tokens.int]: `calc((16 / 9) + 0.5)`,

    // Now, the "integer" value can be used for styling:
    width: `calc(${tokens.int} * 1px)`,
  },
});
```

Since `tokens.int` is declared with an `integer` type, any fractional value is
discarded and the value is cast into an integer type whenever a value is
assigned.

### Animating gradients

It is usually not possible to animate gradients. However, by using a typed
`angle` variable, the gradient can be animated by animating the angle used
within it.

Instead of animating a *normal* CSS property, the `angle` variable can be
animated with `keyframes`:

```tsx
import * as stylex from '@stylexjs/stylex';
import { tokens } from './tokens.stylex';

const rotate = stylex.keyframes({
  from: { [tokens.angle]: '0deg' },
  to: { [tokens.angle]: '360deg' },
});

const colors = [
  '#ffadad',
  '#ffd6a5',
  '#fdffb6',
  '#caffbf',
  '#9bf6ff',
  '#a0c4ff',
  '#bdb2ff',
  '#ffc6ff',
].join(', ');

const styles = stylex.create({
  gradient: {
    backgroundImage: `conic-gradient(from ${tokens.angle}, ${colors})`,
    animationName: rotate,
    animationDuration: '10s',
    animationTimingFunction: 'linear',
    animationIterationCount: 'infinite',
  },
});
```

This can be used to create rotating conic gradients:

import AnimatedGradientBox from '@/components/AnimatedGradientBox';

<AnimatedGradientBox />


# Thinking in StyleX (/docs/learn/thinking-in-stylex)

## Core Principles

To understand why StyleX exists and the reasoning behind its decisions, it may
be beneficial to familiarize oneself with the fundamental principles that guide
it. This may help you decide if StyleX is the right solution for you.

These principles should also be helpful when designing new APIs for StyleX.

### Co-location

There are benefits of DRY code, but we don't think that's usually true when it
comes to authoring styles. The best and most readable way to write styles is to
write them in the same file as the markup.

StyleX is designed for authoring, applying, and reasoning about styles locally.

### Deterministic resolution

CSS is a powerful and expressive language. However, it can sometimes feel
fragile. Some of this stems from a misunderstanding of how CSS works, but a lot
of it stems from the discipline and organization required to keep CSS selectors
with different specificities from conflicting.

StyleX aims to improve both the consistency and predictability of styles *and*
the expressive power available. We believe this is possible through build-tools.

StyleX provides a completely predictable and deterministic styling system that
works across files. It produces deterministic results not only when merging
multiple selectors, but also when merging multiple shorthand and longhand
properties (e.g. `margin` vs `margin-top`). The last style applied always wins.

### Low-cost abstractions

When it comes to the performance cost of StyleX, our guiding principle is that
StyleX should always be the fastest way to achieve a particular pattern. Common
patterns should have no runtime cost and advanced patterns should be as fast as
possible. We make the trade-off of doing more work at build-time to improve
runtime performance.

Here's how this plays out in practice:

#### 1. Styles created and applied locally

When authoring and consuming styles within the same file, the cost of StyleX is
zero. This is because in addition to compiling away `create` calls, StyleX also
compiles away `props` calls when possible.

So,

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  red: { color: 'red' },
});
let a = stylex.props(styles.red);
```

Compiles down to:

<Tabs>
  <TabItem label="JS Output" value="js-output">
    ```tsx
    import * as stylex from '@stylexjs/stylex';

    let a = { className: 'x1e2nbdu' };
    ```
  </TabItem>

  <TabItem label="CSS Output" value="css-output">
    ```css
    .x1e2nbdu {
      color: red;
    }
    ```
  </TabItem>
</Tabs>

There is no runtime overhead here.

#### 2. Using styles across files

Passing styles across file boundaries incurs a small cost for the additional
power and expressivity. The `create` call is not deleted entirely and instead
leaves behind an object mapping keys to class names. And the `props` calls are
executed at runtime.

This code, for example:

```tsx
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  foo: {
    color: 'red',
  },
  bar: {
    backgroundColor: 'blue',
  },
});

function MyComponent({ style }) {
  return <div {...stylex.props(styles.foo, styles.bar, style)} />;
}
```

Compiles down to:

<Tabs>
  <TabItem label="JS Output" value="js-output">
    ```tsx
    import * as stylex from '@stylexjs/stylex';

    const styles = {
      foo: {
        color: 'x1e2nbdu',
        $$css: true,
      },
      bar: {
        backgroundColor: 'x1t391ir',
        $$css: true,
      },
    };

    function MyComponent({ style }) {
      return <div {...stylex.props(styles.foo, styles.bar, style)} />;
    }
    ```
  </TabItem>

  <TabItem label="CSS Output" value="css-output">
    ```css
    .x1e2nbdu {
      color: red;
    }
    .x1t391ir {
      background-color: blue;
    }
    ```
  </TabItem>
</Tabs>

This is a little more code, but the runtime cost is still minimal because of how
fast the `props` function is.

Most other styling solutions don't enable composition of styles across file
boundaries. The state of the art is to combine lists of class names.

### Small API surface

Our goal is to make StyleX as minimal and easy-to-learn as possible. As such we
don't want to invent too many APIs. Instead, we want to be able to lean on
common JavaScript patterns where possible and provide the smallest API surface
possible.

At its core, StyleX can be boiled down to two functions:

1. `stylex.create`
2. `stylex.props`

`create` is used to create styles and `props` is used to apply those styles to
an element.

Within these two functions, we choose to rely on common JS patterns rather than
introduce unique APIs or patterns for StyleX. For example, we don't have an API
for conditional styles. Instead, we support applying styles conditionally with
boolean or ternary expressions.

Things should work as expected when dealing with JavaScript objects and arrays.
There should be no surprises.

### Type-Safe styles

TypeScript has become massively popular due to the experience and safety it
provides. Our styles, however, have largely remained untyped and unreliable.
Other than some path-breaking projects such as
[Vanilla Extract](https://vanilla-extract.style/), styles are just bags of
strings in most styling solutions.

StyleX is authored in Flow with strong static types. Its packages on NPM come
with auto-generated types for both Flow and TypeScript. When there are
incompatibilities between the two type-systems, we take the time to ensure that
we write custom TypeScript types to achieve the same level of power and safety
as the original Flow.

*All styles are typed*. When accepting styles as props, types can be used to
constrain what styles are accepted. Styles should be as type-safe as any other
component props.

The StyleX API is strongly typed. The styles defined with StyleX are typed too.
This is made possible by using JavaScript objects to author raw styles. This is
one of the big reasons we have chosen objects over template strings.

These types can then be leveraged to set contracts for the styles that a
component will accept. For example, a component props can be defined to only
accept `color` and `backgroundColor` but no other styles.

```ts
import type { StyleXStyles } from '@stylexjs/stylex';

type Props = {
  //...
  style?: StyleXStyles<{ color?: string; backgroundColor?: string }>;
  //...
};
```

In another example, the props may disallow margins while allowing all other
styles.

```ts
import type { StyleXStylesWithout } from '@stylexjs/stylex';

type Props = {
  //...
  style?: StyleXStylesWithout<{
    margin: unknown;
    marginBlock: unknown;
    marginInline: unknown;
    marginTop: unknown;
    marginBottom: unknown;
    marginLeft: unknown;
    marginRight: unknown;
    marginBlockStart: unknown;
    marginBlockEnd: unknown;
    marginInlineStart: unknown;
    marginInlineEnd: unknown;
  }>;
  //...
};
```

Styles being typed enables extremely sophisticated rules about how a component's
styles can be customized with **zero-runtime cost**.

### Shareable constants

CSS class names, CSS variables, and other CSS identifiers are defined in a
global namespace. Bringing CSS strings into JavaScript can mean losing
type-safety and composability.

We want styles to be type-safe, so we've spent a lot of time coming up with APIs
to replace these strings with references to JavaScript constants. So far this is
reflected in the following APIs:

1. `create` Abstracts away the generated class names entirely. You deal with
   "opaque" JavaScript objects with strong types to indicate the styles they
   represent.
2. `defineVars` Abstracts away the names of CSS variables generated. They can be
   imported as constants and used within styles directly.
3. `keyframes` Abstracts away the names of keyframe animations. Instead they are
   declared as constants and used by reference.

We're looking into ways to make other CSS identifiers such as `container-name`
and `@font-face` type-safe as well.

### Framework-agnostic

StyleX is a CSS-in-JS solution, not a CSS-in-React solution. Although StyleX has
been tailored to work best with React today, it is designed to be used with any
JavaScript framework that allows authoring markup in JavaScript. This includes
frameworks that use JSX, template strings, etc.

`props` returns an object with `className` and `style` properties. A wrapper
function may be needed to convert this to make it work with various frameworks.

### Encapsulation

> All styles on an element should be caused by class names on that element
> itself.

CSS makes it very easy to author styles in a way that can cause "styles at a
distance":

* `.className > *`
* `.className ~ *`
* `.className:hover button`

All of these patterns, while powerful, make styles fragile, less predictable and
harder to debug. An element could be styled without having any classes applied
to it.

StyleX enables these capabilities using a different pattern that doesn't have
the same trade-offs. The `stylex.when.*` APIs, rely on classes that can be used
to "mark" an element which can then be "observed at a distance" for conditional
styling. More concretely, instead of a selector like `.className:hover button`,
StyleX relies on selectors like `.marked:hover .btn`. The button is always
explicitly styled with a className (`btn` in this case) which *observes* the
hover state of the marked ancestor. Without the `btn` class, the presence of the
`marked` class would not affect the button at all.

Inheritable styles such as `color` will still be inherited, but that is the
*only* form of style-at-a-distance that StyleX allows. In those cases too, the
styles applied directly on an element always take precedence over inherited
styles.

### Readability & maintainability over terseness

Some recent utility-based styling solutions are extremely terse and easy to
write. StyleX chooses to prioritize readability and maintainability over
terseness.

StyleX makes the choice to use familiar CSS property names to prioritize
readability and a shallow learning curve. *(We did decide to use camelCase
instead of kebab-case for convenience.)*

We also enforce that styles are authored in objects separate from the HTML
elements where they are used. We made this decision to help with the readability
of HTML markup and for appropriately named styles to indicate their purpose. For
example, using a name like `styles.active` emphasizes *why* styles are being
applied without having to dig through *what* styles are being applied.

This principle leads to trade-offs where authoring styles may take more typing
with StyleX than some other solutions.

We believe these costs are worth the improved readability over time. Giving each
HTML element a semantic name can communicate a lot more than the styles
themselves.

<Callout type="info">
  One side benefit of using references to styles rather than using the styles
  inline is **testability**. In a unit-testing environment, StyleX can be
  configured to remove all atomic styles and only output single debugging class
  names to indicate the source location of styles rather than the actual styles.

  Among other benefits, it makes snapshot tests more resilient as they won't
  change for every style change.
</Callout>

### Modularity and composability

NPM has made it extremely easy to share code across projects. However, sharing
CSS has remained a challenge. Third-party components either have styles baked in
that are hard or impossible to customize, or are completely unstyled.

The lack of a good system to predictably merge and compose styles across
packages has also been an obstacle when sharing styles within packages.

StyleX aims to create a system to easily and reliably share styles along with
components within packages on NPM.

### Avoid global configuration

StyleX should work similarly across projects. Creating project-specific
configurations that change the syntax or behavior of StyleX should be avoided.
We have chosen to prioritize composability and consistency over short-term
convenience. We lean on linting and types to create project-specific rules.

We also avoid magic strings that have special meaning within a project globally.
Instead, every style, every variable, and every shared constant is imported from
a JavaScript module without needing unique names or project configuration.

### One small file over many smaller files

When dealing with a large amount of CSS, lazy-loading CSS is a way to speed up
the initial load time of a page. However, it comes at the cost of slower update
times, or the *Interaction to Next Paint (INP)* metric. Lazy-loading any CSS on
a page triggers a recalculation of styles for the entire page.

StyleX is optimized for generating a single, highly optimized, CSS bundle that
is loaded upfront. Our goal is to create a system where the total amount of CSS
is small enough that all the CSS can be loaded upfront without a noticeable
performance impact.

Other techniques to make the initial load times faster, such as "critical CSS"
are compatible with StyleX, but should normally be unnecessary.


# LLM Resources (/docs/llm-resources)

These files are intended to give LLM agents clear context on StyleX setup and usage. You can pass these files in as context for your agent or use them directly within prompts.

You can also download these files directly on
[GitHub](https://github.com/facebook/stylex/tree/main/packages/docs/static/llm).

## Installation guide

Steps to install or integrate StyleX across Vite, Next.js, Webpack, Rspack, and Esbuild apps.

<LLMInstallationFile />

## Style authoring guide

Context on defining and using styles, StyleX APIs, and common antipatterns.

<LLMStylingFile />
