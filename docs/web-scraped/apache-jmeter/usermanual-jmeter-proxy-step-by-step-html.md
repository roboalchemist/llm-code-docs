# Source: https://jmeter.apache.org/usermanual/jmeter_proxy_step_by_step.html

Title: Apache JMeter - Apache JMeter HTTP(S) Test Script Recorder

URL Source: https://jmeter.apache.org/usermanual/jmeter_proxy_step_by_step.html

Published Time: Sun, 07 Jan 2024 17:19:24 GMT

Markdown Content:
Apache JMeter - Apache JMeter HTTP(S) Test Script Recorder
===============
[Main content](https://jmeter.apache.org/usermanual/jmeter_proxy_step_by_step.html#content)

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

*   [< Prev](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/junitsampler_tutorial.html)

26. Apache JMeter HTTP(S) Test Script Recorder[¶](https://jmeter.apache.org/usermanual/jmeter_proxy_step_by_step.html#script-recorder "Link to here")
=====================================================================================================================================================

This tutorial attempts to explain the exact steps for recording HTTP/HTTPS. For those new to JMeter, one easy way to create a test plan is to use the Recorder.

26.1 JMeter configuration[¶](https://jmeter.apache.org/usermanual/jmeter_proxy_step_by_step.html#configuration "Link to here")
------------------------------------------------------------------------------------------------------------------------------

Since JMeter 2.10, recording has been improved to better handle embedded resources and creation of certificates on the fly. To enable these features, JMeter uses keytool utility (available in JRE/JDK) so you need to ensure your configuration is correct, read [this wiki page before starting.](https://cwiki.apache.org/confluence/display/JMETER/TestRecording210)

26.2 Basic Instructions[¶](https://jmeter.apache.org/usermanual/jmeter_proxy_step_by_step.html#basic-instructions "Link to here")
---------------------------------------------------------------------------------------------------------------------------------

1.    Go to JMETER_HOME/bin and start JMeter with jmeterw.bat on Windows and jmeter.sh  on Linux/Unix 
2.    Select Templates… on the menu bar 
[![Image 4](https://jmeter.apache.org/images/screenshots/Select-Templates-Icon.png)](https://jmeter.apache.org/images/screenshots/Select-Templates-Icon.png)

3.    Select Recording template on the list 
[![Image 5](https://jmeter.apache.org/images/screenshots/Select-Recording-Template.png)](https://jmeter.apache.org/images/screenshots/Select-Recording-Template.png)

4.    A complete Test Plan is generated 
[![Image 6](https://jmeter.apache.org/images/screenshots/Test_Generated.png)](https://jmeter.apache.org/images/screenshots/Test_Generated.png)

5.    In the HTTP Request Defaults element: Server name or IP enter example.com Path leave blank[![Image 7](https://jmeter.apache.org/images/screenshots/http-config/http-request-defaults.png)](https://jmeter.apache.org/images/screenshots/http-config/http-request-defaults.png)

6.    Return to HTTP(S) Test Script Recorder, and click the Start button at the top. 
[![Image 8](https://jmeter.apache.org/images/screenshots/Proxy_Run.png)](https://jmeter.apache.org/images/screenshots/Proxy_Run.png)

This will start the JMeter proxy server which is used to intercept the browser requests. A file called ApacheJMeterTemporaryRootCA.crt will be generated in JMETER_HOME/bin folder. Install this certificate in your browser, if you don't know how to do it, read [Installing the JMeter CA certificate for HTTPS recording](https://jmeter.apache.org/usermanual/component_reference.html#HTTP%28S%29_Test_Script_Recorder)

26.3 Configure your browser to use the JMeter Proxy[¶](https://jmeter.apache.org/usermanual/jmeter_proxy_step_by_step.html#configure-browser "Link to here")
------------------------------------------------------------------------------------------------------------------------------------------------------------

At this point, JMeter's proxy is running. For this exercise, we will use Iceweasel/Firefox to view some pages on the JMeter website.

1.   Start Iceweasel/Firefox, but do not close JMeter.
2.    From the tool bar, click Edit→Preferences (or Tools→Preferences or type about:preferences#advanced as URL). This should bring up the options. [![Image 9](https://jmeter.apache.org/images/screenshots/firefox-network-settings.png)](https://jmeter.apache.org/images/screenshots/firefox-network-settings.png)

3.    Select the Advanced tab, and Network tab 
4.    Click Settings button near the top. 
5.    On the new pop-up, check Manual proxy configuration. The address and port fields should be enabled now. Address enter localhost or the IP address of your system Port enter 8888. [![Image 10](https://jmeter.apache.org/images/screenshots/firefox-configure-proxy.png)](https://jmeter.apache.org/images/screenshots/firefox-configure-proxy.png)

6.    Check Use this proxy server for all protocols
7.    Click OK button. This should return you to the browser 

26.4 Record your navigation[¶](https://jmeter.apache.org/usermanual/jmeter_proxy_step_by_step.html#navigation-recording "Link to here")
---------------------------------------------------------------------------------------------------------------------------------------

1.    With your browser, in the Address bar at the top, enter http://example.com/index.html (replace example.com with your websites address). and hit the enter key. 
2.   Click on a few links on your sites pages.
3.   Close your browser and bring up the JMeter window.

Expand the Thread Group and there should be several samplers. At this point, the test plan can be saved as is.

If you forget to add default HTTP Request settings, you will have to manually delete the server name, and port.

[![Image 11](https://jmeter.apache.org/images/screenshots/example-recording.png)](https://jmeter.apache.org/images/screenshots/example-recording.png)

In this sample, there aren't any default request parameters. If a particular request parameter is required by all pages, the request defaults is where one would add the entries.

1.    Select Thread Group and change a few defaults: Number of Threads (users) enter 5 Ramp-Up Period (in seconds)do not change Loop Count enter 100[![Image 12](https://jmeter.apache.org/images/screenshots/example-thread-group.png)](https://jmeter.apache.org/images/screenshots/example-thread-group.png)

26.5 Validate the script[¶](https://jmeter.apache.org/usermanual/jmeter_proxy_step_by_step.html#validate-script "Link to here")
-------------------------------------------------------------------------------------------------------------------------------

Now we need to validate the script before to run our test plan. Save the test plan.

Right click on the Thread Group Validate

[![Image 13](https://jmeter.apache.org/images/screenshots/Validate-Test-Plan.png)](https://jmeter.apache.org/images/screenshots/Validate-Test-Plan.png)

Check with View Results Tree element if all is ok.

26.6 Variabilize and Correlate the script[¶](https://jmeter.apache.org/usermanual/jmeter_proxy_step_by_step.html#correlate-start "Link to here")
------------------------------------------------------------------------------------------------------------------------------------------------

In some scripts, we will need to:

*   Variabilize some input (login, password, search words, …)
*   Correlate some data (session variable, …) between two requests

To variabilize, we can use:

*   CSV Data Set Config to get input data from csv file 
*    JMeter functions like __counter, __time, … 
*   etc.

To correlate, we can get data from a request with Post Processors like JSON Extractor, Regular Expression Extractor, … and inject it in another request.

To find data to correlate, the easiest way to do it is to use the Search function in View Results Tree.

[![Image 14](https://jmeter.apache.org/images/screenshots/Search-Correlation.png)](https://jmeter.apache.org/images/screenshots/Search-Correlation.png)

26.7 Start the test[¶](https://jmeter.apache.org/usermanual/jmeter_proxy_step_by_step.html#test-start "Link to here")
---------------------------------------------------------------------------------------------------------------------

At this point, we are ready to run our test plan and see what happens. When you're ready to run the test, there are two ways:

1.   With the gui, but it's not recommended to big load test.
2.   With the command line.

Solution 1, with the gui, but just during debug phase, use CLI mode (Non GUI) for your load test.

Run→Start or use the keyboard and press Ctrl+R

Before you start the test, add a Summary Report element and select it. As the test runs, the statistics will change until the test is done. At the end of the test, the summary report should look like this.

[![Image 15](https://jmeter.apache.org/images/screenshots/example-summary-report.png)](https://jmeter.apache.org/images/screenshots/example-summary-report.png)

While the test is running, in the upper right-hand corner, there should be a green circle. When the test is done, the circle should be grey.

[![Image 16](https://jmeter.apache.org/images/screenshots/example-running.png)](https://jmeter.apache.org/images/screenshots/example-running.png)

Solution 2, in command line, use jmeter -n -t [jmx file] -l [results file] -e -o [Path to output folder]

At the end of the test, an HTML report will be generated and available in [Path to output folder] used in command line.

*   [< Prev](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/junitsampler_tutorial.html)

 Share this page: 
*   [share](https://jmeter.apache.org/usermanual/jmeter_proxy_step_by_step.html "Share on facebook")
*   [tweet](https://jmeter.apache.org/usermanual/jmeter_proxy_step_by_step.html "Tweet on twitter")

[Go to top](https://jmeter.apache.org/usermanual/jmeter_proxy_step_by_step.html#top)

 Copyright © 1999 – 2024 , Apache Software Foundation 

Apache, Apache JMeter, JMeter, the Apache feather, and the Apache JMeter logo are trademarks of the Apache Software Foundation.
