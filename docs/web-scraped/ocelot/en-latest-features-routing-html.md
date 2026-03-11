# Source: https://ocelot.readthedocs.io/en/latest/features/routing.html

Title: Routing — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/features/routing.html

Markdown Content:
Ocelot’s primary function is to handle incoming HTTP requests and forward them to a downstream service. Currently, Ocelot supports this only through HTTP requests. In the future, it might support other transport mechanisms.

Ocelot defines the process of routing one request to another as a “Route”. To make Ocelot functional, you must set up a _route_ in its configuration.

{
 "Routes": []
}

To configure a _route_, you need to add one to the `Routes` JSON array.

{
 "UpstreamHttpMethod": [ "Get", "Post" ],
 "UpstreamPathTemplate": "/posts/{postId}",
 "DownstreamPathTemplate": "/api/posts/{postId}",
 "DownstreamScheme": "https",
 "DownstreamHostAndPorts": [
 { "Host": "localhost", "Port": 80 }
 ]
}

The `DownstreamPathTemplate`, `DownstreamScheme`, and `DownstreamHostAndPorts` properties define the URL to which a request will be forwarded.

The `DownstreamHostAndPorts` property is a collection that specifies the host and port of downstream services to which you intend to forward requests. Typically, it contains a single entry; however, in cases where _load balancing_ is required, Ocelot allows you to add multiple entries and select an appropriate [Load Balancer](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html).

The `UpstreamPathTemplate` property specifies the URL that Ocelot uses to determine the appropriate `DownstreamPathTemplate` for a given request. The `UpstreamHttpMethod` property enables Ocelot to differentiate between requests with different HTTP verbs directed to the same URL. You can either specify a particular list of HTTP methods or leave the list empty to allow all methods.

