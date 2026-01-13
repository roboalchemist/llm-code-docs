# Flint Architecture

## Source: https://flint.fyi

## Hybrid Linting Architecture

Flint's core innovation is its hybrid architecture that combines TypeScript development ergonomics with native-speed performance.

### The Design Choice

Traditional linters face a fundamental tradeoff:

**JavaScript/TypeScript-based Linters (like ESLint)**
- Pros: Easy to understand, contribute to, and extend
- Cons: Slower performance, especially on large codebases

**Native-Speed Linters (like Biome, Oxlint)**
- Pros: Extremely fast performance
- Cons: Harder for community contributions, steeper learning curve

### Flint's Solution

Flint divides responsibilities between two layers:

#### 1. Core Framework (TypeScript)
- Linter orchestration and rule management
- Configuration handling
- Output formatting
- User interface
- Easy for contributors to write and understand

#### 2. Language Plugins (Flexible Implementation)
- Parsing (can use native implementations like `typescript-go`)
- Type checking
- Other computationally expensive operations
- Can be implemented in native languages for speed
- Maintain a well-defined interface for the core framework

### How It Works

```
User Input
    ↓
TypeScript Core Framework
    ↓
Rule Engine (TypeScript)
    ├─→ Core Rules (TypeScript)
    ├─→ Plugin Rules (TypeScript or Native)
    ├─→ Language Plugins (Native-Speed)
    │   ├─→ Parser (could be native)
    │   └─→ Type Checker (could be native)
    └─→ Output Formatting (TypeScript)
    ↓
Formatted Results
```

### Benefits

1. **Low Barrier to Entry**: New contributors can easily write rules in TypeScript
2. **Extensibility**: Plugin authors can choose their implementation language
3. **Performance**: Heavy lifting delegated to optimized native components
4. **Maintainability**: Clear separation of concerns between framework and plugins
5. **Community-Friendly**: TypeScript core makes it easier to build a contributor base

## Core Concepts

### The Rule System

Rules in Flint are written as TypeScript/JavaScript functions that:
- Access TypeScript's type information
- Check specific code patterns
- Report violations with detailed messages
- Can be configured by users

### Type-Aware Linting

Unlike traditional linters that only understand syntax, Flint leverages TypeScript's type information:
- Rules can understand semantic meaning, not just syntax
- Better error detection and fewer false positives
- Integration with TypeScript's type checker

### Configuration System

Flint's type-safe configuration:
- Written in JavaScript/TypeScript (not JSON)
- Full IDE autocomplete support
- Type validation at configuration time
- Reduces user errors and ambiguity

## Multi-Tier Plugin Organization

### Core Plugins (Built-in)

Shipped with Flint, maintained by core team:
- JSON linting
- Markdown linting
- JavaScript/TypeScript linting
- YAML linting
- Package.json manifest linting

### Focused Plugins

Maintained by dedicated teams, focused on specific areas:
- Browser-specific rules
- Node.js-specific rules
- React-specific rules
- Performance-specific rules
- And more

### Incubator Plugins

Community-maintained plugins for emerging needs:
- Framework-specific rules (Next.js, Nuxt, Astro)
- Specialized domain rules (Vitest, SolidJS)

## Performance Optimizations

### Type-Aware Caching

Flint implements intelligent caching:
- Caches type information across runs
- Avoids re-type-checking unchanged files
- Significantly improves performance on large codebases
- Especially beneficial in watch mode and CI environments

### Parallel Processing

- File linting can happen in parallel
- Plugin operations optimized for concurrent execution
- Efficient resource utilization

### Incremental Updates

- Only re-lint changed files
- Maintain state between runs
- Fast feedback in development workflows

## Integration Points

### TypeScript Integration

- Deep integration with TypeScript compiler API
- Access to full type information
- Direct use of TypeScript's parser
- Compatibility with TypeScript projects

### Formatter Integration

- Potential integration with Prettier for formatting
- Unified linting and formatting experience
- Coordinated tooling approach

### Language Server Protocol (LSP)

- Potential editor integration through LSP
- Real-time linting feedback in IDEs
- Language-agnostic editor support

## Comparison with Other Linters

### vs. ESLint

| Aspect | ESLint | Flint |
|--------|--------|-------|
| Language | JavaScript | TypeScript |
| Type-Aware | Limited | Full TypeScript integration |
| Performance | Slower on large codebases | Hybrid approach for optimization |
| Configuration | JSON/JS | Type-safe JavaScript |
| Plugins | Separate npm packages | Integrated tiers |
| Maturity | Production-ready | Experimental |

### vs. Biome

| Aspect | Biome | Flint |
|--------|-------|-------|
| Language | Rust | TypeScript + optional native |
| Contributor Accessibility | Lower | Higher |
| Performance | Very fast | Optimized hybrid |
| Formatter Included | Yes | Planned |
| Linter + Formatter | Yes | Yes (planned) |
| Customizability | Limited | High |

### vs. Oxlint

| Aspect | Oxlint | Flint |
|--------|--------|-------|
| Language | Rust | TypeScript + optional native |
| ESLint Compatible | Partial | Not directly |
| Performance | Extremely fast | Optimized hybrid |
| Community Contributions | Limited | Encouraged |
| Maturity | Established | Early experimental |

## Technical Implementation

### Plugin Interface

Plugins in Flint:
- Implement a well-defined TypeScript interface
- Can be written in any language
- Communicate with core through defined protocols
- Maintain version compatibility

### Rule Definition

Rules follow a consistent structure:
```typescript
interface LintRule {
  name: string;
  description: string;
  severity: 'error' | 'warning';
  create: (context: RuleContext) => RuleListeners;
}
```

### Type Information Flow

1. TypeScript parses the source code
2. Type checker generates type information
3. Rules access both AST and type information
4. Rules report violations with detailed context
5. Core formats and outputs results

## Evolution and Future

### Phase 1: Foundation
- Core architecture definition
- Initial rule set
- Configuration system
- Basic plugin support

### Phase 2: Optimization
- Performance tuning
- Caching system implementation
- Native plugin examples
- Production hardening

### Phase 3: Maturity
- Full LSP integration
- Comprehensive rule library
- Community plugin ecosystem
- Stable release

## Why This Architecture?

Flint's design addresses fundamental questions:

1. **Is hybrid better?** - Can we get both community accessibility and native performance?
2. **Does type-safety help?** - Can better configuration reduce user errors?
3. **Is tiered organization better?** - Can rule organization improve developer experience?
4. **Can tooling unify?** - Can integrated formatters and diagnostics simplify CI?

The experimental nature of Flint allows testing these hypotheses in practice, learning whether this approach represents an actual improvement or validates why existing tools are designed differently.

---

**Related Documentation**:
- [Configuration Guide](./configuration.md)
- [Rules System](./rules.md)
- [Plugin Development](./plugins.md)
