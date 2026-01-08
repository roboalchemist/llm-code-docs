# Flint - A Modern TypeScript-Focused Linter

## Source: https://flint.fyi

Flint is an experimental, fast TypeScript/JavaScript linter with a hybrid architecture designed to test modern approaches to code linting. The core is written in TypeScript for accessibility, with language-specific plugins able to use native-speed tooling for optimal performance.

## Overview

**Flint** is a fast, friendly linter for JavaScript, TypeScript, and other web ecosystem languages. It's a proof-of-concept exploring novel approaches to linting architecture, configuration, rule organization, and tooling integration.

Created by Josh Goldberg and maintained by open source volunteers, Flint operates independently without corporate backing or funding pressure.

### Current Status

**Important**: Flint is still very early stage and experimental. Not all features have been implemented. The project is in active development and the creators explicitly state: "Don't expect Flint to be ready to alpha test for several months from now, at the earliest."

## Design Philosophy

Flint is built on four core hypotheses about modern linting:

### 1. Hybrid Linting Architecture

Traditional linters typically choose between:
- **JavaScript/TypeScript-based**: Easier to contribute to but slower (like ESLint)
- **Native languages**: Faster but harder for community contributions (like Biome, Oxlint)

Flint combines the best of both worlds:
- **Core framework**: Written in TypeScript for accessibility and ease of contribution
- **Language plugins**: Can be developed in native performance-focused languages for computational efficiency

This approach delegates the most computationally expensive tasks like parsing and type checking to native-speed languages, while keeping the linter framework approachable for contributors.

### 2. Streamlined Configuration System

Rather than forcing users to choose between:
- **Rigid JSON configs**: Limited flexibility and prone to errors
- **JavaScript-based setups**: Complex and error-prone

Flint proposes fully type-safe JavaScript configurations that automatically handle parsing, processing, and other edge case hazards behind-the-scenes. This avoids the pitfalls ESLint users experienced while maintaining flexibility for workspace configurations and plugin composition.

### 3. Comprehensive Built-in Rules

Flint bundles extensive rules directly into the core project across multiple tiers:
- **Core plugins**: Universal rules applicable to any project
- **Focused plugins**: Rules for large areas or specific code styles
- **Incubator plugins**: Area-specific plugins under community governance

The project maintains a reference list of over 1,000 popular lint rules to ensure comprehensive coverage.

### 4. Tooling Coordination

Flint integrates formatters (Prettier) and language diagnostics (TypeScript type errors) into a unified linting experience, reducing CI complexity for development teams. This eliminates the need for separate tool chains and coordinates linting concerns.

## Core Features

### Ergonomic Rule Writing
- Write linting rules in JavaScript or TypeScript
- Access to TypeScript's powerful type system for rule definitions
- Approachable for both users and contributors

### Performance Optimization
- Hybrid architecture balances speed with developer experience
- Type-aware caching for significant performance improvements
- Native-speed parsing and type checking when needed

### Streamlined Configuration
- Flexible, type-safe configuration files
- Automatic edge case handling
- Simplified workspace and plugin composition

### Unified Core
- Popular rules promoted to the core project
- More reliable inclusion and maintenance
- Consistent rule quality and documentation

## Rule Organization

Flint organizes linting rules into three tiers:

### Core Plugins (Included with `flint`)

Rules applicable to any project using their language:

- **JSON** - Rules for linting `.json` files
- **Markdown** - Rules for linting `.md` files containing Markdown
- **PackageJSON** - Rules for linting Node.js `package.json` manifest files
- **TypeScript/JavaScript** - Rules for linting JavaScript and TypeScript code
- **YAML** - Rules for linting `.yaml`/`.yml` files

### Focused Plugins

Plugins for large areas of projects or code styles applicable to many (but not all) Flint users. Available as separate packages under `@flint.fyi/`:

- Browser
- Flint
- JSX
- Node.js
- Performance
- Sorting
- Spelling

### Incubator Plugins

Area-specific plugins that should exist under community governance, but don't yet have a dedicated team. Available as separate packages under `@flint.fyi/`:

- Astro
- Next.js
- Nuxt
- React
- SolidJS
- Vitest
- Vue

## Getting Started

Usage instructions are currently being developed. The planned setup process will involve:

1. Running the `flint` command in an existing project
2. Being prompted about preferred linting areas
3. Automatic configuration file generation
4. Installation of necessary dependencies

**Note**: This feature is not yet implemented as Flint is still in very early development.

## Community and Resources

### Connect with the Community

- **Discord Server**: https://flint.fyi/discord - Active community discussing development and ideas
- **GitHub Issues**: https://github.com/flint-fyi/flint/issues - Report bugs and request features
- **Open Collective**: https://opencollective.com/flintfyi - Support the project financially

### Documentation and References

- **Official Website**: https://flint.fyi
- **Rules Reference**: https://flint.fyi/rules
- **GitHub Repository**: https://github.com/flint-fyi/flint
- **Blog**: https://flint.fyi/blog/

### Related Reading

