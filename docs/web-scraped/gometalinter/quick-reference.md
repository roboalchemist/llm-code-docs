# gometalinter Quick Reference

## Source: https://github.com/alecthomas/gometalinter

## Installation

```bash
brew install gometalinter      # macOS
go get gopkg.in/alecthomas/gometalinter.v1  # From source
curl -L https://git.io/vp6lP | sh  # Automatic installer
```

## One-Line Commands

```bash
# Basic lint
gometalinter ./...

# Lint with strict settings
gometalinter --deadline=2m --severity=error ./...

# Generate Checkstyle XML for CI
gometalinter --checkstyle ./... > report.xml

# Only specific linters
gometalinter --disable-all --enable=vet --enable=golint ./...

# Exclude patterns
gometalinter --exclude=vendor ./...

# List available linters
gometalinter --list-linters
```

## Common Configuration

Save as `.gometalinter.json`:

```json
{
  "enable": ["vet", "golint", "errcheck", "staticcheck"],
  "skip-dirs": ["vendor"],
  "deadline": "1m"
}
```

Then run:
```bash
gometalinter ./...
```

## Default Enabled Linters

| Linter | Purpose |
|--------|---------|
| vet | Official static analyzer |
| gotype | Syntactic/semantic analysis |
| deadcode | Finds unused code |
| gocyclo | Cyclomatic complexity |
| golint | Style issues |
| errcheck | Unchecked errors |
| staticcheck | Advanced static analysis |
| gosec | Security issues |
| misspell | Spelling errors |
| unconvert | Unnecessary type conversions |

## Common Flags

| Flag | Purpose |
|------|---------|
| `--deadline=5m` | Set timeout |
| `--enable=NAME` | Enable specific linter |
| `--disable=NAME` | Disable specific linter |
| `--checkstyle` | XML output for CI |
| `--json` | JSON output |
| `--exclude=PATTERN` | Skip files matching pattern |
| `--severity=warning` | Report warnings (default: errors only) |

## Suppress Warnings

Inline suppression:

```go
// nolint
var unused string

// nolint: misspell
const commond = "typo"
```

Per-directory in config:

```json
{
  "skip-dirs": ["vendor", "build"]
}
```

## CI/CD Quick Setup

GitHub Actions:
```yaml
- run: go install gopkg.in/alecthomas/gometalinter.v1@latest
- run: gometalinter --install
- run: gometalinter --deadline=5m ./...
```

## Alias for Development

Add to `.bashrc` or `.zshrc`:

```bash
alias gmt="gometalinter --deadline=30s"
alias gmt-check="gometalinter --deadline=10s --enable=vet --enable=golint"
alias gmt-strict="gometalinter --deadline=5m ./..."
```

## Useful Patterns

### Check Only Modified Files (Git)

```bash
gometalinter $(git diff master --name-only | grep '\.go$' | xargs dirname | sort -u)
```

### Check Package Recursively

```bash
gometalinter ./...
```

### Check Single Package

```bash
gometalinter ./mypkg
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | No issues |
| 1 | Issues found |
| 2 | Error |

## Resources

- **GitHub**: https://github.com/alecthomas/gometalinter
- **pkg.go.dev**: https://pkg.go.dev/gopkg.in/alecthomas/gometalinter.v1
- **Status**: DEPRECATED (use golangci-lint instead)

## Migration to golangci-lint

Since gometalinter is deprecated, migrate to:

```bash
brew install golangci-lint
golangci-lint run ./...
```

See main documentation for migration details.
