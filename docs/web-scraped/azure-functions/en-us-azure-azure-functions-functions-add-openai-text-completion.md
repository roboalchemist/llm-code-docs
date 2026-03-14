# Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-add-openai-text-completion

Title: Tutorial: Add Azure OpenAI text completions to your functions in Visual Studio Code

URL Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-add-openai-text-completion

Markdown Content:
This article shows you how to use Visual Studio Code to add an HTTP endpoint to the function app you created in the previous quickstart article. When triggered, this new HTTP endpoint uses an [Azure OpenAI text completion input binding](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-openai-textcompletion-input) to get text completion hints from your data model.

During this tutorial, you learn how to accomplish these tasks:

*   Create resources in Azure OpenAI.
*   Deploy a model in the OpenAI resource.
*   Set access permissions to the model resource.
*   Enable your function app to connect to OpenAI.
*   Add OpenAI bindings to your HTTP triggered function.

*   Complete the steps in [part 1 of Create a function in Azure using Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-vs-code).
*   Obtain access to Azure OpenAI in your Azure subscription. If you haven't already been granted access, complete [this form](https://aka.ms/oai/access) to request access.

*   Install [.NET Core CLI tools](https://learn.microsoft.com/en-us/dotnet/core/tools/?tabs=netcore2x).

*   The [Azurite storage emulator](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite?tabs=npm). While you can also use an actual Azure Storage account, the article assumes you're using this emulator.

The following steps show how to create an Azure OpenAI data model in the Azure portal.

1.   Sign in with your Azure subscription in the [Azure portal](https://portal.azure.com/).

2.   Select **Create a resource** and search for the **Azure OpenAI**. When you locate the service, select **Create**.

3.   On the **Create Azure OpenAI** page, provide the following information for the fields on the **Basics** tab:

| Field | Description |
| --- | --- |
| **Subscription** | Your subscription, which has been onboarded to use Azure OpenAI. |
| **Resource group** | The resource group you created for the function app in the previous article. You can find this resource group name by right-clicking the function app in the Azure Resources browser, selecting properties, and then searching for the `resourceGroup` setting in the returned JSON resource file. |
| **Region** | Ideally, the same location as the function app. |
| **Name** | A descriptive name for your Azure OpenAI Service resource, such as _mySampleOpenAI_. |
| **Pricing Tier** | The pricing tier for the resource. Currently, only the Standard tier is available for the Azure OpenAI Service. For more info on pricing visit the [Azure OpenAI pricing page](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) | 
![Image 1: Screenshot that shows how to configure an Azure OpenAI resource in the Azure portal.](https://learn.microsoft.com/en-us/azure/ai-services/openai/media/create-resource/create-resource-basic-settings.png)

4.   Select **Next** twice to accept the default values for both the **Network** and **Tags** tabs. The service you create doesn't have any network restrictions, including from the internet.

5.   Select **Next** a final time to move to the final stage in the process: **Review + submit**.

6.   Confirm your configuration settings, and select **Create**.

The Azure portal displays a notification when the new resource is available. Select **Go to resource** in the notification or search for your new Azure OpenAI resource by name.

7.   In the Azure OpenAI resource page for your new resource, select **Click here to view endpoints** under **Essentials**>**Endpoints**. Copy the **endpoint** URL and the **keys**. Save these values, you need them later.

Now that you have the credentials to connect to your model in Azure OpenAI, you need to set these access credentials in application settings.

Now you can deploy a model. You can select from one of several available models in Azure OpenAI Studio.

To deploy a model, follow these steps:

1.   Sign in to [Azure OpenAI Studio](https://oai.azure.com/).

2.   Choose the subscription and the Azure OpenAI resource you created, and select **Use resource**.

3.   Under **Management** select **Deployments**.

4.   Select **Create new deployment** and configure the following fields:

| Field | Description |
| --- | --- |
| **Deployment name** | Choose a name carefully. The deployment name is used in your code to call the model by using the client libraries and the REST APIs, so you must save for use later on. |
| **Select a model** | Model availability varies by region. For a list of available models per region, see [Model summary table and region availability](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability). | Important

When you access the model via the API, you need to refer to the deployment name rather than the underlying model name in API calls, which is one of the key differences between OpenAI and Azure OpenAI. OpenAI only requires the model name. Azure OpenAI always requires deployment name, even when using the model parameter. In our docs, we often have examples where deployment names are represented as identical to model names to help indicate which model works with a particular API endpoint. Ultimately your deployment names can follow whatever naming convention is best for your use case. 
5.   Accept the default values for the rest of the setting and select **Create**.

The deployments table shows a new entry that corresponds to your newly created model.

You now have everything you need to add Azure OpenAI-based text completion to your function app.

1.   In Visual Studio Code, open the local code project you created when you completed the [previous article](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-vs-code?pivot=programming-language-csharp).

2.   In the local.settings.json file in the project root folder, update the `AzureWebJobsStorage` setting to `UseDevelopmentStorage=true`. You can skip this step if the `AzureWebJobsStorage` setting in _local.settings.json_ is set to the connection string for an existing Azure Storage account instead of `UseDevelopmentStorage=true`.

3.   In the local.settings.json file, add these settings values:

    *   **`AZURE_OPENAI_ENDPOINT`**: required by the binding extension. Set this value to the endpoint of the Azure OpenAI resource you created earlier.
    *   **`AZURE_OPENAI_KEY`**: required by the binding extension. Set this value to the key for the Azure OpenAI resource.
    *   **`CHAT_MODEL_DEPLOYMENT_NAME`**: used to define the input binding. Set this value to the name you chose for your model deployment.

4.   Save the file. When you deploy to Azure, you must also add these settings to your function app.

Because you're using an Azure OpenAI output binding, you must have the corresponding bindings extension installed before you run the project.

Except for HTTP and timer triggers, bindings are implemented as extension packages. To add the Azure OpenAI extension package to your project, run this [dotnet add package](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-add-package) command in the **Terminal** window:

```
dotnet add package Microsoft.Azure.Functions.Worker.Extensions.OpenAI --prerelease
```

To access the preview Azure OpenAI bindings, you must use a preview version of the extension bundle that contains this extension.

Replace the `extensionBundle` setting in your current `host.json` file with this JSON:

```
"extensionBundle": {
   "id": "Microsoft.Azure.Functions.ExtensionBundle.Preview",
   "version": "[4.*, 5.0.0)"
 }
```

Now, you can use the Azure OpenAI output binding in your project.

The code you add creates a `whois` HTTP function endpoint in your existing project. In this function, data passed in a URL `name` parameter of a GET request is used to dynamically create a completion prompt. This dynamic prompt is bound to a text completion input binding, which returns a response from the model based on the prompt. The completion from the model is returned in the HTTP response.

1.   In your existing `HttpExample` class file, add this `using` statement:

```
using Microsoft.Azure.Functions.Worker.Extensions.OpenAI.TextCompletion;
```
2.   In the same file, add this code that defines a new HTTP trigger endpoint named `whois`:

```
[Function(nameof(WhoIs))]
public IActionResult WhoIs([HttpTrigger(AuthorizationLevel.Function, Route = "whois/{name}")] HttpRequest req,
[TextCompletionInput("Who is {name}?", ChatModel = "%CHAT_MODEL_DEPLOYMENT_NAME%")] TextCompletionResponse response)
{
    if(!String.IsNullOrEmpty(response.Content))
    {
        return new OkObjectResult(response.Content);
    }
    else
    {
        return new NotFoundObjectResult("Something went wrong.");
    }
}
```

1.   Update the `pom.xml` project file to add this reference to the `properties` collection:

```
<azure-functions-java-library-openai>0.5.0-preview</azure-functions-java-library-openai>
```
2.   In the same file, add this dependency to the `dependencies` collection:

```
<dependency>
    <groupId>com.microsoft.azure.functions</groupId>
    <artifactId>azure-functions-java-library-openai</artifactId>
    <version>${azure-functions-java-library-openai}</version>
</dependency>
```
3.   In the existing `Function.java` project file, add these `import` statements:

```
import com.microsoft.azure.functions.openai.annotation.textcompletion.TextCompletion;
import com.microsoft.azure.functions.openai.annotation.textcompletion.TextCompletionResponse;
```
4.   In the same file, add this code that defines a new HTTP trigger endpoint named `whois`:

```
@FunctionName("WhoIs")
public HttpResponseMessage whoIs(
    @HttpTrigger(
        name = "req", 
        methods = {HttpMethod.GET},
        authLevel = AuthorizationLevel.ANONYMOUS, 
        route = "whois/{name}") 
        HttpRequestMessage<Optional<String>> request,
    @BindingName("name") String name,
    @TextCompletion(prompt = "Who is {name}?", chatModel = "%CHAT_MODEL_DEPLOYMENT_NAME%", name = "response", isReasoningModel = false) TextCompletionResponse response,
    final ExecutionContext context) {
    return request.createResponseBuilder(HttpStatus.OK)
        .header("Content-Type", "application/json")
        .body(response.getContent())
        .build();
}
```

1.   In Visual Studio Code, Press F1 and in the command palette type `Azure Functions: Create Function...`, select **HTTP trigger**, type the function name `whois`, and press Enter.

2.   In the new `whois.js` code file, replace the contents of the file with this code:

```
const { app, input } = require("@azure/functions");

// This OpenAI completion input requires a {name} binding value.
const openAICompletionInput = input.generic({
    prompt: 'Who is {name}?',
    maxTokens: '100',
    type: 'textCompletion',
    chatModel: '%CHAT_MODEL_DEPLOYMENT_NAME%'
})

app.http('whois', {
    methods: ['GET'],
    route: 'whois/{name}',
    authLevel: 'function',
    extraInputs: [openAICompletionInput],
    handler: async (_request, context) => {
        var response = context.extraInputs.get(openAICompletionInput)
        return { body: response.content.trim() }
    }
});
```

1.   In Visual Studio Code, Press F1 and in the command palette type `Azure Functions: Create Function...`, select **HTTP trigger**, type the function name `whois`, and press Enter.

2.   In the new `whois.ts` code file, replace the contents of the file with this code:

```
import { app, input } from "@azure/functions";

// This OpenAI completion input requires a {name} binding value.
const openAICompletionInput = input.generic({
    prompt: 'Who is {name}?',
    maxTokens: '100',
    type: 'textCompletion',
    chatModel: '%CHAT_MODEL_DEPLOYMENT_NAME%'
})

app.http('whois', {
    methods: ['GET'],
    route: 'whois/{name}',
    authLevel: 'function',
    extraInputs: [openAICompletionInput],
    handler: async (_request, context) => {
        var response: any = context.extraInputs.get(openAICompletionInput)
        return { body: response.content.trim() }
    }
});
```

1.   In the existing `function_app.py` project file, add this `import` statement:

```
import json
```
2.   In the same file, add this code that defines a new HTTP trigger endpoint named `whois`:

```
@app.route(route="whois/{name}", methods=["GET"])
@app.text_completion_input(
    arg_name="response",
    prompt="Who is {name}?",
    max_tokens="100",
    chat_model="%CHAT_MODEL_DEPLOYMENT_NAME%",
)
def whois(req: func.HttpRequest, response: str) -> func.HttpResponse:
    response_json = json.loads(response)
    return func.HttpResponse(response_json["content"], status_code=200)
```

1.   In Visual Studio Code, Press F1 and in the command palette type `Azure Functions: Create Function...`, select **HTTP trigger**, type the function name `whois`, select **Anonymous**, and press Enter.

2.   Open the new `whois/function.json` code file and replace its contents with this code, which adds a definition for the `TextCompletionResponse` input binding:

```
{
  "bindings": [
    {
      "authLevel": "function",
      "type": "httpTrigger",
      "direction": "in",
      "name": "Request",
      "route": "whois/{name}",
      "methods": [
        "get"
      ]
    },
    {
      "type": "http",
      "direction": "out",
      "name": "Response"
    },
    {
      "type": "textCompletion",
      "direction": "in",
      "name": "TextCompletionResponse",
      "prompt": "Who is {name}?",
      "maxTokens": "100",
      "chatModel": "%CHAT_MODEL_DEPLOYMENT_NAME%"
    }
  ]
}
```
3.   Replace the content of the `whois/run.ps1` code file with this code, which returns the input binding response:

```
using namespace System.Net

param($Request, $TriggerMetadata, $TextCompletionResponse)

Push-OutputBinding -Name Response -Value ([HttpResponseContext]@{
        StatusCode = [HttpStatusCode]::OK
        Body       = $TextCompletionResponse.Content
    })
```

1.   In Visual Studio Code, Press F1 and in the command palette type `Azurite: Start` and press Enter to start the Azurite storage emulator.

2.   Press F5 to start the function app project and Core Tools in debug mode.

3.   With the Core Tools running, send a GET request to the `whois` endpoint function, with a name in the path, like this URL:

`http://localhost:7071/api/whois/<NAME>`

Replace the `<NAME>` string with the value you want passed to the `"Who is {name}?"` prompt. The `<NAME>` must be the URL-encoded name of a public figure, like `Abraham%20Lincoln`.

The response you see is the text completion response from your Azure OpenAI model.

4.   After a response is returned, press Ctrl + C to stop Core Tools.

In Azure, _resources_ refer to function apps, functions, storage accounts, and so forth. They're grouped into _resource groups_, and you can delete everything in a group by deleting the group.

You created resources to complete these quickstarts. You could be billed for these resources, depending on your [account status](https://azure.microsoft.com/account/) and [service pricing](https://azure.microsoft.com/pricing/). If you don't need the resources anymore, here's how to delete them:

1.   In Visual Studio Code, press F1 to open the command palette. In the command palette, search for and select `Azure: Open in portal`.

2.   Choose your function app and press Enter. The function app page opens in the Azure portal.

3.   In the **Overview** tab, select the named link next to **Resource group**.

![Image 2: Screenshot of select the resource group to delete from the function app page.](https://learn.microsoft.com/en-us/azure/includes/media/functions-cleanup-resources-vs-code/functions-app-delete-resource-group.png)

4.   On the **Resource group** page, review the list of included resources, and verify that they're the ones you want to delete.

5.   Select **Delete resource group**, and follow the instructions.

Deletion may take a couple of minutes. When it's done, a notification appears for a few seconds. You can also select the bell icon at the top of the page to view the notification.

*   [Azure OpenAI extension for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-openai)
*   [Azure OpenAI extension samples](https://github.com/Azure/azure-functions-openai-extension/tree/main/samples)
*   [Machine learning and AI](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios#machine-learning-and-ai)
