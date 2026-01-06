# Revive - Fast Go Linter Documentation

## Overview

**Revive** is a fast, configurable linter for Go with 60+ style rules. It serves as a modern replacement for the deprecated `golint`, providing flexible static code analysis for Go projects.

- **Official Website**: https://revive.run
- **GitHub Repository**: https://github.com/mgechev/revive
- **Primary Language**: Go
- **Purpose**: Static code analysis and linting

## Key Features

- **Fast**: Highly performant linting written in Go
- **Configurable**: Extensive customization via TOML configuration files
- **60+ Rules**: Comprehensive set of built-in style and code quality rules
- **Drop-in Replacement**: Direct replacement for the deprecated golint
- **Multiple Output Formats**: Support for various formatter options
- **Custom Rules**: Ability to define and integrate custom linting rules
- **Integration**: Works with golangci-lint and other Go tooling

## Getting Started

### Installation

```bash
# Using go install (recommended)
go install github.com/mgechev/revive@latest

# Using Docker
docker run ghcr.io/mgechev/revive:latest

# Manual binary download
# Visit https://github.com/mgechev/revive/releases
```

### Basic Usage

```bash
# Lint current directory
revive ./...

# Lint with specific config
revive -config revive.toml ./...

# Use specific formatter
revive -formatter json ./...

# Exclude files
revive -exclude file1.go -exclude file2.go ./...
```

## Configuration

Revive uses TOML configuration files (typically named `revive.toml` or `.revive.toml`).

### Configuration Example

```toml
# Enable all rules by default
ignoreFailures = false

# Comma-separated list of rules to enable
enableAllRules = false

# Rules configuration
[rule.blank-imports]
enabled = true

[rule.context-keys-type]
enabled = true

[rule.cyclomatic]
enabled = true
arguments = [3]

[rule.early-return]
enabled = true

[rule.error-naming]
enabled = true

[rule.error-return]
enabled = true
```

### Default Configuration

Revive provides a default configuration file (`defaults.toml`) with sensible defaults for most projects. You can customize this by creating a `revive.toml` file in your project root.

## Available Rules

Revive includes 60+ built-in rules covering:

- **Code Quality**: cyclomatic complexity, cognitive complexity, nesting levels
- **Naming Conventions**: variable naming, function naming, package naming
- **Error Handling**: proper error returns, unused error values
- **Best Practices**: early return, blank imports, context usage
- **Documentation**: exported function documentation, comment formatting
- **Performance**: unused parameters, inefficient code patterns
- **Style**: code formatting, consistency, readability

See the official documentation for the complete list of rules and their configurations.

## Output Formatters

Revive supports multiple output formats:

- **Default**: Human-readable text format
- **JSON**: Structured JSON output for tool integration
- **SARIF**: Standard analysis result interchange format
- **Checkstyle**: XML format compatible with CI/CD tools
- **Tab**: Tab-separated values for script processing

Example:
```bash
revive -formatter json ./... > lint-results.json
revive -formatter sarif ./... > results.sarif
```

## Integration with Other Tools

### golangci-lint

Revive is integrated into golangci-lint, making it easy to use within your existing Go toolchain:

```bash
golangci-lint run
# Uses revive as one of the configured linters
```

### IDE Integration

- **GoLand**: Native support via Revive configuration
- **VS Code**: Via Go extension with Revive support
- **Vim**: Via vim-go or similar plugins

### CI/CD Integration

Revive can be easily integrated into your CI/CD pipeline:

```yaml
# GitHub Actions example
- name: Run Revive Linter
  run: |
    go install github.com/mgechev/revive@latest
    revive -config revive.toml -formatter sarif ./... > results.sarif

- name: Upload SARIF results
  uses: github/codeql-action/upload-sarif@v2
  with:
    sarif_file: results.sarif
```

## Configuration Best Practices

1. **Start with defaults**: Use the default configuration as a base
2. **Customize incrementally**: Enable/disable rules as needed for your project
3. **Document your choices**: Add comments to your revive.toml explaining why certain rules are configured
4. **Team agreement**: Ensure team consensus on linting rules
5. **Version control**: Commit revive.toml to ensure consistent linting across developers

## Troubleshooting

### Rule not enabled

Check that the rule is:
1. Listed in your `revive.toml` with `enabled = true`
2. Not in the exclude list
3. Spelled correctly

### Performance issues

If Revive runs slowly:
1. Check for unnecessary exclusions
2. Consider using rule filtering for development
3. Enable only the rules your project needs

### Configuration not applied

- Ensure the config file is named correctly (`revive.toml` or `.revive.toml`)
- Use the `-config` flag to explicitly specify the configuration file path
- Check for TOML syntax errors in your configuration

## Command-Line Flags

Key command-line options:

```
-config FILE           Path to config file
-formatter STRING      Output formatter (default: "default")
-exclude PATTERN       Exclude files/paths
-ignore RULE           Disable specific rules
-enable-all-rules      Enable all available rules
-max-open-files INT    Maximum open files
-tmp-dir DIR          Temporary directory for analysis
```

## Resources

- **Official Website**: https://revive.run
- **GitHub Repository**: https://github.com/mgechev/revive
- **Issue Tracker**: https://github.com/mgechev/revive/issues
- **Discussions**: https://github.com/mgechev/revive/discussions
- **Releases**: https://github.com/mgechev/revive/releases

## Related Tools

- **golangci-lint**: Comprehensive Go linter that includes Revive
- **gofmt**: Go code formatter
- **go vet**: Official Go analysis tool
- **staticcheck**: Additional static analysis for Go

## Version Information

Revive is actively maintained and regularly updated. Check the GitHub releases page for the latest version and changelog.

---

*Documentation source: https://revive.run and https://github.com/mgechev/revive*
