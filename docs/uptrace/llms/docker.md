# Source: https://uptrace.dev/raw/get/hosted/docker.md

# Deploying Uptrace with Docker

> Quick deployment of Uptrace using Docker Compose with pre-configured services including ClickHouse, PostgreSQL, and Redis.

This guide provides step-by-step instructions for deploying Uptrace, an open-source APM and observability platform, using Docker and Docker Compose. This method is ideal for quick setup, local development, testing environments, and small-scale production deployments. Uptrace supports distributed tracing, metrics, and log management to help you monitor your applications effectively.

## What is Docker?

Docker is a platform for developing, shipping, and running applications in containers. Containers package your application and all its dependencies together, ensuring it runs consistently across different environments.

**Docker Compose** is a tool for defining and running multi-container Docker applications. With a single configuration file, you can spin up all the services your application needs.

## When to Use Docker Deployment

Docker deployment is best suited for:

- **Quick evaluation**: Test Uptrace features before committing to production
- **Local development**: Run Uptrace locally for application development
- **Small teams**: Simple deployment for teams getting started with observability
- **Testing environments**: Isolated environments for testing configurations

For production deployments at scale, consider the [Kubernetes deployment](/get/hosted/k8s) or [Ansible deployment](/get/hosted/ansible) options.

## Prerequisites

Before proceeding with this guide, ensure you have:

