# Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local

Title: Develop and run Azure Functions locally

URL Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local

Markdown Content:
Whenever possible, create and validate your Azure Functions code project in a local development environment. By using Azure Functions Core Tools, you get a local runtime version of Azure Functions that integrates with popular development tools for an integrated development, debugging, and deployments. Your local functions can even connect to live Azure services.

This article provides some shared guidance for local development, such as working with the [local.settings.json file](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local#local-settings-file). It also links to development environment-specific guidance.

Tip

For detailed information about how to develop functions locally, see the linked IDE-specific guidance articles.

The way you develop functions on your local computer depends on your [language](https://learn.microsoft.com/en-us/azure/azure-functions/supported-languages) and tooling preferences. Choose your preferred language at the [top of the article](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local#top).

Tip

All local development relies on Azure Functions Core Tools to provide the Functions runtime for debugging in a local environment.

Use these development environments to code functions locally in your preferred language:

| Environment | Description |
| --- | --- |
| [Visual Studio](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs) | The Azure Functions tools are included in the **Azure development** workload of [Visual Studio](https://www.visualstudio.com/vs/). You can compile and deploy your C# function code to Azure as a .NET class library. Includes the Core Tools for local testing. To learn more, see [Create your first C# function in Azure using Visual Studio](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-your-first-function-visual-studio). |
| [Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code) | The [Azure Functions extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions) adds Functions support to Visual Studio Code. Requires the Core Tools. Supports development on Linux, macOS, and Windows. To learn more, see [Create your first function using Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-vs-code?pivot=programming-language-csharp). |
| [Command prompt or terminal](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local) | [Azure Functions Core Tools](https://www.npmjs.com/package/azure-functions-core-tools) provides the core runtime and templates for creating functions, which enable local development. Supports development on Linux, macOS, and Windows. To learn more, see [Create a C# function in Azure from the command line](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli?pivots=programming-language-csharp). |

| Environment | Description |
| --- | --- |
| [Maven](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli?pivots=programming-language-java) | Maven archetype uses Core Tools to enable development of Java functions. Supports development on Linux, macOS, and Windows. To learn more, see [Create your first function with Java and Maven](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli?pivots=programming-language-java). |
| [Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code) | The [Azure Functions extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions) adds Functions support to Visual Studio Code. Requires the Core Tools. Supports development on Linux, macOS, and Windows. To learn more, see [Create your first function using Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-vs-code?pivot=programming-language-java). |
| [IntelliJ IDEA](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-maven-intellij) | Maven archetype and Core Tools lets you develop your functions using IntelliJ. For more information, see [Create your first Java function in Azure using IntelliJ](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-maven-intellij). |
| [Eclipse](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-maven-eclipse) | Maven archetype and Core Tools lets you develop your functions using Eclipse. To learn more, see [Create your first Java function in Azure using Ecplise](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-maven-eclipse). |

| Environment | Description |
| --- | --- |
| [Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code) | The [Azure Functions extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions) adds Functions support to Visual Studio Code. Requires the Core Tools. Supports development on Linux, macOS, and Windows. To learn more, see [Create your first function using Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-vs-code?pivot=programming-language-javascript). |
| [Command prompt or terminal](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local) | [Azure Functions Core Tools](https://www.npmjs.com/package/azure-functions-core-tools) provides the core runtime and templates for creating functions, which enable local development. Supports development on Linux, macOS, and Windows. To learn more, see [Create a Node.js function in Azure from the command line](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli?pivots=programming-language-javascript). |

| Environment | Description |
| --- | --- |
| [Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code) | The [Azure Functions extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions) adds Functions support to Visual Studio Code. Requires the Core Tools. Supports development on Linux, macOS, and Windows. To learn more, see [Create your first function using Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-vs-code?pivot=programming-language-powershell). |
| [Command prompt or terminal](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local) | [Azure Functions Core Tools](https://www.npmjs.com/package/azure-functions-core-tools) provides the core runtime and templates for creating functions, which enable local development. Supports development on Linux, macOS, and Windows. To learn more, see [Create a PowerShell function in Azure from the command line](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli?pivots=programming-language-powershell). |

| Environment | Description |
| --- | --- |
| [Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code) | The [Azure Functions extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions) adds Functions support to Visual Studio Code. Requires the Core Tools. Supports development on Linux, macOS, and Windows. To learn more, see [Create your first function using Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-vs-code?pivot=programming-language-python). |
| [Command prompt or terminal](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local) | [Azure Functions Core Tools](https://www.npmjs.com/package/azure-functions-core-tools) provides the core runtime and templates for creating functions, which enable local development. Supports development on Linux, macOS, and Windows. To learn more, see [Create a Python function in Azure from the command line](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli?pivots=programming-language-python). |

Each of these local development environments lets you create function app projects and use predefined function templates to create new functions. Each environment uses the Core Tools so that you can test and debug your functions against the real Functions runtime on your own machine just as you would any other app. You can also publish your function app project from any of these environments to Azure.

A Functions project directory contains the following files in the project root folder, regardless of language:

| File name | Description |
| --- | --- |
| host.json | To learn more, see the [host.json reference](https://learn.microsoft.com/en-us/azure/azure-functions/functions-host-json). |
| local.settings.json | Settings that Core Tools uses when running locally, including app settings. To learn more, see [local settings file](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local#local-settings-file). |
| .gitignore | Prevents the local.settings.json file from being accidentally published to a Git repository. To learn more, see [local settings file](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local#local-settings-file). |
| .vscode\extensions.json | Settings file used when opening the project folder in Visual Studio Code. |

Other files in the project depend on your language and specific functions. For more information, see the developer guide for your language.

The `local.settings.json` file stores app settings and settings used by local development tools. Use the settings in the `local.settings.json` file only when running your project locally. When you publish your project to Azure, add any required settings to the app settings for the function app.

Important

Because the `local.settings.json` file might contain secrets, such as connection strings, be cautious about committing it to source control. Tools that support Functions provide ways to synchronize settings in the `local.settings.json` file with the [app settings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings#settings) in the function app to which your project is deployed.

The `local.settings.json` file has this structure:

```
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "<language worker>",
    "AzureWebJobsStorage": "<connection-string>",
    "MyBindingConnection": "<binding-connection-string>",
    "AzureWebJobs.HttpExample.Disabled": "true"
  },
  "Host": {
    "LocalHttpPort": 7071,
    "CORS": "*",
    "CORSCredentials": false
  },
  "ConnectionStrings": {
    "SQLConnectionString": "<sqlclient-connection-string>"
  }
}
```

These settings are supported when you run projects locally:

| Setting | Description |
| --- | --- |
| **`IsEncrypted`** | When this setting is set to `true`, all values are encrypted by using a local machine key. Used with `func settings` commands. Default value is `false`. You might want to encrypt the local.settings.json file on your local computer when it contains secrets, such as service connection strings. The host automatically decrypts settings when it runs. Use the `func settings decrypt` command before trying to read locally encrypted settings. |
| **`Values`** | Collection of application settings used when a project is running locally. These key-value (string-string) pairs correspond to application settings in your function app in Azure, like [`AzureWebJobsStorage`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#azurewebjobsstorage). Many triggers and bindings have a property that refers to a connection string app setting, like `Connection` for the [Blob storage trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger#configuration). For these properties, you need an application setting defined in the `Values` array. See the subsequent table for a list of commonly used settings. Values must be strings and not JSON objects or arrays. Setting names can't include a double underline (`__`) and shouldn't include a colon (`:`). Double underline characters are reserved by the runtime, and the colon is reserved to support [dependency injection](https://learn.microsoft.com/en-us/azure/azure-functions/functions-dotnet-dependency-injection#working-with-options-and-settings). |
| **`Host`** | Settings in this section customize the Functions host process when you run projects locally. These settings are separate from the host.json settings, which also apply when you run projects in Azure. |
| **`LocalHttpPort`** | Sets the default port used when running the local Functions host (`func host start` and `func run`). The `--port` command-line option takes precedence over this setting. For example, when running in Visual Studio IDE, you can change the port number by navigating to the "Project Properties -> Debug" window and explicitly specifying the port number in a `host start --port <your-port-number>` command that can be supplied in the "Application Arguments" field. |
| **`CORS`** | Defines the origins allowed for [cross-origin resource sharing (CORS)](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing). Origins are supplied as a comma-separated list with no spaces. The wildcard value (*) is supported, which allows requests from any origin. |
| **`CORSCredentials`** | When set to `true`, allows `withCredentials` requests. |
| **`ConnectionStrings`** | A collection. Don't use this collection for the connection strings used by your function bindings. This collection is used only by frameworks that typically get connection strings from the `ConnectionStrings` section of a configuration file, like [Entity Framework](https://learn.microsoft.com/en-us/ef/ef6/). Connection strings in this object are added to the environment with the provider type of [System.Data.SqlClient](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient). Items in this collection aren't published to Azure with other app settings. You must explicitly add these values to the `Connection strings` collection of your function app settings. If you're creating a [`SqlConnection`](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnection) in your function code, store the connection string value with your other connections in **Application Settings** in the portal. |

The following application settings can be included in the **`Values`** array when running locally:

| Setting | Values | Description |
| --- | --- | --- |
| **`AzureWebJobsStorage`** | Storage account connection string, or `UseDevelopmentStorage=true` | Contains the connection string for an Azure storage account. Required when using triggers other than HTTP. For more information, see the [`AzureWebJobsStorage`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#azurewebjobsstorage) reference. When you have the [Azurite Emulator](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite) installed locally and you set [`AzureWebJobsStorage`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#azurewebjobsstorage) to `UseDevelopmentStorage=true`, Core Tools uses the emulator. For more information, see [Local storage emulator](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local#local-storage-emulator). |
| **`AzureWebJobs.<FUNCTION_NAME>.Disabled`** | `true`|`false` | To disable a function when running locally, add `"AzureWebJobs.<FUNCTION_NAME>.Disabled": "true"` to the collection, where `<FUNCTION_NAME>` is the name of the function. To learn more, see [How to disable functions in Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/disable-function#disable-functions-locally). |
| **`FUNCTIONS_WORKER_RUNTIME`** | `dotnet` `dotnet-isolated` `node` `java` `powershell` `python` | Indicates the targeted language of the Functions runtime. Required for version 2.x and higher of the Functions runtime. Core Tools generates this setting for your project. To learn more, see the [`FUNCTIONS_WORKER_RUNTIME`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#functions_worker_runtime) reference. |
| **`FUNCTIONS_WORKER_RUNTIME_VERSION`** | `~7` | Indicates to use PowerShell 7 when running locally. If not set, then PowerShell Core 6 is used. This setting is only used when running locally. The PowerShell runtime version is determined by the `powerShellVersion` site configuration setting, when it runs in Azure, which can be [set in the portal](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-powershell#changing-the-powershell-version). |

To learn how to use values from the `values` array as environment variables in your function code, see [Environment variables](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node#environment-variables) in the developer guide.

To learn how to use values from the `values` array as environment variables in your function code, see [Environment variables](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-java#environment-variables) in the developer guide.

To learn how to use values from the `values` array as environment variables in your function code, see [Environment variables](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-powershell#environment-variables) in the developer guide.

To learn how to use values from the `values` array as environment variables in your function code, see [Environment variables](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python#environment-variables) in the developer guide.

When you develop your functions locally, include any local settings required by your app in the app settings of the function app where you deploy your code. You might also need to download current settings from the function app to your local project. While you can [manually configure app settings in the Azure portal](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings?tabs=portal#settings), the following tools also let you synchronize app settings with local settings in your project:

*   [Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code#application-settings-in-azure)
*   [Visual Studio](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs#function-app-settings)
*   [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local#local-settings)

When you develop your functions locally, consider trigger and binding behaviors. For HTTP triggers, you can call the HTTP endpoint on the local computer by using `http://localhost/`. For non-HTTP triggered functions, use several options to run locally:

*   You can use connection strings that target live Azure services to test bindings during local development. Add the appropriate connection string settings in the `Values` array in the local.settings.json file. When you do this, local executions during testing might affect your production services. Instead, consider setting up separate live services to use during development and testing, and then switch to different services during production.
*   For storage-based triggers, use a [local storage emulator](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local#local-storage-emulator).
*   Run non-HTTP trigger functions manually by using special administrator endpoints. For more information, see [Manually run a non-HTTP-triggered function](https://learn.microsoft.com/en-us/azure/azure-functions/functions-manually-run-non-http).

During local testing, you must run the host provided by Core Tools (func.exe) locally. For more information, see [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local).

During development, you can call any of your function endpoints from a web browser when they support the HTTP GET method. However, for other HTTP methods that support payloads, such as POST or PUT, you need to use an HTTP test tool to create and send these HTTP requests to your function endpoints.

Caution

For scenarios where your requests must include sensitive data, make sure to use a tool that protects your data and reduces the risk of exposing any sensitive data to the public. Sensitive data you should protect might include: credentials, secrets, access tokens, API keys, geolocation data, and personal data.

Keep your data secure by choosing an HTTP test tool that works either offline or locally, doesn't sync your data to the cloud, and doesn't require that you sign in to an online account. Some tools can also protect your data from accidental exposure by implementing specific security features.

Avoid using tools that centrally store your HTTP request history (including sensitive information), don't follow best security practices, or don't respect data privacy concerns.

Consider using one of these tools for securely sending HTTP requests to your function endpoints:

*   [Visual Studio Code](https://code.visualstudio.com/download) with a [.http file extension from Visual Studio Marketplace](https://marketplace.visualstudio.com/vscode), such as [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)
*   [Visual Studio](https://visualstudio.microsoft.com/vs/) supports [.http files](https://learn.microsoft.com/en-us/aspnet/core/test/http-files), starting with version 17.8
*   [PowerShell Invoke-RestMethod](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-restmethod)
*   [Microsoft Edge - Network Console tool](https://learn.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/network-console/network-console-tool)
*   [Bruno](https://www.usebruno.com/)
*   [curl](https://curl.se/)

During local development, you can use the local [Azurite emulator](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite) when testing functions with Azure Storage bindings (Queue Storage, Blob Storage, and Table Storage), without connecting to remote storage services. Azurite integrates with Visual Studio Code and Visual Studio, and you can also run it from the command prompt by using npm. For more information, see [Use the Azurite emulator for local Azure Storage development](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite).

The following setting in the `Values` collection of the local.settings.json file tells the local Functions host to use Azurite for the default `AzureWebJobsStorage` connection:

```
"AzureWebJobsStorage": "UseDevelopmentStorage=true"
```

With this setting value, any Azure Storage trigger or binding that uses `AzureWebJobsStorage` as its connection connects to Azurite when running locally. Keep these considerations in mind when using storage emulation during local execution:

*   You must have Azurite installed and running.
*   You should test with an actual storage connection to Azure services before publishing to Azure.
*   When you publish your project, don't publish the `AzureWebJobsStorage` setting as `UseDevelopmentStorage=true`. In Azure, the `AzureWebJobsStorage` setting must always be the connection string of the storage account used by your function app. For more information, see [`AzureWebJobsStorage`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#azurewebjobsstorage).

*   To learn more about local development of functions using Visual Studio, see [Develop Azure Functions using Visual Studio](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs).

*   To learn more about local development of functions using Visual Studio Code on a Mac, Linux, or Windows computer, see [Develop Azure Functions by using Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code).
*   To learn more about developing functions from the command prompt or terminal, see [Work with Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local).
