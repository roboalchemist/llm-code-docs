# Source: https://www.aptible.com/docs/core-concepts/managed-databases/managing-databases/database-backups.md

# Database Backups

> Learn more about Aptible's database backup solution with automatic backups, default encryption, with flexible customization

# Overview

Database Backups are essential because they provide a way to recover important data in case of disasters or data loss. They also provide a historical record of changes to data, which can be required for auditing and compliance purposes.

Aptible provides Automatic Backups of your Databases every 24 hours, along with a range of other backup options. All Backups are compressed and encrypted for maximum security and efficiency. Additionally, all Backups are automatically stored across multiple Availability Zones for high-availability.

# Automatic Backups

By default, Aptible provides automatic backups of all Databases. The retention period for Automated Backups is determined by the Backup Retention Policy for the Environment in which the Database resides. The configuration options are as follows:

* `DAILY BACKUPS RETAINED` - Number of daily backups retained
* `MONTHLY BACKUPS RETAINED` - Number of monthly backups retained (the last backup of each month)
* `YEARLY BACKUPS RETAINED` - Number of yearly backups retained (the last backup of each year)
* `COPY BACKUPS TO ANOTHER REGION: TRUE/FALSE` - When enabled, Aptible will copy all the backups within that Environment to another region. See: Cross-region Copy Backups
* `KEEP FINAL BACKUP: TRUE/FALSE` - When enabled, Aptible will create and retain one final backup of a Database when you deprovision it. See: Final Backups

<Tip>
  **Recommended Backup Retention Policies**

  **Production environments:** Daily: 14-30, Monthly: 12, Yearly: 5, Copy backups to another region: TRUE (depending on DR needs), Keep final backups: TRUE

  **Non-production environments:** Daily: 1-14, Monthly: 0, Yearly: 0, Copy backups to another region: FALSE, Keep final backups: FALSE
</Tip>

# Manual Backups

Manual Backups can be created anytime and are retained indefinitely (even after the Database is deprovisioned).

# Cross-region Copy Backups

When `COPY BACKUPS TO ANOTHER REGION` is enabled on an Environment, Aptible will copy all the backups within that Environment to another region. For example, if your Stack is in the US East Coast, then Backups will be copied to the US West Coast.

<Tip>
  Cross-region Copy Backups are useful for creating redundancy for disaster recovery purposes. To further improve your recovery time objective (RTO), it’s recommended to have a secondary Stack in the region of your Cross-region Copy Backups to enable quick restoration in the event of a regional outage.
</Tip>

The exact mapping of Cross-region Copy Backups is as follows:

| Originating region | Destination region(s)          |
| ------------------ | ------------------------------ |
| us-east-1          | us-west-1, us-west-2           |
| us-east-2          | us-west-1, us-west-2           |
| us-west-1          | us-east-1                      |
| us-west-2          | us-east-1                      |
| sa-east-1          | us-east-2                      |
| ca-central-1       | ca-west-1 (formerly us-east-2) |
| eu-west-1          | eu-central-1                   |
| eu-west-2          | eu-central-1                   |
| eu-west-3          | eu-central-1                   |
| eu-central-1       | eu-west-1                      |
| ap-northeast-1     | ap-northeast-2                 |
| ap-northeast-2     | ap-northeast-1                 |
| ap-southeast-1     | ap-northeast-2, ap-southeast-2 |
| ap-southeast-2     | ap-southeast-1                 |
| ap-south-1         | ap-southeast-2                 |

<Note>
  Aptible guarantees that data processing and storage occur only within the US for US Stacks and EU for EU Stacks.
</Note>

# Final Backups

When `KEEP FINAL BACKUP` is enabled on an Environment, Aptible will create and retain a backup of the Database when you deprovision it. Final Backups are kept indefinitely as long as the Environment has this setting enabled.

<Tip>
  We highly recommend enabling this setting for production Environments.
</Tip>

# Managing Backup Retention Policy

