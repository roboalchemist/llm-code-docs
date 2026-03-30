# Source: https://docs.axonius.com/docs/entra-id-advanced-settings.md

# Entra-ID Advanced Settings

## Accessing Advanced Configuration

1. Navigate to **Adapters** and search for `Entra ID` then click the adapter tile
2. In the left menu, select **Advanced Configuration** under **Advanced Settings**

## Microsoft Entra ID - Advanced Settings

<Callout icon="📘" theme="info">
  Note:

  Advanced settings can either apply to all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fields to exclude** *(optional)* - Specify a comma-separated list of fields to be excluded from the fetched data. This causes the adapter to exclude the listed fields from the raw and parsed data. For example, if this field value is "emailAddress, phoneNumber", both fields will be excluded from the raw and parsed data fetched by this adapter.
2. **Fetch only users**- Select this option to only fetch users and not fetch data relating to other assets.
3. **Fetch users password reset info** *(default: True)* - Select this to fetch password reset information for user accounts.
4. **Fetch only users with account enabled** *(optional)* - Select to fetch only users with an account enabled in the Entra ID.
5. **Fetch "Guest" users** *(required, default: true)* - Select this option to fetch external users from Entra ID.
6. **Fetch sponsors for “Guest” users** - Select this option to fetch sponsor for Guest users using [this endpoint](https://learn.microsoft.com/en-us/graph/api/user-list-sponsors?view=graph-rest-1.0\&tabs=http) and to display the relationship between sponsors and Guest users in the [Asset Graph](/docs/asset-graph).
7. **Fetch deleted users** - Select this option to also fetch users that were deleted in Entra ID.
8. **Custom filter expression for fetching users** *(optional)* - Enter a filter expression to exclude Entra ID users from the fetch. For more information, see [Use the Filter Query Parameter](https://learn.microsoft.com/en-us/graph/filter-query-parameter?tabs=http#code-try-2),[Advanced query capabilities on Microsoft Entra ID objects](https://learn.microsoft.com/en-us/graph/aad-advanced-queries?tabs=http), and [User resource type](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0).
9. **Fetch custom user flow attributes (Requires `IdentityUserFlow.Read.All` permission)** - Select this option to fetch extra custom user flow attributes to be added dynamically to the User’s assets data.

<Callout icon="📘" theme="info">
  Note:

  When this setting is selected, you must have the `IdentityUserFlow.Read.All` permission.
</Callout>

10. **Fetch active user details from Office 365 in the last X days** - Define a number of last days to fetch active user information from.
11. **Fetch email activity from Office 365 in the last X days** *(required, default: 0)* - Specify the number of days to fetch email activity per user. The email activities include:
    1. Deleted users
    2. Dates of account deletion of users
    3. Number of times an email send action was recorded
    4. Number of times an email received action was recorded
    5. Number of times an email read action was recorded
    6. Last time any user performed a read or send email activity
    7. Report period
    8. Products that are assigned to the users

<Callout icon="📘" theme="info">
  Note:

  In order to use this field the [application permissions](/docs/microsoft-azure-active-directory-ad#1) in Microsoft Azure Portal must include the following permissions:

  * `Reports.Read.All` - To unhide user-level information within O365, a global administrator needs to make that change in the Microsoft 365 admin center.

  * In the admin center, go to the Settings `>` Org Settings `>` Services page.

  * Select **Reports**.

  * Clear the statement Display concealed user, group, and site names in all reports, and then save the changes. Refer to [Microsoft Documentation - Show User Details in the Reports](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports?view=o365-worldwide#show-user-details-in-the-reports)
</Callout>

12. **User mail parse fallback** - Use the option that you select to be the source of the user's email.
13. **Fetch users images** - Select this option to fetch the user’s image.

<Callout icon="📘" theme="info">
  Note

  Risky users are defined in [risky User resource type](https://docs.microsoft.com/en-us/graph/api/resources/riskyuser?view=graph-rest-1.0) and in [What is risk?](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-risks)
</Callout>

14. **Fetch risky users information** - Select whether to fetch information about risky users. Information includes:
    1. If the user was deleted
    2. Is processing
    3. Date the user last updated
    4. Risk level
    5. Risk state
    6. Risk details

<Callout icon="📘" theme="info">
  Note

  For these settings, you must have the `IdentityRiskyUser.Read.All` permission.
</Callout>

15. **Fetch risky users information with selected Level** *(required, default High)*- Select levels of risky users' information to fetch. Otherwise, all levels are fetched
16. **Fetch risky users information with selected 'State'** *(required, Default - At Risk, Confirmed Compromised.)* - Select states of risky users\` information to fetch. Otherwise, all states are fetched.
17. **Fetch user app roles** - Select whether to retrieve the app roles that are assigned to a user.

<Callout icon="📘" theme="info">
  Note:

  When this setting is selected, you must have either the `Directory.Read.All` or the `AppRoleAssignment.ReadWrite.All` permission.
</Callout>

18. **Admin groups for users** - Enter the names of user groups you want to designate as “admin” groups. Users belonging to these groups will have their “Is Admin User” field set to “True”.
19. **Fetch user owned objects** - Fetch the list of directory objects that are owned by a user.
20. **Fetch user contacts**- Select to fetch all Outlook contact information for each user.

<Callout icon="📘" theme="info">
  Note:

  When this setting is selected, you must have the `Contacts.Read` permission.
</Callout>

21. **Fetch user assigned roles (Permissions required `Directory.Read.All` or `RoleManagement.Read.Directory`)** *(optional)* - Select whether to fetch the assigned roles of a user. When **Allow use of BETA API endpoints** is also selected, transitive assigned roles are also fetched.
22. **Fetch user authentication methods** - Fetch user's authentication methods.
23. **Fetch Users' managers** - Select this option to fetch information about managers of Entra ID users.
24. **Fetch users license details** - Select whether to fetch the licenses assigned to a given user.
25. **Fetch managed app registrations from MAM** *(default: disabled)* - Define if and how to fetch managed app registrations from MAM. The following options are available:
    1. Disabled - Do not fetch.
    2. Devices Management API - Fetch managed app registrations from MAM using the Devices Management API .
    3. Report - Fetch MAM information from a Reports. When this is selected, the adapter will fetch this information in a way that will be used to define the Last Seen field of the Azure AD device it is affiliated with.
26. **Fetch mailbox settings for users** - Enter the names of the mailbox settings for users that you want to fetch and populate the 'Has Mailbox' and 'Mailbox Settings' fields under Users assets in Entra ID. Values you can enter include:
    1. **Fetch mailbox Settings**
    2. **Fetch Inbox Message Rules**
    3. **Fetch Mailbox Delegation Info** (for accounts with Axonius SaaS Applications).

<Callout icon="📘" theme="info">
  Note

  When this setting is enabled, you must have the `MailboxSettings.Read` permission.
</Callout>

27. **Fetch mailbox usage information from Office 365 in the last X days** *(optional, default: 0)* - Specify the number of days to fetch mailbox usage information per each user.
28. **Fetch Office 365 Litigation Hold information** - Select this option to enable this adapter to fetch legal hold information as accounts. Additionally, this option enriches users with Litigation Hold information (user sources per legal hold) displayed in "Litigation Holds" under users. This option also enriches users with Custodian (user) information and the case information associated with the custodian under the "Custodian Info" and "eDiscovery Cases Associated with Custodian" user fields, respectively.
29. **Fetch date of last activity for M365 products** - Select this option to fetch the apps usage report from Microsoft and parse the last activity date as the 'Last Seen from Activities' user-aggregated field.
30. **Fetch Microsoft apps reports** - Select one or more reports to fetch information about Microsoft Apps usage. The available options are Visio User Activity and Project User Activity.
31. **Fetch user assigned eligibility schedules** - Select this option to fetch role and group eligibility schedules and their assignments.

    <Callout icon="📘" theme="info">
      **Note**

      Only customers with [Axonius Identities](https://docs.axonius.com/axonius-help-docs/docs/getting-started-with-identities) can fetch eligibility schedules.
    </Callout>
32. **Fetch user cloud extensions attributes** - Select this option to fetch data from user extension attributes.
33. **Fetch user groups** *(required, default: true)* - Select this option to fetch information on every group a user is a member.
34. **User groups exclude list** *(optional)* - When **Fetch user groups** is selected, users who have groups listed in this field will not be added to Axonius. If **Fetch user groups** is not selected, this field has no effect. The contents of this field are comma-separated strings, which are case and space sensitive.
35. **User groups include list** - When you enter the names of specific user groups in this field, only users who belong to those groups  are included in the fetch.
36. **Fetch nested groups** - Select to fetch groups that belong to other groups.
37. **Fetch device groups** - Select this option to fetch information on every Entra ID group for every device.
38. **Fetch group app roles** *(default: False)* - Set this option to fetch group app.roles and present the applications that are being used as an asset of the type Group. Refer to [List appRoleAssignments granted to a group](https://learn.microsoft.com/en-us/graph/api/group-list-approleassignments?view=graph-rest-1.0\&tabs=http) for further information.

<Callout icon="📘" theme="info">
  Note:

  When this setting is enabled, you must have the `Directory.Read.All` or the `AppRoleAssignment.ReadWrite.All` permission.
</Callout>

39. **Fetch group extra attributes** - Add any of the following additional group attributes that you want the adapter to fetch:
    1. `allowExternalSenders`
    2. `autoSubscribeNewMembers`
    3. `hideFromAddressLists`
    4. `hideFromOutlookClients`
    5. `isSubscribedByMail`
    6. `unseenCount`
40. **Fetch only devices**- Select this option to fetch only devices and not users. Only `Device.Read.All` permissions are required here, and the permission `Directory.Read.All` is not required.
41. **Fetch only devices with last seen** - Select this option to only fetch devices which have last seen.
42. **Fetch mobile devices** *(required, default: true)* - Select whether to fetch iOS and Android devices.
43. **Populate Cloud Provider Account Name aggregated field** *(required, default: true)* - When this parameter is not set, the "Cloud Provider Account Name" aggregated field is not populated for devices for Entra ID.
44. **Fetch Device Local Credentials (LAPS) from BETA Graph API** - Select between the following options:
    1. **Disabled** - Do not fetch device local credentials.
    2. **Fetch only basic information** — Fetch information about the local administrator credential information for all device objects that are enabled with Local Admin Password Solution (LAPS).
    3. **Fetch full information including the password (sensitive data)** - Fetch basic information in addition to password information. Note that password is considered sensitive information.
45. **Fetch Device Information Protection - Bitlocker Recovery Key** *(default disabled)*- You can select to fetch **Basic Information** or **Full Information** (including sensitive data) about Bitlocker Recovery Key for all device objects that have a stored Bitlocker key.

<Callout icon="📘" theme="info">
  Note

  When this setting is enabled, you must have the `BitlockerKey.ReadBasic.All` permission.
</Callout>

46. **Allow use of BETA API endpoints** - Select whether Axonius will use Beta API as the default data source.

<Callout icon="📘" theme="info">
  Note:

  This setting requires enabling the following [application permissions](/docs/microsoft-azure-active-directory-ad#set-permissions) to view the last sign-in audit log information:

  * `AuditLog.Read.All`

  * `Directory.Read.All`
</Callout>

47. **Exclude Azure AD joined devices** - Select this option to exclude Entra ID joined devices from data fetched by this adapter.
48. **Do not fetch devices if Device Disabled field equals Yes** *(optional)* - Select this option to exclude disabled devices from the fetch.
49. **Custom filter expression for fetching devices** *(optional)* - Enter a filter expression to exclude Entra ID devices from the fetch. For example, you could enter `(operatingSystem ne ‘Windows’)`. For more information, see [Operators and Functions Supported in $filter Expressions](https://learn.microsoft.com/en-us/graph/filter-query-parameter),[Advanced query capabilities on Microsoft Entra ID objects](https://learn.microsoft.com/en-us/graph/aad-advanced-queries?tabs=http), and [Device Properties](https://learn.microsoft.com/en-us/graph/api/resources/device?view=graph-rest-1.0#properties).
50. **Avoid duplications in names** - Select whether to create only one device when you fetch entities from Entra ID that contain the same name multiple times. In this case create only one device in Axonius using the name with the most recent last seen properties.
51. **Fetch device owner** - Select this option to fetch device ownership (username and email) information for this adapter.
52. **Fetch extension attributes for device owner** - Select this option to fetch additional extension attributes for the device owner user. This setting requires the ‘Fetch device owner’ setting to be enabled as well.
53. **Use asset name as hostname if hostname undefined** - Select this option so that if the hostname value is not defined, the hostname for each device will take the asset name as its value.
54. **Fetch devices from Intune** *(required, default: true)* - Select whether to fetch devices from Intune. Enabling this option will create two adapter connections, one for the Azure AD record and one for the Intune record.

<Callout icon="📘" theme="info">
  Note:

  When this setting is selected, you must have the following permissions: `DeviceManagementApps.Read.All`, `DeviceManagementConfiguration.Read.All`, `DeviceManagementManagedDevices.Read.All`, `DeviceManagementServiceConfig.Read.All`, and `Directory.Read.All`.
</Callout>

55. **Use Beta API in Intune** - Select to use the beta API to fetch Intune devices and additional data. If this option is cleared, the regular API is used.
56. **Fetch Cloud PCs** - Select to fetch Cloud PCs as Intune devices. To enable this option, the application permission `CloudPC.Read.All` is required.
57. **Fetch Apple enrolled devices** - Select this option to fetch enrolled Apple devices from the BETA API endpoint.
    * **Parse device serial number as asset name** - Select this option to parse the serial number of Apple devices as the Asset Name.
58. **Fetch autopilot device identities from Intune** - Select to enrich devices with autopilot information.
59. **Custom filter expression for fetching Intune devices** *(optional)* - Enter a filter expression to exclude Intune devices from the fetch. For more information, see [Operators and Functions Supported in $filter Expressions](https://learn.microsoft.com/en-us/graph/filter-query-parameter),[Advanced query capabilities on Microsoft Entra ID objects](https://learn.microsoft.com/en-us/graph/aad-advanced-queries?tabs=http), and [Intune Managed Device Properties](https://learn.microsoft.com/en-us/graph/api/resources/intune-devices-manageddevice?view=graph-rest-1.0#properties).
60. **Intune OS filter** - Select this option to filter the Intune devices fetched by *Operating System*. The default value is *All*. You can choose to only fetch Windows devices.
61. **Fetch Intune device extra attributes** - Select any of the following extra attributes to fetch for Intune devices.
    1. `activationLockBypassCode`
    2. `remoteAssistanceSessionUrl`
    3. `iccid`
    4. `udid`
    5. `notes`
    6. `physicalMemoryInBytes`
62. **Fetch software information from Intune** *(required, default: Disabled)* - Select whether to fetch installed software from Intune. The options are:
    1. *Disabled* - No installed software is fetched from Intune.
    2. *Device Management API (Foreground)* - Fetches installed software from Intune during the regular fetch time.
    3. *Device Management API (Background)* - Schedules the fetch of installed software from Intune outside the regular fetch time.
    4. *Exported Report (Background) -* Downloads an exported report from Entra ID, and saves the data to the DB instead of calling the Managed Devices API. **This option is most recommended.**
    5. *Exported Report (Foreground)* - Fetches Intune software using exported reports in foreground mode. This option runs the export during the normal fetch process instead of in the background. Note that Foreground fetch might increase the overall fetch time compared to background options.

<Callout icon="📘" theme="info">
  Note

  When **Fetch software information from Intune** is enabled, you must have the following permissions: `DeviceManagementApps.Read.All`, `DeviceManagementConfiguration.Read.All`, `DeviceManagementManagedDevices.Read.All`, `DeviceManagementServiceConfig.Read.All`, `Directory.Read.All`, and `Reports.Read.All`.
</Callout>

63. **Enrich Intune devices with enrollment profile information** - Select this option to fetch the enrollment profile information for Intune devices.
64. **Fetch Windows Defender Compliance state** - Select this option to collect “Windows10CompliancePolicy.DefenderEnabled” Compliance state for any Intune device to the ”Windows 10 Defender Enabled State” field of the adapter.
65. **Enrich Intune devices with hardware information** - Select to enrich Intune devices with their hardware information.
66. **Fetch Encryption Details from BETA Intune API** *(required, default false*) - Select this option to fetch more detailed data about the encryption state of devices (states that indicate if a device is encrypted, if it has encryption policies, etc.) from the [Managed Device Encryption State](https://learn.microsoft.com/en-us/graph/api/intune-deviceconfig-manageddeviceencryptionstate-list?view=graph-rest-beta) endpoint.
    * To fetch this data, your user account must include Beta and Intune licenses.
    * The Azure account must be granted `DeviceManagementConfiguration` permissions.
    * The ‘Fetch devices from Intune’ configuration must be enabled.
67. **Fetch Windows Endpoint Protection Configuration from BETA Intune API** - Select this option to fetch Windows Endpoint Protection Configuration.
68. **Fetch Device Compliance Policies Details** *(required, default false)* - Select this option to fetch information about the states of the compliance policies (Requires Intune License).
69. **Compliance policies date limit (months)** - Enter the number of months for which compliance policies are fetched based on their creation date.
70. **Fetch Security Baseline Device States** - Select this option to allow for enriching Intune devices with their Security Baseline states.
71. **Fetch Device Configuration Policy Reports** - Fetch the device's configuration policy report. With this data, it's possible to check the status of a policy, view the devices assigned to the policy
72. **Fetch Device Configuration Statuses** - Select this option to fetch all configurations for the devices and whether the devices are compliant with the configurations.
73. **Enrich mobile devices from Intune with application data** - Select this option to enrich mobile devices from Intune with application data.
74. **Enrich devices from Intune with Windows Update Distribution Report** - Select this option to fetch additional report information from Microsoft Intune Admin Center and Windows Quality Update Distribution.
75. **Fetch UCClient from Log Analytics (Requires Log Analytics Workspace ID)** - Enter workspace IDs to fetch UCClient data about Intune patches from Log Analytics.
76. **Fetch users Last Sign-In - How to fetch** *(required, default Disabled*) - Define how to fetch the data about the users Last Sign-in.
    * When set to 'Disabled' no data about users last sign in is fetched.
    * 'Enabled in Normal Fetch' fetches the information for successful sign-ins during the regular fetch time.
    * 'Enabled in Background' schedules the fetch of information for successful sign-ins outside the regular fetch time.
    * 'Enabled in Normal Fetch (login errors included)' fetches all sign-in information during the regular fetch time.
    * 'Enabled in Background (login errors included)’ schedules the fetch of all sign-in information outside the regular fetch time.

<Callout icon="📘" theme="info">
  Note

  When this setting is selected, you must have the `AuditLog.Read.All` and `Device.Read.All` permissions.
</Callout>

78. **Fetch audit logs** *(only for Users with Axonius SaaS Applications)* - Select this option to fetch audit logs. You need to enable this option in order to populate fields such as the Assigned Application: Last Access', ‘Inactive operational users’, and other fields that will show you information about SaaS application usage.
79. **Fetch Conditional Access Policies** - Select this option to fetch the conditions created or enforced by the Entra ID configuration.
80. **Fetch Device Configuration Policy Settings for Bitlocker** - Select this option to fetch device configuration policy settings for Bitlocker and save them as configurations in Axonius.
81. **Fetch all directory roles** - Select this option to fetch all directory roles.
82. **Fetch all role definitions** - Select this option to fetch all the available roles in Entra ID, even those that are not in use.
83. **Fetch app registrations secrets** - Select this option to fetch all app registrations secrets
84. **Fetch user extensions**  *(only for Users with Axonius SaaS Applications)*  - Select this option to fetch user extensions and app roles. When you select this option you will see information from this adapter about extensions that Entra ID is granted permissions to.
85. **Fetch service principal as Users** *(default false*) - Select this option to fetch service principals.

<Callout icon="📘" theme="info">
  Note

  When this setting is enabled, the adapters also fetch certificates from the service principals.
</Callout>

86. **Fetch Enterprise Applications Provisioning status** - Select this option to fetch the provisioning status of applications and user extensions: Provisioning Is Enabled or Provisioning Is Supported.

<Callout icon="📘" theme="info">
  Note

  When this setting is enabled, you must have the `Synchronization.Read.All` permission.
</Callout>

87. **Fetch applications that do not require assignment** - Select this option to fetch applications that are available for all the users in your Entra ID.
88. **Fetch only applications with preferred SSO mode as** *(optional)* - To filter which applications are included in the fetch by their preferred SSO mode, Enter the SSO modes you want to filter by.
89. **Fetch claims policy for enterprise applications** - Select this option to fetch claims policy for enterprise applications.

<Callout icon="📘" theme="info">
  Note

  When this setting is enabled, you must have the `Policy.ReadWrite.Configuration` permission.
</Callout>

90. **Fetch Application Settings** *(only for Users with Axonius SaaS Applications)* - Select this option to fetch general Entra ID license information and admin application settings, such as authentication policy settings or notification settings. (To fetch this information you need to configure the [User name and Password](/docs/microsoft-azure-active-directory-ad#create-a-user-account) fields. If 2FA is required for this application, the [2FA key](/docs/microsoft-azure-active-directory-ad#enable-or-exclude-multifactor-authentication) must be provided.)
91. **Number of parallel requests** *(optional, default: 100)* - Specify the maximum number of parallel requests to obtain paged data from the Microsoft Entra ID cloud server.
92. **Max retry count for parallel requests** *(optional, default: 3)* - Specify how many times this adapter will retry a parallel request when the Microsoft Entra ID cloud server returns a response with an error. If not supplied, Axonius will use the default value.
93. **Time in seconds to wait between retries of parallel requests** *(optional, default: 3)* - Specify how many seconds this adapter will wait in between each retry when a parallel request to the Microsoft Entra ID cloud server returns a response with an error. If not supplied, Axonius will use the default value.
94. **Enable real-time asset updates (Supported events: New users, New groups, Group members changes)** - Select this option to fetch new users, new groups, and new group members from the last time interval and trigger their respective events. All workflows configured with these events are then triggered.

<br />

## Axonius SaaS Applications Best Practices

In order to fetch Axonius SaaS Applications data set the following:

* Fetch all role definitions
* Fetch user application role details
* Fetch audit logs
* Fetch user extensions (service principal)