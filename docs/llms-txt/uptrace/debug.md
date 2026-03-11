# Source: https://uptrace.dev/raw/get/hosted/debug.md

# Troubleshooting

> Troubleshoot self hosted Uptrace by checking versions, reading service logs, and enabling verbose ClickHouse or Redis diagnostics.

## Uptrace version

Before trying anything else, make sure you have the latest Uptrace version.

To see the installed Uptrace version:

```shell
uptrace version
```

You can check the latest available version at [GitHub Releases](https://github.com/uptrace/uptrace/releases).

## Uptrace logs

You can view Uptrace logs using `journalctl` command:

```shell
sudo journalctl -u uptrace -f
```

To check the status of the service:

```shell
sudo systemctl status uptrace
```

By default, Uptrace only logs failed HTTP requests and failed ClickHouse queries. You can configure Uptrace to log all incoming HTTP requests with an env variable:

```shell
HTTPDEBUG=2 uptrace serve
```

To log all ClickHouse queries:

```shell
CHDEBUG=2 uptrace serve
```

To log all PostgreSQL queries:

```shell
PGDEBUG=2 uptrace serve
```

## Database logs

To view ClickHouse logs:

```shell
sudo tail -f /var/log/clickhouse-server/clickhouse-server.err.log -n 100
```

To view PostgreSQL logs:

```shell
sudo tail -f /var/log/postgresql/postgresql-17-main.log
```

## Resetting ClickHouse database

If ClickHouse queries are failing, you can try to to reset ClickHouse database:

```shell
uptrace ch reset
```

The check the database status:

```shell
uptrace ch status
```

## Resetting PostgreSQL database

Just like with ClickHouse, you can reset the PostgreSQL database that Uptrace uses to store metadata:

```shell
uptrace pg reset
```

The check the database status:

```shell
uptrace pg status
```

## Common Configuration Issues

**Database Connection Problems:**

```yml
# Check connection settings
pg:
  addr: localhost:5432  # Verify host and port
  user: uptrace         # Ensure user exists
  password: uptrace     # Verify password
  database: uptrace     # Ensure database exists
```

**TLS Certificate Issues:**

```bash
# Verify certificate validity
openssl x509 -in uptrace.crt -text -noout

# Check certificate expiration
openssl x509 -in uptrace.crt -checkend 86400

# Test TLS connection
openssl s_client -connect uptrace.local:443
```

**Performance Problems:**

- Monitor ClickHouse resource usage
- Check for dropped telemetry data in metrics
- Review query performance in ClickHouse logs
- Verify network latency between components

**Authentication Issues:**

- Verify email regex patterns if configured
- Check SSO provider configuration
- Confirm user permissions and project access
- Review authentication logs for error details

## Monitoring Uptrace Health

**Key Metrics to Monitor:**

- Database connection health
- Telemetry data ingestion rates
- Query response times
- Memory and CPU usage
- Disk space utilization

**Health Check Endpoints:**

- API health: `GET /api/health`
- Database connectivity: Monitor connection metrics
- Redis connectivity: Monitor cache hit rates
