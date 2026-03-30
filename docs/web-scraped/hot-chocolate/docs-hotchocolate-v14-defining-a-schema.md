# Source: https://chillicream.com/docs/hotchocolate/v14/defining-a-schema

Title: Overview - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/defining-a-schema

Markdown Content:
This is documentation for **v14**, which is no longer actively maintained.

For up-to-date documentation, see the

[latest stable version](https://chillicream.com/docs/hotchocolate/v15/defining-a-schema).

In this section we will learn everything that is needed to build an expressive GraphQL schema.

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema#operations)Operations
----------------------------------------------------------------------------------------

First we will look at the three root types, often called _Operations_, that represent entry points to our schema:

*   Queries allow us to _query_ our graph and retrieve data in a readonly manner.

[Learn more about queries](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/queries)

*   Mutations allow us to _mutate_ our graph entities in the form of adding, removing or updating entities.

[Learn more about mutations](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/mutations)

*   Subscriptions allow us to _subscribe_ to events in our system and be notified in real-time of their occurrence.

[Learn more about subscriptions](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/subscriptions)

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema#types)Types
------------------------------------------------------------------------------

Each GraphQL schema is made up of two basic building blocks:

*   Object types contain fields and describe our entities.

[Learn more about object types](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/object-types)

*   Scalars are the primitives of our GraphQL schema: `String`, `Int`, etc.

We can also define custom scalars to more precisely describe our business domain.

[Learn more about scalars](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/scalars)

There are also more advanced types:

*   Enums are a special kind of scalar, restricted to a particular set of allowed values.

[Learn more about enums](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/enums)
*   Interfaces represent a shared contract that other types can implement.

[Learn more about interfaces](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/interfaces)
*   Unions represent a set of object types, without the need for a shared contract.

[Learn more about unions](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/unions).

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema#type-modifiers)Type Modifiers
------------------------------------------------------------------------------------------------

Besides regular types, like scalars and object types, there are also _type modifiers_.

A non-null field for example indicates that a client can always expect a non-null value to be returned from the field.

[Learn more about non-null](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/non-null)

List fields indicate to a client that the field will return a list in the specified shape.

[Learn more about lists](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/lists)

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema#arguments)Arguments
--------------------------------------------------------------------------------------

We can pass arguments to individual fields on an object type and access their values inside the field's resolver.

[Learn more about arguments](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/arguments)

Nested object types can also be used as arguments by declaring so called input object types. These are most commonly used when passing a payload to a mutation.

[Learn more about input object types](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/input-object-types)

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema#extending-types)Extending Types
--------------------------------------------------------------------------------------------------

Hot Chocolate allows us to extend existing types, helping us keep our code organized.

Rather than adding more and more fields to the Query type in the same class for instance, we can _extend_ the Query type with a new field from another location in our codebase where that field logically should live.

[Learn more about extending types](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/extending-types)

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema#directives)Directives
----------------------------------------------------------------------------------------

Directives allow us to decorate parts of our GraphQL schema with additional configuration.

This configuration can be used as metadata for client tools or alternate our GraphQL server's runtime execution and type validation behavior.

[Learn more about directives](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/directives)

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema#schema-evolution)Schema evolution
----------------------------------------------------------------------------------------------------

As our data graph and number of developers/clients grows, we need to ensure that the graph is understood by everyone. Therefore, our schema should expose as much information to consumers of our API as possible.

[Learn more about schema documentation](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/documentation)

[Learn more about versioning](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/versioning)

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema#relay)Relay
------------------------------------------------------------------------------

[Relay](https://relay.dev/) proposes some schema design principles for GraphQL servers in order to more efficiently fetch, refetch and cache entities on the client. Since these principles make for a better schema, we encourage all users, not only those of Relay, to consider these principles.

[Learn more about Relay-compatible schema design](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/relay)

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema#automatic-type-registration)Automatic type registration
--------------------------------------------------------------------------------------------------------------------------

Starting with Hot Chocolate 12.7 we introduced a new source generator that automatically registers types and DataLoader with your GraphQL configuration builder. Watch on YouTube how you can simplify your Hot Chocolate configuration code.

Last updated on **2026-02-17** by**Tobias Tengler**
