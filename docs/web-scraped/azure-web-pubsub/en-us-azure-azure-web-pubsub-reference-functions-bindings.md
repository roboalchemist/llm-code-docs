# Source: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings

Title: Reference - Azure Web PubSub trigger and bindings for Azure Functions

URL Source: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings

Markdown Content:
This reference explains how to handle Web PubSub events in Azure Functions.

Web PubSub is an Azure-managed service that helps developers easily build web applications with real-time features and publish-subscribe pattern.

| Action | Type |
| --- | --- |
| Run a function when messages come from service | [Trigger binding](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#trigger-binding) |
| Bind request to target object under HTTP trigger for negotiation and upstream requests | [Input binding](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#input-binding) |
| Invoke service do actions | [Output binding](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#output-binding) |

[Source code](https://github.com/Azure/azure-sdk-for-net/blob/master/sdk/webpubsub/) | [Package](https://www.nuget.org/packages/Microsoft.Azure.WebJobs.Extensions.WebPubSub) | [API reference documentation](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/webpubsub/Microsoft.Azure.WebJobs.Extensions.WebPubSub/api/Microsoft.Azure.WebJobs.Extensions.WebPubSub.netstandard2.0.cs) | [Product documentation](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/) | [Samples](https://github.com/Azure/azure-webpubsub/tree/main/samples/functions)

Working with the trigger and bindings requires you reference the appropriate package. The NuGet package is used for .NET class libraries while an extension bundle is used for all other application types.

| Language | Add by... |
| --- | --- |
| C# | Install the [NuGet package](https://www.nuget.org/packages/Microsoft.Azure.WebJobs.Extensions.WebPubSub), target specific version |
| JavaScript, Python, PowerShell, C# script (Azure portal-only) | [Use extension bundles](https://learn.microsoft.com/en-us/azure/azure-functions/extension-bundles) (recommended), [explicitly install extensions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-register#explicitly-install-extensions) |

![Image 1: Diagram showing the workflow of Azure Web PubSub service working with Function Apps.](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/media/reference-functions-bindings/functions-workflow.png)

(1)-(2) `WebPubSubConnection` input binding with HttpTrigger to generate client connection.

(3)-(4) `WebPubSubTrigger` trigger binding or `WebPubSubContext` input binding with HttpTrigger to handle service request.

(5)-(6) `WebPubSub` output binding to request service do something.

Use the function trigger to handle requests from Azure Web PubSub service.

`WebPubSubTrigger` is used when you need to handle requests from service side. The trigger endpoint pattern would be like below which should be set in Web PubSub service side (Portal: settings -> event handler -> URL Template). In the endpoint pattern, the query part `code=<API_KEY>` is **REQUIRED** when you're using Azure Function App for [security](https://learn.microsoft.com/en-us/azure/azure-functions/function-keys-how-to#understand-keys) reasons. The key can be found in **Azure portal**. Find your function app resource and navigate to **Functions** ->**App keys** ->**System keys** ->**webpubsub_extension** after you deploy the function app to Azure. Though, this key isn't needed when you're working with local functions.

```
<Function_App_Url>/runtime/webhooks/webpubsub?code=<API_KEY>
```

![Image 2: Screenshot of get function system keys.](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/media/quickstart-serverless/func-keys.png)

*   [C#](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#tabpanel_1_csharp)
*   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#tabpanel_1_javascript-v4)
*   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#tabpanel_1_javascript-v3)

```
[FunctionName("WebPubSubTrigger")]
public static void Run(
    [WebPubSubTrigger("<hub>", WebPubSubEventType.User, "message")] UserEventRequest request, ILogger log)
{
    log.LogInformation($"Request from: {request.ConnectionContext.UserId}");
    log.LogInformation($"Request message data: {request.Data}");
    log.LogInformation($"Request message dataType: {request.DataType}");
}
```

`WebPubSubTrigger` binding also supports return value in synchronize scenarios, for example, system `Connect` and user event, when server can check and deny the client request, or send messages to the caller directly. `Connect` event respects `ConnectEventResponse` and `EventErrorResponse`, and user event respects `UserEventResponse` and `EventErrorResponse`, rest types not matching current scenario is ignored. And if `EventErrorResponse` is returned, service drops the client connection.

```
[FunctionName("WebPubSubTriggerReturnValueFunction")]
public static UserEventResponse Run(
    [WebPubSubTrigger("hub", WebPubSubEventType.User, "message")] UserEventRequest request)
{
    return request.CreateResponse(BinaryData.FromString("ack"), WebPubSubDataType.Text);
}
```

In [C# class libraries](https://learn.microsoft.com/en-us/azure/azure-functions/functions-dotnet-class-library), use the `WebPubSubTrigger` attribute.

Here's an `WebPubSubTrigger` attribute in a method signature:

```
[FunctionName("WebPubSubTrigger")]
public static void Run([WebPubSubTrigger("<hub>", <WebPubSubEventType>, "<event-name>")] 
    WebPubSubConnectionContext context, ILogger log)
{
    ...
}
```

For a complete example, see C# example.

The following table explains the binding configuration properties that you set in the _function.json_ file.

| function.json property | Attribute property | Description |
| --- | --- | --- |
| **type** | n/a | Required - must be set to `webPubSubTrigger`. |
| **direction** | n/a | Required - must be set to `in`. |
| **name** | n/a | Required - the variable name used in function code for the parameter that receives the event data. |
| **hub** | Hub | Required - the value must be set to the name of the Web PubSub hub for the function to be triggered. We support set the value in attribute as higher priority, or it can be set in app settings as a global value. |
| **eventType** | WebPubSubEventType | Required - the value must be set as the event type of messages for the function to be triggered. The value should be either `user` or `system`. |
| **eventName** | EventName | Required - the value must be set as the event of messages for the function to be triggered. For `system` event type, the event name should be in `connect`, `connected`, `disconnected`. For user-defined subprotocols, the event name is `message`. For system supported subprotocol `json.webpubsub.azure.v1.`, the event name is user-defined event name. |
| **connection** | Connection | Optional - the name of an app settings or setting collection that specifies the upstream Azure Web PubSub service. The value is used for signature validation. And the value is auto resolved with app settings "WebPubSubConnectionString" by default. And `null` means the validation isn't needed and always succeed. |

In C#, `WebPubSubEventRequest` is type recognized binding parameter, rest parameters are bound by parameter name. Check table below of available parameters and types.

In weakly typed language like JavaScript, `name` in `function.json` is used to bind the trigger object regarding below mapping table. And respect `dataType` in `function.json` to convert message accordingly when `name` is set to `data` as the binding object for trigger input. All the parameters can be read from `context.bindingData.<BindingName>` and is `JObject` converted.

| Binding Name | Binding Type | Description | Properties |
| --- | --- | --- | --- |
| request | `WebPubSubEventRequest` | Describes the upstream request | Property differs by different event types, including derived classes `ConnectEventRequest`, `ConnectedEventRequest`, `UserEventRequest` and `DisconnectedEventRequest` |
| connectionContext | `WebPubSubConnectionContext` | Common request information | EventType, EventName, Hub, ConnectionId, UserId, Headers, Origin, Signature, States |
| data | `BinaryData`,`string`,`Stream`,`byte[]` | Request message data from client in user `message` event | - |
| dataType | `WebPubSubDataType` | Request message dataType, which supports `binary`, `text`, `json` | - |
| claims | `IDictionary<string, string[]>` | User Claims in system `connect` request | - |
| query | `IDictionary<string, string[]>` | User query in system `connect` request | - |
| subprotocols | `IList<string>` | Available subprotocols in system `connect` request | - |
| clientCertificates | `IList<ClientCertificate>` | A list of certificate thumbprint from clients in system `connect` request | - |
| reason | `string` | Reason in system `disconnected` request | - |

Important

In C#, multiple types supported parameter **MUST** be put in the first, i.e. `request` or `data` that other than the default `BinaryData` type to make the function binding correctly.

`WebPubSubTrigger` respects customer returned response for synchronous events of `connect` and user event. Only matched response is sent back to service, otherwise, it's ignored. Besides, `WebPubSubTrigger` return object supports users to `SetState()` and `ClearStates()` to manage the metadata for the connection. And the extension merges the results from return value with the original ones from request `WebPubSubConnectionContext.States`. Value in existing key is overwrite and value in new key is added.

| Return Type | Description | Properties |
| --- | --- | --- |
| `ConnectEventResponse` | Response for `connect` event | Groups, Roles, UserId, Subprotocol |
| `UserEventResponse` | Response for user event | DataType, Data |
| `EventErrorResponse` | Error response for the sync event | Code, ErrorMessage |
| `*WebPubSubEventResponse` | Base response type of the supported ones used for uncertain return cases | - |

Our extension provides two input binding targeting different needs.

*   `WebPubSubConnection`

To let a client connect to Azure Web PubSub Service, it must know the service endpoint URL and a valid access token. The `WebPubSubConnection` input binding produces required information, so client doesn't need to handle this token generation itself. Because the token is time-limited and can be used to authenticate a specific user to a connection, don't cache the token or share it between clients. An HTTP trigger working with this input binding can be used for clients to retrieve the connection information.

*   `WebPubSubContext`

When using is Static Web Apps, `HttpTrigger` is the only supported trigger and under Web PubSub scenario, we provide the `WebPubSubContext` input binding helps users deserialize upstream http request from service side under Web PubSub protocols. So customers can get similar results comparing to `WebPubSubTrigger` to easily handle in functions. See [examples](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#example---webpubsubcontext) in below. When used with `HttpTrigger`, customer requires to configure the HttpTrigger exposed url in event handler accordingly.

The following example shows a C# function that acquires Web PubSub connection information using the input binding and returns it over HTTP. In below example, the `UserId` is passed in through client request query part like `?userid={User-A}`.

*   [C#](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#tabpanel_2_csharp)
*   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#tabpanel_2_javascript-v4)
*   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#tabpanel_2_javascript-v3)

```
[FunctionName("WebPubSubConnectionInputBinding")]
public static WebPubSubConnection Run(
    [HttpTrigger(AuthorizationLevel.Anonymous, "get", "post")] HttpRequest req,
    [WebPubSubConnection(Hub = "<hub>", UserId = "{query.userid}")] WebPubSubConnection connection)
{
    return connection;
}
```

If the function is triggered by an authenticated client, you can add a user ID claim to the generated token. You can easily add authentication to a function app using App Service Authentication.

App Service Authentication sets HTTP headers named `x-ms-client-principal-id` and `x-ms-client-principal-name` that contain the authenticated user's client principal ID and name, respectively.

You can set the UserId property of the binding to the value from either header using a binding expression: `{headers.x-ms-client-principal-id}` or `{headers.x-ms-client-principal-name}`.

```
[FunctionName("WebPubSubConnectionInputBinding")]
public static WebPubSubConnection Run(
    [HttpTrigger(AuthorizationLevel.Anonymous, "get", "post")] HttpRequest req,
    [WebPubSubConnection(Hub = "<hub>", UserId = "{headers.x-ms-client-principal-name}")] WebPubSubConnection connection)
{
    return connection;
}
```

*   [C#](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#tabpanel_3_csharp)
*   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#tabpanel_3_javascript-v4)
*   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#tabpanel_3_javascript-v3)

Note

Limited to the binding parameter types don't support a way to pass list nor array, the `WebPubSubConnection` isn't fully supported with all the parameters server SDK has, especially `roles`, and also includes `groups` and `expiresAfter`. In the case customer needs to add roles or delay build the access token in the function, it's suggested to work with [server SDK for C#](https://learn.microsoft.com/en-us/dotnet/api/overview/azure/messaging.webpubsub-readme).

```
[FunctionName("WebPubSubConnectionCustomRoles")]
public static async Task<Uri> Run(
    [HttpTrigger(AuthorizationLevel.Anonymous, "get", "post")] HttpRequest req)
{
    var serviceClient = new WebPubSubServiceClient(new Uri(endpoint), "<hub>", "<web-pubsub-connection-string>");
    var userId = req.Query["userid"].FirstOrDefault();
    // your method to get custom roles.
    var roles = GetRoles(userId);
    return await serviceClient.GetClientAccessUriAsync(TimeSpan.FromMinutes(5), userId, roles);
}
```

The following example shows a C# function that acquires Web PubSub upstream request information using the input binding under `connect` event type and returns it over HTTP.

*   [C#](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#tabpanel_4_csharp)
*   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#tabpanel_4_javascript-v4)
*   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#tabpanel_4_javascript-v3)

```
[FunctionName("WebPubSubContextInputBinding")]
public static object Run(
    [HttpTrigger(AuthorizationLevel.Anonymous, "get", "post")] HttpRequest req,
    [WebPubSubContext] WebPubSubContext wpsContext)
{
    // in the case request is a preflight or invalid, directly return prebuild response by extension.
    if (wpsContext.IsPreflight || wpsContext.HasError)
    {
        return wpsContext.Response;
    }
    var request = wpsContext.Request as ConnectEventRequest;
    var response = new ConnectEventResponse
    {
        UserId = wpsContext.Request.ConnectionContext.UserId
    };
    return response;
}
```

The following table explains the binding configuration properties that you set in the function.json file and the `WebPubSubConnection` attribute.

| function.json property | Attribute property | Description |
| --- | --- | --- |
| **type** | n/a | Must be set to `webPubSubConnection` |
| **direction** | n/a | Must be set to `in` |
| **name** | n/a | Variable name used in function code for input connection binding object. |
| **hub** | Hub | Required - The value must be set to the name of the Web PubSub hub for the function to be triggered. We support set the value in attribute as higher priority, or it can be set in app settings as a global value. |
| **userId** | UserId | Optional - the value of the user identifier claim to be set in the access key token. |
| **connection** | Connection | Required - The name of the app setting that contains the Web PubSub Service connection string (defaults to "WebPubSubConnectionString"). |

The following table explains the binding configuration properties that you set in the functions.json file and the `WebPubSubContext` attribute.

| function.json property | Attribute property | Description |
| --- | --- | --- |
| **type** | n/a | Must be set to `webPubSubContext`. |
| **direction** | n/a | Must be set to `in`. |
| **name** | n/a | Variable name used in function code for input Web PubSub request. |
| **connection** | Connection | Optional - the name of an app settings or setting collection that specifies the upstream Azure Web PubSub service. The value is used for [Abuse Protection](https://github.com/cloudevents/spec/blob/v1.0.1/http-webhook.md#4-abuse-protection) and Signature validation. The value is auto resolved with "WebPubSubConnectionString" by default. And `null` means the validation isn't needed and always succeed. |

*   [C#](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#tabpanel_5_csharp)
*   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#tabpanel_5_javascript-v4)
*   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#tabpanel_5_javascript-v3)

`WebPubSubConnection` provides below properties.

| Binding Name | Binding Type | Description |
| --- | --- | --- |
| BaseUri | Uri | Web PubSub client connection uri. |
| Uri | Uri | Absolute Uri of the Web PubSub connection, contains `AccessToken` generated base on the request. |
| AccessToken | string | Generated `AccessToken` based on request UserId and service information. |

`WebPubSubContext` provides below properties.

| Binding Name | Binding Type | Description | Properties |
| --- | --- | --- | --- |
| request | `WebPubSubEventRequest` | Request from client, see below table for details. | `WebPubSubConnectionContext` from request header and other properties deserialized from request body describe the request, for example, `Reason` for `DisconnectedEventRequest`. |
| response | `HttpResponseMessage` | Extension builds response mainly for `AbuseProtection` and errors cases. | - |
| errorMessage | string | Describe the error details when processing the upstream request. | - |
| hasError | bool | Flag to indicate whether it's a valid Web PubSub upstream request. | - |
| isPreflight | bool | Flag to indicate whether it's a preflight request of `AbuseProtection`. | - |

For `WebPubSubEventRequest`, it's deserialized to different classes that provide different information about the request scenario. For `PreflightRequest` or not valid cases, user can check the flags `IsPreflight` and `HasError` to know. It's suggested to return system build response `WebPubSubContext.Response` directly, or customer can log errors on demand. In different scenarios, customer can read the request properties as below.

| Derived Class | Description | Properties |
| --- | --- | --- |
| `PreflightRequest` | Used in `AbuseProtection` when `IsPreflight` is **true** | - |
| `ConnectEventRequest` | Used in system `Connect` event type | Claims, Query, Subprotocols, ClientCertificates |
| `ConnectedEventRequest` | Used in system `Connected` event type | - |
| `UserEventRequest` | Used in user event type | Data, DataType |
| `DisconnectedEventRequest` | Used in system `Disconnected` event type | Reason |

Note

Though the `WebPubSubContext` is an input binding that provides a similar request deserialize method under `HttpTrigger` comparing to `WebPubSubTrigger`, there's limitations; that is, connection state post merge isn't supported. The return response is still respected by the service side, but users require to build the response themselves. If users have needs to set the event response, you should return a `HttpResponseMessage` contains `ConnectEventResponse` or messages for user event as **response body** and put connection state with key `ce-connectionstate` in **response header**.

Use the Web PubSub output binding to invoke Azure Web PubSub service to do something. You can broadcast a message to:

*   All connected clients
*   Connected clients authenticated to a specific user
*   Connected clients joined in a specific group
*   A specific client connection

The output binding also allows you to manage clients and groups, as well as grant/revoke permissions targeting specific connectionId with group.

*   Add connection to group
*   Add user to group
*   Remove connection from a group
*   Remove user from a group
*   Remove user from all groups
*   Close all client connections
*   Close a specific client connection
*   Close connections in a group
*   Grant permission of a connection
*   Revoke permission of a connection

For information on setup and configuration details, see the overview.

*   [C#](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#tabpanel_6_csharp)
*   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#tabpanel_6_javascript-v4)
*   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#tabpanel_6_javascript-v3)

```
[FunctionName("WebPubSubOutputBinding")]
public static async Task RunAsync(
    [HttpTrigger(AuthorizationLevel.Anonymous, "get", "post")] HttpRequest req,
    [WebPubSub(Hub = "<hub>")] IAsyncCollector<WebPubSubAction> actions)
{
    await actions.AddAsync(WebPubSubAction.CreateSendToAllAction("Hello Web PubSub!", WebPubSubDataType.Text));
}
```

`WebPubSubAction` is the base abstract type of output bindings. The derived types represent the action server want service to invoke.

*   [C#](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#tabpanel_7_csharp)
*   [JavaScript Model v4](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#tabpanel_7_javascript-v4)
*   [JavaScript Model v3](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/reference-functions-bindings#tabpanel_7_javascript-v3)

In C# language, we provide a few static methods under `WebPubSubAction` to help discover available actions. For example, user can create the `SendToAllAction` by call `WebPubSubAction.CreateSendToAllAction()`.

| Derived Class | Properties |
| --- | --- |
| `SendToAllAction` | Data, DataType, Excluded |
| `SendToGroupAction` | Group, Data, DataType, Excluded |
| `SendToUserAction` | UserId, Data, DataType |
| `SendToConnectionAction` | ConnectionId, Data, DataType |
| `AddUserToGroupAction` | UserId, Group |
| `RemoveUserFromGroupAction` | UserId, Group |
| `RemoveUserFromAllGroupsAction` | UserId |
| `AddConnectionToGroupAction` | ConnectionId, Group |
| `RemoveConnectionFromGroupAction` | ConnectionId, Group |
| `CloseAllConnectionsAction` | Excluded, Reason |
| `CloseClientConnectionAction` | ConnectionId, Reason |
| `CloseGroupConnectionsAction` | Group, Excluded, Reason |
| `GrantPermissionAction` | ConnectionId, Permission, TargetName |
| `RevokePermissionAction` | ConnectionId, Permission, TargetName |

The following table explains the binding configuration properties that you set in the function.json file and the `WebPubSub` attribute.

| function.json property | Attribute property | Description |
| --- | --- | --- |
| **type** | n/a | Must be set to `webPubSub` |
| **direction** | n/a | Must be set to `out` |
| **name** | n/a | Variable name used in function code for output binding object. |
| **hub** | Hub | The value must be set to the name of the Web PubSub hub for the function to be triggered. We support set the value in attribute as higher priority, or it can be set in app settings as a global value. |
| **connection** | Connection | The name of the app setting that contains the Web PubSub Service connection string (defaults to "WebPubSubConnectionString"). |

You can also easily [enable console logging](https://github.com/Azure/azure-sdk-for-net/blob/master/sdk/core/Azure.Core/samples/Diagnostics.md#logging) if you want to dig deeper into the requests you're making against the service.

Use these resources to start building your own application:
