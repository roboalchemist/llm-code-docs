# Source: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless

Title: Tutorial - Build a serverless real-time chat app with client authentication

URL Source: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless

Markdown Content:
Tutorial: Create a serverless real-time chat app with Azure Functions and Azure Web PubSub service
--------------------------------------------------------------------------------------------------

The Azure Web PubSub service helps you build real-time messaging web applications using WebSockets and the publish-subscribe pattern easily. Azure Functions is a serverless platform that lets you run your code without managing any infrastructure. In this tutorial, you learn how to use Azure Web PubSub service and Azure Functions to build a serverless application with real-time messaging and the publish-subscribe pattern.

In this tutorial, you learn how to:

*   Build a serverless real-time chat app
*   Work with Web PubSub function trigger bindings and output bindings
*   Deploy the function to Azure Function App
*   Configure Azure Authentication
*   Configure Web PubSub Event Handler to route events and messages to the application

Important

Raw connection strings appear in this article for demonstration purposes only.

A connection string includes the authorization information required for your application to access Azure Web PubSub service. The access key inside the connection string is similar to a root password for your service. In production environments, always protect your access keys. Use Azure Key Vault to manage and rotate your keys securely and [secure your connection with `WebPubSubServiceClient`](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/howto-create-serviceclient-with-net-and-azure-identity).

Avoid distributing access keys to other users, hard-coding them, or saving them anywhere in plain text that is accessible to others. Rotate your keys if you believe they may have been compromised.

