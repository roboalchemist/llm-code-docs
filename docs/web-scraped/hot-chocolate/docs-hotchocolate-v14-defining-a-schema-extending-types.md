# Source: https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/extending-types

Title: Extending Types - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/extending-types

Markdown Content:
This is documentation for **v14**, which is no longer actively maintained.

For up-to-date documentation, see the

[latest stable version](https://chillicream.com/docs/hotchocolate/v15/defining-a-schema/extending-types).

Type extensions allow us to add, remove or replace fields on existing types, without necessarily needing access to these types.

Because of these capabilities, they also allow for better organization of our types. We could for example have classes that encapsulate part of our domain and extend our `Query` type with these functionalities.

Type extensions are especially useful if we want to modify third-party types, such as types that live in a separate assembly and are therefore not directly modifiable by us.

Warning

Type extensions do not produce the [extend type syntax that GraphQL offers](https://spec.graphql.org/draft/#sec-Object-Extensions), since it would unnecessarily complicate the resulting schema. Instead, Hot Chocolate's type extensions are directly merged with the original type definition to create a single type at runtime.

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/extending-types#object-types)Object Types
------------------------------------------------------------------------------------------------------------

Consider we have the following entity that we want to extend with functionality.

C#

public class Book

{

public int Id { get; set; }

public string Title { get; set; }

public int AuthorId { get; set; }

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/extending-types#adding-fields)Adding fields
--------------------------------------------------------------------------------------------------------------

We can easily add new fields to our existing `Book` type.

C#

[ExtendObjectType(typeof(Book))]

public class BookExtensions

{

public IEnumerable<string> GetGenres([Parent] Book book)

{

}

}

C#

builder.Services

.AddGraphQLServer()

.AddTypeExtension<BookExtensions>();

One of the most common use-cases for this would be adding new resolvers to one of our root types.

C#

[ExtendObjectType(typeof(Query))]

public class QueryBookResolvers

{

public IEnumerable<Book> GetBooks()

{

}

}

C#

builder.Services

.AddGraphQLServer()

.AddTypeExtension<QueryBookResolvers>();

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/extending-types#removing-fields)Removing fields
------------------------------------------------------------------------------------------------------------------

We can also ignore fields of the type we are extending.

C#

[ExtendObjectType(typeof(Book),

IgnoreProperties = new[] { nameof(Book.AuthorId) })]

public class BookExtensions

{

}

C#

builder.Services

.AddGraphQLServer()

.AddTypeExtension<BookExtensions>();

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/extending-types#replacing-fields)Replacing fields
--------------------------------------------------------------------------------------------------------------------

We might have an `Id` field, which we want to replace with a field that resolves the actual type the `Id` is pointing to.

In this example we replace the `authorId` field with an `author` field.

C#

[ExtendObjectType(typeof(Book))]

public class BookExtensions

{

[BindMember(nameof(Book.AuthorId))]

public Author GetAuthor([Parent] Book book)

{

}

}

C#

builder.Services

.AddGraphQLServer()

.AddTypeExtension<BookExtensions>();

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/extending-types#extending-by-name)Extending by name
----------------------------------------------------------------------------------------------------------------------

If we can not reference a type, we can still extend it by specifying its name.

C#

[ExtendObjectType("Foo")]

public class FooExtensions

{

}

When extending root types, we can make use of the constants in `OperationTypeNames`. We can for example use `OperationTypeNames.Query` instead of writing `"Query"` everywhere.

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/extending-types#extending-base-types)Extending base types
----------------------------------------------------------------------------------------------------------------------------

We can also extend multiple types at once, but still dedicate specific resolvers to specific types.

C#

// this extends every type that inherits from object (essentially every type)

[ExtendObjectType(typeof(object))]

public class ObjectExtensions

{

public string NewField()

{

}

public Author GetAuthor([Parent] Book book)

{

}

public IEnumerable<Book> GetBooks([Parent] Author author)

{

}

}

We can also modify all object types that are connected by a base type, like an interface.

C#

[InterfaceType]

public interface IPost

{

string Title { get; set; }

}

[ExtendObjectType(typeof(IPost))]

public class PostExtensions

{

public string NewField([Parent] IPost post)

{

}

}

> Note: The `IPost` is annotated with `[InterfaceType]` to include it in the GraphQL schema, but that isn't necessary for the type extension to work. We can use any base type, like `object` or an `abstract` base class, as an extension point without necessarily exposing the base type in our GraphQL schema.

Last updated on **2026-02-17** by**Tobias Tengler**
