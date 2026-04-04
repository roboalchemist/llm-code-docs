# Source: https://docs.hypermode.com/modus/modus-dgraph.md

# Using Dgraph

> Add 'memory' and Knowledge Graph connection to your app.

Integrating Dgraph in Modus is a powerful solution to expose AI services with
"memory" or to create, maintain and leverage knowledge graphs.

After you have [initialized a Modus app](/modus/first-modus-agent), you can:

1. Provision your environment\
   Run [Dgraph locally](/dgraph/quickstart#locally) or
   [provision a Graph on Hypermode](/dgraph/quickstart#on-hypermode).

2. Declare the connection in the App Manifest\
   Edit the [App Manifest](/modus/app-manifest) to declare a connection to the
   Dgraph instance using the
   [Dgraph connection string](/modus/app-manifest#using-a-dgraph-connection-string).

   For local instance of Dgraph, the connection string is
   `dgraph://localhost:9080`.\
   For a Graph on Hypermode, the connection string is available from the
   Hypermode dashboard.
   <img src="https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/quickstart/graph-details.png?fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=eaa68eeb76893e16ea723dc71435a3ba" alt="Graph detail view" width="2148" height="1128" data-path="images/dgraph/quickstart/graph-details.png" srcset="https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/quickstart/graph-details.png?w=280&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=cbcc9299d383026d2449f615d44d85bc 280w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/quickstart/graph-details.png?w=560&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=3c793950afe5ad8a7bb846318869b4d5 560w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/quickstart/graph-details.png?w=840&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=a73a03970cd65b27bf79968f5ef7c050 840w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/quickstart/graph-details.png?w=1100&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=cada129e77ed62aff0a190298ee9d18c 1100w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/quickstart/graph-details.png?w=1650&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=49bad4592cb9d8235f5618cc7ea8b902 1650w, https://mintcdn.com/hypermode/KxRLwu8b3AQQ03et/images/dgraph/quickstart/graph-details.png?w=2500&fit=max&auto=format&n=KxRLwu8b3AQQ03et&q=85&s=f0c6f31c9b0fe4731f181f516ea78549 2500w" data-optimize="true" data-opv="2" />

   Make sure to use a variable for the bearer token so you don't commit secrets
   in your project!

```jsonc modus.json
"connections": {
    // This defines a dgraph connection
    // Get the connection string from the Hypermode dashboard.
    // use a variable for bearer token
    "my-dgraph": {
      "type": "dgraph",
      "connString": "dgraph://modus-recipes-backend-hypermode.hypermode.host:443?sslmode=verify-ca&bearertoken={{API_KEY}}"
    }
  }
```

\
Note: you can also define a Dgraph connection
[Using the gRPC target](/modus/app-manifest#using-a-dgraph-grpc-target)
parameter.

1. Set the secrets\
   When working locally set your
   [Environment Secrets](/modus/run-locally#environment-secrets) using a .env
   file.

   ```dotenv .env.dev.local
   MODUS_MY_DGRAPH_API_KEY='<your API Key>'
   ```

   \
   When your app is deployed on Hypermode,
   [add the connection secrets](/configure-environment#connection-secrets) in
   the Hypermode Console.

2. Use Modus SDK to query and mutate the graph.\
   In your Modus app, use the Modus SDK to
   [fetch data from Dgraph](/modus/data-fetching#dgraph).

## Resources

* [Manage Schema](/graphs/manage-schema) to deploy a schema to your Dgraph
  instance if needed.
* Get inspirations from
  [Modus Recipes](https://github.com/hypermodeinc/modus-recipes) where you'll
  find examples using Dgraph in Modus.
* Check the Modus SDK examples for
  [Go](https://github.com/hypermodeinc/modus/tree/main/sdk/go/examples) or
  [AssemblyScript](https://github.com/hypermodeinc/modus/tree/main/sdk/assemblyscript/examples)
