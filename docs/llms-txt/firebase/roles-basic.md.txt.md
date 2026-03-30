# Source: https://firebase.google.com/docs/projects/iam/roles-basic.md.txt

# Owner, Editor, and Viewer roles

**Basic roles** (Owner, Editor, and Viewer) are fundamental roles for IAM
and include different levels of access permissions for all the Firebase products
and services.

The following table summarizes the permissions included in each role. Learn more
about [basic roles](https://cloud.google.com/iam/docs/roles-overview#basic)
in the Google Cloud documentation.

Note that basic roles were formerly called "primitive" roles.

Assign these roles to project members using the
[Firebase console](https://console.firebase.google.com/project/_/settings/iam)
or the
[Google Cloud console](https://console.cloud.google.com/iam-admin/iam).

> [!NOTE]
> **Note:** Assigning roles using the Google Cloud console is helpful if you don't have access to open the Firebase project via the Firebase console (for example, you're the administrator of the project's Google Cloud organization).

| Role | Permissions |
|---|---|
| **Viewer** `roles/viewer` | Permissions for read-only actions, such as viewing (but not modifying) existing resources or data. |
| **Editor** `roles/editor` | All the Viewer role permissions, **plus** permissions for actions that modify state, such as changing existing resources. > [!NOTE] > **Note:** The `roles/editor` role contains permissions to create and delete resources for most Firebase products and services. |
| **Owner** `roles/owner` | All the Editor role permissions, **plus** permissions for the following actions: - Manage roles and permissions for a project and all resources within the project. - Set up billing for a project. - Delete or restore a project. |

## Importance of assigning the Owner role

To ensure proper management of a Firebase project, it must have an
[Owner](https://firebase.google.com/docs/projects/iam/roles-basic).

Project members with the Owner role are
**often the *only* project members who can do administrative
tasks or receive important notifications**:

- Project members with the Owner role are often the only members who can perform important administrative actions (like assigning roles and managing Google Analytics properties), and Firebase Support can only fulfill administrative requests from demonstrated project Owners.
- Project members with the Owner role are often the only members who (by default) receive notifications about changes to the project or products (like billing and legal changes, deprecations of features, etc.). You can optionally [customize your project's "essential contacts"](https://cloud.google.com/resource-manager/docs/managing-notification-contacts) if you want specific or additional project members to receive notifications.

After you set up the Owner(s) for a Firebase project, it's important to
keep those assignments up-to-date.

Note that if a Firebase project is part of a Google Cloud organization, the
person who manages your Google Cloud organization can perform many tasks
that an Owner can do. However, for several Owner-specific tasks (like
assigning roles or managing Google Analytics properties), the
administrator may need to assign themselves the
[actual Owner role](https://firebase.google.com/docs/projects/iam/roles-basic) to perform
those tasks.