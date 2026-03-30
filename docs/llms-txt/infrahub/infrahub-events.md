# Source: https://docs.infrahub.app/reference/infrahub-events.md

# Infrahub events

This document provides detailed documentation for all events used in the Infrahub event system.

info

For more detailed explanations on how these events are used within Infrahub, see the [Infrahub event](/topics/events.md) topic.

## Artifact events[​](#artifact-events "Direct link to Artifact events")

### Artifact Created Event[​](#artifact-created-event "Direct link to Artifact Created Event")

**Type**: infrahub.artifact.created **Description**: Event generated when an artifact has been created

**Uses node\_kind filter for webhooks**: `true`

| Key                            | Description                                                           |
| ------------------------------ | --------------------------------------------------------------------- |
| **meta.branch**                | The branch on which originate this event                              |
| **meta.request\_id**           | N/A                                                                   |
| **meta.account\_id**           | The ID of the account triggering this event                           |
| **meta.initiator\_id**         | The worker identity of the initial sender of this message             |
| **meta.context**               | The context used when originating this event                          |
| **meta.level**                 | N/A                                                                   |
| **meta.has\_children**         | Indicates if this event might potentially have child events under it. |
| **meta.id**                    | UUID of the event                                                     |
| **meta.parent**                | The UUID of the parent event if applicable                            |
| **meta.ancestors**             | Any event used to trigger this event                                  |
| **node\_id**                   | The ID of the artifact                                                |
| **artifact\_definition\_id**   | The ID of the artifact definition                                     |
| **artifact\_definition\_name** | The name of the artifact definition                                   |
| **target\_id**                 | The ID of the target of the artifact                                  |
| **target\_kind**               | The kind of the target of the artifact                                |
| **checksum**                   | The current checksum of the artifact                                  |
| **checksum\_previous**         | The previous checksum of the artifact                                 |
| **storage\_id**                | The current storage id of the artifact                                |
| **storage\_id\_previous**      | The previous storage id of the artifact                               |

### Artifact Updated Event[​](#artifact-updated-event "Direct link to Artifact Updated Event")

**Type**: infrahub.artifact.updated **Description**: Event generated when an artifact has been updated

**Uses node\_kind filter for webhooks**: `true`

| Key                            | Description                                                           |
| ------------------------------ | --------------------------------------------------------------------- |
| **meta.branch**                | The branch on which originate this event                              |
| **meta.request\_id**           | N/A                                                                   |
| **meta.account\_id**           | The ID of the account triggering this event                           |
| **meta.initiator\_id**         | The worker identity of the initial sender of this message             |
| **meta.context**               | The context used when originating this event                          |
| **meta.level**                 | N/A                                                                   |
| **meta.has\_children**         | Indicates if this event might potentially have child events under it. |
| **meta.id**                    | UUID of the event                                                     |
| **meta.parent**                | The UUID of the parent event if applicable                            |
| **meta.ancestors**             | Any event used to trigger this event                                  |
| **node\_id**                   | The ID of the artifact                                                |
| **artifact\_definition\_id**   | The ID of the artifact definition                                     |
| **artifact\_definition\_name** | The name of the artifact definition                                   |
| **target\_id**                 | The ID of the target of the artifact                                  |
| **target\_kind**               | The kind of the target of the artifact                                |
| **checksum**                   | The current checksum of the artifact                                  |
| **checksum\_previous**         | The previous checksum of the artifact                                 |
| **storage\_id**                | The current storage id of the artifact                                |
| **storage\_id\_previous**      | The previous storage id of the artifact                               |

## Branch events[​](#branch-events "Direct link to Branch events")

### Branch Created Event[​](#branch-created-event "Direct link to Branch Created Event")

**Type**: infrahub.branch.created **Description**: Event generated when a branch has been created

**Uses node\_kind filter for webhooks**: `false`

