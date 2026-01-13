# eslint-config-airbnb-typescript

Source: https://github.com/iamturns/eslint-config-airbnb-typescript

Enhances Airbnb's ESLint config with TypeScript support.

## Status

**NOTE: This repo has been archived.** After six years and reaching 2 million weekly downloads, the maintainer can no longer give this project the attention it deserves.

A huge thank you to all contributors along the way!

### Alternatives

- [`eslint-config-airbnb-extended`](https://www.npmjs.com/package/eslint-config-airbnb-extended)

---

## Overview

`eslint-config-airbnb-typescript` is an ESLint configuration that extends the popular Airbnb ESLint configuration to add comprehensive TypeScript support. It handles the complexity of linting TypeScript code by replacing or augmenting Airbnb's rules with TypeScript-aware equivalents from the `@typescript-eslint` plugin.

The package provides two configurations:

1. **Full config** (`airbnb-typescript`) - For React projects
2. **Base config** (`airbnb-typescript/base`) - For non-React projects

## Setup

### 1) Setup regular Airbnb config

Make sure you have the regular Airbnb config setup. If you are using React, use [`eslint-config-airbnb`](https://www.npmjs.com/package/eslint-config-airbnb), or if you aren't using React, use [`eslint-config-airbnb-base`](https://www.npmjs.com/package/eslint-config-airbnb-base).

### 2) Install dependencies (and peer dependencies)

```bash
npm install eslint-config-airbnb-typescript \
            @typescript-eslint/eslint-plugin@^7.0.0 \
            @typescript-eslint/parser@^7.0.0 \
            --save-dev
```

### 3) Configure ESLint

Within your ESLint config file:

```javascript
module.exports = {
  extends: [
    'airbnb',
    'airbnb-typescript'
  ]
};
```

If you don't need React support:

```javascript
module.exports = {
  extends: [
    'airbnb-base',
    'airbnb-typescript/base'
  ]
};
```

### 4) Configure the ESLint TypeScript parser

This config requires knowledge of your TypeScript config.

In your ESLint config, set [parserOptions.project](https://github.com/typescript-eslint/typescript-eslint/tree/master/packages/parser#parseroptionsproject) to the path of your `tsconfig.json`.

For example:

```javascript
module.exports = {
  extends: ['airbnb', 'airbnb-typescript'],
  parserOptions: {
    project: './tsconfig.json'
  }
};
```

### 5) Run ESLint

Open a terminal to the root of your project, and run the following command:

```bash
npx eslint . --ext .js,.jsx,.ts,.tsx
```

ESLint will lint all .js, .jsx, .ts, and .tsx files within the current folder, and output results to your terminal.

You can also get results in realtime inside most IDEs via a plugin.

## Configuration Structure

### Root Entry Points

- **`index.js`** - Main export for React projects
  - Extends shared TypeScript config
  - Adds React-specific settings for TypeScript files (.tsx)
  - Configures import resolver for TypeScript extensions

- **`base.js`** - For non-React projects
  - Extends shared TypeScript config
  - No React-specific rules

### Shared Configuration (`lib/shared.js`)

The core configuration that both entry points extend. This file:

1. **Configures the TypeScript ESLint plugin and parser**
   - `plugins: ['@typescript-eslint']`
   - `parser: '@typescript-eslint/parser'`

2. **Replaces Airbnb rules with TypeScript-aware versions**
   - Over 30 rules are replaced with `@typescript-eslint` equivalents
   - Maintains parity with Airbnb's linting philosophy while supporting TypeScript syntax

3. **Configures import resolution for TypeScript**
   - Adds `.ts`, `.tsx`, `.d.ts` to extension lists
   - Includes type definition packages in resolver configuration
   - Handles external type modules

4. **Disables conflicting rules for TypeScript files**
   - Disables ESLint rules that conflict with TypeScript compiler checks
   - Removes rules unnecessary in TypeScript (e.g., `no-undef`, `no-dupe-class-members`)

## Rules Replacements

The configuration replaces the following Airbnb rules with TypeScript-ESLint equivalents:

### Style Rules
- `brace-style` → `@typescript-eslint/brace-style`
- `comma-dangle` → `@typescript-eslint/comma-dangle`
- `comma-spacing` → `@typescript-eslint/comma-spacing`
- `func-call-spacing` → `@typescript-eslint/func-call-spacing`
- `indent` → `@typescript-eslint/indent`
- `keyword-spacing` → `@typescript-eslint/keyword-spacing`
- `lines-between-class-members` → `@typescript-eslint/lines-between-class-members`
- `no-array-constructor` → `@typescript-eslint/no-array-constructor`
- `quotes` → `@typescript-eslint/quotes`
- `semi` → `@typescript-eslint/semi`
- `space-before-blocks` → `@typescript-eslint/space-before-blocks`
- `space-before-function-paren` → `@typescript-eslint/space-before-function-paren`
- `space-infix-ops` → `@typescript-eslint/space-infix-ops`
- `object-curly-spacing` → `@typescript-eslint/object-curly-spacing`

### Naming & Variable Rules
- `camelcase` → `@typescript-eslint/naming-convention`
  - Supports `camelCase`, `PascalCase`, and `UPPER_CASE` for variables
  - Enforces `PascalCase` for types, interfaces, and enums
- `no-dupe-class-members` → `@typescript-eslint/no-dupe-class-members`
- `no-shadow` → `@typescript-eslint/no-shadow`
- `no-unused-vars` → `@typescript-eslint/no-unused-vars`
- `no-use-before-define` → `@typescript-eslint/no-use-before-define`
- `no-useless-constructor` → `@typescript-eslint/no-useless-constructor`

### Best Practices Rules
- `default-param-last` → `@typescript-eslint/default-param-last`
- `dot-notation` → `@typescript-eslint/dot-notation`
- `no-empty-function` → `@typescript-eslint/no-empty-function`
- `no-implied-eval` → `@typescript-eslint/no-implied-eval`
- `no-loop-func` → `@typescript-eslint/no-loop-func`
- `no-magic-numbers` → `@typescript-eslint/no-magic-numbers`
- `no-redeclare` → `@typescript-eslint/no-redeclare`
- `no-throw-literal` → `@typescript-eslint/no-throw-literal`
- `no-unused-expressions` → `@typescript-eslint/no-unused-expressions`
- `require-await` → `@typescript-eslint/require-await`
- `no-return-await` → `@typescript-eslint/return-await`

### Error Prevention Rules
- `no-extra-parens` → `@typescript-eslint/no-extra-parens`
- `no-extra-semi` → `@typescript-eslint/no-extra-semi`
- `no-loss-of-precision` → `@typescript-eslint/no-loss-of-precision`
- `no-new-func` → `@typescript-eslint/no-implied-eval`

## Import Resolution Configuration

The configuration extends Airbnb's import settings to support TypeScript:

```javascript
'import/resolver': {
  node: {
    extensions: ['.mjs', '.js', '.json', '.ts', '.d.ts']  // .tsx in React config
  }
}

'import/parsers': {
  '@typescript-eslint/parser': ['.ts', '.tsx', '.d.ts']
}

'import/extensions': ['.js', '.mjs', '.jsx', '.ts', '.tsx', '.d.ts']

'import/external-module-folders': ['node_modules', 'node_modules/@types']
```

## Frequently Asked Questions

### I get this error when running ESLint: "The file must be included in at least one of the projects provided"

This means you are attempting to lint a file that `tsconfig.json` doesn't include.

A common fix is to create a `tsconfig.eslint.json` file, which extends your `tsconfig.json` file and includes all files you are linting.

```json
{
  "extends": "./tsconfig.json",
  "include": ["src/**/*.ts", "src/**/*.js", "test/**/*.ts"]
}
```

Update your ESLint config file:

```javascript
module.exports = {
  extends: ['airbnb', 'airbnb-typescript'],
  parserOptions: {
    project: './tsconfig.eslint.json'
  }
};
```

### Why do I need the peer dependencies?

`@typescript-eslint/eslint-plugin` is a peer dependency due to a limitation within ESLint. See [ESLint issue #3458](https://github.com/eslint/eslint/issues/3458), [RFC](https://github.com/eslint/rfcs/tree/master/designs/2019-config-simplification), and [progress](https://github.com/eslint/eslint/issues/13481).

`@typescript-eslint/parser` is a peer dependency because the version number must match `@typescript-eslint/eslint-plugin`.

### I wish this config would support [...]

This config simply enhances Airbnb with TypeScript support. It's not a single config to cater for all TypeScript linting requirements. For additional functionality, alter your ESLint config file. For example:

```javascript
module.exports = {
  extends: [
    'airbnb',
    'airbnb-typescript',
    'airbnb/hooks',
    'plugin:@typescript-eslint/recommended-type-checked', // @typescript-eslint v6+
    'plugin:@typescript-eslint/stylistic-type-checked',   // @typescript-eslint v6+
  ],
};
```

### Why is `import/no-unresolved` disabled?

Two reasons:

1. It requires additional configuration, which may be different for monorepos, webpack usage, etc.
2. The rule offers little value in a TypeScript world, as the TypeScript compiler will catch these errors.

If you would like to enable this rule, then:

- Enable the rule within your config: `'import/no-unresolved': 'error'`
- Install and configure the TypeScript import resolver: [`eslint-import-resolver-typescript`](https://www.npmjs.com/package/eslint-import-resolver-typescript)

## Extended Configurations

Both the main and base configs can be extended with additional ESLint configurations:

```javascript
module.exports = {
  extends: [
    'airbnb',
    'airbnb-typescript',
    // Add other configs here
    'plugin:prettier/recommended'  // Example: Prettier integration
  ],
  parserOptions: {
    project: './tsconfig.json'
  }
};
```

## Package Details

- **Name:** eslint-config-airbnb-typescript
- **Latest Version:** 18.0.0
- **License:** MIT
- **Author:** Matt Turnbull (https://iamturns.com)
- **Repository:** https://github.com/iamturns/eslint-config-airbnb-typescript

## Dependencies

- `eslint-config-airbnb-base` ^15.0.0

## Peer Dependencies

- `@typescript-eslint/eslint-plugin` ^7.0.0
- `@typescript-eslint/parser` ^7.0.0
- `eslint` ^8.56.0

## Development

### Setup

1. Fork the repo
2. Install dependencies: `npm install`
3. Ensure everything is working: `npm run validate`

### Workflow

1. Create your feature branch: `git checkout -b my-new-feature`
2. Write code
3. Once complete, submit a pull request on GitHub

### Available Scripts

- `npm run lint` - Lint the codebase
- `npm run format` - Format code, package.json, and markdown files
- `npm run validate` - Run linting checks

## Contributing

See [DEVELOPING.md](https://github.com/iamturns/eslint-config-airbnb-typescript/blob/master/DEVELOPING.md) for development instructions.

To report bugs, please use the [GitHub issue tracker](https://github.com/iamturns/eslint-config-airbnb-typescript/issues).

## License

Open source licensed as MIT. See LICENSE file in the repository.

## Credits

Authored and maintained by Matt Turnbull ([iamturns.com](https://iamturns.com) / [@iamturns](https://twitter.com/iamturns))

A big thank you to all [contributors](https://github.com/iamturns/eslint-config-airbnb-typescript/graphs/contributors)!
