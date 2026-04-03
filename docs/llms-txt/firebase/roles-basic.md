# Source: https://firebase.google.com/docs/projects/iam/roles-basic.md.txt

**Basic roles**(Owner, Editor, and Viewer) are fundamental roles for IAM and include different levels of access permissions for all the Firebase products and services.

The following table summarizes the permissions included in each role. Learn more about[basic roles](https://cloud.google.com/iam/docs/understanding-roles#basic)in theGoogle Clouddocumentation.

Note that basic roles were formerly called "primitive" roles.

Assign these roles to project members using the[Firebaseconsole](https://console.firebase.google.com/project/_/settings/iam)or the[Google Cloudconsole](https://console.cloud.google.com/iam-admin/iam).
| **Note:** Assigning roles using theGoogle Cloudconsole is helpful if you don't have access to open the Firebase project via theFirebaseconsole (for example, you're the administrator of the project's Google Cloud organization).

|           Role            |                                                                                                                     Permissions                                                                                                                      |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Viewer** `roles/viewer` | Permissions for read-only actions, such as viewing (but not modifying) existing resources or data.                                                                                                                                                   |
| **Editor** `roles/editor` | All the Viewer role permissions,**plus** permissions for actions that modify state, such as changing existing resources.**Note:** The`roles/editor`role contains permissions to create and delete resources for most Firebase products and services. |
| **Owner** `roles/owner`   | All the Editor role permissions,**plus** permissions for the following actions: - Manage roles and permissions for a project and all resources within the project. - Set up billing for a project. - Delete or restore a project.                    |

## Importance of assigning the Owner role

To ensure proper management of a Firebase project, it must have an[Owner](https://firebase.google.com/docs/projects/iam/roles-basic).

Project members with the Owner role are**often the*only*project members who can do administrative tasks or receive important notifications**:

- Project members with the Owner role are often the only members who can perform important administrative actions (like assigning roles and managingGoogle Analyticsproperties), and Firebase Support can only fulfill administrative requests from demonstrated project Owners.
- Project members with the Owner role are often the only members who (by default) receive notifications about changes to the project or products (like billing and legal changes, deprecations of features, etc.). You can optionally[customize your project's "essential contacts"](https://cloud.google.com/resource-manager/docs/managing-notification-contacts)if you want specific or additional project members to receive notifications.

After you set up the Owner(s) for a Firebase project, it's important to keep those assignments up-to-date.

Note that if a Firebase project is part of aGoogle Cloudorganization, the person who manages yourGoogle Cloudorganization can perform many tasks that an Owner can do. However, for several Owner-specific tasks (like assigning roles or managingGoogle Analyticsproperties), the administrator may need to assign themselves the[actual Owner role](https://firebase.google.com/docs/projects/iam/roles-basic)to perform those tasks.