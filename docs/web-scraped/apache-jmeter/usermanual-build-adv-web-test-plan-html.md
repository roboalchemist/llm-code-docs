# Source: https://jmeter.apache.org/usermanual/build-adv-web-test-plan.html

Title: User's Manual: Building an Advanced Web Test Plan

URL Source: https://jmeter.apache.org/usermanual/build-adv-web-test-plan.html

Markdown Content:
5.1 Handling User Sessions With URL Rewriting[¶](https://jmeter.apache.org/usermanual/build-adv-web-test-plan.html#session_url_rewriting "Link to here")
--------------------------------------------------------------------------------------------------------------------------------------------------------

If your web application uses URL rewriting rather than cookies to save session information, then you'll need to do a bit of extra work to test your site.

To respond correctly to URL rewriting, JMeter needs to parse the HTML received from the server and retrieve the unique session ID. Use the appropriate [HTTP URL Re-writing Modifier](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_URL_Re-writing_Modifier) to accomplish this. Simply enter the name of your session ID parameter into the modifier, and it will find it and add it to each request. If the request already has a value, it will be replaced. If "Cache Session Id?" is checked, then the last found session id will be saved, and will be used if the previous HTTP sample does not contain a session id.

URL Rewriting Example[¶](https://jmeter.apache.org/usermanual/build-adv-web-test-plan.html#url_rewriting_example "Link to here")

Download [this example](https://jmeter.apache.org/demos/URLRewritingExample.jmx). In Figure 1 is shown a test plan using URL rewriting. Note that the URL Re-writing modifier is added to the SimpleController, thus assuring that it will only affect requests under that SimpleController.

[![Image 1: Figure 1 - Test Tree](https://jmeter.apache.org/images/screenshots/url_rewrite_example_a.png)](https://jmeter.apache.org/images/screenshots/url_rewrite_example_a.png)

Figure 1 - Test Tree

In Figure 2, we see the URL Re-writing modifier GUI, which just has a field for the user to specify the name of the session ID parameter. There is also a checkbox for indicating that the session ID should be part of the path (separated by a ";"), rather than a request parameter

[![Image 2: Figure 2 - Request parameters](https://jmeter.apache.org/images/screenshots/url_rewrite_example_b.png)](https://jmeter.apache.org/images/screenshots/url_rewrite_example_b.png)

Figure 2 - Request parameters

The [HTTP Header Manager](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Header_Manager) lets you customize what information JMeter sends in the HTTP request header. This header includes properties like "User-Agent", "Pragma", "Referer", etc.

The [HTTP Header Manager](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Header_Manager), like the [HTTP Cookie Manager](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Cookie_Manager), should probably be added at the Thread Group level, unless for some reason you wish to specify different headers for the different [HTTP Request](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request) objects in your test.

[Go to top](https://jmeter.apache.org/usermanual/build-adv-web-test-plan.html#top)
