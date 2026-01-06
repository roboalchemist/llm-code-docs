# pprof Usage Examples

Source: https://go.dev/doc/diagnostics, https://go.dev/blog/profiling-go-programs

## Basic CPU Profiling

### Example 1: Profile a Command-Line Tool

```go
// main.go - A tool that processes data
package main

import (
	"flag"
	"log"
	"os"
	"runtime/pprof"
)

var cpuprofile = flag.String("cpuprofile", "", "write cpu profile to file")

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

	// Your application logic
	doWork()
}

func doWork() {
	// CPU-intensive work...
	sum := 0
	for i := 0; i < 1000000000; i++ {
		sum += i
	}
}
```

**Usage:**
```bash
# Run with CPU profiling
go run main.go -cpuprofile=cpu.prof

# Analyze the profile
go tool pprof cpu.prof

# Interactive commands
(pprof) top          # Show top functions
(pprof) web          # Generate graph
(pprof) list doWork  # Show source with costs
```

## Memory Profiling

### Example 2: Detect Memory Leaks

```go
package main

import (
	"fmt"
	"log"
	"os"
	"runtime/pprof"
	"time"
)

func main() {
	// Write heap profile before and after work
	f, err := os.Create("heap.prof")
	if err != nil {
		log.Fatal("could not create profile: ", err)
	}
	defer f.Close()

	// Do some memory allocation
	doMemoryWork()

	// Capture heap profile
	if err := pprof.WriteHeapProfile(f); err != nil {
		log.Fatal("could not write memory profile: ", err)
	}

	fmt.Println("Heap profile written to heap.prof")
}

func doMemoryWork() {
	// Create a slice that grows
	var data [][]int
	for i := 0; i < 1000; i++ {
		// Create 1MB slice
		chunk := make([]int, 256000)
		data = append(data, chunk)
		if i%100 == 0 {
			fmt.Printf("Allocated %d MB\n", (i+1)*4/1024)
		}
	}

	// Keep reference to prevent GC
	_ = data
	time.Sleep(1 * time.Second)
}
```

**Usage:**
```bash
# Run to generate profile
go run main.go

# Analyze heap profile
go tool pprof heap.prof

# Show top memory allocators
(pprof) top
(pprof) alloc_space   # Total allocations
(pprof) alloc_objects # Object count

# Show functions with large allocations
(pprof) list doMemoryWork
```

## HTTP-Based Profiling

### Example 3: Always-On Profiling in a Web Server

```go
package main

import (
	"fmt"
	"log"
	"net/http"
	_ "net/http/pprof"
	"time"
)

func main() {
	// Standard HTTP routes
	http.HandleFunc("/api/users", handleUsers)
	http.HandleFunc("/api/posts", handlePosts)

	// pprof endpoints automatically available at /debug/pprof/
	log.Println("Server running on :8080")
	log.Println("Profiles available at http://localhost:8080/debug/pprof/")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func handleUsers(w http.ResponseWriter, r *http.Request) {
	// Simulate database query
	time.Sleep(100 * time.Millisecond)
	w.Header().Set("Content-Type", "application/json")
	fmt.Fprint(w, `[{"id":1,"name":"Alice"},{"id":2,"name":"Bob"}]`)
}

func handlePosts(w http.ResponseWriter, r *http.Request) {
	// Simulate processing
	processData()
	w.Header().Set("Content-Type", "application/json")
	fmt.Fprint(w, `[{"id":1,"title":"Hello"}]`)
}

func processData() {
	sum := 0
	for i := 0; i < 100000000; i++ {
		sum += i * i
	}
}
```

**Usage:**
```bash
# Start server
go run main.go

# In another terminal, download heap profile
go tool pprof http://localhost:8080/debug/pprof/heap

# Download 30-second CPU profile
go tool pprof http://localhost:8080/debug/pprof/profile?seconds=30

# Download goroutine profile
go tool pprof http://localhost:8080/debug/pprof/goroutine

# View goroutines in plaintext
curl "http://localhost:8080/debug/pprof/goroutine?debug=2"

# Generate execution trace
curl -o trace.out http://localhost:8080/debug/pprof/trace?seconds=5
go tool trace trace.out
```

## Testing with Profiling

### Example 4: Profile Your Tests

```go
// mypackage/compute_test.go
package mypackage

import (
	"testing"
)

func TestComputePerformance(t *testing.T) {
	result := compute(1000000)
	if result <= 0 {
		t.Fatal("expected positive result")
	}
}

func BenchmarkCompute(b *testing.B) {
	for i := 0; i < b.N; i++ {
		compute(1000000)
	}
}

func compute(n int) int {
	sum := 0
	for i := 0; i < n; i++ {
		sum += i
	}
	return sum
}
```

