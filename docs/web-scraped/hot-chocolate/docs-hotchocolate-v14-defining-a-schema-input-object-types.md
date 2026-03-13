# Source: https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/input-object-types

Title: Input Object Types - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/input-object-types

Markdown Content:
We already looked at [arguments](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/arguments), which allow us to use simple [scalars](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/scalars) like `String` to pass data into a field. GraphQL defines input object types to allow us to use objects as arguments on our fields.

Input object type definitions differ from [object types](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/object-types) only in the used keyword and in that their fields can not have arguments.

SDL

input BookInput {

title: String

author: String

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/input-object-types#defining-an-input-type)Defining an Input Type
-----------------------------------------------------------------------------------------------------------------------------------

Input object types can be defined like the following.

C#

public class BookInput

{

public string Title { get; set; }

public string Author { get; set; }

}

public class Mutation

{

public async Task<Book> AddBook(BookInput input)

{

}

}

> Note: If a class is used as an argument to a resolver and it does not end in `Input`, Hot Chocolate (by default) will append `Input` to the type name in the resulting schema.

We can also use a class both as an output- and an input-type.

C#

public class Book

{

public string Title { get; set; }

public string Author { get; set; }

}

public class Mutation

{

public async Task<Book> AddBook(Book input)

{

}

}

This will produce the following schema.

SDL

type Book {

title: String

author: String

}

input BookInput {

title: String

author: String

}

type Mutation {

addBook(input: BookInput): Book

}

> Note: While it is possible, it is not encouraged, as it complicates future extensions of either type.

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/input-object-types#immutable-types)Immutable types
---------------------------------------------------------------------------------------------------------------------

If we want our input type classes to be immutable, or we are using [nullable reference types](https://docs.microsoft.com/dotnet/csharp/nullable-references), we can provide a non-empty constructor and Hot Chocolate will instead use that when instantiating the input. Just note that

1.   The type of the argument must exactly match the property's type
2.   The name of the argument must match the property name (bar a lowercase first letter)
3.   No setters will be called, so you need to provide arguments for all the properties.

Hot Chocolate validates any custom input constructor at schema build time, so we don't need to worry about breaking things during refactoring!

C#

public class BookInput

{

public string Title { get; }

public string Author { get; }

public BookingInput(string title, string author)

{

Title = title;

Author = author;

}

}

We can also use record types, if we're on C# 9.0+. The equivalent to the above would be:

C#

public record BookingInput(string Title, string Author);

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/input-object-types#default-values)Default Values
-------------------------------------------------------------------------------------------------------------------

In GraphQL, default values can be assigned to arguments and input types. These values are automatically utilized if no other value is provided when a query or mutation is executed.

Default values are specified in the GraphQL schema by appending `= value` to the argument or input type definition. For example: `field(value: Int = 10)` would give `value` a default of 10.

Default values can be set for any input types, including scalars, enums, and input object types. They can also be used with list types and non-null types.

Consider the following schema:

GraphQL

type Query {

user(active: Boolean = true): [User]

}

input UserInput {

name: String

active: Boolean = true

}

In the `user` query field, the `active` argument has a default value of `true`. Similarly, in the `UserInput` type, the `active` field defaults to `true`.

In resolvers, arguments with default values are treated as optional. If the client does not provide a value, the resolver will receive the default value. This makes handling optional fields in your resolvers much easier.

This means you can write the following query against the schema described before:

GraphQL

query fetchUser {

user {

name

}

}

Default values also play a vital role in maintaining backward compatibility. When adding new fields to an input type or new arguments to a field, providing a default value ensures existing queries will still work.

For instance, consider the situation where we want to extend the `user` field with another argument. As long as this new argument has a default value, it won't affect the functionality of the `fetchUser` query:

GraphQL

type Query {

user(active: Boolean = true, role: String = "user"): User

}

Despite the addition of the `role` argument, the `fetchUser` query can still be executed without supplying this new argument, as the `role` will default to `"user"`.

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/input-object-types#specifying-defaultvalues)Specifying DefaultValues
---------------------------------------------------------------------------------------------------------------------------------------

The `DefaultValueAttribute` or the `DefaultValue` method on the field descriptor, allow you to assign default values to your fields or arguments.

Consider the following scenario where we have a `UserInput` type with different fields like `name`, `active`. By default, we would like `active` to be `true`.

C#

public class UserInput

{

public string? Name { get; set; }

[DefaultValue(true)]

public bool IsActive { get; set; }

}

This will produce the following schema:

SDL

input UserInput {

name: String

active: Boolean! = true

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/input-object-types#using-graphql-syntax)Using GraphQL Syntax
-------------------------------------------------------------------------------------------------------------------------------

It is also possible to specify default values using GraphQL value syntax. This comes in handy when you want to set default values that are more than just simple scalars. Like for example objects or lists.

Consider a scenario where we have a `UserProfileInput` type with a field `preferences`. The `preferences` field itself is an object containing various user preference settings.

C#

public class Preferences

{

public bool Notifications { get; set; }

public string Theme { get; set; }

}

public class UserProfileInput

{

public string? Name { get; set; }

[DefaultValueSyntax("{ notifications: true, theme: 'light' }")]

public Preferences? Preferences { get; set; }

}

This will produce the following schema:

SDL

input PreferencesInput {

notifications: Boolean

theme: String

}

input UserProfileInput {

name: String

preferences: PreferencesInput = { notifications: true, theme: "light" }

}

In this example, if no value for `preferences` is provided when making a mutation, the system will automatically use the default value `{ notifications: true, theme: 'light' }`.

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/input-object-types#optional-properties)Optional Properties
-----------------------------------------------------------------------------------------------------------------------------

If we want our input type classes to contain optional properties, we can use the `Optional<T>` type or mark the properties of the class as `nullable`. It is important to also define a default value for any non-nullable property that is using the `Optional<T>` type by adding the `[DefaultValue]` attribute, otherwise the field will still be required when defining the input.

C#

public class BookInput

{

[DefaultValue("")]

public Optional<string> Title { get; set; }

public string Author { get; set; }

public BookInput(string title, string author)

{

Title = title;

Author = author;

}

}

Also with record types, the equivalent of the above would be:

C#

public record BookInput([property:DefaultValue("")]Optional<string> Title, string Author);

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/input-object-types#oneof-input-objects)`OneOf` Input Objects
-------------------------------------------------------------------------------------------------------------------------------

`OneOf` Input Objects are a special variant of Input Objects where the type system asserts that exactly one of the fields must be set and non-null, all others being omitted. This is represented in introspection with the _ _ Type.oneField: Boolean field, and in SDL via the @oneOf directive on the input object.

This introduces a form of input polymorphism to GraphQL. For example, the following PetInput input object lets you choose between a number of potential input types:

SDL

input PetInput @oneOf {

cat: CatInput

dog: DogInput

fish: FishInput

}

input CatInput { name: String!, numberOfLives: Int }

input DogInput { name: String!, wagsTail: Boolean }

input FishInput { name: String!, bodyLengthInMm: Int }

type Mutation {

addPet(pet: PetInput!): Pet

}

Since the `OneOf` Input Objects RFC is not yet in the draft stage it is still an opt-in feature. In order to activate it set the schema options to enable it.

C#

builder.Services

.AddGraphQLServer()

...

.ModifyOptions(o => o.EnableOneOf = true);

Once activate you can create `OneOf` Input Objects like the following:

C#

[OneOf]

public class PetInput

{

public Dog? Dog { get; set; }

public Cat? Cat { get; set; }

}

public interface IPet

{

string Name { get; }

}

public class Dog : IPet

{

public string Name { get; set; }

}

public class Cat : IPet

{

public string Name { get; set; }

}

public class Mutation

{

public Task<IPet> CreatePetAsync(PetInput input)

{

}

}

This will produce the following schema.

SDL

input PetInput @oneOf {

dog: DogInput

cat: CatInput

}

input DogInput {

name: String!

}

input CatInput {

name: String!

}

interface Pet {

name: String!

}

type Dog implements Pet {

name: String!

}

type Cat implements Pet {

name: String!

}

type Mutation {

createPet(input: PetInput): Pet

}

Last updated on **2026-02-17** by**Tobias Tengler**
