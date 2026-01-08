# Specialized Profiling Tools - Quick Reference

Fast lookup guide for choosing the right profiling tool based on your needs.

## By Problem Type

### "My queries are slow"
- **SQL databases**: dbForge Studio, SQL Server Profiler, DBeaver, pgAdmin, MySQL Workbench
- **Quick start**: DBeaver (free, multi-database)
- **Enterprise**: Redgate SQL Monitor, SolarWinds SQL Sentry

### "My web app is slow"
- **Frontend**: Lighthouse, WebPageTest, Chrome DevTools
- **Backend Python**: py-spy, Scalene
- **Backend Go**: pprof
- **Backend Java**: JProfiler, YourKit

### "My GPU training is slow"
- **NVIDIA**: Nsight Systems (system-wide), Nsight Compute (per-kernel)
- **AMD**: ROCm Omniperf, AMD uProf
- **Intel**: VTune Profiler
- **Multi-vendor**: HPCToolkit, Omnitrace

### "My network is congested"
- **Deep inspection**: Wireshark, tcpdump
- **Flow analysis**: ManageEngine NetFlow, SolarWinds NPM
- **Easy start**: Wireshark (GUI), tcpdump (CLI)

### "My microservices have latency issues"
- **Open-source**: Jaeger, Zipkin, OpenTelemetry
- **Commercial**: DataDog APM, New Relic, Dynatrace
- **Quick start**: Jaeger (easy deployment)

### "I need continuous production profiling"
- **Low overhead**: py-spy, Linux perf, rbspy
- **Distributed**: Parca, Pixie
- **Visualization**: FlameGraph, Speedscope

## By Language

| Language | Recommended Tools | Free Options |
|----------|-------------------|--------------|
| Python | py-spy, Scalene, cProfile | py-spy, Scalene (both free) |
| Go | pprof, Linux perf | pprof (free) |
| Java | JProfiler, YourKit, Java Flight Recorder | Java Flight Recorder (free, built-in) |
| JavaScript/Node | Chrome DevTools, Lighthouse, clinic.js | Chrome DevTools, Lighthouse (free) |
| SQL | DBeaver, SQL Server Profiler | DBeaver (free) |
| Ruby | rbspy, Linux perf | rbspy (free) |
| Rust | Linux perf, Flamegraph | Both free |
| C/C++ | Linux perf, VTune, Valgrind | Linux perf, Valgrind (free) |

## By Deployment Type

### Local Development
- Python: py-spy, Scalene
- Backend: pprof, cProfile, JProfiler
- Frontend: Chrome DevTools, Lighthouse
- Database: DBeaver

### Staging/Testing
- All development tools (with less overhead)
- Add: Full tracing (Jaeger, Zipkin)
- Add: Network analysis (Wireshark, NetFlow)

### Production
- Minimal overhead: py-spy, pprof, Linux perf
- Distributed systems: Jaeger, OpenTelemetry + DataDog/New Relic
- Continuous: Parca, Pixie
- Avoid: Nsight Systems, full packet capture

## By Budget

### Completely Free (Open-source)
- py-spy, Linux perf, pprof, rbspy
- Jaeger, Zipkin, OpenTelemetry, Grafana
- Wireshark, tcpdump, Prometheus
- FlameGraph, Speedscope, Parca, Pixie
- DBeaver, pgAdmin, Chrome DevTools
- Lightweight: HPCToolkit, Omnitrace

### Freemium (Free tier available)
- DataDog APM (limited)
- New Relic (limited)
- Elastic APM (open-source + cloud)
- Most SaaS APM tools

### Commercial (Paid required)
- JProfiler, YourKit, Dynatrace
- SolarWinds (NetFlow, SQL Sentry)
- Redgate SQL Monitor
- Some: Oracle, IBM enterprise tools

## By Overhead Level

### Negligible (<1%) - Safe for Production
- py-spy
- Linux perf
- rbspy
- tcpdump (read-only)
- Parca
- Prometheus (metrics only)

### Low (1-5%) - Usually Safe for Production
- Lighthouse
- WebPageTest
- pprof
- cProfile (short runs)
- Jaeger (with sampling)
- Speedscope
- Pixie

### Moderate (5-20%) - Development/Staging
- DBeaver
- SQL Server Profiler
- DataDog APM
- JProfiler
- New Relic
- Dynatrace