| Key                    | Description                                                           |
| ---------------------- | --------------------------------------------------------------------- |
| **meta.branch**        | The branch on which originate this event                              |
| **meta.request\_id**   | N/A                                                                   |
| **meta.account\_id**   | The ID of the account triggering this event                           |
| **meta.initiator\_id** | The worker identity of the initial sender of this message             |
| **meta.context**       | The context used when originating this event                          |
| **meta.level**         | N/A                                                                   |
| **meta.has\_children** | Indicates if this event might potentially have child events under it. |
| **meta.id**            | UUID of the event                                                     |
| **meta.parent**        | The UUID of the parent event if applicable                            |
| **meta.ancestors**     | Any event used to trigger this event                                  |
| **branch\_name**       | The name of the branch                                                |
| **branch\_id**         | The ID of the branch                                                  |
| **sync\_with\_git**    | Indicates if the branch was extended to Git                           |

### Branch Deleted Event[​](#branch-deleted-event "Direct link to Branch Deleted Event")

**Type**: infrahub.branch.deleted **Description**: Event generated when a branch has been deleted

**Uses node\_kind filter for webhooks**: `false`

| Key                    | Description                                                           |
| ---------------------- | --------------------------------------------------------------------- |
| **meta.branch**        | The branch on which originate this event                              |
| **meta.request\_id**   | N/A                                                                   |
| **meta.account\_id**   | The ID of the account triggering this event                           |
| **meta.initiator\_id** | The worker identity of the initial sender of this message             |
| **meta.context**       | The context used when originating this event                          |
| **meta.level**         | N/A                                                                   |
| **meta.has\_children** | Indicates if this event might potentially have child events under it. |
| **meta.id**            | UUID of the event                                                     |
| **meta.parent**        | The UUID of the parent event if applicable                            |
| **meta.ancestors**     | Any event used to trigger this event                                  |
| **branch\_name**       | The name of the branch                                                |
| **branch\_id**         | The ID of the mutated node                                            |
| **sync\_with\_git**    | Indicates if the branch was extended to Git                           |

### Branch Merged Event[​](#branch-merged-event "Direct link to Branch Merged Event")

**Type**: infrahub.branch.merged **Description**: Event generated when a branch has been merged

**Uses node\_kind filter for webhooks**: `false`

| Key                      | Description                                                           |
| ------------------------ | --------------------------------------------------------------------- |
| **meta.branch**          | The branch on which originate this event                              |
| **meta.request\_id**     | N/A                                                                   |
| **meta.account\_id**     | The ID of the account triggering this event                           |
| **meta.initiator\_id**   | The worker identity of the initial sender of this message             |
| **meta.context**         | The context used when originating this event                          |
| **meta.level**           | N/A                                                                   |
| **meta.has\_children**   | Indicates if this event might potentially have child events under it. |
| **meta.id**              | UUID of the event                                                     |
| **meta.parent**          | The UUID of the parent event if applicable                            |
| **meta.ancestors**       | Any event used to trigger this event                                  |
| **branch\_name**         | The name of the branch                                                |
| **branch\_id**           | The ID of the branch                                                  |
| **proposed\_change\_id** | The ID of the proposed change that merged this branch if applicable   |

### Branch Migrated Event[​](#branch-migrated-event "Direct link to Branch Migrated Event")

**Type**: infrahub.branch.migrated **Description**: Event generated when a branch has been migrated

**Uses node\_kind filter for webhooks**: `false`

| Key                    | Description                                                           |
| ---------------------- | --------------------------------------------------------------------- |
| **meta.branch**        | The branch on which originate this event                              |
| **meta.request\_id**   | N/A                                                                   |
| **meta.account\_id**   | The ID of the account triggering this event                           |
| **meta.initiator\_id** | The worker identity of the initial sender of this message             |
| **meta.context**       | The context used when originating this event                          |
| **meta.level**         | N/A                                                                   |
| **meta.has\_children** | Indicates if this event might potentially have child events under it. |
| **meta.id**            | UUID of the event                                                     |
| **meta.parent**        | The UUID of the parent event if applicable                            |
| **meta.ancestors**     | Any event used to trigger this event                                  |
| **branch\_id**         | The ID of the branch                                                  |
| **branch\_name**       | The name of the branch                                                |

### Branch Rebased Event[​](#branch-rebased-event "Direct link to Branch Rebased Event")

**Type**: infrahub.branch.rebased **Description**: Event generated when a branch has been rebased

**Uses node\_kind filter for webhooks**: `false`

