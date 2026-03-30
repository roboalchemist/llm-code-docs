# Source: https://uptrace.dev/raw/opentelemetry/collector/host-metrics.md

# OpenTelemetry Host Metrics receiver

> Complete hostmetricsreceiver documentation with configuration examples for all scrapers (CPU, memory, disk, filesystem, network, processes). Includes Docker/Kubernetes deployment, troubleshooting guide, and production-ready templates.

The **hostmetricsreceiver** is an OpenTelemetry Collector [plugin](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/hostmetricsreceiver) that collects comprehensive system-level metrics from host machines. Updated for OpenTelemetry Collector v0.140.1+, it provides critical insights into system performance, resource utilization, and potential bottlenecks that could impact your applications.

## Overview

By collecting and analyzing host metrics, you can:

- **Monitor system health** in real-time across your infrastructure
- **Identify performance bottlenecks** before they impact users
- **Track resource utilization trends** for capacity planning
- **Set up alerts** for anomalous behavior or resource exhaustion
- **Correlate system metrics** with application performance issues

## Available Scrapers

The hostmetricsreceiver includes multiple scrapers for different system components:

<table>
<thead>
  <tr>
    <th>
      Scraper
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Key Metrics
    </th>
    
    <th>
      Platform Support
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <strong>
        cpu
      </strong>
    </td>
    
    <td>
      CPU utilization and time
    </td>
    
    <td>
      <code>
        system.cpu.time
      </code>
      
      , <code>
        system.cpu.utilization
      </code>
    </td>
    
    <td>
      All
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        memory
      </strong>
    </td>
    
    <td>
      RAM usage and availability
    </td>
    
    <td>
      <code>
        system.memory.usage
      </code>
      
      , <code>
        system.memory.utilization
      </code>
    </td>
    
    <td>
      All
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        disk
      </strong>
    </td>
    
    <td>
      Disk I/O operations
    </td>
    
    <td>
      <code>
        system.disk.io
      </code>
      
      , <code>
        system.disk.operations
      </code>
    </td>
    
    <td>
      All
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        filesystem
      </strong>
    </td>
    
    <td>
      Filesystem usage (including NFS)
    </td>
    
    <td>
      <code>
        system.filesystem.usage
      </code>
      
      , <code>
        system.filesystem.utilization
      </code>
    </td>
    
    <td>
      All
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        network
      </strong>
    </td>
    
    <td>
      Network I/O and connections
    </td>
    
    <td>
      <code>
        system.network.io
      </code>
      
      , <code>
        system.network.connections
      </code>
    </td>
    
    <td>
      All
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        load
      </strong>
    </td>
    
    <td>
      System load averages
    </td>
    
    <td>
      <code>
        system.cpu.load_average.1m/5m/15m
      </code>
    </td>
    
    <td>
      Linux/Unix
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        paging
      </strong>
    </td>
    
    <td>
      Swap/paging activity
    </td>
    
    <td>
      <code>
        system.paging.usage
      </code>
      
      , <code>
        system.paging.operations
      </code>
    </td>
    
    <td>
      All
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        process
      </strong>
    </td>
    
    <td>
      Aggregate process counts
    </td>
    
    <td>
      <code>
        system.processes.running
      </code>
      
      , <code>
        system.processes.blocked
      </code>
    </td>
    
    <td>
      All
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        processes
      </strong>
    </td>
    
    <td>
      Per-process metrics
    </td>
    
    <td>
      <code>
        process.cpu.time
      </code>
      
      , <code>
        process.memory.usage
      </code>
    </td>
    
    <td>
      All (requires elevated permissions)
    </td>
  </tr>
</tbody>
</table>

## Prerequisites

Before you begin, ensure you have:

