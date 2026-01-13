# Flint Rules System

## Source: https://flint.fyi/rules

## Overview

Flint organizes linting rules into a tiered system designed to support projects of all sizes and specializations. This structure provides:

- **Accessibility**: Clear categorization helps developers find relevant rules
- **Flexibility**: Projects can adopt just the rules they need
- **Maintainability**: Different tiers have appropriate governance models
- **Growth**: Incubator plugins graduate to focused plugins as they mature

## Rule Tiers

### 1. Core Plugins

**Purpose**: Universal rules applicable to any project

Rules included with Flint by default. Maintained by core team with high quality standards.

#### Core Plugin Categories

##### JSON Plugin
- Validates JSON file structure
- Detects common JSON syntax errors
- Enforces formatting conventions
- File types: `.json`

##### Markdown Plugin
- Validates Markdown syntax
- Enforces consistent formatting
- Detects common Markdown issues
- File types: `.md`, `.markdown`

##### PackageJSON Plugin
- Validates `package.json` structure
- Enforces field completeness
- Detects missing required fields
- Checks dependency consistency
- File type: `package.json`

##### TypeScript/JavaScript Plugin
- Detects common programming mistakes
- Enforces code style conventions
- Identifies performance issues
- Provides type-aware rules
- File types: `.ts`, `.tsx`, `.js`, `.jsx`
- **Type-Aware**: Uses TypeScript compiler API for semantic analysis

##### YAML Plugin
- Validates YAML syntax
- Enforces formatting standards
- Detects common YAML mistakes
- File types: `.yaml`, `.yml`

### 2. Focused Plugins

**Purpose**: Rules for large areas or specific code styles applicable to many projects

Plugins available as separate packages under `@flint.fyi/`. Maintained by dedicated teams with focused expertise.

#### Available Focused Plugins

**@flint.fyi/browser**
- Browser API best practices
- DOM manipulation patterns
- Web platform compatibility
- Recommended for browser-focused JavaScript/TypeScript

**@flint.fyi/flint**
- Flint-specific best practices
- Rules for working with Flint itself
- Plugin development guidelines
- Recommended for Flint contributors and plugin authors

**@flint.fyi/jsx**
- JSX syntax and patterns
- React component best practices
- JSX-specific performance issues
- Recommended for React projects

**@flint.fyi/node**
- Node.js API best practices
- Server-side patterns
- Node.js compatibility
- Recommended for Node.js projects

**@flint.fyi/performance**
- Performance anti-patterns
- Optimization opportunities
- Bundle size considerations
- Recommended for performance-critical projects

**@flint.fyi/sorting**
- Consistent import ordering
- Object key organization
- List sorting conventions
- Recommended for projects with formatting standards

**@flint.fyi/spelling**
- Spell checking for comments and strings
- Terminology consistency
- Documentation quality
- Recommended for projects with high documentation standards

### 3. Incubator Plugins

**Purpose**: Area-specific plugins that should exist under community governance

Plugins available as separate packages under `@flint.fyi/`. Maintained by community contributors, designed to eventually graduate to focused plugins.

#### Available Incubator Plugins

**@flint.fyi/astro**
- Astro-specific best practices
- Component patterns
- Performance optimization
- For Astro projects

**@flint.fyi/next**
- Next.js specific rules
- App Router conventions
- Next.js best practices
- For Next.js projects

**@flint.fyi/nuxt**
- Nuxt.js specific rules
- Composition API patterns
- Nuxt conventions
- For Nuxt projects

**@flint.fyi/react**
- React-specific best practices
- Hooks rules
- Component patterns
- For React projects

**@flint.fyi/solidjs**
- Solid.js specific rules
- Reactivity patterns
- Component best practices
- For SolidJS projects

**@flint.fyi/vitest**
- Vitest testing best practices
- Test structure conventions
- Assertion patterns
- For Vitest test files

**@flint.fyi/vue**
- Vue.js specific rules
- Single-file component patterns
- Vue conventions
- For Vue projects

## Rule Reference

### Rule Properties

Each rule in Flint has the following properties:

- **Name**: Unique identifier for the rule (e.g., `no-unused-variables`)
- **Description**: Human-readable explanation of what the rule checks
- **Severity**: Error level - `error` (blocks build) or `warning` (reported but non-blocking)
- **Type**: Detection category (code quality, performance, style, etc.)
- **Fixable**: Whether the rule can automatically fix issues
- **Configuration**: Optional settings to customize rule behavior
- **Documentation**: Detailed explanation and examples

### Rule Coverage

Flint maintains a reference of over 1,000 popular linting rules from various sources. The project uses this reference to ensure comprehensive coverage across:

- General JavaScript/TypeScript rules
- Framework-specific best practices
- Performance and optimization rules
- Security and vulnerability detection
- Code style and formatting rules
- Documentation and comment quality

