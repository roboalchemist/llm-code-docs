# Source: https://www.apollographql.com/docs/graphos/connectors/getting-started/requirements.md

# REST API Requirements

Connectors make it easy to build a GraphQL API using your existing HTTP/JSON APIs. They're flexible and work with most APIs, especially if they conform to the following guidelines.

## Content Type

Connectors work best with JSON response body. If your API endpoint doesn't default to a JSON content type, you may need to specify an `Accept: application/json` header. See the requests guide to learn [how to set headers](https://www.apollographql.com/docs/graphos/connectors/requests/#headers).

Some APIs may have a different mechanism for specifying the response content type, such as a query parameter or file extension. Ensure your Connector is configured appropriately to request a JSON response.

Connectors don't require a `Content-Type` response header. By default, they interpret any response body as JSON.
Connectors can also work with [some non-JSON content types](https://www.apollographql.com/docs/graphos/connectors/responses#mapping-non-json-content-types).

## Core JSON-over-HTTP requirements

Connectors work with APIs that follow these JSON-over-HTTP principles:

* Your endpoints accept requests using these HTTP verbs: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.
* Your endpoints use path segments and query string parameters for inputs, such as `/users/123` or `/users?limit=10`.
* For `POST`, `PUT`, and `PATCH` requests with request bodies, your endpoints accept JSON or [form URL encoded strings](https://www.apollographql.com/docs/graphos/connectors/requests/#form-url-encoding).
* Your endpoints respond with JSON values—typically objects, but any JSON value is allowed.
* Your endpoints always return a status code between 200 and 299 for successful requests.
* Your endpoints provide a known set of properties. GraphQL doesn't have a `Map` type, so you must define the mapping between JSON properties and GraphQL fields in advance. (You can map an arbitrary map to a scalar field using a custom scalar type.)

## Entity representation and relationships

Connectors work best with APIs that follow these conventions for representing and retrieving entities:

* You represent your entities across various endpoints using the same identifiers. For example, a `User` is consistently identified by `123` across all endpoints.
* You provide endpoints to fetch an entity by its primary key. For example, `/users/123` returns the user with ID `123`.
* Your endpoints use simple values for foreign keys. For example, a `User` object has a `companyId` field containing the ID of the company it belongs to. (Using a full URL such as `{"company": "http://myapi.com/company/234"}` is difficult to work with).
* When appropriate, your endpoints embed related entities in the response. For example, a `User` object might include a `company` field that contains a `Company` object.
* For better performance, you have endpoints for batch requests. For example, `/users?ids=123,456` returns the users with IDs `123` and `456`. This can dramatically reduce the number of requests needed to fetch related entities. See the [batching guide](https://www.apollographql.com/docs/graphos/connectors/requests/batching) for more information.

## Security conventions

To ensure secure interactions, your API should follow these security best practices.

* Your endpoints perform their own authentication and authorization checks as necessary. You can add layers of additional security using GraphOS Router's security features.
* Your endpoints accept authentication information in request headers. The headers can come directly from the client or be injected by the router.
* Your endpoints don't use query parameters for sensitive information. The router emits full URLs in logs and traces.
