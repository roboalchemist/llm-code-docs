# CPU Profiling Tools: Quick Reference

Fast lookup guide for selecting the right profiling tool for your use case.

---

## By Programming Language

### Python

| Use Case | Primary Tool | Alternative | Notes |
|----------|-------------|-------------|-------|
| Development (detailed) | `cProfile` | `line_profiler` | High overhead but precise; good for development |
| Production (low overhead) | `py-spy` | `stackprof` pattern | Sampling-based; non-invasive; 1-2% overhead |
| Per-line analysis | `line_profiler` | `cProfile` + manual | Requires @profile decorator |
| Memory analysis | `memory_profiler` | Valgrind | Line-by-line memory consumption |
| Continuous monitoring | `Pyroscope` | New Relic/Datadog | Always-on production profiling |
| Cloud-hosted | `Google Cloud Profiler` | Datadog APM | Cloud-native profiling |

**Quick start:** `py-spy record -o profile.svg -- python myapp.py`

---

### JavaScript / Node.js

| Use Case | Primary Tool | Alternative | Notes |
|----------|-------------|-------------|-------|
| Comprehensive analysis | `clinic.js` | `0x` | Full suite: CPU, heap, event loop |
| Simple flame graphs | `0x` | `flamegraph` | One-command flame graph generation |
| Event loop problems | `clinic.js bubbleprof` | Custom instrumentation | Specialized for async issues |
| Chrome DevTools integration | Node.js built-in profiler | `clinic.js` | No external tools needed |
| Production monitoring | `Pyroscope` | New Relic/Datadog | Continuous low-overhead profiling |
| HTTP benchmarking | `autocannon` | Artillery | Load testing with metrics |

**Quick start:** `clinic.js doctor -- node myapp.js`

---

### Go

| Use Case | Primary Tool | Alternative | Notes |
|----------|-------------|-------------|-------|
| Default choice | `pprof` (built-in) | `flamegraph` | Use the built-in tool; no alternatives needed |
| Flame graphs | `go tool pprof` with `-http` | `flamegraph` script | Web UI included in pprof |
| Production profiling | `Parca` | `Pyroscope` + agent | eBPF-based; no code changes; continuous |
| Cloud profiling | `Google Cloud Profiler` | Datadog | Cloud-native; GCP integration |
| Custom tracing | Instrumentation in code | `Parca agent` | Use pprof hooks in application |

**Quick start:** `go tool pprof http://localhost:6060/debug/pprof/profile?seconds=30`

---

### Java

| Use Case | Primary Tool | Alternative | Notes |
|----------|-------------|-------------|-------|
| Built-in, modern | `JFR` (JDK 11+) | `JProfiler` | Zero-config; very low overhead; continuous |
| Low-overhead sampling | `async-profiler` | `JFR` | 2-5% overhead; flame graphs; modern |
| IDE integrated | `VisualVM` | `JProfiler` (commercial) | Lightweight; no installation; built-in |
| Commercial option | `JProfiler` | `YourKit` | Comprehensive GUI; good for teams |
| Production low-overhead | `YourKit` | `async-profiler` | <2% overhead; excellent documentation |
| APM integration | `New Relic` | `Datadog` | Full APM stack with profiling |

**Quick start:** `jcmd <pid> JFR.start duration=60s filename=recording.jfr`

---

### Rust

| Use Case | Primary Tool | Alternative | Notes |
|----------|-------------|-------------|-------|
| Flame graphs | `cargo-flamegraph` | `flamegraph` crate | Cargo integration; easy to use |
| Detailed analysis | `perf` (Linux) | `Instruments` (macOS) | OS-specific profilers |
| Production profiling | `Parca` (via eBPF) | Custom integration | Compiled language support via eBPF |
| macOS | `Instruments` + `flamegraph` | Samply | Native macOS profiling tool |

**Quick start:** `cargo flamegraph` (generates `flamegraph.svg`)

---

### Ruby

