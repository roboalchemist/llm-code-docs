# Source: https://jam.dev/docs/debug-a-jam/devtools/graphql.md

# GraphQL

One major difference between GraphQL and REST APIs is how they handle errors. In a REST API, different HTTP status codes indicate the outcome of a request. For example, a 200 status code means the request was successful, while a 400 status code means there was a client error.

In contrast, GraphQL always returns a 200 status code, even if there are errors in the response body. The [GraphQL spec](https://spec.graphql.org/October2021/?ref=strawberryjam.ghost.io#sec-Errors) suggests that servers respond with a structured errors field. This makes errors machine-readable but drops the semantic meaning of HTTP status codes. Additionally, GraphQL typically uses a single endpoint (`/graphql`) for all operations, making it difficult to distinguish between different requests when debugging.

This means that to effectively debug GraphQL, you typically have to comb through every single request to identify errors.

### GraphQL Debug Tools

We addresses these challenges with specialized debugging features:

**Automatic Error Detection** - Jam automatically flags GraphQL responses that contain errors in the response body, even though they return HTTP 200 status codes.

**Mutation Name Visibility** - Jam auto-detects and shows the GraphQL operation name directly in the dev tools interface, making it easy to identify specific mutations and queries without clicking into each request.

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2F8tFkHTPUoS1JRFhEWFKQ%2FGraphQL-devtools.gif?alt=media&#x26;token=5275877e-23cd-4f2c-b1ee-1062c75cf604" alt=""><figcaption></figcaption></figure>

These features eliminate the need to manually inspect every GraphQL request, speeding up your debugging workflow.
