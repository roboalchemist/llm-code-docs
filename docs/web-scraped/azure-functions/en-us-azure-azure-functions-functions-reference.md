# Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference

Title: Guidance for developing Azure Functions

URL Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference

Markdown Content:
In Azure Functions, all functions share some core technical concepts and components, regardless of your preferred language or development environment. This article is language-specific. Choose your preferred language at the top of the article.

This article assumes that you've already read the [Azure Functions overview](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview).

At the core of Azure Functions is a language-specific code project that implements one or more units of code execution called _functions_. Functions are simply methods that run in the Azure cloud based on events, in response to HTTP requests, or on a schedule. Think of your Azure Functions code project as a mechanism for organizing, deploying, and collectively managing your individual functions in the project when they're running in Azure. For more information, see [Organize your functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-best-practices#organize-your-functions).

The way that you lay out your code project and how you indicate which methods in your project are functions depends on the development language of your project. For detailed language-specific guidance, see the [C# developers guide](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide).

The way that you lay out your code project and how you indicate which methods in your project are functions depends on the development language of your project. For language-specific guidance, see the [Java developers guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-java).

The way that you lay out your code project and how you indicate which methods in your project are functions depends on the development language of your project. For language-specific guidance, see the [Node.js developers guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node).

The way that you lay out your code project and how you indicate which methods in your project are functions depends on the development language of your project. For language-specific guidance, see the [PowerShell developers guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-powershell).

The way that you lay out your code project and how you indicate which methods in your project are functions depends on the development language of your project. For language-specific guidance, see the [Python developers guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python).

All functions must have a trigger, which defines how the function starts and can provide input to the function. Your functions can optionally define input and output bindings. These bindings simplify connections to other services without you having to work with client SDKs. For more information, see [Azure Functions triggers and bindings concepts](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings).

Azure Functions provides a set of language-specific project and function templates that make it easy to create new code projects and add functions to your project. You can use any of the tools that support Azure Functions development to generate new apps and functions using these templates.

The following tools provide an integrated development and publishing experience for Azure Functions in your preferred language:

*   [Visual Studio](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs)

*   [Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code)

*   [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local) (command prompt)

*   [Eclipse](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-maven-eclipse)

*   [Gradle](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-first-java-gradle)

*   [IntelliJ IDEA](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-maven-intellij)

*   [Quarkus](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-first-quarkus)

*   [Spring Cloud](https://learn.microsoft.com/en-us/azure/developer/java/spring-framework/getting-started-with-spring-cloud-function-in-azure?toc=/azure/azure-functions/toc.json)

These tools integrate with [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local) so that you can run and debug on your local computer using the Functions runtime. For more information, see [Code and test Azure Functions locally](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local).

[](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference) There's also an editor in the Azure portal that lets you update your code and your _function.json_ definition file directly in the portal. You should only use this editor for small changes or creating proof-of-concept functions. You should always develop your functions locally, when possible. For more information, see [Create your first function in the Azure portal](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-function-app-portal).

Portal editing is only supported for [Node.js version 3](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?pivots=nodejs-model-v3), which uses the function.json file.

When you publish your code project to Azure, you're essentially deploying your project to an existing function app resource. A function app provides an execution context in Azure in which your functions run. As such, it's the unit of deployment and management for your functions. From an Azure Resource perspective, a function app is equivalent to a site resource (`Microsoft.Web/sites`) in Azure App Service, which is equivalent to a web app.

A function app is composed of one or more individual functions that are managed, deployed, and scaled together. All of the functions in a function app share the same [pricing plan](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale), [deployment method](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies), and [runtime version](https://learn.microsoft.com/en-us/azure/azure-functions/functions-versions). For more information, see [How to manage a function app](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings).

When the function app and any other required resources don't already exist in Azure, you first need to create these resources before you can deploy your project files. You can create these resources in one of these ways:

*   During [Visual Studio](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs#publish-to-azure) publishing

*   Using [Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code#publish-to-azure)

*   Programmatically using [Azure CLI](https://learn.microsoft.com/en-us/azure/azure-functions/functions-cli-samples#create), [Azure PowerShell](https://learn.microsoft.com/en-us/azure/azure-functions/create-resources-azure-powershell#create-a-serverless-function-app-for-c), [ARM templates](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-resource-manager), or [Bicep files](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-bicep)

*   In the [Azure portal](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-function-app-portal)

In addition to tool-based publishing, Functions supports other technologies for deploying source code to an existing function app. For more information, see [Deployment technologies in Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies).

A major requirement of any cloud-based compute service is reading data from and writing data to other cloud services. Functions provides an extensive set of bindings that makes it easier for you to connect to services without having to work with client SDKs.

Whether you use the binding extensions provided by Functions or you work with client SDKs directly, you securely store connection data and do not include it in your code. For more information, see [Connections](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#connections).

Functions provides bindings for many Azure services and a few third-party services, which are implemented as extensions. For more information, see the [complete list of supported bindings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings#supported-bindings).

Binding extensions can support both inputs and outputs, and many triggers also act as input bindings. Bindings let you configure the connection to services so that the Functions host can handle the data access for you. For more information, see [Azure Functions triggers and bindings concepts](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings).

If you're having issues with errors coming from bindings, see the [Azure Functions Binding Error Codes](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-error-pages) documentation.

While Functions provides bindings to simplify data access in your function code, you're still able to use a client SDK in your project to directly access a given service, if you prefer. You might need to use client SDKs directly should your functions require a functionality of the underlying SDK that's not supported by the binding extension.

When using client SDKs, you should use the same process for [storing and accessing connection strings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#connections) used by binding extensions.

When you create a client SDK instance in your functions, you should get the connection info required by the client from [Environment variables](https://learn.microsoft.com/en-us/azure/azure-functions/functions-dotnet-class-library#environment-variables).

When you create a client SDK instance in your functions, you should get the connection info required by the client from [Environment variables](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-java#environment-variables).

When you create a client SDK instance in your functions, you should get the connection info required by the client from [Environment variables](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node#environment-variables).

When you create a client SDK instance in your functions, you should get the connection info required by the client from [Environment variables](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-powershell#environment-variables).

When you create a client SDK instance in your functions, you should get the connection info required by the client from [Environment variables](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python#environment-variables).

As a security best practice, Azure Functions takes advantage of the application settings functionality of Azure App Service to help you more securely store strings, keys, and other tokens required to connect to other services. Application settings in Azure are stored encrypted and can be accessed at runtime by your app as environment variable `name``value` pairs. For triggers and bindings that require a connection property, you set the application setting name instead of the actual connection string. You can't configure a binding directly with a connection string or key.

For example, consider a trigger definition that has a `connection` property. Instead of the connection string, you set `connection` to the name of an environment variable that contains the connection string. Using this secrets access strategy both makes your apps more secure and makes it easier for you to change connections across environments. For even more security, you can use identity-based connections.

The default configuration provider uses environment variables. These variables are defined in [application settings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings?tabs=portal#settings) when running in the Azure and in the [local settings file](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local#local-settings-file) when developing locally.

When the connection name resolves to a single exact value, the runtime identifies the value as a _connection string_, which typically includes a secret. The details of a connection string depend on the service to which you connect.

However, a connection name can also refer to a collection of multiple configuration items, useful for configuring [identity-based connections](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#configure-an-identity-based-connection). Environment variables can be treated as a collection by using a shared prefix that ends in double underscores `__`. The group can then be referenced by setting the connection name to this prefix.

For example, the `connection` property for an Azure Blob trigger definition might be `Storage1`. As long as there's no single string value configured by an environment variable named `Storage1`, an environment variable named `Storage1__blobServiceUri` could be used to inform the `blobServiceUri` property of the connection. The connection properties are different for each service. Refer to the documentation for the component that uses the connection.

Note

When using [Azure App Configuration](https://learn.microsoft.com/en-us/azure/azure-app-configuration/quickstart-azure-functions-csharp) or [Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview) to provide settings for Managed Identity connections, setting names should use a valid key separator such as `:` or `/` in place of the `__` to ensure names are resolved correctly.

For example, `Storage1:blobServiceUri`.

Some connections in Azure Functions can be configured to use an identity instead of a secret. Support depends on the runtime version and the extension using the connection. In some cases, a connection string may still be required in Functions even though the service to which you're connecting supports identity-based connections. For a tutorial on configuring your function apps with managed identities, see the [creating a function app with identity-based connections tutorial](https://learn.microsoft.com/en-us/azure/azure-functions/functions-identity-based-connections-tutorial).

Identity-based connections are only supported on Functions 4.x, If you are using version 1.x, you must first [migrate to version 4.x](https://learn.microsoft.com/en-us/azure/azure-functions/migrate-version-1-version-4).

The following components support identity-based connections:

| Connection source | Plans supported | Learn more |
| --- | --- | --- |
| Azure Blobs triggers and bindings | All | [Azure Blobs extension version 5.0.0 or later](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob#install-extension), [Extension bundle 3.3.0 or later](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob#install-extension) |
| Azure Queues triggers and bindings | All | [Azure Queues extension version 5.0.0 or later](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue#storage-extension-5x-and-higher), [Extension bundle 3.3.0 or later](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue#storage-extension-5x-and-higher) |
| Azure Tables (when using Azure Storage) | All | [Azure Tables extension version 1.0.0 or later](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-table#table-api-extension), [Extension bundle 3.3.0 or later](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-table#table-api-extension) |
| Azure SQL Database | All | [Connect a function app to Azure SQL with managed identity and SQL bindings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-identity-access-azure-sql-with-managed-identity) |
| Azure Event Hubs triggers and bindings | All | [Azure Event Hubs extension version 5.0.0 or later](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs?tabs=extensionv5), [Extension bundle 3.3.0 or later](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs?tabs=extensionv5) |
| Azure Service Bus triggers and bindings | All | [Azure Service Bus extension version 5.0.0 or later](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus), [Extension bundle 3.3.0 or later](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus) |
| Azure Event Grid output binding | All | [Azure Event Grid extension version 3.3.0 or later](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-grid?tabs=extensionv3), [Extension bundle 3.3.0 or later](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-grid?tabs=extensionv3) |
| Azure Cosmos DB triggers and bindings | All | [Azure Cosmos DB extension version 4.0.0 or later](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2?tabs=extensionv4), [Extension bundle 4.0.2 or later](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2?tabs=extensionv4) |
| Azure SignalR triggers and bindings | All | [Azure SignalR extension version 1.7.0 or later](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-signalr-service#install-extension) [Extension bundle 3.6.1 or later](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-signalr-service#install-extension) |
| Azure Web PubSub triggers and bindings | All | [Azure Web PubSub extension version 1.10.0 or later](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-web-pubsub#install-extension) [Extension bundle 3.6.1 or later](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-web-pubsub#install-extension) |
| Durable Functions storage provider (Azure Storage) | All | [Durable Functions extension version 2.7.0 or later](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-configure-managed-identity), [Extension bundle 3.3.0 or later](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-configure-managed-identity) |
| Host-required storage ("AzureWebJobsStorage") | All | [Connecting to host storage with an identity](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#connecting-to-host-storage-with-an-identity) |

When hosted in the Azure Functions service, identity-based connections use a [managed identity](https://learn.microsoft.com/en-us/azure/app-service/overview-managed-identity?toc=/azure/azure-functions/toc.json). The system-assigned identity is used by default, although a user-assigned identity can be specified with the `credential` and `clientID` properties. Note that configuring a user-assigned identity with a resource ID is **not** supported. When run in other contexts, such as local development, your developer identity is used instead, although this can be customized. See [Local development with identity-based connections](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#local-development-with-identity-based-connections).

Whatever identity is being used must have permissions to perform the intended actions. For most Azure services, this means you need to [assign a role in Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-steps), using either built-in or custom roles which provide those permissions.

Important

Some permissions might be exposed by the target service that are not necessary for all contexts. Where possible, adhere to the **principle of least privilege**, granting the identity only required privileges. For example, if the app only needs to be able to read from a data source, use a role that only has permission to read. It would be inappropriate to assign a role that also allows writing to that service, as this would be excessive permission for a read operation. Similarly, you would want to ensure the role assignment is scoped only over the resources that need to be read.

Choose one of these tabs to learn about permissions for each component:

*   [Azure Blobs extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#tabpanel_1_blob)
*   [Azure Queues extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#tabpanel_1_queue)
*   [Azure Tables extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#tabpanel_1_table)
*   [Event Hubs extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#tabpanel_1_eventhubs)
*   [Service Bus extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#tabpanel_1_servicebus)
*   [Event Grid extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#tabpanel_1_eventgrid)
*   [Azure Cosmos DB extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#tabpanel_1_cosmos)
*   [Azure SignalR extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#tabpanel_1_signalr)
*   [Azure Web PubSub extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#tabpanel_1_web-pubsub)
*   [Durable Functions storage provider](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#tabpanel_1_durable)
*   [Functions host storage](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#tabpanel_1_azurewebjobsstorage)

You need to create a role assignment that provides access to your blob container at runtime. Management roles like [Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) aren't sufficient. The following table shows built-in roles that are recommended when using the Blob Storage extension in normal operation. Your application may require further permissions based on the code you write.

| Binding type | Example built-in roles |
| --- | --- |
| Trigger | [Storage Blob Data Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-owner)**and**[Storage Queue Data Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-queue-data-contributor)1 Extra permissions must also be granted to the AzureWebJobsStorage connection.2 |
| Input binding | [Storage Blob Data Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-reader) |
| Output binding | [Storage Blob Data Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-owner) |

1 The blob trigger handles failure across multiple retries by writing [poison blobs](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger#poison-blobs) to a queue on the storage account specified by the connection.

2 The AzureWebJobsStorage connection is used internally for blobs and queues that enable the trigger. If it's configured to use an identity-based connection, it needs extra permissions beyond the default requirement. The required permissions are covered by the [Storage Blob Data Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-owner), [Storage Queue Data Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-queue-data-contributor), and [Storage Account Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-account-contributor) roles. To learn more, see [Connecting to host storage with an identity](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#connecting-to-host-storage-with-an-identity).

An identity-based connection for an Azure service accepts the following common properties, where `<CONNECTION_NAME_PREFIX>` is the value of your `connection` property in the trigger or binding definition:

| Property | Environment variable template | Description |
| --- | --- | --- |
| Token Credential | `<CONNECTION_NAME_PREFIX>__credential` | This property determines how a token should be obtained for the connection. The property shouldn't be set in [local development scenarios](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#local-development-with-identity-based-connections). When you intend to use managed identity authentication, set this property to `managedidentity`. When you intend to [connect to a resource in another tenant](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#connecting-to-a-resource-in-another-tenant), instead use `managedidentityasfederatedidentity`. |
| Client ID | `<CONNECTION_NAME_PREFIX>__clientId` | When `credential` is set to `managedidentity`, this property can be set to specify the user-assigned identity to be used when obtaining a token. The property accepts a client ID corresponding to a user-assigned identity assigned to the application. It's invalid to specify both a resource ID and a client ID. If neither are specified, the system-assigned identity is used. This property is used differently in cross-tenant scenarios. See the [cross-tenant scenarios](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#connecting-to-a-resource-in-another-tenant) section. This property is used differently in [local development scenarios](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#local-development-with-identity-based-connections), when `credential` shouldn't be set. |
| Resource ID | `<CONNECTION_NAME_PREFIX>__managedIdentityResourceId` | When `credential` is set to `managedidentity`, this property can be set to specify the user-assigned identity to be used when obtaining a token. The property accepts a resource identifier corresponding to a user-assigned identity assigned to the application. It's invalid to specify both a resource ID and a client ID. If neither are specified, the system-assigned identity is used. |

Other options may be supported for a given connection type. Refer to the documentation for the component making the connection.

Caution

Use of the Azure SDK's [`EnvironmentCredential`](https://learn.microsoft.com/en-us/dotnet/api/azure.identity.environmentcredential) environment variables is not recommended due to the potentially unintentional impact on other connections. They also are not fully supported when deployed to Azure Functions.

The environment variables associated with the Azure SDK's [`EnvironmentCredential`](https://learn.microsoft.com/en-us/dotnet/api/azure.identity.environmentcredential) can also be set, but these are not processed by the Functions service for scaling in Consumption plans. These environment variables are not specific to any one connection and will apply as a default unless a corresponding property is not set for a given connection. For example, if `AZURE_CLIENT_ID` is set, this would be used as if `<CONNECTION_NAME_PREFIX>__clientId` had been configured. Explicitly setting `<CONNECTION_NAME_PREFIX>__clientId` would override this default.

Note

Local development with identity-based connections requires version `4.0.3904` of [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local), or a later version.

When you're running your function project locally, the above configuration tells the runtime to use your local developer identity. The connection attempts to get a token from the following locations, in order:

*   A local cache shared between Microsoft applications
*   The current user context in Visual Studio
*   The current user context in Visual Studio Code
*   The current user context in the Azure CLI

If none of these options are successful, an error occurs.

Your identity may already have some role assignments against Azure resources used for development, but those roles may not provide the necessary data access. Management roles like [Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) aren't sufficient. Double-check what permissions are required for connections for each component, and make sure that you have them assigned to yourself.

In some cases, you may wish to specify use of a different identity. You can add configuration properties for the connection that point to the alternate identity based on a client ID and client Secret for a Microsoft Entra service principal. **This configuration option is not supported when hosted in the Azure Functions service.** To use an ID and secret on your local machine, define the connection with the following extra properties:

| Property | Environment variable template | Description |
| --- | --- | --- |
| Tenant ID | `<CONNECTION_NAME_PREFIX>__tenantId` | The Microsoft Entra tenant (directory) ID. |
| Client ID | `<CONNECTION_NAME_PREFIX>__clientId` | The client (application) ID of an app registration in the tenant. |
| Client secret | `<CONNECTION_NAME_PREFIX>__clientSecret` | A client secret that was generated for the app registration. |

Here's an example of `local.settings.json` properties required for identity-based connection to Azure Blobs:

```
{
  "IsEncrypted": false,
  "Values": {
    "<CONNECTION_NAME_PREFIX>__blobServiceUri": "<blobServiceUri>",
    "<CONNECTION_NAME_PREFIX>__queueServiceUri": "<queueServiceUri>",
    "<CONNECTION_NAME_PREFIX>__tenantId": "<tenantId>",
    "<CONNECTION_NAME_PREFIX>__clientId": "<clientId>",
    "<CONNECTION_NAME_PREFIX>__clientSecret": "<clientSecret>"
  }
}
```

The Azure Functions host uses the storage connection set in [`AzureWebJobsStorage`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#azurewebjobsstorage) to enable core behaviors such as coordinating singleton execution of timer triggers and default app key storage. This connection can also be configured to use an identity.

Caution

Other components in Functions rely on `AzureWebJobsStorage` for default behaviors. You should not move it to an identity-based connection if you are using older versions of extensions that do not support this type of connection, including triggers and bindings for Azure Blobs, Event Hubs, and Durable Functions. Similarly, `AzureWebJobsStorage` is used for deployment artifacts when using server-side build in Linux Consumption, and if you enable this, you will need to deploy via [an external deployment package](https://learn.microsoft.com/en-us/azure/azure-functions/run-functions-from-deployment-package).

In addition, your function app might be reusing `AzureWebJobsStorage` for other storage connections in their triggers, bindings, and/or function code. Make sure that all uses of `AzureWebJobsStorage` are able to use the identity-based connection format before changing this connection from a connection string.

To use an identity-based connection for `AzureWebJobsStorage`, configure the following app settings:

| Setting | Description | Example value |
| --- | --- | --- |
| `AzureWebJobsStorage__blobServiceUri` | The data plane URI of the blob service of the storage account, using the HTTPS scheme. | https://<storage_account_name>.blob.core.windows.net |
| `AzureWebJobsStorage__queueServiceUri` | The data plane URI of the queue service of the storage account, using the HTTPS scheme. | https://<storage_account_name>.queue.core.windows.net |
| `AzureWebJobsStorage__tableServiceUri` | The data plane URI of a table service of the storage account, using the HTTPS scheme. | https://<storage_account_name>.table.core.windows.net |

[Common properties for identity-based connections](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#common-properties-for-identity-based-connections) may also be set as well.

If you're configuring `AzureWebJobsStorage` using a storage account that uses the default DNS suffix and service name for global Azure, following the `https://<accountName>.[blob|queue|file|table].core.windows.net` format, you can instead set `AzureWebJobsStorage__accountName` to the name of your storage account. The endpoints for each storage service are inferred for this account. This doesn't work when the storage account is in a sovereign cloud or has a custom DNS.

| Setting | Description | Example value |
| --- | --- | --- |
| `AzureWebJobsStorage__accountName` | The account name of a storage account, valid only if the account isn't in a sovereign cloud and doesn't have a custom DNS. This syntax is unique to `AzureWebJobsStorage` and can't be used for other identity-based connections. | <storage_account_name> |

You need to create a role assignment that provides access to the storage account for "AzureWebJobsStorage" at runtime. Management roles like [Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) aren't sufficient. The [Storage Blob Data Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-owner) role covers the basic needs of Functions host storage - the runtime needs both read and write access to blobs and the ability to create containers. Several extensions use this connection as a default location for blobs, queues, and tables, and these uses may add requirements as noted in the table below. You may also need other permissions if you use "AzureWebJobsStorage" for any other purposes.

| Extension | Roles required | Explanation |
| --- | --- | --- |
| _No extension (host only)_ | [Storage Blob Data Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-owner) | Functions uses blob storage for general coordination and as a default key store. This scenario represents the minimum set of permissions for normal operation, but it doesn't include support for diagnostic events 1. |
| _No extension (host only), with support for diagnostic events 1_ | [Storage Blob Data Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-owner), [Storage Table Data Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-table-data-contributor) | Diagnostic events are persisted in table storage using the AzureWebJobsStorage connection. |
| Azure Blobs (trigger only) | All of: [Storage Account Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-account-contributor), [Storage Blob Data Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-owner), [Storage Queue Data Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-queue-data-contributor) | The blob trigger internally uses Azure Queues and writes [blob receipts](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger#blob-receipts). It uses the AzureWebJobsStorage connection for these purposes, regardless of the connection configured for the trigger. |
| Azure Event Hubs (trigger only) | (no change from default requirement) [Storage Blob Data Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-owner) | Checkpoints are persisted in blobs using the AzureWebJobsStorage connection. |
| Timer trigger | (no change from default requirement) [Storage Blob Data Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-owner) | To ensure one execution per event, locks are taken with blobs using the AzureWebJobsStorage connection. |
| Durable Functions | All of: [Storage Blob Data Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor), [Storage Queue Data Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-queue-data-contributor), [Storage Table Data Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-table-data-contributor) | Durable Functions uses blobs, queues, and tables to coordinate activity functions and maintain orchestration state. It uses the AzureWebJobsStorage connection by default, but you can specify a different connection in the [Durable Functions extension configuration](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-bindings#host-json). |

1 For some types of issues, Azure Functions can raise a diagnostic event that can assist with troubleshooting, even when the issue prevents the function app from starting. If [Storage Table Data Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-table-data-contributor) isn't assigned, you might see warnings in your logs about the inability to write these events.

If your function needs to connect to a resource in a different Microsoft Entra tenant, your connection needs to use a _federated identity credential_. This requires a user-assigned managed identity and a multitenant Entra ID app registration. You cannot use a system-assigned managed identity for cross-tenant connections.

Important

When you configure a trigger for a cross-tenant connection in the Consumption or Flex Consumption plan types, the platform no longer scales the function app based on that trigger.

To configure a cross-tenant identity-based connection, you first need to set up your infrastructure using the following steps:

1.   In the tenant where your function app is deployed, [create a new user-assigned managed identity](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-manage-user-assigned-managed-identities#create-a-user-assigned-managed-identity).
2.   [Assign that identity](https://learn.microsoft.com/en-us/azure/app-service/overview-managed-identity?toc=/azure/azure-functions/toc.json#add-a-user-assigned-identity) to the function app.
3.   In the same tenant, [create a multitenant Entra app registration](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-config-app-trust-managed-identity#configure-a-multi-tenant-app-registration) that represents the cross-tenant resource you want to access.
4.   [Add the managed identity as a federated identity credential for the app registration.](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-config-app-trust-managed-identity)
5.   In the tenant where the resource is deployed, [create an enterprise application for the app registration](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/create-service-principal-cross-tenant).
6.   Assign permissions for the enterprise application to access the resource.

A cross-tenant identity-based connection uses the following properties, where `<CONNECTION_NAME_PREFIX>` is the value of your `connection` property in the trigger or binding definition:

| Property | Environment variable template | Description |
| --- | --- | --- |
| Token Credential | `<CONNECTION_NAME_PREFIX>__credential` | **Required.** When connecting to a resource in another tenant, set this property to `managedidentityasfederatedidentity`. |
| Azure Cloud | `<CONNECTION_NAME_PREFIX>__azureCloud` | **Required.** This property determines the Azure cloud environment. Allowed values are "public" for Azure Public Cloud, "usgov" for Azure US Government Cloud, and "china" for Azure operated by 21Vianet. |
| Client ID | `<CONNECTION_NAME_PREFIX>__clientId` | **Required.** When `credential` is set to `managedidentityasfederatedidentity`, set this property to the client ID (app ID) of the app registration. This property is used differently in single-tenant identity-based connections. See the [common properties](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#common-properties-for-identity-based-connections) section. This property is used differently in [local development scenarios](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#local-development-with-identity-based-connections), when `credential` shouldn't be set. |
| Tenant ID | `<CONNECTION_NAME_PREFIX>__tenantId` | **Required.** When `credential` is set to `managedidentityasfederatedidentity`, set this property to the tenant ID of the resource tenant. This property is used differently in [local development scenarios](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference#local-development-with-identity-based-connections), when `credential` shouldn't be set. |
| Managed Identity Client ID | `<CONNECTION_NAME_PREFIX>__managedIdentityClientId` | When `credential` is set to `managedidentityasfederatedidentity`, this property specifies the user-assigned identity that you configured as a federated identity credential and assigned to the application.1 The property accepts a client ID corresponding to that user-assigned identity. |
| Managed Identity Object ID | `<CONNECTION_NAME_PREFIX>__managedIdentityObjectId` | When `credential` is set to `managedidentityasfederatedidentity`, this property specifies the user-assigned identity that you configured as a federated identity credential and assigned to the application.1 The property accepts an object ID (principal ID) corresponding to that user-assigned identity. |
| Managed Identity Resource ID | `<CONNECTION_NAME_PREFIX>__managedIdentityResourceId` | When `credential` is set to `managedidentityasfederatedidentity`, this property specifies the user-assigned identity that you configured as a federated identity credential and assigned to the application.1 The property accepts a resource identifier corresponding to that user-assigned identity. |

1 When `credential` is set to `managedidentityasfederatedidentity`, your connection must specify exactly one of `managedIdentityClientId`, `managedIdentityObjectId`, or `managedIdentityResourceId`.

This is also [documented by the Azure SDK](https://learn.microsoft.com/en-us/dotnet/azure/sdk/authentication/create-token-credentials-from-configuration?tabs=client-id#managed-identity-as-a-federated-identity-credential) in a JSON format.

| Item | Description | Link |
| --- | --- | --- |
| Runtime | Script Host, Triggers & Bindings, Language Support | [File an Issue](https://github.com/Azure/azure-webjobs-sdk-script/issues) |
| Templates | Code Issues with Creation Template | [File an Issue](https://github.com/Azure/azure-webjobs-sdk-templates/issues) |

The code for Azure Functions is open source, and you can find key components in these GitHub repositories:

*   [Azure Functions](https://github.com/Azure/Azure-Functions)

*   [Azure Functions host](https://github.com/Azure/azure-functions-host/)

*   [Azure Functions templates](https://github.com/azure/azure-functions-templates)

*   [Azure WebJobs SDK](https://github.com/Azure/azure-webjobs-sdk/)

*   [Azure WebJobs SDK Extensions](https://github.com/Azure/azure-webjobs-sdk-extensions/)

*   [Azure Functions .NET worker (isolated process)](https://github.com/Azure/azure-functions-dotnet-worker)

*   [Azure Functions Java worker](https://github.com/Azure/azure-functions-java-worker)

*   [Azure Functions Node.js Programming Model](https://github.com/Azure/azure-functions-nodejs-library)

*   [Azure Functions PowerShell worker](https://github.com/Azure/azure-functions-powershell-worker)

*   [Azure Functions Python worker](https://github.com/Azure/azure-functions-python-worker)

For more information, see the following resources:

*   [Azure Functions scenarios](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios)
*   [Code and test Azure Functions locally](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local)
*   [Best Practices for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-best-practices)
