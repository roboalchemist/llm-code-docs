# Source: https://uptrace.dev/raw/guides/opentelemetry-docker.md

# OpenTelemetry Docker Monitoring with Collector and Docker Stats

> Learn how to monitor Docker containers with OpenTelemetry. Set up the Collector, configure Docker Stats receiver, and use Docker Compose - with examples.

Docker containers are lightweight and portable, but their dynamic nature makes monitoring challenging. Containers start, stop, and move between hosts constantlyâyou need visibility into their resource usage and performance.

This guide explains how to monitor Docker containers using the OpenTelemetry Collector with the Docker Stats receiver. It covers setting up the Collector (either directly or with Docker Compose), collecting container metrics, and exporting them to your monitoring backend.

## Why Monitor Docker Containers?

Monitoring Docker containers is a key part of ensuring that containerized applications run reliably and perform efficiently. Here's why it matters:

- **Performance Optimization**: Identify resource bottlenecks and optimize container performance before they impact users. By tracking CPU, memory, and I/O metrics, you can fine-tune resource allocation and application configurations.
- **Resource Management**: Ensure efficient allocation of CPU, memory, and network resources across containers. Docker containers share the host system's resources, so monitoring helps prevent resource contention and ensures fair distribution.
- **Troubleshooting**: Quickly diagnose issues by tracking container metrics and identifying anomalies. When a container crashes or performs poorly, historical metrics provide invaluable insights into what went wrong and why.
- **Cost Control**: In cloud environments, efficient resource monitoring can lead to significant cost savings. By right-sizing containers and eliminating waste, you can optimize your cloud spending.
- **Security and Compliance**: Monitor container behavior to detect unusual activity that might indicate security breaches or compliance violations.

## What is OpenTelemetry Collector?

[OpenTelemetry Collector](/opentelemetry/collector) acts as a central hub for receiving, processing, and exporting telemetry data to various backends or observability tools.

The Collector can receive telemetry data (traces, metrics, and logs) from multiple sources, including:

- Applications instrumented with OpenTelemetry SDKs.
- Other telemetry agents or collectors.
- Legacy systems using protocols like Jaeger, Zipkin, Prometheus, etc.

## Why Use OpenTelemetry Collector with Docker?

Running the OpenTelemetry Collector in Docker offers several advantages:

- **Portability**: Behaves identically across development, staging, and production environments
- **Simple deployment**: All dependencies packaged in the container image
- **Easy scaling**: Run multiple collector instances with Docker Compose or Kubernetes
- **Isolation**: Resource limits prevent the collector from impacting host performance
- **Version management**: Pin specific versions and roll back if needed

## OpenTelemetry Docker Stats Receiver

OpenTelemetry Docker Stats [receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/dockerstatsreceiver) allows you to collect container-level resource metrics from Docker. It retrieves metrics such as CPU usage, memory usage, network statistics, and disk I/O from Docker containers and exposes them as OpenTelemetry metrics.

The receiver communicates with the Docker daemon through its API, querying container statistics at regular intervals. This approach is non-intrusive and doesn't require any modifications to your container images or applications.

### CPU Metrics

The Docker Stats receiver collects comprehensive CPU metrics for monitoring container processor usage:

<table>
<thead>
  <tr>
    <th>
      Metric
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      container.cpu.usage.system
    </td>
    
    <td>
      System CPU usage, as reported by docker.
    </td>
  </tr>
  
  <tr>
    <td>
      container.cpu.usage.total
    </td>
    
    <td>
      Total CPU time consumed.
    </td>
  </tr>
  
  <tr>
    <td>
      container.cpu.usage.kernelmode
    </td>
    
    <td>
      Time spent by tasks of the cgroup in kernel mode (Linux).
    </td>
  </tr>
  
  <tr>
    <td>
      container.cpu.usage.usermode
    </td>
    
    <td>
      Time spent by tasks of the cgroup in user mode (Linux).
    </td>
  </tr>
  
  <tr>
    <td>
      container.cpu.usage.percpu
    </td>
    
    <td>
      Per-core CPU usage by the container.
    </td>
  </tr>
  
  <tr>
    <td>
      container.cpu.throttling_data.periods
    </td>
    
    <td>
      Number of periods with throttling active.
    </td>
  </tr>
  
  <tr>
    <td>
      container.cpu.throttling_data.throttled_periods
    </td>
    
    <td>
      Number of periods when the container hits its throttling limit.
    </td>
  </tr>
  
  <tr>
    <td>
      container.cpu.throttling_data.throttled_time
    </td>
    
    <td>
      Aggregate time the container was throttled.
    </td>
  </tr>
  
  <tr>
    <td>
      container.cpu.percent
    </td>
    
    <td>
      Percent of CPU used by the container.
    </td>
  </tr>
