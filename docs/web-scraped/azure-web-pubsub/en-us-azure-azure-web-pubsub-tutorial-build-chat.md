# Source: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat

Title: Tutorial - Create a chat app with Azure Web PubSub service

URL Source: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat

Markdown Content:
In [Publish and subscribe message tutorial](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-pub-sub-messages), you learn the basics of publishing and subscribing messages with Azure Web PubSub. In this tutorial, you learn the event system of Azure Web PubSub and use it to build a complete web application with real-time communication functionality.

In this tutorial, you learn how to:

*   Create a Web PubSub service instance
*   Configure event handler settings for Azure Web PubSub
*   Handle events in the app server and build a real-time chat app

If you don't have an Azure account, create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.

*   Use the Bash environment in [Azure Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/overview). For more information, see [Get started with Azure Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/quickstart).

[![Image 1](https://learn.microsoft.com/en-us/azure/reusable-content/azure-cli/media/hdi-launch-cloud-shell.png)](https://shell.azure.com/)

*   If you prefer to run CLI reference commands locally, [install](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) the Azure CLI. If you're running on Windows or macOS, consider running Azure CLI in a Docker container. For more information, see [How to run the Azure CLI in a Docker container](https://learn.microsoft.com/en-us/cli/azure/run-azure-cli-docker).

    *   If you're using a local installation, sign in to the Azure CLI by using the [az login](https://learn.microsoft.com/en-us/cli/azure/reference-index#az-login) command. To finish the authentication process, follow the steps displayed in your terminal. For other sign-in options, see [Authenticate to Azure using Azure CLI](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli).

    *   When you're prompted, install the Azure CLI extension on first use. For more information about extensions, see [Use and manage extensions with the Azure CLI](https://learn.microsoft.com/en-us/cli/azure/azure-cli-extensions-overview).

    *   Run [az version](https://learn.microsoft.com/en-us/cli/azure/reference-index?#az-version) to find the version and dependent libraries that are installed. To upgrade to the latest version, run [az upgrade](https://learn.microsoft.com/en-us/cli/azure/reference-index?#az-upgrade).

*   This setup requires version 2.22.0 or higher of the Azure CLI. If using Azure Cloud Shell, the latest version is already installed.

A resource group is a logical container into which Azure resources are deployed and managed. Use the [az group create](https://learn.microsoft.com/en-us/cli/azure/group#az-group-create) command to create a resource group named `myResourceGroup` in the `eastus` location.

```
az group create --name myResourceGroup --location EastUS
```

Run [az extension add](https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-add) to install or upgrade the _webpubsub_ extension to the current version.

```
az extension add --upgrade --name webpubsub
```

Use the Azure CLI [az webpubsub create](https://learn.microsoft.com/en-us/cli/azure/webpubsub#az-webpubsub-create) command to create a Web PubSub in the resource group you've created. The following command creates a _Free_ Web PubSub resource under resource group _myResourceGroup_ in _EastUS_:

Important

Each Web PubSub resource must have a unique name. Replace <your-unique-resource-name> with the name of your Web PubSub in the following examples.

```
az webpubsub create --name "<your-unique-resource-name>" --resource-group "myResourceGroup" --location "EastUS" --sku Free_F1
```

The output of this command shows properties of the newly created resource. Take note of the two properties listed below:

*   **Resource Name**: The name you provided to the `--name` parameter above.
*   **hostName**: In the example, the host name is `<your-unique-resource-name>.webpubsub.azure.com/`.

At this point, your Azure account is the only one authorized to perform any operations on this new resource.

Important

Raw connection strings appear in this article for demonstration purposes only.

A connection string includes the authorization information required for your application to access Azure Web PubSub service. The access key inside the connection string is similar to a root password for your service. In production environments, always protect your access keys. Use Azure Key Vault to manage and rotate your keys securely and [secure your connection with `WebPubSubServiceClient`](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/howto-create-serviceclient-with-net-and-azure-identity).

Avoid distributing access keys to other users, hard-coding them, or saving them anywhere in plain text that is accessible to others. Rotate your keys if you believe they may have been compromised.

Use the Azure CLI [az webpubsub key](https://learn.microsoft.com/en-us/cli/azure/webpubsub#az-webpubsub-key) command to get the **ConnectionString** of the service. Replace the `<your-unique-resource-name>` placeholder with the name of your Azure Web PubSub instance.

```
az webpubsub key show --resource-group myResourceGroup --name <your-unique-resource-name> --query primaryConnectionString --output tsv
```

Copy the connection string to use later.

Copy the fetched **ConnectionString** and set it into environment variable `WebPubSubConnectionString`, which the tutorial later reads. Replace `<connection-string>` below with the **ConnectionString** you fetched.

```
export WebPubSubConnectionString="<connection-string>"
```

```
SET WebPubSubConnectionString=<connection-string>
```

*   [C#](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_1_csharp)
*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_1_javascript)
*   [Java](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_1_java)
*   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_1_python)

*   [ASP.NET Core 8](https://learn.microsoft.com/en-us/aspnet/core)

In Azure Web PubSub, there are two roles, server and client. This concept is similar to the server and client roles in a web application. Server is responsible to manage the clients, listen, and respond to client messages. Client is responsible to send and receive user's messages from server and visualize them for end user.

In this tutorial, we build a real-time chat web application. In a real web application, server's responsibility also includes authenticating clients and serving static web pages for the application UI.

*   [C#](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_2_csharp)
*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_2_javascript)
*   [Java](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_2_java)
*   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_2_python)

We use [ASP.NET Core 8](https://learn.microsoft.com/en-us/aspnet/core) to host the web pages and handle incoming requests.

First let's create an ASP.NET Core web app in a `chatapp` folder.

1.   Create a new web app.

```
mkdir chatapp
cd chatapp
dotnet new web
```
2.   Add `app.UseStaticFiles()` Program.cs to support hosting static web pages.

```
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.UseStaticFiles();

app.Run();
```
3.   Create an HTML file and save it as `wwwroot/index.html`, we use it for the UI of the chat app later.

```
<html>
  <body>
    <h1>Azure Web PubSub Chat</h1>
  </body>
</html>
```

You can test the server by running `dotnet run --urls http://localhost:8080` and access `http://localhost:8080/index.html` in the browser.

In the tutorial [Publish and subscribe message](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-pub-sub-messages), the subscriber consumes connection string directly. In a real world application, it isn't safe to share the connection string with any client, because connection string has high privilege to do any operation to the service. Now, let's have your server consuming the connection string, and exposing a `negotiate` endpoint for the client to get the full URL with access token. In such way, the server can add auth middleware before the `negotiate` endpoint to prevent unauthorized access.

*   [C#](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_3_csharp)
*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_3_javascript)
*   [Java](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_3_java)
*   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_3_python)

First install the dependencies.

```
dotnet add package Microsoft.Azure.WebPubSub.AspNetCore
```

Now let's add a `/negotiate` endpoint for the client to call to generate the token.

```
using Azure.Core;
using Microsoft.Azure.WebPubSub.AspNetCore;
using Microsoft.Azure.WebPubSub.Common;
using Microsoft.Extensions.Primitives;

// Read connection string from environment
var connectionString = Environment.GetEnvironmentVariable("WebPubSubConnectionString");
if (connectionString == null)
{
    throw new ArgumentNullException(nameof(connectionString));
}

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddWebPubSub(o => o.ServiceEndpoint = new WebPubSubServiceEndpoint(connectionString))
    .AddWebPubSubServiceClient<Sample_ChatApp>();
var app = builder.Build();

app.UseStaticFiles();

// return the Client Access URL with negotiate endpoint
app.MapGet("/negotiate", (WebPubSubServiceClient<Sample_ChatApp> service, HttpContext context) =>
{
    var id = context.Request.Query["id"];
    if (StringValues.IsNullOrEmpty(id))
    {
        context.Response.StatusCode = 400;
        return null;
    }
    return new
    {
        url = service.GetClientAccessUri(userId: id).AbsoluteUri
    };
});
app.Run();

sealed class Sample_ChatApp : WebPubSubHub
{
}
```

`AddWebPubSubServiceClient<THub>()` is used to inject the service client `WebPubSubServiceClient<THub>`, with which we can use in negotiation step to generate client connection token and in hub methods to invoke service REST APIs when hub events are triggered. This token generation code is similar to the one we used in the [publish and subscribe message tutorial](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-pub-sub-messages), except we pass one more argument (`userId`) when generating the token. User ID can be used to identify the identity of client so when you receive a message you know where the message is coming from.

The code reads connection string from environment variable `WebPubSubConnectionString` that we set in [previous step](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#get-the-connectionstring-for-future-use).

Rerun the server using `dotnet run --urls http://localhost:8080`.

You can test this API by accessing `http://localhost:8080/negotiate?id=user1` and it gives you the full url of the Azure Web PubSub with an access token.

In Azure Web PubSub, when there are certain activities happen at client side (for example a client is connecting, connected, disconnected, or a client is sending messages), service sends notifications to server so it can react to these events.

Events are delivered to server in the form of Webhook. Webhook is served and exposed by the application server and registered at the Azure Web PubSub service side. The service invokes the webhooks whenever an event happens.

Azure Web PubSub follows [CloudEvents](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-cloud-events) to describe the event data.

Below we handle `connected` system events when a client is connected and handle `message` user events when a client is sending messages to build the chat app.

*   [C#](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_4_csharp)
*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_4_javascript)
*   [Java](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_4_java)
*   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_4_python)

The Web PubSub SDK for AspNetCore `Microsoft.Azure.WebPubSub.AspNetCore` we installed in previous step could also help parse and process the CloudEvents requests.

First, add event handlers before `app.Run()`. Specify the endpoint path for the events, let's say `/eventhandler`.

```
app.MapWebPubSubHub<Sample_ChatApp>("/eventhandler/{*path}");
app.Run();
```

Now, inside the class `Sample_ChatApp` we created in previous step, add a constructor to work with `WebPubSubServiceClient<Sample_ChatApp>` that we use to invoke the Web PubSub service. And `OnConnectedAsync()` to respond when `connected` event is triggered, `OnMessageReceivedAsync()` to handle messages from the client.

```
sealed class Sample_ChatApp : WebPubSubHub
{
    private readonly WebPubSubServiceClient<Sample_ChatApp> _serviceClient;

    public Sample_ChatApp(WebPubSubServiceClient<Sample_ChatApp> serviceClient)
    {
        _serviceClient = serviceClient;
    }

    public override async Task OnConnectedAsync(ConnectedEventRequest request)
    {
        Console.WriteLine($"[SYSTEM] {request.ConnectionContext.UserId} joined.");
    }

    public override async ValueTask<UserEventResponse> OnMessageReceivedAsync(UserEventRequest request, CancellationToken cancellationToken)
    {
        await _serviceClient.SendToAllAsync(RequestContent.Create(
        new
        {
            from = request.ConnectionContext.UserId,
            message = request.Data.ToString()
        }),
        ContentType.ApplicationJson);

        return new UserEventResponse();
    }
}
```

In the above code, we use the service client to broadcast a notification message in JSON format to all of whom is joined with `SendToAllAsync`.

Now let's update `index.html` to add the logic to connect, send message, and display received messages in the page.

```
<html>
  <body>
    <h1>Azure Web PubSub Chat</h1>
    <input id="message" placeholder="Type to chat...">
    <div id="messages"></div>
    <script>
      (async function () {
        let id = prompt('Please input your user name');
        let res = await fetch(`/negotiate?id=${id}`);
        let data = await res.json();
        let ws = new WebSocket(data.url);
        ws.onopen = () => console.log('connected');

        let messages = document.querySelector('#messages');
        
        ws.onmessage = event => {
          let m = document.createElement('p');
          let data = JSON.parse(event.data);
          m.innerText = `[${data.type || ''}${data.from || ''}] ${data.message}`;
          messages.appendChild(m);
        };

        let message = document.querySelector('#message');
        message.addEventListener('keypress', e => {
          if (e.charCode !== 13) return;
          ws.send(message.value);
          message.value = '';
        });
      })();
    </script>
  </body>

</html>
```

You can see in the above code we connect use the native WebSocket API in the browser, and use `WebSocket.send()` to send message and `WebSocket.onmessage` to listen to received messages.

You could also use [Client SDKs](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-client-sdk-javascript) to connect to the service, which empowers you with auto reconnect, error handling, and more.

There's now one step left for the chat to work. Let's configure what events we care about and where to send the events to in the Web PubSub service.

We set the event handler in the Web PubSub service to tell the service where to send the events to.

When the web server runs locally, how the Web PubSub service invokes the localhost if it have no internet accessible endpoint? There are usually two ways. One is to expose localhost to public using some general tunnel tool, and the other is to use [awps-tunnel](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/howto-web-pubsub-tunnel-tool) to tunnel the traffic from Web PubSub service through the tool to your local server.

In this section, we use Azure CLI to set the event handlers and use [awps-tunnel](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/howto-web-pubsub-tunnel-tool) to route traffic to localhost.

We set the URL template to use `tunnel` scheme so that Web PubSub routes messages through the `awps-tunnel`'s tunnel connection. Event handlers can be set from either the portal or the CLI as [described in this article](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/howto-develop-eventhandler#configure-event-handler), here we set it through CLI. Since we listen events in path `/eventhandler` as the previous step sets, we set the url template to `tunnel:///eventhandler`.

Use the Azure CLI [az webpubsub hub create](https://learn.microsoft.com/en-us/cli/azure/webpubsub/hub#az-webpubsub-hub-create) command to create the event handler settings for the `Sample_ChatApp` hub.

Important

Replace <your-unique-resource-name> with the name of your Web PubSub resource created from the previous steps.

```
az webpubsub hub create -n "<your-unique-resource-name>" -g "myResourceGroup" --hub-name "Sample_ChatApp" --event-handler url-template="tunnel:///eventhandler" user-event-pattern="*" system-event="connected"
```

The tool runs on [Node.js](https://nodejs.org/) version 16 or higher.

```
npm install -g @azure/web-pubsub-tunnel-tool
```

```
export WebPubSubConnectionString="<your connection string>"
awps-tunnel run --hub Sample_ChatApp --upstream http://localhost:8080
```

Now everything is set. Let's run the web server and play with the chat app in action.

*   [C#](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_5_csharp)
*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_5_javascript)
*   [Java](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_5_java)
*   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_5_python)

Now run the server using `dotnet run --urls http://localhost:8080`.

The complete code sample of this tutorial can be found [here](https://github.com/Azure/azure-webpubsub/tree/main/samples/csharp/chatapp/).

Open `http://localhost:8080/index.html`. You can input your user name and start chatting.

In previous sections, we demonstrate how to use [negotiate](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#add-negotiate-endpoint) endpoint to return the Web PubSub service URL and the JWT access token for the clients to connect to Web PubSub service. In some cases, for example, edge devices that have limited resources, clients might prefer direct connect to Web PubSub resources. In such cases, you can configure `connect` event handler to lazy auth the clients, assign user ID to the clients, specify the groups the clients join once they connect, configure the permissions the clients have and WebSocket subprotocol as the WebSocket response to the client, etc. Details please refer to [connect event handler spec](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-cloud-events#connect).

Now let's use `connect` event handler to achieve the similar as what the [negotiate](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#add-negotiate-endpoint) section does.

First let's update hub settings to also include `connect` event handler, we need to also allow anonymous connect so that clients without JWT access token can connect to the service.

Use the Azure CLI [az webpubsub hub update](https://learn.microsoft.com/en-us/cli/azure/webpubsub/hub#az-webpubsub-hub-update) command to create the event handler settings for the `Sample_ChatApp` hub.

Important

Replace <your-unique-resource-name> with the name of your Web PubSub resource created from the previous steps.

```
az webpubsub hub update -n "<your-unique-resource-name>" -g "myResourceGroup" --hub-name "Sample_ChatApp" --allow-anonymous true --event-handler url-template="tunnel:///eventhandler" user-event-pattern="*" system-event="connected" system-event="connect"
```

Now let's update upstream logic to handle connect event. We could also remove the negotiate endpoint now.

As similar to what we do in negotiate endpoint as demo purpose, we also read id from the query parameters. In connect event, the original client query is preserved in connect event request body.

*   [C#](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_6_csharp)
*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_6_javascript)
*   [Java](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_6_java)
*   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#tabpanel_6_python)

Inside the class `Sample_ChatApp`, override `OnConnectAsync()` to handle `connect` event:

```
sealed class Sample_ChatApp : WebPubSubHub
{
    private readonly WebPubSubServiceClient<Sample_ChatApp> _serviceClient;

    public Sample_ChatApp(WebPubSubServiceClient<Sample_ChatApp> serviceClient)
    {
        _serviceClient = serviceClient;
    }

    public override ValueTask<ConnectEventResponse> OnConnectAsync(ConnectEventRequest request, CancellationToken cancellationToken)
    {
        if (request.Query.TryGetValue("id", out var id))
        {
            return new ValueTask<ConnectEventResponse>(request.CreateResponse(userId: id.FirstOrDefault(), null, null, null));
        }

        // The SDK catches this exception and returns 401 to the caller
        throw new UnauthorizedAccessException("Request missing id");
    }

    public override async Task OnConnectedAsync(ConnectedEventRequest request)
    {
        Console.WriteLine($"[SYSTEM] {request.ConnectionContext.UserId} joined.");
    }

    public override async ValueTask<UserEventResponse> OnMessageReceivedAsync(UserEventRequest request, CancellationToken cancellationToken)
    {
        await _serviceClient.SendToAllAsync(RequestContent.Create(
        new
        {
            from = request.ConnectionContext.UserId,
            message = request.Data.ToString()
        }),
        ContentType.ApplicationJson);

        return new UserEventResponse();
    }
}
```

Now let's update the web page to direct connect to Web PubSub service. One thing to mention is that now for demo purpose the Web PubSub service endpoint is hard-coded into the client code, please update the service hostname `<the host name of your service>` in the below html with the value from your own service. It might be still useful to fetch the Web PubSub service endpoint value from your server, it gives you more flexibility and controllability to where the client connects to.

```
<html>
  <body>
    <h1>Azure Web PubSub Chat</h1>
    <input id="message" placeholder="Type to chat...">
    <div id="messages"></div>
    <script>
      (async function () {
        // sample host: mock.webpubsub.azure.com
        let hostname = "<the host name of your service>";
        let id = prompt('Please input your user name');
        let ws = new WebSocket(`wss://${hostname}/client/hubs/Sample_ChatApp?id=${id}`);
        ws.onopen = () => console.log('connected');

        let messages = document.querySelector('#messages');
        
        ws.onmessage = event => {
          let m = document.createElement('p');
          let data = JSON.parse(event.data);
          m.innerText = `[${data.type || ''}${data.from || ''}] ${data.message}`;
          messages.appendChild(m);
        };

        let message = document.querySelector('#message');
        message.addEventListener('keypress', e => {
          if (e.charCode !== 13) return;
          ws.send(message.value);
          message.value = '';
        });
      })();
    </script>
  </body>

</html>
```

Now [rerun the server](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#run-the-web-server) and visit the web page following the instructions before. If you've stopped `awps-tunnel`, please also [rerun the tunnel tool](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat#run-awps-tunnel-locally).

This tutorial provides you with a basic idea of how the event system works in Azure Web PubSub service.

Check other tutorials to further dive into how to use the service.