**Usage:**
```bash
# Run tests with CPU profiling
go test -cpuprofile=cpu.prof -v ./...

# Run tests with memory profiling
go test -memprofile=mem.prof -v ./...

# Run benchmarks with profiling
go test -bench=. -cpuprofile=bench.prof -benchtime=10s ./...

# Analyze results
go tool pprof cpu.prof
(pprof) web
(pprof) top
```

## Custom Profiling

### Example 5: Profile Specific Operations

```go
package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"runtime/pprof"
	"time"
)

var requestsProfile = pprof.NewProfile("requests")

type Request struct {
	ID        int
	UserID    int
	Operation string
	StartTime time.Time
}

func main() {
	// Capture profile at end
	f, err := os.Create("requests.prof")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	// Process requests
	for i := 1; i <= 100; i++ {
		request := &Request{
			ID:        i,
			UserID:    i % 10,
			Operation: fmt.Sprintf("op-%d", i%5),
			StartTime: time.Now(),
		}
		processRequest(request)
	}

	// Write profile
	if err := requestsProfile.WriteTo(f, 0); err != nil {
		log.Fatal("could not write profile: ", err)
	}
	fmt.Println("Profile written to requests.prof")
}

func processRequest(req *Request) {
	requestsProfile.Add(req, 1)
	defer requestsProfile.Remove(req)

	// Simulate work
	duration := time.Since(req.StartTime)
	fmt.Printf("Processed request %d (%s) in %v\n",
		req.ID, req.Operation, duration)
	time.Sleep(10 * time.Millisecond)
}
```

## Label-Based Profiling

### Example 6: Correlate Profiles with Request Context (Go 1.9+)

```go
package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	_ "net/http/pprof"
	"runtime/pprof"
)

func main() {
	http.HandleFunc("/api/process", handleProcess)

	log.Println("Server on :8080")
	log.Println("Profile at http://localhost:8080/debug/pprof/profile?seconds=30")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func handleProcess(w http.ResponseWriter, r *http.Request) {
	// Extract request parameters
	userID := r.URL.Query().Get("user_id")
	if userID == "" {
		userID = "anonymous"
	}

	endpoint := r.URL.Path
	requestID := r.Header.Get("X-Request-ID")
	if requestID == "" {
		requestID = "unknown"
	}

	// Create labeled context
	ctx := context.Background()
	labels := pprof.Labels(
		"user_id", userID,
		"endpoint", endpoint,
		"request_id", requestID,
	)

	// Execute request with labels
	// All profiling samples are tagged with these labels
	pprof.Do(ctx, labels, func(ctx context.Context) {
		processRequest(ctx, r)
		w.Write([]byte("OK"))
	})
}

func processRequest(ctx context.Context, r *http.Request) {
	// CPU-intensive work here
	sum := 0
	for i := 0; i < 100000000; i++ {
		sum += i * i
	}
	fmt.Printf("Processed: %v\n", sum)
}
```

**Usage:**
```bash
# Start server
go run main.go

# Download CPU profile
go tool pprof http://localhost:8080/debug/pprof/profile?seconds=30

# In pprof, filter by label
(pprof) focus user_id=123
(pprof) top
(pprof) web
```

## Goroutine Leak Detection

### Example 7: Find Goroutine Leaks

```go
package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
	_ "net/http/pprof"
	"runtime"
	"time"
)

func main() {
	http.HandleFunc("/leak", handleLeak)
	http.HandleFunc("/status", handleStatus)

	log.Println("Server on :8080")
	log.Println("Goroutines: http://localhost:8080/debug/pprof/goroutine?debug=1")
	log.Println("Status: http://localhost:8080/status")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func handleLeak(w http.ResponseWriter, r *http.Request) {
	// Spawn goroutine that never exits (leak!)
	go func() {
		for {
			time.Sleep(1 * time.Second)
		}
	}()

	w.Write([]byte("Started background goroutine\n"))
}

func handleStatus(w http.ResponseWriter, r *http.Request) {
	count := runtime.NumGoroutine()
	w.Header().Set("Content-Type", "text/plain")
	fmt.Fprintf(w, "Active goroutines: %d\n", count)
}
```