| Use Case | Primary Tool | Alternative | Notes |
|----------|-------------|-------------|-------|
| Production (low overhead) | `stackprof` | `rbspy` | Sampling-based; 1-2% overhead |
| Development (detailed) | `ruby-prof` | `stackprof` with instrumentation | High overhead; detailed measurements |
| Flame graphs | `stackprof` with flamegraph | `rbspy` | Integrate stackprof output with flamegraph.pl |
| Continuous monitoring | `Pyroscope` + Ruby agent | New Relic/Datadog | Always-on profiling with SDK |

**Quick start:**
```bash
ruby-prof myapp.rb --printer=flat
# or
stackprof --flamegraph tmp/stackprof.dump | flamegraph.pl > flame.svg
```

---

### PHP

| Use Case | Primary Tool | Alternative | Notes |
|----------|-------------|-------------|-------|
| Development + debugging | `Xdebug` | `Xhprof` | Comprehensive debugging + profiling |
| Specialized profiling | `Xhprof / Tideways` | `Xdebug` | Good for hierarchical analysis |
| Commercial option | `Blackfire` | Tideways | SaaS; low-overhead sampling; CI/CD integration |
| Production profiling | `Blackfire` | APM tool | Low overhead; web UI; comparison tools |

**Quick start:** Enable Xdebug profiler in php.ini, analyze with kcachegrind

---

### C / C++

| Use Case | Primary Tool | Alternative | Notes |
|----------|-------------|-------------|-------|
| Linux system-wide | `perf` | `gprofng` | Hardware counters; CPU cycles; cache misses |
| Cross-platform | `gprof` | `Valgrind Callgrind` | Portable; classic tool; requires -pg flag |
| Deep analysis | `Valgrind Callgrind` | `perf` + Flamegraph | Comprehensive but slow (3-5x overhead) |
| Hardware optimization | `Intel VTune` | `perf` | Microarchitecture insights; Intel hardware |
| macOS/BSD | `Instruments` | `DTrace` | Native OS profiler; custom tracing |
| Memory + CPU combined | `Valgrind suite` | `Heaptrack` | Comprehensive; slow but thorough |

**Quick start:** `perf record -g ./myapp && perf report`

---

### C#/.NET

| Use Case | Primary Tool | Alternative | Notes |
|----------|-------------|-------------|-------|
| Built-in IDE | `Visual Studio Profiler` | `dotTrace` (paid) | Free; integrated; comprehensive |
| Commercial option | `dotTrace` | `YourKit` for .NET | Timeline + sampling; tracks SQL/HTTP |
| Legacy profiling | `CLR Profiler` | `Visual Studio Profiler` | Older tool; memory-focused |

**Quick start:** Visual Studio > Analyze > Performance Profiler

---

## By Environment

### Development / Testing

**Recommended approach:** Sampling first, then instrumentation if needed

| Language | Primary | Details |
|----------|---------|---------|
| Python | `cProfile` then `py-spy` | Understand call graph, then identify hotspots |
| Node.js | `clinic.js` | Comprehensive suite tailored for development |
| Go | `pprof` | Built-in; start here |
| Java | `JFR` or `async-profiler` | Modern options; low overhead |
| Ruby | `ruby-prof` | Detailed instrumentation-based analysis |
| PHP | `Xdebug` | Integrated with debugging |
| C/C++ | `perf` (Linux) or `gprof` (portable) | Depends on platform |
| Rust | `cargo-flamegraph` | Easy Cargo integration |

---

### Production / Long-Running Services

**Recommended approach:** Low-overhead continuous sampling

| Language | Primary | Details |
|----------|---------|---------|
| Python | `py-spy` or `Pyroscope` | Non-invasive sampling; continuous option available |
| Node.js | `clinic.js` or `Pyroscope` | Production-safe; event loop aware |
| Go | `pprof` endpoints or `Parca` | Built-in HTTP endpoints; continuous eBPF |
| Java | `JFR` or `async-profiler` | Very low overhead (1-5%) |
| Ruby | `stackprof` or `Pyroscope` | Low-overhead sampling; production-safe |
| PHP | `Blackfire` | Commercial but low-overhead sampling |
| C/C++ | `perf` (Linux) | System-wide; low overhead |
| Rust | `Parca` (eBPF) | Compiled language support |

