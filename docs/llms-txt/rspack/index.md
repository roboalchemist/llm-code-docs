# Source: https://rspack.dev/contribute/index.md

# Source: https://rspack.dev/blog/index.md

# Source: https://rspack.dev/api/plugin-api/index.md

# Source: https://rspack.dev/api/loader-api/index.md

# Source: https://rspack.dev/api/javascript-api/index.md

# Source: https://rspack.dev/api/index.md

# Source: https://rspack.dev/plugins/webpack/index.md

# Source: https://rspack.dev/plugins/index.md

# Source: https://rspack.dev/config/index.md

# Configure Rspack

Rspack provides configurations similar to webpack. This chapter will show you how to use the Rspack configuration.

## Configuration file

When you run the Rspack CLI, Rspack automatically reads the `rspack.config.*` file in the current working directory.

A basic Rspack configuration file looks like this:


**ESM**

```js title="rspack.config.mjs"
import { defineConfig } from '@rspack/cli';

export default defineConfig({
  entry: {
    main: './src/index.js',
  },
});
```


**CJS**

```js title="rspack.config.cjs"
const { defineConfig } = require('@rspack/cli');

module.exports = defineConfig({
  entry: {
    main: './src/index.js',
  },
});
```


**TypeScript**

```ts title="rspack.config.ts"
import { defineConfig } from '@rspack/cli';

export default defineConfig({
  entry: {
    main: './src/index.js',
  },
});
```


## Configuration file formats

Rspack supports these configuration file formats:

