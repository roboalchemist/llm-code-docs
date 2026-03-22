# Source: https://www.apollographql.com/docs/react/api/errors/ServerError.md

# ServerError

Represents an error when a non-200 HTTP status code is returned from the server according to the [GraphQL Over HTTP specification](https://graphql.github.io/graphql-over-http/draft/). This error contains the full server response, including status code and body text.

This error occurs when your GraphQL server responds with an HTTP status code other than 200 (such as 4xx or 5xx status codes) with any media type other than [`application/graphql-response+json`](https://graphql.github.io/graphql-over-http/draft/#sec-application-graphql-response-json).

Servers that return non-200 status codes with other media types are not guaranteed to contain a well-formed GraphQL response and may indicate issues at the HTTP level, such as authentication failures, server unavailability, or other HTTP-level problems.

TypeScript

```
 import { ServerError } from "@apollo/client/errors";

 // Check if an error is a ServerError instance
 if (ServerError.is(error)) {
   console.log(`Server returned status: ${error.statusCode}`);
   console.log(`Response body: ${error.bodyText}`);

   // Handle specific status codes
   if (error.statusCode === 401) {
     // Handle unauthorized access
   }
 }
```

## Static methods

### [`is`](https://www.apollographql.com/docs/react/api/errors/ServerError.md#is)

A method that determines whether an error is a `ServerError` object. This method enables TypeScript to narrow the error type.

#### [Example](https://www.apollographql.com/docs/react/api/errors/ServerError.md#is-example)

TypeScript

```
 if (ServerError.is(error)) {
   // TypeScript now knows `error` is a ServerError object
   console.log(error.errors);
 }
```

#### [Signature](https://www.apollographql.com/docs/react/api/errors/ServerError.md#is-signature)

TypeScript

```
is(
  error: unknown
): error is ServerError
```

See the [instance properties](https://www.apollographql.com/docs/react/api/errors/ServerError.md#instance-properties) for more details about the available properties provided by the `ServerError` object.

## Instance properties

These properties are specific to the `ServerError` object. Standard error [instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error#instance_properties) are also available.

###### [`bodyText`](https://www.apollographql.com/docs/react/api/errors/ServerError.md#instanceproperties-bodytext)

`string`

The raw response body text.

###### [`response`](https://www.apollographql.com/docs/react/api/errors/ServerError.md#instanceproperties-response)

`Response`

The raw [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) object provided by the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API).

###### [`statusCode`](https://www.apollographql.com/docs/react/api/errors/ServerError.md#instanceproperties-statuscode)

`number`

The status code returned by the server in the response. This is provided as a shortcut for `response.status`.
