# gometalinter Configuration Guide

## Source: https://github.com/alecthomas/gometalinter

## Configuration File Locations

gometalinter looks for configuration files in this order:

1. `.gometalinter.json` (project root)
2. `.gometalinter.yaml` (project root)
3. Command-line specified config file (via `--config` flag)

## Configuration File Formats

### JSON Format (.gometalinter.json)

```json
{
  "linters": {
    "vet": {
      "command": "go vet",
      "pattern": "^(?P<path>.*?\\.go):(?P<line>\\d+): (?P<message>.*)"
    },
    "golint": {
      "command": "golint -set_exit_status",
      "pattern": "^(?P<path>.*?\\.go):(?P<line>\\d+):(?P<column>\\d+): (?P<message>.*)"
    }
  },
  "enable": [
    "vet",
    "gotype",
    "golint",
    "errcheck",
    "staticcheck",
    "gosec",
    "misspell",
    "unconvert"
  ],
  "disable": [
    "lll",
    "testify"
  ],
  "severity": "warning",
  "errors": false,
  "warnings": false,
  "skip-dirs": [
    "vendor",
    "build"
  ],
  "skip-files": [
    ".*\\.pb\\.go$"
  ],
  "deadline": "1m",
  "checkstyle": false,
  "json": false
}
```

### YAML Format (.gometalinter.yaml)

```yaml
linters:
  vet:
    command: go vet
    pattern: '^(?P<path>.*?\.go):(?P<line>\d+): (?P<message>.*)$'
  golint:
    command: golint -set_exit_status
    pattern: '^(?P<path>.*?\.go):(?P<line>\d+):(?P<column>\d+): (?P<message>.*)$'

enable:
  - vet
  - gotype
  - golint
  - errcheck
  - staticcheck
  - gosec
  - misspell
  - unconvert

disable:
  - lll
  - testify

severity: warning
errors: false
warnings: false

skip-dirs:
  - vendor
  - build
  - dist

skip-files:
  - .*\.pb\.go$
  - .*\.mock\.go$

deadline: 1m
checkstyle: false
json: false
```

## Configuration Options

### Top-Level Options

#### `linters` (object)
Defines custom linters and overrides for built-in linters.

```json
{
  "linters": {
    "my-custom-linter": {
      "command": "my-linter-command",
      "pattern": "^(?P<path>.*?\\.go):(?P<line>\\d+): (?P<message>.*)$"
    }
  }
}
```

**Linter Definition:**
- **command** - Shell command to run
- **pattern** - Regex pattern to parse output (must include named groups: `path`, `line`, `message`, optional: `column`, `severity`)

#### `enable` (array)
List of linters to enable by default.

```json
{
  "enable": ["vet", "golint", "errcheck", "staticcheck"]
}
```

**Default enabled linters:**
```
vet, gotype, deadcode, gocyclo, golint, errcheck, staticcheck,
gosec, misspell, unconvert
```

#### `disable` (array)
List of linters to disable.

```json
{
  "disable": ["lll", "testify", "gofmt"]
}
```

#### `severity` (string)
Minimum severity level to report.

- `error` - Report only errors (default)
- `warning` - Report errors and warnings

```json
{
  "severity": "warning"
}
```

#### `errors` (boolean)
Show only errors, filter out warnings.

```json
{
  "errors": true
}
```

#### `warnings` (boolean)
Show only warnings, filter out errors.

```json
{
  "warnings": true
}
```

#### `skip-dirs` (array)
Directories to skip during linting.

```json
{
  "skip-dirs": [
    "vendor",
    "build",
    "dist",
    "node_modules",
    ".git"
  ]
}
```

#### `skip-files` (array)
File patterns to skip (regex).

```json
{
  "skip-files": [
    ".*\\.pb\\.go$",
    ".*\\.mock\\.go$",
    ".*_test\\.go$"
  ]
}
```

#### `deadline` (duration)
Maximum time for all linters to complete.

```json
{
  "deadline": "5m"
}
```

Format: Go duration string
- `"300ms"` - 300 milliseconds
- `"5s"` - 5 seconds
- `"2m30s"` - 2 minutes 30 seconds

#### `checkstyle` (boolean)
Output results in Checkstyle XML format.

```json
{
  "checkstyle": true
}
```

#### `json` (boolean)
Output results as JSON.

```json
{
  "json": true
}
```

#### `format` (string)
Custom output format using Go template syntax.

```json
{
  "format": "{{.Path}}:{{.Line}}:{{.Column}}: {{.Message}} ({{.Linter}})"
}
```

**Available template variables:**
- `{{.Path}}` - File path
- `{{.Line}}` - Line number
- `{{.Column}}` - Column number
- `{{.Message}}` - Message text
- `{{.Linter}}` - Linter name
- `{{.Severity}}` - Error/warning severity

