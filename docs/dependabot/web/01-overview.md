# Dependabot Overview

Source: https://docs.github.com/en/code-security/dependabot

## What is Dependabot?

Dependabot is GitHub's automated dependency management tool designed to help you maintain secure and up-to-date project dependencies. The service monitors vulnerabilities in your project's dependencies and enables automatic updates.

## Core Capabilities

### Vulnerability Detection

Dependabot identifies security vulnerabilities within your project's dependency ecosystem. It continuously scans your dependencies against known vulnerability databases to alert you to potential risks.

### Automated Updates

The tool offers two primary update mechanisms:

**Security Updates**: Automatically generates pull requests to address dependencies with known vulnerabilities. When a vulnerability is discovered, Dependabot can immediately propose fixes.

**Version Updates**: Maintains your dependencies at current versions through regular automated pull requests. This keeps your projects current beyond just security patches.

### Alert Management

Dependabot provides comprehensive alert handling including:
- Configuration of alert sensitivity and scope
- Auto-triage rules for intelligent alert prioritization
- Delegated dismissal workflows for team-based decision-making
- Customizable notifications

## The Three Dependabot Features

### 1. Dependabot Alerts

Informs you about vulnerabilities in the dependencies that you use in your repository. The system alerts users to every vulnerable dependency in the full dependency graph.

### 2. Dependabot Security Updates

Automatically generates pull requests when vulnerabilities are detected. When a Dependabot alert is raised for a vulnerable dependency in the dependency graph of your repository, Dependabot automatically tries to fix it by raising a pull request.

### 3. Dependabot Version Updates

"Takes the effort out of maintaining your dependencies" by automatically keeping packages current with their latest releases. Dependabot uses semantic versioning to determine when updates are available, then automatically raises pull requests to update manifests to the latest dependency versions.

## Ecosystem Support

Dependabot supports numerous package management ecosystems across different programming languages and platforms, enabling broad coverage for various project types. This includes:

- Python (pip)
- Node.js (npm, yarn)
- Ruby (bundler)
- Java (Maven, Gradle)
- Go (go modules)
- Rust (Cargo)
- PHP (Composer)
- .NET (NuGet)
- Docker
- Terraform
- And many others

## Integration Features

The platform integrates with GitHub's workflow systems, allowing you to:

- Automate dependency updates alongside your CI/CD pipelines
- Customize pull request behavior and formatting
- Configure access to private package registries
- Manage multi-ecosystem updates simultaneously
- Automatically sign commits
- Filter notifications to show only Dependabot pull requests

## Availability

Dependabot features are available for all repositories on GitHub across free, pro, and team plans.
