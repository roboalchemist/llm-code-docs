# Source: https://docs.apify.com/academy/tools/postman.md

# Postman

**Learn about Postman, a valuable tool for testing requests and proxies when building scalable web scrapers.**

***

https://www.postman.com/ is a powerful collaboration platform for API development and testing. For scraping use-cases, it's mainly used to test requests and proxies (such as checking the response body of a raw request, without loading any additional resources such as JavaScript or CSS). This tool can do much more than that, but we will not be discussing all of its capabilities here. Postman allows us to test requests with cookies, headers, and payloads so that we can be entirely sure what the response looks like for a request URL we plan to eventually use in a scraper.

The desktop app can be downloaded from its https://www.postman.com/downloads/, or the web app can be used with a signup - no download required. If this is your first time working with a tool like Postman, we recommend checking out their https://learning.postman.com/docs/introduction/overview/.

## Understanding the interface

![A basic outline of Postman\&#39;s interface](/assets/images/postman-interface-d0cd1626d8425c1081db491b5625ea06.png)

Following four sections are essential to get familiar with Postman:

### Tabs

Multiple test endpoints/requests can be opened at one time, each of which will be held within its own tab.

### Address bar

The section in which you select the type of request to send, the URL of the request, and of course, send the request with the **Send Request** button.

### Request options

This is a very useful section where you can view and edit structured query parameters, as well as specify any authorization parameters, headers, or payloads.

### Response

After sending a request, the response's body will be found here, along with its cookies and headers. The response body can be viewed in various formats - **Pretty-Print**, **Raw**, or **Preview**.

## Using and testing proxies

In order to use a proxy, the proxy's server and configuration must be provided in the **Proxy** tab in Postman settings.

![Proxy configuration in Postman settings](/assets/images/postman-proxy-d3a16a565dd112c68a1517a861e7fe00.png)

After configuring a proxy, the next request sent will attempt to use it. To switch off the proxy, its details don't need to be deleted. The **Add a custom proxy configuration** option in settings needs to be un-ticked to disable it.

## Managing the cookies cache

Postman keeps a cache of the cookies from all previous responses of a certain domain, which can be a blessing, but also a curse. Sometimes, you might notice that a request is going through just fine with Postman, but that your scraper is being blocked.

More often than not in these cases, the reason is because the endpoint being reached requires a valid `cookie` header to be present when sending the request, and because of Postman's cache, it is sending a valid cookie within each request's headers, while your scraper is not. Another reason this may happen is because you are sending Postman requests without a proxy (using your local IP address), while your scraper is using a proxy that could potentially be getting blocked.

In order to check whether there are any cookies associated with a certain request are cached in Postman, click on the **Cookies** button in any opened request tab:

![Button to view the cached cookies](/assets/images/postman-cookies-button-25f42087846a7a0d29fdf088eeff5756.png)

Clicking on this button opens a **MANAGE COOKIES** window, where a list of all cached cookies per domain can be seen. If we had been previously sending multiple requests to **https://github.com/apify**, within this window we would be able to find cached cookies associated with github.com. Cookies can also be edited (to update some specific values), or deleted (to send a "clean" request without any cached data) here.

![Managing cookies in Postman with the \&quot;MANAGE COOKIES\&quot; window](/assets/images/postman-manage-cookies-5f057bee3fff880af0026b1caf8ecdf5.png)

### Some alternatives to Postman

* https://hoppscotch.io/
* https://docs.apify.com/academy/tools/insomnia.md
* https://testfully.io/
