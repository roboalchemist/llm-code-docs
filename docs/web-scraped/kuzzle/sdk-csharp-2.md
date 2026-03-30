# Source: https://docs.kuzzle.io/sdk/csharp/2

Title: Kuzzle Documentation

URL Source: https://docs.kuzzle.io/sdk/csharp/2

Markdown Content:
Getting Started with Kuzzle and C# [#](https://docs.kuzzle.io/sdk/csharp/2#getting-started-with-kuzzle-and-c)
-------------------------------------------------------------------------------------------------------------

This tutorial explains how to use **Kuzzle** with **C#**, **.NET Core SDK 2.1** and the **Kuzzle C# SDK**. It will walk you through creating scripts that can **store** documents in Kuzzle and subscribe to **notifications** about document creations.

You are going to write an application that **stores** documents in Kuzzle Server and subscribes to **real time notifications** for each created document.

To follow this tutorial, you must have a Kuzzle Server up and running. Follow these instructions if this is not already the case: [Running Kuzzle](https://docs.kuzzle.io/core/2/guides/getting-started/run-kuzzle).

Having trouble? Get in touch with us on [Discord](http://join.discord.kuzzle.io/)!

Explore the SDK [#](https://docs.kuzzle.io/sdk/csharp/2#explore-the-sdk)
------------------------------------------------------------------------

It's time to get started with the [Kuzzle C# SDK](https://docs.kuzzle.io/sdk/csharp/2). This section explains how to store a document and how to subscribe to notifications in Kuzzle using the C# SDK.

Before proceeding, please make sure your system has **.NET Core SDK** version 2.1 or higher.

If you're using monodevelop on Linux, you'll need at least mono 5.20+ (w/ msbuild 16+). Due to compatibility issues, you HAVE TO install .NET Core SDK 2.1, if you only have the 2.2 one, you won't be able to build the project with msbuild (which monodevelop uses).

Prepare your environment [#](https://docs.kuzzle.io/sdk/csharp/2#prepare-your-environment)
------------------------------------------------------------------------------------------

Create your playground directory, initialize a new console application using dotnet CLI and add a reference to the [Kuzzle SDK package](https://www.nuget.org/packages/kuzzlesdk/).

```
mkdir "kuzzle-playground"
cd "kuzzle-playground"
dotnet new console
dotnet add package kuzzlesdk
```

Then inside the `Program.cs` file, we will create a console application that takes an argument to either initialize the application, subscribe to notification or create a document.

```
using KuzzleSdk;
using KuzzleSdk.Protocol;
using System;
using System.Threading;
using System.Threading.Tasks;
using Newtonsoft.Json;
namespace getting_started_csharp
{
  class Init
  {
    static async Task Main(string[] args)
    {
      Console.WriteLine(args[0]);
      switch (args[0])
      {
        case "init":
          await Init();
          break;
        case "subscribe":
          await Subscribe();
          break;
        case "create":
          await Create();
          break;
      }
    }
    static async Task Init() {
      return;
    }
    static async Task Subscribe() {
      return;
    }
    static async Task Create() {
      return;
    }
  }
}
```

Then create a `GetSdk` function to instantiate the SDK and connect it to a Kuzzle instance using the WebSocket protocol.

Once done, connect the client to your Kuzzle server using the [Kuzzle.ConnectAsync](https://docs.kuzzle.io/sdk/csharp/2/core-classes/kuzzle/connect-async) method.

```
static async Task<Kuzzle> GetSdk()
{
  WebSocket socket = new WebSocket(new Uri("ws://kuzzle:7512"));
  Kuzzle kuzzle = new Kuzzle(socket);
  try {
    await kuzzle.ConnectAsync(CancellationToken.None);
  } catch (KuzzleException e) {
    Console.Error.WriteLine(e.Message);
  }
  return kuzzle;
}
```

Replace 'kuzzle' which is the Kuzzle server hostname with 'localhost' or with the host name where your Kuzzle server is running.

Now, you need to create a new 'nyc-open-data' index, holding a new 'yellow-taxi' collection. This structure will be used later on to store data.

```
static async Task Init() {
  Kuzzle kuzzle = await GetSdk();
  try {
    await kuzzle.Index.CreateAsync("nyc-open-data");
    await kuzzle.Collection.CreateAsync("nyc-open-data", "yellow-taxi");
  } catch (KuzzleException e) {
    Console.Error.WriteLine(e.Message);
  }
  Console.WriteLine("nyc-open-data/yellow-taxi ready!");
  return;
}
```

Your `Program.cs` file should now look like this:

```
using KuzzleSdk;
using KuzzleSdk.Protocol;
using KuzzleSdk.Exceptions;
using System;
using System.Threading;
using System.Threading.Tasks;
using Newtonsoft.Json;
namespace getting_started_csharp
{
  class Program
  {
    static async Task Main(string[] args)
    {
      Console.WriteLine(args[0]);
      switch (args[0])
      {
        case "init":
          await Init();
          break;
        case "subscribe":
          await Subscribe();
          break;
        case "create":
          await Create();
          break;
      }
    }
    static async Task<Kuzzle> GetSdk()
    {
      WebSocket socket = new WebSocket(new Uri("ws://kuzzle:7512"));
      Kuzzle kuzzle = new Kuzzle(socket);
      try {
        await kuzzle.ConnectAsync(CancellationToken.None);
      } catch (KuzzleException e) {
        Console.Error.WriteLine(e.Message);
      }
      return kuzzle;
    }
    static async Task Init() {
      Kuzzle kuzzle = await GetSdk();
      try {
        await kuzzle.Index.CreateAsync("nyc-open-data");
        await kuzzle.Collection.CreateAsync("nyc-open-data", "yellow-taxi");
      } catch (KuzzleException e) {
        Console.Error.WriteLine(e.Message);
      }
      Console.WriteLine("nyc-open-data/yellow-taxi ready!");
      return;
    }
    static async Task Subscribe() {
      return;
    }
    static async Task Create() {
      return;
    }
  }
}
```

This code does the following:

*   creates an instance of the SDK
*   connects it to Kuzzle running on `kuzzle` (change the hostname if needed) using WebSocket
*   creates the `nyc-open-data` index
*   creates the `yellow-taxi` collection within the `nyc-open-data` index

Run the code with dotnet:

`dotnet run -- init`

The console should output the following message:

`nyc-open-data/yellow-taxi ready!`

Congratulations! You are now ready to say Hello to the World!

Create your first "Hello World" document [#](https://docs.kuzzle.io/sdk/csharp/2#create-your-first-hello-world-document)
------------------------------------------------------------------------------------------------------------------------

Complete the `Create` method with the following code:

```
static async Task Create() {
  Kuzzle kuzzle = await GetSdk();
  JObject driver = JObject.Parse(@"{
    ""name"": ""Liia"",
    ""birthday"": ""1990-09-12"",
    ""license"": ""B""
  }");
  try {
    await kuzzle.Document.CreateAsync("nyc-open-data", "yellow-taxi", driver);
  } catch (KuzzleException e) {
    Console.Error.WriteLine(e.Message);
  }
  Console.WriteLine("New document successfully created!");
  return;
}
```

This code does the following:

*   creates a new document in the `yellow-taxi` collection, within the `nyc-open-data` index
*   logs a success message to the console if everything went fine
*   logs an error message if any of the previous actions fails

Run the code with dotnet:

`dotnet run -- create`

You have now successfully stored your first document into Kuzzle. You can now open an [Admin Console](http://console.kuzzle.io/) to browse your collection and confirm that your document was saved.

Subscribe to realtime document notifications (pub/sub) [#](https://docs.kuzzle.io/sdk/csharp/2#subscribe-to-realtime-document-notifications-pub-sub)
----------------------------------------------------------------------------------------------------------------------------------------------------

Kuzzle provides pub/sub features that can be used to trigger real-time notifications based on the state of your data (for a deep-dive on notifications check out the [realtime notifications](https://docs.kuzzle.io/sdk/csharp/2/essentials/realtime-notifications/) documentation).

Let's get started. Complete the `Subscribe` method with the following code:

```
static async Task Subscribe() {
  CancellationTokenSource token = new CancellationTokenSource();
  Kuzzle kuzzle = await GetSdk();
  try {
    await kuzzle.Realtime.SubscribeAsync(
      "nyc-open-data",
      "yellow-taxi",
      JObject.Parse("{}"),
      (notification) => {
        string name = (string) notification.Result["_source"]["name"];
        string driverId = (string) notification.Result["_id"];
        Console.WriteLine($"New driver {name} with id {driverId} has B license.");
        token.Cancel();
      });
  } catch (KuzzleException e) {
    Console.Error.WriteLine(e.Message);
  }
  Console.WriteLine("Successfully subscribed to document notifications!");
  await Task.Delay(10000, token.Token);
  return;
}
```

Run the code with dotnet:

`dotnet run -- subscribe`

The program is now running endlessly, waiting for notifications about documents matching its filters, specifically documents that have a `license` field equal to `'B'`.

We added a `await Task.Delay(10000, token.Token);` line after a successfull subscribe to keep the program running until after a notification has been received.

Now in another terminal, launch the program to create a document:

`dotnet run -- create`

This creates a new document in Kuzzle which, in turn, triggers a [document notification](https://docs.kuzzle.io/core/2/api/payloads/notifications/#documents-changes-messages). That notification is sent by Kuzzle to our other running program, which subscribed to changes occuring in that index and collection. Check the subscribe program terminal: a new message is printed everytime a document is created.

`New driver Liia with id AWccRe3-DfukVhSzMdUo has B license.`

Congratulations! You have just set up your first pub/sub communication!

Where do we go from here? [#](https://docs.kuzzle.io/sdk/csharp/2#where-do-we-go-from-here)
-------------------------------------------------------------------------------------------

Now that you're more familiar with Kuzzle, dive even deeper to learn how to leverage its full capabilities:

*   discover what this SDK has to offer by browsing other sections of this documentation
*   learn how to use [Koncorde](https://docs.kuzzle.io/core/2/api/koncorde-filters-syntax) to create incredibly fine-grained and blazing-fast subscriptions
*   learn how to perform a [basic authentication](https://docs.kuzzle.io/sdk/csharp/2/controllers/auth/login)
*   follow our guide to learn how to [manage users, and how to set up fine-grained access control](https://docs.kuzzle.io/core/2/guides/main-concepts/permissions)
