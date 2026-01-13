# CPU Profiling Tools: Complete Documentation Index

Comprehensive index for CPU profiling tools, frameworks, and methodologies across all programming languages.

**Generated:** 2026-01-01
**Total Tools Covered:** 65+
**Languages:** Python, JavaScript/Node.js, Go, Java, Rust, Ruby, PHP, C/C++, C#/.NET, and system-wide profilers
**Documentation Files:** 4

---

## Quick Navigation

### For Different Needs

- **"I need to profile my app and don't know where to start"** → [CPU_PROFILING_TOOLS_QUICK_REFERENCE.md](CPU_PROFILING_TOOLS_QUICK_REFERENCE.md)
- **"I need detailed tool information and comparisons"** → [CPU_PROFILING_TOOLS_COMPREHENSIVE.md](CPU_PROFILING_TOOLS_COMPREHENSIVE.md)
- **"I need a quick lookup table"** → [CPU_PROFILING_TOOLS_CATALOG.csv](CPU_PROFILING_TOOLS_CATALOG.csv)
- **"I need to understand sampling vs instrumentation"** → [CPU_PROFILING_SAMPLING_VS_INSTRUMENTATION.md](CPU_PROFILING_SAMPLING_VS_INSTRUMENTATION.md)

---

## Document Overview

### 1. CPU_PROFILING_TOOLS_COMPREHENSIVE.md (41KB)

**Purpose:** Complete reference guide with detailed tool descriptions