| Key                    | Description                                                           |
| ---------------------- | --------------------------------------------------------------------- |
| **meta.branch**        | The branch on which originate this event                              |
| **meta.request\_id**   | N/A                                                                   |
| **meta.account\_id**   | The ID of the account triggering this event                           |
| **meta.initiator\_id** | The worker identity of the initial sender of this message             |
| **meta.context**       | The context used when originating this event                          |
| **meta.level**         | N/A                                                                   |
| **meta.has\_children** | Indicates if this event might potentially have child events under it. |
| **meta.id**            | UUID of the event                                                     |
| **meta.parent**        | The UUID of the parent event if applicable                            |
| **meta.ancestors**     | Any event used to trigger this event                                  |
| **branch\_id**         | The ID of the branch                                                  |
| **branch\_name**       | The name of the branch                                                |

## Group events[​](#group-events "Direct link to Group events")

### Group Member Added Event[​](#group-member-added-event "Direct link to Group Member Added Event")

**Type**: infrahub.group.member\_added **Description**: Event generated when a one or more members have been added to a group

**Uses node\_kind filter for webhooks**: `true`

| Key                    | Description                                                           |
| ---------------------- | --------------------------------------------------------------------- |
| **meta.branch**        | The branch on which originate this event                              |
| **meta.request\_id**   | N/A                                                                   |
| **meta.account\_id**   | The ID of the account triggering this event                           |
| **meta.initiator\_id** | The worker identity of the initial sender of this message             |
| **meta.context**       | The context used when originating this event                          |
| **meta.level**         | N/A                                                                   |
| **meta.has\_children** | Indicates if this event might potentially have child events under it. |
| **meta.id**            | UUID of the event                                                     |
| **meta.parent**        | The UUID of the parent event if applicable                            |
| **meta.ancestors**     | Any event used to trigger this event                                  |
| **kind**               | The type of updated group                                             |
| **node\_id**           | The ID of the updated group                                           |
| **action**             | N/A                                                                   |
| **members**            | Updated members during this event.                                    |
| **ancestors**          | A list of groups that are ancestors of this group.                    |

### Group Member Removed Event[​](#group-member-removed-event "Direct link to Group Member Removed Event")

**Type**: infrahub.group.member\_removed **Description**: Event generated when a one or more members have been removed to a group

**Uses node\_kind filter for webhooks**: `true`

| Key                    | Description                                                           |
| ---------------------- | --------------------------------------------------------------------- |
| **meta.branch**        | The branch on which originate this event                              |
| **meta.request\_id**   | N/A                                                                   |
| **meta.account\_id**   | The ID of the account triggering this event                           |
| **meta.initiator\_id** | The worker identity of the initial sender of this message             |
| **meta.context**       | The context used when originating this event                          |
| **meta.level**         | N/A                                                                   |
| **meta.has\_children** | Indicates if this event might potentially have child events under it. |
| **meta.id**            | UUID of the event                                                     |
| **meta.parent**        | The UUID of the parent event if applicable                            |
| **meta.ancestors**     | Any event used to trigger this event                                  |
| **kind**               | The type of updated group                                             |
| **node\_id**           | The ID of the updated group                                           |
| **action**             | N/A                                                                   |
| **members**            | Updated members during this event.                                    |
| **ancestors**          | A list of groups that are ancestors of this group.                    |

## Node events[​](#node-events "Direct link to Node events")

### Node Created Event[​](#node-created-event "Direct link to Node Created Event")

**Type**: infrahub.node.created **Description**: Event generated when a node has been created

**Uses node\_kind filter for webhooks**: `true`

| Key                    | Description                                                           |
| ---------------------- | --------------------------------------------------------------------- |
| **meta.branch**        | The branch on which originate this event                              |
| **meta.request\_id**   | N/A                                                                   |
| **meta.account\_id**   | The ID of the account triggering this event                           |
| **meta.initiator\_id** | The worker identity of the initial sender of this message             |
| **meta.context**       | The context used when originating this event                          |
| **meta.level**         | N/A                                                                   |
| **meta.has\_children** | Indicates if this event might potentially have child events under it. |
| **meta.id**            | UUID of the event                                                     |
| **meta.parent**        | The UUID of the parent event if applicable                            |
| **meta.ancestors**     | Any event used to trigger this event                                  |
| **kind**               | The type of object modified                                           |
| **node\_id**           | The ID of the mutated node                                            |
| **action**             | N/A                                                                   |
| **changelog**          | Data on modified object                                               |
| **fields**             | Fields provided in the mutation                                       |

