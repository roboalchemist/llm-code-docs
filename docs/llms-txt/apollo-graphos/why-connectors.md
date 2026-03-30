# Source: https://www.apollographql.com/docs/graphos/connectors/why-connectors.md

# Why use Apollo Connectors?

Most modern apps rely on multiple REST services. Rewriting those REST services into a GraphQL API can be complex and time-consuming.
Apollo Connectors offer a clean, declarative way to integrate REST services directly into a graph.
By representing your REST services as part of a GraphQL schema, you can orchestrate calls across your services to produce a single response for all your clients.

If you learn best with videos and exercises, this [interactive course](https://www.apollographql.com/tutorials/connectors-intro-rest) teaches you how to bring an existing REST API into a GraphQL API using Apollo Connectors.

## Benefits of Connectors

* **Resilient API orchestration**: Efficiently coordinate calls across multiple services and compose results into a single response without needing to write procedural code to handle sequencing, error and retry logic, and more.

* **Increased developer velocity**: Use declarative schema definitions to connect directly to your REST APIs instead of writing custom code. This provides a more scalable orchestration strategy than Backend for Frontends.

* **Production-ready platform**: Develop and deploy from a single platform, GraphOS, that provides security, scalability, and observability features without building additional service layers.

## How do Connectors work?

To connect a REST service to your graph, you write a GraphQL schema for the service. Instead of writing procedural code, you add [Connector directives](https://www.apollographql.com/docs/graphos/schema-design/connectors/directives) to the schema. These directives specify the HTTP method, REST endpoint, and response mapping.

When queried, the GraphOS Router automatically handles requests, transforms responses, and composes data across multiple endpoints and APIs—all without extra service layers or custom logic.

### Connector example

Given a REST API with a `/products` endpoint returning product details:

```json
{
  "products": [
    {
      "id": 1,
      "name": "Lunar Rover Wheels",
      "description": "Designed for traversing the rugged terrain of the moon, these wheels provide unrivaled traction and durability. Made from a lightweight composite, they ensure your rover is agile in challenging conditions.",
      // Other fields...
    }
  ]
}
```

With Apollo Connectors, you can map this endpoint to a GraphQL schema like this:

```graphql
type Query {
  products: [Product]
    @connect(
      http: { GET: "https://ecommerce.demo-api.apollo.dev/products" }
      selection: """
      $.products {
        id
        name
      }
      """
    )
}

type Product {
  id: ID!
  name: String!
}
```

In this example:

* The `http` field tells the router to `GET` data from the `/products` endpoint.
* The `selection` field defines which parts of the JSON response to map to the `Product` type.
* The `Product` type defines the shape of the data clients can receive.

Although the `/products` endpoint returns many fields, Connectors let you select and return only the `id` and `name` fields that you need.

## Where Connectors work best

Connectors excel at quickly exposing REST APIs without the need for custom code, but have [limitations](https://www.apollographql.com/docs/graphos/schema-design/connectors/limitations) with complex data transformations. For instance, aggregating all reviews to calculate an average rating is more efficient in a database rather than via [Connectors transformations](https://www.apollographql.com/docs/graphos/schema-design/connectors/responses#transforming-values).

For advanced scenarios, you can [combine Connectors with Federation](https://www.apollographql.com/docs/graphos/schema-design/connectors/federation)—use resolvers for business logic while Connectors handle data fetching. This hybrid approach works well when you need operations (like filtering) that your REST API doesn't natively support.

```mermaid
flowchart LR;
  clients(Clients);
  router([Router]);
  clients -.- router;
  router --- |filtered list| c[Subgraph];
  c --- |fetch list| a[Rest API];
  router --- |@connect<br>for additional details| a[REST API];
```

## Next steps

Depending on your goals, you have a few options for learning more:

* 🚀 Try it yourself: Follow the [Getting Started guide](https://www.apollographql.com/docs/graphos/connectors/getting-started)
* 🌍 See and share fully working Connectors with the community: [Apollo Connectors Community](https://github.com/apollographql/connectors-community)

### Additional resources

Explore the following resources to learn more about how Apollo Connectors, REST, and GraphQL work together:

* [Can REST and GraphQL be friends?](https://www.youtube.com/watch?v=FGBCwz0FSgY) *(3 min watch)*
* [API Orchestration in 30 Minutes: A Stripe Checkout Workflow with Apollo Connectors](https://www.apollographql.com/events/api-orchestration-in-30-minutes-a-stripe-checkout-workflow-with-apollo-connectors) *(36 min watch)*
* [REST API Orchestration with GraphQL blog post](https://www.apollographql.com/blog/api-orchestration-with-graphql)
* [Our Journey to Apollo Connectors blog post](https://www.apollographql.com/blog/our-journey-to-apollo-connectors)
