# Monorepo Tools Documentation Index

Complete research on language-specific monorepo tools and frameworks across 15+ programming language ecosystems.

## Documentation Files

### Main Reference Documents

1. **[LANGUAGE_SPECIFIC_MONOREPO_TOOLS.md](./LANGUAGE_SPECIFIC_MONOREPO_TOOLS.md)** (10KB)
   - Comprehensive guide with detailed descriptions of 61+ monorepo tools
   - Organized by language ecosystem (JavaScript, Python, Go, Java, .NET, Rust, C++, etc.)
   - Includes use case recommendations and feature comparison matrix
   - Selection criteria for different scenarios

2. **[LANGUAGE_SPECIFIC_MONOREPO_TOOLS_SUMMARY.md](./LANGUAGE_SPECIFIC_MONOREPO_TOOLS_SUMMARY.md)** (8.6KB)
   - Quick-reference guide with one-sentence descriptions for all tools
   - Organized by language with 61+ tools total
   - Key takeaways and summary statistics
   - Perfect for quick lookups

3. **[LANGUAGE_SPECIFIC_MONOREPO_TOOLS_QUICK_REFERENCE.csv](./LANGUAGE_SPECIFIC_MONOREPO_TOOLS_QUICK_REFERENCE.csv)** (4.3KB)
   - Spreadsheet format with 34 tools and their key properties
   - Columns: Tool name, primary languages, category, description, learning curve, features
   - Machine-readable format for filtering and analysis

## Language Coverage

### Fully Documented Languages
- **JavaScript/TypeScript** - 10 ecosystem-specific tools
- **Python** - 5 tools (Pants, Bazel, Setuptools, Poetry, pip)
- **Go** - 5 tools (Go Modules, Bazel, Pants, Earthly, Tainted)
- **Java** - 4 tools (Gradle, Maven, Bazel, Pants)
- **Rust** - 3 tools (Cargo Workspaces, Nx, Bazel)
- **C++** - 4 tools (CMake, Bazel, Swamp, Conan)
- **Kotlin** - 3 tools (Gradle, Bazel, Pants)
- **.NET** - 3 tools (MSBuild, dotnet CLI, Earthly)
- **PHP** - 2 tools (Composer, Bazel)
- **Ruby** - 3 tools (Rush, Pants, Bazel)
- **Elixir** - 3 tools (Pants, Nx, Bazel)
- **Clojure** - 3 tools (Bazel, Pants, Nx)
- **Scala** - 3 tools (Bazel, Pants, Nx)

### Polyglot Tools (9 tools)
- **Bazel**, **Pants**, **Earthly**, **Buck2**, **Please**, **Nx**, **Turborepo**, **baur**, **drkns**
- Support for 8+ languages with consistent build orchestration

## Quick Navigation

### By Ecosystem

| Ecosystem | Primary Tools | Native Support |
|-----------|---------------|-----------------|
| **JavaScript/TypeScript** | Nx, Turborepo, pnpm/Yarn Workspaces | Yes (Workspaces) |
| **Python** | Pants, Bazel | No native |
| **Go** | Go Modules | Yes (replace directives) |
| **Java** | Gradle, Maven | Yes (multi-module) |
| **Rust** | Cargo Workspaces | Yes (native) |
| **.NET** | MSBuild, dotnet CLI | Yes (solution files) |
| **C++** | CMake | Yes (subdirectories) |
| **Kotlin** | Gradle | Yes (via Gradle) |
| **PHP** | Composer Workspaces | Yes (Composer 2.0+) |
| **Ruby** | Rush, Pants | No native |
| **Polyglot** | Bazel, Pants, Earthly | Multi-language |

### By Tool Category

| Category | Key Tools |
|----------|-----------|
| **Build Systems** | Bazel, Pants, CMake, Gradle, Maven |
| **Task Runners** | Nx, Turborepo, Lage |
| **Package Managers** | npm Workspaces, Yarn Workspaces, pnpm, Composer |
| **Component Tools** | Bit |
| **Containerized Builds** | Earthly, Buck2 |
| **Language-Specific** | Cargo, Go Modules, Poetry, Setuptools |

### By Key Features

| Feature | Best Tools |
|---------|-----------|
| **Multi-Language Support** | Bazel, Pants, Earthly, Buck2, Please |
| **Incremental Builds** | Nx, Bazel, Pants, Gradle, Turborepo |
| **Distributed Caching** | Nx, Turborepo, Bazel, Buck2 |
| **Lowest Learning Curve** | pnpm Workspaces, Cargo, Go Modules, npm Workspaces |
| **Dependency Inference** | Bazel, Pants, Nx |
| **Enterprise Ready** | Rush, Bazel, Gradle, Pants |

