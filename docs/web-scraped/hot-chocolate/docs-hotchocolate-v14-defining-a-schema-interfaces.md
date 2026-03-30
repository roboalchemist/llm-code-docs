# Source: https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/interfaces

Title: Interfaces - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/interfaces

Markdown Content:
An interface is an abstract type that defines a certain set of fields that an object type or another interface must include to implement the interface. Interfaces can only be used as output types, meaning we can't use interfaces as arguments or as fields on input object types.

SDL

interface Message {

author: User!

createdAt: DateTime!

}

type TextMessage implements Message {

author: User!

createdAt: DateTime!

content: String!

}

type Query {

messages: [Message]!

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/interfaces#usage)Usage
-----------------------------------------------------------------------------------------

Given is the schema from above.

When querying a field returning an interface, we can query the fields defined in the interface like we would query a regular object type.

GraphQL

{

messages {

createdAt

}

}

If we need to access fields that are part of an object type implementing the interface, we can do so using [fragments](https://graphql.org/learn/queries/#fragments).

GraphQL

{

messages {

createdAt

... on TextMessage {

content

}

}

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/interfaces#definition)Definition
---------------------------------------------------------------------------------------------------

Interfaces can be defined like the following.

C#

[InterfaceType("Message")]

public interface IMessage

{

User Author { get; set; }

DateTime CreatedAt { get; set; }

}

public class TextMessage : IMessage

{

public User Author { get; set; }

public DateTime CreatedAt { get; set; }

public string Content { get; set; }

}

public class Query

{

public IMessage[] GetMessages()

{

}

}

C#

builder.Services

.AddGraphQLServer()

.AddQueryType<Query>()

.AddType<TextMessage>();

We can also use classes to define an interface.

C#

[InterfaceType]

public abstract class Message

{

public User SendBy { get; set; }

public DateTime CreatedAt { get; set; }

}

public class TextMessage : Message

{

public string Content { get; set; }

}

C#

builder.Services

.AddGraphQLServer()

.AddType<TextMessage>();

> Note: We have to explicitly register the interface implementations:
> 
> 
> 
> C#
> 
> 
> services.AddGraphQLServer().AddType<TextMessageType>()

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/interfaces#binding-behavior)Binding behavior
---------------------------------------------------------------------------------------------------------------

In the implementation-first approach all public properties and methods are implicitly mapped to fields on the schema interface type. The same is true for `T` of `InterfaceType<T>` when using the code-first approach.

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

This changes the binding behavior for all types, not only interface types.

We can also override it on a per type basis:

C#

public class MessageType : InterfaceType<IMessage>

{

protected override void Configure(

IInterfaceTypeDescriptor<IMessage> descriptor)

{

descriptor.BindFields(BindingBehavior.Implicit);

}

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/interfaces#ignoring-fields)Ignoring fields
-------------------------------------------------------------------------------------------------------------

In the implementation-first approach we can ignore fields using the `[GraphQLIgnore]` attribute.

C#

public interface IMessage

{

[GraphQLIgnore]

User Author { get; set; }

DateTime CreatedAt { get; set; }

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/interfaces#including-fields)Including fields
---------------------------------------------------------------------------------------------------------------

In the code-first approach we can explicitly include properties of our POCO using the `Field` method on the `IInterfaceTypeDescriptor`. This is only necessary, if the binding behavior of the interface type is explicit.

C#

public class MessageType : InterfaceType<IMessage>

{

protected override void Configure(

IInterfaceTypeDescriptor<IMessage> descriptor)

{

descriptor.BindFieldsExplicitly();

descriptor.Field(f => f.Title);

}

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/interfaces#naming)Naming
-------------------------------------------------------------------------------------------

Unless specified explicitly, Hot Chocolate automatically infers the names of interface types and their fields. Per default the name of the interface / abstract class becomes the name of the interface type. When using `InterfaceType<T>` in code-first, the name of `T` is chosen as the name for the interface type. The names of methods and properties on the respective interface / abstract class are chosen as names of the fields of the interface type

If we need to we can override these inferred names.

The `[GraphQLName]` attribute allows us to specify an explicit name.

C#

[GraphQLName("Post")]

public interface IMessage

{

User Author { get; set; }

[GraphQLName("addedAt")]

DateTime CreatedAt { get; set; }

}

We can also specify a name for the interface type using the `[InterfaceType]` attribute.

C#

[InterfaceType("Post")]

public interface IMessage

This would produce the following `Post` schema interface type:

SDL

interface Post {

author: User!

addedAt: DateTime!

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/interfaces#interfaces-implementing-interfaces)Interfaces implementing interfaces
---------------------------------------------------------------------------------------------------------------------------------------------------

Interfaces can also implement other interfaces.

SDL

interface Message {

author: User

}

interface DatedMessage implements Message {

createdAt: DateTime!

author: User

}

type TextMessage implements DatedMessage & Message {

author: User

createdAt: DateTime!

content: String

}

We can implement this like the following.

C#

[InterfaceType("Message")]

public interface IMessage

{

User Author { get; set; }

}

[InterfaceType("DatedMessage")]

public interface IDatedMessage : IMessage

{

DateTime CreatedAt { get; set; }

}

public class TextMessage : IDatedMessage

{

public User Author { get; set; }

public DateTime CreatedAt { get; set; }

public string Content { get; set; }

}

public class Query

{

public IMessage[] GetMessages()

{

}

}

C#

builder.Services

.AddGraphQLServer()

.AddQueryType<Query>()

.AddType<IDatedMessage>()

.AddType<TextMessage>();

> Note: We also have to register the `DatedMessage` interface manually, if we do not expose it through a field directly:
> 
> 
> 
> C#
> 
> 
> services.AddGraphQLServer().AddType<DatedMessageType>()

Last updated on **2026-02-17** by**Tobias Tengler**
