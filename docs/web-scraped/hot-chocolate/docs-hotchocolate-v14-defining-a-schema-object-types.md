# Source: https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/object-types

Title: Object Types - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/object-types

Markdown Content:
The most important type in a GraphQL schema is the object type. It contains fields that can return simple scalars like `String`, `Int`, or again object types.

SDL

type Author {

name: String

}

type Book {

title: String

author: Author

}

Learn more about object types [here](https://graphql.org/learn/schema/#object-types-and-fields).

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/object-types#definition)Definition
-----------------------------------------------------------------------------------------------------

Object types can be defined like the following.

In the implementation-first approach we are essentially just creating regular C# classes.

C#

public class Author

{

public string Name { get; set; }

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/object-types#binding-behavior)Binding behavior
-----------------------------------------------------------------------------------------------------------------

In the implementation-first approach all public properties and methods are implicitly mapped to fields on the schema object type. The same is true for `T` of `ObjectType<T>` when using the code-first approach.

In the code-first approach we can also enable explicit binding, where we have to opt-in properties and methods we want to include instead of them being implicitly included.

We can configure our preferred binding behavior globally like the following.

C#

builder.Services

.AddGraphQLServer()

.ModifyOptions(options =>

{

options.DefaultBindingBehavior = BindingBehavior.Explicit;

});

Warning

This changes the binding behavior for all types, not only object types.

We can also override it on a per type basis:

C#

public class BookType : ObjectType<Book>

{

protected override void Configure(IObjectTypeDescriptor<Book> descriptor)

{

descriptor.BindFields(BindingBehavior.Implicit);

}

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/object-types#ignoring-fields)Ignoring fields
---------------------------------------------------------------------------------------------------------------

In the implementation-first approach we can ignore fields using the `[GraphQLIgnore]` attribute.

C#

public class Book

{

[GraphQLIgnore]

public string Title { get; set; }

public Author Author { get; set; }

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/object-types#including-fields)Including fields
-----------------------------------------------------------------------------------------------------------------

In the code-first approach we can explicitly include properties of our POCO using the `Field` method on the `IObjectTypeDescriptor`. This is only necessary, if the binding behavior of the object type is explicit.

C#

public class BookType : ObjectType<Book>

{

protected override void Configure(IObjectTypeDescriptor<Book> descriptor)

{

descriptor.BindFieldsExplicitly();

descriptor.Field(f => f.Title);

}

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/object-types#naming)Naming
---------------------------------------------------------------------------------------------

Unless specified explicitly, Hot Chocolate automatically infers the names of object types and their fields. Per default the name of the class becomes the name of the object type. When using `ObjectType<T>` in code-first, the name of `T` is chosen as the name for the object type. The names of methods and properties on the respective class are chosen as names of the fields of the object type.

The following conventions are applied when transforming C# method and property names into SDL types and fields:

*   **Get prefixes are removed:** The get operation is implied and therefore redundant information.
*   **Async postfixes are removed:** The `Async` is an implementation detail and therefore not relevant to the schema.
*   **The first letter is lowercased:** This is not part of the specification, but a widely agreed upon standard in the GraphQL world.

If we need to we can override these inferred names.

The `[GraphQLName]` attribute allows us to specify an explicit name.

C#

[GraphQLName("BookAuthor")]

public class Author

{

[GraphQLName("fullName")]

public string Name { get; set; }

}

This would produce the following `BookAuthor` schema object type:

SDL

type BookAuthor {

fullName: String

}

If only one of our clients requires specific names, it is better to use [aliases](https://graphql.org/learn/queries/#aliases) in this client's operations than changing the entire schema.

GraphQL

{

MyUser: user {

Username: name

}

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/object-types#explicit-types)Explicit types
-------------------------------------------------------------------------------------------------------------

Hot Chocolate will, most of the time, correctly infer the schema types of our fields. Sometimes we might have to be explicit about it though. For example when we are working with custom scalars or code-first types in general.

In the implementation-first approach we can use the `[GraphQLType]` attribute.

C#

public class Author

{

[GraphQLType(typeof(StringType))]

public string Name { get; set; }

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/object-types#additional-fields)Additional fields
-------------------------------------------------------------------------------------------------------------------

We can add additional (dynamic) fields to our schema types, without adding new properties to our backing class.

C#

public class Author

{

public string Name { get; set; }

public DateTime AdditionalField()

{

}

}

What we have just created is a resolver. Hot Chocolate automatically creates resolvers for our properties, but we can also define them ourselves.

[Learn more about resolvers](https://chillicream.com/docs/hotchocolate/v14/fetching-data/resolvers)

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/object-types#generics)Generics
-------------------------------------------------------------------------------------------------

> Note: Read about [interfaces](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/interfaces) and [unions](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/unions) before resorting to generic object types.

In the code-first approach we can define generic object types.

C#

public class Response

{

public string Status { get; set; }

public object Payload { get; set; }

}

public class ResponseType<T> : ObjectType<Response>

where T : class, IOutputType

{

protected override void Configure(

IObjectTypeDescriptor<Response> descriptor)

{

descriptor.Field(f => f.Status);

descriptor

.Field(f => f.Payload)

.Type<T>();

}

}

public class Query

{

public Response GetResponse()

{

return new Response

{

Status = "OK",

Payload = 123

};

}

}

public class QueryType : ObjectType<Query>

{

protected override void Configure(IObjectTypeDescriptor<Query> descriptor)

{

descriptor

.Field(f => f.GetResponse())

.Type<ResponseType<IntType>>();

}

}

This will produce the following schema types.

SDL

type Query {

response: Response

}

type Response {

status: String!

payload: Int

}

We have used an `object` as the generic field above, but we can also make `Response` generic and add another generic parameter to the `ResponseType`.

C#

public class Response<T>

{

public string Status { get; set; }

public T Payload { get; set; }

}

public class ResponseType<TSchemaType, TRuntimeType>

: ObjectType<Response<TRuntimeType>>

where TSchemaType : class, IOutputType

{

protected override void Configure(

IObjectTypeDescriptor<Response<TRuntimeType>> descriptor)

{

descriptor.Field(f => f.Status);

descriptor

.Field(f => f.Payload)

.Type<TSchemaType>();

}

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/object-types#naming-1)Naming
-----------------------------------------------------------------------------------------------

If we were to use the above type with two different generic arguments, we would get an error, since both `ResponseType` have the same name.

We can change the name of our generic object type depending on the used generic type.

C#

public class ResponseType<T> : ObjectType<Response>

where T : class, IOutputType

{

protected override void Configure(

IObjectTypeDescriptor<Response> descriptor)

{

descriptor

.Name(dependency => dependency.Name + "Response")

.DependsOn<T>();

descriptor.Field(f => f.Status);

descriptor

.Field(f => f.Payload)

.Type<T>();

}

}

Last updated on **2026-02-17** by**Tobias Tengler**
