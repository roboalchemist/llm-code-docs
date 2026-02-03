# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-db-modify.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible db:modify

This command modifies existing [Databases](/core-concepts/managed-databases/managing-databases/overview). Running this command does not cause downtime.

# Synopsis

```
Usage:
  aptible db:modify HANDLE [--iops IOPS] [--volume-type [gp2, gp3]]

Options:
  --env, [--environment=ENVIRONMENT]
  [--iops=N]
  [--volume-type=VOLUME_TYPE]

```

> 📘 The IOPS option only applies to GP3 volume.  If you currently have a GP2 volume and need more IOPS, simultaneously specify both the `--volume-type gp3` and `--iops NNNN` options.

> 📘 The maximum IOPS is 16,000, but you must meet a minimum ratio of 1 GB disk size per 500 IOPS.  For example, to reach 16,000 IOPS, you must have at least a 32 GB or larger disk.
