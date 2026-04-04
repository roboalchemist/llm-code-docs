# Source: https://jmeter.apache.org/usermanual/jmeter_accesslog_sampler_step_by_step.html

Title: Apache JMeter - Access log sampler Step-by-step

URL Source: https://jmeter.apache.org/usermanual/jmeter_accesslog_sampler_step_by_step.html

Published Time: Sun, 07 Jan 2024 17:19:24 GMT

Markdown Content:
Apache JMeter - Access log sampler Step-by-step
===============
[Main content](https://jmeter.apache.org/usermanual/jmeter_accesslog_sampler_step_by_step.html#content)

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

*   [< Prev](https://jmeter.apache.org/usermanual/junitsampler_tutorial.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/jmeter_tutorial.html)

28. Access log sampler Step-by-step[¶](https://jmeter.apache.org/usermanual/jmeter_accesslog_sampler_step_by_step.html#access-log-sampler "Link to here")
=========================================================================================================================================================

This is a short tutorial on JMeter's access log sampler. The purpose of the Access Log Sampler is to provide an easy way to simulate production traffic. There are several benefits to using access logs.

*   Rather than guess what users are doing, the test plan is using real traffic data
*   As the traffic pattern changes, the access log provides a record of individual changes and general shifts in usage
*   Access logs contain a lot of useful data, which may provide some insight
*   Access logs can be minded to determine different types of users
*   Access logs can capture detailed session information

The down side of using access logs for test plans is you have to configure the webserver to output the request information. This may not be appropriate where security is an issue. For example, if the webserver dumps the post data from each request to the access logs, users login and password would be stored in plain text. Here are some general cases where access logs might be inappropriate.

*   Security sensitive applications where the data is encrypted
*   The application does not allow fine grain control of which request parameters are written to the access logs
*   The application needs correlation between requests
*   The webserver cannot be configured to append the post data to the access log
*   The webserver is hosting multiple applications, but doesn't provide a way to log the requests of one application to a separate file

To take advantage of access logs, the first thing is the webserver needs to be configured to use extended log format. Links for configuring the popular containers are provided below.

*   [BEA Weblogic](http://e-docs.bea.com/wls/docs70/adminguide/web_server.html#113868)
*   [Tomcat](http://tomcat.apache.org/tomcat-8.5-doc/config/valve.html#Access_Log_Valve)
*   [Websphere](http://e-docs.bea.com/wls/docs61/adminguide/web_server.html#113868)
*   [Resin](http://www.caucho.com/resin-3.0/config/log.xtp#access-log)

In some cases, it may be desirable to write custom logging, so that sensitive information is not written to the access logs. This article does not cover the techniques for writing custom logging.

28.1 Step-by-Step[¶](https://jmeter.apache.org/usermanual/jmeter_accesslog_sampler_step_by_step.html#step-by-step "Link to here")
---------------------------------------------------------------------------------------------------------------------------------

1.   Start JMeter
2.    Select Test Plan
3.    Right click Add→Threads (Users)→Thread Group[![Image 4: Add Thread Group](https://jmeter.apache.org/images/screenshots/add-threadgroup.png)](https://jmeter.apache.org/images/screenshots/add-threadgroup.png)

Add Thread Group

4.    Select Thread Group
5.    Right click Add→Sampler→Access Log Sampler[![Image 5: Add Access Log Sampler](https://jmeter.apache.org/images/screenshots/add-access-log-sampler.png)](https://jmeter.apache.org/images/screenshots/add-access-log-sampler.png)

Add Access Log Sampler

6.    Right click on Thread Group Add→Listener→Aggregate Report[![Image 6: Add Aggregate Report](https://jmeter.apache.org/images/screenshots/add-aggregate-report.png)](https://jmeter.apache.org/images/screenshots/add-aggregate-report.png)

Add Aggregate Report

7.    Select the Access Log Sampler[![Image 7: Access Log Sampler](https://jmeter.apache.org/images/screenshots/accesslogsampler.png)](https://jmeter.apache.org/images/screenshots/accesslogsampler.png)

Access Log Sampler

8.    Enter the IP address or hostname in Server
9.    Enter the port in Port
10.    If you want to download the images, set Parse images to true. 
11.    Select a file for Log File Location[![Image 8: Filled in Access Log Sampler](https://jmeter.apache.org/images/screenshots/example-access-log-sampler.png)](https://jmeter.apache.org/images/screenshots/example-access-log-sampler.png)

Filled in Access Log Sampler

12.   Select Aggregate Report
13.    Enter results.jtl for filename [![Image 9: Aggregate Report with filename](https://jmeter.apache.org/images/screenshots/example-aggregate-report.png)](https://jmeter.apache.org/images/screenshots/example-aggregate-report.png)

Aggregate Report with filename

At this point, the test plan is ready. Start the test with Ctrl+R or from the menu Start→Run.

*   [< Prev](https://jmeter.apache.org/usermanual/junitsampler_tutorial.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/jmeter_tutorial.html)

 Share this page: 
*   [share](https://jmeter.apache.org/usermanual/jmeter_accesslog_sampler_step_by_step.html "Share on facebook")
*   [tweet](https://jmeter.apache.org/usermanual/jmeter_accesslog_sampler_step_by_step.html "Tweet on twitter")

[Go to top](https://jmeter.apache.org/usermanual/jmeter_accesslog_sampler_step_by_step.html#top)

 Copyright © 1999 – 2024 , Apache Software Foundation 

Apache, Apache JMeter, JMeter, the Apache feather, and the Apache JMeter logo are trademarks of the Apache Software Foundation.
