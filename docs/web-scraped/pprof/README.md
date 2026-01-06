# pprof - Go Profiling and Diagnostic Tool

Source: https://go.dev/doc/diagnostics, https://pkg.go.dev/runtime/pprof, https://pkg.go.dev/net/http/pprof

## Overview

pprof is a standard Go tool for analyzing profiling data from Go programs. It helps identify expensive or frequently called sections of code through visualization of stack traces and execution data. The Go runtime provides profiling data in the format expected by the [pprof visualization tool](https://github.com/google/pprof/).

Profiling data can be collected:
- During testing via `go test`
- Via runtime endpoints using the `net/http/pprof` package
- Via manual collection using the `runtime/pprof` package

## Quick Start

### Basic CPU Profiling

```go
package main

import (
	"flag"
	"log"
	"os"
	"runtime/pprof"
)

var cpuprofile = flag.String("cpuprofile", "", "write cpu profile to `file`")

func main() {
	flag.Parse()
	if *cpuprofile != "" {
		f, err := os.Create(*cpuprofile)
		if err != nil {
			log.Fatal("could not create CPU profile: ", err)
		}
		defer f.Close()
		if err := pprof.StartCPUProfile(f); err != nil {
			log.Fatal("could not start CPU profile: ", err)
		}
		defer pprof.StopCPUProfile()
	}
	// ... program logic ...
}
```

Run and analyze:
```bash
# Run with CPU profiling
./myapp -cpuprofile=cpu.prof

# Analyze with pprof
go tool pprof cpu.prof
```

### HTTP-Based Profiling

```go
package main

import (
	"log"
	"net/http"
	_ "net/http/pprof"
)

func main() {
	// pprof handlers automatically registered to default mux
	log.Println(http.ListenAndServe("localhost:6060", nil))
}
```

Then access profiles at:
- http://localhost:6060/debug/pprof/
- http://localhost:6060/debug/pprof/heap
- http://localhost:6060/debug/pprof/profile?seconds=30

## Profile Types

The `runtime/pprof` package provides these predefined profiles:

### CPU Profile
- **Name:** `cpu`
- **Shows:** Where a program spends time consuming CPU cycles (not sleeping or waiting for I/O)
- **Use:** Identify CPU bottlenecks and hot code paths
- **Access:** `pprof.StartCPUProfile()` / `pprof.StopCPUProfile()`

### Heap Profile
- **Name:** `heap`
- **Shows:** Memory allocation samples; monitors current and historical memory usage
- **Use:** Detect memory leaks and memory usage patterns
- **Access:** `pprof.WriteHeapProfile()` or `Lookup("heap")`

### Goroutine Profile
- **Name:** `goroutine`
- **Shows:** Stack traces of all current goroutines
- **Use:** Debug goroutine leaks and concurrent execution
- **Access:** `Lookup("goroutine")`

### Thread Creation Profile
- **Name:** `threadcreate`
- **Shows:** Sections of the program that lead to new OS thread creation
- **Use:** Identify excessive thread creation
- **Access:** `Lookup("threadcreate")`

### Block Profile
- **Name:** `block`
- **Shows:** Where goroutines block on synchronization primitives (timer channels, mutexes, etc.)
- **Use:** Identify synchronization bottlenecks
- **Enabled:** Not by default; use `runtime.SetBlockProfileRate(1)` to enable
- **Access:** `Lookup("block")`

### Mutex Profile
- **Name:** `mutex`
- **Shows:** Lock contention and which goroutines hold contended locks
- **Use:** Identify lock contention issues affecting CPU utilization
- **Enabled:** Not by default; use `runtime.SetMutexProfileFraction(1)` to enable
- **Access:** `Lookup("mutex")`

### Allocs Profile
- **Name:** `allocs`
- **Shows:** Sampling of all past memory allocations
- **Use:** Comprehensive memory usage analysis
- **Access:** `Lookup("allocs")`

## Visualization Methods

### Text Visualization
Lists the most expensive calls as text output:
```bash
go tool pprof -top cpu.prof
```

### Graph Visualization
Visualizes the most expensive calls as a directed graph:
```bash
go tool pprof -web cpu.prof
```

### Weblist Visualization
Displays expensive parts of source code line-by-line in an HTML page, showing cost of each line:
```bash
go tool pprof -weblist cpu.prof
```

### Flame Graphs
Interactive visualization allowing zoom in/out of specific code sections. Provided by the [upstream pprof tool](https://github.com/google/pprof):
```bash
go tool pprof -http=:8080 cpu.prof
```

## Production Profiling

### Is it Safe to Profile Production?

Yes, it is safe to profile programs in production, but enabling some profiles (e.g., CPU profile) adds measurable cost.

**Important considerations:**
- Expect to see performance degradation during profiling
- Measure profiler overhead before enabling in production
- Collection of profiles can interfere with each other

### Best Practices

1. **Periodic Profiling:** Periodically profile production services rather than profiling continuously
2. **Random Sampling:** In systems with many replicas of a single process, select a random replica periodically
3. **Fixed Duration:** Profile for X seconds for every Y seconds and save results for analysis
4. **Single Profile at a Time:** Only collect one profile at a time to avoid interference
5. **Automated Review:** Results may be manually and/or automatically reviewed to find problems
6. **On Linux:** Use [perf tools](https://perf.wiki.kernel.org/index.php/Tutorial) to profile and unwind cgo/SWIG code
7. **On macOS:** Use [Instruments](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/) suite

## Custom pprof Handler Paths

By default, `net/http/pprof` registers handlers to the default HTTP mux. You can serve profiler handlers on a different path and port:

```go
package main

import (
	"log"
	"net/http"
	"net/http/pprof"
)

func main() {
	mux := http.NewServeMux()

	// Register pprof handlers to custom mux
	mux.HandleFunc("/custom_debug_path/profile", pprof.Profile)
	mux.HandleFunc("/custom_debug_path/heap", pprof.Handler("heap").ServeHTTP)
	mux.HandleFunc("/custom_debug_path/goroutine", pprof.Handler("goroutine").ServeHTTP)
	mux.HandleFunc("/custom_debug_path/cmdline", pprof.Cmdline)

	log.Fatal(http.ListenAndServe(":7777", mux))
}
```

## Custom Profiles

You can create custom profiles beyond the predefined ones:

```go
package main

import (
	"runtime/pprof"
)

var requests = pprof.NewProfile("custom_requests")

func handleRequest(r *Request) {
	requests.Add(r, 1)
	defer requests.Remove(r)
	// ... handle request ...
}
```

## API Reference

### runtime/pprof Functions

#### CPU Profiling
- **`StartCPUProfile(w io.Writer) error`** - Enables CPU profiling, buffering output to writer
- **`StopCPUProfile()`** - Stops current CPU profile and waits for all writes to complete

#### Heap Profiling
- **`WriteHeapProfile(w io.Writer) error`** - Shorthand for `Lookup("heap").WriteTo(w, 0)`

#### Profile Management
- **`Lookup(name string) *Profile`** - Returns profile with given name, or nil if not found
- **`NewProfile(name string) *Profile`** - Creates new profile; panics if name exists
- **`Profiles() []*Profile`** - Returns slice of all known profiles, sorted by name

#### Profile Type Methods
- **`(p *Profile) Name() string`** - Returns profile's name
- **`(p *Profile) Count() int`** - Returns number of execution stacks in profile
- **`(p *Profile) Add(value any, skip int)`** - Adds current execution stack associated with value
- **`(p *Profile) Remove(value any)`** - Removes execution stack for value (no-op if not found)
- **`(p *Profile) WriteTo(w io.Writer, debug int) error`** - Writes pprof-formatted snapshot

#### Label Management (Go 1.9+)
- **`Label(ctx context.Context, key string) (string, bool)`** - Returns label value for given key
- **`Labels(args ...string) LabelSet`** - Creates LabelSet from key-value string pairs
- **`WithLabels(ctx context.Context, labels LabelSet) context.Context`** - Returns new context with labels
- **`Do(ctx context.Context, labels LabelSet, f func(context.Context))`** - Calls f with label context
- **`ForLabels(ctx context.Context, f func(key, value string) bool)`** - Invokes f for each label
- **`SetGoroutineLabels(ctx context.Context)`** - Sets current goroutine's labels from context

### net/http/pprof Handlers

#### Index Handler
- **`func Index(w http.ResponseWriter, r *http.Request)`** - Serves named profiles or lists available profiles as HTML at `/debug/pprof/`

#### CPU Profile Handler
- **`func Profile(w http.ResponseWriter, r *http.Request)`** - Responds with pprof-formatted CPU profile
- **Query parameter:** `seconds=N` (default: 30 seconds)
- **Registered as:** `/debug/pprof/profile`

#### Trace Handler
- **`func Trace(w http.ResponseWriter, r *http.Request)`** - Responds with execution trace data (binary)
- **Query parameter:** `seconds=N` (default: 1 second)
- **Registered as:** `/debug/pprof/trace`
- **Available since:** Go 1.5

#### Heap Profile Handler
- **`func Handler(name string) http.Handler`** - Returns HTTP handler for named profile
- **Query parameters:** `debug=N` (0=binary, >0=plaintext), `gc=N` (>0=run GC first)
- **Registered as:** `/debug/pprof/heap`

#### Other Handlers
- **`func Cmdline(w http.ResponseWriter, r *http.Request)`** - Running program's command line with NUL-separated args
- **`func Symbol(w http.ResponseWriter, r *http.Request)`** - Maps program counters to function names

#### Query Parameters (All Profiles)
- **`debug=N`**: `0` = binary format (default), `>0` = plaintext
- **`gc=N`**: `>0` = run garbage collection before profiling (heap, allocs)
- **`seconds=N`**: Profile duration in seconds (cpu, trace, heap, allocs, block, goroutine, mutex, threadcreate)

## Example Usage

### Testing with pprof

```bash
# Run tests with CPU profile
go test -cpuprofile=cpu.prof ./...

# Analyze results
go tool pprof cpu.prof
```

### HTTP Profiling

```bash
# Download heap profile from running service
go tool pprof http://localhost:6060/debug/pprof/heap

# Download 30-second CPU profile
go tool pprof http://localhost:6060/debug/pprof/profile?seconds=30

# Download goroutine profile
go tool pprof http://localhost:6060/debug/pprof/goroutine

# Download mutex contention profile
go tool pprof http://localhost:6060/debug/pprof/mutex

# Download execution trace
curl -o trace.out http://localhost:6060/debug/pprof/trace?seconds=5
go tool trace trace.out
```

### Interactive pprof Commands

```bash
go tool pprof cpu.prof

(pprof) top              # Show top functions by CPU time
(pprof) web              # Generate graph visualization
(pprof) list function    # Show source code for function with annotations
(pprof) alloc_space      # Show all allocations (heap)
(pprof) alloc_objects    # Show allocation counts
(pprof) help             # Show all available commands
```

## Label-Based Profiling

Use labels to associate profiling samples with specific requests or operations (Go 1.9+):

```go
package main

import (
	"context"
	"net/http"
	"runtime/pprof"
)

func handler(w http.ResponseWriter, r *http.Request) {
	ctx := context.Background()
	labels := pprof.Labels("user_id", r.URL.Query().Get("user"))

	pprof.Do(ctx, labels, func(ctx context.Context) {
		// All profiling samples in this context are labeled
		handleRequest(ctx, r)
	})
}
```

Then filter profiles by label:
```bash
go tool pprof -http=:8080 http://localhost:6060/debug/pprof/profile?seconds=30
# In pprof: "focus user_id=123"
```

## Related Tools and Resources

- [pprof GitHub Repository](https://github.com/google/pprof/) - Official visualization tool
- [Profiling Go Programs Blog Post](https://go.dev/blog/profiling-go-programs) - Detailed examples
- [Go Diagnostics Guide](https://go.dev/doc/diagnostics) - Broader profiling and tracing resources
- [Flame Graphs by Brendan Gregg](http://www.brendangregg.com/flamegraphs.html) - Visualization technique
- [perf Tools (Linux)](https://perf.wiki.kernel.org/) - Kernel-level profiling
- [Instruments (macOS)](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/) - System profiling suite

## See Also

- `runtime/pprof` - Core profiling package
- `net/http/pprof` - HTTP profiling endpoint integration
- `runtime` - Runtime profiling control functions
- `go tool pprof` - Command-line profiling analysis tool
