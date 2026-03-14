# Source: https://jmeter.apache.org/usermanual/build-web-test-plan.html

Title: Building a Web Test Plan

URL Source: https://jmeter.apache.org/usermanual/build-web-test-plan.html

Published Time: Sun, 07 Jan 2024 17:19:24 GMT

Markdown Content:
Apache JMeter - User's Manual: Building a Web Test Plan
===============
[Main content](https://jmeter.apache.org/usermanual/build-web-test-plan.html#content)

[![Image 1: Logo ASF](https://jmeter.apache.org/images/asf-logo.svg)](https://www.apache.org/)

[![Image 2: Apache JMeter](https://jmeter.apache.org/images/logo.svg)](https://jmeter.apache.org/)

[![Image 3: Current Apache event teaser](https://www.apache.org/events/current-event-234x60.png)](https://www.apache.org/events/current-event.html)

*   About 
    *   [Overview](https://jmeter.apache.org/index.html)
    *   [License](https://www.apache.org/licenses/)

*   Download 
    *   [Download Releases](https://jmeter.apache.org/download_jmeter.cgi)
    *   [Release Notes](https://jmeter.apache.org/changes.html)

*   Documentation 
    *   [Get Started](https://jmeter.apache.org/usermanual/get-started.html)
    *   [User Manual](https://jmeter.apache.org/usermanual/index.html)
    *   [Best Practices](https://jmeter.apache.org/usermanual/best-practices.html)
    *   [Component Reference](https://jmeter.apache.org/usermanual/component_reference.html)
    *   [Functions Reference](https://jmeter.apache.org/usermanual/functions.html)
    *   [Properties Reference](https://jmeter.apache.org/usermanual/properties_reference.html)
    *   [Change History](https://jmeter.apache.org/changes_history.html)
    *   [Javadocs](https://jmeter.apache.org/api/index.html)
    *   [JMeter Wiki](https://cwiki.apache.org/confluence/display/JMETER/Home)
    *   [FAQ (Wiki)](https://cwiki.apache.org/confluence/display/JMETER/JMeterFAQ)

*   Tutorials 
    *   [Distributed Testing](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html)
    *   [Recording Tests](https://jmeter.apache.org/usermanual/jmeter_proxy_step_by_step.html)
    *   [JUnit Sampler](https://jmeter.apache.org/usermanual/junitsampler_tutorial.html)
    *   [Access Log Sampler](https://jmeter.apache.org/usermanual/jmeter_accesslog_sampler_step_by_step.html)
    *   [Extending JMeter](https://jmeter.apache.org/usermanual/jmeter_tutorial.html)

*   Community 
    *   [Issue Tracking](https://jmeter.apache.org/issues.html)
    *   [Security](https://jmeter.apache.org/security.html)
    *   [Mailing Lists](https://jmeter.apache.org/mail.html)
    *   [Source Repositories](https://jmeter.apache.org/svnindex.html)
    *   [Building and Contributing](https://jmeter.apache.org/building.html)
    *   [Project info at Apache](https://projects.apache.org/project.html?jmeter)
    *   [Contributors](https://cwiki.apache.org/confluence/display/JMETER/JMeterCommitters)

*   Foundation 
    *   [The Apache Software Foundation (ASF)](https://www.apache.org/)
    *   [Get Involved in the ASF](https://www.apache.org/foundation/getinvolved.html)
    *   [Privacy Policy](https://privacy.apache.org/policies/privacy-policy-public.html)
    *   [Sponsorship](https://www.apache.org/foundation/sponsorship.html)
    *   [Thanks](https://www.apache.org/foundation/thanks.html)

*   [Twitter](https://twitter.com/ApacheJMeter "Follow us on Twitter")
*   [github](https://github.com/apache/jmeter "Fork us on github")

*   [< Prev](https://jmeter.apache.org/usermanual/test_plan.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/build-adv-web-test-plan.html)

4. Building a Web Test Plan[¶](https://jmeter.apache.org/usermanual/build-web-test-plan.html#building "Link to here")
=====================================================================================================================

In this section, you will learn how to create a basic [Test Plan](https://jmeter.apache.org/usermanual/build-test-plan.html) to test a Web site. You will create five users that send requests to two pages on the JMeter Web site. Also, you will tell the users to run their tests twice. So, the total number of requests is (5 users) x (2 requests) x (repeat 2 times) = 20 HTTP requests. To construct the Test Plan, you will use the following elements: [Thread Group](https://jmeter.apache.org/usermanual/test_plan.html#thread_group), [HTTP Request](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request), [HTTP Request Defaults](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request_Defaults), and [Graph Results](https://jmeter.apache.org/usermanual/component_reference.html#Graph_Results).

For a more advanced Test Plan, see [Building an Advanced Web Test Plan](https://jmeter.apache.org/usermanual/build-adv-web-test-plan.html).

4.1 Adding Users[¶](https://jmeter.apache.org/usermanual/build-web-test-plan.html#adding_users "Link to here")
==============================================================================================================

The first step you want to do with every JMeter Test Plan is to add a [Thread Group](https://jmeter.apache.org/usermanual/test_plan.html#thread_group) element. The Thread Group tells JMeter the number of users you want to simulate, how often the users should send requests, and how many requests they should send.

Go ahead and add the ThreadGroup element by first selecting the Test Plan, clicking your right mouse button to get the Add menu, and then select Add → ThreadGroup.

You should now see the Thread Group element under Test Plan. If you do not see the element, then "expand" the Test Plan tree by clicking on the Test Plan element.

Next, you need to modify the default properties. Select the Thread Group element in the tree, if you have not already selected it. You should now see the Thread Group Control Panel in the right section of the JMeter window (see Figure 4.1 below)

[![Image 4: Figure 4.1. Thread Group with Default Values](https://jmeter.apache.org/images/screenshots/webtest/threadgroup.png)](https://jmeter.apache.org/images/screenshots/webtest/threadgroup.png)

 Figure 4.1. Thread Group with Default Values

Start by providing a more descriptive name for our Thread Group. In the name field, enter JMeter Users.

Next, increase the number of users (called threads) to 5.

In the next field, the Ramp-Up Period, leave the default value of 1 seconds. This property tells JMeter how long to delay between starting each user. For example, if you enter a Ramp-Up Period of 5 seconds, JMeter will finish starting all of your users by the end of the 5 seconds. So, if we have 5 users and a 5 second Ramp-Up Period, then the delay between starting users would be 1 second (5 users / 5 seconds = 1 user per second). If you set the value to 0, then JMeter will immediately start all of your users.

Finally enter a value of 2 in the Loop Count field. This property tells JMeter how many times to repeat your test. If you enter a loop count value of 1, then JMeter will run your test only once. To have JMeter repeatedly run your Test Plan, select the Forever checkbox.

In most applications, you have to manually accept changes you make in a Control Panel. However, in JMeter, the Control Panel automatically accepts your changes as you make them. If you change the name of an element, the tree will be updated with the new text after you leave the Control Panel (for example, when selecting another tree element).

See Figure 4.2 for the completed JMeter Users Thread Group.

[![Image 5: Figure 4.2. JMeter Users Thread Group](https://jmeter.apache.org/images/screenshots/webtest/threadgroup2.png)](https://jmeter.apache.org/images/screenshots/webtest/threadgroup2.png)

 Figure 4.2. JMeter Users Thread Group

4.2 Adding Default HTTP Request Properties[¶](https://jmeter.apache.org/usermanual/build-web-test-plan.html#adding_defaults "Link to here")
===========================================================================================================================================

Now that we have defined our users, it is time to define the tasks that they will be performing. In this section, you will specify the default settings for your HTTP requests. And then, in section 4.3, you will add HTTP Request elements which use some of the default settings you specified here.

Begin by selecting the JMeter Users (Thread Group) element. Click your right mouse button to get the Add menu, and then select Add → Config Element → HTTP Request Defaults. Then select this new element to view its Control Panel (see Figure 4.3).

[![Image 6: Figure 4.3. HTTP Request Defaults](https://jmeter.apache.org/images/screenshots/webtest/http-defaults1.png)](https://jmeter.apache.org/images/screenshots/webtest/http-defaults1.png)

 Figure 4.3. HTTP Request Defaults

Like most JMeter elements, the [HTTP Request Defaults](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request_Defaults) Control Panel has a name field that you can modify. In this example, leave this field with the default value.

Skip to the next field, which is the Web Server's Server Name/IP. For the Test Plan that you are building, all HTTP requests will be sent to the same Web server, jmeter.apache.org. Enter this domain name into the field. This is the only field that we will specify a default, so leave the remaining fields with their default values.

The HTTP Request Defaults element does not tell JMeter to send an HTTP request. It simply defines the default values that the HTTP Request elements use.

See Figure 4.4 for the completed HTTP Request Defaults element

[![Image 7: Figure 4.4. HTTP Defaults for our Test Plan](https://jmeter.apache.org/images/screenshots/webtest/http-defaults2.png)](https://jmeter.apache.org/images/screenshots/webtest/http-defaults2.png)

 Figure 4.4. HTTP Defaults for our Test Plan

4.3 Adding Cookie Support[¶](https://jmeter.apache.org/usermanual/build-web-test-plan.html#adding_cookie_support "Link to here")
================================================================================================================================

Nearly all web testing should use cookie support, unless your application specifically doesn't use cookies. To add cookie support, simply add an [HTTP Cookie Manager](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Cookie_Manager) to each [Thread Group](https://jmeter.apache.org/usermanual/test_plan.html#thread_group) in your test plan. This will ensure that each thread gets its own cookies, but shared across all [HTTP Request](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request) objects.

[![Image 8: Figure 4.5. HTTP Cookie Manager](https://jmeter.apache.org/images/screenshots/webtest/http-cookie-manager.png)](https://jmeter.apache.org/images/screenshots/webtest/http-cookie-manager.png)

 Figure 4.5. HTTP Cookie Manager

To add the [HTTP Cookie Manager](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Cookie_Manager), simply select the [Thread Group](https://jmeter.apache.org/usermanual/test_plan.html#thread_group), and choose Add → Config Element → HTTP Cookie Manager, either from the Edit Menu, or from the right-click pop-up menu.

4.4 Adding HTTP Requests[¶](https://jmeter.apache.org/usermanual/build-web-test-plan.html#adding_requests "Link to here")
=========================================================================================================================

In our Test Plan, we need to make two HTTP requests. The first one is for the JMeter home page (http://jmeter.apache.org/), and the second one is for the Changes page (http://jmeter.apache.org/changes.html).

JMeter sends requests in the order that they appear in the tree.

Start by adding the first [HTTP Request](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request) to the JMeter Users element (Add → Sampler → HTTP Request). Then, select the HTTP Request element in the tree and edit the following properties (see Figure 4.6):

1.   Change the Name field to "Home Page".
2.   Set the Path field to "/". Remember that you do not have to set the Server Name field because you already specified this value in the HTTP Request Defaults element.

[![Image 9: Figure 4.6. HTTP Request for JMeter Home Page](https://jmeter.apache.org/images/screenshots/webtest/http-request1.png)](https://jmeter.apache.org/images/screenshots/webtest/http-request1.png)

 Figure 4.6. HTTP Request for JMeter Home Page

Next, add the second HTTP Request and edit the following properties (see Figure 4.7:

1.   Change the Name field to "Changes".
2.   Set the Path field to "/changes.html".

[![Image 10: Figure 4.7. HTTP Request for JMeter Changes Page](https://jmeter.apache.org/images/screenshots/webtest/http-request2.png)](https://jmeter.apache.org/images/screenshots/webtest/http-request2.png)

 Figure 4.7. HTTP Request for JMeter Changes Page

4.5 Adding a Listener to View Store the Test Results[¶](https://jmeter.apache.org/usermanual/build-web-test-plan.html#adding_listener "Link to here")
=====================================================================================================================================================

The final element you need to add to your Test Plan is a [Listener](https://jmeter.apache.org/usermanual/component_reference.html#listeners). This element is responsible for storing all of the results of your HTTP requests in a file and presenting a visual model of the data.

Select the JMeter Users element and add a [Graph Results](https://jmeter.apache.org/usermanual/component_reference.html#Graph_Results) listener (Add → Listener → Backend Listener).

4.6 Logging in to a web-site[¶](https://jmeter.apache.org/usermanual/build-web-test-plan.html#logging_in "Link to here")
========================================================================================================================

It's not the case here, but some web-sites require you to login before permitting you to perform certain actions. In a web-browser, the login will be shown as a form for the user name and password, and a button to submit the form. The button generates a POST request, passing the values of the form items as parameters.

To do this in JMeter, add an HTTP Request, and set the method to POST. You'll need to know the names of the fields used by the form, and the target page. These can be found out by inspecting the code of the login page. [If this is difficult to do, you can use the [JMeter Proxy Recorder](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Proxy_Server) to record the login sequence.] Set the path to the target of the submit button. Click the Add button twice and enter the username and password details. Sometimes the login form contains additional hidden fields. These will need to be added as well.

[![Image 11: Figure 4.8. Sample HTTP login request](https://jmeter.apache.org/images/screenshots/webtest/http_login.png)](https://jmeter.apache.org/images/screenshots/webtest/http_login.png)

 Figure 4.8. Sample HTTP login request

4.7 choose the same user or different users[¶](https://jmeter.apache.org/usermanual/build-web-test-plan.html#choose_users "Link to here")
=========================================================================================================================================

When creating a Test Plan, on each Thread Group iteration, we can choose to simulate the same user running multiple iterations, or different users running one iteration. You can configure this behaviour on Thread Group element, and have HTTP Cache Manager, HTTP Cookie Manager, HTTP Authorization Manager controlled by this setting.

[![Image 12: Figure 4.9. Choose the same user or different users](https://jmeter.apache.org/images/screenshots/webtest/threadgroup3.png)](https://jmeter.apache.org/images/screenshots/webtest/threadgroup3.png)

 Figure 4.9. Choose the same user or different users

You can choose to clear the cookies/cache content/authorization in the CookieManager/CacheManager/Authorization Manager, or choose to be controlled by the Thread Group.

[![Image 13: Figure 4.10. Use Thread Group to control CookieManager](https://jmeter.apache.org/images/screenshots/webtest/threadgroup4.png)](https://jmeter.apache.org/images/screenshots/webtest/threadgroup4.png)

 Figure 4.10. Use Thread Group to control CookieManager

[![Image 14: Figure 4.11. Use Thread Group to control CacheManager](https://jmeter.apache.org/images/screenshots/webtest/threadgroup5.png)](https://jmeter.apache.org/images/screenshots/webtest/threadgroup5.png)

 Figure 4.11. Use Thread Group to control CacheManager

[![Image 15: Figure 4.12. Use Thread Group to control Authorization Manager](https://jmeter.apache.org/images/screenshots/webtest/threadgroup6.png)](https://jmeter.apache.org/images/screenshots/webtest/threadgroup6.png)

 Figure 4.12. Use Thread Group to control Authorization Manager

*   [< Prev](https://jmeter.apache.org/usermanual/test_plan.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/build-adv-web-test-plan.html)

 Share this page: 
*   [share](https://jmeter.apache.org/usermanual/build-web-test-plan.html "Share on facebook")
*   [tweet](https://jmeter.apache.org/usermanual/build-web-test-plan.html "Tweet on twitter")

[Go to top](https://jmeter.apache.org/usermanual/build-web-test-plan.html#top)

 Copyright © 1999 – 2024 , Apache Software Foundation 

Apache, Apache JMeter, JMeter, the Apache feather, and the Apache JMeter logo are trademarks of the Apache Software Foundation.
