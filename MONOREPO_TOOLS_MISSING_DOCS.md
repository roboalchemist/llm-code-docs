# Missing Monorepo Tools Documentation

Research conducted on 2026-01-01 to identify monorepo tools missing from llm-code-docs.

## Already Have Documentation

Based on search of docs/ directory, we already have:
- CircleCI (docs/llms-txt/circleci)
- Docker (docs/llms-txt/docker)
- Graphite (docs/llms-txt/graphite)
- Prettier (docs/llms-txt/prettier)
- Vite (docs/llms-txt/vite)
- Vitest (docs/llms-txt/vitest)

## Missing Documentation - High Priority Tools

### Build & Task Orchestration
1. **Nx** - Full-featured monorepo tool with code generation, distributed caching, and dependency graph visualization
2. **Turborepo** - High-performance monorepo build system with remote caching
3. **Bazel** - Google's polyglot build system with hermetic builds and parallel execution
4. **Pants** - Fast scalable monorepo tool for Python, Go, Java with fine-grained dependency modeling
5. **Rush** - Microsoft's large-scale JavaScript monorepo orchestrator
6. **Lerna** - JavaScript monorepo package manager for versioning and publishing
7. **moon** - Rust-based task runner for web ecosystems
8. **Lage** - Microsoft's lightweight JavaScript task scheduler
9. **Gradle** - JVM build automation tool with monorepo support
10. **Buck2** - Meta's next-generation build system
11. **Please** - Go-based high-performance build system
12. **Earthly** - Dockerfile-like build system for containerized builds
13. **Bit** - Component-driven monorepo platform
14. **Maven** - Standard Java build tool with multi-module support

### Package Managers & Workspaces
15. **Yarn** - Package manager with workspace support
16. **pnpm** - Efficient package manager with native workspace support
17. **npm** - Node package manager with workspace features
18. **Composer** - PHP dependency manager with workspace support
19. **Cargo** - Rust package manager with workspace support
20. **Poetry** - Python dependency management with workspace features

### Build Systems
21. **CMake** - Cross-platform build system for C++
22. **MSBuild** - Microsoft's build engine for .NET
23. **Conan** - C++ package manager

### Code Generation & Scaffolding
24. **Plop** - Micro-generator framework for code scaffolding

### Dependency Management
25. **Syncpack** - Synchronizes package.json fields across monorepo packages

### Developer Experience
26. **Commitlint** - Commit message convention enforcer
27. **Husky** - Git hooks manager
28. **Yalc** - Local npm package registry for testing

### Linting & Code Quality
29. **ESLint** - JavaScript/TypeScript linter
30. **TypeScript** - TypeScript compiler with multi-project support

### Build Tools (General)
31. **esbuild** - Fast JavaScript/TypeScript bundler
32. **Webpack** - Module bundler with monorepo support

### CI/CD Platforms
33. **Semaphore** - CI/CD platform with monorepo support
34. **Aviator** - Enterprise monorepo management tool

### Utilities
35. **Tainted** - Go package rebuild detection tool
36. **monorepo-mapper** - Visual dependency mapping tool
37. **depcheck** - Unused dependency detector
38. **Preconstruct** - Multi-entry-point library builder
39. **ORT (OSS Review Toolkit)** - Dependency compliance scanning

## Total Missing Documentation

**High Priority**: 39 tools identified

## Tools Excluded (Not Primary Documentation Targets)

The following were mentioned but are not standalone tools with dedicated documentation:
- Nx Schematics (part of Nx)
- Nx Graph (part of Nx)
- Nx Cloud (part of Nx)
- Nx Dependency Visualizer (part of Nx)
- Turborepo Graph (part of Turborepo)
- Lerna Migrate (part of Lerna)
- Nx Migrate (part of Nx)
- TurboSnap (Chromatic feature)
- Nx Affected (part of Nx)
- PNPM Catalogs (part of pnpm)
- Yarn Workspaces (part of Yarn)
- pnpm Workspaces (part of pnpm)
- npm Workspaces (part of npm)
- Composer Workspaces (part of Composer)
- Cargo Workspaces (part of Cargo)
- Go Modules (part of Go)
- dotnet CLI (part of .NET)
- Setuptools (part of Python)
- pip (part of Python)
- Makefiles (general Unix tool)
- baur (niche, limited adoption)
- drkns (niche, limited adoption)
- OAO/Oao (older/deprecated)
- Swamp (custom/proprietary)
- Buck (superseded by Buck2)

## Research Methodology

- 5 parallel haiku agents researched different aspects of monorepo tools
- Used Perplexity and Tavily APIs for comprehensive search
- Covered build tools, CI/CD, language ecosystems, utilities, and package managers
- De-duplicated and consolidated results into master list
- Cross-referenced against existing llm-code-docs documentation

## Next Steps

Since this repository doesn't have a DOCS trckr project, these findings can be used to:
1. Manually prioritize which tools to add documentation for
2. Create tickets in an external tracking system
3. Use as a reference for documentation gaps

## Recommendation

Focus on top 15 most critical tools first:
1. Nx
2. Turborepo
3. Bazel
4. Pants
5. Rush
6. Lerna
7. pnpm
8. Yarn
9. Gradle
10. Maven
11. CMake
12. Cargo
13. Poetry
14. TypeScript
15. ESLint

These represent the core ecosystem tools that developers are most likely to need documentation for when working with monorepos.

---

**Research Date**: 2026-01-01
**Total Tools Researched**: 70+
**Already Have Docs**: 6 tools
**Missing Documentation**: 39 high-priority tools
**Excluded as Non-Primary**: 25+ tools