## Research Methodology

- **Primary Research Tool**: Perplexity AI with citations
- **Secondary Research Tool**: Tavily AI (API rate-limited)
- **Coverage**: 15+ language ecosystems
- **Total Tools Documented**: 61+ unique monorepo tools
- **Sources**: Official documentation, GitHub repos, comparative analysis articles

### Source Quality
All findings supported by:
- Official tool documentation (monorepo.tools, earthly.dev, etc.)
- Comparative analysis from Graphite, Aviator, BitSrc
- Awesome-monorepo GitHub repository
- Upstream project documentation (Bazel, Pants, Gradle, etc.)

## Key Insights

### 1. Native vs. Specialized Tools
Most languages have native monorepo support:
- **Native**: Go modules, Cargo workspaces, Maven multi-module, Gradle multi-project, Composer workspaces, MSBuild solutions
- **Specialized**: Bazel, Pants, Nx (add tooling around native support)

### 2. Polyglot vs. Language-Specific
- **JavaScript/TypeScript**: 10+ ecosystem-specific tools (most developed)
- **JVM Languages**: Share tools (Bazel, Pants, Gradle)
- **Multi-language**: Bazel and Pants are polyglot leaders
- **Emerging**: Earthly, Buck2, Please for modern distributed builds

### 3. Learning Curve vs. Features
- **Low Curve**: pnpm/Yarn, Cargo, Go Modules, npm Workspaces, Composer
- **Medium Curve**: Gradle, Nx, Pants, Poetry
- **High Curve**: Bazel (but most powerful for large-scale)

### 4. Adoption Patterns
- **Large Enterprises**: Bazel (Google), Pants (Twitter/Uber origins), Rush (Microsoft)
- **Modern Startups**: Turborepo, Nx, pnpm
- **Open Source**: Gradle, Maven, Cargo, CMake
- **Community-Driven**: Pants, Please

## Selection Guide

### For Small Projects (< 20 packages)
**Recommendation**: Use language-native solutions
- JavaScript: npm/Yarn/pnpm Workspaces
- Python: Poetry or Setuptools
- Go: Go Modules
- Rust: Cargo Workspaces

### For Medium Projects (20-100 packages)
**Recommendation**: Add specialized orchestration
- JavaScript: Nx or Turborepo
- Python: Pants
- Go: Bazel or Pants
- Java: Gradle multi-project

### For Large Enterprises (100+ packages, multi-language)
**Recommendation**: Polyglot build system
- **Best**: Bazel or Pants
- **Alternative**: Earthly for simpler Docker-based approach
- **Supplement**: Language-specific tools (Gradle, Cargo, etc.)

## Files at a Glance

```
monorepo-tools-documentation/
├── MONOREPO_TOOLS_INDEX.md (this file)
│   Navigation and overview of all resources
│
├── LANGUAGE_SPECIFIC_MONOREPO_TOOLS.md
│   Complete reference with 61+ tools, organized by language
│   Features comparison matrix, use case guidance
│
├── LANGUAGE_SPECIFIC_MONOREPO_TOOLS_SUMMARY.md
│   Quick-reference with one-sentence descriptions
│   Organized by language, 61+ tools, key takeaways
│
└── LANGUAGE_SPECIFIC_MONOREPO_TOOLS_QUICK_REFERENCE.csv
    Spreadsheet format with 34 key tools and properties
    Machine-readable, sortable by language, category, features
```

## How to Use This Documentation

### For Tool Selection
1. Start with "By Ecosystem" navigation table
2. Check "Selection Guide" for your project scale
3. Read detailed tool descriptions in main reference

### For Comparison
1. Open the CSV file for quick feature comparison
2. Use the "Key Features" matrix in this index
3. Reference "Learning Curve vs. Features" insights

### For Deep Dives
1. Read the comprehensive main reference document
2. Follow source citations for official documentation
3. Check tool-specific sections for implementation details

### For Research
1. Review selection criteria by use case in main reference
2. Check research sources for latest updates
3. Note publication date (2026-01-01) for current relevance

---

**Documentation Complete**: 61+ monorepo tools documented across 13 language ecosystems plus 9 polyglot tools

**Last Updated**: 2026-01-01

**Completeness**: Comprehensive coverage of language-specific monorepo solutions with native and specialized tools
