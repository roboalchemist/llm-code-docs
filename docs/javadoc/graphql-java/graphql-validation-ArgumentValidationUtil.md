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

graphql.validation

## Class ArgumentValidationUtil

- java.lang.Object

- 

  - graphql.validation.ValidationUtil

  - 

    - graphql.validation.ArgumentValidationUtil

- 

---

```
public class ArgumentValidationUtil
extends ValidationUtil
```

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`ArgumentValidationUtil(Argument argument)` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`java.util.Map<java.lang.String,java.lang.Object>`
`getErrorExtensions()` 

`java.lang.String`
`getMessage()` 

`protected void`
`handleEnumError(Value<?> value,
               GraphQLEnumType type,
               GraphQLError invalid)` 

`protected void`
`handleExtraFieldError(Value<?> value,
                     GraphQLInputObjectType type,
                     ObjectField objectField)` 

`protected void`
`handleFieldNotValidError(ObjectField objectField,
                        GraphQLInputObjectType type)` 

`protected void`
`handleFieldNotValidError(Value<?> value,
                        GraphQLType type,
                        int index)` 

`protected void`
`handleMissingFieldsError(Value<?> value,
                        GraphQLInputObjectType type,
                        java.util.Set<java.lang.String> missingFields)` 

`protected void`
`handleNotObjectError(Value<?> value,
                    GraphQLInputObjectType type)` 

`protected void`
`handleNullError(Value<?> value,
               GraphQLType type)` 

`protected void`
`handleScalarError(Value<?> value,
                 GraphQLScalarType type,
                 GraphQLError invalid)` 

    - 

### Methods inherited from class graphql.validation.ValidationUtil

`getUnmodifiedType, isValidLiteralValue`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### ArgumentValidationUtil

```
public ArgumentValidationUtil(Argument argument)
```

  - 

### Method Detail

    - 

#### handleNullError

```
protected void handleNullError(Value<?> value,
                               GraphQLType type)
```

Overrides:
`handleNullError` in class `ValidationUtil`

    - 

#### handleScalarError

```
protected void handleScalarError(Value<?> value,
                                 GraphQLScalarType type,
                                 GraphQLError invalid)
```

Overrides:
`handleScalarError` in class `ValidationUtil`

    - 

#### handleEnumError

```
protected void handleEnumError(Value<?> value,
                               GraphQLEnumType type,
                               GraphQLError invalid)
```

Overrides:
`handleEnumError` in class `ValidationUtil`

    - 

#### handleNotObjectError

```
protected void handleNotObjectError(Value<?> value,
                                    GraphQLInputObjectType type)
```

Overrides:
`handleNotObjectError` in class `ValidationUtil`

    - 

#### handleMissingFieldsError

```
protected void handleMissingFieldsError(Value<?> value,
                                        GraphQLInputObjectType type,
                                        java.util.Set<java.lang.String> missingFields)
```

Overrides:
`handleMissingFieldsError` in class `ValidationUtil`

    - 

#### handleExtraFieldError

```
protected void handleExtraFieldError(Value<?> value,
                                     GraphQLInputObjectType type,
                                     ObjectField objectField)
```

Overrides:
`handleExtraFieldError` in class `ValidationUtil`

    - 

#### handleFieldNotValidError

```
protected void handleFieldNotValidError(ObjectField objectField,
                                        GraphQLInputObjectType type)
```

Overrides:
`handleFieldNotValidError` in class `ValidationUtil`

    - 

#### handleFieldNotValidError

```
protected void handleFieldNotValidError(Value<?> value,
                                        GraphQLType type,
                                        int index)
```

Overrides:
`handleFieldNotValidError` in class `ValidationUtil`

    - 

#### getMessage

```
public java.lang.String getMessage()
```

    - 

#### getErrorExtensions

```
public java.util.Map<java.lang.String,java.lang.Object> getErrorExtensions()
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