# Source: https://docs.hypermode.com/dgraph/guides/message-board-app/graphql/graphql-operations.md

# GraphQL Operations

> Using your schema, Dgraph Cloud generated ways to interact with the graph. In GraphQL, the API can be inspected with introspection queries.

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

The schema that you developed and deployed to Dgraph Cloud in the previous
sections was about the types in our domain and the shape of the app data graph.
From that, Dgraph Cloud generated some ways to interact with the graph. GraphQL
supports the following *operations*, which provide different ways to interact
with a graph:

* **queries**: used to find a starting point and traverse a subgraph
* **mutations**: used to change the graph and return a result
* **subscriptions**: used to listen for changes in the graph

In GraphQL, the API can be inspected with special queries called *introspection
queries*. Introspection queries are a type of GraphQL query that provides the
best way to find out what operations you can perform with a GraphQL API.

## Introspection

Many GraphQL tools support introspection and generate documentation to help you
explore an API. There are several tools in the GraphQL ecosystem you can use to
explore an API, including
[GraphQL Playground](https://github.com/prisma-labs/graphql-playground),
[Insomnia](https://insomnia.rest/),
[GraphiQL](https://github.com/graphql/graphiql),
[Postman](https://www.postman.com/graphql/), and
[Altair](https://github.com/imolorhe/altair).

You can also explore your GraphQL API using the API explorer that's included in
the Dgraph Cloud web UI. Navigate to the **GraphQL** tab where you can access
the introspected schema from the "Documentation Explorer" in the right menu.

*<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/dgraph-cloud-schema-explorer.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=a666945210ec4dbe0dfd1527f53357c2" alt="Dgraph Cloud Schema Explorer" width="3584" height="2240" data-path="images/dgraph/guides/message-board-app/dgraph-cloud-schema-explorer.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/dgraph-cloud-schema-explorer.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=64793a918636763fd937f68c06d74aaa 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/dgraph-cloud-schema-explorer.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=62025bc5d8c8765ebd378af1060a16fe 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/dgraph-cloud-schema-explorer.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=19690cc50c197bcd831711cc432b3a0b 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/dgraph-cloud-schema-explorer.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=dd9bd1fcd38af921183adc8bc7e6a3eb 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/dgraph-cloud-schema-explorer.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=2b541cd0b1311546c32b529389e88336 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/dgraph-cloud-schema-explorer.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=4f1a5032ebf376172f36642d30b13f71 2500w" data-optimize="true" data-opv="2" />*

From there, you can click through to the queries and mutations and check out the
API. For example, this API includes mutations to add, update and delete users,
posts and comments.

Next, you'll
[learn more about the API that Dgraph Cloud created from the schema](./react-graphql-mutations)
by trying out the same kind of queries and mutations you'll use to build the
message board app.
