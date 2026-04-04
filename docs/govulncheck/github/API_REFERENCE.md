# Govulncheck API Reference

## Overview

The `golang.org/x/vuln/scan` package provides programmatic access to govulncheck functionality for integration into Go applications.

**Package Documentation:** [pkg.go.dev/golang.org/x/vuln/scan](https://pkg.go.dev/golang.org/x/vuln/scan)

## Basic Usage

### Running Govulncheck via API

```go
package main

import (
    "context"
    "golang.org/x/vuln/scan"
)

func main() {
    // Create a command to scan the current module
    cmd := scan.Command(context.Background(), "./...")

    // Run the command
    if err := cmd.Run(); err != nil {
        panic(err)
    }
}
```

## Cmd Type

The `Cmd` type represents an external govulncheck command, similar to `exec.Cmd`.

### Fields

```go
type Cmd struct {
    // Stdin specifies the standard input.
    // If provided, it is expected to be the output of govulncheck -json.
    Stdin io.Reader

    // Stdout specifies the standard output.
    // If nil, Run connects os.Stdout.
    Stdout io.Writer

    // Stderr specifies the standard error.
    // If nil, Run connects os.Stderr.
    Stderr io.Writer

    // Env is the environment to use.
    // If Env is nil, the current environment is used.
    // To specify the setting of only a few variables,
    // append to the current environment:
    //
    //    opt.Env = append(os.Environ(),
    //        "GOOS=plan9", "GOARCH=386")
    Env []string
}
```

### Methods

#### Command

```go
func Command(ctx context.Context, arg ...string) *Cmd
```

Returns the Cmd struct to execute govulncheck with the given arguments.

**Parameters:**
- `ctx`: Context for cancellation and timeout
- `arg...`: Arguments to pass to govulncheck (e.g., "./...", "-tags", "linux")

**Example:**
```go
cmd := scan.Command(context.Background(), "-test", "./...")
```

#### Run

```go
func (c *Cmd) Run() error
```

Runs the govulncheck command. It blocks until the command completes.

**Returns:**
- Error if the command execution fails

**Example:**
```go
cmd := scan.Command(context.Background(), "./...")
if err := cmd.Run(); err != nil {
    log.Fatalf("govulncheck failed: %v", err)
}
```

#### Start

```go
func (c *Cmd) Start() error
```

Starts the govulncheck command but does not wait for it to complete.

**Returns:**
- Error if the command fails to start

**Example:**
```go
cmd := scan.Command(context.Background(), "./...")
if err := cmd.Start(); err != nil {
    log.Fatal(err)
}
// Do other work while govulncheck runs...
```

#### Wait

```go
func (c *Cmd) Wait() error
```

Waits for the command to complete. Must be called after Start().

**Example:**
```go
cmd := scan.Command(context.Background(), "./...")
if err := cmd.Start(); err != nil {
    log.Fatal(err)
}

// Do other work...

if err := cmd.Wait(); err != nil {
    log.Fatal(err)
}
```

#### Output

```go
func (c *Cmd) Output() ([]byte, error)
```

Runs the command and returns its standard output.

**Example:**
```go
cmd := scan.Command(context.Background(), "-json", "./...")
output, err := cmd.Output()
if err != nil {
    log.Fatal(err)
}
fmt.Println(string(output))
```

#### CombinedOutput

```go
func (c *Cmd) CombinedOutput() ([]byte, error)
```

Runs the command and returns its combined standard output and standard error.

**Example:**
```go
cmd := scan.Command(context.Background(), "./...")
output, err := cmd.CombinedOutput()
if err != nil {
    log.Fatal(err)
}
```

## Examples

### Scanning a Module

```go
package main

import (
    "context"
    "golang.org/x/vuln/scan"
    "log"
)

func main() {
    cmd := scan.Command(context.Background(), "./...")
    if err := cmd.Run(); err != nil {
        log.Fatal(err)
    }
}
```

### Capturing JSON Output

```go
package main

import (
    "context"
    "encoding/json"
    "golang.org/x/vuln/scan"
    "log"
)

func main() {
    cmd := scan.Command(context.Background(), "-json", "./...")
    output, err := cmd.Output()
    if err != nil {
        log.Fatal(err)
    }

    var results []interface{}
    if err := json.Unmarshal(output, &results); err != nil {
        log.Fatal(err)
    }

    log.Printf("Found %d results", len(results))
}
```

### Custom Stdout/Stderr

```go
package main

import (
    "context"
    "golang.org/x/vuln/scan"
    "log"
    "os"
)

func main() {
    cmd := scan.Command(context.Background(), "./...")
    cmd.Stdout = os.Stdout
    cmd.Stderr = os.Stderr

    if err := cmd.Run(); err != nil {
        log.Fatal(err)
    }
}
```

### With Build Tags

```go
package main

import (
    "context"
    "golang.org/x/vuln/scan"
    "log"
)

func main() {
    cmd := scan.Command(context.Background(), "-tags", "linux,amd64", "./...")
    if err := cmd.Run(); err != nil {
        log.Fatal(err)
    }
}
```

### With Timeout

```go
package main

import (
    "context"
    "golang.org/x/vuln/scan"
    "log"
    "time"
)

func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
    defer cancel()

    cmd := scan.Command(ctx, "./...")
    if err := cmd.Run(); err != nil {
        log.Fatal(err)
    }
}
```

### Binary Analysis

```go
package main

import (
    "context"
    "golang.org/x/vuln/scan"
    "log"
)

func main() {
    cmd := scan.Command(context.Background(), "-mode", "binary", "./my-binary")
    if err := cmd.Run(); err != nil {
        log.Fatal(err)
    }
}
```

### Environment Variables

```go
package main

import (
    "context"
    "golang.org/x/vuln/scan"
    "log"
    "os"
)

func main() {
    cmd := scan.Command(context.Background(), "./...")

    // Add custom environment variables
    cmd.Env = append(os.Environ(), "GOOS=linux", "GOARCH=amd64")

    if err := cmd.Run(); err != nil {
        log.Fatal(err)
    }
}
```

### Parsing JSON Output

```go
package main

import (
    "context"
    "encoding/json"
    "golang.org/x/vuln/scan"
    "log"
)

type Result struct {
    OSV  string      `json:"osv,omitempty"`
    Type string      `json:"type,omitempty"`
    Data interface{} `json:"data,omitempty"`
}

func main() {
    cmd := scan.Command(context.Background(), "-json", "./...")
    output, err := cmd.Output()
    if err != nil {
        log.Fatal(err)
    }

    var results []Result
    if err := json.Unmarshal(output, &results); err != nil {
        log.Fatal(err)
    }

    for _, r := range results {
        if r.Type == "VULNERABILITY" {
            log.Printf("Found vulnerability: %s", r.OSV)
        }
    }
}
```

### Context Cancellation

```go
package main

import (
    "context"
    "golang.org/x/vuln/scan"
    "log"
    "time"
)

func main() {
    ctx, cancel := context.WithCancel(context.Background())

    // Cancel after 10 seconds
    go func() {
        time.Sleep(10 * time.Second)
        cancel()
    }()

    cmd := scan.Command(ctx, "./...")
    if err := cmd.Run(); err != nil {
        log.Printf("Command cancelled or failed: %v", err)
    }
}
```

## JSON Output Format

When using `-json` flag, govulncheck outputs JSON lines. Each line is a JSON object with the following structure:

```json
{
  "osv": "GO-2021-1234",
  "type": "VULNERABILITY",
  "data": {
    "Calls": [
      {
        "Module": "golang.org/x/text",
        "Version": "v0.3.6",
        "Package": "golang.org/x/text/language",
        "Function": "Parse",
        "Receiver": "",
        "StackTrace": [
          {
            "Function": "main",
            "Package": "main"
          }
        ]
      }
    ]
  }
}
```

## Integration Patterns

### As Part of Build Process

```go
// buildtool.go
func runVulnCheck() error {
    cmd := scan.Command(context.Background(), "./...")
    return cmd.Run()
}
```

### Custom Security Scanner

```go
type Scanner struct {
    // fields
}

func (s *Scanner) Scan() error {
    cmd := scan.Command(context.Background(), "-json", "./...")
    output, err := cmd.Output()
    if err != nil {
        return err
    }
    return s.processOutput(output)
}
```

### CI/CD Pipeline

```go
func runInCICD() error {
    // Timeout after 5 minutes
    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Minute)
    defer cancel()

    cmd := scan.Command(ctx, "-json", "./...")
    output, err := cmd.Output()

    if err != nil {
        return err
    }

    // Process and report results
    return reportResults(output)
}
```

## Related Packages

- `golang.org/x/vuln/internal/govulncheck` - Internal govulncheck implementation
- `golang.org/x/vuln/internal/sarif` - SARIF output format
- `golang.org/x/vuln/internal/openvex` - OpenVEX output format

## Error Handling

The package returns standard Go errors. Common error scenarios:

```go
cmd := scan.Command(context.Background(), "./...")
if err := cmd.Run(); err != nil {
    switch err {
    case context.Canceled:
        log.Println("Scan was cancelled")
    case context.DeadlineExceeded:
        log.Println("Scan timed out")
    default:
        log.Printf("Scan failed: %v", err)
    }
}
```

## See Also

- [Official API Documentation](https://pkg.go.dev/golang.org/x/vuln/scan)
- [Command Line Reference](./README.md)
- [Usage Guide](./USAGE_GUIDE.md)
