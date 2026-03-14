# Source: https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-azure-developer-cli

Title: Build a scalable web API using Azure Functions

URL Source: https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-azure-developer-cli

Markdown Content:
In this quickstart, you use Azure Developer command-line tools to build a scalable web API with function endpoints that respond to HTTP requests. After testing the code locally, you deploy it to a new serverless function app you create running in a Flex Consumption plan in Azure Functions.

The project source uses the Azure Developer CLI (azd) to simplify deploying your code to Azure. This deployment follows current best practices for secure and scalable Azure Functions deployments.

By default, the Flex Consumption plan follows a _pay-for-what-you-use_ billing model, which means completing this quickstart incurs a small cost of a few USD cents or less in your Azure account.

*   An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).

*   [Azure Developer CLI](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/install-azd)

*   [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local#install-the-azure-functions-core-tools)

*   [.NET 8.0 SDK](https://dotnet.microsoft.com/download)

*   [Azurite storage emulator](https://learn.microsoft.com/en-us/azure/storage/common/storage-install-azurite?tabs=npm#install-azurite)

*   [Java 17 Developer Kit](https://learn.microsoft.com/en-us/azure/developer/java/fundamentals/java-support-on-azure)
    *   If you use another [supported version of Java](https://learn.microsoft.com/en-us/azure/azure-functions/supported-languages?pivots=programming-language-java#languages-by-runtime-version), you must update the project's pom.xml file.
    *   The `JAVA_HOME` environment variable must be set to the install location of the correct version of the Java Development Kit (JDK).

*   [Apache Maven 3.8.x](https://maven.apache.org/)

*   [Node.js 20](https://nodejs.org/)

*   [PowerShell 7.2](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows)

*   [.NET 6.0 SDK](https://dotnet.microsoft.com/download)

*   [Python 3.11](https://www.python.org/)

*   [Azurite storage emulator](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite)

*   A [secure HTTP test tool](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local#http-test-tools) for sending requests with JSON payloads to your function endpoints. This article uses `curl`.

Use the `azd init` command to create a local Azure Functions code project from a template.

1.   In your local terminal or command prompt, run this `azd init` command in an empty folder:

```
azd init --template functions-quickstart-dotnet-azd -e httpendpoint-dotnet
```

This command pulls the project files from the [template repository](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd) and initializes the project in the current folder. The `-e` flag sets a name for the current environment. In `azd`, the environment maintains a unique deployment context for your app, and you can define more than one. It's also used in the name of the resource group you create in Azure.

2.   Run this command to navigate to the `http` app folder:

```
cd http
```
3.   Create a file named _local.settings.json_ in the `http` folder that contains this JSON data:

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
azd init --template azure-functions-java-flex-consumption-azd -e httpendpoint-java
```

This command pulls the project files from the [template repository](https://github.com/Azure-Samples/azure-functions-java-flex-consumption-azd) and initializes the project in the current folder. The `-e` flag sets a name for the current environment. In `azd`, the environment maintains a unique deployment context for your app, and you can define more than one. It's also used in the name of the resource group you create in Azure.

2.   Run this command to navigate to the `http` app folder:

```
cd http
```
3.   Create a file named _local.settings.json_ in the `http` folder that contains this JSON data:

```
{
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "UseDevelopmentStorage=true",
        "FUNCTIONS_WORKER_RUNTIME": "java"
    }
}
```

This file is required when running locally.

1.   In your local terminal or command prompt, run this `azd init` command in an empty folder:

```
azd init --template functions-quickstart-javascript-azd -e httpendpoint-js
```

This command pulls the project files from the [template repository](https://github.com/Azure-Samples/functions-quickstart-javascript-azd) and initializes the project in the root folder. The `-e` flag sets a name for the current environment. In `azd`, the environment maintains a unique deployment context for your app, and you can define more than one. It's also used in the name of the resource group you create in Azure.

2.   Create a file named _local.settings.json_ in the root folder that contains this JSON data:

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

1.   In your local terminal or command prompt, run this `azd init` command in an empty folder:

```
azd init --template functions-quickstart-powershell-azd -e httpendpoint-ps
```

This command pulls the project files from the [template repository](https://github.com/Azure-Samples/functions-quickstart-powershell-azd) and initializes the project in the root folder. The `-e` flag sets a name for the current environment. In `azd`, the environment maintains a unique deployment context for your app, and you can define more than one. It's also used in the name of the resource group you create in Azure.

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
        "FUNCTIONS_WORKER_RUNTIME": "powershell",
        "FUNCTIONS_WORKER_RUNTIME_VERSION": "7.2"
    }
}
```

This file is required when running locally.

1.   In your local terminal or command prompt, run this `azd init` command in an empty folder:

```
azd init --template functions-quickstart-typescript-azd -e httpendpoint-ts
```

This command pulls the project files from the [template repository](https://github.com/Azure-Samples/functions-quickstart-typescript-azd) and initializes the project in the root folder. The `-e` flag sets a name for the current environment. In `azd`, the environment maintains a unique deployment context for your app, and you can define more than one. The environment name is also used in the name of the resource group you create in Azure.

2.   Create a file named _local.settings.json_ in the root folder that contains this JSON data:

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

1.   In your local terminal or command prompt, run this `azd init` command in an empty folder:

```
azd init --template functions-quickstart-python-http-azd -e httpendpoint-py
```

This command pulls the project files from the [template repository](https://github.com/Azure-Samples/functions-quickstart-python-http-azd) and initializes the project in the root folder. The `-e` flag sets a name for the current environment. In `azd`, the environment maintains a unique deployment context for your app, and you can define more than one. The environment name is also used in the name of the resource group you create in Azure.

2.   Create a file named _local.settings.json_ in the root folder that contains this JSON data:

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

In the root folder, run these commands to create and activate a virtual environment named `.venv`:

*   [Linux/macOS](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-azure-developer-cli#tabpanel_1_linux)
*   [Windows (bash)](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-azure-developer-cli#tabpanel_1_windows-bash)
*   [Windows (Cmd)](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-azure-developer-cli#tabpanel_1_windows-cmd)

```
python3 -m venv .venv
source .venv/bin/activate
```

If Python doesn't install the venv package on your Linux distribution, run the following command:

```
sudo apt-get install python3-venv
```

1.   Run this command from your app folder in a terminal or command prompt:

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
When the Functions host starts in your local project folder, it writes the URL endpoints of your HTTP triggered functions to the terminal output.

Note

Because access key authorization isn't enforced when running locally, the function URL returned doesn't include the access key value and you don't need it to call your function. 
2.   In your browser, go to the `httpget` endpoint, which should look like this URL:

[http://localhost:7071/api/httpget](http://localhost:7071/api/httpget)

3.   From a new terminal or command prompt window, run this `curl` command to send a POST request with a JSON payload to the `httppost` endpoint:

```
curl -i http://localhost:7071/api/httppost -H "Content-Type: text/json" -d @testdata.json
``` ```
curl -i http://localhost:7071/api/httppost -H "Content-Type: text/json" -d "@src/functions/testdata.json"
``` 
This command reads JSON payload data from the `testdata.json` project file. You can find examples of both HTTP requests in the `test.http` project file.

4.   When you're done, press Ctrl+C in the terminal window to stop the `func.exe` host process.

1.   Run `deactivate` to shut down the virtual environment.

You can review the code that defines the two HTTP trigger function endpoints:

*   [`httpget`](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-azure-developer-cli#tabpanel_2_get)
*   [`httppost`](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-azure-developer-cli#tabpanel_2_post)

```
[Function("httpget")]
       public IActionResult Run([HttpTrigger(AuthorizationLevel.Function, "get")]
         HttpRequest req,
         string name)
       {
           var returnValue = string.IsNullOrEmpty(name)
               ? "Hello, World."
               : $"Hello, {name}.";

           _logger.LogInformation($"C# HTTP trigger function processed a request for {returnValue}.");

           return new OkObjectResult(returnValue);
       }
```

```
@FunctionName("httpget")
public HttpResponseMessage run(
        @HttpTrigger(
            name = "req",
            methods = {HttpMethod.GET},
            authLevel = AuthorizationLevel.FUNCTION)
            HttpRequestMessage<Optional<String>> request,
        final ExecutionContext context) {
    context.getLogger().info("Java HTTP trigger processed a request.");

    // Parse query parameter
    String name = Optional.ofNullable(request.getQueryParameters().get("name")).orElse("World");

    return request.createResponseBuilder(HttpStatus.OK).body("Hello, " + name).build();
}
```

```
const { app } = require('@azure/functions');

app.http('httpget', {
    methods: ['GET'],
    authLevel: 'function',
    handler: async (request, context) => {
        context.log(`Http function processed request for url "${request.url}"`);

        const name = request.query.get('name') || await request.text() || 'world';

        return { body: `Hello, ${name}!` };
    }
});
```

```
import { app, HttpRequest, HttpResponseInit, InvocationContext } from "@azure/functions";

export async function httpGetFunction(request: HttpRequest, context: InvocationContext): Promise<HttpResponseInit> {
    context.log(`Http function processed request for url "${request.url}"`);

    const name = request.query.get('name') || await request.text() || 'world';

    return { body: `Hello, ${name}!` };
};

app.http('httpget', {
    methods: ['GET'],
    authLevel: 'function',
    handler: httpGetFunction
});
```

This `function.json` file defines the `httpget` function:

```
{
  "bindings": [
    {
      "authLevel": "function",
      "type": "httpTrigger",
      "direction": "in",
      "name": "Request",
      "methods": [
        "get"
      ],
      "route": "httpget"
    },
    {
      "type": "http",
      "direction": "out",
      "name": "Response"
    }
  ]
}
```

This `run.ps1` file implements the function code:

```
using namespace System.Net

# Input bindings are passed in via param block.
param($Request, $TriggerMetadata)

# Write to the Azure Functions log stream.
Write-Host "PowerShell HTTP trigger function processed a request."

# Interact with query parameters
$name = $Request.Query.name

$body = "This HTTP triggered function executed successfully. Pass a name in the query string for a personalized response."

if ($name) {
    $body = "Hello, $name. This HTTP triggered function executed successfully."
}

# Associate values to output bindings by calling 'Push-OutputBinding'.
Push-OutputBinding -Name Response -Value ([HttpResponseContext]@{
    StatusCode = [HttpStatusCode]::OK
    Body = $body
})
```

```
@app.route(route="httpget", methods=["GET"])
def http_get(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get("name", "World")

    logging.info(f"Processing GET request. Name: {name}")

    return func.HttpResponse(f"Hello, {name}!")
```

You can review the complete template project [here](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd).

You can review the complete template project [here](https://github.com/Azure-Samples/azure-functions-java-flex-consumption-azd).

You can review the complete template project [here](https://github.com/Azure-Samples/functions-quickstart-javascript-azd).

You can review the complete template project [here](https://github.com/Azure-Samples/functions-quickstart-typescript-azd).

You can review the complete template project [here](https://github.com/Azure-Samples/functions-quickstart-powershell-azd).

You can review the complete template project [here](https://github.com/Azure-Samples/functions-quickstart-python-http-azd).

After you verify your functions locally, it's time to publish them to Azure.

This project is configured to use the `azd up` command to deploy this project to a new function app in a Flex Consumption plan in Azure.

Tip

The project includes a set of Bicep files (in the `infra` folder) that `azd` uses to create a secure deployment to a Flex consumption plan that follows best practices.

1.   Run this command to have `azd` create the required Azure resources in Azure and deploy your code project to the new function app:

```
azd up
```

The root folder contains the `azure.yaml` definition file required by `azd`.

If you're not already signed in, you're asked to authenticate with your Azure account.

2.   When prompted, provide these required deployment parameters:

| Parameter | Description |
| --- | --- |
| _Azure subscription_ | Subscription in which your resources are created. |
| _Azure location_ | Azure region in which to create the resource group that contains the new Azure resources. Only regions that currently support the Flex Consumption plan are shown. |
| _vnetEnabled_ | Choose _False_. When set to _True_ the deployment creates your function app in a new virtual network. | 
The `azd up` command uses your responses to these prompts with the Bicep configuration files to complete these deployment tasks:

    *   Create and configure these required Azure resources (equivalent to `azd provision`):

        *   Flex Consumption plan and function app
        *   Azure Storage (required) and Application Insights (recommended)
        *   Access policies and roles for your account
        *   Service-to-service connections using managed identities (instead of stored connection strings)
        *   (Option) Virtual network to securely run both the function app and the other Azure resources

    *   Package and deploy your code to the deployment container (equivalent to `azd deploy`). The app is then started and runs in the deployed package.

After the command completes successfully, you see links to the resources you created.

You can now invoke your function endpoints in Azure by making HTTP requests to their URLs by using your HTTP test tool or from the browser (for GET requests). When your functions run in Azure, access key authorization is enforced, and you must provide a function access key with your request.

You can use the Core Tools to get the URL endpoints of your functions running in Azure.

1.   In your local terminal or command prompt, run these commands to get the URL endpoint values:

    *   [bash](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-azure-developer-cli#tabpanel_3_bash)
    *   [Cmd](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-azure-developer-cli#tabpanel_3_cmd)

```
SET APP_NAME=$(azd env get-value AZURE_FUNCTION_NAME)
func azure functionapp list-functions $APP_NAME --show-keys
```

    *   [PowerShell](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-azure-developer-cli#tabpanel_4_powershell)
    *   [Cmd](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-azure-developer-cli#tabpanel_4_cmd2)

```
$APP_NAME = azd env get-value AZURE_FUNCTION_NAME
func azure functionapp list-functions $APP_NAME --show-keys
```

The `azd env get-value` command gets your function app name from the local environment. When you use the `--show-keys` option with `func azure functionapp list-functions`, the returned **Invoke URL:** value for each endpoint includes a function-level access key.

2.   As before, use your HTTP test tool to validate these URLs in your function app running in Azure.

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

*   [Azure Functions scenarios](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios)
*   [Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan)
*   [Azure Developer CLI (azd)](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/)
*   [azd reference](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/reference)
*   [Azure Functions Core Tools reference](https://learn.microsoft.com/en-us/azure/azure-functions/functions-core-tools-reference)
*   [Code and test Azure Functions locally](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local)