</tbody>
</table>

### Memory Metrics

Memory metrics help you understand RAM usage and identify memory leaks or pressure:

<table>
<thead>
  <tr>
    <th>
      Metric
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      container.memory.usage.limit
    </td>
    
    <td>
      Memory limit of the container.
    </td>
  </tr>
  
  <tr>
    <td>
      container.memory.usage.total
    </td>
    
    <td>
      Memory usage of the container. This excludes the cache.
    </td>
  </tr>
  
  <tr>
    <td>
      container.memory.usage.max
    </td>
    
    <td>
      Maximum memory usage.
    </td>
  </tr>
  
  <tr>
    <td>
      container.memory.percent
    </td>
    
    <td>
      Percentage of memory used.
    </td>
  </tr>
  
  <tr>
    <td>
      container.memory.cache
    </td>
    
    <td>
      The amount of memory used by the processes of this control group that can be associated precisely with a block on a block device.
    </td>
  </tr>
  
  <tr>
    <td>
      container.memory.rss
    </td>
    
    <td>
      The amount of memory that doesn't correspond to anything on disk: stacks, heaps, and anonymous memory maps.
    </td>
  </tr>
  
  <tr>
    <td>
      container.memory.rss_huge
    </td>
    
    <td>
      Number of bytes of anonymous transparent hugepages in this cgroup.
    </td>
  </tr>
  
  <tr>
    <td>
      container.memory.dirty
    </td>
    
    <td>
      Bytes that are waiting to get written back to the disk, from this cgroup.
    </td>
  </tr>
  
  <tr>
    <td>
      container.memory.writeback
    </td>
    
    <td>
      Number of bytes of file/anon cache that are queued for syncing to disk in this cgroup.
    </td>
  </tr>
  
  <tr>
    <td>
      container.memory.mapped_file
    </td>
    
    <td>
      Indicates the amount of memory mapped by the processes in the control group.
    </td>
  </tr>
  
  <tr>
    <td>
      container.memory.swap
    </td>
    
    <td>
      The amount of swap currently used by the processes in this cgroup.
    </td>
  </tr>
</tbody>
</table>

### Block I/O Metrics

Block I/O metrics track disk read and write operations for your containers:

<table>
<thead>
  <tr>
    <th>
      Metric
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      container.blockio.io_merged_recursive
    </td>
    
    <td>
      Number of bios/requests merged into requests belonging to this cgroup and its descendant cgroups.
    </td>
  </tr>
  
  <tr>
    <td>
      container.blockio.io_queued_recursive
    </td>
    
    <td>
      Number of requests queued up for this cgroup and its descendant cgroups.
    </td>
  </tr>
  
  <tr>
    <td>
      container.blockio.io_service_bytes_recursive
    </td>
    
    <td>
      Number of bytes transferred to/from the disk by the group and descendant groups.
    </td>
  </tr>
  
  <tr>
    <td>
      container.blockio.io_service_time_recursive
    </td>
    
    <td>
      Total amount of time in nanoseconds between request dispatch and request completion for the IOs done by this cgroup and descendant cgroups.
    </td>
  </tr>
  
  <tr>
    <td>
      container.blockio.io_serviced_recursive
    </td>
    
    <td>
      Number of IOs (bio) issued to the disk by the group and descendant groups.
    </td>
  </tr>
  
  <tr>
    <td>
      container.blockio.io_time_recursive
    </td>
    
    <td>
      Disk time allocated to cgroup (and descendant cgroups) per device in milliseconds.
    </td>
  </tr>
  
  <tr>
    <td>
      container.blockio.io_wait_time_recursive
    </td>
    
    <td>
      Total amount of time the IOs for this cgroup (and descendant cgroups) spent waiting in the scheduler queues for service.
    </td>
  </tr>
  
  <tr>
    <td>
      container.blockio.sectors_recursive
    </td>
    
    <td>
      Number of sectors transferred to/from disk by the group and descendant groups.
    </td>
  </tr>
</tbody>
</table>

### Network Metrics

Network metrics provide visibility into container network traffic and errors:

