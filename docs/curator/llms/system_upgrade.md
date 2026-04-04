# Source: https://docs.curator.interworks.com/upgrading_migration/upgrading/system_upgrade.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# System Upgrade

> Learn about the various methods to update your Curator installation to the latest version.

There are several easy ways to update Curator.

To see if Curator needs an update, check the status of your Curator instance on the homepage of the backend,
or on the System Upgrade page.

The "Current Version" will show what software version Curator is currently running and the "Latest Version"
will show the latest release available.

**Attention: We recommend taking a Curator Backup before an upgrade. More details can be found [here](/upgrading_migration/backups/curator_backup).**

## Upgrading Curator

***One-click Upgrade:***

1. Login to the backend of your Curator instance (e.g. `https://curator.example.com/backend`).
2. Navigate to the **Settings** > **Curator** > **System Upgrade** section using the left-hand menu.
3. Click the "Start One-click Upgrade" button.

***Manual Upgrade:***

1. Login to the backend of your Curator instance (e.g. `https://curator.example.com/backend`).
2. Navigate to the **Settings** > **Curator** > **System Upgrade** section using the left-hand menu.
3. Click the "Manual Upgrade" button to display the Manual Upgrade links in the release notes section at the
   bottom of the page.
4. Click the link of the version you wish to upgrade to, this will download a .zip file containing the upgrade contents.
5. Upload the .zip file you just downloaded to the "Upgrade Zip Archive" section and click the "Submit" button.

***Curator API:***

1. Login to the backend of your Curator instance (e.g. `https://curator.example.com/backend`).
2. Navigate to the **Settings** > **Curator** > **API Keys** section using the left-hand menu.
3. Select an existing key or create a new key
4. If creating a new key, save the key.
5. From the REST API dropdowns, select 'Portal' in the left dropdown and 'Upgrade' in the right dropdown.
6. Click the link that was generated below the drop-downs.
7. This will open a new tab, when upgrade is successful a small success text display will populate.

## Troubleshooting

***Having Issues With the Upgrade?*** Try our [Upgrade Troubleshooting Documentation](/upgrading_migration/upgrading/troubleshooting_upgrades).

## Multi-version Upgrades (4+ versions)

We recommend upgrading no more than 3 versions at a time.

If you plan to make an upgrade to a Curator instance that is more than 4 versions out-of-date, use the
version-specific upgrades on the upgrade page, instead of the "One-click upgrade".