## Real-World Configuration Examples

### Strict Development Setup

```json
{
  "enable": [
    "vet",
    "golint",
    "errcheck",
    "staticcheck",
    "gosec",
    "misspell"
  ],
  "disable": ["lll"],
  "skip-dirs": ["vendor", "build"],
  "deadline": "30s",
  "severity": "error"
}
```

### CI/CD Pipeline Configuration

```json
{
  "enable": [
    "vet",
    "golint",
    "errcheck",
    "staticcheck",
    "gosec",
    "unconvert",
    "misspell"
  ],
  "disable": ["lll", "testify"],
  "skip-dirs": ["vendor", "build", "dist"],
  "skip-files": [".*_test\\.go$"],
  "deadline": "5m",
  "checkstyle": true,
  "severity": "warning"
}
```

### Lenient Development Configuration

```json
{
  "enable": ["vet", "golint"],
  "disable-all": true,
  "skip-dirs": ["vendor", "build"],
  "deadline": "1m",
  "severity": "error"
}
```

### Custom Linter Integration

```json
{
  "linters": {
    "custom-security-check": {
      "command": "my-security-tool",
      "pattern": "^(?P<path>.*?\\.go):(?P<line>\\d+):(?P<column>\\d+): (?P<message>\\[(?P<severity>[^\\]]+)\\] .*)"
    }
  },
  "enable": [
    "vet",
    "custom-security-check"
  ],
  "deadline": "2m"
}
```

## Pattern Matching for Custom Linters

Custom linter output must match regex patterns with named groups:

### Required Named Groups
- `path` - File path (e.g., `main.go`)
- `line` - Line number (e.g., `42`)
- `message` - Error message text

### Optional Named Groups
- `column` - Column number
- `severity` - "error" or "warning"

### Pattern Examples

```
# Standard format: file:line: message
^(?P<path>.*?\.go):(?P<line>\d+): (?P<message>.*)$

# With column: file:line:column: message
^(?P<path>.*?\.go):(?P<line>\d+):(?P<column>\d+): (?P<message>.*)$

# With severity: file:line: [severity] message
^(?P<path>.*?\.go):(?P<line>\d+): \[(?P<severity>[^\]]+)\] (?P<message>.*)$

# Complex: Multiple captures
^(?P<path>.*?\.go):(?P<line>\d+):(?P<column>\d+):\s+(?P<severity>error|warning):\s+(?P<message>.*)$
```

## Per-Linter Deadlines

Override deadline for specific slow linters:

```json
{
  "deadline": "1m",
  "linters": {
    "misspell": {
      "command": "misspell",
      "pattern": "^(?P<path>.*?\\.go):(?P<line>\\d+):(?P<column>\\d+): (?P<message>.*)",
      "deadline": "10s"
    }
  }
}
```

## Environment Variable Integration

Reference environment variables in configuration:

```bash
# Set environment variables
export GOMETALINTER_DEADLINE="30s"
export GOMETALINTER_ENABLE="vet,golint,errcheck"

# These can be used in custom linter commands
gometalinter --linter="custom:MY_TOOL $MY_VAR" ./...
```

## Configuration Validation

Validate configuration file syntax:

```bash
# Check if config file is valid JSON
cat .gometalinter.json | python3 -m json.tool

# Test configuration with verbose output
gometalinter --config=.gometalinter.json --verbose ./...
```

## Gotchas and Best Practices

### 1. Skip Patterns Are Regex
```json
{
  "skip-dirs": [
    "vendor",      // Matches "vendor" directory name
    "^\\..*",      // Skip hidden directories
    "build|dist"   // Match multiple directories
  ]
}
```

### 2. Deadline Applies to All Linters
- Each linter timeout adds to total deadline
- Set deadline high enough for all linters to complete
- Use `--errors` flag to exit early on errors

### 3. Disable-All Requires Explicit Enable
```json
{
  "disable": ["lll"],  // This doesn't disable all others
  "enable": ["vet"]    // Must explicitly enable what you want
}
```

### 4. JSON Escape Characters
```json
{
  "skip-files": [
    ".*\\.pb\\.go$"     // Backslashes must be escaped
  ]
}
```

### 5. Order Matters
- Command-line flags override config file
- Later config entries override earlier ones

## Migrating to golangci-lint

When migrating from gometalinter to golangci-lint, convert configuration:

**gometalinter:**
```json
{
  "enable": ["vet", "golint", "errcheck"],
  "deadline": "1m"
}
```

**golangci-lint equivalent:**
```yaml
linters:
  enable:
    - vet
    - golint
    - errcheck

run:
  timeout: 1m
```
