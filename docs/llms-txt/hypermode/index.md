# Source: https://docs.hypermode.com/dgraph/guides/message-board-app/react-ui/index.md

# Source: https://docs.hypermode.com/dgraph/guides/message-board-app/graphql/index.md

# Source: https://docs.hypermode.com/dgraph/guides/message-board-app/react-ui/index.md

# Source: https://docs.hypermode.com/dgraph/guides/message-board-app/graphql/index.md

# Working in GraphQL

> Developing a Message Board App in React with Dgraph Learn. Step 2: GraphQL schema design and loading, queries, and mutations.

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

To build an app with Dgraph Cloud, you design your app in GraphQL. You design a
set of GraphQL types that describes the app's data requirements. Dgraph Cloud
GraphQL takes those types, prepares graph storage for them and generates a
GraphQL API with queries and mutations.

In this section of the tutorial, you'll walk through the process of designing a
schema for a message board app, loading the GraphQL schema into Dgraph Cloud,
and then working through the queries and mutations that Dgraph Cloud makes
available from that schema.