**Usage:**
```bash
# Start server
go run main.go

# Check initial goroutine count
curl http://localhost:8080/status
# Output: Active goroutines: 2

# Trigger leak multiple times
for i in {1..10}; do
  curl http://localhost:8080/leak
done

# Check goroutine count again
curl http://localhost:8080/status
# Output: Active goroutines: 12 (10 leaked + 2 initial)

# Analyze goroutine profile
curl -o goroutine.prof http://localhost:8080/debug/pprof/goroutine
go tool pprof goroutine.prof
(pprof) top
```

## Mutex Contention Analysis

### Example 8: Detect Lock Contention

```go
package main

import (
	"fmt"
	"log"
	"net/http"
	_ "net/http/pprof"
	"runtime"
	"sync"
	"time"
)

var (
	counter int
	mu      sync.Mutex
)

func main() {
	// Enable mutex profiling
	runtime.SetMutexProfileFraction(1)

	http.HandleFunc("/increment", handleIncrement)

	log.Println("Server on :8080")
	log.Println("Mutex profile: http://localhost:8080/debug/pprof/mutex")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func handleIncrement(w http.ResponseWriter, r *http.Request) {
	// Spawn concurrent increments
	var wg sync.WaitGroup
	for i := 0; i < 100; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			incrementCounter()
		}()
	}
	wg.Wait()

	w.Write([]byte(fmt.Sprintf("Counter: %d\n", counter)))
}

func incrementCounter() {
	mu.Lock()
	defer mu.Unlock()

	counter++
	// Simulate some work
	time.Sleep(1 * time.Millisecond)
}
```

**Usage:**
```bash
# Start server
go run main.go

# Download mutex profile
go tool pprof http://localhost:8080/debug/pprof/mutex

# Analyze contention
(pprof) top          # Shows lock holders and contention
(pprof) list handleIncrement
```

## Production Monitoring Script

### Example 9: Automated Profiling in Production

```bash
#!/bin/bash
# profile-production.sh - Collect profiles from production service

SERVICE_URL="http://prod-service:8080"
OUTPUT_DIR="./profiles/$(date +%Y%m%d-%H%M%S)"
mkdir -p "$OUTPUT_DIR"

echo "Collecting profiles from $SERVICE_URL"

# Collect multiple profiles
echo "Collecting heap profile..."
curl -s "$SERVICE_URL/debug/pprof/heap" > "$OUTPUT_DIR/heap.prof"

echo "Collecting 30-second CPU profile..."
curl -s "$SERVICE_URL/debug/pprof/profile?seconds=30" > "$OUTPUT_DIR/cpu.prof"

echo "Collecting goroutine profile..."
curl -s "$SERVICE_URL/debug/pprof/goroutine" > "$OUTPUT_DIR/goroutine.prof"

echo "Collecting mutex profile..."
curl -s "$SERVICE_URL/debug/pprof/mutex" > "$OUTPUT_DIR/mutex.prof"

echo "Collecting 5-second trace..."
curl -s "$SERVICE_URL/debug/pprof/trace?seconds=5" > "$OUTPUT_DIR/trace.out"

echo "Profiles collected to $OUTPUT_DIR"
echo ""
echo "Analyze with:"
echo "  go tool pprof $OUTPUT_DIR/heap.prof"
echo "  go tool pprof $OUTPUT_DIR/cpu.prof"
echo "  go tool trace $OUTPUT_DIR/trace.out"
```

**Usage:**
```bash
chmod +x profile-production.sh
./profile-production.sh

# Analyze results
go tool pprof ./profiles/20240115-143022/heap.prof
(pprof) top
(pprof) web
```

## Performance Analysis Workflow

### Step-by-Step: Identify Performance Bottleneck

```bash
# 1. Collect CPU profile
go tool pprof http://localhost:8080/debug/pprof/profile?seconds=60

# 2. View top functions
(pprof) top

# 3. Focus on problematic function
(pprof) list functionName

# 4. View as graph
(pprof) web

# 5. Compare with previous run
(pprof) save baseline.prof
# ... make optimization ...
go tool pprof -base baseline.prof http://localhost:8080/debug/pprof/profile?seconds=60
(pprof) top
```

## Memory Leak Diagnosis

```bash
# 1. Take initial heap snapshot
curl http://localhost:8080/debug/pprof/heap > heap1.prof

# 2. Wait 5 minutes...
sleep 300

# 3. Take second snapshot
curl http://localhost:8080/debug/pprof/heap > heap2.prof

# 4. Compare allocations
go tool pprof -base heap1.prof heap2.prof
(pprof) top         # New allocations since first snapshot
(pprof) list       # Source lines
```
