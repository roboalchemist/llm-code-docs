JavaScript is disabled on your browser.

Skip navigation links

- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

graphql.execution

## Class AbortExecutionException

- java.lang.Object

- 

  - java.lang.Throwable

  - 

    - java.lang.Exception

    - 

      - java.lang.RuntimeException

      - 

        - graphql.GraphQLException

        - 

          - graphql.execution.AbortExecutionException

- 

All Implemented Interfaces:
GraphQLError, java.io.Serializable

---

```
@PublicApi
public class AbortExecutionException
extends GraphQLException
implements GraphQLError
```

This Exception indicates that the current execution should be aborted.

See Also:
Serialized Form

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AbortExecutionException()` 

`AbortExecutionException(java.util.Collection<GraphQLError> underlyingErrors)` 

`AbortExecutionException(java.lang.String message)` 

`AbortExecutionException(java.lang.String message,
                       java.lang.Throwable cause)` 

`AbortExecutionException(java.lang.Throwable cause)` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`ErrorType`
`getErrorType()` 

`java.util.List<SourceLocation>`
`getLocations()` 

`java.util.List<GraphQLError>`
`getUnderlyingErrors()` 

`ExecutionResult`
`toExecutionResult()`
This is useful for turning this abort signal into an execution result which
 is an error state with the underlying errors in it.

    - 

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

    - 

### Methods inherited from interface graphql.GraphQLError

`getExtensions, getMessage, getPath, toSpecification`

- 

  - 

### Constructor Detail

    - 

#### AbortExecutionException

```
public AbortExecutionException()
```

    - 

#### AbortExecutionException

```
public AbortExecutionException(java.util.Collection<GraphQLError> underlyingErrors)
```

    - 

#### AbortExecutionException

```
public AbortExecutionException(java.lang.String message)
```

    - 

#### AbortExecutionException

```
public AbortExecutionException(java.lang.String message,
                               java.lang.Throwable cause)
```

    - 

#### AbortExecutionException

```
public AbortExecutionException(java.lang.Throwable cause)
```

  - 

### Method Detail

    - 

#### getLocations

```
public java.util.List<SourceLocation> getLocations()
```

Specified by:
`getLocations` in interface `GraphQLError`
Returns:
the location(s) within the GraphQL document at which the error occurred. Each `SourceLocation`
 describes the beginning of an associated syntax element

    - 

#### getErrorType

```
public ErrorType getErrorType()
```

Specified by:
`getErrorType` in interface `GraphQLError`
Returns:
an object classifying this error

    - 

#### getUnderlyingErrors

```
public java.util.List<GraphQLError> getUnderlyingErrors()
```

Returns:
a list of underlying errors, which may be empty

    - 

#### toExecutionResult

```
public ExecutionResult toExecutionResult()
```

This is useful for turning this abort signal into an execution result which
 is an error state with the underlying errors in it.

Returns:
an execution result with the errors from this exception

Skip navigation links

- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method