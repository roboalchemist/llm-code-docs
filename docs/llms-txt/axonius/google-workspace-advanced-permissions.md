# Source: https://docs.axonius.com/docs/google-workspace-advanced-permissions.md

# Google Workspace Advanced Permissions

## OAuth Scopes

The following tables summarize all OAuth scopes and permissions required for the Google Workspace adapter in Axonius.

### Google Cloud APIs to Enable

| API                            | When to Enable                   | Required For Scopes                                        |
| ------------------------------ | -------------------------------- | ---------------------------------------------------------- |
| Admin SDK API                  | Always                           | All `admin.directory.*` and `admin.reports.*` scopes       |
| Cloud Identity API             | If using Cloud Identity features | `cloud-identity.devices.readonly`, `cloud-identity.groups` |
| Chrome Management API          | If enriching browser extensions  | `chrome.management.reports.readonly`                       |
| Chrome Policy API              | If enriching browser policies    | `chrome.management.policy.readonly`                        |
| Google Calendar API            | If fetching calendars            | `calendar`                                                 |
| Groups Settings API            | If fetching group settings       | `apps.groups.settings`                                     |
| Service Usage API              | If fetching usage reports        | `admin.reports.usage.readonly`                             |
| Enterprise License Manager API | If fetching licenses             | `apps.licensing`                                           |

### Permissions for Connection Settings

**Additional permissions**

| Connection Name              | Scope                                            | API                |
| :--------------------------- | :----------------------------------------------- | :----------------- |
| Get OAuth Apps               | `admin.directory.user.security`                  | Admin SDK API      |
| Fetch Cloud Identity Devices | `cloud-identity.devices.readonly`                | Cloud Identity API |
| Fetch Chrome Browsers        | `admin.directory.device.chromebrowsers.readonly` | Admin SDK API      |
| Fetch Calendars              | `calendar`                                       | Google Calendar AP |

### Permissions for Advanced Configurations

| Configuration Name                | Scope                                      | API                               |
| :-------------------------------- | :----------------------------------------- | :-------------------------------- |
| Fetch MDM Devices                 | `admin.directory.device.mobile.readonly`   | Admin SDK API                     |
| Fetch ChromeOS Devices            | `admin.directory.device.chromeos.readonly` | Admin SDK API                     |
| Fetch user groups                 | `admin.directory.group.readonly`           | Admin SDK API                     |
| Enrich Groups settings            | `apps.groups.settings`                     | Groups Settings API               |
| Fetch user roles                  | `admin.directory.rolemanagement.readonly`  | Admin SDK API                     |
| Fetch Disk Usage                  | `admin.reports.usage.readonly`             | Admin SDK API + Service Usage API |
| Fetch Licenses                    | `apps.licensing`                           | Enterprise License Manager API    |
| Fetch User Audit Logs             | `admin.reports.audit.readonly`             | Admin SDK API                     |
| Fetch Extensions                  | `chrome.management.reports.readonly`       | Chrome Management API             |
| Fetch Settings (Policies)         | `chrome.management.policy.readonly`        | Chrome Policy API                 |
| Fetch Cloud Identity Device Users | `cloud-identity.devices.readonly`          | Cloud Identity API                |
| Fetch Applications (OAuth)        | `admin.directory.user.security`            | Admin SDK API                     |

#### Scopes to Copy and Paste

These are the scopes that you can copy and paste.

**Minimum Scopes to Copy**

```
https://www.googleapis.com/auth/admin.directory.user.readonly,
https://www.googleapis.com/auth/admin.directory.device.mobile.readonly,
https://www.googleapis.com/auth/admin.directory.device.chromeos.readonly
```

**Recommended for Standard Use to Copy**

```
https://www.googleapis.com/auth/admin.directory.user.readonly,
https://www.googleapis.com/auth/admin.directory.device.mobile.readonly,
https://www.googleapis.com/auth/admin.directory.device.chromeos.readonly,
https://www.googleapis.com/auth/admin.directory.device.chromebrowsers.readonly,
https://www.googleapis.com/auth/admin.directory.group.readonly,
https://www.googleapis.com/auth/admin.directory.customer.readonly,
https://www.googleapis.com/auth/admin.directory.domain.readonly,
https://www.googleapis.com/auth/cloud-identity.devices.readonly,
https://www.googleapis.com/auth/admin.reports.usage.readonly,
https://www.googleapis.com/auth/apps.groups.settings
```

**All Cyber Asset Scopes with Axonius SaaS Application to Copy**

```
https://www.googleapis.com/auth/admin.directory.user.readonly,
https://www.googleapis.com/auth/admin.directory.device.mobile.readonly,
https://www.googleapis.com/auth/admin.directory.device.chromeos.readonly,
https://www.googleapis.com/auth/admin.directory.device.chromebrowsers.readonly,
https://www.googleapis.com/auth/admin.directory.group.readonly,
https://www.googleapis.com/auth/admin.directory.customer.readonly,
https://www.googleapis.com/auth/admin.directory.domain.readonly,
https://www.googleapis.com/auth/cloud-identity.devices.readonly,
https://www.googleapis.com/auth/admin.reports.usage.readonly,
https://www.googleapis.com/auth/apps.groups.settings,
https://www.googleapis.com/auth/admin.directory.rolemanagement.readonly,
https://www.googleapis.com/auth/admin.directory.user.security,
https://www.googleapis.com/auth/admin.reports.audit.readonly,
https://www.googleapis.com/auth/calendar,
https://www.googleapis.com/auth/cloud-identity.groups,
https://www.googleapis.com/auth/chrome.management.reports.readonly,
https://www.googleapis.com/auth/chrome.management.policy.readonly,
https://www.googleapis.com/auth/chat.admin.spaces
```

<br />

### Enforcement Center Actions (Write Scopes)

| Enforcement Area   | Scope                                   | Purpose                                              |
| ------------------ | --------------------------------------- | ---------------------------------------------------- |
| User management    | `admin.directory.user`                  | Add, remove, suspend users, change OU, reset cookies |
| Group management   | `admin.directory.group`                 | Add/remove users from groups                         |
| Role management    | `admin.directory.rolemanagement`        | Create/delete role assignments                       |
| Send Chat messages | `chat.messages.create`                  | Send Google Chat messages                            |
| Browser management | `admin.directory.device.chromebrowsers` | Move Chrome browsers to OU                           |
| Device management  | `cloud-identity.devices`                | Delete Cloud Identity devices                        |