## How Rules Work

### Rule Execution Flow

```
Source Code File
    ↓
Parser (TypeScript AST)
    ↓
Type Checker (if applicable)
    ↓
Rule Engine
    ├─→ Matches rule conditions?
    ├─→ Rule callback triggered
    ├─→ Reports violation(s)
    └─→ Generates fix(es) if applicable
    ↓
Formatted Results
```

### Type-Aware Rules

Rules in the TypeScript/JavaScript core plugin have access to:
- Full TypeScript type information
- Semantic meaning of code, not just syntax
- Type relationships and flow
- Better detection of logical issues

Example: A rule can understand that a function parameter has type `string` and flag attempts to use it as a number, not just detect syntax errors.

### Configurable Rules

Many rules support configuration options:

```typescript
// Example: configure rule behavior
rules: {
  'no-console': {
    severity: 'warn',
    allowedMethods: ['error', 'warn']
  }
}
```

## Rule Configuration

### Per-Rule Configuration

Rules can be configured individually in `flint.config.ts`:

```typescript
export default {
  rules: {
    'rule-name': {
      severity: 'error' | 'warning',
      // rule-specific options...
    }
  }
}
```

### Plugin-Level Configuration

Plugins can be configured with settings:

```typescript
export default {
  plugins: [
    {
      plugin: '@flint.fyi/performance',
      config: {
        // plugin-specific options...
      }
    }
  ]
}
```

### Enabling/Disabling Rules

Rules can be enabled, disabled, or configured per file:

```typescript
// Disable specific rule for this file
// @flint-disable rule-name

code here
```

## Rule Categories

### Code Quality Rules
- Detect common programming mistakes
- Find potential bugs
- Identify unreachable code
- Flag logical errors

Examples: unused variables, unreachable code, type mismatches

### Performance Rules
- Identify performance anti-patterns
- Suggest optimization opportunities
- Flag inefficient algorithms
- Warn about bundle size impact

Examples: unnecessary re-renders, inefficient DOM access

### Style Rules
- Enforce consistent code style
- Maintain readability conventions
- Ensure formatting consistency
- Promote team standards

Examples: naming conventions, indentation, quotes

### Security Rules
- Detect security vulnerabilities
- Prevent unsafe patterns
- Identify injection risks
- Flag potential exploits

Examples: unsafe DOM operations, eval usage

### Documentation Rules
- Check comment quality
- Enforce documentation standards
- Validate JSDoc comments
- Ensure code clarity

Examples: missing documentation, typos in comments

## Best Practices for Rules

### For Users

1. **Start with core rules**: These are most universally applicable
2. **Add focused plugins for your use case**: Browser, Node, React, etc.
3. **Consider incubator plugins**: For framework-specific rules
4. **Customize as needed**: Adjust severity and configuration
5. **Keep rules focused**: Avoid enabling too many rules at once

### For Plugin Authors

1. **Follow consistent patterns**: Match Flint's rule structure
2. **Document thoroughly**: Include examples and rationale
3. **Provide configuration options**: Allow customization
4. **Keep rules focused**: One concern per rule
5. **Include fixes when possible**: Automate remediation where safe

## Rule Composition

Rules can depend on or build upon each other:

- Core rules provide baseline checks
- Focused plugins extend with specialized knowledge
- Incubator plugins test new ideas
- Custom rules can extend any of the above

This allows projects to compose exactly the rule set they need.

## Future Rule Development

The Flint project:

1. **Monitors popular ESLint rules**: Identifies commonly used patterns
2. **Reviews community requests**: Incorporates user needs
3. **Evaluates new patterns**: Tests emerging best practices
4. **Promotes successful rules**: Moves rules from incubator → focused → core based on community adoption

## Rule Statistics

Current rule categories include:
- **Core rules**: ~40+ across JSON, Markdown, YAML, JavaScript/TypeScript
- **Focused plugins**: ~100+ rules across specialized areas
- **Incubator plugins**: Growing collection of framework-specific rules

## Relationship with ESLint Rules

While Flint doesn't aim to be a direct ESLint replacement, many Flint rules are inspired by popular ESLint rules. The project:

- Studies successful ESLint rules
- Adapts patterns that work well
- Improves on rules with confusing configuration
- Adds type-aware versions of semantic rules
- Creates rules specific to Flint's architecture

## Getting More Information

- **Rules Reference**: https://flint.fyi/rules
- **GitHub Discussions**: Community discussions about specific rules
- **Discord**: Real-time discussion with maintainers
- **Blog Posts**: Deep dives into rule design decisions

---

**Related Documentation**:
- [Architecture Overview](./architecture.md)
- [Configuration Guide](./configuration.md)
- [Getting Started](./index.md)
