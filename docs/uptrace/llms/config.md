# Source: https://uptrace.dev/raw/opentelemetry/collector/config.md

# Source: https://uptrace.dev/raw/get/hosted/config.md

# Uptrace Configuration Reference

> Reference guide for every Uptrace configuration option from file management to environment variables and ClickHouse tuning.

Uptrace is an [open source APM](/get/hosted/open-source-apm) and observability platform that supports distributed tracing, metrics, and log management. This guide covers comprehensive configuration options for customizing Uptrace settings and optimizing the ClickHouse database schema through a single YAML configuration file.

## Configuration File Management

### Creating and Locating Configuration Files

Generate a default configuration file using the Uptrace binary:

```shell
./uptrace config create -config=/path/to/config.yml
```

Specify the configuration file location using either method:

**CLI argument (recommended):**

```shell
uptrace --config=/etc/uptrace/config.yml serve
```

**Environment variable:**

```shell
export UPTRACE_CONFIG=/etc/uptrace/config.yml
uptrace serve
```

If no configuration path is specified, Uptrace defaults to `/etc/uptrace/config.yml`.

### Environment Variable Integration

Enhance security and flexibility by using environment variables in your YAML configuration:

```yml
pg:
  addr: ${UPTRACE_PG_ADDR:localhost:5432}
  user: ${UPTRACE_PG_USER:uptrace}
  password: ${UPTRACE_PG_PASSWORD}
  database: ${UPTRACE_PG_DATABASE:uptrace}
```

**Environment Variable Syntax:**

- Simple substitution: `${ENV_VAR_NAME}`
- With fallback defaults: `${ENV_VAR_NAME:default_value}`
- Escape dollar signs: Use `$$` to literal `$`

Variables are expanded using Go's [os.Expand](https://pkg.go.dev/os#Expand) function before YAML parsing.

## Database Architecture and Configuration

Uptrace uses a dual-database architecture optimized for different data types and access patterns.

### PostgreSQL: Metadata Storage

PostgreSQL stores application metadata including user accounts, project settings, dashboards, and alert configurations. This database typically requires only a few megabytes of storage.

**Basic Configuration:**

```yml
pg:
  addr: localhost:5432
  user: uptrace
  password: uptrace
  database: uptrace

  # TLS configuration for secure connections
  # Recommended for production deployments
  #tls:
  #  insecure_skip_verify: true  # WARNING: Only for self-signed certificates
```

**High Availability with Read Replicas:**

```yml
pg:
  addr: primary-host:5432
  user: uptrace
  password: uptrace
  database: uptrace

  # Standby replicas
  replicas:
    - standby-host1:5432
    - standby-host2:5432
```

**Using connection string:**

```yaml
pg:
  dsn: postgresql://user:password@host:5432/database?sslmode=verify-full
```

### ClickHouse: Telemetry Data Storage

ClickHouse serves as the primary storage engine for high-volume telemetry data including spans, logs, and metrics. It's optimized for analytical queries and time-series data.

**Basic Configuration:**

```yml
ch_cluster:
  # Cluster name for ClickHouse operations
  cluster: 'uptrace1'

  # High availability features
  replicated: false    # Enable for automatic failover
  distributed: false   # Enable for horizontal scaling (Premium only)

  shards:
    - replicas:
        - addr: localhost:9000
          user: default
          password: ''
          database: uptrace

          # Connection and query timeouts
          dial_timeout: 3s
          write_timeout: 5s
          max_retries: 3
          max_execution_time: 15s
```

**Production High Availability Setup:**

```yml
ch_cluster:
  cluster: 'uptrace1'
  replicated: true

  shards:
    - replicas:
        - addr: clickhouse-1:9000
          user: default
          password: ''
          database: uptrace

        - addr: clickhouse-2:9000
          user: default
          password: ''
          database: uptrace

        - addr: clickhouse-3:9000
          user: default
          password: ''
          database: uptrace
```

**Using connection string:**

```yaml
ch_cluster:
  shards:
    - replicas:
        - dsn: clickhouse://your_username:your_password@your_host:9000/your_database

          # Connection and query timeouts
          dial_timeout: 3s
          write_timeout: 5s
          max_retries: 3
          max_execution_time: 15s
```

### ClickHouse Advanced Configuration

**Query Performance Tuning:**

