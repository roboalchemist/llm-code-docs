# Source: https://www.aptible.com/docs/how-to-guides/platform-guides/deprovision-resources.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to deprovision resources

First, review the [resource-specific restoration options](/how-to-guides/platform-guides/restore-resources) to understand the impact of deprovisioning each type of resource and make any necessary preparations, such as exporting Database data, before proceeding.

## Apps

Deprovisioning an App also deprovisions its [Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/overview). [Apps](/core-concepts/apps/overview) can be deprovisioned using the [`aptible apps:deprovision`](/reference/aptible-cli/cli-commands/cli-apps-deprovision) CLI command or through the Dashboard:

* Select the App

* Select the **Deprovision** tab

* Follow the prompt

## Database Backups

Automated [Backups](/core-concepts/managed-databases/managing-databases/database-backups) are deleted per the Environment's [backup retention policy](/core-concepts/managed-databases/managing-databases/database-backups#retention-and-disposal) when the Database is deprovisioned. Manual backups, created using the [`aptible db:backup`](/reference/aptible-cli/cli-commands/cli-db-backup) CLI command, must be deleted using the [`aptible backup:purge`](/reference/aptible-cli/cli-commands/cli-backup-purge) CLI command or through the Dashboard:

* Select the **Backup Management** tab within the desired Environment.

* Select "**Permanently remove this backup**" for backups marked as Manual.

## Databases

[Databases](/core-concepts/managed-databases/managing-databases/overview) can be deprovisioned using the [`aptible db:deprovision`](/reference/aptible-cli/cli-commands/cli-db-deprovision) CLI command or through the Dashboard:

* Select the desired Database.

* Select the **Deprovision** tab.

* Follow the prompt.

## Log and Metric Drains

Delete Log and Metric Drains in the Dashboard:

* Select the Log Drains or Metric Drains tabs within each Environment.

* Select **Delete** on the top right of each drain.

## Environments

[Environments](/core-concepts/architecture/environments) can only be deprovisioned after all of the resources in the Environment have been deprovisioned. Environments can only be deprovisioned through the Dashboard:

* Select the **Deprovision** tab within the Environment.

* Follow the prompt.
