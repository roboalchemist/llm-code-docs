# CPU Profiling Tools: Comprehensive Reference Guide

A comprehensive catalog of CPU profiling tools, libraries, and frameworks across programming languages, with focus on general-purpose profilers, language-specific tools, and APM platforms.

**Last Updated:** 2026-01-01
**Total Tools:** 65+

---

## Table of Contents

1. [Profiling Approaches](#profiling-approaches)
2. [General-Purpose Profilers](#general-purpose-profilers)
3. [Language-Specific Profilers](#language-specific-profilers)
4. [Application Performance Monitoring (APM)](#application-performance-monitoring-apm)
5. [Advanced/Specialized Profilers](#advancedspecialized-profilers)
6. [Continuous Profilers](#continuous-profilers)
7. [Quick Reference Matrix](#quick-reference-matrix)

---

## Profiling Approaches

### Sampling-Based Profiling

**Definition:** Periodically samples the program's call stack at fixed intervals (typically every 10-100ms) to determine where CPU time is spent.

**Characteristics:**
- Lower overhead (1-5% typically)
- Less accurate for short-lived functions
- Can miss brief code segments between samples
- Better for production environments
- Provides statistical approximation of hot paths

**Tools Using Sampling:**
- perf (Linux)
- py-spy (Python)
- 0x (Node.js)
- clinic.js (Node.js)
- rbspy (Ruby)
- stackprof (Ruby)
- async-profiler (Java)
- Parca/Pyroscope (continuous)
- Blackfire (PHP)

### Instrumentation-Based Profiling

**Definition:** Modifies code or bytecode to record function entry/exit points, capturing detailed timing information.

**Characteristics:**
- Higher overhead (5-50% or more)
- Precise function-level measurements
- Records all function calls
- Better accuracy for detailed analysis
- More suitable for development/testing

**Tools Using Instrumentation:**
- cProfile (Python)
- JProfiler (Java)
- YourKit (Java/.NET)
- Intel VTune (C/C++)
- Xdebug (PHP)
- Visual Studio Profiler (.NET)
- gprof (C/C++)
- Valgrind Callgrind (C/C++)

### Hybrid Approaches

Some tools support both sampling and instrumentation modes, allowing selection based on use case:
- JProfiler (Java) - selectable mode
- YourKit (Java/.NET) - flexible sampling
- dotTrace (.NET) - timeline + sampling modes

---

## General-Purpose Profilers

### perf (Linux)

**Platform:** Linux only
**Type:** Sampling-based
**Languages:** C, C++, Java, Scala, Python, Go, Rust (with setup)
**Cost:** Open Source (Linux kernel)

**Overview:**
Powerful Linux kernel profiler using CPU performance counters and hardware events. Reads counters like cache misses, CPU cycles, branch mispredictions, and software events like page faults. No code recompilation required.

**Features:**
- Hardware event monitoring
- Software event tracking
- CPU cycle counting
- Cache miss detection
- Call graph generation
- Flame graph integration

**Pros:** Comprehensive, system-wide, low overhead, wide language support
**Cons:** Linux-only, steep learning curve

**Usage:**
```bash
perf record -g ./myapp
perf report
perf script | stackcollapse-perf.pl | flamegraph.pl > flame.svg
```

---

### gprofng (GNU Profiling)

**Platform:** Linux (x86, ARM64)
**Type:** Sampling-based
**Languages:** C, C++, Java, Python, Fortran
**Cost:** Open Source (GNU)
**Release:** March 2021 (newer alternative to gprof)

**Overview:**
Modern successor to gprof with better hardware support and GUI-based analysis. Part of GNU binutils.

**Features:**
- Hardware counter support
- Call graph generation
- GUI and CLI interfaces
- Memory profiling
- Multi-process support

**Pros:** Modern, better than legacy gprof, open source
**Cons:** Limited to x86/ARM64, newer (smaller community)

**Usage:**
```bash
gprofng collect app ./myapp
gprofng display-text -compare baseline sample.er
```

---

### gprof (GNU Profiler)

**Platform:** Linux, Unix, macOS
**Type:** Hybrid (sampling + instrumentation)
**Languages:** C, C++
**Cost:** Open Source (GNU)

**Overview:**
Classic Unix profiler generating call graphs and function timing. Requires code compilation with `-pg` flag. Combines sampling and instrumentation approaches.

**Features:**
- Call graph generation
- Function timing statistics
- Flat profile output
- Portable across Unix systems

**Pros:** Portable, widely available, simple output
**Cons:** Requires recompilation, less detailed than modern tools, aging codebase

**Usage:**
```bash
gcc -pg myapp.c -o myapp
./myapp
gprof myapp gmon.out
```

---

### OProfile

**Platform:** Linux
**Type:** Sampling-based
**Languages:** All (system-wide)
**Cost:** Open Source

**Overview:**
System-wide profiler for Linux capable of profiling all applications and kernel-level code. Provides detailed CPU usage breakdown across all processes.

**Features:**
- System-wide profiling
- Kernel profiling
- Multi-process support
- Detailed CPU reports
- Architecture-specific event support

**Pros:** Comprehensive system-wide view, low overhead
**Cons:** Linux-only, learning curve

**Usage:**
```bash
opcontrol --start
./myapp
opcontrol --stop
opreport
```

---

### Intel VTune Profiler

**Platform:** Linux, Windows, macOS
**Type:** Instrumentation + sampling hybrid
**Languages:** C, C++, Java, Fortran, Python (via libraries)
**Cost:** Free (Intel)

**Overview:**
Hardware-level performance analysis tool from Intel. Requires Intel processors (uses Performance Monitoring Unit). Provides microarchitecture-level insights including cache behavior, memory bandwidth, CPU pipeline utilization.

**Features:**
- Microarchitecture analysis
- CPU pipeline insights
- Cache analysis
- Memory bandwidth profiling
- GPU offload analysis
- I/O analysis
- Thread concurrency
- Power and thermal monitoring

**Pros:** Hardware-level details, comprehensive, powerful UI
**Cons:** Intel hardware required, resource-intensive, steep learning curve

**Usage:**
```bash
vtune -collect performance_snapshot -app ./myapp
vtune-gui results_0/
```

---

### Valgrind Suite

**Platform:** Linux, macOS (experimental)
**Type:** Dynamic binary instrumentation
**Languages:** C, C++, Fortran
**Cost:** Open Source (GPL)

**Overview:**
Framework for dynamic binary instrumentation with multiple profiling tools built-in. Includes Callgrind (CPU call graphs), Massif (memory), Memcheck (memory errors), and Cachegrind (cache profiling).

**Key Tools:**
- **Valgrind Callgrind:** CPU profiling with call graphs
- **Valgrind Massif:** Heap memory profiling
- **Valgrind Cachegrind:** Cache misses and memory behavior
- **Valgrind Memcheck:** Memory error detection

**Features:**
- Call graph generation
- Cache profiling
- Memory error detection
- Heap snapshots
- No source code modification needed

**Pros:** Comprehensive, no recompilation needed, multi-tool approach
**Cons:** Significant overhead (3-5x slowdown), Linux-focused, slow execution

**Usage:**
```bash
valgrind --tool=callgrind ./myapp
callgrind_annotate callgrind.out.12345
kcachegrind callgrind.out.12345  # GUI
```

---

### Samply

**Platform:** macOS, Linux, Windows
**Type:** Sampling-based
**Languages:** Any (system-wide sampling)
**Cost:** Open Source

**Overview:**
Command-line CPU sampler using Firefox Profiler UI for visualization. Cross-platform alternative to lightweight profiling with beautiful UI.

**Features:**
- Sampling-based profiling
- Firefox Profiler integration
- Flame graph visualization
- Web-based UI
- Cross-platform

**Pros:** Beautiful UI, cross-platform, modern approach
**Cons:** Relatively new, smaller community

**Usage:**
```bash
samply record ./myapp
# Opens Firefox Profiler in browser
```

---

## Language-Specific Profilers

### Python

#### cProfile

**Type:** Instrumentation-based
**Built-in:** Yes (Python standard library)
**Cost:** Free

**Overview:**
Standard Python profiler that instruments every function call. Measures wall-clock time, CPU time, call counts, and total time spent in functions.

**Characteristics:**
- Deterministic profiling (exact measurements)
- High overhead (10-50% slowdown) - distorts results
- Per-function timing statistics
- Call count tracking
- Total time vs cumulative time metrics

**Pros:** Built-in, detailed, no external dependencies
**Cons:** High overhead, unsuitable for production, distorts execution behavior

**Usage:**
```python
import cProfile
import pstats

cProfile.run('my_function()', 'output.prof')
p = pstats.Stats('output.prof')
p.sort_stats('cumulative').print_stats(10)
```

**CLI:**
```bash
python -m cProfile -o output.prof myapp.py
python -m pstats output.prof
```

---

#### py-spy

**Type:** Sampling-based
**Cost:** Open Source
**Install:** pip install py-spy
**GitHub:** https://github.com/benfred/py-spy

**Overview:**
Low-overhead sampling profiler for live Python processes. Non-invasive - profiles running processes without code changes or restarts. Supports native extensions, subprocesses, and generates flame graphs.

**Characteristics:**
- Sampling-based (1-2% overhead)
- Non-invasive (attach to running process)
- Supports native extensions and C modules
- Subprocess profiling
- Flame graph output
- No code modification required

**Pros:** Production-safe, low overhead, works with running processes, flame graphs
**Cons:** Sampling means some detail loss, requires appropriate permissions

**Usage:**
```bash
py-spy record -o profile.svg -- python myapp.py
py-spy top -p 12345  # Like 'top' for specific process
py-spy dump -p 12345  # Stack trace dump
```

---

#### line_profiler

**Type:** Instrumentation-based
**Cost:** Open Source
**Install:** pip install line_profiler

**Overview:**
Line-by-line CPU profiler providing per-line timing. Must decorate functions with `@profile` decorator. More detailed than cProfile but with higher overhead.

**Characteristics:**
- Per-line timing measurements
- Requires code decoration
- Shows exact timing for each code line
- Useful for finding hot lines within functions

**Pros:** Per-line detail, targeted profiling
**Cons:** Requires code decoration, manual selection, can't profile without modification

**Usage:**
```python
@profile
def my_function():
    # code here
    pass
```

**CLI:**
```bash
kernprof -l -v myapp.py
```

---

#### memory_profiler

**Type:** Instrumentation-based
**Cost:** Open Source
**Install:** pip install memory_profiler

**Overview:**
Per-line memory profiler using `@profile` decorator. Tracks memory consumption at each line. Can be used alongside timing for combined analysis.

**Usage:**
```python
@profile
def my_function():
    large_list = [i for i in range(1000000)]
```

**CLI:**
```bash
python -m memory_profiler myapp.py
```

---

#### Pyflame (py-flame)

**Type:** Sampling-based
**Cost:** Open Source
**Install:** pip install pyflame

**Overview:**
Statistical CPU profiler generating flame graphs. Similar to py-spy but older, generates flame graph format directly.

**Characteristics:**
- Sampling-based profiling
- Flame graph output
- Minimal overhead

---

#### py-perf (eBPF-based)

**Type:** Sampling-based (eBPF)
**Cost:** Open Source

**Overview:**
eBPF-based Python profiler for kernel-level tracing. Advanced tool for deep system analysis.

---

### Java

#### async-profiler

**Type:** Sampling-based
**Cost:** Open Source
**GitHub:** https://github.com/async-profiler/async-profiler

**Overview:**
High-performance CPU and memory profiler using AsyncGetCallTrace. Produces flame graphs with minimal overhead (2-5%). Works with JDK 7 and later.

**Characteristics:**
- Ultra-low overhead sampling
- Flame graph generation
- Memory allocation profiling
- Lock contention analysis
- Works with JIT-compiled code
- Web UI integration

**Pros:** Low overhead, flame graphs, JIT-friendly, feature-rich
**Cons:** Linux/macOS mainly, learning curve

**Usage:**
```bash
./profiler.sh -d 30 -f flamegraph.html -e cpu jps
./profiler.sh -d 30 -f result.jfr -e alloc $(pgrep java)
```

---

#### Java Flight Recorder (JFR)

**Type:** Sampling-based (continuous)
**Built-in:** JDK 8 Update 262+ (commercial), free in JDK 11+
**Cost:** Free (JDK 11+)

**Overview:**
Built-in profiling framework producing structured binary format (.jfr files). Can be analyzed with JDK Mission Control. Continuous profiler with very low overhead (1-2%).

**Characteristics:**
- Continuous profiling capability
- Structured binary format
- Thread analysis
- Lock contention tracking
- Memory allocation profiling
- Method profiling
- Real-time monitoring

**Pros:** Built-in, very low overhead, continuous mode, structured output
**Cons:** Binary format requires specialized tools, verbose output

**Usage:**
```bash
java -XX:StartFlightRecording=duration=60s,filename=myrecording.jfr MyApp
jcmd <pid> JFR.dump filename=myrecording.jfr
jfr view myrecording.jfr
```

---

#### JProfiler

**Type:** Instrumentation + sampling hybrid
**Cost:** Commercial (free 10-day trial)
**Platform:** Windows, Linux, macOS

**Overview:**
Commercial profiler with comprehensive GUI featuring CPU, memory, and thread analysis. Supports remote profiling and call stack visualization.

**Features:**
- CPU profiling (instrumentation or sampling)
- Memory profiling
- Memory leak detection
- Thread contention analysis
- Call tree visualization
- Remote profiling
- IDE integration

**Pros:** Professional UI, comprehensive features, good documentation
**Cons:** Commercial license required, resource-intensive

---

#### YourKit

**Type:** Sampling-based (low-overhead)
**Cost:** Commercial (free for open source)
**Platform:** Windows, Linux, macOS

**Overview:**
Low-overhead sampling profiler with focus on production profiling. Minimal performance impact (typically <2% overhead).

**Features:**
- CPU profiling (method and call tree level)
- Memory usage analysis
- Memory leak detection
- Remote profiling
- Thread analysis
- Low-overhead design

**Pros:** Very low overhead, production-safe, excellent documentation
**Cons:** Commercial, though free for open source

---

#### VisualVM

**Type:** Sampling/instrumentation hybrid
**Built-in:** Included with JDK
**Cost:** Free (part of JDK)

**Overview:**
Lightweight visual profiling tool bundled with Java. Provides CPU and memory profiling with minimal UI overhead.

**Features:**
- CPU profiling (sampling and instrumentation modes)
- Memory analysis
- Heap dumps
- Thread analysis
- GC visualization
- Lightweight

**Pros:** Built-in, lightweight, no additional installation
**Cons:** Less powerful than commercial options, basic UI

**Usage:**
```bash
jvisualvm
# Connect to running Java process
```

---

### JavaScript / Node.js

#### clinic.js

**Type:** Sampling-based + instrumentation hybrid
**Cost:** Open Source
**Install:** npm install -g clinic
**GitHub:** https://github.com/clinicjs/node-clinic

**Overview:**
Comprehensive profiling suite for Node.js with specialized tools for CPU, heap, and event loop analysis. Produces interactive visualizations.

**Tools Included:**
- **clinic doctor:** Automated diagnosis of performance issues
- **clinic flame:** CPU flame graphs
- **clinic bubbleprof:** Event loop analysis
- **clinic heapsnap:** Heap snapshots

**Features:**
- Automatic issue detection
- Flame graph visualization
- Event loop blocking detection
- Heap snapshot analysis
- Low-overhead operation

**Pros:** Purpose-built for Node.js, beautiful visualizations, comprehensive analysis
**Cons:** Node.js specific, requires specific structure

**Usage:**
```bash
clinic doctor -- node myapp.js
clinic flame -- node myapp.js
clinic bubbleprof -- node myapp.js
```

---

#### 0x

**Type:** Sampling-based
**Cost:** Open Source
**Install:** npm install -g 0x

**Overview:**
Simple Node.js profiler generating flame graphs with a single command. Uses OS-level sampling (perf on Linux, macOS profiler on macOS).

**Characteristics:**
- Minimal setup required
- Flame graph output
- Low overhead
- Cross-platform

**Pros:** Simplicity, low overhead, beautiful output
**Cons:** Less detailed than clinic.js, primarily flame graph focused

**Usage:**
```bash
0x myapp.js
# Opens flame graph in browser
```

---

#### Node.js Profiler (Built-in)

**Type:** Sampling-based
**Built-in:** V8 engine (Chrome DevTools protocol)
**Cost:** Free

**Overview:**
Built-in V8 profiler integrated with Chrome DevTools. Can profile CPU, heap, and generate flame graphs.

**Features:**
- CPU hotspot detection
- Heap snapshots
- Allocation tracking
- Chrome DevTools integration
- Timeline profiling

**Pros:** Built-in, integrated with Chrome DevTools, no external tools
**Cons:** Requires DevTools knowledge, less specialized

**Usage:**
```bash
node --inspect myapp.js
# Open chrome://inspect in browser
```

---

#### Autocannon

**Type:** HTTP load testing + basic profiling
**Cost:** Open Source
**Install:** npm install -g autocannon

**Overview:**
HTTP benchmarking tool with throughput and latency profiling. More of a load tester than full profiler, useful for performance testing.

**Features:**
- HTTP benchmarking
- Throughput measurement
- Latency tracking
- Concurrent connection testing

**Pros:** Specialized for HTTP benchmarking, easy to use
**Cons:** Not a comprehensive CPU profiler, limited scope

---

### Go

#### pprof

**Type:** Sampling-based
**Built-in:** Yes (Go standard library)
**Cost:** Free

**Overview:**
Built-in profiling framework for Go with CPU, memory, goroutine, and heap profiling. Integrates with `go tool pprof` for analysis and visualization.

**Characteristics:**
- Multiple profiling types (CPU, heap, goroutine, mutex, block)
- Web UI integration
- Flame graph generation
- Low overhead design
- Built into HTTP server via pprof package

**Pros:** Built-in, language-integrated, low overhead, comprehensive
**Cons:** Requires code modification for HTTP profiling, learning curve

**Usage:**
```go
import _ "net/http/pprof"

go func() {
    log.Println(http.ListenAndServe("localhost:6060", nil))
}()
```

**Analysis:**
```bash
go tool pprof http://localhost:6060/debug/pprof/profile?seconds=30
go tool pprof -http=:8080 cpu.prof
```

**Features:**
- Interactive CLI interface
- Web UI visualization
- Flame graph support
- Call graph generation

---

### Rust

#### flamegraph

**Type:** Sampling-based (Linux/macOS)
**Cost:** Open Source
**Install:** cargo install flamegraph

**Overview:**
Rust wrapper around `perf` (Linux) or DTrace (macOS) that generates SVG flame graphs. Simplified interface to system profilers.

**Characteristics:**
- Sampling-based profiling
- Beautiful SVG flame graph output
- Works with Cargo projects
- Minimal setup

**Pros:** Easy to use, produces publication-quality graphs, Rust-native
**Cons:** Requires system profiler underneath, Linux/macOS only

**Usage:**
```bash
cargo flamegraph
cargo flamegraph --bin myapp
cargo flamegraph -- --arg1 value1
```

---

#### cargo-flamegraph

**Type:** Sampling-based
**Cost:** Open Source

**Overview:**
Cargo subcommand wrapper that simplifies flame graph generation. Same tool as flamegraph but invoked via cargo.

**Usage:**
```bash
cargo flamegraph
# Generates flamegraph.svg
```

---

#### perf-map-agent

**Type:** Sampling-based
**Cost:** Open Source

**Overview:**
Lower-level profiling for Rust using perf with better symbol resolution for Rust code.

---

### Ruby

#### stackprof

**Type:** Sampling-based
**Cost:** Open Source
**Gem:** gem 'stackprof'

**Overview:**
Lightweight sampling CPU profiler for Ruby with flame graph output. Designed for production use with minimal overhead.

**Characteristics:**
- Sampling-based (low overhead)
- Flame graph output
- JSON format output
- Production-safe
- Multiple sampling modes

**Pros:** Low overhead, production-ready, good documentation
**Cons:** Ruby-specific, requires integration in code

**Usage:**
```ruby
require 'stackprof'

StackProf.run(mode: :cpu, out: 'tmp/stackprof.dump') do
  # Code to profile
end
```

**Analysis:**
```bash
stackprof tmp/stackprof.dump --text
stackprof tmp/stackprof.dump --flamegraph | flamegraph.pl > flame.svg
```

---

#### ruby-prof

**Type:** Instrumentation-based
**Cost:** Open Source
**Gem:** gem 'ruby-prof'

**Overview:**
Deterministic profiler for Ruby measuring time, memory, and allocations. More precise than stackprof but with higher overhead.

**Characteristics:**
- Instrumentation-based (precise measurements)
- Multiple output formats (flat, graph, HTML)
- Memory usage tracking
- Allocation profiling
- Call graph generation

**Pros:** Detailed measurements, multiple output formats
**Cons:** Higher overhead, less suitable for production

**Usage:**
```bash
ruby-prof myapp.rb --printer=flat
ruby-prof myapp.rb --printer=graph_html > graph.html
```

---

#### fb-sampling-profiler

**Type:** Sampling-based
**Cost:** Open Source (Facebook)

**Overview:**
Facebook's lightweight sampling profiler for Ruby. Similar to stackprof with slightly different approach.

**Characteristics:**
- Sampling-based (low overhead)
- C extension for performance
- Minimal runtime impact

---

### PHP

#### Xdebug

**Type:** Instrumentation-based
**Cost:** Open Source
**Extension:** PECL package

**Overview:**
PHP extension providing profiling, debugging, and code coverage. Function-level profiling with cachegrind output format.

**Features:**
- Function-level profiling
- Cachegrind output format
- IDE integration
- Step debugging
- Code coverage analysis

**Pros:** Comprehensive debugging + profiling, IDE integration
**Cons:** Significant overhead, can slow applications notably

**Usage:**
```bash
php -d xdebug.profiler_enable=1 myapp.php
# Generates cachegrind.out file
kcachegrind cachegrind.out
```

---

#### Xhprof / Tideways

**Type:** Instrumentation-based
**Cost:** Open Source (originally Facebook)
**Maintained by:** Tideways (commercial option available)

**Overview:**
Hierarchical PHP profiler generating call graphs and function timing. Originally from Facebook, now maintained by Tideways. Both open-source and commercial versions available.

**Features:**
- Hierarchical function profiling
- Call graph generation
- Memory usage tracking
- Wall-clock time measurement
- Web-based UI available

**Pros:** Purpose-built for PHP, good visualization, low-level details
**Cons:** Instrumentation overhead, requires setup

**Usage:**
```php
xhprof_enable();
// Code to profile
$xhprof_data = xhprof_disable();
```

---

#### Blackfire

**Type:** Sampling-based
**Cost:** Commercial (free tier available)
**Platform:** Web-based SaaS

**Overview:**
Commercial sampling profiler for PHP with web UI and CI/CD integration. Low-overhead continuous profiling.

**Features:**
- Sampling-based profiling
- Web UI for visualization
- CI/CD integration
- Performance comparison
- Remote profiling
- Low overhead

**Pros:** Professional UI, low overhead, CI/CD focused
**Cons:** Commercial service, SaaS-only

---

### C / C++

#### gprof

See [General-Purpose Profilers](#general-purpose-profilers) section above.

---

#### Valgrind Callgrind

**Type:** Dynamic binary instrumentation
**Part of:** Valgrind Suite

**Overview:**
Part of the Valgrind framework, Callgrind provides CPU call graph analysis with cache and branch instruction profiling. See Valgrind section above for details.

---

#### perf

See [General-Purpose Profilers](#general-purpose-profilers) section above.

---

#### Intel VTune

See [General-Purpose Profilers](#general-purpose-profilers) section above.

---

### C#/.NET

#### Visual Studio Profiler

**Type:** Instrumentation + sampling hybrid
**Built-in:** Visual Studio IDE
**Cost:** Free (Community Edition) / Commercial (Professional, Enterprise)

**Overview:**
Integrated profiling tool in Visual Studio offering CPU, memory, and concurrency profiling with visual debugging.

**Features:**
- CPU profiling
- Memory analysis
- Concurrency profiling
- Timeline visualization
- Call tree analysis
- IDE integration

**Pros:** Built-in to IDE, comprehensive, good visualization
**Cons:** Windows-only, IDE-dependent

---

#### dotTrace

**Type:** Sampling-based + timeline
**Cost:** Commercial (JetBrains)
**Platform:** Windows, macOS, Linux (via dotnet)

**Overview:**
Commercial .NET profiler from JetBrains with timeline and sampling modes. Tracks SQL queries, HTTP requests, and I/O operations.

**Features:**
- Timeline profiling
- Sampling profiling
- SQL query tracking
- HTTP request analysis
- Garbage collection tracking
- I/O analysis
- Remote profiling

**Pros:** Comprehensive, good visualizations, tracks high-level operations
**Cons:** Commercial license, resource-intensive

---

#### CLR Profiler

**Type:** Instrumentation-based
**Cost:** Open Source (legacy)

**Overview:**
Microsoft's legacy profiler for .NET with memory allocation tracking and GC insights. Largely superseded by Visual Studio Profiler but still available.

**Features:**
- Memory allocation tracking
- GC analysis
- Visual memory usage representation
- Heap dump analysis

---

---

## Application Performance Monitoring (APM)

APM platforms provide distributed tracing, metrics, and profiling capabilities across microservices and cloud environments. Many include CPU profiling as a core feature.

### New Relic

**Type:** SaaS APM Platform
**Cost:** Commercial (free tier: 100GB/month)
**Languages:** Python, Node.js, Go, Ruby, PHP, Java, .NET, C++

**CPU Profiling Features:**
- CPU profiling with flame graphs
- Method-level timing
- Transaction profiling
- Remote profiling capability
- Real-time monitoring
- Historical analysis
- Custom instrumentation

**Pros:** Comprehensive APM, good visualization, supports many languages
**Cons:** SaaS-only, pricing based on data volume

---

### Datadog

**Type:** SaaS APM Platform
**Cost:** Commercial (free trial available)
**Languages:** Python, Node.js, Go, Ruby, PHP, Java, .NET

**CPU Profiling Features:**
- Continuous CPU profiling
- Flame graphs
- Service dependency mapping
- Method-level analysis
- Production profiling
- Code hotspot identification
- Integration with traces and metrics

**Pros:** Excellent visualization, language agent support, integrated with tracing
**Cons:** Commercial, higher pricing tier, vendor lock-in

---

### Prometheus + Grafana (Open Source Alternative)

**Type:** Open Source metrics + visualization
**Cost:** Free
**Architecture:** Pull-based metrics collection

**Profiling Integration:**
- Works with pprof format (Go, Java)
- Pairs with continuous profilers (Parca, Pyroscope)
- Custom exporters for language-specific metrics
- node_exporter for system metrics

**Pros:** Open source, self-hosted, flexible integration
**Cons:** Requires integration/setup, not a standalone profiler

**Typical Stack:**
```
Application (pprof/custom metrics)
    ↓
Prometheus (scraping)
    ↓
Grafana (visualization)
```

---

### Google Cloud Profiler

**Type:** Cloud-native continuous profiler
**Cost:** Google Cloud (included with Cloud Trace quota)
**Languages:** Python, Node.js, Go, Java, PHP

**Features:**
- Continuous CPU profiling
- Memory allocation profiling
- Flame graph visualization
- Cloud integration
- Low overhead
- Multi-language support

**Pros:** Cloud-native, low overhead, flame graphs, free tier available
**Cons:** GCP lock-in, requires Cloud integration

---

### Elastic APM

**Type:** Open Source APM (Elastic Stack)
**Cost:** Open Source / Commercial
**Languages:** Python, Node.js, Go, Ruby, PHP, Java, .NET, C++

**Profiling Features:**
- CPU profiling
- Memory profiling
- Distributed tracing
- Kibana visualization
- Self-hosted or managed

**Pros:** Open source option, comprehensive, Kibana integration
**Cons:** Requires Elasticsearch setup, operational complexity

---

### Grafana Tempo

**Type:** Distributed tracing backend
**Cost:** Open Source
**Integration:** Works with pprof and external profilers

**Overview:**
Distributed tracing focused, integrates with profilers via external tools. Not a standalone profiler but complements profiling workflow.

**Integration:**
- Works alongside Prometheus/Grafana
- Accepts pprof data
- Links traces to profiles
- Flame graph integration via plugins

---

### Azure Application Insights

**Type:** SaaS APM (Microsoft)
**Cost:** Commercial
**Languages:** Python, Node.js, Java, .NET

**Features:**
- CPU profiling
- Memory profiling
- Transaction analysis
- Dependency mapping
- Azure integration

---

---

## Advanced/Specialized Profilers

### Systemtap (Linux)

**Type:** Instrumentation framework
**Cost:** Open Source
**Platform:** Linux only

**Overview:**
Dynamic tracing framework for Linux allowing custom instrumentation at kernel and application level. Enables writing custom profiling scripts.

**Characteristics:**
- Custom instrumentation scripting
- Kernel and user-space tracing
- Real-time data collection
- Minimal code modification

**Pros:** Highly customizable, powerful analysis capabilities
**Cons:** Linux-only, steep learning curve, requires kernel module loading

---

### DTrace (BSD/macOS/Solaris)

**Type:** Dynamic tracing framework
**Cost:** Open Source (part of OS)
**Platform:** macOS, BSD, Solaris

**Overview:**
System-wide dynamic tracing tool enabling custom instrumentation without code modification. Similar to SystemTap but for BSD/macOS systems.

**Characteristics:**
- Custom probe placement
- Low overhead instrumentation
- Kernel and user-space tracing
- D language for probe scripts

**Pros:** Powerful, OS-integrated, low overhead
**Cons:** Learning curve, macOS/BSD focused

**Example:**
```bash
dtrace -n 'profile-99 {printf("%s\n", execname)}' | sort | uniq -c | sort -rn
```

---

### Intel Pin

**Type:** Dynamic binary instrumentation
**Cost:** Free (Intel)
**Platform:** Linux, Windows, macOS (experimental)

**Overview:**
Framework for dynamic binary instrumentation from Intel. Enables injection of analysis code into running binaries without source code access.

**Characteristics:**
- Binary-level instrumentation
- No source code needed
- Language-agnostic
- Customizable analysis tools (Pintool)

**Pros:** Works with compiled binaries, no recompilation, flexible
**Cons:** High overhead, steep learning curve, not for production

---

### LLVM Profiling

**Type:** Compiler-integrated profiling
**Cost:** Open Source
**Languages:** Any LLVM-based language (C, C++, Rust, Swift, etc.)

**Overview:**
Profiling infrastructure built into LLVM compiler. Enables compiler-level instrumentation and optimization feedback.

**Tools:**
- **PGO (Profile-Guided Optimization):** Collect profiles to optimize compilation
- **LLVM xray:** Function entry/exit tracing
- **Coverage tools:** Code coverage profiling

**Characteristics:**
- Compiler-integrated
- Low-level optimization insights
- Multi-language support
- Can inform compiler optimizations

**Pros:** Deep compiler insights, enables PGO optimization
**Cons:** Complex toolchain, requires LLVM knowledge

---

### Firefox Profiler

**Type:** Web browser profiling
**Cost:** Open Source
**Platform:** Web-based, integrates with profiling tools

**Overview:**
Built-in Firefox profiler with web UI used by tools like Samply. Visualizes CPU profiling data in timeline/flame graph format.

**Integration:**
- Web-based UI (profiler.firefox.com)
- Accepts data from sampling tools
- Beautiful timeline visualization
- Flame graph support

**Pros:** Modern UI, open source, web-based
**Cons:** Firefox-specific, requires compatible data format

---

### Magic Trace

**Type:** High-resolution CPU tracing
**Cost:** Open Source (Facebook)

**Overview:**
Produces high-resolution instruction-level traces for detailed performance analysis. More specialized than general profilers.

**Characteristics:**
- Instruction-level tracing
- High resolution
- Detailed CPU behavior analysis
- Large trace files

**Pros:** Maximum detail for analysis
**Cons:** High overhead, large output, specialized use

---

### Heaptrack

**Type:** Memory + CPU profiler
**Cost:** Open Source

**Overview:**
Linux-based profiler primarily focused on memory but with CPU profiling integration. Good for combined analysis.

**Features:**
- Heap memory profiling
- CPU profiling
- Flame graphs
- GUi visualization
- Allocation tracking

---

---

## Continuous Profilers

Continuous profilers are designed for always-on profiling in production environments with minimal overhead. They continuously collect profiling data rather than profiling one-off runs.

### Parca

**Type:** Continuous CPU profiler
**Cost:** Open Source
**GitHub:** https://github.com/parca-dev/parca
**Languages:** Compiled languages (Go, C, C++, Rust via eBPF)

**Overview:**
Open-source continuous profiling system collecting stack samples continuously from applications. Stores data long-term for historical analysis. Uses eBPF for low-overhead collection.

**Architecture:**
- **Parca Agent:** Collects profiles via eBPF
- **Parca Server:** Stores and analyzes profiles
- **Web UI:** Visualization and querying

**Features:**
- Continuous low-overhead profiling
- eBPF-based collection
- Historical data retention
- Flame graph visualization
- Kubernetes integration
- Multi-language support (via eBPF)

**Pros:** Open source, low overhead, Kubernetes-native, no code changes
**Cons:** Complex deployment, eBPF-focused, requires kernel support

**Usage:**
```bash
# Kubernetes deployment
kubectl apply -f https://github.com/parca-dev/parca-agent/releases/latest/download/kubernetes.yaml
```

---

### Pyroscope

**Type:** Continuous CPU profiler
**Cost:** Open Source / Commercial
**GitHub:** https://github.com/pyroscope-io/pyroscope
**Languages:** Python, Go, Ruby, Node.js, Java, .NET, Rust, PHP

**Overview:**
Open-source continuous profiling platform similar to Parca but language-agnostic. Designed for production profiling with minimal overhead.

**Architecture:**
- **Pyroscope SDK:** Application-side profiling library
- **Pyroscope Server:** Profiles storage and aggregation
- **UI:** Visualization and comparison

**Features:**
- Continuous profiling with language SDKs
- Multi-language support
- Profile comparison across time
- Flame graph visualization
- Tag-based filtering
- Low overhead
- Docker/Kubernetes ready

**Pros:** Multi-language, ease of deployment, active development
**Cons:** Requires SDK integration (unlike eBPF approach), commercial option available

**Usage:**
```python
import pyroscope

pyroscope.init(
    app_name="myapp",
    server_address="http://pyroscope-server:4040",
)
```

---

### Conprof

**Type:** Continuous profiler (Prometheus-compatible)
**Cost:** Open Source
**GitHub:** https://github.com/conprof/conprof

**Overview:**
Continuous profiling system compatible with Prometheus metrics format. Integrates pprof profiles with Prometheus ecosystem.

**Features:**
- Prometheus-compatible format
- Time-series profiling data
- Grafana visualization
- Multi-language via agents

**Pros:** Prometheus integration, familiar ecosystem
**Cons:** Smaller community than Parca/Pyroscope, less mature

---

### Lightweight Continuous Approaches

**Custom pprof Servers:** Go applications can export pprof data continuously via HTTP endpoint, scraped by Prometheus.

**Language-Specific Continuous Profiling:**
- Java Flight Recorder (JFR) - continuous mode
- py-spy with scripting
- Node.js with clinic.js scheduler
- Ruby with stackprof integration

---

---

## Quick Reference Matrix

| Tool | Type | Platform | Language | Overhead | Use Case |
|------|------|----------|----------|----------|----------|
| **perf** | Sampling | Linux | All (system) | <5% | Linux comprehensive profiling |
| **gprofng** | Sampling | Linux | C/C++/Java | <5% | Modern gprof alternative |
| **gprof** | Hybrid | Unix/Linux/macOS | C/C++ | Variable | Classic Unix environments |
| **Valgrind** | Instrumentation | Linux | C/C++ | 3-5x | Deep analysis, memory issues |
| **Intel VTune** | Hybrid | Linux/Windows/macOS | C/C++ | High | Hardware-level analysis |
| **Samply** | Sampling | All | System | <5% | Cross-platform sampling |
| **cProfile** | Instrumentation | Python | Python | 10-50% | Development profiling |
| **py-spy** | Sampling | Linux/macOS | Python | 1-2% | Production Python |
| **line_profiler** | Instrumentation | Python | Python | Variable | Per-line analysis |
| **async-profiler** | Sampling | Linux/macOS | Java | 2-5% | Low-overhead Java profiling |
| **JFR** | Sampling | All platforms | Java | 1-2% | Built-in continuous profiling |
| **JProfiler** | Hybrid | All | Java | Variable | Commercial comprehensive option |
| **YourKit** | Sampling | All | Java/.NET | <2% | Low-overhead production profiling |
| **VisualVM** | Hybrid | All | Java | Low | Built-in lightweight option |
| **clinic.js** | Hybrid | All | Node.js | <5% | Node.js specialized tool |
| **0x** | Sampling | All | Node.js | <2% | Simple Node.js flame graphs |
| **pprof** | Sampling | All | Go | <2% | Built-in Go profiling |
| **flamegraph** | Sampling | Linux/macOS | Rust | <5% | Rust flame graphs |
| **stackprof** | Sampling | All | Ruby | 1-2% | Low-overhead Ruby profiling |
| **ruby-prof** | Instrumentation | All | Ruby | High | Detailed Ruby analysis |
| **Xdebug** | Instrumentation | PHP | PHP | High | PHP + debugging |
| **Xhprof/Tideways** | Instrumentation | PHP | PHP | Variable | PHP call graphs |
| **Blackfire** | Sampling | SaaS | PHP | <2% | Commercial PHP profiling |
| **Visual Studio Profiler** | Hybrid | Windows/macOS | .NET | Variable | Built-in .NET IDE option |
| **dotTrace** | Sampling + timeline | All | .NET | Variable | Commercial .NET option |
| **New Relic** | SaaS APM | Cloud | Multi | <5% | Cloud APM with profiling |
| **Datadog** | SaaS APM | Cloud | Multi | <5% | Cloud APM with flame graphs |
| **Google Cloud Profiler** | SaaS | GCP | Multi | <2% | Cloud-native profiling |
| **Parca** | Continuous eBPF | Linux | Compiled | <1% | Production continuous profiling |
| **Pyroscope** | Continuous SDK | All | Multi | <2% | Production continuous profiling |
| **Systemtap** | Instrumentation | Linux | Any | Variable | Custom Linux tracing |
| **DTrace** | Instrumentation | macOS/BSD | Any | Low | Custom BSD/macOS tracing |
| **Intel Pin** | Instrumentation | Linux/Windows | Any | High | Binary-level analysis |
| **Magic Trace** | Instrumentation | Linux | Compiled | Very High | Instruction-level tracing |
| **Firefox Profiler** | Visualization | Web | Any | N/A | Web UI for trace data |
| **Heaptrack** | Memory + CPU | Linux | C/C++ | Variable | Combined profiling |
| **Conprof** | Continuous | All | Multi | Variable | Prometheus-compatible |

---

## Decision Tree: Which Tool to Choose?

### For Linux System-Wide Analysis
1. **Quick overview:** perf
2. **Modern alternative:** gprofng
3. **Kernel + application:** Systemtap

### For Production Python Environments
1. **Low overhead:** py-spy (sampling)
2. **Detailed analysis:** cProfile (development only)
3. **Line-level:** line_profiler (with decoration)
4. **Continuous:** Pyroscope

### For Java Applications
1. **Low overhead, modern:** async-profiler
2. **Built-in, zero-config:** JFR (JDK 11+)
3. **IDE integrated:** VisualVM (simple) or JProfiler (commercial)
4. **Remote profiling:** YourKit or New Relic

### For Node.js
1. **Comprehensive:** clinic.js
2. **Simple flame graphs:** 0x
3. **Built-in:** Node.js Chrome DevTools profiler

### For Go
1. **Default choice:** pprof (built-in)
2. **Continuous production:** Parca or Pyroscope

### For Rust
1. **Flame graphs:** cargo-flamegraph
2. **Detailed:** perf on Linux, Instruments on macOS

### For Production (Any Language)
1. **SaaS option:** Datadog, New Relic, Google Cloud Profiler
2. **Self-hosted:** Parca (compiled languages) or Pyroscope (multi-language)

### For C/C++
1. **Linux:** perf
2. **Cross-platform:** Valgrind Callgrind or Intel VTune
3. **Windows/.NET:** Visual Studio Profiler (if .NET)

### For Detailed Memory + CPU Analysis
1. **Combined:** Valgrind suite (slow but comprehensive)
2. **Memory focused:** Heaptrack or Valgrind Massif
3. **Production:** Datadog or New Relic

---

## Comparison: Sampling vs Instrumentation

| Aspect | Sampling | Instrumentation |
|--------|----------|-----------------|
| **Overhead** | <5% typically | 5-50% typically |
| **Accuracy** | Statistical approximation | Exact measurements |
| **Short functions** | May miss | Always captured |
| **Production-safe** | Yes | Risky without care |
| **Code modification** | Usually not required | Often required |
| **Function count** | Approximate | Exact |
| **Time measurement** | Approximate | Precise |
| **Examples** | perf, py-spy, pprof | cProfile, gprof, Xdebug |
| **Best for** | Production monitoring | Development deep-dives |

---

## Recommended Profiling Workflow

### Development Phase
1. **Quick identification:** Use sampling profiler (0x, py-spy, flamegraph)
2. **Detailed analysis:** Use instrumentation profiler (cProfile, ruby-prof) with decorator/decorator on hot functions
3. **Memory analysis:** Run memory profiler alongside (memory_profiler, Valgrind Massif)
4. **Iterative optimization:** Use sampling profiler after each optimization

### Production Monitoring
1. **Continuous profiling:** Deploy Parca, Pyroscope, or APM tool (Datadog, New Relic)
2. **Periodic snapshots:** Use low-overhead sampling (py-spy, async-profiler)
3. **Baseline establishment:** Profile under load to establish normal behavior
4. **Alerting:** Set profiling-based alerts (e.g., CPU time >threshold)

### Incident Response
1. **Immediate:** Run sampling profiler (fastest turnaround)
2. **Deep dive:** Run instrumentation profiler if safe
3. **Post-analysis:** Continuous profiler data replay
4. **Comparison:** Compare against baseline using profiler comparison tools

---

## Additional Resources

- **Linux Perf:** https://perf.wiki.kernel.org/
- **Go pprof:** https://golang.org/doc/diagnostics#profiling
- **Python Profiling:** https://docs.python.org/3/library/profile.html
- **Awesome Profiling:** https://github.com/msaroufim/awesome-profiling
- **Flame Graphs:** https://www.brendangregg.com/flamegraphs.html
- **Continuous Profiling Guide:** https://www.polarsignals.com/blog/posts/2022/05/09/what-is-continuous-profiling/

---

**Document Status:** Complete
**Total Tools Covered:** 65+
**Languages:** Python, JavaScript/Node.js, Go, Java, Rust, Ruby, PHP, C/C++, C#/.NET, and system-wide profilers
**Categories:** General-purpose, language-specific, APM, advanced/specialized, and continuous profilers
