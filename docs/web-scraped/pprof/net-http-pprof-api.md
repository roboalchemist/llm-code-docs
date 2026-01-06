# net/http/pprof API Reference

Source: https://pkg.go.dev/net/http/pprof

## Package Overview

Package `pprof` serves runtime profiling data via HTTP in the format expected by the pprof visualization tool. Profiling endpoints are available at paths under `/debug/pprof/`.

## Installation

### Automatic Registration

Simply import the package to register handlers with the default HTTP mux:

```go
import _ "net/http/pprof"
```

This automatically installs handlers for all profiling endpoints.

### Custom Registration

For advanced use cases, explicitly register handlers to a custom mux:

```go
package main

import (
	"log"
	"net/http"
	"net/http/pprof"
)

func main() {
	mux := http.NewServeMux()

	// Register specific handlers
	mux.HandleFunc("/debug/pprof/", pprof.Index)
	mux.HandleFunc("/debug/pprof/profile", pprof.Profile)
	mux.HandleFunc("/debug/pprof/heap", pprof.Handler("heap").ServeHTTP)
	mux.HandleFunc("/debug/pprof/goroutine", pprof.Handler("goroutine").ServeHTTP)
	mux.HandleFunc("/debug/pprof/cmdline", pprof.Cmdline)
	mux.HandleFunc("/debug/pprof/trace", pprof.Trace)

	log.Fatal(http.ListenAndServe(":6060", mux))
}
```

## Handler Functions

### Index

```go
func Index(w http.ResponseWriter, r *http.Request)
```

Serves the pprof index page listing all available profiles or retrieves a named profile.

**Behavior:**
- When accessed without query parameter: Returns HTML page listing all available profiles
- When called with profile name in query: Returns the named profile data

**URL:**
- `GET /debug/pprof/`
- `GET /debug/pprof/<profile>`

**Query Parameters:**
- `debug=N` - `0` = binary format (default), `>0` = plaintext format

**Returns:**
- HTML list of profiles when accessed without parameters
- Profile data in specified format when profile name is provided

**Example:**
```bash
# List all profiles
curl http://localhost:6060/debug/pprof/

# Get goroutine profile (plaintext)
curl "http://localhost:6060/debug/pprof/goroutine?debug=2"
```

### Profile (CPU Profile Handler)

```go
func Profile(w http.ResponseWriter, r *http.Request)
```

Responds with the pprof-formatted CPU profile. Profile data is collected for the duration specified by the `seconds` query parameter.

**URL:**
- `GET /debug/pprof/profile`

**Query Parameters:**
- `seconds=N` - Profiling duration in seconds (default: 30)

**Returns:**
- Binary pprof-formatted CPU profile data

**Example:**
```bash
# 30-second CPU profile (default)
go tool pprof http://localhost:6060/debug/pprof/profile

# 60-second CPU profile
go tool pprof http://localhost:6060/debug/pprof/profile?seconds=60

# Download profile for offline analysis
curl -o cpu.prof http://localhost:6060/debug/pprof/profile?seconds=30
go tool pprof cpu.prof
```

### Trace

```go
func Trace(w http.ResponseWriter, r *http.Request)
```

Responds with execution trace data in binary format. Available since Go 1.5.

**URL:**
- `GET /debug/pprof/trace`

**Query Parameters:**
- `seconds=N` - Trace duration in seconds (default: 1)

**Returns:**
- Binary trace format data

**Example:**
```bash
# 5-second execution trace
curl -o trace.out http://localhost:6060/debug/pprof/trace?seconds=5

# Analyze with trace viewer
go tool trace trace.out
```

### Cmdline

```go
func Cmdline(w http.ResponseWriter, r *http.Request)
```

Responds with the running program's command line with arguments separated by NUL bytes.

**URL:**
- `GET /debug/pprof/cmdline`

**Returns:**
- Command line arguments separated by NUL bytes

**Example:**
```bash
curl http://localhost:6060/debug/pprof/cmdline | tr '\0' '\n'
```

### Symbol

```go
func Symbol(w http.ResponseWriter, r *http.Request)
```

Maps program counters to function names. Used internally by pprof tools for symbol resolution.

**URL:**
- `GET /debug/pprof/symbol`

**Returns:**
- Symbol mapping in pprof format

**Example:**
```bash
go tool pprof http://localhost:6060/debug/pprof/profile?seconds=5
```

The pprof tool automatically uses this endpoint for symbol resolution.

### Handler

```go
func Handler(name string) http.Handler
```

Returns an HTTP handler for the named profile. Allows serving profiles with custom paths or settings.

**Parameters:**
- `name string` - Profile name (e.g., "heap", "goroutine", "mutex", "block", etc.)

**Returns:**
- http.Handler - Handler for the specified profile

**Example:**
```go
mux := http.NewServeMux()
mux.Handle("/custom/heap", pprof.Handler("heap"))
mux.Handle("/custom/goroutine", pprof.Handler("goroutine"))
```

## Available Profiles

The following profiles are automatically available through `pprof.Handler()`:

| Profile | Description | Query Parameters |
|---------|-------------|------------------|
| `heap` | Memory allocations | `debug=N`, `gc=N` |
| `allocs` | All past allocations | `debug=N`, `seconds=N` |
| `goroutine` | Goroutine stack traces | `debug=N`, `seconds=N` |
| `threadcreate` | OS thread creation | `debug=N`, `seconds=N` |
| `block` | Synchronization blocking | `debug=N`, `seconds=N` |
| `mutex` | Mutex contention | `debug=N`, `seconds=N` |
| `profile` | CPU profile | `seconds=N` |
| `trace` | Execution trace | `seconds=N` |

