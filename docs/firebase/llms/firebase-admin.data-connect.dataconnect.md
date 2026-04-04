# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.dataconnect.md.txt

The Firebase`DataConnect`service interface.

**Signature:**  

    export declare class DataConnect 

## Properties

|                                                                    Property                                                                    | Modifiers |                                                                       Type                                                                        | Description |
|------------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [app](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.dataconnect.md#dataconnectapp)                         |           | App                                                                                                                                               |             |
| [connectorConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.dataconnect.md#dataconnectconnectorconfig) |           | [ConnectorConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.connectorconfig.md#connectorconfig_interface) |             |

## Methods

|                                                                                  Method                                                                                  | Modifiers |                                                                                                                                    Description                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [executeGraphql(query, options)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.dataconnect.md#dataconnectexecutegraphql)             |           | Execute an arbitrary GraphQL query or mutation                                                                                                                                                                                                                                    |
| [executeGraphqlRead(query, options)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.dataconnect.md#dataconnectexecutegraphqlread)     |           | Execute an arbitrary read-only GraphQL query                                                                                                                                                                                                                                      |
| [executeMutation(name, options)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.dataconnect.md#dataconnectexecutemutation)            |           | Executes a GraphQL mutation. The mutation must be defined in your Data Connect GraphQL files. Optionally, you can provide auth impersonation details. If you don't specify a value for this option, the query will run with admin privileges and will ignore all auth directives. |
| [executeMutation(name, variables, options)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.dataconnect.md#dataconnectexecutemutation) |           | Executes a GraphQL mutation. The mutation must be defined in your Data Connect GraphQL files. Optionally, you can provide auth impersonation details. If you don't specify a value for this option, the query will run with admin privileges and will ignore all auth directives. |
| [executeQuery(name, options)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.dataconnect.md#dataconnectexecutequery)                  |           | Executes a GraphQL query. The query must be defined in your Data Connect GraphQL files. Optionally, you can provide auth impersonation details. If you don't specify a value for this option, the query will run with admin privileges and will ignore all auth directives.       |
| [executeQuery(name, variables, options)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.dataconnect.md#dataconnectexecutequery)       |           | Executes a GraphQL query. The query must be defined in your Data Connect GraphQL files. Optionally, you can provide auth impersonation details. If you don't specify a value for this option, the query will run with admin privileges and will ignore all auth directives.       |
| [insert(tableName, variables)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.dataconnect.md#dataconnectinsert)                       |           | Insert a single row into the specified table.                                                                                                                                                                                                                                     |
| [insertMany(tableName, variables)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.dataconnect.md#dataconnectinsertmany)               |           | Insert multiple rows into the specified table.                                                                                                                                                                                                                                    |
| [upsert(tableName, variables)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.dataconnect.md#dataconnectupsert)                       |           | Insert a single row into the specified table, or update it if it already exists.                                                                                                                                                                                                  |
| [upsertMany(tableName, variables)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.dataconnect.md#dataconnectupsertmany)               |           | Insert multiple rows into the specified table, or update them if they already exist.                                                                                                                                                                                              |

## DataConnect.app

**Signature:**  

    readonly app: App;

## DataConnect.connectorConfig

**Signature:**  

    readonly connectorConfig: ConnectorConfig;

## DataConnect.executeGraphql()

Execute an arbitrary GraphQL query or mutation

**Signature:**  

    executeGraphql<GraphqlResponse, Variables>(query: string, options?: GraphqlOptions<Variables>): Promise<ExecuteGraphqlResponse<GraphqlResponse>>;

### Parameters

| Parameter |                                                                            Type                                                                             |                                                                                            Description                                                                                            |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| query     | string                                                                                                                                                      | The GraphQL query or mutation.                                                                                                                                                                    |
| options   | [GraphqlOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.graphqloptions.md#graphqloptions_interface)\<Variables\> | Optional[GraphqlOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.graphqloptions.md#graphqloptions_interface)when executing a GraphQL query or mutation. |

**Returns:**

Promise\<[ExecuteGraphqlResponse](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.executegraphqlresponse.md#executegraphqlresponse_interface)\<GraphqlResponse\>\>

A promise that fulfills with a`ExecuteGraphqlResponse`.

## DataConnect.executeGraphqlRead()

Execute an arbitrary read-only GraphQL query

**Signature:**  

    executeGraphqlRead<GraphqlResponse, Variables>(query: string, options?: GraphqlOptions<Variables>): Promise<ExecuteGraphqlResponse<GraphqlResponse>>;

### Parameters

| Parameter |                                                                            Type                                                                             |                                                                                           Description                                                                                           |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| query     | string                                                                                                                                                      | The GraphQL read-only query.                                                                                                                                                                    |
| options   | [GraphqlOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.graphqloptions.md#graphqloptions_interface)\<Variables\> | Optional[GraphqlOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.graphqloptions.md#graphqloptions_interface)when executing a read-only GraphQL query. |

**Returns:**

Promise\<[ExecuteGraphqlResponse](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.executegraphqlresponse.md#executegraphqlresponse_interface)\<GraphqlResponse\>\>

A promise that fulfills with a`ExecuteGraphqlResponse`.

## DataConnect.executeMutation()

Executes a GraphQL mutation. The mutation must be defined in your Data Connect GraphQL files. Optionally, you can provide auth impersonation details. If you don't specify a value for this option, the query will run with admin privileges and will ignore all auth directives.

**Signature:**  

    executeMutation<Data>(name: string, options?: OperationOptions): Promise<ExecuteOperationResponse<Data>>;

### Parameters

| Parameter |                                                                         Type                                                                         |                                Description                                 |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| name      | string                                                                                                                                               | The name of the defined mutation to execute.                               |
| options   | [OperationOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.operationoptions.md#operationoptions_interface) | The GraphQL options, must include operationName and impersonation details. |

**Returns:**

Promise\<[ExecuteOperationResponse](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.executeoperationresponse.md#executeoperationresponse_interface)\<Data\>\>

A promise that fulfills with the GraphQL response.

## DataConnect.executeMutation()

Executes a GraphQL mutation. The mutation must be defined in your Data Connect GraphQL files. Optionally, you can provide auth impersonation details. If you don't specify a value for this option, the query will run with admin privileges and will ignore all auth directives.

**Signature:**  

    executeMutation<Data, Variables>(name: string, variables: Variables, options?: OperationOptions): Promise<ExecuteOperationResponse<Data>>;

### Parameters

| Parameter |                                                                         Type                                                                         |                                        Description                                        |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| name      | string                                                                                                                                               | The name of the defined mutation to execute.                                              |
| variables | Variables                                                                                                                                            | The variables for the mutation. May be optional if the mutation's variables are optional. |
| options   | [OperationOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.operationoptions.md#operationoptions_interface) | The GraphQL options, must include operationName and impersonation details.                |

**Returns:**

Promise\<[ExecuteOperationResponse](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.executeoperationresponse.md#executeoperationresponse_interface)\<Data\>\>

A promise that fulfills with the GraphQL response.

## DataConnect.executeQuery()

Executes a GraphQL query. The query must be defined in your Data Connect GraphQL files. Optionally, you can provide auth impersonation details. If you don't specify a value for this option, the query will run with admin privileges and will ignore all auth directives.

**Signature:**  

    executeQuery<Data>(name: string, options?: OperationOptions): Promise<ExecuteOperationResponse<Data>>;

### Parameters

| Parameter |                                                                         Type                                                                         |                                Description                                 |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| name      | string                                                                                                                                               | The name of the defined query to execute.                                  |
| options   | [OperationOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.operationoptions.md#operationoptions_interface) | The GraphQL options, must include operationName and impersonation details. |

**Returns:**

Promise\<[ExecuteOperationResponse](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.executeoperationresponse.md#executeoperationresponse_interface)\<Data\>\>

A promise that fulfills with the GraphQL response.

## DataConnect.executeQuery()

Executes a GraphQL query. The query must be defined in your Data Connect GraphQL files. Optionally, you can provide auth impersonation details. If you don't specify a value for this option, the query will run with admin privileges and will ignore all auth directives.

**Signature:**  

    executeQuery<Data, Variables>(name: string, variables: Variables, options?: OperationOptions): Promise<ExecuteOperationResponse<Data>>;

### Parameters

| Parameter |                                                                         Type                                                                         |                                     Description                                     |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| name      | string                                                                                                                                               | The name of the defined query to execute.                                           |
| variables | Variables                                                                                                                                            | The variables for the query. May be optional if the query's variables are optional. |
| options   | [OperationOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.operationoptions.md#operationoptions_interface) | The GraphQL options, must include operationName and impersonation details.          |

**Returns:**

Promise\<[ExecuteOperationResponse](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.executeoperationresponse.md#executeoperationresponse_interface)\<Data\>\>

A promise that fulfills with the GraphQL response.

## DataConnect.insert()

Insert a single row into the specified table.

**Signature:**  

    insert<GraphQlResponse, Variables extends object>(tableName: string, variables: Variables): Promise<ExecuteGraphqlResponse<GraphQlResponse>>;

### Parameters

| Parameter |   Type    |                                Description                                 |
|-----------|-----------|----------------------------------------------------------------------------|
| tableName | string    | The name of the table to insert data into.                                 |
| variables | Variables | The data object to insert. The keys should correspond to the column names. |

**Returns:**

Promise\<[ExecuteGraphqlResponse](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.executegraphqlresponse.md#executegraphqlresponse_interface)\<GraphQlResponse\>\>

A promise that fulfills with a`ExecuteGraphqlResponse`.

## DataConnect.insertMany()

Insert multiple rows into the specified table.

**Signature:**  

    insertMany<GraphQlResponse, Variables extends Array<unknown>>(tableName: string, variables: Variables): Promise<ExecuteGraphqlResponse<GraphQlResponse>>;

### Parameters

| Parameter |   Type    |                                          Description                                          |
|-----------|-----------|-----------------------------------------------------------------------------------------------|
| tableName | string    | The name of the table to insert data into.                                                    |
| variables | Variables | An array of data objects to insert. Each object's keys should correspond to the column names. |

**Returns:**

Promise\<[ExecuteGraphqlResponse](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.executegraphqlresponse.md#executegraphqlresponse_interface)\<GraphQlResponse\>\>

A promise that fulfills with a`ExecuteGraphqlResponse`.

## DataConnect.upsert()

Insert a single row into the specified table, or update it if it already exists.

**Signature:**  

    upsert<GraphQlResponse, Variables extends object>(tableName: string, variables: Variables): Promise<ExecuteGraphqlResponse<GraphQlResponse>>;

### Parameters

| Parameter |   Type    |                                Description                                 |
|-----------|-----------|----------------------------------------------------------------------------|
| tableName | string    | The name of the table to upsert data into.                                 |
| variables | Variables | The data object to upsert. The keys should correspond to the column names. |

**Returns:**

Promise\<[ExecuteGraphqlResponse](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.executegraphqlresponse.md#executegraphqlresponse_interface)\<GraphQlResponse\>\>

A promise that fulfills with a`ExecuteGraphqlResponse`.

## DataConnect.upsertMany()

Insert multiple rows into the specified table, or update them if they already exist.

**Signature:**  

    upsertMany<GraphQlResponse, Variables extends Array<unknown>>(tableName: string, variables: Variables): Promise<ExecuteGraphqlResponse<GraphQlResponse>>;

### Parameters

| Parameter |   Type    |                                          Description                                          |
|-----------|-----------|-----------------------------------------------------------------------------------------------|
| tableName | string    | The name of the table to upsert data into.                                                    |
| variables | Variables | An array of data objects to upsert. Each object's keys should correspond to the column names. |

**Returns:**

Promise\<[ExecuteGraphqlResponse](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.executegraphqlresponse.md#executegraphqlresponse_interface)\<GraphQlResponse\>\>

A promise that fulfills with a`ExecuteGraphqlResponse`.