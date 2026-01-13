# Flint Configuration Guide

## Source: https://flint.fyi

## Overview

Flint's configuration system is designed with type safety and developer experience in mind. Unlike JSON-based configuration systems, Flint uses type-safe JavaScript configuration files that provide IDE autocomplete, type checking, and automatic edge case handling.

**Status**: Configuration system is currently under development as Flint is in early experimental stages.

## Configuration Philosophy

### Problems with Existing Configuration Systems

Traditional linters face configuration challenges:

**JSON Configuration**
- No IDE support or autocomplete
- No type validation
- Prone to user errors
- Limited flexibility
- Hard to compose

**JavaScript Configuration**
- More flexible but requires manual validation
- Error-prone with complex edge cases
- No standard structure
- Users must handle parsing and validation

### Flint's Approach

Type-safe JavaScript configuration:

```typescript
// flint.config.ts - Fully type-safe
export default {
  rules: {
    'rule-name': 'error',
    'another-rule': {
      severity: 'warn',
      option: true
    }
  },
  plugins: [
    '@flint.fyi/react',
    '@flint.fyi/performance'
  ]
}
```

**Benefits**:
- Full IDE autocomplete for all options
- Type validation at configuration time
- Cleaner, more readable syntax
- Composable and flexible
- Automatic edge case handling

## Configuration File

### File Location

Configuration is typically defined in the project root:
- `flint.config.ts` - TypeScript (recommended)
- `flint.config.js` - JavaScript (if TS not available)
- `flint.config.mts` - ES modules

### Minimal Configuration

```typescript
// flint.config.ts
export default {}
```

This uses Flint's defaults:
- All core plugins enabled
- Recommended rule settings
- Standard output formatting

## Core Configuration Options

### Rules Configuration

#### Disabling a Rule

```typescript
export default {
  rules: {
    'rule-name': 'off'
  }
}
```

#### Changing Severity

```typescript
export default {
  rules: {
    'rule-name': 'warn',  // 'error' or 'warn'
  }
}
```

#### Rule-Specific Options

```typescript
export default {
  rules: {
    'rule-name': {
      severity: 'error',
      // Rule-specific configuration
      option1: true,
      option2: false,
      option3: 'value'
    }
  }
}
```

### Plugins Configuration

#### Including Plugins

```typescript
export default {
  plugins: [
    '@flint.fyi/react',
    '@flint.fyi/performance',
    '@flint.fyi/node'
  ]
}
```

#### Plugin-Specific Configuration

```typescript
export default {
  plugins: [
    {
      name: '@flint.fyi/react',
      config: {
        hookRulesOfDeps: true,
        reactVersion: '18'
      }
    }
  ]
}
```

## File Patterns and Overrides

### Specifying File Patterns

```typescript
export default {
  // Global rules apply to all files
  rules: {
    'rule-1': 'error'
  },

  // Override rules for specific file patterns
  overrides: [
    {
      files: ['**/*.test.ts', '**/*.spec.ts'],
      rules: {
        'no-console': 'off'
      }
    },
    {
      files: ['src/browser/**/*'],
      plugins: ['@flint.fyi/browser']
    }
  ]
}
```

### File Pattern Syntax

Supports glob patterns:
- `**/*.ts` - All TypeScript files
- `src/**/*` - All files in src directory
- `*.json` - JSON files in root
- `{*.ts,*.tsx}` - Multiple extensions

## Type-Safe Configuration Benefits

### IDE Support

Modern IDEs provide:
- **Autocomplete**: Type hints for all configuration options
- **Type Checking**: Errors for invalid configurations
- **Documentation**: Built-in help and descriptions
- **Quick Navigation**: Jump to definitions and references

### Configuration Validation

The TypeScript compiler validates:
- Correct option names
- Valid values for options
- Type compatibility
- Missing required fields

### Development Experience

Benefits during development:
- Immediate feedback on configuration errors
- Less time debugging configuration issues
- Self-documenting configuration
- Easy refactoring with IDE support

## Advanced Configuration

### Merging Configurations

```typescript
import baseConfig from './flint.config.base'

export default {
  ...baseConfig,
  rules: {
    ...baseConfig.rules,
    'custom-rule': 'error'
  }
}
```

### Conditional Configuration

```typescript
const isDevelopment = process.env.NODE_ENV === 'development'

export default {
  rules: {
    'rule-name': isDevelopment ? 'warn' : 'error'
  }
}
```

### Environment-Specific Configuration

```typescript
export default {
  rules: {
    // Common rules
    'no-console': 'warn'
  },
  overrides: [
    {
      files: ['src/**/*.ts'],
      rules: {
        'strict-mode': 'error'
      }
    },
    {
      files: ['scripts/**/*.ts'],
      rules: {
        'strict-mode': 'off'
      }
    }
  ]
}
```

## Plugin Configuration

### Core Plugins

Core plugins are always available and can be configured:

