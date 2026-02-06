# GritQL Documentation

This directory contains comprehensive documentation for **GritQL**, a query language for structural code search and transformation from [grit.io](https://grit.io/).

## Overview

GritQL is a powerful, intuitive query language designed for developers who want to search and transform code at scale. It enables:

- **Structural Code Search**: Find code patterns beyond simple text matching
- **Automated Transformations**: Rewrite code patterns with metavariables and conditions
- **Multi-Language Support**: Works with JavaScript/TypeScript, Python, JSON, Java, Terraform, Solidity, CSS, Markdown, YAML, Rust, Go, and SQL
- **CLI Integration**: Use patterns from the command line with the Grit CLI
- **CI/CD Ready**: Integrate code transformations into development workflows

## Documentation Structure

### Core Language Documentation
- **language_overview.md** - Introduction to GritQL and its basic concepts
- **language_syntax.md** - Complete syntax reference for GritQL patterns
- **language_patterns.md** - Pattern matching fundamentals including code snippets, metavariables, and the rewrite operator
- **language_conditions.md** - How to add conditions to patterns for more precise matching
- **language_modifiers.md** - Pattern modifiers for controlling matching behavior
- **language_functions.md** - Built-in functions for transformations
- **language_idioms.md** - Common GritQL idioms and best practices
- **language_target-languages.md** - Supported programming languages

### CLI & Tools
- **cli_quickstart.md** - Get started with the Grit CLI tool
- **cli_reference.md** - Complete CLI command reference

### Guides & Best Practices
- **guides_patterns.md** - How to write and structure effective patterns
- **guides_config.md** - Configuration guide for Grit projects
- **guides_authoring.md** - Best practices for authoring GritQL patterns
- **guides_imports.md** - How to import and compose patterns
- **guides_testing.md** - Testing patterns before deployment
- **guides_ci.md** - Integrating GritQL into CI/CD pipelines
- **guides_sharing.md** - Sharing patterns with teams

### Tutorials & Examples
- **tutorials_gritql.md** - Interactive tutorial for learning GritQL
- **patterns.md** - Available pattern library

### Other
- **index.md** - Main documentation homepage
- **blog.md** - Blog articles about GritQL

## Getting Started

To get started with GritQL:

1. Visit [docs.grit.io](https://docs.grit.io/)
2. Read the **language_overview.md** and **language_patterns.md** for fundamentals
3. Follow the **tutorials_gritql.md** for a hands-on introduction
4. Use **cli_quickstart.md** to install and start using the Grit CLI
5. Explore **guides_patterns.md** for best practices

## Key Concepts

### Patterns
The core construct in GritQL. A pattern searches in a codebase for matching clauses and optionally executes a specified transformation.

```gritql
pattern `console.log($message)` => `console.warn($message)`
```

### Metavariables
Used to create bindings to specific parts of the syntax tree, prefixed with `$`:

```gritql
`console.log($foo)` where { $foo => "debug" }
```

### Rewrite Operator
The `=>` operator transforms matched patterns:

```gritql
`println($msg)` => `console.log($msg)`
```

### Conditions
Add `where` clauses to restrict matches:

```gritql
`console.log($msg)` where { $msg <> "debug" }
```

## Supported Languages

- JavaScript/TypeScript
- Python
- JSON
- Java
- Terraform
- Solidity
- CSS
- Markdown
- YAML
- Rust
- Go
- SQL

## Installation

```bash
curl -fsSL https://docs.grit.io/install | bash
```

## Use Cases

- **Code Refactoring**: Bulk refactor code patterns across entire codebases
- **Linting & Standards**: Enforce coding standards automatically
- **API Migrations**: Migrate code to new API versions
- **Security**: Find and fix security vulnerabilities at scale
- **Tech Debt**: Identify and eliminate technical debt patterns

## Official Resources

- **Official Website**: https://grit.io/
- **Official Docs**: https://docs.grit.io/
- **GitHub**: https://github.com/biomejs/gritql
- **Playground**: https://app.grit.io/studio
- **Community Discord**: https://docs.grit.io/discord

## Source Information

This documentation was automatically scraped from the official GritQL documentation site at https://docs.grit.io/ on 2026-02-06.

For the most up-to-date documentation, always refer to https://docs.grit.io/.
