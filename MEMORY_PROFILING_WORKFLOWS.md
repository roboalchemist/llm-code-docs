# Memory Profiling Workflows & Practical Examples

Practical workflows for detecting memory leaks, profiling heap usage, and optimizing memory in different languages and environments.

## Table of Contents

- [C/C++ Workflows](#cc-workflows)
- [Python Workflows](#python-workflows)
- [Java Workflows](#java-workflows)
- [Go Workflows](#go-workflows)
- [Rust Workflows](#rust-workflows)
- [Node.js Workflows](#nodejs-workflows)
- [Production Profiling Workflows](#production-profiling-workflows)
- [Troubleshooting Guides](#troubleshooting-guides)

---

## C/C++ Workflows

### Workflow 1: Quick Memory Error Detection (AddressSanitizer)

**Scenario**: Catch buffer overflows and use-after-free bugs during development.

**Steps**:
```bash
# 1. Compile with AddressSanitizer
clang -fsanitize=address -g -O1 program.c -o program

# 2. Run with verbose error reporting
ASAN_OPTIONS=halt_on_error=0 ./program

# 3. Get detailed leak report
./program 2>&1 | grep -A 5 "SUMMARY"
```

**Output Interpretation**:
```
==12345==ERROR: AddressSanitizer: heap-buffer-overflow on unknown address
    at pc 0x000000123456 bp 0x7fffXXXX sp 0x7fffYYYY T0
Address 0x... is 10 bytes inside a 16-byte region
```

### Workflow 2: Comprehensive Heap Profiling (Valgrind Massif)

**Scenario**: Understand memory usage over time, identify allocation hotspots.

**Steps**:
```bash
# 1. Compile with debug symbols
gcc -g program.c -o program

# 2. Run Valgrind Massif profiler
valgrind --tool=massif --massif-out-file=massif.out ./program

# 3. Generate visualization
ms_print massif.out > heap_report.txt

# 4. View detailed report
cat heap_report.txt | less
```

**Understanding the Output**:
```
    n        time(B)         total(B)   useful-heap(B) extra(B)    stacks(B)
  100    11,457,600       10,263,328    10,054,440    208,888          0
  100    11,457,600       10,263,328    10,054,440    208,888          0  99.95% 0x4A2B8E5: malloc (vg_replace_malloc.c:...)
  100    11,457,600        9,263,328     9,054,440    208,888          0  90.32% 0x401234: init_data (program.c:42)
```

### Workflow 3: Fast Heap Analysis (heaptrack)

**Scenario**: Profile memory allocations with minimal overhead (<15%).

**Steps**:
```bash
# 1. Compile normally (debug symbols helpful but not required)
gcc -g program.c -o program

# 2. Run with heaptrack
heaptrack ./program --some-args

# 3. Analyze with GUI
heaptrack_gui heaptrack.program.<pid>.gz

# 4. In GUI, view:
# - Allocation timeline
# - Top allocating functions
# - Memory growth graph
# - Peak memory usage
```

### Workflow 4: Memory Leak Detection (Valgrind Memcheck)

**Scenario**: Identify memory leaks in long-running applications.

**Steps**:
```bash
# 1. Run Memcheck with leak detection enabled
valgrind --leak-check=full --show-leak-kinds=all \
         --track-origins=yes \
         --log-file=memcheck.log \
         ./program

# 2. Analyze leak report
grep -A 10 "LEAK SUMMARY" memcheck.log

# 3. Find leak source
grep -B 5 "in use" memcheck.log | head -50
```

**Leak Report Example**:
```
==12345== LEAK SUMMARY:
==12345==    definitely lost: 48 bytes in 1 blocks
==12345==    indirectly lost: 0 bytes in 0 blocks
==12345==    possibly lost: 0 bytes in 0 blocks
==12345==    still reachable: 1,024 bytes in 2 blocks
```

### Workflow 5: Production Memory Profiling (Bytehound)

**Scenario**: Profile memory in production with <2% overhead.

**Steps**:
```bash
# 1. Build binary
gcc -g program.c -o program

# 2. Run with bytehound (requires Linux 5.8+)
bytehound ./program

# 3. Real-time analysis at http://localhost:8080
# View allocation timeline, hotspots, memory growth

# 4. Export data for further analysis
# (In UI: Export > Download)
```

---

## Python Workflows

### Workflow 1: Line-by-Line Memory Profiling (memory_profiler)

**Scenario**: Identify which lines consume the most memory.

**Script** (`profile_example.py`):
```python
from memory_profiler import profile

@profile
def load_data():
    large_list = list(range(1000000))
    return sum(large_list)

@profile
def process_data():
    data = {f"key_{i}": i for i in range(100000)}
    return sum(data.values())

if __name__ == "__main__":
    load_data()
    process_data()
```

**Steps**:
```bash
# 1. Install memory_profiler
pip install memory-profiler

# 2. Run profiler
python -m memory_profiler profile_example.py

# 3. Output shows per-line memory usage
```

**Output**:
```
Filename: profile_example.py
Line #    Mem usage    Increment  Occurrences   Line Contents
==========================================================
     3   38.8 MiB      0.0 MiB           1   @profile
     4   38.9 MiB      0.1 MiB           1   def load_data():
     5   78.9 MiB     40.0 MiB           1       large_list = list(range(1000000))
     6   78.9 MiB      0.0 MiB           1       return sum(large_list)
```

### Workflow 2: Multi-Threaded Profiling (Scalene)

**Scenario**: Profile CPU and memory in multi-threaded code.

**Steps**:
```bash
# 1. Install Scalene
pip install scalene

# 2. Run directly (no code changes needed)
scalene myapp.py

# 3. View real-time profiling dashboard
# Shows: CPU, Memory (Python/native), GPU, thread breakdown

# 4. Generate timeline report
scalene --outfile profile.html myapp.py
# Open profile.html in browser
```

### Workflow 3: Memory Leak Detection (tracemalloc)

**Scenario**: Quick memory leak detection without external tools.

**Script** (`check_leaks.py`):
```python
import tracemalloc
import linecache

tracemalloc.start()

# Your code here
def create_leaks():
    leaky_list = []
    for i in range(1000000):
        leaky_list.append([i] * 100)  # Intentional leak
    return leaky_list

create_leaks()

# Take snapshot and get top allocators
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory: {current / 10**6:.1f}MB; Peak: {peak / 10**6:.1f}MB")

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)
```

**Steps**:
```bash
python check_leaks.py
```

### Workflow 4: Production Profiling (py-spy)

**Scenario**: Profile running Python process without code changes.

**Steps**:
```bash
# 1. Find process ID
ps aux | grep python

# 2. Record samples
py-spy record -o profile.svg --pid 12345

# 3. Process for 30 seconds
# (Let it run...)

# 4. View flame graph
open profile.svg  # macOS
# or
firefox profile.svg  # Linux
```

### Workflow 5: Integration Test with Profiling

**Scenario**: Profile specific code paths during testing.

**Script** (`test_with_profile.py`):
```python
import scalene.scalene as scalene
import pytest

def test_memory_intensive():
    scalene.start()

    # Your test code
    large_data = [list(range(1000)) for _ in range(10000)]

    scalene.stop()
    # Results printed to stdout
```

---

## Java Workflows

### Workflow 1: Quick Heap Snapshot (VisualVM)

**Scenario**: Inspect heap contents and find large objects.

**Steps**:
```bash
# 1. Start your Java application
java -jar myapp.jar

# 2. Find Java process
jps -l

# 3. Launch VisualVM
jvisualvm

# 4. In VisualVM:
#    - Double-click target process
#    - Go to "Heap Dump" tab
#    - Click "Heap Dump"
#    - Analyze objects, references, retaining objects
```

### Workflow 2: Leak Detection with Eclipse MAT

**Scenario**: Find memory leaks in heap dumps.

**Steps**:
```bash
# 1. Generate heap dump using jmap
jmap -dump:live,format=b,file=heap.hprof <pid>

# 2. Open Eclipse MAT
# File > Open Heap Dump > heap.hprof

# 3. In MAT:
#    - Right-click > "Leak Suspects Report"
#    - Review suspected leak objects
#    - Check "Retained Objects" for references
```

**Example Leak Report**:
```
Problem Suspect 1

One instance of "com.example.Cache" loaded by "sun.misc.Launcher$AppClassLoader"
occupies 1,048,000 bytes (42% of total heap size).
The memory is accumulated in one instance of "java.util.HashMap" loaded by the same class loader.
```

### Workflow 3: Continuous Profiling with JFR

**Scenario**: Record profiling data for later analysis.

**Steps**:
```bash
# 1. Start application with JFR
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr MyApp

# 2. Wait 60 seconds (or press Ctrl+C)

# 3. Convert to human-readable format
jfr dump --output=output.html recording.jfr

# 4. Open output.html in browser
```

### Workflow 4: Remote Profiling (YourKit)

**Scenario**: Profile application on remote server.

**Steps**:
```bash
# 1. On server: Start with YourKit agent
java -agentpath:/path/to/libyjpagent.so=port=10001 -jar myapp.jar

# 2. On local machine: Connect via YourKit GUI
# File > Connect to Remote VM
# Host: server.example.com, Port: 10001

# 3. Real-time memory profiling with low overhead
```

### Workflow 5: GC Analysis with JFR + jfr tool

**Scenario**: Analyze garbage collection performance.

**Steps**:
```bash
# 1. Create JFR recording (includes GC events)
java -XX:StartFlightRecording=dumponexit=true,filename=gc.jfr MyApp

# 2. Analyze with jfr CLI
jfr print --events GarbageCollection gc.jfr

# 3. View GC timeline in JMC (Java Mission Control)
jmc gc.jfr
```

---

## Go Workflows

### Workflow 1: Built-in pprof Profiling

**Scenario**: Profile CPU and memory allocations.

**Code** (`main.go`):
```go
package main

import (
    "fmt"
    "os"
    "runtime/pprof"
)

func expensiveFunction() {
    data := make([]byte, 1000000000) // 1GB
    _ = data
}

func main() {
    f, _ := os.Create("cpu.prof")
    defer f.Close()
    pprof.StartCPUProfile(f)
    defer pprof.StopCPUProfile()

    expensiveFunction()

    memf, _ := os.Create("mem.prof")
    defer memf.Close()
    pprof.WriteHeapProfile(memf)

    fmt.Println("Profiling complete")
}
```

**Steps**:
```bash
# 1. Build and run
go run main.go

# 2. Analyze with pprof (interactive)
go tool pprof cpu.prof
# (pprof) top10
# (pprof) list expensiveFunction

# 3. Generate graph
go tool pprof -http=:8080 mem.prof
# Opens interactive web UI
```

### Workflow 2: HTTP Server Profiling (net/http/pprof)

**Scenario**: Profile running HTTP service.

**Code** (`server.go`):
```go
package main

import (
    _ "net/http/pprof"
    "net/http"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        // Your handler
    })

    http.ListenAndServe(":6060", nil)
    // pprof endpoints now available at:
    // http://localhost:6060/debug/pprof/
}
```

**Steps**:
```bash
# 1. Start server
go run server.go

# 2. Collect heap profile
go tool pprof http://localhost:6060/debug/pprof/heap

# 3. Collect CPU profile (30 seconds)
go tool pprof http://localhost:6060/debug/pprof/profile?seconds=30

# 4. View in web UI
go tool pprof -http=:8080 http://localhost:6060/debug/pprof/heap
```

### Workflow 3: Production Profiling with Parca

**Scenario**: Continuous profiling in Kubernetes.

**Steps**:
```bash
# 1. Deploy Parca (Helm example)
helm install parca parca-community/parca

# 2. Enable profiling in your app (no code changes!)
# Parca automatically discovers and profiles Go apps

# 3. Access Parca UI
kubectl port-forward svc/parca 7070:7070
# Open http://localhost:7070

# 4. Analyze memory allocations, call stacks over time
```

---

## Rust Workflows

### Workflow 1: Flamegraph Generation (Linux)

**Scenario**: Visualize function call distribution and bottlenecks.

**Steps**:
```bash
# 1. Install flamegraph
cargo install flamegraph

# 2. Add debug info to release build
# Cargo.toml:
# [profile.release]
# debug = true

# 3. Generate flamegraph
cargo flamegraph --bin myapp

# 4. View interactive graph
open flamegraph.svg
```

### Workflow 2: Allocation Profiling (heaptrack on Linux)

**Scenario**: Profile memory allocations in detail.

**Steps**:
```bash
# 1. Build release binary with symbols
cargo build --release

# 2. Run with heaptrack
heaptrack ./target/release/myapp

# 3. Analyze with GUI
heaptrack_gui heaptrack.myapp.<pid>.gz

# 4. View:
#    - Allocation timeline
#    - Top allocating functions
#    - Memory growth
```

### Workflow 3: Instruments Profiling (macOS)

**Scenario**: Profile memory allocations on macOS.

**Steps**:
```bash
# 1. Build with debug symbols
cargo build

# 2. Launch Instruments
# Xcode > Open Developer Tool > Instruments

# 3. Select "System Trace" or "Allocations" template

# 4. Target: cargo (or built binary)

# 5. Record and analyze allocation patterns
```

### Workflow 4: Valgrind Profiling (Linux)

**Scenario**: Comprehensive memory error detection.

**Steps**:
```bash
# 1. Build with debug info
cargo build

# 2. Run with Valgrind
valgrind --leak-check=full --show-leak-kinds=all \
         ./target/debug/myapp

# 3. Review output for memory errors and leaks
```

### Workflow 5: Criterion Benchmarking

**Scenario**: Detect memory-related performance regressions.

**Code** (`benches/memory_bench.rs`):
```rust
use criterion::{black_box, criterion_group, criterion_main, Criterion};

fn memory_intensive(c: &mut Criterion) {
    c.bench_function("allocate_vec", |b| {
        b.iter(|| {
            let v: Vec<i32> = (0..black_box(10000)).collect();
            v
        })
    });
}

criterion_group!(benches, memory_intensive);
criterion_main!(benches);
```

**Steps**:
```bash
# 1. Add to Cargo.toml
# [[bench]]
# name = "memory_bench"
# harness = false

# 2. Run benchmarks
cargo bench

# 3. View results and regressions
```

---

## Node.js Workflows

### Workflow 1: Heap Snapshots via Inspector

**Scenario**: Inspect heap contents and detect leaks.

**Steps**:
```bash
# 1. Start with inspector
node --inspect app.js

# 2. Open Chrome DevTools
# chrome://inspect

# 3. In DevTools:
#    - Memory tab > Take heap snapshot
#    - Compare snapshots over time
#    - Find detached DOM nodes or circular references
```

### Workflow 2: clinic.js Auto-Diagnosis

**Scenario**: Quick diagnosis of performance issues.

**Steps**:
```bash
# 1. Install clinic
npm install -g clinic

# 2. Run doctor mode
clinic doctor -- node app.js

# 3. Interact with app
# (Run normal operations)

# 4. Review auto-generated report
# - Identifies CPU, I/O, or memory issues
# - Recommends tools (flame, doctor, bubbleprof)
```

### Workflow 3: Flame Graph Generation (clinic.js)

**Scenario**: Visualize call stack distribution.

**Steps**:
```bash
# 1. Generate flame graph
clinic flame -- node app.js

# 2. Interact with app

# 3. View interactive flame graph
```

### Workflow 4: 0x Real-Time Profiling

**Scenario**: Quick real-time flame graph.

**Steps**:
```bash
# 1. Install 0x
npm install -g 0x

# 2. Run
0x app.js

# 3. Interact with app

# 4. On exit, opens http://localhost:7070
# Interactive flame graph in browser
```

### Workflow 5: Load Testing + Memory Monitoring

**Scenario**: Find memory leaks under production load.

**Steps**:
```bash
# 1. Start app with inspector
node --inspect app.js

# 2. In separate terminal, run load test
autocannon http://localhost:3000

# 3. In Chrome DevTools:
#    - Monitor memory timeline
#    - Look for memory not being reclaimed after GC
#    - Take snapshots before/after load
```

---

## Production Profiling Workflows

### Workflow: Continuous Profiling with Parca (Multi-Language)

**Scenario**: Monitor memory usage 24/7 across fleet.

**Infrastructure Setup**:
```bash
# 1. Deploy Parca (via Helm/Docker)
docker run -p 7070:7070 ghcr.io/parca-dev/parca:latest

# 2. For each service:
#    - Go: No changes needed (auto-detected)
#    - Python: Run with FIPS-compliant environment
#    - C/C++: Compile with -fno-omit-frame-pointer

# 3. Services auto-report to Parca via eBPF

# 4. Access UI at http://localhost:7070

# 5. Query memory by:
#    - Service name
#    - Function name
#    - Time range
#    - Compare snapshots over hours/days
```

### Workflow: Pyroscope Continuous Profiling (SaaS)

**Scenario**: Managed continuous profiling with historical analysis.

**Setup**:
```bash
# 1. Create Pyroscope account

# 2. Install agent for your language
# Python:
pip install pyroscope-io

# 3. Instrument code
import pyroscope

pyroscope.configure(
    app_name="my-app",
    server_address="https://pyroscope.example.com",
)

# 4. Run application normally
# Continuous profiling happens automatically

# 5. View in Pyroscope dashboard:
# - Flame graphs
# - Memory growth over time
# - Comparison with previous versions
```

### Workflow: Datadog Continuous Profiler

**Scenario**: Integrated observability + profiling.

**Setup**:
```bash
# 1. Install Datadog agent on host

# 2. Enable profiling in agent config
profiling:
  enabled: true

# 3. Restart services
# Profiling auto-activates

# 4. In Datadog dashboard:
#    - View flame graphs
#    - Correlate memory spikes with logs/traces
#    - Set alerts on memory allocation patterns
```

---

## Troubleshooting Guides

### Issue: "Tool reports memory leak that doesn't exist"

**Causes**:
- Static initialization holding memory (not a leak)
- Pool allocators keeping memory for reuse
- Memory-mapped files
- Thread-local storage

**Solutions**:
```c
// Suppress known leaks in Valgrind
#ifdef VALGRIND
#include <valgrind/valgrind.h>
#endif

void cleanup() {
#ifdef VALGRIND
    VALGRIND_DESTROY_MEMPOOL(my_pool);
#endif
}
```

### Issue: AddressSanitizer finds nothing but memory grows

**Causes**:
- Leak is in library code (may need LSAN)
- Heap fragmentation
- Memory pools not freed

**Solutions**:
```bash
# Enable Leak Sanitizer along with AddressSanitizer
clang -fsanitize=address,leak -g program.c

# Increase verbosity
LSAN_OPTIONS=verbosity=1:log_threads=1 ./program
```

### Issue: Production profiler slowing app (<5% overhead requirement not met)

**Causes**:
- Too many sampled events
- Symbol resolution overhead
- Disk I/O for writes

**Solutions**:
```bash
# Reduce sampling frequency
BYTEHOUND_SAMPLE_RATE=1000 ./app  # Every 1000th allocation

# Use async I/O for profile writes
# Use in-memory circular buffer with flush-on-demand
```

### Issue: Memory profiler shows Python using 10GB but app only needs 1GB

**Causes**:
- Python's malloc caching strategy
- Memory not returned to OS immediately
- Fragmentation in allocator

**Solutions**:
```python
# Force malloc trimming (libc only)
import ctypes
ctypes.CDLL(None).malloc_trim(0)

# Or use jemalloc
# LD_PRELOAD=/path/to/libjemalloc.so python app.py
```

### Issue: Heaptrack/perf reports kernel addresses instead of function names

**Causes**:
- Missing debug symbols
- Stripped binary
- ASLR preventing symbol resolution

**Solutions**:
```bash
# Rebuild with debug symbols
gcc -g -fno-omit-frame-pointer program.c -o program

# Use separate debug info
objcopy --only-keep-debug program program.debug
objcopy --strip-debug program
objcopy --add-gnu-debuglink=program.debug program

# Try llvm-symbolizer
heaptrack ./program
llvm-symbolizer < heaptrack.out
```

---

## Quick Reference: Which Tool for Which Problem

| Problem | Best Tool | Language |
|---------|-----------|----------|
| Buffer overflow detection | AddressSanitizer | C/C++ |
| Memory leak hunting | Valgrind/Memcheck | C/C++ |
| Heap hotspots | Heaptrack | C/C++ |
| Production profiling | Bytehound/Parca | C/C++/Multi |
| Data races | ThreadSanitizer | C/C++ |
| Python memory per-line | memory_profiler | Python |
| Python multi-threaded | Scalene | Python |
| Python quick leak check | tracemalloc | Python |
| Java heap objects | VisualVM/Eclipse MAT | Java |
| Java leaks (quick) | VisualVM | Java |
| Java leaks (detailed) | YourKit | Java |
| Go allocations | pprof | Go |
| Go continuous | Parca | Go |
| Rust bottlenecks | Flamegraph | Rust |
| Rust allocations | Heaptrack | Rust |
| Node.js leaks | Chrome DevTools | JavaScript |
| Node.js diagnosis | clinic.js | JavaScript |
| All: production | Continuous Profiler (Parca/Pyroscope/Datadog) | Multi-language |

---

**Last Updated**: 2026-01-01
