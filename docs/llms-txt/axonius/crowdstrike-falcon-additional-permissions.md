# Source: https://docs.axonius.com/docs/crowdstrike-falcon-additional-permissions.md

# CrowdStrike Falcon Additional Permissions

The following permissions are required to support *advanced configuration and enforcement actions* in the **CrowdStrike Falcon** adapter. Ensure these permissions are granted to the user account used for these operations.

## Advanced Configuration

The following permissions are required for various Advanced Configurations:

| Category                                       | Scope                                | Permission |
| :--------------------------------------------- | :----------------------------------- | :--------- |
| Users                                          | User Management                      | Read       |
| Vulnerabilities                                | vulnerabilities:read                 | Read       |
| Configuration Assessments                      | Falcon Configuration Assessment:read | Read       |
| Installed Patches (see more information below) | Scheduled Reports API                | Read       |

### Setting Up the Adapter to Fetch Installed Patches

To be able to use the **Fetch Installed Patches** advanced configuration:

* You must have a Spotlight subscription.
* You must have the following permission: Scheduled Reports API read access.
* Only Windows Devices are supported.

In Spotlight, follow these steps:

1. Navigate to **Scheduled Reporting** > **Vulnerability Management**.

2. Select **Installed Patches**.

3. Include at least the Hostname in the report; add more filters as needed.

4. Name the report (to use in the adapter's Advanced Configuration) and click **Next**.

5. Schedule the report to run daily 2 hours before the start of the global fetch or custom adapter discovery time, then click **Next**.

6. Ensure that the scheduled report can be read by the credentials used in the adapter configuration. Then, click **Next**.

7. Skip the Sharing part and click **Save**.

8. In Axonius, enable the **Fetch installed patches from the following report** advanced setting, and enter the name of the Installed Patches report to fetch.

## Enforcement Actions

The following permissions are required to run **CrowdStrike Falcon** Enforcement Actions:

| Scope | Permission |
| :---- | :--------- |
| Hosts | Write      |