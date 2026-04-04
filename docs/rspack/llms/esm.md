# Source: https://rspack.dev/guide/features/esm.md

# ESM output

Rspack supports building with ESM format output. When building applications, Rspack generates IIFE-based bundled output by default instead of standard CommonJS or ESM format. You can configure [output.module](/config/output.md#outputmodule) to generate ESM format output. The following sections introduce how to [build application ESM output](#building-application-esm-output) and [build library ESM output](#building-library-esm-output), and finally list the [configuration checklist](#configuration-checklist) related to ESM output.

## Building application ESM output

When building applications, Rspack generates CommonJS-like format output by default. If you need to generate ESM format output, you can configure it in `rspack.config.mjs` as follows:

```js title="rspack.config.mjs"
export default {
  //...
  output: {
    module: true,
    chunkFormat: 'module',
    chunkLoading: 'import',
    workerChunkLoading: 'import',
  },
  experiments: {
    outputModule: true,
  },
};
```

You can check out examples of [building React applications to ESM output](https://github.com/rstackjs/rstack-examples/tree/main/rspack/react-refresh-esm) and [React ESM SSR](https://github.com/rstackjs/rstack-examples/tree/main/rspack/react-ssr-esm) in rspack-examples.

## Building library ESM output

We recommend using [Rslib](https://rslib.rs) to build library output. Rslib is built on top of Rspack and can build multiple formats including ES Module, CommonJS, and UMD. Rslib provides higher-level APIs that simplify the library building process. Compared to using Rspack directly, using Rslib for library building is more convenient and efficient.

If you need to use Rspack directly to build ESM format output for libraries (npm library), you need to configure the following:

```js title="rspack.config.mjs"
export default {
  //...
  output: {
    module: true,
    chunkFormat: 'module',
    library: {
      type: 'modern-module',
    },
    chunkLoading: 'import',
    workerChunkLoading: 'import',
  },
  externalsType: 'module-import',
  optimization: {
    concatenateModules: true,
    avoidEntryIife: true,
    minimize: false,
  },
  experiments: {
    outputModule: true,
  },
};
```

You can check out this [rspack-examples](https://github.com/rstackjs/rstack-examples/tree/main/rspack/library-esm) ESM library example.

Building ESM output also requires handling various detailed issues, which are not listed exhaustively here. You can refer to the [ESM format related configurations in Rslib](https://github.com/web-infra-dev/rslib/blob/f727b18805767b99fb85ae67ebff959aa644536e/packages/core/src/config.ts), or use Rslib directly for out-of-the-box library building.

## Future plans for ESM output

Currently, Rspack's ESM support is still being improved. In certain use cases, you may encounter integration issues between ESM and other features. The main limitations include:

1. Lack of static analysis friendly code splitting support
2. Limited custom chunk splitting support in ESM format
3. Lack of module-level side effect information preservation, affecting tree-shaking accuracy
4. Re-exports of external modules (`export * from '...'`) cannot be properly preserved in ESM format

We are continuously improving Rspack's ESM support to provide a comprehensive solution that addresses existing issues and makes ESM usage more simple and intuitive, better embracing the modern JavaScript module system.

## Configuration checklist

Below are the main configuration options related to ESM and their descriptions, which are used when building both applications and libraries.

1. [output.module](/config/output.md#outputmodule): Set to `true` to generate ESM format output. When this option is enabled, it affects the following configurations:
   1. Affects [externalsType](/config/externals.md#externalstype) default value: When `output.module` is `true`, `externalsType` defaults to `'module-import'`
   2. Affects [output.filename](/config/output.md#outputfilename) default value: When `output.module` is `true`, the default filename is `'[name].mjs'` instead of `'[name].js'`
   3. Affects [output.chunkFilename](/config/output.md#outputchunkfilename) default value: When `output.module` is `true`, chunk filename defaults to `'[id].mjs'` instead of `'[id].js'`
   4. Affects [output.hotUpdateChunkFilename](/config/output.md#outputhotupdatechunkfilename) default value: When `output.module` is `true`, defaults to `'[id].[fullhash].hot-update.mjs'`
   5. Affects [output.hotUpdateMainFilename](/config/output.md#outputhotupdatemainfilename) default value: When `output.module` is `true`, defaults to `'[runtime].[fullhash].hot-update.json.mjs'`
   6. Affects [output.iife](/config/output.md#outputiife) default value: When `output.module` is `true`, `output.iife` defaults to `false`
   7. Affects [output.library.type](/config/output.md#outputlibrarytype) default value: When `output.module` is `true`, defaults to `'module'` instead of `'var'`
   8. Affects [output.scriptType](/config/output.md#outputscripttype) default value: When `output.module` is `true`, defaults to `'module'`
   9. Affects [output.environment.dynamicImport](/config/output.md#outputenvironmentdynamicimport) default value: Enabled when `output.module` is `true`
   10. Affects [output.environment.dynamicImportInWorker](/config/output.md#outputenvironmentdynamicimportinworker) default value: Enabled when `output.module` is `true`
   11. Affects [output.environment.module](/config/output.md#outputenvironmentmodule) default value: Enabled when `output.module` is `true`
   12. Affects Node.js related configuration defaults: In Node.js environment, when `output.module` is `true`, `__filename` and `__dirname` default to `'node-module'`
2. [output.chunkFormat](/config/output.md#outputchunkformat): Set to `'module'` to use ESM format.
3. [output.library.type](/config/output.md#outputlibrarytype): Set to `'modern-module'` for additional optimization of library ESM output format.
4. [output.chunkLoading](/config/output.md#outputchunkloading): Set to `'import'` to use ESM `import` for loading chunks.
5. [output.workerChunkLoading](/config/output.md#outputworkerchunkloading): Set to `'import'` to use ESM `import` for loading workers.
6. [optimization.avoidEntryIife](/config/optimization.md#optimizationavoidentryiife): In some cases, Rspack wraps ESM output in an IIFE, which breaks ESM's modular characteristics.
7. [experiments.outputModule](/config/experiments.md#experimentsoutputmodule): Enable the experimental feature required for output.module.
8. [HtmlWebpackPlugin.scriptLoading](/guide/tech/html.md#htmlwebpackplugin): Set to `'module'` to use ESM `<script type="module">` for loading `.mjs` modules.
