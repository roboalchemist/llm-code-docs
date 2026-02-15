# GETting data from an external service

**Source:** [https://developer.wordpress.org/apis/making-http-requests/getting-data-from-an-external-service/](https://developer.wordpress.org/apis/making-http-requests/getting-data-from-an-external-service/)







## In this article


Table of Contents- GET the body you always wanted
- GET the response code
- GET a specific header
- GET using basic authentication



↑Back to top



GETting data is made incredibly simple in WordPress through thewp_remote_get()function. This function takes the following two arguments:


1. $url– Resource to retrieve data from. This must be in a standard HTTP format
1. $args– OPTIONAL – You may pass an array of arguments in here to alter behavior and headers, such as cookies, follow redirects, etc.


The following defaults are assumed, though they can be changed via the$argsparameter:


- method – GET
- timeout – 5 – How long to wait before giving up
- redirection – 5 – How many times to follow redirections.
- httpversion – 1.0
- blocking – true – Should the rest of the page wait to finish loading until this operation is complete?
- headers – array()
- body – null
- cookies – array()


BecauseGitHubprovides an excellent API that does not require app registration for many public aspects we will target GitHub API in the following examples.


Let’s use the URL to a GitHub WordPress organization and see what sort of information we can get.


```
$response = wp_remote_get( 'https://api.github.com/users/wordpress' );
```


$responsewill contain all the headers, content, and other meta data about our request.


Response from previous example will be something like


```
Array(
    [headers] => Array(
        [server] => nginx
        [date] => Fri, 05 Oct 2012 04:43:50 GMT
        [content-type] => application/json; charset=utf-8
        [connection] => close
        [status] => 200 OK
        [vary] => Accept
        [x-ratelimit-remaining] => 4988
        [content-length] => 594
        [last-modified] => Fri, 05 Oct 2012 04:39:58 GMT
        [etag] => "5d5e6f7a09462d6a2b473fb616a26d2a"
        [x-github-media-type] => github.beta
        [cache-control] => public, s-maxage=60, max-age=60
        [x-content-type-options] => nosniff
        [x-ratelimit-limit] => 5000
    )

    [body] => {
"login": "WordPress",
"id": 276006,
"node_id": "MDEyOk9yZ2FuaXphdGlvbjI3NjAwNg==",
"avatar_url": "https://avatars0.githubusercontent.com/u/276006?v=4",
"gravatar_id": "",
"url": "https://api.github.com/users/WordPress",
"html_url": "https://github.com/WordPress",
"followers_url": "https://api.github.com/users/WordPress/followers",
"following_url": "https://api.github.com/users/WordPress/following{/other_user}",
"gists_url": "https://api.github.com/users/WordPress/gists{/gist_id}",
"starred_url": "https://api.github.com/users/WordPress/starred{/owner}{/repo}",
"subscriptions_url": "https://api.github.com/users/WordPress/subscriptions",
"organizations_url": "https://api.github.com/users/WordPress/orgs",
"repos_url": "https://api.github.com/users/WordPress/repos",
"events_url": "https://api.github.com/users/WordPress/events{/privacy}",
"received_events_url": "https://api.github.com/users/WordPress/received_events",
"type": "Organization",
"site_admin": false,
"name": null,
"company": null,
"blog": "https://wordpress.org/",
"location": null,
"email": null,
"hireable": null,
"bio": null,
"twitter_username": null,
"public_repos": 50,
"public_gists": 0,
"followers": 0,
"following": 0,
"created_at": "2010-05-13T22:42:10Z",
"updated_at": "2020-05-22T14:27:02Z"
}
    [response] => Array(
        [preserved_text 5237511b45884ac6db1ff9d7e407f225 /] => 200
        [message] => OK
    )

    [cookies] => Array()
    [filename] =>
)
```


### GET the body you always wanted


To retrieve response body usewp_remote_retrieve_body()function. This function takes just one parameter, the response fromwp_remote_get()function.


```
$response = wp_remote_get( 'https://api.github.com/users/wordpress' );
$body     = wp_remote_retrieve_body( $response );
```


Using the$responsefrom the previous example,$bodywill be something like:


```
{
"login": "WordPress",
"id": 276006,
"node_id": "MDEyOk9yZ2FuaXphdGlvbjI3NjAwNg==",
"avatar_url": "https://avatars0.githubusercontent.com/u/276006?v=4",
"gravatar_id": "",
"url": "https://api.github.com/users/WordPress",
"html_url": "https://github.com/WordPress",
"followers_url": "https://api.github.com/users/WordPress/followers",
"following_url": "https://api.github.com/users/WordPress/following{/other_user}",
"gists_url": "https://api.github.com/users/WordPress/gists{/gist_id}",
"starred_url": "https://api.github.com/users/WordPress/starred{/owner}{/repo}",
"subscriptions_url": "https://api.github.com/users/WordPress/subscriptions",
"organizations_url": "https://api.github.com/users/WordPress/orgs",
"repos_url": "https://api.github.com/users/WordPress/repos",
"events_url": "https://api.github.com/users/WordPress/events{/privacy}",
"received_events_url": "https://api.github.com/users/WordPress/received_events",
"type": "Organization",
"site_admin": false,
"name": null,
"company": null,
"blog": "https://wordpress.org/",
"location": null,
"email": null,
"hireable": null,
"bio": null,
"twitter_username": null,
"public_repos": 50,
"public_gists": 0,
"followers": 0,
"following": 0,
"created_at": "2010-05-13T22:42:10Z",
"updated_at": "2020-05-22T14:27:02Z"
}
```


### GET the response code


You may want to check the response code to ensure your retrieval was successful. This can be done via thewp_remote_retrieve_response_code()function:


```
$http_code = wp_remote_retrieve_response_code( $response );
```


If successful$http_codewill contain200. Otherwise, it will contain some HTTP status codes.


### GET a specific header


If your desire is to retrieve a specific header, say last-modified, you can do so withwp_remote_retrieve_header(). This function takes two parameters


1. $response– The response from the get call
1. $header– Name of the header to retrieve


To retrieve the last-modified header:


```
$last_modified = wp_remote_retrieve_header( $response, 'last-modified' );
```


You can also retrieve all of the headers in an array withwp_remote_retrieve_headers()function.


### GET using basic authentication


APIs that are secured more provide one or more of many different types of authentication. A common, though not highly secure, the authentication method is HTTP Basic Authentication. It can be used in WordPress bypassing ‘Authorization’ to the second parameter of thewp_remote_get()function, as well as the other HTTP method functions.


```
$args = array(
    'headers' => array(
        'Authorization' => 'Basic ' . base64_encode( YOUR_USERNAME . ':' . YOUR_PASSWORD )
    )
);
wp_remote_get( $url, $args );
```


MORE ABOUT AUTH





First published


July 13, 2020


Last updated


November 17, 2022



[PreviousMaking HTTP requestsPrevious: Making HTTP requests](https://developer.wordpress.org/apis/making-http-requests/)
[NextPOSTing data to an external serviceNext: POSTing data to an external service](https://developer.wordpress.org/apis/making-http-requests/posting-data-to-an-external-service/)


