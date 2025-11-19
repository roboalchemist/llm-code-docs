# Source: https://docs.apify.com/academy/tools/insomnia.md

# Insomnia

**Learn about Insomnia, a valuable tool for testing requests and proxies when building scalable web scrapers.**

***

Despite its name, the https://insomnia.rest/download desktop application has absolutely nothing to do with having a lack of sleep. Rather, it is a tool to build and test APIs. If you've already read about https://docs.apify.com/academy/tools/postman.md, you already know what Insomnia can be used for, as they both practically do the same exact things. While Insomnia shares similarities with Postman, such as the ability to send requests with specific headers, cookies, and payloads, it has a few notable differences. One key difference is Insomnia's feature to display the entire request timeline.

Insomnia can be downloaded from its https://insomnia.rest/download, and its features can be read about in the https://docs.insomnia.rest/.

## The Insomnia interface

After opening the app, you'll first need to create a new request. After creating the request, you'll see an interface that looks like this:

![Insomnia interface](/assets/images/insomnia-interface-8db85779b777d023aee844fcd478b402.jpg)

Let's break down the main sections:

### List of requests

You can configure multiple requests with a custom payload, headers, cookies, parameters, etc. They are automatically saved in the list of requests until deleted.

### Address bar

The place where you select the type of request to send (**GET**, **POST**, **PUT**, **DELETE**, etc.), specify the URI of the request and send the request with the **Send** button.

### Request options

Here, you can add a request payload, specify authorization parameters, add query parameters, and attach headers to the request.

### Response

Where the response body is displayed after the request has been sent. Like in Postman, the request can be viewed in preview mode, pretty-printed, or in its raw form. This section also has the **Headers** and **Cookies** tabs, which respectively show the request headers and cookies.

## Request timeline

The one feature of Insomnia that separates it from Postman is the **Timeline**.

![Request timeline](/assets/images/insomnia-timeline-9700132bcd3fc1ca8145b5ea9a1eb062.jpg)

This feature allows you to see information about the request that is not present in the response body.

## Using proxies in Insomnia

In order to use a proxy, you need to specify the proxy's parameters in Insomnia's preferences. In preferences, scroll down to the **HTTP Network Proxy** section under the **General** tab and specify the full proxy URL there:

![Configuring a proxy](/assets/images/insomnia-proxy-1cacb438369ed0cb8054b86acb5a716f.png)

## Managing the cookies cache

Insomnia keeps the cookies for the requests you have already sent before. This might result in you receiving a different response within your scraper from what you're receiving in Insomnia, as a necessary cookie is not present in the request sent by the scraper. To check whether or not some cookies associated with a certain request have been cached, click on the **Cookies** button at the top of the list of requests:

![Click on the \&quot;Cookies\&quot; button](/assets/images/insomnia-cookies-4cf492e7c0821caccb4cc924559a83f9.png)

This will bring up the **Manage cookies** window, where all cached cookies can be viewed, edited, or deleted.

![The \&quot;Manage Cookies\&quot; tab](/assets/images/insomnia-manage-cookies-115b3de173313e250cbe1eddfa3665b5.jpg)

## Postman or Insomnia

The application you choose to use is completely up to your personal preference, and will not affect your development workflow. If viewing timelines of the requests you send is important to you, then you should go with Insomnia; however, if that doesn't matter, choose the one that has the most intuitive interface for you.
