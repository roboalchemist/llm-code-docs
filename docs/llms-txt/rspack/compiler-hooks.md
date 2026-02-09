# Source: https://rspack.dev/api/plugin-api/compiler-hooks.md

# Compiler hooks

Compiler hooks allow Rspack plugins to intervene at specific stages of the build process. These hooks represent various lifecycle stages from initialization to asset output.

This document lists the available compiler hooks in Rspack, their trigger timing, parameters, and usage examples.

:::tip
See [Compiler](/api/javascript-api/compiler.md) for more information about the Compiler object.
:::

## Overview


## `environment`

Called while preparing the compiler environment, right after initializing the plugins in the configuration file.

- **Type:** `SyncHook<[]>`

## `afterEnvironment`

Called right after the `environment` hook, when the compiler environment setup is complete.

- **Type:** `SyncHook<[]>`

## `entryOption`

Called after the [`entry`](/config/entry.md) configuration from Rspack options has been processed.

- **Type:** `SyncBailHook<[string, EntryNormalized]>`
- **Arguments:**
  - `string`: same with [`context`](/config/context.md)
  - `EntryNormalized`: normalized [`entry`](/config/entry.md)

## `afterPlugins`

Called after setting up initial set of internal plugins.

- **Type:** `SyncHook<[Compiler]>`
- **Arguments:**
  - `Compiler`: current compiler instance

Compiler.ts
## `afterResolvers`

Triggered after resolver setup is complete.

- **Type:** `SyncHook<[Compiler]>`
- **Arguments:**
  - `Compiler`: current compiler instance

Compiler.ts
## `initialize`

Called when a compiler object is initialized.

- **Type:** `SyncHook<[]>`

## `beforeRun`

Adds a hook right before running the compiler.

:::note

