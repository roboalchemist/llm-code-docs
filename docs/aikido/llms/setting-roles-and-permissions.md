# Source: https://help.aikido.dev/getting-started/automated-user-management/setting-roles-and-permissions.md

# Setting Roles and Permissions

## Roles and Permissions Logic <a href="#roles-and-permissions-logic" id="roles-and-permissions-logic"></a>

Aikido offers three distinct user roles (**admins**, **default** and **team-only** users) to manage access and permissions effectively. Default and team-only users can have **standard editing rights** or can be **read-only**.

| Role                | Access Level                                                 |
| ------------------- | ------------------------------------------------------------ |
| **Admins**          | Full access                                                  |
| **Default Users**   | <p>Global / All Teams</p><p>Standard rights or read-only</p> |
| **Team-Only Users** | <p>Team-specific</p><p>Standard rights or read-only</p>      |

### Default Users vs Team-Only Users <a href="#default-users-vs-team-only-users" id="default-users-vs-team-only-users"></a>

The main difference between the two is that team-only users only have access to those issues for the teams they belong to. They still are able to mostly manage issues.

| Permission                                                                           | Default Users | Team-Only Users                                       |
| ------------------------------------------------------------------------------------ | ------------- | ----------------------------------------------------- |
| <p><strong>Issue Actions</strong></p><p>Snooze, ignore, severity change, autofix</p> | ✅             | ✅                                                     |
| **Create Tasks**                                                                     | ✅             | ✅                                                     |
| **Add Repos**                                                                        | ✅             | ❌                                                     |
| **Add Container Registries**                                                         | ✅             | ❌                                                     |
| **Add Domains**                                                                      | ✅             | Connected to repos only. No standalone.               |
| **Export Issues**                                                                    | ✅             | ❌                                                     |
| **Pentests**                                                                         | ✅             | ❌                                                     |
| **Code Quality**                                                                     | ✅             | ❌                                                     |
| **Zen Firewall**                                                                     | ✅             | ❌                                                     |
| **Acces to Settings**                                                                | All settings  | General Settings **Only**                             |
| **Acces to Reports**                                                                 | All Reports   | Trends Over Time, Licenses & SBOM and Malware Monitor |

### Advanced Rights for Users with Standard Rights <a href="#advanced-rights-for-users-with-standard-rights" id="advanced-rights-for-users-with-standard-rights"></a>

Aikido has an extra layer of permissions that can be enabled or disabled (both for default and team-only users). This is helpful in case you still want users to be able to execute certain actions. **Read-only rights block all possible actions.**

**Configurable for Default and Team-Only**

* **Snooze/Ignore Issues**: Ability to temporarily or permanently dismiss issues.
* **Change Issue Severity**: Ability to modify the severity level of issues.
* **Can export data:** Ability to export csv reports of vulnerability issues.

**Limited to Default Users**

* **Manage Teams**: Ability to manage team settings and membership.
* **Manage Repositories:** Ability to change branch, set multi-branch scanning and manage custom SAST rules.
* **Manage Clouds:** Ability to add and configure clouds
* **Manage Containers:** Ability to add and configure containers
* **Manage Domains:** Ability to add and configure domains
* **Manage Pentests:** Ability to run and configure pentests
* **Manage Code Quality Rules:** Ability to add and configure Code Quality Rules & manage code context

## How to change roles and permissions <a href="#how-to-change-roles-and-permissions" id="how-to-change-roles-and-permissions"></a>

**Step 1.** Go to the user overview in your settings

**Step 2.** Click the triple dots to open up the role and permissions modal for a specific user

<div data-with-frame="true"><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-cf4b7f2e0972adf8d7be8edaf5ef9bdf997710d3%2Fsetting-roles-and-permissions_3666ec2a-c91c-473f-9352-6c191c51c09b.png?alt=media" alt="" width="563"></div>

**Step 3.** Set the preferred user role and permissions

<div data-full-width="false" data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FzO5WoAYz5yzDF85TIZ0c%2FScreenshot%202025-11-17%20at%2021.47.17.png?alt=media&#x26;token=452bae16-f9a7-43ed-a7f7-152ae3f884e7" alt=""><figcaption></figcaption></figure></div>
