# Profiling Visualization Tools - Quick Reference Guide

## One-Minute Decisions

### Need Real-Time CPU Profiling?
- **Production Environment**: Parca (eBPF, no code changes)
- **Development**: Pyroscope (easy setup) or language-specific pprof
- **Web Apps**: Chrome DevTools or Firefox Profiler

### Need Flame Graphs?
- **Generate from Stacks**: flamegraph.pl (original, lightweight)
- **Visualize Existing Profiles**: speedscope (fast, web-based)
- **GPU Support**: AI Flame Graphs
- **Grafana Integration**: Grafana Pyroscope

### Need Language-Specific Profiling?
| Language | Recommended Profiler | Visualization |
|----------|---------------------|----------------|
| Go | pprof | go tool pprof, speedscope, flame graphs |
| Python | py-spy (production) or cProfile (dev) | snakeviz, speedscope |
| Node.js | clinic.js or Node Inspector | clinic.js UI or flame graphs |
| Java | Java Flight Recorder | Java Mission Control or flame graphs |
| Ruby | stackprof (CPU) or memory_profiler | Flame graphs or custom dashboards |
| C/C++ | perf or bpftrace | flamegraph.pl or speedscope |

### Need Infrastructure-Wide Profiling?
- **Linux Kernel + Apps**: bpftrace or perf + flamegraph.pl
- **Kubernetes**: Parca Agent (eBPF-based)
- **Managed Cloud**: Datadog or New Relic

### Need Distributed Tracing + Profiling?
- **Open-Source**: Grafana Tempo (OpenTelemetry) + Pyroscope
- **Managed**: Datadog or New Relic
- **Simple Integration**: Add Parca Agent + correlate with trace spans

---

## Tool Categories and Trade-offs

### Flame Graph Generators
```
Simple & Fast          Interactive & Rich
    |                         |
flamegraph.pl ──────────────────────── speedscope
    |                         |
stackcollapse         web UI + zoom
minimal overhead      handles large data
```

### Continuous Profilers
```
Infrastructure-Wide    Application-Level
    |                         |
Parca ──────────────────────── Pyroscope
eBPF agents            Language SDKs
no instrumentation     flexible collection
production-focused     dev/test/prod
```

### Language Profilers
```
Low Overhead          Feature-Rich         GUI/Web
    |                     |                  |
bpftrace ──── pprof ──── cProfile ──── Mission Control
<1% overhead  1-2%       5-15%          JVM-specific
kernel focus runtime    deterministic   thread analysis
```

---

## Quick Setup Examples

### Setup Pyroscope (5 minutes)
```bash
# Run server
docker run -it -p 4040:4040 pyroscope/pyroscope:latest server

# Go app (add 3 lines)
import "github.com/grafana/pyroscope-go"
pyroscope.Start(...)

# Visit http://localhost:4040
```

### Setup Parca (10 minutes - Kubernetes)
```bash
# Install Parca + Agent
helm install parca parca/parca
helm install parca-agent parca/parca-agent

# Visit Parca UI for system-wide profiling
```

### Generate Flame Graph from perf (3 commands)
```bash
perf record -a -g -- <workload>
perf script | stackcollapse-perf.pl > out.folded
./flamegraph.pl out.folded > flame.svg
```

### Profile Go Application (1 line)
```bash
# Built-in pprof endpoint
curl http://localhost:6060/debug/pprof/profile?seconds=30 > profile.out
go tool pprof profile.out
```

---

## Decision Tree: Which Profiler to Use

```
Do you need continuous monitoring?
├─ YES → Production environment?
│  ├─ YES → Parca (no instrumentation needed)
│  │   or Pyroscope (needs SDK)
│  └─ NO  → Pyroscope (easier setup)
│
└─ NO → One-time analysis?
   ├─ YES → What language?
   │  ├─ Go       → pprof + speedscope
   │  ├─ Python   → py-spy + flamegraphs
   │  ├─ Java     → Java Flight Recorder
   │  ├─ Node.js  → clinic.js
   │  ├─ Ruby     → stackprof
   │  ├─ System   → perf + flamegraph.pl
   │  └─ Browser  → Chrome/Firefox DevTools
   │
   └─ NO → Full observability stack?
      ├─ YES → Datadog / New Relic
      │   or OpenTelemetry + Grafana Tempo + Pyroscope
      └─ NO  → Just flame graphs?
         ├─ YES → flamegraph.pl or speedscope
         └─ NO  → Start with language profiler
```

---

## Feature Comparison Quick Matrix

### Continuous Profiling Platforms

| Feature | Pyroscope | Parca | Datadog | New Relic |
|---------|-----------|-------|---------|-----------|
| Open Source | Yes | Yes | No | No |
| No Code Changes | No | Yes (eBPF) | No | No |
| CPU Profiling | Yes | Yes | Yes | Yes |
| Memory Profiling | Yes | Yes | Yes | Yes |
| Profile Comparison | Yes | Yes | Yes | Yes |
| Flame Graphs | Yes | Yes | Yes | Yes |
| OpenTelemetry | Yes | Yes | Yes | Yes |
| Infrastructure Labels | Yes | Yes | Yes | Yes |
| Overhead | 2-5% | 2-3% | Managed | Managed |
| Setup Complexity | Low | Medium | Low | Low |
| Grafana Integration | Native | Native | Via plugins | Via plugins |

