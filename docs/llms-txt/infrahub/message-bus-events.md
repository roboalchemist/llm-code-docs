# Source: https://docs.infrahub.app/reference/message-bus-events.md

# Message bus events

This document provides detailed documentation for all events used in the Infrahub message bus system.

info

For more detailed explanations on how these events are used within Infrahub, see the [bus event handling](/topics/bus-event-handling.md) topic.

## Messages events[​](#messages-events "Direct link to Messages events")

### Git File[​](#git-file "Direct link to Git File")

#### Event git.file.get[​](#event-gitfileget "Direct link to Event git.file.get")

**Description**: Read a file from a Git repository.

**Priority**: 4

| Key                  | Description                                 | Type   | Default Value |
| -------------------- | ------------------------------------------- | ------ | ------------- |
| **meta**             | Meta properties for the message             | N/A    | None          |
| **commit**           | The commit id to use to access the file     | string | None          |
| **file**             | The path and filename within the repository | string | None          |
| **repository\_id**   | The unique ID of the Repository             | string | None          |
| **repository\_name** | The name of the repository                  | string | None          |
| **repository\_kind** | The kind of the repository                  | string | None          |

### Git Repository[​](#git-repository "Direct link to Git Repository")

#### Event git.repository.connectivity[​](#event-gitrepositoryconnectivity "Direct link to Event git.repository.connectivity")

**Description**: Validate connectivity and credentials to remote repository

**Priority**: 3

| Key                      | Description                     | Type   | Default Value |
| ------------------------ | ------------------------------- | ------ | ------------- |
| **meta**                 | Meta properties for the message | N/A    | None          |
| **repository\_name**     | The name of the repository      | string | None          |
| **repository\_location** | The location of repository      | string | None          |

### Refresh Git[​](#refresh-git "Direct link to Refresh Git")

#### Event refresh.git.fetch[​](#event-refreshgitfetch "Direct link to Event refresh.git.fetch")

**Description**: Fetch a repository remote changes.

**Priority**: 3

| Key                        | Description                                                      | Type   | Default Value |
| -------------------------- | ---------------------------------------------------------------- | ------ | ------------- |
| **meta**                   | Meta properties for the message                                  | N/A    | None          |
| **location**               | The external URL of the repository                               | string | None          |
| **repository\_id**         | The unique ID of the repository                                  | string | None          |
| **repository\_name**       | The name of the repository                                       | string | None          |
| **repository\_kind**       | The type of repository                                           | string | None          |
| **infrahub\_branch\_name** | Infrahub branch on which to sync the remote repository           | string | None          |
| **infrahub\_branch\_id**   | Id of the Infrahub branch on which to sync the remote repository | string | None          |

### Refresh Registry[​](#refresh-registry "Direct link to Refresh Registry")

#### Event refresh.registry.branches[​](#event-refreshregistrybranches "Direct link to Event refresh.registry.branches")

**Description**: Sent to indicate that the registry should be refreshed and new branch data loaded.

**Priority**: 3

| Key      | Description                     | Type | Default Value |
| -------- | ------------------------------- | ---- | ------------- |
| **meta** | Meta properties for the message | N/A  | None          |

#### Event refresh.registry.rebased\_branch[​](#event-refreshregistryrebased_branch "Direct link to Event refresh.registry.rebased_branch")

**Description**: Sent to refresh a rebased branch within the local registry.

**Priority**: 3

| Key        | Description                     | Type   | Default Value |
| ---------- | ------------------------------- | ------ | ------------- |
| **meta**   | Meta properties for the message | N/A    | None          |
| **branch** | The branch that was rebased     | string | None          |

### Send Echo[​](#send-echo "Direct link to Send Echo")

#### Event send.echo.request[​](#event-sendechorequest "Direct link to Event send.echo.request")

**Description**: Sent a echo request, a ping message for example.

**Priority**: 5

| Key         | Description                     | Type   | Default Value |
| ----------- | ------------------------------- | ------ | ------------- |
| **meta**    | Meta properties for the message | N/A    | None          |
| **message** | The message to send             | string | None          |

## Responses events[​](#responses-events "Direct link to Responses events")

### Git File[​](#git-file-1 "Direct link to Git File")

#### Event git.file.get[​](#event-gitfileget-1 "Direct link to Event git.file.get")

**Priority**: 4

| Key                     | Description                                                                                                            | Type    | Default Value |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------- | ------------- |
| **meta**                | Meta properties for the message                                                                                        | N/A     | None          |
| **passed**              | N/A                                                                                                                    | boolean | True          |
| **routing\_key**        | N/A                                                                                                                    | string  | git.file.get  |
| **data.content**        | N/A                                                                                                                    | N/A     | None          |
| **data.error\_message** | N/A                                                                                                                    | N/A     | None          |
| **data.http\_code**     | N/A                                                                                                                    | N/A     | None          |
| **errors**              | N/A                                                                                                                    | array   | None          |
| **initial\_message**    | Initial message in dict format, the primary goal of this field is to provide additional context when there is an error | N/A     | None          |

### Send Echo[​](#send-echo-1 "Direct link to Send Echo")

#### Event send.echo.request[​](#event-sendechorequest-1 "Direct link to Event send.echo.request")

**Priority**: 5

| Key                  | Description                                                                                                            | Type    | Default Value     |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------- | ----------------- |
| **meta**             | Meta properties for the message                                                                                        | N/A     | None              |
| **passed**           | N/A                                                                                                                    | boolean | True              |
| **routing\_key**     | N/A                                                                                                                    | string  | send.echo.request |
| **data.response**    | The response string                                                                                                    | string  | None              |
| **errors**           | N/A                                                                                                                    | array   | None              |
| **initial\_message** | Initial message in dict format, the primary goal of this field is to provide additional context when there is an error | N/A     | None              |