1. **Docker installed** on your system - Follow the [official installation guide](https://docs.docker.com/get-docker/)
2. **Docker Compose** - Typically included with Docker Desktop, or install separately for Linux
3. **Git** - For cloning the repository
4. **Minimum system requirements**:

  - 2+ CPU cores
  - 4GB+ RAM
  - 10GB+ disk space for initial setup

### Verify Docker Installation

Check that Docker and Docker Compose are properly installed:

```shell
docker --version
docker compose version
```

## Quick Start Installation

### Step 1: Clone the Repository

Clone the Uptrace repository and navigate to the Docker example directory:

```shell
git clone https://github.com/uptrace/uptrace.git
cd uptrace/example/docker
```

### Step 2: Pull Container Images

Download all required container images before starting the services:

```shell
docker compose pull
```

This command pulls the following images:

- **Uptrace** - The main application
- **ClickHouse** - Time-series database for observability data
- **PostgreSQL** - Relational database for metadata
- **Redis** - In-memory cache
- **OpenTelemetry Collector** - Telemetry data collection and processing
- **MailHog** - Email testing tool (optional)

### Step 3: Start Services

Launch all services in detached mode (running in the background):

```shell
docker compose up -d
```

Docker Compose will:

1. Create a dedicated network for the services
2. Start all containers in the correct order
3. Initialize databases and create required schemas
4. Configure OpenTelemetry Collector

### Step 4: Verify Installation

Check that all services are running correctly:

```shell
docker compose ps
```

All services should show a status of "Up" or "running".

View Uptrace application logs to confirm successful startup:

```shell
docker compose logs uptrace
```

Look for log messages indicating that Uptrace has successfully connected to ClickHouse and PostgreSQL, and is ready to accept connections.

## Accessing Uptrace

### Web Interface

Once all services are running, access the Uptrace web interface:

- **URL**: [http://localhost:14318](http://localhost:14318)
- **Email**: `admin@uptrace.local`
- **Password**: `admin`

### First Login

After logging in with the default credentials:

1. **Change the default password** immediately for security
2. **Explore the interface** and familiarize yourself with the dashboard
3. **Create a new project** for your application

## Understanding the Docker Setup

### Services Architecture

The Docker Compose configuration includes the following services:

#### Uptrace Application

- **Port**: 14318 (HTTP)
- **Purpose**: Main application server providing the web UI and API
- **Dependencies**: ClickHouse, PostgreSQL, Redis

#### ClickHouse

- **Port**: 9000 (native), 8123 (HTTP)
- **Purpose**: Stores all observability data (spans, logs, metrics, events)
- **Data retention**: Configurable, defaults to 30 days

#### PostgreSQL

- **Port**: 5432
- **Purpose**: Stores metadata (users, projects, monitors, alert configurations)
- **Database**: `uptrace`

#### Redis

- **Port**: 6379
- **Purpose**: In-memory caching for improved query performance
- **Persistence**: Disabled by default (ephemeral cache)

#### OpenTelemetry Collector

- **Port**: 4317 (gRPC), 4318 (HTTP)
- **Purpose**: Collects telemetry data from applications and forwards to Uptrace
- **Monitoring**: Pre-configured to monitor host metrics and PostgreSQL

#### MailHog (Optional)

- **Web UI Port**: 8025
- **SMTP Port**: 1025
- **Purpose**: Email testing and debugging

### Data Persistence

By default, the Docker setup uses named volumes for data persistence:

- `uptrace_clickhouse_data` - ClickHouse database files
- `uptrace_postgres_data` - PostgreSQL database files

Data persists across container restarts and recreations.

## Monitoring and Testing

### Self-Monitoring

Uptrace monitors itself using the uptrace-go OpenTelemetry distribution. After starting the services:

1. Wait approximately 30 seconds
2. Refresh the Uptrace web interface several times
3. Navigate to your project dashboard
4. You should see traces and metrics from Uptrace itself

This self-monitoring demonstrates that:

- OpenTelemetry instrumentation is working
- Data is flowing through the collector
- ClickHouse is storing data correctly
- The web interface can query and display data

### Email Testing with MailHog

MailHog captures all emails sent by Uptrace, making it easy to test notifications and alerts without sending real emails.

Access the MailHog web interface at [http://localhost:8025](http://localhost:8025).

**Testing email notifications**:

1. Configure an alert or monitor in Uptrace
2. Trigger the alert condition
3. Check MailHog to see the notification email

**Note**: In production environments, configure a real SMTP server instead of MailHog.

## Configuration and Customization

### Configuration File Location

The main Uptrace configuration file is located at:

```text
uptrace/example/docker/uptrace.yml
```

### Common Customizations

#### Change HTTP Port

To run Uptrace on a different port, edit the `docker-compose.yml` file:

```yaml
services:
  uptrace:
    ports:
      - '8080:80' # Change 8080 to your preferred host port
```

Then restart the service:

```shell
docker compose up -d uptrace
```

#### Configure Data Retention

Edit `uptrace.yml` to adjust how long data is retained:

```yaml
ch:
  retention:
    ttl:
      traces: 7 DAY
      metrics: 30 DAY
      logs: 7 DAY
```

Restart Uptrace after making changes:

```shell
docker compose restart uptrace
```

#### Adjust Resource Limits

Limit memory and CPU usage for containers by adding resource constraints to `docker-compose.yml`:

```yaml
services:
  clickhouse:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
        reservations:
          memory: 1G
```

For detailed configuration options, see the [Configuration guide](/get/hosted/config).

## Instrumenting Your Applications

To send telemetry data from your applications to Uptrace:

### Step 1: Get OpenTelemetry Endpoint

Your applications should send data to the OpenTelemetry Collector:

- **gRPC endpoint**: `http://localhost:4317`
- **HTTP endpoint**: `http://localhost:4318`

### Step 2: Configure Your Application

Use the appropriate OpenTelemetry SDK for your programming language. Here are quick examples:

<code-group>

```go [Go]
import (
    "go.opentelemetry.io/otel"
    "go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc"
)

exporter, err := otlptracegrpc.New(ctx,
    otlptracegrpc.WithEndpoint("localhost:4317"),
    otlptracegrpc.WithInsecure(),
)
```

```python [Python]
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

otlp_exporter = OTLPSpanExporter(
    endpoint="http://localhost:4317",
    insecure=True
)
```

```javascript [Node.js]
const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-grpc');

const exporter = new OTLPTraceExporter({
  url: 'http://localhost:4317',
});
```

```java [Java]
import io.opentelemetry.exporter.otlp.trace.OtlpGrpcSpanExporter;

OtlpGrpcSpanExporter spanExporter = OtlpGrpcSpanExporter.builder()
    .setEndpoint("http://localhost:4317")
    .build();
```

</code-group>

### Step 3: View Your Data

After instrumenting your application:

1. Run your application
2. Generate some traffic or activity
3. Open the Uptrace web interface
4. Navigate to your project
5. View traces, metrics, and logs in real-time

For framework-specific guides, see the [instrumentation guides](/guides).

## Managing Services

### View Service Status

Check the status of all services:

```shell
docker compose ps
```

### View Logs

View logs for all services:

```shell
docker compose logs
```

View logs for a specific service:

```shell
docker compose logs uptrace
docker compose logs clickhouse
```

Follow logs in real-time:

```shell
docker compose logs -f uptrace
```

### Restart Services

Restart all services:

```shell
docker compose restart
```

Restart a specific service:

```shell
docker compose restart uptrace
```

### Stop Services

Stop all services without removing containers:

```shell
docker compose stop
```

### Start Stopped Services

Start previously stopped services:

```shell
docker compose start
```

## Upgrading Uptrace

Only upgrades to the next minor version are tested and supported, for example, upgrading from 1.1 to 1.2. Skipping minor versions (e.g., 1.1 to 1.3) is not supported â upgrade one minor version at a time.

To upgrade Uptrace:

1. **Back up your databases.** Create backups of both PostgreSQL and ClickHouse before proceeding. See [Backup and Restore](#backup-and-restore) for details.
2. **Pull the latest images and recreate containers:**```shell
cd uptrace/example/docker
docker compose pull
docker compose up -d
```

Docker automatically validates the config, runs database migrations, and restarts Uptrace.

## Troubleshooting

### Common Issues and Solutions

#### Services Won't Start

**Problem**: Containers fail to start or immediately exit

**Solutions**:

```shell
# Check detailed logs
docker compose logs

# Check for port conflicts
sudo lsof -i :14318
sudo lsof -i :4317

# Check available disk space
df -h

# Check Docker daemon status
sudo systemctl status docker
```

#### Cannot Connect to Uptrace

**Problem**: Web interface is not accessible at localhost:14318

**Solutions**:

1. Verify the container is running:```shell
docker compose ps uptrace
```
2. Check if the port is exposed correctly:```shell
docker compose port uptrace 14318
```
3. Test with curl:```shell
curl http://localhost:14318/api/v1/health
```
4. Check firewall rules if accessing from another machine

#### Database Connection Errors

**Problem**: Uptrace logs show database connection failures

**Solutions**:

1. Verify database containers are healthy:```shell
docker compose ps clickhouse postgres
```
2. Check database logs:```shell
docker compose logs clickhouse
docker compose logs postgres
```
3. Verify network connectivity between containers:```shell
docker compose exec uptrace ping clickhouse
```

#### Out of Memory Errors

**Problem**: ClickHouse or other services crash with OOM errors

**Solutions**:

1. Increase Docker memory limit in Docker Desktop settings
2. Add memory limits to docker-compose.yml
3. Reduce data retention period
4. Clean up old data

#### Data Not Appearing in UI

**Problem**: Applications are instrumented but data doesn't show in Uptrace

**Solutions**:

1. Verify OpenTelemetry Collector is running:```shell
docker compose logs otel-collector
```
2. Check that your application is sending to the correct endpoint
3. Verify network connectivity from your application to the collector
4. Check for errors in application logs
5. Wait 30-60 seconds for data to be processed and indexed

### Diagnostic Commands

```shell
# Check container health
docker compose ps

# View container resource usage
docker stats

# Inspect container details
docker compose inspect uptrace

# Execute commands inside containers
docker compose exec uptrace sh
docker compose exec clickhouse clickhouse-client

# View Docker network configuration
docker network inspect docker_default
```

## Backup and Restore

### Backing Up Data

#### Backup Volumes

Create backups of persistent volumes:

```shell
# Backup ClickHouse data
docker run --rm -v uptrace_clickhouse_data:/data -v $(pwd):/backup ubuntu tar czf /backup/clickhouse-backup.tar.gz /data

# Backup PostgreSQL data
docker run --rm -v uptrace_postgres_data:/data -v $(pwd):/backup ubuntu tar czf /backup/postgres-backup.tar.gz /data
```

#### Database Dumps

Create logical backups:

```shell
# PostgreSQL dump
docker compose exec postgres pg_dump -U uptrace uptrace > uptrace-pg-backup.sql

# ClickHouse backup (requires clickhouse-backup tool)
docker compose exec clickhouse clickhouse-backup create
```

### Restoring Data

Restore from volume backups:

```shell
# Stop services
docker compose down

# Restore ClickHouse
docker run --rm -v uptrace_clickhouse_data:/data -v $(pwd):/backup ubuntu tar xzf /backup/clickhouse-backup.tar.gz -C /

# Restore PostgreSQL
docker run --rm -v uptrace_postgres_data:/data -v $(pwd):/backup ubuntu tar xzf /backup/postgres-backup.tar.gz -C /

# Start services
docker compose up -d
```

## Cleanup

### Stop and Remove Containers

Stop all services and remove containers:

```shell
docker compose down
```

### Remove Volumes (Delete All Data)

To completely remove all data and start fresh:

```shell
docker compose down -v
```

This command removes:

- All containers
- All volumes (data will be lost)
- The network

Named volumes can also be removed individually:

```shell
docker volume rm uptrace_clickhouse_data
docker volume rm uptrace_postgres_data
```

### Remove Images

Remove downloaded images to free up disk space:

```shell
docker compose down --rmi all
```

## Production Considerations

While Docker Compose is suitable for small-scale deployments, consider these factors for production use:

### Security

- **Change default passwords** immediately
- **Use secrets management** instead of plain text credentials
- **Enable TLS/SSL** for all connections
- **Restrict network access** using firewalls
- **Keep images updated** with security patches

### High Availability

Docker Compose doesn't provide high availability. For production:

- Deploy on **Kubernetes** for automatic failover
- Use **managed databases** (AWS RDS, Azure Database)
- Implement **load balancing** across multiple instances
- Set up **automated backups** and disaster recovery

### Monitoring

- Monitor Docker host resources
- Set up alerts for container failures
- Track disk space usage
- Monitor database performance
- Use external monitoring tools

### Scaling

Docker Compose has limited scaling capabilities. To scale:

- Deploy on **Kubernetes** for horizontal scaling
- Use orchestration tools for multi-host deployments
- Implement **auto-scaling** based on metrics

For production-grade deployments, see:

- [Kubernetes deployment guide](/get/hosted/k8s)
- [Ansible deployment guide](/get/hosted/ansible)

## Next Steps

After successful deployment:

1. **Instrument your applications** with OpenTelemetry - See [language-specific guides](/guides)
2. **Create custom dashboards** for your services
3. **Set up monitors and alerts** for critical metrics
4. **Explore distributed tracing** features
5. **Configure log aggregation** from your applications
6. **Review the configuration guide** for advanced options - [Configuration](/get/hosted/config)
7. **Learn about Uptrace features** - [Features](/features)

## Alternative Deployment Methods

Docker Compose is one of several deployment options:

- [DEB/RPM packages](/get/hosted/install) - For traditional server deployments
- [Ansible](/get/hosted/ansible) - For automated bare metal deployments
- [Kubernetes](/get/hosted/k8s) - For container orchestration at scale

Choose the method that best fits your infrastructure and requirements.
