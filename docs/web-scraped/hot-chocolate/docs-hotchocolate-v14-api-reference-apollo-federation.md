# Source: https://chillicream.com/docs/hotchocolate/v14/api-reference/apollo-federation

Title: Apollo Federation Subgraph Support - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/api-reference/apollo-federation

Markdown Content:
> If you want to read more about Apollo Federation in general, you can head over to the [Apollo Federation documentation](https://www.apollographql.com/docs/federation/), which provides a robust overview and set of examples for this GraphQL architectural pattern. Many of the core principles and concepts are referenced within this document.

Hot Chocolate includes an implementation of the Apollo Federation v1 specification for creating Apollo Federated subgraphs. Through Apollo Federation, you can combine multiple GraphQL APIs into a single API for your consumers.

The documentation describes the syntax for creating an Apollo Federated subgraph using Hot Chocolate and relates the implementation specifics to its counterpart in the Apollo Federation docs. This document _will not_ provide a thorough explanation of the Apollo Federation core concepts nor will it describe how you go about creating a supergraph to stitch together various subgraphs, as the Apollo Federation team already provides thorough documentation of those principles.

You can find example projects of the Apollo Federation library in [Hot Chocolate examples](https://github.com/ChilliCream/graphql-platform/tree/main/src/HotChocolate/ApolloFederation/examples).

[](https://chillicream.com/docs/hotchocolate/v14/api-reference/apollo-federation#get-started)Get Started
--------------------------------------------------------------------------------------------------------

To use the Apollo Federation tools, you need to first install v12.6 or later of the `HotChocolate.ApolloFederation` package.

Bash

dotnet add package HotChocolate.ApolloFederation

Warning

All `HotChocolate.*` packages need to have the same version.

After installing the necessary package, you'll need to register the Apollo Federation services with the GraphQL server.

C#

builder.Services

.AddGraphQLServer()

.AddApolloFederation();

[](https://chillicream.com/docs/hotchocolate/v14/api-reference/apollo-federation#defining-an-entity)Defining an entity
----------------------------------------------------------------------------------------------------------------------

Now that the API is ready to support Apollo Federation, we'll need to define an **entity**—an object type that can resolve its fields across multiple subgraphs. We'll work with a `Product` entity to provide an example of how to do this.

C#

public class Product

{

[ID]

public string Id { get; set; }

public string Name { get; set; }

public float Price { get; set; }

}

[](https://chillicream.com/docs/hotchocolate/v14/api-reference/apollo-federation#define-an-entity-key)Define an entity key
--------------------------------------------------------------------------------------------------------------------------

Once we have an object type to work with, we'll [define a key](https://www.apollographql.com/docs/federation/entities#1-define-a-key) for the entity. A key in an Apollo Federated subgraph effectively serves as an "identifier" that can uniquely locate an individual record of that type. This will typically be something like a record's primary key, a SKU, or an account number.

In an implementation-first approach, we'll use the `[Key]` attribute on any property or properties that can be referenced as a key by another subgraph.

C#

public class Product

{

[ID]

[Key]

public string Id { get; set; }

public string Name { get; set; }

public float Price { get; set; }

}

[](https://chillicream.com/docs/hotchocolate/v14/api-reference/apollo-federation#define-a-reference-resolver)Define a reference resolver
----------------------------------------------------------------------------------------------------------------------------------------

Next, we'll need to define an [entity reference resolver](https://www.apollographql.com/docs/federation/entities#2-define-a-reference-resolver) so that the supergraph can resolve this entity across multiple subgraphs during a query. Every subgraph that contributes at least one unique field to an entity must define a reference resolver for that entity.

In an implementation-first approach, a reference resolver will work just like a [regular resolver](https://chillicream.com/docs/hotchocolate/v14/fetching-data/resolvers) with some key differences:

1.   It must be annotated with the `[ReferenceResolver]` attribute
2.   It must be a `public static` method _within_ the type it is resolving

C#

public class Product

{

[ID]

[Key]

public string Id { get; set; }

public string Name { get; set; }

public float Price { get; set; }

[ReferenceResolver]

public static async Task<Product?> ResolveReference(

string id,

ProductBatchDataLoader dataLoader

)

{

return await dataloader.LoadAsync(id);

}

}

Some important details to highlight about `[ReferenceResolver]` methods.

1.   The name of the method decorated with the `[ReferenceResolver]` attribute does not matter. However, as with all programming endeavors, you should aim to provide a descriptive name that reveals the method's intention.
2.   The parameter name and type used in the reference resolver **must match** the GraphQL field name of the `[Key]` attribute, e.g., if the GraphQL key field is `id: String!` or `id: ID!` then the reference resolver's parameter must be `string id`.
3.   If you're using [nullable reference types](https://learn.microsoft.com/en-us/dotnet/csharp/nullable-references), you should make sure the return type is marked as possibly null, i.e., `T?`.
4.   If you have multiple keys defined for an entity, you should include a reference resolver for _each key_ so that the supergraph is able to resolve your entity regardless of which key(s) another graph uses to reference that entity.

C#

public class Product

{

[Key]

public string Id { get; set; }

[Key]

public int Sku { get; set; }

[ReferenceResolver]

public static Product? ResolveReferenceById(string id)

{

}

[ReferenceResolver]

public static Product? ResolveReferenceBySku(int sku)

{

}

}

> ### [](https://chillicream.com/docs/hotchocolate/v14/api-reference/apollo-federation#a-note-about-reference-resolvers)A note about reference resolvers
> 
> 
> It's recommended to use a [dataloader](https://chillicream.com/docs/hotchocolate/v14/fetching-data/dataloader) to fetch the data in a reference resolver. This helps the API avoid [an N+1 problem](https://www.apollographql.com/docs/federation/entities-advanced#handling-the-n1-problem) when a query resolves multiple items from a given subgraph.

[](https://chillicream.com/docs/hotchocolate/v14/api-reference/apollo-federation#register-the-entity)Register the entity
------------------------------------------------------------------------------------------------------------------------

After our type has a key or keys and a reference resolver defined, you'll register the type in the GraphQL schema, which will register it as a type within the GraphQL API itself as well as within the [auto-generated `_service { sdl }` field](https://www.apollographql.com/docs/federation/subgraph-spec/#required-resolvers-for-introspection) within the API.

_Entity type registration_

C#

builder.Services

.AddGraphQLServer()

.AddApolloFederation()

.AddType<Product>()

;

[](https://chillicream.com/docs/hotchocolate/v14/api-reference/apollo-federation#testing-and-executing-your-reference-resolvers)Testing and executing your reference resolvers
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

After creating an entity, you'll likely wonder "how do I invoke and test this reference resolver?" Entities that define a reference resolver can be queried through the [auto-generated `_entities` query](https://www.apollographql.com/docs/federation/subgraph-spec#understanding-query_entities) at the subgraph level.

You'll invoke the query by providing an array of representations using a combination of a `__typename` and key field values to invoke the appropriate resolver. An example query for our `Product` would look something like the following.

_Entities query_

GraphQL

query {

_entities(

representations: [

{ __typename: "Product", id: "<id value of the product>" }

]

) {

... on Product {

id

name

price

}

}

}

_Entities query result_

JSON

{

"data": {

"_entities": [

{

"id": "<id value of the product>",

"name": "Foobar",

"price": 10.99

}

]

}

}

> **Note**: The `_entities` field is an internal implementation detail of Apollo Federation that is necessary for the supergraph to properly resolve entities. API consumers **should not** use the `_entities` field directly nor should they send requests to a subgraph directly. We're only highlighting how to use the `_entities` field so that you can validate and test your subgraph and its entity reference resolvers at runtime or using tools like [`Microsoft.AspNetCore.Mvc.Testing`](https://learn.microsoft.com/aspnet/core/test/integration-tests).

[](https://chillicream.com/docs/hotchocolate/v14/api-reference/apollo-federation#referencing-an-entity-type)Referencing an entity type
--------------------------------------------------------------------------------------------------------------------------------------

Now that we have an entity defined in one of our subgraphs, let's go ahead and create a second subgraph that will make use of our `Product` type. Remember, all of this work should be performed in a _**separate API project**_.

In the second subgraph, we'll create a `Review` type that is focused on providing reviews of `Product` entities from the other subgraph. We'll do that by defining our `Review` type along with a [service type reference](https://www.apollographql.com/docs/federation/entities/#referencing-an-entity-without-contributing-fields) that represents the `Product`.

In our new subgraph API we'll need to start by creating the `Product`. When creating the extended service type, make sure to consider the following details

*   The _GraphQL type name_**must match**. Often, this can be accomplished by using the same class name between the projects, but you can also use tools like the `[GraphQLName(string)]` attribute or `IObjectTypeDescriptor<T>.Name(string)` method to explicitly set a GraphQL name.
*   The extended type must include _at least one_ key that matches in both name and GraphQL type from the source graph.
    *   In our example, we'll be referencing the `id: ID!` field that was defined on our `Product`

C#

[ExtendServiceType]

public class Product

{

[ID]

[Key]

public string Id { get; set; }

}

builder.Services

.AddGraphQLServer()

.AddApolloFederation()

.AddType<Product>();

Next, we'll create our `Review` type that has a reference to the `Product` entity. Similar to our first class, we'll need to denote the type's key(s) and the corresponding entity reference resolver(s).

C#

public class Review

{

[ID]

[Key]

public string Id { get; set; }

public string Content { get; set; }

[GraphQLIgnore]

public string ProductId { get; set; }

public Product GetProduct() => new Product { Id = ProductId };

[ReferenceResolver]

public static Review? ResolveReference(string id)

{

}

}

builder.Services

.AddGraphQLServer()

.AddApolloFederation()

.AddType<Product>()

.AddType<Review>();

In the above snippet two things may pop out as strange to you:

1.   Why did we explicitly ignore the `ProductId` property?
    *   The `ProductId` is, in essence, a "foreign key" to the other graph. Instead of presenting that data as a field of the `Review` type, we're presenting it through the `product: Product!` GraphQL field that is produced by the `GetProduct()` method. This allows the Apollo supergraph to stitch the `Review` and `Product` types together and represent that a query can traverse from the `Review` to the `Product` it is reviewing and make the API more graph-like. With that said, it is not strictly necessary to ignore the `ProductId` or any other external entity Id property.

2.   Why does the `GetProduct()` method instantiate its own `new Product { Id = ProductId }` object?
    *   Since our goal with Apollo Federation is decomposition and [concern-based separation](https://www.apollographql.com/docs/federation/#concern-based-separation), a second subgraph is likely to have that "foreign key" reference to the type that is reference from the other subgraph. However, this graph does not "own" the actual data of the entity itself. This is why our sample simply performs a `new Product { Id = ProductId }` statement for the resolver: it's not opinionated about how the other data of a `Product` is resolved from its owning graph.

With our above changes, we can successfully connect these two subgraphs into a single query within an Apollo supergraph, allowing our API users to send a query like the following.

GraphQL

query {

review(id: "<review id>") {

id

content

product {

id

name

}

}

}

As a reminder, you can create and configure a supergraph by following either the [Apollo Router documentation](https://www.apollographql.com/docs/router/quickstart/) or [`@apollo/gateway` documentation](https://www.npmjs.com/package/@apollo/gateway).

[](https://chillicream.com/docs/hotchocolate/v14/api-reference/apollo-federation#contributing-fields-through-resolvers)Contributing fields through resolvers
------------------------------------------------------------------------------------------------------------------------------------------------------------

Now that our new subgraph has the `Product` reference we can [contribute additional fields to the type](https://www.apollographql.com/docs/federation/entities#contributing-entity-fields). Similar to other types in Hot Chocolate, you can create new fields by defining different method or property resolvers. For a full set of details and examples on creating resolvers, you can read our [documentation on resolvers](https://chillicream.com/docs/hotchocolate/v14/fetching-data/resolvers).

For now, we'll focus on giving our supergraph the ability to retrieve all reviews for a given product by adding a `reviews: [Review!]!` property to the type.

C#

[ExtendServiceType]

public class Product

{

[ID]

[Key]

public string Id { get; set; }

public async Task<IEnumerable<Review>> GetReviews(

ReviewRepository repo

)

{

return await repo.GetReviewsByProductIdAsync(Id);

}

}

These changes will successfully add the new field within the subgraph! However, our current implementation cannot be resolved if we start at a product such as `query { product(id: "foo") { reviews { ... } } }`. To fix this, we'll need to implement an entity reference resolver in our second subgraph.

As mentioned above, since this subgraph does not "own" the data for a `Product`, our resolver will be fairly naive, similar to the `Review::GetProduct()` method: it will simply instantiate a `new Product { Id = id }`. We do this because the reference resolver should only be directly invoked by the supergraph, so our new reference resolver will simply assume the data exists. However, if there is data that needs to be fetched from some kind of data store, the resolver can still do this just as any other data resolver in Hot Chocolate.

C#

[ExtendServiceType]

public class Product

{

[ID]

[Key]

public string Id { get; set; }

public async Task<IEnumerable<Review>> GetReviews(

ReviewRepository repo

)

{

return await repo.GetReviewsByProductIdAsync(Id);

}

[ReferenceResolver]

public static Product ResolveProductReference(string id) => new Product { Id = id };

}

With the above changes, our supergraph can now support traversing both "from a review to a product" as well as "from a product to a review"!

GraphQL

# Example root query fields - not implemented in the tutorial

query {

review(id: "foo") {

id

content

product {

id

name

price

reviews {

id

content

}

}

}

product(id: "bar") {

id

name

price

reviews {

id

content

}

}

}

Last updated on **2026-02-17** by**Tobias Tengler**