The retention period for Automated Backups is determined by the Backup Retention Policy for the Environment in which the Database resides.

The default Backup Retention Policy for an Environment is 30 Automatic Daily Backups, 12 Monthly Backups, 6 Yearly Backups, Keep Final Backup: Enabled, Cross-region Copy Backup: Disabled.

Backup Retention Policies can be modified using one of these methods:

* Within the Aptible Dashboard:
  * Select the desired Environment
  * Select the **Backups** tab
* Using the [`aptible backup_retention_policy:set CLI command`](/reference/aptible-cli/cli-commands/cli-backup-retention-policy-set).
* Using the Aptible [Terraform Provider](https://registry.terraform.io/providers/aptible/aptible/latest/docs)

<Warning>
  Reducing the number of retained backups, including disabling copies or final backups, will automatically delete existing, automated backups that do not match the new policy. This may result in the permanent loss of backup data and could violate your organization's internal compliance controls.
</Warning>

<Tip>
  **Cost Optimization Tip:** [See this related blog for more recommendations for balancing continuity and costs](https://www.aptible.com/blog/backup-strategies-on-aptible-balancing-continuity-and-costs)
</Tip>

### Excluding a Database from new Automatic Backups

<Frame>
    <img src="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/DisablingDatabaseBackups.gif?s=ab77a92c98cc0f60041e8a2eccdedb55" alt="Disabling Backups" data-og-width="904" width="904" data-og-height="720" height="720" data-path="images/DisablingDatabaseBackups.gif" data-optimize="true" data-opv="3" />
</Frame>

A Database can be excluded from the backup retention policy preventing new Automatic Backups from being taken. This can be done within the Aptible Dashboard from the Database Settings, or via the [Terraform Provider](https://registry.terraform.io/providers/aptible/aptible/latest/docs).

Once this is selected, there will be no new automatic backups taken of this database, including preventing a final backup of the database during deprovision, even if the environment's policy specifies it. Please note: making this change on an existing database does not automatically delete previously taken backups. Purging the previously taken backups can be achieved in the following ways:

* Using the [`aptible backup:list DB_HANDLE`](/reference/aptible-cli/cli-commands/cli-backup-list) to provide input into the [`aptible backup:purge BACKUP_ID`](/reference/aptible-cli/cli-commands/cli-backup-purge) command
* Setting the output format to JSON, like so:

```jsx  theme={null}
APTIBLE_OUTPUT_FORMAT=json aptible backup:list DB_HANDLE 
```

# Purging Backups

Automatic Backups are automatically and permanently deleted when the associated database is deprovisioned. Final Backups and Cross-region Copy Backups that do not match the Backup Retention Policy are also automatically and permanently deleted. This purging process can take up to 1 hour.

All Backups can be manually and individually deleted.

# Restoring from a Backup

Restoring a Backup creates a new Database from the backed-up data. It does not replace or modify the Database the Backup was initially created from. By default, all newly restored Databases are created as a 1GB [General Purpose Container Profile](/core-concepts/scaling/container-profiles#default-container-profile), however you can specify both container size and profile using the [`backup:restore`](/reference/aptible-cli/cli-commands/cli-backup-restore.mdx) command.

<Info>
  Deep dive: Databases Backups are stored as volume EBS Snapshots. As such, Databases restored from a Backup will initially have degraded disk performance, as described in the ["Restoring from an Amazon EBS snapshot" documentation](https://docs.aws.amazon.com/prescriptive-guidance/latest/backup-recovery/restore.html).
  If you are using a restored Database for performance testing, the performance test should be run twice: once to ensure all of the required data has been synced to disk and the second time to get an accurate result.
  Disk initialization time can be minimized by restoring the backup in the same region the Database is being restored to. Generally, this means the original Backup should be restored, not a copy.
</Info>

<Tip>
  If you have special retention needs (such as for a litigation hold), please contact [Aptible Support.](/how-to-guides/troubleshooting/aptible-support)
</Tip>

# Encryption

Aptible provides built-in, automatic [Database Encryption](/core-concepts/managed-databases/managing-databases/database-encryption/overview). The encryption key and algorithm used for Database Encryption are automatically applied to all Backups of a given Database.

# FAQ

<AccordionGroup>
  <Accordion title="How do I modify an Environments Backup Retention Policy?">
    Backup Retention Policies can be modified using one of these methods:

    * Within the Aptible Dashboard:
      * Select the desired Environment
      * Select the **Backups** tab
    * Using the [`aptible backup_retention_policy:set CLI command`](/reference/aptible-cli/cli-commands/cli-backup-retention-policy-set).
    * Using the Aptible [Terraform Provider](https://registry.terraform.io/providers/aptible/aptible/latest/docs)

        <img src="https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/backups.png?fit=max&auto=format&n=gJr2xlqbHzeeHUse&q=85&s=99804bb00264e6da0a9a3c20015cbdff" alt="Reviewing Backup Retention Policy in Aptible Dashboard" data-og-width="2800" width="2800" data-og-height="2000" height="2000" data-path="images/backups.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/backups.png?w=280&fit=max&auto=format&n=gJr2xlqbHzeeHUse&q=85&s=44e46a585009d35b4565efecc7c87958 280w, https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/backups.png?w=560&fit=max&auto=format&n=gJr2xlqbHzeeHUse&q=85&s=6a9b4cb756c0cf1ccef4535cb8eff6c2 560w, https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/backups.png?w=840&fit=max&auto=format&n=gJr2xlqbHzeeHUse&q=85&s=6dad40955f5f0a11f0117cc2980dad26 840w, https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/backups.png?w=1100&fit=max&auto=format&n=gJr2xlqbHzeeHUse&q=85&s=65111fe53c0571174528e76fff73b6df 1100w, https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/backups.png?w=1650&fit=max&auto=format&n=gJr2xlqbHzeeHUse&q=85&s=b62811079b049841e64a49f8bfa234bb 1650w, https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/backups.png?w=2500&fit=max&auto=format&n=gJr2xlqbHzeeHUse&q=85&s=1bdbac630ad063bc1607f0565d8c93be 2500w" />
  </Accordion>

  <Accordion title="How do I view/manage Automatic Backups?">
    Automatic Backups can be viewed in two ways:

    * Using the [`aptible backup:list`](/reference/aptible-cli/cli-commands/cli-backup-list) command
    * Within the Aptible Dashboard, by navigating to the Database > Backup tab
  </Accordion>

  <Accordion title="How do I view/manage Final Backups?">
    Final Backups can be viewed in two ways:

    * Using the `aptible backup:orphaned` command
    * Within the Aptible Dashboard by navigating to the respective Environment > “Backup Management” tab > “Retained Backups of Deleted Databases”
  </Accordion>

  <Accordion title="How do I create Manual Backups?">
    Users can create Manual Backups in two ways:

    * Using the [`aptible db:backup`](/reference/aptible-cli/cli-commands/cli-db-backup)) command
    * Within the Aptible Dashboard by navigating to the Database > “Backup Management” tab > “Create Backup”
  </Accordion>

  <Accordion title="How do I delete a Backup?">
    All Backups can be manually and individually deleted in the following ways:

    * Using the [`aptible backup:purge`](/reference/aptible-cli/cli-commands/cli-backup-purge) command
    * For Active Databases - Within the Aptible Dashboard by:
      * Navigating to the respective Environment in which your Database lives in
      * Selecting the respective Database
      * Selecting the **Backups** tab
      * Selecting **Permanently remove this backup** for the respective Backup
    * For deprovisioned Databases - Within the Aptible Dashboard by:
      * Navigating to the respective Environment in which your Database Backup lives in
      * Selecting the **Backup Management** tab
      * Selecting Delete for the respective Backup

        <img src="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Purging_Backups.png?fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=addb53fb4b2e5f84ade35320791a650e" alt="" data-og-width="1919" width="1919" data-og-height="915" height="915" data-path="images/App_UI_Purging_Backups.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Purging_Backups.png?w=280&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=8d94ade53e62ac4b7b48efddf0c4ed34 280w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Purging_Backups.png?w=560&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=14a21720d3b4f2e850369d6354cb03b9 560w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Purging_Backups.png?w=840&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=ac0045bf43b3b2dcaa359a3e5bfa6052 840w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Purging_Backups.png?w=1100&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=34dda12b721194152acf5433773cefd2 1100w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Purging_Backups.png?w=1650&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=64ab67c24a0b57c9b94173e53061d8a0 1650w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Purging_Backups.png?w=2500&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=0a63d4f655893b6f257973a8e17c41ae 2500w" />
  </Accordion>

  <Accordion title="How can I exclude a Database from Automatic Backups?">
    * Navigating to the respective Database
    * Selecting the **Settings** tab
    * Select **Disabled: No new backups allowed** within **Database Backups**
  </Accordion>

  <Accordion title="How should I set my Backup Retention Policy for Production Environments?">
    For critical production data, maintaining a substantial backup repository is crucial. While compliance frameworks like HIPAA don't mandate a specific duration for data retention, our practice has been to keep backups for up to six years. The introduction of Yearly backups now makes this practice more cost-effective.
    Aptible provides a robust default backup retention policy, but in most cases, a custom retention policy is best for tailoring to specific needs. Aptible backup retention policies are customizable at the Environment level, which applies to all databases within that environment.

    A well-balanced backup retention policy for production environments might look something like this:

    * Yearly Backups Retained: 0-6
    * Monthly Backups Retained: 3-12
    * Daily Backups Retained: 15-60
  </Accordion>

  <Accordion title="How should I set my Backup Retention Policy for Non-production Environments?">
    When it comes to non-production environments, the backup requirements tend to be less stringent compared to production environments. In these cases, Aptible recommends the establishment of custom retention policies tailored to the specific needs and cost considerations of non-production environments.
    An effective backup retention policy for a non-production environment might include a more conservative approach:

    * Yearly Backups Retained: 0
    * Monthly Backups Retained: 0-1
    * Daily Backups Retained: 1-7

    To optimize costs, it’s best to disable Cross-region Copy Backups and Keep Final Backups in non-production environments — as these settings are designed for critical production resources.
  </Accordion>

  <Accordion title="How do I restore a Backup?">
    You can restore from a Backup in the following ways:

    * Using the `aptible backup:restore` command
    * For Active Databases - Within the Aptible Dashboard by:
      * Navigating to the respective Environment in which your Database lives in
      * Selecting the respective Database
      * Selecting the **Backups** tab
      * Selecting **Restore to a New Database** from the respective Backup
    * For deprovisioned Databases - Within the Aptible Dashboard by:
      * Navigating to the respective Environment in which your Database Backup lives in
      * Selecting the **Backup Management** tab
      * Selecting **Restore to a New Database** for the respective Backup

        <img src="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Restoring_Backups.png?fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=e74166f0fed1a1f6b7d70e9404019364" alt="" data-og-width="2800" width="2800" data-og-height="2142" height="2142" data-path="images/App_UI_Restoring_Backups.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Restoring_Backups.png?w=280&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=7fe54d60d077a6aeb8149ba493639d02 280w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Restoring_Backups.png?w=560&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=338c1392feb84a29d0e94c61837eee5d 560w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Restoring_Backups.png?w=840&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=c276e972d8abeb65f4d54178f2bce5b0 840w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Restoring_Backups.png?w=1100&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=b7c416df70f9a34187952238b4f1aa6c 1100w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Restoring_Backups.png?w=1650&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=79d462f7af258e005d2e81cb86aca837 1650w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Restoring_Backups.png?w=2500&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=47cd290be0a50b02ad7b214162eb6235 2500w" />
  </Accordion>
</AccordionGroup>