```yml
ch_cluster:
  shards:
    - replicas:
        - addr: localhost:9000
          # ClickHouse-specific query settings
          query_settings:
            async_insert: 1               # Enable async inserts (default: enabled)
            wait_for_async_insert: 1      # Wait for insert completion (default: disabled)
            max_memory_usage: 10000000000 # 10GB memory limit per query
```

**TLS Configuration for ClickHouse:**

First, configure ClickHouse server to enable secure TCP port:

```xml
<!-- ClickHouse server configuration -->
<?xml version="1.0" ?>
<clickhouse>
  <tcp_port_secure>9440</tcp_port_secure>

  <openSSL>
    <server>
      <certificateFile>/etc/clickhouse/certs/chnode.crt</certificateFile>
      <privateKeyFile>/etc/clickhouse/certs/chnode.key</privateKeyFile>
      <verificationMode>relaxed</verificationMode>
      <caConfig>/etc/clickhouse/certs/Uptrace_CA.crt</caConfig>
      <cacheSessions>true</cacheSessions>
      <disableProtocols>sslv2,sslv3</disableProtocols>
      <preferServerCiphers>true</preferServerCiphers>
    </server>
  </openSSL>
</clickhouse>
```

Then configure Uptrace to use TLS:

```yml
ch_cluster:
  shards:
    - replicas:
        - addr: localhost:9440  # Use secure port
          user: default
          database: uptrace

          tls:
            ca_file: /etc/clickhouse/certs/Uptrace_CA.crt
            cert_file: /etc/clickhouse/certs/chnode.crt
            key_file: /etc/clickhouse/certs/chnode.key
            insecure_skip_verify: false
```

**ClickHouse Cloud Configuration:**

```yml
ch_cluster:
  shards:
    - replicas:
        - addr: tm849a32za.us-central1.gcp.clickhouse.cloud:9440
          user: default
          password: your_cloud_password
          database: uptrace
          tls:
            # Override server name if address doesn't match certificate
            server_name_override: 'tm849a32za.us-central1.gcp.clickhouse.cloud'
```

## Database Management Commands

### Resetting ClickHouse Database

Reset the ClickHouse database to apply schema changes or start fresh:

```shell
uptrace ch reset
```

This is equivalent to running:

```shell
uptrace ch rollback
uptrace ch migrate
```

**â ï¸ Warning:** This will delete all telemetry data (spans, logs, metrics).

### Resetting PostgreSQL Database

Reset the PostgreSQL database to clear metadata and start fresh:

```shell
uptrace pg reset
```

This is equivalent to running:

```shell
uptrace pg rollback
uptrace pg migrate
```

**â ï¸ Warning:** This will delete all metadata including users, projects, dashboards, and alerts.

## Schema Configuration and Optimization

Customize ClickHouse schema settings for optimal performance and storage efficiency.

**â ï¸ Critical:** Schema changes require database reset and will delete all existing data:

```shell
uptrace ch reset
```

### Storage and Compression Settings

```yml
ch_schema:
  # Compression algorithm selection
  # LZ4: Fast compression/decompression, moderate ratio
  # ZSTD(1): Better compression ratio, slightly slower
  # Default: ClickHouse default compression
  compression: ZSTD(1)

  # Storage policies for different data types
  # Configure different storage tiers (SSD, HDD, S3) based on access patterns
  spans_index: { storage_policy: hot_storage }    # Frequently accessed span indexes
  spans_data: { storage_policy: warm_storage }    # Span detail data
  span_links: { storage_policy: cold_storage }    # Span relationship data
  logs_index: { storage_policy: hot_storage }     # Log search indexes
  logs_data: { storage_policy: warm_storage }     # Log detail data
  events_index: { storage_policy: hot_storage }   # Event search indexes
  events_data: { storage_policy: warm_storage }   # Event detail data
  metrics: { storage_policy: hot_storage }        # Metrics time-series data
```

### ClickHouse Replication Setup

**Step 1: Configure ClickHouse Cluster**

Create a cluster configuration with at least 3 replicas. **Critical:** Set `internal_replication = true` to prevent data duplication.

```xml
<clickhouse>
  <remote_servers>
    <uptrace1>
      <shard>
        <internal_replication>true</internal_replication>
        <replica>
          <host>clickhouse-1</host>
          <port>9000</port>
        </replica>
        <replica>
          <host>clickhouse-2</host>
          <port>9000</port>
        </replica>
        <replica>
          <host>clickhouse-3</host>
          <port>9000</port>
        </replica>
      </shard>
    </uptrace1>
  </remote_servers>
</clickhouse>
```

