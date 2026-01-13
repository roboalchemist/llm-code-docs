# eslint-config-prettier

## Overview

**eslint-config-prettier** is an ESLint configuration that disables all ESLint rules that are unnecessary or might conflict with Prettier code formatting. This allows you to use your favorite shareable ESLint config without its stylistic choices interfering with Prettier.

- **Repository**: https://github.com/prettier/eslint-config-prettier
- **Package**: https://www.npmjs.com/package/eslint-config-prettier
- **License**: MIT
- **Author**: Simon Lydell

## Key Concepts

### Purpose

This config **only turns rules off** - it doesn't add any new rules. Therefore, it must be used together with some other ESLint configuration.

The main benefit is simplifying your configuration:
- Use any shareable ESLint config you prefer
- Add eslint-config-prettier to disable conflicting rules
- No more linter errors that Prettier will immediately fix

## Installation

### Package Managers

Choose your package manager:

```shell
# npm
npm i -D eslint-config-prettier

# yarn
yarn add -D eslint-config-prettier

# pnpm
pnpm add -D eslint-config-prettier

# bun
bun add -D eslint-config-prettier
```

### Configuration Setup

#### ESLintrc Format

Add `"prettier"` to the "extends" array in your `.eslintrc.*` file. **It must be last** to override other configs:

```json
{
  "extends": [
    "some-other-config-you-use",
    "prettier"
  ]
}
```

#### ESLint Flat Config Format

For `eslint.config.js` (flat config), import the config and place it **after** other configs you want to override:

```js
import someConfig from "some-other-config-you-use";
import eslintConfigPrettier from "eslint-config-prettier/flat";

export default [
  someConfig,
  eslintConfigPrettier,
];
```

## Supported Plugins

eslint-config-prettier automatically disables conflicting rules from these plugins:

- `@babel/eslint-plugin`
- `@stylistic/eslint-plugin`
- `@typescript-eslint/eslint-plugin`
- `eslint-plugin-babel`
- `eslint-plugin-flowtype`
- `eslint-plugin-react`
- `eslint-plugin-standard`
- `eslint-plugin-unicorn`
- `eslint-plugin-vue`

**Note**: As of version 8.0.0, you only need to extend `"prettier"` - it includes all plugins automatically. Older configs like `"prettier/react"` are no longer needed.

## CLI Helper Tool

The package includes a CLI tool to verify your configuration and find conflicting rules.

### Basic Usage

```bash
npx eslint-config-prettier path/to/main.js
```

Change `path/to/main.js` to an existing file in your project.

### Checking Multiple Files

For projects with different rules for different files:

```bash
npx eslint-config-prettier index.js test/index.js legacy/main.js
```

### Exit Codes

- **0**: No problems found
- **1**: Unexpected error
- **2**: Conflicting rules found

### Environment Variables

Control behavior with environment variables:

```bash
# Only use eslint.config.js (flat config)
ESLINT_USE_FLAT_CONFIG=true npx eslint-config-prettier path/to/file.js

# Only use eslintrc files
ESLINT_USE_FLAT_CONFIG=false npx eslint-config-prettier path/to/file.js

# Exclude deprecated rules
ESLINT_CONFIG_PRETTIER_NO_DEPRECATED=true npx eslint-config-prettier path/to/file.js
```

## Handling Conflicting Rules

### ESLintrc Conflicts

With eslintrc, the config can disable rules from extended configs, but not from your own "rules" section:

```json
{
  "extends": [
    "some-other-config-you-use",
    "prettier"
  ],
  "rules": {
    "indent": "error"  // This will still conflict!
  }
}
```

**Solution**: Remove conflicting rules from your "rules" section or disable them manually.

### Flat Config Conflicts

With flat config, you control the override order:

```js
import someConfig from "some-other-config-you-use";
import eslintConfigPrettier from "eslint-config-prettier/flat";

export default [
  someConfig,
  eslintConfigPrettier,
  {
    rules: {
      "indent": "error",  // This will still conflict!
    },
  },
];
```