This hook is only triggered when calling [compiler.run()](/api/javascript-api/index.md#compilerrun) (which is used by the `rspack build` command), and will not be executed in watch mode. You can use the [watchRun](#watchrun) hook in watch mode.

:::

- **Type:** `AsyncSeriesHook<[Compiler]>`
- **Arguments:**
  - `Compiler`: current compiler instance

Compiler.ts
- **Example:** Sync operation

```js
class ExamplePlugin {
  apply(compiler) {
    compiler.hooks.beforeRun.tap('ExamplePlugin', (compiler) => {
      console.log('Build is about to start...');
    });
  }
}
```

- **Example:** Async operation

```js
class ExamplePlugin {
  apply(compiler) {
    compiler.hooks.beforeRun.tapPromise(
      'ExamplePlugin',
      (compiler) => {
        console.log('Build is about to start...');

        await someAsyncOperation();
      },
    );
  }
}
```

## `run`

Called at the beginning of a build execution.

:::note

This hook is only triggered when calling [compiler.run()](/api/javascript-api/index.md#compilerrun) (which is used by the `rspack build` command), and will not be executed in watch mode. You can use the [watchRun](#watchrun) hook in watch mode.

:::

- **Type:** `AsyncSeriesHook<[Compiler]>`
- **Arguments:**
  - `Compiler`: current compiler instance

Compiler.ts
- **Example:** Sync operation

```js
class ExamplePlugin {
  apply(compiler) {
    compiler.hooks.beforeRun.tap('ExamplePlugin', (compiler) => {
      console.log('Build start...');
    });
  }
}
```

- **Example:** Async operation

```js
class ExamplePlugin {
  apply(compiler) {
    compiler.hooks.beforeRun.tapPromise(
      'ExamplePlugin',
      (compiler) => {
        console.log('Build start...');

        await someAsyncOperation();
      },
    );
  }
}
```

## `watchRun`

Executes a plugin during watch mode after a new compilation is triggered but before the compilation is actually started.

You can use `compiler.modifiedFiles` and `compiler.removedFiles` to get the changed file paths and removed file paths.

:::note

This hook is only triggered when calling [compiler.watch()](/api/javascript-api/index.md#compilerwatch), and will not be called in non-watch mode. You can use the [run](#run) or [beforeRun](#beforerun) hook in non-watch mode.

:::

- **Type:** `AsyncSeriesHook<[Compiler]>`
- **Arguments:**
  - `Compiler`: current compiler instance

Compiler.ts
- **Example:** Sync operation

```js
class ExamplePlugin {
  apply(compiler) {
    compiler.hooks.watchRun.tap('ExamplePlugin', (compiler) => {
      const { modifiedFiles, removedFiles } = compiler;
      if (modifiedFiles) {
        console.log('Changed files:', Array.from(modifiedFiles));
      }
      if (removedFiles) {
        console.log('Removed files:', Array.from(removedFiles));
      }
    });
  }
}
```

- **Example:** Async operation

```js
class ExamplePlugin {
  apply(compiler) {
    compiler.hooks.watchRun.tapPromise('ExamplePlugin', compiler => {
      await someAsyncOperation();
    });
  }
}
```

## `beforeCompile`

Executes a plugin after compilation parameters are created.

- **Type:** `AsyncSeriesHook<[]>`

## `compile`

Called right after `beforeCompile`, before a new [compilation object](/api/javascript-api/compilation.md) is created.

- **Type:** `SyncHook<[]>`

## `thisCompilation`

Called while initializing the compilation, can be used to get the current compilation object.

You can use the `compilation` parameter to access the properties of the compilation object, or register [compilation hooks](/api/plugin-api/compilation-hooks.md).

- **Type:** `SyncHook<[Compilation]>`
- **Arguments:**
  - `compilation`: created [compilation](/api/javascript-api/compilation.md) object

Compilation.ts
- **Example:**

```js
class ExamplePlugin {
  apply(compiler) {
    compiler.hooks.thisCompilation.tap('ExamplePlugin', (compilation) => {
      console.log('compilation created:', compilation);

      compilation.hooks.make.tap('ExamplePlugin', (compilation) => {
        console.log("compilation's make hook called:", compilation);
      });
    });
  }
}
```

## `compilation`

Called after the compilation object is created, can be used to get the current compilation object.

You can use the `compilation` parameter to access the properties of the compilation object, or register [compilation hooks](/api/plugin-api/compilation-hooks.md).

`compilation` hook is called after the [thisCompilation](#thiscompilation) hook, and `thisCompilation` hook is not copied to child compiler, while `compilation` hook is copied to child compiler.

- **Type:** `SyncHook<[Compilation]>`
- **Arguments:**
  - `compilation`: created [compilation](/api/javascript-api/compilation.md) object

Compilation.ts
```js
class ExamplePlugin {
  apply(compiler) {
    compiler.hooks.compilation.tap('ExamplePlugin', (compilation) => {
      console.log('compilation created:', compilation);

      compilation.hooks.make.tap('ExamplePlugin', (compilation) => {
        console.log("compilation's make hook called:", compilation);
      });
    });
  }
}
```

## `make`

Called before the make phase.

In the make phase, Rspack will build the module graph starting from the entry, and use the loader to handle each module.

- **Type:** `AsyncParallelHook<[Compilation]>`
- **Arguments:**
  - `Compilation`: current [compilation](/api/javascript-api/compilation.md) object

Compilation.ts
## `finishMake`

Called after finishing the make phase.

In the make phase, Rspack builds the module graph starting from the entry and uses loaders to handle each module. This hook is called when that process completes.

- **Type:** `AsyncSeriesHook<[Compilation]>`
- **Arguments:**
  - `Compilation`: current [compilation](/api/javascript-api/compilation.md) object

Compilation.ts
## `afterCompile`

Called after the make phase and before the seal phase.

In the seal phase, Rspack will create chunk graph from the module graph and then generate the assets.

- **Type:** `AsyncSeriesHook<[Compilation]>`
- **Arguments:**
  - `Compilation`: current [compilation](/api/javascript-api/compilation.md) object

Compilation.ts
## `shouldEmit`

Called before emitting assets. Should return a boolean telling whether to emit.

- **Type:** `SyncBailHook<[Compilation], boolean>`
- **Arguments:**
  - `Compilation`: current [compilation](/api/javascript-api/compilation.md) object

Compilation.ts
- **Example:**

```js
compiler.hooks.shouldEmit.tap('MyPlugin', (compilation) => {
  // return true to emit the output, otherwise false
  return true;
});
```

## `emit`

Called right before emitting assets to output dir.

- **Type:** `AsyncSeriesHook<[Compilation]>`
- **Arguments:**
  - `Compilation`: current [compilation](/api/javascript-api/compilation.md) object

Compilation.ts
## `afterEmit`

Called after emitting assets to output directory.

- **Type:** `AsyncSeriesHook<[Compilation]>`
- **Arguments:**
  - `Compilation`: current [compilation](/api/javascript-api/compilation.md) object

Compilation.ts
## `done`

Called when the compilation has completed.

- **Type:** `AsyncSeriesHook<Stats>`
- **Arguments:**
  - `Stats`: generated stats object

Stats.ts
## `afterDone`

Called after `done` hook.

- **Type:** `SyncHook<Stats>`
- **Arguments:**
  - `Stats`: generated stats object

Stats.ts
## `failed`

Called if the compilation fails.

- **Type:** `SyncHook<[Error]>`

## `invalid`

Executed when a watching compilation has been invalidated. This hook is not copied to child compilers.

- **Type:** `SyncHook<[string | null, number]>`
- **Arguments:**
  - `fileName`: the file path of the invalid file
  - `changeTime`: the change time of the invalid file

When triggering a re-compilation, this hook can be used to get the changed file path and change time, for example:

```ts
compiler.hooks.invalid.tap('MyPlugin', (fileName, changeTime) => {
  console.log(`Changed file: ${fileName}, change time: ${changeTime}`);
});
```

## `watchClose`

Called when a watching compilation has stopped.

- **Type:** `SyncHook<[]>`

## `shutdown`

Called when the compiler is closing.

- **Type:** `AsyncSeriesHook<[]>`

## infrastructureLog

Called when infrastructure logging is triggered, allowing plugins to intercept, modify, or handle log messages.

This hook provides a way to customize Rspack's infrastructure logs - you can filter specific log types, add custom formatting, or completely override the default logging behavior.

If the hook returns `true`, the default infrastructure logging will be prevented. If it returns `undefined`, the default logging will proceed.

- **Type:** `SyncBailHook<[string, string, any[]], true | void>`
- **Arguments:**
  - `name`: The name of the logger
  - `type`: The log type (e.g., 'log', 'warn', 'error', ...)
  - `args`: An array of arguments passed to the logging method
- **Example:**

```js
class ExamplePlugin {
  apply(compiler) {
    compiler.hooks.infrastructureLog.tap('MyPlugin', (name, type, args) => {
      // Custom logging logic
      if (type === 'error') {
        console.error(`[${name}] ERROR:`, ...args);
        return true; // Prevent default logging
      }

      // Let other log types use default behavior
      return undefined;
    });
  }
}
```

> See [infrastructureLogging](/config/infrastructure-logging.md) to learn more about infrastructure logging.