**Step 2: Enable Replication in Uptrace**

```yml
ch_cluster:
  cluster: 'uptrace1'
  replicated: true  # Enable ClickHouse table replication

  shards:
    - replicas:
        - addr: clickhouse-1:9000
        - addr: clickhouse-2:9000
        - addr: clickhouse-3:9000
```

**Step 3: Apply Configuration Changes**

```shell
uptrace ch reset
```

**Step 4: Verify Replication Status**

```sql
SELECT
    database,
    table,
    is_leader,
    replica_is_active
FROM system.replicas;
```

Expected output showing active replicas:

```text
ââdatabaseââ¬âtableââââââââââââ¬âis_leaderââ¬âreplica_is_activeâââââââââââââââââââââââââ
â uptrace  â spans_data      â         1 â {'replica1':1,'replica2':1,'replica3':1} â
â uptrace  â spans_index     â         1 â {'replica1':1,'replica2':1,'replica3':1} â
ââââââââââââ´ââââââââââââââââââ´ââââââââââââ´âââââââââââââââââââââââââââââââââââââââââââ
```

## Network and Domain Configuration

### Port Configuration

Configure network listeners for different protocols:

```yml
listen:
  # HTTP server: OTLP/HTTP API, REST API, and web interface
  http:
    addr: ':80'  # Standard HTTP port

  # gRPC server: OTLP/gRPC for high-performance telemetry ingestion
  grpc:
    addr: ':4317'  # Standard OTLP gRPC port

  # TLS configuration for both HTTP and gRPC
  #tls:
  #  cert_file: /etc/uptrace/uptrace.crt
  #  key_file: /etc/uptrace/uptrace.key
```

### Domain and URL Configuration

**Primary Site Configuration:**

```yml
site:
  # Primary URL for user interface and API access
  # Used for: dashboard links, CORS validation, authentication redirects
  # Must be accessible from all clients and match reverse proxy setup
  url: https://uptrace.mycompany.com
```

**Separate Ingestion Endpoint:**

```yml
site:
  url: https://uptrace.mycompany.com

  # Dedicated URL for telemetry data ingestion
  # Benefits: load balancing, security policies, CDN optimization
  # Defaults to site.url if not specified
  ingest_url: https://ingest.mycompany.com
```

## Security and TLS Configuration

### Automatic TLS with Let's Encrypt

For production deployments with automatic certificate management:

```yml
# -----------------------------------------------------------------------------
# SSL/TLS Certificate Management
# -----------------------------------------------------------------------------
# Automatic certificate issuance and renewal via Let's Encrypt ACME protocol
certmagic:
  enabled: true                 # Enable automatic certificate issuance
  staging_ca: false            # Use production Let's Encrypt (set true for testing)
  http_challenge_addr: ':80'   # Port for HTTP-01 challenge validation
```

### Manual TLS Certificate Configuration

**Generate Self-Signed Certificate (Development):**

```shell
openssl req -x509 -newkey rsa:4096 -sha256 -days 3650 -nodes \
  -keyout uptrace.key -out uptrace.crt -subj "/CN=localhost" \
  -addext "subjectAltName=DNS:localhost,DNS:uptrace.local"
```

**Add to System Trust Store:**

```shell
sudo cp uptrace.crt /usr/local/share/ca-certificates/
sudo update-ca-certificates
```

**Configure Uptrace with Custom Certificates:**

```yml
listen:
  grpc:
    addr: ':4317'
  http:
    addr: ':443'
  tls:
    cert_file: /etc/uptrace/tls/uptrace.crt
    key_file: /etc/uptrace/tls/uptrace.key
    min_version: '1.2'  # Minimum TLS version
    #ca_file: /etc/uptrace/tls/ca.crt  # Custom CA if needed

site:
  url: 'https://uptrace.mycompany.com'
```

### Database TLS Configuration

**Complete TLS Client Options:**

```yml
# PostgreSQL TLS example
pg:
  addr: localhost:5432
  user: uptrace
  password: uptrace
  database: uptrace
  tls:
    # Certificate files (optional for client authentication)
    cert_file: /etc/uptrace/client.crt
    key_file: /etc/uptrace/client.key
    ca_file: /etc/uptrace/ca.crt

    # TLS version constraints
    min_version: '1.2'
    max_version: '1.3'

    # Security settings
    insecure_skip_verify: false  # Verify server certificates
    server_name_override: ''     # Override server name verification
```

