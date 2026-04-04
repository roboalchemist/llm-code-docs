# Source: https://rsbuild.dev/guide/migration/vite-plugin.md

# Vite plugin

This chapter introduces how to migrate a Vite plugin to Rsbuild plugin.

## Existing plugins

Before migrating a Vite plugin, it is recommended to check if there is a corresponding plugin in the Rsbuild ecosystem. You can find the plugins through the following pages:

* [Rsbuild official plugins](/plugins/list.md)
* [Rsbuild community plugins](https://github.com/rstackjs/awesome-rstack?tab=readme-ov-file#rsbuild-plugins)

## Define a plugin

Rsbuild plugin is defined in a way similar to Vite, usually a function that accepts plugin options as a parameter and returns a plugin description object.

The main difference is that Vite's hooks are defined directly on the plugin description object, while Rsbuild's hooks are accessed and called through the [api object](/plugins/dev/core.md). This allows you to control the timing of plugin API calls more flexibly.

* Vite plugin:

```ts title="vitePlugin.ts"
const vitePlugin = (options) => ({
  name: 'vite-plugin',
  transform() {
    // ...
  },
});
```

* Rsbuild plugin:

```ts title="rsbuildPlugin.ts"
const rsbuildPlugin = (options) => ({
  name: 'rsbuild-plugin',
  setup(api) {
    api.transform(() => {
      // ...
    });
  },
});
```

## Plugin hooks

Rsbuild's plugin API covers most of the Vite and Rollup plugin hooks, for example:

| Vite plugin hooks    | Rsbuild plugin API                                                                                                     |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `resolveId`          | [resolve](/plugins/dev/core.md#apiresolve)                                                                                |
| `transform`          | [transform](/plugins/dev/core.md#apitransform)                                                                            |
| `config`             | [modifyRsbuildConfig](/plugins/dev/hooks.md#modifyrsbuildconfig)                                                          |
| `configResolved`     | [getNormalizedConfig](/plugins/dev/core.md#apigetnormalizedconfig)                                                        |
| `configEnvironment`  | [modifyEnvironmentConfig](/plugins/dev/hooks.md#modifyenvironmentconfig)                                                  |
| `configureServer`    | [onBeforeStartDevServer](/plugins/dev/hooks.md#onbeforestartdevserver)                                                    |
| `buildStart`         | [onBeforeBuild](/plugins/dev/hooks.md#onbeforebuild), [onBeforeStartDevServer](/plugins/dev/hooks.md#onbeforestartdevserver) |
| `buildEnd`           | [onAfterBuild](/plugins/dev/hooks.md#onafterbuild), [onCloseDevServer](/plugins/dev/hooks.md#onclosedevserver)               |
| `closeBundle`        | [onCloseBuild](/plugins/dev/hooks.md#onclosebuild), [onCloseDevServer](/plugins/dev/hooks.md#onclosedevserver)               |
| `transformIndexHtml` | [modifyHTML](/plugins/dev/hooks.md#modifyhtml), [modifyHTMLTags](/plugins/dev/hooks.md#modifyhtmltags)                       |

See [Plugin system](/plugins/dev/index.md) for more details.

## `config` hook

Rsbuild provides the [modifyRsbuildConfig](/plugins/dev/hooks.md#modifyrsbuildconfig) hook to modify Rsbuild configuration. Since Rsbuild and Vite have different configuration structures, you'll need to adjust your configuration when migrating Vite plugins.

For example, you should replace Vite's `define` option with Rsbuild's [source.define](/config/source/define.md) option.

* Vite plugin:

```ts title="vitePlugin.ts"
const vitePlugin = {
  name: 'my-plugin',
  config: (config) => {
    config.define = {
      ...config.define,
      FOO: '"foo"',
    };
  },
};
```

* Rsbuild plugin:

```ts title="rsbuildPlugin.ts"
const rsbuildPlugin = {
  name: 'my-plugin',
  setup(api) {
    api.modifyRsbuildConfig((config) => {
      config.source ||= {};
      config.source.define = {
        ...config.source.define,
        FOO: '"foo"',
      };
    });
  },
};
```

:::tip
See [Config migration](/guide/migration/vite.md#config-migration) to learn how to migrate Vite configurations to Rsbuild.
:::

## `configEnvironment` hook

Rsbuild provides the [modifyEnvironmentConfig](/plugins/dev/hooks.md#modifyenvironmentconfig) hook to modify the configuration of a specific environment.

* Vite plugin:

```ts
const vitePlugin = {
  name: 'config-environment',
  configEnvironment(name, config) {
    if (name === 'web') {
      config.resolve.alias = {
        // ...
      };
    }
  },
};
```

* Rsbuild plugin:

```js
const rsbuildPlugin = {
  name: 'config-environment',
  setup(api) {
    api.modifyEnvironmentConfig((config, { name }) => {
      if (name === 'web') {
        config.resolve.alias = {
          // ...
        };
      }
    });
  },
};
```

## `configResolved` hook

Rsbuild provides the [api.getNormalizedConfig](/plugins/dev/core.md#apigetnormalizedconfig) method to get the resolved configuration. This method serves a similar purpose to Vite's `configResolved` hook.

* Vite plugin:

```ts title="vitePlugin.ts"
const vitePlugin = () => {
  let config;
  return {
    name: 'read-config',
    configResolved(resolvedConfig) {
      config = resolvedConfig;
    },
    transform() {
      console.log(config);
      // ...
    },
  };
};
```

* Rsbuild plugin:

```ts title="rsbuildPlugin.ts"
const rsbuildPlugin = () => ({
  name: 'read-config',
  setup(api) {
    api.transform(() => {
      const config = api.getNormalizedConfig();
      console.log(config);
      // ...
    });
  },
});
```

## `transformIndexHtml` hook

Vite's `transformIndexHtml` hook corresponds to two hooks in Rsbuild:

* [modifyHTML](/plugins/dev/hooks.md#modifyhtml): for modifying HTML content
* [modifyHTMLTags](/plugins/dev/hooks.md#modifyhtmltags): for modifying HTML tags

Here is an example of replacing the HTML title.

* Vite Plugin:

```ts title="vitePlugin.ts"
const htmlPlugin = () => {
  return {
    name: 'html-plugin',
    transformIndexHtml(html) {
      return html.replace(
        /<title>(.*?)<\/title>/,
        `<title>Title replaced!</title>`,
      );
    },
  };
};
```

* Rsbuild Plugin:

```ts title="rsbuildPlugin.ts"
const rsbuildPlugin = {
  name: 'html-plugin',
  setup(api) {
    api.modifyHTML((html) => {
      return html.replace(
        /<title>(.*?)<\/title>/,
        `<title>Title replaced!</title>`,
      );
    });
  },
};
```

## `configureServer` hook

Rsbuild provides the `onBeforeStartDevServer` hook to replace Vite's `configureServer` hook, which allows you to get the dev server instance and add custom middleware.

* Vite plugin:

```ts title="vitePlugin.ts"
const vitePlugin = () => ({
  name: 'setup-middleware',
  configureServer(server) {
    server.middlewares.use((req, res, next) => {
      // custom handle request...
    });
  },
});
```

* Rsbuild plugin:

```ts title="rsbuildPlugin.ts"
const rsbuildPlugin = {
  name: 'setup-middleware',
  setup(api) {
    api.onBeforeStartDevServer(({ server }) => {
      server.middlewares.use((req, res, next) => {
        // custom handle request...
      });
    });
  },
};
```

## `apply` property

Rsbuild plugin provides the same [apply property](/plugins/dev/core.md#conditional-application) as Vite plugins.

* Vite plugin:

```ts title="vitePlugin.ts"
const vitePlugin = {
  name: 'vite-plugin',
  apply: 'build',
};
```

* Rsbuild plugin:

```ts title="rsbuildPlugin.ts"
const rsbuildPlugin = {
  name: 'rsbuild-plugin',
  apply: 'build',
};
```
