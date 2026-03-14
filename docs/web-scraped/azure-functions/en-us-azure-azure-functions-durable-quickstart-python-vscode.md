# Source: https://learn.microsoft.com/en-us/azure/azure-functions/durable/quickstart-python-vscode

Title: Quickstart: Create a Python Durable Functions app - Azure Durable

URL Source: https://learn.microsoft.com/en-us/azure/azure-functions/durable/quickstart-python-vscode

Markdown Content:
Use Durable Functions, a feature of [Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview), to write stateful functions in a serverless environment. You install Durable Functions by installing the [Azure Functions extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions) in Visual Studio Code. The extension manages state, checkpoints, and restarts in your application.

In this quickstart, you use the Durable Functions extension in Visual Studio Code to locally create and test a "hello world" Durable Functions app in Azure Functions. The Durable Functions app orchestrates and chains together calls to other functions. Then, you publish the function code to Azure. The tools you use are available via the Visual Studio Code extension.

![Image 1: Screenshot of the running Durable Functions app in Azure.](https://learn.microsoft.com/en-us/azure/azure-functions/durable/media/quickstart-python-vscode/functions-vs-code-complete.png)

Note

This quickstart uses the decorator-based [v2 programming model for Python](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python). This model gives a simpler file structure and is more code-centric compared to v1.

To complete this quickstart, you need:

*   [Visual Studio Code](https://code.visualstudio.com/download) installed.

*   The Visual Studio Code extension [Azure Functions](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions) installed.

*   The latest version of [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local) installed.

*   An HTTP test tool that keeps your data secure. For more information, see [HTTP test tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local#http-test-tools).

*   An Azure subscription for deploying app to Azure.

*   [Python](https://www.python.org/) version 3.7, 3.8, 3.9, or 3.10 installed.

If you don't have an Azure account, create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.

In this section, you use Visual Studio Code to create a local Azure Functions project.

1.   In Visual Studio Code, select F1 (or select Ctrl/Cmd+Shift+P) to open the command palette. At the prompt (`>`), enter and then select **Azure Functions: Create New Project**.

![Image 2: Screenshot of Create function window.](https://learn.microsoft.com/en-us/azure/azure-functions/durable/media/quickstart-python-vscode/functions-create-project.png)

2.   Select **Browse**. In the **Select Folder** dialog, go to a folder to use for your project, and then choose **Select**.

3.   At the prompts, provide the following information:

| Prompt | Action | Description |
| --- | --- | --- |
| **Select a language for your function app project** | Select **Python**. | Creates a local Python Functions project. |
| **Select a version** | Select **Azure Functions v4**. | You see this option only when Core Tools isn't already installed. In this case, Core Tools is installed the first time you run the app. |
| **Python version** | Select **Python 3.7**, **Python 3.8**, **Python 3.9**, or **Python 3.10**. | Visual Studio Code creates a virtual environment by using the version you select. |
| **Select a template for your project's first function** | Select **Skip for now**. |  |
| **Select how you would like to open your project** | Select **Open in current window**. | Opens Visual Studio Code in the folder you selected. | 

Visual Studio Code installs Azure Functions Core Tools if it's required to create a project. It also creates a function app project in a folder. This project contains the [host.json](https://learn.microsoft.com/en-us/azure/azure-functions/functions-host-json) and [local.settings.json](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local#local-settings-file) configuration files.

A _requirements.txt_ file is also created in the root folder. It specifies the Python packages required to run your function app.

When you create the project, the Azure Functions Visual Studio Code extension automatically creates a virtual environment with your selected Python version. You then need to activate the virtual environment in a terminal and install some dependencies required by Azure Functions and Durable Functions.

1.   Open the _requirements.txt_ in the editor and change its content to the following code:

```
azure-functions
azure-functions-durable
```
2.   In the current folder, open the editor's integrated terminal (Ctrl+Shift+`).

3.   In the integrated terminal, activate the virtual environment in the current folder, depending on your operating system.

    *   [Linux](https://learn.microsoft.com/en-us/azure/azure-functions/durable/quickstart-python-vscode#tabpanel_1_linux)
    *   [macOS](https://learn.microsoft.com/en-us/azure/azure-functions/durable/quickstart-python-vscode#tabpanel_1_macos)
    *   [Windows](https://learn.microsoft.com/en-us/azure/azure-functions/durable/quickstart-python-vscode#tabpanel_1_windows)

```
source .venv/bin/activate
```

* * *

Then, in the integrated terminal where the virtual environment is activated, use pip to install the packages you defined.

```
python -m pip install -r requirements.txt
```

The most basic Durable Functions app has three functions:

*   **Orchestrator function**: A workflow that orchestrates other functions.
*   **Activity function**: A function that is called by the orchestrator function, performs work, and optionally returns a value.
*   **Client function**: A regular function in Azure that starts an orchestrator function. This example uses an HTTP-triggered function.

To create a basic Durable Functions app by using these three function types, replace the contents of _function\_app.py_ with the following Python code:

```
import azure.functions as func
import azure.durable_functions as df

myApp = df.DFApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# An HTTP-triggered function with a Durable Functions client binding
@myApp.route(route="orchestrators/{functionName}")
@myApp.durable_client_input(client_name="client")
async def http_start(req: func.HttpRequest, client):
    function_name = req.route_params.get('functionName')
    instance_id = await client.start_new(function_name)
    response = client.create_check_status_response(req, instance_id)
    return response

# Orchestrator
@myApp.orchestration_trigger(context_name="context")
def hello_orchestrator(context):
    result1 = yield context.call_activity("hello", "Seattle")
    result2 = yield context.call_activity("hello", "Tokyo")
    result3 = yield context.call_activity("hello", "London")

    return [result1, result2, result3]

# Activity
@myApp.activity_trigger(input_name="city")
def hello(city: str):
    return f"Hello {city}"
```

Review the following table for an explanation of each function and its purpose in the sample:

| Method | Description |
| --- | --- |
| `hello_orchestrator` | The orchestrator function, which describes the workflow. In this case, the orchestration starts, invokes three functions in a sequence, and then returns the ordered results of all three functions in a list. |
| `hello` | The activity function, which performs the work that is orchestrated. The function returns a simple greeting to the city passed as an argument. |
| `http_start` | An [HTTP-triggered function](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook) that starts an instance of the orchestration and returns a `check status` response. |

Note

Durable Functions also supports Python v2 programming model [blueprints](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python#organizing-with-blueprints). To use blueprints, register your blueprint functions by using the [azure-functions-durable](https://pypi.org/project/azure-functions-durable)`Blueprint`[class](https://github.com/Azure/azure-functions-durable-python/blob/dev/samples-v2/blueprint/durable_blueprints.py). You can register the resulting blueprint as usual. You can use our [sample](https://github.com/Azure/azure-functions-durable-python/tree/dev/samples-v2/blueprint) as an example.

You can use [Azurite](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite?tabs=visual-studio-code), an emulator for Azure Storage, to test the function locally. In _local.settings.json_, set the value for `AzureWebJobsStorage` to `UseDevelopmentStorage=true` like in this example:

```
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python"
  }
}
```

To install and start running the Azurite extension in Visual Studio Code, in the command palette, enter **Azurite: Start** and select Enter.

You can use other storage options for your Durable Functions app. For more information about storage options and benefits, see [Durable Functions storage providers](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-storage-providers).

Azure Functions Core Tools gives you the capability to run an Azure Functions project on your local development computer. If it isn't installed, you're prompted to install these tools the first time you start a function in Visual Studio Code.

1.   To test your function, set a breakpoint in the `hello` activity function code. Select F5 or select **Debug: Start Debugging** in the command palette to start the function app project. Output from Core Tools appears in the terminal panel.

2.   In the terminal panel, copy the URL endpoint of your HTTP-triggered function.

![Image 3: Screenshot of Azure local output.](https://learn.microsoft.com/en-us/azure/azure-functions/durable/media/quickstart-python-vscode/functions-f5.png)

3.   Use your browser or an HTTP test tool to send an HTTP POST request to the URL endpoint.

Replace the last segment with the name of the orchestrator function (`hello_orchestrator`). The URL should be similar to `http://localhost:7071/api/orchestrators/hello_orchestrator`.

The response is the HTTP function's initial result. It lets you know that the durable orchestration has started successfully. It doesn't yet display the end result of the orchestration. The response includes a few useful URLs. For now, query the status of the orchestration.

4.   Copy the URL value for `statusQueryGetUri`, paste it in your browser's address bar, and execute the request. You can also continue to use your HTTP test tool to issue the GET request.

The request queries the orchestration instance for the status. You should see that the instance finished and that it includes the outputs or results of the durable function. It looks similar to this example:

```
{
    "name": "hello_orchestrator",
    "instanceId": "9a528a9e926f4b46b7d3deaa134b7e8a",
    "runtimeStatus": "Completed",
    "input": null,
    "customStatus": null,
    "output": [
        "Hello Tokyo!",
        "Hello Seattle!",
        "Hello London!"
    ],
    "createdTime": "2020-03-18T21:54:49Z",
    "lastUpdatedTime": "2020-03-18T21:54:54Z"
}
```
5.   To stop debugging, in Visual Studio Code, select Shift+F5.

After you verify that the function runs correctly on your local computer, it's time to publish the project to Azure.

Before you can create Azure resources or publish your app, you must sign in to Azure.

1.   If you aren't already signed in, in the **Activity bar**, select the Azure icon. Then under **Resources**, select **Sign in to Azure**.

![Image 4: Screenshot of the sign in to Azure window in Visual Studio Code.](https://learn.microsoft.com/en-us/azure/includes/media/functions-sign-in-vs-code/functions-sign-into-azure.png)

If you're already signed in and can see your existing subscriptions, go to the next section. If you don't yet have an Azure account, select **Create an Azure Account**. Students can select **Create an Azure for Students Account**.

2.   When you are prompted in the browser, select your Azure account and sign in by using your Azure account credentials. If you create a new account, you can sign in after your account is created.

3.   After you successfully sign in, you can close the new browser window. The subscriptions that belong to your Azure account are displayed in the side bar.

In this section, you create a function app in the Flex Consumption plan along with related resources in your Azure subscription. Many of the resource creation decisions are made for you based on default behaviors. For more control over the created resources, you must instead [create your function app with advanced options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code?tabs=advanced-options#publish-to-azure).

1.   In Visual Studio Code, select F1 to open the command palette. At the prompt (`>`), enter and then select **Azure Functions: Create Function App in Azure**.

2.   At the prompts, provide the following information:

| Prompt | Action |
| --- | --- |
| **Select subscription** | Select the Azure subscription to use. The prompt doesn't appear when you have only one subscription visible under **Resources**. |
| **Enter a new function app name** | Enter a globally unique name that's valid in a URL path. The name you enter is validated to make sure that it's unique in Azure Functions. |
| **Select a location for new resources** | Select an Azure region. For better performance, select a [region](https://azure.microsoft.com/explore/global-infrastructure/geographies/) near you. Only regions supported by Flex Consumption plans are displayed. |
| **Select a runtime stack** | Select the language version you currently run locally. |
| **Select resource authentication type** | Select **Managed identity**, which is the most secure option for connecting to the [default host storage account](https://learn.microsoft.com/en-us/azure/azure-functions/storage-considerations#storage-account-guidance). | 
In the **Azure: Activity Log** panel, the Azure extension shows the status of individual resources as they're created in Azure.

![Image 5: Screenshot that shows the log of Azure resource creation.](https://learn.microsoft.com/en-us/azure/includes/media/functions-create-azure-resources-vs-code/resource-activity-log.png)

3.   When the function app is created, the following related resources are created in your Azure subscription. The resources are named based on the name you entered for your function app.

    *   A [resource group](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview), which is a logical container for related resources.
    *   A function app, which provides the environment for executing your function code. A function app lets you group functions as a logical unit for easier management, deployment, and sharing of resources within the same hosting plan.
    *   An Azure App Service plan, which defines the underlying host for your function app.
    *   A standard [Azure Storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create), which is used by the Functions host to maintain state and other information about your function app.
    *   An Application Insights instance that's connected to the function app, and which tracks the use of your functions in the app.
    *   A user-assigned managed identity that's added to the [Storage Blob Data Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/storage#storage-blob-data-contributor) role in the new default host storage account.

A notification is displayed after your function app is created and the deployment package is applied.

Tip

By default, the Azure resources required by your function app are created based on the name you enter for your function app. By default, the resources are created with the function app in the same, new resource group. If you want to customize the names of the associated resources or reuse existing resources, [publish the project with advanced create options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code?tabs=advanced-options#publish-to-azure).

Important

Deploying to an existing function app always overwrites the contents of that app in Azure.

1.   In the command palette, enter and then select **Azure Functions: Deploy to Function App**.

2.   Select the function app you just created. When prompted about overwriting previous deployments, select **Deploy** to deploy your function code to the new function app resource.

3.   When deployment is completed, select **View Output** to view the creation and deployment results, including the Azure resources that you created. If you miss the notification, select the bell icon in the lower-right corner to see it again.

![Image 6: Screenshot of the View Output window.](https://learn.microsoft.com/en-us/azure/includes/media/functions-publish-project-vscode/function-create-notifications.png)

1.   Copy the URL of the HTTP trigger from the output panel. The URL that calls your HTTP-triggered function must be in this format:

`https://<functionappname>.azurewebsites.net/api/orchestrators/hello_orchestrator`

2.   Paste the new URL for the HTTP request in your browser's address bar. When you use the published app, you can expect to get the same status response that you got when you tested locally.

The Python Durable Functions app that you created and published by using Visual Studio Code is ready to use.

If you no longer need the resources that you created to complete the quickstart, to avoid related costs in your Azure subscription, [delete the resource group](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/delete-resource-group?tabs=azure-portal#delete-resource-group) and all related resources.

*   Learn about [common Durable Functions app patterns](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-sequence).
*   Learn about [Unit testing](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-unit-testing)
