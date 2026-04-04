# Source: https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html

Title: Headers Transformation — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html

Markdown Content:
Ocelot allows the user to transform [HTTP headers](https://developer.mozilla.org/en-US/docs/Glossary/HTTP_header) both before and after the downstream request.

> **Note**: _Headers Transformation_ is generally available for static routes with a global configuration. For dynamic and aggregate routes, this feature is not implemented. This limitation is noted in the current [Roadmap](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#ht-roadmap).

Schema[¶](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#schema "Link to this heading")
--------------------------------------------------------------------------------------------------------------------

As you may already know from the [Configuration](https://ocelot.readthedocs.io/en/latest/features/configuration.html) chapter and the [Route Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-route-schema) section, the route’s _Headers Transformation_ schema is quite simple, a JSON dictionary:

"DownstreamHeaderTransform": {
 // "header_name": "transformation_expression",
},
"UpstreamHeaderTransform": {
 // "header_name": "transformation_expression",
},

Typically, a `transformation_expression` is a constant header value, a single placeholder from the [Placeholders](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#ht-placeholders) list, or a “[Find and Replace](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#ht-find-and-replace)” expression. Additionally, the [Global Configuration Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-global-configuration-schema) allows configuring global _Headers Transformations_ (refer to the [Configuration](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#ht-configuration) section).

Configuration [[1]](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#f1)[¶](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#configuration "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A complete _configuration_ consists of both route-level and global _Headers Transformations_.

{
 "Routes": [
 {
 "DownstreamHeaderTransform": {
 // ...
 },
 "UpstreamHeaderTransform": {
 // ...
 }
 }
 ],
 "GlobalConfiguration": {
 "DownstreamHeaderTransform": {
 // ...
 },
 "UpstreamHeaderTransform": {
 // ...
 }
 }
}

> **Note**: Route-level transformations take precedence over global transformations. In addition, when route-level transformations are defined, they do not entirely override the full set of header names from the global configuration. Ocelot’s Core internal [Merge](https://github.com/search?q=repo%3AThreeMammals%2FOcelot+%22public+static+IEnumerable%3CHeader%3E+Merge%22&type=code) algorithm identifies global header names not specified at the route level and appends them to the route’s header set.

Find and Replace [[2]](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#f2)[¶](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#find-and-replace "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In order to transform a header first we specify the header key and then the type of transform we want e.g.

"Test": "http://www.bbc.co.uk/, http://ocelot.net/"

The key is `Test` and the value is `http://www.bbc.co.uk/, http://ocelot.net/`. The value is saying: replace `http://www.bbc.co.uk/` with `http://ocelot.net/`. The syntax is `{find}, {replace}`. Hopefully pretty simple. There are examples below that explain more.

**Pre Downstream Request**

Add the following to a Route in [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/ocelot.json) in order to replace `http://www.bbc.co.uk/` with `http://ocelot.net/`. This header will be changed before the request downstream and will be sent to the downstream server.

"UpstreamHeaderTransform": {
 "Test": "http://www.bbc.co.uk/, http://ocelot.net/"
}

**Post Downstream Request**

Add the following to a Route in [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/ocelot.json) in order to replace `http://www.bbc.co.uk/` with `http://ocelot.net/`. This transformation will take place after Ocelot has received the response from the downstream service.

"DownstreamHeaderTransform": {
 "Test": "http://www.bbc.co.uk/, http://ocelot.net/"
}

Add to Request [[3]](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#f3)[¶](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#add-to-request "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you want to add a header to your upstream request please add the following to a route in your [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/ocelot.json):

"UpstreamHeaderTransform": {
 "Uncle": "Bob"
}

In the example above a header with the key `Uncle` and value `Bob` would be send to to the upstream service.

> [Placeholders](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#ht-placeholders) are supported too (see below).

Add to Response [[4]](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#f4)[¶](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#add-to-response "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you want to add a header to your downstream response, please add the following to a route in [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/ocelot.json):

"DownstreamHeaderTransform": {
 "Uncle": "Bob"
}

In the example above a header with the key `Uncle` and value `Bob` would be returned by Ocelot when requesting the specific route.

If you want to return the [Butterfly](https://ocelot.readthedocs.io/en/latest/features/tracing.html#tr-butterfly) Trace ID, do something like the following:

"DownstreamHeaderTransform": {
 "AnyKey": "{TraceId}"
}

Placeholders[¶](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#placeholders "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------

Ocelot allows placeholders that can be used in header transformation.

| _Placeholder_ | _Description_ |
| --- | --- |
| `{BaseUrl}` | This will use Ocelot base URL e.g. `http://localhost:5000` as its value. |
| `{DownstreamBaseUrl}` | This will use the downstream services base URL e.g. `http://localhost:5000` as its value. This only works for `DownstreamHeaderTransform` route option at the moment. |
| `{RemoteIpAddress}` | This will find the clients IP address using `HttpContext.Connection.RemoteIpAddress`, so you will get back some IP. See more in the [GetRemoteIpAddress](https://github.com/search?q=repo%3AThreeMammals%2FOcelot%20%22Response%3Cstring%3E%20GetRemoteIpAddress()%22&type=code) method. |
| `{TraceId}` | This will use the [Butterfly](https://ocelot.readthedocs.io/en/latest/features/tracing.html#tr-butterfly) Trace ID. This only works for `DownstreamHeaderTransform` route option at the moment. |
| `{UpstreamHost}` | This will look for the incoming `Host` header. |

For now, we believe these placeholders are sufficient for basic user scenarios. However, if you need additional placeholders, refer to the [Roadmap](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#ht-roadmap).

Samples[¶](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#samples "Link to this heading")
----------------------------------------------------------------------------------------------------------------------

### Handling 302 redirects[¶](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#handling-302-redirects "Link to this heading")

Ocelot will by default automatically follow redirects, however if you want to return the location header to the client, you might want to change the location to be Ocelot not the downstream service. Ocelot allows this with the following configuration:

"DownstreamHeaderTransform": {
 "Location": "http://www.bbc.co.uk/, http://ocelot.net/"
},
"HttpHandlerOptions": {
 "AllowAutoRedirect": false,
}

Or, you could use the `{BaseUrl}` placeholder.

"DownstreamHeaderTransform": {
 "Location": "http://localhost:6773, {BaseUrl}"
},
"HttpHandlerOptions": {
 "AllowAutoRedirect": false,
}

Finally, if you are using a load balancer with Ocelot, you will get multiple downstream base URLs so the above would not work. In this case you can do the following:

"DownstreamHeaderTransform": {
 "Location": "{DownstreamBaseUrl}, {BaseUrl}"
},
"HttpHandlerOptions": {
 "AllowAutoRedirect": false,
}

### `X-Forwarded-For` header[¶](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#x-forwarded-for-header "Link to this heading")

An example of using `{RemoteIpAddress}` placeholder:

"UpstreamHeaderTransform": {
 "X-Forwarded-For": "{RemoteIpAddress}"
}

Roadmap[¶](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#roadmap "Link to this heading")
----------------------------------------------------------------------------------------------------------------------

1.   Ideally the “[Find and Replace](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#ht-find-and-replace)” feature would be able to support the fact that a header can have multiple values. At the moment it just assumes one. It would also be nice if it could multi find and replace e.g.

"DownstreamHeaderTransform": {
 "Location": "[{one,one},{two,two}]"
},
"HttpHandlerOptions": {
 "AllowAutoRedirect": false,
} 

1.   The _Headers Transformation_ feature is not implemented for [Dynamic Routes](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-dynamic-route-schema) and [Aggregate Routes](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-aggregate-route-schema). For [Dynamic Routing](https://ocelot.readthedocs.io/en/latest/features/routing.html#routing-dynamic), potential development would require [moderate effort](https://github.com/ThreeMammals/Ocelot/labels/medium%20effort). However, the Ocelot team expects that designing and implementing _Headers Transformation_ for [Aggregation](https://ocelot.readthedocs.io/en/latest/features/aggregation.html) will demand [significant effort](https://github.com/ThreeMammals/Ocelot/labels/large%20effort), as aggregated routes typically lose their headers.

Ideas and proposals are welcome in the repository’s [Discussions](https://github.com/ThreeMammals/Ocelot/discussions) space. [![Image 1: octocat](https://github.githubassets.com/images/icons/emoji/octocat.png)](https://github.githubassets.com/images/icons/emoji/octocat.png)

* * *
