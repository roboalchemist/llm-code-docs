# Source: https://www.apollographql.com/docs/react/api/errors/UnconventionalError.md

# UnconventionalError

A wrapper error type that represents a non-standard error thrown from a A wrapper error type that represents a non-error value thrown from the link chain, such as a symbol, primitive or plain object. Read the `cause` property to determine the source of the error.

This error is used to standardize error handling when non-Error values are thrown in the Apollo Client link chain or other parts of the system. JavaScript allows throwing any value (not just Error instances), and this wrapper ensures that all thrown values can be handled consistently as Error-like objects while preserving the original thrown value.

**note**

Plain strings thrown as errors are wrapped in regular [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) objects instead of `UnconventionalError` objects since strings can be safely used as the error's `message`.

TypeScript

```
 import { UnconventionalError } from "@apollo/client/errors";

 // Check if an error is an UnconventionalError instance
 if (UnconventionalError.is(error)) {
   console.log("Non-standard error thrown:", error.cause);

   // Check the type of the original thrown value
   if (typeof error.cause === "symbol") {
     console.log("A symbol was thrown:", error.cause.toString());
   } else if (typeof error.cause === "object") {
     console.log("An object was thrown:", error.cause);
   } else {
     console.log("Unexpected value thrown:", error.cause);
   }
 }
```

## Common scenarios

`UnconventionalError` is typically encountered when custom link implementations, provided either by third-party libraries or your own link implementations, throw symbols, arrays, or other non-Error objects.

By wrapping these unconventional error types, Apollo Client ensures consistent error handling throughout the system while preserving the original error information.

Apollo Client itself does not throw or emit non-Error objects. Unless you're
using third-party packages integrated with Apollo Client, you will not
encounter this error type.

## Static methods

### [`is`](https://www.apollographql.com/docs/react/api/errors/UnconventionalError.md#is)

A method that determines whether an error is an `UnconventionalError` object. This method enables TypeScript to narrow the error type.

#### [Example](https://www.apollographql.com/docs/react/api/errors/UnconventionalError.md#is-example)

TypeScript

```
 if (UnconventionalError.is(error)) {
   // TypeScript now knows `error` is a UnconventionalError object
   console.log("What caused this?", error.cause);
 }
```

#### [Signature](https://www.apollographql.com/docs/react/api/errors/UnconventionalError.md#is-signature)

TypeScript

```
is(
  error: unknown
): error is UnconventionalError
```
