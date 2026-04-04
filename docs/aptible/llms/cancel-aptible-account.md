# Source: https://www.aptible.com/docs/how-to-guides/platform-guides/cancel-aptible-account.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to cancel my Aptible Account

> To cancel your Deploy account and avoid any future charges, please follow these steps in order.

<Warning>
  Customers are responsible for ensuring all resources are properly deprovisioned to avoid additional future charges. Please review all steps carefully.
</Warning>

1. Export any [database](/core-concepts/managed-databases/overview) data that you need.
   * To export Aptible backups, [restore the backup](/core-concepts/managed-databases/managing-databases/database-backups#restoring-from-a-backup) to a new database first.
   * Use the [`aptible db:tunnel CLI command`](/reference/aptible-cli/cli-commands/cli-db-tunnel) and whichever tool your database supports to dump the database to your computer.
2. Delete [metric drains](/core-concepts/observability/metrics/metrics-drains/overview)
   * [Metric drains](/core-concepts/observability/metrics/metrics-drains/overview) for an [environment](/core-concepts/architecture/environments) can be deleted by navigating to the environment's **Metric Drains** tab in the dashboard.
3. Delete [log drains](/core-concepts/observability/logs/log-drains/overview)
   * Log drains for an [environment](/core-concepts/architecture/environments) can be deleted by navigating to the environment's **Log Drains** tab in the dashboard.
4. Deprovision your [apps](/core-concepts/apps/overview) from the dashboard or with the [`aptible apps:deprovision`](/reference/aptible-cli/cli-commands/cli-apps-deprovision) CLI command.
   * Deprovisioning an [app](/core-concepts/apps/overview) automatically deprovisions all of its [endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/overview) as well.
5. Deprovision your [databases](/core-concepts/managed-databases/overview) from the dashboard or with the [`aptible db:deprovision`](/reference/aptible-cli/cli-commands/cli-db-deprovision) CLI command.
   * Monthly and daily backups are automatically deleted when the [database](/core-concepts/managed-databases/overview) is deprovisioned.
6. Delete [database backups](/core-concepts/managed-databases/managing-databases/database-backups)
   * Use the **delete all on page** option to delete the final backups for your [databases](/core-concepts/managed-databases/overview).

     <Warning>
       Backups Warning: Please note Aptible will no longer have a copy of your data when you delete your backups. Please create your own backup if you need to retain a copy of the data.
     </Warning>
7. Deprovision the [environment](/core-concepts/architecture/environments) from the dashboard.
   * You can deprovision environments once all the resources in that [environment](/core-concepts/architecture/environments) have been deprovisioned. If you have not deleted all resources, you will see a message advising you to delete any remaining resources before you can successfully deprovision the [environment](/core-concepts/architecture/environments).
8. Submit an account deletion request through the Dashboard to deprovision your [Dedicated Stack](/core-concepts/architecture/stacks#dedicated-stacks) and, if applicable, remove Premium or Enterprise Support.
   * Navigate to your organization's settings to access the account deletion form.
   * Confirm your organization name and provide a cancellation reason (both required).
   * The request automatically creates a support ticket with your account details and cancellation reason.
   * If this step is incomplete, you will incur charges until Aptible deprovisions the dedicated stack and removes paid support from your account. Aptible Support can only complete this step after you submit the account deletion form.

<Warning>
  Final Invoice: Please note you will likely receive one more invoice after deprovisioning for usage from the last invoice to the time of deprovisioning.
</Warning>

<Tip>
  Verifying you have successfully deprovisioned resources: You can review your estimated monthly costs and/or future invoices to verify that all resources have been successfully deprovisioned.
</Tip>