---

### Cloud-Hosted / Multi-Language Environments

**Recommended:** APM platform with integrated profiling

| Platform | Primary | Details |
|----------|---------|---------|
| AWS | `New Relic` or `Datadog` | General APM; both have profiling |
| GCP | `Google Cloud Profiler` | Native GCP integration; low cost |
| Azure | `Azure Application Insights` | Microsoft's APM; good .NET support |
| Generic Cloud | `Datadog` | Best-in-class visualizations; multi-language |
| Self-Hosted | `Pyroscope` or `Parca` | Open source; flexible deployment |
| Observability-First | `Prometheus + Pyroscope/Parca` | Metrics + profiling integration |

---

### Continuous Production Profiling (Always-On)

**Tools:** Parca, Pyroscope, Google Cloud Profiler, JFR (Java)

| Language | Recommended | Deployment |
|----------|-------------|------------|
| Go | `Parca` | eBPF agent (no code changes) |
| Java | `JFR` (built-in) | Enable JFR; collect periodically |
| Python | `Pyroscope` | Lightweight SDK integration |
| Node.js | `Pyroscope` | npm module integration |
| Ruby | `Pyroscope` | Ruby gem integration |
| .NET | `dotTrace` agent | JetBrains continuous option |
| C/C++ | `Parca` | eBPF agent; compiled languages only |
| PHP | `Blackfire` or `Pyroscope` | Blackfire (commercial); Pyroscope (SDK) |

---

## By Profiling Approach

### Sampling-Based (Low Overhead)

**Characteristics:** ~1-5% overhead; approximation of hotspots; production-safe

| Tool | Language(s) | Details |
|------|-------------|---------|
| `perf` | All (Linux) | Linux kernel profiler; hardware counters |
| `py-spy` | Python | Non-invasive; 1-2% overhead |
| `async-profiler` | Java | Ultra-low overhead; flame graphs |
| `stackprof` | Ruby | Production-safe; flame graph output |
| `0x` | Node.js | Simple; minimal setup |
| `pprof` | Go | Built-in; low overhead |
| `flamegraph` | Rust | Simplified flame graph generation |
| `Pyroscope` | Multi | Continuous sampling via SDKs |
| `Parca` | Compiled | eBPF-based; no code changes |

**When to use:** Production monitoring, continuous profiling, low-overhead analysis

---

### Instrumentation-Based (Detailed)

**Characteristics:** 5-50%+ overhead; exact measurements; development-focused

| Tool | Language(s) | Details |
|------|-------------|---------|
| `cProfile` | Python | Built-in; high overhead; detailed |
| `gprof` | C/C++ | Classic Unix tool; requires -pg |
| `JProfiler` | Java | Commercial; comprehensive; high overhead |
| `ruby-prof` | Ruby | Instrumentation-based; detailed metrics |
| `Xdebug` | PHP | Integrated debugging + profiling |
| `Valgrind Callgrind` | C/C++ | Comprehensive but slow (3-5x) |
| `Visual Studio Profiler` | C#/.NET | IDE-integrated; powerful |

**When to use:** Development deep-dives, detailed function analysis, accuracy priority

---

### Hybrid (Both Modes)

**Characteristics:** Flexible; choose sampling or instrumentation depending on use case

| Tool | Language(s) | Details |
|------|-------------|---------|
| `JFR` | Java | Sampling-focused; structured format |
| `gprofng` | C/C++ | Modern; both modes; replaces gprof |
| `Intel VTune` | C/C++ | Hardware analysis; both modes |
| `VisualVM` | Java | Lightweight; both modes available |
| `JProfiler` | Java | Commercial; selectable mode |
| `YourKit` | Java/.NET | Low-overhead sampling + detailed options |
| `clinic.js` | Node.js | Multiple specialized tools |
| `Valgrind` | C/C++ | Suite; choose specific tool per use case |