### Node Deleted Event[​](#node-deleted-event "Direct link to Node Deleted Event")

**Type**: infrahub.node.deleted **Description**: Event generated when a node has been deleted

**Uses node\_kind filter for webhooks**: `true`

| Key                    | Description                                                           |
| ---------------------- | --------------------------------------------------------------------- |
| **meta.branch**        | The branch on which originate this event                              |
| **meta.request\_id**   | N/A                                                                   |
| **meta.account\_id**   | The ID of the account triggering this event                           |
| **meta.initiator\_id** | The worker identity of the initial sender of this message             |
| **meta.context**       | The context used when originating this event                          |
| **meta.level**         | N/A                                                                   |
| **meta.has\_children** | Indicates if this event might potentially have child events under it. |
| **meta.id**            | UUID of the event                                                     |
| **meta.parent**        | The UUID of the parent event if applicable                            |
| **meta.ancestors**     | Any event used to trigger this event                                  |
| **kind**               | The type of object modified                                           |
| **node\_id**           | The ID of the mutated node                                            |
| **action**             | N/A                                                                   |
| **changelog**          | Data on modified object                                               |
| **fields**             | Fields provided in the mutation                                       |

### Node Updated Event[​](#node-updated-event "Direct link to Node Updated Event")

**Type**: infrahub.node.updated **Description**: Event generated when a node has been updated

**Uses node\_kind filter for webhooks**: `true`

| Key                    | Description                                                           |
| ---------------------- | --------------------------------------------------------------------- |
| **meta.branch**        | The branch on which originate this event                              |
| **meta.request\_id**   | N/A                                                                   |
| **meta.account\_id**   | The ID of the account triggering this event                           |
| **meta.initiator\_id** | The worker identity of the initial sender of this message             |
| **meta.context**       | The context used when originating this event                          |
| **meta.level**         | N/A                                                                   |
| **meta.has\_children** | Indicates if this event might potentially have child events under it. |
| **meta.id**            | UUID of the event                                                     |
| **meta.parent**        | The UUID of the parent event if applicable                            |
| **meta.ancestors**     | Any event used to trigger this event                                  |
| **kind**               | The type of object modified                                           |
| **node\_id**           | The ID of the mutated node                                            |
| **action**             | N/A                                                                   |
| **changelog**          | Data on modified object                                               |
| **fields**             | Fields provided in the mutation                                       |

## Proposed events[​](#proposed-events "Direct link to Proposed events")

### Proposed Change Approval Revoked Event[​](#proposed-change-approval-revoked-event "Direct link to Proposed Change Approval Revoked Event")

**Type**: infrahub.proposed\_change.approval\_revoked **Description**: Event generated when a proposed change approval has been revoked

**Uses node\_kind filter for webhooks**: `false`

| Key                            | Description                                                           |
| ------------------------------ | --------------------------------------------------------------------- |
| **meta.branch**                | The branch on which originate this event                              |
| **meta.request\_id**           | N/A                                                                   |
| **meta.account\_id**           | The ID of the account triggering this event                           |
| **meta.initiator\_id**         | The worker identity of the initial sender of this message             |
| **meta.context**               | The context used when originating this event                          |
| **meta.level**                 | N/A                                                                   |
| **meta.has\_children**         | Indicates if this event might potentially have child events under it. |
| **meta.id**                    | UUID of the event                                                     |
| **meta.parent**                | The UUID of the parent event if applicable                            |
| **meta.ancestors**             | Any event used to trigger this event                                  |
| **proposed\_change\_id**       | The ID of the proposed change                                         |
| **proposed\_change\_name**     | The name of the proposed change                                       |
| **proposed\_change\_state**    | The state of the proposed change                                      |
| **reviewer\_account\_id**      | The ID of the user who reviewed the proposed change                   |
| **reviewer\_account\_name**    | The name of the user who reviewed the proposed change                 |
| **reviewer\_former\_decision** | The former decision made by the reviewer                              |

### Proposed Change Approvals Revoked Event[​](#proposed-change-approvals-revoked-event "Direct link to Proposed Change Approvals Revoked Event")

