# Source: https://chillicream.com/docs/hotchocolate/v14/performance/automatic-persisted-operations

Title: Automatic persisted operations - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/performance/automatic-persisted-operations

Markdown Content:
This guide will walk you through how automatic persisted operations work and how you can set them up with the Hot Chocolate GraphQL server.

[](https://chillicream.com/docs/hotchocolate/v14/performance/automatic-persisted-operations#how-it-works)How it works
---------------------------------------------------------------------------------------------------------------------

The Automatic Persisted Queries (APQ) protocol was originally specified by Apollo and represents an evolution of the persisted operations feature that many GraphQL servers implement. Instead of storing operation documents ahead of time, the client can store operation documents dynamically. This preserves the original proposal's performance benefits but removes the friction of setting up build processes that post-process the client applications source code.

When the client makes a request to the server, it will optimistically send a short cryptographic hash instead of the full operation document.

[](https://chillicream.com/docs/hotchocolate/v14/performance/automatic-persisted-operations#optimized-path)Optimized Path
-------------------------------------------------------------------------------------------------------------------------

Hot Chocolate server will inspect the incoming request for an operation ID or a full GraphQL operation document. If the request has only an operation ID, the execution engine will first try to resolve the full operation document from the operation document storage. If the operation document storage contains an operation document that matches the provided operation ID, the request will be upgraded to a fully valid GraphQL request and will be executed.

[](https://chillicream.com/docs/hotchocolate/v14/performance/automatic-persisted-operations#new-operation-path)New Operation Path
---------------------------------------------------------------------------------------------------------------------------------

If the operation document storage does not contain an operation document that matches the sent operation ID, the Hot Chocolate server will return an error result that indicates that the operation document was not found (this will only happen the first time a client asks for a certain operation document). The client application will then send in a second request with the specified operation document ID and the complete GraphQL operation document. This will trigger Hot Chocolate server to store this new operation document in its operation document storage and, at the same time, execute the operation and return the result.

[](https://chillicream.com/docs/hotchocolate/v14/performance/automatic-persisted-operations#setup)Setup
-------------------------------------------------------------------------------------------------------

In the following tutorial, we will walk you through creating a Hot Chocolate GraphQL server and configuring it to support automatic persisted operations.

[](https://chillicream.com/docs/hotchocolate/v14/performance/automatic-persisted-operations#step-1-create-a-graphql-server-project)Step 1: Create a GraphQL server project
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Open your preferred terminal and select a directory where you want to add the code of this tutorial.

1.   Install the Hot Chocolate templates.

Bash

dotnet new install HotChocolate.Templates

1.   Create a new Hot Chocolate GraphQL server project.

Bash

dotnet new graphql

1.   Add the in-memory persisted operations package to your project.

Bash

dotnet add package HotChocolate.PersistedOperations.InMemory

Warning

All `HotChocolate.*` packages need to have the same version.

[](https://chillicream.com/docs/hotchocolate/v14/performance/automatic-persisted-operations#step-2-configure-automatic-persisted-operations)Step 2: Configure automatic persisted operations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Next, we want to configure our GraphQL server to be able to handle automatic persisted operation requests. For this, we need to register the in-memory operation storage and configure the automatic persisted operation request pipeline.

1.   Configure GraphQL server to use the automatic persisted operation pipeline.

C#

public void ConfigureServices(IServiceCollection services)

{

services

.AddGraphQLServer()

.AddQueryType<Query>()

.UseAutomaticPersistedOperationPipeline();

}

1.   Next, register the in-memory operation document storage.

C#

public void ConfigureServices(IServiceCollection services)

{

services

.AddGraphQLServer()

.AddQueryType<Query>()

.UseAutomaticPersistedOperationPipeline()

.AddInMemoryOperationDocumentStorage();

}

1.   Last but not least, we need to add the Microsoft Memory Cache, which the in-memory operation document storage will use as the in-memory key-value store.

C#

public void ConfigureServices(IServiceCollection services)

{

services

.AddMemoryCache()

.AddGraphQLServer()

.AddQueryType<Query>()

.UseAutomaticPersistedOperationPipeline()

.AddInMemoryOperationDocumentStorage();

}

[](https://chillicream.com/docs/hotchocolate/v14/performance/automatic-persisted-operations#step-3-verify-server-setup)Step 3: Verify server setup
--------------------------------------------------------------------------------------------------------------------------------------------------

Now that our server is set up with automatic persisted operations, let us verify that it works as expected. We can do that by just using our console and a tool called `curl`. For our example, we will use a dummy operation `{__typename}` with an MD5 hash serialized to base64 as an operation ID `71yeex4k3iYWQgg9TilDIg==`. We will test the full automatic persisted operation flow and walk you through the responses.

1.   Start the GraphQL server.

Bash

dotnet run

1.   First, we will ask our GraphQL server to execute our operation with the optimized request containing only the operation hash. At this point, the server will not know this operation and has to return an error indicating this.

**Request**

Bash

curl -g 'http://localhost:5000/graphql/?extensions={"persistedQuery":{"version":1,"md5Hash":"71yeex4k3iYWQgg9TilDIg=="}}'

**Response**

The response indicates, as expected, that this operation is unknown so far.

JSON

{

"errors": [

{

"message": "PersistedQueryNotFound",

"extensions": { "code": "HC0020" }

}

]

}

1.   Next, we want to store our dummy operation document on the server. We will send in the hash as before but now also provide the `query` parameter with the full GraphQL operation string.

**Request**

Bash

curl -g 'http://localhost:5000/graphql/?query={__typename}&extensions={"persistedQuery":{"version":1,"md5Hash":"71yeex4k3iYWQgg9TilDIg=="}}'

**Response**

Our GraphQL server will respond with the operation result and indicate that the operation was stored on the server `"persisted": true`.

JSON

{

"data": { "__typename": "Query" },

"extensions": {

"persistedQuery": {

"md5Hash": "71yeex4k3iYWQgg9TilDIg==",

"persisted": true

}

}

}

1.   Last but not least, we will verify that we can now use our optimized request by executing our initial request containing only the operation document hash.

**Request**

Bash

curl -g 'http://localhost:5000/graphql/?extensions={"persistedQuery":{"version":1,"md5Hash":"71yeex4k3iYWQgg9TilDIg=="}}'

**Response**

This time the server knows the operation and will respond with the simple result of this operation.

JSON

{ "data": { "__typename": "Query" } }

> In this example, we used GraphQL HTTP GET requests, which are also useful in caching scenarios with CDNs. But the automatic persisted operation flow can also be used with GraphQL HTTP POST requests.

[](https://chillicream.com/docs/hotchocolate/v14/performance/automatic-persisted-operations#step-4-configure-the-hashing-algorithm)Step 4: Configure the hashing algorithm
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Hot Chocolate server is configured to use by default the MD5 hashing algorithm, which is serialized to a base64 string. Hot Chocolate server comes out of the box with support for MD5, SHA1, and SHA256 and can serialize the hash to base64 or hex. In this step, we will walk you through changing the hashing algorithm to SHA256 with a hex serialization.

1.   Add the SHA256 document hash provider to your Hot Chocolate GraphQL server's global services.

C#

public void ConfigureServices(IServiceCollection services)

{

services

.AddMemoryCache()

.AddSha256DocumentHashProvider(HashFormat.Hex)

.AddGraphQLServer()

.AddQueryType<Query>()

.UseAutomaticPersistedOperationPipeline()

.AddInMemoryOperationDocumentStorage();

}

1.   Start the GraphQL server.

Bash

dotnet run

1.   Next, let us verify that our server now operates with the new hash provider and the new hash serialization format. For this we will store again an operation document on the server, but this time our hash string will look like the following: `7f56e67dd21ab3f30d1ff8b7bed08893f0a0db86449836189b361dd1e56ddb4b`.

**Request**

Bash

curl -g 'http://localhost:5000/graphql/?query={__typename}&extensions={"persistedQuery":{"version":1,"sha256Hash":"7f56e67dd21ab3f30d1ff8b7bed08893f0a0db86449836189b361dd1e56ddb4b"}}'

**Response**

JSON

{

"data": { "__typename": "Query" },

"extensions": {

"persistedQuery": {

"sha256Hash": "7f56e67dd21ab3f30d1ff8b7bed08893f0a0db86449836189b361dd1e56ddb4b",

"persisted": true

}

}

}

[](https://chillicream.com/docs/hotchocolate/v14/performance/automatic-persisted-operations#step-4-use-redis-as-an-operation-document-storage)Step 4: Use Redis as an operation document storage
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you run multiple Hot Chocolate server instances and want to preserve stored operation documents after a server restart, you can opt to use a file-system-based operation document storage or opt to use a Redis cache. Hot Chocolate server supports both.

1.   Setup a Redis docker container.

Bash

docker run --name redis-stitching -p 7000:6379 -d redis

1.   Add the Redis persisted operations package to your server.

Bash

dotnet add package HotChocolate.PersistedOperations.Redis

Warning

All `HotChocolate.*` packages need to have the same version.

1.   Next, we need to configure the server to use Redis as operation document storage.

C#

public void ConfigureServices(IServiceCollection services)

{

services

.AddSha256DocumentHashProvider(HashFormat.Hex)

.AddGraphQLServer()

.AddQueryType<Query>()

.UseAutomaticPersistedOperationPipeline()

.AddRedisOperationDocumentStorage(services => ConnectionMultiplexer.Connect("localhost:7000").GetDatabase());

}

1.   Start the GraphQL server.

Bash

dotnet run

1.   Now, let us verify again if our server works correctly by storing our operation document first.

**Request**

Bash

curl -g 'http://localhost:5000/graphql/?query={__typename}&extensions={"persistedQuery":{"version":1,"sha256Hash":"7f56e67dd21ab3f30d1ff8b7bed08893f0a0db86449836189b361dd1e56ddb4b"}}'

**Response**

JSON

{

"data": { "__typename": "Query" },

"extensions": {

"persistedQuery": {

"sha256Hash": "7f56e67dd21ab3f30d1ff8b7bed08893f0a0db86449836189b361dd1e56ddb4b",

"persisted": true

}

}

}

1.   Stop your GraphQL server.

2.   Start your GraphQL server again.

Bash

dotnet run

1.   Let us execute the optimized operation to see if our operation document was correctly stored in our Redis cache.

**Request**

Bash

curl -g 'http://localhost:5000/graphql/?extensions={"persistedQuery":{"version":1,"sha256Hash":"7f56e67dd21ab3f30d1ff8b7bed08893f0a0db86449836189b361dd1e56ddb4b"}}'

**Response**

JSON

{ "data": { "__typename": "Query" } }

Last updated on **2026-02-17** by**Tobias Tengler**