**When to use:** Flexibility; start with sampling, drill down with instrumentation if needed

---

## Quick Decision Matrix

### "My app is slow. Which profiler should I use?"

```
1. What language?
   ├─ Python → py-spy (production) or cProfile (development)
   ├─ Node.js → clinic.js (comprehensive) or 0x (simple)
   ├─ Go → pprof (always)
   ├─ Java → JFR (modern) or async-profiler (low-overhead)
   ├─ Ruby → stackprof (production) or ruby-prof (detailed)
   ├─ PHP → Blackfire (commercial) or Xhprof (open source)
   ├─ C/C++ → perf (Linux) or gprof (portable)
   ├─ Rust → cargo-flamegraph (easy) or perf (detailed)
   └─ .NET → Visual Studio Profiler (built-in)

2. Can you modify the app / restart it?
   ├─ Yes → Use instrumentation profilers for detailed analysis
   └─ No → Use sampling profilers (py-spy, 0x, async-profiler)

3. Production or development?
   ├─ Production → Sampling profiler (low overhead)
   └─ Development → Either; instrumentation for detail

4. Is it a framework issue or code issue?
   ├─ Framework (slow framework calls) → Use instrumentation to see internal calls
   └─ Code logic → Use sampling to find hotspots
```

---

## Selection by Overhead Tolerance

### <2% overhead (Safe for production)

- `py-spy` (Python)
- `async-profiler` (Java)
- `stackprof` (Ruby)
- `Blackfire` (PHP)
- `pprof` (Go)
- `JFR` (Java)
- `Pyroscope` (Multi)
- `Parca` (Compiled)
- `YourKit` (Java/.NET)
- `Google Cloud Profiler` (Multi)

### 2-5% overhead (Production-safe with caution)

- `perf` (Linux)
- `0x` (Node.js)
- `clinic.js` (Node.js)
- `flamegraph` (Rust)
- `gprofng` (Linux)

### 5-50% overhead (Development only)

- `cProfile` (Python)
- `ruby-prof` (Ruby)
- `JProfiler` (Java)
- `Xdebug` (PHP)
- `gprof` (C/C++)
- `Visual Studio Profiler` (.NET)
- `line_profiler` (Python)

### 3-5x+ overhead (Deep analysis, not for production)

- `Valgrind` (C/C++)
- `Intel Pin` (Binary analysis)
- `Heaptrack` (C/C++)

---

## Tool Comparison: Common Use Cases

### "I need flame graphs"

| Tool | Language | Overhead | Effort |
|------|----------|----------|--------|
| `flamegraph` command | C/C++ (Linux) | Low | Easy |
| `py-spy` | Python | Very Low | Easy |
| `async-profiler` | Java | Very Low | Easy |
| `cargo-flamegraph` | Rust | Low | Very Easy |
| `0x` | Node.js | Very Low | Very Easy |
| `stackprof` + script | Ruby | Very Low | Medium |
| `pprof` with `-http` | Go | Very Low | Easy |
| `clinic.js flame` | Node.js | Low | Easy |

**Winner by ease:** `cargo-flamegraph`, `0x`, `clinic.js flame`

---

### "I need to profile running production app without restarting"

| Tool | Language | Method | Difficulty |
|------|----------|--------|------------|
| `py-spy` | Python | Attach to PID | Very Easy |
| `async-profiler` | Java | Attach to PID | Medium |
| `DTrace` | macOS | Custom scripts | Hard |
| `Systemtap` | Linux | Custom scripts | Hard |
| `perf` | Linux | Attach to PID | Medium |
| `0x` | Node.js | Must wrap command | Easy |
| `pprof endpoints` | Go | HTTP endpoint | Easy (if app instrumented) |

**Winner:** `py-spy` (easiest for Python)

---

### "I need continuous always-on profiling"

| Tool | Language(s) | Overhead | Deployment |
|------|-------------|----------|------------|
| `Parca` | Compiled (eBPF) | <1% | Agent-based |
| `Pyroscope` | Multi | <2% | SDK-based |
| `JFR` | Java | 1-2% | Built-in flag |
| `Google Cloud Profiler` | Multi | <2% | Cloud API |
| `Datadog` | Multi | <5% | Agent-based |