*   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_1_javascript-v4)
*   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_1_javascript-v3)
*   [C# in-process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_1_csharp-in-process)
*   [C# isolated process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_1_csharp-isolated-process)
*   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_1_python)

*   A code editor, such as [Visual Studio Code](https://code.visualstudio.com/)

*   [Node.js](https://nodejs.org/en/download/package-manager/), version 18.x or above.

*   [Azure Functions Core Tools](https://github.com/Azure/azure-functions-core-tools#installing) (v4 or higher preferred) to run Azure Function apps locally and deploy to Azure.

*   The [Azure CLI](https://learn.microsoft.com/en-us/cli/azure) to manage Azure resources.

If you don't have an Azure account, create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.

Sign in to the Azure portal at [https://portal.azure.com/](https://portal.azure.com/) with your Azure account.

Your application will connect to a Web PubSub service instance in Azure.

1.   Select the New button found on the upper left-hand corner of the Azure portal. In the New screen, type _Web PubSub_ in the search box and press enter. (You could also search the Azure Web PubSub from the `Web` category.)

![Image 1: Screenshot of searching the Azure Web PubSub in portal.](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/media/create-instance-portal/search-web-pubsub-in-portal.png)

2.   Select **Web PubSub** from the search results, then select **Create**.

3.   Enter the following settings.

| Setting | Suggested value | Description |
| --- | --- | --- |
| **Resource name** | Globally unique name | The globally unique Name that identifies your new Web PubSub service instance. Valid characters are `a-z`, `A-Z`, `0-9`, and `-`. |
| **Subscription** | Your subscription | The Azure subscription under which this new Web PubSub service instance is created. |
| **[Resource Group](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview)** | myResourceGroup | Name for the new resource group in which to create your Web PubSub service instance. |
| **Location** | West US | Choose a [region](https://azure.microsoft.com/regions/) near you. |
| **Pricing tier** | Free | You can first try Azure Web PubSub service for free. Learn more details about [Azure Web PubSub service pricing tiers](https://azure.microsoft.com/pricing/details/web-pubsub/) |
| **Unit count** | - | Unit count specifies how many connections your Web PubSub service instance can accept. Each unit supports 1,000 concurrent connections at most. It is only configurable in the Standard tier. | 
![Image 2: Screenshot of creating the Azure Web PubSub instance in portal.](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/media/howto-develop-create-instance/create-web-pubsub-instance-in-portal.png)

4.   Select **Create** to start deploying the Web PubSub service instance.

1.   Make sure you have [Azure Functions Core Tools](https://github.com/Azure/azure-functions-core-tools#installing) installed. And then create an empty directory for the project. Run command under this working directory.

    *   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_2_javascript-v4)
    *   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_2_javascript-v3)
    *   [C# in-process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_2_csharp-in-process)
    *   [C# isolated process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_2_csharp-isolated-process)
    *   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_2_python)

```
func init --worker-runtime javascript --model V4
```

2.   Install `Microsoft.Azure.WebJobs.Extensions.WebPubSub`.

    *   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_3_javascript-v4)
    *   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_3_javascript-v3)
    *   [C# in-process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_3_csharp-in-process)
    *   [C# isolated process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_3_csharp-isolated-process)
    *   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_3_python)

Confirm and update `host.json`'s extensionBundle to version _4.*_ or later to get Web PubSub support.

```
{
  "extensionBundle": {
    "id": "Microsoft.Azure.Functions.ExtensionBundle",
    "version": "[4.*, 5.0.0)"
  }
}
```

3.   Create an `index` function to read and host a static web page for clients.

```
func new -n index -t HttpTrigger
```

    *   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_4_javascript-v4)
    *   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_4_javascript-v3)
    *   [C# in-process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_4_csharp-in-process)
    *   [C# isolated process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_4_csharp-isolated-process)
    *   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_4_python)

    *   Update `src/functions/index.js` and copy following codes. 
```
const { app } = require('@azure/functions');
const { readFile } = require('fs/promises');

app.http('index', {
    methods: ['GET', 'POST'],
    authLevel: 'anonymous',
    handler: async (context) => {
        const content = await readFile('index.html', 'utf8', (err, data) => {
            if (err) {
                context.err(err)
                return
            }
        });

        return { 
            status: 200,
            headers: { 
                'Content-Type': 'text/html'
            }, 
            body: content, 
        };
    }
});
```

4.   Create a `negotiate` function to help clients get service connection url with access token.

```
func new -n negotiate -t HttpTrigger
```
Note

In this sample, we use [Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/app-service/configure-authentication-user-identities) user identity header `x-ms-client-principal-name` to retrieve `userId`. And this won't work in a local function. You can make it empty or change to other ways to get or generate `userId` when playing in local. For example, let client type a user name and pass it in query like `?user={$username}` when call `negotiate` function to get service connection url. And in the `negotiate` function, set `userId` with value `{query.user}`. 

    *   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_5_javascript-v4)
    *   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_5_javascript-v3)
    *   [C# in-process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_5_csharp-in-process)
    *   [C# isolated process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_5_csharp-isolated-process)
    *   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_5_python)

    *   Update `src/functions/negotiate` and copy following codes. 
```
const { app, input } = require('@azure/functions');

const connection = input.generic({
    type: 'webPubSubConnection',
    name: 'connection',
    userId: '{headers.x-ms-client-principal-name}',
    hub: 'simplechat'
});

app.http('negotiate', {
    methods: ['GET', 'POST'],
    authLevel: 'anonymous',
    extraInputs: [connection],
    handler: async (request, context) => {
        return { body: JSON.stringify(context.extraInputs.get('connection')) };
    },
});
```

5.   Create a `message` function to broadcast client messages through service.

```
func new -n message -t HttpTrigger
```

    *   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_6_javascript-v4)
    *   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_6_javascript-v3)
    *   [C# in-process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_6_csharp-in-process)
    *   [C# isolated process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_6_csharp-isolated-process)
    *   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_6_python)

    *   Update `src/functions/message.js` and copy following codes. 
```
const { app, output, trigger } = require('@azure/functions');

const wpsMsg = output.generic({
    type: 'webPubSub',
    name: 'actions',
    hub: 'simplechat',
});

const wpsTrigger = trigger.generic({
    type: 'webPubSubTrigger',
    name: 'request',
    hub: 'simplechat',
    eventName: 'message',
    eventType: 'user'
});

app.generic('message', {
    trigger: wpsTrigger,
    extraOutputs: [wpsMsg],
    handler: async (request, context) => {
        context.extraOutputs.set(wpsMsg, [{
            "actionName": "sendToAll",
            "data": `[${context.triggerMetadata.connectionContext.userId}] ${request.data}`,
            "dataType": request.dataType
        }]);

        return {
            data: "[SYSTEM] ack.",
            dataType: "text",
        };
    }
});
```

6.   Add the client single page `index.html` in the project root folder and copy content.

```
<html>
  <body>
    <h1>Azure Web PubSub Serverless Chat App</h1>
    <div id="login"></div>
    <p></p>
    <input id="message" placeholder="Type to chat..." />
    <div id="messages"></div>
    <script>
      (async function () {
        let authenticated = window.location.href.includes(
          "?authenticated=true"
        );
        if (!authenticated) {
          // auth
          let login = document.querySelector("#login");
          let link = document.createElement("a");
          link.href = `${window.location.origin}/.auth/login/aad?post_login_redirect_url=/api/index?authenticated=true`;
          link.text = "login";
          login.appendChild(link);
        } else {
          // negotiate
          let messages = document.querySelector("#messages");
          let res = await fetch(`${window.location.origin}/api/negotiate`, {
            credentials: "include",
          });
          let url = await res.json();
          // connect
          let ws = new WebSocket(url.url);
          ws.onopen = () => console.log("connected");
          ws.onmessage = (event) => {
            let m = document.createElement("p");
            m.innerText = event.data;
            messages.appendChild(m);
          };
          let message = document.querySelector("#message");
          message.addEventListener("keypress", (e) => {
            if (e.charCode !== 13) return;
            ws.send(message.value);
            message.value = "";
          });
        }
      })();
    </script>
  </body>
</html>
```

    *   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_7_javascript-v4)
    *   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_7_javascript-v3)
    *   [C# in-process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_7_csharp-in-process)
    *   [C# isolated process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_7_csharp-isolated-process)
    *   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_7_python)

Before you can deploy your function code to Azure, you need to create three resources:

*   A resource group, which is a logical container for related resources.
*   A storage account, which is used to maintain state and other information about your functions.
*   A function app, which provides the environment for executing your function code. A function app maps to your local function project and lets you group functions as a logical unit for easier management, deployment and sharing of resources.

Use the following commands to create these items.

1.   If you haven't done so already, sign in to Azure:

```
az login
```
2.   Create a resource group or you can skip by reusing the one of Azure Web PubSub service:

```
az group create -n WebPubSubFunction -l <REGION>
```
3.   Create a general-purpose storage account in your resource group and region:

```
az storage account create -n <STORAGE_NAME> -l <REGION> -g WebPubSubFunction
```
4.   Create the function app in Azure:

    *   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_8_javascript-v4)
    *   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_8_javascript-v3)
    *   [C# in-process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_8_csharp-in-process)
    *   [C# isolated process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_8_csharp-isolated-process)
    *   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-serverless#tabpanel_8_python)

```
az functionapp create --resource-group WebPubSubFunction --consumption-plan-location <REGION> --runtime node --runtime-version 18 --functions-version 4 --name <FUNCIONAPP_NAME> --storage-account <STORAGE_NAME>
```

5.   Deploy the function project to Azure:

After you have successfully created your function app in Azure, you're now ready to deploy your local functions project by using the [func azure functionapp publish](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local) command.

```
func azure functionapp publish <FUNCIONAPP_NAME>
```
6.   Configure the `WebPubSubConnectionString` for the function app:

Raw connection strings appear in this article for demonstration purposes only. In production environments, always protect your access keys. Use Azure Key Vault to manage and rotate your keys securely and [secure your connection with `WebPubSubServiceClient`](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/howto-create-serviceclient-with-net-and-azure-identity).

First, find your Web PubSub resource from **Azure portal** and copy out the connection string under **Keys**. Then, navigate to Function App settings in **Azure portal** ->**Settings** ->**Environment variables**. And add a new item under **App settings**, with name equals `WebPubSubConnectionString` and value is your Web PubSub resource connection string.

In this sample, we're using `WebPubSubTrigger` to listen to service upstream requests. So Web PubSub need to know the function's endpoint information in order to send target client requests. And Azure Function App requires a system key for security regarding extension-specific webhook methods. In the previous step after we deployed the Function App with `message` functions, we're able to get the system key.

Go to **Azure portal** -> Find your Function App resource ->**App keys** ->**System keys** ->**`webpubsub_extension`**. Copy out the value as `<APP_KEY>`.

![Image 3: Screenshot of get function system keys.](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/media/quickstart-serverless/func-keys.png)

Set `Event Handler` in Azure Web PubSub service. Go to **Azure portal** -> Find your Web PubSub resource ->**Settings**. Add a new hub settings mapping to the one function in use. Replace the `<FUNCTIONAPP_NAME>` and `<APP_KEY>` to yours.

*   Hub Name: `simplechat`
*   URL Template: **https://<FUNCTIONAPP_NAME>.azurewebsites.net/runtime/webhooks/webpubsub?code=<APP_KEY>**
*   User Event Pattern: *
*   System Events: -(No need to configure in this sample)

![Image 4: Screenshot of setting the event handler.](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/media/quickstart-serverless/set-event-handler.png)

Go to **Azure portal** -> Find your Function App resource ->**Authentication**. Click **`Add identity provider`**. Set **App Service authentication settings** to **Allow unauthenticated access**, so your client index page can be visited by anonymous users before redirect to authenticate. Then **Save**.

Here we choose `Microsoft` as identify provider, which uses `x-ms-client-principal-name` as `userId` in the `negotiate` function. Besides, you can configure other identity providers following the links, and don't forget update the `userId` value in `negotiate` function accordingly.

*   [Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/app-service/configure-authentication-provider-aad)
*   [Facebook](https://learn.microsoft.com/en-us/azure/app-service/configure-authentication-provider-facebook)
*   [Google](https://learn.microsoft.com/en-us/azure/app-service/configure-authentication-provider-google)
*   [X](https://learn.microsoft.com/en-us/azure/app-service/configure-authentication-provider-twitter)

Now you're able to test your page from your function app: `https://<FUNCTIONAPP_NAME>.azurewebsites.net/api/index`. See snapshot.

1.   Click `login` to auth yourself.
2.   Type message in the input box to chat.

In the message function, we broadcast caller's message to all clients and return caller with message `[SYSTEM] ack`. So we can know in sample chat snapshot, first four messages are from current client and last two messages are from another client.

![Image 5: Screenshot of chat sample.](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/media/quickstart-serverless/chat-sample.png)

If you're not going to continue to use this app, delete all resources created by this doc with the following steps so you don't incur any charges:

1.   In the Azure portal, select **Resource groups** on the far left, and then select the resource group you created. You may use the search box to find the resource group by its name instead.

2.   In the window that opens, select the resource group, and then select **Delete resource group**.

3.   In the new window, type the name of the resource group to delete, and then select **Delete**.

In this quickstart, you learned how to run a serverless chat application. Now, you could start to build your own application.
