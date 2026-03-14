# Source: https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html

Title: Apache JMeter - Apache JMeter Distributed Testing Step-by-step

URL Source: https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html

Published Time: Sun, 07 Jan 2024 17:19:24 GMT

Markdown Content:
Apache JMeter - Apache JMeter Distributed Testing Step-by-step
===============
[Main content](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html#content)

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

*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/jmeter_proxy_step_by_step.html)

25. Apache JMeter Distributed Testing Step-by-step[¶](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html#distributed-testing "Link to here")
===========================================================================================================================================================================

This short tutorial explains how to use multiple systems to perform stress testing. Before we start, there are a couple of things to check.

*   the firewalls on the systems are turned off or correct ports are opened.
*   all the clients are on the same subnet.
*    the server is in the same subnet, if 192.x.x.x or 10.x.x.x IP addresses are used. If the server doesn't use 192.xx or 10.xx IP address, there shouldn't be any problems. 
*   Make sure JMeter can access the server.
*   Make sure you use the same version of JMeter and Java on all the systems. Mixing versions will not work correctly.
*    You have [setup SSL for RMI](https://jmeter.apache.org/usermanual/remote-test.html#setup_ssl) or disabled it. 

Once you've made sure the systems are ready, it's time to setup remote testing. The tutorial assumes you already have JMeter installed on all the systems. The way JMeter works is one controller node initiates the test on multiple worker nodes.

In this tutorial we use GUI Mode just for demonstration. In real life you should use CLI mode (NON GUI) to start your load test

[![Image 4: One controller node with multiple worker nodes](https://jmeter.apache.org/images/screenshots/distributed-jmeter.svg)](https://jmeter.apache.org/images/screenshots/distributed-jmeter.svg)

One controller node with multiple worker nodes

25.1 Terminology[¶](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html#terminology "Link to here")
---------------------------------------------------------------------------------------------------------------------------------

Before we dive into the step-by-step instructions, it's a good idea to define the terms and make sure the definition is clear.

Controller Node the system running JMeter GUI, which controls the test Worker Node the system running jmeter-server, which takes commands from the GUI and send requests to the target system(s) Target the webserver we plan to stress test[![Image 5: Categories of systems](https://jmeter.apache.org/images/screenshots/distributed-names.svg)](https://jmeter.apache.org/images/screenshots/distributed-names.svg)

Categories of systems

25.2 Step-by-Step[¶](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html#step-by-step "Link to here")
-----------------------------------------------------------------------------------------------------------------------------------

1.    On the worker nodes, go to jmeter/bin directory and execute jmeter-server.bat (jmeter-server on unix). 
2.    On controller node acting as the console, open windows explorer and go to jmeter/bin directory 
3.    Open jmeter.properties in a text editor 
4.    Edit the line remote_hosts=127.0.0.1
5.    Add the IP address. For example, if I have JMeter server running on 192.168.0.10, …, 192.168.0.15, the entry would look like this: remote_hosts=192.168.0.10,192.168.0.11,192.168.0.12,192.168.0.13,192.168.0.14
6.   Start JMeter.
7.   Open the test plan you want to use

[![Image 6: Simple test plan](https://jmeter.apache.org/images/screenshots/example-simple-plan.png)](https://jmeter.apache.org/images/screenshots/example-simple-plan.png)

Simple test plan

25.2 Starting the Test[¶](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html#starting "Link to here")
------------------------------------------------------------------------------------------------------------------------------------

At this point, you are ready to start load testing. If you want to double check the worker nodes are working, open jmeter.log in your editor. You should see the following in the log.

Writing log file to: /XXXX/XXXXX/bin/jmeter-server.log
Created remote object: UnicastServerRef [liveRef: [endpoint:[192.X.X.X:XXXXX](local),objID:[-6a665beb:15a2c8b9419:-7fff, 3180474504933847586]]]

If you do not see this message, it means jmeter-server did not start correctly. For tips on debugging the issue, [go to the tips section](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html#tips). There are two ways to initiate the test: a single system and all systems.

25.3 Start a single clients[¶](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html#start-single-client "Link to here")
----------------------------------------------------------------------------------------------------------------------------------------------------

1.   Click Run at the top
2.   Select Remote Start
3.   Select the IP address

[![Image 7: Start a single worker node](https://jmeter.apache.org/images/screenshots/example-remote-start.png)](https://jmeter.apache.org/images/screenshots/example-remote-start.png)

Start a single worker node

25.4 Start all clients[¶](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html#start-all-clients "Link to here")
---------------------------------------------------------------------------------------------------------------------------------------------

1.   Click Run at the top
2.    Select Remote Start all or use Ctrl+Shift+R

[![Image 8: Start all worker nodes](https://jmeter.apache.org/images/screenshots/example-remote-start-all.png)](https://jmeter.apache.org/images/screenshots/example-remote-start-all.png)

Start all worker nodes

25.5 Limitations[¶](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html#limitations "Link to here")
---------------------------------------------------------------------------------------------------------------------------------

There are some basic limitations for distributed testing. Here's the list of the known items in no specific order.

1.   RMI cannot communicate across subnets without a proxy; therefore neither can JMeter without a proxy.
2.   Since version 2.9, JMeter sends all the test results stripping Response data to the controlling console, this allows us to reduce impact on network IO. Ensure you monitor your network traffic so that this traffic does not incur contention
3.   A single JMeter client running on a 2-3 GHz CPU (recent CPU) can handle 1000-2000 threads depending on the type of test.

25.6 Additional resources[¶](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html#additional-resources "Link to here")
---------------------------------------------------------------------------------------------------------------------------------------------------

[Wiki page on remote testing](https://cwiki.apache.org/confluence/display/JMETER/JMeterFAQ#JMeterFAQ-Howtodoremotetestingthe'properway'?)

[Remote Testing in the user manual](https://jmeter.apache.org/usermanual/remote-test.html)

25.7 Tips[¶](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html#tips "Link to here")
-------------------------------------------------------------------------------------------------------------------

In some cases, the firewall may still be blocking RMI traffic.

### Anti Virus and Firewall

Antivirus should be stopped during a Load Test as it can drastically impact timings leading to wrong results.

Firewall needs to be stopped from windows services or at least some ports need to be opened.

1.   Open control panel
2.   Open administrative tools
3.   Double click services
4.   Go to down to Symantec anti virus, right click and select stop

### Windows firewall

1.   Open network connections
2.   Select the network connection
3.   Right click and select properties
4.   Select advanced tab
5.   Uncheck internet connection firewall

### Linux

On Linux, iptables might be turned on by default. For instructions, please refer to the [Remote Testing in the user manual](https://jmeter.apache.org/usermanual/remote-test.html)

On RedHat (or derivatives), iptables is turned on by default. Execute

service iptables stop to stop the Linux firewall or ensure you open the correct ports. 

*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/jmeter_proxy_step_by_step.html)

 Share this page: 
*   [share](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html "Share on facebook")
*   [tweet](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html "Tweet on twitter")

[Go to top](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html#top)

 Copyright © 1999 – 2024 , Apache Software Foundation 

Apache, Apache JMeter, JMeter, the Apache feather, and the Apache JMeter logo are trademarks of the Apache Software Foundation.