**Winner overall:** `Parca` (for compiled) or `Pyroscope` (for flexibility)

---

### "I need detailed function-by-function timing"

| Tool | Language | Type | Overhead |
|------|----------|------|----------|
| `cProfile` | Python | Instrumentation | 10-50% |
| `ruby-prof` | Ruby | Instrumentation | High |
| `JProfiler` | Java | Hybrid | Medium-High |
| `Xhprof` | PHP | Instrumentation | Medium |
| `gprof` | C/C++ | Hybrid | Variable |
| `Valgrind Callgrind` | C/C++ | Instrumentation | 3-5x |

**Winner for detail:** `cProfile` (Python) or `Valgrind` (C/C++; if slow is acceptable)

---

### "I need to find memory leaks"

| Tool | Language | Type | Details |
|------|----------|------|---------|
| `Valgrind Memcheck` | C/C++ | Instrumentation | Most comprehensive |
| `memory_profiler` | Python | Line-by-line | Per-line memory tracking |
| `JProfiler` | Java | Instrumentation | Memory leak detection |
| `YourKit` | Java/.NET | Sampling | Memory leak analysis |
| `Heaptrack` | C/C++ | Instrumentation | Heap-focused |

**Winner:** `Valgrind Memcheck` (C/C++) or `JProfiler` (Java)

---

## Installation Quick Reference

### Language-Specific Package Managers

```bash
# Python
pip install py-spy line_profiler memory_profiler pyroscope-agent

# Node.js
npm install -g clinic 0x pyroscope-nodejs

# Ruby
gem install stackprof ruby-prof pyroscope-ruby

# PHP
pecl install xdebug  # or use Blackfire

# Go
# pprof is built-in; no installation needed

# Rust
cargo install flamegraph

# Java
# JFR is built-in JDK 11+
# async-profiler via GitHub releases
```

### System Package Managers

```bash
# macOS (Homebrew)
brew install perf-tools-next  # Linux tools on macOS
brew install dtruss           # DTrace alternatives

# Linux (apt/yum)
apt-get install linux-tools   # perf, etc.
apt-get install valgrind
apt-get install graphviz      # For gprof visualization

# From source
# See tool-specific documentation
```

---

## Common Patterns

### Development Workflow (Finding bottleneck)

```bash
# 1. Run profiler
py-spy record -o profile.svg -- python myapp.py

# 2. Check flame graph
open profile.svg

# 3. Find hot path (tallest stack)
# 4. Use instrumentation for detail (if needed)
python -m cProfile -o output.prof myapp.py
python -m pstats output.prof
```

### Production Issue (Low-overhead investigation)

```bash
# 1. Attach sampling profiler
py-spy dump -p <PID>  # Stack trace of running process

# 2. Continuous sampling
py-spy record -p <PID> -o production.svg --duration 60

# 3. Analyze output
open production.svg
```

### Continuous Monitoring (Always-on)

```bash
# 1. Deploy continuous profiler
docker run -e PYROSCOPE_APPLICATION_NAME=myapp pyroscope-agent

# 2. Access UI
# Visit http://pyroscope-server:4040

# 3. Analyze trends over time
```

---

## Performance Expectations

### Sampling Profilers (Typical Overhead)

- `perf`: <5%
- `py-spy`: 1-2%
- `async-profiler`: 2-5%
- `stackprof`: 1-2%
- `pprof`: <2%
- `JFR`: 1-2%
- `0x`: <2%

### Instrumentation Profilers (Typical Overhead)

- `cProfile`: 10-50% (distorts results)
- `gprof`: 5-15%
- `ruby-prof`: 10-30%
- `Xdebug`: 10-50%
- `JProfiler`: 5-20%
- `Valgrind`: 3-5x (100-400% slowdown)

---

**Key Takeaway:** Start with sampling profilers in production; use instrumentation in development for detail.
