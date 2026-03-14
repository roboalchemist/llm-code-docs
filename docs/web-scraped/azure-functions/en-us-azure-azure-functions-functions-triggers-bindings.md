# Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings

Title: Triggers and Bindings in Azure Functions

URL Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings

Published Time: Mon, 02 Mar 2026 18:37:16 GMT

Markdown Content:
In this article, you learn the high-level concepts surrounding triggers and bindings for functions.

Triggers cause a function to run. A trigger defines how a function is invoked, and a function must have exactly one trigger. Triggers can also pass data into your function, as you would with method calls.

Binding to a function is a way of declaratively connecting your functions to other resources. Bindings either pass data into your function (an _input binding_) or enable you to write data out from your function (an _output binding_) by using _binding parameters_. Your function trigger is essentially a special type of input binding.

You can mix and match bindings to suit your function's specific scenario. Bindings are optional, and a function might have one or multiple input and/or output bindings.

Triggers and bindings let you avoid hardcoding access to other services. Your function receives data (for example, the content of a queue message) in function parameters. You send data (for example, to create a queue message) by using the return value of the function.

Consider the following examples of how you could implement functions:

| Example scenario | Trigger | Input binding | Output binding |
| --- | --- | --- | --- |
| A new queue message arrives, which runs a function to write to another queue. | Queue* | _None_ | Queue* |
| A scheduled job reads Azure Blob Storage contents and creates a new Azure Cosmos DB document. | Timer | Blob Storage | Azure Cosmos DB |
| Azure Event Grid is used to read an image from Blob Storage and a document from Azure Cosmos DB to send an email. | Event Grid | Blob Storage and Azure Cosmos DB | SendGrid |

* Represents different queues.

These examples aren't meant to be exhaustive, but they illustrate how you can use triggers and bindings together. For a more comprehensive set of scenarios, see [Azure Functions scenarios](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios).

Tip

Azure Functions doesn't require you to use input and output bindings to connect to Azure services. You can always create an Azure SDK client in your code and use it instead for your data transfers. For more information, see [Connect to services](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#connect-to-services).

The following example shows an HTTP-triggered function with an output binding that writes a message to an Azure Storage queue.

For C# class library functions, you configure triggers and bindings by decorating methods and parameters with C# attributes. The specific attribute that you apply might depend on the C# runtime model:

*   [Isolated worker model](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings#tabpanel_1_isolated-process)
*   [In-process model](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings#tabpanel_1_in-process)

The HTTP trigger (`HttpTrigger`) is defined on the `Run` method for a function named `HttpExample` that returns a `MultiResponse` object:

```
[Function("HttpExample")]
public MultiResponse Run([HttpTrigger(AuthorizationLevel.Function, "get", "post")] HttpRequest req)
```

This example shows the `MultiResponse` object definition. The object definition returns `HttpResponse` to the HTTP request and writes a message to a storage queue by using a `QueueOutput` binding:

```
public class MultiResponse
{
    [QueueOutput("outqueue", Connection = "AzureWebJobsStorage")]
    public string[] Messages { get; set; }
    public IActionResult HttpResponse { get; set; }
}
```

For more information, see the [C# guide for isolated worker models](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#methods-recognized-as-functions).

Legacy C# script functions use a `function.json` definition file. For more information, see the [Azure Functions C# script (.csx) developer reference](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-csharp).

For Java functions, you configure triggers and bindings by annotating specific methods and parameters. This HTTP trigger (`@HttpTrigger`) is defined on the `run` method for a function named `HttpExample`. The function writes to a storage queue named `outqueue` that the `@QueueOutput` annotation defines on the `msg` parameter:

```
@FunctionName("HttpExample")
public HttpResponseMessage run(
        @HttpTrigger(name = "req", methods = {HttpMethod.GET, HttpMethod.POST}, authLevel = AuthorizationLevel.ANONYMOUS) 
        HttpRequestMessage<Optional<String>> request, 
        @QueueOutput(name = "msg", queueName = "outqueue", 
        connection = "AzureWebJobsStorage") OutputBinding<String> msg, 
        final ExecutionContext context) {
    context.getLogger().info("Java HTTP trigger processed a request.");
```

For more information, see the [Java developer guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-java#triggers-and-annotations).

The way that you define triggers and bindings for Node.js functions depends on the specific version of Node.js for Azure Functions:

*   [v4](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings#tabpanel_2_node-v4)
*   [v3](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings#tabpanel_2_node-v3)

In Node.js for Azure Functions version 4, you configure triggers and bindings by using objects exported from the `@azure/functions` module. For more information, see the [Node.js developer guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?pivots=nodejs-model-v4#inputs-and-outputs).

*   [v4](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings#tabpanel_3_node-v4)
*   [v3](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings#tabpanel_3_node-v3)

The `http` method on the exported `app` object defines an HTTP trigger. The `storageQueue` method on `output` defines an output binding on this trigger.

```
const { app, output } = require('@azure/functions');

const queueOutput = output.storageQueue({
    queueName: 'outqueue',
    connection: 'MyStorageConnectionAppSetting',
});

app.http('httpTrigger1', {
    methods: ['GET', 'POST'],
    authLevel: 'anonymous',
    extraOutputs: [queueOutput],
    handler: async (request, context) => {
        const body = await request.text();
        context.extraOutputs.set(queueOutput, body);
        return { body: 'Created queue item.' };
    },
});
```

*   [v4](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings#tabpanel_4_node-v4)
*   [v3](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings#tabpanel_4_node-v3)

The `http` method on the exported `app` object defines an HTTP trigger. The `storageQueue` method on `output` defines an output binding on this trigger.

```
import { app, HttpRequest, HttpResponseInit, InvocationContext, output } from '@azure/functions';

const queueOutput = output.storageQueue({
    queueName: 'outqueue',
    connection: 'MyStorageConnectionAppSetting',
});

export async function httpTrigger1(request: HttpRequest, context: InvocationContext): Promise<HttpResponseInit> {
    const body = await request.text();
    context.extraOutputs.set(queueOutput, body);
    return { body: 'Created queue item.' };
}

app.http('httpTrigger1', {
    methods: ['GET', 'POST'],
    authLevel: 'anonymous',
    extraOutputs: [queueOutput],
    handler: httpTrigger1,
});
```

This example `function.json` file defines the function:

```
{
      "authLevel": "function",
      "type": "httpTrigger",
      "direction": "in",
      "name": "Request",
      "methods": [
        "get",
        "post"
      ]
    },
    {
      "type": "http",
      "direction": "out",
      "name": "Response"
    },
    {
      "type": "queue",
      "direction": "out",
      "name": "msg",
      "queueName": "outqueue",
      "connection": "AzureWebJobsStorage"
    }
  ]
}
```

For more information, see the [PowerShell developer guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-powershell#bindings).

The way that the function is defined depends on the version of Python for Azure Functions:

*   [v2](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings#tabpanel_5_python-v2)
*   [v1](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings#tabpanel_5_python-v1)

In Python for Azure Functions version 2, you define the function directly in code by using decorators:

```
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="HttpExample")
@app.queue_output(arg_name="msg", queue_name="outqueue", connection="AzureWebJobsStorage")
def HttpExample(req: func.HttpRequest, msg: func.Out [func.QueueMessage]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
```

*   Not all services support both input and output bindings. See your specific binding extension for [specific code examples for bindings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings#code-examples-for-bindings).

*   Triggers and bindings are defined differently depending on the development language. Make sure to select your language at the [top](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings#top) of this article.

*   Trigger and binding names are limited to alphanumeric characters and `_`, the underscore.

You can connect your function to other services by using input or output bindings. Add a binding by adding its specific definitions to your function. To learn how, see [Add bindings to an existing function in Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/add-bindings-existing-function).

Azure Functions supports multiple bindings, which must be configured correctly. For example, a function can read data from a queue (input binding) and write data to a database (output binding) simultaneously.

This table shows the bindings that are supported in the major versions of the Azure Functions runtime:

| Type | 4.x 1 | 1.x 2 | Trigger | Input | Output |
| --- | --- | --- | --- | --- | --- |
| [Blob Storage](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob) | ✔ | ✔ | ✔ | ✔ | ✔ |
| [Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2) | ✔ | ✔ | ✔ | ✔ | ✔ |
| [Azure Data Explorer](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-data-explorer) | ✔ |  |  | ✔ | ✔ |
| [Azure SQL](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-sql) | ✔ |  | ✔ | ✔ | ✔ |
| [Dapr](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-dapr)4 | ✔ |  | ✔ | ✔ | ✔ |
| [Event Grid](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-grid) | ✔ | ✔ | ✔ |  | ✔ |
| [Event Hubs](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs) | ✔ | ✔ | ✔ |  | ✔ |
| [HTTP and webhooks](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook) | ✔ | ✔ | ✔ |  | ✔ |
| [IoT Hub](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-iot) | ✔ | ✔ | ✔ |  |  |
| [Kafka](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-kafka)3 | ✔ |  | ✔ |  | ✔ |
| [Mobile Apps](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-mobile-apps) |  | ✔ |  | ✔ | ✔ |
| [Model Context Protocol](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-mcp) | ✔ |  | ✔ |  |  |
| [Notification Hubs](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-notification-hubs) |  | ✔ |  | ✔ |  |
| [Queue Storage](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue) | ✔ | ✔ | ✔ |  | ✔ |
| [Redis](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cache) | ✔ |  | ✔ | ✔ | ✔ |
| [RabbitMQ](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-rabbitmq)3 | ✔ |  | ✔ |  | ✔ |
| [SendGrid](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-sendgrid) | ✔ | ✔ |  |  | ✔ |
| [Service Bus](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus) | ✔ | ✔ | ✔ |  | ✔ |
| [Azure SignalR Service](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-signalr-service) | ✔ |  | ✔ | ✔ | ✔ |
| [Table Storage](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-table) | ✔ | ✔ |  | ✔ | ✔ |
| [Timer](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer) | ✔ | ✔ | ✔ |  |  |
| [Twilio](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-twilio) | ✔ | ✔ |  |  | ✔ |

1.   Register all bindings except HTTP and timer. See [Register Azure Functions binding extensions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-register). This step isn't required when using version 1.x of the Functions runtime.
2.   [Support ends for version 1.x of the Azure Functions runtime on September 14, 2026](https://aka.ms/azure-functions-retirements/hostv1). [Migrate your apps to version 4.x](https://learn.microsoft.com/en-us/azure/azure-functions/migrate-version-1-version-4) for full support.
3.   Triggers aren't supported in the Consumption plan. This binding type requires [runtime-driven triggers](https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options#elastic-premium-plan-with-virtual-network-triggers).
4.   This binding type is supported in Kubernetes, Azure IoT Edge, and other self-hosted modes only.

For information about which bindings are in preview or are approved for production use, see [Supported languages](https://learn.microsoft.com/en-us/azure/azure-functions/supported-languages).

Specific versions of binding extensions are supported only while the underlying service SDK is supported. Changes to support in the underlying service SDK version affect the support for the consuming extension.

Azure Functions binding extensions use Azure service SDKs to connect to Azure services. The specific SDK types used by bindings can affect how you work with the data in your functions. Some bindings support SDK-specific types that provide richer functionality and better integration with the service, while others use more generic types like strings or byte arrays. When available, using SDK-specific types can provide benefits such as better type safety, easier data manipulation, and access to service-specific features.

This table indicates binding extensions that currently support SDK types:

| Extension | Types | Support level |
| --- | --- | --- |
| [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob?tabs=isolated-process,extensionv5&pivots=programming-language-csharp#binding-types) | `BlobClient` `BlobContainerClient` `BlockBlobClient` `PageBlobClient` `AppendBlobClient` | Trigger: GA Input: GA |
| [Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2?tabs=isolated-process,extensionv4&pivots=programming-language-csharp#binding-types) | `CosmosClient` `Database` `Container` | Input: GA |
| [Azure Event Grid](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-grid?tabs=isolated-process,extensionv3&pivots=programming-language-csharp#binding-types) | `CloudEvent` `EventGridEvent` | Trigger: GA |
| [Azure Event Hubs](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs?tabs=isolated-process,extensionv5&pivots=programming-language-csharp#binding-types) | `EventData` `EventHubProducerClient` | Trigger: GA |
| [Azure Queue Storage](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue?tabs=isolated-process,extensionv5&pivots=programming-language-csharp#binding-types) | `QueueClient` `QueueMessage` | Trigger: GA |
| [Azure Service Bus](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus?tabs=isolated-process,extensionv5&pivots=programming-language-csharp#binding-types) | `ServiceBusClient` `ServiceBusReceiver` `ServiceBusSender` `ServiceBusMessage` | Trigger: GA |
| [Azure Table Storage](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-table?tabs=isolated-process,table-api&pivots=programming-language-csharp#binding-types) | `TableClient` `TableEntity` | Input: GA |

Considerations for SDK types:

*   When using [binding expressions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-expressions-patterns) that rely on trigger data, SDK types for the trigger itself cannot be used.
*   For output scenarios where you might use an SDK type, create and work with SDK clients directly instead of using an output binding.
*   The Azure Cosmos DB trigger uses the [Azure Cosmos DB change feed](https://learn.microsoft.com/en-us/azure/cosmos-db/change-feed) and exposes change feed items as JSON-serializable types. As a result, SDK types aren't supported for this trigger.

For more information, see [SDK types](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#sdk-types) in the C# developer guide.

| Extension | Types | Support level | Samples |
| --- | --- | --- | --- |
| [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob) | `BlobClient` `ContainerClient` `StorageStreamDownloader` | Trigger: GA Input: GA | [Quickstart](https://github.com/Azure-Samples/azure-functions-blob-sdk-bindings-python) [`BlobClient`](https://github.com/Azure/azure-functions-python-extensions/blob/dev/azurefunctions-extensions-bindings-blob/samples/blob_samples_blobclient/function_app.py) [`ContainerClient`](https://github.com/Azure/azure-functions-python-extensions/blob/dev/azurefunctions-extensions-bindings-blob/samples/blob_samples_containerclient/function_app.py) [`StorageStreamDownloader`](https://github.com/Azure/azure-functions-python-extensions/blob/dev/azurefunctions-extensions-bindings-blob/samples/blob_samples_storagestreamdownloader/function_app.py) |
| [Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2) | `CosmosClient` `DatabaseProxy` `ContainerProxy` | Input: preview | [Quickstart](https://github.com/Azure-Samples/azure-functions-cosmosdb-sdk-bindings-python) [`ContainerProxy`](https://github.com/Azure/azure-functions-python-extensions/blob/dev/azurefunctions-extensions-bindings-cosmosdb/samples/cosmosdb_samples_containerproxy/function_app.py) [`CosmosClient`](https://github.com/Azure/azure-functions-python-extensions/tree/dev/azurefunctions-extensions-bindings-cosmosdb/samples/cosmosdb_samples_cosmosclient/function_app.py) [`DatabaseProxy`](https://github.com/Azure/azure-functions-python-extensions/tree/dev/azurefunctions-extensions-bindings-cosmosdb/samples/cosmosdb_samples_databaseproxy/function_app.py) |
| [Azure Event Hubs](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs) | `EventData` | Trigger: preview | [Quickstart](https://github.com/Azure-Samples/azure-functions-eventhub-sdk-bindings-python) [`EventData`](https://github.com/Azure/azure-functions-python-extensions/blob/dev/azurefunctions-extensions-bindings-eventhub/samples/eventhub_samples_eventdata/function_app.py) |
| [Azure Service Bus](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus) | `ServiceBusReceivedMessage` | Trigger: preview | [Quickstart](https://github.com/Azure/azure-functions-python-extensions/blob/dev/azurefunctions-extensions-bindings-servicebus/samples/README.md) [`ServiceBusReceivedMessage`](https://github.com/Azure/azure-functions-python-extensions/blob/dev/azurefunctions-extensions-bindings-servicebus/samples/servicebus_samples_single/function_app.py) |

Considerations for SDK types:

*   For output scenarios where you might use an SDK type, create and work with SDK clients directly instead of using an output binding.
*   The Azure Cosmos DB trigger uses the [Azure Cosmos DB change feed](https://learn.microsoft.com/en-us/azure/cosmos-db/change-feed) and exposes change feed items as JSON-serializable types. As a result, SDK types aren't supported for this trigger.

SDK types are supported only when using the Python v2 programming model. For more information, see [SDK type bindings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python#sdk-type-bindings) in the Python developer guide.

| Extension | Types | Support level |
| --- | --- | --- |
| [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob) | `BlobClient` `ContainerClient` `ReadableStream` | Preview |
| [Azure Service Bus](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus) | `ServiceBusClient` `ServiceBusReceiver` `ServiceBusSender` `ServiceBusMessage` | Preview |

SDK types are supported only when using the Node v4 programming model. For more information, see [SDK types](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node#sdk-types) in the Node.js developer guide.

| Extension | Types | Support level |
| --- | --- | --- |
| [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob) | `BlobClient` `BlobContainerClient` | Preview |

For more information, see [SDK types](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-java#sdk-types) in the Java developer guide.

Important

SDK types aren't currently supported for PowerShell apps.

Use the following table to find more examples of specific binding types that show you how to work with bindings in your functions. First, choose the language tab that corresponds to your project.

Binding code for C# depends on the [specific process model](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#benefits-of-the-isolated-worker-model).

*   [Isolated process](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings#tabpanel_1_isolated-process)
*   [In-process](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings#tabpanel_1_in-process)

| Service | Examples | Samples |
| --- | --- | --- |
| Blob Storage | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?tabs=isolated-process&pivots=programming-language-csharp#example) [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-input?tabs=isolated-process&pivots=programming-language-csharp#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-output?tabs=isolated-process&pivots=programming-language-csharp#example) | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/storage/Microsoft.Azure.WebJobs.Extensions.Storage.Blobs) |
| Azure Cosmos DB | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2-trigger?tabs=isolated-process&pivots=programming-language-csharp#example) [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2-input?tabs=isolated-process&pivots=programming-language-csharp#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2-output?tabs=isolated-process&pivots=programming-language-csharp#example) | [Link](https://github.com/Azure/azure-webjobs-sdk-extensions/tree/dev/sample/ExtensionsSample/Samples) |
| Azure Data Explorer | [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-data-explorer-input?pivots=programming-language-csharp#examples) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-data-explorer-output?pivots=programming-language-csharp#examples) | [Link](https://github.com/Azure/Webjobs.Extensions.Kusto/tree/main/samples/samples-csharp) |
| Azure SQL | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-sql-trigger?tabs=isolated-process&pivots=programming-language-csharp#example) [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-sql-input?tabs=isolated-process&pivots=programming-language-csharp#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-sql-output?tabs=isolated-process&pivots=programming-language-csharp#example) | [Link](https://learn.microsoft.com/en-us/samples/azure-samples/azure-sql-binding-func-dotnet-todo/todo-backend-dotnet-azure-sql-bindings-azure-functions/) |
| Event Grid | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-grid-trigger?tabs=isolated-process&pivots=programming-language-csharp#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-grid-output?tabs=isolated-process&pivots=programming-language-csharp#example) | [Link](https://github.com/Azure/azure-webjobs-sdk-extensions/tree/dev/sample/ExtensionsSample/Samples) |
| Event Hubs | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs-trigger?tabs=isolated-process&pivots=programming-language-csharp#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs-output?tabs=isolated-process&pivots=programming-language-csharp#example) |  |
| IoT Hub | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-iot-trigger?tabs=isolated-process&pivots=programming-language-csharp#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-iot-output?tabs=isolated-process&pivots=programming-language-csharp#example) |  |
| HTTP | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger?tabs=isolated-process&pivots=programming-language-csharp#example) | [Link](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd) |
| Queue Storage | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue-trigger?tabs=isolated-process&pivots=programming-language-csharp#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue-output?tabs=isolated-process&pivots=programming-language-csharp#example) | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/storage/Microsoft.Azure.WebJobs.Extensions.Storage.Queues/samples/functionapp) |
| RabbitMQ | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-rabbitmq-trigger?tabs=isolated-process&pivots=programming-language-csharp#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-rabbitmq-output?tabs=isolated-process&pivots=programming-language-csharp#example) |  |
| SendGrid | [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-sendgrid?tabs=isolated-process&pivots=programming-language-csharp#example) |  |
| Service Bus | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus-trigger?tabs=isolated-process&pivots=programming-language-csharp#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus-output?tabs=isolated-process&pivots=programming-language-csharp#example) | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/servicebus/Microsoft.Azure.WebJobs.Extensions.ServiceBus) |
| Azure SignalR Service | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-signalr-service-trigger?tabs=isolated-process&pivots=programming-language-csharp#example) [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-signalr-service-input?tabs=isolated-process&pivots=programming-language-csharp#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-signalr-service-output?tabs=isolated-process&pivots=programming-language-csharp) |  |
| Table Storage | [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-table-input?tabs=isolated-process&pivots=programming-language-csharp) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-table-output?tabs=isolated-process&pivots=programming-language-csharp) |  |
| Timer | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer?tabs=isolated-process&pivots=programming-language-csharp#example) | [Link](https://github.com/Azure/azure-webjobs-sdk-extensions/tree/dev/sample/ExtensionsSample/Samples) |
| Twilio | [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-twilio?tabs=isolated-process&pivots=programming-language-csharp#example) | [Link](https://github.com/Azure/azure-webjobs-sdk-extensions/tree/dev/sample/ExtensionsSample/Samples) |

| Service | Examples | Samples |
| --- | --- | --- |
| Blob Storage | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?pivots=programming-language-java#example) [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-input?pivots=programming-language-java#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-output?pivots=programming-language-java#example) | [Link](https://github.com/Azure-Samples/azure-functions-samples-java/tree/master/triggers-bindings/src/main/java/com/functions) |
| Azure Cosmos DB | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2-trigger?pivots=programming-language-java#example) [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2-input?pivots=programming-language-java#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2-output?pivots=programming-language-java#example) | [Link](https://github.com/Azure-Samples/java-functions-eventhub-cosmosdb) |
| Azure Data Explorer | [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-data-explorer-input?pivots=programming-language-java#examples) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-data-explorer-output?pivots=programming-language-java#examples) | [Link](https://github.com/Azure/Webjobs.Extensions.Kusto/tree/main/samples/samples-java) |
| Azure SQL | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-sql-trigger?pivots=programming-language-java#example) [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-sql-input?pivots=programming-language-java#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-sql-output?pivots=programming-language-java#example) |  |
| Event Grid | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-grid-trigger?pivots=programming-language-java#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-grid-output?pivots=programming-language-java#example) | [Link](https://github.com/Azure-Samples/azure-functions-samples-java/tree/master/triggers-bindings/src/main/java/com/functions) |
| Event Hubs | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs-trigger?pivots=programming-language-java#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs-output?pivots=programming-language-java#example) |  |
| IoT Hub | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-iot-trigger?pivots=programming-language-java#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-iot-output?pivots=programming-language-java#example) |  |
| HTTP | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger?pivots=programming-language-java#example) | [Link](https://github.com/Azure-Samples/azure-functions-samples-java/tree/master/triggers-bindings/src/main/java/com/functions) |
| Queue Storage | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue-trigger?pivots=programming-language-java#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue-output?pivots=programming-language-java#example) | [Link](https://github.com/Azure-Samples/azure-functions-samples-java/tree/master/triggers-bindings/src/main/java/com/functions) |
| RabbitMQ | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-rabbitmq-trigger?pivots=programming-language-java#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-rabbitmq-output?pivots=programming-language-java#example) |  |
| SendGrid | [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-sendgrid?pivots=programming-language-java#example) |  |
| Service Bus | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus-trigger?pivots=programming-language-java#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus-output?pivots=programming-language-java#example) | [Link](https://github.com/Azure-Samples/azure-functions-samples-java/tree/master/triggers-bindings/src/main/java/com/functions) |
| Azure SignalR Service | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-signalr-service-trigger?pivots=programming-language-java#example) [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-signalr-service-input?pivots=programming-language-java#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-signalr-service-output?pivots=programming-language-java) |  |
| Table Storage | [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-table-input?pivots=programming-language-java) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-table-output?pivots=programming-language-java) |  |
| Timer | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer?pivots=programming-language-java#example) | [Link](https://github.com/Azure-Samples/azure-functions-samples-java/tree/master/triggers-bindings/src/main/java/com/functions) |
| Twilio | [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-twilio?pivots=programming-language-java#example) |  |

| Service | Examples | Samples |
| --- | --- | --- |
| Blob Storage | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?pivots=programming-language-javascript#example) [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-input?pivots=programming-language-javascript#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-output?pivots=programming-language-javascript#example) | [Link](https://github.com/Azure-Samples/azure-functions-blob-sdk-bindings-nodejs) |
| Azure Cosmos DB | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2-trigger?pivots=programming-language-javascript#example) [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2-input?pivots=programming-language-javascript#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2-output?pivots=programming-language-javascript#example) | [Link](https://github.com/Azure-Samples/functions-docs-javascript/tree/master/functions-add-output-binding-cosmosdb-cli-v4-programming-model) |
| Azure Data Explorer | [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-data-explorer-input?pivots=programming-language-javascript#examples) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-data-explorer-output?pivots=programming-language-javascript#examples) |  |
| Azure SQL | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-sql-trigger?pivots=programming-language-javascript#example) [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-sql-input?pivots=programming-language-javascript#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-sql-output?pivots=programming-language-javascript#example) | [Link](https://github.com/Azure/Webjobs.Extensions.Kusto/tree/main/samples/samples-node) |
| Event Grid | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-grid-trigger?pivots=programming-language-javascript#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-grid-output?pivots=programming-language-javascript#example) |  |
| Event Hubs | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs-trigger?pivots=programming-language-javascript#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs-output?pivots=programming-language-javascript#example) |  |
| IoT Hub | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-iot-trigger?pivots=programming-language-javascript#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-iot-output?pivots=programming-language-javascript#example) |  |
| HTTP | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger?pivots=programming-language-javascript#example) | [Link](https://github.com/Azure-Samples/functions-docs-javascript/tree/master/functions-typescript) |
| Queue Storage | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue-trigger?pivots=programming-language-javascript#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue-output?pivots=programming-language-javascript#example) | [Link](https://github.com/Azure-Samples/functions-docs-javascript/tree/master/functions-add-output-binding-storage-queue-cli-v4-programming-model) |
| RabbitMQ | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-rabbitmq-trigger?pivots=programming-language-javascript#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-rabbitmq-output?pivots=programming-language-javascript#example) |  |
| SendGrid | [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-sendgrid?pivots=programming-language-javascript#example) |  |
| Service Bus | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus-trigger?pivots=programming-language-javascript#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus-output?pivots=programming-language-javascript#example) | [Link](https://github.com/Azure-Samples/azure-functions-servicebus-sdk-bindings-nodejs/tree/main/serviceBusSampleWithComplete) |
| Azure SignalR Service | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-signalr-service-trigger?pivots=programming-language-javascript#example) [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-signalr-service-input?pivots=programming-language-javascript#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-signalr-service-output?pivots=programming-language-javascript) |  |
| Table Storage | [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-table-input?pivots=programming-language-javascript) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-table-output?pivots=programming-language-javascript) |  |
| Timer | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer?pivots=programming-language-javascript#example) |  |
| Twilio | [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-twilio?pivots=programming-language-javascript#example) |  |

| Service | Examples | Samples |
| --- | --- | --- |
| Blob Storage | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?pivots=programming-language-powershell#example) [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-input?pivots=programming-language-powershell#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-output?pivots=programming-language-powershell#example) |  |
| Azure Cosmos DB | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2-trigger?pivots=programming-language-powershell#example) [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2-input?pivots=programming-language-powershell#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2-output?pivots=programming-language-powershell#example) |  |
| Azure SQL | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-sql-trigger?pivots=programming-language-powershell#example) [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-sql-input?pivots=programming-language-powershell#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-sql-output?pivots=programming-language-powershell#example) |  |
| Event Grid | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-grid-trigger?pivots=programming-language-powershell#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-grid-output?pivots=programming-language-powershell#example) |  |
| Event Hubs | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs-trigger?pivots=programming-language-powershell#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs-output?pivots=programming-language-powershell#example) |  |
| IoT Hub | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-iot-trigger?pivots=programming-language-powershell#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-iot-output?pivots=programming-language-powershell#example) |  |
| HTTP | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger?pivots=programming-language-powershell#example) | [Link](https://github.com/Azure-Samples/functions-quickstart-powershell-azd) |
| Queue Storage | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue-trigger?pivots=programming-language-powershell#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue-output?pivots=programming-language-powershell#example) |  |
| RabbitMQ | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-rabbitmq-trigger?pivots=programming-language-powershell#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-rabbitmq-output?pivots=programming-language-powershell#example) |  |
| SendGrid | [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-sendgrid?pivots=programming-language-powershell#example) |  |
| Service Bus | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus-trigger?pivots=programming-language-powershell#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus-output?pivots=programming-language-powershell#example) |  |
| Azure SignalR Service | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-signalr-service-trigger?pivots=programming-language-powershell#example) [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-signalr-service-input?pivots=programming-language-powershell#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-signalr-service-output?pivots=programming-language-powershell) |  |
| Table Storage | [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-table-input?pivots=programming-language-powershell) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-table-output?pivots=programming-language-powershell) |  |
| Timer | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer?pivots=programming-language-powershell#example) |  |
| Twilio | [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-twilio?pivots=programming-language-powershell#example) |  |

Binding code for Python depends on the Python model version.

*   [v2](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings#tabpanel_2_python-v2)
*   [v1](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings#tabpanel_2_python-v1)

| Service | Examples | Samples |
| --- | --- | --- |
| Blob Storage | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?tabs=python-v2&pivots=programming-language-python#example) [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-input?tabs=python-v2&pivots=programming-language-python#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-output?tabs=python-v2&pivots=programming-language-python#example) | [Link](https://github.com/Azure-Samples/azure-functions-blob-sdk-bindings-python) |
| Azure Cosmos DB | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2-trigger?tabs=python-v2&pivots=programming-language-python#example) [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2-input?tabs=python-v2&pivots=programming-language-python#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2-output?tabs=python-v2&pivots=programming-language-python#example) | [Link](https://github.com/Azure-Samples/functions-quickstart-python-azd-cosmosdb) |
| Azure Data Explorer | [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-data-explorer-input?pivots=programming-language-python#examples) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-data-explorer-output?pivots=programming-language-python#examples) |  |
| Azure SQL | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-sql-trigger?tabs=python-v2&pivots=programming-language-python#example) [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-sql-input?tabs=python-v2&pivots=programming-language-python#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-sql-output?tabs=python-v2&pivots=programming-language-python#example) | [Link](https://github.com/Azure/Webjobs.Extensions.Kusto/tree/main/samples/samples-python) |
| Event Grid | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-grid-trigger?tabs=python-v2&pivots=programming-language-python#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-grid-output?tabs=python-v2&pivots=programming-language-python#example) |  |
| Event Hubs | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs-trigger?tabs=python-v2&pivots=programming-language-python#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs-output?tabs=python-v2&pivots=programming-language-python#example) |  |
| IoT Hub | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-iot-trigger?tabs=python-v2&pivots=programming-language-python#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-iot-output?tabs=python-v2&pivots=programming-language-python#example) |  |
| HTTP | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger?tabs=python-v2&pivots=programming-language-python#example) | [Link](https://github.com/Azure-Samples/functions-quickstart-python-http-azd) |
| Queue Storage | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue-trigger?tabs=python-v2&pivots=programming-language-python#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue-output?tabs=python-v2&pivots=programming-language-python#example) |  |
| RabbitMQ | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-rabbitmq-trigger?tabs=python-v2&pivots=programming-language-python#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-rabbitmq-output?tabs=python-v2&pivots=programming-language-python#example) |  |
| SendGrid | [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-sendgrid?tabs=python-v2&pivots=programming-language-python#example) |  |
| Service Bus | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus-trigger?tabs=python-v2&pivots=programming-language-python#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus-output?tabs=python-v2&pivots=programming-language-python#example) | [Link](https://github.com/Azure-Samples/functions-quickstart-python-azd-service-bus) |
| Azure SignalR Service | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-signalr-service-trigger?tabs=python-v2&pivots=programming-language-python#example) [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-signalr-service-input?tabs=python-v2&pivots=programming-language-python#example) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-signalr-service-output?tabs=python-v2&pivots=programming-language-python) |  |
| Table Storage | [Input](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-table-input?tabs=python-v2&pivots=programming-language-python) [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-table-output?tabs=python-v2&pivots=programming-language-python) |  |
| Timer | [Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer?tabs=python-v2&pivots=programming-language-python#example) |  |
| Twilio | [Output](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-twilio?tabs=python-v2&pivots=programming-language-python#example) |  |

You can create custom input and output bindings. Bindings must be authored in .NET, but they can be consumed from any supported language. For more information about creating custom bindings, see [Creating custom input and output bindings](https://github.com/Azure/azure-webjobs-sdk/wiki/Creating-custom-input-and-output-bindings).

*   [Binding expressions and patterns](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-expressions-patterns)
*   [Register Azure Functions binding extensions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-register)
*   [Manually run a non-HTTP-triggered function](https://learn.microsoft.com/en-us/azure/azure-functions/functions-manually-run-non-http)
*   [Handling binding errors](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-error-pages)
