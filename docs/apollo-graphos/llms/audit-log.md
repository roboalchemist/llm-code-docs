# Source: https://www.apollographql.com/docs/graphos/platform/access-management/audit-log.md

# Export and Read Audit Logs

Organizations with a GraphOS Enterprise plan can export and download an audit log of all material events that have occurred in the organization over a given timeframe.

The interface for requesting an export of auditable events is available under the **Audit** tab of your organization's homepage in GraphOS Studio:

Audit log data is available from July 2021 onward.

## Creating an audit log export

Only [Organization Admins](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#organization-wide-member-roles) can request audit exports.

When creating an audit log export, you specify a **time range**, along with optional filters to limit actions to a particular **user** or **graph**. The maximum time range that you can request audits for is 180 days, as defined by Apollo's [retention policy](https://www.apollographql.com/pricing?referrer=docs-content).

Exports sometimes take a few minutes to process. When an export is ready, Studio emails you a link to its CSV file, and you can also find that link in the audit exports table. Audit export files are available to download for 30 days. Actions may take up to 30 minutes to appear in an audit log.

If you need to export a log with more complex filters and against archives, please email [support@apollographql.com](mailto:support@apollographql.com).

## Reading an audit log

An exported audit log is a CSV file in which each row represents a material change to your Studio organization. Columns contain the following information:

| Column             | Description                                                                                                                                                                                                                                                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Timestamp`        | The time when the action occurred.                                                                                                                                                                                                                                                                                                    |
| `Action`           | The type of action that occurred. Possible values are listed in [Audited actions](https://www.apollographql.com/docs/graphos/platform/access-management/audit-log.md#audited-actions).                                                                                                                                                |
| `Resource_ID`      | The ID of the resource that was acted on.                                                                                                                                                                                                                                                                                             |
| `Resource_Type`    | The type of resource that was acted on. Possible values are listed in [Resource types](https://www.apollographql.com/docs/graphos/platform/access-management/audit-log.md#resource-types).                                                                                                                                            |
| `Details`          | A JSON object containing details of the action that occurred. The fields of this object vary depending on the action.                                                                                                                                                                                                                 |
| `Actor_ID`         | The Studio ID of the actor that performed the action.                                                                                                                                                                                                                                                                                 |
| `Actor_Type`       | The type of actor that performed the action. This is most commonly `USER` (an authenticated user) or `GRAPH` (a tool such as the Rover CLI using a graph API key).                                                                                                                                                                    |
| `Effective_Role`   | The [organizational role](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#organization-wide-member-roles) of the actor that performed the action, indicating its corresponding [permissions](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#role-permissions). |
| `Actor_Email`      | The actor's email address, if the actor is a `USER`.                                                                                                                                                                                                                                                                                  |
| `Actor_Name`       | The actor's name, if the actor is a `USER`.                                                                                                                                                                                                                                                                                           |
| `API_KEY_ID`       | If the actor is a system using an API key, that API key's ID.                                                                                                                                                                                                                                                                         |
| `API_KEY_Redacted` | If the actor is a system using an API key, that API key's redacted value.                                                                                                                                                                                                                                                             |
| `Graph_ID`         | The ID of the Studio graph that the action pertains to, if any.                                                                                                                                                                                                                                                                       |

## Resource types

An audit log's `Resource_Type` column indicates what type of resource each action was performed on. Possible values are listed below.

| Resource type                | Description                                                                                        |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| `ACCOUNT`                    | A Studio [organization](https://www.apollographql.com/docs/graphos/platform/access-management/org) |
| `USER`                       | A Studio user                                                                                      |
| `GRAPH`                      | A Studio [graph](https://www.apollographql.com/docs/graphos/get-started/concepts/graphs)           |
| `GRAPH_VARIANT`              | A graph [variant](https://www.apollographql.com/docs/graphos/platform/graph-management/variants)   |
| `GRAPH_API_KEY`              | A graph [API key](https://www.apollographql.com/docs/graphos/platform/access-management/api-keys)  |
| `USER_API_KEY`               | A user [API key](https://www.apollographql.com/docs/graphos/platform/access-management/api-keys)   |
| `ZENDESK_TICKET`             | An Apollo support ticket                                                                           |
| `AUDIT_JOB`                  | The generation of an audit log export                                                              |
| `EMAIL_SETTINGS`             | A user's marketing email settings                                                                  |
| `ACCOUNT_INVITATION`         | An invitation for a user to join an organization                                                   |
| `OPERATION_COLLECTION`       | A saved collection of GraphQL operations                                                           |
| `OPERATION_COLLECTION_ENTRY` | An individual entry within an operation collection                                                 |

## Audited actions

The `Action` column of an audit log indicates the type of each action that was performed. Possible values are listed below.

If your audit log includes an action type not listed below and you have questions about it, please contact [support@apollographql.com](mailto:support@apollographql.com).

### Generic actions

These actions are applied to a variety of [resource types](https://www.apollographql.com/docs/graphos/platform/access-management/audit-log.md#resource-types), including graphs, variants, and API keys.

| Action type        | Description                                                                                                                                                                            |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CREATE`           | Creates a resource of the corresponding resource type.                                                                                                                                 |
| `UPDATE`           | Modifies an existing resource of the corresponding resource type.                                                                                                                      |
| `SOFT_DELETE`      | Deletes a resource of the corresponding resource type, but the resource is still recoverable if necessary.                                                                             |
| `UNDO_SOFT_DELETE` | Recovers a resource from a previous `SOFT_DELETE`.                                                                                                                                     |
| `DELETE`           | Permanently deletes a resource of the corresponding resource type.                                                                                                                     |
| `CONFIG_CHANGE`    | Modifies a resource's configuration, such as changing a variant's endpoint URL. Many different configuration changes use this action type.                                             |
| `API_KEY`          | Creates, renames, or deletes an API key. This action type is deprecated in favor of `CREATE`, `UPDATE`, and `DELETE`, but it still appears alongside those action types in audit logs. |
| `DUPLICATE`        | Duplicates an existing resource.                                                                                                                                                       |
| `TRANSFER`         | Transfers ownership of a resource to another entity.                                                                                                                                   |

### Federated graphs

| Action type                   | Description                                |
| ----------------------------- | ------------------------------------------ |
| `IMPLEMENTING_SERVICE_UPSERT` | Adds a new subgraph to a federated graph.  |
| `IMPLEMENTING_SERVICE_REMOVE` | Removes a subgraph from a federated graph. |

### Graph variants

| Action type        | Description                                  |
| ------------------ | -------------------------------------------- |
| `ADD_LINK_INFO`    | Adds additional metadata to a resource link. |
| `REMOVE_LINK_INFO` | Removes metadata from a resource link.       |

### Studio features

| Action type                       | Description                                                                                                                                                                                                                          |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `IGNORE_OPERATION_IN_CHECKS`      | Ignores a particular GraphQL operation when running [schema checks](https://www.apollographql.com/docs/graphos/platform/schema-management/checks/).                                                                                  |
| `MARK_CHANGES_SAFE_FOR_OPERATION` | Marks a particular set of changes as safe when running [schema checks](https://www.apollographql.com/docs/graphos/platform/schema-management/checks/).                                                                               |
| `TOGGLE_DATADOG`                  | Enables or disables [Datadog metrics forwarding](https://www.apollographql.com/docs/graphos/platform/insights/datadog-forwarding).                                                                                                   |
| (Deprecated) `REGISTER_OPERATION` | Registered a GraphQL operation in the operation registry. [Safelisting with persisted queries](https://www.apollographql.com/docs/graphos/platform/security/persisted-queries) is now the recommended way of registering operations. |

### GraphOS plans

| Action type                           | Description                                                                                                                                        |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CURRENT_BILLING_SUBSCRIPTION_CHANGE` | Changes an organization's active Studio plan.                                                                                                      |
| `BILLING_PERIOD_CHANGE`               | Changes a Studio plan's billing period.                                                                                                            |
| `CANCEL_STUDIO_SUBSCRIPTION`          | Cancels a Studio plan (the plan remains active through the current billing period, after which the `TERMINATE_STUDIO_SUBSCRIPTION` action occurs). |
| `TERMINATE_STUDIO_SUBSCRIPTION`       | Terminates an organization's canceled plan at the end of the current billing period.                                                               |
| `REACTIVATE_STUDIO_SUBSCRIPTION`      | Reactivates a previously canceled Studio plan.                                                                                                     |
| `DISMISS_EXPIRED_TRIAL`               | Dismisses an expired trial notification for a Studio plan.                                                                                         |

### Organization members

| Action type           | Description                                                                                                                                                   |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `JOIN_ACCOUNT`        | Adds a user to an organization.                                                                                                                               |
| `LEAVE_ACCOUNT`       | Removes a user from an organization.                                                                                                                          |
| `CHANGE_ROLE`         | Changes a user's [organizational role](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#organization-wide-member-roles).    |
| `OVERRIDE_GRAPH_ROLE` | [Overrides a user's role](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#graph-specific-member-roles) for a single graph. |

### Account and security

| Action type          | Description                                       |
| -------------------- | ------------------------------------------------- |
| `EMAIL_VERIFICATION` | Verifies an email address for an account.         |
| `SET_SUBSCRIPTIONS`  | Updates marketing email subscription preferences. |
