# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-db-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible db:create

This command creates a new [Database](/core-concepts/managed-databases/overview) using the General Purpose container profile by default. The container profile can only be modified in the Aptible dashboard.

# Synopsis

```
Usage:
  aptible db:create HANDLE [--type TYPE] [--version VERSION] [--container-size SIZE_MB] [--container-profile PROFILE] [--disk-size SIZE_GB] [--iops IOPS] [--key-arn KEY_ARN]

Options:
  [--type=TYPE]
  [--version=VERSION]
  [--container-size=N]
  [--container-profile PROFILE]
                               # Default: m
  [--disk-size=N]
                               # Default: 10
  [--size=N]
  [--key-arn=KEY_ARN]
  [--iops=IOPS]
  --env, [--environment=ENVIRONMENT]
```

# Examples

#### Create a new Database using a specific type

You can specify the type using the `--type` option. This parameter defaults to `postgresql`, but you can use any of Aptible's [Supported Databases](/core-concepts/managed-databases/supported-databases/overview).

For example, to create a [Redis](/core-concepts/managed-databases/supported-databases/redis) database:

```shell  theme={null}
aptible db:create --type redis
```

#### Create a new Database using a specific version

Use the `--version` flag in combination with `--type` to use a specific version:

```shell  theme={null}
aptible db:create --type postgresql --version 9.6
```

> 📘 Use the [`aptible db:versions`](/reference/aptible-cli/cli-commands/cli-db-versions) command to identify available versions.

#### Create a new Database with a custom Disk Size

```shell  theme={null}
aptible db:create --disk-size 20 "$DB_HANDLE"
```

#### Create a new Database with a custom Container Size

```shell  theme={null}
aptible db:create --container-size 2048 "$DB_HANDLE"
```

#### Container Sizes (MB)

**General Purpose(M)**: 512, 1024, 2048, 4096, 7168, 15360, 30720, 61440, 153600, 245760

#### Profiles

`m`: General purpose container \
`c`: Compute-optimized container \
`r`: Memory-optimized container