## Query Parameters Reference

### debug Parameter

```
debug=N
```

Controls output format:
- `0` (default) - Binary pprof format
- `>0` - Plaintext human-readable format

**Example:**
```bash
# Binary format (for pprof tool)
curl http://localhost:6060/debug/pprof/heap > heap.prof

# Plaintext format (human-readable)
curl "http://localhost:6060/debug/pprof/heap?debug=1"
```

### gc Parameter

```
gc=N
```

Run garbage collection before profiling (heap and allocs profiles only):
- `0` (default) - Do not run GC
- `>0` - Run GC before collecting profile

**Example:**
```bash
# Heap profile with GC run first
curl "http://localhost:6060/debug/pprof/heap?gc=1"
```

### seconds Parameter

```
seconds=N
```

Profiling duration in seconds (CPU, trace, and delta profiles):
- Default: 30 for CPU, 1 for trace
- Can be any positive integer

**Example:**
```bash
# 60-second CPU profile
curl http://localhost:6060/debug/pprof/profile?seconds=60

# 5-second execution trace
curl -o trace.out http://localhost:6060/debug/pprof/trace?seconds=5
```

## Common Usage Patterns

### Interactive Profiling

```bash
# Start interactive pprof session with heap profile
go tool pprof http://localhost:6060/debug/pprof/heap

# Start interactive pprof session with CPU profile
go tool pprof http://localhost:6060/debug/pprof/profile?seconds=30

# View top CPU-consuming functions
go tool pprof -top http://localhost:6060/debug/pprof/profile?seconds=30
```

### Goroutine Debugging

```bash
# Get current goroutine count and stack traces
go tool pprof http://localhost:6060/debug/pprof/goroutine

# Export plaintext format
curl "http://localhost:6060/debug/pprof/goroutine?debug=1" > goroutines.txt
```

### Memory Analysis

```bash
# Heap profile
go tool pprof http://localhost:6060/debug/pprof/heap

# All allocations
go tool pprof http://localhost:6060/debug/pprof/allocs

# With visualization
go tool pprof -http=:8080 http://localhost:6060/debug/pprof/heap
```

### Lock Contention

```bash
# Mutex contention profile
go tool pprof http://localhost:6060/debug/pprof/mutex

# Block profile (synchronization blocking)
go tool pprof http://localhost:6060/debug/pprof/block
```

### Execution Tracing

```bash
# Collect 5-second trace
curl -o trace.out http://localhost:6060/debug/pprof/trace?seconds=5

# View in trace viewer
go tool trace trace.out
```

## Setup Examples

### Simple HTTP Server with pprof

```go
package main

import (
	"log"
	"net/http"
	_ "net/http/pprof"
)

func main() {
	// pprof handlers automatically registered
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Hello World"))
	})

	log.Println("Server running on :6060")
	log.Println("Profiles available at http://localhost:6060/debug/pprof/")
	log.Fatal(http.ListenAndServe(":6060", nil))
}
```

### Custom Port and Path

```go
package main

import (
	"log"
	"net/http"
	"net/http/pprof"
)

func main() {
	mux := http.NewServeMux()

	// Serve application routes
	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Hello World"))
	})

	// Register pprof handlers on custom port/path
	debugMux := http.NewServeMux()
	debugMux.HandleFunc("/", pprof.Index)
	debugMux.HandleFunc("/profile", pprof.Profile)
	debugMux.Handle("/heap", pprof.Handler("heap"))
	debugMux.Handle("/goroutine", pprof.Handler("goroutine"))
	debugMux.HandleFunc("/cmdline", pprof.Cmdline)
	debugMux.HandleFunc("/trace", pprof.Trace)

	// Serve public API on :8080
	go func() {
		log.Fatal(http.ListenAndServe(":8080", mux))
	}()

	// Serve debugging on :6060
	log.Println("Profiler available at http://localhost:6060/")
	log.Fatal(http.ListenAndServe(":6060", debugMux))
}
```

### Integrated with Default Mux

```go
package main

import (
	"log"
	"net/http"
	_ "net/http/pprof"
)

func init() {
	// pprof handlers automatically registered to DefaultMux
	// Available at: http://localhost:6060/debug/pprof/
}

func main() {
	http.HandleFunc("/api/data", func(w http.ResponseWriter, r *http.Request) {
		// API handler
		w.Write([]byte("data"))
	})

	log.Println("Server + pprof on :6060")
	log.Fatal(http.ListenAndServe(":6060", nil))
}
```

## Combining with Production Monitoring

```go
package main

import (
	"context"
	"log"
	"net/http"
	_ "net/http/pprof"
	"time"
)

func main() {
	// Main application server (public)
	mux := http.NewServeMux()
	mux.HandleFunc("/api", handleAPI)

	// Debug server (pprof already registered to default mux)
	go func() {
		log.Println("Debug server on :6060")
		log.Fatal(http.ListenAndServe(":6060", nil))
	}()

	// Main server
	log.Println("Server on :8080")
	log.Fatal(http.ListenAndServe(":8080", mux))
}

func handleAPI(w http.ResponseWriter, r *http.Request) {
	ctx, cancel := context.WithTimeout(r.Context(), 5*time.Second)
	defer cancel()

	// API logic...
	w.Write([]byte("OK"))
}
```

## Performance Considerations

- CPU profiling adds 2-5% overhead
- Heap profiling adds minimal overhead (sampling-based)
- Block and mutex profiles must be explicitly enabled
- Only collect one profile at a time in production
- Use fixed sampling windows (e.g., 30 seconds every 5 minutes)
