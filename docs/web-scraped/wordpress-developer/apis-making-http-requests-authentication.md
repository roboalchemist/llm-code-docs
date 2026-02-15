# Authentication

**Source:** [https://developer.wordpress.org/apis/making-http-requests/authentication/](https://developer.wordpress.org/apis/making-http-requests/authentication/)






↑Back to top



Many APIs will require you to make authenticated requests to access some endpoints. A common authentication method is called HTTP Basic Authentication. It can be used in WordPress using the ‘Authorization’ headerwp_remote_get().


```
$args = array(
    'headers' => array(
        'Authorization' => 'Basic ' . base64_encode( YOUR_USERNAME . ':' . YOUR_PASSWORD )
    )
);
wp_remote_get( $url, $args );
```


HTTP Basic Auth is very insecure because it exposes the username and password and is only used for testing and development. Check the documentation of the API you want to access for more information on how to authenticate.


If you want to make authenticated requests to the WordPress REST API, checkthis article.





First published


July 13, 2020


Last updated


November 17, 2022



[PreviousAdvancedPrevious: Advanced](https://developer.wordpress.org/apis/making-http-requests/advanced/)
[NextQuicktagsNext: Quicktags](https://developer.wordpress.org/apis/quicktags/)


