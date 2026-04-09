# DeepScan Overview

# Source: https://deepscan.io

DeepScan is a semantic JavaScript analyzer that detects runtime errors and code quality issues using advanced static code analysis with data-flow capabilities.

## What is DeepScan?

DeepScan is a **static code analysis service** for JavaScript and TypeScript projects that goes beyond traditional linters like ESLint. It performs **semantic analysis** using data-flow analysis to identify potential runtime errors and quality issues that syntax-based tools typically miss.

### Key Characteristics

- **Data-flow Analysis**: Traces how data flows through code to detect issues like null pointer dereferences and type mismatches
- **Runtime Error Detection**: Identifies code that might throw exceptions at runtime or cause unintended execution
- **Code Quality Analysis**: Focuses on readability, reusability, and refactorability rather than coding conventions
- **Semantic Understanding**: Goes beyond style checking to understand what code actually does

## Supported Technologies

DeepScan provides analysis for:
- **JavaScript** (all modern ECMAScript specifications)
- **TypeScript**
- **React** (with 50+ framework-specific rules)
- **Vue.js** (with 60+ framework-specific rules)
- **Node.js** (CommonJS and require() patterns)
- **Astro** framework
- **Web Standards**: DOM APIs and browser APIs

## Key Differentiators

DeepScan is ideal if you are serious about JavaScript code quality. Unlike traditional linters that focus on code style and conventions, DeepScan emphasizes:

1. **Runtime Error Prevention**: Detects actual bugs that could crash code at runtime
2. **Deep Semantic Analysis**: Understands execution flow, type implications, and data dependencies
3. **Reduced False Positives**: Uses impact classification to minimize noise and false alarms
4. **Framework-Aware**: Specialized rules for React, Vue.js, and Node.js patterns

## Core Analysis Categories

### Error Rules (200+ rules)
Code which might throw an exception at runtime or cause unintended execution:
- Null pointer dereference (NULL_POINTER)
- Type mismatches and coercion errors
- Missing operators or statements
- Unreachable code
- Regular expression issues
- Event listener problems

### Code Quality Rules (80+ rules)
Code which should be more readable, reusable, and refactorable:
- Dead code and unused variables
- Constant conditions
- Identical branch implementations
- Loop inefficiencies
- Unnecessary complexity

## Standards Alignment

DeepScan rules map to **Common Weakness Enumeration (CWE)** standards, addressing vulnerabilities including:
- **CWE-476**: Null Pointer Dereference
- **CWE-628**: Incorrect Function Arguments
- **CWE-843**: Type Confusion
- And many others related to security and code quality

## Platform Architecture

### Browser-Based & CI-Integrated
DeepScan operates as both:
- A **browser-based service** accessible from the web
- A **CI/CD-integrated tool** for automated analysis in pipelines

### GitHub Integration
- Native GitHub integration with automatic repository synchronization
- Pull request code review with inline comments
- Continuous monitoring as commits are pushed
- Support for both public and private repositories

### Issue Tracking
- Automatically tracks issues over time despite code changes
- Merges issues intelligently to follow them across refactoring
- Displays when issues were first detected
- Shows fixed issues with original code snippets

### Project Grading System
DeepScan assigns simple project grades based on detected issues and their impact:
- **Poor**: Significant code quality issues detected
- **Normal**: Acceptable code quality with some issues
- **Good**: High code quality with minimal issues

This grading mechanism motivates teams to maintain and improve code quality continuously.

## Integration Options

### Editor Plugins
- **Visual Studio Code** extension
- **IntelliJ** integration

### CI/CD & Infrastructure
- **SonarQube** server integration for on-premises analysis
- **Command-line interface** for automated testing
- **GitHub Marketplace** billing integration
- **Enterprise deployment** options

## Team Collaboration

DeepScan provides a **Team Collaboration Dashboard** where:
- Teams configure their organization and add GitHub repositories
- Get "an overall picture of your team regarding its quality status, code issues and lines of code"
- Monitor code quality metrics as commits are pushed
- Track team-wide quality trends over time
- Manage team members and permissions

## User Base

DeepScan is trusted by thousands of teams, including notable organizations like **Samsung SDS** and other enterprise companies focused on code quality.

---

**Learn More**: Visit [deepscan.io](https://deepscan.io) for more information.
