# Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios

Title: Azure Functions Scenarios

URL Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios

Markdown Content:
Often, you build systems that react to a series of critical events. Whether you're building a web API, responding to database changes, or processing event streams or messages, you can use Azure Functions to implement these systems.

In many cases, a function [integrates with an array of cloud services](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings) to provide feature-rich implementations. The following list shows common (but by no means exhaustive) scenarios for Azure Functions.

Select your development language at the top of the article.

You can use functions in several ways to process files into or out of a blob storage container. To learn more about options for triggering on a blob container, see [Working with blobs](https://learn.microsoft.com/en-us/azure/azure-functions/storage-considerations#working-with-blobs) in the best practices documentation.

For example, in a retail solution, a partner system can submit product catalog information as files into blob storage. You can use a blob triggered function to validate, transform, and process the files into the main system as you upload them.

[![Image 1: Diagram of a file upload process using Azure Functions.](https://learn.microsoft.com/en-us/azure/azure-functions/media/functions-scenarios/process-file-uploads.png)](https://learn.microsoft.com/en-us/azure/azure-functions/media/functions-scenarios/process-file-uploads-expanded.png#lightbox)

The following tutorials use a Blob trigger (Event Grid based) to process files in a blob container:

*   [Quickstart: Respond to blob storage events by using Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/scenario-blob-storage-events)
*   [Sample: Blob trigger with the Event Grid source type quickstart sample)](https://github.com/Azure-Samples/functions-quickstart-python-azd-eventgrid-blob)
*   [Tutorial: Trigger Azure Functions on blob containers using an event subscription](https://learn.microsoft.com/en-us/azure/azure-functions/functions-event-grid-blob-trigger?pivots=programming-language-python)

*   [Quickstart: Respond to blob storage events by using Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/scenario-blob-storage-events)
*   [Sample: Blob trigger with the Event Grid source type quickstart sample)](https://github.com/Azure-Samples/functions-quickstart-javascript-azd-eventgrid-blob)
*   [Tutorial (events): Trigger Azure Functions on blob containers using an event subscription](https://learn.microsoft.com/en-us/azure/azure-functions/functions-event-grid-blob-trigger?pivots=programming-language-javascript)
*   [Tutorial (polling): Upload and analyze a file with Azure Functions and Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/blob-upload-function-trigger-javascript)

*   [Quickstart: Respond to blob storage events by using Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/scenario-blob-storage-events)
*   [Sample: Blob trigger with the Event Grid source type quickstart sample)](https://github.com/Azure-Samples/functions-quickstart-powershell-azd-eventgrid-blob)
*   [Tutorial: Trigger Azure Functions on blob containers using an event subscription](https://learn.microsoft.com/en-us/azure/azure-functions/functions-event-grid-blob-trigger?pivots=programming-language-powershell)

*   [Quickstart: Respond to blob storage events by using Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/scenario-blob-storage-events)
*   [Sample: lob trigger with the Event Grid source type quickstart sample)](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-eventgrid-blob)
*   [Tutorial: Trigger Azure Functions on blob containers using an event subscription](https://learn.microsoft.com/en-us/azure/azure-functions/functions-event-grid-blob-trigger?pivots=programming-language-typescript)

*   [Quickstart: Respond to blob storage events by using Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/scenario-blob-storage-events)
*   [Sample: Blob trigger with the Event Grid source type quickstart sample)](https://github.com/Azure-Samples/functions-quickstart-java-azd-eventgrid-blob)
*   [Tutorial: Trigger Azure Functions on blob containers using an event subscription](https://learn.microsoft.com/en-us/azure/azure-functions/functions-event-grid-blob-trigger?pivots=programming-language-java)

Cloud applications, IoT devices, and networking devices generate and collect a large amount of telemetry. Azure Functions can process that data in near real-time as the hot path, then store it in [Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/introduction) for use in an analytics dashboard.

Your functions can also use low-latency event triggers, like Event Grid, and real-time outputs like SignalR to process data in near-real-time.

[![Image 2: Diagram of a real-time stream process using Azure Functions.](https://learn.microsoft.com/en-us/azure/azure-functions/media/functions-scenarios/real-time-stream-processing.png)](https://learn.microsoft.com/en-us/azure/azure-functions/media/functions-scenarios/real-time-stream-processing-expanded.png#lightbox)

For example, you can use the event hubs trigger to read from an event hub and the output binding to write to an event hub after debatching and transforming the events:

```
[FunctionName("ProcessorFunction")]
public static async Task Run(
    [EventHubTrigger(
        "%Input_EH_Name%",
        Connection = "InputEventHubConnectionSetting",
        ConsumerGroup = "%Input_EH_ConsumerGroup%")] EventData[] inputMessages,
    [EventHub(
        "%Output_EH_Name%",
        Connection = "OutputEventHubConnectionSetting")] IAsyncCollector<SensorDataRecord> outputMessages,
    PartitionContext partitionContext,
    ILogger log)
{
    var debatcher = new Debatcher(log);
    var debatchedMessages = await debatcher.Debatch(inputMessages, partitionContext.PartitionId);

    var xformer = new Transformer(log);
    await xformer.Transform(debatchedMessages, partitionContext.PartitionId, outputMessages);
}
```

*   [Streaming at scale with Azure Event Hubs, Functions and Azure SQL](https://github.com/Azure-Samples/streaming-at-scale/tree/main/eventhubs-functions-azuresql)
*   [Streaming at scale with Azure Event Hubs, Functions and Cosmos DB](https://github.com/Azure-Samples/streaming-at-scale/tree/main/eventhubs-functions-cosmosdb)
*   [Streaming at scale with Azure Event Hubs with Kafka producer, Functions with Kafka trigger and Cosmos DB](https://github.com/Azure-Samples/streaming-at-scale/tree/main/eventhubskafka-functions-cosmosdb)
*   [Streaming at scale with Azure IoT Hub, Functions and Azure SQL](https://github.com/Azure-Samples/streaming-at-scale/tree/main/iothub-functions-azuresql)
*   [Azure Event Hubs trigger for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs-trigger?pivots=programming-language-csharp)
*   [Apache Kafka trigger for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-kafka-trigger?pivots=programming-language-csharp)

*   [Azure Event Hubs trigger for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs-trigger?pivots=programming-language-python)
*   [Apache Kafka trigger for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-kafka-trigger?pivots=programming-language-python)

*   [Azure Event Hubs trigger for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs-trigger?pivots=programming-language-javascript)
*   [Apache Kafka trigger for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-kafka-trigger?pivots=programming-language-javascript)

*   [Azure Event Hubs trigger for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs-trigger?pivots=programming-language-powershell)
*   [Apache Kafka trigger for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-kafka-trigger?pivots=programming-language-powershell)

*   [Azure Functions Kafka trigger Java Sample](https://github.com/azure/azure-functions-kafka-extension/tree/main/samples/WalletProcessing_KafkademoSample)
*   [Azure Event Hubs trigger for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs-trigger?pivots=programming-language-java)
*   [Apache Kafka trigger for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-kafka-trigger?pivots=programming-language-java)

Azure Functions provides serverless compute resources that integrate with AI and Azure services to streamline building cloud-hosted intelligent applications. You can use the Functions programming model to create and host remote Model Content Protocol (MCP) servers and implement various AI tools. For more information, see [Tools and MCP servers](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-ai-enabled-apps#tools-and-mcp-servers).

The [Azure OpenAI binding extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-openai) lets you integrate AI features and behaviors of the [Azure OpenAI service](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview), such as retrieval-augmented generation (RAG), into your function code executions. For more information, see [Retrieval-augmented generation](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-ai-enabled-apps#retrieval-augmented-generation).

A function might also call a TensorFlow model or Foundry Tools to process and classify a stream of images.

[![Image 3: Diagram of a machine learning and AI process using Azure Functions.](https://learn.microsoft.com/en-us/azure/azure-functions/media/functions-scenarios/machine-learning-and-ai.png)](https://learn.microsoft.com/en-us/azure/azure-functions/media/functions-scenarios/machine-learning-and-ai-expanded.png#lightbox)

*   [Tools and MCP servers](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios#tabpanel_1_mcp-tools)
*   [Azure OpenAI service](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios#tabpanel_1_open-ai)

*   [Quickstart: Build a custom remote MCP server using Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/scenario-custom-remote-mcp-server)
*   [Quickstart: Host servers built with MCP SDKs on Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/scenario-host-mcp-server-sdks)
*   [Sample: Getting Started with Remote MCP Servers using Azure Functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
*   [Sample: Host remote MCP servers built with official MCP SDKs on Azure Functions](https://github.com/Azure-Samples/mcp-sdk-functions-hosting-dotnet)

*   [Tools and MCP servers](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios#tabpanel_2_mcp-tools)
*   [Azure OpenAI service](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios#tabpanel_2_open-ai)

*   [Quickstart: Build a custom remote MCP server using Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/scenario-custom-remote-mcp-server)
*   [Sample: Getting Started with Remote MCP Servers using Azure Functions](https://github.com/Azure-Samples/remote-mcp-functions-java)

*   [Tutorial: Text completion using Azure OpenAI](https://learn.microsoft.com/en-us/azure/azure-functions/functions-add-openai-text-completion?pivots=programming-language-javascript)
*   [Training: Create a custom skill for Azure AI Search](https://learn.microsoft.com/en-us/training/modules/create-enrichment-pipeline-azure-cognitive-search)
*   [Sample: Chat using ChatGPT](https://github.com/Azure-Samples/function-javascript-ai-openai-chatgpt)
*   [Sample: Upload text files and access data using various OpenAI features](https://github.com/azure-samples/azure-functions-openai-demo)

*   [Tools and MCP servers](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios#tabpanel_3_mcp-tools)
*   [Azure OpenAI service](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios#tabpanel_3_open-ai)

*   [Quickstart: Build a custom remote MCP server using Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/scenario-custom-remote-mcp-server)
*   [Quickstart: Host servers built with MCP SDKs on Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/scenario-host-mcp-server-sdks)
*   [Sample: Getting Started with Remote MCP Servers using Azure Functions](https://github.com/Azure-Samples/remote-mcp-functions-typescript)
*   [Sample: Host remote MCP servers built with official MCP SDKs on Azure Functions](https://github.com/Azure-Samples/mcp-sdk-functions-hosting-node)

*   [Tools and MCP servers](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios#tabpanel_4_mcp-tools-2)
*   [Azure OpenAI service](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios#tabpanel_4_open-ai-2)
*   [Data models](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios#tabpanel_4_data-models)

*   [Quickstart: Build a custom remote MCP server using Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/scenario-custom-remote-mcp-server)
*   [Quickstart: Host servers built with MCP SDKs on Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/scenario-host-mcp-server-sdks)

*   [Tutorial: Text completion using Azure OpenAI](https://learn.microsoft.com/en-us/azure/azure-functions/functions-add-openai-text-completion?pivots=programming-language-powershell)
*   [Sample: Text completion using Azure OpenAI](https://github.com/Azure/azure-functions-openai-extension/tree/main/samples/textcompletion/powershell)
*   [Sample: Provide assistant skills to your model](https://github.com/Azure/azure-functions-openai-extension/tree/main/samples/assistant/powershell)
*   [Sample: Generate embeddings](https://github.com/Azure/azure-functions-openai-extension/tree/main/samples/embeddings/powershell)
*   [Sample: Leverage semantic search](https://github.com/Azure/azure-functions-openai-extension/tree/main/samples/rag-aisearch/powershell)

For more information, see [Use AI tools and models in Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-ai-enabled-apps).

Functions enables you to run your code based on a [cron schedule](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer#usage) that you define.

See [Create a function in the Azure portal that runs on a schedule](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-scheduled-function).

For example, you might analyze a financial services customer database for duplicate entries every 15 minutes to avoid multiple communications going out to the same customer.

[![Image 4: Diagram of a scheduled task where a function cleans a database every 15 minutes deduplicating entries based on business logic.](https://learn.microsoft.com/en-us/azure/azure-functions/media/functions-scenarios/scheduled-task.png)](https://learn.microsoft.com/en-us/azure/azure-functions/media/functions-scenarios/scheduled-task-expanded.png#lightbox)

For examples, see these code snippets:

```
[FunctionName("TimerTriggerCSharp")]
public static void Run([TimerTrigger("0 */15 * * * *")]TimerInfo myTimer, ILogger log)
{
    if (myTimer.IsPastDue)
    {
        log.LogInformation("Timer is running late!");
    }
    log.LogInformation($"C# Timer trigger function executed at: {DateTime.Now}");

    // Perform the database deduplication
}
```

*   [Quickstart: Azure Functions Timer trigger](https://learn.microsoft.com/en-us/azure/azure-functions/scenario-scheduled-tasks?pivots=programming-language-csharp)

*   [Quickstart: Azure Functions Timer trigger](https://learn.microsoft.com/en-us/azure/azure-functions/scenario-scheduled-tasks?pivots=programming-language-python)

An HTTP triggered function defines an HTTP endpoint. These endpoints run function code that can connect to other services directly or by using binding extensions. You can compose the endpoints into a web-based API.

You can also use an HTTP triggered function endpoint as a webhook integration, such as GitHub webhooks. In this way, you can create functions that process data from GitHub events. For more information, see [Monitor GitHub events by using a webhook with Azure Functions](https://learn.microsoft.com/en-us/training/modules/monitor-github-events-with-a-function-triggered-by-a-webhook/).

[![Image 5: Diagram of processing an HTTP request using Azure Functions.](https://learn.microsoft.com/en-us/azure/azure-functions/media/functions-scenarios/scalable-web-api.png)](https://learn.microsoft.com/en-us/azure/azure-functions/media/functions-scenarios/scalable-web-api-expanded.png#lightbox)

For examples, see these code snippets:

*   [Quickstart: Azure Functions HTTP trigger](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-azure-developer-cli?pivots=programming-language-python)

*   [Quickstart: Azure Functions HTTP trigger](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-azure-developer-cli?pivots=programming-language-javascript)

*   [Quickstart: Azure Functions HTTP trigger](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-azure-developer-cli?pivots=programming-language-powershell)

*   [Quickstart: Azure Functions HTTP trigger](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-azure-developer-cli?pivots=programming-language-typescript)

*   [Quickstart: Azure Functions HTTP trigger](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-azure-developer-cli?pivots=programming-language-java)

Functions often serve as the compute component in a serverless workflow topology, such as a Logic Apps workflow. You can also create long-running orchestrations by using the Durable Functions extension. For more information, see [Durable Functions overview](https://learn.microsoft.com/en-us/azure/azure-functions/durable/what-is-durable-task).

[![Image 6: A combination diagram of a series of specific serverless workflows using Azure Functions.](https://learn.microsoft.com/en-us/azure/azure-functions/media/functions-scenarios/build-a-serverless-workflow.png)](https://learn.microsoft.com/en-us/azure/azure-functions/media/functions-scenarios/build-a-serverless-workflow-expanded.png#lightbox)

*   [Tutorial: Create a function to integrate with Azure Logic Apps](https://learn.microsoft.com/en-us/azure/azure-functions/functions-twitter-email)
*   [Quickstart: Create your first durable function in Azure using C#](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-isolated-create-first-csharp)
*   [Training: Deploy serverless APIs with Azure Functions, Logic Apps, and Azure SQL Database](https://learn.microsoft.com/en-us/training/modules/deploy-backend-apis/)

*   [Quickstart: Create your first durable function in Azure using JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/durable/quickstart-js-vscode)
*   [Training: Deploy serverless APIs with Azure Functions, Logic Apps, and Azure SQL Database](https://learn.microsoft.com/en-us/training/modules/deploy-backend-apis/)

*   [Quickstart: Create your first durable function in Azure using JavaScript](https://learn.microsoft.com/en-us/azure/azure-functions/durable/quickstart-ts-vscode)
*   [Training: Deploy serverless APIs with Azure Functions, Logic Apps, and Azure SQL Database](https://learn.microsoft.com/en-us/training/modules/deploy-backend-apis/)

*   [Quickstart: Create your first durable function in Azure using Python](https://learn.microsoft.com/en-us/azure/azure-functions/durable/quickstart-python-vscode)
*   [Training: Deploy serverless APIs with Azure Functions, Logic Apps, and Azure SQL Database](https://learn.microsoft.com/en-us/training/modules/deploy-backend-apis/)

*   [Quickstart: Create your first durable function in Azure using Java](https://learn.microsoft.com/en-us/azure/azure-functions/durable/quickstart-java)

*   [Quickstart: Create your first durable function in Azure using PowerShell](https://learn.microsoft.com/en-us/azure/azure-functions/durable/quickstart-powershell-vscode)

Some processes need to log, audit, or perform other operations when stored data changes. Functions triggers provide a good way to get notified of data changes to initial such an operation.

[![Image 7: Diagram of a function being used to respond to database changes.](https://learn.microsoft.com/en-us/azure/azure-functions/media/functions-scenarios/respond-to-database-changes.png)](https://learn.microsoft.com/en-us/azure/azure-functions/media/functions-scenarios/respond-to-database-changes-expanded.png#lightbox)

*   [Sample: Azure Functions with Azure Cosmos DB (trigger)](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-cosmosdb)

*   [Sample: Azure Functions with Azure SQL Database (trigger)](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-sql)

*   [Sample: Azure Functions with Azure Cosmos DB Trigger](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-cosmosdb)

*   [Sample: Azure Functions with Azure SQL Database (trigger)](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-sql)

*   [Sample: Azure Functions with Azure Cosmos DB Trigger](https://github.com/Azure-Samples/functions-quickstart-python-azd-cosmosdb)

*   [Sample: Azure Functions with Azure SQL Database (trigger)](https://github.com/Azure-Samples/functions-quickstart-python-azd-sql)

You can use Functions with Azure messaging services to create advanced event-driven messaging solutions.

For example, you can use triggers on Azure Storage queues as a way to chain together a series of function executions. Or use service bus queues and triggers for an online ordering system.

[![Image 8: Diagram of Azure Functions in a reliable message system.](https://learn.microsoft.com/en-us/azure/azure-functions/media/functions-scenarios/create-reliable-message-systems.png)](https://learn.microsoft.com/en-us/azure/azure-functions/media/functions-scenarios/create-reliable-message-systems-expanded.png#lightbox)

These articles show how to write output to a storage queue:

*   [Article: Connect Azure Functions to Azure Storage using Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/functions-add-output-binding-storage-queue-vs-code?pivots=programming-language-csharp&tabs=isolated-process)
*   [Article: Create a function triggered by Azure Queue storage (Azure portal)](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-storage-queue-triggered-function)

*   [Article: Connect Azure Functions to Azure Storage using Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/functions-add-output-binding-storage-queue-vs-code?pivots=programming-language-javascript)
*   [Article: Create a function triggered by Azure Queue storage (Azure portal)](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-storage-queue-triggered-function)
*   [Training: Chain Azure Functions together using input and output bindings](https://learn.microsoft.com/en-us/training/modules/chain-azure-functions-data-using-bindings/)

*   [Article: Connect Azure Functions to Azure Storage using Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/functions-add-output-binding-storage-queue-vs-code?pivots=programming-language-python)
*   [Article: Create a function triggered by Azure Queue storage (Azure portal)](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-storage-queue-triggered-function)

*   [Article: Connect Azure Functions to Azure Storage using Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/functions-add-output-binding-storage-queue-vs-code?pivots=programming-language-java)
*   [Article: Create a function triggered by Azure Queue storage (Azure portal)](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-storage-queue-triggered-function)

*   [Article: Connect Azure Functions to Azure Storage using Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/functions-add-output-binding-storage-queue-vs-code?pivots=programming-language-powershell)
*   [Article: Create a function triggered by Azure Queue storage (Azure portal)](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-storage-queue-triggered-function)
*   [Training: Chain Azure Functions together using input and output bindings](https://learn.microsoft.com/en-us/training/modules/chain-azure-functions-data-using-bindings/)

These articles show how to trigger from an Azure Service Bus queue or topic.

*   [Azure Service Bus trigger for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus-trigger?pivots=programming-language-csharp)

*   [Azure Service Bus trigger for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus-trigger?pivots=programming-language-javascript)

*   [Azure Service Bus trigger for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus-trigger?pivots=programming-language-typescript)

*   [Azure Service Bus trigger for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus-trigger?pivots=programming-language-python)

*   [Azure Service Bus trigger for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus-trigger?pivots=programming-language-java)

*   [Azure Service Bus trigger for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus-trigger?pivots=programming-language-powershell)
