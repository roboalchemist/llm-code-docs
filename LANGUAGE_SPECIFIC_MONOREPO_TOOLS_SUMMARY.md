# Language-Specific Monorepo Tools - Quick Summary

Complete list of monorepo tools organized by language ecosystem with concise one-sentence descriptions.

## JavaScript/TypeScript

1. **Nx** - High-performance task runner with plugins for JS/TS/React/Angular, Go, and Rust providing incremental builds and distributed caching.
2. **Turborepo** - High-performance build system optimized for JavaScript monorepos with remote caching and parallel task execution.
3. **Rush** - Large-scale monorepo manager by Microsoft for TypeScript projects with advanced versioning and coordinated builds.
4. **Lerna** - JavaScript monorepo package manager providing version management, dependency linking, and automated publishing.
5. **Bit** - Language-agnostic component monorepo tool with build orchestration, dependency graphs, and automated publishing.
6. **Yarn Workspaces** - Native workspace feature in Yarn for managing multiple packages with shared dependencies.
7. **pnpm Workspaces** - High-performance monorepo workspace support with strict dependency resolution via pnpm.
8. **npm Workspaces** - Native workspace management in npm 7+ for multi-package monorepos.
9. **Lage** - Fast JavaScript monorepo task scheduler with incremental builds optimized for large codebases.
10. **OAO** - Simple monorepo tool for managing and releasing multiple npm packages.

## Python

1. **Pants** - Powerful Python monorepo tool with dependency inference, incremental builds, and multi-language support.
2. **Bazel** - Google's scalable build system with Python support for large-scale monorepos with fine-grained dependency resolution.
3. **Setuptools** - Python's standard build system supporting workspace-like structures with local package discovery.
4. **Poetry** - Dependency management and packaging with workspace features for multi-package monorepos.
5. **pip** - Standard package manager supporting local dependencies via editable installs and path-based requirements for monorepos.

## Go

1. **Go Modules** - Standard tooling using go.mod with replace directives for local module imports and selective builds.
2. **Bazel** - Fine-grained dependency tracking and incremental rebuilds for Go monorepos with scalable multi-project support.
3. **Pants** - Multi-language monorepo tool with strong Go support for incremental builds and dependency management.
4. **Earthly** - Dockerfile-like build system for Go monorepos with containerized builds and CI/CD integration.
5. **Tainted** - Tool that determines which Go packages need rebuilding in monorepos based on code changes.

## Java

1. **Gradle** - Modern build system with superior monorepo support via multi-module projects with incremental builds and flexible dependency management.
2. **Maven** - Standard Java build tool providing multi-module project support for monorepo structures.
3. **Bazel** - Scalable build system with java_library and java_binary rules for large-scale Java monorepos.
4. **Pants** - Multi-language monorepo tool with native Java support for incremental builds and dependency inference.

## .NET

1. **MSBuild** - Microsoft's standard build engine supporting monorepo structures via solution files (.sln) and shared project configurations.
2. **dotnet CLI** - Native .NET tooling with Directory.Build.props for shared project configurations and multi-project solution management.
3. **Earthly** - Dockerfile-inspired build system compatible with .NET projects in Linux-based environments.

## Rust

1. **Cargo Workspaces** - Rust's native monorepo support via Cargo.toml with [workspace] members for shared dependencies and selective building.
2. **Nx** - Task runner with Rust plugins for monorepo optimization with incremental builds and distributed caching.
3. **Bazel** - Scalable build system with Rust rules for large monorepos with fine-grained dependency tracking.

## C++

1. **CMake** - Standard C++ build system orchestrating subprojects with incremental builds and modular architecture.
2. **Bazel** - Purpose-built for C++ monorepos with cc_library and cc_binary rules and fine-grained dependency resolution.
3. **Swamp** - Custom C++ build system optimized for monorepos with fast bootstrapping and tailored builds.
4. **Conan** - C++ package manager supporting monorepo publishing of individual libraries from unified codebases.

## Kotlin

1. **Gradle with Kotlin DSL** - Gradle's multi-module project support via settings.gradle.kts with incremental builds and Kotlin-first configuration.
2. **Bazel** - Kotlin monorepo support via JVM rules with scalable dependency management.
3. **Pants** - Multi-language monorepo tool compatible with Kotlin via JVM rulesets.

