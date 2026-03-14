# Source: https://jmeter.apache.org/usermanual/realtime-results.html

Title: Apache JMeter
          -
          User's Manual: Live Statistics

URL Source: https://jmeter.apache.org/usermanual/realtime-results.html

Published Time: Sun, 07 Jan 2024 17:19:24 GMT

Markdown Content:
Apache JMeter - User's Manual: Live Statistics
===============
[Main content](https://jmeter.apache.org/usermanual/realtime-results.html#content)

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

*   [< Prev](https://jmeter.apache.org/usermanual/generating-dashboard.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/best-practices.html)

15. Real-time results[¶](https://jmeter.apache.org/usermanual/realtime-results.html#realtime-results "Link to here")
====================================================================================================================

Since JMeter 2.13 you can get real-time results sent to a backend through the [Backend Listener](https://jmeter.apache.org/usermanual/component_reference.html#Backend_Listener) using potentially any backend (JDBC, JMS, Webservice, …) by providing a class which implements [AbstractBackendListenerClient](https://jmeter.apache.org/api/org/apache/jmeter/visualizers/backend/AbstractBackendListenerClient.html). 

 JMeter ships with:

*    a GraphiteBackendListenerClient which allows you to send metrics to a Graphite Backend. 

 This feature provides: 
    *   Live results
    *   Nice graphs for metrics
    *   Ability to compare 2 or more load tests
    *   Storing monitoring data as long as JMeter results in the same backend
    *   …

*    an InfluxDBBackendListenerClient introduced in JMeter 3.2 which allows you to send metrics to an InfluxDB Backend using UDP or HTTP protocols This feature provides: 
    *   Live results
    *   Nice graphs for metrics
    *   Ability to compare 2 or more load tests
    *   Ability to add annotations to graphs
    *   Storing monitoring data as long as JMeter results in the same backend
    *   …

 In this document we will present the configuration setup to graph and historize the data in different backends: 
*   InfluxDB setup for InfluxDBBackendListenerClient
*   InfluxDB setup for GraphiteBackendListenerClient
*   Grafana
*   Graphite

15.1 Metrics exposed[¶](https://jmeter.apache.org/usermanual/realtime-results.html#metrics "Link to here")
----------------------------------------------------------------------------------------------------------

15.1.1 Thread/Virtual Users metrics[¶](https://jmeter.apache.org/usermanual/realtime-results.html#metrics-threads "Link to here")
---------------------------------------------------------------------------------------------------------------------------------

Thread metrics are the following:

<rootMetricsPrefix>test.minAT Min active threads<rootMetricsPrefix>test.maxAT Max active threads<rootMetricsPrefix>test.meanAT Mean active threads<rootMetricsPrefix>test.startedT Started threads<rootMetricsPrefix>test.endedT Finished threads

15.1.2 Response times metrics[¶](https://jmeter.apache.org/usermanual/realtime-results.html#metrics-response-times "Link to here")
----------------------------------------------------------------------------------------------------------------------------------

Response related metrics are the following:

<rootMetricsPrefix><samplerName>.ok.count Number of successful responses for sampler name<rootMetricsPrefix><samplerName>.h.count Server hits per seconds, this metric cumulates Sample Result and Sub results (if using Transaction Controller, "Generate parent sampler" should be unchecked)<rootMetricsPrefix><samplerName>.ok.min Min response time for successful responses of sampler name<rootMetricsPrefix><samplerName>.ok.max Max response time for successful responses of sampler name<rootMetricsPrefix><samplerName>.ok.avg Average response time for successful responses of sampler name.<rootMetricsPrefix><samplerName>.ok.pct<percentileValue>Percentile computed for successful responses of sampler name. There will be one metric for each calculated value.<rootMetricsPrefix><samplerName>.ko.count Number of failed responses for sampler name<rootMetricsPrefix><samplerName>.ko.min Min response time for failed responses of sampler name<rootMetricsPrefix><samplerName>.ko.max Max response time for failed responses of sampler name<rootMetricsPrefix><samplerName>.ko.avg Average response time for failed responses of sampler name.<rootMetricsPrefix><samplerName>.ko.pct<percentileValue>Percentile computed for failed responses of sampler name. There will be one metric for each calculated value.<rootMetricsPrefix><samplerName>.a.count Number of responses for sampler name (sum of ok.count and ko.count)<rootMetricsPrefix><samplerName>.sb.bytes Sent Bytes<rootMetricsPrefix><samplerName>.rb.bytes Received Bytes<rootMetricsPrefix><samplerName>.a.min Min response time for responses of sampler name (min of ok.count and ko.count)<rootMetricsPrefix><samplerName>.a.max Max response time for responses of sampler name (max of ok.count and ko.count)<rootMetricsPrefix><samplerName>.a.avg Average response time for responses of sampler name (avg of ok.count and ko.count)<rootMetricsPrefix><samplerName>.a.pct<percentileValue>Percentile computed for responses of sampler name. There will be one metric for each calculated value. (calculated on the totals for OK and failed samples)
The default percentiles setting on the [Backend Listener](https://jmeter.apache.org/usermanual/component_reference.html#Backend_Listener) is "90;95;99", i.e. the 3 percentiles 90%, 95% and 99%.

The [Graphite naming hierarchy](https://graphite.readthedocs.io/en/latest/feeding-carbon.html#step-1-plan-a-naming-hierarchy) uses dot (".") to separate elements. This could be confused with decimal percentile values. JMeter converts any such values, replacing dot (".") with underscore ("-"). For example, "99.9" becomes "99_9"

By default JMeter sends metrics for all samplers accumulated under the samplerName "all". If the Backend Listener samplersList is configured, then JMeter also sends the metrics for the matching sample names unless summaryOnly=true

15.2 JMeter configuration[¶](https://jmeter.apache.org/usermanual/realtime-results.html#jmeter-configuration "Link to here")
----------------------------------------------------------------------------------------------------------------------------

To make JMeter send metrics to backend add a [BackendListener](https://jmeter.apache.org/usermanual/component_reference.html#Backend_Listener) using the InfluxDBBackendListenerClient.

[![Image 4: InfluxDB configuration](https://jmeter.apache.org/images/screenshots/backend_listener.png)](https://jmeter.apache.org/images/screenshots/backend_listener.png)

InfluxDB configuration

15.3 InfluxDB configuration[¶](https://jmeter.apache.org/usermanual/realtime-results.html#influxdb_db_configuration "Link to here")
-----------------------------------------------------------------------------------------------------------------------------------

Do one of the following to store data sent by the Backend Listener:

*    For InfluxDB 2 setup, create a jmeter[bucket](https://v2.docs.influxdata.com/v2.0/organizations/buckets/create-bucket/)
*    For InfluxDB 1.x setup, create a jmeter database using the [Influx CLI](https://docs.influxdata.com/influxdb/v1.8/introduction/get-started/)

 You can also use the HTTP API i.e. curl -i -XPOST http://localhost:8086/query --data-urlencode "q=CREATE DATABASE jmeter"

15.3.1 InfluxDB setup for InfluxDBBackendListenerClient[¶](https://jmeter.apache.org/usermanual/realtime-results.html#influxdb "Link to here")
----------------------------------------------------------------------------------------------------------------------------------------------

InfluxDB is an open-source, distributed, time-series database that allows to easily store metrics. Installation and configuration is very easy, read this for more details [InfluxDB documentation](https://docs.influxdata.com/influxdb/latest/introduction/installation/). 

 InfluxDB data can be easily viewed in a browser through [Grafana](http://grafana.org/).

15.3.2 InfluxDB 2 setup for InfluxDBBackendListenerClient[¶](https://jmeter.apache.org/usermanual/realtime-results.html#influxdb_v2 "Link to here")
---------------------------------------------------------------------------------------------------------------------------------------------------

The configuration should specify the influxdbToken parameter and also specify bucket and org as query parameters in the influxdbUrl. See the [InfluxDB v2 API](https://v2.docs.influxdata.com/v2.0/api/#operation/PostWrite) for more details.

How to retrieve the required information in the InfluxDB UI:

*   [influxdbToken](https://v2.docs.influxdata.com/v2.0/security/tokens/view-tokens/)
*   [bucket](https://v2.docs.influxdata.com/v2.0/organizations/buckets/view-buckets/)
*   [org](https://v2.docs.influxdata.com/v2.0/organizations/view-orgs/)

[![Image 5: InfluxDB 2 configuration](https://jmeter.apache.org/images/screenshots/backend_listener_influxdb_v2.png)](https://jmeter.apache.org/images/screenshots/backend_listener_influxdb_v2.png)

InfluxDB 2 configuration

15.4 Grafana configuration[¶](https://jmeter.apache.org/usermanual/realtime-results.html#grafana_configuration "Link to here")
------------------------------------------------------------------------------------------------------------------------------

Installing grafana 

 Read [documentation](https://docs.grafana.org/) for more details. Add the [datasource](https://docs.grafana.org/features/datasources/influxdb/)

 Here is the kind of dashboard that you could obtain: [![Image 6: Grafana dashboard](https://jmeter.apache.org/images/screenshots/grafana_dashboard.png)](https://jmeter.apache.org/images/screenshots/grafana_dashboard.png)

Grafana dashboard

15.5 Graphite Configuration[¶](https://jmeter.apache.org/usermanual/realtime-results.html#graphite_configuration "Link to here")
--------------------------------------------------------------------------------------------------------------------------------

To make JMeter send metrics to backend, add a BackendListener using the GraphiteBackendListenerClient.

[GraphiteBackendListenerClient](https://jmeter.apache.org/usermanual/component_reference.html#Backend_Listener) section will help you do the configuration.

[![Image 7: Graphite configuration](https://jmeter.apache.org/images/screenshots/backend_listener_graphite.png)](https://jmeter.apache.org/images/screenshots/backend_listener_graphite.png)

Graphite configuration

15.5.1 Graphite Sender[¶](https://jmeter.apache.org/usermanual/realtime-results.html#graphite_sendor "Link to here")
--------------------------------------------------------------------------------------------------------------------

Two types of Senders are available. TextGraphiteMetricsSender, PickleGraphiteMetricsSender

*    For plaintext protocol, set graphiteMetricsSender parameter to org.apache.jmeter.visualizers.backend.graphite.TextGraphiteMetricsSender
*    For pickle protocol, set graphiteMetricsSender parameter to org.apache.jmeter.visualizers.backend.graphite.PickleGraphiteMetricsSender

To send large amounts of data, use the Pickle sender. It is a more efficient transmission method compared to textplain. Read [the Graphite documentation](https://graphite.readthedocs.io/en/latest/feeding-carbon.html) for more details.

[![Image 8: Graphite pickle sender](https://jmeter.apache.org/images/screenshots/backend_listener_graphite_pickle.png)](https://jmeter.apache.org/images/screenshots/backend_listener_graphite_pickle.png)

Graphite pickle sender

*   [< Prev](https://jmeter.apache.org/usermanual/generating-dashboard.html)
*   [Index](https://jmeter.apache.org/index.html)
*   [Next >](https://jmeter.apache.org/usermanual/best-practices.html)

 Share this page: 
*   [share](https://jmeter.apache.org/usermanual/realtime-results.html "Share on facebook")
*   [tweet](https://jmeter.apache.org/usermanual/realtime-results.html "Tweet on twitter")

[Go to top](https://jmeter.apache.org/usermanual/realtime-results.html#top)

 Copyright © 1999 – 2024 , Apache Software Foundation 

Apache, Apache JMeter, JMeter, the Apache feather, and the Apache JMeter logo are trademarks of the Apache Software Foundation.