Flint's design is informed by Josh Goldberg's blog series on linter architecture:

1. [Hybrid Linters: The Best of Both Worlds](https://www.joshuakgoldberg.com/blog/hybrid-linters-the-best-of-both-worlds)
2. [If I Wrote a Linter, Part 1: Architecture](https://www.joshuakgoldberg.com/blog/if-i-wrote-a-linter-part-1-architecture)
3. [If I Wrote a Linter, Part 2: Developer Experience](https://www.joshuakgoldberg.com/blog/if-i-wrote-a-linter-part-2-developer-experience)
4. [If I Wrote a Linter, Part 3: Ecosystem](https://www.joshuakgoldberg.com/blog/if-i-wrote-a-linter-part-3-ecosystem)
5. [If I Wrote a Linter, Part 4: Summary](https://www.joshuakgoldberg.com/blog/if-i-wrote-a-linter-part-4-summary)

## Contributing

Flint welcomes contributions from the community. The project maintains:

- **Contributor Covenant Code of Conduct** - Expected behavior for all contributors
- **Contributing Guidelines** - Process for reporting issues and sending pull requests
- **Development Documentation** - Instructions for local development setup

Contributors should:

1. File or find an issue marked as `status: accepting prs`
2. Send a pull request adhering to conventional commits
3. Add a changeset for user-facing changes using `pnpm changeset`
4. Keep PRs single-purpose and focused
5. Ensure GitHub status checks pass before requesting review

### For First-Time Contributors

Look for issues marked with both:
- `good first issue` label
- `status: accepting prs` label

These are specifically identified as suitable starting points for new contributors.

## Technical Stack

### Core Technology
- **Language**: TypeScript (strict mode)
- **Package Manager**: npm (published as `flint`)
- **Repository**: https://github.com/flint-fyi/flint
- **License**: MIT

### Architecture Highlights
- **Monorepo Structure**: Multiple packages organized for different plugins and tools
- **Type Safety**: Strict TypeScript configuration
- **Plugin System**: Modular architecture supporting core, focused, and incubator plugins
- **Performance**: Hybrid approach with native-speed components where needed

## Success Criteria

Flint's ultimate purpose is experimental validation. Success means either:

1. **Confirming all hypotheses** - Proving this approach creates a fast, straightforward linter that's better than existing solutions
2. **Disproving them** - Validating why existing solutions like ESLint and Biome are designed the way they are

The project explicitly acknowledges it might go nowhere, might show some ideas to be wrong, or might become a real linter. Only time will tell.

## Why Flint Exists

Traditional linters have made compromises:
- ESLint prioritized developer experience over performance
- Biome and Oxlint prioritized performance over community contribution accessibility

Flint explores whether a third way is possible: combining the accessibility of ESLint with the performance of native linters through intelligent architectural choices.

The project tests whether:
- A hybrid approach can deliver both ergonomics and performance
- Type-safe configuration can solve years of ESLint configuration pain points
- Organizing rules by scope improves developer experience
- Unified tooling coordination reduces CI complexity

## Project Statistics

- **Contributors**: 10+ community members
- **NPM Package**: Published as `flint`
- **Repository**: Active development on GitHub
- **Code Quality**: Strict TypeScript

## Frequently Asked Questions

### Is Flint ready to use?

No, Flint is in very early experimental development. The core features are still being designed and implemented. Expect several more months of development before alpha testing.

### Can I contribute?

Yes! Flint actively welcomes contributions. Check the GitHub issues for items marked as `status: accepting prs` and `good first issue` to get started.

### What's the relationship between Flint and ESLint?

Flint is inspired by ESLint's approach but explores different architectural choices. Both projects serve different purposes and audiences. Flint is experimental, while ESLint is a mature, widely-used production tool.

### Will Flint replace ESLint?

Flint's goal is to test novel hypotheses about linting, not necessarily to replace existing tools. It might validate existing approaches or provide alternatives. The success criteria is learning from the experiment, regardless of outcome.

### How can I follow Flint's progress?

- Join the Discord: https://flint.fyi/discord
- Watch the GitHub repository: https://github.com/flint-fyi/flint
- Read the blog: https://flint.fyi/blog/

## Related Tools and Concepts

### Similar Linters
- **ESLint** - JavaScript linter (JavaScript-based, mature)
- **Biome** - JavaScript/TypeScript toolchain (native-speed, monorepo focused)
- **Oxlint** - JavaScript linter (native-speed, high performance)

### Complementary Tools
- **Prettier** - Code formatter (integrated into Flint's vision)
- **TypeScript** - Language and type checker (integrated into rules)

### Concepts Explored
- Hybrid linting architecture
- Type-safe configuration
- Rule tier organization
- Tooling coordination

## License

MIT License - See the GitHub repository for details.

## Credits

- **Creator**: Josh Goldberg
- **Team**: Maintained by open source volunteers
- **Contributors**: 10+ community members actively contributing to the project
- **Location**: Boston, USA

---

**Last Updated**: January 2026
**Source**: https://flint.fyi | https://github.com/flint-fyi/flint
