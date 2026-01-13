# SonarTS - TypeScript Static Code Analyzer

## Overview

**SonarTS** is a legacy static code analyzer for TypeScript developed by SonarSource. It detects bugs, code smells, and security vulnerabilities in TypeScript code.

## Current Status

**DEPRECATED AND ARCHIVED** - SonarTS is no longer actively maintained as a standalone tool.

- **Repository Status**: Archived on April 27, 2021
- **Final Release**: SonarTS 2.1 (November 15, 2019)
- **GitHub Repository**: https://github.com/SonarSource/SonarTS (read-only)

### Why SonarTS is Archived

SonarSource has consolidated TypeScript analysis into a unified **JavaScript/TypeScript analyzer** that is now part of modern SonarQube and SonarCloud. The SonarTS 2.1 release explicitly disables TypeScript analysis to direct users to the modern integrated solution.

## Migration Path

If you are currently using SonarTS, migrate to:

- **SonarCloud**: Cloud-based version for GitHub, GitLab, Bitbucket, or Azure DevOps
- **SonarQube**: Self-hosted on-premises solution

Both platforms provide comprehensive JavaScript/TypeScript analysis with:
- Advanced bug detection using AST analysis
- Data-flow-based security vulnerability detection
- Dead code and code smell detection
- Coverage reporting
- Security hotspot identification
- AI-powered code fix suggestions

## Features (Historical)

SonarTS provided sophisticated analysis for TypeScript code:

### Analysis Techniques
- **AST-based Rules**: Structural analysis for code pattern detection
- **Live Variable Analysis**: Dead store detection
- **Symbolic Execution**: Data-flow-related bug detection
- **Copy-Paste Detection**: Identifies duplicated code blocks
- **API Misuse Detection**: Catches common API usage errors

### Key Rules
- `no-all-duplicated-branches` - Detects redundant branches
- `no-identical-expressions` - Finds logically identical expressions
- Dead store detection
- Unused variable detection
- Type safety violations

## Installation (Legacy)

For historical reference, SonarTS was available as a SonarQube plugin. To use the final version:

```bash
# Download SonarTS 2.1 plugin JAR
# Place in SonarQube extensions/plugins directory
# Restart SonarQube server
```

However, **new installations should use SonarCloud or modern SonarQube** instead.

## Configuration

Historic SonarTS configuration via `sonar-project.properties`:

```properties
sonar.projectKey=my.project
sonar.projectName=My Project
sonar.sources=src
sonar.language=ts
```

Modern equivalent in SonarCloud/SonarQube uses the same properties format.

## Analysis Examples

### Detecting Dead Code
SonarTS can identify unreachable code:

```typescript
// Dead store example
function process(value: number): void {
  let result = value * 2;  // Assigned but never used
  result = value * 3;       // Overwritten without being read
  console.log(value);       // Result never used
}
```

### Detecting Copy-Paste Errors
Finds duplicated code blocks that may hide bugs:

```typescript
// Duplicate logic that might be a mistake
if (condition1) {
  doSomething();
  processA();
  finalize();
}

if (condition2) {
  doSomething();
  processA();  // Same as above - potential copy-paste error
  finalize();
}
```

### Security Vulnerability Detection
Identifies potential security issues through data flow analysis:

```typescript
// SQL injection vulnerability pattern
const query = `SELECT * FROM users WHERE id = ${userId}`;
database.execute(query);
```

## Relationship to SonarJS

SonarTS functionality was eventually merged into **SonarJS**, which now provides unified analysis for:
- JavaScript
- TypeScript
- CSS

The SonarJS analyzer is part of modern SonarQube and SonarCloud distributions.

## Upgrading to Modern Solutions

### For SonarQube Users

1. Update to latest SonarQube LTS or current version
2. Built-in JavaScript/TypeScript analyzer is included
3. Remove old SonarTS plugin from extensions/plugins
4. Re-analyze your TypeScript projects

### For SonarCloud Users

1. No action required - JavaScript/TypeScript analysis is included
2. Connect your repository (GitHub, GitLab, Bitbucket, Azure DevOps)
3. Analysis starts automatically
4. Advanced features like AI CodeFix available with commercial license

## Documentation References

### Official SonarSource Documentation
- **SonarQube JavaScript/TypeScript Analysis**: https://docs.sonarsource.com/sonarqube/latest/analyzing-source-code/languages/javascript-typescript-css/
- **SonarCloud Documentation**: https://docs.sonarsource.com/sonarqube-cloud/

### Project Resources
- **GitHub Repository**: https://github.com/SonarSource/SonarTS
- **SonarTS Example Project**: https://github.com/SonarSource/SonarTS-example
- **Release Notes**: https://github.com/SonarSource/SonarTS/releases

## Comparison: SonarTS vs Modern Solutions

| Feature | SonarTS 2.1 | SonarQube/Cloud |
|---------|------------|-----------------|
| TypeScript Support | Yes (Archived) | Yes (Active) |
| JavaScript Support | Limited | Full |
| CSS Support | No | Yes |
| Security Hotspots | No | Yes |
| Data Flow Analysis | Yes | Enhanced |
| AI CodeFix | No | Yes (Premium) |
| SonarLint Integration | Limited | Full |
| IDE Support | No | VSCode, JetBrains, etc. |
| Continuous Updates | No | Yes |
| Community Support | Minimal | Active |

## Summary

SonarTS is a **legacy tool no longer recommended for new projects**. SonarSource has consolidated TypeScript analysis into modern solutions:

- **Use SonarCloud** for cloud-based analysis with GitHub, GitLab, Bitbucket, or Azure DevOps
- **Use SonarQube** for self-hosted enterprise analysis
- Both include comprehensive JavaScript/TypeScript analysis, security features, and modern tooling

If you're maintaining legacy SonarTS installations, plan a migration to these modern platforms for continued support and security updates.

## Source

This documentation is compiled from:
- SonarTS GitHub Repository: https://github.com/SonarSource/SonarTS
- SonarSource Official Documentation
- SonarTS Release Notes and Archive

Generated: 2026-01-08
