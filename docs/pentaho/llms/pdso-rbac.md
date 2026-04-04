# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-management/pdso-rbac.md

# Default user roles and permissions in Data Optimizer

Data Optimizer provides default user roles with role-based permissions that enable administrators to allow and restrict access as necessary. Administrators can also fine-tune access by creating communities of users to which they assign specific permissions, such as access to data sources, rule applications, or dashboards.

All users can comment on, rate, and be notified of changes to assets for which they have access. The following user actions in Data Optimizer depend on the applicable data sources permission type:

* AddContent and DeleteContent are required to tier, rehydrate, and delete data.
* ViewDashboard is required to view the dashboards.
* ApplyRules is required to execute rules.
* View, Create, Update, and Delete are required to view, create, edit, and delete the metadata rules and rule definitions.

The tables below outline the permission types available in the default roles. You can customize the permissions for a user by defining a community with greater or more restrictive permissions and adding the user to this community. See **Manage users and permissions** in **Data Catalog** for more information.

## User roles

The following table shows the access permitted by default for a user with the Business User or Data User role. For example, a user with the Business User role cannot view data sources.

| Role          | Permission Type                                | Actions |
| ------------- | ---------------------------------------------- | ------- |
| Business User | Business Glossary                              | View    |
| Data User     | Business Glossary                              | View    |
| Data Sources  | View, AddContent, DeleteContent, ViewDashboard |         |

## Steward roles

The following table shows the access permitted by default for a user with the Business Steward or Data Steward role. For example, a user with the Business Steward role can view, but cannot create or update data sources.

| Role                        | Permission Type                                                                                                                          | Actions                                      |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| Business Steward            | Business Glossary                                                                                                                        | View, Create, Update, Delete, Import, Export |
| Data Sources                | View                                                                                                                                     |                                              |
| Data Steward                | Business Glossary                                                                                                                        | View                                         |
| Data Sources                | View, Create, ViewSamples, Update, RunJobs, ApplyRules, TermAssignment, Delete, Import, Export, AddContent, DeleteContent, ViewDashboard |                                              |
| Business Rules              | View, Create, Update, Delete, Import, Export                                                                                             |                                              |
| Data Identification Methods | View, Create, Update, Delete, Import, Export                                                                                             |                                              |
| Reference Data              | Create, Delete, Export, Import, Update, UpdateValues, View, ViewValues                                                                   |                                              |
| Domain Asset                | View, ApplyRules, ApproveRecords                                                                                                         |                                              |

## Admin and Developer roles

The following table shows the access permitted by default for a user with the Admin or Data Developer role. For example, a user with the Admin role can view data sources but cannot view or create business rules.

| Role                 | Permission Type                                             | Actions |
| -------------------- | ----------------------------------------------------------- | ------- |
| Admin                | Business Glossary                                           | View    |
| Data Sources         | View                                                        |         |
| Administration       | View, Modify                                                |         |
| Domain Asset         | View, Modify, ApplyRules, RunEngine, ApproveRecords, Export |         |
| Data Developer       | Business Glossary                                           | View    |
| Data Sources         | View                                                        |         |
| Business Rules       | View, Create, Update, Delete, Import, Export                |         |
| Domain Asset         | View, Modify, ApplyRules, RunEngine, ApproveRecords, Export |         |
