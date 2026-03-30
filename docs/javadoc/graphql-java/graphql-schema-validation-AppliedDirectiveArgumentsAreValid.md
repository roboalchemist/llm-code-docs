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

graphql.schema.validation

## Class AppliedDirectiveArgumentsAreValid

- java.lang.Object

- 

  - graphql.schema.GraphQLTypeVisitorStub

  - 

    - graphql.schema.validation.AppliedDirectiveArgumentsAreValid

- 

All Implemented Interfaces:
GraphQLTypeVisitor

---

```
public class AppliedDirectiveArgumentsAreValid
extends GraphQLTypeVisitorStub
```

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AppliedDirectiveArgumentsAreValid()` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`TraversalControl`
`visitGraphQLDirective(GraphQLDirective directive,
                     TraverserContext<GraphQLSchemaElement> context)` 

    - 

### Methods inherited from class graphql.schema.GraphQLTypeVisitorStub

`visitGraphQLArgument, visitGraphQLEnumType, visitGraphQLEnumValueDefinition, visitGraphQLFieldDefinition, visitGraphQLInputObjectField, visitGraphQLInputObjectType, visitGraphQLInterfaceType, visitGraphQLList, visitGraphQLNonNull, visitGraphQLObjectType, visitGraphQLScalarType, visitGraphQLType, visitGraphQLTypeReference, visitGraphQLUnionType`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

    - 

### Methods inherited from interface graphql.schema.GraphQLTypeVisitor

`changeNode, deleteNode, insertAfter, insertBefore, visitBackRef, visitGraphQLCompositeType, visitGraphQLDirectiveContainer, visitGraphQLFieldsContainer, visitGraphQLInputFieldsContainer, visitGraphQLInputType, visitGraphQLModifiedType, visitGraphQLNullableType, visitGraphQLOutputType, visitGraphQLUnmodifiedType`

- 

  - 

### Constructor Detail

    - 

#### AppliedDirectiveArgumentsAreValid

```
public AppliedDirectiveArgumentsAreValid()
```

  - 

### Method Detail

    - 

#### visitGraphQLDirective

```
public TraversalControl visitGraphQLDirective(GraphQLDirective directive,
                                              TraverserContext<GraphQLSchemaElement> context)
```

Specified by:
`visitGraphQLDirective` in interface `GraphQLTypeVisitor`
Overrides:
`visitGraphQLDirective` in class `GraphQLTypeVisitorStub`

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