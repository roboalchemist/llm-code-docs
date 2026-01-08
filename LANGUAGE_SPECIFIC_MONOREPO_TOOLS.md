# Language-Specific Monorepo Tools and Frameworks

A comprehensive reference of monorepo tools and frameworks across programming language ecosystems, including native and specialized solutions.

## JavaScript/TypeScript Ecosystem

### Task Orchestration & Build Tools
- **Nx** - High-performance task runner with plugins for JS/TS/React/Angular, Go, and Rust with incremental builds and distributed caching.
- **Turborepo** - High-performance build system optimized for monorepos with remote caching and parallel task execution.
- **Rush** - Large-scale monorepo manager by Microsoft for TypeScript projects with advanced versioning and coordinated builds.
- **Lerna** - Package manager for JavaScript monorepos providing version management, dependency linking, and automated publishing.
- **Bit** - Language-agnostic component monorepo tool with build orchestration, dependency graphs, and automated publishing.

### Workspace Management
- **Yarn Workspaces** - Native workspace feature in Yarn for managing multiple packages with shared dependencies.
- **pnpm Workspaces** - High-performance monorepo workspace support with strict dependency resolution via pnpm.
- **npm Workspaces** - Native workspace management in npm 7+ for multi-package monorepos.

### Niche Tools
- **Lage** - Fast JavaScript monorepo task scheduler with incremental builds optimized for large codebases.
- **OAO** - Simple monorepo tool for managing and releasing multiple npm packages.

---

## Python Ecosystem

### Primary Monorepo Tools
- **Pants** - Powerful Python monorepo tool with dependency inference, incremental builds, and multi-language support (Python, Go, Java, Shell, Docker).
- **Bazel** - Google's scalable build system with Python support for large-scale monorepos with fine-grained dependency resolution.

### Native Package Management
- **Setuptools** - Python's standard build system supporting workspace-like structures with local package discovery.
- **Poetry** - Dependency management and packaging with workspace features for multi-package monorepos.
- **pip** - Can resolve local dependencies via editable installs and path-based requirements for monorepo setups.

---

## Go Ecosystem

### Native Solutions
- **Go Modules** - Standard tooling using `go.mod` with `replace` directives for local module imports and selective builds.

### Build Orchestration
- **Bazel** - Fine-grained dependency tracking and incremental rebuilds for Go monorepos with scalable multi-project support.
- **Pants** - Multi-language monorepo tool with strong Go support for incremental builds and dependency management.
- **Earthly** - Dockerfile-like build system for Go monorepos with containerized builds and CI/CD integration.

### Utility Tools
- **Tainted** - Determines which Go packages need rebuilding in monorepos based on code changes.
- **Makefiles** - Traditional build orchestration for Go monorepos with selective compilation and testing.

---

## Java Ecosystem

### Native Multi-Module Solutions
- **Gradle** - Modern build system with superior monorepo support via multi-module projects with incremental builds and flexible dependency management.
- **Maven** - Standard Java build tool providing multi-module project support for monorepo structures.

### Polyglot Monorepo Tools
- **Bazel** - Scalable build system with `java_library` and `java_binary` rules for large-scale Java monorepos.
- **Pants** - Multi-language monorepo tool with native Java support for incremental builds and dependency inference.

---

## .NET Ecosystem

### Native Solutions
- **MSBuild** - Microsoft's standard build engine supporting monorepo structures via solution files (.sln) and shared configurations.
- **dotnet CLI** - Native .NET tooling with `Directory.Build.props` for shared project configurations and multi-project solutions.

### Build Orchestration
- **Earthly** - Dockerfile-inspired build system compatible with .NET projects (Linux-based environments).
- **Bazel** - Can support .NET monorepos through custom rules for cross-platform build orchestration.

---

## Rust Ecosystem

### Native Workspace Solution
- **Cargo Workspaces** - Rust's native monorepo support via `Cargo.toml` with `[workspace]` members for shared dependencies and selective building.

### Advanced Build Tools
- **Nx** - Task runner with Rust plugins for monorepo optimization with incremental builds and distributed caching.
- **Bazel** - Scalable build system with Rust rules for large monorepos with fine-grained dependency tracking.

---

## C++ Ecosystem

### Build Systems
- **CMake** - Standard C++ build system orchestrating subprojects with incremental builds and modular architecture.
- **Bazel** - Purpose-built for C++ monorepos with `cc_library` and `cc_binary` rules and fine-grained dependency resolution.
- **Swamp** - Custom C++ build system optimized for monorepos with fast bootstrapping and tailored builds.

### Package Management
- **Conan** - C++ package manager supporting monorepo publishing of individual libraries from unified codebases.

---

## Kotlin Ecosystem

### Native Solutions
- **Gradle with Kotlin DSL** - Gradle's multi-module project support via `settings.gradle.kts` with incremental builds and Kotlin-first configuration.

### Multi-Language Support
- **Bazel** - Kotlin monorepo support via JVM rules with scalable dependency management.
- **Pants** - Multi-language monorepo tool compatible with Kotlin via JVM rulesets.

---

## PHP Ecosystem

