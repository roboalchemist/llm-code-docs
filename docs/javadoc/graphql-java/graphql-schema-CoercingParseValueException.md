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

## Class CoercingParseValueException

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

            - graphql.schema.CoercingParseValueException

- 

All Implemented Interfaces:
GraphQLError, java.io.Serializable

---

```
@PublicApi
public class CoercingParseValueException
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
`CoercingParseValueException.Builder` 

    - 

### Nested classes/interfaces inherited from class graphql.GraphqlErrorException

`GraphqlErrorException.BuilderBase<T extends GraphqlErrorException.BuilderBase<T,B>,B extends GraphqlErrorException>`

  - 

### Constructor Summary

Constructors 

Constructor and Description

`CoercingParseValueException()` 

`CoercingParseValueException(java.lang.String message)` 

`CoercingParseValueException(java.lang.String message,
                           java.lang.Throwable cause)` 

`CoercingParseValueException(java.lang.String message,
                           java.lang.Throwable cause,
                           SourceLocation sourceLocation)` 

`CoercingParseValueException(java.lang.Throwable cause)` 

  - 

### Method Summary

All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`ErrorType`
`getErrorType()` 

`static CoercingParseValueException.Builder`
`newCoercingParseValueException()` 

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

#### CoercingParseValueException

```
public CoercingParseValueException()
```

    - 

#### CoercingParseValueException

```
public CoercingParseValueException(java.lang.String message)
```

    - 

#### CoercingParseValueException

```
public CoercingParseValueException(java.lang.String message,
                                   java.lang.Throwable cause)
```

    - 

#### CoercingParseValueException

```
public CoercingParseValueException(java.lang.Throwable cause)
```

    - 

#### CoercingParseValueException

```
public CoercingParseValueException(java.lang.String message,
                                   java.lang.Throwable cause,
                                   SourceLocation sourceLocation)
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

#### newCoercingParseValueException

```
public static CoercingParseValueException.Builder newCoercingParseValueException()
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