**Type**: infrahub.proposed\_change.approvals\_revoked

**Uses node\_kind filter for webhooks**: `false`

| Key                         | Description                                                           |
| --------------------------- | --------------------------------------------------------------------- |
| **meta.branch**             | The branch on which originate this event                              |
| **meta.request\_id**        | N/A                                                                   |
| **meta.account\_id**        | The ID of the account triggering this event                           |
| **meta.initiator\_id**      | The worker identity of the initial sender of this message             |
| **meta.context**            | The context used when originating this event                          |
| **meta.level**              | N/A                                                                   |
| **meta.has\_children**      | Indicates if this event might potentially have child events under it. |
| **meta.id**                 | UUID of the event                                                     |
| **meta.parent**             | The UUID of the parent event if applicable                            |
| **meta.ancestors**          | Any event used to trigger this event                                  |
| **proposed\_change\_id**    | The ID of the proposed change                                         |
| **proposed\_change\_name**  | The name of the proposed change                                       |
| **proposed\_change\_state** | The state of the proposed change                                      |
| **reviewer\_accounts**      | ID to name map of accounts whose approval was revoked                 |

### Proposed Change Approved Event[​](#proposed-change-approved-event "Direct link to Proposed Change Approved Event")

**Type**: infrahub.proposed\_change.approved **Description**: Event generated when a proposed change has been approved

**Uses node\_kind filter for webhooks**: `false`

| Key                         | Description                                                           |
| --------------------------- | --------------------------------------------------------------------- |
| **meta.branch**             | The branch on which originate this event                              |
| **meta.request\_id**        | N/A                                                                   |
| **meta.account\_id**        | The ID of the account triggering this event                           |
| **meta.initiator\_id**      | The worker identity of the initial sender of this message             |
| **meta.context**            | The context used when originating this event                          |
| **meta.level**              | N/A                                                                   |
| **meta.has\_children**      | Indicates if this event might potentially have child events under it. |
| **meta.id**                 | UUID of the event                                                     |
| **meta.parent**             | The UUID of the parent event if applicable                            |
| **meta.ancestors**          | Any event used to trigger this event                                  |
| **proposed\_change\_id**    | The ID of the proposed change                                         |
| **proposed\_change\_name**  | The name of the proposed change                                       |
| **proposed\_change\_state** | The state of the proposed change                                      |
| **reviewer\_account\_id**   | The ID of the user who reviewed the proposed change                   |
| **reviewer\_account\_name** | The name of the user who reviewed the proposed change                 |
| **reviewer\_decision**      | The decision made by the reviewer                                     |

### Proposed Change Merged Event[​](#proposed-change-merged-event "Direct link to Proposed Change Merged Event")

**Type**: infrahub.proposed\_change.merged **Description**: Event generated when a proposed change has been merged

**Uses node\_kind filter for webhooks**: `false`

| Key                           | Description                                                           |
| ----------------------------- | --------------------------------------------------------------------- |
| **meta.branch**               | The branch on which originate this event                              |
| **meta.request\_id**          | N/A                                                                   |
| **meta.account\_id**          | The ID of the account triggering this event                           |
| **meta.initiator\_id**        | The worker identity of the initial sender of this message             |
| **meta.context**              | The context used when originating this event                          |
| **meta.level**                | N/A                                                                   |
| **meta.has\_children**        | Indicates if this event might potentially have child events under it. |
| **meta.id**                   | UUID of the event                                                     |
| **meta.parent**               | The UUID of the parent event if applicable                            |
| **meta.ancestors**            | Any event used to trigger this event                                  |
| **proposed\_change\_id**      | The ID of the proposed change                                         |
| **proposed\_change\_name**    | The name of the proposed change                                       |
| **proposed\_change\_state**   | The state of the proposed change                                      |
| **merged\_by\_account\_id**   | The ID of the user who merged the proposed change                     |
| **merged\_by\_account\_name** | The name of the user who merged the proposed change                   |

### Proposed Change Rejected Event[​](#proposed-change-rejected-event "Direct link to Proposed Change Rejected Event")

**Type**: infrahub.proposed\_change.rejected **Description**: Event generated when a proposed change has been rejected

**Uses node\_kind filter for webhooks**: `false`

