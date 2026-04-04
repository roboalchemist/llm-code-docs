# Source: https://firebase.google.com/docs/firestore/enterprise/security/iam.md.txt

<br />

Manage access to your resources with Identity and Access Management (IAM). IAM lets you give more granular access to specificGoogle Cloudresources and prevents unwanted access to other resources. This page describes the IAM permissions and roles forCloud Firestore. For a detailed description of IAM, read the[IAM documentation](https://cloud.google.com/iam/docs/).

IAM lets you adopt the[security principle of least privilege](https://wikipedia.org/wiki/Principle_of_least_privilege), so you grant only the necessary access to your resources.

IAM lets you control**who (user)** has**what (role)** permission for**which** resources by setting IAM policies. IAM policies grant one or more roles to a user, giving the user certain permissions. For example, you can grant the`datastore.indexAdmin`role to a user, which allows the user to create, modify, delete, list, or view indexes.

## Permissions and roles

This section summarizes the permissions and roles thatCloud Firestoresupports.
| **Note:** SomeCloud Firestorepermissions differ from the standard IAM model permissions. For example, in the IAM model, the`datastore.databases.get`permission lets you return a database object while, inCloud Firestore,`datastore.databases.get`lets you begin or roll back a transaction. To retrieve a database object's information, use the`datastore.databases.getMetadata`permission.

### Required permissions for API methods

The following table lists the permissions that the caller must have to perform each action:

|                                                   Method                                                    |                                                                                         Required permissions                                                                                         |
|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `projects.databases.MongoDBCompatible`                                                                                                                                                                                                                                                                            ||
| `ListDatabases`                                                                                             | `datastore.databases.getMetadata`                                                                                                                                                                    |
| `ListIndexes`                                                                                               | `datastore.indexes.list`                                                                                                                                                                             |
| `Find`                                                                                                      | `datastore.entities.get` `datastore.entities.list`                                                                                                                                                   |
| `Aggregate`                                                                                                 | `datastore.entities.get` `datastore.entities.list`                                                                                                                                                   |
| `GetMore`                                                                                                   | The same permissions that were required by the call that created the cursor.                                                                                                                         |
| `ListCollections`                                                                                           | `datastore.entities.list`                                                                                                                                                                            |
| `Count`                                                                                                     | `datastore.entities.list`                                                                                                                                                                            |
| `Distinct`                                                                                                  | `datastore.entities.get` `datastore.entities.list`                                                                                                                                                   |
| `CommitTransaction`                                                                                         | `datastore.databases.get`                                                                                                                                                                            |
| `AbortTransaction`                                                                                          | `datastore.databases.get`                                                                                                                                                                            |
| `EndSessions`                                                                                               | `datastore.databases.get`                                                                                                                                                                            |
| `KillCursors`                                                                                               | `datastore.databases.get`                                                                                                                                                                            |
| `Insert`                                                                                                    | `datastore.entities.create`                                                                                                                                                                          |
| `Update`                                                                                                    | `datastore.entities.get` `datastore.entities.list` `datastore.entities.update` `datastore.entities.create`(for upsert only)                                                                          |
| `FindAndModify`                                                                                             | `datastore.entities.get` `datastore.entities.list` `datastore.entities.update`(for replace or update only) `datastore.entities.create`(for upsert only) `datastore.entities.delete`(for delete only) |
| `CreateCollection`                                                                                          | `datastore.entities.create`                                                                                                                                                                          |
| `projects.databases.indexes`                                                                                                                                                                                                                                                                                      ||
| [`create`](https://cloud.google.com/firestore/docs/reference/rest/latest/projects.databases.indexes/create) | `datastore.indexes.create`                                                                                                                                                                           |
| [`delete`](https://cloud.google.com/firestore/docs/reference/rest/latest/projects.databases.indexes/delete) | `datastore.indexes.delete`                                                                                                                                                                           |
| [`get`](https://cloud.google.com/firestore/docs/reference/rest/latest/projects.databases.indexes/get)       | `datastore.indexes.get`                                                                                                                                                                              |
| [`list`](https://cloud.google.com/firestore/docs/reference/rest/latest/projects.databases.indexes/list)     | `datastore.indexes.list`                                                                                                                                                                             |
| `projects.databases`                                                                                                                                                                                                                                                                                              ||
| [`create`](https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases/create)             | `datastore.databases.create`                                                                                                                                                                         |
| [`delete`](https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases/delete)             | `datastore.databases.delete`                                                                                                                                                                         |
| [`get`](https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases/get)                   | `datastore.databases.getMetadata`                                                                                                                                                                    |
| [`list`](https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases/list)                 | `datastore.databases.list`                                                                                                                                                                           |
| [`patch`](https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases/patch)               | `datastore.databases.update`                                                                                                                                                                         |
| restore                                                                                                     | `datastore.backups.restoreDatabase`                                                                                                                                                                  |
| [`clone`](https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases/clone)               | `datastore.databases.clone`                                                                                                                                                                          | Clone a database. If your`clone`request contains a`tags`value, then the following additional permissions are required: - `datastore.databases.createTagBinding` If you would like to verify whether the tag bindings are set successfully by listing the bindings, then the following additional permissions are required: - `datastore.databases.listTagBindings` - `datastore.databases.listEffectiveTags` |
| `projects.locations`                                                                                                                                                                                                                                                                                              ||
| [`get`](https://cloud.google.com/firestore/docs/reference/rest/v1/projects.locations/get)                   | `datastore.locations.get`                                                                                                                                                                            |
| [`list`](https://cloud.google.com/firestore/docs/reference/rest/v1/projects.locations/list)                 | `datastore.locations.list`                                                                                                                                                                           |
| `projects.databases.backupschedules`                                                                                                                                                                                                                                                                              ||
| `get`                                                                                                       | `datastore.backupSchedules.get`                                                                                                                                                                      |
| `list`                                                                                                      | `datastore.backupSchedules.list`                                                                                                                                                                     |
| `create`                                                                                                    | `datastore.backupSchedules.create`                                                                                                                                                                   |
| `update`                                                                                                    | `datastore.backupSchedules.update`                                                                                                                                                                   |
| `delete`                                                                                                    | `datastore.backupSchedules.delete`                                                                                                                                                                   |
| `projects.locations.backups`                                                                                                                                                                                                                                                                                      ||
| `get`                                                                                                       | `datastore.backups.get`                                                                                                                                                                              |
| `list`                                                                                                      | `datastore.backups.list`                                                                                                                                                                             |
| `delete`                                                                                                    | `datastore.backups.delete`                                                                                                                                                                           |
| `projects.databases.usercreds`                                                                                                                                                                                                                                                                                    ||
| `get`                                                                                                       | `datastore.userCreds.get`                                                                                                                                                                            |
| `list`                                                                                                      | `datastore.userCreds.list`                                                                                                                                                                           |
| `create`                                                                                                    | `datastore.userCreds.create`                                                                                                                                                                         |
| `enable`                                                                                                    | `datastore.userCreds.update`                                                                                                                                                                         |
| `disable`                                                                                                   | `datastore.userCreds.update`                                                                                                                                                                         |
| `resetPassword`                                                                                             | `datastore.userCreds.update`                                                                                                                                                                         |
| `delete`                                                                                                    | `datastore.userCreds.delete`                                                                                                                                                                         |

### Predefined roles

With IAM, every API method inCloud Firestorerequires that the account making the API request has the appropriate permissions to use the resource. Permissions are granted by setting policies that grant roles to a user, group, or service account. In addition to the primitive roles,[owner, editor, and viewer](https://cloud.google.com/iam/docs/understanding-roles#primitive_roles), you can grantCloud Firestoreroles to the users of your project.

The following table lists theCloud FirestoreIAM roles. You can grant multiple roles to a user, group, or service account.

|                  Role                   |                                                                                                                                                                                             Permissions                                                                                                                                                                                              |                                                                             Description                                                                              |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `roles/datastore.owner`                 | `appengine.applications.get` `datastore.*` `resourcemanager.projects.get` `resourcemanager.projects.list`                                                                                                                                                                                                                                                                                            | Full access toCloud Firestore.                                                                                                                                       |
| `roles/datastore.user`                  | `appengine.applications.get` `datastore.databases.get` `datastore.databases.getMetadata` `datastore.databases.list` `datastore.entities.*` `datastore.indexes.list` `datastore.namespaces.get` `datastore.namespaces.list` `datastore.statistics.get` `datastore.statistics.list` `resourcemanager.projects.get` `resourcemanager.projects.list`                                                     | Read/write access to data in aCloud Firestoredatabase. Intended for application developers and service accounts.                                                     |
| `roles/datastore.viewer`                | `appengine.applications.get` `datastore.databases.get` `datastore.databases.getMetadata` `datastore.databases.list` `datastore.entities.get` `datastore.entities.list` `datastore.indexes.get` `datastore.indexes.list` `datastore.namespaces.get` `datastore.namespaces.list` `datastore.statistics.get` `datastore.statistics.list` `resourcemanager.projects.get` `resourcemanager.projects.list` | Read access to allCloud Firestoreresources.                                                                                                                          |
| `roles/datastore.indexAdmin`            | `appengine.applications.get` `datastore.databases.getMetadata` `datastore.indexes.*` `datastore.operations.list` `datastore.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`                                                                                                                                                                                           | Full access to manage index definitions.                                                                                                                             |
| `roles/datastore.backupSchedulesViewer` | `datastore.backupSchedules.get` `datastore.backupSchedules.list`                                                                                                                                                                                                                                                                                                                                     | Read access to backup schedules in aCloud Firestoredatabase.                                                                                                         |
| `roles/datastore.backupSchedulesAdmin`  | `datastore.backupSchedules.get` `datastore.backupSchedules.list` `datastore.backupSchedules.create` `datastore.backupSchedules.update` `datastore.backupSchedules.delete` `datastore.databases.list` `datastore.databases.getMetadata`                                                                                                                                                               | Full access to backup schedules in aCloud Firestoredatabase.                                                                                                         |
| `roles/datastore.backupsViewer`         | `datastore.backups.get` `datastore.backups.list`                                                                                                                                                                                                                                                                                                                                                     | Read access to backup information in aCloud Firestorelocation.                                                                                                       |
| `roles/datastore.backupsAdmin`          | `datastore.backups.get` `datastore.backups.list` `datastore.backups.delete`                                                                                                                                                                                                                                                                                                                          | Full access to backups in aCloud Firestorelocation.                                                                                                                  |
| `roles/datastore.restoreAdmin`          | `datastore.backups.get` `datastore.backups.list` `datastore.backups.restoreDatabase` `datastore.databases.list` `datastore.databases.create` `datastore.databases.getMetadata` `datastore.operations.list` `datastore.operations.get`                                                                                                                                                                | Ability to restore aCloud Firestorebackup into a new database. This role also gives the ability to create new databases, not necessarily by restoring from a backup. |
| `roles/datastore.cloneAdmin`            | `datastore.databases.clone` `datastore.databases.list` `datastore.databases.create` `datastore.databases.getMetadata` `datastore.operations.list` `datastore.operations.get`                                                                                                                                                                                                                         | Ability to clone aCloud Firestoredatabase into a new database. This role also gives the ability to create new databases, not necessarily by cloning.                 |
| `roles/datastore.statisticsViewer`      | `resourcemanager.projects.get` `resourcemanager.projects.list` `datastore.databases.getMetadata` `datastore.insights.get` `datastore.keyVisualizerScans.get` `datastore.keyVisualizerScans.list` `datastore.statistics.list` `datastore.statistics.get`                                                                                                                                              | Read access to Insights, Stats, and Key Visualizer scans.                                                                                                            |
| `roles/datastore.userCredsViewer`       | `datastore.userCreds.get` `datastore.userCreds.list`                                                                                                                                                                                                                                                                                                                                                 | Read access to user credentials in aCloud Firestoredatabase.                                                                                                         |
| `roles/datastore.userCredsAdmin`        | `datastore.userCreds.get` `datastore.userCreds.list` `datastore.userCreds.create` `datastore.userCreds.update` `datastore.userCreds.delete` `datastore.databases.list` `datastore.databases.getMetadata`                                                                                                                                                                                             | Full access to user credentials in aCloud Firestoredatabase.                                                                                                         |

### Custom roles

If the predefined roles do not address your business requirements, you can define your own custom roles with permissions that you specify:

- [Learn about custom roles.](https://cloud.google.com/iam/docs/understanding-custom-roles)
- [Create and manage custom roles.](https://cloud.google.com/iam/docs/creating-custom-roles)

#### Required roles to create and manage tags

If any tag is represented in create or restore actions, some roles are required. See[Creating and managing tags](https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing)for more details on creating tag key-value pairs before associate them to the database resources.

The following listed permissions are required.

##### View tags

- `datastore.databases.listTagBindings`
- `datastore.databases.listEffectiveTags`

##### Manage tags on resources

The following permission is required for the database resource you're attaching the tag value.

- `datastore.databases.createTagBinding`

### Permissions

The following table lists the permissions thatCloud Firestoresupports.

|            Database permission name            |                                                 Description                                                  |   |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------|---|
| `datastore.databases.get`                      | Begin or rollback a transaction.                                                                             |   |
| `datastore.databases.getMetadata`              | Read metadata from a database.                                                                               |   |
| `datastore.databases.list`                     | List databases in a project.                                                                                 |   |
| `datastore.databases.create`                   | Create a database.                                                                                           |   |
| `datastore.databases.update`                   | Update a database.                                                                                           |   |
| `datastore.databases.delete`                   | Delete a database.                                                                                           |   |
| `datastore.databases.clone`                    | Clone a database.                                                                                            |   |
| `datastore.databases.createTagBinding`         | Create a tag binding for a database.                                                                         |   |
| `datastore.databases.deleteTagBinding`         | Delete a tag binding for a database.                                                                         |   |
| `datastore.databases.listTagBindings`          | List all tag bindings for a database.                                                                        |   |
| `datastore.databases.listEffectiveTagBindings` | List effective tag bindings for a database.                                                                  |   |
| `datastore.entities.create`                    | Create a document.                                                                                           |   |
| `datastore.entities.delete`                    | Delete a document.                                                                                           |   |
| `datastore.entities.get`                       | Read a document.                                                                                             |   |
| `datastore.entities.list`                      | List the names of documents in a project. (`datastore.entities.get`is required to access the document data.) |   |
| `datastore.entities.update`                    | Update a document.                                                                                           |   |
| `datastore.indexes.create`                     | Create an index.                                                                                             |   |
| `datastore.indexes.delete`                     | Delete an index.                                                                                             |   |
| `datastore.indexes.get`                        | Read metadata from an index.                                                                                 |   |
| `datastore.indexes.list`                       | List the indexes in a project.                                                                               |   |
| `datastore.indexes.update`                     | Update an index.                                                                                             |   |
| `datastore.operations.cancel`                  | Cancel a long-running operation.                                                                             |   |
| `datastore.operations.delete`                  | Delete a long-running operation.                                                                             |   |
| `datastore.operations.get`                     | Gets the latest state of a long-running operation.                                                           |   |
| `datastore.operations.list`                    | List long-running operations.                                                                                |   |
| `resourcemanager.projects.get`                 | Browse resources in the project.                                                                             |   |
| `resourcemanager.projects.list`                | List owned projects.                                                                                         |   |
| `datastore.locations.get`                      | Get details about a database location. Required to create a new database.                                    |   |
| `datastore.locations.list`                     | List available database locations. Required to create a new database.                                        |   |
| `datastore.keyVisualizerScans.get`             | Get details about Key Visualizer scans.                                                                      |   |
| `datastore.keyVisualizerScans.list`            | List available Key Visualizer scans.                                                                         |   |
| `datastore.backupSchedules.get`                | Get details about a backup schedule.                                                                         |   |
| `datastore.backupSchedules.list`               | List available backup schedules.                                                                             |   |
| `datastore.backupSchedules.create`             | Create a backup schedule.                                                                                    |   |
| `datastore.backupSchedules.update`             | Update a backup schedule.                                                                                    |   |
| `datastore.backupSchedules.delete`             | Delete a backup schedule.                                                                                    |   |
| `datastore.backups.get`                        | Get details about a backup.                                                                                  |   |
| `datastore.backups.list`                       | List available backups.                                                                                      |   |
| `datastore.backups.delete`                     | Delete a backup.                                                                                             |   |
| `datastore.backups.restoreDatabase`            | Restore a database from a backup.                                                                            |   |
| `datastore.insights.get`                       | Get insights of a resource                                                                                   |   |
| `datastore.userCreds.get`                      | Get details about user credentials.                                                                          |   |
| `datastore.userCreds.list`                     | List available user credentials.                                                                             |   |
| `datastore.userCreds.create`                   | Create user credentials.                                                                                     |   |
| `datastore.userCreds.update`                   | Enable or disable user credentials, or reset a user password.                                                |   |
| `datastore.userCreds.delete`                   | Delete user credentials.                                                                                     |   |

## Role change latency

Cloud Firestorecaches IAM permissions for 5 minutes, so it takes up to 5 minutes for a role change to become effective.

## ManagingCloud FirestoreIAM

You can get and set IAM policies using the Google Cloud console, the IAM API, or the`gcloud`command-line tool. See[Granting, Changing, and Revoking Access to Project Members](https://cloud.google.com/iam/docs/granting-changing-revoking-access)for details.

## Configure conditional access permissions

You can use[IAM Conditions](https://cloud.google.com/iam/docs/conditions-overview)to define and enforce conditional access control.

For example, the following condition assigns a principal the`datastore.user`role up until a specified date:  

    {
      "role": "roles/datastore.user",
      "members": [
        "user:travis@example.com"
      ],
      "condition": {
        "title": "Expires_December_1_2023",
        "description": "Expires on December 1, 2023",
        "expression":
          "request.time < timestamp('2023-12-01T00:00:00.000Z')"
      }
    }

To learn how to define IAM Conditions for temporary access, see[Configure temporary access](https://cloud.google.com/iam/docs/configuring-temporary-access).

To learn how to configure IAM Conditions for access to one or more databases, see[Configure database access conditions](https://firebase.google.com/docs/firestore/enterprise/create-databases#configure_per-database_access_permissions).

## What's next

- Learn more about[IAM](https://cloud.google.com/iam/docs/).
- [Grant IAM roles](https://cloud.google.com/iam/docs/granting-changing-revoking-access).
- Learn about[authentication](https://firebase.google.com/docs/firestore/enterprise/connect).