# Source: https://www.apollographql.com/docs/react/api/errors/ServerParseError.md

# ServerParseError

Represents a failure to parse the response as JSON from the server. This error helps debug issues where the server returns malformed JSON or non-JSON content.

This error occurs when Apollo Client receives a response from the server but cannot parse it as valid JSON. This typically happens when the server returns HTML error pages, plain text responses, or malformed JSON instead of the expected GraphQL JSON response format.

TypeScript

```
 import { ServerParseError } from "@apollo/client/errors";

 // Check if an error is a ServerParseError instance
 if (ServerParseError.is(error)) {
   console.log(`Failed to parse response from ${error.response.url}`);
   console.log(`Raw response: ${error.bodyText}`);
   console.log(`Status code: ${error.statusCode}`);

   // Access the original parse error
   console.log(`Parse error: ${error.cause}`);
 }
```

## Static methods

### [`is`](https://www.apollographql.com/docs/react/api/errors/ServerParseError.md#is)

A method that determines whether an error is a `ServerParseError` object. This method enables TypeScript to narrow the error type.

#### [Example](https://www.apollographql.com/docs/react/api/errors/ServerParseError.md#is-example)

TypeScript

```
 if (ServerParseError.is(error)) {
   // TypeScript now knows `error` is a ServerParseError object
   console.log(error.statusCode);
 }
```

#### [Signature](https://www.apollographql.com/docs/react/api/errors/ServerParseError.md#is-signature)

TypeScript

```
is(
  error: unknown
): error is ServerParseError
```

See the [instance properties](https://www.apollographql.com/docs/react/api/errors/ServerParseError.md#instance-properties) for more details about the available properties provided by the `ServerParseError` object.

## Instance properties

These properties are specific to the `ServerParseError` object. Standard error [instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error#instance_properties) are also available.

Use the `cause` property to access the original parse error thrown by
`JSON.parse()`.

###### [`bodyText`](https://www.apollographql.com/docs/react/api/errors/ServerParseError.md#instanceproperties-bodytext)

`string`

The raw response body text.

###### [`response`](https://www.apollographql.com/docs/react/api/errors/ServerParseError.md#instanceproperties-response)

`Response`

The raw [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) object provided by the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API).

###### [`statusCode`](https://www.apollographql.com/docs/react/api/errors/ServerParseError.md#instanceproperties-statuscode)

`number`

The status code returned by the server in the response. This is provided as a shortcut for `response.status`.