**Common TLS Configurations:**

```yml
# Use system certificate store
pg:
  tls: {}

# Skip certificate verification (insecure, testing only)
pg:
  tls:
    insecure_skip_verify: true

# Disable TLS entirely
pg:
  tls:
    insecure: true
```

## User Management and Authentication

### Initial Setup Configuration

Customize default users and organizational structure:

```yml
# -----------------------------------------------------------------------------
# Bootstrap Data
# -----------------------------------------------------------------------------
# Initial data created during first startup - defines default users, organizations, and projects
# This data is only created once and can be modified through the UI afterward
seed_data:
  users:
    - key: admin_user
      name: System Administrator
      email: admin@mycompany.com
      password: ChangeThisPassword123!  # Use strong password
      email_confirmed: true

  user_tokens:
    - key: admin_token
      user: admin_user
      token: secure_admin_token_here    # Generate random token

  orgs:
    - key: main_org
      name: My Company

  org_users:
    - key: admin_org_membership
      org: main_org
      user: admin_user
      role: owner                       # Roles: owner, admin, member

  projects:
    - key: production_project
      name: Production Environment
      org: main_org

  project_tokens:
    - key: prod_token
      project: production_project
      token: prod_telemetry_secret      # Used in OTLP DSN

  project_users:
    - key: admin_project_access
      project: production_project
      user: admin_user
      perm_level: admin                 # Levels: admin, editor, viewer
```

### Authentication Controls

Configure authentication behavior to match your security requirements:

```yml
auth:
  # Disable built-in username/password authentication
  # Useful when using only SSO providers (OAuth, SAML, etc.)
  # Note: SSO authentication methods will remain available
  #disabled: true

  # Disable user registration (sign up)
  # When enabled, new users cannot create accounts
  # Existing users can still sign in normally
  # Use this to restrict access to pre-provisioned users only
  #sign_up_disabled: true

  # Disable user sign in
  # When enabled, users cannot log in to the system
  # Useful for maintenance mode or emergency lockdown scenarios
  #sign_in_disabled: true

  # Email domain restriction for user registration
  # Only users with email addresses matching this regex can register/login
  # Examples:
  # - Single domain: '^.+@mycompany\.com$'
  # - Multiple domains: '^.+@(example|acme)\.com$'
  # - Subdomain wildcard: '^.+@.*\.mycompany\.com$'
  # - Stricter validation: '^[^@]+@example\.com$'
  #email_regexp: '^.+@mycompany\.com$'
```

**Common Authentication Scenarios:**

<table>
<thead>
  <tr>
    <th>
      Scenario
    </th>
    
    <th>
      Configuration
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      SSO-only (disable password auth)
    </td>
    
    <td>
      <code>
        disabled: true
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      No new registrations
    </td>
    
    <td>
      <code>
        sign_up_disabled: true
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Maintenance mode
    </td>
    
    <td>
      <code>
        sign_in_disabled: true
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Restrict to company domain
    </td>
    
    <td>
      <code>
        email_regexp: '^.+@mycompany\.com$'
      </code>
    </td>
  </tr>
</tbody>
</table>

### Single Sign-On Integration

Uptrace supports enterprise identity providers:

- **Okta** - Enterprise SSO platform
- **Keycloak** - Open-source identity management
- **Google Workspace** - Google enterprise accounts

## Data Processing and Performance Tuning

### Telemetry Data Processing Configuration

Optimize processing for different telemetry data types based on your ingestion volume:

```yml
# Spans (distributed tracing data)
# Contains trace information showing request flow across services
spans:
  # Number of parallel processing threads
  # Default: GOMAXPROCS (number of CPU cores)
  # Increase for high-volume tracing workloads
  max_threads: 16

  # Batch size for database insertions
  # Larger batches improve throughput but increase memory usage
  # Tune based on your ingestion rate and memory constraints
  max_insert_size: 20000

  # In-memory buffer capacity for incoming spans
  # Spans are dropped when buffer is full (check metrics for drops)
  # Default scales with max_threads
  max_buffered_records: 200000

# Span links (relationships between spans)
# Used for connecting spans across trace boundaries
span_links:
  # Disable if not using span links to save resources
  disabled: false
  max_threads: 2
  max_insert_size: 5000
  max_buffered_records: 25000

# Application logs
# Structured and unstructured log data from applications
logs:
  max_threads: 12
  max_insert_size: 15000
  max_buffered_records: 150000

# Custom events
# Application-specific events and business metrics
events:
  max_threads: 4
  max_insert_size: 5000
  max_buffered_records: 50000

# Metrics and time series data
# Numerical measurements over time (counters, gauges, histograms)
metrics:
  max_threads: 8
  max_insert_size: 10000
  max_buffered_records: 100000

  # Memory limit for cumulative to delta conversion
  # Affects processing of cumulative counters from OpenTelemetry
  max_cumulative_timeseries: 2000000
```

### Query Performance Limits

Prevent resource exhaustion from expensive queries:

```yml
# Trace query resource limits
trace:
  # Maximum number of spans to return in a single query
  # Prevents UI timeouts and excessive memory usage
  query_limit: 500000

  # Maximum memory usage per query (in bytes)
  # Prevents OOM errors from complex queries
  # Adjust based on available system memory
  max_memory_usage_bytes: 500000000  # 500MB
```

### Caching Configuration

Redis caching improves query performance and reduces database load:

```yml
# -----------------------------------------------------------------------------
# Redis Cache Configuration
# -----------------------------------------------------------------------------
# In-memory cache for improved query performance and session storage
# Reduces database load and improves response times
redis_cache:
  # Redis Ring server addresses
  addrs:
    alpha: redis-1:6379
    bravo: redis-2:6379

  # Authentication
  username: ''
  password: 'redis_password'
  db: 0

  # Connection settings
  dial_timeout: 5s
  read_timeout: 3s
  write_timeout: 3s

  # TLS for secure connections
  #tls:
  #  insecure_skip_verify: false
```

## Feature Management

### Optional Feature Modules

Enable or disable features based on your needs:

```yml
# Monitoring and alerting system
# Provides proactive monitoring with notifications
alerting:
  # Uncomment to disable the entire alerting system
  # This saves resources if you don't use monitoring alerts
  #disabled: true

# Service dependency graph generation
# Automatically builds service topology from trace data
service_graph:
  # Uncomment to disable service graph processing
  # This saves CPU and memory if you don't use the service map
  #disabled: true

# JavaScript error sourcemap processing
# Provides better error stack traces for frontend applications
# Requires internet access to download source maps from URLs
sourcemaps:
  # Uncomment to disable sourcemap processing
  # Disable in air-gapped environments or if not using JS error tracking
  #disabled: true

# Internal telemetry collection
# Uptrace monitors itself and sends telemetry to the configured DSN
self_monitoring:
  # Disable self-monitoring to prevent internal telemetry data
  disabled: false
  # DSN for sending Uptrace's own telemetry
  dsn: http://project1_secret@uptrace.local/2?grpc=4317
```

## Notification and Communication

### Email Configuration

Configure SMTP for alert notifications and user management:

```yml
# SMTP configuration for alert notifications and user management emails
# Required for: password resets, alert notifications, user invitations
# Documentation: https://uptrace.dev/features/alerting
mailer:
  smtp:
    enabled: false                # Enable email notifications
    host: localhost               # SMTP server hostname
    port: 1025                    # SMTP server port (25, 465, 587, 1025)
    username: mailhog             # SMTP authentication username
    password: mailhog             # SMTP authentication password
    from: no-reply@uptrace.local  # Sender email address (must be authorized)

    # TLS configuration
    # Most production SMTP servers require TLS
    #tls: { insecure: true }     # Uncomment to disable opportunistic TLS
```

**Gmail Configuration Example:**

1. Generate app-specific password in Gmail settings
2. Configure Uptrace:

```yml
mailer:
  smtp:
    enabled: true
    host: smtp.gmail.com
    port: 587
    username: youraccount@gmail.com
    password: your_app_specific_password  # Not your regular password
    from: 'youraccount@gmail.com'
```

### Telegram Integration

Enable Telegram notifications for alerts:

```yml
##
## Telegram bot configuration
## Setup guide: https://core.telegram.org/bots#6-botfather
##
telegram:
  # Bot token from @BotFather
  bot_token: 'your_telegram_bot_token'
```

## System Configuration

### Application Logging