<table>
<thead>
  <tr>
    <th>
      Metric
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      container.network.io.usage.rx_bytes
    </td>
    
    <td>
      Bytes received by the container.
    </td>
  </tr>
  
  <tr>
    <td>
      container.network.io.usage.tx_bytes
    </td>
    
    <td>
      Bytes sent.
    </td>
  </tr>
  
  <tr>
    <td>
      container.network.io.usage.rx_dropped
    </td>
    
    <td>
      Incoming packets dropped.
    </td>
  </tr>
  
  <tr>
    <td>
      container.network.io.usage.tx_dropped
    </td>
    
    <td>
      Outgoing packets dropped.
    </td>
  </tr>
  
  <tr>
    <td>
      container.network.io.usage.rx_errors
    </td>
    
    <td>
      Received errors.
    </td>
  </tr>
  
  <tr>
    <td>
      container.network.io.usage.tx_errors
    </td>
    
    <td>
      Sent errors.
    </td>
  </tr>
  
  <tr>
    <td>
      container.network.io.usage.rx_packets
    </td>
    
    <td>
      Packets received.
    </td>
  </tr>
  
  <tr>
    <td>
      container.network.io.usage.tx_packets
    </td>
    
    <td>
      Packets sent.
    </td>
  </tr>
</tbody>
</table>

## Prerequisites

Before getting started with Docker container monitoring, ensure you have:

- **Docker installed and running** on your system (Docker API version 1.25 or higher)
- **Running Docker containers** to monitor (or follow our setup below)
- **Basic understanding** of YAML configuration files

### Choose Your Monitoring Backend

In this guide, we use **Uptrace** for examples, but you can use any [OTLP-compatible backend](/blog/opentelemetry-backend).

**For Uptrace:**

