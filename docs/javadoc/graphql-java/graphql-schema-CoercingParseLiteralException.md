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

graphql.schema

## Class CoercingParseLiteralException

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

          - graphql.GraphqlErrorException

          - 

            - graphql.schema.CoercingParseLiteralException

- 

All Implemented Interfaces:
GraphQLError, java.io.Serializable

---

```
@PublicApi
public class CoercingParseLiteralException
extends GraphqlErrorException
```

See Also:
Serialized Form

- 

  - 

### Nested Class Summary

Nested Classes 

Modifier and Type
Class and Description

`static class `
`CoercingParseLiteralException.Builder` 

    - 

### Nested classes/interfaces inherited from class graphql.GraphqlErrorException

`GraphqlErrorException.BuilderBase<T extends GraphqlErrorException.BuilderBase<T,B>,B extends GraphqlErrorException>`

  - 

### Constructor Summary

Constructors 

Constructor and Description

`CoercingParseLiteralException()` 

`CoercingParseLiteralException(java.lang.String message)` 

`CoercingParseLiteralException(java.lang.String message,
                             java.lang.Throwable cause)` 

`CoercingParseLiteralException(java.lang.String message,
                             java.lang.Throwable cause,
                             SourceLocation sourceLocation)` 

`CoercingParseLiteralException(java.lang.Throwable cause)` 

  - 

### Method Summary

All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`ErrorType`
`getErrorType()` 

`static CoercingParseLiteralException.Builder`
`newCoercingParseLiteralException()` 

    - 

### Methods inherited from class graphql.GraphqlErrorException

`getExtensions, getLocations, getPath, newErrorException`

    - 

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

    - 

### Methods inherited from interface graphql.GraphQLError

`getMessage, toSpecification`

- 

  - 

### Constructor Detail

    - 

#### CoercingParseLiteralException

```
public CoercingParseLiteralException()
```

    - 

#### CoercingParseLiteralException

```
public CoercingParseLiteralException(java.lang.String message)
```

    - 

#### CoercingParseLiteralException

```
public CoercingParseLiteralException(java.lang.String message,
                                     java.lang.Throwable cause)
```

    - 

#### CoercingParseLiteralException

```
public CoercingParseLiteralException(java.lang.String message,
                                     java.lang.Throwable cause,
                                     SourceLocation sourceLocation)
```

    - 

#### CoercingParseLiteralException

```
public CoercingParseLiteralException(java.lang.Throwable cause)
```

  - 

### Method Detail

    - 

#### getErrorType

```
public ErrorType getErrorType()
```

Specified by:
`getErrorType` in interface `GraphQLError`
Overrides:
`getErrorType` in class `GraphqlErrorException`
Returns:
an object classifying this error

    - 

#### newCoercingParseLiteralException

```
public static CoercingParseLiteralException.Builder newCoercingParseLiteralException()
```

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