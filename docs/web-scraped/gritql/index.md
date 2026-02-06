# Source: https://docs.grit.io

# Grit - Declarative Code Search and Transformation

- Grit - Declarative Code Search and Transformation- - **Documentation**GitHubDiscordBlogTutorialPlaygroundDocsGetting Started
OverviewCLI QuickstartCLI ReferencePattern LibraryConfigLanguage
OverviewTutorialPatternsConditionsPattern ModifiersTarget LanguagesBubble and ScopingDefining PatternsFunctionsCommon IdiomsSyntax ReferenceTesting GritQLGuides
Continuous IntegrationAuthoring GritQLImportsVS CodeSharing Patterns
# GritQL
GritQL is a declarative query language for searching and modifying source code.

## Why GritQL?
- 📖 **Start simply** without learning AST details: any code snippet is a valid GritQL query
- ⚡️ **Scale to millions of lines** using Rust and query optimization for repositories with 10M+ lines
- 📦 **Reuse patterns** with Grit&#x27;s built-in module system to access 200+ standard patterns or share your own
- ♻️ **Works everywhere**: use GritQL to rewrite JavaScript/TypeScript, Python, JSON, Java, Terraform, Solidity, CSS, Markdown, YAML, Rust, Go, or SQL
- 🔧 **Auto-fix built in**: GritQL makes it easy to include auto-fix rules for faster remediation

## Quick Example
Search for patterns using backticks and metavariables (like `$msg`):
grit apply &#x27;`console.log($msg)` => `winston.log($msg)`&#x27;Save patterns to enforce as custom lints, with powerful where clauses to exclude specific cases:
`console.log($msg)` => `winston.log($msg)` where {
  $msg <: not within or { `it($_, $_)`, `test($_, $_)` }
}
## Use Cases
GritQL excels at automating:
- **Large-scale migrations** - Migrate APIs, frameworks, or refactor codebases across millions of lines
- **Custom linting** - Enforce team-specific code standards and best practices
- **Code quality improvements** - Systematically improve code quality with consistent patterns
- **Dependency upgrades** - Handle breaking changes when upgrading dependencies
Interactive Tutorial
Learn GritQL step-by-step
Language Reference
Complete GritQL documentation
CLI Quickstart
Install and use the Grit CLI