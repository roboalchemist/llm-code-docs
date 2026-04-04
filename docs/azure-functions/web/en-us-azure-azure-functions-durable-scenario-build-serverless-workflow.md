# Source: https://learn.microsoft.com/en-us/azure/azure-functions/durable/scenario-build-serverless-workflow?toc=/azure/azure-functions/toc.json&bc=/azure/azure-functions/breadcrumb/toc.json

Title: Build a serverless workflow using Durable Functions - Azure Functions - Azure Durable

URL Source: https://learn.microsoft.com/en-us/azure/azure-functions/durable/scenario-build-serverless-workflow?toc=/azure/azure-functions/toc.json&bc=/azure/azure-functions/breadcrumb/toc.json

Markdown Content:
In this quickstart, you use Azure Developer command-line tools to build a serverless workflow that orchestrates multiple tasks running in parallel. After testing the code locally, you deploy it to a new serverless function app running in a Flex Consumption plan in Azure Functions.

The project uses the Azure Developer CLI (azd) to simplify deploying your code to Azure. This deployment follows current best practices for secure and scalable Azure Functions deployments. This quickstart demonstrates the **fan-out/fan-in** pattern in [Durable Functions](https://learn.microsoft.com/en-us/azure/azure-functions/durable/what-is-durable-task), an extension that orchestrates stateful workflows with durable execution. The sample fetches article titles in parallel—the orchestration fans out to multiple activities running concurrently, then fans back in to aggregate the results.

By default, the Flex Consumption plan follows a _pay-for-what-you-use_ billing model, which means completing this quickstart incurs a small cost of a few USD cents or less in your Azure account.

Important

A sample project for this language isn't currently available. Check back later or instead switch to one of these languages: C#, Python, or TypeScript.

*   An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).

*   [Azure Developer CLI](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/install-azd)

