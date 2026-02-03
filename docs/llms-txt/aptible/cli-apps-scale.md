# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-apps-scale.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible apps:scale

This command [scales](/core-concepts/scaling/overview) App [Services](/core-concepts/apps/deploying-apps/services) up or down.

# Synopsis

```
Usage:
  aptible apps:scale [--app APP] SERVICE [--container-count COUNT] [--container-size SIZE_MB] [--container-profile PROFILE]

Options:
      [--app=APP]
  --env, [--environment=ENVIRONMENT]
  -r, [--remote=REMOTE]
      [--container-count=N]
      [--container-size=N]
      [--container-profile=PROFILE]
```

# Examples

```shell  theme={null}
# Scale a service up or down
aptible apps:scale --app "$APP_HANDLE" SERVICE \
        --container-count COUNT \
        --container-size SIZE_MB

# Restart a service by scaling to its current count
aptible apps:scale --app "$APP_HANDLE" SERVICE \
        --container-count CURRENT_COUNT
```

#### Container Sizes (MB)

**All container profiles** support the following sizes: 512, 1024, 2048, 4096, 7168, 15360, 30720

The following profiles offer additional supported sizes:

* **General Purpose (M) - Legacy, General Purpose(M) and Memory Optimized(R)** - **Legacy**: 61440, 153600, 245760
* **Compute Optimized (C)**: 61440, 153600, 245760, 376832
* **Memory Optimized (R)**: 61440, 153600, 245760, 376832, 507904, 770048
