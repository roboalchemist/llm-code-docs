# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-services-settings.md

# aptible services:settings

This command lets you configure [Services](/core-concepts/apps/deploying-apps/services) for a given [App](/core-concepts/apps/overview).

# Synopsis

```
Usage:
  aptible services:settings [--app APP] SERVICE [--force-zero-downtime|--no-force-zero-downtime] [--simple-health-check|--no-simple-health-check] [--stop-timeout SECONDS]

Options:
      [--app=APP]
  --env, [--environment=ENVIRONMENT]
  -r, [--remote=REMOTE]
      [--force-zero-downtime|--no-force-zero-downtime]
      [--simple-health-check|--no-simple-health-check]
      [--stop-timeout=SECONDS]
```

# Examples

```shell  theme={null}
aptible services:settings --app "$APP_HANDLE" SERVICE \
        --force-zero-downtime \
        --simple-health-check
```

```shell  theme={null}
aptible services:settings --app "$APP_HANDLE" SERVICE \
        --stop-timeout 60
```

#### Force Zero Downtime

For Services without endpoints, you can force a zero downtime deployment strategy, which enables healthchecks via Docker's healthcheck mechanism.

#### Simple Health Check

When enabled, instead of using Docker healthchecks, Aptible will ensure your container can stay up for 30 seconds before continuing the deployment.