### Language Profilers

| Feature | pprof | cProfile | py-spy | JFR | stackprof |
|---------|-------|----------|--------|-----|-----------|
| Language | Go | Python | Python | Java | Ruby |
| Sampling | Yes (timer/PMU) | No (instrumented) | Yes | Yes (events) | Yes |
| No Code Changes | Varies | No | Yes | No | No |
| Overhead | 1-2% | 5-15% | 2-5% | 1-3% | 1-3% |
| Built-in | Yes | Yes | No | Yes | No (gem) |
| Web UI | Yes | No | No | Yes (JMC) | No |
| Flame Graphs | Via tools | Via tools | Native | Via tools | Via tools |

---

## Common Use Cases and Solutions

### Case 1: "My Go service is slow in production"
1. Start pprof: `import _ "net/http/pprof"` in main()
2. Capture profile: `curl http://service:6060/debug/pprof/profile?seconds=30 > profile.out`
3. Analyze: `go tool pprof profile.out`
4. For continuous monitoring: Deploy Pyroscope or Parca Agent

### Case 2: "Python script is hanging, don't want to modify code"
1. Use py-spy: `py-spy record -o profile.svg -- python script.py`
2. Analyze SVG with speedscope
3. For repeated issues: Deploy Pyroscope with py-spy integration

### Case 3: "Need to profile entire Kubernetes cluster"
1. Deploy Parca Agent as DaemonSet
2. Automatic eBPF profiling of all containers
3. Query in Parca UI with Kubernetes labels
4. Correlate with traces if using OpenTelemetry

### Case 4: "Browser app is slow, need to find bottleneck"
1. Chrome DevTools: Performance tab → Record → Interact → Analyze
2. Look for long JavaScript tasks (yellow), rendering (purple)
3. Use Timeline and Flame Chart to drill into specific functions

### Case 5: "Java microservices need profiling"
1. Enable JFR: `-XX:StartFlightRecording=...`
2. Dump recordings periodically or on-demand
3. Analyze with Java Mission Control (JMC)
4. For continuous: Use Datadog or New Relic

---

## Overhead and Sampling Rates

### Minimal Overhead (<1%)
- bpftrace (eBPF, kernel-space)
- perf (kernel-space)
- eBPF-based profilers

### Low Overhead (1-3%)
- pprof (Go runtime, sampling)
- py-spy (Python, sampling)
- stackprof (Ruby, sampling)
- Java Flight Recorder (event-based)
- Parca Agent (eBPF)

### Moderate Overhead (2-5%)
- Pyroscope (sampling-based)
- Ruby memory_profiler (allocations)

### Higher Overhead (5-15%)
- cProfile (Python, instrumented)
- ruby-prof with instrumentation
- Heavy instrumentation profilers

### Managed/Transparent
- Datadog (optimized overhead)
- New Relic (optimized overhead)

---

## Integration Points

### With Distributed Tracing
- **Tempo + Pyroscope**: Click trace span → jump to flame graph
- **Jaeger + Parca**: Correlate spans with infrastructure profiling
- **OpenTelemetry**: Universal protocol for profiling + tracing + metrics

### With Observability Stacks
- **Grafana**: Pyroscope + Prometheus + Loki + Tempo
- **Datadog**: Native integration (APM + Profiling + Logs)
- **New Relic**: Native integration (all observability)
- **SigNoz**: OpenTelemetry-based (open-source)

### With CI/CD
- **Continuous Profiling**: Catch regressions post-deployment
- **Benchmark Comparisons**: Profile diff between versions
- **Automated Analysis**: LLM-assisted interpretation (Grafana)

---

## Tools You Probably Don't Need (Unless...)

| Tool | Skip Unless |
|------|------------|
| flamegraph.pl | You're debugging legacy systems or need fine-grained control |
| bpftrace | You need kernel-space insights or system-wide visibility |
| cProfile | You're debugging Python in development (use py-spy for production) |
| Xcode Instruments | You're developing iOS/macOS apps |
| Java Mission Control | You're using Java Flight Recorder extensively |
| Chrome DevTools | You're not developing web applications |

---

## Resources and Links

### Official Documentation
- **Pyroscope**: https://pyroscope.io/docs/
- **Parca**: https://www.parca.dev/docs/
- **Grafana Pyroscope**: https://grafana.com/docs/pyroscope/
- **Go pprof**: https://pkg.go.dev/runtime/pprof
- **flamegraph.pl**: https://github.com/brendangregg/FlameGraph

### Learning Resources
- **Brendan Gregg's Perf Analysis**: https://www.brendangregg.com/linuxperf.html
- **Go Profiling Best Practices**: https://dave.cheney.net/
- **Python Profiling Guide**: https://docs.python.org/3/library/profile.html
- **OpenTelemetry Overview**: https://opentelemetry.io/docs/what-is-opentelemetry/

### Benchmarking & Comparison
- APM Digest (Datadog/New Relic comparisons)
- CNCF Landscape (Observability category)
- Cloud Chipr (cloud observability tools)

---

## Last Updated
January 2026 | Based on 2025-2026 research | 40+ tools covered
