# Source: https://grafbase.com/docs/platform/audit-logs.md

# Audit Logs

Audit logs help you track and analyze your organization member's activitiy.

## Export

Only owners and admins of an organization can export and download the audit logs. To do so:

- Go to the `Settings` tab of your organization.
- `Audit Logs`
- Select the desired date range and export the CSV.

Audit logs are available for the last 90 days.

### CSV Export Structure

The exported CSV file can be opened using any spreadsheet-compatible software and includes the following fields:

| Column                  | Description                                                     |
| ----------------------- | --------------------------------------------------------------- |
| timestamp               | Time and date at which the event occurred                       |
| actor_access_token_id   | UUID of the access token used for the action                    |
| actor_access_token_name | Name of the access token used                                   |
| actor_user_id           | UUID of the user who performed the action                       |
| actor_user_name         | Username of the team member responsible for the event           |
| actor_user_email        | Email address of the team member responsible for the event      |
| action                  | Specific action taken (e.g., created, updated, deleted)         |
| previous                | JSON object showing the object's previous state (if applicable) |
| next                    | JSON object showing the object's updated state (if applicable)  |

An action is either done by a user _or_ an account access token, so at least one of them will always be present.

## Actions

### graph

A federated GraphQL supergraph

| Action Name     | Description                            |
| --------------- | -------------------------------------- |
| `graph.created` | Indicates that a new graph was created |
| `graph.deleted` | Indicates that a new graph was deleted |
| `graph.updated` | Indicates that a new graph was updated |

### subgraph

A subgraph within a federated GraphQL supergraph

| Action Name          | Description                                      |
| -------------------- | ------------------------------------------------ |
| `subgraph.created`   | Indicates that a new subgraph was created        |
| `subgraph.deleted`   | Indicates that a subgraph was deleted            |
| `subgraph.updated`   | Indicates that a subgraph was updated            |
| `subgraph.published` | Indicates that a schema was published to a graph |

### member

Organization and team members

| Action Name      | Description                           |
| ---------------- | ------------------------------------- |
| `member.created` | Indicates that a new member was added |
| `member.deleted` | Indicates that a member was removed   |
| `member.updated` | Indicates that a member was updated   |

### branch

Graph branches for development and testing

| Action Name      | Description                             |
| ---------------- | --------------------------------------- |
| `branch.created` | Indicates that a new branch was created |
| `branch.deleted` | Indicates that a branch was deleted     |
| `branch.updated` | Indicates that a branch was updated     |

### team

Organizational teams for access control

| Action Name           | Description                                     |
| --------------------- | ----------------------------------------------- |
| `team.created`        | Indicates that a new team was created           |
| `team.deleted`        | Indicates that a team was deleted               |
| `team.updated`        | Indicates that a team was updated               |
| `team.member.added`   | Indicates that a member was added to a team     |
| `team.member.updated` | Indicates that a team member's role was updated |
| `team.member.removed` | Indicates that a member was removed from a team |

### invite

User invitations to join the organization

| Action Name      | Description                             |
| ---------------- | --------------------------------------- |
| `invite.created` | Indicates that a new invite was created |
| `invite.deleted` | Indicates that an invite was deleted    |
| `invite.updated` | Indicates that an invite was updated    |

### organization

Organization management

| Action Name            | Description                                   |
| ---------------------- | --------------------------------------------- |
| `organization.created` | Indicates that a new organization was created |
| `organization.updated` | Indicates that an organization was updated    |

### access_token

API access tokens for programmatic access

| Action Name                  | Description                                                      |
| ---------------------------- | ---------------------------------------------------------------- |
| `access_token.created`       | Indicates that a new access token was created                    |
| `access_token.deleted`       | Indicates that an access token was deleted                       |
| `access_token.updated`       | Indicates that an access token was updated                       |
| `access_token.graph.added`   | Indicates that access to a graph was granted to a token          |
| `access_token.graph.updated` | Indicates that graph access permissions were updated for a token |
| `access_token.graph.removed` | Indicates that access to a graph was revoked from a token        |

### audit_log

Audit log export and management operations

| Action Name                   | Description                                               |
| ----------------------------- | --------------------------------------------------------- |
| `audit_log.export.downloaded` | Indicates that an audit log export was downloaded (async) |

### trusted_document

Trusted documents management for GraphQL operations

| Action Name                  | Description                                                  |
| ---------------------------- | ------------------------------------------------------------ |
| `trusted_document.submitted` | Indicates that trusted documents were submitted for a client |