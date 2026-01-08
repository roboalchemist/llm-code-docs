# Source: https://github.com/vuejs/eslint-config-typescript

# @vue/eslint-config-typescript

ESLint configuration for Vue 3 + TypeScript projects.

## Package Information

- **Name**: @vue/eslint-config-typescript
- **Version**: 14.6.0
- **Description**: ESLint config for TypeScript + Vue.js projects
- **Repository**: git+https://github.com/vuejs/eslint-config-typescript.git
- **License**: MIT

## Overview

This package provides ESLint configuration specifically designed for Vue 3 + TypeScript projects. It is designed to be used by `create-vue` setups but can be used independently with some adaptations.

The configuration integrates with `typescript-eslint` for TypeScript-specific linting rules and works seamlessly with `eslint-plugin-vue` for Vue-specific rules.

## Installation

```sh
npm add --dev @vue/eslint-config-typescript
```

Requirements:
- TypeScript installed
- ESLint installed
- For flat config support, ESLint 9.0.0+

## Quick Start

### Minimal Setup

```js
// eslint.config.mjs
import pluginVue from 'eslint-plugin-vue'
import {
  defineConfigWithVueTs,
  vueTsConfigs,
} from '@vue/eslint-config-typescript'

export default defineConfigWithVueTs(
  pluginVue.configs['flat/essential'],
  vueTsConfigs.recommended,
)
```

This enables:
- Essential rules for Vue 3
- Recommended rules for TypeScript
- All `<script>` blocks in `.vue` files must be written in TypeScript

### Advanced Setup with configureVueProject

```js
// eslint.config.mjs
import pluginVue from 'eslint-plugin-vue'
import {
  defineConfigWithVueTs,
  vueTsConfigs,
  configureVueProject,
} from '@vue/eslint-config-typescript'

// Configure the Vue project
configureVueProject({
  // Parse TypeScript syntax in Vue templates (default: true)
  tsSyntaxInTemplates: true,

  // Specify script langs in .vue files (default: ['ts'])
  scriptLangs: ['ts'],

  // Override no-unsafe-* rules (default: true)
  allowComponentTypeUnsafety: true,

  // Root directory to resolve .vue files (default: process.cwd())
  rootDir: import.meta.dirname,
})

export default defineConfigWithVueTs(
  pluginVue.configs['flat/essential'],
  vueTsConfigs.base,
)
```

## Exported Utilities

### defineConfigWithVueTs

A utility function that modifies the given ESLint config to work with Vue.js + TypeScript.

- Type signature matches the `config` function from `typescript-eslint`
- Automatically handles Vue-specific TypeScript configuration
- Returns a proper flat config for ESLint 9.0.0+

### vueTsConfigs

Contains all shared configurations from `typescript-eslint` (in camelCase) and applies them to both `.vue` and TypeScript files.

Available configurations:
- `base` - Base configuration for custom rule setup
- `recommended` - Recommended rules for TypeScript
- `recommendedTypeChecked` - Recommended rules with type-aware linting
- `strict` - Strict TypeScript rules
- `strictTypeChecked` - Strict rules with type-aware linting

### configureVueProject(options)

Factory function for Vue-specific configuration. Options:

- `tsSyntaxInTemplates` (boolean, default: true) - Parse TypeScript syntax in Vue templates. Set to false for better performance if templates use only basic JavaScript.
- `scriptLangs` (array, default: ['ts']) - Script languages allowed in `.vue` files. Can include: 'ts', 'js', 'tsx', 'jsx'
- `allowComponentTypeUnsafety` (boolean, default: true) - Override `no-unsafe-*` rules for Vue component operations. Disable for strict type-checking in TSX-only projects.
- `rootDir` (string, default: process.cwd()) - Root directory for resolving `.vue` files. Important for monorepos.

## Linting with Type Information

Type-aware rules provide deeper code insights but are slower than syntax-only linting.

**Recommended approach:**
1. Start with `recommendedTypeChecked` configuration
2. Turn on/off individual rules as needed

```js
export default defineConfigWithVueTs(
  pluginVue.configs['flat/essential'],
  vueTsConfigs.recommendedTypeChecked
)
```

## Available Rules

See [@typescript-eslint/eslint-plugin documentation](https://typescript-eslint.io/rules/) for complete list of available rules and their configurations.

## Integration with Other Tools

### With Prettier

Compatible with `@vue/eslint-config-prettier` for code formatting.

### With JavaScript Standard Style

Use `@vue/eslint-config-standard-with-typescript` for StandardJS-style configurations.

## Important Notes

- **Not recommended for standalone use**: While this can be used independently, it's designed for `create-vue` setups
- **Requires eslint-plugin-vue**: Must be included in the same ESLint config
- **TypeScript in script blocks**: All `<script>` blocks must use TypeScript syntax (lang="ts")
- **Legacy .eslintrc format**: For older ESLint config format, use version 13 or earlier
- **Performance**: Set `tsSyntaxInTemplates: false` if templates don't use TypeScript syntax for faster linting

## Version History

This package follows Vue's release cycle. Version 14+ requires ESLint 9.0.0+ with flat config format.

For legacy .eslintrc support, refer to v13 and earlier documentation.

## Further Reading

- [TypeScript ESLint Rules](https://typescript-eslint.io/rules/)
- [TypeScript ESLint User Guide](https://typescript-eslint.io/getting-started/)
- [ESLint Plugin Vue](https://eslint.vuejs.org/)
- [Create Vue Documentation](https://github.com/vuejs/create-vue)

## Source Code Structure

The package exports from:
- `src/index.ts` - Main entry point with exported utilities
- `src/configs.ts` - Configuration definitions
- `src/createConfig.ts` - Config factory functions
- `src/utilities.ts` - Helper utilities
- `src/fpHelpers.ts` - Functional programming helpers
- `src/groupVueFiles.ts` - Vue file grouping utilities

## License

MIT - See LICENSE file for details
