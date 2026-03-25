# Source: https://chillicream.com/docs/hotchocolate/v14/api-reference/language

Title: Language - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/api-reference/language

Markdown Content:
Hot Chocolate v14

##### Table of contents

1.   [Introduction](https://chillicream.com/docs/hotchocolate/v14)
2.   [Getting Started](https://chillicream.com/docs/hotchocolate/v14/get-started-with-graphql-in-net-core)
3.   Defining a schema 
4.   Fetching data 
5.   Execution Engine 
6.   Integrations 
7.   Server 
8.   Performance 
9.   Security 
10.   API Reference 
11.   Migrating 

This is documentation for **v14**, which is no longer actively maintained.

For up-to-date documentation, see the

[latest stable version](https://chillicream.com/docs/hotchocolate/v15/api-reference/language).

[](https://chillicream.com/docs/hotchocolate/v14/api-reference/language#abstract-syntax-tree-ast)Abstract Syntax Tree (AST)
---------------------------------------------------------------------------------------------------------------------------

Hot Chocolate seems to focus solely around `ObjectType`, `InputType` et al. These types work as an interface to configure the _GraphQL_ schema. This schema is used to parse and validate incoming requests. Under the hood, every `query`, `mutation` or `subscription` request is parsed into a so-called abstract syntax tree. Each node of this tree denotes a part of the incoming _GraphQL_ query.

GraphQL

query Users {

userName

address {

street

nr

}

}

* * *

[](https://chillicream.com/docs/hotchocolate/v14/api-reference/language#syntax-node)Syntax Node
-----------------------------------------------------------------------------------------------

Every node in a syntax tree implements `ISyntaxNode`.

> 💡 The `ToString` method of a syntax node prints the corresponding _GraphQL_ syntax.

This interface defines the `NodeKind` of the node.

**Node Kinds:**

| Name | Description (Spec Link) | Context | Example |
| --- | --- | --- | --- |
| Name | [All names. e.g. Field, Argument ...](https://spec.graphql.org/June2018/#sec-Names) | Both | foo |
| NamedType | [Denotes a reference to a type](https://spec.graphql.org/June2018/#NamedType) | Both | Foo |
| ListType | [Definition of a list](https://spec.graphql.org/June2018/#ListType) | Both | [Foo] |
| NonNullType | [Definition of type that cannot be null](https://spec.graphql.org/June2018/#NonNullType) | Both | Foo! |
| Argument | [Representation of an argument. Has a _Name_ and a _Value_](https://spec.graphql.org/June2018/#sec-Language.Arguments) | Both | foo: "bar" |
| Directive | [Denotes a directive](https://spec.graphql.org/June2018/#sec-Language.Directives) | Query | @foo |
| Document | [Describes a complete file or request a _GraphQL_ service operates on.](https://spec.graphql.org/June2018/#sec-Language.Document) | Query(out) |  |
| OperationDefinition | [Describes a graphql operation like `query``mutation` or `subscription`](https://spec.graphql.org/June2018/#sec-Language.Document) | Query(out) | query Foo {} |
| VariableDefinition | [The variables defined by an operation](https://spec.graphql.org/June2018/#VariableDefinitions) | Query(out) | (\$foo: String) |
| Variable | [A variable](https://spec.graphql.org/June2018/#sec-Language.Variables) | Query(out) | \$foo |
| SelectionSet | [specifies a selection of _Field_, _FragmentSpread_ or _InlineFragment_](https://spec.graphql.org/June2018/#sec-Selection-Sets) | Query(out) | {foo bar} |
| Field | [Describes a field as a part of a selection set](https://spec.graphql.org/June2018/#sec-Language.Fields) | Query(out) | foo |
| FragmentSpread | [Denotes a spread of a `FragmentDefinition`](https://spec.graphql.org/June2018/#FragmentSpread) | Query(out) | ...f1 |
| InlineFragment | [Denotes an inline fragment](https://spec.graphql.org/June2018/#sec-Inline-Fragments) | Query(out) | ... on Foo { bar} |
| FragmentDefinition | [Defines the definition of a fragment](https://spec.graphql.org/June2018/#FragmentDefinition) | Query(out) | fragment f1 on Foo {} |
| IntValue | [Denotes a `int` value](https://spec.graphql.org/June2018/#sec-Int-Value) | Query(in) | 1 |
| StringValue | [Denotes a `string` value](https://spec.graphql.org/June2018/#sec-String-Value) | Query(in) | "bar" |
| BooleanValue | [Denotes a `boolean` value](https://spec.graphql.org/June2018/#sec-Boolean-Value) | Query(in) | true |
| NullValue | [Denotes a `null` value](https://spec.graphql.org/June2018/#sec-Null-Value) | Query(in) | null |
| EnumValue | [Denotes a `enum` value](https://spec.graphql.org/June2018/#sec-Enum-Value) | Query(in) | FOO |
| FloatValue | [Denotes a _Float_ value](https://spec.graphql.org/June2018/#sec-Float-Value) | Query(in) | 0.2 |
| ListValue | [Denotes a _List_ value](https://spec.graphql.org/June2018/#sec-List-Value) | Query(in) | ["string"] |
| ObjectValue | [Denotes a _ObjectValue_ value](https://spec.graphql.org/June2018/#sec-Input-Object-Values) | Query(in) | {foo: "bar" } |
| ObjectField | [Denotes a field of am input object type](https://spec.graphql.org/June2018/#ObjectField) | Query(in) | foo: "bar" |
| SchemaDefinition | [Definition of a schema](https://spec.graphql.org/June2018/#sec-Schema) | Schema | schema {} |
| OperationTypeDefinition | [This defines one of the root operations `Query`, `Mutation` or `Subscription` on the schema-definition](https://spec.graphql.org/June2018/#RootOperationTypeDefinition) | Schema | query:FooQuery |
| ScalarTypeDefinition | [Definition of a scalar](https://spec.graphql.org/June2018/#sec-Scalars) | Schema | scalar JSON |
| ObjectTypeDefinition | [Definition of an object type](https://spec.graphql.org/June2018/#sec-Objects) | Schema | type Foo{} |
| FieldDefinition | [Definition of a field](https://spec.graphql.org/June2018/#FieldDefinition) | Schema | bar:String |
| InputValueDefinition | [Definition of an input value of an argument](https://spec.graphql.org/June2018/#sec-Field-Arguments) | Schema | x: Float |
| InterfaceTypeDefinition | [Definition of an interface](https://spec.graphql.org/June2018/#sec-Interfaces) | Schema | interface NamedEntity {} |
| UnionTypeDefinition | [Definition of a union](https://spec.graphql.org/June2018/#sec-Unions) | Schema | union Ex = Foo | Bar |
| EnumTypeDefinition | [Definition of an enum](https://spec.graphql.org/June2018/#sec-Enums) | Schema | enum Foo {BAR} |
| EnumValueDefinition | [Definition of an enum value](https://spec.graphql.org/June2018/#sec-Enum) | Schema | BAR |
| InputObjectTypeDefinition | [Definition of an input type definition](https://spec.graphql.org/June2018/#sec-Input-Objects) | Schema | input FooInput {} |
| SchemaExtension | [Definition of a schema extension](https://spec.graphql.org/June2018/#sec-Schema-Extension) | Schema | extend schema {} |
| ScalarTypeExtension | [Definition of a scalar extension](https://spec.graphql.org/June2018/#sec-Scalar-Extensions) | Schema | extend scalar Foo @bar |
| ObjectTypeExtension | [Definition of an object type extension](https://spec.graphql.org/June2018/#sec-Object-Extensions) | Schema | extend type Foo { name} |
| InterfaceTypeExtension | [Definition of an interface type extension](https://spec.graphql.org/June2018/#sec-Interface-Extensions) | Schema | extend interface NamedEntity {} |
| UnionTypeExtension | [Definition of a union type extension](https://spec.graphql.org/June2018/#sec-Union-Extensions) | Schema | extend union Ex = Foo{} |
| EnumTypeExtension | [Definition of an enum type extension](https://spec.graphql.org/June2018/#sec-Enum-Extensions) | Schema | extend enum foo{} |
| InputObjectTypeExtension | [Definition of an input types](https://spec.graphql.org/June2018/#sec-Input-Object-Extensions) | Schema | input foo {} |
| DirectiveDefinition | [Definition of a directive](https://spec.graphql.org/June2018/#sec-Type-System.Directives) | Schema | directive @foo on |

Last updated on **2026-02-17** by**Tobias Tengler**
