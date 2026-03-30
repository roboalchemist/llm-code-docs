# Source: https://jmeter.apache.org/usermanual/glossary.html

Title: Apache JMeter
          -
          User's Manual: Glossary

URL Source: https://jmeter.apache.org/usermanual/glossary.html

Published Time: Sun, 07 Jan 2024 17:19:24 GMT

Markdown Content:
Apache JMeter - User's Manual: Glossary
===============
[Main content](https://jmeter.apache.org/usermanual/glossary.html#content)

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

*   [< Prev](https://jmeter.apache.org/usermanual/hints_and_tips.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/curl.html)

23. Glossary[¶](https://jmeter.apache.org/usermanual/glossary.html#glossary "Link to here")
===========================================================================================

[**Elapsed time**](https://jmeter.apache.org/usermanual/glossary.html). JMeter measures the elapsed time from just before sending the request to just after the last response has been received. JMeter does not include the time needed to render the response, nor does JMeter process any client code, for example Javascript.

[**Latency**](https://jmeter.apache.org/usermanual/glossary.html). JMeter measures the latency from just before sending the request to just after the first response has been received. Thus the time includes all the processing needed to assemble the request as well as assembling the first part of the response, which in general will be longer than one byte. Protocol analysers (such as Wireshark) measure the time when bytes are actually sent/received over the interface. The JMeter time should be closer to that which is experienced by a browser or other application client.

[**Connect Time**](https://jmeter.apache.org/usermanual/glossary.html). JMeter measures the time it took to establish the connection, including SSL handshake. Note that connect time is not automatically subtracted from [latency](https://jmeter.apache.org/usermanual/glossary.html#Latency). In case of connection error, the metric will be equal to the time it took to face the error, for example in case of Timeout, it should be equal to connection timeout.

As of JMeter 3.1, this metric is only computed for TCP Sampler, HTTP Request and JDBC Request.

[**Median**](https://jmeter.apache.org/usermanual/glossary.html) is a number which divides the samples into two equal halves. Half of the samples are smaller than the median, and half are larger. [Some samples may equal the median.] This is a standard statistical measure. See, for example: [Median](http://en.wikipedia.org/wiki/Median) entry at Wikipedia. The Median is the same as the 50 th Percentile

[**90% Line (90 th Percentile)**](https://jmeter.apache.org/usermanual/glossary.html) is the value below which 90% of the samples fall. The remaining samples too at least as long as the value. This is a standard statistical measure. See, for example: [Percentile](http://en.wikipedia.org/wiki/Percentile) entry at Wikipedia.

[**Standard Deviation**](https://jmeter.apache.org/usermanual/glossary.html) is a measure of the variability of a data set. This is a standard statistical measure. See, for example: [Standard Deviation](http://en.wikipedia.org/wiki/Standard_deviation) entry at Wikipedia. JMeter calculates the population standard deviation (e.g. STDEVP function in spreadsheets), not the sample standard deviation (e.g. STDEV).

[The **Thread Name**](https://jmeter.apache.org/usermanual/glossary.html) as it appears in Listeners and logfiles is derived from the Thread Group name and the thread within the group. 

 The name has the format groupName + " " + groupIndex + "-" + threadIndex where:

*   groupName - name of the Thread Group element
*   groupIndex - number of the Thread Group in the Test Plan, starting from 1
*   threadIndex - number of the thread within the Thread Group, starting from 1

 A test plan with two Thread Groups each with two threads would use the names: 
Thread Group 1-1
Thread Group 1-2
Thread Group 2-1
Thread Group 2-2

[**Throughput**](https://jmeter.apache.org/usermanual/glossary.html) is calculated as requests/unit of time. The time is calculated from the start of the first sample to the end of the last sample. This includes any intervals between samples, as it is supposed to represent the load on the server. 

 The formula is: Throughput = (number of requests) / (total time).

*   [< Prev](https://jmeter.apache.org/usermanual/hints_and_tips.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/curl.html)

 Share this page: 
*   [share](https://jmeter.apache.org/usermanual/glossary.html "Share on facebook")
*   [tweet](https://jmeter.apache.org/usermanual/glossary.html "Tweet on twitter")

[Go to top](https://jmeter.apache.org/usermanual/glossary.html#top)

 Copyright © 1999 – 2024 , Apache Software Foundation 

Apache, Apache JMeter, JMeter, the Apache feather, and the Apache JMeter logo are trademarks of the Apache Software Foundation.
