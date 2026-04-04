# Source: https://securego.io/docs/rules/rule-intro

# Gosec - Go Security Scanner

Gosec is a source code security scanner for Go that inspects source code for security problems
by scanning the Go AST (Abstract Syntax Tree). It's designed to identify security vulnerabilities
in Go applications including:

- SQL injection attacks
- Weak cryptography
- Hardcoded credentials and secrets
- Insecure temporary file creation
- Missing input validation
- Unsafe file operations

## Security Rules Overview

Gosec implements multiple security rules to detect various vulnerability classes:

### G101: Hardcoded Credentials
Detects hardcoded passwords and sensitive credentials in string literals.
Variables matching patterns like "password", "token", "secret", etc. are flagged.

### G102: Bind to All Interfaces
Identifies insecure network binding that listens on 0.0.0.0, exposing services to all interfaces.

### G103: Use of Unsafe Block
Flags usage of Go's unsafe package which bypasses type safety.

### G104: Audit Errors Not Checked
Detects error handling issues where error returns are ignored.

### G107: URL Taint Input
Identifies potential SSRF vulnerabilities where user input is passed directly to HTTP requests.

### G201/G202: SQL Injection
- G201: Detects SQL query construction using format strings
- G202: Detects SQL query construction using string concatenation

### G304: File Path Taint Input
Identifies file path operations using untrusted input.

## Installation

gosec can be installed via:

```bash
# Using go install
go install github.com/securego/gosec/v2/cmd/gosec@latest

# Using Docker
docker pull securego/gosec

# Using Homebrew (macOS)
brew install gosec
```

## Usage

Basic usage:

```bash
# Scan current directory
gosec ./...

# Scan specific file
gosec myfile.go

# With detailed output
gosec -v ./...

# Generate JSON report
gosec -fmt=json ./... > report.json
```

## Features

- Fast scanning of Go source code
- Low false positive rate through configuration
- JSON/CSV/SARIF output formats
- Integration with CI/CD pipelines
- Customizable rule configuration
- Extensive documentation for each rule

## References

- Official Website: https://securego.io
- GitHub Repository: https://github.com/securego/gosec
- Rule Documentation: https://securego.io/docs/rules/
- Slack Community: http://securego.herokuapp.com/

