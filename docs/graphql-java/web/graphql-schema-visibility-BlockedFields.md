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

graphql.schema.visibility

## Class BlockedFields

- java.lang.Object

- 

  - graphql.schema.visibility.BlockedFields

- 

All Implemented Interfaces:
GraphqlFieldVisibility

---

```
@PublicApi
public class BlockedFields
extends java.lang.Object
implements GraphqlFieldVisibility
```

This helper class will take a list of regular expressions and match them against the fully qualified name
 of a type and its fields.  So for example an object type called "User" with an inner field called "firstName"
 will have a fully qualified name of "User.firstName" in terms of pattern matching.

 Remember that graphql type and fields names MUST be inside the name space "[_A-Za-z][_0-9A-Za-z]*"

- 

  - 

### Nested Class Summary

Nested Classes 

Modifier and Type
Class and Description

`static class `
`BlockedFields.Builder` 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`BlockedFields(java.util.List<java.util.regex.Pattern> patterns)`
Deprecated. 
use the `newBlock()` builder pattern instead, as this constructor will be made private in a future version.

  - 

### Method Summary

All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`GraphQLFieldDefinition`
`getFieldDefinition(GraphQLFieldsContainer fieldsContainer,
                  java.lang.String fieldName)`
Called to get a named field from an object type or interface

`GraphQLInputObjectField`
`getFieldDefinition(GraphQLInputFieldsContainer fieldsContainer,
                  java.lang.String fieldName)`
Called to get a named field from an input object type

`java.util.List<GraphQLFieldDefinition>`
`getFieldDefinitions(GraphQLFieldsContainer fieldsContainer)`
Called to get the list of fields from an object type or interface

`java.util.List<GraphQLInputObjectField>`
`getFieldDefinitions(GraphQLInputFieldsContainer fieldsContainer)`
Called to get the list of fields from an input object type

`static BlockedFields.Builder`
`newBlock()` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### BlockedFields

```
@Deprecated
public BlockedFields(java.util.List<java.util.regex.Pattern> patterns)
```

Deprecated. use the `newBlock()` builder pattern instead, as this constructor will be made private in a future version.

Parameters:
`patterns` - the blocked field patterns

  - 

### Method Detail

    - 

#### getFieldDefinitions

```
public java.util.List<GraphQLFieldDefinition> getFieldDefinitions(GraphQLFieldsContainer fieldsContainer)
```

Description copied from interface: `GraphqlFieldVisibility`
Called to get the list of fields from an object type or interface

Specified by:
`getFieldDefinitions` in interface `GraphqlFieldVisibility`
Parameters:
`fieldsContainer` - the type in play
Returns:
a non null list of `GraphQLFieldDefinition`s

    - 

#### getFieldDefinition

```
public GraphQLFieldDefinition getFieldDefinition(GraphQLFieldsContainer fieldsContainer,
                                                 java.lang.String fieldName)
```

Description copied from interface: `GraphqlFieldVisibility`
Called to get a named field from an object type or interface

Specified by:
`getFieldDefinition` in interface `GraphqlFieldVisibility`
Parameters:
`fieldsContainer` - the type in play
`fieldName` - the name of the desired field
Returns:
a `GraphQLFieldDefinition` or null if its not visible

    - 

#### getFieldDefinitions

```
public java.util.List<GraphQLInputObjectField> getFieldDefinitions(GraphQLInputFieldsContainer fieldsContainer)
```

Description copied from interface: `GraphqlFieldVisibility`
Called to get the list of fields from an input object type

Specified by:
`getFieldDefinitions` in interface `GraphqlFieldVisibility`
Parameters:
`fieldsContainer` - the type in play
Returns:
a non null list of `GraphQLInputObjectField`s

    - 

#### getFieldDefinition

```
public GraphQLInputObjectField getFieldDefinition(GraphQLInputFieldsContainer fieldsContainer,
                                                  java.lang.String fieldName)
```

Description copied from interface: `GraphqlFieldVisibility`
Called to get a named field from an input object type

Specified by:
`getFieldDefinition` in interface `GraphqlFieldVisibility`
Parameters:
`fieldsContainer` - the type in play
`fieldName` - the name of the desired field
Returns:
a `GraphQLInputObjectField` or null if its not visible

    - 

#### newBlock

```
public static BlockedFields.Builder newBlock()
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