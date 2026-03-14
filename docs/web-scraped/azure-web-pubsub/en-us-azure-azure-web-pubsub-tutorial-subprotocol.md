# Source: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol

Title: Tutorial - Publish and subscribe messages between WebSocket clients using subprotocol in Azure Web PubSub service

URL Source: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol

Markdown Content:
In [Build a chat app tutorial](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat), you learned how to use WebSocket APIs to send and receive data with Azure Web PubSub. You can see there's no protocol needed when client is communicating with the service. For example, you can send any type of data using `WebSocket.send()`, and the server receives it just as it is. WebSocket APIs process is easy to use, but the functionality is limited. For example, you can't specify the event name when sending the event to your server, or publish message to other clients instead of sending it to your server. In this tutorial, you learn how to use subprotocol to extend the functionality of client.

In this tutorial, you learn how to:

*   Create a Web PubSub service instance
*   Generate the full URL to establish the WebSocket connection
*   Publish messages between WebSocket clients using subprotocol

If you don't have an Azure account, create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.

*   Use the Bash environment in [Azure Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/overview). For more information, see [Get started with Azure Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/quickstart).

[![Image 1](https://learn.microsoft.com/en-us/azure/reusable-content/azure-cli/media/hdi-launch-cloud-shell.png)](https://shell.azure.com/)

*   If you prefer to run CLI reference commands locally, [install](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) the Azure CLI. If you're running on Windows or macOS, consider running Azure CLI in a Docker container. For more information, see [How to run the Azure CLI in a Docker container](https://learn.microsoft.com/en-us/cli/azure/run-azure-cli-docker).

    *   If you're using a local installation, sign in to the Azure CLI by using the [az login](https://learn.microsoft.com/en-us/cli/azure/reference-index#az-login) command. To finish the authentication process, follow the steps displayed in your terminal. For other sign-in options, see [Authenticate to Azure using Azure CLI](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli).

    *   When you're prompted, install the Azure CLI extension on first use. For more information about extensions, see [Use and manage extensions with the Azure CLI](https://learn.microsoft.com/en-us/cli/azure/azure-cli-extensions-overview).

    *   Run [az version](https://learn.microsoft.com/en-us/cli/azure/reference-index?#az-version) to find the version and dependent libraries that are installed. To upgrade to the latest version, run [az upgrade](https://learn.microsoft.com/en-us/cli/azure/reference-index?#az-upgrade).

*   This setup requires version 2.22.0 or higher of the Azure CLI. If using Azure Cloud Shell, the latest version is already installed.

Important

Raw connection strings appear in this article for demonstration purposes only.

A connection string includes the authorization information required for your application to access Azure Web PubSub service. The access key inside the connection string is similar to a root password for your service. In production environments, always protect your access keys. Use Azure Key Vault to manage and rotate your keys securely and [secure your connection with `WebPubSubServiceClient`](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/howto-create-serviceclient-with-net-and-azure-identity).

Avoid distributing access keys to other users, hard-coding them, or saving them anywhere in plain text that is accessible to others. Rotate your keys if you believe they may have been compromised.

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

Raw connection strings appear in this article for demonstration purposes only. In production environments, always protect your access keys. Use Azure Key Vault to manage and rotate your keys securely and [secure your connection with `WebPubSubServiceClient`](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/howto-create-serviceclient-with-net-and-azure-identity).

Use the Azure CLI [az webpubsub key](https://learn.microsoft.com/en-us/cli/azure/webpubsub#az-webpubsub-key) command to get the **ConnectionString** of the service. Replace the `<your-unique-resource-name>` placeholder with the name of your Azure Web PubSub instance.

```
az webpubsub key show --resource-group myResourceGroup --name <your-unique-resource-name> --query primaryConnectionString --output tsv
```

Copy the connection string to use later.

Copy the fetched **ConnectionString** and use later in this tutorial as the value of `<connection_string>`.

*   [C#](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_1_csharp)
*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_1_javascript)
*   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_1_python)
*   [Java](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_1_java)

*   [ASP.NET Core 3.1 or above](https://learn.microsoft.com/en-us/aspnet/core)

The client can start a WebSocket connection using a specific [subprotocol](https://datatracker.ietf.org/doc/html/rfc6455#section-1.9). Azure Web PubSub service supports a subprotocol called `json.webpubsub.azure.v1` to empower the clients to do publish/subscribe directly through the Web PubSub service instead of a round trip to the upstream server. Check [Azure Web PubSub supported JSON WebSocket subprotocol](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-json-webpubsub-subprotocol) for details about the subprotocol.

> If you use other protocol names, they will be ignored by the service and passthrough to server in the connect event handler, so you can build your own protocols.

Now let's create a web application using the `json.webpubsub.azure.v1` subprotocol.

1.   Install dependencies

    *   [C#](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_2_csharp)
    *   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_2_javascript)
    *   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_2_python)
    *   [Java](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_2_java)

```
mkdir logstream
cd logstream
dotnet new web
dotnet add package Microsoft.Extensions.Azure
dotnet add package Azure.Messaging.WebPubSub
```

2.   Create the server-side to host the `/negotiate` API and web page.

    *   [C#](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_3_csharp)
    *   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_3_javascript)
    *   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_3_python)
    *   [Java](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_3_java)

Update `Program.cs` with the below code.

    *   Use `AddAzureClients` to add the service client, and read the connection string from configuration.
    *   Add `app.UseStaticFiles();` before `app.Run();` to support static files.
    *   And update `app.MapGet` to generate the client access token with `/negotiate` requests.

```
using Azure.Messaging.WebPubSub;
using Microsoft.Extensions.Azure;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddAzureClients(s =>
{
    s.AddWebPubSubServiceClient(builder.Configuration["Azure:WebPubSub:ConnectionString"], "stream");
});

var app = builder.Build();
app.UseStaticFiles();
app.MapGet("/negotiate", async context =>
{
    var service = context.RequestServices.GetRequiredService<WebPubSubServiceClient>();
    var response = new
    {
        url = service.GetClientAccessUri(roles: new string[] { "webpubsub.sendToGroup.stream", "webpubsub.joinLeaveGroup.stream" }).AbsoluteUri
    };
    await context.Response.WriteAsJsonAsync(response);
});

app.Run();
```

3.   Create the web page

    *   [C#](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_4_csharp)
    *   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_4_javascript)
    *   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_4_python)
    *   [Java](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_4_java)

Create an HTML page with below content and save it as `wwwroot/index.html`:

```
<html>
  <body>
    <div id="output"></div>
    <script>
      (async function () {
        let res = await fetch('/negotiate')
        let data = await res.json();
        let ws = new WebSocket(data.url, 'json.webpubsub.azure.v1');
        ws.onopen = () => {
          console.log('connected');
        };

        let output = document.querySelector('#output');
        ws.onmessage = event => {
          let d = document.createElement('p');
          d.innerText = event.data;
          output.appendChild(d);
        };
      })();
    </script>
  </body>
</html>
```

The code above connects to the service and print any message received to the page. The main change is that we specify the subprotocol when creating the WebSocket connection.

4.   Run the server

    *   [C#](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_5_csharp)
    *   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_5_javascript)
    *   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_5_python)
    *   [Java](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_5_java)

We use [Secret Manager](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets#secret-manager) tool for .NET Core to set the connection string. Run the below command, replacing `<connection_string>` with the one fetched in [previous step](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#get-the-connectionstring-for-future-use), and open http://localhost:5000/index.html in browser:

```
dotnet user-secrets init
dotnet user-secrets set Azure:WebPubSub:ConnectionString "<connection-string>"
dotnet run
```

If you're using Chrome, you can press F12 or right-click ->**Inspect** ->**Developer Tools**, and select the **Network** tab. Load the web page, and you can see the WebSocket connection is established. Select to inspect the WebSocket connection, you can see below `connected` event message is received in client. You can see that you can get the `connectionId` generated for this client.

```
{"type":"system","event":"connected","userId":null,"connectionId":"<the_connection_id>"}
```

You can see that with the help of subprotocol, you can get some metadata of the connection when the connection is `connected`.

The client now receives a JSON message instead of a plain text. JSON message contains more information such as type and source of the message. So you can use this information to do more processing to the message (for example, display the message in a different style if it's from a different source), which you can find in later sections.

In the [Build a chat app](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-build-chat) tutorial, when client sends a message through WebSocket connection to the Web PubSub service, the service triggers a user event at your server side. With subprotocol, client has more functionalities by sending a JSON message. For example, you can publish messages directly from client through the Web PubSub service to other clients.

This is useful if you want to stream a large amount of data to other clients in real time. Let's use this feature to build a log streaming application, which can stream console logs to browser in real time.

1.   Creating the streaming program

    *   [C#](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_6_csharp)
    *   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_6_javascript)
    *   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_6_python)
    *   [Java](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_6_java)

Create a `stream` program:

```
mkdir stream
cd stream
dotnet new console
```

Update `Program.cs` with the following content:

```
using System;
using System.Net.Http;
using System.Net.WebSockets;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace stream
{
    class Program
    {
        private static readonly HttpClient http = new HttpClient();
        static async Task Main(string[] args)
        {
            // Get client url from remote
            var stream = await http.GetStreamAsync("http://localhost:5000/negotiate");
            var url = (await JsonSerializer.DeserializeAsync<ClientToken>(stream)).url;
            var client = new ClientWebSocket();
            client.Options.AddSubProtocol("json.webpubsub.azure.v1");

            await client.ConnectAsync(new Uri(url), default);

            Console.WriteLine("Connected.");
            var streaming = Console.ReadLine();
            while (streaming != null)
            {
                if (!string.IsNullOrEmpty(streaming))
                {
                    var message = JsonSerializer.Serialize(new
                    {
                        type = "sendToGroup",
                        group = "stream",
                        data = streaming + Environment.NewLine,
                    });
                    Console.WriteLine("Sending " + message);
                    await client.SendAsync(Encoding.UTF8.GetBytes(message), WebSocketMessageType.Text, true, default);
                }

                streaming = Console.ReadLine();
            }

            await client.CloseAsync(WebSocketCloseStatus.NormalClosure, null, default);
        }

        private sealed class ClientToken
        {
            public string url { get; set; }
        }
    }
}
```

You can see there's a new concept "group" here. Group is logical concept in a hub where you can publish message to a group of connections. In a hub, you can have multiple groups and one client can subscribe to multiple groups at the same time. When using subprotocol, you can only publish to a group instead of broadcasting to the whole hub. For details about the terms, check the [basic concepts](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/key-concepts).

2.   Since we use group here, we also need to update the web page `index.html` to join the group when the WebSocket connection is established inside `ws.onopen` callback.

```
let ackId = 0;
ws.onopen = () => {
  console.log('connected');
  ws.send(JSON.stringify({
    type: 'joinGroup',
    group: 'stream',
    ackId: ++ackId
  }));
};
```

You can see client joins the group by sending a message in `joinGroup` type.

3.   Also update the `ws.onmessage` callback logic slightly to parse the JSON response and print the messages only from `stream` group so that it acts as live stream printer.

```
ws.onmessage = event => {
  let message = JSON.parse(event.data);
  if (message.type === 'message' && message.group === 'stream') {
    let d = document.createElement('span');
    d.innerText = message.data;
    output.appendChild(d);
    window.scrollTo(0, document.body.scrollHeight);
  }
};
```
4.   For security consideration, by default a client can't publish or subscribe to a group by itself. So you noticed that we set `roles` to the client when generating the token:

    *   [C#](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_7_csharp)
    *   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_7_javascript)
    *   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_7_python)
    *   [Java](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_7_java)

Set the `roles` when `GenerateClientAccessUri` in `Startup.cs` like below:

```
service.GenerateClientAccessUri(roles: new string[] { "webpubsub.sendToGroup.stream", "webpubsub.joinLeaveGroup.stream" })
```

5.   Finally also apply some style to `index.html` so it displays nicely.

```
<html>

  <head>
    <style>
      #output {
        white-space: pre;
        font-family: monospace;
      }
    </style>
  </head>
```

Now run below code and type any text and they're displayed in the browser in real time:

*   [C#](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_8_csharp)
*   [JavaScript](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_8_javascript)
*   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_8_python)
*   [Java](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-subprotocol#tabpanel_8_java)

```
ls -R | dotnet run

# Or call `dir /s /b | dotnet run` when you are using CMD under Windows
```

Or you make it slower so you can see the data is streamed to browser in real time:

```
for i in $(ls -R); do echo $i; sleep 0.1; done | dotnet run
```

The complete code sample of this tutorial can be found [here](https://github.com/Azure/azure-webpubsub/tree/main/samples/csharp/logstream/).

This tutorial provides you with a basic idea of how to connect to the Web PubSub service and how to publish messages to the connected clients using subprotocol.

Check other tutorials to further dive into how to use the service.
