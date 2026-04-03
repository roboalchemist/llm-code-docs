# Introduction to Apollo Federation

Apollo Federation enables you to declaratively combine multiple APIs into a single federated GraphQL API. Federation serves as an API orchestration layer, where clients make a single GraphQL request and it coordinates multiple API calls to return a unified response.

Clients makes requests to the federated GraphQL API's single entry point called the *router*. The router intelligently orchestrates and distributes the request across your APIs and returns a unified response. For a client, the request and response cycle of querying the router looks the same as querying any GraphQL API.

Your federated GraphQL API, or *graph*, can be made of GraphQL APIs, REST APIs, and other data sources. The router connects to REST APIs via Apollo Connectors and can connect to other data sources via GraphQL APIs.

## Benefits of federation

### Microservices architecture

Apollo Federation lets API teams operate in a [microservices architecture](https://www.atlassian.com/microservices/microservices-architecture/microservices-vs-monolith) while exposing a unified GraphQL API to clients. Understanding these concepts can help you get the most out of federation.

* Learn more about the [considerations and benefits of GraphQL](https://graphql.com/learn/what-is-graphql/).
* Learn more about the [considerations and benefits of microservices architecture](https://aws.amazon.com/compare/the-difference-between-monolithic-and-microservices-architecture/).

### Preserve client simplicity and performance

A client may need to make multiple requests when interacting with multiple non-federated GraphQL APIs. This can happen when an organization adopting GraphQL  has multiple teams developing APIs independently. Each team sets up a GraphQL API that provides the data used by that team. For example, a travel app may have separate GraphQL APIs for users, flights, and hotels:

With a single federated graph, you preserve a powerful advantage of GraphQL over traditional REST APIs: the ability to fetch all the data you need in a single request.

The router intelligently calls all the APIs it needs to complete requests rather than simply forwarding them.
For performance and security reasons, clients should only query the router, and only the router should query the constituent APIs.
No client-side configuration is required.

### Design schemas at scale

Some alternative approaches to combining GraphQL APIs impose limits on your schema, like adding namespaces or representing relationships with IDs instead of types. With these approaches, your individual GraphQL API schemas may look unchanged—but the resulting federated schema that clients interact with is more complex. Subsequently, it requires you to make frontend as well as backend changes.

With Apollo Federation, clients can interact with the federated schema as if it were a monolith. Consumers of your API shouldn't know or care that it's implemented as microservices.

### Maintain a single API

With federation, every team contributes directly to the overall federated GraphQL schema. Each team can work independently without needing to maintain multiple API layers. This frees your platform team to focus on the quality of your API rather than keeping it up to date.

### Connect APIs declaratively

Apollo Federation is the foundation of Apollo Connectors, which allows you to integrate REST APIs into your federated graph by defining them declaratively in your GraphQL schema.

## Next steps

Before continuing, it's helpful to know some terminology:

* When combining multiple GraphQL APIs, the single, federated graph is called a *supergraph*.
* In a supergraph, the constituent APIs are called *subgraphs*.

Different subgraphs in the same supergraph can use different server implementations and even different programming languages as long as they are [federation-compatible](https://www.apollographql.com/docs/graphos/reference/federation/compatible-subgraphs).

Ready to get started?

* Connect REST APIs to your graph using Apollo Connectors with the [REST quickstart](https://www.apollographql.com/docs/graphos/get-started/guides/rest-quickstart).

* Create and run a federated graph with the [Quickstart](https://www.apollographql.com/docs/graphos/get-started/guides/quickstart).

### Additional resources

If you're new to federated architecture, this [overview article](https://graphql.com/learn/federated-architecture/) can introduce the concepts.

* To integrate existing APIs into a federated graph, this [interactive course](https://www.apollographql.com/tutorials/connectors-intro-rest) teaches you how to bring an existing REST API into a GraphQL API using Apollo Connectors.

* To federate a GraphQL backend, this [interactive course](https://www.apollographql.com/tutorials/voyage-part1) teaches you how to build an example supergraph using Apollo Federation.
