# Source: https://docs.infrahub.app/reference/configuration.md

# Source: https://docs.infrahub.app/exporter/guides/configuration.md

# Source: https://docs.infrahub.app/emma/reference/configuration.md

# Source: https://docs.infrahub.app/emma/getting-started/configuration.md

# Source: https://docs.infrahub.app/backup/reference/configuration.md

# Configuration reference

Complete reference for configuring Infrahub Backup through environment variables and runtime flags.

## Configuration methods[​](#configuration-methods "Direct link to Configuration methods")

Tools can be configured through these methods, applied in precedence order:

1. **Command-line flags** (highest priority)
2. **Environment variables**
3. **Default values** (lowest priority)

## Environment variables[​](#environment-variables "Direct link to Environment variables")

### Core configuration[​](#core-configuration "Direct link to Core configuration")

| Variable              | Description                        | Default              | Example         |
| --------------------- | ---------------------------------- | -------------------- | --------------- |
| `INFRAHUB_BACKUP_DIR` | Directory for storing backup files | `./infrahub_backups` | `/data/backups` |
| `INFRAHUB_LOG_FORMAT` | Output format for logs             | `text`               | `json`          |

### Docker compose configuration[​](#docker-compose-configuration "Direct link to Docker compose configuration")

| Variable           | Description                 | Default     | Example         |
| ------------------ | --------------------------- | ----------- | --------------- |
| `INFRAHUB_PROJECT` | Docker Compose project name | Auto-detect | `infrahub-prod` |

### Database configuration[​](#database-configuration "Direct link to Database configuration")

#### Neo4j[​](#neo4j "Direct link to Neo4j")

| Variable               | Description         | Default | Example         |
| ---------------------- | ------------------- | ------- | --------------- |
| `INFRAHUB_DB_DATABASE` | Neo4j database name | `neo4j` | `infrahub`      |
| `INFRAHUB_DB_USERNAME` | Neo4j username      | `neo4j` | `admin`         |
| `INFRAHUB_DB_PASSWORD` | Neo4j password      | `admin` | `SecurePass123` |

#### Task manager PostgreSQL[​](#task-manager-postgresql "Direct link to Task manager PostgreSQL")

| Variable                              | Description                  | Default     | Example                                    |
| ------------------------------------- | ---------------------------- | ----------- | ------------------------------------------ |
| `PREFECT_API_DATABASE_CONNECTION_URL` | PostgreSQL connection string | Auto-detect | `postgresql://user:pass@localhost/prefect` |

## Command-line flag reference[​](#command-line-flag-reference "Direct link to Command-line flag reference")

### Global flags[​](#global-flags "Direct link to Global flags")

| Flag           | Environment Override  | Description                            |
| -------------- | --------------------- | -------------------------------------- |
| `--backup-dir` | `INFRAHUB_BACKUP_DIR` | Set backup directory                   |
| `--project`    | `INFRAHUB_PROJECT`    | Target specific Docker Compose project |
| `--log-format` | `INFRAHUB_LOG_FORMAT` | Set log output format                  |

### Backup command flags[​](#backup-command-flags "Direct link to Backup command flags")

| Flag              | Description                                         |
| ----------------- | --------------------------------------------------- |
| `--force`         | Force backup creation even if tasks are running     |
| `--neo4jmetadata` | Neo4j metadata to include (all, none, users, roles) |

## Auto-detection behavior[​](#auto-detection-behavior "Direct link to Auto-detection behavior")

### Docker Compose project detection[​](#docker-compose-project-detection "Direct link to Docker Compose project detection")

Order of detection:

1. `--project` flag
2. `INFRAHUB_PROJECT` environment variable
3. Search for running Infrahub containers

Detection command:

```
docker compose ls --filter "name=*infrahub*"
```

### Database credential detection[​](#database-credential-detection "Direct link to Database credential detection")

For Docker Compose deployments:

```
# Neo4j credentials from environment
docker compose exec database printenv NEO4J_AUTH

# PostgreSQL credentials from environment
docker compose exec task-manager-db printenv POSTGRES_PASSWORD
```

## Troubleshooting configuration[​](#troubleshooting-configuration "Direct link to Troubleshooting configuration")

### Debug configuration loading[​](#debug-configuration-loading "Direct link to Debug configuration loading")

View effective configuration:

```
infrahub-backup --help
```

### Test configuration[​](#test-configuration "Direct link to Test configuration")

Validate configuration without running operations:

```
infrahub-backup environment detect
```

### Common issues[​](#common-issues "Direct link to Common issues")

#### Cannot detect environment[​](#cannot-detect-environment "Direct link to Cannot detect environment")

```
# Check Docker
docker compose ls
docker ps

# Check for Infrahub containers
docker ps --filter "name=infrahub"
```

#### Authentication failures[​](#authentication-failures "Direct link to Authentication failures")

```
# Verify credentials are set
env | grep INFRAHUB
env | grep PREFECT

# Test database connectivity
docker compose exec database cypher-shell -u neo4j
```

## Examples[​](#examples "Direct link to Examples")

### Minimal configuration[​](#minimal-configuration "Direct link to Minimal configuration")

For basic Docker Compose setup:

```
export INFRAHUB_BACKUP_DIR=/backups
infrahub-backup create
```

### Production configuration[​](#production-configuration "Direct link to Production configuration")

```
#!/bin/bash
# production-backup.sh

export INFRAHUB_LOG_FORMAT=json
export INFRAHUB_PROJECT=infrahub-production
export INFRAHUB_BACKUP_DIR=/data/backups/infrahub
export INFRAHUB_DB_PASSWORD="${NEO4J_PASSWORD}"

infrahub-backup create --neo4jmetadata=all
```

## Related documentation[​](#related-documentation "Direct link to Related documentation")

* [CLI command reference](/backup/reference/commands.md)
* [How to install](/backup/guides/install.md)
