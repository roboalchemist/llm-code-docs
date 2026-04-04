# ESLint Import Resolver TypeScript

**Source:** https://github.com/import-js/eslint-import-resolver-typescript

TypeScript module path resolution for ESLint import linting. This resolver adds TypeScript support to the `eslint-plugin-import` plugin, enabling proper resolution of TypeScript paths, aliases, and module imports.

## Overview

eslint-import-resolver-typescript is a resolver for `eslint-plugin-import`(-x) that adds TypeScript support. It is not an ESLint plugin itself, but rather an extension that enhances the import resolution capabilities of eslint-plugin-import.

**Current Version:** 4.4.4
**License:** ISC
**Repository:** https://github.com/import-js/eslint-import-resolver-typescript

## Key Features

- Import/require files with extensions: `.cts`, `.mts`, `.ts`, `.tsx`, `.d.cts`, `.d.mts`, `.d.ts`
- Use `paths` defined in `tsconfig.json` for module resolution
- Prefer resolving `@types/*` definitions over plain `.js`/`.jsx` files
- Multiple tsconfigs support, useful for monorepos
- `imports/exports` fields support in `package.json`
- Full TypeScript path alias resolution
- Support for both ESLint flat config and legacy `.eslintrc` format
- Bun runtime support

## Installation

### For eslint-plugin-import-x

```sh
# npm
npm i -D eslint-plugin-import-x eslint-import-resolver-typescript

# pnpm
pnpm i -D eslint-plugin-import-x eslint-import-resolver-typescript

# yarn
yarn add -D eslint-plugin-import-x eslint-import-resolver-typescript

# bun
bun add -d eslint-plugin-import-x eslint-import-resolver-typescript
```

### For eslint-plugin-import

```sh
# npm
npm i -D eslint-plugin-import eslint-import-resolver-typescript

# pnpm
pnpm i -D eslint-plugin-import eslint-import-resolver-typescript

# yarn
yarn add -D eslint-plugin-import eslint-import-resolver-typescript

# bun
bun add -d eslint-plugin-import eslint-import-resolver-typescript
```

## Configuration

### ESLint Flat Config (eslint.config.js)

If you are using `eslint-plugin-import-x@>=4.5.0`, you can use `import`/`require` to reference eslint-import-resolver-typescript directly:

```js
// eslint.config.js (CommonJS is also supported)
import { createTypeScriptImportResolver } from 'eslint-import-resolver-typescript'

export default [
  {
    settings: {
      'import-x/resolver-next': [
        createTypeScriptImportResolver({
          alwaysTryTypes: true, // Always try to resolve types under `<root>@types` directory

          bun: true, // Resolve Bun modules

          // Choose from one of the "project" configs below or omit to use
          // <root>/tsconfig.json or <root>/jsconfig.json by default

          // Use <root>/path/to/folder/tsconfig.json or <root>/path/to/folder/jsconfig.json
          project: 'path/to/folder',

          // Multiple tsconfigs/jsconfigs (Useful for monorepos,
          // but discouraged in favor of `references` supported)

          // Use a glob pattern
          project: 'packages/*/{ts,js}config.json',

          // Use an array
          project: [
            'packages/module-a/tsconfig.json',
            'packages/module-b/jsconfig.json',
          ],

          // Use an array of glob patterns
          project: [
            'packages/*/tsconfig.json',
            'other-packages/*/jsconfig.json',
          ],
        }),
      ],
    },
  },
]
```

For older versions of `eslint-plugin-import-x` or `eslint-plugin-import`, use string configuration:

```js
// eslint.config.js (CommonJS is also supported)
export default [
  {
    settings: {
      'import/resolver': {
        typescript: {
          alwaysTryTypes: true,
          bun: true,

          // Project configuration options
          project: 'path/to/folder',
          // or
          project: 'packages/*/{ts,js}config.json',
          // or
          project: [
            'packages/module-a/tsconfig.json',
            'packages/module-b/jsconfig.json',
          ],
        },
      },
    },
  },
]
```

### Legacy .eslintrc Format

Add the following to your `.eslintrc` configuration:

```jsonc
{
  "plugins": ["import"],
  "rules": {
    // Turn on errors for missing imports
    "import/no-unresolved": "error"
  },
  "settings": {
    "import/parsers": {
      "@typescript-eslint/parser": [".ts", ".tsx"]
    },
    "import/resolver": {
      "typescript": {
        "alwaysTryTypes": true,
        "bun": true,

        // Choose one of these project configurations
        "project": "path/to/folder",
        // or
        "project": "packages/*/{ts,js}config.json",
        // or
        "project": [
          "packages/module-a/tsconfig.json",
          "packages/module-b/jsconfig.json"
        ]
      }
    }
  }
}
```

## Configuration Options

### Core Options

#### `alwaysTryTypes`

**Type:** `boolean`
**Default:** `false`

Always try to resolve types under `<root>@types` directory even if it doesn't contain any source code, like `@types/unist`.

#### `bun`

**Type:** `boolean`
**Default:** `false`

Resolve Bun built-in modules. Bun provides built-in modules such as `bun:test`, which are not resolved by default.