- OpenTelemetry Collector installed ([installation guide](/opentelemetry/collector#installation))
- Appropriate permissions to collect system metrics
- Access to modify the Collector configuration
- A telemetry backend configured (e.g., Uptrace, Prometheus, Jaeger)

## What is OpenTelemetry Collector?

OpenTelemetry Collector is a vendor-agnostic agent that:

- **Collects** telemetry data from various sources using receivers
- **Processes** data through a pipeline (filtering, aggregating, transforming)
- **Exports** data to one or multiple observability backends

The Collector provides a unified way to receive, process, and export telemetry data (traces, metrics, and logs), eliminating the need for multiple agents.

### Key Benefits

- **Simplified deployment** - Single agent for all telemetry data
- **Vendor neutrality** - Switch backends without changing instrumentation
- **Powerful processing** - Transform and enrich data before export
- **Reduced overhead** - Efficient batching and compression

## Quick Start Guide

### Basic Configuration

To start collecting host metrics immediately, add this minimal configuration to your `otel-collector-config.yaml`:

```yaml
receivers:
  hostmetrics:
    collection_interval: 10s
    scrapers:
      cpu:
      memory:
      disk:
      filesystem:
      network:
      load:

processors:
  batch:
    timeout: 10s

exporters:
  # Configure your exporter here
  otlp:
    endpoint: "your-backend:4317"

service:
  pipelines:
    metrics:
      receivers: [hostmetrics]
      processors: [batch]
      exporters: [otlp]
```

### Starting the Collector

```bash
# Run with your configuration
otelcol-contrib --config=otel-collector-config.yaml

# Or as a service (systemd)
sudo systemctl start otelcol-contrib
```

## Complete Configuration Example

Here's a comprehensive configuration that includes all available scrapers and recommended processors:

```yaml
processors:
  # Detect and add resource attributes
  resourcedetection:
    detectors: [env, system, docker, ec2, gcp, azure]
    timeout: 5s
    override: false

  # Convert cumulative metrics to delta
  cumulativetodelta:

  # Batch data for efficient export
  batch:
    timeout: 10s
    send_batch_size: 1024

receivers:
  hostmetrics:
    # How often to collect metrics
    collection_interval: 10s

    # Configure individual scrapers
    scrapers:
      # CPU utilization metrics
      cpu:
        metrics:
          system.cpu.utilization:
            enabled: true

      # Disk I/O metrics
      disk:
        # Exclude specific mount points
        exclude:
          devices: ["^/dev/loop.*"]

      # File System utilization metrics
      filesystem:
        exclude:
          mount_points: ["/tmp/*", "/dev/shm"]
        include_fs_types:
          match_type: strict
          fs_types: [ext3, ext4, xfs, btrfs]

      # CPU load average metrics (1, 5, 15 minutes)
      load:

      # Memory utilization metrics
      memory:

      # Network interface I/O metrics & TCP connection metrics
      network:
        include:
          interfaces: ["eth0", "eth1"]

      # Paging/Swap space utilization and I/O metrics
      paging:

      # Process count by status
      process:

      # Per-process metrics (requires elevated permissions)
      processes:
        include:
          names: ["nginx", "postgres", "redis"]
        mute_process_name_error: true

service:
  pipelines:
    metrics:
      receivers: [hostmetrics]
      processors: [resourcedetection, cumulativetodelta, batch]
      exporters: [otlp]
```

## Production-Ready Configuration Template

This is a complete, copy-paste ready configuration optimized for production environments:

```yaml
# Complete production-ready configuration for hostmetricsreceiver
# Tested with OpenTelemetry Collector v0.140.1+

receivers:
  hostmetrics:
    # Collect metrics every 30 seconds (balance between granularity and overhead)
    collection_interval: 30s

    # Root path for containerized deployments
    # root_path: /hostfs

    scrapers:
      # CPU metrics - enabled by default
      cpu:
        metrics:
          system.cpu.utilization:
            enabled: true
          system.cpu.logical.count:
            enabled: true

      # Memory metrics
      memory:
        metrics:
          system.memory.utilization:
            enabled: true

      # Disk I/O metrics - exclude virtual/loop devices
      disk:
        exclude:
          devices: ["^/dev/loop.*", "^/dev/dm-.*"]
          match_type: regexp

      # Filesystem metrics - production filesystems only
      filesystem:
        include_fs_types:
          match_type: strict
          fs_types: [ext3, ext4, xfs, btrfs, zfs, nfs, nfs4]
        exclude:
          mount_points: ["/boot", "/tmp/*", "/dev/*", "/run/*", "/sys/*"]
          match_type: regexp
        include_virtual_filesystems: false

      # Network metrics - filter primary interfaces
      network:
        include:
          interfaces: ["eth.*", "en.*", "ens.*"]
          match_type: regexp
        exclude:
          interfaces: ["lo", "docker.*", "veth.*"]
          match_type: regexp

      # Load average (Linux/Unix only)
      load:

      # Paging/Swap metrics
      paging:

      # Process count metrics
      process:
        metrics:
          system.processes.created:
            enabled: true

      # Per-process metrics (optional - requires elevated permissions)
      # processes:
      #   include:
      #     names: ["nginx", "mysql", "postgres", "redis"]
      #     match_type: regexp
      #   mute_process_name_error: true
      #   max_processes: 100

processors:
  # Detect cloud/container environment
  resourcedetection:
    detectors: [env, system, docker, ec2, gcp, azure, aks, eks, gke]
    timeout: 5s
    override: false
    system:
      hostname_sources: [dns, os]

  # Convert cumulative to delta for backends that expect delta
  cumulativetodelta:
    metrics:
      - system.network.io
      - system.disk.io

  # Batch for efficient export
  batch:
    timeout: 10s
    send_batch_size: 1024
    send_batch_max_size: 2048

  # Filter out noisy metrics (optional)
  # filter/metrics:
  #   metrics:
  #     exclude:
  #       match_type: regexp
  #       metric_names:
  #         - "system\\.disk\\.merged"

exporters:
  # Configure your backend
  otlp:
    endpoint: "your-backend:4317"
    compression: gzip
    # headers:
    #   api-key: "${API_KEY}"

  # Debug exporter for troubleshooting
  # debug:
  #   verbosity: detailed

service:
  # Enable telemetry for the collector itself
  telemetry:
    logs:
      level: info
    metrics:
      level: detailed
      address: ":8888"

  pipelines:
    metrics:
      receivers: [hostmetrics]
      processors: [resourcedetection, cumulativetodelta, batch]
      exporters: [otlp]
```

**Usage instructions:**

1. Save as `otel-collector-config.yaml`
2. Update `exporters.otlp.endpoint` with your backend URL
3. Uncomment `root_path` if running in Docker/Kubernetes
4. Adjust `collection_interval` based on your needs (10s for high frequency, 60s for lower overhead)
5. Enable `processes` scraper if you need per-process metrics (requires root/elevated permissions)

## Available Scrapers

The hostmetricsreceiver includes multiple scrapers, each collecting specific metric types:

### CPU Scraper

Collects CPU utilization metrics per core and aggregated.

**Metrics collected:**

- `system.cpu.time` - CPU time in different states (user, system, idle, etc.)
- `system.cpu.utilization` - CPU utilization percentage

**Example configuration:**

```yaml
cpu:
  metrics:
    system.cpu.utilization:
      enabled: true
    system.cpu.logical.count:
      enabled: true
```

### Memory Scraper

Monitors RAM usage and availability.

**Metrics collected:**

- `system.memory.usage` - Memory usage by state
- `system.memory.utilization` - Memory utilization percentage

**Example configuration:**

```yaml
memory:
  metrics:
    system.memory.utilization:
      enabled: true
```

### Disk Scraper

Tracks disk I/O operations and performance.

**Metrics collected:**

- `system.disk.io` - Bytes read/written
- `system.disk.operations` - Read/write operations count
- `system.disk.io_time` - Time spent on I/O operations
- `system.disk.merged` - Merged read/write operations

**Example configuration:**

```yaml
disk:
  # Collect metrics for specific devices only
  include:
    devices: ["sda", "sdb"]
  exclude:
    devices: ["^/dev/loop.*"]
```

### Filesystem Scraper

Monitors filesystem usage and capacity, including network filesystems like NFS.

**Metrics collected:**

- `system.filesystem.usage` - Used/free space
- `system.filesystem.utilization` - Usage percentage
- `system.filesystem.inodes.usage` - Inode usage

**Example configuration:**

```yaml
filesystem:
  include_fs_types:
    match_type: regexp
    fs_types: ["^ext[234]$", "^xfs$"]
  exclude:
    mount_points: ["/boot", "/dev/*"]
  include_virtual_filesystems: false
```

**Collecting NFS metrics:**

To monitor NFS mounts specifically, configure the filesystem scraper to include NFS filesystem types:

```yaml
filesystem:
  # Include NFS v3 and v4 mounts
  include_fs_types:
    match_type: strict
    fs_types: [nfs, nfs4]

  # Optionally filter specific mount points
  include:
    mount_points: ["/mnt/nfs/*"]

  # Collect metrics for network filesystems
  include_virtual_filesystems: true
```

This configuration collects standard filesystem metrics (`usage`, `utilization`, `inodes`) for all NFS mounts on the system.

### Network Scraper

Collects network interface and connection statistics.

**Metrics collected:**

- `system.network.io` - Bytes sent/received
- `system.network.packets` - Packets sent/received
- `system.network.errors` - Network errors
- `system.network.connections` - TCP connection states

**Example configuration:**

```yaml
network:
  include:
    interfaces: ["eth.*", "en.*"]
  exclude:
    interfaces: ["lo", "docker.*"]
```

### Load Scraper

Reports system load averages (Linux/Unix only).

**Metrics collected:**

- `system.cpu.load_average.1m` - 1-minute load average
- `system.cpu.load_average.5m` - 5-minute load average
- `system.cpu.load_average.15m` - 15-minute load average

### Paging Scraper

Monitors swap/paging activity.

**Metrics collected:**

- `system.paging.usage` - Swap space usage
- `system.paging.operations` - Page in/out operations
- `system.paging.faults` - Page fault counts

### Process Scrapers

Two scrapers provide process-level insights:

**Process Scraper** - Aggregate process counts:

- `system.processes.running` - Running processes
- `system.processes.blocked` - Blocked processes

**Processes Scraper** - Per-process metrics:

- `process.cpu.time` - CPU time per process
- `process.memory.usage` - Memory usage per process
- `process.disk.io` - Disk I/O per process

## Advanced Configuration

### Filesystem Metrics Configuration

For production environments with diverse filesystem types:

```yaml
receivers:
  hostmetrics:
    collection_interval: 10s
    scrapers:
      filesystem:
        # Only collect from specific filesystem types
        include_fs_types:
          match_type: strict
          fs_types: [ext3, ext4, xfs, btrfs, zfs]

        # Exclude temporary and virtual filesystems
        exclude:
          mount_points:
            - "/tmp/*"
            - "/dev/shm"
            - "/run/*"
            - "/sys/*"
          fs_types: [tmpfs, devtmpfs, autofs]

        # Include metrics for virtual filesystems
        include_virtual_filesystems: false
```

### Process Metrics Configuration

To collect detailed per-process metrics:

```yaml
receivers:
  hostmetrics:
    collection_interval: 10s
    scrapers:
      # Aggregate process counts
      process:
        metrics:
          system.processes.created:
            enabled: true

      # Detailed per-process metrics
      processes:
        # Include specific processes by name
        include:
          names: ["nginx", "mysql", "redis", "postgres"]
          match_type: regexp

        # Or exclude specific processes
        exclude:
          names: ["^kernel.*"]

        # Mute errors for processes that terminate during collection
        mute_process_name_error: true

        # Limit number of processes to track
        max_processes: 256
```

#### Permission Requirements

Process metrics require elevated permissions. Configure based on your system:

**Linux (systemd):**

```ini
# /lib/systemd/system/otelcol-contrib.service
[Service]
User=root
Group=root
# Or use capabilities instead of root
AmbientCapabilities=CAP_SYS_PTRACE CAP_DAC_READ_SEARCH
```

**Docker:**

```bash
docker run --pid=host --cap-add=SYS_PTRACE ...
```

**Kubernetes:**

```yaml
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: otel-collector
    securityContext:
      capabilities:
        add: ["SYS_PTRACE", "DAC_READ_SEARCH"]
```

## Container Deployments

### Docker Configuration

When running the Collector in a container, mount host directories to collect host (not container) metrics:

```bash
# Full host filesystem access
docker run \
  -v /:/hostfs:ro \
  -v ./config.yaml:/etc/otel-collector-config.yaml \
  otel/opentelemetry-collector-contrib:latest \
  --config=/etc/otel-collector-config.yaml

# Minimal required mounts
docker run \
  -v /proc:/hostfs/proc:ro \
  -v /sys:/hostfs/sys:ro \
  -v /etc/hostname:/hostfs/etc/hostname:ro \
  -v ./config.yaml:/etc/otel-collector-config.yaml \
  otel/opentelemetry-collector-contrib:latest
```

**Configuration with root_path:**

```yaml
receivers:
  hostmetrics:
    root_path: /hostfs
    collection_interval: 10s
    scrapers:
      cpu:
      memory:
      disk:
      filesystem:
      network:
```

### Kubernetes DaemonSet

Deploy as a DaemonSet to collect metrics from all nodes:

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: otel-collector
spec:
  selector:
    matchLabels:
      app: otel-collector
  template:
    metadata:
      labels:
        app: otel-collector
    spec:
      serviceAccountName: otel-collector
      containers:
      - name: otel-collector
        image: otel/opentelemetry-collector-contrib:latest
        volumeMounts:
        - name: hostfs
          mountPath: /hostfs
          readOnly: true
        - name: config
          mountPath: /etc/otel-collector-config.yaml
          subPath: config.yaml
        env:
        - name: NODE_NAME
          valueFrom:
            fieldRef:
              fieldPath: spec.nodeName
      volumes:
      - name: hostfs
        hostPath:
          path: /
      - name: config
        configMap:
          name: otel-collector-config
      hostNetwork: true
      hostPID: true
```

## Resource Detection

The Resource Detection Processor automatically discovers and adds metadata about the environment:

```yaml
processors:
  resourcedetection:
    # Detectors to run
    detectors: [env, system, docker, ec2, gcp, azure, aks, eks, gke]

    # Detection timeout
    timeout: 5s

    # Override existing attributes
    override: false

    # Configure specific detectors
    system:
      hostname_sources: [dns, os, cname]

    ec2:
      tags:
        - "^env$"
        - "^team$"

    docker:
      use_hostname_if_available: true
```

### Available Detectors

- **env** - Environment variables
- **system** - System information (hostname, OS, architecture)
- **docker** - Docker container metadata
- **ec2** - AWS EC2 instance metadata
- **ecs** - AWS ECS task metadata
- **eks** - AWS EKS cluster information
- **gcp** - Google Cloud Platform metadata
- **gke** - Google Kubernetes Engine metadata
- **azure** - Azure VM metadata
- **aks** - Azure Kubernetes Service metadata
- **kubernetes** - Kubernetes pod/node metadata

### Hostname Configuration

Control how hostnames are determined:

```yaml
processors:
  resourcedetection/custom:
    detectors: [system]
    system:
      # Sources: dns, os, cname, lookup
      hostname_sources: [dns, os]

      # Use FQDN
      use_fqdn: true
```

## Performance Optimization

### Collection Interval Tuning

Balance between data granularity and resource usage:

```yaml
receivers:
  hostmetrics:
    # High-frequency for critical metrics
    collection_interval: 5s
    scrapers:
      cpu:
      memory:

  hostmetrics/detailed:
    # Lower frequency for detailed metrics
    collection_interval: 30s
    scrapers:
      filesystem:
      processes:
```

### Metric Filtering

Reduce data volume by filtering unnecessary metrics:

```yaml
processors:
  filter/metrics:
    metrics:
      exclude:
        match_type: regexp
        metric_names:
          - "system\\.network\\.io.*"
          - "system\\.disk\\.merged"
```

### Batching Configuration

Optimize export efficiency:

```yaml
processors:
  batch:
    # Maximum time before sending
    timeout: 10s
    # Maximum batch size
    send_batch_size: 1024
    # Maximum queue size
    send_batch_max_size: 2048
```

## Troubleshooting

### Common Issues and Solutions

#### 1. Missing Metrics

**Problem:** Some expected metrics aren't being collected.

**Solutions:**

- Check if the scraper is enabled in configuration
- Verify permissions (especially for process metrics)
- Ensure filesystem/device isn't excluded
- Check collector logs for errors

#### 2. High CPU Usage

**Problem:** Collector consuming excessive CPU.

**Solutions:**

- Increase collection interval
- Reduce number of processes tracked
- Filter out unnecessary metrics
- Enable metric aggregation

#### 3. Permission Denied Errors

**Problem:** Cannot collect process or certain system metrics.

**Solutions:**

```bash
# Check current permissions
ps aux | grep otelcol

# Run with elevated permissions
sudo systemctl edit otelcol-contrib
# Add: User=root

# Or add specific capabilities
setcap cap_sys_ptrace,cap_dac_read_search+ep /usr/bin/otelcol-contrib
```

#### 4. Container Metrics Instead of Host

**Problem:** Seeing container metrics when expecting host metrics.

**Solution:**

```yaml
# Ensure root_path is set
receivers:
  hostmetrics:
    root_path: /hostfs

# Verify mounts
docker inspect <container_id> | grep Mounts -A 20
```

### Debug Logging

Enable debug logging to troubleshoot issues:

```yaml
service:
  telemetry:
    logs:
      level: debug
      development: true
```

## Monitoring Best Practices

### 1. Establish Baselines

- Collect metrics for at least 1-2 weeks
- Identify normal operating ranges
- Document peak usage patterns

### 2. Set Meaningful Alerts

```yaml
# Example alert thresholds
- CPU utilization > 80% for 5 minutes
- Memory utilization > 90% for 10 minutes
- Disk usage > 85%
- Load average > number of CPU cores
```

### 3. Create Dashboards

Group related metrics for quick insights:

- **System Overview** - CPU, memory, load
- **Storage** - Disk usage, I/O, filesystem
- **Network** - Traffic, errors, connections
- **Processes** - Top consumers, process counts

### 4. Correlate with Application Metrics

- Link system metrics with application performance
- Identify resource constraints affecting applications
- Plan capacity based on usage trends

## Integration with Uptrace

To send metrics to Uptrace:

```yaml
exporters:
  otlp/uptrace:
    endpoint: api.uptrace.dev:4317
    headers:
      uptrace-dsn: "your-project-dsn"
    compression: gzip

service:
  pipelines:
    metrics:
      receivers: [hostmetrics]
      processors: [resourcedetection, batch]
      exporters: [otlp/uptrace]
```

See the [complete Uptrace integration guide](/get) for detailed setup instructions.

## Security Considerations

### Principle of Least Privilege

- Run with minimal required permissions
- Use capabilities instead of root when possible
- Restrict file system access with read-only mounts

### Sensitive Data

- Process names may reveal application architecture
- Network connections could expose service topology
- Consider filtering sensitive metrics before export

### Configuration Security

```yaml
# Use environment variables for sensitive data
exporters:
  otlp:
    endpoint: ${OTLP_ENDPOINT}
    headers:
      api-key: ${API_KEY}
```

## What's Next?

Expand your observability stack with these complementary receivers:

- **OpenTelemetry Kubernetes** - Collect Kubernetes cluster metrics and metadata
- **OpenTelemetry Docker** - Monitor Docker containers and daemon metrics
- **OpenTelemetry Redis** - Track Redis performance and usage
- **OpenTelemetry PostgreSQL** - Monitor PostgreSQL database metrics
- **Prometheus Integration** - Scrape Prometheus metrics

## Additional Resources

- [Official hostmetricsreceiver Documentation](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/hostmetricsreceiver)
- [Troubleshooting Guide](https://github.com/open-telemetry/opentelemetry-collector/blob/main/docs/troubleshooting.md)
