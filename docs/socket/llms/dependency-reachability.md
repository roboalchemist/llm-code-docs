# Source: https://docs.socket.dev/docs/dependency-reachability.md

# Dependency Reachability

Dependency Reachability filters out unreachable alerts by constructing a dependency graph.

> 📘 See [Reachability Analysis](https://docs.socket.dev/docs/reachability-analysis) for an overview of all Reachability Analysis capabilities in Socket. This page is about just one of the reachability techniques that Socket offers.

Dependency reachability identifies unused (dead) packages by building a graph of how packages import each other. Although it’s the simplest form of reachability analysis, it has a major advantage: it can help prioritize nearly all types of alerts in Socket, not just vulnerability-related ones like [Tier 2 and Tier 1](reachability-analysis#reachability-maturity-levels) reachability.

## How Dependency Reachability Works

### 1. From Manifest to Map

The analysis scans your manifest files (`package.json`, `go.mod`, `Gemfile`, `pom.xml`, `build.gradle`, and others) to generate a complete list of direct and transitive dependencies, along with the dependency graph that connects them.

### 2. Dependency-Only Scanning — No Access to Your Source Code

For each supported language, Socket parses only the files from dependency packages—**never** your proprietary source code—and extracts every import statement (e.g., `import`, `require`, or `using`).

| Language                | Parser                 | Example we catch                   |
| ----------------------- | ---------------------- | ---------------------------------- |
| JavaScript / TypeScript | tree‑sitter‑javascript | `import { useState } from 'react'` |
| Python                  | tree‑sitter‑python     | `from pathlib import Path`         |
| Go                      | tree‑sitter‑go         | `import "github.com/user/project"` |
| Ruby                    | tree‑sitter‑ruby       | `require 'net/http'`               |
| Java                    | tree‑sitter‑java       | `import javax.sql.DataSource;`     |

> Privacy first: Your source code is never uploaded or stored. The scan runs in a secure worker, extracts only the package names, and immediately discards the file contents.

### 3. Dead vs. Alive

If a transitive package never appears in any import statement, Socket marks it as dead. Then, it walks the dependency graph in the following way:

* If a parent is marked as dead, its children are also marked as dead—*unless* they are also required by a live parent.
* Direct dependencies are **always** considered alive, since the analysis doesn’t scan application source code to determine how it interacts with its direct dependencies.

The result is a clear “used” or “unused” status for every transitive package.

## What You’ll See in the Product

### Filter CVEs by *Used* Dependencies

In the **Vulnerabilities** tab you’ll find the toggle: **Used dependencies only**. Flip it on and watch the noise disappear—CVE counts drop to only the libraries that actually execute in your application.

<Image align="center" src="https://files.readme.io/8910423fcbec05e897e0f7f624f15de0f51e428bb03d54ccd5dd64543a09aed5-dependency_use.jpg" />

### Enabling the Feature

Dependency Reachability is already enabled by default for users on the free tier—no action needed. For paid plans, it’s currently opt-in via the **Settings** page. We’ve kept it optional during the beta since the additional source-code scan can add a small delay to SBOM generation. After the beta, Reachability will be enabled by default for all plans, with a toggle available if you prefer to turn it off. No additional configuration or build steps required.

<Image align="center" src="https://files.readme.io/2ce0515a3d5854111ddbff718eb230aae9dba86bea9fa49797f4c607bacda15d-dependency_reachability_setting.jpg" />

When you enable Reachability, you'll see a significant reduction in noise—on average, **25–35% of transitive dependencies are filtered out** as unused. That means fewer alerts, fewer false positives, and a shorter list of vulnerabilities to triage.