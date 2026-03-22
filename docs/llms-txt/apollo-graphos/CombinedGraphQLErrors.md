# Source: https://www.apollographql.com/docs/react/api/errors/CombinedGraphQLErrors.md

# CombinedGraphQLErrors

Represents the combined list of GraphQL errors returned from the server in a GraphQL response. This error type is used when your GraphQL operation returns errors in the `errors` field of the response.

When your GraphQL operation encounters errors on the server side (such as resolver errors, validation errors, or syntax errors), the server returns these errors in the `errors` array of the GraphQL response. Apollo Client wraps these errors in a `CombinedGraphQLErrors` object, which provides access to the individual errors while maintaining additional context about the response.

TypeScript

```
 import { CombinedGraphQLErrors } from "@apollo/client/errors";

 // Check if an error is a CombinedGraphQLErrors object
 if (CombinedGraphQLErrors.is(error)) {
   // Access individual GraphQL errors
   error.errors.forEach((graphQLError) => {
     console.log(graphQLError.message);
     console.log(graphQLError.path);
     console.log(graphQLError.locations);
   });

   // Access the original GraphQL result
   console.log(error.result);
 }
```

## Providing a custom message formatter

By default, `CombinedGraphQLErrors` formats the `message` property by joining each error's `message` field with a newline. To customize the format of the `message`, such as changing the delimiter or adding a message prefix, override the static `formatMessage` method.

The following example demonstrates how to format the error message by joining each error with a comma.

TypeScript

```
import { CombinedGraphQLErrors } from "@apollo/client/errors";

CombinedGraphQLErrors.formatMessage = (errors) => {
  return errors.map((error) => error.message).join(", ");
};
```

See the [`formatMessage`](https://www.apollographql.com/docs/react/api/errors/CombinedGraphQLErrors.md#formatmessage) docs for details about the parameters provided to the `formatMessage` function.

**note**

The message formatter needs to be configured before any operation is executed by Apollo Client, otherwise the default message formatter is used. We recommend configuring the message formatter before initializing your `ApolloClient` instance.

### Using the default message formatter

To format part of the message using the default message formatter, call the `defaultFormatMessage` function provided to the `options` argument of your message formatter.

The following example prepends a string to the message and uses the default message formatter to format the error messages.

TypeScript

```
CombinedGraphQLErrors.formatMessage = (errors, { defaultFormatMessage }) => {
  return `[GraphQL errors]: ${defaultFormatMessage(errors)}`;
};
```

## Static methods

### [`is`](https://www.apollographql.com/docs/react/api/errors/CombinedGraphQLErrors.md#is)

A method that determines whether an error is a `CombinedGraphQLErrors` object. This method enables TypeScript to narrow the error type.

#### [Example](https://www.apollographql.com/docs/react/api/errors/CombinedGraphQLErrors.md#is-example)

TypeScript

```
 if (CombinedGraphQLErrors.is(error)) {
   // TypeScript now knows `error` is a `CombinedGraphQLErrors` object
   console.log(error.errors);
 }
```

#### [Signature](https://www.apollographql.com/docs/react/api/errors/CombinedGraphQLErrors.md#is-signature)

TypeScript

```
is(
  error: unknown
): error is CombinedGraphQLErrors
```

See the [instance properties](https://www.apollographql.com/docs/react/api/errors/CombinedGraphQLErrors.md#instance-properties) for more details about the available properties provided by the `CombinedGraphQLErrors` object.

### [`formatMessage`](https://www.apollographql.com/docs/react/api/errors/CombinedGraphQLErrors.md#formatmessage)

A function that formats the error message used for the error's `message` property. Override this method to provide your own formatting.

The `formatMessage` function is called by the `CombinedGraphQLErrors` constructor to provide a formatted message as the `message` property of the `CombinedGraphQLErrors` object. Follow the ["Providing a custom message formatter"](https://www.apollographql.com/docs/react/api/errors/CombinedGraphQLErrors.md#providing-a-custom-message-formatter) guide to learn how to modify the message format.

#### [Signature](https://www.apollographql.com/docs/react/api/errors/CombinedGraphQLErrors.md#formatmessage-signature)

TypeScript

```
formatMessage(
  errors: ReadonlyArray<GraphQLFormattedError>,
  options: MessageFormatterOptions
): string
```

#### [Parameters](https://www.apollographql.com/docs/react/api/errors/CombinedGraphQLErrors.md#formatmessage-parameters)

Name / Type

Description

[`errors`](https://www.apollographql.com/docs/react/api/errors/CombinedGraphQLErrors.md#formatmessage-parameters-errors)\
`ReadonlyArray<GraphQLFormattedError>`

The array of GraphQL errors returned from the server in the `errors` field of the response.

[`options`](https://www.apollographql.com/docs/react/api/errors/CombinedGraphQLErrors.md#formatmessage-parameters-options)\
`MessageFormatterOptions`

Additional context that could be useful when formatting the message.

#### [`CombinedGraphQLErrors.MessageFormatterOptions`](https://www.apollographql.com/docs/react/api/errors/CombinedGraphQLErrors.md#combinedgraphqlerrors.messageformatteroptions)

Properties

Name / Type

Description

###### [`defaultFormatMessage`](https://www.apollographql.com/docs/react/api/errors/CombinedGraphQLErrors.md#messageformatteroptions-defaultformatmessage)

`(errors: ReadonlyArray<GraphQLFormattedError>) => string`

The default message formatter. Call this to get a string with the default formatted message.

Read more...

To format part of the message using the default message formatter, call the `defaultFormatMessage` function provided to the `options` argument of your message formatter.

The following example prepends a string to the message and uses the default message formatter to format the error messages.

TypeScript

```
CombinedGraphQLErrors.formatMessage = (errors, { defaultFormatMessage }) => {
  return `[GraphQL errors]: ${defaultFormatMessage(errors)}`;
};
```

###### [`result`](https://www.apollographql.com/docs/react/api/errors/CombinedGraphQLErrors.md#messageformatteroptions-result)

`ApolloLink.Result<unknown>`

The raw result returned from the server.

## Instance properties

These properties are specific to the `CombinedGraphQLErrors` object. Standard error [instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error#instance_properties) are also available.

###### [`data`](https://www.apollographql.com/docs/react/api/errors/CombinedGraphQLErrors.md#instanceproperties-data)

`Record<string, unknown> | null | undefined`

Partial data returned in the `data` field of the GraphQL response.

###### [`errors`](https://www.apollographql.com/docs/react/api/errors/CombinedGraphQLErrors.md#instanceproperties-errors)

`ReadonlyArray<GraphQLFormattedError>`

The raw list of GraphQL errors returned by the `errors` field in the GraphQL response.

###### [`extensions`](https://www.apollographql.com/docs/react/api/errors/CombinedGraphQLErrors.md#instanceproperties-extensions)

`Record<string, unknown> | undefined`

Extensions returned by the `extensions` field in the GraphQL response.