| Key                         | Description                                                           |
| --------------------------- | --------------------------------------------------------------------- |
| **meta.branch**             | The branch on which originate this event                              |
| **meta.request\_id**        | N/A                                                                   |
| **meta.account\_id**        | The ID of the account triggering this event                           |
| **meta.initiator\_id**      | The worker identity of the initial sender of this message             |
| **meta.context**            | The context used when originating this event                          |
| **meta.level**              | N/A                                                                   |
| **meta.has\_children**      | Indicates if this event might potentially have child events under it. |
| **meta.id**                 | UUID of the event                                                     |
| **meta.parent**             | The UUID of the parent event if applicable                            |
| **meta.ancestors**          | Any event used to trigger this event                                  |
| **proposed\_change\_id**    | The ID of the proposed change                                         |
| **proposed\_change\_name**  | The name of the proposed change                                       |
| **proposed\_change\_state** | The state of the proposed change                                      |
| **reviewer\_account\_id**   | The ID of the user who reviewed the proposed change                   |
| **reviewer\_account\_name** | The name of the user who reviewed the proposed change                 |
| **reviewer\_decision**      | The decision made by the reviewer                                     |

### Proposed Change Rejection Revoked Event[​](#proposed-change-rejection-revoked-event "Direct link to Proposed Change Rejection Revoked Event")

**Type**: infrahub.proposed\_change.rejection\_revoked **Description**: Event generated when a proposed change rejection has been revoked

**Uses node\_kind filter for webhooks**: `false`

| Key                            | Description                                                           |
| ------------------------------ | --------------------------------------------------------------------- |
| **meta.branch**                | The branch on which originate this event                              |
| **meta.request\_id**           | N/A                                                                   |
| **meta.account\_id**           | The ID of the account triggering this event                           |
| **meta.initiator\_id**         | The worker identity of the initial sender of this message             |
| **meta.context**               | The context used when originating this event                          |
| **meta.level**                 | N/A                                                                   |
| **meta.has\_children**         | Indicates if this event might potentially have child events under it. |
| **meta.id**                    | UUID of the event                                                     |
| **meta.parent**                | The UUID of the parent event if applicable                            |
| **meta.ancestors**             | Any event used to trigger this event                                  |
| **proposed\_change\_id**       | The ID of the proposed change                                         |
| **proposed\_change\_name**     | The name of the proposed change                                       |
| **proposed\_change\_state**    | The state of the proposed change                                      |
| **reviewer\_account\_id**      | The ID of the user who reviewed the proposed change                   |
| **reviewer\_account\_name**    | The name of the user who reviewed the proposed change                 |
| **reviewer\_former\_decision** | The former decision made by the reviewer                              |

### Proposed Change Review Requested Event[​](#proposed-change-review-requested-event "Direct link to Proposed Change Review Requested Event")

**Type**: infrahub.proposed\_change.review\_requested **Description**: Event generated when a proposed change has been flagged for review

**Uses node\_kind filter for webhooks**: `false`

| Key                              | Description                                                           |
| -------------------------------- | --------------------------------------------------------------------- |
| **meta.branch**                  | The branch on which originate this event                              |
| **meta.request\_id**             | N/A                                                                   |
| **meta.account\_id**             | The ID of the account triggering this event                           |
| **meta.initiator\_id**           | The worker identity of the initial sender of this message             |
| **meta.context**                 | The context used when originating this event                          |
| **meta.level**                   | N/A                                                                   |
| **meta.has\_children**           | Indicates if this event might potentially have child events under it. |
| **meta.id**                      | UUID of the event                                                     |
| **meta.parent**                  | The UUID of the parent event if applicable                            |
| **meta.ancestors**               | Any event used to trigger this event                                  |
| **proposed\_change\_id**         | The ID of the proposed change                                         |
| **proposed\_change\_name**       | The name of the proposed change                                       |
| **proposed\_change\_state**      | The state of the proposed change                                      |
| **requested\_by\_account\_id**   | The ID of the user who requested the proposed change to be reviewed   |
| **requested\_by\_account\_name** | The name of the user who requested the proposed change to be reviewed |

### Proposed Change Thread Created Event[​](#proposed-change-thread-created-event "Direct link to Proposed Change Thread Created Event")

