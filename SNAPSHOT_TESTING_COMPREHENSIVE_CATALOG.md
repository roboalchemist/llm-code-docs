# Snapshot Testing Libraries and Frameworks - Comprehensive Catalog

Complete compilation of snapshot testing tools, libraries, and frameworks across programming languages and ecosystems (2025-2026).

## Table of Contents

1. [JavaScript/TypeScript Ecosystems](#javascripttypescript-ecosystems)
2. [Python](#python)
3. [Go](#go)
4. [Rust](#rust)
5. [Java](#java)
6. [C# / .NET](#c-net)
7. [Ruby](#ruby)
8. [PHP / Laravel](#php-laravel)
9. [Visual & Image Snapshot Testing](#visual--image-snapshot-testing)
10. [Cross-Language Tools (Approval Tests)](#cross-language-tools-approval-tests)
11. [Other Languages](#other-languages)

---

## JavaScript/TypeScript Ecosystems

### Built-in Snapshot Support

| Tool | Framework Support | Key Features | Status |
|------|------------------|--------------|--------|
| **Jest** | React, Angular, Vue, Node.js | Built-in snapshots, code coverage, mock functions; Reference implementation for snapshot testing | Stable/Active |
| **Vitest** | React, Vue, Angular, Svelte | Jest-compatible, fast, TypeScript-first, built-in snapshots | Stable/Active |
| **Bun** | All frameworks via Bun test runner | Jest-compatible test runner with `toMatchSnapshot()` method | Stable/Active |
| **Japa** | Node.js, Express, AdonisJS | Via `@japa/snapshot` plugin, TypeScript support, VS Code integration | Stable/Active |
| **Node-Tap** | Node.js | Test-Anything Protocol (TAP), includes snapshot support + fixtures + mocking | Stable/Active |

### Plugin-Based Snapshot Support

| Tool | Framework | Plugin | Key Features | Status |
|------|-----------|--------|--------------|--------|
| **Mocha** | Node.js, Browser | snap-shot-it | BDD framework with snapshot plugin | Stable/Active |
| **Cypress** | E2E Testing | @cypress/snapshot | Official Cypress snapshot plugin | Stable/Active |

### Snapshot Libraries Without Framework

| Tool | Purpose | Key Features | Status |
|------|---------|--------------|--------|
| **snap-shot-it** | JavaScript/Node.js | Adds snapshot testing to BDD frameworks like Mocha | Stable/Active |
| **Approval Tests** | Multi-language | JavaScript support for approval testing workflows | Stable/Active |

### Note on Jest Alternatives

- **Jasmine** - BDD framework, lacks native snapshot support
- **Minitest** - Ruby framework, not applicable to JavaScript

---

## Python

### Core Snapshot Testing Libraries

| Tool | Test Framework | Key Features | Status |
|------|----------------|--------------|--------|
| **Syrupy** | pytest | Human-readable serialization, dataclass/custom object support, interactive review tool, 23-hour cache | Stable/Active |
| **pytest-snapshot** | pytest | Customizable snapshot file paths, one snapshot per file, flexible organization | Stable/Active |
| **pytest-insta** | pytest | Multiple formats (text, binary, hexdump, JSON, pickle), interactive review | Stable/Active |
| **snapshottest** | pytest | General snapshot testing for pytest | Stable/Active |

### Approval Tests

| Tool | Purpose | Key Features | Status |
|------|---------|--------------|--------|
| **approvaltests** | Python | Approval testing framework, complex output verification | Stable/Active |

---

## Go

### Snapshot Testing Libraries

| Tool | Key Features | Repository | Status |
|------|--------------|------------|--------|
| **Cupaloy** | Simple snapshot testing, automatic file management, go-spew for pretty-printing | github.com/bradleyjkemp/cupaloy | Stable/Active |
| **go-snaps** | Jest-inspired, multiple matchers (`MatchSnapshot()`, `MatchJSON()`, `MatchYAML()`), JSON/YAML files | github.com/gkampitakis/go-snaps | Stable/Active |
| **go.followtheprocess.codes/snapshot** | testdata directory organization, auto-update flag, cleanup unused snapshots | pkg.go.dev/go.followtheprocess.codes/snapshot | Stable/Active |

---

## Rust

### Snapshot Testing Libraries

| Tool | Key Features | Serialization Formats | Status |
|------|--------------|----------------------|--------|
| **Insta** | Most popular, CLI tool (`cargo insta`), inline snapshots, comprehensive review features | CSV, JSON, TOML, YAML, RON via Serde | Stable/Active |
| **expect-test** | Minimal/lightweight, macro-based (`expect!`), inline snapshots in source code | Source code inline | Stable/Active |
| **Runt** | Binary snapshot testing, transcript tests | N/A | Active |

---

## Java

### Snapshot Testing Libraries

| Tool | Frameworks | Key Features | Status |
|------|------------|--------------|--------|
| **snapshot-tests** | JUnit5, JUnit4 | Java 11+, multiple formats (text, JSON, XML, HTML), snapshot persistence | Stable/Active |
| **Approval Tests** | JUnit5, JUnit4, TestNG | Complex output verification, cross-language support | Stable/Active |
| **AssertJ** | JUnit5, JUnit4 | Assertion library with snapshot capabilities | Stable/Active |

### Note
Traditional frameworks like TestNG, Mockito, JBehave, Serenity, and Spock exist in the Java ecosystem but lack dedicated snapshot testing features.

---

## C# / .NET

### Snapshot Testing Libraries

| Tool | Test Frameworks | Key Features | Approach | Status |
|------|-----------------|--------------|----------|--------|
| **Verify** | xUnit, NUnit, MSTest | Most popular, specialized extensions (AspNetCore, WinForms, Xaml), embedded interactivity | File-based | Stable/Active |
| **Snapshooter** | xUnit, NUnit, MSTest | Jest-inspired, minimal setup, snapshot comparison | File-based | Stable/Active |
| **Storm Petrel** | xUnit, NUnit, MSTest | Code-based baselines via .NET Incremental Generators, traditional test approach | Code-based | Stable/Active |

### Visual Testing

| Tool | Purpose | Key Features | Status |
|------|---------|--------------|--------|
| **VisualCeption** | PHP-based (Codeception), visual regression detection | HTML reporting, flexible configuration | Active |

---

## Ruby

### RSpec Libraries

| Tool | Framework | Key Features | Snapshot Format | Status |
|------|-----------|--------------|-----------------|--------|
| **rspec-snapshot** | RSpec | `match_snapshot` and `snapshot` matchers, Jest-inspired, custom serializers, Rails view support | `.snap` files | Stable/Active |
| **snapshot_testing** | RSpec, Minitest, Test::Unit | Framework-agnostic, human-readable snapshots, custom serializers (YAML, etc.) | `.snap` files | Stable/Active |

### Minitest Libraries

| Tool | Framework | Key Features | Status |
|------|-----------|--------------|--------|
| **snapshot_testing** | Minitest, Test::Unit | Via `assert_snapshot` method, included in SnapshotTesting::Minitest | Stable/Active |
| **minitest-snapshots** | Minitest 5+ | Jest-style snapshot testing for Minitest | Stable/Active |

---

## PHP / Laravel

### PHPUnit-based

| Tool | Key Features | Framework | Status |
|------|--------------|-----------|--------|
| **spatie/phpunit-snapshot-assertions** | JSON/text/YAML/image snapshots, multiple assertion types, JsonDriver support | PHPUnit | Stable/Active |
| **Astrotomic/pest-plugin-laravel-snapshots** | Laravel HTTP test snapshots, built on phpunit-snapshot-assertions | Pest, Laravel | Stable/Active |

### Pest Framework Plugins

| Tool | Key Features | Status |
|------|--------------|--------|
| **pestphp/pest-plugin-snapshots** | `expect($data)->toMatchSnapshot()` syntax, `tests/.pest/snapshots` directory, `--update-snapshots` flag | Stable/Active |

### Specialized Laravel

| Tool | Purpose | Key Features | Status |
|------|---------|--------------|--------|
| **grazulex/laravel-snapshot** | Eloquent model tracking | Audit trails, data recovery, debugging, version control, analytics, CLI commands | Production-ready |

---

## Visual & Image Snapshot Testing

### Commercial Solutions

| Tool | Purpose | Key Features | Best For |
|------|---------|--------------|----------|
| **Percy** (BrowserStack) | Visual regression testing | AI-powered Visual Engine, CI/CD integration, team review dashboard, parallelized environments | Enterprise visual testing |
| **Chromatic** | Visual testing platform | TurboSnap (81% acceleration), 2K tests in <2 min, performance-tuned | Component visual testing |
| **Applitools** | Visual AI testing | AI-powered analysis, cross-browser testing, mobile support | Complex visual testing |

### Open-Source Solutions

| Tool | Purpose | Key Features | Status |
|------|---------|--------------|--------|
| **BackstopJS** | Visual regression testing | Automated screenshot capture/comparison, multiple browsers, viewport sizes, HTML reports | Stable/Active |
| **jest-image-snapshot** | Image comparison for Jest | Jest matcher for UI screenshots, pixel-level comparison | Stable/Active |
| **Playwright** | E2E testing with visual snapshots | `await expect(page).toHaveScreenshot()`, cross-platform, cross-browser | Stable/Active |
| **Testplane** | Visual regression detection | Multiple diff modes, TypeScript support, auto-wait, retries | Stable/Active |

### Framework-Specific Visual Testing

| Tool | Framework | Integration | Status |
|------|-----------|-------------|--------|
| **Ladle** | React components | Visual snapshots integration with Playwright | Stable/Active |
| **Storybook** | Component library | Native snapshot testing support for stories | Stable/Active |

---

## Cross-Language Tools (Approval Tests)

### Approval Tests Framework

**ApprovalTests** is an open-source assertion/verification library designed for approval-based testing across multiple languages.

| Language | Package | Repository | Status |
|----------|---------|-----------|--------|
| **.NET / C#** | ApprovalTests.Net | github.com/approvals/ApprovalTests.Net | Stable/Active |
| **Python** | approvaltests | pypi.org/project/approvaltests/ | Stable/Active |
| **JavaScript** | Approval Tests | github.com/approvals/ApprovalTests.JavaScript | Stable/Active |
| **Java** | ApprovalTests | Java implementation | Stable/Active |
| **C++** | ApprovalTests | C++ implementation | Stable/Active |
| **Multiple** | ApprovalTests (main) | approvaltests.com | Ecosystem hub |

### Use Cases for Approval Tests

- Long strings and large arrays
- Complex data structures and objects
- Dictionaries and collections
- Log file comparisons
- Non-deterministic outputs (UI, graphics)
- Legacy code refactoring ("software vise")

---

## Other Languages

### C++ / C
- Approval Tests (C++ implementation)
- Catch2 (testing framework with snapshot potential)

### Zig
- **Snapshot testing tools** referenced in community (kristoff.it/blog/dead-simple-snapshot-testing/)
- Limited dedicated snapshot libraries; primarily using general testing frameworks

### Additional Languages
- ApprovalTests available across 20+ programming languages
- Most modern testing frameworks increasingly include or support snapshot testing via plugins

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Total tools and libraries | 50+ |
| Languages/ecosystems covered | 12+ |
| JavaScript/TypeScript tools | 8 |
| Python libraries | 5 |
| Visual testing tools | 8 |
| Approval Tests implementations | 6+ |
| Cross-framework solutions | 3 |

---

## Key Trends (2025-2026)

1. **Jest remains dominant** for JavaScript/TypeScript snapshot testing
2. **Vitest gaining popularity** as modern Jest alternative with better performance
3. **Visual snapshot testing maturation** with tools like Percy and Chromatic
4. **Approval Tests expanding** across more language ecosystems
5. **Framework integration** increasing (built-in support rather than plugins)
6. **AI-powered visual comparison** emerging (Applitools, Percy AI Engine)
7. **Inline snapshots** gaining traction (Insta in Rust, expect-test, Storm Petrel in .NET)

---

## Research Sources

- Jest Documentation: https://jestjs.io
- Vitest: https://vitest.dev
- Insta (Rust): https://insta.rs
- Verify (.NET): https://github.com/VerifyTests/Verify
- ApprovalTests: https://approvaltests.com
- Percy: https://percy.io
- Chromatic: https://www.chromatic.com
- Syrupy (Python): https://github.com/syrusakbary/syrupy
- spatie/phpunit-snapshot-assertions: https://github.com/spatie/phpunit-snapshot-assertions

---

**Last Updated**: January 1, 2026
**Research Method**: Perplexity AI research + Tavily web search + community documentation