```typescript
export default {
  rules: {
    // Configure core rules
    'json-valid': 'error',
    'markdown-valid': 'error',
    'yaml-valid': 'error'
  }
}
```

### Adding Focused Plugins

```typescript
export default {
  plugins: [
    '@flint.fyi/react',      // React best practices
    '@flint.fyi/node',       // Node.js best practices
    '@flint.fyi/performance' // Performance rules
  ]
}
```

### Adding Incubator Plugins

```typescript
export default {
  plugins: [
    '@flint.fyi/next',  // Next.js specific
    '@flint.fyi/vitest' // Vitest testing
  ]
}
```

## Disable Comments

### File-Level Disables

Disable a rule for an entire file:

```typescript
// @flint-disable rule-name
// File content...
```

### Line-Level Disables

Disable a rule for a single line:

```typescript
const x: any = 'something'; // @flint-disable-line rule-name
```

Disable multiple rules:

```typescript
// @flint-disable rule-1 rule-2 rule-3
// Multiple lines can be affected...
```

## Formatting and Output

### Output Options

```typescript
export default {
  output: {
    format: 'json' | 'text' | 'html',
    // ... more options
  }
}
```

### Interactive Mode

```typescript
export default {
  output: {
    interactive: true  // Allow interactive fixing
  }
}
```

## Performance Configuration

### Caching

Type-aware caching is automatically enabled:

```typescript
export default {
  cache: {
    enabled: true,        // Enable caching (default)
    directory: '.flint'   // Cache directory
  }
}
```

### Parallel Processing

```typescript
export default {
  performance: {
    workers: 4  // Number of parallel workers
  }
}
```

## Extending Configurations

### Shareable Configurations

Create a base configuration to share across projects:

```typescript
// shared-flint-config.ts
export default {
  rules: {
    'no-console': 'warn',
    'no-debugger': 'error'
  },
  plugins: [
    '@flint.fyi/react'
  ]
}
```

### Using Shared Configurations

```typescript
import baseConfig from '@company/flint-config'

export default {
  ...baseConfig,
  rules: {
    ...baseConfig.rules,
    'custom-rule': 'error'
  }
}
```

## Migration from ESLint

### Similar Concepts

| ESLint | Flint |
|--------|-------|
| `.eslintrc.json` | `flint.config.ts` |
| `rules` | `rules` |
| `extends` | `...config` or imports |
| `overrides` | `overrides` |
| `plugins` | `plugins` |

### Key Differences

1. **Type Safety**: Flint configs are type-checked
2. **Language**: TypeScript instead of JSON
3. **Syntax**: No extends, use JavaScript imports instead
4. **Plugins**: Different plugin naming and interface
5. **Rules**: Different rule names and options

## Troubleshooting Configuration

### Rule Not Being Applied

1. Check rule is enabled in configuration
2. Verify file matches pattern in `overrides`
3. Check plugin is listed in `plugins`
4. Confirm rule name is correct

### Conflicting Rules

If rules conflict:
1. Disable one rule for the file type
2. Use `overrides` for different settings
3. Check plugin documentation for interactions

### Configuration Not Loaded

Ensure:
1. File is named `flint.config.ts` (or `.js`)
2. File is in project root
3. File has `export default` statement
4. TypeScript syntax is valid

## Best Practices

### Configuration Organization

1. **Keep it simple**: Start with defaults, add only needed config
2. **Use TypeScript**: Take advantage of type safety
3. **Document complex rules**: Add comments for non-obvious settings
4. **Organize overrides**: Group related overrides together
5. **Version control**: Include config in git

### Rule Configuration Strategy

1. **Start conservative**: More rules can be too strict
2. **Gradually adopt**: Enable rules as team agrees on standards
3. **Use warnings first**: Ease into errors for new rules
4. **Per-file customization**: Use overrides for special cases
5. **Team alignment**: Discuss rules with team before enforcing

### Plugin Selection

1. **Core first**: Enable core rules matching your languages
2. **Pick relevant plugins**: Only include what your project uses
3. **Avoid plugin overload**: Too many rules can be overwhelming
4. **Incubator usage**: Try incubator plugins for emerging tech

## Configuration in CI/CD

### GitHub Actions Example

```yaml
name: Lint
on: [push, pull_request]
jobs:
  flint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: 18
      - run: npm install
      - run: npx flint
```

### Pre-commit Hook

```bash
#!/bin/bash
# .husky/pre-commit
npx flint --staged
```

## Environment Variables

Configuration can use environment variables:

```typescript
export default {
  rules: {
    'rule-name': process.env.STRICT_MODE ? 'error' : 'warn'
  }
}
```

Set before running flint:

```bash
STRICT_MODE=true flint
```

## See Also

- [Rules System](./rules.md)
- [Architecture Overview](./architecture.md)
- [Getting Started](./index.md)

---

**Note**: Configuration system is under active development. Details may change as Flint matures.