**Solution**: Move eslint-config-prettier to the end (it will override):

```js
export default [
  someConfig,
  {
    rules: {
      "indent": "error",
    },
  },
  eslintConfigPrettier,  // Now it overrides
];
```

## Special Rules

Some rules can be enabled with eslint-config-prettier when used correctly. These require special attention:

### arrow-body-style and prefer-arrow-callback

**Warning**: These can cause issues with `eslint-plugin-prettier` and `--fix`.

Solutions:
1. Use `"plugin:prettier/recommended"` in extends (easiest)
2. Use `"prettier/prettier"` in extends
3. Manually disable them in your config

Safe to use if you run `eslint --fix` and `prettier --write` as separate steps.

### curly

Can be used if not using `"multi-line"` or `"multi-or-nest"` options:

```json
{
  "rules": {
    "curly": ["error", "all"]
  }
}
```

### lines-around-comment

Can be used with specific configuration:

```json
{
  "rules": {
    "lines-around-comment": [
      "error",
      {
        "beforeBlockComment": true,
        "afterBlockComment": true,
        "beforeLineComment": true,
        "afterLineComment": true,
        "allowBlockStart": true,
        "allowBlockEnd": true,
        "allowObjectStart": true,
        "allowObjectEnd": true,
        "allowArrayStart": true,
        "allowArrayEnd": true
      }
    ]
  }
}
```

### max-len

Can be enabled for extra strictness, but keep it in sync with Prettier's `printWidth`:

```json
{
  "rules": {
    "max-len": ["error", {"code": 80, "ignoreUrls": true}]
  }
}
```

### no-confusing-arrow

Can be used with `allowParens: false` option:

```json
{
  "rules": {
    "no-confusing-arrow": ["error", { "allowParens": false }]
  }
}
```

### no-mixed-operators

Requires refactoring to split complex expressions:

```json
{
  "rules": {
    "no-mixed-operators": "error"
  }
}
```

Example refactoring:
```js
// Before: may conflict
var foo = a + b * c;

// After: explicit separation
var bar = b * c;
var foo = a + bar;
```

### no-tabs

Can be used with `allowIndentationTabs: true`:

```json
{
  "rules": {
    "no-tabs": ["error", {"allowIndentationTabs": true}]
  }
}
```

### no-unexpected-multiline

Requires special attention - may need comments to disable rule on specific lines:

```json
{
  "rules": {
    "no-unexpected-multiline": "error"
  }
}
```

### quotes

Can enforce backticks or forbid unnecessary backticks with proper setup:

**Enforce backticks**:
```json
{
  "rules": {
    "quotes": ["error", "backtick"]
  }
}
```