- `rspack.config.js`: defaults to `CommonJS` format, or `ES modules` format if the type of the package.json is "module".
- `rspack.config.ts`: `TypeScript` format, see [TypeScript configuration file](#typescript-configuration-file) for more details.
- `rspack.config.cjs`: Forced to `CommonJS` format.
- `rspack.config.mjs`: Forced to `ES modules` format.

Note that Rspack will first search JS configuration file and then TS configuration file.

> See [ES modules](https://nodejs.org/api/esm.html#modules-ecmascript-modules) and [CommonJS](https://nodejs.org/api/modules.html) for the difference between `CommonJS` and `ES modules`.

## Extending configurations

See [Extending Configurations](/config/extends.md) for details on how to extend configurations from other files or packages.

## TypeScript configuration file

When using `rspack.config.ts`, you can choose from one of the following approaches:

### Default behavior

Starting from v1.5.0, Rspack CLI has built-in support for TypeScript configuration, using SWC by default to transform TypeScript code into CommonJS format JavaScript code.

If you're using a Rspack CLI earlier than v1.5.0, it's recommended to upgrade to the latest version. You no longer need to load configuration files through `ts-node` or `esbuild-register`, and these dependencies can be removed.

### Native support

If your JavaScript runtime already natively supports TypeScript, you can use the built-in TS transformation to load the configuration file, ensuring that module resolution behavior is consistent with native behavior.

For example, Node.js already natively supports TypeScript, you can use the following command to use the Node.js native loader to load the configuration file:

- For Node.js v22.18+ and v24.3+ which support native TypeScript by default, you can run the following command to load the TS config:

```json title="package.json"
{
  "scripts": {
    "build": "rspack build --configLoader=native"
  }
}
```

See [Node.js - Running TypeScript Natively](https://nodejs.org/en/learn/typescript/run-natively#running-typescript-natively) for more details.

### Using esbuild

For lower Node.js versions, you can use `esbuild-register` to load the configuration file.

Install [esbuild](https://npmjs.com/package/esbuild) and [esbuild-register](https://npmjs.com/package/esbuild-register), no additional configuration is needed.


```sh [npm]
npm add esbuild esbuild-register -D
```

```sh [yarn]
yarn add esbuild esbuild-register -D
```

```sh [pnpm]
pnpm add esbuild esbuild-register -D
```

```sh [bun]
bun add esbuild esbuild-register -D
```

```sh [deno]
deno add npm:esbuild npm:esbuild-register -D
```

### Using ts-node

You can also use [ts-node](https://npmjs.com/package/ts-node) to load the configuration file.

1. Install `ts-node`:


```sh [npm]
npm add ts-node -D
```

```sh [yarn]
yarn add ts-node -D
```

```sh [pnpm]
pnpm add ts-node -D
```

```sh [bun]
bun add ts-node -D
```

```sh [deno]
deno add npm:ts-node -D
```

2. Then configure `ts-node` to use `CommonJS` modules in `tsconfig.json`:

```json title="tsconfig.json"
{
  "ts-node": {
    "compilerOptions": {
      "module": "CommonJS"
    }
  }
}
```

## Type checking

Use the `defineConfig` helper to enable auto-completion. For JavaScript configuration files, you can use the `// @ts-check` comment to enable type checking.


**TypeScript**

```ts title="rspack.config.ts"
import { defineConfig } from '@rspack/cli';

export default defineConfig({
  entry: {
    main: './src/index.js',
  },
});
```


**JavaScript**

```js title="rspack.config.mjs"
// @ts-check
import { defineConfig } from '@rspack/cli';

export default defineConfig({
  entry: {
    main: './src/index.js',
  },
});
```


Alternatively, you can use [JSDoc](https://jsdoc.app/) for type checking.

```js title="rspack.config.mjs"
// @ts-check
/** @type {import('@rspack/cli').Configuration} */
const config = {
  entry: {
    main: './src/index.js',
  },
};
export default config;
```

## Specify the configuration file

Specify the name of the configuration file using the `--config` option.

For example, if you need to use the `rspack.prod.config.js` file when running build, you can add the following scripts to `package.json`:

```json title="package.json"
{
  "scripts": {
    "dev": "rspack serve",
    "build": "rspack build --config rspack.prod.config.js"
  }
}
```

Abbreviate the `--config` option to `-c`:

```bash
$ rspack build -c rspack.prod.config.js
```

## Exporting a configuration function

Rspack supports exporting a function in Rspack configuration file, you can dynamically compute the configuration in the function and return it to Rspack.

```js title="rspack.config.mjs"
export default function (env, argv) {
  return {
    devtool: env.production ? 'source-map' : 'eval',
  };
}
```

As you can see from the example above, the function takes two input parameters:

- The first argument is `env`, which corresponds to the value of the `--env` option when running the CLI command.
- The second argument is `argv`, which contains all the options passed to the CLI.

### Determine the current environment

In addition to passing the `env` parameter, it is more common to use `process.env.NODE_ENV` to determine the current environment:

```js title="rspack.config.mjs"
export default function (env, argv) {
  const isProduction = process.env.NODE_ENV === 'production';
  return {
    devtool: isProduction ? 'source-map' : 'eval',
  };
}
```

## Merge configurations

Use Rspack's [extends](/config/extends.md) option or [webpack-merge](https://npmjs.com/package/webpack-merge) package to merge multiple Rspack configurations.

### extends option

When using [@rspack/cli](/api/cli.md), Rspack provides the `extends` option, allowing you to extend configurations from other files or packages.

```js title="rspack.config.mjs"
export default {
  extends: './base.rspack.config.mjs',
  output: {
    filename: '[name].bundle.js',
  },
};
```

> This option is only supported in `@rspack/cli`, see [extends](/config/extends.md) for more usage.

### webpack-merge

`webpack-merge` is a community library for merging multiple webpack configurations, and it can also be used to merge Rspack configurations.

First install `webpack-merge`:


```sh [npm]
npm add webpack-merge -D
```

```sh [yarn]
yarn add webpack-merge -D
```

```sh [pnpm]
pnpm add webpack-merge -D
```

```sh [bun]
bun add webpack-merge -D
```

```sh [deno]
deno add npm:webpack-merge -D
```

Then you can use its `merge` function to merge configurations:

```js title="rspack.config.mjs"
import { merge } from 'webpack-merge';

const isDev = process.env.NODE_ENV === 'development';
const base = {};
const dev = {
  plugins: [new SomeDevPlugin()],
};

export default isDev ? merge(base, dev) : base;
```

> See [webpack-merge documentation](https://npmjs.com/package/webpack-merge) for more details.
