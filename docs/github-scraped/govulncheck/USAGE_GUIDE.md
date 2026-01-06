# Govulncheck Usage Guide

## Quick Start

### 1. Installation

```bash
go install golang.org/x/vuln/cmd/govulncheck@latest
```

Verify installation:
```bash
govulncheck version
```

### 2. Basic Scan

```bash
cd your-go-module
govulncheck ./...
```

### 3. Interpreting Results

If vulnerabilities are found, you'll see output like:
```
Vulnerability GO-2021-1234 in golang.org/x/text:
  The Parse function in language.Parse has a vulnerability
  main.go:42:5: main.myFunc calls golang.org/x/text/language.Parse
```

## Common Workflows

### Scanning Specific Packages

```bash
# Scan only the current package
govulncheck .

# Scan a specific package
govulncheck ./pkg/mypackage

# Scan multiple packages
govulncheck ./cmd/... ./pkg/...
```

### Including Test Files

```bash
govulncheck -test ./...
```

### Using Build Tags

```bash
# Scan with specific build tags
govulncheck -tags=linux ./...

# Multiple tags
govulncheck -tags=linux,amd64 ./...
```

### Detailed Output

Show full call stacks:
```bash
govulncheck -show traces ./...
```

Show progress and detailed information:
```bash
govulncheck -show verbose ./...
```

### JSON Output

For programmatic processing:
```bash
govulncheck -json ./... > results.json
```

Parse with jq:
```bash
govulncheck -json ./... | jq '.[] | select(.type == "VULNERABILITY")'
```

## Binary Analysis

### Scanning a Compiled Binary

```bash
# Direct binary scan
govulncheck -mode binary ./my-binary

# With detailed output
govulncheck -mode binary -show verbose ./my-binary
```

### Binary Extraction

For large binaries, extract vulnerability information:
```bash
# Extract minimal information
govulncheck -mode extract ./my-binary > info.blob

# Later, scan the extracted information
govulncheck -mode binary info.blob
```

### When to Use Binary Mode

- The binary is the only artifact available
- Source code is not available
- You need to scan already-built artifacts in CI/CD

## Output Formats

### Standard Text Output

```bash
govulncheck ./...
```

Provides:
- Module path
- Vulnerability ID
- Affected version range
- Call stack summary
- Recommendation

### JSON Output

```bash
govulncheck -format json ./...
```

Useful for:
- CI/CD integration
- Automated vulnerability reports
- Tool integration

### SARIF Output

```bash
govulncheck -format sarif ./...
```

Benefits:
- Standard format for static analysis tools
- Integration with GitHub Code Scanning
- Integration with other SAST platforms

### VEX Output

```bash
govulncheck -format openvex ./...
```

Use for:
- Vulnerability exchange and tracking
- Multi-tool vulnerability correlation
- Standard compliance

## Custom Database Configuration

### Using a Custom Vulnerability Database

```bash
# Point to a custom database endpoint
govulncheck -db https://custom-vuln-db.example.com ./...
```

Database must implement the specification at: https://go.dev/security/vuln/database

### Common Custom Database Scenarios

- Internal vulnerability tracking
- Air-gapped environments
- Custom vulnerability feeds
- Compliance requirements

## CI/CD Integration

### GitHub Actions

```yaml
name: Security Check
on: [push, pull_request]
jobs:
  vulncheck:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-go@v4
      - uses: golang/govulncheck-action@v1
```

### Manual CI/CD Integration

```bash
#!/bin/bash
set -e

# Run govulncheck
govulncheck ./...

# Check exit code
if [ $? -ne 0 ]; then
    echo "Vulnerabilities found!"
    exit 1
fi

echo "No vulnerabilities detected"
```

### JSON-Based CI/CD

```bash
#!/bin/bash

# Run and capture JSON
VULNS=$(govulncheck -json ./... | jq '[.[] | select(.type == "VULNERABILITY")] | length')

if [ "$VULNS" -gt 0 ]; then
    echo "Found $VULNS vulnerabilities"
    govulncheck -json ./... | jq '.[] | select(.type == "VULNERABILITY")'
    exit 1
fi
```

## Troubleshooting

### "Command not found"

Ensure govulncheck is in your PATH:
```bash
# Check installation
which govulncheck

# Add to PATH if needed (for bash)
export PATH="$PATH:$(go env GOPATH)/bin"
```

### "No vulnerabilities found" vs. Empty results

- **Message but no output**: No vulnerabilities detected
- **Empty JSON array**: No vulnerabilities detected (with `-json`)

### Module Not Found Errors

Ensure go.mod exists and dependencies are downloaded:
```bash
cd your-module
go mod download
govulncheck ./...
```

### Build Configuration Mismatch

Specify the build configuration:
```bash
# For specific Go version
go get golang.org/x/vuln/cmd/govulncheck@latest

# For specific platform/OS
GOOS=linux GOARCH=amd64 govulncheck ./...
```

### False Positives

Govulncheck may report false positives with:
- Function pointers
- Interface method calls
- Dynamic code (via `reflect` package)

Review call stacks with `-show traces`:
```bash
govulncheck -show traces ./...
```

## Performance Tips

### Large Projects

```bash
# Scan specific packages instead of entire project
govulncheck ./cmd/... ./pkg/...

# Parallel processing (go command handles automatically)
# But useful for CI/CD
time govulncheck ./...
```

### Binary Extraction for Repeated Scans

```bash
# Extract once
govulncheck -mode extract ./my-binary > cache.blob

# Reuse for multiple scans
govulncheck -mode binary cache.blob
```

## Examples

### Scanning a Web Service

```bash
cd myservice
govulncheck -test -show verbose ./...
```

### Scanning a CLI Tool

```bash
# Build then scan binary
go build -o myapp ./cmd/main.go
govulncheck -mode binary ./myapp
```

### Scanning with Specific Go Version

```bash
# Use go1.21
go1.21 run govulncheck@latest ./...
```

### Integration with go.dev

Visit https://pkg.go.dev for more information on any reported vulnerabilities:
```bash
# Look up vulnerability
# https://pkg.go.dev/vuln/GO-2021-1234
```

## Additional Resources

- [Go Security Vulnerabilities](https://go.dev/security/vuln)
- [Govulncheck Tutorial](https://go.dev/doc/tutorial/govulncheck)
- [Vulnerability Database](https://vuln.go.dev)
- [GitHub Repository](https://github.com/golang/vuln)