- Sign up at [uptrace.dev](https://app.uptrace.dev/join)
- Get your DSN from Project â Data Source Name

**For other backends:**

- Configure the OTLP exporter endpoint in your collector config
- See the [OpenTelemetry documentation](https://opentelemetry.io/docs/collector/configuration/) for other exporters

### Verify Your Docker Installation

Check your Docker version and API compatibility:

```bash
docker --version
# Docker version 27.0.0 or higher

docker version --format '{{.Server.APIVersion}}'
# Should return 1.25 or higher
```

Verify Docker is running:

```bash
docker ps
```

### Start Sample Containers (Optional)

If you don't have containers running, start a few for testing:

```bash
# Start an Nginx web server
docker run -d --name nginx-test -p 8080:80 nginx:latest

# Start a MySQL database
docker run -d --name mysql-test \
  -e MYSQL_ROOT_PASSWORD=mysecretpassword \
  -p 3306:3306 mysql:latest

# Start Redis
docker run -d --name redis-test -p 6379:6379 redis:latest
```

Verify containers are running:

```bash
docker ps
```

You should see your containers listed with their status as "Up".

## Setting Up OpenTelemetry Collector

You have several options for running the OpenTelemetry Collector. Choose the one that best fits your environment.

### Option 1: Run Collector Natively

Running the collector as a native binary is ideal for development and testing environments.

#### Step 1: Download OpenTelemetry Collector

Download the appropriate binary for your operating system from the [OpenTelemetry Collector releases](https://github.com/open-telemetry/opentelemetry-collector-releases/releases) page. We'll use the `contrib` distribution which includes the Docker Stats receiver.

**For Linux (amd64):**

```bash
curl --proto '=https' --tlsv1.2 -fOL \
  https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.145.0/otelcol-contrib_0.145.0_linux_amd64.tar.gz
```

**For macOS (Apple Silicon/arm64):**

```bash
curl --proto '=https' --tlsv1.2 -fOL \
  https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.145.0/otelcol-contrib_0.145.0_darwin_arm64.tar.gz
```

**For macOS (Intel/amd64):**

```bash
curl --proto '=https' --tlsv1.2 -fOL \
  https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.145.0/otelcol-contrib_0.145.0_darwin_amd64.tar.gz
```

#### Step 2: Extract and Install

```bash
# Create directory
mkdir otelcol-contrib

# Extract the archive (adjust filename for your OS)
tar xvzf otelcol-contrib_0.145.0_*.tar.gz -C otelcol-contrib

# Navigate to the directory
cd otelcol-contrib

# Make binary executable
chmod +x otelcol-contrib
```

#### Step 3: Verify Installation

```bash
./otelcol-contrib --version
# Output: otelcol-contrib version v0.145.0
```

Optionally, move the binary to your system path for easier access:

```bash
sudo mv otelcol-contrib /usr/local/bin/
```

### Option 2: Run Collector in Docker

Running the collector as a Docker container is often the preferred method for containerized environments. The OpenTelemetry project provides official Docker images on Docker Hub under `otel/opentelemetry-collector-contrib`.

#### Pull the OpenTelemetry Docker Image

OpenTelemetry provides official Docker images on Docker Hub and GitHub Container Registry. The `opentelemetry-collector-contrib` distribution includes all community-contributed receivers, processors, and exporters, including the Docker Stats receiver.

```bash
# From Docker Hub (recommended)
docker pull otel/opentelemetry-collector-contrib:0.145.0

# Or from GitHub Container Registry
docker pull ghcr.io/open-telemetry/opentelemetry-collector-releases/opentelemetry-collector-contrib:0.145.0
```

You can find all available versions on [Docker Hub: otel/opentelemetry-collector-contrib](https://hub.docker.com/r/otel/opentelemetry-collector-contrib).

#### Download and Verify the Image

After pulling the image, verify it's available:

```bash
# List Docker images
docker images | grep opentelemetry-collector

# Check image details
docker inspect otel/opentelemetry-collector-contrib:0.145.0
```

#### Basic Docker Run Command

Run the collector with a custom configuration:

```bash
docker run -d \
  --name otel-collector \
  -v $(pwd)/config.yaml:/etc/otelcol-contrib/config.yaml \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  -p 4317:4317 \
  -p 4318:4318 \
  --restart unless-stopped \
  otel/opentelemetry-collector-contrib:0.145.0
```

**Important:** The `-v /var/run/docker.sock:/var/run/docker.sock:ro` mount is required for Docker Stats receiver to access container metrics.

#### Understanding the Docker Run Parameters

- `-d`: Run container in detached mode (background)
- `--name`: Assign a name for easy reference
- `-v $(pwd)/config.yaml:/etc/otelcol-contrib/config.yaml`: Mount your configuration file
- `-v /var/run/docker.sock:/var/run/docker.sock:ro`: Mount Docker socket (read-only)
- `-p 4317:4317`: Expose OTLP gRPC receiver port
- `-p 4318:4318`: Expose OTLP HTTP receiver port
- `--restart unless-stopped`: Automatically restart on failure

#### Docker Socket Access on Different OS

On **Linux** and **macOS**, the default Docker socket path is the same:

```bash
-v /var/run/docker.sock:/var/run/docker.sock:ro
```

On **Windows** (Docker Desktop), use a double slash:

```bash
-v //var/run/docker.sock:/var/run/docker.sock:ro
```

#### Viewing Logs

Monitor collector logs to ensure it's working correctly:

```bash
# Follow logs in real-time
docker logs -f otel-collector

# View last 100 lines
docker logs --tail 100 otel-collector
```

#### Stopping and Removing

```bash
# Stop the container
docker stop otel-collector

# Remove the container
docker rm otel-collector
```

### Option 3: Docker Compose Setup

For production-like environments or when running multiple services together, Docker Compose provides an elegant solution. This Docker Compose example shows how to set up the OpenTelemetry Collector for monitoring your Docker containers.

#### Basic OpenTelemetry Docker Compose Configuration

Create a `docker-compose.yaml` file for the OpenTelemetry Collector:

```yaml
services:
  otel-collector:
    image: otel/opentelemetry-collector-contrib:0.145.0
    container_name: otel-collector
    command: ["--config=/etc/otelcol-contrib/config.yaml"]
    volumes:
      - ./config.yaml:/etc/otelcol-contrib/config.yaml
      - /var/run/docker.sock:/var/run/docker.sock:ro
    ports:
      - "4317:4317"   # OTLP gRPC
      - "4318:4318"   # OTLP HTTP
      - "8888:8888"   # Prometheus metrics (collector's own metrics)
      - "13133:13133" # Health check
    restart: unless-stopped
    networks:
      - monitoring
    healthcheck:
      test: ["CMD", "wget", "--spider", "-q", "http://localhost:13133/"]
      interval: 30s
      timeout: 10s
      retries: 3

networks:
  monitoring:
    driver: bridge
```

This OpenTelemetry Docker Compose example provides a production-ready setup with health checks and proper networking.

#### Complete OpenTelemetry Collector Docker Compose Example

For a complete monitoring stack, the following OpenTelemetry Docker Compose example includes the Collector and sample applications to demonstrate an end-to-end setup.

```yaml
services:
  # OpenTelemetry Collector
  otel-collector:
    image: otel/opentelemetry-collector-contrib:0.145.0
    container_name: otel-collector
    command: ["--config=/etc/otelcol-contrib/config.yaml"]
    volumes:
      - ./otel-config.yaml:/etc/otelcol-contrib/config.yaml
      - /var/run/docker.sock:/var/run/docker.sock:ro
    ports:
      - "4317:4317"   # OTLP gRPC receiver
      - "4318:4318"   # OTLP HTTP receiver
    environment:
      - UPTRACE_DSN=${UPTRACE_DSN}
    networks:
      - monitoring
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "wget", "--spider", "-q", "http://localhost:13133/"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Sample Application (to generate telemetry)
  sample-app:
    image: nginx:latest
    container_name: sample-app
    ports:
      - "8080:80"
    networks:
      - monitoring
    labels:
      app: "sample-nginx"
      environment: "production"

  # Another sample service
  redis:
    image: redis:latest
    container_name: sample-redis
    ports:
      - "6379:6379"
    networks:
      - monitoring
    labels:
      app: "redis"
      environment: "production"

networks:
  monitoring:
    driver: bridge
```

This Docker Compose tutorial demonstrates a complete setup for OpenTelemetry monitoring with multiple services.

```bash
# Start all services
docker compose up -d

# View logs from all services
docker compose logs -f

# View logs from specific service
docker compose logs -f otel-collector

# Check service status
docker compose ps
```

#### Stopping the Stack

```bash
# Stop all services
docker compose down

# Stop and remove volumes
docker compose down -v
```

#### Environment Variables in Docker Compose

Use environment variables for sensitive data:

```yaml
services:
  otel-collector:
    image: otel/opentelemetry-collector-contrib:0.145.0
    environment:
      - UPTRACE_DSN=${UPTRACE_DSN}
    env_file:
      - .env
```

Create a `.env` file:

```text
UPTRACE_DSN=your_dsn_here
```

**Important:** Add `.env` to your `.gitignore` to avoid committing secrets.

## Configuring Docker Stats Receiver

The Docker Stats receiver connects to the Docker daemon to collect container metrics. Create a configuration file to define how metrics are collected and exported.

### Basic Configuration

For a minimal setup, create a file named `config.yaml`. This example exports to Uptrace, but you can replace the exporter with any OTLP-compatible backend:

```yaml
receivers:
  docker_stats:
    endpoint: unix:///var/run/docker.sock
    collection_interval: 30s

exporters:
  otlp:
    endpoint: api.uptrace.dev:4317
    headers:
      uptrace-dsn: '<YOUR_DSN>'

processors:
  batch:
    timeout: 10s

service:
  pipelines:
    metrics:
      receivers: [docker_stats]
      processors: [batch]
      exporters: [otlp]
```

Replace `<YOUR_DSN>` with your Uptrace DSN, or configure a different exporter for your monitoring backend.

This basic configuration:

- Collects Docker container metrics every 30 seconds
- Uses the batch processor to optimize data transmission
- Exports metrics to Uptrace via OTLP protocol

### Production Configuration

For production environments, use this enhanced configuration with additional features:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
      http:

  docker_stats:
    endpoint: unix:///var/run/docker.sock
    collection_interval: 15s
    timeout: 10s
    api_version: "1.25"

    # Enable additional metrics
    metrics:
      container.uptime:
        enabled: true
      container.restarts:
        enabled: true
      container.network.io.usage.rx_errors:
        enabled: true
      container.network.io.usage.tx_errors:
        enabled: true
      container.network.io.usage.rx_packets:
        enabled: true
      container.network.io.usage.tx_packets:
        enabled: true
      container.cpu.usage.percpu:
        enabled: true

    # Filter out unwanted containers
    excluded_images:
      - undesired-container
      - /.*undesired.*/
      - another-*-container

    # Map container labels to metric labels
    container_labels_to_metric_labels:
      my.container.label: my-metric-label
      my.other.container.label: my-other-metric-label
      com.docker.compose.service: service_name
      com.docker.compose.project: project_name

    # Map environment variables to metric labels
    env_vars_to_metric_labels:
      MY_ENVIRONMENT_VARIABLE: my-metric-label
      MY_OTHER_ENVIRONMENT_VARIABLE: my-other-metric-label

exporters:
  otlp:
    endpoint: api.uptrace.dev:4317  # Replace with your backend endpoint
    headers:
      uptrace-dsn: '<YOUR_DSN>'     # Or use your backend's auth method

processors:
  resourcedetection:
    detectors: [env, system]

  cumulativetodelta:

  batch:
    timeout: 10s
    send_batch_size: 1000

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp]

    metrics:
      receivers: [otlp, docker_stats]
      processors: [cumulativetodelta, batch, resourcedetection]
      exporters: [otlp]
```

This production configuration includes:

- **Additional metrics** for better observability (uptime, restarts, network errors)
- **Container filtering** to exclude test/development containers
- **Label mapping** to enrich metrics with custom labels
- **Resource detection** to add host information to metrics
- **Both OTLP receivers** for collecting traces from applications

### Docker Socket Configuration

The Docker socket path varies by operating system:

**For Linux:**

The default socket path is `/var/run/docker.sock`

```yaml
docker_stats:
  endpoint: unix:///var/run/docker.sock
```

**For macOS with Docker Desktop:**

Check the socket location:

```bash
ls -la /var/run/docker.sock
# or
ls -la ~/.docker/run/docker.sock
```

Update your configuration accordingly if the path differs.

**For Windows with Docker Desktop:**

Docker uses a named pipe:

```yaml
docker_stats:
  endpoint: npipe:////./pipe/docker_engine
```

### Alternative: Docker Daemon TCP Endpoint

If you prefer using a TCP endpoint instead of Unix socket, you can configure the Docker daemon to listen on a TCP port. This is useful for remote monitoring.

First, [configure](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-socket-option) Docker daemon to listen on `0.0.0.0:2375`, then adjust the OpenTelemetry Collector config:

```yaml
receivers:
  docker_stats:
    endpoint: http://localhost:2375
```

**Note:** The Unix socket approach is more secure and should be preferred for local monitoring.

## Combining Multiple Receivers

The OpenTelemetry Collector can receive telemetry from multiple sources simultaneously, making it a central hub for all your observability data.

### Docker Stats + OTLP Configuration

Monitor both Docker containers and application traces/metrics:

```yaml
receivers:
  # Collect Docker container metrics
  docker_stats:
    endpoint: unix:///var/run/docker.sock
    collection_interval: 15s
    metrics:
      container.uptime:
        enabled: true
      container.restarts:
        enabled: true

  # Receive application telemetry
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:
    timeout: 10s
    send_batch_size: 1024

  resourcedetection:
    detectors: [env, system, docker]

exporters:
  otlp:
    endpoint: api.uptrace.dev:4317
    headers:
      uptrace-dsn: '<YOUR_DSN>'

service:
  pipelines:
    # Pipeline for application traces
    traces:
      receivers: [otlp]
      processors: [batch, resourcedetection]
      exporters: [otlp]

    # Pipeline for all metrics (Docker + Application)
    metrics:
      receivers: [otlp, docker_stats]
      processors: [batch, resourcedetection]
      exporters: [otlp]

    # Pipeline for application logs
    logs:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp]
```

This configuration creates a complete observability pipeline:

- **Docker Stats receiver** collects container resource metrics
- **OTLP receivers** collect application traces, metrics, and logs
- All data is enriched with resource information
- Everything flows to a single backend (Uptrace)

### Benefits of Combined Collection

1. **Unified View**: Correlate application performance with container resource usage
2. **Simplified Architecture**: One collector handles all telemetry types
3. **Consistent Processing**: Apply the same processors to all data
4. **Reduced Overhead**: Single agent instead of multiple monitoring tools

## Running the Collector

### Run in Foreground (for testing)

From the directory containing your `config.yaml` file:

```bash
./otelcol-contrib --config ./config.yaml
```

Or if you installed it to your system path:

```bash
otelcol-contrib --config ./config.yaml
```

You should see output indicating the collector has started:

```text
2026-02-07T10:00:00.000Z info service/telemetry.go:84 Setting up own telemetry...
2026-02-07T10:00:00.100Z info service/service.go:143 Starting otelcol-contrib...
2026-02-07T10:00:00.200Z info extensions/extensions.go:42 Starting extensions...
2026-02-07T10:00:01.000Z info dockerstatsreceiver@v0.145.0/receiver.go:123 Starting docker_stats receiver
```

Press `Ctrl+C` to stop the collector.

### Run in Background

To run the collector in the background:

```bash
# Start in background and redirect output to log file
./otelcol-contrib --config ./config.yaml &> otelcol-output.log & echo "$!" > otel-pid

# View logs in real-time
tail -f otelcol-output.log

# View last 50 lines of logs
tail -n 50 otelcol-output.log

# Stop the collector
kill "$(< otel-pid)"
```

### Run as systemd Service (Linux)

For production deployments on Linux, create a systemd service for automatic startup and management.

Create a service file `/etc/systemd/system/otelcol.service`:

```ini
[Unit]
Description=OpenTelemetry Collector
After=network.target docker.service
Requires=docker.service

[Service]
Type=simple
User=otel
Group=docker
ExecStart=/usr/local/bin/otelcol-contrib --config /etc/otelcol/config.yaml
Restart=on-failure
RestartSec=30

[Install]
WantedBy=multi-user.target
```

Create the otel user and copy your configuration:

```bash
# Create otel user
sudo useradd -r -s /bin/false otel

# Add otel user to docker group
sudo usermod -aG docker otel

# Create config directory
sudo mkdir -p /etc/otelcol

# Copy your config file
sudo cp config.yaml /etc/otelcol/

# Set permissions
sudo chown -R otel:otel /etc/otelcol
```

Enable and start the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable otelcol
sudo systemctl start otelcol

# Check status
sudo systemctl status otelcol

# View logs
sudo journalctl -u otelcol -f
```

### Verify Data Collection

Within 30 seconds of starting the collector, you should see metrics appearing in your Uptrace dashboard:

1. Navigate to your Uptrace instance
2. Go to the **Metrics** section
3. You should see Docker container metrics like:

  - `container.cpu.usage.total`
  - `container.memory.usage.total`
  - `container.network.io.usage.rx_bytes`
  - And many more

If metrics don't appear, check the [Troubleshooting](#troubleshooting) section below.

## Monitoring with Uptrace

Once the metrics are collected and exported, you can visualize them using Uptrace dashboards. Uptrace provides powerful querying capabilities and customizable dashboards for analyzing your Docker container metrics.

### Creating Dashboards

In the Uptrace dashboard:

1. Navigate to **Dashboards** tab
2. Click **New Dashboard**
3. Add panels to visualize different metrics

You can create various types of visualizations:

- **Time series charts** for CPU and memory usage over time
- **Gauges** for current resource utilization
- **Tables** for listing containers and their current state
- **Heatmaps** for distribution analysis

### Example Queries

Here are some useful queries to get started:

**Average CPU usage per container:**

```text
avg(container.cpu.utilization) by container.name
```

**Memory usage percentage:**

```text
(container.memory.usage.total / container.memory.usage.limit) * 100
```

**Network throughput:**

```text
rate(container.network.io.usage.rx_bytes[5m]) + rate(container.network.io.usage.tx_bytes[5m])
```

**Containers by state:**

```text
count(container.cpu.utilization) by container.name
```

### Setting Up Alerts

Configure alerts to be notified of potential issues:

1. In your dashboard panel, set up monitors and create alerts
2. Set conditions, for example:

  - CPU usage > 80% for 5 minutes
  - Memory usage > 90% for 2 minutes
  - Container restarts > 3 in 10 minutes
3. Configure notification channels (email, Slack, PagerDuty, etc.)

Common alert rules:

- High CPU utilization
- Memory pressure
- Excessive container restarts
- Network errors
- Disk I/O saturation

## OpenTelemetry Backend

The OpenTelemetry Collector exports metrics to any [OTLP-compatible backend](/opentelemetry/backend-comparison). This guide uses Uptrace in examples, but you can use for example:

- **Prometheus + Grafana** - Self-hosted metrics and visualization
- **Grafana Cloud** - Managed observability platform
- **Datadog, New Relic** - Commercial APM solutions

To switch backends, update the exporter configuration in your `config.yaml`.

## Troubleshooting

### Permission Denied: Cannot Access Docker Socket

**Error:**

```text
Error: Get "http://%2Fvar%2Frun%2Fdocker.sock/_ping": dial unix /var/run/docker.sock: connect: permission denied
```

**Solution:**

Add your user to the docker group:

```bash
sudo usermod -aG docker $USER
```

Then log out and log back in, or run:

```bash
newgrp docker
```

Alternatively, if running the collector in Docker, ensure the container has access to the socket.

For systemd service, ensure the service user is in the docker group (as shown in the systemd setup above).

### Docker Socket Not Found

**Error:**

```text
Error: dial unix /var/run/docker.sock: connect: no such file or directory
```

**Solution:**

Verify Docker is running:

```bash
docker ps
```

Check if the socket exists:

```bash
# Linux
ls -la /var/run/docker.sock

# macOS
ls -la /var/run/docker.sock
ls -la ~/.docker/run/docker.sock
```

Update your `config.yaml` with the correct socket path if it differs from the default.

### No Metrics in Uptrace

If metrics aren't appearing in Uptrace after a few minutes:

**1. Verify DSN is correct:**

- Check that you've correctly copied your DSN from Uptrace Settings â Ingestion Settings
- Ensure there are no extra spaces or quotes around the DSN value

**2. Check network connectivity:**

```bash
# Test connection to Uptrace
curl -v https://api.uptrace.dev:4317
```

**3. Review collector logs:**

```bash
# If running in foreground, check the console output
# If running in background:
tail -f otelcol-output.log

# If running in Docker:
docker logs otel-collector

# If running as systemd:
sudo journalctl -u otelcol -f
```

Look for error messages related to exporters or authentication.

**4. Enable debug logging:**

Add to your `config.yaml`:

```yaml
service:
  telemetry:
    logs:
      level: debug
  pipelines:
    # ... your existing pipelines
```

Restart the collector and check logs for detailed output.

**5. Verify firewall rules:**

Ensure outbound connections to `api.uptrace.dev:4317` are allowed.

### Docker API Version Incompatibility

**Error:**

```text
Error response from daemon: client version 1.41 is too new. Maximum supported API version is 1.40
```

**Solution:**

Check your Docker API version:

```bash
docker version --format '{{.Server.APIVersion}}'
```

Specify the API version in your `config.yaml`:

```yaml
receivers:
  docker_stats:
    endpoint: unix:///var/run/docker.sock
    api_version: "1.40"  # Use your Docker's API version
```

### High CPU Usage by Collector

If the OpenTelemetry Collector is consuming excessive CPU:

**1. Increase collection interval:**

```yaml
docker_stats:
  collection_interval: 60s  # Increase from default 30s or 15s
```

**2. Disable expensive metrics:**

```yaml
docker_stats:
  metrics:
    container.cpu.usage.percpu:
      enabled: false
    container.blockio.io_service_bytes_recursive:
      enabled: false
```

**3. Optimize batch processing:**

```yaml
processors:
  batch:
    timeout: 30s
    send_batch_size: 2000  # Increase batch size
```

**4. Filter containers:**

Use `excluded_images` to reduce the number of monitored containers:

```yaml
docker_stats:
  excluded_images:
    - /.*test.*/
    - /.*dev.*/
```

### Collector Crashes or Restarts Frequently

**Common causes and solutions:**

**1. Memory issues:**

- Reduce collection frequency
- Decrease batch size
- Enable memory_limiter processor:

```yaml
processors:
  memory_limiter:
    check_interval: 1s
    limit_mib: 512
    spike_limit_mib: 128

service:
  pipelines:
    metrics:
      receivers: [docker_stats]
      processors: [memory_limiter, batch]
      exporters: [otlp]
```

**2. Configuration errors:**

- Validate your YAML syntax
- Check collector logs for specific error messages
- Test with minimal configuration first

**3. Network issues:**

Add retry configuration to exporter:

```yaml
exporters:
  otlp:
    endpoint: api.uptrace.dev:4317
    headers:
      uptrace-dsn: '<YOUR_DSN>'
    retry_on_failure:
      enabled: true
      initial_interval: 5s
      max_interval: 30s
      max_elapsed_time: 300s
```

### Missing Expected Metrics

If some metrics are not appearing:

**1. Check if metrics are enabled:**

Many metrics are disabled by default. Enable them explicitly:

```yaml
docker_stats:
  metrics:
    container.uptime:
      enabled: true
    container.restarts:
      enabled: true
    # ... enable other metrics as needed
```

**2. Verify container is running:**

The receiver only collects metrics from running containers.

**3. Check cgroup version:**

Some metrics are only available on cgroup v1 or v2. Check your system:

```bash
# Check cgroup version
mount | grep cgroup
```

If you're using cgroup v2, some v1-specific metrics won't be available.

## FAQ

**What's the difference between Docker Stats receiver and cAdvisor?** The Docker Stats receiver queries the Docker API directly for container metrics. cAdvisor is a standalone container monitoring daemon that also works with Kubernetes. For pure Docker environments, the Docker Stats receiver is simpler. For Kubernetes, cAdvisor is typically already running as part of kubelet.

**Can I monitor Docker Swarm with this setup?** Yes. The Docker Stats receiver works with Docker Swarm since it connects to the Docker daemon API. Deploy the Collector on each Swarm node to collect metrics from all containers.

**Should I use the core or contrib distribution?** The Docker Stats receiver is part of the `contrib` distribution only. Use `otel/opentelemetry-collector-contrib` for Docker monitoring.

**How do I monitor containers on remote hosts?** Configure the Docker daemon to listen on a TCP endpoint, then set `endpoint: http://remote-host:2375` in the receiver config. Use TLS for production remote access.

**Why are some block I/O metrics missing?** Block I/O metrics depend on your cgroup version. cgroup v2 (default on modern Linux) reports different metrics than cgroup v1. Check with `mount | grep cgroup` to identify your version.

**How do I reduce the volume of metrics collected?** Use `excluded_images` to skip test/development containers, increase `collection_interval`, and disable expensive metrics like `container.cpu.usage.percpu` that you don't need.

## Additional Resources

- [Docker Stats Receiver Docs](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/dockerstatsreceiver)
- [OpenTelemetry Docker Demo](https://github.com/open-telemetry/opentelemetry-demo)
- [Docker Hub](https://hub.docker.com/r/otel/opentelemetry-collector-contrib)
- [Binary downloads](https://github.com/open-telemetry/opentelemetry-collector-releases/releases)

## What's next?

With Docker container monitoring configured, you can track resource usage, container health, and application performance.

Next steps to enhance your observability:

- Scale up to [Kubernetes monitoring](/get/kubernetes) for orchestrated deployments
- Collect container logs with the [Filelog Receiver](/guides/opentelemetry-filelog-receiver)
- Monitor databases with [PostgreSQL](/guides/opentelemetry-postgresql) and [MySQL](/guides/opentelemetry-mysql) receivers
- Track message brokers with [RabbitMQ](/guides/opentelemetry-rabbitmq) or [Kafka](/guides/opentelemetry-kafka) monitoring
- Collect host-level metrics with the [host metrics receiver](/opentelemetry/collector/host-metrics)
- Explore [top APM tools](/tools/top-apm-tools) for container monitoring
