# Build Tools Documentation Coverage Report

**Repository:** `/Users/joe/github/llm-code-docs/`
**Total Tools Checked:** 140
**Coverage:** 17 tools (12.1%)
**Date:** January 1, 2026

---

## TOOLS WITH DOCUMENTATION (17/140)

### Frontend Build Tools & Runtimes
1. **Vite** → `docs/llms-txt/vite/`
2. **Turbo** → `docs/llms-txt/turbo/`
3. **Expo** → `docs/llms-txt/expo/`
4. **Next.js** → `docs/llms-txt/nextjs/`
5. **Bun** → `docs/llms-txt/bun/`
6. **React Native** → `docs/llms-txt/react-native/`

### CI/CD & Cloud Platforms
7. **CircleCI** → `docs/llms-txt/circleci/`
8. **AWS CodePipeline** → `docs/llms-txt/aws/`

### Containerization
9. **Docker** → `docs/llms-txt/docker/`
10. **Docker BuildKit** → `docs/llms-txt/docker/`

### Language-Specific Build Tools
11. **Go Build** → `docs/github-scraped/go-docs/`
12. **go mod** → `docs/github-scraped/go-docs/`

### Styling & UI Frameworks
13. **Tailwind CSS** → `docs/llms-txt/tailwindcss/`
14. **Chakra UI** → `docs/llms-txt/chakra-ui/`
15. **Styled Components** → `docs/github-scraped/styled-components/`
16. **Emotion** → `docs/web-scraped/emotion/`
17. **Vanilla Extract** → `docs/web-scraped/vanilla-extract/`

---

## TOOLS WITHOUT DOCUMENTATION (123/140)

### Build Automation & Make Tools (12)
Apache Ant, Autotools, Bazel, Buck, Buck2, CMake, GNU Make, Just, Make, Meson, Ninja, Scons

### Task Runners & Monorepo Tools (8)
Lage, Lerna, Moonrepo, Nx, Rush, Task, Taskfile, Turborepo

### JavaScript/TypeScript Build Tools (14)
Babel, Biome, Gulp, Grunt, Parcel, Rolldown, Rollup, Rome, SWC, Sucrase, Turbopack, TypeScript Compiler, esbuild, tsup

### Package Managers & Dependency Management (25)
Apache Maven, Bower, Bundler, Cargo, Carthage, CocoaPods, Gradle, Hatch, Maven, PDM, Pipenv, Poetry, Ruff, Swift Package Manager, Yarn, cargo-deny, cargo-mobile, cargo-watch, ccache, cross, npm, npm Workspaces, npm scripts, pip, pnpm, setuptools, uv, vcpkg

### CSS/Styling Tools (5)
Less, Lightning CSS, PostCSS, Sass, Stitches

### Containerization & Build Infrastructure (6)
Buildah, Buildcache, Kaniko, Podman, Remote Build Execution, Webpack

### CI/CD & Deployment Platforms (11)
Azure DevOps, Bamboo, Bitbucket Pipelines, Buildkite, GitHub Actions, GitLab CI, Google Cloud Build, Harness, Jenkins, Spacelift, TeamCity, Travis CI

### Infrastructure & Configuration Management (5)
Ansible, Kubernetes, Terraform, Vagrant, nix

### Workflow Orchestration & Automation (5)
Dagger, Earthly, Invoke, Kestra, Prefect

### Mobile & Native Development (8)
Android NDK, Android Studio, Android Studio with NDK, Flutter, FlutterFlow, Gomobile, TinyGo, Zig, Zig cc

### Web Frameworks & Generators (3)
Gatsby, Ionic, WaveMaker

### Other Tools (6)
Apache Cordova, Dune, LLVM, MAMP, Nix Flakes, Pants, ReproZip, guix, moon, ImageOptim, Imagemin

---

## Statistics by Documentation Source

| Source | Count | Tools |
|--------|-------|-------|
| **llms-txt** | 14 | aws, bun, chakra-ui, circleci, docker, expo, nextjs, react-native, tailwindcss, turbo, vite |
| **github-scraped** | 2 | go-docs, styled-components |
| **web-scraped** | 2 | emotion, vanilla-extract |
| **Total** | **17** | — |

---

## High-Priority Gaps (Recommended for Addition)

The following tools are missing and would provide high LLM value:

1. **npm** - Most widely used JavaScript package manager
2. **webpack** - Dominant production bundler
3. **GitHub Actions** - Default CI/CD for GitHub projects
4. **TypeScript Compiler** - Essential for TypeScript projects
5. **Babel** - Universal JavaScript transpiler
6. **Gradle** - Standard Android/JVM build tool
7. **Cargo** - Rust's package manager
8. **Poetry** - Python dependency management
9. **Terraform** - Infrastructure as Code standard
10. **Ansible** - Configuration management leader

---

## Notes

- **llms-txt files:** Documentation follows the `llms.txt` standard for LLM consumption
- **github-scraped:** Direct Git repository extractions
- **web-scraped:** HTML-to-Markdown conversions
- Many missing tools (especially npm, webpack, Gradle) likely have `llms.txt` endpoints and could be quickly added