> **Note**: The complete schema on a single _route_ object is described in the [Route Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-route-schema) section of the [Configuration](https://ocelot.readthedocs.io/en/latest/features/configuration.html) feature.

Placeholders[¶](https://ocelot.readthedocs.io/en/latest/features/routing.html#placeholders "Link to this heading")
------------------------------------------------------------------------------------------------------------------

In Ocelot, you can add placeholders for variables to your templates using the format of `{something}`. The placeholder variable must be included in both the `DownstreamPathTemplate` and `UpstreamPathTemplate` properties. When present, Ocelot attempts to substitute the value of the placeholder from the `UpstreamPathTemplate` into the `DownstreamPathTemplate` for each request it processes.

You can also do a [Catch All](https://ocelot.readthedocs.io/en/latest/features/routing.html#routing-catch-all) type of _route_ e.g.

{
 "UpstreamHttpMethod": [ "Get", "Post" ],
 "UpstreamPathTemplate": "/{everything}",
 "DownstreamPathTemplate": "/api/{everything}",
 "DownstreamScheme": "https",
 "DownstreamHostAndPorts": [
 { "Host": "localhost", "Port": 80 }
 ]
}

This will forward all path and query string combinations to the downstream service, appending them after the `/api` path.

> **Note**: The default routing configuration is **case-insensitive**. To change this, you can specify the following setting on a per-route basis:
> 
> 
> 
> "RouteIsCaseSensitive": true
> 
> 
> This means that when Ocelot attempts to match an incoming upstream URL with an upstream template, the evaluation will be _case-sensitive_.

### Embedded Placeholders [[1]](https://ocelot.readthedocs.io/en/latest/features/routing.html#f1)[¶](https://ocelot.readthedocs.io/en/latest/features/routing.html#embedded-placeholders "Link to this heading")

Before version [23.4](https://github.com/ThreeMammals/Ocelot/releases/tag/23.4.0), Ocelot could not evaluate multiple placeholders embedded between two forward slashes (`/`). Additionally, it faced difficulties distinguishing placeholders from other elements within the slashes. For example, when the pattern `/{url}-2/` was applied to `/y-2/`, it would produce `{url}` with `y-2` value.

We have introduced an improved method for placeholder evaluation, making it easier to identify placeholders in complex URLs.

**Example**:

*   **Path Pattern**: `/api/invoices_{url0}/{url1}-{url2}_abcd/{url3}?urlId={url4}`

*   **Upstream URL Path**: `/api/invoices_super/123-456_abcd/789?urlId=987`

*   **Resulting Placeholders**:

    *   `{url0}` = `super`

    *   `{url1}` = `123`

    *   `{url2}` = `456`

    *   `{url3}` = `789`

    *   `{url4}` = `987`

> **Note**, we believe this feature should be compatible with any URL query strings, although it has not been thoroughly tested.

### Empty Placeholders [[2]](https://ocelot.readthedocs.io/en/latest/features/routing.html#f2)[¶](https://ocelot.readthedocs.io/en/latest/features/routing.html#empty-placeholders "Link to this heading")

This represents a special edge case of [Placeholders](https://ocelot.readthedocs.io/en/latest/features/routing.html#routing-placeholders), in which the value of the placeholder is simply an empty string (`""`).

For example, given the following _route_ configuration:

{
 "UpstreamPathTemplate": "/invoices/{url}",
 "DownstreamPathTemplate": "/api/invoices/{url}",
}

This route works correctly when `{url}` is specified. For instance:

*   `/invoices/123`→`/api/invoices/123`

**Edge Cases with Empty Placeholder Values**:

1.   **Empty Placeholder**: When `{url}` is empty, the upstream path `/invoices/` routes to the downstream path `/api/invoices/`.

2.   **Omitting the Last Slash**: When the trailing slash is omitted, the upstream path `/invoices` should still route to the downstream path `/api/invoices`. This behavior aligns intuitively with user expectations.

Catch All[¶](https://ocelot.readthedocs.io/en/latest/features/routing.html#catch-all "Link to this heading")
------------------------------------------------------------------------------------------------------------

Ocelot’s _routing_ supports a _“Catch All”_ style, allowing users to specify routes that match all incoming traffic.

If you configure your settings as shown below, all requests will be proxied directly. The placeholder `{catchAll}` is not significant, and any name can be used.

{
 "UpstreamPathTemplate": "/{catchAll}",
 "DownstreamPathTemplate": "/{catchAll}",
 // ...
}

The _“Catch All”_ route has a lower [priority](https://ocelot.readthedocs.io/en/latest/features/routing.html#routing-priority) than other routes. If the following route is included in your configuration, Ocelot will match it before the _“Catch All”_ route.

{
 "UpstreamPathTemplate": "/",
 "DownstreamPathTemplate": "/",
 // ...
}

Priority [[3]](https://ocelot.readthedocs.io/en/latest/features/routing.html#f3)[¶](https://ocelot.readthedocs.io/en/latest/features/routing.html#priority "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can define the order in which your _routes_ match the upstream URL by including a `Priority` property in the [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/ocelot.json) file.

{
 "Priority": 0
}

Priority **0** is the lowest _priority_. Ocelot always assigns `0` to [Catch All](https://ocelot.readthedocs.io/en/latest/features/routing.html#routing-catch-all) routes, and this value is still hardcoded. Beyond that, you are free to assign any _priority_ you wish.

e.g. you could have

{
 "UpstreamPathTemplate": "/goods/{catchAll}",
 "Priority": 0
}

and

{
 "UpstreamPathTemplate": "/goods/delete",
 "Priority": 1
}

In the example above, if a request is made to Ocelot on `/goods/delete`, it will match the `/goods/delete` route. Previously, it would have matched `/goods/{catchAll}`, as this was the first _route_ in the list.

Query Placeholders[¶](https://ocelot.readthedocs.io/en/latest/features/routing.html#query-placeholders "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------

In addition to URL path [Placeholders](https://ocelot.readthedocs.io/en/latest/features/routing.html#routing-placeholders), Ocelot can forward query string parameters, processing them in the form of `{something}`. The query parameter placeholder must be included in both the `DownstreamPathTemplate` and `UpstreamPathTemplate` properties. Placeholder replacement works bi-directionally between paths and query strings, although it is subject to certain restrictions (see [Merging of Query Parameters](https://ocelot.readthedocs.io/en/latest/features/routing.html#routing-merging-of-query-parameters)).

### Path to Query String direction[¶](https://ocelot.readthedocs.io/en/latest/features/routing.html#path-to-query-string-direction "Link to this heading")

Ocelot allows you to include a query string as part of the `DownstreamPathTemplate`, as demonstrated in the following example:

{
 "UpstreamPathTemplate": "/api/units/{subscription}/{unit}/updates",
 "DownstreamPathTemplate": "/api/subscriptions/{subscription}/updates?unitId={unit}",
}

In this example, Ocelot uses the value of the `{unit}` placeholder from the upstream path template and includes it in the downstream request as a query string parameter named `unitId`.

> **Note**: Ensure that the placeholder is named differently to account for the [Merging of Query Parameters](https://ocelot.readthedocs.io/en/latest/features/routing.html#routing-merging-of-query-parameters).

### Query String to Path direction[¶](https://ocelot.readthedocs.io/en/latest/features/routing.html#query-string-to-path-direction "Link to this heading")

Ocelot also allows you to include query string parameters in the `UpstreamPathTemplate`, enabling you to match specific queries to corresponding services:

{
 "UpstreamPathTemplate": "/api/subscriptions/{subscriptionId}/updates?unitId={uid}",
 "DownstreamPathTemplate": "/api/units/{subscriptionId}/{uid}/updates",
}

In this example, Ocelot matches only requests with a corresponding URL path where the query string begins with `unitId=something`. Additional queries are permitted but must follow the matching parameter. Additionally, Ocelot replaces the `{uid}` parameter in the query string and incorporates it into the downstream request path.

> **Note**: The best practice is to use a placeholder name that differs from the name of the query parameter to accommodate the [Merging of Query Parameters](https://ocelot.readthedocs.io/en/latest/features/routing.html#routing-merging-of-query-parameters).

### Catch All Query String[¶](https://ocelot.readthedocs.io/en/latest/features/routing.html#catch-all-query-string "Link to this heading")

Ocelot’s _routing_ also supports a “[Catch All](https://ocelot.readthedocs.io/en/latest/features/routing.html#routing-catch-all)” style, allowing all query string parameters to be forwarded. The placeholder `{query}` is not significant, and any name can be used.

{
 "UpstreamPathTemplate": "/contracts?{query}",
 "DownstreamPathTemplate": "/apipath/contracts?{query}",
}

This query string routing feature is particularly useful in scenarios where the query string needs to be routed without any transformations—for example, OData filters (see issue [1174](https://github.com/ThreeMammals/Ocelot/issues/1174)).

> **Note**: The `{query}` placeholder can remain empty while catching all query strings, as this functionality is part of the “[Empty Placeholders](https://ocelot.readthedocs.io/en/latest/features/routing.html#routing-empty-placeholders)” feature [[2]](https://ocelot.readthedocs.io/en/latest/features/routing.html#f2). Consequently, upstream paths `/contracts?` and `/contracts` are routed to the downstream path `/apipath/contracts`, with no query string attached.

### Merging of Query Parameters[¶](https://ocelot.readthedocs.io/en/latest/features/routing.html#merging-of-query-parameters "Link to this heading")

Query string parameters are unsorted and merged to form the final downstream URL. This process is crucial because the `DownstreamUrlCreatorMiddleware` requires control over placeholder replacement and the merging of duplicate parameters. A parameter that appears first in the `UpstreamPathTemplate` may occupy a different position in the final downstream URL. Moreover, if the `DownstreamPathTemplate` includes query parameters at the beginning, their positions in the `UpstreamPathTemplate` will remain undefined unless explicitly specified.

In a typical scenario, the merging algorithm constructs the final downstream URL query string as follows:

1.   It begins by taking the initially defined query parameters in the `DownstreamPathTemplate` and placing them at the start, along with any necessary placeholder replacements.

2.   Next, it adds all parameters from the [Catch All Query String](https://ocelot.readthedocs.io/en/latest/features/routing.html#routing-catch-all-query-string), represented by the placeholder `{query}`, in the second position—following the explicitly defined parameters from _step 1_.

3.   Finally, it appends any remaining replaced placeholder values as parameter values to the end of the query string, if present.

#### Array parameters in ASP.NET API’s model binding[¶](https://ocelot.readthedocs.io/en/latest/features/routing.html#array-parameters-in-asp-net-api-s-model-binding "Link to this heading")

Due to the merging of parameters, ASP.NET API’s special [model binding](https://learn.microsoft.com/en-us/aspnet/core/mvc/models/model-binding?view=aspnetcore-8.0#collections) for arrays does not support the array item representation format `selectedCourses=1050&selectedCourses=2000`. This query string will be merged into `selectedCourses=1050` in the downstream URL, leading to the loss of array data. It is essential for upstream clients to generate the correct query string for array models, such as `selectedCourses[0]=1050&selectedCourses[1]=2000`. For a detailed explanation of array model binding, refer to the documentation: “[Bind arrays and string values from headers and query strings](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis/parameter-binding?view=aspnetcore-8.0#bind-arrays-and-string-values-from-headers-and-query-strings)”.

#### Control over parameter existence[¶](https://ocelot.readthedocs.io/en/latest/features/routing.html#control-over-parameter-existence "Link to this heading")

Be aware that query string placeholders are subject to naming restrictions due to the implementation of the `DownstreamUrlCreatorMiddleware` merging algorithm. Nevertheless, this restriction also offers flexibility in managing the presence of parameters in the final downstream URL based on their names.

Consider the following two development scenarios →

1.   A developer wishes **to preserve a parameter** after substituting a placeholder (refer to issue [473](https://github.com/ThreeMammals/Ocelot/issues/473)). This requires the use of the following template definition:

{
 "UpstreamPathTemplate": "/path/{serverId}/{action}",
 "DownstreamPathTemplate": "/path2/{action}?server={serverId}"
} In this case, the `{serverId}` placeholder and the server parameter **names differ**. As a result, the `server` parameter is retained.

It is important to note that, due to the case-sensitive comparison of names, the `server` parameter will not be preserved with the `{server}` placeholder. However, using the `{Server}` placeholder is acceptable for retaining the parameter. 
2.   The developer intends **to remove an outdated parameter** after substituting a placeholder (refer to issue [952](https://github.com/ThreeMammals/Ocelot/issues/952)). To achieve this, identical names must be used, adhering to case-sensitive comparison rules.

{
 "UpstreamPathTemplate": "/users?userId={userId}",
 "DownstreamPathTemplate": "/persons?personId={userId}"
} Thus, the `{userId}` placeholder and the `userId` parameter **have identical names**. As a result, the `userId` parameter is eliminated.

Be aware that, due to the case-sensitive nature of the comparison, the `userId` parameter will not be removed if the `{userid}` placeholder is used. 

Upstream Host [[4]](https://ocelot.readthedocs.io/en/latest/features/routing.html#f4)[¶](https://ocelot.readthedocs.io/en/latest/features/routing.html#upstream-host "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This feature allows you to define routes based on the _upstream host_. It works by examining the `Host` header used by the client and incorporating it into the information used to identify a _route_.

In order to use this feature, add the following to your configuration:

{
 "UpstreamHost": "mydomain.com"
}

The _route_ above will only match requests where the `Host` header value is `mydomain.com`.

If you do not set the `UpstreamHost` on a _route_, any `Host` header will match it. As a result, if you have two routes that are identical except for the `UpstreamHost`, where one is null and the other is set, Ocelot will prioritize the one that is set.

Security Options [[6]](https://ocelot.readthedocs.io/en/latest/features/routing.html#f6)[¶](https://ocelot.readthedocs.io/en/latest/features/routing.html#security-options "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Ocelot facilitates the management of multiple patterns for allowed and blocked IPs using the [IPAddressRange](https://github.com/jsakamoto/ipaddressrange) package, which is licensed under the [MPL-2.0 license](https://github.com/jsakamoto/ipaddressrange/blob/master/LICENSE).

This feature is designed to enhance IP management, allowing for the inclusion or exclusion of a broad IP range using CIDR notation or specific IP ranges. The current managed patterns are as follows:

| _IP Rule_ | _Example_ |
| --- | --- |
| Single IP | `192.168.1.1` |
| IP Range | `192.168.1.1-192.168.1.250` |
| IP Short Range | `192.168.1.1-250` |
| IP Subnet | `192.168.1.0/255.255.255.0` |
| CIDR IPv4 | `192.168.1.0/24` |
| CIDR IPv6 | `fe80::/10` |

Here is a simple example:

{
 "SecurityOptions": {
 "IPBlockedList": [ "192.168.0.0/23" ],
 "IPAllowedList": ["192.168.0.15", "192.168.1.15"],
 "ExcludeAllowedFromBlocked": true
 }
}

Please **note**:

*   The allowed/blocked lists are evaluated during configuration loading.

*   The `ExcludeAllowedFromBlocked` property enables specifying a wide range of blocked IP addresses while allowing a subrange of IP addresses. Default value: `false`.

*   The absence of a property in _Security Options_ is permitted, as it takes the default value.

*   _Security Options_ can be configured _globally_ in the `GlobalConfiguration` JSON [[7]](https://ocelot.readthedocs.io/en/latest/features/routing.html#f7). However, they are ignored if overriding options are specified at the route level.

Dynamic Routing [[8]](https://ocelot.readthedocs.io/en/latest/features/routing.html#f8)[¶](https://ocelot.readthedocs.io/en/latest/features/routing.html#dynamic-routing "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The concept of dynamic _routing_ allows you to use a [Service Discovery](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html) provider, eliminating the need to manually configure _route_ settings. For more details, refer to the [Dynamic Routing](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html#sd-dynamic-routing) complete reference in the “[Service Discovery](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html)” chapter.

Errors and Gotchas[¶](https://ocelot.readthedocs.io/en/latest/features/routing.html#errors-and-gotchas "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------

In this section, Ocelot team has gathered user scenarios where routing behavior was unclear or errors appeared in the logs. Please note that the failed routing cases listed below do not represent all application configurations. If your case is not included, feel free to open a “[Show and tell](https://github.com/ThreeMammals/Ocelot/discussions/categories/show-and-tell)” discussion.

*   **Magic 499 status**. According to Ocelot Core’s design, HTTP status code [499 (Client Closed Request)](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status499clientclosedrequest) is returned in cases involving an `OperationCanceledException`. Please note that due to extensive warning-level logging, you may encounter spikes in `499` responses—as discussed in thread [2072](https://github.com/ThreeMammals/Ocelot/discussions/2072). This status is typically caused by:

    1.   Forced cancellation of the request by the client

    2.   Browser events such as page refreshes or closures while the downstream request is still in progress

As a quick recipe, the Ocelot team recommends ensuring client stability and, if necessary, adjusting the [Timeout](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-timeout) strategy: either increasing or decreasing the route [Timeout](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-timeout) depending on your usage scenario and the behavior of the downstream service.

*   **Timeout errors aka 503 status**. According to Ocelot Core’s design, HTTP status code [503 (Service Unavailable)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/503) is returned in cases involving a `TimeoutException`. This status is typically caused by:

    1.   Slow downstream services that may fail to respond

    2.   Large requests forwarded to slow downstream services

As a quick recipe, the Ocelot team recommends increasing the route [Timeout](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-timeout) in your configuration. This adjustment can help resolve timeout-related issues with sluggish downstream services, ultimately reducing occurrences of [503 (Service Unavailable)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/503).

> **Note**: For comprehensive documentation regarding errors and status codes in Ocelot, please refer to the [Error Handling](https://ocelot.readthedocs.io/en/latest/features/errorcodes.html) chapter.

* * *
