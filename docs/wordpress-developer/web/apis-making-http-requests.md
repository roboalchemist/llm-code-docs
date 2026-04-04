# Making HTTP requests

**Source:** [https://developer.wordpress.org/apis/making-http-requests/](https://developer.wordpress.org/apis/making-http-requests/)






↑Back to top



Very often we need to make HTTP requests from our theme or plugin, for example when we need to fetch data from an external API. Luckily WordPress has many helper functions to help you do that.


In this section, you will learn how to properly make HTTP requests and handle their responses.


Here’s an example of what you’re going to see


```
$response = wp_remote_get( 'https://api.github.com/users/wordpress' );
$body     = wp_remote_retrieve_body( $response );
```


In the next articles you’ll see a detailed explanation on how to make the requests:


- GETting data from an external service
- POSTing data to an external service
- Performance
- Advanced
- Authentication


If you’re just looking for the available helper functions, here they are:


The functions below are the ones you will use to retrieve a URL.


- wp_remote_get(): Retrieves a URL using the GET HTTP method.
- wp_remote_post(): Retrieves a URL using the POST HTTP method.
- wp_remote_head(): Retrieves a URL using the HEAD HTTP method.
- wp_remote_request(): Retrieves a URL using either the default GET or a custom HTTP method that you specify.


The other helper functions deal with retrieving different parts of the response. These make usage of the API very simple and are the preferred method for processing response objects.


- wp_remote_retrieve_body()– Retrieves just the body from the response.
- wp_remote_retrieve_header()– Retrieve a single header by name from the raw response.
- wp_remote_retrieve_headers()– Retrieve only the headers from the raw response.
- wp_remote_retrieve_response_code()– Retrieve the response code for the HTTP response. This should be 200, but could be 4xx or even 3xx on failure.
- wp_remote_retrieve_response_message()– Retrieve only the response message from the raw response.





First published


July 13, 2020


Last updated


November 21, 2022



[PreviousPluginsPrevious: Plugins](https://developer.wordpress.org/apis/plugins/)
[NextGETting data from an external serviceNext: GETting data from an external service](https://developer.wordpress.org/apis/making-http-requests/getting-data-from-an-external-service/)


