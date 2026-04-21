<!-- Source: https://namespace.so/docs/architecture/compute/observability -->

# Observability

Gain comprehensive insights into your compute instance performance with detailed metrics, logs, and resource monitoring.

## Performance Metrics

The dedicated job view allows correlating job steps with performance metrics and comparing a job's performance to previous runs.
This visibility helps you identify performance bottlenecks and track improvements over time.

![Instance metrics](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Finstancemetrics.d5f0cbfb.png&w=1200&q=75)

- **CPU Usage**: Track processor utilization across all cores, identify CPU-intensive operations
- **Memory Consumption**: Detect memory leaks and excessive allocation
- **Disk I/O**: Understand disk read/write patterns, identify storage bottlenecks
- **Network Activity**: Track network usage, bandwidth consumption, and connection patterns

## Advanced Logging Capabilities

Access comprehensive logging, providing visibility into every aspect of your workflow execution.
Namespace log collection and serving goes beyond stdout/stderr and provides meaningful insights.

**Container Logs**
Namespace provides direct access to logs from running containers within your workflows.

![Container Logs](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ftestcontainerlogs.f785750e.png&w=1200&q=75)

**Build logs**
Any Docker build issued from a Namespace runner is linked from the instance UI, granting you direct access to the build logs and build performance telemetry.

![Container Builds](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcontainer-builds.7d9275bb.png&w=640&q=75)![Build Tracing](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbuildtrace.c35385df.png&w=828&q=75)

## Out of Memory (OOM) Detection

Memory consumption graphs can already give insights on memory leaks and excessive allocation patterns.
However, when only working with memory allocation metrics it is hard to isolate if a task was running close to a memory limit, or encountered an error when running out of memory.
Namespace's automatic OOM detection makes these conditions explicit and simple to detect.

## Crash Dump Collection

Namespace can automatically detect if your task execution crashes, collect crash dumps, and store them as [artifacts](/docs/architecture/storage/artifact-storage).
These dumps contain invaluable forensic information useful for determining the cause of the crash.
Crash dump collection is not enabled by default - reach out to [support@namespace.so](mailto:support@namespace.so) to get access.

## Hands-on Support

Got stuck? Need help with debugging one of your workflows? Our team is here to assist:

- **Technical Support**: Reach out to [support@namespace.so](mailto:support@namespace.so) to talk to one of our engineers.
- **Community**: Join our community [Discord](https://discord.gg/DqMzDFR6Hc) to learn about tips and best practices.

## API Reference

Metrics and logs can be queried programmatically via the Namespace API.

### Instance Metrics

The [ComputeService](https://buf.build/namespace/cloud/docs/main:namespace.cloud.compute.v1beta) `GetInstanceMetrics`
RPC returns time-series resource usage data for a specified instance. You can query metrics from both
running and terminated instances, and optionally filter by time range.

Available metric resources:

| Resource | Metrics |
|---|---|
| `CPU` | `cpu_max` (peak CPU utilization, 0-100%), `cpu_avg` (average across all CPUs) |
| `CPU_BREAKDOWN` | Per-CPU utilization: `cpu_0`, `cpu_1`, ... `cpu_n` (0-100%) |
| `IO_WAIT` | `io_wait_max`, `io_wait_avg` (percentage of time CPUs spent waiting on I/O) |
| `MEMORY` | `mem_available`, `mem_used` (in bytes) |
| `STORAGE` | `storage_used_percent_/` (root disk), plus per-cache-volume mountpoints (0-100%) |

### Logs

The [ObservabilityService](https://buf.build/namespace/cloud/docs/main:namespace.cloud.compute.v1beta)
provides two RPCs for accessing instance logs:

- **`StreamInstanceLogs`**: Stream logs in real-time from a running instance. Set `follow: true`
  to wait for additional log output. The stream terminates when the instance shuts down.
- **`FetchInstanceLogs`**: Query historical logs with pagination and time range filtering.
  Supports matching by instance ID pattern for querying logs across multiple instances.

Log entries include the source (e.g. `containers`, `kubernetes`, `kmsg`), stream (`stdout`, `stderr`),
timestamp, and associated labels.

Last updated March 20, 2026
