# Source: https://www.apollographql.com/docs/react/api/errors/LocalStateError.md

# LocalStateError

Represents a fatal error when executing `@client` fields from `LocalState`, typically to indicate a problem with the `LocalState` configuration or incorrect usage of a resolver function. This error does not represent user errors thrown in a local resolver when resolving `@client` fields.

TypeScript

```
 import { LocalStateError } from "@apollo/client/errors";

 // Check if an error is a LocalStateError instance
 if (LocalStateError.is(error)) {
   console.log("Original error:", error.cause);

   // Determine which field caused the error
   if (error.path) {
     console.log("Error occurred at field path:", error.path.join("."));
   }
 }
```

## Static methods

### [`is`](https://www.apollographql.com/docs/react/api/errors/LocalStateError.md#is)

A method that determines whether an error is a `LocalStateError` object. This method enables TypeScript to narrow the error type.

#### [Example](https://www.apollographql.com/docs/react/api/errors/LocalStateError.md#is-example)

TypeScript

```
 if (LocalStateError.is(error)) {
   // TypeScript now knows `error` is a LocalStateError object
   console.log(error.path);
 }
```

#### [Signature](https://www.apollographql.com/docs/react/api/errors/LocalStateError.md#is-signature)

TypeScript

```
is(
  error: unknown
): error is LocalStateError
```

See the [instance properties](https://www.apollographql.com/docs/react/api/errors/LocalStateError.md#instance-properties) for more details about the available properties provided by the `LocalStateError` object.

## Instance properties

These properties are specific to the `LocalStateError` object. Standard error [instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error#instance_properties) are also available.

The `cause` property contains the original error thrown by local resolvers
when exporting variables for [`@export`](https://www.apollographql.com/docs/react/data/directives#export)
directive fields.

###### [`path`*(optional)*](https://www.apollographql.com/docs/react/api/errors/LocalStateError.md#instanceproperties-path)

`Array<string | number>`

The path to the field that caused the error.