**Type**: infrahub.proposed\_change\_thread.created **Description**: Event generated when a thread has been created in a proposed change

**Uses node\_kind filter for webhooks**: `false`

| Key                         | Description                                                           |
| --------------------------- | --------------------------------------------------------------------- |
| **meta.branch**             | The branch on which originate this event                              |
| **meta.request\_id**        | N/A                                                                   |
| **meta.account\_id**        | The ID of the account triggering this event                           |
| **meta.initiator\_id**      | The worker identity of the initial sender of this message             |
| **meta.context**            | The context used when originating this event                          |
| **meta.level**              | N/A                                                                   |
| **meta.has\_children**      | Indicates if this event might potentially have child events under it. |
| **meta.id**                 | UUID of the event                                                     |
| **meta.parent**             | The UUID of the parent event if applicable                            |
| **meta.ancestors**          | Any event used to trigger this event                                  |
| **proposed\_change\_id**    | The ID of the proposed change                                         |
| **proposed\_change\_name**  | The name of the proposed change                                       |
| **proposed\_change\_state** | The state of the proposed change                                      |
| **thread\_id**              | The ID of the thread that was created or updated                      |
| **thread\_kind**            | The name of the thread that was created or updated                    |
| **action**                  | N/A                                                                   |

### Proposed Change Thread Updated Event[​](#proposed-change-thread-updated-event "Direct link to Proposed Change Thread Updated Event")

**Type**: infrahub.proposed\_change\_thread.updated **Description**: Event generated when a thread has been updated in a proposed change

**Uses node\_kind filter for webhooks**: `false`

| Key                         | Description                                                           |
| --------------------------- | --------------------------------------------------------------------- |
| **meta.branch**             | The branch on which originate this event                              |
| **meta.request\_id**        | N/A                                                                   |
| **meta.account\_id**        | The ID of the account triggering this event                           |
| **meta.initiator\_id**      | The worker identity of the initial sender of this message             |
| **meta.context**            | The context used when originating this event                          |
| **meta.level**              | N/A                                                                   |
| **meta.has\_children**      | Indicates if this event might potentially have child events under it. |
| **meta.id**                 | UUID of the event                                                     |
| **meta.parent**             | The UUID of the parent event if applicable                            |
| **meta.ancestors**          | Any event used to trigger this event                                  |
| **proposed\_change\_id**    | The ID of the proposed change                                         |
| **proposed\_change\_name**  | The name of the proposed change                                       |
| **proposed\_change\_state** | The state of the proposed change                                      |
| **thread\_id**              | The ID of the thread that was created or updated                      |
| **thread\_kind**            | The name of the thread that was created or updated                    |
| **action**                  | N/A                                                                   |

## Commit events[​](#commit-events "Direct link to Commit events")

### Commit Updated Event[​](#commit-updated-event "Direct link to Commit Updated Event")

**Type**: infrahub.repository.update\_commit **Description**: Event generated when the the commit within a repository has been updated.

**Uses node\_kind filter for webhooks**: `false`

| Key                    | Description                                                           |
| ---------------------- | --------------------------------------------------------------------- |
| **meta.branch**        | The branch on which originate this event                              |
| **meta.request\_id**   | N/A                                                                   |
| **meta.account\_id**   | The ID of the account triggering this event                           |
| **meta.initiator\_id** | The worker identity of the initial sender of this message             |
| **meta.context**       | The context used when originating this event                          |
| **meta.level**         | N/A                                                                   |
| **meta.has\_children** | Indicates if this event might potentially have child events under it. |
| **meta.id**            | UUID of the event                                                     |
| **meta.parent**        | The UUID of the parent event if applicable                            |
| **meta.ancestors**     | Any event used to trigger this event                                  |
| **commit**             | The commit the repository was updated to                              |
| **repository\_id**     | The ID of the repository                                              |
| **repository\_name**   | The name of the repository                                            |

## Validator events[​](#validator-events "Direct link to Validator events")

### Validator Failed Event[​](#validator-failed-event "Direct link to Validator Failed Event")

**Type**: infrahub.validator.failed **Description**: Event generated when an validator within a pipeline has completed successfully.

**Uses node\_kind filter for webhooks**: `true`

