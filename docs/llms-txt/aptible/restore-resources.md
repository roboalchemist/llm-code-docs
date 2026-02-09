# Source: https://www.aptible.com/docs/how-to-guides/platform-guides/restore-resources.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Recover Deleted Resources

## Apps

It is not possible to restore an App, its [Configuration](/core-concepts/apps/deploying-apps/configuration), or its [Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/overview) once deprovisioned. Instead, deploy a new App using the same [Image](/core-concepts/apps/deploying-apps/image/overview) and manually recreate the App's Configuration and any Endpoints.

## Database Backups

It is not possible to restore Database Backups once deleted. Aptible permanently deletes database backups when an account is closed. Users must export all essential data in Aptible before the account is closed.

## Databases

It is not possible to restore a Database, its [Endpoints](/core-concepts/managed-databases/connecting-databases/database-endpoints) or its [Replicas](/core-concepts/managed-databases/managing-databases/replication-clustering) once deprovisioned. Instead, create a new Database using the backed-up data from Database Backups via the [`aptible backup:restore`](/reference/aptible-cli/cli-commands/cli-backup-restore) CLI command or through the Dashboard:

* Select the Backup Management tab within the desired environment.

* Select "Restore to a New Database" for the relevant backup.

Then, recreate any Database Endpoints and Replicas. Restoring a Backup creates a new Database from the backed-up data. It does not replace or modify the Database the Backup was originally created from in any way. The new Database will have the same data, username, and password as the original did at the time the Backup was taken.

## Log and Metric Drains

Once deleted, it is not possible to restore log and metric drains. Create new drains instead.

## Environments

Once deleted, it is not possible to restore Environments.