**Forbid unnecessary backticks** (keep in sync with Prettier's `singleQuote`):
```json
{
  "rules": {
    "quotes": [
      "error",
      "single",
      { "avoidEscape": true, "allowTemplateLiterals": false }
    ]
  }
}
```

### unicorn/template-indent

Can be used with configuration to exclude templates Prettier handles:

```json
{
  "rules": {
    "unicorn/template-indent": [
      "error",
      {
        "tags": ["outdent", "dedent", "sql", "styled"],
        "functions": ["dedent", "stripIndent"],
        "selectors": [],
        "comments": ["indent"]
      }
    ]
  }
}
```

### vue/html-self-closing

Can be used with specific options:

```json
{
  "rules": {
    "vue/html-self-closing": [
      "error",
      {
        "html": {
          "void": "any"
        }
      }
    ]
  }
}
```

## Other Rules Worth Mentioning

### no-sequences

This rule doesn't conflict with Prettier, but Prettier auto-wraps sequences in parentheses. For better error catching, use:

```json
{
  "rules": {
    "no-restricted-syntax": ["error", "SequenceExpression"]
  }
}
```

With custom message:
```json
{
  "rules": {
    "no-restricted-syntax": [
      "error",
      {
        "selector": "SequenceExpression",
        "message": "The comma operator is confusing. Don't use it!"
      }
    ]
  }
}
```

## Flat Config Plugin Naming

With flat config, you control plugin names. Make sure to use standard names - eslint-config-prettier only knows the official names:

```js
import typescriptEslint from "@typescript-eslint/eslint-plugin";
import eslintConfigPrettier from "eslint-config-prettier/flat";

export default [
  {
    plugins: {
      // Use official name
      typescriptEslint: typescriptEslint,
      // Not: ts: typescriptEslint
    },
    rules: {
      // This works: @typescript-eslint/indent
      "typescriptEslint/indent": "error",
      // Not: ts/indent
    },
  },
  eslintConfigPrettier,
];
```

## Deprecated Rules

Some rules eslint-config-prettier disables may be deprecated or removed. To exclude deprecated rules, set the environment variable:

```bash
env ESLINT_CONFIG_PRETTIER_NO_DEPRECATED=true npx eslint-config-prettier index.js
```

## Common Workflows

### Setup with TypeScript

```js
import typescriptEslint from "@typescript-eslint/eslint-plugin";
import eslintConfigPrettier from "eslint-config-prettier/flat";

export default [
  {
    files: ["**/*.{ts,tsx}"],
    plugins: { typescriptEslint },
    rules: {
      // your typescript rules
    }
  },
  eslintConfigPrettier,
];
```

### Setup with React

```js
import react from "eslint-plugin-react";
import eslintConfigPrettier from "eslint-config-prettier/flat";

export default [
  {
    files: ["**/*.{js,jsx}"],
    plugins: { react },
    rules: {
      // your react rules
    }
  },
  eslintConfigPrettier,
];
```

### Combining with eslint-plugin-prettier

If using `eslint-plugin-prettier` to format code directly:

```js
import eslintPluginPrettier from "eslint-plugin-prettier";
import eslintConfigPrettier from "eslint-config-prettier/flat";

export default [
  {
    plugins: { prettier: eslintPluginPrettier },
    rules: {
      "prettier/prettier": "error",
    }
  },
  eslintConfigPrettier,
];
```

## Disabled Rules Reference

The config disables 150+ ESLint rules across ESLint core and supported plugins, including:

- Spacing rules: `indent`, `space-before-blocks`, `key-spacing`, etc.
- Semicolon rules: `semi`, `semi-spacing`
- Quote rules: `quotes`, `jsx-quotes`
- Line formatting: `max-len`, `linebreak-style`, `eol-last`
- Brace styles: `brace-style`, `arrow-parens`
- Object/array formatting: `object-curly-newline`, `array-bracket-spacing`
- Operator rules: `operator-linebreak`, `no-mixed-operators`
- And many more from @stylistic, @typescript-eslint, and other plugins

See the [full rules list](https://github.com/prettier/eslint-config-prettier/blob/main/index.js) in the source.

## Development and Contributing

To add support for a new plugin or report issues:

1. Create a test file in `test-lint/plugin-name.js`
2. Add rules to `index.js` and `eslint.base.config.mjs`
3. Update `README.md` with the plugin in supported list
4. Run `npm test` to verify

For more details, see the [GitHub repository](https://github.com/prettier/eslint-config-prettier).

## Related Resources

- **Prettier**: https://github.com/prettier/prettier
- **eslint-plugin-prettier**: https://github.com/prettier/eslint-plugin-prettier
- **ESLint Documentation**: https://eslint.org/docs/

## Version Information

- **Current Version**: 10.1.8
- **ESLint Requirement**: >=7.0.0
- **Maintained by**: JounQin, Simon Lydell

## License

MIT

## Source

This documentation is based on the official [eslint-config-prettier README](https://github.com/prettier/eslint-config-prettier) and source code from the repository.