Control Uptrace's internal logging:

```yml
##
## Application logging configuration
##
logging:
  # Log levels: DEBUG, INFO, WARN, ERROR
  # DEBUG: Verbose output for troubleshooting
  # INFO: Standard operational information
  # WARN: Warnings and errors only
  # ERROR: Errors only
  level: INFO
```

### Premium Features

Enable advanced features with a license:

```yml
##
## Premium Edition license
## Enables: distributed tables, advanced SSO, priority support
##
license:
  key: 'your_premium_license_key'
```

**Premium Features Include:**

- ClickHouse distributed tables for horizontal scaling
- Advanced SSO integrations
- Priority technical support
- Enhanced security features

## Deployment Patterns

### Production Checklist

**Security Requirements:**

- â Change all default passwords and tokens in `seed_data`
- â Configure TLS/SSL certificates for all connections
- â Set up authentication restrictions (`auth.email_regexp`)
- â Enable secure database connections
- â Configure proper firewall rules

**High Availability Setup:**

- â Deploy multiple Uptrace instances behind load balancer
- â Configure PostgreSQL with read replicas
- â Set up ClickHouse replication (minimum 3 nodes)
- â Configure Redis for caching and session storage
- â Set up database backup procedures

**Performance Optimization:**

- â Tune telemetry processing settings based on volume
- â Configure appropriate resource limits
- â Set up monitoring for Uptrace itself
- â Configure data retention policies
- â Optimize ClickHouse storage policies

**Operational Requirements:**

- â Configure email notifications for alerts
- â Set up log aggregation for Uptrace logs
- â Document recovery procedures
- â Configure backup verification
- â Set up monitoring dashboards

### Reverse Proxy Configuration

When deploying behind a reverse proxy, ensure proper URL configuration:

```yml
site:
  # Main deployment
  url: https://uptrace.mycompany.com

  # Subpath deployment
  url: https://mycompany.com/uptrace
```

**Subpath Deployment Path Rewriting:**

When deploying Uptrace under a subpath (e.g., `/uptrace`), the reverse proxy must strip the subpath prefix before forwarding requests to Uptrace. The path `/uptrace(/|$)(.*)` needs to be rewritten to `/$2`.

<code-group>

```nginx [Nginx]
location ~ ^/uptrace(/|$) {
    rewrite ^/uptrace$ / break;
    rewrite ^/uptrace(/.*)$ $1 break;
    proxy_pass http://uptrace:14318;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

```haproxy [HAProxy]
frontend http_front
    bind *:80
    acl is_uptrace path_beg /uptrace
    use_backend uptrace_backend if is_uptrace

backend uptrace_backend
    http-request replace-path /uptrace(/|$)(.*) /\2
    http-request set-header X-Forwarded-Proto https
    http-request set-header X-Forwarded-For %[src]
    server uptrace uptrace:14318 check
```

```yaml [Traefik]
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.uptrace.rule=PathPrefix(`/uptrace`)"
  - "traefik.http.routers.uptrace.middlewares=uptrace-strip"
  - "traefik.http.middlewares.uptrace-strip.stripprefix.prefixes=/uptrace"
  - "traefik.http.services.uptrace.loadbalancer.server.port=14318"
```

</code-group>

**Load Balancer Health Checks:**

- HTTP endpoint: `GET /api/health`
- Expected response: `200 OK`

### Scaling Guidelines

**Horizontal Scaling:**

- Uptrace instances are stateless and can be scaled horizontally
- Use load balancer to distribute traffic across instances
- Each instance should connect to the same PostgreSQL and ClickHouse databases

**Vertical Scaling Recommendations:**<br />


According to [ClickHouse documentation](https://clickhouse.com/blog/common-getting-started-issues-with-clickhouse#2-going-horizontal-too-early), prefer vertical scaling over horizontal scaling:

> Successful deployments with ClickHouse use servers with hundreds of cores, terabytes of RAM, and petabytes of disk space. Scaling vertically first provides cost efficiency, lower operational overhead, and better query performance.

**Resource Requirements:**

- **Uptrace instances:** 2-4 CPU cores, 4-8GB RAM per instance
- **PostgreSQL:** 2-4 CPU cores, 4-8GB RAM, SSD storage
- **ClickHouse:** Scale based on data volume (prefer large instances)
- **Redis:** 1-2 CPU cores, 2-4GB RAM
