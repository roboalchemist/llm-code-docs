# Source: https://docs.axonius.com/docs/okta-advanced-settings.md

# Okta - Advanced Settings

## Accessing Advanced Configuration

1. Navigate to **Adapters** and search for `Okta` then click the adapter tile
2. In the left menu, select **Advanced Configuration** under **Advanced Settings**

## Okta - Advanced Settings

<Callout icon="📘" theme="info">
  Note:

  Advanced settings can either apply to all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Email domain include list** *(optional)* - Specify a comma-separated list of email domains to only fetch users whose email domain is in the specified list.
2. **Fetch enrichment assets in the background (Apps, Groups)** - Select to fetch apps and groups in the background - outside the regular fetch cycle. \[Note: This setting doesn’t apply when the adapter is running in real time.]
3. **Fetch Apps** - Select this option to also fetch information about applications.
4. **Exclude Inactive Apps** - Select this option to only fetch apps with a status of ‘Active’. The ‘Fetch apps’ setting must be selected.
5. **Fetch Apps with no users** - Select this option to also fetch information about applications with no users.
6. **Fetch Bookmarks apps** *(This option is only available for users who have Axonius SaaS Applications)* - Select this option to also fetch information about Bookmarks apps.
7. **Fetch groups** - Select this option to fetch group details.
8. **Fetch users authentication factors** - Select this option to also fetch users’ authentication factors. *(This option is enabled by default for accounts with Axonius Identity.)*
9. **Fetch Users** - Select this option to also fetch information about users.
10. **Enrich Groups with Applications (SaaS Management)** - Select this option to populate the ‘Applications’ field in Group assets with relevant data fetched from Okta.
11. **Enrich user data on a synchronous manner (for example: groups)** - Select this option to enrich data synchronously. (Use for organizations with large amounts of users/groups/apps/roles).
12. **Fetch users logs** - Select this option to fetch information about user's log events, that include details such as: IP address, browser, OS type.
13. **Fetch logs from the last X days** *(optional)*  - Enter a number of days back from which to fetch logs.
14. **Fetch roles and permissions** - Select this option to fetch additional information on roles and permissions, also used to enrich users and groups (the roles are also associated with Okta Groups). Note that when enabling this, Resource Sets will be fetched as Application Resources.
15. **Fetch deprovisioned users** - Select this option to fetch users that are deprovisioned.
16. **Display recovery question in View Advanced** - Select this option to save the users' recovery questions in the Axonius database. When you enable this parameter, the recovery question is displayed in plain-text in the **View Advanced** data for the Okta Adapter.
17. **User results limit** *(required, default: 200)* - Specify the number of results per page when Axonius makes the API call.
18. **Device with users fetch pagination limit** *(required, default: 50)* - Sets the limit of results per page when fetching devices with detailed users information. This configuration should not be changed unless instructed by technical support or engineering.
19. **Disable Devices Fetch** - Select this option to disable fetching device details from Okta.
20. **Fetch application permissions (applications grants)**: Enrich applications with grant and scope info. The configured Okta credentials must have the `okta.appGrants.read` permission in order to fetch this data. For customers that configured an API key/token, they must ensure that the account for which the token was created has a role with “View applications and their details” permission.
21. **Group type** *(optional)* - Select the type of group to fetch from Okta. For more information, see [Okta group source types](https://help.okta.com/en-us/content/topics/users-groups-profiles/usgp-group-types.htm).
22. **Raw data fields exclusions (comma separated list)***(optional)* - Specify a comma-separated list of data fields to exclude from the fetch. Note Nested data fields should be separated by forward slashes. For example, if you want to exclude a field email inside the Profile complex field then specify `profile/email`.
23. **List of known domains** *(This option is only available for users who have Axonius SaaS Applications)*-\_ Specify a comma-separated list of domains used to identify external users in Okta.
24. **Fetch audit activities (Behavior Analytics)** *(This option is only available for users who have Axonius SaaS Applications)* - Select this option to also fetch audit logs from Okta.
25. **Fetch all logs history each cycle**  *(This option is only available for users who have Axonius SaaS Applications)*- Select this option to also fetch logs in each discovery cycle, otherwise it will only fetch the new logs since the last fetch cycle.
26. **Fetch Security Logs** - Select this option to fetch security logs based on `security.request.blocked` and `security.threat.detected` events.
27. **Fetch Application Settings** *(This option is only available for users who have Axonius SaaS Applications)* - Select this option to fetch general Okta admin settings, such as authentication policy settings or notification settings. (To fetch this information you need to configure the User name and Password fields. If 2FA is required for this application, the 2FA key must be provided.)
28. **Enrich Groups with owners** - Select this option to enrich Groups with group owners data.

### Working with Axonius Identities

If Axonius Identities is being used, specific settings must be enabled to fetch complete data.

* Fetch Apps
* Exclude Inactive Apps
* Fetch Apps with no users
* Fetch Bookmarks apps
* Fetch groups
* Fetch users authentication factors
* Fetch Users
* Enrich Groups with Applications
* Fetch users logs
* Fetch roles and permissions
* Fetch deprovisioned users
* Fetch application permissions
* Fetch audit activities
* Fetch Security Logs
* Fetch Application Settings