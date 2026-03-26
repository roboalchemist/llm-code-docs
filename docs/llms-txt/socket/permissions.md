# Source: https://docs.socket.dev/docs/permissions.md

# GitHub App Permissions

What permissions does Socket for GitHub require?

Socket is designed to work without the need to analyze, upload, or share your source code.

* The only files we collect from your repository are **dependency manifests, lockfiles, and related configuration files** — collectively called the *dependency snapshot*. We use the dependency snapshot to determine the packages used by your repository, perform our open source risk analysis, and produce a report.

* **We never read, collect, or analyze your source code.** Although the GitHub App requests read access to repository contents, this is solely because GitHub's permissions model does not support granting access to specific file patterns. We use this access only to retrieve the file tree listing (names and paths) and then download only the specific file types listed below. All other files are filtered out before any content is fetched.

### Files collected by ecosystem

| Ecosystem               | Files                                                                                                                                                                                                 |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **npm**                 | `package.json`, `package-lock.json`, `npm-shrinkwrap.json`, `yarn.lock`, `pnpm-lock.yaml`/`.yml`, `pnpm-workspace.yaml`/`.yml`, `rush.json`                                                           |
| **Python (PyPI)**       | `pyproject.toml`, `poetry.lock`, `uv.lock`, `pylock.toml`/`pylock.*.toml`, `Pipfile`, `Pipfile.lock`, `setup.py`, `requirements.txt` (and variants like `requirements-dev.txt`, `requirements/*.txt`) |
| **Java (Maven/Gradle)** | `pom.xml`, `*.gradle`, `*.gradle.kts`, `gradle.lockfile`, `build.sbt`, `ivy.xml`, `project.clj`, `Buildfile`                                                                                          |
| **Go**                  | `go.mod`, `go.sum`                                                                                                                                                                                    |
| **Ruby (RubyGems)**     | `Gemfile.lock`                                                                                                                                                                                        |
| **Rust (Cargo)**        | `Cargo.toml`, `Cargo.lock`                                                                                                                                                                            |
| **.NET (NuGet)**        | `*.sln`, `*.*proj`, `*.nuspec`, `*.props`, `*.targets`, `*.projitems`, `packages.config`, `packages.lock.json`                                                                                        |
| **PHP (Composer)**      | `composer.json`, `composer.lock`                                                                                                                                                                      |
| **Swift**               | `Package.swift` (including version-specific variants like `Package@swift-5.9.swift`), `Package.resolved`                                                                                              |
| **SBOM formats**        | CycloneDX (`bom.json`, `bom.xml`, `cyclonedx.json`, `cyclonedx.xml`, and variants), SPDX (`*.spdx.json`)                                                                                              |
| **GitHub Actions**      | `.github/workflows/*.yml`/`.yaml`, `.github/workflow.yml`/`.yaml`, `action.yml`/`.yaml`                                                                                                               |
| **Socket**              | `*.socket.facts.json`                                                                                                                                                                                 |