# eslint-config-standard-with-typescript

**Source:** https://github.com/mightyiam/eslint-config-standard-with-typescript
**npm Package:** https://www.npmjs.com/package/eslint-config-standard-with-typescript
**Current Name:** eslint-config-love

## Overview

This is an **ESLint shareable configuration** for TypeScript projects. It provides standard code linting rules based on the Standard JavaScript style guide with TypeScript support.

Note: The package was renamed from `eslint-config-standard-with-typescript` to `eslint-config-love` but is still accessible under the old name for backwards compatibility.

## Core Philosophy

The configuration follows these principles:

- **Safety at the cost of verbosity** - Prefers explicit, safe rules over convenience
- **Convention over arbitrary choice** - Uses standard conventions rather than arbitrary decisions
- **No formatting rules** - Doesn't handle code formatting (use a formatter like Prettier instead)
- **No redundant TypeScript rules** - Doesn't include rules already covered by strict TypeScript checking
- **No library/framework-specific rules** - Focuses on core JavaScript and TypeScript standards, not framework-specific linting

## Installation

### npm
```bash
npm install --save-dev eslint-config-standard-with-typescript typescript eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin
```

### Yarn
Note: Yarn does not automatically install peerDependencies. If using Yarn, install them manually:

```bash
yarn add --dev eslint-config-standard-with-typescript typescript eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin
```

## Dependencies

### Peer Dependencies
- `eslint` >= 9.35.0
- `typescript` (any version)

### Direct Dependencies
- `@typescript-eslint/utils` - Utilities for TypeScript ESLint rules
- `eslint-plugin-eslint-comments` - Lints ESLint comment directives
- `eslint-plugin-import` - Validates proper imports
- `eslint-plugin-n` - Validates Node.js compatibility
- `eslint-plugin-promise` - Enforces best practices for Promises
- `typescript-eslint` - TypeScript support for ESLint

## Configuration

### ESLint Flat Config Format (Recommended)

Using ES Modules:

```javascript
import love from 'eslint-config-standard-with-typescript'

export default [
  {
    ...love,
    files: ['**/*.js', '**/*.ts'],
  },
]
```

Using CommonJS:

```javascript
module.exports = (async function config() {
  const { default: love } = await import('eslint-config-standard-with-typescript')

  return [
    {
      ...love,
      files: ['**/*.js', '**/*.ts'],
    },
  ]
})()
```

## Configuration Options

### Parser Options

The configuration exported by this package automatically sets:
- `languageOptions.parserOptions.project = true`

This enables TypeScript-aware linting.

#### Additional Parser Options

You may customize additional parser options if needed:

```javascript
import love from 'eslint-config-standard-with-typescript'

export default [
  {
    ...love,
    files: ['**/*.js', '**/*.ts'],
    languageOptions: {
      parserOptions: {
        project: true,
        // Add other parser options here
        // See: https://typescript-eslint.io/packages/parser/#configuration
      },
    },
  },
]
```

For more information on available parser options, refer to the [TypeScript ESLint Parser Configuration](https://typescript-eslint.io/packages/parser/#configuration).

## Usage

### Command Line

```bash
npx eslint .
```

### With Configuration File

Create an `eslint.config.js` (or `eslint.config.mjs`) file in your project root with the configuration shown above, then run:

```bash
eslint .
```

## Disabling Rules

As with any ESLint configuration, ad-hoc rule disabling is expected. The strict nature of this configuration may require more frequent rule disabling than other configs.

### Best Practices for Disabling Rules

1. **Minimize scope** - Disable rules in the smallest scope possible
2. **Use comments** - Prefer `eslint-disable-*` comments over configuration when possible:

```javascript
// eslint-disable-next-line rule-name
const risky = somethingDangerous()

/* eslint-disable rule-name */
// code here
/* eslint-enable rule-name */
```

3. **File-level disabling** - Use configuration to disable rules for specific file patterns:

```javascript
import love from 'eslint-config-standard-with-typescript'

export default [
  {
    ...love,
    files: ['**/*.js', '**/*.ts'],
  },
  {
    files: ['test/**/*.ts'],
    rules: {
      'rule-name': 'off',
    },
  },
]
```

## Versioning

This package follows semantic versioning with a strict interpretation:

- **Major version bumps** - Any change that might require users to modify their code
  - This includes adding new rules, as users may need to disable them
  - Even rule additions are considered breaking changes
- **Minor/Patch versions** - Bug fixes and internal improvements

It is expected that most version bumps will be **major**.

## Contributing

### Contribution Process

1. **Discuss first** - Consider [opening a discussion](https://github.com/mightyiam/eslint-config-love/discussions) before implementing changes
2. **Run tests** - This project has tests; please run them before submitting
3. **Make accurate commits** - Each change should be its own pull request if it can stand on its own
4. **Use conventional commits** - Follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification

### Development Details

This project is developed primarily in a **remote mob programming format**. See [the mob schedule](https://mobusoperandi.com/mobs/love.html) for how to participate.

### Suggesting New Rules

A list of not yet considered rules is maintained in the test file. Contributions can:

1. Pick a rule from the "to consider" list
2. Evaluate if it's appropriate for this configuration
3. [Suggest it](https://github.com/mightyiam/eslint-config-love/discussions) with rationale

## Project Maintenance

### Sponsoring

To ensure the continuity of this project, consider [sponsoring the author](https://github.com/sponsors/mightyiam).

### Funding Options

- GitHub Sponsors: https://github.com/sponsors/mightyiam
- Wise (international transfer): https://wise.com/pay/me/shaharo

## License

MIT - See [LICENSE](https://github.com/mightyiam/eslint-config-standard-with-typescript/blob/main/LICENSE) for details.

## Related Projects

- **ts-standard** - A TypeScript style guide and CLI tool that uses the standard-engine combined with eslint-config-love
- **eslint-config-standard** - The base ESLint configuration without TypeScript support
- **@typescript-eslint** - Core TypeScript support for ESLint

## References

- [ESLint Shareable Configurations](https://eslint.org/docs/latest/use/core-concepts#shareable-configurations)
- [ESLint Configuration Files](https://eslint.org/docs/latest/use/configure/configuration-files)
- [TypeScript ESLint Parser Documentation](https://typescript-eslint.io/packages/parser/)
- [TypeScript ESLint Project Option](https://typescript-eslint.io/packages/parser/#project)
- [Standard JS](https://standardjs.com/)

## Changelog

For a complete list of changes, see [CHANGELOG.md](https://github.com/mightyiam/eslint-config-standard-with-typescript/blob/main/CHANGELOG.md) in the repository.

---

**Last Updated:** 2025-01-08
**Repository:** https://github.com/mightyiam/eslint-config-standard-with-typescript
