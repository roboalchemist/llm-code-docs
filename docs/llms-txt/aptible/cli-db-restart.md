# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-db-restart.md

# aptible db:restart

This command restarts a [Database](/core-concepts/managed-databases/overview) and can be used to resize a Database.

<Tip> If you want to restart your Database in place without resizing it, consider using [`aptible db:reload`](/reference/aptible-cli/cli-commands/cli-db-reload) instead. [`aptible db:reload`](/reference/aptible-cli/cli-commands/cli-db-reload) is slightly faster than [`aptible db:restart`](/reference/aptible-cli/cli-commands/cli-db-restart).</Tip>

# Synopsis

```
Usage:
  aptible db:restart HANDLE [--container-size SIZE_MB] [--container-profile PROFILE]  [--disk-size SIZE_GB] [--iops IOPS] [--volume-type [gp2, gp3]]

Options:
  --env, [--environment=ENVIRONMENT]
  [--container-size=N]
  [--container-profile PROFILE]
                               # Default: m
  [--disk-size=N]
  [--size=N]
  [--iops=N]
  [--volume-type=VOLUME_TYPE]
```

# Examples

#### Resize the Container

```shell  theme={null}
aptible db:restart "$DB_HANDLE" \
        --container-size 2048
```

#### Resize the Disk

```shell  theme={null}
aptible db:restart "$DB_HANDLE" \
        --disk-size 120
```

#### Resize Container and Disk

```shell  theme={null}
aptible db:restart "$DB_HANDLE" \
        --container-size 2048 \
        --disk-size 120
```

#### Container Sizes (MB)

**All container profiles** support the following sizes: 512, 1024, 2048, 4096, 7168, 15360, 30720

The following profiles offer additional supported sizes:

* **General Purpose (M) - Legacy, General Purpose(M) and Memory Optimized(R)** - **Legacy**: 61440, 153600, 245760
* **Compute Optimized (C)**: 61440, 153600, 245760, 376832
* **Memory Optimized (R)**: 61440, 153600, 245760, 376832, 507904, 770048

#### Profiles

`m`: General purpose container \
`c`: Compute-optimized container \
`r`: Memory-optimized container
