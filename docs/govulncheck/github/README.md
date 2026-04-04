# Govulncheck Documentation

## Overview

Govulncheck reports known vulnerabilities that affect Go code. It uses static analysis of source code or a binary's symbol table to narrow down reports to only those that could affect the application.

Govulncheck is part of Go's support for vulnerability management and is backed by the Go vulnerability database, which is curated by the Go security team. Go's tooling reduces noise in your results by only surfacing vulnerabilities in functions that your code is actually calling.

**Official Repository:** [github.com/golang/vuln](https://github.com/golang/vuln)

**API Documentation:** [pkg.go.dev/golang.org/x/vuln/scan](https://pkg.go.dev/golang.org/x/vuln/scan)

**Vulnerability Database:** [vuln.go.dev](https://vuln.go.dev)

## Installation

Install the latest version of govulncheck using `go install`:

```bash
go install golang.org/x/vuln/cmd/govulncheck@latest
```

Then, run govulncheck inside your module:

```bash
govulncheck ./...
```

## Basic Usage

### Analyzing Source Code

To analyze source code from the module directory:

```bash
cd my-module
govulncheck ./...
```

If no vulnerabilities are found, govulncheck will display a short message. If there are vulnerabilities, each is displayed briefly with a summary of a call stack.

**Output Example:**
```
main.go:[line]:[column]: mypackage.main calls golang.org/x/text/language.Parse
```

### Analyzing Binary

To run govulncheck on a compiled binary, pass it the path to the binary file with the `-mode binary` flag:

```bash
govulncheck -mode binary $HOME/go/bin/my-go-program
```

Govulncheck uses the binary's symbol information to find mentions of vulnerable functions. These functions can belong to the binary's transitive dependencies and also the main module of the binary. Govulncheck output on binaries omits call stacks, which require source code analysis.

### Binary Extraction Mode

Govulncheck also supports `-mode extract` on a Go binary for extraction of minimal information needed to analyze the binary:

```bash
govulncheck -mode extract /path/to/binary > extraction.blob
govulncheck -mode binary extraction.blob
```

This produces a blob, typically much smaller than the binary, that can also be passed to govulncheck.

## Command-Line Flags

### Build Configuration

- **`-tags string`**: Comma-separated list of build tags to use when analyzing source code
- **`-test`**: Include test files in the analysis

### Output Control

- **`-show traces`**: Include more detailed stack traces (print full call stack for each entry)
- **`-show verbose`**: Include progress messages and more details on findings
- **`-format string`**: Output format (json, sarif, openvex)

### Database Configuration

- **`-db string`**: Specify a different vulnerability database (must implement the specification at https://go.dev/security/vuln/database). Default is https://vuln.go.dev

### Mode Selection

- **`-mode source`**: Analyze source code (default)
- **`-mode binary`**: Analyze compiled binary
- **`-mode extract`**: Extract minimal information from binary for later analysis

## Output Formats

### Standard Output

The default output format provides:
- Vulnerability description
- Affected module version
- Call stack summary showing how the vulnerable function is called

### JSON Format

Stream vulnerabilities as JSON:

```bash
govulncheck -json ./... | jq
```

### SARIF Format

Generate Static Analysis Results Interchange Format (SARIF) output:

```bash
govulncheck -format sarif ./...
```

Follows the specification at https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=sarif

### VEX Format

Generate Vulnerability EXchange (VEX) output:

```bash
govulncheck -format openvex ./...
```

Follows the specification at https://github.com/openvex/spec

## Exit Codes

- **Exit code 0**: No vulnerabilities found, OR format is `-json`, `-format sarif`, or `-format openvex`
- **Non-zero exit code**: Vulnerabilities were found (in standard output mode)

## Build Configuration Considerations

Govulncheck looks for vulnerabilities in Go programs using a specific build configuration:

- **For source code analysis**: Uses the Go version specified by the "go" command found on the PATH
- **For binaries**: Uses the build configuration used to build the binary

Different build configurations may have different known vulnerabilities.

## Privacy

By default, govulncheck makes requests to the Go vulnerability database at https://vuln.go.dev. Requests to the vulnerability database contain only module paths with vulnerabilities already known to the database, not code or other properties of your program.

See [vuln.go.dev/privacy](https://vuln.go.dev/privacy) for more information about privacy practices.

## Limitations

Govulncheck has these limitations:

- **Function pointers and interfaces**: Analyzes conservatively, which may result in false positives or inaccurate call stacks in some cases
- **Reflection**: Calls to functions made using package `reflect` are not visible to static analysis. Vulnerable code reachable only through those calls will not be reported in source scan mode
- **Unsafe package**: Use of the `unsafe` package may result in false negatives
- **Binary analysis**: Because Go binaries do not contain detailed call information, govulncheck cannot show the call graphs for detected vulnerabilities. It may also report false positives for code that is in the binary but unreachable
- **Silencing findings**: There is no support for silencing vulnerability findings (see https://go.dev/issue/61211 for updates)
- **Legacy binaries**: Only reports standard library vulnerabilities for binaries built with Go versions prior to Go 1.18
- **Symbol information**: For binaries where symbol information cannot be extracted, govulncheck reports vulnerabilities for all modules on which the binary depends

## Go Vulnerability Database

The Go vulnerability database is rooted at `https://vuln.go.dev` and provides data as JSON.

### Database Endpoints

| Path | Description |
|------|-------------|
| `$base/index.json` | List of module paths in the database mapped to its last modified timestamp ([example](https://vuln.go.dev/index.json)) |
| `$base/$module.json` | List of vulnerability entries for that module ([example](https://vuln.go.dev/golang.org/x/crypto.json)) |
| `$base/ID/index.json` | List of all vulnerability entries in the database |
| `$base/ID/$vuln.json` | An individual Go vulnerability report |

Where:
- `$base` is `https://vuln.go.dev`
- `$module` is a module path
- `$vuln` is a Go vulnerability ID (for example, `GO-2021-1234`)

**Note:** These paths and format are provisional and likely to change until an approved proposal.

## API Usage

The scan package provides programmatic access to govulncheck functionality:

```go
package main

import (
    "context"
    "golang.org/x/vuln/scan"
)

func main() {
    cmd := scan.Command(context.Background(), "./...")
    cmd.Run()
}
```

See [pkg.go.dev/golang.org/x/vuln/scan](https://pkg.go.dev/golang.org/x/vuln/scan) for complete API documentation.

## CI/CD Integration

### GitHub Actions

Govulncheck provides official GitHub Actions integration:

- **Repository**: https://github.com/golang/govulncheck-action
- **Marketplace**: [Golang Vulncheck Action](https://github.com/marketplace/actions/golang-vulncheck)

### Example Workflow

```yaml
name: Vulnerability Check

on: [push, pull_request]

jobs:
  vulncheck:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-go@v4
      - uses: golang/govulncheck-action@v1
```

## Feedback

To share feedback about govulncheck, see [go.dev/security/vuln](https://go.dev/security/vuln).

## License

Unless otherwise noted, the Go source files are distributed under the BSD-style license found in the LICENSE file.

Database entries available at https://vuln.go.dev are distributed under the terms of the [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.

## See Also

- [Go Vulnerability Management Tutorial](https://go.dev/doc/tutorial/govulncheck)
- [Go Security Vulnerability Information](https://go.dev/security/vuln)
- [Go Vulnerability Database](https://vuln.go.dev)
- [Source: golang/vuln Repository](https://github.com/golang/vuln)
