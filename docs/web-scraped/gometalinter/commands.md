# gometalinter Command Reference

## Source: https://github.com/alecthomas/gometalinter

## Basic Syntax

```bash
gometalinter [flags] [packages]
```

## Common Commands and Examples

### Basic Linting

```bash
# Lint current package
gometalinter ./

# Lint all packages recursively
gometalinter ./...

# Lint specific package
gometalinter ./mypackage

# Lint multiple packages
gometalinter ./pkg1 ./pkg2 ./pkg3
```

### Linter Control

```bash
# List all available linters
gometalinter --list-linters

# Enable specific linters only
gometalinter --disable-all --enable=vet --enable=golint ./...

# Disable specific linters
gometalinter --disable=misspell --disable=lll ./...

# Enable all linters
gometalinter --enable-all ./...
```

### Output and Formatting

```bash
# Checkstyle XML format (for CI/CD tools)
gometalinter --checkstyle ./...

# JSON output
gometalinter --json ./...

# Specify output format with template
gometalinter --format='{{.Path}}:{{.Line}}:{{.Column}}: {{.Message}} ({{.Linter}})' ./...

# Show only errors (not warnings)
gometalinter --severity=error ./...

# Show errors and warnings
gometalinter --severity=warning ./...
```

### Performance and Timeout

```bash
# Set deadline (timeout) for all linters
gometalinter --deadline=30s ./...

# Set deadline for specific linter
gometalinter --deadline=vet:5s ./...

# Run linters with specific number of workers
gometalinter --concurrency=4 ./...

# Skip linters that take too long
gometalinter --deadline=1m --errors ./...
```

### File and Pattern Matching

```bash
# Exclude files matching pattern
gometalinter --exclude=vendor ./...

# Exclude directories
gometalinter --exclude-dir=build --exclude-dir=dist ./...

# Only check Go test files
gometalinter --include='.*_test\.go$' ./...

# Include specific file patterns
gometalinter --include='*.go' ./...
```

### Configuration Files

```bash
# Use specific config file
gometalinter --config=.custom-gometalinter.json ./...

# Generate config file
gometalinter --write-config=.gometalinter.json ./...

# Save configuration to file
gometalinter --save-config ./...
```

## Detailed Flag Reference

### Linter Selection

| Flag | Type | Description |
|------|------|-------------|
| `--enable` | string | Enable specific linter |
| `--disable` | string | Disable specific linter |
| `--enable-all` | bool | Enable all linters |
| `--disable-all` | bool | Disable all linters (use with `--enable`) |
| `--list-linters` | bool | List all available linters and exit |

### Output Control

| Flag | Type | Description |
|------|------|-------------|
| `--format` | string | Output format template (default: `<file>:<line>:[<col>]: <message> (<linter>)`) |
| `--json` | bool | Output results as JSON |
| `--checkstyle` | bool | Output Checkstyle XML format |
| `--severity` | string | Report only issues with this severity or higher (error, warning) |

### Performance

| Flag | Type | Description |
|------|------|-------------|
| `--deadline` | duration | Maximum total time for all linters (e.g., "30s", "2m") |
| `--concurrency` | int | Number of worker threads for parallel execution |

### File Matching

| Flag | Type | Description |
|------|------|-------------|
| `--include` | string | Include file pattern (regex) |
| `--exclude` | string | Exclude file pattern (regex) |
| `--exclude-dir` | string | Exclude directory pattern (regex) |
| `--vendor` | bool | Enable checking vendor directory |

### Configuration

| Flag | Type | Description |
|------|------|-------------|
| `--config` | string | Path to config file |
| `--write-config` | string | Write config to file and exit |
| `--save-config` | bool | Save config file for this run |

### Other Options

| Flag | Type | Description |
|------|------|-------------|
| `--fast` | bool | Only run fast linters |
| `--skip-vendor` | bool | Skip vendor directory |
| `--var-naming` | bool | Enable variable naming checks |
| `--errors` | bool | Show errors only |
| `--warnings` | bool | Show warnings only |

## Environment Variables

```bash
# Override PATH for linter binaries
export GOMETALINTER_LINTERS=/custom/path/to/linters

# Set default deadline
export GOMETALINTER_DEADLINE=30s

# Enable specific linters by default
export GOMETALINTER_ENABLE=vet,golint
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success (no linting issues found) |
| 1 | Linting issues found |
| 2 | Error running gometalinter |

## Practical Examples

### CI/CD Pipeline

```bash
# Run with strict settings for CI
gometalinter \
  --deadline=5m \
  --severity=error \
  --checkstyle \
  --errors \
  ./... > linting-results.xml
```

### Pre-commit Hook

```bash
#!/bin/bash
# .git/hooks/pre-commit

if ! gometalinter --deadline=10s ./...; then
    echo "Linting errors found. Commit aborted."
    exit 1
fi
```

### Development Check

```bash
# Fast check during development
gometalinter --deadline=30s --enable=vet --enable=golint ./...
```

### Custom Linter Integration

```bash
# Add custom linter
gometalinter \
  --linter="custom:my-linter {file}:^(?P<path>.*?):(?P<line>\d+): (?P<message>.*)$" \
  ./...
```

### Jenkins Integration

```groovy
// Jenkinsfile
stage('Lint') {
    steps {
        sh 'gometalinter --checkstyle ./... > checkstyle-report.xml'
        publishHTML target: [
            reportDir: '.',
            reportFiles: 'checkstyle-report.xml',
            reportName: 'Linting Report'
        ]
    }
}
```

## Troubleshooting Commands

```bash
# Check which linters are installed
gometalinter --list-linters

# Test specific linter
gometalinter --enable=golint --disable-all ./...

# Check for timeout issues
gometalinter --deadline=60s --verbose ./...

# View configuration being used
gometalinter --config=.gometalinter.json --help

# Test with minimal linters
gometalinter --enable-all --exclude-dir=vendor ./mypackage
```

## Notes

- All durations use Go duration format: "300ms", "5s", "2m30s"
- Patterns use Go regex syntax (RE2)
- Multiple `--enable` and `--disable` flags can be combined
- Configuration file options override command-line defaults
