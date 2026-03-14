# Source: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification

Title: Tutorial - Create a serverless notification app using Azure Web PubSub service and Azure Functions

URL Source: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification

Markdown Content:
The Azure Web PubSub service helps you build real-time messaging web applications using WebSockets. Azure Functions is a serverless platform that lets you run your code without managing any infrastructure. In this tutorial, you learn how to use Azure Web PubSub service and Azure Functions to build a serverless application with real-time messaging under notification scenarios.

In this tutorial, you learn how to:

*   Build a serverless notification app
*   Work with Web PubSub function input and output bindings
*   Run the sample functions locally
*   Deploy the function to Azure Function App

Important

Raw connection strings appear in this article for demonstration purposes only.

A connection string includes the authorization information required for your application to access Azure Web PubSub service. The access key inside the connection string is similar to a root password for your service. In production environments, always protect your access keys. Use Azure Key Vault to manage and rotate your keys securely and [secure your connection with `WebPubSubServiceClient`](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/howto-create-serviceclient-with-net-and-azure-identity).

Avoid distributing access keys to other users, hard-coding them, or saving them anywhere in plain text that is accessible to others. Rotate your keys if you believe they may have been compromised.

*   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_1_javascript-v4)
*   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_1_javascript-v3)
*   [C# in-process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_1_csharp-in-process)
*   [C# isolated process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_1_csharp-isolated-process)
*   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_1_python)

*   A code editor, such as [Visual Studio Code](https://code.visualstudio.com/)

*   [Node.js](https://nodejs.org/en/download/package-manager/), version 18.x or above.

*   [Azure Functions Core Tools](https://github.com/Azure/azure-functions-core-tools#installing) (V4 or higher preferred) to run Azure Function apps locally and deploy to Azure.

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

1.   Make sure you have [Azure Functions Core Tools](https://github.com/Azure/azure-functions-core-tools#installing) installed. Now, create an empty directory for the project. Run command under this working directory. Use one of the given options below.

    *   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_2_javascript-v4)
    *   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_2_javascript-v3)
    *   [C# in-process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_2_csharp-in-process)
    *   [C# isolated process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_2_csharp-isolated-process)
    *   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_2_python)

```
func init --worker-runtime javascript --model V4
```

2.   Follow the steps to install `Microsoft.Azure.WebJobs.Extensions.WebPubSub`.

    *   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_3_javascript-v4)
    *   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_3_javascript-v3)
    *   [C# in-process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_3_csharp-in-process)
    *   [C# isolated process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_3_csharp-isolated-process)
    *   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_3_python)

Confirm or update `host.json`'s extensionBundle to version _4.*_ or later to get Web PubSub support. For updating the `host.json`, open the file in editor, and then replace the existing version extensionBundle to version _4.*_ or later.

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

    *   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_4_javascript-v4)
    *   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_4_javascript-v3)
    *   [C# in-process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_4_csharp-in-process)
    *   [C# isolated process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_4_csharp-isolated-process)
    *   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_4_python)

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

    *   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_5_javascript-v4)
    *   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_5_javascript-v3)
    *   [C# in-process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_5_csharp-in-process)
    *   [C# isolated process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_5_csharp-isolated-process)
    *   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_5_python)

    *   Update `src/functions/negotiate.js` and copy following codes. 
```
const { app, input } = require('@azure/functions');

const connection = input.generic({
    type: 'webPubSubConnection',
    name: 'connection',
    hub: 'notification'
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

5.   Create a `notification` function to generate notifications with `TimerTrigger`.

```
func new -n notification -t TimerTrigger
```

    *   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_6_javascript-v4)
    *   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_6_javascript-v3)
    *   [C# in-process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_6_csharp-in-process)
    *   [C# isolated process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_6_csharp-isolated-process)
    *   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_6_python)

    *   Update `src/functions/notification.js` and copy following codes. 
```
const { app, output } = require('@azure/functions');

const wpsAction = output.generic({
    type: 'webPubSub',
    name: 'action',
    hub: 'notification'
});

app.timer('notification', {
    schedule: "*/10 * * * * *",
    extraOutputs: [wpsAction],
    handler: (myTimer, context) => {
        context.extraOutputs.set(wpsAction, {
            actionName: 'sendToAll',
            data: `[DateTime: ${new Date()}] Temperature: ${getValue(22, 1)}\xB0C, Humidity: ${getValue(40, 2)}%`,
            dataType: 'text',
        });
    },
});

function getValue(baseNum, floatNum) {
    return (baseNum + 2 * floatNum * (Math.random() - 0.5)).toFixed(3);
}
```

6.   Add the client single page `index.html` in the project root folder and copy content.

```
<html>
    <body>
    <h1>Azure Web PubSub Notification</h1>
    <div id="messages"></div>
    <script>
        (async function () {
            let messages = document.querySelector('#messages');
            let res = await fetch(`${window.location.origin}/api/negotiate`);
            let url = await res.json();
            let ws = new WebSocket(url.url);
            ws.onopen = () => console.log('connected');

            ws.onmessage = event => {
                let m = document.createElement('p');
                m.innerText = event.data;
                messages.appendChild(m);
            };
        })();
    </script>
    </body>
</html>
```

    *   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_7_javascript-v4)
    *   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_7_javascript-v3)
    *   [C# in-process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_7_csharp-in-process)
    *   [C# isolated process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_7_csharp-isolated-process)
    *   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_7_python)

7.   Configure and run the Azure Function app

Raw connection strings appear in this article for demonstration purposes only. In production environments, always protect your access keys. Use Azure Key Vault to manage and rotate your keys securely and [secure your connection with `WebPubSubServiceClient`](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/howto-create-serviceclient-with-net-and-azure-identity).

    *   In the browser, open the **Azure portal** and confirm the Web PubSub Service instance you deployed earlier was successfully created. Navigate to the instance.
    *   Select **Keys** and copy out the connection string.

![Image 3: Screenshot of copying the Web PubSub connection string.](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/media/quickstart-serverless/copy-connection-string.png)

Run command in the function folder to set the service connection string. Replace `<connection-string>` with your value as needed.

```
func settings add WebPubSubConnectionString "<connection-string>"
```

Note

`TimerTrigger` used in the sample has dependency on Azure Storage, but you can use local storage emulator when the Function is running locally. If you got some error like `There was an error performing a read operation on the Blob Storage Secret Repository. Please ensure the 'AzureWebJobsStorage' connection string is valid.`, you'll need to download and enable [Storage Emulator](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-emulator).

Now you're able to run your local function by command.

```
func start --port 7071
```

And checking the running logs, you can visit your local host static page by visiting: `http://localhost:7071/api/index`.

Note

Some browsers automatically redirect to `https` that leads to wrong url. Suggest to use `Edge` and double check the url if rendering is not success.

Before you can deploy your function code to Azure, you need to create three resources:

*   A resource group, which is a logical container for related resources.
*   A storage account, which is used to maintain state and other information about your functions.
*   A function app, which provides the environment for executing your function code. A function app maps to your local function project and lets you group functions as a logical unit for easier management, deployment and sharing of resources.

Use the following commands to create these items.

1.   Sign in to Azure:

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

    *   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_8_javascript-v4)
    *   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_8_javascript-v3)
    *   [C# in-process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_8_csharp-in-process)
    *   [C# isolated process](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_8_csharp-isolated-process)
    *   [Python](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/tutorial-serverless-notification#tabpanel_8_python)

```
az functionapp create --resource-group WebPubSubFunction --consumption-plan-location <REGION> --runtime node --runtime-version 18 --functions-version 4 --name <FUNCIONAPP_NAME> --storage-account <STORAGE_NAME>
```

5.   Deploy the function project to Azure:

Once you create your function app in Azure, you're now ready to deploy your local functions project by using the [func azure functionapp publish](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local) command.

```
func azure functionapp publish <FUNCIONAPP_NAME> --publish-local-settings
```
Note

Here we are deploying local settings `local.settings.json` together with command parameter `--publish-local-settings`. If you're using Microsoft Azure Storage Emulator, you can type `no` to skip overwriting this value on Azure following the prompt message: `App setting AzureWebJobsStorage is different between azure and local.settings.json, Would you like to overwrite value in azure? [yes/no/show]`. Besides, you can update Function App settings in **Azure portal** ->**Settings** ->**Configuration**. 
6.   Now you can check your site from Azure Function App by navigating to URL: `https://<FUNCIONAPP_NAME>.azurewebsites.net/api/index`.

If you're not going to continue to use this app, delete all resources created by this doc with the following steps so you don't incur any charges:

1.   In the Azure portal, select **Resource groups** on the far left, and then select the resource group you created. Use the search box to find the resource group by its name instead.

2.   In the window that opens, select the resource group, and then select **Delete resource group**.

3.   In the new window, type the name of the resource group to delete, and then select **Delete**.

In this quickstart, you learned how to run a serverless chat application. Now, you could start to build your own application.