### Native Workspace Solution
- **Composer Workspaces** - Native monorepo support in Composer 2.0+ via `repositories` pointing to local sibling packages.

### Build Orchestration
- **Bazel** - Can support PHP monorepos through custom rules for web project structures.

---

## Ruby Ecosystem

### Monorepo-Specific Tools
- **Rush** - Comprehensive monorepo tool for Ruby and JavaScript with incremental builds, dependency handling, and package management.
- **Pants** - Multi-language monorepo tool with Ruby support for fine-grained dependencies and parallel execution.
- **Bazel** - Ruby monorepo support through extensible rules for dependency graphs and efficient rebuilds.

---

## Elixir Ecosystem

### Build Tools
- **Pants** - Multi-language monorepo tool with Elixir support for scalable, incremental builds across mixed language projects.
- **Nx** - Monorepo optimizer with extensible plugin system adaptable to Elixir projects.
- **Bazel** - Enables Elixir monorepos with custom rules for dependency management and parallel builds.

---

## Clojure Ecosystem

### JVM-Based Build Tools
- **Bazel** - Supports Clojure via JVM rules with automatic incremental rebuilds and dependency tracking.
- **Pants** - JVM-compatible monorepo tool for Clojure with fast, dependency-aware builds and testing.
- **Nx** - Extensible monorepo tool with potential Clojure/JVM plugin integration for caching and distributed CI.

---

## Scala Ecosystem

### JVM Build Systems
- **Bazel** - Scala monorepo support with `scala_library` targets for incremental rebuilds and fine-grained dependency resolution.
- **Pants** - Native Scala support in polyglot monorepos with incremental builds and dependency inference.
- **Nx** - Monorepo tool adaptable to Scala/JVM environments via plugin system.

---

## Cross-Language Polyglot Tools

### Universal Monorepo Platforms
- **Bazel** - Google's polyglot build system supporting Java, Python, Go, C++, Rust, Kotlin, Ruby, Scala, Clojure with fine-grained dependency tracking.
- **Pants** - Fast monorepo tool with native support for Python, Go, Java, Shell, Docker, and other languages via extensible rulesets.
- **Earthly** - Dockerfile-like build system for any Linux-compatible language (JS, Python, Java, Go, Rust, C++) with containerized builds.
- **Buck2** - Meta's monorepo build system (successor to Buck) supporting multiple languages with incremental builds and distributed execution.
- **Please** - Go-based high-performance build system with cross-language support, reproducible builds, and fast incremental rebuilds.

### Specialized Orchestration
- **Nx** - Extensible task runner with plugins for multiple languages, designed for monorepo optimization with caching and CI distribution.
- **Turborepo** - Originally JS/TS focused but adaptable for multi-language via custom configurations.
- **baur** - Builds only changed applications in monorepos with artifact management across languages.
- **drkns** - Language-agnostic simple build system for monorepo structures.

---

## Selection Criteria by Use Case

### For JavaScript/TypeScript
Use **Nx**, **Turborepo**, or **pnpm Workspaces** for simplicity and ecosystem integration.

### For Python
Use **Pants** for comprehensive monorepo support or **Bazel** for multi-language integration.

### For Go
Use native **Go Modules** with `replace` directives or **Bazel/Pants** for advanced multi-project scenarios.

### For Java
Use **Gradle** for native monorepo support or **Bazel/Pants** for multi-language coordination.

### For .NET
Use native **MSBuild** and **dotnet CLI** with solution files.

### For Rust
Use native **Cargo Workspaces** or **Bazel/Nx** for advanced caching and task orchestration.

### For C++
Use **CMake** for standard builds or **Bazel** for large-scale monorepos with fine-grained control.

### For Multi-Language Monorepos
Use **Bazel**, **Pants**, or **Earthly** for consistent build orchestration across language boundaries.

---

## Key Features Comparison

| Tool | Languages | Incremental Builds | Dependency Inference | Distributed Caching | Learning Curve |
|------|-----------|-------------------|---------------------|-------------------|-----------------|
| Nx | JS/TS/Go/Rust | Yes | Partial | Yes | Low |
| Bazel | All Major | Yes | Yes | Yes | High |
| Pants | Python/Go/Java/etc | Yes | Yes | Yes | Medium |
| Turborepo | JS/TS | Yes | No | Yes | Low |
| Gradle | Java/Kotlin | Yes | Yes | Yes | Medium |
| Cargo | Rust | Yes | Yes | No | Low |
| CMake | C++ | Yes | No | No | Medium |
| Composer | PHP | No | Yes | No | Low |
| go.mod | Go | Yes | Yes | No | Low |

---

## Research Sources

- https://monorepo.tools
- https://earthly.dev/blog/monorepo-tools/
- https://www.aviator.co/blog/monorepo-tools/
- https://github.com/korfuri/awesome-monorepo
- https://graphite.com/guides/monorepo-tools-a-comprehensive-comparison
- https://blog.bitsrc.io/11-tools-to-build-a-monorepo-in-2021-7ce904821cc2

---

**Last Updated:** 2026-01-01
**Status:** Comprehensive coverage of 15+ languages and 25+ tools