**Contents:**
- Profiling approaches (sampling, instrumentation, hybrid)
- 50+ tool descriptions with features and examples
- General-purpose profilers (perf, gprof, gprofng, OProfile, Valgrind, Intel VTune, Samply)
- Language-specific tools (Python, Java, JavaScript/Node.js, Go, Rust, Ruby, PHP, C/C++, C#/.NET)
- APM platforms (New Relic, Datadog, Google Cloud Profiler, Elastic APM, Grafana Tempo)
- Advanced/specialized profilers (Systemtap, DTrace, Intel Pin, LLVM, Firefox Profiler, Heaptrack, Magic Trace)
- Continuous profilers (Parca, Pyroscope, Conprof)
- Detailed comparison matrix
- Decision tree for tool selection
- Recommended workflow

**Best for:** Deep understanding, complete reference, detailed comparisons

**Key Sections:**
- Profiling Approaches (Sampling vs Instrumentation)
- General-Purpose Profilers (8 tools)
- Language-Specific Profilers (30+ tools)
  - Python (5 tools)
  - Java (5 tools)
  - JavaScript/Node.js (5 tools)
  - Go (1 tool with deep detail)
  - Rust (3 tools)
  - Ruby (3 tools)
  - PHP (3 tools)
  - C/C++ (4 tools)
  - C#/.NET (3 tools)
- APM Tools (6 platforms)
- Advanced Profilers (9 tools)
- Continuous Profilers (3 tools)
- Quick Reference Matrix (50+ tools)
- Decision Tree
- Additional Resources

---

### 2. CPU_PROFILING_TOOLS_QUICK_REFERENCE.md (17KB)

**Purpose:** Fast lookup and decision-making guide

**Contents:**
- By programming language (Python, JavaScript, Go, Java, Rust, Ruby, PHP, C/C++, C#/.NET)
- By environment (Development/Testing, Production/Long-running, Cloud-hosted, Continuous)
- By profiling approach (Sampling, Instrumentation, Hybrid)
- Quick decision matrix
- Selection by overhead tolerance
- Common use case comparisons
- Tool comparison tables
- Quick installation reference
- Common patterns and workflows
- Performance expectations

**Best for:** Quick lookups, decision-making, finding tools for specific use cases

**Key Sections:**
- By Programming Language (detailed tables)
- By Environment (Development, Production, Cloud, Continuous)
- By Profiling Approach (Sampling, Instrumentation, Hybrid)
- Quick Decision Matrix
- Selection by Overhead Tolerance
- Tool Comparison: Common Use Cases
- Quick Installation Reference
- Common Patterns and Workflows
- Performance Expectations

**Quick Start Examples:**
- Python: `py-spy record -o profile.svg -- python myapp.py`
- Node.js: `clinic.js doctor -- node myapp.js`
- Go: `go tool pprof http://localhost:6060/debug/pprof/profile?seconds=30`
- Java: `jcmd <pid> JFR.start duration=60s filename=recording.jfr`
- Rust: `cargo flamegraph`

---

### 3. CPU_PROFILING_TOOLS_CATALOG.csv (15KB)

**Purpose:** Tabular reference for quick lookup and filtering

**Contents:**
- Tool name, type, platform, primary languages, overhead, cost, URL/package
- Key features for each tool
- Best use cases
- Sampling/instrumentation classification
- 50+ tools in CSV format

**Columns:**
1. Tool Name
2. Type (General-Purpose, Language-Specific, Hardware, APM, etc.)
3. Platform(s) (Linux, macOS, Windows, All platforms, etc.)
4. Primary Language(s)
5. Overhead (percentage or multiplier)
6. Cost (Open Source, Free, Commercial)
7. URL/Package
8. Key Features (comma-separated)
9. Best For (use cases)
10. Sampling/Instrumentation (or hybrid)

**Best for:** Spreadsheet analysis, filtering, comparison, finding specific tool attributes

**Quick Filters:**
- Free tools only: Filter Cost column
- Low overhead (<5%): Filter Overhead column
- Multi-language tools: Search for "Multi" in Languages column
- Production-safe tools: Filter for <5% overhead

---

### 4. CPU_PROFILING_SAMPLING_VS_INSTRUMENTATION.md (22KB)

**Purpose:** Comprehensive technical comparison of profiling approaches

**Contents:**
- How sampling works (technical mechanism)
- How instrumentation works (technical mechanism)
- Characteristics comparison
- Advantages and disadvantages
- Detailed comparison matrix
- Hybrid profilers
- Edge cases and special considerations
- Practical decision workflow
- Language-specific recommendations
- Common misconceptions
- Best practice workflow

**Best for:** Understanding profiling methodologies, making architectural decisions, understanding tradeoffs

**Key Topics:**
- Sampling-Based Profiling (how it works, characteristics, advantages, disadvantages, when to use)
- Instrumentation-Based Profiling (how it works, characteristics, advantages, disadvantages, when to use)
- Hybrid Profilers (examples, strategy, workflow)
- Edge Cases (high call frequency, short functions, multi-threaded, async, JIT, I/O)
- Practical Decision Workflow
- Language-Specific Recommendations
- Common Misconceptions
- Best Practice Workflow

**Key Takeaway:** Use sampling in production and for general analysis. Use instrumentation in development for deep dives. Combine both for comprehensive understanding.

---

## Tools by Category

### General-Purpose Profilers (8)
1. perf (Linux kernel profiler)
2. gprofng (modern alternative to gprof)
3. gprof (classic Unix profiler)
4. OProfile (system-wide Linux profiler)
5. Intel VTune Profiler (hardware-level analysis)
6. Valgrind Suite (dynamic instrumentation)
7. Samply (cross-platform sampler)
8. Linux Systemtap and macOS/BSD DTrace

### Python (5)
1. cProfile (instrumentation, built-in)
2. py-spy (sampling, production-safe)
3. line_profiler (per-line instrumentation)
4. memory_profiler (memory profiling)
5. pyflame/pyroscope (sampling, continuous)

### Java (5)
1. async-profiler (low-overhead sampling)
2. Java Flight Recorder (JFR, built-in, continuous)
3. JProfiler (commercial, comprehensive)
4. YourKit (commercial, low-overhead)
5. VisualVM (lightweight, built-in)

### JavaScript / Node.js (5)
1. clinic.js (comprehensive Node.js suite)
2. 0x (simple flame graphs)
3. Node.js Profiler (built-in Chrome DevTools)
4. Autocannon (HTTP benchmarking)
5. Pyroscope (continuous, multi-language)

### Go (1, but comprehensive)
1. pprof (built-in, production-ready)

### Rust (3)
1. cargo-flamegraph (Cargo integration)
2. flamegraph (wrapper around perf/DTrace)
3. perf-map-agent (lower-level)

### Ruby (3)
1. stackprof (sampling, production-safe)
2. ruby-prof (instrumentation, detailed)
3. fb-sampling-profiler (Facebook's lightweight option)

### PHP (3)
1. Xdebug (integrated debugging + profiling)
2. Xhprof / Tideways (hierarchical profiling)
3. Blackfire (commercial SaaS)

### C/C++ (4)
1. gprof (portable)
2. perf (Linux)
3. Valgrind Callgrind (comprehensive)
4. Intel VTune (hardware analysis)

### C#/.NET (3)
1. Visual Studio Profiler (built-in, free Community Edition)
2. dotTrace (commercial, from JetBrains)
3. CLR Profiler (legacy, memory-focused)

### APM Platforms (6)
1. New Relic (cloud APM)
2. Datadog (cloud APM)
3. Google Cloud Profiler (GCP-native)
4. Elastic APM (open source/commercial)
5. Azure Application Insights (Microsoft cloud)
6. Prometheus + Grafana (open source metrics)

### Advanced / Specialized (9)
1. Systemtap (Linux custom instrumentation)
2. DTrace (macOS/BSD custom instrumentation)
3. Intel Pin (binary instrumentation)
4. Magic Trace (instruction-level)
5. LLVM profiling (compiler-integrated)
6. Firefox Profiler (web UI)
7. Heaptrack (memory + CPU)
8. Conprof (Prometheus-compatible)
9. Custom eBPF tools

### Continuous Profilers (3)
1. Parca (eBPF-based, no code changes)
2. Pyroscope (SDK-based, multi-language)
3. Google Cloud Profiler (cloud-native)

---

## Technologies Covered

### Languages
- Python (5 dedicated tools + APM options)
- JavaScript/Node.js (5 dedicated tools)
- Java (5 dedicated tools)
- Go (comprehensive built-in)
- Rust (3 tools)
- Ruby (3 tools)
- PHP (3 tools)
- C/C++ (4 tools)
- C#/.NET (3 tools)
- System-wide (8 general-purpose)

### Platforms
- Linux (15+ tools)
- macOS (12+ tools)
- Windows (10+ tools)
- Cross-platform (25+ tools)
- Cloud (6 APM tools)
- Container/Kubernetes (4 tools)

### Profiling Types
- CPU Profiling (all)
- Memory Profiling (20+ tools)
- Call Graph Analysis (30+ tools)
- Flame Graph Generation (25+ tools)
- Event Loop Analysis (3 tools)
- Lock Contention Analysis (8+ tools)
- Hardware Performance Counters (5+ tools)
- Distributed Tracing (6+ tools)

### Approaches
- Sampling-Based (30+ tools)
- Instrumentation-Based (25+ tools)
- Hybrid (8+ tools)
- eBPF-Based (2 tools)
- DTrace-Based (2 tools)

---

## How to Use These Documents

### Scenario 1: "I need to profile my Python application"

1. Check [CPU_PROFILING_TOOLS_QUICK_REFERENCE.md](CPU_PROFILING_TOOLS_QUICK_REFERENCE.md) → Python section
2. Decide: Development (cProfile) vs Production (py-spy)
3. Go to [CPU_PROFILING_TOOLS_COMPREHENSIVE.md](CPU_PROFILING_TOOLS_COMPREHENSIVE.md) for detailed tool info
4. Run the tool with provided quick start command
5. If unsure about sampling vs instrumentation, see [CPU_PROFILING_SAMPLING_VS_INSTRUMENTATION.md](CPU_PROFILING_SAMPLING_VS_INSTRUMENTATION.md)

### Scenario 2: "I need to choose between multiple tools"

1. Open [CPU_PROFILING_TOOLS_CATALOG.csv](CPU_PROFILING_TOOLS_CATALOG.csv) in a spreadsheet
2. Filter by language, platform, overhead, cost
3. Narrow down to 2-3 candidates
4. Read detailed descriptions in [CPU_PROFILING_TOOLS_COMPREHENSIVE.md](CPU_PROFILING_TOOLS_COMPREHENSIVE.md)
5. Check quick reference for typical overhead and use cases

### Scenario 3: "I don't know where to start"

1. Open [CPU_PROFILING_TOOLS_QUICK_REFERENCE.md](CPU_PROFILING_TOOLS_QUICK_REFERENCE.md)
2. Find your language in "By Programming Language" section
3. Look at recommended tools and their use cases
4. Pick the one marked "recommended"
5. Follow the quick start command

### Scenario 4: "I need to understand sampling vs instrumentation"

1. Read [CPU_PROFILING_SAMPLING_VS_INSTRUMENTATION.md](CPU_PROFILING_SAMPLING_VS_INSTRUMENTATION.md)
2. Check "When to Use" sections for your scenario
3. Review "Practical Decision Workflow"
4. Look at language-specific recommendations
5. Follow "Best Practice Workflow"

### Scenario 5: "I need a quick lookup table"

1. Use [CPU_PROFILING_TOOLS_CATALOG.csv](CPU_PROFILING_TOOLS_CATALOG.csv)
2. Open in Excel/Google Sheets
3. Filter/sort by desired columns
4. Find tool information quickly

---

## Key Statistics

- **Total tools documented:** 65+
- **Languages covered:** 9 (Python, JavaScript, Go, Java, Rust, Ruby, PHP, C/C++, C#/.NET)
- **Platforms covered:** 6+ (Linux, macOS, Windows, cloud, containers)
- **General-purpose profilers:** 8
- **Language-specific profilers:** 30+
- **APM platforms:** 6
- **Advanced/specialized tools:** 9
- **Continuous profilers:** 3
- **Total documentation:** ~95KB (4 files)

## Most Recommended Tools by Language

| Language | Production | Development | Always-On |
|----------|-----------|-------------|-----------|
| Python | py-spy | cProfile | Pyroscope |
| JavaScript | clinic.js | clinic.js | Pyroscope |
| Go | pprof | pprof | Parca |
| Java | JFR/async-profiler | JProfiler | JFR |
| Ruby | stackprof | ruby-prof | Pyroscope |
| PHP | Blackfire | Xdebug | Blackfire |
| C/C++ | perf | gprof/Valgrind | Parca |
| Rust | cargo-flamegraph | perf | Parca |
| .NET | Visual Studio | Visual Studio/dotTrace | dotTrace |

---

## Document Maintenance

**Last Updated:** 2026-01-01
**Version:** 1.0
**Status:** Complete

### Sources

Documentation compiled from:
- Official tool documentation and websites
- GitHub repositories
- Research via Tavily and Perplexity
- Community best practices
- Performance engineering resources

### To Update

1. Check if new tools emerged (search: "profiling tools 2026")
2. Check if tools were renamed or discontinued
3. Verify installation and usage examples still work
4. Update performance benchmarks if available
5. Add new tools to all relevant sections

---

## Quick Tool Selection by Use Case

### "My app is slow in production"
→ py-spy (Python), clinic.js (Node.js), async-profiler (Java), pprof (Go)

### "I want to understand the code flow"
→ cProfile (Python), JProfiler (Java), ruby-prof (Ruby), Xhprof (PHP)

### "I need to optimize memory"
→ memory_profiler (Python), JProfiler (Java), Valgrind (C/C++)

### "I want continuous monitoring"
→ Pyroscope (multi-language), Parca (compiled), Google Cloud Profiler (cloud)

### "I'm profiling for the first time"
→ Your language's built-in tool (pprof for Go, JFR for Java, cProfile for Python)

### "I need production profiling without overhead"
→ Sampling-based tools (<5%): py-spy, async-profiler, stackprof, pprof, JFR

### "I need the most detail possible"
→ Instrumentation-based tools: cProfile, JProfiler, ruby-prof, Xhprof, Valgrind

---

## Related Documentation

These documents complement the CPU profiling tools documentation:

- Performance testing and benchmarking tools
- Distributed tracing systems (Jaeger, Tempo, OpenTelemetry)
- Application performance monitoring (APM)
- Infrastructure monitoring (Prometheus, Grafana)
- Log aggregation and analysis (ELK, Loki)

---

**Quick Start Commands:**

```bash
# Python
py-spy record -o profile.svg -- python myapp.py

# Node.js
clinic.js doctor -- node myapp.js

# Go
go tool pprof http://localhost:6060/debug/pprof/profile?seconds=30

# Java
jcmd <pid> JFR.start duration=60s

# Ruby
stackprof tmp/stackprof.dump --flamegraph | flamegraph.pl

# Rust
cargo flamegraph

# C/C++ (Linux)
perf record -g ./myapp && perf report
```

---

**For more information, see the individual documentation files above.**
