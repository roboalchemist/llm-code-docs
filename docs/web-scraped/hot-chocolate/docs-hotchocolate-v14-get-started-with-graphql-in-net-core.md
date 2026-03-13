# Source: https://chillicream.com/docs/hotchocolate/v14/get-started-with-graphql-in-net-core

Title: Getting started with GraphQL in .NET Core - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/get-started-with-graphql-in-net-core

Markdown Content:
In this tutorial, we will walk you through the basics of creating a GraphQL server with Hot Chocolate.

[](https://chillicream.com/docs/hotchocolate/v14/get-started-with-graphql-in-net-core#setup)Setup
-------------------------------------------------------------------------------------------------

[](https://chillicream.com/docs/hotchocolate/v14/get-started-with-graphql-in-net-core#install-the-hot-chocolate-templates)Install the Hot Chocolate templates
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Hot Chocolate provides a set of templates that can be used to quickly get started. Run the following command to install the templates:

Bash

dotnet new install HotChocolate.Templates

These templates are kept up to date with the latest .NET and Hot Chocolate features.

[](https://chillicream.com/docs/hotchocolate/v14/get-started-with-graphql-in-net-core#create-a-new-hot-chocolate-graphql-server-project)Create a new Hot Chocolate GraphQL server project
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Once you have installed the templates you can use them to bootstrap your next ASP.NET Core project with Hot Chocolate.

Bash

dotnet new graphql --name GettingStarted

This will create a new directory named `GettingStarted` containing your project's files. You can open the directory or the `GettingStarted.csproj` file in your favorite code editor.

[](https://chillicream.com/docs/hotchocolate/v14/get-started-with-graphql-in-net-core#exploring-the-template-files)Exploring the template files
-----------------------------------------------------------------------------------------------------------------------------------------------

[](https://chillicream.com/docs/hotchocolate/v14/get-started-with-graphql-in-net-core#types)Types
-------------------------------------------------------------------------------------------------

The `Types` directory defines the types that our GraphQL schema should contain. These types and their fields define what consumers can query from our GraphQL API.

We define two object types that we want to expose through our schema.

C#

public record Author(string Name);

C#

public record Book(string Title, Author Author);

> Note: Regular classes may also be used to define object types.

We also define a `Query` type that exposes the types above through a field.

C#

[QueryType]

public static class Query

{

public static Book GetBook()

=> new Book("C# in depth.", new Author("Jon Skeet"));

}

The field in question is named `GetBook`, but the name will be shortened to just `book` in the resulting schema.

The `QueryType` attribute marks a class as an extension of the `query` operation type.

[](https://chillicream.com/docs/hotchocolate/v14/get-started-with-graphql-in-net-core#program)Program
-----------------------------------------------------------------------------------------------------

In the `Program.cs` file, we start by adding the services required by Hot Chocolate to our dependency injection container.

C#

builder.Services

.AddGraphQLServer()

`AddGraphQLServer` returns an `IRequestExecutorBuilder`, which has many extension methods, similar to an `IServiceCollection`, that can be used to configure the GraphQL server.

We then call `AddTypes`, a source-generated extension method that automatically registers all types in the assembly.

> Note: The name of the `AddTypes` method is based on the assembly name by default, but can be set using the `[Module]` assembly attribute, as seen in `ModuleInfo.cs`.

Next, we call `app.MapGraphQL()` to expose our GraphQL server at an endpoint with the default path `/graphql`. Hot Chocolate comes with an ASP.NET Core middleware that is used to serve up the GraphQL server.

Finally, we call `app.RunWithGraphQLCommands(args)` to start the server.

And that is it – you have successfully set up a Hot Chocolate GraphQL server! 🚀

[](https://chillicream.com/docs/hotchocolate/v14/get-started-with-graphql-in-net-core#executing-a-query)Executing a query
-------------------------------------------------------------------------------------------------------------------------

First off we have to run the project.

Bash

dotnet run --no-hot-reload

If you have set everything up correctly, you should be able to open [http://localhost:5095/graphql](http://localhost:5095/graphql) in your browser and be greeted by our GraphQL IDE [Nitro](https://chillicream.com/products/nitro).

[![Image 1: GraphQL IDE](https://chillicream.com/static/e934ecd00b4d37a09724b344debba6c6/cf465/getting-started-nitro.webp)](https://chillicream.com/static/e934ecd00b4d37a09724b344debba6c6/548e7/getting-started-nitro.webp)

Next, click on `Create Document`. You will be presented with a settings dialog for this new tab, pictured below. Make sure the `HTTP Endpoint` input field has the correct URL under which your GraphQL endpoint is available. If it is correct you can just go ahead and click the `Apply` button.

[![Image 2: GraphQL IDE: Setup](https://chillicream.com/static/795e1ece38ccb8a33192d106c41b9c58/cf465/getting-started-nitro-setup.webp)](https://chillicream.com/static/795e1ece38ccb8a33192d106c41b9c58/dbf17/getting-started-nitro-setup.webp)

Now you should be seeing an editor like the one pictured below. If your GraphQL server has been correctly set up you should see `Schema available` at the bottom right of the editor.

[![Image 3: GraphQL IDE: Editor](https://chillicream.com/static/900c505b9e6498f61b5327d4e1c4fa7d/cf465/getting-started-nitro-editor.webp)](https://chillicream.com/static/900c505b9e6498f61b5327d4e1c4fa7d/548e7/getting-started-nitro-editor.webp)

The view is split into five panes.

1.   `Builder`
    *   This is where you build operations with a visual editor.

2.   `Request`
    *   This is where you enter operations that you wish to send to the GraphQL server.

3.   `Response`
    *   This is where results will be displayed.

4.   `GraphQL Variables / HTTP Headers`
    *   This is where you modify variables and headers.

5.   `Responses`
    *   This is where you view recent queries.

Let's send a query to your GraphQL server. Paste the below query into the `Request` pane of the editor:

GraphQL

{

book {

title

author {

name

}

}

}

To execute the query, simply press the `Run` button. The result should be displayed as JSON in the `Response` pane as shown below:

[![Image 4: GraphQL IDE: Executing a query](https://chillicream.com/static/516362ad16242530dd0c63aa5d7332c0/cf465/getting-started-nitro-query.webp)](https://chillicream.com/static/516362ad16242530dd0c63aa5d7332c0/548e7/getting-started-nitro-query.webp)

You can also view and browse the schema from within Nitro. Click on the `Schema Reference` tab next to `Operation` in order to browse the schema. There's also a `Schema Definition` tab, pictured below, which shows the schema using the raw SDL (Schema Definition Language).

[![Image 5: GraphQL IDE: Schema](https://chillicream.com/static/c7b4219068ae1a5c08cf88f32ac0ab07/cf465/getting-started-nitro-schema.webp)](https://chillicream.com/static/c7b4219068ae1a5c08cf88f32ac0ab07/548e7/getting-started-nitro-schema.webp)

Congratulations, you've built your first Hot Chocolate GraphQL server and sent a query using the Nitro GraphQL IDE. 🎉🚀

[](https://chillicream.com/docs/hotchocolate/v14/get-started-with-graphql-in-net-core#additional-resources)Additional resources
-------------------------------------------------------------------------------------------------------------------------------

Now that you've set up a basic GraphQL server, what should your next steps be?

If this is your first time using GraphQL, we recommend [this guide](https://graphql.org/learn/) that walks you through the basic concepts of GraphQL.

If you want to get an overview of Hot Chocolate's features, we recommend reading the _Overview_ pages in each section of the documentation. They can be found in the sidebar to your left.

For a guided tutorial that explains how you can set up your GraphQL server beyond this basic example, check out [our workshop](https://github.com/ChilliCream/graphql-workshop). Here we will dive deeper into several topics around Hot Chocolate and GraphQL in general.

You can also jump straight into our documentation and learn more about [Defining a GraphQL schema](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema).

Last updated on **2026-02-17** by**Tobias Tengler**
