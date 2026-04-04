# Advanced

**Source:** [https://developer.wordpress.org/apis/making-http-requests/advanced/](https://developer.wordpress.org/apis/making-http-requests/advanced/)







## In this article


Table of Contents- Other methods
- Options
- Headers



↑Back to top



Here are some advanced usage of the HTTP API.


## Other methods


GET and POST are the most commonly used methods when making a HTTP request, but there are many others, such as DELETE, PUT, PATCH, OPTIONS, etc.


The WordPress HTTP API does not have one specific helper function for each method, but rest assured that the great people developing WordPress already thought of that and lovingly providedwp_remote_request(). This function takes the same two parameters aswp_remote_get(), and allows you to specify the HTTP method as well. What data you need to pass along is up to your method.


To send a DELETE method, for example, you may have something similar to the following:


```
$args     = array(
    'method' => 'DELETE',
);
$response = wp_remote_request( 'http://some-api.com/object/to/delete', $args );
```


## Options


As you probably noticed by now, all the helper functions take a second$argsparameter that allows you to set additional options to your request.


For example,timeoutallows for setting the time in seconds, before the connection is dropped and an error is returned. Thehttpversionargument sets the HTTP version and defaults to ‘1.0’, however depending on the service you are interacting with you may need to set this to ‘1.1’.


CheckWP_Http::request()method documentation for all available options and what they do.


## Headers


It can be pretty important, and sometimes required by the API, to check a resource status using HEAD before retrieving it. On high traffic APIs, GET is often limited to number of requests per minute or hour. There is no need to even attempt a GET request unless the HEAD request shows that the data on the API has been updated.


Going back to the GitHub example, here are are few headers to watch out for. Most of these headers are standard, but you should always check the API docs to ensure you understand which headers are named what, and their purpose.


- x-ratelimit-limit– Number of requests allowed in a time period
- x-ratelimit-remaining– Number of remaining available requests in time period
- content-length– How large the content is in bytes. Can be useful to warn the user if the content is fairly large
- last-modified– When the resource was last modified. Highly useful to caching tools
- cache-control– How should the client handle caching


The following will check the HEAD value of my GitHub user account:


```
$response = wp_remote_head( 'https://api.github.com/users/wordpress' );
```


$responseshould look similar to:


```
Array(
    [headers] => Array
        (
        [server] => nginx
        [date] => Fri, 05 Oct 2012 05:21:26 GMT
        [content-type] => application/json; charset=utf-8
        [connection] => close
        [status] => 200 OK
        [vary] => Accept
        [x-ratelimit-remaining] => 4982
        [content-length] => 594
        [last-modified] => Fri, 05 Oct 2012 04:39:58 GMT
        [etag] => "5d5e6f7a09462d6a2b473fb616a26d2a"
        [x-github-media-type] => github.beta
        [cache-control] => public, s-maxage=60, max-age=60
        [x-content-type-options] => nosniff
        [x-ratelimit-limit] => 5000
    )
    [body] =>
    [response] => Array
        (
        [preserved_text 39a8515bd2dce2aa06ee8a2a6656b1de /] => 200
        [message] => OK
    )
    [cookies] => Array(
    )
    [filename] =>
)
```


All of the same helper functions can be used on this function as with the previous two. The exception here being that HEAD never returns a body, so that element will always be empty.





First published


July 13, 2020


Last updated


November 17, 2022



[PreviousPerformancePrevious: Performance](https://developer.wordpress.org/apis/making-http-requests/performance/)
[NextAuthenticationNext: Authentication](https://developer.wordpress.org/apis/making-http-requests/authentication/)


