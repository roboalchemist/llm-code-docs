# Source: https://kreya.app/docs/operations.md

# Operations

Operations are the core feature of Kreya. They correspondend to "service methods":

* For gRPC, an operation corresponds to a gRPC service method, e.g. `MyService.GetList()`
* For GraphQL, an operation corresponds to a query, mutation or subscription
* For REST, an operation is an HTTP endpoint, e.g. `POST https://example.com/api/invoices`
* For WebSocket, an operation is a WebSocket connection, e.g. `wss://example.com/ws`

You may create multiple operations for one "service method".

## Creating operations[​](#creating-operations "Direct link to Creating operations")

With REST and WebSocket operations, you can simply create operations from scratch. However, this can be a hassle to do manually.

If you have an API definition, such as an OpenAPI document, you can [import operations](/docs/importers.md) automatically. For gRPC, this is required, as the API definitions are needed for (de-)serialization.

## Organization[​](#organization "Direct link to Organization")

The operations can be organised into directories. Note that this directory structure is stored and read directly from the file system. That is why some characters are forbidden in folder and file names and why the operations are always sorted alphabetically.

When organizing operations into directories, take a look at the [directory settings](/docs/default-settings.md). With this Kreya feature, you can apply settings to all operations within a directory.
