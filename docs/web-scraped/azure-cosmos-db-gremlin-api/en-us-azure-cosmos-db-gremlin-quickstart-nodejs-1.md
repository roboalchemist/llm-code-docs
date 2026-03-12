# Source: https://learn.microsoft.com/en-us/azure/cosmos-db/gremlin/quickstart-nodejs?pivots=programming-language-js

Title: Quickstart: Node.js library - Azure Cosmos DB for Apache Gremlin

URL Source: https://learn.microsoft.com/en-us/azure/cosmos-db/gremlin/quickstart-nodejs?pivots=programming-language-js

Markdown Content:
Important

Are you looking for a database solution for **high-scale** scenarios with a 99.999% availability service level agreement (SLA), instant autoscale, and automatic failover across multiple regions? Consider [Azure Cosmos DB for NoSQL](https://learn.microsoft.com/en-us/azure/cosmos-db/overview).

Are you looking to implement an online analytical processing (OLAP) graph or migrate an existing Apache Gremlin application? Consider [Graph in Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/graph/overview).

Get started with the Azure Cosmos DB for Apache Gremlin client library for Node.js to store, manage, and query unstructured data. Follow the steps in this guide to create a new account, install a Node.js client library, connect to the account, perform common operations, and query your final sample data.

[Library source code](https://github.com/apache/tinkerpop/tree/master/gremlin-javascript/src/main/javascript/gremlin-javascript) | [Package (npm)](https://www.npmjs.com/package/gremlin)

*   An Azure subscription

    *   If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.

*   The latest version of the [Azure CLI](https://learn.microsoft.com/en-us/cli/azure) in [Azure Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell).

    *   If you prefer to run CLI reference commands locally, sign in to the Azure CLI by using the [`az login`](https://learn.microsoft.com/en-us/cli/azure/reference-index#az-login) command.

*   Node.js 22 or newer

First, set up the account and development environment for this guide. This section walks you through the process of creating an account, getting its credentials, and then preparing your development environment.

Start by creating an API for Apache Gremlin account. Once the account is created, create the database and graph resources.

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/cosmos-db/gremlin/quickstart-nodejs?pivots=programming-language-js#tabpanel_1_azure-cli)
*   [Azure portal](https://learn.microsoft.com/en-us/azure/cosmos-db/gremlin/quickstart-nodejs?pivots=programming-language-js#tabpanel_1_azure-portal)

1.   If you don't already have a target resource group, use the `az group create` command to create a new resource group in your subscription.

```
az group create \
    --name "<resource-group-name>" \
    --location "<location>"
```
2.   Use the `az cosmosdb create` command to create a new Azure Cosmos DB for Apache Gremlin account with default settings.

```
az cosmosdb create \
    --resource-group "<resource-group-name>" \
    --name "<account-name>" \
    --locations "regionName=<location>" \
    --capabilities "EnableGremlin"
```
3.   Create a new database using `az cosmosdb gremlin database create` named `cosmicworks`.

```
az cosmosdb gremlin database create \
    --resource-group "<resource-group-name>" \
    --account-name "<account-name>" \
    --name "cosmicworks"
```
4.   Use the `az cosmosdb gremlin graph create` command to create a new graph named `products`.

```
az cosmosdb gremlin graph create \
    --resource-group "<resource-group-name>" \
    --account-name "<account-name>" \
    --database-name "cosmicworks" \
    --name "products" \
    --partition-key-path "/category"
```

Now, get the password for the client library to use to create a connection to the recently created account.

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/cosmos-db/gremlin/quickstart-nodejs?pivots=programming-language-js#tabpanel_1_azure-cli)
*   [Azure portal](https://learn.microsoft.com/en-us/azure/cosmos-db/gremlin/quickstart-nodejs?pivots=programming-language-js#tabpanel_1_azure-portal)

1.   Use `az cosmosdb show` to get the host for the account.

```
az cosmosdb show \
    --resource-group "<resource-group-name>" \
    --name "<account-name>" \
    --query "{host:name}"
```
2.   Record the value of the `host` property from the previous commands' output. This property' value is the **host** you use later in this guide to connect to the account with the library.

3.   Use `az cosmosdb keys list` to get the **keys** for the account.

```
az cosmosdb keys list \
    --resource-group "<resource-group-name>" \
    --name "<account-name>" \
    --type "keys"
```
4.   Record the value of the `primaryMasterKey` property from the previous commands' output. This property's value is the **key** you use later in this guide to connect to the account with the library.

Then, configure your development environment with a new project and the client library. This step is the last required prerequisite before moving on to the rest of this guide.

1.   Start in an empty folder.

2.   Initialize a new module.

```
npm init es6 --yes
```
3.   Install the `gremlin` package from Node Package Manager (npm).

```
npm install --save gremlin
```
4.   Create the _index.js_ file.

1.   Start in an empty folder.

2.   Initialize a new module.

```
npm init es6 --yes
```
3.   Install the `typescript` package from Node Package Manager (npm).

```
npm install --save-dev typescript
```
4.   Install the `tsx` package from npm.

```
npm install --save-dev tsx
```
5.   Install the `gremlin` package from npm.

```
npm install --save gremlin
```
6.   Install the `@types/node` package from npm.

```
npm install --save-dev @types/node
```
7.   Install the `@types/gremlin` package from npm.

```
npm install --save-dev @types/gremlin
```
8.   Initialize the TypeScript project using the compiler (`tsc`).

```
npx tsc --init --target es2017 --module es2022 --moduleResolution nodenext
```
9.   Create the _index.ts_ file.

|  | Description |
| --- | --- |
| `DriverRemoteConnection` | Represents the connection to the Gremlin server |
| `GraphTraversalSource` | Used to construct and execute Gremlin traversals |

*   [Authenticate client](https://learn.microsoft.com/en-us/azure/cosmos-db/gremlin/quickstart-nodejs?pivots=programming-language-js#authenticate-client)
*   [Insert data](https://learn.microsoft.com/en-us/azure/cosmos-db/gremlin/quickstart-nodejs?pivots=programming-language-js#insert-data)
*   [Read data](https://learn.microsoft.com/en-us/azure/cosmos-db/gremlin/quickstart-nodejs?pivots=programming-language-js#read-data)
*   [Query data](https://learn.microsoft.com/en-us/azure/cosmos-db/gremlin/quickstart-nodejs?pivots=programming-language-js#query-data)

Start by authenticating the client using the credentials gathered earlier in this guide.

1.   Open the _index.js_ file in your integrated development environment (IDE).

2.   Import the `gremlin` package and required types:

```
import gremlin from 'gremlin';
const { Client, auth } = gremlin.driver;
const { PlainTextSaslAuthenticator } = auth;
```
3.   Create string variables for the credentials collected earlier in this guide. Name the variables `hostname` and `primaryKey`.

```
const hostname = '<host>';
const primaryKey = '<key>';
```
4.   Create an object of type `PlainTextSaslAuthenticator` using the credentials and configuration variables created in the previous steps. Store the object in a variable named `authenticator`.

```
const authenticator = new PlainTextSaslAuthenticator(
    '/dbs/cosmicworks/colls/products',
    primaryKey
);
```
5.   Create a `Client` object using the authenticator variable. Name the variable `client`.

```
const client = new Client(
    `wss://${hostname}.gremlin.cosmos.azure.com:443/`,
    {
        authenticator,
        traversalsource: 'g',
        rejectUnauthorized: true,
        mimeType: 'application/vnd.gremlin-v2.0+json'
    }
);
```

1.   Open the _index.ts_ file in your integrated development environment (IDE).

2.   Import the `gremlin` package and required types:

```
import gremlin from 'gremlin';
const { Client, auth } = gremlin.driver;
const { PlainTextSaslAuthenticator } = auth;
```
3.   Create string variables for the credentials collected earlier in this guide. Name the variables `hostname` and `primaryKey`.

```
const hostname: string = '<host>';
const primaryKey: string = '<key>';
```
4.   Create an object of type `PlainTextSaslAuthenticator` using the credentials and configuration variables created in the previous steps. Store the object in a variable named `authenticator`.

```
const authenticator = new PlainTextSaslAuthenticator(
    '/dbs/cosmicworks/colls/products',
    primaryKey
);
```
5.   Create a `Client` object using the authenticator variable. Name the variable `client`.

```
const client = new Client(
    `wss://${hostname}.gremlin.cosmos.azure.com:443/`,
    {
        authenticator,
        traversalsource: 'g',
        rejectUnauthorized: true,
        mimeType: 'application/vnd.gremlin-v2.0+json'
    }
);
```

Next, insert new vertex and edge data into the graph. Before creating the new data, clear the graph of any existing data.

1.   Run the `g.V().drop()` query to clear all vertices and edges from the graph.

```
await client.submit('g.V().drop()');
```
2.   Create a Gremlin query that adds a vertex.

```
const insert_vertex_query = `
    g.addV('product')
        .property('id', prop_id)
        .property('name', prop_name)
        .property('category', prop_category)
        .property('quantity', prop_quantity)
        .property('price', prop_price)
        .property('clearance', prop_clearance)
`;
```
3.   Add a vertex for a single product.

```
await client.submit(insert_vertex_query, {
    prop_id: 'aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb',
    prop_name: 'Yamba Surfboard',
    prop_category: 'gear-surf-surfboards',
    prop_quantity: 12,
    prop_price: 850.00,
    prop_clearance: false,
});
```
4.   Add two more vertices for two extra products.

```
await client.submit(insert_vertex_query, {
    prop_id: 'bbbbbbbb-1111-2222-3333-cccccccccccc',
    prop_name: 'Montau Turtle Surfboard',
    prop_category: 'gear-surf-surfboards',
    prop_quantity: 5,
    prop_price: 600.00,
    prop_clearance: true,
});

await client.submit(insert_vertex_query, {
    prop_id: 'cccccccc-2222-3333-4444-dddddddddddd',
    prop_name: 'Noosa Surfboard',
    prop_category: 'gear-surf-surfboards',
    prop_quantity: 31,
    prop_price: 1100.00,
    prop_clearance: false,
});
```
5.   Create another Gremlin query that adds an edge.

```
const insert_edge_query = `
    g.V([prop_partition_key, prop_source_id])
        .addE('replaces')
        .to(g.V([prop_partition_key, prop_target_id]))
`;
```
6.   Add two edges.

```
await client.submit(insert_edge_query, {
    prop_partition_key: 'gear-surf-surfboards',
    prop_source_id: 'bbbbbbbb-1111-2222-3333-cccccccccccc',
    prop_target_id: 'aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb',
});

await client.submit(insert_edge_query, {
    prop_partition_key: 'gear-surf-surfboards',
    prop_source_id: 'bbbbbbbb-1111-2222-3333-cccccccccccc',
    prop_target_id: 'cccccccc-2222-3333-4444-dddddddddddd',
});
```

1.   Run the `g.V().drop()` query to clear all vertices and edges from the graph.

```
await client.submit('g.V().drop()');
```
2.   Create a Gremlin query that adds a vertex.

```
const insert_vertex_query: string = `
    g.addV('product')
        .property('id', prop_id)
        .property('name', prop_name)
        .property('category', prop_category)
        .property('quantity', prop_quantity)
        .property('price', prop_price)
        .property('clearance', prop_clearance)
`;
```
3.   Add a vertex for a single product.

```
await client.submit(insert_vertex_query, {
    prop_id: 'aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb',
    prop_name: 'Yamba Surfboard',
    prop_category: 'gear-surf-surfboards',
    prop_quantity: 12,
    prop_price: 850.00,
    prop_clearance: false,
});
```
4.   Add two more vertices for two extra products.

```
await client.submit(insert_vertex_query, {
    prop_id: 'bbbbbbbb-1111-2222-3333-cccccccccccc',
    prop_name: 'Montau Turtle Surfboard',
    prop_category: 'gear-surf-surfboards',
    prop_quantity: 5,
    prop_price: 600.00,
    prop_clearance: true,
});

await client.submit(insert_vertex_query, {
    prop_id: 'cccccccc-2222-3333-4444-dddddddddddd',
    prop_name: 'Noosa Surfboard',
    prop_category: 'gear-surf-surfboards',
    prop_quantity: 31,
    prop_price: 1100.00,
    prop_clearance: false,
});
```
5.   Create another Gremlin query that adds an edge.

```
const insert_edge_query: string = `
    g.V([prop_partition_key, prop_source_id])
        .addE('replaces')
        .to(g.V([prop_partition_key, prop_target_id]))
`;
```
6.   Add two edges.

```
await client.submit(insert_edge_query, {
    prop_partition_key: 'gear-surf-surfboards',
    prop_source_id: 'bbbbbbbb-1111-2222-3333-cccccccccccc',
    prop_target_id: 'aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb',
});

await client.submit(insert_edge_query, {
    prop_partition_key: 'gear-surf-surfboards',
    prop_source_id: 'bbbbbbbb-1111-2222-3333-cccccccccccc',
    prop_target_id: 'cccccccc-2222-3333-4444-dddddddddddd',
});
```

Then, read data that was previously inserted into the graph.

1.   Create a query that reads a vertex using the unique identifier and partition key value.

```
const read_vertex_query = 'g.V([prop_partition_key, prop_id])';
```
2.   Then, read a vertex by supplying the required parameters.

```
let read_results = await client.submit(read_vertex_query, {
    prop_partition_key: 'gear-surf-surfboards',
    prop_id: 'aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb',
});

let matched_item = read_results._items[0];
```

1.   Create a query that reads a vertex using the unique identifier and partition key value.

```
const read_vertex_query: string = 'g.V([prop_partition_key, prop_id])';
```
2.   Then, read a vertex by supplying the required parameters.

```
let read_results = await client.submit(read_vertex_query, {
    prop_partition_key: 'gear-surf-surfboards',
    prop_id: 'aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb',
});

let matched_item = read_results._items[0];
```

Finally, use a query to find all data that matches a specific traversal or filter in the graph.

1.   Create a query that finds all vertices that traverse out from a specific vertex.

```
const find_vertices_query = `
    g.V().hasLabel('product')
        .has('category', prop_partition_key)
        .has('name', prop_name)
        .outE('replaces').inV()
`;
```
2.   Execute the query specifying the `Montau Turtle Surfboard` product.

```
let find_results = await client.submit(find_vertices_query, {
    prop_partition_key: 'gear-surf-surfboards',
    prop_name: 'Montau Turtle Surfboard',
});
```
3.   Iterate over the query results.

```
for (const item of find_results._items) {
    // Do something here with each result
}
```

1.   Create a query that finds all vertices that traverse out from a specific vertex.

```
const find_vertices_query: string = `
    g.V().hasLabel('product')
        .has('category', prop_partition_key)
        .has('name', prop_name)
        .outE('replaces').inV()
`;
```
2.   Execute the query specifying the `Montau Turtle Surfboard` product.

```
let find_results = await client.submit(find_vertices_query, {
    prop_partition_key: 'gear-surf-surfboards',
    prop_name: 'Montau Turtle Surfboard',
});
```
3.   Iterate over the query results.

```
for (const item of find_results._items) {
    // Do something here with each result
}
```

Run the newly created application using a terminal in your application directory.

```
node index.js
```

```
npx tsx index.ts
```

When you no longer need the account, remove the account from your Azure subscription by **deleting** the resource.

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/cosmos-db/gremlin/quickstart-nodejs?pivots=programming-language-js#tabpanel_1_azure-cli)
*   [Azure portal](https://learn.microsoft.com/en-us/azure/cosmos-db/gremlin/quickstart-nodejs?pivots=programming-language-js#tabpanel_1_azure-portal)

```
az cosmosdb delete \
    --resource-group "<resource-group-name>" \
    --name "<account-name>"
```