| Key                      | Description                                                           |
| ------------------------ | --------------------------------------------------------------------- |
| **meta.branch**          | The branch on which originate this event                              |
| **meta.request\_id**     | N/A                                                                   |
| **meta.account\_id**     | The ID of the account triggering this event                           |
| **meta.initiator\_id**   | The worker identity of the initial sender of this message             |
| **meta.context**         | The context used when originating this event                          |
| **meta.level**           | N/A                                                                   |
| **meta.has\_children**   | Indicates if this event might potentially have child events under it. |
| **meta.id**              | UUID of the event                                                     |
| **meta.parent**          | The UUID of the parent event if applicable                            |
| **meta.ancestors**       | Any event used to trigger this event                                  |
| **node\_id**             | The ID of the validator                                               |
| **kind**                 | The kind of the validator                                             |
| **proposed\_change\_id** | The ID of the proposed change                                         |

### Validator Passed Event[​](#validator-passed-event "Direct link to Validator Passed Event")

**Type**: infrahub.validator.passed **Description**: Event generated when an validator within a pipeline has completed successfully.

**Uses node\_kind filter for webhooks**: `true`

| Key                      | Description                                                           |
| ------------------------ | --------------------------------------------------------------------- |
| **meta.branch**          | The branch on which originate this event                              |
| **meta.request\_id**     | N/A                                                                   |
| **meta.account\_id**     | The ID of the account triggering this event                           |
| **meta.initiator\_id**   | The worker identity of the initial sender of this message             |
| **meta.context**         | The context used when originating this event                          |
| **meta.level**           | N/A                                                                   |
| **meta.has\_children**   | Indicates if this event might potentially have child events under it. |
| **meta.id**              | UUID of the event                                                     |
| **meta.parent**          | The UUID of the parent event if applicable                            |
| **meta.ancestors**       | Any event used to trigger this event                                  |
| **node\_id**             | The ID of the validator                                               |
| **kind**                 | The kind of the validator                                             |
| **proposed\_change\_id** | The ID of the proposed change                                         |

### Validator Started Event[​](#validator-started-event "Direct link to Validator Started Event")

**Type**: infrahub.validator.started **Description**: Event generated when an validator within a pipeline has started.

**Uses node\_kind filter for webhooks**: `true`

| Key                      | Description                                                           |
| ------------------------ | --------------------------------------------------------------------- |
| **meta.branch**          | The branch on which originate this event                              |
| **meta.request\_id**     | N/A                                                                   |
| **meta.account\_id**     | The ID of the account triggering this event                           |
| **meta.initiator\_id**   | The worker identity of the initial sender of this message             |
| **meta.context**         | The context used when originating this event                          |
| **meta.level**           | N/A                                                                   |
| **meta.has\_children**   | Indicates if this event might potentially have child events under it. |
| **meta.id**              | UUID of the event                                                     |
| **meta.parent**          | The UUID of the parent event if applicable                            |
| **meta.ancestors**       | Any event used to trigger this event                                  |
| **node\_id**             | The ID of the validator                                               |
| **kind**                 | The kind of the validator                                             |
| **proposed\_change\_id** | The ID of the proposed change                                         |

## Schema events[​](#schema-events "Direct link to Schema events")

### Schema Updated Event[​](#schema-updated-event "Direct link to Schema Updated Event")

**Type**: infrahub.schema.updated **Description**: Event generated when the schema within a branch has been updated.

**Uses node\_kind filter for webhooks**: `false`

| Key                    | Description                                                           |
| ---------------------- | --------------------------------------------------------------------- |
| **meta.branch**        | The branch on which originate this event                              |
| **meta.request\_id**   | N/A                                                                   |
| **meta.account\_id**   | The ID of the account triggering this event                           |
| **meta.initiator\_id** | The worker identity of the initial sender of this message             |
| **meta.context**       | The context used when originating this event                          |
| **meta.level**         | N/A                                                                   |
| **meta.has\_children** | Indicates if this event might potentially have child events under it. |
| **meta.id**            | UUID of the event                                                     |
| **meta.parent**        | The UUID of the parent event if applicable                            |
| **meta.ancestors**     | Any event used to trigger this event                                  |
| **branch\_name**       | The name of the branch                                                |
| **schema\_hash**       | Schema hash after the update                                          |
