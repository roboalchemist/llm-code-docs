# Source: https://rspack.dev/config/mode.md

CC 4.0 License> The content of this section is derived from the content of the following links and is subject to the CC BY 4.0 license.
> 
> - [https://webpack.js.org/configuration/mode/](https://webpack.js.org/configuration/mode/)
> 
> The following contents can be assumed to be the result of modifications and deletions based on the original contents if not specifically stated.
> 
> 


# Mode

- Type: `'production' | 'development' | 'none'`
- Default:`'production'`


The `mode` configuration is used to set the build mode of Rspack to enable the default optimization strategy.

## Usage

You can set the mode directly in Rspack config:

```js title="rspack.config.mjs"
export default {
  mode: 'production',
};
```

In actual scenarios, you can dynamically set the mode according to `process.env.NODE_ENV`:

```js title="rspack.config.mjs"
const isProduction = process.env.NODE_ENV === 'production';

export default {
  mode: isProduction ? 'production' : 'development',
};
```

Alternatively, you can set the mode using the `--mode` option on the Rspack CLI:

```bash
rspack --mode=production
```

:::info
`--mode` option on the CLI has a higher priority than `mode` in Rspack config.
:::

## Optional values

`mode` has the following optional values:

### production

In production mode, Rspack automatically enables the following optimization strategies:

- Replace `process.env.NODE_ENV` in code with `'production'`.
- Set the default value of `optimization.minimize` to `true` to enable SWC minification.

### development

In development mode, Rspack automatically enables the following optimization strategies:

- Replace `process.env.NODE_ENV` in code with `'development'`.
- Set proper naming format for modules and chunks.

### none

When `mode` is set to `'none'`, Rspack will not enable any default optimization strategies.