### High (>20%) - Development Only
- NVIDIA Nsight Systems/Compute
- AMD uProf/Omniperf
- Intel VTune
- Full packet capture
- Wireshark (live capture)

## Quick Decision Tree

```
START: What's the problem?

├─ Database slow
│  └─ What database? → DBeaver (general), dbForge (SQL Server), pgAdmin (PostgreSQL)
│
├─ Web app slow
│  ├─ Frontend? → Lighthouse
│  └─ Backend?
│     ├─ Python? → py-spy (low overhead) or Scalene (detailed)
│     ├─ Go? → pprof
│     └─ Java? → JProfiler or JFR
│
├─ GPU slow
│  ├─ NVIDIA? → Nsight Compute (kernels) or Nsight Systems (system)
│  ├─ AMD? → ROCm Omniperf
│  └─ Intel? → VTune
│
├─ Network slow
│  ├─ Need detail? → Wireshark
│  ├─ Need throughput? → iperf
│  └─ Need flows? → ManageEngine NetFlow or SolarWinds
│
├─ Microservices slow
│  ├─ Self-hosted? → Jaeger or Zipkin
│  └─ Managed? → DataDog APM or New Relic
│
└─ Need continuous monitoring
   ├─ Single service? → py-spy
   ├─ Distributed? → Parca or Pixie
   └─ Full observability? → DataDog or New Relic
```

## Integration Combos

### Minimal Stack (Free)
```
Database: DBeaver
Frontend: Lighthouse
Backend: py-spy (Python)
Network: Wireshark
Distributed: Jaeger
Visualization: Grafana + Prometheus
```

### Full Stack (Mixed)
```
Database: Redgate SQL Monitor
Frontend: WebPageTest
Backend: DataDog APM
Network: SolarWinds NPM
Logs: Grafana Loki
Visualization: DataDog dashboard
```

### Startup Stack (Low Cost)
```
Database: DBeaver (free)
Frontend: Chrome DevTools + Lighthouse
Backend: py-spy (free) + New Relic (free tier)
Distributed: Jaeger (free, self-hosted)
Visualization: Grafana (free)
```

## Setup Time Comparison

| Tool | Setup Time | Difficulty |
|------|-----------|------------|
| Chrome DevTools | 0 min | Trivial |
| Lighthouse | 2 min | Trivial |
| DBeaver | 5 min | Easy |
| Wireshark | 5 min | Easy |
| py-spy | 5 min | Easy |
| Jaeger | 15 min | Medium |
| Linux perf | 10 min | Medium |
| DataDog APM | 20 min | Medium |
| New Relic | 20 min | Medium |
| Dynatrace | 30 min | Hard |
| NVIDIA Nsight | 20 min | Hard |
| JProfiler | 15 min | Medium |

## Common Mistakes to Avoid

1. **Using production profilers in dev**: Nsight Systems, full Wireshark captures waste time
2. **Wrong tool for scope**: Using Wireshark for application-level issues (use APM instead)
3. **No sampling strategy**: Jaeger without sampling kills production performance
4. **Forgetting overhead**: Not checking tool overhead = surprised by production behavior
5. **Single-tool mindset**: Database slow ≠ always a query issue (network might be problem)
6. **Not correlating data**: Ignoring logs while tracing (lose context)
7. **Tool sprawl**: Too many tools = harder root-cause analysis (consolidate)

## Recommended Paths by Company Size

### Solo Developer
- py-spy (Python), Chrome DevTools (Frontend)
- DBeaver (Database), Wireshark (Network)
- Lightweight, learn as you go

### Small Team (2-10)
- Add: Jaeger (self-hosted), Prometheus + Grafana
- Add: pprof (Go), JFR (Java if applicable)
- Add: WebPageTest (for CI/CD)

### Medium Team (10-50)
- Add: DataDog APM free tier or Elastic APM
- Add: Managed Jaeger or Zipkin
- Add: SolarWinds or ManageEngine for network
- Add: SQL monitoring (Redgate, SolarWinds)

### Enterprise (50+)
- DataDog or New Relic (full platform)
- Dynatrace (AI-powered)
- SolarWinds NPM + SQL Sentry
- Internal observability platform
- Dedicated profiling/APM team

---

**Tip**: Start with free tools. Upgrade only when specific pain points justify cost.

**Last Updated**: 2025-01-01
