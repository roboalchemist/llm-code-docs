# Source: https://docs.rootly.com/edge-connectors-installation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Installation & Deployment

> Install and deploy the Rootly Edge Connector in your environment

## Overview

The Rootly Edge Connector is a lightweight agent that runs in your infrastructure to securely integrate with internal systems. This guide covers installation, configuration, and deployment for production environments.

## Prerequisites

Before installing the Edge Connector, ensure you have:

* **Operating System**: Linux (systemd-based distributions recommended)
* **Network Access**: Outbound HTTPS to `rec.rootly.com` (port 443)
* **API Key**: Edge Connector API key from Rootly (see [Getting Started](/edge-connectors#getting-started))
* **Permissions**: Root or sudo access for system installation

<Info>
  The Edge Connector only requires **outbound** network access. No inbound firewall rules are needed.
</Info>

## Installation Methods

Choose one of the following installation methods based on your environment:

### Option 1: Homebrew (Recommended for macOS/Linux)

```bash  theme={null}
# Add Rootly tap
brew tap rootlyhq/tap

# Install Edge Connector
brew install rootly-edge-connector

# Verify installation
rootly-edge-connector --version
```

### Option 2: Go Install

If you have Go 1.24+ installed:

```bash  theme={null}
# Install latest version
go install github.com/rootlyhq/rootly-edge-connector/cmd/rec@latest

# The binary will be installed to $GOPATH/bin/rec
```

### Option 3: Build from Source

```bash  theme={null}
# Clone repository
git clone https://github.com/rootlyhq/rootly-edge-connector.git
cd rootly-edge-connector

# Build and install
make build
make install

# Verify installation
rootly-edge-connector --version
```

### Option 4: Pre-built Binaries

For enterprise customers with access to private releases:

<Note>
  Contact [support@rootly.com](mailto:support@rootly.com) for access to pre-built binaries and download credentials.
</Note>

## Quick Start (Development)

For testing and development, run the Edge Connector directly:

### 1. Create Configuration Files

**config.yml:**

```yaml  theme={null}
app:
  name: "rootly-edge-connector"

rootly:
  api_url: "https://rec.rootly.com"
  api_path: "/v1"
  api_key: "YOUR_REC_API_KEY"

poller:
  polling_wait_interval_ms: 5000
  visibility_timeout_sec: 30

logging:
  level: "info"
  format: "json"

metrics:
  enabled: true
  port: 9090
```

**actions.yml:**

```yaml  theme={null}
defaults:
  timeout: 30

on:
  alert.created:
    script: /path/to/test-script.sh
    parameters:
      alert_id: "{{ id }}"
      severity: "{{ labels.severity }}"
    timeout: 60
```

### 2. Set API Key

```bash  theme={null}
export REC_API_KEY="your-api-key-here"
```

### 3. Run the Connector

```bash  theme={null}
./rootly-edge-connector \
  -config config.yml \
  -actions actions.yml
```

You should see output indicating the connector is polling:

```
INFO Starting Rootly Edge Connector
INFO Registered actions with backend  action_count=1
INFO Polling for events  poll_interval=10s
```

## Production Installation (Linux/systemd)

For production deployments, install the Edge Connector as a systemd service.

### Step 1: Create System User

Create a dedicated user for the Edge Connector:

```bash  theme={null}
sudo groupadd -r rootly
sudo useradd -r -g rootly -s /bin/false -d /opt/rootly-edge-connector rootly
```

### Step 2: Create Directories

Set up the directory structure:

```bash  theme={null}
sudo mkdir -p /opt/rootly-edge-connector/bin
sudo mkdir -p /opt/rootly-edge-connector/scripts
sudo mkdir -p /etc/rootly-edge-connector
sudo mkdir -p /var/log/rootly-edge-connector
```

### Step 3: Install Binary

Copy the binary to the installation directory. The binary location depends on your installation method:

```bash  theme={null}
# If you built from source or downloaded a binary directly:
sudo cp rootly-edge-connector /opt/rootly-edge-connector/bin/

# If you used Homebrew:
sudo cp $(which rootly-edge-connector) /opt/rootly-edge-connector/bin/

# If you used Go install:
sudo cp $GOPATH/bin/rec /opt/rootly-edge-connector/bin/rootly-edge-connector

# Set permissions
sudo chmod +x /opt/rootly-edge-connector/bin/rootly-edge-connector
```

### Step 4: Create Configuration

Create your configuration files in `/etc/rootly-edge-connector/`:

**`/etc/rootly-edge-connector/config.yml`:**

```yaml  theme={null}
app:
  name: "rootly-edge-connector"

rootly:
  api_url: "https://rec.rootly.com"
  api_path: "/v1"
  api_key: "YOUR_REC_API_KEY"

poller:
  polling_wait_interval_ms: 10000
  visibility_timeout_sec: 30
  max_number_of_messages: 10

security:
  script_timeout: 300
  allowed_script_paths:
    - /opt/rootly-edge-connector/scripts

logging:
  level: "info"
  format: "json"
  output: "stdout"

metrics:
  enabled: true
  port: 9090
  path: "/metrics"
```

**`/etc/rootly-edge-connector/actions.yml`:**

```yaml  theme={null}
# Automatic action - runs when incidents are created
on:
  incident.created:
    http:
      url: "{{ env.WEBHOOK_URL }}"
      method: POST
      headers:
        Content-Type: "application/json"
      body: |
        {
          "incident_id": "{{ id }}",
          "title": "{{ title }}",
          "severity": "{{ severity.name }}"
        }
    timeout: 30

# Manual action - triggered by users from Rootly UI
callable:
  restart_service:
    name: "Restart Service"
    trigger: alert.action_triggered
    script: /opt/rootly-edge-connector/scripts/restart.sh
    parameter_definitions:
      - name: service_name
        type: string
        required: true
    timeout: 120
```

### Step 5: Create Environment File

Store the API key and sensitive values securely:

```bash  theme={null}
sudo tee /etc/rootly-edge-connector/environment > /dev/null <<EOF
REC_API_KEY=your-actual-api-key-here
REC_WEBHOOK_URL=https://example.com/webhook
EOF
```

### Step 6: Set Permissions

Secure the files with appropriate permissions:

```bash  theme={null}
sudo chown -R rootly:rootly /opt/rootly-edge-connector
sudo chown -R rootly:rootly /etc/rootly-edge-connector
sudo chown -R rootly:rootly /var/log/rootly-edge-connector

# Protect sensitive files
sudo chmod 600 /etc/rootly-edge-connector/environment
sudo chmod 640 /etc/rootly-edge-connector/config.yml
sudo chmod 640 /etc/rootly-edge-connector/actions.yml
```

### Step 7: Create Systemd Service

Create `/etc/systemd/system/rootly-edge-connector.service`:

```ini  theme={null}
[Unit]
Description=Rootly Edge Connector
Documentation=https://docs.rootly.com/edge-connectors
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=rootly
Group=rootly
EnvironmentFile=/etc/rootly-edge-connector/environment
ExecStart=/opt/rootly-edge-connector/bin/rootly-edge-connector \
  -config /etc/rootly-edge-connector/config.yml \
  -actions /etc/rootly-edge-connector/actions.yml
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal
SyslogIdentifier=rootly-edge-connector

# Security hardening
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=strict
ProtectHome=true
ReadWritePaths=/var/log/rootly-edge-connector

[Install]
WantedBy=multi-user.target
```

### Step 8: Enable and Start Service

```bash  theme={null}
# Reload systemd
sudo systemctl daemon-reload

# Enable service to start on boot
sudo systemctl enable rootly-edge-connector

# Start the service
sudo systemctl start rootly-edge-connector

# Check status
sudo systemctl status rootly-edge-connector
```

## Configuration Reference

### config.yml

```yaml  theme={null}
# Application settings
app:
  name: "rootly-edge-connector"

# Rootly API configuration (required)
rootly:
  api_url: "https://rec.rootly.com"  # API base URL
  api_path: "/v1"                     # API path prefix (default: /v1)
  api_key: "YOUR_REC_API_KEY"         # Set via REC_API_KEY env var (format: rec_xxxxx)

# Polling configuration
poller:
  polling_wait_interval_ms: 10000    # Polling interval in milliseconds (default: 5000)
  visibility_timeout_sec: 30         # Event visibility timeout (default: 30)
  max_number_of_messages: 10         # Max events per poll (default: 10)
  retry_on_error: true               # Retry on errors (default: true)
  retry_backoff: "exponential"       # Backoff: "exponential" or "linear"
  max_retries: 3                     # Max retry attempts (default: 3)

# Worker pool configuration
pool:
  max_number_of_workers: 10          # Maximum workers (default: 10)
  min_number_of_workers: 2           # Minimum workers (default: 2)
  queue_size: 1000                   # Event queue size (default: 1000)
  keep_alive_time_ms: 60000          # Worker keep-alive (default: 60000)
  monitoring_period_ms: 30000        # Monitoring interval (default: 30000)

# Security settings
security:
  script_timeout: 300                # Default script timeout in seconds (default: 300)
  allowed_script_paths:              # Restrict script execution (empty = allow all)
    - /opt/rootly-edge-connector/scripts
    - /usr/local/bin
  global_env:                        # Environment variables for all scripts
    ENVIRONMENT: "production"
    LOG_LEVEL: "info"

# Logging configuration
logging:
  level: "info"                      # Log level: trace, debug, info, warn, error
  format: "json"                     # Format: json, text, colored (default: text)
  output: "stdout"                   # Output: stdout or file path
  # Log rotation (only for file output)
  max_size_mb: 100                   # Max file size before rotation (default: 100)
  max_backups: 3                     # Old log files to retain (default: 3)
  max_age_days: 7                    # Days to retain old logs (default: 7)
  compress: true                     # Compress rotated logs (default: true)
  local_time: false                  # Use local time for filenames (default: false)

# Metrics configuration
metrics:
  enabled: true                      # Enable Prometheus metrics (default: true)
  port: 9090                         # Metrics HTTP server port (default: 9090)
  path: "/metrics"                   # Metrics endpoint path (default: /metrics)
  labels:                            # Custom labels for all metrics
    connector_id: "prod-us-east-1"   # Unique connector identifier
    environment: "production"        # Environment (production, staging, dev)
    region: "us-east-1"              # Geographic region or datacenter
```

### actions.yml

See the [Action Configuration](/edge-connectors-actions) guide for detailed action syntax.

## Management Commands

### Systemd Service Control

```bash  theme={null}
# Start the service
sudo systemctl start rootly-edge-connector

# Stop the service
sudo systemctl stop rootly-edge-connector

# Restart the service
sudo systemctl restart rootly-edge-connector

# View service status
sudo systemctl status rootly-edge-connector

# Enable start on boot
sudo systemctl enable rootly-edge-connector

# Disable start on boot
sudo systemctl disable rootly-edge-connector
```

### Viewing Logs

```bash  theme={null}
# Follow logs in real-time
sudo journalctl -u rootly-edge-connector -f

# View last 100 lines
sudo journalctl -u rootly-edge-connector -n 100

# View logs since 1 hour ago
sudo journalctl -u rootly-edge-connector --since "1 hour ago"

# View errors only
sudo journalctl -u rootly-edge-connector -p err

# Export logs to file
sudo journalctl -u rootly-edge-connector > connector-logs.txt
```

### Checking Metrics

If metrics are enabled (default port 9090):

```bash  theme={null}
# View Prometheus metrics
curl http://localhost:9090/metrics

# Common metrics:
# - rec_events_polled_total: Total events polled
# - rec_actions_executed_total: Total actions executed
# - rec_action_duration_seconds: Action execution duration
# - rec_poll_errors_total: Polling errors
```

## Updating

### Update Binary

```bash  theme={null}
# Stop the service
sudo systemctl stop rootly-edge-connector

# Backup current binary
sudo cp /opt/rootly-edge-connector/bin/rootly-edge-connector \
       /opt/rootly-edge-connector/bin/rootly-edge-connector.backup

# Install new binary
sudo cp new-rootly-edge-connector /opt/rootly-edge-connector/bin/rootly-edge-connector
sudo chmod +x /opt/rootly-edge-connector/bin/rootly-edge-connector
sudo chown rootly:rootly /opt/rootly-edge-connector/bin/rootly-edge-connector

# Start the service
sudo systemctl start rootly-edge-connector

# Verify
sudo systemctl status rootly-edge-connector
```

### Update Configuration

```bash  theme={null}
# Edit configuration files
sudo vim /etc/rootly-edge-connector/config.yml
sudo vim /etc/rootly-edge-connector/actions.yml

# Validate configuration (optional)
sudo -u rootly /opt/rootly-edge-connector/bin/rootly-edge-connector \
  -config /etc/rootly-edge-connector/config.yml \
  -actions /etc/rootly-edge-connector/actions.yml \
  -validate

# Restart service to apply changes
sudo systemctl restart rootly-edge-connector
```

## Docker Deployment

For containerized environments:

**Dockerfile:**

```dockerfile  theme={null}
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/*

COPY rootly-edge-connector /usr/local/bin/
RUN chmod +x /usr/local/bin/rootly-edge-connector

USER 1000:1000

ENTRYPOINT ["/usr/local/bin/rootly-edge-connector"]
CMD ["-config", "/etc/rootly/config.yml", "-actions", "/etc/rootly/actions.yml"]
```

**docker-compose.yml:**

```yaml  theme={null}
version: '3.8'

services:
  edge-connector:
    image: rootly-edge-connector:latest
    container_name: rootly-edge-connector
    restart: always
    environment:
      - REC_API_KEY=${REC_API_KEY}
    volumes:
      - ./config.yml:/etc/rootly/config.yml:ro
      - ./actions.yml:/etc/rootly/actions.yml:ro
      - ./scripts:/opt/scripts:ro
    ports:
      - "9090:9090"  # Metrics port
```

**Run with Docker:**

```bash  theme={null}
# Build image
docker build -t rootly-edge-connector:latest .

# Run container
docker run -d \
  --name rootly-edge-connector \
  --restart always \
  -e REC_API_KEY="your-api-key" \
  -v $(pwd)/config.yml:/etc/rootly/config.yml:ro \
  -v $(pwd)/actions.yml:/etc/rootly/actions.yml:ro \
  -v $(pwd)/scripts:/opt/scripts:ro \
  -p 9090:9090 \
  rootly-edge-connector:latest

# View logs
docker logs -f rootly-edge-connector
```

## Troubleshooting

### Connector Won't Start

**Check configuration syntax:**

```bash  theme={null}
sudo -u rootly /opt/rootly-edge-connector/bin/rootly-edge-connector \
  -config /etc/rootly-edge-connector/config.yml \
  -actions /etc/rootly-edge-connector/actions.yml \
  -validate
```

**Check permissions:**

```bash  theme={null}
ls -la /opt/rootly-edge-connector/bin/
ls -la /etc/rootly-edge-connector/
```

**View detailed logs:**

```bash  theme={null}
sudo journalctl -u rootly-edge-connector -n 50 --no-pager
```

### API Connection Issues

**Test network connectivity:**

```bash  theme={null}
curl -v https://rec.rootly.com/health
```

**Verify API key:**

```bash  theme={null}
# Check environment file
sudo cat /etc/rootly-edge-connector/environment

# Test with API key
curl -H "Authorization: Bearer YOUR_API_KEY" \
  https://rec.rootly.com/rec/v1/health
```

### Actions Not Executing

**Check action registration:**

```bash  theme={null}
# Look for registration success in logs
sudo journalctl -u rootly-edge-connector | grep "Registered actions"
```

**Verify script permissions:**

```bash  theme={null}
# Scripts must be executable
sudo chmod +x /opt/rootly-edge-connector/scripts/*.sh

# Check script ownership
ls -la /opt/rootly-edge-connector/scripts/
```

**Test script manually:**

```bash  theme={null}
sudo -u rootly /opt/rootly-edge-connector/scripts/your-script.sh arg1 arg2
```

### High Memory/CPU Usage

**Check poll interval:**

* Increase `poller.polling_wait_interval_ms` in config.yml (e.g., from 5000 to 30000)

**Review action timeouts:**

* Ensure actions complete within their timeout values
* Check for hung processes

**Monitor metrics:**

```bash  theme={null}
curl http://localhost:9090/metrics | grep rec_
```

## Security Best Practices

### 1. Run as Dedicated User

Always run the Edge Connector as a non-root user with minimal privileges.

### 2. Protect Sensitive Files

```bash  theme={null}
# Environment file should be 600 (owner read/write only)
sudo chmod 600 /etc/rootly-edge-connector/environment

# Config files should be 640 (owner read/write, group read)
sudo chmod 640 /etc/rootly-edge-connector/*.yml
```

### 3. Network Isolation

* Run on a dedicated or isolated host
* Restrict outbound connections to rec.rootly.com only (if using firewall)
* Do not expose metrics port publicly

### 4. Audit Scripts

* Review all scripts before adding to actions.yml
* Use version control for scripts
* Implement pull request approval process

### 5. Rotate API Keys

* Rotate API keys periodically (e.g., quarterly)
* Use different keys for dev/staging/production
* Revoke old keys after rotation

### 6. Monitor Logs

* Set up log aggregation (e.g., to ELK, Splunk)
* Alert on errors and failures
* Review execution logs regularly

## Next Steps

* Configure [Actions](/edge-connectors-actions) for your use cases
* Learn [Template Syntax](/edge-connectors-templates) for dynamic values
* Review [Event Examples](/edge-connectors-event-examples) for payload structures
* See the main [Edge Connectors](/edge-connectors) documentation for architecture details


Built with [Mintlify](https://mintlify.com).