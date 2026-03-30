# Source: https://docs.infrahub.app/mcp/references/methods.md

# Infrahub MCP methods

## Schema[​](#schema "Direct link to Schema")

### get\_schema\_mapping[​](#get_schema_mapping "Direct link to get_schema_mapping")

### Capabilities[​](#capabilities "Direct link to Capabilities")

* read-only
* idempotent
* no destroy

List all schema nodes and generics available in Infrahub.

### Parameters[​](#parameters "Direct link to Parameters")

* **branch** (string): branch to read from; default is the server’s default branch

### get\_schema[​](#get_schema "Direct link to get_schema")

### Capabilities[​](#capabilities-1 "Direct link to Capabilities")

* read-only
* idempotent
* no destroy

Retrieve the full schema for a specific kind (attributes, relationships, and types).

### Parameters[​](#parameters-1 "Direct link to Parameters")

* **kind** (string, required): schema Kind to retrieve
* **branch** (string): branch to read from; default is the server’s default branch

### get\_schemas[​](#get_schemas "Direct link to get_schemas")

### Capabilities[​](#capabilities-2 "Direct link to Capabilities")

* read-only
* idempotent
* no destroy

Retrieve all schemas, optionally excluding Profiles and Templates.

### Parameters[​](#parameters-2 "Direct link to Parameters")

* **branch** (string): branch to read from; default is the server’s default branch
* **exclude\_profiles** (boolean, default: true): omit Profile schemas
* **exclude\_templates** (boolean, default: true): omit Template schemas

## Nodes[​](#nodes "Direct link to Nodes")

### get\_nodes[​](#get_nodes "Direct link to get_nodes")

### Capabilities[​](#capabilities-3 "Direct link to Capabilities")

* read-only
* idempotent
* no destroy

Get all objects of a specific kind from Infrahub. Use `get_schema_mapping` to discover kinds and `get_node_filters` to discover filter keys.

### Parameters[​](#parameters-3 "Direct link to Parameters")

* **kind** (string, required): kind of the objects to retrieve
* **branch** (string): branch name (default: server’s default branch)
* **filters** (object): dictionary of filters to apply
* **partial\_match** (boolean, default: false): enable substring matches for string filters

### get\_node\_filters[​](#get_node_filters "Direct link to get_node_filters")

### Capabilities[​](#capabilities-4 "Direct link to Capabilities")

* read-only
* idempotent
* no destroy

Retrieve all available filters for a specific schema node kind.

### Parameters[​](#parameters-4 "Direct link to Parameters")

* **kind** (string, required): node kind (example: "Router")
* **branch** (string): branch name

info

* Attribute filters: `attribute__value`
* Relationship filters: `relationship__attribute__value`
* Filters starting with `parent__` refer to a related generic node
* Use `get_schema` to inspect peer kinds and attributes used in relationship filters

### get\_related\_nodes[​](#get_related_nodes "Direct link to get_related_nodes")

### Capabilities[​](#capabilities-5 "Direct link to Capabilities")

* read-only
* idempotent
* no destroy

Retrieve related nodes by relation name for a given kind.

### Parameters[​](#parameters-5 "Direct link to Parameters")

* **kind** (string, required): source node kind (example: "Device")
* **relation** (string, required): relationship name to follow (example: "interfaces")
* **filters** (object): filters applied to the **source** nodes before following the relation
* **branch** (string): branch name

## Branches[​](#branches "Direct link to Branches")

### branch\_create[​](#branch_create "Direct link to branch_create")

### Capabilities[​](#capabilities-6 "Direct link to Capabilities")

* write
* idempotent
* no destroy

Create a new branch in Infrahub.

### Parameters[​](#parameters-6 "Direct link to Parameters")

* **name** (string, required): name of the branch to create
* **sync\_with\_git** (boolean, default: false): whether to sync the branch with Git

### get\_branches[​](#get_branches "Direct link to get_branches")

### Capabilities[​](#capabilities-7 "Direct link to Capabilities")

* read-only
* idempotent
* no destroy

Retrieve all branches from Infrahub.

## GraphQL[​](#graphql "Direct link to GraphQL")

### get\_graphql\_schema[​](#get_graphql_schema "Direct link to get_graphql_schema")

### Capabilities[​](#capabilities-8 "Direct link to Capabilities")

* read-only
* idempotent
* no destroy

Retrieve the GraphQL schema from Infrahub as a string.

### query\_graphql[​](#query_graphql "Direct link to query_graphql")

### Capabilities[​](#capabilities-9 "Direct link to Capabilities")

* may write (depends on operation)
* idempotent for queries; non-idempotent for mutations
* destructive potential depends on mutation

Execute a GraphQL operation against Infrahub.

### Parameters[​](#parameters-7 "Direct link to Parameters")

* **query** (string, required): GraphQL document (use `query { ... }` for reads, `mutation { ... }` for writes)
