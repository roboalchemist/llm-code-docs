# Pinpoint Documentation

Source: https://pinpoint-apm.gitbook.io/llms-full.txt

---

# Introduction

[![Maven](https://img.shields.io/github/actions/workflow/status/pinpoint-apm/pinpoint/maven.yml?branch=master\&label=build\&logo=github)](https://github.com/pinpoint-apm/pinpoint/actions?query=workflow%3AMaven) [![codecov](https://codecov.io/gh/pinpoint-apm/pinpoint/branch/master/graph/badge.svg)](https://codecov.io/gh/pinpoint-apm/pinpoint)

**Pinpoint** is an APM (Application Performance Management) tool for large-scale distributed systems written in Java / [PHP](https://github.com/pinpoint-apm/pinpoint-c-agent). Inspired by [Dapper](http://research.google.com/pubs/pub36356.html), Pinpoint provides a solution to help analyze the overall structure of the system and how components within them are interconnected by tracing transactions across distributed applications.

You should definitely check **Pinpoint** out If you want to

* understand your [application topology](https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/overview) at a glance
* monitor your application in *Real-Time*
* gain code-level visibility to every transaction
* install APM Agents without changing a single line of code
* have minimal impact on the performance (approximately 3% increase in resource usage)

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-a15a27acd3b0d96723a857cf64503b9979c76bfa%2Fss_server-map.png?alt=media\&token=899f1043-030f-4df7-a52f-4433b6e2ca72)

## Live Demo

* [demo](http://223.130.142.103:8080/main/ApiGateway@SPRING_BOOT/5m?inbound=1\&outbound=4\&wasOnly=false\&bidirectional=false) - Here is a Demo, So that you can take a look at Pinpoint right away.

## Want a quick tour?

* [Overview](https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/overview) / [History](https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/history) / [Tech Details](https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/techdetail) to get to know more about Pinpoint
* [Videos](https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/videos) - Checkout our videos on Pinpoint

{% embed url="<https://youtu.be/U4EwnB34Dus>" %}

## Getting Started

* [Quick-start guide(Lastest Snapshot)](https://pinpoint-apm.gitbook.io/pinpoint/getting-started/quickstart) for simple test run of Pinpoint
* [Installation guide(Lastest Snapshot)](https://pinpoint-apm.gitbook.io/pinpoint/getting-started/installation) for further instructions.

## Google Analytics

The web module has google analytics attached that tracks the number and the order of button clicks in the server map, transaction list, and the inspector view.

This data is used to better understand how users interact with the Web UI which gives us valuable information in improving Pinpoint Web's user experience. To disable this for any reason, set the following option to false in *pinpoint-web.properties* for your web instance.

```
config.sendUsage=false
```

## Is your application created with PHP?

Pinpoint has started to support application written in PHP. [Check-out our php-agent repository](https://github.com/pinpoint-apm/pinpoint-c-agent).

## Looking for place to ask questions?

[Questions and FAQ](https://pinpoint-apm.gitbook.io/pinpoint/faq)

## License

Pinpoint is licensed under the Apache License, Version 2.0. See [LICENSE](https://github.com/pinpoint-apm/pinpoint/blob/master/LICENSE) for full license text.

```
Copyright 2019 NAVER Corp.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```


# What's New

## Improvements

* **\[Agent]** Enhanced Reactor tracing
* **\[Agent]** Added support for nested JAR file systems used in Spring Boot
* **\[Agent]** Added Kafka Streams support `-Dprofiler.kafka-streams.trace.process=true`
* **\[Agent]** Added support for Java 26
* **\[Collector]** Improved CPU usage

## Bug Fixes

* **\[Agent]** Fixed an issue where annotation values were not sent to the collector when the value was null

## What's Changed

* \[#12559] Prepare 3.0.4-SNAPSHOT by @intr3p1d in <https://github.com/pinpoint-apm/pinpoint/pull/12568>
* \[#12657] Backport: Update mono runnable interceptor of reactor pulgin by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12658>
* \[#noissue] 3.0.4-alpha1 release by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12659>
* \[#noissue] rollback 3.0.4-alpha1 release by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12661>
* \[#12664] Backport: Fix nested jar loading of instrument class scanner by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12665>
* \[#12667] Backport: Fix kafka plugin streams interceptor by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12668>
* \[#12905] Backport: Update agent "not matched stack id" error log by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12906>
* \[#12919] Backport: Fix agent NPE in annotation value mapper by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12947>
* \[#12966] Backport: Remove validation annotations from high-frequency collector methods to fix performance regression by @Copilot in <https://github.com/pinpoint-apm/pinpoint/pull/12967>
* \[#12948] Backport: Bump asm from 9.7.1 to 9.8 by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12949>
* \[#12986] Backport : Introducing jitter-based scheduling for LinkScheduler by @emeroad in <https://github.com/pinpoint-apm/pinpoint/pull/12988>
* \[#13030] Backport: Bump spring-security by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/13042>
* \[#13033] Backport: Bump ASM from 9.8 to 9.9 by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/13043>
* \[#13054] 3.0.4 release by @intr3p1d in <https://github.com/pinpoint-apm/pinpoint/pull/13055>

**Full Changelog**: <https://github.com/pinpoint-apm/pinpoint/compare/v3.0.3...v3.0.4>

## Upgrade consideration

HBase compatibility table:

| Pinpoint Version | HBase 1.x | HBase 2.x                                                                                                             |
| ---------------- | --------- | --------------------------------------------------------------------------------------------------------------------- |
| 2.0.x - 2.2.x    | yes       | [optional](https://pinpoint-apm.gitbook.io/pinpoint/documents/hbase-upgrade#do-you-like-to-use-hbase-2x-for-pinpoint) |
| 2.3.x - 2.5.x    | yes       | [hbase2-module](https://github.com/pinpoint-apm/pinpoint/tree/2.3.x/hbase2-module)                                    |
| 3.0.x            | no        | yes                                                                                                                   |
| 3.1.x            | no        | yes                                                                                                                   |

Agent compatibility to Collector table:

| Agent Version | Collector 2.x.x | Collector 3.0.x | Collector 3.1.x |
| ------------- | --------------- | --------------- | --------------- |
| 2.x.x         | yes             | yes             | yes             |
| 3.0.x         | no              | yes             | yes             |
| 3.1.x         | no              | no              | yes             |

Additionally, the required Java version to run each Pinpoint component is given below:

| Pinpoint Version | Agent | Collector | Web | Batch |
| ---------------- | ----- | --------- | --- | ----- |
| 2.0.x            | 6-13  | 8         | 8   | 8     |
| 2.1.x            | 6-14  | 8         | 8   | 8     |
| 2.2.x            | 7-14  | 8         | 8   | 8     |
| 2.3.x            | 7-17  | 8         | 8   | 8     |
| 2.4.x            | 7-18  | 11        | 11  | 11    |
| 2.5.x            | 8-19  | 11        | 11  | 11    |
| 3.0.x            | 8-21  | 17        | 17  | 17    |
| 3.1.x            | 8-24  | 17        | 17  | 17    |

## Supported Modules

* JDK 6+
* Supported versions of the \* indicated library may differ from the actual version.

| Title                                                                                                          | Instrumented Library                 | Min      | Max       | Comment |   |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------ | -------- | --------- | ------- | - |
| [Tomcat](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/tomcat)                     |                                      | 6.x      | 9.x       |         |   |
| [Jetty](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/jetty)                       |                                      | 8.x      | 9.x       |         |   |
| [JBoss](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/jboss)                       |                                      | 6.x      | 7.x       |         |   |
| [Websphere](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/websphere)               |                                      | 6.x      | 8.x       |         |   |
| [Vertx](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/vertx)                       |                                      | 3.3      | 3.5       |         |   |
| [Weblogic](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/weblogic)                 |                                      | 10.x     | 12.x      |         |   |
| [Undertow](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/undertow)                 |                                      |          |           |         |   |
| [Undertow Servlet](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/undertow-servlet) |                                      |          |           |         |   |
| Jasper                                                                                                         |                                      |          |           |         |   |
|                                                                                                                |                                      |          |           |         |   |
| Java Async Thread                                                                                              |                                      |          |           |         |   |
|                                                                                                                |                                      |          |           |         |   |
| OpenWhisk                                                                                                      | whisk.core                           |          |           |         |   |
|                                                                                                                |                                      |          |           |         |   |
| SpringMVC Framework                                                                                            | spring-webmvc                        | 3.0.7    | 5.3.6     |         |   |
| Spring Web                                                                                                     | spring-web                           | 4.1.2    | 4.3.30    |         |   |
| Spring RabbitMQ                                                                                                | spring-rabbit                        | 1.3.3    | 2.2.16    |         |   |
| Spring IBatis                                                                                                  | spring-ibatis                        | 2.0.7    | 2.0.8     |         |   |
| Spring MyBatis                                                                                                 | mybatis-spring                       | 1.1.0    | 1.3.3     |         |   |
| \*[Spring Boot](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/spring-boot)         | spring-boot-autoconfigure            |          |           |         |   |
| \*[Spring Webflux](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/spring-webflux)   | spring-webflux                       |          |           |         |   |
|                                                                                                                |                                      |          |           |         |   |
| MyBatis                                                                                                        | mybatis                              | 3.0.3    | 3.3.1     |         |   |
| [Hystrix](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/hystrix)                   | hystrix-core                         | 1.4.0    | 1.5.18    |         |   |
|                                                                                                                |                                      |          |           |         |   |
| JDKHTTP                                                                                                        |                                      |          |           |         |   |
| Httpclient3                                                                                                    | commons-httpclient                   | 3.0      | 3.1       |         |   |
| Httpclient4                                                                                                    | httpclient                           | 4.0      | 4.5.4     |         |   |
| Thrift                                                                                                         | libthrift                            | 0.9.1    | 0.14.1    |         |   |
| Google HTTP Client                                                                                             | google-http-client                   | 1.19.0   | 1.39.2    |         |   |
| AsyncHttpClient                                                                                                | async-http-client                    | 1.7.24   | 1.8.17    |         |   |
| OkHttp                                                                                                         | okhttp                               | 2.0.0    | 3.3.1     |         |   |
| Apache HttpAsyncClient                                                                                         | httpasyncclient                      | 4.0      | 4.1.3     |         |   |
| \*Akka HTTP                                                                                                    | akka-http\_2.12                      | 10.1.0   | 10.1.x    |         |   |
| \*[Kafka](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/kafka)                     | kafka-clients                        | 0.11.0.1 |           |         |   |
| GRPC                                                                                                           | grpc-stub                            | 1.8.0    | 1.37.0    |         |   |
| \*[Reactor](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/reactor)                 | reactor-core                         | 3.3.0    | 3.3.1     |         |   |
| \*[Reactor Netty](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/reactor-netty)     | reactor-netty                        | 0.8.0    | 0.9.2     |         |   |
|                                                                                                                |                                      |          |           |         |   |
| Log4j                                                                                                          | log4j                                | 1.2.16   | 1.2.17    |         |   |
| Logback                                                                                                        | logback-classic                      | 1.0.13   | 1.2.3     |         |   |
| Log4j2                                                                                                         | log4j-core                           | 2.0      | 2.12.1    |         |   |
|                                                                                                                |                                      |          |           |         |   |
| \*Arcus                                                                                                        | arcus-java-client                    | 1.7.0    | 1.11.4    |         |   |
| \*MsSQL (jTDS)                                                                                                 | jtds                                 | 1.2.8    |           |         |   |
| \*MsSQL                                                                                                        | mssql-jdbc                           |          |           |         |   |
| HikariCP                                                                                                       | HikariCP-java6                       | 2.3.0    | 2.3.13    |         |   |
| Jackson-mapper-asl                                                                                             | jackson-mapper-asl                   | 1.0.1    | 1.8.11    |         |   |
| Jackson Databind                                                                                               | jackson-databind                     | 2.0.6    | 2.12.3    |         |   |
| MariaDB Connector/J                                                                                            | mariadb-java-client                  | 1.3.0    | 2.7.2     |         |   |
| MongoDB Java Driver                                                                                            | mongodb-driver                       | 3.0.0    | 3.12.8    |         |   |
| Elasticsearch                                                                                                  | elasticsearch-rest-high-level-client | 6.0.0    | 6.8.15    |         |   |
| Datastax Java Driver                                                                                           | cassandra-driver-core                | 2.0.10   | 3.11.0    |         |   |
| Druid                                                                                                          | druid                                | 1.0.0    | 1.2.6     |         |   |
| \*Cubrid                                                                                                       | cubrid-jdbc-driver                   | 8.4.1    | 10.0.0    |         |   |
| \*Commons DBCP                                                                                                 | commons-dbcp                         | 1.0      | 1.4       |         |   |
| \*Commons DBCP2                                                                                                | commons-dbcp2                        | 2.0      | 2.5.0     |         |   |
| \*HBase                                                                                                        | hbase-client                         | 1.2.6.1  | 1.2.6.1   |         |   |
| \*MySQL                                                                                                        | mysql-connector-java                 | 5.0      | 8.x       |         |   |
| \*Oracle JDBC Driver                                                                                           | ojdbc                                |          |           |         |   |
| \*PostgreSQL JDBC Driver                                                                                       | postgresql                           |          |           |         |   |
| \*[Redis](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/redis)                     | jedis                                | 2.4.2    |           |         |   |
| \*[Redis](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/redis-lettuce)             | lettuce-core                         | 5.0.0    | 5.1.2     |         |   |
| \*[Redis](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/redis-redisson)            | redisson                             | 3.10.0   | 3.10.4    |         |   |
|                                                                                                                |                                      |          |           |         |   |
| Apache CXF                                                                                                     | cxf-rt-rs-client                     | 3.0.0    | 3.4.3     |         |   |
| Netty                                                                                                          | netty-all                            | 4.1.0    | 4.1.63    |         |   |
| ActiveMQ                                                                                                       | activemq-all                         | 5.1.0    | 5.16.1    |         |   |
| [RxJAVA](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/rxjava)                     | rxjava                               | 1.0.0    | 1.3.8     |         |   |
| [RabbitMQ](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/rabbitmq)                 | amqp-client                          | 2.7.0    | 5.12.0    |         |   |
| [Paho MQTT](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/paho-mqtt)               | org.eclipse.paho.client.mqttv3       | 1.0.2    | 1.2.5     |         |   |
| [Paho MQTT](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/paho-mqtt)               | org.eclipse.paho.mqttv5.client       | 1.2.5    | 1.2.5     |         |   |
|                                                                                                                |                                      |          |           |         |   |
| Gson                                                                                                           | gson                                 | 1.1      | 2.8.3     |         |   |
| Json                                                                                                           | json-lib                             | 1.0      | 2.2.2     |         |   |
| FastJson                                                                                                       | fastjson                             | 1.2.10   | 1.2.76    |         |   |
| Dubbo                                                                                                          | dubbo                                | 2.5.1    | 2.6.9     |         |   |
| kafka-clients                                                                                                  | kafka-clients                        | 0.11.0.0 | 2.6.1     |         |   |
| postgresql                                                                                                     | postgresql                           | 9.4.1208 | 42.2.19   |         |   |
| ojdbc8                                                                                                         | ojdbc8                               | 12.2.0.1 | 21.1.0.0  |         |   |
| ojdbc10                                                                                                        | ojdbc10                              | 19.3.0.0 | 19.10.0.0 |         |   |


# Overview

Services nowadays often consist of many different components, communicating amongst themselves as well as making API calls to external services. How each and every transaction gets executed is often left as a blackbox. Pinpoint traces transaction flows between these components and provides a clear view to identify problem areas and potential bottlenecks.

* **ServerMap** - Understand the topology of any distributed systems by visualizing how their components are interconnected. Clicking on a node reveals details about the component, such as its current status, and transaction count.
* **Realtime Active Thread Chart** - Monitor active threads inside applications in real-time.
* **Request/Response Scatter Chart** - Visualize request count and response patterns over time to identify potential problems. Transactions can be selected for additional detail by **dragging over the chart**.

![Server Map](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-a15a27acd3b0d96723a857cf64503b9979c76bfa%2Fss_server-map.png?alt=media\&token=899f1043-030f-4df7-a52f-4433b6e2ca72)

* **CallStack** - Gain code-level visibility to every transaction in a distributed environment, identifying bottlenecks and points of failure in a single view.

![Call Stack](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-735f042f7dc51378efe3f24d2ce53e1f295409d4%2Fss_call-stack.png?alt=media\&token=4afcecf6-8d1a-48d5-b5b8-8d0e6c8e8647)

* **Inspector** - View additional details on the application such as CPU usage, Memory/Garbage Collection, TPS, and JVM arguments.

![Inspector](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-07c84a62894cf4307ed7dc6ab2f5e44013ca2892%2Fss_inspector.png?alt=media\&token=97d631ef-f05b-47fa-8059-36efa841278b)

## Architecture

![Pinpoint Architecture](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-fc010a909c9559db169703072bd0dccacc283078%2Fpinpoint-architecture.png?alt=media)


# History

Pinpoint is a platform that analyzes large-scale distributed systems and provides a solution to handle large collections of trace data. It has been developed since July 2012 and was launched as an open-source project on January 9, 2015.

This article introduces Pinpoint; it describes what motivated us to start this project, which technologies are used, and how the Pinpoint Agent can be optimized.

> 本文的中文翻译版本 [请见这里](https://github.com/skyao/leaning-pinpoint/blob/master/design/technical_overview.md)

## Motivation to Get Started & Pinpoint Characteristics

Compared to nowadays, the number of Internet users was relatively small and the architecture of Internet services was less complex. Web services were generally configured using a 2-tier (web server and database) or 3-tier (web server, application server, and database) architecture. However, today, supporting a large number of concurrent connections is required and functionalities and services should be organically integrated as the Internet has grown, resulting in much more complex combinations of the software stack. That is n-tier architecture more than 3 tiers has become more widespread. A service-oriented architecture (SOA) or the [microservices](http://en.wikipedia.org/wiki/Microservices) architecture is now a reality.

The system's complexity has consequently increased. The more complex it is, the more difficult you solve problems such as system failure or performance issues. For example, Finding solutions in a 3-tier system is far less complicated. You only need to analyze 3 main components; a web server, an application server, and a database where the number of servers is small. While, if a problem occurs in an n-tier architecture, a large number of components and servers should be investigated. Another problem is that it is difficult to see the big picture only with an analysis of individual components; a low visibility issue is raised. The higher the degree of system complexity is, the longer it takes time to find out the reasons. Even worse, probability increases in which we may not even find them at all.

Such problems have occurred in the systems at NAVER. A variety of tools like Application Performance Management (APM) were used but they were not enough to handle the problems effectively; so we finally ended up developing a new tracing platform for n-tier architecture, which can provide solutions to systems with an n-tier architecture.

Pinpoint, began development in July 2012 and was launched as an open-source project in January 2015, is an n-tier architecture tracing platform for large-scale distributed systems. The characteristics of Pinpoint are as follows:

* Distributed transaction tracing to trace messages across distributed applications
* Automatically detecting the application topology that helps you to figure out the configurations of an application
* Horizontal scalability to support large-scale server group
* Providing code-level visibility to easily identify points of failure and bottlenecks
* Adding a new functionality without code modifications, using the bytecode instrumentation technique


# Tech Details

In this article, we describe the Pinpoint's techniques such as transaction tracing and bytecode instrumentation. And we explain the optimization method applied to Pinpoint Agent, which modifies bytecode and record performance data.

## Distributed Transaction Tracing, Modeled after Google's Dapper

Pinpoint traces distributed requests in a single transaction, modeled after Google's Dapper.

### How Distributed Transaction Tracing Works in Google's Dapper

The purpose of a distributed tracing system is to identify relationships between Node 1 and Node 2 in a distributed system when a message is sent from Node 1 to Node 2 (Figure 1).

![Figure 1. Message relationship in a distributed system](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-9473e149d5d3ec8ddbc00e2c8834478edb9b63d0%2Ftd_figure1.png?alt=media\&token=8fc3d32f-0801-40da-a3e9-b3c93bd6c5c1)

Figure 1. Message relationship in a distributed system

The problem is that there is no way to identify relationships between messages. For example, we cannot recognize relationships between N messages sent from Node 1 and N' messages received in Node 2. In other words, when X-th message is sent from Node 1, the X-th message cannot be identified among N' messages received in Node 2. An attempt was made to trace messages at TCP or operating system level. However, implementation complexity was high with low performance because it should be implemented separately for each protocol. In addition, it was difficult to accurately trace messages.

However, a simple solution to resolve such issues has been implemented in Google's Dapper. The solution is to add application-level tags that can be a link between messages when sending a message. For example, it includes tag information for a message in the HTTP header at an HTTP request and traces the message using this tag.

> Google's Dapper
>
> For more information on Google's Dapper, see "[Dapper, a Large-Scale Distributed Systems Tracing Infrastructure](http://research.google.com/pubs/pub36356.html)."

Pinpoint is modeled on the tracing technique of Google's Dapper but has been modified to add application-level tag data in the call header to trace distributed transactions at a remote call. The tag data consists of a collection of keys, which is defined as a TraceId.

### Data Structure in Pinpoint

In Pinpoint, the core of data structure consists of Spans, Traces, and TraceIds.

* Span: The basic unit of RPC (remote procedure call) tracing; it indicates work processed when an RPC arrives and contains trace data. To ensure the code-level visibility, a Span has children labeled SpanEvent as a data structure. Each Span contains a TraceId.
* Trace: A collection of Spans; it consists of associated RPCs (Spans). Spans in the same trace share the same TransactionId. A Trace is sorted as a hierarchical tree structure through SpanIds and ParentSpanIds.
* TraceId: A collections of keys consisting of TransactionId, SpanId, and ParentSpanId. The TransactionId indicates the message ID, and both the SpanId and the ParentSpanId represent the parent-child relationship of RPCs.
  * TransactionId (TxId): The ID of the message sent/received across distributed systems from a single transaction; it must be globally unique across the entire group of servers.
  * SpanId: The ID of a job processed when receiving RPC messages; it is generated when an RPC arrives at a node.
  * ParentSpanId (pSpanId): The SpanId of the parent span which generated the RPC. If a node is the starting point of a transaction, there will not be a parent span - for these cases, we use a value of -1 to denote that the span is the root span of a transaction.

> Differences in terms between Google's Dapper and NAVER's Pinpoint
>
> The term "TransactionId" in Pinpoint has the same meaning as the term "TraceId" in Google's Dapper and the term "TraceId" in Pinpoint refers to a collection of keys.

### How TraceId Works

The figure below illustrates the behavior of a TraceId in which RPCs were made 3 times within 4 nodes.

![Figure 2. Example of a TraceId behavior](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-e40328489e218852c90f58e486f1107fecce2bb7%2Ftd_figure2.png?alt=media\&token=0c0732ef-a83f-45c4-ae7f-63bba50cb60c)

Figure 2. Example of a TraceId behavior

A TransactionId (TxId) represents that three different RPCs are associated with each other as a single transaction in Figure 2. However, a TransactionId itself can't explicitly describe the relationship between RPCs. To identify the relationships between RPCs, a SpanId and a ParentSpanId (pSpanId) are required. Suppose that a node is Tomcat. You can think of a SpanId as a thread which handles HTTP requests. A ParentSpanId indicates the SpainId of a parent that makes RPC calls.

Pinpoint can find associated n Spans using a TransactionId and can sort them as a hierarchical tree structure using a SpanId and a ParentSpanId.

A SpanId and a ParentSpanId are 64-bit long integers. A conflict might arise because the number is generated arbitrarily, but considering the range of value from -9223372036854775808 to 9223372036854775807, this is unlikely to happen. If there is a conflict between keys, Pinpoint as well as Google's Dapper lets developers know what happened, instead of resolving the conflict.

A TransactionId consists of AgentIds, JVM (Java virtual machine) startup time, and SequenceNumbers.

* AgentId: A user-created ID when JVM starts; it must be globally unique across the entire group of servers where Pinpoint has been installed. The easiest way to make it unique is to use a hostname ($HOSTNAME) because the hostname is not duplicate in general. If you need to run multiple JVMs within the server group, add a postfix to the hostname to avoid duplicates.
* JVM startup time: Required to guarantee a unique SequenceNumber which starts with zero. This value is used to prevent ID conflicts when a user creates duplicate AgentId by mistake.
* SequenceNumber: ID issued by the Pinpoint Agent, with sequentially increasing numbers that start with zero; it is issued per message.

Dapper and [Zipkin](https://github.com/twitter/zipkin), a distributed systems tracing platform at Twitter, generate random TraceIds (TransactionIds in Pinpoint) and consider conflict situations as a normal case. However, we wanted to avoid this conflict as much as possible in Pinpoint. We had two available options for this; one with a method in which the amount of data is small but the probability of conflict is high; the other is a method in which the amount of data is large but the probability of conflict is low; We chose the second option.

There may be a better ways to handle transactions. We came up with several ideas such as key issue by a central key server. But we didn't implement this in the system due to performance issues and network errors. We are still considering issuing keys in bulk as an alternative Solution. So maybe later in the future, such methods can be developed; But for now, a simple method is adopted. In Pinpoint, a TransactionId is regarded as changeable data.

## Bytecode Instrumentation, Not Requiring Code Modifications

Earlier, we explained distributed transaction tracing. One way for implementing this is that developers to modify their code by themselves. Allow developers to add tag information when an RPC is made. However, it could be a burden to modify code even though such functionality is useful to developers.

Twitter's Zipkin provides the functionality of distributed transaction tracing using modified libraries and its container (Finagle). However, it requires the code to be modified if needed. We wanted the functionality to work without code modifications and desired to ensure code-level visibility. To solve such problems, the bytecode instrumentation technique was adopted in Pinpoint. The Pinpoint Agent intervenes code to make RPCs so as to automatically handle tag information.

### Overcoming Disadvantages of Bytecode Instrumentation

There are two ways for distributed transaction tracing as below. Bytecode instrumentation is one of an automatic method.

* Manual method: Developers develop code that records data at important points using APIs provided by Pinpoint.
* Automatic method: Developers do not involve code modifications because Pinpoint decides which API is to be intervened and developed.

Advantages and disadvantages of each method are as follows:

Table 1 Advantages and disadvantage of each method

| Item                  | Advantage                                                                                                                   | Disadvantage                                                                                                                                                                                                                                                                                                                       |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Manual Tracing**    | - Requires less development resources. - An API can become simpler and consequently the number of bugs can be reduced.      | - Developers must modify the code. - Tracing level is low.                                                                                                                                                                                                                                                                         |
| **Automatic Tracing** | - Developers are not required to modify the code. - More precise data can be collected due to more information in bytecode. | - It would cost 10 times more to develop Pinpoint with automatic method. - Requires highly competent developers who can instantly recognize the library code to be traced and make decisions on the tracing points. - Can increase the possibility of a bug due to high-level development skills such as bytecode instrumentation. |

Bytecode instrumentation is a technique that includes high difficulty level and risks. Nevertheless, using this technique has many benefits.

Although it requires a large number of development resources, it requires almost none for applying the service. For example, the following shows the costs between an automatic method which uses bytecode instrumentation and a manual method which uses libraries (in this context, costs are random numbers assumed for clarity).

* Automatic method: Total of 100
  * Cost of Pinpoint development: 100
  * Cost of services applied: 0
* Manual method: Total of 30
  * Cost of Pinpoint development: 20
  * Cost of services applied: 10

The data above tells us that a manual method is more cost-effective than an automatic one. However, it will not guarantee the same result for NAVER since we have thousands of services. For example, if we have 10 services which require being modified, the total cost will be calculated as follows:

* Cost of Pinpoint development 20 + Cost of services applied 10 x 10 services = 120

As you can see, the automatic method was more cost-efficient for us.

We are lucky to have many developers who are highly competent and specialized in Java in the Pinpoint team. Therefore, we believed it was only a matter of time to overcome the technical difficulties in Pinpoint development.

### The Value of Bytecode Instrumentation

The reason we chose to implement bytecode instrumentation(Automatic method) is not only those that we have already explained but also the following points.

#### Hidden API

If the API is exposed for developers to use. We, as API providers, are restricted to modify the API as we desire. Such a restriction can impose stress on us.

We may modify an API to correct mistaken design or add new functions. However, if there is a restriction to do this, it would be difficult for us to improve the API. The best answer for solving such a problem is a scalable system design, which is not an easy option as everyone knows. It is almost impossible to create perfect API design as we can't predict the future.

With bytecode instrumentation, we don't have to worry about the problems caused by exposing the tracing APIs and can continuously improve the design, without considering dependency relationships. For those who are planning to develop their applications using Pinpoint, please note that API can be changed by the Pinpoint developers since improving performance and design is our first priority.

#### Easy to Enable or Disable

The disadvantage of using bytecode instrumentation is that it could affect your applications when a problem occurs in the profiling section of a library or Pinpoint itself. However, you can easily solve it by just disabling the Pinpoint since you don't have to change any code.

You can easily enable Pinpoint for your applications by adding the three lines (associated with the configuration of the Pinpoint Agent) below into your JVM startup script:

```
-javaagent:$AGENT_PATH/pinpoint-bootstrap-$VERSION.jar
-Dpinpoint.agentId=<Agent's UniqueId>
-Dpinpoint.applicationName=<The name indicating a same service (AgentId collection)>
```

If any problem occurs due to Pinpoint, you can just delete the configuration data in the JVM startup script.

### How Bytecode Instrumentation Works

Since bytecode instrumentation technique has to deal with Java bytecode, it tends to increase the risk of development while it decreases productivity. In addition, developers are prone to make mistakes. In Pinpoint, we improved productivity and accessibility by abstraction with the interceptor. Pinpoint injects necessary codes to track distributed transactions and performance information by intervening application code at class loading time. This increases performance since tracking codes are directly injected into the application code.

![Figure 3. Behavior of bytecode instrumentation](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-609a918a392f37fd672a3b18b908c3fe5575abde%2Ftd_figure3.png?alt=media\&token=3106bb9c-6fa2-4f18-a686-a1c0ca156b77)

Figure 3. Basic principle of bytecode instrumentation

In Pinpoint, the API intercepting part and data recording part are separated. Interceptor is injected into the method that we'd like to track and calls before() and after() methods where data recording is taken care of. Through bytecode instrumentation, Pinpoint Agent can record data only from the necessary method which makes the size of profiling data compact.

## Optimizing Performance of the Pinpoint Agent

Finally, we will describe how to optimize the performance of Pinpoint Agent.

### Using Binary Format (Thrift)

You can increase encoding speed by using a binary format ([Thrift](https://thrift.apache.org/)). Although it is difficult to use and debug, It can improve the efficiency of network usage by reducing the size of data generated.

### Optimize Recorded Data for Variable-Length Encoding and Format

If you convert a long integer into a fixed-length string, the data size will be 8 bytes. However, if you use variable-length encoding, the data size can vary from 1 to 10 bytes depending on the size of a given number. To reduce data size, Pinpoint encodes data as a variable-length string through Compact Protocol of Thrift and records data to be optimized for encoding format. Pinpoint Agent reduces data size by converting remaining time based on root method into a vector value.

> Variable-length encoding
>
> For more information on the variable-length encoding, see "[Base 128 Varints](https://developers.google.com/protocol-buffers/docs/encoding#varints)" in Google Developers.

![Figure 4. Comparison between fixed-length encoding and variable-length encoding](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-4ad3f0fc9dc26c54c3dc86a4851d0261c3252ca6%2Ftd_figure4.png?alt=media\&token=32a56aa3-f5a8-4d30-ba13-d650e3e9356f)

Figure 4. Comparison between fixed-length encoding and variable-length encoding

As you can see in Figure 4, you need to measure the time of 6 different points to get information of when three different methods are called and finished(Figure 4); With fixed-length encoding, this process requires 48 bytes (6points × 8bytes).

Meanwhile, Pinpoint Agent uses variable-length encoding and records the data according to its corresponding format. And calculate time information on other points with the difference(in vector value) based on the start time of the root method. Since vector value is a small number, it consumes a small number of bytes resulting only 13 bytes consumed rather than 48bytes.

If it takes more time to execute a method, it will increase the number of bytes even though variable-length encoding is used. However, it is still more efficient than fixed-length encoding.

### Replacing Repeated API Information, SQLs, and Strings with Constant Tables

We wanted Pinpoint to enable code-level tracing. However, it had a problem in terms of increasing data size. Every time data with a high degree of precision is sent to a server, due to the size of the data it increased network usage.

To solve such a problem, we adopted a strategy by creating a constant table in a remote HBase server. Since there will be an overload to send data of "method A" to Pinpoint Collector each time, Pinpoint Agent converts "method A" data to an ID and stores this information as a constant table in HBase, and continue tracing data with the ID. When a user retrieves trace data on the Website, the Pinpoint Web searches for the method information of the corresponding ID in the constant table and reorganize them. The same way is used to reduce data size in SQLs or frequently-used strings.

### Handling Samples for Bulk Requests

The requests to online portal services which Naver is providing are huge. A single service handles more than 20 billion requests a day. A simple way to trace such request is by expanding network infrastructure and servers as much as needed to suit the number of requests. However, this is not a cost-effective way to handle such situations.

In Pinpoint, you can collect only sampling data rather than tracking every request. In a development environment where requests are few, every data is collected. While in the production environment where requests are large, only 1\~5% out of whole data is collected which is sufficient to analyze the status of entire applications. With sampling, you can minimize network overhead in applications and reduce costs of infrastructure such as networks and servers.

> Sampling method in Pinpoint
>
> Pinpoint supports a Counting sampler, which collects data only for one of 10 requests if it is set to 10. We plan to add new samplers that can collect data more effectively.

### Minimizing Application Threads Being Aborted Using Asynchronous Data Transfer

Pinpoint does not interfere with application threads since encoded data or remote messages are transferred asynchronously by another thread.

#### Transferring Data via UDP

Unlike Google's Dapper, Pinpoint transfers data through a network to ensure data speed. Sharing network with your service can be an issue when data traffic bursts out. In such situations, the Pinpoint Agent starts to use UDP protocol to give the network connection priority to your service.

> Note
>
> The data transfer APIs can be replaced since it's separated as an interface. It can be changed into an implementation that stores data in a different way, like local files.

## Example of Pinpoint Applied

Here is an example of how to get data from your application so that you can comprehensively understand the contents described earlier.

Figure 5 shows what you can see when you install Pinpoint in TomcatA and TomcatB. You can see the trace data of an individual node as a single transaction, which represents the flow of distributed transaction tracing.

![Figure 5. Example 1: Pinpoint applied](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-f9194d26378f10cc869a147b5bec42932e6bad76%2Ftd_figure5.png?alt=media\&token=9166f164-58dc-454a-9b19-67222be27c61)

Figure 5. Example of Pinpoint in action

The following describes what Pinpoint does for each method.

1. Pinpoint Agent issues a TraceId when a request arrives at TomcatA.
   * TX\_ID: TomcatA^TIME^1
   * SpanId: 10
   * ParentSpanId: -1(Root)
2. Records data from Spring MVC controllers.
3. Intervene the calls of HttpClient.execute() method and configure the TraceId in HttpGet.
   * Creates a child TraceId.
     * TX\_ID: TomcatA^TIME^1 -> TomcatA^TIME^1
     * SPAN\_ID: 10 -> 20
     * PARENT\_SPAN\_ID: -1 -> 10 (parent SpanId)
   * Configures the child TraceId in the HTTP header.
     * HttpGet.setHeader(PINPOINT\_TX\_ID, "TomcatA^TIME^1")
     * HttpGet.setHeader(PINPOINT\_SPAN\_ID, "20")
     * HttpGet.setHeader(PINPOINT\_PARENT\_SPAN\_ID, "10")
4. Transfer tagged request to TomcatB.
   * TomcatB checks the header from the transferred request.
     * HttpServletRequest.getHeader(PINPOINT\_TX\_ID)
   * TomcatB becomes a child node as it identifies a TraceId in the header.
     * TX\_ID: TomcatA^TIME^1
     * SPAN\_ID: 20
     * PARENT\_SPAN\_ID: 10
5. Records data from Spring MVC controllers and completes the request.

   ![Figure 6. Example 2: Pinpoint applied](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-ea5417ab1e132ffa795122934391fe7f7c1642c1%2Ftd_figure6.png?alt=media\&token=89e841e9-1ef1-49b5-9445-9c2c29d8cdc9)
6. Pinpoint Agent sends trace data to Pinpoint Collector to store it in HBase when the request from TomcatB is completed.
7. After the HTTP calls from TomcatB is terminated, then the request from TomcatA is complete. The Pinpoint Agent sends trace data to Pinpoint Collector to store it in HBase.
8. UI reads the trace data from HBase and creates a call stack by sorting trees.

## Conclusions

Pinpoint is another application that runs along with your applications. Using bytecode instrumentation makes Pinpoint seem like that it does not require code modifications. In general, the bytecode instrumentation technique makes applications vulnerable to risks; if a problem occurs in Pinpoint, it will affect your applications as well. But for now, instead of getting rid of such threats, we are focusing on improving performance and design of Pinpoint. Because we think this makes Pinpoint more valuable. So whether or not to use Pinpoint is for you to decide.

We still have a large amount of work to be done to improve Pinpoint. Despite its incompleteness, Pinpoint was released as an open-source project; we are continuously trying to develop and improve Pinpoint so as to meet your expectations.

> Written by Woonduk Kang
>
> In 2011, I wrote about myself like this—As a developer, I would like to make a software program that users are willing to pay for, like those of Microsoft or Oracle. As Pinpoint was launched as an open-source project, it seems that my dreams somewhat came true. For now, my desire is to make Pinpoint more valuable and attractive to users.


# Videos

## Speaking at COSCUP2019

Speaking at Taiwan's largest open source conference

Title : [Naver, monitoring services with trillions of event with open source APM, Pinpoint](https://coscup.org/2019/en/programs/naver-monitoring-services-with-trillions-of-event-with-open-source-apm-pinpoint)\
Date : Aug 18, 2019

{% embed url="<https://youtu.be/Uyy:CgRc5:M>" %}

### Speaking at HKOSCon2019

Speaking at HongKong's largest open source conference

Title : [How we started an open source APM project and troubleshooting with it](https://hkoscon.org/2019/topics/how-we-started-open-source-apm-project-and-troubleshooting-it)\
Date : June 15, 2019

{% embed url="<https://youtu.be/9-Kf87k4sEA>" %}

## Introduction to Pinpoint v1.5.0

Video introducing Pinpoint

{% embed url="<https://youtu.be/U4EwnB34Dus>" %}


# Additional Plugins

## Third-party agents/plugins

There may be agents, and plugins that are being developed and managed by other individuals/organizations.

Below include agents and plugins that are not merged into this repository.\
Take a look at them if you are interested and would like to help out.

* Plugins
  * Websphere - <https://github.com/sjmittal/pinpoint/tree/cpu_monitoring_fix/plugins/websphere>
  * RocketMQ - <https://github.com/ruizlake/pinpoint/tree/master/plugins/rocketmq>

If you are working on an agent or a plugin and want to add it to this list, please feel free to [contact us](mailto:roy.kim@navercorp.com) anytime.


# Quick-start guide

Pinpoint QuickStart provides a sample TestApp for the Agent.

## Docker

Installing Pinpoint with these docker files will take approximately 10min.

Visit [Official Pinpoint-Docker repository](https://github.com/pinpoint-apm/pinpoint-docker) for more information.

## Installation

To set up your very own Pinpoint instance you can either **download the build results** from our [**latest release**](https://github.com/pinpoint-apm/pinpoint/releases/latest).

### HBase

Download, Configure, and Start HBase - [1. Hbase](https://pinpoint-apm.gitbook.io/pinpoint/installation#1-hbase).

```
$ tar xzvf hbase-x.x.x-bin.tar.gz
$ cd hbase-x.x.x/
$ ./bin/start-hbase.sh
```

See [scripts](https://github.com/pinpoint-apm/pinpoint/tree/master/hbase/scripts) and Run.

```
$ ./bin/hbase shell hbase-create.hbase
```

### Pinpoint Collector

Download, and Start Collector - [3. Pinpoint Collector](https://pinpoint-apm.gitbook.io/pinpoint/installation#3-pinpoint-collector)

```
$ java -jar -Dpinpoint.zookeeper.address=localhost pinpoint-collector-boot-2.2.1.jar
```

### Pinpoint Web

Download, and Start Web - [4. Pinpoint Web](https://pinpoint-apm.gitbook.io/pinpoint/installation#4-pinpoint-web)

```
$ java -jar -Dpinpoint.zookeeper.address=localhost pinpoint-web-boot-2.2.1.jar
```

## Java Agent

### Requirements

In order to build Pinpoint, the following requirements must be met:

* JDK 8 installed

### When Using Released Binary(Recommended)

Download Pinpoint from [Latest Release](https://github.com/pinpoint-apm/pinpoint/releases/latest).

Extract the downloaded file.

```
$ tar xvzf pinpoint-agent-2.2.1.tar.gz
```

Run the JAR file, as follows:

```
$ java -jar -javaagent:pinpoint-agent-2.2.1/pinpoint-bootstrap.jar -Dpinpoint.agentId=test-agent -Dpinpoint.applicationName=TESTAPP pinpoint-quickstart-testapp-2.2.1.jar
```

### When Building Manually

Download Pinpoint with `git clone https://github.com/pinpoint-apm/pinpoint.git` or [download](https://github.com/pinpoint-apm/pinpoint/archive/master.zip) the project as a zip file and unzip.

Change to the pinpoint directory, and build.

```
$ cd pinpoint
$ ./mvnw install -DskipTests=true
```

Change to the quickstart testapp directory, and build. Let's build and run.

```
$ cd quickstart/testapp
$ ./mvnw clean package
```

Change to the pinpoint directory, and run.

```
$ cd ../../
$ java -jar -javaagent:agent/target/pinpoint-agent-2.2.1/pinpoint-bootstrap.jar -Dpinpoint.agentId=test-agent -Dpinpoint.applicationName=TESTAPP quickstart/testapp/target/pinpoint-quickstart-testapp-2.2.1.jar
```

### Get Started

You should see some output that looks very similar to this:

```
  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::        (v2.3.2.RELEASE)

2020-08-06 17:24:59.519  INFO 19236 --- [           main] com.navercorp.pinpoint.testapp.TestApp   : Starting TestApp on AD01160256 with PID 19236 (C:\repository\github\pinpoint\quickstart\testapp\target\classes started by Naver in C:\repository\github\pinpoint)
2020-08-06 17:24:59.520  INFO 19236 --- [           main] com.navercorp.pinpoint.testapp.TestApp   : No active profile set, falling back to default profiles: default
2020-08-06 17:24:59.520 DEBUG 19236 --- [           main] o.s.boot.SpringApplication               : Loading source class com.navercorp.pinpoint.testapp.TestApp
2020-08-06 17:24:59.558 DEBUG 19236 --- [           main] o.s.b.c.c.ConfigFileApplicationListener  : Loaded config file 'file:/C:/repository/github/pinpoint/quickstart/testapp/target/classes/application.yml' (classpath:/application.yml)
2020-08-06 17:24:59.558 DEBUG 19236 --- [           main] ConfigServletWebServerApplicationContext : Refreshing org.springframework.boot.web.servlet.context.AnnotationConfigServletWebServerApplicationContext@46185a1b
08-06 17:24:59.059 [           main] INFO  .n.p.p.DefaultDynamicTransformerRegistry:67  -- added dynamic transformer classLoader: sun.misc.Launcher$AppClassLoader@18b4aac2, className: com.navercorp.pinpoint.testapp.controller.ApisController, registry size: 1
08-06 17:24:59.059 [           main] INFO  .n.p.p.DefaultDynamicTransformerRegistry:67  -- added dynamic transformer classLoader: sun.misc.Launcher$AppClassLoader@18b4aac2, className: com.navercorp.pinpoint.testapp.controller.CallSelfController, registry size: 2
08-06 17:24:59.059 [           main] INFO  .n.p.p.DefaultDynamicTransformerRegistry:67  -- added dynamic transformer classLoader: sun.misc.Launcher$AppClassLoader@18b4aac2, className: com.navercorp.pinpoint.testapp.controller.HttpClient4Controller, registry size: 3
08-06 17:24:59.059 [           main] INFO  .n.p.p.DefaultDynamicTransformerRegistry:67  -- added dynamic transformer classLoader: sun.misc.Launcher$AppClassLoader@18b4aac2, className: com.navercorp.pinpoint.testapp.controller.SimpleController, registry size: 4
08-06 17:24:59.059 [           main] INFO  .n.p.p.DefaultDynamicTransformerRegistry:67  -- added dynamic transformer classLoader: sun.misc.Launcher$AppClassLoader@18b4aac2, className: com.navercorp.pinpoint.testapp.controller.StressController, registry size: 5
2020-08-06 17:25:00.313 DEBUG 19236 --- [           main] .s.b.w.e.t.TomcatServletWebServerFactory : Code archive: C:\Users\Naver\.m2\repository\org\springframework\boot\spring-boot\2.3.2.RELEASE\spring-boot-2.3.2.RELEASE.jar
2020-08-06 17:25:00.313 DEBUG 19236 --- [           main] .s.b.w.e.t.TomcatServletWebServerFactory : Code archive: C:\Users\Naver\.m2\repository\org\springframework\boot\spring-boot\2.3.2.RELEASE\spring-boot-2.3.2.RELEASE.jar
2020-08-06 17:25:00.314 DEBUG 19236 --- [           main] .s.b.w.e.t.TomcatServletWebServerFactory : None of the document roots [src/main/webapp, public, static] point to a directory and will be ignored.
2020-08-06 17:25:00.347  INFO 19236 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 8082 (http)
2020-08-06 17:25:00.355  INFO 19236 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2020-08-06 17:25:00.356  INFO 19236 --- [           main] org.apache.catalina.core.StandardEngine  : Starting Servlet engine: [Apache Tomcat/9.0.37]
```

The last couple of lines here tell us that Spring has started. Spring Boot’s embedded Apache Tomcat server is acting as a webserver and is listening for requests on localhost port 8082. Open your browser and in the address bar at the top enter <http://localhost:8082>


# quickstart.Win.en


# quickstart.Win.ko


# Installation guide

To set up your very own Pinpoint instance you can either **download the build results** from our [**latest release**](https://github.com/pinpoint-apm/pinpoint/releases/latest), or manually build from your Git clone. In order to run your own Pinpoint instance, you will need to run below components:

* **HBase** (for storage)
* **Pinot** (for storage)
* **Pinpoint Collector** (deployed on a web container)
* **Pinpoint Web** (deployed on a web container)
* **Pinpoint Agent** (attached to a java application for profiling)

To try out a simple quickstart project, please refer to the [quick-start guide](https://pinpoint-apm.gitbook.io/pinpoint/getting-started/quickstart).

### Apple silicon(M1/M2) build failures

If an error `protoc-gen-grpc-java-1.49.2-osx-aarch_64.exe: program not found or is not executable` occurs in the Apple silicon Mac (M1/M2) development environment, it has to install Rosetta.

```
$> softwareupdate --install-rosetta --agree-to-license
```

## Quick Overview of Installation

1. HBase ([details](#1-hbase))
   1. Set up HBase cluster - [Apache HBase](http://hbase.apache.org)
   2. Create HBase Schemas - feed `/scripts/hbase-create.hbase` to hbase shell.
2. Pinot ([details](#2-pinot))
   1. Set up Pinot - [Apache Pinot](https://pinot.apache.org)
   2. Set up Kafka - [Apache Kafka](https://kafka.apache.org)
   3. Create Kafka topics and Pinot tables. Refer to the documentation for the features you are using.
      * [New Inspector](https://pinpoint-apm.gitbook.io/pinpoint/documents/new-inspector)
      * [System Metric](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric)
      * [URI Statistics](https://pinpoint-apm.gitbook.io/pinpoint/documents/uri_statistics)
      * [Error Analysis](https://pinpoint-apm.gitbook.io/pinpoint/documents/error_analysis)
3. Build Pinpoint (Optional)([details](#3-building-pinpoint)) - No need if you use the binaries.([here](https://github.com/pinpoint-apm/pinpoint/releases)). 4. Clone Pinpoint - `git clone $PINPOINT_GIT_REPOSITORY` 5. Set JAVA\_HOME environment variable to JDK 8 home directory. 6. Set JAVA\_8\_HOME environment variable to JDK 8 home directory. 7. Set JAVA\_11\_HOME environment variable to JDK 11 home directory. 8. Set JAVA\_17\_HOME environment variable to JDK 17 home directory. 9. Run `./mvnw clean install -DskipTests=true` (or `./mvnw.cmd` for Windows)
4. Pinpoint Collector ([details](#4-pinpoint-collector)) 1. Start *pinpoint-collector-boot-$VERSION.jar* with java -jar command.

   ```
    java -jar -Dpinpoint.zookeeper.address=localhost pinpoint-collector-boot-$VERSION.jar
   ```

   * It will start with default settings. To learn more about default values or how to override them, please see the details below.
   * Use [collector starter](#collector-starter) to connect to Pinot and Kafka
5. Pinpoint Web ([details](#5-pinpoint-web)) 1. Start *pinpoint-web-boot-$VERSION.jar* with java -jar command.

   ```
    java -jar -Dpinpoint.zookeeper.address=localhost pinpoint-web-boot-$VERSION.jar
   ```

   * It will start with default settings. To learn more about default values or how to override them, please see the details below.
   * Use [web starter](#web-starter) to connect to Pinot
6. Pinpoint Agent ([details](#6-pinpoint-agent))
   1. Extract/move *pinpoint-agent/* to a convenient location (`$AGENT_PATH`).
   2. Set `-javaagent:$AGENT_PATH/pinpoint-bootstrap-$VERSION.jar` JVM argument to attach the agent to a java application.
   3. Set `-Dpinpoint.agentId` and `-Dpinpoint.applicationName` command-line arguments.
      * If you're launching an agent in a containerized environment with dynamically changing *agent id*, consider adding `-Dpinpoint.container` command-line argument.
   4. Set `-Dprofiler.sampling.type=PERCENT` and `-Dprofiler.sampling.percent.sampling-rate=100` command-line arguments.
      * You can adjust the sampling rate with the above option.
   5. Launch java application with the options above.

## 1. HBase

Pinpoint uses HBase as its storage backend for the Collector and the Web.

To set up your own cluster, take a look at the [HBase website](http://hbase.apache.org) for instructions. The HBase compatibility table is given below:

Once you have HBase up and running, make sure the Collector and the Web are configured properly and are able to connect to HBase.

### Creating Schemas for HBase

There are 2 scripts available to create tables for Pinpoint: *hbase-create.hbase*, and *hbase-create-snappy.hbase*. Use *hbase-create-snappy.hbase* for snappy compression (requires [snappy](http://google.github.io/snappy/)), otherwise use *hbase-create.hbase* instead.

To run these scripts, feed them into the HBase shell like below:

`$HBASE_HOME/bin/hbase shell hbase-create.hbase`

See [here](https://github.com/pinpoint-apm/pinpoint/tree/master/hbase/scripts) for a complete list of scripts.

## 2. Pinot

Pinpoint uses Pinot for metric data storage, and Kafka is required for [Pinot stream ingestion](https://docs.pinot.apache.org/basics/data-import/pinot-stream-ingestion/import-from-apache-kafka)

Here are documents for Installing Pinot and Kafka

* Install Pinot following the instructions in [Pinot Getting Started guide](https://docs.pinot.apache.org/basics/getting-started)
  * Above guide provides instructions for running Pinot locally, in Docker, and in Kubernetes.
* Install Kafka by referring to [Kafka quickstart](https://kafka.apache.org/quickstart)

Once Pinot is up and running, ensure that the [collector starter](#collector-starter) and the [web starter](#web-starter) are properly configured and able to connect to Pinot.

### Creating Pinot tables

Please refer to the documentation to create Kafka topics and Pinot tables for Pinot-related feature.

The descriptions for the required Kafka topics and Pinot tables are provided in the following feature documents

* [New Inspector](https://pinpoint-apm.gitbook.io/pinpoint/documents/new-inspector)
* [System Metric](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric)
* [URI Statistics](https://pinpoint-apm.gitbook.io/pinpoint/documents/uri_statistics)
* [Error Analysis](https://pinpoint-apm.gitbook.io/pinpoint/documents/error_analysis)

## 3. Building Pinpoint

There are two options:

1. Download the build results from our [**latest release**](https://github.com/pinpoint-apm/pinpoint/releases/latest) and skip building process. **(Recommended)**
2. Build Pinpoint manually from the Git clone. **(Optional)**

   In order to do so, the following **requirements** must be met:

   * JDK 8 installed
   * JDK 11 installed
   * JDK 17 installed
   * JAVA\_HOME environment variable set to JDK 8 home directory.
   * JAVA\_8\_HOME environment variable set to JDK 8 home directory.
   * JAVA\_11\_HOME environment variable set to JDK 11 home directory.
   * JAVA\_17\_HOME environment variable set to JDK 17 home directory.

     Agent compatibility to Collector table:

     Once the above requirements are met, simply run the command below (you may need to add permission for **mvnw** so that it can be executed) :

     `./mvnw install -DskipTests=true`

     The default agent built this way will have log level set to DEBUG by default. If you're building an agent for release and need a higher log level, you can set maven profile to *release* when building :\
     `./mvnw install -Prelease -DskipTests=true`

     Note that having multibyte characters in maven local repository path, or any class paths may cause the build to fail.

     The guide will refer to the full path of the pinpoint home directory as `$PINPOINT_PATH`.

Regardless of your method, you should end up with the files and directories mentioned in the following sections.

## 4. Pinpoint Collector

You should have the following **executable jar** file.

*pinpoint-collector-boot-$VERSION.jar*

The path to this file should look like *$PINPOINT\_PATH/collector/target/deploy/pinpoint-collector-boot-$VERSION.jar* if you built it manually.

### Installation

Since Pinpoint Collector is packaged as an executable jar file, you can start Collector by running it directly.

e.g.) `java -jar -Dpinpoint.zookeeper.address=localhost pinpoint-collector-boot-$VERSION.jar`

### Configuration

There are 2 configuration files used for Pinpoint Collector: *pinpoint-collector-grpc.properties*, and *hbase.properties*.

* pinpoint-collector-grpc.properties - contains configurations for the grpc.
  * `collector.receiver.grpc.agent.port` (agent's *profiler.transport.grpc.agent.collector.port*, *profiler.transport.grpc.metadata.collector.port* - default: 9991/TCP)
  * `collector.receiver.grpc.stat.port` (agent's *profiler.transport.grpc.stat.collector.port* - default: 9992/TCP)
  * `collector.receiver.grpc.span.port` (agent's *profiler.transport.grpc.span.collector.port* - default: 9993/TCP)
* hbase.properties - contains configurations to connect to HBase.
  * `hbase.client.host` (default: localhost)
  * `hbase.client.port` (default: 2181)

You may take a look at the full list of default configurations here:

* [pinpoint-collector-grpc.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/collector/src/main/resources/profiles/local/pinpoint-collector-grpc.properties)
* [hbase.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/collector/src/main/resources/profiles/local/hbase.properties)

#### When Building Manually

You can modify default configuration values or add new profiles under `collector/src/main/resources/profiles/`.

#### When Using Released Binary **(Recommended)**

* You can override any configuration values with `-D` option. For example,
  * `java -jar -Dspring.profiles.active=release -Dpinpoint.zookeeper.address=localhost -Dhbase.client.port=1234 pinpoint-collector-boot-$VERSION.jar`
* To import a list of your customized configuration values from a file, you can use `--spring.config.additional-location` option. For example,
  * Create a file `./config/collector.properties`, and list the configuration values you want to override. >

    > spring.profiles.active=release
    >
    > pinpoint.zookeeper.address=localhost
    >
    > collector.receiver.grpc.agent.port=9999
    >
    > collector.receiver.stat.udp.receiveBufferSize=1234567
  * Execute with `java -jar pinpoint-collector-boot-$VERSION.jar --spring.config.additional-location=./config/collector.properties`
* To further explore how to use externalized configurations, refer to [Spring Boot Reference Document](https://docs.spring.io/spring-boot/docs/2.2.x/reference/html/spring-boot-features.html#boot-features-external-config-application-property-files).

### Profiles

Pinpoint Collector provides two profiles: [release](https://github.com/pinpoint-apm/pinpoint/tree/master/collector/src/main/resources/profiles/release) and [local](https://github.com/pinpoint-apm/pinpoint/tree/master/collector/src/main/resources/profiles/local) (default).

To specify which profile to use, configure `spring.profiles.active` value as described in the previous section.

#### Adding a custom profile

To add a custom profile, you need to rebuild `pinpoint-collector` module.

1. Add a new folder under `collector/src/main/resources/profiles` with a profile name.
2. Copy files from local or release profiles folder, and modify configuration values as needed.
3. To use the new profile, rebuild `pinpoint-collector` module and configure `spring.profiles.active` as described in the previous section.

When using released binary, you cannot add a custom profile. Instead, you can manage your configuration values in separate files and use them to override default values as described in the [previous section](#3-pinpoint-collector).

### Collector Starter

To utilize Pinot-related features, you need to execute with Pinpoint Collector starter.

Since the `collector-starter` is packaged as an executable jar file, you can start the `collector-starter` with the following command to override Zookeeper, Kafka and Pinot properties.

```
java -jar -Dspring.config.additional-location=collector-starter-application.yml pinpoint-collector-starter-boot-$VERSION.jar
```

* collector-starter-application.yml

```
pinpoint:
  zookeeper:
    address: localhost
  metric:
    kafka:
      bootstrap:
        servers: localhost:19092
spring:
  pinot-datasource:
    pinot:
      jdbc-url: jdbc:pinot://localhost:9000
      username: --username--
      password: --password--
```

## 5. Pinpoint Web

You should have the following **executable jar** file.

*pinpoint-web-boot-$VERSION.jar*

The path to this file should look like *$PINPOINT\_PATH/web/target/deploy/pinpoint-web-boot-$VERSION.jar* if you built it manually.

Pinpoint Web Supported Browsers:

* Chrome

### Installation

Since Pinpoint Web is packaged as an executable jar file, you can start Web by running it directly.

```
java -jar -Dpinpoint.zookeeper.address=localhost pinpoint-web-boot-$VERSION.jar
```

### Configuration

There are 2 configuration files used for Pinpoint Web: *pinpoint-web-root.properties*, and *hbase.properties*.

* hbase.properties - contains configurations to connect to HBase.
  * `hbase.client.host` (default: localhost)
  * `hbase.client.port` (default: 2181)

You may take a look at the default configuration files here

* [pinpoint-web-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/pinpoint-web-root.properties)
* [hbase.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/profiles/release/hbase.properties)
* [pinpoint-web.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/profiles/release/pinpoint-web.properties)

#### When Building Manually

You can modify default configuration values or add new profiles under `web/src/main/resources/profiles/`.

#### When Using Released Binary **(Recommended)**

* You can override any configuration values with `-D` option. For example,
  * `java -jar -Dspring.profiles.active=release -Dpinpoint.zookeeper.address=localhost -Dhbase.client.port=1234 pinpoint-web-boot-$VERSION.jar`
* To import a list of your customized configuration values from a file, you can use `--spring.config.additional-location` option. For example,
  * Create a file `./config/web.properties`, and list the configuration values you want to override. >

    > spring.profiles.active=release
    >
    > pinpoint.zookeeper.address=localhost
    >
    > cluster.zookeeper.sessiontimeout=10000
  * Execute with `java -jar pinpoint-web-boot-$VERSION.jar --spring.config.additional-location=./config/web.properties`
* To further explore how to use externalized configurations, refer to [Spring Boot Reference Document](https://docs.spring.io/spring-boot/docs/2.2.x/reference/html/spring-boot-features.html#boot-features-external-config-application-property-files).

### Profiles

Pinpoint Web provides two profiles: [release](https://github.com/pinpoint-apm/pinpoint/tree/master/web/src/main/resources/profiles/release) (default) and [local](https://github.com/pinpoint-apm/pinpoint/tree/master/web/src/main/resources/profiles/local).

To specify which profile to use, configure `spring.profiles.active` value as described in the previous section.

#### Adding a custom profile

To add a custom profile, you need to rebuild `pinpoint-web` module.

1. Add a new folder under `web/src/main/resources/profiles` with a profile name.
2. Copy files from local or release profiles folder, and modify configuration values as needed.
3. To use the new profile, rebuild `pinpoint-web` module and configure `spring.profiles.active` as described in the previous section.

When using released binary, you cannot add a custom profile. Instead, you can manage your configuration values in separate files and use them to override default values as described in the [previous section](#4-pinpoint-web).

### Web Starter

To utilize Pinot-related features, you need to execute with Pinpoint Web Starter.

Since the `web-starter` is packaged as an executable jar file, you can start the `web-starter` with the following command to override Zookeeper and Pinot properties.

```
java -jar -Dspring.config.additional-location=web-starter-application.yml pinpoint-web-starter-boot-$VERSION.jar
```

* web-starter-application.yml

```
pinpoint:
  zookeeper:
    address: localhost
spring:
  pinot-datasource:
    pinot:
      jdbc-url: jdbc:pinot://localhost:9000
      username: --username--
      password: --password--
```

## 6. Pinpoint Agent

If downloaded, unzip the Pinpoint Agent file. You should have a **pinpoint-agent** directory with the layout below :

```
pinpoint-agent
|-- boot
|   |-- pinpoint-annotations-$VERSION.jar
|   |-- pinpoint-bootstrap-core-$VERSION.jar
|   |-- pinpoint-bootstrap-java8-$VERSION.jar
|   |-- pinpoint-bootstrap-java9-$VERSION.jar
|   |-- pinpoint-commons-$VERSION.jar
|-- lib
|   |-- pinpoint-profiler-$VERSION.jar
|   |-- pinpoint-profiler-optional-$VERSION.jar
|   |-- pinpoint-rpc-$VERSION.jar
|   |-- pinpoint-thrift-$VERSION.jar
|   |-- ...
|-- plugin
|   |-- pinpoint-activemq-client-plugin-$VERSION.jar
|   |-- pinpoint-tomcat-plugin-$VERSION.jar
|   |-- ...
|-- profiles
|   |-- local
|   |   |-- pinpoint.config
|   |-- release
|       |-- pinpoint.config
|-- log4j2-agent.xml
|-- pinpoint-bootstrap-$VERSION.jar
|-- pinpoint-root.config
```

The path to this directory should look like *$PINPOINT\_PATH/agent/target/pinpoint-agent* if you built it manually.

You may move/extract the contents of **pinpoint-agent** directory to any location of your choice. The guide will refer to the full path of this directory as `$AGENT_PATH`.

> Note that you may change the agent's log level by modifying the *log4j.xml* located in the *profiles/$PROFILE/log4j.xml* directory above.

Agent compatibility to Collector table:

### Installation

Pinpoint Agent runs as a java agent attached to an application to be profiled (such as Tomcat).

To wire up the agent, pass *$AGENT\_PATH/pinpoint-bootstrap-$VERSION.jar* to the *-javaagent* JVM argument when running the application:

* `-javaagent:$AGENT_PATH/pinpoint-bootstrap-$VERSION.jar`

Additionally, Pinpoint Agent requires 2 command-line arguments in order to identify itself in the distributed system:

* `-Dpinpoint.agentId` - uniquely identifies the application instance in which the agent is running on
* `-Dpinpoint.applicationName` - groups a number of identical application instances as a single service

Note that *pinpoint.agentId* must be globally unique to identify an application instance, and all applications that share the same *pinpoint.applicationName* are treated as multiple instances of a single service.

* `-Dprofiler.sampling.type=PERCENT` - sampler type
* `-Dprofiler.sampling.percent.sampling-rate=100` - support from 100% to 0.01%

If you're launching the agent in a containerized environment, you might have set your *agent id* to be auto-generated every time the container is launched. With frequent deployment and auto-scaling, this will lead to the Web UI being cluttered with all the list of agents that were launched and destroyed previously. For such cases, you might want to add `-Dpinpoint.container` in addition to the 2 required command-line arguments above when launching the agent.

**Tomcat Example**

Add *-javaagent*, *-Dpinpoint.agentId*, *-Dpinpoint.applicationName* to *CATALINA\_OPTS* in the Tomcat startup script (*catalina.sh*).

```
CATALINA_OPTS="$CATALINA_OPTS -javaagent:$AGENT_PATH/pinpoint-bootstrap-$VERSION.jar"
CATALINA_OPTS="$CATALINA_OPTS -Dpinpoint.agentId=$AGENT_ID"
CATALINA_OPTS="$CATALINA_OPTS -Dpinpoint.applicationName=$APPLICATION_NAME"
```

Start up Tomcat to start profiling your web application.

Some application servers require additional configuration and/or may have caveats. Please take a look at the links below for further details.

* [JBoss](https://github.com/pinpoint-apm/pinpoint/blob/master/agent-module/plugins/jboss/README.md)
* [Jetty](https://github.com/pinpoint-apm/pinpoint/blob/master/agent-module/plugins/jetty/README.md)
* [Other Application Servers](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins)

### Configuration

There are various configuration options for Pinpoint Agent available in *$AGENT\_PATH/pinpoint-root.config*.

Most of these options are self explanatory, but the most important configuration options you must check are **Collector ip address**, and the **TCP/UDP ports**. These values are required for the agent to establish connection to the *Collector* and function correctly.

Set these values appropriately in *pinpoint-root.config*:

**GRPC**

* `profiler.transport.grpc.collector.ip` (default: 127.0.0.1)
* `profiler.transport.grpc.agent.collector.port` (collector's *collector.receiver.grpc.agent.port* - default: 9991/TCP)
* `profiler.transport.grpc.metadata.collector.port` (collector's *collector.receiver.grpc.agent.port* - default: 9991/TCP)
* `profiler.transport.grpc.stat.collector.port` (collector's *collector.receiver.grpc.stat.port* - default: 9992/TCP)
* `profiler.transport.grpc.span.collector.port` (collector's *collector.receiver.grpc.span.port* - default: 9993/TCP)

You may take a look at the default *pinpoint-root.config* file [here](https://github.com/pinpoint-apm/pinpoint/blob/master/agent/src/main/resources/pinpoint-root.config) along with all the available configuration options.

### Profiles

Add `-Dkey=value` to Java System Properties

* $PINPOINT\_AGENT\_DIR/profiles/$PROFILE
  * `-Dpinpoint.profiler.profiles.active=release or local`
  * Modify `pinpoint.profiler.profiles.active=release` in $PINPOINT\_AGENT\_DIR/pinpoint-root.config
  * Default profile : `release`
* Custom Profile
  1. Create a custom profile in $PINPOINT\_AGENT\_HOME/profiles/MyProfile
     * Add pinpoint.config & log4j.xml
  2. Add `-Dpinpoint.profiler.profiles.active=MyProfile`
* Support external config
  * `-Dpinpoint.config=$MY_EXTERNAL_CONFIG_PATH`

## Miscellaneous

### HBase region servers hostname resolution

Please note that collector/web must be able to resolve the hostnames of HBase region servers. This is because HBase region servers are registered to ZooKeeper by their hostnames, so when the collector/web asks ZooKeeper for a list of region servers to connect to, it receives their hostnames. Please ensure that these hostnames are in your DNS server, or add these entries to the collector/web instances' *hosts* file.

### Routing Web requests to Agents

Starting from 1.5.0, Pinpoint can send requests from the Web to Agents directly via the Collector (and vice-versa). To make this possible, we use Zookeeper to co-ordinate the communication channels established between Agents and Collectors, and those between Collectors and Web instances. With this addition, real-time communication (for things like active thread count monitoring) is now possible.

We typically use the Zookeeper instance provided by the HBase backend so no additional Zookeeper configuration is required. Related configuration options are shown below.

* **Collector** - *pinpoint-collector.properties*
  * `cluster.enable`
  * `cluster.zookeeper.address`
  * `cluster.zookeeper.sessiontimeout`
  * `cluster.listen.ip`
  * `cluster.listen.port`
* **Web** - *pinpoint-web.properties*
  * `cluster.enable`
  * `cluster.web.tcp.port`
  * `cluster.zookeeper.address`
  * `cluster.zookeeper.sessiontimeout`
  * `cluster.zookeeper.retry.interval`
  * `cluster.connect.address`


# Install with Docker

We've create docker files to support docker.\
Installing Pinpoint with these docker files will take approximately 10min. to check out the features of Pinpoint.

Visit [Official Pinpoint-Docker repository](https://github.com/pinpoint-apm/pinpoint-docker) for more information.


# TrobleShooting(Network)

## Checking network configuration

We provide a simple tool that can check your network configurations.\
This tool checks the network status between Pinpoint-Agent and Pinpoint-Collector

## Testing with binary release

If you have downloaded the build results from our [**latest release**](https://github.com/pinpoint-apm/pinpoint/releases/latest).

1. Start your collector server
2. With any terminal that you are using, go to *script* folder which is under *pinpoint-agent-VERSION.tar.gz* package that you have downloaded.

```
> pwd
/Users/user/Downloads/pinpoint-agent-1.7.2-SNAPSHOT/script
```

and run *networktest.sh* shell script

```
> sh networktest.sh
```

You will see some CLASSPATH and configuration you have made in the *pinpoint.config* file as below

```
CLASSPATH=./tools/pinpoint-tools-1.7.2-SNAPSHOT.jar
...Remainder Omitted...
2018-04-10 17:36:30 [INFO ](com.navercorp.pinpoint.bootstrap.config.DefaultProfilerConfig) profiler.enable=true
2018-04-10 17:36:30 [INFO ](com.navercorp.pinpoint.bootstrap.config.DefaultProfilerConfig) profiler.instrument.engine=ASM
2018-04-10 17:36:30 [INFO ](com.navercorp.pinpoint.bootstrap.config.DefaultProfilerConfig) profiler.instrument.matcher.enable=true
...Remainder Omitted...
```

And after that, you will see the results. (In this case, collector server was started locally) If you receive all six SUCCESSes as below, then you are all set and ready to go.

```
UDP-STAT:// localhost
    => 127.0.0.1:9995 [SUCCESS]
    => 0:0:0:0:0:0:0:1:9995 [SUCCESS]

UDP-SPAN:// localhost
    => 127.0.0.1:9996 [SUCCESS]
    => 0:0:0:0:0:0:0:1:9996 [SUCCESS]

TCP:// localhost
    => 127.0.0.1:9994 [SUCCESS]
    => 0:0:0:0:0:0:0:1:9994 [SUCCESS]
```

## Testing with source code

The idea is basically the same.

1. Start your collector server
2. Pass the *path* of the pinpoint.config file as a *program argument* and run ***NetworkAvailabilityChecker*** class.
3. (only for under v1.7.2)For the few who gets JNI error while running. Please remove `<scope>provided</scope>` line from pom.xml under *tools* module and try again

Results should be same as shown above.

> If you face error for v1.7.3 take a look at this [issue](https://github.com/pinpoint-apm/pinpoint/issues/4668)


# Plugin Developer Guide

You can write Pinpoint profiler plugins to extend profiling target coverage. It is highly advisable to look into the trace data recorded by pinpoint plugins before jumping into plugin development.

* There is a [fast auto pinpoint agent plugin generate tool](https://github.com/bbossgroups/pinpoint-plugin-generate) from a 3rd party for creating a simple plug-in, if you'd like to check out.

## I. Trace Data

In Pinpoint, a transaction consists of a group of `Spans`. Each `Span` represents a trace of a single logical node where the transaction has gone through.

To aid in visualization, let's suppose that there is a system like below. The *FrontEnd* server receives requests from users, then sends request to the *BackEnd* server, which queries a DB. Among these nodes, let's assume only the *FrontEnd* and *BackEnd* servers are profiled by the Pinpoint Agent.

![trace](https://user-images.githubusercontent.com/10043788/133535491-adafcd89-c04e-49af-9ad7-f7746bb9c95c.PNG)

When a request arrives at the *FrontEnd* server, Pinpoint Agent generates a new transaction id and creates a `Span` with it. To handle the request, the *FrontEnd* server then invokes the *BackEnd* server. At this point, Pinpoint Agent injects the transaction id (plus a few other values for propagation) into the invocation message. When the *BackEnd* server receives this message, it extracts the transaction id (and the other values) from the message and creates a new `Span` with them. Resulting, all `Spans` in a single transaction share the same transaction id.

A `Span` records important method invocations and their related data(arguments, return value, etc) before encapsulating them as `SpanEvents` in a call stack like representation. The `Span` itself and each of its `SpanEvents` represents a method invocation.

`Span` and `SpanEvent` have many fields, but most of them are handled internally by Pinpoint Agent and most plugin developers won't need to worry about them. But the fields and data that must be handled by plugin developers will be listed throughout this guide.

## II. Pinpoint Plugin Structure

Pinpoint plugin consists of *type-provider.yml* and `ProfilerPlugin` implementations. *type-provider.yml* defines the `ServiceTypes` and `AnnotationKeys` that will be provided by the plugin, and provides them to Pinpoint Agent, Web and Collector. `ProfilerPlugin` implementations are used by Pinpoint Agent to transform target classes to record trace data.

Plugins are deployed as jar files. These jar files are packaged under the *plugin* directory for the agent, while the collector and web have them deployed under *WEB-INF/lib*. On start up, Pinpoint Agent, Collector, and Web iterates through each of these plugins; parses *type-provider.yml*, and loads `ProfilerPlugin` implementations using `ServiceLoader` from the following locations:

* META-INF/pinpoint/type-provider.yml
* META-INF/services/com.navercorp.pinpoint.bootstrap.plugin.ProfilerPlugin

Here is a [template plugin project](https://github.com/pinpoint-apm/pinpoint-plugin-template) you can use to start creating your own plugin.

### 1. type-provider.yml

*type-provider.yml* defines the `ServiceTypes` and `AnnotationKeys` that will be used by the plugin and provided to the agent, collector and web; the format of which is outlined below.

```yaml
serviceTypes:
    - code: <short>
      name: <String>
      desc: <String>   # May be omitted, defaulting to the same value as name.
      property:        # May be omitted, all properties defaulting to false.
          terminal: <boolean>               # May be omitted, defaulting to false.
          queue: <boolean>                  # May be omitted, defaulting to false.
          recordStatistics: <boolean>       # May be omitted, defaulting to false.
          includeDestinationId: <boolean>   # May be omitted, defaulting to false.
          alias: <boolean>                  # May be omitted, defaulting to false.          
      matcher:         # May be omitted
          type: <String>   # Any one of 'args', 'exact', 'none'
          code: <int>      # Annotation key code - required only if type is 'exact'

annotationKeys:
    - code: <int>
      name: <String>
      property:        # May be omitted, all properties defaulting to false.
          viewInRecordSet: <boolean>
```

`ServiceType` and `AnnotationKey` defined here are instantiated when the agent loads, and can be obtained using `ServiceTypeProvider` and `AnnotationKeyProvider` like below.

```java
// ServiceType
ServiceType serviceType = ServiceTypeProvider.getByCode(1000);    // by ServiceType code
ServiceType serviceType = ServiceTypeProvider.getByName("NAME");  // by ServiceType name
// AnnotationKey
AnnotationKey annotationKey = AnnotationKeyProvider.getByCode("100");
```

#### 1.1 ServiceType

Every `Span` and `SpanEvent` contains a `ServiceType`. The `ServiceType` represents which library the traced method belongs to, as well as how the `Span` and `SpanEvent` should be handled.

The table below shows the `ServiceType`'s properties.

| property   | description                                                |
| ---------- | ---------------------------------------------------------- |
| name       | name of the `ServiceType`. Must be unique                  |
| code       | short type code value of the `ServiceType`. Must be unique |
| desc       | description                                                |
| properties | properties                                                 |

`ServiceType` code must use a value from its appropriate category. The table below shows these categories and their range of codes.

| category     | range        |
| ------------ | ------------ |
| Internal Use | 0 \~ 999     |
| Server       | 1000 \~ 1999 |
| DB Client    | 2000 \~ 2999 |
| Cache Client | 8000 \~ 8999 |
| RPC Client   | 9000 \~ 9999 |
| Others       | 5000 \~ 7999 |

`ServiceType` code must be unique. Therefore, if you are writing a plugin that will be shared publicly, **you must** contact Pinpoint dev. team to get a `ServiceType` code assigned. If your plugin is for private use, you may freely pick a value for `ServiceType` code from the table below.

| category     | range        |
| ------------ | ------------ |
| Server       | 1900 \~ 1999 |
| DB client    | 2900 \~ 2999 |
| Cache client | 8900 \~ 8999 |
| RPC client   | 9900 \~ 9999 |
| Others       | 7500 \~ 7999 |

`ServiceTypes` can have the following properties.

| property                 | description                                                                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TERMINAL                 | This `Span` or `SpanEvent` invokes a remote node but the target node is not traceable with Pinpoint                                                           |
| QUEUE                    | This `Span` or `SpanEvent` consumes/produces a message from/to a message queue.                                                                               |
| INCLUDE\_DESTINATION\_ID | This `Span` or `SpanEvent` records a `destination id` and remote server is not a traceable type.                                                              |
| RECORD\_STATISTICS       | Pinpoint Collector should collect execution time statistics of this `Span` or `SpanEvent`                                                                     |
| ALIAS                    | The service may or may not have Pinpoint-Agent attached at the following service but regardlessly have knowledge what will follow. (Ex. Elasticsearch client) |

#### 1.2 AnnotationKey

You can annotate spans and span events with more information. An **Annotation** is a key-value pair where the key is an `AnnotationKey` type and the value is a primitive type, String or a byte\[]. There are pre-defined `AnnotationKeys` for commonly used annotation types, but you can define your own keys in *type-provider.yml* if these are not enough.

| property   | description                                                 |
| ---------- | ----------------------------------------------------------- |
| name       | Name of the `AnnotationKey`                                 |
| code       | int type code value of the `AnnotationKey`. Must be unique. |
| properties | properties                                                  |

If you are writing a plugin for public use, and are looking to add a new `AnnotationKey`, you must contact the Pinpoint dev. team to get an `AnnotationKey` code assigned. If your plugin is for private use, you may pick a value between 900 to 999 safely to use as `AnnotationKey` code.

The table below shows the `AnnotationKey` properties.

| property              | description                                    |
| --------------------- | ---------------------------------------------- |
| VIEW\_IN\_RECORD\_SET | Show this annotation in transaction call tree. |
| ERROR\_API\_METADATA  | This property is not for plugins.              |

#### Example

You can find *type-provider.yml* sample [here](https://github.com/pinpoint-apm/pinpoint-plugin-sample/blob/master/plugins/sample/src/main/resources/META-INF/pinpoint/type-provider.yml).

You may also define and attach an `AnnotationKeyMatcher` with a `ServiceType` (`matcher` element in the sample *type-provider* code above). If you attach an `AnnotationKeyMatcher` this way, matching annotations will be displayed as representative annotation when the `ServiceType`'s `Span` or `SpanEvent` is displayed in the transaction call tree.

### 2. ProfilerPlugin

`ProfilerPlugin` modifies target library classes to collect trace data.

`ProfilerPlugin` works in the order of following steps:

1. Pinpoint Agent is started when the JVM starts.
2. Pinpoint Agent loads all plugins under `plugin` directory.
3. Pinpoint Agent invokes `ProfilerPlugin.setup(ProfilerPluginSetupContext)` for each loaded plugin.
4. In the `setup` method, the plugin registers a `TransformerCallback` to all classes that are going to be transformed.
5. Target application starts.
6. Every time a class is loaded, Pinpoint Agent looks for the `TransformerCallback` registered to the class.
7. If a `TransformerCallback` is registered, the Agent invokes it's `doInTransform` method.
8. `TransformerCallback` modifies the target class' byte code. (e.g. add interceptors, add fields, etc.)
9. The modified byte code is returned to the JVM, and the class is loaded with the returned byte code.
10. Application continues running.
11. When a modified method is invoked, the injected interceptor's `before` and `after` methods are invoked.
12. The interceptor records the trace data.

The most important points to consider when writing a plugin are 1) figuring out which methods are interesting enough to warrant tracing, and 2) injecting interceptors to actually trace these methods. These interceptors are used to extract, store, and pass trace data around before they are sent off to the Collector. Interceptors may even cooperate with each other, sharing context between them. Plugins may also aid in tracing by adding getters or even custom fields to the target class so that the interceptors may access them during execution. [Pinpoint plugin sample](https://github.com/pinpoint-apm/pinpoint-plugin-sample) shows you how the `TransformerCallback` modifies classes and what the injected interceptors do to trace a method.

We will now describe what interceptors must do to trace different kinds of methods.

#### 2.1 Plain method

*Plain method* refers to anything that is not a top-level method of a node, or is not related to remote or asynchronous invocation. [Sample 2](https://github.com/pinpoint-apm/pinpoint-plugin-sample/tree/master/plugins/sample/src/main/java/com/navercorp/pinpoint/plugin/sample/_02_Injecting_Custom_Interceptor) shows you how to trace these plain methods.

#### 2.2 Top level method of a node

*Top level method of a node* is a method in which its interceptor begins a new trace in a node. These methods are typically acceptors for RPCs, and the trace is recorded as a `Span` with `ServiceType` categorized as a server.

How the `Span` is recorded depends on whether the transaction has already begun at any previous nodes.

**2.2.1 New transaction**

If the current node is the first one that is recording the transaction, you must issue a new transaction id and record it. `TraceContext.newTraceObject()` will handle this task automatically, so you will simply need to invoke it.

**2.2.2 Continue Transaction**

If the request came from another node traced by a Pinpoint Agent, then the transaction will already have a transaction id issued; and you will have to record the data below to the `Span`. (Most of these data are sent from the previous node, usually packed in the request message)

| name                  | description                           |
| --------------------- | ------------------------------------- |
| transactionId         | Transaction ID                        |
| parentSpanId          | Span ID of the previous node          |
| parentApplicationName | Application name of the previous node |
| parentApplicationType | Application type of the previous node |
| rpc                   | Procedure name (Optional)             |
| endPoint              | Server(current node) address          |
| remoteAddr            | Client address                        |
| acceptorHost          | Server address that the client used   |

Pinpoint finds caller-callee relation between nodes using *acceptorHost*. In most cases, *acceptorHost* is identical to *endPoint*. However, the address which client sent the request to may sometimes be different from the address the server received the request (proxy). To handle such cases, you have to record the actual address the client used to send the request to as *acceptorHost*. Normally, the client plugin will have added this address into the request message along with the transaction data.

Moreover, you must also use the span id issued and sent by the previous node.

Sometimes, the previous node marks the transaction to not be traced. In this case, you must not trace the transaction.

As you can see, the client plugin must be able pass trace data to the server plugin, and how to do this is protocol dependent.

You can find an example of top-level method server interceptor [here](https://github.com/pinpoint-apm/pinpoint-plugin-sample/tree/master/plugins/sample/src/main/java/com/navercorp/pinpoint/plugin/sample/_14_RPC_Server).

#### 2.3 Methods invoking a remote node

An interceptor of a method that invokes a remote node has to record the following data:

| name          | description                                                                           |
| ------------- | ------------------------------------------------------------------------------------- |
| endPoint      | Target server address                                                                 |
| destinationId | Logical name of the target                                                            |
| rpc           | Invoking target procedure name (optional)                                             |
| nextSpanId    | Span id that will be used by next node's span (If next node is traceable by Pinpoint) |

Whether or not the next node is traceable by Pinpoint affects how the interceptor is implemented. The term "traceable" here is about possibility. For example, a HTTP client's next node is a HTTP server. Pinpoint does not trace all HTTP servers, but it is possible to trace them (and there already are HTTP server plugins). In this case, the HTTP client's next node is traceable. On the other hand, MySQL JDBC's next node, a MySQL database server, is not traceable.

**2.3.1 If the next node is traceable**

If the next node is traceable, the interceptor must propagate the following data to the next node. How to pass them is protocol dependent, and in worst cases may be impossible to pass them at all.

| name                  | description                                                                                   |
| --------------------- | --------------------------------------------------------------------------------------------- |
| transactionId         | Transaction ID                                                                                |
| parentApplicationName | Application name of current node                                                              |
| parentApplicationType | Application type of current node                                                              |
| parentSpanId          | Span id of trace at current node                                                              |
| nextSpanId            | Span id that will be used by the next node's span (same value with nextSpanId of above table) |

Pinpoint finds out caller-callee relation by matching *destinationId* of client trace and *acceptorHost* of server trace. Therefore the client plugin has to record *destinationId* and the server plugin has to record *acceptorHost* with the same value. If server cannot acquire the value by itself, client plugin has to pass it to server.

The interceptor's recorded `ServiceType` must be from the RPC client category.

You can find an example for these interceptors [here](https://github.com/pinpoint-apm/pinpoint-plugin-sample/tree/master/plugins/sample/src/main/java/com/navercorp/pinpoint/plugin/sample/_13_RPC_Client).

**2.3.2 If the next node is not traceable**

If the next node is not traceable, your `ServiceType` must have the `TERMINAL` property.

If you want to record the *destinationId*, it must also have the `INCLUDE_DESTINATION_ID` property. If you record *destinationId*, server map will show a node per destinationId even if they have same *endPoint*.

Also, the `ServiceType` must be a DB client or Cache client category. Note that you do not need to concern yourself about the terms "DB" or "Cache", as any plugin tracing a client library with non-traceable target server may use them. The only difference between "DB" and "Cache" is the time range of the response time histogram ("Cache" having smaller intervals for the histogram).

#### 2.4 Asynchronous task

Trace objects are bound to the thread that first created them via **ThreadLocal** and whenever the execution crosses a thread boundary, trace objects are *lost* to the new thread. Therefore, in order to trace tasks across thread boundaries, you must take care of passing the current trace context over to the new thread. This is done by injecting an **AsyncContext** into an object shared by both the invocation thread and the execution thread.\
The invocation thread creates an **AsyncContext** from the current trace, and injects it into an object that will be passed over to the execution thread. The execution thread then retrieves the **AsyncContext** from the object, creates a new trace out of it and binds it to it's own **ThreadLocal**.\
You must therefore create interceptors for two methods : i) one that initiates the task (invocation thread), and ii) the other that actually handles the task (execution thread).

The initiating method's interceptor has to issue an **AsyncContext** and pass it to the handling method. How to pass this value depends on the target library. In worst cases, you may not be able to pass it at all.

The handling method's interceptor must then continue the trace using the propagated **AsyncContext** and bind it to it's own thread. However, it is very strongly recommended that you simply extend the **AsyncContextSpanEventSimpleAroundInterceptor** so that you do not have to handle this manually.

Keep in mind that since the shared object must be able have **AsyncContext** injected into it, you have to add a field using `AsyncContextAccessor` during it's class transformation. You can find an example for tracing asynchronous tasks [here](https://github.com/pinpoint-apm/pinpoint-plugin-sample/tree/master/plugins/sample/src/main/java/com/navercorp/pinpoint/plugin/sample/_12_Asynchronous_Trace).

#### 2.5 Case Study: HTTP

HTTP client is an example of *a method invoking a remote node* (client), and HTTP server is an example of a *top level method of a node* (server). As mentioned before, client plugins must have a way to pass transaction data to server plugins to continue the trace. Note that the implementation is protocol dependent, and [HttpMethodBaseExecuteMethodInterceptor](https://github.com/pinpoint-apm/pinpoint/blob/master/plugins/httpclient3/src/main/java/com/navercorp/pinpoint/plugin/httpclient3/interceptor/HttpMethodBaseExecuteMethodInterceptor.java) of [HttpClient3 plugin](https://github.com/pinpoint-apm/pinpoint/tree/master/plugins/httpclient3) and [StandardHostValveInvokeInterceptor](https://github.com/pinpoint-apm/pinpoint/blob/master/plugins/tomcat/src/main/java/com/navercorp/pinpoint/plugin/tomcat/interceptor/StandardHostValveInvokeInterceptor.java) of [Tomcat plugin](https://github.com/pinpoint-apm/pinpoint/tree/master/plugins/tomcat) show a working example of this for HTTP:

1. Pass transaction data as HTTP headers. You can find header names [here](https://github.com/pinpoint-apm/pinpoint/blob/master/bootstrap-core/src/main/java/com/navercorp/pinpoint/bootstrap/context/Header.java)
2. Client plugin records `IP:PORT` of the server as `destinationId`.
3. Client plugin passes `destinationId` value to server as `Header.HTTP_HOST` header.
4. Server plugin records `Header.HTTP_HOST` header value as `acceptorHost`.

One more thing you have to remember is that all the clients and servers using the same protocol must pass the transaction data in the same way to ensure compatibility. So if you are writing a plugin of some other HTTP client or server, your plugin has to record and pass transaction data as described above.

### 3. Plugin Integration Test

You can run plugin integration tests (`mvn integration-test`) with [PinointPluginTestSuite](https://github.com/pinpoint-apm/pinpoint/blob/master/test/src/main/java/com/navercorp/pinpoint/test/plugin/PinpointPluginTestSuite.java), which is a *JUnit Runner*. It downloads all the required dependencies from maven repositories and launches a new JVM with the Pinpoint Agent and the aforementioned dependencies. The JUnit tests are executed in this JVM.

To run the plugin integration test, it needs a complete agent distribution - which is why integration tests are in the *plugin-sample-agent* module and why they are run in **integration-test phase**.

For the actual integration test, you will want to first invoke the method you are tracing, and then use [PluginTestVerifier](https://github.com/pinpoint-apm/pinpoint/blob/master/bootstrap-core/src/main/java/com/navercorp/pinpoint/bootstrap/plugin/test/PluginTestVerifier.java) to check if the trace data is correctly recorded.

#### 3.1 Test Dependency

`PinointPluginTestSuite` doesn't use the project's dependencies (configured in pom.xml). It uses the dependencies that are listed by `@Dependency` annotation. This way, you may test multiple versions of the target library using the same test class.

Dependencies are declared as following. You may specify versions or version ranges for a dependency library.

```
@Dependency({"some.group:some-artifact:1.0", "another.group:another-artifact:2.1-RELEASE"})
@Dependency({"some.group:some-artifact:[1.0,)"})
@Dependency({"some.group:some-artifact:[1.0,1.9]"})
@Dependency({"some.group:some-artifact:[1.0],[2.1],[3.2])"})
```

`PinointPluginTestSuite` by default searches the local repository and maven central repository. You may also add your own repositories by using the `@Repository` annotation.

#### 3.2 Jvm Version

You can specify the JVM version for a test using `@JvmVersion`. If `@JvmVersion` is not present, JVM at `java.home property` will be used.

#### 3.3 Application Test

`PinpointPluginTestSuite` is not for applications that has to be launched by its own main class. You can extend [AbstractPinpointPluginTestSuite](https://github.com/pinpoint-apm/pinpoint/blob/master/test/src/main/java/com/navercorp/pinpoint/test/plugin/AbstractPinpointPluginTestSuite.java) and related types to test such applications.

### 4. Adding Images

If you're developing a plugin for applications, you need to add images so the server map can render the corresponding node. The plugin jar itself cannot provide these image files and for now, you will have to add the image files to the web module manually.

First, put the PNG files to following directories:

* web/src/main/webapp/images/icons (25x25)
* web/src/main/webapp/images/servermap (80x40)

Then, add `ServiceType` name and the image file name to `htIcons` in *web/src/main/webapp/components/server-map2/jquery.ServerMap2.js*.


# Setting Alarm

[English](#alarm) | [한국어](#alarm-1)

## Alarm

Application's status is periodically checked and alarm is triggered if certain pre-configured conditions (rules) are satisfied.

pinpoint-batch server checks every 3 minutes based on the last 5 minutes of data. And if the conditions are satisfied, it sends sms/email/webhook to the users listed in the user group.

> If an email/sms/webhook is sent everytime when the threshold is exceeded, even after the recipients are aware of the event they might get the same alarms continuously which we thought might be unneccessary. Therefore we decided to gradually increase the transmission frequency for alarms.\
> ex) If an alarm occurs continuously, transmission frequency is increased by a factor of two. 3 min -> 6min -> 12min -> 24min
>
> **NOTICE!**
>
> * These logics were part of pinpoint-web server and ran in the background until v2.2.0 From v2.2.1 it is separated into pinpoint-batch server. Since the batch logic(code) in pinpoint-web will be deprecated in the future, we advise you to transfer the execution of batch to pinpoint-batch server.
> * Webhook function is newly added in v2.1.1, and has some changes in v2.3.1. In both versions, MYSQL table needs to be changed. Please check the notice on these changes in [2.1.1](#2.1-configuration-and-implementation-in-pinpoint-batch)

### 1. User Guide

1\) Configuration menu

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-0ea93f5e306fc6e4958749507fdf8155578552d8%2FConfiguration%20page.gif?alt=media\&token=4245c260-1575-4aa1-9bda-9b9aad19b52a)

2\) Register users

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-f622485ac439ce9675079f95fcdb75b5e04420e4%2Fadd%20user.gif?alt=media\&token=f18e8f55-5ca4-43fe-8f7b-8247e03f5205)

3\) Create user groups

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-4ea91f0d20fecae25061c23e7d92d5f49b6252e3%2FAdd%20usergroup.gif?alt=media\&token=75431576-cd7f-43ef-b58c-ce97a768b23f)

4\) (Optional) Add webhooks

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-b44f12715e808e3b0bd8f641b7769251a6285735%2Fadd%20webhook.gif?alt=media\&token=3b808ba5-b1f0-4911-9ca7-9f35f347f3f5)

5\) Set alarm rules

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-63548e3c2432358b70ae68a911d25e8bb00bd4da%2Fadd%20alarm.gif?alt=media\&token=3d1039cc-5d99-461d-b69f-e111ca8cd254)

**Alarm Rules**

```
SLOW COUNT
   Triggered when the number of slow requests sent to the application exceeds the configured threshold.

SLOW RATE
   Triggered when the percentage(%) of slow requests sent to the application exceeds the configured threshold.

ERROR COUNT
   Triggered when the number of failed requests sent to the application exceeds the configured threshold.

ERROR RATE
   Triggered when the percentage(%) of failed requests sent to the application exceeds the configured threshold.

TOTAL COUNT
   Triggered when the number of all requests sent to the application exceeds the configured threshold.

APDEX SCORE
   Triggered when the Apdex score goes down below the configured threshold.

SLOW COUNT TO CALLEE
   Triggered when the number of slow requests sent by the application exceeds the configured threshold.
   You must specify the domain or the address(ip, port) in the configuration UI's "Note..." box 
   ex) www.naver.com, 127.0.0.1:8080

SLOW RATE TO CALLEE
   Triggered when the percentage(%) of slow requests sent by the application exceeds the configured threshold.
   You must specify the domain or the address(ip, port) in the configuration UI's "Note..." box 
   ex) www.naver.com, 127.0.0.1:8080

ERROR COUNT TO CALLEE
   Triggered when the number of failed requests sent by the application exceeds the configured threshold.
   You must specify the domain or the address(ip, port) in the configuration UI's "Note..." box 
   ex) www.naver.com, 127.0.0.1:8080

ERROR RATE TO CALLEE
   Triggered when the percentage(%) of failed requests sent by the application exceeds the configured threshold.
   You must specify the domain or the address(ip, port) in the configuration UI's "Note..." box 
   ex) www.naver.com, 127.0.0.1:8080

TOTAL COUNT TO CALLEE
   Triggered when the number of all requests sent by the application exceeds the configured threshold.
   You must specify the domain or the address(ip, port) in the configuration UI's "Note..." box 
   ex) www.naver.com, 127.0.0.1:8080

HEAP USAGE RATE
   Triggered when the application's heap usage(%) exceeds the configured threshold.

JVM CPU USAGE RATE
   Triggered when the application's CPU usage(%) detected by JVM exceeds the configured threshold.

SYSTEM CPU USAGE RATE
   Triggered when the application's CPU usage(%) detected by system exceeds the configured threshold.

DATASOURCE CONNECTION USAGE RATE
   Triggered when the application's DataSource connection usage(%) exceeds the configured threshold.

FILE DESCRIPTOR COUNT
   Triggered when the number of open file descriptors exceeds the configured threshold.
```

### 2. Configuration & Implementation

Alarms generated by Pinpoint can be configured to be sent over email, sms and webhook.

Sending alarms over email is simple - you will simply need to configure the property file. Sending alarms over sms requires some implementation. Read on to find out how to do this. The alarm using webhook requires a separate webhook receiver service. You should implement the webhook receiver service - which is not provided by Pinpoint, or You can use [the sample project](https://github.com/doll6777/slack-receiver).

Few modifications are required in pinpoint-batch and pinpoint-web to use the alarm feature. Add some implementations and settings in pinpoint-batch. Configure Pinpoint-web for user to set an alarm settings.

### 2.1 Configuration & Implementation in pinpoint-batch

#### 2.1.1) Email configuration, sms and webhook implementation

**A. Email alarm service**

To use the mailing feature, you need to configure the SMTP server information and information to be included in the email in the [batch-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/batch-root.properties) file.

```
pinpoint.url= #pinpoint-web server url
alarm.mail.server.url= #smtp server address
alarm.mail.server.port= #smtp server port
alarm.mail.server.username= #username for smtp server authentication
alarm.mail.server.password= #password for smtp server authentication
alarm.mail.sender.address= #sender's email address

ex)
pinpoint.url=http://pinpoint.com
alarm.mail.server.url=stmp.server.com
alarm.mail.server.port=587
alarm.mail.server.username=pinpoint
alarm.mail.server.password=pinpoint
alarm.mail.sender.address=pinpoint_operator@pinpoint.com
```

The class that sends emails is already registered as Spring bean in [applicationContext-batch-sender.xml](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/applicationContext-batch-sender.xml).

```
    <bean id="mailSender" class="com.navercorp.pinpoint.batch.alarm.SpringSmtpMailSender">
        <constructor-arg ref="batchConfiguration"/>
        <constructor-arg ref="userGroupService"/>
        <constructor-arg ref="javaMailSenderImpl"/>
    </bean>

    <bean id="javaMailSenderImpl" class="org.springframework.mail.javamail.JavaMailSenderImpl">
        <property name="host" value="${alarm.mail.server.url:}" />
        <property name="port" value="${alarm.mail.server.port:587}" />
        <property name="username" value="${alarm.mail.server.username:}" />
        <property name="password" value="${alarm.mail.server.password:}" />
        <property name="javaMailProperties">
            <props>
                <prop key="mail.transport.protocol">${alarm.mail.transport.protocol:}</prop>
                <prop key="mail.smtp.port">${alarm.mail.smtp.port:}</prop>
                <prop key="mail.smtp.from">${alarm.mail.sender.address:}</prop>
                <prop key="mail.smtp.auth">${alarm.mail.smtp.auth:false}</prop>
                <prop key="mail.smtp.starttls.enable">${alarm.mail.smtp.starttls.enable:false}</prop>
                <prop key="mail.smtp.starttls.required">${alarm.mail.smtp.starttls.required:false}</prop>
                <prop key="mail.debug">${alarm.mail.debug:false}</prop>
            </props>
        </property>
    </bean>
```

If you would like to implement your own mail sender, simply replace the `SpringSmtpMailSender`, `JavaMailSenderImpl` beans above with your own implementation that implements `com.navercorp.pinpoint.web.alarm.MailSender` interface.

```
public interface MailSender {
   void sendEmail(AlarmChecker checker, int sequenceCount);
}
```

**B. Sms alarm service**

To send alarms over sms, you will need to implement your own sms sender by implementing `com.navercorp.pinpoint.batch.alarm.SmsSender` interface. If there is no `SmsSender` implementation, then alarms will not be sent over sms.

```
public interface SmsSender {
    public void sendSms(AlarmChecker checker, int sequenceCount);
}
```

**C. Webhook alarm service**

Webhook alarm service is a feature that can transmit Pinpoint's alarm message through Webhook API.

The webhook receiver service that receives the webhook message should be implemented by yourself, or use [a sample project](https://github.com/doll6777/slack-receiver) provided (in this case Slack).

The alarm messages(refer to as payloads) sent to webhook receiver have the different schema depending on the Alarm Checker type. You can see the payload schemas in [3.Others - The Specification of webhook payloads and the examples](##3.Others).

To enable the webhook alarm service, You need to configure *pinpoint.modules.web.webhook* in [application.yml](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/application.yml) file. Webhook receiver urls can be configured in web UI after configuring the web module to enable webhook as described in the following section.

```
# webhook config
pinpoint.modules.web:
    webhook: true
```

> **NOTICE!**
>
> \*\*\* \*\*MYSQL table ALTER for migrating to Pinpoint v2.1.1 \*\*\*\*\*
>
> As the webhook alarm service is newly added in Pinpoint 2.1.1, you should add column `webhook_send` in table `alarm_rule` to your MYSQL server used for previous versions of Pinpoint.
>
> ```
> ALTER TABLE alarm_rule ADD COLUMN webhook_send CHAR(1) DEFAULT NULL;
> ```
>
> **\*\*\* MYSQL table CREATE for migrating to Pinpoint v2.3.1 \*\*\***
>
> Different webhook destinations can be specified to different alarms and new tables are added for this. Create table `webhook` and `webhook_send` as below in your MYSQL server used for previous versions of Pinpoint.
>
> ```
> CREATE TABLE `webhook` (
>   `webhook_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
>   `alias` VARCHAR(45) NULL,
>   `url` VARCHAR(45) NOT NULL,
>   `application_id` VARCHAR(45) NULL,
>   `service_name` VARCHAR(45) NULL,
>   PRIMARY KEY (`webhook_id`)
> );
>
> CREATE TABLE `webhook_send` (
>   `webhook_send_info_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
>   `webhook_id` INT UNSIGNED NOT NULL,
>   `rule_id` INT UNSIGNED NOT NULL,
>   PRIMARY KEY (`webhook_send_info_id`)
> );
> ```
>
> Of course if you are migrating from versions lower than v2.1.1 to v2.3.1, all the changes above need to be applied.

WebhookSenderImpl class, which sends the webhook, is already implemented for you and is added as webhookSender bean in [applicationContext-batch-sender.xml](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/applicationContext-batch-sender.xml) of Pinpoint-batch.

```markup
   <bean id="webHookSender" class="com.navercorp.pinpoint.web.alarm.WebhookSenderImpl">
        <constructor-arg ref="batchConfiguration"/>
        <constructor-arg ref="userServiceImpl"/>
        <constructor-arg ref="restTemplate" />
    </bean>
```

#### 2.1.2) Configuring MYSQL

**step 1**

Prepare MYSQL Instance to persist the alarm service metadata.

**step 2**

Set up a MYSQL server and configure connection information in [jdbc-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/jdbc-root.properties) file.

```
jdbc.driverClassName=com.mysql.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:13306/pinpoint
jdbc.username=admin
jdbc.password=admin
```

**step 3**

Create tables for the alarm service. Use below DDL files.

* [CreateTableStatement-mysql.sql](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/sql/CreateTableStatement-mysql.sql)
* [SpringBatchJobRepositorySchema-mysql.sql](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/sql/SpringBatchJobRepositorySchema-mysql.sql)

#### 2.1.3) How to execute pinpoint-batch

The pinpoint-batch project is based on spring boot and can be executed with the following command. When building is successfully finished, the executable file is placed under the target/deploy folder of the pinpoint-batch.

```
java -Dspring.profiles.active=XXXX -jar pinpoint-batch-VERSION.jar 

ex) java -Dspring.profiles.active=local -jar pinpoint-batch-2.1.1.jar
```

### 2.2 How to configure pinpoint-web

#### 2.2.1) Configuring MYSQL Server IP

In order to persist user alarm settings, set the mysql connection information in [jdbc-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/jdbc-root.properties) file in pinpoint-web.

```
jdbc.driverClassName=com.mysql.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:13306/pinpoint
jdbc.username=admin
jdbc.password=admin
```

#### 2.2.2) Enabling Webhook Alarm Service

Set *pinpoint.modules.web.webhook* in [pinpoint-web-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/application.yml) as *true* for user to configure the webhook alarm in *Alarm* menu.

```
# webhook config
pinpoint.modules.web:
    webhook: true
```

As you enable the webhook alarm service, you can set the webhook as alarm type and specify the target webhook.

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-d40bb10eb1e4c87b0b49c40df0da30ec191e496f%2Falarm_select_webhook.png?alt=media\&token=ca848cb1-b636-4810-a64e-164a619ce89a)

### 3. Others

### 3.1 Configuration, Execution, Performance.

**1) You may change the batch execution period by modifying the cron expression in** [***applicationContext-batch-schedule.xml***](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/applicationContext-batch-schedule.xml) **file**

```
<task:scheduled-tasks scheduler="scheduler">
    <task:scheduled ref="batchJobLauncher" method="alarmJob" cron="0 0/3 * * * *" />
</task:scheduled-tasks>
```

**2) Ways to improve alarm batch performance**

The alarm batch was designed to run concurrently. If there are a lot of applications using alarms, you may increase the size of the executor's thread pool by modifying `pool-size` in [*applicationContext-alarmJob.xml*](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/job/applicationContext-alarmJob.xml) file.

Note that increasing this value will result in higher resource usage.

```
<task:executor id="poolTaskExecutorForPartition" pool-size="1" />
```

If there are a lot of alarms registered to each application, you may set the `alarmStep` registered in [*applicationContext-alarmJob.xml*](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/job/applicationContext-alarmJob.xml) file to run concurrently.

```
<step id="alarmStep" xmlns="http://www.springframework.org/schema/batch">
    <tasklet task-executor="poolTaskExecutorForStep" throttle-limit="3">
        <chunk reader="reader" processor="processor" writer="writer" commit-interval="1"/>
    </tasklet>
</step>
<task:executor id="poolTaskExecutorForStep" pool-size="10" />
```

**3) Use quickstart's web**

Pinpoint Web uses Mysql to persist users, user groups, and alarm configurations, but our Quickstart example uses MockDAO to reduce memory usage. If you want to use Mysql with Quickstart, please refer to Pinpoint Web's [applicationContext-dao-config.xml](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/applicationContext-dao-config.xml) and [jdbc.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/jdbc.properties).

### 3.2 Details on Webhook

#### 3.2.1) webhook receiver sample project

[Slack-Receiver](https://github.com/doll6777/slack-receiver) is an example project for the webhook receiver. The project can receive alarms from Pinpoint through webhook and send the message to Slack. If you want more details, see [the project repository](https://github.com/doll6777/slack-receiver).

#### 3.2.2) The Specification of webhook payloads and the examples

**The Schemas of webhook payloads**

Key

| Name          | Type      | Description                                                  | Nullable |
| ------------- | --------- | ------------------------------------------------------------ | -------- |
| pinpointUrl   | String    | Pinpoint-web server URL                                      | O        |
| batchEnv      | String    | Batch server environment variable                            | X        |
| applicationId | String    | Alarm target application Id                                  | X        |
| serviceType   | String    | Alarm target application service type                        | X        |
| userGroup     | UserGroup | The UserGroup in the user group page                         | X        |
| checker       | Checker   | The checker info in the alarm setting page                   | X        |
| unit          | String    | The unit of detected value by checker                        | O        |
| threshold     | Integer   | The threshold of value detected by checker during a set time | X        |
| notes         | String    | The notes in the alarm setting page                          | O        |
| sequenceCount | Integer   | The number of alarm occurence                                | X        |

UserGroup

| Name             | Type          | Description                              | Nullable |
| ---------------- | ------------- | ---------------------------------------- | -------- |
| userGroupId      | String        | The user group id in the user group page | X        |
| userGroupMembers | UserMember\[] | Members Info of a specific user group    | X        |

Checker

| Name          | Type                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Nullable |
| ------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| name          | String                      | The name of checker in the alarm setting page                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | X        |
| type          | String                      | <p>The type of checker abstracted by value detected by checker<br>"LongValueAlarmChecker" type is the abstracted checker type of “Slow Count”, “Slow Rate”, “Error Count”, “Error Rate”, “Total Count”, “Slow Count To Callee”, “Slow Rate To Callee”, “Error Count To Callee”, “Error Rate To Callee”, “Total Count to Callee”.<br>"LongValueAgentChecker" type is the abstracted checker type of "Heap Usage Rate", "Jvm Cpu Usage Rate", "System Cpu Usage Rate", "File Descriptor Count".<br>"BooleanValueAgentChecker" type is the abstracted checker type of "Deadlock or not".<br>"DataSourceAlarmListValueAgentChecker" type is the abstracted checker type of "DataSource Connection Usage Rate".</p> | X        |
| detectedValue | Integer or DetectedAgent\[] | <p>The value detected by checker<br>If “type” is “LongValueAlarmChecker”, “detectedValue” is Integer type.<br>If "type" is not "LongValueAlarmChecker", "detectedValue" is DetectedAgents\[] type.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | X        |

UserMember

| Name             | Type   | Description               | Nullable |
| ---------------- | ------ | ------------------------- | -------- |
| id               | String | Member id                 | X        |
| name             | String | Member name               | X        |
| email            | String | Member email              | O        |
| department       | String | Member department         | O        |
| phoneNumber      | String | Member phone number       | O        |
| phoneCountryCode | String | Member phone country code | O        |

DetectedAgent

| Name       | Type                                                  | Description                                                                                                                                                                                                                                                                                   | Nullable |
| ---------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| agentId    | String                                                | Agent id detected by checker                                                                                                                                                                                                                                                                  | X        |
| agentValue | <p>Integer or<br>Boolean or<br>DataSourceAlarm\[]</p> | <p>The value of Agent detected by checker<br>If “type” is “LongValueAgentChecker”, “agentValue” is Integer type.<br>If “type” is “BooleanValueAgentChecker”,“agentValue” is Boolean type.<br>If “type” is “DataSourceAlarmListValueAgentChecker”, “agentValue” is DataSourceAlarm\[] type</p> | X        |

DataSourceAlarm

| Name            | Type    | Description                                   | Nullable |
| --------------- | ------- | --------------------------------------------- | -------- |
| databaseName    | String  | The database name connected to application    | X        |
| connectionValue | Integer | The application's DataSource connection usage | X        |

**The Examples of the webhook Payload**

LongValueAlarmChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "TOTAL COUNT",
   "type": "LongValueAlarmChecker",
   "detectedValue": 33
 },
 "unit": "",
 "threshold": 15,
 "notes": "Note Example",
 "sequenceCount": 4
}
```

LongValueAgentChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "HEAP USAGE RATE",
   "type": "LongValueAgentChecker",
   "detectedValue": [
     {
       "agentId": "test-agent",
       "agentValue": 8
     }
   ]
 },
 "unit": "%",
 "threshold": 5,
 "notes": "Note Example",
 "sequenceCount": 4
}
```

BooleanValueAgentChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "DEADLOCK OCCURRENCE",
   "type": "BooleanValueAgentChecker",
   "detectedValue": [
     {
       "agentId": "test-agent",
       "agentValue": true
     }
   ]
 },
 "unit": "BOOLEAN",
 "threshold": 1,
 "notes": "Note Example",
 "sequenceCount": 4
}
```

DataSourceAlarmListValueAgentChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "DATASOURCE CONNECTION USAGE RATE",
   "type": "DataSourceAlarmListValueAgentChecker",
   "detectedValue": [
     {
       "agentId": "test-agent",
       "agentValue": [
                 {
                     "databaseName": "test",
                     "connectionValue": 32
                 }
        ]
     }
   ]
 },
 "unit": "%",
 "threshold": 16,
 "notes": "Note Example",
 "sequenceCount": 4
}
```

## Alarm

Pinpoint는 application 상태를 주기적으로 체크하여 application 상태의 수치가 임계치를 초과할 경우 사용자에게 알람을 전송하는 기능을 제공한다.

Application 상태 값이 사용자가 설정한 임계치를 초과하는지 판단하는 batch는 [pinpoint-batch](https://github.com/pinpoint-apm/pinpoint/tree/master/batch)에서 동작 한다. Alarm batch는 기본적으로 3분에 한번씩 동작이 된다. 최근 5분동안의 데이터를 수집해서 alarm 조건을 만족하면 user group에 속한 user 들에게 sms/email/webhook message를 전송한다.

> 연속적으로 알람 조건이 임계치를 초과한 경우에 매번 sms/email/webhook를 전송하지 않는다.\
> 알람 조건이 만족할때마다 매번 sms/email/webhook이 전송되는것은 오히려 방해가 된다고 생각하기 때문이다. 그래서 연속해서 알람이 발생할 경우 sms/email/webhook 전송 주기가 점증적으로 증가된다.\
> 예) 알람이 연속해서 발생할 경우, 전송 주기는 3분 -> 6분 -> 12분 -> 24분 으로 증가한다.
>
> ***
>
> **알림**
>
> * Batch는 pinpoint 2.2.0 버전까지는 [pinpoint-web](https://github.com/pinpoint-apm/pinpoint/tree/master/web)에서 동작되었지만, 2.2.1 버전 부터는 batch가 [pinpoint-batch](https://github.com/pinpoint-apm/pinpoint/tree/master/batch)에서 동작되도록 로직을 분리했다.\*\* \*\*앞으로 pinpoint-web의 batch로직은 제거를 할 예정이므로, pinpoint-web에서 batch를 동작시키는 경우 pinpoint-batch에서 batch를 실행하도록 구성하는것을 추천한다.
> * 웹훅 기능은 v2.1.1에 신규로 추가되었으며 v2.3.1에 기능이 개선되었다. 두 버전 모두에서 MYSQL 테이블 변경이 있으므로, 해당 버전 이전에서 업그레이드할 경우, [2.1.1 항목](#2.1-pinpoint-batch)에서 관련 변경 사항을 확인 후 적용해야 한다.

### 1. Alarm 기능 사용 방법

1\) 설정 화면으로 이동

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-0ea93f5e306fc6e4958749507fdf8155578552d8%2FConfiguration%20page.gif?alt=media\&token=4245c260-1575-4aa1-9bda-9b9aad19b52a)

2\) user를 등록

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-f622485ac439ce9675079f95fcdb75b5e04420e4%2Fadd%20user.gif?alt=media\&token=f18e8f55-5ca4-43fe-8f7b-8247e03f5205)

3\) userGroup을 생성

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-4ea91f0d20fecae25061c23e7d92d5f49b6252e3%2FAdd%20usergroup.gif?alt=media\&token=75431576-cd7f-43ef-b58c-ce97a768b23f)

4\) (선택사항) webhook 등

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-b44f12715e808e3b0bd8f641b7769251a6285735%2Fadd%20webhook.gif?alt=media\&token=3b808ba5-b1f0-4911-9ca7-9f35f347f3f5)

5\) alarm rule을 등록

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-63548e3c2432358b70ae68a911d25e8bb00bd4da%2Fadd%20alarm.gif?alt=media\&token=3d1039cc-5d99-461d-b69f-e111ca8cd254)

alarm rule에 대한 설명은 아래를 참고하시오.

```
SLOW COUNT
   외부에서 application을 호출한 요청 중에 외부서버로 응답을 늦게 준 요청의 개수가 임계치를 초과한 경우 알람이 전송된다.

SLOW RATE
   외부에서 application을 호출한 요청 중에 외부서버로 응답을 늦게 준 요청의 비율(%)이 임계치를 초과한 경우 알람이 전송된다.

ERROR COUNT
   외부에서 application을 호출한 요청 중에 에러가 발생한 요청의 개수가 임계치를 초과한 경우 알람이 전송된다.

ERROR RATE
   외부에서 application을 호출한 요청 중에 에러가 발생한 요청의 비율(%)이 임계치를 초과한 경우 알람이 전송된다.

TOTAL COUNT
   외부에서 application을 호출한 요청 개수가 임계치를 초과한 경우 알람이 전송된다.
   
APDEX SCORE
   Apdex 점수가 임계치 이하로 내려간 경우 알람이 전송된다.

SLOW COUNT TO CALLEE
   application 내에서 외부서버를 호출한 요청 중 slow 호출의 개수가 임계치를 초과한 경우 알람이 전송된다.
   설정 화면의 Note 항목에 외부서버의 도메인 이나 주소(ip, port)를 입력해야 합니다. ex) naver.com, 127.0.0.1:8080

SLOW RATE TO CALLEE
   application 내에서 외부서버를 호출한 요청 중 slow 호출의 비율(%)이 임계치를 초과한 경우 알람이 전송된다.
   설정 화면의 Note 항목에 외부서버의 도메인 이나 주소(ip, port)를 입력해야 합니다. ex) naver.com, 127.0.0.1:8080

ERROR COUNT TO CALLEE
   application 내에서 외부서버를 호출한 요청 중 error 가 발생한 호출의 개수가 임계치를 초과한 경우 알람이 전송된다.
   설정 화면의 Note 항목에 외부서버의 도메인 이나 주소(ip, port)를 입력해야 합니다. ex) naver.com, 127.0.0.1:8080

ERROR RATE TO CALLEE
   application 내에서 외부서버를 호출한 요청 중 error 가 발생한 호출의 비율이 임계치를 초과한 경우 알람이 전송된다.
   설정 화면의 Note 항목에 외부서버의 도메인 이나 주소(ip, port)를 입력해야 합니다. ex) naver.com, 127.0.0.1:8080

TOTAL COUNT TO CALLEE
   application 내에서 외부서버를 호출한 요청의 개수가 임계치를 초과한 경우 알람이 전송된다.
   설정 화면의 Note 항목에 외부서버의 도메인 이나 주소(ip, port)를 입력해야 합니다. ex) naver.com, 127.0.0.1:8080

HEAP USAGE RATE
   heap의 사용률이 임계치를 초과한 경우 알람이 전송된다.

JVM CPU USAGE RATE
   applicaiton의 CPU 사용률이 임계치를 초과한 경우 알람이 전송된다.

SYSTEM CPU USAGE RATE
   서버의 CPU 사용률이 임계치를 초과한 경우 알람이 전송된다.

DATASOURCE CONNECTION USAGE RATE
   applicaiton의 DataSource내의 Connection 사용률이 임계치를 초과한 경우 알람이 전송된다.

FILE DESCRIPTOR COUNT
   열려있는 File Descriptor 개수가 임계치를 초가한 경우 알람이 전송된다.
```

### 2. 설정 및 구현 방법

알람을 전송하는 방법은 총 3가지로서, email, sms와 webhook으로 알람을 전송할 수 있다.

email 전송은 설정만 추가하면 기능을 사용할 수 있고, sms 전송을 하기 위해서는 직접 전송 로직을 구현해야 한다.\
webhook 전송은 webhook message를 받는 webhook receiver 서비스를 별도로 준비해야한다. webhook receiver 서비스는 [샘플 프로젝트](https://github.com/doll6777/slack-receiver)를 사용하거나 직접 구현해야 한다.

alarm 기능을 사용하려면 pinpoint-batch와 pinpoint-web를 수정해야한다. pinpoint-batch에는 alarm batch 동작을 위해서 설정 및 구현체를 추가해야 한다. pinpoint-web에는 사용자가 알람을 추가할 수 있도록 설정해야한다.

### 2.1 pinpoint-batch 설정 및 구현 방법

#### 2.1.1) email/sms/webhook 전송 설정 및 구현

**A. email 전송**

email 전송 기능을 사용하기 위해서 [batch-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/batch-root.properties)파일에 smtp 서버 정보와 email에 포함될 정보들을 설정해야 한다.

```
pinpoint.url= #pinpoint-web 서버의 url 
alarm.mail.server.url= #smtp 서버 주소  
alarm.mail.server.port= #smtp 서버 port 
alarm.mail.server.username= #smtp 인증을 위한 userName
alarm.mail.server.password= #smtp 인증을 위한 password
alarm.mail.sender.address= # 송신자 email

ex)
pinpoint.url=http://pinpoint.com
alarm.mail.server.url=stmp.server.com
alarm.mail.server.port=587
alarm.mail.server.username=pinpoint
alarm.mail.server.password=pinpoint
alarm.mail.sender.address=pinpoint_operator@pinpoint.com
```

참고로 [applicationContext-batch-sender.xml](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/applicationContext-batch-sender.xml) 파일에 email을 전송하는 class가 bean으로 등록 되어있다.

```
    <bean id="mailSender" class="com.navercorp.pinpoint.batch.alarm.SpringSmtpMailSender">
        <constructor-arg ref="batchConfiguration"/>
        <constructor-arg ref="userGroupService"/>
        <constructor-arg ref="javaMailSenderImpl"/>
    </bean>

    <bean id="javaMailSenderImpl" class="org.springframework.mail.javamail.JavaMailSenderImpl">
        <property name="host" value="${alarm.mail.server.url:}" />
        <property name="port" value="${alarm.mail.server.port:587}" />
        <property name="username" value="${alarm.mail.server.username:}" />
        <property name="password" value="${alarm.mail.server.password:}" />
        <property name="javaMailProperties">
            <props>
                <prop key="mail.transport.protocol">${alarm.mail.transport.protocol:}</prop>
                <prop key="mail.smtp.port">${alarm.mail.smtp.port:}</prop>
                <prop key="mail.smtp.from">${alarm.mail.sender.address:}</prop>
                <prop key="mail.smtp.auth">${alarm.mail.smtp.auth:false}</prop>
                <prop key="mail.smtp.starttls.enable">${alarm.mail.smtp.starttls.enable:false}</prop>
                <prop key="mail.smtp.starttls.required">${alarm.mail.smtp.starttls.required:false}</prop>
                <prop key="mail.debug">${alarm.mail.debug:false}</prop>
            </props>
        </property>
    </bean>
```

만약 email 전송 로직을 직접 구현하고 싶다면 위의 SpringSmtpMailSender, JavaMailSenderImpl bean 선언을 제거하고 com.navercorp.pinpoint.web.alarm.MailSender interface를 구현해서 bean을 등록하면 된다.

```
public interface MailSender {
   void sendEmail(AlarmChecker checker, int sequenceCount);
}
```

**B. sms 전송**

sms 전송 기능을 사용 하려면 com.navercorp.pinpoint.batch.alarm.SmsSender interface를 구현하고 bean으로 등록해야 한다. SmsSender 구현 class가 없는 경우 sms는 전송되지 않는다.

```
public interface SmsSender {
    public void sendSms(AlarmChecker checker, int sequenceCount);
}
```

**C. webhook 전송**

Webhook 전송 기능은 Pinpoint의 Alarm message를 Webhook API로 전송 할 수 있는 기능이다.

webhook message를 전송받는 webhook receiver 서비스는 [**샘플 프로젝트**](https://github.com/doll6777/slack-receiver)**를 사용하거나 직접 구현해야 한다.** Webhook Receiver 서버에 전송되는 Alarm message(이하 payload)는 Alarm Checker 타입에 따라 스키마가 다르다. Checker 타입에 따른 payload 스키마는 [**3.기타** - webhook 페이로드 스키마 명세, 예시](##3.기타)에서 설명한다.

webhook 기능을 활성화 하기위해서, [pinpoint.modules.web.webhook](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/application.yml) 파일에 Webhook 전송 여부(pinpoint.modules.web.webhook)를 설정한다. Receiver 서버 정보의 경우 [2.2 pinpoint-web 설정 방법](#2.2-pinpoint-web) 같이 web 설정을 마친 후, UI를 통해 추가할 수 있다.

```
# webhook config
pinpoint.modules.web:
    webhook: true
```

> **알림**\
> \&#xNAN;**\*\*\* Pinpoint v2.1.1로 업그레이드를 하기 위한 MYSQL 테이블 변경 \*\*\***
>
> webhook 기능이 추가되면서 mysql 테이블 스키마가 수정되었기 때문에, Pinpoint 2.1.1 미만 버전에서 2.1.1 버전 이상으로 업그레이드한 경우 Mysql의 'alarm\_rule' 테이블에 'webhook\_send' 컬럼을 추가해야 다.
>
> ```
> ALTER TABLE alarm_rule ADD COLUMN webhook_send CHAR(1) DEFAULT NULL;
> ```
>
> **\*\*\* Pinpoint v2.3.1로 업그레이드를 하기 위한 MYSQL 테이블 추가 생성 \*\*\***
>
> Pinpoint v2.1.1에서는 하나의 webhook receiver로만 알람을 보낼 수 있었는데, Pinpoint v2.3.1에서부터 각 알람마다 서로 다른 webhook destination을 설정할 수 있다. 이를 위해서 두 개의 새로운 MYSQL 테이블이 추가되었으며, 아래와 같이 ‘webhook’과 ‘webhook\_send’테이블을 추가해야 한다.
>
> ```
> CREATE TABLE `webhook` (
>   `webhook_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
>   `alias` VARCHAR(45) NULL,
>   `url` VARCHAR(45) NOT NULL,
>   `application_id` VARCHAR(45) NULL,
>   `service_name` VARCHAR(45) NULL,
>   PRIMARY KEY (`webhook_id`)
> );
>
> CREATE TABLE `webhook_send` (
>   `webhook_send_info_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
>   `webhook_id` INT UNSIGNED NOT NULL,
>   `rule_id` INT UNSIGNED NOT NULL,
>   PRIMARY KEY (`webhook_send_info_id`)
> );
> ```
>
> 물론 v2.3.1 이전 버전에서 바로 v2.3.1로 업그레이드하는 경우, 위의 모든 변경사항을 적용해야한다.

참고로 Webhook을 전송하는 클래스(WebhookSenderImpl)는 Pinpoint에서 이미 제공하고 있으며, webHookSender bean으 Pinpoint-batch의 [applicationContext-batch-sender.xml](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/applicationContext-batch-sender.xml) 파일에 등록 되어있다.

```markup
<bean id="webHookSender" class="com.navercorp.pinpoint.web.alarm.WebhookSenderImpl">
    <constructor-arg ref="batchConfiguration"/>
    <constructor-arg ref="userServiceImpl"/>
    <constructor-arg ref="restTemplate" />
</bean>
```

#### 2.1.2) MYSQL 서버 IP 주소 설정 & table 생성

**step 1**

알람에 관련된 데이터를 저장하기 위해 Mysql 서버를 준비한다.

**step 2**

mysql 접근을 위해서 pinpoint-batch의 [jdbc-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/jdbc-root.properties) 파일에 접속 정보를 설정한다.

```
jdbc.driverClassName=com.mysql.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:13306/pinpoint
jdbc.username=admin
jdbc.password=admin
```

**step 3**

mysql에 Alarm 기능에 필요한 table을 생성한다. table 스키마는 아래 파일을 참조한다.

* [*CreateTableStatement-mysql.sql*](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/sql/CreateTableStatement-mysql.sql)
* [*SpringBatchJobRepositorySchema-mysql.sql*](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/sql/SpringBatchJobRepositorySchema-mysql.sql)

#### 2.1.3) pinpoint-batch 실행 방법

pinpoint-batch 프로젝트는 spring boot기반으로 되어있고 아래와 같은 명령어로 실행하면 된다. 빌드후 실행파일은 pinpoint-batch 모듈의 target/deploy 폴더 하위에서 확인할 수 있다.

```
java -Dspring.profiles.active=XXXX -jar pinpoint-batch-VERSION.jar 

ex) java -Dspring.profiles.active=local -jar pinpoint-batch-2.1.1.jar
```

### 2.2 pinpoint-web 설정 방법

#### 2.2.1) MYSQL 서버 IP 주소 설정

사용자 알람 설정을 저장하기 위해서 pinpoint-web의 [jdbc-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/jdbc-root.properties) 파일에 mysql 접속 정보를 설정한다.

```
jdbc.driverClassName=com.mysql.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:13306/pinpoint
jdbc.username=admin
jdbc.password=admin
```

#### 2.2.2) webhook 기능 활성화

사용자가 알람 설정에 webhook 기능을 적용할수 있도록 [pinpoint-web-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/application.yml) 파일에 webhook 기능을 활성화한다.

```
# webhook config
pinpoint.modules.web:
    webhook: true
```

webhook 기능을 활성화하면, 아래 그림처럼 알람 설정 화면에서 webhook을 알람 타입으로 선택할 수 있다.

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-d40bb10eb1e4c87b0b49c40df0da30ec191e496f%2Falarm_select_webhook.png?alt=media\&token=ca848cb1-b636-4810-a64e-164a619ce89a)

### 3. 기타

### 3.1 설정, 실행, 성능

**1) Batch의 동작 주기를 조정하고 싶다면** [***applicationContext-batch-schedule.xml***](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/applicationContext-batch-schedule.xml) **파일의 cron expression을 수정하면 된다.**

```
<task:scheduled-tasks scheduler="scheduler">
    <task:scheduled ref="batchJobLauncher" method="alarmJob" cron="0 0/3 * * * *" />
</task:scheduled-tasks>
```

**2) Alarm batch 성능을 높이는 방법은 다음과 같다.**

Alarm batch 성능 튜닝을 위해서 병렬로 동작이 가능하도록 구현을 해놨다. 그래서 아래에서 언급된 조건에 해당하는 경우 설정 값을 조정한다면 성능을 향상 시킬 수 있다. 단, 병렬성을 높이면 리소스 사용률이 높아지는 것은 감안해야 한다.

Alarm이 등록된 application의 개수가 많다면 [*applicationContext-alarmJob.xml*](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/job/applicationContext-alarmJob.xml) 파일의 poolTaskExecutorForPartition의 pool size를 늘려주면 된다.

```
<task:executor id="poolTaskExecutorForPartition" pool-size="1" />
```

Application 각각마다 등록된 alarm의 개수가 많다면 [*applicationContext-alarmJob.xml*](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/job/applicationContext-alarmJob.xml) 파일에 선언된 alarmStep이 병렬로 동작되도록 설정하면 된다.

```
<step id="alarmStep" xmlns="http://www.springframework.org/schema/batch">
    <tasklet task-executor="poolTaskExecutorForStep" throttle-limit="3">
        <chunk reader="reader" processor="processor" writer="writer" commit-interval="1"/>
    </tasklet>
</step>
<task:executor id="poolTaskExecutorForStep" pool-size="10" />
```

**3) Quickstart web을 사용한다면.**

Quickstart pinpoint web은 mockDAO를 사용하기 때문에 추가한 알람 설정들이 저장되지 않는다. Mysql과 quickstart를 연동해서 사용하려면 다음의 설정들을 참고해서 수정 후 기능을 사용해야한다: [applicationContext-dao-config.xml](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/applicationContext-dao-config.xml), [jdbc.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/jdbc.properties).

### 3.2 webhook 상세

#### 3.2.1 **Webhook receiver 예제 프로젝트**

[Slack-Receiver](https://github.com/doll6777/slack-receiver) 는 Webhook Receiver의 예제 프로젝트이다. 이 프로젝트는 Pinpoint의 webhook의 알람을 받아서 Slack으로 메시지를 전송할 수 있는 스프링 부트로 구현된 서비스이다. 이 프로젝트의 자세한 사항은 [해당 GitHub 저장소](https://github.com/doll6777/slack-receiver) 를 참고하면 된다.

#### 3.2.2 webhook 페이로드 스키마 및 예시

**페이로드 스키마**

Key

| Name          | Type      | Description              | Nullable |
| ------------- | --------- | ------------------------ | -------- |
| pinpointUrl   | String    | Pinpoint-web의 서버 URL 주소  | O        |
| batchEnv      | String    | Batch 서버의 환경 변수          | X        |
| applicationId | String    | 타겟 애플리케이션 ID             | X        |
| serviceType   | String    | 타겟 애플리케이션 서비스 타입         | X        |
| userGroup     | UserGroup | 유저 그룹 페이지의 유저 그룹         | X        |
| checker       | Checker   | alarm 설정 페이지의 checker 정보 | X        |
| unit          | String    | checker가 감지한 값의 단위       | O        |
| threshold     | Integer   | 설정된 시간동안 체커가 감지한 값의 임계치  | X        |
| notes         | String    | 알람 설정 페이지의 notes         | O        |
| sequenceCount | Integer   | 알람 발생 횟수                 | X        |

UserGroup

| Name             | Type          | Description         | Nullable |
| ---------------- | ------------- | ------------------- | -------- |
| userGroupId      | String        | 유저 그룹 페이지의 유저 그룹 ID | X        |
| userGroupMembers | UserMember\[] | 특정 유저 그룹의 멤버 정보     | X        |

Checker

| Name          | Type                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Nullable |
| ------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| name          | String                      | 알람 설정 페이지의 checker 이름                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | X        |
| type          | String                      | <p>체커가 감지한 값의 추상 타입, 다음 중 하나에 해당됨<br>"LongValueAlarmChecker" 타입은 "Slow Count", “Slow Count”, “Slow Rate”, “Error Count”, “Error Rate”, “Total Count”, “Slow Count To Callee”, “Slow Rate To Callee”, “Error Count To Callee”, “Error Rate To Callee”, “Total Count to Callee”의 추상 타입에 속한다.<br>"LongValueAgentChecker" 타입은 "Heap Usage Rate", "Jvm Cpu Usage Rate", "System Cpu Usage Rate", "File Descriptor Count"의 추상타입이다.<br>"BooleanValueAgentChecker" 타입은 "Deadlock or not"의 추상 타입이다.<br>"DataSourceAlarmListValueAgentChecker" 타입은 "DataSource Connection Usage Rate"의 추상타입이다.</p> | X        |
| detectedValue | Integer or DetectedAgent\[] | <p>Checker가 감지한 값<br>“LongValueAlarmChecker”, “detectedValue” 타입은 Integer 타입이다.<br>"LongValueAlarmChecker", "detectedValue"이 아닌 타입은 DetectedAgents\[] 타입 이다.</p>                                                                                                                                                                                                                                                                                                                                                                                                                         | X        |

UserMember

| Name             | Type   | Description            | Nullable |
| ---------------- | ------ | ---------------------- | -------- |
| id               | String | 멤버의 id                 | X        |
| name             | String | 멤버의 name               | X        |
| email            | String | 멤버의 email              | O        |
| department       | String | 멤버의 department         | O        |
| phoneNumber      | String | 멤버의 phone number       | O        |
| phoneCountryCode | String | 멤버의 phone country code | O        |

DetectedAgent

| Name       | Type                                                  | Description                                                                                                                                                                                                                   | Nullable |
| ---------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| agentId    | String                                                | Checker가 감지한 에이전트 ID                                                                                                                                                                                                          | X        |
| agentValue | <p>Integer or<br>Boolean or<br>DataSourceAlarm\[]</p> | <p>체커가 감지한 에이전트의 값<br>“LongValueAgentChecker”, “agentValue” 은 Integer 타입이다.<br>“BooleanValueAgentChecker”,“agentValue” 은 Boolean 타입이다..<br>“DataSourceAlarmListValueAgentChecker”, “agentValue”은 DataSourceAlarm\[] 타입이다.</p> | X        |

DataSourceAlarm

| Name            | Type    | Description                              | Nullable |
| --------------- | ------- | ---------------------------------------- | -------- |
| databaseName    | String  | 애플리케이션에 접속한 데이터베이스 이름                    | X        |
| connectionValue | Integer | Applicaiton의 DataSource내의 Connection 사용률 | X        |

**webhook Payload 예제**

LongValueAlarmChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "TOTAL COUNT",
   "type": "LongValueAlarmChecker",
   "detectedValue": 33
 },
 "unit": "",
 "threshold": 15,
 "notes": "Note Example",
 "sequenceCount": 4
}
```

LongValueAgentChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "HEAP USAGE RATE",
   "type": "LongValueAgentChecker",
   "detectedValue": [
     {
       "agentId": "test-agent",
       "agentValue": 8
     }
   ]
 },
 "unit": "%",
 "threshold": 5,
 "notes": "Note Example",
 "sequenceCount": 4
}
```

BooleanValueAgentChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "DEADLOCK OCCURRENCE",
   "type": "BooleanValueAgentChecker",
   "detectedValue": [
     {
       "agentId": "test-agent",
       "agentValue": true
     }
   ]
 },
 "unit": "BOOLEAN",
 "threshold": 1,
 "notes": "Note Example",
 "sequenceCount": 4
}
```

DataSourceAlarmListValueAgentChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "DATASOURCE CONNECTION USAGE RATE",
   "type": "DataSourceAlarmListValueAgentChecker",
   "detectedValue": [
     {
       "agentId": "test-agent",
       "agentValue": [
                 {
                     "databaseName": "test",
                     "connectionValue": 32
                 }
        ]
     }
   ]
 },
 "unit": "%",
 "threshold": 16,
 "notes": "Note Example",
 "sequenceCount": 4
}
```


# New Inspector

[English](#id-1-overview) | [한국어](#id-1)

## 1 Overview

There has been changes in inspector in v3.0.0. The newly renewed inspector will be referred to as 'New Inspector' below, while the previous version will be referred to as 'Legacy Inspector' ([Legacy Application Inspector](https://pinpoint-apm.gitbook.io/pinpoint/v/v2.5.4/documents/application-inspector)).

Although users won't see significant changes on front-end, but the whole architecture has been rebuilt from the scratch. The data storage has been changed from HBase to Pinot. And the APIs have been improved so that it is more easily extenable and their responses more clear to understand.

## 2 Installation and Configuration

### 2.1 Install and Run Kafka

Kafka enables real-time streaming of inspector data from Pinpoint collector to Pinot.

#### 2.1.A Set Up Kafka

Refer to [this document](https://kafka.apache.org/quickstart) to download Kafka and start the Kafka environment.

If you have already [set up Kafka for Pinpoint System Metric](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.2.a-kafka-installation-guide), please skip this step.

#### 2.1.B Create Kafka Topics for New Inspector

* Create 2 topics with the names below:
  * inspector-stat-agent-00
  * inspector-stat-app

### 2.2 Set Up Pinot

#### 2.2.A Install Pinot

Install Pinot according to [Pinot Getting Started guide](https://docs.pinot.apache.org/basics/getting-started).

If you have already [set up Pinot for Pinpoint System Metric](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#id-3.2.a-install-and-run-pinot), please skip this step.

#### 2.2.B Create Pinot Tables

* Create 2 tables with the snames below:
  * inspectorStatAgent00: This table stores agent inspector data. The [script file to create the table](https://github.com/pinpoint-apm/pinpoint/tree/master/inspector-module/inspector-collector/src/main/pinot/multi-table) is provided in our github repository.
  * inspectorStatApp: This table stores application inspector data.
* Refer to the [github repository](https://github.com/pinpoint-apm/pinpoint/tree/master/inspector-module/inspector-collector/src/main/pinot) for table schema and configuration settings.

### 2.3 Configure and Run Pinpoint Collector, Web, and Batch with New Inspector

* **Related options and settings are already enabled by default, so there is no need to modify any settings from what is provided in our github repository.**
* When upgrading from Pinpoint version below 3.0 to version 3.0.0 or above, some of the options may be missing in the configuration properties files you have been using. Please refer to the related configurations in the following section to check if any changes are needed in your settings.

## 3 Related Settings of Pinpoint Components

* The following configurations are already set by default in Pinpoint version 3.0.
* When upgrading from Pinpoint version below 3.0 to version 3.0.0 or above and when you wish to continue using customized configuration files you have been using, please check if below mentioned configurations are well set in your files.

### Pinpoint Collector

* `application.yml` file in `collector-starter` module:

```
pinpoint:
  modules:
    collector:
      inspector:
        enabled: true
```

### Pinpoint Web

* `application.yml` file in `web-starter` module:

```
pinpoint:
  modules:
    web:
      inspector:
        enabled: true
```

### Pinpoint Batch

* `batch-root.properties` file in `batch` module:

```
alarm.collector.version=2
```

## 4 Q\&A

#### A Can we still use the Legacy Inspector to save the data to HBase?

Yes, but Legacy Inspector will be deprecated in v3.0.1 so we recommended you to use the New Inspector.

To use Legacy Inspector with v3.0.0, you need to add the following settings to the Pinpoint components:

**Modify `application.yml` file in `collector-starter` module OR add java vm option when running Pinpoint Collector.**

* application.yml

```
pinpoint:
  modules:
    collector:
      inspector:
        hbase:
          enabled: true
```

* java vm option

```
-Dpinpoint.modules.collector.inspector.hbase.enabled=true
```

**Modify `batch-root.properties` file in `batch` module OR add java vm option when running Pinpoint Batch.**

* batch-root.properties

```
alarm.collector.version=1
```

* java vm option

```
-Dalarm.collector.version=1
```

#### B Why change database to Pinot when there are no additional features provided to users?

New Inspector saves and retrieves the data faster than the Legacy Inspector thanks to Pinot. As Pinot project gets mature over time, there can be further improvements on performance or additional features can be introduced to Pinpoint Inpsector as well.

#### C Reading inspector-stat-agent table becomes slow as more data is being stored.

You can improve performance by distributing the data across multiple tables. Follow the steps below to create multiple Kafka topics and Pinot tables. Then, add settings to Pinpoint components to read and write data from multiple Pinot tables.

**Create More Kafka Topics**

* Create N Kafka topics. (From 00 to N-1)
* The format of the topics is as follows:
  * inspector-stat-agent-00
  * inspector-stat-agent-01
  * ...
  * inspector-stat-agent-99

**Create More Pinot Tables**

* Create N Pinot tables. (From 00 to N-1)
  * [The script file](https://github.com/pinpoint-apm/pinpoint/tree/master/inspector-module/inspector-collector/src/main/pinot/multi-table) creating multiple Pinot tables is provided in our github repository.
* The format of the table names and schema names is as follows:
  * inspectorStatAgent00
  * inspectorStatAgent01
  * ...
  * inspectorStatAgent99

**Modify `application.yml` file in `collector-starter` module OR add java vm option when running Pinpoint Collector**

* application.yml

```
kafka:
  inspector:
    agent:
      table:
        count: N
```

* java vm option

```
-Dkafka.inspector.agent.topic.count=N
```

**Modify `application.yml` file in `web-starter` module OR add java vm option when running Pinpoint Web**

* application.yml

```
pinot:
  inspector:
    agent:
      table:
        count: N
```

* java vm option

```
-Dpinot.inspector.agent.topic.count=N
```

**Modify `batch-root.properties` file in `batch` module OR add java vm option when running Pinpoint Batch**

* batch-root.properties

```
job.alarm.agent.inspector.stat.table.count=N
```

* java vm option

```
-Djob.alarm.agent.inspector.stat.table.count=N
```

***

## 1 개요

inspector가 Pinpoint v3.0.0에서 새로워졌습니다. 이하 새로워진 inspector를 'New Inspector'이라고 부르고 과거의 inspector는 'Legacy Inspector'라고 칭합니다 ([Legacy Application Inspector](https://pinpoint-apm.gitbook.io/pinpoint/v/v2.5.4/documents/application-inspector)).

New Inspector에서 사용자가 보는 화면은 크게 달라진 건은 없습니다. 그러나 내부적으로 많은 변화가 있었습니다. 데이터를 저장하는 저장소가 HBase에서 Pinot로 변경이 되었습니다. api를 쉽게 확장할 수 있고, response를 명확한 형식으로 개편했습니다. 즉 inspector 기능을 추가하고 확장하기 쉽게 개선되었습니다.

## 2 설치/설정 방법

### 2.1 Kafka 설치 및 실행

실시간으로 collector에서 데이터를 전달받아 Pinot에 저장하기 위해서 Kafka를 설치해야 합니다.

**2.1.A Kafka 설치**

[설치 가이드 링크](https://kafka.apache.org/quickstart)를 보고 Kafka를 다운 받아 실행합니다.

**2.1.B topic 생성**

* 아래 2개 Kafka topic을 생성합니다.
  * inspector-stat-agent-00
  * inspector-stat-app

### 2.2 Pinot 설치 및 실행

**2.1.A Pinot 설치**

Pinot 사이트에서 [설치 방법 가이드](https://docs.pinot.apache.org/basics/getting-started)를 참고하여 Pinot를 설치합니다.

**2.1.B Pinot table 생성**

* 아래 2개 테이블을 생성합니다.
  * inspectorStatAgent00: 이 테이블은 agent inspector data를 저장합니다. [스크립트](https://github.com/pinpoint-apm/pinpoint/tree/master/inspector-module/inspector-collector/src/main/pinot/multi-table)로 생성이 가능합니다.
  * inspectorStatApp: 이 테이블은 application inspector data를 저장합니다.
* table schema와 configuration은 [github repository](https://github.com/pinpoint-apm/pinpoint/tree/master/inspector-module/inspector-collector/src/main/pinot)를 참고해주세요.

### 2.3 Pinpoint Collector, batch, Web의 New Inspector 기능 활성화

* **관련 옵션 및 설정은 기본적으로 활성화되어 있으므로 추가로 설정할 필요가 없습니다.**
* Pinpoint 3.0 미만버전에서 3.0.0 이상버전으로 업그레이드 시 일부 옵션이 누락되는경우 아래 관련 옵션 설명을 참고해주세요.

## 3 Pinpoint 컴포넌트의 관련 설정

* 아래 설정들은 Pinpoint 3.0 버전에서 기본적으로 설정되어있습니다.
* Pinpoint 버전을 3.0으로 업그레이드하는경우 일부 설정이 누락되는 경우 참고하기 위해서 설정을 명시해놓습니다.

### Pinpoint Collector

* `collector-starter` 모둘의 `application.yml` 파일:

```
pinpoint:
  modules:
    collector:
      inspector:
        enabled: true
```

### Pinpoint Web

* `web-starter` 모듈의 `application.yml` 파일:

```
pinpoint:
  modules:
    web:
      inspector:
        enabled: true
```

### Pinpoint Batch

* `batch` 모듈의 `batch-root.properties` 파일:

```
alarm.collector.version=2
```

## 4 Q\&A

#### A HBase에 데이터를 저장하는 Legacy Inspector를 사용할 수 없나요?

가능합니다. 그러나 3.0.1 버전 이상 부터는 Legacy Inspector를 삭제할 예정이므로 Pinpoint 버전이 올라갈수록 기능을 사용할수 없으므로 New Inspector를 사용하는것을 권장합니다. 기능을 사용하려면 Pinpoint 컴포넌트들에 아래 설정을 추가해야합니다.

**collector-starter 프로젝트의 application.yml 파일이나 java vm option에 아래 설정을 추가해주세요.**

* application.yml

```
pinpoint:
  modules:
    collector:
      inspector:
        hbase:
          enabled: true
```

* java vm option

```
-Dpinpoint.modules.collector.inspector.hbase.enabled=true
```

**batch 프로젝트에서 batch-root.properties 파일이나 java vm option에 아래 설정을 추가해주세요.**

* batch-root.properties

```
alarm.collector.version=1
```

* java vm option

```
-Dalarm.collector.version=1
```

#### B 사용자에게 제공되는 기능은 비슷한데 Pinot기반으로 inspector를 개선한 이유는 뭘까요?

다양한 데이터를 빠르게 저장하고 확인하고 위해서 Pinot로 데이터를 저장하도록 개선되었고 아직 부족한 기능이 많지만 Pinot의 발전에 맞춰서 기능을 보완하도록 하겠습니다.

#### C inspector-stat-agent 테이블의 데이터가 많아서 읽기 속도가 느려집니다.

여러 개의 체이블에 데이터를 나누어 저장해서 성능 향상을 얻을 수 있습니다. 아래를 단계를 따라 전체 N 개의 Kafka topic과 Pinot table을 생성하고, Pinpoint 컴포넌트들에 설정을 추가해서 data를 수집/조회합니다.

**Kafka topic 생성**

* N개 Kafka topic을 생성합니다. (00에서 N-1까지)
* topic의 형식은 다음과 같습니다.
  * inspector-stat-agent-00
  * inspector-stat-agent-01
  * ...
  * inspector-stat-agent-99

**Pinot table 생성**

* N개 Pinot table을 생성합니다. (00에서 N-1까지)
  * [스크립트](https://github.com/pinpoint-apm/pinpoint/tree/master/inspector-module/inspector-collector/src/main/pinot/multi-table)로 다수의 테이블 생성이 가능합니다.
* table name과 schema name의 형식은 다음과 같습니다.
  * insepctorStatAgent00
  * insepctorStatAgent01
  * ...
  * insepctorStatAgent99

**`collector-starter` 모듈의 `application.yml` 파일이나 java vm option에 아래 설정을 추가해 주세요.**

* application.yml

```
kafka:
  inspector:
    agent:
      table:
        count: N
```

* java vm option

```
-Dkafka.inspector.agent.topic.count=N
```

**`web-starter` 모듈의 `application.yml` 파일이나 java vm option에 아래 설정을 추가해 주세요.**

* application.yml

```
pinot:
  inspector:
    agent:
      table:
        count: N
```

* java vm option

```
-Dpinot.inspector.agent.topic.count=N
```

**`batch` 모듈의 `batch-root.properties` 파일이나 java vm option에 아래 설정을 추가해 주세요.**

* batch-root.properties

```
job.alarm.agent.inspector.stat.table.count=N
```

* java vm option

```
-Djob.alarm.agent.inspector.stat.table.count=N
```


# System Metric

[English](#system_metrics) | [한국어](#1_system_metrics_기능이란?)

## 1 System Metrics

System metrics menu is newly added to Pinpoint in v2.5.0. Pinpoint uses [telegraf agent](https://portal.influxdata.com/downloads/) to collect system metrics data to Pinpoint Collector in which the data are saved in Pinot. Saved system metrics data are accessible via Pinpoint web.

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-c894164f22ccffbbac3a17a452c9c99867ae5280%2Fsystem_metric_01.png?alt=media\&token=3509e031-d53c-431c-b924-5ff9bfc768a2)

Pinot is a real-time distributed OLAP datastore. For further information please refer to [their official documents](https://docs.pinot.apache.org).

## 2 Architecture

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-13e876804194ef1b6837ef12ae31d84461ec6fab%2Fsystem_metric_02.jpeg?alt=media\&token=50e1986f-afa6-4587-9291-ea7f24743158)

1. Telegraf agent sends system metrics data to Pinpoint collector.
2. Pinpoint collector saves data to Pinot through Kafka.

* Kafka is necessary to stream data to Pinot.

3. Pinpoint web accesses Pinot to display collected metrics data.

## 3 Installation and Configuration

### 3.1 Install Kafka

Kafka enables real-time streaming of system metrics data from Pinpoint collector to Pinot.

#### 3.1.A Kafka Installation Guide

Please refer to [this document](https://kafka.apache.org/quickstart) to get Kafka and start the Kafka environment.

#### 3.1.B Create Kafka Topics for Pinpoint System Metrics

Create 3 topics with the names below:

* `system-metric-data-type`
* `system-metric-tag`
* `system-metric-double`

### 3.2 Install Pinot

This section describes how to install Pinot which is used in Pinpoint to save system metrics data.

#### 3.2.A Install and Run Pinot

* Install Pinot according to [Pinot Getting Started guide](https://docs.pinot.apache.org/basics/getting-started)
* Above guide gives you the way to run Pinot locally, in Docker, and in Kubernetes.

#### 3.2.B Create Pinot Tables

* Pinot table schemas for Pinpoint system metrics is provided in [our github repository](https://github.com/pinpoint-apm/pinpoint/tree/master/metric-module/metric/src/main/pinot).
* Please refer to [Pinot documents](https://docs.pinot.apache.org/basics/components/table#streaming-table-creation) to create necessary tables in your Pinot cluster.
* Total 3 tables should be created.
  * systemMetricDataType: this table saves type informations on collected data.
  * systemMetricTag: this table saves metadata (i.e., host, tags) for collected data.
  * systemMetricDouble: this table saves metric data in double. In order to use the hybrid table feature, create both REALTIME and OFFLINE tables.

### 3.3 Configure and Run Pinpoint Collector with System Metrics

There are additional configurations for Pinpoint collector to collect the metrics data from Telegraf agents.

#### 3.3.A Pinpoint Collector Settings for System Metrics

**1)** In order to communicate with Pinot, you need to modify the configuration files in the [profiles](https://github.com/pinpoint-apm/pinpoint/tree/master/pinot/pinot-config/src/main/resources/pinot/profiles) directory according to your profile.

* Modify pinot-jdbc.properties configuration: Set the address of the Pinot installed in [3.1](#3.1-Install-Pinot) as follows:
  * ```
            pinpoint.pinot.jdbc.url=jdbc:pinot://localhost:9000
            pinpoint.pinot.jdbc.username=userId
            pinpoint.pinot.jdbc.password=password
    ```

**2)** In order to communicate with Kafka, you need to modify the configuration files in the [profiles](https://github.com/pinpoint-apm/pinpoint/tree/master/pinot/pinot-kafka/src/main/resources/profiles) directory according to your profile.

* Modify kafka-producer-factory.properties configuration: Set the address of your Kafka instance:
  * ```
    pinpoint.metric.kafka.bootstrap.servers=--KAFKA_ADDRESS--
    ```

#### 3.3.B Run Pinpoint Collector with System Metrics

After successfully building Pinpoint project, run `pinpoint-collector-starter-boot-XXXX.jar` file created under `pinpoint/metric-module/collector-starter/target/deploy`.

* `pinpoint-collector-starter-boot-XXXX.jar` includes system metrics on top of original pinpoint-collector.
* In order to enable metric functions, you need to add `--pinpoint.collector.type=METRIC` or `--pinpoint.collector.type=ALL` arguments when starting the application.
  * METRIC: only enables collecting the system metrics.
  * ALL: enables both pinpoint collector and system metrics collection.

### 3.4 Configure and Run Pinpoint Web with System Metrics

There are additional configurations for Pinpoint web to display the system metrics data stored in Pinot.

#### 3.4.A Pinpoint Web Settings for System Metrics

1. In order to communicate with Pinot, you need to modify the configuration files in the \[profiles]\((<https://github.com/pinpoint-apm/pinpoint/tree/master/pinot/pinot-config/src/main/resources/pinot/profiles>) directory according to your profile.

* Update the address of the Pinot installed in [3.1](#3.1-Install-Pinot) in the jdbc-pinot.properties configuration file:

  ```
  pinpoint.pinot.jdbc.url=jdbc:pinot://localhost:9000
  pinpoint.pinot.jdbc.username=userId
  pinpoint.pinot.jdbc.password=password
  ```

**2)** To enable the system metric feature in the web interface, modify the [pinpoint-web-metric.properties](https://github.com/pinpoint-apm/pinpoint/tree/master/metric-module/metric/src/main/resources/pinot-web/profiles) file:

```
config.show.systemMetric=true
```

#### 3.4.B Run Pinpoint Web with System Metrics

After successfully building Pinpoint project, run `pinpoint-web-starter-boot-XXXX.jar` file created under `pinpoint/metric-module/web-starter/target/deploy`.

#### 3.5 Additional Information

Pinpoint web and collector binaries with system metrics is located under different directories from those of the original Pinpoint web and collector.

* original collector: pinpoint/collector/deploy -> collector with system metrics: pinpoint/metric-module/collector-starter/target/deploy
* original web: pinpoint/web/deploy -> web with system metrics: pinpoint/metric-module/web-starter/target/deploy

### 3.6 Install and Configure Talegraf Agent

Telegraf collects below metrics information on the host machine:

* cpu
* disk usage
* disk usage (percent)
* inode usage
* memory usage
* memory usage(percent)
* swap
* system load
* nginx
* apache

***

* Install Telegraf according to this [installation guide](https://docs.influxdata.com/telegraf/v1.21/introduction/installation/).
* Add below configuration to `telegraf.conf` file to send collected metrics to Pinpoint collector via http.
  * **Note**: Starting from Pinpoint v3.0.2, the metric port has been changed from `15200` to `9995`.
  * ```
              [[outputs.http]]
                url = "http://{PINPOINT_COLLECTOR_IP}:9995/telegraf"
                 
                 [outputs.http.headers]
                 hostGroupName = {applicationName}
                 Content-Type = "application/json"  
    ```
  * `url`: substitute `{PINPOINT_COLLECTOR_IP}` to your Pinpoint collector address so that telegraf can send collected metrics to Pinpoint collector
  * `hostGroupName`: this value will be used as the key in Pinpoint web when querying the metrics details. It is recommended to use your applicationName already used in Pinpoint.

### 4 View Collected System Metrics Data

1. Click `Infrastructure` on the side bar menu in Pinpoint web.
2. Search for the hostGroupName you have configured for Telegraf agents as decribed [in 3.4](#3.4-Install-and-Configure-Talegraf-Agent).
3. A list of hosts will be displayed on the left, and you can view the system metrics data by clicking each of them.

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-c894164f22ccffbbac3a17a452c9c99867ae5280%2Fsystem_metric_01.png?alt=media\&token=3509e031-d53c-431c-b924-5ff9bfc768a2)

### 5 Notes

* Other metrics and statistics data will be stored in Pinot to enhance Pinpoint experience in near future.
* Currently this system metrics versions are in beta. It will be officially released when when we can make sure that everything works as we intended.
* If you have been using the system metric feature in version 2.5.0 or lower and are upgrading, please refer to [guide](https://github.com/pinpoint-apm/pinpoint/issues/9791#issuecomment-1491486262) for instructions.

***

## 1 system metrics 기능이란?

system metrics 기능은 v2.5.0에 핀포인트에 새로 추가되었다. [telegraf agent](https://portal.influxdata.com/downloads/) 를 사용하여 system metric 데이터를 collector에 전달하고 pinot에 데이터를 저장한다. pinpoint web에서 저장된 system metric 데이터를 확인할 수 있다.

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-c894164f22ccffbbac3a17a452c9c99867ae5280%2Fsystem_metric_01.png?alt=media\&token=3509e031-d53c-431c-b924-5ff9bfc768a2)

pinot는 실시간 분산 OLAP 데이터 저장소이다. 자세한 사항은 [pinot 사이트](https://docs.pinot.apache.org)를 참고하도록 하자.

## 2 구조

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-13e876804194ef1b6837ef12ae31d84461ec6fab%2Fsystem_metric_02.jpeg?alt=media\&token=50e1986f-afa6-4587-9291-ea7f24743158)

* ① telgegraf agent에서 system metric 데이터를 collector에 전달한다.
* ② collector는 kafka에 데이터를 전송하여 pinot에 데이터를 저장한다.
  * 참고로 pinot는 stream 데이터 전송을 위해서 kafka를 반드시 필요로 한다.
* ③ web은 pinot에서 데이터를 조회하여 화면으로 데이터를 보여준다.

## 3 설치/설정 방법

### 3.1 kafka 설치 및 실행

실시간으로 collector에서 데이터를 전달받아 pinot에 저장하기 위해서 kafka를 설치해야 한다.

#### 3.1.A. kafka 설치

* [설치 가이드 링크](https://kafka.apache.org/quickstart)를 보고 kafka를 다운 받아 실행하자.

#### 3.1.B. topic 생성

* 아래 3개 topic을 생성하자. -`system-metric-data-type`, `system-metric-tag`, `system-metric-double`

### 3.2 pinot 설치 및 실행

시스템 메트릭 데이터를 저장하는 pinot를 설치하는 법을 안내한다.

#### 3.2.A. pinot 설치 및 실행

* pinot 사이트에서 [설치 방법 가이드](https://docs.pinot.apache.org/basics/getting-started)를 참고하여 pinot를 설치한다.
* 다양한 환경(local, docker, Kubernetes)에서 pinot 실행 환경을 구성할 수 있으니 위 가이드를 참고하자.

#### 3.2.B. 테이블 스키마 및 생성

* [테이블 생성 스키마 파일](https://github.com/pinpoint-apm/pinpoint/tree/master/metric-module/metric/src/main/pinot)에 테이블 정보가 있다.
* 테이블 생성 방법은 [pinot가이드](https://docs.pinot.apache.org/basics/components/table#streaming-table-creation)를 참고하여 pinot 실행 환경 맞게 테이블을 생성하면 된다.
* 생성하는 테이블은 총 3개이다.
  * systemMetricDataType : 수집되는 데이터의 type 정보를 저장하는 테이블이다.
  * systemMetricTag : 수집되는 데이터의 metadata(host 정보, 데이터의 tag 정보)를 저장하는 테이블이다.
  * systemMetricDouble : double 데이터를 저장하는 테이블이다. hybrid table 기능 사용을 위해서 REALTIME, OFFLINE 테이블 둘다 생성하자.

### 3.3 collector 설정 및 실행

telegraf agent로 부터 전송된 데이터를 수집하기 위해서 collector에 설정을 추가한다.

#### 3.3.A. collector 설정

**1)** pinot와 통신을 위해서 [설정파일](https://github.com/pinpoint-apm/pinpoint/tree/master/pinot/pinot-config/src/main/resources/pinot/profiles)들을 profile에 맞게 수정해야 한다.

* pinot-jdbc.properties 설정 : [3.1](#3.1-pinot-설치-및-실행)에서 설치한 pinot의 주소를 설정한다.
  * ```
            pinpoint.pinot.jdbc.url=jdbc:pinot://localhost:9000
            pinpoint.pinot.jdbc.username=userId
            pinpoint.pinot.jdbc.password=password
    ```

**2)** kafka와 통신을 위해서 [설정파일](https://github.com/pinpoint-apm/pinpoint/tree/master/pinot/pinot-kafka/src/main/resources/profiles)들을 profile에 맞게 수정해야 한다.

* kafka-producer-factory.properties 설정 : kafka 의 주소를 설정한다.
  * ```
            pinpoint.metric.kafka.bootstrap.servers=--KAFKA_ADDRESS--
    ```

#### 3.3.B. collector 실행 방법

빌드 후 pinpoint/metric-module/collector-starter/target/deploy에 생성된 `pinpoint-collector-starter-boot-XXXX.jar`을 실행하면 된다.

* `pinpoint-collector-starter-boot-XXXX.jar` 은 pinpoint-collector 기능과 system metric 수집기능이 합해진 패키지이다.
* metric 기능을 활성화 하기 위해서 실행시 `--pinpoint.collector.type=METRIC` 나 `--pinpoint.collector.type=ALL` 옵션을 추가해야한다.
  * METRIC : system metric 수집기능만 동작된다.
  * ALL : pinpoint collector 기능과 system metric 수집기능이 동시에 동작된다.

### 3.4 web 설정 및 실행

pinot에 저장된 시스템 메트릭 데이터를 보여주기 위해서 web 설정을 수정한다.

#### 3.4.A. web 설정

**1)** pinot와 통신을 위해서 [설정파일](https://github.com/pinpoint-apm/pinpoint/tree/master/pinot/pinot-config/src/main/resources/pinot/profiles)들을 profile에 맞게 수정해야 한다.

* jdbc-pinot.properties 설정 : [3.1](#3.1-pinot-설치-및-실행)에서 설치한 pinot의 주소를 설정한다.
  * ````
        pinpoint.pinot.jdbc.url=jdbc:pinot://localhost:9000
        pinpoint.pinot.jdbc.username=userId
        pinpoint.pinot.jdbc.password=password
        ```
    ````

**2)**

* system metric 기능을 web에서 활성화하기 위해서 [pinpoint-web-metric.properties](https://github.com/pinpoint-apm/pinpoint/tree/master/metric-module/metric/src/main/resources/pinot-web/profiles) 파일을 수정한다.
  * ````
        config.show.systemMetric=true
        ```
    ````

#### 3.4.B. web 실행 방법

빌드 후 pinpoint/metric-module/web-starter/target/deploy에 생성된 `pinpoint-web-starter-boot-XXXX.jar`을 실행하면 된다.

* `pinpoint-web-starter-boot-XXXX.jar` 은 pinpoint web 기능과 metric 데이터 확인 기능이 합해진 패키지이다.

### 3.5 참고

* 참고로 web, collector의 실행파일이 과거 버전과 다르게 다른곳에 존재한다.
* 기존의 web, collector 실행파일 경로와 다르게 system metric기능이 포함된 collector, web은 실행 파일 경로는 다음과 같다.
  * collector : pinpoint/collector/deploy -> pinpoint/metric-module/collector-starter/target/deploy
  * web : pinpoint/web/deploy -> pinpoint/metric-module/web-starter/target/deploy

### 3.6 telegraf agent 설치 및 설정

telegraf agent를 통해 수집된 시스템 메트릭은 다음과 같다.

* cpu
* disk usage
* disk usage(percent)
* inode usage
* memory usage
* memory usage(percent)
* swap
* system load
* nginx
* apache

***

* 시스템 메트릭 데이터를 수집하는 telegraf agent를 설치하자.
  * [telegraf agent 설치 가이드](https://docs.influxdata.com/telegraf/v1.21/introduction/installation/)
* telegraf agent가 http 프로토콜로 collector에 데이터를 전달할 수 있도록 설정파일을 수정 해야한다.
  * telegraf.conf 설정 방법
    * http 프로토콜로 데이터를 전달수 있도록 output http plugin 아래 설정을 추가한다.
      * **참고**: Pinpoint v3.0.2부터 메트릭 포트가 `15200`에서 `9995`로 변경되었습니다.
      * ```
                [[outputs.http]]
                  url = "http://{PINPOINT_COLLECTOR_IP}:9995/telegraf"
                   
                   [outputs.http.headers]
                   hostGroupName = {applicationName}
                   Content-Type = "application/json"
        ```
    * `url`: {PINPOINT\_COLLECTOR\_IP} 자리에 데이터를 수집하는 collector의 주소를 설정한다.
    * `outputs.http.headers`은 서버 그룹의 key와 Content-Type을 설정한다.
      * `hostGroupName`: {applicationName}에 설정한 값을 key로 pinpoint-web에서 데이터를 조회할 수 있다. 핀포인트를 이미 사용 중이라면 application을 추적할 때 agent 설정 값으로 사용했던 applicationName을 사용하는 것을 추천한다.

## 4 데이터 조회

* pinpoint-web에서 왼쪽 `Infrastructure` 메뉴를 선택하여 system metric 화면으로 이동한다.
* 상단의 select box에서 telegraf.conf 파일에 설정한 hostGroupName 값을 찾아서 선택한다.
* 아래와 같이 왼쪽에 호스트 목록이 나오고, 호스트를 선택해서 system metric 데이터를 확인할 수 있다.

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-c894164f22ccffbbac3a17a452c9c99867ae5280%2Fsystem_metric_01.png?alt=media\&token=3509e031-d53c-431c-b924-5ff9bfc768a2)

## 5 기타

* pinot에는 system metric 뿐만아니라 pinpoint의 다양한 메트릭 데이터와 통계 데이터를 저장할 예정이다. 즉 pinot는 다양한 데이터를 저장하는 목적으로 사용될 것이다.
* system metric의 경우 당분간은 beta 기능으로 제공할것이고 안정적으로 기능이 운영되는 경험이 쌓이면 공식적으로 기능을 제공할 것이다.
* 2.5.0 이하 버전에서 system metric 기능을 사용하다가 버전을 업그레이드 하는 경우 [guide](https://github.com/pinpoint-apm/pinpoint/issues/9791#issuecomment-1491486262) 설명을 참고하자.


# URI Statistics

[English](#uri_statistics) | [한국어](#URI_통계)

## URI Statistics

URI statistics menu is newly added to Pinpoint in v2.5.0. Pinpoint Agent aggregates URI templates and send them to Pinpoint collector via GRPC. Pinpoint Collector saves the data to Pinot via Apache Kafka. Pinpoint Web accesses Pinot to display the data.

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-766216ae1ef81bd7cf547351f746d5d7ccc833b7%2Furi_statistics_01.png?alt=media\&token=0c62b604-1c64-4293-8d0e-1f8ded88c148)

### 1. Installation and Configuration

#### 1.1 Install and Run Kafka

Kafka enables real-time streaming of URI statistics data from Pinpoint collector to Pinot. If you have already [set up Kafka for Pinpoint System Metric](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.2.a-kafka-installation-guide), please skip this step.

* Please refer to [this document](https://kafka.apache.org/quickstart) to get Kafka and start the Kafka environment.

#### 1.2 Create Kafka Topics for Pinpoint URI Statistics

Create a topic with the name `url-stat`

```
$ bin/kafka-topics.sh --create --topic url-stat --bootstrap-server ${YOUR_KAFKA_SERVER_ADDRESS}
```

#### 1.3 Install and Run Pinot

This section describes how to install Pinot which is used in Pinpoint to save URI statistics data. If you have already [set up Pinot for Pinpoint System Metric](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.1-install-pinot), please skip this step.

* Install Pinot according to [Pinot Getting Started guide](https://docs.pinot.apache.org/basics/getting-started).
* Above guide gives you the way to run Pinot locally, in Docker, and in Kubernetes.

#### 1.4 Create Pinot Tables

* Pinot table schema for Pinpoint URI statistics is provided in [our github repository](https://github.com/pinpoint-apm/pinpoint/tree/master/uristat/uristat-common/src/main/pinot).
* Please refer to [Pinot documents](https://docs.pinot.apache.org/basics/components/table#streaming-table-creation) to create necessary tables in your Pinot cluster.
* Let's create the uriStat table by referencing the schema file and table settings from the provided path. To enable hybrid table functionality, let's create both REALTIME and OFFLINE tables for the 'uriStat' table.

#### 1.5 Configure and Attach Pinpoint Agent

This section describes the URI stat configuration values added for URI statistics.

**1.5.1 Configuration values for URI Statistics**

Below are default agent configuration values for URI statistics.

```
###########################################################
# URI Stat
###########################################################
profiler.uri.stat.enable=true
profiler.uri.stat.spring.webmvc.enable=true
profiler.uri.stat.spring.webmvc.useuserinput=false
profiler.uri.stat.spring.webflux.enable=true
profiler.uri.stat.spring.webflux.useuserinput=false
profiler.uri.stat.vertx.enable=true
profiler.uri.stat.vertx.useuserinput=false
profiler.uri.stat.tomcat.useuserinput=false
```

* profiler.uri.stat.enable: whether Pinpoint Agent collects URI statistics or not.
  * `true`: collects URI statistics
  * `false`: doesn't collect URI statistics
* profiler.uri.stat.spring.webmvc.enable: whether Pinpoint Agent collects URI statistics from Spring Web MVC applications.
  * `true`: collects URI statistics from Spring Web MVC applications.
  * `false`: doesn't collect URI statistics from Spring Web MVC applications.
* profiler.uri.stat.spring.webmvc.useuserinput: whether Pinpoint Agent uses user-input request attribute values for URI templates when available.

  * `true`: uses user-input request attribute values.
  * `false`: ignores user-input request attribute values.

  Set attribute `pinpoint.metric.uri-template` to your Spring web request as shown below to override default URI template provided by Pinpoint.

  ```
    @RequestMapping("/testUserInputRequestAttribute")
    public Map<String, Object> testUserInputAttribute(HttpServletRequest request) {
        Map<String, Object> map = new HashMap<String, Object>();
        map.put("message", "test user input attribute");
        request.setAttribute("pinpoint.metric.uri-template", "/userInput");
        return map;
    }
  ```
* profiler.uri.stat.spring.webflux.enable: whether Pinpoint Agent collects URI statistics from Spring Webflux applications.
  * `true`: collects URI statistics from Spring Webflux applications.
  * `false`: doesn't collect URI statistics from Spring Webflux applications.
* profiler.uri.stat.spring.webflux.useuserinput: whether Pinpoint Agent uses user-input request attribute values for URI templates when available.

  * `true`: uses user-input request attribute values.
  * `false`: ignores user-input request attribute values.

  Set attribute `pinpoint.metric.uri-template` to your Spring web request as shown below to override default URI template provided by Pinpoint.

  ```
    @GetMapping("/server/welcome/**")
    public Mono<String> welcome(ServerWebExchange exchange) {
        exchange.getAttributes().put("pinpoint.metric.uri-template", "/test");
        return Mono.just("Welcome Home");
    }
  ```
* profiler.uri.stat.vertx.enable: whether Pinpoint Agent collects URI statistics from Vert.x applications.
  * `true`: collects URI statistics from Vert.x applications.
  * `false`: doesn't collect URI statistics from Vert.x applications.
* profiler.uri.stat.vertx.useuserinput: whether Pinpoint Agent uses user-input routing context attribute values for URI templates when available.

  * `true`: uses user-input routing context attribute values.
  * `false`: ignores user-input routing context attribute values.

  Set attribute `pinpoint.metric.uri-template` to your Vert.x routing context as shown below to override default URI template provided by Pinpoint.

  ```
    router.get("/routinContextAttributeAdded").handler(routingContext -> {
        routingContext.put("pinpoint.metric.uri-template", "/test");
        routingContext.response().end("pinpoint.metric.uri-tempate = /test");
    });
  ```
* profiler.uri.stat.tomcat.useuserinput: (Added in v2.5.3) whether Pinpoint Agent uses user-input attribute values from Tomcat for URI templates when available.

  * `true`: collects URI statics from Tomcat user-input attribute values.
  * `false`: doesn't check Tomcat request attributes for URI statistics.

  This is provided to collect URI statistics information in Tomcat applications without supported frameworks(Spring WebMVC, Spring Webflux, VertX). If you are using supported frameworks, it is recommended to use framework-specific options and disable this option. Since there is no default URI template provided by tomcat, users need to set attribute `pinpoint.metric.uri-template` to your Tomcat request to start collecting URI statistics information.

To change the configuration values described above, update `pinpoint.config` under [each profile directory](https://github.com/pinpoint-apm/pinpoint/tree/master/agent/src/main/resources/profiles) and rebuild the project. Or, you can simply pass these properties when starting your application with Pinpoint Agent (e.g. `-Dprofiler.uri.stat.enable=false`).

#### 1.6 Configure and Run Pinpoint Collector & Web with URI Statistics

Instead of the default Pinpoint Collector and Web binaries, you should use those compiled under metric-module.

Please check [here](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.3-configure-and-run-pinpoint-collector-with-system-metrics) for Pinpoint Metric Collector properties.

* Enable URI statistics by adding the below line at [pinpoint-collector.properties](https://github.com/pinpoint-apm/pinpoint/tree/master/metric-module/collector-starter/src/main/resources/profiles):

  ```
  collector.stat.uri=true
  ```
* `pinpoint.collector.type=BASIC` argument should be used to collect URI statistics in collector.

Please check [here](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.4-configure-and-run-pinpoint-web-with-system-metrics) for Pinpoint Metric Web properties.

* Enable URI statistics by adding the below line at [pinpoint-web-uristat.properties](https://github.com/pinpoint-apm/pinpoint/tree/master/uristat/uristat-web/src/main/resources/profiles):

  ```
  config.show.urlStat=true
  ```

### 2. View Collected URI Statistics Data

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-478271df836f370ea719470568b103ee42d51a81%2Furi_statistics_02.png?alt=media\&token=baf016a1-68ea-41ed-ad22-2017d4982154)

1. Click `URL Statistic` on the side bar menu in Pinpoint web.
2. Search for the application name you used to configure Pinpoint Agent.
3. Top 50 URIs used in your application will be displayed below the empty chart.
4. Click each URI to load the chart.

## URI 통계

URI 통계 기능은 핀포인트 v2.5.0에 신규로 추가되었다. 핀포인트 에이전트에서 URI 템플릿 정보를 수집하여 GRPC를 사용해 핀포인트 콜렉터에 전달하고, 핀포인트 콜렉터는 아파치 카프카를 통해 아파치 피노에 값을 저장한다. 핀포인트 웹에서 저장된 URI 통계 데이터를 확인할 수 있다.

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-766216ae1ef81bd7cf547351f746d5d7ccc833b7%2Furi_statistics_01.png?alt=media\&token=0c62b604-1c64-4293-8d0e-1f8ded88c148)

### 1. 설치 및 설정 방법

#### 1.1 카프카 설치 및 실행

실시간으로 핀포인트 콜렉터에서 데이터를 전달받아 피노에 저장하기 위해서 카프카를 설치해야 한다. 이미 [시스템 메트릭 설정을 하면서 카프카를 설치](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.2-kafka)하였다면, 이 부분은 건너뛰십시오.

* [설치 방법 가이드](https://kafka.apache.org/quickstart)를 참고하여 kafka를 설치한다.

#### 1.2 카프카 토픽 생성

아래와 같이 `url-stat` 토픽을 생성한다.

```
$ bin/kafka-topics.sh --create --topic url-stat --bootstrap-server ${YOUR_KAFKA_SERVER_ADDRESS}
```

#### 1.3 피노 설치 및 실행

URI 통계 값을 저장하는 피노를 설치하는 법을 안내한다. 이미 [시스템 메트릭 설정을 하면서 피노를 설치](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.1.a.-pinot)하였다면, 이 부분은 건너뛰십시오.

* [피노 설치 가이드](https://docs.pinot.apache.org/basics/getting-started)를 참고하여 피노를 설치한다.
* 다양한 환경 (local, docker, kubernetes)에서 피노 실행 환경을 구성할 수 있으니 위 가이드를 참고하자.

#### 1.4 피노 테이블 스키마 및 테이블 생성

* [핀포인트 깃헙 저장소](https://github.com/pinpoint-apm/pinpoint/tree/master/uristat/uristat-common/src/main/pinot)에 URI 통계를 위한 피노 테이블 스키마와 테이블 정보가 있다.
* 위 경로에서 스키마 파일과 테이블 설정을 참고해서 `uriStat` 테이블을 생성한다. hybrid table 기능 사용을 위해서 REALTIME, OFFLINE 테이블 둘다 생성하자.
* 피노에 필요한 테이블을 구성하는 방법은 [피노 공식 문서](https://docs.pinot.apache.org/basics/components/table#streaming-table-creation)를 참고하자.

#### 1.5 핀포인트 에이전트 설정

URI 통계 수집을 위해 핀포인트 에이전트에 설정해야 하는 값들을 안내한다.

**1.5.1 URI 통계 수집을 위한 설정 값**

URI 통계 수집과 관련된 핀포인트 에이전트의 설정 기본값들은 아래와 같다.

```
###########################################################
# URI Stat
###########################################################
profiler.uri.stat.enable=true
profiler.uri.stat.spring.webmvc.enable=true
profiler.uri.stat.spring.webmvc.useuserinput=false
profiler.uri.stat.spring.webflux.enable=true
profiler.uri.stat.spring.webflux.useuserinput=false
profiler.uri.stat.vertx.enable=true
profiler.uri.stat.vertx.useuserinput=false
profiler.uri.stat.tomcat.useuserinput=false
```

* profiler.uri.stat.enable: 핀포인트 에이전트가 URI 통계를 수집하는지 여부.
  * `true`: URI 통계를 수집한다.
  * `false`: URI 통계를 수집하지 않는다.
* profiler.uri.stat.spring.webmvc.enable: 핀포인트 에이전트가 스프링 웹 MVC 어플리케이션에서 URI 통계를 수집하는지 여부.
  * `true`: 스프링 웹 MVC 어플리케이션에서 URI 통계를 수집힌다.
  * `false`: 스프링 웹 MVC 어플리케이션에서 URI 통계를 수집하지 않는다.
* profiler.uri.stat.spring.webmvc.useuserinput: 핀포인트 에이전트가 스프링 웹 어플리케이션에서 사용자 정의 URI 템플릿을 우선적으로 사용하는지 여부.

  * `true`: 스프링 웹 어플리케이션에서 사용자 정의 URI 템플릿을 우선적으로 사용한다.
  * `false`: 스프링 웹 어플리케이션에서 사용자 정의 URI 템플릿을 확인하지 않고 핀포인트가 수집한 템플릿만 사용한다.

  핀포인트에서 수집하는 URI 템플릿을 사용하지 않고 사용자 정의 URI 템플릿을 사용하고 싶다면, 아래 예제와 같이 스프링 웹 리퀘스트 객체 attribute에 `pinpoint.metric.uri-template`를 key 값으로 하는 속성 값을 설정해야 한다.

  ```
    @RequestMapping("/testUserInputRequestAttribute")
    public Map<String, Object> testUserInputAttribute(HttpServletRequest request) {
        Map<String, Object> map = new HashMap<String, Object>();
        map.put("message", "test user input attribute");
        request.setAttribute("pinpoint.metric.uri-template", "/userInput");
        return map;
    }
  ```
* profiler.uri.stat.spring.webflux.enable: 핀포인트 에이전트가 스프링 웹플럭스 어플리케이션에서 URI 통계를 수집하는지 여부.
  * `true`: 스프링 웹플럭스 어플리케이션에서 URI 통계를 수집힌다.
  * `false`: 스프링 웹플럭스 어플리케이션에서 URI 통계를 수집하지 않는다.
* profiler.uri.stat.spring.webflux.useuserinput: 핀포인트 에이전트가 스프링 웹플럭스 어플리케이션에서 사용자 정의 URI 템플릿을 우선적으로 사용하는지 여부.

  * `true`: 스프링 웹플럭스 어플리케이션에서 사용자 정의 URI 템플릿을 우선적으로 사용한다.
  * `false`: 스프링 웹플럭스 어플리케이션에서 사용자 정의 URI 템플릿을 확인하지 않고 핀포인트가 수집한 템플릿만 사용한다.

  핀포인트에서 수집하는 URI 템플릿을 사용하지 않고 사용자 정의 URI 템플릿을 사용하고 싶다면, 아래 예제와 같이 스프링 웹 리퀘스트 객체 attribute에 `pinpoint.metric.uri-template`를 key 값으로 하는 속성 값을 설정해야 한다.

  ```
    @GetMapping("/server/welcome/**")
    public Mono<String> welcome(ServerWebExchange exchange) {
        exchange.getAttributes().put("pinpoint.metric.uri-template", "/test");
        return Mono.just("Welcome Home");
    }
  ```
* profiler.uri.stat.vertx.enable: 핀포인트 에이전트가 Vert.x 어플리케이션에서 URI 통계를 수집하는지 여부.
  * `true`: Vert.x 어플리케이션에서 URI 통계를 수집힌다.
  * `false`: Vert.x 어플리케이션에서 URI 통계를 수집하지 않는다.
* profiler.uri.stat.vertx.useuserinput: 핀포인트 에이전트가 Vert.x 어플리케이션에서 사용자 정의 URI 템플릿을 우선적으로 사용하는지 여부.

  * `true`: Vert.x 어플리케이션에서 사용자 정의 URI 템플릿을 우선적으로 사용한다.
  * `false`: Vert.x 어플리케이션에서 사용자 정의 URI 템플릿을 확인하지 않고 핀포인트가 수집한 템플릿만 사용한다.

  핀포인트에서 수집하는 URI 템플릿을 사용하지 않고 사용자 정의 URI 템플릿을 사용하고 싶다면, 아래 예제와 같이 Vert.x RoutingContext 객체에 `pinpoint.metric.uri-template` 를 key 값으로 하는 속성 값을 설정해야 한다.

  ```
    router.get("/routinContextAttributeAdded").handler(routingContext -> {
        routingContext.put("pinpoint.metric.uri-template", "/test");
        routingContext.response().end("pinpoint.metric.uri-tempate = /test");
    });
  ```
* profiler.uri.stat.tomcat.useuserinput: (v2.5.3에 추가 됨) 핀포인트 에이전트가 Tomcat 어플리케이션에서 사용자 정의 URI 템플릿을 사용하여 통계를 수집하는지 여부.

  * `true`: Tomcat 어플리케이션에서 사용자 정의 URI 템플릿을 사용하여 URI 통계를 수집한다.
  * `false`: URI 통계 수집을 할 때 Tomcat 리퀘스트 attribute를 확인하지 않는다.

  이 옵션은 지원하는 프레임워크(Spring WebMVC, Spring Webflux, VertX)를 사용하지 않는 Tomcat 어플리케이션에서 URI 통계를 수집하기 위해 추가되었습니다. 만약 지원하는 프레임워크를 사용하고 있다면, 해당 프레임워크 관련 URI 통계 옵션을 사용하고 이 옵션은 false로 사용하는 것을 권장합니다. 지원하는 프레임워크에서와는 다르게 Tomcat 자체적으로 URI 템플릿을 제공하지 않기 때문에, 이 옵션을 사용할 경우, 사용자가 직접 Tomcat request attribute에 `pinpoint.metric.uri-template`를 추가하여야만 URI 통계가 수집됩니다.

위 설정 값들을 변경하려면 원하는 [핀포인트 프로파일 경로](https://github.com/pinpoint-apm/pinpoint/tree/master/agent/src/main/resources/profiles)의 `pinpoint.config` 파일에서 값을 변경하여 핀포인트를 재빌드한다. 파일을 수정하지 않고, 핀포인트 에이전트를 붙힐 어플리케이션을 실행할 때 `-Dprofiler.uri.stat.enable=false`와 같이 값을 넣어도 된다.

#### 1.6 핀포인트 콜렉터와 핀포인트 웹 설정 및 실행

URI 통계를 수집하고 값을 확인하려면, 핀포인트 v2.5.0 이전 버전에서 사용하던 콜렉터와 웹 JAR 파일이 아니라 metric-module 밑에 생성되는 파일을 사용해야 한다.

[핀포인트 메트릭 콜렉터를 설명한 문서](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.3-collector)에 자세한 설명이 있으니 참고해서 메트릭 콜렉터 설정값을 세팅하자.

* 위 설정 외에 URI 통계를 위해 [pinpoint.collector.properties](https://github.com/pinpoint-apm/pinpoint/tree/master/metric-module/collector-starter/src/main/resources/profiles)에 아래 설정값이 추가되었다:

  ```
  collector.stat.uri=true
  ```
* URI 통계를 수집하기 위해서는 콜렉터를 시작할 때 `pinpoint.collector.type=BASIC` argument를 넣어야 한다.

[핀포인트 메트릭 웹을 설명한 문서](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.4-web)에 자세한 설명이 있으니 참고해서 메트릭 웹 설정값을 세팅하자.

* 위 설정 외에 URI 통계를 위해 [pinpoint-web-uristat.properties](https://github.com/pinpoint-apm/pinpoint/tree/master/uristat/uristat-web/src/main/resources/profiles)에 아래 설정값이 추가되었다:

  ```
  config.show.urlStat=true
  ```

### 2. URI 통계 데이터 조회

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-478271df836f370ea719470568b103ee42d51a81%2Furi_statistics_02.png?alt=media\&token=baf016a1-68ea-41ed-ad22-2017d4982154)

1. 핀포인트 메트릭 웹을 실행하여 왼쪽 `URL Statistic` 메뉴를 선택한다.
2. 상단의 seslect box에서 핀포인트 에이전트에 설정한 어플리케이션 이름을 조회한다..
3. 초기 화면에서는 선택한 어플리케이션에서 가장 많이 사용한 상위 50개 URI가 빈 차트 밑에 표시된다.
4. 원하는 URI를 클릭하면 차트에 데이터가 표시된다.


# URI Statistics Alarm

## URI Statistics Alarms

Alarms for URI statistics will be introduced to Pinpoint in v3.0.0. Similar to the existing [alarms in Pinpoint](https://pinpoint-apm.gitbook.io/pinpoint/documents/alarm), pinpoint-batch server checks every 3 minutes if configured alarm rules are triggered with data in the last 5 minutes.

### 1. Alarm Rules

Alarms rules can be created for each URI, using data collected with [URI Statistics](https://pinpoint-apm.gitbook.io/pinpoint/documents/uri_statistics).

#### Alarm Data

* APDEX: The APDEX score of the specified URI for the past 5 minutes (0.00 \~ 1.00)
* Average Response Time: The avgerage response time of the specified URI for the past 5 minutes (ms)
* Maximum Response Time: The maximum response time of the specified URI for the past 5 minutes (ms)
* Total Request Count: The total number of requests made to the specified URI in the past 5 minutes
* Failed Request Count: The number of failed requests to the specified URI in the past 5 minutes

#### Alarm Condition

When setting up a new alarm, the conditions for triggering the alarm need to be specified. You can choose from the following comparison operators:

* (collected value) `>` (threshold value)
* (collected value) `>=` (threshold value)
* (collected value) `==` (threshold value)
* (collected value) `<` (threshold value)
* (collected value) `<=` (threshold value)

### 2. Configuration and Implementation

To use URI Statistics Alarms, MYSQL table `pinot_alarm_history`, `pinot_alarm_rule`, and `pinot_webhook_send` need to be added.

```
CREATE TABLE `pinot_alarm_history` (
  `history_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `rule_id` int(10) unsigned NOT NULL,
  `timestamp` datetime NOT NULL,
  PRIMARY KEY (`history_id`)
);
```

```
CREATE TABLE `pinot_alarm_rule` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `service_name` varchar(30) NOT NULL,
  `application_name` varchar(30) NOT NULL,
  `category_name` varchar(30) NOT NULL,
  `checker_name` varchar(30) NOT NULL,
  `target` varchar(256) NOT NULL,
  `condition` varchar(30) NOT NULL,
  `threshold` decimal(10,2) DEFAULT NULL,
  `baseline` varchar(30) DEFAULT NULL,
  `user_group_id` varchar(30) NOT NULL,
  `sms_send` char(1) DEFAULT NULL,
  `email_send` char(1) DEFAULT NULL,
  `webhook_send` char(1) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
```

```
CREATE TABLE `pinot_webhook_send` (
  `webhook_send_info_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `webhook_id` int(10) unsigned NOT NULL,
  `rule_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`webhook_send_info_id`),
  UNIQUE KEY `webhook_send_info_id_UNIQUE` (`webhook_send_info_id`)
);
```

### 3. How to add alarms on Web UI

(TO BE UPDATED)

## URI 통계 알람

[URI 통계](https://pinpoint-apm.gitbook.io/pinpoint/documents/uri_statistics)를 이용한 알람 기능은 핀포인트 2.6.0에 추가되었습니다. 기존 [핀포인트 알람](https://pinpoint-apm.gitbook.io/pinpoint/documents/alarm)에서와 동일하게 pinpoint-batch 서버가 매 3분동안 지난 5분간의 데이터가 알람 조건을 만족하는 지 체크합니다.

### 1. 설정 가능한 알람

[URI 통계](https://pinpoint-apm.gitbook.io/pinpoint/documents/uri_statistics) 기능으로 수집한 통계값을 사용하여 특정 URI에 대해 아래와 같은 조건으로 알람을 설정할 수 있습니다.

#### 알람 대상 데이터

* APDEX: 해당 URI의 과거 5분 동안의 APDEX 점수 (0.00 \~ 1.00)
* 평균 응답 속도: 해당 URI의 과거 5분 동안의 평균 응답 속도 (ms)
* 최대 응답 속도: 해당 URI의 과거 5분 동안의 최대 응답 속도 (ms)
* 전체 요청 수: 해당 URI의 과거 5분 동안의 전체 request 개수
* 실패 요청 수: 해당 URI의 과거 5분 동안 실패한 request의 개수

#### 알람 조건

새로운 알람을 등록할 때 수집한 값이 지정한 임계값과 비교해서 어떤 조건일 때 알람이 울리는 지 설정하게 됩니다. 다음 비교 연산자 중에서 선택할 수 있고 아래 조건이 만족하면 알람이 울립니다.

* (수집한 값) `>` (설정한 값)
* (수집한 값) `>=` (설정한 값)
* (수집한 값) `==` (설정한 값)
* (수집한 값) `<` (설정한 값)
* (수집한 값) `<=` (설정한 값)

### 2. 설치 및 설정 방법

URI 통계 알람을 사용하기 위해서는 MYSQL table 세 개( `pinot_alarm_history`, `pinot_alarm_rule`, `pinot_webhook_send`)를 추가해야 합니다.

```
CREATE TABLE `pinot_alarm_history` (
  `history_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `rule_id` int(10) unsigned NOT NULL,
  `timestamp` datetime NOT NULL,
  PRIMARY KEY (`history_id`)
);
```

```
CREATE TABLE `pinot_alarm_rule` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `service_name` varchar(30) NOT NULL,
  `application_name` varchar(30) NOT NULL,
  `category_name` varchar(30) NOT NULL,
  `checker_name` varchar(30) NOT NULL,
  `target` varchar(256) NOT NULL,
  `condition` varchar(30) NOT NULL,
  `threshold` decimal(10,2) DEFAULT NULL,
  `baseline` varchar(30) DEFAULT NULL,
  `user_group_id` varchar(30) NOT NULL,
  `sms_send` char(1) DEFAULT NULL,
  `email_send` char(1) DEFAULT NULL,
  `webhook_send` char(1) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
```

```
CREATE TABLE `pinot_webhook_send` (
  `webhook_send_info_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `webhook_id` int(10) unsigned NOT NULL,
  `rule_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`webhook_send_info_id`),
  UNIQUE KEY `webhook_send_info_id_UNIQUE` (`webhook_send_info_id`)
);
```

### 3. 알람 추가하는 법

\[ Web 구현 후 추가 예정]


# Error Analysis

[English](#error_analysis) | [한국어](#1.설치_및_설정_방법)

## Error Analysis

![](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-66f5caa12ca010e28eb6c3e1bce69e98e300ea2f%2Ferror_analysis_01.png?alt=media)

Error Analysis is a new feature introduced in Pinpoint v3.0.0.

The Pinpoint agent collects more detailed exception information and transmits it to the Pinpoint collector via gRPC. The Pinpoint collector then stores this data in Apache Pinot through Apache Kafka. You can view the stored Error Analysis data in the Pinpoint web interface.

## 1. Installation and Configuration Guide

### 1.1. Kafka Installation and Configuration

To store data from the Pinpoint Collector into Pinot, Kafka needs to be installed. If you have already installed Kafka during the [system metric setup](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.2-kafka), you can skip this section.

#### 1.1.1. Kafka Installation

Refer to the [Kafka Quickstart Guide](https://kafka.apache.org/quickstart) for detailed instructions on installing Kafka.

#### 1.1.2. Kafka Topic Creation

You need to create a topic named `exception-trace`. Use the following command to create the `exception-trace` topic:

```shell
$ bin/kafka-topics.sh --create --topic exception-trace --bootstrap-server ${YOUR_KAFKA_SERVER_ADDRESS}
```

### 1.2. Pinot Installation and Configuration

To store collected data, Pinot must be installed. If you have already completed the Pinot installation during the [system metric setup](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.1.a.-pinot), you can skip this section.

#### 1.2.1. Pinot Installation

Refer to the [Pinot Getting Started Guide](https://docs.pinot.apache.org/basics/getting-started) for detailed instructions on installing Pinot. Pinot can be set up in various environments (local, Docker, Kubernetes), so follow the guide that best fits your setup.

Pinpoint Error Analysis requires [CLP (Compressed Log Processor)](https://docs.pinot.apache.org/basics/data-import/clp), supported from Pinot version 1.0.0, to appropriately process and group error messages. Please ensure you are using the correct version.

Due to the binary issue with `clp-ffi-java`, we recommend using an amd64-based / x86-based machine when installing Pinot version 1.0.0. [Related Issue](https://github.com/pinpoint-apm/pinpoint/issues/11170)

#### 1.2.2. Pinot Table Schema and Table Creation

Create the following table in Pinot:

* `exceptionTrace`

Refer to the [table schema file](https://github.com/pinpoint-apm/pinpoint/tree/master/exceptiontrace/exceptiontrace-common/src/main/pinot) for details on creating the table.

### 1.3. Pinpoint Agent Configuration

This section covers the settings related to Error Analysis data collection. The default settings for the release profile are as follows:

```config
###########################################################
# Exception Trace
###########################################################
profiler.exceptiontrace.enable=true
# Permits per second
profiler.exceptiontrace.new.throughput=1000
profiler.exceptiontrace.errormessage.max=2048
# Permits depth of exception. if max depth is 0, it is unlimited.
profiler.exceptiontrace.max.depth=5
profiler.exceptiontrace.io.buffering.buffersize=20
```

* `profiler.exceptiontrace.enable`
  * `true`: Collects exceptions that occur. **Default**
  * `false`: Does not collect exceptions that occur.
* `profiler.exceptiontrace.new.throughput`
  * **Default**: `1000`
  * Determines how many exceptions per second to collect from the agent.
* `profiler.exceptiontrace.errormessage.max`
  * **Default**: `2048`
  * Determines the maximum length of the error message for exceptions collected by the agent.
* `profiler.exceptiontrace.max.depth`
  * **Default**: `5`
  * Determines the depth to traverse the exception chain.
  * If the value is 0, it will traverse until `Throwable.getCause()` returns null.
* `profiler.exceptiontrace.io.buffering.buffersize`
  * **Default**: `20`
  * Determines the number of exceptions to buffer.
  * This buffer is approximately the size of the buffer generated per Span.

### 1.4. Pinpoint Collector and Web Configuration and Execution

#### 1.4.1. Collector Configuration and Execution

The collector configuration is basically the same as for system metrics. Refer to the [Pinpoint Metric Collector](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.3-collector) documentation for detailed setup instructions.

In addition to setting the addresses for Pinot and Kafka and enabling metric collection, ensure that `pinpoint.modules.collector.exceptiontrace.enabled=true` is set to enable exception storage. **Default**: `true`

#### 1.4.2. Web Configuration and Execution

The web configuration is essentially the same as for system metrics. Refer to the [Pinpoint Metric Web](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.4-web) documentation for detailed setup instructions.

Additionally, ensure that `pinpoint.modules.web.exceptiontrace.enabled=true` is set to enable reading exception data. **Default**: `true`

For Error Analysis, the following setting is added to `pinpoint-web-metric.properties` to control whether the Error Analysis item is displayed in the side menu. **Default**: `true`

```config
config.show.exceptionTrace=true
```

***

## Error Analysis

Error Analysis 는 핀포인트 v3.0.0 에 신규로 추가되었다. 핀포인트 에이전트에서 보다 상세한 Exception 정보를 수집하여 gRPC 를 통해 핀포인트 콜렉터로 전달한다. 핀포인트 콜렉터는 이를 아파치 카프카를 통해 아파치 피노에 값을 저장한다. 핀포인트 웹에서 저장된 Error Analysis 를 확인할 수 있다.

## 1. 설치 및 설정 방법

### 1.1. 카프카 Kafka 설치 및 설정

핀포인트 콜렉터에서 피노Pinot 에 데이터를 저장하기 위해서는 카프카를 설치해야한다. 이미 [시스템 메트릭 설정](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.2-kafka) 과정 중에 카프카를 설치하였다면, 이 부분은 건너뛴다.

#### 1.1.1. 카프카 Kafka 설치

[설치 방법 가이드](https://kafka.apache.org/quickstart)를 참고하여 kafka를 설치한다.

#### 1.1.2. 카프카 Kafka 토픽 생성

`exception-trace` 라는 이름의 topic 을 생성해야 한다. 아래와 같이 `exception-trace` 토픽을 생성한다.

```shell
$ bin/kafka-topics.sh --create --topic exception-trace --bootstrap-server ${YOUR_KAFKA_SERVER_ADDRESS}
```

### 1.2. 피노 Pinot 설치 및 설정

수집된 데이터를 저장하기 위해서는 피노 Pinot 를 설치해야한다. 이미 [시스템 메트릭 설정](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.1.a.-pinot) 과정 중에 피노를 설치하였다면, 이 부분은 건너뛴다.

#### 1.2.1. 피노 Pinot 설치

[피노 설치 가이드](https://docs.pinot.apache.org/basics/getting-started)를 참고하여 피노를 설치한다. 다양한 환경 (local, docker, kubernetes)에서 피노 실행 환경을 구성할 수 있으니 위 가이드를 참고하자.

핀포인트는 Error Message 를 적절히 처리하고 그룹화하기 위해 Pinot 1.0.0 부터 지원하는 [CLP (Compressed Log Processor)](https://docs.pinot.apache.org/basics/data-import/clp) 가 필요하다. 버전에 주의할 것.

#### 1.2.2. 피노 Pinot 테이블 스키마 및 테이블 생성

피노 Pinot 에 다음 테이블을 새로 생성한다.

* `exceptionTrace` [테이블 생성 스키마 파일](https://github.com/pinpoint-apm/pinpoint/tree/master/exceptiontrace/exceptiontrace-common/src/main/pinot)의 테이블 정보를 참고하여 생성한다.

### 1.3 핀포인트 에이전트 설정

Error Analysis 데이터 수집과 관련된 설정이다. release 프로필의 기본 설정은 다음과 같다.

```config
###########################################################
# Exception Trace
###########################################################
profiler.exceptiontrace.enable=true
# Permits per second
profiler.exceptiontrace.new.throughput=1000
profiler.exceptiontrace.errormessage.max=2048
# Permits depth of exception. if max depth is 0, it is unlimited.
profiler.exceptiontrace.max.depth=5
profiler.exceptiontrace.io.buffering.buffersize=20
```

* `profiler.exceptiontrace.enable`
  * `true`: 발생하는 exception 을 수집한다. **기본값**
  * `false` : 발생하는 exception 을 수집하지 않는다.
* `profiler.exceptiontrace.new.throughput`
  * **기본값** 1000
  * 해당 에이전트에서 초당 몇개까지의 exception 을 수집할지 결정한다.
* `profiler.exceptiontrace.errormessage.max`
  * **기본값** 2048
  * 해당 에이전트에서 발생하는 exception 의 error message 를 몇자까지 수집할지 결정한다.
* `profiler.exceptiontrace.max.depth`
  * **기본값** 5
  * exception chain 이 주어졌을 때, 깊이를 어느정도 순회할지 결정한다.
  * 값이 0이면 Throwable.getCause() 가 null 일 때까지 순회한다.
* `profiler.exceptiontrace.io.buffering.buffersize`
  * **기본값** 20
  * buffer 에 exception 을 몇개까지 쌓아둘지 결정한다.
  * 해당 buffer 는 대략 Span 단위로 생성되는 buffer 이다.

### 1.4 핀포인트 콜렉터와 핀포인트 웹 설정 및 실행

### 1.4.1. collector 설정 및 실행

collector 설정은 기본적으로 system metric 와 동일하다. [핀포인트 메트릭 콜렉터](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.3-collector)를 설명한 문서에 자세한 설명이 있으니 참고해서 메트릭 콜렉터 설정값을 세팅하자.

이처럼 pinot 과 kafka 의 주소를 알려주고 metric 수집 기능을 활성화하면 된다.

이에 추가적으로 `pinpoint.modules.collector.exceptiontrace.enabled=true` 로 되어있어야 exception 을 저장한다. **기본값** `true`

### 1.4.2 web 설정 및 실행

web 설정은 기본적으로 system metric 와 동일하다. [핀포인트 메트릭 웹](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.4-web)을 설명한 문서에 자세한 설명이 있으니 참고해서 메트릭 웹 설정값을 세팅하자.

이에 추가적으로 `pinpoint.modules.web.exceptiontrace.enabled=true` 로 되어있어야 exception 데이터를 읽어온다. **기본값** `true`

위 설정 외에 Error Analysis 를 위해 pinpoint-web-metric.properties에 아래 설정값이 추가되었다: 이 설정은 좌측 사이드 메뉴에서 Error Analysis 항목을 노출시킬지 결정한다. **기본값**`true`

* ```
    config.show.exceptionTrace=true
  ```


# How to use Application Inspector

[English](#application-inspector) | [한국어](#application-inspector-1)

## Application Inspector

### 1. Introduction

Application inspector provides an aggregate view of all the agent's resource data (cpu, memory, tps, datasource connection count, etc) registered under the same application name. A separate view is provided for the application inspector with stat charts similar to the agent inspector.

To access application inspector, click on the application inspector menu on the left side of the screen.

* 1 : application inspector menu, 2 : application stat data

  ![inspector\_view.jpg](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-1db8d686fb94a6f086fd1b0c665759237de98e86%2Finspector_view.jpg?alt=media\&token=22949d0d-a2aa-4e1e-9642-376355be3521)

The Heap Usage chart above for example, shows the average(Avg), smallest(Min), greatest(Max) heap usage of the agents registered under the same application name along with the id of the agent that had the smallest/greatest heap usage at a certain point in time. The application inspector also provides other statistics found in the agent inspector in a similar fashion.

![graph.jpg](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-1b9fe2dfc5933f8a6d8dcfee8cf77076489f34c7%2Fgraph.jpg?alt=media\&token=d6892cf4-8086-4bce-899e-65baa9b12221)

Application inspector requires [flink](https://flink.apache.org) and [zookeeper](https://zookeeper.apache.org/). Please read on for more detail.

### 2. Architecture

![execute\_flow.jpg](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-67c467a049c249107c3d9f9c23d24c98270ddfd1%2Fexecute_flow.jpg?alt=media\&token=a7960f59-0384-4e26-89ac-64fdcf2aa3ba)

**A.** Run a streaming job on [flink](https://flink.apache.org).\
**B.** The taskmanager server is registered to zookeeper as a data node once the job starts.\
**C.** The Collector obtains the flink server info from zookeeper to create a tcp connection with it and starts sending agent data.\
**D.** The flink server aggregates data sent by the Collector and stores them into hbase.

### 3. Configuration

In order to enable application inspector, you will need to do the following and run Pinpoint.

**A.** Create **ApplicationStatAggre** table (refer to [create table script](https://github.com/pinpoint-apm/pinpoint/tree/master/hbase/scripts)), which stores application stat data.

**B.** Configure zookeeper address in [Pinpoint-flink.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/flink/src/main/resources/pinpoint-flink.properties) which will be used to store flink's taskmanager server information.

```
    flink.cluster.enable=true
    flink.cluster.zookeeper.address=YOUR_ZOOKEEPER_ADDRESS
    flink.cluster.zookeeper.sessiontimeout=3000
    flink.cluster.zookeeper.retry.interval=5000
    flink.cluster.tcp.port=19994
```

**C.** Configure job execution type and the number of listeners to receive data from the Collector in [Pinpoint-flink.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/flink/src/main/resources/profiles/release/pinpoint-flink.properties).

* If you are running a flink cluster, set *flink.StreamExecutionEnvironment* to **server**.
* If you are running flink as a standalone, set *flink.StreamExecutionEnvironment* to **local**.

  ```
    flink.StreamExecutionEnvironment=server
  ```

**D.** Configure hbase address in [hbase.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/flink/src/main/resources/profiles/release/hbase.properties) which will be used to store aggregated application data.

```
    hbase.client.host=YOUR_HBASE_ADDRESS
    hbase.client.port=2181
```

**E.** Build [Pinpoint-flink](https://github.com/pinpoint-apm/pinpoint/tree/master/flink) and run the streaming job file created under *target* directory on the flink server.

* The name of the streaming job is `pinpoint-flink-job-{pinpoint.version}.jar`.
* For details on how to run the job, please refer to the [flink website](https://flink.apache.org).
* You must put `spring.profiles.active release` or`spring.profiles.active local` as the job parameter so that the job can refer to the configuration file configured above when running. It must be entered because it uses the spring profile function inside the job to refer to the configuration file.

**F.** Configure zookeeper address in [Pinpoint-Collector.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/collector/src/main/resources/profiles/release/pinpoint-collector.properties) so that the Collector can connect to the flink server.

```
    flink.cluster.enable=true
    flink.cluster.zookeeper.address=YOUR_ZOOKEEPER_ADDRESS
    flink.cluster.zookeeper.sessiontimeout=3000
```

**G.** Enable application inspector in the web-ui by enabling the following configuration in [pinpoint-web.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/pinpoint-web-root.properties).

```
    config.show.applicationStat=true
```

### 4. Monitoring Streaming Jobs

There is a batch job that monitors how Pinpoint streaming jobs are running. To enable this batch job, configure the following files for *Pinpoint-web*.

**batch.properties**

```
batch.flink.server=FLINK_MANGER_SERVER_IP_LIST
# Flink job manager server IPs, separated by ','.
# ex) batch.flink.server=123.124.125.126,123.124.125.127
```

**applicationContext-batch-schedule.xml**

```markup
<task:scheduled-tasks scheduler="scheduler">
    ...
    <task:scheduled ref="batchJobLauncher" method="flinkCheckJob" cron="0 0/10 * * * *" />
</task:scheduled-tasks>
```

If you would like to send alarms in case of batch job failure, you must implement `com.navercorp.pinpoint.web.batch.JobFailMessageSender class` and register it as a Spring bean.

### 5. Others

For more details on how to install and operate flink, please refer to the [flink website](https://flink.apache.org).

## Application Inspector

### 1. 기능 설명

application inspector 기능은 agent들의 리소스 데이터(stat : cpu, memory, tps, datasource connection count)를 집계하여 데이터를 보여주는 기능이다. 참고로 application은 agent의 그룹으로 이뤄진다. 그리고 agent의 리소스 데이터는 agent inspector 화면에서 에서 볼 수 있다. application inspector 기능 또한 별도의 화면에서 확인할 수 있다.

inspector 화면 왼쪽 메뉴의 링크를 클릭하면 application inspector 버튼을 클릭하고 데이터를 볼 수 있다.

* 1 : application inspector menu, 2: application stat data

  ![inspector\_view.jpg](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-1db8d686fb94a6f086fd1b0c665759237de98e86%2Finspector_view.jpg?alt=media\&token=22949d0d-a2aa-4e1e-9642-376355be3521)

예를들면 A라는 application에 포함된 agent들의 heap 사용량을 모아서 heap 사용량 평균값 , heap 사용량의 평균값, heap 사용량이 가장 높은 agentid와 사용량, heap 사용량이 가장 적은 agentid와 사용량을 보여준다. 이외에도 agent inspector 에서 제공하는 다른 데이터들도 집계하여 application inspector에서 제공한다.

![graph.jpg](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-1b9fe2dfc5933f8a6d8dcfee8cf77076489f34c7%2Fgraph.jpg?alt=media\&token=d6892cf4-8086-4bce-899e-65baa9b12221)

application inspector 기능을 동작시키기 위해서는 [flink](https://flink.apache.org)와 [zookeeper](https://zookeeper.apache.org/)가 필요하고, 기능의 동작 구조와 구성 및 설정 방법을 아래 설명한다.

### 2. 동작 구조

application inspector 기능의 동작 및 구조를 그림과 함께 보자.

![execute\_flow.jpg](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-67c467a049c249107c3d9f9c23d24c98270ddfd1%2Fexecute_flow.jpg?alt=media\&token=a7960f59-0384-4e26-89ac-64fdcf2aa3ba)

**A.** [flink](https://flink.apache.org)에 streaming job을 실행시킨다.\
**B.** job이 실행되면 taskmanager 서버의 정보가 zookeeper의 데이터 노드로 등록이 된다.\
**C.** Collector는 zookeeper에서 flink 서버의 정보를 가져와서 flink 서버와 tcp 연결을 맺고 agent stat 데이터를 전송한다.\
**D.** flink 서버에서는 agent 데이터를 집계하여 통계 데이터를 hbase에 저장한다.

### 3. 기능 실행 방법

application inspector 기능을 실행하기 위해서 아래와 같이 설정을 변경하고 Pinpoint를 실행해야 한다.

**A.** [테이블 생성 스크립트를 참조](https://github.com/pinpoint-apm/pinpoint/tree/master/hbase/scripts)하여 application 통계 데이터를 저장하는 **ApplicationStatAggre** 테이블을 생성한다.

**B.** flink 프로젝트 설정파일([Pinpoint-flink.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/flink/src/main/resources/profiles/release/pinpoint-flink.properties))에 taskmanager 서버 정보를 저장하는 zookeeper 주소를 설정한다.

```
    flink.cluster.enable=true
    flink.cluster.zookeeper.address=YOUR_ZOOKEEPER_ADDRESS
    flink.cluster.zookeeper.sessiontimeout=3000
    flink.cluster.zookeeper.retry.interval=5000
    flink.cluster.tcp.port=19994
```

**C.** flink 프로젝트 설정파일([Pinpoint-flink.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/flink/src/main/resources/profiles/release/pinpoint-flink.properties))에 job의 실행 방법과 Collector에서 데이터를 받는 listener의 개수를 설정한다.

* flink를 cluster로 구축해서 사용한다면 \_flink.StreamExecutionEnvironment\_에는 **server**를 설정한다.
* flink를 Standalone 형태로 실행한다면 \_flink.StreamExecutionEnvironment\_에는 **local**을 설정한다.

```
    flink.StreamExecutionEnvironment=server
    flink.sourceFunction.Parallel=1
```

**D.** flink 프로젝트 설정파일([hbase.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/flink/src/main/resources/profiles/release/hbase.properties))에 집계 데이터를 저장하는 hbase 주소를 설정한다.

```
    hbase.client.host=YOUR_HBASE_ADDRESS
    hbase.client.port=2181
```

**E.** [flink 프로젝트](https://github.com/pinpoint-apm/pinpoint/tree/master/flink)를 빌드하여 target 폴더 하위에 생성된 streaming job 파일을 flink 서버에 job을 실행한다.

* streaming job 파일 이름은 `pinpoint-flink-job-{pinpoint.version}.jar` 이다.
* 실행방법은 [flink 사이트](https://flink.apache.org)를 참조한다.
* 반드시 실행시 job이 위에서 설정한 설정파일을 참고 할수 있도록 job parameter로 `spring.profiles.active release` or `spring.profiles.active local`를 넣어주야 한다. job 내부에서 spring profile 기능을 사용하여 설정파일을 참고 하고 있기때문에 반드시 입력해야한다.

**F.** Collector에서 flink와 연결을 맺을 수 있도록 설정파일([Pinpoint-Collector.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/collector/src/main/resources/pinpoint-collector.properties))에 zookeeper 주소를 설정한다.

```
    flink.cluster.enable=true
    flink.cluster.zookeeper.address=YOUR_ZOOKEEPER_ADDRESS
    flink.cluster.zookeeper.sessiontimeout=3000
```

**G.** web에서 application inspector 버튼을 활성화 하기 위해서 설정파일(pinpoint-web.properties)을 수정한다.

```
    config.show.applicationStat=true
```

### 4. streaming job 동작 확인 모니터링 batch

Pinpoint streaming job이 실행되고 있는지 확인하는 batch job이 있다. batch job을 동작 시키고 싶다면 Pinpoint web 프로젝트의 설정 파일을 수정하면 된다.

**batch.properties**

```
batch.flink.server=FLINK_MANGER_SERVER_IP_LIST
#`batch.flink.server` 속성 값에 flink job manager 서버 IP를 입력하면 된다. 서버 리스트의 구분자는 ','이다.
# ex) batch.flink.server=123.124.125.126,123.124.125.127
```

**applicationContext-batch-schedule.xml**

```markup
<task:scheduled-tasks scheduler="scheduler">
    ...
    <task:scheduled ref="batchJobLauncher" method="flinkCheckJob" cron="0 0/10 * * * *" />
</task:scheduled-tasks>
```

batch job이 실패할 경우 알람이 전송되도록 기능을 추가 하고싶다면 `com.navercorp.pinpoint.web.batch.JobFailMessageSender class` 구현체를 만들고 bean으로 등록하면 된다.

### 5. 기타

자세한 flink 운영 설치에 대한 내용은 [flink 사이트](https://flink.apache.org)를 참고하자.


# Realtime Request Monitoring

The collection of request information can sometimes be so resource intensive that it can have a serious impact on the target system. Pinpoint provides a number of features that allow this expensive information to be monitored in real time only when the user really needs it.

## Features

The realtime monitor consists of 2 features: recording the number of active requests, thread-dumping the thread handling the active request

### Active request - realtime graph

In the datetime range picker there is a `REAL TIME` button which is focused on automatically augmenting the current data with the just generated realtime data.

![range picker realtime](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-90bd8818e94c54dc52208747339519e4e1432015%2Frange-picker-realtime.png?alt=media\&token=5bbb35fc-f602-4295-9a03-e955c34066e4)

REAL TIME also activates the Active Requests window. This shows the number of active requests at the moment.

![active requests](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-0308fbfceb32dde0e1c800402eb08e986d1e067b%2Factive-requests.png?alt=media\&token=a956e197-474e-4170-a91b-854a7a88bb79)

### Active request thread dump

Pressing the icon in the green square above navigates to the thread dump view

![thread dump list](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-9675d449afda87c24f809cfc53832bcc4c487d1d%2Fthread-dump.png?alt=media\&token=a1898001-df1f-49df-8c03-307421d5c003)

The above list view contains brief information about the threads that were handling requests at the time the page was loaded. When the item is selected, the thread dump is collected and displayed in the UI as shown below.

![thread dump detail](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-6d65c35fa41f337f1bc388fae5c5924518f09c8c%2Fthread-dump-detail.png?alt=media\&token=bed5d2d2-1514-463c-aa29-10ca7be7a7e0)

The thread dump only works if the request is still active, but can be replaced with `There is no message( may be completed)` if the request session is already closed by the time the user selects the item in the list.

## Requirements and installation

These features are **disabled by default** and can be enabled with the property `pinpoint.modules.realtime.enabled=true` at the web, collector module.

### Required properties

Once the feature is enabled, the [Redis](https://redis.io) connection must be provided, which can be configured by adjusting the properties below in \`redis/src/main/resources/redis/profiles'.

Most of the properties below follow, but are not exactly the same as, those defined in the [spring-data-redis](https://spring.io/projects/spring-data-redis) library.

```yaml
spring.data.redis.lettuce.client.io-thread-pool-size=8
spring.data.redis.lettuce.client.computation-thread-pool-size=8
spring.data.redis.lettuce.client.request-queue-size=1024

spring.data.redis.username=default
spring.data.redis.password=

# Standalone mode
spring.data.redis.host=localhost
spring.data.redis.port=6379

# Cluster mode: Cluster mode is prior to standalone
spring.data.redis.cluster.nodes=localhost.1:6379,localhost.2:6379,localhost.3:6379
```

If `spring.data.redis.cluster.nodes` is not empty, `spring.data.redis.host` is ignored.

## Architecture

Real-time information is not collected on a 24-hour basis, but is triggered by some kind of signal from a collector listening to a specific channel for broadcasting the event that a user has accessed that web page (demand). The collected information (supply) is immediately sent to the corresponding channel in Redis and can be read by the web server that sent the demand event.

![redis usage summary](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-0c0b76d5af672d4e0596bbb04cbb8b830fe0a071%2Fredis.drawio.png?alt=media\&token=a1cc5879-bb1b-4ace-864a-dc8fd998038a)

### Case: the number of active requests

Most of the specifications for this section are described in `ATCServiceProtocolConfig.java`.

```java
@Bean
FluxChannelServiceProtocol<ATCDemand, ATCSupply> atcProtocol(ObjectMapper objectMapper) {
    return ChannelServiceProtocol.<ATCDemand, ATCSupply>builder()
      ...
            .setDemandPubChannelURIProvider(demand -> URI.create(RedisPubSubConstants.SCHEME + ":demand:atc-2"))
            .setDemandSubChannelURI(URI.create(RedisPubSubConstants.SCHEME + ":demand:atc-2"))
            .setSupplyChannelURIProvider(demand -> URI.create(RedisPubSubConstants.SCHEME + ":supply:atc-2:" + demand.getApplicationName() + ':' + demand.getAgentId() + ':' + demand.getStartTimestamp()))
            .buildFlux();
}
```

As described in the code above, the demand for the number of active requests is communicated over the redis pubsub channel using the key `demand:atc-2`. If real-time is enabled, all collectors should listen to this channel from the start.

A collector can ignore a demand event if it determines that it cannot respond to that event on its own, but you should design your demands carefully so that there is exactly one collector that can respond to the demand.

The appropriate collector with the appropriate connection triggers the agent to gather the required information, which is then passed in real time to the redis pubsub supply channel with the key 'supply:atc-2:{applicationName}:{agentId}:{startTimestamp}'.

![redis request response](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-a50199f131acc73ab44a33b7811108da2b657c60%2Fredis-req-res.drawio.png?alt=media\&token=3c6ce23c-70fd-4536-8e02-5815921fc4a5)


# Separate Logging Per Request

## ENGLISH GUIDE

### Per-request logging

#### 1. Description

Pinpoint saves additional information(transactionId, spanId) in log messages to classify them by request.

When tomcat processes multiple requests concurrently, we can see log files printed in chronological order. But we can not classify them by each request. For example when an exception message is logged, we can not easily identify all the logs related to the request that threw the exception.

Pinpoint is able to classify logs by requests by storing additional information(transactionId, spanId) in MDC of each request. The transactionId printed in the log message is the same as the transactionId in Pinpoint Web’s Transaction List view.

Let’s take a look at a more specific example. The log below is from an exception that occurred without using Pinpoint. As you can see, it is hard to identify the logs related to the request that threw the exception. ex) Without Pinpoint

```
2015-04-04 14:35:20 [INFO](ContentInfoCollector:76 ) get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:123 ) get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoCollector:12) get content name : SPORTS
2015-04-04 14:35:20 [INFO](ContentInfoCollector:25 ) get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:56 ) get content name : NATIONAL
2015-04-04 14:35:20 [INFO](ContentInfoCollector:34 ) get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoService:55 ) check authorization of user
2015-04-04 14:35:20 [INFO](ContentInfoService:14 ) get title of content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14 ) execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114 ) execute query ...    
2015-04-04 14:35:20 [INFO](ContentInfoService:74 ) get top linking for content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14 ) execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114 ) execute query ...
2015-04-04 14:35:22 [INFO](ContentDAOImpl:186 ) execute query ...
2015-04-04 14:35:22 [ERROR]ContentDAOImpl:158 )
     com.mysql.jdbc.exceptions.jdbc4.CommunicationsException: Communications link failure
          at example.ContentDAO.executequery(ContentDAOImpl.java:152)
          ...
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at com.mysql.jdbc.ConnectionImpl.<init>(ConnectionImpl.java:787)
          ...
     Caused by: com.mysql.jdbc.exceptions.jdbc4.CommunicationsException:
     Communications link failure The last packet sent successfully to the server was 0 milliseconds ago.
     The driver has not received any packets from the server.    
          at com.mysql.jdbc.ConnectionImpl.createNewIO(ConnectionImpl.java:2181)
          ... 12 more
     Caused by: java.net.ConnectException: Connection refused
          at java.net.PlainSocketImpl.socketConnect(Native Method)
          at java.net.PlainSocketImpl.doConnect(PlainSocketImpl.java:333)
          at java.net.PlainSocketImpl.connectToAddress(PlainSocketImpl.java:195)   
          at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:182)   
          at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:432)   
          at java.net.Socket.connect(Socket.java:529)    
          ...13 more
2015-04-04 14:35:22 [INFO](ContentDAO:145 ) execute query ...
2015-04-04 14:35:20 [INFO](ContentInfoService:38 ) update hits for content
2015-04-04 14:35:20 [INFO](ContentInfoService:89 ) check of user
2015-04-04 14:35:24 [INFO](ContentDAO:146 ) execute query ...
2015-04-04 14:35:25 [INFO](ContentDAO:123 ) execute query ...
```

Pinpoint classifies logs by requests by storing additional information(transactionId, spanId) in MDC of each request. ex) With Pinpoint

```
2015-04-04 14:35:20 [INFO](ContentInfoCollector:76) [txId : agent^14252^17 spanId : 1224] get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:123) [txId : agent^142533^18 spanId : 1231] get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoCollector:12) [txId : agent^142533^19 spanId : 1246] get content name : SPORTS
2015-04-04 14:35:20 [INFO](ContentInfoCollector:25) [txId : agent^142533^20 spanId : 1263] get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:56) [txId : agent^142533^21 spanId : 1265] get content name : NATIONAL
2015-04-04 14:35:20 [INFO](ContentInfoCollector:34) [txId : agent^142533^22 spanId : 1278] get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoService:55) [txId : agent^14252^18 spanId : 1231] check authorization of user
2015-04-04 14:35:20 [INFO](ContentInfoService:14) [txId : agent^14252^17 spanId : 1224] get title of content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14) [txId : agent^14252^17 spanId : 1224] execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114) [txId : agent^142533^19 spanId : 1246] execute query ...    
2015-04-04 14:35:20 [INFO](ContentInfoService:74) [txId : agent^14252^17 spanId : 1224] get top linking for content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14) [txId : agent^142533^18 spanId : 1231] execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114) [txId : agent^142533^21 spanId : 1265] execute query ...
2015-04-04 14:35:22 [INFO](ContentDAOImpl:186) [txId : agent^142533^22 spanId : 1278] execute query ...
2015-04-04 14:35:22 [ERROR](ContentDAOImpl:158) [txId : agent^142533^18 spanId : 1231]
     com.mysql.jdbc.exceptions.jdbc4.CommunicationsException: Communications link failure
          at com.pinpoint.example.dao.ContentDAO.executequery(ContentDAOImpl.java:152)
          ...
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at com.mysql.jdbc.ConnectionImpl.<init>(ConnectionImpl.java:787)   
          ...
     Caused by: com.mysql.jdbc.exceptions.jdbc4.CommunicationsException:
     Communications link failure The last packet sent successfully to the server was 0 milliseconds ago.
     The driver has not received any packets from the server.
          ...
          at com.mysql.jdbc.ConnectionImpl.createNewIO(ConnectionImpl.java:2181)
          ... 12 more
     Caused by: java.net.ConnectException: Connection refused
          at java.net.PlainSocketImpl.socketConnect(Native Method)   
          at java.net.PlainSocketImpl.doConnect(PlainSocketImpl.java:333)
          at java.net.PlainSocketImpl.connectToAddress(PlainSocketImpl.java:195)
          at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:182)
          at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:432)
          at java.net.Socket.connect(Socket.java:529)
          ... 13 more
2015-04-04 14:35:22 [INFO](ContentDAO:145) [txId : agent^14252^17 spanId : 1224] execute query ...
2015-04-04 14:35:20 [INFO](ContentInfoService:38) [txId : agent^142533^19 spanId : 1246] update hits for content
2015-04-04 14:35:20 [INFO](ContentInfoService:89) [txId : agent^142533^21 spanId : 1265] check of user
2015-04-04 14:35:24 [INFO](ContentDAO:146) [txId : agent^142533^22 spanId : 1278] execute query ...
2015-04-04 14:35:25 [INFO](ContentDAO:123) [txId : agent^14252^17 spanId : 1224] execute query ...
```

The transactionId printed in the log message is the same as the transactionId in Pinpoint Web’s Transaction List view. ![per-request\_feature\_1.jpg](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-740fd5dfd8b1f9c2023c4c78cf1d69226b51c214%2Fper-request_feature_1.jpg?alt=media\&token=74a17e0a-5551-4573-8620-622444795342)

#### 2. How to configure

**2-1 Pinpoint agent configuration**

To enable this feature, set the logging property corresponding to the logging library in use to true in *pinpoint.config*. For example,

ex) pinpoint.config when using log4j

```
###########################################################
# log4j
###########################################################
profiler.log4j.logging.transactioninfo=true
```

ex) pinpoint.config when using log4j2

```
###########################################################
# log4j2 
###########################################################
profiler.log4j2.logging.transactioninfo=true
```

ex) pinpoint.config when using logback

```
###########################################################
# logback
###########################################################
profiler.logback.logging.transactioninfo=true
```

**2-2 log4j, log4j2, logback configuration**

Change the log message format to print the transactionId, and spanId saved in MDC.

ex) log4j : log4j.xml

```markup
Before
<appender name = "console" class= "org.apache.log4j.ConsoleAppender" >
     <layout class = "org.apache.log4j.EnhancedPatternLayout">
          <param name = "ConversionPattern" value= "%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) %m%n" />
     </layout >
</appender >

After
<appender name = "console" class= "org.apache.log4j.ConsoleAppender" >
     <layout class = "org.apache.log4j.EnhancedPatternLayout">
          <param name = "ConversionPattern" value= "%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) [TxId : %X{PtxId} , SpanId : %X{PspanId}] %m%n" />
        </layout >
</appender >
```

ex) log4j2 - log4j2.xml

```markup
Before
<appender>
     <console name="STDOUT" target="SYSTEM_OUT">
          <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) %m%n""/>
     </console>
<appender>

After
<appender>
     <console name="STDOUT" target="SYSTEM_OUT">
          <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) [TxId : %X{PtxId} , SpanId : %X{PspanId}] %m%n""/>
     </console>
<appender>
```

ex) logback : logback.xml

```markup
Before
<appender name = "STDOUT" class= "ch.qos.logback.core.ConsoleAppender" >
     <layout class = "ch.qos.logback.classic.PatternLayout">
          <Pattern >%d{HH:mm} %-5level %logger{36} - %msg%n</Pattern >
     </layout >
</appender >

After
<appender name = "STDOUT" class= "ch.qos.logback.core.ConsoleAppender" >
     <layout class = "ch.qos.logback.classic.PatternLayout">
          <Pattern >%d{HH:mm} %-5level %logger{36} - [TxId : %X{PtxId} , SpanId : %X{PspanId}] %msg%n</Pattern >
     </layout >
</appender >
```

**2-3 Checking log message**

If the per-request logging is correctly configured, the transactionId, and spanId are printed in the log file.

```
2015-04-04 14:35:20 [INFO](ContentInfoCollector:76 ) [txId : agent^14252^17 spanId : 1224] get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:123 ) [txId : agent^142533^18 spanId : 1231] get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoCollector:12) [txId : agent^142533^19 spanId : 1246] get content name : SPORTS
```

#### 3. expose log in Pinpoint web

If you want to add links to the logs in the transaction list view, you should configure and implement the logic as below. Pinpoint Web only adds link buttons - you should implement the logic to retrieve the log message.

If you want to expose your agent’s log messages, please follow the steps below.

**step 1** You should implement a controller that receives transactionId, spanId, transaction\_start\_time as parameters and retrieve the logs yourself. We do not yet provide a way to retrieve the logs.

example)

```java
@RestController
public class Nelo2LogController {

    @RequestMapping(value = "/????")
    public String NeloLogForTransactionId(@RequestParam (value= "transactionId", required=true) String transactionId,
                                            @RequestParam(value= "spanId" , required=false) String spanId,
                                            @RequestParam(value="time" , required=true) long time ) {

          // you should implement the logic to retrieve your agent’s logs.
    }
```

**step 2** In *pinpoint-web.properties* file, set `log.enable` to true, and `log.page.url` to the url of the controller above. The value set in `log.button.name` will show up as the button text in the Web UI.

```
log.enable= true
log.page.url=XXXX.pinpoint
log.button.name= log
```

**step 3** Pinpoint 1.5.0 or later, we improve button to decided enable/disable depending on whether or not being logged. You should implement interceptor for using logging appender to add logic whether or not being logged. you also should create plugin for logging appender internally. Please refer to Pinpoint Profiler Plugin Sample([Link](https://github.com/pinpoint-apm/pinpoint-plugin-sample)). Location added logic of interceptor is method to log for data of LoggingEvent in appender class. you should review your appender class and find method. This is interceptor example.

```
public class AppenderInterceptor implements AroundInterceptor0 {

    private final TraceContext traceContext;

    public AppenderInterceptor(TraceContext traceContext) {
        this.traceContext = traceContext;
    }

    @Override
    public void before(Object target) {
        Trace trace = traceContext.currentTraceObject();

        if (trace != null) {
            SpanRecorder recorder = trace.getSpanRecorder();
            recorder.recordLogging(LoggingInfo.LOGGED);
        }
    }

    @IgnoreMethod
    @Override
    public void after(Object target, Object result, Throwable throwable) {

    }
}
```

If those are correctly configured, the buttons are added in the transaction list view. ![per-request\_feature\_2.jpg](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-3ce49da1cdfd63c7208ec92142b21950c2bff409%2Fper-request_feature_2.jpg?alt=media\&token=0d69041b-a91d-4ba3-9b6e-91b325b5ae4d)

For details in how the log buttons are generated, please refer to Pinpoint Web’s BusinessTransactionController and ScatterChartController.

## 한국어 가이드

### Per-request logging

#### 1. 기능 설명

Pinpoint에서는 log message를 request 단위로 구분할 수 있도록 log message 에 추가정보를 저장해준다.

다수의 요청을 처리하는 tomcat을 사용할 경우 로그 파일을 보면 시간순으로 출력된 로그를 확인할 수 있다. 그러나 동시에 요청된 다수의 request 각각에 대한 로그를 구분 해서 볼 수 없다. 예를 들어 로그에서 exception message가 출력됐을 때 그 exception이 발생한 request의 모든 log를 확인하기 힘들다.

Pinpoint는 log message 마다 request와 연관된 정보(transactionId, spanId)를 MDC에 넣어줘서 request 단위로 log message를 구분할 수 있도록 해준다. 로그에 출력된 transactionId는 pinpoint web의 transaction List 화면에 출력된 transactionId와 일치한다.

구체적으로 예를 들어보자. Pinpoint를 사용하지 않았을 때 exception이 발생했을 경우 로그 메시지를 살펴 보자. 요청된 다수의 request 각각을 구분하여 로그를 확인할 수가 없다.

ex) Without Pinpoint

```
2015-04-04 14:35:20 [INFO](ContentInfoCollector:76 ) get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:123 ) get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoCollector:12) get content name : SPORTS
2015-04-04 14:35:20 [INFO](ContentInfoCollector:25 ) get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:56 ) get content name : NATIONAL
2015-04-04 14:35:20 [INFO](ContentInfoCollector:34 ) get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoService:55 ) check authorization of user
2015-04-04 14:35:20 [INFO](ContentInfoService:14 ) get title of content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14 ) execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114 ) execute query ...
2015-04-04 14:35:20 [INFO](ContentInfoService:74 ) get top linking for content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14 ) execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114 ) execute query ...
2015-04-04 14:35:22 [INFO](ContentDAOImpl:186 ) execute query ...
2015-04-04 14:35:22 [ERROR]ContentDAOImpl:158 )
     com.mysql.jdbc.exceptions.jdbc4.CommunicationsException: Communications link failure
          at example.ContentDAO.executequery(ContentDAOImpl.java:152)
          ...
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at com.mysql.jdbc.ConnectionImpl.<init>(ConnectionImpl.java:787)
          ...
     Caused by: com.mysql.jdbc.exceptions.jdbc4.CommunicationsException:
     Communications link failure The last packet sent successfully to the server was 0 milliseconds ago.
     The driver has not received any packets from the server.
          at com.mysql.jdbc.ConnectionImpl.createNewIO(ConnectionImpl.java:2181)
          ... 12 more
     Caused by: java.net.ConnectException: Connection refused
          at java.net.PlainSocketImpl.socketConnect(Native Method)
          at java.net.PlainSocketImpl.doConnect(PlainSocketImpl.java:333)
          at java.net.PlainSocketImpl.connectToAddress(PlainSocketImpl.java:195)
          at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:182)
          at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:432)
          at java.net.Socket.connect(Socket.java:529)
          ...13 more
2015-04-04 14:35:22 [INFO](ContentDAO:145 ) execute query ...
2015-04-04 14:35:20 [INFO](ContentInfoService:38 ) update hits for content
2015-04-04 14:35:20 [INFO](ContentInfoService:89 ) check of user
2015-04-04 14:35:24 [INFO](ContentDAO:146 ) execute query ...
2015-04-04 14:35:25 [INFO](ContentDAO:123 ) execute query ...
```

Pinpoint는 로그 메세지 마다 request와 연관된 정보(transactionId, spanId)를 MDC에 넣어줘서 request 단위로 log message를 구분시켜 준다.

ex) With Pinpoint

```
2015-04-04 14:35:20 [INFO](ContentInfoCollector:76) [txId : agent^14252^17 spanId : 1224] get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:123) [txId : agent^142533^18 spanId : 1231] get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoCollector:12) [txId : agent^142533^19 spanId : 1246] get content name : SPORTS
2015-04-04 14:35:20 [INFO](ContentInfoCollector:25) [txId : agent^142533^20 spanId : 1263] get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:56) [txId : agent^142533^21 spanId : 1265] get content name : NATIONAL
2015-04-04 14:35:20 [INFO](ContentInfoCollector:34) [txId : agent^142533^22 spanId : 1278] get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoService:55) [txId : agent^14252^18 spanId : 1231] check authorization of user
2015-04-04 14:35:20 [INFO](ContentInfoService:14) [txId : agent^14252^17 spanId : 1224] get title of content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14) [txId : agent^14252^17 spanId : 1224] execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114) [txId : agent^142533^19 spanId : 1246] execute query ...
2015-04-04 14:35:20 [INFO](ContentInfoService:74) [txId : agent^14252^17 spanId : 1224] get top linking for content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14) [txId : agent^142533^18 spanId : 1231] execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114) [txId : agent^142533^21 spanId : 1265] execute query ...
2015-04-04 14:35:22 [INFO](ContentDAOImpl:186) [txId : agent^142533^22 spanId : 1278] execute query ...
2015-04-04 14:35:22 [ERROR](ContentDAOImpl:158) [txId : agent^142533^18 spanId : 1231]
     com.mysql.jdbc.exceptions.jdbc4.CommunicationsException: Communications link failure
          at com.pinpoint.example.dao.ContentDAO.executequery(ContentDAOImpl.java:152)
          ...
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at com.mysql.jdbc.ConnectionImpl.<init>(ConnectionImpl.java:787)
          ...
     Caused by: com.mysql.jdbc.exceptions.jdbc4.CommunicationsException:
     Communications link failure The last packet sent successfully to the server was 0 milliseconds ago.
     The driver has not received any packets from the server.
          ...
          at com.mysql.jdbc.ConnectionImpl.createNewIO(ConnectionImpl.java:2181)
          ... 12 more
     Caused by: java.net.ConnectException: Connection refused
          at java.net.PlainSocketImpl.socketConnect(Native Method)
          at java.net.PlainSocketImpl.doConnect(PlainSocketImpl.java:333)
          at java.net.PlainSocketImpl.connectToAddress(PlainSocketImpl.java:195)
          at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:182)
          at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:432)
          at java.net.Socket.connect(Socket.java:529)
          ... 13 more
2015-04-04 14:35:22 [INFO](ContentDAO:145) [txId : agent^14252^17 spanId : 1224] execute query ...
2015-04-04 14:35:20 [INFO](ContentInfoService:38) [txId : agent^142533^19 spanId : 1246] update hits for content
2015-04-04 14:35:20 [INFO](ContentInfoService:89) [txId : agent^142533^21 spanId : 1265] check of user
2015-04-04 14:35:24 [INFO](ContentDAO:146) [txId : agent^142533^22 spanId : 1278] execute query ...
2015-04-04 14:35:25 [INFO](ContentDAO:123) [txId : agent^14252^17 spanId : 1224] execute query ...
```

로그메시지에 출력된 transactionId는 Pinpoint web의 transactionlist의 transactionId와 일치한다. ![per-request\_feature\_1.jpg](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-740fd5dfd8b1f9c2023c4c78cf1d69226b51c214%2Fper-request_feature_1.jpg?alt=media\&token=74a17e0a-5551-4573-8620-622444795342)

#### 2. 설정 방법

**2-1 Pinpoint agent 설정**

Pinpoint를 사용하려면 Pinpoint agent 설정파일(Pinpoint.config)의 logging 설정 값을 true로 변경해야 한다. 사용하는 logging 라이브러리에 해당하는 설정값만 true로 변경하면 된다. 아래 설정에 대한 예시가 있다.

ex) Pinpoint.config - log4j 를 사용할 경우

```
###########################################################
# log4j
###########################################################
profiler.log4j.logging.transactioninfo=true
```

ex) Pinpoint.config - log4j2 를 사용할 경우

```
###########################################################
# log4j2 
###########################################################
profiler.log4j2.logging.transactioninfo=true
```

ex) Pinpoint.config - logback 를 사용할 경우

```
###########################################################
# logback
###########################################################
profiler.logback.logging.transactioninfo=true
```

**2-2 log4j, log4j2, logback 설정 파일 설정**

logging 설정 파일의 log message pattern 설정에 Pinpoint에서 MDC에 저장한 transactionId, spanId값이 출력될수 있도록 설정을 추가하자.

ex) log4j - log4j.xml

```markup
변경 전
<appender name = "console" class= "org.apache.log4j.ConsoleAppender" >
     <layout class = "org.apache.log4j.EnhancedPatternLayout">
          <param name = "ConversionPattern" value= "%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) %m%n" />
     </layout >
</appender >

변경 후
<appender name = "console" class= "org.apache.log4j.ConsoleAppender" >
     <layout class = "org.apache.log4j.EnhancedPatternLayout">
          <param name = "ConversionPattern" value= "%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) [TxId : %X{PtxId} , SpanId : %X{PspanId}] %m%n" />
        </layout >
</appender >
```

ex) log4j2 - log4j2.xml

```markup
변경 전
<appender>
     <console name="STDOUT" target="SYSTEM_OUT">
          <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) %m%n""/>
     </console>
<appender>

변경 후
<appender>
     <console name="STDOUT" target="SYSTEM_OUT">
          <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) [TxId : %X{PtxId} , SpanId : %X{PspanId}] %m%n""/>
     </console>
<appender>
```

ex) logback - logback.xml

```markup
변경 전
<appender name = "STDOUT" class= "ch.qos.logback.core.ConsoleAppender" >
     <layout class = "ch.qos.logback.classic.PatternLayout">
          <Pattern >%d{HH:mm} %-5level %logger{36} - %msg%n</Pattern >
     </layout >
</appender >

변경 후
<appender name = "STDOUT" class= "ch.qos.logback.core.ConsoleAppender" >
     <layout class = "ch.qos.logback.classic.PatternLayout">
          <Pattern >%d{HH:mm} %-5level %logger{36} - [TxId : %X{PtxId} , SpanId : %X{PspanId}] %msg%n</Pattern >
     </layout >
</appender >
```

**2-3 로그 출력 확인**

Pinpoint agent가 적용된 서비스를 동작하여 log message에 아래와 같이 transactionId, spanId 정보가 출력되는것을 확인하면 된다.

```
2015-04-04 14:35:20 [INFO](ContentInfoCollector:76 ) [txId : agent^14252^17 spanId : 1224] get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:123 ) [txId : agent^142533^18 spanId : 1231] get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoCollector:12) [txId : agent^142533^19 spanId : 1246] get content name : SPORTS
```

#### 3. Pinpoint web에서 로그 확인

Pinpoint web의 transaction list 화면에서 log를 출력하는 링크를 제공하고 싶다면 아래와 같이 설정 및 구현을 추가하면 된다. Pinpoint web에서는 버튼 을 추가해주기만 하고 로그를 가져오는 로직은 직접 구현을 해야한다.

로그 메시지를 Pinpoint web에서 보여주기 위해서는 아래와 같이 2가지 step을 따라야 한다.

**step 1** transactionId와 spanId, transaction 시작 시간을 파라미터로 받아서 로그 메시지를 가져오는 controller을 구현해야한다.

example)

```java
@RestController
public class Nelo2LogController {

    @RequestMapping(value = "/XXXX")
    public String NeloLogForTransactionId(@RequestParam (value= "transactionId", required=true) String transactionId,
                                            @RequestParam(value= "spanId" , required=false) String spanId,
                                            @RequestParam(value="time" , required=true) long time ) {

          // you should implement the logic to retrieve your agent’s logs.
    }
```

**step 2** Pinpoint-web.properties 파일에서 버튼을 추가해주는 기능을 활성화 하기 위해서 log.enable의 값을 true로 설정하고 위에서 구현한 controller의 url과 button의 이름을 추가해주자.

```
log.enable=true
log.page.url=XXXX.Pinpoint
log.button.name=log
```

**step 3** pinpoint 1.5 이후 버전부터 log 기록 여부에 따라 log 버튼의 활성화가 결정되도록 개선 됐기 때문에 당신이 사용하는 logging appender의 로깅 메소드에 logging 여부를 저장하는 interceptor를 추가하는 플러그인을 개발해야 한다. 플러그인 개발 방법은 다음 링크를 참고하면 된다([Link](https://github.com/pinpoint-apm/pinpoint-plugin-sample)). interceptor 로직이 추가돼야 하는 위치는 appender class 내에 LoggingEvent 객체의 데이터를 이용하여 로깅을 하는 메소드다. 아래는 interceptor 예제이다.

```
public class AppenderInterceptor implements AroundInterceptor0 {

    private final TraceContext traceContext;

    public AppenderInterceptor(TraceContext traceContext) {
        this.traceContext = traceContext;
    }

    @Override
    public void before(Object target) {
        Trace trace = traceContext.currentTraceObject();

        if (trace != null) {
            SpanRecorder recorder = trace.getSpanRecorder();
            recorder.recordLogging(LoggingInfo.LOGGED);
        }
    }

    @IgnoreMethod
    @Override
    public void after(Object target, Object result, Throwable throwable) {

    }
}
```

위와 같이 설정 및 구현을 추가하고 pinpoint web을 동작시키면 아래와 같이 버튼이 추가 된다. ![per-request\_feature\_2.jpg](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-3ce49da1cdfd63c7208ec92142b21950c2bff409%2Fper-request_feature_2.jpg?alt=media\&token=0d69041b-a91d-4ba3-9b6e-91b325b5ae4d) 로그 버튼을 생성해주는 과정을 보시려면, Pinpoint Web의 BusinessTransactionController 와 ScatterChartController class를 참고하세요.


# Marking Transaction as Fail

## HTTP Status Code with Request Failure. <a href="#http-status-code-with-request-failure" id="http-status-code-with-request-failure"></a>

![overview](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-cf1140a4afb3c0a73333b81a2a20c55ebe2fbaae%2Fhttp-status-code-failure-overview.png?alt=media\&token=e9992a8d-2429-4720-8463-f55386afde3c)

## Pinpoint Configuration

pinpoint.config

```
profiler.http.status.code.errors=5xx, 401, 403, 406
```

Comma separated list of HTTP status codes.

* 1xx: Informational(100 \~ 199).
  * 100: Continue
  * 101: Switching Protocols
* 2xx: Successful(200 \~ 299).
  * 200: OK
  * 201: Created
  * 202: Accepted
  * 203: Non-Authoritative Information
  * 204: No Content
  * 205: Reset Content
  * 206: Partial Content
* 3xx: Redirection(300 \~ 399).
  * 300: Multiple Choices
  * 301: Moved Permanently
  * 302: Found
  * 303: See Other
  * 304: Not Modified
  * 305: Use Proxy
  * 307: Temporary Redirect
* 4xx: Client Error(400 \~ 499).
  * 400: Bad Request
  * 401: Unauthorized
  * 402: Payment Required
  * 403: Forbidden
  * 404: Not Found
  * 405: Method Not Allowed
  * 406: Not Acceptable
  * 407: Proxy Authentication Required
  * 408: Request Time-out
  * 409: Conflict
  * 410: Gone
  * 411: Length Required
  * 412: Precondition Failed
  * 413: Request Entity Too Large
  * 414: Request-URI Too Large
  * 415: Unsupported Media Type
  * 416: Requested range not satisfiable
  * 417: Expectation Failed
* 5xx: Server Error(500 \~ 599).
  * 500: Internal Server Error
  * 501: Not Implemented
  * 502: Bad Gateway
  * 503: Service Unavailable
  * 504: Gateway Time-out
  * 505: HTTP Version not supported

Resources

* <https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html>


# Monitoring Proxy Server

## Proxy monitoring using HTTP headers <a href="#proxy-monitoring-using-http-headers" id="proxy-monitoring-using-http-headers"></a>

It is used to know the elapsed time between proxy and WAS.

![overview](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-257fbee4518c6805487a8e000f6da518440eb974%2Fproxy-http-header-overview.png?alt=media\&token=ed6c55aa-00dd-444c-b98e-6dc57e679303)

## Pinpoint Configuration

pinpoint.config

```
profiler.proxy.http.header.enable=true
```

## Proxy Configuration

### Apache HTTP Server

* <http://httpd.apache.org/docs/2.4/en/mod/mod_headers.html>

Add HTTP header.

```
Pinpoint-ProxyApache: t=991424704447256 D=3775428 i=51 b=49
```

e.g.

httpd.conf

```
<IfModule mod_jk.c>
...
RequestHeader set Pinpoint-ProxyApache "%t %D %i %b"
...
</IfModule>
```

**%t is required value.**

### Nginx

* <http://nginx.org/en/docs/http/ngx_http_core_module.html>
* <http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_set_header>

Add HTTP header.

```
Pinpoint-ProxyNginx: t=1504248328.423 D=0.123
```

e.g.

nginx.conf

```
...
  server {
        listen       9080;
        server_name  localhost;

        location / {
            ...
            set $pinpoint_proxy_header "t=$msec D=$request_time";
            proxy_set_header Pinpoint-ProxyNginx $pinpoint_proxy_header;
        }
  }
...
```

or

```
http {
...

    proxy_set_header Pinpoint-ProxyNginx t=$msec;

...
}
```

**t=$msec is required value.**

### App

Milliseconds since epoch (13 digits) and app information.

Add HTTP header.

```
Pinpoint-ProxyApp: t=1594316309407 app=foo-bar
```

**t=epoch is required value.**


# Upgrade Database Hbase2

### Do you like to use Hbase 2.x for Pinpoint? <a href="#do-you-like-to-use-hbase-2x-for-pinpoint" id="do-you-like-to-use-hbase-2x-for-pinpoint"></a>

Default settings of current releases are for Hbase 1.x.

If you'd like to use Hbase 2.x for Pinpoint database.

check out [Hbase2-module](https://github.com/pinpoint-apm/pinpoint/tree/master/hbase2-module).


# Contribution

Thank you very much for choosing to share your contribution with us. Please read this page to help yourself to the contribution.

Before making first pull-request, please make sure you've signed the [Contributor License Agreement](http://goo.gl/forms/A6Bp2LRoG3). This isn't a copyright - it gives us (Naver) permission to use and redistribute your code as part of the project.

## Making Pull Requests

Apart from trivial fixes such as typo or formatting, all pull requests should have a corresponding issue associated with them. It is always helpful to know what people are working on, and different (often better) ideas may pop up while discussing them. Please keep these in mind before you create a pull request:

* Every new java file must have a copy of the license comment. You may copy this from an existing file.
* Make sure you've tested your code thoroughly. For plugins, please try your best to include integration tests if possible.
* Before submitting your code, make sure any changes introduced by your code does not break the build, or any tests.
* Clean up your commit log into logical chunks of work to make it easier for us to figure out what and why you've changed something. (`git rebase -i` helps)
* Please try best to keep your code updated against the master branch before creating a pull request.
* Make sure you create the pull request against our master branch.
* If you've created your own plugin, please take a look at [plugin contribution guideline](#plugin-contribution-guideline)

## Plugin Contribution Guideline

We welcome your plugin contribution. Currently, we would love to see additional tracing support for libraries such as [Storm](https://storm.apache.org), [HBase](http://hbase.apache.org), as well as profiler support for additional languages (.NET, C++).

### Technical Guide

**For technical guides for developing plug-in,** take a look at our [plugin development guide](https://pinpoint-apm.gitbook.io/pinpoint/documents/plugin-dev-guide), along with [plugin samples](https://github.com/pinpoint-apm/pinpoint-plugin-sample) project to get an idea of how we do instrumentation. The samples will provide you with example codes to help you get started.

### Contributing Plugin

If you want to contribute your plugin, it has to satisfy the following requirements:

1. Configuration key names must start with `profiler.[pluginName]`.
2. At least 1 plugin integration test.

Once your plugin is complete, please open an issue to contribute the plugin as below:

```
Title: [Target Library Name] Plugin Contribution

Link: Plugin Repository URL
Target: Target Library Name
Supported Version: 
Description: Simple description about the target library and/or target library homepage URL

ServiceTypes: List of service type names and codes the plugin adds
Annotations: List of annotation key names and codes the plugin adds
Configurations: List of configuration keys and description the plugin adds.
```

Our team will review the plugin, and your plugin repository will be linked at the third-party plugin list page if everything checks out. If the plugin is for a widely used library, and if we feel confident that we can continuously provide support for it, you may be asked to send us a PR. Should you choose to accept it, your plugin will be merged to the Pinpoint repository.

As much as we'd love to merge all the plugins to the source repository, we do not have the man power to manage all of them, yet. We are a very small team, and we certainly are not experts in all of the target libraries. We feel that it would be better to not merge a plugin if we are not confident in our ability to provide continuous support for it.

To send a PR, you have to modify your plugin like this:

* Fork Pinpoint repository
* Copy your plugin under /plugins directory
* Set parent pom

  ```
    <parent>
        <groupId>com.navercorp.pinpoint</groupId>
        <artifactId>pinpoint-plugins</artifactId>
        <version>Current Version</version>
    </parent>
  ```
* Add your plugin to *plugins/pom.xml* as a sub-module.
* Add your plugin to *plugins/assembly/pom.xml* as a dependency.
* Copy your plugin integration tests under /agent-it/src/test directory.
* Add your configurations to /agent/src/main/resources/\*.config files.
* Insert following license header to all java source files.

  ```
  /*
  * Copyright 2018 Pinpoint contributors and NAVER Corp.
  *
  * Licensed under the Apache License, Version 2.0 (the "License");
  * you may not use this file except in compliance with the License.
  * You may obtain a copy of the License at
  *
  *     http://www.apache.org/licenses/LICENSE-2.0
  *
  * Unless required by applicable law or agreed to in writing, software
  * distributed under the License is distributed on an "AS IS" BASIS,
  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  * See the License for the specific language governing permissions and
  * limitations under the License.
  */
  ```

If you do not want to be bothered with a PR, you may choose to tell us to do it ourselves. However, please note that your contribution will not visible through git history or the Github profile.


# Performance Analysis

## Introduction

Team members of Pinpoint are always aware of performance and stability issues. We've adapted technologies to reduced elements that hinder performance and always carefully examine the codes when there is a plugin pull requests.(plugin codes affects most in performance)

While we have been testing internally everyday for last few years, We've finally had the chance to make the data presentable.

This article doesn't include results compared with other APMs. It's pointless to compare with others due to the difference in collected data. Pinpoint collects massive data to enhance observability as much as possible. But still with minimum impact on the performance

## Test Environment

JVM : 1.8.0\_77 (G1, -Xms4g, -Xmx4g)\
Server : Tomcat\
Database : Cubrid\
Stress test generator : [NGrinder](https://github.com/pinpoint-apm/ngrinder)

## Test Result

![Test Result](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-6b556e592a22322d6fc454605726a1bc5d1b6690%2F20191022_Performance.png?alt=media)

*off : non traced*\
on-20 : trace 5% transaction using thrift\
\&#xNAN;*grpc-on-20 : trace 5% transaction using grpc*\
on-1 : trace 100% transaction using thrift\
\*grpc-on-1 : trace 100% transaction using grpc

**Test result shows that Pinpoint affects less than 3% in performance and memory**\
**TPS is effected by various reasons, which may not always be exact**\
**gRPC is little slow than thrift in this test, the performance gap between the two is expected to be reduced, or even more, reversed in v1.9.0 release**

## Conclusion

Pinpoint is already being used in dozens of global companies in the world. With right environment and configuration it's been proved to be worthy. We believe most of the services can spare their 3% of resource to gain high observability with Pinpoint.

## Check List

If you still have low performance issue due to Pinpoint. Here are several items to check in advance.

1. Check the default log option for Pinpoint-Agent (Default was `DEBUG` prior to v1.8.1)
2. JVM option
   * use G1 for the GC Type
   * fix initial/maximum memory allocation pool with same size. ex) -Xms4g -Xmx4g
3. Change [sampling rate](https://pinpoint-apm.gitbook.io/pinpoint/faq#why-is-only-the-first-some-of-the-requests-traced). Even 1\~2% would be enough if you are dealing big data.

   When certain transaction doesn't bypass database, it may appear that Pinpoint is consuming much more resources than 3%, since instrumentation time is not relative, but absolute. But this phenomenon appears in all APM, not only Pinpoint.

## Reference Data

We run test with various technology stacks. Planning to expand more as we go.\
[Full Result](https://pinpoint-apm.gitbook.io/pinpoint/performance)


# FAQ

[Github issues](https://github.com/pinpoint-apm/pinpoint/issues)\
[Google group](https://groups.google.com/forum/#!forum/pinpoint_user)\
[Gitter](https://gitter.im/naver/pinpoint)

Chinese groups

|                                                                                                       QQ Group: 897594820                                                                                                       |                                                                                                                             DING Group                                                                                                                            |
| :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![QQ Group](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-f9cbff4e99069d1c453f335f53bd198c0db8b640%2FNAVERPinpoint.png?alt=media) | ![DING Group](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-79e1332a4388413fdf35be2f47822102a0f1b11d%2FNaverPinpoint%E4%BA%A4%E6%B5%81%E7%BE%A4-DING.jpg?alt=media) |

## How do I get the call stack view?

Click on a server node, which will populate the scatter chart on the right. This chart shows all succeeded/failed requests that went through the server. If there are any requests that spike your interest, simply **drag on the scatter chart** to select them. This will bring up the call stack view containing the requests you've selected.

## How do I change agent's log level?

You can change the log level by modifying the agent's *log4j.xml* located in *PINPOINT\_AGENT/lib* directory.

## Why is only the first/some of the requests traced?

There is a sampling rate option in the agent's pinpoint.config file (profiler.sampling.rate). Pinpoint agent samples 1 trace every N transactions if this value was set as N. Changing this value to 1 will allow you to trace every transaction.

## Request count in the Scatter Chart is different from the ones in Response Summary chart. Why is this?

The Scatter Chart data have a second granularity, so the requests counted here can be differentiated by a second interval. On the other hand, the Server Map, Response Summary, and Load Chart data are stored in a minute granularity (the collector aggregates these in memory and flushes them every minute due to performance reasons). For example, if the data is queried from 10:00:30 to 10:05:30, the Scatter Chart will show the requests counted between 10:00:30 and 10:05:30, whereas the server map, response summary, and load chart will show the requests counted between 10:00:00 and 10:05:59.

## How do I delete application name and/or agent id from HBase?

Application names and agent ids, once registered, stay in HBase until their TTL expires (default 1year). You may however delete them proactively using [admin APIs](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/java/com/navercorp/pinpoint/web/controller/AdminController.java) once they are no longer used.

* Remove application name - `/admin/removeApplicationName.pinpoint?applicationName=$APPLICATION_NAME&password=$PASSWORD`
* Remove agent id - `/admin/removeAgentId.pinpoint?applicationName=$APPLICATION_NAME&agentId=$AGENT_ID&password=$PASSWORD`

  Note that the value for the password parameter is what you defined `admin.password` property in *pinpoint-web.properties*. Leaving this blank will allow you to call admin APIs without the password parameter.

## What are the criteria for the application name?

Pinpoint's applicationName doesn't support special characters. such as @,#,$,%,\*. Pinpoint's applicationName only supports \[a-zA-Z0-9], '.', '-', '\_' characters.

## HBase is taking up too much space, which data should I delete first?

Hbase is very scalable so you can always add more region servers if you're running out of space. Shortening the TTL values, especially for **AgentStatV2** and **TraceV2**, can also help (though you might have to wait for a major compaction before space is reclaimed). For details on how to major compact, please refer to [this](https://github.com/pinpoint-apm/pinpoint/blob/master/hbase/scripts/hbase-major-compact-htable.hbase) script.

However, if you **must** make space asap, data in **AgentStatV2** and **TraceV2** tables are probably the safest to delete. You will lose agent statistic data (inspector view) and call stack data (transaction view), but deleting these will not break anything.

Note that deleting **\*MetaData** tables will result in *\*-METADATA-NOT-FOUND* being displayed in the call stack and the only way to "fix" this is to restart all the agents, so it is generally a good idea to leave these tables alone.

## My custom jar application is not being traced. Help!

Pinpoint Agent need an entry point to start off a new trace for a transaction. This is usually done by various WAS plugins (such as Tomcat, Jetty, etc) in which a new trace is started when they receive an RPC request. For custom jar applications, you need to set this manually as the Agent does not have knowledge of when and where to start a trace. You can set this by configuring `profiler.entrypoint` in *pinpoint.config* file.

## Building is failing after new release. Help!

Please remember to run the command `./mvnw clean verify -DskipTests=true` if you've used a previous version before, and replace './mvnw' with './mvnw\.cmd' if you are using Windows.

## How to set java runtime option when using atlassian OSGi

`-Datlassian.org.osgi.framework.bootdelegation=sun.,com.sun.,com.navercorp.*,org.apache.xerces.*`

## Why do I see UI send requests to <https://www.google-analytics.com/collect?>

Pinpoint Web module has google analytics attached which tracks the number and the order of button clicks in the Server Map, Transaction List, and the Inspector View.\
This data is used to better understand how users interact with the Web UI which gives us valuable information on improving Pinpoint Web's user experience. To disable this for any reason, set following option to false in pinpoint-web.properties for your web instance.

```
config.sendUsage=false
```

## I'd like to use Hbase 2.x for Pinpoint.

If you'd like to use Hbase 2.x for Pinpoint database, check out [Hbase2-module](https://github.com/pinpoint-apm/pinpoint/tree/master/hbase2-module).


# Powered by Pinpoint

This page, documents **alphabetical list** of organizations using Pinpoint.

## Sites using Pinpoint

1. Coupang ([www.coupang.com](http://www.coupang.com))
2. Echemi ([www.echemi.com](http://www.echemi.com))
3. HANATOUR ([www.hanatour.com](http://www.hanatour.com))
4. NAVER ([www.naver.com](http://www.naver.com))
5. NHN Entertainment
6. Pikicast ([www.pikicast.com](http://www.pikicast.com))
7. SKPlanet ([www.skplanet.com](http://www.skplanet.com))
8. THE PIRATES([www.tpirates.com](http://www.tpirates.com))
9. Toss ([toss.im](https://toss.im))
10. XLGAMES ([www.xlgames.com](http://www.xlgames.com))

## Naver

Naver Co., Ltd. uses Pinpoint as primary APM. Monitoring 2k+ applications with 10k+ instances. Supports 870k+ tps with only 17 Pinpoint-Collectors. Around 70 billion span chunks are collected per day. Which is equivalent to 10 billion transaction.


# Resources

If you have created informative posts on pinpoint and want the link to be added. Feel free to contact us anytime. We are glad to add more links.

## Resources (KOREAN)

* 유용한 자료를 작성하셨다면 공유부탁드립니다!!!
* [Pinpoint 개발자가 작성한 Pinpoint 기술문서 (helloworld.naver.com)](http://helloworld.naver.com/helloworld/1194202)
* [설치 가이드 동영상 강좌 1 (okjsp 대표 허광남님)](https://www.youtube.com/watch?v=hrvKaEaDEGs)
* [설치 가이드 동영상 강좌 2 (okjsp 대표 허광남님)](https://www.youtube.com/watch?v=fliKPGHGXK4)

## Resources (ENGLISH)

* Anyone who would like to share any document are always welcome
* [Technical Overview of Pinpoint](https://github.com/pinpoint-apm/pinpoint/wiki/Technical-Overview-Of-Pinpoint)
* [Official Docker Repository](https://github.com/pinpoint-apm/pinpoint-docker)
* [Notes on Jetty Plugin for Pinpoint](https://github.com/cijung/Docs/blob/master/JettyPluginNotes.md) ([@cijung](https://github.com/cijung))

## Resources (中文)

* [Pinpoint学习笔记](http://skyao.gitbooks.io/leaning-pinpoint/)：中文资料收集整理和更重要的-中文翻译！
* [Pinpoint - 应用性能管理(APM)平台实践之部署篇](https://sconts.com/11)
* [开源APM工具Pinpoint线上部署](https://www.iqarr.com/2018/02/04/java/pinpoint/pinpoint-deploy/)


# Introduction

[![Maven](https://img.shields.io/github/actions/workflow/status/pinpoint-apm/pinpoint/maven.yml?branch=master\&label=build\&logo=github)](https://github.com/pinpoint-apm/pinpoint/actions?query=workflow%3AMaven) [![codecov](https://codecov.io/gh/pinpoint-apm/pinpoint/branch/master/graph/badge.svg)](https://codecov.io/gh/pinpoint-apm/pinpoint)

**Pinpoint** is an APM (Application Performance Management) tool for large-scale distributed systems written in Java / [PHP](https://github.com/pinpoint-apm/pinpoint-c-agent). Inspired by [Dapper](http://research.google.com/pubs/pub36356.html), Pinpoint provides a solution to help analyze the overall structure of the system and how components within them are interconnected by tracing transactions across distributed applications.

You should definitely check **Pinpoint** out If you want to

* understand your [application topology](https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/overview) at a glance
* monitor your application in *Real-Time*
* gain code-level visibility to every transaction
* install APM Agents without changing a single line of code
* have minimal impact on the performance (approximately 3% increase in resource usage)

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-a15a27acd3b0d96723a857cf64503b9979c76bfa%2Fss_server-map.png?alt=media)

## Live Demo

* [demo](http://223.130.142.103:8080/main/ApiGateway@SPRING_BOOT/5m?inbound=1\&outbound=4\&wasOnly=false\&bidirectional=false) - Here is a Demo, So that you can take a look at Pinpoint right away.

## Want a quick tour?

* [Overview](https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/overview) / [History](https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/history) / [Tech Details](https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/techdetail) to get to know more about Pinpoint
* [Videos](https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/videos) - Checkout our videos on Pinpoint

{% embed url="<https://youtu.be/U4EwnB34Dus>" %}

## Getting Started

* [Quick-start guide(Lastest Snapshot)](https://pinpoint-apm.gitbook.io/pinpoint/getting-started/quickstart) for simple test run of Pinpoint
* [Installation guide(Lastest Snapshot)](https://pinpoint-apm.gitbook.io/pinpoint/getting-started/installation) for further instructions.

## Google Analytics

The web module has google analytics attached that tracks the number and the order of button clicks in the server map, transaction list, and the inspector view.

This data is used to better understand how users interact with the Web UI which gives us valuable information in improving Pinpoint Web's user experience. To disable this for any reason, set the following option to false in *pinpoint-web.properties* for your web instance.

```
config.sendUsage=false
```

## Is your application created with PHP?

Pinpoint has started to support application written in PHP. [Check-out our php-agent repository](https://github.com/pinpoint-apm/pinpoint-c-agent).

## Looking for place to ask questions?

[Questions and FAQ](https://pinpoint-apm.gitbook.io/pinpoint/faq)

## License

Pinpoint is licensed under the Apache License, Version 2.0. See [LICENSE](https://github.com/pinpoint-apm/pinpoint/blob/master/LICENSE) for full license text.

```
Copyright 2019 NAVER Corp.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```


# What's New

## New Features

Supports Java 25

## What's Changed

* \[#12559] Prepare 3.0.4-SNAPSHOT by @intr3p1d in <https://github.com/pinpoint-apm/pinpoint/pull/12568>
* \[#12657] Backport: Update mono runnable interceptor of reactor pulgin by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12658>
* \[#noissue] 3.0.4-alpha1 release by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12659>
* \[#noissue] rollback 3.0.4-alpha1 release by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12661>
* \[#12664] Backport: Fix nested jar loading of instrument class scanner by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12665>
* \[#12667] Backport: Fix kafka plugin streams interceptor by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12668>
* \[#12905] Backport: Update agent "not matched stack id" error log by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12906>
* \[#12919] Backport: Fix agent NPE in annotation value mapper by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12947>
* \[#12966] Backport: Remove validation annotations from high-frequency collector methods to fix performance regression by @Copilot in <https://github.com/pinpoint-apm/pinpoint/pull/12967>
* \[#12948] Backport: Bump asm from 9.7.1 to 9.8 by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12949>
* \[#12986] Backport : Introducing jitter-based scheduling for LinkScheduler by @emeroad in <https://github.com/pinpoint-apm/pinpoint/pull/12988>
* \[#13030] Backport: Bump spring-security by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/13042>
* \[#13033] Backport: Bump ASM from 9.8 to 9.9 by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/13043>
* \[#13054] 3.0.4 release by @intr3p1d in <https://github.com/pinpoint-apm/pinpoint/pull/13055>

**Full Changelog**: <https://github.com/pinpoint-apm/pinpoint/compare/v3.0.3...v3.0.4>

## Upgrade consideration

HBase compatibility table:

| Pinpoint Version | HBase 1.x | HBase 2.x                                                                                                             |
| ---------------- | --------- | --------------------------------------------------------------------------------------------------------------------- |
| 2.0.x - 2.2.x    | yes       | [optional](https://pinpoint-apm.gitbook.io/pinpoint/documents/hbase-upgrade#do-you-like-to-use-hbase-2x-for-pinpoint) |
| 2.3.x - 2.5.x    | yes       | [hbase2-module](https://github.com/pinpoint-apm/pinpoint/tree/2.3.x/hbase2-module)                                    |
| 3.0.x            | no        | yes                                                                                                                   |
| 3.1.x            | no        | yes                                                                                                                   |

Agent compatibility to Collector table:

| Agent Version | Collector 2.x.x | Collector 3.0.x | Collector 3.1.x |
| ------------- | --------------- | --------------- | --------------- |
| 2.x.x         | yes             | yes             | yes             |
| 3.0.x         | no              | yes             | yes             |
| 3.1.x         | no              | no              | yes             |

Additionally, the required Java version to run each Pinpoint component is given below:

| Pinpoint Version | Agent | Collector | Web | Batch |
| ---------------- | ----- | --------- | --- | ----- |
| 2.0.x            | 6-13  | 8         | 8   | 8     |
| 2.1.x            | 6-14  | 8         | 8   | 8     |
| 2.2.x            | 7-14  | 8         | 8   | 8     |
| 2.3.x            | 7-17  | 8         | 8   | 8     |
| 2.4.x            | 7-18  | 11        | 11  | 11    |
| 2.5.x            | 8-19  | 11        | 11  | 11    |
| 3.0.x            | 8-21  | 17        | 17  | 17    |
| 3.1.x            | 8-24  | 17        | 17  | 17    |

## Supported Modules

* JDK 6+
* Supported versions of the \* indicated library may differ from the actual version.

| Title                                                                                                          | Instrumented Library                 | Min      | Max       | Comment |   |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------ | -------- | --------- | ------- | - |
| [Tomcat](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/tomcat)                     |                                      | 6.x      | 9.x       |         |   |
| [Jetty](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/jetty)                       |                                      | 8.x      | 9.x       |         |   |
| [JBoss](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/jboss)                       |                                      | 6.x      | 7.x       |         |   |
| [Websphere](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/websphere)               |                                      | 6.x      | 8.x       |         |   |
| [Vertx](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/vertx)                       |                                      | 3.3      | 3.5       |         |   |
| [Weblogic](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/weblogic)                 |                                      | 10.x     | 12.x      |         |   |
| [Undertow](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/undertow)                 |                                      |          |           |         |   |
| [Undertow Servlet](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/undertow-servlet) |                                      |          |           |         |   |
| Jasper                                                                                                         |                                      |          |           |         |   |
|                                                                                                                |                                      |          |           |         |   |
| Java Async Thread                                                                                              |                                      |          |           |         |   |
|                                                                                                                |                                      |          |           |         |   |
| OpenWhisk                                                                                                      | whisk.core                           |          |           |         |   |
|                                                                                                                |                                      |          |           |         |   |
| SpringMVC Framework                                                                                            | spring-webmvc                        | 3.0.7    | 5.3.6     |         |   |
| Spring Web                                                                                                     | spring-web                           | 4.1.2    | 4.3.30    |         |   |
| Spring RabbitMQ                                                                                                | spring-rabbit                        | 1.3.3    | 2.2.16    |         |   |
| Spring IBatis                                                                                                  | spring-ibatis                        | 2.0.7    | 2.0.8     |         |   |
| Spring MyBatis                                                                                                 | mybatis-spring                       | 1.1.0    | 1.3.3     |         |   |
| \*[Spring Boot](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/spring-boot)         | spring-boot-autoconfigure            |          |           |         |   |
| \*[Spring Webflux](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/spring-webflux)   | spring-webflux                       |          |           |         |   |
|                                                                                                                |                                      |          |           |         |   |
| MyBatis                                                                                                        | mybatis                              | 3.0.3    | 3.3.1     |         |   |
| [Hystrix](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/hystrix)                   | hystrix-core                         | 1.4.0    | 1.5.18    |         |   |
|                                                                                                                |                                      |          |           |         |   |
| JDKHTTP                                                                                                        |                                      |          |           |         |   |
| Httpclient3                                                                                                    | commons-httpclient                   | 3.0      | 3.1       |         |   |
| Httpclient4                                                                                                    | httpclient                           | 4.0      | 4.5.4     |         |   |
| Thrift                                                                                                         | libthrift                            | 0.9.1    | 0.14.1    |         |   |
| Google HTTP Client                                                                                             | google-http-client                   | 1.19.0   | 1.39.2    |         |   |
| AsyncHttpClient                                                                                                | async-http-client                    | 1.7.24   | 1.8.17    |         |   |
| OkHttp                                                                                                         | okhttp                               | 2.0.0    | 3.3.1     |         |   |
| Apache HttpAsyncClient                                                                                         | httpasyncclient                      | 4.0      | 4.1.3     |         |   |
| \*Akka HTTP                                                                                                    | akka-http\_2.12                      | 10.1.0   | 10.1.x    |         |   |
| \*[Kafka](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/kafka)                     | kafka-clients                        | 0.11.0.1 |           |         |   |
| GRPC                                                                                                           | grpc-stub                            | 1.8.0    | 1.37.0    |         |   |
| \*[Reactor](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/reactor)                 | reactor-core                         | 3.3.0    | 3.3.1     |         |   |
| \*[Reactor Netty](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/reactor-netty)     | reactor-netty                        | 0.8.0    | 0.9.2     |         |   |
|                                                                                                                |                                      |          |           |         |   |
| Log4j                                                                                                          | log4j                                | 1.2.16   | 1.2.17    |         |   |
| Logback                                                                                                        | logback-classic                      | 1.0.13   | 1.2.3     |         |   |
| Log4j2                                                                                                         | log4j-core                           | 2.0      | 2.12.1    |         |   |
|                                                                                                                |                                      |          |           |         |   |
| \*Arcus                                                                                                        | arcus-java-client                    | 1.7.0    | 1.11.4    |         |   |
| \*MsSQL (jTDS)                                                                                                 | jtds                                 | 1.2.8    |           |         |   |
| \*MsSQL                                                                                                        | mssql-jdbc                           |          |           |         |   |
| HikariCP                                                                                                       | HikariCP-java6                       | 2.3.0    | 2.3.13    |         |   |
| Jackson-mapper-asl                                                                                             | jackson-mapper-asl                   | 1.0.1    | 1.8.11    |         |   |
| Jackson Databind                                                                                               | jackson-databind                     | 2.0.6    | 2.12.3    |         |   |
| MariaDB Connector/J                                                                                            | mariadb-java-client                  | 1.3.0    | 2.7.2     |         |   |
| MongoDB Java Driver                                                                                            | mongodb-driver                       | 3.0.0    | 3.12.8    |         |   |
| Elasticsearch                                                                                                  | elasticsearch-rest-high-level-client | 6.0.0    | 6.8.15    |         |   |
| Datastax Java Driver                                                                                           | cassandra-driver-core                | 2.0.10   | 3.11.0    |         |   |
| Druid                                                                                                          | druid                                | 1.0.0    | 1.2.6     |         |   |
| \*Cubrid                                                                                                       | cubrid-jdbc-driver                   | 8.4.1    | 10.0.0    |         |   |
| \*Commons DBCP                                                                                                 | commons-dbcp                         | 1.0      | 1.4       |         |   |
| \*Commons DBCP2                                                                                                | commons-dbcp2                        | 2.0      | 2.5.0     |         |   |
| \*HBase                                                                                                        | hbase-client                         | 1.2.6.1  | 1.2.6.1   |         |   |
| \*MySQL                                                                                                        | mysql-connector-java                 | 5.0      | 8.x       |         |   |
| \*Oracle JDBC Driver                                                                                           | ojdbc                                |          |           |         |   |
| \*PostgreSQL JDBC Driver                                                                                       | postgresql                           |          |           |         |   |
| \*[Redis](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/redis)                     | jedis                                | 2.4.2    |           |         |   |
| \*[Redis](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/redis-lettuce)             | lettuce-core                         | 5.0.0    | 5.1.2     |         |   |
| \*[Redis](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/redis-redisson)            | redisson                             | 3.10.0   | 3.10.4    |         |   |
|                                                                                                                |                                      |          |           |         |   |
| Apache CXF                                                                                                     | cxf-rt-rs-client                     | 3.0.0    | 3.4.3     |         |   |
| Netty                                                                                                          | netty-all                            | 4.1.0    | 4.1.63    |         |   |
| ActiveMQ                                                                                                       | activemq-all                         | 5.1.0    | 5.16.1    |         |   |
| [RxJAVA](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/rxjava)                     | rxjava                               | 1.0.0    | 1.3.8     |         |   |
| [RabbitMQ](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/rabbitmq)                 | amqp-client                          | 2.7.0    | 5.12.0    |         |   |
| [Paho MQTT](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/paho-mqtt)               | org.eclipse.paho.client.mqttv3       | 1.0.2    | 1.2.5     |         |   |
| [Paho MQTT](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/paho-mqtt)               | org.eclipse.paho.mqttv5.client       | 1.2.5    | 1.2.5     |         |   |
|                                                                                                                |                                      |          |           |         |   |
| Gson                                                                                                           | gson                                 | 1.1      | 2.8.3     |         |   |
| Json                                                                                                           | json-lib                             | 1.0      | 2.2.2     |         |   |
| FastJson                                                                                                       | fastjson                             | 1.2.10   | 1.2.76    |         |   |
| Dubbo                                                                                                          | dubbo                                | 2.5.1    | 2.6.9     |         |   |
| kafka-clients                                                                                                  | kafka-clients                        | 0.11.0.0 | 2.6.1     |         |   |
| postgresql                                                                                                     | postgresql                           | 9.4.1208 | 42.2.19   |         |   |
| ojdbc8                                                                                                         | ojdbc8                               | 12.2.0.1 | 21.1.0.0  |         |   |
| ojdbc10                                                                                                        | ojdbc10                              | 19.3.0.0 | 19.10.0.0 |         |   |


# Overview

Services nowadays often consist of many different components, communicating amongst themselves as well as making API calls to external services. How each and every transaction gets executed is often left as a blackbox. Pinpoint traces transaction flows between these components and provides a clear view to identify problem areas and potential bottlenecks.

* **ServerMap** - Understand the topology of any distributed systems by visualizing how their components are interconnected. Clicking on a node reveals details about the component, such as its current status, and transaction count.
* **Realtime Active Thread Chart** - Monitor active threads inside applications in real-time.
* **Request/Response Scatter Chart** - Visualize request count and response patterns over time to identify potential problems. Transactions can be selected for additional detail by **dragging over the chart**.

![Server Map](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-a15a27acd3b0d96723a857cf64503b9979c76bfa%2Fss_server-map.png?alt=media)

* **CallStack** - Gain code-level visibility to every transaction in a distributed environment, identifying bottlenecks and points of failure in a single view.

![Call Stack](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-735f042f7dc51378efe3f24d2ce53e1f295409d4%2Fss_call-stack.png?alt=media)

* **Inspector** - View additional details on the application such as CPU usage, Memory/Garbage Collection, TPS, and JVM arguments.

![Inspector](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-07c84a62894cf4307ed7dc6ab2f5e44013ca2892%2Fss_inspector.png?alt=media)

## Architecture

![Pinpoint Architecture](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-fc010a909c9559db169703072bd0dccacc283078%2Fpinpoint-architecture.png?alt=media)


# History

Pinpoint is a platform that analyzes large-scale distributed systems and provides a solution to handle large collections of trace data. It has been developed since July 2012 and was launched as an open-source project on January 9, 2015.

This article introduces Pinpoint; it describes what motivated us to start this project, which technologies are used, and how the Pinpoint Agent can be optimized.

> 本文的中文翻译版本 [请见这里](https://github.com/skyao/leaning-pinpoint/blob/master/design/technical_overview.md)

## Motivation to Get Started & Pinpoint Characteristics

Compared to nowadays, the number of Internet users was relatively small and the architecture of Internet services was less complex. Web services were generally configured using a 2-tier (web server and database) or 3-tier (web server, application server, and database) architecture. However, today, supporting a large number of concurrent connections is required and functionalities and services should be organically integrated as the Internet has grown, resulting in much more complex combinations of the software stack. That is n-tier architecture more than 3 tiers has become more widespread. A service-oriented architecture (SOA) or the [microservices](http://en.wikipedia.org/wiki/Microservices) architecture is now a reality.

The system's complexity has consequently increased. The more complex it is, the more difficult you solve problems such as system failure or performance issues. For example, Finding solutions in a 3-tier system is far less complicated. You only need to analyze 3 main components; a web server, an application server, and a database where the number of servers is small. While, if a problem occurs in an n-tier architecture, a large number of components and servers should be investigated. Another problem is that it is difficult to see the big picture only with an analysis of individual components; a low visibility issue is raised. The higher the degree of system complexity is, the longer it takes time to find out the reasons. Even worse, probability increases in which we may not even find them at all.

Such problems have occurred in the systems at NAVER. A variety of tools like Application Performance Management (APM) were used but they were not enough to handle the problems effectively; so we finally ended up developing a new tracing platform for n-tier architecture, which can provide solutions to systems with an n-tier architecture.

Pinpoint, began development in July 2012 and was launched as an open-source project in January 2015, is an n-tier architecture tracing platform for large-scale distributed systems. The characteristics of Pinpoint are as follows:

* Distributed transaction tracing to trace messages across distributed applications
* Automatically detecting the application topology that helps you to figure out the configurations of an application
* Horizontal scalability to support large-scale server group
* Providing code-level visibility to easily identify points of failure and bottlenecks
* Adding a new functionality without code modifications, using the bytecode instrumentation technique


# Tech Details

In this article, we describe the Pinpoint's techniques such as transaction tracing and bytecode instrumentation. And we explain the optimization method applied to Pinpoint Agent, which modifies bytecode and record performance data.

## Distributed Transaction Tracing, Modeled after Google's Dapper

Pinpoint traces distributed requests in a single transaction, modeled after Google's Dapper.

### How Distributed Transaction Tracing Works in Google's Dapper

The purpose of a distributed tracing system is to identify relationships between Node 1 and Node 2 in a distributed system when a message is sent from Node 1 to Node 2 (Figure 1).

![Figure 1. Message relationship in a distributed system](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-9473e149d5d3ec8ddbc00e2c8834478edb9b63d0%2Ftd_figure1.png?alt=media)

Figure 1. Message relationship in a distributed system

The problem is that there is no way to identify relationships between messages. For example, we cannot recognize relationships between N messages sent from Node 1 and N' messages received in Node 2. In other words, when X-th message is sent from Node 1, the X-th message cannot be identified among N' messages received in Node 2. An attempt was made to trace messages at TCP or operating system level. However, implementation complexity was high with low performance because it should be implemented separately for each protocol. In addition, it was difficult to accurately trace messages.

However, a simple solution to resolve such issues has been implemented in Google's Dapper. The solution is to add application-level tags that can be a link between messages when sending a message. For example, it includes tag information for a message in the HTTP header at an HTTP request and traces the message using this tag.

> Google's Dapper
>
> For more information on Google's Dapper, see "[Dapper, a Large-Scale Distributed Systems Tracing Infrastructure](http://research.google.com/pubs/pub36356.html)."

Pinpoint is modeled on the tracing technique of Google's Dapper but has been modified to add application-level tag data in the call header to trace distributed transactions at a remote call. The tag data consists of a collection of keys, which is defined as a TraceId.

### Data Structure in Pinpoint

In Pinpoint, the core of data structure consists of Spans, Traces, and TraceIds.

* Span: The basic unit of RPC (remote procedure call) tracing; it indicates work processed when an RPC arrives and contains trace data. To ensure the code-level visibility, a Span has children labeled SpanEvent as a data structure. Each Span contains a TraceId.
* Trace: A collection of Spans; it consists of associated RPCs (Spans). Spans in the same trace share the same TransactionId. A Trace is sorted as a hierarchical tree structure through SpanIds and ParentSpanIds.
* TraceId: A collections of keys consisting of TransactionId, SpanId, and ParentSpanId. The TransactionId indicates the message ID, and both the SpanId and the ParentSpanId represent the parent-child relationship of RPCs.
  * TransactionId (TxId): The ID of the message sent/received across distributed systems from a single transaction; it must be globally unique across the entire group of servers.
  * SpanId: The ID of a job processed when receiving RPC messages; it is generated when an RPC arrives at a node.
  * ParentSpanId (pSpanId): The SpanId of the parent span which generated the RPC. If a node is the starting point of a transaction, there will not be a parent span - for these cases, we use a value of -1 to denote that the span is the root span of a transaction.

> Differences in terms between Google's Dapper and NAVER's Pinpoint
>
> The term "TransactionId" in Pinpoint has the same meaning as the term "TraceId" in Google's Dapper and the term "TraceId" in Pinpoint refers to a collection of keys.

### How TraceId Works

The figure below illustrates the behavior of a TraceId in which RPCs were made 3 times within 4 nodes.

![Figure 2. Example of a TraceId behavior](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-e40328489e218852c90f58e486f1107fecce2bb7%2Ftd_figure2.png?alt=media)

Figure 2. Example of a TraceId behavior

A TransactionId (TxId) represents that three different RPCs are associated with each other as a single transaction in Figure 2. However, a TransactionId itself can't explicitly describe the relationship between RPCs. To identify the relationships between RPCs, a SpanId and a ParentSpanId (pSpanId) are required. Suppose that a node is Tomcat. You can think of a SpanId as a thread which handles HTTP requests. A ParentSpanId indicates the SpainId of a parent that makes RPC calls.

Pinpoint can find associated n Spans using a TransactionId and can sort them as a hierarchical tree structure using a SpanId and a ParentSpanId.

A SpanId and a ParentSpanId are 64-bit long integers. A conflict might arise because the number is generated arbitrarily, but considering the range of value from -9223372036854775808 to 9223372036854775807, this is unlikely to happen. If there is a conflict between keys, Pinpoint as well as Google's Dapper lets developers know what happened, instead of resolving the conflict.

A TransactionId consists of AgentIds, JVM (Java virtual machine) startup time, and SequenceNumbers.

* AgentId: A user-created ID when JVM starts; it must be globally unique across the entire group of servers where Pinpoint has been installed. The easiest way to make it unique is to use a hostname ($HOSTNAME) because the hostname is not duplicate in general. If you need to run multiple JVMs within the server group, add a postfix to the hostname to avoid duplicates.
* JVM startup time: Required to guarantee a unique SequenceNumber which starts with zero. This value is used to prevent ID conflicts when a user creates duplicate AgentId by mistake.
* SequenceNumber: ID issued by the Pinpoint Agent, with sequentially increasing numbers that start with zero; it is issued per message.

Dapper and [Zipkin](https://github.com/twitter/zipkin), a distributed systems tracing platform at Twitter, generate random TraceIds (TransactionIds in Pinpoint) and consider conflict situations as a normal case. However, we wanted to avoid this conflict as much as possible in Pinpoint. We had two available options for this; one with a method in which the amount of data is small but the probability of conflict is high; the other is a method in which the amount of data is large but the probability of conflict is low; We chose the second option.

There may be a better ways to handle transactions. We came up with several ideas such as key issue by a central key server. But we didn't implement this in the system due to performance issues and network errors. We are still considering issuing keys in bulk as an alternative Solution. So maybe later in the future, such methods can be developed; But for now, a simple method is adopted. In Pinpoint, a TransactionId is regarded as changeable data.

## Bytecode Instrumentation, Not Requiring Code Modifications

Earlier, we explained distributed transaction tracing. One way for implementing this is that developers to modify their code by themselves. Allow developers to add tag information when an RPC is made. However, it could be a burden to modify code even though such functionality is useful to developers.

Twitter's Zipkin provides the functionality of distributed transaction tracing using modified libraries and its container (Finagle). However, it requires the code to be modified if needed. We wanted the functionality to work without code modifications and desired to ensure code-level visibility. To solve such problems, the bytecode instrumentation technique was adopted in Pinpoint. The Pinpoint Agent intervenes code to make RPCs so as to automatically handle tag information.

### Overcoming Disadvantages of Bytecode Instrumentation

There are two ways for distributed transaction tracing as below. Bytecode instrumentation is one of an automatic method.

* Manual method: Developers develop code that records data at important points using APIs provided by Pinpoint.
* Automatic method: Developers do not involve code modifications because Pinpoint decides which API is to be intervened and developed.

Advantages and disadvantages of each method are as follows:

Table 1 Advantages and disadvantage of each method

| Item                  | Advantage                                                                                                                   | Disadvantage                                                                                                                                                                                                                                                                                                                       |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Manual Tracing**    | - Requires less development resources. - An API can become simpler and consequently the number of bugs can be reduced.      | - Developers must modify the code. - Tracing level is low.                                                                                                                                                                                                                                                                         |
| **Automatic Tracing** | - Developers are not required to modify the code. - More precise data can be collected due to more information in bytecode. | - It would cost 10 times more to develop Pinpoint with automatic method. - Requires highly competent developers who can instantly recognize the library code to be traced and make decisions on the tracing points. - Can increase the possibility of a bug due to high-level development skills such as bytecode instrumentation. |

Bytecode instrumentation is a technique that includes high difficulty level and risks. Nevertheless, using this technique has many benefits.

Although it requires a large number of development resources, it requires almost none for applying the service. For example, the following shows the costs between an automatic method which uses bytecode instrumentation and a manual method which uses libraries (in this context, costs are random numbers assumed for clarity).

* Automatic method: Total of 100
  * Cost of Pinpoint development: 100
  * Cost of services applied: 0
* Manual method: Total of 30
  * Cost of Pinpoint development: 20
  * Cost of services applied: 10

The data above tells us that a manual method is more cost-effective than an automatic one. However, it will not guarantee the same result for NAVER since we have thousands of services. For example, if we have 10 services which require being modified, the total cost will be calculated as follows:

* Cost of Pinpoint development 20 + Cost of services applied 10 x 10 services = 120

As you can see, the automatic method was more cost-efficient for us.

We are lucky to have many developers who are highly competent and specialized in Java in the Pinpoint team. Therefore, we believed it was only a matter of time to overcome the technical difficulties in Pinpoint development.

### The Value of Bytecode Instrumentation

The reason we chose to implement bytecode instrumentation(Automatic method) is not only those that we have already explained but also the following points.

#### Hidden API

If the API is exposed for developers to use. We, as API providers, are restricted to modify the API as we desire. Such a restriction can impose stress on us.

We may modify an API to correct mistaken design or add new functions. However, if there is a restriction to do this, it would be difficult for us to improve the API. The best answer for solving such a problem is a scalable system design, which is not an easy option as everyone knows. It is almost impossible to create perfect API design as we can't predict the future.

With bytecode instrumentation, we don't have to worry about the problems caused by exposing the tracing APIs and can continuously improve the design, without considering dependency relationships. For those who are planning to develop their applications using Pinpoint, please note that API can be changed by the Pinpoint developers since improving performance and design is our first priority.

#### Easy to Enable or Disable

The disadvantage of using bytecode instrumentation is that it could affect your applications when a problem occurs in the profiling section of a library or Pinpoint itself. However, you can easily solve it by just disabling the Pinpoint since you don't have to change any code.

You can easily enable Pinpoint for your applications by adding the three lines (associated with the configuration of the Pinpoint Agent) below into your JVM startup script:

```
-javaagent:$AGENT_PATH/pinpoint-bootstrap-$VERSION.jar
-Dpinpoint.agentId=<Agent's UniqueId>
-Dpinpoint.applicationName=<The name indicating a same service (AgentId collection)>
```

If any problem occurs due to Pinpoint, you can just delete the configuration data in the JVM startup script.

### How Bytecode Instrumentation Works

Since bytecode instrumentation technique has to deal with Java bytecode, it tends to increase the risk of development while it decreases productivity. In addition, developers are prone to make mistakes. In Pinpoint, we improved productivity and accessibility by abstraction with the interceptor. Pinpoint injects necessary codes to track distributed transactions and performance information by intervening application code at class loading time. This increases performance since tracking codes are directly injected into the application code.

![Figure 3. Behavior of bytecode instrumentation](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-609a918a392f37fd672a3b18b908c3fe5575abde%2Ftd_figure3.png?alt=media)

Figure 3. Basic principle of bytecode instrumentation

In Pinpoint, the API intercepting part and data recording part are separated. Interceptor is injected into the method that we'd like to track and calls before() and after() methods where data recording is taken care of. Through bytecode instrumentation, Pinpoint Agent can record data only from the necessary method which makes the size of profiling data compact.

## Optimizing Performance of the Pinpoint Agent

Finally, we will describe how to optimize the performance of Pinpoint Agent.

### Using Binary Format (Thrift)

You can increase encoding speed by using a binary format ([Thrift](https://thrift.apache.org/)). Although it is difficult to use and debug, It can improve the efficiency of network usage by reducing the size of data generated.

### Optimize Recorded Data for Variable-Length Encoding and Format

If you convert a long integer into a fixed-length string, the data size will be 8 bytes. However, if you use variable-length encoding, the data size can vary from 1 to 10 bytes depending on the size of a given number. To reduce data size, Pinpoint encodes data as a variable-length string through Compact Protocol of Thrift and records data to be optimized for encoding format. Pinpoint Agent reduces data size by converting remaining time based on root method into a vector value.

> Variable-length encoding
>
> For more information on the variable-length encoding, see "[Base 128 Varints](https://developers.google.com/protocol-buffers/docs/encoding#varints)" in Google Developers.

![Figure 4. Comparison between fixed-length encoding and variable-length encoding](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-4ad3f0fc9dc26c54c3dc86a4851d0261c3252ca6%2Ftd_figure4.png?alt=media)

Figure 4. Comparison between fixed-length encoding and variable-length encoding

As you can see in Figure 4, you need to measure the time of 6 different points to get information of when three different methods are called and finished(Figure 4); With fixed-length encoding, this process requires 48 bytes (6points × 8bytes).

Meanwhile, Pinpoint Agent uses variable-length encoding and records the data according to its corresponding format. And calculate time information on other points with the difference(in vector value) based on the start time of the root method. Since vector value is a small number, it consumes a small number of bytes resulting only 13 bytes consumed rather than 48bytes.

If it takes more time to execute a method, it will increase the number of bytes even though variable-length encoding is used. However, it is still more efficient than fixed-length encoding.

### Replacing Repeated API Information, SQLs, and Strings with Constant Tables

We wanted Pinpoint to enable code-level tracing. However, it had a problem in terms of increasing data size. Every time data with a high degree of precision is sent to a server, due to the size of the data it increased network usage.

To solve such a problem, we adopted a strategy by creating a constant table in a remote HBase server. Since there will be an overload to send data of "method A" to Pinpoint Collector each time, Pinpoint Agent converts "method A" data to an ID and stores this information as a constant table in HBase, and continue tracing data with the ID. When a user retrieves trace data on the Website, the Pinpoint Web searches for the method information of the corresponding ID in the constant table and reorganize them. The same way is used to reduce data size in SQLs or frequently-used strings.

### Handling Samples for Bulk Requests

The requests to online portal services which Naver is providing are huge. A single service handles more than 20 billion requests a day. A simple way to trace such request is by expanding network infrastructure and servers as much as needed to suit the number of requests. However, this is not a cost-effective way to handle such situations.

In Pinpoint, you can collect only sampling data rather than tracking every request. In a development environment where requests are few, every data is collected. While in the production environment where requests are large, only 1\~5% out of whole data is collected which is sufficient to analyze the status of entire applications. With sampling, you can minimize network overhead in applications and reduce costs of infrastructure such as networks and servers.

> Sampling method in Pinpoint
>
> Pinpoint supports a Counting sampler, which collects data only for one of 10 requests if it is set to 10. We plan to add new samplers that can collect data more effectively.

### Minimizing Application Threads Being Aborted Using Asynchronous Data Transfer

Pinpoint does not interfere with application threads since encoded data or remote messages are transferred asynchronously by another thread.

#### Transferring Data via UDP

Unlike Google's Dapper, Pinpoint transfers data through a network to ensure data speed. Sharing network with your service can be an issue when data traffic bursts out. In such situations, the Pinpoint Agent starts to use UDP protocol to give the network connection priority to your service.

> Note
>
> The data transfer APIs can be replaced since it's separated as an interface. It can be changed into an implementation that stores data in a different way, like local files.

## Example of Pinpoint Applied

Here is an example of how to get data from your application so that you can comprehensively understand the contents described earlier.

Figure 5 shows what you can see when you install Pinpoint in TomcatA and TomcatB. You can see the trace data of an individual node as a single transaction, which represents the flow of distributed transaction tracing.

![Figure 5. Example 1: Pinpoint applied](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-f9194d26378f10cc869a147b5bec42932e6bad76%2Ftd_figure5.png?alt=media)

Figure 5. Example of Pinpoint in action

The following describes what Pinpoint does for each method.

1. Pinpoint Agent issues a TraceId when a request arrives at TomcatA.
   * TX\_ID: TomcatA^TIME^1
   * SpanId: 10
   * ParentSpanId: -1(Root)
2. Records data from Spring MVC controllers.
3. Intervene the calls of HttpClient.execute() method and configure the TraceId in HttpGet.
   * Creates a child TraceId.
     * TX\_ID: TomcatA^TIME^1 -> TomcatA^TIME^1
     * SPAN\_ID: 10 -> 20
     * PARENT\_SPAN\_ID: -1 -> 10 (parent SpanId)
   * Configures the child TraceId in the HTTP header.
     * HttpGet.setHeader(PINPOINT\_TX\_ID, "TomcatA^TIME^1")
     * HttpGet.setHeader(PINPOINT\_SPAN\_ID, "20")
     * HttpGet.setHeader(PINPOINT\_PARENT\_SPAN\_ID, "10")
4. Transfer tagged request to TomcatB.
   * TomcatB checks the header from the transferred request.
     * HttpServletRequest.getHeader(PINPOINT\_TX\_ID)
   * TomcatB becomes a child node as it identifies a TraceId in the header.
     * TX\_ID: TomcatA^TIME^1
     * SPAN\_ID: 20
     * PARENT\_SPAN\_ID: 10
5. Records data from Spring MVC controllers and completes the request.

   ![Figure 6. Example 2: Pinpoint applied](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-ea5417ab1e132ffa795122934391fe7f7c1642c1%2Ftd_figure6.png?alt=media)
6. Pinpoint Agent sends trace data to Pinpoint Collector to store it in HBase when the request from TomcatB is completed.
7. After the HTTP calls from TomcatB is terminated, then the request from TomcatA is complete. The Pinpoint Agent sends trace data to Pinpoint Collector to store it in HBase.
8. UI reads the trace data from HBase and creates a call stack by sorting trees.

## Conclusions

Pinpoint is another application that runs along with your applications. Using bytecode instrumentation makes Pinpoint seem like that it does not require code modifications. In general, the bytecode instrumentation technique makes applications vulnerable to risks; if a problem occurs in Pinpoint, it will affect your applications as well. But for now, instead of getting rid of such threats, we are focusing on improving performance and design of Pinpoint. Because we think this makes Pinpoint more valuable. So whether or not to use Pinpoint is for you to decide.

We still have a large amount of work to be done to improve Pinpoint. Despite its incompleteness, Pinpoint was released as an open-source project; we are continuously trying to develop and improve Pinpoint so as to meet your expectations.

> Written by Woonduk Kang
>
> In 2011, I wrote about myself like this—As a developer, I would like to make a software program that users are willing to pay for, like those of Microsoft or Oracle. As Pinpoint was launched as an open-source project, it seems that my dreams somewhat came true. For now, my desire is to make Pinpoint more valuable and attractive to users.


# Videos

## Speaking at COSCUP2019

Speaking at Taiwan's largest open source conference

Title : [Naver, monitoring services with trillions of event with open source APM, Pinpoint](https://coscup.org/2019/en/programs/naver-monitoring-services-with-trillions-of-event-with-open-source-apm-pinpoint)\
Date : Aug 18, 2019

{% embed url="<https://youtu.be/Uyy:CgRc5:M>" %}

### Speaking at HKOSCon2019

Speaking at HongKong's largest open source conference

Title : [How we started an open source APM project and troubleshooting with it](https://hkoscon.org/2019/topics/how-we-started-open-source-apm-project-and-troubleshooting-it)\
Date : June 15, 2019

{% embed url="<https://youtu.be/9-Kf87k4sEA>" %}

## Introduction to Pinpoint v1.5.0

Video introducing Pinpoint

{% embed url="<https://youtu.be/U4EwnB34Dus>" %}


# Additional Plugins

## Third-party agents/plugins

There may be agents, and plugins that are being developed and managed by other individuals/organizations.

Below include agents and plugins that are not merged into this repository.\
Take a look at them if you are interested and would like to help out.

* Plugins
  * Websphere - <https://github.com/sjmittal/pinpoint/tree/cpu_monitoring_fix/plugins/websphere>
  * RocketMQ - <https://github.com/ruizlake/pinpoint/tree/master/plugins/rocketmq>

If you are working on an agent or a plugin and want to add it to this list, please feel free to [contact us](mailto:roy.kim@navercorp.com) anytime.


# Quick-start guide

Pinpoint QuickStart provides a sample TestApp for the Agent.

## Docker

Installing Pinpoint with these docker files will take approximately 10min.

Visit [Official Pinpoint-Docker repository](https://github.com/pinpoint-apm/pinpoint-docker) for more information.

## Installation

To set up your very own Pinpoint instance you can either **download the build results** from our [**latest release**](https://github.com/pinpoint-apm/pinpoint/releases/latest).

### HBase

Download, Configure, and Start HBase - [1. Hbase](https://pinpoint-apm.gitbook.io/pinpoint/installation#1-hbase).

```
$ tar xzvf hbase-x.x.x-bin.tar.gz
$ cd hbase-x.x.x/
$ ./bin/start-hbase.sh
```

See [scripts](https://github.com/pinpoint-apm/pinpoint/tree/master/hbase/scripts) and Run.

```
$ ./bin/hbase shell hbase-create.hbase
```

### Pinpoint Collector

Download, and Start Collector - [3. Pinpoint Collector](https://pinpoint-apm.gitbook.io/pinpoint/installation#3-pinpoint-collector)

```
$ java -jar -Dpinpoint.zookeeper.address=localhost pinpoint-collector-boot-2.2.1.jar
```

### Pinpoint Web

Download, and Start Web - [4. Pinpoint Web](https://pinpoint-apm.gitbook.io/pinpoint/installation#4-pinpoint-web)

```
$ java -jar -Dpinpoint.zookeeper.address=localhost pinpoint-web-boot-2.2.1.jar
```

## Java Agent

### Requirements

In order to build Pinpoint, the following requirements must be met:

* JDK 8 installed

### When Using Released Binary(Recommended)

Download Pinpoint from [Latest Release](https://github.com/pinpoint-apm/pinpoint/releases/latest).

Extract the downloaded file.

```
$ tar xvzf pinpoint-agent-2.2.1.tar.gz
```

Run the JAR file, as follows:

```
$ java -jar -javaagent:pinpoint-agent-2.2.1/pinpoint-bootstrap.jar -Dpinpoint.agentId=test-agent -Dpinpoint.applicationName=TESTAPP pinpoint-quickstart-testapp-2.2.1.jar
```

### When Building Manually

Download Pinpoint with `git clone https://github.com/pinpoint-apm/pinpoint.git` or [download](https://github.com/pinpoint-apm/pinpoint/archive/master.zip) the project as a zip file and unzip.

Change to the pinpoint directory, and build.

```
$ cd pinpoint
$ ./mvnw install -DskipTests=true
```

Change to the quickstart testapp directory, and build. Let's build and run.

```
$ cd quickstart/testapp
$ ./mvnw clean package
```

Change to the pinpoint directory, and run.

```
$ cd ../../
$ java -jar -javaagent:agent/target/pinpoint-agent-2.2.1/pinpoint-bootstrap.jar -Dpinpoint.agentId=test-agent -Dpinpoint.applicationName=TESTAPP quickstart/testapp/target/pinpoint-quickstart-testapp-2.2.1.jar
```

### Get Started

You should see some output that looks very similar to this:

```
  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::        (v2.3.2.RELEASE)

2020-08-06 17:24:59.519  INFO 19236 --- [           main] com.navercorp.pinpoint.testapp.TestApp   : Starting TestApp on AD01160256 with PID 19236 (C:\repository\github\pinpoint\quickstart\testapp\target\classes started by Naver in C:\repository\github\pinpoint)
2020-08-06 17:24:59.520  INFO 19236 --- [           main] com.navercorp.pinpoint.testapp.TestApp   : No active profile set, falling back to default profiles: default
2020-08-06 17:24:59.520 DEBUG 19236 --- [           main] o.s.boot.SpringApplication               : Loading source class com.navercorp.pinpoint.testapp.TestApp
2020-08-06 17:24:59.558 DEBUG 19236 --- [           main] o.s.b.c.c.ConfigFileApplicationListener  : Loaded config file 'file:/C:/repository/github/pinpoint/quickstart/testapp/target/classes/application.yml' (classpath:/application.yml)
2020-08-06 17:24:59.558 DEBUG 19236 --- [           main] ConfigServletWebServerApplicationContext : Refreshing org.springframework.boot.web.servlet.context.AnnotationConfigServletWebServerApplicationContext@46185a1b
08-06 17:24:59.059 [           main] INFO  .n.p.p.DefaultDynamicTransformerRegistry:67  -- added dynamic transformer classLoader: sun.misc.Launcher$AppClassLoader@18b4aac2, className: com.navercorp.pinpoint.testapp.controller.ApisController, registry size: 1
08-06 17:24:59.059 [           main] INFO  .n.p.p.DefaultDynamicTransformerRegistry:67  -- added dynamic transformer classLoader: sun.misc.Launcher$AppClassLoader@18b4aac2, className: com.navercorp.pinpoint.testapp.controller.CallSelfController, registry size: 2
08-06 17:24:59.059 [           main] INFO  .n.p.p.DefaultDynamicTransformerRegistry:67  -- added dynamic transformer classLoader: sun.misc.Launcher$AppClassLoader@18b4aac2, className: com.navercorp.pinpoint.testapp.controller.HttpClient4Controller, registry size: 3
08-06 17:24:59.059 [           main] INFO  .n.p.p.DefaultDynamicTransformerRegistry:67  -- added dynamic transformer classLoader: sun.misc.Launcher$AppClassLoader@18b4aac2, className: com.navercorp.pinpoint.testapp.controller.SimpleController, registry size: 4
08-06 17:24:59.059 [           main] INFO  .n.p.p.DefaultDynamicTransformerRegistry:67  -- added dynamic transformer classLoader: sun.misc.Launcher$AppClassLoader@18b4aac2, className: com.navercorp.pinpoint.testapp.controller.StressController, registry size: 5
2020-08-06 17:25:00.313 DEBUG 19236 --- [           main] .s.b.w.e.t.TomcatServletWebServerFactory : Code archive: C:\Users\Naver\.m2\repository\org\springframework\boot\spring-boot\2.3.2.RELEASE\spring-boot-2.3.2.RELEASE.jar
2020-08-06 17:25:00.313 DEBUG 19236 --- [           main] .s.b.w.e.t.TomcatServletWebServerFactory : Code archive: C:\Users\Naver\.m2\repository\org\springframework\boot\spring-boot\2.3.2.RELEASE\spring-boot-2.3.2.RELEASE.jar
2020-08-06 17:25:00.314 DEBUG 19236 --- [           main] .s.b.w.e.t.TomcatServletWebServerFactory : None of the document roots [src/main/webapp, public, static] point to a directory and will be ignored.
2020-08-06 17:25:00.347  INFO 19236 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 8082 (http)
2020-08-06 17:25:00.355  INFO 19236 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2020-08-06 17:25:00.356  INFO 19236 --- [           main] org.apache.catalina.core.StandardEngine  : Starting Servlet engine: [Apache Tomcat/9.0.37]
```

The last couple of lines here tell us that Spring has started. Spring Boot’s embedded Apache Tomcat server is acting as a webserver and is listening for requests on localhost port 8082. Open your browser and in the address bar at the top enter <http://localhost:8082>


# quickstart.Win.en


# quickstart.Win.ko


# Installation guide

To set up your very own Pinpoint instance you can either **download the build results** from our [**latest release**](https://github.com/pinpoint-apm/pinpoint/releases/latest), or manually build from your Git clone. In order to run your own Pinpoint instance, you will need to run below components:

* **HBase** (for storage)
* **Pinot** (for storage)
* **Pinpoint Collector** (deployed on a web container)
* **Pinpoint Web** (deployed on a web container)
* **Pinpoint Agent** (attached to a java application for profiling)

To try out a simple quickstart project, please refer to the [quick-start guide](https://pinpoint-apm.gitbook.io/pinpoint/getting-started/quickstart).

### Apple silicon(M1/M2) build failures

If an error `protoc-gen-grpc-java-1.49.2-osx-aarch_64.exe: program not found or is not executable` occurs in the Apple silicon Mac (M1/M2) development environment, it has to install Rosetta.

```
$> softwareupdate --install-rosetta --agree-to-license
```

## Quick Overview of Installation

1. HBase ([details](#1-hbase))
   1. Set up HBase cluster - [Apache HBase](http://hbase.apache.org)
   2. Create HBase Schemas - feed `/scripts/hbase-create.hbase` to hbase shell.
2. Pinot ([details](#2-pinot))
   1. Set up Pinot - [Apache Pinot](https://pinot.apache.org)
   2. Set up Kafka - [Apache Kafka](https://kafka.apache.org)
   3. Create Kafka topics and Pinot tables. Refer to the documentation for the features you are using.
      * [New Inspector](https://pinpoint-apm.gitbook.io/pinpoint/documents/new-inspector)
      * [System Metric](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric)
      * [URI Statistics](https://pinpoint-apm.gitbook.io/pinpoint/documents/uri_statistics)
      * [Error Analysis](https://pinpoint-apm.gitbook.io/pinpoint/documents/error_analysis)
3. Build Pinpoint (Optional)([details](#3-building-pinpoint)) - No need if you use the binaries.([here](https://github.com/pinpoint-apm/pinpoint/releases)). 4. Clone Pinpoint - `git clone $PINPOINT_GIT_REPOSITORY` 5. Set JAVA\_HOME environment variable to JDK 8 home directory. 6. Set JAVA\_8\_HOME environment variable to JDK 8 home directory. 7. Set JAVA\_11\_HOME environment variable to JDK 11 home directory. 8. Set JAVA\_17\_HOME environment variable to JDK 17 home directory. 9. Run `./mvnw clean install -DskipTests=true` (or `./mvnw.cmd` for Windows)
4. Pinpoint Collector ([details](#4-pinpoint-collector)) 1. Start *pinpoint-collector-boot-$VERSION.jar* with java -jar command.

   ```
    java -jar -Dpinpoint.zookeeper.address=localhost pinpoint-collector-boot-$VERSION.jar
   ```

   * It will start with default settings. To learn more about default values or how to override them, please see the details below.
   * Use [collector starter](#collector-starter) to connect to Pinot and Kafka
5. Pinpoint Web ([details](#5-pinpoint-web)) 1. Start *pinpoint-web-boot-$VERSION.jar* with java -jar command.

   ```
    java -jar -Dpinpoint.zookeeper.address=localhost pinpoint-web-boot-$VERSION.jar
   ```

   * It will start with default settings. To learn more about default values or how to override them, please see the details below.
   * Use [web starter](#web-starter) to connect to Pinot
6. Pinpoint Agent ([details](#6-pinpoint-agent))
   1. Extract/move *pinpoint-agent/* to a convenient location (`$AGENT_PATH`).
   2. Set `-javaagent:$AGENT_PATH/pinpoint-bootstrap-$VERSION.jar` JVM argument to attach the agent to a java application.
   3. Set `-Dpinpoint.agentId` and `-Dpinpoint.applicationName` command-line arguments.
      * If you're launching an agent in a containerized environment with dynamically changing *agent id*, consider adding `-Dpinpoint.container` command-line argument.
   4. Set `-Dprofiler.sampling.type=PERCENT` and `-Dprofiler.sampling.percent.sampling-rate=100` command-line arguments.
      * You can adjust the sampling rate with the above option.
   5. Launch java application with the options above.

## 1. HBase

Pinpoint uses HBase as its storage backend for the Collector and the Web.

To set up your own cluster, take a look at the [HBase website](http://hbase.apache.org) for instructions. The HBase compatibility table is given below:

Once you have HBase up and running, make sure the Collector and the Web are configured properly and are able to connect to HBase.

### Creating Schemas for HBase

There are 2 scripts available to create tables for Pinpoint: *hbase-create.hbase*, and *hbase-create-snappy.hbase*. Use *hbase-create-snappy.hbase* for snappy compression (requires [snappy](http://google.github.io/snappy/)), otherwise use *hbase-create.hbase* instead.

To run these scripts, feed them into the HBase shell like below:

`$HBASE_HOME/bin/hbase shell hbase-create.hbase`

See [here](https://github.com/pinpoint-apm/pinpoint/tree/master/hbase/scripts) for a complete list of scripts.

## 2. Pinot

Pinpoint uses Pinot for metric data storage, and Kafka is required for [Pinot stream ingestion](https://docs.pinot.apache.org/basics/data-import/pinot-stream-ingestion/import-from-apache-kafka)

Here are documents for Installing Pinot and Kafka

* Install Pinot following the instructions in [Pinot Getting Started guide](https://docs.pinot.apache.org/basics/getting-started)
  * Above guide provides instructions for running Pinot locally, in Docker, and in Kubernetes.
* Install Kafka by referring to [Kafka quickstart](https://kafka.apache.org/quickstart)

Once Pinot is up and running, ensure that the [collector starter](#collector-starter) and the [web starter](#web-starter) are properly configured and able to connect to Pinot.

### Creating Pinot tables

Please refer to the documentation to create Kafka topics and Pinot tables for Pinot-related feature.

The descriptions for the required Kafka topics and Pinot tables are provided in the following feature documents

* [New Inspector](https://pinpoint-apm.gitbook.io/pinpoint/documents/new-inspector)
* [System Metric](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric)
* [URI Statistics](https://pinpoint-apm.gitbook.io/pinpoint/documents/uri_statistics)
* [Error Analysis](https://pinpoint-apm.gitbook.io/pinpoint/documents/error_analysis)

## 3. Building Pinpoint

There are two options:

1. Download the build results from our [**latest release**](https://github.com/pinpoint-apm/pinpoint/releases/latest) and skip building process. **(Recommended)**
2. Build Pinpoint manually from the Git clone. **(Optional)**

   In order to do so, the following **requirements** must be met:

   * JDK 8 installed
   * JDK 11 installed
   * JDK 17 installed
   * JAVA\_HOME environment variable set to JDK 8 home directory.
   * JAVA\_8\_HOME environment variable set to JDK 8 home directory.
   * JAVA\_11\_HOME environment variable set to JDK 11 home directory.
   * JAVA\_17\_HOME environment variable set to JDK 17 home directory.

     Agent compatibility to Collector table:

     Once the above requirements are met, simply run the command below (you may need to add permission for **mvnw** so that it can be executed) :

     `./mvnw install -DskipTests=true`

     The default agent built this way will have log level set to DEBUG by default. If you're building an agent for release and need a higher log level, you can set maven profile to *release* when building :\
     `./mvnw install -Prelease -DskipTests=true`

     Note that having multibyte characters in maven local repository path, or any class paths may cause the build to fail.

     The guide will refer to the full path of the pinpoint home directory as `$PINPOINT_PATH`.

Regardless of your method, you should end up with the files and directories mentioned in the following sections.

## 4. Pinpoint Collector

You should have the following **executable jar** file.

*pinpoint-collector-boot-$VERSION.jar*

The path to this file should look like *$PINPOINT\_PATH/collector/target/deploy/pinpoint-collector-boot-$VERSION.jar* if you built it manually.

### Installation

Since Pinpoint Collector is packaged as an executable jar file, you can start Collector by running it directly.

e.g.) `java -jar -Dpinpoint.zookeeper.address=localhost pinpoint-collector-boot-$VERSION.jar`

### Configuration

There are 2 configuration files used for Pinpoint Collector: *pinpoint-collector-grpc.properties*, and *hbase.properties*.

* pinpoint-collector-grpc.properties - contains configurations for the grpc.
  * `collector.receiver.grpc.agent.port` (agent's *profiler.transport.grpc.agent.collector.port*, *profiler.transport.grpc.metadata.collector.port* - default: 9991/TCP)
  * `collector.receiver.grpc.stat.port` (agent's *profiler.transport.grpc.stat.collector.port* - default: 9992/TCP)
  * `collector.receiver.grpc.span.port` (agent's *profiler.transport.grpc.span.collector.port* - default: 9993/TCP)
* hbase.properties - contains configurations to connect to HBase.
  * `hbase.client.host` (default: localhost)
  * `hbase.client.port` (default: 2181)

You may take a look at the full list of default configurations here:

* [pinpoint-collector-grpc.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/collector/src/main/resources/profiles/local/pinpoint-collector-grpc.properties)
* [hbase.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/collector/src/main/resources/profiles/local/hbase.properties)

#### When Building Manually

You can modify default configuration values or add new profiles under `collector/src/main/resources/profiles/`.

#### When Using Released Binary **(Recommended)**

* You can override any configuration values with `-D` option. For example,
  * `java -jar -Dspring.profiles.active=release -Dpinpoint.zookeeper.address=localhost -Dhbase.client.port=1234 pinpoint-collector-boot-$VERSION.jar`
* To import a list of your customized configuration values from a file, you can use `--spring.config.additional-location` option. For example,
  * Create a file `./config/collector.properties`, and list the configuration values you want to override. >

    > spring.profiles.active=release
    >
    > pinpoint.zookeeper.address=localhost
    >
    > collector.receiver.grpc.agent.port=9999
    >
    > collector.receiver.stat.udp.receiveBufferSize=1234567
  * Execute with `java -jar pinpoint-collector-boot-$VERSION.jar --spring.config.additional-location=./config/collector.properties`
* To further explore how to use externalized configurations, refer to [Spring Boot Reference Document](https://docs.spring.io/spring-boot/docs/2.2.x/reference/html/spring-boot-features.html#boot-features-external-config-application-property-files).

### Profiles

Pinpoint Collector provides two profiles: [release](https://github.com/pinpoint-apm/pinpoint/tree/master/collector/src/main/resources/profiles/release) and [local](https://github.com/pinpoint-apm/pinpoint/tree/master/collector/src/main/resources/profiles/local) (default).

To specify which profile to use, configure `spring.profiles.active` value as described in the previous section.

#### Adding a custom profile

To add a custom profile, you need to rebuild `pinpoint-collector` module.

1. Add a new folder under `collector/src/main/resources/profiles` with a profile name.
2. Copy files from local or release profiles folder, and modify configuration values as needed.
3. To use the new profile, rebuild `pinpoint-collector` module and configure `spring.profiles.active` as described in the previous section.

When using released binary, you cannot add a custom profile. Instead, you can manage your configuration values in separate files and use them to override default values as described in the [previous section](#3-pinpoint-collector).

### Collector Starter

To utilize Pinot-related features, you need to execute with Pinpoint Collector starter.

Since the `collector-starter` is packaged as an executable jar file, you can start the `collector-starter` with the following command to override Zookeeper, Kafka and Pinot properties.

```
java -jar -Dspring.config.additional-location=collector-starter-application.yml pinpoint-collector-starter-boot-$VERSION.jar
```

* collector-starter-application.yml

```
pinpoint:
  zookeeper:
    address: localhost
  metric:
    kafka:
      bootstrap:
        servers: localhost:19092
spring:
  pinot-datasource:
    pinot:
      jdbc-url: jdbc:pinot://localhost:9000
      username: --username--
      password: --password--
```

## 5. Pinpoint Web

You should have the following **executable jar** file.

*pinpoint-web-boot-$VERSION.jar*

The path to this file should look like *$PINPOINT\_PATH/web/target/deploy/pinpoint-web-boot-$VERSION.jar* if you built it manually.

Pinpoint Web Supported Browsers:

* Chrome

### Installation

Since Pinpoint Web is packaged as an executable jar file, you can start Web by running it directly.

```
java -jar -Dpinpoint.zookeeper.address=localhost pinpoint-web-boot-$VERSION.jar
```

### Configuration

There are 2 configuration files used for Pinpoint Web: *pinpoint-web-root.properties*, and *hbase.properties*.

* hbase.properties - contains configurations to connect to HBase.
  * `hbase.client.host` (default: localhost)
  * `hbase.client.port` (default: 2181)

You may take a look at the default configuration files here

* [pinpoint-web-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/pinpoint-web-root.properties)
* [hbase.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/profiles/release/hbase.properties)
* [pinpoint-web.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/profiles/release/pinpoint-web.properties)

#### When Building Manually

You can modify default configuration values or add new profiles under `web/src/main/resources/profiles/`.

#### When Using Released Binary **(Recommended)**

* You can override any configuration values with `-D` option. For example,
  * `java -jar -Dspring.profiles.active=release -Dpinpoint.zookeeper.address=localhost -Dhbase.client.port=1234 pinpoint-web-boot-$VERSION.jar`
* To import a list of your customized configuration values from a file, you can use `--spring.config.additional-location` option. For example,
  * Create a file `./config/web.properties`, and list the configuration values you want to override. >

    > spring.profiles.active=release
    >
    > pinpoint.zookeeper.address=localhost
    >
    > cluster.zookeeper.sessiontimeout=10000
  * Execute with `java -jar pinpoint-web-boot-$VERSION.jar --spring.config.additional-location=./config/web.properties`
* To further explore how to use externalized configurations, refer to [Spring Boot Reference Document](https://docs.spring.io/spring-boot/docs/2.2.x/reference/html/spring-boot-features.html#boot-features-external-config-application-property-files).

### Profiles

Pinpoint Web provides two profiles: [release](https://github.com/pinpoint-apm/pinpoint/tree/master/web/src/main/resources/profiles/release) (default) and [local](https://github.com/pinpoint-apm/pinpoint/tree/master/web/src/main/resources/profiles/local).

To specify which profile to use, configure `spring.profiles.active` value as described in the previous section.

#### Adding a custom profile

To add a custom profile, you need to rebuild `pinpoint-web` module.

1. Add a new folder under `web/src/main/resources/profiles` with a profile name.
2. Copy files from local or release profiles folder, and modify configuration values as needed.
3. To use the new profile, rebuild `pinpoint-web` module and configure `spring.profiles.active` as described in the previous section.

When using released binary, you cannot add a custom profile. Instead, you can manage your configuration values in separate files and use them to override default values as described in the [previous section](#4-pinpoint-web).

### Web Starter

To utilize Pinot-related features, you need to execute with Pinpoint Web Starter.

Since the `web-starter` is packaged as an executable jar file, you can start the `web-starter` with the following command to override Zookeeper and Pinot properties.

```
java -jar -Dspring.config.additional-location=web-starter-application.yml pinpoint-web-starter-boot-$VERSION.jar
```

* web-starter-application.yml

```
pinpoint:
  zookeeper:
    address: localhost
spring:
  pinot-datasource:
    pinot:
      jdbc-url: jdbc:pinot://localhost:9000
      username: --username--
      password: --password--
```

## 6. Pinpoint Agent

If downloaded, unzip the Pinpoint Agent file. You should have a **pinpoint-agent** directory with the layout below :

```
pinpoint-agent
|-- boot
|   |-- pinpoint-annotations-$VERSION.jar
|   |-- pinpoint-bootstrap-core-$VERSION.jar
|   |-- pinpoint-bootstrap-java8-$VERSION.jar
|   |-- pinpoint-bootstrap-java9-$VERSION.jar
|   |-- pinpoint-commons-$VERSION.jar
|-- lib
|   |-- pinpoint-profiler-$VERSION.jar
|   |-- pinpoint-profiler-optional-$VERSION.jar
|   |-- pinpoint-rpc-$VERSION.jar
|   |-- pinpoint-thrift-$VERSION.jar
|   |-- ...
|-- plugin
|   |-- pinpoint-activemq-client-plugin-$VERSION.jar
|   |-- pinpoint-tomcat-plugin-$VERSION.jar
|   |-- ...
|-- profiles
|   |-- local
|   |   |-- pinpoint.config
|   |-- release
|       |-- pinpoint.config
|-- log4j2-agent.xml
|-- pinpoint-bootstrap-$VERSION.jar
|-- pinpoint-root.config
```

The path to this directory should look like *$PINPOINT\_PATH/agent/target/pinpoint-agent* if you built it manually.

You may move/extract the contents of **pinpoint-agent** directory to any location of your choice. The guide will refer to the full path of this directory as `$AGENT_PATH`.

> Note that you may change the agent's log level by modifying the *log4j.xml* located in the *profiles/$PROFILE/log4j.xml* directory above.

Agent compatibility to Collector table:

### Installation

Pinpoint Agent runs as a java agent attached to an application to be profiled (such as Tomcat).

To wire up the agent, pass *$AGENT\_PATH/pinpoint-bootstrap-$VERSION.jar* to the *-javaagent* JVM argument when running the application:

* `-javaagent:$AGENT_PATH/pinpoint-bootstrap-$VERSION.jar`

Additionally, Pinpoint Agent requires 2 command-line arguments in order to identify itself in the distributed system:

* `-Dpinpoint.agentId` - uniquely identifies the application instance in which the agent is running on
* `-Dpinpoint.applicationName` - groups a number of identical application instances as a single service

Note that *pinpoint.agentId* must be globally unique to identify an application instance, and all applications that share the same *pinpoint.applicationName* are treated as multiple instances of a single service.

* `-Dprofiler.sampling.type=PERCENT` - sampler type
* `-Dprofiler.sampling.percent.sampling-rate=100` - support from 100% to 0.01%

If you're launching the agent in a containerized environment, you might have set your *agent id* to be auto-generated every time the container is launched. With frequent deployment and auto-scaling, this will lead to the Web UI being cluttered with all the list of agents that were launched and destroyed previously. For such cases, you might want to add `-Dpinpoint.container` in addition to the 2 required command-line arguments above when launching the agent.

**Tomcat Example**

Add *-javaagent*, *-Dpinpoint.agentId*, *-Dpinpoint.applicationName* to *CATALINA\_OPTS* in the Tomcat startup script (*catalina.sh*).

```
CATALINA_OPTS="$CATALINA_OPTS -javaagent:$AGENT_PATH/pinpoint-bootstrap-$VERSION.jar"
CATALINA_OPTS="$CATALINA_OPTS -Dpinpoint.agentId=$AGENT_ID"
CATALINA_OPTS="$CATALINA_OPTS -Dpinpoint.applicationName=$APPLICATION_NAME"
```

Start up Tomcat to start profiling your web application.

Some application servers require additional configuration and/or may have caveats. Please take a look at the links below for further details.

* [JBoss](https://github.com/pinpoint-apm/pinpoint/tree/master/plugins/jboss#pinpoint-jboss-plugin-configuration)
* [Jetty](https://github.com/pinpoint-apm/pinpoint/blob/master/plugins/jetty/README.md)
* [Resin](https://github.com/pinpoint-apm/pinpoint/tree/master/plugins/resin#pinpoint-resin-plugin-configuration)

### Configuration

There are various configuration options for Pinpoint Agent available in *$AGENT\_PATH/pinpoint-root.config*.

Most of these options are self explanatory, but the most important configuration options you must check are **Collector ip address**, and the **TCP/UDP ports**. These values are required for the agent to establish connection to the *Collector* and function correctly.

Set these values appropriately in *pinpoint-root.config*:

**GRPC**

* `profiler.transport.grpc.collector.ip` (default: 127.0.0.1)
* `profiler.transport.grpc.agent.collector.port` (collector's *collector.receiver.grpc.agent.port* - default: 9991/TCP)
* `profiler.transport.grpc.metadata.collector.port` (collector's *collector.receiver.grpc.agent.port* - default: 9991/TCP)
* `profiler.transport.grpc.stat.collector.port` (collector's *collector.receiver.grpc.stat.port* - default: 9992/TCP)
* `profiler.transport.grpc.span.collector.port` (collector's *collector.receiver.grpc.span.port* - default: 9993/TCP)

You may take a look at the default *pinpoint-root.config* file [here](https://github.com/pinpoint-apm/pinpoint/blob/master/agent/src/main/resources/pinpoint-root.config) along with all the available configuration options.

### Profiles

Add `-Dkey=value` to Java System Properties

* $PINPOINT\_AGENT\_DIR/profiles/$PROFILE
  * `-Dpinpoint.profiler.profiles.active=release or local`
  * Modify `pinpoint.profiler.profiles.active=release` in $PINPOINT\_AGENT\_DIR/pinpoint-root.config
  * Default profile : `release`
* Custom Profile
  1. Create a custom profile in $PINPOINT\_AGENT\_HOME/profiles/MyProfile
     * Add pinpoint.config & log4j.xml
  2. Add `-Dpinpoint.profiler.profiles.active=MyProfile`
* Support external config
  * `-Dpinpoint.config=$MY_EXTERNAL_CONFIG_PATH`

## Miscellaneous

### HBase region servers hostname resolution

Please note that collector/web must be able to resolve the hostnames of HBase region servers. This is because HBase region servers are registered to ZooKeeper by their hostnames, so when the collector/web asks ZooKeeper for a list of region servers to connect to, it receives their hostnames. Please ensure that these hostnames are in your DNS server, or add these entries to the collector/web instances' *hosts* file.

### Routing Web requests to Agents

Starting from 1.5.0, Pinpoint can send requests from the Web to Agents directly via the Collector (and vice-versa). To make this possible, we use Zookeeper to co-ordinate the communication channels established between Agents and Collectors, and those between Collectors and Web instances. With this addition, real-time communication (for things like active thread count monitoring) is now possible.

We typically use the Zookeeper instance provided by the HBase backend so no additional Zookeeper configuration is required. Related configuration options are shown below.

* **Collector** - *pinpoint-collector.properties*
  * `cluster.enable`
  * `cluster.zookeeper.address`
  * `cluster.zookeeper.sessiontimeout`
  * `cluster.listen.ip`
  * `cluster.listen.port`
* **Web** - *pinpoint-web.properties*
  * `cluster.enable`
  * `cluster.web.tcp.port`
  * `cluster.zookeeper.address`
  * `cluster.zookeeper.sessiontimeout`
  * `cluster.zookeeper.retry.interval`
  * `cluster.connect.address`


# Install with Docker

We've create docker files to support docker.\
Installing Pinpoint with these docker files will take approximately 10min. to check out the features of Pinpoint.

Visit [Official Pinpoint-Docker repository](https://github.com/pinpoint-apm/pinpoint-docker) for more information.


# TrobleShooting(Network)

## Checking network configuration

We provide a simple tool that can check your network configurations.\
This tool checks the network status between Pinpoint-Agent and Pinpoint-Collector

## Testing with binary release

If you have downloaded the build results from our [**latest release**](https://github.com/pinpoint-apm/pinpoint/releases/latest).

1. Start your collector server
2. With any terminal that you are using, go to *script* folder which is under *pinpoint-agent-VERSION.tar.gz* package that you have downloaded.

```
> pwd
/Users/user/Downloads/pinpoint-agent-1.7.2-SNAPSHOT/script
```

and run *networktest.sh* shell script

```
> sh networktest.sh
```

You will see some CLASSPATH and configuration you have made in the *pinpoint.config* file as below

```
CLASSPATH=./tools/pinpoint-tools-1.7.2-SNAPSHOT.jar
...Remainder Omitted...
2018-04-10 17:36:30 [INFO ](com.navercorp.pinpoint.bootstrap.config.DefaultProfilerConfig) profiler.enable=true
2018-04-10 17:36:30 [INFO ](com.navercorp.pinpoint.bootstrap.config.DefaultProfilerConfig) profiler.instrument.engine=ASM
2018-04-10 17:36:30 [INFO ](com.navercorp.pinpoint.bootstrap.config.DefaultProfilerConfig) profiler.instrument.matcher.enable=true
...Remainder Omitted...
```

And after that, you will see the results. (In this case, collector server was started locally) If you receive all six SUCCESSes as below, then you are all set and ready to go.

```
UDP-STAT:// localhost
    => 127.0.0.1:9995 [SUCCESS]
    => 0:0:0:0:0:0:0:1:9995 [SUCCESS]

UDP-SPAN:// localhost
    => 127.0.0.1:9996 [SUCCESS]
    => 0:0:0:0:0:0:0:1:9996 [SUCCESS]

TCP:// localhost
    => 127.0.0.1:9994 [SUCCESS]
    => 0:0:0:0:0:0:0:1:9994 [SUCCESS]
```

## Testing with source code

The idea is basically the same.

1. Start your collector server
2. Pass the *path* of the pinpoint.config file as a *program argument* and run ***NetworkAvailabilityChecker*** class.
3. (only for under v1.7.2)For the few who gets JNI error while running. Please remove `<scope>provided</scope>` line from pom.xml under *tools* module and try again

Results should be same as shown above.

> If you face error for v1.7.3 take a look at this [issue](https://github.com/pinpoint-apm/pinpoint/issues/4668)


# Plugin Developer Guide

You can write Pinpoint profiler plugins to extend profiling target coverage. It is highly advisable to look into the trace data recorded by pinpoint plugins before jumping into plugin development.

* There is a [fast auto pinpoint agent plugin generate tool](https://github.com/bbossgroups/pinpoint-plugin-generate) from a 3rd party for creating a simple plug-in, if you'd like to check out.

## I. Trace Data

In Pinpoint, a transaction consists of a group of `Spans`. Each `Span` represents a trace of a single logical node where the transaction has gone through.

To aid in visualization, let's suppose that there is a system like below. The *FrontEnd* server receives requests from users, then sends request to the *BackEnd* server, which queries a DB. Among these nodes, let's assume only the *FrontEnd* and *BackEnd* servers are profiled by the Pinpoint Agent.

![trace](https://user-images.githubusercontent.com/10043788/133535491-adafcd89-c04e-49af-9ad7-f7746bb9c95c.PNG)

When a request arrives at the *FrontEnd* server, Pinpoint Agent generates a new transaction id and creates a `Span` with it. To handle the request, the *FrontEnd* server then invokes the *BackEnd* server. At this point, Pinpoint Agent injects the transaction id (plus a few other values for propagation) into the invocation message. When the *BackEnd* server receives this message, it extracts the transaction id (and the other values) from the message and creates a new `Span` with them. Resulting, all `Spans` in a single transaction share the same transaction id.

A `Span` records important method invocations and their related data(arguments, return value, etc) before encapsulating them as `SpanEvents` in a call stack like representation. The `Span` itself and each of its `SpanEvents` represents a method invocation.

`Span` and `SpanEvent` have many fields, but most of them are handled internally by Pinpoint Agent and most plugin developers won't need to worry about them. But the fields and data that must be handled by plugin developers will be listed throughout this guide.

## II. Pinpoint Plugin Structure

Pinpoint plugin consists of *type-provider.yml* and `ProfilerPlugin` implementations. *type-provider.yml* defines the `ServiceTypes` and `AnnotationKeys` that will be provided by the plugin, and provides them to Pinpoint Agent, Web and Collector. `ProfilerPlugin` implementations are used by Pinpoint Agent to transform target classes to record trace data.

Plugins are deployed as jar files. These jar files are packaged under the *plugin* directory for the agent, while the collector and web have them deployed under *WEB-INF/lib*. On start up, Pinpoint Agent, Collector, and Web iterates through each of these plugins; parses *type-provider.yml*, and loads `ProfilerPlugin` implementations using `ServiceLoader` from the following locations:

* META-INF/pinpoint/type-provider.yml
* META-INF/services/com.navercorp.pinpoint.bootstrap.plugin.ProfilerPlugin

Here is a [template plugin project](https://github.com/pinpoint-apm/pinpoint-plugin-template) you can use to start creating your own plugin.

### 1. type-provider.yml

*type-provider.yml* defines the `ServiceTypes` and `AnnotationKeys` that will be used by the plugin and provided to the agent, collector and web; the format of which is outlined below.

```yaml
serviceTypes:
    - code: <short>
      name: <String>
      desc: <String>   # May be omitted, defaulting to the same value as name.
      property:        # May be omitted, all properties defaulting to false.
          terminal: <boolean>               # May be omitted, defaulting to false.
          queue: <boolean>                  # May be omitted, defaulting to false.
          recordStatistics: <boolean>       # May be omitted, defaulting to false.
          includeDestinationId: <boolean>   # May be omitted, defaulting to false.
          alias: <boolean>                  # May be omitted, defaulting to false.          
      matcher:         # May be omitted
          type: <String>   # Any one of 'args', 'exact', 'none'
          code: <int>      # Annotation key code - required only if type is 'exact'

annotationKeys:
    - code: <int>
      name: <String>
      property:        # May be omitted, all properties defaulting to false.
          viewInRecordSet: <boolean>
```

`ServiceType` and `AnnotationKey` defined here are instantiated when the agent loads, and can be obtained using `ServiceTypeProvider` and `AnnotationKeyProvider` like below.

```java
// ServiceType
ServiceType serviceType = ServiceTypeProvider.getByCode(1000);    // by ServiceType code
ServiceType serviceType = ServiceTypeProvider.getByName("NAME");  // by ServiceType name
// AnnotationKey
AnnotationKey annotationKey = AnnotationKeyProvider.getByCode("100");
```

#### 1.1 ServiceType

Every `Span` and `SpanEvent` contains a `ServiceType`. The `ServiceType` represents which library the traced method belongs to, as well as how the `Span` and `SpanEvent` should be handled.

The table below shows the `ServiceType`'s properties.

| property   | description                                                |
| ---------- | ---------------------------------------------------------- |
| name       | name of the `ServiceType`. Must be unique                  |
| code       | short type code value of the `ServiceType`. Must be unique |
| desc       | description                                                |
| properties | properties                                                 |

`ServiceType` code must use a value from its appropriate category. The table below shows these categories and their range of codes.

| category     | range        |
| ------------ | ------------ |
| Internal Use | 0 \~ 999     |
| Server       | 1000 \~ 1999 |
| DB Client    | 2000 \~ 2999 |
| Cache Client | 8000 \~ 8999 |
| RPC Client   | 9000 \~ 9999 |
| Others       | 5000 \~ 7999 |

`ServiceType` code must be unique. Therefore, if you are writing a plugin that will be shared publicly, **you must** contact Pinpoint dev. team to get a `ServiceType` code assigned. If your plugin is for private use, you may freely pick a value for `ServiceType` code from the table below.

| category     | range        |
| ------------ | ------------ |
| Server       | 1900 \~ 1999 |
| DB client    | 2900 \~ 2999 |
| Cache client | 8900 \~ 8999 |
| RPC client   | 9900 \~ 9999 |
| Others       | 7500 \~ 7999 |

`ServiceTypes` can have the following properties.

| property                 | description                                                                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TERMINAL                 | This `Span` or `SpanEvent` invokes a remote node but the target node is not traceable with Pinpoint                                                           |
| QUEUE                    | This `Span` or `SpanEvent` consumes/produces a message from/to a message queue.                                                                               |
| INCLUDE\_DESTINATION\_ID | This `Span` or `SpanEvent` records a `destination id` and remote server is not a traceable type.                                                              |
| RECORD\_STATISTICS       | Pinpoint Collector should collect execution time statistics of this `Span` or `SpanEvent`                                                                     |
| ALIAS                    | The service may or may not have Pinpoint-Agent attached at the following service but regardlessly have knowledge what will follow. (Ex. Elasticsearch client) |

#### 1.2 AnnotationKey

You can annotate spans and span events with more information. An **Annotation** is a key-value pair where the key is an `AnnotationKey` type and the value is a primitive type, String or a byte\[]. There are pre-defined `AnnotationKeys` for commonly used annotation types, but you can define your own keys in *type-provider.yml* if these are not enough.

| property   | description                                                 |
| ---------- | ----------------------------------------------------------- |
| name       | Name of the `AnnotationKey`                                 |
| code       | int type code value of the `AnnotationKey`. Must be unique. |
| properties | properties                                                  |

If you are writing a plugin for public use, and are looking to add a new `AnnotationKey`, you must contact the Pinpoint dev. team to get an `AnnotationKey` code assigned. If your plugin is for private use, you may pick a value between 900 to 999 safely to use as `AnnotationKey` code.

The table below shows the `AnnotationKey` properties.

| property              | description                                    |
| --------------------- | ---------------------------------------------- |
| VIEW\_IN\_RECORD\_SET | Show this annotation in transaction call tree. |
| ERROR\_API\_METADATA  | This property is not for plugins.              |

#### Example

You can find *type-provider.yml* sample [here](https://github.com/pinpoint-apm/pinpoint-plugin-sample/blob/master/plugins/sample/src/main/resources/META-INF/pinpoint/type-provider.yml).

You may also define and attach an `AnnotationKeyMatcher` with a `ServiceType` (`matcher` element in the sample *type-provider* code above). If you attach an `AnnotationKeyMatcher` this way, matching annotations will be displayed as representative annotation when the `ServiceType`'s `Span` or `SpanEvent` is displayed in the transaction call tree.

### 2. ProfilerPlugin

`ProfilerPlugin` modifies target library classes to collect trace data.

`ProfilerPlugin` works in the order of following steps:

1. Pinpoint Agent is started when the JVM starts.
2. Pinpoint Agent loads all plugins under `plugin` directory.
3. Pinpoint Agent invokes `ProfilerPlugin.setup(ProfilerPluginSetupContext)` for each loaded plugin.
4. In the `setup` method, the plugin registers a `TransformerCallback` to all classes that are going to be transformed.
5. Target application starts.
6. Every time a class is loaded, Pinpoint Agent looks for the `TransformerCallback` registered to the class.
7. If a `TransformerCallback` is registered, the Agent invokes it's `doInTransform` method.
8. `TransformerCallback` modifies the target class' byte code. (e.g. add interceptors, add fields, etc.)
9. The modified byte code is returned to the JVM, and the class is loaded with the returned byte code.
10. Application continues running.
11. When a modified method is invoked, the injected interceptor's `before` and `after` methods are invoked.
12. The interceptor records the trace data.

The most important points to consider when writing a plugin are 1) figuring out which methods are interesting enough to warrant tracing, and 2) injecting interceptors to actually trace these methods. These interceptors are used to extract, store, and pass trace data around before they are sent off to the Collector. Interceptors may even cooperate with each other, sharing context between them. Plugins may also aid in tracing by adding getters or even custom fields to the target class so that the interceptors may access them during execution. [Pinpoint plugin sample](https://github.com/pinpoint-apm/pinpoint-plugin-sample) shows you how the `TransformerCallback` modifies classes and what the injected interceptors do to trace a method.

We will now describe what interceptors must do to trace different kinds of methods.

#### 2.1 Plain method

*Plain method* refers to anything that is not a top-level method of a node, or is not related to remote or asynchronous invocation. [Sample 2](https://github.com/pinpoint-apm/pinpoint-plugin-sample/tree/master/plugins/sample/src/main/java/com/navercorp/pinpoint/plugin/sample/_02_Injecting_Custom_Interceptor) shows you how to trace these plain methods.

#### 2.2 Top level method of a node

*Top level method of a node* is a method in which its interceptor begins a new trace in a node. These methods are typically acceptors for RPCs, and the trace is recorded as a `Span` with `ServiceType` categorized as a server.

How the `Span` is recorded depends on whether the transaction has already begun at any previous nodes.

**2.2.1 New transaction**

If the current node is the first one that is recording the transaction, you must issue a new transaction id and record it. `TraceContext.newTraceObject()` will handle this task automatically, so you will simply need to invoke it.

**2.2.2 Continue Transaction**

If the request came from another node traced by a Pinpoint Agent, then the transaction will already have a transaction id issued; and you will have to record the data below to the `Span`. (Most of these data are sent from the previous node, usually packed in the request message)

| name                  | description                           |
| --------------------- | ------------------------------------- |
| transactionId         | Transaction ID                        |
| parentSpanId          | Span ID of the previous node          |
| parentApplicationName | Application name of the previous node |
| parentApplicationType | Application type of the previous node |
| rpc                   | Procedure name (Optional)             |
| endPoint              | Server(current node) address          |
| remoteAddr            | Client address                        |
| acceptorHost          | Server address that the client used   |

Pinpoint finds caller-callee relation between nodes using *acceptorHost*. In most cases, *acceptorHost* is identical to *endPoint*. However, the address which client sent the request to may sometimes be different from the address the server received the request (proxy). To handle such cases, you have to record the actual address the client used to send the request to as *acceptorHost*. Normally, the client plugin will have added this address into the request message along with the transaction data.

Moreover, you must also use the span id issued and sent by the previous node.

Sometimes, the previous node marks the transaction to not be traced. In this case, you must not trace the transaction.

As you can see, the client plugin must be able pass trace data to the server plugin, and how to do this is protocol dependent.

You can find an example of top-level method server interceptor [here](https://github.com/pinpoint-apm/pinpoint-plugin-sample/tree/master/plugins/sample/src/main/java/com/navercorp/pinpoint/plugin/sample/_14_RPC_Server).

#### 2.3 Methods invoking a remote node

An interceptor of a method that invokes a remote node has to record the following data:

| name          | description                                                                           |
| ------------- | ------------------------------------------------------------------------------------- |
| endPoint      | Target server address                                                                 |
| destinationId | Logical name of the target                                                            |
| rpc           | Invoking target procedure name (optional)                                             |
| nextSpanId    | Span id that will be used by next node's span (If next node is traceable by Pinpoint) |

Whether or not the next node is traceable by Pinpoint affects how the interceptor is implemented. The term "traceable" here is about possibility. For example, a HTTP client's next node is a HTTP server. Pinpoint does not trace all HTTP servers, but it is possible to trace them (and there already are HTTP server plugins). In this case, the HTTP client's next node is traceable. On the other hand, MySQL JDBC's next node, a MySQL database server, is not traceable.

**2.3.1 If the next node is traceable**

If the next node is traceable, the interceptor must propagate the following data to the next node. How to pass them is protocol dependent, and in worst cases may be impossible to pass them at all.

| name                  | description                                                                                   |
| --------------------- | --------------------------------------------------------------------------------------------- |
| transactionId         | Transaction ID                                                                                |
| parentApplicationName | Application name of current node                                                              |
| parentApplicationType | Application type of current node                                                              |
| parentSpanId          | Span id of trace at current node                                                              |
| nextSpanId            | Span id that will be used by the next node's span (same value with nextSpanId of above table) |

Pinpoint finds out caller-callee relation by matching *destinationId* of client trace and *acceptorHost* of server trace. Therefore the client plugin has to record *destinationId* and the server plugin has to record *acceptorHost* with the same value. If server cannot acquire the value by itself, client plugin has to pass it to server.

The interceptor's recorded `ServiceType` must be from the RPC client category.

You can find an example for these interceptors [here](https://github.com/pinpoint-apm/pinpoint-plugin-sample/tree/master/plugins/sample/src/main/java/com/navercorp/pinpoint/plugin/sample/_13_RPC_Client).

**2.3.2 If the next node is not traceable**

If the next node is not traceable, your `ServiceType` must have the `TERMINAL` property.

If you want to record the *destinationId*, it must also have the `INCLUDE_DESTINATION_ID` property. If you record *destinationId*, server map will show a node per destinationId even if they have same *endPoint*.

Also, the `ServiceType` must be a DB client or Cache client category. Note that you do not need to concern yourself about the terms "DB" or "Cache", as any plugin tracing a client library with non-traceable target server may use them. The only difference between "DB" and "Cache" is the time range of the response time histogram ("Cache" having smaller intervals for the histogram).

#### 2.4 Asynchronous task

Trace objects are bound to the thread that first created them via **ThreadLocal** and whenever the execution crosses a thread boundary, trace objects are *lost* to the new thread. Therefore, in order to trace tasks across thread boundaries, you must take care of passing the current trace context over to the new thread. This is done by injecting an **AsyncContext** into an object shared by both the invocation thread and the execution thread.\
The invocation thread creates an **AsyncContext** from the current trace, and injects it into an object that will be passed over to the execution thread. The execution thread then retrieves the **AsyncContext** from the object, creates a new trace out of it and binds it to it's own **ThreadLocal**.\
You must therefore create interceptors for two methods : i) one that initiates the task (invocation thread), and ii) the other that actually handles the task (execution thread).

The initiating method's interceptor has to issue an **AsyncContext** and pass it to the handling method. How to pass this value depends on the target library. In worst cases, you may not be able to pass it at all.

The handling method's interceptor must then continue the trace using the propagated **AsyncContext** and bind it to it's own thread. However, it is very strongly recommended that you simply extend the **AsyncContextSpanEventSimpleAroundInterceptor** so that you do not have to handle this manually.

Keep in mind that since the shared object must be able have **AsyncContext** injected into it, you have to add a field using `AsyncContextAccessor` during it's class transformation. You can find an example for tracing asynchronous tasks [here](https://github.com/pinpoint-apm/pinpoint-plugin-sample/tree/master/plugins/sample/src/main/java/com/navercorp/pinpoint/plugin/sample/_12_Asynchronous_Trace).

#### 2.5 Case Study: HTTP

HTTP client is an example of *a method invoking a remote node* (client), and HTTP server is an example of a *top level method of a node* (server). As mentioned before, client plugins must have a way to pass transaction data to server plugins to continue the trace. Note that the implementation is protocol dependent, and [HttpMethodBaseExecuteMethodInterceptor](https://github.com/pinpoint-apm/pinpoint/blob/master/plugins/httpclient3/src/main/java/com/navercorp/pinpoint/plugin/httpclient3/interceptor/HttpMethodBaseExecuteMethodInterceptor.java) of [HttpClient3 plugin](https://github.com/pinpoint-apm/pinpoint/tree/master/plugins/httpclient3) and [StandardHostValveInvokeInterceptor](https://github.com/pinpoint-apm/pinpoint/blob/master/plugins/tomcat/src/main/java/com/navercorp/pinpoint/plugin/tomcat/interceptor/StandardHostValveInvokeInterceptor.java) of [Tomcat plugin](https://github.com/pinpoint-apm/pinpoint/tree/master/plugins/tomcat) show a working example of this for HTTP:

1. Pass transaction data as HTTP headers. You can find header names [here](https://github.com/pinpoint-apm/pinpoint/blob/master/bootstrap-core/src/main/java/com/navercorp/pinpoint/bootstrap/context/Header.java)
2. Client plugin records `IP:PORT` of the server as `destinationId`.
3. Client plugin passes `destinationId` value to server as `Header.HTTP_HOST` header.
4. Server plugin records `Header.HTTP_HOST` header value as `acceptorHost`.

One more thing you have to remember is that all the clients and servers using the same protocol must pass the transaction data in the same way to ensure compatibility. So if you are writing a plugin of some other HTTP client or server, your plugin has to record and pass transaction data as described above.

### 3. Plugin Integration Test

You can run plugin integration tests (`mvn integration-test`) with [PinointPluginTestSuite](https://github.com/pinpoint-apm/pinpoint/blob/master/test/src/main/java/com/navercorp/pinpoint/test/plugin/PinpointPluginTestSuite.java), which is a *JUnit Runner*. It downloads all the required dependencies from maven repositories and launches a new JVM with the Pinpoint Agent and the aforementioned dependencies. The JUnit tests are executed in this JVM.

To run the plugin integration test, it needs a complete agent distribution - which is why integration tests are in the *plugin-sample-agent* module and why they are run in **integration-test phase**.

For the actual integration test, you will want to first invoke the method you are tracing, and then use [PluginTestVerifier](https://github.com/pinpoint-apm/pinpoint/blob/master/bootstrap-core/src/main/java/com/navercorp/pinpoint/bootstrap/plugin/test/PluginTestVerifier.java) to check if the trace data is correctly recorded.

#### 3.1 Test Dependency

`PinointPluginTestSuite` doesn't use the project's dependencies (configured in pom.xml). It uses the dependencies that are listed by `@Dependency` annotation. This way, you may test multiple versions of the target library using the same test class.

Dependencies are declared as following. You may specify versions or version ranges for a dependency library.

```
@Dependency({"some.group:some-artifact:1.0", "another.group:another-artifact:2.1-RELEASE"})
@Dependency({"some.group:some-artifact:[1.0,)"})
@Dependency({"some.group:some-artifact:[1.0,1.9]"})
@Dependency({"some.group:some-artifact:[1.0],[2.1],[3.2])"})
```

`PinointPluginTestSuite` by default searches the local repository and maven central repository. You may also add your own repositories by using the `@Repository` annotation.

#### 3.2 Jvm Version

You can specify the JVM version for a test using `@JvmVersion`. If `@JvmVersion` is not present, JVM at `java.home property` will be used.

#### 3.3 Application Test

`PinpointPluginTestSuite` is not for applications that has to be launched by its own main class. You can extend [AbstractPinpointPluginTestSuite](https://github.com/pinpoint-apm/pinpoint/blob/master/test/src/main/java/com/navercorp/pinpoint/test/plugin/AbstractPinpointPluginTestSuite.java) and related types to test such applications.

### 4. Adding Images

If you're developing a plugin for applications, you need to add images so the server map can render the corresponding node. The plugin jar itself cannot provide these image files and for now, you will have to add the image files to the web module manually.

First, put the PNG files to following directories:

* web/src/main/webapp/images/icons (25x25)
* web/src/main/webapp/images/servermap (80x40)

Then, add `ServiceType` name and the image file name to `htIcons` in *web/src/main/webapp/components/server-map2/jquery.ServerMap2.js*.


# Setting Alarm

[English](#alarm) | [한국어](#alarm-1)

## Alarm

Application's status is periodically checked and alarm is triggered if certain pre-configured conditions (rules) are satisfied.

pinpoint-batch server checks every 3 minutes based on the last 5 minutes of data. And if the conditions are satisfied, it sends sms/email/webhook to the users listed in the user group.

> If an email/sms/webhook is sent everytime when the threshold is exceeded, even after the recipients are aware of the event they might get the same alarms continuously which we thought might be unneccessary. Therefore we decided to gradually increase the transmission frequency for alarms.\
> ex) If an alarm occurs continuously, transmission frequency is increased by a factor of two. 3 min -> 6min -> 12min -> 24min
>
> **NOTICE!**
>
> * These logics were part of pinpoint-web server and ran in the background until v2.2.0 From v2.2.1 it is separated into pinpoint-batch server. Since the batch logic(code) in pinpoint-web will be deprecated in the future, we advise you to transfer the execution of batch to pinpoint-batch server.
> * Webhook function is newly added in v2.1.1, and has some changes in v2.3.1. In both versions, MYSQL table needs to be changed. Please check the notice on these changes in [2.1.1](#2.1-configuration-and-implementation-in-pinpoint-batch)

### 1. User Guide

1\) Configuration menu

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-0ea93f5e306fc6e4958749507fdf8155578552d8%2FConfiguration%20page.gif?alt=media)

2\) Register users

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-f622485ac439ce9675079f95fcdb75b5e04420e4%2Fadd%20user.gif?alt=media)

3\) Create user groups

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-4ea91f0d20fecae25061c23e7d92d5f49b6252e3%2FAdd%20usergroup.gif?alt=media)

4\) (Optional) Add webhooks

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-b44f12715e808e3b0bd8f641b7769251a6285735%2Fadd%20webhook.gif?alt=media)

5\) Set alarm rules

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-63548e3c2432358b70ae68a911d25e8bb00bd4da%2Fadd%20alarm.gif?alt=media)

**Alarm Rules**

```
SLOW COUNT
   Triggered when the number of slow requests sent to the application exceeds the configured threshold.

SLOW RATE
   Triggered when the percentage(%) of slow requests sent to the application exceeds the configured threshold.

ERROR COUNT
   Triggered when the number of failed requests sent to the application exceeds the configured threshold.

ERROR RATE
   Triggered when the percentage(%) of failed requests sent to the application exceeds the configured threshold.

TOTAL COUNT
   Triggered when the number of all requests sent to the application exceeds the configured threshold.

APDEX SCORE
   Triggered when the Apdex score goes down below the configured threshold.

SLOW COUNT TO CALLEE
   Triggered when the number of slow requests sent by the application exceeds the configured threshold.
   You must specify the domain or the address(ip, port) in the configuration UI's "Note..." box 
   ex) www.naver.com, 127.0.0.1:8080

SLOW RATE TO CALLEE
   Triggered when the percentage(%) of slow requests sent by the application exceeds the configured threshold.
   You must specify the domain or the address(ip, port) in the configuration UI's "Note..." box 
   ex) www.naver.com, 127.0.0.1:8080

ERROR COUNT TO CALLEE
   Triggered when the number of failed requests sent by the application exceeds the configured threshold.
   You must specify the domain or the address(ip, port) in the configuration UI's "Note..." box 
   ex) www.naver.com, 127.0.0.1:8080

ERROR RATE TO CALLEE
   Triggered when the percentage(%) of failed requests sent by the application exceeds the configured threshold.
   You must specify the domain or the address(ip, port) in the configuration UI's "Note..." box 
   ex) www.naver.com, 127.0.0.1:8080

TOTAL COUNT TO CALLEE
   Triggered when the number of all requests sent by the application exceeds the configured threshold.
   You must specify the domain or the address(ip, port) in the configuration UI's "Note..." box 
   ex) www.naver.com, 127.0.0.1:8080

HEAP USAGE RATE
   Triggered when the application's heap usage(%) exceeds the configured threshold.

JVM CPU USAGE RATE
   Triggered when the application's CPU usage(%) detected by JVM exceeds the configured threshold.

SYSTEM CPU USAGE RATE
   Triggered when the application's CPU usage(%) detected by system exceeds the configured threshold.

DATASOURCE CONNECTION USAGE RATE
   Triggered when the application's DataSource connection usage(%) exceeds the configured threshold.

FILE DESCRIPTOR COUNT
   Triggered when the number of open file descriptors exceeds the configured threshold.
```

### 2. Configuration & Implementation

Alarms generated by Pinpoint can be configured to be sent over email, sms and webhook.

Sending alarms over email is simple - you will simply need to configure the property file. Sending alarms over sms requires some implementation. Read on to find out how to do this. The alarm using webhook requires a separate webhook receiver service. You should implement the webhook receiver service - which is not provided by Pinpoint, or You can use [the sample project](https://github.com/doll6777/slack-receiver).

Few modifications are required in pinpoint-batch and pinpoint-web to use the alarm feature. Add some implementations and settings in pinpoint-batch. Configure Pinpoint-web for user to set an alarm settings.

### 2.1 Configuration & Implementation in pinpoint-batch

#### 2.1.1) Email configuration, sms and webhook implementation

**A. Email alarm service**

To use the mailing feature, you need to configure the SMTP server information and information to be included in the email in the [batch-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/batch-root.properties) file.

```
pinpoint.url= #pinpoint-web server url
alarm.mail.server.url= #smtp server address
alarm.mail.server.port= #smtp server port
alarm.mail.server.username= #username for smtp server authentication
alarm.mail.server.password= #password for smtp server authentication
alarm.mail.sender.address= #sender's email address

ex)
pinpoint.url=http://pinpoint.com
alarm.mail.server.url=stmp.server.com
alarm.mail.server.port=587
alarm.mail.server.username=pinpoint
alarm.mail.server.password=pinpoint
alarm.mail.sender.address=pinpoint_operator@pinpoint.com
```

The class that sends emails is already registered as Spring bean in [applicationContext-batch-sender.xml](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/applicationContext-batch-sender.xml).

```
    <bean id="mailSender" class="com.navercorp.pinpoint.batch.alarm.SpringSmtpMailSender">
        <constructor-arg ref="batchConfiguration"/>
        <constructor-arg ref="userGroupService"/>
        <constructor-arg ref="javaMailSenderImpl"/>
    </bean>

    <bean id="javaMailSenderImpl" class="org.springframework.mail.javamail.JavaMailSenderImpl">
        <property name="host" value="${alarm.mail.server.url:}" />
        <property name="port" value="${alarm.mail.server.port:587}" />
        <property name="username" value="${alarm.mail.server.username:}" />
        <property name="password" value="${alarm.mail.server.password:}" />
        <property name="javaMailProperties">
            <props>
                <prop key="mail.transport.protocol">${alarm.mail.transport.protocol:}</prop>
                <prop key="mail.smtp.port">${alarm.mail.smtp.port:}</prop>
                <prop key="mail.smtp.from">${alarm.mail.sender.address:}</prop>
                <prop key="mail.smtp.auth">${alarm.mail.smtp.auth:false}</prop>
                <prop key="mail.smtp.starttls.enable">${alarm.mail.smtp.starttls.enable:false}</prop>
                <prop key="mail.smtp.starttls.required">${alarm.mail.smtp.starttls.required:false}</prop>
                <prop key="mail.debug">${alarm.mail.debug:false}</prop>
            </props>
        </property>
    </bean>
```

If you would like to implement your own mail sender, simply replace the `SpringSmtpMailSender`, `JavaMailSenderImpl` beans above with your own implementation that implements `com.navercorp.pinpoint.web.alarm.MailSender` interface.

```
public interface MailSender {
   void sendEmail(AlarmChecker checker, int sequenceCount);
}
```

**B. Sms alarm service**

To send alarms over sms, you will need to implement your own sms sender by implementing `com.navercorp.pinpoint.batch.alarm.SmsSender` interface. If there is no `SmsSender` implementation, then alarms will not be sent over sms.

```
public interface SmsSender {
    public void sendSms(AlarmChecker checker, int sequenceCount);
}
```

**C. Webhook alarm service**

Webhook alarm service is a feature that can transmit Pinpoint's alarm message through Webhook API.

The webhook receiver service that receives the webhook message should be implemented by yourself, or use [a sample project](https://github.com/doll6777/slack-receiver) provided (in this case Slack).

The alarm messages(refer to as payloads) sent to webhook receiver have the different schema depending on the Alarm Checker type. You can see the payload schemas in [3.Others - The Specification of webhook payloads and the examples](##3.Others).

To enable the webhook alarm service, You need to configure *pinpoint.modules.web.webhook* in [application.yml](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/application.yml) file. Webhook receiver urls can be configured in web UI after configuring the web module to enable webhook as described in the following section.

```
# webhook config
pinpoint.modules.web:
    webhook: true
```

> **NOTICE!**
>
> \*\*\* \*\*MYSQL table ALTER for migrating to Pinpoint v2.1.1 \*\*\*\*\*
>
> As the webhook alarm service is newly added in Pinpoint 2.1.1, you should add column `webhook_send` in table `alarm_rule` to your MYSQL server used for previous versions of Pinpoint.
>
> ```
> ALTER TABLE alarm_rule ADD COLUMN webhook_send CHAR(1) DEFAULT NULL;
> ```
>
> **\*\*\* MYSQL table CREATE for migrating to Pinpoint v2.3.1 \*\*\***
>
> Different webhook destinations can be specified to different alarms and new tables are added for this. Create table `webhook` and `webhook_send` as below in your MYSQL server used for previous versions of Pinpoint.
>
> ```
> CREATE TABLE `webhook` (
>   `webhook_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
>   `alias` VARCHAR(45) NULL,
>   `url` VARCHAR(45) NOT NULL,
>   `application_id` VARCHAR(45) NULL,
>   `service_name` VARCHAR(45) NULL,
>   PRIMARY KEY (`webhook_id`)
> );
>
> CREATE TABLE `webhook_send` (
>   `webhook_send_info_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
>   `webhook_id` INT UNSIGNED NOT NULL,
>   `rule_id` INT UNSIGNED NOT NULL,
>   PRIMARY KEY (`webhook_send_info_id`)
> );
> ```
>
> Of course if you are migrating from versions lower than v2.1.1 to v2.3.1, all the changes above need to be applied.

WebhookSenderImpl class, which sends the webhook, is already implemented for you and is added as webhookSender bean in [applicationContext-batch-sender.xml](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/applicationContext-batch-sender.xml) of Pinpoint-batch.

```markup
   <bean id="webHookSender" class="com.navercorp.pinpoint.web.alarm.WebhookSenderImpl">
        <constructor-arg ref="batchConfiguration"/>
        <constructor-arg ref="userServiceImpl"/>
        <constructor-arg ref="restTemplate" />
    </bean>
```

#### 2.1.2) Configuring MYSQL

**step 1**

Prepare MYSQL Instance to persist the alarm service metadata.

**step 2**

Set up a MYSQL server and configure connection information in [jdbc-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/jdbc-root.properties) file.

```
jdbc.driverClassName=com.mysql.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:13306/pinpoint
jdbc.username=admin
jdbc.password=admin
```

**step 3**

Create tables for the alarm service. Use below DDL files.

* [CreateTableStatement-mysql.sql](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/sql/CreateTableStatement-mysql.sql)
* [SpringBatchJobRepositorySchema-mysql.sql](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/sql/SpringBatchJobRepositorySchema-mysql.sql)

#### 2.1.3) How to execute pinpoint-batch

The pinpoint-batch project is based on spring boot and can be executed with the following command. When building is successfully finished, the executable file is placed under the target/deploy folder of the pinpoint-batch.

```
java -Dspring.profiles.active=XXXX -jar pinpoint-batch-VERSION.jar 

ex) java -Dspring.profiles.active=local -jar pinpoint-batch-2.1.1.jar
```

### 2.2 How to configure pinpoint-web

#### 2.2.1) Configuring MYSQL Server IP

In order to persist user alarm settings, set the mysql connection information in [jdbc-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/jdbc-root.properties) file in pinpoint-web.

```
jdbc.driverClassName=com.mysql.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:13306/pinpoint
jdbc.username=admin
jdbc.password=admin
```

#### 2.2.2) Enabling Webhook Alarm Service

Set *pinpoint.modules.web.webhook* in [pinpoint-web-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/application.yml) as *true* for user to configure the webhook alarm in *Alarm* menu.

```
# webhook config
pinpoint.modules.web:
    webhook: true
```

As you enable the webhook alarm service, you can set the webhook as alarm type and specify the target webhook.

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-d40bb10eb1e4c87b0b49c40df0da30ec191e496f%2Falarm_select_webhook.png?alt=media)

### 3. Others

### 3.1 Configuration, Execution, Performance.

**1) You may change the batch execution period by modifying the cron expression in** [***applicationContext-batch-schedule.xml***](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/applicationContext-batch-schedule.xml) **file**

```
<task:scheduled-tasks scheduler="scheduler">
    <task:scheduled ref="batchJobLauncher" method="alarmJob" cron="0 0/3 * * * *" />
</task:scheduled-tasks>
```

**2) Ways to improve alarm batch performance**

The alarm batch was designed to run concurrently. If there are a lot of applications using alarms, you may increase the size of the executor's thread pool by modifying `pool-size` in [*applicationContext-alarmJob.xml*](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/job/applicationContext-alarmJob.xml) file.

Note that increasing this value will result in higher resource usage.

```
<task:executor id="poolTaskExecutorForPartition" pool-size="1" />
```

If there are a lot of alarms registered to each application, you may set the `alarmStep` registered in [*applicationContext-alarmJob.xml*](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/job/applicationContext-alarmJob.xml) file to run concurrently.

```
<step id="alarmStep" xmlns="http://www.springframework.org/schema/batch">
    <tasklet task-executor="poolTaskExecutorForStep" throttle-limit="3">
        <chunk reader="reader" processor="processor" writer="writer" commit-interval="1"/>
    </tasklet>
</step>
<task:executor id="poolTaskExecutorForStep" pool-size="10" />
```

**3) Use quickstart's web**

Pinpoint Web uses Mysql to persist users, user groups, and alarm configurations, but our Quickstart example uses MockDAO to reduce memory usage. If you want to use Mysql with Quickstart, please refer to Pinpoint Web's [applicationContext-dao-config.xml](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/applicationContext-dao-config.xml) and [jdbc.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/jdbc.properties).

### 3.2 Details on Webhook

#### 3.2.1) webhook receiver sample project

[Slack-Receiver](https://github.com/doll6777/slack-receiver) is an example project for the webhook receiver. The project can receive alarms from Pinpoint through webhook and send the message to Slack. If you want more details, see [the project repository](https://github.com/doll6777/slack-receiver).

#### 3.2.2) The Specification of webhook payloads and the examples

**The Schemas of webhook payloads**

Key

| Name          | Type      | Description                                                  | Nullable |
| ------------- | --------- | ------------------------------------------------------------ | -------- |
| pinpointUrl   | String    | Pinpoint-web server URL                                      | O        |
| batchEnv      | String    | Batch server environment variable                            | X        |
| applicationId | String    | Alarm target application Id                                  | X        |
| serviceType   | String    | Alarm target application service type                        | X        |
| userGroup     | UserGroup | The UserGroup in the user group page                         | X        |
| checker       | Checker   | The checker info in the alarm setting page                   | X        |
| unit          | String    | The unit of detected value by checker                        | O        |
| threshold     | Integer   | The threshold of value detected by checker during a set time | X        |
| notes         | String    | The notes in the alarm setting page                          | O        |
| sequenceCount | Integer   | The number of alarm occurence                                | X        |

UserGroup

| Name             | Type          | Description                              | Nullable |
| ---------------- | ------------- | ---------------------------------------- | -------- |
| userGroupId      | String        | The user group id in the user group page | X        |
| userGroupMembers | UserMember\[] | Members Info of a specific user group    | X        |

Checker

| Name          | Type                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Nullable |
| ------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| name          | String                      | The name of checker in the alarm setting page                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | X        |
| type          | String                      | <p>The type of checker abstracted by value detected by checker<br>"LongValueAlarmChecker" type is the abstracted checker type of “Slow Count”, “Slow Rate”, “Error Count”, “Error Rate”, “Total Count”, “Slow Count To Callee”, “Slow Rate To Callee”, “Error Count To Callee”, “Error Rate To Callee”, “Total Count to Callee”.<br>"LongValueAgentChecker" type is the abstracted checker type of "Heap Usage Rate", "Jvm Cpu Usage Rate", "System Cpu Usage Rate", "File Descriptor Count".<br>"BooleanValueAgentChecker" type is the abstracted checker type of "Deadlock or not".<br>"DataSourceAlarmListValueAgentChecker" type is the abstracted checker type of "DataSource Connection Usage Rate".</p> | X        |
| detectedValue | Integer or DetectedAgent\[] | <p>The value detected by checker<br>If “type” is “LongValueAlarmChecker”, “detectedValue” is Integer type.<br>If "type" is not "LongValueAlarmChecker", "detectedValue" is DetectedAgents\[] type.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | X        |

UserMember

| Name             | Type   | Description               | Nullable |
| ---------------- | ------ | ------------------------- | -------- |
| id               | String | Member id                 | X        |
| name             | String | Member name               | X        |
| email            | String | Member email              | O        |
| department       | String | Member department         | O        |
| phoneNumber      | String | Member phone number       | O        |
| phoneCountryCode | String | Member phone country code | O        |

DetectedAgent

| Name       | Type                                                  | Description                                                                                                                                                                                                                                                                                   | Nullable |
| ---------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| agentId    | String                                                | Agent id detected by checker                                                                                                                                                                                                                                                                  | X        |
| agentValue | <p>Integer or<br>Boolean or<br>DataSourceAlarm\[]</p> | <p>The value of Agent detected by checker<br>If “type” is “LongValueAgentChecker”, “agentValue” is Integer type.<br>If “type” is “BooleanValueAgentChecker”,“agentValue” is Boolean type.<br>If “type” is “DataSourceAlarmListValueAgentChecker”, “agentValue” is DataSourceAlarm\[] type</p> | X        |

DataSourceAlarm

| Name            | Type    | Description                                   | Nullable |
| --------------- | ------- | --------------------------------------------- | -------- |
| databaseName    | String  | The database name connected to application    | X        |
| connectionValue | Integer | The application's DataSource connection usage | X        |

**The Examples of the webhook Payload**

LongValueAlarmChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "TOTAL COUNT",
   "type": "LongValueAlarmChecker",
   "detectedValue": 33
 },
 "unit": "",
 "threshold": 15,
 "notes": "Note Example",
 "sequenceCount": 4
}
```

LongValueAgentChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "HEAP USAGE RATE",
   "type": "LongValueAgentChecker",
   "detectedValue": [
     {
       "agentId": "test-agent",
       "agentValue": 8
     }
   ]
 },
 "unit": "%",
 "threshold": 5,
 "notes": "Note Example",
 "sequenceCount": 4
}
```

BooleanValueAgentChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "DEADLOCK OCCURRENCE",
   "type": "BooleanValueAgentChecker",
   "detectedValue": [
     {
       "agentId": "test-agent",
       "agentValue": true
     }
   ]
 },
 "unit": "BOOLEAN",
 "threshold": 1,
 "notes": "Note Example",
 "sequenceCount": 4
}
```

DataSourceAlarmListValueAgentChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "DATASOURCE CONNECTION USAGE RATE",
   "type": "DataSourceAlarmListValueAgentChecker",
   "detectedValue": [
     {
       "agentId": "test-agent",
       "agentValue": [
                 {
                     "databaseName": "test",
                     "connectionValue": 32
                 }
        ]
     }
   ]
 },
 "unit": "%",
 "threshold": 16,
 "notes": "Note Example",
 "sequenceCount": 4
}
```

## Alarm

Pinpoint는 application 상태를 주기적으로 체크하여 application 상태의 수치가 임계치를 초과할 경우 사용자에게 알람을 전송하는 기능을 제공한다.

Application 상태 값이 사용자가 설정한 임계치를 초과하는지 판단하는 batch는 [pinpoint-batch](https://github.com/pinpoint-apm/pinpoint/tree/master/batch)에서 동작 한다. Alarm batch는 기본적으로 3분에 한번씩 동작이 된다. 최근 5분동안의 데이터를 수집해서 alarm 조건을 만족하면 user group에 속한 user 들에게 sms/email/webhook message를 전송한다.

> 연속적으로 알람 조건이 임계치를 초과한 경우에 매번 sms/email/webhook를 전송하지 않는다.\
> 알람 조건이 만족할때마다 매번 sms/email/webhook이 전송되는것은 오히려 방해가 된다고 생각하기 때문이다. 그래서 연속해서 알람이 발생할 경우 sms/email/webhook 전송 주기가 점증적으로 증가된다.\
> 예) 알람이 연속해서 발생할 경우, 전송 주기는 3분 -> 6분 -> 12분 -> 24분 으로 증가한다.
>
> ***
>
> **알림**
>
> * Batch는 pinpoint 2.2.0 버전까지는 [pinpoint-web](https://github.com/pinpoint-apm/pinpoint/tree/master/web)에서 동작되었지만, 2.2.1 버전 부터는 batch가 [pinpoint-batch](https://github.com/pinpoint-apm/pinpoint/tree/master/batch)에서 동작되도록 로직을 분리했다.\*\* \*\*앞으로 pinpoint-web의 batch로직은 제거를 할 예정이므로, pinpoint-web에서 batch를 동작시키는 경우 pinpoint-batch에서 batch를 실행하도록 구성하는것을 추천한다.
> * 웹훅 기능은 v2.1.1에 신규로 추가되었으며 v2.3.1에 기능이 개선되었다. 두 버전 모두에서 MYSQL 테이블 변경이 있으므로, 해당 버전 이전에서 업그레이드할 경우, [2.1.1 항목](#2.1-pinpoint-batch)에서 관련 변경 사항을 확인 후 적용해야 한다.

### 1. Alarm 기능 사용 방법

1\) 설정 화면으로 이동

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-0ea93f5e306fc6e4958749507fdf8155578552d8%2FConfiguration%20page.gif?alt=media)

2\) user를 등록

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-f622485ac439ce9675079f95fcdb75b5e04420e4%2Fadd%20user.gif?alt=media)

3\) userGroup을 생성

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-4ea91f0d20fecae25061c23e7d92d5f49b6252e3%2FAdd%20usergroup.gif?alt=media)

4\) (선택사항) webhook 등

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-b44f12715e808e3b0bd8f641b7769251a6285735%2Fadd%20webhook.gif?alt=media)

5\) alarm rule을 등록

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-63548e3c2432358b70ae68a911d25e8bb00bd4da%2Fadd%20alarm.gif?alt=media)

alarm rule에 대한 설명은 아래를 참고하시오.

```
SLOW COUNT
   외부에서 application을 호출한 요청 중에 외부서버로 응답을 늦게 준 요청의 개수가 임계치를 초과한 경우 알람이 전송된다.

SLOW RATE
   외부에서 application을 호출한 요청 중에 외부서버로 응답을 늦게 준 요청의 비율(%)이 임계치를 초과한 경우 알람이 전송된다.

ERROR COUNT
   외부에서 application을 호출한 요청 중에 에러가 발생한 요청의 개수가 임계치를 초과한 경우 알람이 전송된다.

ERROR RATE
   외부에서 application을 호출한 요청 중에 에러가 발생한 요청의 비율(%)이 임계치를 초과한 경우 알람이 전송된다.

TOTAL COUNT
   외부에서 application을 호출한 요청 개수가 임계치를 초과한 경우 알람이 전송된다.
   
APDEX SCORE
   Apdex 점수가 임계치 이하로 내려간 경우 알람이 전송된다.

SLOW COUNT TO CALLEE
   application 내에서 외부서버를 호출한 요청 중 slow 호출의 개수가 임계치를 초과한 경우 알람이 전송된다.
   설정 화면의 Note 항목에 외부서버의 도메인 이나 주소(ip, port)를 입력해야 합니다. ex) naver.com, 127.0.0.1:8080

SLOW RATE TO CALLEE
   application 내에서 외부서버를 호출한 요청 중 slow 호출의 비율(%)이 임계치를 초과한 경우 알람이 전송된다.
   설정 화면의 Note 항목에 외부서버의 도메인 이나 주소(ip, port)를 입력해야 합니다. ex) naver.com, 127.0.0.1:8080

ERROR COUNT TO CALLEE
   application 내에서 외부서버를 호출한 요청 중 error 가 발생한 호출의 개수가 임계치를 초과한 경우 알람이 전송된다.
   설정 화면의 Note 항목에 외부서버의 도메인 이나 주소(ip, port)를 입력해야 합니다. ex) naver.com, 127.0.0.1:8080

ERROR RATE TO CALLEE
   application 내에서 외부서버를 호출한 요청 중 error 가 발생한 호출의 비율이 임계치를 초과한 경우 알람이 전송된다.
   설정 화면의 Note 항목에 외부서버의 도메인 이나 주소(ip, port)를 입력해야 합니다. ex) naver.com, 127.0.0.1:8080

TOTAL COUNT TO CALLEE
   application 내에서 외부서버를 호출한 요청의 개수가 임계치를 초과한 경우 알람이 전송된다.
   설정 화면의 Note 항목에 외부서버의 도메인 이나 주소(ip, port)를 입력해야 합니다. ex) naver.com, 127.0.0.1:8080

HEAP USAGE RATE
   heap의 사용률이 임계치를 초과한 경우 알람이 전송된다.

JVM CPU USAGE RATE
   applicaiton의 CPU 사용률이 임계치를 초과한 경우 알람이 전송된다.

SYSTEM CPU USAGE RATE
   서버의 CPU 사용률이 임계치를 초과한 경우 알람이 전송된다.

DATASOURCE CONNECTION USAGE RATE
   applicaiton의 DataSource내의 Connection 사용률이 임계치를 초과한 경우 알람이 전송된다.

FILE DESCRIPTOR COUNT
   열려있는 File Descriptor 개수가 임계치를 초가한 경우 알람이 전송된다.
```

### 2. 설정 및 구현 방법

알람을 전송하는 방법은 총 3가지로서, email, sms와 webhook으로 알람을 전송할 수 있다.

email 전송은 설정만 추가하면 기능을 사용할 수 있고, sms 전송을 하기 위해서는 직접 전송 로직을 구현해야 한다.\
webhook 전송은 webhook message를 받는 webhook receiver 서비스를 별도로 준비해야한다. webhook receiver 서비스는 [샘플 프로젝트](https://github.com/doll6777/slack-receiver)를 사용하거나 직접 구현해야 한다.

alarm 기능을 사용하려면 pinpoint-batch와 pinpoint-web를 수정해야한다. pinpoint-batch에는 alarm batch 동작을 위해서 설정 및 구현체를 추가해야 한다. pinpoint-web에는 사용자가 알람을 추가할 수 있도록 설정해야한다.

### 2.1 pinpoint-batch 설정 및 구현 방법

#### 2.1.1) email/sms/webhook 전송 설정 및 구현

**A. email 전송**

email 전송 기능을 사용하기 위해서 [batch-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/batch-root.properties)파일에 smtp 서버 정보와 email에 포함될 정보들을 설정해야 한다.

```
pinpoint.url= #pinpoint-web 서버의 url 
alarm.mail.server.url= #smtp 서버 주소  
alarm.mail.server.port= #smtp 서버 port 
alarm.mail.server.username= #smtp 인증을 위한 userName
alarm.mail.server.password= #smtp 인증을 위한 password
alarm.mail.sender.address= # 송신자 email

ex)
pinpoint.url=http://pinpoint.com
alarm.mail.server.url=stmp.server.com
alarm.mail.server.port=587
alarm.mail.server.username=pinpoint
alarm.mail.server.password=pinpoint
alarm.mail.sender.address=pinpoint_operator@pinpoint.com
```

참고로 [applicationContext-batch-sender.xml](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/applicationContext-batch-sender.xml) 파일에 email을 전송하는 class가 bean으로 등록 되어있다.

```
    <bean id="mailSender" class="com.navercorp.pinpoint.batch.alarm.SpringSmtpMailSender">
        <constructor-arg ref="batchConfiguration"/>
        <constructor-arg ref="userGroupService"/>
        <constructor-arg ref="javaMailSenderImpl"/>
    </bean>

    <bean id="javaMailSenderImpl" class="org.springframework.mail.javamail.JavaMailSenderImpl">
        <property name="host" value="${alarm.mail.server.url:}" />
        <property name="port" value="${alarm.mail.server.port:587}" />
        <property name="username" value="${alarm.mail.server.username:}" />
        <property name="password" value="${alarm.mail.server.password:}" />
        <property name="javaMailProperties">
            <props>
                <prop key="mail.transport.protocol">${alarm.mail.transport.protocol:}</prop>
                <prop key="mail.smtp.port">${alarm.mail.smtp.port:}</prop>
                <prop key="mail.smtp.from">${alarm.mail.sender.address:}</prop>
                <prop key="mail.smtp.auth">${alarm.mail.smtp.auth:false}</prop>
                <prop key="mail.smtp.starttls.enable">${alarm.mail.smtp.starttls.enable:false}</prop>
                <prop key="mail.smtp.starttls.required">${alarm.mail.smtp.starttls.required:false}</prop>
                <prop key="mail.debug">${alarm.mail.debug:false}</prop>
            </props>
        </property>
    </bean>
```

만약 email 전송 로직을 직접 구현하고 싶다면 위의 SpringSmtpMailSender, JavaMailSenderImpl bean 선언을 제거하고 com.navercorp.pinpoint.web.alarm.MailSender interface를 구현해서 bean을 등록하면 된다.

```
public interface MailSender {
   void sendEmail(AlarmChecker checker, int sequenceCount);
}
```

**B. sms 전송**

sms 전송 기능을 사용 하려면 com.navercorp.pinpoint.batch.alarm.SmsSender interface를 구현하고 bean으로 등록해야 한다. SmsSender 구현 class가 없는 경우 sms는 전송되지 않는다.

```
public interface SmsSender {
    public void sendSms(AlarmChecker checker, int sequenceCount);
}
```

**C. webhook 전송**

Webhook 전송 기능은 Pinpoint의 Alarm message를 Webhook API로 전송 할 수 있는 기능이다.

webhook message를 전송받는 webhook receiver 서비스는 [**샘플 프로젝트**](https://github.com/doll6777/slack-receiver)**를 사용하거나 직접 구현해야 한다.** Webhook Receiver 서버에 전송되는 Alarm message(이하 payload)는 Alarm Checker 타입에 따라 스키마가 다르다. Checker 타입에 따른 payload 스키마는 [**3.기타** - webhook 페이로드 스키마 명세, 예시](##3.기타)에서 설명한다.

webhook 기능을 활성화 하기위해서, [pinpoint.modules.web.webhook](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/application.yml) 파일에 Webhook 전송 여부(pinpoint.modules.web.webhook)를 설정한다. Receiver 서버 정보의 경우 [2.2 pinpoint-web 설정 방법](#2.2-pinpoint-web) 같이 web 설정을 마친 후, UI를 통해 추가할 수 있다.

```
# webhook config
pinpoint.modules.web:
    webhook: true
```

> **알림**\
> \&#xNAN;**\*\*\* Pinpoint v2.1.1로 업그레이드를 하기 위한 MYSQL 테이블 변경 \*\*\***
>
> webhook 기능이 추가되면서 mysql 테이블 스키마가 수정되었기 때문에, Pinpoint 2.1.1 미만 버전에서 2.1.1 버전 이상으로 업그레이드한 경우 Mysql의 'alarm\_rule' 테이블에 'webhook\_send' 컬럼을 추가해야 다.
>
> ```
> ALTER TABLE alarm_rule ADD COLUMN webhook_send CHAR(1) DEFAULT NULL;
> ```
>
> **\*\*\* Pinpoint v2.3.1로 업그레이드를 하기 위한 MYSQL 테이블 추가 생성 \*\*\***
>
> Pinpoint v2.1.1에서는 하나의 webhook receiver로만 알람을 보낼 수 있었는데, Pinpoint v2.3.1에서부터 각 알람마다 서로 다른 webhook destination을 설정할 수 있다. 이를 위해서 두 개의 새로운 MYSQL 테이블이 추가되었으며, 아래와 같이 ‘webhook’과 ‘webhook\_send’테이블을 추가해야 한다.
>
> ```
> CREATE TABLE `webhook` (
>   `webhook_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
>   `alias` VARCHAR(45) NULL,
>   `url` VARCHAR(45) NOT NULL,
>   `application_id` VARCHAR(45) NULL,
>   `service_name` VARCHAR(45) NULL,
>   PRIMARY KEY (`webhook_id`)
> );
>
> CREATE TABLE `webhook_send` (
>   `webhook_send_info_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
>   `webhook_id` INT UNSIGNED NOT NULL,
>   `rule_id` INT UNSIGNED NOT NULL,
>   PRIMARY KEY (`webhook_send_info_id`)
> );
> ```
>
> 물론 v2.3.1 이전 버전에서 바로 v2.3.1로 업그레이드하는 경우, 위의 모든 변경사항을 적용해야한다.

참고로 Webhook을 전송하는 클래스(WebhookSenderImpl)는 Pinpoint에서 이미 제공하고 있으며, webHookSender bean으 Pinpoint-batch의 [applicationContext-batch-sender.xml](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/applicationContext-batch-sender.xml) 파일에 등록 되어있다.

```markup
<bean id="webHookSender" class="com.navercorp.pinpoint.web.alarm.WebhookSenderImpl">
    <constructor-arg ref="batchConfiguration"/>
    <constructor-arg ref="userServiceImpl"/>
    <constructor-arg ref="restTemplate" />
</bean>
```

#### 2.1.2) MYSQL 서버 IP 주소 설정 & table 생성

**step 1**

알람에 관련된 데이터를 저장하기 위해 Mysql 서버를 준비한다.

**step 2**

mysql 접근을 위해서 pinpoint-batch의 [jdbc-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/jdbc-root.properties) 파일에 접속 정보를 설정한다.

```
jdbc.driverClassName=com.mysql.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:13306/pinpoint
jdbc.username=admin
jdbc.password=admin
```

**step 3**

mysql에 Alarm 기능에 필요한 table을 생성한다. table 스키마는 아래 파일을 참조한다.

* [*CreateTableStatement-mysql.sql*](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/sql/CreateTableStatement-mysql.sql)
* [*SpringBatchJobRepositorySchema-mysql.sql*](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/sql/SpringBatchJobRepositorySchema-mysql.sql)

#### 2.1.3) pinpoint-batch 실행 방법

pinpoint-batch 프로젝트는 spring boot기반으로 되어있고 아래와 같은 명령어로 실행하면 된다. 빌드후 실행파일은 pinpoint-batch 모듈의 target/deploy 폴더 하위에서 확인할 수 있다.

```
java -Dspring.profiles.active=XXXX -jar pinpoint-batch-VERSION.jar 

ex) java -Dspring.profiles.active=local -jar pinpoint-batch-2.1.1.jar
```

### 2.2 pinpoint-web 설정 방법

#### 2.2.1) MYSQL 서버 IP 주소 설정

사용자 알람 설정을 저장하기 위해서 pinpoint-web의 [jdbc-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/jdbc-root.properties) 파일에 mysql 접속 정보를 설정한다.

```
jdbc.driverClassName=com.mysql.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:13306/pinpoint
jdbc.username=admin
jdbc.password=admin
```

#### 2.2.2) webhook 기능 활성화

사용자가 알람 설정에 webhook 기능을 적용할수 있도록 [pinpoint-web-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/application.yml) 파일에 webhook 기능을 활성화한다.

```
# webhook config
pinpoint.modules.web:
    webhook: true
```

webhook 기능을 활성화하면, 아래 그림처럼 알람 설정 화면에서 webhook을 알람 타입으로 선택할 수 있다.

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-d40bb10eb1e4c87b0b49c40df0da30ec191e496f%2Falarm_select_webhook.png?alt=media)

### 3. 기타

### 3.1 설정, 실행, 성능

**1) Batch의 동작 주기를 조정하고 싶다면** [***applicationContext-batch-schedule.xml***](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/applicationContext-batch-schedule.xml) **파일의 cron expression을 수정하면 된다.**

```
<task:scheduled-tasks scheduler="scheduler">
    <task:scheduled ref="batchJobLauncher" method="alarmJob" cron="0 0/3 * * * *" />
</task:scheduled-tasks>
```

**2) Alarm batch 성능을 높이는 방법은 다음과 같다.**

Alarm batch 성능 튜닝을 위해서 병렬로 동작이 가능하도록 구현을 해놨다. 그래서 아래에서 언급된 조건에 해당하는 경우 설정 값을 조정한다면 성능을 향상 시킬 수 있다. 단, 병렬성을 높이면 리소스 사용률이 높아지는 것은 감안해야 한다.

Alarm이 등록된 application의 개수가 많다면 [*applicationContext-alarmJob.xml*](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/job/applicationContext-alarmJob.xml) 파일의 poolTaskExecutorForPartition의 pool size를 늘려주면 된다.

```
<task:executor id="poolTaskExecutorForPartition" pool-size="1" />
```

Application 각각마다 등록된 alarm의 개수가 많다면 [*applicationContext-alarmJob.xml*](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/job/applicationContext-alarmJob.xml) 파일에 선언된 alarmStep이 병렬로 동작되도록 설정하면 된다.

```
<step id="alarmStep" xmlns="http://www.springframework.org/schema/batch">
    <tasklet task-executor="poolTaskExecutorForStep" throttle-limit="3">
        <chunk reader="reader" processor="processor" writer="writer" commit-interval="1"/>
    </tasklet>
</step>
<task:executor id="poolTaskExecutorForStep" pool-size="10" />
```

**3) Quickstart web을 사용한다면.**

Quickstart pinpoint web은 mockDAO를 사용하기 때문에 추가한 알람 설정들이 저장되지 않는다. Mysql과 quickstart를 연동해서 사용하려면 다음의 설정들을 참고해서 수정 후 기능을 사용해야한다: [applicationContext-dao-config.xml](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/applicationContext-dao-config.xml), [jdbc.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/jdbc.properties).

### 3.2 webhook 상세

#### 3.2.1 **Webhook receiver 예제 프로젝트**

[Slack-Receiver](https://github.com/doll6777/slack-receiver) 는 Webhook Receiver의 예제 프로젝트이다. 이 프로젝트는 Pinpoint의 webhook의 알람을 받아서 Slack으로 메시지를 전송할 수 있는 스프링 부트로 구현된 서비스이다. 이 프로젝트의 자세한 사항은 [해당 GitHub 저장소](https://github.com/doll6777/slack-receiver) 를 참고하면 된다.

#### 3.2.2 webhook 페이로드 스키마 및 예시

**페이로드 스키마**

Key

| Name          | Type      | Description              | Nullable |
| ------------- | --------- | ------------------------ | -------- |
| pinpointUrl   | String    | Pinpoint-web의 서버 URL 주소  | O        |
| batchEnv      | String    | Batch 서버의 환경 변수          | X        |
| applicationId | String    | 타겟 애플리케이션 ID             | X        |
| serviceType   | String    | 타겟 애플리케이션 서비스 타입         | X        |
| userGroup     | UserGroup | 유저 그룹 페이지의 유저 그룹         | X        |
| checker       | Checker   | alarm 설정 페이지의 checker 정보 | X        |
| unit          | String    | checker가 감지한 값의 단위       | O        |
| threshold     | Integer   | 설정된 시간동안 체커가 감지한 값의 임계치  | X        |
| notes         | String    | 알람 설정 페이지의 notes         | O        |
| sequenceCount | Integer   | 알람 발생 횟수                 | X        |

UserGroup

| Name             | Type          | Description         | Nullable |
| ---------------- | ------------- | ------------------- | -------- |
| userGroupId      | String        | 유저 그룹 페이지의 유저 그룹 ID | X        |
| userGroupMembers | UserMember\[] | 특정 유저 그룹의 멤버 정보     | X        |

Checker

| Name          | Type                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Nullable |
| ------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| name          | String                      | 알람 설정 페이지의 checker 이름                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | X        |
| type          | String                      | <p>체커가 감지한 값의 추상 타입, 다음 중 하나에 해당됨<br>"LongValueAlarmChecker" 타입은 "Slow Count", “Slow Count”, “Slow Rate”, “Error Count”, “Error Rate”, “Total Count”, “Slow Count To Callee”, “Slow Rate To Callee”, “Error Count To Callee”, “Error Rate To Callee”, “Total Count to Callee”의 추상 타입에 속한다.<br>"LongValueAgentChecker" 타입은 "Heap Usage Rate", "Jvm Cpu Usage Rate", "System Cpu Usage Rate", "File Descriptor Count"의 추상타입이다.<br>"BooleanValueAgentChecker" 타입은 "Deadlock or not"의 추상 타입이다.<br>"DataSourceAlarmListValueAgentChecker" 타입은 "DataSource Connection Usage Rate"의 추상타입이다.</p> | X        |
| detectedValue | Integer or DetectedAgent\[] | <p>Checker가 감지한 값<br>“LongValueAlarmChecker”, “detectedValue” 타입은 Integer 타입이다.<br>"LongValueAlarmChecker", "detectedValue"이 아닌 타입은 DetectedAgents\[] 타입 이다.</p>                                                                                                                                                                                                                                                                                                                                                                                                                         | X        |

UserMember

| Name             | Type   | Description            | Nullable |
| ---------------- | ------ | ---------------------- | -------- |
| id               | String | 멤버의 id                 | X        |
| name             | String | 멤버의 name               | X        |
| email            | String | 멤버의 email              | O        |
| department       | String | 멤버의 department         | O        |
| phoneNumber      | String | 멤버의 phone number       | O        |
| phoneCountryCode | String | 멤버의 phone country code | O        |

DetectedAgent

| Name       | Type                                                  | Description                                                                                                                                                                                                                   | Nullable |
| ---------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| agentId    | String                                                | Checker가 감지한 에이전트 ID                                                                                                                                                                                                          | X        |
| agentValue | <p>Integer or<br>Boolean or<br>DataSourceAlarm\[]</p> | <p>체커가 감지한 에이전트의 값<br>“LongValueAgentChecker”, “agentValue” 은 Integer 타입이다.<br>“BooleanValueAgentChecker”,“agentValue” 은 Boolean 타입이다..<br>“DataSourceAlarmListValueAgentChecker”, “agentValue”은 DataSourceAlarm\[] 타입이다.</p> | X        |

DataSourceAlarm

| Name            | Type    | Description                              | Nullable |
| --------------- | ------- | ---------------------------------------- | -------- |
| databaseName    | String  | 애플리케이션에 접속한 데이터베이스 이름                    | X        |
| connectionValue | Integer | Applicaiton의 DataSource내의 Connection 사용률 | X        |

**webhook Payload 예제**

LongValueAlarmChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "TOTAL COUNT",
   "type": "LongValueAlarmChecker",
   "detectedValue": 33
 },
 "unit": "",
 "threshold": 15,
 "notes": "Note Example",
 "sequenceCount": 4
}
```

LongValueAgentChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "HEAP USAGE RATE",
   "type": "LongValueAgentChecker",
   "detectedValue": [
     {
       "agentId": "test-agent",
       "agentValue": 8
     }
   ]
 },
 "unit": "%",
 "threshold": 5,
 "notes": "Note Example",
 "sequenceCount": 4
}
```

BooleanValueAgentChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "DEADLOCK OCCURRENCE",
   "type": "BooleanValueAgentChecker",
   "detectedValue": [
     {
       "agentId": "test-agent",
       "agentValue": true
     }
   ]
 },
 "unit": "BOOLEAN",
 "threshold": 1,
 "notes": "Note Example",
 "sequenceCount": 4
}
```

DataSourceAlarmListValueAgentChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "DATASOURCE CONNECTION USAGE RATE",
   "type": "DataSourceAlarmListValueAgentChecker",
   "detectedValue": [
     {
       "agentId": "test-agent",
       "agentValue": [
                 {
                     "databaseName": "test",
                     "connectionValue": 32
                 }
        ]
     }
   ]
 },
 "unit": "%",
 "threshold": 16,
 "notes": "Note Example",
 "sequenceCount": 4
}
```


# New Inspector

[English](#id-1-overview) | [한국어](#id-1)

## 1 Overview

There has been changes in inspector in v3.0.0. The newly renewed inspector will be referred to as 'New Inspector' below, while the previous version will be referred to as 'Legacy Inspector' ([Legacy Application Inspector](https://pinpoint-apm.gitbook.io/pinpoint/v/v2.5.4/documents/application-inspector)).

Although users won't see significant changes on front-end, but the whole architecture has been rebuilt from the scratch. The data storage has been changed from HBase to Pinot. And the APIs have been improved so that it is more easily extenable and their responses more clear to understand.

## 2 Installation and Configuration

### 2.1 Install and Run Kafka

Kafka enables real-time streaming of inspector data from Pinpoint collector to Pinot.

#### 2.1.A Set Up Kafka

Refer to [this document](https://kafka.apache.org/quickstart) to download Kafka and start the Kafka environment.

If you have already [set up Kafka for Pinpoint System Metric](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.2.a-kafka-installation-guide), please skip this step.

#### 2.1.B Create Kafka Topics for New Inspector

* Create 2 topics with the names below:
  * inspector-stat-agent-00
  * inspector-stat-app

### 2.2 Set Up Pinot

#### 2.2.A Install Pinot

Install Pinot according to [Pinot Getting Started guide](https://docs.pinot.apache.org/basics/getting-started).

If you have already [set up Pinot for Pinpoint System Metric](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#id-3.2.a-install-and-run-pinot), please skip this step.

#### 2.2.B Create Pinot Tables

* Create 2 tables with the snames below:
  * inspectorStatAgent00: This table stores agent inspector data. The [script file to create the table](https://github.com/pinpoint-apm/pinpoint/tree/master/inspector-module/inspector-collector/src/main/pinot/multi-table) is provided in our github repository.
  * inspectorStatApp: This table stores application inspector data.
* Refer to the [github repository](https://github.com/pinpoint-apm/pinpoint/tree/master/inspector-module/inspector-collector/src/main/pinot) for table schema and configuration settings.

### 2.3 Configure and Run Pinpoint Collector, Web, and Batch with New Inspector

* **Related options and settings are already enabled by default, so there is no need to modify any settings from what is provided in our github repository.**
* When upgrading from Pinpoint version below 3.0 to version 3.0.0 or above, some of the options may be missing in the configuration properties files you have been using. Please refer to the related configurations in the following section to check if any changes are needed in your settings.

## 3 Related Settings of Pinpoint Components

* The following configurations are already set by default in Pinpoint version 3.0.
* When upgrading from Pinpoint version below 3.0 to version 3.0.0 or above and when you wish to continue using customized configuration files you have been using, please check if below mentioned configurations are well set in your files.

### Pinpoint Collector

* `application.yml` file in `collector-starter` module:

```
pinpoint:
  modules:
    collector:
      inspector:
        enabled: true
```

### Pinpoint Web

* `application.yml` file in `web-starter` module:

```
pinpoint:
  modules:
    web:
      inspector:
        enabled: true
```

### Pinpoint Batch

* `batch-root.properties` file in `batch` module:

```
alarm.collector.version=2
```

## 4 Q\&A

#### A Can we still use the Legacy Inspector to save the data to HBase?

Yes, but Legacy Inspector will be deprecated in v3.0.1 so we recommended you to use the New Inspector.

To use Legacy Inspector with v3.0.0, you need to add the following settings to the Pinpoint components:

**Modify `application.yml` file in `collector-starter` module OR add java vm option when running Pinpoint Collector.**

* application.yml

```
pinpoint:
  modules:
    collector:
      inspector:
        hbase:
          enabled: true
```

* java vm option

```
-Dpinpoint.modules.collector.inspector.hbase.enabled=true
```

**Modify `batch-root.properties` file in `batch` module OR add java vm option when running Pinpoint Batch.**

* batch-root.properties

```
alarm.collector.version=1
```

* java vm option

```
-Dalarm.collector.version=1
```

#### B Why change database to Pinot when there are no additional features provided to users?

New Inspector saves and retrieves the data faster than the Legacy Inspector thanks to Pinot. As Pinot project gets mature over time, there can be further improvements on performance or additional features can be introduced to Pinpoint Inpsector as well.

#### C Reading inspector-stat-agent table becomes slow as more data is being stored.

You can improve performance by distributing the data across multiple tables. Follow the steps below to create multiple Kafka topics and Pinot tables. Then, add settings to Pinpoint components to read and write data from multiple Pinot tables.

**Create More Kafka Topics**

* Create N Kafka topics. (From 00 to N-1)
* The format of the topics is as follows:
  * inspector-stat-agent-00
  * inspector-stat-agent-01
  * ...
  * inspector-stat-agent-99

**Create More Pinot Tables**

* Create N Pinot tables. (From 00 to N-1)
  * [The script file](https://github.com/pinpoint-apm/pinpoint/tree/master/inspector-module/inspector-collector/src/main/pinot/multi-table) creating multiple Pinot tables is provided in our github repository.
* The format of the table names and schema names is as follows:
  * inspectorStatAgent00
  * inspectorStatAgent01
  * ...
  * inspectorStatAgent99

**Modify `application.yml` file in `collector-starter` module OR add java vm option when running Pinpoint Collector**

* application.yml

```
kafka:
  inspector:
    agent:
      table:
        count: N
```

* java vm option

```
-Dkafka.inspector.agent.topic.count=N
```

**Modify `application.yml` file in `web-starter` module OR add java vm option when running Pinpoint Web**

* application.yml

```
pinot:
  inspector:
    agent:
      table:
        count: N
```

* java vm option

```
-Dpinot.inspector.agent.topic.count=N
```

**Modify `batch-root.properties` file in `batch` module OR add java vm option when running Pinpoint Batch**

* batch-root.properties

```
job.alarm.agent.inspector.stat.table.count=N
```

* java vm option

```
-Djob.alarm.agent.inspector.stat.table.count=N
```

***

## 1 개요

inspector가 Pinpoint v3.0.0에서 새로워졌습니다. 이하 새로워진 inspector를 'New Inspector'이라고 부르고 과거의 inspector는 'Legacy Inspector'라고 칭합니다 ([Legacy Application Inspector](https://pinpoint-apm.gitbook.io/pinpoint/v/v2.5.4/documents/application-inspector)).

New Inspector에서 사용자가 보는 화면은 크게 달라진 건은 없습니다. 그러나 내부적으로 많은 변화가 있었습니다. 데이터를 저장하는 저장소가 HBase에서 Pinot로 변경이 되었습니다. api를 쉽게 확장할 수 있고, response를 명확한 형식으로 개편했습니다. 즉 inspector 기능을 추가하고 확장하기 쉽게 개선되었습니다.

## 2 설치/설정 방법

### 2.1 Kafka 설치 및 실행

실시간으로 collector에서 데이터를 전달받아 Pinot에 저장하기 위해서 Kafka를 설치해야 합니다.

**2.1.A Kafka 설치**

[설치 가이드 링크](https://kafka.apache.org/quickstart)를 보고 Kafka를 다운 받아 실행합니다.

**2.1.B topic 생성**

* 아래 2개 Kafka topic을 생성합니다.
  * inspector-stat-agent-00
  * inspector-stat-app

### 2.2 Pinot 설치 및 실행

**2.1.A Pinot 설치**

Pinot 사이트에서 [설치 방법 가이드](https://docs.pinot.apache.org/basics/getting-started)를 참고하여 Pinot를 설치합니다.

**2.1.B Pinot table 생성**

* 아래 2개 테이블을 생성합니다.
  * inspectorStatAgent00: 이 테이블은 agent inspector data를 저장합니다. [스크립트](https://github.com/pinpoint-apm/pinpoint/tree/master/inspector-module/inspector-collector/src/main/pinot/multi-table)로 생성이 가능합니다.
  * inspectorStatApp: 이 테이블은 application inspector data를 저장합니다.
* table schema와 configuration은 [github repository](https://github.com/pinpoint-apm/pinpoint/tree/master/inspector-module/inspector-collector/src/main/pinot)를 참고해주세요.

### 2.3 Pinpoint Collector, batch, Web의 New Inspector 기능 활성화

* **관련 옵션 및 설정은 기본적으로 활성화되어 있으므로 추가로 설정할 필요가 없습니다.**
* Pinpoint 3.0 미만버전에서 3.0.0 이상버전으로 업그레이드 시 일부 옵션이 누락되는경우 아래 관련 옵션 설명을 참고해주세요.

## 3 Pinpoint 컴포넌트의 관련 설정

* 아래 설정들은 Pinpoint 3.0 버전에서 기본적으로 설정되어있습니다.
* Pinpoint 버전을 3.0으로 업그레이드하는경우 일부 설정이 누락되는 경우 참고하기 위해서 설정을 명시해놓습니다.

### Pinpoint Collector

* `collector-starter` 모둘의 `application.yml` 파일:

```
pinpoint:
  modules:
    collector:
      inspector:
        enabled: true
```

### Pinpoint Web

* `web-starter` 모듈의 `application.yml` 파일:

```
pinpoint:
  modules:
    web:
      inspector:
        enabled: true
```

### Pinpoint Batch

* `batch` 모듈의 `batch-root.properties` 파일:

```
alarm.collector.version=2
```

## 4 Q\&A

#### A HBase에 데이터를 저장하는 Legacy Inspector를 사용할 수 없나요?

가능합니다. 그러나 3.0.1 버전 이상 부터는 Legacy Inspector를 삭제할 예정이므로 Pinpoint 버전이 올라갈수록 기능을 사용할수 없으므로 New Inspector를 사용하는것을 권장합니다. 기능을 사용하려면 Pinpoint 컴포넌트들에 아래 설정을 추가해야합니다.

**collector-starter 프로젝트의 application.yml 파일이나 java vm option에 아래 설정을 추가해주세요.**

* application.yml

```
pinpoint:
  modules:
    collector:
      inspector:
        hbase:
          enabled: true
```

* java vm option

```
-Dpinpoint.modules.collector.inspector.hbase.enabled=true
```

**batch 프로젝트에서 batch-root.properties 파일이나 java vm option에 아래 설정을 추가해주세요.**

* batch-root.properties

```
alarm.collector.version=1
```

* java vm option

```
-Dalarm.collector.version=1
```

#### B 사용자에게 제공되는 기능은 비슷한데 Pinot기반으로 inspector를 개선한 이유는 뭘까요?

다양한 데이터를 빠르게 저장하고 확인하고 위해서 Pinot로 데이터를 저장하도록 개선되었고 아직 부족한 기능이 많지만 Pinot의 발전에 맞춰서 기능을 보완하도록 하겠습니다.

#### C inspector-stat-agent 테이블의 데이터가 많아서 읽기 속도가 느려집니다.

여러 개의 체이블에 데이터를 나누어 저장해서 성능 향상을 얻을 수 있습니다. 아래를 단계를 따라 전체 N 개의 Kafka topic과 Pinot table을 생성하고, Pinpoint 컴포넌트들에 설정을 추가해서 data를 수집/조회합니다.

**Kafka topic 생성**

* N개 Kafka topic을 생성합니다. (00에서 N-1까지)
* topic의 형식은 다음과 같습니다.
  * inspector-stat-agent-00
  * inspector-stat-agent-01
  * ...
  * inspector-stat-agent-99

**Pinot table 생성**

* N개 Pinot table을 생성합니다. (00에서 N-1까지)
  * [스크립트](https://github.com/pinpoint-apm/pinpoint/tree/master/inspector-module/inspector-collector/src/main/pinot/multi-table)로 다수의 테이블 생성이 가능합니다.
* table name과 schema name의 형식은 다음과 같습니다.
  * insepctorStatAgent00
  * insepctorStatAgent01
  * ...
  * insepctorStatAgent99

**`collector-starter` 모듈의 `application.yml` 파일이나 java vm option에 아래 설정을 추가해 주세요.**

* application.yml

```
kafka:
  inspector:
    agent:
      table:
        count: N
```

* java vm option

```
-Dkafka.inspector.agent.topic.count=N
```

**`web-starter` 모듈의 `application.yml` 파일이나 java vm option에 아래 설정을 추가해 주세요.**

* application.yml

```
pinot:
  inspector:
    agent:
      table:
        count: N
```

* java vm option

```
-Dpinot.inspector.agent.topic.count=N
```

**`batch` 모듈의 `batch-root.properties` 파일이나 java vm option에 아래 설정을 추가해 주세요.**

* batch-root.properties

```
job.alarm.agent.inspector.stat.table.count=N
```

* java vm option

```
-Djob.alarm.agent.inspector.stat.table.count=N
```


# System Metric

[English](#system_metrics) | [한국어](#1_system_metrics_기능이란?)

## 1 System Metrics

System metrics menu is newly added to Pinpoint in v2.5.0. Pinpoint uses [telegraf agent](https://portal.influxdata.com/downloads/) to collect system metrics data to Pinpoint Collector in which the data are saved in Pinot. Saved system metrics data are accessible via Pinpoint web.

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-c894164f22ccffbbac3a17a452c9c99867ae5280%2Fsystem_metric_01.png?alt=media)

Pinot is a real-time distributed OLAP datastore. For further information please refer to [their official documents](https://docs.pinot.apache.org).

## 2 Architecture

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-13e876804194ef1b6837ef12ae31d84461ec6fab%2Fsystem_metric_02.jpeg?alt=media)

1. Telegraf agent sends system metrics data to Pinpoint collector.
2. Pinpoint collector saves data to Pinot through Kafka.

* Kafka is necessary to stream data to Pinot.

3. Pinpoint web accesses Pinot to display collected metrics data.

## 3 Installation and Configuration

### 3.1 Install Kafka

Kafka enables real-time streaming of system metrics data from Pinpoint collector to Pinot.

#### 3.1.A Kafka Installation Guide

Please refer to [this document](https://kafka.apache.org/quickstart) to get Kafka and start the Kafka environment.

#### 3.1.B Create Kafka Topics for Pinpoint System Metrics

Create 3 topics with the names below:

* `system-metric-data-type`
* `system-metric-tag`
* `system-metric-double`

### 3.2 Install Pinot

This section describes how to install Pinot which is used in Pinpoint to save system metrics data.

#### 3.2.A Install and Run Pinot

* Install Pinot according to [Pinot Getting Started guide](https://docs.pinot.apache.org/basics/getting-started)
* Above guide gives you the way to run Pinot locally, in Docker, and in Kubernetes.

#### 3.2.B Create Pinot Tables

* Pinot table schemas for Pinpoint system metrics is provided in [our github repository](https://github.com/pinpoint-apm/pinpoint/tree/master/metric-module/metric/src/main/pinot).
* Please refer to [Pinot documents](https://docs.pinot.apache.org/basics/components/table#streaming-table-creation) to create necessary tables in your Pinot cluster.
* Total 3 tables should be created.
  * systemMetricDataType: this table saves type informations on collected data.
  * systemMetricTag: this table saves metadata (i.e., host, tags) for collected data.
  * systemMetricDouble: this table saves metric data in double. In order to use the hybrid table feature, create both REALTIME and OFFLINE tables.

### 3.3 Configure and Run Pinpoint Collector with System Metrics

There are additional configurations for Pinpoint collector to collect the metrics data from Telegraf agents.

#### 3.3.A Pinpoint Collector Settings for System Metrics

**1)** In order to communicate with Pinot, you need to modify the configuration files in the [profiles](https://github.com/pinpoint-apm/pinpoint/tree/master/pinot/pinot-config/src/main/resources/pinot/profiles) directory according to your profile.

* Modify pinot-jdbc.properties configuration: Set the address of the Pinot installed in [3.1](#3.1-Install-Pinot) as follows:
  * ```
            pinpoint.pinot.jdbc.url=jdbc:pinot://localhost:9000
            pinpoint.pinot.jdbc.username=userId
            pinpoint.pinot.jdbc.password=password
    ```

**2)** In order to communicate with Kafka, you need to modify the configuration files in the [profiles](https://github.com/pinpoint-apm/pinpoint/tree/master/pinot/pinot-kafka/src/main/resources/profiles) directory according to your profile.

* Modify kafka-producer-factory.properties configuration: Set the address of your Kafka instance:
  * ```
    pinpoint.metric.kafka.bootstrap.servers=--KAFKA_ADDRESS--
    ```

#### 3.3.B Run Pinpoint Collector with System Metrics

After successfully building Pinpoint project, run `pinpoint-collector-starter-boot-XXXX.jar` file created under `pinpoint/metric-module/collector-starter/target/deploy`.

* `pinpoint-collector-starter-boot-XXXX.jar` includes system metrics on top of original pinpoint-collector.
* In order to enable metric functions, you need to add `--pinpoint.collector.type=METRIC` or `--pinpoint.collector.type=ALL` arguments when starting the application.
  * METRIC: only enables collecting the system metrics.
  * ALL: enables both pinpoint collector and system metrics collection.

### 3.4 Configure and Run Pinpoint Web with System Metrics

There are additional configurations for Pinpoint web to display the system metrics data stored in Pinot.

#### 3.4.A Pinpoint Web Settings for System Metrics

1. In order to communicate with Pinot, you need to modify the configuration files in the \[profiles]\((<https://github.com/pinpoint-apm/pinpoint/tree/master/pinot/pinot-config/src/main/resources/pinot/profiles>) directory according to your profile.

* Update the address of the Pinot installed in [3.1](#3.1-Install-Pinot) in the jdbc-pinot.properties configuration file:

  ```
  pinpoint.pinot.jdbc.url=jdbc:pinot://localhost:9000
  pinpoint.pinot.jdbc.username=userId
  pinpoint.pinot.jdbc.password=password
  ```

**2)** To enable the system metric feature in the web interface, modify the [pinpoint-web-metric.properties](https://github.com/pinpoint-apm/pinpoint/tree/master/metric-module/metric/src/main/resources/pinot-web/profiles) file:

```
config.show.systemMetric=true
```

#### 3.4.B Run Pinpoint Web with System Metrics

After successfully building Pinpoint project, run `pinpoint-web-starter-boot-XXXX.jar` file created under `pinpoint/metric-module/web-starter/target/deploy`.

#### 3.5 Additional Information

Pinpoint web and collector binaries with system metrics is located under different directories from those of the original Pinpoint web and collector.

* original collector: pinpoint/collector/deploy -> collector with system metrics: pinpoint/metric-module/collector-starter/target/deploy
* original web: pinpoint/web/deploy -> web with system metrics: pinpoint/metric-module/web-starter/target/deploy

### 3.6 Install and Configure Talegraf Agent

Telegraf collects below metrics information on the host machine:

* cpu
* disk usage
* disk usage (percent)
* inode usage
* memory usage
* memory usage(percent)
* swap
* system load
* nginx
* apache

***

* Install Telegraf according to this [installation guide](https://docs.influxdata.com/telegraf/v1.21/introduction/installation/).
* Add below configuration to `telegraf.conf` file to send collected metrics to Pinpoint collector via http.
  * **Note**: Starting from Pinpoint v3.0.2, the metric port has been changed from `15200` to `9995`.
  * ```
              [[outputs.http]]
                url = "http://{PINPOINT_COLLECTOR_IP}:9995/telegraf"
                 
                 [outputs.http.headers]
                 hostGroupName = {applicationName}
                 Content-Type = "application/json"  
    ```
  * `url`: substitute `{PINPOINT_COLLECTOR_IP}` to your Pinpoint collector address so that telegraf can send collected metrics to Pinpoint collector
  * `hostGroupName`: this value will be used as the key in Pinpoint web when querying the metrics details. It is recommended to use your applicationName already used in Pinpoint.

### 4 View Collected System Metrics Data

1. Click `Infrastructure` on the side bar menu in Pinpoint web.
2. Search for the hostGroupName you have configured for Telegraf agents as decribed [in 3.4](#3.4-Install-and-Configure-Talegraf-Agent).
3. A list of hosts will be displayed on the left, and you can view the system metrics data by clicking each of them.

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-c894164f22ccffbbac3a17a452c9c99867ae5280%2Fsystem_metric_01.png?alt=media)

### 5 Notes

* Other metrics and statistics data will be stored in Pinot to enhance Pinpoint experience in near future.
* Currently this system metrics versions are in beta. It will be officially released when when we can make sure that everything works as we intended.
* If you have been using the system metric feature in version 2.5.0 or lower and are upgrading, please refer to [guide](https://github.com/pinpoint-apm/pinpoint/issues/9791#issuecomment-1491486262) for instructions.

***

## 1 system metrics 기능이란?

system metrics 기능은 v2.5.0에 핀포인트에 새로 추가되었다. [telegraf agent](https://portal.influxdata.com/downloads/) 를 사용하여 system metric 데이터를 collector에 전달하고 pinot에 데이터를 저장한다. pinpoint web에서 저장된 system metric 데이터를 확인할 수 있다.

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-c894164f22ccffbbac3a17a452c9c99867ae5280%2Fsystem_metric_01.png?alt=media)

pinot는 실시간 분산 OLAP 데이터 저장소이다. 자세한 사항은 [pinot 사이트](https://docs.pinot.apache.org)를 참고하도록 하자.

## 2 구조

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-13e876804194ef1b6837ef12ae31d84461ec6fab%2Fsystem_metric_02.jpeg?alt=media)

* ① telgegraf agent에서 system metric 데이터를 collector에 전달한다.
* ② collector는 kafka에 데이터를 전송하여 pinot에 데이터를 저장한다.
  * 참고로 pinot는 stream 데이터 전송을 위해서 kafka를 반드시 필요로 한다.
* ③ web은 pinot에서 데이터를 조회하여 화면으로 데이터를 보여준다.

## 3 설치/설정 방법

### 3.1 kafka 설치 및 실행

실시간으로 collector에서 데이터를 전달받아 pinot에 저장하기 위해서 kafka를 설치해야 한다.

#### 3.1.A. kafka 설치

* [설치 가이드 링크](https://kafka.apache.org/quickstart)를 보고 kafka를 다운 받아 실행하자.

#### 3.1.B. topic 생성

* 아래 3개 topic을 생성하자. -`system-metric-data-type`, `system-metric-tag`, `system-metric-double`

### 3.2 pinot 설치 및 실행

시스템 메트릭 데이터를 저장하는 pinot를 설치하는 법을 안내한다.

#### 3.2.A. pinot 설치 및 실행

* pinot 사이트에서 [설치 방법 가이드](https://docs.pinot.apache.org/basics/getting-started)를 참고하여 pinot를 설치한다.
* 다양한 환경(local, docker, Kubernetes)에서 pinot 실행 환경을 구성할 수 있으니 위 가이드를 참고하자.

#### 3.2.B. 테이블 스키마 및 생성

* [테이블 생성 스키마 파일](https://github.com/pinpoint-apm/pinpoint/tree/master/metric-module/metric/src/main/pinot)에 테이블 정보가 있다.
* 테이블 생성 방법은 [pinot가이드](https://docs.pinot.apache.org/basics/components/table#streaming-table-creation)를 참고하여 pinot 실행 환경 맞게 테이블을 생성하면 된다.
* 생성하는 테이블은 총 3개이다.
  * systemMetricDataType : 수집되는 데이터의 type 정보를 저장하는 테이블이다.
  * systemMetricTag : 수집되는 데이터의 metadata(host 정보, 데이터의 tag 정보)를 저장하는 테이블이다.
  * systemMetricDouble : double 데이터를 저장하는 테이블이다. hybrid table 기능 사용을 위해서 REALTIME, OFFLINE 테이블 둘다 생성하자.

### 3.3 collector 설정 및 실행

telegraf agent로 부터 전송된 데이터를 수집하기 위해서 collector에 설정을 추가한다.

#### 3.3.A. collector 설정

**1)** pinot와 통신을 위해서 [설정파일](https://github.com/pinpoint-apm/pinpoint/tree/master/pinot/pinot-config/src/main/resources/pinot/profiles)들을 profile에 맞게 수정해야 한다.

* pinot-jdbc.properties 설정 : [3.1](#3.1-pinot-설치-및-실행)에서 설치한 pinot의 주소를 설정한다.
  * ```
            pinpoint.pinot.jdbc.url=jdbc:pinot://localhost:9000
            pinpoint.pinot.jdbc.username=userId
            pinpoint.pinot.jdbc.password=password
    ```

**2)** kafka와 통신을 위해서 [설정파일](https://github.com/pinpoint-apm/pinpoint/tree/master/pinot/pinot-kafka/src/main/resources/profiles)들을 profile에 맞게 수정해야 한다.

* kafka-producer-factory.properties 설정 : kafka 의 주소를 설정한다.
  * ```
            pinpoint.metric.kafka.bootstrap.servers=--KAFKA_ADDRESS--
    ```

#### 3.3.B. collector 실행 방법

빌드 후 pinpoint/metric-module/collector-starter/target/deploy에 생성된 `pinpoint-collector-starter-boot-XXXX.jar`을 실행하면 된다.

* `pinpoint-collector-starter-boot-XXXX.jar` 은 pinpoint-collector 기능과 system metric 수집기능이 합해진 패키지이다.
* metric 기능을 활성화 하기 위해서 실행시 `--pinpoint.collector.type=METRIC` 나 `--pinpoint.collector.type=ALL` 옵션을 추가해야한다.
  * METRIC : system metric 수집기능만 동작된다.
  * ALL : pinpoint collector 기능과 system metric 수집기능이 동시에 동작된다.

### 3.4 web 설정 및 실행

pinot에 저장된 시스템 메트릭 데이터를 보여주기 위해서 web 설정을 수정한다.

#### 3.4.A. web 설정

**1)** pinot와 통신을 위해서 [설정파일](https://github.com/pinpoint-apm/pinpoint/tree/master/pinot/pinot-config/src/main/resources/pinot/profiles)들을 profile에 맞게 수정해야 한다.

* jdbc-pinot.properties 설정 : [3.1](#3.1-pinot-설치-및-실행)에서 설치한 pinot의 주소를 설정한다.
  * ````
        pinpoint.pinot.jdbc.url=jdbc:pinot://localhost:9000
        pinpoint.pinot.jdbc.username=userId
        pinpoint.pinot.jdbc.password=password
        ```
    ````

**2)**

* system metric 기능을 web에서 활성화하기 위해서 [pinpoint-web-metric.properties](https://github.com/pinpoint-apm/pinpoint/tree/master/metric-module/metric/src/main/resources/pinot-web/profiles) 파일을 수정한다.
  * ````
        config.show.systemMetric=true
        ```
    ````

#### 3.4.B. web 실행 방법

빌드 후 pinpoint/metric-module/web-starter/target/deploy에 생성된 `pinpoint-web-starter-boot-XXXX.jar`을 실행하면 된다.

* `pinpoint-web-starter-boot-XXXX.jar` 은 pinpoint web 기능과 metric 데이터 확인 기능이 합해진 패키지이다.

### 3.5 참고

* 참고로 web, collector의 실행파일이 과거 버전과 다르게 다른곳에 존재한다.
* 기존의 web, collector 실행파일 경로와 다르게 system metric기능이 포함된 collector, web은 실행 파일 경로는 다음과 같다.
  * collector : pinpoint/collector/deploy -> pinpoint/metric-module/collector-starter/target/deploy
  * web : pinpoint/web/deploy -> pinpoint/metric-module/web-starter/target/deploy

### 3.6 telegraf agent 설치 및 설정

telegraf agent를 통해 수집된 시스템 메트릭은 다음과 같다.

* cpu
* disk usage
* disk usage(percent)
* inode usage
* memory usage
* memory usage(percent)
* swap
* system load
* nginx
* apache

***

* 시스템 메트릭 데이터를 수집하는 telegraf agent를 설치하자.
  * [telegraf agent 설치 가이드](https://docs.influxdata.com/telegraf/v1.21/introduction/installation/)
* telegraf agent가 http 프로토콜로 collector에 데이터를 전달할 수 있도록 설정파일을 수정 해야한다.
  * telegraf.conf 설정 방법
    * http 프로토콜로 데이터를 전달수 있도록 output http plugin 아래 설정을 추가한다.
      * **참고**: Pinpoint v3.0.2부터 메트릭 포트가 `15200`에서 `9995`로 변경되었습니다.
      * ```
                [[outputs.http]]
                  url = "http://{PINPOINT_COLLECTOR_IP}:9995/telegraf"
                   
                   [outputs.http.headers]
                   hostGroupName = {applicationName}
                   Content-Type = "application/json"
        ```
    * `url`: {PINPOINT\_COLLECTOR\_IP} 자리에 데이터를 수집하는 collector의 주소를 설정한다.
    * `outputs.http.headers`은 서버 그룹의 key와 Content-Type을 설정한다.
      * `hostGroupName`: {applicationName}에 설정한 값을 key로 pinpoint-web에서 데이터를 조회할 수 있다. 핀포인트를 이미 사용 중이라면 application을 추적할 때 agent 설정 값으로 사용했던 applicationName을 사용하는 것을 추천한다.

## 4 데이터 조회

* pinpoint-web에서 왼쪽 `Infrastructure` 메뉴를 선택하여 system metric 화면으로 이동한다.
* 상단의 select box에서 telegraf.conf 파일에 설정한 hostGroupName 값을 찾아서 선택한다.
* 아래와 같이 왼쪽에 호스트 목록이 나오고, 호스트를 선택해서 system metric 데이터를 확인할 수 있다.

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-c894164f22ccffbbac3a17a452c9c99867ae5280%2Fsystem_metric_01.png?alt=media)

## 5 기타

* pinot에는 system metric 뿐만아니라 pinpoint의 다양한 메트릭 데이터와 통계 데이터를 저장할 예정이다. 즉 pinot는 다양한 데이터를 저장하는 목적으로 사용될 것이다.
* system metric의 경우 당분간은 beta 기능으로 제공할것이고 안정적으로 기능이 운영되는 경험이 쌓이면 공식적으로 기능을 제공할 것이다.
* 2.5.0 이하 버전에서 system metric 기능을 사용하다가 버전을 업그레이드 하는 경우 [guide](https://github.com/pinpoint-apm/pinpoint/issues/9791#issuecomment-1491486262) 설명을 참고하자.


# URI Statistics

[English](#uri_statistics) | [한국어](#URI_통계)

## URI Statistics

URI statistics menu is newly added to Pinpoint in v2.5.0. Pinpoint Agent aggregates URI templates and send them to Pinpoint collector via GRPC. Pinpoint Collector saves the data to Pinot via Apache Kafka. Pinpoint Web accesses Pinot to display the data.

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-766216ae1ef81bd7cf547351f746d5d7ccc833b7%2Furi_statistics_01.png?alt=media)

### 1. Installation and Configuration

#### 1.1 Install and Run Kafka

Kafka enables real-time streaming of URI statistics data from Pinpoint collector to Pinot. If you have already [set up Kafka for Pinpoint System Metric](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.2.a-kafka-installation-guide), please skip this step.

* Please refer to [this document](https://kafka.apache.org/quickstart) to get Kafka and start the Kafka environment.

#### 1.2 Create Kafka Topics for Pinpoint URI Statistics

Create a topic with the name `url-stat`

```
$ bin/kafka-topics.sh --create --topic url-stat --bootstrap-server ${YOUR_KAFKA_SERVER_ADDRESS}
```

#### 1.3 Install and Run Pinot

This section describes how to install Pinot which is used in Pinpoint to save URI statistics data. If you have already [set up Pinot for Pinpoint System Metric](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.1-install-pinot), please skip this step.

* Install Pinot according to [Pinot Getting Started guide](https://docs.pinot.apache.org/basics/getting-started).
* Above guide gives you the way to run Pinot locally, in Docker, and in Kubernetes.

#### 1.4 Create Pinot Tables

* Pinot table schema for Pinpoint URI statistics is provided in [our github repository](https://github.com/pinpoint-apm/pinpoint/tree/master/uristat/uristat-common/src/main/pinot).
* Please refer to [Pinot documents](https://docs.pinot.apache.org/basics/components/table#streaming-table-creation) to create necessary tables in your Pinot cluster.
* Let's create the uriStat table by referencing the schema file and table settings from the provided path. To enable hybrid table functionality, let's create both REALTIME and OFFLINE tables for the 'uriStat' table.

#### 1.5 Configure and Attach Pinpoint Agent

This section describes the URI stat configuration values added for URI statistics.

**1.5.1 Configuration values for URI Statistics**

Below are default agent configuration values for URI statistics.

```
###########################################################
# URI Stat
###########################################################
profiler.uri.stat.enable=true
profiler.uri.stat.spring.webmvc.enable=true
profiler.uri.stat.spring.webmvc.useuserinput=false
profiler.uri.stat.spring.webflux.enable=true
profiler.uri.stat.spring.webflux.useuserinput=false
profiler.uri.stat.vertx.enable=true
profiler.uri.stat.vertx.useuserinput=false
profiler.uri.stat.tomcat.useuserinput=false
```

* profiler.uri.stat.enable: whether Pinpoint Agent collects URI statistics or not.
  * `true`: collects URI statistics
  * `false`: doesn't collect URI statistics
* profiler.uri.stat.spring.webmvc.enable: whether Pinpoint Agent collects URI statistics from Spring Web MVC applications.
  * `true`: collects URI statistics from Spring Web MVC applications.
  * `false`: doesn't collect URI statistics from Spring Web MVC applications.
* profiler.uri.stat.spring.webmvc.useuserinput: whether Pinpoint Agent uses user-input request attribute values for URI templates when available.

  * `true`: uses user-input request attribute values.
  * `false`: ignores user-input request attribute values.

  Set attribute `pinpoint.metric.uri-template` to your Spring web request as shown below to override default URI template provided by Pinpoint.

  ```
    @RequestMapping("/testUserInputRequestAttribute")
    public Map<String, Object> testUserInputAttribute(HttpServletRequest request) {
        Map<String, Object> map = new HashMap<String, Object>();
        map.put("message", "test user input attribute");
        request.setAttribute("pinpoint.metric.uri-template", "/userInput");
        return map;
    }
  ```
* profiler.uri.stat.spring.webflux.enable: whether Pinpoint Agent collects URI statistics from Spring Webflux applications.
  * `true`: collects URI statistics from Spring Webflux applications.
  * `false`: doesn't collect URI statistics from Spring Webflux applications.
* profiler.uri.stat.spring.webflux.useuserinput: whether Pinpoint Agent uses user-input request attribute values for URI templates when available.

  * `true`: uses user-input request attribute values.
  * `false`: ignores user-input request attribute values.

  Set attribute `pinpoint.metric.uri-template` to your Spring web request as shown below to override default URI template provided by Pinpoint.

  ```
    @GetMapping("/server/welcome/**")
    public Mono<String> welcome(ServerWebExchange exchange) {
        exchange.getAttributes().put("pinpoint.metric.uri-template", "/test");
        return Mono.just("Welcome Home");
    }
  ```
* profiler.uri.stat.vertx.enable: whether Pinpoint Agent collects URI statistics from Vert.x applications.
  * `true`: collects URI statistics from Vert.x applications.
  * `false`: doesn't collect URI statistics from Vert.x applications.
* profiler.uri.stat.vertx.useuserinput: whether Pinpoint Agent uses user-input routing context attribute values for URI templates when available.

  * `true`: uses user-input routing context attribute values.
  * `false`: ignores user-input routing context attribute values.

  Set attribute `pinpoint.metric.uri-template` to your Vert.x routing context as shown below to override default URI template provided by Pinpoint.

  ```
    router.get("/routinContextAttributeAdded").handler(routingContext -> {
        routingContext.put("pinpoint.metric.uri-template", "/test");
        routingContext.response().end("pinpoint.metric.uri-tempate = /test");
    });
  ```
* profiler.uri.stat.tomcat.useuserinput: (Added in v2.5.3) whether Pinpoint Agent uses user-input attribute values from Tomcat for URI templates when available.

  * `true`: collects URI statics from Tomcat user-input attribute values.
  * `false`: doesn't check Tomcat request attributes for URI statistics.

  This is provided to collect URI statistics information in Tomcat applications without supported frameworks(Spring WebMVC, Spring Webflux, VertX). If you are using supported frameworks, it is recommended to use framework-specific options and disable this option. Since there is no default URI template provided by tomcat, users need to set attribute `pinpoint.metric.uri-template` to your Tomcat request to start collecting URI statistics information.

To change the configuration values described above, update `pinpoint.config` under [each profile directory](https://github.com/pinpoint-apm/pinpoint/tree/master/agent/src/main/resources/profiles) and rebuild the project. Or, you can simply pass these properties when starting your application with Pinpoint Agent (e.g. `-Dprofiler.uri.stat.enable=false`).

#### 1.6 Configure and Run Pinpoint Collector & Web with URI Statistics

Instead of the default Pinpoint Collector and Web binaries, you should use those compiled under metric-module.

Please check [here](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.3-configure-and-run-pinpoint-collector-with-system-metrics) for Pinpoint Metric Collector properties.

* Enable URI statistics by adding the below line at [pinpoint-collector.properties](https://github.com/pinpoint-apm/pinpoint/tree/master/metric-module/collector-starter/src/main/resources/profiles):

  ```
  collector.stat.uri=true
  ```
* `pinpoint.collector.type=BASIC` argument should be used to collect URI statistics in collector.

Please check [here](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.4-configure-and-run-pinpoint-web-with-system-metrics) for Pinpoint Metric Web properties.

* Enable URI statistics by adding the below line at [pinpoint-web-uristat.properties](https://github.com/pinpoint-apm/pinpoint/tree/master/uristat/uristat-web/src/main/resources/profiles):

  ```
  config.show.urlStat=true
  ```

### 2. View Collected URI Statistics Data

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-478271df836f370ea719470568b103ee42d51a81%2Furi_statistics_02.png?alt=media)

1. Click `URL Statistic` on the side bar menu in Pinpoint web.
2. Search for the application name you used to configure Pinpoint Agent.
3. Top 50 URIs used in your application will be displayed below the empty chart.
4. Click each URI to load the chart.

## URI 통계

URI 통계 기능은 핀포인트 v2.5.0에 신규로 추가되었다. 핀포인트 에이전트에서 URI 템플릿 정보를 수집하여 GRPC를 사용해 핀포인트 콜렉터에 전달하고, 핀포인트 콜렉터는 아파치 카프카를 통해 아파치 피노에 값을 저장한다. 핀포인트 웹에서 저장된 URI 통계 데이터를 확인할 수 있다.

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-766216ae1ef81bd7cf547351f746d5d7ccc833b7%2Furi_statistics_01.png?alt=media)

### 1. 설치 및 설정 방법

#### 1.1 카프카 설치 및 실행

실시간으로 핀포인트 콜렉터에서 데이터를 전달받아 피노에 저장하기 위해서 카프카를 설치해야 한다. 이미 [시스템 메트릭 설정을 하면서 카프카를 설치](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.2-kafka)하였다면, 이 부분은 건너뛰십시오.

* [설치 방법 가이드](https://kafka.apache.org/quickstart)를 참고하여 kafka를 설치한다.

#### 1.2 카프카 토픽 생성

아래와 같이 `url-stat` 토픽을 생성한다.

```
$ bin/kafka-topics.sh --create --topic url-stat --bootstrap-server ${YOUR_KAFKA_SERVER_ADDRESS}
```

#### 1.3 피노 설치 및 실행

URI 통계 값을 저장하는 피노를 설치하는 법을 안내한다. 이미 [시스템 메트릭 설정을 하면서 피노를 설치](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.1.a.-pinot)하였다면, 이 부분은 건너뛰십시오.

* [피노 설치 가이드](https://docs.pinot.apache.org/basics/getting-started)를 참고하여 피노를 설치한다.
* 다양한 환경 (local, docker, kubernetes)에서 피노 실행 환경을 구성할 수 있으니 위 가이드를 참고하자.

#### 1.4 피노 테이블 스키마 및 테이블 생성

* [핀포인트 깃헙 저장소](https://github.com/pinpoint-apm/pinpoint/tree/master/uristat/uristat-common/src/main/pinot)에 URI 통계를 위한 피노 테이블 스키마와 테이블 정보가 있다.
* 위 경로에서 스키마 파일과 테이블 설정을 참고해서 `uriStat` 테이블을 생성한다. hybrid table 기능 사용을 위해서 REALTIME, OFFLINE 테이블 둘다 생성하자.
* 피노에 필요한 테이블을 구성하는 방법은 [피노 공식 문서](https://docs.pinot.apache.org/basics/components/table#streaming-table-creation)를 참고하자.

#### 1.5 핀포인트 에이전트 설정

URI 통계 수집을 위해 핀포인트 에이전트에 설정해야 하는 값들을 안내한다.

**1.5.1 URI 통계 수집을 위한 설정 값**

URI 통계 수집과 관련된 핀포인트 에이전트의 설정 기본값들은 아래와 같다.

```
###########################################################
# URI Stat
###########################################################
profiler.uri.stat.enable=true
profiler.uri.stat.spring.webmvc.enable=true
profiler.uri.stat.spring.webmvc.useuserinput=false
profiler.uri.stat.spring.webflux.enable=true
profiler.uri.stat.spring.webflux.useuserinput=false
profiler.uri.stat.vertx.enable=true
profiler.uri.stat.vertx.useuserinput=false
profiler.uri.stat.tomcat.useuserinput=false
```

* profiler.uri.stat.enable: 핀포인트 에이전트가 URI 통계를 수집하는지 여부.
  * `true`: URI 통계를 수집한다.
  * `false`: URI 통계를 수집하지 않는다.
* profiler.uri.stat.spring.webmvc.enable: 핀포인트 에이전트가 스프링 웹 MVC 어플리케이션에서 URI 통계를 수집하는지 여부.
  * `true`: 스프링 웹 MVC 어플리케이션에서 URI 통계를 수집힌다.
  * `false`: 스프링 웹 MVC 어플리케이션에서 URI 통계를 수집하지 않는다.
* profiler.uri.stat.spring.webmvc.useuserinput: 핀포인트 에이전트가 스프링 웹 어플리케이션에서 사용자 정의 URI 템플릿을 우선적으로 사용하는지 여부.

  * `true`: 스프링 웹 어플리케이션에서 사용자 정의 URI 템플릿을 우선적으로 사용한다.
  * `false`: 스프링 웹 어플리케이션에서 사용자 정의 URI 템플릿을 확인하지 않고 핀포인트가 수집한 템플릿만 사용한다.

  핀포인트에서 수집하는 URI 템플릿을 사용하지 않고 사용자 정의 URI 템플릿을 사용하고 싶다면, 아래 예제와 같이 스프링 웹 리퀘스트 객체 attribute에 `pinpoint.metric.uri-template`를 key 값으로 하는 속성 값을 설정해야 한다.

  ```
    @RequestMapping("/testUserInputRequestAttribute")
    public Map<String, Object> testUserInputAttribute(HttpServletRequest request) {
        Map<String, Object> map = new HashMap<String, Object>();
        map.put("message", "test user input attribute");
        request.setAttribute("pinpoint.metric.uri-template", "/userInput");
        return map;
    }
  ```
* profiler.uri.stat.spring.webflux.enable: 핀포인트 에이전트가 스프링 웹플럭스 어플리케이션에서 URI 통계를 수집하는지 여부.
  * `true`: 스프링 웹플럭스 어플리케이션에서 URI 통계를 수집힌다.
  * `false`: 스프링 웹플럭스 어플리케이션에서 URI 통계를 수집하지 않는다.
* profiler.uri.stat.spring.webflux.useuserinput: 핀포인트 에이전트가 스프링 웹플럭스 어플리케이션에서 사용자 정의 URI 템플릿을 우선적으로 사용하는지 여부.

  * `true`: 스프링 웹플럭스 어플리케이션에서 사용자 정의 URI 템플릿을 우선적으로 사용한다.
  * `false`: 스프링 웹플럭스 어플리케이션에서 사용자 정의 URI 템플릿을 확인하지 않고 핀포인트가 수집한 템플릿만 사용한다.

  핀포인트에서 수집하는 URI 템플릿을 사용하지 않고 사용자 정의 URI 템플릿을 사용하고 싶다면, 아래 예제와 같이 스프링 웹 리퀘스트 객체 attribute에 `pinpoint.metric.uri-template`를 key 값으로 하는 속성 값을 설정해야 한다.

  ```
    @GetMapping("/server/welcome/**")
    public Mono<String> welcome(ServerWebExchange exchange) {
        exchange.getAttributes().put("pinpoint.metric.uri-template", "/test");
        return Mono.just("Welcome Home");
    }
  ```
* profiler.uri.stat.vertx.enable: 핀포인트 에이전트가 Vert.x 어플리케이션에서 URI 통계를 수집하는지 여부.
  * `true`: Vert.x 어플리케이션에서 URI 통계를 수집힌다.
  * `false`: Vert.x 어플리케이션에서 URI 통계를 수집하지 않는다.
* profiler.uri.stat.vertx.useuserinput: 핀포인트 에이전트가 Vert.x 어플리케이션에서 사용자 정의 URI 템플릿을 우선적으로 사용하는지 여부.

  * `true`: Vert.x 어플리케이션에서 사용자 정의 URI 템플릿을 우선적으로 사용한다.
  * `false`: Vert.x 어플리케이션에서 사용자 정의 URI 템플릿을 확인하지 않고 핀포인트가 수집한 템플릿만 사용한다.

  핀포인트에서 수집하는 URI 템플릿을 사용하지 않고 사용자 정의 URI 템플릿을 사용하고 싶다면, 아래 예제와 같이 Vert.x RoutingContext 객체에 `pinpoint.metric.uri-template` 를 key 값으로 하는 속성 값을 설정해야 한다.

  ```
    router.get("/routinContextAttributeAdded").handler(routingContext -> {
        routingContext.put("pinpoint.metric.uri-template", "/test");
        routingContext.response().end("pinpoint.metric.uri-tempate = /test");
    });
  ```
* profiler.uri.stat.tomcat.useuserinput: (v2.5.3에 추가 됨) 핀포인트 에이전트가 Tomcat 어플리케이션에서 사용자 정의 URI 템플릿을 사용하여 통계를 수집하는지 여부.

  * `true`: Tomcat 어플리케이션에서 사용자 정의 URI 템플릿을 사용하여 URI 통계를 수집한다.
  * `false`: URI 통계 수집을 할 때 Tomcat 리퀘스트 attribute를 확인하지 않는다.

  이 옵션은 지원하는 프레임워크(Spring WebMVC, Spring Webflux, VertX)를 사용하지 않는 Tomcat 어플리케이션에서 URI 통계를 수집하기 위해 추가되었습니다. 만약 지원하는 프레임워크를 사용하고 있다면, 해당 프레임워크 관련 URI 통계 옵션을 사용하고 이 옵션은 false로 사용하는 것을 권장합니다. 지원하는 프레임워크에서와는 다르게 Tomcat 자체적으로 URI 템플릿을 제공하지 않기 때문에, 이 옵션을 사용할 경우, 사용자가 직접 Tomcat request attribute에 `pinpoint.metric.uri-template`를 추가하여야만 URI 통계가 수집됩니다.

위 설정 값들을 변경하려면 원하는 [핀포인트 프로파일 경로](https://github.com/pinpoint-apm/pinpoint/tree/master/agent/src/main/resources/profiles)의 `pinpoint.config` 파일에서 값을 변경하여 핀포인트를 재빌드한다. 파일을 수정하지 않고, 핀포인트 에이전트를 붙힐 어플리케이션을 실행할 때 `-Dprofiler.uri.stat.enable=false`와 같이 값을 넣어도 된다.

#### 1.6 핀포인트 콜렉터와 핀포인트 웹 설정 및 실행

URI 통계를 수집하고 값을 확인하려면, 핀포인트 v2.5.0 이전 버전에서 사용하던 콜렉터와 웹 JAR 파일이 아니라 metric-module 밑에 생성되는 파일을 사용해야 한다.

[핀포인트 메트릭 콜렉터를 설명한 문서](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.3-collector)에 자세한 설명이 있으니 참고해서 메트릭 콜렉터 설정값을 세팅하자.

* 위 설정 외에 URI 통계를 위해 [pinpoint.collector.properties](https://github.com/pinpoint-apm/pinpoint/tree/master/metric-module/collector-starter/src/main/resources/profiles)에 아래 설정값이 추가되었다:

  ```
  collector.stat.uri=true
  ```
* URI 통계를 수집하기 위해서는 콜렉터를 시작할 때 `pinpoint.collector.type=BASIC` argument를 넣어야 한다.

[핀포인트 메트릭 웹을 설명한 문서](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.4-web)에 자세한 설명이 있으니 참고해서 메트릭 웹 설정값을 세팅하자.

* 위 설정 외에 URI 통계를 위해 [pinpoint-web-uristat.properties](https://github.com/pinpoint-apm/pinpoint/tree/master/uristat/uristat-web/src/main/resources/profiles)에 아래 설정값이 추가되었다:

  ```
  config.show.urlStat=true
  ```

### 2. URI 통계 데이터 조회

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-478271df836f370ea719470568b103ee42d51a81%2Furi_statistics_02.png?alt=media)

1. 핀포인트 메트릭 웹을 실행하여 왼쪽 `URL Statistic` 메뉴를 선택한다.
2. 상단의 seslect box에서 핀포인트 에이전트에 설정한 어플리케이션 이름을 조회한다..
3. 초기 화면에서는 선택한 어플리케이션에서 가장 많이 사용한 상위 50개 URI가 빈 차트 밑에 표시된다.
4. 원하는 URI를 클릭하면 차트에 데이터가 표시된다.


# URI Statistics Alarm

## URI Statistics Alarms

Alarms for URI statistics will be introduced to Pinpoint in v3.0.0. Similar to the existing [alarms in Pinpoint](https://pinpoint-apm.gitbook.io/pinpoint/documents/alarm), pinpoint-batch server checks every 3 minutes if configured alarm rules are triggered with data in the last 5 minutes.

### 1. Alarm Rules

Alarms rules can be created for each URI, using data collected with [URI Statistics](https://pinpoint-apm.gitbook.io/pinpoint/documents/uri_statistics).

#### Alarm Data

* APDEX: The APDEX score of the specified URI for the past 5 minutes (0.00 \~ 1.00)
* Average Response Time: The avgerage response time of the specified URI for the past 5 minutes (ms)
* Maximum Response Time: The maximum response time of the specified URI for the past 5 minutes (ms)
* Total Request Count: The total number of requests made to the specified URI in the past 5 minutes
* Failed Request Count: The number of failed requests to the specified URI in the past 5 minutes

#### Alarm Condition

When setting up a new alarm, the conditions for triggering the alarm need to be specified. You can choose from the following comparison operators:

* (collected value) `>` (threshold value)
* (collected value) `>=` (threshold value)
* (collected value) `==` (threshold value)
* (collected value) `<` (threshold value)
* (collected value) `<=` (threshold value)

### 2. Configuration and Implementation

To use URI Statistics Alarms, MYSQL table `pinot_alarm_history`, `pinot_alarm_rule`, and `pinot_webhook_send` need to be added.

```
CREATE TABLE `pinot_alarm_history` (
  `history_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `rule_id` int(10) unsigned NOT NULL,
  `timestamp` datetime NOT NULL,
  PRIMARY KEY (`history_id`)
);
```

```
CREATE TABLE `pinot_alarm_rule` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `service_name` varchar(30) NOT NULL,
  `application_name` varchar(30) NOT NULL,
  `category_name` varchar(30) NOT NULL,
  `checker_name` varchar(30) NOT NULL,
  `target` varchar(256) NOT NULL,
  `condition` varchar(30) NOT NULL,
  `threshold` decimal(10,2) DEFAULT NULL,
  `baseline` varchar(30) DEFAULT NULL,
  `user_group_id` varchar(30) NOT NULL,
  `sms_send` char(1) DEFAULT NULL,
  `email_send` char(1) DEFAULT NULL,
  `webhook_send` char(1) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
```

```
CREATE TABLE `pinot_webhook_send` (
  `webhook_send_info_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `webhook_id` int(10) unsigned NOT NULL,
  `rule_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`webhook_send_info_id`),
  UNIQUE KEY `webhook_send_info_id_UNIQUE` (`webhook_send_info_id`)
);
```

### 3. How to add alarms on Web UI

(TO BE UPDATED)

## URI 통계 알람

[URI 통계](https://pinpoint-apm.gitbook.io/pinpoint/documents/uri_statistics)를 이용한 알람 기능은 핀포인트 2.6.0에 추가되었습니다. 기존 [핀포인트 알람](https://pinpoint-apm.gitbook.io/pinpoint/documents/alarm)에서와 동일하게 pinpoint-batch 서버가 매 3분동안 지난 5분간의 데이터가 알람 조건을 만족하는 지 체크합니다.

### 1. 설정 가능한 알람

[URI 통계](https://pinpoint-apm.gitbook.io/pinpoint/documents/uri_statistics) 기능으로 수집한 통계값을 사용하여 특정 URI에 대해 아래와 같은 조건으로 알람을 설정할 수 있습니다.

#### 알람 대상 데이터

* APDEX: 해당 URI의 과거 5분 동안의 APDEX 점수 (0.00 \~ 1.00)
* 평균 응답 속도: 해당 URI의 과거 5분 동안의 평균 응답 속도 (ms)
* 최대 응답 속도: 해당 URI의 과거 5분 동안의 최대 응답 속도 (ms)
* 전체 요청 수: 해당 URI의 과거 5분 동안의 전체 request 개수
* 실패 요청 수: 해당 URI의 과거 5분 동안 실패한 request의 개수

#### 알람 조건

새로운 알람을 등록할 때 수집한 값이 지정한 임계값과 비교해서 어떤 조건일 때 알람이 울리는 지 설정하게 됩니다. 다음 비교 연산자 중에서 선택할 수 있고 아래 조건이 만족하면 알람이 울립니다.

* (수집한 값) `>` (설정한 값)
* (수집한 값) `>=` (설정한 값)
* (수집한 값) `==` (설정한 값)
* (수집한 값) `<` (설정한 값)
* (수집한 값) `<=` (설정한 값)

### 2. 설치 및 설정 방법

URI 통계 알람을 사용하기 위해서는 MYSQL table 세 개( `pinot_alarm_history`, `pinot_alarm_rule`, `pinot_webhook_send`)를 추가해야 합니다.

```
CREATE TABLE `pinot_alarm_history` (
  `history_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `rule_id` int(10) unsigned NOT NULL,
  `timestamp` datetime NOT NULL,
  PRIMARY KEY (`history_id`)
);
```

```
CREATE TABLE `pinot_alarm_rule` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `service_name` varchar(30) NOT NULL,
  `application_name` varchar(30) NOT NULL,
  `category_name` varchar(30) NOT NULL,
  `checker_name` varchar(30) NOT NULL,
  `target` varchar(256) NOT NULL,
  `condition` varchar(30) NOT NULL,
  `threshold` decimal(10,2) DEFAULT NULL,
  `baseline` varchar(30) DEFAULT NULL,
  `user_group_id` varchar(30) NOT NULL,
  `sms_send` char(1) DEFAULT NULL,
  `email_send` char(1) DEFAULT NULL,
  `webhook_send` char(1) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
```

```
CREATE TABLE `pinot_webhook_send` (
  `webhook_send_info_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `webhook_id` int(10) unsigned NOT NULL,
  `rule_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`webhook_send_info_id`),
  UNIQUE KEY `webhook_send_info_id_UNIQUE` (`webhook_send_info_id`)
);
```

### 3. 알람 추가하는 법

\[ Web 구현 후 추가 예정]


# Error Analysis

[English](#error_analysis) | [한국어](#1.설치_및_설정_방법)

## Error Analysis

![](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-66f5caa12ca010e28eb6c3e1bce69e98e300ea2f%2Ferror_analysis_01.png?alt=media)

Error Analysis is a new feature introduced in Pinpoint v3.0.0.

The Pinpoint agent collects more detailed exception information and transmits it to the Pinpoint collector via gRPC. The Pinpoint collector then stores this data in Apache Pinot through Apache Kafka. You can view the stored Error Analysis data in the Pinpoint web interface.

## 1. Installation and Configuration Guide

### 1.1. Kafka Installation and Configuration

To store data from the Pinpoint Collector into Pinot, Kafka needs to be installed. If you have already installed Kafka during the [system metric setup](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.2-kafka), you can skip this section.

#### 1.1.1. Kafka Installation

Refer to the [Kafka Quickstart Guide](https://kafka.apache.org/quickstart) for detailed instructions on installing Kafka.

#### 1.1.2. Kafka Topic Creation

You need to create a topic named `exception-trace`. Use the following command to create the `exception-trace` topic:

```shell
$ bin/kafka-topics.sh --create --topic exception-trace --bootstrap-server ${YOUR_KAFKA_SERVER_ADDRESS}
```

### 1.2. Pinot Installation and Configuration

To store collected data, Pinot must be installed. If you have already completed the Pinot installation during the [system metric setup](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.1.a.-pinot), you can skip this section.

#### 1.2.1. Pinot Installation

Refer to the [Pinot Getting Started Guide](https://docs.pinot.apache.org/basics/getting-started) for detailed instructions on installing Pinot. Pinot can be set up in various environments (local, Docker, Kubernetes), so follow the guide that best fits your setup.

Pinpoint Error Analysis requires [CLP (Compressed Log Processor)](https://docs.pinot.apache.org/basics/data-import/clp), supported from Pinot version 1.0.0, to appropriately process and group error messages. Please ensure you are using the correct version.

Due to the binary issue with `clp-ffi-java`, we recommend using an amd64-based / x86-based machine when installing Pinot version 1.0.0. [Related Issue](https://github.com/pinpoint-apm/pinpoint/issues/11170)

#### 1.2.2. Pinot Table Schema and Table Creation

Create the following table in Pinot:

* `exceptionTrace`

Refer to the [table schema file](https://github.com/pinpoint-apm/pinpoint/tree/master/exceptiontrace/exceptiontrace-common/src/main/pinot) for details on creating the table.

### 1.3. Pinpoint Agent Configuration

This section covers the settings related to Error Analysis data collection. The default settings for the release profile are as follows:

```config
###########################################################
# Exception Trace
###########################################################
profiler.exceptiontrace.enable=true
# Permits per second
profiler.exceptiontrace.new.throughput=1000
profiler.exceptiontrace.errormessage.max=2048
# Permits depth of exception. if max depth is 0, it is unlimited.
profiler.exceptiontrace.max.depth=5
profiler.exceptiontrace.io.buffering.buffersize=20
```

* `profiler.exceptiontrace.enable`
  * `true`: Collects exceptions that occur. **Default**
  * `false`: Does not collect exceptions that occur.
* `profiler.exceptiontrace.new.throughput`
  * **Default**: `1000`
  * Determines how many exceptions per second to collect from the agent.
* `profiler.exceptiontrace.errormessage.max`
  * **Default**: `2048`
  * Determines the maximum length of the error message for exceptions collected by the agent.
* `profiler.exceptiontrace.max.depth`
  * **Default**: `5`
  * Determines the depth to traverse the exception chain.
  * If the value is 0, it will traverse until `Throwable.getCause()` returns null.
* `profiler.exceptiontrace.io.buffering.buffersize`
  * **Default**: `20`
  * Determines the number of exceptions to buffer.
  * This buffer is approximately the size of the buffer generated per Span.

### 1.4. Pinpoint Collector and Web Configuration and Execution

#### 1.4.1. Collector Configuration and Execution

The collector configuration is basically the same as for system metrics. Refer to the [Pinpoint Metric Collector](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.3-collector) documentation for detailed setup instructions.

In addition to setting the addresses for Pinot and Kafka and enabling metric collection, ensure that `pinpoint.modules.collector.exceptiontrace.enabled=true` is set to enable exception storage. **Default**: `true`

#### 1.4.2. Web Configuration and Execution

The web configuration is essentially the same as for system metrics. Refer to the [Pinpoint Metric Web](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.4-web) documentation for detailed setup instructions.

Additionally, ensure that `pinpoint.modules.web.exceptiontrace.enabled=true` is set to enable reading exception data. **Default**: `true`

For Error Analysis, the following setting is added to `pinpoint-web-metric.properties` to control whether the Error Analysis item is displayed in the side menu. **Default**: `true`

```config
config.show.exceptionTrace=true
```

***

## Error Analysis

Error Analysis 는 핀포인트 v3.0.0 에 신규로 추가되었다. 핀포인트 에이전트에서 보다 상세한 Exception 정보를 수집하여 gRPC 를 통해 핀포인트 콜렉터로 전달한다. 핀포인트 콜렉터는 이를 아파치 카프카를 통해 아파치 피노에 값을 저장한다. 핀포인트 웹에서 저장된 Error Analysis 를 확인할 수 있다.

## 1. 설치 및 설정 방법

### 1.1. 카프카 Kafka 설치 및 설정

핀포인트 콜렉터에서 피노Pinot 에 데이터를 저장하기 위해서는 카프카를 설치해야한다. 이미 [시스템 메트릭 설정](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.2-kafka) 과정 중에 카프카를 설치하였다면, 이 부분은 건너뛴다.

#### 1.1.1. 카프카 Kafka 설치

[설치 방법 가이드](https://kafka.apache.org/quickstart)를 참고하여 kafka를 설치한다.

#### 1.1.2. 카프카 Kafka 토픽 생성

`exception-trace` 라는 이름의 topic 을 생성해야 한다. 아래와 같이 `exception-trace` 토픽을 생성한다.

```shell
$ bin/kafka-topics.sh --create --topic exception-trace --bootstrap-server ${YOUR_KAFKA_SERVER_ADDRESS}
```

### 1.2. 피노 Pinot 설치 및 설정

수집된 데이터를 저장하기 위해서는 피노 Pinot 를 설치해야한다. 이미 [시스템 메트릭 설정](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.1.a.-pinot) 과정 중에 피노를 설치하였다면, 이 부분은 건너뛴다.

#### 1.2.1. 피노 Pinot 설치

[피노 설치 가이드](https://docs.pinot.apache.org/basics/getting-started)를 참고하여 피노를 설치한다. 다양한 환경 (local, docker, kubernetes)에서 피노 실행 환경을 구성할 수 있으니 위 가이드를 참고하자.

핀포인트는 Error Message 를 적절히 처리하고 그룹화하기 위해 Pinot 1.0.0 부터 지원하는 [CLP (Compressed Log Processor)](https://docs.pinot.apache.org/basics/data-import/clp) 가 필요하다. 버전에 주의할 것.

#### 1.2.2. 피노 Pinot 테이블 스키마 및 테이블 생성

피노 Pinot 에 다음 테이블을 새로 생성한다.

* `exceptionTrace` [테이블 생성 스키마 파일](https://github.com/pinpoint-apm/pinpoint/tree/master/exceptiontrace/exceptiontrace-common/src/main/pinot)의 테이블 정보를 참고하여 생성한다.

### 1.3 핀포인트 에이전트 설정

Error Analysis 데이터 수집과 관련된 설정이다. release 프로필의 기본 설정은 다음과 같다.

```config
###########################################################
# Exception Trace
###########################################################
profiler.exceptiontrace.enable=true
# Permits per second
profiler.exceptiontrace.new.throughput=1000
profiler.exceptiontrace.errormessage.max=2048
# Permits depth of exception. if max depth is 0, it is unlimited.
profiler.exceptiontrace.max.depth=5
profiler.exceptiontrace.io.buffering.buffersize=20
```

* `profiler.exceptiontrace.enable`
  * `true`: 발생하는 exception 을 수집한다. **기본값**
  * `false` : 발생하는 exception 을 수집하지 않는다.
* `profiler.exceptiontrace.new.throughput`
  * **기본값** 1000
  * 해당 에이전트에서 초당 몇개까지의 exception 을 수집할지 결정한다.
* `profiler.exceptiontrace.errormessage.max`
  * **기본값** 2048
  * 해당 에이전트에서 발생하는 exception 의 error message 를 몇자까지 수집할지 결정한다.
* `profiler.exceptiontrace.max.depth`
  * **기본값** 5
  * exception chain 이 주어졌을 때, 깊이를 어느정도 순회할지 결정한다.
  * 값이 0이면 Throwable.getCause() 가 null 일 때까지 순회한다.
* `profiler.exceptiontrace.io.buffering.buffersize`
  * **기본값** 20
  * buffer 에 exception 을 몇개까지 쌓아둘지 결정한다.
  * 해당 buffer 는 대략 Span 단위로 생성되는 buffer 이다.

### 1.4 핀포인트 콜렉터와 핀포인트 웹 설정 및 실행

### 1.4.1. collector 설정 및 실행

collector 설정은 기본적으로 system metric 와 동일하다. [핀포인트 메트릭 콜렉터](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.3-collector)를 설명한 문서에 자세한 설명이 있으니 참고해서 메트릭 콜렉터 설정값을 세팅하자.

이처럼 pinot 과 kafka 의 주소를 알려주고 metric 수집 기능을 활성화하면 된다.

이에 추가적으로 `pinpoint.modules.collector.exceptiontrace.enabled=true` 로 되어있어야 exception 을 저장한다. **기본값** `true`

### 1.4.2 web 설정 및 실행

web 설정은 기본적으로 system metric 와 동일하다. [핀포인트 메트릭 웹](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.4-web)을 설명한 문서에 자세한 설명이 있으니 참고해서 메트릭 웹 설정값을 세팅하자.

이에 추가적으로 `pinpoint.modules.web.exceptiontrace.enabled=true` 로 되어있어야 exception 데이터를 읽어온다. **기본값** `true`

위 설정 외에 Error Analysis 를 위해 pinpoint-web-metric.properties에 아래 설정값이 추가되었다: 이 설정은 좌측 사이드 메뉴에서 Error Analysis 항목을 노출시킬지 결정한다. **기본값**`true`

* ```
    config.show.exceptionTrace=true
  ```


# How to use Application Inspector

[English](#application-inspector) | [한국어](#application-inspector-1)

## Application Inspector

### 1. Introduction

Application inspector provides an aggregate view of all the agent's resource data (cpu, memory, tps, datasource connection count, etc) registered under the same application name. A separate view is provided for the application inspector with stat charts similar to the agent inspector.

To access application inspector, click on the application inspector menu on the left side of the screen.

* 1 : application inspector menu, 2 : application stat data

  ![inspector\_view.jpg](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-1db8d686fb94a6f086fd1b0c665759237de98e86%2Finspector_view.jpg?alt=media)

The Heap Usage chart above for example, shows the average(Avg), smallest(Min), greatest(Max) heap usage of the agents registered under the same application name along with the id of the agent that had the smallest/greatest heap usage at a certain point in time. The application inspector also provides other statistics found in the agent inspector in a similar fashion.

![graph.jpg](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-1b9fe2dfc5933f8a6d8dcfee8cf77076489f34c7%2Fgraph.jpg?alt=media)

Application inspector requires [flink](https://flink.apache.org) and [zookeeper](https://zookeeper.apache.org/). Please read on for more detail.

### 2. Architecture

![execute\_flow.jpg](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-67c467a049c249107c3d9f9c23d24c98270ddfd1%2Fexecute_flow.jpg?alt=media)

**A.** Run a streaming job on [flink](https://flink.apache.org).\
**B.** The taskmanager server is registered to zookeeper as a data node once the job starts.\
**C.** The Collector obtains the flink server info from zookeeper to create a tcp connection with it and starts sending agent data.\
**D.** The flink server aggregates data sent by the Collector and stores them into hbase.

### 3. Configuration

In order to enable application inspector, you will need to do the following and run Pinpoint.

**A.** Create **ApplicationStatAggre** table (refer to [create table script](https://github.com/pinpoint-apm/pinpoint/tree/master/hbase/scripts)), which stores application stat data.

**B.** Configure zookeeper address in [Pinpoint-flink.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/flink/src/main/resources/pinpoint-flink.properties) which will be used to store flink's taskmanager server information.

```
    flink.cluster.enable=true
    flink.cluster.zookeeper.address=YOUR_ZOOKEEPER_ADDRESS
    flink.cluster.zookeeper.sessiontimeout=3000
    flink.cluster.zookeeper.retry.interval=5000
    flink.cluster.tcp.port=19994
```

**C.** Configure job execution type and the number of listeners to receive data from the Collector in [Pinpoint-flink.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/flink/src/main/resources/profiles/release/pinpoint-flink.properties).

* If you are running a flink cluster, set *flink.StreamExecutionEnvironment* to **server**.
* If you are running flink as a standalone, set *flink.StreamExecutionEnvironment* to **local**.

  ```
    flink.StreamExecutionEnvironment=server
  ```

**D.** Configure hbase address in [hbase.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/flink/src/main/resources/profiles/release/hbase.properties) which will be used to store aggregated application data.

```
    hbase.client.host=YOUR_HBASE_ADDRESS
    hbase.client.port=2181
```

**E.** Build [Pinpoint-flink](https://github.com/pinpoint-apm/pinpoint/tree/master/flink) and run the streaming job file created under *target* directory on the flink server.

* The name of the streaming job is `pinpoint-flink-job-{pinpoint.version}.jar`.
* For details on how to run the job, please refer to the [flink website](https://flink.apache.org).
* You must put `spring.profiles.active release` or`spring.profiles.active local` as the job parameter so that the job can refer to the configuration file configured above when running. It must be entered because it uses the spring profile function inside the job to refer to the configuration file.

**F.** Configure zookeeper address in [Pinpoint-Collector.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/collector/src/main/resources/profiles/release/pinpoint-collector.properties) so that the Collector can connect to the flink server.

```
    flink.cluster.enable=true
    flink.cluster.zookeeper.address=YOUR_ZOOKEEPER_ADDRESS
    flink.cluster.zookeeper.sessiontimeout=3000
```

**G.** Enable application inspector in the web-ui by enabling the following configuration in [pinpoint-web.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/pinpoint-web-root.properties).

```
    config.show.applicationStat=true
```

### 4. Monitoring Streaming Jobs

There is a batch job that monitors how Pinpoint streaming jobs are running. To enable this batch job, configure the following files for *Pinpoint-web*.

**batch.properties**

```
batch.flink.server=FLINK_MANGER_SERVER_IP_LIST
# Flink job manager server IPs, separated by ','.
# ex) batch.flink.server=123.124.125.126,123.124.125.127
```

**applicationContext-batch-schedule.xml**

```markup
<task:scheduled-tasks scheduler="scheduler">
    ...
    <task:scheduled ref="batchJobLauncher" method="flinkCheckJob" cron="0 0/10 * * * *" />
</task:scheduled-tasks>
```

If you would like to send alarms in case of batch job failure, you must implement `com.navercorp.pinpoint.web.batch.JobFailMessageSender class` and register it as a Spring bean.

### 5. Others

For more details on how to install and operate flink, please refer to the [flink website](https://flink.apache.org).

## Application Inspector

### 1. 기능 설명

application inspector 기능은 agent들의 리소스 데이터(stat : cpu, memory, tps, datasource connection count)를 집계하여 데이터를 보여주는 기능이다. 참고로 application은 agent의 그룹으로 이뤄진다. 그리고 agent의 리소스 데이터는 agent inspector 화면에서 에서 볼 수 있다. application inspector 기능 또한 별도의 화면에서 확인할 수 있다.

inspector 화면 왼쪽 메뉴의 링크를 클릭하면 application inspector 버튼을 클릭하고 데이터를 볼 수 있다.

* 1 : application inspector menu, 2: application stat data

  ![inspector\_view.jpg](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-1db8d686fb94a6f086fd1b0c665759237de98e86%2Finspector_view.jpg?alt=media)

예를들면 A라는 application에 포함된 agent들의 heap 사용량을 모아서 heap 사용량 평균값 , heap 사용량의 평균값, heap 사용량이 가장 높은 agentid와 사용량, heap 사용량이 가장 적은 agentid와 사용량을 보여준다. 이외에도 agent inspector 에서 제공하는 다른 데이터들도 집계하여 application inspector에서 제공한다.

![graph.jpg](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-1b9fe2dfc5933f8a6d8dcfee8cf77076489f34c7%2Fgraph.jpg?alt=media)

application inspector 기능을 동작시키기 위해서는 [flink](https://flink.apache.org)와 [zookeeper](https://zookeeper.apache.org/)가 필요하고, 기능의 동작 구조와 구성 및 설정 방법을 아래 설명한다.

### 2. 동작 구조

application inspector 기능의 동작 및 구조를 그림과 함께 보자.

![execute\_flow.jpg](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-67c467a049c249107c3d9f9c23d24c98270ddfd1%2Fexecute_flow.jpg?alt=media)

**A.** [flink](https://flink.apache.org)에 streaming job을 실행시킨다.\
**B.** job이 실행되면 taskmanager 서버의 정보가 zookeeper의 데이터 노드로 등록이 된다.\
**C.** Collector는 zookeeper에서 flink 서버의 정보를 가져와서 flink 서버와 tcp 연결을 맺고 agent stat 데이터를 전송한다.\
**D.** flink 서버에서는 agent 데이터를 집계하여 통계 데이터를 hbase에 저장한다.

### 3. 기능 실행 방법

application inspector 기능을 실행하기 위해서 아래와 같이 설정을 변경하고 Pinpoint를 실행해야 한다.

**A.** [테이블 생성 스크립트를 참조](https://github.com/pinpoint-apm/pinpoint/tree/master/hbase/scripts)하여 application 통계 데이터를 저장하는 **ApplicationStatAggre** 테이블을 생성한다.

**B.** flink 프로젝트 설정파일([Pinpoint-flink.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/flink/src/main/resources/profiles/release/pinpoint-flink.properties))에 taskmanager 서버 정보를 저장하는 zookeeper 주소를 설정한다.

```
    flink.cluster.enable=true
    flink.cluster.zookeeper.address=YOUR_ZOOKEEPER_ADDRESS
    flink.cluster.zookeeper.sessiontimeout=3000
    flink.cluster.zookeeper.retry.interval=5000
    flink.cluster.tcp.port=19994
```

**C.** flink 프로젝트 설정파일([Pinpoint-flink.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/flink/src/main/resources/profiles/release/pinpoint-flink.properties))에 job의 실행 방법과 Collector에서 데이터를 받는 listener의 개수를 설정한다.

* flink를 cluster로 구축해서 사용한다면 \_flink.StreamExecutionEnvironment\_에는 **server**를 설정한다.
* flink를 Standalone 형태로 실행한다면 \_flink.StreamExecutionEnvironment\_에는 **local**을 설정한다.

```
    flink.StreamExecutionEnvironment=server
    flink.sourceFunction.Parallel=1
```

**D.** flink 프로젝트 설정파일([hbase.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/flink/src/main/resources/profiles/release/hbase.properties))에 집계 데이터를 저장하는 hbase 주소를 설정한다.

```
    hbase.client.host=YOUR_HBASE_ADDRESS
    hbase.client.port=2181
```

**E.** [flink 프로젝트](https://github.com/pinpoint-apm/pinpoint/tree/master/flink)를 빌드하여 target 폴더 하위에 생성된 streaming job 파일을 flink 서버에 job을 실행한다.

* streaming job 파일 이름은 `pinpoint-flink-job-{pinpoint.version}.jar` 이다.
* 실행방법은 [flink 사이트](https://flink.apache.org)를 참조한다.
* 반드시 실행시 job이 위에서 설정한 설정파일을 참고 할수 있도록 job parameter로 `spring.profiles.active release` or `spring.profiles.active local`를 넣어주야 한다. job 내부에서 spring profile 기능을 사용하여 설정파일을 참고 하고 있기때문에 반드시 입력해야한다.

**F.** Collector에서 flink와 연결을 맺을 수 있도록 설정파일([Pinpoint-Collector.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/collector/src/main/resources/pinpoint-collector.properties))에 zookeeper 주소를 설정한다.

```
    flink.cluster.enable=true
    flink.cluster.zookeeper.address=YOUR_ZOOKEEPER_ADDRESS
    flink.cluster.zookeeper.sessiontimeout=3000
```

**G.** web에서 application inspector 버튼을 활성화 하기 위해서 설정파일(pinpoint-web.properties)을 수정한다.

```
    config.show.applicationStat=true
```

### 4. streaming job 동작 확인 모니터링 batch

Pinpoint streaming job이 실행되고 있는지 확인하는 batch job이 있다. batch job을 동작 시키고 싶다면 Pinpoint web 프로젝트의 설정 파일을 수정하면 된다.

**batch.properties**

```
batch.flink.server=FLINK_MANGER_SERVER_IP_LIST
#`batch.flink.server` 속성 값에 flink job manager 서버 IP를 입력하면 된다. 서버 리스트의 구분자는 ','이다.
# ex) batch.flink.server=123.124.125.126,123.124.125.127
```

**applicationContext-batch-schedule.xml**

```markup
<task:scheduled-tasks scheduler="scheduler">
    ...
    <task:scheduled ref="batchJobLauncher" method="flinkCheckJob" cron="0 0/10 * * * *" />
</task:scheduled-tasks>
```

batch job이 실패할 경우 알람이 전송되도록 기능을 추가 하고싶다면 `com.navercorp.pinpoint.web.batch.JobFailMessageSender class` 구현체를 만들고 bean으로 등록하면 된다.

### 5. 기타

자세한 flink 운영 설치에 대한 내용은 [flink 사이트](https://flink.apache.org)를 참고하자.


# Realtime Request Monitoring

The collection of request information can sometimes be so resource intensive that it can have a serious impact on the target system. Pinpoint provides a number of features that allow this expensive information to be monitored in real time only when the user really needs it.

## Features

The realtime monitor consists of 2 features: recording the number of active requests, thread-dumping the thread handling the active request

### Active request - realtime graph

In the datetime range picker there is a `REAL TIME` button which is focused on automatically augmenting the current data with the just generated realtime data.

![range picker realtime](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-90bd8818e94c54dc52208747339519e4e1432015%2Frange-picker-realtime.png?alt=media)

REAL TIME also activates the Active Requests window. This shows the number of active requests at the moment.

![active requests](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-0308fbfceb32dde0e1c800402eb08e986d1e067b%2Factive-requests.png?alt=media)

### Active request thread dump

Pressing the icon in the green square above navigates to the thread dump view

![thread dump list](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-9675d449afda87c24f809cfc53832bcc4c487d1d%2Fthread-dump.png?alt=media)

The above list view contains brief information about the threads that were handling requests at the time the page was loaded. When the item is selected, the thread dump is collected and displayed in the UI as shown below.

![thread dump detail](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-6d65c35fa41f337f1bc388fae5c5924518f09c8c%2Fthread-dump-detail.png?alt=media)

The thread dump only works if the request is still active, but can be replaced with `There is no message( may be completed)` if the request session is already closed by the time the user selects the item in the list.

## Requirements and installation

These features are **disabled by default** and can be enabled with the property `pinpoint.modules.realtime.enabled=true` at the web, collector module.

### Required properties

Once the feature is enabled, the [Redis](https://redis.io) connection must be provided, which can be configured by adjusting the properties below in \`redis/src/main/resources/redis/profiles'.

Most of the properties below follow, but are not exactly the same as, those defined in the [spring-data-redis](https://spring.io/projects/spring-data-redis) library.

```yaml
spring.data.redis.lettuce.client.io-thread-pool-size=8
spring.data.redis.lettuce.client.computation-thread-pool-size=8
spring.data.redis.lettuce.client.request-queue-size=1024

spring.data.redis.username=default
spring.data.redis.password=

# Standalone mode
spring.data.redis.host=localhost
spring.data.redis.port=6379

# Cluster mode: Cluster mode is prior to standalone
spring.data.redis.cluster.nodes=localhost.1:6379,localhost.2:6379,localhost.3:6379
```

If `spring.data.redis.cluster.nodes` is not empty, `spring.data.redis.host` is ignored.

## Architecture

Real-time information is not collected on a 24-hour basis, but is triggered by some kind of signal from a collector listening to a specific channel for broadcasting the event that a user has accessed that web page (demand). The collected information (supply) is immediately sent to the corresponding channel in Redis and can be read by the web server that sent the demand event.

![redis usage summary](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-0c0b76d5af672d4e0596bbb04cbb8b830fe0a071%2Fredis.drawio.png?alt=media)

### Case: the number of active requests

Most of the specifications for this section are described in `ATCServiceProtocolConfig.java`.

```java
@Bean
FluxChannelServiceProtocol<ATCDemand, ATCSupply> atcProtocol(ObjectMapper objectMapper) {
    return ChannelServiceProtocol.<ATCDemand, ATCSupply>builder()
      ...
            .setDemandPubChannelURIProvider(demand -> URI.create(RedisPubSubConstants.SCHEME + ":demand:atc-2"))
            .setDemandSubChannelURI(URI.create(RedisPubSubConstants.SCHEME + ":demand:atc-2"))
            .setSupplyChannelURIProvider(demand -> URI.create(RedisPubSubConstants.SCHEME + ":supply:atc-2:" + demand.getApplicationName() + ':' + demand.getAgentId() + ':' + demand.getStartTimestamp()))
            .buildFlux();
}
```

As described in the code above, the demand for the number of active requests is communicated over the redis pubsub channel using the key `demand:atc-2`. If real-time is enabled, all collectors should listen to this channel from the start.

A collector can ignore a demand event if it determines that it cannot respond to that event on its own, but you should design your demands carefully so that there is exactly one collector that can respond to the demand.

The appropriate collector with the appropriate connection triggers the agent to gather the required information, which is then passed in real time to the redis pubsub supply channel with the key 'supply:atc-2:{applicationName}:{agentId}:{startTimestamp}'.

![redis request response](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-a50199f131acc73ab44a33b7811108da2b657c60%2Fredis-req-res.drawio.png?alt=media)


# Separate Logging Per Request

## ENGLISH GUIDE

### Per-request logging

#### 1. Description

Pinpoint saves additional information(transactionId, spanId) in log messages to classify them by request.

When tomcat processes multiple requests concurrently, we can see log files printed in chronological order. But we can not classify them by each request. For example when an exception message is logged, we can not easily identify all the logs related to the request that threw the exception.

Pinpoint is able to classify logs by requests by storing additional information(transactionId, spanId) in MDC of each request. The transactionId printed in the log message is the same as the transactionId in Pinpoint Web’s Transaction List view.

Let’s take a look at a more specific example. The log below is from an exception that occurred without using Pinpoint. As you can see, it is hard to identify the logs related to the request that threw the exception. ex) Without Pinpoint

```
2015-04-04 14:35:20 [INFO](ContentInfoCollector:76 ) get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:123 ) get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoCollector:12) get content name : SPORTS
2015-04-04 14:35:20 [INFO](ContentInfoCollector:25 ) get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:56 ) get content name : NATIONAL
2015-04-04 14:35:20 [INFO](ContentInfoCollector:34 ) get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoService:55 ) check authorization of user
2015-04-04 14:35:20 [INFO](ContentInfoService:14 ) get title of content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14 ) execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114 ) execute query ...    
2015-04-04 14:35:20 [INFO](ContentInfoService:74 ) get top linking for content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14 ) execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114 ) execute query ...
2015-04-04 14:35:22 [INFO](ContentDAOImpl:186 ) execute query ...
2015-04-04 14:35:22 [ERROR]ContentDAOImpl:158 )
     com.mysql.jdbc.exceptions.jdbc4.CommunicationsException: Communications link failure
          at example.ContentDAO.executequery(ContentDAOImpl.java:152)
          ...
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at com.mysql.jdbc.ConnectionImpl.<init>(ConnectionImpl.java:787)
          ...
     Caused by: com.mysql.jdbc.exceptions.jdbc4.CommunicationsException:
     Communications link failure The last packet sent successfully to the server was 0 milliseconds ago.
     The driver has not received any packets from the server.    
          at com.mysql.jdbc.ConnectionImpl.createNewIO(ConnectionImpl.java:2181)
          ... 12 more
     Caused by: java.net.ConnectException: Connection refused
          at java.net.PlainSocketImpl.socketConnect(Native Method)
          at java.net.PlainSocketImpl.doConnect(PlainSocketImpl.java:333)
          at java.net.PlainSocketImpl.connectToAddress(PlainSocketImpl.java:195)   
          at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:182)   
          at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:432)   
          at java.net.Socket.connect(Socket.java:529)    
          ...13 more
2015-04-04 14:35:22 [INFO](ContentDAO:145 ) execute query ...
2015-04-04 14:35:20 [INFO](ContentInfoService:38 ) update hits for content
2015-04-04 14:35:20 [INFO](ContentInfoService:89 ) check of user
2015-04-04 14:35:24 [INFO](ContentDAO:146 ) execute query ...
2015-04-04 14:35:25 [INFO](ContentDAO:123 ) execute query ...
```

Pinpoint classifies logs by requests by storing additional information(transactionId, spanId) in MDC of each request. ex) With Pinpoint

```
2015-04-04 14:35:20 [INFO](ContentInfoCollector:76) [txId : agent^14252^17 spanId : 1224] get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:123) [txId : agent^142533^18 spanId : 1231] get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoCollector:12) [txId : agent^142533^19 spanId : 1246] get content name : SPORTS
2015-04-04 14:35:20 [INFO](ContentInfoCollector:25) [txId : agent^142533^20 spanId : 1263] get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:56) [txId : agent^142533^21 spanId : 1265] get content name : NATIONAL
2015-04-04 14:35:20 [INFO](ContentInfoCollector:34) [txId : agent^142533^22 spanId : 1278] get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoService:55) [txId : agent^14252^18 spanId : 1231] check authorization of user
2015-04-04 14:35:20 [INFO](ContentInfoService:14) [txId : agent^14252^17 spanId : 1224] get title of content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14) [txId : agent^14252^17 spanId : 1224] execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114) [txId : agent^142533^19 spanId : 1246] execute query ...    
2015-04-04 14:35:20 [INFO](ContentInfoService:74) [txId : agent^14252^17 spanId : 1224] get top linking for content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14) [txId : agent^142533^18 spanId : 1231] execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114) [txId : agent^142533^21 spanId : 1265] execute query ...
2015-04-04 14:35:22 [INFO](ContentDAOImpl:186) [txId : agent^142533^22 spanId : 1278] execute query ...
2015-04-04 14:35:22 [ERROR](ContentDAOImpl:158) [txId : agent^142533^18 spanId : 1231]
     com.mysql.jdbc.exceptions.jdbc4.CommunicationsException: Communications link failure
          at com.pinpoint.example.dao.ContentDAO.executequery(ContentDAOImpl.java:152)
          ...
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at com.mysql.jdbc.ConnectionImpl.<init>(ConnectionImpl.java:787)   
          ...
     Caused by: com.mysql.jdbc.exceptions.jdbc4.CommunicationsException:
     Communications link failure The last packet sent successfully to the server was 0 milliseconds ago.
     The driver has not received any packets from the server.
          ...
          at com.mysql.jdbc.ConnectionImpl.createNewIO(ConnectionImpl.java:2181)
          ... 12 more
     Caused by: java.net.ConnectException: Connection refused
          at java.net.PlainSocketImpl.socketConnect(Native Method)   
          at java.net.PlainSocketImpl.doConnect(PlainSocketImpl.java:333)
          at java.net.PlainSocketImpl.connectToAddress(PlainSocketImpl.java:195)
          at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:182)
          at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:432)
          at java.net.Socket.connect(Socket.java:529)
          ... 13 more
2015-04-04 14:35:22 [INFO](ContentDAO:145) [txId : agent^14252^17 spanId : 1224] execute query ...
2015-04-04 14:35:20 [INFO](ContentInfoService:38) [txId : agent^142533^19 spanId : 1246] update hits for content
2015-04-04 14:35:20 [INFO](ContentInfoService:89) [txId : agent^142533^21 spanId : 1265] check of user
2015-04-04 14:35:24 [INFO](ContentDAO:146) [txId : agent^142533^22 spanId : 1278] execute query ...
2015-04-04 14:35:25 [INFO](ContentDAO:123) [txId : agent^14252^17 spanId : 1224] execute query ...
```

The transactionId printed in the log message is the same as the transactionId in Pinpoint Web’s Transaction List view. ![per-request\_feature\_1.jpg](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-740fd5dfd8b1f9c2023c4c78cf1d69226b51c214%2Fper-request_feature_1.jpg?alt=media)

#### 2. How to configure

**2-1 Pinpoint agent configuration**

To enable this feature, set the logging property corresponding to the logging library in use to true in *pinpoint.config*. For example,

ex) pinpoint.config when using log4j

```
###########################################################
# log4j
###########################################################
profiler.log4j.logging.transactioninfo=true
```

ex) pinpoint.config when using log4j2

```
###########################################################
# log4j2 
###########################################################
profiler.log4j2.logging.transactioninfo=true
```

ex) pinpoint.config when using logback

```
###########################################################
# logback
###########################################################
profiler.logback.logging.transactioninfo=true
```

**2-2 log4j, log4j2, logback configuration**

Change the log message format to print the transactionId, and spanId saved in MDC.

ex) log4j : log4j.xml

```markup
Before
<appender name = "console" class= "org.apache.log4j.ConsoleAppender" >
     <layout class = "org.apache.log4j.EnhancedPatternLayout">
          <param name = "ConversionPattern" value= "%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) %m%n" />
     </layout >
</appender >

After
<appender name = "console" class= "org.apache.log4j.ConsoleAppender" >
     <layout class = "org.apache.log4j.EnhancedPatternLayout">
          <param name = "ConversionPattern" value= "%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) [TxId : %X{PtxId} , SpanId : %X{PspanId}] %m%n" />
        </layout >
</appender >
```

ex) log4j2 - log4j2.xml

```markup
Before
<appender>
     <console name="STDOUT" target="SYSTEM_OUT">
          <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) %m%n""/>
     </console>
<appender>

After
<appender>
     <console name="STDOUT" target="SYSTEM_OUT">
          <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) [TxId : %X{PtxId} , SpanId : %X{PspanId}] %m%n""/>
     </console>
<appender>
```

ex) logback : logback.xml

```markup
Before
<appender name = "STDOUT" class= "ch.qos.logback.core.ConsoleAppender" >
     <layout class = "ch.qos.logback.classic.PatternLayout">
          <Pattern >%d{HH:mm} %-5level %logger{36} - %msg%n</Pattern >
     </layout >
</appender >

After
<appender name = "STDOUT" class= "ch.qos.logback.core.ConsoleAppender" >
     <layout class = "ch.qos.logback.classic.PatternLayout">
          <Pattern >%d{HH:mm} %-5level %logger{36} - [TxId : %X{PtxId} , SpanId : %X{PspanId}] %msg%n</Pattern >
     </layout >
</appender >
```

**2-3 Checking log message**

If the per-request logging is correctly configured, the transactionId, and spanId are printed in the log file.

```
2015-04-04 14:35:20 [INFO](ContentInfoCollector:76 ) [txId : agent^14252^17 spanId : 1224] get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:123 ) [txId : agent^142533^18 spanId : 1231] get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoCollector:12) [txId : agent^142533^19 spanId : 1246] get content name : SPORTS
```

#### 3. expose log in Pinpoint web

If you want to add links to the logs in the transaction list view, you should configure and implement the logic as below. Pinpoint Web only adds link buttons - you should implement the logic to retrieve the log message.

If you want to expose your agent’s log messages, please follow the steps below.

**step 1** You should implement a controller that receives transactionId, spanId, transaction\_start\_time as parameters and retrieve the logs yourself. We do not yet provide a way to retrieve the logs.

example)

```java
@RestController
public class Nelo2LogController {

    @RequestMapping(value = "/????")
    public String NeloLogForTransactionId(@RequestParam (value= "transactionId", required=true) String transactionId,
                                            @RequestParam(value= "spanId" , required=false) String spanId,
                                            @RequestParam(value="time" , required=true) long time ) {

          // you should implement the logic to retrieve your agent’s logs.
    }
```

**step 2** In *pinpoint-web.properties* file, set `log.enable` to true, and `log.page.url` to the url of the controller above. The value set in `log.button.name` will show up as the button text in the Web UI.

```
log.enable= true
log.page.url=XXXX.pinpoint
log.button.name= log
```

**step 3** Pinpoint 1.5.0 or later, we improve button to decided enable/disable depending on whether or not being logged. You should implement interceptor for using logging appender to add logic whether or not being logged. you also should create plugin for logging appender internally. Please refer to Pinpoint Profiler Plugin Sample([Link](https://github.com/pinpoint-apm/pinpoint-plugin-sample)). Location added logic of interceptor is method to log for data of LoggingEvent in appender class. you should review your appender class and find method. This is interceptor example.

```
public class AppenderInterceptor implements AroundInterceptor0 {

    private final TraceContext traceContext;

    public AppenderInterceptor(TraceContext traceContext) {
        this.traceContext = traceContext;
    }

    @Override
    public void before(Object target) {
        Trace trace = traceContext.currentTraceObject();

        if (trace != null) {
            SpanRecorder recorder = trace.getSpanRecorder();
            recorder.recordLogging(LoggingInfo.LOGGED);
        }
    }

    @IgnoreMethod
    @Override
    public void after(Object target, Object result, Throwable throwable) {

    }
}
```

If those are correctly configured, the buttons are added in the transaction list view. ![per-request\_feature\_2.jpg](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-3ce49da1cdfd63c7208ec92142b21950c2bff409%2Fper-request_feature_2.jpg?alt=media)

For details in how the log buttons are generated, please refer to Pinpoint Web’s BusinessTransactionController and ScatterChartController.

## 한국어 가이드

### Per-request logging

#### 1. 기능 설명

Pinpoint에서는 log message를 request 단위로 구분할 수 있도록 log message 에 추가정보를 저장해준다.

다수의 요청을 처리하는 tomcat을 사용할 경우 로그 파일을 보면 시간순으로 출력된 로그를 확인할 수 있다. 그러나 동시에 요청된 다수의 request 각각에 대한 로그를 구분 해서 볼 수 없다. 예를 들어 로그에서 exception message가 출력됐을 때 그 exception이 발생한 request의 모든 log를 확인하기 힘들다.

Pinpoint는 log message 마다 request와 연관된 정보(transactionId, spanId)를 MDC에 넣어줘서 request 단위로 log message를 구분할 수 있도록 해준다. 로그에 출력된 transactionId는 pinpoint web의 transaction List 화면에 출력된 transactionId와 일치한다.

구체적으로 예를 들어보자. Pinpoint를 사용하지 않았을 때 exception이 발생했을 경우 로그 메시지를 살펴 보자. 요청된 다수의 request 각각을 구분하여 로그를 확인할 수가 없다.

ex) Without Pinpoint

```
2015-04-04 14:35:20 [INFO](ContentInfoCollector:76 ) get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:123 ) get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoCollector:12) get content name : SPORTS
2015-04-04 14:35:20 [INFO](ContentInfoCollector:25 ) get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:56 ) get content name : NATIONAL
2015-04-04 14:35:20 [INFO](ContentInfoCollector:34 ) get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoService:55 ) check authorization of user
2015-04-04 14:35:20 [INFO](ContentInfoService:14 ) get title of content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14 ) execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114 ) execute query ...
2015-04-04 14:35:20 [INFO](ContentInfoService:74 ) get top linking for content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14 ) execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114 ) execute query ...
2015-04-04 14:35:22 [INFO](ContentDAOImpl:186 ) execute query ...
2015-04-04 14:35:22 [ERROR]ContentDAOImpl:158 )
     com.mysql.jdbc.exceptions.jdbc4.CommunicationsException: Communications link failure
          at example.ContentDAO.executequery(ContentDAOImpl.java:152)
          ...
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at com.mysql.jdbc.ConnectionImpl.<init>(ConnectionImpl.java:787)
          ...
     Caused by: com.mysql.jdbc.exceptions.jdbc4.CommunicationsException:
     Communications link failure The last packet sent successfully to the server was 0 milliseconds ago.
     The driver has not received any packets from the server.
          at com.mysql.jdbc.ConnectionImpl.createNewIO(ConnectionImpl.java:2181)
          ... 12 more
     Caused by: java.net.ConnectException: Connection refused
          at java.net.PlainSocketImpl.socketConnect(Native Method)
          at java.net.PlainSocketImpl.doConnect(PlainSocketImpl.java:333)
          at java.net.PlainSocketImpl.connectToAddress(PlainSocketImpl.java:195)
          at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:182)
          at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:432)
          at java.net.Socket.connect(Socket.java:529)
          ...13 more
2015-04-04 14:35:22 [INFO](ContentDAO:145 ) execute query ...
2015-04-04 14:35:20 [INFO](ContentInfoService:38 ) update hits for content
2015-04-04 14:35:20 [INFO](ContentInfoService:89 ) check of user
2015-04-04 14:35:24 [INFO](ContentDAO:146 ) execute query ...
2015-04-04 14:35:25 [INFO](ContentDAO:123 ) execute query ...
```

Pinpoint는 로그 메세지 마다 request와 연관된 정보(transactionId, spanId)를 MDC에 넣어줘서 request 단위로 log message를 구분시켜 준다.

ex) With Pinpoint

```
2015-04-04 14:35:20 [INFO](ContentInfoCollector:76) [txId : agent^14252^17 spanId : 1224] get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:123) [txId : agent^142533^18 spanId : 1231] get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoCollector:12) [txId : agent^142533^19 spanId : 1246] get content name : SPORTS
2015-04-04 14:35:20 [INFO](ContentInfoCollector:25) [txId : agent^142533^20 spanId : 1263] get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:56) [txId : agent^142533^21 spanId : 1265] get content name : NATIONAL
2015-04-04 14:35:20 [INFO](ContentInfoCollector:34) [txId : agent^142533^22 spanId : 1278] get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoService:55) [txId : agent^14252^18 spanId : 1231] check authorization of user
2015-04-04 14:35:20 [INFO](ContentInfoService:14) [txId : agent^14252^17 spanId : 1224] get title of content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14) [txId : agent^14252^17 spanId : 1224] execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114) [txId : agent^142533^19 spanId : 1246] execute query ...
2015-04-04 14:35:20 [INFO](ContentInfoService:74) [txId : agent^14252^17 spanId : 1224] get top linking for content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14) [txId : agent^142533^18 spanId : 1231] execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114) [txId : agent^142533^21 spanId : 1265] execute query ...
2015-04-04 14:35:22 [INFO](ContentDAOImpl:186) [txId : agent^142533^22 spanId : 1278] execute query ...
2015-04-04 14:35:22 [ERROR](ContentDAOImpl:158) [txId : agent^142533^18 spanId : 1231]
     com.mysql.jdbc.exceptions.jdbc4.CommunicationsException: Communications link failure
          at com.pinpoint.example.dao.ContentDAO.executequery(ContentDAOImpl.java:152)
          ...
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at com.mysql.jdbc.ConnectionImpl.<init>(ConnectionImpl.java:787)
          ...
     Caused by: com.mysql.jdbc.exceptions.jdbc4.CommunicationsException:
     Communications link failure The last packet sent successfully to the server was 0 milliseconds ago.
     The driver has not received any packets from the server.
          ...
          at com.mysql.jdbc.ConnectionImpl.createNewIO(ConnectionImpl.java:2181)
          ... 12 more
     Caused by: java.net.ConnectException: Connection refused
          at java.net.PlainSocketImpl.socketConnect(Native Method)
          at java.net.PlainSocketImpl.doConnect(PlainSocketImpl.java:333)
          at java.net.PlainSocketImpl.connectToAddress(PlainSocketImpl.java:195)
          at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:182)
          at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:432)
          at java.net.Socket.connect(Socket.java:529)
          ... 13 more
2015-04-04 14:35:22 [INFO](ContentDAO:145) [txId : agent^14252^17 spanId : 1224] execute query ...
2015-04-04 14:35:20 [INFO](ContentInfoService:38) [txId : agent^142533^19 spanId : 1246] update hits for content
2015-04-04 14:35:20 [INFO](ContentInfoService:89) [txId : agent^142533^21 spanId : 1265] check of user
2015-04-04 14:35:24 [INFO](ContentDAO:146) [txId : agent^142533^22 spanId : 1278] execute query ...
2015-04-04 14:35:25 [INFO](ContentDAO:123) [txId : agent^14252^17 spanId : 1224] execute query ...
```

로그메시지에 출력된 transactionId는 Pinpoint web의 transactionlist의 transactionId와 일치한다. ![per-request\_feature\_1.jpg](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-740fd5dfd8b1f9c2023c4c78cf1d69226b51c214%2Fper-request_feature_1.jpg?alt=media)

#### 2. 설정 방법

**2-1 Pinpoint agent 설정**

Pinpoint를 사용하려면 Pinpoint agent 설정파일(Pinpoint.config)의 logging 설정 값을 true로 변경해야 한다. 사용하는 logging 라이브러리에 해당하는 설정값만 true로 변경하면 된다. 아래 설정에 대한 예시가 있다.

ex) Pinpoint.config - log4j 를 사용할 경우

```
###########################################################
# log4j
###########################################################
profiler.log4j.logging.transactioninfo=true
```

ex) Pinpoint.config - log4j2 를 사용할 경우

```
###########################################################
# log4j2 
###########################################################
profiler.log4j2.logging.transactioninfo=true
```

ex) Pinpoint.config - logback 를 사용할 경우

```
###########################################################
# logback
###########################################################
profiler.logback.logging.transactioninfo=true
```

**2-2 log4j, log4j2, logback 설정 파일 설정**

logging 설정 파일의 log message pattern 설정에 Pinpoint에서 MDC에 저장한 transactionId, spanId값이 출력될수 있도록 설정을 추가하자.

ex) log4j - log4j.xml

```markup
변경 전
<appender name = "console" class= "org.apache.log4j.ConsoleAppender" >
     <layout class = "org.apache.log4j.EnhancedPatternLayout">
          <param name = "ConversionPattern" value= "%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) %m%n" />
     </layout >
</appender >

변경 후
<appender name = "console" class= "org.apache.log4j.ConsoleAppender" >
     <layout class = "org.apache.log4j.EnhancedPatternLayout">
          <param name = "ConversionPattern" value= "%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) [TxId : %X{PtxId} , SpanId : %X{PspanId}] %m%n" />
        </layout >
</appender >
```

ex) log4j2 - log4j2.xml

```markup
변경 전
<appender>
     <console name="STDOUT" target="SYSTEM_OUT">
          <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) %m%n""/>
     </console>
<appender>

변경 후
<appender>
     <console name="STDOUT" target="SYSTEM_OUT">
          <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) [TxId : %X{PtxId} , SpanId : %X{PspanId}] %m%n""/>
     </console>
<appender>
```

ex) logback - logback.xml

```markup
변경 전
<appender name = "STDOUT" class= "ch.qos.logback.core.ConsoleAppender" >
     <layout class = "ch.qos.logback.classic.PatternLayout">
          <Pattern >%d{HH:mm} %-5level %logger{36} - %msg%n</Pattern >
     </layout >
</appender >

변경 후
<appender name = "STDOUT" class= "ch.qos.logback.core.ConsoleAppender" >
     <layout class = "ch.qos.logback.classic.PatternLayout">
          <Pattern >%d{HH:mm} %-5level %logger{36} - [TxId : %X{PtxId} , SpanId : %X{PspanId}] %msg%n</Pattern >
     </layout >
</appender >
```

**2-3 로그 출력 확인**

Pinpoint agent가 적용된 서비스를 동작하여 log message에 아래와 같이 transactionId, spanId 정보가 출력되는것을 확인하면 된다.

```
2015-04-04 14:35:20 [INFO](ContentInfoCollector:76 ) [txId : agent^14252^17 spanId : 1224] get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:123 ) [txId : agent^142533^18 spanId : 1231] get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoCollector:12) [txId : agent^142533^19 spanId : 1246] get content name : SPORTS
```

#### 3. Pinpoint web에서 로그 확인

Pinpoint web의 transaction list 화면에서 log를 출력하는 링크를 제공하고 싶다면 아래와 같이 설정 및 구현을 추가하면 된다. Pinpoint web에서는 버튼 을 추가해주기만 하고 로그를 가져오는 로직은 직접 구현을 해야한다.

로그 메시지를 Pinpoint web에서 보여주기 위해서는 아래와 같이 2가지 step을 따라야 한다.

**step 1** transactionId와 spanId, transaction 시작 시간을 파라미터로 받아서 로그 메시지를 가져오는 controller을 구현해야한다.

example)

```java
@RestController
public class Nelo2LogController {

    @RequestMapping(value = "/XXXX")
    public String NeloLogForTransactionId(@RequestParam (value= "transactionId", required=true) String transactionId,
                                            @RequestParam(value= "spanId" , required=false) String spanId,
                                            @RequestParam(value="time" , required=true) long time ) {

          // you should implement the logic to retrieve your agent’s logs.
    }
```

**step 2** Pinpoint-web.properties 파일에서 버튼을 추가해주는 기능을 활성화 하기 위해서 log.enable의 값을 true로 설정하고 위에서 구현한 controller의 url과 button의 이름을 추가해주자.

```
log.enable=true
log.page.url=XXXX.Pinpoint
log.button.name=log
```

**step 3** pinpoint 1.5 이후 버전부터 log 기록 여부에 따라 log 버튼의 활성화가 결정되도록 개선 됐기 때문에 당신이 사용하는 logging appender의 로깅 메소드에 logging 여부를 저장하는 interceptor를 추가하는 플러그인을 개발해야 한다. 플러그인 개발 방법은 다음 링크를 참고하면 된다([Link](https://github.com/pinpoint-apm/pinpoint-plugin-sample)). interceptor 로직이 추가돼야 하는 위치는 appender class 내에 LoggingEvent 객체의 데이터를 이용하여 로깅을 하는 메소드다. 아래는 interceptor 예제이다.

```
public class AppenderInterceptor implements AroundInterceptor0 {

    private final TraceContext traceContext;

    public AppenderInterceptor(TraceContext traceContext) {
        this.traceContext = traceContext;
    }

    @Override
    public void before(Object target) {
        Trace trace = traceContext.currentTraceObject();

        if (trace != null) {
            SpanRecorder recorder = trace.getSpanRecorder();
            recorder.recordLogging(LoggingInfo.LOGGED);
        }
    }

    @IgnoreMethod
    @Override
    public void after(Object target, Object result, Throwable throwable) {

    }
}
```

위와 같이 설정 및 구현을 추가하고 pinpoint web을 동작시키면 아래와 같이 버튼이 추가 된다. ![per-request\_feature\_2.jpg](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-3ce49da1cdfd63c7208ec92142b21950c2bff409%2Fper-request_feature_2.jpg?alt=media) 로그 버튼을 생성해주는 과정을 보시려면, Pinpoint Web의 BusinessTransactionController 와 ScatterChartController class를 참고하세요.


# Marking Transaction as Fail

## HTTP Status Code with Request Failure. <a href="#http-status-code-with-request-failure" id="http-status-code-with-request-failure"></a>

![overview](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-cf1140a4afb3c0a73333b81a2a20c55ebe2fbaae%2Fhttp-status-code-failure-overview.png?alt=media)

## Pinpoint Configuration

pinpoint.config

```
profiler.http.status.code.errors=5xx, 401, 403, 406
```

Comma separated list of HTTP status codes.

* 1xx: Informational(100 \~ 199).
  * 100: Continue
  * 101: Switching Protocols
* 2xx: Successful(200 \~ 299).
  * 200: OK
  * 201: Created
  * 202: Accepted
  * 203: Non-Authoritative Information
  * 204: No Content
  * 205: Reset Content
  * 206: Partial Content
* 3xx: Redirection(300 \~ 399).
  * 300: Multiple Choices
  * 301: Moved Permanently
  * 302: Found
  * 303: See Other
  * 304: Not Modified
  * 305: Use Proxy
  * 307: Temporary Redirect
* 4xx: Client Error(400 \~ 499).
  * 400: Bad Request
  * 401: Unauthorized
  * 402: Payment Required
  * 403: Forbidden
  * 404: Not Found
  * 405: Method Not Allowed
  * 406: Not Acceptable
  * 407: Proxy Authentication Required
  * 408: Request Time-out
  * 409: Conflict
  * 410: Gone
  * 411: Length Required
  * 412: Precondition Failed
  * 413: Request Entity Too Large
  * 414: Request-URI Too Large
  * 415: Unsupported Media Type
  * 416: Requested range not satisfiable
  * 417: Expectation Failed
* 5xx: Server Error(500 \~ 599).
  * 500: Internal Server Error
  * 501: Not Implemented
  * 502: Bad Gateway
  * 503: Service Unavailable
  * 504: Gateway Time-out
  * 505: HTTP Version not supported

Resources

* <https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html>


# Monitoring Proxy Server

## Proxy monitoring using HTTP headers <a href="#proxy-monitoring-using-http-headers" id="proxy-monitoring-using-http-headers"></a>

It is used to know the elapsed time between proxy and WAS.

![overview](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-257fbee4518c6805487a8e000f6da518440eb974%2Fproxy-http-header-overview.png?alt=media)

## Pinpoint Configuration

pinpoint.config

```
profiler.proxy.http.header.enable=true
```

## Proxy Configuration

### Apache HTTP Server

* <http://httpd.apache.org/docs/2.4/en/mod/mod_headers.html>

Add HTTP header.

```
Pinpoint-ProxyApache: t=991424704447256 D=3775428 i=51 b=49
```

e.g.

httpd.conf

```
<IfModule mod_jk.c>
...
RequestHeader set Pinpoint-ProxyApache "%t %D %i %b"
...
</IfModule>
```

**%t is required value.**

### Nginx

* <http://nginx.org/en/docs/http/ngx_http_core_module.html>
* <http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_set_header>

Add HTTP header.

```
Pinpoint-ProxyNginx: t=1504248328.423 D=0.123
```

e.g.

nginx.conf

```
...
  server {
        listen       9080;
        server_name  localhost;

        location / {
            ...
            set $pinpoint_proxy_header "t=$msec D=$request_time";
            proxy_set_header Pinpoint-ProxyNginx $pinpoint_proxy_header;
        }
  }
...
```

or

```
http {
...

    proxy_set_header Pinpoint-ProxyNginx t=$msec;

...
}
```

**t=$msec is required value.**

### App

Milliseconds since epoch (13 digits) and app information.

Add HTTP header.

```
Pinpoint-ProxyApp: t=1594316309407 app=foo-bar
```

**t=epoch is required value.**


# Upgrade Database Hbase2

### Do you like to use Hbase 2.x for Pinpoint? <a href="#do-you-like-to-use-hbase-2x-for-pinpoint" id="do-you-like-to-use-hbase-2x-for-pinpoint"></a>

Default settings of current releases are for Hbase 1.x.

If you'd like to use Hbase 2.x for Pinpoint database.

check out [Hbase2-module](https://github.com/pinpoint-apm/pinpoint/tree/master/hbase2-module).


# Contribution

Thank you very much for choosing to share your contribution with us. Please read this page to help yourself to the contribution.

Before making first pull-request, please make sure you've signed the [Contributor License Agreement](http://goo.gl/forms/A6Bp2LRoG3). This isn't a copyright - it gives us (Naver) permission to use and redistribute your code as part of the project.

## Making Pull Requests

Apart from trivial fixes such as typo or formatting, all pull requests should have a corresponding issue associated with them. It is always helpful to know what people are working on, and different (often better) ideas may pop up while discussing them. Please keep these in mind before you create a pull request:

* Every new java file must have a copy of the license comment. You may copy this from an existing file.
* Make sure you've tested your code thoroughly. For plugins, please try your best to include integration tests if possible.
* Before submitting your code, make sure any changes introduced by your code does not break the build, or any tests.
* Clean up your commit log into logical chunks of work to make it easier for us to figure out what and why you've changed something. (`git rebase -i` helps)
* Please try best to keep your code updated against the master branch before creating a pull request.
* Make sure you create the pull request against our master branch.
* If you've created your own plugin, please take a look at [plugin contribution guideline](#plugin-contribution-guideline)

## Plugin Contribution Guideline

We welcome your plugin contribution. Currently, we would love to see additional tracing support for libraries such as [Storm](https://storm.apache.org), [HBase](http://hbase.apache.org), as well as profiler support for additional languages (.NET, C++).

### Technical Guide

**For technical guides for developing plug-in,** take a look at our [plugin development guide](https://pinpoint-apm.gitbook.io/pinpoint/documents/plugin-dev-guide), along with [plugin samples](https://github.com/pinpoint-apm/pinpoint-plugin-sample) project to get an idea of how we do instrumentation. The samples will provide you with example codes to help you get started.

### Contributing Plugin

If you want to contribute your plugin, it has to satisfy the following requirements:

1. Configuration key names must start with `profiler.[pluginName]`.
2. At least 1 plugin integration test.

Once your plugin is complete, please open an issue to contribute the plugin as below:

```
Title: [Target Library Name] Plugin Contribution

Link: Plugin Repository URL
Target: Target Library Name
Supported Version: 
Description: Simple description about the target library and/or target library homepage URL

ServiceTypes: List of service type names and codes the plugin adds
Annotations: List of annotation key names and codes the plugin adds
Configurations: List of configuration keys and description the plugin adds.
```

Our team will review the plugin, and your plugin repository will be linked at the third-party plugin list page if everything checks out. If the plugin is for a widely used library, and if we feel confident that we can continuously provide support for it, you may be asked to send us a PR. Should you choose to accept it, your plugin will be merged to the Pinpoint repository.

As much as we'd love to merge all the plugins to the source repository, we do not have the man power to manage all of them, yet. We are a very small team, and we certainly are not experts in all of the target libraries. We feel that it would be better to not merge a plugin if we are not confident in our ability to provide continuous support for it.

To send a PR, you have to modify your plugin like this:

* Fork Pinpoint repository
* Copy your plugin under /plugins directory
* Set parent pom

  ```
    <parent>
        <groupId>com.navercorp.pinpoint</groupId>
        <artifactId>pinpoint-plugins</artifactId>
        <version>Current Version</version>
    </parent>
  ```
* Add your plugin to *plugins/pom.xml* as a sub-module.
* Add your plugin to *plugins/assembly/pom.xml* as a dependency.
* Copy your plugin integration tests under /agent-it/src/test directory.
* Add your configurations to /agent/src/main/resources/\*.config files.
* Insert following license header to all java source files.

  ```
  /*
  * Copyright 2018 Pinpoint contributors and NAVER Corp.
  *
  * Licensed under the Apache License, Version 2.0 (the "License");
  * you may not use this file except in compliance with the License.
  * You may obtain a copy of the License at
  *
  *     http://www.apache.org/licenses/LICENSE-2.0
  *
  * Unless required by applicable law or agreed to in writing, software
  * distributed under the License is distributed on an "AS IS" BASIS,
  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  * See the License for the specific language governing permissions and
  * limitations under the License.
  */
  ```

If you do not want to be bothered with a PR, you may choose to tell us to do it ourselves. However, please note that your contribution will not visible through git history or the Github profile.


# Performance Analysis

## Introduction

Team members of Pinpoint are always aware of performance and stability issues. We've adapted technologies to reduced elements that hinder performance and always carefully examine the codes when there is a plugin pull requests.(plugin codes affects most in performance)

While we have been testing internally everyday for last few years, We've finally had the chance to make the data presentable.

This article doesn't include results compared with other APMs. It's pointless to compare with others due to the difference in collected data. Pinpoint collects massive data to enhance observability as much as possible. But still with minimum impact on the performance

## Test Environment

JVM : 1.8.0\_77 (G1, -Xms4g, -Xmx4g)\
Server : Tomcat\
Database : Cubrid\
Stress test generator : [NGrinder](https://github.com/pinpoint-apm/ngrinder)

## Test Result

![Test Result](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-6b556e592a22322d6fc454605726a1bc5d1b6690%2F20191022_performance.png?alt=media)

*off : non traced*\
on-20 : trace 5% transaction using thrift\
\&#xNAN;*grpc-on-20 : trace 5% transaction using grpc*\
on-1 : trace 100% transaction using thrift\
\*grpc-on-1 : trace 100% transaction using grpc

**Test result shows that Pinpoint affects less than 3% in performance and memory**\
**TPS is effected by various reasons, which may not always be exact**\
**gRPC is little slow than thrift in this test, the performance gap between the two is expected to be reduced, or even more, reversed in v1.9.0 release**

## Conclusion

Pinpoint is already being used in dozens of global companies in the world. With right environment and configuration it's been proved to be worthy. We believe most of the services can spare their 3% of resource to gain high observability with Pinpoint.

## Check List

If you still have low performance issue due to Pinpoint. Here are several items to check in advance.

1. Check the default log option for Pinpoint-Agent (Default was `DEBUG` prior to v1.8.1)
2. JVM option
   * use G1 for the GC Type
   * fix initial/maximum memory allocation pool with same size. ex) -Xms4g -Xmx4g
3. Change [sampling rate](https://pinpoint-apm.gitbook.io/pinpoint/faq#why-is-only-the-first-some-of-the-requests-traced). Even 1\~2% would be enough if you are dealing big data.

   When certain transaction doesn't bypass database, it may appear that Pinpoint is consuming much more resources than 3%, since instrumentation time is not relative, but absolute. But this phenomenon appears in all APM, not only Pinpoint.

## Reference Data

We run test with various technology stacks. Planning to expand more as we go.\
[Full Result](https://pinpoint-apm.gitbook.io/pinpoint/performance)


# FAQ

[Github issues](https://github.com/pinpoint-apm/pinpoint/issues)\
[Google group](https://groups.google.com/forum/#!forum/pinpoint_user)\
[Gitter](https://gitter.im/naver/pinpoint)

Chinese groups

|                                                                                                  QQ Group: 897594820                                                                                                 |                                                                                                                       DING Group                                                                                                                       |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![QQ Group](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-f9cbff4e99069d1c453f335f53bd198c0db8b640%2Fnaverpinpoint.png?alt=media) | ![DING Group](https://4133784059-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrFjbcyAcLbyLJEp0sVi4%2Fuploads%2Fgit-blob-79e1332a4388413fdf35be2f47822102a0f1b11d%2FNaverPinpoint%E4%BA%A4%E6%B5%81%E7%BE%A4-DING.jpg?alt=media) |

## How do I get the call stack view?

Click on a server node, which will populate the scatter chart on the right. This chart shows all succeeded/failed requests that went through the server. If there are any requests that spike your interest, simply **drag on the scatter chart** to select them. This will bring up the call stack view containing the requests you've selected.

## How do I change agent's log level?

You can change the log level by modifying the agent's *log4j.xml* located in *PINPOINT\_AGENT/lib* directory.

## Why is only the first/some of the requests traced?

There is a sampling rate option in the agent's pinpoint.config file (profiler.sampling.rate). Pinpoint agent samples 1 trace every N transactions if this value was set as N. Changing this value to 1 will allow you to trace every transaction.

## Request count in the Scatter Chart is different from the ones in Response Summary chart. Why is this?

The Scatter Chart data have a second granularity, so the requests counted here can be differentiated by a second interval. On the other hand, the Server Map, Response Summary, and Load Chart data are stored in a minute granularity (the collector aggregates these in memory and flushes them every minute due to performance reasons). For example, if the data is queried from 10:00:30 to 10:05:30, the Scatter Chart will show the requests counted between 10:00:30 and 10:05:30, whereas the server map, response summary, and load chart will show the requests counted between 10:00:00 and 10:05:59.

## How do I delete application name and/or agent id from HBase?

Application names and agent ids, once registered, stay in HBase until their TTL expires (default 1year). You may however delete them proactively using [admin APIs](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/java/com/navercorp/pinpoint/web/controller/AdminController.java) once they are no longer used.

* Remove application name - `/admin/removeApplicationName.pinpoint?applicationName=$APPLICATION_NAME&password=$PASSWORD`
* Remove agent id - `/admin/removeAgentId.pinpoint?applicationName=$APPLICATION_NAME&agentId=$AGENT_ID&password=$PASSWORD`

  Note that the value for the password parameter is what you defined `admin.password` property in *pinpoint-web.properties*. Leaving this blank will allow you to call admin APIs without the password parameter.

## What are the criteria for the application name?

Pinpoint's applicationName doesn't support special characters. such as @,#,$,%,\*. Pinpoint's applicationName only supports \[a-zA-Z0-9], '.', '-', '\_' characters.

## HBase is taking up too much space, which data should I delete first?

Hbase is very scalable so you can always add more region servers if you're running out of space. Shortening the TTL values, especially for **AgentStatV2** and **TraceV2**, can also help (though you might have to wait for a major compaction before space is reclaimed). For details on how to major compact, please refer to [this](https://github.com/pinpoint-apm/pinpoint/blob/master/hbase/scripts/hbase-major-compact-htable.hbase) script.

However, if you **must** make space asap, data in **AgentStatV2** and **TraceV2** tables are probably the safest to delete. You will lose agent statistic data (inspector view) and call stack data (transaction view), but deleting these will not break anything.

Note that deleting **\*MetaData** tables will result in *\*-METADATA-NOT-FOUND* being displayed in the call stack and the only way to "fix" this is to restart all the agents, so it is generally a good idea to leave these tables alone.

## My custom jar application is not being traced. Help!

Pinpoint Agent need an entry point to start off a new trace for a transaction. This is usually done by various WAS plugins (such as Tomcat, Jetty, etc) in which a new trace is started when they receive an RPC request. For custom jar applications, you need to set this manually as the Agent does not have knowledge of when and where to start a trace. You can set this by configuring `profiler.entrypoint` in *pinpoint.config* file.

## Building is failing after new release. Help!

Please remember to run the command `./mvnw clean verify -DskipTests=true` if you've used a previous version before, and replace './mvnw' with './mvnw\.cmd' if you are using Windows.

## How to set java runtime option when using atlassian OSGi

`-Datlassian.org.osgi.framework.bootdelegation=sun.,com.sun.,com.navercorp.*,org.apache.xerces.*`

## Why do I see UI send requests to <https://www.google-analytics.com/collect?>

Pinpoint Web module has google analytics attached which tracks the number and the order of button clicks in the Server Map, Transaction List, and the Inspector View.\
This data is used to better understand how users interact with the Web UI which gives us valuable information on improving Pinpoint Web's user experience. To disable this for any reason, set following option to false in pinpoint-web.properties for your web instance.

```
config.sendUsage=false
```

## I'd like to use Hbase 2.x for Pinpoint.

If you'd like to use Hbase 2.x for Pinpoint database, check out [Hbase2-module](https://github.com/pinpoint-apm/pinpoint/tree/master/hbase2-module).


# Powered by Pinpoint

This page, documents **alphabetical list** of organizations using Pinpoint.

## Sites using Pinpoint

1. Coupang ([www.coupang.com](http://www.coupang.com))
2. Echemi ([www.echemi.com](http://www.echemi.com))
3. HANATOUR ([www.hanatour.com](http://www.hanatour.com))
4. NAVER ([www.naver.com](http://www.naver.com))
5. NHN Entertainment
6. Pikicast ([www.pikicast.com](http://www.pikicast.com))
7. SKPlanet ([www.skplanet.com](http://www.skplanet.com))
8. THE PIRATES([www.tpirates.com](http://www.tpirates.com))
9. Toss ([toss.im](https://toss.im))
10. XLGAMES ([www.xlgames.com](http://www.xlgames.com))

## Naver

Naver Co., Ltd. uses Pinpoint as primary APM. Monitoring 2k+ applications with 10k+ instances. Supports 870k+ tps with only 17 Pinpoint-Collectors. Around 70 billion span chunks are collected per day. Which is equivalent to 10 billion transaction.


# Resources

If you have created informative posts on pinpoint and want the link to be added. Feel free to contact us anytime. We are glad to add more links.

## Resources (KOREAN)

* 유용한 자료를 작성하셨다면 공유부탁드립니다!!!
* [Pinpoint 개발자가 작성한 Pinpoint 기술문서 (helloworld.naver.com)](http://helloworld.naver.com/helloworld/1194202)
* [설치 가이드 동영상 강좌 1 (okjsp 대표 허광남님)](https://www.youtube.com/watch?v=hrvKaEaDEGs)
* [설치 가이드 동영상 강좌 2 (okjsp 대표 허광남님)](https://www.youtube.com/watch?v=fliKPGHGXK4)

## Resources (ENGLISH)

* Anyone who would like to share any document are always welcome
* [Technical Overview of Pinpoint](https://github.com/pinpoint-apm/pinpoint/wiki/Technical-Overview-Of-Pinpoint)
* [Official Docker Repository](https://github.com/pinpoint-apm/pinpoint-docker)
* [Notes on Jetty Plugin for Pinpoint](https://github.com/cijung/Docs/blob/master/JettyPluginNotes.md) ([@cijung](https://github.com/cijung))

## Resources (中文)

* [Pinpoint学习笔记](http://skyao.gitbooks.io/leaning-pinpoint/)：中文资料收集整理和更重要的-中文翻译！
* [Pinpoint - 应用性能管理(APM)平台实践之部署篇](https://sconts.com/11)
* [开源APM工具Pinpoint线上部署](https://www.iqarr.com/2018/02/04/java/pinpoint/pinpoint-deploy/)


# Introduction

[![Maven](https://img.shields.io/github/actions/workflow/status/pinpoint-apm/pinpoint/maven.yml?branch=master\&label=build\&logo=github)](https://github.com/pinpoint-apm/pinpoint/actions?query=workflow%3AMaven)[![codecov](https://codecov.io/gh/pinpoint-apm/pinpoint/branch/master/graph/badge.svg)](https://codecov.io/gh/pinpoint-apm/pinpoint)

**Pinpoint** is an APM (Application Performance Management) tool for large-scale distributed systems written in Java / [PHP](https://github.com/pinpoint-apm/pinpoint-c-agent). Inspired by [Dapper](http://research.google.com/pubs/pub36356.html), Pinpoint provides a solution to help analyze the overall structure of the system and how components within them are interconnected by tracing transactions across distributed applications.

You should definitely check **Pinpoint** out If you want to

* understand your [application topology](https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/overview) at a glance
* monitor your application in *Real-Time*
* gain code-level visibility to every transaction
* install APM Agents without changing a single line of code
* have minimal impact on the performance (approximately 3% increase in resource usage)

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-a15a27acd3b0d96723a857cf64503b9979c76bfa%2Fss_server-map.png?alt=media)

## Live Demo

* [demo](http://223.130.142.103:8080/main/ApiGateway@SPRING_BOOT/5m?inbound=1\&outbound=4\&wasOnly=false\&bidirectional=false) - Here is a Demo, So that you can take a look at Pinpoint right away.

## Want a quick tour?

* [Overview](https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/overview) / [History](https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/history) / [Tech Details](https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/techdetail) to get to know more about Pinpoint
* [Videos](https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/videos) - Checkout our videos on Pinpoint

{% embed url="<https://youtu.be/U4EwnB34Dus>" %}

## Getting Started

* [Quick-start guide(Lastest Snapshot)](https://pinpoint-apm.gitbook.io/pinpoint/getting-started/quickstart) for simple test run of Pinpoint
* [Installation guide(Lastest Snapshot)](https://pinpoint-apm.gitbook.io/pinpoint/getting-started/installation) for further instructions.

## Google Analytics

The web module has google analytics attached that tracks the number and the order of button clicks in the server map, transaction list, and the inspector view.

This data is used to better understand how users interact with the Web UI which gives us valuable information in improving Pinpoint Web's user experience. To disable this for any reason, set the following option to false in *pinpoint-web.properties* for your web instance.

```
config.sendUsage=false
```

## Is your application created with PHP?

Pinpoint has started to support application written in PHP. [Check-out our php-agent repository](https://github.com/pinpoint-apm/pinpoint-c-agent).

## Looking for place to ask questions?

[Questions and FAQ](https://pinpoint-apm.gitbook.io/pinpoint/faq)

## License

Pinpoint is licensed under the Apache License, Version 2.0. See [LICENSE](https://github.com/pinpoint-apm/pinpoint/blob/master/LICENSE) for full license text.

```
Copyright 2019 NAVER Corp.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```


# What's New

## New Plugins

* Add S3(Simple Storage Service) client plugin #12457
* Update the entry point for kafka stream #12378
* Update kafka plugin for compatibility with kafka 4.x #12376
* Update spring kafka container entry point of kafka plugin #12218
* Update forwarding server call tracking in grpc plugin #12564

## BugFix

* Fix NPE of elasticsearch plugin #12413

***

**From version 3.x, the executable JAR files will be uploaded to Maven Central Repository.**
\
<https://repo1.maven.org/maven2/com/navercorp/pinpoint/>

* [pinpoint-agent-3.0.3.tar.gz](https://repo1.maven.org/maven2/com/navercorp/pinpoint/pinpoint-agent/3.0.3/pinpoint-agent-3.0.3.tar.gz)
* [pinpoint-batch-3.0.3-exec.jar](https://repo1.maven.org/maven2/com/navercorp/pinpoint/pinpoint-batch/3.0.3/pinpoint-batch-3.0.3-exec.jar)
* [pinpoint-collector-3.0.3-exec.jar](https://repo1.maven.org/maven2/com/navercorp/pinpoint/pinpoint-collector/3.0.3/pinpoint-collector-3.0.3-exec.jar)
* [pinpoint-collector-starter-3.0.3-exec.jar](https://repo1.maven.org/maven2/com/navercorp/pinpoint/pinpoint-collector-starter/3.0.3/pinpoint-collector-starter-3.0.3-exec.jar)
* [pinpoint-web-3.0.3-exec.jar](https://repo1.maven.org/maven2/com/navercorp/pinpoint/pinpoint-web/3.0.3/pinpoint-web-3.0.3-exec.jar)
* [pinpoint-web-starter-3.0.3-exec.jar](https://repo1.maven.org/maven2/com/navercorp/pinpoint/pinpoint-web-starter/3.0.3/pinpoint-web-starter-3.0.3-exec.jar)

## What's Changed

* \[#12179] Prepare 3.0.3-SNAPSHOT by @intr3p1d in <https://github.com/pinpoint-apm/pinpoint/pull/12184>
* \[#12218] Backport: Update spring kafka container entry point of kafka… by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12219>
* \[#12220] Backport: Bump ASM from 9.6 to 9.7.1 by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12224>
* \[#12376] Backport: Update kafka plugin for compatibility with kafka 4.x by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12377>
* \[#12378] Backport: Update the entry point for kafka stream by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12380>
* \[#12413] Backport: Fix NPE of elasticsearch plugin by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12414>
* \[#12457] Backport: Add S3(Simple Storage Service) client plugin by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12458>
* \[#12457] Backport: Update s3 client error mark by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12486>
* \[#12564] Backport: Update forwarding server call tracking in grpc plugin by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12565>
* \[#12559] 3.0.3 release by @intr3p1d in <https://github.com/pinpoint-apm/pinpoint/pull/12566>

**Full Changelog**: <https://github.com/pinpoint-apm/pinpoint/compare/v3.0.2...v3.0.3>

## Upgrade consideration

HBase compatibility table:

| Pinpoint Version | HBase 1.x | HBase 2.x                                                                                                             |
| ---------------- | --------- | --------------------------------------------------------------------------------------------------------------------- |
| 2.0.x - 2.2.x    | yes       | [optional](https://pinpoint-apm.gitbook.io/pinpoint/documents/hbase-upgrade#do-you-like-to-use-hbase-2x-for-pinpoint) |
| 2.3.x - 2.5.x    | yes       | [hbase2-module](https://github.com/pinpoint-apm/pinpoint/tree/2.3.x/hbase2-module)                                    |
| 3.0.x            | no        | yes                                                                                                                   |
| 3.1.x            | no        | yes                                                                                                                   |

Agent compatibility to Collector table:

| Agent Version | Collector 2.x.x | Collector 3.0.x | Collector 3.1.x |
| ------------- | --------------- | --------------- | --------------- |
| 2.x.x         | yes             | yes             | yes             |
| 3.0.x         | no              | yes             | yes             |
| 3.1.x         | no              | no              | yes             |

Additionally, the required Java version to run each Pinpoint component is given below:

| Pinpoint Version | Agent | Collector | Web | Batch |
| ---------------- | ----- | --------- | --- | ----- |
| 2.0.x            | 6-13  | 8         | 8   | 8     |
| 2.1.x            | 6-14  | 8         | 8   | 8     |
| 2.2.x            | 7-14  | 8         | 8   | 8     |
| 2.3.x            | 7-17  | 8         | 8   | 8     |
| 2.4.x            | 7-18  | 11        | 11  | 11    |
| 2.5.x            | 8-19  | 11        | 11  | 11    |
| 3.0.x            | 8-21  | 17        | 17  | 17    |
| 3.1.x            | 8-24  | 17        | 17  | 17    |

## Supported Modules

* JDK 6+
* Supported versions of the \* indicated library may differ from the actual version.

| Title                                                                                                          | Instrumented Library                 | Min      | Max       | Comment |   |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------ | -------- | --------- | ------- | - |
| [Tomcat](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/tomcat)                     |                                      | 6.x      | 9.x       |         |   |
| [Jetty](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/jetty)                       |                                      | 8.x      | 9.x       |         |   |
| [JBoss](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/jboss)                       |                                      | 6.x      | 7.x       |         |   |
| [Websphere](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/websphere)               |                                      | 6.x      | 8.x       |         |   |
| [Vertx](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/vertx)                       |                                      | 3.3      | 3.5       |         |   |
| [Weblogic](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/weblogic)                 |                                      | 10.x     | 12.x      |         |   |
| [Undertow](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/undertow)                 |                                      |          |           |         |   |
| [Undertow Servlet](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/undertow-servlet) |                                      |          |           |         |   |
| Jasper                                                                                                         |                                      |          |           |         |   |
|                                                                                                                |                                      |          |           |         |   |
| Java Async Thread                                                                                              |                                      |          |           |         |   |
|                                                                                                                |                                      |          |           |         |   |
| OpenWhisk                                                                                                      | whisk.core                           |          |           |         |   |
|                                                                                                                |                                      |          |           |         |   |
| SpringMVC Framework                                                                                            | spring-webmvc                        | 3.0.7    | 5.3.6     |         |   |
| Spring Web                                                                                                     | spring-web                           | 4.1.2    | 4.3.30    |         |   |
| Spring RabbitMQ                                                                                                | spring-rabbit                        | 1.3.3    | 2.2.16    |         |   |
| Spring IBatis                                                                                                  | spring-ibatis                        | 2.0.7    | 2.0.8     |         |   |
| Spring MyBatis                                                                                                 | mybatis-spring                       | 1.1.0    | 1.3.3     |         |   |
| \*[Spring Boot](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/spring-boot)         | spring-boot-autoconfigure            |          |           |         |   |
| \*[Spring Webflux](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/spring-webflux)   | spring-webflux                       |          |           |         |   |
|                                                                                                                |                                      |          |           |         |   |
| MyBatis                                                                                                        | mybatis                              | 3.0.3    | 3.3.1     |         |   |
| [Hystrix](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/hystrix)                   | hystrix-core                         | 1.4.0    | 1.5.18    |         |   |
|                                                                                                                |                                      |          |           |         |   |
| JDKHTTP                                                                                                        |                                      |          |           |         |   |
| Httpclient3                                                                                                    | commons-httpclient                   | 3.0      | 3.1       |         |   |
| Httpclient4                                                                                                    | httpclient                           | 4.0      | 4.5.4     |         |   |
| Thrift                                                                                                         | libthrift                            | 0.9.1    | 0.14.1    |         |   |
| Google HTTP Client                                                                                             | google-http-client                   | 1.19.0   | 1.39.2    |         |   |
| AsyncHttpClient                                                                                                | async-http-client                    | 1.7.24   | 1.8.17    |         |   |
| OkHttp                                                                                                         | okhttp                               | 2.0.0    | 3.3.1     |         |   |
| Apache HttpAsyncClient                                                                                         | httpasyncclient                      | 4.0      | 4.1.3     |         |   |
| \*Akka HTTP                                                                                                    | akka-http\_2.12                      | 10.1.0   | 10.1.x    |         |   |
| \*[Kafka](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/kafka)                     | kafka-clients                        | 0.11.0.1 |           |         |   |
| GRPC                                                                                                           | grpc-stub                            | 1.8.0    | 1.37.0    |         |   |
| \*[Reactor](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/reactor)                 | reactor-core                         | 3.3.0    | 3.3.1     |         |   |
| \*[Reactor Netty](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/reactor-netty)     | reactor-netty                        | 0.8.0    | 0.9.2     |         |   |
|                                                                                                                |                                      |          |           |         |   |
| Log4j                                                                                                          | log4j                                | 1.2.16   | 1.2.17    |         |   |
| Logback                                                                                                        | logback-classic                      | 1.0.13   | 1.2.3     |         |   |
| Log4j2                                                                                                         | log4j-core                           | 2.0      | 2.12.1    |         |   |
|                                                                                                                |                                      |          |           |         |   |
| \*Arcus                                                                                                        | arcus-java-client                    | 1.7.0    | 1.11.4    |         |   |
| \*MsSQL (jTDS)                                                                                                 | jtds                                 | 1.2.8    |           |         |   |
| \*MsSQL                                                                                                        | mssql-jdbc                           |          |           |         |   |
| HikariCP                                                                                                       | HikariCP-java6                       | 2.3.0    | 2.3.13    |         |   |
| Jackson-mapper-asl                                                                                             | jackson-mapper-asl                   | 1.0.1    | 1.8.11    |         |   |
| Jackson Databind                                                                                               | jackson-databind                     | 2.0.6    | 2.12.3    |         |   |
| MariaDB Connector/J                                                                                            | mariadb-java-client                  | 1.3.0    | 2.7.2     |         |   |
| MongoDB Java Driver                                                                                            | mongodb-driver                       | 3.0.0    | 3.12.8    |         |   |
| Elasticsearch                                                                                                  | elasticsearch-rest-high-level-client | 6.0.0    | 6.8.15    |         |   |
| Datastax Java Driver                                                                                           | cassandra-driver-core                | 2.0.10   | 3.11.0    |         |   |
| Druid                                                                                                          | druid                                | 1.0.0    | 1.2.6     |         |   |
| \*Cubrid                                                                                                       | cubrid-jdbc-driver                   | 8.4.1    | 10.0.0    |         |   |
| \*Commons DBCP                                                                                                 | commons-dbcp                         | 1.0      | 1.4       |         |   |
| \*Commons DBCP2                                                                                                | commons-dbcp2                        | 2.0      | 2.5.0     |         |   |
| \*HBase                                                                                                        | hbase-client                         | 1.2.6.1  | 1.2.6.1   |         |   |
| \*MySQL                                                                                                        | mysql-connector-java                 | 5.0      | 8.x       |         |   |
| \*Oracle JDBC Driver                                                                                           | ojdbc                                |          |           |         |   |
| \*PostgreSQL JDBC Driver                                                                                       | postgresql                           |          |           |         |   |
| \*[Redis](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/redis)                     | jedis                                | 2.4.2    |           |         |   |
| \*[Redis](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/redis-lettuce)             | lettuce-core                         | 5.0.0    | 5.1.2     |         |   |
| \*[Redis](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/redis-redisson)            | redisson                             | 3.10.0   | 3.10.4    |         |   |
|                                                                                                                |                                      |          |           |         |   |
| Apache CXF                                                                                                     | cxf-rt-rs-client                     | 3.0.0    | 3.4.3     |         |   |
| Netty                                                                                                          | netty-all                            | 4.1.0    | 4.1.63    |         |   |
| ActiveMQ                                                                                                       | activemq-all                         | 5.1.0    | 5.16.1    |         |   |
| [RxJAVA](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/rxjava)                     | rxjava                               | 1.0.0    | 1.3.8     |         |   |
| [RabbitMQ](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/rabbitmq)                 | amqp-client                          | 2.7.0    | 5.12.0    |         |   |
| [Paho MQTT](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/paho-mqtt)               | org.eclipse.paho.client.mqttv3       | 1.0.2    | 1.2.5     |         |   |
| [Paho MQTT](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/paho-mqtt)               | org.eclipse.paho.mqttv5.client       | 1.2.5    | 1.2.5     |         |   |
|                                                                                                                |                                      |          |           |         |   |
| Gson                                                                                                           | gson                                 | 1.1      | 2.8.3     |         |   |
| Json                                                                                                           | json-lib                             | 1.0      | 2.2.2     |         |   |
| FastJson                                                                                                       | fastjson                             | 1.2.10   | 1.2.76    |         |   |
| Dubbo                                                                                                          | dubbo                                | 2.5.1    | 2.6.9     |         |   |
| kafka-clients                                                                                                  | kafka-clients                        | 0.11.0.0 | 2.6.1     |         |   |
| postgresql                                                                                                     | postgresql                           | 9.4.1208 | 42.2.19   |         |   |
| ojdbc8                                                                                                         | ojdbc8                               | 12.2.0.1 | 21.1.0.0  |         |   |
| ojdbc10                                                                                                        | ojdbc10                              | 19.3.0.0 | 19.10.0.0 |         |   |


# Overview

Services nowadays often consist of many different components, communicating amongst themselves as well as making API calls to external services. How each and every transaction gets executed is often left as a blackbox. Pinpoint traces transaction flows between these components and provides a clear view to identify problem areas and potential bottlenecks.

* **ServerMap** - Understand the topology of any distributed systems by visualizing how their components are interconnected. Clicking on a node reveals details about the component, such as its current status, and transaction count.
* **Realtime Active Thread Chart** - Monitor active threads inside applications in real-time.
* **Request/Response Scatter Chart** - Visualize request count and response patterns over time to identify potential problems. Transactions can be selected for additional detail by **dragging over the chart**.

![Server Map](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-a15a27acd3b0d96723a857cf64503b9979c76bfa%2Fss_server-map.png?alt=media)

* **CallStack** - Gain code-level visibility to every transaction in a distributed environment, identifying bottlenecks and points of failure in a single view.

![Call Stack](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-735f042f7dc51378efe3f24d2ce53e1f295409d4%2Fss_call-stack.png?alt=media)

* **Inspector** - View additional details on the application such as CPU usage, Memory/Garbage Collection, TPS, and JVM arguments.

![Inspector](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-07c84a62894cf4307ed7dc6ab2f5e44013ca2892%2Fss_inspector.png?alt=media)

## Architecture

![Pinpoint Architecture](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-fc010a909c9559db169703072bd0dccacc283078%2Fpinpoint-architecture.png?alt=media)


# History

Pinpoint is a platform that analyzes large-scale distributed systems and provides a solution to handle large collections of trace data. It has been developed since July 2012 and was launched as an open-source project on January 9, 2015.

This article introduces Pinpoint; it describes what motivated us to start this project, which technologies are used, and how the Pinpoint Agent can be optimized.

> 本文的中文翻译版本 [请见这里](https://github.com/skyao/leaning-pinpoint/blob/master/design/technical_overview.md)

## Motivation to Get Started & Pinpoint Characteristics

Compared to nowadays, the number of Internet users was relatively small and the architecture of Internet services was less complex. Web services were generally configured using a 2-tier (web server and database) or 3-tier (web server, application server, and database) architecture. However, today, supporting a large number of concurrent connections is required and functionalities and services should be organically integrated as the Internet has grown, resulting in much more complex combinations of the software stack. That is n-tier architecture more than 3 tiers has become more widespread. A service-oriented architecture (SOA) or the [microservices](http://en.wikipedia.org/wiki/Microservices) architecture is now a reality.

The system's complexity has consequently increased. The more complex it is, the more difficult you solve problems such as system failure or performance issues. For example, Finding solutions in a 3-tier system is far less complicated. You only need to analyze 3 main components; a web server, an application server, and a database where the number of servers is small. While, if a problem occurs in an n-tier architecture, a large number of components and servers should be investigated. Another problem is that it is difficult to see the big picture only with an analysis of individual components; a low visibility issue is raised. The higher the degree of system complexity is, the longer it takes time to find out the reasons. Even worse, probability increases in which we may not even find them at all.

Such problems have occurred in the systems at NAVER. A variety of tools like Application Performance Management (APM) were used but they were not enough to handle the problems effectively; so we finally ended up developing a new tracing platform for n-tier architecture, which can provide solutions to systems with an n-tier architecture.

Pinpoint, began development in July 2012 and was launched as an open-source project in January 2015, is an n-tier architecture tracing platform for large-scale distributed systems. The characteristics of Pinpoint are as follows:

* Distributed transaction tracing to trace messages across distributed applications
* Automatically detecting the application topology that helps you to figure out the configurations of an application
* Horizontal scalability to support large-scale server group
* Providing code-level visibility to easily identify points of failure and bottlenecks
* Adding a new functionality without code modifications, using the bytecode instrumentation technique


# Tech Details

In this article, we describe the Pinpoint's techniques such as transaction tracing and bytecode instrumentation. And we explain the optimization method applied to Pinpoint Agent, which modifies bytecode and record performance data.

## Distributed Transaction Tracing, Modeled after Google's Dapper

Pinpoint traces distributed requests in a single transaction, modeled after Google's Dapper.

### How Distributed Transaction Tracing Works in Google's Dapper

The purpose of a distributed tracing system is to identify relationships between Node 1 and Node 2 in a distributed system when a message is sent from Node 1 to Node 2 (Figure 1).

![Figure 1. Message relationship in a distributed system](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-9473e149d5d3ec8ddbc00e2c8834478edb9b63d0%2Ftd_figure1.png?alt=media)

Figure 1. Message relationship in a distributed system

The problem is that there is no way to identify relationships between messages. For example, we cannot recognize relationships between N messages sent from Node 1 and N' messages received in Node 2. In other words, when X-th message is sent from Node 1, the X-th message cannot be identified among N' messages received in Node 2. An attempt was made to trace messages at TCP or operating system level. However, implementation complexity was high with low performance because it should be implemented separately for each protocol. In addition, it was difficult to accurately trace messages.

However, a simple solution to resolve such issues has been implemented in Google's Dapper. The solution is to add application-level tags that can be a link between messages when sending a message. For example, it includes tag information for a message in the HTTP header at an HTTP request and traces the message using this tag.

> Google's Dapper
>
> For more information on Google's Dapper, see "[Dapper, a Large-Scale Distributed Systems Tracing Infrastructure](http://research.google.com/pubs/pub36356.html)."

Pinpoint is modeled on the tracing technique of Google's Dapper but has been modified to add application-level tag data in the call header to trace distributed transactions at a remote call. The tag data consists of a collection of keys, which is defined as a TraceId.

### Data Structure in Pinpoint

In Pinpoint, the core of data structure consists of Spans, Traces, and TraceIds.

* Span: The basic unit of RPC (remote procedure call) tracing; it indicates work processed when an RPC arrives and contains trace data. To ensure the code-level visibility, a Span has children labeled SpanEvent as a data structure. Each Span contains a TraceId.
* Trace: A collection of Spans; it consists of associated RPCs (Spans). Spans in the same trace share the same TransactionId. A Trace is sorted as a hierarchical tree structure through SpanIds and ParentSpanIds.
* TraceId: A collections of keys consisting of TransactionId, SpanId, and ParentSpanId. The TransactionId indicates the message ID, and both the SpanId and the ParentSpanId represent the parent-child relationship of RPCs.
  * TransactionId (TxId): The ID of the message sent/received across distributed systems from a single transaction; it must be globally unique across the entire group of servers.
  * SpanId: The ID of a job processed when receiving RPC messages; it is generated when an RPC arrives at a node.
  * ParentSpanId (pSpanId): The SpanId of the parent span which generated the RPC. If a node is the starting point of a transaction, there will not be a parent span - for these cases, we use a value of -1 to denote that the span is the root span of a transaction.

> Differences in terms between Google's Dapper and NAVER's Pinpoint
>
> The term "TransactionId" in Pinpoint has the same meaning as the term "TraceId" in Google's Dapper and the term "TraceId" in Pinpoint refers to a collection of keys.

### How TraceId Works

The figure below illustrates the behavior of a TraceId in which RPCs were made 3 times within 4 nodes.

![Figure 2. Example of a TraceId behavior](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-e40328489e218852c90f58e486f1107fecce2bb7%2Ftd_figure2.png?alt=media)

Figure 2. Example of a TraceId behavior

A TransactionId (TxId) represents that three different RPCs are associated with each other as a single transaction in Figure 2. However, a TransactionId itself can't explicitly describe the relationship between RPCs. To identify the relationships between RPCs, a SpanId and a ParentSpanId (pSpanId) are required. Suppose that a node is Tomcat. You can think of a SpanId as a thread which handles HTTP requests. A ParentSpanId indicates the SpainId of a parent that makes RPC calls.

Pinpoint can find associated n Spans using a TransactionId and can sort them as a hierarchical tree structure using a SpanId and a ParentSpanId.

A SpanId and a ParentSpanId are 64-bit long integers. A conflict might arise because the number is generated arbitrarily, but considering the range of value from -9223372036854775808 to 9223372036854775807, this is unlikely to happen. If there is a conflict between keys, Pinpoint as well as Google's Dapper lets developers know what happened, instead of resolving the conflict.

A TransactionId consists of AgentIds, JVM (Java virtual machine) startup time, and SequenceNumbers.

* AgentId: A user-created ID when JVM starts; it must be globally unique across the entire group of servers where Pinpoint has been installed. The easiest way to make it unique is to use a hostname ($HOSTNAME) because the hostname is not duplicate in general. If you need to run multiple JVMs within the server group, add a postfix to the hostname to avoid duplicates.
* JVM startup time: Required to guarantee a unique SequenceNumber which starts with zero. This value is used to prevent ID conflicts when a user creates duplicate AgentId by mistake.
* SequenceNumber: ID issued by the Pinpoint Agent, with sequentially increasing numbers that start with zero; it is issued per message.

Dapper and [Zipkin](https://github.com/twitter/zipkin), a distributed systems tracing platform at Twitter, generate random TraceIds (TransactionIds in Pinpoint) and consider conflict situations as a normal case. However, we wanted to avoid this conflict as much as possible in Pinpoint. We had two available options for this; one with a method in which the amount of data is small but the probability of conflict is high; the other is a method in which the amount of data is large but the probability of conflict is low; We chose the second option.

There may be a better ways to handle transactions. We came up with several ideas such as key issue by a central key server. But we didn't implement this in the system due to performance issues and network errors. We are still considering issuing keys in bulk as an alternative Solution. So maybe later in the future, such methods can be developed; But for now, a simple method is adopted. In Pinpoint, a TransactionId is regarded as changeable data.

## Bytecode Instrumentation, Not Requiring Code Modifications

Earlier, we explained distributed transaction tracing. One way for implementing this is that developers to modify their code by themselves. Allow developers to add tag information when an RPC is made. However, it could be a burden to modify code even though such functionality is useful to developers.

Twitter's Zipkin provides the functionality of distributed transaction tracing using modified libraries and its container (Finagle). However, it requires the code to be modified if needed. We wanted the functionality to work without code modifications and desired to ensure code-level visibility. To solve such problems, the bytecode instrumentation technique was adopted in Pinpoint. The Pinpoint Agent intervenes code to make RPCs so as to automatically handle tag information.

### Overcoming Disadvantages of Bytecode Instrumentation

There are two ways for distributed transaction tracing as below. Bytecode instrumentation is one of an automatic method.

* Manual method: Developers develop code that records data at important points using APIs provided by Pinpoint.
* Automatic method: Developers do not involve code modifications because Pinpoint decides which API is to be intervened and developed.

Advantages and disadvantages of each method are as follows:

Table 1 Advantages and disadvantage of each method

| Item                  | Advantage                                                                                                                   | Disadvantage                                                                                                                                                                                                                                                                                                                       |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Manual Tracing**    | - Requires less development resources. - An API can become simpler and consequently the number of bugs can be reduced.      | - Developers must modify the code. - Tracing level is low.                                                                                                                                                                                                                                                                         |
| **Automatic Tracing** | - Developers are not required to modify the code. - More precise data can be collected due to more information in bytecode. | - It would cost 10 times more to develop Pinpoint with automatic method. - Requires highly competent developers who can instantly recognize the library code to be traced and make decisions on the tracing points. - Can increase the possibility of a bug due to high-level development skills such as bytecode instrumentation. |

Bytecode instrumentation is a technique that includes high difficulty level and risks. Nevertheless, using this technique has many benefits.

Although it requires a large number of development resources, it requires almost none for applying the service. For example, the following shows the costs between an automatic method which uses bytecode instrumentation and a manual method which uses libraries (in this context, costs are random numbers assumed for clarity).

* Automatic method: Total of 100
  * Cost of Pinpoint development: 100
  * Cost of services applied: 0
* Manual method: Total of 30
  * Cost of Pinpoint development: 20
  * Cost of services applied: 10

The data above tells us that a manual method is more cost-effective than an automatic one. However, it will not guarantee the same result for NAVER since we have thousands of services. For example, if we have 10 services which require being modified, the total cost will be calculated as follows:

* Cost of Pinpoint development 20 + Cost of services applied 10 x 10 services = 120

As you can see, the automatic method was more cost-efficient for us.

We are lucky to have many developers who are highly competent and specialized in Java in the Pinpoint team. Therefore, we believed it was only a matter of time to overcome the technical difficulties in Pinpoint development.

### The Value of Bytecode Instrumentation

The reason we chose to implement bytecode instrumentation(Automatic method) is not only those that we have already explained but also the following points.

#### Hidden API

If the API is exposed for developers to use. We, as API providers, are restricted to modify the API as we desire. Such a restriction can impose stress on us.

We may modify an API to correct mistaken design or add new functions. However, if there is a restriction to do this, it would be difficult for us to improve the API. The best answer for solving such a problem is a scalable system design, which is not an easy option as everyone knows. It is almost impossible to create perfect API design as we can't predict the future.

With bytecode instrumentation, we don't have to worry about the problems caused by exposing the tracing APIs and can continuously improve the design, without considering dependency relationships. For those who are planning to develop their applications using Pinpoint, please note that API can be changed by the Pinpoint developers since improving performance and design is our first priority.

#### Easy to Enable or Disable

The disadvantage of using bytecode instrumentation is that it could affect your applications when a problem occurs in the profiling section of a library or Pinpoint itself. However, you can easily solve it by just disabling the Pinpoint since you don't have to change any code.

You can easily enable Pinpoint for your applications by adding the three lines (associated with the configuration of the Pinpoint Agent) below into your JVM startup script:

```
-javaagent:$AGENT_PATH/pinpoint-bootstrap-$VERSION.jar
-Dpinpoint.agentId=<Agent's UniqueId>
-Dpinpoint.applicationName=<The name indicating a same service (AgentId collection)>
```

If any problem occurs due to Pinpoint, you can just delete the configuration data in the JVM startup script.

### How Bytecode Instrumentation Works

Since bytecode instrumentation technique has to deal with Java bytecode, it tends to increase the risk of development while it decreases productivity. In addition, developers are prone to make mistakes. In Pinpoint, we improved productivity and accessibility by abstraction with the interceptor. Pinpoint injects necessary codes to track distributed transactions and performance information by intervening application code at class loading time. This increases performance since tracking codes are directly injected into the application code.

![Figure 3. Behavior of bytecode instrumentation](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-609a918a392f37fd672a3b18b908c3fe5575abde%2Ftd_figure3.png?alt=media)

Figure 3. Basic principle of bytecode instrumentation

In Pinpoint, the API intercepting part and data recording part are separated. Interceptor is injected into the method that we'd like to track and calls before() and after() methods where data recording is taken care of. Through bytecode instrumentation, Pinpoint Agent can record data only from the necessary method which makes the size of profiling data compact.

## Optimizing Performance of the Pinpoint Agent

Finally, we will describe how to optimize the performance of Pinpoint Agent.

### Using Binary Format (Thrift)

You can increase encoding speed by using a binary format ([Thrift](https://thrift.apache.org/)). Although it is difficult to use and debug, It can improve the efficiency of network usage by reducing the size of data generated.

### Optimize Recorded Data for Variable-Length Encoding and Format

If you convert a long integer into a fixed-length string, the data size will be 8 bytes. However, if you use variable-length encoding, the data size can vary from 1 to 10 bytes depending on the size of a given number. To reduce data size, Pinpoint encodes data as a variable-length string through Compact Protocol of Thrift and records data to be optimized for encoding format. Pinpoint Agent reduces data size by converting remaining time based on root method into a vector value.

> Variable-length encoding
>
> For more information on the variable-length encoding, see "[Base 128 Varints](https://developers.google.com/protocol-buffers/docs/encoding#varints)" in Google Developers.

![Figure 4. Comparison between fixed-length encoding and variable-length encoding](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-4ad3f0fc9dc26c54c3dc86a4851d0261c3252ca6%2Ftd_figure4.png?alt=media)

Figure 4. Comparison between fixed-length encoding and variable-length encoding

As you can see in Figure 4, you need to measure the time of 6 different points to get information of when three different methods are called and finished(Figure 4); With fixed-length encoding, this process requires 48 bytes (6points × 8bytes).

Meanwhile, Pinpoint Agent uses variable-length encoding and records the data according to its corresponding format. And calculate time information on other points with the difference(in vector value) based on the start time of the root method. Since vector value is a small number, it consumes a small number of bytes resulting only 13 bytes consumed rather than 48bytes.

If it takes more time to execute a method, it will increase the number of bytes even though variable-length encoding is used. However, it is still more efficient than fixed-length encoding.

### Replacing Repeated API Information, SQLs, and Strings with Constant Tables

We wanted Pinpoint to enable code-level tracing. However, it had a problem in terms of increasing data size. Every time data with a high degree of precision is sent to a server, due to the size of the data it increased network usage.

To solve such a problem, we adopted a strategy by creating a constant table in a remote HBase server. Since there will be an overload to send data of "method A" to Pinpoint Collector each time, Pinpoint Agent converts "method A" data to an ID and stores this information as a constant table in HBase, and continue tracing data with the ID. When a user retrieves trace data on the Website, the Pinpoint Web searches for the method information of the corresponding ID in the constant table and reorganize them. The same way is used to reduce data size in SQLs or frequently-used strings.

### Handling Samples for Bulk Requests

The requests to online portal services which Naver is providing are huge. A single service handles more than 20 billion requests a day. A simple way to trace such request is by expanding network infrastructure and servers as much as needed to suit the number of requests. However, this is not a cost-effective way to handle such situations.

In Pinpoint, you can collect only sampling data rather than tracking every request. In a development environment where requests are few, every data is collected. While in the production environment where requests are large, only 1\~5% out of whole data is collected which is sufficient to analyze the status of entire applications. With sampling, you can minimize network overhead in applications and reduce costs of infrastructure such as networks and servers.

> Sampling method in Pinpoint
>
> Pinpoint supports a Counting sampler, which collects data only for one of 10 requests if it is set to 10. We plan to add new samplers that can collect data more effectively.

### Minimizing Application Threads Being Aborted Using Asynchronous Data Transfer

Pinpoint does not interfere with application threads since encoded data or remote messages are transferred asynchronously by another thread.

#### Transferring Data via UDP

Unlike Google's Dapper, Pinpoint transfers data through a network to ensure data speed. Sharing network with your service can be an issue when data traffic bursts out. In such situations, the Pinpoint Agent starts to use UDP protocol to give the network connection priority to your service.

> Note
>
> The data transfer APIs can be replaced since it's separated as an interface. It can be changed into an implementation that stores data in a different way, like local files.

## Example of Pinpoint Applied

Here is an example of how to get data from your application so that you can comprehensively understand the contents described earlier.

Figure 5 shows what you can see when you install Pinpoint in TomcatA and TomcatB. You can see the trace data of an individual node as a single transaction, which represents the flow of distributed transaction tracing.

![Figure 5. Example 1: Pinpoint applied](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-f9194d26378f10cc869a147b5bec42932e6bad76%2Ftd_figure5.png?alt=media)

Figure 5. Example of Pinpoint in action

The following describes what Pinpoint does for each method.

1. Pinpoint Agent issues a TraceId when a request arrives at TomcatA.
   * TX\_ID: TomcatA^TIME^1
   * SpanId: 10
   * ParentSpanId: -1(Root)
2. Records data from Spring MVC controllers.
3. Intervene the calls of HttpClient.execute() method and configure the TraceId in HttpGet.
   * Creates a child TraceId.
     * TX\_ID: TomcatA^TIME^1 -> TomcatA^TIME^1
     * SPAN\_ID: 10 -> 20
     * PARENT\_SPAN\_ID: -1 -> 10 (parent SpanId)
   * Configures the child TraceId in the HTTP header.
     * HttpGet.setHeader(PINPOINT\_TX\_ID, "TomcatA^TIME^1")
     * HttpGet.setHeader(PINPOINT\_SPAN\_ID, "20")
     * HttpGet.setHeader(PINPOINT\_PARENT\_SPAN\_ID, "10")
4. Transfer tagged request to TomcatB.
   * TomcatB checks the header from the transferred request.
     * HttpServletRequest.getHeader(PINPOINT\_TX\_ID)
   * TomcatB becomes a child node as it identifies a TraceId in the header.
     * TX\_ID: TomcatA^TIME^1
     * SPAN\_ID: 20
     * PARENT\_SPAN\_ID: 10
5. Records data from Spring MVC controllers and completes the request.

   ![Figure 6. Example 2: Pinpoint applied](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-ea5417ab1e132ffa795122934391fe7f7c1642c1%2Ftd_figure6.png?alt=media)
6. Pinpoint Agent sends trace data to Pinpoint Collector to store it in HBase when the request from TomcatB is completed.
7. After the HTTP calls from TomcatB is terminated, then the request from TomcatA is complete. The Pinpoint Agent sends trace data to Pinpoint Collector to store it in HBase.
8. UI reads the trace data from HBase and creates a call stack by sorting trees.

## Conclusions

Pinpoint is another application that runs along with your applications. Using bytecode instrumentation makes Pinpoint seem like that it does not require code modifications. In general, the bytecode instrumentation technique makes applications vulnerable to risks; if a problem occurs in Pinpoint, it will affect your applications as well. But for now, instead of getting rid of such threats, we are focusing on improving performance and design of Pinpoint. Because we think this makes Pinpoint more valuable. So whether or not to use Pinpoint is for you to decide.

We still have a large amount of work to be done to improve Pinpoint. Despite its incompleteness, Pinpoint was released as an open-source project; we are continuously trying to develop and improve Pinpoint so as to meet your expectations.

> Written by Woonduk Kang
>
> In 2011, I wrote about myself like this—As a developer, I would like to make a software program that users are willing to pay for, like those of Microsoft or Oracle. As Pinpoint was launched as an open-source project, it seems that my dreams somewhat came true. For now, my desire is to make Pinpoint more valuable and attractive to users.


# Videos

## Speaking at COSCUP2019

Speaking at Taiwan's largest open source conference

Title : [Naver, monitoring services with trillions of event with open source APM, Pinpoint](https://coscup.org/2019/en/programs/naver-monitoring-services-with-trillions-of-event-with-open-source-apm-pinpoint)\
Date : Aug 18, 2019

{% embed url="<https://youtu.be/Uyy:CgRc5:M>" %}

### Speaking at HKOSCon2019

Speaking at HongKong's largest open source conference

Title : [How we started an open source APM project and troubleshooting with it](https://hkoscon.org/2019/topics/how-we-started-open-source-apm-project-and-troubleshooting-it)\
Date : June 15, 2019

{% embed url="<https://youtu.be/9-Kf87k4sEA>" %}

## Introduction to Pinpoint v1.5.0

Video introducing Pinpoint

{% embed url="<https://youtu.be/U4EwnB34Dus>" %}


# Additional Plugins

## Third-party agents/plugins

There may be agents, and plugins that are being developed and managed by other individuals/organizations.

Below include agents and plugins that are not merged into this repository.\
Take a look at them if you are interested and would like to help out.

* Plugins
  * Websphere - <https://github.com/sjmittal/pinpoint/tree/cpu_monitoring_fix/plugins/websphere>
  * RocketMQ - <https://github.com/ruizlake/pinpoint/tree/master/plugins/rocketmq>

If you are working on an agent or a plugin and want to add it to this list, please feel free to [contact us](mailto:roy.kim@navercorp.com) anytime.


# Quick-start guide

Pinpoint QuickStart provides a sample TestApp for the Agent.

## Docker

Installing Pinpoint with these docker files will take approximately 10min.

Visit [Official Pinpoint-Docker repository](https://github.com/pinpoint-apm/pinpoint-docker) for more information.

## Installation

To set up your very own Pinpoint instance you can either **download the build results** from our [**latest release**](https://github.com/pinpoint-apm/pinpoint/releases/latest).

### HBase

Download, Configure, and Start HBase - [1. Hbase](https://pinpoint-apm.gitbook.io/pinpoint/installation#1-hbase).

```
$ tar xzvf hbase-x.x.x-bin.tar.gz
$ cd hbase-x.x.x/
$ ./bin/start-hbase.sh
```

See [scripts](https://github.com/pinpoint-apm/pinpoint/tree/master/hbase/scripts) and Run.

```
$ ./bin/hbase shell hbase-create.hbase
```

### Pinpoint Collector

Download, and Start Collector - [3. Pinpoint Collector](https://pinpoint-apm.gitbook.io/pinpoint/installation#3-pinpoint-collector)

```
$ java -jar -Dpinpoint.zookeeper.address=localhost pinpoint-collector-boot-2.2.1.jar
```

### Pinpoint Web

Download, and Start Web - [4. Pinpoint Web](https://pinpoint-apm.gitbook.io/pinpoint/installation#4-pinpoint-web)

```
$ java -jar -Dpinpoint.zookeeper.address=localhost pinpoint-web-boot-2.2.1.jar
```

## Java Agent

### Requirements

In order to build Pinpoint, the following requirements must be met:

* JDK 8 installed

### When Using Released Binary(Recommended)

Download Pinpoint from [Latest Release](https://github.com/pinpoint-apm/pinpoint/releases/latest).

Extract the downloaded file.

```
$ tar xvzf pinpoint-agent-2.2.1.tar.gz
```

Run the JAR file, as follows:

```
$ java -jar -javaagent:pinpoint-agent-2.2.1/pinpoint-bootstrap.jar -Dpinpoint.agentId=test-agent -Dpinpoint.applicationName=TESTAPP pinpoint-quickstart-testapp-2.2.1.jar
```

### When Building Manually

Download Pinpoint with `git clone https://github.com/pinpoint-apm/pinpoint.git` or [download](https://github.com/pinpoint-apm/pinpoint/archive/master.zip) the project as a zip file and unzip.

Change to the pinpoint directory, and build.

```
$ cd pinpoint
$ ./mvnw install -DskipTests=true
```

Change to the quickstart testapp directory, and build. Let's build and run.

```
$ cd quickstart/testapp
$ ./mvnw clean package
```

Change to the pinpoint directory, and run.

```
$ cd ../../
$ java -jar -javaagent:agent/target/pinpoint-agent-2.2.1/pinpoint-bootstrap.jar -Dpinpoint.agentId=test-agent -Dpinpoint.applicationName=TESTAPP quickstart/testapp/target/pinpoint-quickstart-testapp-2.2.1.jar
```

### Get Started

You should see some output that looks very similar to this:

```
  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::        (v2.3.2.RELEASE)

2020-08-06 17:24:59.519  INFO 19236 --- [           main] com.navercorp.pinpoint.testapp.TestApp   : Starting TestApp on AD01160256 with PID 19236 (C:\repository\github\pinpoint\quickstart\testapp\target\classes started by Naver in C:\repository\github\pinpoint)
2020-08-06 17:24:59.520  INFO 19236 --- [           main] com.navercorp.pinpoint.testapp.TestApp   : No active profile set, falling back to default profiles: default
2020-08-06 17:24:59.520 DEBUG 19236 --- [           main] o.s.boot.SpringApplication               : Loading source class com.navercorp.pinpoint.testapp.TestApp
2020-08-06 17:24:59.558 DEBUG 19236 --- [           main] o.s.b.c.c.ConfigFileApplicationListener  : Loaded config file 'file:/C:/repository/github/pinpoint/quickstart/testapp/target/classes/application.yml' (classpath:/application.yml)
2020-08-06 17:24:59.558 DEBUG 19236 --- [           main] ConfigServletWebServerApplicationContext : Refreshing org.springframework.boot.web.servlet.context.AnnotationConfigServletWebServerApplicationContext@46185a1b
08-06 17:24:59.059 [           main] INFO  .n.p.p.DefaultDynamicTransformerRegistry:67  -- added dynamic transformer classLoader: sun.misc.Launcher$AppClassLoader@18b4aac2, className: com.navercorp.pinpoint.testapp.controller.ApisController, registry size: 1
08-06 17:24:59.059 [           main] INFO  .n.p.p.DefaultDynamicTransformerRegistry:67  -- added dynamic transformer classLoader: sun.misc.Launcher$AppClassLoader@18b4aac2, className: com.navercorp.pinpoint.testapp.controller.CallSelfController, registry size: 2
08-06 17:24:59.059 [           main] INFO  .n.p.p.DefaultDynamicTransformerRegistry:67  -- added dynamic transformer classLoader: sun.misc.Launcher$AppClassLoader@18b4aac2, className: com.navercorp.pinpoint.testapp.controller.HttpClient4Controller, registry size: 3
08-06 17:24:59.059 [           main] INFO  .n.p.p.DefaultDynamicTransformerRegistry:67  -- added dynamic transformer classLoader: sun.misc.Launcher$AppClassLoader@18b4aac2, className: com.navercorp.pinpoint.testapp.controller.SimpleController, registry size: 4
08-06 17:24:59.059 [           main] INFO  .n.p.p.DefaultDynamicTransformerRegistry:67  -- added dynamic transformer classLoader: sun.misc.Launcher$AppClassLoader@18b4aac2, className: com.navercorp.pinpoint.testapp.controller.StressController, registry size: 5
2020-08-06 17:25:00.313 DEBUG 19236 --- [           main] .s.b.w.e.t.TomcatServletWebServerFactory : Code archive: C:\Users\Naver\.m2\repository\org\springframework\boot\spring-boot\2.3.2.RELEASE\spring-boot-2.3.2.RELEASE.jar
2020-08-06 17:25:00.313 DEBUG 19236 --- [           main] .s.b.w.e.t.TomcatServletWebServerFactory : Code archive: C:\Users\Naver\.m2\repository\org\springframework\boot\spring-boot\2.3.2.RELEASE\spring-boot-2.3.2.RELEASE.jar
2020-08-06 17:25:00.314 DEBUG 19236 --- [           main] .s.b.w.e.t.TomcatServletWebServerFactory : None of the document roots [src/main/webapp, public, static] point to a directory and will be ignored.
2020-08-06 17:25:00.347  INFO 19236 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 8082 (http)
2020-08-06 17:25:00.355  INFO 19236 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2020-08-06 17:25:00.356  INFO 19236 --- [           main] org.apache.catalina.core.StandardEngine  : Starting Servlet engine: [Apache Tomcat/9.0.37]
```

The last couple of lines here tell us that Spring has started. Spring Boot’s embedded Apache Tomcat server is acting as a webserver and is listening for requests on localhost port 8082. Open your browser and in the address bar at the top enter <http://localhost:8082>


# quickstart.Win.en


# quickstart.Win.ko


# Installation guide

To set up your very own Pinpoint instance you can either **download the build results** from our [**latest release**](https://github.com/pinpoint-apm/pinpoint/releases/latest), or manually build from your Git clone. In order to run your own Pinpoint instance, you will need to run below components:

* **HBase** (for storage)
* **Pinot** (for storage)
* **Pinpoint Collector** (deployed on a web container)
* **Pinpoint Web** (deployed on a web container)
* **Pinpoint Agent** (attached to a java application for profiling)

To try out a simple quickstart project, please refer to the [quick-start guide](https://pinpoint-apm.gitbook.io/pinpoint/getting-started/quickstart).

### Apple silicon(M1/M2) build failures

If an error `protoc-gen-grpc-java-1.49.2-osx-aarch_64.exe: program not found or is not executable` occurs in the Apple silicon Mac (M1/M2) development environment, it has to install Rosetta.

```
$> softwareupdate --install-rosetta --agree-to-license
```

## Quick Overview of Installation

1. HBase ([details](#1-hbase))
   1. Set up HBase cluster - [Apache HBase](http://hbase.apache.org)
   2. Create HBase Schemas - feed `/scripts/hbase-create.hbase` to hbase shell.
2. Pinot ([details](#2-pinot))
   1. Set up Pinot - [Apache Pinot](https://pinot.apache.org)
   2. Set up Kafka - [Apache Kafka](https://kafka.apache.org)
   3. Create Kafka topics and Pinot tables. Refer to the documentation for the features you are using.
      * [New Inspector](https://pinpoint-apm.gitbook.io/pinpoint/documents/new-inspector)
      * [System Metric](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric)
      * [URI Statistics](https://pinpoint-apm.gitbook.io/pinpoint/documents/uri_statistics)
      * [Error Analysis](https://pinpoint-apm.gitbook.io/pinpoint/documents/error_analysis)
3. Build Pinpoint (Optional)([details](#3-building-pinpoint)) - No need if you use the binaries.([here](https://github.com/pinpoint-apm/pinpoint/releases)).\
   4\. Clone Pinpoint - `git clone $PINPOINT_GIT_REPOSITORY`\
   5\. Set JAVA\_HOME environment variable to JDK 8 home directory.\
   6\. Set JAVA\_8\_HOME environment variable to JDK 8 home directory.\
   7\. Set JAVA\_11\_HOME environment variable to JDK 11 home directory.\
   8\. Set JAVA\_17\_HOME environment variable to JDK 17 home directory.\
   9\. Run `./mvnw clean install -DskipTests=true` (or `./mvnw.cmd` for Windows)
4. Pinpoint Collector ([details](#4-pinpoint-collector)) 1. Start *pinpoint-collector-boot-$VERSION.jar* with java -jar command.

   ```
    java -jar -Dpinpoint.zookeeper.address=localhost pinpoint-collector-boot-$VERSION.jar
   ```

   * It will start with default settings. To learn more about default values or how to override them, please see the details below.
   * Use [collector starter](#collector-starter) to connect to Pinot and Kafka
5. Pinpoint Web ([details](#5-pinpoint-web)) 1. Start *pinpoint-web-boot-$VERSION.jar* with java -jar command.

   ```
    java -jar -Dpinpoint.zookeeper.address=localhost pinpoint-web-boot-$VERSION.jar
   ```

   * It will start with default settings. To learn more about default values or how to override them, please see the details below.
   * Use [web starter](#web-starter) to connect to Pinot
6. Pinpoint Agent ([details](#6-pinpoint-agent))
   1. Extract/move *pinpoint-agent/* to a convenient location (`$AGENT_PATH`).
   2. Set `-javaagent:$AGENT_PATH/pinpoint-bootstrap-$VERSION.jar` JVM argument to attach the agent to a java application.
   3. Set `-Dpinpoint.agentId` and `-Dpinpoint.applicationName` command-line arguments.
      * If you're launching an agent in a containerized environment with dynamically changing *agent id*, consider adding `-Dpinpoint.container` command-line argument.
   4. Set `-Dprofiler.sampling.type=PERCENT` and `-Dprofiler.sampling.percent.sampling-rate=100` command-line arguments.
      * You can adjust the sampling rate with the above option.
   5. Launch java application with the options above.

## 1. HBase

Pinpoint uses HBase as its storage backend for the Collector and the Web.

To set up your own cluster, take a look at the [HBase website](http://hbase.apache.org) for instructions. The HBase compatibility table is given below:

Once you have HBase up and running, make sure the Collector and the Web are configured properly and are able to connect to HBase.

### Creating Schemas for HBase

There are 2 scripts available to create tables for Pinpoint: *hbase-create.hbase*, and *hbase-create-snappy.hbase*. Use *hbase-create-snappy.hbase* for snappy compression (requires [snappy](http://google.github.io/snappy/)), otherwise use *hbase-create.hbase* instead.

To run these scripts, feed them into the HBase shell like below:

`$HBASE_HOME/bin/hbase shell hbase-create.hbase`

See [here](https://github.com/pinpoint-apm/pinpoint/tree/master/hbase/scripts) for a complete list of scripts.

## 2. Pinot

Pinpoint uses Pinot for metric data storage,\
and Kafka is required for [Pinot stream ingestion](https://docs.pinot.apache.org/basics/data-import/pinot-stream-ingestion/import-from-apache-kafka)

Here are documents for Installing Pinot and Kafka

* Install Pinot following the instructions in [Pinot Getting Started guide](https://docs.pinot.apache.org/basics/getting-started)
  * Above guide provides instructions for running Pinot locally, in Docker, and in Kubernetes.
* Install Kafka by referring to [Kafka quickstart](https://kafka.apache.org/quickstart)

Once Pinot is up and running, ensure that the [collector starter](#collector-starter) and the [web starter](#web-starter) are properly configured and able to connect to Pinot.

### Creating Pinot tables

Please refer to the documentation to create Kafka topics and Pinot tables for Pinot-related feature.

The descriptions for the required Kafka topics and Pinot tables are provided in the following feature documents

* [New Inspector](https://pinpoint-apm.gitbook.io/pinpoint/documents/new-inspector)
* [System Metric](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric)
* [URI Statistics](https://pinpoint-apm.gitbook.io/pinpoint/documents/uri_statistics)
* [Error Analysis](https://pinpoint-apm.gitbook.io/pinpoint/documents/error_analysis)

## 3. Building Pinpoint

There are two options:

1. Download the build results from our [**latest release**](https://github.com/pinpoint-apm/pinpoint/releases/latest) and skip building process. **(Recommended)**
2. Build Pinpoint manually from the Git clone. **(Optional)**

   In order to do so, the following **requirements** must be met:

   * JDK 8 installed
   * JDK 11 installed
   * JDK 17 installed
   * JAVA\_HOME environment variable set to JDK 8 home directory.
   * JAVA\_8\_HOME environment variable set to JDK 8 home directory.
   * JAVA\_11\_HOME environment variable set to JDK 11 home directory.
   * JAVA\_17\_HOME environment variable set to JDK 17 home directory.

     Agent compatibility to Collector table:

     Once the above requirements are met, simply run the command below (you may need to add permission for **mvnw** so that it can be executed) :

     `./mvnw install -DskipTests=true`

     The default agent built this way will have log level set to DEBUG by default. If you're building an agent for release and need a higher log level, you can set maven profile to *release* when building :\
     `./mvnw install -Prelease -DskipTests=true`

     Note that having multibyte characters in maven local repository path, or any class paths may cause the build to fail.

     The guide will refer to the full path of the pinpoint home directory as `$PINPOINT_PATH`.

Regardless of your method, you should end up with the files and directories mentioned in the following sections.

## 4. Pinpoint Collector

You should have the following **executable jar** file.

*pinpoint-collector-boot-$VERSION.jar*

The path to this file should look like *$PINPOINT\_PATH/collector/target/deploy/pinpoint-collector-boot-$VERSION.jar* if you built it manually.

### Installation

Since Pinpoint Collector is packaged as an executable jar file, you can start Collector by running it directly.

e.g.) `java -jar -Dpinpoint.zookeeper.address=localhost pinpoint-collector-boot-$VERSION.jar`

### Configuration

There are 2 configuration files used for Pinpoint Collector: *pinpoint-collector-grpc.properties*, and *hbase.properties*.

* pinpoint-collector-grpc.properties - contains configurations for the grpc.
  * `collector.receiver.grpc.agent.port` (agent's *profiler.transport.grpc.agent.collector.port*, *profiler.transport.grpc.metadata.collector.port* - default: 9991/TCP)
  * `collector.receiver.grpc.stat.port` (agent's *profiler.transport.grpc.stat.collector.port* - default: 9992/TCP)
  * `collector.receiver.grpc.span.port` (agent's *profiler.transport.grpc.span.collector.port* - default: 9993/TCP)
* hbase.properties - contains configurations to connect to HBase.
  * `hbase.client.host` (default: localhost)
  * `hbase.client.port` (default: 2181)

You may take a look at the full list of default configurations here:

* [pinpoint-collector-grpc.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/collector/src/main/resources/profiles/local/pinpoint-collector-grpc.properties)
* [hbase.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/collector/src/main/resources/profiles/local/hbase.properties)

#### When Building Manually

You can modify default configuration values or add new profiles under `collector/src/main/resources/profiles/`.

#### When Using Released Binary **(Recommended)**

* You can override any configuration values with `-D` option. For example,
  * `java -jar -Dspring.profiles.active=release -Dpinpoint.zookeeper.address=localhost -Dhbase.client.port=1234 pinpoint-collector-boot-$VERSION.jar`
* To import a list of your customized configuration values from a file, you can use `--spring.config.additional-location` option. For example,
  * Create a file `./config/collector.properties`, and list the configuration values you want to override. >

    > spring.profiles.active=release
    >
    > pinpoint.zookeeper.address=localhost
    >
    > collector.receiver.grpc.agent.port=9999
    >
    > collector.receiver.stat.udp.receiveBufferSize=1234567
  * Execute with `java -jar pinpoint-collector-boot-$VERSION.jar --spring.config.additional-location=./config/collector.properties`
* To further explore how to use externalized configurations, refer to [Spring Boot Reference Document](https://docs.spring.io/spring-boot/docs/2.2.x/reference/html/spring-boot-features.html#boot-features-external-config-application-property-files).

### Profiles

Pinpoint Collector provides two profiles: [release](https://github.com/pinpoint-apm/pinpoint/tree/master/collector/src/main/resources/profiles/release) and [local](https://github.com/pinpoint-apm/pinpoint/tree/master/collector/src/main/resources/profiles/local) (default).

To specify which profile to use, configure `spring.profiles.active` value as described in the previous section.

#### Adding a custom profile

To add a custom profile, you need to rebuild `pinpoint-collector` module.

1. Add a new folder under `collector/src/main/resources/profiles` with a profile name.
2. Copy files from local or release profiles folder, and modify configuration values as needed.
3. To use the new profile, rebuild `pinpoint-collector` module and configure `spring.profiles.active` as described in the previous section.

When using released binary, you cannot add a custom profile. Instead, you can manage your configuration values in separate files and use them to override default values as described in the [previous section](#3-pinpoint-collector).

### Collector Starter

To utilize Pinot-related features, you need to execute with Pinpoint Collector starter.

Since the `collector-starter` is packaged as an executable jar file,\
you can start the `collector-starter` with the following command to override Zookeeper, Kafka and Pinot properties.

```
java -jar -Dspring.config.additional-location=collector-starter-application.yml pinpoint-collector-starter-boot-$VERSION.jar
```

* collector-starter-application.yml

```
pinpoint:
  zookeeper:
    address: localhost
  metric:
    kafka:
      bootstrap:
        servers: localhost:19092
spring:
  pinot-datasource:
    pinot:
      jdbc-url: jdbc:pinot://localhost:9000
      username: --username--
      password: --password--
```

## 5. Pinpoint Web

You should have the following **executable jar** file.

*pinpoint-web-boot-$VERSION.jar*

The path to this file should look like *$PINPOINT\_PATH/web/target/deploy/pinpoint-web-boot-$VERSION.jar* if you built it manually.

Pinpoint Web Supported Browsers:

* Chrome

### Installation

Since Pinpoint Web is packaged as an executable jar file, you can start Web by running it directly.

```
java -jar -Dpinpoint.zookeeper.address=localhost pinpoint-web-boot-$VERSION.jar
```

### Configuration

There are 2 configuration files used for Pinpoint Web: *pinpoint-web-root.properties*, and *hbase.properties*.

* hbase.properties - contains configurations to connect to HBase.
  * `hbase.client.host` (default: localhost)
  * `hbase.client.port` (default: 2181)

You may take a look at the default configuration files here

* [pinpoint-web-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/pinpoint-web-root.properties)
* [hbase.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/profiles/release/hbase.properties)
* [pinpoint-web.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/profiles/release/pinpoint-web.properties)

#### When Building Manually

You can modify default configuration values or add new profiles under `web/src/main/resources/profiles/`.

#### When Using Released Binary **(Recommended)**

* You can override any configuration values with `-D` option. For example,
  * `java -jar -Dspring.profiles.active=release -Dpinpoint.zookeeper.address=localhost -Dhbase.client.port=1234 pinpoint-web-boot-$VERSION.jar`
* To import a list of your customized configuration values from a file, you can use `--spring.config.additional-location` option. For example,
  * Create a file `./config/web.properties`, and list the configuration values you want to override. >

    > spring.profiles.active=release
    >
    > pinpoint.zookeeper.address=localhost
    >
    > cluster.zookeeper.sessiontimeout=10000
  * Execute with `java -jar pinpoint-web-boot-$VERSION.jar --spring.config.additional-location=./config/web.properties`
* To further explore how to use externalized configurations, refer to [Spring Boot Reference Document](https://docs.spring.io/spring-boot/docs/2.2.x/reference/html/spring-boot-features.html#boot-features-external-config-application-property-files).

### Profiles

Pinpoint Web provides two profiles: [release](https://github.com/pinpoint-apm/pinpoint/tree/master/web/src/main/resources/profiles/release) (default) and [local](https://github.com/pinpoint-apm/pinpoint/tree/master/web/src/main/resources/profiles/local).

To specify which profile to use, configure `spring.profiles.active` value as described in the previous section.

#### Adding a custom profile

To add a custom profile, you need to rebuild `pinpoint-web` module.

1. Add a new folder under `web/src/main/resources/profiles` with a profile name.
2. Copy files from local or release profiles folder, and modify configuration values as needed.
3. To use the new profile, rebuild `pinpoint-web` module and configure `spring.profiles.active` as described in the previous section.

When using released binary, you cannot add a custom profile. Instead, you can manage your configuration values in separate files and use them to override default values as described in the [previous section](#4-pinpoint-web).

### Web Starter

To utilize Pinot-related features, you need to execute with Pinpoint Web Starter.

Since the `web-starter` is packaged as an executable jar file,\
you can start the `web-starter` with the following command to override Zookeeper and Pinot properties.

```
java -jar -Dspring.config.additional-location=web-starter-application.yml pinpoint-web-starter-boot-$VERSION.jar
```

* web-starter-application.yml

```
pinpoint:
  zookeeper:
    address: localhost
spring:
  pinot-datasource:
    pinot:
      jdbc-url: jdbc:pinot://localhost:9000
      username: --username--
      password: --password--
```

## 6. Pinpoint Agent

If downloaded, unzip the Pinpoint Agent file. You should have a **pinpoint-agent** directory with the layout below :

```
pinpoint-agent
|-- boot
|   |-- pinpoint-annotations-$VERSION.jar
|   |-- pinpoint-bootstrap-core-$VERSION.jar
|   |-- pinpoint-bootstrap-java8-$VERSION.jar
|   |-- pinpoint-bootstrap-java9-$VERSION.jar
|   |-- pinpoint-commons-$VERSION.jar
|-- lib
|   |-- pinpoint-profiler-$VERSION.jar
|   |-- pinpoint-profiler-optional-$VERSION.jar
|   |-- pinpoint-rpc-$VERSION.jar
|   |-- pinpoint-thrift-$VERSION.jar
|   |-- ...
|-- plugin
|   |-- pinpoint-activemq-client-plugin-$VERSION.jar
|   |-- pinpoint-tomcat-plugin-$VERSION.jar
|   |-- ...
|-- profiles
|   |-- local
|   |   |-- pinpoint.config
|   |-- release
|       |-- pinpoint.config
|-- log4j2-agent.xml
|-- pinpoint-bootstrap-$VERSION.jar
|-- pinpoint-root.config
```

The path to this directory should look like *$PINPOINT\_PATH/agent/target/pinpoint-agent* if you built it manually.

You may move/extract the contents of **pinpoint-agent** directory to any location of your choice. The guide will refer to the full path of this directory as `$AGENT_PATH`.

> Note that you may change the agent's log level by modifying the *log4j.xml* located in the *profiles/$PROFILE/log4j.xml* directory above.

Agent compatibility to Collector table:

### Installation

Pinpoint Agent runs as a java agent attached to an application to be profiled (such as Tomcat).

To wire up the agent, pass *$AGENT\_PATH/pinpoint-bootstrap-$VERSION.jar* to the *-javaagent* JVM argument when running the application:

* `-javaagent:$AGENT_PATH/pinpoint-bootstrap-$VERSION.jar`

Additionally, Pinpoint Agent requires 2 command-line arguments in order to identify itself in the distributed system:

* `-Dpinpoint.agentId` - uniquely identifies the application instance in which the agent is running on
* `-Dpinpoint.applicationName` - groups a number of identical application instances as a single service

Note that *pinpoint.agentId* must be globally unique to identify an application instance, and all applications that share the same *pinpoint.applicationName* are treated as multiple instances of a single service.

* `-Dprofiler.sampling.type=PERCENT` - sampler type
* `-Dprofiler.sampling.percent.sampling-rate=100` - support from 100% to 0.01%

If you're launching the agent in a containerized environment, you might have set your *agent id* to be auto-generated every time the container is launched. With frequent deployment and auto-scaling, this will lead to the Web UI being cluttered with all the list of agents that were launched and destroyed previously. For such cases, you might want to add `-Dpinpoint.container` in addition to the 2 required command-line arguments above when launching the agent.

**Tomcat Example**

Add *-javaagent*, *-Dpinpoint.agentId*, *-Dpinpoint.applicationName* to *CATALINA\_OPTS* in the Tomcat startup script (*catalina.sh*).

```
CATALINA_OPTS="$CATALINA_OPTS -javaagent:$AGENT_PATH/pinpoint-bootstrap-$VERSION.jar"
CATALINA_OPTS="$CATALINA_OPTS -Dpinpoint.agentId=$AGENT_ID"
CATALINA_OPTS="$CATALINA_OPTS -Dpinpoint.applicationName=$APPLICATION_NAME"
```

Start up Tomcat to start profiling your web application.

Some application servers require additional configuration and/or may have caveats. Please take a look at the links below for further details.

* [JBoss](https://github.com/pinpoint-apm/pinpoint/tree/master/plugins/jboss#pinpoint-jboss-plugin-configuration)
* [Jetty](https://github.com/pinpoint-apm/pinpoint/blob/master/plugins/jetty/README.md)
* [Resin](https://github.com/pinpoint-apm/pinpoint/tree/master/plugins/resin#pinpoint-resin-plugin-configuration)

### Configuration

There are various configuration options for Pinpoint Agent available in *$AGENT\_PATH/pinpoint-root.config*.

Most of these options are self explanatory, but the most important configuration options you must check are **Collector ip address**, and the **TCP/UDP ports**. These values are required for the agent to establish connection to the *Collector* and function correctly.

Set these values appropriately in *pinpoint-root.config*:

**GRPC**

* `profiler.transport.grpc.collector.ip` (default: 127.0.0.1)
* `profiler.transport.grpc.agent.collector.port` (collector's *collector.receiver.grpc.agent.port* - default: 9991/TCP)
* `profiler.transport.grpc.metadata.collector.port` (collector's *collector.receiver.grpc.agent.port* - default: 9991/TCP)
* `profiler.transport.grpc.stat.collector.port` (collector's *collector.receiver.grpc.stat.port* - default: 9992/TCP)
* `profiler.transport.grpc.span.collector.port` (collector's *collector.receiver.grpc.span.port* - default: 9993/TCP)

You may take a look at the default *pinpoint-root.config* file [here](https://github.com/pinpoint-apm/pinpoint/blob/master/agent/src/main/resources/pinpoint-root.config) along with all the available configuration options.

### Profiles

Add `-Dkey=value` to Java System Properties

* $PINPOINT\_AGENT\_DIR/profiles/$PROFILE
  * `-Dpinpoint.profiler.profiles.active=release or local`
  * Modify `pinpoint.profiler.profiles.active=release` in $PINPOINT\_AGENT\_DIR/pinpoint-root.config
  * Default profile : `release`
* Custom Profile
  1. Create a custom profile in $PINPOINT\_AGENT\_HOME/profiles/MyProfile
     * Add pinpoint.config & log4j.xml
  2. Add `-Dpinpoint.profiler.profiles.active=MyProfile`
* Support external config
  * `-Dpinpoint.config=$MY_EXTERNAL_CONFIG_PATH`

## Miscellaneous

### HBase region servers hostname resolution

Please note that collector/web must be able to resolve the hostnames of HBase region servers. This is because HBase region servers are registered to ZooKeeper by their hostnames, so when the collector/web asks ZooKeeper for a list of region servers to connect to, it receives their hostnames. Please ensure that these hostnames are in your DNS server, or add these entries to the collector/web instances' *hosts* file.

### Routing Web requests to Agents

Starting from 1.5.0, Pinpoint can send requests from the Web to Agents directly via the Collector (and vice-versa). To make this possible, we use Zookeeper to co-ordinate the communication channels established between Agents and Collectors, and those between Collectors and Web instances. With this addition, real-time communication (for things like active thread count monitoring) is now possible.

We typically use the Zookeeper instance provided by the HBase backend so no additional Zookeeper configuration is required. Related configuration options are shown below.

* **Collector** - *pinpoint-collector.properties*
  * `cluster.enable`
  * `cluster.zookeeper.address`
  * `cluster.zookeeper.sessiontimeout`
  * `cluster.listen.ip`
  * `cluster.listen.port`
* **Web** - *pinpoint-web.properties*
  * `cluster.enable`
  * `cluster.web.tcp.port`
  * `cluster.zookeeper.address`
  * `cluster.zookeeper.sessiontimeout`
  * `cluster.zookeeper.retry.interval`
  * `cluster.connect.address`


# Install with Docker

We've create docker files to support docker.\
Installing Pinpoint with these docker files will take approximately 10min. to check out the features of Pinpoint.

Visit [Official Pinpoint-Docker repository](https://github.com/pinpoint-apm/pinpoint-docker) for more information.


# TrobleShooting(Network)

## Checking network configuration

We provide a simple tool that can check your network configurations.\
This tool checks the network status between Pinpoint-Agent and Pinpoint-Collector

## Testing with binary release

If you have downloaded the build results from our [**latest release**](https://github.com/pinpoint-apm/pinpoint/releases/latest).

1. Start your collector server
2. With any terminal that you are using, go to *script* folder which is under *pinpoint-agent-VERSION.tar.gz* package that you have downloaded.

```
> pwd
/Users/user/Downloads/pinpoint-agent-1.7.2-SNAPSHOT/script
```

and run *networktest.sh* shell script

```
> sh networktest.sh
```

You will see some CLASSPATH and configuration you have made in the *pinpoint.config* file as below

```
CLASSPATH=./tools/pinpoint-tools-1.7.2-SNAPSHOT.jar
...Remainder Omitted...
2018-04-10 17:36:30 [INFO ](com.navercorp.pinpoint.bootstrap.config.DefaultProfilerConfig) profiler.enable=true
2018-04-10 17:36:30 [INFO ](com.navercorp.pinpoint.bootstrap.config.DefaultProfilerConfig) profiler.instrument.engine=ASM
2018-04-10 17:36:30 [INFO ](com.navercorp.pinpoint.bootstrap.config.DefaultProfilerConfig) profiler.instrument.matcher.enable=true
...Remainder Omitted...
```

And after that, you will see the results. (In this case, collector server was started locally) If you receive all six SUCCESSes as below, then you are all set and ready to go.

```
UDP-STAT:// localhost
    => 127.0.0.1:9995 [SUCCESS]
    => 0:0:0:0:0:0:0:1:9995 [SUCCESS]

UDP-SPAN:// localhost
    => 127.0.0.1:9996 [SUCCESS]
    => 0:0:0:0:0:0:0:1:9996 [SUCCESS]

TCP:// localhost
    => 127.0.0.1:9994 [SUCCESS]
    => 0:0:0:0:0:0:0:1:9994 [SUCCESS]
```

## Testing with source code

The idea is basically the same.

1. Start your collector server
2. Pass the *path* of the pinpoint.config file as a *program argument* and run ***NetworkAvailabilityChecker*** class.
3. (only for under v1.7.2)For the few who gets JNI error while running. Please remove `<scope>provided</scope>` line from pom.xml under *tools* module and try again

Results should be same as shown above.

> If you face error for v1.7.3 take a look at this [issue](https://github.com/pinpoint-apm/pinpoint/issues/4668)


# Plugin Developer Guide

You can write Pinpoint profiler plugins to extend profiling target coverage. It is highly advisable to look into the trace data recorded by pinpoint plugins before jumping into plugin development.

* There is a [fast auto pinpoint agent plugin generate tool](https://github.com/bbossgroups/pinpoint-plugin-generate) from a 3rd party for creating a simple plug-in, if you'd like to check out.

## I. Trace Data

In Pinpoint, a transaction consists of a group of `Spans`. Each `Span` represents a trace of a single logical node where the transaction has gone through.

To aid in visualization, let's suppose that there is a system like below. The *FrontEnd* server receives requests from users, then sends request to the *BackEnd* server, which queries a DB. Among these nodes, let's assume only the *FrontEnd* and *BackEnd* servers are profiled by the Pinpoint Agent.

![trace](https://user-images.githubusercontent.com/10043788/133535491-adafcd89-c04e-49af-9ad7-f7746bb9c95c.PNG)

When a request arrives at the *FrontEnd* server, Pinpoint Agent generates a new transaction id and creates a `Span` with it. To handle the request, the *FrontEnd* server then invokes the *BackEnd* server. At this point, Pinpoint Agent injects the transaction id (plus a few other values for propagation) into the invocation message. When the *BackEnd* server receives this message, it extracts the transaction id (and the other values) from the message and creates a new `Span` with them. Resulting, all `Spans` in a single transaction share the same transaction id.

A `Span` records important method invocations and their related data(arguments, return value, etc) before encapsulating them as `SpanEvents` in a call stack like representation. The `Span` itself and each of its `SpanEvents` represents a method invocation.

`Span` and `SpanEvent` have many fields, but most of them are handled internally by Pinpoint Agent and most plugin developers won't need to worry about them. But the fields and data that must be handled by plugin developers will be listed throughout this guide.

## II. Pinpoint Plugin Structure

Pinpoint plugin consists of *type-provider.yml* and `ProfilerPlugin` implementations. *type-provider.yml* defines the `ServiceTypes` and `AnnotationKeys` that will be provided by the plugin, and provides them to Pinpoint Agent, Web and Collector. `ProfilerPlugin` implementations are used by Pinpoint Agent to transform target classes to record trace data.

Plugins are deployed as jar files. These jar files are packaged under the *plugin* directory for the agent, while the collector and web have them deployed under *WEB-INF/lib*. On start up, Pinpoint Agent, Collector, and Web iterates through each of these plugins; parses *type-provider.yml*, and loads `ProfilerPlugin` implementations using `ServiceLoader` from the following locations:

* META-INF/pinpoint/type-provider.yml
* META-INF/services/com.navercorp.pinpoint.bootstrap.plugin.ProfilerPlugin

Here is a [template plugin project](https://github.com/pinpoint-apm/pinpoint-plugin-template) you can use to start creating your own plugin.

### 1. type-provider.yml

*type-provider.yml* defines the `ServiceTypes` and `AnnotationKeys` that will be used by the plugin and provided to the agent, collector and web; the format of which is outlined below.

```yaml
serviceTypes:
    - code: <short>
      name: <String>
      desc: <String>   # May be omitted, defaulting to the same value as name.
      property:        # May be omitted, all properties defaulting to false.
          terminal: <boolean>               # May be omitted, defaulting to false.
          queue: <boolean>                  # May be omitted, defaulting to false.
          recordStatistics: <boolean>       # May be omitted, defaulting to false.
          includeDestinationId: <boolean>   # May be omitted, defaulting to false.
          alias: <boolean>                  # May be omitted, defaulting to false.          
      matcher:         # May be omitted
          type: <String>   # Any one of 'args', 'exact', 'none'
          code: <int>      # Annotation key code - required only if type is 'exact'

annotationKeys:
    - code: <int>
      name: <String>
      property:        # May be omitted, all properties defaulting to false.
          viewInRecordSet: <boolean>
```

`ServiceType` and `AnnotationKey` defined here are instantiated when the agent loads, and can be obtained using `ServiceTypeProvider` and `AnnotationKeyProvider` like below.

```java
// ServiceType
ServiceType serviceType = ServiceTypeProvider.getByCode(1000);    // by ServiceType code
ServiceType serviceType = ServiceTypeProvider.getByName("NAME");  // by ServiceType name
// AnnotationKey
AnnotationKey annotationKey = AnnotationKeyProvider.getByCode("100");
```

#### 1.1 ServiceType

Every `Span` and `SpanEvent` contains a `ServiceType`. The `ServiceType` represents which library the traced method belongs to, as well as how the `Span` and `SpanEvent` should be handled.

The table below shows the `ServiceType`'s properties.

| property   | description                                                |
| ---------- | ---------------------------------------------------------- |
| name       | name of the `ServiceType`. Must be unique                  |
| code       | short type code value of the `ServiceType`. Must be unique |
| desc       | description                                                |
| properties | properties                                                 |

`ServiceType` code must use a value from its appropriate category. The table below shows these categories and their range of codes.

| category     | range        |
| ------------ | ------------ |
| Internal Use | 0 \~ 999     |
| Server       | 1000 \~ 1999 |
| DB Client    | 2000 \~ 2999 |
| Cache Client | 8000 \~ 8999 |
| RPC Client   | 9000 \~ 9999 |
| Others       | 5000 \~ 7999 |

`ServiceType` code must be unique. Therefore, if you are writing a plugin that will be shared publicly, **you must** contact Pinpoint dev. team to get a `ServiceType` code assigned. If your plugin is for private use, you may freely pick a value for `ServiceType` code from the table below.

| category     | range        |
| ------------ | ------------ |
| Server       | 1900 \~ 1999 |
| DB client    | 2900 \~ 2999 |
| Cache client | 8900 \~ 8999 |
| RPC client   | 9900 \~ 9999 |
| Others       | 7500 \~ 7999 |

`ServiceTypes` can have the following properties.

| property                 | description                                                                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TERMINAL                 | This `Span` or `SpanEvent` invokes a remote node but the target node is not traceable with Pinpoint                                                           |
| QUEUE                    | This `Span` or `SpanEvent` consumes/produces a message from/to a message queue.                                                                               |
| INCLUDE\_DESTINATION\_ID | This `Span` or `SpanEvent` records a `destination id` and remote server is not a traceable type.                                                              |
| RECORD\_STATISTICS       | Pinpoint Collector should collect execution time statistics of this `Span` or `SpanEvent`                                                                     |
| ALIAS                    | The service may or may not have Pinpoint-Agent attached at the following service but regardlessly have knowledge what will follow. (Ex. Elasticsearch client) |

#### 1.2 AnnotationKey

You can annotate spans and span events with more information. An **Annotation** is a key-value pair where the key is an `AnnotationKey` type and the value is a primitive type, String or a byte\[]. There are pre-defined `AnnotationKeys` for commonly used annotation types, but you can define your own keys in *type-provider.yml* if these are not enough.

| property   | description                                                 |
| ---------- | ----------------------------------------------------------- |
| name       | Name of the `AnnotationKey`                                 |
| code       | int type code value of the `AnnotationKey`. Must be unique. |
| properties | properties                                                  |

If you are writing a plugin for public use, and are looking to add a new `AnnotationKey`, you must contact the Pinpoint dev. team to get an `AnnotationKey` code assigned. If your plugin is for private use, you may pick a value between 900 to 999 safely to use as `AnnotationKey` code.

The table below shows the `AnnotationKey` properties.

| property              | description                                    |
| --------------------- | ---------------------------------------------- |
| VIEW\_IN\_RECORD\_SET | Show this annotation in transaction call tree. |
| ERROR\_API\_METADATA  | This property is not for plugins.              |

#### Example

You can find *type-provider.yml* sample [here](https://github.com/pinpoint-apm/pinpoint-plugin-sample/blob/master/plugins/sample/src/main/resources/META-INF/pinpoint/type-provider.yml).

You may also define and attach an `AnnotationKeyMatcher` with a `ServiceType` (`matcher` element in the sample *type-provider* code above). If you attach an `AnnotationKeyMatcher` this way, matching annotations will be displayed as representative annotation when the `ServiceType`'s `Span` or `SpanEvent` is displayed in the transaction call tree.

### 2. ProfilerPlugin

`ProfilerPlugin` modifies target library classes to collect trace data.

`ProfilerPlugin` works in the order of following steps:

1. Pinpoint Agent is started when the JVM starts.
2. Pinpoint Agent loads all plugins under `plugin` directory.
3. Pinpoint Agent invokes `ProfilerPlugin.setup(ProfilerPluginSetupContext)` for each loaded plugin.
4. In the `setup` method, the plugin registers a `TransformerCallback` to all classes that are going to be transformed.
5. Target application starts.
6. Every time a class is loaded, Pinpoint Agent looks for the `TransformerCallback` registered to the class.
7. If a `TransformerCallback` is registered, the Agent invokes it's `doInTransform` method.
8. `TransformerCallback` modifies the target class' byte code. (e.g. add interceptors, add fields, etc.)
9. The modified byte code is returned to the JVM, and the class is loaded with the returned byte code.
10. Application continues running.
11. When a modified method is invoked, the injected interceptor's `before` and `after` methods are invoked.
12. The interceptor records the trace data.

The most important points to consider when writing a plugin are 1) figuring out which methods are interesting enough to warrant tracing, and 2) injecting interceptors to actually trace these methods. These interceptors are used to extract, store, and pass trace data around before they are sent off to the Collector. Interceptors may even cooperate with each other, sharing context between them. Plugins may also aid in tracing by adding getters or even custom fields to the target class so that the interceptors may access them during execution. [Pinpoint plugin sample](https://github.com/pinpoint-apm/pinpoint-plugin-sample) shows you how the `TransformerCallback` modifies classes and what the injected interceptors do to trace a method.

We will now describe what interceptors must do to trace different kinds of methods.

#### 2.1 Plain method

*Plain method* refers to anything that is not a top-level method of a node, or is not related to remote or asynchronous invocation. [Sample 2](https://github.com/pinpoint-apm/pinpoint-plugin-sample/tree/master/plugins/sample/src/main/java/com/navercorp/pinpoint/plugin/sample/_02_Injecting_Custom_Interceptor) shows you how to trace these plain methods.

#### 2.2 Top level method of a node

*Top level method of a node* is a method in which its interceptor begins a new trace in a node. These methods are typically acceptors for RPCs, and the trace is recorded as a `Span` with `ServiceType` categorized as a server.

How the `Span` is recorded depends on whether the transaction has already begun at any previous nodes.

**2.2.1 New transaction**

If the current node is the first one that is recording the transaction, you must issue a new transaction id and record it. `TraceContext.newTraceObject()` will handle this task automatically, so you will simply need to invoke it.

**2.2.2 Continue Transaction**

If the request came from another node traced by a Pinpoint Agent, then the transaction will already have a transaction id issued; and you will have to record the data below to the `Span`. (Most of these data are sent from the previous node, usually packed in the request message)

| name                  | description                           |
| --------------------- | ------------------------------------- |
| transactionId         | Transaction ID                        |
| parentSpanId          | Span ID of the previous node          |
| parentApplicationName | Application name of the previous node |
| parentApplicationType | Application type of the previous node |
| rpc                   | Procedure name (Optional)             |
| endPoint              | Server(current node) address          |
| remoteAddr            | Client address                        |
| acceptorHost          | Server address that the client used   |

Pinpoint finds caller-callee relation between nodes using *acceptorHost*. In most cases, *acceptorHost* is identical to *endPoint*. However, the address which client sent the request to may sometimes be different from the address the server received the request (proxy). To handle such cases, you have to record the actual address the client used to send the request to as *acceptorHost*. Normally, the client plugin will have added this address into the request message along with the transaction data.

Moreover, you must also use the span id issued and sent by the previous node.

Sometimes, the previous node marks the transaction to not be traced. In this case, you must not trace the transaction.

As you can see, the client plugin must be able pass trace data to the server plugin, and how to do this is protocol dependent.

You can find an example of top-level method server interceptor [here](https://github.com/pinpoint-apm/pinpoint-plugin-sample/tree/master/plugins/sample/src/main/java/com/navercorp/pinpoint/plugin/sample/_14_RPC_Server).

#### 2.3 Methods invoking a remote node

An interceptor of a method that invokes a remote node has to record the following data:

| name          | description                                                                           |
| ------------- | ------------------------------------------------------------------------------------- |
| endPoint      | Target server address                                                                 |
| destinationId | Logical name of the target                                                            |
| rpc           | Invoking target procedure name (optional)                                             |
| nextSpanId    | Span id that will be used by next node's span (If next node is traceable by Pinpoint) |

Whether or not the next node is traceable by Pinpoint affects how the interceptor is implemented. The term "traceable" here is about possibility. For example, a HTTP client's next node is a HTTP server. Pinpoint does not trace all HTTP servers, but it is possible to trace them (and there already are HTTP server plugins). In this case, the HTTP client's next node is traceable. On the other hand, MySQL JDBC's next node, a MySQL database server, is not traceable.

**2.3.1 If the next node is traceable**

If the next node is traceable, the interceptor must propagate the following data to the next node. How to pass them is protocol dependent, and in worst cases may be impossible to pass them at all.

| name                  | description                                                                                   |
| --------------------- | --------------------------------------------------------------------------------------------- |
| transactionId         | Transaction ID                                                                                |
| parentApplicationName | Application name of current node                                                              |
| parentApplicationType | Application type of current node                                                              |
| parentSpanId          | Span id of trace at current node                                                              |
| nextSpanId            | Span id that will be used by the next node's span (same value with nextSpanId of above table) |

Pinpoint finds out caller-callee relation by matching *destinationId* of client trace and *acceptorHost* of server trace. Therefore the client plugin has to record *destinationId* and the server plugin has to record *acceptorHost* with the same value. If server cannot acquire the value by itself, client plugin has to pass it to server.

The interceptor's recorded `ServiceType` must be from the RPC client category.

You can find an example for these interceptors [here](https://github.com/pinpoint-apm/pinpoint-plugin-sample/tree/master/plugins/sample/src/main/java/com/navercorp/pinpoint/plugin/sample/_13_RPC_Client).

**2.3.2 If the next node is not traceable**

If the next node is not traceable, your `ServiceType` must have the `TERMINAL` property.

If you want to record the *destinationId*, it must also have the `INCLUDE_DESTINATION_ID` property. If you record *destinationId*, server map will show a node per destinationId even if they have same *endPoint*.

Also, the `ServiceType` must be a DB client or Cache client category. Note that you do not need to concern yourself about the terms "DB" or "Cache", as any plugin tracing a client library with non-traceable target server may use them. The only difference between "DB" and "Cache" is the time range of the response time histogram ("Cache" having smaller intervals for the histogram).

#### 2.4 Asynchronous task

Trace objects are bound to the thread that first created them via **ThreadLocal** and whenever the execution crosses a thread boundary, trace objects are *lost* to the new thread. Therefore, in order to trace tasks across thread boundaries, you must take care of passing the current trace context over to the new thread. This is done by injecting an **AsyncContext** into an object shared by both the invocation thread and the execution thread.\
The invocation thread creates an **AsyncContext** from the current trace, and injects it into an object that will be passed over to the execution thread. The execution thread then retrieves the **AsyncContext** from the object, creates a new trace out of it and binds it to it's own **ThreadLocal**.\
You must therefore create interceptors for two methods : i) one that initiates the task (invocation thread), and ii) the other that actually handles the task (execution thread).

The initiating method's interceptor has to issue an **AsyncContext** and pass it to the handling method. How to pass this value depends on the target library. In worst cases, you may not be able to pass it at all.

The handling method's interceptor must then continue the trace using the propagated **AsyncContext** and bind it to it's own thread. However, it is very strongly recommended that you simply extend the **AsyncContextSpanEventSimpleAroundInterceptor** so that you do not have to handle this manually.

Keep in mind that since the shared object must be able have **AsyncContext** injected into it, you have to add a field using `AsyncContextAccessor` during it's class transformation. You can find an example for tracing asynchronous tasks [here](https://github.com/pinpoint-apm/pinpoint-plugin-sample/tree/master/plugins/sample/src/main/java/com/navercorp/pinpoint/plugin/sample/_12_Asynchronous_Trace).

#### 2.5 Case Study: HTTP

HTTP client is an example of *a method invoking a remote node* (client), and HTTP server is an example of a *top level method of a node* (server). As mentioned before, client plugins must have a way to pass transaction data to server plugins to continue the trace. Note that the implementation is protocol dependent, and [HttpMethodBaseExecuteMethodInterceptor](https://github.com/pinpoint-apm/pinpoint/blob/master/plugins/httpclient3/src/main/java/com/navercorp/pinpoint/plugin/httpclient3/interceptor/HttpMethodBaseExecuteMethodInterceptor.java) of [HttpClient3 plugin](https://github.com/pinpoint-apm/pinpoint/tree/master/plugins/httpclient3) and [StandardHostValveInvokeInterceptor](https://github.com/pinpoint-apm/pinpoint/blob/master/plugins/tomcat/src/main/java/com/navercorp/pinpoint/plugin/tomcat/interceptor/StandardHostValveInvokeInterceptor.java) of [Tomcat plugin](https://github.com/pinpoint-apm/pinpoint/tree/master/plugins/tomcat) show a working example of this for HTTP:

1. Pass transaction data as HTTP headers. You can find header names [here](https://github.com/pinpoint-apm/pinpoint/blob/master/bootstrap-core/src/main/java/com/navercorp/pinpoint/bootstrap/context/Header.java)
2. Client plugin records `IP:PORT` of the server as `destinationId`.
3. Client plugin passes `destinationId` value to server as `Header.HTTP_HOST` header.
4. Server plugin records `Header.HTTP_HOST` header value as `acceptorHost`.

One more thing you have to remember is that all the clients and servers using the same protocol must pass the transaction data in the same way to ensure compatibility. So if you are writing a plugin of some other HTTP client or server, your plugin has to record and pass transaction data as described above.

### 3. Plugin Integration Test

You can run plugin integration tests (`mvn integration-test`) with [PinointPluginTestSuite](https://github.com/pinpoint-apm/pinpoint/blob/master/test/src/main/java/com/navercorp/pinpoint/test/plugin/PinpointPluginTestSuite.java), which is a *JUnit Runner*. It downloads all the required dependencies from maven repositories and launches a new JVM with the Pinpoint Agent and the aforementioned dependencies. The JUnit tests are executed in this JVM.

To run the plugin integration test, it needs a complete agent distribution - which is why integration tests are in the *plugin-sample-agent* module and why they are run in **integration-test phase**.

For the actual integration test, you will want to first invoke the method you are tracing, and then use [PluginTestVerifier](https://github.com/pinpoint-apm/pinpoint/blob/master/bootstrap-core/src/main/java/com/navercorp/pinpoint/bootstrap/plugin/test/PluginTestVerifier.java) to check if the trace data is correctly recorded.

#### 3.1 Test Dependency

`PinointPluginTestSuite` doesn't use the project's dependencies (configured in pom.xml). It uses the dependencies that are listed by `@Dependency` annotation. This way, you may test multiple versions of the target library using the same test class.

Dependencies are declared as following. You may specify versions or version ranges for a dependency library.

```
@Dependency({"some.group:some-artifact:1.0", "another.group:another-artifact:2.1-RELEASE"})
@Dependency({"some.group:some-artifact:[1.0,)"})
@Dependency({"some.group:some-artifact:[1.0,1.9]"})
@Dependency({"some.group:some-artifact:[1.0],[2.1],[3.2])"})
```

`PinointPluginTestSuite` by default searches the local repository and maven central repository. You may also add your own repositories by using the `@Repository` annotation.

#### 3.2 Jvm Version

You can specify the JVM version for a test using `@JvmVersion`. If `@JvmVersion` is not present, JVM at `java.home property` will be used.

#### 3.3 Application Test

`PinpointPluginTestSuite` is not for applications that has to be launched by its own main class. You can extend [AbstractPinpointPluginTestSuite](https://github.com/pinpoint-apm/pinpoint/blob/master/test/src/main/java/com/navercorp/pinpoint/test/plugin/AbstractPinpointPluginTestSuite.java) and related types to test such applications.

### 4. Adding Images

If you're developing a plugin for applications, you need to add images so the server map can render the corresponding node. The plugin jar itself cannot provide these image files and for now, you will have to add the image files to the web module manually.

First, put the PNG files to following directories:

* web/src/main/webapp/images/icons (25x25)
* web/src/main/webapp/images/servermap (80x40)

Then, add `ServiceType` name and the image file name to `htIcons` in *web/src/main/webapp/components/server-map2/jquery.ServerMap2.js*.


# Setting Alarm

[English](#alarm) | [한국어](#alarm-1)

## Alarm

Application's status is periodically checked and alarm is triggered if certain pre-configured conditions (rules) are satisfied.

pinpoint-batch server checks every 3 minutes based on the last 5 minutes of data. And if the conditions are satisfied, it sends sms/email/webhook to the users listed in the user group.

> If an email/sms/webhook is sent everytime when the threshold is exceeded, even after the recipients are aware of the event they might get the same alarms continuously which we thought might be unneccessary. Therefore we decided to gradually increase the transmission frequency for alarms.\
> ex) If an alarm occurs continuously, transmission frequency is increased by a factor of two. 3 min -> 6min -> 12min -> 24min
>
> **NOTICE!**
>
> * These logics were part of pinpoint-web server and ran in the background until v2.2.0 From v2.2.1 it is separated into pinpoint-batch server. Since the batch logic(code) in pinpoint-web will be deprecated in the future, we advise you to transfer the execution of batch to pinpoint-batch server.
> * Webhook function is newly added in v2.1.1, and has some changes in v2.3.1. In both versions, MYSQL table needs to be changed. Please check the notice on these changes in [2.1.1](#2.1-configuration-and-implementation-in-pinpoint-batch)

### 1. User Guide

1\) Configuration menu

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-0ea93f5e306fc6e4958749507fdf8155578552d8%2FConfiguration%20page.gif?alt=media)

2\) Register users

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-f622485ac439ce9675079f95fcdb75b5e04420e4%2Fadd%20user.gif?alt=media)

3\) Create user groups

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-4ea91f0d20fecae25061c23e7d92d5f49b6252e3%2FAdd%20usergroup.gif?alt=media)

4\) (Optional) Add webhooks

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-b44f12715e808e3b0bd8f641b7769251a6285735%2Fadd%20webhook.gif?alt=media)

5\) Set alarm rules

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-63548e3c2432358b70ae68a911d25e8bb00bd4da%2Fadd%20alarm.gif?alt=media)

**Alarm Rules**

```
SLOW COUNT
   Triggered when the number of slow requests sent to the application exceeds the configured threshold.

SLOW RATE
   Triggered when the percentage(%) of slow requests sent to the application exceeds the configured threshold.

ERROR COUNT
   Triggered when the number of failed requests sent to the application exceeds the configured threshold.

ERROR RATE
   Triggered when the percentage(%) of failed requests sent to the application exceeds the configured threshold.

TOTAL COUNT
   Triggered when the number of all requests sent to the application exceeds the configured threshold.

APDEX SCORE
   Triggered when the Apdex score goes down below the configured threshold.

SLOW COUNT TO CALLEE
   Triggered when the number of slow requests sent by the application exceeds the configured threshold.
   You must specify the domain or the address(ip, port) in the configuration UI's "Note..." box 
   ex) www.naver.com, 127.0.0.1:8080

SLOW RATE TO CALLEE
   Triggered when the percentage(%) of slow requests sent by the application exceeds the configured threshold.
   You must specify the domain or the address(ip, port) in the configuration UI's "Note..." box 
   ex) www.naver.com, 127.0.0.1:8080

ERROR COUNT TO CALLEE
   Triggered when the number of failed requests sent by the application exceeds the configured threshold.
   You must specify the domain or the address(ip, port) in the configuration UI's "Note..." box 
   ex) www.naver.com, 127.0.0.1:8080

ERROR RATE TO CALLEE
   Triggered when the percentage(%) of failed requests sent by the application exceeds the configured threshold.
   You must specify the domain or the address(ip, port) in the configuration UI's "Note..." box 
   ex) www.naver.com, 127.0.0.1:8080

TOTAL COUNT TO CALLEE
   Triggered when the number of all requests sent by the application exceeds the configured threshold.
   You must specify the domain or the address(ip, port) in the configuration UI's "Note..." box 
   ex) www.naver.com, 127.0.0.1:8080

HEAP USAGE RATE
   Triggered when the application's heap usage(%) exceeds the configured threshold.

JVM CPU USAGE RATE
   Triggered when the application's CPU usage(%) detected by JVM exceeds the configured threshold.

SYSTEM CPU USAGE RATE
   Triggered when the application's CPU usage(%) detected by system exceeds the configured threshold.

DATASOURCE CONNECTION USAGE RATE
   Triggered when the application's DataSource connection usage(%) exceeds the configured threshold.

FILE DESCRIPTOR COUNT
   Triggered when the number of open file descriptors exceeds the configured threshold.
```

### 2. Configuration & Implementation

Alarms generated by Pinpoint can be configured to be sent over email, sms and webhook.

Sending alarms over email is simple - you will simply need to configure the property file. Sending alarms over sms requires some implementation. Read on to find out how to do this. The alarm using webhook requires a separate webhook receiver service. You should implement the webhook receiver service - which is not provided by Pinpoint, or You can use [the sample project](https://github.com/doll6777/slack-receiver).

Few modifications are required in pinpoint-batch and pinpoint-web to use the alarm feature. Add some implementations and settings in pinpoint-batch. Configure Pinpoint-web for user to set an alarm settings.

### 2.1 Configuration & Implementation in pinpoint-batch

#### 2.1.1) Email configuration, sms and webhook implementation

**A. Email alarm service**

To use the mailing feature, you need to configure the SMTP server information and information to be included in the email in the [batch-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/batch-root.properties) file.

```
pinpoint.url= #pinpoint-web server url
alarm.mail.server.url= #smtp server address
alarm.mail.server.port= #smtp server port
alarm.mail.server.username= #username for smtp server authentication
alarm.mail.server.password= #password for smtp server authentication
alarm.mail.sender.address= #sender's email address

ex)
pinpoint.url=http://pinpoint.com
alarm.mail.server.url=stmp.server.com
alarm.mail.server.port=587
alarm.mail.server.username=pinpoint
alarm.mail.server.password=pinpoint
alarm.mail.sender.address=pinpoint_operator@pinpoint.com
```

The class that sends emails is already registered as Spring bean in [applicationContext-batch-sender.xml](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/applicationContext-batch-sender.xml).

```
    <bean id="mailSender" class="com.navercorp.pinpoint.batch.alarm.SpringSmtpMailSender">
        <constructor-arg ref="batchConfiguration"/>
        <constructor-arg ref="userGroupService"/>
        <constructor-arg ref="javaMailSenderImpl"/>
    </bean>

    <bean id="javaMailSenderImpl" class="org.springframework.mail.javamail.JavaMailSenderImpl">
        <property name="host" value="${alarm.mail.server.url:}" />
        <property name="port" value="${alarm.mail.server.port:587}" />
        <property name="username" value="${alarm.mail.server.username:}" />
        <property name="password" value="${alarm.mail.server.password:}" />
        <property name="javaMailProperties">
            <props>
                <prop key="mail.transport.protocol">${alarm.mail.transport.protocol:}</prop>
                <prop key="mail.smtp.port">${alarm.mail.smtp.port:}</prop>
                <prop key="mail.smtp.from">${alarm.mail.sender.address:}</prop>
                <prop key="mail.smtp.auth">${alarm.mail.smtp.auth:false}</prop>
                <prop key="mail.smtp.starttls.enable">${alarm.mail.smtp.starttls.enable:false}</prop>
                <prop key="mail.smtp.starttls.required">${alarm.mail.smtp.starttls.required:false}</prop>
                <prop key="mail.debug">${alarm.mail.debug:false}</prop>
            </props>
        </property>
    </bean>
```

If you would like to implement your own mail sender, simply replace the `SpringSmtpMailSender`, `JavaMailSenderImpl` beans above with your own implementation that implements `com.navercorp.pinpoint.web.alarm.MailSender` interface.

```
public interface MailSender {
   void sendEmail(AlarmChecker checker, int sequenceCount);
}
```

**B. Sms alarm service**

To send alarms over sms, you will need to implement your own sms sender by implementing `com.navercorp.pinpoint.batch.alarm.SmsSender` interface. If there is no `SmsSender` implementation, then alarms will not be sent over sms.

```
public interface SmsSender {
    public void sendSms(AlarmChecker checker, int sequenceCount);
}
```

**C. Webhook alarm service**

Webhook alarm service is a feature that can transmit Pinpoint's alarm message through Webhook API.

The webhook receiver service that receives the webhook message should be implemented by yourself, or use [a sample project](https://github.com/doll6777/slack-receiver) provided (in this case Slack).

The alarm messages(refer to as payloads) sent to webhook receiver have the different schema depending on the Alarm Checker type. You can see the payload schemas in [3.Others - The Specification of webhook payloads and the examples](##3.Others).

To enable the webhook alarm service, You need to configure *pinpoint.modules.web.webhook* in [application.yml](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/application.yml) file. Webhook receiver urls can be configured in web UI after configuring the web module to enable webhook as described in the following section.

```
# webhook config
pinpoint.modules.web:
    webhook: true
```

> **NOTICE!**
>
> \*\*\* \*\*MYSQL table ALTER for migrating to Pinpoint v2.1.1 \*\*\*\*\*
>
> As the webhook alarm service is newly added in Pinpoint 2.1.1, you should add column `webhook_send` in table `alarm_rule` to your MYSQL server used for previous versions of Pinpoint.
>
> ```
> ALTER TABLE alarm_rule ADD COLUMN webhook_send CHAR(1) DEFAULT NULL;
> ```
>
> **\*\*\* MYSQL table CREATE for migrating to Pinpoint v2.3.1 \*\*\***
>
> Different webhook destinations can be specified to different alarms and new tables are added for this. Create table `webhook` and `webhook_send` as below in your MYSQL server used for previous versions of Pinpoint.
>
> ```
> CREATE TABLE `webhook` (
>   `webhook_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
>   `alias` VARCHAR(45) NULL,
>   `url` VARCHAR(45) NOT NULL,
>   `application_id` VARCHAR(45) NULL,
>   `service_name` VARCHAR(45) NULL,
>   PRIMARY KEY (`webhook_id`)
> );
>
> CREATE TABLE `webhook_send` (
>   `webhook_send_info_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
>   `webhook_id` INT UNSIGNED NOT NULL,
>   `rule_id` INT UNSIGNED NOT NULL,
>   PRIMARY KEY (`webhook_send_info_id`)
> );
> ```
>
> Of course if you are migrating from versions lower than v2.1.1 to v2.3.1, all the changes above need to be applied.

WebhookSenderImpl class, which sends the webhook, is already implemented for you and is added as webhookSender bean in [applicationContext-batch-sender.xml](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/applicationContext-batch-sender.xml) of Pinpoint-batch.

```markup
   <bean id="webHookSender" class="com.navercorp.pinpoint.web.alarm.WebhookSenderImpl">
        <constructor-arg ref="batchConfiguration"/>
        <constructor-arg ref="userServiceImpl"/>
        <constructor-arg ref="restTemplate" />
    </bean>
```

#### 2.1.2) Configuring MYSQL

**step 1**

Prepare MYSQL Instance to persist the alarm service metadata.

**step 2**

Set up a MYSQL server and configure connection information in [jdbc-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/jdbc-root.properties) file.

```
jdbc.driverClassName=com.mysql.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:13306/pinpoint
jdbc.username=admin
jdbc.password=admin
```

**step 3**

Create tables for the alarm service. Use below DDL files.

* [CreateTableStatement-mysql.sql](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/sql/CreateTableStatement-mysql.sql)
* [SpringBatchJobRepositorySchema-mysql.sql](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/sql/SpringBatchJobRepositorySchema-mysql.sql)

#### 2.1.3) How to execute pinpoint-batch

The pinpoint-batch project is based on spring boot and can be executed with the following command. When building is successfully finished, the executable file is placed under the target/deploy folder of the pinpoint-batch.

```
java -Dspring.profiles.active=XXXX -jar pinpoint-batch-VERSION.jar 

ex) java -Dspring.profiles.active=local -jar pinpoint-batch-2.1.1.jar
```

### 2.2 How to configure pinpoint-web

#### 2.2.1) Configuring MYSQL Server IP

In order to persist user alarm settings, set the mysql connection information in [jdbc-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/jdbc-root.properties) file in pinpoint-web.

```
jdbc.driverClassName=com.mysql.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:13306/pinpoint
jdbc.username=admin
jdbc.password=admin
```

#### 2.2.2) Enabling Webhook Alarm Service

Set *pinpoint.modules.web.webhook* in [pinpoint-web-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/application.yml) as *true* for user to configure the webhook alarm in *Alarm* menu.

```
# webhook config
pinpoint.modules.web:
    webhook: true
```

As you enable the webhook alarm service, you can set the webhook as alarm type and specify the target webhook.

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-d40bb10eb1e4c87b0b49c40df0da30ec191e496f%2Falarm_select_webhook.png?alt=media)

### 3. Others

### 3.1 Configuration, Execution, Performance.

**1) You may change the batch execution period by modifying the cron expression in** [***applicationContext-batch-schedule.xml***](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/applicationContext-batch-schedule.xml) **file**

```
<task:scheduled-tasks scheduler="scheduler">
    <task:scheduled ref="batchJobLauncher" method="alarmJob" cron="0 0/3 * * * *" />
</task:scheduled-tasks>
```

**2) Ways to improve alarm batch performance**

The alarm batch was designed to run concurrently. If there are a lot of applications using alarms, you may increase the size of the executor's thread pool by modifying `pool-size` in [*applicationContext-alarmJob.xml*](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/job/applicationContext-alarmJob.xml) file.

Note that increasing this value will result in higher resource usage.

```
<task:executor id="poolTaskExecutorForPartition" pool-size="1" />
```

If there are a lot of alarms registered to each application, you may set the `alarmStep` registered in [*applicationContext-alarmJob.xml*](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/job/applicationContext-alarmJob.xml) file to run concurrently.

```
<step id="alarmStep" xmlns="http://www.springframework.org/schema/batch">
    <tasklet task-executor="poolTaskExecutorForStep" throttle-limit="3">
        <chunk reader="reader" processor="processor" writer="writer" commit-interval="1"/>
    </tasklet>
</step>
<task:executor id="poolTaskExecutorForStep" pool-size="10" />
```

**3) Use quickstart's web**

Pinpoint Web uses Mysql to persist users, user groups, and alarm configurations, but our Quickstart example uses MockDAO to reduce memory usage. If you want to use Mysql with Quickstart, please refer to Pinpoint Web's [applicationContext-dao-config.xml](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/applicationContext-dao-config.xml) and [jdbc.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/jdbc.properties).

### 3.2 Details on Webhook

#### 3.2.1) webhook receiver sample project

[Slack-Receiver](https://github.com/doll6777/slack-receiver) is an example project for the webhook receiver. The project can receive alarms from Pinpoint through webhook and send the message to Slack. If you want more details, see [the project repository](https://github.com/doll6777/slack-receiver).

#### 3.2.2) The Specification of webhook payloads and the examples

**The Schemas of webhook payloads**

Key

| Name          | Type      | Description                                                  | Nullable |
| ------------- | --------- | ------------------------------------------------------------ | -------- |
| pinpointUrl   | String    | Pinpoint-web server URL                                      | O        |
| batchEnv      | String    | Batch server environment variable                            | X        |
| applicationId | String    | Alarm target application Id                                  | X        |
| serviceType   | String    | Alarm target application service type                        | X        |
| userGroup     | UserGroup | The UserGroup in the user group page                         | X        |
| checker       | Checker   | The checker info in the alarm setting page                   | X        |
| unit          | String    | The unit of detected value by checker                        | O        |
| threshold     | Integer   | The threshold of value detected by checker during a set time | X        |
| notes         | String    | The notes in the alarm setting page                          | O        |
| sequenceCount | Integer   | The number of alarm occurence                                | X        |

UserGroup

| Name             | Type          | Description                              | Nullable |
| ---------------- | ------------- | ---------------------------------------- | -------- |
| userGroupId      | String        | The user group id in the user group page | X        |
| userGroupMembers | UserMember\[] | Members Info of a specific user group    | X        |

Checker

| Name          | Type                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Nullable |
| ------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| name          | String                      | The name of checker in the alarm setting page                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | X        |
| type          | String                      | <p>The type of checker abstracted by value detected by checker<br>"LongValueAlarmChecker" type is the abstracted checker type of “Slow Count”, “Slow Rate”, “Error Count”, “Error Rate”, “Total Count”, “Slow Count To Callee”, “Slow Rate To Callee”, “Error Count To Callee”, “Error Rate To Callee”, “Total Count to Callee”.<br>"LongValueAgentChecker" type is the abstracted checker type of "Heap Usage Rate", "Jvm Cpu Usage Rate", "System Cpu Usage Rate", "File Descriptor Count".<br>"BooleanValueAgentChecker" type is the abstracted checker type of "Deadlock or not".<br>"DataSourceAlarmListValueAgentChecker" type is the abstracted checker type of "DataSource Connection Usage Rate".</p> | X        |
| detectedValue | Integer or DetectedAgent\[] | <p>The value detected by checker<br>If “type” is “LongValueAlarmChecker”, “detectedValue” is Integer type.<br>If "type" is not "LongValueAlarmChecker", "detectedValue" is DetectedAgents\[] type.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | X        |

UserMember

| Name             | Type   | Description               | Nullable |
| ---------------- | ------ | ------------------------- | -------- |
| id               | String | Member id                 | X        |
| name             | String | Member name               | X        |
| email            | String | Member email              | O        |
| department       | String | Member department         | O        |
| phoneNumber      | String | Member phone number       | O        |
| phoneCountryCode | String | Member phone country code | O        |

DetectedAgent

| Name       | Type                                                  | Description                                                                                                                                                                                                                                                                                   | Nullable |
| ---------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| agentId    | String                                                | Agent id detected by checker                                                                                                                                                                                                                                                                  | X        |
| agentValue | <p>Integer or<br>Boolean or<br>DataSourceAlarm\[]</p> | <p>The value of Agent detected by checker<br>If “type” is “LongValueAgentChecker”, “agentValue” is Integer type.<br>If “type” is “BooleanValueAgentChecker”,“agentValue” is Boolean type.<br>If “type” is “DataSourceAlarmListValueAgentChecker”, “agentValue” is DataSourceAlarm\[] type</p> | X        |

DataSourceAlarm

| Name            | Type    | Description                                   | Nullable |
| --------------- | ------- | --------------------------------------------- | -------- |
| databaseName    | String  | The database name connected to application    | X        |
| connectionValue | Integer | The application's DataSource connection usage | X        |

**The Examples of the webhook Payload**

LongValueAlarmChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "TOTAL COUNT",
   "type": "LongValueAlarmChecker",
   "detectedValue": 33
 },
 "unit": "",
 "threshold": 15,
 "notes": "Note Example",
 "sequenceCount": 4
}
```

LongValueAgentChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "HEAP USAGE RATE",
   "type": "LongValueAgentChecker",
   "detectedValue": [
     {
       "agentId": "test-agent",
       "agentValue": 8
     }
   ]
 },
 "unit": "%",
 "threshold": 5,
 "notes": "Note Example",
 "sequenceCount": 4
}
```

BooleanValueAgentChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "DEADLOCK OCCURRENCE",
   "type": "BooleanValueAgentChecker",
   "detectedValue": [
     {
       "agentId": "test-agent",
       "agentValue": true
     }
   ]
 },
 "unit": "BOOLEAN",
 "threshold": 1,
 "notes": "Note Example",
 "sequenceCount": 4
}
```

DataSourceAlarmListValueAgentChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "DATASOURCE CONNECTION USAGE RATE",
   "type": "DataSourceAlarmListValueAgentChecker",
   "detectedValue": [
     {
       "agentId": "test-agent",
       "agentValue": [
                 {
                     "databaseName": "test",
                     "connectionValue": 32
                 }
        ]
     }
   ]
 },
 "unit": "%",
 "threshold": 16,
 "notes": "Note Example",
 "sequenceCount": 4
}
```

## Alarm

Pinpoint는 application 상태를 주기적으로 체크하여 application 상태의 수치가 임계치를 초과할 경우 사용자에게 알람을 전송하는 기능을 제공한다.

Application 상태 값이 사용자가 설정한 임계치를 초과하는지 판단하는 batch는 [pinpoint-batch](https://github.com/pinpoint-apm/pinpoint/tree/master/batch)에서 동작 한다. Alarm batch는 기본적으로 3분에 한번씩 동작이 된다. 최근 5분동안의 데이터를 수집해서 alarm 조건을 만족하면 user group에 속한 user 들에게 sms/email/webhook message를 전송한다.

> 연속적으로 알람 조건이 임계치를 초과한 경우에 매번 sms/email/webhook를 전송하지 않는다.\
> 알람 조건이 만족할때마다 매번 sms/email/webhook이 전송되는것은 오히려 방해가 된다고 생각하기 때문이다. 그래서 연속해서 알람이 발생할 경우 sms/email/webhook 전송 주기가 점증적으로 증가된다.\
> 예) 알람이 연속해서 발생할 경우, 전송 주기는 3분 -> 6분 -> 12분 -> 24분 으로 증가한다.
>
> ***
>
> **알림**
>
> * Batch는 pinpoint 2.2.0 버전까지는 [pinpoint-web](https://github.com/pinpoint-apm/pinpoint/tree/master/web)에서 동작되었지만, 2.2.1 버전 부터는 batch가 [pinpoint-batch](https://github.com/pinpoint-apm/pinpoint/tree/master/batch)에서 동작되도록 로직을 분리했다.\*\* \*\*앞으로 pinpoint-web의 batch로직은 제거를 할 예정이므로, pinpoint-web에서 batch를 동작시키는 경우 pinpoint-batch에서 batch를 실행하도록 구성하는것을 추천한다.
> * 웹훅 기능은 v2.1.1에 신규로 추가되었으며 v2.3.1에 기능이 개선되었다. 두 버전 모두에서 MYSQL 테이블 변경이 있으므로, 해당 버전 이전에서 업그레이드할 경우, [2.1.1 항목](#2.1-pinpoint-batch)에서 관련 변경 사항을 확인 후 적용해야 한다.

### 1. Alarm 기능 사용 방법

1\) 설정 화면으로 이동

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-0ea93f5e306fc6e4958749507fdf8155578552d8%2FConfiguration%20page.gif?alt=media)

2\) user를 등록

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-f622485ac439ce9675079f95fcdb75b5e04420e4%2Fadd%20user.gif?alt=media)

3\) userGroup을 생성

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-4ea91f0d20fecae25061c23e7d92d5f49b6252e3%2FAdd%20usergroup.gif?alt=media)

4\) (선택사항) webhook 등

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-b44f12715e808e3b0bd8f641b7769251a6285735%2Fadd%20webhook.gif?alt=media)

5\) alarm rule을 등록

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-63548e3c2432358b70ae68a911d25e8bb00bd4da%2Fadd%20alarm.gif?alt=media)

alarm rule에 대한 설명은 아래를 참고하시오.

```
SLOW COUNT
   외부에서 application을 호출한 요청 중에 외부서버로 응답을 늦게 준 요청의 개수가 임계치를 초과한 경우 알람이 전송된다.

SLOW RATE
   외부에서 application을 호출한 요청 중에 외부서버로 응답을 늦게 준 요청의 비율(%)이 임계치를 초과한 경우 알람이 전송된다.

ERROR COUNT
   외부에서 application을 호출한 요청 중에 에러가 발생한 요청의 개수가 임계치를 초과한 경우 알람이 전송된다.

ERROR RATE
   외부에서 application을 호출한 요청 중에 에러가 발생한 요청의 비율(%)이 임계치를 초과한 경우 알람이 전송된다.

TOTAL COUNT
   외부에서 application을 호출한 요청 개수가 임계치를 초과한 경우 알람이 전송된다.
   
APDEX SCORE
   Apdex 점수가 임계치 이하로 내려간 경우 알람이 전송된다.

SLOW COUNT TO CALLEE
   application 내에서 외부서버를 호출한 요청 중 slow 호출의 개수가 임계치를 초과한 경우 알람이 전송된다.
   설정 화면의 Note 항목에 외부서버의 도메인 이나 주소(ip, port)를 입력해야 합니다. ex) naver.com, 127.0.0.1:8080

SLOW RATE TO CALLEE
   application 내에서 외부서버를 호출한 요청 중 slow 호출의 비율(%)이 임계치를 초과한 경우 알람이 전송된다.
   설정 화면의 Note 항목에 외부서버의 도메인 이나 주소(ip, port)를 입력해야 합니다. ex) naver.com, 127.0.0.1:8080

ERROR COUNT TO CALLEE
   application 내에서 외부서버를 호출한 요청 중 error 가 발생한 호출의 개수가 임계치를 초과한 경우 알람이 전송된다.
   설정 화면의 Note 항목에 외부서버의 도메인 이나 주소(ip, port)를 입력해야 합니다. ex) naver.com, 127.0.0.1:8080

ERROR RATE TO CALLEE
   application 내에서 외부서버를 호출한 요청 중 error 가 발생한 호출의 비율이 임계치를 초과한 경우 알람이 전송된다.
   설정 화면의 Note 항목에 외부서버의 도메인 이나 주소(ip, port)를 입력해야 합니다. ex) naver.com, 127.0.0.1:8080

TOTAL COUNT TO CALLEE
   application 내에서 외부서버를 호출한 요청의 개수가 임계치를 초과한 경우 알람이 전송된다.
   설정 화면의 Note 항목에 외부서버의 도메인 이나 주소(ip, port)를 입력해야 합니다. ex) naver.com, 127.0.0.1:8080

HEAP USAGE RATE
   heap의 사용률이 임계치를 초과한 경우 알람이 전송된다.

JVM CPU USAGE RATE
   applicaiton의 CPU 사용률이 임계치를 초과한 경우 알람이 전송된다.

SYSTEM CPU USAGE RATE
   서버의 CPU 사용률이 임계치를 초과한 경우 알람이 전송된다.

DATASOURCE CONNECTION USAGE RATE
   applicaiton의 DataSource내의 Connection 사용률이 임계치를 초과한 경우 알람이 전송된다.

FILE DESCRIPTOR COUNT
   열려있는 File Descriptor 개수가 임계치를 초가한 경우 알람이 전송된다.
```

### 2. 설정 및 구현 방법

알람을 전송하는 방법은 총 3가지로서, email, sms와 webhook으로 알람을 전송할 수 있다.

email 전송은 설정만 추가하면 기능을 사용할 수 있고, sms 전송을 하기 위해서는 직접 전송 로직을 구현해야 한다.\
webhook 전송은 webhook message를 받는 webhook receiver 서비스를 별도로 준비해야한다. webhook receiver 서비스는 [샘플 프로젝트](https://github.com/doll6777/slack-receiver)를 사용하거나 직접 구현해야 한다.

alarm 기능을 사용하려면 pinpoint-batch와 pinpoint-web를 수정해야한다. pinpoint-batch에는 alarm batch 동작을 위해서 설정 및 구현체를 추가해야 한다. pinpoint-web에는 사용자가 알람을 추가할 수 있도록 설정해야한다.

### 2.1 pinpoint-batch 설정 및 구현 방법

#### 2.1.1) email/sms/webhook 전송 설정 및 구현

**A. email 전송**

email 전송 기능을 사용하기 위해서 [batch-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/batch-root.properties)파일에 smtp 서버 정보와 email에 포함될 정보들을 설정해야 한다.

```
pinpoint.url= #pinpoint-web 서버의 url 
alarm.mail.server.url= #smtp 서버 주소  
alarm.mail.server.port= #smtp 서버 port 
alarm.mail.server.username= #smtp 인증을 위한 userName
alarm.mail.server.password= #smtp 인증을 위한 password
alarm.mail.sender.address= # 송신자 email

ex)
pinpoint.url=http://pinpoint.com
alarm.mail.server.url=stmp.server.com
alarm.mail.server.port=587
alarm.mail.server.username=pinpoint
alarm.mail.server.password=pinpoint
alarm.mail.sender.address=pinpoint_operator@pinpoint.com
```

참고로 [applicationContext-batch-sender.xml](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/applicationContext-batch-sender.xml) 파일에 email을 전송하는 class가 bean으로 등록 되어있다.

```
    <bean id="mailSender" class="com.navercorp.pinpoint.batch.alarm.SpringSmtpMailSender">
        <constructor-arg ref="batchConfiguration"/>
        <constructor-arg ref="userGroupService"/>
        <constructor-arg ref="javaMailSenderImpl"/>
    </bean>

    <bean id="javaMailSenderImpl" class="org.springframework.mail.javamail.JavaMailSenderImpl">
        <property name="host" value="${alarm.mail.server.url:}" />
        <property name="port" value="${alarm.mail.server.port:587}" />
        <property name="username" value="${alarm.mail.server.username:}" />
        <property name="password" value="${alarm.mail.server.password:}" />
        <property name="javaMailProperties">
            <props>
                <prop key="mail.transport.protocol">${alarm.mail.transport.protocol:}</prop>
                <prop key="mail.smtp.port">${alarm.mail.smtp.port:}</prop>
                <prop key="mail.smtp.from">${alarm.mail.sender.address:}</prop>
                <prop key="mail.smtp.auth">${alarm.mail.smtp.auth:false}</prop>
                <prop key="mail.smtp.starttls.enable">${alarm.mail.smtp.starttls.enable:false}</prop>
                <prop key="mail.smtp.starttls.required">${alarm.mail.smtp.starttls.required:false}</prop>
                <prop key="mail.debug">${alarm.mail.debug:false}</prop>
            </props>
        </property>
    </bean>
```

만약 email 전송 로직을 직접 구현하고 싶다면 위의 SpringSmtpMailSender, JavaMailSenderImpl bean 선언을 제거하고 com.navercorp.pinpoint.web.alarm.MailSender interface를 구현해서 bean을 등록하면 된다.

```
public interface MailSender {
   void sendEmail(AlarmChecker checker, int sequenceCount);
}
```

**B. sms 전송**

sms 전송 기능을 사용 하려면 com.navercorp.pinpoint.batch.alarm.SmsSender interface를 구현하고 bean으로 등록해야 한다. SmsSender 구현 class가 없는 경우 sms는 전송되지 않는다.

```
public interface SmsSender {
    public void sendSms(AlarmChecker checker, int sequenceCount);
}
```

**C. webhook 전송**

Webhook 전송 기능은 Pinpoint의 Alarm message를 Webhook API로 전송 할 수 있는 기능이다.

webhook message를 전송받는 webhook receiver 서비스는 [**샘플 프로젝트**](https://github.com/doll6777/slack-receiver)**를 사용하거나 직접 구현해야 한다.** Webhook Receiver 서버에 전송되는 Alarm message(이하 payload)는 Alarm Checker 타입에 따라 스키마가 다르다. Checker 타입에 따른 payload 스키마는 [**3.기타** - webhook 페이로드 스키마 명세, 예시](##3.기타)에서 설명한다.

webhook 기능을 활성화 하기위해서, [pinpoint.modules.web.webhook](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/application.yml) 파일에 Webhook 전송 여부(pinpoint.modules.web.webhook)를 설정한다. Receiver 서버 정보의 경우 [2.2 pinpoint-web 설정 방법](#2.2-pinpoint-web) 같이 web 설정을 마친 후, UI를 통해 추가할 수 있다.

```
# webhook config
pinpoint.modules.web:
    webhook: true
```

> **알림**\
> \&#xNAN;**\*\*\* Pinpoint v2.1.1로 업그레이드를 하기 위한 MYSQL 테이블 변경 \*\*\***
>
> webhook 기능이 추가되면서 mysql 테이블 스키마가 수정되었기 때문에, Pinpoint 2.1.1 미만 버전에서 2.1.1 버전 이상으로 업그레이드한 경우 Mysql의 'alarm\_rule' 테이블에 'webhook\_send' 컬럼을 추가해야 다.
>
> ```
> ALTER TABLE alarm_rule ADD COLUMN webhook_send CHAR(1) DEFAULT NULL;
> ```
>
> **\*\*\* Pinpoint v2.3.1로 업그레이드를 하기 위한 MYSQL 테이블 추가 생성 \*\*\***
>
> Pinpoint v2.1.1에서는 하나의 webhook receiver로만 알람을 보낼 수 있었는데, Pinpoint v2.3.1에서부터 각 알람마다 서로 다른 webhook destination을 설정할 수 있다. 이를 위해서 두 개의 새로운 MYSQL 테이블이 추가되었으며, 아래와 같이 ‘webhook’과 ‘webhook\_send’테이블을 추가해야 한다.
>
> ```
> CREATE TABLE `webhook` (
>   `webhook_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
>   `alias` VARCHAR(45) NULL,
>   `url` VARCHAR(45) NOT NULL,
>   `application_id` VARCHAR(45) NULL,
>   `service_name` VARCHAR(45) NULL,
>   PRIMARY KEY (`webhook_id`)
> );
>
> CREATE TABLE `webhook_send` (
>   `webhook_send_info_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
>   `webhook_id` INT UNSIGNED NOT NULL,
>   `rule_id` INT UNSIGNED NOT NULL,
>   PRIMARY KEY (`webhook_send_info_id`)
> );
> ```
>
> 물론 v2.3.1 이전 버전에서 바로 v2.3.1로 업그레이드하는 경우, 위의 모든 변경사항을 적용해야한다.

참고로 Webhook을 전송하는 클래스(WebhookSenderImpl)는 Pinpoint에서 이미 제공하고 있으며, webHookSender bean으 Pinpoint-batch의 [applicationContext-batch-sender.xml](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/applicationContext-batch-sender.xml) 파일에 등록 되어있다.

```markup
<bean id="webHookSender" class="com.navercorp.pinpoint.web.alarm.WebhookSenderImpl">
    <constructor-arg ref="batchConfiguration"/>
    <constructor-arg ref="userServiceImpl"/>
    <constructor-arg ref="restTemplate" />
</bean>
```

#### 2.1.2) MYSQL 서버 IP 주소 설정 & table 생성

**step 1**

알람에 관련된 데이터를 저장하기 위해 Mysql 서버를 준비한다.

**step 2**

mysql 접근을 위해서 pinpoint-batch의 [jdbc-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/jdbc-root.properties) 파일에 접속 정보를 설정한다.

```
jdbc.driverClassName=com.mysql.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:13306/pinpoint
jdbc.username=admin
jdbc.password=admin
```

**step 3**

mysql에 Alarm 기능에 필요한 table을 생성한다. table 스키마는 아래 파일을 참조한다.

* [*CreateTableStatement-mysql.sql*](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/sql/CreateTableStatement-mysql.sql)
* [*SpringBatchJobRepositorySchema-mysql.sql*](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/sql/SpringBatchJobRepositorySchema-mysql.sql)

#### 2.1.3) pinpoint-batch 실행 방법

pinpoint-batch 프로젝트는 spring boot기반으로 되어있고 아래와 같은 명령어로 실행하면 된다. 빌드후 실행파일은 pinpoint-batch 모듈의 target/deploy 폴더 하위에서 확인할 수 있다.

```
java -Dspring.profiles.active=XXXX -jar pinpoint-batch-VERSION.jar 

ex) java -Dspring.profiles.active=local -jar pinpoint-batch-2.1.1.jar
```

### 2.2 pinpoint-web 설정 방법

#### 2.2.1) MYSQL 서버 IP 주소 설정

사용자 알람 설정을 저장하기 위해서 pinpoint-web의 [jdbc-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/jdbc-root.properties) 파일에 mysql 접속 정보를 설정한다.

```
jdbc.driverClassName=com.mysql.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:13306/pinpoint
jdbc.username=admin
jdbc.password=admin
```

#### 2.2.2) webhook 기능 활성화

사용자가 알람 설정에 webhook 기능을 적용할수 있도록 [pinpoint-web-root.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/application.yml) 파일에 webhook 기능을 활성화한다.

```
# webhook config
pinpoint.modules.web:
    webhook: true
```

webhook 기능을 활성화하면, 아래 그림처럼 알람 설정 화면에서 webhook을 알람 타입으로 선택할 수 있다.

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-d40bb10eb1e4c87b0b49c40df0da30ec191e496f%2Falarm_select_webhook.png?alt=media)

### 3. 기타

### 3.1 설정, 실행, 성능

**1) Batch의 동작 주기를 조정하고 싶다면** [***applicationContext-batch-schedule.xml***](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/applicationContext-batch-schedule.xml) **파일의 cron expression을 수정하면 된다.**

```
<task:scheduled-tasks scheduler="scheduler">
    <task:scheduled ref="batchJobLauncher" method="alarmJob" cron="0 0/3 * * * *" />
</task:scheduled-tasks>
```

**2) Alarm batch 성능을 높이는 방법은 다음과 같다.**

Alarm batch 성능 튜닝을 위해서 병렬로 동작이 가능하도록 구현을 해놨다. 그래서 아래에서 언급된 조건에 해당하는 경우 설정 값을 조정한다면 성능을 향상 시킬 수 있다. 단, 병렬성을 높이면 리소스 사용률이 높아지는 것은 감안해야 한다.

Alarm이 등록된 application의 개수가 많다면 [*applicationContext-alarmJob.xml*](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/job/applicationContext-alarmJob.xml) 파일의 poolTaskExecutorForPartition의 pool size를 늘려주면 된다.

```
<task:executor id="poolTaskExecutorForPartition" pool-size="1" />
```

Application 각각마다 등록된 alarm의 개수가 많다면 [*applicationContext-alarmJob.xml*](https://github.com/pinpoint-apm/pinpoint/blob/master/batch/src/main/resources/job/applicationContext-alarmJob.xml) 파일에 선언된 alarmStep이 병렬로 동작되도록 설정하면 된다.

```
<step id="alarmStep" xmlns="http://www.springframework.org/schema/batch">
    <tasklet task-executor="poolTaskExecutorForStep" throttle-limit="3">
        <chunk reader="reader" processor="processor" writer="writer" commit-interval="1"/>
    </tasklet>
</step>
<task:executor id="poolTaskExecutorForStep" pool-size="10" />
```

**3) Quickstart web을 사용한다면.**

Quickstart pinpoint web은 mockDAO를 사용하기 때문에 추가한 알람 설정들이 저장되지 않는다. Mysql과 quickstart를 연동해서 사용하려면 다음의 설정들을 참고해서 수정 후 기능을 사용해야한다: [applicationContext-dao-config.xml](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/applicationContext-dao-config.xml), [jdbc.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/jdbc.properties).

### 3.2 webhook 상세

#### 3.2.1 **Webhook receiver 예제 프로젝트**

[Slack-Receiver](https://github.com/doll6777/slack-receiver) 는 Webhook Receiver의 예제 프로젝트이다. 이 프로젝트는 Pinpoint의 webhook의 알람을 받아서 Slack으로 메시지를 전송할 수 있는 스프링 부트로 구현된 서비스이다. 이 프로젝트의 자세한 사항은 [해당 GitHub 저장소](https://github.com/doll6777/slack-receiver) 를 참고하면 된다.

#### 3.2.2 webhook 페이로드 스키마 및 예시

**페이로드 스키마**

Key

| Name          | Type      | Description              | Nullable |
| ------------- | --------- | ------------------------ | -------- |
| pinpointUrl   | String    | Pinpoint-web의 서버 URL 주소  | O        |
| batchEnv      | String    | Batch 서버의 환경 변수          | X        |
| applicationId | String    | 타겟 애플리케이션 ID             | X        |
| serviceType   | String    | 타겟 애플리케이션 서비스 타입         | X        |
| userGroup     | UserGroup | 유저 그룹 페이지의 유저 그룹         | X        |
| checker       | Checker   | alarm 설정 페이지의 checker 정보 | X        |
| unit          | String    | checker가 감지한 값의 단위       | O        |
| threshold     | Integer   | 설정된 시간동안 체커가 감지한 값의 임계치  | X        |
| notes         | String    | 알람 설정 페이지의 notes         | O        |
| sequenceCount | Integer   | 알람 발생 횟수                 | X        |

UserGroup

| Name             | Type          | Description         | Nullable |
| ---------------- | ------------- | ------------------- | -------- |
| userGroupId      | String        | 유저 그룹 페이지의 유저 그룹 ID | X        |
| userGroupMembers | UserMember\[] | 특정 유저 그룹의 멤버 정보     | X        |

Checker

| Name          | Type                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Nullable |
| ------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| name          | String                      | 알람 설정 페이지의 checker 이름                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | X        |
| type          | String                      | <p>체커가 감지한 값의 추상 타입, 다음 중 하나에 해당됨<br>"LongValueAlarmChecker" 타입은 "Slow Count", “Slow Count”, “Slow Rate”, “Error Count”, “Error Rate”, “Total Count”, “Slow Count To Callee”, “Slow Rate To Callee”, “Error Count To Callee”, “Error Rate To Callee”, “Total Count to Callee”의 추상 타입에 속한다.<br>"LongValueAgentChecker" 타입은 "Heap Usage Rate", "Jvm Cpu Usage Rate", "System Cpu Usage Rate", "File Descriptor Count"의 추상타입이다.<br>"BooleanValueAgentChecker" 타입은 "Deadlock or not"의 추상 타입이다.<br>"DataSourceAlarmListValueAgentChecker" 타입은 "DataSource Connection Usage Rate"의 추상타입이다.</p> | X        |
| detectedValue | Integer or DetectedAgent\[] | <p>Checker가 감지한 값<br>“LongValueAlarmChecker”, “detectedValue” 타입은 Integer 타입이다.<br>"LongValueAlarmChecker", "detectedValue"이 아닌 타입은 DetectedAgents\[] 타입 이다.</p>                                                                                                                                                                                                                                                                                                                                                                                                                         | X        |

UserMember

| Name             | Type   | Description            | Nullable |
| ---------------- | ------ | ---------------------- | -------- |
| id               | String | 멤버의 id                 | X        |
| name             | String | 멤버의 name               | X        |
| email            | String | 멤버의 email              | O        |
| department       | String | 멤버의 department         | O        |
| phoneNumber      | String | 멤버의 phone number       | O        |
| phoneCountryCode | String | 멤버의 phone country code | O        |

DetectedAgent

| Name       | Type                                                  | Description                                                                                                                                                                                                                   | Nullable |
| ---------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| agentId    | String                                                | Checker가 감지한 에이전트 ID                                                                                                                                                                                                          | X        |
| agentValue | <p>Integer or<br>Boolean or<br>DataSourceAlarm\[]</p> | <p>체커가 감지한 에이전트의 값<br>“LongValueAgentChecker”, “agentValue” 은 Integer 타입이다.<br>“BooleanValueAgentChecker”,“agentValue” 은 Boolean 타입이다..<br>“DataSourceAlarmListValueAgentChecker”, “agentValue”은 DataSourceAlarm\[] 타입이다.</p> | X        |

DataSourceAlarm

| Name            | Type    | Description                              | Nullable |
| --------------- | ------- | ---------------------------------------- | -------- |
| databaseName    | String  | 애플리케이션에 접속한 데이터베이스 이름                    | X        |
| connectionValue | Integer | Applicaiton의 DataSource내의 Connection 사용률 | X        |

**webhook Payload 예제**

LongValueAlarmChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "TOTAL COUNT",
   "type": "LongValueAlarmChecker",
   "detectedValue": 33
 },
 "unit": "",
 "threshold": 15,
 "notes": "Note Example",
 "sequenceCount": 4
}
```

LongValueAgentChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "HEAP USAGE RATE",
   "type": "LongValueAgentChecker",
   "detectedValue": [
     {
       "agentId": "test-agent",
       "agentValue": 8
     }
   ]
 },
 "unit": "%",
 "threshold": 5,
 "notes": "Note Example",
 "sequenceCount": 4
}
```

BooleanValueAgentChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "DEADLOCK OCCURRENCE",
   "type": "BooleanValueAgentChecker",
   "detectedValue": [
     {
       "agentId": "test-agent",
       "agentValue": true
     }
   ]
 },
 "unit": "BOOLEAN",
 "threshold": 1,
 "notes": "Note Example",
 "sequenceCount": 4
}
```

DataSourceAlarmListValueAgentChecker

```javascript
{
 "pinpointUrl": "http://pinpoint.com",
 "batchEnv": "release",
 "applicationId": "TESTAPP",
 "serviceType": "TOMCAT",
 "userGroup": {
   "userGroupId": "Group-1",
   "userGroupMembers": [
     {
       "id": "msk1111",
       "name": "minsookim",
       "email": "pinpoint@naver.com",
       "department": "Platform",
       "phoneNumber": "01012345678",
       "phoneCountryCode": 82
     }
   ]
 },
 "checker": {
   "name": "DATASOURCE CONNECTION USAGE RATE",
   "type": "DataSourceAlarmListValueAgentChecker",
   "detectedValue": [
     {
       "agentId": "test-agent",
       "agentValue": [
                 {
                     "databaseName": "test",
                     "connectionValue": 32
                 }
        ]
     }
   ]
 },
 "unit": "%",
 "threshold": 16,
 "notes": "Note Example",
 "sequenceCount": 4
}
```


# New Inspector

[English](#id-1-overview) | [한국어](#id-1)

## 1 Overview

There has been changes in inspector in v3.0.0. The newly renewed inspector will be referred to as 'New Inspector' below, while the previous version will be referred to as 'Legacy Inspector' ([Legacy Application Inspector](https://pinpoint-apm.gitbook.io/pinpoint/v/v2.5.4/documents/application-inspector)).

Although users won't see significant changes on front-end, but the whole architecture has been rebuilt from the scratch.\
The data storage has been changed from HBase to Pinot.\
And the APIs have been improved so that it is more easily extenable and their responses more clear to understand.

## 2 Installation and Configuration

### 2.1 Install and Run Kafka

Kafka enables real-time streaming of inspector data from Pinpoint collector to Pinot.

#### 2.1.A Set Up Kafka

Refer to [this document](https://kafka.apache.org/quickstart) to download Kafka and start the Kafka environment.

If you have already [set up Kafka for Pinpoint System Metric](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.2.a-kafka-installation-guide), please skip this step.

#### 2.1.B Create Kafka Topics for New Inspector

* Create 2 topics with the names below:
  * inspector-stat-agent-00
  * inspector-stat-app

### 2.2 Set Up Pinot

#### 2.2.A Install Pinot

Install Pinot according to [Pinot Getting Started guide](https://docs.pinot.apache.org/basics/getting-started).

If you have already [set up Pinot for Pinpoint System Metric](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#id-3.2.a-install-and-run-pinot), please skip this step.

#### 2.2.B Create Pinot Tables

* Create 2 tables with the snames below:
  * inspectorStatAgent00: This table stores agent inspector data. The [script file to create the table](https://github.com/pinpoint-apm/pinpoint/tree/master/inspector-module/inspector-collector/src/main/pinot/multi-table) is provided in our github repository.
  * inspectorStatApp: This table stores application inspector data.
* Refer to the [github repository](https://github.com/pinpoint-apm/pinpoint/tree/master/inspector-module/inspector-collector/src/main/pinot) for table schema and configuration settings.

### 2.3 Configure and Run Pinpoint Collector, Web, and Batch with New Inspector

* **Related options and settings are already enabled by default, so there is no need to modify any settings from what is provided in our github repository.**
* When upgrading from Pinpoint version below 3.0 to version 3.0.0 or above, some of the options may be missing in the configuration properties files you have been using. Please refer to the related configurations in the following section to check if any changes are needed in your settings.

## 3 Related Settings of Pinpoint Components

* The following configurations are already set by default in Pinpoint version 3.0.
* When upgrading from Pinpoint version below 3.0 to version 3.0.0 or above and when you wish to continue using customized configuration files you have been using, please check if below mentioned configurations are well set in your files.

### Pinpoint Collector

* `application.yml` file in `collector-starter` module:

```
pinpoint:
  modules:
    collector:
      inspector:
        enabled: true
```

### Pinpoint Web

* `application.yml` file in `web-starter` module:

```
pinpoint:
  modules:
    web:
      inspector:
        enabled: true
```

### Pinpoint Batch

* `batch-root.properties` file in `batch` module:

```
alarm.collector.version=2
```

## 4 Q\&A

#### A Can we still use the Legacy Inspector to save the data to HBase?

Yes, but Legacy Inspector will be deprecated in v3.0.1 so we recommended you to use the New Inspector.

To use Legacy Inspector with v3.0.0, you need to add the following settings to the Pinpoint components:

**Modify `application.yml` file in `collector-starter` module OR add java vm option when running Pinpoint Collector.**

* application.yml

```
pinpoint:
  modules:
    collector:
      inspector:
        hbase:
          enabled: true
```

* java vm option

```
-Dpinpoint.modules.collector.inspector.hbase.enabled=true
```

**Modify `batch-root.properties` file in `batch` module OR add java vm option when running Pinpoint Batch.**

* batch-root.properties

```
alarm.collector.version=1
```

* java vm option

```
-Dalarm.collector.version=1
```

#### B Why change database to Pinot when there are no additional features provided to users?

New Inspector saves and retrieves the data faster than the Legacy Inspector thanks to Pinot. As Pinot project gets mature over time, there can be further improvements on performance or additional features can be introduced to Pinpoint Inpsector as well.

#### C Reading inspector-stat-agent table becomes slow as more data is being stored.

You can improve performance by distributing the data across multiple tables. Follow the steps below to create multiple Kafka topics and Pinot tables. Then, add settings to Pinpoint components to read and write data from multiple Pinot tables.

**Create More Kafka Topics**

* Create N Kafka topics. (From 00 to N-1)
* The format of the topics is as follows:
  * inspector-stat-agent-00
  * inspector-stat-agent-01
  * ...
  * inspector-stat-agent-99

**Create More Pinot Tables**

* Create N Pinot tables. (From 00 to N-1)
  * [The script file](https://github.com/pinpoint-apm/pinpoint/tree/master/inspector-module/inspector-collector/src/main/pinot/multi-table) creating multiple Pinot tables is provided in our github repository.
* The format of the table names and schema names is as follows:
  * inspectorStatAgent00
  * inspectorStatAgent01
  * ...
  * inspectorStatAgent99

**Modify `application.yml` file in `collector-starter` module OR add java vm option when running Pinpoint Collector**

* application.yml

```
kafka:
  inspector:
    agent:
      table:
        count: N
```

* java vm option

```
-Dkafka.inspector.agent.topic.count=N
```

**Modify `application.yml` file in `web-starter` module OR add java vm option when running Pinpoint Web**

* application.yml

```
pinot:
  inspector:
    agent:
      table:
        count: N
```

* java vm option

```
-Dpinot.inspector.agent.topic.count=N
```

**Modify `batch-root.properties` file in `batch` module OR add java vm option when running Pinpoint Batch**

* batch-root.properties

```
job.alarm.agent.inspector.stat.table.count=N
```

* java vm option

```
-Djob.alarm.agent.inspector.stat.table.count=N
```

***

## 1 개요

inspector가 Pinpoint v3.0.0에서 새로워졌습니다.\
이하 새로워진 inspector를 'New Inspector'이라고 부르고 과거의 inspector는 'Legacy Inspector'라고 칭합니다 ([Legacy Application Inspector](https://pinpoint-apm.gitbook.io/pinpoint/v/v2.5.4/documents/application-inspector)).

New Inspector에서 사용자가 보는 화면은 크게 달라진 건은 없습니다.\
그러나 내부적으로 많은 변화가 있었습니다. 데이터를 저장하는 저장소가 HBase에서 Pinot로 변경이 되었습니다. api를 쉽게 확장할 수 있고, response를 명확한 형식으로 개편했습니다.\
즉 inspector 기능을 추가하고 확장하기 쉽게 개선되었습니다.

## 2 설치/설정 방법

### 2.1 Kafka 설치 및 실행

실시간으로 collector에서 데이터를 전달받아 Pinot에 저장하기 위해서 Kafka를 설치해야 합니다.

**2.1.A Kafka 설치**

[설치 가이드 링크](https://kafka.apache.org/quickstart)를 보고 Kafka를 다운 받아 실행합니다.

**2.1.B topic 생성**

* 아래 2개 Kafka topic을 생성합니다.
  * inspector-stat-agent-00
  * inspector-stat-app

### 2.2 Pinot 설치 및 실행

**2.1.A Pinot 설치**

Pinot 사이트에서 [설치 방법 가이드](https://docs.pinot.apache.org/basics/getting-started)를 참고하여 Pinot를 설치합니다.

**2.1.B Pinot table 생성**

* 아래 2개 테이블을 생성합니다.
  * inspectorStatAgent00: 이 테이블은 agent inspector data를 저장합니다. [스크립트](https://github.com/pinpoint-apm/pinpoint/tree/master/inspector-module/inspector-collector/src/main/pinot/multi-table)로 생성이 가능합니다.
  * inspectorStatApp: 이 테이블은 application inspector data를 저장합니다.
* table schema와 configuration은 [github repository](https://github.com/pinpoint-apm/pinpoint/tree/master/inspector-module/inspector-collector/src/main/pinot)를 참고해주세요.

### 2.3 Pinpoint Collector, batch, Web의 New Inspector 기능 활성화

* **관련 옵션 및 설정은 기본적으로 활성화되어 있으므로 추가로 설정할 필요가 없습니다.**
* Pinpoint 3.0 미만버전에서 3.0.0 이상버전으로 업그레이드 시 일부 옵션이 누락되는경우 아래 관련 옵션 설명을 참고해주세요.

## 3 Pinpoint 컴포넌트의 관련 설정

* 아래 설정들은 Pinpoint 3.0 버전에서 기본적으로 설정되어있습니다.
* Pinpoint 버전을 3.0으로 업그레이드하는경우 일부 설정이 누락되는 경우 참고하기 위해서 설정을 명시해놓습니다.

### Pinpoint Collector

* `collector-starter` 모둘의 `application.yml` 파일:

```
pinpoint:
  modules:
    collector:
      inspector:
        enabled: true
```

### Pinpoint Web

* `web-starter` 모듈의 `application.yml` 파일:

```
pinpoint:
  modules:
    web:
      inspector:
        enabled: true
```

### Pinpoint Batch

* `batch` 모듈의 `batch-root.properties` 파일:

```
alarm.collector.version=2
```

## 4 Q\&A

#### A HBase에 데이터를 저장하는 Legacy Inspector를 사용할 수 없나요?

가능합니다. 그러나 3.0.1 버전 이상 부터는 Legacy Inspector를 삭제할 예정이므로 Pinpoint 버전이 올라갈수록 기능을 사용할수 없으므로 New Inspector를 사용하는것을 권장합니다.\
기능을 사용하려면 Pinpoint 컴포넌트들에 아래 설정을 추가해야합니다.

**collector-starter 프로젝트의 application.yml 파일이나 java vm option에 아래 설정을 추가해주세요.**

* application.yml

```
pinpoint:
  modules:
    collector:
      inspector:
        hbase:
          enabled: true
```

* java vm option

```
-Dpinpoint.modules.collector.inspector.hbase.enabled=true
```

**batch 프로젝트에서 batch-root.properties 파일이나 java vm option에 아래 설정을 추가해주세요.**

* batch-root.properties

```
alarm.collector.version=1
```

* java vm option

```
-Dalarm.collector.version=1
```

#### B 사용자에게 제공되는 기능은 비슷한데 Pinot기반으로 inspector를 개선한 이유는 뭘까요?

다양한 데이터를 빠르게 저장하고 확인하고 위해서 Pinot로 데이터를 저장하도록 개선되었고\
아직 부족한 기능이 많지만 Pinot의 발전에 맞춰서 기능을 보완하도록 하겠습니다.

#### C inspector-stat-agent 테이블의 데이터가 많아서 읽기 속도가 느려집니다.

여러 개의 체이블에 데이터를 나누어 저장해서 성능 향상을 얻을 수 있습니다.\
아래를 단계를 따라 전체 N 개의 Kafka topic과 Pinot table을 생성하고, Pinpoint 컴포넌트들에 설정을 추가해서 data를 수집/조회합니다.

**Kafka topic 생성**

* N개 Kafka topic을 생성합니다. (00에서 N-1까지)
* topic의 형식은 다음과 같습니다.
  * inspector-stat-agent-00
  * inspector-stat-agent-01
  * ...
  * inspector-stat-agent-99

**Pinot table 생성**

* N개 Pinot table을 생성합니다. (00에서 N-1까지)
  * [스크립트](https://github.com/pinpoint-apm/pinpoint/tree/master/inspector-module/inspector-collector/src/main/pinot/multi-table)로 다수의 테이블 생성이 가능합니다.
* table name과 schema name의 형식은 다음과 같습니다.
  * insepctorStatAgent00
  * insepctorStatAgent01
  * ...
  * insepctorStatAgent99

**`collector-starter` 모듈의 `application.yml` 파일이나 java vm option에 아래 설정을 추가해 주세요.**

* application.yml

```
kafka:
  inspector:
    agent:
      table:
        count: N
```

* java vm option

```
-Dkafka.inspector.agent.topic.count=N
```

**`web-starter` 모듈의 `application.yml` 파일이나 java vm option에 아래 설정을 추가해 주세요.**

* application.yml

```
pinot:
  inspector:
    agent:
      table:
        count: N
```

* java vm option

```
-Dpinot.inspector.agent.topic.count=N
```

**`batch` 모듈의 `batch-root.properties` 파일이나 java vm option에 아래 설정을 추가해 주세요.**

* batch-root.properties

```
job.alarm.agent.inspector.stat.table.count=N
```

* java vm option

```
-Djob.alarm.agent.inspector.stat.table.count=N
```


# System Metric

[English](#system_metrics) | [한국어](#1_system_metrics_기능이란?)

## 1 System Metrics

System metrics menu is newly added to Pinpoint in v2.5.0.\
Pinpoint uses [telegraf agent](https://portal.influxdata.com/downloads/) to collect system metrics data to Pinpoint Collector in which the data are saved in Pinot.\
Saved system metrics data are accessible via Pinpoint web.

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-c894164f22ccffbbac3a17a452c9c99867ae5280%2Fsystem_metric_01.png?alt=media)

Pinot is a real-time distributed OLAP datastore. For further information please refer to [their official documents](https://docs.pinot.apache.org).

## 2 Architecture

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-13e876804194ef1b6837ef12ae31d84461ec6fab%2Fsystem_metric_02.jpeg?alt=media)

1. Telegraf agent sends system metrics data to Pinpoint collector.
2. Pinpoint collector saves data to Pinot through Kafka.

* Kafka is necessary to stream data to Pinot.

3. Pinpoint web accesses Pinot to display collected metrics data.

## 3 Installation and Configuration

### 3.1 Install Kafka

Kafka enables real-time streaming of system metrics data from Pinpoint collector to Pinot.

#### 3.1.A Kafka Installation Guide

Please refer to [this document](https://kafka.apache.org/quickstart) to get Kafka and start the Kafka environment.

#### 3.1.B Create Kafka Topics for Pinpoint System Metrics

Create 3 topics with the names below:

* `system-metric-data-type`
* `system-metric-tag`
* `system-metric-double`

### 3.2 Install Pinot

This section describes how to install Pinot which is used in Pinpoint to save system metrics data.

#### 3.2.A Install and Run Pinot

* Install Pinot according to [Pinot Getting Started guide](https://docs.pinot.apache.org/basics/getting-started)
* Above guide gives you the way to run Pinot locally, in Docker, and in Kubernetes.

#### 3.2.B Create Pinot Tables

* Pinot table schemas for Pinpoint system metrics is provided in [our github repository](https://github.com/pinpoint-apm/pinpoint/tree/master/metric-module/metric/src/main/pinot).
* Please refer to [Pinot documents](https://docs.pinot.apache.org/basics/components/table#streaming-table-creation) to create necessary tables in your Pinot cluster.
* Total 3 tables should be created.
  * systemMetricDataType: this table saves type informations on collected data.
  * systemMetricTag: this table saves metadata (i.e., host, tags) for collected data.
  * systemMetricDouble: this table saves metric data in double. In order to use the hybrid table feature, create both REALTIME and OFFLINE tables.

### 3.3 Configure and Run Pinpoint Collector with System Metrics

There are additional configurations for Pinpoint collector to collect the metrics data from Telegraf agents.

#### 3.3.A Pinpoint Collector Settings for System Metrics

**1)** In order to communicate with Pinot, you need to modify the configuration files in the [profiles](https://github.com/pinpoint-apm/pinpoint/tree/master/pinot/pinot-config/src/main/resources/pinot/profiles) directory according to your profile.

* Modify pinot-jdbc.properties configuration: Set the address of the Pinot installed in [3.1](#3.1-Install-Pinot) as follows:
  * ```
            pinpoint.pinot.jdbc.url=jdbc:pinot://localhost:9000
            pinpoint.pinot.jdbc.username=userId
            pinpoint.pinot.jdbc.password=password
    ```

**2)** In order to communicate with Kafka, you need to modify the configuration files in the [profiles](https://github.com/pinpoint-apm/pinpoint/tree/master/pinot/pinot-kafka/src/main/resources/profiles) directory according to your profile.

* Modify kafka-producer-factory.properties configuration: Set the address of your Kafka instance:
  * ```
    pinpoint.metric.kafka.bootstrap.servers=--KAFKA_ADDRESS--
    ```

#### 3.3.B Run Pinpoint Collector with System Metrics

After successfully building Pinpoint project, run `pinpoint-collector-starter-boot-XXXX.jar` file created under `pinpoint/metric-module/collector-starter/target/deploy`.

* `pinpoint-collector-starter-boot-XXXX.jar` includes system metrics on top of original pinpoint-collector.
* In order to enable metric functions, you need to add `--pinpoint.collector.type=METRIC` or `--pinpoint.collector.type=ALL` arguments when starting the application.
  * METRIC: only enables collecting the system metrics.
  * ALL: enables both pinpoint collector and system metrics collection.

### 3.4 Configure and Run Pinpoint Web with System Metrics

There are additional configurations for Pinpoint web to display the system metrics data stored in Pinot.

#### 3.4.A Pinpoint Web Settings for System Metrics

1. In order to communicate with Pinot, you need to modify the configuration files in the \[profiles]\((<https://github.com/pinpoint-apm/pinpoint/tree/master/pinot/pinot-config/src/main/resources/pinot/profiles>) directory according to your profile.

* Update the address of the Pinot installed in [3.1](#3.1-Install-Pinot) in the jdbc-pinot.properties configuration file:

  ```
  pinpoint.pinot.jdbc.url=jdbc:pinot://localhost:9000
  pinpoint.pinot.jdbc.username=userId
  pinpoint.pinot.jdbc.password=password
  ```

**2)** To enable the system metric feature in the web interface, modify the [pinpoint-web-metric.properties](https://github.com/pinpoint-apm/pinpoint/tree/master/metric-module/metric/src/main/resources/pinot-web/profiles) file:

```
config.show.systemMetric=true
```

#### 3.4.B Run Pinpoint Web with System Metrics

After successfully building Pinpoint project, run `pinpoint-web-starter-boot-XXXX.jar` file created under `pinpoint/metric-module/web-starter/target/deploy`.

#### 3.5 Additional Information

Pinpoint web and collector binaries with system metrics is located under different directories from those of the original Pinpoint web and collector.

* original collector: pinpoint/collector/deploy -> collector with system metrics: pinpoint/metric-module/collector-starter/target/deploy
* original web: pinpoint/web/deploy -> web with system metrics: pinpoint/metric-module/web-starter/target/deploy

### 3.6 Install and Configure Talegraf Agent

Telegraf collects below metrics information on the host machine:

* cpu
* disk usage
* disk usage (percent)
* inode usage
* memory usage
* memory usage(percent)
* swap
* system load
* nginx
* apache

***

* Install Telegraf according to this [installation guide](https://docs.influxdata.com/telegraf/v1.21/introduction/installation/).
* Add below configuration to `telegraf.conf` file to send collected metrics to Pinpoint collector via http.
  * **Note**: Starting from Pinpoint v3.0.2, the metric port has been changed from `15200` to `9995`.
  * ```
              [[outputs.http]]
                url = "http://{PINPOINT_COLLECTOR_IP}:9995/telegraf"
                 
                 [outputs.http.headers]
                 hostGroupName = {applicationName}
                 Content-Type = "application/json"  
    ```
  * `url`: substitute `{PINPOINT_COLLECTOR_IP}` to your Pinpoint collector address so that telegraf can send collected metrics to Pinpoint collector
  * `hostGroupName`: this value will be used as the key in Pinpoint web when querying the metrics details. It is recommended to use your applicationName already used in Pinpoint.

### 4 View Collected System Metrics Data

1. Click `Infrastructure` on the side bar menu in Pinpoint web.
2. Search for the hostGroupName you have configured for Telegraf agents as decribed [in 3.4](#3.4-Install-and-Configure-Talegraf-Agent).
3. A list of hosts will be displayed on the left, and you can view the system metrics data by clicking each of them.

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-c894164f22ccffbbac3a17a452c9c99867ae5280%2Fsystem_metric_03.png?alt=media)

### 5 Notes

* Other metrics and statistics data will be stored in Pinot to enhance Pinpoint experience in near future.
* Currently this system metrics versions are in beta. It will be officially released when when we can make sure that everything works as we intended.
* If you have been using the system metric feature in version 2.5.0 or lower and are upgrading, please refer to [guide](https://github.com/pinpoint-apm/pinpoint/issues/9791#issuecomment-1491486262) for instructions.

***

## 1 system metrics 기능이란?

system metrics 기능은 v2.5.0에 핀포인트에 새로 추가되었다.[telegraf agent](https://portal.influxdata.com/downloads/) 를 사용하여 system metric 데이터를 collector에 전달하고 pinot에 데이터를 저장한다.\
pinpoint web에서 저장된 system metric 데이터를 확인할 수 있다.

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-c894164f22ccffbbac3a17a452c9c99867ae5280%2Fsystem_metric_01.png?alt=media)

pinot는 실시간 분산 OLAP 데이터 저장소이다. 자세한 사항은 [pinot 사이트](https://docs.pinot.apache.org)를 참고하도록 하자.

## 2 구조

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-13e876804194ef1b6837ef12ae31d84461ec6fab%2Fsystem_metric_02.jpeg?alt=media)

* ① telgegraf agent에서 system metric 데이터를 collector에 전달한다.
* ② collector는 kafka에 데이터를 전송하여 pinot에 데이터를 저장한다.
  * 참고로 pinot는 stream 데이터 전송을 위해서 kafka를 반드시 필요로 한다.
* ③ web은 pinot에서 데이터를 조회하여 화면으로 데이터를 보여준다.

## 3 설치/설정 방법

### 3.1 kafka 설치 및 실행

실시간으로 collector에서 데이터를 전달받아 pinot에 저장하기 위해서 kafka를 설치해야 한다.

#### 3.1.A. kafka 설치

* [설치 가이드 링크](https://kafka.apache.org/quickstart)를 보고 kafka를 다운 받아 실행하자.

#### 3.1.B. topic 생성

* 아래 3개 topic을 생성하자.\
  -`system-metric-data-type`, `system-metric-tag`, `system-metric-double`

### 3.2 pinot 설치 및 실행

시스템 메트릭 데이터를 저장하는 pinot를 설치하는 법을 안내한다.

#### 3.2.A. pinot 설치 및 실행

* pinot 사이트에서 [설치 방법 가이드](https://docs.pinot.apache.org/basics/getting-started)를 참고하여 pinot를 설치한다.
* 다양한 환경(local, docker, Kubernetes)에서 pinot 실행 환경을 구성할 수 있으니 위 가이드를 참고하자.

#### 3.2.B. 테이블 스키마 및 생성

* [테이블 생성 스키마 파일](https://github.com/pinpoint-apm/pinpoint/tree/master/metric-module/metric/src/main/pinot)에 테이블 정보가 있다.
* 테이블 생성 방법은 [pinot가이드](https://docs.pinot.apache.org/basics/components/table#streaming-table-creation)를 참고하여 pinot 실행 환경 맞게 테이블을 생성하면 된다.
* 생성하는 테이블은 총 3개이다.
  * systemMetricDataType : 수집되는 데이터의 type 정보를 저장하는 테이블이다.
  * systemMetricTag : 수집되는 데이터의 metadata(host 정보, 데이터의 tag 정보)를 저장하는 테이블이다.
  * systemMetricDouble : double 데이터를 저장하는 테이블이다. hybrid table 기능 사용을 위해서 REALTIME, OFFLINE 테이블 둘다 생성하자.

### 3.3 collector 설정 및 실행

telegraf agent로 부터 전송된 데이터를 수집하기 위해서 collector에 설정을 추가한다.

#### 3.3.A. collector 설정

**1)** pinot와 통신을 위해서 [설정파일](https://github.com/pinpoint-apm/pinpoint/tree/master/pinot/pinot-config/src/main/resources/pinot/profiles)들을 profile에 맞게 수정해야 한다.

* pinot-jdbc.properties 설정 : [3.1](#3.1-pinot-설치-및-실행)에서 설치한 pinot의 주소를 설정한다.
  * ```
            pinpoint.pinot.jdbc.url=jdbc:pinot://localhost:9000
            pinpoint.pinot.jdbc.username=userId
            pinpoint.pinot.jdbc.password=password
    ```

**2)** kafka와 통신을 위해서 [설정파일](https://github.com/pinpoint-apm/pinpoint/tree/master/pinot/pinot-kafka/src/main/resources/profiles)들을 profile에 맞게 수정해야 한다.

* kafka-producer-factory.properties 설정 : kafka 의 주소를 설정한다.
  * ```
            pinpoint.metric.kafka.bootstrap.servers=--KAFKA_ADDRESS--
    ```

#### 3.3.B. collector 실행 방법

빌드 후 pinpoint/metric-module/collector-starter/target/deploy에 생성된 `pinpoint-collector-starter-boot-XXXX.jar`을 실행하면 된다.

* `pinpoint-collector-starter-boot-XXXX.jar` 은 pinpoint-collector 기능과 system metric 수집기능이 합해진 패키지이다.
* metric 기능을 활성화 하기 위해서 실행시 `--pinpoint.collector.type=METRIC` 나 `--pinpoint.collector.type=ALL` 옵션을 추가해야한다.
  * METRIC : system metric 수집기능만 동작된다.
  * ALL : pinpoint collector 기능과 system metric 수집기능이 동시에 동작된다.

### 3.4 web 설정 및 실행

pinot에 저장된 시스템 메트릭 데이터를 보여주기 위해서 web 설정을 수정한다.

#### 3.4.A. web 설정

**1)** pinot와 통신을 위해서 [설정파일](https://github.com/pinpoint-apm/pinpoint/tree/master/pinot/pinot-config/src/main/resources/pinot/profiles)들을 profile에 맞게 수정해야 한다.

* jdbc-pinot.properties 설정 : [3.1](#3.1-pinot-설치-및-실행)에서 설치한 pinot의 주소를 설정한다.
  * ````
        pinpoint.pinot.jdbc.url=jdbc:pinot://localhost:9000
        pinpoint.pinot.jdbc.username=userId
        pinpoint.pinot.jdbc.password=password
        ```
    ````

**2)**

* system metric 기능을 web에서 활성화하기 위해서 [pinpoint-web-metric.properties](https://github.com/pinpoint-apm/pinpoint/tree/master/metric-module/metric/src/main/resources/pinot-web/profiles) 파일을 수정한다.
  * ````
        config.show.systemMetric=true
        ```
    ````

#### 3.4.B. web 실행 방법

빌드 후 pinpoint/metric-module/web-starter/target/deploy에 생성된 `pinpoint-web-starter-boot-XXXX.jar`을 실행하면 된다.

* `pinpoint-web-starter-boot-XXXX.jar` 은 pinpoint web 기능과 metric 데이터 확인 기능이 합해진 패키지이다.

### 3.5 참고

* 참고로 web, collector의 실행파일이 과거 버전과 다르게 다른곳에 존재한다.
* 기존의 web, collector 실행파일 경로와 다르게 system metric기능이 포함된 collector, web은 실행 파일 경로는 다음과 같다.
  * collector : pinpoint/collector/deploy -> pinpoint/metric-module/collector-starter/target/deploy
  * web : pinpoint/web/deploy -> pinpoint/metric-module/web-starter/target/deploy

### 3.6 telegraf agent 설치 및 설정

telegraf agent를 통해 수집된 시스템 메트릭은 다음과 같다.

* cpu
* disk usage
* disk usage(percent)
* inode usage
* memory usage
* memory usage(percent)
* swap
* system load
* nginx
* apache

***

* 시스템 메트릭 데이터를 수집하는 telegraf agent를 설치하자.
  * [telegraf agent 설치 가이드](https://docs.influxdata.com/telegraf/v1.21/introduction/installation/)
* telegraf agent가 http 프로토콜로 collector에 데이터를 전달할 수 있도록 설정파일을 수정 해야한다.
  * telegraf.conf 설정 방법
    * http 프로토콜로 데이터를 전달수 있도록 output http plugin 아래 설정을 추가한다.
      * **참고**: Pinpoint v3.0.2부터 메트릭 포트가 `15200`에서 `9995`로 변경되었습니다.
      * ```
                [[outputs.http]]
                  url = "http://{PINPOINT_COLLECTOR_IP}:9995/telegraf"
                   
                   [outputs.http.headers]
                   hostGroupName = {applicationName}
                   Content-Type = "application/json"
        ```
    * `url`: {PINPOINT\_COLLECTOR\_IP} 자리에 데이터를 수집하는 collector의 주소를 설정한다.
    * `outputs.http.headers`은 서버 그룹의 key와 Content-Type을 설정한다.
      * `hostGroupName`: {applicationName}에 설정한 값을 key로 pinpoint-web에서 데이터를 조회할 수 있다. 핀포인트를 이미 사용 중이라면 application을 추적할 때 agent 설정 값으로 사용했던 applicationName을 사용하는 것을 추천한다.

## 4 데이터 조회

* pinpoint-web에서 왼쪽 `Infrastructure` 메뉴를 선택하여 system metric 화면으로 이동한다.
* 상단의 select box에서 telegraf.conf 파일에 설정한 hostGroupName 값을 찾아서 선택한다.
* 아래와 같이 왼쪽에 호스트 목록이 나오고, 호스트를 선택해서 system metric 데이터를 확인할 수 있다.

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-c894164f22ccffbbac3a17a452c9c99867ae5280%2Fsystem_metric_03.png?alt=media)

## 5 기타

* pinot에는 system metric 뿐만아니라 pinpoint의 다양한 메트릭 데이터와 통계 데이터를 저장할 예정이다. 즉 pinot는 다양한 데이터를 저장하는 목적으로 사용될 것이다.
* system metric의 경우 당분간은 beta 기능으로 제공할것이고 안정적으로 기능이 운영되는 경험이 쌓이면 공식적으로 기능을 제공할 것이다.
* 2.5.0 이하 버전에서 system metric 기능을 사용하다가 버전을 업그레이드 하는 경우 [guide](https://github.com/pinpoint-apm/pinpoint/issues/9791#issuecomment-1491486262) 설명을 참고하자.


# URI Statistics

[English](#uri_statistics) | [한국어](#URI_통계)

## URI Statistics

URI statistics menu is newly added to Pinpoint in v2.5.0.\
Pinpoint Agent aggregates URI templates and send them to Pinpoint collector via GRPC.\
Pinpoint Collector saves the data to Pinot via Apache Kafka.\
Pinpoint Web accesses Pinot to display the data.

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-766216ae1ef81bd7cf547351f746d5d7ccc833b7%2Furi_statistics_01.png?alt=media)

### 1. Installation and Configuration

#### 1.1 Install and Run Kafka

Kafka enables real-time streaming of URI statistics data from Pinpoint collector to Pinot.\
If you have already [set up Kafka for Pinpoint System Metric](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.2.a-kafka-installation-guide), please skip this step.

* Please refer to [this document](https://kafka.apache.org/quickstart) to get Kafka and start the Kafka environment.

#### 1.2 Create Kafka Topics for Pinpoint URI Statistics

Create a topic with the name `url-stat`

```
$ bin/kafka-topics.sh --create --topic url-stat --bootstrap-server ${YOUR_KAFKA_SERVER_ADDRESS}
```

#### 1.3 Install and Run Pinot

This section describes how to install Pinot which is used in Pinpoint to save URI statistics data.\
If you have already [set up Pinot for Pinpoint System Metric](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.1-install-pinot), please skip this step.

* Install Pinot according to [Pinot Getting Started guide](https://docs.pinot.apache.org/basics/getting-started).
* Above guide gives you the way to run Pinot locally, in Docker, and in Kubernetes.

#### 1.4 Create Pinot Tables

* Pinot table schema for Pinpoint URI statistics is provided in [our github repository](https://github.com/pinpoint-apm/pinpoint/tree/master/uristat/uristat-common/src/main/pinot).
* Please refer to [Pinot documents](https://docs.pinot.apache.org/basics/components/table#streaming-table-creation) to create necessary tables in your Pinot cluster.
* Let's create the uriStat table by referencing the schema file and table settings from the provided path. To enable hybrid table functionality, let's create both REALTIME and OFFLINE tables for the 'uriStat' table.

#### 1.5 Configure and Attach Pinpoint Agent

This section describes the URI stat configuration values added for URI statistics.

**1.5.1 Configuration values for URI Statistics**

Below are default agent configuration values for URI statistics.

```
###########################################################
# URI Stat
###########################################################
profiler.uri.stat.enable=true
profiler.uri.stat.spring.webmvc.enable=true
profiler.uri.stat.spring.webmvc.useuserinput=false
profiler.uri.stat.spring.webflux.enable=true
profiler.uri.stat.spring.webflux.useuserinput=false
profiler.uri.stat.vertx.enable=true
profiler.uri.stat.vertx.useuserinput=false
profiler.uri.stat.tomcat.useuserinput=false
```

* profiler.uri.stat.enable: whether Pinpoint Agent collects URI statistics or not.
  * `true`: collects URI statistics
  * `false`: doesn't collect URI statistics
* profiler.uri.stat.spring.webmvc.enable: whether Pinpoint Agent collects URI statistics from Spring Web MVC applications.
  * `true`: collects URI statistics from Spring Web MVC applications.
  * `false`: doesn't collect URI statistics from Spring Web MVC applications.
* profiler.uri.stat.spring.webmvc.useuserinput: whether Pinpoint Agent uses user-input request attribute values for URI templates when available.

  * `true`: uses user-input request attribute values.
  * `false`: ignores user-input request attribute values.

  Set attribute `pinpoint.metric.uri-template` to your Spring web request as shown below to override default URI template provided by Pinpoint.

  ```
    @RequestMapping("/testUserInputRequestAttribute")
    public Map<String, Object> testUserInputAttribute(HttpServletRequest request) {
        Map<String, Object> map = new HashMap<String, Object>();
        map.put("message", "test user input attribute");
        request.setAttribute("pinpoint.metric.uri-template", "/userInput");
        return map;
    }
  ```
* profiler.uri.stat.spring.webflux.enable: whether Pinpoint Agent collects URI statistics from Spring Webflux applications.
  * `true`: collects URI statistics from Spring Webflux applications.
  * `false`: doesn't collect URI statistics from Spring Webflux applications.
* profiler.uri.stat.spring.webflux.useuserinput: whether Pinpoint Agent uses user-input request attribute values for URI templates when available.

  * `true`: uses user-input request attribute values.
  * `false`: ignores user-input request attribute values.

  Set attribute `pinpoint.metric.uri-template` to your Spring web request as shown below to override default URI template provided by Pinpoint.

  ```
    @GetMapping("/server/welcome/**")
    public Mono<String> welcome(ServerWebExchange exchange) {
        exchange.getAttributes().put("pinpoint.metric.uri-template", "/test");
        return Mono.just("Welcome Home");
    }
  ```
* profiler.uri.stat.vertx.enable: whether Pinpoint Agent collects URI statistics from Vert.x applications.
  * `true`: collects URI statistics from Vert.x applications.
  * `false`: doesn't collect URI statistics from Vert.x applications.
* profiler.uri.stat.vertx.useuserinput: whether Pinpoint Agent uses user-input routing context attribute values for URI templates when available.

  * `true`: uses user-input routing context attribute values.
  * `false`: ignores user-input routing context attribute values.

  Set attribute `pinpoint.metric.uri-template` to your Vert.x routing context as shown below to override default URI template provided by Pinpoint.

  ```
    router.get("/routinContextAttributeAdded").handler(routingContext -> {
        routingContext.put("pinpoint.metric.uri-template", "/test");
        routingContext.response().end("pinpoint.metric.uri-tempate = /test");
    });
  ```
* profiler.uri.stat.tomcat.useuserinput: (Added in v2.5.3) whether Pinpoint Agent uses user-input attribute values from Tomcat for URI templates when available.

  * `true`: collects URI statics from Tomcat user-input attribute values.
  * `false`: doesn't check Tomcat request attributes for URI statistics.

  This is provided to collect URI statistics information in Tomcat applications without supported frameworks(Spring WebMVC, Spring Webflux, VertX).\
  If you are using supported frameworks, it is recommended to use framework-specific options and disable this option.\
  Since there is no default URI template provided by tomcat, users need to set attribute `pinpoint.metric.uri-template` to your Tomcat request to start collecting URI statistics information.

To change the configuration values described above, update `pinpoint.config` under [each profile directory](https://github.com/pinpoint-apm/pinpoint/tree/master/agent/src/main/resources/profiles) and rebuild the project.\
Or, you can simply pass these properties when starting your application with Pinpoint Agent (e.g. `-Dprofiler.uri.stat.enable=false`).

#### 1.6 Configure and Run Pinpoint Collector & Web with URI Statistics

Instead of the default Pinpoint Collector and Web binaries, you should use those compiled under metric-module.

Please check [here](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.3-configure-and-run-pinpoint-collector-with-system-metrics) for Pinpoint Metric Collector properties.

* Enable URI statistics by adding the below line at [pinpoint-collector.properties](https://github.com/pinpoint-apm/pinpoint/tree/master/metric-module/collector-starter/src/main/resources/profiles):

  ```
  collector.stat.uri=true
  ```
* `pinpoint.collector.type=BASIC` argument should be used to collect URI statistics in collector.

Please check [here](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.4-configure-and-run-pinpoint-web-with-system-metrics) for Pinpoint Metric Web properties.

* Enable URI statistics by adding the below line at [pinpoint-web-uristat.properties](https://github.com/pinpoint-apm/pinpoint/tree/master/uristat/uristat-web/src/main/resources/profiles):

  ```
  config.show.urlStat=true
  ```

### 2. View Collected URI Statistics Data

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-478271df836f370ea719470568b103ee42d51a81%2Furi_statistics_02.png?alt=media)

1. Click `URL Statistic` on the side bar menu in Pinpoint web.
2. Search for the application name you used to configure Pinpoint Agent.
3. Top 50 URIs used in your application will be displayed below the empty chart.
4. Click each URI to load the chart.

## URI 통계

URI 통계 기능은 핀포인트 v2.5.0에 신규로 추가되었다.\
핀포인트 에이전트에서 URI 템플릿 정보를 수집하여 GRPC를 사용해 핀포인트 콜렉터에 전달하고, 핀포인트 콜렉터는 아파치 카프카를 통해 아파치 피노에 값을 저장한다.\
핀포인트 웹에서 저장된 URI 통계 데이터를 확인할 수 있다.

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-766216ae1ef81bd7cf547351f746d5d7ccc833b7%2Furi_statistics_01.png?alt=media)

### 1. 설치 및 설정 방법

#### 1.1 카프카 설치 및 실행

실시간으로 핀포인트 콜렉터에서 데이터를 전달받아 피노에 저장하기 위해서 카프카를 설치해야 한다.\
이미 [시스템 메트릭 설정을 하면서 카프카를 설치](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.2-kafka)하였다면, 이 부분은 건너뛰십시오.

* [설치 방법 가이드](https://kafka.apache.org/quickstart)를 참고하여 kafka를 설치한다.

#### 1.2 카프카 토픽 생성

아래와 같이 `url-stat` 토픽을 생성한다.

```
$ bin/kafka-topics.sh --create --topic url-stat --bootstrap-server ${YOUR_KAFKA_SERVER_ADDRESS}
```

#### 1.3 피노 설치 및 실행

URI 통계 값을 저장하는 피노를 설치하는 법을 안내한다.\
이미 [시스템 메트릭 설정을 하면서 피노를 설치](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.1.a.-pinot)하였다면, 이 부분은 건너뛰십시오.

* [피노 설치 가이드](https://docs.pinot.apache.org/basics/getting-started)를 참고하여 피노를 설치한다.
* 다양한 환경 (local, docker, kubernetes)에서 피노 실행 환경을 구성할 수 있으니 위 가이드를 참고하자.

#### 1.4 피노 테이블 스키마 및 테이블 생성

* [핀포인트 깃헙 저장소](https://github.com/pinpoint-apm/pinpoint/tree/master/uristat/uristat-common/src/main/pinot)에 URI 통계를 위한 피노 테이블 스키마와 테이블 정보가 있다.
* 위 경로에서 스키마 파일과 테이블 설정을 참고해서 `uriStat` 테이블을 생성한다. hybrid table 기능 사용을 위해서 REALTIME, OFFLINE 테이블 둘다 생성하자.
* 피노에 필요한 테이블을 구성하는 방법은 [피노 공식 문서](https://docs.pinot.apache.org/basics/components/table#streaming-table-creation)를 참고하자.

#### 1.5 핀포인트 에이전트 설정

URI 통계 수집을 위해 핀포인트 에이전트에 설정해야 하는 값들을 안내한다.

**1.5.1 URI 통계 수집을 위한 설정 값**

URI 통계 수집과 관련된 핀포인트 에이전트의 설정 기본값들은 아래와 같다.

```
###########################################################
# URI Stat
###########################################################
profiler.uri.stat.enable=true
profiler.uri.stat.spring.webmvc.enable=true
profiler.uri.stat.spring.webmvc.useuserinput=false
profiler.uri.stat.spring.webflux.enable=true
profiler.uri.stat.spring.webflux.useuserinput=false
profiler.uri.stat.vertx.enable=true
profiler.uri.stat.vertx.useuserinput=false
profiler.uri.stat.tomcat.useuserinput=false
```

* profiler.uri.stat.enable: 핀포인트 에이전트가 URI 통계를 수집하는지 여부.
  * `true`: URI 통계를 수집한다.
  * `false`: URI 통계를 수집하지 않는다.
* profiler.uri.stat.spring.webmvc.enable: 핀포인트 에이전트가 스프링 웹 MVC 어플리케이션에서 URI 통계를 수집하는지 여부.
  * `true`: 스프링 웹 MVC 어플리케이션에서 URI 통계를 수집힌다.
  * `false`: 스프링 웹 MVC 어플리케이션에서 URI 통계를 수집하지 않는다.
* profiler.uri.stat.spring.webmvc.useuserinput: 핀포인트 에이전트가 스프링 웹 어플리케이션에서 사용자 정의 URI 템플릿을 우선적으로 사용하는지 여부.

  * `true`: 스프링 웹 어플리케이션에서 사용자 정의 URI 템플릿을 우선적으로 사용한다.
  * `false`: 스프링 웹 어플리케이션에서 사용자 정의 URI 템플릿을 확인하지 않고 핀포인트가 수집한 템플릿만 사용한다.

  핀포인트에서 수집하는 URI 템플릿을 사용하지 않고 사용자 정의 URI 템플릿을 사용하고 싶다면, 아래 예제와 같이 스프링 웹 리퀘스트 객체 attribute에 `pinpoint.metric.uri-template`를 key 값으로 하는 속성 값을 설정해야 한다.

  ```
    @RequestMapping("/testUserInputRequestAttribute")
    public Map<String, Object> testUserInputAttribute(HttpServletRequest request) {
        Map<String, Object> map = new HashMap<String, Object>();
        map.put("message", "test user input attribute");
        request.setAttribute("pinpoint.metric.uri-template", "/userInput");
        return map;
    }
  ```
* profiler.uri.stat.spring.webflux.enable: 핀포인트 에이전트가 스프링 웹플럭스 어플리케이션에서 URI 통계를 수집하는지 여부.
  * `true`: 스프링 웹플럭스 어플리케이션에서 URI 통계를 수집힌다.
  * `false`: 스프링 웹플럭스 어플리케이션에서 URI 통계를 수집하지 않는다.
* profiler.uri.stat.spring.webflux.useuserinput: 핀포인트 에이전트가 스프링 웹플럭스 어플리케이션에서 사용자 정의 URI 템플릿을 우선적으로 사용하는지 여부.

  * `true`: 스프링 웹플럭스 어플리케이션에서 사용자 정의 URI 템플릿을 우선적으로 사용한다.
  * `false`: 스프링 웹플럭스 어플리케이션에서 사용자 정의 URI 템플릿을 확인하지 않고 핀포인트가 수집한 템플릿만 사용한다.

  핀포인트에서 수집하는 URI 템플릿을 사용하지 않고 사용자 정의 URI 템플릿을 사용하고 싶다면, 아래 예제와 같이 스프링 웹 리퀘스트 객체 attribute에 `pinpoint.metric.uri-template`를 key 값으로 하는 속성 값을 설정해야 한다.

  ```
    @GetMapping("/server/welcome/**")
    public Mono<String> welcome(ServerWebExchange exchange) {
        exchange.getAttributes().put("pinpoint.metric.uri-template", "/test");
        return Mono.just("Welcome Home");
    }
  ```
* profiler.uri.stat.vertx.enable: 핀포인트 에이전트가 Vert.x 어플리케이션에서 URI 통계를 수집하는지 여부.
  * `true`: Vert.x 어플리케이션에서 URI 통계를 수집힌다.
  * `false`: Vert.x 어플리케이션에서 URI 통계를 수집하지 않는다.
* profiler.uri.stat.vertx.useuserinput: 핀포인트 에이전트가 Vert.x 어플리케이션에서 사용자 정의 URI 템플릿을 우선적으로 사용하는지 여부.

  * `true`: Vert.x 어플리케이션에서 사용자 정의 URI 템플릿을 우선적으로 사용한다.
  * `false`: Vert.x 어플리케이션에서 사용자 정의 URI 템플릿을 확인하지 않고 핀포인트가 수집한 템플릿만 사용한다.

  핀포인트에서 수집하는 URI 템플릿을 사용하지 않고 사용자 정의 URI 템플릿을 사용하고 싶다면, 아래 예제와 같이 Vert.x RoutingContext 객체에 `pinpoint.metric.uri-template` 를 key 값으로 하는 속성 값을 설정해야 한다.

  ```
    router.get("/routinContextAttributeAdded").handler(routingContext -> {
        routingContext.put("pinpoint.metric.uri-template", "/test");
        routingContext.response().end("pinpoint.metric.uri-tempate = /test");
    });
  ```
* profiler.uri.stat.tomcat.useuserinput: (v2.5.3에 추가 됨) 핀포인트 에이전트가 Tomcat 어플리케이션에서 사용자 정의 URI 템플릿을 사용하여 통계를 수집하는지 여부.

  * `true`: Tomcat 어플리케이션에서 사용자 정의 URI 템플릿을 사용하여 URI 통계를 수집한다.
  * `false`: URI 통계 수집을 할 때 Tomcat 리퀘스트 attribute를 확인하지 않는다.

  이 옵션은 지원하는 프레임워크(Spring WebMVC, Spring Webflux, VertX)를 사용하지 않는 Tomcat 어플리케이션에서 URI 통계를 수집하기 위해 추가되었습니다.\
  만약 지원하는 프레임워크를 사용하고 있다면, 해당 프레임워크 관련 URI 통계 옵션을 사용하고 이 옵션은 false로 사용하는 것을 권장합니다.\
  지원하는 프레임워크에서와는 다르게 Tomcat 자체적으로 URI 템플릿을 제공하지 않기 때문에, 이 옵션을 사용할 경우, 사용자가 직접 Tomcat request attribute에 `pinpoint.metric.uri-template`를 추가하여야만 URI 통계가 수집됩니다.

위 설정 값들을 변경하려면 원하는 [핀포인트 프로파일 경로](https://github.com/pinpoint-apm/pinpoint/tree/master/agent/src/main/resources/profiles)의 `pinpoint.config` 파일에서 값을 변경하여 핀포인트를 재빌드한다. 파일을 수정하지 않고, 핀포인트 에이전트를 붙힐 어플리케이션을 실행할 때 `-Dprofiler.uri.stat.enable=false`와 같이 값을 넣어도 된다.

#### 1.6 핀포인트 콜렉터와 핀포인트 웹 설정 및 실행

URI 통계를 수집하고 값을 확인하려면, 핀포인트 v2.5.0 이전 버전에서 사용하던 콜렉터와 웹 JAR 파일이 아니라 metric-module 밑에 생성되는 파일을 사용해야 한다.

[핀포인트 메트릭 콜렉터를 설명한 문서](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.3-collector)에 자세한 설명이 있으니 참고해서 메트릭 콜렉터 설정값을 세팅하자.

* 위 설정 외에 URI 통계를 위해 [pinpoint.collector.properties](https://github.com/pinpoint-apm/pinpoint/tree/master/metric-module/collector-starter/src/main/resources/profiles)에 아래 설정값이 추가되었다:

  ```
  collector.stat.uri=true
  ```
* URI 통계를 수집하기 위해서는 콜렉터를 시작할 때 `pinpoint.collector.type=BASIC` argument를 넣어야 한다.

[핀포인트 메트릭 웹을 설명한 문서](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.4-web)에 자세한 설명이 있으니 참고해서 메트릭 웹 설정값을 세팅하자.

* 위 설정 외에 URI 통계를 위해 [pinpoint-web-uristat.properties](https://github.com/pinpoint-apm/pinpoint/tree/master/uristat/uristat-web/src/main/resources/profiles)에 아래 설정값이 추가되었다:

  ```
  config.show.urlStat=true
  ```

### 2. URI 통계 데이터 조회

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-478271df836f370ea719470568b103ee42d51a81%2Furi_statistics_02.png?alt=media)

1. 핀포인트 메트릭 웹을 실행하여 왼쪽 `URL Statistic` 메뉴를 선택한다.
2. 상단의 seslect box에서 핀포인트 에이전트에 설정한 어플리케이션 이름을 조회한다..
3. 초기 화면에서는 선택한 어플리케이션에서 가장 많이 사용한 상위 50개 URI가 빈 차트 밑에 표시된다.
4. 원하는 URI를 클릭하면 차트에 데이터가 표시된다.


# URI Statistics Alarm

## URI Statistics Alarms

Alarms for URI statistics will be introduced to Pinpoint in v3.0.0.\
Similar to the existing [alarms in Pinpoint](https://pinpoint-apm.gitbook.io/pinpoint/documents/alarm), pinpoint-batch server checks every 3 minutes if configured alarm rules are triggered with data in the last 5 minutes.

### 1. Alarm Rules

Alarms rules can be created for each URI, using data collected with [URI Statistics](https://pinpoint-apm.gitbook.io/pinpoint/documents/uri_statistics).

#### Alarm Data

* APDEX: The APDEX score of the specified URI for the past 5 minutes (0.00 \~ 1.00)
* Average Response Time: The avgerage response time of the specified URI for the past 5 minutes (ms)
* Maximum Response Time: The maximum response time of the specified URI for the past 5 minutes (ms)
* Total Request Count: The total number of requests made to the specified URI in the past 5 minutes
* Failed Request Count: The number of failed requests to the specified URI in the past 5 minutes

#### Alarm Condition

When setting up a new alarm, the conditions for triggering the alarm need to be specified.\
You can choose from the following comparison operators:

* (collected value) `>` (threshold value)
* (collected value) `>=` (threshold value)
* (collected value) `==` (threshold value)
* (collected value) `<` (threshold value)
* (collected value) `<=` (threshold value)

### 2. Configuration and Implementation

To use URI Statistics Alarms, MYSQL table `pinot_alarm_history`, `pinot_alarm_rule`, and `pinot_webhook_send` need to be added.

```
CREATE TABLE `pinot_alarm_history` (
  `history_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `rule_id` int(10) unsigned NOT NULL,
  `timestamp` datetime NOT NULL,
  PRIMARY KEY (`history_id`)
);
```

```
CREATE TABLE `pinot_alarm_rule` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `service_name` varchar(30) NOT NULL,
  `application_name` varchar(30) NOT NULL,
  `category_name` varchar(30) NOT NULL,
  `checker_name` varchar(30) NOT NULL,
  `target` varchar(256) NOT NULL,
  `condition` varchar(30) NOT NULL,
  `threshold` decimal(10,2) DEFAULT NULL,
  `baseline` varchar(30) DEFAULT NULL,
  `user_group_id` varchar(30) NOT NULL,
  `sms_send` char(1) DEFAULT NULL,
  `email_send` char(1) DEFAULT NULL,
  `webhook_send` char(1) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
```

```
CREATE TABLE `pinot_webhook_send` (
  `webhook_send_info_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `webhook_id` int(10) unsigned NOT NULL,
  `rule_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`webhook_send_info_id`),
  UNIQUE KEY `webhook_send_info_id_UNIQUE` (`webhook_send_info_id`)
);
```

### 3. How to add alarms on Web UI

(TO BE UPDATED)

## URI 통계 알람

[URI 통계](https://pinpoint-apm.gitbook.io/pinpoint/documents/uri_statistics)를 이용한 알람 기능은 핀포인트 2.6.0에 추가되었습니다.\
기존 [핀포인트 알람](https://pinpoint-apm.gitbook.io/pinpoint/documents/alarm)에서와 동일하게 pinpoint-batch 서버가 매 3분동안 지난 5분간의 데이터가 알람 조건을 만족하는 지 체크합니다.

### 1. 설정 가능한 알람

[URI 통계](https://pinpoint-apm.gitbook.io/pinpoint/documents/uri_statistics) 기능으로 수집한 통계값을 사용하여 특정 URI에 대해 아래와 같은 조건으로 알람을 설정할 수 있습니다.

#### 알람 대상 데이터

* APDEX: 해당 URI의 과거 5분 동안의 APDEX 점수 (0.00 \~ 1.00)
* 평균 응답 속도: 해당 URI의 과거 5분 동안의 평균 응답 속도 (ms)
* 최대 응답 속도: 해당 URI의 과거 5분 동안의 최대 응답 속도 (ms)
* 전체 요청 수: 해당 URI의 과거 5분 동안의 전체 request 개수
* 실패 요청 수: 해당 URI의 과거 5분 동안 실패한 request의 개수

#### 알람 조건

새로운 알람을 등록할 때 수집한 값이 지정한 임계값과 비교해서 어떤 조건일 때 알람이 울리는 지 설정하게 됩니다.\
다음 비교 연산자 중에서 선택할 수 있고 아래 조건이 만족하면 알람이 울립니다.

* (수집한 값) `>` (설정한 값)
* (수집한 값) `>=` (설정한 값)
* (수집한 값) `==` (설정한 값)
* (수집한 값) `<` (설정한 값)
* (수집한 값) `<=` (설정한 값)

### 2. 설치 및 설정 방법

URI 통계 알람을 사용하기 위해서는 MYSQL table 세 개( `pinot_alarm_history`, `pinot_alarm_rule`, `pinot_webhook_send`)를 추가해야 합니다.

```
CREATE TABLE `pinot_alarm_history` (
  `history_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `rule_id` int(10) unsigned NOT NULL,
  `timestamp` datetime NOT NULL,
  PRIMARY KEY (`history_id`)
);
```

```
CREATE TABLE `pinot_alarm_rule` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `service_name` varchar(30) NOT NULL,
  `application_name` varchar(30) NOT NULL,
  `category_name` varchar(30) NOT NULL,
  `checker_name` varchar(30) NOT NULL,
  `target` varchar(256) NOT NULL,
  `condition` varchar(30) NOT NULL,
  `threshold` decimal(10,2) DEFAULT NULL,
  `baseline` varchar(30) DEFAULT NULL,
  `user_group_id` varchar(30) NOT NULL,
  `sms_send` char(1) DEFAULT NULL,
  `email_send` char(1) DEFAULT NULL,
  `webhook_send` char(1) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
```

```
CREATE TABLE `pinot_webhook_send` (
  `webhook_send_info_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `webhook_id` int(10) unsigned NOT NULL,
  `rule_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`webhook_send_info_id`),
  UNIQUE KEY `webhook_send_info_id_UNIQUE` (`webhook_send_info_id`)
);
```

### 3. 알람 추가하는 법

\[ Web 구현 후 추가 예정]


# Error Analysis

[English](#error_analysis) | [한국어](#1.설치_및_설정_방법)

## Error Analysis

![](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-66f5caa12ca010e28eb6c3e1bce69e98e300ea2f%2Ferror_analysis_01.png?alt=media)

Error Analysis is a new feature introduced in Pinpoint v3.0.0.

The Pinpoint agent collects more detailed exception information and transmits it to the Pinpoint collector via gRPC. The Pinpoint collector then stores this data in Apache Pinot through Apache Kafka. You can view the stored Error Analysis data in the Pinpoint web interface.

## 1. Installation and Configuration Guide

### 1.1. Kafka Installation and Configuration

To store data from the Pinpoint Collector into Pinot, Kafka needs to be installed. If you have already installed Kafka during the [system metric setup](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.2-kafka), you can skip this section.

#### 1.1.1. Kafka Installation

Refer to the [Kafka Quickstart Guide](https://kafka.apache.org/quickstart) for detailed instructions on installing Kafka.

#### 1.1.2. Kafka Topic Creation

You need to create a topic named `exception-trace`.\
Use the following command to create the `exception-trace` topic:

```shell
$ bin/kafka-topics.sh --create --topic exception-trace --bootstrap-server ${YOUR_KAFKA_SERVER_ADDRESS}
```

### 1.2. Pinot Installation and Configuration

To store collected data, Pinot must be installed. If you have already completed the Pinot installation during the [system metric setup](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.1.a.-pinot), you can skip this section.

#### 1.2.1. Pinot Installation

Refer to the [Pinot Getting Started Guide](https://docs.pinot.apache.org/basics/getting-started) for detailed instructions on installing Pinot. Pinot can be set up in various environments (local, Docker, Kubernetes), so follow the guide that best fits your setup.

Pinpoint Error Analysis requires [CLP (Compressed Log Processor)](https://docs.pinot.apache.org/basics/data-import/clp), supported from Pinot version 1.0.0, to appropriately process and group error messages. Please ensure you are using the correct version.

Due to the binary issue with `clp-ffi-java`, we recommend using an amd64-based / x86-based machine when installing Pinot version 1.0.0. [Related Issue](https://github.com/pinpoint-apm/pinpoint/issues/11170)

#### 1.2.2. Pinot Table Schema and Table Creation

Create the following table in Pinot:

* `exceptionTrace`

Refer to the [table schema file](https://github.com/pinpoint-apm/pinpoint/tree/master/exceptiontrace/exceptiontrace-common/src/main/pinot) for details on creating the table.

### 1.3. Pinpoint Agent Configuration

This section covers the settings related to Error Analysis data collection. The default settings for the release profile are as follows:

```config
###########################################################
# Exception Trace
###########################################################
profiler.exceptiontrace.enable=true
# Permits per second
profiler.exceptiontrace.new.throughput=1000
profiler.exceptiontrace.errormessage.max=2048
# Permits depth of exception. if max depth is 0, it is unlimited.
profiler.exceptiontrace.max.depth=5
profiler.exceptiontrace.io.buffering.buffersize=20
```

* `profiler.exceptiontrace.enable`
  * `true`: Collects exceptions that occur. **Default**
  * `false`: Does not collect exceptions that occur.
* `profiler.exceptiontrace.new.throughput`
  * **Default**: `1000`
  * Determines how many exceptions per second to collect from the agent.
* `profiler.exceptiontrace.errormessage.max`
  * **Default**: `2048`
  * Determines the maximum length of the error message for exceptions collected by the agent.
* `profiler.exceptiontrace.max.depth`
  * **Default**: `5`
  * Determines the depth to traverse the exception chain.
  * If the value is 0, it will traverse until `Throwable.getCause()` returns null.
* `profiler.exceptiontrace.io.buffering.buffersize`
  * **Default**: `20`
  * Determines the number of exceptions to buffer.
  * This buffer is approximately the size of the buffer generated per Span.

### 1.4. Pinpoint Collector and Web Configuration and Execution

#### 1.4.1. Collector Configuration and Execution

The collector configuration is basically the same as for system metrics. Refer to the [Pinpoint Metric Collector](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.3-collector) documentation for detailed setup instructions.

In addition to setting the addresses for Pinot and Kafka and enabling metric collection, ensure that `pinpoint.modules.collector.exceptiontrace.enabled=true` is set to enable exception storage. **Default**: `true`

#### 1.4.2. Web Configuration and Execution

The web configuration is essentially the same as for system metrics. Refer to the [Pinpoint Metric Web](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.4-web) documentation for detailed setup instructions.

Additionally, ensure that `pinpoint.modules.web.exceptiontrace.enabled=true` is set to enable reading exception data. **Default**: `true`

For Error Analysis, the following setting is added to `pinpoint-web-metric.properties` to control whether the Error Analysis item is displayed in the side menu. **Default**: `true`

```config
config.show.exceptionTrace=true
```

***

## Error Analysis

Error Analysis 는 핀포인트 v3.0.0 에 신규로 추가되었다.\
핀포인트 에이전트에서 보다 상세한 Exception 정보를 수집하여 gRPC 를 통해 핀포인트 콜렉터로 전달한다.\
핀포인트 콜렉터는 이를 아파치 카프카를 통해 아파치 피노에 값을 저장한다.\
핀포인트 웹에서 저장된 Error Analysis 를 확인할 수 있다.

## 1. 설치 및 설정 방법

### 1.1. 카프카 Kafka 설치 및 설정

핀포인트 콜렉터에서 피노Pinot 에 데이터를 저장하기 위해서는 카프카를 설치해야한다. 이미 [시스템 메트릭 설정](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.2-kafka) 과정 중에 카프카를 설치하였다면, 이 부분은 건너뛴다.

#### 1.1.1. 카프카 Kafka 설치

[설치 방법 가이드](https://kafka.apache.org/quickstart)를 참고하여 kafka를 설치한다.

#### 1.1.2. 카프카 Kafka 토픽 생성

`exception-trace` 라는 이름의 topic 을 생성해야 한다.\
아래와 같이 `exception-trace` 토픽을 생성한다.

```shell
$ bin/kafka-topics.sh --create --topic exception-trace --bootstrap-server ${YOUR_KAFKA_SERVER_ADDRESS}
```

### 1.2. 피노 Pinot 설치 및 설정

수집된 데이터를 저장하기 위해서는 피노 Pinot 를 설치해야한다. 이미 [시스템 메트릭 설정](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.1.a.-pinot) 과정 중에 피노를 설치하였다면, 이 부분은 건너뛴다.

#### 1.2.1. 피노 Pinot 설치

[피노 설치 가이드](https://docs.pinot.apache.org/basics/getting-started)를 참고하여 피노를 설치한다.\
다양한 환경 (local, docker, kubernetes)에서 피노 실행 환경을 구성할 수 있으니 위 가이드를 참고하자.

핀포인트는 Error Message 를 적절히 처리하고 그룹화하기 위해 Pinot 1.0.0 부터 지원하는 [CLP (Compressed Log Processor)](https://docs.pinot.apache.org/basics/data-import/clp) 가 필요하다. 버전에 주의할 것.

#### 1.2.2. 피노 Pinot 테이블 스키마 및 테이블 생성

피노 Pinot 에 다음 테이블을 새로 생성한다.

* `exceptionTrace`[테이블 생성 스키마 파일](https://github.com/pinpoint-apm/pinpoint/tree/master/exceptiontrace/exceptiontrace-common/src/main/pinot)의 테이블 정보를 참고하여 생성한다.

### 1.3 핀포인트 에이전트 설정

Error Analysis 데이터 수집과 관련된 설정이다.\
release 프로필의 기본 설정은 다음과 같다.

```config
###########################################################
# Exception Trace
###########################################################
profiler.exceptiontrace.enable=true
# Permits per second
profiler.exceptiontrace.new.throughput=1000
profiler.exceptiontrace.errormessage.max=2048
# Permits depth of exception. if max depth is 0, it is unlimited.
profiler.exceptiontrace.max.depth=5
profiler.exceptiontrace.io.buffering.buffersize=20
```

* `profiler.exceptiontrace.enable`
  * `true`: 발생하는 exception 을 수집한다. **기본값**
  * `false` : 발생하는 exception 을 수집하지 않는다.
* `profiler.exceptiontrace.new.throughput`
  * **기본값** 1000
  * 해당 에이전트에서 초당 몇개까지의 exception 을 수집할지 결정한다.
* `profiler.exceptiontrace.errormessage.max`
  * **기본값** 2048
  * 해당 에이전트에서 발생하는 exception 의 error message 를 몇자까지 수집할지 결정한다.
* `profiler.exceptiontrace.max.depth`
  * **기본값** 5
  * exception chain 이 주어졌을 때, 깊이를 어느정도 순회할지 결정한다.
  * 값이 0이면 Throwable.getCause() 가 null 일 때까지 순회한다.
* `profiler.exceptiontrace.io.buffering.buffersize`
  * **기본값** 20
  * buffer 에 exception 을 몇개까지 쌓아둘지 결정한다.
  * 해당 buffer 는 대략 Span 단위로 생성되는 buffer 이다.

### 1.4 핀포인트 콜렉터와 핀포인트 웹 설정 및 실행

### 1.4.1. collector 설정 및 실행

collector 설정은 기본적으로 system metric 와 동일하다.[핀포인트 메트릭 콜렉터](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.3-collector)를 설명한 문서에 자세한 설명이 있으니 참고해서 메트릭 콜렉터 설정값을 세팅하자.

이처럼 pinot 과 kafka 의 주소를 알려주고 metric 수집 기능을 활성화하면 된다.

이에 추가적으로`pinpoint.modules.collector.exceptiontrace.enabled=true`\
로 되어있어야 exception 을 저장한다. **기본값** `true`

### 1.4.2 web 설정 및 실행

web 설정은 기본적으로 system metric 와 동일하다.[핀포인트 메트릭 웹](https://pinpoint-apm.gitbook.io/pinpoint/documents/system_metric#3.4-web)을 설명한 문서에 자세한 설명이 있으니 참고해서 메트릭 웹 설정값을 세팅하자.

이에 추가적으로`pinpoint.modules.web.exceptiontrace.enabled=true`\
로 되어있어야 exception 데이터를 읽어온다. **기본값** `true`

위 설정 외에 Error Analysis 를 위해 pinpoint-web-metric.properties에 아래 설정값이 추가되었다:\
이 설정은 좌측 사이드 메뉴에서 Error Analysis 항목을 노출시킬지 결정한다.**기본값**`true`

* ```
    config.show.exceptionTrace=true
  ```


# How to use Application Inspector

[English](#application-inspector) | [한국어](#application-inspector-1)

## Application Inspector

### 1. Introduction

Application inspector provides an aggregate view of all the agent's resource data (cpu, memory, tps, datasource connection count, etc) registered under the same application name. A separate view is provided for the application inspector with stat charts similar to the agent inspector.

To access application inspector, click on the application inspector menu on the left side of the screen.

* 1 : application inspector menu, 2 : application stat data

  ![inspector\_view.jpg](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-1db8d686fb94a6f086fd1b0c665759237de98e86%2Finspector_view.jpg?alt=media)

The Heap Usage chart above for example, shows the average(Avg), smallest(Min), greatest(Max) heap usage of the agents registered under the same application name along with the id of the agent that had the smallest/greatest heap usage at a certain point in time. The application inspector also provides other statistics found in the agent inspector in a similar fashion.

![graph.jpg](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-1b9fe2dfc5933f8a6d8dcfee8cf77076489f34c7%2Fgraph.jpg?alt=media)

Application inspector requires [flink](https://flink.apache.org) and [zookeeper](https://zookeeper.apache.org/). Please read on for more detail.

### 2. Architecture

![execute\_flow.jpg](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-67c467a049c249107c3d9f9c23d24c98270ddfd1%2Fexecute_flow.jpg?alt=media)

**A.** Run a streaming job on [flink](https://flink.apache.org).\
**B.** The taskmanager server is registered to zookeeper as a data node once the job starts.\
**C.** The Collector obtains the flink server info from zookeeper to create a tcp connection with it and starts sending agent data.\
**D.** The flink server aggregates data sent by the Collector and stores them into hbase.

### 3. Configuration

In order to enable application inspector, you will need to do the following and run Pinpoint.

**A.** Create **ApplicationStatAggre** table (refer to [create table script](https://github.com/pinpoint-apm/pinpoint/tree/master/hbase/scripts)), which stores application stat data.

**B.** Configure zookeeper address in [Pinpoint-flink.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/flink/src/main/resources/pinpoint-flink.properties) which will be used to store flink's taskmanager server information.

```
    flink.cluster.enable=true
    flink.cluster.zookeeper.address=YOUR_ZOOKEEPER_ADDRESS
    flink.cluster.zookeeper.sessiontimeout=3000
    flink.cluster.zookeeper.retry.interval=5000
    flink.cluster.tcp.port=19994
```

**C.** Configure job execution type and the number of listeners to receive data from the Collector in [Pinpoint-flink.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/flink/src/main/resources/profiles/release/pinpoint-flink.properties).

* If you are running a flink cluster, set *flink.StreamExecutionEnvironment* to **server**.
* If you are running flink as a standalone, set *flink.StreamExecutionEnvironment* to **local**.

  ```
    flink.StreamExecutionEnvironment=server
  ```

**D.** Configure hbase address in [hbase.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/flink/src/main/resources/profiles/release/hbase.properties) which will be used to store aggregated application data.

```
    hbase.client.host=YOUR_HBASE_ADDRESS
    hbase.client.port=2181
```

**E.** Build [Pinpoint-flink](https://github.com/pinpoint-apm/pinpoint/tree/master/flink) and run the streaming job file created under *target* directory on the flink server.

* The name of the streaming job is `pinpoint-flink-job-{pinpoint.version}.jar`.
* For details on how to run the job, please refer to the [flink website](https://flink.apache.org).
* You must put `spring.profiles.active release` or`spring.profiles.active local` as the job parameter so that the job can refer to the configuration file configured above when running. It must be entered because it uses the spring profile function inside the job to refer to the configuration file.

**F.** Configure zookeeper address in [Pinpoint-Collector.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/collector/src/main/resources/profiles/release/pinpoint-collector.properties) so that the Collector can connect to the flink server.

```
    flink.cluster.enable=true
    flink.cluster.zookeeper.address=YOUR_ZOOKEEPER_ADDRESS
    flink.cluster.zookeeper.sessiontimeout=3000
```

**G.** Enable application inspector in the web-ui by enabling the following configuration in [pinpoint-web.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/resources/pinpoint-web-root.properties).

```
    config.show.applicationStat=true
```

### 4. Monitoring Streaming Jobs

There is a batch job that monitors how Pinpoint streaming jobs are running. To enable this batch job, configure the following files for *Pinpoint-web*.

**batch.properties**

```
batch.flink.server=FLINK_MANGER_SERVER_IP_LIST
# Flink job manager server IPs, separated by ','.
# ex) batch.flink.server=123.124.125.126,123.124.125.127
```

**applicationContext-batch-schedule.xml**

```markup
<task:scheduled-tasks scheduler="scheduler">
    ...
    <task:scheduled ref="batchJobLauncher" method="flinkCheckJob" cron="0 0/10 * * * *" />
</task:scheduled-tasks>
```

If you would like to send alarms in case of batch job failure, you must implement `com.navercorp.pinpoint.web.batch.JobFailMessageSender class` and register it as a Spring bean.

### 5. Others

For more details on how to install and operate flink, please refer to the [flink website](https://flink.apache.org).

## Application Inspector

### 1. 기능 설명

application inspector 기능은 agent들의 리소스 데이터(stat : cpu, memory, tps, datasource connection count)를 집계하여 데이터를 보여주는 기능이다. 참고로 application은 agent의 그룹으로 이뤄진다. 그리고 agent의 리소스 데이터는 agent inspector 화면에서 에서 볼 수 있다. application inspector 기능 또한 별도의 화면에서 확인할 수 있다.

inspector 화면 왼쪽 메뉴의 링크를 클릭하면 application inspector 버튼을 클릭하고 데이터를 볼 수 있다.

* 1 : application inspector menu, 2: application stat data

  ![inspector\_view.jpg](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-1db8d686fb94a6f086fd1b0c665759237de98e86%2Finspector_view.jpg?alt=media)

예를들면 A라는 application에 포함된 agent들의 heap 사용량을 모아서 heap 사용량 평균값 , heap 사용량의 평균값, heap 사용량이 가장 높은 agentid와 사용량, heap 사용량이 가장 적은 agentid와 사용량을 보여준다. 이외에도 agent inspector 에서 제공하는 다른 데이터들도 집계하여 application inspector에서 제공한다.

![graph.jpg](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-1b9fe2dfc5933f8a6d8dcfee8cf77076489f34c7%2Fgraph.jpg?alt=media)

application inspector 기능을 동작시키기 위해서는 [flink](https://flink.apache.org)와 [zookeeper](https://zookeeper.apache.org/)가 필요하고, 기능의 동작 구조와 구성 및 설정 방법을 아래 설명한다.

### 2. 동작 구조

application inspector 기능의 동작 및 구조를 그림과 함께 보자.

![execute\_flow.jpg](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-67c467a049c249107c3d9f9c23d24c98270ddfd1%2Fexecute_flow.jpg?alt=media)

**A.** [flink](https://flink.apache.org)에 streaming job을 실행시킨다.\
**B.** job이 실행되면 taskmanager 서버의 정보가 zookeeper의 데이터 노드로 등록이 된다.\
**C.** Collector는 zookeeper에서 flink 서버의 정보를 가져와서 flink 서버와 tcp 연결을 맺고 agent stat 데이터를 전송한다.\
**D.** flink 서버에서는 agent 데이터를 집계하여 통계 데이터를 hbase에 저장한다.

### 3. 기능 실행 방법

application inspector 기능을 실행하기 위해서 아래와 같이 설정을 변경하고 Pinpoint를 실행해야 한다.

**A.** [테이블 생성 스크립트를 참조](https://github.com/pinpoint-apm/pinpoint/tree/master/hbase/scripts)하여 application 통계 데이터를 저장하는 **ApplicationStatAggre** 테이블을 생성한다.

**B.** flink 프로젝트 설정파일([Pinpoint-flink.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/flink/src/main/resources/profiles/release/pinpoint-flink.properties))에 taskmanager 서버 정보를 저장하는 zookeeper 주소를 설정한다.

```
    flink.cluster.enable=true
    flink.cluster.zookeeper.address=YOUR_ZOOKEEPER_ADDRESS
    flink.cluster.zookeeper.sessiontimeout=3000
    flink.cluster.zookeeper.retry.interval=5000
    flink.cluster.tcp.port=19994
```

**C.** flink 프로젝트 설정파일([Pinpoint-flink.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/flink/src/main/resources/profiles/release/pinpoint-flink.properties))에 job의 실행 방법과 Collector에서 데이터를 받는 listener의 개수를 설정한다.

* flink를 cluster로 구축해서 사용한다면 \_flink.StreamExecutionEnvironment\_에는 **server**를 설정한다.
* flink를 Standalone 형태로 실행한다면 \_flink.StreamExecutionEnvironment\_에는 **local**을 설정한다.

```
    flink.StreamExecutionEnvironment=server
    flink.sourceFunction.Parallel=1
```

**D.** flink 프로젝트 설정파일([hbase.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/flink/src/main/resources/profiles/release/hbase.properties))에 집계 데이터를 저장하는 hbase 주소를 설정한다.

```
    hbase.client.host=YOUR_HBASE_ADDRESS
    hbase.client.port=2181
```

**E.** [flink 프로젝트](https://github.com/pinpoint-apm/pinpoint/tree/master/flink)를 빌드하여 target 폴더 하위에 생성된 streaming job 파일을 flink 서버에 job을 실행한다.

* streaming job 파일 이름은 `pinpoint-flink-job-{pinpoint.version}.jar` 이다.
* 실행방법은 [flink 사이트](https://flink.apache.org)를 참조한다.
* 반드시 실행시 job이 위에서 설정한 설정파일을 참고 할수 있도록 job parameter로 `spring.profiles.active release` or `spring.profiles.active local`를 넣어주야 한다. job 내부에서 spring profile 기능을 사용하여 설정파일을 참고 하고 있기때문에 반드시 입력해야한다.

**F.** Collector에서 flink와 연결을 맺을 수 있도록 설정파일([Pinpoint-Collector.properties](https://github.com/pinpoint-apm/pinpoint/blob/master/collector/src/main/resources/pinpoint-collector.properties))에 zookeeper 주소를 설정한다.

```
    flink.cluster.enable=true
    flink.cluster.zookeeper.address=YOUR_ZOOKEEPER_ADDRESS
    flink.cluster.zookeeper.sessiontimeout=3000
```

**G.** web에서 application inspector 버튼을 활성화 하기 위해서 설정파일(pinpoint-web.properties)을 수정한다.

```
    config.show.applicationStat=true
```

### 4. streaming job 동작 확인 모니터링 batch

Pinpoint streaming job이 실행되고 있는지 확인하는 batch job이 있다. batch job을 동작 시키고 싶다면 Pinpoint web 프로젝트의 설정 파일을 수정하면 된다.

**batch.properties**

```
batch.flink.server=FLINK_MANGER_SERVER_IP_LIST
#`batch.flink.server` 속성 값에 flink job manager 서버 IP를 입력하면 된다. 서버 리스트의 구분자는 ','이다.
# ex) batch.flink.server=123.124.125.126,123.124.125.127
```

**applicationContext-batch-schedule.xml**

```markup
<task:scheduled-tasks scheduler="scheduler">
    ...
    <task:scheduled ref="batchJobLauncher" method="flinkCheckJob" cron="0 0/10 * * * *" />
</task:scheduled-tasks>
```

batch job이 실패할 경우 알람이 전송되도록 기능을 추가 하고싶다면 `com.navercorp.pinpoint.web.batch.JobFailMessageSender class` 구현체를 만들고 bean으로 등록하면 된다.

### 5. 기타

자세한 flink 운영 설치에 대한 내용은 [flink 사이트](https://flink.apache.org)를 참고하자.


# Realtime Request Monitoring

The collection of request information can sometimes be so resource intensive that it can have a serious impact on the target system. Pinpoint provides a number of features that allow this expensive information to be monitored in real time only when the user really needs it.

## Features

The realtime monitor consists of 2 features: recording the number of active requests, thread-dumping the thread handling the active request

### Active request - realtime graph

In the datetime range picker there is a `REAL TIME` button which is focused on automatically augmenting the current data with the just generated realtime data.

![range picker realtime](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-90bd8818e94c54dc52208747339519e4e1432015%2Frange-picker-realtime.png?alt=media)

REAL TIME also activates the Active Requests window. This shows the number of active requests at the moment.

![active requests](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-0308fbfceb32dde0e1c800402eb08e986d1e067b%2Factive-requests.png?alt=media)

### Active request thread dump

Pressing the icon in the green square above navigates to the thread dump view

![thread dump list](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-9675d449afda87c24f809cfc53832bcc4c487d1d%2Fthread-dump.png?alt=media)

The above list view contains brief information about the threads that were handling requests at the time the page was loaded. When the item is selected, the thread dump is collected and displayed in the UI as shown below.

![thread dump detail](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-6d65c35fa41f337f1bc388fae5c5924518f09c8c%2Fthread-dump-detail.png?alt=media)

The thread dump only works if the request is still active, but can be replaced with `There is no message( may be completed)` if the request session is already closed by the time the user selects the item in the list.

## Requirements and installation

These features are **disabled by default** and can be enabled with the property `pinpoint.modules.realtime.enabled=true` at the web, collector module.

### Required properties

Once the feature is enabled, the [Redis](https://redis.io) connection must be provided, which can be configured by adjusting the properties below in \`redis/src/main/resources/redis/profiles'.

Most of the properties below follow, but are not exactly the same as, those defined in the [spring-data-redis](https://spring.io/projects/spring-data-redis) library.

```yaml
spring.data.redis.lettuce.client.io-thread-pool-size=8
spring.data.redis.lettuce.client.computation-thread-pool-size=8
spring.data.redis.lettuce.client.request-queue-size=1024

spring.data.redis.username=default
spring.data.redis.password=

# Standalone mode
spring.data.redis.host=localhost
spring.data.redis.port=6379

# Cluster mode: Cluster mode is prior to standalone
spring.data.redis.cluster.nodes=localhost.1:6379,localhost.2:6379,localhost.3:6379
```

If `spring.data.redis.cluster.nodes` is not empty, `spring.data.redis.host` is ignored.

## Architecture

Real-time information is not collected on a 24-hour basis, but is triggered by some kind of signal from a collector listening to a specific channel for broadcasting the event that a user has accessed that web page (demand). The collected information (supply) is immediately sent to the corresponding channel in Redis and can be read by the web server that sent the demand event.

![redis usage summary](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-0c0b76d5af672d4e0596bbb04cbb8b830fe0a071%2Fredis.drawio.png?alt=media)

### Case: the number of active requests

Most of the specifications for this section are described in `ATCServiceProtocolConfig.java`.

```java
@Bean
FluxChannelServiceProtocol<ATCDemand, ATCSupply> atcProtocol(ObjectMapper objectMapper) {
    return ChannelServiceProtocol.<ATCDemand, ATCSupply>builder()
      ...
            .setDemandPubChannelURIProvider(demand -> URI.create(RedisPubSubConstants.SCHEME + ":demand:atc-2"))
            .setDemandSubChannelURI(URI.create(RedisPubSubConstants.SCHEME + ":demand:atc-2"))
            .setSupplyChannelURIProvider(demand -> URI.create(RedisPubSubConstants.SCHEME + ":supply:atc-2:" + demand.getApplicationName() + ':' + demand.getAgentId() + ':' + demand.getStartTimestamp()))
            .buildFlux();
}
```

As described in the code above, the demand for the number of active requests is communicated over the redis pubsub channel using the key `demand:atc-2`. If real-time is enabled, all collectors should listen to this channel from the start.

A collector can ignore a demand event if it determines that it cannot respond to that event on its own, but you should design your demands carefully so that there is exactly one collector that can respond to the demand.

The appropriate collector with the appropriate connection triggers the agent to gather the required information, which is then passed in real time to the redis pubsub supply channel with the key 'supply:atc-2:{applicationName}:{agentId}:{startTimestamp}'.

![redis request response](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-a50199f131acc73ab44a33b7811108da2b657c60%2Fredis-req-res.drawio.png?alt=media)


# Separate Logging Per Request

## ENGLISH GUIDE

### Per-request logging

#### 1. Description

Pinpoint saves additional information(transactionId, spanId) in log messages to classify them by request.

When tomcat processes multiple requests concurrently, we can see log files printed in chronological order. But we can not classify them by each request. For example when an exception message is logged, we can not easily identify all the logs related to the request that threw the exception.

Pinpoint is able to classify logs by requests by storing additional information(transactionId, spanId) in MDC of each request. The transactionId printed in the log message is the same as the transactionId in Pinpoint Web’s Transaction List view.

Let’s take a look at a more specific example. The log below is from an exception that occurred without using Pinpoint. As you can see, it is hard to identify the logs related to the request that threw the exception. ex) Without Pinpoint

```
2015-04-04 14:35:20 [INFO](ContentInfoCollector:76 ) get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:123 ) get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoCollector:12) get content name : SPORTS
2015-04-04 14:35:20 [INFO](ContentInfoCollector:25 ) get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:56 ) get content name : NATIONAL
2015-04-04 14:35:20 [INFO](ContentInfoCollector:34 ) get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoService:55 ) check authorization of user
2015-04-04 14:35:20 [INFO](ContentInfoService:14 ) get title of content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14 ) execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114 ) execute query ...    
2015-04-04 14:35:20 [INFO](ContentInfoService:74 ) get top linking for content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14 ) execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114 ) execute query ...
2015-04-04 14:35:22 [INFO](ContentDAOImpl:186 ) execute query ...
2015-04-04 14:35:22 [ERROR]ContentDAOImpl:158 )
     com.mysql.jdbc.exceptions.jdbc4.CommunicationsException: Communications link failure
          at example.ContentDAO.executequery(ContentDAOImpl.java:152)
          ...
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at com.mysql.jdbc.ConnectionImpl.<init>(ConnectionImpl.java:787)
          ...
     Caused by: com.mysql.jdbc.exceptions.jdbc4.CommunicationsException:
     Communications link failure The last packet sent successfully to the server was 0 milliseconds ago.
     The driver has not received any packets from the server.    
          at com.mysql.jdbc.ConnectionImpl.createNewIO(ConnectionImpl.java:2181)
          ... 12 more
     Caused by: java.net.ConnectException: Connection refused
          at java.net.PlainSocketImpl.socketConnect(Native Method)
          at java.net.PlainSocketImpl.doConnect(PlainSocketImpl.java:333)
          at java.net.PlainSocketImpl.connectToAddress(PlainSocketImpl.java:195)   
          at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:182)   
          at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:432)   
          at java.net.Socket.connect(Socket.java:529)    
          ...13 more
2015-04-04 14:35:22 [INFO](ContentDAO:145 ) execute query ...
2015-04-04 14:35:20 [INFO](ContentInfoService:38 ) update hits for content
2015-04-04 14:35:20 [INFO](ContentInfoService:89 ) check of user
2015-04-04 14:35:24 [INFO](ContentDAO:146 ) execute query ...
2015-04-04 14:35:25 [INFO](ContentDAO:123 ) execute query ...
```

Pinpoint classifies logs by requests by storing additional information(transactionId, spanId) in MDC of each request. ex) With Pinpoint

```
2015-04-04 14:35:20 [INFO](ContentInfoCollector:76) [txId : agent^14252^17 spanId : 1224] get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:123) [txId : agent^142533^18 spanId : 1231] get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoCollector:12) [txId : agent^142533^19 spanId : 1246] get content name : SPORTS
2015-04-04 14:35:20 [INFO](ContentInfoCollector:25) [txId : agent^142533^20 spanId : 1263] get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:56) [txId : agent^142533^21 spanId : 1265] get content name : NATIONAL
2015-04-04 14:35:20 [INFO](ContentInfoCollector:34) [txId : agent^142533^22 spanId : 1278] get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoService:55) [txId : agent^14252^18 spanId : 1231] check authorization of user
2015-04-04 14:35:20 [INFO](ContentInfoService:14) [txId : agent^14252^17 spanId : 1224] get title of content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14) [txId : agent^14252^17 spanId : 1224] execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114) [txId : agent^142533^19 spanId : 1246] execute query ...    
2015-04-04 14:35:20 [INFO](ContentInfoService:74) [txId : agent^14252^17 spanId : 1224] get top linking for content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14) [txId : agent^142533^18 spanId : 1231] execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114) [txId : agent^142533^21 spanId : 1265] execute query ...
2015-04-04 14:35:22 [INFO](ContentDAOImpl:186) [txId : agent^142533^22 spanId : 1278] execute query ...
2015-04-04 14:35:22 [ERROR](ContentDAOImpl:158) [txId : agent^142533^18 spanId : 1231]
     com.mysql.jdbc.exceptions.jdbc4.CommunicationsException: Communications link failure
          at com.pinpoint.example.dao.ContentDAO.executequery(ContentDAOImpl.java:152)
          ...
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at com.mysql.jdbc.ConnectionImpl.<init>(ConnectionImpl.java:787)   
          ...
     Caused by: com.mysql.jdbc.exceptions.jdbc4.CommunicationsException:
     Communications link failure The last packet sent successfully to the server was 0 milliseconds ago.
     The driver has not received any packets from the server.
          ...
          at com.mysql.jdbc.ConnectionImpl.createNewIO(ConnectionImpl.java:2181)
          ... 12 more
     Caused by: java.net.ConnectException: Connection refused
          at java.net.PlainSocketImpl.socketConnect(Native Method)   
          at java.net.PlainSocketImpl.doConnect(PlainSocketImpl.java:333)
          at java.net.PlainSocketImpl.connectToAddress(PlainSocketImpl.java:195)
          at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:182)
          at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:432)
          at java.net.Socket.connect(Socket.java:529)
          ... 13 more
2015-04-04 14:35:22 [INFO](ContentDAO:145) [txId : agent^14252^17 spanId : 1224] execute query ...
2015-04-04 14:35:20 [INFO](ContentInfoService:38) [txId : agent^142533^19 spanId : 1246] update hits for content
2015-04-04 14:35:20 [INFO](ContentInfoService:89) [txId : agent^142533^21 spanId : 1265] check of user
2015-04-04 14:35:24 [INFO](ContentDAO:146) [txId : agent^142533^22 spanId : 1278] execute query ...
2015-04-04 14:35:25 [INFO](ContentDAO:123) [txId : agent^14252^17 spanId : 1224] execute query ...
```

The transactionId printed in the log message is the same as the transactionId in Pinpoint Web’s Transaction List view. ![per-request\_feature\_1.jpg](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-740fd5dfd8b1f9c2023c4c78cf1d69226b51c214%2Fper-request_feature_1.jpg?alt=media)

#### 2. How to configure

**2-1 Pinpoint agent configuration**

To enable this feature, set the logging property corresponding to the logging library in use to true in *pinpoint.config*. For example,

ex) pinpoint.config when using log4j

```
###########################################################
# log4j
###########################################################
profiler.log4j.logging.transactioninfo=true
```

ex) pinpoint.config when using log4j2

```
###########################################################
# log4j2 
###########################################################
profiler.log4j2.logging.transactioninfo=true
```

ex) pinpoint.config when using logback

```
###########################################################
# logback
###########################################################
profiler.logback.logging.transactioninfo=true
```

**2-2 log4j, log4j2, logback configuration**

Change the log message format to print the transactionId, and spanId saved in MDC.

ex) log4j : log4j.xml

```markup
Before
<appender name = "console" class= "org.apache.log4j.ConsoleAppender" >
     <layout class = "org.apache.log4j.EnhancedPatternLayout">
          <param name = "ConversionPattern" value= "%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) %m%n" />
     </layout >
</appender >

After
<appender name = "console" class= "org.apache.log4j.ConsoleAppender" >
     <layout class = "org.apache.log4j.EnhancedPatternLayout">
          <param name = "ConversionPattern" value= "%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) [TxId : %X{PtxId} , SpanId : %X{PspanId}] %m%n" />
        </layout >
</appender >
```

ex) log4j2 - log4j2.xml

```markup
Before
<appender>
     <console name="STDOUT" target="SYSTEM_OUT">
          <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) %m%n""/>
     </console>
<appender>

After
<appender>
     <console name="STDOUT" target="SYSTEM_OUT">
          <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) [TxId : %X{PtxId} , SpanId : %X{PspanId}] %m%n""/>
     </console>
<appender>
```

ex) logback : logback.xml

```markup
Before
<appender name = "STDOUT" class= "ch.qos.logback.core.ConsoleAppender" >
     <layout class = "ch.qos.logback.classic.PatternLayout">
          <Pattern >%d{HH:mm} %-5level %logger{36} - %msg%n</Pattern >
     </layout >
</appender >

After
<appender name = "STDOUT" class= "ch.qos.logback.core.ConsoleAppender" >
     <layout class = "ch.qos.logback.classic.PatternLayout">
          <Pattern >%d{HH:mm} %-5level %logger{36} - [TxId : %X{PtxId} , SpanId : %X{PspanId}] %msg%n</Pattern >
     </layout >
</appender >
```

**2-3 Checking log message**

If the per-request logging is correctly configured, the transactionId, and spanId are printed in the log file.

```
2015-04-04 14:35:20 [INFO](ContentInfoCollector:76 ) [txId : agent^14252^17 spanId : 1224] get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:123 ) [txId : agent^142533^18 spanId : 1231] get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoCollector:12) [txId : agent^142533^19 spanId : 1246] get content name : SPORTS
```

#### 3. expose log in Pinpoint web

If you want to add links to the logs in the transaction list view, you should configure and implement the logic as below. Pinpoint Web only adds link buttons - you should implement the logic to retrieve the log message.

If you want to expose your agent’s log messages, please follow the steps below.

**step 1** You should implement a controller that receives transactionId, spanId, transaction\_start\_time as parameters and retrieve the logs yourself. We do not yet provide a way to retrieve the logs.

example)

```java
@RestController
public class Nelo2LogController {

    @RequestMapping(value = "/????")
    public String NeloLogForTransactionId(@RequestParam (value= "transactionId", required=true) String transactionId,
                                            @RequestParam(value= "spanId" , required=false) String spanId,
                                            @RequestParam(value="time" , required=true) long time ) {

          // you should implement the logic to retrieve your agent’s logs.
    }
```

**step 2** In *pinpoint-web.properties* file, set `log.enable` to true, and `log.page.url` to the url of the controller above. The value set in `log.button.name` will show up as the button text in the Web UI.

```
log.enable= true
log.page.url=XXXX.pinpoint
log.button.name= log
```

**step 3** Pinpoint 1.5.0 or later, we improve button to decided enable/disable depending on whether or not being logged. You should implement interceptor for using logging appender to add logic whether or not being logged. you also should create plugin for logging appender internally. Please refer to Pinpoint Profiler Plugin Sample([Link](https://github.com/pinpoint-apm/pinpoint-plugin-sample)). Location added logic of interceptor is method to log for data of LoggingEvent in appender class. you should review your appender class and find method. This is interceptor example.

```
public class AppenderInterceptor implements AroundInterceptor0 {

    private final TraceContext traceContext;

    public AppenderInterceptor(TraceContext traceContext) {
        this.traceContext = traceContext;
    }

    @Override
    public void before(Object target) {
        Trace trace = traceContext.currentTraceObject();

        if (trace != null) {
            SpanRecorder recorder = trace.getSpanRecorder();
            recorder.recordLogging(LoggingInfo.LOGGED);
        }
    }

    @IgnoreMethod
    @Override
    public void after(Object target, Object result, Throwable throwable) {

    }
}
```

If those are correctly configured, the buttons are added in the transaction list view. ![per-request\_feature\_2.jpg](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-3ce49da1cdfd63c7208ec92142b21950c2bff409%2Fper-request_feature_2.jpg?alt=media)

For details in how the log buttons are generated, please refer to Pinpoint Web’s BusinessTransactionController and ScatterChartController.

## 한국어 가이드

### Per-request logging

#### 1. 기능 설명

Pinpoint에서는 log message를 request 단위로 구분할 수 있도록 log message 에 추가정보를 저장해준다.

다수의 요청을 처리하는 tomcat을 사용할 경우 로그 파일을 보면 시간순으로 출력된 로그를 확인할 수 있다. 그러나 동시에 요청된 다수의 request 각각에 대한 로그를 구분 해서 볼 수 없다. 예를 들어 로그에서 exception message가 출력됐을 때 그 exception이 발생한 request의 모든 log를 확인하기 힘들다.

Pinpoint는 log message 마다 request와 연관된 정보(transactionId, spanId)를 MDC에 넣어줘서 request 단위로 log message를 구분할 수 있도록 해준다. 로그에 출력된 transactionId는 pinpoint web의 transaction List 화면에 출력된 transactionId와 일치한다.

구체적으로 예를 들어보자. Pinpoint를 사용하지 않았을 때 exception이 발생했을 경우 로그 메시지를 살펴 보자. 요청된 다수의 request 각각을 구분하여 로그를 확인할 수가 없다.

ex) Without Pinpoint

```
2015-04-04 14:35:20 [INFO](ContentInfoCollector:76 ) get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:123 ) get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoCollector:12) get content name : SPORTS
2015-04-04 14:35:20 [INFO](ContentInfoCollector:25 ) get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:56 ) get content name : NATIONAL
2015-04-04 14:35:20 [INFO](ContentInfoCollector:34 ) get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoService:55 ) check authorization of user
2015-04-04 14:35:20 [INFO](ContentInfoService:14 ) get title of content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14 ) execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114 ) execute query ...
2015-04-04 14:35:20 [INFO](ContentInfoService:74 ) get top linking for content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14 ) execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114 ) execute query ...
2015-04-04 14:35:22 [INFO](ContentDAOImpl:186 ) execute query ...
2015-04-04 14:35:22 [ERROR]ContentDAOImpl:158 )
     com.mysql.jdbc.exceptions.jdbc4.CommunicationsException: Communications link failure
          at example.ContentDAO.executequery(ContentDAOImpl.java:152)
          ...
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at com.mysql.jdbc.ConnectionImpl.<init>(ConnectionImpl.java:787)
          ...
     Caused by: com.mysql.jdbc.exceptions.jdbc4.CommunicationsException:
     Communications link failure The last packet sent successfully to the server was 0 milliseconds ago.
     The driver has not received any packets from the server.
          at com.mysql.jdbc.ConnectionImpl.createNewIO(ConnectionImpl.java:2181)
          ... 12 more
     Caused by: java.net.ConnectException: Connection refused
          at java.net.PlainSocketImpl.socketConnect(Native Method)
          at java.net.PlainSocketImpl.doConnect(PlainSocketImpl.java:333)
          at java.net.PlainSocketImpl.connectToAddress(PlainSocketImpl.java:195)
          at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:182)
          at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:432)
          at java.net.Socket.connect(Socket.java:529)
          ...13 more
2015-04-04 14:35:22 [INFO](ContentDAO:145 ) execute query ...
2015-04-04 14:35:20 [INFO](ContentInfoService:38 ) update hits for content
2015-04-04 14:35:20 [INFO](ContentInfoService:89 ) check of user
2015-04-04 14:35:24 [INFO](ContentDAO:146 ) execute query ...
2015-04-04 14:35:25 [INFO](ContentDAO:123 ) execute query ...
```

Pinpoint는 로그 메세지 마다 request와 연관된 정보(transactionId, spanId)를 MDC에 넣어줘서 request 단위로 log message를 구분시켜 준다.

ex) With Pinpoint

```
2015-04-04 14:35:20 [INFO](ContentInfoCollector:76) [txId : agent^14252^17 spanId : 1224] get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:123) [txId : agent^142533^18 spanId : 1231] get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoCollector:12) [txId : agent^142533^19 spanId : 1246] get content name : SPORTS
2015-04-04 14:35:20 [INFO](ContentInfoCollector:25) [txId : agent^142533^20 spanId : 1263] get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:56) [txId : agent^142533^21 spanId : 1265] get content name : NATIONAL
2015-04-04 14:35:20 [INFO](ContentInfoCollector:34) [txId : agent^142533^22 spanId : 1278] get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoService:55) [txId : agent^14252^18 spanId : 1231] check authorization of user
2015-04-04 14:35:20 [INFO](ContentInfoService:14) [txId : agent^14252^17 spanId : 1224] get title of content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14) [txId : agent^14252^17 spanId : 1224] execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114) [txId : agent^142533^19 spanId : 1246] execute query ...
2015-04-04 14:35:20 [INFO](ContentInfoService:74) [txId : agent^14252^17 spanId : 1224] get top linking for content
2015-04-04 14:35:21 [INFO](ContentDAOImpl:14) [txId : agent^142533^18 spanId : 1231] execute query ...
2015-04-04 14:35:21 [INFO](ContentDAOImpl:114) [txId : agent^142533^21 spanId : 1265] execute query ...
2015-04-04 14:35:22 [INFO](ContentDAOImpl:186) [txId : agent^142533^22 spanId : 1278] execute query ...
2015-04-04 14:35:22 [ERROR](ContentDAOImpl:158) [txId : agent^142533^18 spanId : 1231]
     com.mysql.jdbc.exceptions.jdbc4.CommunicationsException: Communications link failure
          at com.pinpoint.example.dao.ContentDAO.executequery(ContentDAOImpl.java:152)
          ...
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
          at com.mysql.jdbc.ConnectionImpl.<init>(ConnectionImpl.java:787)
          ...
     Caused by: com.mysql.jdbc.exceptions.jdbc4.CommunicationsException:
     Communications link failure The last packet sent successfully to the server was 0 milliseconds ago.
     The driver has not received any packets from the server.
          ...
          at com.mysql.jdbc.ConnectionImpl.createNewIO(ConnectionImpl.java:2181)
          ... 12 more
     Caused by: java.net.ConnectException: Connection refused
          at java.net.PlainSocketImpl.socketConnect(Native Method)
          at java.net.PlainSocketImpl.doConnect(PlainSocketImpl.java:333)
          at java.net.PlainSocketImpl.connectToAddress(PlainSocketImpl.java:195)
          at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:182)
          at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:432)
          at java.net.Socket.connect(Socket.java:529)
          ... 13 more
2015-04-04 14:35:22 [INFO](ContentDAO:145) [txId : agent^14252^17 spanId : 1224] execute query ...
2015-04-04 14:35:20 [INFO](ContentInfoService:38) [txId : agent^142533^19 spanId : 1246] update hits for content
2015-04-04 14:35:20 [INFO](ContentInfoService:89) [txId : agent^142533^21 spanId : 1265] check of user
2015-04-04 14:35:24 [INFO](ContentDAO:146) [txId : agent^142533^22 spanId : 1278] execute query ...
2015-04-04 14:35:25 [INFO](ContentDAO:123) [txId : agent^14252^17 spanId : 1224] execute query ...
```

로그메시지에 출력된 transactionId는 Pinpoint web의 transactionlist의 transactionId와 일치한다. ![per-request\_feature\_1.jpg](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-740fd5dfd8b1f9c2023c4c78cf1d69226b51c214%2Fper-request_feature_1.jpg?alt=media)

#### 2. 설정 방법

**2-1 Pinpoint agent 설정**

Pinpoint를 사용하려면 Pinpoint agent 설정파일(Pinpoint.config)의 logging 설정 값을 true로 변경해야 한다. 사용하는 logging 라이브러리에 해당하는 설정값만 true로 변경하면 된다. 아래 설정에 대한 예시가 있다.

ex) Pinpoint.config - log4j 를 사용할 경우

```
###########################################################
# log4j
###########################################################
profiler.log4j.logging.transactioninfo=true
```

ex) Pinpoint.config - log4j2 를 사용할 경우

```
###########################################################
# log4j2 
###########################################################
profiler.log4j2.logging.transactioninfo=true
```

ex) Pinpoint.config - logback 를 사용할 경우

```
###########################################################
# logback
###########################################################
profiler.logback.logging.transactioninfo=true
```

**2-2 log4j, log4j2, logback 설정 파일 설정**

logging 설정 파일의 log message pattern 설정에 Pinpoint에서 MDC에 저장한 transactionId, spanId값이 출력될수 있도록 설정을 추가하자.

ex) log4j - log4j.xml

```markup
변경 전
<appender name = "console" class= "org.apache.log4j.ConsoleAppender" >
     <layout class = "org.apache.log4j.EnhancedPatternLayout">
          <param name = "ConversionPattern" value= "%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) %m%n" />
     </layout >
</appender >

변경 후
<appender name = "console" class= "org.apache.log4j.ConsoleAppender" >
     <layout class = "org.apache.log4j.EnhancedPatternLayout">
          <param name = "ConversionPattern" value= "%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) [TxId : %X{PtxId} , SpanId : %X{PspanId}] %m%n" />
        </layout >
</appender >
```

ex) log4j2 - log4j2.xml

```markup
변경 전
<appender>
     <console name="STDOUT" target="SYSTEM_OUT">
          <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) %m%n""/>
     </console>
<appender>

변경 후
<appender>
     <console name="STDOUT" target="SYSTEM_OUT">
          <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss} [%-5p](%-30c{1}) [TxId : %X{PtxId} , SpanId : %X{PspanId}] %m%n""/>
     </console>
<appender>
```

ex) logback - logback.xml

```markup
변경 전
<appender name = "STDOUT" class= "ch.qos.logback.core.ConsoleAppender" >
     <layout class = "ch.qos.logback.classic.PatternLayout">
          <Pattern >%d{HH:mm} %-5level %logger{36} - %msg%n</Pattern >
     </layout >
</appender >

변경 후
<appender name = "STDOUT" class= "ch.qos.logback.core.ConsoleAppender" >
     <layout class = "ch.qos.logback.classic.PatternLayout">
          <Pattern >%d{HH:mm} %-5level %logger{36} - [TxId : %X{PtxId} , SpanId : %X{PspanId}] %msg%n</Pattern >
     </layout >
</appender >
```

**2-3 로그 출력 확인**

Pinpoint agent가 적용된 서비스를 동작하여 log message에 아래와 같이 transactionId, spanId 정보가 출력되는것을 확인하면 된다.

```
2015-04-04 14:35:20 [INFO](ContentInfoCollector:76 ) [txId : agent^14252^17 spanId : 1224] get content name : TECH
2015-04-04 14:35:20 [INFO](ContentInfoCollector:123 ) [txId : agent^142533^18 spanId : 1231] get content name : OPINION
2015-04-04 14:35:20 [INFO](ContentInfoCollector:12) [txId : agent^142533^19 spanId : 1246] get content name : SPORTS
```

#### 3. Pinpoint web에서 로그 확인

Pinpoint web의 transaction list 화면에서 log를 출력하는 링크를 제공하고 싶다면 아래와 같이 설정 및 구현을 추가하면 된다. Pinpoint web에서는 버튼 을 추가해주기만 하고 로그를 가져오는 로직은 직접 구현을 해야한다.

로그 메시지를 Pinpoint web에서 보여주기 위해서는 아래와 같이 2가지 step을 따라야 한다.

**step 1** transactionId와 spanId, transaction 시작 시간을 파라미터로 받아서 로그 메시지를 가져오는 controller을 구현해야한다.

example)

```java
@RestController
public class Nelo2LogController {

    @RequestMapping(value = "/XXXX")
    public String NeloLogForTransactionId(@RequestParam (value= "transactionId", required=true) String transactionId,
                                            @RequestParam(value= "spanId" , required=false) String spanId,
                                            @RequestParam(value="time" , required=true) long time ) {

          // you should implement the logic to retrieve your agent’s logs.
    }
```

**step 2** Pinpoint-web.properties 파일에서 버튼을 추가해주는 기능을 활성화 하기 위해서 log.enable의 값을 true로 설정하고 위에서 구현한 controller의 url과 button의 이름을 추가해주자.

```
log.enable=true
log.page.url=XXXX.Pinpoint
log.button.name=log
```

**step 3** pinpoint 1.5 이후 버전부터 log 기록 여부에 따라 log 버튼의 활성화가 결정되도록 개선 됐기 때문에 당신이 사용하는 logging appender의 로깅 메소드에 logging 여부를 저장하는 interceptor를 추가하는 플러그인을 개발해야 한다. 플러그인 개발 방법은 다음 링크를 참고하면 된다([Link](https://github.com/pinpoint-apm/pinpoint-plugin-sample)). interceptor 로직이 추가돼야 하는 위치는 appender class 내에 LoggingEvent 객체의 데이터를 이용하여 로깅을 하는 메소드다. 아래는 interceptor 예제이다.

```
public class AppenderInterceptor implements AroundInterceptor0 {

    private final TraceContext traceContext;

    public AppenderInterceptor(TraceContext traceContext) {
        this.traceContext = traceContext;
    }

    @Override
    public void before(Object target) {
        Trace trace = traceContext.currentTraceObject();

        if (trace != null) {
            SpanRecorder recorder = trace.getSpanRecorder();
            recorder.recordLogging(LoggingInfo.LOGGED);
        }
    }

    @IgnoreMethod
    @Override
    public void after(Object target, Object result, Throwable throwable) {

    }
}
```

위와 같이 설정 및 구현을 추가하고 pinpoint web을 동작시키면 아래와 같이 버튼이 추가 된다. ![per-request\_feature\_2.jpg](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-3ce49da1cdfd63c7208ec92142b21950c2bff409%2Fper-request_feature_2.jpg?alt=media) 로그 버튼을 생성해주는 과정을 보시려면, Pinpoint Web의 BusinessTransactionController 와 ScatterChartController class를 참고하세요.


# Marking Transaction as Fail

## HTTP Status Code with Request Failure. <a href="#http-status-code-with-request-failure" id="http-status-code-with-request-failure"></a>

![overview](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-cf1140a4afb3c0a73333b81a2a20c55ebe2fbaae%2Fhttp-status-code-failure-overview.png?alt=media)

## Pinpoint Configuration

pinpoint.config

```
profiler.http.status.code.errors=5xx, 401, 403, 406
```

Comma separated list of HTTP status codes.

* 1xx: Informational(100 \~ 199).
  * 100: Continue
  * 101: Switching Protocols
* 2xx: Successful(200 \~ 299).
  * 200: OK
  * 201: Created
  * 202: Accepted
  * 203: Non-Authoritative Information
  * 204: No Content
  * 205: Reset Content
  * 206: Partial Content
* 3xx: Redirection(300 \~ 399).
  * 300: Multiple Choices
  * 301: Moved Permanently
  * 302: Found
  * 303: See Other
  * 304: Not Modified
  * 305: Use Proxy
  * 307: Temporary Redirect
* 4xx: Client Error(400 \~ 499).
  * 400: Bad Request
  * 401: Unauthorized
  * 402: Payment Required
  * 403: Forbidden
  * 404: Not Found
  * 405: Method Not Allowed
  * 406: Not Acceptable
  * 407: Proxy Authentication Required
  * 408: Request Time-out
  * 409: Conflict
  * 410: Gone
  * 411: Length Required
  * 412: Precondition Failed
  * 413: Request Entity Too Large
  * 414: Request-URI Too Large
  * 415: Unsupported Media Type
  * 416: Requested range not satisfiable
  * 417: Expectation Failed
* 5xx: Server Error(500 \~ 599).
  * 500: Internal Server Error
  * 501: Not Implemented
  * 502: Bad Gateway
  * 503: Service Unavailable
  * 504: Gateway Time-out
  * 505: HTTP Version not supported

Resources

* <https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html>


# Monitoring Proxy Server

## Proxy monitoring using HTTP headers <a href="#proxy-monitoring-using-http-headers" id="proxy-monitoring-using-http-headers"></a>

It is used to know the elapsed time between proxy and WAS.

![overview](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-257fbee4518c6805487a8e000f6da518440eb974%2Fproxy-http-header-overview.png?alt=media)

## Pinpoint Configuration

pinpoint.config

```
profiler.proxy.http.header.enable=true
```

## Proxy Configuration

### Apache HTTP Server

* <http://httpd.apache.org/docs/2.4/en/mod/mod_headers.html>

Add HTTP header.

```
Pinpoint-ProxyApache: t=991424704447256 D=3775428 i=51 b=49
```

e.g.

httpd.conf

```
<IfModule mod_jk.c>
...
RequestHeader set Pinpoint-ProxyApache "%t %D %i %b"
...
</IfModule>
```

**%t is required value.**

### Nginx

* <http://nginx.org/en/docs/http/ngx_http_core_module.html>
* <http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_set_header>

Add HTTP header.

```
Pinpoint-ProxyNginx: t=1504248328.423 D=0.123
```

e.g.

nginx.conf

```
...
  server {
        listen       9080;
        server_name  localhost;

        location / {
            ...
            set $pinpoint_proxy_header "t=$msec D=$request_time";
            proxy_set_header Pinpoint-ProxyNginx $pinpoint_proxy_header;
        }
  }
...
```

or

```
http {
...

    proxy_set_header Pinpoint-ProxyNginx t=$msec;

...
}
```

**t=$msec is required value.**

### App

Milliseconds since epoch (13 digits) and app information.

Add HTTP header.

```
Pinpoint-ProxyApp: t=1594316309407 app=foo-bar
```

**t=epoch is required value.**


# Upgrade Database Hbase2

### Do you like to use Hbase 2.x for Pinpoint? <a href="#do-you-like-to-use-hbase-2x-for-pinpoint" id="do-you-like-to-use-hbase-2x-for-pinpoint"></a>

Default settings of current releases are for Hbase 1.x.

If you'd like to use Hbase 2.x for Pinpoint database.

check out [Hbase2-module](https://github.com/pinpoint-apm/pinpoint/tree/master/hbase2-module).


# Contribution

Thank you very much for choosing to share your contribution with us. Please read this page to help yourself to the contribution.

Before making first pull-request, please make sure you've signed the [Contributor License Agreement](http://goo.gl/forms/A6Bp2LRoG3). This isn't a copyright - it gives us (Naver) permission to use and redistribute your code as part of the project.

## Making Pull Requests

Apart from trivial fixes such as typo or formatting, all pull requests should have a corresponding issue associated with them. It is always helpful to know what people are working on, and different (often better) ideas may pop up while discussing them. Please keep these in mind before you create a pull request:

* Every new java file must have a copy of the license comment. You may copy this from an existing file.
* Make sure you've tested your code thoroughly. For plugins, please try your best to include integration tests if possible.
* Before submitting your code, make sure any changes introduced by your code does not break the build, or any tests.
* Clean up your commit log into logical chunks of work to make it easier for us to figure out what and why you've changed something. (`git rebase -i` helps)
* Please try best to keep your code updated against the master branch before creating a pull request.
* Make sure you create the pull request against our master branch.
* If you've created your own plugin, please take a look at [plugin contribution guideline](#plugin-contribution-guideline)

## Plugin Contribution Guideline

We welcome your plugin contribution. Currently, we would love to see additional tracing support for libraries such as [Storm](https://storm.apache.org), [HBase](http://hbase.apache.org), as well as profiler support for additional languages (.NET, C++).

### Technical Guide

**For technical guides for developing plug-in,** take a look at our [plugin development guide](https://pinpoint-apm.gitbook.io/pinpoint/documents/plugin-dev-guide), along with [plugin samples](https://github.com/pinpoint-apm/pinpoint-plugin-sample) project to get an idea of how we do instrumentation. The samples will provide you with example codes to help you get started.

### Contributing Plugin

If you want to contribute your plugin, it has to satisfy the following requirements:

1. Configuration key names must start with `profiler.[pluginName]`.
2. At least 1 plugin integration test.

Once your plugin is complete, please open an issue to contribute the plugin as below:

```
Title: [Target Library Name] Plugin Contribution

Link: Plugin Repository URL
Target: Target Library Name
Supported Version: 
Description: Simple description about the target library and/or target library homepage URL

ServiceTypes: List of service type names and codes the plugin adds
Annotations: List of annotation key names and codes the plugin adds
Configurations: List of configuration keys and description the plugin adds.
```

Our team will review the plugin, and your plugin repository will be linked at the third-party plugin list page if everything checks out. If the plugin is for a widely used library, and if we feel confident that we can continuously provide support for it, you may be asked to send us a PR. Should you choose to accept it, your plugin will be merged to the Pinpoint repository.

As much as we'd love to merge all the plugins to the source repository, we do not have the man power to manage all of them, yet. We are a very small team, and we certainly are not experts in all of the target libraries. We feel that it would be better to not merge a plugin if we are not confident in our ability to provide continuous support for it.

To send a PR, you have to modify your plugin like this:

* Fork Pinpoint repository
* Copy your plugin under /plugins directory
* Set parent pom

  ```
    <parent>
        <groupId>com.navercorp.pinpoint</groupId>
        <artifactId>pinpoint-plugins</artifactId>
        <version>Current Version</version>
    </parent>
  ```
* Add your plugin to *plugins/pom.xml* as a sub-module.
* Add your plugin to *plugins/assembly/pom.xml* as a dependency.
* Copy your plugin integration tests under /agent-it/src/test directory.
* Add your configurations to /agent/src/main/resources/\*.config files.
* Insert following license header to all java source files.

  ```
  /*
  * Copyright 2018 Pinpoint contributors and NAVER Corp.
  *
  * Licensed under the Apache License, Version 2.0 (the "License");
  * you may not use this file except in compliance with the License.
  * You may obtain a copy of the License at
  *
  *     http://www.apache.org/licenses/LICENSE-2.0
  *
  * Unless required by applicable law or agreed to in writing, software
  * distributed under the License is distributed on an "AS IS" BASIS,
  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  * See the License for the specific language governing permissions and
  * limitations under the License.
  */
  ```

If you do not want to be bothered with a PR, you may choose to tell us to do it ourselves. However, please note that your contribution will not visible through git history or the Github profile.


# Performance Analysis

## Introduction

Team members of Pinpoint are always aware of performance and stability issues. We've adapted technologies to reduced elements that hinder performance and always carefully examine the codes when there is a plugin pull requests.(plugin codes affects most in performance)

While we have been testing internally everyday for last few years, We've finally had the chance to make the data presentable.

This article doesn't include results compared with other APMs. It's pointless to compare with others due to the difference in collected data. Pinpoint collects massive data to enhance observability as much as possible. But still with minimum impact on the performance

## Test Environment

JVM : 1.8.0\_77 (G1, -Xms4g, -Xmx4g)\
Server : Tomcat\
Database : Cubrid\
Stress test generator : [NGrinder](https://github.com/pinpoint-apm/ngrinder)

## Test Result

![Test Result](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-6b556e592a22322d6fc454605726a1bc5d1b6690%2F20191022_performance.png?alt=media)

*off : non traced*\
on-20 : trace 5% transaction using thrift\
\&#xNAN;*grpc-on-20 : trace 5% transaction using grpc*\
on-1 : trace 100% transaction using thrift\
\*grpc-on-1 : trace 100% transaction using grpc

**Test result shows that Pinpoint affects less than 3% in performance and memory**\
**TPS is effected by various reasons, which may not always be exact**\
**gRPC is little slow than thrift in this test, the performance gap between the two is expected to be reduced, or even more, reversed in v1.9.0 release**

## Conclusion

Pinpoint is already being used in dozens of global companies in the world. With right environment and configuration it's been proved to be worthy. We believe most of the services can spare their 3% of resource to gain high observability with Pinpoint.

## Check List

If you still have low performance issue due to Pinpoint. Here are several items to check in advance.

1. Check the default log option for Pinpoint-Agent (Default was `DEBUG` prior to v1.8.1)
2. JVM option
   * use G1 for the GC Type
   * fix initial/maximum memory allocation pool with same size. ex) -Xms4g -Xmx4g
3. Change [sampling rate](https://pinpoint-apm.gitbook.io/pinpoint/faq#why-is-only-the-first-some-of-the-requests-traced). Even 1\~2% would be enough if you are dealing big data.

   When certain transaction doesn't bypass database, it may appear that Pinpoint is consuming much more resources than 3%, since instrumentation time is not relative, but absolute. But this phenomenon appears in all APM, not only Pinpoint.

## Reference Data

We run test with various technology stacks. Planning to expand more as we go.\
[Full Result](https://pinpoint-apm.gitbook.io/pinpoint/performance)


# FAQ

[Github issues](https://github.com/pinpoint-apm/pinpoint/issues)\
[Google group](https://groups.google.com/forum/#!forum/pinpoint_user)\
[Gitter](https://gitter.im/naver/pinpoint)

Chinese groups

|                                                                                                  QQ Group: 897594820                                                                                                 |                                                                                                                DING Group                                                                                                                |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![QQ Group](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-f9cbff4e99069d1c453f335f53bd198c0db8b640%2Fnaverpinpoint.png?alt=media) | ![DING Group](https://1605299358-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHRdTdLaVR1i6jbr9ZpeS%2Fuploads%2Fgit-blob-79e1332a4388413fdf35be2f47822102a0f1b11d%2Fnaverpinpoint-jiao-liu-qun-ding.jpg?alt=media) |

## How do I get the call stack view?

Click on a server node, which will populate the scatter chart on the right. This chart shows all succeeded/failed requests that went through the server. If there are any requests that spike your interest, simply **drag on the scatter chart** to select them. This will bring up the call stack view containing the requests you've selected.

## How do I change agent's log level?

You can change the log level by modifying the agent's *log4j.xml* located in *PINPOINT\_AGENT/lib* directory.

## Why is only the first/some of the requests traced?

There is a sampling rate option in the agent's pinpoint.config file (profiler.sampling.rate). Pinpoint agent samples 1 trace every N transactions if this value was set as N. Changing this value to 1 will allow you to trace every transaction.

## Request count in the Scatter Chart is different from the ones in Response Summary chart. Why is this?

The Scatter Chart data have a second granularity, so the requests counted here can be differentiated by a second interval. On the other hand, the Server Map, Response Summary, and Load Chart data are stored in a minute granularity (the collector aggregates these in memory and flushes them every minute due to performance reasons). For example, if the data is queried from 10:00:30 to 10:05:30, the Scatter Chart will show the requests counted between 10:00:30 and 10:05:30, whereas the server map, response summary, and load chart will show the requests counted between 10:00:00 and 10:05:59.

## How do I delete application name and/or agent id from HBase?

Application names and agent ids, once registered, stay in HBase until their TTL expires (default 1year). You may however delete them proactively using [admin APIs](https://github.com/pinpoint-apm/pinpoint/blob/master/web/src/main/java/com/navercorp/pinpoint/web/controller/AdminController.java) once they are no longer used.

* Remove application name - `/admin/removeApplicationName.pinpoint?applicationName=$APPLICATION_NAME&password=$PASSWORD`
* Remove agent id - `/admin/removeAgentId.pinpoint?applicationName=$APPLICATION_NAME&agentId=$AGENT_ID&password=$PASSWORD`

  Note that the value for the password parameter is what you defined `admin.password` property in *pinpoint-web.properties*. Leaving this blank will allow you to call admin APIs without the password parameter.

## What are the criteria for the application name?

Pinpoint's applicationName doesn't support special characters. such as @,#,$,%,\*. Pinpoint's applicationName only supports \[a-zA-Z0-9], '.', '-', '\_' characters.

## HBase is taking up too much space, which data should I delete first?

Hbase is very scalable so you can always add more region servers if you're running out of space. Shortening the TTL values, especially for **AgentStatV2** and **TraceV2**, can also help (though you might have to wait for a major compaction before space is reclaimed). For details on how to major compact, please refer to [this](https://github.com/pinpoint-apm/pinpoint/blob/master/hbase/scripts/hbase-major-compact-htable.hbase) script.

However, if you **must** make space asap, data in **AgentStatV2** and **TraceV2** tables are probably the safest to delete. You will lose agent statistic data (inspector view) and call stack data (transaction view), but deleting these will not break anything.

Note that deleting **\*MetaData** tables will result in *\*-METADATA-NOT-FOUND* being displayed in the call stack and the only way to "fix" this is to restart all the agents, so it is generally a good idea to leave these tables alone.

## My custom jar application is not being traced. Help!

Pinpoint Agent need an entry point to start off a new trace for a transaction. This is usually done by various WAS plugins (such as Tomcat, Jetty, etc) in which a new trace is started when they receive an RPC request. For custom jar applications, you need to set this manually as the Agent does not have knowledge of when and where to start a trace. You can set this by configuring `profiler.entrypoint` in *pinpoint.config* file.

## Building is failing after new release. Help!

Please remember to run the command `./mvnw clean verify -DskipTests=true` if you've used a previous version before, and replace './mvnw' with './mvnw\.cmd' if you are using Windows.

## How to set java runtime option when using atlassian OSGi

`-Datlassian.org.osgi.framework.bootdelegation=sun.,com.sun.,com.navercorp.*,org.apache.xerces.*`

## Why do I see UI send requests to <https://www.google-analytics.com/collect?>

Pinpoint Web module has google analytics attached which tracks the number and the order of button clicks in the Server Map, Transaction List, and the Inspector View.\
This data is used to better understand how users interact with the Web UI which gives us valuable information on improving Pinpoint Web's user experience. To disable this for any reason, set following option to false in pinpoint-web.properties for your web instance.

```
config.sendUsage=false
```

## I'd like to use Hbase 2.x for Pinpoint.

If you'd like to use Hbase 2.x for Pinpoint database, check out [Hbase2-module](https://github.com/pinpoint-apm/pinpoint/tree/master/hbase2-module).


# Powered by Pinpoint

This page, documents **alphabetical list** of organizations using Pinpoint.

## Sites using Pinpoint

1. Coupang ([www.coupang.com](http://www.coupang.com))
2. Echemi ([www.echemi.com](http://www.echemi.com))
3. HANATOUR ([www.hanatour.com](http://www.hanatour.com))
4. NAVER ([www.naver.com](http://www.naver.com))
5. NHN Entertainment
6. Pikicast ([www.pikicast.com](http://www.pikicast.com))
7. SKPlanet ([www.skplanet.com](http://www.skplanet.com))
8. THE PIRATES([www.tpirates.com](http://www.tpirates.com))
9. Toss ([toss.im](https://toss.im))
10. XLGAMES ([www.xlgames.com](http://www.xlgames.com))

## Naver

Naver Co., Ltd. uses Pinpoint as primary APM. Monitoring 2k+ applications with 10k+ instances. Supports 870k+ tps with only 17 Pinpoint-Collectors. Around 70 billion span chunks are collected per day. Which is equivalent to 10 billion transaction.


# Resources

If you have created informative posts on pinpoint and want the link to be added. Feel free to contact us anytime. We are glad to add more links.

## Resources (KOREAN)

* 유용한 자료를 작성하셨다면 공유부탁드립니다!!!
* [Pinpoint 개발자가 작성한 Pinpoint 기술문서 (helloworld.naver.com)](http://helloworld.naver.com/helloworld/1194202)
* [설치 가이드 동영상 강좌 1 (okjsp 대표 허광남님)](https://www.youtube.com/watch?v=hrvKaEaDEGs)
* [설치 가이드 동영상 강좌 2 (okjsp 대표 허광남님)](https://www.youtube.com/watch?v=fliKPGHGXK4)

## Resources (ENGLISH)

* Anyone who would like to share any document are always welcome
* [Technical Overview of Pinpoint](https://github.com/pinpoint-apm/pinpoint/wiki/Technical-Overview-Of-Pinpoint)
* [Official Docker Repository](https://github.com/pinpoint-apm/pinpoint-docker)
* [Notes on Jetty Plugin for Pinpoint](https://github.com/cijung/Docs/blob/master/JettyPluginNotes.md) ([@cijung](https://github.com/cijung))

## Resources (中文)

* [Pinpoint学习笔记](http://skyao.gitbooks.io/leaning-pinpoint/)：中文资料收集整理和更重要的-中文翻译！
* [Pinpoint - 应用性能管理(APM)平台实践之部署篇](https://sconts.com/11)
* [开源APM工具Pinpoint线上部署](https://www.iqarr.com/2018/02/04/java/pinpoint/pinpoint-deploy/)


# Introduction

[![Maven](https://img.shields.io/github/actions/workflow/status/pinpoint-apm/pinpoint/maven.yml?branch=master\&label=build\&logo=github)](https://github.com/pinpoint-apm/pinpoint/actions?query=workflow%3AMaven) [![codecov](https://codecov.io/gh/pinpoint-apm/pinpoint/branch/master/graph/badge.svg)](https://codecov.io/gh/pinpoint-apm/pinpoint)

**Pinpoint** is an APM (Application Performance Management) tool for large-scale distributed systems written in Java / [PHP](https://github.com/pinpoint-apm/pinpoint-c-agent). Inspired by [Dapper](http://research.google.com/pubs/pub36356.html), Pinpoint provides a solution to help analyze the overall structure of the system and how components within them are interconnected by tracing transactions across distributed applications.

You should definitely check **Pinpoint** out If you want to

* understand your [application topology](https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/overview) at a glance
* monitor your application in *Real-Time*
* gain code-level visibility to every transaction
* install APM Agents without changing a single line of code
* have minimal impact on the performance (approximately 3% increase in resource usage)

![](https://content.gitbook.com/content/aqCauh91263NlJBUe0Lo/blobs/beMCkai3AePpjRTgJAm5/ss_server-map.png)

## Live Demo

* [demo](http://223.130.142.103:8080/main/ApiGateway@SPRING_BOOT/5m?inbound=1\&outbound=4\&wasOnly=false\&bidirectional=false) - Here is a Demo, So that you can take a look at Pinpoint right away.

## Want a quick tour?

* [Overview](https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/overview) / [History](https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/history) / [Tech Details](https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/techdetail) to get to know more about Pinpoint
* [Videos](https://pinpoint-apm.gitbook.io/pinpoint/want-a-quick-tour/videos) - Checkout our videos on Pinpoint

{% embed url="<https://youtu.be/U4EwnB34Dus>" %}

## Getting Started

* [Quick-start guide(Lastest Snapshot)](https://pinpoint-apm.gitbook.io/pinpoint/getting-started/quickstart) for simple test run of Pinpoint
* [Installation guide(Lastest Snapshot)](https://pinpoint-apm.gitbook.io/pinpoint/getting-started/installation) for further instructions.

## Google Analytics

The web module has google analytics attached that tracks the number and the order of button clicks in the server map, transaction list, and the inspector view.

This data is used to better understand how users interact with the Web UI which gives us valuable information in improving Pinpoint Web's user experience. To disable this for any reason, set the following option to false in *pinpoint-web.properties* for your web instance.

```
config.sendUsage=false
```

## Is your application created with PHP?

Pinpoint has started to support application written in PHP. [Check-out our php-agent repository](https://github.com/pinpoint-apm/pinpoint-c-agent).

## Looking for place to ask questions?

[Questions and FAQ](https://pinpoint-apm.gitbook.io/pinpoint/faq)

## License

Pinpoint is licensed under the Apache License, Version 2.0. See [LICENSE](https://github.com/pinpoint-apm/pinpoint/blob/master/LICENSE) for full license text.

```
Copyright 2019 NAVER Corp.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```


# What's New

## Key Features

### Removal of Comments in SQL Queries

* issue: #12061.
* Comments are no longer collected with the SQL queries by default.
  \
  In case you need them, please use the configuration below.

```properties
profiler.jdbc.removecomments=false
```

## New Plugins

* Update Update io.asyncer:r2dbc-mysql of spring r2dbc plugin #12077
* Update kafka plugin for compatibility with kafka 3.x version #11926
* Update reactor subscriber.subscribeOn #12079

## BugFix

* Fix java.lang.NoClassDefFoundError: java/sql/Date in spring data r2dbc plugin #12117
* Fix datetime/time columns config for Ingestion Aggregations #12180
* Fix missing dependency of pinpoint-batch #11984

***

**From version 3.x, the executable JAR files will be uploaded to Maven Central Repository.**
\
<https://repo1.maven.org/maven2/com/navercorp/pinpoint/>

* [pinpoint-agent-3.0.2.tar.gz](https://repo1.maven.org/maven2/com/navercorp/pinpoint/pinpoint-agent/3.0.2/pinpoint-agent-3.0.2.tar.gz)
* [pinpoint-batch-3.0.2-exec.jar](https://repo1.maven.org/maven2/com/navercorp/pinpoint/pinpoint-batch/3.0.2/pinpoint-batch-3.0.2-exec.jar)
* [pinpoint-collector-3.0.2-exec.jar](https://repo1.maven.org/maven2/com/navercorp/pinpoint/pinpoint-collector/3.0.2/pinpoint-collector-3.0.2-exec.jar)
* [pinpoint-collector-starter-3.0.2-exec.jar](https://repo1.maven.org/maven2/com/navercorp/pinpoint/pinpoint-collector-starter/3.0.2/pinpoint-collector-starter-3.0.2-exec.jar)
* [pinpoint-web-3.0.2-exec.jar](https://repo1.maven.org/maven2/com/navercorp/pinpoint/pinpoint-web/3.0.2/pinpoint-web-3.0.2-exec.jar)
* [pinpoint-web-starter-3.0.2-exec.jar](https://repo1.maven.org/maven2/com/navercorp/pinpoint/pinpoint-web-starter/3.0.2/pinpoint-web-starter-3.0.2-exec.jar)

***

## What's Changed

* \[#11604] Prepare 3.0.2-SNAPSHOT by @intr3p1d in <https://github.com/pinpoint-apm/pinpoint/pull/11605>
* \[#noissue] Bump actions/setup-java\@v3 to actions/setup-java\@v4 by @intr3p1d in <https://github.com/pinpoint-apm/pinpoint/pull/11618>
* \[#noissue] Run actions on 3.0.x branch by @kojandy in <https://github.com/pinpoint-apm/pinpoint/pull/11646>
* \[#11807] Backport: Fix reactor-plugin empty mono and flux by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/11808>
* \[#noissue] release 3.0.2-alpha1 by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/11838>
* \[#11604] Prepare 3.0.2-SNAPSHOT by @kojandy in <https://github.com/pinpoint-apm/pinpoint/pull/11863>
* \[#11854] Backport: fix possible NPE in ServerTransportFilter by @kojandy in <https://github.com/pinpoint-apm/pinpoint/pull/11862>
* \[#11926] Backport: Update kafka plugin for compatibility with kafka 3… by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/11927>
* \[#11984] Backport: Add missing dependency by @kojandy in <https://github.com/pinpoint-apm/pinpoint/pull/11985>
* \[#12073] Backport: Update matchable transform list by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12074>
* \[#12075] Backport: Add async nested of reactor plugin by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12076>
* \[#12077] Backport: Update io.asyncer:r2dbc-mysql of spring r2dbc plugin by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12078>
* \[#12079] Update reactor subscriber.subscribeOn by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12083>
* \[#noissue] release 3.0.2-alpha2 by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12086>
* \[#noissue] rename 3.0.2-SNAPSHOT by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12087>
* \[#12117] Backport: Fix java.lang.NoClassDefFoundError: java/sql/Date … by @jaehong-kim in <https://github.com/pinpoint-apm/pinpoint/pull/12118>
* \[#12061] Backport: Remove comments from SQL queries by @kojandy in <https://github.com/pinpoint-apm/pinpoint/pull/12127>
* \[#12180] Backport: Fix datetime/time columns config for Ingestion Aggregations by @donghun-cho in <https://github.com/pinpoint-apm/pinpoint/pull/12181>
* \[#12179] 3.0.2 release by @intr3p1d in <https://github.com/pinpoint-apm/pinpoint/pull/12183>

**Full Changelog**: <https://github.com/pinpoint-apm/pinpoint/compare/v3.0.1...v3.0.2>

## Upgrade consideration

HBase compatibility table:

| Pinpoint Version | HBase 1.x | HBase 2.x                                                                                                             |
| ---------------- | --------- | --------------------------------------------------------------------------------------------------------------------- |
| 2.0.x - 2.2.x    | yes       | [optional](https://pinpoint-apm.gitbook.io/pinpoint/documents/hbase-upgrade#do-you-like-to-use-hbase-2x-for-pinpoint) |
| 2.3.x - 2.5.x    | yes       | [hbase2-module](https://github.com/pinpoint-apm/pinpoint/tree/2.3.x/hbase2-module)                                    |
| 3.0.x            | no        | yes                                                                                                                   |
| 3.1.x            | no        | yes                                                                                                                   |

Agent compatibility to Collector table:

| Agent Version | Collector 2.x.x | Collector 3.0.x | Collector 3.1.x |
| ------------- | --------------- | --------------- | --------------- |
| 2.x.x         | yes             | yes             | yes             |
| 3.0.x         | no              | yes             | yes             |
| 3.1.x         | no              | no              | yes             |

Additionally, the required Java version to run each Pinpoint component is given below:

| Pinpoint Version | Agent | Collector | Web | Batch |
| ---------------- | ----- | --------- | --- | ----- |
| 2.0.x            | 6-13  | 8         | 8   | 8     |
| 2.1.x            | 6-14  | 8         | 8   | 8     |
| 2.2.x            | 7-14  | 8         | 8   | 8     |
| 2.3.x            | 7-17  | 8         | 8   | 8     |
| 2.4.x            | 7-18  | 11        | 11  | 11    |
| 2.5.x            | 8-19  | 11        | 11  | 11    |
| 3.0.x            | 8-21  | 17        | 17  | 17    |
| 3.1.x            | 8-24  | 17        | 17  | 17    |

## Supported Modules

* JDK 6+
* Supported versions of the \* indicated library may differ from the actual version.

| Title                                                                                                          | Instrumented Library                 | Min      | Max       | Comment |   |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------ | -------- | --------- | ------- | - |
| [Tomcat](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/tomcat)                     |                                      | 6.x      | 9.x       |         |   |
| [Jetty](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/jetty)                       |                                      | 8.x      | 9.x       |         |   |
| [JBoss](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/jboss)                       |                                      | 6.x      | 7.x       |         |   |
| [Resin](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/resin)                       |                                      | 4.x      | 4.x       |         |   |
| [Websphere](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/websphere)               |                                      | 6.x      | 8.x       |         |   |
| [Vertx](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/vertx)                       |                                      | 3.3      | 3.5       |         |   |
| [Weblogic](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/weblogic)                 |                                      | 10.x     | 12.x      |         |   |
| [Undertow](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/undertow)                 |                                      |          |           |         |   |
| [Undertow Servlet](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/undertow-servlet) |                                      |          |           |         |   |
| Jasper                                                                                                         |                                      |          |           |         |   |
|                                                                                                                |                                      |          |           |         |   |
| Java Async Thread                                                                                              |                                      |          |           |         |   |
|                                                                                                                |                                      |          |           |         |   |
| OpenWhisk                                                                                                      | whisk.core                           |          |           |         |   |
|                                                                                                                |                                      |          |           |         |   |
| SpringMVC Framework                                                                                            | spring-webmvc                        | 3.0.7    | 5.3.6     |         |   |
| Spring Web                                                                                                     | spring-web                           | 4.1.2    | 4.3.30    |         |   |
| Spring RabbitMQ                                                                                                | spring-rabbit                        | 1.3.3    | 2.2.16    |         |   |
| Spring IBatis                                                                                                  | spring-ibatis                        | 2.0.7    | 2.0.8     |         |   |
| Spring MyBatis                                                                                                 | mybatis-spring                       | 1.1.0    | 1.3.3     |         |   |
| \*[Spring Boot](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/spring-boot)         | spring-boot-autoconfigure            |          |           |         |   |
| \*[Spring Webflux](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/spring-webflux)   | spring-webflux                       |          |           |         |   |
|                                                                                                                |                                      |          |           |         |   |
| MyBatis                                                                                                        | mybatis                              | 3.0.3    | 3.3.1     |         |   |
| [Hystrix](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/hystrix)                   | hystrix-core                         | 1.4.0    | 1.5.18    |         |   |
|                                                                                                                |                                      |          |           |         |   |
| JDKHTTP                                                                                                        |                                      |          |           |         |   |
| Httpclient3                                                                                                    | commons-httpclient                   | 3.0      | 3.1       |         |   |
| Httpclient4                                                                                                    | httpclient                           | 4.0      | 4.5.4     |         |   |
| Thrift                                                                                                         | libthrift                            | 0.9.1    | 0.14.1    |         |   |
| Google HTTP Client                                                                                             | google-http-client                   | 1.19.0   | 1.39.2    |         |   |
| AsyncHttpClient                                                                                                | async-http-client                    | 1.7.24   | 1.8.17    |         |   |
| OkHttp                                                                                                         | okhttp                               | 2.0.0    | 3.3.1     |         |   |
| Apache HttpAsyncClient                                                                                         | httpasyncclient                      | 4.0      | 4.1.3     |         |   |
| \*Akka HTTP                                                                                                    | akka-http\_2.12                      | 10.1.0   | 10.1.x    |         |   |
| \*[Kafka](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/kafka)                     | kafka-clients                        | 0.11.0.1 |           |         |   |
| GRPC                                                                                                           | grpc-stub                            | 1.8.0    | 1.37.0    |         |   |
| \*[Reactor](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/reactor)                 | reactor-core                         | 3.3.0    | 3.3.1     |         |   |
| \*[Reactor Netty](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/reactor-netty)     | reactor-netty                        | 0.8.0    | 0.9.2     |         |   |
|                                                                                                                |                                      |          |           |         |   |
| Log4j                                                                                                          | log4j                                | 1.2.16   | 1.2.17    |         |   |
| Logback                                                                                                        | logback-classic                      | 1.0.13   | 1.2.3     |         |   |
| Log4j2                                                                                                         | log4j-core                           | 2.0      | 2.12.1    |         |   |
|                                                                                                                |                                      |          |           |         |   |
| \*Arcus                                                                                                        | arcus-java-client                    | 1.7.0    | 1.11.4    |         |   |
| \*MsSQL (jTDS)                                                                                                 | jtds                                 | 1.2.8    |           |         |   |
| \*MsSQL                                                                                                        | mssql-jdbc                           |          |           |         |   |
| HikariCP                                                                                                       | HikariCP-java6                       | 2.3.0    | 2.3.13    |         |   |
| Jackson-mapper-asl                                                                                             | jackson-mapper-asl                   | 1.0.1    | 1.8.11    |         |   |
| Jackson Databind                                                                                               | jackson-databind                     | 2.0.6    | 2.12.3    |         |   |
| MariaDB Connector/J                                                                                            | mariadb-java-client                  | 1.3.0    | 2.7.2     |         |   |
| MongoDB Java Driver                                                                                            | mongodb-driver                       | 3.0.0    | 3.12.8    |         |   |
| Elasticsearch                                                                                                  | elasticsearch-rest-high-level-client | 6.0.0    | 6.8.15    |         |   |
| Datastax Java Driver                                                                                           | cassandra-driver-core                | 2.0.10   | 3.11.0    |         |   |
| Druid                                                                                                          | druid                                | 1.0.0    | 1.2.6     |         |   |
| \*Cubrid                                                                                                       | cubrid-jdbc-driver                   | 8.4.1    | 10.0.0    |         |   |
| \*Commons DBCP                                                                                                 | commons-dbcp                         | 1.0      | 1.4       |         |   |
| \*Commons DBCP2                                                                                                | commons-dbcp2                        | 2.0      | 2.5.0     |         |   |
| \*HBase                                                                                                        | hbase-client                         | 1.2.6.1  | 1.2.6.1   |         |   |
| \*MySQL                                                                                                        | mysql-connector-java                 | 5.0      | 8.x       |         |   |
| \*Oracle JDBC Driver                                                                                           | ojdbc                                |          |           |         |   |
| \*PostgreSQL JDBC Driver                                                                                       | postgresql                           |          |           |         |   |
| \*[Redis](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/redis)                     | jedis                                | 2.4.2    |           |         |   |
| \*[Redis](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/redis-lettuce)             | lettuce-core                         | 5.0.0    | 5.1.2     |         |   |
| \*[Redis](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/redis-redisson)            | redisson                             | 3.10.0   | 3.10.4    |         |   |
|                                                                                                                |                                      |          |           |         |   |
| Apache CXF                                                                                                     | cxf-rt-rs-client                     | 3.0.0    | 3.4.3     |         |   |
| Netty                                                                                                          | netty-all                            | 4.1.0    | 4.1.63    |         |   |
| ActiveMQ                                                                                                       | activemq-all                         | 5.1.0    | 5.16.1    |         |   |
| [RxJAVA](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/rxjava)                     | rxjava                               | 1.0.0    | 1.3.8     |         |   |
| [RabbitMQ](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/rabbitmq)                 | amqp-client                          | 2.7.0    | 5.12.0    |         |   |
| [Paho MQTT](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/paho-mqtt)               | org.eclipse.paho.client.mqttv3       | 1.0.2    | 1.2.5     |         |   |
| [Paho MQTT](https://github.com/pinpoint-apm/pinpoint/tree/master/agent-module/plugins/paho-mqtt)               | org.eclipse.paho.mqttv5.client       | 1.2.5    | 1.2.5     |         |   |
|                                                                                                                |                                      |          |           |         |   |
| Gson                                                                                                           | gson                                 | 1.1      | 2.8.3     |         |   |
| Json                                                                                                           | json-lib                             | 1.0      | 2.2.2     |         |   |
| FastJson                                                                                                       | fastjson                             | 1.2.10   | 1.2.76    |         |   |
| Dubbo                                                                                                          | dubbo                                | 2.5.1    | 2.6.9     |         |   |
| kafka-clients                                                                                                  | kafka-clients                        | 0.11.0.0 | 2.6.1     |         |   |
| postgresql                                                                                                     | postgresql                           | 9.4.1208 | 42.2.19   |         |   |
| ojdbc8                                                                                                         | ojdbc8                               | 12.2.0.1 | 21.1.0.0  |         |   |
| ojdbc10                                                                                                        | ojdbc10                              | 19.3.0.0 | 19.10.0.0 |         |   |


# Overview

Services nowadays often consist of many different components, communicating amongst themselves as well as making API calls to external services. How each and every transaction gets executed is often left as a blackbox. Pinpoint traces transaction flows between these components and provides a clear view to identify problem areas and potential bottlenecks.

* **ServerMap** - Understand the topology of any distributed systems by visualizing how their components are interconnected. Clicking on a node reveals details about the component, such as its current status, and transaction count.
* **Realtime Active Thread Chart** - Monitor active threads inside applications in real-time.
* **Request/Response Scatter Chart** - Visualize request count and response patterns over time to identify potential problems. Transactions can be selected for additional detail by **dragging over the chart**.

![Server Map](https://content.gitbook.com/content/aqCauh91263NlJBUe0Lo/blobs/beMCkai3AePpjRTgJAm5/ss_server-map.png)

* **CallStack** - Gain code-level visibility to every transaction in a distributed environment, identifying bottlenecks and points of failure in a single view.

![Call Stack](https://content.gitbook.com/content/aqCauh91263NlJBUe0Lo/blobs/O4O9w5T2KRrdtrhA4Gkb/ss_call-stack.png)

* **Inspector** - View additional details on the application such as CPU usage, Memory/Garbage Collection, TPS, and JVM arguments.

![Inspector](https://content.gitbook.com/content/aqCauh91263NlJBUe0Lo/blobs/Ql4c8dEJvuVG42lVPXE3/ss_inspector.png)

## Architecture

![Pinpoint Architecture](https://content.gitbook.com/content/aqCauh91263NlJBUe0Lo/blobs/MpkTeLHHEWkzh5EGJCOm/pinpoint-architecture.png)


# History

Pinpoint is a platform that analyzes large-scale distributed systems and provides a solution to handle large collections of trace data. It has been developed since July 2012 and was launched as an open-source project on January 9, 2015.

This article introduces Pinpoint; it describes what motivated us to start this project, which technologies are used, and how the Pinpoint Agent can be optimized.

> 本文的中文翻译版本 [请见这里](https://github.com/skyao/leaning-pinpoint/blob/master/design/technical_overview.md)

## Motivation to Get Started & Pinpoint Characteristics

Compared to nowadays, the number of Internet users was relatively small and the architecture of Internet services was less complex. Web services were generally configured using a 2-tier (web server and database) or 3-tier (web server, application server, and database) architecture. However, today, supporting a large number of concurrent connections is required and functionalities and services should be organically integrated as the Internet has grown, resulting in much more complex combinations of the software stack. That is n-tier architecture more than 3 tiers has become more widespread. A service-oriented architecture (SOA) or the [microservices](http://en.wikipedia.org/wiki/Microservices) architecture is now a reality.

The system's complexity has consequently increased. The more complex it is, the more difficult you solve problems such as system failure or performance issues. For example, Finding solutions in a 3-tier system is far less complicated. You only need to analyze 3 main components; a web server, an application server, and a database where the number of servers is small. While, if a problem occurs in an n-tier architecture, a large number of components and servers should be investigated. Another problem is that it is difficult to see the big picture only with an analysis of individual components; a low visibility issue is raised. The higher the degree of system complexity is, the longer it takes time to find out the reasons. Even worse, probability increases in which we may not even find them at all.

Such problems have occurred in the systems at NAVER. A variety of tools like Application Performance Management (APM) were used but they were not enough to handle the problems effectively; so we finally ended up developing a new tracing platform for n-tier architecture, which can provide solutions to systems with an n-tier architecture.

Pinpoint, began development in July 2012 and was launched as an open-source project in January 2015, is an n-tier architecture tracing platform for large-scale distributed systems. The characteristics of Pinpoint are as follows:

* Distributed transaction tracing to trace messages across distributed applications
* Automatically detecting the application topology that helps you to figure out the configurations of an application
* Horizontal scalability to support large-scale server group
* Providing code-level visibility to easily identify points of failure and bottlenecks
* Adding a new functionality without code modifications, using the bytecode instrumentation technique


# Tech Details

In this article, we describe the Pinpoint's techniques such as transaction tracing and bytecode instrumentation. And we explain the optimization method applied to Pinpoint Agent, which modifies bytecode and record performance data.

## Distributed Transaction Tracing, Modeled after Google's Dapper

Pinpoint traces distributed requests in a single transaction, modeled after Google's Dapper.

### How Distributed Transaction Tracing Works in Google's Dapper

The purpose of a distributed tracing system is to identify relationships between Node 1 and Node 2 in a distributed system when a message is sent from Node 1 to Node 2 (Figure 1).

![Figure 1. Message relationship in a distributed system](https://content.gitbook.com/content/aqCauh91263NlJBUe0Lo/blobs/Mw16dyZvx0bLrb7dpR0D/td_figure1.png)

Figure 1. Message relationship in a distributed system

The problem is that there is no way to identify relationships between messages. For example, we cannot recognize relationships between N messages sent from Node 1 and N' messages received in Node 2. In other words, when X-th message is sent from Node 1, the X-th message cannot be identified among N' messages received in Node 2. An attempt was made to trace messages at TCP or operating system level. However, implementation complexity was high with low performance because it should be implemented separately for each protocol. In addition, it was difficult to accurately trace messages.

However, a simple solution to resolve such issues has been implemented in Google's Dapper. The solution is to add application-level tags that can be a link between messages when sending a message. For example, it includes tag information for a message in the HTTP header at an HTTP request and traces the message using this tag.

> Google's Dapper
>
> For more information on Google's Dapper, see "[Dapper, a Large-Scale Distributed Systems Tracing Infrastructure](http://research.google.com/pubs/pub36356.html)."

Pinpoint is modeled on the tracing technique of Google's Dapper but has been modified to add application-level tag data in the call header to trace distributed transactions at a remote call. The tag data consists of a collection of keys, which is defined as a TraceId.

### Data Structure in Pinpoint

In Pinpoint, the core of data structure consists of Spans, Traces, and TraceIds.

* Span: The basic unit of RPC (remote procedure call) tracing; it indicates work processed when an RPC arrives and contains trace data. To ensure the code-level visibility, a Span has children labeled SpanEvent as a data structure. Each Span contains a TraceId.
* Trace: A collection of Spans; it consists of associated RPCs (Spans). Spans in the same trace share the same TransactionId. A Trace is sorted as a hierarchical tree structure through SpanIds and ParentSpanIds.
* TraceId: A collections of keys consisting of TransactionId, SpanId, and ParentSpanId. The TransactionId indicates the message ID, and both the SpanId and the ParentSpanId represent the parent-child relationship of RPCs.
  * TransactionId (TxId): The ID of the message sent/received across distributed systems from a single transaction; it must be globally unique across the entire group of servers.
  * SpanId: The ID of a job processed when receiving RPC messages; it is generated when an RPC arrives at a node.
  * ParentSpanId (pSpanId): The SpanId of the parent span which generated the RPC. If a node is the starting point of a transaction, there will not be a parent span - for these cases, we use a value of -1 to denote that the span is the root span of a transaction.

> Differences in terms between Google's Dapper and NAVER's Pinpoint
>
> The term "TransactionId" in Pinpoint has the same meaning as the term "TraceId" in Google's Dapper and the term "TraceId" in Pinpoint refers to a collection of keys.

### How TraceId Works

The figure below illustrates the behavior of a TraceId in which RPCs were made 3 times within 4 nodes.

![Figure 2. Example of a TraceId behavior](https://content.gitbook.com/content/aqCauh91263NlJBUe0Lo/blobs/9tbJR30tYUe9lZJNQXAU/td_figure2.png)

Figure 2. Example of a TraceId behavior

A TransactionId (TxId) represents that three different RPCs are associated with each other as a single transaction in Figure 2. However, a TransactionId itself can't explicitly describe the relationship between RPCs. To identify the relationships between RPCs, a SpanId and a ParentSpanId (pSpanId) are required. Suppose that a node is Tomcat. You can think of a SpanId as a thread which handles HTTP requests. A ParentSpanId indicates the SpainId of a parent that makes RPC calls.

Pinpoint can find associated n Spans using a TransactionId and can sort them as a hierarchical tree structure using a SpanId and a ParentSpanId.

A SpanId and a ParentSpanId are 64-bit long integers. A conflict might arise because the number is generated arbitrarily, but considering the range of value from -9223372036854775808 to 9223372036854775807, this is unlikely to happen. If there is a conflict between keys, Pinpoint as well as Google's Dapper lets developers know what happened, instead of resolving the conflict.

A TransactionId consists of AgentIds, JVM (Java virtual machine) startup time, and SequenceNumbers.

* AgentId: A user-created ID when JVM starts; it must be globally unique across the entire group of servers where Pinpoint has been installed. The easiest way to make it unique is to use a hostname ($HOSTNAME) because the hostname is not duplicate in general. If you need to run multiple JVMs within the server group, add a postfix to the hostname to avoid duplicates.
* JVM startup time: Required to guarantee a unique SequenceNumber which starts with zero. This value is used to prevent ID conflicts when a user creates duplicate AgentId by mistake.
* SequenceNumber: ID issued by the Pinpoint Agent, with sequentially increasing numbers that start with zero; it is issued per message.

Dapper and [Zipkin](https://github.com/twitter/zipkin), a distributed systems tracing platform at Twitter, generate random TraceIds (TransactionIds in Pinpoint) and consider conflict situations as a normal case. However, we wanted to avoid this conflict as much as possible in Pinpoint. We had two available options for this; one with a method in which the amount of data is small but the probability of conflict is high; the other is a method in which the amount of data is large but the probability of conflict is low; We chose the second option.

There may be a better ways to handle transactions. We came up with several ideas such as key issue by a central key server. But we didn't implement this in the system due to performance issues and network errors. We are still considering issuing keys in bulk as an alternative Solution. So maybe later in the future, such methods can be developed; But for now, a simple method is adopted. In Pinpoint, a TransactionId is regarded as changeable data.

## Bytecode Instrumentation, Not Requiring Code Modifications

Earlier, we explained distributed transaction tracing. One way for implementing this is that developers to modify their code by themselves. Allow developers to add tag information when an RPC is made. However, it could be a burden to modify code even though such functionality is useful to developers.

Twitter's Zipkin provides the functionality of distributed transaction tracing using modified libraries and its container (Finagle). However, it requires the code to be modified if needed. We wanted the functionality to work without code modifications and desired to ensure code-level visibility. To solve such problems, the bytecode instrumentation technique was adopted in Pinpoint. The Pinpoint Agent intervenes code to make RPCs so as to automatically handle tag information.

### Overcoming Disadvantages of Bytecode Instrumentation

There are two ways for distributed transaction tracing as below. Bytecode instrumentation is one of an automatic method.

* Manual method: Developers develop code that records data at important points using APIs provided by Pinpoint.
* Automatic method: Developers do not involve code modifications because Pinpoint decides which API is to be intervened and developed.

Advantages and disadvantages of each method are as follows:

Table 1 Advantages and disadvantage of each method

| Item                  | Advantage                                                                                                                   | Disadvantage                                                                                                                                                                                                                                                                                                                       |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Manual Tracing**    | - Requires less development resources. - An API can become simpler and consequently the number of bugs can be reduced.      | - Developers must modify the code. - Tracing level is low.                                                                                                                                                                                                                                                                         |
| **Automatic Tracing** | - Developers are not required to modify the code. - More precise data can be collected due to more information in bytecode. | - It would cost 10 times more to develop Pinpoint with automatic method. - Requires highly competent developers who can instantly recognize the library code to be traced and make decisions on the tracing points. - Can increase the possibility of a bug due to high-level development skills such as bytecode instrumentation. |

Bytecode instrumentation is a technique that includes high difficulty level and risks. Nevertheless, using this technique has many benefits.

Although it requires a large number of development resources, it requires almost none for applying the service. For example, the following shows the costs between an automatic method which uses bytecode instrumentation and a manual method which uses libraries (in this context, costs are random numbers assumed for clarity).

* Automatic method: Total of 100
  * Cost of Pinpoint development: 100
  * Cost of services applied: 0
* Manual method: Total of 30
  * Cost of Pinpoint development: 20
  * Cost of services applied: 10

The data above tells us that a manual method is more cost-effective than an automatic one. However, it will not guarantee the same result for NAVER since we have thousands of services. For example, if we have 10 services which require being modified, the total cost will be calculated as follows:

* Cost of Pinpoint development 20 + Cost of services applied 10 x 10 services = 120

As you can see, the automatic method was more cost-efficient for us.

We are lucky to have many developers who are highly competent and specialized in Java in the Pinpoint team. Therefore, we believed it was only a matter of time to overcome the technical difficulties in Pinpoint development.

### The Value of Bytecode Instrumentation

The reason we chose to implement bytecode instrumentation(Automatic method) is not only those that we have already explained but also the following points.

#### Hidden API

If the API is exposed for developers to use. We, as API providers, are restricted to modify the API as we desire. Such a restriction can impose stress on us.

We may modify an API to correct mistaken design or add new functions. However, if there is a restriction to do this, it would be difficult for us to improve the API. The best answer for solving such a problem is a scalable system design, which is not an easy option as everyone knows. It is almost impossible to create perfect API design as we can't predict the future.

With bytecode instrumentation, we don't have to worry about the problems caused by exposing the tracing APIs and can continuously improve the design, without considering dependency relationships. For those who are planning to develop their applications using Pinpoint, please note that API can be changed by the Pinpoint developers since improving performance and design is our first priority.

#### Easy to Enable or Disable

The disadvantage of using bytecode instrumentation is that it could affect your applications when a problem occurs in the profiling section of a library or Pinpoint itself. However, you can easily solve it by just disabling the Pinpoint since you don't have to change any code.

You can easily enable Pinpoint for your applications by adding the three lines (associated with the configuration of the Pinpoint Agent) below into your JVM startup script:

```
-javaagent:$AGENT_PATH/pinpoint-bootstrap-$VERSION.jar
-Dpinpoint.agentId=<Agent's UniqueId>
-Dpinpoint.applicationName=<The name indicating a same service (AgentId collection)>
```

If any problem occurs due to Pinpoint, you can just delete the configuration data in the JVM startup script.

### How Bytecode Instrumentation Works

Since bytecode instrumentation technique has to deal with Java bytecode, it tends to increase the risk of development while it decreases productivity. In addition, developers are prone to make mistakes. In Pinpoint, we improved productivity and accessibility by abstraction with the interceptor. Pinpoint injects necessary codes to track distributed transactions and performance information by intervening application code at class loading time. This increases performance since tracking codes are directly injected into the application code.

![Figure 3. Behavior of bytecode instrumentation](https://content.gitbook.com/content/aqCauh91263NlJBUe0Lo/blobs/PwwJpYeq9YlHgnoTKgth/td_figure3.png)

Figure 3. Basic principle of bytecode instrumentation

In Pinpoint, the API intercepting part and data recording part are separated. Interceptor is injected into the method that we'd like to track and calls before() and after() methods where data recording is taken care of. Through bytecode instrumentation, Pinpoint Agent can record data only from the necessary method which makes the size of profiling data compact.

## Optimizing Performance of the Pinpoint Agent

Finally, we will describe how to optimize the performance of Pinpoint Agent.

### Using Binary Format (Thrift)

You can increase encoding speed by using a binary format ([Thrift](https://thrift.apache.org/)). Although it is difficult to use and debug, It can improve the efficiency of network usage by reducing the size of data generated.

### Optimize Recorded Data for Variable-Length Encoding and Format

If you convert a long integer into a fixed-length string, the data size will be 8 bytes. However, if you use variable-length encoding, the data size can vary from 1 to 10 bytes depending on the size of a given number. To reduce data size, Pinpoint encodes data as a variable-length string through Compact Protocol of Thrift and records data to be optimized for encoding format. Pinpoint Agent reduces data size by converting remaining time based on root method into a vector value.

> Variable-length encoding
>
> For more information on the variable-length encoding, see "[Base 128 Varints](https://developers.google.com/protocol-buffers/docs/encoding#varints)" in Google Developers.

![Figure 4. Comparison between fixed-length encoding and variable-length encoding](https://content.gitbook.com/content/aqCauh91263NlJBUe0Lo/blobs/N5y3xOKchOxrmOoEIZbH/td_figure4.png)

Figure 4. Comparison between fixed-length encoding and variable-length encoding

As you can see in Figure 4, you need to measure the time of 6 different points to get information of when three different methods are called and finished(Figure 4); With fixed-length encoding, this process requires 48 bytes (6points × 8bytes).

Meanwhile, Pinpoint Agent uses variable-length encoding and records the data according to its corresponding format. And calculate time information on other points with the difference(in vector value) based on the start time of the root method. Since vector value is a small number, it consumes a small number of bytes resulting only 13 bytes consumed rather than 48bytes.

If it takes more time to execute a method, it will increase the number of bytes even though variable-length encoding is used. However, it is still more efficient than fixed-length encoding.

### Replacing Repeated API Information, SQLs, and Strings with Constant Tables

We wanted Pinpoint to enable code-level tracing. However, it had a problem in terms of increasing data size. Every time data with a high degree of precision is sent to a server, due to the size of the data it increased network usage.

To solve such a problem, we adopted a strategy by creating a constant table in a remote HBase server. Since there will be an overload to send data of "method A" to Pinpoint Collector each time, Pinpoint Agent converts "method A" data to an ID and stores this information as a constant table in HBase, and continue tracing data with the ID. When a user retrieves trace data on the Website, the Pinpoint Web searches for the method information of the corresponding ID in the constant table and reorganize them. The same way is used to reduce data size in SQLs or frequently-used strings.

### Handling Samples for Bulk Requests

The requests to online portal services which Naver is providing are huge. A single service handles more than 20 billion requests a day. A simple way to trace such request is by expanding network infrastructure and servers as much as needed to suit the number of requests. However, this is not a cost-effective way to handle such situations.

In Pinpoint, you can collect only sampling data rather than tracking every request. In a development environment where requests are few, every data is collected. While in the production environment where requests are large, only 1\~5% out of whole data is collected which is sufficient to analyze the status of entire applications. With sampling, you can minimize network overhead in applications and reduce costs of infrastructure such as networks and servers.

> Sampling method in Pinpoint
>
> Pinpoint supports a Counting sampler, which collects data only for one of 10 requests if it is set to 10. We plan to add new samplers that can collect data more effectively.

### Minimizing Application Threads Being Aborted Using Asynchronous Data Transfer

Pinpoint does not interfere with application threads since encoded data or remote messages are transferred asynchronously by another thread.

#### Transferring Data via UDP

Unlike Google's Dapper, Pinpoint transfers data through a network to ensure data speed. Sharing network with your service can be an issue when data traffic bursts out. In such situations, the Pinpoint Agent starts to use UDP protocol to give the network connection priority to your service.

> Note
>
> The data transfer APIs can be replaced since it's separated as an interface. It can be changed into an implementation that stores data in a different way, like local files.

## Example of Pinpoint Applied

Here is an example of how to get data from your application so that you can comprehensively understand the contents described earlier.

Figure 5 shows what you can see when you install Pinpoint in TomcatA and TomcatB. You can see the trace data of an individual node as a single transaction, which represents the flow of distributed transaction tracing.

![Figure 5. Example 1: Pinpoint applied](https://content.gitbook.com/content/aqCauh91263NlJBUe0Lo/blobs/38pOlSiARupnK1EOi9Vr/td_figure5.png)

Figure 5. Example of Pinpoint in action

The following describes what Pinpoint does for each method.

1. Pinpoint Agent issues a TraceId when a request arrives at TomcatA.
   * TX\_ID: TomcatA^TIME^1
   * SpanId: 10
   * ParentSpanId: -1(Root)
2. Records data from Spring MVC controllers.
3. Intervene the calls of HttpClient.execute() method and configure the TraceId in HttpGet.
   * Creates a child TraceId.
     * TX\_ID: TomcatA^TIME^1 -> TomcatA^TIME^1
     * SPAN\_ID: 10 -> 20
     * PARENT\_SPAN\_ID: -1 -> 10 (parent SpanId)
   * Configures the child TraceId in the HTTP header.
     * HttpGet.setHeader(PINPOINT\_TX\_ID, "TomcatA^TIME^1")
     * HttpGet.setHeader(PINPOINT\_SPAN\_ID, "20")
     * HttpGet.setHeader(PINPOINT\_PARENT\_SPAN\_ID, "10")
4. Transfer tagged request to TomcatB.
   * TomcatB checks the header from the transferred request.
     * HttpServletRequest.getHeader(PINPOINT\_TX\_ID)
   * TomcatB becomes a child node as it identifies a TraceId in the header.
     * TX\_ID: TomcatA^TIME^1
     * SPAN\_ID: 20
     * PARENT\_SPAN\_ID: 10
5. Records data from Spring MVC controllers and completes the request.

   <img src="https://content.gitbook.com/content/aqCauh91263NlJBUe0Lo/blobs/lpwmQAeQY1ZHtEksOIfF/td_figure6.png" alt="Figure 6. Example 2: Pinpoint applied" data-size="original">
6. Pinpoint Agent sends trace data to Pinpoint Collector to store it in HBase when the request from TomcatB is completed.
7. After the HTTP calls from TomcatB is terminated, then the request from TomcatA is complete. The Pinpoint Agent sends trace data to Pinpoint Collector to store it in HBase.
8. UI reads the trace data from HBase and creates a call stack by sorting trees.

## Conclusions

Pinpoint is another application that runs along with your applications. Using bytecode instrumentation makes Pinpoint seem like that it does not require code modifications. In general, the bytecode instrumentation technique makes applications vulnerable to risks; if a problem occurs in Pinpoint, it will affect your applications as well. But for now, instead of getting rid of such threats, we are focusing on improving performance and design of Pinpoint. Because we think this makes Pinpoint more valuable. So whether or not to use Pinpoint is for you to decide.

We still have a large amount of work to be done to improve Pinpoint. Despite its incompleteness, Pinpoint was released as an open-source project; we are continuously trying to develop and improve Pinpoint so as to meet your expectations.

> Written by Woonduk Kang
>
> In 2011, I wrote about myself like this—As a developer, I would like to make a software program that users are willing to pay for, like those of Microsoft or Oracle. As Pinpoint was launched as an open-source project, it seems that my dreams somewhat came true. For now, my desire is to make Pinpoint more valuable and attractive to users.


# Videos

## Speaking at COSCUP2019

Speaking at Taiwan's largest open source conference

Title : [Naver, monitoring services with trillions of event with open source APM, Pinpoint](https://coscup.org/2019/en/programs/naver-monitoring-services-with-trillions-of-event-with-open-source-apm-pinpoint)\
Date : Aug 18, 2019

{% embed url="<https://youtu.be/Uyy:CgRc5:M>" %}

### Speaking at HKOSCon2019

Speaking at HongKong's largest open source conference

Title : [How we started an open source APM project and troubleshooting with it](https://hkoscon.org/2019/topics/how-we-started-open-source-apm-project-and-troubleshooting-it)\
Date : June 15, 2019

{% embed url="<https://youtu.be/9-Kf87k4sEA>" %}

## Introduction to Pinpoint v1.5.0

Video introducing Pinpoint

{% embed url="<https://youtu.be/U4EwnB34Dus>" %}


# Additional Plugins

## Third-party agents/plugins

There may be agents, and plugins that are being developed and managed by other individuals/organizations.

Below include agents and plugins that are not merged into this repository.\
Take a look at them if you are interested and would like to help out.

* Plugins
  * Websphere - <https://github.com/sjmittal/pinpoint/tree/cpu_monitoring_fix/plugins/websphere>
  * RocketMQ - <https://github.com/ruizlake/pinpoint/tree/master/plugins/rocketmq>

If you are working on an agent or a plugin and want to add it to this list, please feel free to [contact us](mailto:roy.kim@navercorp.com) anytime.




---

[Next Page](/pinpoint/llms-full.txt/1)

