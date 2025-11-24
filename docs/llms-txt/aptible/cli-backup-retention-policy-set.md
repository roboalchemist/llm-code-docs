# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-backup-retention-policy-set.md

# aptible backup_retention_policy:set

This command changes the
[backup retention policy](/core-concepts/managed-databases/managing-databases/database-backups#automatic-backups)
for an [Environment](/core-concepts/architecture/environments). Only the
specified attributes will be changed. The rest will reuse the current value.

# Synopsis

```
Usage:
  aptible backup_retention_policy:set [ENVIRONMENT_HANDLE] [--daily DAILY_BACKUPS] [--monthly MONTHLY_BACKUPS] [--yearly YEARLY_BACKUPS] [--make-copy|--no-make-copy] [--keep-final|--no-keep-final] [--force]

Options:
  [--daily=N]                        # Number of daily backups to retain
  [--monthly=N]                      # Number of monthly backups to retain
  [--yearly=N]                       # Number of yearly backups to retain
  [--make-copy], [--no-make-copy]    # If backup copies should be created
  [--keep-final], [--no-keep-final]  # If final backups should be kept when databases are deprovisioned
  [--force]                          # Do not prompt for confirmation if the new policy retains fewer backups than the current policy

Change the environment's backup retention policy
```