## PHP

1. **Composer Workspaces** - Native monorepo support in Composer 2.0+ via repositories pointing to local sibling packages.
2. **Bazel** - Custom rule support for PHP monorepos enabling web project structure management.

## Ruby

1. **Rush** - Comprehensive monorepo tool for Ruby and JavaScript with incremental builds, dependency handling, and package management.
2. **Pants** - Multi-language monorepo tool with Ruby support for fine-grained dependencies and parallel execution.
3. **Bazel** - Ruby monorepo support through extensible rules for dependency graphs and efficient rebuilds.

## Elixir

1. **Pants** - Multi-language monorepo tool with Elixir support for scalable, incremental builds across mixed language projects.
2. **Nx** - Monorepo optimizer with extensible plugin system adaptable to Elixir projects.
3. **Bazel** - Enables Elixir monorepos with custom rules for dependency management and parallel builds.

## Clojure

1. **Bazel** - Supports Clojure via JVM rules with automatic incremental rebuilds and dependency tracking.
2. **Pants** - JVM-compatible monorepo tool for Clojure with fast, dependency-aware builds and testing.
3. **Nx** - Extensible monorepo tool with potential Clojure/JVM plugin integration for caching and distributed CI.

## Scala

1. **Bazel** - Scala monorepo support with scala_library targets for incremental rebuilds and fine-grained dependency resolution.
2. **Pants** - Native Scala support in polyglot monorepos with incremental builds and dependency inference.
3. **Nx** - Monorepo tool adaptable to Scala/JVM environments via plugin system.

## Cross-Language & Polyglot Tools

1. **Bazel** - Google's polyglot build system supporting Java, Python, Go, C++, Rust, Kotlin, Ruby, Scala, Clojure with fine-grained dependency tracking.
2. **Pants** - Fast monorepo tool with native support for Python, Go, Java, Shell, Docker, and other languages via extensible rulesets.
3. **Earthly** - Dockerfile-like build system for any Linux-compatible language with containerized builds and CI/CD integration.
4. **Buck2** - Meta's monorepo build system supporting multiple languages with incremental builds and distributed execution.
5. **Please** - Go-based high-performance build system with cross-language support, reproducible builds, and fast incremental rebuilds.
6. **Nx** - Extensible task runner with plugins for multiple languages, designed for monorepo optimization with caching and CI distribution.
7. **Turborepo** - JavaScript/TypeScript focused but adaptable for multi-language via custom configurations.
8. **baur** - Builds only changed applications in monorepos with artifact management across languages.
9. **drkns** - Language-agnostic simple build system for monorepo structures.

---

## Total Count by Category

- **JavaScript/TypeScript**: 10 tools
- **Python**: 5 tools
- **Go**: 5 tools
- **Java**: 4 tools
- **.NET**: 3 tools
- **Rust**: 3 tools
- **C++**: 4 tools
- **Kotlin**: 3 tools
- **PHP**: 2 tools
- **Ruby**: 3 tools
- **Elixir**: 3 tools
- **Clojure**: 3 tools
- **Scala**: 3 tools
- **Polyglot/Cross-Language**: 9 tools

**Grand Total**: 61 language-specific and polyglot monorepo tools documented

---

## Key Takeaways

1. **JavaScript/TypeScript has the most options** - 10+ ecosystem-specific tools with workspace standards built into package managers.
2. **Bazel and Pants are polyglot champions** - Both support 8+ languages natively with sophisticated dependency inference.
3. **Most languages have native solutions** - Go modules, Cargo, Composer, Maven, Gradle, CMake, MSBuild, etc. provide baseline monorepo support.
4. **JVM languages share tools** - Java, Kotlin, Scala, and Clojure often use Bazel, Pants, or Gradle for advanced monorepo needs.
5. **Incremental builds are standard** - Nearly all modern tools support incremental builds; caching and distributed execution vary by tool.

---

**Research Sources:**
- https://monorepo.tools
- https://earthly.dev/blog/monorepo-tools/
- https://www.aviator.co/blog/monorepo-tools/
- https://github.com/korfuri/awesome-monorepo
- https://graphite.com/guides/monorepo-tools-a-comprehensive-comparison

**Last Updated:** 2026-01-01
