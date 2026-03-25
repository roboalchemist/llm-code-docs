# Source: https://docs.xano.com/the-function-stack/additional-features/response-caching.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Response Caching

#### Response Caching

[**Watch a practical example**](https://youtu.be/TTQky7FqRQE) of Response Caching using the [Star Wars API](https://swapi.dev/)

From the settings of an [API Endpoint](/the-function-stack/building-with-visual-development/apis) or [Custom Function](/the-function-stack/functions/custom-functions) response caching can be accessed. Response caching is an abstracted caching method to cache the response of an endpoint or function.

<img src="https://mintcdn.com/xano-997cb9ee/dyVYERTquSXdpw_-/images/CleanShot2025-08-05at09.51.13.png?fit=max&auto=format&n=dyVYERTquSXdpw_-&q=85&s=f5a975316378942d772d3205f7797c1e" alt="CleanShot 2025-08-05 at 09.51.13.png" width="990" height="653" data-path="images/CleanShot2025-08-05at09.51.13.png" />

You can choose from a number of different settings to determine how to cache the response.

**TTL** - Stands for time to live. This defines how long to cache the response for. Options range from 5 seconds to 7 days. After the TTL expires, the query will run normally and reset the response cache.

**Use inputs for caching signature** - This is defaulted to yes. It will create a response cache for each new or unique set of inputs for the duration of the TTL.

**Use IP address for caching signature** - This is defaulted to no. It can be used if you wish to record a response cache on a per IP address basis.

**HTTP Request Header Names** - This is optional. You are able to cache the HTTP request headers of the response. Add the request header name or names that you wish to cache.

**Environment Variable Names** - This is optional. It allows you to cache any defined [environment variable](/what-xano-includes/workspace/settings/environment-variables) names to the response cache.

**Use Authentication ID for caching signature** - When an API endpoint requires [authentication](/building-features/authentication-sign-up-and-log-in/authentication), this option becomes available. This can be turned on to enable a caching on a per user basis for authenticated endpoints.

#### Example Use Cases

**Use inputs and disable authentication ID for caching signature**

Company statistics for your entire team. If you need to display company statistics for your entire team then you may consider using inputs and disabling authentication ID for caching signature. You API endpoint would require authentication so that only your team can access the API but you would disable the authentication ID for caching. This would make it so the cache response is not on a per user basis. Since it is company statistics you want each user to see the same statistics. Using inputs enables each searched or inputted value gets cached, so if other team members search or input the same values then the response will already be there.

**Use inputs and use authentication ID for caching signature**

Personal statistics. In this scenario you would enable both inputs and authentication ID for caching signature. This would cache responses on a per user basis. For example, you might have each individual sales rep reviewing their own statistics for the quarter. Enabling inputs would cache the response for each inputted value. Additionally, enabling authentication ID for caching signature (with the appropriate business logic) would cache the responses on a per user basis.

**Disable inputs and disable authentication ID for caching signature**

There's a movie night event and you want to generate a random movie. Imagine you have an API that inputs a category or genre of movie and based on that, returns a random movie. By disabling both inputs and authentication ID for caching signature, this will allow for the first search on this API to generate a random movie to be played during movie night. It won't matter what other people search. So if the first person searched Science-Fiction and the result is Star Wars then all other searches (drama, action, comedy, etc.) will return Star Wars. Now you have your random movie for movie night.


Built with [Mintlify](https://mintlify.com).