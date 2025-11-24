# Source: https://docs.apify.com/academy/tools/proxyman.md

# Proxyman

**Learn about Proxyman, a tool for viewing all network requests that are coming through your system. Filter by response type, by a keyword, or by application.**

***

Though the name sounds very similar to https://docs.apify.com/academy/tools/postman.md, https://proxyman.io/ is used for a different purpose. Rather than for manually sending and analyzing the responses of requests, Proxyman is a tool for macOS that allows you to view and analyze the HTTP/HTTPS requests that are going through your device. This is done by routing all of your requests through a proxy, which intercepts them and allows you to view data about them. Because it's just a proxy, the HTTP/HTTPS requests going through iOS devices, Android devices, and even iOS simulators can also be viewed with Proxyman.

If you've already gone through the https://docs.apify.com/academy/api-scraping/general-api-scraping/locating-and-learning.md in the **API scraping** section, you can think of Proxyman as an advanced Network Tab, where you can see requests that you sometimes can't see in regular browser DevTools.

## The basics

Though the application offers a whole lot of advanced features, there are only a few main features you'll be utilizing when using Proxyman for scraper development purposes. Let's open up Proxyman and take a look at some of the basic features:

### Apps

The **Apps** tab allows you to both view all of the applications on your machine which are sending requests, as well as filter requests based on application.

![Apps tab in Proxyman](/assets/images/proxyman-apps-tab-3653fe914c2d03b6f7091d22ee04f804.png)

### Results

Let's open up Safari and visit **apify.com**, then check back in Proxyman to see all of the requests Safari has made when visiting the website.

![Results in Proxyman](/assets/images/proxyman-results-86853f0d8dcbf9dd1d8c4e6ddf63aa6a.jpg)

We can see all of the requests related to us visiting **apify.com**. Then, by clicking a request, we can see a whole lot of information about it. The most important information for you, however, will usually be the request and response **headers** and **body**.

![View a request](/assets/images/proxyman-view-request-1244c56bbe015b469af10732e896e4cf.jpg)

### Filtering

Sometimes, there can be hundreds (or even thousands) of requests that appear in the list. Rather than spending your time rooting through all of them, you can use the plethora of filtering methods that Proxyman offers to find exactly what you are looking for.

![Filter requests with the filter options](/assets/images/proxyman-filter-b685c20107702e86a2e70fcdebc2eb2f.png)

## Alternatives

Since Proxyman is only available for macOS, it's only appropriate to list some alternatives to it that are accessible to our Windows and Linux friends:

* https://portswigger.net/burp
* https://www.charlesproxy.com/documentation/installation/
* https://www.telerik.com/fiddler
