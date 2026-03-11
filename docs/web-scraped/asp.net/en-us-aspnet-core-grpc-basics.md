# Source: https://learn.microsoft.com/en-us/aspnet/core/grpc/basics?view=aspnetcore-10.0

Title: gRPC services with C#

URL Source: https://learn.microsoft.com/en-us/aspnet/core/grpc/basics?view=aspnetcore-10.0

Markdown Content:
This document outlines the concepts needed to write [gRPC](https://grpc.io/docs/guides/) apps in C#. The topics covered here apply to both [C-core](https://grpc.io/blog/grpc-stacks)-based and ASP.NET Core-based gRPC apps.

gRPC uses a contract-first approach to API development. Protocol buffers (protobuf) are used as the Interface Definition Language (IDL) by default. The `.proto` file contains:

*   The definition of the gRPC service.
*   The messages sent between clients and servers.

For more information on the syntax of protobuf files, see [Create Protobuf messages for .NET apps](https://learn.microsoft.com/en-us/aspnet/core/grpc/protobuf?view=aspnetcore-10.0).

For example, consider the _greet.proto_ file used in [Get started with gRPC service](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0):

*   Defines a `Greeter` service.
*   The `Greeter` service defines a `SayHello` call.
*   `SayHello` sends a `HelloRequest` message and receives a `HelloReply` message:

```
syntax = "proto3";

option csharp_namespace = "GrpcGreeter";

package greet;

// The greeting service definition.
service Greeter {
  // Sends a greeting
  rpc SayHello (HelloRequest) returns (HelloReply);
}

// The request message containing the user's name.
message HelloRequest {
  string name = 1;
}

// The response message containing the greetings.
message HelloReply {
  string message = 1;
}
```

The `.proto` file is included in a project by adding it to the `<Protobuf>` item group:

```
<ItemGroup>
  <Protobuf Include="Protos\greet.proto" GrpcServices="Server" />
</ItemGroup>
```

By default, a `<Protobuf>` reference generates a concrete client and a service base class. The reference element's `GrpcServices` attribute can be used to limit C# asset generation. Valid `GrpcServices` options are:

*   `Both` (default when not present)
*   `Server`
*   `Client`
*   `None`

The tooling package [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/) is required to generate the C# assets from `.proto` files. The generated assets (files):

*   Are generated on an as-needed basis each time the project is built.
*   Aren't added to the project or checked into source control.
*   Are a build artifact contained in the _obj_ directory.

This package is required by both the server and client projects. The `Grpc.AspNetCore` metapackage includes a reference to `Grpc.Tools`. Server projects can add `Grpc.AspNetCore` using the Package Manager in Visual Studio or by adding a `<PackageReference>` to the project file:

```
<PackageReference Include="Grpc.AspNetCore" Version="2.32.0" />
```

Client projects should directly reference `Grpc.Tools` alongside the other packages required to use the gRPC client. The tooling package isn't required at runtime, so the dependency is marked with `PrivateAssets="All"`:

```
<PackageReference Include="Google.Protobuf" Version="3.18.0" />
<PackageReference Include="Grpc.Net.Client" Version="2.52.0" />
<PackageReference Include="Grpc.Tools" Version="2.40.0">
  <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
  <PrivateAssets>all</PrivateAssets>
</PackageReference>
```

The tooling package generates the C# types representing the messages defined in the included `.proto` files.

For server-side assets, an abstract service base type is generated. The base type contains the definitions of all the gRPC calls contained in the `.proto` file. Create a concrete service implementation that derives from this base type and implements the logic for the gRPC calls. For the `greet.proto`, the example described previously, an abstract `GreeterBase` type that contains a virtual `SayHello` method is generated. A concrete implementation `GreeterService` overrides the method and implements the logic handling the gRPC call.

```
public class GreeterService : Greeter.GreeterBase
{
    private readonly ILogger<GreeterService> _logger;
    public GreeterService(ILogger<GreeterService> logger)
    {
        _logger = logger;
    }

    public override Task<HelloReply> SayHello(HelloRequest request, ServerCallContext context)
    {
        return Task.FromResult(new HelloReply
        {
            Message = "Hello " + request.Name
        });
    }
}
```

For client-side assets, a concrete client type is generated. The gRPC calls in the `.proto` file are translated into methods on the concrete type, which can be called. For the `greet.proto`, the example described previously, a concrete `GreeterClient` type is generated. Call `GreeterClient.SayHelloAsync` to initiate a gRPC call to the server.

```
// The port number must match the port of the gRPC server.
using var channel = GrpcChannel.ForAddress("https://localhost:7042");
var client = new Greeter.GreeterClient(channel);
var reply = await client.SayHelloAsync(
                  new HelloRequest { Name = "GreeterClient" });
Console.WriteLine("Greeting: " + reply.Message);
Console.WriteLine("Press any key to exit...");
Console.ReadKey();
```

By default, server and client assets are generated for each `.proto` file included in the `<Protobuf>` item group. To ensure only the server assets are generated in a server project, the `GrpcServices` attribute is set to `Server`.

```
<ItemGroup>
  <Protobuf Include="Protos\greet.proto" GrpcServices="Server" />
</ItemGroup>
```

Similarly, the attribute is set to `Client` in client projects.

*   [Overview for gRPC on .NET](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0)
*   [Create a .NET gRPC client and server in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0)
*   [gRPC services with ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/grpc/aspnetcore?view=aspnetcore-10.0)
*   [Call gRPC services with the .NET client](https://learn.microsoft.com/en-us/aspnet/core/grpc/client?view=aspnetcore-10.0)

This document outlines the concepts needed to write [gRPC](https://grpc.io/docs/guides/) apps in C#. The topics covered here apply to both [C-core](https://grpc.io/blog/grpc-stacks)-based and ASP.NET Core-based gRPC apps.

gRPC uses a contract-first approach to API development. Protocol buffers (protobuf) are used as the Interface Definition Language (IDL) by default. The `.proto` file contains:

*   The definition of the gRPC service.
*   The messages sent between clients and servers.

For more information on the syntax of protobuf files, see [Create Protobuf messages for .NET apps](https://learn.microsoft.com/en-us/aspnet/core/grpc/protobuf?view=aspnetcore-10.0).

For example, consider the _greet.proto_ file used in [Get started with gRPC service](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0):

*   Defines a `Greeter` service.
*   The `Greeter` service defines a `SayHello` call.
*   `SayHello` sends a `HelloRequest` message and receives a `HelloReply` message:

```
syntax = "proto3";

option csharp_namespace = "GrpcGreeter";

package greet;

// The greeting service definition.
service Greeter {
  // Sends a greeting
  rpc SayHello (HelloRequest) returns (HelloReply);
}

// The request message containing the user's name.
message HelloRequest {
  string name = 1;
}

// The response message containing the greetings.
message HelloReply {
  string message = 1;
}
```

The `.proto` file is included in a project by adding it to the `<Protobuf>` item group:

```
<ItemGroup>
  <Protobuf Include="Protos\greet.proto" GrpcServices="Server" />
</ItemGroup>
```

By default, a `<Protobuf>` reference generates a concrete client and a service base class. The reference element's `GrpcServices` attribute can be used to limit C# asset generation. Valid `GrpcServices` options are:

*   `Both` (default when not present)
*   `Server`
*   `Client`
*   `None`

The tooling package [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/) is required to generate the C# assets from `.proto` files. The generated assets (files):

*   Are generated on an as-needed basis each time the project is built.
*   Aren't added to the project or checked into source control.
*   Are a build artifact contained in the _obj_ directory.

This package is required by both the server and client projects. The `Grpc.AspNetCore` metapackage includes a reference to `Grpc.Tools`. Server projects can add `Grpc.AspNetCore` using the Package Manager in Visual Studio or by adding a `<PackageReference>` to the project file:

```
<PackageReference Include="Grpc.AspNetCore" Version="2.28.0" />
```

Client projects should directly reference `Grpc.Tools` alongside the other packages required to use the gRPC client. The tooling package isn't required at runtime, so the dependency is marked with `PrivateAssets="All"`:

```
<PackageReference Include="Google.Protobuf" Version="3.11.4" />
<PackageReference Include="Grpc.Net.Client" Version="2.52.0" />
<PackageReference Include="Grpc.Tools" Version="2.28.1">
  <PrivateAssets>all</PrivateAssets>
  <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
</PackageReference>
```

The tooling package generates the C# types representing the messages defined in the included `.proto` files.

For server-side assets, an abstract service base type is generated. The base type contains the definitions of all the gRPC calls contained in the `.proto` file. Create a concrete service implementation that derives from this base type and implements the logic for the gRPC calls. For the `greet.proto`, the example described previously, an abstract `GreeterBase` type that contains a virtual `SayHello` method is generated. A concrete implementation `GreeterService` overrides the method and implements the logic handling the gRPC call.

```
public class GreeterService : Greeter.GreeterBase
{
    private readonly ILogger<GreeterService> _logger;
    public GreeterService(ILogger<GreeterService> logger)
    {
        _logger = logger;
    }

    public override Task<HelloReply> SayHello(HelloRequest request, ServerCallContext context)
    {
        return Task.FromResult(new HelloReply
        {
            Message = "Hello " + request.Name
        });
    }
}
```

For client-side assets, a concrete client type is generated. The gRPC calls in the `.proto` file are translated into methods on the concrete type, which can be called. For the `greet.proto`, the example described previously, a concrete `GreeterClient` type is generated. Call `GreeterClient.SayHelloAsync` to initiate a gRPC call to the server.

```
static async Task Main(string[] args)
{
    // The port number(5001) must match the port of the gRPC server.
    using var channel = GrpcChannel.ForAddress("https://localhost:5001");
    var client = new Greeter.GreeterClient(channel);
    var reply = await client.SayHelloAsync(
                      new HelloRequest { Name = "GreeterClient" });
    Console.WriteLine("Greeting: " + reply.Message);
    Console.WriteLine("Press any key to exit...");
    Console.ReadKey();
}
```

By default, server and client assets are generated for each `.proto` file included in the `<Protobuf>` item group. To ensure only the server assets are generated in a server project, the `GrpcServices` attribute is set to `Server`.

```
<ItemGroup>
  <Protobuf Include="Protos\greet.proto" GrpcServices="Server" />
</ItemGroup>
```

Similarly, the attribute is set to `Client` in client projects.

*   [Overview for gRPC on .NET](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0)
*   [Create a .NET gRPC client and server in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0)
*   [gRPC services with ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/grpc/aspnetcore?view=aspnetcore-10.0)
*   [Call gRPC services with the .NET client](https://learn.microsoft.com/en-us/aspnet/core/grpc/client?view=aspnetcore-10.0)
