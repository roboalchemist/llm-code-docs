# Source: https://docs.pentaho.com/pdc-use/pdc-user-roles-and-permissions.md

# User roles and permissions in Data Catalog

Pentaho Data Catalog uses **role-based access control (RBAC)** to define what users can view, create, or manage in the catalog. By default, Data Catalog provides a set of predefined user roles that align with common responsibilities in data management and cataloging.

In addition to default roles, you can create **communities** to group users with similar responsibilities and tailor their access to specific data assets. Communities help you refine permissions for business areas or projects. For example, you can create a community for the Finance team that grants access only to financial glossaries and data sources. For more information, see **Communities in Data Catalog**.

Each user must be assigned at least one role or community when the account is created. You can assign multiple roles or communities to a user if the permissions do not overlap or originate from the same default role. When a user has multiple roles, either directly or through community membership, the **highest-level role** determines the user’s effective permissions.

{% hint style="info" %}
When a user belongs to multiple communities, Data Catalog combines the permissions from all assigned communities. If there are conflicts, the higher-level role or less restrictive permission takes precedence. This ensures that users retain the broadest level of access granted across their assigned communities.
{% endhint %}

Data Catalog supports two main user tiers: **Business Users**, who primarily view or explore data and business terms, and **Expert Users**, who create, ingest, or curate entities and metadata within the catalog. See [Default user roles and permissions](https://github.com/pentaho/documentation/blob/main/PDC/10.2/Use/pdc-user-roles-and-permissions.md#default-user-roles-and-permissions) for details on the permissions for users in each tier. Contact your sales representative if you have questions about this feature.

{% hint style="info" %}
Your software license determines user-based entitlement.
{% endhint %}

## Default user roles and permissions

Data Catalog provides default user roles with role-based permissions that enable administrators to control access as necessary across Data Catalog. These permissions are distributed across two tiers of licensed users: **Business Users** and **Expert Users**, as needed.

Administrators can also fine-tune access by creating communities of users to which they assign permissions, such as access to specific data source types or business glossaries. Administrators can further refine access by creating **communities**, which act as custom roles with additional or restricted permissions. Communities are useful when you need to limit access to specific asset types, such as particular data sources, glossaries, or policies.

Using a community, an administrator can grant or deny access to specific assets, such as business glossaries or data connections. For more information, see the [Manage users and permissions #Add a community](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ldc-manage-users-and-permissions-cp-ag#add-a-community "mention") topic under the [Manage users and permissions](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ldc-manage-users-and-permissions-cp-ag "mention") section in the [Administer Pentaho Data Catalog](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ "mention") guide.

All users, regardless of role, can comment on, rate, and receive notifications for assets they have permission to access. The following sections outline the permissions that are available in the tiered default roles.

### Business Users

The first tier of licensed users is **Business Users**. This tier includes two roles with different levels of access: **Business User** and **Data User**. The following table lists the default permissions for each role. For example, a user with the **Business User** role can view business glossaries and policies but cannot access data sources. The **Data User** role includes all Business User permissions and provides additional access to data assets that are relevant to the user's specific line of business.

{% hint style="info" %}
Data may be masked if it contains sensitive or confidential information.
{% endhint %}

| Role              | Permission Type       | Actions                                        |
| ----------------- | --------------------- | ---------------------------------------------- |
| **Business User** | Business Glossary     | View                                           |
|                   | Policies              | View                                           |
| **Data User**     | Applications          | View                                           |
|                   | Business Glossary     | View                                           |
|                   | Business Intelligence | View                                           |
|                   | Data Sources          | View, AddContent, DeleteContent, ViewDashboard |
|                   | Policies              | View                                           |

### Expert Users

The second tier of licensed users is Expert Users, which includes four roles with differing permissions.

**Note:** Your license limits the number of Expert Users to whom you can assign a Data Catalog role. When the number of your allowed Expert Users reaches 75% of the limit allowed by your license agreement, you see a warning message. You also receive a message if you have exceeded the quota.

#### Business Steward

Business Stewards focus on maintaining **business glossaries and governance policies**. They can create, update, and manage definitions and policies, but cannot modify data sources.

| Role                 | Permission Type       | Actions                                      |
| -------------------- | --------------------- | -------------------------------------------- |
| **Business Steward** | Applications          | View                                         |
|                      | Business Glossary     | View, Create, Update, Delete, Import, Export |
|                      | Business Intelligence | View                                         |
|                      | Data Sources          | View                                         |
|                      | Policies              | View, Create, Update, Delete, Import, Export |

#### **Data Steward**

Data Stewards are responsible for **data quality, profiling, and metadata curation**. They can create and manage data sources, define business and metadata rules, and run profiling or validation jobs.

| Role             | Permission Type                | Actions                                                                                                                                          |
| ---------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Data Steward** | Applications                   | View, Create, Update, Delete, Import, Export                                                                                                     |
|                  | Business Glossary              | View                                                                                                                                             |
|                  | Business Intelligence          | View                                                                                                                                             |
|                  | Business Rules                 | View, Create, Update, Delete, Import, Export                                                                                                     |
|                  | Data Identification Methods    | View, Create, Update, Delete, Import, Export                                                                                                     |
|                  | Data Sources                   | View, Create, Update, Delete, Import, Export, AddContent, ApplyRules, DeleteContent, RelationshipAssignment, RunJobs, ViewDashboard, ViewSamples |
|                  | Domain Asset                   | View, ApplyRules, ApproveRecords                                                                                                                 |
|                  | Match & Merge (Metadata) Rules | View, Modify                                                                                                                                     |
|                  | Policies                       | View                                                                                                                                             |
|                  | Reference Data                 | View, Create, Update, Delete, Import, Export, UpdateValues, ViewValues                                                                           |

#### **Admin**

Admins are responsible for **managing user accounts, roles, permissions, and system configuration.** They can view most assets but cannot create or edit business rules.

| Role      | Permission Type                | Actions                                                     |
| --------- | ------------------------------ | ----------------------------------------------------------- |
| **Admin** | Administration                 | View, Modify                                                |
|           | Applications                   | View                                                        |
|           | Business Glossary              | View                                                        |
|           | Business Intelligence          | View                                                        |
|           | Data Sources                   | View                                                        |
|           | Domain Asset                   | View, Modify, Export, ApplyRules, ApproveRecords, RunEngine |
|           | MDM Data Sources               | View, Modify                                                |
|           | Match & Merge (Metadata) Rules | View, Modify                                                |
|           | Policies                       | View                                                        |

#### **Data Storage Administrator**

Data Storage Administrators manage **storage utilization and optimization** across data sources, folders, and schemas. They monitor capacity, data temperature, business terms, and duplicate file analysis.

| Role                           | Permission Type             | Actions                                                                                                                                                               |
| ------------------------------ | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Data Storage Administrator** | Applications                | View                                                                                                                                                                  |
|                                | Business Glossary           | View                                                                                                                                                                  |
|                                | Business Intelligence       | View                                                                                                                                                                  |
|                                | Business Rules              | View, Create, Update, Delete, Import, Export                                                                                                                          |
|                                | Data Identification Methods | View, Create, Update, Delete, Import, Export                                                                                                                          |
|                                | Data Sources                | View, Create, ViewSamples, Update, RunJobs, ApplyRules, RelationshipsAssignment, Delete, Import, Export, AddContent, DeleteContent, ViewDashboard, ViewStorageReports |
|                                | Policies                    | View                                                                                                                                                                  |

#### **Data Developer**

Data Developers design and maintain **business rules, metadata rules, and data domain logic**. They typically work with structured metadata, reference data, and rule automation.

| Role               | Permission Type                | Actions                                                     |
| ------------------ | ------------------------------ | ----------------------------------------------------------- |
| **Data Developer** | Applications                   | View                                                        |
|                    | Business Glossary              | View                                                        |
|                    | Business Intelligence          | View                                                        |
|                    | Business Rules                 | View, Create, Update, Delete, Import, Export                |
|                    | Data Sources                   | View                                                        |
|                    | Domain Asset                   | View, Modify, Export, ApplyRules, ApproveRecords, RunEngine |
|                    | MDM Data Sources               | View, Modify                                                |
|                    | Match & Merge (Metadata) Rules | View, Modify                                                |
|                    | Policies                       | View                                                        |

### Communities in Data Catalog

**Communities** in Pentaho Data Catalog extend role-based access control (RBAC) by allowing administrators to manage access at a more granular level. A community groups users, who share similar responsibilities, projects, or business areas and assigns them customized permissions for specific catalog assets. Communities are useful when you want to limit or extend access within a department, project, or data domain without creating new global roles. For example, you can create a **Finance** community that grants analysts access only to finance-related data sources and glossaries, while members of other departments retain access to their respective assets.

Each community is based on an existing **default role**, such as *Business User* or *Data Steward*. Permissions from the base role are inherited, and you can fine-tune them by enabling or disabling actions for specific features. When you assign a user to a community:

* The user automatically inherits all permissions defined in the community.
* The user’s permissions combine with those from any other assigned roles or communities.
* If permissions conflict, the **highest-level role** or the **least restrictive permission** applies.

When a user belongs to multiple communities, Data Catalog merges permissions from all assigned communities. The resulting access level always reflects the most permissive combination of granted rights.

To know more about creating and managing communities, see [Manage users and permissions](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ldc-manage-users-and-permissions-cp-ag "mention") in the [Administer Pentaho Data Catalog](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ "mention") guide.

## Data Catalog permission types and actions

The following table lists the permission types and actions available in Pentaho Data Catalog. These permissions can be fine-tuned through communities to grant or restrict specific capabilities for selected users. A user’s base role determines the general level of access for each feature. When you create or edit a community, you can modify these permissions to extend or limit access beyond the default role settings.

For example, the **ViewSamples** action for data sources is available by default to users with the **Data Steward** role that allows them to view sample data for profiled columns. If you create a community based on this role, you can assign other users to that community to give them the same permission to view sample data for profiled columns.

{% hint style="info" %}
In the user interface, some actions appear as selectable checkboxes but cannot be performed, such as deleting a data source or a data identification method.
{% endhint %}

![Permissions table in add or edit community page](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-412702d2a68cb79eeefe881a1b490100fe4f9168%2FPDC%20Permissions%20table%20in%20Edit%20Community%20RBAC%3DGUID-8425F6E8-8D6C-40AE-B3C3-590727DC4065%3D1%3Den%3DLow.png?alt=media)

The permissions available for each Data Catalog feature are shown in the following table.

<table><thead><tr><th width="277.3333740234375">Permission type</th><th>Action</th></tr></thead><tbody><tr><td>Administration</td><td>Modify, View</td></tr><tr><td>Applications</td><td>Create, Delete, Export, Import, Update, View</td></tr><tr><td>Business Glossary</td><td>Create, Delete, Export, Import, Update, View</td></tr><tr><td>Business Intelligence</td><td>Create, Delete, Export, Import, Update, View</td></tr><tr><td>Business Rules</td><td>Create, Delete, Export, Import, Update, View</td></tr><tr><td>Data Identification Methods</td><td>Create, Delete, Export, Import, Update, View</td></tr><tr><td>Data Sources</td><td>AddContent, ApplyRules, Create, Delete, DeleteContent, Export, Import, RelationshipAssignment, RunJobs, Update, View, ViewDashboard, ViewSamples</td></tr><tr><td>Domain Asset</td><td>ApplyRules, ApproveRecords, Export, Modify, RunEngine, View</td></tr><tr><td>Match &#x26; Merge (Metadata) Rules</td><td>Modify, View</td></tr><tr><td>MDM Data Sources</td><td>Modify, View</td></tr><tr><td>Policies</td><td>Create, Delete, Export, Import, Update, View</td></tr><tr><td>Reference Data</td><td>Create, Delete, Export, Import, Update, UpdateValues, View, ViewValues</td></tr></tbody></table>