Enable Bun module resolution by choosing one of:
- Set the `bun: true` option in configuration
- Run ESLint with `bun --bun eslint`
- Configure `run.bun` in `bunfig.toml`

#### `project`

**Type:** `string | string[]`
**Default:** Auto-detect `<root>/tsconfig.json` or `<root>/jsconfig.json`

Specify which tsconfig/jsconfig files to use for module resolution.

Supports:
- Single file path: `path/to/folder`
- Glob pattern: `packages/*/{ts,js}config.json`
- Array of paths: `['path1/tsconfig.json', 'path2/tsconfig.json']`
- Array of glob patterns: `['packages/*/tsconfig.json', 'other/*/jsconfig.json']`

### Options from unrs-resolver

The resolver passes through options from [unrs-resolver](https://github.com/unrs/unrs-resolver).

#### `conditionNames`

**Default:**

```json
[
  "types",
  "import",
  "esm2020",
  "es2020",
  "es2015",
  "require",
  "node",
  "node-addons",
  "browser",
  "default"
]
```

Defines the order of export conditions to check in package.json exports field.

#### `extensions`

**Default:**

```json
[
  ".ts",
  ".tsx",
  ".d.ts",
  ".js",
  ".jsx",
  ".json",
  ".node"
]
```

File extensions to resolve. Note: `.mts`, `.cts`, `.d.mts`, `.d.cts`, `.mjs`, `.cjs` are not included because they must be used explicitly.

#### `extensionAlias`

**Default:**

```json
{
  ".js": [".ts", ".tsx", ".d.ts", ".js"],
  ".ts": [".ts", ".d.ts", ".js"],
  ".jsx": [".tsx", ".d.ts", ".jsx"],
  ".tsx": [".tsx", ".d.ts", ".jsx", ".js"],
  ".cjs": [".cts", ".d.cts", ".cjs"],
  ".cts": [".cts", ".d.cts", ".cjs"],
  ".mjs": [".mts", ".d.mts", ".mjs"],
  ".mts": [".mts", ".d.mts", ".mjs"]
}
```

Defines how to resolve imports when source file extension differs from target extension.

#### `mainFields`

**Default:**

```json
[
  "types",
  "typings",
  "fesm2020",
  "fesm2015",
  "esm2020",
  "es2020",
  "module",
  "jsnext:main",
  "main"
]
```

Order of package.json fields to check for module entry points.

### Default Exports

You can reuse the default configurations by importing:

```js
import {
  defaultConditionNames,
  defaultExtensions,
  defaultExtensionAlias,
  defaultMainFields
} from 'eslint-import-resolver-typescript'
```

## Type Definition Resolution

After version 2.0.0, `.d.ts` files take higher priority than normal `.js`/`.jsx` files when resolving `node_modules` packages. This favors `@types/*` definitions or package-provided types.

## Important Notes

### Rules Compatibility

If you're facing issues with the `import/default` or `import/named` rules from eslint-plugin-import, these are expected behaviors on the plugin side, not resolver issues. Refer to:
- [eslint-plugin-import#1525](https://github.com/import-js/eslint-plugin-import/issues/1525)
- [import-js/eslint-import-resolver-typescript#31](https://github.com/import-js/eslint-import-resolver-typescript/issues/31)

## Node.js Compatibility

- **Required:** Node.js ^16.17.0 || >=18.6.0
- **Package Manager:** Yarn 4.9.2+

## Contributing

To contribute:

1. Ensure changes are covered by tests
2. Run `yarn test` without failures
3. Run `yarn lint` without conflicts
4. Match the project's type-coverage settings: `yarn type-coverage`

The project uses GitHub Actions to run these checks on all PRs.

## Dependencies

### Direct Dependencies

- `debug` - Debugging utility
- `eslint-import-context` - ESLint import context handling
- `get-tsconfig` - TypeScript config detection
- `is-bun-module` - Bun module detection
- `stable-hash-x` - Stable hashing for caching
- `tinyglobby` - Glob pattern matching
- `unrs-resolver` - Universal module resolver

### Peer Dependencies

- `eslint` - Required for ESLint integration
- `eslint-plugin-import` - Optional, for eslint-plugin-import support
- `eslint-plugin-import-x` - Optional, for eslint-plugin-import-x support

## Development Scripts

```bash
# Build the project
yarn build

# Run tests
yarn test

# Run linting
yarn lint

# Format code
yarn format

# Check type coverage
yarn typecov

# Release new version
yarn release
```

## Related Projects

- [eslint-plugin-import](https://github.com/import-js/eslint-plugin-import) - ESLint plugin for import/export syntax validation
- [eslint-plugin-import-x](https://github.com/un-ts/eslint-plugin-import-x) - Faster fork of eslint-plugin-import
- [unrs-resolver](https://github.com/unrs/unrs-resolver) - Universal module resolver
- [@typescript-eslint/parser](https://github.com/typescript-eslint/typescript-eslint) - TypeScript parser for ESLint

## Funding

Support the project:
- [Open Collective](https://opencollective.com/eslint-import-resolver-typescript)

## License

[ISC License](./LICENSE)

## Changelog

Detailed changes for each release are documented in [CHANGELOG.md](https://github.com/import-js/eslint-import-resolver-typescript/blob/master/CHANGELOG.md).
