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

## Interface Coercing<I,O>

- 

All Known Implementing Classes:
GraphqlBooleanCoercing, GraphqlFloatCoercing, GraphqlIDCoercing, GraphqlIntCoercing, GraphqlStringCoercing

---

```
@PublicSpi
public interface Coercing<I,O>
```

The Coercing interface is used by `GraphQLScalarType`s to parse and serialise object values.
 

 There are two major responsibilities, result coercion and input coercion.
 

 Result coercion is taking a value from a Java object and coercing it into the constraints of the scalar type.
 For example imagine a DateTime scalar, the result coercion would need to take an object and turn it into a
 ISO date or throw an exception if it cant.
 

 Input coercion is made out of three different methods `parseLiteral(Object)` which converts an literal Ast
 into an internal input value, `parseValue(Object)` which converts an external input value into an internal one
 and `valueToLiteral(Object)` which is a translation between an external input value into a literal.
 

 The relationship between these three methods is as follows:
 It is required that every valid external input values for `parseValue(Object)` is also valid for
 `valueToLiteral(Object)`
 and vice versa.
 Furthermore the literals returned by `valueToLiteral(Object)` are required to be valid for
 `parseLiteral(Object)`.

- 

  - 

### Method Summary

All Methods Instance Methods Abstract Methods Default Methods 

Modifier and Type
Method and Description

`I`
`parseLiteral(@NotNull java.lang.Object input)`
Called during query validation to convert a query input AST node into a Java object acceptable for the scalar type.

`default I`
`parseLiteral(java.lang.Object input,
            java.util.Map<java.lang.String,java.lang.Object> variables)`
Called during query execution to convert a query input AST node into a Java object acceptable for the scalar type.

`I`
`parseValue(@NotNull java.lang.Object input)`
Called to resolve an input from a query variable into a Java object acceptable for the scalar type.

`O`
`serialize(@NotNull java.lang.Object dataFetcherResult)`
Called to convert a Java object result of a DataFetcher to a valid runtime value for the scalar type.

`default @NotNull Value`
`valueToLiteral(@NotNull java.lang.Object input)`
Converts an external input value to a literal (Ast Value).

- 

  - 

### Method Detail

    - 

#### serialize

```
O serialize(@NotNull
            @NotNull java.lang.Object dataFetcherResult)
     throws CoercingSerializeException
```

Called to convert a Java object result of a DataFetcher to a valid runtime value for the scalar type.
 

 Note : Throw `CoercingSerializeException` if there is fundamental
 problem during serialisation, don't return null to indicate failure.
 

 Note : You should not allow `RuntimeException`s to come out of your serialize method, but rather
 catch them and fire them as `CoercingSerializeException` instead as per the method contract.

Parameters:
`dataFetcherResult` - is never null
Returns:
a serialized value which may be null.
Throws:
`CoercingSerializeException` - if value input can't be serialized

    - 

#### parseValue

```
@NotNull
I parseValue(@NotNull
                      @NotNull java.lang.Object input)
               throws CoercingParseValueException
```

Called to resolve an input from a query variable into a Java object acceptable for the scalar type.
 

 Note : You should not allow `RuntimeException`s to come out of your parseValue method, but rather
 catch them and fire them as `CoercingParseValueException` instead as per the method contract.

Parameters:
`input` - is never null
Returns:
a parsed value which is never null
Throws:
`CoercingParseValueException` - if value input can't be parsed

    - 

#### parseLiteral

```
@NotNull
I parseLiteral(@NotNull
                        @NotNull java.lang.Object input)
                 throws CoercingParseLiteralException
```

Called during query validation to convert a query input AST node into a Java object acceptable for the scalar type.  The input
 object will be an instance of `Value`.
 

 Note : You should not allow `RuntimeException`s to come out of your parseLiteral method, but rather
 catch them and fire them as `CoercingParseLiteralException` instead as per the method contract.

Parameters:
`input` - is never null
Returns:
a parsed value which is never null
Throws:
`CoercingParseLiteralException` - if input literal can't be parsed

    - 

#### parseLiteral

```
@NotNull
default I parseLiteral(java.lang.Object input,
                                java.util.Map<java.lang.String,java.lang.Object> variables)
                         throws CoercingParseLiteralException
```

Called during query execution to convert a query input AST node into a Java object acceptable for the scalar type.  The input
 object will be an instance of `Value`.
 

 Note : You should not allow `RuntimeException`s to come out of your parseLiteral method, but rather
 catch them and fire them as `CoercingParseLiteralException` instead as per the method contract.
 

 Many scalar types don't need to implement this method because they don't take AST `VariableReference`
 objects and convert them into actual values.  But for those scalar types that want to do this, then this
 method should be implemented.

Parameters:
`input` - is never null
`variables` - the resolved variables passed to the query
Returns:
a parsed value which is never null
Throws:
`CoercingParseLiteralException` - if input literal can't be parsed

    - 

#### valueToLiteral

```
@NotNull
default @NotNull Value valueToLiteral(@NotNull
                                               @NotNull java.lang.Object input)
```

Converts an external input value to a literal (Ast Value).

 IMPORTANT: the argument is validated before by calling `parseValue(Object)`.

Parameters:
`input` - an external input value
Returns:
The literal matching the external input value.

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