# Source: https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0

Title: Create a .NET gRPC client and server in ASP.NET Core

URL Source: https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0

Published Time: Tue, 03 Feb 2026 23:31:00 GMT

Markdown Content:
This tutorial shows how to create a .NET [gRPC](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0) client and an ASP.NET Core gRPC Server. At the end, you'll have a gRPC client that communicates with the gRPC Greeter service.

In this tutorial, you:

*   Create a gRPC Server.
*   Create a gRPC client.
*   Test the gRPC client with the gRPC Greeter service.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   [The latest version of Visual Studio](https://visualstudio.microsoft.com/downloads/) with the **ASP.NET and web development** workload.

[![Image 1: VS26 installer workloads](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev-2026.png?view=aspnetcore-10.0)](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev-2026.png?view=aspnetcore-10.0#lightbox)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)

*   Start Visual Studio and select **Create a new Project**.
*   In the **Create a new project** dialog, search for `gRPC`. Select **ASP.NET Core gRPC Service** and select **Next**.
*   In the **Configure your new project** dialog, enter `GrpcGreeter` for **Project name**. It's important to name the project _GrpcGreeter_ so the namespaces match when you copy and paste code.
*   Select **Next**.
*   In the **Additional information** dialog, select **.NET 10.0 (Long Term Support)** and then select **Create**.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   Press Ctrl+F5 to run without the debugger.

Visual Studio displays the following dialog:

![Image 2: This project is configured to use SSL. To avoid SSL warnings in the browser you can choose to trust the self-signed certificate that IIS Express has generated. Would you like to trust the IIS Express SSL certificate?](https://learn.microsoft.com/en-us/aspnet/core/static/trustcertvs26.png?view=aspnetcore-10.0)

Select **Yes** if you trust the IIS Express SSL certificate.

The following dialog is displayed:

![Image 3: Security warning dialog](https://learn.microsoft.com/en-us/aspnet/core/static/certvs26.png?view=aspnetcore-10.0)

Select **Yes** if you agree to trust the development certificate.

For information on trusting the Firefox browser, see [Firefox SEC_ERROR_INADEQUATE_KEY_USAGE certificate error](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff).

Visual Studio:

    *   Starts [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/?view=aspnetcore-10.0#kestrel) server.
    *   Launches a browser.
    *   Navigates to `http://localhost:port`, such as `http://localhost:7042`. 
        *   _port_: A randomly assigned port number for the app.
        *   `localhost`: The standard hostname for the local computer. Localhost only serves web requests from the local computer.

The logs show the service listening on `https://localhost:<port>`, where `<port>` is the localhost port number randomly assigned when the project is created and set in `Properties/launchSettings.json`.

```
info: Microsoft.Hosting.Lifetime[0]
      Now listening on: https://localhost:<port>
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Development
```

Note

The gRPC template is configured to use [Transport Layer Security (TLS)](https://tools.ietf.org/html/rfc5246). gRPC clients need to use HTTPS to call the server. The gRPC service localhost port number is randomly assigned when the project is created and set in the _Properties\launchSettings.json_ file of the gRPC service project.

_GrpcGreeter_ project files:

*   `Protos/greet.proto`: defines the `Greeter` gRPC and is used to generate the gRPC server assets. For more information, see [Introduction to gRPC](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0).
*   `Services` folder: Contains the implementation of the `Greeter` service.
*   `appsettings.json`: Contains configuration data such as the protocol used by Kestrel. For more information, see [Configuration in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0).
*   `Program.cs`, which contains: 
    *   The entry point for the gRPC service. For more information, see [.NET Generic Host in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0).
    *   Code that configures app behavior. For more information, see [App startup](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/startup?view=aspnetcore-10.0).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)

*   Open a second instance of Visual Studio and select **Create a new project**.
*   In the **Create a new project** dialog, select **Console App**, and select **Next**.
*   In the **Project name** text box, enter **GrpcGreeterClient** and select **Next**.
*   In the **Additional information** dialog, select **.NET 10.0 (Long Term Support)** and then select **Create**.

The gRPC client project requires the following NuGet packages:

*   [Grpc.Net.Client](https://www.nuget.org/packages/Grpc.Net.Client), which contains the .NET client.
*   [Google.Protobuf](https://www.nuget.org/packages/Google.Protobuf/), which contains protobuf message APIs for C#.
*   [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/), which contain C# tooling support for protobuf files. The tooling package isn't required at runtime, so the dependency is marked with `PrivateAssets="All"`.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_4_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_4_visual-studio-code)

Install the packages using either the Package Manager Console (PMC) or Manage NuGet Packages.

*   From Visual Studio, select **Tools**>**NuGet Package Manager**>**Package Manager Console**

*   From the **Package Manager Console** window, run `cd GrpcGreeterClient` to change directories to the folder containing the `GrpcGreeterClient.csproj` files.

*   Run the following commands:

```
Install-Package Grpc.Net.Client
Install-Package Google.Protobuf
Install-Package Grpc.Tools
```

*   Right-click the project in **Solution Explorer**>**Manage NuGet Packages**.
*   Select the **Browse** tab.
*   Enter **Grpc.Net.Client** in the search box.
*   Select the **Grpc.Net.Client** package from the **Browse** tab and select **Install**.
*   Repeat for `Google.Protobuf` and `Grpc.Tools`.

*   Create a _Protos_ folder in the gRPC client project.

*   Copy the _Protos\greet.proto_ file from the gRPC Greeter service to the _Protos_ folder in the gRPC client project.

*   Update the namespace inside the `greet.proto` file to the project's namespace:

```
option csharp_namespace = "GrpcGreeterClient";
```
*   Edit the `GrpcGreeterClient.csproj` project file:

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_5_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_5_visual-studio-code)

Right-click the project and select **Edit Project File**.

*   Add an item group with a `<Protobuf>` element that refers to the _greet.proto_ file:

```
<ItemGroup>
  <Protobuf Include="Protos\greet.proto" GrpcServices="Client" />
</ItemGroup>
```

*   Build the client project to create the types in the `GrpcGreeterClient` namespace.

Note

The `GrpcGreeterClient` types are generated automatically by the build process. The tooling package [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/) generates the following files based on the _greet.proto_ file:

*   `GrpcGreeterClient\obj\Debug\[TARGET_FRAMEWORK]\Protos\Greet.cs`: The protocol buffer code which populates, serializes and retrieves the request and response message types.
*   `GrpcGreeterClient\obj\Debug\[TARGET_FRAMEWORK]\Protos\GreetGrpc.cs`: Contains the generated client classes.

For more information on the C# assets automatically generated by [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/), see [gRPC services with C#: Generated C# assets](https://learn.microsoft.com/en-us/aspnet/core/grpc/basics?view=aspnetcore-10.0#generated-c-assets).

*   Update the gRPC client `Program.cs` file with the following code.

```
using Grpc.Net.Client;
using GrpcGreeterClient;

// The port number must match the port of the gRPC server.
using var channel = GrpcChannel.ForAddress("https://localhost:7042");
var client = new Greeter.GreeterClient(channel);
var reply = await client.SayHelloAsync(
    new HelloRequest { Name = "GreeterClient" });
Console.WriteLine("Greeting: " + reply.Message);
Console.WriteLine("Press any key to exit...");
Console.ReadKey();
```
*   In the preceding highlighted code, replace the localhost port number `7042` with the `HTTPS` port number specified in `Properties/launchSettings.json` within the `GrpcGreeter` service project.

`Program.cs` contains the entry point and logic for the gRPC client.

The Greeter client is created by:

*   Instantiating a `GrpcChannel` containing the information for creating the connection to the gRPC service.
*   Using the `GrpcChannel` to construct the Greeter client:

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

The Greeter client calls the asynchronous `SayHello` method. The result of the `SayHello` call is displayed:

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

Update the `appsettings.Development.json` file by adding the following highlighted lines:

```
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning",
      "Microsoft.AspNetCore.Hosting": "Information",
      "Microsoft.AspNetCore.Routing.EndpointMiddleware": "Information"
    }
  }
}
```

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_6_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_6_visual-studio-code)

*   In the `GrpcGreeter` service project, press `Ctrl+F5` to start the server without the debugger.
*   In the `GrpcGreeterClient` console project, press `Ctrl+F5` to start the client without the debugger.

The client sends a greeting to the service with a message containing its name, _GreeterClient_. The service sends the message "Hello GreeterClient" as a response. The "Hello GreeterClient" response is displayed in the command prompt:

```
Greeting: Hello GreeterClient
Press any key to exit...
```

The gRPC service records the details of the successful call in the logs written to the command prompt:

```
info: Microsoft.Hosting.Lifetime[0]
      Now listening on: https://localhost:<port>
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Development
info: Microsoft.Hosting.Lifetime[0]
      Content root path: C:\GH\aspnet\docs\4\Docs\aspnetcore\tutorials\grpc\grpc-start\sample\GrpcGreeter
info: Microsoft.AspNetCore.Hosting.Diagnostics[1]
      Request starting HTTP/2 POST https://localhost:<port>/greet.Greeter/SayHello application/grpc
info: Microsoft.AspNetCore.Routing.EndpointMiddleware[0]
      Executing endpoint 'gRPC - /greet.Greeter/SayHello'
info: Microsoft.AspNetCore.Routing.EndpointMiddleware[1]
      Executed endpoint 'gRPC - /greet.Greeter/SayHello'
info: Microsoft.AspNetCore.Hosting.Diagnostics[2]
      Request finished HTTP/2 POST https://localhost:7042/greet.Greeter/SayHello - 200 - application/grpc 40.4615ms
```

Note

The code in this article requires the ASP.NET Core HTTPS development certificate to secure the gRPC service. If the .NET gRPC client fails with the message `The remote certificate is invalid according to the validation procedure.` or `The SSL connection could not be established.`, the development certificate isn't trusted. To fix this issue, see [Call a gRPC service with an untrusted/invalid certificate](https://learn.microsoft.com/en-us/aspnet/core/grpc/troubleshoot?view=aspnetcore-10.0#call-a-grpc-service-with-an-untrustedinvalid-certificate).

*   View or download [the completed sample code for this tutorial](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/grpc/grpc-start/sample) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample)).
*   [Overview for gRPC on .NET](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0)
*   [gRPC services with C#](https://learn.microsoft.com/en-us/aspnet/core/grpc/basics?view=aspnetcore-10.0)
*   [Migrate gRPC from C-core to gRPC for .NET](https://learn.microsoft.com/en-us/aspnet/core/grpc/migration?view=aspnetcore-10.0)

This tutorial shows how to create a .NET [gRPC](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0) client and an ASP.NET Core gRPC Server. At the end, you'll have a gRPC client that communicates with the gRPC Greeter service.

In this tutorial, you:

*   Create a gRPC Server.
*   Create a gRPC client.
*   Test the gRPC client with the gRPC Greeter service.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) with the **ASP.NET and web development** workload.

![Image 4: VS22 installer workloads](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)

*   Start Visual Studio 2022 and select **New Project**.
*   In the **Create a new project** dialog, search for `gRPC`. Select **ASP.NET Core gRPC Service** and select **Next**.
*   In the **Configure your new project** dialog, enter `GrpcGreeter` for **Project name**. It's important to name the project _GrpcGreeter_ so the namespaces match when you copy and paste code.
*   Select **Next**.
*   In the **Additional information** dialog, select **.NET 9.0 (Standard Term Support)** and then select **Create**.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   Press Ctrl+F5 to run without the debugger.

Visual Studio displays the following dialog when a project is not yet configured to use SSL:

![Image 5: This project is configured to use SSL. To avoid SSL warnings in the browser you can choose to trust the self-signed certificate that IIS Express has generated. Would you like to trust the IIS Express SSL certificate?](https://learn.microsoft.com/en-us/aspnet/core/static/trustcert.png?view=aspnetcore-10.0)

Select **Yes** if you trust the IIS Express SSL certificate.

The following dialog is displayed:

![Image 6: Security warning dialog](https://learn.microsoft.com/en-us/aspnet/core/static/cert.png?view=aspnetcore-10.0)

Select **Yes** if you agree to trust the development certificate.

For information on trusting the Firefox browser, see [Firefox SEC_ERROR_INADEQUATE_KEY_USAGE certificate error](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff).

Visual Studio:

    *   Starts [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/?view=aspnetcore-10.0#kestrel) server.
    *   Launches a browser.
    *   Navigates to `http://localhost:port`, such as `http://localhost:7042`. 
        *   _port_: A randomly assigned port number for the app.
        *   `localhost`: The standard hostname for the local computer. Localhost only serves web requests from the local computer.

The logs show the service listening on `https://localhost:<port>`, where `<port>` is the localhost port number randomly assigned when the project is created and set in `Properties/launchSettings.json`.

```
info: Microsoft.Hosting.Lifetime[0]
      Now listening on: https://localhost:<port>
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Development
```

Note

The gRPC template is configured to use [Transport Layer Security (TLS)](https://tools.ietf.org/html/rfc5246). gRPC clients need to use HTTPS to call the server. The gRPC service localhost port number is randomly assigned when the project is created and set in the _Properties\launchSettings.json_ file of the gRPC service project.

_GrpcGreeter_ project files:

*   `Protos/greet.proto`: defines the `Greeter` gRPC and is used to generate the gRPC server assets. For more information, see [Introduction to gRPC](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0).
*   `Services` folder: Contains the implementation of the `Greeter` service.
*   `appsettings.json`: Contains configuration data such as the protocol used by Kestrel. For more information, see [Configuration in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0).
*   `Program.cs`, which contains: 
    *   The entry point for the gRPC service. For more information, see [.NET Generic Host in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0).
    *   Code that configures app behavior. For more information, see [App startup](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/startup?view=aspnetcore-10.0).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)

*   Open a second instance of Visual Studio and select **New Project**.
*   In the **Create a new project** dialog, select **Console App**, and select **Next**.
*   In the **Project name** text box, enter **GrpcGreeterClient** and select **Next**.
*   In the **Additional information** dialog, select **.NET 9.0 (Standard Term Support)** and then select **Create**.

The gRPC client project requires the following NuGet packages:

*   [Grpc.Net.Client](https://www.nuget.org/packages/Grpc.Net.Client), which contains the .NET client.
*   [Google.Protobuf](https://www.nuget.org/packages/Google.Protobuf/), which contains protobuf message APIs for C#.
*   [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/), which contain C# tooling support for protobuf files. The tooling package isn't required at runtime, so the dependency is marked with `PrivateAssets="All"`.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_4_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_4_visual-studio-code)

Install the packages using either the Package Manager Console (PMC) or Manage NuGet Packages.

*   From Visual Studio, select **Tools**>**NuGet Package Manager**>**Package Manager Console**

*   From the **Package Manager Console** window, run `cd GrpcGreeterClient` to change directories to the folder containing the `GrpcGreeterClient.csproj` files.

*   Run the following commands:

```
Install-Package Grpc.Net.Client
Install-Package Google.Protobuf
Install-Package Grpc.Tools
```

*   Right-click the project in **Solution Explorer**>**Manage NuGet Packages**.
*   Select the **Browse** tab.
*   Enter **Grpc.Net.Client** in the search box.
*   Select the **Grpc.Net.Client** package from the **Browse** tab and select **Install**.
*   Repeat for `Google.Protobuf` and `Grpc.Tools`.

*   Create a _Protos_ folder in the gRPC client project.

*   Copy the _Protos\greet.proto_ file from the gRPC Greeter service to the _Protos_ folder in the gRPC client project.

*   Update the namespace inside the `greet.proto` file to the project's namespace:

```
option csharp_namespace = "GrpcGreeterClient";
```
*   Edit the `GrpcGreeterClient.csproj` project file:

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_5_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_5_visual-studio-code)

Right-click the project and select **Edit Project File**.

*   Add an item group with a `<Protobuf>` element that refers to the _greet.proto_ file:

```
<ItemGroup>
  <Protobuf Include="Protos\greet.proto" GrpcServices="Client" />
</ItemGroup>
```

*   Build the client project to create the types in the `GrpcGreeterClient` namespace.

Note

The `GrpcGreeterClient` types are generated automatically by the build process. The tooling package [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/) generates the following files based on the _greet.proto_ file:

*   `GrpcGreeterClient\obj\Debug\[TARGET_FRAMEWORK]\Protos\Greet.cs`: The protocol buffer code which populates, serializes and retrieves the request and response message types.
*   `GrpcGreeterClient\obj\Debug\[TARGET_FRAMEWORK]\Protos\GreetGrpc.cs`: Contains the generated client classes.

For more information on the C# assets automatically generated by [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/), see [gRPC services with C#: Generated C# assets](https://learn.microsoft.com/en-us/aspnet/core/grpc/basics?view=aspnetcore-10.0#generated-c-assets).

*   Update the gRPC client `Program.cs` file with the following code.

```
using Grpc.Net.Client;
using GrpcGreeterClient;

// The port number must match the port of the gRPC server.
using var channel = GrpcChannel.ForAddress("https://localhost:7042");
var client = new Greeter.GreeterClient(channel);
var reply = await client.SayHelloAsync(
    new HelloRequest { Name = "GreeterClient" });
Console.WriteLine("Greeting: " + reply.Message);
Console.WriteLine("Press any key to exit...");
Console.ReadKey();
```
*   In the preceding highlighted code, replace the localhost port number `7042` with the `HTTPS` port number specified in `Properties/launchSettings.json` within the `GrpcGreeter` service project.

`Program.cs` contains the entry point and logic for the gRPC client.

The Greeter client is created by:

*   Instantiating a `GrpcChannel` containing the information for creating the connection to the gRPC service.
*   Using the `GrpcChannel` to construct the Greeter client:

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

The Greeter client calls the asynchronous `SayHello` method. The result of the `SayHello` call is displayed:

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

Update the `appsettings.Development.json` file by adding the following highlighted lines:

```
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning",
      "Microsoft.AspNetCore.Hosting": "Information",
      "Microsoft.AspNetCore.Routing.EndpointMiddleware": "Information"
    }
  }
}
```

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_6_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_6_visual-studio-code)

*   In the `GrpcGreeter` service project, press `Ctrl+F5` to start the server without the debugger.
*   In the `GrpcGreeterClient` console project, press `Ctrl+F5` to start the client without the debugger.

The client sends a greeting to the service with a message containing its name, _GreeterClient_. The service sends the message "Hello GreeterClient" as a response. The "Hello GreeterClient" response is displayed in the command prompt:

```
Greeting: Hello GreeterClient
Press any key to exit...
```

The gRPC service records the details of the successful call in the logs written to the command prompt:

```
info: Microsoft.Hosting.Lifetime[0]
      Now listening on: https://localhost:<port>
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Development
info: Microsoft.Hosting.Lifetime[0]
      Content root path: C:\GH\aspnet\docs\4\Docs\aspnetcore\tutorials\grpc\grpc-start\sample\GrpcGreeter
info: Microsoft.AspNetCore.Hosting.Diagnostics[1]
      Request starting HTTP/2 POST https://localhost:<port>/greet.Greeter/SayHello application/grpc
info: Microsoft.AspNetCore.Routing.EndpointMiddleware[0]
      Executing endpoint 'gRPC - /greet.Greeter/SayHello'
info: Microsoft.AspNetCore.Routing.EndpointMiddleware[1]
      Executed endpoint 'gRPC - /greet.Greeter/SayHello'
info: Microsoft.AspNetCore.Hosting.Diagnostics[2]
      Request finished HTTP/2 POST https://localhost:7042/greet.Greeter/SayHello - 200 - application/grpc 40.4615ms
```

Note

The code in this article requires the ASP.NET Core HTTPS development certificate to secure the gRPC service. If the .NET gRPC client fails with the message `The remote certificate is invalid according to the validation procedure.` or `The SSL connection could not be established.`, the development certificate isn't trusted. To fix this issue, see [Call a gRPC service with an untrusted/invalid certificate](https://learn.microsoft.com/en-us/aspnet/core/grpc/troubleshoot?view=aspnetcore-10.0#call-a-grpc-service-with-an-untrustedinvalid-certificate).

*   View or download [the completed sample code for this tutorial](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/grpc/grpc-start/sample) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample)).
*   [Overview for gRPC on .NET](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0)
*   [gRPC services with C#](https://learn.microsoft.com/en-us/aspnet/core/grpc/basics?view=aspnetcore-10.0)
*   [Migrate gRPC from C-core to gRPC for .NET](https://learn.microsoft.com/en-us/aspnet/core/grpc/migration?view=aspnetcore-10.0)

This tutorial shows how to create a .NET [gRPC](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0) client and an ASP.NET Core gRPC Server. At the end, you'll have a gRPC client that communicates with the gRPC Greeter service.

In this tutorial, you:

*   Create a gRPC Server.
*   Create a gRPC client.
*   Test the gRPC client with the gRPC Greeter service.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) with the **ASP.NET and web development** workload.

![Image 7: VS22 installer workloads](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)

*   Start Visual Studio 2022 and select **New Project**.
*   In the **Create a new project** dialog, search for `gRPC`. Select **ASP.NET Core gRPC Service** and select **Next**.
*   In the **Configure your new project** dialog, enter `GrpcGreeter` for **Project name**. It's important to name the project _GrpcGreeter_ so the namespaces match when you copy and paste code.
*   Select **Next**.
*   In the **Additional information** dialog, select **.NET 8.0 (Long Term Support)** and then select **Create**.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   Press Ctrl+F5 to run without the debugger.

Visual Studio displays the following dialog when a project is not yet configured to use SSL:

![Image 8: This project is configured to use SSL. To avoid SSL warnings in the browser you can choose to trust the self-signed certificate that IIS Express has generated. Would you like to trust the IIS Express SSL certificate?](https://learn.microsoft.com/en-us/aspnet/core/static/trustcert.png?view=aspnetcore-10.0)

Select **Yes** if you trust the IIS Express SSL certificate.

The following dialog is displayed:

![Image 9: Security warning dialog](https://learn.microsoft.com/en-us/aspnet/core/static/cert.png?view=aspnetcore-10.0)

Select **Yes** if you agree to trust the development certificate.

For information on trusting the Firefox browser, see [Firefox SEC_ERROR_INADEQUATE_KEY_USAGE certificate error](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff).

Visual Studio:

    *   Starts [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/?view=aspnetcore-10.0#kestrel) server.
    *   Launches a browser.
    *   Navigates to `http://localhost:port`, such as `http://localhost:7042`. 
        *   _port_: A randomly assigned port number for the app.
        *   `localhost`: The standard hostname for the local computer. Localhost only serves web requests from the local computer.

The logs show the service listening on `https://localhost:<port>`, where `<port>` is the localhost port number randomly assigned when the project is created and set in `Properties/launchSettings.json`.

```
info: Microsoft.Hosting.Lifetime[0]
      Now listening on: https://localhost:<port>
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Development
```

Note

The gRPC template is configured to use [Transport Layer Security (TLS)](https://tools.ietf.org/html/rfc5246). gRPC clients need to use HTTPS to call the server. The gRPC service localhost port number is randomly assigned when the project is created and set in the _Properties\launchSettings.json_ file of the gRPC service project.

_GrpcGreeter_ project files:

*   `Protos/greet.proto`: defines the `Greeter` gRPC and is used to generate the gRPC server assets. For more information, see [Introduction to gRPC](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0).
*   `Services` folder: Contains the implementation of the `Greeter` service.
*   `appSettings.json`: Contains configuration data such as the protocol used by Kestrel. For more information, see [Configuration in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0).
*   `Program.cs`, which contains: 
    *   The entry point for the gRPC service. For more information, see [.NET Generic Host in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0).
    *   Code that configures app behavior. For more information, see [App startup](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/startup?view=aspnetcore-10.0).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)

*   Open a second instance of Visual Studio and select **New Project**.
*   In the **Create a new project** dialog, select **Console App**, and select **Next**.
*   In the **Project name** text box, enter **GrpcGreeterClient** and select **Next**.
*   In the **Additional information** dialog, select **.NET 8.0 (Long Term Support)** and then select **Create**.

The gRPC client project requires the following NuGet packages:

*   [Grpc.Net.Client](https://www.nuget.org/packages/Grpc.Net.Client), which contains the .NET client.
*   [Google.Protobuf](https://www.nuget.org/packages/Google.Protobuf/), which contains protobuf message APIs for C#.
*   [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/), which contain C# tooling support for protobuf files. The tooling package isn't required at runtime, so the dependency is marked with `PrivateAssets="All"`.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_4_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_4_visual-studio-code)

Install the packages using either the Package Manager Console (PMC) or Manage NuGet Packages.

*   From Visual Studio, select **Tools**>**NuGet Package Manager**>**Package Manager Console**

*   From the **Package Manager Console** window, run `cd GrpcGreeterClient` to change directories to the folder containing the `GrpcGreeterClient.csproj` files.

*   Run the following commands:

```
Install-Package Grpc.Net.Client
Install-Package Google.Protobuf
Install-Package Grpc.Tools
```

*   Right-click the project in **Solution Explorer**>**Manage NuGet Packages**.
*   Select the **Browse** tab.
*   Enter **Grpc.Net.Client** in the search box.
*   Select the **Grpc.Net.Client** package from the **Browse** tab and select **Install**.
*   Repeat for `Google.Protobuf` and `Grpc.Tools`.

*   Create a _Protos_ folder in the gRPC client project.

*   Copy the _Protos\greet.proto_ file from the gRPC Greeter service to the _Protos_ folder in the gRPC client project.

*   Update the namespace inside the `greet.proto` file to the project's namespace:

```
option csharp_namespace = "GrpcGreeterClient";
```
*   Edit the `GrpcGreeterClient.csproj` project file:

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_5_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_5_visual-studio-code)

Right-click the project and select **Edit Project File**.

*   Add an item group with a `<Protobuf>` element that refers to the _greet.proto_ file:

```
<ItemGroup>
  <Protobuf Include="Protos\greet.proto" GrpcServices="Client" />
</ItemGroup>
```

*   Build the client project to create the types in the `GrpcGreeterClient` namespace.

Note

The `GrpcGreeterClient` types are generated automatically by the build process. The tooling package [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/) generates the following files based on the _greet.proto_ file:

*   `GrpcGreeterClient\obj\Debug\[TARGET_FRAMEWORK]\Protos\Greet.cs`: The protocol buffer code which populates, serializes and retrieves the request and response message types.
*   `GrpcGreeterClient\obj\Debug\[TARGET_FRAMEWORK]\Protos\GreetGrpc.cs`: Contains the generated client classes.

For more information on the C# assets automatically generated by [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/), see [gRPC services with C#: Generated C# assets](https://learn.microsoft.com/en-us/aspnet/core/grpc/basics?view=aspnetcore-10.0#generated-c-assets).

*   Update the gRPC client `Program.cs` file with the following code.

```
using System.Threading.Tasks;
using Grpc.Net.Client;
using GrpcGreeterClient;

// The port number must match the port of the gRPC server.
using var channel = GrpcChannel.ForAddress("https://localhost:7042");
var client = new Greeter.GreeterClient(channel);
var reply = await client.SayHelloAsync(
                  new HelloRequest { Name = "GreeterClient" });
Console.WriteLine("Greeting: " + reply.Message);
Console.WriteLine("Press any key to exit...");
Console.ReadKey();
```
*   In the preceding highlighted code, replace the localhost port number `7042` with the `HTTPS` port number specified in `Properties/launchSettings.json` within the `GrpcGreeter` service project.

`Program.cs` contains the entry point and logic for the gRPC client.

The Greeter client is created by:

*   Instantiating a `GrpcChannel` containing the information for creating the connection to the gRPC service.
*   Using the `GrpcChannel` to construct the Greeter client:

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

The Greeter client calls the asynchronous `SayHello` method. The result of the `SayHello` call is displayed:

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

Update the `appsettings.Development.json` file by adding the following highlighted lines:

```
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
      ,"Microsoft.AspNetCore.Hosting": "Information",
      "Microsoft.AspNetCore.Routing.EndpointMiddleware": "Information"
    }
  }
}
```

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_6_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_6_visual-studio-code)

*   In the Greeter service, press `Ctrl+F5` to start the server without the debugger.
*   In the `GrpcGreeterClient` project, press `Ctrl+F5` to start the client without the debugger.

The client sends a greeting to the service with a message containing its name, _GreeterClient_. The service sends the message "Hello GreeterClient" as a response. The "Hello GreeterClient" response is displayed in the command prompt:

```
Greeting: Hello GreeterClient
Press any key to exit...
```

The gRPC service records the details of the successful call in the logs written to the command prompt:

```
info: Microsoft.Hosting.Lifetime[0]
      Now listening on: https://localhost:<port>
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Development
info: Microsoft.Hosting.Lifetime[0]
      Content root path: C:\GH\aspnet\docs\4\Docs\aspnetcore\tutorials\grpc\grpc-start\sample\GrpcGreeter
info: Microsoft.AspNetCore.Hosting.Diagnostics[1]
      Request starting HTTP/2 POST https://localhost:<port>/Greet.Greeter/SayHello application/grpc
info: Microsoft.AspNetCore.Routing.EndpointMiddleware[0]
      Executing endpoint 'gRPC - /Greet.Greeter/SayHello'
info: Microsoft.AspNetCore.Routing.EndpointMiddleware[1]
      Executed endpoint 'gRPC - /Greet.Greeter/SayHello'
info: Microsoft.AspNetCore.Hosting.Diagnostics[2]
      Request finished in 78.32260000000001ms 200 application/grpc
```

Note

The code in this article requires the ASP.NET Core HTTPS development certificate to secure the gRPC service. If the .NET gRPC client fails with the message `The remote certificate is invalid according to the validation procedure.` or `The SSL connection could not be established.`, the development certificate isn't trusted. To fix this issue, see [Call a gRPC service with an untrusted/invalid certificate](https://learn.microsoft.com/en-us/aspnet/core/grpc/troubleshoot?view=aspnetcore-10.0#call-a-grpc-service-with-an-untrustedinvalid-certificate).

*   View or download [the completed sample code for this tutorial](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/grpc/grpc-start/sample) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample)).
*   [Overview for gRPC on .NET](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0)
*   [gRPC services with C#](https://learn.microsoft.com/en-us/aspnet/core/grpc/basics?view=aspnetcore-10.0)
*   [Migrate gRPC from C-core to gRPC for .NET](https://learn.microsoft.com/en-us/aspnet/core/grpc/migration?view=aspnetcore-10.0)

This tutorial shows how to create a .NET [gRPC](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0) client and an ASP.NET Core gRPC Server. At the end, you'll have a gRPC client that communicates with the gRPC Greeter service.

In this tutorial, you:

*   Create a gRPC Server.
*   Create a gRPC client.
*   Test the gRPC client with the gRPC Greeter service.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   [Visual Studio 2022](https://visualstudio.microsoft.com/vs/#download) with the **ASP.NET and web development** workload.

![Image 10: VS22 installer workloads](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-mac)

*   Start Visual Studio 2022 and select **Create a new project**.
*   In the **Create a new project** dialog, search for `gRPC`. Select **ASP.NET Core gRPC Service** and select **Next**.
*   In the **Configure your new project** dialog, enter `GrpcGreeter` for **Project name**. It's important to name the project _GrpcGreeter_ so the namespaces match when you copy and paste code.
*   Select **Next**.
*   In the **Additional information** dialog, select **.NET 6.0 (Long-term support)** and then select **Create**.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   Press Ctrl+F5 to run without the debugger.

Visual Studio displays the following dialog when a project is not yet configured to use SSL:

![Image 11: This project is configured to use SSL. To avoid SSL warnings in the browser you can choose to trust the self-signed certificate that IIS Express has generated. Would you like to trust the IIS Express SSL certificate?](https://learn.microsoft.com/en-us/aspnet/core/static/trustcert.png?view=aspnetcore-10.0)

Select **Yes** if you trust the IIS Express SSL certificate.

The following dialog is displayed:

![Image 12: Security warning dialog](https://learn.microsoft.com/en-us/aspnet/core/static/cert.png?view=aspnetcore-10.0)

Select **Yes** if you agree to trust the development certificate.

For information on trusting the Firefox browser, see [Firefox SEC_ERROR_INADEQUATE_KEY_USAGE certificate error](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff).

Visual Studio:

    *   Starts [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/?view=aspnetcore-10.0#kestrel) server.
    *   Launches a browser.
    *   Navigates to `http://localhost:port`, such as `http://localhost:7042`. 
        *   _port_: A randomly assigned port number for the app.
        *   `localhost`: The standard hostname for the local computer. Localhost only serves web requests from the local computer.

The logs show the service listening on `https://localhost:<port>`, where `<port>` is the localhost port number randomly assigned when the project is created and set in `Properties/launchSettings.json`.

```
info: Microsoft.Hosting.Lifetime[0]
      Now listening on: https://localhost:<port>
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Development
```

Note

The gRPC template is configured to use [Transport Layer Security (TLS)](https://tools.ietf.org/html/rfc5246). gRPC clients need to use HTTPS to call the server. The gRPC service localhost port number is randomly assigned when the project is created and set in the _Properties\launchSettings.json_ file of the gRPC service project.

macOS doesn't support ASP.NET Core gRPC with TLS. Additional configuration is required to successfully run gRPC services on macOS. For more information, see [Unable to start ASP.NET Core gRPC app on macOS](https://learn.microsoft.com/en-us/aspnet/core/grpc/troubleshoot?view=aspnetcore-10.0#unable-to-start-aspnet-core-grpc-app-on-macos).

_GrpcGreeter_ project files:

*   `Protos/greet.proto`: defines the `Greeter` gRPC and is used to generate the gRPC server assets. For more information, see [Introduction to gRPC](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0).
*   `Services` folder: Contains the implementation of the `Greeter` service.
*   `appSettings.json`: Contains configuration data such as the protocol used by Kestrel. For more information, see [Configuration in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0).
*   `Program.cs`, which contains: 
    *   The entry point for the gRPC service. For more information, see [.NET Generic Host in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0).
    *   Code that configures app behavior. For more information, see [App startup](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/startup?view=aspnetcore-10.0).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_3_visual-studio-mac)

*   Open a second instance of Visual Studio and select **Create a new project**.
*   In the **Create a new project** dialog, select **Console Application**, and select **Next**.
*   In the **Project name** text box, enter **GrpcGreeterClient** and select **Next**.
*   In the **Additional information** dialog, select **.NET 6.0 (Long-term support)** and then select **Create**.

The gRPC client project requires the following NuGet packages:

*   [Grpc.Net.Client](https://www.nuget.org/packages/Grpc.Net.Client), which contains the .NET client.
*   [Google.Protobuf](https://www.nuget.org/packages/Google.Protobuf/), which contains protobuf message APIs for C#.
*   [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/), which contain C# tooling support for protobuf files. The tooling package isn't required at runtime, so the dependency is marked with `PrivateAssets="All"`.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_4_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_4_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_4_visual-studio-mac)

Install the packages using either the Package Manager Console (PMC) or Manage NuGet Packages.

*   From Visual Studio, select **Tools**>**NuGet Package Manager**>**Package Manager Console**

*   From the **Package Manager Console** window, run `cd GrpcGreeterClient` to change directories to the folder containing the `GrpcGreeterClient.csproj` files.

*   Run the following commands:

```
Install-Package Grpc.Net.Client
Install-Package Google.Protobuf
Install-Package Grpc.Tools
```

*   Right-click the project in **Solution Explorer**>**Manage NuGet Packages**.
*   Select the **Browse** tab.
*   Enter **Grpc.Net.Client** in the search box.
*   Select the **Grpc.Net.Client** package from the **Browse** tab and select **Install**.
*   Repeat for `Google.Protobuf` and `Grpc.Tools`.

*   Create a _Protos_ folder in the gRPC client project.

*   Copy the _Protos\greet.proto_ file from the gRPC Greeter service to the _Protos_ folder in the gRPC client project.

*   Update the namespace inside the `greet.proto` file to the project's namespace:

```
option csharp_namespace = "GrpcGreeterClient";
```
*   Edit the `GrpcGreeterClient.csproj` project file:

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_5_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_5_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_5_visual-studio-mac)

Right-click the project and select **Edit Project File**.

*   Add an item group with a `<Protobuf>` element that refers to the _greet.proto_ file:

```
<ItemGroup>
  <Protobuf Include="Protos\greet.proto" GrpcServices="Client" />
</ItemGroup>
```

*   Build the client project to create the types in the `GrpcGreeterClient` namespace.

Note

The `GrpcGreeterClient` types are generated automatically by the build process. The tooling package [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/) generates the following files based on the _greet.proto_ file:

*   `GrpcGreeterClient\obj\Debug\[TARGET_FRAMEWORK]\Protos\Greet.cs`: The protocol buffer code which populates, serializes and retrieves the request and response message types.
*   `GrpcGreeterClient\obj\Debug\[TARGET_FRAMEWORK]\Protos\GreetGrpc.cs`: Contains the generated client classes.

For more information on the C# assets automatically generated by [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/), see [gRPC services with C#: Generated C# assets](https://learn.microsoft.com/en-us/aspnet/core/grpc/basics?view=aspnetcore-10.0#generated-c-assets).

*   Update the gRPC client `Program.cs` file with the following code.

```
using System.Threading.Tasks;
using Grpc.Net.Client;
using GrpcGreeterClient;

// The port number must match the port of the gRPC server.
using var channel = GrpcChannel.ForAddress("https://localhost:7042");
var client = new Greeter.GreeterClient(channel);
var reply = await client.SayHelloAsync(
                  new HelloRequest { Name = "GreeterClient" });
Console.WriteLine("Greeting: " + reply.Message);
Console.WriteLine("Press any key to exit...");
Console.ReadKey();
```
*   In the preceding highlighted code, replace the localhost port number `7042` with the `HTTPS` port number specified in `Properties/launchSettings.json` within the `GrpcGreeter` service project.

`Program.cs` contains the entry point and logic for the gRPC client.

The Greeter client is created by:

*   Instantiating a `GrpcChannel` containing the information for creating the connection to the gRPC service.
*   Using the `GrpcChannel` to construct the Greeter client:

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

The Greeter client calls the asynchronous `SayHello` method. The result of the `SayHello` call is displayed:

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

Update the `appsettings.Development.json` file by adding the following highlighted lines:

```
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
      ,"Microsoft.AspNetCore.Hosting": "Information",
      "Microsoft.AspNetCore.Routing.EndpointMiddleware": "Information"
    }
  }
}
```

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_6_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_6_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_6_visual-studio-mac)

*   In the Greeter service, press `Ctrl+F5` to start the server without the debugger.
*   In the `GrpcGreeterClient` project, press `Ctrl+F5` to start the client without the debugger.

The client sends a greeting to the service with a message containing its name, _GreeterClient_. The service sends the message "Hello GreeterClient" as a response. The "Hello GreeterClient" response is displayed in the command prompt:

```
Greeting: Hello GreeterClient
Press any key to exit...
```

The gRPC service records the details of the successful call in the logs written to the command prompt:

```
info: Microsoft.Hosting.Lifetime[0]
      Now listening on: https://localhost:<port>
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Development
info: Microsoft.Hosting.Lifetime[0]
      Content root path: C:\GH\aspnet\docs\4\Docs\aspnetcore\tutorials\grpc\grpc-start\sample\GrpcGreeter
info: Microsoft.AspNetCore.Hosting.Diagnostics[1]
      Request starting HTTP/2 POST https://localhost:<port>/Greet.Greeter/SayHello application/grpc
info: Microsoft.AspNetCore.Routing.EndpointMiddleware[0]
      Executing endpoint 'gRPC - /Greet.Greeter/SayHello'
info: Microsoft.AspNetCore.Routing.EndpointMiddleware[1]
      Executed endpoint 'gRPC - /Greet.Greeter/SayHello'
info: Microsoft.AspNetCore.Hosting.Diagnostics[2]
      Request finished in 78.32260000000001ms 200 application/grpc
```

Note

The code in this article requires the ASP.NET Core HTTPS development certificate to secure the gRPC service. If the .NET gRPC client fails with the message `The remote certificate is invalid according to the validation procedure.` or `The SSL connection could not be established.`, the development certificate isn't trusted. To fix this issue, see [Call a gRPC service with an untrusted/invalid certificate](https://learn.microsoft.com/en-us/aspnet/core/grpc/troubleshoot?view=aspnetcore-10.0#call-a-grpc-service-with-an-untrustedinvalid-certificate).

*   View or download [the completed sample code for this tutorial](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/grpc/grpc-start/sample/sample6) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample)).
*   [Overview for gRPC on .NET](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0)
*   [gRPC services with C#](https://learn.microsoft.com/en-us/aspnet/core/grpc/basics?view=aspnetcore-10.0)
*   [Migrate gRPC from C-core to gRPC for .NET](https://learn.microsoft.com/en-us/aspnet/core/grpc/migration?view=aspnetcore-10.0)

This tutorial shows how to create a .NET [gRPC](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0) client and an ASP.NET Core gRPC Server. At the end, you'll have a gRPC client that communicates with the gRPC Greeter service.

In this tutorial, you:

*   Create a gRPC Server.
*   Create a gRPC client.
*   Test the gRPC client with the gRPC Greeter service.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   [Visual Studio 2022](https://visualstudio.microsoft.com/vs/#download) with the **ASP.NET and web development** workload.
*   [.NET 6 SDK](https://dotnet.microsoft.com/download/dotnet/6.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-mac)

*   Start Visual Studio 2022 and select **Create a new project**.
*   In the **Create a new project** dialog, search for `gRPC`. Select **ASP.NET Core gRPC Service** and select **Next**.
*   In the **Configure your new project** dialog, enter `GrpcGreeter` for **Project name**. It's important to name the project _GrpcGreeter_ so the namespaces match when you copy and paste code.
*   Select **Next**.
*   In the **Additional information** dialog, select **.NET 6.0 (Long-term support)** and then select **Create**.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   Press Ctrl+F5 to run without the debugger.

Visual Studio displays the following dialog when a project is not yet configured to use SSL:

![Image 13: This project is configured to use SSL. To avoid SSL warnings in the browser you can choose to trust the self-signed certificate that IIS Express has generated. Would you like to trust the IIS Express SSL certificate?](https://learn.microsoft.com/en-us/aspnet/core/static/trustcert.png?view=aspnetcore-10.0)

Select **Yes** if you trust the IIS Express SSL certificate.

The following dialog is displayed:

![Image 14: Security warning dialog](https://learn.microsoft.com/en-us/aspnet/core/static/cert.png?view=aspnetcore-10.0)

Select **Yes** if you agree to trust the development certificate.

For information on trusting the Firefox browser, see [Firefox SEC_ERROR_INADEQUATE_KEY_USAGE certificate error](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff).

Visual Studio:

    *   Starts [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/?view=aspnetcore-10.0#kestrel) server.
    *   Launches a browser.
    *   Navigates to `http://localhost:port`, such as `http://localhost:7042`. 
        *   _port_: A randomly assigned port number for the app.
        *   `localhost`: The standard hostname for the local computer. Localhost only serves web requests from the local computer.

The logs show the service listening on `https://localhost:<port>`, where `<port>` is the localhost port number randomly assigned when the project is created and set in `Properties/launchSettings.json`.

```
info: Microsoft.Hosting.Lifetime[0]
      Now listening on: https://localhost:<port>
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Development
```

Note

The gRPC template is configured to use [Transport Layer Security (TLS)](https://tools.ietf.org/html/rfc5246). gRPC clients need to use HTTPS to call the server. The gRPC service localhost port number is randomly assigned when the project is created and set in the _Properties\launchSettings.json_ file of the gRPC service project.

macOS doesn't support ASP.NET Core gRPC with TLS. Additional configuration is required to successfully run gRPC services on macOS. For more information, see [Unable to start ASP.NET Core gRPC app on macOS](https://learn.microsoft.com/en-us/aspnet/core/grpc/troubleshoot?view=aspnetcore-10.0#unable-to-start-aspnet-core-grpc-app-on-macos).

_GrpcGreeter_ project files:

*   `Protos/greet.proto`: defines the `Greeter` gRPC and is used to generate the gRPC server assets. For more information, see [Introduction to gRPC](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0).
*   `Services` folder: Contains the implementation of the `Greeter` service.
*   `appSettings.json`: Contains configuration data such as the protocol used by Kestrel. For more information, see [Configuration in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0).
*   `Program.cs`, which contains: 
    *   The entry point for the gRPC service. For more information, see [.NET Generic Host in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0).
    *   Code that configures app behavior. For more information, see [App startup](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/startup?view=aspnetcore-10.0).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_3_visual-studio-mac)

*   Open a second instance of Visual Studio and select **Create a new project**.
*   In the **Create a new project** dialog, select **Console Application**, and select **Next**.
*   In the **Project name** text box, enter **GrpcGreeterClient** and select **Next**.
*   In the **Additional information** dialog, select **.NET 6.0 (Long-term support)** and then select **Create**.

The gRPC client project requires the following NuGet packages:

*   [Grpc.Net.Client](https://www.nuget.org/packages/Grpc.Net.Client), which contains the .NET client.
*   [Google.Protobuf](https://www.nuget.org/packages/Google.Protobuf/), which contains protobuf message APIs for C#.
*   [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/), which contain C# tooling support for protobuf files. The tooling package isn't required at runtime, so the dependency is marked with `PrivateAssets="All"`.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_4_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_4_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_4_visual-studio-mac)

Install the packages using either the Package Manager Console (PMC) or Manage NuGet Packages.

*   From Visual Studio, select **Tools**>**NuGet Package Manager**>**Package Manager Console**

*   From the **Package Manager Console** window, run `cd GrpcGreeterClient` to change directories to the folder containing the `GrpcGreeterClient.csproj` files.

*   Run the following commands:

```
Install-Package Grpc.Net.Client
Install-Package Google.Protobuf
Install-Package Grpc.Tools
```

*   Right-click the project in **Solution Explorer**>**Manage NuGet Packages**.
*   Select the **Browse** tab.
*   Enter **Grpc.Net.Client** in the search box.
*   Select the **Grpc.Net.Client** package from the **Browse** tab and select **Install**.
*   Repeat for `Google.Protobuf` and `Grpc.Tools`.

*   Create a _Protos_ folder in the gRPC client project.

*   Copy the _Protos\greet.proto_ file from the gRPC Greeter service to the _Protos_ folder in the gRPC client project.

*   Update the namespace inside the `greet.proto` file to the project's namespace:

```
option csharp_namespace = "GrpcGreeterClient";
```
*   Edit the `GrpcGreeterClient.csproj` project file:

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_5_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_5_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_5_visual-studio-mac)

Right-click the project and select **Edit Project File**.

*   Add an item group with a `<Protobuf>` element that refers to the _greet.proto_ file:

```
<ItemGroup>
  <Protobuf Include="Protos\greet.proto" GrpcServices="Client" />
</ItemGroup>
```

*   Build the client project to create the types in the `GrpcGreeterClient` namespace.

Note

The `GrpcGreeterClient` types are generated automatically by the build process. The tooling package [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/) generates the following files based on the _greet.proto_ file:

*   `GrpcGreeterClient\obj\Debug\[TARGET_FRAMEWORK]\Protos\Greet.cs`: The protocol buffer code which populates, serializes and retrieves the request and response message types.
*   `GrpcGreeterClient\obj\Debug\[TARGET_FRAMEWORK]\Protos\GreetGrpc.cs`: Contains the generated client classes.

For more information on the C# assets automatically generated by [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/), see [gRPC services with C#: Generated C# assets](https://learn.microsoft.com/en-us/aspnet/core/grpc/basics?view=aspnetcore-10.0#generated-c-assets).

*   Update the gRPC client `Program.cs` file with the following code.

```
using System.Threading.Tasks;
using Grpc.Net.Client;
using GrpcGreeterClient;

// The port number must match the port of the gRPC server.
using var channel = GrpcChannel.ForAddress("https://localhost:7042");
var client = new Greeter.GreeterClient(channel);
var reply = await client.SayHelloAsync(
                  new HelloRequest { Name = "GreeterClient" });
Console.WriteLine("Greeting: " + reply.Message);
Console.WriteLine("Press any key to exit...");
Console.ReadKey();
```
*   In the preceding highlighted code, replace the localhost port number `7042` with the `HTTPS` port number specified in `Properties/launchSettings.json` within the `GrpcGreeter` service project.

`Program.cs` contains the entry point and logic for the gRPC client.

The Greeter client is created by:

*   Instantiating a `GrpcChannel` containing the information for creating the connection to the gRPC service.
*   Using the `GrpcChannel` to construct the Greeter client:

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

The Greeter client calls the asynchronous `SayHello` method. The result of the `SayHello` call is displayed:

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

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_6_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_6_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_6_visual-studio-mac)

*   In the Greeter service, press `Ctrl+F5` to start the server without the debugger.
*   In the `GrpcGreeterClient` project, press `Ctrl+F5` to start the client without the debugger.

The client sends a greeting to the service with a message containing its name, _GreeterClient_. The service sends the message "Hello GreeterClient" as a response. The "Hello GreeterClient" response is displayed in the command prompt:

```
Greeting: Hello GreeterClient
Press any key to exit...
```

The gRPC service records the details of the successful call in the logs written to the command prompt:

```
info: Microsoft.Hosting.Lifetime[0]
      Now listening on: https://localhost:<port>
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Development
info: Microsoft.Hosting.Lifetime[0]
      Content root path: C:\GH\aspnet\docs\4\Docs\aspnetcore\tutorials\grpc\grpc-start\sample\GrpcGreeter
info: Microsoft.AspNetCore.Hosting.Diagnostics[1]
      Request starting HTTP/2 POST https://localhost:<port>/Greet.Greeter/SayHello application/grpc
info: Microsoft.AspNetCore.Routing.EndpointMiddleware[0]
      Executing endpoint 'gRPC - /Greet.Greeter/SayHello'
info: Microsoft.AspNetCore.Routing.EndpointMiddleware[1]
      Executed endpoint 'gRPC - /Greet.Greeter/SayHello'
info: Microsoft.AspNetCore.Hosting.Diagnostics[2]
      Request finished in 78.32260000000001ms 200 application/grpc
```

Update the `appsettings.Development.json` file by adding the following lines:

```
"Microsoft.AspNetCore.Hosting": "Information",
"Microsoft.AspNetCore.Routing.EndpointMiddleware": "Information"
```

Note

The code in this article requires the ASP.NET Core HTTPS development certificate to secure the gRPC service. If the .NET gRPC client fails with the message `The remote certificate is invalid according to the validation procedure.` or `The SSL connection could not be established.`, the development certificate isn't trusted. To fix this issue, see [Call a gRPC service with an untrusted/invalid certificate](https://learn.microsoft.com/en-us/aspnet/core/grpc/troubleshoot?view=aspnetcore-10.0#call-a-grpc-service-with-an-untrustedinvalid-certificate).

*   View or download [the completed sample code for this tutorial](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/grpc/grpc-start/sample/sample6) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample)).
*   [Overview for gRPC on .NET](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0)
*   [gRPC services with C#](https://learn.microsoft.com/en-us/aspnet/core/grpc/basics?view=aspnetcore-10.0)
*   [Migrate gRPC from C-core to gRPC for .NET](https://learn.microsoft.com/en-us/aspnet/core/grpc/migration?view=aspnetcore-10.0)

This tutorial shows how to create a .NET [gRPC](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0) client and an ASP.NET Core gRPC Server.

At the end, you'll have a gRPC client that communicates with the gRPC Greeter service.

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/grpc/grpc-start/sample) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample)).

In this tutorial, you:

*   Create a gRPC Server.
*   Create a gRPC client.
*   Test the gRPC client with the gRPC Greeter service.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   [Visual Studio 2019 16.8 or later](https://visualstudio.microsoft.com/downloads/?utm_medium=microsoft&utm_source=learn.microsoft.com&utm_campaign=inline+link&utm_content=download+vs2019) with the **ASP.NET and web development** workload
*   [.NET 5 SDK](https://dotnet.microsoft.com/download/dotnet/5.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-mac)

*   Start Visual Studio and select **Create a new project**.
*   In the **Create a new project** dialog, select **gRPC Service** and select **Next**.
*   In the **Configure your new project** dialog, enter `GrpcGreeter` for **Project name**. It's important to name the project _GrpcGreeter_ so the namespaces match when you copy and paste code.
*   Select **Next**.
*   In the **Additional information** dialog, select **.NET 5.0** in the **Target Framework** dropdown.
*   Select **Create**.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   Press Ctrl+F5 to run without the debugger.

Visual Studio displays the following dialog when a project is not yet configured to use SSL:

![Image 15: This project is configured to use SSL. To avoid SSL warnings in the browser you can choose to trust the self-signed certificate that IIS Express has generated. Would you like to trust the IIS Express SSL certificate?](https://learn.microsoft.com/en-us/aspnet/core/static/trustcert.png?view=aspnetcore-10.0)

Select **Yes** if you trust the IIS Express SSL certificate.

The following dialog is displayed:

![Image 16: Security warning dialog](https://learn.microsoft.com/en-us/aspnet/core/static/cert.png?view=aspnetcore-10.0)

Select **Yes** if you agree to trust the development certificate.

For information on trusting the Firefox browser, see [Firefox SEC_ERROR_INADEQUATE_KEY_USAGE certificate error](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff).

Visual Studio starts [IIS Express](https://learn.microsoft.com/en-us/iis/extensions/introduction-to-iis-express/iis-express-overview) and runs the app. The address bar shows `localhost:port#` and not something like `example.com`. That's because `localhost` is the standard hostname for the local computer. Localhost only serves web requests from the local computer. When Visual Studio creates a web project, a random port is used for the web server.

The logs show the service listening on `https://localhost:5001`.

```
info: Microsoft.Hosting.Lifetime[0]
      Now listening on: https://localhost:5001
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Development
```

_GrpcGreeter_ project files:

*   _greet.proto_: The _Protos/greet.proto_ file defines the `Greeter` gRPC and is used to generate the gRPC server assets. For more information, see [Introduction to gRPC](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0).
*   _Services_ folder: Contains the implementation of the `Greeter` service.
*   `appsettings.json`: Contains configuration data, such as protocol used by Kestrel. For more information, see [Configuration in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0).
*   `Program.cs`: Contains the entry point for the gRPC service. For more information, see [.NET Generic Host in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0).
*   `Startup.cs`: Contains code that configures app behavior. For more information, see [App startup](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/startup?view=aspnetcore-10.0).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_3_visual-studio-mac)

*   Open a second instance of Visual Studio and select **Create a new project**.
*   In the **Create a new project** dialog, select **Console App (.NET)** and select **Next**.
*   In the **Project name** text box, enter **GrpcGreeterClient** and select **Create**.

The gRPC client project requires the following packages:

*   [Grpc.Net.Client](https://www.nuget.org/packages/Grpc.Net.Client), which contains the .NET client.
*   [Google.Protobuf](https://www.nuget.org/packages/Google.Protobuf/), which contains protobuf message APIs for C#.
*   [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/), which contains C# tooling support for protobuf files. The tooling package isn't required at runtime, so the dependency is marked with `PrivateAssets="All"`.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_4_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_4_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_4_visual-studio-mac)

Install the packages using either the Package Manager Console (PMC) or Manage NuGet Packages.

*   From Visual Studio, select **Tools**>**NuGet Package Manager**>**Package Manager Console**

*   From the **Package Manager Console** window, run `cd GrpcGreeterClient` to change directories to the folder containing the `GrpcGreeterClient.csproj` files.

*   Run the following commands:

```
Install-Package Grpc.Net.Client
Install-Package Google.Protobuf
Install-Package Grpc.Tools
```

*   Right-click the project in **Solution Explorer**>**Manage NuGet Packages**.
*   Select the **Browse** tab.
*   Enter **Grpc.Net.Client** in the search box.
*   Select the **Grpc.Net.Client** package from the **Browse** tab and select **Install**.
*   Repeat for `Google.Protobuf` and `Grpc.Tools`.

*   Create a _Protos_ folder in the gRPC client project.

*   Copy the _Protos\greet.proto_ file from the gRPC Greeter service to the _Protos_ folder in the gRPC client project.

*   Update the namespace inside the `greet.proto` file to the project's namespace:

```
option csharp_namespace = "GrpcGreeterClient";
```
*   Edit the `GrpcGreeterClient.csproj` project file:

    *   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_5_visual-studio)
    *   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_5_visual-studio-code)
    *   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_5_visual-studio-mac)

Right-click the project and select **Edit Project File**.

* * *

*   Add an item group with a `<Protobuf>` element that refers to the _greet.proto_ file:

```
<ItemGroup>
  <Protobuf Include="Protos\greet.proto" GrpcServices="Client" />
</ItemGroup>
```

*   Build the client project to create the types in the `GrpcGreeterClient` namespace.

Note

The `GrpcGreeterClient` types are generated automatically by the build process. The tooling package [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/) generates the following files based on the _greet.proto_ file:

*   `GrpcGreeterClient\obj\Debug\[TARGET_FRAMEWORK]\Protos\Greet.cs`: The protocol buffer code which populates, serializes and retrieves the request and response message types.
*   `GrpcGreeterClient\obj\Debug\[TARGET_FRAMEWORK]\Protos\GreetGrpc.cs`: Contains the generated client classes.

For more information on the C# assets automatically generated by [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/), see [gRPC services with C#: Generated C# assets](https://learn.microsoft.com/en-us/aspnet/core/grpc/basics?view=aspnetcore-10.0#generated-c-assets).

*   Update the gRPC client `Program.cs` file with the following code:

```
using System;
using System.Net.Http;
using System.Threading.Tasks;
using Grpc.Net.Client;

namespace GrpcGreeterClient
{
    class Program
    {
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
    }
}
```

`Program.cs` contains the entry point and logic for the gRPC client.

The Greeter client is created by:

*   Instantiating a `GrpcChannel` containing the information for creating the connection to the gRPC service.
*   Using the `GrpcChannel` to construct the Greeter client:

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

The Greeter client calls the asynchronous `SayHello` method. The result of the `SayHello` call is displayed:

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

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_6_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_6_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_6_visual-studio-mac)

*   In the Greeter service, press `Ctrl+F5` to start the server without the debugger.
*   In the `GrpcGreeterClient` project, press `Ctrl+F5` to start the client without the debugger.

The client sends a greeting to the service with a message containing its name, _GreeterClient_. The service sends the message "Hello GreeterClient" as a response. The "Hello GreeterClient" response is displayed in the command prompt:

```
Greeting: Hello GreeterClient
Press any key to exit...
```

The gRPC service records the details of the successful call in the logs written to the command prompt:

```
info: Microsoft.Hosting.Lifetime[0]
      Now listening on: https://localhost:5001
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Development
info: Microsoft.Hosting.Lifetime[0]
      Content root path: C:\GH\aspnet\docs\4\Docs\aspnetcore\tutorials\grpc\grpc-start\sample\GrpcGreeter
info: Microsoft.AspNetCore.Hosting.Diagnostics[1]
      Request starting HTTP/2 POST https://localhost:5001/Greet.Greeter/SayHello application/grpc
info: Microsoft.AspNetCore.Routing.EndpointMiddleware[0]
      Executing endpoint 'gRPC - /Greet.Greeter/SayHello'
info: Microsoft.AspNetCore.Routing.EndpointMiddleware[1]
      Executed endpoint 'gRPC - /Greet.Greeter/SayHello'
info: Microsoft.AspNetCore.Hosting.Diagnostics[2]
      Request finished in 78.32260000000001ms 200 application/grpc
```

Note

The code in this article requires the ASP.NET Core HTTPS development certificate to secure the gRPC service. If the .NET gRPC client fails with the message `The remote certificate is invalid according to the validation procedure.` or `The SSL connection could not be established.`, the development certificate isn't trusted. To fix this issue, see [Call a gRPC service with an untrusted/invalid certificate](https://learn.microsoft.com/en-us/aspnet/core/grpc/troubleshoot?view=aspnetcore-10.0#call-a-grpc-service-with-an-untrustedinvalid-certificate).

*   [Overview for gRPC on .NET](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0)
*   [gRPC services with C#](https://learn.microsoft.com/en-us/aspnet/core/grpc/basics?view=aspnetcore-10.0)
*   [Migrate gRPC from C-core to gRPC for .NET](https://learn.microsoft.com/en-us/aspnet/core/grpc/migration?view=aspnetcore-10.0)

This tutorial shows how to create a .NET Core [gRPC](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0) client and an ASP.NET Core gRPC Server.

At the end, you'll have a gRPC client that communicates with the gRPC Greeter service.

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/grpc/grpc-start/sample) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample)).

In this tutorial, you:

*   Create a gRPC Server.
*   Create a gRPC client.
*   Test the gRPC client with the gRPC Greeter service.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   [Visual Studio 2019 16.4 or later](https://visualstudio.microsoft.com/downloads/?utm_medium=microsoft&utm_source=learn.microsoft.com&utm_campaign=inline+link&utm_content=download+vs2019) with the **ASP.NET and web development** workload
*   [.NET Core 3.1 SDK](https://dotnet.microsoft.com/download/dotnet-core/3.1)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-mac)

*   Start Visual Studio and select **Create a new project**. Alternatively, from the Visual Studio **File** menu, select **New**>**Project**.

*   In the **Create a new project** dialog, select **gRPC Service** and select **Next**:

![Image 17: Create a new project dialog in Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start/static/cnp.png?view=aspnetcore-10.0)

*   Name the project **GrpcGreeter**. It's important to name the project _GrpcGreeter_ so the namespaces match when you copy and paste code.

*   Select **Create**.

*   In the **Create a new gRPC service** dialog:

    *   The **gRPC Service** template is selected.
    *   Select **Create**.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   Press Ctrl+F5 to run without the debugger.

Visual Studio displays the following dialog when a project is not yet configured to use SSL:

![Image 18: This project is configured to use SSL. To avoid SSL warnings in the browser you can choose to trust the self-signed certificate that IIS Express has generated. Would you like to trust the IIS Express SSL certificate?](https://learn.microsoft.com/en-us/aspnet/core/static/trustcert.png?view=aspnetcore-10.0)

Select **Yes** if you trust the IIS Express SSL certificate.

The following dialog is displayed:

![Image 19: Security warning dialog](https://learn.microsoft.com/en-us/aspnet/core/static/cert.png?view=aspnetcore-10.0)

Select **Yes** if you agree to trust the development certificate.

For information on trusting the Firefox browser, see [Firefox SEC_ERROR_INADEQUATE_KEY_USAGE certificate error](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff).

Visual Studio starts [IIS Express](https://learn.microsoft.com/en-us/iis/extensions/introduction-to-iis-express/iis-express-overview) and runs the app. The address bar shows `localhost:port#` and not something like `example.com`. That's because `localhost` is the standard hostname for the local computer. Localhost only serves web requests from the local computer. When Visual Studio creates a web project, a random port is used for the web server.

The logs show the service listening on `https://localhost:5001`.

```
info: Microsoft.Hosting.Lifetime[0]
      Now listening on: https://localhost:5001
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Development
```

_GrpcGreeter_ project files:

*   _greet.proto_: The _Protos/greet.proto_ file defines the `Greeter` gRPC and is used to generate the gRPC server assets. For more information, see [Introduction to gRPC](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0).
*   _Services_ folder: Contains the implementation of the `Greeter` service.
*   `appsettings.json`: Contains configuration data, such as protocol used by Kestrel. For more information, see [Configuration in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0).
*   `Program.cs`: Contains the entry point for the gRPC service. For more information, see [.NET Generic Host in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0).
*   `Startup.cs`: Contains code that configures app behavior. For more information, see [App startup](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/startup?view=aspnetcore-10.0).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_3_visual-studio-mac)

*   Open a second instance of Visual Studio and select **Create a new project**.
*   In the **Create a new project** dialog, select **Console App (.NET Core)** and select **Next**.
*   In the **Project name** text box, enter **GrpcGreeterClient** and select **Create**.

The gRPC client project requires the following packages:

*   [Grpc.Net.Client](https://www.nuget.org/packages/Grpc.Net.Client), which contains the .NET Core client.
*   [Google.Protobuf](https://www.nuget.org/packages/Google.Protobuf/), which contains protobuf message APIs for C#.
*   [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/), which contains C# tooling support for protobuf files. The tooling package isn't required at runtime, so the dependency is marked with `PrivateAssets="All"`.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_4_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_4_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_4_visual-studio-mac)

Install the packages using either the Package Manager Console (PMC) or Manage NuGet Packages.

*   From Visual Studio, select **Tools**>**NuGet Package Manager**>**Package Manager Console**

*   From the **Package Manager Console** window, run `cd GrpcGreeterClient` to change directories to the folder containing the `GrpcGreeterClient.csproj` files.

*   Run the following commands:

```
Install-Package Grpc.Net.Client
Install-Package Google.Protobuf
Install-Package Grpc.Tools
```

*   Right-click the project in **Solution Explorer**>**Manage NuGet Packages**.
*   Select the **Browse** tab.
*   Enter **Grpc.Net.Client** in the search box.
*   Select the **Grpc.Net.Client** package from the **Browse** tab and select **Install**.
*   Repeat for `Google.Protobuf` and `Grpc.Tools`.

*   Create a _Protos_ folder in the gRPC client project.

*   Copy the _Protos\greet.proto_ file from the gRPC Greeter service to the _Protos_ folder in the gRPC client project.

*   Update the namespace inside the `greet.proto` file to the project's namespace:

```
option csharp_namespace = "GrpcGreeterClient";
```
*   Edit the `GrpcGreeterClient.csproj` project file:

    *   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_5_visual-studio)
    *   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_5_visual-studio-code)
    *   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_5_visual-studio-mac)

Right-click the project and select **Edit Project File**.

* * *

*   Add an item group with a `<Protobuf>` element that refers to the _greet.proto_ file:

```
<ItemGroup>
  <Protobuf Include="Protos\greet.proto" GrpcServices="Client" />
</ItemGroup>
```

*   Build the client project to create the types in the `GrpcGreeterClient` namespace.

Note

The `GrpcGreeterClient` types are generated automatically by the build process. The tooling package [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/) generates the following files based on the _greet.proto_ file:

*   `GrpcGreeterClient\obj\Debug\[TARGET_FRAMEWORK]\Protos\Greet.cs`: The protocol buffer code which populates, serializes and retrieves the request and response message types.
*   `GrpcGreeterClient\obj\Debug\[TARGET_FRAMEWORK]\Protos\GreetGrpc.cs`: Contains the generated client classes.

For more information on the C# assets automatically generated by [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/), see [gRPC services with C#: Generated C# assets](https://learn.microsoft.com/en-us/aspnet/core/grpc/basics?view=aspnetcore-10.0#generated-c-assets).

Update the gRPC client `Program.cs` file with the following code:

```
using System;
using System.Net.Http;
using System.Threading.Tasks;
using Grpc.Net.Client;

namespace GrpcGreeterClient
{
    class Program
    {
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
    }
}
```

`Program.cs` contains the entry point and logic for the gRPC client.

The Greeter client is created by:

*   Instantiating a `GrpcChannel` containing the information for creating the connection to the gRPC service.
*   Using the `GrpcChannel` to construct the Greeter client:

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

The Greeter client calls the asynchronous `SayHello` method. The result of the `SayHello` call is displayed:

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

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_6_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_6_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-10.0#tabpanel_6_visual-studio-mac)

*   In the Greeter service, press `Ctrl+F5` to start the server without the debugger.
*   In the `GrpcGreeterClient` project, press `Ctrl+F5` to start the client without the debugger.

The client sends a greeting to the service with a message containing its name, _GreeterClient_. The service sends the message "Hello GreeterClient" as a response. The "Hello GreeterClient" response is displayed in the command prompt:

```
Greeting: Hello GreeterClient
Press any key to exit...
```

The gRPC service records the details of the successful call in the logs written to the command prompt:

```
info: Microsoft.Hosting.Lifetime[0]
      Now listening on: https://localhost:5001
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Development
info: Microsoft.Hosting.Lifetime[0]
      Content root path: C:\GH\aspnet\docs\4\Docs\aspnetcore\tutorials\grpc\grpc-start\sample\GrpcGreeter
info: Microsoft.AspNetCore.Hosting.Diagnostics[1]
      Request starting HTTP/2 POST https://localhost:5001/Greet.Greeter/SayHello application/grpc
info: Microsoft.AspNetCore.Routing.EndpointMiddleware[0]
      Executing endpoint 'gRPC - /Greet.Greeter/SayHello'
info: Microsoft.AspNetCore.Routing.EndpointMiddleware[1]
      Executed endpoint 'gRPC - /Greet.Greeter/SayHello'
info: Microsoft.AspNetCore.Hosting.Diagnostics[2]
      Request finished in 78.32260000000001ms 200 application/grpc
```

Note

The code in this article requires the ASP.NET Core HTTPS development certificate to secure the gRPC service. If the .NET gRPC client fails with the message `The remote certificate is invalid according to the validation procedure.` or `The SSL connection could not be established.`, the development certificate isn't trusted. To fix this issue, see [Call a gRPC service with an untrusted/invalid certificate](https://learn.microsoft.com/en-us/aspnet/core/grpc/troubleshoot?view=aspnetcore-10.0#call-a-grpc-service-with-an-untrustedinvalid-certificate).

*   [Overview for gRPC on .NET](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-10.0)
*   [gRPC services with C#](https://learn.microsoft.com/en-us/aspnet/core/grpc/basics?view=aspnetcore-10.0)
*   [Migrate gRPC from C-core to gRPC for .NET](https://learn.microsoft.com/en-us/aspnet/core/grpc/migration?view=aspnetcore-10.0)
