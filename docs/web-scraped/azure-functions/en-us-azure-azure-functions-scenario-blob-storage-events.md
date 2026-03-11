# Source: https://learn.microsoft.com/en-us/azure/azure-functions/scenario-blob-storage-events

Title: Respond to blob storage events using Azure Functions

URL Source: https://learn.microsoft.com/en-us/azure/azure-functions/scenario-blob-storage-events

Markdown Content:
In this quickstart, you use Visual Studio Code to build an app that responds to events in a Blob Storage container. After testing the code locally by using an emulator, you deploy it to a new serverless function app running in a Flex Consumption plan in Azure Functions.

The project uses the Azure Developer CLI (`azd`) extension with Visual Studio Code to simplify initializing and verifying your project code locally, as well as deploying your code to Azure. This deployment follows current best practices for secure and scalable Azure Functions deployments.

This article supports version 4 of the Node.js programming model for Azure Functions.

This article supports version 2 of the Python programming model for Azure Functions.

*   An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).

*   [Visual Studio Code](https://code.visualstudio.com/) on one of the [supported platforms](https://code.visualstudio.com/docs/supporting/requirements#_platforms).

*   The [Azure Functions extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions) for Visual Studio Code. This extension requires [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local). When this tool isn't available locally, the extension tries to install it by using a package-based installer. You can also install or update the Core Tools package by running `Azure Functions: Install or Update Azure Functions Core Tools` from the command palette. If you don't have npm or Homebrew installed on your local computer, you must instead [manually install or update Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local#install-the-azure-functions-core-tools).

*   [.NET 8.0 SDK](https://dotnet.microsoft.com/download)

*   [C# extension](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp) for Visual Studio Code.

*   The [Java Development Kit](https://learn.microsoft.com/en-us/azure/developer/java/fundamentals/java-support-on-azure), version 8, 11, 17 or 21 (Linux).

*   [Apache Maven](https://maven.apache.org/), version 3.0 or above.

*   The [Java extension pack](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack)

*   [Node.js 18.x](https://nodejs.org/en/about/previous-releases) or above. Use the `node --version` command to check your version.

*   [PowerShell 7.2](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows)

*   [.NET 6.0 runtime](https://dotnet.microsoft.com/download/dotnet)

*   The [PowerShell extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode.PowerShell).

*   Python versions that are [supported by Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/supported-languages#languages-by-runtime-version). For more information, see [How to install Python](https://wiki.python.org/moin/BeginnersGuide/Download).

*   The [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) for Visual Studio Code.

*   The [Azure Developer CLI extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.azure-dev) for Visual Studio Code.

*   [Azure Storage extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurestorage)

*   [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) or an equivalent REST tool you use to securely execute HTTP requests.

Use the `azd init` command from the command palette to create a local Azure Functions code project from a template.

1.   In Visual Studio Code, open a folder or workspace where you want to create your project.

2.   Press F1 to open the command palette, search for and run the command `Azure Developer CLI (azd): Initialize App (init)`, then choose **Select a template**.

There might be a slight delay while `azd` initializes the current folder or workspace.

1.   When prompted, choose **Select a template**, then search for and select `Azure Functions C# Event Grid Blob Trigger using Azure Developer CLI`.

2.   When prompted in the terminal, enter a unique environment name, such as `blobevents-dotnet`.

This command pulls the project files from the [template repository](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-eventgrid-blob) and initializes the project in the current folder or workspace.

1.   When prompted, choose **Select a template**, then search for and select `Azure Functions Python Event Grid Blob Trigger using Azure Developer CLI`.

2.   When prompted in the terminal, enter a unique environment name, such as `blobevents-python`.

This command pulls the project files from the [template repository](https://github.com/Azure-Samples/functions-quickstart-python-azd-eventgrid-blob) and initializes the project in the current folder or workspace.

1.   When prompted, choose **Select a template**, then search for and select `Azure Functions TypeScript Event Grid Blob Trigger using Azure Developer CLI`.

2.   When prompted, enter a unique environment name, such as `blobevents-typescript`.

This command pulls the project files from the [template repository](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-eventgrid-blob) and initializes the project in the current folder or workspace.

1.   When prompted, choose **Select a template**, then search for and select `Azure Functions Java Event Grid Blob Trigger using Azure Developer CLI`.

2.   When prompted, enter a unique environment name, such as `blobevents-java`.

This command pulls the project files from the [template repository](https://github.com/Azure-Samples/functions-quickstart-java-azd-eventgrid-blob) and initializes the project in the current folder or workspace.

1.   When prompted, choose **Select a template**, then search for and select `Azure Functions PowerShell Event Grid Blob Trigger using Azure Developer CLI`.

2.   When prompted, enter a unique environment name, such as `blobevents-powershell`.

This command pulls the project files from the [template repository](https://github.com/Azure-Samples/functions-quickstart-powershell-azd-eventgrid-blob) and initializes the project in the current folder or workspace.

In `azd`, the environment maintains a unique deployment context for your app, and you can define more than one. It's also part of the name of the resource group you create in Azure.

Functions needs the local.settings.json file to configure the host when running locally.

1.   Run this command to go to the `src` app folder:

```
cd src
```

1.   Create a file named _local.settings.json_ in the `src` folder that contains this JSON data:

```
{
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "UseDevelopmentStorage=true",
        "FUNCTIONS_WORKER_RUNTIME": "dotnet-isolated",
        "PDFProcessorSTORAGE": "UseDevelopmentStorage=true"
    }
}
```

1.   Create a file named _local.settings.json_ in the `src` folder that contains this JSON data:

```
{
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "UseDevelopmentStorage=true",
        "FUNCTIONS_WORKER_RUNTIME": "java",
        "PDFProcessorSTORAGE": "UseDevelopmentStorage=true"
    }
}
```

1.   Create a file named _local.settings.json_ in the `src` folder that contains this JSON data:

```
{
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "UseDevelopmentStorage=true",
        "FUNCTIONS_WORKER_RUNTIME": "node",
        "PDFProcessorSTORAGE": "UseDevelopmentStorage=true"
    }
}
```

1.   Create a file named _local.settings.json_ in the `src` folder that contains this JSON data:

```
{
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "UseDevelopmentStorage=true",
        "FUNCTIONS_WORKER_RUNTIME": "powershell",
        "FUNCTIONS_WORKER_RUNTIME_VERSION": "7.2",
        "PDFProcessorSTORAGE": "UseDevelopmentStorage=true"
    }
}
```

1.   Create a file named _local.settings.json_ in the `src` folder that contains this JSON data:

```
{
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "UseDevelopmentStorage=true",
        "FUNCTIONS_WORKER_RUNTIME": "python",
        "PDFProcessorSTORAGE": "UseDevelopmentStorage=true"
    }
}
```

In the `src` folder, run these commands to create and activate a virtual environment named `.venv`:

*   [Linux/macOS](https://learn.microsoft.com/en-us/azure/azure-functions/scenario-blob-storage-events#tabpanel_1_linux)
*   [Windows (bash)](https://learn.microsoft.com/en-us/azure/azure-functions/scenario-blob-storage-events#tabpanel_1_windows-bash)
*   [Windows (Cmd)](https://learn.microsoft.com/en-us/azure/azure-functions/scenario-blob-storage-events#tabpanel_1_windows-cmd)

```
python3 -m venv .venv
source .venv/bin/activate
```

If Python doesn't install the venv package on your Linux distribution, run the following command:

```
sudo apt-get install python3-venv
```

Use the Azurite emulator to run your code project locally before creating and using Azure resources.

1.   If you haven't already, [install Azurite](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite#install-azurite).

2.   Press F1. In the command palette, search for and run the command `Azurite: Start` to start the local storage emulator.

3.   In the **Azure** area, expand **Workspace**>**Attached Storage Accounts**>**Local Emulator**, right-click (Ctrl-click on Mac) **Blob Containers**, select **Create Blob Container...**, and create these two blob storage containers in the local emulator:

    *   `unprocessed-pdf`: container that the trigger monitors for storage events.
    *   `processed-pdf`: container where the function sends processed blobs as output.

4.   Expand **Blob Containers**, right-click (Ctrl-click on Mac) **unprocessed-pdf**, select **Upload Files...**, press Enter to accept the root directory, and upload the PDF files from the `data` project folder.

When running locally, you can use REST to trigger the function by simulating the function receiving a message from an event subscription.

Visual Studio Code integrates with [Azure Functions Core tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local) to let you run this project on your local development computer by using the Azurite emulator. The `PDFProcessorSTORAGE` environment variable defines the storage account connection, which is also set to `"UseDevelopmentStorage=true"` in the local.settings.json file when running locally.

1.   Run this command from the `src` project folder in a terminal or command prompt:

```
func start
``` ```
mvn clean package
mvn azure-functions:run
``` ```
npm install
func start
``` ```
npm install
npm start
``` 
When the Functions host starts, it writes the name of the trigger and the trigger type to the terminal output. In Functions, the project root folder contains the host.json file.

2.   With Core Tools still running in **Terminal**, open the `test.http` file in your project and select **Send Request** to trigger the `ProcessBlobUpload` function by sending a test blob event to the blob event webhook.

This step simulates receiving an event from an event subscription when running locally, and you should see the request and processed file information written in the logs. If you aren't using _REST Client_, you must use another secure REST tool to call the endpoint with the payload in `test.http`.

3.   In the Workspace area for the blob container, expand **processed-pdf** and verify that the function processed the PDF file and copied it with a `processed-` prefix.

4.   When you're done, press Ctrl+C in the terminal window to stop the `func.exe` host process.

You can review the code that defines the Event Grid blob trigger in the [ProcessBlobUpload.cs project file](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-eventgrid-blob/blob/main/src/ProcessBlobUpload.cs). The function demonstrates how to:

*   Use `BlobTrigger` with `Source = BlobTriggerSource.EventGrid` for near real-time processing
*   Bind to `BlobClient` for the source blob and `BlobContainerClient` for the destination
*   Process blob content and copy it to another container by using streams

You can review the code that defines the Event Grid blob trigger in the [function_app.py project file](https://github.com/Azure-Samples/functions-quickstart-python-azd-eventgrid-blob/blob/main/src/function_app.py). The function demonstrates how to:

*   Use `@app.blob_trigger` with `source="EventGrid"` for near real-time processing
*   Access blob content using the `InputStream` parameter
*   Copy processed files to the destination container using the Azure Storage SDK

You can review the code that defines the Event Grid blob trigger in the [processBlobUpload.ts project file](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-eventgrid-blob/blob/main/src/functions/processBlobUpload.ts). The function demonstrates how to:

*   Use `app.storageBlob()` with `source: 'EventGrid'` for near real-time processing
*   Access blob content using the Node.js Azure Storage SDK
*   Process and copy files to the destination container asynchronously

You can review the code that defines the Event Grid blob trigger in the [ProcessBlobUpload.java project file](https://github.com/Azure-Samples/functions-quickstart-java-azd-eventgrid-blob/blob/main/src/src/main/java/com/microsoft/azure/samples/ProcessBlobUpload.java). The function demonstrates how to:

*   Use `@BlobTrigger` with `source = "EventGrid"` for near real-time processing
*   Access blob content using `BlobInputStream` parameter
*   Copy processed files to the destination container using Azure Storage SDK for Java

You can review the code that defines the Event Grid blob trigger in the [ProcessBlobUpload/run.ps1 project file](https://github.com/Azure-Samples/functions-quickstart-powershell-azd-eventgrid-blob/blob/main/src/processBlobUpload/run.ps1) and the corresponding [function.json](https://github.com/Azure-Samples/functions-quickstart-powershell-azd-eventgrid-blob/blob/main/src/processBlobUpload/function.json). The function demonstrates how to:

*   Configure blob trigger with `"source": "EventGrid"` in function.json for near real-time processing
*   Access blob content using PowerShell Azure Storage cmdlets
*   Process and copy files to the destination container using Azure PowerShell modules

After you review and verify your function code locally, it's time to publish the project to Azure.

Use the `azd up` command to create the function app in a Flex Consumption plan along with other required Azure resources, including the event subscription. After the infrastructure is ready, `azd` also deploys your project code to the new function app in Azure.

1.   In Visual Studio Code, press F1 to open the command palette. Search for and run the command `Azure Developer CLI (azd): Sign In with Azure Developer CLI`, then sign in by using your Azure account.

2.   In the project root, press F1 to open the command palette. Search for and run the command `Azure Developer CLI (azd): Provision and Deploy (up)` to create the required Azure resources and deploy your code.

3.   When prompted in the Terminal window, provide these required deployment parameters:

| Prompt | Description |
| --- | --- |
| Select an Azure Subscription to use | Choose the subscription in which you want to create your resources. |
| _Environment name_ | An environment that's used to maintain a unique deployment context for your app. |
| _Azure location_ | Azure region in which to create the resource group that contains the new Azure resources. Only regions that currently support the Flex Consumption plan are shown. | 
The `azd up` command uses your responses to these prompts with the Bicep configuration files to create and configure these required Azure resources, following the latest best practices:

    *   Flex Consumption plan and function app
    *   Azure Storage account with blob containers
    *   Application Insights (recommended)
    *   Access policies and roles for your account
    *   Event Grid subscription for blob events
    *   Service-to-service connections by using managed identities (instead of stored connection strings)

After the command completes successfully, your app runs in Azure with an event subscription configured to trigger your function when blobs are added to the `unprocessed-pdf` container.

4.   Make a note of the `AZURE_STORAGE_ACCOUNT_NAME` and `AZURE_FUNCTION_APP_NAME` in the output. These names are unique for your storage account and function app in Azure, respectively.

1.   In Visual Studio Code, press F1. In the command palette, search for and run the command `Azure Storage: Upload Files...`. Accept the root directory, and as before, upload one or more PDF files from the `data` project folder.

2.   When prompted, select the name of your new storage account (from `AZURE_STORAGE_ACCOUNT_NAME`). Select **Blob Containers**>**unprocessed-pdf**.

3.   Press F1. In the command palette, search for and run the command `Azure Storage: Open in Explorer`. Select the same storage account >**Blob Containers**>**processed-pdf**, then **Open in new window**.

4.   In the Explorer, verify that the PDF files you uploaded were processed by your function. The output is written to the `processed-pdf` container with a `processed-` prefix.

The Event Grid blob trigger processes files within seconds of upload. This speed demonstrates the near real-time capabilities of this approach compared to traditional polling-based blob triggers.

Run the `azd up` command as many times as you need to both provision your Azure resources and deploy code updates to your function app.

Note

Deployed code files are always overwritten by the latest deployment package.

Your initial responses to `azd` prompts and any environment variables generated by `azd` are stored locally in your named environment. Use the `azd env get-values` command to review all of the variables in your environment that were used when creating Azure resources.

When you're done working with your function app and related resources, use this command to delete the function app and its related resources from Azure. This action helps you avoid incurring any further costs:

```
azd down --no-prompt
```

Note

The `--no-prompt` option instructs `azd` to delete your resource group without a confirmation from you.

This command doesn't affect your local code project.

*   [Azure Functions scenarios](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios)
*   [Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan)
*   [Tutorial: Trigger Azure Functions on blob containers using an event subscription](https://learn.microsoft.com/en-us/azure/azure-functions/functions-event-grid-blob-trigger)
*   [Azure Developer CLI (azd)](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/)
*   [azd reference](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/reference)
*   [Azure Functions Core Tools reference](https://learn.microsoft.com/en-us/azure/azure-functions/functions-core-tools-reference)
*   [Code and test Azure Functions locally](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local)
