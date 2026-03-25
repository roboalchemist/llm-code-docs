# Source: https://ocelot.readthedocs.io/en/latest/features/aggregation.html

Title: Aggregation — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/features/aggregation.html

Markdown Content:
_Aggregation_, also known as HTTP response data aggregation, is a well-known Backend for Frontend pattern of Microservices architecture.

> *   [Backend for Frontend (BFF) Pattern: Microservices for UX | Teleport Academy](https://goteleport.com/learn/backend-for-frontend-bff-pattern/)
> 
> *   [Gateway Aggregation pattern | Azure Architecture Center | Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/patterns/gateway-aggregation)
> 
> *   [Backends for Frontends pattern | Azure Architecture Center | Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/patterns/backends-for-frontends)
> 
> *   [Implement API Gateways with Ocelot | .NET microservices - Architecture e-book | Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/multi-container-microservice-net-applications/implement-api-gateways-with-ocelot)

Ocelot allows you to specify _Aggregate Routes_[[1]](https://ocelot.readthedocs.io/en/latest/features/aggregation.html#f1) that combine multiple normal routes and map their responses into a single object. This is particularly useful when a client is making multiple requests to a server that could be consolidated into one. This feature supports the implementation of a Backend for Frontend (BFF) architecture using Ocelot.

Configuration[¶](https://ocelot.readthedocs.io/en/latest/features/aggregation.html#configuration "Link to this heading")
------------------------------------------------------------------------------------------------------------------------

In order to set this up, you need to configure the [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/ocelot.json) file as follows. In this example, two normal routes are specified, each having a `Key` property. An _aggregation_ is then defined, which combines the two routes using their keys listed in `RouteKeys`, and the `UpstreamPathTemplate` is set up to function like a normal route.

> Note that duplicate `UpstreamPathTemplates` are not allowed between `Routes` and `Aggregates`. You can use all of Ocelot’s normal route options, except for `RequestIdKey`, as explained in the [Gotchas](https://ocelot.readthedocs.io/en/latest/features/aggregation.html#agg-gotchas) section.

{
 "Routes": [
 {
 "UpstreamHttpMethod": [ "Get" ],
 "UpstreamPathTemplate": "/laura",
 "DownstreamPathTemplate": "/",
 "DownstreamScheme": "http",
 "DownstreamHostAndPorts": [
 { "Host": "localhost", "Port": 51881 }
 ],
 "Key": "Laura" },
 {
 "UpstreamHttpMethod": [ "Get" ],
 "UpstreamPathTemplate": "/tom",
 "DownstreamPathTemplate": "/",
 "DownstreamScheme": "http",
 "DownstreamHostAndPorts": [
 { "Host": "localhost", "Port": 51882 }
 ],
 "Key": "Tom" }
 ],
 "Aggregates": [ {
 "UpstreamPathTemplate": "/",
 "RouteKeys": [ "Tom", "Laura" ]
 }
 ]
}

You can also set `UpstreamHost` and `RouteIsCaseSensitive` in the _aggregation_ configuration. These settings behave the same as in other routes.

If the route `/tom` returned a body of `{"Age": 19}` and `/laura` returned `{"Age": 25}`, the response after _aggregation_ would be as follows:

{"Tom":{"Age": 19},"Laura":{"Age": 25}}

At the moment, the _aggregation_ is quite simple. Ocelot retrieves the response from your downstream service and inserts it into a JSON dictionary, as shown above. The route `Key` becomes the key of the dictionary, and the response body from your downstream service serves as the value. The resulting object is plain JSON without any formatting or additional spaces.

> **Note 1**: All headers will be lost from the downstream service’s response.
> 
> 
> **Note 2**: Ocelot will always return the content type `application/json` for an aggregate request.
> 
> 
> **Note 3**: If your downstream services return a `404`[Not Found](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404), the aggregate will simply return nothing for that downstream service. It will not change the aggregate response to a `404`, even if all the downstream services return a `404`.

Complex Aggregation [[2]](https://ocelot.readthedocs.io/en/latest/features/aggregation.html#f2)[¶](https://ocelot.readthedocs.io/en/latest/features/aggregation.html#complex-aggregation "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Imagine you would like to use aggregated queries but don’t have all the parameters for your queries. First, you need to call an endpoint to obtain the necessary data, such as a user’s ID, and then return the user’s details.

Let’s say we have an endpoint that returns a series of comments referencing various users or threads. The author of the comments is identified by their ID, but you want to return all the details about the author.

Here, you could use aggregation to: 1) retrieve all the comments, and 2) attach the author details. In fact, two endpoints are called, but for the second, you dynamically replace the user’s ID in the route to obtain the details.

In concrete terms:

1.   `/Comments` contains the `authorId` property.

2.   `/users/{userId}`, with `{userId}` replaced by `authorId`, is used to obtain the user’s details.

To perform the mapping, you need to use the `RouteKeysConfig` list of configuration options for aggreagte route, typed as `AggregateRouteConfig` class:

"RouteKeysConfig": [
 {
 "RouteKey": "UserDetails",
 "JsonPath": "$[*].authorId",
 "Parameter": "userId"
 }
]

`RouteKey` is used as a reference for the route, `JsonPath` indicates where the parameter of interest is located in the first request’s response body, and `Parameter` specifies that the value for `authorId` should be used as the request parameter `userId`.

The final configuration is as follows:

{
 "Routes": [
 {
 "UpstreamPathTemplate": "/Comments",
 "DownstreamPathTemplate": "/",
 // ...
 "Key": "Comments"
 },
 {
 "UpstreamPathTemplate": "/UserDetails/{userId}",
 "DownstreamPathTemplate": "/users/{userId}",
 // ...
 "Key": "UserDetails"
 },
 {
 "UpstreamPathTemplate": "/PostDetails/{postId}",
 "DownstreamPathTemplate": "/posts/{postId}",
 // ...
 "Key": "PostDetails"
 }
 ],
 "Aggregates": [
 {
 "UpstreamPathTemplate": "/",
 "UpstreamHost": "localhost",
 "RouteKeys": [ "Comments", "UserDetails", "PostDetails" ],
 "RouteKeysConfig": [ { "RouteKey": "UserDetails", "JsonPath": "$[*].writerId", "Parameter": "userId" }, { "RouteKey": "PostDetails", "JsonPath": "$[*].postId", "Parameter": "postId" } ] }
 ]
}

Custom Aggregators[¶](https://ocelot.readthedocs.io/en/latest/features/aggregation.html#custom-aggregators "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------

Ocelot started with basic request _aggregation_, and since then, a more advanced method has been added. This method allows the user to take the responses from downstream services and aggregate them into a response object. The [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/ocelot.json) setup is almost identical to the basic _aggregation_ approach, except that you need to add an `Aggregator` property, as shown below:

{
 "Routes": [
 {
 "UpstreamPathTemplate": "/laura",
 "DownstreamPathTemplate": "/",
 // ...
 "Key": "Laura"
 },
 {
 "UpstreamPathTemplate": "/tom",
 "DownstreamPathTemplate": "/",
 // ...
 "Key": "Tom"
 }
 ],
 "Aggregates": [
 {
 "UpstreamPathTemplate": "/",
 "RouteKeys": [ "Tom", "Laura" ],
 "Aggregator": "MyAggregator" }
 ]
}

Here, we have added an aggregator called `MyAggregator`. Ocelot will look for this aggregator when it tries to aggregate this route.

In order to make the aggregator available in Ocelot Core, we must add the `MyAggregator` to the `OcelotBuilder` returned by `AddOcelot()`[[3]](https://ocelot.readthedocs.io/en/latest/features/aggregation.html#f3), as shown below:

using Ocelot.Multiplexer;

builder.Services
 .AddOcelot(builder.Configuration)
 .AddSingletonDefinedAggregator<MyAggregator>();

Now, when Ocelot tries to aggregate the route above, it will find the `MyAggregator` in the DI-container and use it to aggregate the route. Since the `MyAggregator` is registered in the DI-container, you can add any dependencies it needs to the container, as shown below:

builder.Services
 .AddSingleton<MyDependency>();// ...
builder.Services
 .AddOcelot(builder.Configuration)
 .AddSingletonDefinedAggregator<MyAggregator>();

In this example, `MyAggregator` depends on `MyDependency`, and it will be resolved by the DI container. In addition to this, Ocelot lets you add transient aggregators, as shown below:

builder.Services
 .AddOcelot(builder.Configuration)
 .AddTransientDefinedAggregator<MyAggregator>();

In order to create an _aggregator_, you must implement the following interface:

public interface IDefinedAggregator
{
 Task<DownstreamResponse> Aggregate(List<HttpContext> responses);
}

With this feature, you can essentially do whatever you want, as the `HttpContext` objects contain the results of all the aggregate requests.

> Please note that if the `HttpClient` throws an exception when making a request to a route in the aggregate, you will not receive a `HttpContext` for it. However, you will receive one for any that succeed. If an exception is thrown, it will be logged.

Below is an example of an _aggregator_ that can be implemented for your solution:

public class MyAggregator : IDefinedAggregator
{
 public async Task<DownstreamResponse> Aggregate(List<HttpContext> responseHttpContexts)
 {
 // The aggregator gets a list of downstream responses as parameter.
 // You can now implement your own logic to aggregate the responses (including bodies and headers) from the downstream services
 var responses = responseHttpContexts.Select(x => x.Items.DownstreamResponse()).ToArray();

 // In this example we are concatenating the results,
 // but you could create a more complex construct, up to you.
 var contentList = new List<string>();
 foreach (var response in responses)
 {
 var content = await response.Content.ReadAsStringAsync();
 contentList.Add(content);
 }

 // The only constraint here: You must return a DownstreamResponse object.
 return new DownstreamResponse(
 new StringContent(JsonConvert.SerializeObject(contentList)),
 HttpStatusCode.OK,
 responses.SelectMany(x => x.Headers).ToList(),
 "reason");
 }
}

Gotchas[¶](https://ocelot.readthedocs.io/en/latest/features/aggregation.html#gotchas "Link to this heading")
------------------------------------------------------------------------------------------------------------

*   You cannot use routes with specific `RequestIdKeys`, as this would be overly complicated to track.

*   _Aggregation_ supports only the `GET` HTTP verb.

*   _Aggregation_ allows the forwarding of `HttpRequest.Body` to downstream services by duplicating the body data. Form data and attached files should also be forwarded. It is essential to specify the `Content-Length` header in requests to the upstream; otherwise, Ocelot will log warnings such as: _“Aggregation does not support body copy without a Content-Length header!”_

* * *
