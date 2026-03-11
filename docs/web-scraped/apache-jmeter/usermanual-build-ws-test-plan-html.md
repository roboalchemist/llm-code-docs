# Source: https://jmeter.apache.org/usermanual/build-ws-test-plan.html

Title: Building a SOAP WebService Test Plan

URL Source: https://jmeter.apache.org/usermanual/build-ws-test-plan.html

Published Time: Sun, 07 Jan 2024 17:19:24 GMT

Markdown Content:
Apache JMeter - User's Manual: Building a SOAP WebService Test Plan
===============
[Main content](https://jmeter.apache.org/usermanual/build-ws-test-plan.html#content)

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

*   [< Prev](https://jmeter.apache.org/usermanual/build-ldapext-test-plan.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/build-jms-point-to-point-test-plan.html)

9. Building a WebService Test Plan[¶](https://jmeter.apache.org/usermanual/build-ws-test-plan.html#building "Link to here")
===========================================================================================================================

In this section, you will learn how to create a [Test Plan](https://jmeter.apache.org/usermanual/build-test-plan.html) to test a WebService. You will create five users that send requests to One page. Also, you will tell the users to run their tests twice. So, the total number of requests is (5 users) x (1 requests) x (repeat 2 times) = 10 HTTP requests. To construct the Test Plan, you will use the following elements: [Thread Group](https://jmeter.apache.org/usermanual/test_plan.html#thread_group), [HTTP Request](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request), and [Aggregate Graph](https://jmeter.apache.org/usermanual/component_reference.html#Aggregate_Graph).

If the sampler appears to be getting an error from the webservice, double check the SOAP message and make sure the format is correct. In particular, make sure the xmlns attributes are exactly the same as the WSDL. If the xml namespace is different, the webservice will likely return an error.

9.1 Creating WebService Test Plan[¶](https://jmeter.apache.org/usermanual/build-ws-test-plan.html#soap_webservice_template "Link to here")
==========================================================================================================================================

In our Test Plan, we will use a .NET webservice. We won't go into the details of writing a webservice. If you don't know how to write a webservice, google for webservice and familiarize yourself with writing webservices for Java and .NET. It should be noted there is a significant difference between how .NET and Java implement webservices. The topic is too broad to cover in the user manual. Please refer to other sources to get a better idea of the differences.

JMeter sends requests in the order that they appear in the tree.

Start by using menu File→Templates… and select template "Building a SOAP Webservice Test Plan". Then, click "Create" button.

[![Image 4: Figure 9.1.0. Webservice Template](https://jmeter.apache.org/images/screenshots/ws_template.png)](https://jmeter.apache.org/images/screenshots/ws_template.png)

 Figure 9.1.0. Webservice Template

 Change the following: 
1.    In "HTTP Request Defaults" change "Server Name of IP" 
2.    In "Soap Request", change "Path:" [![Image 5: Figure 9.1.3 Webservice Body](https://jmeter.apache.org/images/screenshots/ws_http_request.png)](https://jmeter.apache.org/images/screenshots/ws_http_request.png)

Figure 9.1.1 Webservice Path

Next, select "HTTP Header Manager" and update "SOAPAction" header to match your webservice. Some webservices may not use SOAPAction in this case remove it. 

 Currently, only .NET uses SOAPAction, so it is normal to have a blank SOAPAction for all other webservices. The list includes JWSDP, Weblogic, Axis, The Mind Electric Glue, and gSoap.

[![Image 6: Figure 9.1.2 Webservice Headers](https://jmeter.apache.org/images/screenshots/ws_header.png)](https://jmeter.apache.org/images/screenshots/ws_header.png)

Figure 9.1.2 Webservice Headers

The last step is to paste the SOAP message in the "Body Data" text area.

[![Image 7: Figure 9.1.3 Webservice Body](https://jmeter.apache.org/images/screenshots/ws_http_request.png)](https://jmeter.apache.org/images/screenshots/ws_http_request.png)

Figure 9.1.3 Webservice Body

9.2 Adding Users[¶](https://jmeter.apache.org/usermanual/build-ws-test-plan.html#adding_users "Link to here")
=============================================================================================================

The [Thread Group](https://jmeter.apache.org/usermanual/test_plan.html#thread_group) tells JMeter the number of users you want to simulate, how often the users should send requests, and the how many requests they should send.

Select the Thread Group element in the tree, if you have not already selected it. You should now see the Thread Group Control Panel in the right section of the JMeter window (see Figure 9.2 below)

[![Image 8: Figure 9.2. Thread Group with Default Values](https://jmeter.apache.org/images/screenshots/webtest/threadgroup.png)](https://jmeter.apache.org/images/screenshots/webtest/threadgroup.png)

 Figure 9.2. Thread Group with Default Values

Start by providing a more descriptive name for our Thread Group. In the name field, enter JMeter Users.

Next, increase the number of users (called threads) to 10.

In the next field, the Ramp-Up Period, leave the default value of 0 seconds. This property tells JMeter how long to delay between starting each user. For example, if you enter a Ramp-Up Period of 5 seconds, JMeter will finish starting all of your users by the end of the 5 seconds. So, if we have 5 users and a 5 second Ramp-Up Period, then the delay between starting users would be 1 second (5 users / 5 seconds = 1 user per second). If you set the value to 0, then JMeter will immediately start all of your users.

Finally, clear the checkbox labeled "Forever", and enter a value of 2 in the Loop Count field. This property tells JMeter how many times to repeat your test. If you enter a loop count value of 0, then JMeter will run your test only once. To have JMeter repeatedly run your Test Plan, select the Forever checkbox.

In most applications, you have to manually accept changes you make in a Control Panel. However, in JMeter, the Control Panel automatically accepts your changes as you make them. If you change the name of an element, the tree will be updated with the new text after you leave the Control Panel (for example, when selecting another tree element).

See Figure 9.2 for the completed JMeter Users Thread Group.

[![Image 9: Figure 9.3. JMeter Users Thread Group](https://jmeter.apache.org/images/screenshots/webtest/threadgroup2.png)](https://jmeter.apache.org/images/screenshots/webtest/threadgroup2.png)

 Figure 9.3. JMeter Users Thread Group

9.3 Adding a Listener to View Store the Test Results[¶](https://jmeter.apache.org/usermanual/build-ws-test-plan.html#adding_listener "Link to here")
====================================================================================================================================================

The final element you need to add to your Test Plan is a [Listener](https://jmeter.apache.org/usermanual/component_reference.html#listeners). This element is responsible for storing all of the results of your HTTP requests in a file and presenting a visual model of the data.

Select the JMeter Users element and add a [Aggregate Graph](https://jmeter.apache.org/usermanual/component_reference.html#Aggregate_Graph) listener (Add→Listener→Aggregate Graph). Next, you need to specify a directory and filename of the output file. You can either type it into the filename field, or select the Browse button and browse to a directory and then enter a filename.

[![Image 10: Figure 9.4. Graph Results Listener](https://jmeter.apache.org/images/screenshots/ws_listener.png)](https://jmeter.apache.org/images/screenshots/ws_listener.png)

 Figure 9.4. Graph Results Listener

9.4 Rest Webservice[¶](https://jmeter.apache.org/usermanual/build-ws-test-plan.html#rest_webservice "Link to here")
===================================================================================================================

Testing a REST Webservice is very similar as you only need to modify in HTTP Request

*   Method: to select the one you want to test 
*   Body Data: which can be JSON, XML or any custom text 

 You may also need to modify "HTTP Header Manager" to select the correct "Content-Type" 

*   [< Prev](https://jmeter.apache.org/usermanual/build-ldapext-test-plan.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/build-jms-point-to-point-test-plan.html)

 Share this page: 
*   [share](https://jmeter.apache.org/usermanual/build-ws-test-plan.html "Share on facebook")
*   [tweet](https://jmeter.apache.org/usermanual/build-ws-test-plan.html "Tweet on twitter")

[Go to top](https://jmeter.apache.org/usermanual/build-ws-test-plan.html#top)

 Copyright © 1999 – 2024 , Apache Software Foundation 

Apache, Apache JMeter, JMeter, the Apache feather, and the Apache JMeter logo are trademarks of the Apache Software Foundation.
