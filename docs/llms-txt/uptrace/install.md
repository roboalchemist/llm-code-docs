# Source: https://uptrace.dev/raw/get/hosted/install.md

# Installing Uptrace

> Install self hosted Uptrace by provisioning ClickHouse, PostgreSQL, and Redis, generating config files, and wiring telemetry sources.

To install Uptrace on your computer, you need to:

1. Create a [ClickHouse](#clickhouse) database to store telemetry data.
2. Create a [PostgreSQL](#postgresql) database to store users and projects.
3. Install [Redis](#redis) database for caching.
4. [Install](#installation) the Uptrace binary.
5. [Set up the databases](#database-setup) by running migrations and seeding data.
6. [Start sending data](#start-sending-data) using the OpenTelemetry protocol.
7. Enjoy! ð

Instead of installing everything manually, you can also try the following deployment methods:

- [Docker](/get/hosted/docker) can get you started quickly with all dependencies pre-configured.
- [Ansible playbook](/get/hosted/ansible) is ideal for installing Uptrace on bare metal servers.
- [Kubernetes Helm chart](/get/hosted/k8s) works best if you already have a Kubernetes cluster.

## Hardware Requirements

<table>
<thead>
  <tr>
    <th>
      Spans and Logs
    </th>
    
    <th>
      Time Series
    </th>
    
    <th>
      Hardware Requirements
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      30 TB
    </td>
    
    <td>
      2 million
    </td>
    
    <td>
      24 vCPU, 48GB RAM, 1TB SSD, 6TB HDD
    </td>
  </tr>
  
  <tr>
    <td>
      50 TB
    </td>
    
    <td>
      3 million
    </td>
    
    <td>
      32 vCPU, 96GB RAM, 2TB SSD, 12TB HDD
    </td>
  </tr>
  
  <tr>
    <td>
      100 TB
    </td>
    
    <td>
      6 million
    </td>
    
    <td>
      64 vCPU, 160GB RAM, 4TB SSD, 20TB HDD
    </td>
  </tr>
  
  <tr>
    <td>
      500 TB
    </td>
    
    <td>
      30 million
    </td>
    
    <td>
      192 vCPU, 576GB RAM, 8TB SSD, 100TB HDD
    </td>
  </tr>
</tbody>
</table>

## Configuration

All Uptrace configuration is done with a single YAML file that can be created using the Uptrace binary:

```shell
uptrace --config=/path/to/config.yml config create
```

You can then specify the config file location when starting Uptrace:

```shell
uptrace --config=/path/to/config.yml serve
```

See [Configuration](/get/hosted/config) for more details.

## ClickHouse

Uptrace requires a ClickHouse database to store telemetry data such as traces, logs, and metrics. ClickHouse is an open-source columnar database management system designed to handle large amounts of data and execute complex analytical queries with low latency.

After [installing](https://clickhouse.com/docs/en/getting-started/install/) ClickHouse, you can create the `uptrace` database like this:

```shell
clickhouse-client -q "CREATE DATABASE uptrace"
```

On startup, Uptrace connects to the ClickHouse database specified in the `uptrace.yml` configuration file and automatically creates the required tables and views.

```yml
# uptrace.yml

ch_cluster:
  shards:
    - replicas:
        - addr: localhost:9000
          user: default
          password:
          database: uptrace
```

## PostgreSQL

Uptrace also requires a PostgreSQL database to store metadata such as metric names and alerts. Typically, the PostgreSQL database requires only a few megabytes of disk space.

After installing PostgreSQL, you can create the database like this:

```shell
sudo -u postgres psql
postgres=# CREATE DATABASE uptrace;
postgres=# CREATE USER uptrace WITH ENCRYPTED PASSWORD 'uptrace';
postgres=# GRANT ALL PRIVILEGES ON DATABASE uptrace TO uptrace;
postgres=# \c uptrace
postgres=# GRANT ALL ON SCHEMA public TO uptrace;
```

On startup, Uptrace connects to the PostgreSQL database specified in the `uptrace.yml` configuration file and automatically creates the required tables and views.

```yml
# uptrace.yml

pg:
  addr: localhost:5432
  user: uptrace
  password: uptrace
  database: uptrace
```

## Redis

Uptrace requires Redis for caching query results and session management. Redis is a mandatory dependency that significantly improves query performance and reduces database load.

After installing Redis, you must configure Uptrace to connect to it by adding the following to your `uptrace.yml` configuration file:

```yml
# uptrace.yml

redis_cache:
  # Redis Ring server addresses
  addrs:
    alpha: redis-1:6379
    bravo: redis-2:6379

  # Authentication (if required)
  username: ''
  password: 'your_redis_password'
  db: 0

  # Connection timeouts
  dial_timeout: 5s
  read_timeout: 3s
  write_timeout: 3s
```

## Installation

### Packages

Uptrace provides [DEB](#deb) and [RPM](#rpm) packages for Linux amd64/arm64 systems. After installing the appropriate package, you will have:

- Uptrace binary at `/usr/bin/uptrace`
- Uptrace config at `/etc/uptrace/config.yml`
- Systemd service at `/lib/systemd/system/uptrace.service`
- Environment file used by the systemd service at `/etc/uptrace/uptrace.conf`

To check the status of the Uptrace service:

```shell
sudo systemctl status uptrace
```

To restart Uptrace:

```shell
sudo systemctl restart uptrace
```

To view Uptrace logs:

```shell
sudo journalctl -u uptrace -f
```

#### DEB

To install the Debian package, run the following command, replacing `2.0.0` with the desired version and `amd64` with the desired architecture:

```shell
wget https://github.com/uptrace/uptrace/releases/download/v2.0.0/uptrace_2.0.0_amd64.deb
sudo dpkg -i uptrace_2.0.0_amd64.deb
```

#### RPM

To install the RPM package, run the following command, replacing `2.0.0` with the desired version and `x86_64` with the desired architecture:

```shell
wget https://github.com/uptrace/uptrace/releases/download/v2.0.0/uptrace-2.0.0-1.x86_64.rpm
sudo rpm -ivh uptrace-2.0.0-1.x86_64.rpm
```

### Binaries

Alternatively, instead of installing [DEB](#deb) or [RPM](#rpm) packages, you can [download](https://github.com/uptrace/uptrace/releases) a pre-compiled binary and install Uptrace manually.

- [Linux](#linux)
- [macOS](#macos)
- [Windows](#windows)

#### Linux

Download the Linux binary:

```shell
wget -O ./uptrace https://github.com/uptrace/uptrace/releases/download/v2.0.0/uptrace_linux_amd64
chmod +x ./uptrace
```

Create the Uptrace config:

```shell
./uptrace --config=/path/to/config.yml config create
```

Start Uptrace:

```shell
./uptrace --config=/path/to/config.yml serve
```

#### macOS

Download the macOS binary:

```shell
wget -O uptrace https://github.com/uptrace/uptrace/releases/download/v2.0.0/uptrace_darwin_amd64
chmod +x uptrace
```

Create the Uptrace config:

```shell
./uptrace --config=/path/to/config.yml config create
```

Start Uptrace:

```shell
./uptrace --config=/path/to/config.yml serve
```

#### Windows

Download the Windows binary:

```shell
curl -O uptrace_windows_amd64.exe https://github.com/uptrace/uptrace/releases/download/v2.0.0/uptrace_windows_amd64.exe
```

Create the Uptrace config:

```shell
uptrace_windows_amd64.exe --config=/path/to/config.yml config create
```

Start Uptrace:

```shell
uptrace_windows_amd64.exe --config=/path/to/config.yml serve
```

#### Other

For pre-compiled binaries for other platforms, check [GitHub Releases](https://github.com/uptrace/uptrace/releases).

## Database Setup

After installing Uptrace and creating the databases, you need to initialize the database schemas and seed them with data from your config file.

### PostgreSQL

Initialize the PostgreSQL database (only required once during the first setup):

```shell
uptrace --config=/etc/uptrace/config.yml pg init
```

Run PostgreSQL migrations to create or update the schema:

```shell
uptrace --config=/etc/uptrace/config.yml pg migrate
```

### ClickHouse

Initialize the ClickHouse database (only required once during the first setup):

```shell
uptrace --config=/etc/uptrace/config.yml ch init
```

Run ClickHouse migrations to create or update the schema:

```shell
uptrace --config=/etc/uptrace/config.yml ch migrate
```

Create ClickHouse distributed tables (required for clustered setups):

```shell
uptrace --config=/etc/uptrace/config.yml ch dist
```

### Seed Data

Seed the database with initial data from your config file, such as projects and users. Re-run this command whenever you change the seed data in your config:

```shell
uptrace --config=/etc/uptrace/config.yml db seed
```

## Start Sending Data

To start sending data, you can use OpenTelemetry distributions that are pre-configured to work with Uptrace. Uptrace uses the OpenTelemetry protocol (OTLP) to receive telemetry data such as [traces](/opentelemetry/distributed-tracing#spans), [metrics](/opentelemetry/metrics), and [logs](/opentelemetry/logs). As a transport protocol, OTLP can use gRPC (**OTLP/gRPC**) or HTTP (**OTLP/HTTP**).

Uptrace supports OTLP/gRPC on port `4317` and OTLP/HTTP on port `4318`. Both ports are specified in the Uptrace DSN that you will receive after installing Uptrace.

<home-distro-list>



</home-distro-list>

## Upgrading Uptrace

Only upgrades to the next minor version are tested and supported, for example, upgrading from 1.1 to 1.2. Skipping minor versions (e.g., 1.1 to 1.3) is not supported â upgrade one minor version at a time.

To upgrade Uptrace:

1. **Back up your databases.** Create backups of both PostgreSQL and ClickHouse before proceeding.
2. **Install the new version.** Download and install the new Uptrace binary using [DEB](#deb), [RPM](#rpm), or a [pre-compiled binary](#binaries).
3. **Validate your config** to ensure it is compatible with the new version:```shell
uptrace config validate
```
4. **Run database migrations** to apply schema changes:```shell
uptrace pg migrate
uptrace ch migrate
```
5. **Restart Uptrace:**```shell
sudo systemctl restart uptrace
```

## What's Next?

Next, learn how to [configure](/get/hosted/config) Uptrace for your needs.
