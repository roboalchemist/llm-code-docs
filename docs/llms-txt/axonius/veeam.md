# Source: https://docs.axonius.com/docs/veeam.md

# Veeam

Veeam provides backup, disaster recovery and modern data protection software for virtual, physical and multi-cloud infrastructures.

The Veeam adapter enables Axonius to fetch and catalog backup infrastructure assets, including managed servers, virtual machines, and backup jobs, ensuring comprehensive visibility into data protection coverage and recovery readiness.

## Asset Types Fetched

* Devices

## Before You Begin

### Required Ports

* 9398/9419

### Authentication Methods

* User Name/Password

### Required Permissions

The user account used for the adapter connection must have permissions to access the Veeam API and read asset data.

### APIs

Axonius uses the following APIs to retrieve asset data:

* <Anchor label="Veeam Backup Enterprise Manager REST API" target="_blank" href="https://helpcenter.veeam.com/docs/backup/em_rest/overview.html?ver=110">Veeam Backup Enterprise Manager REST API</Anchor>
* <Anchor label="Versioning" target="_blank" href="https://helpcenter.veeam.com/docs/backup/vbr_rest/versioning.html?ver=120">Versioning</Anchor>
* <Anchor label="Veeam Backup and Replication 11" target="_blank" href="https://helpcenter.veeam.com/archive/backup/110/vbr_rest/reference/vbr-rest-v1-rev2.html?ver=110">Veeam Backup and Replication 11</Anchor>

### Supported from Version

This adapter is supported from Axonius version 4.5.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Veeam server.
2. **Port** *(default: 9398)* - The port used for the connection. When you select  *API v 1.0-rev1 ('Veeam Backup and Replication 11)*, the default port is 9419 (the adapter will try both ports)
3. **User Name** and **Password** - The credentials for a user account that has permissions to fetch assets.
4. **API Version** *(default: API v1\_6 Veeam Enterprise Manager)* - Select the API Version, either API v1\_6 (Veeam Enterprise Manager), API v 1.0-rev1 (Veeam Backup and Replication 11), API 1.1-rev0 (Veeam Backup and Replication 12), or API 1.2-rev0 (Veeam Backup and Replication 12).

<Image alt="Veeam" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Veeam.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<Callout icon="💡" theme="warn">
  Important

  Most of the advanced configurations are relevant only for API v1\_6 (Veeam Enterprise Manager) rather than API 1.1-rev0 or API 1.2-rev0 (Veeam Backup and Replication 12). See below for clarification.
</Callout>

1. **Fetch Managed Servers** - Select whether to fetch managed servers. **Note**: This setting no longer fetches VMs and job devices.
2. **Fetch Backup Servers** *(only relevant for Veeam Enterprise Manager)* - Select whether to fetch backup servers.
3. **Fetch Job Devices** - Select whether to fetch job devices.
4. **Fetch CDP Jobs** *(only relevant for Veeam Enterprise Manager)* - Select whether to fetch Customer Data Platform jobs.
5. **Fetch Agent Jobs** *(only relevant for Veeam Enterprise Manager)* - Select this option to fetch information about physical infrastructure servers.
6. **Fetch Statuses** *(only relevant for Veeam Enterprise Manager)* - Select whether to fetch backup statuses.
7. **Fetch VMs** (*default: false*) - Select this option to fetch information about Virtual Machines.
8. **Fetch excluded VMs** - Select this option to fetch virtual machines that have been excluded from backup jobs. This option is available when **Fetch VMs** (above) is enabled.
9. **Fetch Restore Points** - Select this option to fetch restore points for backups and backup objects.
10. **Fetch Backup Objects** *(only relevant for Veeam Backup and Replication 12)* - Select this option to fetch Backup Objects as devices.
11. **Use object ID as Cloud ID** *(default: true)* - By default Axonius uses the object ID as the Cloud ID. Clear this option to not use the object ID as the Cloud ID.
12. **Backup server prefix to remove** *(optional)* - Enter the backup server prefix to parse from the hostname.
13. **Ignore prefix in device name** *(default: true)* - If the device name contains a prefix in the format "prefix - name", the prefix will be ignored. If this setting is disabled, the full device name will be parsed.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                                           | Supported | Notes |
| ------------------------------------------------- | --------- | ----- |
| Veeam Backup & Replication 11: Enterprise Manager | Yes       | --    |
| Veeam Backup & Replication 11                     | Yes       | --    |