*   [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local#install-the-azure-functions-core-tools)

*   [Azurite storage emulator](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite?tabs=npm#install-azurite)

*   [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0)

*   [Python 3.12](https://www.python.org/downloads/)

*   [Node.js 22+](https://nodejs.org/)

Use the `azd init` command to create a local Durable Functions code project from a template.

1.   In your local terminal or command prompt, run this `azd init` command in an empty folder:

```
azd init --template durable-functions-quickstart-dotnet-azd -e dfquickstart-dotnet
```

This command pulls the project files from the [template repository](https://github.com/Azure-Samples/durable-functions-quickstart-dotnet-azd) and initializes the project in the current folder. The `-e` flag sets a name for the current environment. In `azd`, the environment maintains a unique deployment context for your app, and you can define more than one. The environment name is also used in the name of the resource group you create in Azure.

2.   Run this command to navigate to the `fanoutfanin` app folder:

```
cd fanoutfanin
```
3.   Create a file named _local.settings.json_ in the `fanoutfanin` folder that contains this JSON data:

```
{
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "UseDevelopmentStorage=true",
        "FUNCTIONS_WORKER_RUNTIME": "dotnet-isolated"
    }
}
```

This file is required when running locally.

1.   In your local terminal or command prompt, run this `azd init` command in an empty folder:

```
azd init --template durable-functions-quickstart-python-azd -e dfquickstart-python
```

This command pulls the project files from the [template repository](https://github.com/Azure-Samples/durable-functions-quickstart-python-azd) and initializes the project in the current folder. The `-e` flag sets a name for the current environment. In `azd`, the environment maintains a unique deployment context for your app, and you can define more than one. The environment name is also used in the name of the resource group you create in Azure.

2.   Run this command to navigate to the `src` app folder:

```
cd src
```
3.   Create a file named _local.settings.json_ in the `src` folder that contains this JSON data:

```
{
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "UseDevelopmentStorage=true",
        "FUNCTIONS_WORKER_RUNTIME": "python"
    }
}
```

This file is required when running locally.

In the `src` folder, run these commands to create and activate a virtual environment named `.venv`:

*   [Linux/macOS](https://learn.microsoft.com/en-us/azure/azure-functions/durable/scenario-build-serverless-workflow?toc=/azure/azure-functions/toc.json&bc=/azure/azure-functions/breadcrumb/toc.json#tabpanel_1_linux)
*   [Windows (bash)](https://learn.microsoft.com/en-us/azure/azure-functions/durable/scenario-build-serverless-workflow?toc=/azure/azure-functions/toc.json&bc=/azure/azure-functions/breadcrumb/toc.json#tabpanel_1_windows-bash)
*   [Windows (Cmd)](https://learn.microsoft.com/en-us/azure/azure-functions/durable/scenario-build-serverless-workflow?toc=/azure/azure-functions/toc.json&bc=/azure/azure-functions/breadcrumb/toc.json#tabpanel_1_windows-cmd)

```
python3 -m venv .venv
source .venv/bin/activate
```

If Python doesn't install the venv package on your Linux distribution, run the following command:

```
sudo apt-get install python3-venv
```

From the `src` folder with the virtual environment activated, run this command to install the required dependencies:

```
pip install -r requirements.txt
```

1.   In your local terminal or command prompt, run this `azd init` command in an empty folder:

```
azd init --template durable-functions-quickstart-typescript-azd -e dfquickstart-typescript
```

This command pulls the project files from the [template repository](https://github.com/Azure-Samples/durable-functions-quickstart-typescript-azd) and initializes the project in the current folder. The `-e` flag sets a name for the current environment. In `azd`, the environment maintains a unique deployment context for your app, and you can define more than one. The environment name is also used in the name of the resource group you create in Azure.

2.   Run this command to navigate to the `src` app folder:

```
cd src
```
3.   Create a file named _local.settings.json_ in the `src` folder that contains this JSON data:

```
{
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "UseDevelopmentStorage=true",
        "FUNCTIONS_WORKER_RUNTIME": "node"
    }
}
```

This file is required when running locally.

From the `src` folder, run these commands to install the required dependencies and build the project:

```
npm install
npm run build
```

The Functions runtime needs a storage component. The `"AzureWebJobsStorage": "UseDevelopmentStorage=true"` setting in the local.settings.json file directs the runtime to use the local storage emulator, Azurite.

Run this command to start Azurite:

```
npx azurite --skipApiVersionCheck --location ~/azurite-data
```

Keep Azurite running in the terminal window. You need it running while testing locally.

1.   From the `fanoutfanin` folder in a new terminal window, run this command to start the Functions host:

```
func start
```

When the Functions host starts in your local project folder, it writes the local URL endpoints of your HTTP triggered functions to the terminal output.

Note

Because access key authorization isn't enforced when running locally, you don't need an access key to call your function. 
2.   In your browser, make a GET request to the endpoint that starts the orchestration:

[http://localhost:7071/api/FetchOrchestration_HttpStart](http://localhost:7071/api/FetchOrchestration_HttpStart)

This request starts a new orchestration instance. The orchestration fans out to several activities to fetch the titles of Microsoft Learn articles in parallel. When the activities finish, the orchestration fans back in and returns the titles as a formatted string.

1.   From the `src` folder in a new terminal window with the virtual environment activated, run this command to start the Functions host:

```
func start
```

When the Functions host starts in your local project folder, it writes the local URL endpoints of your HTTP triggered functions to the terminal output.

Note

Because access key authorization isn't enforced when running locally, you don't need an access key to call your function. 
2.   In your browser, make a GET request to the HTTP start endpoint:

[http://localhost:7071/api/orchestrators/fetch_orchestration](http://localhost:7071/api/orchestrators/fetch_orchestration)

This request starts a new orchestration instance. The orchestration fans out to several activities to fetch the titles of Microsoft Learn articles in parallel. When the activities finish, the orchestration fans back in and returns the titles as a formatted string.

1.   From the `src` folder in a new terminal window with the virtual environment activated, run this command to start the Functions host:

```
func start
```

When the Functions host starts in your local project folder, it writes the local URL endpoints of your HTTP triggered functions to the terminal output.

Note

Because access key authorization isn't enforced when running locally, you don't need an access key to call your function. 
2.   In your browser, make a GET request to the HTTP start endpoint:

[http://localhost:7071/api/orchestrators/fetchOrchestration](http://localhost:7071/api/orchestrators/fetchOrchestration)

This request starts a new orchestration instance. The orchestration fans out to several activities to fetch the titles of Microsoft Learn articles in parallel. When the activities finish, the orchestration fans back in and returns the titles as a formatted string.

1.   The HTTP endpoint returns a JSON response with several URLs. The `statusQueryGetUri` endpoint provides the orchestration status.

2.   Copy the `statusQueryGetUri` value and paste it into your browser or HTTP test tool to check the status of the orchestration. When the orchestration completes, you see the fetched article titles in the response.

3.   When you're done, press Ctrl+C in the terminal window to stop the `func` host process.

1.   Run `deactivate` to shut down the virtual environment.

You can review the code that implements the fan-out/fan-in pattern:

The title fetching activities are tracked using a dynamic task list. The line `await Task.WhenAll(parallelTasks);` waits for all the called activities, which run concurrently, to complete. When done, all outputs are aggregated as a formatted string.

```
[Function(nameof(FetchOrchestration))]
public static async Task<string> RunOrchestrator(
    [OrchestrationTrigger] TaskOrchestrationContext context)
{
    ILogger logger = context.CreateReplaySafeLogger(nameof(FetchOrchestration));
    logger.LogInformation("Fetching data.");
    var parallelTasks = new List<Task<string>>();
    
    // List of URLs to fetch titles from
    var urls = new List<string>
    {
        "https://learn.microsoft.com/azure/azure-functions/durable/durable-functions-overview",
        "https://learn.microsoft.com/azure/azure-functions/durable/durable-task-scheduler/durable-task-scheduler",
        "https://learn.microsoft.com/azure/azure-functions/functions-scenarios",
        "https://learn.microsoft.com/azure/azure-functions/functions-create-ai-enabled-apps",
    };

    // Run fetching tasks in parallel
    foreach (var url in urls)
    {
        Task<string> task = context.CallActivityAsync<string>(nameof(FetchTitleAsync), url);
        parallelTasks.Add(task);
    }
    
    // Wait for all the parallel tasks to complete before continuing
    await Task.WhenAll(parallelTasks);
   
    // Return fetched titles as a formatted string
    return string.Join("; ", parallelTasks.Select(t => t.Result));
}
```

You can review the complete template project [here](https://github.com/Azure-Samples/durable-functions-quickstart-dotnet-azd).

The title fetching activities are tracked using a dynamic task list. The line `yield context.task_all(tasks)` waits for all the called activities, which run concurrently, to complete. When done, all outputs are aggregated as a formatted string.

```
# List of URLs to fetch titles from
    urls = [
        "https://learn.microsoft.com/azure/azure-functions/durable/durable-functions-overview",
        "https://learn.microsoft.com/azure/azure-functions/durable/durable-task-scheduler/durable-task-scheduler",
        "https://learn.microsoft.com/azure/azure-functions/functions-scenarios",
        "https://learn.microsoft.com/azure/azure-functions/functions-create-ai-enabled-apps",
    ]
    
    # Run fetching tasks in parallel
    tasks = []
    for url in urls:
        task = context.call_activity("fetch_title", url)
        tasks.append(task)
    
    # Wait for all the parallel tasks to complete before continuing
    results = yield context.task_all(tasks)
    
    # Return fetched titles as a formatted string
    return "; ".join(results)

@myApp.activity_trigger(input_name="url")
async def fetch_title(url: str):
    """Activity function that fetches the title from a URL."""
    logger = logging.getLogger("FetchTitle")
    logger.info(f"Fetching from url {url}.")
    
    try:
        async with ClientSession() as session:
```

You can review the complete template project [here](https://github.com/Azure-Samples/durable-functions-quickstart-python-azd).

The title fetching activities are tracked using a dynamic task list. The line `yield context.df.Task.all(parallelTasks)` waits for all the called activities, which run concurrently, to complete. When done, all outputs are aggregated as a formatted string.

```
const urls = [
        "https://learn.microsoft.com/azure/azure-functions/durable/durable-functions-overview",
        "https://learn.microsoft.com/azure/azure-functions/durable/durable-task-scheduler/durable-task-scheduler",
        "https://learn.microsoft.com/azure/azure-functions/functions-scenarios",
        "https://learn.microsoft.com/azure/azure-functions/functions-create-ai-enabled-apps",
    ];

    // Run fetching tasks in parallel
    const parallelTasks = [];
    for (const url of urls) {
        const task = context.df.callActivity(fetchTitleActivityName, url);
        parallelTasks.push(task);
    }

    // Wait for all the parallel tasks to complete before continuing
    const results: string[] = yield context.df.Task.all(parallelTasks);

    // Return fetched titles as a formatted string
    return results.join("; ");
};
df.app.orchestration("fetchOrchestration", fetchOrchestration);

const fetchTitleAsync: ActivityHandler = async function (
    url: string,
    context: InvocationContext
```

You can review the complete template project [here](https://github.com/Azure-Samples/durable-functions-quickstart-typescript-azd).

After you verify your functions locally, it's time to publish them to Azure.

This project is configured to use the `azd up` command, run from the project root folder, to deploy this project to a new function app in a Flex Consumption plan in Azure.

Tip

The project includes a set of Bicep files (in the `infra` folder) that `azd` uses to create a secure deployment to a Flex consumption plan that follows best practices.

1.   In the project root folder, which contains the azure.yaml file, run this command to authenticate with your Azure account:

```
azd auth login
```
2.   For this quickstart, run this command to disable the virtual network deployment:

```
azd env set VNET_ENABLED false
```
3.   Run this command from the root project folder to have `azd` create the required Azure resources and deploy your code project to the new function app:

```
azd up
```

The root folder contains the `azure.yaml` definition file required by `azd`.

4.   When prompted, provide these required deployment parameters:

| Parameter | Description |
| --- | --- |
| _Azure subscription_ | Subscription in which your resources are created. |
| _Azure location_ | Azure region in which to create the resource group that contains the new Azure resources. Only regions that currently support the Flex Consumption plan are shown. | 
The `azd up` command uses your responses to these prompts with the Bicep configuration files to complete these deployment tasks:

    *   Create and configure these required Azure resources:

        *   Flex Consumption plan and function app
        *   Azure Storage (required) and Application Insights (recommended)
        *   Access policies and roles for your account
        *   Service-to-service connections using managed identities (instead of stored connection strings)

    *   Package and deploy your code to the deployment container. The app is then started and runs in the deployed package.

After the command completes successfully, you see links to the resources you created.

You can now invoke your orchestration endpoint in Azure by making an HTTP request to its URL. When your functions run in Azure, access key authorization is enforced, and you must provide a function access key with your request.

You can use the Core Tools to get the URL endpoint of the HTTP trigger that starts the orchestration in Azure.

1.   In your local terminal or command prompt, run these commands to get the URL endpoint values:

    *   [bash](https://learn.microsoft.com/en-us/azure/azure-functions/durable/scenario-build-serverless-workflow?toc=/azure/azure-functions/toc.json&bc=/azure/azure-functions/breadcrumb/toc.json#tabpanel_2_bash)
    *   [PowerShell](https://learn.microsoft.com/en-us/azure/azure-functions/durable/scenario-build-serverless-workflow?toc=/azure/azure-functions/toc.json&bc=/azure/azure-functions/breadcrumb/toc.json#tabpanel_2_powershell)
    *   [Cmd](https://learn.microsoft.com/en-us/azure/azure-functions/durable/scenario-build-serverless-workflow?toc=/azure/azure-functions/toc.json&bc=/azure/azure-functions/breadcrumb/toc.json#tabpanel_2_cmd)

```
APP_NAME=$(azd env get-value AZURE_FUNCTION_NAME)
func azure functionapp list-functions $APP_NAME --show-keys
```

The `azd env get-value` command gets your function app name from the local environment. When you use the `--show-keys` option with `func azure functionapp list-functions`, the returned **Invoke URL:** value for each endpoint includes any required function-level access keys.

2.   As before, use a browser or HTTP test tool to start the orchestration in your function app running in Azure.

Run the `azd up` command as many times as you need to both provision your Azure resources and deploy code updates to your function app.

Note

Deployed code files are always overwritten by the latest deployment package.

Your initial responses to `azd` prompts and any environment variables generated by `azd` are stored locally in your named environment. Use the `azd env get-values` command to review all of the variables in your environment that you used when creating Azure resources.

When you're done working with your function app and related resources, use this command to delete the function app and its related resources from Azure and avoid incurring any further costs:

```
azd down --no-prompt
```

Note

The `--no-prompt` option instructs `azd` to delete your resource group without a confirmation from you.

This command doesn't affect your local code project.

*   [Durable Functions overview](https://learn.microsoft.com/en-us/azure/azure-functions/durable/what-is-durable-task)
*   [Durable Task programming model](https://learn.microsoft.com/en-us/azure/azure-functions/durable/programming-model-overview)
*   [Azure Functions scenarios](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios)
*   [Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan)
*   [Azure Developer CLI (azd)](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/)
*   [azd reference](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/reference)
