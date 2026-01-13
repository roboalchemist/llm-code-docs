# Source: https://github.com/vuejs/eslint-config-typescript

# API Reference

## defineConfigWithVueTs

**Type**: Function

**Signature**:
```typescript
export function defineConfigWithVueTs(
  ...configs: FlatConfig[]
): FlatConfig[]
```

**Description**: Transforms ESLint flat configurations to work with Vue 3 + TypeScript.

**Parameters**:
- Accepts any number of ESLint flat config objects

**Returns**: Modified flat config array optimized for Vue 3 + TypeScript

**Example**:
```javascript
import pluginVue from 'eslint-plugin-vue'
import { defineConfigWithVueTs, vueTsConfigs } from '@vue/eslint-config-typescript'

export default defineConfigWithVueTs(
  pluginVue.configs['flat/essential'],
  vueTsConfigs.recommended,
)
```

## vueTsConfigs

**Type**: Object with config properties

**Available Configs**:

### vueTsConfigs.base
- Type-aware: No
- Use case: Starting point for custom rule configuration

### vueTsConfigs.recommended
- Type-aware: No
- Use case: Standard recommended setup without type checking

### vueTsConfigs.recommendedTypeChecked
- Type-aware: Yes (with type checking enabled)
- Use case: Recommended setup with advanced type-aware rules
- Performance impact: Slower (requires type-checking)

### vueTsConfigs.strict
- Type-aware: No
- Use case: Strict rules without type-aware linting
- Performance: Faster than type-checked versions

### vueTsConfigs.strictTypeChecked
- Type-aware: Yes (with type checking enabled)
- Use case: Maximum strictness with type-aware rules
- Performance impact: Slowest (requires type-checking)

**Example**:
```javascript
export default defineConfigWithVueTs(
  pluginVue.configs['flat/essential'],
  vueTsConfigs.recommendedTypeChecked,
)
```

## configureVueProject(options)

**Type**: Function

**Signature**:
```typescript
export function configureVueProject(options?: {
  tsSyntaxInTemplates?: boolean
  scriptLangs?: string[]
  allowComponentTypeUnsafety?: boolean
  rootDir?: string
}): void
```

**Description**: Configures Vue project-specific ESLint settings.

**Options**:

### tsSyntaxInTemplates
- **Type**: boolean
- **Default**: true
- **Description**: Parse TypeScript syntax in Vue template expressions
- **Performance**: Set to false for ~20-30% faster linting if templates don't use TypeScript

### scriptLangs
- **Type**: string[]
- **Default**: ['ts']
- **Allowed values**: 'ts', 'js', 'tsx', 'jsx'
- **Note**: Only 'ts' is recommended; other options may conflict with type-aware rules

### allowComponentTypeUnsafety
- **Type**: boolean
- **Default**: true
- **Description**: Relax `no-unsafe-*` rules for Vue component type operations
- **Use case**: Keep true for Vue SFC projects; set false for TSX-only projects with strict typing

### rootDir
- **Type**: string
- **Default**: process.cwd()
- **Description**: Root directory for resolving .vue files
- **Important**: Set this for monorepo setups to properly resolve all .vue files

**Example**:
```javascript
import { configureVueProject } from '@vue/eslint-config-typescript'

configureVueProject({
  tsSyntaxInTemplates: true,
  scriptLangs: ['ts'],
  allowComponentTypeUnsafety: true,
  rootDir: import.meta.dirname,
})
```

## Configuration Properties

ESLint flat config objects have:

- `files` - Glob patterns for files to apply rules
- `rules` - Rule name to severity mapping
- `languageOptions` - Parser, globals, sourceType settings
- `plugins` - ESLint plugins

When using these utilities, they automatically configure:
- Vue file parsing
- TypeScript parser setup
- TypeScript ESLint plugin
- Vue ESLint plugin integration
