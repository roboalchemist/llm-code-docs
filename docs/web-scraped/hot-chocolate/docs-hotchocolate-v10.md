# Source: https://chillicream.com/docs/hotchocolate/v10

Title: Introduction - Hot Chocolate v10

URL Source: https://chillicream.com/docs/hotchocolate/v10

Markdown Content:
Hot Chocolate is a .NET GraphQL platform that can help you build a GraphQL layer over your existing and new infrastructure.

Our API will let you start very quickly with pre-built templates that let you start in seconds.

[](https://chillicream.com/docs/hotchocolate/v10#features)Features
------------------------------------------------------------------

Here you will find a list of the most interesting features of Hot Chocolate.

[](https://chillicream.com/docs/hotchocolate/v10#code-first-approach)Code-First approach
----------------------------------------------------------------------------------------

Use your favorite .NET language to define your schema.

> Make sure to add the following usings to your project in order to get the `Execute` extension method: using HotChocolate; using HotChocolate.Execution;

C#

public class Query

{

public string Hello() => "World!";

}

var schema = SchemaBuilder.New()

.AddQueryType<Query>()

.Create();

var executor = schema.MakeExecutable();

Console.WriteLine(executor.Execute("{ hello }").ToJson());

[Learn more](https://chillicream.com/docs/hotchocolate/v10/code-first)

[](https://chillicream.com/docs/hotchocolate/v10#schema-first-approach)Schema-First approach
--------------------------------------------------------------------------------------------

Use the GraphQL schema definition language to define your schema and bind simple methods or whole types to it.

> Make sure to add the following usings to your project in order to get the `Execute` extension method: using HotChocolate; using HotChocolate.Execution;

C#

public class QueryResolver

{

public string Hello() => "World!";

}

var schema = SchemaBuilder.New()

.AddDocumentFromString("type Query { hello: String! }")

.BindResolver<QueryResolver>(c => c

.To("Query")

.Resolve("hello")

.With(r => r.Hello())

)

.Create();

var executor = schema.MakeExecutable();

Console.WriteLine(executor.Execute("{ hello }").ToJson());

[Learn more](https://chillicream.com/docs/hotchocolate/v10/schema-first)

[](https://chillicream.com/docs/hotchocolate/v10#mix-it-all-together)Mix it all together
----------------------------------------------------------------------------------------

With the Hot Chocolate `SchemaBuilder` you can declare types however you want. Define a type schema-first and extend that same type with code-first.

> Make sure to add the following usings to your project in order to get the `Execute` extension method: using HotChocolate; using HotChocolate.Execution;

**What ever makes you happy!**

C#

public class QueryResolver

{

public string Hello() => "World!";

}

public class QueryTypeExtension

: ObjectTypeExtension

{

protected override void Configure(IObjectTypeDescriptor descriptor)

{

descriptor.Name("Query");

descriptor.Field("hello").ResolveWith<QueryResolver>(e=>e.Hello());

}

}

var schema = SchemaBuilder.New()

.AddDocumentFromString("type Query { hello: String! }")

.AddType<QueryTypeExtension>()

.BindResolver<QueryResolver>()

.Create();

var executor = schema.MakeExecutable();

Console.WriteLine(executor.Execute("{ hello foo }").ToJson());

[Learn more](https://chillicream.com/docs/hotchocolate/v10/schema)

[](https://chillicream.com/docs/hotchocolate/v10#support-for-custom-scalars)Support for Custom Scalars
------------------------------------------------------------------------------------------------------

We provide built-in support for GraphQL defined Scalar Types. Moreover, you can also define your own scalar types to make your schemas even richer.

[Learn more](https://chillicream.com/docs/hotchocolate/v10/schema/custom-scalar-types)

[](https://chillicream.com/docs/hotchocolate/v10#support-for-dataloader)Support for DataLoader
----------------------------------------------------------------------------------------------

We have baked-in support for data loaders which makes batching and caching for faster query requests a breeze.

C#

public class PersonResolvers

{

public Task<Person> GetPerson(string id, IResolverContext context, [Service]IPersonRepository repository)

{

return context.BatchDataLoader<string, Person>(

"personByIdBatch",

repository.GetPersonBatchAsync)

.LoadAsync(id);

}

}

[Learn more](https://chillicream.com/docs/hotchocolate/v10/data-fetching)

[](https://chillicream.com/docs/hotchocolate/v10#support-for-custom-directives)Support for Custom Directives
------------------------------------------------------------------------------------------------------------

Implement your own directives and change the execution behavior of your types.

SDL

type Query {

employee(employeeId: String!): Employee

@httpGet(url: "http://someserver/persons/$employeeId")

}

type Employee @json {

name: String

address: String

}

[Learn more](https://chillicream.com/docs/hotchocolate/v10/schema/directives)

Use ASP.NET Core policies on your fields to enable field base authorization.

SDL

type Query {

employee(employeeId: String!): Employee

}

type Employee @authorize(policy: "Everyone") {

name: String

address: String @authorize(policy: "HumanResources")

}

C#

public class QueryType : ObjectType<Query>

{

protected override void Configure(IObjectTypeDescriptor<Query> descriptor)

{

descriptor.Authorize("Everyone");

descriptor.Field(t => t.Hello()).Authorize("HumanResources");

}

}

[Learn more](https://chillicream.com/docs/hotchocolate/v10/security#authorization)

[](https://chillicream.com/docs/hotchocolate/v10#built-in-support-for-filters)Built-in Support for Filters
----------------------------------------------------------------------------------------------------------

We support database filters that offer you rich query capabilities through your GraphQL API.

C#

public class QueryType : ObjectType<Query>

{

protected override void Configure(IObjectTypeDescriptor<Query> descriptor)

{

descriptor.Field(t => t.GetPersons()).UseFiltering();

}

}

GraphQL

query filterPersons {

persons(

where: { OR: [{ name_contains: "foo" }, { name_starts_with: "bar" }] }

) {

name

friends {

name

}

}

}

[Learn more](https://chillicream.com/docs/hotchocolate/v10/data-fetching/filters)

[](https://chillicream.com/docs/hotchocolate/v10#built-in-support-for-relay-paging)Built-in Support for Relay Paging
--------------------------------------------------------------------------------------------------------------------

Our paging support is just plug-and-play :)

C#

public class QueryType : ObjectType<Query>

{

protected override void Configure(IObjectTypeDescriptor<Query> descriptor)

{

descriptor.Field(t => t.GetPersons()).UsePaging<PersonType>();

}

}

GraphQL

query filterPersons {

persons(first: 10) {

edges {

node {

name

}

}

}

}

[Learn more](https://chillicream.com/docs/hotchocolate/v10/data-fetching/pagination)

[](https://chillicream.com/docs/hotchocolate/v10#support-for-graphql-subscriptions)Support for GraphQL Subscriptions
--------------------------------------------------------------------------------------------------------------------

Subscriptions allow GraphQL clients to observe specific events and receive updates from the server in real-time.

[Learn more](https://chillicream.com/docs/hotchocolate/v10/execution-engine/subscriptions)

[](https://chillicream.com/docs/hotchocolate/v10#schema-stitching)Schema Stitching
----------------------------------------------------------------------------------

Schema stitching will give you the capability to build small GraphQL services and stitch them together into one rich schema. This gives you flexibility in your development process and confidence once you are ready to deploy. Update only parts of your schema without the need to deploy always everything.

[Learn more](https://chillicream.com/docs/hotchocolate/v10/stitching)

[](https://chillicream.com/docs/hotchocolate/v10#batching)Batching
------------------------------------------------------------------

Hot Chocolate supports operation and request batching.

`POST /graphql?batchOperations=[StoryComments, NewsFeed]`

GraphQL

query NewsFeed {

feed {

stories {

id @export(as: "ids")

actor

message

}

}

}

query StoryComments {

stories(ids: $ids) {

comments {

actor

message

}

}

}

[Learn more](https://chillicream.com/docs/hotchocolate/v10/execution-engine/batching)

[](https://chillicream.com/docs/hotchocolate/v10#graphql-server)GraphQL Server
------------------------------------------------------------------------------

We support ASP.NET Core and ASP.NET Framework and constantly update these implementations. Hosting our GraphQL server with one of there frameworks is as easy as eating pie :)

Furthermore, you can host Hot Chocolate as an Azure Function or AWS Lambda.

[Learn more](https://chillicream.com/docs/hotchocolate/v10/server)

[](https://chillicream.com/docs/hotchocolate/v10#dotnet-cli-templates)dotnet CLI Templates
------------------------------------------------------------------------------------------

In order to get you even faster started we are providing templates for the dotnet CLI which lets you setup a .NET GraphQL server in less than 10 seconds.

[Learn more](https://chillicream.com/docs/hotchocolate/v10/advanced/dotnet-cli)

[](https://chillicream.com/docs/hotchocolate/v10#we-provide-awesome-tooling-so-you-can-test-your-server)We provide awesome tooling so you can test your server
--------------------------------------------------------------------------------------------------------------------------------------------------------------

[![Image 1: Banana Cake Pop](https://chillicream.com/static/56c756a21181d6e82fd5979b876e06a3/78d47/bcp_6.png)](https://chillicream.com/static/56c756a21181d6e82fd5979b876e06a3/a77a5/bcp_6.png)

[Learn more](https://chillicream.com/products/bananacakepop)

Last updated on **2026-02-17** by**Tobias Tengler**
