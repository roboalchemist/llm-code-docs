# Source: https://docs.axonius.com/docs/permissions-list.md

# Permissions List

Use permissions to control the access different roles have to the different functions and assets in Axonius.

Permissions are the building blocks for Axonius Role Based Access Control (RBAC). Each [role](/docs/manage-roles) consists of a collection of permissions for various elements in the system. Each user is assigned a specific role with permissions.
Each role consists of the following categories and each category consists of different set of permissions.

There are two types of permissions:

* **Platform Capabilities Permissions** - These permissions control access to the various functions and pages in Axonius. Some examples are [Dashboards](https://docs.axonius.com/axonius-help-docs/docs/working-with-dashboard-spaces-2), [Asset Graph](https://docs.axonius.com/axonius-help-docs/docs/asset-graph-overview), [Activity Logs](https://docs.axonius.com/axonius-help-docs/docs/activity-logs), [Adapters](https://docs.axonius.com/axonius-help-docs/docs/adapters), and [Action Center](https://docs.axonius.com/axonius-help-docs/docs/new-ec-docs).
* **Asset Permissions** - Permissions are configured separately for each asset type in Axonius. Refer to the [list of Asset Types](/docs/assets-page#viewing-assets-by-type) for the full list of assets that a user needs permission to work with them.

See [Managing Roles](https://docs.axonius.com/axonius-help-docs/docs/manage-roles) for how to create roles and assign permissions.

The tables below lists all the system permissions and some asset permissions:

| Category       | Module                 | Sub-Category            | Permission                             |
| :------------- | :--------------------- | :---------------------- | :------------------------------------- |
| System         | Global Actions         | General                 | Save data analytics                    |
|                |                        |                         | Enable support center link             |
| Access         | API Access             | General                 | Enable API access                      |
|                |                        |                         | Reset API key                          |
| Management     | System Management      | General                 | View                                   |
|                |                        |                         | Update                                 |
|                |                        |                         | Manage data scopes                     |
|                |                        |                         | Move between data scopes               |
|                |                        | Roles                   | Add                                    |
|                |                        |                         | Edit                                   |
|                |                        |                         | Delete                                 |
|                |                        | General                 | Manage admin users                     |
|                |                        |                         | Manage gateways                        |
|                |                        |                         | View gateways                          |
|                |                        | Notifications           | View                                   |
|                |                        | General                 | Run manual discovery cycle             |
|                |                        | Tenants                 | Add                                    |
|                |                        |                         | Edit                                   |
|                |                        |                         | Delete                                 |
|                |                        | General                 | Export to CSV                          |
| Users          | Users Management       | General                 | View user accounts and roles           |
|                |                        | User                    | Add                                    |
|                |                        |                         | Edit                                   |
|                |                        |                         | Delete                                 |
|                |                        | General                 | Manage Service Accounts                |
|                |                        |                         | Export to CSV                          |
| Analytics      | Dashboards             | General                 | View                                   |
|                |                        | Charts                  | Add                                    |
|                |                        |                         | Edit                                   |
|                |                        |                         | Delete                                 |
|                |                        | Dashboards              | Add and edit                           |
|                |                        |                         | Add and edit for all data scopes       |
|                |                        |                         | Add and edit private dashboards        |
|                |                        |                         | Import                                 |
|                |                        |                         | Export                                 |
|                |                        |                         | Delete                                 |
|                |                        |                         | Set default dashboards for data scopes |
|                |                        |                         | Manage dashboard folders               |
|                |                        |                         | Refresh                                |
|                |                        | General                 | Export to CSV                          |
| Identities     | Identities: Rules      | General                 | Create and Edit                        |
|                |                        |                         | Delete                                 |
|                |                        |                         | Activation                             |
| Search         | Queries                | General                 | Manage query folders                   |
|                |                        |                         | Manage query calculation               |
|                |                        |                         | Import                                 |
|                |                        |                         | Export                                 |
|                |                        |                         | View query history of all users        |
|                |                        |                         | Add and edit for all data scopes       |
|                |                        |                         | Export to CSV                          |
| Reporting      | Reports                | General                 | View                                   |
|                |                        |                         | Add                                    |
|                |                        |                         | Edit                                   |
|                |                        |                         | Disable email reports                  |
|                |                        |                         | Delete                                 |
|                |                        |                         | Allow private reports                  |
|                |                        |                         | Export to CSV                          |
| Infrastructure | Managed Compute Nodes  | General                 | View                                   |
|                |                        |                         | Edit                                   |
|                |                        |                         | Restart and shut down                  |
| Adapters       | Adapters               | General                 | View                                   |
|                |                        | Connections             | Create                                 |
|                |                        |                         | Edit                                   |
|                |                        |                         | Delete                                 |
|                |                        |                         | Terminate                              |
|                |                        |                         | Fetch                                  |
|                |                        | General                 | Edit advanced settings                 |
|                |                        | Saved Queries           | Run                                    |
|                |                        |                         | Create                                 |
|                |                        |                         | Edit                                   |
|                |                        |                         | Delete                                 |
|                |                        | General                 | Export to CSV                          |
| Investigation  | Asset Investigation    | General                 | View                                   |
|                |                        |                         | Edit tracked fields                    |
|                |                        | Saved Queries           | Run                                    |
|                |                        |                         | Create                                 |
|                |                        |                         | Edit                                   |
|                |                        |                         | Delete                                 |
| Visualization  | Asset Graph            | General                 | View                                   |
|                |                        |                         | Create                                 |
|                |                        |                         | Edit                                   |
|                |                        |                         | Add and edit for all data scopes       |
|                |                        |                         | Load saved graph                       |
|                |                        |                         | Manage graph folders                   |
|                |                        |                         | Delete                                 |
| Alerts         | Findings               | General                 | View                                   |
|                |                        |                         | Modify                                 |
|                |                        | Alerts                  | View                                   |
|                |                        |                         | Modify                                 |
|                |                        | Saved Queries           | Run                                    |
|                |                        |                         | Create                                 |
|                |                        |                         | Edit                                   |
|                |                        |                         | Delete                                 |
| Auditing       | Activity logs          | General                 | View                                   |
|                |                        | Saved Queries           | Run                                    |
|                |                        |                         | Create                                 |
|                |                        |                         | Edit                                   |
|                |                        |                         | Delete                                 |
|                |                        | General                 | Export to CSV                          |
| Automation     | Action Center          | General                 | View                                   |
|                |                        |                         | Add and import                         |
|                |                        |                         | Edit                                   |
|                |                        |                         | Duplicate                              |
|                |                        |                         | Export                                 |
|                |                        |                         | Run                                    |
|                |                        |                         | Delete                                 |
|                |                        | Action Center Tasks     | View                                   |
|                |                        |                         | Terminate                              |
|                |                        |                         | Export to CSV                          |
| Cases          | Case Management        | General                 | View                                   |
|                |                        |                         | Create case                            |
|                |                        |                         | Edit case                              |
|                |                        |                         | Delete case                            |
| Mapping        | Field Mapping          | General                 | View                                   |
|                |                        |                         | Add                                    |
|                |                        |                         | Edit                                   |
|                |                        |                         | Delete                                 |
| Access         | Access Request         | General                 | Create request                         |
| Compliance     | Cloud Asset Compliance | General                 | View                                   |
|                |                        |                         | Update Benchmark settings              |
|                |                        | Exclusions and Comments | Manage Exclusions and Comments         |
|                |                        | General                 | Export to CSV                          |
| Data           | Ingestion Rules        | General                 | View                                   |
|                |                        |                         | Update                                 |
| AI             | Chatbot                | General                 | Enable Chatbot                         |
| UI             | Workspaces             | General                 | Set homepage dashboard                 |
|                |                        |                         | Edit homepage dashboard                |
|                |                        |                         |                                        |

<br />

### Assets

<br />

<Callout icon="📘" theme="info">
  Note:

  * Permissions are configured separately for each asset type in Axonius. The permissions available for each asset are similar to those detailed below for Device and User assets. Refer to the [list of Asset Types](/docs/assets-page#viewing-assets-by-type) for the full list of assets which each need these permissions configured.
  * When you apply permissions to assets that have sub-assets the permissions apply to all related sub-assets.
</Callout>

<br />

| Category | Module              | Sub-Category  | Permission                            |
| :------- | :------------------ | :------------ | :------------------------------------ |
| Assets   | Devices             | General       | View devices                          |
|          |                     |               | Create, delete, and link              |
|          |                     |               | Edit tags and custom data             |
|          |                     |               | Manage notes                          |
|          |                     | Saved Queries | Run                                   |
|          |                     |               | Create                                |
|          |                     |               | Edit                                  |
|          |                     |               | Delete                                |
|          |                     | General       | Edit device relationships             |
|          |                     | Column Views  | View                                  |
|          |                     |               | Manage                                |
|          |                     | General       | Export to CSV                         |
|          | Users               | General       | View users                            |
|          |                     |               | Create, delete, and link              |
|          |                     |               | Edit tags and custom data             |
|          |                     |               | Manage notes                          |
|          |                     | Saved Queries | Run                                   |
|          |                     |               | Create                                |
|          |                     |               | Edit                                  |
|          |                     |               | Delete                                |
|          |                     | General       | Edit user relationships               |
|          |                     | Column Views  | View                                  |
|          |                     |               | Manage                                |
|          |                     | General       | Export to CSV                         |
|          |                     |               | Edit tags and custom data             |
|          | Alerts/Findings     | General       | View alerts/findings                  |
|          |                     |               | Create, delete, and link              |
|          |                     |               | Manage notes                          |
|          |                     | Saved Queries | Run                                   |
|          |                     |               | Create                                |
|          |                     |               | Edit                                  |
|          |                     |               | Delete                                |
|          |                     | Column Views  | View                                  |
|          |                     |               | Manage                                |
|          |                     | General       | Edit alert finding relationships      |
|          |                     |               | Export to CSV                         |
|          | Cases               | General       | View cases                            |
|          |                     |               | Create, delete, and link              |
|          |                     |               | Edit tags and custom data             |
|          |                     |               | Manage notes                          |
|          |                     | Saved Queries | Run                                   |
|          |                     |               | Create                                |
|          |                     |               | Edit                                  |
|          |                     |               | Delete                                |
|          |                     | Column Views  | View                                  |
|          |                     |               | Manage                                |
|          |                     | General       | Edit case relationships               |
|          |                     |               | Export to CSV                         |
|          | Compliance Findings | General       | View compliance findings              |
|          |                     |               | Create, delete, and link              |
|          |                     |               | Edit tags and custom data             |
|          |                     |               | Manage notes                          |
|          |                     | Saved Queries | Run                                   |
|          |                     |               | Create                                |
|          |                     |               | Edit                                  |
|          |                     |               | Delete                                |
|          |                     | Column Views  | View                                  |
|          |                     |               | Manage                                |
|          |                     | General       | Edit compliance finding relationships |
|          |                     |               | Export to CSV                         |