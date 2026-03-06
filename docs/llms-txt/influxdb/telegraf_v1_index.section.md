---
title: Telegraf documentation
description: Documentation for Telegraf, the plugin-driven server agent of the InfluxData time series platform, used to collect and report metrics. Telegraf supports four categories of plugins – input, output, aggregator, and processor.
url: https://docs.influxdata.com/telegraf/v1/
product: Telegraf
type: section
pages: 17
estimated_tokens: 321879
child_pages:
  - url: https://docs.influxdata.com/telegraf/v1/release-notes/
    title: Telegraf release notes
  - url: https://docs.influxdata.com/telegraf/v1/processor-plugins/
    title: Telegraf Processor Plugins
  - url: https://docs.influxdata.com/telegraf/v1/plugins/
    title: Plugin directory
  - url: https://docs.influxdata.com/telegraf/v1/output-plugins/
    title: Telegraf Output Plugins
  - url: https://docs.influxdata.com/telegraf/v1/metrics/
    title: Telegraf metrics
  - url: https://docs.influxdata.com/telegraf/v1/mcp-server/
    title: Use the InfluxDB documentation MCP server
  - url: https://docs.influxdata.com/telegraf/v1/install/
    title: Install Telegraf
  - url: https://docs.influxdata.com/telegraf/v1/input-plugins/
    title: Telegraf Input Plugins
  - url: https://docs.influxdata.com/telegraf/v1/glossary/
    title: Telegraf glossary
  - url: https://docs.influxdata.com/telegraf/v1/get-started/
    title: Get started
  - url: https://docs.influxdata.com/telegraf/v1/data_formats/
    title: Telegraf data formats
  - url: https://docs.influxdata.com/telegraf/v1/contribute/
    title: Contribute to Telegraf
  - url: https://docs.influxdata.com/telegraf/v1/configure_plugins/
    title: Configure plugins
  - url: https://docs.influxdata.com/telegraf/v1/configuration/
    title: Configuration options
  - url: https://docs.influxdata.com/telegraf/v1/commands/
    title: Telegraf commands and flags
  - url: https://docs.influxdata.com/telegraf/v1/aggregator-plugins/
    title: Telegraf Aggregator Plugins
---

# Telegraf documentation

Telegraf, a server-based agent, collects and sends metrics and events from databases, systems, and IoT sensors. Written in Go, Telegraf compiles into a single binary with no external dependencies–requiring very minimal memory.

For an introduction to Telegraf and an overview of how it works, watch the following video:

![InfluxDB University](/svgs/influxdbu-full-white.svg)

#### Telegraf Basics

Learn how to get started with Telegraf with this **free** course that covers common use cases, proper configuration, and best practices for deployment. Also, discover how to write your own custom Telegraf plugins.

[Take the course](https://university.influxdata.com/courses/telegraf-basics-tutorial/)

![InfluxDB University](/svgs/influxdbu-full-white.svg)

#### Data Collection with Telegraf

Learn how to use Telegraf to make data time series data collection easy in this **free** InfluxDB University course.

[Take the course](https://university.influxdata.com/courses/data-collection-with-telegraf-tutorial/)

#### Related

- [Intro to Telegraf](/resources/videos/intro-to-telegraf/)
- [Install Telegraf](/telegraf/v1/install/)

---

## Telegraf release notes

## v1.37.3

### Bugfixes

- [#18195](https://github.com/influxdata/telegraf/pull/18195) `common.jolokia2` Add Jolokia 2.x compatibility for proxy target tag
- [#18378](https://github.com/influxdata/telegraf/pull/18378) `common.opcua` Include node ID in duplicate metric check
- [#18335](https://github.com/influxdata/telegraf/pull/18335) `inputs.disk` Preserve device tag for virtual filesystems
- [#18374](https://github.com/influxdata/telegraf/pull/18374) `inputs.docker` Remove pre-filtering of states
- [#18383](https://github.com/influxdata/telegraf/pull/18383) `inputs.docker_log` Remove pre-filtering of states
- [#18347](https://github.com/influxdata/telegraf/pull/18347) `inputs.jenkins` Report all concurrent builds
- [#18377](https://github.com/influxdata/telegraf/pull/18377) `inputs.prometheus` Add thread safety and proper cleanup for shared informer factories
- [#18304](https://github.com/influxdata/telegraf/pull/18304) `inputs.prometheus` Cleanup shared informers on stop
- [#18367](https://github.com/influxdata/telegraf/pull/18367) `inputs.upsd` Stop silently dropping mandatory variables from additional\_fields
- [#18386](https://github.com/influxdata/telegraf/pull/18386) `serializers.template` Unwrap tracking metrics

### Dependency Updates

- [#18354](https://github.com/influxdata/telegraf/pull/18354) `deps` Bump cloud.google.com/go/auth from 0.18.1 to 0.18.2
- [#18324](https://github.com/influxdata/telegraf/pull/18324) `deps` Bump cloud.google.com/go/bigquery from 1.72.0 to 1.73.1
- [#18319](https://github.com/influxdata/telegraf/pull/18319) `deps` Bump cloud.google.com/go/pubsub/v2 from 2.3.0 to 2.4.0
- [#18298](https://github.com/influxdata/telegraf/pull/18298) `deps` Bump cloud.google.com/go/storage from 1.59.1 to 1.59.2
- [#18361](https://github.com/influxdata/telegraf/pull/18361) `deps` Bump cloud.google.com/go/storage from 1.59.2 to 1.60.0
- [#18376](https://github.com/influxdata/telegraf/pull/18376) `deps` Bump filippo.io/edwards25519 from 1.1.0 to 1.1.1
- [#18292](https://github.com/influxdata/telegraf/pull/18292) `deps` Bump github.com/ClickHouse/clickhouse-go/v2 from 2.42.0 to 2.43.0
- [#18295](https://github.com/influxdata/telegraf/pull/18295) `deps` Bump github.com/IBM/nzgo/v12 from 12.0.10 to 12.0.11
- [#18297](https://github.com/influxdata/telegraf/pull/18297) `deps` Bump github.com/SAP/go-hdb from 1.14.18 to 1.14.19
- [#18328](https://github.com/influxdata/telegraf/pull/18328) `deps` Bump github.com/SAP/go-hdb from 1.14.19 to 1.14.22
- [#18364](https://github.com/influxdata/telegraf/pull/18364) `deps` Bump github.com/SAP/go-hdb from 1.14.22 to 1.15.0
- [#18358](https://github.com/influxdata/telegraf/pull/18358) `deps` Bump github.com/alitto/pond/v2 from 2.6.0 to 2.6.2
- [#18289](https://github.com/influxdata/telegraf/pull/18289) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.282.0 to 1.285.0
- [#18362](https://github.com/influxdata/telegraf/pull/18362) `deps` Bump github.com/coocood/freecache from 1.2.4 to 1.2.5
- [#18299](https://github.com/influxdata/telegraf/pull/18299) `deps` Bump github.com/coreos/go-systemd/v22 from 22.6.0 to 22.7.0
- [#18294](https://github.com/influxdata/telegraf/pull/18294) `deps` Bump github.com/golang-jwt/jwt/v5 from 5.3.0 to 5.3.1
- [#18291](https://github.com/influxdata/telegraf/pull/18291) `deps` Bump github.com/google/cel-go from 0.26.1 to 0.27.0
- [#18330](https://github.com/influxdata/telegraf/pull/18330) `deps` Bump github.com/klauspost/compress from 1.18.3 to 1.18.4
- [#18268](https://github.com/influxdata/telegraf/pull/18268) `deps` Bump github.com/lxc/incus/v6 from 6.20.0 to 6.21.0
- [#18296](https://github.com/influxdata/telegraf/pull/18296) `deps` Bump github.com/nats-io/nats-server/v2 from 2.12.3 to 2.12.4
- [#18356](https://github.com/influxdata/telegraf/pull/18356) `deps` Bump github.com/p4lang/p4runtime from 1.4.1 to 1.5.0
- [#18326](https://github.com/influxdata/telegraf/pull/18326) `deps` Bump github.com/prometheus-community/pro-bing from 0.7.0 to 0.8.0
- [#18355](https://github.com/influxdata/telegraf/pull/18355) `deps` Bump github.com/redis/go-redis/v9 from 9.17.3 to 9.18.0
- [#18293](https://github.com/influxdata/telegraf/pull/18293) `deps` Bump github.com/shirou/gopsutil/v4 from 4.25.11 to 4.26.1
- [#18331](https://github.com/influxdata/telegraf/pull/18331) `deps` Bump github.com/snowflakedb/gosnowflake from 1.18.1 to 1.19.0
- [#18323](https://github.com/influxdata/telegraf/pull/18323) `deps` Bump github.com/vertica/vertica-sql-go from 1.3.4 to 1.3.5
- [#18290](https://github.com/influxdata/telegraf/pull/18290) `deps` Bump go.mongodb.org/mongo-driver from 1.17.7 to 1.17.8
- [#18332](https://github.com/influxdata/telegraf/pull/18332) `deps` Bump go.mongodb.org/mongo-driver from 1.17.8 to 1.17.9
- [#18318](https://github.com/influxdata/telegraf/pull/18318) `deps` Bump golang.org/x/mod from 0.32.0 to 0.33.0
- [#18322](https://github.com/influxdata/telegraf/pull/18322) `deps` Bump golang.org/x/net from 0.49.0 to 0.50.0
- [#18333](https://github.com/influxdata/telegraf/pull/18333) `deps` Bump golang.org/x/term from 0.39.0 to 0.40.0
- [#18329](https://github.com/influxdata/telegraf/pull/18329) `deps` Bump golang.org/x/text from 0.33.0 to 0.34.0
- [#18300](https://github.com/influxdata/telegraf/pull/18300) `deps` Bump google.golang.org/api from 0.262.0 to 0.264.0
- [#18317](https://github.com/influxdata/telegraf/pull/18317) `deps` Bump google.golang.org/api from 0.264.0 to 0.265.0
- [#18357](https://github.com/influxdata/telegraf/pull/18357) `deps` Bump google.golang.org/grpc from 1.78.0 to 1.79.1
- [#18363](https://github.com/influxdata/telegraf/pull/18363) `deps` Bump k8s.io/client-go from 0.35.0 to 0.35.1
- [#18327](https://github.com/influxdata/telegraf/pull/18327) `deps` Bump modernc.org/sqlite from 1.44.3 to 1.45.0
- [#18288](https://github.com/influxdata/telegraf/pull/18288) `deps` Bump super-linter/super-linter from 8.3.2 to 8.4.0
- [#18315](https://github.com/influxdata/telegraf/pull/18315) `deps` Bump super-linter/super-linter from 8.4.0 to 8.5.0
- [#18353](https://github.com/influxdata/telegraf/pull/18353) `deps` Bump the aws-sdk-go-v2 group with 2 updates
- [#18316](https://github.com/influxdata/telegraf/pull/18316) `deps` Bump the aws-sdk-go-v2 group with 2 updates
- [#18314](https://github.com/influxdata/telegraf/pull/18314) `deps` Bump tj-actions/changed-files from 47.0.1 to 47.0.2
- [#18372](https://github.com/influxdata/telegraf/pull/18372) `deps` Update github.com/pion/dtls from v2 to v3

## v1.37.2

### Bugfixes

- [#18254](https://github.com/influxdata/telegraf/pull/18254) `inputs.cisco_telemetry_mdt` Handle DME events correctly
- [#18177](https://github.com/influxdata/telegraf/pull/18177) `inputs.nftables` Handle named counter references in JSON output
- [#18233](https://github.com/influxdata/telegraf/pull/18233) `inputs.procstat` Handle newer versions of systemd correctly
- [#18225](https://github.com/influxdata/telegraf/pull/18225) `inputs.statsd` Handle negative lengths
- [#18278](https://github.com/influxdata/telegraf/pull/18278) `parsers.dropwizard` Correct sample config setting name for tag path

### Dependency Updates

- [#18204](https://github.com/influxdata/telegraf/pull/18204) `deps` Bump aws-sdk-go-v2 group with 11 updates
- [#18260](https://github.com/influxdata/telegraf/pull/18260) `deps` Bump aws-sdk-go-v2 group with 2 updates
- [#18265](https://github.com/influxdata/telegraf/pull/18265) `deps` Bump cloud.google.com/go/auth from 0.18.0 to 0.18.1
- [#18212](https://github.com/influxdata/telegraf/pull/18212) `deps` Bump cloud.google.com/go/storage from 1.58.0 to 1.59.0
- [#18243](https://github.com/influxdata/telegraf/pull/18243) `deps` Bump cloud.google.com/go/storage from 1.59.0 to 1.59.1
- [#18237](https://github.com/influxdata/telegraf/pull/18237) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/azcore from 1.20.0 to 1.21.0
- [#18216](https://github.com/influxdata/telegraf/pull/18216) `deps` Bump github.com/SAP/go-hdb from 1.14.16 to 1.14.17
- [#18236](https://github.com/influxdata/telegraf/pull/18236) `deps` Bump github.com/SAP/go-hdb from 1.14.17 to 1.14.18
- [#18270](https://github.com/influxdata/telegraf/pull/18270) `deps` Bump github.com/apache/arrow-go/v18 from 18.5.0 to 18.5.1
- [#18235](https://github.com/influxdata/telegraf/pull/18235) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.279.1 to 1.279.2
- [#18206](https://github.com/influxdata/telegraf/pull/18206) `deps` Bump github.com/gosnmp/gosnmp from 1.43.1 to 1.43.2
- [#18240](https://github.com/influxdata/telegraf/pull/18240) `deps` Bump github.com/hashicorp/consul/api from 1.33.0 to 1.33.2
- [#18242](https://github.com/influxdata/telegraf/pull/18242) `deps` Bump github.com/klauspost/compress from 1.18.2 to 1.18.3
- [#18266](https://github.com/influxdata/telegraf/pull/18266) `deps` Bump github.com/linkedin/goavro/v2 from 2.14.1 to 2.15.0
- [#18239](https://github.com/influxdata/telegraf/pull/18239) `deps` Bump github.com/microsoft/go-mssqldb from 1.9.5 to 1.9.6
- [#18210](https://github.com/influxdata/telegraf/pull/18210) `deps` Bump github.com/miekg/dns from 1.1.69 to 1.1.70
- [#18264](https://github.com/influxdata/telegraf/pull/18264) `deps` Bump github.com/miekg/dns from 1.1.70 to 1.1.72
- [#18271](https://github.com/influxdata/telegraf/pull/18271) `deps` Bump github.com/redis/go-redis/v9 from 9.17.2 to 9.17.3
- [#18244](https://github.com/influxdata/telegraf/pull/18244) `deps` Bump github.com/sirupsen/logrus from 1.9.3 to 1.9.4
- [#18262](https://github.com/influxdata/telegraf/pull/18262) `deps` Bump github.com/tdrn-org/go-tr064 from 0.2.2 to 0.2.3
- [#18267](https://github.com/influxdata/telegraf/pull/18267) `deps` Bump go.mongodb.org/mongo-driver from 1.17.6 to 1.17.7
- [#18269](https://github.com/influxdata/telegraf/pull/18269) `deps` Bump go.step.sm/crypto from 0.75.0 to 0.76.0
- [#18215](https://github.com/influxdata/telegraf/pull/18215) `deps` Bump golang.org/x/crypto from 0.46.0 to 0.47.0
- [#18208](https://github.com/influxdata/telegraf/pull/18208) `deps` Bump golang.org/x/mod from 0.31.0 to 0.32.0
- [#18207](https://github.com/influxdata/telegraf/pull/18207) `deps` Bump golang.org/x/net from 0.48.0 to 0.49.0
- [#18217](https://github.com/influxdata/telegraf/pull/18217) `deps` Bump gonum.org/v1/gonum from 0.16.0 to 0.17.0
- [#18261](https://github.com/influxdata/telegraf/pull/18261) `deps` Bump google.golang.org/api from 0.257.0 to 0.262.0
- [#18213](https://github.com/influxdata/telegraf/pull/18213) `deps` Bump modernc.org/sqlite from 1.42.2 to 1.43.0
- [#18241](https://github.com/influxdata/telegraf/pull/18241) `deps` Bump modernc.org/sqlite from 1.43.0 to 1.44.2
- [#18263](https://github.com/influxdata/telegraf/pull/18263) `deps` Bump modernc.org/sqlite from 1.44.2 to 1.44.3

## v1.37.1

### Bugfixes

- [#18138](https://github.com/influxdata/telegraf/pull/18138) `config` Add missing validation for labels in plugins
- [#18108](https://github.com/influxdata/telegraf/pull/18108) `config` Make labels and selectors conform to specification
- [#18144](https://github.com/influxdata/telegraf/pull/18144) `inputs.procstat` Isolate process cache per filter to fix tag collision
- [#18191](https://github.com/influxdata/telegraf/pull/18191) `outputs.sql` Populate column cache for existing tables

### Dependency Updates

- [#18125](https://github.com/influxdata/telegraf/pull/18125) `deps` Bump cloud.google.com/go/auth from 0.17.0 to 0.18.0
- [#18140](https://github.com/influxdata/telegraf/pull/18140) `deps` Bump cloud.google.com/go/auth from 0.17.0 to 0.18.0
- [#18094](https://github.com/influxdata/telegraf/pull/18094) `deps` Bump cloud.google.com/go/storage from 1.57.2 to 1.58.0
- [#18157](https://github.com/influxdata/telegraf/pull/18157) `deps` Bump github.com/BurntSushi/toml from 1.5.0 to 1.6.0
- [#18124](https://github.com/influxdata/telegraf/pull/18124) `deps` Bump github.com/ClickHouse/clickhouse-go/v2 from 2.41.0 to 2.42.0
- [#18101](https://github.com/influxdata/telegraf/pull/18101) `deps` Bump github.com/SAP/go-hdb from 1.14.13 to 1.14.14
- [#18153](https://github.com/influxdata/telegraf/pull/18153) `deps` Bump github.com/SAP/go-hdb from 1.14.14 to 1.14.15
- [#18199](https://github.com/influxdata/telegraf/pull/18199) `deps` Bump github.com/SAP/go-hdb from 1.14.15 to 1.14.16
- [#18123](https://github.com/influxdata/telegraf/pull/18123) `deps` Bump github.com/apache/arrow-go/v18 from 18.4.1 to 18.5.0
- [#18200](https://github.com/influxdata/telegraf/pull/18200) `deps` Bump github.com/apache/inlong/inlong-sdk/dataproxy-sdk-twins/dataproxy-sdk-golang from 1.0.6 to 1.0.7
- [#18197](https://github.com/influxdata/telegraf/pull/18197) `deps` Bump github.com/gophercloud/gophercloud/v2 from 2.9.0 to 2.10.0
- [#18198](https://github.com/influxdata/telegraf/pull/18198) `deps` Bump github.com/gosnmp/gosnmp from 1.42.1 to 1.43.1
- [#18132](https://github.com/influxdata/telegraf/pull/18132) `deps` Bump github.com/jedib0t/go-pretty/v6 from 6.7.5 to 6.7.7
- [#18169](https://github.com/influxdata/telegraf/pull/18169) `deps` Bump github.com/jedib0t/go-pretty/v6 from 6.7.7 to 6.7.8
- [#18189](https://github.com/influxdata/telegraf/pull/18189) `deps` Bump github.com/likexian/whois from 1.15.6 to 1.15.7
- [#18187](https://github.com/influxdata/telegraf/pull/18187) `deps` Bump github.com/likexian/whois-parser from 1.24.20 to 1.24.21
- [#18150](https://github.com/influxdata/telegraf/pull/18150) `deps` Bump github.com/lxc/incus/v6 from 6.19.1 to 6.20.0
- [#18130](https://github.com/influxdata/telegraf/pull/18130) `deps` Bump github.com/miekg/dns from 1.1.68 to 1.1.69
- [#18149](https://github.com/influxdata/telegraf/pull/18149) `deps` Bump github.com/nats-io/nats-server/v2 from 2.12.2 to 2.12.3
- [#18147](https://github.com/influxdata/telegraf/pull/18147) `deps` Bump github.com/nats-io/nats.go from 1.47.0 to 1.48.0
- [#18172](https://github.com/influxdata/telegraf/pull/18172) `deps` Bump github.com/netsampler/goflow2/v2 from 2.2.3 to 2.2.6
- [#18190](https://github.com/influxdata/telegraf/pull/18190) `deps` Bump github.com/prometheus/common from 0.67.4 to 0.67.5
- [#18102](https://github.com/influxdata/telegraf/pull/18102) `deps` Bump github.com/prometheus/prometheus from 0.307.3 to 0.308.0
- [#18155](https://github.com/influxdata/telegraf/pull/18155) `deps` Bump github.com/prometheus/prometheus from 0.308.0 to 0.308.1
- [#18129](https://github.com/influxdata/telegraf/pull/18129) `deps` Bump github.com/snowflakedb/gosnowflake from 1.18.0 to 1.18.1
- [#18103](https://github.com/influxdata/telegraf/pull/18103) `deps` Bump github.com/tinylib/msgp from 1.5.0 to 1.6.1
- [#18188](https://github.com/influxdata/telegraf/pull/18188) `deps` Bump github.com/tinylib/msgp from 1.6.1 to 1.6.3
- [#18186](https://github.com/influxdata/telegraf/pull/18186) `deps` Bump github.com/yuin/goldmark from 1.7.13 to 1.7.15
- [#18201](https://github.com/influxdata/telegraf/pull/18201) `deps` Bump github.com/yuin/goldmark from 1.7.15 to 1.7.16
- [#18092](https://github.com/influxdata/telegraf/pull/18092) `deps` Bump go.step.sm/crypto from 0.74.0 to 0.75.0
- [#18098](https://github.com/influxdata/telegraf/pull/18098) `deps` Bump golang.org/x/crypto from 0.45.0 to 0.46.0
- [#18100](https://github.com/influxdata/telegraf/pull/18100) `deps` Bump golang.org/x/mod from 0.30.0 to 0.31.0
- [#18127](https://github.com/influxdata/telegraf/pull/18127) `deps` Bump golang.org/x/net from 0.47.0 to 0.48.0
- [#18095](https://github.com/influxdata/telegraf/pull/18095) `deps` Bump golang.org/x/oauth2 from 0.33.0 to 0.34.0
- [#18093](https://github.com/influxdata/telegraf/pull/18093) `deps` Bump golang.org/x/sync from 0.18.0 to 0.19.0
- [#18096](https://github.com/influxdata/telegraf/pull/18096) `deps` Bump golang.org/x/sys from 0.38.0 to 0.39.0
- [#18099](https://github.com/influxdata/telegraf/pull/18099) `deps` Bump golang.org/x/term from 0.37.0 to 0.38.0
- [#18097](https://github.com/influxdata/telegraf/pull/18097) `deps` Bump golang.org/x/text from 0.31.0 to 0.32.0
- [#18104](https://github.com/influxdata/telegraf/pull/18104) `deps` Bump google.golang.org/api from 0.256.0 to 0.257.0
- [#18173](https://github.com/influxdata/telegraf/pull/18173) `deps` Bump google.golang.org/grpc from 1.77.0 to 1.78.0
- [#18131](https://github.com/influxdata/telegraf/pull/18131) `deps` Bump google.golang.org/protobuf from 1.36.10 to 1.36.11
- [#18128](https://github.com/influxdata/telegraf/pull/18128) `deps` Bump k8s.io/api from 0.34.2 to 0.34.3
- [#18148](https://github.com/influxdata/telegraf/pull/18148) `deps` Bump k8s.io/apimachinery from 0.34.3 to 0.35.0
- [#18126](https://github.com/influxdata/telegraf/pull/18126) `deps` Bump k8s.io/client-go from 0.34.2 to 0.34.3
- [#18154](https://github.com/influxdata/telegraf/pull/18154) `deps` Bump k8s.io/client-go from 0.34.3 to 0.35.0
- [#18152](https://github.com/influxdata/telegraf/pull/18152) `deps` Bump modernc.org/sqlite from 1.40.1 to 1.41.0
- [#18171](https://github.com/influxdata/telegraf/pull/18171) `deps` Bump modernc.org/sqlite from 1.41.0 to 1.42.2
- [#18170](https://github.com/influxdata/telegraf/pull/18170) `deps` Bump software.sslmate.com/src/go-pkcs12 from 0.6.0 to 0.7.0
- [#18158](https://github.com/influxdata/telegraf/pull/18158) `deps` Bump super-linter/super-linter from 8.3.0 to 8.3.1
- [#18174](https://github.com/influxdata/telegraf/pull/18174) `deps` Bump super-linter/super-linter from 8.3.1 to 8.3.2
- [#18091](https://github.com/influxdata/telegraf/pull/18091) `deps` Bump the aws-sdk-go-v2 group with 11 updates
- [#18146](https://github.com/influxdata/telegraf/pull/18146) `deps` Bump the aws-sdk-go-v2 group with 3 updates
- [#18121](https://github.com/influxdata/telegraf/pull/18121) `deps` Bump the aws-sdk-go-v2 group with 8 updates
- [#18120](https://github.com/influxdata/telegraf/pull/18120) `deps` Bump tj-actions/changed-files from 47.0.0 to 47.0.1
- [#18115](https://github.com/influxdata/telegraf/pull/18115) `deps` Update golangci-lint to 2.7.2

## v1.37.0

### Important Changes

- PR [#17966](https://github.com/influxdata/telegraf/pull/17966) introduced the strict handling of environment variables to prevent security issues. However, strict handling prevents using environment variables for non-string settings as the configuration before replacing the variables must be TOML conform. To provide security-by-default, we will change the **default behavior of Telegraf to the strict environment variable handling with v1.38.0**! Please make sure your configuration works in the now conditions by using the `--strict-env-handling` flag! If your configuration works in strict mode or you are not using environment variables, **do not** add the flag as it will be removed later and ignore the new warning at startup. In case you need the current behavior please add `--non-strict-env-handling` when starting Telegraf to prepare for the upcoming change!

### New Plugins

- [#17993](https://github.com/influxdata/telegraf/pull/17993) `inputs.logql` Add plugin
- [#17604](https://github.com/influxdata/telegraf/pull/17604) `inputs.nftables` Add plugin
- [#17701](https://github.com/influxdata/telegraf/pull/17701) `inputs.promql` Add plugin
- [#17831](https://github.com/influxdata/telegraf/pull/17831) `inputs.timex` Add plugin
- [#17875](https://github.com/influxdata/telegraf/pull/17875) `outputs.arc` Add plugin
- [#17998](https://github.com/influxdata/telegraf/pull/17998) `outputs.heartbeat` Add plugin
- [#17921](https://github.com/influxdata/telegraf/pull/17921) `secretstores.googlecloud` Add plugin
- [#17844](https://github.com/influxdata/telegraf/pull/17844) `secretstores.vault` Add plugin

### Features

- [#18084](https://github.com/influxdata/telegraf/pull/18084) `config` Allow specifying env-handling mode for config check
- [#17753](https://github.com/influxdata/telegraf/pull/17753) `config` Remove deprecated options
- [#17915](https://github.com/influxdata/telegraf/pull/17915) `config` Store loaded sources
- [#17080](https://github.com/influxdata/telegraf/pull/17080) `internal` Add support for parsing a timestamp in a TimeZone
- [#17916](https://github.com/influxdata/telegraf/pull/17916) `logging` Allow registering callbacks for logging events
- [#17749](https://github.com/influxdata/telegraf/pull/17749) `models` Implement collection of plugin-internal statistics for all types
- [#18044](https://github.com/influxdata/telegraf/pull/18044) `common.socket` Add option to specify source IP restrictions
- [#17760](https://github.com/influxdata/telegraf/pull/17760) `inputs.aerospike` Remove deprecated options
- [#17759](https://github.com/influxdata/telegraf/pull/17759) `inputs.cpu` Add number of physical CPUs
- [#17761](https://github.com/influxdata/telegraf/pull/17761) `inputs.gnmi` Remove deprecated options
- [#17732](https://github.com/influxdata/telegraf/pull/17732) `inputs.influxdb_v2_listener` Implement ping endpoint
- [#17733](https://github.com/influxdata/telegraf/pull/17733) `inputs.influxdb_v2_listener` Migrate to selfstat collector
- [#17965](https://github.com/influxdata/telegraf/pull/17965) `inputs.ldap` Support external SASL bind (#17477)
- [#17478](https://github.com/influxdata/telegraf/pull/17478) `inputs.ldap` Support ldapi protocol
- [#17743](https://github.com/influxdata/telegraf/pull/17743) `inputs.modbus` Remove deprecated plugin option values
- [#17762](https://github.com/influxdata/telegraf/pull/17762) `inputs.mongodb` Remove deprecated options
- [#17792](https://github.com/influxdata/telegraf/pull/17792) `inputs.nats_consumer` Acknowledge messages on delivery
- [#17710](https://github.com/influxdata/telegraf/pull/17710) `inputs.nats_consumer` Allow configuring Jetstream stream
- [#17742](https://github.com/influxdata/telegraf/pull/17742) `inputs.net` Remove deprecated plugin option value
- [#17624](https://github.com/influxdata/telegraf/pull/17624) `inputs.netflow` Add datatypes to PEN mapping
- [#17697](https://github.com/influxdata/telegraf/pull/17697) `inputs.netflow` Add support for float32 datatype
- [#17906](https://github.com/influxdata/telegraf/pull/17906) `inputs.opcua` Add namespace URI support
- [#17825](https://github.com/influxdata/telegraf/pull/17825) `inputs.opcua` Add remote certificate trust configuration
- [#17752](https://github.com/influxdata/telegraf/pull/17752) `inputs.opcua` Remove deprecated options
- [#17991](https://github.com/influxdata/telegraf/pull/17991) `inputs.opcua` Support persistent self-signed client certificates
- [#17633](https://github.com/influxdata/telegraf/pull/17633) `inputs.rabbitmq` Add type tag to queues
- [#18080](https://github.com/influxdata/telegraf/pull/18080) `inputs.s7comm` Add option idle\_timeout
- [#17550](https://github.com/influxdata/telegraf/pull/17550) `inputs.smart` Parse vendor specific ratio values
- [#17948](https://github.com/influxdata/telegraf/pull/17948) `inputs.snmp` Add option to stop polling on first error
- [#17375](https://github.com/influxdata/telegraf/pull/17375) `inputs.sql` Add Vertica support
- [#17924](https://github.com/influxdata/telegraf/pull/17924) `inputs.sqlserver` Add support for LPC and named-pipe protocols
- [#17796](https://github.com/influxdata/telegraf/pull/17796) `inputs.sqlserver` Set pool size and idle connection
- [#17872](https://github.com/influxdata/telegraf/pull/17872) `inputs.statsd` Improve performance
- [#17763](https://github.com/influxdata/telegraf/pull/17763) `inputs.win_perf_counters` Remove deprecated options
- [#17751](https://github.com/influxdata/telegraf/pull/17751) `inputs.zookeeper` Remove deprecated option
- [#17950](https://github.com/influxdata/telegraf/pull/17950) `outputs.amon` Deprecate plugin
- [#18062](https://github.com/influxdata/telegraf/pull/18062) `outputs.heartbeat` Add configuration information
- [#18050](https://github.com/influxdata/telegraf/pull/18050) `outputs.heartbeat` Add optional statistics output
- [#17869](https://github.com/influxdata/telegraf/pull/17869) `outputs.mongodb` Add PLAIN authentication support and validation
- [#17755](https://github.com/influxdata/telegraf/pull/17755) `outputs.mqtt` Remove deprecated option
- [#18048](https://github.com/influxdata/telegraf/pull/18048) `outputs.nats` Add secret-support for credentials
- [#18007](https://github.com/influxdata/telegraf/pull/18007) `outputs.nats` Support nkey seed authentication
- [#17409](https://github.com/influxdata/telegraf/pull/17409) `outputs.remotefile` Add compression for remotefile plugin
- [#17764](https://github.com/influxdata/telegraf/pull/17764) `parsers.binary` Remove deprecated options
- [#17754](https://github.com/influxdata/telegraf/pull/17754) `parsers.xpath` Remove deprecated options
- [#17576](https://github.com/influxdata/telegraf/pull/17576) `processors.execd` Add log prefixing
- [#17741](https://github.com/influxdata/telegraf/pull/17741) `processors.template` Remove deprecated template syntax

### Bugfixes

- [#18064](https://github.com/influxdata/telegraf/pull/18064) `common.opcua` Skip file permission check on Windows
- [#18012](https://github.com/influxdata/telegraf/pull/18012) `inputs.docker_log` Remove hard-coded API version
- [#17960](https://github.com/influxdata/telegraf/pull/17960) `inputs.opcua` Add private key for certificate-based user authentication
- [#18036](https://github.com/influxdata/telegraf/pull/18036) `inputs.procstat` Make port conversion more robust
- [#18014](https://github.com/influxdata/telegraf/pull/18014) `outputs.influxdb_v2` Correct calculation of amount of batches for concurrent writes

### Dependency Updates

- [#18051](https://github.com/influxdata/telegraf/pull/18051) `deps` Bump actions/checkout from 5 to 6
- [#18021](https://github.com/influxdata/telegraf/pull/18021) `deps` Bump cloud.google.com/go/storage from 1.57.1 to 1.57.2
- [#18055](https://github.com/influxdata/telegraf/pull/18055) `deps` Bump github.com/ClickHouse/clickhouse-go/v2 from 2.40.3 to 2.41.0
- [#18019](https://github.com/influxdata/telegraf/pull/18019) `deps` Bump github.com/SAP/go-hdb from 1.14.12 to 1.14.13
- [#18076](https://github.com/influxdata/telegraf/pull/18076) `deps` Bump github.com/alitto/pond/v2 from 2.5.0 to 2.6.0
- [#18074](https://github.com/influxdata/telegraf/pull/18074) `deps` Bump github.com/aws/smithy-go from 1.23.2 to 1.24.0
- [#18020](https://github.com/influxdata/telegraf/pull/18020) `deps` Bump github.com/gophercloud/gophercloud/v2 from 2.8.0 to 2.9.0
- [#17887](https://github.com/influxdata/telegraf/pull/17887) `deps` Bump github.com/hashicorp/consul/api from 1.32.4 to 1.33.0
- [#18024](https://github.com/influxdata/telegraf/pull/18024) `deps` Bump github.com/jedib0t/go-pretty/v6 from 6.7.1 to 6.7.2
- [#18056](https://github.com/influxdata/telegraf/pull/18056) `deps` Bump github.com/jedib0t/go-pretty/v6 from 6.7.2 to 6.7.5
- [#18072](https://github.com/influxdata/telegraf/pull/18072) `deps` Bump github.com/klauspost/compress from 1.18.1 to 1.18.2
- [#18071](https://github.com/influxdata/telegraf/pull/18071) `deps` Bump github.com/lxc/incus/v6 from 6.18.0 to 6.19.1
- [#18018](https://github.com/influxdata/telegraf/pull/18018) `deps` Bump github.com/microsoft/go-mssqldb from 1.9.3 to 1.9.4
- [#18017](https://github.com/influxdata/telegraf/pull/18017) `deps` Bump github.com/nats-io/nats-server/v2 from 2.12.1 to 2.12.2
- [#18054](https://github.com/influxdata/telegraf/pull/18054) `deps` Bump github.com/prometheus/common from 0.67.2 to 0.67.4
- [#18053](https://github.com/influxdata/telegraf/pull/18053) `deps` Bump github.com/redis/go-redis/v9 from 9.16.0 to 9.17.0
- [#18073](https://github.com/influxdata/telegraf/pull/18073) `deps` Bump github.com/redis/go-redis/v9 from 9.17.0 to 9.17.2
- [#18027](https://github.com/influxdata/telegraf/pull/18027) `deps` Bump github.com/safchain/ethtool from 0.6.2 to 0.7.0
- [#18070](https://github.com/influxdata/telegraf/pull/18070) `deps` Bump github.com/shirou/gopsutil/v4 from 4.25.10 to 4.25.11
- [#18057](https://github.com/influxdata/telegraf/pull/18057) `deps` Bump github.com/snowflakedb/gosnowflake from 1.17.0 to 1.18.0
- [#17815](https://github.com/influxdata/telegraf/pull/17815) `deps` Bump github.com/vertica/vertica-sql-go from 1.3.3 to 1.3.4
- [#18031](https://github.com/influxdata/telegraf/pull/18031) `deps` Bump go.opentelemetry.io/collector/pdata from 1.45.0 to 1.46.0
- [#18043](https://github.com/influxdata/telegraf/pull/18043) `deps` Bump golang.org/x/crypto from 0.44.0 to 0.45.0
- [#18023](https://github.com/influxdata/telegraf/pull/18023) `deps` Bump golang.org/x/mod from 0.29.0 to 0.30.0
- [#18029](https://github.com/influxdata/telegraf/pull/18029) `deps` Bump golang.org/x/net from 0.46.0 to 0.47.0
- [#18025](https://github.com/influxdata/telegraf/pull/18025) `deps` Bump google.golang.org/api from 0.255.0 to 0.256.0
- [#18058](https://github.com/influxdata/telegraf/pull/18058) `deps` Bump google.golang.org/grpc from 1.76.0 to 1.77.0
- [#18033](https://github.com/influxdata/telegraf/pull/18033) `deps` Bump k8s.io/client-go from 0.34.1 to 0.34.2
- [#18030](https://github.com/influxdata/telegraf/pull/18030) `deps` Bump modernc.org/sqlite from 1.40.0 to 1.40.1
- [#18069](https://github.com/influxdata/telegraf/pull/18069) `deps` Bump super-linter/super-linter from 8.2.1 to 8.3.0
- [#18052](https://github.com/influxdata/telegraf/pull/18052) `deps` Bump the aws-sdk-go-v2 group with 11 updates
- [#18015](https://github.com/influxdata/telegraf/pull/18015) `deps` Bump the aws-sdk-go-v2 group with 9 updates

## v1.36.4

### Bugfixes

- [#17873](https://github.com/influxdata/telegraf/pull/17873) `common.kafka` Avoid API version requests for SASLv0 handshakes
- [#17966](https://github.com/influxdata/telegraf/pull/17966) `config` Implement strict envvar handling to prevent insecure text replacement
- [#17877](https://github.com/influxdata/telegraf/pull/17877) `inputs.kinesis_consumer` Ignore expired parent shards
- [#17908](https://github.com/influxdata/telegraf/pull/17908) `inputs.tail` Handle missing read permissions for directory globbing
- [#17968](https://github.com/influxdata/telegraf/pull/17968) `inputs.turbostat` Allow floating point intervals
- [#17953](https://github.com/influxdata/telegraf/pull/17953) `inputs.zfs` Avoid panic by handling explicitly empty kstat metrics
- [#17949](https://github.com/influxdata/telegraf/pull/17949) `outputs.influxdb_v2` Handle serialization errors correctly
- [#17920](https://github.com/influxdata/telegraf/pull/17920) `outputs.loki` Sanitize colons in label names
- [#17990](https://github.com/influxdata/telegraf/pull/17990) `outputs.sql` Mark table as found during initial existence check

### Dependency Updates

- [#17935](https://github.com/influxdata/telegraf/pull/17935) `deps` Bump cloud.google.com/go/bigquery from 1.71.0 to 1.72.0
- [#17897](https://github.com/influxdata/telegraf/pull/17897) `deps` Bump cloud.google.com/go/pubsub/v2 from 2.2.1 to 2.3.0
- [#17943](https://github.com/influxdata/telegraf/pull/17943) `deps` Bump cloud.google.com/go/storage from 1.57.0 to 1.57.1
- [#17970](https://github.com/influxdata/telegraf/pull/17970) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/azcore from 1.19.1 to 1.20.0
- [#17973](https://github.com/influxdata/telegraf/pull/17973) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/azidentity from 1.13.0 to 1.13.1
- [#17901](https://github.com/influxdata/telegraf/pull/17901) `deps` Bump github.com/IBM/sarama from 1.46.2 to 1.46.3
- [#17889](https://github.com/influxdata/telegraf/pull/17889) `deps` Bump github.com/SAP/go-hdb from 1.14.7 to 1.14.9
- [#17977](https://github.com/influxdata/telegraf/pull/17977) `deps` Bump github.com/SAP/go-hdb from 1.14.9 to 1.14.12
- [#17981](https://github.com/influxdata/telegraf/pull/17981) `deps` Bump github.com/apache/iotdb-client-go from 1.3.4 to 1.3.5
- [#17900](https://github.com/influxdata/telegraf/pull/17900) `deps` Bump github.com/aws/aws-sdk-go-v2 from 1.39.3 to 1.39.4
- [#17899](https://github.com/influxdata/telegraf/pull/17899) `deps` Bump github.com/aws/aws-sdk-go-v2/config from 1.31.13 to 1.31.15
- [#17898](https://github.com/influxdata/telegraf/pull/17898) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatch from 1.51.2 to 1.51.4
- [#17858](https://github.com/influxdata/telegraf/pull/17858) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs from 1.58.2 to 1.58.3
- [#17892](https://github.com/influxdata/telegraf/pull/17892) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs from 1.58.3 to 1.58.5
- [#17854](https://github.com/influxdata/telegraf/pull/17854) `deps` Bump github.com/aws/aws-sdk-go-v2/service/dynamodb from 1.51.0 to 1.51.1
- [#17890](https://github.com/influxdata/telegraf/pull/17890) `deps` Bump github.com/aws/aws-sdk-go-v2/service/dynamodb from 1.51.1 to 1.52.2
- [#17855](https://github.com/influxdata/telegraf/pull/17855) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.255.0 to 1.257.2
- [#17886](https://github.com/influxdata/telegraf/pull/17886) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.257.2 to 1.258.1
- [#17883](https://github.com/influxdata/telegraf/pull/17883) `deps` Bump github.com/aws/aws-sdk-go-v2/service/kinesis from 1.40.6 to 1.41.0
- [#17847](https://github.com/influxdata/telegraf/pull/17847) `deps` Bump github.com/aws/aws-sdk-go-v2/service/timestreamwrite from 1.35.5 to 1.35.6
- [#17891](https://github.com/influxdata/telegraf/pull/17891) `deps` Bump github.com/aws/aws-sdk-go-v2/service/timestreamwrite from 1.35.6 to 1.35.7
- [#17944](https://github.com/influxdata/telegraf/pull/17944) `deps` Bump github.com/aws/smithy-go from 1.23.1 to 1.23.2
- [#17978](https://github.com/influxdata/telegraf/pull/17978) `deps` Bump github.com/docker/docker from 28.5.1+incompatible to 28.5.2+incompatible
- [#18009](https://github.com/influxdata/telegraf/pull/18009) `deps` Bump github.com/dvsekhvalnov/jose2go from 1.6.0 to 1.7.0
- [#17941](https://github.com/influxdata/telegraf/pull/17941) `deps` Bump github.com/gofrs/uuid/v5 from 5.3.2 to 5.4.0
- [#17927](https://github.com/influxdata/telegraf/pull/17927) `deps` Bump github.com/gopacket/gopacket from 1.4.0 to 1.5.0
- [#17988](https://github.com/influxdata/telegraf/pull/17988) `deps` Bump github.com/influxdata/toml from v0.0.0-20190415235208-270119a8ce65 to v0.0.0-20251106153700-c381e153d076
- [#17932](https://github.com/influxdata/telegraf/pull/17932) `deps` Bump github.com/jedib0t/go-pretty/v6 from 6.6.8 to 6.6.9
- [#17979](https://github.com/influxdata/telegraf/pull/17979) `deps` Bump github.com/jedib0t/go-pretty/v6 from 6.6.9 to 6.7.1
- [#17896](https://github.com/influxdata/telegraf/pull/17896) `deps` Bump github.com/linkedin/goavro/v2 from 2.14.0 to 2.14.1
- [#17942](https://github.com/influxdata/telegraf/pull/17942) `deps` Bump github.com/lxc/incus/v6 from 6.17.0 to 6.18.0
- [#17937](https://github.com/influxdata/telegraf/pull/17937) `deps` Bump github.com/prometheus/common from 0.67.1 to 0.67.2
- [#17885](https://github.com/influxdata/telegraf/pull/17885) `deps` Bump github.com/prometheus/procfs from 0.17.0 to 0.19.1
- [#17930](https://github.com/influxdata/telegraf/pull/17930) `deps` Bump github.com/prometheus/procfs from 0.19.1 to 0.19.2
- [#17894](https://github.com/influxdata/telegraf/pull/17894) `deps` Bump github.com/prometheus/prometheus from 0.307.1 to 0.307.2
- [#17928](https://github.com/influxdata/telegraf/pull/17928) `deps` Bump github.com/prometheus/prometheus from 0.307.2 to 0.307.3
- [#17895](https://github.com/influxdata/telegraf/pull/17895) `deps` Bump github.com/redis/go-redis/v9 from 9.14.1 to 9.16.0
- [#17939](https://github.com/influxdata/telegraf/pull/17939) `deps` Bump github.com/shirou/gopsutil/v4 from 4.25.9 to 4.25.10
- [#17976](https://github.com/influxdata/telegraf/pull/17976) `deps` Bump github.com/testcontainers/testcontainers-go from 0.39.0 to 0.40.0
- [#17983](https://github.com/influxdata/telegraf/pull/17983) `deps` Bump github.com/testcontainers/testcontainers-go/modules/azure from 0.39.0 to 0.40.0
- [#17972](https://github.com/influxdata/telegraf/pull/17972) `deps` Bump github.com/testcontainers/testcontainers-go/modules/kafka from 0.39.0 to 0.40.0
- [#17893](https://github.com/influxdata/telegraf/pull/17893) `deps` Bump github.com/tinylib/msgp from 1.4.0 to 1.5.0
- [#17934](https://github.com/influxdata/telegraf/pull/17934) `deps` Bump go.mongodb.org/mongo-driver from 1.17.4 to 1.17.6
- [#17865](https://github.com/influxdata/telegraf/pull/17865) `deps` Bump go.opentelemetry.io/collector/pdata from 1.43.0 to 1.44.0
- [#17945](https://github.com/influxdata/telegraf/pull/17945) `deps` Bump go.opentelemetry.io/collector/pdata from 1.44.0 to 1.45.0
- [#17933](https://github.com/influxdata/telegraf/pull/17933) `deps` Bump go.opentelemetry.io/proto/otlp from 1.8.0 to 1.9.0
- [#17938](https://github.com/influxdata/telegraf/pull/17938) `deps` Bump go.opentelemetry.io/proto/otlp/collector/profiles/v1development from 0.1.0 to 0.2.0
- [#17936](https://github.com/influxdata/telegraf/pull/17936) `deps` Bump go.step.sm/crypto from 0.72.0 to 0.73.0
- [#17974](https://github.com/influxdata/telegraf/pull/17974) `deps` Bump go.step.sm/crypto from 0.73.0 to 0.74.0
- [#17984](https://github.com/influxdata/telegraf/pull/17984) `deps` Bump golang.org/x/oauth2 from 0.32.0 to 0.33.0
- [#17980](https://github.com/influxdata/telegraf/pull/17980) `deps` Bump golang.org/x/sync from 0.17.0 to 0.18.0
- [#17971](https://github.com/influxdata/telegraf/pull/17971) `deps` Bump golang.org/x/sys from 0.37.0 to 0.38.0
- [#17884](https://github.com/influxdata/telegraf/pull/17884) `deps` Bump google.golang.org/api from 0.252.0 to 0.253.0
- [#17929](https://github.com/influxdata/telegraf/pull/17929) `deps` Bump google.golang.org/api from 0.253.0 to 0.254.0
- [#17975](https://github.com/influxdata/telegraf/pull/17975) `deps` Bump google.golang.org/api from 0.254.0 to 0.255.0
- [#17931](https://github.com/influxdata/telegraf/pull/17931) `deps` Bump modernc.org/sqlite from 1.39.1 to 1.40.0
- [#17926](https://github.com/influxdata/telegraf/pull/17926) `deps` Bump the aws-sdk-go-v2 group with 11 updates
- [#17969](https://github.com/influxdata/telegraf/pull/17969) `deps` Bump the aws-sdk-go-v2 group with 11 updates

## v1.36.3

### Bugfixes

- [#17765](https://github.com/influxdata/telegraf/pull/17765) `inputs.chrony` Prevent race condition in concurrent gather calls
- [#17634](https://github.com/influxdata/telegraf/pull/17634) `inputs.docker` Fix incorrect CPU usage\_percent for Podman containers
- [#17740](https://github.com/influxdata/telegraf/pull/17740) `inputs.kube_inventory` Prevent panic in endpoints’ ready flag
- [#17483](https://github.com/influxdata/telegraf/pull/17483) `inputs.smart` Correct exit\_status for active vs standby drives
- [#17617](https://github.com/influxdata/telegraf/pull/17617) `inputs.zfs` Parse field values according to provided type
- [#17787](https://github.com/influxdata/telegraf/pull/17787) `outputs.nats` Unwrap wrapped metrics to avoid panic on missing Field method
- [#17573](https://github.com/influxdata/telegraf/pull/17573) `parsers.csv` Support concurrent usage
- [#17738](https://github.com/influxdata/telegraf/pull/17738) `secretstores.systemd` Handle dash version separator correctly

### Dependency Updates

- [#17770](https://github.com/influxdata/telegraf/pull/17770) `deps` Bump cloud.google.com/go/bigquery from 1.70.0 to 1.71.0
- [#17821](https://github.com/influxdata/telegraf/pull/17821) `deps` Bump cloud.google.com/go/monitoring from 1.24.2 to 1.24.3
- [#17777](https://github.com/influxdata/telegraf/pull/17777) `deps` Bump cloud.google.com/go/pubsub/v2 from 2.0.0 to 2.2.0
- [#17846](https://github.com/influxdata/telegraf/pull/17846) `deps` Bump cloud.google.com/go/pubsub/v2 from 2.2.0 to 2.2.1
- [#17718](https://github.com/influxdata/telegraf/pull/17718) `deps` Bump cloud.google.com/go/storage from 1.56.2 to 1.57.0
- [#17805](https://github.com/influxdata/telegraf/pull/17805) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/azidentity from 1.12.0 to 1.13.0
- [#17784](https://github.com/influxdata/telegraf/pull/17784) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/messaging/azeventhubs from 1.4.0 to 2.0.0
- [#17810](https://github.com/influxdata/telegraf/pull/17810) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/messaging/azeventhubs/v2 from 2.0.0 to 2.0.1
- [#17804](https://github.com/influxdata/telegraf/pull/17804) `deps` Bump github.com/IBM/sarama from 1.46.1 to 1.46.2
- [#17724](https://github.com/influxdata/telegraf/pull/17724) `deps` Bump github.com/SAP/go-hdb from 1.14.4 to 1.14.5
- [#17808](https://github.com/influxdata/telegraf/pull/17808) `deps` Bump github.com/SAP/go-hdb from 1.14.5 to 1.14.6
- [#17866](https://github.com/influxdata/telegraf/pull/17866) `deps` Bump github.com/SAP/go-hdb from 1.14.6 to 1.14.7
- [#17822](https://github.com/influxdata/telegraf/pull/17822) `deps` Bump github.com/antchfx/xmlquery from 1.4.4 to 1.5.0
- [#17868](https://github.com/influxdata/telegraf/pull/17868) `deps` Bump github.com/aws/aws-sdk-go-v2/config from 1.31.12 to 1.31.13
- [#17730](https://github.com/influxdata/telegraf/pull/17730) `deps` Bump github.com/aws/aws-sdk-go-v2/config from 1.31.9 to 1.31.12
- [#17719](https://github.com/influxdata/telegraf/pull/17719) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatch from 1.50.1 to 1.51.1
- [#17863](https://github.com/influxdata/telegraf/pull/17863) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatch from 1.51.1 to 1.51.2
- [#17716](https://github.com/influxdata/telegraf/pull/17716) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs from 1.58.0 to 1.58.2
- [#17715](https://github.com/influxdata/telegraf/pull/17715) `deps` Bump github.com/aws/aws-sdk-go-v2/service/dynamodb from 1.50.3 to 1.50.5
- [#17772](https://github.com/influxdata/telegraf/pull/17772) `deps` Bump github.com/aws/aws-sdk-go-v2/service/dynamodb from 1.50.5 to 1.51.0
- [#17714](https://github.com/influxdata/telegraf/pull/17714) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.253.0 to 1.254.1
- [#17814](https://github.com/influxdata/telegraf/pull/17814) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.254.1 to 1.255.0
- [#17728](https://github.com/influxdata/telegraf/pull/17728) `deps` Bump github.com/aws/aws-sdk-go-v2/service/kinesis from 1.40.3 to 1.40.5
- [#17848](https://github.com/influxdata/telegraf/pull/17848) `deps` Bump github.com/aws/aws-sdk-go-v2/service/kinesis from 1.40.5 to 1.40.6
- [#17723](https://github.com/influxdata/telegraf/pull/17723) `deps` Bump github.com/aws/aws-sdk-go-v2/service/timestreamwrite from 1.35.3 to 1.35.5
- [#17864](https://github.com/influxdata/telegraf/pull/17864) `deps` Bump github.com/aws/smithy-go from 1.23.0 to 1.23.1
- [#17849](https://github.com/influxdata/telegraf/pull/17849) `deps` Bump github.com/bluenviron/gomavlib/v3 from 3.2.1 to 3.3.0
- [#17774](https://github.com/influxdata/telegraf/pull/17774) `deps` Bump github.com/docker/docker from 28.4.0+incompatible to 28.5.0+incompatible
- [#17816](https://github.com/influxdata/telegraf/pull/17816) `deps` Bump github.com/docker/docker from 28.5.0+incompatible to 28.5.1+incompatible
- [#17769](https://github.com/influxdata/telegraf/pull/17769) `deps` Bump github.com/go-ldap/ldap/v3 from 3.4.11 to 3.4.12
- [#17775](https://github.com/influxdata/telegraf/pull/17775) `deps` Bump github.com/go-logfmt/logfmt from 0.6.0 to 0.6.1
- [#17727](https://github.com/influxdata/telegraf/pull/17727) `deps` Bump github.com/hashicorp/consul/api from 1.32.3 to 1.32.4
- [#17862](https://github.com/influxdata/telegraf/pull/17862) `deps` Bump github.com/klauspost/compress from 1.18.0 to 1.18.1
- [#17773](https://github.com/influxdata/telegraf/pull/17773) `deps` Bump github.com/leodido/go-syslog/v4 from 4.2.1-0.20250421191238-de2e76af1251 to 4.3.0
- [#17729](https://github.com/influxdata/telegraf/pull/17729) `deps` Bump github.com/lxc/incus/v6 from 6.16.0 to 6.17.0
- [#17860](https://github.com/influxdata/telegraf/pull/17860) `deps` Bump github.com/nats-io/nats-server/v2 from 2.12.0 to 2.12.1
- [#17766](https://github.com/influxdata/telegraf/pull/17766) `deps` Bump github.com/nats-io/nats.go from 1.46.0 to 1.46.1
- [#17851](https://github.com/influxdata/telegraf/pull/17851) `deps` Bump github.com/nats-io/nats.go from 1.46.1 to 1.47.0
- [#17813](https://github.com/influxdata/telegraf/pull/17813) `deps` Bump github.com/prometheus/common from 0.66.1 to 0.67.1
- [#17867](https://github.com/influxdata/telegraf/pull/17867) `deps` Bump github.com/prometheus/prometheus from 0.306.0 to 0.307.1
- [#17861](https://github.com/influxdata/telegraf/pull/17861) `deps` Bump github.com/redis/go-redis/v9 from 9.14.0 to 9.14.1
- [#17767](https://github.com/influxdata/telegraf/pull/17767) `deps` Bump github.com/shirou/gopsutil/v4 from 4.25.8 to 4.25.9
- [#17725](https://github.com/influxdata/telegraf/pull/17725) `deps` Bump github.com/snowflakedb/gosnowflake from 0.0.0-20250911095445-20c4d105d9a0 to 1.17.0
- [#17776](https://github.com/influxdata/telegraf/pull/17776) `deps` Bump go.opentelemetry.io/collector/pdata from 1.42.0 to 1.43.0
- [#17817](https://github.com/influxdata/telegraf/pull/17817) `deps` Bump go.step.sm/crypto from 0.70.0 to 0.71.0
- [#17857](https://github.com/influxdata/telegraf/pull/17857) `deps` Bump go.step.sm/crypto from 0.71.0 to 0.72.0
- [#17820](https://github.com/influxdata/telegraf/pull/17820) `deps` Bump golang.org/x/crypto from 0.42.0 to 0.43.0
- [#17806](https://github.com/influxdata/telegraf/pull/17806) `deps` Bump golang.org/x/mod from 0.28.0 to 0.29.0
- [#17819](https://github.com/influxdata/telegraf/pull/17819) `deps` Bump golang.org/x/net from 0.44.0 to 0.46.0
- [#17818](https://github.com/influxdata/telegraf/pull/17818) `deps` Bump golang.org/x/oauth2 from 0.31.0 to 0.32.0
- [#17823](https://github.com/influxdata/telegraf/pull/17823) `deps` Bump golang.org/x/sys from 0.36.0 to 0.37.0
- [#17717](https://github.com/influxdata/telegraf/pull/17717) `deps` Bump google.golang.org/api from 0.249.0 to 0.250.0
- [#17778](https://github.com/influxdata/telegraf/pull/17778) `deps` Bump google.golang.org/api from 0.250.0 to 0.251.0
- [#17807](https://github.com/influxdata/telegraf/pull/17807) `deps` Bump google.golang.org/api from 0.251.0 to 0.252.0
- [#17771](https://github.com/influxdata/telegraf/pull/17771) `deps` Bump google.golang.org/grpc from 1.75.1 to 1.76.0
- [#17768](https://github.com/influxdata/telegraf/pull/17768) `deps` Bump google.golang.org/protobuf from 1.36.9 to 1.36.10
- [#17811](https://github.com/influxdata/telegraf/pull/17811) `deps` Bump modernc.org/sqlite from 1.39.0 to 1.39.1
- [#17779](https://github.com/influxdata/telegraf/pull/17779) `deps` Bump super-linter/super-linter from 8.1.0 to 8.2.0
- [#17853](https://github.com/influxdata/telegraf/pull/17853) `deps` Bump super-linter/super-linter from 8.2.0 to 8.2.1
- [#17610](https://github.com/influxdata/telegraf/pull/17610) `deps` Switch to maintained yaml library
- [#17794](https://github.com/influxdata/telegraf/pull/17794) `deps` Update golangci-lint to 2.5.0

## v1.36.2

### Bugfixes

- [#17609](https://github.com/influxdata/telegraf/pull/17609) `filter` Handle multiple conditions correctly
- [#17552](https://github.com/influxdata/telegraf/pull/17552) `inputs.procstat` Use correct values for disk\_read\_bytes, disk\_write\_bytes on Linux
- [#17613](https://github.com/influxdata/telegraf/pull/17613) `inputs.tail` Fix data race when cleaning up unused tailers

### Dependency Updates

- [#17599](https://github.com/influxdata/telegraf/pull/17599) `deps` Bump actions/setup-go from 5 to 6
- [#17650](https://github.com/influxdata/telegraf/pull/17650) `deps` Bump cloud.google.com/go/bigquery from 1.69.0 to 1.70.0
- [#17654](https://github.com/influxdata/telegraf/pull/17654) `deps` Bump cloud.google.com/go/storage from 1.56.1 to 1.56.2
- [#17688](https://github.com/influxdata/telegraf/pull/17688) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/azcore from 1.19.0 to 1.19.1
- [#17683](https://github.com/influxdata/telegraf/pull/17683) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/azidentity from 1.11.0 to 1.12.0
- [#17644](https://github.com/influxdata/telegraf/pull/17644) `deps` Bump github.com/ClickHouse/clickhouse-go/v2 from 2.40.1 to 2.40.3
- [#17522](https://github.com/influxdata/telegraf/pull/17522) `deps` Bump github.com/IBM/sarama from 1.45.2 to 1.46.0
- [#17682](https://github.com/influxdata/telegraf/pull/17682) `deps` Bump github.com/IBM/sarama from 1.46.0 to 1.46.1
- [#17636](https://github.com/influxdata/telegraf/pull/17636) `deps` Bump github.com/SAP/go-hdb from 1.14.0 to 1.14.3
- [#17677](https://github.com/influxdata/telegraf/pull/17677) `deps` Bump github.com/SAP/go-hdb from 1.14.3 to 1.14.4
- [#17647](https://github.com/influxdata/telegraf/pull/17647) `deps` Bump github.com/apache/arrow-go/v18 from 18.4.0 to 18.4.1
- [#17587](https://github.com/influxdata/telegraf/pull/17587) `deps` Bump github.com/apache/inlong/inlong-sdk/dataproxy-sdk-twins/dataproxy-sdk-golang from 1.0.5 to 1.0.6
- [#17642](https://github.com/influxdata/telegraf/pull/17642) `deps` Bump github.com/awnumar/memguard from 0.22.5 to 0.23.0
- [#17693](https://github.com/influxdata/telegraf/pull/17693) `deps` Bump github.com/aws/aws-sdk-go-v2/config from 1.31.4 to 1.31.9
- [#17588](https://github.com/influxdata/telegraf/pull/17588) `deps` Bump github.com/aws/aws-sdk-go-v2/feature/ec2/imds from 1.18.5 to 1.18.7
- [#17641](https://github.com/influxdata/telegraf/pull/17641) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatch from 1.48.2 to 1.50.1
- [#17656](https://github.com/influxdata/telegraf/pull/17656) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs from 1.57.0 to 1.57.4
- [#17690](https://github.com/influxdata/telegraf/pull/17690) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs from 1.57.4 to 1.58.0
- [#17596](https://github.com/influxdata/telegraf/pull/17596) `deps` Bump github.com/aws/aws-sdk-go-v2/service/dynamodb from 1.49.1 to 1.50.2
- [#17649](https://github.com/influxdata/telegraf/pull/17649) `deps` Bump github.com/aws/aws-sdk-go-v2/service/dynamodb from 1.50.2 to 1.50.3
- [#17583](https://github.com/influxdata/telegraf/pull/17583) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.246.0 to 1.251.1
- [#17640](https://github.com/influxdata/telegraf/pull/17640) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.251.1 to 1.251.2
- [#17681](https://github.com/influxdata/telegraf/pull/17681) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.251.2 to 1.253.0
- [#17595](https://github.com/influxdata/telegraf/pull/17595) `deps` Bump github.com/aws/aws-sdk-go-v2/service/kinesis from 1.39.1 to 1.40.2
- [#17646](https://github.com/influxdata/telegraf/pull/17646) `deps` Bump github.com/aws/aws-sdk-go-v2/service/kinesis from 1.40.2 to 1.40.3
- [#17638](https://github.com/influxdata/telegraf/pull/17638) `deps` Bump github.com/aws/aws-sdk-go-v2/service/sts from 1.38.1 to 1.38.4
- [#17582](https://github.com/influxdata/telegraf/pull/17582) `deps` Bump github.com/aws/aws-sdk-go-v2/service/timestreamwrite from 1.34.2 to 1.35.2
- [#17658](https://github.com/influxdata/telegraf/pull/17658) `deps` Bump github.com/aws/aws-sdk-go-v2/service/timestreamwrite from 1.35.2 to 1.35.3
- [#17673](https://github.com/influxdata/telegraf/pull/17673) `deps` Bump github.com/cloudevents/sdk-go/v2 from 2.16.1 to 2.16.2
- [#17601](https://github.com/influxdata/telegraf/pull/17601) `deps` Bump github.com/docker/docker from 28.3.3+incompatible to 28.4.0+incompatible
- [#17653](https://github.com/influxdata/telegraf/pull/17653) `deps` Bump github.com/eclipse/paho.golang from 0.22.0 to 0.23.0
- [#17680](https://github.com/influxdata/telegraf/pull/17680) `deps` Bump github.com/eclipse/paho.mqtt.golang from 1.5.0 to 1.5.1
- [#17597](https://github.com/influxdata/telegraf/pull/17597) `deps` Bump github.com/google/cel-go from 0.26.0 to 0.26.1
- [#17689](https://github.com/influxdata/telegraf/pull/17689) `deps` Bump github.com/hashicorp/consul/api from 1.32.1 to 1.32.3
- [#17651](https://github.com/influxdata/telegraf/pull/17651) `deps` Bump github.com/lxc/incus/v6 from 6.15.0 to 6.16.0
- [#17635](https://github.com/influxdata/telegraf/pull/17635) `deps` Bump github.com/nats-io/nats-server/v2 from 2.11.8 to 2.11.9
- [#17670](https://github.com/influxdata/telegraf/pull/17670) `deps` Bump github.com/nats-io/nats-server/v2 from 2.11.9 to 2.12.0
- [#17675](https://github.com/influxdata/telegraf/pull/17675) `deps` Bump github.com/nats-io/nats.go from 1.45.0 to 1.46.0
- [#17674](https://github.com/influxdata/telegraf/pull/17674) `deps` Bump github.com/peterbourgon/unixtransport from 0.0.6 to 0.0.7
- [#17593](https://github.com/influxdata/telegraf/pull/17593) `deps` Bump github.com/prometheus/client\_golang from 1.23.0 to 1.23.2
- [#17585](https://github.com/influxdata/telegraf/pull/17585) `deps` Bump github.com/prometheus/common from 0.65.0 to 0.66.1
- [#17685](https://github.com/influxdata/telegraf/pull/17685) `deps` Bump github.com/prometheus/prometheus from 0.305.0 to 0.306.0
- [#17329](https://github.com/influxdata/telegraf/pull/17329) `deps` Bump github.com/prometheus/prometheus from 0.54.1 to 0.305.0
- [#17645](https://github.com/influxdata/telegraf/pull/17645) `deps` Bump github.com/redis/go-redis/v9 from 9.12.1 to 9.14.0
- [#17567](https://github.com/influxdata/telegraf/pull/17567) `deps` Bump github.com/shirou/gopsutil/v4 from 4.25.7 to 4.25.8
- [#17699](https://github.com/influxdata/telegraf/pull/17699) `deps` Bump github.com/snowflakedb/gosnowflake from 1.16.0 to 0.0.0-20250911095445-20c4d105d9a0
- [#17590](https://github.com/influxdata/telegraf/pull/17590) `deps` Bump github.com/stretchr/testify from 1.10.0 to 1.11.1
- [#17687](https://github.com/influxdata/telegraf/pull/17687) `deps` Bump github.com/testcontainers/testcontainers-go from 0.38.0 to 0.39.0
- [#17676](https://github.com/influxdata/telegraf/pull/17676) `deps` Bump github.com/testcontainers/testcontainers-go/modules/azure from 0.38.0 to 0.39.0
- [#17671](https://github.com/influxdata/telegraf/pull/17671) `deps` Bump github.com/testcontainers/testcontainers-go/modules/kafka from 0.38.0 to 0.39.0
- [#17584](https://github.com/influxdata/telegraf/pull/17584) `deps` Bump github.com/tidwall/wal from 1.2.0 to 1.2.1
- [#17581](https://github.com/influxdata/telegraf/pull/17581) `deps` Bump github.com/tinylib/msgp from 1.3.0 to 1.4.0
- [#17591](https://github.com/influxdata/telegraf/pull/17591) `deps` Bump go.opentelemetry.io/collector/pdata from 1.39.0 to 1.41.0
- [#17686](https://github.com/influxdata/telegraf/pull/17686) `deps` Bump go.opentelemetry.io/collector/pdata from 1.41.0 to 1.42.0
- [#17602](https://github.com/influxdata/telegraf/pull/17602) `deps` Bump go.opentelemetry.io/proto/otlp from 1.7.0 to 1.8.0
- [#17652](https://github.com/influxdata/telegraf/pull/17652) `deps` Bump golang.org/x/crypto from 0.41.0 to 0.42.0
- [#17691](https://github.com/influxdata/telegraf/pull/17691) `deps` Bump golang.org/x/mod from 0.27.0 to 0.28.0
- [#17655](https://github.com/influxdata/telegraf/pull/17655) `deps` Bump golang.org/x/oauth2 from 0.30.0 to 0.31.0
- [#17589](https://github.com/influxdata/telegraf/pull/17589) `deps` Bump golang.org/x/sync from 0.16.0 to 0.17.0
- [#17580](https://github.com/influxdata/telegraf/pull/17580) `deps` Bump golang.org/x/term from 0.34.0 to 0.35.0
- [#17679](https://github.com/influxdata/telegraf/pull/17679) `deps` Bump google.golang.org/api from 0.248.0 to 0.249.0
- [#17639](https://github.com/influxdata/telegraf/pull/17639) `deps` Bump google.golang.org/grpc from 1.75.0 to 1.75.1
- [#17643](https://github.com/influxdata/telegraf/pull/17643) `deps` Bump google.golang.org/protobuf from 1.36.8 to 1.36.9
- [#17598](https://github.com/influxdata/telegraf/pull/17598) `deps` Bump k8s.io/api from 0.33.4 to 0.34.0
- [#17692](https://github.com/influxdata/telegraf/pull/17692) `deps` Bump k8s.io/client-go from 0.34.0 to 0.34.1
- [#17657](https://github.com/influxdata/telegraf/pull/17657) `deps` Bump modernc.org/sqlite from 1.38.2 to 1.39.0
- [#17648](https://github.com/influxdata/telegraf/pull/17648) `deps` Bump tj-actions/changed-files from 46.0.5 to 47.0.0
- [#17707](https://github.com/influxdata/telegraf/pull/17707) `deps` Remove collectd replacement

## v1.36.1

### Bugfixes

- [#17605](https://github.com/influxdata/telegraf/pull/17605) `outputs.influxdb` Fix crash on init

## v1.36.0

### Important Changes

- Pull request [#17355](https://github.com/influxdata/telegraf/pull/17355) updates `profiles` support in `inputs.opentelemetry` from v1 experimental to v1 development, following upstream changes to the experimental API. This update modifies metric output. For example, the `frame_type`, `stack_trace_id`, `build_id`, and `build_id_type` fields are no longer reported. The value format of other fields or tags might also have changed. For more information, see the [OpenTelemetry documentation](https://opentelemetry.io/docs/).

### New Plugins

- [#17368](https://github.com/influxdata/telegraf/pull/17368) `inputs.turbostat` Add plugin
- [#17078](https://github.com/influxdata/telegraf/pull/17078) `processors.round` Add plugin

### Features

- [#16705](https://github.com/influxdata/telegraf/pull/16705) `agent` Introduce labels and selectors to enable and disable plugins
- [#17547](https://github.com/influxdata/telegraf/pull/17547) `inputs.influxdb_v2_listener` Add `/health` route
- [#17312](https://github.com/influxdata/telegraf/pull/17312) `inputs.internal` Allow to collect statistics per plugin instance
- [#17024](https://github.com/influxdata/telegraf/pull/17024) `inputs.lvm` Add sync\_percent for lvm\_logical\_vol
- [#17355](https://github.com/influxdata/telegraf/pull/17355) `inputs.opentelemetry` Upgrade otlp proto module
- [#17156](https://github.com/influxdata/telegraf/pull/17156) `inputs.syslog` Add support for RFC3164 over TCP
- [#17543](https://github.com/influxdata/telegraf/pull/17543) `inputs.syslog` Allow limiting message size in octet counting mode
- [#17539](https://github.com/influxdata/telegraf/pull/17539) `inputs.x509_cert` Add support for Windows certificate stores
- [#17244](https://github.com/influxdata/telegraf/pull/17244) `output.nats` Allow disabling stream creation for externally managed streams
- [#17474](https://github.com/influxdata/telegraf/pull/17474) `outputs.elasticsearch` Support array headers and preserve commas in values
- [#17548](https://github.com/influxdata/telegraf/pull/17548) `outputs.influxdb` Add internal statistics for written bytes
- [#17213](https://github.com/influxdata/telegraf/pull/17213) `outputs.nats` Allow providing a subject layout
- [#17346](https://github.com/influxdata/telegraf/pull/17346) `outputs.nats` Enable batch serialization with use\_batch\_format
- [#17249](https://github.com/influxdata/telegraf/pull/17249) `outputs.sql` Allow sending batches of metrics in transactions
- [#17510](https://github.com/influxdata/telegraf/pull/17510) `parsers.avro` Support record arrays at root level
- [#17365](https://github.com/influxdata/telegraf/pull/17365) `plugins.snmp` Allow debug logging in gosnmp
- [#17345](https://github.com/influxdata/telegraf/pull/17345) `selfstat` Implement collection of plugin-internal statistics

### Bugfixes

- [#17411](https://github.com/influxdata/telegraf/pull/17411) `inputs.diskio` Handle counter wrapping in io fields
- [#17551](https://github.com/influxdata/telegraf/pull/17551) `inputs.s7comm` Use correct value for string length with ’extra’ parameter
- [#17579](https://github.com/influxdata/telegraf/pull/17579) `internal` Extract go version more robustly
- [#17566](https://github.com/influxdata/telegraf/pull/17566) `outputs` Retrigger batch-available-events only if at least one metric was written successfully
- [#17381](https://github.com/influxdata/telegraf/pull/17381) `packaging` Rename rpm from loong64 to loongarch64

### Dependency Updates

- [#17519](https://github.com/influxdata/telegraf/pull/17519) `deps` Bump cloud.google.com/go/storage from 1.56.0 to 1.56.1
- [#17532](https://github.com/influxdata/telegraf/pull/17532) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/azcore from 1.18.2 to 1.19.0
- [#17494](https://github.com/influxdata/telegraf/pull/17494) `deps` Bump github.com/SAP/go-hdb from 1.13.12 to 1.14.0
- [#17488](https://github.com/influxdata/telegraf/pull/17488) `deps` Bump github.com/antchfx/xpath from 1.3.4 to 1.3.5
- [#17540](https://github.com/influxdata/telegraf/pull/17540) `deps` Bump github.com/aws/aws-sdk-go-v2/config from 1.31.0 to 1.31.2
- [#17538](https://github.com/influxdata/telegraf/pull/17538) `deps` Bump github.com/aws/aws-sdk-go-v2/credentials from 1.18.4 to 1.18.6
- [#17517](https://github.com/influxdata/telegraf/pull/17517) `deps` Bump github.com/aws/aws-sdk-go-v2/feature/ec2/imds from 1.18.3 to 1.18.4
- [#17528](https://github.com/influxdata/telegraf/pull/17528) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatch from 1.48.0 to 1.48.2
- [#17536](https://github.com/influxdata/telegraf/pull/17536) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs from 1.56.0 to 1.57.0
- [#17524](https://github.com/influxdata/telegraf/pull/17524) `deps` Bump github.com/aws/aws-sdk-go-v2/service/dynamodb from 1.46.0 to 1.49.1
- [#17493](https://github.com/influxdata/telegraf/pull/17493) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.242.0 to 1.244.0
- [#17527](https://github.com/influxdata/telegraf/pull/17527) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.244.0 to 1.246.0
- [#17530](https://github.com/influxdata/telegraf/pull/17530) `deps` Bump github.com/aws/aws-sdk-go-v2/service/kinesis from 1.38.0 to 1.39.1
- [#17534](https://github.com/influxdata/telegraf/pull/17534) `deps` Bump github.com/aws/aws-sdk-go-v2/service/sts from 1.37.0 to 1.38.0
- [#17513](https://github.com/influxdata/telegraf/pull/17513) `deps` Bump github.com/aws/aws-sdk-go-v2/service/timestreamwrite from 1.34.0 to 1.34.2
- [#17514](https://github.com/influxdata/telegraf/pull/17514) `deps` Bump github.com/coreos/go-systemd/v22 from 22.5.0 to 22.6.0
- [#17563](https://github.com/influxdata/telegraf/pull/17563) `deps` Bump github.com/facebook/time from 0.0.0-20240626113945-18207c5d8ddc to 0.0.0-20250903103710-a5911c32cdb9
- [#17526](https://github.com/influxdata/telegraf/pull/17526) `deps` Bump github.com/gophercloud/gophercloud/v2 from 2.7.0 to 2.8.0
- [#17537](https://github.com/influxdata/telegraf/pull/17537) `deps` Bump github.com/microsoft/go-mssqldb from 1.9.2 to 1.9.3
- [#17490](https://github.com/influxdata/telegraf/pull/17490) `deps` Bump github.com/nats-io/nats-server/v2 from 2.11.7 to 2.11.8
- [#17523](https://github.com/influxdata/telegraf/pull/17523) `deps` Bump github.com/nats-io/nats.go from 1.44.0 to 1.45.0
- [#17492](https://github.com/influxdata/telegraf/pull/17492) `deps` Bump github.com/safchain/ethtool from 0.5.10 to 0.6.2
- [#17486](https://github.com/influxdata/telegraf/pull/17486) `deps` Bump github.com/snowflakedb/gosnowflake from 1.15.0 to 1.16.0
- [#17541](https://github.com/influxdata/telegraf/pull/17541) `deps` Bump github.com/tidwall/wal from 1.1.8 to 1.2.0
- [#17529](https://github.com/influxdata/telegraf/pull/17529) `deps` Bump github.com/vmware/govmomi from 0.51.0 to 0.52.0
- [#17496](https://github.com/influxdata/telegraf/pull/17496) `deps` Bump go.opentelemetry.io/collector/pdata from 1.36.1 to 1.38.0
- [#17533](https://github.com/influxdata/telegraf/pull/17533) `deps` Bump go.opentelemetry.io/collector/pdata from 1.38.0 to 1.39.0
- [#17516](https://github.com/influxdata/telegraf/pull/17516) `deps` Bump go.step.sm/crypto from 0.69.0 to 0.70.0
- [#17499](https://github.com/influxdata/telegraf/pull/17499) `deps` Bump golang.org/x/mod from 0.26.0 to 0.27.0
- [#17497](https://github.com/influxdata/telegraf/pull/17497) `deps` Bump golang.org/x/net from 0.42.0 to 0.43.0
- [#17487](https://github.com/influxdata/telegraf/pull/17487) `deps` Bump google.golang.org/api from 0.246.0 to 0.247.0
- [#17531](https://github.com/influxdata/telegraf/pull/17531) `deps` Bump google.golang.org/api from 0.247.0 to 0.248.0
- [#17520](https://github.com/influxdata/telegraf/pull/17520) `deps` Bump google.golang.org/grpc from 1.74.2 to 1.75.0
- [#17518](https://github.com/influxdata/telegraf/pull/17518) `deps` Bump google.golang.org/protobuf from 1.36.7 to 1.36.8
- [#17498](https://github.com/influxdata/telegraf/pull/17498) `deps` Bump k8s.io/client-go from 0.33.3 to 0.33.4
- [#17515](https://github.com/influxdata/telegraf/pull/17515) `deps` Bump super-linter/super-linter from 8.0.0 to 8.1.0

## v1.35.4

### Bugfixes

- [#17451](https://github.com/influxdata/telegraf/pull/17451) `agent` Update help message for `--test` CLI flag
- [#17413](https://github.com/influxdata/telegraf/pull/17413) `inputs.gnmi` Handle empty updates in gnmi notification response
- [#17445](https://github.com/influxdata/telegraf/pull/17445) `inputs.redfish` Log correct address on HTTP error

### Dependency Updates

- [#17454](https://github.com/influxdata/telegraf/pull/17454) `deps` Bump actions/checkout from 4 to 5
- [#17404](https://github.com/influxdata/telegraf/pull/17404) `deps` Bump cloud.google.com/go/storage from 1.55.0 to 1.56.0
- [#17428](https://github.com/influxdata/telegraf/pull/17428) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/azcore from 1.18.1 to 1.18.2
- [#17455](https://github.com/influxdata/telegraf/pull/17455) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/azidentity from 1.10.1 to 1.11.0
- [#17383](https://github.com/influxdata/telegraf/pull/17383) `deps` Bump github.com/ClickHouse/clickhouse-go/v2 from 2.37.2 to 2.39.0
- [#17435](https://github.com/influxdata/telegraf/pull/17435) `deps` Bump github.com/ClickHouse/clickhouse-go/v2 from 2.39.0 to 2.40.1
- [#17393](https://github.com/influxdata/telegraf/pull/17393) `deps` Bump github.com/apache/arrow-go/v18 from 18.3.1 to 18.4.0
- [#17439](https://github.com/influxdata/telegraf/pull/17439) `deps` Bump github.com/apache/inlong/inlong-sdk/dataproxy-sdk-twins/dataproxy-sdk-golang from 1.0.3 to 1.0.5
- [#17437](https://github.com/influxdata/telegraf/pull/17437) `deps` Bump github.com/aws/aws-sdk-go-v2 from 1.37.0 to 1.37.2
- [#17402](https://github.com/influxdata/telegraf/pull/17402) `deps` Bump github.com/aws/aws-sdk-go-v2/config from 1.29.17 to 1.30.0
- [#17458](https://github.com/influxdata/telegraf/pull/17458) `deps` Bump github.com/aws/aws-sdk-go-v2/config from 1.30.1 to 1.31.0
- [#17391](https://github.com/influxdata/telegraf/pull/17391) `deps` Bump github.com/aws/aws-sdk-go-v2/credentials from 1.17.70 to 1.18.0
- [#17436](https://github.com/influxdata/telegraf/pull/17436) `deps` Bump github.com/aws/aws-sdk-go-v2/credentials from 1.18.1 to 1.18.3
- [#17434](https://github.com/influxdata/telegraf/pull/17434) `deps` Bump github.com/aws/aws-sdk-go-v2/feature/ec2/imds from 1.18.0 to 1.18.2
- [#17461](https://github.com/influxdata/telegraf/pull/17461) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatch from 1.45.3 to 1.48.0
- [#17392](https://github.com/influxdata/telegraf/pull/17392) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs from 1.51.0 to 1.54.0
- [#17440](https://github.com/influxdata/telegraf/pull/17440) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs from 1.54.0 to 1.55.0
- [#17473](https://github.com/influxdata/telegraf/pull/17473) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs from 1.55.0 to 1.56.0
- [#17431](https://github.com/influxdata/telegraf/pull/17431) `deps` Bump github.com/aws/aws-sdk-go-v2/service/dynamodb from 1.44.0 to 1.46.0
- [#17470](https://github.com/influxdata/telegraf/pull/17470) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.231.0 to 1.242.0
- [#17397](https://github.com/influxdata/telegraf/pull/17397) `deps` Bump github.com/aws/aws-sdk-go-v2/service/kinesis from 1.35.3 to 1.36.0
- [#17430](https://github.com/influxdata/telegraf/pull/17430) `deps` Bump github.com/aws/aws-sdk-go-v2/service/kinesis from 1.36.0 to 1.37.0
- [#17469](https://github.com/influxdata/telegraf/pull/17469) `deps` Bump github.com/aws/aws-sdk-go-v2/service/kinesis from 1.37.0 to 1.38.0
- [#17432](https://github.com/influxdata/telegraf/pull/17432) `deps` Bump github.com/aws/aws-sdk-go-v2/service/sts from 1.35.0 to 1.36.0
- [#17401](https://github.com/influxdata/telegraf/pull/17401) `deps` Bump github.com/aws/aws-sdk-go-v2/service/timestreamwrite from 1.31.2 to 1.32.0
- [#17421](https://github.com/influxdata/telegraf/pull/17421) `deps` Bump github.com/aws/aws-sdk-go-v2/service/timestreamwrite from 1.32.0 to 1.33.0
- [#17464](https://github.com/influxdata/telegraf/pull/17464) `deps` Bump github.com/aws/aws-sdk-go-v2/service/timestreamwrite from 1.33.0 to 1.34.0
- [#17457](https://github.com/influxdata/telegraf/pull/17457) `deps` Bump github.com/clarify/clarify-go from 0.4.0 to 0.4.1
- [#17407](https://github.com/influxdata/telegraf/pull/17407) `deps` Bump github.com/docker/docker from 28.3.2+incompatible to 28.3.3+incompatible
- [#17463](https://github.com/influxdata/telegraf/pull/17463) `deps` Bump github.com/docker/go-connections from 0.5.0 to 0.6.0
- [#17394](https://github.com/influxdata/telegraf/pull/17394) `deps` Bump github.com/golang-jwt/jwt/v5 from 5.2.2 to 5.2.3
- [#17423](https://github.com/influxdata/telegraf/pull/17423) `deps` Bump github.com/gopacket/gopacket from 1.3.1 to 1.4.0
- [#17399](https://github.com/influxdata/telegraf/pull/17399) `deps` Bump github.com/jedib0t/go-pretty/v6 from 6.6.7 to 6.6.8
- [#17422](https://github.com/influxdata/telegraf/pull/17422) `deps` Bump github.com/lxc/incus/v6 from 6.14.0 to 6.15.0
- [#17429](https://github.com/influxdata/telegraf/pull/17429) `deps` Bump github.com/miekg/dns from 1.1.67 to 1.1.68
- [#17433](https://github.com/influxdata/telegraf/pull/17433) `deps` Bump github.com/nats-io/nats-server/v2 from 2.11.6 to 2.11.7
- [#17426](https://github.com/influxdata/telegraf/pull/17426) `deps` Bump github.com/nats-io/nats.go from 1.43.0 to 1.44.0
- [#17456](https://github.com/influxdata/telegraf/pull/17456) `deps` Bump github.com/redis/go-redis/v9 from 9.11.0 to 9.12.1
- [#17420](https://github.com/influxdata/telegraf/pull/17420) `deps` Bump github.com/shirou/gopsutil/v4 from 4.25.6 to 4.25.7
- [#17388](https://github.com/influxdata/telegraf/pull/17388) `deps` Bump github.com/testcontainers/testcontainers-go/modules/azure from 0.37.0 to 0.38.0
- [#17382](https://github.com/influxdata/telegraf/pull/17382) `deps` Bump github.com/testcontainers/testcontainers-go/modules/kafka from 0.37.0 to 0.38.0
- [#17427](https://github.com/influxdata/telegraf/pull/17427) `deps` Bump github.com/yuin/goldmark from 1.7.12 to 1.7.13
- [#17386](https://github.com/influxdata/telegraf/pull/17386) `deps` Bump go.opentelemetry.io/collector/pdata from 1.36.0 to 1.36.1
- [#17425](https://github.com/influxdata/telegraf/pull/17425) `deps` Bump go.step.sm/crypto from 0.67.0 to 0.68.0
- [#17462](https://github.com/influxdata/telegraf/pull/17462) `deps` Bump go.step.sm/crypto from 0.68.0 to 0.69.0
- [#17460](https://github.com/influxdata/telegraf/pull/17460) `deps` Bump golang.org/x/crypto from 0.40.0 to 0.41.0
- [#17424](https://github.com/influxdata/telegraf/pull/17424) `deps` Bump google.golang.org/api from 0.243.0 to 0.244.0
- [#17459](https://github.com/influxdata/telegraf/pull/17459) `deps` Bump google.golang.org/api from 0.244.0 to 0.246.0
- [#17465](https://github.com/influxdata/telegraf/pull/17465) `deps` Bump google.golang.org/protobuf from 1.36.6 to 1.36.7
- [#17384](https://github.com/influxdata/telegraf/pull/17384) `deps` Bump k8s.io/apimachinery from 0.33.2 to 0.33.3
- [#17389](https://github.com/influxdata/telegraf/pull/17389) `deps` Bump k8s.io/client-go from 0.33.2 to 0.33.3
- [#17396](https://github.com/influxdata/telegraf/pull/17396) `deps` Bump modernc.org/sqlite from 1.38.0 to 1.38.1
- [#17385](https://github.com/influxdata/telegraf/pull/17385) `deps` Bump software.sslmate.com/src/go-pkcs12 from 0.5.0 to 0.6.0
- [#17390](https://github.com/influxdata/telegraf/pull/17390) `deps` Bump super-linter/super-linter from 7.4.0 to 8.0.0
- [#17448](https://github.com/influxdata/telegraf/pull/17448) `deps` Fix collectd dependency not resolving
- [#17410](https://github.com/influxdata/telegraf/pull/17410) `deps` Migrate from cloud.google.com/go/pubsub to v2

## v1.35.3

### Bug fixes

- [#17373](https://github.com/influxdata/telegraf/pull/17373) `agent` Handle nil timer on telegraf reload when no debounce is specified
- [#17340](https://github.com/influxdata/telegraf/pull/17340) `agent` Make Windows service install more robust
- [#17310](https://github.com/influxdata/telegraf/pull/17310) `outputs.sql` Add timestamp to derived datatypes
- [#17349](https://github.com/influxdata/telegraf/pull/17349) `outputs` Retrigger batch-available-events only for non-failing writes
- [#17293](https://github.com/influxdata/telegraf/pull/17293) `parsers.json_v2` Respect string type for objects and arrays
- [#17367](https://github.com/influxdata/telegraf/pull/17367) `plugins.snmp` Update gosnmp to prevent panic in snmp agents
- [#17292](https://github.com/influxdata/telegraf/pull/17292) `processors.snmp_lookup` Avoid re-enqueing updates after plugin stopped
- [#17369](https://github.com/influxdata/telegraf/pull/17369) `processors.snmp_lookup` Prevent deadlock during plugin shutdown

### Dependency updates

- [#17320](https://github.com/influxdata/telegraf/pull/17320) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/azcore from 1.18.0 to 1.18.1
- [#17328](https://github.com/influxdata/telegraf/pull/17328) `deps` Bump github.com/SAP/go-hdb from 1.13.11 to 1.13.12
- [#17301](https://github.com/influxdata/telegraf/pull/17301) `deps` Bump github.com/SAP/go-hdb from 1.13.9 to 1.13.11
- [#17326](https://github.com/influxdata/telegraf/pull/17326) `deps` Bump github.com/alitto/pond/v2 from 2.4.0 to 2.5.0
- [#17295](https://github.com/influxdata/telegraf/pull/17295) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.227.0 to 1.230.0
- [#17332](https://github.com/influxdata/telegraf/pull/17332) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.230.0 to 1.231.0
- [#17300](https://github.com/influxdata/telegraf/pull/17300) `deps` Bump github.com/docker/docker from 28.3.0+incompatible to 28.3.1+incompatible
- [#17334](https://github.com/influxdata/telegraf/pull/17334) `deps` Bump github.com/docker/docker from 28.3.1+incompatible to 28.3.2+incompatible
- [#17327](https://github.com/influxdata/telegraf/pull/17327) `deps` Bump github.com/google/cel-go from 0.25.0 to 0.26.0
- [#17331](https://github.com/influxdata/telegraf/pull/17331) `deps` Bump github.com/miekg/dns from 1.1.66 to 1.1.67
- [#17297](https://github.com/influxdata/telegraf/pull/17297) `deps` Bump github.com/nats-io/nats-server/v2 from 2.11.5 to 2.11.6
- [#17321](https://github.com/influxdata/telegraf/pull/17321) `deps` Bump github.com/openconfig/goyang from 1.6.2 to 1.6.3
- [#17298](https://github.com/influxdata/telegraf/pull/17298) `deps` Bump github.com/prometheus/procfs from 0.16.1 to 0.17.0
- [#17296](https://github.com/influxdata/telegraf/pull/17296) `deps` Bump github.com/shirou/gopsutil/v4 from 4.25.5 to 4.25.6
- [#17299](https://github.com/influxdata/telegraf/pull/17299) `deps` Bump github.com/snowflakedb/gosnowflake from 1.14.1 to 1.15.0
- [#17323](https://github.com/influxdata/telegraf/pull/17323) `deps` Bump go.opentelemetry.io/collector/pdata from 1.35.0 to 1.36.0
- [#17091](https://github.com/influxdata/telegraf/pull/17091) `deps` Bump go.step.sm/crypto from 0.64.0 to 0.67.0
- [#17330](https://github.com/influxdata/telegraf/pull/17330) `deps` Bump golang.org/x/crypto from 0.39.0 to 0.40.0
- [#17322](https://github.com/influxdata/telegraf/pull/17322) `deps` Bump golang.org/x/mod from 0.25.0 to 0.26.0
- [#17336](https://github.com/influxdata/telegraf/pull/17336) `deps` Bump golang.org/x/net from 0.41.0 to 0.42.0
- [#17337](https://github.com/influxdata/telegraf/pull/17337) `deps` Bump golang.org/x/sys from 0.33.0 to 0.34.0
- [#17335](https://github.com/influxdata/telegraf/pull/17335) `deps` Bump golang.org/x/term from 0.32.0 to 0.33.0
- [#17294](https://github.com/influxdata/telegraf/pull/17294) `deps` Bump google.golang.org/api from 0.239.0 to 0.240.0
- [#17325](https://github.com/influxdata/telegraf/pull/17325) `deps` Bump google.golang.org/api from 0.240.0 to 0.241.0
- [#17138](https://github.com/influxdata/telegraf/pull/17138) `deps` Bump modernc.org/sqlite from 1.37.0 to 1.38.0

## v1.35.2

### Bug fixes

- [#17248](https://github.com/influxdata/telegraf/pull/17248) `agent` Add missing config flags for migrate command
- [#17240](https://github.com/influxdata/telegraf/pull/17240) `disk-buffer` Correctly reset the mask after adding to an empty buffer
- [#17284](https://github.com/influxdata/telegraf/pull/17284) `disk-buffer` Expire metric tracking information in the right place
- [#17257](https://github.com/influxdata/telegraf/pull/17257) `disk-buffer` Mask old tracking metrics on restart
- [#17247](https://github.com/influxdata/telegraf/pull/17247) `disk-buffer` Remove empty buffer on close
- [#17285](https://github.com/influxdata/telegraf/pull/17285) `inputs.gnmi` Avoid interpreting path elements with multiple colons as namespace
- [#17278](https://github.com/influxdata/telegraf/pull/17278) `inputs.gnmi` Handle base64 encoded IEEE-754 floats correctly
- [#17258](https://github.com/influxdata/telegraf/pull/17258) `inputs.kibana` Support Kibana 8.x status API format change
- [#17214](https://github.com/influxdata/telegraf/pull/17214) `inputs.ntpq` Fix ntpq field misalignment parsing errors
- [#17234](https://github.com/influxdata/telegraf/pull/17234) `outputs.microsoft_fabric` Correct app name
- [#17291](https://github.com/influxdata/telegraf/pull/17291) `outputs.nats` Avoid initializing Jetstream unconditionally
- [#17246](https://github.com/influxdata/telegraf/pull/17246) `outputs` Retrigger batch-available-events correctly

### Dependency updates

- [#17217](https://github.com/influxdata/telegraf/pull/17217) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/messaging/azeventhubs from 1.3.2 to 1.4.0
- [#17226](https://github.com/influxdata/telegraf/pull/17226) `deps` Bump github.com/ClickHouse/clickhouse-go/v2 from 2.37.0 to 2.37.1
- [#17265](https://github.com/influxdata/telegraf/pull/17265) `deps` Bump github.com/ClickHouse/clickhouse-go/v2 from 2.37.1 to 2.37.2
- [#17268](https://github.com/influxdata/telegraf/pull/17268) `deps` Bump github.com/Masterminds/semver/v3 from 3.3.1 to 3.4.0
- [#17271](https://github.com/influxdata/telegraf/pull/17271) `deps` Bump github.com/SAP/go-hdb from 1.13.7 to 1.13.9
- [#17232](https://github.com/influxdata/telegraf/pull/17232) `deps` Bump github.com/alitto/pond/v2 from 2.3.4 to 2.4.0
- [#17231](https://github.com/influxdata/telegraf/pull/17231) `deps` Bump github.com/apache/arrow-go/v18 from 18.3.0 to 18.3.1
- [#17223](https://github.com/influxdata/telegraf/pull/17223) `deps` Bump github.com/aws/aws-sdk-go-v2/config from 1.29.15 to 1.29.17
- [#17220](https://github.com/influxdata/telegraf/pull/17220) `deps` Bump github.com/aws/aws-sdk-go-v2/credentials from 1.17.69 to 1.17.70
- [#17227](https://github.com/influxdata/telegraf/pull/17227) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs from 1.50.3 to 1.51.0
- [#17262](https://github.com/influxdata/telegraf/pull/17262) `deps` Bump github.com/aws/aws-sdk-go-v2/service/dynamodb from 1.43.4 to 1.44.0
- [#17224](https://github.com/influxdata/telegraf/pull/17224) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.225.1 to 1.225.2
- [#17260](https://github.com/influxdata/telegraf/pull/17260) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.226.0 to 1.227.0
- [#17264](https://github.com/influxdata/telegraf/pull/17264) `deps` Bump github.com/docker/docker from 28.2.2+incompatible to 28.3.0+incompatible
- [#17256](https://github.com/influxdata/telegraf/pull/17256) `deps` Bump github.com/lxc/incus/v6 from 6.13.0 to 6.14.0
- [#17272](https://github.com/influxdata/telegraf/pull/17272) `deps` Bump github.com/microsoft/go-mssqldb from 1.8.2 to 1.9.2
- [#17261](https://github.com/influxdata/telegraf/pull/17261) `deps` Bump github.com/nats-io/nats-server/v2 from 2.11.4 to 2.11.5
- [#17266](https://github.com/influxdata/telegraf/pull/17266) `deps` Bump github.com/peterbourgon/unixtransport from 0.0.5 to 0.0.6
- [#17229](https://github.com/influxdata/telegraf/pull/17229) `deps` Bump github.com/prometheus/common from 0.64.0 to 0.65.0
- [#17267](https://github.com/influxdata/telegraf/pull/17267) `deps` Bump github.com/redis/go-redis/v9 from 9.10.0 to 9.11.0
- [#17273](https://github.com/influxdata/telegraf/pull/17273) `deps` Bump go.opentelemetry.io/collector/pdata from 1.34.0 to 1.35.0
- [#17219](https://github.com/influxdata/telegraf/pull/17219) `deps` Bump google.golang.org/api from 0.237.0 to 0.238.0
- [#17263](https://github.com/influxdata/telegraf/pull/17263) `deps` Bump google.golang.org/api from 0.238.0 to 0.239.0
- [#17218](https://github.com/influxdata/telegraf/pull/17218) `deps` Bump k8s.io/api from 0.33.1 to 0.33.2
- [#17228](https://github.com/influxdata/telegraf/pull/17228) `deps` Bump k8s.io/client-go from 0.33.1 to 0.33.2

## v1.35.1

### Bug fixes

- [#17178](https://github.com/influxdata/telegraf/pull/17178) `inputs.procstat` Fix user filter conditional logic
- [#17210](https://github.com/influxdata/telegraf/pull/17210) `processors.strings` Add explicit TOML tags on struct fields

### Dependency updates

- [#17194](https://github.com/influxdata/telegraf/pull/17194) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/azidentity from 1.10.0 to 1.10.1
- [#17189](https://github.com/influxdata/telegraf/pull/17189) `deps` Bump github.com/ClickHouse/clickhouse-go/v2 from 2.36.0 to 2.37.0
- [#17186](https://github.com/influxdata/telegraf/pull/17186) `deps` Bump github.com/SAP/go-hdb from 1.13.6 to 1.13.7
- [#17188](https://github.com/influxdata/telegraf/pull/17188) `deps` Bump github.com/alitto/pond/v2 from 2.3.2 to 2.3.4
- [#17180](https://github.com/influxdata/telegraf/pull/17180) `deps` Bump github.com/aws/aws-sdk-go-v2/credentials from 1.17.68 to 1.17.69
- [#17185](https://github.com/influxdata/telegraf/pull/17185) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatch from 1.45.1 to 1.45.2
- [#17187](https://github.com/influxdata/telegraf/pull/17187) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs from 1.50.1 to 1.50.2
- [#17183](https://github.com/influxdata/telegraf/pull/17183) `deps` Bump github.com/aws/aws-sdk-go-v2/service/dynamodb from 1.43.2 to 1.43.3
- [#17182](https://github.com/influxdata/telegraf/pull/17182) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.225.0 to 1.225.1
- [#17190](https://github.com/influxdata/telegraf/pull/17190) `deps` Bump github.com/aws/aws-sdk-go-v2/service/kinesis from 1.35.1 to 1.35.2
- [#17193](https://github.com/influxdata/telegraf/pull/17193) `deps` Bump github.com/aws/aws-sdk-go-v2/service/timestreamwrite from 1.31.0 to 1.31.1
- [#17195](https://github.com/influxdata/telegraf/pull/17195) `deps` Bump github.com/aws/smithy-go from 1.22.3 to 1.22.4
- [#17196](https://github.com/influxdata/telegraf/pull/17196) `deps` Bump github.com/cloudevents/sdk-go/v2 from 2.16.0 to 2.16.1
- [#17212](https://github.com/influxdata/telegraf/pull/17212) `deps` Bump github.com/go-chi/chi/v5 from 5.2.1 to 5.2.2
- [#17191](https://github.com/influxdata/telegraf/pull/17191) `deps` Bump github.com/go-sql-driver/mysql from 1.9.2 to 1.9.3
- [#17192](https://github.com/influxdata/telegraf/pull/17192) `deps` Bump github.com/peterbourgon/unixtransport from 0.0.4 to 0.0.5
- [#17181](https://github.com/influxdata/telegraf/pull/17181) `deps` Bump github.com/redis/go-redis/v9 from 9.9.0 to 9.10.0
- [#17197](https://github.com/influxdata/telegraf/pull/17197) `deps` Bump github.com/urfave/cli/v2 from 2.27.6 to 2.27.7
- [#17198](https://github.com/influxdata/telegraf/pull/17198) `deps` Bump go.opentelemetry.io/collector/pdata from 1.33.0 to 1.34.0
- [#17184](https://github.com/influxdata/telegraf/pull/17184) `deps` Bump google.golang.org/api from 0.236.0 to 0.237.0

## v1.35.0

### Deprecation Removals

This release removes the following deprecated plugin aliases:

- `inputs.cisco_telemetry_gnmi` in [#17101](https://github.com/influxdata/telegraf/pull/17101)
- `inputs.http_listener` in [#17102](https://github.com/influxdata/telegraf/pull/17102)
- `inputs.KNXListener` in [#17168](https://github.com/influxdata/telegraf/pull/17168)
- `inputs.logparser` in [#17170](https://github.com/influxdata/telegraf/pull/17170)

And removes the following deprecated plugin options:

- `ssl_ca`, `ssl_cert` and `ssl_key` of common TLS settings in [#17119](https://github.com/influxdata/telegraf/pull/17119)
- `url` of `inputs.amqp_consumer` in [#17149](https://github.com/influxdata/telegraf/pull/17149)
- `namespace` of `inputs.cloudwatch` in [#17123](https://github.com/influxdata/telegraf/pull/17123)
- `datacentre` of `inputs.consul` in [#17150](https://github.com/influxdata/telegraf/pull/17150)
- `container_names`, `perdevice` and `total` of `inputs.docker` in [#17148](https://github.com/influxdata/telegraf/pull/17148)
- `http_timeout` of `inputs.elasticsearch` in [#17124](https://github.com/influxdata/telegraf/pull/17124)
- `directory` of `inputs.filecount` in [#17152](https://github.com/influxdata/telegraf/pull/17152)
- `guess_path_tag` and `enable_tls` of `inputs.gnmi` in [#17151](https://github.com/influxdata/telegraf/pull/17151)
- `bearer_token` of `inputs.http` in [#17153](https://github.com/influxdata/telegraf/pull/17153)
- `path` and `port` of `inputs.http_listener_v2` in [#17158](https://github.com/influxdata/telegraf/pull/17158)
- `address` of `inputs.http_response` in [#17157](https://github.com/influxdata/telegraf/pull/17157)
- `object_type` of `inputs.icinga2` in [#17163](https://github.com/influxdata/telegraf/pull/17163)
- `max_line_size` of `inputs.influxdb_listener` in [#17162](https://github.com/influxdata/telegraf/pull/17162)
- `enable_file_download` of `inputs.internet_speed` in [#17165](https://github.com/influxdata/telegraf/pull/17165)
- `bearer_token_string` of `inputs.kube_inventory` in [#17110](https://github.com/influxdata/telegraf/pull/17110)
- `bearer_token_string` of `inputs.kubernetes` in [#17109](https://github.com/influxdata/telegraf/pull/17109)
- `server` of `inputs.nsq_consumer` in [#17166](https://github.com/influxdata/telegraf/pull/17166)
- `dns_lookup` of `inputs.ntpq` in [#17159](https://github.com/influxdata/telegraf/pull/17159)
- `ssl` of `inputs.openldap` in [#17103](https://github.com/influxdata/telegraf/pull/17103)
- `name` and `queues` of `inputs.rabbitmq` in [#17105](https://github.com/influxdata/telegraf/pull/17105)
- `path` of `inputs.smart` in [#17113](https://github.com/influxdata/telegraf/pull/17113)
- `azuredb` and `query_version` of `inputs.sqlserver` in [#17112](https://github.com/influxdata/telegraf/pull/17112)
- `parse_data_dog_tags` and `udp_packet_size` of `inputs.statsd` in [#17171](https://github.com/influxdata/telegraf/pull/17171)
- `force_discover_on_init` of `inputs.vsphere` in [#17169](https://github.com/influxdata/telegraf/pull/17169)
- `database`, `precision`, `retention_policy` and `url` of `outputs.amqp` in [#16950](https://github.com/influxdata/telegraf/pull/16950)
- `precision` of `outputs.influxdb` in [#17160](https://github.com/influxdata/telegraf/pull/17160)
- `partitionkey` and `use_random_partitionkey` of `outputs.kinesis` in [#17167](https://github.com/influxdata/telegraf/pull/17167)
- `source_tag` of `outputs.librato` in [#17174](https://github.com/influxdata/telegraf/pull/17174)
- `batch` and `topic_prefix` of `outputs.mqtt` in [#17176](https://github.com/influxdata/telegraf/pull/17176)
- `trace` of `outputs.remotefile` in [#17173](https://github.com/influxdata/telegraf/pull/17173)
- `host`, `port` and `string_to_number` of `outputs.wavefront` in [#17172](https://github.com/influxdata/telegraf/pull/17172)

If you’re using deprecated Telegraf plugins or options, migrate your configuration to use the available replacements. The `telegraf config migrate` command might be able to help with the migration.

### New Plugins

- [#16390](https://github.com/influxdata/telegraf/pull/16390) `inputs.fritzbox` Add plugin
- [#16780](https://github.com/influxdata/telegraf/pull/16780) `inputs.mavlink` Add plugin
- [#16509](https://github.com/influxdata/telegraf/pull/16509) `inputs.whois` Add plugin
- [#16211](https://github.com/influxdata/telegraf/pull/16211) `outputs.inlong` Add plugin
- [#16827](https://github.com/influxdata/telegraf/pull/16827) `outputs.microsoft_fabric` Add plugin
- [#16629](https://github.com/influxdata/telegraf/pull/16629) `processors.cumulative_sum` Add plugin

### Features

- [#17048](https://github.com/influxdata/telegraf/pull/17048) `agent` Add debounce for watch events
- [#16524](https://github.com/influxdata/telegraf/pull/16524) `common.kafka` Add AWS-MSK-IAM SASL authentication
- [#16867](https://github.com/influxdata/telegraf/pull/16867) `common.ratelimiter` Implement means to reserve memory for concurrent use
- [#16148](https://github.com/influxdata/telegraf/pull/16148) `common.shim` Add batch to shim
- [#17121](https://github.com/influxdata/telegraf/pull/17121) `inputs.amqp_consumer` Allow string values in queue arguments
- [#17051](https://github.com/influxdata/telegraf/pull/17051) `inputs.opcua` Allow forcing reconnection on every gather cycle
- [#16532](https://github.com/influxdata/telegraf/pull/16532) `inputs.opcua_listener` Allow to subscribe to OPCUA events
- [#16882](https://github.com/influxdata/telegraf/pull/16882) `inputs.prometheus` Add HTTP service discovery support
- [#16999](https://github.com/influxdata/telegraf/pull/16999) `inputs.s7comm` Add support for LREAL and LINT data types
- [#16452](https://github.com/influxdata/telegraf/pull/16452) `inputs.unbound` Collect histogram statistics
- [#16700](https://github.com/influxdata/telegraf/pull/16700) `inputs.whois` Support IDN domains
- [#17119](https://github.com/influxdata/telegraf/pull/17119) `migrations` Add migration for common.tls ssl options
- [#17101](https://github.com/influxdata/telegraf/pull/17101) `migrations` Add migration for inputs.cisco\_telemetry\_gnmi
- [#17123](https://github.com/influxdata/telegraf/pull/17123) `migrations` Add migration for inputs.cloudwatch
- [#17148](https://github.com/influxdata/telegraf/pull/17148) `migrations` Add migration for inputs.docker
- [#17124](https://github.com/influxdata/telegraf/pull/17124) `migrations` Add migration for inputs.elasticsearch
- [#17102](https://github.com/influxdata/telegraf/pull/17102) `migrations` Add migration for inputs.http\_listener
- [#17162](https://github.com/influxdata/telegraf/pull/17162) `migrations` Add migration for inputs.influxdb\_listener
- [#17110](https://github.com/influxdata/telegraf/pull/17110) `migrations` Add migration for inputs.kube\_inventory
- [#17109](https://github.com/influxdata/telegraf/pull/17109) `migrations` Add migration for inputs.kubernetes
- [#17103](https://github.com/influxdata/telegraf/pull/17103) `migrations` Add migration for inputs.openldap
- [#17105](https://github.com/influxdata/telegraf/pull/17105) `migrations` Add migration for inputs.rabbitmq
- [#17113](https://github.com/influxdata/telegraf/pull/17113) `migrations` Add migration for inputs.smart
- [#17112](https://github.com/influxdata/telegraf/pull/17112) `migrations` Add migration for inputs.sqlserver
- [#16950](https://github.com/influxdata/telegraf/pull/16950) `migrations` Add migration for outputs.amqp
- [#17160](https://github.com/influxdata/telegraf/pull/17160) `migrations` Add migration for outputs.influxdb
- [#17149](https://github.com/influxdata/telegraf/pull/17149) `migrations` Add migration for inputs.amqp\_consumer
- [#17150](https://github.com/influxdata/telegraf/pull/17150) `migrations` Add migration for inputs.consul
- [#17152](https://github.com/influxdata/telegraf/pull/17152) `migrations` Add migration for inputs.filecount
- [#17151](https://github.com/influxdata/telegraf/pull/17151) `migrations` Add migration for inputs.gnmi
- [#17153](https://github.com/influxdata/telegraf/pull/17153) `migrations` Add migration for inputs.http
- [#17158](https://github.com/influxdata/telegraf/pull/17158) `migrations` Add migration for inputs.http\_listener\_v2
- [#17157](https://github.com/influxdata/telegraf/pull/17157) `migrations` Add migration for inputs.http\_response
- [#17163](https://github.com/influxdata/telegraf/pull/17163) `migrations` Add migration for inputs.icinga2
- [#17165](https://github.com/influxdata/telegraf/pull/17165) `migrations` Add migration for inputs.internet\_speed
- [#17166](https://github.com/influxdata/telegraf/pull/17166) `migrations` Add migration for inputs.nsq\_consumer
- [#17159](https://github.com/influxdata/telegraf/pull/17159) `migrations` Add migration for inputs.ntpq
- [#17171](https://github.com/influxdata/telegraf/pull/17171) `migrations` Add migration for inputs.statsd
- [#17169](https://github.com/influxdata/telegraf/pull/17169) `migrations` Add migration for inputs.vsphere
- [#17167](https://github.com/influxdata/telegraf/pull/17167) `migrations` Add migration for outputs.kinesis
- [#17174](https://github.com/influxdata/telegraf/pull/17174) `migrations` Add migration for outputs.librato
- [#17176](https://github.com/influxdata/telegraf/pull/17176) `migrations` Add migration for outputs.mqtt
- [#17173](https://github.com/influxdata/telegraf/pull/17173) `migrations` Add migration for outputs.remotefile
- [#17172](https://github.com/influxdata/telegraf/pull/17172) `migrations` Add migration for outputs.wavefront
- [#17168](https://github.com/influxdata/telegraf/pull/17168) `migrations` Add migration for inputs.KNXListener
- [#17170](https://github.com/influxdata/telegraf/pull/17170) `migrations` Add migration for inputs.logparser
- [#16646](https://github.com/influxdata/telegraf/pull/16646) `outputs.health` Add max time between metrics check
- [#16597](https://github.com/influxdata/telegraf/pull/16597) `outputs.http` Include body sample in non-retryable error logs
- [#16741](https://github.com/influxdata/telegraf/pull/16741) `outputs.influxdb_v2` Implement concurrent writes
- [#16746](https://github.com/influxdata/telegraf/pull/16746) `outputs.influxdb_v2` Support secrets in http\_headers values
- [#16582](https://github.com/influxdata/telegraf/pull/16582) `outputs.nats` Allow asynchronous publishing for Jetstream
- [#16544](https://github.com/influxdata/telegraf/pull/16544) `outputs.sql` Add option to automate table schema updates
- [#16678](https://github.com/influxdata/telegraf/pull/16678) `outputs.sql` Support secret for dsn
- [#16583](https://github.com/influxdata/telegraf/pull/16583) `outputs.stackdriver` Ensure quota is charged to configured project
- [#16717](https://github.com/influxdata/telegraf/pull/16717) `processors.defaults` Add support for specifying default tags
- [#16701](https://github.com/influxdata/telegraf/pull/16701) `processors.enum` Add multiple tag mapping
- [#16030](https://github.com/influxdata/telegraf/pull/16030) `processors.enum` Allow mapping to be applied to multiple fields
- [#16494](https://github.com/influxdata/telegraf/pull/16494) `serializer.prometheusremotewrite` Allow sending native histograms

### Bug fixes

- [#17044](https://github.com/influxdata/telegraf/pull/17044) `inputs.opcua` Fix integration test
- [#16986](https://github.com/influxdata/telegraf/pull/16986) `inputs.procstat` Resolve remote usernames on Posix systems
- [#16699](https://github.com/influxdata/telegraf/pull/16699) `inputs.win_wmi` Free resources to avoid leaks
- [#17118](https://github.com/influxdata/telegraf/pull/17118) `migrations` Update table content for general plugin migrations

### Dependency updates

- [#17089](https://github.com/influxdata/telegraf/pull/17089) `deps` Bump cloud.google.com/go/bigquery from 1.68.0 to 1.69.0
- [#17026](https://github.com/influxdata/telegraf/pull/17026) `deps` Bump cloud.google.com/go/storage from 1.53.0 to 1.54.0
- [#17095](https://github.com/influxdata/telegraf/pull/17095) `deps` Bump cloud.google.com/go/storage from 1.54.0 to 1.55.0
- [#17034](https://github.com/influxdata/telegraf/pull/17034) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/azidentity from 1.9.0 to 1.10.0
- [#17065](https://github.com/influxdata/telegraf/pull/17065) `deps` Bump github.com/ClickHouse/clickhouse-go/v2 from 2.34.0 to 2.35.0
- [#17145](https://github.com/influxdata/telegraf/pull/17145) `deps` Bump github.com/ClickHouse/clickhouse-go/v2 from 2.35.0 to 2.36.0
- [#17062](https://github.com/influxdata/telegraf/pull/17062) `deps` Bump github.com/IBM/nzgo/v12 from 12.0.9 to 12.0.10
- [#17083](https://github.com/influxdata/telegraf/pull/17083) `deps` Bump github.com/IBM/sarama from 1.45.1 to 1.45.2
- [#17040](https://github.com/influxdata/telegraf/pull/17040) `deps` Bump github.com/apache/inlong/inlong-sdk/dataproxy-sdk-twins/dataproxy-sdk-golang from 1.0.0 to 1.0.1
- [#17060](https://github.com/influxdata/telegraf/pull/17060) `deps` Bump github.com/apache/inlong/inlong-sdk/dataproxy-sdk-twins/dataproxy-sdk-golang from 1.0.1 to 1.0.2
- [#17127](https://github.com/influxdata/telegraf/pull/17127) `deps` Bump github.com/apache/inlong/inlong-sdk/dataproxy-sdk-twins/dataproxy-sdk-golang from 1.0.2 to 1.0.3
- [#17061](https://github.com/influxdata/telegraf/pull/17061) `deps` Bump github.com/apache/thrift from 0.21.0 to 0.22.0
- [#16954](https://github.com/influxdata/telegraf/pull/16954) `deps` Bump github.com/aws/aws-msk-iam-sasl-signer-go from 1.0.1 to 1.0.3
- [#17041](https://github.com/influxdata/telegraf/pull/17041) `deps` Bump github.com/aws/aws-msk-iam-sasl-signer-go from 1.0.3 to 1.0.4
- [#17128](https://github.com/influxdata/telegraf/pull/17128) `deps` Bump github.com/aws/aws-sdk-go-v2/config from 1.29.14 to 1.29.15
- [#17129](https://github.com/influxdata/telegraf/pull/17129) `deps` Bump github.com/aws/aws-sdk-go-v2/credentials from 1.17.67 to 1.17.68
- [#17057](https://github.com/influxdata/telegraf/pull/17057) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatch from 1.44.3 to 1.45.0
- [#17132](https://github.com/influxdata/telegraf/pull/17132) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatch from 1.45.0 to 1.45.1
- [#17029](https://github.com/influxdata/telegraf/pull/17029) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs from 1.49.0 to 1.50.0
- [#17131](https://github.com/influxdata/telegraf/pull/17131) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs from 1.50.0 to 1.50.1
- [#17143](https://github.com/influxdata/telegraf/pull/17143) `deps` Bump github.com/aws/aws-sdk-go-v2/service/dynamodb from 1.43.1 to 1.43.2
- [#17037](https://github.com/influxdata/telegraf/pull/17037) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.218.0 to 1.219.0
- [#17067](https://github.com/influxdata/telegraf/pull/17067) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.220.0 to 1.222.0
- [#17093](https://github.com/influxdata/telegraf/pull/17093) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.222.0 to 1.224.0
- [#17136](https://github.com/influxdata/telegraf/pull/17136) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.224.0 to 1.225.0
- [#17139](https://github.com/influxdata/telegraf/pull/17139) `deps` Bump github.com/aws/aws-sdk-go-v2/service/kinesis from 1.35.0 to 1.35.1
- [#16996](https://github.com/influxdata/telegraf/pull/16996) `deps` Bump github.com/bluenviron/gomavlib/v3 from 3.1.0 to 3.2.1
- [#16987](https://github.com/influxdata/telegraf/pull/16987) `deps` Bump github.com/creack/goselect from 0.1.2 to 0.1.3
- [#17097](https://github.com/influxdata/telegraf/pull/17097) `deps` Bump github.com/docker/docker from 28.1.1+incompatible to 28.2.2+incompatible
- [#17133](https://github.com/influxdata/telegraf/pull/17133) `deps` Bump github.com/gosnmp/gosnmp from 1.40.0 to 1.41.0
- [#17126](https://github.com/influxdata/telegraf/pull/17126) `deps` Bump github.com/linkedin/goavro/v2 from 2.13.1 to 2.14.0
- [#17087](https://github.com/influxdata/telegraf/pull/17087) `deps` Bump github.com/lxc/incus/v6 from 6.12.0 to 6.13.0
- [#17085](https://github.com/influxdata/telegraf/pull/17085) `deps` Bump github.com/microsoft/go-mssqldb from 1.8.1 to 1.8.2
- [#17064](https://github.com/influxdata/telegraf/pull/17064) `deps` Bump github.com/nats-io/nats-server/v2 from 2.11.3 to 2.11.4
- [#17140](https://github.com/influxdata/telegraf/pull/17140) `deps` Bump github.com/nats-io/nats.go from 1.42.0 to 1.43.0
- [#17134](https://github.com/influxdata/telegraf/pull/17134) `deps` Bump github.com/netsampler/goflow2/v2 from 2.2.2 to 2.2.3
- [#17028](https://github.com/influxdata/telegraf/pull/17028) `deps` Bump github.com/prometheus/common from 0.63.0 to 0.64.0
- [#17066](https://github.com/influxdata/telegraf/pull/17066) `deps` Bump github.com/rclone/rclone from 1.69.2 to 1.69.3
- [#17096](https://github.com/influxdata/telegraf/pull/17096) `deps` Bump github.com/redis/go-redis/v9 from 9.8.0 to 9.9.0
- [#17088](https://github.com/influxdata/telegraf/pull/17088) `deps` Bump github.com/shirou/gopsutil/v4 from 4.25.4 to 4.25.5
- [#17135](https://github.com/influxdata/telegraf/pull/17135) `deps` Bump github.com/sijms/go-ora/v2 from 2.8.24 to 2.9.0
- [#17094](https://github.com/influxdata/telegraf/pull/17094) `deps` Bump github.com/snowflakedb/gosnowflake from 1.14.0 to 1.14.1
- [#17035](https://github.com/influxdata/telegraf/pull/17035) `deps` Bump github.com/tinylib/msgp from 1.2.5 to 1.3.0
- [#17054](https://github.com/influxdata/telegraf/pull/17054) `deps` Bump github.com/vmware/govmomi from 0.50.0 to 0.51.0
- [#17039](https://github.com/influxdata/telegraf/pull/17039) `deps` Bump github.com/yuin/goldmark from 1.7.11 to 1.7.12
- [#17130](https://github.com/influxdata/telegraf/pull/17130) `deps` Bump go.mongodb.org/mongo-driver from 1.17.3 to 1.17.4
- [#17056](https://github.com/influxdata/telegraf/pull/17056) `deps` Bump go.opentelemetry.io/collector/pdata from 1.31.0 to 1.33.0
- [#17058](https://github.com/influxdata/telegraf/pull/17058) `deps` Bump go.step.sm/crypto from 0.63.0 to 0.64.0
- [#17141](https://github.com/influxdata/telegraf/pull/17141) `deps` Bump golang.org/x/crypto from 0.38.0 to 0.39.0
- [#17144](https://github.com/influxdata/telegraf/pull/17144) `deps` Bump golang.org/x/mod from 0.24.0 to 0.25.0
- [#17033](https://github.com/influxdata/telegraf/pull/17033) `deps` Bump google.golang.org/api from 0.232.0 to 0.233.0
- [#17055](https://github.com/influxdata/telegraf/pull/17055) `deps` Bump google.golang.org/api from 0.233.0 to 0.234.0
- [#17086](https://github.com/influxdata/telegraf/pull/17086) `deps` Bump google.golang.org/api from 0.234.0 to 0.235.0
- [#17036](https://github.com/influxdata/telegraf/pull/17036) `deps` Bump google.golang.org/grpc from 1.72.0 to 1.72.1
- [#17059](https://github.com/influxdata/telegraf/pull/17059) `deps` Bump google.golang.org/grpc from 1.72.1 to 1.72.2
- [#17137](https://github.com/influxdata/telegraf/pull/17137) `deps` Bump google.golang.org/grpc from 1.72.2 to 1.73.0
- [#17031](https://github.com/influxdata/telegraf/pull/17031) `deps` Bump k8s.io/api from 0.33.0 to 0.33.1
- [#17038](https://github.com/influxdata/telegraf/pull/17038) `deps` Bump k8s.io/apimachinery from 0.33.0 to 0.33.1
- [#17030](https://github.com/influxdata/telegraf/pull/17030) `deps` Bump k8s.io/client-go from 0.33.0 to 0.33.1
- [#17025](https://github.com/influxdata/telegraf/pull/17025) `deps` Bump super-linter/super-linter from 7.3.0 to 7.4.0

## v1.34.4

### Bug fixes

- [#17009](https://github.com/influxdata/telegraf/pull/17009) `inputs.cloudwatch` Restore filtering to match all dimensions
- [#16978](https://github.com/influxdata/telegraf/pull/16978) `inputs.nfsclient` Handle errors during mountpoint filtering
- [#17021](https://github.com/influxdata/telegraf/pull/17021) `inputs.opcua` Fix type mismatch in unit test
- [#16854](https://github.com/influxdata/telegraf/pull/16854) `inputs.opcua` Handle session invalidation between gather cycles
- [#16879](https://github.com/influxdata/telegraf/pull/16879) `inputs.tail` Prevent leaking file descriptors
- [#16815](https://github.com/influxdata/telegraf/pull/16815) `inputs.win_eventlog` Handle large events to avoid they get dropped silently
- [#16878](https://github.com/influxdata/telegraf/pull/16878) `parsers.json_v2` Handle measurements with multiple objects correctly

### Dependency updates

- [#16991](https://github.com/influxdata/telegraf/pull/16991) `deps` Bump cloud.google.com/go/bigquery from 1.67.0 to 1.68.0
- [#16963](https://github.com/influxdata/telegraf/pull/16963) `deps` Bump cloud.google.com/go/storage from 1.52.0 to 1.53.0
- [#16955](https://github.com/influxdata/telegraf/pull/16955) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/storage/azqueue from 1.0.0 to 1.0.1
- [#16989](https://github.com/influxdata/telegraf/pull/16989) `deps` Bump github.com/SAP/go-hdb from 1.13.5 to 1.13.6
- [#16998](https://github.com/influxdata/telegraf/pull/16998) `deps` Bump github.com/apache/arrow-go/v18 from 18.2.0 to 18.3.0
- [#16952](https://github.com/influxdata/telegraf/pull/16952) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs from 1.47.3 to 1.48.0
- [#16995](https://github.com/influxdata/telegraf/pull/16995) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs from 1.48.0 to 1.49.0
- [#16974](https://github.com/influxdata/telegraf/pull/16974) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.212.0 to 1.214.0
- [#16993](https://github.com/influxdata/telegraf/pull/16993) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.215.0 to 1.218.0
- [#16968](https://github.com/influxdata/telegraf/pull/16968) `deps` Bump github.com/aws/aws-sdk-go-v2/service/kinesis from 1.33.3 to 1.35.0
- [#16988](https://github.com/influxdata/telegraf/pull/16988) `deps` Bump github.com/aws/aws-sdk-go-v2/service/timestreamwrite from 1.30.2 to 1.31.0
- [#17013](https://github.com/influxdata/telegraf/pull/17013) `deps` Bump github.com/ebitengine/purego from 0.8.2 to 0.8.3
- [#16972](https://github.com/influxdata/telegraf/pull/16972) `deps` Bump github.com/hashicorp/consul/api from 1.32.0 to 1.32.1
- [#16992](https://github.com/influxdata/telegraf/pull/16992) `deps` Bump github.com/microsoft/go-mssqldb from 1.8.0 to 1.8.1
- [#16990](https://github.com/influxdata/telegraf/pull/16990) `deps` Bump github.com/miekg/dns from 1.1.65 to 1.1.66
- [#16975](https://github.com/influxdata/telegraf/pull/16975) `deps` Bump github.com/nats-io/nats-server/v2 from 2.11.2 to 2.11.3
- [#16967](https://github.com/influxdata/telegraf/pull/16967) `deps` Bump github.com/nats-io/nats.go from 1.41.2 to 1.42.0
- [#16964](https://github.com/influxdata/telegraf/pull/16964) `deps` Bump github.com/rclone/rclone from 1.69.1 to 1.69.2
- [#16973](https://github.com/influxdata/telegraf/pull/16973) `deps` Bump github.com/redis/go-redis/v9 from 9.7.3 to 9.8.0
- [#16962](https://github.com/influxdata/telegraf/pull/16962) `deps` Bump github.com/shirou/gopsutil/v4 from 4.25.3 to 4.25.4
- [#16969](https://github.com/influxdata/telegraf/pull/16969) `deps` Bump github.com/snowflakedb/gosnowflake from 1.13.3 to 1.14.0
- [#16994](https://github.com/influxdata/telegraf/pull/16994) `deps` Bump github.com/vishvananda/netlink from 1.3.1-0.20250221194427-0af32151e72b to 1.3.1
- [#16958](https://github.com/influxdata/telegraf/pull/16958) `deps` Bump go.step.sm/crypto from 0.62.0 to 0.63.0
- [#16960](https://github.com/influxdata/telegraf/pull/16960) `deps` Bump golang.org/x/crypto from 0.37.0 to 0.38.0
- [#16966](https://github.com/influxdata/telegraf/pull/16966) `deps` Bump golang.org/x/net from 0.39.0 to 0.40.0
- [#16957](https://github.com/influxdata/telegraf/pull/16957) `deps` Bump google.golang.org/api from 0.230.0 to 0.231.0
- [#16853](https://github.com/influxdata/telegraf/pull/16853) `deps` Switch to maintained azure testcontainer module

## v1.34.3

### Bug fixes

- [#16697](https://github.com/influxdata/telegraf/pull/16697) `agent` Correctly truncate the disk buffer
- [#16868](https://github.com/influxdata/telegraf/pull/16868) `common.ratelimiter` Only grow the buffer but never shrink
- [#16812](https://github.com/influxdata/telegraf/pull/16812) `inputs.cloudwatch` Handle metric includes/excludes correctly to prevent panic
- [#16911](https://github.com/influxdata/telegraf/pull/16911) `inputs.lustre2` Skip empty files
- [#16594](https://github.com/influxdata/telegraf/pull/16594) `inputs.opcua` Handle node array values
- [#16782](https://github.com/influxdata/telegraf/pull/16782) `inputs.win_wmi` Replace hard-coded class-name with correct config setting
- [#16781](https://github.com/influxdata/telegraf/pull/16781) `inputs.win_wmi` Restrict threading model to APARTMENTTHREADED
- [#16857](https://github.com/influxdata/telegraf/pull/16857) `outputs.quix` Allow empty certificate for new cloud managed instances

### Dependency updates

- [#16804](https://github.com/influxdata/telegraf/pull/16804) `deps` Bump cloud.google.com/go/bigquery from 1.66.2 to 1.67.0
- [#16835](https://github.com/influxdata/telegraf/pull/16835) `deps` Bump cloud.google.com/go/monitoring from 1.24.0 to 1.24.2
- [#16785](https://github.com/influxdata/telegraf/pull/16785) `deps` Bump cloud.google.com/go/pubsub from 1.48.0 to 1.49.0
- [#16897](https://github.com/influxdata/telegraf/pull/16897) `deps` Bump cloud.google.com/go/storage from 1.51.0 to 1.52.0
- [#16840](https://github.com/influxdata/telegraf/pull/16840) `deps` Bump github.com/BurntSushi/toml from 1.4.0 to 1.5.0
- [#16838](https://github.com/influxdata/telegraf/pull/16838) `deps` Bump github.com/aliyun/alibaba-cloud-sdk-go from 1.63.104 to 1.63.106
- [#16908](https://github.com/influxdata/telegraf/pull/16908) `deps` Bump github.com/aliyun/alibaba-cloud-sdk-go from 1.63.106 to 1.63.107
- [#16789](https://github.com/influxdata/telegraf/pull/16789) `deps` Bump github.com/antchfx/xpath from 1.3.3 to 1.3.4
- [#16807](https://github.com/influxdata/telegraf/pull/16807) `deps` Bump github.com/apache/arrow-go/v18 from 18.1.0 to 18.2.0
- [#16844](https://github.com/influxdata/telegraf/pull/16844) `deps` Bump github.com/apache/iotdb-client-go from 1.3.3 to 1.3.4
- [#16839](https://github.com/influxdata/telegraf/pull/16839) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatch from 1.44.1 to 1.44.3
- [#16836](https://github.com/influxdata/telegraf/pull/16836) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs from 1.45.3 to 1.47.3
- [#16846](https://github.com/influxdata/telegraf/pull/16846) `deps` Bump github.com/aws/aws-sdk-go-v2/service/dynamodb from 1.42.2 to 1.42.4
- [#16905](https://github.com/influxdata/telegraf/pull/16905) `deps` Bump github.com/aws/aws-sdk-go-v2/service/dynamodb from 1.42.4 to 1.43.1
- [#16842](https://github.com/influxdata/telegraf/pull/16842) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.210.1 to 1.211.3
- [#16900](https://github.com/influxdata/telegraf/pull/16900) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.211.3 to 1.212.0
- [#16903](https://github.com/influxdata/telegraf/pull/16903) `deps` Bump github.com/aws/aws-sdk-go-v2/service/kinesis from 1.33.2 to 1.33.3
- [#16793](https://github.com/influxdata/telegraf/pull/16793) `deps` Bump github.com/aws/aws-sdk-go-v2/service/timestreamwrite from 1.27.4 to 1.30.2
- [#16802](https://github.com/influxdata/telegraf/pull/16802) `deps` Bump github.com/clarify/clarify-go from 0.3.1 to 0.4.0
- [#16849](https://github.com/influxdata/telegraf/pull/16849) `deps` Bump github.com/docker/docker from 28.0.4+incompatible to 28.1.1+incompatible
- [#16830](https://github.com/influxdata/telegraf/pull/16830) `deps` Bump github.com/go-ldap/ldap/v3 from 3.4.10 to 3.4.11
- [#16801](https://github.com/influxdata/telegraf/pull/16801) `deps` Bump github.com/go-sql-driver/mysql from 1.8.1 to 1.9.2
- [#16806](https://github.com/influxdata/telegraf/pull/16806) `deps` Bump github.com/gofrs/uuid/v5 from 5.3.0 to 5.3.2
- [#16895](https://github.com/influxdata/telegraf/pull/16895) `deps` Bump github.com/google/cel-go from 0.24.1 to 0.25.0
- [#16797](https://github.com/influxdata/telegraf/pull/16797) `deps` Bump github.com/gopcua/opcua from 0.7.1 to 0.7.4
- [#16894](https://github.com/influxdata/telegraf/pull/16894) `deps` Bump github.com/gopcua/opcua from 0.7.4 to 0.8.0
- [#16660](https://github.com/influxdata/telegraf/pull/16660) `deps` Bump github.com/gosmnp/gosnmp from 1.39.0 to 1.40.0
- [#16902](https://github.com/influxdata/telegraf/pull/16902) `deps` Bump github.com/gosnmp/gosnmp from 1.39.0 to 1.40.0
- [#16841](https://github.com/influxdata/telegraf/pull/16841) `deps` Bump github.com/hashicorp/consul/api from 1.31.2 to 1.32.0
- [#16891](https://github.com/influxdata/telegraf/pull/16891) `deps` Bump github.com/jedib0t/go-pretty/v6 from 6.6.5 to 6.6.7
- [#16892](https://github.com/influxdata/telegraf/pull/16892) `deps` Bump github.com/lxc/incus/v6 from 6.11.0 to 6.12.0
- [#16786](https://github.com/influxdata/telegraf/pull/16786) `deps` Bump github.com/microsoft/go-mssqldb from 1.7.2 to 1.8.0
- [#16851](https://github.com/influxdata/telegraf/pull/16851) `deps` Bump github.com/miekg/dns from 1.1.64 to 1.1.65
- [#16808](https://github.com/influxdata/telegraf/pull/16808) `deps` Bump github.com/nats-io/nats-server/v2 from 2.10.25 to 2.10.27
- [#16888](https://github.com/influxdata/telegraf/pull/16888) `deps` Bump github.com/nats-io/nats-server/v2 from 2.10.27 to 2.11.2
- [#16909](https://github.com/influxdata/telegraf/pull/16909) `deps` Bump github.com/nats-io/nats.go from 1.41.1 to 1.41.2
- [#16790](https://github.com/influxdata/telegraf/pull/16790) `deps` Bump github.com/openconfig/gnmi from 0.11.0 to 0.14.1
- [#16799](https://github.com/influxdata/telegraf/pull/16799) `deps` Bump github.com/openconfig/goyang from 1.6.0 to 1.6.2
- [#16848](https://github.com/influxdata/telegraf/pull/16848) `deps` Bump github.com/prometheus-community/pro-bing from 0.4.1 to 0.7.0
- [#16795](https://github.com/influxdata/telegraf/pull/16795) `deps` Bump github.com/prometheus/client\_golang from 1.21.1 to 1.22.0
- [#16845](https://github.com/influxdata/telegraf/pull/16845) `deps` Bump github.com/prometheus/client\_model from 0.6.1 to 0.6.2
- [#16901](https://github.com/influxdata/telegraf/pull/16901) `deps` Bump github.com/prometheus/procfs from 0.16.0 to 0.16.1
- [#16792](https://github.com/influxdata/telegraf/pull/16792) `deps` Bump github.com/safchain/ethtool from 0.3.0 to 0.5.10
- [#16791](https://github.com/influxdata/telegraf/pull/16791) `deps` Bump github.com/seancfoley/ipaddress-go from 1.7.0 to 1.7.1
- [#16794](https://github.com/influxdata/telegraf/pull/16794) `deps` Bump github.com/shirou/gopsutil/v4 from 4.25.1 to 4.25.3
- [#16828](https://github.com/influxdata/telegraf/pull/16828) `deps` Bump github.com/snowflakedb/gosnowflake from 1.11.2 to 1.13.1
- [#16904](https://github.com/influxdata/telegraf/pull/16904) `deps` Bump github.com/snowflakedb/gosnowflake from 1.13.1 to 1.13.3
- [#16787](https://github.com/influxdata/telegraf/pull/16787) `deps` Bump github.com/srebhan/cborquery from 1.0.3 to 1.0.4
- [#16837](https://github.com/influxdata/telegraf/pull/16837) `deps` Bump github.com/srebhan/protobufquery from 1.0.1 to 1.0.4
- [#16893](https://github.com/influxdata/telegraf/pull/16893) `deps` Bump github.com/testcontainers/testcontainers-go from 0.36.0 to 0.37.0
- [#16803](https://github.com/influxdata/telegraf/pull/16803) `deps` Bump github.com/testcontainers/testcontainers-go/modules/kafka from 0.34.0 to 0.36.0
- [#16890](https://github.com/influxdata/telegraf/pull/16890) `deps` Bump github.com/testcontainers/testcontainers-go/modules/kafka from 0.36.0 to 0.37.0
- [#16850](https://github.com/influxdata/telegraf/pull/16850) `deps` Bump github.com/vmware/govmomi from 0.49.0 to 0.50.0
- [#16784](https://github.com/influxdata/telegraf/pull/16784) `deps` Bump github.com/yuin/goldmark from 1.7.8 to 1.7.9
- [#16896](https://github.com/influxdata/telegraf/pull/16896) `deps` Bump github.com/yuin/goldmark from 1.7.9 to 1.7.11
- [#16832](https://github.com/influxdata/telegraf/pull/16832) `deps` Bump go.mongodb.org/mongo-driver from 1.17.0 to 1.17.3
- [#16800](https://github.com/influxdata/telegraf/pull/16800) `deps` Bump go.opentelemetry.io/collector/pdata from 1.29.0 to 1.30.0
- [#16907](https://github.com/influxdata/telegraf/pull/16907) `deps` Bump go.opentelemetry.io/collector/pdata from 1.30.0 to 1.31.0
- [#16831](https://github.com/influxdata/telegraf/pull/16831) `deps` Bump go.step.sm/crypto from 0.60.0 to 0.61.0
- [#16886](https://github.com/influxdata/telegraf/pull/16886) `deps` Bump go.step.sm/crypto from 0.61.0 to 0.62.0
- [#16816](https://github.com/influxdata/telegraf/pull/16816) `deps` Bump golangci-lint from v2.0.2 to v2.1.2
- [#16852](https://github.com/influxdata/telegraf/pull/16852) `deps` Bump gonum.org/v1/gonum from 0.15.1 to 0.16.0
- [#16805](https://github.com/influxdata/telegraf/pull/16805) `deps` Bump google.golang.org/api from 0.228.0 to 0.229.0
- [#16898](https://github.com/influxdata/telegraf/pull/16898) `deps` Bump google.golang.org/api from 0.229.0 to 0.230.0
- [#16834](https://github.com/influxdata/telegraf/pull/16834) `deps` Bump google.golang.org/grpc from 1.71.1 to 1.72.0
- [#16889](https://github.com/influxdata/telegraf/pull/16889) `deps` Bump k8s.io/client-go from 0.32.3 to 0.33.0
- [#16843](https://github.com/influxdata/telegraf/pull/16843) `deps` Bump modernc.org/sqlite from 1.36.2 to 1.37.0

## v1.34.2

### Bug fixes

- [#16375](https://github.com/influxdata/telegraf/pull/16375) `aggregators` Handle time drift when calculating aggregation windows

### Dependency updates

- [#16689](https://github.com/influxdata/telegraf/pull/16689) `deps` Bump cloud.google.com/go/pubsub from 1.45.3 to 1.48.0
- [#16769](https://github.com/influxdata/telegraf/pull/16769) `deps` Bump cloud.google.com/go/storage from 1.50.0 to 1.51.0
- [#16771](https://github.com/influxdata/telegraf/pull/16771) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/azcore from 1.17.0 to 1.18.0
- [#16708](https://github.com/influxdata/telegraf/pull/16708) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/messaging/azeventhubs from 1.2.3 to 1.3.1
- [#16764](https://github.com/influxdata/telegraf/pull/16764) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/messaging/azeventhubs from 1.3.1 to 1.3.2
- [#16777](https://github.com/influxdata/telegraf/pull/16777) `deps` Bump github.com/ClickHouse/clickhouse-go/v2 from 2.30.3 to 2.34.0
- [#16707](https://github.com/influxdata/telegraf/pull/16707) `deps` Bump github.com/IBM/sarama from v1.43.3 to v1.45.1
- [#16739](https://github.com/influxdata/telegraf/pull/16739) `deps` Bump github.com/SAP/go-hdb from 1.9.10 to 1.13.5
- [#16754](https://github.com/influxdata/telegraf/pull/16754) `deps` Bump github.com/aliyun/alibaba-cloud-sdk-go from 1.62.721 to 1.63.104
- [#16767](https://github.com/influxdata/telegraf/pull/16767) `deps` Bump github.com/antchfx/jsonquery from 1.3.3 to 1.3.6
- [#16758](https://github.com/influxdata/telegraf/pull/16758) `deps` Bump github.com/aws/aws-sdk-go-v2/config from 1.29.6 to 1.29.13
- [#16710](https://github.com/influxdata/telegraf/pull/16710) `deps` Bump github.com/aws/aws-sdk-go-v2/credentials from 1.17.59 to 1.17.65
- [#16685](https://github.com/influxdata/telegraf/pull/16685) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatch from 1.43.14 to 1.44.1
- [#16773](https://github.com/influxdata/telegraf/pull/16773) `deps` Bump github.com/aws/aws-sdk-go-v2/service/dynamodb from 1.40.0 to 1.42.2
- [#16688](https://github.com/influxdata/telegraf/pull/16688) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.203.1 to 1.210.1
- [#16772](https://github.com/influxdata/telegraf/pull/16772) `deps` Bump github.com/aws/aws-sdk-go-v2/service/kinesis from 1.32.6 to 1.33.2
- [#16711](https://github.com/influxdata/telegraf/pull/16711) `deps` Bump github.com/cloudevents/sdk-go/v2 from 2.15.2 to 2.16.0
- [#16687](https://github.com/influxdata/telegraf/pull/16687) `deps` Bump github.com/google/cel-go from 0.23.0 to 0.24.1
- [#16712](https://github.com/influxdata/telegraf/pull/16712) `deps` Bump github.com/gophercloud/gophercloud/v2 from 2.0.0-rc.3 to 2.6.0
- [#16738](https://github.com/influxdata/telegraf/pull/16738) `deps` Bump github.com/gorcon/rcon from 1.3.5 to 1.4.0
- [#16737](https://github.com/influxdata/telegraf/pull/16737) `deps` Bump github.com/gosnmp/gosnmp from 1.38.0 to 1.39.0
- [#16752](https://github.com/influxdata/telegraf/pull/16752) `deps` Bump github.com/lxc/incus/v6 from 6.9.0 to 6.11.0
- [#16761](https://github.com/influxdata/telegraf/pull/16761) `deps` Bump github.com/nats-io/nats.go from 1.39.1 to 1.41.1
- [#16753](https://github.com/influxdata/telegraf/pull/16753) `deps` Bump github.com/netsampler/goflow2/v2 from 2.2.1 to 2.2.2
- [#16760](https://github.com/influxdata/telegraf/pull/16760) `deps` Bump github.com/p4lang/p4runtime from 1.4.0 to 1.4.1
- [#16766](https://github.com/influxdata/telegraf/pull/16766) `deps` Bump github.com/prometheus/common from 0.62.0 to 0.63.0
- [#16686](https://github.com/influxdata/telegraf/pull/16686) `deps` Bump github.com/rclone/rclone from 1.68.2 to 1.69.1
- [#16770](https://github.com/influxdata/telegraf/pull/16770) `deps` Bump github.com/sijms/go-ora/v2 from 2.8.22 to 2.8.24
- [#16709](https://github.com/influxdata/telegraf/pull/16709) `deps` Bump github.com/testcontainers/testcontainers-go from 0.35.0 to 0.36.0
- [#16763](https://github.com/influxdata/telegraf/pull/16763) `deps` Bump github.com/tinylib/msgp from 1.2.0 to 1.2.5
- [#16757](https://github.com/influxdata/telegraf/pull/16757) `deps` Bump github.com/urfave/cli/v2 from 2.27.2 to 2.27.6
- [#16724](https://github.com/influxdata/telegraf/pull/16724) `deps` Bump github.com/vmware/govmomi from v0.45.1 to v0.49.0
- [#16768](https://github.com/influxdata/telegraf/pull/16768) `deps` Bump go.opentelemetry.io/collector/pdata from 1.25.0 to 1.29.0
- [#16765](https://github.com/influxdata/telegraf/pull/16765) `deps` Bump go.step.sm/crypto from 0.59.1 to 0.60.0
- [#16756](https://github.com/influxdata/telegraf/pull/16756) `deps` Bump golang.org/x/crypto from 0.36.0 to 0.37.0
- [#16683](https://github.com/influxdata/telegraf/pull/16683) `deps` Bump golangci-lint from v1.64.5 to v2.0.2
- [#16759](https://github.com/influxdata/telegraf/pull/16759) `deps` Bump google.golang.org/api from 0.224.0 to 0.228.0
- [#16755](https://github.com/influxdata/telegraf/pull/16755) `deps` Bump k8s.io/client-go from 0.32.1 to 0.32.3
- [#16684](https://github.com/influxdata/telegraf/pull/16684) `deps` Bump tj-actions/changed-files from 46.0.1 to 46.0.3
- [#16736](https://github.com/influxdata/telegraf/pull/16736) `deps` Bump tj-actions/changed-files from 46.0.3 to 46.0.4
- [#16751](https://github.com/influxdata/telegraf/pull/16751) `deps` Bump tj-actions/changed-files from 46.0.4 to 46.0.5

## v1.34.1

### Bug fixes

- [#16638](https://github.com/influxdata/telegraf/pull/16638) `agent` Condense plugin source information table when multiple plugins in same file
- [#16674](https://github.com/influxdata/telegraf/pull/16674) `inputs.tail` Do not seek on pipes
- [#16643](https://github.com/influxdata/telegraf/pull/16643) `inputs.tail` Use correct initial\_read\_offset persistent offset naming in the code
- [#16628](https://github.com/influxdata/telegraf/pull/16628) `outputs.influxdb_v2` Use dynamic token secret
- [#16625](https://github.com/influxdata/telegraf/pull/16625) `outputs.sql` Allow to disable timestamp column
- [#16682](https://github.com/influxdata/telegraf/pull/16682) `secrets` Make ‘insufficient lockable memory’ warning work on BSDs

### Dependency updates

- [#16612](https://github.com/influxdata/telegraf/pull/16612) `deps` Bump github.com/PaesslerAG/gval from 1.2.2 to 1.2.4
- [#16650](https://github.com/influxdata/telegraf/pull/16650) `deps` Bump github.com/aws/smithy-go from 1.22.2 to 1.22.3
- [#16680](https://github.com/influxdata/telegraf/pull/16680) `deps` Bump github.com/golang-jwt/jwt/v4 from 4.5.1 to 4.5.2
- [#16679](https://github.com/influxdata/telegraf/pull/16679) `deps` Bump github.com/golang-jwt/jwt/v5 from 5.2.1 to 5.2.2
- [#16610](https://github.com/influxdata/telegraf/pull/16610) `deps` Bump github.com/golang/snappy from 0.0.4 to 1.0.0
- [#16652](https://github.com/influxdata/telegraf/pull/16652) `deps` Bump github.com/hashicorp/consul/api from 1.29.2 to 1.31.2
- [#16651](https://github.com/influxdata/telegraf/pull/16651) `deps` Bump github.com/leodido/go-syslog/v4 from 4.1.0 to 4.2.0
- [#16613](https://github.com/influxdata/telegraf/pull/16613) `deps` Bump github.com/linkedin/goavro/v2 from 2.13.0 to 2.13.1
- [#16671](https://github.com/influxdata/telegraf/pull/16671) `deps` Bump github.com/redis/go-redis/v9 from 9.7.0 to 9.7.3
- [#16611](https://github.com/influxdata/telegraf/pull/16611) `deps` Bump go.step.sm/crypto from 0.54.0 to 0.59.1
- [#16640](https://github.com/influxdata/telegraf/pull/16640) `deps` Bump golang.org/x/crypto from 0.35.0 to 0.36.0
- [#16620](https://github.com/influxdata/telegraf/pull/16620) `deps` Bump golang.org/x/net from 0.35.0 to 0.36.0
- [#16639](https://github.com/influxdata/telegraf/pull/16639) `deps` Bump golang.org/x/oauth2 from 0.26.0 to 0.28.0
- [#16653](https://github.com/influxdata/telegraf/pull/16653) `deps` Bump k8s.io/api from 0.32.1 to 0.32.3
- [#16659](https://github.com/influxdata/telegraf/pull/16659) `deps` Bump tj-actions/changed-files from v45 to v46.0.1

## v1.34.0

### New Plugins

- [#15988](https://github.com/influxdata/telegraf/pull/15988) `inputs.firehose` Add new plugin
- [#16352](https://github.com/influxdata/telegraf/pull/16352) `inputs.huebridge` Add plugin
- [#16392](https://github.com/influxdata/telegraf/pull/16392) `inputs.nsdp` Add plugin

### Features

- [#16333](https://github.com/influxdata/telegraf/pull/16333) `agent` Add support for input probing
- [#16270](https://github.com/influxdata/telegraf/pull/16270) `agent` Print plugins source information
- [#16474](https://github.com/influxdata/telegraf/pull/16474) `inputs.cgroup` Support more cgroup v2 formats
- [#16337](https://github.com/influxdata/telegraf/pull/16337) `inputs.cloudwatch` Allow wildcards for namespaces
- [#16292](https://github.com/influxdata/telegraf/pull/16292) `inputs.docker` Support swarm jobs
- [#16501](https://github.com/influxdata/telegraf/pull/16501) `inputs.exec` Allow to get untruncated errors in debug mode
- [#16480](https://github.com/influxdata/telegraf/pull/16480) `inputs.gnmi` Add support for `depth` extension
- [#16336](https://github.com/influxdata/telegraf/pull/16336) `inputs.infiniband` Add support for RDMA counters
- [#16124](https://github.com/influxdata/telegraf/pull/16124) `inputs.ipset` Add metric for number of entries and individual IPs
- [#16579](https://github.com/influxdata/telegraf/pull/16579) `inputs.nvidia_smi` Add new power-draw fields for v12 scheme
- [#16305](https://github.com/influxdata/telegraf/pull/16305) `inputs.nvidia_smi` Implement probing
- [#16105](https://github.com/influxdata/telegraf/pull/16105) `inputs.procstat` Add child level tag
- [#16066](https://github.com/influxdata/telegraf/pull/16066) `inputs.proxmox` Allow to add VM-id and status as tag
- [#16287](https://github.com/influxdata/telegraf/pull/16287) `inputs.systemd_units` Add active\_enter\_timestamp\_us field
- [#16342](https://github.com/influxdata/telegraf/pull/16342) `inputs.tail` Add `initial_read_offset` config for controlling read behavior
- [#16355](https://github.com/influxdata/telegraf/pull/16355) `inputs.webhooks` Add support for GitHub workflow events
- [#16508](https://github.com/influxdata/telegraf/pull/16508) `inputs.x509_cert` Add support for JKS and PKCS#12 keystores
- [#16491](https://github.com/influxdata/telegraf/pull/16491) `outputs.mqtt` Add sprig for topic name generator for homie layout
- [#16570](https://github.com/influxdata/telegraf/pull/16570) `outputs.nats` Use Jetstream publisher when using Jetstream
- [#16566](https://github.com/influxdata/telegraf/pull/16566) `outputs.prometheus_client` Allow adding custom headers
- [#16272](https://github.com/influxdata/telegraf/pull/16272) `parsers.avro` Allow union fields to be specified as tags
- [#16493](https://github.com/influxdata/telegraf/pull/16493) `parsers.prometheusremotewrite` Add dense metric version to better support histograms
- [#16214](https://github.com/influxdata/telegraf/pull/16214) `processors.converter` Add support for base64 encoded IEEE floats
- [#16497](https://github.com/influxdata/telegraf/pull/16497) `processors.template` Add sprig function for templates

### Bug fixes

- [#16542](https://github.com/influxdata/telegraf/pull/16542) `inputs.gnmi` Handle path elements without name but with keys correctly
- [#16606](https://github.com/influxdata/telegraf/pull/16606) `inputs.huebridge` Cleanup and fix linter issues
- [#16580](https://github.com/influxdata/telegraf/pull/16580) `inputs.net` Skip checks in containerized environments
- [#16555](https://github.com/influxdata/telegraf/pull/16555) `outputs.opensearch` Use correct pipeline name while creating bulk-indexers
- [#16557](https://github.com/influxdata/telegraf/pull/16557) `serializers.prometheus` Use legacy validation for metric name

### Dependency updates

- [#16576](https://github.com/influxdata/telegraf/pull/16576) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/azidentity from 1.8.1 to 1.8.2
- [#16553](https://github.com/influxdata/telegraf/pull/16553) `deps` Bump github.com/Azure/go-autorest/autorest from 0.11.29 to 0.11.30
- [#16552](https://github.com/influxdata/telegraf/pull/16552) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.198.1 to 1.203.1
- [#16554](https://github.com/influxdata/telegraf/pull/16554) `deps` Bump github.com/go-jose/go-jose/v4 from 4.0.4 to 4.0.5
- [#16574](https://github.com/influxdata/telegraf/pull/16574) `deps` Bump github.com/gopcua/opcua from 0.5.3 to 0.7.1
- [#16551](https://github.com/influxdata/telegraf/pull/16551) `deps` Bump github.com/nats-io/nats.go from 1.39.0 to 1.39.1
- [#16575](https://github.com/influxdata/telegraf/pull/16575) `deps` Bump github.com/tidwall/wal from 1.1.7 to 1.1.8
- [#16578](https://github.com/influxdata/telegraf/pull/16578) `deps` Bump super-linter/super-linter from 7.2.1 to 7.3.0

## v1.33.3

### Important Changes

- PR [#16507](https://github.com/influxdata/telegraf/pull/16507) adds the `enforce_first_namespace_as_origin` to the GNMI input plugin. This option allows to disable mangling of the response `path` tag by *not* using namespaces as origin. It is highly recommended to disable the option. However, disabling the behavior might change the `path` tag and thus might break existing queries. Furthermore, the tag modification might increase cardinality in your database.

### Bug fixes

- [#16546](https://github.com/influxdata/telegraf/pull/16546) `agent` Add authorization and user-agent when watching remote configs
- [#16507](https://github.com/influxdata/telegraf/pull/16507) `inputs.gnmi` Allow to disable using first namespace as origin
- [#16511](https://github.com/influxdata/telegraf/pull/16511) `inputs.proxmox` Allow search domain to be empty
- [#16530](https://github.com/influxdata/telegraf/pull/16530) `internal` Fix plural acronyms in SnakeCase function
- [#16539](https://github.com/influxdata/telegraf/pull/16539) `logging` Handle closing correctly and fix tests
- [#16535](https://github.com/influxdata/telegraf/pull/16535) `processors.execd` Detect line-protocol parser correctly

### Dependency updates

- [#16506](https://github.com/influxdata/telegraf/pull/16506) `deps` Bump github.com/ClickHouse/clickhouse-go/v2 from 2.30.1 to 2.30.3
- [#16502](https://github.com/influxdata/telegraf/pull/16502) `deps` Bump github.com/antchfx/xmlquery from 1.4.1 to 1.4.4
- [#16519](https://github.com/influxdata/telegraf/pull/16519) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatch from 1.43.1 to 1.43.14
- [#16503](https://github.com/influxdata/telegraf/pull/16503) `deps` Bump github.com/aws/aws-sdk-go-v2/service/dynamodb from 1.36.2 to 1.40.0
- [#16522](https://github.com/influxdata/telegraf/pull/16522) `deps` Bump github.com/nats-io/nats.go from 1.37.0 to 1.39.0
- [#16505](https://github.com/influxdata/telegraf/pull/16505) `deps` Bump github.com/srebhan/cborquery from 1.0.1 to 1.0.3
- [#16534](https://github.com/influxdata/telegraf/pull/16534) `deps` Bump github.com/vishvananda/netlink from 1.3.0 to 1.3.1-0.20250221194427-0af32151e72b
- [#16521](https://github.com/influxdata/telegraf/pull/16521) `deps` Bump go.opentelemetry.io/collector/pdata from 1.12.0 to 1.25.0
- [#16504](https://github.com/influxdata/telegraf/pull/16504) `deps` Bump golang.org/x/net from 0.34.0 to 0.35.0
- [#16512](https://github.com/influxdata/telegraf/pull/16512) `deps` Bump golangci-lint from v1.63.4 to v1.64.5

## v1.33.2

### Important Changes

- PR [#16423](https://github.com/influxdata/telegraf/pull/16423) converts the ClickHouse drivers to the v2 version. This new version also requires a [new format for the DSN](https://github.com/ClickHouse/clickhouse-go/tree/v2.30.2?tab=readme-ov-file#dsn). The plugin tries its best to convert the old DSN to the new format but might not be able to do so. Please check for warnings in your log file and convert to the new format as soon as possible.
- PR [#16403](https://github.com/influxdata/telegraf/pull/16403) ensures consistency of the NetFlow plugin’s `ip_version` field type by enforcing “IPv4”, “IPv6”, or “unknown” string values. Previously the `ip_version` could become an (unsigned) integer when parsing raw-packets’ headers especially with SFlow v5 input. Please watch out for type-conflicts on the output side!

### Bug fixes

- [#16477](https://github.com/influxdata/telegraf/pull/16477) `agent` Avoid panic by checking for skip\_processors\_after\_aggregators
- [#16489](https://github.com/influxdata/telegraf/pull/16489) `agent` Set `godebug x509negativeserial=1` as a workaround
- [#16403](https://github.com/influxdata/telegraf/pull/16403) `inputs.netflow` Ensure type consistency for sFlow's IP version field
- [#16447](https://github.com/influxdata/telegraf/pull/16447) `inputs.x509_cert` Add config to left-pad serial number to 128-bits
- [#16448](https://github.com/influxdata/telegraf/pull/16448) `outputs.azure_monitor` Prevent infinite send loop for outdated metrics
- [#16472](https://github.com/influxdata/telegraf/pull/16472) `outputs.sql` Fix insert into ClickHouse
- [#16454](https://github.com/influxdata/telegraf/pull/16454) `service` Set address to prevent orphaned dbus-session processes

### Dependency updates

- [#16442](https://github.com/influxdata/telegraf/pull/16442) `deps` Bump cloud.google.com/go/storage from 1.47.0 to 1.50.0
- [#16414](https://github.com/influxdata/telegraf/pull/16414) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/azidentity from 1.7.0 to 1.8.1
- [#16416](https://github.com/influxdata/telegraf/pull/16416) `deps` Bump github.com/apache/iotdb-client-go from 1.3.2 to 1.3.3
- [#16415](https://github.com/influxdata/telegraf/pull/16415) `deps` Bump github.com/aws/aws-sdk-go-v2 from 1.32.8 to 1.33.0
- [#16394](https://github.com/influxdata/telegraf/pull/16394) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs from 1.38.0 to 1.45.3
- [#16468](https://github.com/influxdata/telegraf/pull/16468) `deps` Bump github.com/aws/aws-sdk-go-v2/service/sts from 1.33.10 to 1.33.12
- [#16439](https://github.com/influxdata/telegraf/pull/16439) `deps` Bump github.com/aws/aws-sdk-go-v2/service/sts from 1.33.2 to 1.33.10
- [#16395](https://github.com/influxdata/telegraf/pull/16395) `deps` Bump github.com/eclipse/paho.golang from 0.21.0 to 0.22.0
- [#16470](https://github.com/influxdata/telegraf/pull/16470) `deps` Bump github.com/go-ldap/ldap/v3 from 3.4.8 to 3.4.10
- [#16440](https://github.com/influxdata/telegraf/pull/16440) `deps` Bump github.com/google/cel-go from 0.21.0 to 0.23.0
- [#16445](https://github.com/influxdata/telegraf/pull/16445) `deps` Bump github.com/lxc/incus/v6 from 6.6.0 to 6.9.0
- [#16466](https://github.com/influxdata/telegraf/pull/16466) `deps` Bump github.com/nats-io/nats-server/v2 from 2.10.17 to 2.10.25
- [#16453](https://github.com/influxdata/telegraf/pull/16453) `deps` Bump github.com/prometheus/common from 0.61.0 to 0.62.0
- [#16417](https://github.com/influxdata/telegraf/pull/16417) `deps` Bump github.com/shirou/gopsutil/v4 from 4.24.10 to 4.24.12
- [#16369](https://github.com/influxdata/telegraf/pull/16369) `deps` Bump github.com/shirou/gopsutil/v4 from v4.24.10 to v4.24.12
- [#16397](https://github.com/influxdata/telegraf/pull/16397) `deps` Bump github.com/showwin/speedtest-go from 1.7.9 to 1.7.10
- [#16467](https://github.com/influxdata/telegraf/pull/16467) `deps` Bump github.com/yuin/goldmark from 1.6.0 to 1.7.8
- [#16360](https://github.com/influxdata/telegraf/pull/16360) `deps` Bump golangci-lint from v1.62.2 to v1.63.4
- [#16469](https://github.com/influxdata/telegraf/pull/16469) `deps` Bump google.golang.org/api from 0.214.0 to 0.219.0
- [#16396](https://github.com/influxdata/telegraf/pull/16396) `deps` Bump k8s.io/api from 0.31.3 to 0.32.1
- [#16482](https://github.com/influxdata/telegraf/pull/16482) `deps` Update Apache arrow from 0.0-20240716144821-cf5d7c7ec3cf to 18.1.0
- [#16423](https://github.com/influxdata/telegraf/pull/16423) `deps` Update ClickHouse SQL driver from 1.5.4 to to 2.30.1

## v1.33.1

### Important Changes

- The default value of `skip_processors_after_aggregators` will change to `true` with Telegraf `v1.40.0`, skip running the processors again after aggregators! If you need the current default behavior, please explicitly set the option to `false`! To silence the warning and use the future default behavior, please explicitly set the option to `true`.

### Bug fixes

- [#16290](https://github.com/influxdata/telegraf/pull/16290) `agent` Skip initialization of second processor state if requested
- [#16377](https://github.com/influxdata/telegraf/pull/16377) `inputs.intel_powerstat` Fix option removal version
- [#16310](https://github.com/influxdata/telegraf/pull/16310) `inputs.mongodb` Do not dereference nil pointer if gathering database stats fails
- [#16383](https://github.com/influxdata/telegraf/pull/16383) `outputs.influxdb_v2` Allow overriding auth and agent headers
- [#16388](https://github.com/influxdata/telegraf/pull/16388) `outputs.influxdb_v2` Fix panic and API error handling
- [#16289](https://github.com/influxdata/telegraf/pull/16289) `outputs.remotefile` Handle tracking metrics correctly

### Dependency updates

- [#16344](https://github.com/influxdata/telegraf/pull/16344) `deps` Bump cloud.google.com/go/bigquery from 1.64.0 to 1.65.0
- [#16283](https://github.com/influxdata/telegraf/pull/16283) `deps` Bump cloud.google.com/go/monitoring from 1.21.1 to 1.22.0
- [#16315](https://github.com/influxdata/telegraf/pull/16315) `deps` Bump github.com/Azure/go-autorest/autorest/adal from 0.9.23 to 0.9.24
- [#16319](https://github.com/influxdata/telegraf/pull/16319) `deps` Bump github.com/IBM/nzgo/v12 from 12.0.9-0.20231115043259-49c27f2dfe48 to 12.0.9
- [#16346](https://github.com/influxdata/telegraf/pull/16346) `deps` Bump github.com/Masterminds/semver/v3 from 3.3.0 to 3.3.1
- [#16280](https://github.com/influxdata/telegraf/pull/16280) `deps` Bump github.com/aws/aws-sdk-go-v2/config from 1.27.39 to 1.28.6
- [#16343](https://github.com/influxdata/telegraf/pull/16343) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.162.1 to 1.198.1
- [#16317](https://github.com/influxdata/telegraf/pull/16317) `deps` Bump github.com/fatih/color from 1.17.0 to 1.18.0
- [#16345](https://github.com/influxdata/telegraf/pull/16345) `deps` Bump github.com/gopacket/gopacket from 1.3.0 to 1.3.1
- [#16282](https://github.com/influxdata/telegraf/pull/16282) `deps` Bump github.com/nats-io/nats.go from 1.36.0 to 1.37.0
- [#16318](https://github.com/influxdata/telegraf/pull/16318) `deps` Bump github.com/prometheus/common from 0.60.0 to 0.61.0
- [#16324](https://github.com/influxdata/telegraf/pull/16324) `deps` Bump github.com/vapourismo/knx-go from v0.0.0-20240217175130-922a0d50c241 to v0.0.0-20240915133544-a6ab43471c11
- [#16297](https://github.com/influxdata/telegraf/pull/16297) `deps` Bump golang.org/x/crypto from 0.29.0 to 0.31.0
- [#16281](https://github.com/influxdata/telegraf/pull/16281) `deps` Bump k8s.io/client-go from 0.30.1 to 0.31.3
- [#16313](https://github.com/influxdata/telegraf/pull/16313) `deps` Bump super-linter/super-linter from 7.2.0 to 7.2.1

## v1.33.0

### New Plugins

- [#15754](https://github.com/influxdata/telegraf/pull/15754) `inputs.neoom_beaam` Add new plugin
- [#15869](https://github.com/influxdata/telegraf/pull/15869) `processors.batch` Add batch processor
- [#16144](https://github.com/influxdata/telegraf/pull/16144) `outputs.quix` Add plugin

### Features

- [#16010](https://github.com/influxdata/telegraf/pull/16010) `agent` Add –watch-interval option for polling config changes
- [#15948](https://github.com/influxdata/telegraf/pull/15948) `aggregators.basicstats` Add first field
- [#15891](https://github.com/influxdata/telegraf/pull/15891) `common.socket` Allow parallel parsing with a pool of workers
- [#16141](https://github.com/influxdata/telegraf/pull/16141) `inputs.amqp_consumer` Allow specification of queue arguments
- [#15950](https://github.com/influxdata/telegraf/pull/15950) `inputs.diskio` Add field io await and util
- [#15919](https://github.com/influxdata/telegraf/pull/15919) `inputs.kafka_consumer` Implement startup error behavior options
- [#15910](https://github.com/influxdata/telegraf/pull/15910) `inputs.memcached` Add support for external-store metrics
- [#15990](https://github.com/influxdata/telegraf/pull/15990) `inputs.mock` Add sine phase
- [#16040](https://github.com/influxdata/telegraf/pull/16040) `inputs.modbus` Allow grouping across register types
- [#15865](https://github.com/influxdata/telegraf/pull/15865) `inputs.prometheus` Allow to use secrets for credentials
- [#16230](https://github.com/influxdata/telegraf/pull/16230) `inputs.smart` Add Power on Hours and Cycle Count
- [#15935](https://github.com/influxdata/telegraf/pull/15935) `inputs.snmp` Add displayhint conversion
- [#16027](https://github.com/influxdata/telegraf/pull/16027) `inputs.snmp` Convert uneven bytes to int
- [#15976](https://github.com/influxdata/telegraf/pull/15976) `inputs.socket_listener` Use reception time as timestamp
- [#15853](https://github.com/influxdata/telegraf/pull/15853) `inputs.statsd` Allow reporting sets and timings count as floats
- [#11591](https://github.com/influxdata/telegraf/pull/11591) `inputs.vsphere` Add VM memory configuration
- [#16109](https://github.com/influxdata/telegraf/pull/16109) `inputs.vsphere` Add cpu temperature field
- [#15917](https://github.com/influxdata/telegraf/pull/15917) `inputs` Add option to choose the metric time source
- [#16242](https://github.com/influxdata/telegraf/pull/16242) `logging` Allow overriding message key for structured logging
- [#15742](https://github.com/influxdata/telegraf/pull/15742) `outputs.influxdb_v2` Add rate limit implementation
- [#15943](https://github.com/influxdata/telegraf/pull/15943) `outputs.mqtt` Add sprig functions for topic name generator
- [#16041](https://github.com/influxdata/telegraf/pull/16041) `outputs.postgresql` Allow limiting of column name length
- [#16258](https://github.com/influxdata/telegraf/pull/16258) `outputs` Add rate-limiting infrastructure
- [#16146](https://github.com/influxdata/telegraf/pull/16146) `outputs` Implement partial write errors
- [#15883](https://github.com/influxdata/telegraf/pull/15883) `outputs` Only copy metric if its not filtered out
- [#15893](https://github.com/influxdata/telegraf/pull/15893) `serializers.prometheusremotewrite` Log metric conversion errors

### Bug fixes

- [#16248](https://github.com/influxdata/telegraf/pull/16248) `inputs.netflow` Decode flags in TCP and IP headers correctly
- [#16257](https://github.com/influxdata/telegraf/pull/16257) `inputs.procstat` Handle running processes correctly across multiple filters
- [#16219](https://github.com/influxdata/telegraf/pull/16219) `logging` Add `Close()` func for redirectLogger
- [#16255](https://github.com/influxdata/telegraf/pull/16255) `logging` Clean up extra empty spaces when redirectLogger is used
- [#16274](https://github.com/influxdata/telegraf/pull/16274) `logging` Fix duplicated prefix and attrMsg in log message when redirectLogger is used

### Dependency updates

- [#16232](https://github.com/influxdata/telegraf/pull/16232) `deps` Bump cloud.google.com/go/bigquery from 1.63.1 to 1.64.0
- [#16235](https://github.com/influxdata/telegraf/pull/16235) `deps` Bump cloud.google.com/go/storage from 1.43.0 to 1.47.0
- [#16198](https://github.com/influxdata/telegraf/pull/16198) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatch from 1.42.2 to 1.43.1
- [#16234](https://github.com/influxdata/telegraf/pull/16234) `deps` Bump github.com/aws/aws-sdk-go-v2/service/kinesis from 1.29.3 to 1.32.6
- [#16201](https://github.com/influxdata/telegraf/pull/16201) `deps` Bump github.com/intel/powertelemetry from 1.0.1 to 1.0.2
- [#16200](https://github.com/influxdata/telegraf/pull/16200) `deps` Bump github.com/rclone/rclone from 1.68.1 to 1.68.2
- [#16199](https://github.com/influxdata/telegraf/pull/16199) `deps` Bump github.com/vishvananda/netns from 0.0.4 to 0.0.5
- [#16236](https://github.com/influxdata/telegraf/pull/16236) `deps` Bump golang.org/x/net from 0.30.0 to 0.31.0
- [#16250](https://github.com/influxdata/telegraf/pull/16250) `deps` Bump golangci-lint from v1.62.0 to v1.62.2
- [#16233](https://github.com/influxdata/telegraf/pull/16233) `deps` Bump google.golang.org/grpc from 1.67.1 to 1.68.0
- [#16202](https://github.com/influxdata/telegraf/pull/16202) `deps` Bump modernc.org/sqlite from 1.33.1 to 1.34.1
- [#16203](https://github.com/influxdata/telegraf/pull/16203) `deps` Bump super-linter/super-linter from 7.1.0 to 7.2.0

## v1.32.3

### Important Changes

- PR [#16015](https://github.com/influxdata/telegraf/pull/16015) changes the internal counters of the Bind plugin to unsigned integers (as in the server implementation). For backward compatibility, `report_counters_as_int` is `true` by default to avoid type conflicts on the output side. *However, you should set `report_counters_as_int` to `false` as soon as possible to avoid invalid values and parsing errors with the v3 XML statistics.*

### Bug fixes

- [#16123](https://github.com/influxdata/telegraf/pull/16123) `agent` Restore setup order of stateful plugins to `Init()` then `SetState()`
- [#16111](https://github.com/influxdata/telegraf/pull/16111) `common.socket` Make sure the scanner buffer matches the read-buffer size
- [#16156](https://github.com/influxdata/telegraf/pull/16156) `common.socket` Use read buffer size config setting as a datagram reader buffer size
- [#16015](https://github.com/influxdata/telegraf/pull/16015) `inputs.bind` Convert counters to uint64
- [#16171](https://github.com/influxdata/telegraf/pull/16171) `inputs.gnmi` Register connection statistics before creating client
- [#16197](https://github.com/influxdata/telegraf/pull/16197) `inputs.netflow` Cast TCP ports to uint16
- [#16110](https://github.com/influxdata/telegraf/pull/16110) `inputs.ntpq` Avoid panic on empty lines and make sure -p is present
- [#16155](https://github.com/influxdata/telegraf/pull/16155) `inputs.snmp` Fix crash when trying to format fields from unknown OIDs
- [#16145](https://github.com/influxdata/telegraf/pull/16145) `inputs.snmp_trap` Remove timeout deprecation
- [#16108](https://github.com/influxdata/telegraf/pull/16108) `logger` Avoid setting the log-format default too early

### Dependency updates

- [#16093](https://github.com/influxdata/telegraf/pull/16093) `deps` Bump cloud.google.com/go/pubsub from 1.42.0 to 1.45.1
- [#16175](https://github.com/influxdata/telegraf/pull/16175) `deps` Bump github.com/aws/aws-sdk-go-v2/credentials from 1.17.37 to 1.17.44
- [#16096](https://github.com/influxdata/telegraf/pull/16096) `deps` Bump github.com/gofrs/uuid/v5 from 5.2.0 to 5.3.0
- [#16136](https://github.com/influxdata/telegraf/pull/16136) `deps` Bump github.com/golang-jwt/jwt/v4 from 4.5.0 to 4.5.1
- [#16094](https://github.com/influxdata/telegraf/pull/16094) `deps` Bump github.com/gopacket/gopacket from 1.2.0 to 1.3.0
- [#16133](https://github.com/influxdata/telegraf/pull/16133) `deps` Bump github.com/jackc/pgtype from 1.14.3 to 1.14.4
- [#16131](https://github.com/influxdata/telegraf/pull/16131) `deps` Bump github.com/openconfig/gnmi from 0.10.0 to 0.11.0
- [#16092](https://github.com/influxdata/telegraf/pull/16092) `deps` Bump github.com/prometheus/client\_golang from 1.20.4 to 1.20.5
- [#16178](https://github.com/influxdata/telegraf/pull/16178) `deps` Bump github.com/rclone/rclone from 1.67.0 to 1.68.1
- [#16132](https://github.com/influxdata/telegraf/pull/16132) `deps` Bump github.com/shirou/gopsutil/v4 from 4.24.9 to 4.24.10
- [#16176](https://github.com/influxdata/telegraf/pull/16176) `deps` Bump github.com/sijms/go-ora/v2 from 2.8.19 to 2.8.22
- [#16134](https://github.com/influxdata/telegraf/pull/16134) `deps` Bump github.com/testcontainers/testcontainers-go/modules/kafka from 0.33.0 to 0.34.0
- [#16174](https://github.com/influxdata/telegraf/pull/16174) `deps` Bump github.com/tidwall/gjson from 1.17.1 to 1.18.0
- [#16135](https://github.com/influxdata/telegraf/pull/16135) `deps` Bump github.com/vmware/govmomi from 0.39.0 to 0.45.1
- [#16095](https://github.com/influxdata/telegraf/pull/16095) `deps` Bump golang.org/x/sys from 0.25.0 to 0.26.0
- [#16177](https://github.com/influxdata/telegraf/pull/16177) `deps` Bump golang.org/x/text from 0.19.0 to 0.20.0
- [#16172](https://github.com/influxdata/telegraf/pull/16172) `deps` Bump golangci-lint from v1.61.0 to v1.62.0

## v1.32.2

### Bug fixes

- [#15966](https://github.com/influxdata/telegraf/pull/15966) `agent` Use a unique WAL file for plugin instances of the same type
- [#16074](https://github.com/influxdata/telegraf/pull/16074) `inputs.kafka_consumer` Fix deadlock
- [#16009](https://github.com/influxdata/telegraf/pull/16009) `inputs.netflow` Cast complex types to field compatible ones
- [#16026](https://github.com/influxdata/telegraf/pull/16026) `inputs.opcua` Allow to retry reads on invalid sessions
- [#16060](https://github.com/influxdata/telegraf/pull/16060) `inputs.procstat` Correctly use systemd-unit setting for finding them
- [#16008](https://github.com/influxdata/telegraf/pull/16008) `inputs.win_eventlog` Handle XML data fields’ filtering the same way as event fields
- [#15968](https://github.com/influxdata/telegraf/pull/15968) `outputs.remotefile` Create a new serializer instance per output file
- [#16014](https://github.com/influxdata/telegraf/pull/16014) `outputs.syslog` Trim field-names belonging to explicit SDIDs correctly

### Dependency updates

- [#15992](https://github.com/influxdata/telegraf/pull/15992) `deps` Bump cloud.google.com/go/bigquery from 1.62.0 to 1.63.1
- [#16056](https://github.com/influxdata/telegraf/pull/16056) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/azcore from 1.14.0 to 1.16.0
- [#16021](https://github.com/influxdata/telegraf/pull/16021) `deps` Bump github.com/IBM/sarama from 1.43.2 to 1.43.3
- [#16019](https://github.com/influxdata/telegraf/pull/16019) `deps` Bump github.com/alitto/pond from 1.9.0 to 1.9.2
- [#16018](https://github.com/influxdata/telegraf/pull/16018) `deps` Bump github.com/apache/thrift from 0.20.0 to 0.21.0
- [#16054](https://github.com/influxdata/telegraf/pull/16054) `deps` Bump github.com/aws/aws-sdk-go-v2 from 1.32.1 to 1.32.2
- [#15996](https://github.com/influxdata/telegraf/pull/15996) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatch from 1.40.4 to 1.42.1
- [#16055](https://github.com/influxdata/telegraf/pull/16055) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatch from 1.42.1 to 1.42.2
- [#16057](https://github.com/influxdata/telegraf/pull/16057) `deps` Bump github.com/aws/aws-sdk-go-v2/service/dynamodb from 1.34.9 to 1.36.2
- [#16022](https://github.com/influxdata/telegraf/pull/16022) `deps` Bump github.com/docker/docker from 27.1.1+incompatible to 27.3.1+incompatible
- [#15993](https://github.com/influxdata/telegraf/pull/15993) `deps` Bump github.com/gosnmp/gosnmp from 1.37.0 to 1.38.0
- [#15947](https://github.com/influxdata/telegraf/pull/15947) `deps` Bump github.com/gwos/tcg/sdk from v8.7.2 to v8.8.0
- [#16053](https://github.com/influxdata/telegraf/pull/16053) `deps` Bump github.com/lxc/incus/v6 from 6.2.0 to 6.6.0
- [#15994](https://github.com/influxdata/telegraf/pull/15994) `deps` Bump github.com/signalfx/golib/v3 from 3.3.53 to 3.3.54
- [#15995](https://github.com/influxdata/telegraf/pull/15995) `deps` Bump github.com/snowflakedb/gosnowflake from 1.11.1 to 1.11.2
- [#16020](https://github.com/influxdata/telegraf/pull/16020) `deps` Bump go.step.sm/crypto from 0.51.1 to 0.54.0
- [#16023](https://github.com/influxdata/telegraf/pull/16023) `deps` Bump github.com/shirou/gopsutil from v3.24.4 to v4.24.9

## v1.32.1

### Important Changes

- PR [#15796](https://github.com/influxdata/telegraf/pull/15796) changes the delivery state update of un-parseable messages from `ACK` to `NACK` without requeueing. This way, those messages are not lost and can optionally be handled using a dead-letter exchange by other means.
- Removal of old-style serializer creation. This should not directly affect users as it is an API change; all serializers in Telegraf are already ported to the new framework. If you experience any issues creating serializers, [contact us](/telegraf/v1/#bug-reports-and-feedback).

### Bug fixes

- [#15969](https://github.com/influxdata/telegraf/pull/15969) `agent` Fix buffer not flushing if all metrics are written
- [#15937](https://github.com/influxdata/telegraf/pull/15937) `config` Correctly print removal version info
- [#15900](https://github.com/influxdata/telegraf/pull/15900) `common.http` Keep timeout after creating oauth client
- [#15796](https://github.com/influxdata/telegraf/pull/15796) `inputs.amqp_consumer` NACKing messages on non-delivery related errors
- [#15923](https://github.com/influxdata/telegraf/pull/15923) `inputs.cisco_telemetry_mdt` Handle NXOS DME subtree telemetry format
- [#15907](https://github.com/influxdata/telegraf/pull/15907) `inputs.consul` Move config checking to Init method
- [#15982](https://github.com/influxdata/telegraf/pull/15982) `inputs.influxdb_v2_listener` Fix concurrent read/write dict
- [#15960](https://github.com/influxdata/telegraf/pull/15960) `inputs.vsphere` Add tags to VSAN ESA disks
- [#15921](https://github.com/influxdata/telegraf/pull/15921) `parsers.avro` Add mutex to cache access
- [#15965](https://github.com/influxdata/telegraf/pull/15965) `processors.aws_ec2` Remove leading slash and cancel worker only if it exists

### Dependency updates

- [#15932](https://github.com/influxdata/telegraf/pull/15932) `deps` Bump cloud.google.com/go/monitoring from 1.20.2 to 1.21.1
- [#15863](https://github.com/influxdata/telegraf/pull/15863) `deps` Bump github.com/Azure/azure-kusto-go from 0.15.3 to 0.16.1
- [#15862](https://github.com/influxdata/telegraf/pull/15862) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/azcore from 1.13.0 to 1.14.0
- [#15957](https://github.com/influxdata/telegraf/pull/15957) `deps` Bump github.com/aws/aws-sdk-go-v2/feature/ec2/imds from 1.16.12 to 1.16.14
- [#15859](https://github.com/influxdata/telegraf/pull/15859) `deps` Bump github.com/aws/aws-sdk-go-v2/service/dynamodb from 1.34.4 to 1.34.9
- [#15931](https://github.com/influxdata/telegraf/pull/15931) `deps` Bump github.com/boschrexroth/ctrlx-datalayer-golang from 1.3.0 to 1.3.1
- [#15890](https://github.com/influxdata/telegraf/pull/15890) `deps` Bump github.com/harlow/kinesis-consumer from v0.3.6-0.20240606153816-553e2392fdf3 to v0.3.6-0.20240916192723-43900507c911
- [#15904](https://github.com/influxdata/telegraf/pull/15904) `deps` Bump github.com/netsampler/goflow2/v2 from 2.1.5 to 2.2.1
- [#15903](https://github.com/influxdata/telegraf/pull/15903) `deps` Bump github.com/p4lang/p4runtime from 1.3.0 to 1.4.0
- [#15905](https://github.com/influxdata/telegraf/pull/15905) `deps` Bump github.com/prometheus/client\_golang from 1.20.2 to 1.20.3
- [#15930](https://github.com/influxdata/telegraf/pull/15930) `deps` Bump github.com/prometheus/client\_golang from 1.20.3 to 1.20.4
- [#15962](https://github.com/influxdata/telegraf/pull/15962) `deps` Bump github.com/prometheus/common from 0.55.0 to 0.60.0
- [#15860](https://github.com/influxdata/telegraf/pull/15860) `deps` Bump github.com/snowflakedb/gosnowflake from 1.10.0 to 1.11.1
- [#15954](https://github.com/influxdata/telegraf/pull/15954) `deps` Bump github.com/srebhan/protobufquery from 0.0.0-20230803132024-ae4c0d878e55 to 1.0.1
- [#15929](https://github.com/influxdata/telegraf/pull/15929) `deps` Bump go.mongodb.org/mongo-driver from 1.16.0 to 1.17.0
- [#15902](https://github.com/influxdata/telegraf/pull/15902) `deps` Bump golang.org/x/mod from 0.19.0 to 0.21.0
- [#15955](https://github.com/influxdata/telegraf/pull/15955) `deps` Bump golang.org/x/oauth2 from 0.21.0 to 0.23.0
- [#15861](https://github.com/influxdata/telegraf/pull/15861) `deps` Bump golang.org/x/term from 0.23.0 to 0.24.0
- [#15856](https://github.com/influxdata/telegraf/pull/15856) `deps` Bump golangci-lint from v1.60.3 to v1.61.0
- [#15933](https://github.com/influxdata/telegraf/pull/15933) `deps` Bump k8s.io/apimachinery from 0.30.1 to 0.31.1
- [#15901](https://github.com/influxdata/telegraf/pull/15901) `deps` Bump modernc.org/sqlite from 1.32.0 to 1.33.1

## v1.32.0

### Important Changes

- This release contains a logging overhaul as well as some new features for logging (see PRs [#15556](https://github.com/influxdata/telegraf/pull/15556), [#15629](https://github.com/influxdata/telegraf/pull/15629), [#15677](https://github.com/influxdata/telegraf/pull/15677), [#15695](https://github.com/influxdata/telegraf/pull/15695) and [#15751](https://github.com/influxdata/telegraf/pull/15751)). As a consequence, the redundant `logtarget` setting is deprecated. `stderr` is used if no `logfile` is provided, otherwise messages are logged to the given file. To use Windows `eventlog`, set `logformat = "eventlog"`.
- This release contains a change in json\_v2 parser config parsing: if the config is empty (doesn’t define any rules), initialization will fail (see PR [#15844](https://github.com/influxdata/telegraf/pull/15844)).
- This release contains a feature for a disk-backed metric buffer under the `buffer_strategy` agent config (see PR [#15564](https://github.com/influxdata/telegraf/pull/15564)). *This feature is **experimental**. Please report any issues you encounter while using it.*

### New Plugins

- [#15700](https://github.com/influxdata/telegraf/pull/15700) `inputs.slurm` SLURM workload manager
- [#15602](https://github.com/influxdata/telegraf/pull/15602) `outputs.parquet` Parquet file writer
- [#15569](https://github.com/influxdata/telegraf/pull/15569) `outputs.remotefile` Output to remote location like S3

### Features

- [#15732](https://github.com/influxdata/telegraf/pull/15732) `agent` Add config check sub-command
- [#15564](https://github.com/influxdata/telegraf/pull/15564) `agent` Add metric disk buffer
- [#15645](https://github.com/influxdata/telegraf/pull/15645) `agent` Enable watching for new configuration files
- [#15644](https://github.com/influxdata/telegraf/pull/15644) `agent` Watch for deleted files
- [#15695](https://github.com/influxdata/telegraf/pull/15695) `logging` Add ’trace’ log-level
- [#15677](https://github.com/influxdata/telegraf/pull/15677) `logging` Allow to override log-level per plugin
- [#15751](https://github.com/influxdata/telegraf/pull/15751) `logging` Implement structured logging
- [#15640](https://github.com/influxdata/telegraf/pull/15640) `common.cookie` Allow usage of secrets in headers
- [#15636](https://github.com/influxdata/telegraf/pull/15636) `common.shim` Enable metric tracking within external plugins
- [#15570](https://github.com/influxdata/telegraf/pull/15570) `common.tls` Allow group aliases for cipher-suites
- [#15628](https://github.com/influxdata/telegraf/pull/15628) `inputs.amd_rocm_smi` Parse newer ROCm versions
- [#15519](https://github.com/influxdata/telegraf/pull/15519) `inputs.azure_monitor` Add client options parameter
- [#15544](https://github.com/influxdata/telegraf/pull/15544) `inputs.elasticsearch` Add support for custom headers
- [#15688](https://github.com/influxdata/telegraf/pull/15688) `inputs.elasticsearch` Gather enrich stats
- [#15834](https://github.com/influxdata/telegraf/pull/15834) `inputs.execd` Allow to provide logging prefixes on stderr
- [#15764](https://github.com/influxdata/telegraf/pull/15764) `inputs.http_listener_v2` Add unix socket mode
- [#15495](https://github.com/influxdata/telegraf/pull/15495) `inputs.ipmi_sensor` Collect additional commands
- [#15790](https://github.com/influxdata/telegraf/pull/15790) `inputs.kafka_consumer` Allow to select the metric time source
- [#15648](https://github.com/influxdata/telegraf/pull/15648) `inputs.modbus` Allow reading single bits of input and holding registers
- [#15528](https://github.com/influxdata/telegraf/pull/15528) `inputs.mqtt_consumer` Add variable length topic parsing
- [#15486](https://github.com/influxdata/telegraf/pull/15486) `inputs.mqtt_consumer` Implement startup error behaviors
- [#15749](https://github.com/influxdata/telegraf/pull/15749) `inputs.mysql` Add support for replica status
- [#15521](https://github.com/influxdata/telegraf/pull/15521) `inputs.netflow` Add more fields for sFlow extended gateway packets
- [#15396](https://github.com/influxdata/telegraf/pull/15396) `inputs.netflow` Add support for sFlow drop notification packets
- [#15468](https://github.com/influxdata/telegraf/pull/15468) `inputs.openstack` Allow collection without admin privileges
- [#15637](https://github.com/influxdata/telegraf/pull/15637) `inputs.opentelemetry` Add profiles support
- [#15423](https://github.com/influxdata/telegraf/pull/15423) `inputs.procstat` Add ability to collect per-process socket statistics
- [#15655](https://github.com/influxdata/telegraf/pull/15655) `inputs.s7comm` Implement startup-error behavior settings
- [#15600](https://github.com/influxdata/telegraf/pull/15600) `inputs.sql` Add SAP HANA SQL driver
- [#15424](https://github.com/influxdata/telegraf/pull/15424) `inputs.sqlserver` Introduce user specified ID parameter for ADD logins
- [#15687](https://github.com/influxdata/telegraf/pull/15687) `inputs.statsd` Expose allowed\_pending\_messages as internal stat
- [#15458](https://github.com/influxdata/telegraf/pull/15458) `inputs.systemd_units` Support user scoped units
- [#15702](https://github.com/influxdata/telegraf/pull/15702) `outputs.datadog` Add support for submitting alongside dd-agent
- [#15668](https://github.com/influxdata/telegraf/pull/15668) `outputs.dynatrace` Report metrics as a delta counter using regular expression
- [#15471](https://github.com/influxdata/telegraf/pull/15471) `outputs.elasticsearch` Allow custom template index settings
- [#15613](https://github.com/influxdata/telegraf/pull/15613) `outputs.elasticsearch` Support data streams
- [#15722](https://github.com/influxdata/telegraf/pull/15722) `outputs.kafka` Add option to add metric name as record header
- [#15689](https://github.com/influxdata/telegraf/pull/15689) `outputs.kafka` Add option to set producer message timestamp
- [#15787](https://github.com/influxdata/telegraf/pull/15787) `outputs.syslog` Implement startup error behavior options
- [#15697](https://github.com/influxdata/telegraf/pull/15697) `parsers.value` Add base64 datatype
- [#15795](https://github.com/influxdata/telegraf/pull/15795) `processors.aws_ec2` Allow to use instance metadata

### Bug fixes

- [#15661](https://github.com/influxdata/telegraf/pull/15661) `agent` Fix buffer directory config and document
- [#15788](https://github.com/influxdata/telegraf/pull/15788) `inputs.kinesis_consumer` Honor the configured endpoint
- [#15791](https://github.com/influxdata/telegraf/pull/15791) `inputs.mysql` Enforce float for all known floating-point information
- [#15743](https://github.com/influxdata/telegraf/pull/15743) `inputs.snmp` Avoid sending a nil to gosmi’s GetEnumBitsFormatted
- [#15815](https://github.com/influxdata/telegraf/pull/15815) `logger` Handle trace level for standard log
- [#15781](https://github.com/influxdata/telegraf/pull/15781) `outputs.kinesis` Honor the configured endpoint
- [#15615](https://github.com/influxdata/telegraf/pull/15615) `outputs.remotefile` Resolve linter not checking error
- [#15740](https://github.com/influxdata/telegraf/pull/15740) `serializers.template` Unwrap metrics if required

### Dependency updates

- [#15829](https://github.com/influxdata/telegraf/pull/15829) `deps` Bump github.com/BurntSushi/toml from 1.3.2 to 1.4.0
- [#15775](https://github.com/influxdata/telegraf/pull/15775) `deps` Bump github.com/aws/aws-sdk-go-v2/feature/ec2/imds from 1.16.11 to 1.16.12
- [#15733](https://github.com/influxdata/telegraf/pull/15733) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatch from 1.38.7 to 1.40.3
- [#15761](https://github.com/influxdata/telegraf/pull/15761) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatch from 1.40.3 to 1.40.4
- [#15827](https://github.com/influxdata/telegraf/pull/15827) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs from 1.37.3 to 1.38.0
- [#15760](https://github.com/influxdata/telegraf/pull/15760) `deps` Bump github.com/aws/aws-sdk-go-v2/service/timestreamwrite from 1.25.5 to 1.27.4
- [#15737](https://github.com/influxdata/telegraf/pull/15737) `deps` Bump github.com/eclipse/paho.mqtt.golang from 1.4.3 to 1.5.0
- [#15734](https://github.com/influxdata/telegraf/pull/15734) `deps` Bump github.com/google/cel-go from 0.20.1 to 0.21.0
- [#15777](https://github.com/influxdata/telegraf/pull/15777) `deps` Bump github.com/miekg/dns from 1.1.59 to 1.1.62
- [#15828](https://github.com/influxdata/telegraf/pull/15828) `deps` Bump github.com/openconfig/goyang from 1.5.0 to 1.6.0
- [#15735](https://github.com/influxdata/telegraf/pull/15735) `deps` Bump github.com/pion/dtls/v2 from 2.2.11 to 2.2.12
- [#15779](https://github.com/influxdata/telegraf/pull/15779) `deps` Bump github.com/prometheus/client\_golang from 1.19.1 to 1.20.2
- [#15831](https://github.com/influxdata/telegraf/pull/15831) `deps` Bump github.com/prometheus/prometheus from 0.53.1 to 0.54.1
- [#15736](https://github.com/influxdata/telegraf/pull/15736) `deps` Bump github.com/redis/go-redis/v9 from 9.5.1 to 9.6.1
- [#15830](https://github.com/influxdata/telegraf/pull/15830) `deps` Bump github.com/seancfoley/ipaddress-go from 1.6.0 to 1.7.0
- [#15842](https://github.com/influxdata/telegraf/pull/15842) `deps` Bump github.com/showwin/speedtest-go from 1.7.7 to 1.7.9
- [#15778](https://github.com/influxdata/telegraf/pull/15778) `deps` Bump go.step.sm/crypto from 0.50.0 to 0.51.1
- [#15776](https://github.com/influxdata/telegraf/pull/15776) `deps` Bump golang.org/x/net from 0.27.0 to 0.28.0
- [#15757](https://github.com/influxdata/telegraf/pull/15757) `deps` Bump golang.org/x/sync from 0.7.0 to 0.8.0
- [#15759](https://github.com/influxdata/telegraf/pull/15759) `deps` Bump gonum.org/v1/gonum from 0.15.0 to 0.15.1
- [#15758](https://github.com/influxdata/telegraf/pull/15758) `deps` Bump modernc.org/sqlite from 1.30.0 to 1.32.0
- [#15756](https://github.com/influxdata/telegraf/pull/15756) `deps` Bump super-linter/super-linter from 6.8.0 to 7.0.0
- [#15826](https://github.com/influxdata/telegraf/pull/15826) `deps` Bump super-linter/super-linter from 7.0.0 to 7.1.0
- [#15780](https://github.com/influxdata/telegraf/pull/15780) `deps` Bump tj-actions/changed-files from 44 to 45

## v1.31.3

### Bug fixes

- [#15552](https://github.com/influxdata/telegraf/pull/15552) `inputs.chrony` Use DGRAM for the unix socket
- [#15667](https://github.com/influxdata/telegraf/pull/15667) `inputs.diskio` Print warnings once, add details to messages
- [#15670](https://github.com/influxdata/telegraf/pull/15670) `inputs.mqtt_consumer` Restore trace logging option
- [#15696](https://github.com/influxdata/telegraf/pull/15696) `inputs.opcua` Reconnect if closed connection
- [#15724](https://github.com/influxdata/telegraf/pull/15724) `inputs.smartctl` Use –scan-open instead of –scan to provide correct device type info
- [#15649](https://github.com/influxdata/telegraf/pull/15649) `inputs.tail` Prevent deadlock when closing and max undelivered lines hit

### Dependency updates

- [#15720](https://github.com/influxdata/telegraf/pull/15720) `deps` Bump Go from v1.22.5 to v1.22.6
- [#15683](https://github.com/influxdata/telegraf/pull/15683) `deps` Bump cloud.google.com/go/bigquery from 1.61.0 to 1.62.0
- [#15654](https://github.com/influxdata/telegraf/pull/15654) `deps` Bump cloud.google.com/go/monitoring from 1.19.0 to 1.20.2
- [#15679](https://github.com/influxdata/telegraf/pull/15679) `deps` Bump cloud.google.com/go/monitoring from 1.20.2 to 1.20.3
- [#15626](https://github.com/influxdata/telegraf/pull/15626) `deps` Bump github.com/antchfx/xmlquery from 1.4.0 to 1.4.1
- [#15706](https://github.com/influxdata/telegraf/pull/15706) `deps` Bump github.com/apache/iotdb-client-go from 1.2.0-tsbs to 1.3.2
- [#15651](https://github.com/influxdata/telegraf/pull/15651) `deps` Bump github.com/aws/aws-sdk-go-v2/credentials from 1.17.17 to 1.17.27
- [#15703](https://github.com/influxdata/telegraf/pull/15703) `deps` Bump github.com/aws/aws-sdk-go-v2/service/kinesis from v1.27.4 to v1.29.3
- [#15681](https://github.com/influxdata/telegraf/pull/15681) `deps` Bump github.com/docker/docker from 25.0.5-incompatible to 27.1.1-incompatible
- [#15650](https://github.com/influxdata/telegraf/pull/15650) `deps` Bump github.com/gofrs/uuid/v5 from 5.0.0 to 5.2.0
- [#15705](https://github.com/influxdata/telegraf/pull/15705) `deps` Bump github.com/gorilla/websocket from 1.5.1 to 1.5.3
- [#15708](https://github.com/influxdata/telegraf/pull/15708) `deps` Bump github.com/multiplay/go-ts3 from 1.1.0 to 1.2.0
- [#15707](https://github.com/influxdata/telegraf/pull/15707) `deps` Bump github.com/prometheus-community/pro-bing from 0.4.0 to 0.4.1
- [#15709](https://github.com/influxdata/telegraf/pull/15709) `deps` Bump github.com/prometheus/prometheus from 0.48.1 to 0.53.1
- [#15680](https://github.com/influxdata/telegraf/pull/15680) `deps` Bump github.com/vmware/govmomi from 0.37.2 to 0.39.0
- [#15682](https://github.com/influxdata/telegraf/pull/15682) `deps` Bump go.mongodb.org/mongo-driver from 1.14.0 to 1.16.0
- [#15652](https://github.com/influxdata/telegraf/pull/15652) `deps` Bump go.step.sm/crypto from 0.47.1 to 0.50.0
- [#15653](https://github.com/influxdata/telegraf/pull/15653) `deps` Bump google.golang.org/grpc from 1.64.1 to 1.65.0
- [#15704](https://github.com/influxdata/telegraf/pull/15704) `deps` Bump super-linter/super-linter from 6.7.0 to 6.8.0

## v1.31.2

### Bug fixes

- [#15589](https://github.com/influxdata/telegraf/pull/15589) `common.socket` Switch to context to simplify closing
- [#15601](https://github.com/influxdata/telegraf/pull/15601) `inputs.ping` Check addr length to avoid crash
- [#15618](https://github.com/influxdata/telegraf/pull/15618) `inputs.snmp` Translate field correctly when not in table
- [#15586](https://github.com/influxdata/telegraf/pull/15586) `parsers.xpath` Allow resolving extensions
- [#15630](https://github.com/influxdata/telegraf/pull/15630) `tools.custom_builder` Handle multiple instances of the same plugin correctly

### Dependency updates

- [#15582](https://github.com/influxdata/telegraf/pull/15582) `deps` Bump cloud.google.com/go/storage from 1.41.0 to 1.42.0
- [#15623](https://github.com/influxdata/telegraf/pull/15623) `deps` Bump cloud.google.com/go/storage from 1.42.0 to 1.43.0
- [#15607](https://github.com/influxdata/telegraf/pull/15607) `deps` Bump github.com/alitto/pond from 1.8.3 to 1.9.0
- [#15625](https://github.com/influxdata/telegraf/pull/15625) `deps` Bump github.com/antchfx/xpath from 1.3.0 to 1.3.1
- [#15622](https://github.com/influxdata/telegraf/pull/15622) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs from 1.34.3 to 1.37.3
- [#15606](https://github.com/influxdata/telegraf/pull/15606) `deps` Bump github.com/hashicorp/consul/api from 1.26.1 to 1.29.1
- [#15604](https://github.com/influxdata/telegraf/pull/15604) `deps` Bump github.com/jackc/pgx/v4 from 4.18.2 to 4.18.3
- [#15581](https://github.com/influxdata/telegraf/pull/15581) `deps` Bump github.com/nats-io/nats-server/v2 from 2.10.16 to 2.10.17
- [#15603](https://github.com/influxdata/telegraf/pull/15603) `deps` Bump github.com/openconfig/goyang from 1.0.0 to 1.5.0
- [#15624](https://github.com/influxdata/telegraf/pull/15624) `deps` Bump github.com/sijms/go-ora/v2 from 2.8.4 to 2.8.19
- [#15585](https://github.com/influxdata/telegraf/pull/15585) `deps` Bump github.com/testcontainers/testcontainers-go/modules/kafka from 0.30.0 to 0.31.0
- [#15605](https://github.com/influxdata/telegraf/pull/15605) `deps` Bump github.com/tinylib/msgp from 1.1.9 to 1.2.0
- [#15584](https://github.com/influxdata/telegraf/pull/15584) `deps` Bump github.com/urfave/cli/v2 from 2.27.1 to 2.27.2
- [#15614](https://github.com/influxdata/telegraf/pull/15614) `deps` Bump google.golang.org/grpc from 1.64.0 to 1.64.1
- [#15608](https://github.com/influxdata/telegraf/pull/15608) `deps` Bump super-linter/super-linter from 6.6.0 to 6.7.0

For versions earlier than v1.13 and earlier see [CHANGELOG-1.13.md](CHANGELOG-1.13.md).

## v1.31.1

### Bug fixes

- [#15488](https://github.com/influxdata/telegraf/pull/15488) `agent` Ignore startup-errors in test mode
- [#15568](https://github.com/influxdata/telegraf/pull/15568) `inputs.chrony` Handle ServerStats4 response
- [#15551](https://github.com/influxdata/telegraf/pull/15551) `inputs.chrony` Support local (reference) sources
- [#15565](https://github.com/influxdata/telegraf/pull/15565) `inputs.gnmi` Handle YANG namespaces in paths correctly
- [#15496](https://github.com/influxdata/telegraf/pull/15496) `inputs.http_response` Fix for IPv4 and IPv6 addresses when interface is set
- [#15493](https://github.com/influxdata/telegraf/pull/15493) `inputs.mysql` Handle custom TLS configs correctly
- [#15514](https://github.com/influxdata/telegraf/pull/15514) `logging` Add back constants for backward compatibility
- [#15531](https://github.com/influxdata/telegraf/pull/15531) `secretstores.oauth2` Ensure endpoint params is not nil

### Dependency updates

- [#15483](https://github.com/influxdata/telegraf/pull/15483) `deps` Bump cloud.google.com/go/monitoring from 1.18.1 to 1.19.0
- [#15559](https://github.com/influxdata/telegraf/pull/15559) `deps` Bump github.com/Azure/azure-kusto-go from 0.15.2 to 0.15.3
- [#15489](https://github.com/influxdata/telegraf/pull/15489) `deps` Bump github.com/Azure/azure-sdk-for-go/sdk/azidentity from 1.5.1 to 1.6.0
- [#15560](https://github.com/influxdata/telegraf/pull/15560) `deps` Bump github.com/Azure/go-autorest/autorest/azure/auth from 0.5.12 to 0.5.13
- [#15480](https://github.com/influxdata/telegraf/pull/15480) `deps` Bump github.com/IBM/sarama from 1.43.1 to 1.43.2
- [#15526](https://github.com/influxdata/telegraf/pull/15526) `deps` Bump github.com/aws/aws-sdk-go-v2/service/cloudwatch from 1.37.0 to 1.38.7
- [#15527](https://github.com/influxdata/telegraf/pull/15527) `deps` Bump github.com/aws/aws-sdk-go-v2/service/dynamodb from 1.30.2 to 1.32.9
- [#15558](https://github.com/influxdata/telegraf/pull/15558) `deps` Bump github.com/aws/aws-sdk-go-v2/service/dynamodb from 1.32.9 to 1.33.2
- [#15448](https://github.com/influxdata/telegraf/pull/15448) `deps` Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.161.1 to 1.162.1
- [#15557](https://github.com/influxdata/telegraf/pull/15557) `deps` Bump github.com/go-ldap/ldap/v3 from 3.4.6 to 3.4.8
- [#15523](https://github.com/influxdata/telegraf/pull/15523) `deps` Bump github.com/linkedin/goavro/v2 from 2.12.0 to 2.13.0
- [#15484](https://github.com/influxdata/telegraf/pull/15484) `deps` Bump github.com/microsoft/go-mssqldb from 1.7.0 to 1.7.2
- [#15561](https://github.com/influxdata/telegraf/pull/15561) `deps` Bump github.com/nats-io/nats-server/v2 from 2.10.14 to 2.10.16
- [#15524](https://github.com/influxdata/telegraf/pull/15524) `deps` Bump github.com/prometheus/common from 0.53.0 to 0.54.0
- [#15481](https://github.com/influxdata/telegraf/pull/15481) `deps` Bump github.com/prometheus/procfs from 0.15.0 to 0.15.1
- [#15482](https://github.com/influxdata/telegraf/pull/15482) `deps` Bump github.com/rabbitmq/amqp091-go from 1.9.0 to 1.10.0
- [#15525](https://github.com/influxdata/telegraf/pull/15525) `deps` Bump go.step.sm/crypto from 0.44.1 to 0.47.1
- [#15479](https://github.com/influxdata/telegraf/pull/15479) `deps` Bump super-linter/super-linter from 6.5.1 to 6.6.0

## v1.31.0

### Important Changes

- The fields `read_bytes` and `write_bytes` in `inputs.procstat` now contain all I/O operations for consistency with other operating systems. Previous values are output as `disk_read_bytes` and `disk_write_bytes` measuring only the I/O on the storage layer.

### New Plugins

#### Inputs

- [smartctl](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/smartctl) (`inputs.smartctl`)

#### Parsers

- [openmetrics](https://github.com/influxdata/telegraf/tree/master/plugins/parsers/openmetrics) (`parsers.openmetrics`)
- [parquet](https://github.com/influxdata/telegraf/tree/master/plugins/parsers/parquet) (`parsers.parquet`)

#### Processors

- [timestamp](https://github.com/influxdata/telegraf/tree/master/plugins/processors/timestamp) (`processors.timestamp`)

### Features

- Agent:
    - Add uint support in cli test output.
    - Introduce CLI option to set config URL retry attempts.
    - Introduce CLI option to reload remote URL configs on change.
- Azure Monitor (`input.azure_monitor`): Use default Azure credentials chain when no secret provided.
- Basicstats (aggregators.basicstats\`): Add last field.
- Binary (`parsers.binary`): Allow base64-encoded input data.
- Ceph (`inputs.ceph`): Use perf schema to determine metric type.
- CLI: List available parsers and serializers.
- CrateDB (`outputs.cratedb`): Allow configuration of startup error handling.
- DNS Query (`inputs.dns_query`): Allow ignoring errors of specific types.
- ElasticSearch (\`outputs.elasticsearch Allow settings extra headers for elasticsearch output.
- Exec (`inputs.exec`): Add option to ignore return code.
- Execd (`inputs.execd`): Add option to not restart program on error.
- File (`inputs.file`): Add tag with absolute path of file.
- Final (aggregators.final\`): Add option to disable appending \_final.
- GNMI (`inputs.gnmi`):
    - Add keepalive settings.
    - Add option to create more descriptive tags.
    - Add secret store support for username and password.
    - Add yang-model decoding of JSON IETF payloads.
    - Allow to pass accepted cipher suites.
- HTTP Listener (`inputs.http_listener`): Allow setting custom success return code.
- HTTP Response (`inputs.http_response`): Add cookie authentication.
- Influx (`serializers.influx`): Add option to omit timestamp.
- InfluxDB (`inputs.influxdb`): Add metrics for build, crypto and commandline.
- InfluxDB (`outputs.influxdb`): Add option to define local address.
- InfluxDB v2 (`outputs.influxdb_v2`)
    - Add option to set local address.
    - Preserve custom query parameters on write.
- InfluxDB v2 Listener (`inputs.influxdb_v2_listener`):
    - Add support for rate limiting.
    - Support secret store for token.
- Internet Speed (`inputs.internet_speed`): Introduce packet loss field.
- Inputs (`inputs`): Add framework to retry on startup errors.
- Kafka Consumer (`inputs.kafka_consumer`): Add resolve canonical bootstrap server option.
- KNX Listener (`inputs.knx_listener`):
    - Add support for string data type.
    - Allow usage of DPT string representation.
- Kubernetes (`inputs.kubernetes`): Add option to node metric name.
- Lustre2 (`inputs.lustre2`):
    - Add eviction\_count field.
    - Add health-check metric.
    - Add support for bulk read/write stats.
    - Skip brw\_stats in case of insufficient permissions.
- Merge (aggregators.merge\`): Allow to round metric timestamps.
- MQTT (`outputs.mqtt`): Add client trace logging, resolve MQTT5 reconnect login.
- Mock (`inputs.mock`): Add baseline option to sine.
- Netflow (`inputs.netflow`):
    - Add support for IPFIX option packets.
    - Add support for netflow v9 option packets.
- Nvidia SMI (`inputs.nvidia_smi`): Add power-limit field for v12 scheme.
- OPCUA (`common.opcua`): Add session timeout as configuration option.
- OpenStack (`inputs.openstack`): Use service catalog from v3 authentication if available.
- OpenTelemetry (`inputs.opentelemetry`): Add option to set max receive message size
- Outputs (`outputs`): Add framework to retry on startup errors.
- Parser (`processors.parser`): Add base64 decode for fields.
- PostgreSQL (`outputs.postgresql`):
    - Add secret store support.
    - Allow configuration of startup error handling.
- Printer (`processors.printer`): Embed Influx serializer options.
- Procstat (`inputs.procstat`):
    - Add option to select properties to collect.
    - Allow multiple selection criteria.
    - Report consistent I/O on Linux.
- Prometheus Remote Write (`parser.prometheusremotewrite`): Parse and generate histogram buckets.
- Radius (`inputs.radius`): Provide setting to set request IP address.
- Redis (`inputs.redis`): Add latency percentiles metric.
- s7comm (`inputs.s7comm`): Add optional connection type setting.
- SNMP (`snmp`): Add secret support for auth\_password and priv\_password.
- SNMP (`inputs.snmp`): Convert octet string with invalid data to hex.
- SQLServer (`inputs.sqlserver`): Add persistent version store metrics.
- Starlark (`processors.starlark`): Allow persistence of global state.
- Statsd (`inputs.statsd`):
    - Add support for DogStatsD v1.2.
    - Allow counters to report as float.
- Windows EventLog (`inputs.win_eventlog`): Add option to define event batch-size.
- Windows WMI (`inputs.win_wmi`):
    - Add support for remote queries.
    - Allow to invoke methods.

### Bug fixes

- Agent: Warn on multiple agent configuration tables seen.
- CloudWatch (`inputs.cloudwatch`):
    - Add accounts when enabled.
    - Ensure account list is larger than index.
- ECS (`inputs.ecs`): Check for nil pointer before use.
- PostgreSQL Extensible (`inputs.postgresql_extensible`): Use same timestamp for each gather.
- procstat (`inputs.procstat`): Do not report dead processes as running for orphan PID files.
- smartctl (`inputs.smartctl`): Add additional fields.
- SNMP Lookup (`processors.snmp_lookup`): Return empty tag-map on error to avoid panic.

### Dependency updates

- Update `cloud.google.com/go/storage` from 1.40.0 to 1.41.0.
- Update `github.com/awnumar/memguard` from 0.22.4 to 0.22.5.
- Update `github.com/fatih/color` from 1.16.0 to 1.17.0.
- Update `github.com/jhump/protoreflect` from 1.15.6 to 1.16.0.
- Update `github.com/lxc/incus` v0.4.0 to v6.2.0.
- Update `github.com/miekg/dns` from 1.1.58 to 1.1.59.
- Update `github.com/openzipkin/zipkin-go` from 0.4.2 to 0.4.3.
- Update `github.com/prometheus/common` from 0.52.2 to 0.53.0.
- Update `github.com/showwin/speedtest-go` from 1.7.5 to 1.7.6.
- Update `github.com/showwin/speedtest-go` from 1.7.6 to 1.7.7.
- Update `github.com/snowflakedb/gosnowflake` from 1.7.2 to 1.10.0.
- Update `go` from v1.22.3 to v1.22.4.
- Update `golang.org/x/crypto` from 0.22.0 to 0.23.0.
- Update `golang.org/x/net` from 0.24.0 to 0.25.0.
- Update `k8s.io/*` from 0.29.3 to 0.30.1.
- Update `modernc.org/sqlite` from 1.29.10 to 1.30.0.
- Update `modernc.org/sqlite` from 1.29.5 to 1.29.10.
- Update `super-linter/super-linter` from 6.4.1 to 6.5.0.
- Update `super-linter/super-linter` from 6.5.0 to 6.5.1.
- Switch to `github.com/leodido/go-syslog`.
- Update all OpenTelemetry dependencies.

## v1.30.3

### Bug fixes

- Cloudwatch (`inputs.cloudwatch`): Option to produce dense metrics.
- GNMI (`inputs.gnmi`): Ensure path contains elements to avoid panic.
- Graphite (`outputs.graphite`): Handle local address without port correctly.
- HTTP (`http`): Stop plugins from leaking file descriptors on telegraf reload.
- HTTP Listener v2 (`inputs.http_listener_v2`): Wrap timestamp parsing error messages.
- Loki (`outputs.loki`): Option to sanitize label names.
- Makefile (`makefile`): Use go’s dependency checker for per platform builds.
- Netflow (`inputs.netflow`): Log unknown fields only once.
- Redis (`input.redis`): Discard invalid errorstat lines.
- Sysstat (`inputs.sysstat`): Prevent default sadc\_interval from increasing on reload.
- Windows (`windows`): Make sure to log the final error message on exit.

### Dependency updates

- Update `cloud.google.com/go/bigquery` from 1.59.1 to 1.61.0.
- Update `github.com/Azure/azure-kusto-go` from 0.15.0 to 0.15.2.
- Update `github.com/aliyun/alibaba-cloud-sdk-go` from 1.62.713 to 1.62.721.
- Update `github.com/antchfx/xmlquery` from 1.3.18 to 1.4.0.
- Update `github.com/antchfx/xpath` from 1.2.5 to 1.3.0.
- Update `github.com/aws/aws-sdk-go-v2/config` from 1.27.9 to 1.27.13.
- Update `github.com/aws/aws-sdk-go-v2/credentials` from 1.17.9 to 1.17.11.
- Update `github.com/aws/aws-sdk-go-v2/service/ec2` from 1.151.1 to 1.161.1.
- Update `github.com/coocood/freecache` from 1.2.3 to 1.2.4.
- Update `github.com/google/cel-go` from 0.18.1 to 0.20.1.
- Update `github.com/grid-x/modbus` from v0.0.0-20211113184042-7f2251c342c9 to v0.0.0-20240503115206-582f2ab60a18.
- Update `github.com/nats-io/nats-server/v2` from 2.10.9 to 2.10.14.
- Update `github.com/pion/dtls/v2` from 2.2.10 to 2.2.11.
- Update `github.com/prometheus/procfs` from 0.13.0 to 0.14.0.
- Update `github.com/shirou/gopsutil/v3` from v3.24.3 to v3.24.4.
- Update `github.com/testcontainers/testcontainers-go/modules/kafka` from 0.26.1-0.20231116140448-68d5f8983d09 to 0.30.0.
- Update `github.com/vmware/govmomi` from 0.37.0 to 0.37.2.
- Update `go` from v1.22.2 to v1.22.3.
- Update `golang.org/x/mod` from 0.16.0 to 0.17.0.
- Update `golang.org/x/sync` from 0.6.0 to 0.7.0.
- Update `golangci-lint` from v1.57.2 to v1.58.0.
- Update `google.golang.org/api` from 0.171.0 to 0.177.0.
- Update `super-linter/super-linter` from 6.3.1 to 6.4.1.
- Migrate to maintained gopacket library.

## v1.30.2

### Important Changes

- This release reverts the behavior of `inputs.systemd_units` back to pre-v1.30.0 to only collect units already loaded by systemd (i.e. not collecting disabled or static units). This was necessary because using unspecific filters will cause significant load on the system as systemd needs to read all unit-files matching the pattern in each gather cycle. If you use specific patterns and want to collect non-loaded units, please set the `collect_disabled_units` option to true.

### Bug fixes

- Agent (`agent`): Ensure import of required package for pprof support.
- Disk I/O (`inputs.diskio`): Update path from /sys/block to /sys/class/block.
- Modbus (`inputs.modbus`): Avoid overflow when calculating with uint16 addresses.
- Nvidia (`inputs.nvidia`): Include power limit field for v11.
- OPC UA (`inputs.opcua`): Make sure to always create a request.
- OpenSearch (`outputs.opensearch`): Correctly error during failures or disconnect.
- PHP FPM (`inputs.phpfpm`): Check for error before continue processing.
- Prometheus (`inputs.prometheus`):
    - Correctly handle host header.
    - Remove duplicate response\_timeout option.
- SQL (`outputs.sql`): Enable the use of krb5 with mssql driver.
- SQL Server (`inputs.sqlserver`): Honor timezone on backup metrics.
- systemd (`systemd`): Remove 5 second timeout, use default (90 seconds).
- systemd Units (`inputs.systemd_units`):
    - Reconnect if connection is lost.
    - Revert to only gather loaded units by default.
- Windows Event Log (`inputs.win_eventlog`): Handle empty query correctly.

### Dependency updates

- Update `github.com/aliyun/alibaba-cloud-sdk-go` from 1.62.563 to 1.62.708.
- Update `github.com/aliyun/alibaba-cloud-sdk-go` from 1.62.708 to 1.62.713.
- Update `github.com/apache/iotdb-client-go` from 0.12.2-0.20220722111104-cd17da295b46 to 1.2.0-tsbs.
- Update `github.com/aws/aws-sdk-go-v2/service/cloudwatch` from 1.36.1 to 1.37.0.
- Update `github.com/aws/aws-sdk-go-v2/service/kinesis` from 1.27.1 to 1.27.4.
- Update `github.com/aws/aws-sdk-go-v2/service/timestreamwrite` from 1.25.2 to 1.25.5.
- Update `github.com/go-sql-driver/mysql` from 1.7.1 to 1.8.1.
- Update `github.com/gophercloud/gophercloud` from 1.9.0 to 1.11.0.
- Update `github.com/jackc/pgtype` from 1.14.2 to 1.14.3.
- Update `github.com/prometheus/client_golang` from 1.18.0 to 1.19.0.
- Update `github.com/redis/go-redis/v9` from 9.2.1 to 9.5.1.
- Update `github.com/shirou/gopsutil` from v3.23.11 to v3.24.3.
- Update `github.com/testcontainers/testcontainers-go` from 0.27.0 to 0.29.1.
- Update `github.com/vmware/govmomi` from 0.33.1 to 0.37.0.
- Update `golang.org/x/net` from 0.22.0 to 0.23.0.
- Update `golang.org/x/oauth2` from 0.18.0 to 0.19.0.
- Update `k8s.io/client-go` from 0.29.2 to 0.29.3.
- Update `super-linter/super-linter` from 6.3.0 to 6.3.1.
- Update `tj-actions/changed-files` from 43 to 44

## v1.30.1

### Bug fixes

- Chrony (`inputs.chrony`): Remove chronyc dependency in documentation.
- DiskIO (`inputs.diskio`): Add missing udev properties.
- DNS Query (`inputs.dns_query`):
    - Fill out additional record fields.
    - Include the canonical CNAME target.
- KNX (`inputs.knx_listener`):
    - Ignore GroupValueRead requests.
    - Reconnect after connection loss.
- MySQL (`inputs.mysql`):
    - Parse boolean values in metric v1 correctly.
    - Use correct column-types for Percona 8 user stats.
- NVIDIA SMI (`inputs.nvidia_smi`): Add process info metrics.
- OpenStack(`inputs.openstack`): Resolve regression in block storage and server info.
- PHP-FPM (`inputs.phpfpm`): Add timeout for fcgi.
- Ping (`inputs.ping`): Add option to force ipv4.
- Prometheus (`inputs.prometheus`): Initialize logger of parser.
- S.M.A.R.T. (`inputs.smart`): Improve regexp to support flags with a plus.
- Systemd Units (`inputs.systemd_units`): Handle disabled multi-instance units correctly.
- BigQuery (`outputs.bigquery`): Add scope to bigquery and remove timeout context.
- Avoid count underflow by only counting initialized secrets.
- Ensure watch-config is passed to the Windows service.

### Dependency updates

- Update `github.com/IBM/sarama` from v1.42.2 to v1.43.1.
- Update `github.com/aws/aws-sdk-go-v2` from 1.25.3 to 1.26.0.
- Update `github.com/aws/aws-sdk-go-v2/config` from 1.27.5 to 1.27.9.
- Update `github.com/aws/aws-sdk-go-v2/feature/ec2/imds` from 1.15.2 to 1.16.0.
- Update `github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs` from 1.34.2 to 1.34.3.
- Update `github.com/aws/aws-sdk-go-v2/service/ec2` from 1.149.3 to 1.151.1.
- Update `github.com/aws/aws-sdk-go-v2/service/sts` from 1.28.2 to 1.28.4.
- Update `github.com/docker/docker` from 25.0.0+incompatible to 25.0.5+incompatible.
- Update `github.com/jackc/pgtype` from 1.14.0 to 1.14.2.
- Update `github.com/jackc/pgx/v4` from 4.18.1 to 4.18.2.
- Update `github.com/klauspost/compress` from 1.17.6 to 1.17.7.
- Update `github.com/pion/dtls/v2` from 2.2.8 to 2.2.10.
- Update `github.com/prometheus-community/pro-bing` from 0.3.0 to 0.4.0.
- Update `github.com/prometheus/procfs` from 0.12.0 to 0.13.0.
- Update `github.com/stretchr/testify` v1.8.4 to v1.9.0.
- Update `go.step.sm/crypto` from 0.43.0 to 0.44.1.
- Update `golang.org/x/crypto` from 0.20.0 to 0.21.0.
- Update `gonum.org/v1/gonum` from 0.14.0 to 0.15.0.
- Update `google.golang.org/api` from 0.165.0 to 0.171.0.
- Update `google.golang.org/protobuf` from 1.32.0 to 1.33.0.
- Update `tj-actions/changed-files` from 42 to 43.

## v1.30.0

### Deprecation removals

This release removes the following deprecated plugins:

- `inputs.cassandra`
- `inputs.httpjson`
- `inputs.io`
- `inputs.jolokia`
- `inputs.kafka_consumer_legacy`
- `inputs.snmp_legacy`
- `inputs.tcp_listener`
- `inputs.udp_listener`
- `outputs.riemann_legacy`

Furthermore, the following deprecated plugin options are removed:

- `mountpoints` of `inputs.disk`
- `metric_buffer` of `inputs.mqtt_consumer`
- `metric_buffer` of `inputs.nats_consumer`
- `url` of `outputs.influxdb`

Replacements do exist, so please migrate your configuration in case you are still using one of these plugins. The [`telegraf config migrate` command](/telegraf/v1/commands/config/migrate/) can help with migrating to newer plugins.

### Important Changes

- The default read-timeout of `inputs.syslog` of five seconds is not a sensible default as the plugin will close the connection if the time between consecutive messages exceeds the timeout. Telegraf 1.30.0+ sets the timeout to infinite (i.e zero) as this is the expected behavior.
- Telegraf 1.30.0+ correctly sanitize PostgreSQL addresses, which may change the server tag value for a URI-formatted address that contains spaces, backslashes or single-quotes in non-redacted parameters.

### New Plugins

#### Outputs

- [Zabbix](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/zabbix) (`outputs.zabbix`)

#### Serializers

- [Binary](https://github.com/influxdata/telegraf/tree/master/plugins/serializers/binary) (`serializers.binary`)

#### Processors

- [SNMP lookup](https://github.com/influxdata/telegraf/tree/master/plugins/processors/snmp_lookup) (`processors.snmp_lookup`)

### Features

- Add loongarch64 nightly and release builds.
- Add `skip_processors_after_aggregators` configuration option to skip re-running processors after aggregators.
- Allow secrets in headers
- OPCUA (`common.opcua`): Add debug info for nodes not in server namespace.
- Aerospike (`inputs.aerospike`): Deprecate plugin.
- AMD ROCm System Management Interface (`inputs.amd_rocm_smi`): Add `startup_error_behavior` configuration option.
- Chrony (`inputs.chrony`):
    - Allow the collection of additional metrics.
    - Remove `chronyc` dependency.
- Kafka Consumer (`inputs.kafka_consumer`): Mark messages that failed parsing.
- Kernel (`inputs.kernel`): Add pressure stall information.
- Modbus (`inputs.modbus`): Add a workaround for unusual string-byte locations.
- Net (`inputs.net`): Add speed metric.
- NVIDIA SMI (`inputs.nvidia_smi`): Add `startup_error_behavior` configuration option.
- Prometheus (`inputs.prometheus`):
    - Add internal metrics.
    - Add option to limit body length.
- Redfish (`inputs.redfish`): Allow secrets for username/password configuration.
- S.M.A.R.T. (`inputs.smart`): Add a `device_type` tag to differentiate disks behind a RAID controller.
- SQL Server (`inputs.sqlserver`): Add stolen target memory ratio.
- Systemd Units (`inputs.systemd_units`)
    - Support querying unloaded/disabled units.
    - Introduce show subcommand for additional data.
- Windows Services (`inputs.win_services`): Make service selection case-insensitive.
- Graphite (`outputs.graphite`): Set the local address to bind to.
- NATS (`outputs.nats`): Introduce NATS Jetstream option.
- Nebius Cloud Monitoring (`outputs.nebius_cloud_monitoring`): Add service configuration setting.
- Webscoket (`outputs.websocket`): Support secrets in headers.
- CSV (`serializers.csv`): Specify a fixed column order.

### Bug fixes

- Catch panics in input plugin goroutines.
- Reword error message about missing configuration options.
- Docker Log (`inputs.docker_log`): Use the correct name when matching container.
- GNMI (`inputs.gnmi`):
    - Add option to infer the path tag from the subscription.
    - Handle canonical field-name correctly
- Netflow (`inputs.netflow`): Fallback to IPFIX mappings for Netflow v9.
- PHP-FPM (`inputs.phpfpm`): Continue despite erroneous sockets.
- Prometheus (`inputs.prometheus`): List namespaces only when filtering by namespace.
- Prometheus (`parsers.prometheus`): Do not touch input data for protocol-buffers.
- Override (`processors.override`): Correct TOML tag name.
- Ensure valid statefile in package.

### Dependency updates

- Update all `github.com/aws/aws-sdk-go-v2` dependencies.
- Update `cloud.google.com/go/bigquery` from 1.58.0 to 1.59.1.
- Update `github.com/aws/aws-sdk-go-v2/service/dynamodb` from 1.27.0 to 1.30.2.
- Update `github.com/cloudevents/sdk-go/v2` from 2.15.0 to 2.15.2.
- Update `github.com/eclipse/paho.golang` from 0.20.0 to 0.21.0.
- Update `github.com/microsoft/go-mssqldb` from 1.6.0 to 1.7.0.
- Update `github.com/netsampler/goflow2` from v1.3.6 to v2.1.2.
- Update `github.com/peterbourgon/unixtransport` from 0.0.3 to 0.0.4.
- Update `github.com/prometheus/client_model` from 0.5.0 to 0.6.0.
- Update `github.com/srebhan/cborquery` from v0.0.0-20230626165538-38be85b82316 to v1.0.1.
- Update `github.com/vapourismo/knx-go` from v0.0.0-20240107135439-816b70397a00 to v0.0.0-20240217175130-922a0d50c241.
- Update `go.mongodb.org/mongo-driver` from 1.13.1 to 1.14.0.
- Update `golang.org/x/crypto` from 0.19.0 to 0.20.0.
- Update `modernc.org/sqlite` from 1.28.0 to 1.29.2.
- Update `super-linter/super-linter` from 6.1.1 to 6.3.0.

## v1.29.5

### Bug fixes

- execd (`processors.execd`): Accept tracking metrics instead of dropping them.
- Filecount (`inputs.filecount`): Respect symlink files with FollowSymLinks.
- GNMI (`inputs.gnmi`): Normalize path for inline origin handling.
- Kafka Consume (`inputs.kafka_consumer`): Fix typo of msg\_headers\_as\_tags.
- MQTT (`outputs.mqtt`): Retry metrics for server timeout.
- Packaging (`rpm`): Ensure telegraf is installed after useradd.
- PostgreSQL Extensible (`inputs.postgresql_extensible`): Add support for bool tags.
- Redfish (`inputs.redfish`): Resolve iLO4 fan data.
- SNMP Trap (`inputs.snmp_trap`): Enable SHA ciphers.
- unpivot (`processors.unpivot`): Handle tracking metrics correctly.
- Vsphere (`inputs.vsphere`): Use guest.guestId value if set for guest name.

### Dependency updates

- Update `cloud.google.com/go/bigquery` from 1.57.1 to 1.58.0.
- Update `cloud.google.com/go/pubsub` from 1.33.0 to 1.36.1.
- Update `cloud.google.com/go/storage` from 1.36.0 to 1.38.0.
- Update `github.com/Azure/azure-event-hubs-go/v3` from 3.6.1 to 3.6.2.
- Update `github.com/DATA-DOG/go-sqlmock` from 1.5.0 to 1.5.2.
- Update `github.com/IBM/sarama` from 1.42.1 to 1.42.2.
- Update `github.com/awnumar/memguard` from 0.22.4-0.20231204102859-fce56aae03b8 to 0.22.4.
- Update `github.com/cloudevents/sdk-go/v2` from 2.14.0 to 2.15.0.
- Update `github.com/eclipse/paho.golang` from 0.11.0 to 0.20.0.
- Update `github.com/google/uuid` from 1.5.0 to 1.6.0.
- Update `github.com/gopcua/opcua` from 0.4.0 to 0.5.3.
- Update `github.com/gophercloud/gophercloud` from 1.7.0 to 1.9.0.
- Update `github.com/gwos/tcg/sdk` from v0.0.0-20220621192633-df0eac0a1a4c to v8.7.2.
- Update `github.com/jhump/protoreflect` from 1.15.4 to 1.15.6.
- Update `github.com/klauspost/compress` from 1.17.4 to 1.17.6.
- Update `github.com/miekg/dns` from 1.1.57 to 1.1.58.
- Update `github.com/showwin/speedtest-go` from 1.6.7 to 1.6.10.
- Update `github.com/urfave/cli/v2` from 2.25.7 to 2.27.1.
- Update `go.opentelemetry.io/collector/pdata` from 1.0.1 to 1.1.0.
- Update `golang.org/x/oauth2` from 0.16.0 to 0.17.0.
- Update `google.golang.org/api` from 0.162.0 to 0.165.0.
- Update `google.golang.org/grpc` from 1.61.0 to 1.61.1.
- Update `k8s.io/apimachinery` from 0.29.0 to 0.29.1.
- Update `k8s.io/client-go` from 0.29.0 to 0.29.1.
- Update `k8s.io/client-go` from 0.29.1 to 0.29.2.
- Update `super-linter/super-linter` from 6.0.0 to 6.1.1.
- Update `tj-actions/changed-files` from 41 to 42.
- Remove `golang.org/x/exp` and use stable versions instead.
- Use `github.com/coreos/go-systemd/v22` instead of git version.

## v1.29.4

### Bug fixes

- SNMP (`inputs.temp`): Fix regression in metric formats.
- SNMP Trap (`inputs.snmp_trap`): Handle octet strings.
- Parser (`processors.parser`): Drop tracking metrics when not carried forward.

### Dependency updates

- Update all AWS dependencies
- Update `github.com/compose-spec/compose-go` from 1.20.0 to 1.20.2.
- Update `github.com/gosnmp/gosnmp` from 1.36.1 to 1.37.0.
- Update `github.com/microsoft/go-mssqldb` from 1.5.0 to 1.6.0.
- Update `github.com/nats-io/nats-server/v2` from 2.10.6 to 2.10.9.
- Update `github.com/yuin/goldmark` from 1.5.6 to 1.6.0.

## v1.29.3

### Bug fixes

- Encoding (`common.encoding`): Remove locally-defined errors and use upstream ones.
- GNMI (`inputs.gnmi`): Refactor alias handling to prevent clipping.
- IOTDB (`outputs.iotdb`): Handle paths that contain illegal characters.
- Loki (`outputs.loki`): Do not close body before reading it.
- MQTT (`outputs.mqtt`): Preserve leading slash in topic.
- Temperature (`inputs.temp`): Recover pre-v1.22.4 temperature sensor readings.
- Windows Performance Counters (`inputs.win_perf_counters`):
    - Check errors post-collection for skip.
    - Ignore PdhCstatusNoInstance as well.

### Dependency updates

- Update `github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs` from 1.29.5 to 1.31.0.
- Update `github.com/aws/aws-sdk-go-v2/service/sts` from 1.26.5 to 1.26.7.
- Update `github.com/clarify/clarify-go` from 0.2.4 to 0.3.1.
- Update `github.com/docker/docker` from 24.0.7+incompatible to 25.0.0+incompatible.
- Update `github.com/docker/go-connections` from 0.4.0 to 0.5.0.
- Update `github.com/fatih/color` from 1.15.0 to 1.16.0.
- Update `github.com/gorilla/mux` from 1.8.0 to 1.8.1.
- Update `github.com/intel/powertelemetry` from 1.0.0 to 1.0.1.
- Update `github.com/nats-io/nats.go` from 1.31.0 to 1.32.0.
- Update `github.com/prometheus/common` from 0.44.0 to 0.45.0.
- Update `github.com/testcontainers/testcontainers-go` from 0.26.0 to 0.27.0.
- Update `github.com/vapourismo/knx-go` from v0.0.0-20220829185957-fb5458a5389d to 20240107135439-816b70397a00.
- Update `go.opentelemetry.io/collector/pdata` from 1.0.0-rcv0016 to 1.0.1.
- Update `go.starlark.net` from `go.starlark.net` v0.0.0-20220328144851-d1966c6b9fcd to v0.0.0-20231121155337-90ade8b19d09.
- Update `k8s.io/client-go` from 0.28.3 to 0.29.0.
- Update `modernc.org/sqlite` from 1.24.0 to 1.28.0.

## v1.29.2

### Bug fixes

- Bigquery (`outputs.bigquery`): Ignore fields containing NaN or infinity.
- Filter (`processors.filter`): Rename processors.Filter -> processors.filter.
- InfluxDB (`outputs.influxdb`): Support setting Host header.
- InfluxDB v2 (`outputs.influxdb_v2`): Support setting Host header.
- Kafka (`common.kafka`): Correctly set gssapi username/password.
    - Add pid field to differentiate metrics.
    - Use logger without causing panic.
- PHP FPM (`inputs.phpfpm`):
- procstat (`inputs.procstat`): Correctly set tags on procstat\_lookup.
- Prometheus Client (`outputs.prometheus_client`): Always default to TCP.
- Starlark (`processors.starlark`): Use tracking ID to identify tracking metrics.
- systemd (`systemd`): Allow notify access from all.
- UPSD (`inputs.upsd`): Add additional fields to upsd from NUT.
- Vsphere (`inputs.vsphere`): Resolve occasional serverFault.

### Dependency updates

- Update `collectd.org` from v0.5.0 to v0.6.0.
- Update `github.com/Azure/azure-kusto-go` from 0.13.1 to 0.15.0.
- Update `github.com/containerd/containerd` from 1.7.7 to 1.7.11.
- Update `github.com/djherbis/times` from 1.5.0 to 1.6.0.
- Update `github.com/dvsekhvalnov/jose2go` from v1.5.0 to v1.5.1-0.20231206184617-48ba0b76bc88.
- Update `github.com/google/uuid` from 1.4.0 to 1.5.0.
- Update `github.com/jhump/protoreflect` from 1.15.3 to 1.15.4.
- Update `github.com/pion/dtls/v2` from 2.2.7 to 2.2.8.
- Update `github.com/prometheus/prometheus` from 0.48.0 to 0.48.1.
- Update `github.com/sijms/go-ora/v2` from 2.7.18 to 2.8.4.
- Update `go.mongodb.org/mongo-driver` from 1.12.1 to 1.13.1.
- Update `golang.org/x/crypto` from 0.16.0 to 0.17.0.
- Update `golang.org/x/net` from 0.17.0 to 0.19.0.
- Update `google.golang.org/protobuf` from 1.31.1-0.20231027082548-f4a6c1f6e5c1 to 1.32.0.

## v1.29.1

### Bug fixes

- Clickhouse (`inputs.clickhouse`): Omit zookeeper metrics on clickhouse cloud.
- PHP FPM (`inputs.php-fpm`): Parse JSON output.
- procstat (`inputs.procstat`): Revert unintended renaming of systemd\_unit option.

### Dependency updates

- Update `github.com/go-ldap/ldap/v3` from 3.4.5 to 3.4.6.
- Update `github.com/klauspost/compress` from 1.17.3 to 1.17.4.
- Update `github.com/openzipkin/zipkin-go` from 0.4.1 to 0.4.2.
- Update `github.com/tidwall/gjson` from 1.14.4 to 1.17.0.
- Update all `github.com/aws/aws-sdk-go-v2` dependencies.

## v1.29.0

### New Plugins

#### Inputs

- [LDAP](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/ldap) (`inputs.inputs.ldap`)

#### Outputs

- [OpenSearch](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/opensearch) (`outputs.opensearch`)

#### Processors

- [Filter](https://github.com/influxdata/telegraf/tree/master/plugins/processors/filter) (`processors.filter`)

#### Secret Stores

- [systemd](https://github.com/influxdata/telegraf/tree/master/plugins/secretstores/systemd) (`secretstores.systemd`)

### Features

- Agent (`agent`): Allow separators for namepass and namedrop filters
- Final (`aggregators.final`): Specify output strategy
- HTTP (`common.http`): Add support for connecting over unix-socket
- OPCUA (`common.opcua`): Add option to include OPC-UA DataType as a field
- Config (`config`): Deprecate `fieldpass` and `fielddrop` modifiers
- Intel PMT (`input.intel_pmt`): Add `pci_bdf` tag to uniquely identify GPUs and other peripherals
- AMQP Consumer (`inputs.amqp_consumer`): Add secretstore support for username and password
- Docker (`inputs.docker`): Add disk usage
- DPDK (`inputs.dpdk`): Add options to customize error-behavior and metric layout
- Elasticsearch (`inputs.elasticsearch`): Use HTTPClientConfig struct
- Elasticsearch Query (`inputs.elasticsearch_query`): Use HTTPClientConfig struct
- GNMI (`inputs.gnmi`): Rework plugin
- HTTP Response (`inputs.http_response`): Add body form configuration option
- Intel PowerStat (`inputs.intel_powerstat`): Extract business logic to external library
- Kafka Consumer (`inputs.kafka_consumer`):
    - Add message headers as metric tags
    - Add option to set metric name from message header
- Kibana (`inputs.kibana`): Use HTTPClientConfig struct
- Kube Inventory (`inputs.kube_inventory`)
    - Support filtering pods and nodes by node name
    - Support using kubelet to get pods data
- LDAP (`inputs.ldap`): Collect additional fields
- Logstash (`inputs.logstash`): Use HTTPClientConfig struct
- Modbus (`inputs.modbus`): Add support for string fields
- NATS Consumer (`inputs.nats_consumer`): Add nkey-seed-file authentication
- OPCUA Listener (`inputs.opcua_listener`): Add monitoring params
- Open Weather Map(`inputs.openweathermap`): Add per-city query scheme for current weather
- procstat (`inputs.procstat`): Obtain process information through supervisor
- RabbitMQ (`inputs.rabbitmq`): Add secretstore support for username and password
- Redfish (`inputs.redfish`): Allow specifying which metrics to collect
- SNMP (`inputs.snmp`): Hint to use source tag
- Socket Listener (`inputs.socket_listener`): Add vsock support to socket listener and writer
- SQL (`inputs.sql`):
    - Add Oracle driver
    - Add IBM Netezza driver
- Windows Service (`inputs.win_service`): Reduce required rights to `GENERIC_READ`
- Migrations (`migrations`):
    - Add migration for `fieldpass` and `fielddrop`
    - Add migration for `inputs.jolokia`
    - Add migration for `inputs.kafka_consumer_legacy`
    - Add migration for `inputs.snmp_legacy`
    - Add migration for `inputs.tcp_listener`
    - Add migration for `inputs.udp_listener`
    - Add migration for `outputs.riemann_legacy`
    - Add option migration for `inputs.disk`
    - Add option migration for `inputs.mqtt_consumer`
    - Add option migration for `inputs.nats_consumer`
    - Add option migration for `outputs.influxdb`
- Azure Data Explorer (`outputs.azure_data_explorer`): Set user agent string
- BigQuery (`outputs.bigquery`):
    - Add metrics in one compact table
    - Make `project` no longer a required field
- Exec (`outputs.exec`): Execute command once per metric
- Prometheus Client (`outputs.prometheus_client`): Support listening on vsock
- Socket Writer (`outputs.socket_writer`): Add vsock support to socket listener and writer
- Stackdriver (`outputs.stackdriver`):
    - Add metric type config options
    - Enable histogram support
- Wavefront (`outputs.wavefront`): Use common/http to configure http client
- Avro (`parsers.avro`):
    - Allow connection to https schema registry
    - Get metric name from the message field
    - Support multiple modes for union handling
- Dedup (`processors.dedup`): Add state persistence between runs
- Regex (`processors.regex`): Allow batch transforms using named groups
- Secrets (`secrets`): Add unprotected secret implementation

### Bug Fixes

- OAuth (`common.oauth`): Initialize EndpointParams to avoid panic with audience settings
- HTTP (`inputs.http`): Use correct token variable
- Intel PowerStat (`inputs.intel_powerstat`): Fix unit tests to work on every CPU/platform
- Modbus (`inputs.modbus`): Split large request correctly at field borders
- Netflow (`inputs.netflow`): Handle malformed inputs gracefully
- s7comm (`inputs.s7comm`): Reconnect if query fails
- tail (`inputs.tail`): Retry opening file after permission denied
- BigQuery (`outputs.bigquery`): Correct use of auto-detected project ID
- OpenSearch (`outputs.opensearch`):
    - Expose TLS setting correctly
    - Migrate to new secrets API
- Prometheus Client (`outputs.prometheus_client`): Ensure v1 collector data expires promptly
- Avro (`parsers.avro`):
    - Clean up Warnf error wrapping error
    - Attempt to read CA cert file only if filename is not empty string
- JSON v2 (`parsers.json v2`):
    - Correct wrong name of config option
    - Reset state before parsing
- Starlark (`processors.starlark`):
    - Avoid negative refcounts for tracking metrics
    - Maintain tracking information post-apply

### Dependency updates

- Update `cloud.google.com/go/bigquery` from 1.56.0 to 1.57.1
- Update `github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs` from 1.26.0 to 1.27.2
- Update `github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/monitor/armmonitor` from 0.10.1 to 0.10.2
- Update `github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/monitor/armmonitor` from 0.10.2 to 0.11.0
- Update `github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/resources/armresources from` 1.1.1 to 1.2.0
- Update `github.com/golang-jwt/jwt/v5` from 5.0.0 to 5.2.0
- Update `github.com/IBM/sarama` from 1.41.3 to 1.42.1
- Update `github.com/influxdata/tail` from 1.0.1-0.20210707231403-b283181d1fa7 to 1.0.1-0.20221130111531-19b97bffd978
- Update `github.com/jackc/pgconn from` 1.14.0 to 1.14.1
- Update `github.com/nats-io/nats-server/v2` from 2.9.23 to 2.10.6
- Update `github.com/prometheus/prometheus` from 0.46.0 to 0.48.0
- Update `github.com/vmware/govmomi` from 0.32.0 to 0.33.1
- Update `golang.org/x/text` from 0.13.0 to 0.14.0
- Update `k8s.io/api` from 0.28.3 to 0.28.4
- Point kafka dependency to IBM organization

## v1.28.5

### Bug Fixes

- ECS (`inputs.ecs`): Correct v4 metadata URLs.
- Intel RDT (`inputs.intel_rdt`): Do not fail on missing PIDs.
- JSON v2 (`parsers.json_v2`): Log inner errors.
- s7comm (`inputs.s7comm`): Truncate strings to reported length.

### Dependency updates

- Update `github.com/gosnmp/gosnmp` from 1.35.1-0.20230602062452-f30602b8dad6 to 1.36.1.
- Update `github.com/Masterminds/semver/v3` from 3.2.0 to 3.2.1.
- Update `golang.org/x/sync` from 0.4.0 to 0.5.0.
- Update `golang.org/x/mod` from 0.13.0 to 0.14.0.
- Update `google.golang.org/api` from 0.149.0 to 0.150.0.

## v1.28.4

### Bug Fixes

- cGroup (`inputs.cgroup`): Escape backslashes in path.
- Config (`config`): Fix comment removal in TOML files.
- Disk (`inputs.disk`): Add inodes\_used\_percent field.
- ECS (`inputs.ecs`):
    - Fix cgroupv2 CPU metrics.
    - Test for v4 metadata endpoint.
- Elasticsearch (`outputs.elasticsearch`): Print error status value.
- IP Set (`inputs.ipset`): Parse lines with timeout.
- JSON v2 (`parsers.json_v2`): Prevent race condition in parse function.
- Prometheus (`inputs.prometheus`): Read bearer token from file every time.
- MQTT Consumer (`inputs.mqtt_consumer`): Resolve could not mark message delivered.
- Netflow (`inputs.netflow`): Fix sFlow metric timestamp.
- s7comm (`inputs.s7comm`): Fix bit queries.
- Timestream (`outputs.timestream`): Clip uint64 values.
- Windows Performance Counters (`inputs.win_perf_counter`): Do not rely on returned buffer size.
- ZFS (`inputs.zfs`):
    - Parse metrics correctly on FreeBSD 14.
    - Support gathering metrics on zfs 2.2.0 and later.

### Dependency updates

- Update `cloud.google.com/go/storage` from 1.30.1 to 1.34.1.
- Update `github.com/aws/aws-sdk-go-v2/config` from 1.18.42 to 1.19.1.
- Update `github.com/aws/aws-sdk-go-v2/credentials` from 1.13.40 to 1.13.43.
- Update `github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs` from 1.23.5 to 1.26.0.
- Update `github.com/antchfx/xmlquery` from 1.3.17 to 1.3.18.
- Update `github.com/antchfx/xpath` from 1.2.5-0.20230505064641-588960cceeac to 1.2.5.
- Update `github.com/benbjohnson/clock` from 1.3.3 to 1.3.5.
- Update `github.com/compose-spec/compose-go` from 1.16.0 to 1.20.0.
- Update `github.com/docker/docker` from 24.0.6 to 24.0.7.
- Update `github.com/hashicorp/consul/api` from 1.24.0 to 1.25.1.
- Update `github.com/hashicorp/consul/api` from 1.25.1 to 1.26.1.
- Update `github.com/nats-io/nkeys` from 0.4.5 to 0.4.6.
- Update `github.com/prometheus/client_golang` from 1.16.0 to 1.17.0.
- Update `github.com/rabbitmq/amqp091-go` from 1.8.1 to 1.9.0.
- Update `github.com/showwin/speedtest-go` from 1.6.6 to 1.6.7.
- Update `google.golang.org/grpc` from 1.58.2 to 1.58.3.
- Update `k8s.io/client-go` from 0.28.2 to 0.28.3.

## v1.28.3

### Bug Fixes

- Infiniband (`inputs.infiniband`): Handle devices without counters.
- Jenkins (`inputs.jenkins`): Filter after searching sub-folders.
- Jolokia2 Agent (`inputs.jolokia2_agent`): Trim quotes around tags.
- JSON (`serializers.json`): Append newline for batch-serialization.
- Kafka (`outputs.kafka`): Simplify send-error handling.
- MQTT (`inputs.mqtt`): Reference correct password variable.
- Nebius Cloud Monitoring (`outputs.nebius_cloud_monitoring`): Use correct endpoint.
- PostgreSQL Extensible (`inputs.postgresql_extensible`): Restore default db name.
- Redis Time Series (`outputs.redistimeseries`): Handle string fields correctly.
- s7comm (`inputs.s7comm`): Allow PDU-size to be set as config option.
- Vault (`inputs.vault`): Use http client to handle redirects correctly.

### Dependency updates

- Update `github.com/apache/arrow/go/v13` from 13.0.0-git to 13.0.0.
- Update `github.com/google/cel-go` from 0.14.1-git to 0.18.1.
- Update `github.com/google/go-cmp` from 0.5.9 to 0.6.0.
- Update `github.com/jhump/protoreflect` from 1.15.1 to 1.15.3.
- Update `github.com/klauspost/compress` from 1.16.7 to 1.17.0.
- Update `github.com/miekg/dns` from 1.1.55 to 1.1.56.
- Update `github.com/nats-io/nats.go` from 1.28.0 to 1.31.0.
- Update `github.com/nats-io/nats-server/v2` from 2.9.9 to 2.9.23.
- Update `github.com/netsampler/goflow2` from 1.3.3 to 1.3.6.
- Update `github.com/signalfx/golib/v3` from 3.3.50 to 3.3.53.
- Update `github.com/testcontainers/testcontainers-go` from 0.22.0 to 0.25.0.
- Update `github.com/yuin/goldmark` from 1.5.4 to 1.5.6.
- Update `golang.org/x/mod` from 0.12.0 to 0.13.0.
- Update `golang.org/x/net` from 0.15.0 to 0.17.0.
- Update `golang.org/x/oauth2` from 0.11.0 to 0.13.0.
- Update `gonum.org/v1/gonum` from 0.13.0 to 0.14.0.
- Update `google.golang.org/api` from 0.139.0 to 0.147.0.

## v1.28.2

### Bug Fixes

- Cisco Telemetry MDT (`inputs.cisco_telemetry_mdt`): Print string message on decode failure.
- Cloudwatch (`outputs.cloudwatch`): Increase number of metrics per write.
- exec (`inputs.exec`): Clean up grandchildren processes.
- Intel PMT (`inputs.intel_pmt`): Handle telem devices without numa\_node attribute.
- JTI OpenConfig Telemetry (`inputs.jti_openconfig_telemetry`): Do not block gRPC dial.
- JSON v2 (`parsers.json_v2`): Handle optional fields properly.
- Mock (`inputs.mock`): Align plugin with documentation.
- NFS Client (`inputs.nfsclient`): Avoid panics, better error messages.
- Nvidia SMI (`inputs.nvidia_smi`): Add legacy power readings to v12 schema.
- OpenStack (`inputs.openstack`): Handle dependencies between enabled services and available endpoints.
- PostgreSQL Extensible (`inputs.postgresql_extensible`): Restore outputaddress behavior.
- SMART (`inputs.smart`): Remove parsing error message.
- Stackdriver (`outputs.stackdriver`):
    - Do not shallow copy map.
    - Drop metrics on InvalidArgument gRPC error.
- systemd Units `inputs.systemd_units`): Add missing upstream states.
- Template (`processors.template`): Handle tracking metrics correctly.

### Dependency updates

- Update `github.com/aliyun/alibaba-cloud-sdk-go` from 1.62.470 to 1.62.563.
- Update `github.com/aws/aws-sdk-go-v2/config` from 1.18.27 to 1.18.42.
- Update `github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs` from 1.20.9 to 1.23.5.
- Update `github.com/aws/aws-sdk-go-v2/service/ec2` from 1.80.1 to 1.120.0.
- Update `github.com/aws/aws-sdk-go-v2/feature/ec2/imds` from 1.13.8 to 1.13.11.
- Update `github.com/eclipse/paho.mqtt.golang` from 1.4.2 to 1.4.3.
- Update `github.com/google/uuid` from 1.3.0 to 1.3.1.
- Update `github.com/shirou/gopsutil/v3` from 3.23.6 to 3.23.8.
- Update `github.com/vmware/govmomi` from 0.28.0 to 0.32.0.
- Update `golang.org/x/net` from 0.14.0 to 0.15.0.
- Update `k8s.io/api` from 0.28.1 to 0.28.2.

## v1.28.1

### Bug fixes

- Packaging: Revert permission change on package configs
- Redis (`inputs.redis`): Fix password typo
- Vsphere (`inputs.vsphere`): Fix config name typo in example

## v1.28.0

### Important Changes

- **metricpass**: Removed the Python compatibility support for “not”, “and”, and “or” keywords. This support was incorrectly removing these keywords from actual data. Users should instead use the standard “!”, “&&”, and “||” operators.
- **Avro Processor**: The avro processor will no longer create a timestamp field by default unless explicitly provided in the parser config.

### New Plugins

#### Inputs

- [Intel PMT](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/intel_pmt) (`inputs.intel_pmt`)
- [S7comm](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/s7comm) (`inputs.s7comm`)
- [Tacacs](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/tacacs) (`inputs.tacacs`)

#### Processors

- [Split metrics](https://github.com/influxdata/telegraf/tree/master/plugins/processors/split) (`processors.split`)

#### Secret Stores

- [OAuth2 services](https://github.com/influxdata/telegraf/tree/master/plugins/secretstores/oauth2) (`secretstores.oauth2`)

#### Serializers

- [Template based](https://github.com/influxdata/telegraf/tree/master/plugins/serializers/template) (`serializers.template`)

### Features

- Agent:
    - Add option to avoid filtering of global tags
    - Watch default config files if none specified
- CLI: Add plugins subcommand to list available and deprecated
- AMQP Consumer (`inputs.amqp_consumer`): Add support to rabbitmq stream queue
- Cisco Telemetry MDT (`inputs.cisco_telemetry_mdt`): Add microbust support
- Couchbase (`inputs.couchbase`): Add failover metrics
- Fail2Ban (`inputs.fail2ban`): Allow specification of socket
- Fibaro (`inputs.fibaro`): Support HC3 device types
- HTTP (`inputs.http`): Rework token options
- InfluxDB Listener (`inputs.influxdb_listener`): Add token based authentication
- Internal (`inputs.internal`): Add Go metric collection option
- Jenkins (`inputs.jenkins`): Add option for node labels as tag
- JTI OpenConfig Telemetry (`inputs.jti_openconfig_telemetry`): Add keep-alive setting
- Kernel (`inputs.kernel`): Collect KSM metrics
- Modbus (`inputs.modbus`): Add per-metric configuration style
- Nvidia SMI (`inputs.nvidia_smi`):
    - Add Nvidia DCGM MIG usage values
    - Add additional fields
    - Support newer data schema versions
- OpenStack (`inputs.openstack`): Gather cinder services
- OpenTelemetry (`inputs.opentelemetry`): Add configurable log record dimensions
- PGBouncer (`inputs.pgbouncer`): Add show\_commands to select the collected pgbouncer metrics
- PostgreSQL Extensible (`inputs.postgresql_extensible`): Introduce max\_version for query
- Procstat (`inputs.procstat`): Add status field
- Prometheus (`inputs.prometheus`): Always apply kubernetes label and field selectors
- RavenDB (`inputs.ravendb`): Add new disk metrics fields
- Redfish (`inputs.redfish`): Add additional chassis tags
- Redis (`inputs.redis`):
    - Add additional commandstat fields
    - Support of redis 6.2 ERRORSTATS
- Redis Sentinel (`inputs.redis_sentinel`): Allow username and password
- Solr (`inputs.solr`): Support version 7.x to 9.3
- SQL Server (`inputs.sqlserver`): Add IsHadrEnabled server property
- Vsphere (`inputs.vsphere`):
    - Allow to set vSAN sampling interval
    - Support explicit proxy setting
- Internal (`internal`):
    - Add gather\_timeouts metric
    - Add zstd to internal content\_coding
- Kafka (`kafka`): Set and send SASL extensions
- Migrations:
    - Add migration for inputs.httpjson
    - Add migration for inputs.io
- execd (`outputs.execd`): Add option for batch format
- File (`outputs.file`): Add compression
- HTTP (`outputs.http`): Allow PATCH method
- Postgresql (`outputs.postgresql`):
    - Add option to create time column with timezone
    - Add option to rename time column
- Prometheus Client (`outputs.prometheus_client`): Add secretstore support for basic\_password
- Wavefront (`outputs.wavefront`): Add more auth options and update SDK
- Avro (`parsers.avro`): Add support for JSON format
- Influx (`parsers.influx`): Allow a user to set the timestamp precision
- Value (`parsers.value`): Add support for automatic fallback for numeric types
- XPath (`parsers.xpath`):
    - Add Concise Binary Object Representation parser
    - Add option to store fields as base64
- Parser (`processors.parser`) Allow also non-string fields
- Template (`processors.template`): Unify template metric

### Bug fixes

- Packaging: Change the systemd KillMode from control-group to mixed
- AMQP Consumer (`inputs.amqp_consumer`): Print error on connection failure
- Kafka Consumer (`inputs.kafka_consumer`): Use per-message parser to avoid races
- OPCUA (`inputs.opcua`): Verify groups or root nodes included in config
- PostgreSQL (`inputs.postgresql`): Fix default database definition
- Procstat (`inputs.procstat`): Collect swap via /proc/$pid/smaps
- SQL Server (`inputs.sqlserver`): Cast max\_size to bigint
- Sysstat (`inputs.sysstat`): Remove tmpfile to avoid file-descriptor leak
- Avro (`parsers.avro`):
    - Do not force addition of timestamp as a field
    - Handle timestamp format checking correctly
- SQL (`sql`):
    - Allow sqlite on Windows (amd64 and arm64)
    - Move conversion\_style config option to the right place of sample config

### Dependency updates

- Update `github.com/aws/aws-sdk-go-v2/service/kinesis` from 1.18.2 to 1.18.5.
- Update `github.com/hashicorp/consul/api` from 1.20.0 to 1.24.0.
- Update `github.com/nats-io/nats.go` from 1.27.0 to 1.28.0.
- Update `github.com/prometheus/prometheus` from 0.42.0 to 0.46.0.
- Update `github.com/showwin/speedtest-go` from 1.6.2 to 1.6.6.
- Update `k8s.io/api` from 0.27.4 to 0.28.1.

## v1.27.4

### Bug fixes

- Cisco Telemetry MDT (`inputs.cisco_telemetry_mdt`): Fix MDT source field overwrite.
- NowMetric (`serializers.nowmetric`): Add option for JSONv2 format.
- OPCUA (`inputs.opcua`): Register node IDs again on reconnect.
- OPCUA Listener (`inputs.opcua_listener`): Avoid segfault when subscription was not successful.
- Stackdriver (`outputs.stackdriver`): Regenerate time interval for unknown metrics.
- Xpath (`parsers.xpath`): Handle protobuf maps correctly.

### Dependency updates

- Update `cloud.google.com/go/pubsub` from 1.32.0 to 1.33.0.
- Update `github.com/aws/aws-sdk-go-v2/credentials` from 1.13.26 to 1.13.32.
- Update `github.com/aws/aws-sdk-go-v2/feature/ec2/imds` from 1.13.4 to 1.13.7.
- Update `github.com/aws/aws-sdk-go-v2/service/kinesis` from 1.17.14 to 1.18.0.
- Update `github.com/aws/aws-sdk-go-v2/service/kinesis` from 1.18.0 to 1.18.2.
- Update `github.com/aws/aws-sdk-go-v2/service/sts` from 1.19.3 to 1.21.2.
- Update `github.com/gophercloud/gophercloud` from 1.2.0 to 1.5.0.
- Update `github.com/microsoft/go-mssqldb` from 1.3.1-0.20230630170514-78ad89164253 to 1.5.0.
- Update `github.com/miekg/dns` from 1.1.51 to 1.1.55.
- Update `github.com/openconfig/gnmi` from 0.9.1 to 0.10.0.
- Update `github.com/santhosh-tekuri/jsonschema/v5` from 5.3.0 to 5.3.1.
- Update `go.mongodb.org/mongo-driver` from 1.11.6 to 1.12.1.
- Update `golang.org/x/oauth2` from 0.10.0 to 0.11.0.
- Update `google.golang.org/api` from 0.129.0 to 0.134.0.

## v1.27.3

### Bug fixes

- Agent (`agent`): Respect processor order in file.
- Config (`config`):
    - Handle escaping and quotation correctly.
    - Setup logger for secret-stores.
- Custom Builder (`tools.custom_builder`): Ignore non-plugin sections during configuration.
- Docker (`inputs.docker`): Add restart count.
- JTI OpenConfig Telemetry (`inputs.jti_openconfig_telemetry`): Reauthenticate connection on reconnect.
- MQTT Consumer (`inputs.mqtt_consumer`): Add client trace logs via option.
- Nebius Cloud Monitoring (`outputs.nebius_cloud_monitoring`): Replace reserved label names.
- OpenTelemetry (`outputs.opentelemetry`): Group metrics by age and timestamp.
- Prometheus (`inputs.prometheus`):
    - Do not collect metrics from finished pods.
    - Fix missing metrics when multiple plugin instances specified.
- Stackdriver (`outputs.stackdriver`): Add tag as resource label option.
- Xpath (`parsers.xpath`):
    - Ensure precedence of explicitly defined tags and fields.
    - Fix field-names for arrays of simple types.
    - Improve handling of complex-type nodes.

### Dependency updates

- Update `github.com/aliyun/alibaba-cloud-sdk-go` 1.62.389 to 1.62.470.
- Update `github.com/antchfx/jsonquery` from 1.3.1 to 1.3.2.
- Update `github.com/antchfx/xmlquery` from 1.3.15 to 1.3.17.
- Update `github.com/antchfx/xpath` from v1.2.4 to latest master.
- Update `github.com/aws/aws-sdk-go-v2/service/dynamodb` from 1.17.3 to 1.20.0.
- Update `github.com/aws/aws-sdk-go-v2/service/sts` from 1.19.2 to 1.19.3.
- Update `github.com/eclipse/paho.golang` from 0.10.0 to 0.11.0.
- Update `github.com/go-ldap/ldap/v3` from 3.4.4 to 3.4.5.
- Update `github.com/jaegertracing/jaeger` from 1.38.0 to 1.47.0.
- Update `github.com/opensearch-project/opensearch-go/v2` from 2.2.0 to 2.3.0.
- Update `github.com/prometheus-community/pro-bing` from 0.2.0 to 0.3.0.
- Update `github.com/shirou/gopsutil/v3` from 3.23.5 to 3.23.6.
- Update `github.com/thomasklein94/packer-plugin-libvirt` from 0.3.4 to 0.5.0.
- Update `k8s.io/api` from 0.27.2 to 0.27.4.
- Update `k8s.io/apimachinery` from 0.27.2 to 0.27.3.
- Update `modernc.org/sqlite` from 1.23.1 to 1.24.0.

## v1.27.2

### Bug fixes

- Binary (`parsers.binary`): Fix binary parser example in README.md.
- Config (`config`): Replace environment variables if existing but empty.
- Cloud PubSub (`inputs.cloud_pubsub`): Properly lock for decompression.
- Custom Builder (`tools.custom_builder`): Error out for unknown plugins in configuration.
- GNMI (`inputs.gnmi`): Add option to explicitly trim field-names.
- Graphite (`outputs.graphite`): Rework connection handling.
- Grok (`parsers.grok`): Use UTC as the default timezone.
- InfluxDB v2 (`outputs.influxdb_v2`): Expose HTTP/2 client timeouts.
- Internet Speed (`inputs.internet_speed`): Add location as a field.
- Modbus (`inputs.modbus`):
    - Check number of register for datatype.
    - Fix optimization of overlapping requests and add warning.
- MQTT Consumer (`inputs.mqtt_consumer`):
    - Correctly handle semaphores on messages.
    - Print warning on no metrics generated.
- OPC UA (`inputs.opcua`): Ensure connection after reconnect.
- PHP FPM (`inputs.phpfpm`): Check address length to avoid crash.
- Printer (`processors.printer`): Convert output to string.
- SNMP Trap (`inputs.snmp_trap`): Copy GoSNMP global defaults to prevent side-effects.
- Secretstores (`secretstores`): Skip dbus connection with kwallet.
- Splunk Metric (`serializers.splunkmetric`): Fix TOML option name for multi-metric.
- Stackdriver (`outputs.stackdriver`): Options to use official path and types.
- Sumologic (`outputs.sumologic`): Unwrap serializer for type check.
- Vsphere (`inputs.vpshere`): Compare versions as a string.
- Xpath (`parsers.xpath`): Handle explicitly defined fields correctly.

### Dependency updates

- Replace `github.com/denisenkom/go-mssqldb` with `github.com/microsoft/go-mssqldb`.
- Update `cloud.google.com/go/bigquery` from 1.51.1 to 1.52.0.
- Update `github.com/aliyun/alibaba-cloud-sdk-go` from 1.62.337 to 1.62.389.
- Update `github.com/aws/aws-sdk-go-v2/config` from 1.18.8 to 1.18.27.
- Update `github.com/aws/aws-sdk-go-v2/service/kinesis` from 1.17.8 to 1.17.14.
- Update `github.com/gopcua/opcua` from 0.3.7 to 0.4.0.
- Update `github.com/prometheus/client_golang` from 1.15.1 to 1.16.0.
- Update `github.com/snowflakedb/gosnowflake` from 1.6.13 to 1.6.22.
- Update `github.com/urfave/cli/v2` from 2.25.5 to 2.25.7.
- Update `golang.org/x/text` from 0.9.0 to 0.10.0.
- Update `golang.org/x/text` from 0.10.0 to 0.11.0.
- Update `google.golang.org/api` from 0.126.0 to 0.129.0.

## v1.27.1

### Bug fixes

- Correctly handle serializers and parsers with custom builder.
- Handle compression level correctly for different algorithms.
- Restore old environment var behavior with option.

### Dependency updates

- Update `github.com/aws/aws-sdk-go-v2/credentials` from 1.13.20 to 1.13.26.
- Update `github.com/aws/aws-sdk-go-v2/service/cloudwatch` from 1.25.9 to 1.26.2.
- Update `github.com/aws/aws-sdk-go-v2/service/timestreamwrite` from 1.16.0 to 1.17.2.
- Update `github.com/go-sql-driver/mysql` from 1.6.0 to 1.7.1.
- Update `github.com/jackc/pgx/v4` from 4.17.1 to 4.18.1.
- Update `github.com/nats-io/nats.go` from 1.24.0 to 1.27.0.
- Update `github.com/prometheus-community/pro-bing` from 0.1.0 to 0.2.0.
- Update `golang.org/x/crypto` from 0.8.0 to 0.9.0.
- Update `golang.org/x/term` from 0.8.0 to 0.9.0.
- Update `modernc.org/sqlite` from 1.21.0 to 1.23.1.

## v1.27.0

### Important Changes

- **Timezone Parsing**: Fix parsing of timezone abbreviations such as `MST`. Up to now, when parsing times with abbreviated timezones (i.e. the format ) the timezone information is ignored completely and the *timestamp* is located in UTC. This is a golang issue (see [#9617](https://github.com/golang/go/issues/9617) or [#56528](https://github.com/golang/go/issues/56528)). If you worked around that issue, please remove the workaround before using v1.27+. In case you experience issues with abbreviated timezones please file an issue.
- **Internal Parser methods**: Removal of old-style parser creation. This should not directly affect users as it is an API change. All parsers in Telegraf are already ported to the new framework. If you experience any issues with not being able to create parsers let us know!

### New Plugins

#### Inputs

- [ctrlX Data Layer](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/ctrlx_datalayer) (`inputs.ctrlx_datalayer`)
- [Intel Baseband Accelerator](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/intel_baseband) (`inputs.intel_baseband`)

#### Outputs

- [Clarify](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/clarify) (`outputs.clarify`)
- [Nebius Cloud Monitoring](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/nebius_cloud_monitoring) (`outputs.nebius_cloud_monitoring`)

#### Processors

- [Scale](https://github.com/influxdata/telegraf/tree/master/plugins/processors/scale) (`processors.scale`)

#### Secret Stores

- [Docker](https://github.com/influxdata/telegraf/tree/master/plugins/secretstores/docker) (`secretstores.docker`)
- [HTTP](https://github.com/influxdata/telegraf/tree/master/plugins/secretstores/http) (`secretstores.http`)

#### Serializers

- [Cloud Events](https://github.com/influxdata/telegraf/tree/master/plugins/serializers/cloudevents) (`serializers.cloudevents`)

### Features

- Agent (`agent`):
    - Add option to avoid filtering of explicit plugin tags
    - Add common expression language metric filtering
- BasicStats (`aggregators.basicstats`): Add percentage change
- Cloud PubSub (`cloud_pubsub`): Add support for gzip compression
- OPCUA (`common.opcua`): Add support for secret-store secrets
- TLS (`common.tls`): Add support for passphrase-protected private key
- Config (`config`):
    - Add framework for migrating deprecated plugins
    - Support shell like syntax for environment variable substitution
- Cloudwatch (`inputs.cloudwatch`): Add support for cross account observability
- Directory Monitor (`inputs.directory_monitor`): Improve internal stats
- Filecount (`inputs.filecount`): Add oldestFileTimestamp and newestFileTimestamp
- GNMI (`inputs.gnmi`):
    - Allow canonical field names
    - Support Juniper GNMI Extension Header
- Internet Speed (`inputs.internet_speed`): Support multi-server test
- Kafka Consumer (`inputs.kafka_consumer`): Add regular expression support for topics
- Kubernetes (`inputs.kubernetes`): Extend kube\_inventory plugin to include and extend resource quota, secret, node, and pod measurement
- Nats Consumer (`inputs.nats_consumer`): Add receiver subject as tag
- Netflow (`inputs.netflow`):
    - Add sFlow decoder
    - Allow custom PEN field mappings
- Nvidia SMI (`inputs.nvidia_smi`): Add additional memory related fields
- Open Telemetry (`inputs.opentelemetry`): Add configurable span dimensions
- Prometheus (`inputs.prometheus`): Control which pod metadata is added as tags
- SQL (`inputs.sql`):
    - Add disconnected\_servers\_behavior field in the configuration
    - Add FlightSQL support
- SQL Server (`inputs.sqlserver`):
    - Add Azure Arc-enabled SQL MI support
    - Check SQL Server encryptionEnforce with xp\_instance\_regread
- StatsD (`inputs.statsd`): Add optional temporality and start\_time tag for statsd metrics
- Suricata (`inputs.suricata`): Add ability to parse drop or rejected
- Vsphere (`inputs.vsphere`): Add vSAN extension
- Internal (`internal`): Add additional faster compression options
- Loki (`outputs.loki`): Add option for metric name label
- Wavefront (`outputs.wavefront`): Add TLS and HTTP Timeout configuration fields
- OpenTSDB (`parsers.opentsdb`): Add OpenTSDB data format parser
- AWS EC2 (`processors.aws_ec2`): Add caching of imds and ec2 tags
- Parser (`processors.parser`): Add merge with timestamp option
- Scale (`processors.scale`): Add scaling by factor and offset
- Template (`processors.template`): Allow tag to be a template
- Prometheus Remote (`serializer.prometheusremote`): Improve performance
- Test (`test`): Allow to capture all messages during test

### Bug fixes

- Cloud PubSub (`inputs.cloud_pubsub`): Fix gzip decompression.
- GNMI (`inputs.gnmi`):
    - Allow optional origin for update path.
    - Handle canonical field-name correctly for non-explicit subscriptions.
- MQTT (`inputs.mqtt`): ACK messages when persistence is enabled.
- MySQL (`inputs.mysql`): Update MariaDB Dialect regex version check.
- Netflow (`inputs.netflow`):
    - Fix field mappings.
    - Handle PEN messages correctly.
- Prometheus (`inputs.prometheus`): Avoid race when creating informer factory.
- Socket Listener (`inputs.socket_listener`): Avoid noisy logs on closed connection.
- Temp (`inputs.temp`): Ignore warnings and instead return only errors.
- UPSD (`inputs.upsd`): Handle float battery.runtime value.
- Internal (`internal`): Fix time parsing for abbreviated timezones.
- SQL (`outputs.sql`): Use config.duration to correctly to parse toml config.
- Wavefront (`outputs.wavefront`): Flush metric buffer before reaching overflow.
- Lookup (`processors.lookup`): Do not strip tracking info.
- Influx (`serializers.influx`): Restore disabled uint support by default.

### Dependency updates

- Update cloud.google.com/go/monitoring from 1.13.0 to 1.14.0.
- Update github.com/aliyun/alibaba-cloud-sdk-go from 1.62.193 to 1.62.337.
- Update github.com/aws/aws-sdk-go-v2/feature/ec2/imds from 1.13.2 to 1.13.3.
- Update github.com/aws/aws-sdk-go-v2/service/sts from 1.18.9 to 1.19.0.
- Update github.com/Azure/azure-event-hubs-go/v3 from 3.4.0 to 3.5.0.
- Update github.com/Azure/go-autorest/autorest from 0.11.28 to 0.11.29.
- Update github.com/influxdata/influxdb-observability libraries from 0.3.3 to 0.3.15.
- Update github.com/jackc/pgconn from 1.13.0 to 1.14.0.
- Update github.com/jackc/pgtype from 1.12.0 to 1.14.0.
- Update github.com/Mellanox/rdmamap to 1.1.0.
- Update github.com/pion/dtls/v2 from 2.2.6 to 2.2.7.
- Update github.com/prometheus/common from 0.43.0 to 0.44.0.
- Update github.com/rabbitmq/amqp091-go from 1.8.0 to 1.8.1.
- Update github.com/shirou/gopsutil from 3.23.4 to 3.23.5.
- Update github.com/showwin/speedtest-go from 1.5.2 to 1.6.2.
- Update github.com/urfave/cli/v2 from 2.23.5 to 2.25.5.
- Update k8s.io/client-go from 0.26.2 to 0.27.2.

## v1.26.3

### Bug fixes

- GNMI (`inputs.gnmi`): Create selfstat to track connection state.
- Graphite (`outputs.graphite`): Fix logic to reconnect with servers that were not up on agent startup.
- Intel PMU (`inputs.intel_pmu`): Fix handling of the json perfmon format.
- Prometheus Client (`outputs.prometheus_client`): Fix export\_timestamp for v1 metric type.
- Socket Listener (`inputs.socket_listener`):
    - Fix loss of connection tracking.
    - Fix race in tests.
- Stackdriver (`outputs.stackdriver`):
    - Allow for custom metric type prefix.
    - Group batches by timestamp.
- Starlark (`processors.starlark`): Do not reject tracking metrics twice.
- Vsphere (`inputs.vsphere`): Specify the correct option for disconnected\_servers\_behavior.
- Warp10 (`outputs.warp10`): Support Infinity/-Infinity/NaN values.

### Dependency updates

- Update `cloud.google.com/go/pubsub` from 1.30.0 to 1.30.1.
- Update `github.com/aerospike/aerospike-client-go/v5` from 5.10.0 to 5.11.0.
- Update `github.com/antchfx/xpath` to latest master for string-join().
- Update `github.com/aws/aws-sdk-go-v2` from 1.17.8 to 1.18.0.
- Update `github.com/Azure/go-autorest/autorest/adal` from 0.9.22 to 0.9.23.
- Update `github.com/benbjohnson/clock` from 1.3.0 to 1.3.3.
- Update `github.com/docker/distribution` from 2.8.1 to 2.8.2.
- Update `github.com/fatih/color` from 1.13.0 to 1.15.0.
- Update `github.com/netsampler/goflow2` from 1.1.1 to 1.3.3.
- Update `github.com/yuin/goldmark` from 1.5.3 to 1.5.4.
- Update `go.opentelemetry.io/collector/pdata` from 1.0.0-rc7 to 1.0.0-rcv0011.
- Update `golang.org/x/net` from 0.8.0 to 0.9.0.
- Update `golang.org/x/net` from 0.9.0 to 0.10.0.
- Update `golang.org/x/oauth2` from 0.5.0 to 0.7.0.
- Update `google.golang.org/api` from 0.106.0 to 0.120.0.
- Update `govulncheck-action` from 0.10.0 to 0.10.1.
- Update `prometheus` from v1.8.2 to v2.42.0.
- Update `signalfx/golib` from 3.3.46 to 3.3.50.

## v1.26.2

### Bug fixes

- Agent (`agent`): Pass quiet flag earlier.
- Grok (`parsers.grok`): Fix nil metric for multiline inputs.
- Lookup (`processors.lookup`): Fix tracking metrics.
- Prometheus (`inputs.prometheus`): Add namespace option in k8s informer factory.
- Socket Listener (`inputs.socket_listener`): Fix tracking of unix sockets.

### Dependency updates

- Update `github.com/aws/aws-sdk-go-v2/credentials` from 1.13.15 to 1.13.20.
- Update `github.com/aws/aws-sdk-go-v2/service/cloudwatch` from 1.21.6 to 1.25.9.
- Update `github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs` from 1.15.13 to 1.20.9.
- Update `github.com/aws/aws-sdk-go-v2/service/kinesis` from 1.15.19 to 1.17.8.
- Update `github.com/aws/aws-sdk-go-v2/service/sts` from 1.18.5 to 1.18.9.
- Update `github.com/docker/docker` from 23.0.0 to 23.0.4.
- Update `github.com/openconfig/gnmi` from 0.0.0-20220920173703-480bf53a74d2 to 0.9.1.
- Update `github.com/prometheus/common` from 0.41.0 to 0.42.0.
- Update `github.com/safchain/ethtool` from 0.2.0 to 0.3.0.
- Update `github.com/tinylib/msgp` from 1.1.6 to 1.1.8.
- Update `github.com/vishvananda/netns` from 0.0.2 to 0.0.4.
- Update `github.com/wavefronthq/wavefront-sdk-go` from 0.11.0 to 0.12.0.

## v1.26.1

### Bug fixes

- Config (`config`): Return error on order set as string.
- ethtool (`inputs.ethtool`): Check for nil.
- execd (`inputs.execd`): Add option to set buffer size.
- Graphite (`outputs.graphite`): Add custom regex to outputs.
- Graphite (`serializers.graphite`): Allow for specifying regex to sanitize.
- Internet Speed (`inputs.internet_speed`): Rename host tag to source.
- Kubernetes (`inputs.kubernetes`): Apply timeout for the whole HTTP request.
- Netflow (`inputs.netflow`): Use correct name in the build tag.
- Procstat (`inputs.procstat`): Return tags of pids if lookup\_error.
- Prometheus (`inputs.prometheus`):
    - Correctly set timeout param.
    - Use set over add for custom headers.
- Secret Stores (`secrets`):
    - Add function to set a secret.
    - Minimize secret holding time.
    - Warn if OS limit for locked memory is too low.
    - Handle array of secrets correctly.
- systemd (`systemd`): Increase lock memory for service to 8192kb.
- UPSD (`inputs.upsd`): Include ups.real\_power.

### Dependency updates

- Update `github.com/antchfx/xpath` from 1.2.3 to 1.2.4.
- Update `github.com/apache/thrift` from 0.16.0 to 0.18.1.
- Update `github.com/Azure/azure-event-hubs-go/v3` from 3.3.20 to 3.4.0.
- Update `github.com/Azure/go-autorest/autorest/azure/auth` from 0.5.11 to 0.5.12.
- Update `github.com/golang-jwt/jwt/v4` from 4.4.2 to 4.5.0.
- Update `github.com/jhump/protoreflect` from 1.8.3-0.20210616212123-6cc1efa697ca to 1.15.1.
- Update `github.com/nats-io/nats.go` from 1.19.0 to 1.24.0.
- Update `github.com/opencontainers/runc` from 1.1.4 to 1.1.5.
- Update `github.com/pion/dtls/v2` from 2.2.4 to 2.2.6.
- Update `github.com/rabbitmq/amqp091-go` from 1.7.0 to 1.8.0.
- Update `github.com/shirou/gopsutil` from 3.23.2 to 3.23.3.
- Update `github.com/Shopify/sarama` from 1.37.2 to 1.38.1.
- Update `github.com/sensu/sensu-go/api/core/v2` from 2.15.0 to 2.16.0.
- Update `github.com/tidwall/gjson` from 1.14.3 to 1.14.4.
- Update `golang.org/x/net` from 0.7.0 to 0.8.0.
- Update `modernc.org/sqlite` from 1.19.2 to 1.21.0.

## v1.26.0

### Important Changes

- **Static builds**: Linux builds are now statically built. Other operating systems were cross-built in the past and as a result, already static. Users should not notice any change in behavior. The `_static` specific Linux binary is no longer produced as a result.
- **telegraf.d behavior**: The default behavior of reading `/etc/telegraf/telegraf.conf` now includes any `.conf` files under `/etc/telegraf/telegraf.d/`. This change will apply to the official Telegraf Docker image as well. This will simplify Docker usage when using multiple configuration files.
- **Default configuration**: The `telegraf config` command and default config file provided by Telegraf now includes all plugins and produces the same output across all operating systems. Plugin comments specify what platforms are supported or not.
- **State persistence**: State persistence is now available in select plugins. This will allow plugins to start collecting data, where they left off. A configuration with state persistence cannot change or it will not be able to recover.

### New Plugins

#### Inputs

- [Opensearch Query](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/opensearch_query) (`inputs.opensearch_query`)
- [P4Runtime](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/p4runtime) (`inputs.p4runtime`)
- [Radius Auth Response Time](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/radius) (`inputs.radius`)
- [Windows Management Instrumentation (WMI)](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/win_wmi) (`inputs.win_wmi`)

#### Parsers

- [Apache Avro](https://github.com/influxdata/telegraf/tree/master/plugins/parsers/avro) (`parsers.avro`)

#### Processors

- [lookup](https://github.com/influxdata/telegraf/tree/master/plugins/processors/lookup) (`processors.lookup`)

### Features

- Always disable cgo support (static builds).
- Plugin state-persistence.
- Add `/etc/telegraf/telegraf.d` to default configuration file locations.
- Print loaded configurations.
- Accept durations given in days (e.g. 7d).
- OAuth (`common.oauth`): Add `audience` parameter.
- TLS (`common.tls`): Add `enable` flag.
- CGroups (`inputs.cgroup`): Add support for `cpu.stat`.
- Cisco Telemetry MDT (`inputs.cisco_telemetry_mdt`): Include `delete` field.
- Disk (`inputs.disk`): Add label as tag.
- DNS Query (`inputs.dns_query`): Add IP fields.
- Docker Log (`inputs.docker_log`): Add state-persistence capabilities.
- Ethtool (`inputs.ethtool`): Add support for link speed, duplex, etc.
- GNMI (`inputs.gnmi`): Set max gRPC message size.
- HA Proxy (`inputs.haproxy`): Add support for TCP endpoints in haproxy plugin.
- HTTP Listener v2 (`inputs.http_listener_v2`): Add custom server HTTP headers.
- Icinga2 (`inputs.icinga2`): Support collecting hosts, services, and endpoint metrics.
- InfluxDB (`inputs.influxdb`): Collect uptime statistics.
- Intel PowerStat (`inputs.intel_powerstat`): Add CPU base frequency metric and add support for new platforms.
- Internet Speed (`inputs.internet_speed`):
    - Add the best server selection via latency and jitter field.
    - Server ID include and exclude filter.
- JTI OpenConfig Telemtry (`inputs.jti_openconfig_telemetry`): Set timestamp from data.
- Modbus (`inputs.modbus`):
    - Add RS485 specific config options.
    - Add workaround to enforce reads from zero for coil registers.
    - Allow to convert coil and discrete registers to boolean.
- MySQL (`inputs.mysql`): Add secret-store support.
- Open Weather Map (`inputs.openweathermap`): Add `snow` parameter.
- Processes (`inputs.processes`): Add use\_sudo option for BSD.
- Prometheus (`inputs.prometheus`): Use namespace annotations to filter pods to be scraped.
- Redfish (`inputs.redfish`): Add power control metric.
- SQL Server (`inputs.sqlserver`): Get database pages performance counter.
- Stackdriver (`inputs.stackdriver`): Allow filtering by resource metadata labels.
- Statsd (`inputs.statsd`): Add pending messages stat and allow to configure number of threads.
- Vsphere (`inputs.vsphere`): Flag for more lenient behavior when connect fails on startup.
- Windows Event Log (`inputs.win_eventlog`): Add state-persistence capabilities.
- Windows Performance Counters (`inputs.win_perf_counters`): Add remote system support.
- Wireguard (`inputs.wireguard`): Add allowed\_peer\_cidr field.
- x509 Certificates (`inputs.x509_cert`):
    - Add OCSP stapling information for leaf certificates.
    - Add tag for certificate type-classification.
- MQTT (`outputs.mqtt`):
    - Add option to specify topic layouts.
    - Add support for MQTT 5 publish properties.
    - Enhance routing capabilities.
- XPath Parser (`parsers.xpath`): Add timezone handling.
- Converter Processor (`processors.converter`): Convert tag or field as metric timestamp.
- Unpivot Processor (`processors.unpivot`): Add mode to create new metrics.
- Secret Stores:
    - Add command-line option to specify password.
    - Add support for additional input plugins.
    - Convert many output plugins.

### Bug fixes

- Allow graceful shutdown on interrupt (e.g. Ctrl-C).
- Only rotate log on SIGHUP if needed.
- AMQP Consumer (`inputs.amqp_consumer`):
    - Avoid deprecations when handling defaults.
    - Fix panic on Stop() if not connected successfully.
- ethtool (`inputs.ethtool`): Close namespace file to prevent crash.
- statsd (`inputs.statsd`): On close, verify listener is not nil.

### Dependency updates

- Update cloud.google.com/go/storage from 1.28.1 to 1.29.0.
- Update github.com/Azure/go-autorest/autorest/adal from 0.9.21 to 0.9.22.
- Update github.com/aliyun/alibaba-cloud-sdk-go from 1.62.77 to 1.62.193.
- Update github.com/aws/aws-sdk-go-v2/credentials from 1.13.2 to 1.13.15.
- Update github.com/aws/aws-sdk-go-v2/service/timestreamwrite from 1.14.5 to 1.16.0.
- Update github.com/coocood/freecache from 1.2.2 to 1.2.3.
- Update github.com/karrick/godirwalk from v1.17.0 to v1.16.2.
- Update github.com/opencontainers/runc from 1.1.3 to 1.1.4.
- Update github.com/opensearch-project/opensearch-go/v2 from 2.1.0 to 2.2.0.
- Update github.com/openzipkin-contrib/zipkin-go-opentracing from 0.4.5 to 0.5.0.
- Update github.com/rabbitmq/amqp091-go from 1.5.0 to 1.7.0.
- Update github.com/shirou/gopsutil from v3.22.12 to v3.23.2.
- Update github.com/stretchr/testify from 1.8.1 to 1.8.2.
- Update OpenTelemetry from 0.3.1 to 0.3.3.

## v1.25.3

### Bug fixes

- Fix reload config on config update/SIGHUP.
- Bond (`inputs.bond`): Reset slave stats for each interface.
- Cloudwatch (`inputs.cloudwatch`): Verify endpoint is not nil.
- LVM (`inputs.lvm`): Add options to specify path to binaries.
- XPath (`parsers.xpath`): Fix panic for JSON name expansion.
- JSON (`serializers.json`): Fix stateful transformations.

### Dependency updates

- Update cloud.google.com/go/pubsub from 1.27.1 to 1.28.0.
- Update github.com/containerd/containerd from 1.6.8 to 1.6.18.
- Update github.com/go-logfmt/logfmt from 0.5.1 to 0.6.0.
- Update github.com/gofrs/uuid from 4.3.1 to 5.0.0.
- Update github.com/gophercloud/gophercloud from 1.0.0 to 1.2.0.
- Update github.com/pion/dtls/v2 from 2.1.5 to 2.2.4.
- Update golang.org/x/net from 0.5.0 to 0.7.0.
- Update golang.org/x/sys from 0.4.0 to 0.5.0.
- Update google.golang.org/grpc from 1.52.3 to 1.53.0.
- Update k8s.io/apimachinery from 0.25.3 to 0.25.6.
- Update testcontainers from 0.14.0 to 0.18.0.

## v1.25.2

### Bug fixes

- Only read the config once.
- fix link to license for Google flatbuffers.
- Cisco Telemetry MDT (`inputs.cisco_telemetry_mdt`): Check subfield sizes to avoid panics.
- Cloudwatch (`inputs.cloudwatch`): Enable custom endpoint support.
- Conntrack (`inputs.conntrack`): Resolve segfault when setting collect field.
- GNMI (`inputs.gnmi`): Handle both new-style tag\_subscription and old-style tag\_only.
- MongoDB (`inputs.mongodb`):
    - Improve error logging.
    - SIGSEGV when restarting MongoDB node.
- MySQL (`inputs.mysql`): Avoid side-effects for TLS between plugin instances.
- Prometheus (`inputs.prometheus`): Deprecate and rename the timeout variable.
- Tail (`inputs.tail`): Fix typo in the README.
- UPSD (`inputs.upsd`): Add additional fields.
- x509 Cert (`inputs.x509_cert`): Fix Windows path handling.
- Prometheus Client (`outputs.prometheus_client`): Expire with ticker, not add/collect.
- Secret Stores: Check store id format and presence.

### Dependency updates

- Update cloud.google.com/go/bigquery from 1.44.0 to 1.45.0.
- Update github.com/99designs/keyring from 1.2.1 to 1.2.2.
- Update github.com/antchfx/xmlquery from 1.3.12 to 1.3.15.
- Update github.com/antchfx/xpath from 1.2.2 to 1.2.3.
- Update github.com/coreos/go-semver from 0.3.0 to 0.3.1.
- Update github.com/moby/ipvs from 1.0.2 to 1.1.0.
- Update github.com/multiplay/go-ts3 from 1.0.1 to 1.1.0.
- Update github.com/prometheus/client\_golang from 1.13.1 to 1.14.0.
- Update github.com/shirou/gopsutil from 3.22.9 to 3.22.12.
- Update go.mongodb.org/mongo-driver from 1.11.0 to 1.11.1.
- Update golang/x dependencies.
- Update google.golang.org/grpc from 1.51.0 to 1.52.0.
- Update google.golang.org/grpc from 1.52.0 to 1.52.3.

## v1.25.1

### Bug fixes

- Catch non-existing commands and error out.
- Correctly reload configuration files.
- Handle float time with fractions of seconds correctly.
- Only set default snmp after reading all configs.
- Allow any 2xx status code.
- Kafka: Add keep-alive period setting for input and output.
- Cisco Telemetry MDT (`inputs.cisco_telemetry_mdt`): Add operation-metric and class-policy prefix.
- Exec (`inputs.exec`): Restore pre-v1.21 behavior for CSV data\_format.
- GNMI (`inputs.gnmi`): Update configuration documentation.
- Logstash (`inputs.logstash`): Collect opensearch specific stats.
- MySQL (`inputs.mysql`): Revert slice declarations with non-zero initial length.
- OPC UA (`inputs.opcua`): Fix opcua and opcua-listener for servers using password-based auth.
- Prometheus (`inputs.prometheus`):
    - Correctly track deleted pods.
    - Set the timeout for slow running API endpoints correctly.
- SQL Server (`inputs.sqlserver`):
    - Add more precise version check.
    - Added own SPID filter.
    - SqlRequests include sleeping sessions with open transactions.
    - Suppress error on secondary replicas.
- UPSD (`inputs.upsd`):
    - Always convert to float.
    - Ensure firmware is always a string.
- Windows Event Log (`inputs.win_eventlog`): Handle remote events more robustly.
- x509 Cert (`inputs.x509_cert`): Fix off-by-one when adding intermediate certificates.
- Loki (`outputs.loki`): Return response body on error.
- JSON v2 parser (`parsers.json_v2`): In case of invalid json, log message to debug log.
- Secret Stores:
    - Cleanup duplicate printing.
    - Fix handling of “id” and print failing secret-store.
    - Fix handling of TOML strings.

### Dependency updates

- Update cloud.google.com/go/storage from 1.23.0 to 1.28.1.
- Update github.com/antchfx/jsonquery from 1.3.0 to 1.3.1.
- Update github.com/aws/aws-sdk-go-v2 from 1.17.1 to 1.17.3.
- Update github.com/aws/aws-sdk-go-v2/service/ec2 from 1.54.4 to 1.80.1.
- Update github.com/denisenkom/go-mssqldb from 0.12.0 to 0.12.3.
- Update github.com/eclipse/paho.mqtt.golang from 1.4.1 to 1.4.2.
- Update github.com/hashicorp/consul/api from 1.15.2 to 1.18.0.
- Update github.com/karrick/godirwalk from 1.16.1 to 1.17.0.
- Update github.com/kardianos/service from 1.2.1 to 1.2.2.
- Update github.com/nats-io/nats-server/v2 from 2.9.4 to 2.9.9.

## v1.25.0

### New Plugins

#### Inputs

- [Azure Monitor](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/azure_monitor) (`inputs.azure_monitor`)
- [Google Cloud Storage](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/google_cloud_storage) (`inputs.google_cloud_storage`)
- [Intel Dynamic Load Balancer (Intel DLB)](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/intel_dlb) (`inputs.intel_dlb`)
- [libvirt](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/libvirt) (`inputs.libvirt`)
- [Netflow](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/netflow) (`inputs.netflow`)
- [OPC UA Client Listener](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/opcua_listener) (`inputs.opcua_listener`)

#### Parsers

- [Binary](https://github.com/influxdata/telegraf/tree/master/plugins/parsers/binary) (`parsers.binary`)

### Features

- Add arm64 Windows builds to nightly and CI.
- Add method to inform of deprecated plugin option values.
- Add Secret-store implementation.
- Deprecate active usage of netsnmp translator.

#### Plugin updates

- Kafka (`common.kafka`): Add exponential backoff when connecting or reconnecting and allow plugin to start without making initial connection.
- AMQP Consumer (`inputs.amqp_consumer`): Determine content encoding automatically.
- APCUPSD (`inputs.apcupsd`): Add new fields:
    - status
    - cumulative\_time\_on\_battery\_ns
    - last\_transfer
    - number\_transfers
- CGroup (`inputs.cgroups`):
    - Do not abort on first error.
    - Print message once.
- Conntrack (`inputs.conntrack`): Parse conntrack stats.
- DiskIO (`inputs.diskio`): Allow selecting devices by ID.
- Ethtool (`inputs.ethtool`):
    - Gather statistics from namespaces.
    - Possibility to skip gathering metrics for downed interfaces
- HTTP Response (`inputs.http_response`):
    - Add setting for TLS renegotiation method.
    - Add User-Agent header.
- Kafka Consumer (`inputs.kafka_consumer`): Add Sarama debug logs.
- KNX (`inputs.knx_listener`): Add support for TCP as a transport protocol.
- Kubernetes (`inputs.kubernetes`): Allow fetching kublet metrics remotely.
- Modbus (`inputs.modbus`):
    - Add 8-bit integer types.
    - Add configuration option to pause after connect.
    - Add support for half-precision floats (float16).
    - Optimize grouped requests.
    - Optimize requests.
- OPC UA (`inputs.opcua`): Use regular reads instead of registered reads.
- PowerDNS Recursor (`inputs.powerdns_recursor`): Support for new PowerDNS recursor control protocol.
- Prometheus (`inputs.prometheus`): Add support for custom headers.
    - Allow explicit scrape configuration without annotations.
    - Use system wide proxy settings.
- S.M.A.R.T. (`inputs.smart`): Add additional SMART metrics that indicate/predict device failure.
- SNMP (`inputs.snmp`): Convert enum values.
- Socket Listener (`inputs.socket_listener`): Specify message separator for streams.
- SQL Server (`inputs.sqlserver` ):
    - Add `@@SERVICENAME` and `SERVERPROPERTY(IsClustered)` in measurement `sqlserver_server_properties`.
    - Add data and log used space metrics for Azure SQL DB.
    - Add metric `available_physical_memory_kb` in `sqlserver_server_properties`.
    - Introduce timeout for query execution.
- System (`inputs.system`): Collect unique user count logged in.
- Tail (`inputs.tail`):
    - Add option to preserve newlines for multiline data
    - Allow handling of quoted strings spanning multiple lines
- Tomcat (`inputs.tomcat`): Add source tag.
- Azure Data Explorer (`outputs.azure_data_explorer`): Add support for streaming ingestion for ADX output plugin.
- Event Hubs (`outputs.event_hubs`): Expose max message size batch option.
- Graylog (`outputs.graylog`): Implement optional connection retries.
- Timestream (`outputs.timestream`): Support ingesting multi-measures.
- Binary parser (`parsers.binary`) Handle hex-encoded inputs.
- CSV parser (`parsers.csv`):
    - Add option for overwrite tags
    - Support null delimiters
- Grok parser (`parsers.grok`): Add option to allow multiline messages.
- XPath parser (`parsers.xpath`):
    - Add option to skip (header) bytes.
    - Allow to specify byte-array fields to encode in HEX.
- JSON serializer (`serializers.json`) Support serializing JSON nested in string fields.

### Bug fixes

- Run processors in configuration order.
- Watch for changes in configuration files in config directories.
- Conntrack (`inputs.conntrack`): Skip gather tests if conntrack kernel module is not loaded.
- Filecount (`inputs.filecount`): Revert library version.
- Kubernetes Inventory (`inputs.kube_inventory`): Change default token path, use in-cluster config by default.
- Modbus (`inputs.modbus`):
    - Add workaround to read field in separate requests.
    - Fix Windows COM-port path.
    - Fix default value of transmission mode.
- MongoDB (`inputs.mongodb`): Fix connection leak triggered by configuration reload.
- OPC UA (`inputs.opcua`):
    - Add support for OPC UA datetime values.
    - Parse full range of status codes with uint32.
- Prometheus (`inputs.prometheus`): Respect selectors when scraping pods.
- SQL (`inputs.sql`): Cast `measurement_column` to string.
- VSphere (`inputs.vsphere`): Eliminate duplicate samples.
- ZFS (`inputs.zfs`): Unbreak dataset stat gathering in case listsnaps is enabled on a zfs pool.
- Azure Data Explorer (`outputs.azure_data_explorer`): Update test call to `NewSerializer`.
- Parser processor (`processors.parser`): Handle empty metric names correctly.

### Dependency updates

- Update `github.com/aliyun/alibaba-cloud-sdk-go` from 1.61.1836 to 1.62.77
- Update `github.com/gosnmp/gosnmp` from 1.34.0 to 1.35.0
- Update `OpenTelemetry` from 0.2.30 to 0.2.33

## v1.24.4

### Bug fixes

- Amazon CloudWatch (`inputs.cloudwatch`): Correctly handle multiple namespaces.
- Directory Monitor (`inputs.directory_monitor`): Close input file before removal.
- GMNI (`inputs.gnmi`):
    - Handle decimal\_val as per gnmi v0.8.0.
    - Do not provide empty prefix for subscription request.
    - Fix empty name for Sonic devices.
- Ping (`inputs.ping`): Avoid -x/-X on FreeBSD 13 and newer with ping6.
- Prometheus input (`inputs.prometheus`): Correctly default to port 9102.
- Redis Sentinel (`input.redis_sentinel`): Fix sentinel and replica stats gathering.
- Socket Listener (`inputs.socket_listener`): Ensure connections are closed.
- Datadog (`output.datadog`): Log response in case of non 2XX response from API
- Prometheus output (`outputs.prometheus`): Expire metrics correctly during adds.
- Yandex Cloud Monitoring (`outputs.yandex_cloud_monitoring`): Catch int64 values.

### Dependency updates

- Update `github.com/aliyun/alibaba-cloud-sdk-go` from 1.61.1818 to 1.61.1836
- Update `github.com/prometheus/client_golang` from 1.13.0 to 1.13.1
- Update `github.com/aws/aws-sdk-go-v2/service/timestreamwrite` from 1.13.12 to 1.14.5
- Update `github.com/aws/aws-sdk-go-v2/feature/ec2/imds` from 1.12.17 to 1.12.19
- Update `github.com/gofrs/uuid` from v4.3.0 to v4.3.1
- Update `github.com/aws/aws-sdk-go-v2/service/sts` from 1.16.19 to 1.17.2
- Update `github.com/urfave/cli/v2` from 2.16.3 to 2.23.5
- Update `github.com/Azure/azure-event-hubs-go/v3` from 3.3.18 to 3.3.20
- Update `github.com/showwin/speedtest-go` from 1.1.5 to 1.2.1
- Update `github.com/aws/aws-sdk-go-v2/credentials` from 1.12.21 to 1.13.2
- Update `github.com/yuin/goldmark` from 1.5.2 to 1.5.3
- Update `cloud.google.com/go/pubsub` from 1.25.1 to 1.26.0
- Update `go.mongodb.org/mongo-driver` from 1.10.2 to 1.11.0

## v1.24.3

### Bug fixes

- Restore warning on unused configuration options.
- Correct default value of `enable_tls`.
- Update systemd unit description.
- Fix panic due to tickers slice being off-by-one in size.
- Set default parser.
- Correctly setup processors
- Fix problem with metrics not exposed by plugins.
- Directory Monitor (`inputs.directory_monitor`): Allow cross filesystem directories.
- Kafka (`inputs.kafka`): Switch to Sarama’s new consumer group rebalance strategy setting.
- Modbus (`inputs.modbus`):
    - Add slave ID to failing connection.
    - Handle field-measurement definitions correctly on duplicate field check
    - Improve duplicate field checks
- OPC UA (`inputs.opcua`): Add metric tags to node.
- Syslog (`inputs.syslog`): Print error when no error or message given.
- Zookeeper (`inputs.zookeeper`): Add the ability to parse floats as floats.
- JSON v2 parser (`parsers.json_v2`): Remove BOM before parsing.
- Parser processor (`processors.parser`): Keep name of original metric if parser doesn’t return one.
- Splunk Metric serializer (`serializers.splunkmetric`): Provide option to remove event metric tag.

### Features

- Support sections in markdown.

### Dependency updates

- Update github.com/snowflakedb/gosnowflake from 1.6.2 to 1.6.13
- Update github.com/sensu/sensu-go/api/core/v2 from 2.14.0 to 2.15.0
- Update github.com/gofrs/uuid from 4.2.0& to 4.3.0
- Update github.com/hashicorp/consul/api from 1.14.0 to 1.15.2
- Update github.com/aws/aws-sdk-go-v2/credentials from 1.12.5 to 1.12.21
- Update github.com/aws/aws-sdk-go-v2/service/cloudwatch
- Update github.com/aws/aws-sdk-go-v2/config
- Update k8s.io/apimachinery from 0.25.1 to 0.25.2
- Update k8s.io/api from 0.25.0 to 0.25.2
- Update k8s.io/api from 0.25.2 to 0.25.3
- Update modernc.org/sqlite from 1.17.3 to 1.19.2
- Update github.com/signalfx/golib/v3 from 3.3.45 to 3.3.46
- Update github.com/yuin/goldmark from 1.4.13 to 1.5.2
- Update cloud.google.com/go/bigquery from 1.40.0 to 1.42.0
- Update github.com/aws/aws-sdk-go-v2/service/kinesis
- Update github.com/aliyun/alibaba-cloud-sdk-go
- Update github.com/Shopify/sarama from 1.36.0 to 1.37.2
- Update testcontainers-go from 0.13.0 to 0.14.0 and address breaking change
- Update modernc.org/libc from v1.20.3 to v1.21.2
- Update github.com/aws/aws-sdk-go-v2/service/dynamodb
- Update google.golang.org/api from 0.95.0 to 0.100.0
- Update github.com/gopcua/opcua from 0.3.3 to 0.3.7
- Update github.com/prometheus/client\_model from 0.2.0 to 0.3.0
- Update cloud.google.com/go/monitoring from 1.5.0 to 1.7.0
- Update github.com/nats-io/nats-server/v2 from 2.8.4 to 2.9.4

## v1.24.2

### Bug fixes

- Support old style of filtering sample configurations in CLI.
- Enable TLS in Kafka plugins without custom configuration.
- Avoid Ethtool internal name conflict with AWS.

### Input plugin updates

- InfluxDB Listener (`influxdb_listener`): Error on invalid precision.
- Internet speed (`internet_speed`): Rename `enable_file_download` to match upstream intent.
- MongoDB (`mongodb`): Start plugin correctly.
- MQTT Consumer (`mqtt_consumer`): Rework connection and message tracking.

### Parser updates

- XPath (`xpath`): Handle floating-point times correctly.
- Allow specifying the Influx parser type.

### Dependency updates

- Update dependencies for OpenBSD support.
- Update `k8s.io/apimachinery` from 0.25.0 to 0.25.1.
- Update `github.com/aerospike/aerospike-client-go/v5` from 5.9.0 to 5.10.0.
- Update github.com/nats-io/nats.go from 1.16.0 to 1.17.0.
- Replace `go-ping` with `pro-bing`.
- Update `go.mongodb.org/mongo-driver` from 1.10.1 to 1.10.2.
- Update `github.com/aws/smithy-go` from 1.13.2 to 1.13.3.
- Update `github.com/rabbitmq/amqp091-go` from 1.4.0 to 1.5.0.
- Update `github.com/docker/distribution` from v2.7.1 to v2.8.1.

## v1.24.1

### Bug fixes

- Clear error message when provided configuration is not a text file.
- Enable global confirmation for installing `mingw`.

### Input plugin updates

- Ceph (`ceph`): Modernize metrics.
- Modbus (`modbus`): Do not fail if a single server reports errors.
- NTPQ (`ntpq`): Handle pools with `-`.

### Parser updates

- CSV (`csv`): Remove direct check.
- XPath (`xpath`): Add array index when expanding names.
- Fix memory leak for plugins using `ParserFunc`.
- Unwrap parsers and remove some special handling.
- `processors.parser`: Add option to parse tags

### Dependency updates

- Update `cloud.google.com/go/pubsub` from 1.24.0 to 1.25.1.
- Update `github.com/urfave/cli/v2` from 2.14.1 to 2.16.3.
- Update `github.com/aws/aws-sdk-go-v2/service/ec2`.
- Update `github.com/wavefronthq/wavefront-sdk-go`.
- Update `cloud.google.com/go/bigquery` from 1.33.0 to 1.40.0.

## v1.24.0

### Breaking change

- Set default minimum TLS version to v1.2 for security reasons on both server and client connections. This is a change from the previous defaults (TLS v1.0) on the server configuration and might break clients relying on older TLS versions. Older versions can be manually reverted on a per-plugin basis using the `tls_min_version` option in the plugins required.

### Features

- Create custom builder to scan a Telegraf configuration file for the plugin files being defined and builds a new binary only including these plugins.
- Add license checking tool.
- Add metrics for member and replica-set average health of MongoDB.
- Allow collecting node-level metrics for Couchbase buckets.
- Make `config` subcommand.

### Bug fixes

- Add version number to MacOS packages.
- Backport sync `sample.conf` and `README.md` files.
- Fix to parsing errors in Datadog mode.
- Clean up after Redis merge.
- Refactor Telegraf version.
- Remove shell execution for `license-checker`.

### New plugins

#### Inputs

- [AWS CloudWatch Metric Streams](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/cloudwatch_metric_streams) (`cloudwatch_metric_streams`) - Contributed by [@mccabecillian](https://github.com/mccabecillian).
- [Linux CPU](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/linux_cpu)(`linux_cpu`) - Contributed by [@fabianishere](http://github.com/fabianishere).
- [NSDP](https://github.com/hdecarne-github/nsdp-telegraf-plugin) (`nsdp`) - Contributed by [@hdecarne](https://github.com/@hdecarne).
- [Supervisor](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/supervisor) (`supervisor`) - Contributed by [@niasar](http://github.com/niasar).
- [UPSD](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/upsd) (`upsd`) - Contributed by [@Malinskiy](http://github.com/Malinskiy).

#### Outputs

- [PostgreSQL](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/postgresql) (`postgresql`) - Contributed by [@phemmer](https://github.com/phemmer).
- [RedisTimeSeries](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/redistimeseries) (`redistimeseries`) - Contributed by [@gkorland](http://github.com/gkorland).
- [Stomp (Active MQ)](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/stomp) - Contributed by [@amus-sal](http://github.com/amus-sal).

#### Serializers

- [CSV](https://github.com/influxdata/telegraf/tree/master/plugins/serializers/csv) (`csv`) - Contributed by [@influxdata](http://github.com/influxdata).

### Input plugin updates

- Nats Consumer (`nats_consumer`): Add simple support for jetstream subjects.
- Cisco Telemetry MDT (`cisco_telemetry_mdt`): Add GRPC Keepalive/timeout configuration options.
- Directory Monitor (`directory_monitor`):
    - Support paths for `files_to_ignore` and `files_to_monitor`.
    - Traverse subdirectories.
- Kafka Consumer (`kafka_consumer`): Option to set default fetch message bytes.
- Linux CPU (`linux_cpu`): Add plugin to collect CPU metrics on Linux.
- Logstash (`logstash`): Record number of failures.
- Modbus (`modbus`): Error out on requests with no fields defined.
- MQTT Consumer (`mqtt_consumer`): Add incoming MQTT message size calculation.
- Nginx Plus API (`nginx_plus_api`) Gather `limit_reqs` metrics.
- NTPQ (`ntpq`):
    - Add option to specify command flags.
    - Add possibility to query remote servers.
    - Allow to specify `reach` output format.
- Openstack (`openstack`): Add `allow_reauth` configuration option.
- Smart (`smart`): Collect SSD endurance information where available in `smartctl`.
- SQL Server (`sqlserver`):
    - Add database name to IO stats for MI.
    - Improved filtering for active requests.
    - Fix filtering for `sqlAzureMIRequests` and s`qlAzureDBRequests`.
- StatsD (`statsd`): Add median timing calculation.
- Syslog (`syslog`): Log remote host as source tag.
- x509 Cert (`x509_cert`):
    - Add SMTP protocol.
    - Add proxy support.
    - Multiple sources with non-overlapping DNS entries.
- RabbitMQ (`rabbitmq`): Add support for `head_message_timestamp` metric.
- Redis (`redis`): Add Redis 6 ACL authorization support.
- Jolokia 2 (`jolokia2`): Add optional origin header.
- MongoDB (`mongodb`): Add an option to bypass connection errors on start.
- OPC UA (`opcua`): Assign node ID correctly.
- Prometheus (`prometheus`): Run outside Kubernetes cluster error.
- UPSD (`upsd`): Move to new `sample.conf` style.

### Output plugin updates

- Cloudwatch (`cloudwatch`): Add proxy support.
- MQTT (`mqtt`): Add support for MQTT protocol version 5.
- AMQP (`amqp`): Add proxy support.
- Graphite (`graphite`): Retry connecting to servers with failed send attempts.
- Groundwork (`groundwork`):
    - Improve metric parsing to extend output.
    - Add default appType as configuration option.
- Redis Time Series (`redistimeseries`): Add integration test
- SQL (`sql`): Add settings for Go `sql.DB` settings.
- ExecD (`execd`): Fix error when partially unserializable metrics are written.
- Wavefront (`wavefront`): Update Wavefront SDK and use non-deprecated APIs.

### Serializer updates

- JSON (`json`): Add new `json_transformation` option transform outputted JSON. This new option can be used to transform the JSON output using the JSONata language to accommodate for requirements on the receiver side. The setting can also filter and process JSON data points.
- Prometheus (`prometheus`):
    - Provide option to reduce payload size by removing HELP from payload
    - Sort labels in prometheusremotewrite serializer

### Parser updates

- Migrate parsers to new style.
- XPath (`xpath`): Add support for returning underlying data types.
- CSV (`csv`): Add `reset-mode` flag.

### Processor updates

- Starlark (`starlark`): Add benchmark for tag concatenation.

### Dependency updates

- Update `github.com/jackc/pgx/v4` from 4.16.1 to 4.17.0.
- Update `github.com/Azure/go-autorest/autorest` from 0.11.24 to 0.11.28.
- Update `github.com/aws/aws-sdk-go-v2/service/ec2` from 1.51.2 to 1.52.1
- Update `github.com/urfave/cli/v2` from 2.3.0 to 2.11.2.
- Update `github.com/aws/aws-sdk-go-v2/service/timestreamwrite` from 1.13.6 to 1.13.12.
- Update `github.com/aliyun/alibaba-cloud-sdk-go` from 1.61.1695 to 1.61.1727.
- Update `go.mongodb.org/mongo-driver` from 1.9.1 to 1.10.1.
- Update `github.com/wavefronthq/wavefront-sdk-go` from 0.10.1 to 0.10.2.
- Update `github.com/aws/aws-sdk-go-v2/service/sts` from 1.16.7 to 1.16.13.
- Update `github.com/aerospike/aerospike-client-go/v5` from 5.7.0 to 5.9.0.
- Update `github.com/hashicorp/consul/api` from 1.13.1 to 1.14.0.
- Update `github.com/tidwall/gjson` from 1.14.1 to 1.14.3.
- Update `github.com/rabbitmq/amqp091-go` from 1.3.4 to 1.4.0.
- Update `github.com/aws/aws-sdk-go-v2/service/dynamodb` from 1.15.10 to 1.16.1.
- Update `github.com/gophercloud/gophercloud` from 0.25.0 to 1.0.0.
- Update `k8s.io/client-go` from 0.24.3 to 0.25.0.
- Update `github.com/aws/aws-sdk-go-v2/feature/ec2/imds` from 1.12.11 to 1.12.13.
- Update `github.com/urfave/cli/v2` from 2.11.2 to 2.14.1.
- Update `gonum.org/v1/gonum` from 0.11.0 to 0.12.0.
- Update `github.com/Azure/azure-kusto-go` from 0.7.0 to 0.8.0.
- Update `google.golang.org/grpc` from 1.48.0 to 1.49.0.

## v1.23.4

### Bug fixes

- Update `github.com/lxc/lxd` to be able to run tests.
- Sync sql output and input build constraints to handle loong64 in go1.19.
- Updating credentials file to not use `endpoint_url` parameter.
- Cloudwatch (`inputs.cloudwatch`): Customize batch size when querying
- Kubernetes Inventor (`inputs.kube_inventory`): Send file location to enable token auto-refresh.
- Kubernetes (`inputs.kubernetes`): Refresh token from file at each read.
- MongoDB (`inputs.mongodb`): Update version check for newer versions.
- OPC UA (`inputs.opcua`): Return an error with mismatched types.
- SQL Server (`inputs.sqlserver`): Set lower deadlock priority.
- Stackdriver Google Cloud Monitoring (`inputs.stackdriver`): Handle when no buckets are available.
- Fix Linter issues

### Features

- Add coralogix dialect to opentelemetry

### Dependency updates

- Update `github.com/testcontainers/testcontainers-go` from 0.12.0 to 0.13.0.
- Update `github.com/apache/thrift` from 0.15.0 to 0.16.0.
- Update `github.com/aws/aws-sdk-go-v2/service/ec2` from 1.46.0 to 1.51.0.
- Update all `go.opentelemetry.io` dependencies.
- Update `github.com/go-ldap/ldap/v3` from 3.4.1 to 3.4.4.
- Update `github.com/karrick/godirwalk` from 1.16.1 to 1.17.0.
- Update `github.com/vmware/govmomi` from 0.28.0 to 0.29.0.
- Update `github.com/eclipse/paho.mqtt.golang` from 1.3.5 to 1.4.1.
- Update `github.com/shirou/gopsutil/v3` from 3.22.4 to 3.22.7.
- Update `github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs`.
- Update `github.com/Azure/go-autorest/autorest/adal`.
- Update `github.com/pion/dtls/v2` from 2.0.13 to 2.1.5.
- Update `github.com/Azure/azure-event-hubs-go/v3`.
- Update `github.com/aws/aws-sdk-go-v2/service/cloudwatch`.
- Update `github.com/aws/aws-sdk-go-v2/service/kinesis`.
- Update `github.com/aws/aws-sdk-go-v2/service/dynamodb`.
- Update `github.com/signalfx/golib/v3` from 3.3.43 to 3.3.45.
- Update `github.com/BurntSushi/toml` from 0.4.1 to 1.2.0.
- Update `cloud.google.com/go/pubsub` from 1.24.0 to 1.24.0.
- Update `k8s.io/apimachinery` from 0.24.2 to 0.24.3.
- Update `github.com/Shopify/sarama` from 1.34.1 to 1.35.0.
- Update `github.com/sirupsen/logrus` from 1.8.1 to 1.9.0.
- Update `github.com/emicklei/go-restful` from v2.9.5+incompatible to v3.8.0.
- Update `github.com/hashicorp/consul/api` from 1.12.0 to 1.13.1.
- Update `github.com/prometheus/client_golang` from 1.12.2 to 1.13.0.
- Update `google.golang.org/api` from 0.85.0 to 0.91.0.
- Update `github.com/antchfx/xmlquery` from 1.3.9 to 1.3.12.
- Update `github.com/aws/aws-sdk-go-v2/service/ec2`.
- Update `github.com/aws/aws-sdk-go-v2/feature/ec2/imds`.
- Update `github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs`.

## v1.23.4

- Update `github.com/lxc/lxd` to be able to run tests.
- Sync sql output and input build constraints to handle loong64 in go1.19.
- Update credentials file to not use `endpoint_url` parameter
- Fixes to linter issues
- Add Coralogix dialect to open telemetry.

### Input plugin updates

- Cloudwatch (`cloudwatch`): Customizable batch size when querying.
- Kube Inventory (`kube_inventory`): Send file location to enable token auto-refresh.
- Kubernetes (`kubernetes`): Refresh token from file at each read.
- MongoDB (`mongodb`): Update to most recent version.
- OPC UA (`opcua`): Return an error with mismatched types.
- SQL server (`sqlserver`): Set lower deadlock priority.
- Stackdriver (`stackdriver`) Handle when no buckets available.

### Dependency updates

- Bump github.com/testcontainers/testcontainers-go from 0.12.0 to 0.13.0.
- Bump github.com/apache/thrift from 0.15.0 to 0.16.0.
- Bump github.com/aws/aws-sdk-go-v2/service/ec2 from 1.46.0 to 1.51.0.
- Update all go.opentelemetry.io dependencies.
- Bump github.com/go-ldap/ldap/v3 from 3.4.1 to 3.4.4.
- Bump github.com/karrick/godirwalk from 1.16.1 to 1.17.0.
- Bump github.com/vmware/govmomi from 0.28.0 to 0.29.0.
- Bump github.com/eclipse/paho.mqtt.golang from 1.3.5 to 1.4.1.
- Bump github.com/shirou/gopsutil/v3 from 3.22.4 to 3.22.7.
- Bump github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs.
- Bump github.com/Azure/go-autorest/autorest/adal.
- Bump github.com/pion/dtls/v2 from 2.0.13 to 2.1.5.
- Bump github.com/Azure/azure-event-hubs-go/v3.
- Bump github.com/aws/aws-sdk-go-v2/service/cloudwatch.
- Bump github.com/aws/aws-sdk-go-v2/service/kinesis.
- Bump github.com/aws/aws-sdk-go-v2/service/dynamodb.
- Bump github.com/signalfx/golib/v3 from 3.3.43 to 3.3.45.
- Update github.com/BurntSushi/toml from 0.4.1 to 1.2.0.
- Update cloud.google.com/go/pubsub from 1.24.0 to 1.24.0.
- Update k8s.io/apimachinery from 0.24.2 to 0.24.3.
- Update github.com/Shopify/sarama from 1.34.1 to 1.35.0.
- Bump github.com/sirupsen/logrus from 1.8.1 to 1.9.0.
- Bump github.com/emicklei/go-restful from v2.9.5+incompatible to v3.8.0.
- Bump github.com/hashicorp/consul/api from 1.12.0 to 1.13.1.
- Bump github.com/prometheus/client\_golang from 1.12.2 to 1.13.0.
- Bump google.golang.org/api from 0.85.0 to 0.91.0.
- Bump github.com/antchfx/xmlquery from 1.3.9 to 1.3.12.
- Bump github.com/aws/aws-sdk-go-v2/service/ec2.
- Bump github.com/aws/aws-sdk-go-v2/feature/ec2/imds.
- Bump github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs.

## v1.23.3

### Bug fixes

- Openstack input plugin (`inputs.openstack`): Use v3 volume library.
- MQTT Consumer input plugin (`inputs.mqtt_consumer`): Topic parsing error when topic having prefix ‘/’.
- SNMP Trap input plugin (`inputs.snmp_trap`): Prevent map panic when using with `netsnmp` translator.
- SQL Server input plugin (`inputs.sqlserver`): Set lower deadlock priority on queries.
- `common.cookie`: Use reader over readcloser, regenerate `cookie-jar` at reauthorization.
- Prometheus parser (`parsers.prometheus`): Histogram infinity bucket is now always present.

### Dependency updates

- Bump `github.com/antchfx/jsonquery` from 1.1.5 to 1.2.0.

## v1.23.2

### Bug fixes

- Remove unexpected deprecation warnings for non-deprecated packages that occurred in 1.24.1.
- HTTP input plugin (`inputs.http`): Allow both 200 and 201 response codes when generating cookie authentication. Also update the cookie header docs to show a TOML map rather than a string.
- Microsoft SQL Server input plugin (`inputs.sqlserver`): Use `bigint` for `backupsize` in `sqlserver` queries.
- gNMI input plugin (`inputs.gnmi`): Refactor `tag_only` subscriptions for complex keys (such as `network-instances`) and to improve concurrrency. The subscription key is no longer hardcoded to the device name and the `name` tag. Adds ability to specify a subscription key on a per-tag basis.
- SNMP input plugin (`inputs.snmp`): Now sets gosnmp’s `UseUnconnectedUDPSocket` to true when using UDP. Adds support to accept SNMP responses from any address (not just the requested address). Useful when gathering responses from redundant/failover systems.

### Dependency updates

- Bump `github.com/docker/docker` from 20.10.14 to 20.10.17.

## v1.23.1

### Bug fixes

- Jolokia2 input plugin (`jolikia2`): Resolve panic on null response.
- RabbitMQ input plugin (`rabbitmq`) Don’t require listeners to be present in overview.
- Sync back `sample.confs` for Couchbuse input plugin (`couchbase`) and Groundwork output plugin (`groundwork`).
- Filter out views in MongoDB lookup.
- Fix race condition in configuration and prevent concurrent map writes to `c.UnusedFields`.
- Restore sample configurations broken during initial migration
- Sync back sample.confs for inputs.couchbase and outputs.groundwork.

### Dependency updates

- Bump `cloud.google.com/go/monitoring` from 1.2.0 to 1.5.0.
- Bump `github.com/aws/aws-sdk-go-v2/credentials` from 1.12.2 to 1.12.5.
- Bump `google.golang.org/grpc` from 1.46.2 to 1.47.0.
- Bump `k8s.io/client-go` from 0.23.3 to 0.24.1.
- Bump `github.com/go-logfmt/logfmt` from 0.5.0 to 0.5.1.
- Bump `github.com/aws/aws-sdk-go-v2/service/dynamodb` from 1.15.3 to 1.15.7.
- Bump `go.mongodb.org/mongo-driver` from 1.9.0 to 1.9.1.
- Bump `github.com/gophercloud/gophercloud` from 0.24.0 to 0.25.0.
- Bump `google.golang.org/api` from 0.74.0 to 0.84.0.
- Bump `github.com/fatih/color` from 1.10.0 to 1.13.0.
- Bump `github.com/aws/aws-sdk-go-v2/service/timestreamwrite` from 1.3.2 to 1.13.6.
- Bump `github.com/shopify/sarama` from 1.32.0 to 1.34.1.
- Bump `github.com/dynatrace-oss/dynatrace-metric-utils-go` from 0.3.0 to 0.5.0.
- Bump `github.com/nats-io/nats.go` from 1.15.0 to 1.16.0.
- Bump `cloud.google.com/go/pubsub` from 1.18.0 to 1.22.2.
- Bump `go.opentelemetry.io/collector/pdata` from 0.52.0 to 0.54.0.
- Bump `github.com/jackc/pgx/v4` from 4.15.0 to 4.16.1.
- Bump `cloud.google.com/go/bigquery` from 1.8.0 to 1.33.0.
- Bump `github.com/Azure/azure-kusto-go` from 0.6.0 to 0.7.0.
- Bump `cloud.google.com/go/pubsub` from 1.22.2 to 1.24.0.
- Bump `github.com/aws/aws-sdk-go-v2/service/kinesis` from 1.13.0 to 1.15.7.
- Bump `github.com/aws/aws-sdk-go-v2/service/ec2` from 1.1.0 to 1.46.0.
- Bump `github.com/golang-jwt/jwt/v4` from 4.4.1 to 4.4.2.
- Bump `github.com/vmware/govmomi` from 0.27.3 to 0.28.0.
- Bump `github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs` from 1.15.4 to 1.15.8.
- Bump `github.com/influxdata/influxdb-observability/otel2influx` from 0.2.21 to 0.2.22.
- Bump `k8s.io/api` from 0.24.1 to 0.24.2.
- Bump `github.com/prometheus/client_golang` from 1.12.1 to 1.12.2.

## v1.23.0

- Sample configuration (`sample.conf`) files for the different plugins are now embedded into the Golang code by the Go compiler. You can now download the sample configuration from Telegraf without having to paste in sample configurations from each plugin’s README.md.
- Add missing build constraints for sqlite.
- Always build README-embedder for host-architecture.
- Avoid calling `sadc` with invalid 0 interval.
- Check `net.Listen()` error in tests.
- Add DataDog count metrics.
- Deprecate unused database configuration option.
- Document interval setting for internet speed plugin.
- Add Elasticsearch output float handling test.
- Log instance name in skip warnings.
- Output erroneous namespace and fix error.
- Remove any content type from Prometheus accept header.
- Remove full access permissions.
- Search services file in `/etc/services` and fall back to `/usr/etc/services`.
- Migrate XPath parser to new style.
- Add field key option to set event partition key
- Add semantic commits checker.
- Allow other `fluentd` metrics.
- Add Artifactory Webhook Receiver.
- Create and push nightly Docker images to quay.io.
- Fix error if no nodes found for current configuration with XPath parser.

### New plugins

- [Fritzbox](https://github.com/gridscale/linux-psi-telegraf-plugin/blob/main/README.md)(`fritzbox`) - Contributed by [@hdecarne](https://github.com/@hdecarne).
- [Huebridge](https://github.com/hdecarne-github/huebridge-telegraf-plugin/blob/main/README.md)(`huebridge`) - Contributed by [@hdecarne](https://github.com/@hdecarne).
- [Slab](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/slab/README.md) (`slab`) - Contributed by @bobuhiro11.

### Input plugin updates

- Burrow (`burrow`): Move Dialer to variable and run `make fmt`.
- CPU (`cpu`): Add core and physical ID tags that contain information about physical CPU or cores in cases of hyper-threading.
- HTTP (`http`): Use readers over closers.
- Lustre (`lustre`): Support collecting per-client stats.
- Mock (`mock`) Add constant algorithm.
- Tail (`tail`): Add ANSI color filter.
- Redis (`redis`): Fix to `goroutine` leak triggered by auto-reload configuration mechanism.

### Output plugin updates

- HTTP (`http`): Enable authentication against a Google API protected by the OAuth 2.0 protocol.
- HTTP (`elasticsearch`): Add healthcheck timeout.
- SQL (`sql`): Add table existence cache.

### Dependency updates

- Update `github.com/wavefronthq/wavefront-sdk-go` from 0.9.10 to 0.9.11.
- Update `github.com/aws/aws-sdk-go-v2/config` from 1.15.3 to 1.15.7.
- Update `github.com/sensu/sensu-go/api/core/v2` from 2.13.0 to 2.14.0.
- Update `go.opentelemetry.io/otel/metric` from 0.28.0 to 0.30.0.
- Update `github.com/nats-io/nats-server/v2` from 2.7.4 to 2.8.4.
- Update `golangci-lint` from v1.45.2 to v1.46.2.
- Update `gopsutil` from v3.22.3 to v3.22.4 to allow for HOST\_PROC\_MOUNTINFO.
- Update `moby/ipvs` dependency from v1.0.1 to v1.0.2.
- Update `modernc.org/sqlite` from v1.10.8 to v1.17.3.
- Update `github.com/containerd/containerd` from v1.5.11 to v1.5.13.
- Update `github.com/tidwall/gjson` from 1.10.2 to 1.14.1.

## v1.22.4

- Wait for network up in `systemd` packaging.

### Input plugin updates

- Couchbase (`couchbase`): Do not assume metrics will all be of the same length.
- StatsD (`statsd`): Fix error when closing network connection.
- Add mount option filtering to disk plugin.

### Output plugin updates

- Azure Monitor (`azure_monitor`): Reinitialize `http` client on context deadline error.
- Wavefront (`wavefront`): Do not add `telegraf.host` tag if no `host` tag is provided.

### Dependency updates

- Update `github.com/showwin/speedtest-go` from 1.1.4 to 1.1.5.
- Update OpenTelemetry plugins to v0.51.0.

## v1.22.3

- Update Go to 1.18.1.

### Input plugin updates

- InfluxDB Listener (`influxdb_listener`): Remove duplicate writes with upstream parser.
- GNMI (`gnmi`): Use external xpath parser.
- System (`system`): Reduce log level back to original level.

## v1.22.2

- Allow Makefile to work on Windows.
- Allow zero outputs when using `test-wait` parameter.

### Input plugin updates

- Aerospike (`aerospike`): Fix statistics query bug.
- Aliyun CMS (`aliyuncms`): Ensure metrics accept array.
- Cisco Telemetry MDT (`cisco_telemetry_mdt`):
    - Align the default value for message size.
    - Remove overly verbose info message.
- GNMI (`gnmi`):
    - Add mutex to lookup map.
    - Use sprint to cast to strings.
- Consul agent (`consul_agent`): Use correct auth token.
- MySQL (`mysql`): Add `mariadb_dialect` to address the MariaDB differences in `INNODB_METRICS`.
- SMART (`smart`): Correctly parse various numeric forms
- Prometheus (`prometheus`): Moved from watcher to informer.

### Output plugin updates

- InfluxDB v2 (`influxdb_v2`): Improve error message.

### Dependency updates

- Update `github.com/Azure/azure-kusto-go` from 0.5.0 to 0.60.
- Update `opentelemetry` from v0.2.10 to v0.2.17.
- Update `go.opentelemetry.io/collector/pdata` from v0.48.0 to v0.49.0.
- Update `github.com/aws/aws-sdk-go-v2/config` from 1.13.1 to 1.15.3
- Update `github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs`.
- Update `github.com/aws/aws-sdk-go-v2/credentials` from 1.8.0 to 1.11.2.
- Update `github.com/containerd/containerd` from v1.5.9 to v1.5.11.
- Update `github.com/miekg/dns` from 1.1.46 to 1.1.48.
- Update `github.com/gopcua/opcua` from v0.3.1 to v0.3.3
- Update `github.com/aws/aws-sdk-go-v2/service/dynamodb`.
- Update `github.com/xdg/scram` from 1.0.3 to 1.0.5.
- Update `go.mongodb.org/mongo-driver` from 1.8.3 to 1.9.0.
- Update `starlark 7a1108eaa012->d1966c6b9fcd`.

## v1.22.1

- Update `gonum.org/v1/gonum` from 0.9.3 to 0.11.0.
- Update `github.com/golang-jwt/jwt/v4` from 4.2.0 to 4.4.1.
- Update `gopsutil` and associated dependencies for improved OpenBSD support.
- Fix default value for logfile rotation interval.

### Input plugin updates

- Intel PMU (`intel_pmu`): Fix slow running intel-pmu test.
- Cloud PubSub (`cloud_pubsub`): Skip longer integration tests on `-short` mode.
- Cloud PubSub Push (`cloud_pubsub_push`): Reduce timeouts and sleeps.
- SQL Server (`sqlserver`): Fix inconsistencies in `sql*Requests` queries.
- ZFS (`zfs`): Fix redundant pool tag.
- vSphere (`vsphere`): Update debug message information.

### Output plugin updates

- Azure Monitor (`azure_monitor`): Include body in error message.
- HTTP (`http`): Switch HTTP 100 test case values.

### Processor plugin updates

- TopK (`topk`) Clarify the `k` and `fields` parameters.

### New external plugins

- [PSI External Plugin](https://github.com/gridscale/linux-psi-telegraf-plugin/blob/main/README.md)(`external.psi`) - Contributed by [@ajfriesen](https://github.com/ajfriesen).

## v1.22.0

### Features

- Add `autorestart` and `restartdelay` flags to Windows service
- Add builds for `riscv64`.
- Add file version and icon to `win.exe`.
- Add `systemd` notify support.
- Check TLS configuration early to catch missing certificates.
- Implement collection offset.
- `common.auth`: HTTP basic auth.
- `common.cookie`: Support headers with cookie auth.
- `common.proxy`: Add `socks5` proxy support.
- Improve error logging on plugin initialization.

### Bug fixes

- Print loaded plugins and deprecations for once and test.
- Remove signed MacOS artifacts.
- Run `go mod tidy`.
- Fix `prometheusremotewrite` wrong timestamp unit.
- Fix sudden close caused by OPC UA input.
- Update `containerd` to 1.5.9.
- Update `go-sensu` to v2.12.0.
- Update `gosmi` from v0.4.3 to v0.4.4.
- Update parsing logic of `config.duration`.
- Update precision parameter default value.
- Use `sha256` for rpm digest.
- Warning output when running with `--test`.
- Graceful shutdown of Telegraf with Windows service.
- Add push-only updated values flag to histogram aggregator.
- `common.cookie`: Address flaky tests in cookie\_test.go and graylog\_test.go.
- `common.shim`: Linter fixes.
- Do not save cache on i386 builds.
- Add error msg for missing environment variables in configuration file.
- Fix panic in parsers due to missing log for all plugins using `setparserfunc`.
- Grab table columns more accurately.
- Improve parser tests by using `go-cmp/cmp`.
- Linter fixes for `config/config.go`.
- Log error when loading mibs.
- Fix Mac signing issue with arm64.

### New plugins

#### Inputs

- [Hashicorp Consul Agent Input Plugin](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/consul_metrics)(`consul_agent`) - Contributed by [@efbar](https://github.com/efbar).
- [Hashicorp Nomad Input Plugin](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/nomad)(`nomad`) - Contributed by [@efbar](https://github.com/efbar).
- [Hashicorp Vault Input Plugin](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/vault)(`vault`) - Contributed by [@efbar](https://github.com/efbar).
- [Hugepages Input Plugin](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/hugepages)(`hugepages`) - Contributed by [@zak-pawel](https://github.com/zak-pawel).
- [Mock Input Plugin](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/mock)(`mock`) - Contributed by [InfluxData](https://github.com/influxdata).
- [Redis Sentinel Input Plugin](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/redis_sentinel)(`redis_sentinel`) - Contributed by [@spideyfusion](https://github.com/spideyfusion).
- [Socketstat Input Plugin](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/socketstat)(`socketstat`) - Contributed by [@sajoupa](https://github.com/sajoupa).
- [XtremIO Input Plugin](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/xtremio)(`xtremio`) - Contributed by [@cthiel42](https://github.com/cthiel42).

#### Processors

- [Noise Processor](https://github.com/influxdata/telegraf/tree/master/plugins/processors/noise) (`noise`) - Contributed by [@wizarq](https://github.com/wizarq).

### Input plugin updates

- Aerospike (`aerospike`): Update `github.com/aerospike/aerospike-client-go` from 1.27.0 to 5.7.0.
- Bond (`bond`): Add additional stats.
- Directory Monitor (`directory_monitor`):
    - Update `djherbis/times` and fix `dependabot`.
    - Plugin restructuring.
- Disk (`disk`): Fix missing storage in container.
- Docker (`docker`):
    - Keep field type of `tasks_desired` the same.
    - Update memory usage calculation.
    - Update client API version.
- ECS (`ecs`): Use current time as timestamp.
- Execd `execd`: Add newline for Prometheus parsing.
- File (`file`): Stateful parser handling.
- GNMI (`gnmi`): Add dynamic tagging.
- Graylog (`graylog`):
    - Add `toml` tags.
    - Add `timeout-setting`.
    - Update documentation to use current URLs.
- HTTP (`http`): Ensure http body is empty.
- HTTP Listener v2 (`http_listener_v2`): Revert deprecation.
- Internet speed (`internet_speed`): Add caching.
- IPset (`ipset`): Fix crash when command not found.
- JSON V2 (`json_v2`):
    - Allow multiple optional objects.
    - Use raw values for timestamps.
- Kibana (`kibana`): Add `heap_size_limit` field.
- Logparser (`logparser`):
    - Add comment.
    - Fix panic due to missing log.
- MDStat (`mdstat`): Fix when sync is less than 10%.
- Memcached (`memcached`): Gather additional stats.
- Modbus `modbus`:
    - Make Telegraf compile on Windows with golang 1.16.2.
    - Re-enable openbsd support.
    - Update documentation.
    - Add `per-request` tags.
    - Support multiple slaves (gateway feature).
- MQTT Consumer (`mqtt_consumer`): Topic extracting no longer requires all three fields.
- NFS Client (`nfsclient`): Add new field.
- NTPQ (`ntpq`): Correctly read long poll output.
- OPC UA (`opcua`):
    - Accept non-standard OK status by implementing a configurable workaround.
    - Add more data to error log.
    - Remove duplicate addition of fields.
- OpenLDAP (`openldap`): Update go-ldap to v3.4.1.
- OpenStack (`openstack`): Fix typo.
- OpenWeatherMap (`openweathermap`): Add `feels_like` field.
- PHPfpm (`phpfpm`): Ensure CI tests runs against i386.
- PostgreSQL (`postgresql`): Add option to disable prepared statements.
- SMART (`smart`): Add concurrency configuration option, support and lint fixes.
- SNMP `(snmp`):
    - Respect number of retries configured.
    - Use the correct path when evaluating symlink.
    - Add option to select translator.
    - Check index before assignment.
    - Do not require networking during tests.
    - Ensure folders do not get loaded more than once.
    - Fix panic due to no module.
    - Fix errors if mibs folder doesn’t exist.
    - Optimize locking for mibs loading.
- SNMP Trap (`snmp_trap`):
    - Collapsed fields by calling more in-depth function.
    - Deprecate unused timeout configuration option.
- SQL (`sql`): Add Clickhouse driver.
- StatsD (`statsd`): Sanitize names.
- Syslog (`syslog`): Add rfc3164 to rfc5424 translation to docs.
- System (`system`): Remove verbose logging.
- Windows Performance Counter (`win_perf_counter`):
    - Allow errors to be ignored.
    - Implemented support for reading raw values, added tests, and update documentation.
- X.509 Certificate (`x509_cert`):
    - Mark `testgatherudpcert` as an integration test.
    - Add `exclude_root_certs` option.
- ZFS (`zfs`): Pool detection and metrics gathering for ZFS 2.1.x.

### Output plugin updates

- AMQP (`amqp`): Check for nil client before closing.
- ElasticSearch (`elasticsearch`):
    - Implement `nan` and `inf` handling.
    - Add bearer token support.
- Graylog (`graylog`): Fix to field prefixes.
- Groundwork (`groundwork`):
    - Set `nextchecktime` to `lastchecktime`.
    - Update SDK and improve logging.
    - Process group tag.
- InfluxDB V2 (`influxdb_v2`): Include bucket name in error messages.
- SQL (`sql`): Fix unsigned settings.
- Stackdriver (`stackdriver`): Cumulative interval start times.
- Syslog (`syslog`): Correctly set trailer.
- Timestream (`timestream`): Fix batching logic with write record and introduce concurrent requests.
- Datadog (`datadog`): Add compression.
- HTTP (`http`):
    - Add optional list of non-retryable status codes.
    - Support AWS managed service for Prometheus.
- Websocket `websocket`: `socks5` proxy support.
- Wavefront (`wavefront`):
    - Flush sender on error to clean up broken connections.
    - Run `gofmt`.
    - Fix panic if no mibs folder is found.

### Parser plugin updates

- CSV (`csv`):
    - Empty import tzdata for Windows binaries.
    - Fix typo.
- Ifname (`ifname`):
    - Eliminate mib dependency.
    - Parallelism fix.
- JSON V2 (`parsers.json_v2`):
    - Allow optional paths and handle wrong paths correctly.
    - Check if gpath exists and support optional in fields/tags.
    - Fixes to timestamp setting.
- Nagios (`nagios`): Use real error for logging.
- XPath (`xpath`):
    - Handle duplicate registration of protocol-buffer files gracefully.
    - Fix typo.

### Dependency updates

- Update `github.com/azure/azure-kusto-go` from 0.5.0 to 0.5.2.
- Update `github.com/nats-io/nats-server/v2` from 2.7.3 to 2.7.4.
- Update `github.com/shopify/sarama` from 1.29.1 to 1.32.0.
- Update `github.com/shirou/gopsutil`/v3 from 3.21.12 to 3.22.2.
- Update `github.com/aws/aws-sdk-go-v2/feature/ec2/imds`.
- Update `github.com/miekg/dns` from 1.1.43 to 1.1.46.
- Update `github.com/aws/aws-sdk-go-v2/service/dynamodb`.
- Update `github.com/nats-io/nats-server/v2` from 2.7.2 to 2.7.3.
- Update `github.com/aws/aws-sdk-go-v2/config` from 1.8.3 to 1.13.1.
- Update `github.com/testcontainers/testcontainers-go`.
- Update `github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs`.
- Update `github.com/aws/aws-sdk-go-v2/feature/ec2/imds`.
- Update `github.com/wavefronthq/wavefront-sdk-go` from 0.9.9 to 0.9.10.
- Update `github.com/clickhouse/clickhouse-go` from 1.5.1 to 1.5.4.
- Update `k8s.io/api` from 0.23.3 to 0.23.4.
- Update `cloud.google.com/go/pubsub` from 1.17.1 to 1.18.0.
- Update `github.com/newrelic/newrelic-telemetry-sdk-go`.
- Update `github.com/aws/aws-sdk-go-v2/service/dynamodb` from 1.5.0 to 1.13.0.
- Update `github.com/sensu/sensu-go/api/core/v2` from 2.12.0 to 2.13.0.
- Update `github.com/gophercloud/gophercloud` from 0.16.0 to 0.24.0.
- Update `github.com/jackc/pgx/v4` from 4.14.1 to 4.15.0.
- Update `github.com/aws/aws-sdk-go-v2/service/sts` from 1.7.2 to 1.14.0.
- Update all `go.opentelemetry.io` dependencies.
- Update `github.com/signalfx/golib/v3` from 3.3.38 to 3.3.43.
- Update `github.com/aliyun/alibaba-cloud-sdk-go`.
- Update `github.com/denisenkom/go-mssqldb` from 0.10.0 to 0.12.0.
- Update `github.com/gopcua/opcua` from 0.2.3 to 0.3.1.
- Update `github.com/nats-io/nats-server/v2` from 2.6.5 to 2.7.2.
- Update `k8s.io/client-go` from 0.22.2 to 0.23.3.
- Update `github.com/aws/aws-sdk-go-v2/service/kinesis` from 1.6.0 to 1.13.0.
- Update `github.com/benbjohnson/clock` from 1.1.0 to 1.3.0.
- Update `github.com/vmware/govmomi` from 0.27.2 to 0.27.3.
- Update `github.com/prometheus/client_golang` from 1.11.0 to 1.12.1.
- Update `go.mongodb.org/mongo-driver` from 1.7.3 to 1.8.3.
- Update `github.com/google/go-cmp` from 0.5.6 to 0.5.7.
- Update `go.opentelemetry.io/collector/model` from 0.39.0 to 0.43.2.
- Update `github.com/multiplay/go-ts3` from 1.0.0 to 1.0.1.
- Update `cloud.google.com/go/monitoring` from 0.2.0 to 1.2.0.
- Update `github.com/vmware/govmomi` from 0.26.0 to 0.27.2.
- Update `google.golang.org/api` from 0.54.0 to 0.65.0.
- Update `github.com/antchfx/xmlquery` from 1.3.6 to 1.3.9.
- Update `github.com/nsqio/go-nsq` from 1.0.8 to 1.1.0.
- Update `github.com/prometheus/common` from 0.31.1 to 0.32.1.
- Update `cloud.google.com/go/pubsub` from 1.17.0 to 1.17.1.
- Update `github.com/influxdata/influxdb-observability/influx2otel` from 0.2.8 to 0.2.10.
- Update `github.com/shirou/gopsutil/v3` from 3.21.10 to 3.21.12.
- Update `github.com/jackc/pgx/v4` from 4.6.0 to 4.14.1.
- Update `github.com/azure/azure-event-hubs-go/v3` from 3.3.13 to 3.3.17.
- Update `github.com/gosnmp/gosnmp` from 1.33.0 to 1.34.0.
- Update `github.com/hashicorp/consul/api` from 1.9.1 to 1.12.0.
- Update `github.com/antchfx/xpath` from 1.1.11 to 1.2.0.
- Update `github.com/antchfx/jsonquery` from 1.1.4 to 1.1.5.
- Update `github.com/prometheus/procfs` from 0.6.0 to 0.7.3.
- Update `github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs` from 1.5.2 to 1.12.0.
- Update `github.com/kardianos/service` from 1.0.0 to 1.2.1.
- Update `github.com/couchbase/go-couchbase` from 0.1.0 to 0.1.1.
- Update `github.com/pion/dtls/v2` from 2.0.9 to 2.0.13.
- Update `github.com/eclipse/paho.mqtt.golang` from 1.3.0 to 1.3.5.

## v1.21.4

- Update to Go 1.17.7 to address [three security issues](https://groups.google.com/g/golang-announce/c/SUsQn0aSgPQ/m/gx45t8JEAgAJ?pli=1) in the library.
- Update all `go.opentelemetry.io` from 0.24.0 to 0.27.0.
- Update `github.com/signalfx/golib/v3` from 3.3.38 to 3.3.43.
- Update `github.com/aliyun/alibaba-cloud-sdk-go` from 1.61.1004 to 1.61.1483.
- Update `github.com/denisenkom/go-mssqldb` from 0.10.0 to 0.12.0.
- Update `github.com/gopcua/opcua` from 0.2.3 to 0.3.1.
- Update `github.com/nats-io/nats-server/v2` from 2.6.5 to 2.7.2.
- Update `k8s.io/client-go` from 0.22.2 to 0.23.3.
- Update `github.com/aws/aws-sdk-go-v2/service/kinesis` from 1.6.0 to 1.13.0.
- Update `github.com/benbjohnson/clock` from 1.1.0 to 1.3.0.
- Update `github.com/Azure/azure-kusto-go` from 0.5.0 to 0.5.2.
- Update `github.com/vmware/govmomi` from 0.27.2 to 0.27.3.
- Update `github.com/prometheus/client_golang` from 1.11.0 to 1.12.1.
- Update `go.mongodb.org/mongo-driver` from 1.7.3 to 1.8.3.
- Update `github.com/google/go-cmp` from 0.5.6 to 0.5.7.
- Update `go.opentelemetry.io/collector/model` from 0.39.0 to 0.43.2.
- Update `github.com/multiplay/go-ts3` from 1.0.0 to 1.0.1.
- Update `cloud.google.com/go/monitoring` from 0.2.0 to 1.2.0.
- Update `github.com/vmware/govmomi` from 0.26.0 to 0.27.2.

### Input plugin updates

- Docker (`docker`): Update memory usage calculation.
- ECS (`ecs`): Use current time as timestamp.
- SNMP (`snmp`): Ensure folders do not get loaded more than once.
- Windows Performance Counters (`win_perf_counters`): Add deprecated warning and version.

### Output plugin updates

- AMQP (`amqp`): Check for nil client before closing.
- Azure Data Explorer (`azure_data_explorer`): Lower RAM usage.
- ElasticSearch (`elasticsearch`): Add scheme to fix error in sniffing option.

### Parser plugin updates

- JSON v2 (`json_v2`):
    - Fix timestamp change during execution.
    - Fix incorrect handling of `timestamp_path`.
    - Allow optional paths and handle wrong paths correctly.

### Serializer updates

- Prometheus serializer (`prometheusremotewrite`): Use correct timestamp unit.

### New External Plugins

- [apt](https://github.com/x70b1/telegraf-apt/blob/master/README.md)(`telegraf-apt`) - Contributed by [@x70b1](https://github.com/x70b1).
- [knot](https://github.com/x70b1/telegraf-knot/blob/master/README.md)(`telegraf-knot`) - Contributed by [@x70b1](https://github.com/x70b1).

## v1.21.3

- Update `grpc` module to v1.44.0.
- Update `google.golang.org/api` module from 0.54.0 to 0.65.0.
- Update `antchfx/xmlquery` module from 1.3.6 to 1.3.9.
- Update `nsqio/go-nsq` module from 1.0.8 to 1.1.0.
- Update `prometheus/common` module from 0.31.1 to 0.32.1.
- Update `cloud.google.com/go/pubsub` module from 1.17.0 to 1.17.1.
- Update `influxdata/influxdb-observability/influx2otel` module from 0.2.8 to 0.2.10.
- Update `shirou/gopsutil/v3` module from 3.21.10 to 3.21.12.
- Update `jackc/pgx/v4` module from 4.6.0 to 4.14.1.
- Update `Azure/azure-event-hubs-go/v3` module from 3.3.13 to 3.3.17.
- Update `gosnmp/gosnmp` module from 1.33.0 to 1.34.0.
- Update `hashicorp/consul/api` module from 1.9.1 to 1.12.0.
- Update `antchfx/xpath` module from 1.1.11 to 1.2.0.
- Update `antchfx/jsonquery` module from 1.1.4 to 1.1.5.
- Update `prometheus/procfs` module from 0.6.0 to 0.7.3.
- Update `aws/aws-sdk-go-v2/service/cloudwatchlogs` module from 1.5.2 to 1.12.0.
- Update `kardianos/service` module from 1.0.0 to 1.2.1.
- Update `couchbase/go-couchbase` module from 0.1.0 to 0.1.1.
- Update `pion/dtls/v2` module from 2.0.9 to 2.0.13.
- Update `containerd/containerd` module to 1.5.9.

### Input plugin updates

- Execd (`execd`): Resolve a Prometheus text format parsing error.
- IPset (`ipset`): Prevent panic from occurring after startup.
- OPC-UA (`opc_ua`): Fix issue where fields were being duplicated.
- HTTP (`http`): Prevent server side error message.
- SNMP (`snmp`): Fix error when a MIBs folder doesn’t exist.
- SNMP Trap (`snmp_trap`): Fix translation of partially resolved OIDs.

### Output plugin updates

- AMQP (`amqp`): Update to avoid connection leaks.
- Timestream (`timestream`):
    - Fix an issue with batching logic of write records.
    - Introduce concurrent requests.
- Stackdriver (`stackdriver`): Send correct interval start times for all counter metrics.
- Syslog (`syslog`): Correctly set the ASCII trailer per [RFC 6587](https://datatracker.ietf.org/doc/html/rfc6587).

### Parser plugin updates

- Nagios (`nagios`): Log correct errors when executing commands to aid in debugging.
- JSON v2 (`json_v2`): Fix timestamp precision when using `unix_ns` timestamp format.
- Wavefront (`wavefront`): Add missing setting `wavefront_disable_prefix_conversion`.

## v1.21.2

- Add arm64 MacOS builds for M1 devices.
- Add RISC-V64 Linux builds.
- Complete numerous changes to CircleCI config to ensure more timely completion and more clear execution flow.
- Update `github.com/djherbis/times` module from v1.2.0 to v1.5.0.
- Update `github.com/go-ldap/ldap/v3` module from v3.1.0 to v3.4.1.
- Update `github.com/gwos/tcg/sdk` module to v0.0.0-20211223101342-35fbd1ae683c.

### Input plugin updates

- Disk (`disk`): Fix issue of missing disks when running Telegraf in a container.
- DPDK (`dpdk`): Add a note to documentation about socket availability.
- Logparser (`logparser`): Resolve panic in the logparser plugins due to a missing `Log`.
- SNMP (`snmp`):
    - Resolve panic due to a missing `gosmi` module.
    - Resolve panic to check the index before assignment where a floating `::` exists.
    - Resolve a panic when no MIBs folder was found.
    - Ensure the module load order to avoid an SNMP marshal error.
    - Now more accurately grabs MIB table columns.
    - Networking no longer required during tests.
- SNMP Trap (`snmp_trap`): Documented deprecation of the `timeout` setting.

### Parser plugin updates

- CSV (`csv`): Use an empty import of `tzdata` to correctly set the time zone.

## v1.21.1

### Bug fixes

- Fix panic in parsers due to missing log.
- Update `go-sensu module` to v2.12.0
- Fix typo in OpenStack input plugin.

### Features

- Add SMART input plugin concurrency configuration option, `nvme-cli v1.14+` support, and lint fixes.

## v1.21

The signing for RPM digest has changed to use sha256 to improve security. Due to this change, RPM builds might not be compatible with RHEL6 and older releases. (Telegraf only supports releases in RHEL production.)

- Restart Telegraf service if it’s already running and upgraded via RPM.
- Print loaded plugins and deprecations for once and test flags.
- Update `eclipse/paho.mqtt.golang` module from 1.3.0 to 1.3.5.
- Shutdown Telegraf gracefully on Windows Service.
- Skip `knxlistener` when writing the sample configuration file.
- Update `nats-sever` to support `openbsd`.
- Revert unintended corruption of the Makefile.
- Filter client certificates by DNS names.
- Update `etc/telegraf.conf` and `etc/telegraf_windows.conf`.
- Add full metadata to configuration for `common.kafka`.
- Update `google.golang.org/grpc` module from 1.39.1 to 1.40.0.

### Input plugin updates

- Cloudwatch (`cloudwatch`): Fix metrics collection.
- CPU (`cpu`): Update `shirou/gopsutil` from v2 to v3.
- Directory Monitor (`directory_monitor`):
    - Fix to when when data format is CSV and `csv_skip_rows>0` and `csv_header_row_count>=1`.
    - Adds the ability to create and name a tag containing the filename.
- ElasticSearch (`elasticsearch_query`): Add debug query output.
- HTTP Listener v2: (`http_listener_v2`): Fix panic on close to check that Telegraf is closing.
- Kubernetes Inventory (`kube_inventory`): Set TLS server name configuration properly.
- Modbus (`modbus`): Update connection settings (serial).
- MQTT Consumer (`mqtt_consumer`):
    - Extracting no longer requires all three fields
    - Enable extracting tag values from MQTT topics
- OPC UA (`opc_ua`):
    - Fix sudden closing of Telegraf.
    - Allow user to select the source for the metric timestamp.
- Prometheus (`prometheus`):
    - Check error before defer.
    - Add `ignore_timestamp` option.
- Puppet (`puppetagent`): Add measurements from puppet 5.
- SNMP (`snmp`):
    - Update snmp plugin to respect number of retries configured.
    - Optimize locking for SNMP MIBs loading.
    - Update to use gosmi.
    - Remove `snmptranslate` from READme and fix default path.
    - Merge tables with different indexes.
- StatsD (`statsd`): Fix parse error.
- Sysstat (`sysstat`): Use unique temporary file.
- Windows Performance Counters (`win_perf_counters`): Add setting to ignore localization.
- Windows Services (`win_services`): Add exclude filter.
- ZFS (`zfs`): Pool detection and metrics gathering for ZFS >= 2.1.x

### Output plugin updates

- Register `bigquery` to all output plugins.
- Azure Data Explorer (`azure_data_explorer`):
    - Add option to skip table creation.
    - Add `json_timestamp_layout` option.
- ElasticSearch (`elasticsearch`): Implement NaN and inf handling.
- Graylog (`graylog`):
    - Ensure graylog spec fields not prefixed with `_`.
    - Failing test due to port already in use.
    - Mute UDP/TCP tests by marking them as integration.
    - TLS support and message format.
    - Add TCP support.
- HTTP (`http`): Add `use_batch_format`.
- InfluxDB V2 (`influxdb_v2`): Add retry to 413 errors with InfluxDB output.
- Wavefront (`wavefront`): Flush sender on error to clean up broken connections.

### Parser plugin updates

- XPath (`xpath`): Handle duplicate registration of protocol-buffer files gracefully
- JSON v2 (`json_v2`):
    - Parser timestamp setting order.
    - Remove dead code.
    - Support defining field/tag tables within an object table.

### Processor plugin updates

- IfName (`ifname`):
    - Eliminate MIB dependency.
    - Parallelism fix.
    - Add more details to log messages.
- Starlark (`starlark`): Example for processing `sparkplug_b` messages.
- RegEx (`regex`): Extend to allow renaming of measurements, tags, and fields.

### Aggregator plugin updates

- Implement deprecation infrastructure
- Add support of aggregator as Starlark script

### New plugins

#### Inputs

- [Intel PMU Input Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/intel_pmu/README.md)(`intel_pmu`) - Contributed by [@bkoltowski](https://github.com/bkotlowski).
- [Logical Volume Manager Input Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/lvm/README.md)(`lvm`) - Contributed by @InfluxData.
- [OpenStack Input Plugin](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/openstack)(`openstack`) - Contributed by \[@singamSrikar\].(https://github.com/singamSrikar).

### Outputs

- [Azure Event Hubs Output Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/outputs/event_hubs/README.md)(`event_hubs`) - Contributed by [@tomconte](https://github.com/tomconte).
- [GroundWork Output Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/outputs/groundwork/README.md)(`groundwork`) - Contributed by \[@VladislavSenkevich)(https://github.com/VladislavSenkevich).
- [MongoDB Output Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/outputs/mongodb/README.md)(`mongodb`) - Contributed by [@bustedware](https://github.com/bustedware).

#### Aggregator

- [Starlark Aggregator](https://github.com/influxdata/telegraf/blob/master/plugins/aggregators/starlark/README.md)(`starlark`) - Contributed by [@essobedo](https://github.com/essobedo).

## v1.20.4

- Update `BurntSushi/toml` from 0.3.1 to 0.4.1.
- Update `gosnmp` module from 1.32 to 1.33.
- Update `go.opentelemetry.io/otel` from v0.23.0 to v0.24.0.
- Fix plugin linters.

### Input plugin updates

- Cisco Model-Driven Telemetry (`cisco_telemetry_mdt`): Move to new protobuf library.
- InfluxDB (`influxdb`): Update input schema docs.
- Intel RDT (`intel_rdt`): Correct the timezone to use local timezone by default instead of UTC from metrics gathered from the `pqos` tool.
- IPMI Sensor (`ipmi`): Redact passwords in log files to maintain security.
- Modbus (`modbus`): Do not build on OpenBSD.
- MySQL (`mysql`):
    - Fix type conversion follow-up.
    - Correctly set the default paths.
- NVIDIA SMI (`nvidia_smi`): Correctly set the default paths.
- Proxmox (`proxmox`): Parse the column types of the server status.
- SQL Server (`sqlserver`): Add elastic pool in supported versions.

### Output plugin updates

- Loki (`loki`): Include the metric name as a label for improved query performance and metric filtering.

## v1.20.3

- Update Go to 1.17.2.
- Update `gjson` module to v1.10.2.
- Update Snowflake database driver module to 1.6.2.
- Update `github.com/apache/thrift` module from 0.14.2 to 0.15.0.
- Update `github.com/aws/aws-sdk-go-v2/config` module from 1.8.2 to 1.8.3.
- Update `github.com/Azure/azure-kusto-go` module from 0.3.2 to 0.4.0.
- Update `github.com/docker/docker` module from 20.10.7+incompatible to 20.10.9+incompatible.
- Update `github.com/golang-jwt/jwt/v4` module from 4.0.0 to 4.1.0.
- Update `github.com/jaegertracing/jaeger` module from 1.15.1 to 1.26.0.
- Update `github.com/prometheus/common` module from 0.26.0 to 0.31.1.

### Input plugin updates

- IPMI Sensor (`ipmi_sensor`): Redact IPMI password in logs.
- Kube Inventory (`kube_inventory`):
    - Do not skip resources with zero s/ns timestamps.
    - Fix segfault in ingress, persistentvolumeclaim, statefulset.
- Procstat (`procstat`): Revert and fix tag creation.
- SQL Server (`sqlserver`): Add integration tests.
- Amazon CloudWatch (`cloudwatch`): Use the AWS SDK v2 library.
- ZFS (`zfs`): Check return code of zfs command for FreeBSD.
- Ethtool (`ethtool`): Add normalization of tags.
- Internet Speed (`internet_speed`): Resolve missing latency field.
- Prometheus (`prometheus`):
    - Decode Prometheus scrape path from Kubernetes labels.
    - Move err check to correct place.
- Procstat (`procstat`): Correct conversion of int with specific bit size.
- Webhooks (`webhooks`): Provide more fields.
- MongoDB (`mongodb`): Solve compatibility issue when using 5.x relicaset.
- Intel RDT (`intel_rdt`): Allow sudo usage.
- MySQL (`mysql`): Fix inconsistent metric types.

### Processor plugin updates

- Starlark (`starlark`): Pop operation for non-existing keys.

### New plugins

#### External

- [IBM DB2](https://github.com/bonitoo-io/telegraf-input-db2): Contributed by @sranka.
- [Oracle Database](https://github.com/bonitoo-io/telegraf-input-oracle): Contributed by @sranka.

## v1.20.2

- Fix makefile typo that prevented i386 tar and rpm packages from being built.

### Input plugin updates

- Cloudwatch (`cloudwatch`): Use new session API.
- Stackdriver (`stackdriver`): Migrate to `cloud.google.com/go/monitoring/apiv3/v2`.

### Parser plugin updates

- JSON V2 (`json_v2`): Duplicate line\_protocol when using object and fields.
- Influx (`influx`): Fix memory leak.

## v1.20.1

- Fix output buffer never completely flushing.
- Update `k8s.io/apimachinery` module to 0.22.2.
- Update `consul` module to 1.11.0.
- Update `github.com/testcontainers/testcontainers-go` module to 0.11.1.
- Update `github.com/Azure/go-autorest/autorest/adal` module.
- Update `github.com/Azure/go-autorest/autorest/azure/auth module` to 0.5.8.
- Update `cloud.google.com/go/pubsub` module to 1.17.0.
- Update `github.com/aws/smithy-go` module to 1.8.0.

### Input plugin updates

- ElasticSearch (`elasticsearch_query`): Add custom time/date format field.
- OpenTelemetry (`opentelemetry`): Fix error returned to OpenTelemetry client.
- Couchbase (`couchbase`): Fix insecure certificate validation.
- MongoDB (`mongodb`): Fix panic due to nil dereference.
- Intel RDT (`intel_rdt`): Prevent timeout when logging.
- Procstat (`procstat`): Add missing tags.

### Output plugin updates

- Loki (`loki`): Update http\_headers setting to match sample config.
- MQTT (`mqtt`): Add “keep alive” config option and documentation around issue with eclipse/mosquito version.

## v.1.20

- Update Go to 1.17.0
- Update runc module to v1.0.0-rc95.
- Migrate `dgrijalva/jwt-go` to `golang-jwt/jwt/v4`.
- Update `thrift` module to 0.14.2 and `zipkin-go-opentracing` 0.4.5.
- Update `cloud.google.com/go/pubsub` module to 1.15.0.
- Update `github.com/tinylib/msgp` module to 1.1.6.

### Input plugin updates

- MongoDB (`mongodb`): Change command based on server version.
- SQL (`sql`): Make timeout apply to single query.
- SystemD Units (`systemd_units`): Add pattern support.
- Cloudwatch (`cloudwatch`):
    - Pull metrics from multiple AWS CloudWatch namespaces.
    - Support AWS Web Identity Provider.
- Modbus (`modbus`): Add support for RTU over TCP.
- Procstat (`procstat`): Support cgroup globs and include `systemd` unit children.
- Suricata (`suricata`): Support alert event type.
- Prometheus (`prometheus`): Add ability to query Consul Service catalog.
- HTTP Listener V2 (`http_listener_v2`): Allow multiple paths and add path\_tag.
- HTTP (`http`): Add cookie authentication.
- Syslog (`syslog`): Add RFC 3164 support for BSD-style syslog messages.
- Jenkins (`jenkins`): Add option to include nodes by name.
- SNMP Trap (`snmp_trap`): Improve MIB lookup performance.
- Smart (`smart`): Add power mode status.
- New Relic (`newrelic`): Add option to override `metric_url`.

### Output plugin updates

- Dynatrace (`dynatrace`): Remove hardcoded int value.
- InfluxDB v2 (`influxdb_v2`): Increase accepted retry-after header values.
- SQL (`sql`): Add bool datatype.
- Prometheus Client (`prometheus_client`): Add Landing page.
- HTTP (`http`): Add cookie authentication.

### Serializer plugin updates

- Prometheus (`prometheus`): Update timestamps and expiration time as new data arrives.

### Parser plugin updates

- XPath (`xpath`): Add JSON, MessagePack, and Protocol-buffers format support.

### New plugins

#### Input

- [Elasticsearch Query](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/elasticsearch_query) - Contributed by @lpic10
- [Internet Speed Monitor](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/internet_speed) - Contributed by @ersanyamarya
- [mdstat](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/mdstat) - Contributed by @johnseekins
- [AMD ROCm System Management Interface (SMI)](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/amd_rocm_smi) - Contributed by @mconcas

#### Output

- [OpenTelemetry](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/opentelemetry) - Contributed by @jacobmarble
- [Azure Data Explorer](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/azure_data_explorer) - Contributed by @minwal

## v.1.19.3

- Update `sirupsen/logrus` module from 1.7.0 to 1.8.1.
- Update `testcontainers/testcontainers-go` module from 0.11.0 to 0.11.1.
- Update `golang/snappy` module from 0.0.3 to 0.0.4.
- Update `aws/aws-sdk-go-v2` module from 1.3.2 to 1.8.0.
- Update `sensu/go` module to v2.9.0.
- Update `hashicorp/consul/api` module to 1.9.1.

### Input plugin updates

- Prometheus (`prometheus`): Fix Kubernetes pod discovery.
- Redis (`redis`) Improve redis commands documentation.
- Clickhouse (`clickhouse`): Fix panic, improve handling empty result set.
- OPC UA: (`opcua`):
    - Avoid closing session on a closed connection.
    - Fix reconnection regression introduced in 1.19.1.
    - Don’t skip good quality nodes after encountering bad quality node.
- Kubernetes Inventory (`kube_inventory`): Fix k8s nodes and pods parsing error.
- PostgreSQL (`postgresql`): Normalize unix socket path.
- vSphere (`vsphere`): Update `vmware/govmomi` module to v0.26.0 in order to support vSphere 7.0.

### Output plugin updates

- Loki (`loki`): Sort logs by timestamp before writing to Loki.
- CrateDB (`cratedb`): Replace dots in tag keys with underscores.

### Processor plugin updates

- AWS (`aws`): Refactor EC2 init.

## v.1.19.2

- Update Go to 1.16.6.
- Linter fixes.
- Update `dynatrace-metric-utils-go` module to v0.2.0.
- Detect changes to configuration and reload Telegraf.

### Input plugin updates

- CGroup (`couchbase`): Allow for multiple keys when parsing cgroups.
- Kubernetes (`kubernetes`): Update plugin to attach pod labels to the `kubernetes_pod_volume` and `kubernetes_pod_network` metrics.
- Kubernetes Inventory (`kube_inventory`): Fix a segmentation fault when selector labels were not present on a persistent volume claim.
- MongoDB (`mongodb`): Switch to official `mongo-go-driver` module to fix an SSL authentication failure.
- NSQ Consumer (`couchbase`): Fix a connection error when attempting to connect to an empty list of servers.
- Prometheus (`prometheus`): Fix Prometheus cAdvisor authentication.
- SQL (`sql`): Fix issue when handling a boolean column.
- SQL Server (`sqlserver`):
    - Add TempDB troubleshooting stats and missing v2 query metrics.
    - Update to provide more detailed error messaging.
- StatsD (`statsd`): Fix a regression that didn’t allow integer percentiles.
- x509 Certificate (`x509_cert`): Fix an issue where plugin would hang indefinitely to a UDP connection.

### Output plugin updates

- Dynatrace Output (`dynatrace`):
    - Update plugin to allow optional default dimensions.
    - Fix a panic caused by uninitialized `loggedMetrics` map.
- InfluxDB (`influxdb`): Fix issue where metrics were reporting as written but not actually written.

### Processor plugin updates

- IfName (`ifname`): Fix issue with SNMP empty metric name.

### Parser plugin updates

- JSON v2 (`json_v2`):
    - Simplify how nesting is handled in parser.
    - Add support for large uint64 and int64 numbers.
    - Fix an issue to handle nested objects in arrays properly.

## v.1.19.1

- Update nat-server module to v2.2.6.
- Update apimachinary module to v0.21.1.
- Update jwt module to v1.2.2 and jwt-go module to v3.2.3.
- Update couchbase module to v0.1.0.
- Update signalfx module to v3.3.34.
- Update gjson module to v1.8.0.
- Linter fixes.

### Input plugin updates

- SQL Server (`sqlserver`): Require authentication method to be specified.
- Kube Inventory (`kube_inventory`): Fix segfault.
- Couchbase (`couchbase`): Fix panic.
- KNX (`knx_listener`): Fix nil pointer panic.
- Procstat (`procstat`): Update gopsutil module to fix panic.
- RabbitMQ (`rabbitmq`) Fix JSON unmarshall regression.
- Dovecot (`dovecot`): Exclude read-timeout from being an error.
- StatsD(`statsd`) Don’t stop parsing after parsing error.
- SNMP (`snmp`): Add a check for oid and name to prevent empty metrics.
- (`x509_cert`):
    - Fix ‘source’ tag for https.
    - Fix SNI support.

### Output plugin updates

- (`http`): Fix toml error when parsing insecure\_skip\_verify.

### Parser plugin updates

- (`json_v2`): Don’t require tags to be added to included\_keys.

## v1.19.0

- Update Go to 1.16.5.

### Bug fixes

- Update pgx to v4.
- Fix reading configuration files starting with HTTP:
- `serializers.prometheusremotewrite`: Update dependency and remove tags with empty values.
- `outputs.kafka`: Don’t prevent telegraf from starting when there’s a connection error.
- `parsers.prometheusremotewrite`: Update prometheus dependency to v2.21.0.
- `outputs.dynatrace`: Use dynatrace-metric-utils.
- Many linter fixes. (Thanks @zak-pawel and all!)

### Features

- Configuration file environment variable can now be a URL.
- Add named timestamp formats.
- Allow multiple `--config` and `--config-directory` flags.

### Plugin updates

#### Input plugin updates

- (`aliyuncms`): Add configuration option list of regions to query.
- (`cisco_telemetry_mdt`): Add support for events and class based query.
- (`cloudwatch`): Add wildcard support in dimensions configuration.
- (`couchbase`): Add ~200 more Couchbase metrics via buckets endpoint.
- (`dovecot`): Add support for Unix domain sockets.
- (`http_listener_v2`): Add support for snappy compression
- (`http`): Add OAuth2 to HTTP input.
- (`kinesis_consumer`): Add `content_encoding` option with gzip and zlib support.
- (`logstash`): Add support for version 7 queue statistics.
- (`mongodb`): Optionally collect top statistics.
- (`mysql`): Gather all MySQL channels.
- (`ping`): Add an option to specify packet size.
- (`sqlserver`): Add an optional health metric.
- (`sqlserver`): Added `login_name`.
- (`sqlserver`): Enable Azure Active Directory (AAD) authentication.
- (`sqlserver`): input/sqlserver: Add service and save connection pools.
- (`vsphere`): Add configuration option for the historical interval duration.
- (`x509_)cert`: Wildcard support for certificate filenames.

#### Output plugin updates

- (`datadog`): Add HTTP proxy to DataDog output.
- (`graphite`): Allow more characters in graphite tags.

#### Parser plugin updates

- (`prometheusremotewrite`): Add Starlark script for renaming metrics.
- (`value`): Add custom field name configuration option.

#### Processor plugin updates

- (`enum`): Support `float64`.
- (`starlark`): Add an example showing how to obtain IOPS from `diskio` input.
- (`starlark`): Add `math` module.
- (`starlark`): Add `time` module.
- (`starlark`): Support nanosecond resolution timestamp.
- (`strings`): Add UTF-8 sanitizer.

### New plugins

#### Input

- [Alibaba CloudMonitor Service (Aliyun)](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/aliyuncms) - Contributed by @i-prudnikov
- [Intel Data Plane Development Kit (DPDK)](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/dpdk) - Contributed by @p-zak
- [KNX](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/knx_listener) - Contributed by @DocLambda
- [OpenTelemetry](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/opentelemetry) - Contributed by @jacobmarble
- [SQL](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/sql) - Contributed by @srebhan

#### Output

- [AWS Cloudwatch logs](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/cloudwatch_logs) - Contributed by @i-prudnikov
- [SQL](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/sql) - Contributed by @illuusio
- [Websocket](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/websocket) - Contributed by @FZambia

#### Parser

- [Prometheus Remote Write](https://github.com/influxdata/telegraf/tree/master/plugins/parsers/prometheusremotewrite) - Contributed by @influxdata
- [JSON V2](https://github.com/influxdata/telegraf/tree/master/plugins/parsers/json_v2) - Contributed by @influxdata

#### External

- [Big Blue Button](https://github.com/SLedunois/bigbluebutton-telegraf-plugin) - Contributed by @SLedunois
- [dnsmasq](https://github.com/machinly/dnsmasq-telegraf-plugin) - Contributed by @machinly
- [ldap\_org and ds389](https://github.com/falon/CSI-telegraf-plugins) - Contributed by @falon
- [x509\_crl](https://github.com/jcgonnard/telegraf-input-x590crl) - Contributed by @jcgonnard

## v1.18.3

- Add FreeBSD ARMv7 build.
- Dependencies:
    - Migrate from `soniah/gosnmp` to `gosnmp/gosnmp` v1.32.0.
    - Migrate from `docker/libnetwork/ipvs` to `moby/ipvs`.
    - Migrate from `ericchiang/k8s` to `kubernetes/client-go`.
    - Update `hashicorp/consul/api` module to v1.8.1.
    - Update `shirou/gopsutil` to v3.21.3.
    - Update `microsoft/ApplicationInsights-Go` to v0.4.4
    - Update `gogo/protobuf` to v1.3.2.
    - Update `Azure/go-autorest/autorest/azure/auth` to v0.5.6 and `Azure/go-autorest/autorest` to v0.11.17.
    - Update `collectd.org` to v0.5.0.
    - Update `nats-io/nats.go` to v1.10.0.
    - Update `golang/protobuf` to v1.5.1.

### Input plugin updates

- [Prometheus Input](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/prometheus): Add ability to set user agent when scraping Prometheus metrics.
- [Kinesis Input](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/kinesis_consumer): Fix repeating parser error.
- [SQL Server Input](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/sqlserver): Remove disallowed white space from `sqlServerRingBufferCPU` query.

### Output plugin updates

- [Elasticsearch Output](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/elasticsearch/README.md): Add ability to to enable gzip compression.

## v1.18.2

- Make JSON format compatible with nulls to ensure Telegraf successfully detects null values and returns an empty metric without error.
- Update `common.shim` by changing `NewStreamParser` to accept larger inputs from scanner.

### Input plugin updates

- [APCUPSD Input](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/apcupsd/README.md) (`apcupsd`): Resolve an ‘ALARMDEL’ bug in a forked repository. This fix ensures the plugin works when `no alarm` delay duration is set.
- [NFS Client Input](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/nfsclient) (`nfsclient`): Update to successfully collect metrics other than read and write.
- [SNMP Input](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/snmp/README.md) (`snmp`): Update to log snmpv3 auth failures.
- [VMware vSphere Input](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/vsphere/README.md) (`vsphere`): Add `MetricLookback` setting to handle reporting delays in vCenter 6.7 and later.
- [OPC UA Client Input](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/opcua/README.md) (`opcua`): Fix error handling.

### Output plugin updates

- [Sumo Logic Output](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/outputs/sumologic/README.md) (`sumologic`): Add support to [sanitize the metric name](https://github.com/influxdata/telegraf/tree/release-1.18/plugins/serializers/carbon2#metric-name-sanitization) in Carbon2 serializer.

### Processor plugin updates

- [Converter Processor](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/processors/converter/README.md) (`converter`): Add support for `float64` to support converting longer hexadecimal string values to a numeric type without losing in precision. Note, if a string number exceeds the size limit for `float64`, precision may be lost.

## v1.18.1

- Agent: Closes running outputs when agent reloads on SIGHUP.

### Input plugin updates

- [Docker Input](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/docker) (`docker`): Fix panic when parsing container statistics.
- [Exec Input](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/exec) (`exec`): Fix truncated messages in debug mode; debug mode now shows full messages.
- [IPMI Sensor Input](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/ipmi_sensor) (`ipmi_sensor`): Fix panic by implementing a length check to plugin.
- [MySQL Input](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/mysql) (`mysql`): Fix the ability to handle ‘binary logs’ query for MySQL version 8.0+.
- [NFS Client Input](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/nfsclient) (`nfsclient`): Fix integer overflow in fields received by mountstat.
- [Ping Input](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/ping) (`ping`): Resolve error that prevented the agent from running when an unprivileged UDP ping was sent. Now, `SetPrivileged(true)` is always true in native mode to ensure a privileged ICMP ping is sent.
- [SNMP Input](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/snmp) (`snmp`): Fix `init()` when no MIBs are installed.
- [SQL Server Input](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/sqlserver) (`sqlserver`): Fix `sqlserver_process_cpu` calculation.
- [Tail Input](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/tail) (`tail`): Added configurable option to override `path` tag.

### Output plugin updates

- [Azure Monitor Output](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/azure_monitor) (`azure_monitor`): Fix an issue to handle error when initializing the authentication object.
- [Yandex Cloud Monitoring Output](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/yandex_cloud_monitoring) (`yandex_cloud_monitoring`): Fix an issue to use correct computed metadata URL to get `folder-id`.

### Processor plugin updates

- [ifName](https://github.com/influxdata/telegraf/tree/master/plugins/processors/ifname) (`ifname`): Retrieve interface name more efficiently.

## v1.18

### Features

- Update to Go 1.16.2.
- Add code signing for Windows and macOS.
- More SNMP v3 authentication protocols, including SHA-512.
- Add support for [DataDog distributions](https://docs.datadoghq.com/metrics/distributions/#counting-distribution-metrics) metric type.

### New plugins

#### Inputs

- [Beat](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/beat)(`beat`) - Contributed by [@nferch](https://github.com/nferch)
- [CS:GO](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/csgo)(`csgo`) - Contributed by [@oofdog](https://github.com/oofdog)
- [Directory Monitoring](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/directory_monitor)(`directory_monitor`) - Contributed by [@influxdata](https://github.com/influxdata)
- [NFS](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/nfsclient)(`nfsclient`) - Contributed by [@pmoranga](https://github.com/pmoranga)
- [RavenDB](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/ravendb)(`ravendb`) - Contributed by [@ml054](https://github.com/ml054) and [@bartoncasey](https://github.com/bartoncasey)

#### Outputs

- [Grafana Loki](https://github.com/influxdata/telegraf/blob/master/plugins/outputs/loki)(`loki`) - Contributed by [@eraac](https://github.com/eraac)
- [Sensu](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/sensu)(`sensu`) - Contributed by [@calebhailey](https://github.com/calebhailey)
- [SignalFX](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/signalfx)(`signalfx`) - Contributed by [@keitwb](https://github.com/keitwb)

#### External

- [GeoIP](https://github.com/a-bali/telegraf-geoip)(`geoip`) - Contributed by [@a-bali](https://github.com/a-bali)
- [Plex Webhook](https://github.com/russorat/telegraf-webhooks-plex)(`plex`) - Contributed by [@russorat](https://github.com/russorat)
- [SMCIPMI](https://github.com/jhpope/smc_ipmi)(`smc_ipmi`) - Contributed by [@jhpope](https://github.com/jhpope)

#### Aggregators

- [Derivative](https://github.com/influxdata/telegraf/tree/master/plugins/aggregators/derivative)(`derivative`) - Contributed by [@KarstenSchnitter](https://github.com/karstenschnitter)
- [Quantile](https://github.com/influxdata/telegraf/tree/master/plugins/aggregators/quantile)(`quantile`) - Contributed by [@srebhan](https://github.com/srebhan)

#### Processors

- [AWS EC2 Metadata](https://github.com/influxdata/telegraf/tree/master/plugins/processors/aws/ec2)(`aws_ec2`) - Contributed by [@pmalek-sumo](https://github.com/pmalek-sumo)

#### Parsers

- [XML](https://github.com/influxdata/telegraf/tree/master/plugins/parsers/xml)(`xml`) - Contributed by [@srebhan](https://github.com/srebhan)

#### Serializers

- [MessagePack](https://github.com/influxdata/telegraf/tree/master/plugins/serializers/msgpack)(`msgpack`) - Contributed by [@dialogbox](https://github.com/dialogbox)

## v.1.17.3

- Update to Go 1.15.8.

### Input plugin updates

- Filestat (`filestat`): Skip missing files.
- MQTT Consumer (`mqtt_consumer`): Fix reconnection issues.
- Ping (`ping`):
    - Fix a timeout for `deadline` configuration.
    - Update README with correct cmd for native ping on Linux.
    - Fix percentile calculations.
- SNMP (`snmp`): Add support to expose IPv4/IPv6 as connection-schemes.
- x509 Certificate (`x509_cert`): Fix a timeout issue.

### Output plugin updates

- InfluxDB v1.x (`influxdb`): Validate InfluxDB response after creating a database to avoid JSON parsing errors.
- Warp10 (`warp10`): Add support for commas in tags to be URL encoded.

### Miscellaneous fixes and updates

- Telegraf configuration file (`telegraf.conf`): Resolve issue reading `flush_jitter` output.
- Library updates:
    - Update `github.com/gopcua/opcua` to 0.1.13.
    - Update `go-ping` to latest version.

## v.1.17.2

### Input plugin updates

- `ping`:
    - Added support to the interface in native mode using either the name or IP address.
    - Resolved regression from 1.17.1 by adding back missing function.

## v.1.17.1

### Features

- Add Event Log support for Windows platforms.
- Allow specifying SNI hostnames in `common.tls`.

### Input plugin updates

- `csv`:
    - Add ability to define an array of string skip values.
    - Address issue of ignoring missing values.
- `gnmi`: Metric path no longer has leading character truncated.
- `http_listener_v2`: Fixed an issue with `stop()` when plugin fails to start.
- `ipmi_sensor`:
    - Add setting to enable caching.
    - Add `hex_key` parameter.
- `jenkins`: Add support for inclusive job list.
- `lustre2`: No longer crashes if the field name and value are not separated.
- `ping`: Use go-ping library when `method = "native"` in the configuration
- `prometheus`: Use mime-type to handle protocol-buffer responses.
- `procstat`:
    - Provide an option to include core count when reporting `cpu_usage`
    - Use the same timestamp for all metrics in the same `Gather()` cycle.
- `postgresql_extensible`: Add timestamp column option to postgres\_extensible to handle log-like queries.
- `snmp`: Extended the internal SNMP wrapper to support AES-192, AES-192C, AES-256, and AES-256C.
- `webhooks`: Use the `measurement` json field from the Particle.io webhook as the measurement name.
- `x509_cert`: Fixed a timeout issue
- `zookeeper`: Improve `mntr` regex expression to match user-specific keys.

### Output plugin updates

- `http`: Add option to control idle connection timeout.
- `influxdb_v2`:
    - Log no longer flooded with errors when Elasticsearch receiver is in read-only state.
    - Add exponential backoff and respecting client error responses.

### Aggregator plugin updates

- `merge`: Performance optimization improvements.

## v1.17.0

### Features

- Update Go to 1.15.5.
- Added support for Linux/ppc64le.

### New plugins

#### Inputs

- [Intel Powerstat](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/intel_powerstat/README.md)(`intel_powerstat`)
- [Riemann Listener](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/riemann_listener/README.md)(`riemann`)

#### Outputs

- [Logz.io](https://github.com/influxdata/telegraf/blob/master/plugins/outputs/logzio/README.md)(`logzio`)
- [Yandex Cloud Monitoring](https://github.com/influxdata/telegraf/blob/master/plugins/outputs/yandex_cloud_monitoring/README.md)(`yandex_cloud_monitoring`)

#### Output data formats (serializers)

- [Prometheus Remote Write](https://github.com/influxdata/telegraf/blob/master/plugins/serializers/prometheusremotewrite/README.md)(`prometheusremotewrite`)

#### Parsers

- [Prometheus](https://github.com/influxdata/telegraf/blob/master/plugins/parsers/prometheus/README.md)(`prometheus`)

### Input plugin updates

- `aerospike`: Fix edge case where unexpected hex string was converted to integer if all digits.
- `bcache`: Fix tests for Windows.
- `bind`: Add configurable timeout.
- `carbon2`: Fix tests.
- `ecs`: Remove duplicated field from `ecs_task`.
- `execd`: Add support for new lines in line protocol fields.
- `github`: Add query of pull request statistics.
- `graphite`: Parse tags.
- `http`: Add proxy support.
- `http_response`: Fix network test.
- `jenkins`: Add build number field to `jenkins_job` measurement.
- `kafka_consumer`: Enable `ztsd` compression and idempotent writes.
- `kube_inventory`:
    - Fix issue with missing metrics when pod has only pending containers.
    - Update string parsing of allocatable cpu cores.
- `modbus`: Add FLOAT64-IEEE support.
- `monit`: Add `response_time`.
- `mysql`: Add per user metrics.
- `mqtt_consumer`: Fix issue with concurrent map write.
- `opcua`Add node groups.
- `ping`:
    - Add percentiles.
    - Fix potential issue with race condition.
- `snmp`:
    - Add support for converting hex strings to integers.
    - Translate field values.
- `socket_listener`: Fix crash when receiving invalid data.
- `sqlserver`:
    - Add tags for monitoring readable secondaries for Azure SQL MI.
    - Add SQL Server HA/DR Availability Group queries.
    - Remove duplicate column (`session_db_name`).
    - Add column `measurement_db_type` to output of all queries if not empty.
- `statsd`: Add configurable Max TTL duration.
- `vsphere`: Fix spelling of datacenter check.
- `win_services`: Add Glob pattern matching.
- `zfs`: Add dataset metrics.

### Output plugin updates

- `kafka`: Enable `ztsd` compression and idempotent writes.
- `nats`: Add `name` parameter.

### Processor plugin updates

- `starlark`: Can now store state between runs using a global state variable.

## v1.16.3

### Features

- Update `godirwalk` to 1.16.1 for Dragonfly BSD support.

### Input plugin updates

- APCUPSD (`apcupsd`): Add driver and CUDA version.

- CSV Parser (`csv`): Fix issue where CSV timestamp was being read as Unix instead of Go reference time.

- gNMI (`gnmi`): Add logging of `SubscribeResponse_Error` response types.

- NVIDIA SMI (`nvidia_smi`): Add driver and CUDA version.

- PHP-FPM (`phpfpm`): Fix issue with “index out of range” error.

- SQL Server (`sqlserver`): Fix typo in `database_name` column.

### Output plugin updates

- Wavefront (`wavefront`):
    - Distinguish between retryable and non-retryable errors .
    - Add debug-level logging for metric data that is not retryable.

### Parser plugin updates

- Starlark (`starlark`):
    - Allow the processor to manage errors that occur in the `apply` function.
    - Add support for logging.
    - Add capability to return multiple metrics.

## v1.16.2

### Input plugin updates

- CSV Parser (`csv`): Fix parsing multiple CSV files with different headers.
- DC/OS (`dcos`): Fix high-severity vulnerability in previous version of the `jwt-go` library.
- gNMI (`gnmi`): Add support for bytes encoding for gNMI messages.
- Proxmox ( `proxmox`):
    - Fix a few issues with error reporting.
    - Now ignores QEMU templates.
- RAS (`ras`): Fix tests failing on some systems.
- Redfish (`redfish`): Fix a parsing issue.
- SMART (`smart`): Fix an issue to recognize all devices from the configuration.
- SQL Server (`sqlserver`): Fix an issue with errors in on-premise instance queries.
- Systemd Units (`systemd_units`): Add `--plain` to the command invocation to fix an issue for reporting errors for units not found.
- vSphere (`vsphere`)
    - Fix to how metrics were counted.
    - Fix to metrics being skipped under in certain specific circumstances.

### Output plugin updates

- Dynatrace (`dynatrace`): Fix pushing metrics to separate Dynatrace environments.
- Wavefront (`wavefront`): Add `immediate_flush` tag.

## v1.16.1

### Input plugin updates

- Apache Kafka Consumer (`kafka_consumer`): Add Kafka SASL-mechanism authentication support for SCRAM-SHA-256, SCRAM-SHA-512, and GSSAPI.
- Microsoft SQL Server (`sqlserver`):
    - Fix a syntax error in Azure queries.
    - Remove synthetic performance counters that no longer exist from the `sqlserver_performance_counters` measurement.
    - Add a new tag (`sql_version_desc`) to identify the readable SQL Server version.
- RAS (`ras`):
    - Disable on specific Linux architectures (MIPS64, mips64le, ppc64le, riscv64).
    - Fix an issue to properly close file handlers.
- Processes (`processes`): Fix an issue with receiving `no such file or directory` stat error.
- Windows Performance Counters (`win_perf_counters`): Fix an issue with the counter where a negative denominator error would cause gathering operations to fail.

### Output plugin updates

- Apache Kafka (`kafka`): Add Kafka SASL-mechanism authentication support for SCRAM-SHA-256, SCRAM-SHA-512, GSSAPI.

## v1.16.0

### New plugins

#### Inputs

- [InfluxDB v2 Listener Input Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/influxdb_v2_listener/README.md)(`influxdb_v2_listener`) - Contributed by [@magichair](https://github.com/magichair)
- [Intel RDT Input Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/intel_rdt/README.md)(`intel_rdt`) - Contributed by [@p-zak](https://github.com/p-zak)
- [NSD Input Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/nsd/README.md)(`nsd`) - Contributed by [@gearnode](https://github.com/gearnode)
- [OPC UA Input Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/opcua/README.md)(`opcua`) - Contributed by [@influxdata](https://github.com/influxdata)
- [Proxmox Input Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/proxmox/README.md)(`proxmox`) - Contributed by [@effitient](https://github.com/effitient)
- [RAS Input Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/ras/README.md)(`ras`)- Contributed by [@p-zak](https://github.com/p-zak)
- [Windows Eventlog Input Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/win_eventlog/README.md)(`win_eventlog`) - Contributed by [@simnv](https://github.com/simnv)

#### Outputs

- [Dynatrace Output Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/outputs/dynatrace/README.md)(`dynatrace`) - Contributed by [@thschue](https://github.com/theschue)
- [Sumo Logic Output Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/outputs/sumologic/README.md) (`sumologic`) - Contributed by [@pmalek-sumo](https://github.com/pmalek-sumo)
- [Timestream Output Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/outputs/timestream) (`timestream`) - Contributed by [@piotrwest](https://github.com/piotrwest)

#### External

- [Amazon Cloudwatch Alarms Input Plugin](https://github.com/vipinvkmenon/awsalarms)(`awsalarms`) - Contributed by [@vipinvkmenon](https://github.com/vipinvkmenon)
- [YouTube Input Plugin](https://github.com/inabagumi/youtube-telegraf-plugin)(`youtube`) - Contrbuted by [@inabagumi](https://github.com/inabagumi)
- [Octoprint Input Plugin](https://github.com/sspaink/octoprint-telegraf-plugin)\[`octoprint`\] - Contributed by [@sspaink](https://github.com/sspaink/)
- [Systemd Timings Input Plugin](https://github.com/pdmorrow/telegraf-execd-systemd-timings)(`systemd-timings`) - Contributed by [@pdmorrow](https://github.com/pdmorrow)

### Input plugin updates

- `aerospike`: Add set and histogram reporting.
- `agent`:
    - Send metrics in FIFO order.
    - Fix issue with `execd restart_delay` being ignored.
    - Sort plugin name lists for output.
- `clickhouse`: Add additional metrics.
- `cloudwatch`: Implement AWS CloudWatch Input Plugin ListMetrics API calls to use Active Metric Filter.
- `consul`: Add `metric_version` flag.
- `docker`: Fix vulnerabilities found in BDBA scan.
- `execd`: Fix issue with `restart_delay` being ignored.
- `gnmi`: Next message after send returns EOF.
- `http_listener_v2`: Make header tags case-insensitive.
- `http_response`: Match on status code.
- `jenkins`: Multiple escaping occurs on at certain folder depth.
- `kubernetes`: Add missing error check for HTTP requirement failure.
- `modbus`: Extend support of fixed point values on input.
- `mongodb`: Add pages written from cache metric.
- `net`: Fix broken link to `proc.c`.
- `snmp` Add agent host tag configuration option.
- `smart`: Add missing NVMe attributes.
- `sqlserver`:
    - Database\_type config to Split up sql queries by engine type
    - Fixed query mapping
    - New refactoring and formatting queries.
    - Add more performance counters.
- `tail`:
    - Close file to ensure it has been flushed.
    - Fix following on EOF.

### Output plugin updates

- `elasticsearch`: Added `force_document_id` option to ES output enable resend data and avoid duplicated ES documents.
- `opentsdb`: Skips NaN and Inf JSON values.

### Processor plugin updates

- `execd`: Increased the maximum serialized metric size in line protocol
- `ifname`: Add `addTag` debugging.
- `starlark`: Add JSON parsing support.

### Bug fixes

- Fix `darwin` package build flags.
- `shim`:
    - Fix bug with loading plugins with no config.
    - Logger improvements.
    - Fix issue with loading processor config from `execd`.
- Initialize aggregation processors.
- Fix arch name in `deb/rpm` builds.
- Fix issue with `rpm /var/log/telegraf` permissions
- Fix `docker-image make` target.
- Remove Event field from `serializers.splunkmetric`.
- Fix panic on streaming processors using logging
- `ParseError.Error` panic in `parsers.influx`
- Fix `procstat` performance regression
- Fix serialization when using `carbon2`.
- Fix bugs found by LGTM analysis platform.
- Update to Go 1.15.2

## v.1.15.3

### Features

- `processors.starlark`:
    - Improve the quality of docs by executing them as tests.
    - Add pivot example.
- `outputs.application_insights`: Added ability to set endpoint url.
- `inputs.sqlserver`: Added new counter - Lock Timeouts (timeout > 0)/sec.

### Bug fixes

- `agent`: Fix minor error message race condition.
- `build`: Update dockerfiles to Go 1.14.
- `shim`:
    - Fix bug in logger affecting `AddError`.
    - Fix issue with `config.Duration`.
- `inputs.eventhub_consumer`: Fix string to int conversion.
- `inputs.http_listener_v2`: Make http header tags case-insensitive.
- `inputs.modbus`: Extend support of fixed point values.
- `inputs.ping`: Fix issue for FreeBSD’s ping6.
- `inputs.vsphere`: Fixed missing cluster name.
- `outputs.opentsdb` Fix JSON handling of values `NaN` and `Inf`.

## v1.15.2

### Bug Fixes

- Fix RPM `/var/log/telegraf` permissions.
- Fix tail following on EOF.

## v1.15.1

### Bug fixes

- Fix architecture in non-amd64 deb and rpm packages.

## v1.15.0

Critical bug that impacted non-amd64 packages was introduced in 1.15.0. **Do not install this release.** Instead, install 1.15.1, which includes the features, new plugins, and bug fixes below.

### Breaking changes

Breaking changes are updates that may cause Telegraf plugins to fail or function incorrectly. If you have one of the following plugins installed, make sure to update your plugin as needed:

- **Logparser** (`logparser`) input plugin: Deprecated. Use the `tail` input with `data_format = "grok"` as a replacement.
- **Cisco GNMI Telemetry** (`cisco_telemetry_gnmi`) input plugin: Renamed to `gnmi` to better reflect its general support for gNMI devices.
- **Splunkmetric** (`splunkmetric`) serializer: Several fields used primarily for debugging have been removed. If you are making use of these fields, they can be added back with the `tag` option.

### New plugins

#### Inputs

- [NGINX Stream STS Input Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/nginx_sts/README.md)(`nginx_sts`) - Contributed by [@zdmytriv](https://github.com/zdmytriv)
- [Redfish Input Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/redfish/README.md)(`redfish`) - Contributed by [@sarvanikonda](https://github.com/sarvanikonda)

#### Outputs

- [Execd Output Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/outputs/execd/README.md)(`execd`) - Contributed by [@influxdata](https://github.com/influxdata)
- [New Relic Output Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/outputs/newrelic/README.md)(`newrelic`) - Contributed by @hsingkalsi

#### Processors

- [Defaults Processor Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/processors/defaults/README.md)(`defaults`) - Contributed by [@jregistr](https://github.com/jregistr)
- [Execd Processor Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/processors/execd/README.md)(`execd`) - Contributed by [@influxdata](https://github.com/influxdata)
- [Filepath Processor Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/processors/filepath/README.md)(`filepath`) - Contributed by [@kir4h](https://github.com/kir4h)
- [Network Interface Name Processor Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/processors/ifname/README.md)(`ifname`) - Contributed by [@influxdata](https://github.com/influxdata)
- [Port Name Processor Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/processors/port_name/README.md)(`port_name`) - Contributed by [@influxdata](https://github.com/influxdata)
- [Reverse DNS Processor Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/processors/reverse_dns/README.md)(`reverse_dns`) - Contributed by [@influxdata](https://github.com/influxdata)
- [Starlark Processor Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/processors/starlark/README.md)(`starlark`) - Contributed by [@influxdata](https://github.com/influxdata)

### Features

- Telegraf’s `--test` mode runs processors and aggregators before printing metrics.
- Official packages built with Go 1.14.5.
- When updating the Debian package, you will no longer be prompted to merge the `telegraf.conf` file. Instead, the new version will be installed to `/etc/telegraf/telegraf.conf.sample`. The `tar` and `zip` packages now include the version in the top-level directory.
- Allow per input overriding of `collection_jitter` and `precision`.
- Deploy Telegraf configuration as `telegraf.conf.sample`.
- Use Docker log timestamp as metric time.
- Apply ping deadline to DNS lookup.
- Support multiple templates for graphite serializers.
- Add configurable separator graphite serializer and output.
- Add support for SIGUSR1 to trigger flush.
- Add support for once mode that writes to outputs and exits.
- Run processors and aggregators during test mode.
- Add timezone configuration to CSV parser.

#### Input plugin updates

- **Ceph Storage** (`ceph`): Add support for MDS and RGW sockets.
- **ECS** (`ecs`): Add v3 metadata support.
- **Fibaro** (`fibaro`): Add support for battery-level monitoring.
- **File** (`file`):
    - Support UTF-16.
    - Exclude `csv_timestamp_column` and `csv_measurement_column` from fields.
- **HTTP** (`http`): Add reading bearer token.
- **HTTP Listener v2** (`http_listener_v2`): Add ability to specify HTTP headers as tags.
- **HTTP Response** (`http_response`):
    - Add authentication support.
    - Allow collection of HTTP headers.
    - Add ability to collect response body as field.
- **Icinga 2** (`icinga2`):
    - Fix source field.
    - Add tag for server hostname.
- **InfluxDB Listener** (`influxdb_listener`): Add option to save retention policy as tag.
- **IPtables** (`iptables`): Extract target as a tag for each rule.
- **Kibana** (`kibana`): Fix `json unmarshal` error.
- **Kubernetes Inventory** (`kube_inventory`): Add ability to add selectors as tags.
- **Mem** (`mem`): Add laundry on FreeBSD.
- **Microsoft SQL Server** (`sqlserver`):
    - Add `VolumeSpace` query.
    - Add `cpu` query.
    - Add counter type to `perfmon` collector.
    - Improve compatibility with older server versions.
    - Fix typo in `total_elapsed_time_ms` field.
- **Modbus** (`modbus`):
    - Add support for 64-bit integer types.
    - Add retry when replica is busy.
    - Add ability to specify measurement per register.
- **MongoDB** (`monogdb`):
    - Add commands stats.
    - Add additional fields.
    - Add cluster state integer.
    - Add option to disable cluster status.
    - Add additional conccurrent transaction information.
- **NVIDIA SMI** (`nvidia_smi`): Add video codec stats.
- **Procstat** (`procstat`):
    - Improve performance.
    - Fix memory leak.
- **S.M.A.R.T.** (`smart`): Add missing `nvme` attributes.
- **SNMP Trap** (`snmp_trap`): Add SNMPv3 trap support.
- **System** (`system`): Fix incorrect uptime when clock is adjusted.
- **Tail** (`tail`): Support UTF-16.

#### Output plugin updates

- **Enum** (`enum`): Add integer mapping support.

#### Processor plugin updates

- **Date** (`date`):
    - Add field creation.
    - Add integer unix time support.
- **Wavefront** (`wavefront`): Add `truncate_tags` setting.

### Bug fixes

- Fix ability to write metrics to CloudWatch with IMDSv1 disabled.
- Fix vSphere 6.7 missing data issue.
- Fix gzip support in `socket_listener` with tcp sockets.
- Fix interval drift when `round_interval` is set in agent.
- Fix incorrect uptime when clock is adjusted.
- Remove trailing backslash from tag keys/values in `influx` serializer.
- Fix incorrect Azure SQL DB server properties.
- Send metrics in FIFO order.

## v1.14.5

### Bug fixes

- Improve the performance of the `procstat` input.
- Fix ping exit code handling on non-Linux operating systems.
- Fix errors in output of the `sensors` command.
- Prevent startup when tags have incorrect type in configuration file.
- Fix panic with GJSON multiselect query in JSON parser.
- Allow any key usage type on x509 certificate.
- Allow histograms and summary types without buckets or quantiles in `prometheus_client` output.

## v1.14.4

### Bug fixes

- Fix the `cannot insert the value NULL` error with the `PerformanceCounters` query in the `sqlServer` input plugin.
- Fix a typo in the naming of `the gc_cpu_fraction` field in the `influxdb` input plugin.
- Fix a numeric to bool conversion in the `converter` processor.
- Fix an issue with the `influx` stream parser blocking when the data is in buffer.

## v1.14.3

### Bug fixes

- Use same timestamp for all objects in arrays in the `json` parser.
- Handle multiple metrics with the same timestamp in `dedup` processor.
- Fix reconnection of timed out HTTP2 connections `influxdb` outputs.
- Fix negative value parsing in `impi_sensor` input.

## v1.14.2

### Bug fixes

- Trim white space from instance tag in `sqlserver` input .
- Use increased AWS Cloudwatch GetMetricData limit of 500 metrics per call.
- Fix limit on dimensions in `azure_monitor` output.
- Fix 64-bit integer to string conversion in `snmp` input.
- Fix shard indices reporting in `elasticsearch` input plugin.
- Ignore fields with Not a Number or Infinity floats in the JSON serializer.
- Fix typo in name of `gc_cpu_fraction` field of the `kapacitor` input.
- Don’t retry create database when using database\_tag if forbidden by the server in `influxdb` output.
- Allow CR and FF inside of string fields in InfluxDB line protocol parser.

## v1.14.1

### Bug fixes

- Fix `PerformanceCounter` query performance degradation in `sqlserver` input.
- Fix error when using the `Name` field in template processor.
- Fix export timestamp not working for Prometheus on v2.
- Fix exclude database and retention policy tags.
- Fix status path when using globs in `phpfpm`.

## v1.14

### Breaking changes

Breaking changes are updates that may cause Telegraf plugins to fail or function incorrectly. If you have one of the following plugins installed, make sure to update your plugin as needed:

- **Microsoft SQL Server** (`sqlserver`) input plugin: Renamed the `sqlserver_azurestats` measurement to `sqlserver_azure_db_resource_stats` to resolve an issue where numeric metrics were previously being reported incorrectly as strings.
- **Date** (`date`) processor plugin: Now uses the UTC timezone when creating its tag. Previously, the local time was used.

Support for SSL v3.0 is deprecated in this release. Telegraf now uses the [Go TLS library](https://golang.org/pkg/crypto/tls/).

### New plugins

#### Inputs

- [Arista LANZ Consumer](https://github.com/influxdata/telegraf/blob/release-1.14/plugins/inputs/lanz/README.md) - Contributed by [@timhughes](https://github.com/timhughes)
- [ClickHouse](https://github.com/influxdata/telegraf/blob/release-1.14/plugins/inputs/clickhouse/README.md)(`clickhouse`) - Contributed by [@kshvakov](https://github.com/kshvakov)
- [Execd](https://github.com/influxdata/telegraf/blob/release-1.14/plugins/inputs/execd/README.md)(`execd`) - Contributed by [@jgraichen](https://github.com/jgraichen)
- [Event Hub Consumer](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/eventhub_consumer/README.md)(`eventhub_consumer`) - Contributed by [@R290](https://github.com/R290)
- [InfiniBand](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/infiniband/README.md)(`infiniband`) - Contributed by [@willfurnell](https://github.com/willfurnell)
- [Modbus](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/modbus/README.md)(`modbus`) - Contributed by [@garciaolais](https://github.com/garciaolais)
- [Monit](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/monit/README.md)(`monit`) - Contributed by [@SirishaGopigiri](https://github.com/SirishaGopigiri)
- [SFlow](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/sflow/README.md)(`sflow`) - Contributed by [@influxdata](https://github.com/influxdata)
- [Wireguard](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/wireguard/README.md)(`wireguard`) - Contributed by [@LINKIWI](https://github.com/LINKIWI)

#### Processors

- [Dedup](https://github.com/influxdata/telegraf/blob/master/plugins/processors/dedup/README.md)(`dedup`) - Contributed by [@igomura](https://github.com/igomura)
- [S2 Geo](https://github.com/influxdata/telegraf/blob/master/plugins/processors/s2geo/README.md)(`s2geo`) - Contributed by [@alespour](https://github.com/alespour)
- [Template](https://github.com/influxdata/telegraf/blob/master/plugins/processors/template/README.md) (`template`) - Contributed by [@RobMalvern](https://github.com/RobMalvern)

#### Outputs

- [Warp10](https://github.com/influxdata/telegraf/blob/master/plugins/outputs/warp10/README.md)(`warp10`) - Contributed by [@aurrelhebert](https://github.com/aurrelhebert)

### Features

#### Input plugin updates

- **Apache Kafka Consumer** (`kafka_consumer`): Add SASL version control to support Microsoft Azure Event Hub.
- **Apcupsd** (`apcupsd`): Add new tag `model` and new metrics: `battery_date`, `nominal_input_voltage`, `nominal_battery_voltage`, `nominal_power`, `firmware`.
- **Cisco Model-driven Telemetry (MDT)** (`cisco_telemetry_gnmi`) input plugin:
    - Add support for GNMI DecimalVal type.
    - Replace dash (`-`) with underscore (`_`) when handling embedded tags.
- **DiskIO** (`diskio`): Add counters for merged reads and writes.
- **IPMI Sensor** (`ipmi_sensor`): Add `use_sudo` option.
- **Jenkins** (`jenkins`):
    - Add `source` and `port` tags to `jenkins_job` metrics.
    - Add new fields `total_executors` and `busy_executors`.
- **Kubernetes** (`kubernetes`): Add ability to collect pod labels.
- **Microsoft SQL Server** (`sqlserver`):
    - Add RBPEX IO statistics to DatabaseIO query.
    - Add space on disk for each file to DatabaseIO query.
    - Calculate DB Name instead of GUID in `physical_db_name`.
    - Add `DatabaseIO` TempDB per Azure DB.
    - Add `query_include` option for explicitly including queries.
    - Add `volume_mount_point` to DatabaseIO query.
- **MongoDB** (`mongodb`):
    - Add `page_faults` for WiredTiger storage engine.
    - Add latency statistics.
    - Add replica set tag (`rs_name`).
- **NATS Consumer** (`nats_consumer`): Add support for credentials file.
- **NGINX Plus API** (`nginx_plus_api`): Add support for new endpoints.
- **OpenLDAP** (`openldap`): Add support for MDB database information.
- **PHP-FPM** (`phpfpm`): Allow globs in FPM unix socket paths (`unixsocket`).
- **Procstat** (`procstat`): Add process `created_at` time.
- **Prometheus** (`prometheus`) input plugin: Add `label` and `field` selectors for Kubernetes service discovery.
- **RabbitMQ** (`rabbitmq`): Add `slave_nodes` and `synchronized_slave_nodes` metrics.
- **StatsD** (`statsd`): Add UDP internal metrics.
- **Unbound** (`unbound`): Expose [`-c cfgfile` option of `unbound-control`](https://linux.die.net/man/8/unbound-control) and set the default unbound configuration (`config_file= "/etc/unbound/unbound.conf`) in the Telegraf configuration file.
- **VMware vSphere** (`vsphere`): Add option to exclude resources by inventory path, including `vm_exclude`, `host_exclude`, `cluster_exclude` (for both clusters and datastores), and `datacenter_exclude`.
- **X.509 Certificate** (`x509_cert`): Add `server_name` override.

#### Output plugin updates

- **Apache Kafka** (`kafka`): Add `topic_tag` and `exclude_topic_tag` options.
- **Graylog** (`graylog`): Allow a user defined field (`short_message_field`) to be used as the `GELF short_message`.
- **InfluxDB v1.x** (`influxdb`): Add support for setting the retention policy using a tag (`retention_policy_tag`).
- **NATS Output** (`nats`): Add support for credentials file.

#### Aggregator plugin updates

- **Histogram** (`histogram`): Add non-cumulative histogram.

#### Processor plugin updates

- **Converter** (`converter`): Add support for converting `tag` or `field` to `measurement`.
- **Date** (`date`): Add date offset and timezone options.
- **Strings** (`strings`): Add support for titlecase transformation.

### Bug fixes

- Fix Telegraf log rotation to use actual file size instead of bytes written.
- Fix internal Telegraf metrics to prevent output split into multiple lines.
- **Chrony** (`chrony`) input plugin: When plugin is enabled, search for `chronyc` only.
- **Microsoft SQL Server** (`sqlserver`) input plugin:
    - Fix conversion to floats in AzureDBResourceStats query.
    - Fix case sensitive collation.
    - Fix several issues with DatabaseIO query.
    - Fix schedulers query compatibility with pre SQL-2016.
- **InfluxDB Listener** (`influxdb_listener`):
    - Fix request failing with EOF.
    - Continue parsing after error.
    - Set headers on ping URL.

## v1.13.4

### Release Notes

Official packages now built with Go 1.13.8.

### Bug fixes

- Parse NaN values from summary types in Prometheus (`prometheus`) input plugin.
- Fix PgBouncer (`pgbouncer`) input plugin when used with newer PgBouncer versions.
- Support up to 8192 stats in the Ethtool (`ethtool`) input plugin.
- Fix performance counters collection on named instances in Microsoft SQL Server (`sqlserver`) input plugin.
- Use add time for Prometheus expiration calculation.
- Fix inconsistency with input error counting in Telegraf v1.x (`internal`) input plugin.
- Use the same timestamp per call if no time is provided in Prometheus (`prometheus`) input plugin.

## v1.13.3

### Bug fixes

- Update Kibana (`kibana`) input plugin to support Kibana 6.4 and later.
- Prevent duplicate `TrackingIDs` from being returned in the following queue consumer input plugins:
    - Amazon Kineses Consumer (`kinesis_consumer`)
    - AMQP Consumer (`amqp_consumer`)
    - Apache Consumer (`apache_consumer`)
    - MQTT Consumer (`mqtt_consumer`)
    - NATS Consumer (`nats_consumer`)
    - NSQ Consumer (`nsq_consumer`)
- Increase support for up to 4096 statistics in the Ethtool (`ethtool`) input plugin.
- Remove expired metrics from the Prometheus Client (`prometheus_client`) output plugin. Previously, expired metrics were only removed when new metrics were added.

## v1.13.2

### Bug fixes

- Warn without error when Processes (`processes`) input is started on Windows.
- Only parse certificate blocks in X.509 Certificate (`x509_cert`) input plugin.
- Add custom attributes for all resource types in VMware vSphere (`vsphere`) input plugin.
- Support URL agent address form with UDP in SNMP (`snmp`) input plugin.
- Record device fields in the SMART (`smart`) input plugin when attributes is `false`.
- Remove invalid timestamps from Kafka messages.
- Update `json` parser to fix `json_strict` option and set `default` to `true`.

## v1.13.1

### Bug fixes

- Fix ServerProperty query stops working on Azure after failover.
- Add leading period to OID in SNMP v1 generic traps.
- Fix missing config fields in prometheus serializer.
- Fix panic on connection loss with undelivered messages in MQTT Consumer (`mqtt_consumer`) input plugin.
- Encode query hash fields as hex strings in SQL Server (`sqlserver`) input plugin.
- Invalidate diskio cache if the metadata mtime has changed.
- Show platform not supported warning only on plugin creation.
- Fix rabbitmq cannot complete gather after request error.
- Fix `/sbin/init --version` executed on Telegraf startup.
- Use last path element as field key if path fully specified in Cisco GNMI Telemetry (`cisco_telemetry_gnmi`) input plugin.

## v1.13

### Release Notes

Official packages built with Go 1.13.5. The Prometheus Format (`prometheus`) input plugin and Prometheus Client (`prometheus_client`) output have a new mapping to and from Telegraf metrics, which can be enabled by setting `metric_version = 2`. The original mapping is deprecated. When both plugins have the same setting, passthrough metrics are unchanged. Refer to the [Prometheus input plugin](https://github.com/influxdata/telegraf/blob/release-1.13/plugins/inputs/prometheus/README.md) for details about the mapping.

### New Inputs

- [Azure Storage Queue](https://github.com/influxdata/telegraf/blob/release-1.13/plugins/inputs/azure_storage_queue/README.md) (`azure_storage_queue`) - Contributed by [@mjiderhamn](https://github.com/mjiderhamn)
- [Ethtool](https://github.com/influxdata/telegraf/blob/release-1.13/plugins/inputs/ethtool/README.md) (`ethtool`) - Contributed by [@philippreston](https://github.com/philippreston)
- [SNMP Trap](https://github.com/influxdata/telegraf/blob/release-1.13/plugins/inputs/snmp_trap/README.md) (`snmp_trap`) - Contributed by [@influxdata](https://github.com/influxdata)
- [Suricata](https://github.com/influxdata/telegraf/blob/release-1.13/plugins/inputs/suricata/README.md) (`suricata`) - Contributed by [@satta](https://github.com/satta)
- [Synproxy](https://github.com/influxdata/telegraf/blob/release-1.13/plugins/inputs/synproxy/README.md) (`synproxy`) - Contributed by [@rfrenayworldstream](https://github.com/rfrenayworldstream)
- [Systemd Units](https://github.com/influxdata/telegraf/blob/release-1.13/plugins/inputs/systemd_units/README.md) (`systemd_units`) - Contributed by [@benschweizer](https://github.com/benschweizer)

### New Processors

- [Clone](https://github.com/influxdata/telegraf/blob/release-1.13/plugins/processors/clone/README.md) (`clone`) - Contributed by [@adrianlzt](https://github.com/adrianlzt)

### New Aggregators

- [Merge](https://github.com/influxdata/telegraf/blob/release-1.13/plugins/aggregators/merge/README.md) (`merge`) - Contributed by [@influxdata](https://github.com/influxdata)

### Features

- Add per node memory stats to RabbitMQ (`rabbitmq`) input plugin.
- Add ability to read query from file to PostgreSQL (`postgresql_extensible`) input plugin.
- Add replication metrics to the Redis (`redis`) input plugin.
- Support NX-OS telemetry extensions in Cisco Model-driven Telemetry (`cisco_telemetry_mdt`) input plugin.
- Allow `graphite` parser to create `Inf` and `NaN` values.
- Use prefix base detection for ints in `grok` parser.
- Add more performance counter metrics to Microsoft SQL Server (`sqlserver`) input plugin.
- Add millisecond unix time support to `grok` parser.
- Add container ID as optional source tag to Docker (`docker`) and Docker Log (`docker_log`) input plugins.
- Add `lang` parameter to OpenWeatherMap (`openweathermap`) input plugin.
- Log file open errors at debug level in Tail (`tail`) input plugin.
- Add timeout option to Amazon CloudWatch (`cloudwatch`) input plugin.
- Support custom success codes in HTTP (`http`) input plugin.
- Improve IPVS (`ipvs`) input plugin error strings and logging.
- Add strict mode to JSON parser that can be disabled to ignore invalid items.
- Add support for Kubernetes 1.16 and remove deprecated API usage.
- Add gathering of RabbitMQ federation link metrics.
- Add bearer token defaults for Kubernetes plugins.
- Add support for SNMP over TCP.
- Add support for per output flush jitter.
- Add a nameable file tag to File (`file`) input plugin.
- Add Splunk MultiMetric support.
- Add support for sending HTTP Basic Auth in InfluxDB (`influxdb`) input plugin.
- Add ability to configure the url tag in the Prometheus Format (`prometheus`) input plugin.
- Add Prometheus `metric_version=2` mapping to internal metrics/line protocol.
- Add Prometheus `metric_version=2` support to Prometheus Client (`prometheus_client`) output plugin.
- Add content\_encoding compression support to Socket Listener (`socket_listener`) input plugin.
- Add high resolution metrics support to Amazon CloudWatch (`cloudwatch`) output plugin.
- Add `SReclaimable` and `SUnreclaim` to Memory (`mem`) input plugin.
- Allow multiple certificates per file in X.509 Certificate (`x509_cert`) input plugin.
- Add additional tags to the X.509 Certificate (`x509_cert`) input plugin.
- Add batch data format support to File (`file`) output plugin.
- Support partition assignment strategy configuration in Apache Kafka Consumer (`kafka_consumer`) input plugin.
- Add node type tag to MongoDB (`mongodb`) input plugin.
- Add `uptime_ns` field to MongoDB (`mongodb`) input plugin.
- Support resolution of symlinks in Filecount (`filecount`) input plugin.
- Set message timestamp to the metric time in Apache Kafka (`kafka`) output plugin.
- Add base64decode operation to String (`string`) processor.
- Add option to control collecting global variables to MySQL (`mysql`) input plugin.

### Bug fixes

- Show correct default settings in MySQL (`mysql`) sample configuration.
- Use `1h` or `3h` rain values as appropriate in OpenWeatherMap (`openweathermap`) input plugin.
- Fix `not a valid field` error in Windows with Nvidia SMI (`nvidia_smi`) input plugin.
- Fix InfluxDB (`influxdb`) output serialization on connection closed.
- Fix ping skips remaining hosts after DNS lookup error.
- Log MongoDB oplog auth errors at debug level.
- Remove trailing underscore trimming from json flattener.
- Revert change causing CPU usage to be capped at 100 percent.
- Accept any media type in the Prometheus Format (`prometheus`) input plugin.
- Fix unix socket dial arguments in uWSGI (`uwsgi`) input plugin.
- Replace colon characters in Prometheus (`prometheus_client`) output labels with `metric_version=1`.
- Set TrimLeadingSpace when TrimSpace is on in CSV (`csv`) parser.

## v1.12.6

### Bug fixes

- Fix many plugin errors logged at debug logging level.
- Use nanosecond precision in Docker Log (`docker_log`) input plugin.
- Fix interface option with `method = native` in Ping (`ping`) input plugin.
- Fix panic in MongoDB (`mongodb`) input plugin if shard connection pool stats are unreadable.

## v1.12.5

### Bug fixes

- Fix incorrect results in Ping (`ping`) input plugin.
- Add missing character replacement to `sql_instance` tag.
- Change `no metric` error message to `debug` level in CloudWatch (`cloudwatch`) input plugin.
- Add missing `ServerProperties` query to SQLServer (`sqlserver`) input plugin documentation.
- Fix MongoDB `connections_total_created` field loading.
- Fix metric creation when node is offline in Jenkins (`jenkins`) input plugin.
- Fix Docker `uptime_ns` calculation when container has been restarted.
- Fix MySQL field type conflict in conversion of `gtid_mode` to an integer.
- Fix MySQL field type conflict with `ssl_verify_depth` and `ssl_ctx_verify_depth`.

## v1.12.4

- Build official packages with Go 1.12.12.

### Bug fixes

- Fix metric generation with Ping (`ping`) input plugin `native` method.
- Exclude alias tag if unset from plugin internal stats.
- Fix `socket_mode` option in PowerDNS Recursor (`powerdns_recursor`) input plugin.

## v1.12.3

- Build official packages with Go 1.12.10.

### Bug fixes

- Use batch serialization format in Exec (`exec`) output plugin.
- Use case-insensitive serial number match in S.M.A.R.T. (`smart`) input plugin.
- Add authorization header only when environment variable is set.
- Fix issue when running multiple MySQL and SQL Server plugin instances.
- Fix database routing on retry with `exclude_database_tag`.
- Fix logging panic in Exec (`exec`) input plugin with Nagios data format.

## v1.12.2

### Bug fixes

- Fix timestamp format detection in `csv` and `json` parsers.
- Apcupsd input (`apcupsd`)
    - Fix parsing of `BATTDATE`.
- Keep boolean values listed in `json_string_fields`.
- Disable Go plugin support in official builds.
- Cisco GNMI Telemetry input (`cisco_telemetry_gnmi`)
    - Fix path handling issues.

## v1.12.1

### Bug fixes

- Fix dependenciess on GLIBC\_2.14 symbol version.
- Filecount input (`filecount`)
    - Fix filecount for paths with trailing slash.
- Icinga2 input (`icinga2`)
    - Convert check state to an integer.
- Apache Kafka Consumer input (`kafka_consumer`)
    - Fix could not mark message delivered error.
- MongoDB input (`mongodb`)
    - Skip collection stats when disabled.
- HTTP Response input (`http_response`)
    - Fix error reading closed response body.
- Apcupsd input (`apcupsd`)
    - Fix documentation to reflect plugin.
- InfluxDB v2 output (`influxdb_v2`)
    - Display retry log message only when retry after is received.

## v1.12

### Release Notes

- The cluster health related fields in the Elasticsearch input have been split out from the `elasticsearch_indices` measurement into the new `elasticsearch_cluster_health_indices` measurement as they were originally combined by error.

### New Inputs

- [Apcupsd](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/apcupsd/README.md) (`apcupsd`) - Contributed by @jonaz
- [Docker Log](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/docker_log/README.md) (`docker_log`) - Contributed by @prashanthjbabu
- [Fireboard](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/fireboard/README.md) (`fireboard`) - Contributed by @ronnocol
- [Logstash](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/logstash/README.md) (`logstash`) - Contributed by @lkmcs @dmitryilyin @arkady-emelyanov
- [MarkLogic](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/marklogic/README.md) (`marklogic`) - Contributed by @influxdata
- [OpenNTPD](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/openntpd/README.md) (`openntpd`) - Contributed by @aromeyer
- [uWSGI](https://github.com/influxdata/telegraf/blob/master/plugins/inputs/uwsgi) (`uwsgi`) - Contributed by @blaggacao

### New Parsers

- [From Urlencoded](https://github.com/influxdata/telegraf/blob/master/plugins/parsers/form_urlencoded) (`form_urlencoded`) - Contributed by @byonchev

### New Processors

- [Date](https://github.com/influxdata/telegraf/blob/master/plugins/processors/date/README.md) (`date`) - Contributed by @influxdata
- [Pivot](https://github.com/influxdata/telegraf/blob/master/plugins/processors/pivot/README.md) (`pivot`) - Contributed by @influxdata
- [Tag Limit](https://github.com/influxdata/telegraf/blob/master/plugins/processors/tag_limit/README.md) (`tag_limit`) - Contributed by @memory
- [Unpivot](https://github.com/influxdata/telegraf/blob/master/plugins/processors/unpivot/README.md) (`unpivot`) - Contributed by @influxdata

### New Outputs

- [Exec](https://github.com/influxdata/telegraf/blob/master/plugins/outputs/exec/README.md) (`exec`) - Contributed by @Jaeyo

### Features

- Improve performance of `wavefront` serializer.
- Allow `regex` processor to append tag values.
- Add `starttime` field to `phpfpm` input.
- Add cluster name tag to elasticsearch indices.
- Add support for interface field in `http_response` input plugin.
- Add container uptime\_ns in `docker` input plugin.
- Add better user-facing errors for API timeouts in docker input.
- Add TLS mutual auth support to `jti_openconfig_telemetry` input.
- Add support for ES 7.x to `elasticsearch` output.
- Add basic auth to `prometheus` input plugin.
- Add node roles tag to `elasticsearch` input.
- Support floats in `statsd` percentiles.
- Add native Go ping method to `ping` input plugin.
- Resume from last known offset in `tail` input when reloading Telegraf.
- Add improved support for Azure SQL Database to `sqlserver` input.
- Add extra attributes for NVMe devices to `smart` input.
- Add `docker_devicemapper` measurement to `docker` input plugin.
- Add basic auth support to `elasticsearch` input.
- Support string field glob matching in `json` parser.
- Update gjson to allow multipath syntax in `json` parser.
- Add support for collecting SQL Requests to identify waits and blocking to `sqlserver` input.
- Collect k8s endpoints, ingress, and services in `kube_inventory` plugin.
- Add support for field/tag keys to `strings` processor.
- Add certificate verification status to `x509_cert` input.
- Support percentage value parsing in `redis` input.
- Load external Go plugins from `--plugin-directory`.
- Add ability to exclude db/bucket tag from `influxdb` outputs.
- Gather per collections stats in `mongodb` input plugin.
- Add TLS & credentials configuration for `nats_consumer` input plugin.
- Add support for enterprise repos to `github` plugin.
- Add Indices stats to `elasticsearch` input.
- Add left function to `string` processor.
- Add grace period for metrics late for aggregation.
- Add `diff` and `non_negative_diff` to `basicstats` aggregator.
- Add device tags to `smart_attributes`.
- Collect `framework_offers` and `allocator` metrics in `mesos` input.
- Add Telegraf and Go version to the `internal` input plugin.
- Update the number of logical CPUs dynamically in `system` plugin.
- Add darwin (macOS) builds to the release.
- Add configurable timeout setting to `smart` input.
- Add `memory_usage` field to `procstat` input plugin.
- Add support for custom attributes to `vsphere` input.
- Add `cmdstat` metrics to `redis` input.
- Add `content_length` metric to `http_response` input plugin.
- Add `database_tag` option to `influxdb_listener` to add database from query string.
- Add capability to limit TLS versions and cipher suites.
- Add `topic_tag` option to `mqtt_consumer`.
- Add ability to label inputs for logging.
- Add TLS support to `nginx_plus`, `nginx_plus_api` and `nginx_vts`.

### Bug fixes

- Fix sensor read error stops reporting of all sensors in `temp` input.
- Fix double pct replacement in `sysstat` input.
- Fix race in master node detection in `elasticsearch` input.
- Fix SSPI authentication not working in `sqlserver` input.
- Fix memory error panic in `mqtt` input.
- Support Kafka 2.3.0 consumer groups.
- Fix persistent session in `mqtt_consumer`.
- Fix finder inconsistencies in `vsphere` input.
- Fix parsing multiple metrics on the first line of tailed file.
- Send TERM to `exec` processes before sending KILL signal.
- Query oplog only when connected to a replica set.
- Use environment variables to locate Program Files on Windows.

## v1.11.5

### Bug fixes

- Update `go-sql-driver/mysql` driver to 1.4.1 to address auth issues.
- Return error status from `--test` if input plugins produce an error.
- Fix with multiple instances only last configuration is used in smart input.
- Build official packages with Go 1.12.9.
- Split out `-w` argument in `iptables` input plugin.
- Add support for parked process state on Linux.
- Remove leading slash from rcon command.
- Allow jobs with dashes in the name in `lustre2` input plugin.

## v1.11.4

### Bug fixes

#### Plugins

- Kubernetes input (`kubernetes`)
    - Correct typo in `logsfs_available_bytes` field.
- Datadog output (`datadog`)
    - Skip floats that are `NaN` or `Inf`.
- Socket Listener input (`socket_listener`)
    - Fix reload panic.

## v1.11.3

### Bug fixes

#### Agent

- Treat empty array as successful parse in JSON parser.
- Fix template pattern partial wildcard matching.

#### Plugins

- Bind input (`bind`)
    - Add missing `rcode` and `zonestat`.
- GitHub input
    - Fix panic.
- Lustre2 input (`lustre2`)
    - Fix config parse regression.
- NVIDIA-SMI output (`nvidia-smi`)
    - Handle unknown error.
- StatD input (`statd`)
    - Fix panic when processing Datadog events.
- VMware vSphere input (`vsphere`)
    - Fix unable to reconnect after vCenter reboot.

## v1.11.2

### Bug fixes

#### Plugins

- Bind input (`bind`)
    - Fix `value out of range` error on 32-bit systems.
- Burrow input (`burrow`)
    - Apply topic filter to partition metrics.
- Filecount input (`filecount`)
    - Fix path separator handling in Windows.
- Logparser input (`logparser`)
    - Fix stop working after reload.
- Ping input (`ping`)
    - Fix source address ping flag on BSD.
- StatsD input (`statsd`)
    - Fix panic with empty Datadog tag string.
- Tail input (`tail`)
    - Fix stop working after reload.

## v1.11.1

### Bug fixes

#### Agent

- Fix panic if `pool_mode` column does not exist.
- Add missing `container_id` field to `docker_container_status` metrics.
- Add `device`, `serial_no`, and `wwn` tags to synthetic attributes.

#### Plugins

- Cisco GNMI Telemetry input (`cisco_telemetry_gnmi`)
    - Omit keys when creating measurement names for GNMI telemetry.
- Disk input (`disk`)
    - Cannot set `mount_points` option.
- NGINX Plus API input (`nginx_plus_api`)
    - Skip 404 error reporting.
- Procstat input (`procstat`)
    - Don’t consider `pid` of `0` when using systemd lookup.
- StatsD input (`statsd`)
    - Fix parsing of remote TCP address.
- System input (`system`)
    - Ignore error when `utmp` is missing.

## v1.11.0

- System (`system`) input plugin
    - The `uptime_format` field has been deprecated — use the `uptime` field instead.
- Amazon Cloudwatch Statistics (`cloudwatch`) input plugin
    - Updated to use a more efficient API and now requires `GetMetricData` permissions instead of `GetMetricStatistics`. The `units` tag is not available from this API and is no longer collected.

### New input plugins

- [BIND 9 Nameserver Statistics (`bind`)](https://github.com/influxdata/telegraf/blob/release-1.11/plugins/inputs/bind/README.md) - Contributed by @dswarbrick & @danielllek
- [Cisco GNMI Telemetry (`cisco_telemetry_gnmi`)](https://github.com/influxdata/telegraf/blob/release-1.11/plugins/inputs/cisco_telemetry_gnmi/README.md) - Contributed by @sbyx
- [Cisco Model-driven Telemetry (`cisco_telemetry_mdt`)](https://github.com/influxdata/telegraf/blob/release-1.11/plugins/inputs/cisco_telemetry_mdt/README.md) - Contributed by @sbyx
- [ECS (`ecs`)](https://github.com/influxdata/telegraf/blob/release-1.11/plugins/inputs/ecs/README.md) - Contributed by @rbtr
- [GitHub (`github`)](https://github.com/influxdata/telegraf/blob/release-1.11/plugins/inputs/github/README.md) - Contributed by @influxdata
- [OpenWeatherMap (`openweathermap`)](https://github.com/influxdata/telegraf/blob/release-1.11/plugins/inputs/openweathermap/README.md) - Contributed by @regel
- [PowerDNS Recursor (`powerdns_recursor`)](https://github.com/influxdata/telegraf/blob/release-1.11/plugins/inputs/powerdns_recursor/README.md) - Contributed by @dupondje

### New aggregator plugins

- [Final (`final`)](https://github.com/influxdata/telegraf/blob/release-1.11/plugins/aggregators/final/README.md) - Contributed by @oplehto

### New output plugins

- [Syslog (`syslog`)](https://github.com/influxdata/telegraf/blob/release-1.11/plugins/outputs/syslog/README.md) - Contributed by @javicrespo
- [Health (`health`)](https://github.com/influxdata/telegraf/blob/release-1.11/plugins/outputs/health/README.md) - Contributed by @influxdata

### New output data formats (serializers)

- [wavefront](https://github.com/influxdata/telegraf/blob/release-1.11/plugins/serializers/wavefront/README.md) - Contributed by @puckpuck

### Features

#### Agent

- Add CLI support for outputting sections of the configuration.
- Add `service-display-name` option for use with Windows service.
- Add support for log rotation.
- Allow env vars `${}` expansion syntax in configuration file.
- Allow devices option to match against devlinks.

### Input data formats

- Nagios
    - Add support for multiple line text and perfdata.

#### Input plugins

- AMQP Consumer (`amqp_consumer`)
    - Support passive queue declaration.
    - Add support for gzip compression.
- Amazon Cloudwatch Statistics (`cloudwatch`)
    - Use more efficient GetMetricData API to collect Cloudwatch metrics.
    - Allow selection of collected statistic types in cloudwatch input.
- Apache Solr (`solr`)
    - Add support for HTTP basic auth.
- Hddtemp (`hddtemp`)
    - Add source tag.
- InfluxDB Listener (`influxdb_listener`)
    - Support verbose query parameter in ping endpoint.
- NVIDIA SMI (`nvidia-smi`)
    - Extend metrics collected from Nvidia GPUs.
- Net (`net`)
    - Speed up interface stat collection.
- PHP FM (`phpfm`)
    - Enhance HTTP connection options.
- Ping (`ping`)
    - Add TTL field.
- Procstat (`procstat`)
    - Add `cmdline` tag.
    - Add pagefault data.
- Prometheus (`prometheus`)
    - Add namespace restriction.
- SMART (`smart`)
    - Support more drive types.
- Socket Listener (`socket_listener`)
    - Add option to set permissions for UNIX domain sockets.
- StatsD (`statsd`)
    - Add support for Datadog events.

### Output plugins

- AMQP (`amqp`)
    - Add support for gzip compression.
- File (`file`)
    - Add file rotation support.
- Stackdriver (`stackdriver`)
    - Set user agent. – VMware Wavefront (`wavefront`)
    - Add option to use strict sanitization rules.

### Aggregator plugins

- Histogram aggregator
    - Add option to reset buckets on flush.

#### Processor plugins

- Converter (`converter`)
    - Add hexadecimal string to integer conversion.
- Enum (`enum`)
    - Support tags.

### Bug fixes

#### Agent

- Create Windows service only when specified or in service manager.
- Don’t start Telegraf when stale pid file found.
- Fix inline table support in configuration file.
- Fix multi-line basic strings support in configuration file.
- Fix multiple SIGHUP causes Telegraf to shutdown.
- Fix batch fails when single metric is unserializable.
- Log a warning on write if the metric buffer has overflowed.

#### Plugins

- AMQP (`amqp`) output
    - Fix direct exchange routing key.
- Apex Neptune (`apex_neptune`) inpur
    - Skip invalid power times.
- Docker (`docker`) input
    - Fix docker input does not parse image name correctly.
- Fibaro (`fibaro`) input
    - Set default timeout of `5s`.
- InfluxDB v1.x (`influxdb`) output
    - Fix connection leak on reload.
- InfluxDB v2 output
    - Fix connection leak on reload.
- Lustre 2 (`lustre2`) input
    - Fix only one job per storage target reported.
- Microsoft Azure Monitor (`azure_monitor`) output
    - Fix scale set resource id.
- Microsoft SQL Server (`sqlserver`) input Fix connection closing on error.
- Minecraft (`minecraft`) input
    - Support Minecraft server 1.13 and newer.
- NGINX Upstream Check (`nginx_upstream_check`) input
    - Fix TOML option name.
- PgBounder (`pgbouncer`) input
    - Fix unsupported pkt type error.
- Procstat (`procstat`) input
    - Verify a process passed by `pid_file` exists.
- VMware vSphere (`vsphere`) input
    - Fixed datastore name mapping.

## v1.10.4

### Bug fixes

#### Agent

- Create telegraf user in pre-install RPM scriptlet.
- Fix parse of unix timestamp with more than ns precision.
- Fix race condition in the Wavefront parser.

#### Plugins

- HTTP output plugin (`http`)
    - Fix http output cannot set Host header.
- IPMI Sensor input (`ipmi_sensor`)
    - Add support for hex values.
- InfluxDB v2 output (`influxdb_v2`)
    - Don’t discard metrics on forbidden error.
- Interrupts input (`interrupts`)
    - Restore field name case.
- NTPQ input (`ntpq`)
    - Skip lines with missing `refid`.
- VMware vSphere input (`vsphere`)
    - Fix interval estimation.

## v1.10.3

### Bug fixes

#### Agent

- Set log directory attributes in RPM specification.

#### Plugins

- Prometheus Client (`prometheus_client`) output plugin.
    - Allow colons in metric names.

## v1.10.2

### Breaking changes

Grok input data format (parser): string fields no longer have leading and trailing quotation marks removed. If you are capturing quoted strings, the patterns might need to be updated.

### Bug fixes

#### Agent

- Fix deadlock when Telegraf is aligning aggregators.
- Add owned directories to RPM package specification.
- Fix drop tracking of metrics removed with aggregator `drop_original`.
- Fix aggregator window alignment.
- Fix panic during shutdown of multiple aggregators.
- Fix tags applied to wrong metric on parse error.

#### Plugins

- Ceph (`ceph`) input
    - Fix missing cluster stats.
- DiskIO (`diskio`) input
    - Fix reading major and minor block devices identifiers.
- File (`file`) output
    - Fix open file error handling.
- Filecount (`filecount`) input
    - Fix basedir check and parent dir extraction.
- Grok (`grok`) parser
    - Fix last character removed from string field.
- InfluxDB v2 (`influxdb_v2`) output
    - Fix plugin name in output logging.
- Prometheus (`prometheus`) input
    - Fix parsing of kube config `certificate-authority-data`.
- Prometheus (`prometheus`) output
    - Remove tags that would create invalid label names.
- StatsD (`statsd`) input
    - Listen before leaving start.

## v1.10.1

#### Bug fixes

- Show error when TLS configuration cannot be loaded.
- Add base64-encoding/decoding for Google Cloud PubSub (`pubsub`) plugins.
- Fix type compatibility in VMware vSphere (`vsphere`) input plugin with `use_int_samples` option.
- Fix VMware vSphere (`vsphere`) input plugin shows failed task in vCenter.
- Fix invalid measurement name and skip column in the CSV input data format parser.
- Fix System (`system`) input plugin causing high CPU usage on Raspbian.

## v1.10

#### New input plugins

- [Google Cloud PubSub (`cloud_pubsub`)](https://github.com/influxdata/telegraf/blob/release-1.10/plugins/inputs/cloud_pubsub/README.md) - Contributed by @emilymye
- [Kubernetes Inventory (`kube_inventory`)](https://github.com/influxdata/telegraf/blob/release-1.10/plugins/inputs/cloud_pubsub_push/README.md) - Contributed by @influxdata
- [Neptune Apex (`neptune_apex`)](https://github.com/influxdata/telegraf/blob/release-1.10/plugins/inputs/neptune_apex/README.md) - Contributed by @MaxRenaud
- [NGINX Upstream Check (`nginx_upstream_check`)](https://github.com/influxdata/telegraf/blob/release-1.10/plugins/inputs/nginx_upstream_check/README.md) - Contributed by @dmitryilyin
- [Multifile (`multifile`)](https://github.com/influxdata/telegraf/blob/release-1.10/plugins/inputs/multifile/README.md) - Contributed by @martin2250

#### New output plugins

- [Google Cloud PubSub (`cloud_pubsub`)](https://github.com/influxdata/telegraf/blob/release-1.10/plugins/outputs/cloud_pubsub/README.md) - Contributed by @emilymye

#### New output data formats (serializers)

- [ServiceNow Metrics](/telegraf/v1/data_formats/output/nowmetric) - Contributed by @JefMuller
- [Carbon2](/telegraf/v1/data_formats/output/carbon2) - Contributed by @frankreno

#### Features

- **General**
    - Allow for force gathering ES cluster stats.
    - Add Linux `mipsle` packages.
- **Input plugins**
    - Ceph (`ceph`)
        - Add read and write op per second fields.
    - CouchDB (`couchdb`)
        - Add support for basic auth.
    - DNS Query (`dns_query`)
        - Add `rcode` tag and field.
    - DiskIO (`diskio`)
        - Include `DEVLINKS` in available `udev` properties.
    - HTTP (`http`)
        - Add support for sending a request body to `http` input.
    - InfluxDB Listener (`influxdb_listener`)
        - Add internal metric for line too long.
    - Interrupts (`interrupts`)
        - Add option to store `cpu` as a tag.
    - Kafka Consumer (`kafka_consumer`)
        - Add ability to tag metrics with topic.
    - Kubernetes (`k8s`)
    - Support passing bearer token directly.
    - Microsoft SQL Server (`sqlserver`)
        - Add log send and redo queue fields.
    - MongoDB (`mongodb`)
        - Add `flush_total_time_ns` and additional wired tiger fields.
    - Procstat (`procstat_lookup`)
        - Add running field.
    - Prometheus (`prometheus`)
        - Support passing bearer token directly.
        - Add option to report input timestamp.
    - VMware vSphere (`vsphere`)
        - Improve scalability.
        - Add resource path-based filtering.
    - Varnish (`varnish`)
        - Add configurable timeout.
- **Output plugins**
    - MQTT (`mqtt`)
        - Add option to set retain flag on messages.
    - Stackdriver (`stackdriver`)
        - Add resource type and resource label support
    - VMware Wavefront (`wavefront`)
        - Add support for the Wavefront Direct Ingestion API.
- **Aggregator plugins**
    - Value Counter (`valuecounter`)
        - Allow counting float values.
- **Data formats**
    - **Input data formats**
    - CSV
        - Support `unix_us` and `unix_ns` timestamp format.
        - Add support for `unix` and `unix_ms` timestamps.
    - Grok (`grok`)
        - Allow parser to produce metrics with no fields.
    - JSON
        - Add micro and nanosecond unix timestamp support.
    - **Output data formats**
        - ServiceNow Metrics

#### Bug fixes

- **General**
    - Use `systemd` in Amazon Linux 2 rpm.
    - Fix `initscript` removes `pidfile` of restarted Telegraf process.
- **Input plugins**
    - Consul (`consul`)
        - Use datacenter option spelling.
    - InfluxDB Listener (`influxdb_listener`)
        - Remove auth from `/ping` route.
    - Microsoft SQL Server (`sqlserver`)
        - Set deadlock priority.
    - Nstat (`nstat`)
        - Remove error log when `snmp6` directory does not exist.
    - Ping (`ping`)
        - Host not added when using custom arguments.
    - X.509 Certificate
        - Fix input stops checking certificates after first error.
- **Output plugins**
    - Prometheus (`prometheus`)
        - Sort metrics by timestamp.
    - Stackdriver (`stackdriver`)
        - Skip string fields when writing.
        - Send metrics in ascending time order.

## v1.9.5

### Bug fixes

- General
    - Use `systemd` in Amazon Linux 2 rpm.
- Ceph Storage (`ceph`) input plugin
    - Add backwards compatibility fields in usage and pool statistics.
- InfluxDB (`influxdb`) output plugin
    - Fix UDP line splitting.
- Microsoft SQL Server (`sqlserver`) input plugin
    - Set deadlock priority to low.
    - Disable results by row in AzureDB query.
- Nstat (`nstat`) input plugin
    - Remove error log when `snmp6` directory does not exist.
- Ping (`ping`) input plugin
    - Host not added when using custom arguments.
- Stackdriver (`stackdriver`) output plugin
    - Skip string fields when writing to stackdriver output.
    - Send metrics in ascending time order.

## v1.9.4

### Bug fixes

- General
    - Fix `skip_rows` and `skip_columns` options in csv parser.
    - Build official packages with Go 1.11.5.
- Jenkins input plugin
    - Always send basic auth in jenkins input.
- Syslog (`syslog`) input plugin
    - Fix definition of multiple syslog plugins.

## v1.9.3

#### Bug fixes

- General
    - Fix latest metrics not sent first when output fails.
    - Fix `internal_write buffer_size` not reset on timed writes.
- AMQP Consumer (`amqp_consumer`) input plugin
    - Fix `amqp_consumer` input stops consuming when it receives unparsable messages.
- Couchbase (`couchbase`) input plugin
    - Remove `userinfo` from cluster tag in `couchbase` input.
- Microsoft SQL Server (`sqlserver`) input plugin
    - Fix arithmetic overflow in `sqlserver`) input.
- Prometheus (`prometheus`) input plugin
    - Fix `prometheus` input not detecting added and removed pods.

## v1.9.2

### Bug fixes

- Increase `varnishstat` timeout.
- Remove storage calculation for non-Azure-managed instances and add server version.
- Fix error sending empty tag value in `azure_monitor` output.
- Fix panic with Prometheus input plugin on shutdown.
- Support non-transparent framing of syslog messages.
- Apply global- and plugin-level metric modifications before filtering.
- Fix `num_remapped_pgs` field in `ceph` plugin.
- Add `PDH_NO_DATA` to known counter error codes in `win_perf_counters`.
- Fix `amqp_consumer` stops consuming on empty message.
- Fix multiple replace tables not working in strings processor.
- Allow non-local UDP connections in `net_response`.
- Fix TOML option names in parser processor.
- Fix panic in Docker input with bad endpoint.
- Fix original metric modified by aggregator filters.

## v1.9.1

### Bug fixes

- Fix boolean handling in splunkmetric serializer.
- Set default config values in Jenkins input.
- Fix server connection and document stats in MongoDB input.
- Add X-Requested-By header to Graylog input.
- Fix metric memory not freed from the metric buffer on write.
- Add support for client TLS certificates in PostgreSQL inputs.
- Prevent panic when marking the offset in `kafka_consumer`.
- Add early metrics to aggregator and honor `drop_original` setting.
- Use `-W` flag on BSD variants in ping input.
- Allow delta metrics in Wavefront parser.

## v1.9.0

#### Release Notes

- The HTTP Listener (`http_listener`) input plugin has been renamed to InfluxDB Listener (`influxdb_listener`) input plugin and use of the original name is deprecated. The new name better describes the intended use of the plugin as an InfluxDB relay. For general purpose transfer of metrics in any format using HTTP, InfluxData recommends using HTTP Listener v2 (`http_listener_v2`) input plugin.

- Input plugins are no longer limited from adding metrics when the output is writing and new metrics will move into the metric buffer as needed. This will provide more robust degradation and recovery when writing to a slow output at high throughput.

    To avoid overconsumption when reading from queue consumers, the following input plugins use the new option `max_undelivered_messages` to limit the number of outstanding unwritten metrics:

    - Apache Kafka Consumer (`kafka_consumer`)
    - AMQP Consumer (`amqp_consumer`)
    - MQTT Consumer (`mqtt_consumer`)
    - NATS Consumer (`nats_consumer`)
    - NSQ Consumer (`nsq_consumer`)

#### New input plugins

- [HTTP Listener v2 (`http_listener_v2`)](https://github.com/influxdata/telegraf/blob/release-1.9/plugins/inputs/http_listener_v2/README.md) - Contributed by @jul1u5
- [IPVS (`ipvs`)](https://github.com/influxdata/telegraf/blob/release-1.9/plugins/inputs/ipvs/README.md) - Contributed by @amoghe
- [Jenkins (`jenkins`)](https://github.com/influxdata/telegraf/blob/release-1.9/plugins/inputs/jenkins/README.md) - Contributed by @influxdata & @lpic10
- [NGINX Plus API (`nginx_plus_api`)](https://github.com/influxdata/telegraf/blob/release-1.9/plugins/inputs/nginx_plus_api/README.md) - Contributed by @Bugagazavr
- [NGINX VTS (`nginx_vts`)](https://github.com/influxdata/telegraf/blob/release-1.9/plugins/inputs/nginx_vts/README.md) - Contributed by @monder
- [Wireless (`wireless`)](https://github.com/influxdata/telegraf/blob/release-1.9/plugins/inputs/wireless/README.md) - Contributed by @jamesmaidment

#### New output plugins

- [Stackdriver (stackdriver)](https://github.com/influxdata/telegraf/blob/release-1.9/plugins/outputs/stackdriver/README.md) - Contributed by @jamesmaidment

#### Features

- General
    - Add ability to define a custom service name when installing as a Windows service.
    - Add new configuration for CSV column explicit type conversion.
    - Add Telegraf version to `User-Agent` header.
    - Add ability to specify bytes options as strings with units.
    - Add per output `flush_interval`, `metric_buffer_limit`, and `metric_batch_size`.
- Amazon Kinesis (`kinesis`) output plugin
    - Use `DescribeStreamSummary` in place of `ListStreams`.
- DNS Query (`dns_query`) input plugin
    - Query servers in parallel.
- Datadog (`datadog`) output plugin
    - Add an option to specify a custom URL.
    - Use non-allocating field and tag accessors.
- Filecount (`filecount`) input plugin
    - Add per-directory file count.
- HTTP Output (`http output`) plugin
    - Add entity-body compression.
- Memcached (`memcached`) input plugin
    - Collect additional statistics.
- NSQ (`nsq`) input plugin
    - Add TLS configuration support.
- Ping (`ping`) input plugin
    - Add support for IPv6.
- Procstat (`procstat`) input plugin
    - Add Windows service name lookup.
- Prometheus (`prometheus`) input plugin
    - Add scraping for Prometheus annotation in Kubernetes.
    - Allow connecting to Prometheus using UNIX socket.
- Strings (`strings`) processor plugin
    - Add `replace` function.
- VMware vSphere (`vsphere`) input plugin
    - Add LUN to data source translation.

#### Bug fixes

- Remove `time_key` from the field values in JSON parser.
- Fix input time rounding when using a custom interval.
- Fix potential deadlock or leaked resources on restart or reload.
- Fix outputs block inputs when batch size is reached.
- Fix potential missing datastore metrics in VMware vSphere (`vsphere`) input plugin.

## v1.8.3

### Bug fixes

- Add DN attributes as tags in X.509 Certificate (`x509_cert`) input plugin to avoid series overwrite.
- Prevent connection leak by closing unused connections in AMQP (`amqp`) output plugin.
- Use default partition key when tag does not exist in Amazon Kinesis (`kinesis`) output plugin.
- Log the correct error in JTI OpenConfig Telemetry (`jti_openconfig_telemetry`) input plugin.
- Handle panic when IMPI Sensor (`ipmi_sensor`) input plugin gets bad input.
- Don’t add unserializable fields to Jolokia2 (`jolokia2`) input plugin.
- Fix version check in PostgreSQL Exstensible (`postgresql_extensible`) plugin.

## v1.8.2

### Bug fixes

- Aerospike (`aerospike`) input plugin
    - Support uint fields.
- Docker (`docker`) input plugin
    - Use container name from list if no name in container stats.
- Filecount (`filecount`) input plugin
    - Prevent panic on error in file stat.
- InfluxDB v2 (`influxdb_v2`) input plugin
    - Update write path to match updated v2 API.
- Logparser (`logparser`) input plugin
    - Fix panic.
- MongoDB (`mongodb`) input plugin
    - Lower authorization errors to debug level.
- MQTT Consumer (`mqtt_consumer`) input plugin
    - Fix connect and reconnect.
- Ping (`ping`) input plugin
    - Return correct response code.
- VMware vSphere (`vsphere`) input plugin
    - Fix missing timeouts.
- X.509 Certificate (`x509_cert`) input plugin
    - Fix segfault.

## v1.8.1

### Bug fixes

- Fix `hardware_type` may be truncated in Microsoft SQL Server (`sqlserver`) input plugin.
- Improve performance in Basicstats (`basicstats`) aggregator plugin.
- Add `hostname` to TLS config for SNI support in X.509 Certificate (`x509_cert`) input plugin.
- Don’t add tags with empty values to OpenTSDB (`opentsdb`) output plugin.
- Fix panic during network error in VMware vSphere (`vsphere`) input plugin.
- Unify error response in HTTP Listener (`http_listener`) input plugin with InfluxDB (`influxdb`) output plugin.
- Add `UUID` to VMs in VMware vSphere (`vsphere`) input plugin.
- Skip tags with empty values in Amazon Cloudwatch (`cloudwatch`) output plugin.
- Fix missing non-realtime samples in VMware vSphere (`vsphere`) input plugin.
- Fix case of `timezone`/`grok_timezone` options in grok parser and logparser input plugin.

## v1.8

### New input plugins

- [ActiveMQ (`activemq`)](https://github.com/influxdata/telegraf/blob/release-1.8/plugins/inputs/activemq/README.md) - Contributed by @mlabouardy
- [Beanstalkd (`beanstalkd`)](https://github.com/influxdata/telegraf/blob/release-1.8/plugins/inputs/beanstalkd/README.md) - Contributed by @44px
- [File (`file`)](https://github.com/influxdata/telegraf/blob/release-1.8/plugins/inputs/file/README.md) - Contributed by @maxunt
- [Filecount (`filecount`)](https://github.com/influxdata/telegraf/blob/release-1.8/plugins/inputs/filecount/README.md) - Contributed by @sometimesfood
- [Icinga2 (`icinga2`)](https://github.com/influxdata/telegraf/blob/release-1.8/plugins/inputs/icinga2/README.md) - Contributed by @mlabouardy
- [Kibana (`kibana`)](https://github.com/influxdata/telegraf/blob/release-1.8/plugins/inputs/kibana/README.md) - Contributed by @lpic10
- [PgBouncer (`pgbouncer`)](https://github.com/influxdata/telegraf/blob/release-1.8/plugins/inputs/pgbouncer/README.md) - Contributed by @nerzhul
- [Temp (`temp`)](https://github.com/influxdata/telegraf/blob/release-1.8/plugins/inputs/temp/README.md) - Contributed by @pytimer
- [Tengine (`tengine`)](https://github.com/influxdata/telegraf/blob/release-1.8/plugins/inputs/tengine/README.md) - Contributed by @ertaoxu
- [VMware vSphere (`vsphere`)](https://github.com/influxdata/telegraf/blob/release-1.8/plugins/inputs/vsphere/README.md) - Contributed by @prydin
- [X.509 Certificate (`x509_cert`)](https://github.com/influxdata/telegraf/blob/release-1.8/plugins/inputs/x509_cert/README.md) - Contributed by @jtyr

### New processor plugins

- [Enum (`enum`)](https://github.com/influxdata/telegraf/blob/release-1.8/plugins/processors/enum/README.md) - Contributed by @KarstenSchnitter
- [Parser (`parser`)](https://github.com/influxdata/telegraf/blob/release-1.8/plugins/processors/parser/README.md) - Contributed by @Ayrdrie & @maxunt
- [Rename (`rename`)](https://github.com/influxdata/telegraf/blob/release-1.8/plugins/processors/rename/README.md) - Contributed by @goldibex
- [Strings (`strings`)](https://github.com/influxdata/telegraf/blob/release-1.8/plugins/processors/strings/README.md) - Contributed by @bsmaldon

### New aggregator plugins

- [ValueCounter (`valuecounter`)](https://github.com/influxdata/telegraf/blob/release-1.8/plugins/aggregators/valuecounter/README.md) - Contributed by @piotr1212

### New output plugins

- [Azure Monitor (`azure_monitor`)](https://github.com/influxdata/telegraf/blob/release-1.8/plugins/outputs/azure_monitor/README.md) - Contributed by @influxdata
- [InfluxDB v2 (`influxdb_v2`)](https://github.com/influxdata/telegraf/blob/release-1.8/plugins/outputs/influxdb_v2/README.md) - Contributed by @influxdata

### New input data formats (parsers)

- [csv](https://docs.influxdata.com/telegraf/v1/data_formats/input/csv/) - Contributed by @maxunt
- [grok](https://docs.influxdata.com/telegraf/v1/data_formats/input/grok/) - Contributed by @maxunt
- [logfmt](https://docs.influxdata.com/telegraf/v1/data_formats/input/logfmt/) - Contributed by @Ayrdrie & @maxunt
- [wavefront](https://docs.influxdata.com/telegraf/v1/data_formats/input/wavefront/) - Contributed by @puckpuck

### New output data formats (serializers)

- [splunkmetric](https://docs.influxdata.com/telegraf/v1/data_formats/output/splunkmetric/) - Contributed by @ronnocol

### Features

- Add SSL/TLS support to Redis (`redis`) input plugin.
- Add tengine input plugin.
- Add power draw field to the NVIDIA SMI (`nvidia_smi`) input plugin.
- Add support for Solr 7 to the Solr (`solr`) input plugin.
- Add owner tag on partitions in Burrow (`burrow`) input plugin.
- Add container status tag to Docker (`docker`) input plugin.
- Add ValueCounter (`valuecounter`) aggregator plugin.
- Add new measurement with results of `pgrep` lookup to Procstat (`procstat`) input plugin.
- Add support for comma in logparser timestamp format.
- Add path tag to Tail (`tail`) input plugin.
- Add log message when tail is added or removed from a file.
- Add option to use of counter time in win perf counters.
- Add energy and power field and device id tag to Fibaro (`fibaro`) input plugin.
- Add HTTP path configuration for OpenTSDB output.
- Gather IPMI metrics concurrently.
- Add mongo document and connection metrics.
- Add enum processor plugin.
- Add user tag to procstat input.
- Add support for multivalue metrics to collectd parser.
- Add support for setting kafka client id.
- Add file input plugin and grok parser.
- Improve cloudwatch output performance.
- Add x509\_cert input plugin.
- Add IPSIpAddress syntax to ipaddr conversion in snmp plugin.
- Add Filecount filecount input plugin.
- Add support for configuring an AWS `endpoint_url`.
- Send all messages before waiting for results in Kafka output plugin.
- Add support for lz4 compression to Kafka output plugin.
- Split multiple sensor keys in ipmi input.
- Support StatisticValues in cloudwatch output plugin.
- Add ip restriction for the prometheus\_client output.
- Add PgBouncer (`pgbouncer`) input plugin.
- Add ActiveMQ input plugin.
- Add wavefront parser plugin.
- Add rename processor plugin.
- Add message ‘max\_bytes’ configuration to kafka input.
- Add gopsutil meminfo fields to Mem (`mem`) input plugin.
- Document how to parse Telegraf logs.
- Use dep v0.5.0.
- Add ability to set measurement from matched text in grok parser.
- Drop message batches in Kafka (`kafka`) output plugin if too large.
- Add support for static and random routing keys in Kafka (`kafka`) output plugin.
- Add logfmt parser plugin.
- Add parser processor plugin.
- Add Icinga2 input plugin.
- Add name, time, path and string field options to JSON parser.
- Add forwarded records to sqlserver input.
- Add Kibana input plugin.
- Add csv parser plugin.
- Add read\_buffer\_size option to statsd input.
- Add azure\_monitor output plugin.
- Add queue\_durability parameter to amqp\_consumer input.
- Add strings processor.
- Add OAuth 2.0 support to HTTP output plugin.
- Add Unix epoch timestamp support for JSON parser.
- Add options for basic auth to haproxy input.
- Add temp input plugin.
- Add Beanstalkd input plugin.
- Add means to specify server password for redis input.
- Add Splunk Metrics serializer.
- Add input plugin for VMware vSphere.
- Align metrics window to interval in cloudwatch input.
- Improve Azure Managed Instance support + more in sqlserver input.
- Allow alternate binaries for iptables input plugin.
- Add influxdb\_v2 output plugin.

### Bug fixes

- Fix divide by zero in logparser input.
- Fix instance and object name in performance counters with backslashes.
- Reset/flush saved contents from bad metric.
- Document all supported cli arguments.
- Log access denied opening a service at debug level in win\_services.
- Add support for Kafka 2.0.
- Fix nagios parser does not support ranges in performance data.
- Fix nagios parser does not strip quotes from performance data.
- Fix null value crash in postgresql\_extensible input.
- Remove the startup authentication check from the cloudwatch output.
- Support tailing files created after startup in tail input.
- Fix CSV format configuration loading.

## v1.7.4

### Bug fixes

- Continue sending write batch in UDP if a metric is unserializable in InfluxDB (`influxdb`) output plugin.
- Fix PowerDNS (`powerdns`) input plugin tests.
- Fix `burrow_group` offset calculation for Burrow (`burrow`) input plugin.
- Add `result_code` value for errors running ping command.
- Remove timeout deadline for UDP in Syslog (`syslog`) input plugin.
- Ensure channel is closed if an error occurs in CGroup (`cgroup`) input plugin.
- Fix sending of basic authentication credentials in HTTP `(output)` output plugin.
- Use the correct `GOARM` value in the Linux armel package.

## v1.7.3

### Bug fixes

- Reduce required Docker API version.
- Keep leading whitespace for messages in syslog input.
- Skip bad entries on interrupt input.
- Preserve metric type when using filters in output plugins.
- Fix error message if URL is unparseable in InfluxDB output.
- Use explicit `zpool` properties to fix parse error on FreeBSD 11.2.
- Lock buffer when adding metrics.

## v1.7.2

### Bug fixes

- Use localhost as default server tag in Zookeeper (`zookeeper`) input plugin.
- Don’t set values when pattern doesn’t match in Regex (`regex`) processor plugin.
- Fix output format of Printer (`printer`) processor plugin.
- Fix metric can have duplicate field.
- Return error if NewRequest fails in HTTP (`http`) output plugin.
- Reset read deadline for Syslog (`syslog`) input plugin.
- Exclude cached memory on Docker (`docker`) input plugin.

## v1.7.1

### Bug fixes

- Treat `sigterm` as a clean shutdown signal.
- Fix selection of tags under nested objects in the JSON parser.
- Fix Postfix (`postfix`) input plugin handling of multilevel queues.
- Fix Syslog (`syslog` input plugin timestamp parsing with single digit day of month.
- Handle MySQL (`mysql`) input plugin variations in the `user_statistics` collecting.
- Fix Minmax (`minmax`) and Basicstats (`basicstats`) aggregator plugins to use `uint64`.
- Document Swap (`swap`) input plugin.
- Fix incorrect precision being applied to metric in HTTP Listener (`http_listener`) input plugin.

## v1.7

### Release notes

- The Cassandra (`cassandra`) input plugin has been deprecated in favor of the Jolokia2 (`jolokia2`) input plugin which is much more configurable and more performant. There is an [example configuration](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/jolokia2/examples) to help you get started.

- For plugins supporting TLS, you can now specify the certificate and keys using `tls_ca`, `tls_cert`, `tls_key`. These options behave the same as the, now deprecated, `ssl` forms.

### New input plugins

- [Aurora (`aurora`)](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/aurora/README.md) - Contributed by @influxdata
- [Burrow (`burrow`) input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/burrow/README.md) - Contributed by @arkady-emelyanov
- [`fibaro`](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/fibaro/README.md) - Contributed by @dynek
- [`jti_openconfig_telemetry`](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/jti_openconfig_telemetry/README.md) - Contributed by @ajhai
- [`mcrouter`](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/mcrouter/README.md) - Contributed by @cthayer
- [NVIDIA SMI (`nvidia_smi`)](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/nvidia_smi/README.md) - Contributed by @jackzampolin
- [Syslog (`syslog`)](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/syslog/README.md) - Contributed by @influxdata

### New processor plugins

- [converter](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/processors/converter/README.md) - Contributed by @influxdata
- [regex](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/processors/regex/README.md) - Contributed by @44px
- [topk](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/processors/topk/README.md) - Contributed by @mirath

### New output plugins

- [HTTP (`http`)](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/outputs/http/README.md) - Contributed by @Dark0096
- [Application Insights (`application_insights`) output plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/outputs/application_insights/README.md): Contribute by @karolz-ms

### Features

- Add `repl_oplog_window_sec` metric to MongoDB (`mongodb`) input plugin.
- Add per-host shard metrics in MongoDB (`mongodb`) input plugin.
- Skip files with leading `..` in config directory.
- Add TLS support to `socket_writer` and `socket_listener` plugins.
- Add `snmp` input option to strip non-fixed length index suffixes.
- Add server version tag to the Docker (`docker`) input plugin.
- Add support for LeoFS 1.4 to `leofs` input.
- Add parameter to force the interval of gather for Sysstat (`sysstat`).
- Support BusyBox ping in the Ping (`ping`) input plugin.
- Add Mcrouter (`mcrouter`) input plugin.
- Add TopK (`topk`) processor plugin.
- Add cursor metrics to MongoDB (`mongodb`) input plugin.
- Add tag/integer pair for result to Network Response (`net_response`) input plugin.
- Add Application Insights (`application_insights`) output plugin.
- Added several important Elasticsearch cluster health metrics.
- Add batch mode to `mqtt` output.
- Add Aurora (`aurora`) input plugin.
- Add Regex (`regex`) processor plugin.
- Add support for Graphite 1.1 tags.
- Add timeout option to Sensors (`sensors)` input plugin.
- Add Burrow (`burrow`) input plugin.
- Add option to Unbound (`unbound`) input plugin to use threads as tags.
- Add support for TLS and username/password auth to Aerospike (`aerospike`) input plugin.
- Add special syslog timestamp parser to grok parser that uses current year.
- Add Syslog (`syslog`) input plugin.
- Print the enabled aggregator and processor plugins on startup.
- Add static `routing_key` option to `amqp` output.
- Add passive mode exchange declaration option to AMQP Consumer (`amqp_consumer`) input plugin.
- Add counter fields to PF (`pf`) input plugin.

### Bug fixes

- Write to working file outputs if any files are not writeable.
- Add all win\_perf\_counters fields for a series in a single metric.
- Report results of `dns_query` instead of `0ms` on timeout.
- Add consul service tags to metric.
- Fix wildcards and multi instance processes in win\_perf\_counters.
- Fix crash on 32-bit Windows in `win_perf_counters`.
- Fix `win_perf_counters` not collecting at every interval.
- Use same flags for all BSD family ping variants.

## v1.6.4

### Bug fixes

- Fix SNMP overriding of auto-configured table fields.
- Fix uint support in CloudWatch output.
- Fix documentation of `instance_name` option in Varnish input.
- Revert to previous Aerospike library version due to memory leak.

## v1.6.3

### Bug fixes

- Fix intermittent panic in Aerospike input plugin.
- Fix connection leak in the Jolokia agent (`Jolokia2_agent`) input plugin.
- Fix Jolokia agent (`Jolokia2_agent`) input plugin timeout parsing.
- Fix error parsing Dropwizard metrics.
- Fix Librato (`librato`) output plugin support for unsigned integer (`uint`) and Boolean (`bool`).
- Fix WaitGroup deadlock, if URL is incorrect, in Apache input plugin.

## v1.6.2

### Bug fixes

- Use same timestamp for fields in system input.
- Fix handling of uint64 in Datadog (`datadog`) output.
- Ignore UTF8 BOM in JSON parser.
- Fix case for slave metrics in MySQL (`mysql`) input.
- Fix uint support in CrateDB (`cratedb`) output.

## v1.6.1

### Bug fixes

- Report mem input fields as gauges instead of counters.
- Fix Graphite outputs unsigned integers in wrong format.
- Report available fields if `utmp` is unreadable.
- Fix potential `no fields` error writing to outputs.
- Fix uptime reporting in system input when ran inside docker.
- Fix mem input `cannot allocate memory` error on FreeBSD-based systems.
- Fix duplicate tags when overriding an existing tag.
- Add server argument as first argument in the Unbound (`unbound`) input plugin.
- Fix handling of floats with multiple leading zeroes.
- Return errors in SSL/TLS configuration of MongoDB (`mongodb`) input plugin.

## v1.6

### Release notes

- The MySQL (`mysql`) input plugin has been updated fix a number of type conversion issues. This may cause a `field type error` when inserting into InfluxDB due the change of types.

    To address this, we have introduced a new `metric_version` option to control enabling the new format. For in depth recommendations on upgrading, see [Metric version](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/mysql#metric-version) in the MySQL input plugin documentation.

    You are encouraged to migrate to the new model when possible as the old version is deprecated and will be removed in a future version.

- The PostgreSQL (`postgresql`) input plugin now defaults to using a persistent connection to the database. In environments where TCP connections are terminated, the `max_lifetime` setting should be set less than the collection `interval` to prevent errors.

- The SQL Server (`sqlserver`) input plugin has a new query and data model that can be enabled by setting `query_version = 2`. Migrate to the new model, if possible, since the old version is deprecated and will be removed in a future version.

- The OpenLDAP (`openldap`) input plugin has a new option, `reverse_metric_names = true`, that reverses metric names to improve grouping. Enable this option, when possible, as the old ordering is deprecated.

- The new HTTP (`http`) input plugin, when configured with `data_format = "json"`, can perform the same task as the, now deprecated, HTTP JSON (`httpjson`) input plugin.

### New input plugins

- [HTTP (`http`) input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/http/README.md) - Thanks to @grange74
- [Ipset (`ipset`) input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/ipset/README.md) - Thanks to @sajoupa
- [NATS Server Monitoring (`nats`) input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/nats/README.md) - Thanks to @mjs and @levex

### New processor plugins

- [Override (`override`) processor plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/processors/override/README.md) - Thanks to @KarstenSchnitter

### New parsers

- [Dropwizard input data format](https://github.com/influxdata/telegraf/blob/release-1.8/docs/DATA_FORMATS_INPUT.md#dropwizard) - Thanks to @atzoum

### Features

- Add health status mapping from `string` to `int` in Elasticsearch (`elasticsearch`) input plugin.
- Add control over which stats to gather in BasicStats (`basicstats`) aggregator plugin.
- Add `messages_delivered_get` to RabbitMQ (`rabbitmq`) input plugin.
- Add `wired` field to mem input plugin.
- Add support for gathering exchange metrics to the RabbitMQ (`rabbitmq`) input plugin.
- Add support for additional metrics on Linux in Zfs (`zfs`) input plugin.
- Add `available_entropy` field to Kernel (`kernel`) input plugin.
- Add user privilege level setting to IPMI sensors.
- Use persistent connection to PostgreSQL database.
- Add support for dropwizard input data format.
- Add container health metrics to Docker (`docker`) input plugin.
- Add support for using globs in devices list of DiskIO (`diskio`) input plugin.
- Allow running as console application on Windows.
- Add listener counts and node running status to RabbitMQ (`rabbitmq`) input plugin.
- Add NATS Server Monitoring (`nats`) input plugin.
- Add ability to select which queues will be gathered in RabbitMQ (`rabbitmq`) input plugin.
- Add support for setting BSD source address to the ping (`ping`) input plugin.
- Add Ipset (`ipset`) input plugin.
- Add TLS and HTTP basic auth to Prometheus Client (`prometheus_client`) output plugin.
- Add new sqlserver output data model.
- Add native Go method for finding `pid` to the Procstat (`procstat`) input plugin.
- Add additional metrics and reverse metric names option to OpenLDAP (`openldap`) input plugin.
- Add TLS support to the Mesos (`mesos`) input plugin.
- Add HTTP (`http`) input plugin.
- Add keep alive support to the TCP mode of StatsD (`statsd`) input plugin .
- Support deadline in Ping (`ping`) input plugin.
- Add option to disable labels in the Prometheus Client (`prometheus`) output plugin for string fields.
- Add shard server stats to the MongoDB (`mongodb`) input plugin.
- Add server option to Unbound (`unbound`) input plugin.
- Convert boolean metric values to float in Datadog (`datadog`) output plugin.
- Add Solr 3 compatibility.
- Add sum stat to BasicStats (`basicstats`) aggregator plugin.
- Add ability to override proxy from environment in HTTP Response (`http_response`) input plugin.
- Add host to ping timeout log message.
- Add override processor plugin.
- Add `status_code` and result tags and `result_type` field to HTTP Response (`http_response`) input plugin.
- Added config flag to skip collection of network protocol metrics.
- Add TLS support to Kapacitor (`kapacitor`) input plugin.
- Add HTTP basic auth support to the HTTP Listener (`http_listener`) input plugin.
- Tags in output InfluxDB Line Protocol are now sorted.
- InfluxDB Line Protocol parser now accepts DOS line endings.
- An option has been added to skip database creation in the InfluxDB (`influxdb`) output plugin.
- Add support for connecting to InfluxDB over a UNIX domain socket.
- Add optional unsigned integer support to the influx data format.
- Add TLS support to Zookeeper (`zookeeper`) input plugin.
- Add filters for container state to Docker (`docker`) input plugin.

### Bug fixes

- Fix various MySQL data type conversions.
- Fix metric buffer limit in internal plugin after reload.
- Fix panic in HTTP Response (`http_response`) input plugin on invalid regex.
- Fix socket\_listener setting ReadBufferSize on TCP sockets.
- Add tag for target URL to `phpfpm` input plugin.
- Fix cannot unmarshal object error in Mesosphere DC/OS (`dcos`) input plugin.
- Fix InfluxDB output not able to reconnect when server address changes.
- Fix parsing of DOS line endings in the SMART (`smart`) input plugin.
- Fix precision truncation when no timestamp included.
- Fix SNMPv3 connection with Cisco ASA 5515 in SNMP (`snmp`) input plugin.

## v1.5.3

### Bug fixes

- Set path to `/` if `HOST_MOUNT_PREFIX` matches full path.
- Remove `userinfo` from `url` tag in Prometheus input plugin.
- Fix Ping input plugin not reporting zero durations.
- Disable `keepalive` in MQTT output plugin to prevent deadlock.
- Fix collation difference in SQL Server (`sqlserver`) input plugin.
- Fix uptime metric in Passenger (`passenger`) input plugin.
- Add output of stderr in case of error to exec log message.

## v1.5.2

### Bug fixes

- Ignore empty lines in Graphite plaintext.
- Fix `index out of bounds` error in Solr input plugin.
- Reconnect before sending Graphite metrics if disconnected.
- Align aggregator period with internal ticker to avoid skipping metrics.
- Fix a potential deadlock when using aggregators.
- Limit wait time for writes in MQTT (`mqtt`) output plugin.
- Revert change in Graphite (`graphite`) output plugin where dot(`.`) in field key was replaced by underscore (`_`).
- Add `timeout` to Wavefront output write.
- Exclude `master_replid` fields from Redis input.

## v1.5.1

### Bug fixes

- Fix name error in jolokia2\_agent sample config.
- Fix DC/OS input - login expiration time.
- Set Content-Type charset parameter in InfluxDB (`influxdb`) output plugin and allow it to be overridden.
- Document permissions setup for Postfix (`postfix`) input plugin.
- Fix `deliver_get` field in RabbitMQ (`rabbitmq`) input plugin.
- Escape environment variables during config TOML parsing.

## v1.5

### New plugins

#### Input plugins

- [Bond (bond)](https://github.com/influxdata/telegraf/tree/release-1.5/plugins/inputs/bond/README.md) - Thanks to @ildarsv
- [DC/OS (dcos)](https://github.com/influxdata/telegraf/tree/release-1.5/plugins/inputs/dcos/README.md) - Thanks to @influxdata
- [Jolokia2 (jolokia2)](https://github.com/influxdata/telegraf/tree/release-1.5/plugins/inputs/jolokia2/README.md) - Thanks to @dylanmei
- [NGINX Plus (nginx\_plus)](https://github.com/influxdata/telegraf/tree/release-1.5/plugins/inputs/nginx_plus/README.md) - Thanks to @mplonka & @poblahblahblah
- [OpenSMTPD (opensmtpd)](https://github.com/influxdata/telegraf/tree/release-1.5/plugins/inputs/opensmtpd/README.md) - Thanks to @aromeyer
- [Particle.io Webhooks (particle)](https://github.com/influxdata/telegraf/tree/release-1.5/plugins/inputs/webhooks/particle/README.md) - Thanks to @davidgs
- [PF (pf)](https://github.com/influxdata/telegraf/tree/release-1.5/plugins/inputs/pf/README.md) - Thanks to @nferch
- [Postfix (postfix)](https://github.com/influxdata/telegraf/tree/release-1.5/plugins/inputs/postfix/README.md) - Thanks to @phemmer
- [SMART (smart)](https://github.com/influxdata/telegraf/tree/release-1.5/plugins/inputs/smart/README.md) - Thanks to @rickard-von-essen
- [Solr (solr)](https://github.com/influxdata/telegraf/tree/release-1.5/plugins/inputs/solr/README.md) - Thanks to @ljagiello
- [Teamspeak (teamspeak)](https://github.com/influxdata/telegraf/tree/release-1.5/plugins/inputs/teamspeak/README.md) - Thanks to @p4ddy1
- [Unbound (unbound)](https://github.com/influxdata/telegraf/tree/release-1.5/plugins/inputs/unbound/README.md) - Thanks to @aromeyer

#### Aggregator plugins

- [BasicStats (basicstats)](https://github.com/influxdata/telegraf/tree/release-1.5/plugins/aggregators/basicstats/README.md) - Thanks to @toni-moreno

#### Output plugins

- [CrateDB (cratedb)](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/outputs/cratedb) - Thanks to @felixge
- [Wavefront (wavefront)](https://github.com/influxdata/telegraf/tree/release-1.5/plugins/outputs/wavefront/README.md) - Thanks to @puckpuck

### Release notes

- In the Kinesis (`kinesis`) output plugin, use of the `partition_key` and `use_random_partitionkey` options has been deprecated in favor of the `partition` subtable. This allows for more flexible methods to set the partition key such as by metric name or by tag.

- With the release of the new improved Jolokia2 (`jolokia2`) input plugin, the legacy `jolokia` plugin is deprecated and will be removed in a future release. Users of this plugin are encouraged to update to the new `jolokia2` plugin.

### Features

- Add support for sharding based on metric name.
- Add Kafka output plugin `topic_suffix` option.
- Include mount mode option in disk metrics.
- TLS and MTLS enhancements to HTTP Listener input plugin.
- Add polling method to logparser and tail inputs.
- Add timeout option for Kubernetes (`kubernetes`) input plugin.
- Add support for timing sums in statsd input plugin.
- Add resource limit monitoring to Procstat (`procstat`) input plugin.
- Add support for k8s service DNS discovery to Prometheus Client (`prometheus`) input plugin.
- Add configurable metrics endpoint to (`prometheus`) output plugin.
- Add support for NSQLookupd to `nsq_consumer`.
- Add configurable separator for metrics and fields in OpenTSDB (`opentsdb`) output plugin.
- Add support for the rollbar occurrence webhook event.
- Add extra wired tiger cache metrics to `mongodb` input.
- Collect Docker Swarm service metrics in Docker (`docker`) input plugin.
- Add cluster health level configuration to Elasticsearch (`elasticsearch`) input plugin.
- Add ability to limit node stats in Elasticsearch (`elasticsearch`) input plugin.
- Add UDP IPv6 support to StatsD (`statsd`) input plugin.
- Use labels in Prometheus Client (`prometheus`) output plugin for string fields.
- Add support for decimal timestamps to ts-epoch modifier.
- Add histogram and summary types and use in Prometheus (`prometheus`) plugins.
- Gather concurrently from snmp agents.
- Perform DNS lookup before ping and report result.
- Add instance name option to Varnish (`varnish`) plugin.
- Add support for SSL settings to ElasticSearch (`elasticsearch`) output plugin.
- Add modification\_time field to Filestat (`filestat`) input plugin.
- Add systemd unit pid and cgroup matching to Procstat (`procstat`) .
- Use MAX() instead of SUM() for latency measurements in SQL Server (`sqlserver`) input plugin.
- Add index by week number to Elasticsearch (`elasticsearch`) output plugin.
- Add support for tags in the index name in Elasticsearch (`elasticsearch`) output plugin.
- Add slab to mem plugin.
- Add support for glob patterns in net input plugin.
- Add option to AMQP (`amqp`) output plugin to publish persistent messages.
- Support I (idle) process state on procfs+Linux.

### Bug fixes

- Fix webhooks input address in use during reload.
- Unlock Statsd when stopping to prevent deadlock.
- Fix cloudwatch output requires unneeded permissions.
- Fix prometheus passthrough for existing value types.
- Always ignore autofs filesystems in disk input.
- Fail metrics parsing on unescaped quotes.
- Whitelist allowed char classes for graphite output.
- Use hexadecimal ids and lowercase names in zipkin input.
- Fix snmp-tools output parsing with Windows EOLs.
- Add shadow-utils dependency to rpm package.
- Use deb-systemd-invoke to restart service.
- Fix kafka\_consumer outside range of offsets error.
- Fix separation of multiple prometheus\_client outputs.
- Don’t add system input uptime\_format as a counter.

## v1.4.5

### Bug fixes

- Fix global variable collection when using interval\_slow option in MySQL input.
- Fix error getting net connections info in netstat input.
- Fix HOST\_MOUNT\_PREFIX in Docker with disk input.

## v1.4.4

### Bug fixes

- Use schema specified in mqtt\_consumer input.
- Redact Datadog API key in log output.
- Fix error getting PIDs in netstat input.
- Support HOST\_VAR envvar to locate /var in system input.
- Use current time if Docker container read time is zero value.

## v1.4.3

### Bug fixes

- Fix container name filters in Docker input.
- Fix snmpwalk address format in leofs input.
- Fix case sensitivity issue in SQL Server query.
- Fix CPU input plugin stuck after suspend on Linux.
- Fix MongoDB input panic when restarting MongoDB.
- Preserve URL path prefix in InfluxDB output.
- Fix TELEGRAF\_OPTS expansion in systemd service unit.
- Remove warning when JSON contains null value.
- Fix ACL token usage in consul input plugin.
- Fix unquoting error with Tomcat 6.
- Fix syscall panic in diskio on some Linux systems.

## v1.4.2

### Bug fixes

- Fix error if int larger than 32-bit in `/proc/vmstat`.
- Fix parsing of JSON with a UTF8 BOM in `httpjson`.
- Allow JSON data format to contain zero metrics.
- Fix format of connection\_timeout in `mqtt_consumer`.
- Fix case sensitivity error in SQL Server input.
- Add support for proxy environment variables to `http_response`.
- Add support for standard proxy env vars in outputs.
- Fix panic in CPU input if number of CPUs changes.
- Use chunked transfer encoding in InfluxDB output.

## v1.4.1

### Bug fixes

- Fix MQTT input exits if Broker is not available on startup.
- Fix optional field value conversions in fluentd input.
- Whitelist allowed char classes for opentsdb output.
- Fix counter and gauge metric types.
- Fix skipped line with empty target in iptables.
- Fix duplicate keys in perf counters sqlserver query.
- Fix panic in statsd p100 calculation.
- Fix arm64 packages contain 32-bit executable.

## v1.4.0

### Release Notes

- The `kafka_consumer` input has been updated to support Kafka 0.9 and above style consumer offset handling. The previous version of this plugin supporting Kafka 0.8 and below is available as the `kafka_consumer_legacy` plugin.
- In the `aerospike` input the `node_name` field has been changed to be a tag for both the `aerospike_node` and `aerospike_namespace` measurements.
- The default prometheus\_client port has been changed to 9273.

### New plugins

- fail2ban
- fluentd
- histogram
- minecraft
- openldap
- salesforce
- tomcat
- win\_services
- zipkin

### Features

- Add Kafka 0.9+ consumer support.
- Add support for self-signed certs to InfluxDB input plugin.
- Add TCP listener for statsd input.
- Add Docker container environment variables as tags. Only whitelisted.
- Add timeout option to IPMI sensor plugin.
- Add support for an optional SSL/TLS configuration to Nginx input plugin.
- Add timezone support for logparser timestamps.
- Add result\_type field for http\_response input.
- Add include/exclude filters for docker containers.
- Add secure connection support to graphite output.
- Add min/max response time on linux/darwin to ping.
- Add HTTP Proxy support to influxdb output.
- Add standard SSL options to mysql input.
- Add input plugin for fail2ban.
- Support HOST\_PROC in processes and linux\_sysctl\_fs inputs.
- Add Minecraft input plugin.
- Add support for RethinkDB 1.0 handshake protocol.
- Add optional usage\_active and time\_active CPU metrics.
- Change default prometheus\_client port.
- Add fluentd input plugin.
- Add result\_type field to net\_response input plugin.
- Add read timeout to socket\_listener.
- Add input plugin for OpenLDAP.
- Add network option to dns\_query.
- Add redis\_version field to redis input.
- Add tls options to docker input.
- Add histogram aggregator plugin.
- Add Zipkin input plugin.
- Add Windows Services input plugin.
- Add path tag to logparser containing path of logfile.
- Add Salesforce input plugin.
- Add option to run varnish under sudo.
- Add weighted\_io\_time to diskio input.
- Add gzip content-encoding support to influxdb output.
- Allow using system plugin in Windows.
- Add Tomcat input plugin.
- HTTP headers can be added to InfluxDB output.

### Bug fixes

- Improve logging of errors in Cassandra input.
- \[enh\] set db\_version at 0 if query version fails.
- Fixed SQL Server input to work with case sensitive server collation.
- Systemd does not see all shutdowns as failures.
- Reuse transports in input plugins.
- Inputs processes fails with “no such process”.
- Fix multiple plugin loading in win\_perf\_counters.
- MySQL input: log and continue on field parse error.
- Fix timeout option in Windows ping input sample configuration.
- Fix Kinesis output plugin in govcloud.
- Fix Aerospike input adds all nodes to a single series.
- Improve Prometheus Client output documentation.
- Display error message if prometheus output fails to listen.
- Fix elasticsearch output content type detection warning.
- Prevent possible deadlock when using aggregators.
- Fix combined tagdrop/tagpass filtering.
- Fix filtering when both pass and drop match an item.
- Only report cpu usage for online cpus in docker input.
- Start first aggregator period at startup time.
- Fix panic in logparser if file cannot be opened.
- Default to localhost if zookeeper has no servers set.
- Fix docker memory and cpu reporting in Windows.
- Allow iptable entries with trailing text.
- Sanitize password from couchbase metric.
- Converge to typed value in prometheus output.
- Skip compilation of logparser and tail on solaris.
- Discard logging from tail library.
- Remove log message on ping timeout.
- Don’t retry points beyond retention policy.
- Don’t start Telegraf on install in Amazon Linux.
- Enable hddtemp input on all platforms.
- Escape backslash within string fields.
- Fix parsing of SHM remotes in ntpq input
- Don’t fail parsing zpool stats if pool health is UNAVAIL on FreeBSD.
- Fix NSQ input plugin when used with version 1.0.0-compat.
- Added CloudWatch metric constraint validation.
- Skip non-numerical values in graphite format.
- Fix panic when handling string fields with escapes.

## v1.3.5

### Bug fixes

- Fix prometheus output cannot be reloaded.
- Fix filestat reporting exists when cannot list directory.
- Fix ntpq parse issue when using dns\_lookup.
- Fix panic when agent.interval = “0s”.

## v1.3.4

### Bug fixes

- Fix handling of escape characters within fields.
- Fix chrony plugin does not track system time offset.
- Do not allow metrics with trailing slashes.
- Prevent Write from being called concurrently.

## v1.3.3

### Bug fixes

- Allow dos line endings in tail and logparser.
- Remove label value sanitization in prometheus output.
- Fix bug parsing default timestamps with modified precision.
- Fix panic in elasticsearch input if cannot determine master.

## v1.3.2

### Bug fixes

- Fix InfluxDB UDP metric splitting.
- Fix mongodb/leofs urls without scheme.
- Fix inconsistent label dimensions in prometheus output.

## v1.3.1

### Bug fixes

- Fixed sqlserver input to work with case-sensitive server collation.
- Reuse transports in input plugins.
- Process input fails with `no such process`.
- Fix InfluxDB output database quoting.
- Fix net input on older Linux kernels.
- Fix panic in mongo input.
- Fix length calculation of split metric buffer.

## v1.3.0

#### Changes to the Windows ping plugin

Users of the windows [ping plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/ping) will need to drop or migrate their measurements to continue using the plugin. The reason for this is that the windows plugin was outputting a different type than the linux plugin. This made it impossible to use the `ping` plugin for both windows and linux machines.

#### Changes to the Ceph plugin

For the [Ceph plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/ceph), the `ceph_pgmap_state` metric content has been modified to use a unique field `count`, with each state expressed as a `state` tag.

Telegraf < 1.3:

```text
# field_name             value
active+clean             123
active+clean+scrubbing   3
```

Telegraf >= 1.3:

```text
# field_name    value       tag
count           123         state=active+clean
count           3           state=active+clean+scrubbing
```

#### Rewritten Riemann plugin

The [Riemann output plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/outputs/riemann) has been rewritten and the [previous riemann plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/outputs/riemann_legacy) is *incompatible* with the new one. The reasons for this are outlined in issue [#1878](https://github.com/influxdata/telegraf/issues/1878). The previous Riemann output will still be available using `outputs.riemann_legacy` if needed, but that will eventually be deprecated. It is highly recommended that all users migrate to the new Riemann output plugin.

#### New Socket Listener and Socket Writer plugins

Generic [Socket Listener](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/socket_listener) and [Socket Writer](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/outputs/socket_writer) plugins have been implemented for receiving and sending UDP, TCP, unix, & unix-datagram data. These plugins will replace [udp\_listener](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/udp_listener) and [tcp\_listener](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/tcp_listener), which are still available but will be deprecated eventually.

### Features

- Add SASL options for the [Kafka output plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/outputs/kafka).
- Add SSL configuration for [HAproxy input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/haproxy).
- Add the [Interrupts input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/interrupts).
- Add generic [Socket Listener input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/socket_listener) and [socket writer output plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/outputs/socket_writer).
- Extend the [HTTP Response input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/http_response) to support searching for a substring in response. Return 1 if found, else 0.
- Add userstats to the [MySQL input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/mysql).
- Add more InnoDB metric to the [MySQL input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/mysql).
- For the [Ceph input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/ceph), `ceph_pgmap_state` metric now uses a single field `count`, with PG state published as `state` tag.
- Use own client for improved through-put and less allocations in the [InfluxDB output plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/outputs/influxdb).
- Keep -config-directory when running as Windows service.
- Rewrite the [Riemann output plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/outputs/riemann).
- Add support for name templates and udev tags to the [DiskIO input plugin](https://github.com/influxdata/telegraf/blob/release-1.8/plugins/inputs/diskio/README.md).
- Add integer metrics for [Consul](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/consul) check health state.
- Add lock option to the [IPtables input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/iptables).
- Support [ipmi\_sensor input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/ipmi_sensor) querying local ipmi sensors.
- Increment gather\_errors for all errors emitted by inputs.
- Use the official docker SDK.
- Add [AMQP consumer input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/amqp_consumer).
- Add pprof tool.
- Support DEAD(X) state in the [system input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/system).
- Add support for [MongoDB](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/mongodb) client certificates.
- Support adding [SNMP](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/snmp) table indexes as tags.
- Add [Elasticsearch 5.x output plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/outputs/elasticsearch).
- Add json timestamp units configurability.
- Add support for Linux sysctl-fs metrics.
- Support to include/exclude docker container labels as tags.
- Add [DMCache input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/dmcache).
- Add support for precision in [HTTP Listener input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/http_listener).
- Add `message_len_max` option to the [Kafka consumer input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/kafka_consumer).
- Add [collectd parser](https://docs.influxdata.com/telegraf/v1/data_formats/input/collectd/).
- Simplify plugin testing without outputs.
- Check signature in the [GitHub webhook input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/webhooks/github).
- Add [papertrail](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/webhooks/papertrail) support to webhooks.
- Change [jolokia input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/jolokia) to use bulk requests.
- Add [DiskIO input plugin](https://github.com/influxdata/telegraf/blob/release-1.8/plugins/inputs/diskio/README.md) for Darwin.
- Add use\_random\_partitionkey option to the [Kinesis output plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/outputs/kinesis).
- Add tcp keep-alive to [Socket Listener input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/socket_listener) and [Socket Writer output plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/outputs/socket_writer).
- Add [Kapacitor input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/kapacitor).
- Use Go (golang) 1.8.1.
- Add documentation for the [RabbitMQ input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/rabbitmq).
- Make the [Logparser input plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/logparser) check for newly-created files.

### Bug fixes

- Allow `@` symbol in password for the ipmi\_sensor plugin.
- Fix arithmetic overflow error converting numeric to data type int in SQL Server input.
- Flush jitter can inhibit metric collection.
- Add missing fields for HAproxy input.
- Handle null startTime for stopped pods for the Kubernetes input.
- Fix cpu input panic when /proc/stat is empty.
- Fix telegraf swallowing panics in –test mode.
- Create pidfile with 644 permissions & defer file deletion.
- Fix install/remove of telegraf on non-systemd Debian/Ubuntu systems.
- Fix for reloading telegraf freezes prometheus output.
- Fix when empty tag value causes error on InfluxDB output.
- buffer\_size field value is negative number from “internal” plugin.
- Missing error handling in the MySQL plugin leads to segmentation violation.
- Fix type conflict in windows ping plugin.
- logparser: regexp with lookahead.
- Telegraf can crash in LoadDirectory on 0600 files.
- Iptables input: document better that rules without a comment are ignored.
- Fix win\_perf\_counters capping values at 100.
- Exporting Ipmi.Path to be set by config.
- Remove warning if parse empty content.
- Update default value for Cloudwatch rate limit.
- create /etc/telegraf/telegraf.d directory in tarball.
- Return error on unsupported serializer data format.
- Fix Windows Performance Counters multi instance identifier.
- Add write timeout to Riemann output.
- fix timestamp parsing on prometheus plugin.
- Fix deadlock when output cannot write.
- Fix connection leak in postgresql.
- Set default measurement name for snmp input.
- Improve performance of diskio with many disks.
- The internal input plugin uses the wrong units for `heap_objects`.
- Fix ipmi\_sensor config is shared between all plugin instances.
- Network statistics not collected when system has alias interfaces.
- Sysstat plugin needs LANG=C or similar locale.
- File output closes standard streams on reload.
- AMQP output disconnect blocks all outputs.
- Improve documentation for redis input plugin.

## v1.2.1

### Bug fixes

- Fix segfault on nil metrics with InfluxDB output.
- Fix negative number handling.

### Features

- Go (golang) version update 1.7.4 -> 1.7.5

## v1.2

### Release Notes

- The StatsD plugin will now default all “delete\_” config options to “true”. This will change te default behavior for users who were not specifying these parameters in their config file.

- The StatsD plugin will also no longer save it’s state on a service reload. Essentially we have reverted PR [#887](https://github.com/influxdata/telegraf/pull/887). The reason for this is that saving the state in a global variable is not thread-safe (see [#1975](https://github.com/influxdata/telegraf/issues/1975) & [#2102](https://github.com/influxdata/telegraf/issues/2102)), and this creates issues if users want to define multiple instances of the statsd plugin. Saving state on reload may be considered in the future, but this would need to be implemented at a higher level and applied to all plugins, not just statsd.

### Features

- Fix improper calculation of CPU percentages
- Use RFC3339 timestamps in log output.
- Non-default HTTP timeouts for RabbitMQ plugin.
- “Discard” output plugin added, primarily for testing purposes.
- The JSON parser can now parse an array of objects using the same configuration.
- Option to use device name rather than path for reporting disk stats.
- Telegraf “internal” plugin for collecting stats on itself.
- Update GoLang version to 1.7.4.
- Support a metric.Split function.
- Elasticsearch “shield” (basic auth) support doc.
- Fix over-querying of cloudwatch metrics
- OpenTSDB basic auth support.
- RabbitMQ Connection metrics.
- HAProxy session limit metric.
- Accept strings for StatsD sets.
- Change StatsD default “reset” behavior.
- Enable setting ClientID in MQTT output.
- MongoDB input plugin: Improve state data.
- Ping input: add standard deviation field.
- Add GC pause metric to InfluxDB input plugin.
- Added response\_timeout property to prometheus input plugin.
- Pulling github.com/lxn/win’s pdh wrapper into Telegraf.
- Support negative statsd counters.
- Elasticsearch cluster stats support.
- Change Amazon Kinesis output plugin to use the built-in serializer plugins.
- Hide username/password from elasticsearch error log messages.
- Configurable HTTP timeouts in Jolokia plugin.
- Allow changing jolokia attribute delimiter.

### Bug fixes

- Fix the Value data format not trimming null characters from input.
- Fix windows `.net` plugin.
- Cache & expire metrics for delivery to prometheus
- Fix potential panic in aggregator plugin metric maker.
- Add optional ability to define PID as a tag.
- Fix win\_perf\_counters not gathering non-English counters.
- Fix panic when file stat info cannot be collected due to permissions or other issue(s).
- Graylog output should set short\_message field.
- Hddtemp always put the value in the field temperature.
- Properly collect nested jolokia struct data.
- Fix puppetagent inputs plugin to support string for config variable.
- Fix docker input plugin tags when registry has port.
- Fix tail input when reading from a pipe.
- MongoDB plugin always shows 0 replication lag.
- Consul plugin: add check\_id as a tag in metrics to avoid overwrites.
- Partial fix: logparser CLF pattern with IPv6 addresses.
- Fix thread-safety when using multiple instances of the statsd input plugin.
- Docker input: interface conversion panic fix.
- SNMP: ensure proper context is present on error messages.
- OpenTSDB: add tcp:// prefix if no scheme provided.
- Influx parser: parse line-protocol without newlines.
- InfluxDB output: fix field type conflict blocking output buffer.

## v1.1.2

### Bug fixes

- Make snmptranslate not required when using numeric OID.
- Add a global snmp translation cache.

## v1.1.1

### Bug fixes

- Fix issue parsing toml durations with single quotes.

## v1.1.0

### Release Notes

- Telegraf now supports two new types of plugins: processors & aggregators.

- On systemd Telegraf will no longer redirect it’s stdout to /var/log/telegraf/telegraf.log. On most systems, the logs will be directed to the systemd journal and can be accessed by `journalctl -u telegraf.service`. Consult the systemd journal documentation for configuring journald. There is also a [`logfile` config option](https://github.com/influxdata/telegraf/blob/release-1.8/etc/telegraf.conf#L70) available in 1.1, which will allow users to easily configure telegraf to continue sending logs to /var/log/telegraf/telegraf.log.

### Features

- Processor & Aggregator plugin support.
- Adding the tags in the graylog output plugin.
- Telegraf systemd service, log to journal.
- Allow numeric and non-string values for tag\_keys.
- Adding Gauge and Counter metric types.
- Remove carraige returns from exec plugin output on Windows
- Elasticsearch input: configurable timeout.
- Massage metric names in Instrumental output plugin
- Apache Mesos improvements.
- Add Ceph Cluster Performance Statistics
- Ability to configure response\_timeout in httpjson input.
- Add additional redis metrics.
- Added capability to send metrics through HTTP API for OpenTSDB.
- iptables input plugin.
- Add filestack webhook plugin.
- Add server hostname for each Docker measurements.
- Add NATS output plugin.
- HTTP service listener input plugin.
- Add database blacklist option for Postgresql
- Add Docker container state metrics to Docker input plugin output
- Add support to SNMP for IP & MAC address conversion.
- Add support to SNMP for OID index suffixes.
- Change default arguments for SNMP plugin.
- Apache Mesos input plugin: very high-cardinality mesos-task metrics removed.
- Logging overhaul to centralize the logger & log levels, & provide a logfile config option.
- HAProxy plugin socket glob matching.
- Add Kubernetes plugin for retrieving pod metrics.

### Bug fixes

- Fix NATS plug-ins reconnection logic.
- Set required default values in udp\_listener & tcp\_listener.
- Fix toml unmarshal panic in Duration objects.
- Fix handling of non-string values for JSON keys listed in tag\_keys.
- Fix mongodb input panic on version 2.2.
- Fix statsd scientific notation parsing.
- Sensors plugin strconv.ParseFloat: parsing “”: invalid syntax.
- Fix prometheus\_client reload panic.
- Fix Apache Kafka consumer panic when nil error is returned down errs channel.
- Speed up statsd parsing.
- Fix powerdns integer parse error handling.
- Fix varnish plugin defaults not being used.
- Fix Windows glob paths.
- Fix issue loading config directory on Windows.
- Windows remote management interactive service fix.
- SQLServer, fix issue when case sensitive collation is activated.
- Fix huge allocations in http\_listener when dealing with huge payloads.
- Fix translating SNMP fields not in MIB.
- Fix SNMP emitting empty fields.
- SQL Server waitstats truncation bug.
- Fix logparser common log format: numbers in ident.
- Fix JSON Serialization in OpenTSDB output.
- Fix Graphite template ordering, use most specific.
- Fix snmp table field initialization for non-automatic table.
- cgroups path being parsed as metric.
- Fix phpfpm fcgi client panic when URL does not exist.
- Fix config file parse error logging.
- Delete nil fields in the metric maker.
- Fix MySQL special characters in DSN parsing.
- Ping input odd timeout behavior.
- Switch to github.com/kballard/go-shellquote.

## v1.0.1

### Bug fixes

- Prometheus output: Fix bug with multi-batch writes.
- Fix unmarshal of influxdb metrics with null tags.
- Add configurable timeout to influxdb input plugin.
- Fix statsd no default value panic.

## v1.0

### Release Notes

**Breaking Change** The SNMP plugin is being deprecated in it’s current form. There is a [new SNMP plugin](https://github.com/influxdata/telegraf/tree/release-1.8/plugins/inputs/snmp) which fixes many of the issues and confusions of its predecessor. For users wanting to continue to use the deprecated SNMP plugin, you will need to change your config file from `[[inputs.snmp]]` to `[[inputs.snmp_legacy]]`. The configuration of the new SNMP plugin is *not* backwards-compatible.

**Breaking Change**: Aerospike main server node measurements have been renamed aerospike\_node. Aerospike namespace measurements have been renamed to aerospike\_namespace. They will also now be tagged with the node\_name that they correspond to. This has been done to differentiate measurements that pertain to node vs. namespace statistics.

**Breaking Change**: users of github\_webhooks must change to the new `[[inputs.webhooks]]` plugin.

This means that the default github\_webhooks config:

```ini
# A Github Webhook Event collector
[[inputs.github_webhooks]]
  ## Address and port to host Webhook listener on
  service_address = ":1618"
```

should now look like:

```ini
# A Webhooks Event collector
[[inputs.webhooks]]
  ## Address and port to host Webhook listener on
  service_address = ":1618"

  [inputs.webhooks.github]
    path = "/"
```

- Telegraf now supports being installed as an official windows service, which can be installed via `> C:\Program Files\Telegraf\telegraf.exe --service install`

- `flush_jitter` behavior has been changed. The random jitter will now be evaluated at every flush interval, rather than once at startup. This makes it consistent with the behavior of `collection_jitter`.

- PostgreSQL plugins now handle oid and name typed columns seamlessly, previously they were ignored/skipped.

### Features

- postgresql\_extensible now handles name and oid types correctly.
- Separate container\_version from container\_image tag.
- Support setting per-device and total metrics for Docker network and blockio.
- MongoDB input plugin: adding per DB stats from db.stats()
- Add tls support for certs to RabbitMQ input plugin.
- Webhooks input plugin.
- Rollbar webhook plugin.
- Mandrill webhook plugin.
- docker-machine/boot2docker no longer required for unit tests.
- cgroup input plugin.
- Add input plugin for consuming metrics from NSQD.
- Add ability to read Redis from a socket.
- **Breaking Change** - Redis `role` tag renamed to `replication_role` to avoid global\_tags override.
- Fetching Galera status metrics in MySQL
- Aerospike plugin refactored to use official client library.
- Add measurement name arg to logparser plugin.
- logparser: change resp\_code from a field to a tag.
- Implement support for fetching hddtemp data
- statsd: do not log every dropped metric.
- Add precision rounding to all metrics on collection.
- Add support for Tengine.
- Logparser input plugin for parsing grok-style log patterns.
- ElasticSearch: now supports connecting to ElasticSearch via SSL.
- Add graylog input plugin.
- Consul input plugin.
- conntrack input plugin.
- vmstat input plugin.
- Standardized AWS credentials evaluation & wildcard CloudWatch dimensions.
- Add SSL config options to http\_response plugin.
- Graphite parser: add ability to specify multiple tag keys, for consistency with influxdb parser.
- Make DNS lookups for chrony configurable.
- Allow wildcard filtering of varnish stats.
- Support for glob patterns in exec plugin commands configuration.
- RabbitMQ input: made url parameter optional by using DefaultURL (`http://localhost:15672`) if not specified.
- Limit AWS GetMetricStatistics requests to 10 per second.
- RabbitMQ/Apache/InfluxDB inputs: made url(s) parameter optional by using reasonable input defaults if not specified.
- Refactor of flush\_jitter argument.
- Add inactive & active memory to mem plugin.
- Official Windows service.
- Forking sensors command to remove C package dependency.
- Add a new SNMP plugin.

### Bug fixes

- Fix `make windows` build target.
- Fix error race conditions and partial failures.
- nstat: fix inaccurate config panic.
- jolokia: fix handling multiple multi-dimensional attributes.
- Fix prometheus character sanitizing. Sanitize more win\_perf\_counters characters.
- Add diskio io\_time to FreeBSD & report timing metrics as ms (as linux does).
- Fix covering Amazon Linux for post remove flow.
- procstat missing fields: read/write bytes & count.
- diskio input plugin: set ‘skip\_serial\_number = true’ by default to avoid high cardinality.
- nil metrics panic fix.
- Fix datarace in apache input plugin.
- Add `read_repairs` statistics to riak plugin.
- Fix memory/connection leak in Prometheus input plugin.
- Trim BOM from config file for Windows support.
- Prometheus client output panic on service reload.
- Prometheus parser, protobuf format header fix.
- Prometheus output, metric refresh and caching fixes.
- Panic fix for multiple graphite outputs under very high load.
- Instrumental output has better reconnect behavior.
- Remove PID from procstat plugin to fix cardinality issues.
- Cassandra input: version 2.x “column family” fix.
- Shared WaitGroup in Exec plugin.
- logparser: honor modifiers in “pattern” config.
- logparser: error and exit on file permissions/missing errors.
- Make the user able to specify full path for HAproxy stats.
- Fix Redis url, an extra “tcp://” was added.
- Fix exec plugin panic when using single binary.
- Fixed incorrect prometheus metrics source selection.
- Set default Zookeeper chroot to empty string.
- Fix overall ping timeout to be calculated based on per-ping timeout.
- Change “default” retention policy to “”.
- Graphite output mangling ‘%’ character.
- Prometheus input plugin now supports x509 certs authentication.
- Fix systemd service.
- Fix influxdb n\_shards counter.
- Fix potential kernel plugin integer parse error.
- Fix potential influxdb input type assertion panic.
- Still send processes metrics if a process exited during metric collection.
- disk plugin panic when usage grab fails.
- Removed leaked “database” tag on redis metrics.
- Processes plugin: fix potential error with /proc/net/stat directory.
- Fix rare RHEL 5.2 panic in gopsutil diskio gathering function.
- Remove IF NOT EXISTS from influxdb output database creation.
- Fix quoting with text values in postgresql\_extensible plugin.
- Fix win\_perf\_counter “index out of range” panic.
- Fix ntpq panic when field is missing.
- Sanitize graphite output field names.
- Fix MySQL plugin not sending 0 value fields.

---

## Telegraf Processor Plugins

Telegraf processor plugins transform individual metrics by e.g. converting tags and fields or data-types.

### AWS EC2 Metadata

Plugin ID: `processors.aws_ec2`
Telegraf v1.18.0+

This plugin appends metadata gathered from [AWS IMDS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) to metrics associated with EC2 instances.

[View](/telegraf/v1/processor-plugins/aws_ec2/)

### Batch

Plugin ID: `processors.batch`
Telegraf v1.33.0+

This plugin groups metrics into batches by adding a batch tag. This is useful for parallel processing of metrics where downstream processors, aggregators or outputs can then select a batch using `tagpass` or `metricpass`.

Metrics are distributed across batches using the round-robin scheme.

[View](/telegraf/v1/processor-plugins/batch/)

### Clone

Plugin ID: `processors.clone`
Telegraf v1.13.0+

This plugin creates a copy of each metric passing through it, preserving the original metric and allowing modifications such as [metric modifiers](/telegraf/v1/configuration/#modifiers) in the copied metric.

[Metric filtering](/telegraf/v1/configuration/#metric-filtering) options apply to both the clone and the original metric.

[View](/telegraf/v1/processor-plugins/clone/)

### Converter

Plugin ID: `processors.converter`
Telegraf v1.7.0+

This plugin allows transforming tags into fields or timestamps, and converting fields into tags or timestamps. The plugin furthermore allows to change the field type.

When converting tags to fields, take care to ensure the series is still uniquely identifiable. Fields with the same series key (measurement + tags) will overwrite one another.

[View](/telegraf/v1/processor-plugins/converter/)

### Cumulative Sum

Plugin ID: `processors.cumulative_sum`
Telegraf v1.35.0+

This plugin accumulates field values per-metric over time and emit metrics with cumulative sums whenever a metric is updated. This is useful when using outputs relying on monotonically increasing values

Metrics within a series are accumulated in the **order of arrival** and not in order of their timestamps!

[View](/telegraf/v1/processor-plugins/cumulative_sum/)

### Date

Plugin ID: `processors.date`
Telegraf v1.12.0+

This plugin adds the metric timestamp as a human readable tag. A common use is to add a tag that can be used to group by month or year.

[View](/telegraf/v1/processor-plugins/date/)

### Dedup

Plugin ID: `processors.dedup`
Telegraf v1.14.0+

This plugin filters metrics whose field values are exact repetitions of the previous values. This plugin will store its state between runs if the `statefile` option in the agent config section is set.

[View](/telegraf/v1/processor-plugins/dedup/)

### Defaults

Plugin ID: `processors.defaults`
Telegraf v1.15.0+

This plugin allows to specify default values for fields and tags for cases where the tag or field does not exist or has an empty value.

[View](/telegraf/v1/processor-plugins/defaults/)

### Enum

Plugin ID: `processors.enum`
Telegraf v1.8.0+

This plugin allows the mapping of field or tag values according to the configured enumeration. The main use-case is to rewrite numerical values into human-readable values or vice versa. Default mappings can be configured to be used for all remaining values.

[View](/telegraf/v1/processor-plugins/enum/)

### Execd

Plugin ID: `processors.execd`
Telegraf v1.15.0+

This plugin runs an external program as a separate process and pipes metrics in to the process’s `stdin` and reads processed metrics from its `stdout`. Program output on `stderr` is logged.

[View](/telegraf/v1/processor-plugins/execd/)

### Filepath

Plugin ID: `processors.filepath`
Telegraf v1.15.0+

This plugin allows transforming a path, using e.g. basename to extract the last path element, for tag and field values. Values can be modified in place or stored in another key.

[View](/telegraf/v1/processor-plugins/filepath/)

### Filter

Plugin ID: `processors.filter`
Telegraf v1.29.0+

This plugin allows specifying a set of rules for metrics with the ability to *keep* or *drop* those metrics. It does *not* modify the metric. As such a user might want to apply this processor to remove metrics from the processing/output stream.

The filtering is *not* output specific, but will apply to the metrics processed by this processor.

[View](/telegraf/v1/processor-plugins/filter/)

### Network Interface Name

Plugin ID: `processors.ifname`
Telegraf v1.15.0+

This plugin looks up network interface names using SNMP.

[View](/telegraf/v1/processor-plugins/ifname/)

### Lookup

Plugin ID: `processors.lookup`
Telegraf v1.15.0+

This plugin allows to use one or more files containing lookup-tables for annotating incoming metrics. The lookup is *static* as the files are only used on startup. The main use-case for this is to annotate metrics with additional tags e.g. dependent on their source. Multiple tags can be added depending on the lookup-table *files*.

The lookup key can be generated using a Golang template with the ability to access the metric name via `{{.Name}}`, the tag values via `{{.Tag "mytag"}}`, with `mytag` being the tag-name and field-values via `{{.Field "myfield"}}`, with `myfield` being the field-name. Non-existing tags and field will result in an empty string or `nil` respectively. In case the key cannot be found, the metric is passed-through unchanged. By default all matching tags are added and existing tag-values are overwritten.

The plugin only supports the addition of tags and thus all mapped tag-values need to be strings!

[View](/telegraf/v1/processor-plugins/lookup/)

### Noise

Plugin ID: `processors.noise`
Telegraf v1.22.0+

This plugin is used to add noise to numerical field values. For each field a noise is generated using a defined probability density function and added to the value. The function type can be configured as *Laplace*, *Gaussian* or *Uniform*.

[View](/telegraf/v1/processor-plugins/noise/)

### Override

Plugin ID: `processors.override`
Telegraf v1.6.0+

This plugin allows to modify metrics using [metric modifiers](/telegraf/v1/configuration/#modifiers). Use-cases of this plugin encompass ensuring certain tags or naming conventions are adhered to irrespective of input plugin configurations, e.g. by `taginclude`.

[Metric filtering](/telegraf/v1/configuration/#metric-filtering) options apply to both the clone and the original metric.

[View](/telegraf/v1/processor-plugins/override/)

### Parser

Plugin ID: `processors.parser`
Telegraf v1.8.0+

This plugin parses defined fields or tags containing the specified [data format](/telegraf/v1/data_formats/input) and creates new metrics based on the resulting fields and tags.

[View](/telegraf/v1/processor-plugins/parser/)

### Pivot

Plugin ID: `processors.pivot`
Telegraf v1.12.0+

This plugin rotates single-valued metrics into a multi-field metric. The result is a more compact representation for applying mathematical operators to or do comparisons between metrics or flatten fields.

To perform the reverse operation use the [unpivot](/telegraf/v1/plugins/#processor-unpivot) processor.

[View](/telegraf/v1/processor-plugins/pivot/)

### Port Name Lookup

Plugin ID: `processors.port_name`
Telegraf v1.15.0+

This plugin allows converting a tag or field containing a well-known port, either a number (e.g. `80`) for TCP ports or a port and protocol (e.g. `443/tcp`), to the registered service name.

[View](/telegraf/v1/processor-plugins/port_name/)

### Printer

Plugin ID: `processors.printer`
Telegraf v1.1.0+

This plugin prints every metric passing through it to the standard output.

[View](/telegraf/v1/processor-plugins/printer/)

### Regex

Plugin ID: `processors.regex`
Telegraf v1.7.0+

This plugin transforms tag and field *values* as well as renaming tags, fields and metrics using regular expression patterns. Tag and field *values* can be transformed using named-groups in a batch fashion.

The regex processor **only operates on string fields**. It will not work on any other data types, like an integer or float.

[View](/telegraf/v1/processor-plugins/regex/)

### Rename

Plugin ID: `processors.rename`
Telegraf v1.8.0+

This plugin allows to rename measurements, fields and tags.

[View](/telegraf/v1/processor-plugins/rename/)

### Reverse DNS

Plugin ID: `processors.reverse_dns`
Telegraf v1.15.0+

This plugin does a reverse-dns lookup on tags or fields containing IPs and creates a tag or field containing the corresponding DNS name.

[View](/telegraf/v1/processor-plugins/reverse_dns/)

### Round

Plugin ID: `processors.round`
Telegraf v1.36.0+

This plugin allows to round numerical field values to the configured precision. This is particularly useful in combination with the [dedup processor](/telegraf/v1/plugins/#processor-dedup) to reduce the number of metrics sent to the output if only a lower precision is required for the values.

[View](/telegraf/v1/processor-plugins/round/)

### S2 Geo

Plugin ID: `processors.s2geo`
Telegraf v1.14.0+

This plugin uses the WGS-84 coordinates in decimal degrees specified in the latitude and longitude fields and adds a tag with the corresponding S2 cell ID token of specified [cell level](https://s2geometry.io/resources/s2cell_statistics.html).

[View](/telegraf/v1/processor-plugins/s2geo/)

### Scale

Plugin ID: `processors.scale`
Telegraf v1.27.0+

This plugin allows to scale field-values from an input range into the given output range according to this formula:

Alternatively, you can apply a factor and offset to the input according to this formula

Input fields are converted to floating point values if possible. Otherwise, fields that cannot be converted are ignored and keep their original value.

Neither the input nor output values are clipped to their respective ranges!

[View](/telegraf/v1/processor-plugins/scale/)

### SNMP Lookup

Plugin ID: `processors.snmp_lookup`
Telegraf v1.30.0+

This plugin looks up extra information via SNMP and adds it to the metric as tags.

[View](/telegraf/v1/processor-plugins/snmp_lookup/)

### Split

Plugin ID: `processors.split`
Telegraf v1.28.0+

This plugin splits a metric up into one or more metrics based on a configured template. The resulting metrics will be timestamped according to the source metric. Templates can overlap, where a field or tag, is used across templates and as a result end up in multiple metrics.

If drop original is changed to true, then the plugin can result in dropping all metrics when no match is found! Please ensure to test templates before putting into production *and* use metric filtering to avoid data loss.

[View](/telegraf/v1/processor-plugins/split/)

### Starlark

Plugin ID: `processors.starlark`
Telegraf v1.15.0+

This plugin calls the provided Starlark function for each matched metric, allowing for custom programmatic metric processing.

The Starlark language is a dialect of Python, and will be familiar to those who have experience with the Python language. However, there are major differences. Existing Python code is unlikely to work unmodified. The execution environment is sandboxed, and it is not possible to do I/O operations such as reading from files or sockets.

The **[Starlark specification](https://github.com/google/starlark-go/blob/d1966c6b9fcd/doc/spec.md)** has details about the syntax and available functions.

[View](/telegraf/v1/processor-plugins/starlark/)

### Strings

Plugin ID: `processors.strings`
Telegraf v1.8.0+

This plugin allows to manipulate strings in the measurement name, tag and field values using different functions.

[View](/telegraf/v1/processor-plugins/strings/)

### Tag Limit

Plugin ID: `processors.tag_limit`
Telegraf v1.12.0+

This plugin ensures that only a certain number of tags are preserved for any given metric, and to choose the tags to preserve when the number of tags appended by the data source is over the limit.

This can be useful when dealing with output systems (e.g. Stackdriver) that impose hard limits on the number of tags/labels per metric or where high levels of cardinality are computationally and/or financially expensive.

[View](/telegraf/v1/processor-plugins/tag_limit/)

### Template

Plugin ID: `processors.template`
Telegraf v1.14.0+

This plugin applies templates to metrics for generating a new tag. The primary use case of this plugin is to create a tag that can be used for dynamic routing to multiple output plugins or using an output specific routing option.

The template has access to each metric’s measurement name, tags, fields, and timestamp. Templates follow the [Go Template syntax](https://golang.org/pkg/text/template/) and may contain [Sprig functions](http://masterminds.github.io/sprig/).

[View](/telegraf/v1/processor-plugins/template/)

### Timestamp

Plugin ID: `processors.timestamp`
Telegraf v1.31.0+

This plugin allows to parse fields containing timestamps into timestamps of other format.

[View](/telegraf/v1/processor-plugins/timestamp/)

### TopK

Plugin ID: `processors.topk`
Telegraf v1.7.0+

This plugin filters the top series over a period of time and calculates the top metrics via different aggregation functions. The processing steps comprise grouping the metrics based on the metric name and tags, computing the aggregate functions for each group every period and outputting the top `K` groups.

[View](/telegraf/v1/processor-plugins/topk/)

### Unpivot

Plugin ID: `processors.unpivot`
Telegraf v1.12.0+

This plugin allows to rotate a multi-field series into single-valued metrics. The resulting metrics allow to more easily aggregate data across fields.

To perform the reverse operation use the [pivot](/telegraf/v1/plugins/#processor-pivot) processor.

[View](/telegraf/v1/processor-plugins/unpivot/)

---

## Plugin directory

Telegraf is a plugin-driven agent that collects, processes, aggregates, and writes metrics. It supports four categories of plugins: input, output, aggregator, and processor. In addition to the included plugins, you can run *external plugins* that integrate with the Telegraf Execd processor plugin.

##### Plugin type

- Input
- Output
- Aggregator
- Processor

##### Plugin category

- Annotation
- Applications
- Cloud
- Containers
- Datastore
- Filtering
- General Purpose
- Grouping
- Hardware
- IoT
- Logging
- Math
- Messaging
- Network
- Sampling
- Server
- Statistics
- System
- Testing
- Transformation
- Web

##### Operating system

- FreeBSD
- Linux
- macOS
- Solaris
- Windows

##### Status

- New
- Deprecated

**Jump to:**

- [Input plugins](#input-plugins)
- [Output plugins](#output-plugins)
- [Aggregator plugins](#aggregator-plugins)
- [Processor plugins](#processor-plugins)

## Input plugins

Telegraf input plugins are used with the InfluxData time series platform to collect metrics from the system, services, or third-party APIs.

### ActiveMQ

Plugin ID: `inputs.activemq`
Telegraf v1.8.0+

This plugin gathers queue, topics and subscribers metrics using the Console API [ActiveMQ](https://activemq.apache.org/) message broker daemon.

[View](/telegraf/v1/input-plugins/activemq/)

### Aerospike

Plugin ID: `inputs.aerospike`
Telegraf v0.2.0 - v1.30.0 Deprecated

This plugin queries [Aerospike](https://www.aerospike.com) server(s) for node statistics and statistics on all configured namespaces.

As of version 1.30 the Aerospike plugin has been deprecated in favor of the prometheus plugin and the officially supported [Aerospike Prometheus Exporter](https://aerospike.com/docs/monitorstack/configure/configure-exporter)

For details on the measurements mean, please consult the [Aerospike Metrics Reference Docs](https://www.aerospike.com/docs/reference/metrics).

Metric names will have dashes (`-`) replaced as underscores (`_`) to make querying more consistently and easy.

All metrics are attempted to be cast to integers, then booleans, then strings in order.

[View](/telegraf/v1/input-plugins/aerospike/)

### Alibaba Cloud Monitor Service (Aliyun)

Plugin ID: `inputs.aliyuncms`
Telegraf v1.19.0+

This plugin gathers statistics from the [Alibaba / Aliyun cloud monitoring service](https://www.alibabacloud.com). In the following we will use `Aliyun` instead of `Alibaba` as it’s the default naming across the web console and docs.

[View](/telegraf/v1/input-plugins/aliyuncms/)

### AMD ROCm System Management Interface (SMI)

Plugin ID: `inputs.amd_rocm_smi`
Telegraf v1.20.0+

This plugin gathers statistics including memory and GPU usage, temperatures etc from [AMD ROCm platform](https://rocm.docs.amd.com/) GPUs.

The [`rocm-smi` binary](https://github.com/RadeonOpenCompute/rocm_smi_lib/tree/master/python_smi_tools) is required and needs to be installed on the system.

[View](/telegraf/v1/input-plugins/amd_rocm_smi/)

### AMQP Consumer

Plugin ID: `inputs.amqp_consumer`
Telegraf v1.3.0+

This plugin consumes messages from an Advanced Message Queuing Protocol v0.9.1 broker. A prominent implementation of this protocol is [RabbitMQ](https://www.rabbitmq.com).

Metrics are read from a topic exchange using the configured queue and binding key. The message payloads must be formatted in one of the supported [data formats](/telegraf/v1/data_formats/input).

For an introduction check the [AMQP concepts page](https://www.rabbitmq.com/tutorials/amqp-concepts.html) and the [RabbitMQ getting started guide](https://www.rabbitmq.com/getstarted.html).

[View](/telegraf/v1/input-plugins/amqp_consumer/)

### Apache

Plugin ID: `inputs.apache`
Telegraf v1.8.0+

This plugin collects performance information from [Apache HTTP Servers](https://httpd.apache.org) using the [`mod_status` module](https://httpd.apache.org/docs/current/mod/mod_status.html). Typically, this module is configured to expose a page at the `/server-status?auto` endpoint the server.

The [ExtendedStatus option](https://httpd.apache.org/docs/current/mod/core.html#extendedstatus) must be enabled in order to collect all available fields. For information about configuration of your server check the [module documentation](https://httpd.apache.org/docs/current/mod/mod_status.html).

[View](/telegraf/v1/input-plugins/apache/)

### APC UPSD

Plugin ID: `inputs.apcupsd`
Telegraf v1.12.0+

This plugin gathers data from one or more [apcupsd daemon](https://sourceforge.net/projects/apcupsd/) over the NIS network protocol. To query a server, the daemon must be running and be accessible.

[View](/telegraf/v1/input-plugins/apcupsd/)

### Apache Aurora

Plugin ID: `inputs.aurora`
Telegraf v1.7.0+

This plugin gathers metrics from [Apache Aurora](https://aurora.apache.org) schedulers. For monitoring recommendations check the [Monitoring your Aurora cluster](https://aurora.apache.org/documentation/latest/operations/monitoring) article.

[View](/telegraf/v1/input-plugins/aurora/)

### Azure Monitor

Plugin ID: `inputs.azure_monitor`
Telegraf v1.25.0+

This plugin gathers metrics of Azure resources using the [Azure Monitor](https://docs.microsoft.com/en-us/azure/azure-monitor) API. The plugin requires a `client_id`, `client_secret` and `tenant_id` for authentication via access token. The `subscription_id` is required for accessing Azure resources.

Check the [supported metrics page](https://docs.microsoft.com/en-us/azure/azure-monitor/essentials/metrics-supported) for available resource types and their metrics.

The Azure API has a read limit of 12,000 requests per hour. Please make sure you don’t exceed this limit with the total number of metrics you are in the configured interval.

[View](/telegraf/v1/input-plugins/azure_monitor/)

### Azure Queue Storage

Plugin ID: `inputs.azure_storage_queue`
Telegraf v1.13.0+

This plugin gathers queue sizes from the [Azure Queue Storage](https://learn.microsoft.com/en-us/azure/storage/queues) service, storing a large numbers of messages.

[View](/telegraf/v1/input-plugins/azure_storage_queue/)

### Bcache

Plugin ID: `inputs.bcache`
Telegraf v0.2.0+

This plugin gathers statistics for the [block layer cache](https://docs.kernel.org/admin-guide/bcache.html) from the `stats_total` directory and `dirty_data` file.

[View](/telegraf/v1/input-plugins/bcache/)

### Beanstalkd

Plugin ID: `inputs.beanstalkd`
Telegraf v1.8.0+

This plugin collects server statistics as well as tube statistics from a [Beanstalkd work queue](https://beanstalkd.github.io/) as reported by the `stats` and `stats-tube` server commands.

[View](/telegraf/v1/input-plugins/beanstalkd/)

### Beat

Plugin ID: `inputs.beat`
Telegraf v1.18.0+

This plugin will collect metrics from a [Beats](https://www.elastic.co/beats) instances. It is known to work with Filebeat and Kafkabeat.

[View](/telegraf/v1/input-plugins/beat/)

### BIND 9 Nameserver

Plugin ID: `inputs.bind`
Telegraf v1.11.0+

This plugin collects metrics from [BIND 9 nameservers](https://www.isc.org/bind) using the XML or JSON endpoint.

For *XML*, version 2 statistics (BIND 9.6 to 9.9) and version 3 statistics (BIND 9.9+) are supported. Version 3 statistics are the default and only XML format in BIND 9.10+.

For BIND 9.9 to support version 3 statistics, it must be built with the `--enable-newstats` compile flag, and the statistics must be specifically requested via the correct URL.

For *JSON*, version 1 statistics (BIND 9.10+) are supported. As of writing, some distros still do not enable support for JSON statistics in their BIND packages.

[View](/telegraf/v1/input-plugins/bind/)

### Bond

Plugin ID: `inputs.bond`
Telegraf v1.5.0+

This plugin collects metrics for both the network bond interface as well as its slave interfaces using `/proc/net/bonding/*` files.

[View](/telegraf/v1/input-plugins/bond/)

### Burrow

Plugin ID: `inputs.burrow`
Telegraf v1.7.0+

This plugin collect Kafka topic, consumer and partition status from the [Burrow - Kafka Consumer Lag Checking](https://github.com/linkedin/Burrow) companion via [HTTP API](https://github.com/linkedin/Burrow/wiki/HTTP-Endpoint). Burrow v1.x versions are supported.

[View](/telegraf/v1/input-plugins/burrow/)

### Ceph Storage

Plugin ID: `inputs.ceph`
Telegraf v0.13.1+

This plugin collects performance metrics from MON and OSD nodes in a [Ceph storage cluster](https://ceph.com). Support for Telegraf has been introduced in the v13.x Mimic release where data is sent to a socket (see [their documnetation](https://docs.ceph.com/en/latest/mgr/telegraf)).

[View](/telegraf/v1/input-plugins/ceph/)

### Control Group

Plugin ID: `inputs.cgroup`
Telegraf v1.0.0+

This plugin gathers statistics per [control group (cgroup)](https://docs.kernel.org/admin-guide/cgroup-v2.html).

Consider restricting paths to the set of cgroups you are interested in if you have a large number of cgroups, to avoid cardinality issues.

The plugin supports the *single value format* in the form

the *new line separated values format* in the form

the *space separated values format* in the form

and the *space separated keys and value, separated by new line format* in the form

[View](/telegraf/v1/input-plugins/cgroup/)

### chrony

Plugin ID: `inputs.chrony`
Telegraf v0.13.1+

This plugin queries metrics from a [chrony NTP server](https://chrony-project.org). For details on the meaning of the gathered fields please check the [chronyc manual](https://chrony-project.org/doc/4.4/chronyc.html).

[View](/telegraf/v1/input-plugins/chrony/)

### Cisco Model-Driven Telemetry (MDT)

Plugin ID: `inputs.cisco_telemetry_mdt`
Telegraf v1.11.0+

This plugin consumes [Cisco model-driven telemetry (MDT)](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9300-series-switches/model-driven-telemetry-wp.html) data from Cisco IOS XR, IOS XE and NX-OS platforms via TCP or GRPC. GRPC-based transport can utilize TLS for authentication and encryption. Telemetry data is expected to be GPB-KV (self-describing-gpb) encoded.

The GRPC dialout transport is supported on various IOS XR (64-bit) 6.1.x and later, IOS XE 16.10 and later, as well as NX-OS 7.x and later platforms. The TCP dialout transport is supported on IOS XR (32-bit and 64-bit) 6.1.x and later.

[View](/telegraf/v1/input-plugins/cisco_telemetry_mdt/)

### ClickHouse

Plugin ID: `inputs.clickhouse`
Telegraf v1.14.0+

This plugin gathers statistics data from a [ClickHouse server](https://github.com/ClickHouse/ClickHouse). Users on Clickhouse Cloud will not see the Zookeeper metrics as they may not have permissions to query those tables.

[View](/telegraf/v1/input-plugins/clickhouse/)

### Google Cloud PubSub

Plugin ID: `inputs.cloud_pubsub`
Telegraf v1.10.0+

This plugin consumes messages from the [Google Cloud PubSub](https://cloud.google.com/pubsub) service and creates metrics using one of the supported [data formats](/telegraf/v1/data_formats/input).

[View](/telegraf/v1/input-plugins/cloud_pubsub/)

### Google Cloud PubSub Push

Plugin ID: `inputs.cloud_pubsub_push`
Telegraf v1.10.0+

This plugin listens for messages sent via an HTTP POST from [Google Cloud PubSub](https://cloud.google.com/pubsub) and expects messages in Google’s Pub/Sub *JSON format*. The plugin allows Telegraf to serve as an endpoint of push service.

Google’s PubSub service will **only** send over HTTPS/TLS so this plugin must be behind a valid proxy or must be configured to use TLS by setting the `tls_cert` and `tls_key` accordingly.

Enable mutually authenticated TLS and authorize client connections by signing certificate authority by including a list of allowed CA certificate file names in `tls_allowed_cacerts`.

[View](/telegraf/v1/input-plugins/cloud_pubsub_push/)

### Amazon CloudWatch Statistics

Plugin ID: `inputs.cloudwatch`
Telegraf v0.12.1+

This plugin will gather metric statistics from [Amazon CloudWatch](https://aws.amazon.com/cloudwatch).

[View](/telegraf/v1/input-plugins/cloudwatch/)

### Amazon CloudWatch Metric Streams

Plugin ID: `inputs.cloudwatch_metric_streams`
Telegraf v1.24.0+

This plugin listens for metrics sent via HTTP by [Cloudwatch metric streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Streams.html) implementing the required [response specifications](https://docs.aws.amazon.com/firehose/latest/dev/httpdeliveryrequestresponse.html).

Using this plugin can incure costs, see the *Metric Streams example* in [CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing).

[View](/telegraf/v1/input-plugins/cloudwatch_metric_streams/)

### Netfilter Conntrack

Plugin ID: `inputs.conntrack`
Telegraf v1.0.0+

This plugin collects metrics from [Netfilter’s conntrack tools](https://conntrack-tools.netfilter.org/). There are two collection mechanisms for this plugin:

1. Extracting information from `/proc/net/stat/nf_conntrack` files if the `collect` option is set accordingly for finding CPU specific values.
2. Using specific files and directories by specifying the `dirs` option. At runtime, conntrack exposes many of those connection statistics within `/proc/sys/net`. Depending on your kernel version, these files can be found in either `/proc/sys/net/ipv4/netfilter` or `/proc/sys/net/netfilter` and will be prefixed with either `ip` or `nf`.

In order to simplify configuration in a heterogeneous environment, a superset of directory and filenames can be specified. Any locations that doesn’t exist is ignored.

[View](/telegraf/v1/input-plugins/conntrack/)

### Hashicorp Consul

Plugin ID: `inputs.consul`
Telegraf v1.0.0+

This plugin will collect statistics about all health checks registered in [Consul](https://www.consul.io) using the [Consul API](https://www.consul.io/docs/agent/http/health.html#health_state). The plugin will not report any [telemetry metrics](https://www.consul.io/docs/agent/telemetry.html) but Consul can report those statistics using the StatsD protocol if needed.

[View](/telegraf/v1/input-plugins/consul/)

### Hashicorp Consul Agent

Plugin ID: `inputs.consul_agent`
Telegraf v1.22.0+

This plugin collects metrics from a [Consul agent](https://developer.hashicorp.com/consul/commands/agent). Telegraf may be present in every node and connect to the agent locally. Tested on Consul v1.10.

[View](/telegraf/v1/input-plugins/consul_agent/)

### Couchbase

Plugin ID: `inputs.couchbase`
Telegraf v0.12.0+

This plugin collects metrics from [Couchbase](https://www.couchbase.com/), a distributed NoSQL database. Metrics are collected for each node, as well as detailed metrics for each bucket, for a given couchbase server.

[View](/telegraf/v1/input-plugins/couchbase/)

### Apache CouchDB

Plugin ID: `inputs.couchdb`
Telegraf v0.10.3+

This plugin gathers metrics from [Apache CouchDB](https://couchdb.apache.org/) instances using the [stats](http://docs.couchdb.org/en/1.6.1/api/server/common.html?highlight=stats#get--_stats) endpoint.

[View](/telegraf/v1/input-plugins/couchdb/)

### CPU

Plugin ID: `inputs.cpu`
Telegraf v0.1.5+

This plugin gathers metrics about the system’s CPUs.

[View](/telegraf/v1/input-plugins/cpu/)

### Counter-Strike Global Offensive (CSGO)

Plugin ID: `inputs.csgo`
Telegraf v1.18.0+

This plugin gather metrics from [Counter-Strike: Global Offensive](https://www.counter-strike.net/) servers.

[View](/telegraf/v1/input-plugins/csgo/)

### Bosch Rexroth ctrlX Data Layer

Plugin ID: `inputs.ctrlx_datalayer`
Telegraf v1.27.0+

This plugin gathers data from the [ctrlX Data Layer](https://ctrlx-automation.com) a communication middleware running on Bosch Rexroth’s [ctrlX CORE devices](https://ctrlx-core.com). The platform is used for professional automation applications like industrial automation, building automation, robotics, IoT Gateways or as classical PLC.

[View](/telegraf/v1/input-plugins/ctrlx_datalayer/)

### Mesosphere Distributed Cloud OS

Plugin ID: `inputs.dcos`
Telegraf v1.5.0+

This input plugin gathers metrics from a [Distributed Cloud OS](https://dcos.io/) cluster’s [metrics component](https://docs.mesosphere.com/1.10/metrics/).

Depending on the workload of your DC/OS cluster, this plugin can quickly create a high number of series which, when unchecked, can cause high load on your database!

[View](/telegraf/v1/input-plugins/dcos/)

### Directory Monitor

Plugin ID: `inputs.directory_monitor`
Telegraf v1.18.0+

This plugin monitors a single directory (traversing sub-directories), and processes each file placed in the directory. The plugin will gather all files in the directory at the configured interval, and parse the ones that haven’t been picked up yet.

Files should not be used by another process or the plugin may fail. Furthermore, files should not be written *live* to the monitored directory. If you absolutely must write files directly, they must be guaranteed to finish writing before `directory_duration_threshold`.

[View](/telegraf/v1/input-plugins/directory_monitor/)

### Disk

Plugin ID: `inputs.disk`
Telegraf v0.1.1+

This plugin gathers metrics about disk usage.

The `used_percent` field is calculated by `used / (used + free)` and *not* `used / total` as the unix `df` command does it. See [wikipedia - df](https://en.wikipedia.org/wiki/Df_\(Unix\)) for more details.

[View](/telegraf/v1/input-plugins/disk/)

### DiskIO

Plugin ID: `inputs.diskio`
Telegraf v0.10.0+

This plugin gathers metrics about disk traffic and timing.

[View](/telegraf/v1/input-plugins/diskio/)

### Disque

Plugin ID: `inputs.disque`
Telegraf v0.10.0+

This plugin gathers data from a [Disque](https://github.com/antirez/disque) instance, an experimental distributed, in-memory, message broker.

[View](/telegraf/v1/input-plugins/disque/)

### Device Mapper Cache

Plugin ID: `inputs.dmcache`
Telegraf v1.3.0+

This plugin provide a native collection for dmsetup based statistics for [dm-cache](https://docs.kernel.org/admin-guide/device-mapper/cache.html).

This plugin requires super-user permissions! Please make sure, Telegraf is able to run `sudo /sbin/dmsetup status --target cache` without requiring a password.

[View](/telegraf/v1/input-plugins/dmcache/)

### DNS Query

Plugin ID: `inputs.dns_query`
Telegraf v1.4.0+

This plugin gathers information about DNS queries such as response time and result codes.

[View](/telegraf/v1/input-plugins/dns_query/)

### Docker

Plugin ID: `inputs.docker`
Telegraf v0.1.9+

This plugin uses the [Docker Engine API](https://docs.docker.com/engine/api) to gather metrics on running Docker containers.

Make sure Telegraf has sufficient permissions to access the configured endpoint.

[View](/telegraf/v1/input-plugins/docker/)

### Docker Log

Plugin ID: `inputs.docker_log`
Telegraf v1.12.0+

This plugin uses the [Docker Engine API](https://docs.docker.com/engine/api) to gather logs from running Docker containers.

This plugin works only for containers with the `local` or `json-file` or `journald` logging driver. Make sure Telegraf has sufficient permissions to access the configured endpoint.

[View](/telegraf/v1/input-plugins/docker_log/)

### Dovecot

Plugin ID: `inputs.dovecot`
Telegraf v0.10.3+

This plugin uses the Dovecot [v2.1 stats protocol](https://doc.dovecot.org/configuration_manual/stats/old_statistics/#old-statistics) to gather metrics about configured domains of [Dovecot](https://www.dovecot.org/) servers. You can use this plugin on Dovecot up to and including version v2.3.x.

Dovecot v2.4+ has the old protocol removed and this plugin will not work. Please use Dovecot’s [Openmetrics exporter](https://doc.dovecot.org/latest/core/config/statistics.html#openmetrics) in combination with the [http input plugin](/telegraf/v1/plugins/#input-http) and `openmetrics` data format for newer versions of Dovecot.

[View](/telegraf/v1/input-plugins/dovecot/)

### Data Plane Development Kit (DPDK)

Plugin ID: `inputs.dpdk`
Telegraf v1.19.0+

This plugin collects metrics exposed by applications built with the [Data Plane Development Kit](https://www.dpdk.org) which is an extensive set of open source libraries designed for accelerating packet processing workloads.

Since DPDK will most likely run with root privileges, the telemetry socket exposed by DPDK will also require root access. Please adjust permissions accordingly!

Refer to the [Telemetry User Guide](https://doc.dpdk.org/guides/howto/telemetry.html) for details and examples on how to use DPDK in your application.

This plugin uses the `v2` interface to read telemetry > data from applications and required DPDK version `v20.05` or higher. Some metrics might require later versions. The recommended version, especially in conjunction with the `in_memory` option is `DPDK 21.11.2` or higher.

[View](/telegraf/v1/input-plugins/dpdk/)

### Amazon Elastic Container Service

Plugin ID: `inputs.ecs`
Telegraf v1.11.0+

This plugin gathers statistics on running containers in a Task from the [Amazon Elastic Container Service](https://aws.amazon.com/ecs/) using the [Amazon ECS metadata](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint.html) and the [v2](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v2.html) or [v3](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v3.html) statistics API endpoints.

The telegraf container must be run in the same Task as the workload it is inspecting.

The amazon-ecs-agent (though it *is* a container running on the host) is not present in the metadata/stats endpoints.

[View](/telegraf/v1/input-plugins/ecs/)

### Elasticsearch

Plugin ID: `inputs.elasticsearch`
Telegraf v0.1.5+

This plugin queries endpoints of a [Elasticsearch](https://www.elastic.co/) instance to obtain [node statistics](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-nodes-stats.html) and optionally [cluster-health](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-health.html) metrics. Additionally, the plugin is able to query [cluster](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-stats.html), [indices and shard](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-stats.html) statistics for the master node.

Specific statistics information can change between Elasticsearch versions. In general, this plugin attempts to stay as version-generic as possible by tagging high-level categories only and creating unique field names of whatever statistics names are provided at the mid-low level.

[View](/telegraf/v1/input-plugins/elasticsearch/)

### Elasticsearch Query

Plugin ID: `inputs.elasticsearch_query`
Telegraf v1.20.0+

This plugin allows to query an [Elasticsearch](https://www.elastic.co/) instance to obtain metrics from data stored in the cluster. The plugins supports counting the number of hits for a search query, calculating statistics for numeric fields, filtered by a query, aggregated per tag and to count the number of terms for a particular field.

This plugins supports Elasticsearch 5.x and 6.x but is known to break on 7.x or higher.

[View](/telegraf/v1/input-plugins/elasticsearch_query/)

### Ethtool

Plugin ID: `inputs.ethtool`
Telegraf v1.13.0+

This plugin collects ethernet device statistics. The available information strongly depends on the network device and driver.

[View](/telegraf/v1/input-plugins/ethtool/)

### Azure Event Hub Consumer

Plugin ID: `inputs.eventhub_consumer`
Telegraf v1.14.0+

This plugin allows consuming messages from [Azure Event Hubs](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-about) and [Azure IoT Hub](https://azure.microsoft.com/en-us/products/iot-hub) instances.

[View](/telegraf/v1/input-plugins/eventhub_consumer/)

### Exec

Plugin ID: `inputs.exec`
Telegraf v0.1.5+

This plugin executes the given `commands` on every interval and parses metrics from their output in any one of the supported [data formats](/telegraf/v1/data_formats/input). This plugin can be used to poll for custom metrics from any source.

[View](/telegraf/v1/input-plugins/exec/)

### Execd

Plugin ID: `inputs.execd`
Telegraf v1.14.0+

This plugin runs the given external program as a long-running daemon and collects the metrics in one of the supported [data formats](/telegraf/v1/data_formats/input) on the process’s `stdout`. The program is expected to stay running and output data when receiving the configured `signal`.

The `stderr` output of the process will be relayed to Telegraf’s logging facilities and will be logged as *error* by default. However, you can log to other levels by prefixing your message with `E!` for error, `W!` for warning, `I!` for info, `D!` for debugging and `T!` for trace levels followed by a space and the actual message. For example outputting `I! A log message` will create a `info` log line in your Telegraf logging output.

[View](/telegraf/v1/input-plugins/execd/)

### Fail2ban

Plugin ID: `inputs.fail2ban`
Telegraf v1.4.0+

This plugin gathers the count of failed and banned IP addresses using [fail2ban](https://www.fail2ban.org) by running the `fail2ban-client` command.

The `fail2ban-client` requires root access, so please make sure to either allow Telegraf to run that command using `sudo` without a password or by running telegraf as root (not recommended).

[View](/telegraf/v1/input-plugins/fail2ban/)

### Fibaro

Plugin ID: `inputs.fibaro`
Telegraf v1.7.0+

This plugin gathers data from devices connected to a [Fibaro](https://www.fibaro.com) controller. Those values could be true (1) or false (0) for switches, percentage for dimmers, temperature, etc. Both *Home Center 2* and *Home Center 3* devices are supported.

[View](/telegraf/v1/input-plugins/fibaro/)

### File

Plugin ID: `inputs.file`
Telegraf v1.8.0+

This plugin reads the **complete** contents of the configured files in **every** interval. The file content is split line-wise and parsed according to one of the supported [data formats](/telegraf/v1/data_formats/input).

If you wish to only process newly appended lines use the [tail](/telegraf/v1/plugins/#input-tail) input plugin instead.

[View](/telegraf/v1/input-plugins/file/)

### Filecount

Plugin ID: `inputs.filecount`
Telegraf v1.8.0+

This plugin reports the number and total size of files in specified directories.

[View](/telegraf/v1/input-plugins/filecount/)

### File statistics

Plugin ID: `inputs.filestat`
Telegraf v0.13.0+

This plugin gathers metrics about file existence, size, and other file statistics.

[View](/telegraf/v1/input-plugins/filestat/)

### Fireboard

Plugin ID: `inputs.fireboard`
Telegraf v1.12.0+

This plugin gathers real-time temperature data from [fireboard](https://www.fireboard.com) thermometers.

You will need to sign up to for the [Fireboard REST API](https://docs.fireboard.io/reference/restapi.html) in order to use this plugin.

[View](/telegraf/v1/input-plugins/fireboard/)

### AWS Data Firehose

Plugin ID: `inputs.firehose`
Telegraf v1.34.0+

This plugin listens for metrics sent via HTTP from [AWS Data Firehose](https://aws.amazon.com/de/firehose/) in one of the supported [data formats](/telegraf/v1/data_formats/input). The plugin strictly follows the request-response schema as describe in the official [documentation](https://docs.aws.amazon.com/firehose/latest/dev/httpdeliveryrequestresponse.html).

[View](/telegraf/v1/input-plugins/firehose/)

### Fluentd

Plugin ID: `inputs.fluentd`
Telegraf v1.4.0+

This plugin gathers internal metrics of a [fluentd](https://www.fluentd.org/) instance provided by fluentd’s [monitor agent plugin](https://docs.fluentd.org/input/monitor_agent). Data provided by the `/api/plugin.json` resource, `/api/config.json` is not covered.

This plugin might produce high-cardinality series as the `plugin_id` value is random after each restart of fluentd. You might need to adjust your fluentd configuration, in order to reduce series cardinality in case your fluentd restarts frequently by adding the `@id` parameter to each plugin. See [fluentd’s documentation](https://docs.fluentd.org/configuration/config-file#common-plugin-parameter) for details.

[View](/telegraf/v1/input-plugins/fluentd/)

### Fritzbox

Plugin ID: `inputs.fritzbox`
Telegraf v1.35.0+

This plugin gathers status information from [AVM](https://en.avm.de/) devices (routers, repeaters, etc) using the device’s [TR-064](https://avm.de/service/schnittstellen/) interface.

[View](/telegraf/v1/input-plugins/fritzbox/)

### GitHub

Plugin ID: `inputs.github`
Telegraf v1.11.0+

This plugin gathers information from projects and repositories hosted on [GitHub](https://www.github.com).

Telegraf also contains the [webhook input plugin](/telegraf/v1/plugins/#input-webhooks) which can be used as an alternative method for collecting repository information.

[View](/telegraf/v1/input-plugins/github/)

### gNMI (gRPC Network Management Interface)

Plugin ID: `inputs.gnmi`
Telegraf v1.15.0+

This plugin consumes telemetry data based on [gNMI](https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md) subscriptions. TLS is supported for authentication and encryption. This plugin is vendor-agnostic and is supported on any platform that supports the gNMI specification.

For Cisco devices the plugin has been optimized to support gNMI telemetry as produced by Cisco IOS XR (64-bit) version 6.5.1, Cisco NX-OS 9.3 and Cisco IOS XE 16.12 and later.

[View](/telegraf/v1/input-plugins/gnmi/)

### Google Cloud Storage

Plugin ID: `inputs.google_cloud_storage`
Telegraf v1.25.0+

This plugin will collect metrics from the given [Google Cloud Storage](https://cloud.google.com/storage) buckets in any of the supported [data formats](/telegraf/v1/data_formats/input).

[View](/telegraf/v1/input-plugins/google_cloud_storage/)

### GrayLog

Plugin ID: `inputs.graylog`
Telegraf v1.0.0+

This plugin collects data from [Graylog servers](https://graylog.org/), currently supporting two type of end points `multiple` (e.g. `http://<host>:9000/api/system/metrics/multiple`) and `namespace` (e.g. `http://<host>:9000/api/system/metrics/namespace/{namespace}`).

Multiple endpoint can be queried and mixing `multiple` and serveral `namespace` end points is possible. Check `http://<host>:9000/api/api-browser` for the full list of available endpoints.

When specifying a `namespace` endpoint without an actual namespace, the metrics array will be ignored.

[View](/telegraf/v1/input-plugins/graylog/)

### HAProxy

Plugin ID: `inputs.haproxy`
Telegraf v0.1.5+

This plugin gathers statistics of [HAProxy](http://www.haproxy.org/) servers using sockets or the HTTP protocol.

[View](/telegraf/v1/input-plugins/haproxy/)

### HDDtemp

Plugin ID: `inputs.hddtemp`
Telegraf v1.0.0+

This plugin reads data from a [hddtemp](https://savannah.nongnu.org/projects/hddtemp/) daemon.

This plugin requires `hddtemp` to be installed and running as a daemon.

As the upstream project is not activly maintained anymore and various distributions (e.g. Debian Bookwork and later) don’t ship packages for `hddtemp` anymore, the binary might not be available (e.g. in Ubuntu 22.04 or later).

As an alternative consider using the [smartctl](/telegraf/v1/plugins/#input-smartctl) relying on SMART information or [sensors](/telegraf/v1/plugins/#input-sensors) plugins to retrieve temperature data of your hard-drive.

[View](/telegraf/v1/input-plugins/hddtemp/)

### HTTP

Plugin ID: `inputs.http`
Telegraf v1.6.0+

This plugin collects metrics from one or more HTTP endpoints providing data in one of the supported [data formats](/telegraf/v1/data_formats/input).

[View](/telegraf/v1/input-plugins/http/)

### HTTP Listener v2

Plugin ID: `inputs.http_listener_v2`
Telegraf v1.9.0+

This plugin listens for metrics sent via HTTP in any of the supported [data formats](/telegraf/v1/data_formats/input).

If you would like Telegraf to act as a proxy/relay for InfluxDB v1 or InfluxDB v2 it is recommended to use the [influxdb\_\_listener](/telegraf/v1/plugins/#input-influxdb_listener) or [influxdb\_v2\_listener](/telegraf/v1/plugins/#input-influxdb_v2_listener) plugin instead.

[View](/telegraf/v1/input-plugins/http_listener_v2/)

### HTTP Response

Plugin ID: `inputs.http_response`
Telegraf v0.12.1+

This plugin generates metrics from HTTP responses including the status code and response statistics.

[View](/telegraf/v1/input-plugins/http_response/)

### HueBridge

Plugin ID: `inputs.huebridge`
Telegraf v1.34.0+

This plugin gathers status from [Hue Bridge](https://www.philips-hue.com/) devices using the [CLIP API](https://developers.meethue.com/develop/hue-api-v2/) interface of the devices.

[View](/telegraf/v1/input-plugins/huebridge/)

### Hugepages

Plugin ID: `inputs.hugepages`
Telegraf v1.22.0+

This plugin gathers metrics from the Linux’ [Transparent Huge Pages (THP) memory management system](https://www.kernel.org/doc/html/latest/admin-guide/mm/hugetlbpage.html) that reduces the overhead of Translation Lookaside Buffer (TLB) lookups on machines with large amounts of memory.

[View](/telegraf/v1/input-plugins/hugepages/)

### Icinga2

Plugin ID: `inputs.icinga2`
Telegraf v1.8.0+

This plugin gather services and hosts status information using the [Icinga2 remote API](https://docs.icinga.com/icinga2/latest/doc/module/icinga2/chapter/icinga2-api).

[View](/telegraf/v1/input-plugins/icinga2/)

### InfiniBand

Plugin ID: `inputs.infiniband`
Telegraf v1.14.0+

This plugin gathers statistics for all InfiniBand devices and ports on the system. These are the counters that can be found in `/sys/class/infiniband/<dev>/port/<port>/counters/` and RDMA counters can be found in `/sys/class/infiniband/<dev>/ports/<port>/hw_counters/`

[View](/telegraf/v1/input-plugins/infiniband/)

### InfluxDB

Plugin ID: `inputs.influxdb`
Telegraf v0.2.5+

This plugin collects metrics on the given InfluxDB v1 servers from the `/debug/vars` endpoint. Read the [documentation](https://docs.influxdata.com/platform/monitoring/influxdata-platform/tools/measurements-internal/) for detailed information about `influxdb` metrics.

Additionally, this plugin can gather metrics from endpoints exposing InfluxDB-formatted endpoints.

To gather [InfluxDB v2 metrics](https://docs.influxdata.com/influxdb/latest/reference/internals/metrics/) use the [prometheus plugin](/telegraf/v1/plugins/#input-prometheus) with\[\[inputs.prometheus\]\] urls = \[“http://localhost:8086/metrics”\] metric\_version = 1

[View](/telegraf/v1/input-plugins/influxdb/)

### InfluxDB Listener

Plugin ID: `inputs.influxdb_listener`
Telegraf v1.9.0+

This plugin listens for requests sent according to the [InfluxDB HTTP v1 API](https://docs.influxdata.com/influxdb/v1.8/guides/write_data/). This allows Telegraf to serve as a proxy/router for the `/write` endpoint of the InfluxDB HTTP API.

This plugin was previously known as `http_listener`. If you wish to send general metrics via HTTP it is recommended to use the [`http_listener_v2`](/telegraf/v1/plugins/#input-http_listener_v2) instead.

The `/write` endpoint supports the `precision` query parameter and can be set to one of `ns`, `u`, `ms`, `s`, `m`, `h`. All other parameters are ignored and defer to the output plugins configuration.

When chaining Telegraf instances using this plugin, `CREATE DATABASE` requests receive a `200 OK` response with message body `{"results":[]}` but they are not relayed. The configuration of the output plugin ultimately submits data to InfluxDB determines the destination database.

[View](/telegraf/v1/input-plugins/influxdb_listener/)

### InfluxDB V2 Listener

Plugin ID: `inputs.influxdb_v2_listener`
Telegraf v1.16.0+

This plugin listens for requests sent according to the [InfluxDB HTTP v2 API](https://docs.influxdata.com/influxdb/v2/api/). This allows Telegraf to serve as a proxy/router for the `/api/v2/write` endpoint of the InfluxDB HTTP API.

The `/api/v2/write` endpoint supports the `precision` query parameter and can be set to one of `ns`, `us`, `ms`, `s`. All other parameters are ignored and defer to the output plugins configuration.

[View](/telegraf/v1/input-plugins/influxdb_v2_listener/)

### Intel Baseband Accelerator

Plugin ID: `inputs.intel_baseband`
Telegraf v1.27.0+

This plugin collects metrics from both dedicated and integrated Intel devices providing Wireless Baseband hardware acceleration. These devices play a key role in accelerating 5G and 4G Virtualized Radio Access Networks (vRAN) workloads, increasing the overall compute capacity of commercial, off-the-shelf platforms by integrating e.g.

- Forward Error Correction (FEC) processing,
- 4G Turbo FEC processing,
- 5G Low Density Parity Check (LDPC)
- Fast Fourier Transform (FFT) block providing DFT/iDFT processing offload for the 5G Sounding Reference Signal (SRS)

[View](/telegraf/v1/input-plugins/intel_baseband/)

### Intel® Dynamic Load Balancer

Plugin ID: `inputs.intel_dlb`
Telegraf v1.25.0+

This plugin collects metrics exposed by applications built with the [Data Plane Development Kit](https://www.dpdk.org/), an extensive set of open source libraries designed for accelerating packet processing workloads, plugin is also using bifurcated driver. More specifically it’s targeted for applications using Intel DLB as eventdev devices accessed via bifurcated driver (allowing access from kernel and user-space).

[View](/telegraf/v1/input-plugins/intel_dlb/)

### Intel® Platform Monitoring Technology

Plugin ID: `inputs.intel_pmt`
Telegraf v1.28.0+

This plugin collects metrics via the Linux kernel driver for Intel® Platform Monitoring Technology (Intel® PMT), an architecture capable of enumerating and accessing hardware monitoring capabilities on supported devices.

[View](/telegraf/v1/input-plugins/intel_pmt/)

### Intel Performance Monitoring Unit

Plugin ID: `inputs.intel_pmu`
Telegraf v1.21.0+

This plugin gathers Intel Performance Monitoring Unit metrics available via the [Linux Perf](https://perf.wiki.kernel.org/index.php/Main_Page) subsystem.

PMU metrics provide insights into performance and health of IA processors’ internal components, including core and uncore units. With the number of cores increasing and processor topology getting more complex the insight into those metrics is vital to assure the best CPU performance and utilization.

Performance counters are CPU hardware registers that count hardware events such as instructions executed, cache-misses suffered, or branches mispredicted. They form a basis for profiling applications to trace dynamic control flow and identify hotspots.

[View](/telegraf/v1/input-plugins/intel_pmu/)

### Intel PowerStat

Plugin ID: `inputs.intel_powerstat`
Telegraf v1.17.0+

This plugin gathers power statistics on Intel-based platforms providing insights into power saving and workload migration. Those are beneficial for Monitoring and Analytics systems to take preventive or corrective actions based on platform busyness, CPU temperature, actual CPU utilization and power statistics.

[View](/telegraf/v1/input-plugins/intel_powerstat/)

### Intel RDT

Plugin ID: `inputs.intel_rdt`
Telegraf v1.16.0+

This plugin collects information provided by monitoring features of the [Intel Resource Director Technology](https://www.intel.com/content/www/us/en/architecture-and-technology/resource-director-technology.html), a hardware framework to monitor and control the utilization of shared resources (e.g. last level cache, memory bandwidth).

Intel’s Resource Director Technology (RDT) framework consists of:

- Cache Monitoring Technology (CMT)
- Memory Bandwidth Monitoring (MBM)
- Cache Allocation Technology (CAT)
- Code and Data Prioritization (CDP)

As multithreaded and multicore platform architectures emerge, the last level cache and memory bandwidth are key resources to manage for running workloads in single-threaded, multithreaded, or complex virtual machine environments. Intel introduces CMT, MBM, CAT and CDP to manage these workloads across shared resources.

[View](/telegraf/v1/input-plugins/intel_rdt/)

### Telegraf Internal

Plugin ID: `inputs.internal`
Telegraf v1.2.0+

This plugin collects metrics about the telegraf agent and its plugins.

Some metrics are aggregates across all instances of a plugin type.

[View](/telegraf/v1/input-plugins/internal/)

### Internet Speed Monitor

Plugin ID: `inputs.internet_speed`
Telegraf v1.20.0+

This plugin collects metrics about the internet speed on the system like download/upload speed, latency etc using the [speedtest.net service](https://www.speedtest.net/).

[View](/telegraf/v1/input-plugins/internet_speed/)

### Interrupts

Plugin ID: `inputs.interrupts`
Telegraf v1.3.0+

This plugin gathers metrics about IRQs from interrupts (`/proc/interrupts`) and soft-interrupts (`/proc/softirqs`).

[View](/telegraf/v1/input-plugins/interrupts/)

### IPMI Sensor

Plugin ID: `inputs.ipmi_sensor`
Telegraf v0.12.0+

This plugin gathers metrics from the [Intelligent Platform Management Interface](https://www.intel.com/content/dam/www/public/us/en/documents/specification-updates/ipmi-intelligent-platform-mgt-interface-spec-2nd-gen-v2-0-spec-update.pdf) using the [`ipmitool`](https://github.com/ipmitool/ipmitool) command line utility.

The `ipmitool` requires access to the IPMI device. Please check the permission section for possible solutions.

[View](/telegraf/v1/input-plugins/ipmi_sensor/)

### Ipset

Plugin ID: `inputs.ipset`
Telegraf v1.6.0+

This plugin gathers packets and bytes counters from [Linux IP sets](https://ipset.netfilter.org/) using the `ipset` command line tool.

IP sets created without the “counters” option are ignored.

[View](/telegraf/v1/input-plugins/ipset/)

### Iptables

Plugin ID: `inputs.iptables`
Telegraf v1.1.0+

This plugin gathers packets and bytes counters for rules within a set of table and chain from the Linux’s iptables firewall.

Rules are identified through associated comment, so you must ensure that the rules you want to monitor do have a **unique** comment using the `--comment` flag when adding them. Rules without comments are ignored.

The rule number cannot be used as identifier as it is not constant and may vary when rules are inserted/deleted at start-up or by automatic tools (interactive firewalls, fail2ban, …).

The `iptables` command requires `CAP_NET_ADMIN` and `CAP_NET_RAW` capabilities. Check the permissions section for ways to grant them.

[View](/telegraf/v1/input-plugins/iptables/)

### IPVS

Plugin ID: `inputs.ipvs`
Telegraf v1.9.0+

This plugin gathers metrics about the [IPVS virtual and real servers](http://www.linuxvirtualserver.org/software/ipvs.html) using the netlink socket interface of the Linux kernel.

The plugin requires `CAP_NET_ADMIN` and `CAP_NET_RAW` capabilities. Check the permissions section for ways to grant them.

[View](/telegraf/v1/input-plugins/ipvs/)

### Jenkins

Plugin ID: `inputs.jenkins`
Telegraf v1.9.0+

This plugin gathers information about the nodes and jobs running in a [Jenkins](https://www.jenkins.io/) instance. The plugin uses the Jenkins API and does not require a plugin on the server.

[View](/telegraf/v1/input-plugins/jenkins/)

### Jolokia2 Agent

Plugin ID: `inputs.jolokia2_agent`
Telegraf v1.5.0+

This plugin reads JMX metrics from one or more [Jolokia agent](https://jolokia.org/agent/jvm.html) REST endpoints.

[View](/telegraf/v1/input-plugins/jolokia2_agent/)

### Jolokia2 Proxy

Plugin ID: `inputs.jolokia2_proxy`
Telegraf v1.5.0+

This plugin reads JMX metrics from one or more *targets* by interacting with a [Jolokia proxy](https://jolokia.org/features/proxy.html) REST endpoint.

[View](/telegraf/v1/input-plugins/jolokia2_proxy/)

### Juniper Telemetry

Plugin ID: `inputs.jti_openconfig_telemetry`
Telegraf v1.7.0+

This service plugin reads [OpenConfig](http://openconfig.net/) telemetry data via the [Junos Telemetry Interface (JTI)](https://www.juniper.net/documentation/en_US/junos/topics/concept/junos-telemetry-interface-oveview.html) from configured from listed sensors.

[View](/telegraf/v1/input-plugins/jti_openconfig_telemetry/)

### Apache Kafka Consumer

Plugin ID: `inputs.kafka_consumer`
Telegraf v0.2.3+

This service plugin consumes messages from [Kafka brokers](https://kafka.apache.org) in one of the supported [data formats](/telegraf/v1/data_formats/input). The plugin uses [consumer groups](http://godoc.org/github.com/wvanbergen/kafka/consumergroup) when talking to the Kafka cluster so multiple instances of Telegraf can consume messages from the same topic in parallel.

[View](/telegraf/v1/input-plugins/kafka_consumer/)

### Kapacitor

Plugin ID: `inputs.kapacitor`
Telegraf v1.3.0+

This plugin collects metrics from the configured [InfluxData Kapacitor](https://www.influxdata.com/time-series-platform/kapacitor/) instances.

[View](/telegraf/v1/input-plugins/kapacitor/)

### Kernel

Plugin ID: `inputs.kernel`
Telegraf v0.11.0+

This plugin gathers metrics about the [Linux kernel](https://kernel.org/) including, among others, the [available entropy](https://www.kernel.org/doc/html/latest/admin-guide/sysctl/kernel.html#random), [Kernel Samepage Merging](https://www.kernel.org/doc/html/latest/mm/ksm.html) and [Pressure Stall Information](https://www.kernel.org/doc/html/latest/accounting/psi.html).

[View](/telegraf/v1/input-plugins/kernel/)

### Kernel VM Statistics

Plugin ID: `inputs.kernel_vmstat`
Telegraf v1.0.0+

This plugin gathers virtual memory statistics of the [Linux kernel](https://kernel.org/) by reading `/proc/vmstat`. For a full list of available fields check the `/proc/vmstat` section of the [proc man page](http://man7.org/linux/man-pages/man5/proc.5.html) and for a detailed description about the fields see the [vmstat man page](https://man7.org/linux/man-pages/man8/vmstat.8.html).

[View](/telegraf/v1/input-plugins/kernel_vmstat/)

### Kibana

Plugin ID: `inputs.kibana`
Telegraf v1.8.0+

This plugin collects metrics about service status from [Kibana](https://www.elastic.co/kibana) instances via the server’s API.

This plugin requires Kibana version 6.0+.

[View](/telegraf/v1/input-plugins/kibana/)

### Kinesis Consumer

Plugin ID: `inputs.kinesis_consumer`
Telegraf v1.10.0+

This service input plugin consumes messages from [AWS Kinesis](https://aws.amazon.com/kinesis/) data stream in one of the supported [data formats](/telegraf/v1/data_formats/input).

[View](/telegraf/v1/input-plugins/kinesis_consumer/)

### KNX

Plugin ID: `inputs.knx_listener`
Telegraf v1.19.0+

This service plugin listens for messages on the [KNX home-automation bus](https://www.knx.org) by connecting via a KNX-IP interface. Information about supported KNX datapoint-types can be found at the underlying [`knx-go` project](https://github.com/vapourismo/knx-go).

[View](/telegraf/v1/input-plugins/knx_listener/)

### Kubernetes Inventory

Plugin ID: `inputs.kube_inventory`
Telegraf v1.10.0+

This plugin gathers metrics from [Kubernetes](https://kubernetes.io/) resources.

This plugin requires Kubernetes version 1.11+.

The gathered resources include for example daemon sets, deployments, endpoints, ingress, nodes, persistent volumes and many more.

This plugin produces high cardinality data, which when not controlled for will cause high load on your database. Please make sure to [filter](/telegraf/v1/configuration/#metric-filtering) the produced metrics or configure your database to avoid cardinality issues!

[View](/telegraf/v1/input-plugins/kube_inventory/)

### Kubernetes

Plugin ID: `inputs.kubernetes`
Telegraf v1.1.0+

This plugin gathers metrics about running pods and containers of a [Kubernetes](https://kubernetes.io/) instance via the Kubelet API.

This plugin has to run as part of a `daemonset` within a Kubernetes installation. Telegraf must run on every node within the cluster.

You should configure this plugin to talk to its locally running kubelet.

This plugin produces high cardinality data, which when not controlled for will cause high load on your database. Please make sure to [filter](/telegraf/v1/configuration/#metric-filtering) the produced metrics or configure your database to avoid cardinality issues!

[View](/telegraf/v1/input-plugins/kubernetes/)

### Arista LANZ Consumer

Plugin ID: `inputs.lanz`
Telegraf v1.14.0+

This service plugin consumes messages from the [Arista Networks’ Latency Analyzer (LANZ)](https://www.arista.com/en/um-eos/eos-latency-analyzer-lanz) by receiving the datastream on TCP (usually through port 50001) on the switch’s management IP.

You will need to configure LANZ and enable streaming LANZ data, see the [documentation](https://www.arista.com/en/um-eos/eos-section-44-3-configuring-lanz) for more details.

[View](/telegraf/v1/input-plugins/lanz/)

### LDAP

Plugin ID: `inputs.ldap`
Telegraf v1.29.0+

This plugin gathers metrics from LDAP servers’ monitoring (`cn=Monitor`) backend. Currently this plugin supports [OpenLDAP](https://www.openldap.org/) and [389ds](https://www.port389.org/) servers.

[View](/telegraf/v1/input-plugins/ldap/)

### LeoFS

Plugin ID: `inputs.leofs`
Telegraf v0.1.5+

This plugin gathers metrics of the [LEO filesystem](https://leo-project.net/leofs/) services *LeoGateway*, *LeoManager*, and *LeoStorage* via SNMP. Check the [LeoFS system monitoring documentation](https://leo-project.net/leofs/docs/admin/system_admin/monitoring/) for details.

[View](/telegraf/v1/input-plugins/leofs/)

### Libvirt

Plugin ID: `inputs.libvirt`
Telegraf v1.25.0+

This plugin collects statistics about virtualized guests on a system by using the [libvirt](https://libvirt.org/) virtualization API. Metrics are gathered directly from the hypervisor on a host system, so Telegraf doesn’t have to be installed and configured on a guest system.

[View](/telegraf/v1/input-plugins/libvirt/)

### Linux CPU

Plugin ID: `inputs.linux_cpu`
Telegraf v1.24.0+

This plugin gathers CPU metrics exposed on [Linux](https://kernel.org/) systems.

[View](/telegraf/v1/input-plugins/linux_cpu/)

### Linux Sysctl Filesystem

Plugin ID: `inputs.linux_sysctl_fs`
Telegraf v1.24.0+

This plugin gathers metrics by reading the [system filesystem](https://www.kernel.org/doc/Documentation/sysctl/fs.txt) files on [Linux](https://kernel.org/) systems.

[View](/telegraf/v1/input-plugins/linux_sysctl_fs/)

### LogQL

Plugin ID: `inputs.logql`
Telegraf v1.37.0+

This plugin gathers metrics from a [Loki](https://grafana.com/oss/loki/) endpoint using [LogQL queries](https://grafana.com/docs/loki/latest/query/) via the [HTTP API](https://grafana.com/docs/loki/latest/reference/loki-http-api/).

[View](/telegraf/v1/input-plugins/logql/)

### Logstash

Plugin ID: `inputs.logstash`
Telegraf v1.12.0+

This plugin gathers metrics from a [Logstash](https://www.elastic.co/logstash) endpoint using the [Monitoring API](https://www.elastic.co/guide/en/logstash/current/monitoring-logstash.html).

This plugin supports Logstash 5+.

[View](/telegraf/v1/input-plugins/logstash/)

### Lustre

Plugin ID: `inputs.lustre2`
Telegraf v0.1.5+

This plugin gathers metrics for the [Lustre® file system](http://lustre.org/) using its entries in the `proc` filesystem. Reference the [Lustre Monitoring and Statistics Guide](http://wiki.lustre.org/Lustre_Monitoring_and_Statistics_Guide) for the reported information.

This plugin doesn’t report *all* information available but only a limited set of items. Check the metrics section.

[View](/telegraf/v1/input-plugins/lustre2/)

### Logical Volume Manager

Plugin ID: `inputs.lvm`
Telegraf v1.21.0+

This plugin collects information about physical volumes, volume groups and logical volumes from the Logical Volume Management (LVM) of the [Linux kernel](https://www.kernel.org/).

[View](/telegraf/v1/input-plugins/lvm/)

### Mailchimp

Plugin ID: `inputs.mailchimp`
Telegraf v0.2.4+

This plugin gathers metrics from the [Mailchimp](https://mailchimp.com) service using the [Mailchimp API](https://developer.mailchimp.com/).

[View](/telegraf/v1/input-plugins/mailchimp/)

### MarkLogic

Plugin ID: `inputs.marklogic`
Telegraf v1.12.0+

This plugin gathers health status metrics from one or more [MarkLogic](https://www.progress.com/marklogic) hosts.

[View](/telegraf/v1/input-plugins/marklogic/)

### MavLink

Plugin ID: `inputs.mavlink`
Telegraf v1.35.0+

This plugin collects metrics from [MavLink](https://mavlink.io/)\-compatible flight controllers such as [ArduPilot](https://ardupilot.org/) or [PX4](https://px4.io/) to live ingest flight metrics from unmanned systems (drones, planes, boats, etc.) Currently the ArduPilot-specific Mavlink dialect is used, check the [Mavlink documentation](https://mavlink.io/en/messages/ardupilotmega.html) for more details and the various messages available.

This plugin potentially generates a large amount of data. If your output plugin cannot handle the rate of messages, use [Metric filters](/telegraf/v1/configuration/#metric-filtering) to limit the metrics written to outputs, and/or the `filters` configuration parameter to limit which Mavlink messages this plugin parses.

[View](/telegraf/v1/input-plugins/mavlink/)

### Mcrouter

Plugin ID: `inputs.mcrouter`
Telegraf v1.7.0+

This plugin gathers statistics data from [Mcrouter](https://github.com/facebook/mcrouter) instances, a protocol router, developed and maintained by Facebook, for scaling [memcached](http://memcached.org/) deployments.

[View](/telegraf/v1/input-plugins/mcrouter/)

### MD RAID Statistics

Plugin ID: `inputs.mdstat`
Telegraf v1.20.0+

This plugin gathers statistics about any [Linux MD RAID arrays](https://docs.kernel.org/admin-guide/md.html) configured on the host by reading `/proc/mdstat`. For a full list of available fields see the `/proc/mdstat` section of the [proc man page](http://man7.org/linux/man-pages/man5/proc.5.html). For details on the fields check the [mdstat wiki](https://raid.wiki.kernel.org/index.php/Mdstat).

[View](/telegraf/v1/input-plugins/mdstat/)

### Memory

Plugin ID: `inputs.mem`
Telegraf v0.1.5+

This plugin collects metrics about the system memory.

For an explanation of the difference between *used* and *actual\_used* RAM, see [Linux ate my ram](http://www.linuxatemyram.com/).

[View](/telegraf/v1/input-plugins/mem/)

### Memcached

Plugin ID: `inputs.memcached`
Telegraf v0.1.2+

This plugin gathers statistics data from [Memcached](https://memcached.org/) instances.

[View](/telegraf/v1/input-plugins/memcached/)

### Apache Mesos

Plugin ID: `inputs.mesos`
Telegraf v0.10.3+

This plugin gathers metrics from [Apache Mesos](https://mesos.apache.org/) instances. For more information, please check the [Mesos Observability Metrics](http://mesos.apache.org/documentation/latest/monitoring/) page.

[View](/telegraf/v1/input-plugins/mesos/)

### Minecraft

Plugin ID: `inputs.minecraft`
Telegraf v1.4.0+

This plugin collects score metrics from a [Minecraft](https://www.minecraft.net/) server using the RCON protocol.

This plugin supports Minecraft Java Edition versions 1.11 - 1.14. When using a version earlier than 1.13, be aware that the values for some criteria has changed and need to be modified.

[View](/telegraf/v1/input-plugins/minecraft/)

### Mock Data

Plugin ID: `inputs.mock`
Telegraf v1.22.0+

The plugin generates mock-metrics based on different algorithms like sine-wave functions, random numbers and more with the configured names and tags. Those metrics are usefull during testing (e.g. processors) or if random data is required.

[View](/telegraf/v1/input-plugins/mock/)

### Modbus

Plugin ID: `inputs.modbus`
Telegraf v1.14.0+

This plugin collects data from [Modbus](https://www.modbus.org/) registers using e.g. Modbus TCP or serial interfaces with Modbus RTU or Modbus ASCII.

[View](/telegraf/v1/input-plugins/modbus/)

### MongoDB

Plugin ID: `inputs.mongodb`
Telegraf v0.1.5+

This plugin collects metrics about [MongoDB](https://www.mongodb.com) server instances by running database commands.

This plugin supports all versions marked as supported in the [MongoDB Software Lifecycle Schedules](https://www.mongodb.com/support-policy/lifecycles).

[View](/telegraf/v1/input-plugins/mongodb/)

### Monit

Plugin ID: `inputs.monit`
Telegraf v1.14.0+

This plugin gathers metrics and status information about local processes, remote hosts, files, file systems, directories and network interfaces managed and watched over by [Monit](https://mmonit.com/).

The plugin supports Monit version 5.16+. To use this plugin you have to enable the [HTTPD TCP port](https://mmonit.com/monit/documentation/monit.html#TCP-PORT) in Monit.

[View](/telegraf/v1/input-plugins/monit/)

### MQTT Consumer

Plugin ID: `inputs.mqtt_consumer`
Telegraf v0.10.3+

This service plugin consumes messages from [MQTT](https://mqtt.org) brokers for the configured topics in one of the supported [data formats](/telegraf/v1/data_formats/input).

[View](/telegraf/v1/input-plugins/mqtt_consumer/)

### Multifile

Plugin ID: `inputs.multifile`
Telegraf v1.10.0+

This plugin reads the combined data from multiple files into a single metric, creating one field or tag per file. This is often useful creating custom metrics from the `/sys` or `/proc` filesystems.

To parse metrics from a single file you should use the [file](/telegraf/v1/plugins/#input-file) input plugin instead.

[View](/telegraf/v1/input-plugins/multifile/)

### MySQL

Plugin ID: `inputs.mysql`
Telegraf v0.1.1+

This plugin gathers statistics from [MySQL](https://www.mysql.com/) server instances.

To gather metrics from the performance schema, it must first be enabled in MySQL. See the performance schema [quick start](https://dev.mysql.com/doc/refman/8.0/en/performance-schema-quick-start.html) for details.

[View](/telegraf/v1/input-plugins/mysql/)

### NATS Server Monitoring

Plugin ID: `inputs.nats`
Telegraf v1.6.0+

This plugin gathers metrics of a [NATS](http://www.nats.io) server instance using its [monitoring endpoints](https://docs.nats.io/running-a-nats-service/nats_admin/monitoring).

[View](/telegraf/v1/input-plugins/nats/)

### NATS Consumer

Plugin ID: `inputs.nats_consumer`
Telegraf v0.10.3+

This service plugin consumes messages from [NATS](https://www.nats.io/about/) instances in one of the supported [data formats](/telegraf/v1/data_formats/input). A [Queue Group](https://www.nats.io/documentation/concepts/nats-queueing/) is used when subscribing to subjects so multiple instances of telegraf can consume messages in parallel. The plugin supports authenticating via [username/password](https://docs.nats.io/using-nats/developer/connecting/userpass), a [credentials file](https://docs.nats.io/using-nats/developer/connecting/creds) (NATS 2.0), or an [nkey seed file](https://docs.nats.io/using-nats/developer/connecting/nkey) (NATS 2.0).

[View](/telegraf/v1/input-plugins/nats_consumer/)

### Neoom Beaam

Plugin ID: `inputs.neoom_beaam`
Telegraf v1.33.0+

This plugin gathers metrics from a [Neoom Beaam gateway](https://neoom.com/en/products/beaam) using the [Beaam API](https://developer.neoom.com/reference/concepts-terms-1) with access token that can be created in the Neoom web interface. Please follow the [developer instructions](https://neoom.com/developers) to create the token.

[View](/telegraf/v1/input-plugins/neoom_beaam/)

### Neptune Apex

Plugin ID: `inputs.neptune_apex`
Telegraf v1.10.0+

This plugin gathers metrics from [Neptune Apex controller](https://www.neptunesystems.com) instances, allowing aquarium hobbyists to monitor and control their tanks based on various probes.

[View](/telegraf/v1/input-plugins/neptune_apex/)

### Network

Plugin ID: `inputs.net`
Telegraf v0.1.1+

This plugin gathers metrics about network interface and protocol usage.

[View](/telegraf/v1/input-plugins/net/)

### Network Response

Plugin ID: `inputs.net_response`
Telegraf v0.10.3+

This plugin tests UDP/TCP connection and produces metrics from the result, the response time and optionally verifies text in the response.

[View](/telegraf/v1/input-plugins/net_response/)

### Netflow

Plugin ID: `inputs.netflow`
Telegraf v1.25.0+

This service plugin acts as a collector for Netflow v5, Netflow v9 and IPFIX flow information. The Layer 4 protocol numbers are gathered from the [official IANA assignments](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml). The internal field mappings for Netflow v5 fields are defined according to [Cisco’s Netflow v5 documentation](https://www.cisco.com/c/en/us/td/docs/net_mgmt/netflow_collection_engine/3-6/user/guide/format.html#wp1006186), Netflow v9 fields are defined according to [Cisco’s Netflow v9 documentation](https://www.cisco.com/en/US/technologies/tk648/tk362/technologies_white_paper09186a00800a3db9.html) and the [ASA extensions](https://www.cisco.com/c/en/us/td/docs/security/asa/special/netflow/asa_netflow.html). Definitions for IPFIX are according to [IANA assignment document](https://www.iana.org/assignments/ipfix/ipfix.xhtml#ipfix-nat-type).

[View](/telegraf/v1/input-plugins/netflow/)

### Network Connection Statistics

Plugin ID: `inputs.netstat`
Telegraf v0.2.0+

This plugin collects statistics about TCP connection states and UDP socket counts.

[View](/telegraf/v1/input-plugins/netstat/)

### Network Filesystem

Plugin ID: `inputs.nfsclient`
Telegraf v1.18.0+

This plugin collects metrics about operations on [Network Filesystem](https://www.ietf.org/rfc/rfc1813.txt?number=1813) mounts. By default, only a limited number of general system-level metrics are collected, including basic read/write counts but more detailed metrics can be enabled.

Many of the metrics, even if tagged with a mount point, are really *per-server*. E.g. if you mount two shares: `nfs01:/vol/foo/bar` and `nfs01:/vol/foo/baz`, there will be two near identical entries in `/proc/self/mountstats`. This is a limitation of the metrics exposed by the kernel, not by this plugin.

[View](/telegraf/v1/input-plugins/nfsclient/)

### Nftables

Plugin ID: `inputs.nftables`
Telegraf v1.37.0+

This plugin gathers packets and bytes counters for rules within Linux’s [nftables](https://wiki.nftables.org/wiki-nftables/index.php/Main_Page) firewall.

Rules are identified by the associated comment so those **comments have to be unique**! Rules without comment are ignored.

[View](/telegraf/v1/input-plugins/nftables/)

### Nginx

Plugin ID: `inputs.nginx`
Telegraf v0.1.5+

This plugin gathers metrics from the open source [Nginx web server](https://www.nginx.com). Nginx Plus is a commercial version. For more information about differences between Nginx (F/OSS) and Nginx Plus, see the Nginx [documentation](https://www.nginx.com/blog/whats-difference-nginx-foss-nginx-plus/).

[View](/telegraf/v1/input-plugins/nginx/)

### Nginx Plus

Plugin ID: `inputs.nginx_plus`
Telegraf v1.5.0+

This plugin gathers metrics from the commercial [Nginx Plus web server](https://www.f5.com/products/nginx/nginx-plus) via the [status module](http://nginx.org/en/docs/http/ngx_http_status_module.html).

Using this plugin requires a license.

For more information about differences between Nginx (F/OSS) and Nginx Plus, see the Nginx [documentation](https://www.nginx.com/blog/whats-difference-nginx-foss-nginx-plus/).

[View](/telegraf/v1/input-plugins/nginx_plus/)

### Nginx Plus API

Plugin ID: `inputs.nginx_plus_api`
Telegraf v1.9.0+

This plugin gathers metrics from the commercial [Nginx Plus web server](https://www.f5.com/products/nginx/nginx-plus) via the [REST API](https://demo.nginx.com/swagger-ui/).

Using this plugin requires a license.

For more information about differences between Nginx (F/OSS) and Nginx Plus, see the Nginx [documentation](https://www.nginx.com/blog/whats-difference-nginx-foss-nginx-plus/).

[View](/telegraf/v1/input-plugins/nginx_plus_api/)

### Nginx Stream Server Traffic

Plugin ID: `inputs.nginx_sts`
Telegraf v1.15.0+

This plugin gathers metrics from the [Nginx web server](https://www.nginx.com) using the [external stream server traffic status module](https://github.com/vozlt/nginx-module-sts). This module provides access to stream host status information containing the current status of servers, upstreams and caches, similar to the live activity monitoring of Nginx plus. For module configuration details please see the [module documentation](https://github.com/vozlt/nginx-module-sts#synopsis).

[View](/telegraf/v1/input-plugins/nginx_sts/)

### Nginx Upstream Check

Plugin ID: `inputs.nginx_upstream_check`
Telegraf v1.10.0+

This plugin gathers metrics from the [Nginx web server](https://www.nginx.com) using the [upstream check module](https://github.com/yaoweibin/nginx_upstream_check_module). This module periodically sends the configured requests to servers in the Nginx’s upstream determining their availability.

[View](/telegraf/v1/input-plugins/nginx_upstream_check/)

### Nginx Virtual Host Traffic

Plugin ID: `inputs.nginx_vts`
Telegraf v1.9.0+

This plugin gathers metrics from the [Nginx web server](https://www.nginx.com) using the [external virtual host traffic status module](https://github.com/vozlt/nginx-module-vts). This module provides access to virtual host status information containing the current status of servers, upstreams and caches, similar to the live activity monitoring of Nginx plus. For module configuration details please see the [module documentation](https://github.com/vozlt/nginx-module-vts#synopsis).

[View](/telegraf/v1/input-plugins/nginx_vts/)

### Hashicorp Nomad

Plugin ID: `inputs.nomad`
Telegraf v1.22.0+

This plugin collects metrics from every [Nomad agent](https://www.nomadproject.io/) of the specified cluster. Telegraf may be present in every node and connect to the agent locally.

[View](/telegraf/v1/input-plugins/nomad/)

### NLnet Labs Name Server Daemon

Plugin ID: `inputs.nsd`
Telegraf v1.0.0+

This plugin gathers statistics from a [NLnet Labs Name Server Daemon](https://www.nlnetlabs.nl/projects/nsd/about), an authoritative DNS name server.

[View](/telegraf/v1/input-plugins/nsd/)

### Netgear Switch Discovery Protocol

Plugin ID: `inputs.nsdp`
Telegraf v1.34.0+

This plugin gathers metrics from devices via the [Netgear Switch Discovery Protocol](https://en.wikipedia.org/wiki/Netgear_Switch_Discovery_Protocol) for all available switches and ports.

[View](/telegraf/v1/input-plugins/nsdp/)

### NSQ

Plugin ID: `inputs.nsq`
Telegraf v1.16.0+

This plugin gathers metrics from [NSQ](https://nsq.io/) realtime distributed messaging platform instances using the [NSQD API](https://nsq.io/components/nsqd.html).

[View](/telegraf/v1/input-plugins/nsq/)

### NSQ Consumer

Plugin ID: `inputs.nsq_consumer`
Telegraf v0.10.1+

This service plugin consumes messages from [NSQ](https://nsq.io/) realtime distributed messaging platform brokers in one of the supported [data formats](/telegraf/v1/data_formats/input).

[View](/telegraf/v1/input-plugins/nsq_consumer/)

### Kernel Network Statistics

Plugin ID: `inputs.nstat`
Telegraf v0.13.1+

This plugin collects network metrics from `/proc/net/netstat`, `/proc/net/snmp` and `/proc/net/snmp6` files

[View](/telegraf/v1/input-plugins/nstat/)

### Network Time Protocol Query

Plugin ID: `inputs.ntpq`
Telegraf v0.11.0+

This plugin gathers metrics about [Network Time Protocol](https://ntp.org/) queries.

This plugin requires the `ntpq` executable to be installed on the system.

[View](/telegraf/v1/input-plugins/ntpq/)

### Nvidia System Management Interface (SMI)

Plugin ID: `inputs.nvidia_smi`
Telegraf v1.7.0+

This plugin collects metrics for [NVIDIA GPUs](https://www.nvidia.com/) including memory and GPU usage, temperature and other, using the [NVIDIA System Management Interface](https://developer.nvidia.com/nvidia-system-management-interface).

This plugin requires the `nvidia-smi` binary to be installed on the system.

[View](/telegraf/v1/input-plugins/nvidia_smi/)

### OPC UA Client Reader

Plugin ID: `inputs.opcua`
Telegraf v1.16.0+

This plugin gathers data from an [OPC UA](https://opcfoundation.org/about/opc-technologies/opc-ua/) server by subscribing to the configured nodes.

[View](/telegraf/v1/input-plugins/opcua/)

### OPC UA Client Listener

Plugin ID: `inputs.opcua_listener`
Telegraf v1.25.0+

This service plugin receives data from an [OPC UA](https://opcfoundation.org/about/opc-technologies/opc-ua/) server by subscribing to nodes and events.

[View](/telegraf/v1/input-plugins/opcua_listener/)

### OpenLDAP

Plugin ID: `inputs.openldap`
Telegraf v1.4.0+

This plugin gathers metrics from [OpenLDAP](https://www.openldap.org/)’s `cn=Monitor` backend. To use this plugin you must enable the [slapd monitoring](https://www.openldap.org/devel/admin/monitoringslapd.html) backend.

It is recommended to use the newer [`ldap` input plugin](/telegraf/v1/plugins/#input-ldap) instead.

[View](/telegraf/v1/input-plugins/openldap/)

### OpenNTPD

Plugin ID: `inputs.openntpd`
Telegraf v1.12.0+

This plugin gathers metrics from [OpenNTPD](http://www.openntpd.org/) using the `ntpctl` command.

The `ntpctl` binary must be present on the system and executable by Telegraf. The plugin supports using `sudo` for execution.

[View](/telegraf/v1/input-plugins/openntpd/)

### OpenSearch Query

Plugin ID: `inputs.opensearch_query`
Telegraf v1.26.0+

This plugin queries [OpenSearch](https://opensearch.org/) endpoints to derive metrics from data stored in an OpenSearch cluster like the number of hits for a search query, statistics on numeric fields, document counts, etc.

This plugins is tested against OpenSearch 2.5.0 and 1.3.7 but newer version should also work.

[View](/telegraf/v1/input-plugins/opensearch_query/)

### OpenSMTPD

Plugin ID: `inputs.opensmtpd`
Telegraf v1.5.0+

This plugin gathers statistics from [OpenSMTPD](https://www.opensmtpd.org/) using the `smtpctl` binary.

The `smtpctl` binary must be present on the system and executable by Telegraf. The plugin supports using `sudo` for execution.

[View](/telegraf/v1/input-plugins/opensmtpd/)

### OpenStack

Plugin ID: `inputs.openstack`
Telegraf v1.21.0+

This plugin collects metrics about services from [OpenStack](https://www.openstack.org/) endpoints.

Due to the large number of unique tags generated by the plugin it is **highly recommended** to use [metric filtering](/telegraf/v1/configuration/#modifiers) like `taginclude` and `tagexclude` to reduce cardinality.

[View](/telegraf/v1/input-plugins/openstack/)

### OpenTelemetry

Plugin ID: `inputs.opentelemetry`
Telegraf v1.19.0+

This service plugin receives traces, metrics, logs and profiles from [OpenTelemetry](https://opentelemetry.io) clients and compatible agents via gRPC.

Telegraf v1.32 through v1.35 support the Profiles signal using the v1 experimental API. Telegraf v1.36 supports the Profiles signal using the v1 development API before v0.1.0. Telegraf v1.37+ supports the Profiles signal using the v1 development API v0.2.0.

[View](/telegraf/v1/input-plugins/opentelemetry/)

### OpenWeatherMap

Plugin ID: `inputs.openweathermap`
Telegraf v1.11.0+

This plugin collects weather and forecast data from the [OpenWeatherMap](https://openweathermap.org) service.

To use this plugin you will need an [APP-ID](https://openweathermap.org/appid) to work.

[View](/telegraf/v1/input-plugins/openweathermap/)

### P4 Runtime

Plugin ID: `inputs.p4runtime`
Telegraf v1.26.0+

This plugin collects metrics from the data plane of network devices, such as Programmable Switches or Programmable Network Interface Cards by reading the `Counter` values of the [P4 program](https://p4.org) running on the device. Metrics are collected through a gRPC connection with the [P4 runtime](https://github.com/p4lang/p4runtime) server.

If you want to gather information about the program name, please follow the instruction in [6.2.1. Annotating P4 code with PkgInfo](https://p4.org/p4-spec/p4runtime/main/P4Runtime-Spec.html#sec-annotating-p4-code-with-pkginfo) to modify your P4 program.

[View](/telegraf/v1/input-plugins/p4runtime/)

### Passenger

Plugin ID: `inputs.passenger`
Telegraf v0.10.1+

This plugin gathers metrics from the [Phusion Passenger](https://www.phusionpassenger.com/) service.

Depending on your environment, this plugin can create a high number of series which can cause high load on your database. Please use [measurement filtering](/telegraf/v1/configuration/#metric-filtering) to manage your series cardinality!

The plugin uses the `passenger-status` command line tool.

This plugin requires the `passenger-status` binary to be installed on the system and to be executable by Telegraf.

[View](/telegraf/v1/input-plugins/passenger/)

### PF

Plugin ID: `inputs.pf`
Telegraf v1.5.0+

This plugin gathers information from the FreeBSD or OpenBSD pf firewall like the number of current entries in the table, counters for the number of searches, inserts, and removals to tables using the `pfctl` command.

This plugin requires the `pfctl` binary to be executable by Telegraf. It requires read access to the device file `/dev/pf`.

[View](/telegraf/v1/input-plugins/pf/)

### PgBouncer

Plugin ID: `inputs.pgbouncer`
Telegraf v1.8.0+

This plugin collects metrics from a [PgBouncer load balancer](https://pgbouncer.github.io) instance. Check the [documentation](https://pgbouncer.github.io/usage.html) for available metrics and their meaning.

This plugin requires PgBouncer v1.5+.

[View](/telegraf/v1/input-plugins/pgbouncer/)

### PHP-FPM

Plugin ID: `inputs.phpfpm`
Telegraf v0.1.10+

This plugin gathers statistics of the [PHP FastCGI Process Manager](https://www.php.net/manual/en/install.fpm.php) using either the HTTP status page or the fpm socket.

[View](/telegraf/v1/input-plugins/phpfpm/)

### Ping

Plugin ID: `inputs.ping`
Telegraf v0.1.8+

This plugin collects metrics on ICMP ping packets including the round-trip time, response times and other packet statistics.

When using the `exec` method the `ping` command must be available on the systems and executable by Telegraf.

[View](/telegraf/v1/input-plugins/ping/)

### Postfix

Plugin ID: `inputs.postfix`
Telegraf v1.5.0+

This plugin collects metrics on a local [Postfix](https://www.postfix.org/) instance reporting the length, size and age of the active, hold, incoming, maildrop, and deferred [queues](https://www.postfix.org/QSHAPE_README.html#queues).

[View](/telegraf/v1/input-plugins/postfix/)

### PostgreSQL

Plugin ID: `inputs.postgresql`
Telegraf v0.10.3+

This plugin provides metrics for a [PostgreSQL](https://www.postgresql.org/) Server instance. Recorded metrics are lightweight and use Dynamic Management Views supplied by PostgreSQL.

[View](/telegraf/v1/input-plugins/postgresql/)

### PostgreSQL Extensible

Plugin ID: `inputs.postgresql_extensible`
Telegraf v0.12.0+

This plugin queries a [PostgreSQL](https://www.postgresql.org/) server and provides metrics for the returned result. This is useful when using PostgreSQL extensions to collect additional metrics.

Please also check the more generic [sql input plugin](/telegraf/v1/plugins/#input-sql).

[View](/telegraf/v1/input-plugins/postgresql_extensible/)

### PowerDNS

Plugin ID: `inputs.powerdns`
Telegraf v0.10.2+

This plugin gathers metrics from [PowerDNS](https://www.powerdns.com/) servers using unix sockets.

This plugin will need access to the powerdns control socket.

[View](/telegraf/v1/input-plugins/powerdns/)

### PowerDNS Recursor

Plugin ID: `inputs.powerdns_recursor`
Telegraf v1.11.0+

This plugin gathers metrics from [PowerDNS Recursor](https://www.powerdns.com/powerdns-recursor) instances using the unix control-sockets.

Telegraf will need read and write access to the control socket and the `socket_dir`.

[View](/telegraf/v1/input-plugins/powerdns_recursor/)

### Processes

Plugin ID: `inputs.processes`
Telegraf v0.11.0+

This plugin gathers info about the total number of processes and groups them by status (zombie, sleeping, running, etc.)

On Linux this plugin requires access to procfs (/proc), on other operating systems the plugin must be able to execute the `ps` command.

[View](/telegraf/v1/input-plugins/processes/)

### Procstat

Plugin ID: `inputs.procstat`
Telegraf v0.2.0+

This plugin allows to monitor the system resource usage of one or more processes. The plugin provides metrics about the individual processes as well as accumulated metrics on the number of PIDs returned on a search. Processes can be filtered e.g. by regular expressions on the command, the user owning the process or the service that started the process.

[View](/telegraf/v1/input-plugins/procstat/)

### Prometheus

Plugin ID: `inputs.prometheus`
Telegraf v0.1.5+

This plugin gathers metrics from [Prometheus](https://prometheus.io/) metric endpoints such as applications implementing such an endpoint or node-exporter instances. This plugin also supports various service-discovery methods.

[View](/telegraf/v1/input-plugins/prometheus/)

### PromQL

Plugin ID: `inputs.promql`
Telegraf v1.37.0+

This plugin gathers metrics from a [Prometheus](https://prometheus.io/) endpoint using [PromQL queries](https://prometheus.io/docs/prometheus/latest/querying/basics/) via the [HTTP API](https://prometheus.io/docs/prometheus/latest/querying/api/).

[View](/telegraf/v1/input-plugins/promql/)

### Proxmox

Plugin ID: `inputs.proxmox`
Telegraf v1.16.0+

This plugin gathers metrics about containers and VMs running on a [Proxmox](https://www.proxmox.com) instance using the Proxmox API.

[View](/telegraf/v1/input-plugins/proxmox/)

### Puppet Agent

Plugin ID: `inputs.puppetagent`
Telegraf v0.2.0+

This plugin gathers metrics of a [Puppet agent](https://www.puppet.com/) by parsing variables from the local last-run-summary file.

[View](/telegraf/v1/input-plugins/puppetagent/)

### RabbitMQ

Plugin ID: `inputs.rabbitmq`
Telegraf v0.1.5+

This plugin gathers statistics from [RabbitMQ](https://www.rabbitmq.com) servers via the [Management Plugin](https://www.rabbitmq.com/management.html).

[View](/telegraf/v1/input-plugins/rabbitmq/)

### Radius

Plugin ID: `inputs.radius`
Telegraf v1.26.0+

This plugin collects response times for [Radius](https://datatracker.ietf.org/doc/html/rfc2865) authentication requests.

[View](/telegraf/v1/input-plugins/radius/)

### Raindrops Middleware

Plugin ID: `inputs.raindrops`
Telegraf v0.10.3+

This plugin collects statistics for [Raindrops middleware](http://raindrops.bogomips.org/Raindrops/Middleware.html) instances.

[View](/telegraf/v1/input-plugins/raindrops/)

### RAS Daemon

Plugin ID: `inputs.ras`
Telegraf v1.16.0+

This plugin gathers statistics and error counts provided by the local [RAS (reliability, availability and serviceability)](https://github.com/mchehab/rasdaemon) daemon.

This plugin requires access to SQLite3 database from `RASDaemon`. Please make sure the Telegraf user has the required permissions to this database!

[View](/telegraf/v1/input-plugins/ras/)

### RavenDB

Plugin ID: `inputs.ravendb`
Telegraf v1.18.0+

This plugin gathers metrics from [RavenDB](https://ravendb.net/) servers via the monitoring API.

This plugin requires RavenDB Server v5.2+.

[View](/telegraf/v1/input-plugins/ravendb/)

### Redfish

Plugin ID: `inputs.redfish`
Telegraf v1.15.0+

This plugin gathers metrics and status information of server hardware with enabled [DMTF’s Redfish](https://redfish.dmtf.org/) support.

[View](/telegraf/v1/input-plugins/redfish/)

### Redis

Plugin ID: `inputs.redis`
Telegraf v0.1.1+

This plugin gathers metrics from [Redis](https://redis.io/) servers.

[View](/telegraf/v1/input-plugins/redis/)

### Redis Sentinel

Plugin ID: `inputs.redis_sentinel`
Telegraf v1.22.0+

This plugin collects metrics for [Redis Sentinel](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/) instances monitoring Redis servers and replicas.

[View](/telegraf/v1/input-plugins/redis_sentinel/)

### RethinkDB

Plugin ID: `inputs.rethinkdb`
Telegraf v0.1.3+

This plugin collects metrics from [RethinkDB](https://www.rethinkdb.com/) servers.

[View](/telegraf/v1/input-plugins/rethinkdb/)

### Riak

Plugin ID: `inputs.riak`
Telegraf v0.10.4+

This plugin gathers metrics from [Riak](https://riak.com/) instances.

[View](/telegraf/v1/input-plugins/riak/)

### Riemann Listener

Plugin ID: `inputs.riemann_listener`
Telegraf v1.17.0+

This service plugin listens for messages from [Riemann](https://riemann.io/) clients using the protocol buffer format.

[View](/telegraf/v1/input-plugins/riemann_listener/)

### Siemens S7

Plugin ID: `inputs.s7comm`
Telegraf v1.28.0+

This plugin reads metrics from Siemens PLCs via the S7 protocol.

[View](/telegraf/v1/input-plugins/s7comm/)

### Salesforce

Plugin ID: `inputs.salesforce`
Telegraf v1.4.0+

This plugin gathers metrics about the limits in your [Salesforce](https://salesforce.com) organization and the remaining usage using the [limits endpoint](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_limits.htm) of Salesforce’s REST API.

[View](/telegraf/v1/input-plugins/salesforce/)

### LM Sensors

Plugin ID: `inputs.sensors`
Telegraf v0.10.1+

This plugin collects metrics from hardware sensors using [lm-sensors](https://en.wikipedia.org/wiki/Lm_sensors).

This plugin requires the lm-sensors package to be installed on the system and `sensors` to be executable from Telegraf.

[View](/telegraf/v1/input-plugins/sensors/)

### SFlow

Plugin ID: `inputs.sflow`
Telegraf v1.14.0+

This service plugin produces metrics from information received by acting as a [SFlow V5](https://sflow.org/sflow_version_5.txt) collector. Currently, the plugin can collect Flow Samples of Ethernet / IPv4, IPv4 TCP and UDP headers. Counters and other header samples are ignored. Please use the [netflow plugin](/telegraf/v1/plugins/#input-netflow) for a more modern and sophisticated implementation.

This plugin produces high cardinality data, which when not controlled for will cause high load on your database. Please make sure to [filter](/telegraf/v1/configuration/#metric-filtering) the produced metrics or configure your database to avoid cardinality issues!

[View](/telegraf/v1/input-plugins/sflow/)

### Slab

Plugin ID: `inputs.slab`
Telegraf v1.23.0+

This plugin collects details on memory consumption of [Slab cache](https://www.kernel.org/doc/gorman/html/understand/understand011.html) entries by parsing the `/proc/slabinfo` file respecting the `HOST_PROC` environment variable.

This plugin requires `/proc/slabinfo` to be readable by the Telegraf user.

[View](/telegraf/v1/input-plugins/slab/)

### SLURM

Plugin ID: `inputs.slurm`
Telegraf v1.32.0+

This plugin gather diagnoses, jobs, nodes, partitions and reservation metrics for a [SLURM](https://slurm.schedmd.com) instance using the REST API provided by the `slurmrestd` daemon.

This plugin supports the [REST API v0.0.38](https://slurm.schedmd.com/rest.html) which must be enabled in the `slurmrestd` daemon. For more information, check the [documentation](https://slurm.schedmd.com/rest_quickstart.html#customization).

[View](/telegraf/v1/input-plugins/slurm/)

### S.M.A.R.T.

Plugin ID: `inputs.smart`
Telegraf v1.5.0+

This plugin collects [Self-Monitoring, Analysis and Reporting Technology](https://en.wikipedia.org/wiki/Self-Monitoring,_Analysis_and_Reporting_Technology) information for storage devices information using the `smartmontools` package. This plugin also supports NVMe devices by using the [`nvme-cli`](https://github.com/linux-nvme/nvme-cli) package.

This plugin requires the `smartmontools` and, for NVMe devices, the [`nvme-cli`](https://github.com/linux-nvme/nvme-cli) packages to be installed on your system. The `smartctl` and `nvme` commands must to be executable by Telegraf.

[View](/telegraf/v1/input-plugins/smart/)

### smartctl JSON

Plugin ID: `inputs.smartctl`
Telegraf v1.31.0+

This plugin collects [Self-Monitoring, Analysis and Reporting Technology](https://en.wikipedia.org/wiki/Self-Monitoring,_Analysis_and_Reporting_Technology) information for storage devices information using the `smartmontools` package. Contrary to the [smart plugin](/telegraf/v1/plugins/#input-smart), this plugin does not use the [`nvme-cli`](https://github.com/linux-nvme/nvme-cli) package to collect additional information about NVMe devices.

This plugin requires `smartmontools` to be installed on your system. The `smartctl` command must to be executable by Telegraf and must supporting JSON output. JSON output was added in v7.0 and improved in subsequent releases

[View](/telegraf/v1/input-plugins/smartctl/)

### SNMP

Plugin ID: `inputs.snmp`
Telegraf v0.10.1+

This plugin gathers metrics by polling [SNMP](https://datatracker.ietf.org/doc/html/rfc1157) agents with individual OIDs or complete SNMP tables.

The path setting is shared between all instances of all SNMP plugin types!

[View](/telegraf/v1/input-plugins/snmp/)

### SNMP Trap

Plugin ID: `inputs.snmp_trap`
Telegraf v1.13.0+

This service plugin listens for [SNMP](https://datatracker.ietf.org/doc/html/rfc1157) notifications like traps and inform requests. Notifications are received on plain UDP with a configurable port.

The path setting is shared between all instances of all SNMP plugin types!

[View](/telegraf/v1/input-plugins/snmp_trap/)

### Socket Listener

Plugin ID: `inputs.socket_listener`
Telegraf v1.3.0+

This service plugin listens for messages on sockets (TCP, UDP, Unix or Unixgram) and parses the packets received in one of the supported [data formats](/telegraf/v1/data_formats/input).

[View](/telegraf/v1/input-plugins/socket_listener/)

### Socket Statistics

Plugin ID: `inputs.socketstat`
Telegraf v1.22.0+

This plugin gathers metrics for established network connections using [iproute2](https://github.com/iproute2/iproute2)’s `ss` command. The `ss` command does not require specific privileges.

This plugin produces high cardinality data, which when not controlled for will cause high load on your database. Please make sure to [filter](/telegraf/v1/configuration/#metric-filtering) the produced metrics or configure your database to avoid cardinality issues!

[View](/telegraf/v1/input-plugins/socketstat/)

### Apache Solr

Plugin ID: `inputs.solr`
Telegraf v1.5.0+

This plugin collects statistics from [Solr](http://lucene.apache.org/solr/) instances using the [MBean Request Handler](https://cwiki.apache.org/confluence/display/solr/MBean+Request+Handler). For additional details on performance statistics check the [performance statistics reference](https://cwiki.apache.org/confluence/display/solr/Performance+Statistics+Reference).

This plugin requires Apache Solr v3.5+.

[View](/telegraf/v1/input-plugins/solr/)

### SQL

Plugin ID: `inputs.sql`
Telegraf v1.19.0+

This plugin reads metrics from performing [SQL](https://www.iso.org/standard/76583.html) queries against a SQL server. Different server types are supported and their settings might differ (especially the connection parameters). Please check the list of [supported SQL drivers](/docs/SQL_DRIVERS_INPUT.md) for the `driver` name and options for the data-source-name (`dsn`) options.

[View](/telegraf/v1/input-plugins/sql/)

### Microsoft SQL Server

Plugin ID: `inputs.sqlserver`
Telegraf v0.10.1+

This plugin provides metrics for your [SQL Server](https://docs.microsoft.com/en-us/sql/sql-server) instance. Recorded metrics are lightweight and use Dynamic Management Views supplied by SQL Server.

This plugin supports SQL server versions supported by Microsoft (see [lifecycle dates](https://docs.microsoft.com/en-us/sql/sql-server/end-of-support/sql-server-end-of-life-overview?view=sql-server-ver15#lifecycle-dates)), Azure SQL Databases (Single), Azure SQL Managed Instances, Azure SQL Elastic Pools and Azure Arc-enabled SQL Managed Instances.

[View](/telegraf/v1/input-plugins/sqlserver/)

### Stackdriver Google Cloud Monitoring

Plugin ID: `inputs.stackdriver`
Telegraf v1.10.0+

This plugin collects metrics from [Google Cloud Monitoring](https://cloud.google.com/monitoring) (formerly Stackdriver) using the [Cloud Monitoring API v3](https://cloud.google.com/monitoring/api/v3/).

This plugin accesses APIs which are [chargeable](https://cloud.google.com/stackdriver/pricing#stackdriver_monitoring_services), cost might incur.

[View](/telegraf/v1/input-plugins/stackdriver/)

### StatsD

Plugin ID: `inputs.statsd`
Telegraf v0.2.0+

This service plugin gathers metrics from a [Statsd](https://github.com/statsd/statsd) server.

[View](/telegraf/v1/input-plugins/statsd/)

### Supervisor

Plugin ID: `inputs.supervisor`
Telegraf v1.24.0+

This plugin gathers information about processes running under [supervisord](https://supervisord.org/) using the [XML-RPC API](https://supervisord.org/api.html).

This plugin requires supervisor v3.3.2+.

[View](/telegraf/v1/input-plugins/supervisor/)

### Suricata

Plugin ID: `inputs.suricata`
Telegraf v1.13.0+

This service plugin reports internal performance counters of the [Suricata IDS/IPS](https://suricata.io/) engine, such as captured traffic volume, memory usage, uptime, flow counters, and much more. This plugin provides a socket for the Suricata log output to write JSON stats output to, and processes the incoming data to fit Telegraf’s format. It can also report for triggered Suricata IDS/IPS alerts.

[View](/telegraf/v1/input-plugins/suricata/)

### Swap

Plugin ID: `inputs.swap`
Telegraf v1.7.0+

This plugin collects metrics on the operating-system’s swap memory.

[View](/telegraf/v1/input-plugins/swap/)

### Synproxy

Plugin ID: `inputs.synproxy`
Telegraf v1.13.0+

This plugin gathers metrics about the Linux netfilter’s [synproxy](https://wiki.nftables.org/wiki-nftables/index.php/Synproxy) module used for mitigating SYN attacks.

[View](/telegraf/v1/input-plugins/synproxy/)

### Syslog

Plugin ID: `inputs.syslog`
Telegraf v1.7.0+

This service plugin listens for [syslog](https://en.wikipedia.org/wiki/Syslog) messages transmitted over a Unix Domain socket, [UDP](https://tools.ietf.org/html/rfc5426), [TCP](https://tools.ietf.org/html/rfc6587) or [TLS](https://tools.ietf.org/html/rfc5425) with or without the octet counting framing.

Syslog messages should be formatted according to the [syslog protocol](https://tools.ietf.org/html/rfc5424) or the [BSD syslog protocol](https://tools.ietf.org/html/rfc3164).

[View](/telegraf/v1/input-plugins/syslog/)

### System Performance Statistics

Plugin ID: `inputs.sysstat`
Telegraf v0.12.1+

This plugin collects Linux [system performance statistics](https://github.com/sysstat/sysstat) using the `sysstat` package. This plugin uses the `sadc` collector utility and and parses the created binary data file using the `sadf` utility.

This plugin requires the `sysstat` package to be installed on the system and both `sadc` and `sadf` to be executable by Telegraf.

[View](/telegraf/v1/input-plugins/sysstat/)

### System

Plugin ID: `inputs.system`
Telegraf v0.1.6+

This plugin gathers general system statistics like system load, uptime or the number of users logged in. It is similar to the unix `uptime` command.

[View](/telegraf/v1/input-plugins/system/)

### Systemd-Units

Plugin ID: `inputs.systemd_units`
Telegraf v1.13.0+

This plugin gathers the status of systemd-units on Linux, using systemd’s DBus interface.

This plugin requires systemd v230+!

[View](/telegraf/v1/input-plugins/systemd_units/)

### Tacacs

Plugin ID: `inputs.tacacs`
Telegraf v1.28.0+

This plugin collects metrics on [Terminal Access Controller Access Control System](https://datatracker.ietf.org/doc/html/rfc1492) authentication requests like response status and response time from servers such as [Aruba ClearPass](https://www.hpe.com/de/de/aruba-clearpass-policy-manager.html), [FreeRADIUS](https://www.freeradius.org/) or [TACACS+](https://datatracker.ietf.org/doc/html/rfc8907).

The plugin is primarily meant to monitor how long it takes for the server to fully handle an authentication request, including all potential dependent calls (for example to AD servers, or other sources of truth).

[View](/telegraf/v1/input-plugins/tacacs/)

### Tail

Plugin ID: `inputs.tail`
Telegraf v1.1.2+

This service plugin continuously reads a file and parses new data as it arrives similar to the [tail -f command](https://man7.org/linux/man-pages/man1/tail.1.html). The incoming messages are expected to be in one of the supported [data formats](/telegraf/v1/data_formats/input).

[View](/telegraf/v1/input-plugins/tail/)

### Teamspeak

Plugin ID: `inputs.teamspeak`
Telegraf v1.5.0+

This plugin collects statistics of one or more virtual [Teamspeak](https://www.teamspeak.com) servers using the `ServerQuery` interface. Currently this plugin only supports Teamspeak 3 servers.

For querying external Teamspeak server, make sure to add the Telegraf host to the `query_ip_allowlist.txt` file in the Teamspeak Server directory.

[View](/telegraf/v1/input-plugins/teamspeak/)

### Temperature

Plugin ID: `inputs.temp`
Telegraf v1.8.0+

This plugin gathers metrics on system temperatures.

[View](/telegraf/v1/input-plugins/temp/)

### Tengine Web Server

Plugin ID: `inputs.tengine`
Telegraf v1.8.0+

This plugin gathers metrics from the [Tengine Web Server](http://tengine.taobao.org) via the [reqstat](http://tengine.taobao.org/document/http_reqstat.html) module.

[View](/telegraf/v1/input-plugins/tengine/)

### Timex

Plugin ID: `inputs.timex`
Telegraf v1.37.0+

This plugin gathers metrics on system time using the Linux Kernel [adjtimex syscall](https://man7.org/linux/man-pages/man2/adjtimex.2.html).

The call gets the information of the kernel time variables that are controlled by the ntpd, systemd-timesyncd, chrony or other time synchronization services.

[View](/telegraf/v1/input-plugins/timex/)

### Apache Tomcat

Plugin ID: `inputs.tomcat`
Telegraf v1.4.0+

This plugin collects statistics from a [Tomcat server](https://tomcat.apache.org) instance using the manager status page. See the [Tomcat documentation](https://tomcat.apache.org/tomcat-9.0-doc/manager-howto.html#Server_Status) for details of these statistics.

[View](/telegraf/v1/input-plugins/tomcat/)

### Trig

Plugin ID: `inputs.trig`
Telegraf v0.3.0+

This plugin is for demonstration purposes and inserts sine and cosine values as metrics.

[View](/telegraf/v1/input-plugins/trig/)

### Turbostat

Plugin ID: `inputs.turbostat`
Telegraf v1.36.0+

This service plugin monitors system performance using the [turbostat](https://github.com/torvalds/linux/tree/master/tools/power/x86/turbostat) command.

This plugin requires the `turbostat` executable to be installed on the system.

[View](/telegraf/v1/input-plugins/turbostat/)

### Twemproxy

Plugin ID: `inputs.twemproxy`
Telegraf v0.3.0+

This plugin gathers statistics from [Twemproxy](https://github.com/twitter/twemproxy) servers.

[View](/telegraf/v1/input-plugins/twemproxy/)

### Unbound

Plugin ID: `inputs.unbound`
Telegraf v1.5.0+

This plugin gathers stats from an [Unbound](https://www.unbound.net) DNS resolver.

[View](/telegraf/v1/input-plugins/unbound/)

### UPSD

Plugin ID: `inputs.upsd`
Telegraf v1.24.0+

This plugin reads data of one or more Uninterruptible Power Supplies from a [Network UPS Tools](https://networkupstools.org/) daemon using its NUT network protocol.

[View](/telegraf/v1/input-plugins/upsd/)

### uWSGI

Plugin ID: `inputs.uwsgi`
Telegraf v1.12.0+

This plugin gathers metrics about [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) using its [Stats Server](https://uwsgi-docs.readthedocs.io/en/latest/StatsServer.html).

[View](/telegraf/v1/input-plugins/uwsgi/)

### Varnish

Plugin ID: `inputs.varnish`
Telegraf v0.13.1+

This plugin gathers statistics from a local [Varnish HTTP Cache](https://varnish-cache.org) instance using the `varnishstat` command.

This plugin requires the `varnishstat` executable to be installed on the system and executable by Telegraf. Furthermore, the plugin requires Varnish v6.0.2+.

[View](/telegraf/v1/input-plugins/varnish/)

### Hashicorp Vault

Plugin ID: `inputs.vault`
Telegraf v1.22.0+

This plugin collects metrics from every [Vault](https://www.hashicorp.com/de/products/vault) agent of a cluster.

This plugin requires Vault v1.8.5+

[View](/telegraf/v1/input-plugins/vault/)

### VMware vSphere

Plugin ID: `inputs.vsphere`
Telegraf v1.8.0+

This plugin gathers metrics from [vSphere](https://www.vmware.com/products/cloud-infrastructure/vsphere) servers of a vCenter including clusters, hosts, resource pools, VMs, datastores and vSAN information.

This plugin requires vSphere v7.0+.

[View](/telegraf/v1/input-plugins/vsphere/)

### Webhooks

Plugin ID: `inputs.webhooks`
Telegraf v1.0.0+

This service plugin provides an HTTP server and register for multiple webhook listeners.

[View](/telegraf/v1/input-plugins/webhooks/)

### WHOIS

Plugin ID: `inputs.whois`
Telegraf v1.35.0+

This plugin queries [WHOIS information](https://datatracker.ietf.org/doc/html/rfc3912) for configured domains and provides metrics such as expiration timestamps, registrar details and domain status from e.g. [IANA](https://www.iana.org/whois) or [ICANN](https://lookup.icann.org/) servers.

[View](/telegraf/v1/input-plugins/whois/)

### Windows Eventlog

Plugin ID: `inputs.win_eventlog`
Telegraf v1.16.0+

This plugin gathers metrics from the [Windows event log](https://learn.microsoft.com/en-us/shows/inside/event-viewer) on Windows Vista and higher.

Some event channels, like the System Log, require Administrator permissions to subscribe.

[View](/telegraf/v1/input-plugins/win_eventlog/)

### Windows Performance Counters

Plugin ID: `inputs.win_perf_counters`
Telegraf v0.10.2+

This plugin produces metrics from the collected [Windows Performance Counters](https://learn.microsoft.com/en-us/windows/win32/perfctrs/about-performance-counters).

[View](/telegraf/v1/input-plugins/win_perf_counters/)

### Windows Services

Plugin ID: `inputs.win_services`
Telegraf v1.4.0+

This plugin collects information about the status of Windows services.

Monitoring some services may require running Telegraf with administrator privileges.

[View](/telegraf/v1/input-plugins/win_services/)

### Windows Management Instrumentation

Plugin ID: `inputs.win_wmi`
Telegraf v1.26.0+

This plugin queries information or invokes methods using [Windows Management Instrumentation](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page) classes. This allows capturing and filtering virtually any configuration or metric value exposed through WMI.

The telegraf service user must have at least permission to [read](https://learn.microsoft.com/en-us/windows/win32/wmisdk/access-to-wmi-namespaces) the WMI namespace being queried.

[View](/telegraf/v1/input-plugins/win_wmi/)

### Wireguard

Plugin ID: `inputs.wireguard`
Telegraf v1.14.0+

This plugin collects statistics on a local [Wireguard](https://www.wireguard.com/) server using the [`wgctrl` library](https://github.com/WireGuard/wgctrl-go). The plugin reports gauge metrics for Wireguard interface device(s) and its peers.

[View](/telegraf/v1/input-plugins/wireguard/)

### Wireless

Plugin ID: `inputs.wireless`
Telegraf v1.9.0+

This plugin gathers metrics about wireless link quality by reading the `/proc/net/wireless` file.

[View](/telegraf/v1/input-plugins/wireless/)

### x509 Certificate

Plugin ID: `inputs.x509_cert`
Telegraf v1.8.0+

This plugin provides information about [X.509](https://en.wikipedia.org/wiki/X.509) certificates accessible e.g. via local file, tcp, udp, https or smtp protocols and the Windows Certificate Store.

When using a UDP address as a certificate source, the server must support [DTLS](https://en.wikipedia.org/wiki/Datagram_Transport_Layer_Security).

[View](/telegraf/v1/input-plugins/x509_cert/)

### Dell EMC XtremIO

Plugin ID: `inputs.xtremio`
Telegraf v1.22.0+

This plugin gathers metrics from a [Dell EMC XtremIO Storage Array](https://www.delltechnologies.com/asset/en-sa/products/storage/industry-market/h16444-introduction-xtremio-x2-storage-array-wp.pdf) instance using the [v3 Rest API](https://dl.dell.com/content/docu96624_xtremio-storage-array-x1-and-x2-cluster-types-with-xms-6-3-0-to-6-3-3-and-xios-4-0-15-to-4-0-31-and-6-0-0-to-6-3-3-restful-api-3-x-guide.pdf).

[View](/telegraf/v1/input-plugins/xtremio/)

### ZFS

Plugin ID: `inputs.zfs`
Telegraf v0.2.1+

This plugin gathers metrics from [ZFS](https://en.wikipedia.org/wiki/ZFS) filesystems using `/proc/spl/kstat/zfs` on Linux and `sysctl`, `zfs` and `zpool` on FreeBSD.

[View](/telegraf/v1/input-plugins/zfs/)

### Zipkin

Plugin ID: `inputs.zipkin`
Telegraf v1.4.0+

This service plugin implements the [Zipkin](https://zipkin.io/) HTTP server to gather trace and timing data needed to troubleshoot latency problems in microservice architectures.

This plugin produces high cardinality data, which when not controlled for will cause high load on your database. Please make sure to [filter](/telegraf/v1/configuration/#metric-filtering) the produced metrics or configure your database to avoid cardinality issues!

[View](/telegraf/v1/input-plugins/zipkin/)

### Apache Zookeeper

Plugin ID: `inputs.zookeeper`
Telegraf v0.2.0+

This plugin collects variables from [Zookeeper](https://zookeeper.apache.org) instances using the [`mntr` command](https://zookeeper.apache.org/doc/current/zookeeperAdmin.html#sc_zkCommands).

If the Prometheus Metric provider is enabled in Zookeeper use the [prometheus plugin](/telegraf/v1/plugins/#input-prometheus) instead with `http://<ip>:7000/metrics`.

[View](/telegraf/v1/input-plugins/zookeeper/)

## Output plugins

Telegraf processor plugins write metrics to various destinations.

### Amon

Plugin ID: `outputs.amon`
Telegraf v0.2.1 - v1.37.0 Deprecated

This plugin writes metrics to [Amon monitoring platform](https://www.amon.cx). It requires a `serverkey` and `amoninstance` URL which can be obtained from the [website](https://www.amon.cx/docs/monitoring/) for your account.

If point values being sent cannot be converted to a `float64`, the metric is skipped.

[View](/telegraf/v1/output-plugins/amon/)

### AMQP

Plugin ID: `outputs.amqp`
Telegraf v0.1.9+

This plugin writes to an Advanced Message Queuing Protocol v0.9.1 broker. A prominent implementation of this protocol is [RabbitMQ](https://www.rabbitmq.com).

This plugin does not bind the AMQP exchange to a queue.

For an introduction check the [AMQP concepts page](https://www.rabbitmq.com/tutorials/amqp-concepts.html) and the [RabbitMQ getting started guide](https://www.rabbitmq.com/getstarted.html).

[View](/telegraf/v1/output-plugins/amqp/)

### Azure Application Insights

Plugin ID: `outputs.application_insights`
Telegraf v1.7.0+

This plugin writes metrics to the [Azure Application Insights](https://azure.microsoft.com/en-us/services/application-insights/) service.

[View](/telegraf/v1/output-plugins/application_insights/)

### Arc

Plugin ID: `outputs.arc`
Telegraf v1.37.0+

This plugin writes metrics to [Arc](https://github.com/basekick-labs/arc), a high-performance time-series database, via MessagePack binary protocol messages providing a **3-5x better performance** than the line-protocol format.

[View](/telegraf/v1/output-plugins/arc/)

### Azure Data Explorer

Plugin ID: `outputs.azure_data_explorer`
Telegraf v1.20.0+

This plugin writes metrics to the [Azure Data Explorer](https://docs.microsoft.com/en-us/azure/data-explorer), [Azure Synapse Data Explorer](https://docs.microsoft.com/en-us/azure/synapse-analytics/data-explorer/data-explorer-overview), and [Real time analytics in Fabric](https://learn.microsoft.com/en-us/fabric/real-time-analytics/overview) services.

Azure Data Explorer is a distributed, columnar store, purpose built for any type of logs, metrics and time series data.

[View](/telegraf/v1/output-plugins/azure_data_explorer/)

### Azure Monitor

Plugin ID: `outputs.azure_monitor`
Telegraf v1.8.0+

This plugin writes metrics to [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor) which has a metric resolution of one minute. To accomodate for this in Telegraf, the plugin will automatically aggregate metrics into one minute buckets and send them to the service on every flush interval.

The Azure Monitor custom metrics service is currently in preview and might not be available in all Azure regions. Please also take the metric time limitations into account!

The metrics from each input plugin will be written to a separate Azure Monitor namespace, prefixed with `Telegraf/` by default. The field name for each metric is written as the Azure Monitor metric name. All field values are written as a summarized set that includes: min, max, sum, count. Tags are written as a dimension on each Azure Monitor metric.

[View](/telegraf/v1/output-plugins/azure_monitor/)

### Google BigQuery

Plugin ID: `outputs.bigquery`
Telegraf v1.18.0+

This plugin writes metrics to the [Google Cloud BigQuery](https://cloud.google.com/bigquery) service and requires [authentication](https://cloud.google.com/bigquery/docs/authentication) with Google Cloud using either a service account or user credentials.

Be aware that this plugin accesses APIs that are [chargeable](https://cloud.google.com/bigquery/pricing) and might incur costs.

[View](/telegraf/v1/output-plugins/bigquery/)

### Clarify

Plugin ID: `outputs.clarify`
Telegraf v1.27.0+

This plugin writes metrics to [Clarify](https://clarify.io). To use this plugin you will need to obtain a set of [credentials](https://docs.clarify.io/users/admin/integrations/credentials).

[View](/telegraf/v1/output-plugins/clarify/)

### Google Cloud PubSub

Plugin ID: `outputs.cloud_pubsub`
Telegraf v1.10.0+

This plugin publishes metrics to a [Google Cloud PubSub](https://cloud.google.com/pubsub) topic in one of the supported [data formats](/telegraf/v1/data_formats/output).

[View](/telegraf/v1/output-plugins/cloud_pubsub/)

### Amazon CloudWatch

Plugin ID: `outputs.cloudwatch`
Telegraf v0.10.1+

This plugin writes metrics to the [Amazon CloudWatch](https://aws.amazon.com/cloudwatch) service.

[View](/telegraf/v1/output-plugins/cloudwatch/)

### Amazon CloudWatch Logs

Plugin ID: `outputs.cloudwatch_logs`
Telegraf v1.19.0+

This plugin writes log-metrics to the [Amazon CloudWatch](https://aws.amazon.com/cloudwatch) service.

[View](/telegraf/v1/output-plugins/cloudwatch_logs/)

### CrateDB

Plugin ID: `outputs.cratedb`
Telegraf v1.5.0+

This plugin writes metrics to [CrateDB](https://crate.io/) via its [PostgreSQL protocol](https://crate.io/docs/crate/reference/protocols/postgres.html).

[View](/telegraf/v1/output-plugins/cratedb/)

### Datadog

Plugin ID: `outputs.datadog`
Telegraf v0.1.6+

This plugin writes metrics to the [Datadog Metrics API](https://docs.datadoghq.com/api/v1/metrics/#submit-metrics) and requires an `apikey` which can be obtained on the [website](https://app.datadoghq.com/account/settings#api) for the account.

This plugin supports the v1 API.

[View](/telegraf/v1/output-plugins/datadog/)

### Discard

Plugin ID: `outputs.discard`
Telegraf v1.2.0+

This plugin discards all metrics written to it and is meant for testing purposes.

[View](/telegraf/v1/output-plugins/discard/)

### Dynatrace

Plugin ID: `outputs.dynatrace`
Telegraf v1.16.0+

This plugin writes metrics to [Dynatrace](https://www.dynatrace.com) via the [Dynatrace Metrics API V2](https://docs.dynatrace.com/docs/shortlink/api-metrics-v2). It may be run alongside the Dynatrace OneAgent for automatic authentication or it may be run standalone on a host without OneAgent by specifying a URL and API Token.

More information on the plugin can be found in the [Dynatrace documentation](https://docs.dynatrace.com/docs/shortlink/telegraf).

All metrics are reported as gauges, unless they are specified to be delta counters using the `additional_counters` or `additional_counters_patterns` config option (see below). See the [Dynatrace Metrics ingestion protocol documentation](https://docs.dynatrace.com/docs/shortlink/metric-ingestion-protocol) for details on the types defined there.

[View](/telegraf/v1/output-plugins/dynatrace/)

### Elasticsearch

Plugin ID: `outputs.elasticsearch`
Telegraf v0.1.5+

This plugin writes metrics to [Elasticsearch](https://www.elastic.co) via HTTP using the [Elastic client library](http://olivere.github.io/elastic/). The plugin supports Elasticsearch releases from v5.x up to v7.x.

[View](/telegraf/v1/output-plugins/elasticsearch/)

### Azure Event Hubs

Plugin ID: `outputs.event_hubs`
Telegraf v1.21.0+

This plugin writes metrics to the [Azure Event Hubs](https://azure.microsoft.com/en-gb/services/event-hubs/) service in any of the supported [data formats](/telegraf/v1/data_formats/output). Metrics are sent as batches with each message payload containing one metric object, preferably as JSON as this eases integration with downstream components.

Each patch is sent to a single Event Hub within a namespace. In case no partition key is specified the batches will be automatically load-balanced (round-robin) across all the Event Hub partitions.

[View](/telegraf/v1/output-plugins/event_hubs/)

### Executable

Plugin ID: `outputs.exec`
Telegraf v1.12.0+

This plugin writes metrics to an external application via `stdin`. The command will be executed on each write creating a new process. Metrics are passed in one of the supported [data formats](/telegraf/v1/data_formats/output).

The executable and the individual parameters must be defined as a list. All outputs of the executable to `stderr` will be logged in the Telegraf log.

For better performance consider execd which runs continuously.

[View](/telegraf/v1/output-plugins/exec/)

### Executable Daemon

Plugin ID: `outputs.execd`
Telegraf v1.15.0+

This plugin writes metrics to an external daemon program via `stdin`. The command will be executed once and metrics will be passed to it on every write in one of the supported [data formats](/telegraf/v1/data_formats/output). The executable and the individual parameters must be defined as a list.

All outputs of the executable to `stderr` will be logged in the Telegraf log. Telegraf minimum version: Telegraf 1.15.0

[View](/telegraf/v1/output-plugins/execd/)

### File

Plugin ID: `outputs.file`
Telegraf v0.10.3+

This plugin writes metrics to one or more local files in one of the supported [data formats](/telegraf/v1/data_formats/output).

[View](/telegraf/v1/output-plugins/file/)

### Graphite

Plugin ID: `outputs.graphite`
Telegraf v0.10.1+

This plugin writes metrics to [Graphite](http://graphite.readthedocs.org/en/latest/index.html) via TCP. For details on the translation between Telegraf Metrics and Graphite output see the [Graphite data format](/telegraf/v1/plugins/#serializer-graphite).

[View](/telegraf/v1/output-plugins/graphite/)

### Graylog

Plugin ID: `outputs.graylog`
Telegraf v1.0.0+

This plugin writes metrics to a [Graylog](https://graylog.org/) instance using the [GELF data format](https://docs.graylog.org/en/3.1/pages/gelf.html#gelf-payload-specification).

[View](/telegraf/v1/output-plugins/graylog/)

### GroundWork

Plugin ID: `outputs.groundwork`
Telegraf v1.21.0+

This plugin writes metrics to a [GroundWork Monitor](https://www.gwos.com/product/groundwork-monitor/) instance.

Plugin only supports GroundWork v8 or later.

[View](/telegraf/v1/output-plugins/groundwork/)

### Health

Plugin ID: `outputs.health`
Telegraf v1.11.0+

This plugin provides a HTTP health check endpoint that can be configured to return failure status codes based on the value of a metric.

When the plugin is healthy it will return a 200 response; when unhealthy it will return a 503 response. The default state is healthy, one or more checks must fail in order for the resource to enter the failed state.

[View](/telegraf/v1/output-plugins/health/)

### Heartbeat

Plugin ID: `outputs.heartbeat`
Telegraf v1.37.0+

This plugin sends a heartbeat signal via POST to a HTTP endpoint on a regular interval. This is useful to keep track of existing Telegraf instances in a large deployment.

[View](/telegraf/v1/output-plugins/heartbeat/)

### HTTP

Plugin ID: `outputs.http`
Telegraf v1.7.0+

This plugin writes metrics to a HTTP endpoint using one of the supported [data formats](/telegraf/v1/data_formats/output). For data formats supporting batching, metrics are sent in batches by default.

[View](/telegraf/v1/output-plugins/http/)

### InfluxDB v1.x

Plugin ID: `outputs.influxdb`
Telegraf v0.1.1+

This plugin writes metrics to a [InfluxDB v1.x](https://docs.influxdata.com/influxdb/v1) instance via HTTP or UDP protocol.

[View](/telegraf/v1/output-plugins/influxdb/)

### InfluxDB v2.x

Plugin ID: `outputs.influxdb_v2`
Telegraf v1.8.0+

This plugin writes metrics to a [InfluxDB v2.x](https://docs.influxdata.com/influxdb/v2) instance via HTTP.

[View](/telegraf/v1/output-plugins/influxdb_v2/)

### Inlong

Plugin ID: `outputs.inlong`
Telegraf v1.35.0+

This plugin publishes metrics to an [Apache InLong](https://inlong.apache.org) instance.

[View](/telegraf/v1/output-plugins/inlong/)

### Instrumental

Plugin ID: `outputs.instrumental`
Telegraf v0.13.1+

This plugin writes metrics to the [Instrumental Collector API](https://instrumentalapp.com/docs/tcp-collector) and requires a project-specific API token.

Instrumental accepts stats in a format very close to Graphite, with the only difference being that the type of stat (gauge, increment) is the first token, separated from the metric itself by whitespace. The `increment` type is only used if the metric comes in as a counter via the [statsd input plugin](/telegraf/v1/plugins/#input-statsd).

[View](/telegraf/v1/output-plugins/instrumental/)

### Apache IoTDB

Plugin ID: `outputs.iotdb`
Telegraf v1.24.0+

This plugin writes metrics to an [Apache IoTDB](https://iotdb.apache.org) instance, a database for the Internet of Things, supporting session connection and data insertion.

[View](/telegraf/v1/output-plugins/iotdb/)

### Kafka

Plugin ID: `outputs.kafka`
Telegraf v0.1.7+

This plugin writes metrics to a [Kafka Broker](http://kafka.apache.org) acting a Kafka Producer.

[View](/telegraf/v1/output-plugins/kafka/)

### Amazon Kinesis

Plugin ID: `outputs.kinesis`
Telegraf v0.2.5+

This plugin writes metrics to a [Amazon Kinesis](https://aws.amazon.com/kinesis) endpoint. It will batch all Points in one request to reduce the number of API requests.

Please consult [Amazon’s official documentation](http://docs.aws.amazon.com/kinesis/latest/dev/key-concepts.html) for more details on the Kinesis architecture and concepts.

[View](/telegraf/v1/output-plugins/kinesis/)

### Librato

Plugin ID: `outputs.librato`
Telegraf v0.2.0+

This plugin writes metrics to the [Librato](https://www.librato.com/) service. It requires an `api_user` and `api_token` which can be obtained on the [website](https://metrics.librato.com/account/api_tokens) for your account.

The `source_tag` option in the Configuration file is used to send contextual information from Point Tags to the API. Besides from this, the plugin currently does not send any additional associated Point Tags.

If the point value being sent cannot be converted to a `float64`, the metric is skipped.

[View](/telegraf/v1/output-plugins/librato/)

### Logz.io

Plugin ID: `outputs.logzio`
Telegraf v1.17.0+

This plugin writes metrics to the [Logz.io](https://logz.io) service via HTTP.

[View](/telegraf/v1/output-plugins/logzio/)

### Grafana Loki

Plugin ID: `outputs.loki`
Telegraf v1.18.0+

This plugin writes logs to a [Grafana Loki](https://grafana.com/loki) instance, using the metric name and tags as labels. The log line will contain all fields in `key="value"` format easily parsable with the `logfmt` parser in Loki.

Logs within each stream are sorted by timestamp before being sent to Loki.

[View](/telegraf/v1/output-plugins/loki/)

### Microsoft Fabric

Plugin ID: `outputs.microsoft_fabric`
Telegraf v1.35.0+

This plugin writes metrics to [Fabric Eventhouse](https://learn.microsoft.com/fabric/real-time-intelligence/eventhouse) and [Fabric Eventstream](https://learn.microsoft.com/fabric/real-time-intelligence/event-streams/overview?tabs=enhancedcapabilities) artifacts of [Real-Time Intelligence in Microsoft Fabric](https://learn.microsoft.com/fabric/real-time-intelligence/overview).

Real-Time Intelligence is a SaaS service in Microsoft Fabric that allows you to extract insights and visualize data in motion. It offers an end-to-end solution for event-driven scenarios, streaming data, and data logs.

[View](/telegraf/v1/output-plugins/microsoft_fabric/)

### MongoDB

Plugin ID: `outputs.mongodb`
Telegraf v1.21.0+

This plugin writes metrics to [MongoDB](https://www.mongodb.com) automatically creating collections as time series collections if they don’t exist.

This plugin requires MongoDB v5 or later for time series collections.

[View](/telegraf/v1/output-plugins/mongodb/)

### MQTT Producer

Plugin ID: `outputs.mqtt`
Telegraf v0.2.0+

This plugin writes metrics to a [MQTT broker](http://http://mqtt.org/) acting as a MQTT producer. The plugin supports the MQTT protocols `3.1.1` and `5`.

In v2.0.12+ of the mosquitto MQTT server, there is a [bug](https://github.com/eclipse/mosquitto/issues/2117) requiring the `keep_alive` value to be set non-zero in Telegraf. Otherwise, the server will return with `identifier rejected`. As a reference `eclipse/paho.golang` sets the `keep_alive` to 30.

[View](/telegraf/v1/output-plugins/mqtt/)

### NATS

Plugin ID: `outputs.nats`
Telegraf v1.1.0+

This plugin writes metrics to subjects of a set of [NATS](https://nats.io) instances in one of the supported [data formats](/telegraf/v1/data_formats/output).

[View](/telegraf/v1/output-plugins/nats/)

### Nebius Cloud Monitoring

Plugin ID: `outputs.nebius_cloud_monitoring`
Telegraf v1.27.0+

This plugin writes metrics to the [Nebuis Cloud Monitoring](https://nebius.com/il/services/monitoring) service.

[View](/telegraf/v1/output-plugins/nebius_cloud_monitoring/)

### New Relic

Plugin ID: `outputs.newrelic`
Telegraf v1.15.0+

This plugins writes metrics to [New Relic Insights](https://newrelic.com) using the [Metrics API](https://docs.newrelic.com/docs/data-ingest-apis/get-data-new-relic/metric-api/introduction-metric-api). To use this plugin you have to obtain an [Insights API Key](https://docs.newrelic.com/docs/apis/get-started/intro-apis/types-new-relic-api-keys#user-api-key).

[View](/telegraf/v1/output-plugins/newrelic/)

### NSQ

Plugin ID: `outputs.nsq`
Telegraf v0.2.1+

This plugin writes metrics to the given topic of a [NSQ](https://nsq.io) instance as a producer in one of the supported [data formats](/telegraf/v1/data_formats/output).

[View](/telegraf/v1/output-plugins/nsq/)

### OpenSearch

Plugin ID: `outputs.opensearch`
Telegraf v1.29.0+

This plugin writes metrics to a [OpenSearch](https://opensearch.org/) instance via HTTP. It supports OpenSearch releases v1 and v2 but future comparability with 1.x is not guaranteed and instead will focus on 2.x support.

Consider using the existing Elasticsearch plugin for 1.x.

[View](/telegraf/v1/output-plugins/opensearch/)

### OpenTelemetry

Plugin ID: `outputs.opentelemetry`
Telegraf v1.20.0+

This plugin writes metrics to [OpenTelemetry](https://opentelemetry.io) servers and agents via gRPC.

[View](/telegraf/v1/output-plugins/opentelemetry/)

### OpenTSDB

Plugin ID: `outputs.opentsdb`
Telegraf v0.1.9+

This plugin writes metrics to an [OpenTSDB](http://opentsdb.net/) instance using either the telnet or HTTP mode. Using the HTTP API is recommended since OpenTSDB 2.0.

[View](/telegraf/v1/output-plugins/opentsdb/)

### Parquet

Plugin ID: `outputs.parquet`
Telegraf v1.32.0+

This plugin writes metrics to [parquet](https://parquet.apache.org) files. By default, metrics are grouped by metric name and written all to the same file.

If a metric schema does not match the schema in the file it will be dropped.

To lean more about the parquet format, check out the [parquet docs](https://parquet.apache.org/docs/) as well as a blog post on [querying parquet](https://www.influxdata.com/blog/querying-parquet-millisecond-latency/).

[View](/telegraf/v1/output-plugins/parquet/)

### PostgreSQL

Plugin ID: `outputs.postgresql`
Telegraf v1.24.0+

This plugin writes metrics to a [PostgreSQL](https://www.postgresql.org/) (or compatible) server managing the schema and automatically updating missing columns.

[View](/telegraf/v1/output-plugins/postgresql/)

### Prometheus

Plugin ID: `outputs.prometheus_client`
Telegraf v0.2.1+

This plugin starts a [Prometheus](https://prometheus.io) client and exposes the written metrics on a `/metrics` endpoint by default. This endpoint can then be polled by a Prometheus server.

[View](/telegraf/v1/output-plugins/prometheus_client/)

### Quix

Plugin ID: `outputs.quix`
Telegraf v1.33.0+

This plugin writes metrics to a [Quix](https://quix.io) endpoint.

Please consult Quix’s [official documentation](https://quix.io/docs/) for more details on the Quix platform architecture and concepts.

[View](/telegraf/v1/output-plugins/quix/)

### Redis Time Series

Plugin ID: `outputs.redistimeseries`
Telegraf v1.0.0+

This plugin writes metrics to a [Redis time-series](https://redis.io/timeseries) server.

[View](/telegraf/v1/output-plugins/redistimeseries/)

### Remote File

Plugin ID: `outputs.remotefile`
Telegraf v1.32.0+

This plugin writes metrics to files in a remote location using the [rclone library](https://rclone.org). Currently the following backends are supported:

- `local`: [Local filesystem](https://rclone.org/local/)
- `s3`: [Amazon S3 storage providers](https://rclone.org/s3/)
- `sftp`: [Secure File Transfer Protocol](https://rclone.org/sftp/)

[View](/telegraf/v1/output-plugins/remotefile/)

### Riemann

Plugin ID: `outputs.riemann`
Telegraf v1.3.0+

This plugin writes metric to the [Riemann](http://riemann.io) serice via TCP or UDP.

[View](/telegraf/v1/output-plugins/riemann/)

### Sensu Go

Plugin ID: `outputs.sensu`
Telegraf v1.18.0+

This plugin writes metrics to [Sensu Go](https://sensu.io) via its HTTP events API.

[View](/telegraf/v1/output-plugins/sensu/)

### SignalFx

Plugin ID: `outputs.signalfx`
Telegraf v1.18.0+

This plugin writes metrics to [SignalFx](https://docs.signalfx.com/en/latest/).

[View](/telegraf/v1/output-plugins/signalfx/)

### Socket Writer

Plugin ID: `outputs.socket_writer`
Telegraf v1.3.0+

This plugin writes metrics to a network service e.g. via UDP or TCP in one of the supported [data formats](/telegraf/v1/data_formats/output).

[View](/telegraf/v1/output-plugins/socket_writer/)

### SQL

Plugin ID: `outputs.sql`
Telegraf v1.19.0+

This plugin writes metrics to a supported SQL database using a simple, hard-coded database schema. There is a table for each metric type with the table name corresponding to the metric name. There is a column per field and a column per tag with an optional column for the metric timestamp.

A row is written for every metric. This means multiple metrics are never merged into a single row, even if they have the same metric name, tags, and timestamp.

The plugin uses Golang’s generic “database/sql” interface and third party drivers. See the driver-specific section for a list of supported drivers and details.

[View](/telegraf/v1/output-plugins/sql/)

### Google Cloud Monitoring

Plugin ID: `outputs.stackdriver`
Telegraf v1.9.0+

This plugin writes metrics to a `project` in [Google Cloud Monitoring](https://cloud.google.com/monitoring/api/v3/) (formerly called Stackdriver). [Authentication](https://cloud.google.com/docs/authentication/getting-started) with Google Cloud is required using either a service account or user credentials.

This plugin accesses APIs which are [chargeable](https://cloud.google.com/stackdriver/pricing#google-clouds-operations-suite-pricing) and might incur costs.

By default, Metrics are grouped by the `namespace` variable and metric key, eg: `custom.googleapis.com/telegraf/system/load5`. However, this is not the best practice. Setting `metric_name_format = "official"` will produce a more easily queried format of: `metric_type_prefix/[namespace_]name_key/kind`. If the global namespace is not set, it is omitted as well.

[View](/telegraf/v1/output-plugins/stackdriver/)

### ActiveMQ STOMP

Plugin ID: `outputs.stomp`
Telegraf v1.24.0+

This plugin writes metrics to an [Active MQ Broker](http://activemq.apache.org/) for [STOMP](https://stomp.github.io) but also supports [Amazon MQ](https://aws.amazon.com/amazon-mq) brokers. Metrics can be written in one of the supported [data formats](/telegraf/v1/data_formats/output).

[View](/telegraf/v1/output-plugins/stomp/)

### Sumo Logic

Plugin ID: `outputs.sumologic`
Telegraf v1.16.0+

This plugin writes metrics to a [Sumo Logic HTTP Source](https://help.sumologic.com/03Send-Data/Sources/02Sources-for-Hosted-Collectors/HTTP-Source/Upload-Metrics-to-an-HTTP-Source) using one of the following data formats:

- `graphite` for Content-Type of `application/vnd.sumologic.graphite`
- `carbon2` for Content-Type of `application/vnd.sumologic.carbon2`
- `prometheus` for Content-Type of `application/vnd.sumologic.prometheus`

[View](/telegraf/v1/output-plugins/sumologic/)

### Syslog

Plugin ID: `outputs.syslog`
Telegraf v1.11.0+

This plugin writes metrics as syslog messages via UDP in [RFC5426 format](https://tools.ietf.org/html/rfc5426) or via TCP in [RFC6587 format](https://tools.ietf.org/html/rfc6587) or via TLS in [RFC5425 format](https://tools.ietf.org/html/rfc5425), with or without the octet counting framing.

Syslog messages are formatted according to [RFC5424](https://tools.ietf.org/html/rfc5424) limiting the field sizes when sending messages according to the [syslog message format](https://datatracker.ietf.org/doc/html/rfc5424#section-6) section of the RFC. Sending messages beyond these sizes may get dropped by a strict receiver silently.

[View](/telegraf/v1/output-plugins/syslog/)

### Amazon Timestream

Plugin ID: `outputs.timestream`
Telegraf v1.16.0+

This plugin writes metrics to the [Amazon Timestream](https://aws.amazon.com/timestream) service.

[View](/telegraf/v1/output-plugins/timestream/)

### Warp10

Plugin ID: `outputs.warp10`
Telegraf v1.14.0+

This plugin writes metrics to the [Warp 10](https://www.warp10.io) service.

[View](/telegraf/v1/output-plugins/warp10/)

### Wavefront

Plugin ID: `outputs.wavefront`
Telegraf v1.5.0+

This plugin writes metrics to a [Wavefront](https://www.wavefront.com) instance or a Wavefront Proxy instance over HTTP or HTTPS.

[View](/telegraf/v1/output-plugins/wavefront/)

### Websocket

Plugin ID: `outputs.websocket`
Telegraf v1.19.0+

This plugin writes metrics to a WebSocket endpoint in one of the supported [data formats](/telegraf/v1/data_formats/output).

[View](/telegraf/v1/output-plugins/websocket/)

### Yandex Cloud Monitoring

Plugin ID: `outputs.yandex_cloud_monitoring`
Telegraf v1.17.0+

This plugin writes metrics to the [Yandex Cloud Monitoring](https://cloud.yandex.com/services/monitoring) service.

[View](/telegraf/v1/output-plugins/yandex_cloud_monitoring/)

### Zabbix

Plugin ID: `outputs.zabbix`
Telegraf v1.30.0+

This plugin writes metrics to [Zabbix](https://www.zabbix.com/) via [traps](https://www.zabbix.com/documentation/current/en/manual/appendix/items/trapper). It has been tested with versions v3.0, v4.0 and v6.0 but should work with newer versions of Zabbix as long as the protocol doesn’t change.

[View](/telegraf/v1/output-plugins/zabbix/)

## Aggregator plugins

Telegraf aggregator plugins create aggregate metrics (for example, mean, min, max, quantiles, etc.)

### Basic Statistics

Plugin ID: `aggregators.basicstats`
Telegraf v1.5.0+

This plugin computes basic statistics such as counts, differences, minima, maxima, mean values, non-negative differences etc. for a set of metrics and emits these statistical values every `period`.

[View](/telegraf/v1/aggregator-plugins/basicstats/)

### Derivative

Plugin ID: `aggregators.derivative`
Telegraf v1.18.0+

This plugin computes the derivative for all fields of the aggregated metrics.

[View](/telegraf/v1/aggregator-plugins/derivative/)

### Final

Plugin ID: `aggregators.final`
Telegraf v1.11.0+

This plugin emits the last metric of a contiguous series, defined as a series which receives updates within the time period in `series_timeout`. The contiguous series may be longer than the time interval defined by `period`. When a series has not been updated within the `series_timeout`, the last metric is emitted.

Alternatively, the plugin emits the last metric in the `period` for the `periodic` output strategy.

This is useful for getting the final value for data sources that produce discrete time series such as procstat, cgroup, kubernetes etc. or to downsample metrics collected at a higher frequency.

All emited metrics do have fields with `_final` appended to the field-name by default.

[View](/telegraf/v1/aggregator-plugins/final/)

### Histogram

Plugin ID: `aggregators.histogram`
Telegraf v1.4.0+

This plugin creates histograms containing the counts of field values within the configured range. The histogram metric is emitted every `period`.

In `cumulative` mode, values added to a bucket are also added to the consecutive buckets in the distribution creating a [cumulative histogram](https://en.wikipedia.org/wiki/Histogram#/media/File:Cumulative_vs_normal_histogram.svg).

By default bucket counts are not reset between periods and will be non-strictly increasing while Telegraf is running. This behavior can be by setting the `reset` parameter.

[View](/telegraf/v1/aggregator-plugins/histogram/)

### Merge

Plugin ID: `aggregators.merge`
Telegraf v1.13.0+

This plugin merges metrics of the same series and timestamp into new metrics with the super-set of fields. A series here is defined by the metric name and the tag key-value set.

Use this plugin when fields are split over multiple metrics, with the same measurement, tag set and timestamp.

[View](/telegraf/v1/aggregator-plugins/merge/)

### Minimum-Maximum

Plugin ID: `aggregators.minmax`
Telegraf v1.1.0+

This plugin aggregates the minimum and maximum values of each field it sees, emitting the aggrate every `period` seconds with field names suffixed by `_min` and `_max` respectively.

[View](/telegraf/v1/aggregator-plugins/minmax/)

### Quantile

Plugin ID: `aggregators.quantile`
Telegraf v1.18.0+

This plugin aggregates each numeric field per metric into the specified quantiles and emits the quantiles every `period`. Different aggregation algorithms are supported with varying accuracy and limitations.

[View](/telegraf/v1/aggregator-plugins/quantile/)

### Starlark

Plugin ID: `aggregators.starlark`
Telegraf v1.21.0+

This plugin allows to implement a custom aggregator plugin via a [Starlark](https://github.com/google/starlark-go) script.

The Starlark language is a dialect of Python and will be familiar to those who have experience with the Python language. However, there are major differences. Existing Python code is unlikely to work unmodified.

The execution environment is sandboxed, and it is not possible to access the local filesystem or perfoming network operations. This is by design of the Starlark language as a configuration language.

The Starlark script used by this plugin needs to be composed of the three methods defining an aggreagtor named `add`, `push` and `reset`.

The `add` method is called as soon as a new metric is added to the plugin the metrics to the aggregator. After `period`, the `push` method is called to output the resulting metrics and finally the aggregation is reset by using the `reset` method of the Starlark script.

The Starlark functions might use the global function `state` to keep aggregation information such as added metrics etc.

More details on the syntax and available functions can be found in the [Starlark specification](https://github.com/google/starlark-go/blob/d1966c6b9fcd/doc/spec.md).

[View](/telegraf/v1/aggregator-plugins/starlark/)

### Value Counter

Plugin ID: `aggregators.valuecounter`
Telegraf v1.8.0+

This plugin counts the occurrence of unique values in fields and emits the counter once every `period` with the field-names being suffixed by the unique value converted to `string`.

The fields to be counted must be configured using the `fields` setting, otherwise no field will be counted and no metric is emitted.

This plugin is useful to e.g. count the occurrances of HTTP status codes or other categorical values in the defined `period`.

Counting fields with a high number of potential values may produce a significant amounts of new fields and results in an increased memory usage. Take care to only count fields with a limited set of values.

[View](/telegraf/v1/aggregator-plugins/valuecounter/)

## Processor plugins

Telegraf output plugins transform, decorate, and filter metrics.

### AWS EC2 Metadata

Plugin ID: `processors.aws_ec2`
Telegraf v1.18.0+

This plugin appends metadata gathered from [AWS IMDS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) to metrics associated with EC2 instances.

[View](/telegraf/v1/processor-plugins/aws_ec2/)

### Batch

Plugin ID: `processors.batch`
Telegraf v1.33.0+

This plugin groups metrics into batches by adding a batch tag. This is useful for parallel processing of metrics where downstream processors, aggregators or outputs can then select a batch using `tagpass` or `metricpass`.

Metrics are distributed across batches using the round-robin scheme.

[View](/telegraf/v1/processor-plugins/batch/)

### Clone

Plugin ID: `processors.clone`
Telegraf v1.13.0+

This plugin creates a copy of each metric passing through it, preserving the original metric and allowing modifications such as [metric modifiers](/telegraf/v1/configuration/#modifiers) in the copied metric.

[Metric filtering](/telegraf/v1/configuration/#metric-filtering) options apply to both the clone and the original metric.

[View](/telegraf/v1/processor-plugins/clone/)

### Converter

Plugin ID: `processors.converter`
Telegraf v1.7.0+

This plugin allows transforming tags into fields or timestamps, and converting fields into tags or timestamps. The plugin furthermore allows to change the field type.

When converting tags to fields, take care to ensure the series is still uniquely identifiable. Fields with the same series key (measurement + tags) will overwrite one another.

[View](/telegraf/v1/processor-plugins/converter/)

### Cumulative Sum

Plugin ID: `processors.cumulative_sum`
Telegraf v1.35.0+

This plugin accumulates field values per-metric over time and emit metrics with cumulative sums whenever a metric is updated. This is useful when using outputs relying on monotonically increasing values

Metrics within a series are accumulated in the **order of arrival** and not in order of their timestamps!

[View](/telegraf/v1/processor-plugins/cumulative_sum/)

### Date

Plugin ID: `processors.date`
Telegraf v1.12.0+

This plugin adds the metric timestamp as a human readable tag. A common use is to add a tag that can be used to group by month or year.

[View](/telegraf/v1/processor-plugins/date/)

### Dedup

Plugin ID: `processors.dedup`
Telegraf v1.14.0+

This plugin filters metrics whose field values are exact repetitions of the previous values. This plugin will store its state between runs if the `statefile` option in the agent config section is set.

[View](/telegraf/v1/processor-plugins/dedup/)

### Defaults

Plugin ID: `processors.defaults`
Telegraf v1.15.0+

This plugin allows to specify default values for fields and tags for cases where the tag or field does not exist or has an empty value.

[View](/telegraf/v1/processor-plugins/defaults/)

### Enum

Plugin ID: `processors.enum`
Telegraf v1.8.0+

This plugin allows the mapping of field or tag values according to the configured enumeration. The main use-case is to rewrite numerical values into human-readable values or vice versa. Default mappings can be configured to be used for all remaining values.

[View](/telegraf/v1/processor-plugins/enum/)

### Execd

Plugin ID: `processors.execd`
Telegraf v1.15.0+

This plugin runs an external program as a separate process and pipes metrics in to the process’s `stdin` and reads processed metrics from its `stdout`. Program output on `stderr` is logged.

[View](/telegraf/v1/processor-plugins/execd/)

### Filepath

Plugin ID: `processors.filepath`
Telegraf v1.15.0+

This plugin allows transforming a path, using e.g. basename to extract the last path element, for tag and field values. Values can be modified in place or stored in another key.

[View](/telegraf/v1/processor-plugins/filepath/)

### Filter

Plugin ID: `processors.filter`
Telegraf v1.29.0+

This plugin allows specifying a set of rules for metrics with the ability to *keep* or *drop* those metrics. It does *not* modify the metric. As such a user might want to apply this processor to remove metrics from the processing/output stream.

The filtering is *not* output specific, but will apply to the metrics processed by this processor.

[View](/telegraf/v1/processor-plugins/filter/)

### Network Interface Name

Plugin ID: `processors.ifname`
Telegraf v1.15.0+

This plugin looks up network interface names using SNMP.

[View](/telegraf/v1/processor-plugins/ifname/)

### Lookup

Plugin ID: `processors.lookup`
Telegraf v1.15.0+

This plugin allows to use one or more files containing lookup-tables for annotating incoming metrics. The lookup is *static* as the files are only used on startup. The main use-case for this is to annotate metrics with additional tags e.g. dependent on their source. Multiple tags can be added depending on the lookup-table *files*.

The lookup key can be generated using a Golang template with the ability to access the metric name via `{{.Name}}`, the tag values via `{{.Tag "mytag"}}`, with `mytag` being the tag-name and field-values via `{{.Field "myfield"}}`, with `myfield` being the field-name. Non-existing tags and field will result in an empty string or `nil` respectively. In case the key cannot be found, the metric is passed-through unchanged. By default all matching tags are added and existing tag-values are overwritten.

The plugin only supports the addition of tags and thus all mapped tag-values need to be strings!

[View](/telegraf/v1/processor-plugins/lookup/)

### Noise

Plugin ID: `processors.noise`
Telegraf v1.22.0+

This plugin is used to add noise to numerical field values. For each field a noise is generated using a defined probability density function and added to the value. The function type can be configured as *Laplace*, *Gaussian* or *Uniform*.

[View](/telegraf/v1/processor-plugins/noise/)

### Override

Plugin ID: `processors.override`
Telegraf v1.6.0+

This plugin allows to modify metrics using [metric modifiers](/telegraf/v1/configuration/#modifiers). Use-cases of this plugin encompass ensuring certain tags or naming conventions are adhered to irrespective of input plugin configurations, e.g. by `taginclude`.

[Metric filtering](/telegraf/v1/configuration/#metric-filtering) options apply to both the clone and the original metric.

[View](/telegraf/v1/processor-plugins/override/)

### Parser

Plugin ID: `processors.parser`
Telegraf v1.8.0+

This plugin parses defined fields or tags containing the specified [data format](/telegraf/v1/data_formats/input) and creates new metrics based on the resulting fields and tags.

[View](/telegraf/v1/processor-plugins/parser/)

### Pivot

Plugin ID: `processors.pivot`
Telegraf v1.12.0+

This plugin rotates single-valued metrics into a multi-field metric. The result is a more compact representation for applying mathematical operators to or do comparisons between metrics or flatten fields.

To perform the reverse operation use the [unpivot](/telegraf/v1/plugins/#processor-unpivot) processor.

[View](/telegraf/v1/processor-plugins/pivot/)

### Port Name Lookup

Plugin ID: `processors.port_name`
Telegraf v1.15.0+

This plugin allows converting a tag or field containing a well-known port, either a number (e.g. `80`) for TCP ports or a port and protocol (e.g. `443/tcp`), to the registered service name.

[View](/telegraf/v1/processor-plugins/port_name/)

### Printer

Plugin ID: `processors.printer`
Telegraf v1.1.0+

This plugin prints every metric passing through it to the standard output.

[View](/telegraf/v1/processor-plugins/printer/)

### Regex

Plugin ID: `processors.regex`
Telegraf v1.7.0+

This plugin transforms tag and field *values* as well as renaming tags, fields and metrics using regular expression patterns. Tag and field *values* can be transformed using named-groups in a batch fashion.

The regex processor **only operates on string fields**. It will not work on any other data types, like an integer or float.

[View](/telegraf/v1/processor-plugins/regex/)

### Rename

Plugin ID: `processors.rename`
Telegraf v1.8.0+

This plugin allows to rename measurements, fields and tags.

[View](/telegraf/v1/processor-plugins/rename/)

### Reverse DNS

Plugin ID: `processors.reverse_dns`
Telegraf v1.15.0+

This plugin does a reverse-dns lookup on tags or fields containing IPs and creates a tag or field containing the corresponding DNS name.

[View](/telegraf/v1/processor-plugins/reverse_dns/)

### Round

Plugin ID: `processors.round`
Telegraf v1.36.0+

This plugin allows to round numerical field values to the configured precision. This is particularly useful in combination with the [dedup processor](/telegraf/v1/plugins/#processor-dedup) to reduce the number of metrics sent to the output if only a lower precision is required for the values.

[View](/telegraf/v1/processor-plugins/round/)

### S2 Geo

Plugin ID: `processors.s2geo`
Telegraf v1.14.0+

This plugin uses the WGS-84 coordinates in decimal degrees specified in the latitude and longitude fields and adds a tag with the corresponding S2 cell ID token of specified [cell level](https://s2geometry.io/resources/s2cell_statistics.html).

[View](/telegraf/v1/processor-plugins/s2geo/)

### Scale

Plugin ID: `processors.scale`
Telegraf v1.27.0+

This plugin allows to scale field-values from an input range into the given output range according to this formula:

Alternatively, you can apply a factor and offset to the input according to this formula

Input fields are converted to floating point values if possible. Otherwise, fields that cannot be converted are ignored and keep their original value.

Neither the input nor output values are clipped to their respective ranges!

[View](/telegraf/v1/processor-plugins/scale/)

### SNMP Lookup

Plugin ID: `processors.snmp_lookup`
Telegraf v1.30.0+

This plugin looks up extra information via SNMP and adds it to the metric as tags.

[View](/telegraf/v1/processor-plugins/snmp_lookup/)

### Split

Plugin ID: `processors.split`
Telegraf v1.28.0+

This plugin splits a metric up into one or more metrics based on a configured template. The resulting metrics will be timestamped according to the source metric. Templates can overlap, where a field or tag, is used across templates and as a result end up in multiple metrics.

If drop original is changed to true, then the plugin can result in dropping all metrics when no match is found! Please ensure to test templates before putting into production *and* use metric filtering to avoid data loss.

[View](/telegraf/v1/processor-plugins/split/)

### Starlark

Plugin ID: `processors.starlark`
Telegraf v1.15.0+

This plugin calls the provided Starlark function for each matched metric, allowing for custom programmatic metric processing.

The Starlark language is a dialect of Python, and will be familiar to those who have experience with the Python language. However, there are major differences. Existing Python code is unlikely to work unmodified. The execution environment is sandboxed, and it is not possible to do I/O operations such as reading from files or sockets.

The **[Starlark specification](https://github.com/google/starlark-go/blob/d1966c6b9fcd/doc/spec.md)** has details about the syntax and available functions.

[View](/telegraf/v1/processor-plugins/starlark/)

### Strings

Plugin ID: `processors.strings`
Telegraf v1.8.0+

This plugin allows to manipulate strings in the measurement name, tag and field values using different functions.

[View](/telegraf/v1/processor-plugins/strings/)

### Tag Limit

Plugin ID: `processors.tag_limit`
Telegraf v1.12.0+

This plugin ensures that only a certain number of tags are preserved for any given metric, and to choose the tags to preserve when the number of tags appended by the data source is over the limit.

This can be useful when dealing with output systems (e.g. Stackdriver) that impose hard limits on the number of tags/labels per metric or where high levels of cardinality are computationally and/or financially expensive.

[View](/telegraf/v1/processor-plugins/tag_limit/)

### Template

Plugin ID: `processors.template`
Telegraf v1.14.0+

This plugin applies templates to metrics for generating a new tag. The primary use case of this plugin is to create a tag that can be used for dynamic routing to multiple output plugins or using an output specific routing option.

The template has access to each metric’s measurement name, tags, fields, and timestamp. Templates follow the [Go Template syntax](https://golang.org/pkg/text/template/) and may contain [Sprig functions](http://masterminds.github.io/sprig/).

[View](/telegraf/v1/processor-plugins/template/)

### Timestamp

Plugin ID: `processors.timestamp`
Telegraf v1.31.0+

This plugin allows to parse fields containing timestamps into timestamps of other format.

[View](/telegraf/v1/processor-plugins/timestamp/)

### TopK

Plugin ID: `processors.topk`
Telegraf v1.7.0+

This plugin filters the top series over a period of time and calculates the top metrics via different aggregation functions. The processing steps comprise grouping the metrics based on the metric name and tags, computing the aggregate functions for each group every period and outputting the top `K` groups.

[View](/telegraf/v1/processor-plugins/topk/)

### Unpivot

Plugin ID: `processors.unpivot`
Telegraf v1.12.0+

This plugin allows to rotate a multi-field series into single-valued metrics. The resulting metrics allow to more easily aggregate data across fields.

To perform the reverse operation use the [pivot](/telegraf/v1/plugins/#processor-pivot) processor.

[View](/telegraf/v1/processor-plugins/unpivot/)

---

## Telegraf Output Plugins

Telegraf output plugins send metrics to various destinations.

### Amon

Plugin ID: `outputs.amon`
Telegraf v0.2.1 - v1.37.0 Deprecated

This plugin writes metrics to [Amon monitoring platform](https://www.amon.cx). It requires a `serverkey` and `amoninstance` URL which can be obtained from the [website](https://www.amon.cx/docs/monitoring/) for your account.

If point values being sent cannot be converted to a `float64`, the metric is skipped.

[View](/telegraf/v1/output-plugins/amon/)

### AMQP

Plugin ID: `outputs.amqp`
Telegraf v0.1.9+

This plugin writes to an Advanced Message Queuing Protocol v0.9.1 broker. A prominent implementation of this protocol is [RabbitMQ](https://www.rabbitmq.com).

This plugin does not bind the AMQP exchange to a queue.

For an introduction check the [AMQP concepts page](https://www.rabbitmq.com/tutorials/amqp-concepts.html) and the [RabbitMQ getting started guide](https://www.rabbitmq.com/getstarted.html).

[View](/telegraf/v1/output-plugins/amqp/)

### Azure Application Insights

Plugin ID: `outputs.application_insights`
Telegraf v1.7.0+

This plugin writes metrics to the [Azure Application Insights](https://azure.microsoft.com/en-us/services/application-insights/) service.

[View](/telegraf/v1/output-plugins/application_insights/)

### Arc

Plugin ID: `outputs.arc`
Telegraf v1.37.0+

This plugin writes metrics to [Arc](https://github.com/basekick-labs/arc), a high-performance time-series database, via MessagePack binary protocol messages providing a **3-5x better performance** than the line-protocol format.

[View](/telegraf/v1/output-plugins/arc/)

### Azure Data Explorer

Plugin ID: `outputs.azure_data_explorer`
Telegraf v1.20.0+

This plugin writes metrics to the [Azure Data Explorer](https://docs.microsoft.com/en-us/azure/data-explorer), [Azure Synapse Data Explorer](https://docs.microsoft.com/en-us/azure/synapse-analytics/data-explorer/data-explorer-overview), and [Real time analytics in Fabric](https://learn.microsoft.com/en-us/fabric/real-time-analytics/overview) services.

Azure Data Explorer is a distributed, columnar store, purpose built for any type of logs, metrics and time series data.

[View](/telegraf/v1/output-plugins/azure_data_explorer/)

### Azure Monitor

Plugin ID: `outputs.azure_monitor`
Telegraf v1.8.0+

This plugin writes metrics to [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor) which has a metric resolution of one minute. To accomodate for this in Telegraf, the plugin will automatically aggregate metrics into one minute buckets and send them to the service on every flush interval.

The Azure Monitor custom metrics service is currently in preview and might not be available in all Azure regions. Please also take the metric time limitations into account!

The metrics from each input plugin will be written to a separate Azure Monitor namespace, prefixed with `Telegraf/` by default. The field name for each metric is written as the Azure Monitor metric name. All field values are written as a summarized set that includes: min, max, sum, count. Tags are written as a dimension on each Azure Monitor metric.

[View](/telegraf/v1/output-plugins/azure_monitor/)

### Google BigQuery

Plugin ID: `outputs.bigquery`
Telegraf v1.18.0+

This plugin writes metrics to the [Google Cloud BigQuery](https://cloud.google.com/bigquery) service and requires [authentication](https://cloud.google.com/bigquery/docs/authentication) with Google Cloud using either a service account or user credentials.

Be aware that this plugin accesses APIs that are [chargeable](https://cloud.google.com/bigquery/pricing) and might incur costs.

[View](/telegraf/v1/output-plugins/bigquery/)

### Clarify

Plugin ID: `outputs.clarify`
Telegraf v1.27.0+

This plugin writes metrics to [Clarify](https://clarify.io). To use this plugin you will need to obtain a set of [credentials](https://docs.clarify.io/users/admin/integrations/credentials).

[View](/telegraf/v1/output-plugins/clarify/)

### Google Cloud PubSub

Plugin ID: `outputs.cloud_pubsub`
Telegraf v1.10.0+

This plugin publishes metrics to a [Google Cloud PubSub](https://cloud.google.com/pubsub) topic in one of the supported [data formats](/telegraf/v1/data_formats/output).

[View](/telegraf/v1/output-plugins/cloud_pubsub/)

### Amazon CloudWatch

Plugin ID: `outputs.cloudwatch`
Telegraf v0.10.1+

This plugin writes metrics to the [Amazon CloudWatch](https://aws.amazon.com/cloudwatch) service.

[View](/telegraf/v1/output-plugins/cloudwatch/)

### Amazon CloudWatch Logs

Plugin ID: `outputs.cloudwatch_logs`
Telegraf v1.19.0+

This plugin writes log-metrics to the [Amazon CloudWatch](https://aws.amazon.com/cloudwatch) service.

[View](/telegraf/v1/output-plugins/cloudwatch_logs/)

### CrateDB

Plugin ID: `outputs.cratedb`
Telegraf v1.5.0+

This plugin writes metrics to [CrateDB](https://crate.io/) via its [PostgreSQL protocol](https://crate.io/docs/crate/reference/protocols/postgres.html).

[View](/telegraf/v1/output-plugins/cratedb/)

### Datadog

Plugin ID: `outputs.datadog`
Telegraf v0.1.6+

This plugin writes metrics to the [Datadog Metrics API](https://docs.datadoghq.com/api/v1/metrics/#submit-metrics) and requires an `apikey` which can be obtained on the [website](https://app.datadoghq.com/account/settings#api) for the account.

This plugin supports the v1 API.

[View](/telegraf/v1/output-plugins/datadog/)

### Discard

Plugin ID: `outputs.discard`
Telegraf v1.2.0+

This plugin discards all metrics written to it and is meant for testing purposes.

[View](/telegraf/v1/output-plugins/discard/)

### Dynatrace

Plugin ID: `outputs.dynatrace`
Telegraf v1.16.0+

This plugin writes metrics to [Dynatrace](https://www.dynatrace.com) via the [Dynatrace Metrics API V2](https://docs.dynatrace.com/docs/shortlink/api-metrics-v2). It may be run alongside the Dynatrace OneAgent for automatic authentication or it may be run standalone on a host without OneAgent by specifying a URL and API Token.

More information on the plugin can be found in the [Dynatrace documentation](https://docs.dynatrace.com/docs/shortlink/telegraf).

All metrics are reported as gauges, unless they are specified to be delta counters using the `additional_counters` or `additional_counters_patterns` config option (see below). See the [Dynatrace Metrics ingestion protocol documentation](https://docs.dynatrace.com/docs/shortlink/metric-ingestion-protocol) for details on the types defined there.

[View](/telegraf/v1/output-plugins/dynatrace/)

### Elasticsearch

Plugin ID: `outputs.elasticsearch`
Telegraf v0.1.5+

This plugin writes metrics to [Elasticsearch](https://www.elastic.co) via HTTP using the [Elastic client library](http://olivere.github.io/elastic/). The plugin supports Elasticsearch releases from v5.x up to v7.x.

[View](/telegraf/v1/output-plugins/elasticsearch/)

### Azure Event Hubs

Plugin ID: `outputs.event_hubs`
Telegraf v1.21.0+

This plugin writes metrics to the [Azure Event Hubs](https://azure.microsoft.com/en-gb/services/event-hubs/) service in any of the supported [data formats](/telegraf/v1/data_formats/output). Metrics are sent as batches with each message payload containing one metric object, preferably as JSON as this eases integration with downstream components.

Each patch is sent to a single Event Hub within a namespace. In case no partition key is specified the batches will be automatically load-balanced (round-robin) across all the Event Hub partitions.

[View](/telegraf/v1/output-plugins/event_hubs/)

### Executable

Plugin ID: `outputs.exec`
Telegraf v1.12.0+

This plugin writes metrics to an external application via `stdin`. The command will be executed on each write creating a new process. Metrics are passed in one of the supported [data formats](/telegraf/v1/data_formats/output).

The executable and the individual parameters must be defined as a list. All outputs of the executable to `stderr` will be logged in the Telegraf log.

For better performance consider execd which runs continuously.

[View](/telegraf/v1/output-plugins/exec/)

### Executable Daemon

Plugin ID: `outputs.execd`
Telegraf v1.15.0+

This plugin writes metrics to an external daemon program via `stdin`. The command will be executed once and metrics will be passed to it on every write in one of the supported [data formats](/telegraf/v1/data_formats/output). The executable and the individual parameters must be defined as a list.

All outputs of the executable to `stderr` will be logged in the Telegraf log. Telegraf minimum version: Telegraf 1.15.0

[View](/telegraf/v1/output-plugins/execd/)

### File

Plugin ID: `outputs.file`
Telegraf v0.10.3+

This plugin writes metrics to one or more local files in one of the supported [data formats](/telegraf/v1/data_formats/output).

[View](/telegraf/v1/output-plugins/file/)

### Graphite

Plugin ID: `outputs.graphite`
Telegraf v0.10.1+

This plugin writes metrics to [Graphite](http://graphite.readthedocs.org/en/latest/index.html) via TCP. For details on the translation between Telegraf Metrics and Graphite output see the [Graphite data format](/telegraf/v1/plugins/#serializer-graphite).

[View](/telegraf/v1/output-plugins/graphite/)

### Graylog

Plugin ID: `outputs.graylog`
Telegraf v1.0.0+

This plugin writes metrics to a [Graylog](https://graylog.org/) instance using the [GELF data format](https://docs.graylog.org/en/3.1/pages/gelf.html#gelf-payload-specification).

[View](/telegraf/v1/output-plugins/graylog/)

### GroundWork

Plugin ID: `outputs.groundwork`
Telegraf v1.21.0+

This plugin writes metrics to a [GroundWork Monitor](https://www.gwos.com/product/groundwork-monitor/) instance.

Plugin only supports GroundWork v8 or later.

[View](/telegraf/v1/output-plugins/groundwork/)

### Health

Plugin ID: `outputs.health`
Telegraf v1.11.0+

This plugin provides a HTTP health check endpoint that can be configured to return failure status codes based on the value of a metric.

When the plugin is healthy it will return a 200 response; when unhealthy it will return a 503 response. The default state is healthy, one or more checks must fail in order for the resource to enter the failed state.

[View](/telegraf/v1/output-plugins/health/)

### Heartbeat

Plugin ID: `outputs.heartbeat`
Telegraf v1.37.0+

This plugin sends a heartbeat signal via POST to a HTTP endpoint on a regular interval. This is useful to keep track of existing Telegraf instances in a large deployment.

[View](/telegraf/v1/output-plugins/heartbeat/)

### HTTP

Plugin ID: `outputs.http`
Telegraf v1.7.0+

This plugin writes metrics to a HTTP endpoint using one of the supported [data formats](/telegraf/v1/data_formats/output). For data formats supporting batching, metrics are sent in batches by default.

[View](/telegraf/v1/output-plugins/http/)

### InfluxDB v1.x

Plugin ID: `outputs.influxdb`
Telegraf v0.1.1+

This plugin writes metrics to a [InfluxDB v1.x](https://docs.influxdata.com/influxdb/v1) instance via HTTP or UDP protocol.

[View](/telegraf/v1/output-plugins/influxdb/)

### InfluxDB v2.x

Plugin ID: `outputs.influxdb_v2`
Telegraf v1.8.0+

This plugin writes metrics to a [InfluxDB v2.x](https://docs.influxdata.com/influxdb/v2) instance via HTTP.

[View](/telegraf/v1/output-plugins/influxdb_v2/)

### Inlong

Plugin ID: `outputs.inlong`
Telegraf v1.35.0+

This plugin publishes metrics to an [Apache InLong](https://inlong.apache.org) instance.

[View](/telegraf/v1/output-plugins/inlong/)

### Instrumental

Plugin ID: `outputs.instrumental`
Telegraf v0.13.1+

This plugin writes metrics to the [Instrumental Collector API](https://instrumentalapp.com/docs/tcp-collector) and requires a project-specific API token.

Instrumental accepts stats in a format very close to Graphite, with the only difference being that the type of stat (gauge, increment) is the first token, separated from the metric itself by whitespace. The `increment` type is only used if the metric comes in as a counter via the [statsd input plugin](/telegraf/v1/plugins/#input-statsd).

[View](/telegraf/v1/output-plugins/instrumental/)

### Apache IoTDB

Plugin ID: `outputs.iotdb`
Telegraf v1.24.0+

This plugin writes metrics to an [Apache IoTDB](https://iotdb.apache.org) instance, a database for the Internet of Things, supporting session connection and data insertion.

[View](/telegraf/v1/output-plugins/iotdb/)

### Kafka

Plugin ID: `outputs.kafka`
Telegraf v0.1.7+

This plugin writes metrics to a [Kafka Broker](http://kafka.apache.org) acting a Kafka Producer.

[View](/telegraf/v1/output-plugins/kafka/)

### Amazon Kinesis

Plugin ID: `outputs.kinesis`
Telegraf v0.2.5+

This plugin writes metrics to a [Amazon Kinesis](https://aws.amazon.com/kinesis) endpoint. It will batch all Points in one request to reduce the number of API requests.

Please consult [Amazon’s official documentation](http://docs.aws.amazon.com/kinesis/latest/dev/key-concepts.html) for more details on the Kinesis architecture and concepts.

[View](/telegraf/v1/output-plugins/kinesis/)

### Librato

Plugin ID: `outputs.librato`
Telegraf v0.2.0+

This plugin writes metrics to the [Librato](https://www.librato.com/) service. It requires an `api_user` and `api_token` which can be obtained on the [website](https://metrics.librato.com/account/api_tokens) for your account.

The `source_tag` option in the Configuration file is used to send contextual information from Point Tags to the API. Besides from this, the plugin currently does not send any additional associated Point Tags.

If the point value being sent cannot be converted to a `float64`, the metric is skipped.

[View](/telegraf/v1/output-plugins/librato/)

### Logz.io

Plugin ID: `outputs.logzio`
Telegraf v1.17.0+

This plugin writes metrics to the [Logz.io](https://logz.io) service via HTTP.

[View](/telegraf/v1/output-plugins/logzio/)

### Grafana Loki

Plugin ID: `outputs.loki`
Telegraf v1.18.0+

This plugin writes logs to a [Grafana Loki](https://grafana.com/loki) instance, using the metric name and tags as labels. The log line will contain all fields in `key="value"` format easily parsable with the `logfmt` parser in Loki.

Logs within each stream are sorted by timestamp before being sent to Loki.

[View](/telegraf/v1/output-plugins/loki/)

### Microsoft Fabric

Plugin ID: `outputs.microsoft_fabric`
Telegraf v1.35.0+

This plugin writes metrics to [Fabric Eventhouse](https://learn.microsoft.com/fabric/real-time-intelligence/eventhouse) and [Fabric Eventstream](https://learn.microsoft.com/fabric/real-time-intelligence/event-streams/overview?tabs=enhancedcapabilities) artifacts of [Real-Time Intelligence in Microsoft Fabric](https://learn.microsoft.com/fabric/real-time-intelligence/overview).

Real-Time Intelligence is a SaaS service in Microsoft Fabric that allows you to extract insights and visualize data in motion. It offers an end-to-end solution for event-driven scenarios, streaming data, and data logs.

[View](/telegraf/v1/output-plugins/microsoft_fabric/)

### MongoDB

Plugin ID: `outputs.mongodb`
Telegraf v1.21.0+

This plugin writes metrics to [MongoDB](https://www.mongodb.com) automatically creating collections as time series collections if they don’t exist.

This plugin requires MongoDB v5 or later for time series collections.

[View](/telegraf/v1/output-plugins/mongodb/)

### MQTT Producer

Plugin ID: `outputs.mqtt`
Telegraf v0.2.0+

This plugin writes metrics to a [MQTT broker](http://http://mqtt.org/) acting as a MQTT producer. The plugin supports the MQTT protocols `3.1.1` and `5`.

In v2.0.12+ of the mosquitto MQTT server, there is a [bug](https://github.com/eclipse/mosquitto/issues/2117) requiring the `keep_alive` value to be set non-zero in Telegraf. Otherwise, the server will return with `identifier rejected`. As a reference `eclipse/paho.golang` sets the `keep_alive` to 30.

[View](/telegraf/v1/output-plugins/mqtt/)

### NATS

Plugin ID: `outputs.nats`
Telegraf v1.1.0+

This plugin writes metrics to subjects of a set of [NATS](https://nats.io) instances in one of the supported [data formats](/telegraf/v1/data_formats/output).

[View](/telegraf/v1/output-plugins/nats/)

### Nebius Cloud Monitoring

Plugin ID: `outputs.nebius_cloud_monitoring`
Telegraf v1.27.0+

This plugin writes metrics to the [Nebuis Cloud Monitoring](https://nebius.com/il/services/monitoring) service.

[View](/telegraf/v1/output-plugins/nebius_cloud_monitoring/)

### New Relic

Plugin ID: `outputs.newrelic`
Telegraf v1.15.0+

This plugins writes metrics to [New Relic Insights](https://newrelic.com) using the [Metrics API](https://docs.newrelic.com/docs/data-ingest-apis/get-data-new-relic/metric-api/introduction-metric-api). To use this plugin you have to obtain an [Insights API Key](https://docs.newrelic.com/docs/apis/get-started/intro-apis/types-new-relic-api-keys#user-api-key).

[View](/telegraf/v1/output-plugins/newrelic/)

### NSQ

Plugin ID: `outputs.nsq`
Telegraf v0.2.1+

This plugin writes metrics to the given topic of a [NSQ](https://nsq.io) instance as a producer in one of the supported [data formats](/telegraf/v1/data_formats/output).

[View](/telegraf/v1/output-plugins/nsq/)

### OpenSearch

Plugin ID: `outputs.opensearch`
Telegraf v1.29.0+

This plugin writes metrics to a [OpenSearch](https://opensearch.org/) instance via HTTP. It supports OpenSearch releases v1 and v2 but future comparability with 1.x is not guaranteed and instead will focus on 2.x support.

Consider using the existing Elasticsearch plugin for 1.x.

[View](/telegraf/v1/output-plugins/opensearch/)

### OpenTelemetry

Plugin ID: `outputs.opentelemetry`
Telegraf v1.20.0+

This plugin writes metrics to [OpenTelemetry](https://opentelemetry.io) servers and agents via gRPC.

[View](/telegraf/v1/output-plugins/opentelemetry/)

### OpenTSDB

Plugin ID: `outputs.opentsdb`
Telegraf v0.1.9+

This plugin writes metrics to an [OpenTSDB](http://opentsdb.net/) instance using either the telnet or HTTP mode. Using the HTTP API is recommended since OpenTSDB 2.0.

[View](/telegraf/v1/output-plugins/opentsdb/)

### Parquet

Plugin ID: `outputs.parquet`
Telegraf v1.32.0+

This plugin writes metrics to [parquet](https://parquet.apache.org) files. By default, metrics are grouped by metric name and written all to the same file.

If a metric schema does not match the schema in the file it will be dropped.

To lean more about the parquet format, check out the [parquet docs](https://parquet.apache.org/docs/) as well as a blog post on [querying parquet](https://www.influxdata.com/blog/querying-parquet-millisecond-latency/).

[View](/telegraf/v1/output-plugins/parquet/)

### PostgreSQL

Plugin ID: `outputs.postgresql`
Telegraf v1.24.0+

This plugin writes metrics to a [PostgreSQL](https://www.postgresql.org/) (or compatible) server managing the schema and automatically updating missing columns.

[View](/telegraf/v1/output-plugins/postgresql/)

### Prometheus

Plugin ID: `outputs.prometheus_client`
Telegraf v0.2.1+

This plugin starts a [Prometheus](https://prometheus.io) client and exposes the written metrics on a `/metrics` endpoint by default. This endpoint can then be polled by a Prometheus server.

[View](/telegraf/v1/output-plugins/prometheus_client/)

### Quix

Plugin ID: `outputs.quix`
Telegraf v1.33.0+

This plugin writes metrics to a [Quix](https://quix.io) endpoint.

Please consult Quix’s [official documentation](https://quix.io/docs/) for more details on the Quix platform architecture and concepts.

[View](/telegraf/v1/output-plugins/quix/)

### Redis Time Series

Plugin ID: `outputs.redistimeseries`
Telegraf v1.0.0+

This plugin writes metrics to a [Redis time-series](https://redis.io/timeseries) server.

[View](/telegraf/v1/output-plugins/redistimeseries/)

### Remote File

Plugin ID: `outputs.remotefile`
Telegraf v1.32.0+

This plugin writes metrics to files in a remote location using the [rclone library](https://rclone.org). Currently the following backends are supported:

- `local`: [Local filesystem](https://rclone.org/local/)
- `s3`: [Amazon S3 storage providers](https://rclone.org/s3/)
- `sftp`: [Secure File Transfer Protocol](https://rclone.org/sftp/)

[View](/telegraf/v1/output-plugins/remotefile/)

### Riemann

Plugin ID: `outputs.riemann`
Telegraf v1.3.0+

This plugin writes metric to the [Riemann](http://riemann.io) serice via TCP or UDP.

[View](/telegraf/v1/output-plugins/riemann/)

### Sensu Go

Plugin ID: `outputs.sensu`
Telegraf v1.18.0+

This plugin writes metrics to [Sensu Go](https://sensu.io) via its HTTP events API.

[View](/telegraf/v1/output-plugins/sensu/)

### SignalFx

Plugin ID: `outputs.signalfx`
Telegraf v1.18.0+

This plugin writes metrics to [SignalFx](https://docs.signalfx.com/en/latest/).

[View](/telegraf/v1/output-plugins/signalfx/)

### Socket Writer

Plugin ID: `outputs.socket_writer`
Telegraf v1.3.0+

This plugin writes metrics to a network service e.g. via UDP or TCP in one of the supported [data formats](/telegraf/v1/data_formats/output).

[View](/telegraf/v1/output-plugins/socket_writer/)

### SQL

Plugin ID: `outputs.sql`
Telegraf v1.19.0+

This plugin writes metrics to a supported SQL database using a simple, hard-coded database schema. There is a table for each metric type with the table name corresponding to the metric name. There is a column per field and a column per tag with an optional column for the metric timestamp.

A row is written for every metric. This means multiple metrics are never merged into a single row, even if they have the same metric name, tags, and timestamp.

The plugin uses Golang’s generic “database/sql” interface and third party drivers. See the driver-specific section for a list of supported drivers and details.

[View](/telegraf/v1/output-plugins/sql/)

### Google Cloud Monitoring

Plugin ID: `outputs.stackdriver`
Telegraf v1.9.0+

This plugin writes metrics to a `project` in [Google Cloud Monitoring](https://cloud.google.com/monitoring/api/v3/) (formerly called Stackdriver). [Authentication](https://cloud.google.com/docs/authentication/getting-started) with Google Cloud is required using either a service account or user credentials.

This plugin accesses APIs which are [chargeable](https://cloud.google.com/stackdriver/pricing#google-clouds-operations-suite-pricing) and might incur costs.

By default, Metrics are grouped by the `namespace` variable and metric key, eg: `custom.googleapis.com/telegraf/system/load5`. However, this is not the best practice. Setting `metric_name_format = "official"` will produce a more easily queried format of: `metric_type_prefix/[namespace_]name_key/kind`. If the global namespace is not set, it is omitted as well.

[View](/telegraf/v1/output-plugins/stackdriver/)

### ActiveMQ STOMP

Plugin ID: `outputs.stomp`
Telegraf v1.24.0+

This plugin writes metrics to an [Active MQ Broker](http://activemq.apache.org/) for [STOMP](https://stomp.github.io) but also supports [Amazon MQ](https://aws.amazon.com/amazon-mq) brokers. Metrics can be written in one of the supported [data formats](/telegraf/v1/data_formats/output).

[View](/telegraf/v1/output-plugins/stomp/)

### Sumo Logic

Plugin ID: `outputs.sumologic`
Telegraf v1.16.0+

This plugin writes metrics to a [Sumo Logic HTTP Source](https://help.sumologic.com/03Send-Data/Sources/02Sources-for-Hosted-Collectors/HTTP-Source/Upload-Metrics-to-an-HTTP-Source) using one of the following data formats:

- `graphite` for Content-Type of `application/vnd.sumologic.graphite`
- `carbon2` for Content-Type of `application/vnd.sumologic.carbon2`
- `prometheus` for Content-Type of `application/vnd.sumologic.prometheus`

[View](/telegraf/v1/output-plugins/sumologic/)

### Syslog

Plugin ID: `outputs.syslog`
Telegraf v1.11.0+

This plugin writes metrics as syslog messages via UDP in [RFC5426 format](https://tools.ietf.org/html/rfc5426) or via TCP in [RFC6587 format](https://tools.ietf.org/html/rfc6587) or via TLS in [RFC5425 format](https://tools.ietf.org/html/rfc5425), with or without the octet counting framing.

Syslog messages are formatted according to [RFC5424](https://tools.ietf.org/html/rfc5424) limiting the field sizes when sending messages according to the [syslog message format](https://datatracker.ietf.org/doc/html/rfc5424#section-6) section of the RFC. Sending messages beyond these sizes may get dropped by a strict receiver silently.

[View](/telegraf/v1/output-plugins/syslog/)

### Amazon Timestream

Plugin ID: `outputs.timestream`
Telegraf v1.16.0+

This plugin writes metrics to the [Amazon Timestream](https://aws.amazon.com/timestream) service.

[View](/telegraf/v1/output-plugins/timestream/)

### Warp10

Plugin ID: `outputs.warp10`
Telegraf v1.14.0+

This plugin writes metrics to the [Warp 10](https://www.warp10.io) service.

[View](/telegraf/v1/output-plugins/warp10/)

### Wavefront

Plugin ID: `outputs.wavefront`
Telegraf v1.5.0+

This plugin writes metrics to a [Wavefront](https://www.wavefront.com) instance or a Wavefront Proxy instance over HTTP or HTTPS.

[View](/telegraf/v1/output-plugins/wavefront/)

### Websocket

Plugin ID: `outputs.websocket`
Telegraf v1.19.0+

This plugin writes metrics to a WebSocket endpoint in one of the supported [data formats](/telegraf/v1/data_formats/output).

[View](/telegraf/v1/output-plugins/websocket/)

### Yandex Cloud Monitoring

Plugin ID: `outputs.yandex_cloud_monitoring`
Telegraf v1.17.0+

This plugin writes metrics to the [Yandex Cloud Monitoring](https://cloud.yandex.com/services/monitoring) service.

[View](/telegraf/v1/output-plugins/yandex_cloud_monitoring/)

### Zabbix

Plugin ID: `outputs.zabbix`
Telegraf v1.30.0+

This plugin writes metrics to [Zabbix](https://www.zabbix.com/) via [traps](https://www.zabbix.com/documentation/current/en/manual/appendix/items/trapper). It has been tested with versions v3.0, v4.0 and v6.0 but should work with newer versions of Zabbix as long as the protocol doesn’t change.

[View](/telegraf/v1/output-plugins/zabbix/)

---

## Telegraf metrics

Telegraf metrics are the internal representation used to model data during processing. These metrics are closely based on InfluxDB’s data model and contain four main components:

- **Measurement name**: Description and namespace for the metric.
- **Tags**: Key/Value string pairs and usually used to identify the metric.
- **Fields**: Key/Value pairs that are typed and usually contain the metric data.
- **Timestamp**: Date and time associated with the fields.

Telegraf metrics exist only in memory and must be converted to a concrete representation to be transmitted or viewed. Telegraf provides [output data formats](/telegraf/v1/data_formats/output/) (also known as *serializers*) for these conversions. Telegraf’s default serializer converts to [InfluxDB line protocol](/telegraf/v1/data_formats/output/influx/), which provides a high performance and one-to-one direct mapping from Telegraf metrics.

---

## Use the InfluxDB documentation MCP server

The **InfluxDB documentation MCP server** lets AI tools and agents search InfluxDB documentation directly from your development environment. Use it to find answers, code examples, and configuration details without leaving your IDE.

## Why use the documentation MCP server?

When you connect the documentation MCP server to your AI coding assistant, the assistant can search InfluxDB documentation to answer your questions with accurate, up-to-date information. Instead of switching to a browser or guessing at syntax, you can ask questions in your IDE and get responses grounded in official documentation.

**Common use cases:**

- Get help writing queries, client library code, or CLI commands
- Look up configuration options and environment variables
- Find code examples for specific tasks
- Troubleshoot errors with documentation-backed answers

## Install the documentation MCP server

The documentation MCP server is a hosted service—you don’t need to install or run anything locally. Add the server URL to your AI assistant’s MCP configuration.

On first use, you’ll be prompted to sign in with Google. This authentication is used only for rate limiting—no personal data is collected.

**MCP server URL:**

```text
https://influxdb-docs.mcp.kapa.ai
```

The server uses SSE (Server-Sent Events) transport.

### Configure your AI assistant to use the documentation MCP server

The following instructions show how to configure popular AI assistants to use the InfluxDB documentation MCP server.

<!-- Tabbed content: Select one of the following options -->

**Claude Desktop:**

In **Claude Desktop**, go to **Settings** > **Developer** and edit your configuration. Add the following JSON configuration:

```json
{
  "mcpServers": {
    "influxdb-docs": {
      "url": "https://influxdb-docs.mcp.kapa.ai"
    }
  }
}
```

Save the file and restart Claude Desktop for the changes to take effect.

**ChatGPT Desktop:**

In **ChatGPT Desktop**, go to **Settings** > **Integrations** > **Enable MCP** and add a new server. Add the following JSON configuration:

```json
{
  "mcpServers": {
    "influxdb-docs": {
      "url": "https://influxdb-docs.mcp.kapa.ai",
      "transport": "sse"
    }
  }
}
```

Save the configuration and restart ChatGPT Desktop.

**GitHub Copilot (VS Code):**

In **VS Code**, configure GitHub Copilot to use the MCP server:

1. Create or edit `.vscode/mcp.json` in your workspace or project directory
2. Add the following configuration:

```json
{
  "servers": {
    "influxdb-docs": {
      "type": "http",
      "url": "https://influxdb-docs.mcp.kapa.ai"
    }
  }
}
```

3. Restart or reload VS Code
4. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`)
5. Run **MCP: List Servers** to verify the server is registered

The InfluxDB documentation MCP server will now be available through GitHub Copilot Chat.

**Cursor:**

In **Cursor**, add the MCP server configuration to your MCP settings file.

1. Open **Settings** and navigate to **MCP Servers**
2. Click **Add MCP Server** or edit the configuration file directly
3. Add the following configuration to `.cursor/mcp.json` (project-level) or `~/.cursor/mcp.json` (global):

```json
{
  "mcpServers": {
    "influxdb-docs": {
      "url": "https://influxdb-docs.mcp.kapa.ai",
      "transport": "streamableHttp"
    }
  }
}
```

Save the file and restart Cursor.

**OpenCode:**

In **OpenCode**, configure the MCP server in your configuration file:

1. Create or edit `opencode.json` (or `opencode.jsonc`) in your workspace
2. Add the following configuration:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "influxdb-docs": {
      "type": "remote",
      "url": "https://influxdb-docs.mcp.kapa.ai",
      "enabled": true
    }
  }
}
```

3. Start OpenCode and use the `/init` command to verify the MCP server is accessible

The InfluxDB documentation search tools will be available in your OpenCode sessions.

<!-- End tabbed content -->

## Authentication and rate limits

When you connect to the documentation MCP server for the first time, a Google sign-in window opens to complete an OAuth/OpenID Connect login.

The hosted MCP server:

- Requests only the `openid` scope from Google
- Receives an ID token (JWT) containing a stable, opaque user ID
- Does not request `email` or `profile` scopes—your name, email address, and other personal data are not collected

The anonymous Google ID enforces per-user rate limits to prevent abuse:

- **40 requests** per user per hour
- **200 requests** per user per day

On Google’s consent screen, this appears as “Associate you with your personal info on Google.” This is Google’s generic wording for the `openid` scope—it means the app can recognize that the same Google account is signing in again. It does not grant access to your email, name, contacts, or other data.

## Search documentation with the MCP tool

The documentation MCP server exposes a semantic search tool:

```text
search_influxdb_knowledge_sources
```

This tool lets AI agents perform semantic retrieval over InfluxDB documentation and related knowledge sources.

**What the tool does:**

- Searches all InfluxDB documentation for a given query
- Returns the most relevant chunks in descending order of relevance
- Each chunk is a self-contained snippet from a single documentation page

**Response format:**

Each result includes:

- `source_url`: URL of the original documentation page
- `content`: The chunk content in Markdown

![MCP tool search results showing InfluxDB documentation](/img/influxdb3/core-mcp-influxdb3-plugin.png)

## Use the documentation MCP server

After you install the documentation MCP server, your AI assistant can search InfluxDB documentation to help you with tasks. Ask questions naturally—the assistant uses the MCP server to find relevant documentation and provide accurate answers.

### Example prompts

> “How do I write data to InfluxDB using Python?”
>
> “What’s the syntax for a SQL query with a WHERE clause in InfluxDB?”
>
> “Show me how to configure Telegraf to collect CPU metrics.”
>
> “What environment variables does the InfluxDB CLI use?”
>
> “How do I create a database token with read-only permissions?”

---

## Install Telegraf

Use this guide to install, start, and configure Telegraf on your system:

- [Review requirements](#requirements)
- [Download and install Telegraf](#download-and-install-telegraf)
- [Deploy in Kubernetes with Helm](#deploy-telegraf-in-kubernetes-with-helm)
- [Generate a configuration file](#generate-a-configuration-file)
- [Custom compile Telegraf](#custom-compile-telegraf)

## Requirements

Installation of the Telegraf package may require `root` or administrator privileges to complete successfully.

### Networking

Telegraf offers multiple service [input plugins](/telegraf/v1/plugins/inputs/) that may require custom ports. Modify port mappings through the configuration file (`telegraf.conf`).

For Linux distributions, this file is located at `/etc/telegraf` for default installations.

For Windows distributions, the configuration file is located in the directory where you unzipped the Telegraf ZIP archive. The default location is `C:\InfluxData\telegraf`.

### NTP

Telegraf uses a host’s local time in UTC to assign timestamps to data. Use the Network Time Protocol (NTP) to synchronize time between hosts. If hosts’ clocks aren’t synchronized with NTP, the timestamps on the data might be inaccurate.

## Download and install Telegraf

Recommended:: Before you open and install packages and downloaded files, use SHA checksum verification and GPG signature verification to ensure the files are intact and authentic.

SHA checksum and GPG signature verification are complementary checks.

*For some Linux platforms, the [installation instructions](#download-and-install-instructions) include steps to verify downloaded packages and binaries.*

For more information, see the following:

[](#verify-download-integrity-using-sha-256)

Verify download integrity using SHA-256

For each released binary, InfluxData publishes the SHA checksum that you can use to verify that the downloaded file is intact and hasn’t been corrupted.

To use the SHA checksum to verify the downloaded file, do the following:

1. In the [downloads page](https://www.influxdata.com/downloads), select the **Version** and **Platform** for your download, and then copy the SHA256 checksum for the file.

2. Compute the SHA checksum of the downloaded file and compare it to the checksum you copied in the preceding step–for example, enter the following command in your terminal.

### Syntax

```bash
# Use 2 spaces to separate the checksum from the filename
echo "<SHA256_CHECKSUM>  telegraf-1.37.3_linux_amd64.tar.gz" \
| sha256sum -c -
```

Replace the following:

- `<SHA256_CHECKSUM>`: the **SHA256:** checksum value that you copied from the downloads page

### Example

The following sample code uses `curl` to download Telegraf, and then uses `sha256` to compare it to the checksum:

```bash
curl -s --location -O \
"https://dl.influxdata.com/telegraf/releases/telegraf-1.37.3_linux_amd64.tar.gz"
echo "21e781cc2352713e4eabf0931e3eeea640a2014850a33ea04f86b4dc288d6add  telegraf-1.37.3_linux_amd64.tar.gz" \
| sha256sum -c -
```

Replace the following:

- `21e781cc2352713e4eabf0931e3eeea640a2014850a33ea04f86b4dc288d6add`: the **SHA256:** checksum value that you copied from the downloads page

If the checksums match, the output is the following; otherwise, an error message.

```text
telegraf-1.37.3_linux_amd64.tar.gz: OK
```

[](#verify-file-integrity-and-authenticity-using-gpg)

Verify file integrity and authenticity using GPG

InfluxData uses [GPG (GnuPG)](https://www.gnupg.org/software/) to sign released software and provides public key and encrypted private key (`.key` file) pairs that you can use to verify the integrity of packages and binaries from the InfluxData repository.

Before running the [install](#download-and-install-instructions) sample code, substitute the key-pair compatible with your OS version:

For newer OS releases (for example, Ubuntu 20.04 LTS and newer, Debian Buster and newer) that support subkey verification:

- GPG key file: [`influxdata-archive.key`](https://repos.influxdata.com/influxdata-archive.key)
- Primary key fingerprint: `24C975CBA61A024EE1B631787C3D57159FC2F927`

For older versions (for example, CentOS/RHEL 7, Ubuntu 18.04 LTS, or Debian Stretch) that don’t support subkeys for verification:

- GPG key file: [`influxdata-archive_compat.key`](https://repos.influxdata.com/influxdata-archive_compat.key)
- Signing key fingerprint: `9D539D90D3328DC7D6C8D3B9D8FF8E1F7DF8B07E`

*For security, InfluxData periodically rotates keys and publishes the new key pairs.*

<!-- Tabbed content: Select one of the following options -->

**Ubuntu & Debian:**

Debian and Ubuntu users can install the latest stable version of Telegraf using the `apt-get` package manager.

- [Install from the InfluxData repository](#install-from-the-influxdata-repository)
- [Install from a `.deb` file](#install-from-a-deb-file)

### Install from the InfluxData repository

Run the following commands using `apt-get` to install Telegraf from the InfluxData repository:

<!-- Tabbed content: Select one of the following options -->

**Ubuntu 20.04 LTS and newer:**

```bash
curl --silent --location -O https://repos.influxdata.com/influxdata-archive.key
gpg --show-keys --with-fingerprint --with-colons ./influxdata-archive.key 2>&1 \
| grep -q '^fpr:\+24C975CBA61A024EE1B631787C3D57159FC2F927:$' \
&& cat influxdata-archive.key \
| gpg --dearmor \
| sudo tee /etc/apt/keyrings/influxdata-archive.gpg > /dev/null \
&& echo 'deb [signed-by=/etc/apt/keyrings/influxdata-archive.gpg] https://repos.influxdata.com/debian stable main' \
| sudo tee /etc/apt/sources.list.d/influxdata.list
sudo apt-get update && sudo apt-get install telegraf
```

**Older than Ubuntu 20.04:**

```bash
# influxdata-archive_compat.key GPG Fingerprint: 9D539D90D3328DC7D6C8D3B9D8FF8E1F7DF8B07E
curl --silent --location -O https://repos.influxdata.com/influxdata-archive_compat.key
gpg --show-keys --with-fingerprint --with-colons ./influxdata-archive_compat.key 2>&1 \
| grep -q '^fpr:\+9D539D90D3328DC7D6C8D3B9D8FF8E1F7DF8B07E:$' \
&& cat influxdata-archive_compat.key \
| gpg --dearmor \
| sudo tee /etc/apt/keyrings/influxdata-archive_compat.gpg > /dev/null
echo 'deb [signed-by=/etc/apt/keyrings/influxdata-archive_compat.gpg] https://repos.influxdata.com/debian stable main' \
| sudo tee /etc/apt/sources.list.d/influxdata.list
sudo apt-get update && sudo apt-get install telegraf
```

<!-- End tabbed content -->

### Install from a `.deb` file

To manually install the Debian package from a `.deb` file:

1. Download the latest Telegraf `.deb` release from the [downloads page](https://influxdata.com/downloads/#telegraf).

2. Run the following command (making sure to supply the correct version number for the downloaded file):

    ```bash
    sudo dpkg -i telegraf_1.37.3-1_amd64.deb
    ```

**RedHat & CentOS:**

To learn how to manually install the RPM package from a file, see the [downloads page](https://www.influxdata.com/downloads/).

To use the `yum` package manager to install the latest stable version of Telegraf, follow these steps:

1. In your terminal, enter the following command to add the InfluxData repository to the `yum` configuration:

    ```bash
    cat <<EOF | sudo tee /etc/yum.repos.d/influxdata.repo
    [influxdata]
    name = InfluxData Repository - Stable
    baseurl = https://repos.influxdata.com/stable/\$basearch/main
    enabled = 1
    gpgcheck = 1
    gpgkey = file:///etc/pki/rpm-gpg/RPM-GPG-KEY-influxdata
    EOF
    ```

2. Enter the following command to install `telegraf` from the repository.

    ```bash
    sudo yum install telegraf
    ```

The `telegraf` configuration file is installed at `/etc/telegraf/telegraf.conf`.

**SLES & openSUSE:**

The openSUSE Build Service provides RPM packages for SUSE Linux.

To use the `zypper` package manager to install the latest stable version of Telegraf, follow these steps:

1. In your terminal, enter the following command to add the Go repository to the `zypper` configuration:

    ```bash
    # add go repository
    zypper ar -f obs://devel:languages:go/ go
    ```

2. Enter the following command to install `telegraf`.

    ```bash
    # install latest telegraf
    zypper in telegraf
    ```

**FreeBSD/PC-BSD:**

Telegraf is part of the FreeBSD package system.

To use the `pkg` package manager to install the latest stable version of Telegraf, enter the following command:

```bash
sudo pkg install telegraf
```

The `telegraf` configuration file is installed at `/usr/local/etc/telegraf.conf`. Examples are installed at `/usr/local/etc/telegraf.conf.sample`.

**Linux binaries (AMD):**

Choose from the following options to install Telegraf binary files for Linux AMD:

- To install on Linux AMD32, see the [downloads page](https://www.influxdata.com/downloads/#telegraf).
- [Download and install on Linux AMD64](#download-and-install-on-linux-amd64)

### Download and install on Linux AMD64

```bash
curl -s --location -O \
https://dl.influxdata.com/telegraf/releases/telegraf-1.37.3_linux_amd64.tar.gz \
&& echo "21e781cc2352713e4eabf0931e3eeea640a2014850a33ea04f86b4dc288d6add  telegraf-1.37.3_linux_amd64.tar.gz" \
| sha256sum -c -
```

Replace the following:

- `21e781cc2352713e4eabf0931e3eeea640a2014850a33ea04f86b4dc288d6add`: the SHA checksum from the [downloads page](https://www.influxdata.com/downloads/#telegraf)

**Linux binaries (ARM):**

Choose from the following options to install Telegraf binary files for Linux ARM:

- To install on Linux ARMv7(32-bit), see the [downloads page](https://www.influxdata.com/downloads/#telegraf).
- [Download and install on Linux ARMv8 (64-bit)](#download-and-install-on-linux-armv8)

### Download and install on Linux ARMv8

```bash
curl -s --location -O \
https://dl.influxdata.com/telegraf/releases/telegraf-1.37.3_linux_arm64.tar.gz \
&& echo "7782bbcf50e67e73229fd0703c532d733e4fa259aa4b246debd012421f65c969  telegraf-1.37.3_linux_arm64.tar.gz" \
| sha256sum -c -
```

Replace the following:

- `7782bbcf50e67e73229fd0703c532d733e4fa259aa4b246debd012421f65c969`: the SHA checksum from the [downloads page](https://www.influxdata.com/downloads/#telegraf)

**macOS:**

Choose from the following options to install Telegraf for macOS:

- To manually install Telegraf from a file, see the [downloads page](https://www.influxdata.com/downloads/).
- [Install using Homebrew](#install-using-homebrew)

### Install using Homebrew

Users of macOS 10.8 and higher can install Telegraf using the [Homebrew](http://brew.sh/) package manager.

The `telegraf` binary installed by Homebrew differs from the macOS `.dmg` builds available from the [downloads page](https://www.influxdata.com/downloads/).

- `telegraf` (Homebrew) isn’t a static binary.
- `telegraf` (Homebrew) works with the Telegraf CPU plugin (due to Homebrew support for [Cgo](https://pkg.go.dev/cmd/cgo)). The `.dmg` builds available on the [downloads page](https://www.influxdata.com/downloads/) don’t support the CPU plugin.

To install using Homebrew, do the following:

1. If you haven’t already, follow the instructions to install the [Homebrew](http://brew.sh/) package manager.

2. Enter the following commands to update brew and install Telegraf:

    ```zsh
    brew update && brew install telegraf
    ```

    The path where `brew` installs the `telegraf.conf` configuration file depends on your system architecture:

    - ARM-based (Apple Silicon) systems: `/opt/homebrew/etc/telegraf.conf`
    - Intel-based (x86\_64) systems: `/usr/local/etc/telegraf.conf`
3. Choose one of the following methods to start Telegraf and begin collecting and processing metrics:

    - [Run Telegraf in your terminal](#run-telegraf-in-your-terminal)
    - [Run Telegraf as a service](#run-telegraf-as-a-background-service)

### Run Telegraf in your terminal

To run `telegraf` in your terminal (in the foreground and not as a service), enter the following command:

<!-- Tabbed content: Select one of the following options -->

**ARM (Apple Silicon):**

```zsh
telegraf -config /opt/homebrew/etc/telegraf.conf
```

**x86_64 (Intel):**

```zsh
telegraf -config /usr/local/etc/telegraf.conf
```

<!-- End tabbed content -->

### Run Telegraf as a background service

In your terminal, enter the following command to add `telegraf` to your system’s `LaunchAgents`:

<!-- Tabbed content: Select one of the following options -->

**ARM (Apple Silicon):**

```zsh
ln -sfv /opt/homebrew/opt/telegraf/*.plist ~/Library/LaunchAgents
```

**x86_64 (Intel):**

```zsh
ln -sfv /usr/local/opt/telegraf/*.plist ~/Library/LaunchAgents
```

<!-- End tabbed content -->

The next time you login, launchd starts the `telegraf` service.

To immediately start the `telegraf` service, enter the following command:

```zsh
launchctl load ~/Library/LaunchAgents/homebrew.mxcl.telegraf.plist
```

**Windows:**

#### Download and run Telegraf as a Windows service

Installing a Windows service requires administrative permissions. To run PowerShell as an administrator, see [Launch PowerShell as administrator](https://docs.microsoft.com/en-us/powershell/scripting/windows-powershell/starting-windows-powershell?view=powershell-7#with-administrative-privileges-run-as-administrator).

In PowerShell *as an administrator*, do the following:

1. Use the following commands to download the Telegraf Windows binary and extract its contents to `C:\Program Files\InfluxData\telegraf\`:

    ```powershell
    wget `
    https://dl.influxdata.com/telegraf/releases/telegraf-1.37.3_windows_amd64.zip `
    -UseBasicParsing `
    -OutFile telegraf-1.37.3_windows_amd64.zip
    Expand-Archive .\telegraf-1.37.3_windows_amd64.zip `
    -DestinationPath 'C:\Program Files\InfluxData\telegraf\'
    ```

2. Choose *one* of the following steps to place your `telegraf.exe` and `telegraf.conf` files in `C:\Program Files\InfluxData\telegraf`:

    - Move the `telegraf.exe` and `telegraf.conf` files from `C:\Program Files\InfluxData\telegraf\telegraf-1.37.3` to the parent directory `C:\Program Files\InfluxData\telegraf`–for example:

        ```powershell
        cd "C:\Program Files\InfluxData\telegraf";
        mv .\telegraf-1.37.3\telegraf.* .
        ```

    - **Or**, create a [Windows symbolic link (Symlink)](https://blogs.windows.com/windowsdeveloper/2016/12/02/symlinks-windows-10/) for `C:\Program Files\InfluxData\telegraf` that points to the extracted directory.

The remaining instructions assume that `telegraf.exe` and `telegraf.conf` files are stored in `C:\Program Files\InfluxData\telegraf` or that you created a Symlink to point to this directory.

3. Optional: Enable a plugin to collect Windows-specific metrics–for example, uncomment the [`inputs.win_services` plugin](/telegraf/v1/plugins/#input-win_services) configuration line:

    ```toml
    ...
    # # Input plugin to report Windows services info.
    # # This plugin ONLY supports Windows
    [[inputs.win_services]]
    ...
    ```

4. Run the following command to install Telegraf and the configuration as a Windows service. For the `--config` option, pass the absolute path of the `telegraf.conf` configuration file.

    ```powershell
    .\telegraf.exe --service install `
    --config "C:\Program Files\InfluxData\telegraf\telegraf.conf"
    ```

5. To test that the installation works, enter the following command:

    ```powershell
    .\telegraf.exe `
    --config C:\"Program Files"\InfluxData\telegraf\telegraf.conf --test
    ```

    When run in test mode (using the `--test` flag), Telegraf runs once, collects metrics, outputs them to the console, and then exits. It doesn’t run processors, aggregators, or output plugins.

6. To start collecting data, run:

    ```powershell
    .\telegraf.exe --service start
    ```

### Logging and troubleshooting

When Telegraf runs as a Windows service, Telegraf logs messages to Windows event logs. If the Telegraf service fails to start, view error logs by selecting **Event Viewer**→**Windows Logs**→**Application**.

### Windows service commands

The following commands are available:

| Command | Effect |
| --- | --- |
| telegraf.exe --service install | Install telegraf as a service |
| telegraf.exe --service uninstall | Remove the telegraf service |
| telegraf.exe --service start | Start the telegraf service |
| telegraf.exe --service stop | Stop the telegraf service |

<!-- End tabbed content -->

## Deploy Telegraf in Kubernetes with Helm

For Kubernetes deployments, InfluxData provides several Helm charts:

- [telegraf](https://github.com/influxdata/helm-charts/tree/master/charts/telegraf): Deploy Telegraf as a single instance
- [telegraf-ds](https://github.com/influxdata/helm-charts/tree/master/charts/telegraf-ds): Deploy Telegraf as a DaemonSet to run on every node
- [telegraf-operator](https://github.com/influxdata/helm-charts/tree/master/charts/telegraf-operator): Deploy the Telegraf Operator for managing Telegraf instances declaratively

## Generate a configuration file

The `telegraf config` command lets you generate a configuration file from Telegraf’s [plugin list](/telegraf/v1/commands/plugins/).

- [Create a configuration file with default input and output plugins](#create-a-configuration-file-with-default-input-and-output-plugins)
- [Create a configuration with specific input and output plugins](#create-a-configuration-file-with-specific-input-and-output-plugins)

### Create a configuration file with default input and output plugins

To generate a configuration file with default input and output plugins enabled, enter the following command in your terminal:

<!-- Tabbed content: Select one of the following options -->

**Linux and macOS:**

```bash
telegraf config > telegraf.conf
```

**Windows:**

```powershell
.\telegraf.exe config > telegraf.conf
```

<!-- End tabbed content -->

### Create a configuration file with specific input and output plugins

To generate a configuration file that contains settings for only specific plugins, use the `--input-filter` and `--output-filter` options to specify [input plugins](/telegraf/v1/configure_plugins/input_plugins/) and [output plugins](/telegraf/v1/configure_plugins/output_plugins/)–for example:

<!-- Tabbed content: Select one of the following options -->

**Linux and macOS:**

```bash
telegraf \
--input-filter cpu:http \
--output-filter influxdb_v2:file \
config > telegraf.conf
```

**Windows:**

```powershell
.\telegraf.exe `
--input-filter cpu:http `
--output-filter influxdb_v2:file `
config > telegraf.conf
```

<!-- End tabbed content -->

For more advanced configuration details, see the [configuration documentation](/telegraf/v1/administration/configuration/).

## Custom-compile Telegraf

Use the Telegraf custom builder tool to compile Telegraf with only the plugins you need and reduce the Telegraf binary size.

1. [Prerequisites](#prerequisites)
2. [Build the custom builder tool](#build-the-custom-builder-tool)
3. [Run the custom builder to create a `telegraf` binary](#run-the-custom-builder-to-create-a-telegraf-binary)

### Prerequisites

- Follow the instructions to install [Go](https://go.dev/) for your system.
- [Create your Telegraf configuration file](#generate-a-configuration-file) with the plugins you want to use.

### Build the custom builder tool

1. Clone the Telegraf repository and then change into the repository directory–for example, enter the following command in your terminal:

    ```bash
    git clone https://github.com/influxdata/telegraf.git && cd ./telegraf
    ```

2. To build the Telegraf custom builder tool, enter the following command:

    ```bash
    make build_tools
    ```

### Run the custom builder to create a `telegraf` binary

The custom builder builds a `telegraf` binary with only the plugins included in the specified configuration files or directories.

Run the `custom_builder` tool with at least one `--config` or `--config-directory` flag to specify Telegraf configuration files to build from.

- `--config`: accepts local file paths and URLs.
- `--config-dir`: accepts local directory paths.

You can include multiple `--config` and `--config-dir` flags.

#### Examples

##### Single Telegraf configuration

```bash
./tools/custom_builder/custom_builder --config /etc/telegraf.conf
```

##### Single Telegraf configuration and Telegraf configuration directory

```bash
./tools/custom_builder/custom_builder \
--config /etc/telegraf.conf \
--config-dir /etc/telegraf/telegraf.d
```

##### Remote Telegraf configuration

```bash
./tools/custom_builder/custom_builder \
--config http://url-to-remote-telegraf/telegraf.conf
```

After a successful build, you can view your customized `telegraf` binary within the top level of your Telegraf repository.

### Update your custom binary

To add or remove plugins from your customized Telegraf build, edit your configuration file, and then [run the custom builder](#run-the-custom-builder-to-create-a-telegraf-binary) to regenerate the Telegraf binary.

---

## Telegraf Input Plugins

Telegraf input plugins collect metrics from the system, services, and third-party APIs.

### ActiveMQ

Plugin ID: `inputs.activemq`
Telegraf v1.8.0+

This plugin gathers queue, topics and subscribers metrics using the Console API [ActiveMQ](https://activemq.apache.org/) message broker daemon.

[View](/telegraf/v1/input-plugins/activemq/)

### Aerospike

Plugin ID: `inputs.aerospike`
Telegraf v0.2.0 - v1.30.0 Deprecated

This plugin queries [Aerospike](https://www.aerospike.com) server(s) for node statistics and statistics on all configured namespaces.

As of version 1.30 the Aerospike plugin has been deprecated in favor of the prometheus plugin and the officially supported [Aerospike Prometheus Exporter](https://aerospike.com/docs/monitorstack/configure/configure-exporter)

For details on the measurements mean, please consult the [Aerospike Metrics Reference Docs](https://www.aerospike.com/docs/reference/metrics).

Metric names will have dashes (`-`) replaced as underscores (`_`) to make querying more consistently and easy.

All metrics are attempted to be cast to integers, then booleans, then strings in order.

[View](/telegraf/v1/input-plugins/aerospike/)

### Alibaba Cloud Monitor Service (Aliyun)

Plugin ID: `inputs.aliyuncms`
Telegraf v1.19.0+

This plugin gathers statistics from the [Alibaba / Aliyun cloud monitoring service](https://www.alibabacloud.com). In the following we will use `Aliyun` instead of `Alibaba` as it’s the default naming across the web console and docs.

[View](/telegraf/v1/input-plugins/aliyuncms/)

### AMD ROCm System Management Interface (SMI)

Plugin ID: `inputs.amd_rocm_smi`
Telegraf v1.20.0+

This plugin gathers statistics including memory and GPU usage, temperatures etc from [AMD ROCm platform](https://rocm.docs.amd.com/) GPUs.

The [`rocm-smi` binary](https://github.com/RadeonOpenCompute/rocm_smi_lib/tree/master/python_smi_tools) is required and needs to be installed on the system.

[View](/telegraf/v1/input-plugins/amd_rocm_smi/)

### AMQP Consumer

Plugin ID: `inputs.amqp_consumer`
Telegraf v1.3.0+

This plugin consumes messages from an Advanced Message Queuing Protocol v0.9.1 broker. A prominent implementation of this protocol is [RabbitMQ](https://www.rabbitmq.com).

Metrics are read from a topic exchange using the configured queue and binding key. The message payloads must be formatted in one of the supported [data formats](/telegraf/v1/data_formats/input).

For an introduction check the [AMQP concepts page](https://www.rabbitmq.com/tutorials/amqp-concepts.html) and the [RabbitMQ getting started guide](https://www.rabbitmq.com/getstarted.html).

[View](/telegraf/v1/input-plugins/amqp_consumer/)

### Apache

Plugin ID: `inputs.apache`
Telegraf v1.8.0+

This plugin collects performance information from [Apache HTTP Servers](https://httpd.apache.org) using the [`mod_status` module](https://httpd.apache.org/docs/current/mod/mod_status.html). Typically, this module is configured to expose a page at the `/server-status?auto` endpoint the server.

The [ExtendedStatus option](https://httpd.apache.org/docs/current/mod/core.html#extendedstatus) must be enabled in order to collect all available fields. For information about configuration of your server check the [module documentation](https://httpd.apache.org/docs/current/mod/mod_status.html).

[View](/telegraf/v1/input-plugins/apache/)

### APC UPSD

Plugin ID: `inputs.apcupsd`
Telegraf v1.12.0+

This plugin gathers data from one or more [apcupsd daemon](https://sourceforge.net/projects/apcupsd/) over the NIS network protocol. To query a server, the daemon must be running and be accessible.

[View](/telegraf/v1/input-plugins/apcupsd/)

### Apache Aurora

Plugin ID: `inputs.aurora`
Telegraf v1.7.0+

This plugin gathers metrics from [Apache Aurora](https://aurora.apache.org) schedulers. For monitoring recommendations check the [Monitoring your Aurora cluster](https://aurora.apache.org/documentation/latest/operations/monitoring) article.

[View](/telegraf/v1/input-plugins/aurora/)

### Azure Monitor

Plugin ID: `inputs.azure_monitor`
Telegraf v1.25.0+

This plugin gathers metrics of Azure resources using the [Azure Monitor](https://docs.microsoft.com/en-us/azure/azure-monitor) API. The plugin requires a `client_id`, `client_secret` and `tenant_id` for authentication via access token. The `subscription_id` is required for accessing Azure resources.

Check the [supported metrics page](https://docs.microsoft.com/en-us/azure/azure-monitor/essentials/metrics-supported) for available resource types and their metrics.

The Azure API has a read limit of 12,000 requests per hour. Please make sure you don’t exceed this limit with the total number of metrics you are in the configured interval.

[View](/telegraf/v1/input-plugins/azure_monitor/)

### Azure Queue Storage

Plugin ID: `inputs.azure_storage_queue`
Telegraf v1.13.0+

This plugin gathers queue sizes from the [Azure Queue Storage](https://learn.microsoft.com/en-us/azure/storage/queues) service, storing a large numbers of messages.

[View](/telegraf/v1/input-plugins/azure_storage_queue/)

### Bcache

Plugin ID: `inputs.bcache`
Telegraf v0.2.0+

This plugin gathers statistics for the [block layer cache](https://docs.kernel.org/admin-guide/bcache.html) from the `stats_total` directory and `dirty_data` file.

[View](/telegraf/v1/input-plugins/bcache/)

### Beanstalkd

Plugin ID: `inputs.beanstalkd`
Telegraf v1.8.0+

This plugin collects server statistics as well as tube statistics from a [Beanstalkd work queue](https://beanstalkd.github.io/) as reported by the `stats` and `stats-tube` server commands.

[View](/telegraf/v1/input-plugins/beanstalkd/)

### Beat

Plugin ID: `inputs.beat`
Telegraf v1.18.0+

This plugin will collect metrics from a [Beats](https://www.elastic.co/beats) instances. It is known to work with Filebeat and Kafkabeat.

[View](/telegraf/v1/input-plugins/beat/)

### BIND 9 Nameserver

Plugin ID: `inputs.bind`
Telegraf v1.11.0+

This plugin collects metrics from [BIND 9 nameservers](https://www.isc.org/bind) using the XML or JSON endpoint.

For *XML*, version 2 statistics (BIND 9.6 to 9.9) and version 3 statistics (BIND 9.9+) are supported. Version 3 statistics are the default and only XML format in BIND 9.10+.

For BIND 9.9 to support version 3 statistics, it must be built with the `--enable-newstats` compile flag, and the statistics must be specifically requested via the correct URL.

For *JSON*, version 1 statistics (BIND 9.10+) are supported. As of writing, some distros still do not enable support for JSON statistics in their BIND packages.

[View](/telegraf/v1/input-plugins/bind/)

### Bond

Plugin ID: `inputs.bond`
Telegraf v1.5.0+

This plugin collects metrics for both the network bond interface as well as its slave interfaces using `/proc/net/bonding/*` files.

[View](/telegraf/v1/input-plugins/bond/)

### Burrow

Plugin ID: `inputs.burrow`
Telegraf v1.7.0+

This plugin collect Kafka topic, consumer and partition status from the [Burrow - Kafka Consumer Lag Checking](https://github.com/linkedin/Burrow) companion via [HTTP API](https://github.com/linkedin/Burrow/wiki/HTTP-Endpoint). Burrow v1.x versions are supported.

[View](/telegraf/v1/input-plugins/burrow/)

### Ceph Storage

Plugin ID: `inputs.ceph`
Telegraf v0.13.1+

This plugin collects performance metrics from MON and OSD nodes in a [Ceph storage cluster](https://ceph.com). Support for Telegraf has been introduced in the v13.x Mimic release where data is sent to a socket (see [their documnetation](https://docs.ceph.com/en/latest/mgr/telegraf)).

[View](/telegraf/v1/input-plugins/ceph/)

### Control Group

Plugin ID: `inputs.cgroup`
Telegraf v1.0.0+

This plugin gathers statistics per [control group (cgroup)](https://docs.kernel.org/admin-guide/cgroup-v2.html).

Consider restricting paths to the set of cgroups you are interested in if you have a large number of cgroups, to avoid cardinality issues.

The plugin supports the *single value format* in the form

the *new line separated values format* in the form

the *space separated values format* in the form

and the *space separated keys and value, separated by new line format* in the form

[View](/telegraf/v1/input-plugins/cgroup/)

### chrony

Plugin ID: `inputs.chrony`
Telegraf v0.13.1+

This plugin queries metrics from a [chrony NTP server](https://chrony-project.org). For details on the meaning of the gathered fields please check the [chronyc manual](https://chrony-project.org/doc/4.4/chronyc.html).

[View](/telegraf/v1/input-plugins/chrony/)

### Cisco Model-Driven Telemetry (MDT)

Plugin ID: `inputs.cisco_telemetry_mdt`
Telegraf v1.11.0+

This plugin consumes [Cisco model-driven telemetry (MDT)](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9300-series-switches/model-driven-telemetry-wp.html) data from Cisco IOS XR, IOS XE and NX-OS platforms via TCP or GRPC. GRPC-based transport can utilize TLS for authentication and encryption. Telemetry data is expected to be GPB-KV (self-describing-gpb) encoded.

The GRPC dialout transport is supported on various IOS XR (64-bit) 6.1.x and later, IOS XE 16.10 and later, as well as NX-OS 7.x and later platforms. The TCP dialout transport is supported on IOS XR (32-bit and 64-bit) 6.1.x and later.

[View](/telegraf/v1/input-plugins/cisco_telemetry_mdt/)

### ClickHouse

Plugin ID: `inputs.clickhouse`
Telegraf v1.14.0+

This plugin gathers statistics data from a [ClickHouse server](https://github.com/ClickHouse/ClickHouse). Users on Clickhouse Cloud will not see the Zookeeper metrics as they may not have permissions to query those tables.

[View](/telegraf/v1/input-plugins/clickhouse/)

### Google Cloud PubSub

Plugin ID: `inputs.cloud_pubsub`
Telegraf v1.10.0+

This plugin consumes messages from the [Google Cloud PubSub](https://cloud.google.com/pubsub) service and creates metrics using one of the supported [data formats](/telegraf/v1/data_formats/input).

[View](/telegraf/v1/input-plugins/cloud_pubsub/)

### Google Cloud PubSub Push

Plugin ID: `inputs.cloud_pubsub_push`
Telegraf v1.10.0+

This plugin listens for messages sent via an HTTP POST from [Google Cloud PubSub](https://cloud.google.com/pubsub) and expects messages in Google’s Pub/Sub *JSON format*. The plugin allows Telegraf to serve as an endpoint of push service.

Google’s PubSub service will **only** send over HTTPS/TLS so this plugin must be behind a valid proxy or must be configured to use TLS by setting the `tls_cert` and `tls_key` accordingly.

Enable mutually authenticated TLS and authorize client connections by signing certificate authority by including a list of allowed CA certificate file names in `tls_allowed_cacerts`.

[View](/telegraf/v1/input-plugins/cloud_pubsub_push/)

### Amazon CloudWatch Statistics

Plugin ID: `inputs.cloudwatch`
Telegraf v0.12.1+

This plugin will gather metric statistics from [Amazon CloudWatch](https://aws.amazon.com/cloudwatch).

[View](/telegraf/v1/input-plugins/cloudwatch/)

### Amazon CloudWatch Metric Streams

Plugin ID: `inputs.cloudwatch_metric_streams`
Telegraf v1.24.0+

This plugin listens for metrics sent via HTTP by [Cloudwatch metric streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Streams.html) implementing the required [response specifications](https://docs.aws.amazon.com/firehose/latest/dev/httpdeliveryrequestresponse.html).

Using this plugin can incure costs, see the *Metric Streams example* in [CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing).

[View](/telegraf/v1/input-plugins/cloudwatch_metric_streams/)

### Netfilter Conntrack

Plugin ID: `inputs.conntrack`
Telegraf v1.0.0+

This plugin collects metrics from [Netfilter’s conntrack tools](https://conntrack-tools.netfilter.org/). There are two collection mechanisms for this plugin:

1. Extracting information from `/proc/net/stat/nf_conntrack` files if the `collect` option is set accordingly for finding CPU specific values.
2. Using specific files and directories by specifying the `dirs` option. At runtime, conntrack exposes many of those connection statistics within `/proc/sys/net`. Depending on your kernel version, these files can be found in either `/proc/sys/net/ipv4/netfilter` or `/proc/sys/net/netfilter` and will be prefixed with either `ip` or `nf`.

In order to simplify configuration in a heterogeneous environment, a superset of directory and filenames can be specified. Any locations that doesn’t exist is ignored.

[View](/telegraf/v1/input-plugins/conntrack/)

### Hashicorp Consul

Plugin ID: `inputs.consul`
Telegraf v1.0.0+

This plugin will collect statistics about all health checks registered in [Consul](https://www.consul.io) using the [Consul API](https://www.consul.io/docs/agent/http/health.html#health_state). The plugin will not report any [telemetry metrics](https://www.consul.io/docs/agent/telemetry.html) but Consul can report those statistics using the StatsD protocol if needed.

[View](/telegraf/v1/input-plugins/consul/)

### Hashicorp Consul Agent

Plugin ID: `inputs.consul_agent`
Telegraf v1.22.0+

This plugin collects metrics from a [Consul agent](https://developer.hashicorp.com/consul/commands/agent). Telegraf may be present in every node and connect to the agent locally. Tested on Consul v1.10.

[View](/telegraf/v1/input-plugins/consul_agent/)

### Couchbase

Plugin ID: `inputs.couchbase`
Telegraf v0.12.0+

This plugin collects metrics from [Couchbase](https://www.couchbase.com/), a distributed NoSQL database. Metrics are collected for each node, as well as detailed metrics for each bucket, for a given couchbase server.

[View](/telegraf/v1/input-plugins/couchbase/)

### Apache CouchDB

Plugin ID: `inputs.couchdb`
Telegraf v0.10.3+

This plugin gathers metrics from [Apache CouchDB](https://couchdb.apache.org/) instances using the [stats](http://docs.couchdb.org/en/1.6.1/api/server/common.html?highlight=stats#get--_stats) endpoint.

[View](/telegraf/v1/input-plugins/couchdb/)

### CPU

Plugin ID: `inputs.cpu`
Telegraf v0.1.5+

This plugin gathers metrics about the system’s CPUs.

[View](/telegraf/v1/input-plugins/cpu/)

### Counter-Strike Global Offensive (CSGO)

Plugin ID: `inputs.csgo`
Telegraf v1.18.0+

This plugin gather metrics from [Counter-Strike: Global Offensive](https://www.counter-strike.net/) servers.

[View](/telegraf/v1/input-plugins/csgo/)

### Bosch Rexroth ctrlX Data Layer

Plugin ID: `inputs.ctrlx_datalayer`
Telegraf v1.27.0+

This plugin gathers data from the [ctrlX Data Layer](https://ctrlx-automation.com) a communication middleware running on Bosch Rexroth’s [ctrlX CORE devices](https://ctrlx-core.com). The platform is used for professional automation applications like industrial automation, building automation, robotics, IoT Gateways or as classical PLC.

[View](/telegraf/v1/input-plugins/ctrlx_datalayer/)

### Mesosphere Distributed Cloud OS

Plugin ID: `inputs.dcos`
Telegraf v1.5.0+

This input plugin gathers metrics from a [Distributed Cloud OS](https://dcos.io/) cluster’s [metrics component](https://docs.mesosphere.com/1.10/metrics/).

Depending on the workload of your DC/OS cluster, this plugin can quickly create a high number of series which, when unchecked, can cause high load on your database!

[View](/telegraf/v1/input-plugins/dcos/)

### Directory Monitor

Plugin ID: `inputs.directory_monitor`
Telegraf v1.18.0+

This plugin monitors a single directory (traversing sub-directories), and processes each file placed in the directory. The plugin will gather all files in the directory at the configured interval, and parse the ones that haven’t been picked up yet.

Files should not be used by another process or the plugin may fail. Furthermore, files should not be written *live* to the monitored directory. If you absolutely must write files directly, they must be guaranteed to finish writing before `directory_duration_threshold`.

[View](/telegraf/v1/input-plugins/directory_monitor/)

### Disk

Plugin ID: `inputs.disk`
Telegraf v0.1.1+

This plugin gathers metrics about disk usage.

The `used_percent` field is calculated by `used / (used + free)` and *not* `used / total` as the unix `df` command does it. See [wikipedia - df](https://en.wikipedia.org/wiki/Df_\(Unix\)) for more details.

[View](/telegraf/v1/input-plugins/disk/)

### DiskIO

Plugin ID: `inputs.diskio`
Telegraf v0.10.0+

This plugin gathers metrics about disk traffic and timing.

[View](/telegraf/v1/input-plugins/diskio/)

### Disque

Plugin ID: `inputs.disque`
Telegraf v0.10.0+

This plugin gathers data from a [Disque](https://github.com/antirez/disque) instance, an experimental distributed, in-memory, message broker.

[View](/telegraf/v1/input-plugins/disque/)

### Device Mapper Cache

Plugin ID: `inputs.dmcache`
Telegraf v1.3.0+

This plugin provide a native collection for dmsetup based statistics for [dm-cache](https://docs.kernel.org/admin-guide/device-mapper/cache.html).

This plugin requires super-user permissions! Please make sure, Telegraf is able to run `sudo /sbin/dmsetup status --target cache` without requiring a password.

[View](/telegraf/v1/input-plugins/dmcache/)

### DNS Query

Plugin ID: `inputs.dns_query`
Telegraf v1.4.0+

This plugin gathers information about DNS queries such as response time and result codes.

[View](/telegraf/v1/input-plugins/dns_query/)

### Docker

Plugin ID: `inputs.docker`
Telegraf v0.1.9+

This plugin uses the [Docker Engine API](https://docs.docker.com/engine/api) to gather metrics on running Docker containers.

Make sure Telegraf has sufficient permissions to access the configured endpoint.

[View](/telegraf/v1/input-plugins/docker/)

### Docker Log

Plugin ID: `inputs.docker_log`
Telegraf v1.12.0+

This plugin uses the [Docker Engine API](https://docs.docker.com/engine/api) to gather logs from running Docker containers.

This plugin works only for containers with the `local` or `json-file` or `journald` logging driver. Make sure Telegraf has sufficient permissions to access the configured endpoint.

[View](/telegraf/v1/input-plugins/docker_log/)

### Dovecot

Plugin ID: `inputs.dovecot`
Telegraf v0.10.3+

This plugin uses the Dovecot [v2.1 stats protocol](https://doc.dovecot.org/configuration_manual/stats/old_statistics/#old-statistics) to gather metrics about configured domains of [Dovecot](https://www.dovecot.org/) servers. You can use this plugin on Dovecot up to and including version v2.3.x.

Dovecot v2.4+ has the old protocol removed and this plugin will not work. Please use Dovecot’s [Openmetrics exporter](https://doc.dovecot.org/latest/core/config/statistics.html#openmetrics) in combination with the [http input plugin](/telegraf/v1/plugins/#input-http) and `openmetrics` data format for newer versions of Dovecot.

[View](/telegraf/v1/input-plugins/dovecot/)

### Data Plane Development Kit (DPDK)

Plugin ID: `inputs.dpdk`
Telegraf v1.19.0+

This plugin collects metrics exposed by applications built with the [Data Plane Development Kit](https://www.dpdk.org) which is an extensive set of open source libraries designed for accelerating packet processing workloads.

Since DPDK will most likely run with root privileges, the telemetry socket exposed by DPDK will also require root access. Please adjust permissions accordingly!

Refer to the [Telemetry User Guide](https://doc.dpdk.org/guides/howto/telemetry.html) for details and examples on how to use DPDK in your application.

This plugin uses the `v2` interface to read telemetry > data from applications and required DPDK version `v20.05` or higher. Some metrics might require later versions. The recommended version, especially in conjunction with the `in_memory` option is `DPDK 21.11.2` or higher.

[View](/telegraf/v1/input-plugins/dpdk/)

### Amazon Elastic Container Service

Plugin ID: `inputs.ecs`
Telegraf v1.11.0+

This plugin gathers statistics on running containers in a Task from the [Amazon Elastic Container Service](https://aws.amazon.com/ecs/) using the [Amazon ECS metadata](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint.html) and the [v2](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v2.html) or [v3](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v3.html) statistics API endpoints.

The telegraf container must be run in the same Task as the workload it is inspecting.

The amazon-ecs-agent (though it *is* a container running on the host) is not present in the metadata/stats endpoints.

[View](/telegraf/v1/input-plugins/ecs/)

### Elasticsearch

Plugin ID: `inputs.elasticsearch`
Telegraf v0.1.5+

This plugin queries endpoints of a [Elasticsearch](https://www.elastic.co/) instance to obtain [node statistics](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-nodes-stats.html) and optionally [cluster-health](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-health.html) metrics. Additionally, the plugin is able to query [cluster](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-stats.html), [indices and shard](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-stats.html) statistics for the master node.

Specific statistics information can change between Elasticsearch versions. In general, this plugin attempts to stay as version-generic as possible by tagging high-level categories only and creating unique field names of whatever statistics names are provided at the mid-low level.

[View](/telegraf/v1/input-plugins/elasticsearch/)

### Elasticsearch Query

Plugin ID: `inputs.elasticsearch_query`
Telegraf v1.20.0+

This plugin allows to query an [Elasticsearch](https://www.elastic.co/) instance to obtain metrics from data stored in the cluster. The plugins supports counting the number of hits for a search query, calculating statistics for numeric fields, filtered by a query, aggregated per tag and to count the number of terms for a particular field.

This plugins supports Elasticsearch 5.x and 6.x but is known to break on 7.x or higher.

[View](/telegraf/v1/input-plugins/elasticsearch_query/)

### Ethtool

Plugin ID: `inputs.ethtool`
Telegraf v1.13.0+

This plugin collects ethernet device statistics. The available information strongly depends on the network device and driver.

[View](/telegraf/v1/input-plugins/ethtool/)

### Azure Event Hub Consumer

Plugin ID: `inputs.eventhub_consumer`
Telegraf v1.14.0+

This plugin allows consuming messages from [Azure Event Hubs](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-about) and [Azure IoT Hub](https://azure.microsoft.com/en-us/products/iot-hub) instances.

[View](/telegraf/v1/input-plugins/eventhub_consumer/)

### Exec

Plugin ID: `inputs.exec`
Telegraf v0.1.5+

This plugin executes the given `commands` on every interval and parses metrics from their output in any one of the supported [data formats](/telegraf/v1/data_formats/input). This plugin can be used to poll for custom metrics from any source.

[View](/telegraf/v1/input-plugins/exec/)

### Execd

Plugin ID: `inputs.execd`
Telegraf v1.14.0+

This plugin runs the given external program as a long-running daemon and collects the metrics in one of the supported [data formats](/telegraf/v1/data_formats/input) on the process’s `stdout`. The program is expected to stay running and output data when receiving the configured `signal`.

The `stderr` output of the process will be relayed to Telegraf’s logging facilities and will be logged as *error* by default. However, you can log to other levels by prefixing your message with `E!` for error, `W!` for warning, `I!` for info, `D!` for debugging and `T!` for trace levels followed by a space and the actual message. For example outputting `I! A log message` will create a `info` log line in your Telegraf logging output.

[View](/telegraf/v1/input-plugins/execd/)

### Fail2ban

Plugin ID: `inputs.fail2ban`
Telegraf v1.4.0+

This plugin gathers the count of failed and banned IP addresses using [fail2ban](https://www.fail2ban.org) by running the `fail2ban-client` command.

The `fail2ban-client` requires root access, so please make sure to either allow Telegraf to run that command using `sudo` without a password or by running telegraf as root (not recommended).

[View](/telegraf/v1/input-plugins/fail2ban/)

### Fibaro

Plugin ID: `inputs.fibaro`
Telegraf v1.7.0+

This plugin gathers data from devices connected to a [Fibaro](https://www.fibaro.com) controller. Those values could be true (1) or false (0) for switches, percentage for dimmers, temperature, etc. Both *Home Center 2* and *Home Center 3* devices are supported.

[View](/telegraf/v1/input-plugins/fibaro/)

### File

Plugin ID: `inputs.file`
Telegraf v1.8.0+

This plugin reads the **complete** contents of the configured files in **every** interval. The file content is split line-wise and parsed according to one of the supported [data formats](/telegraf/v1/data_formats/input).

If you wish to only process newly appended lines use the [tail](/telegraf/v1/plugins/#input-tail) input plugin instead.

[View](/telegraf/v1/input-plugins/file/)

### Filecount

Plugin ID: `inputs.filecount`
Telegraf v1.8.0+

This plugin reports the number and total size of files in specified directories.

[View](/telegraf/v1/input-plugins/filecount/)

### File statistics

Plugin ID: `inputs.filestat`
Telegraf v0.13.0+

This plugin gathers metrics about file existence, size, and other file statistics.

[View](/telegraf/v1/input-plugins/filestat/)

### Fireboard

Plugin ID: `inputs.fireboard`
Telegraf v1.12.0+

This plugin gathers real-time temperature data from [fireboard](https://www.fireboard.com) thermometers.

You will need to sign up to for the [Fireboard REST API](https://docs.fireboard.io/reference/restapi.html) in order to use this plugin.

[View](/telegraf/v1/input-plugins/fireboard/)

### AWS Data Firehose

Plugin ID: `inputs.firehose`
Telegraf v1.34.0+

This plugin listens for metrics sent via HTTP from [AWS Data Firehose](https://aws.amazon.com/de/firehose/) in one of the supported [data formats](/telegraf/v1/data_formats/input). The plugin strictly follows the request-response schema as describe in the official [documentation](https://docs.aws.amazon.com/firehose/latest/dev/httpdeliveryrequestresponse.html).

[View](/telegraf/v1/input-plugins/firehose/)

### Fluentd

Plugin ID: `inputs.fluentd`
Telegraf v1.4.0+

This plugin gathers internal metrics of a [fluentd](https://www.fluentd.org/) instance provided by fluentd’s [monitor agent plugin](https://docs.fluentd.org/input/monitor_agent). Data provided by the `/api/plugin.json` resource, `/api/config.json` is not covered.

This plugin might produce high-cardinality series as the `plugin_id` value is random after each restart of fluentd. You might need to adjust your fluentd configuration, in order to reduce series cardinality in case your fluentd restarts frequently by adding the `@id` parameter to each plugin. See [fluentd’s documentation](https://docs.fluentd.org/configuration/config-file#common-plugin-parameter) for details.

[View](/telegraf/v1/input-plugins/fluentd/)

### Fritzbox

Plugin ID: `inputs.fritzbox`
Telegraf v1.35.0+

This plugin gathers status information from [AVM](https://en.avm.de/) devices (routers, repeaters, etc) using the device’s [TR-064](https://avm.de/service/schnittstellen/) interface.

[View](/telegraf/v1/input-plugins/fritzbox/)

### GitHub

Plugin ID: `inputs.github`
Telegraf v1.11.0+

This plugin gathers information from projects and repositories hosted on [GitHub](https://www.github.com).

Telegraf also contains the [webhook input plugin](/telegraf/v1/plugins/#input-webhooks) which can be used as an alternative method for collecting repository information.

[View](/telegraf/v1/input-plugins/github/)

### gNMI (gRPC Network Management Interface)

Plugin ID: `inputs.gnmi`
Telegraf v1.15.0+

This plugin consumes telemetry data based on [gNMI](https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md) subscriptions. TLS is supported for authentication and encryption. This plugin is vendor-agnostic and is supported on any platform that supports the gNMI specification.

For Cisco devices the plugin has been optimized to support gNMI telemetry as produced by Cisco IOS XR (64-bit) version 6.5.1, Cisco NX-OS 9.3 and Cisco IOS XE 16.12 and later.

[View](/telegraf/v1/input-plugins/gnmi/)

### Google Cloud Storage

Plugin ID: `inputs.google_cloud_storage`
Telegraf v1.25.0+

This plugin will collect metrics from the given [Google Cloud Storage](https://cloud.google.com/storage) buckets in any of the supported [data formats](/telegraf/v1/data_formats/input).

[View](/telegraf/v1/input-plugins/google_cloud_storage/)

### GrayLog

Plugin ID: `inputs.graylog`
Telegraf v1.0.0+

This plugin collects data from [Graylog servers](https://graylog.org/), currently supporting two type of end points `multiple` (e.g. `http://<host>:9000/api/system/metrics/multiple`) and `namespace` (e.g. `http://<host>:9000/api/system/metrics/namespace/{namespace}`).

Multiple endpoint can be queried and mixing `multiple` and serveral `namespace` end points is possible. Check `http://<host>:9000/api/api-browser` for the full list of available endpoints.

When specifying a `namespace` endpoint without an actual namespace, the metrics array will be ignored.

[View](/telegraf/v1/input-plugins/graylog/)

### HAProxy

Plugin ID: `inputs.haproxy`
Telegraf v0.1.5+

This plugin gathers statistics of [HAProxy](http://www.haproxy.org/) servers using sockets or the HTTP protocol.

[View](/telegraf/v1/input-plugins/haproxy/)

### HDDtemp

Plugin ID: `inputs.hddtemp`
Telegraf v1.0.0+

This plugin reads data from a [hddtemp](https://savannah.nongnu.org/projects/hddtemp/) daemon.

This plugin requires `hddtemp` to be installed and running as a daemon.

As the upstream project is not activly maintained anymore and various distributions (e.g. Debian Bookwork and later) don’t ship packages for `hddtemp` anymore, the binary might not be available (e.g. in Ubuntu 22.04 or later).

As an alternative consider using the [smartctl](/telegraf/v1/plugins/#input-smartctl) relying on SMART information or [sensors](/telegraf/v1/plugins/#input-sensors) plugins to retrieve temperature data of your hard-drive.

[View](/telegraf/v1/input-plugins/hddtemp/)

### HTTP

Plugin ID: `inputs.http`
Telegraf v1.6.0+

This plugin collects metrics from one or more HTTP endpoints providing data in one of the supported [data formats](/telegraf/v1/data_formats/input).

[View](/telegraf/v1/input-plugins/http/)

### HTTP Listener v2

Plugin ID: `inputs.http_listener_v2`
Telegraf v1.9.0+

This plugin listens for metrics sent via HTTP in any of the supported [data formats](/telegraf/v1/data_formats/input).

If you would like Telegraf to act as a proxy/relay for InfluxDB v1 or InfluxDB v2 it is recommended to use the [influxdb\_\_listener](/telegraf/v1/plugins/#input-influxdb_listener) or [influxdb\_v2\_listener](/telegraf/v1/plugins/#input-influxdb_v2_listener) plugin instead.

[View](/telegraf/v1/input-plugins/http_listener_v2/)

### HTTP Response

Plugin ID: `inputs.http_response`
Telegraf v0.12.1+

This plugin generates metrics from HTTP responses including the status code and response statistics.

[View](/telegraf/v1/input-plugins/http_response/)

### HueBridge

Plugin ID: `inputs.huebridge`
Telegraf v1.34.0+

This plugin gathers status from [Hue Bridge](https://www.philips-hue.com/) devices using the [CLIP API](https://developers.meethue.com/develop/hue-api-v2/) interface of the devices.

[View](/telegraf/v1/input-plugins/huebridge/)

### Hugepages

Plugin ID: `inputs.hugepages`
Telegraf v1.22.0+

This plugin gathers metrics from the Linux’ [Transparent Huge Pages (THP) memory management system](https://www.kernel.org/doc/html/latest/admin-guide/mm/hugetlbpage.html) that reduces the overhead of Translation Lookaside Buffer (TLB) lookups on machines with large amounts of memory.

[View](/telegraf/v1/input-plugins/hugepages/)

### Icinga2

Plugin ID: `inputs.icinga2`
Telegraf v1.8.0+

This plugin gather services and hosts status information using the [Icinga2 remote API](https://docs.icinga.com/icinga2/latest/doc/module/icinga2/chapter/icinga2-api).

[View](/telegraf/v1/input-plugins/icinga2/)

### InfiniBand

Plugin ID: `inputs.infiniband`
Telegraf v1.14.0+

This plugin gathers statistics for all InfiniBand devices and ports on the system. These are the counters that can be found in `/sys/class/infiniband/<dev>/port/<port>/counters/` and RDMA counters can be found in `/sys/class/infiniband/<dev>/ports/<port>/hw_counters/`

[View](/telegraf/v1/input-plugins/infiniband/)

### InfluxDB

Plugin ID: `inputs.influxdb`
Telegraf v0.2.5+

This plugin collects metrics on the given InfluxDB v1 servers from the `/debug/vars` endpoint. Read the [documentation](https://docs.influxdata.com/platform/monitoring/influxdata-platform/tools/measurements-internal/) for detailed information about `influxdb` metrics.

Additionally, this plugin can gather metrics from endpoints exposing InfluxDB-formatted endpoints.

To gather [InfluxDB v2 metrics](https://docs.influxdata.com/influxdb/latest/reference/internals/metrics/) use the [prometheus plugin](/telegraf/v1/plugins/#input-prometheus) with\[\[inputs.prometheus\]\] urls = \[“http://localhost:8086/metrics”\] metric\_version = 1

[View](/telegraf/v1/input-plugins/influxdb/)

### InfluxDB Listener

Plugin ID: `inputs.influxdb_listener`
Telegraf v1.9.0+

This plugin listens for requests sent according to the [InfluxDB HTTP v1 API](https://docs.influxdata.com/influxdb/v1.8/guides/write_data/). This allows Telegraf to serve as a proxy/router for the `/write` endpoint of the InfluxDB HTTP API.

This plugin was previously known as `http_listener`. If you wish to send general metrics via HTTP it is recommended to use the [`http_listener_v2`](/telegraf/v1/plugins/#input-http_listener_v2) instead.

The `/write` endpoint supports the `precision` query parameter and can be set to one of `ns`, `u`, `ms`, `s`, `m`, `h`. All other parameters are ignored and defer to the output plugins configuration.

When chaining Telegraf instances using this plugin, `CREATE DATABASE` requests receive a `200 OK` response with message body `{"results":[]}` but they are not relayed. The configuration of the output plugin ultimately submits data to InfluxDB determines the destination database.

[View](/telegraf/v1/input-plugins/influxdb_listener/)

### InfluxDB V2 Listener

Plugin ID: `inputs.influxdb_v2_listener`
Telegraf v1.16.0+

This plugin listens for requests sent according to the [InfluxDB HTTP v2 API](https://docs.influxdata.com/influxdb/v2/api/). This allows Telegraf to serve as a proxy/router for the `/api/v2/write` endpoint of the InfluxDB HTTP API.

The `/api/v2/write` endpoint supports the `precision` query parameter and can be set to one of `ns`, `us`, `ms`, `s`. All other parameters are ignored and defer to the output plugins configuration.

[View](/telegraf/v1/input-plugins/influxdb_v2_listener/)

### Intel Baseband Accelerator

Plugin ID: `inputs.intel_baseband`
Telegraf v1.27.0+

This plugin collects metrics from both dedicated and integrated Intel devices providing Wireless Baseband hardware acceleration. These devices play a key role in accelerating 5G and 4G Virtualized Radio Access Networks (vRAN) workloads, increasing the overall compute capacity of commercial, off-the-shelf platforms by integrating e.g.

- Forward Error Correction (FEC) processing,
- 4G Turbo FEC processing,
- 5G Low Density Parity Check (LDPC)
- Fast Fourier Transform (FFT) block providing DFT/iDFT processing offload for the 5G Sounding Reference Signal (SRS)

[View](/telegraf/v1/input-plugins/intel_baseband/)

### Intel® Dynamic Load Balancer

Plugin ID: `inputs.intel_dlb`
Telegraf v1.25.0+

This plugin collects metrics exposed by applications built with the [Data Plane Development Kit](https://www.dpdk.org/), an extensive set of open source libraries designed for accelerating packet processing workloads, plugin is also using bifurcated driver. More specifically it’s targeted for applications using Intel DLB as eventdev devices accessed via bifurcated driver (allowing access from kernel and user-space).

[View](/telegraf/v1/input-plugins/intel_dlb/)

### Intel® Platform Monitoring Technology

Plugin ID: `inputs.intel_pmt`
Telegraf v1.28.0+

This plugin collects metrics via the Linux kernel driver for Intel® Platform Monitoring Technology (Intel® PMT), an architecture capable of enumerating and accessing hardware monitoring capabilities on supported devices.

[View](/telegraf/v1/input-plugins/intel_pmt/)

### Intel Performance Monitoring Unit

Plugin ID: `inputs.intel_pmu`
Telegraf v1.21.0+

This plugin gathers Intel Performance Monitoring Unit metrics available via the [Linux Perf](https://perf.wiki.kernel.org/index.php/Main_Page) subsystem.

PMU metrics provide insights into performance and health of IA processors’ internal components, including core and uncore units. With the number of cores increasing and processor topology getting more complex the insight into those metrics is vital to assure the best CPU performance and utilization.

Performance counters are CPU hardware registers that count hardware events such as instructions executed, cache-misses suffered, or branches mispredicted. They form a basis for profiling applications to trace dynamic control flow and identify hotspots.

[View](/telegraf/v1/input-plugins/intel_pmu/)

### Intel PowerStat

Plugin ID: `inputs.intel_powerstat`
Telegraf v1.17.0+

This plugin gathers power statistics on Intel-based platforms providing insights into power saving and workload migration. Those are beneficial for Monitoring and Analytics systems to take preventive or corrective actions based on platform busyness, CPU temperature, actual CPU utilization and power statistics.

[View](/telegraf/v1/input-plugins/intel_powerstat/)

### Intel RDT

Plugin ID: `inputs.intel_rdt`
Telegraf v1.16.0+

This plugin collects information provided by monitoring features of the [Intel Resource Director Technology](https://www.intel.com/content/www/us/en/architecture-and-technology/resource-director-technology.html), a hardware framework to monitor and control the utilization of shared resources (e.g. last level cache, memory bandwidth).

Intel’s Resource Director Technology (RDT) framework consists of:

- Cache Monitoring Technology (CMT)
- Memory Bandwidth Monitoring (MBM)
- Cache Allocation Technology (CAT)
- Code and Data Prioritization (CDP)

As multithreaded and multicore platform architectures emerge, the last level cache and memory bandwidth are key resources to manage for running workloads in single-threaded, multithreaded, or complex virtual machine environments. Intel introduces CMT, MBM, CAT and CDP to manage these workloads across shared resources.

[View](/telegraf/v1/input-plugins/intel_rdt/)

### Telegraf Internal

Plugin ID: `inputs.internal`
Telegraf v1.2.0+

This plugin collects metrics about the telegraf agent and its plugins.

Some metrics are aggregates across all instances of a plugin type.

[View](/telegraf/v1/input-plugins/internal/)

### Internet Speed Monitor

Plugin ID: `inputs.internet_speed`
Telegraf v1.20.0+

This plugin collects metrics about the internet speed on the system like download/upload speed, latency etc using the [speedtest.net service](https://www.speedtest.net/).

[View](/telegraf/v1/input-plugins/internet_speed/)

### Interrupts

Plugin ID: `inputs.interrupts`
Telegraf v1.3.0+

This plugin gathers metrics about IRQs from interrupts (`/proc/interrupts`) and soft-interrupts (`/proc/softirqs`).

[View](/telegraf/v1/input-plugins/interrupts/)

### IPMI Sensor

Plugin ID: `inputs.ipmi_sensor`
Telegraf v0.12.0+

This plugin gathers metrics from the [Intelligent Platform Management Interface](https://www.intel.com/content/dam/www/public/us/en/documents/specification-updates/ipmi-intelligent-platform-mgt-interface-spec-2nd-gen-v2-0-spec-update.pdf) using the [`ipmitool`](https://github.com/ipmitool/ipmitool) command line utility.

The `ipmitool` requires access to the IPMI device. Please check the permission section for possible solutions.

[View](/telegraf/v1/input-plugins/ipmi_sensor/)

### Ipset

Plugin ID: `inputs.ipset`
Telegraf v1.6.0+

This plugin gathers packets and bytes counters from [Linux IP sets](https://ipset.netfilter.org/) using the `ipset` command line tool.

IP sets created without the “counters” option are ignored.

[View](/telegraf/v1/input-plugins/ipset/)

### Iptables

Plugin ID: `inputs.iptables`
Telegraf v1.1.0+

This plugin gathers packets and bytes counters for rules within a set of table and chain from the Linux’s iptables firewall.

Rules are identified through associated comment, so you must ensure that the rules you want to monitor do have a **unique** comment using the `--comment` flag when adding them. Rules without comments are ignored.

The rule number cannot be used as identifier as it is not constant and may vary when rules are inserted/deleted at start-up or by automatic tools (interactive firewalls, fail2ban, …).

The `iptables` command requires `CAP_NET_ADMIN` and `CAP_NET_RAW` capabilities. Check the permissions section for ways to grant them.

[View](/telegraf/v1/input-plugins/iptables/)

### IPVS

Plugin ID: `inputs.ipvs`
Telegraf v1.9.0+

This plugin gathers metrics about the [IPVS virtual and real servers](http://www.linuxvirtualserver.org/software/ipvs.html) using the netlink socket interface of the Linux kernel.

The plugin requires `CAP_NET_ADMIN` and `CAP_NET_RAW` capabilities. Check the permissions section for ways to grant them.

[View](/telegraf/v1/input-plugins/ipvs/)

### Jenkins

Plugin ID: `inputs.jenkins`
Telegraf v1.9.0+

This plugin gathers information about the nodes and jobs running in a [Jenkins](https://www.jenkins.io/) instance. The plugin uses the Jenkins API and does not require a plugin on the server.

[View](/telegraf/v1/input-plugins/jenkins/)

### Jolokia2 Agent

Plugin ID: `inputs.jolokia2_agent`
Telegraf v1.5.0+

This plugin reads JMX metrics from one or more [Jolokia agent](https://jolokia.org/agent/jvm.html) REST endpoints.

[View](/telegraf/v1/input-plugins/jolokia2_agent/)

### Jolokia2 Proxy

Plugin ID: `inputs.jolokia2_proxy`
Telegraf v1.5.0+

This plugin reads JMX metrics from one or more *targets* by interacting with a [Jolokia proxy](https://jolokia.org/features/proxy.html) REST endpoint.

[View](/telegraf/v1/input-plugins/jolokia2_proxy/)

### Juniper Telemetry

Plugin ID: `inputs.jti_openconfig_telemetry`
Telegraf v1.7.0+

This service plugin reads [OpenConfig](http://openconfig.net/) telemetry data via the [Junos Telemetry Interface (JTI)](https://www.juniper.net/documentation/en_US/junos/topics/concept/junos-telemetry-interface-oveview.html) from configured from listed sensors.

[View](/telegraf/v1/input-plugins/jti_openconfig_telemetry/)

### Apache Kafka Consumer

Plugin ID: `inputs.kafka_consumer`
Telegraf v0.2.3+

This service plugin consumes messages from [Kafka brokers](https://kafka.apache.org) in one of the supported [data formats](/telegraf/v1/data_formats/input). The plugin uses [consumer groups](http://godoc.org/github.com/wvanbergen/kafka/consumergroup) when talking to the Kafka cluster so multiple instances of Telegraf can consume messages from the same topic in parallel.

[View](/telegraf/v1/input-plugins/kafka_consumer/)

### Kapacitor

Plugin ID: `inputs.kapacitor`
Telegraf v1.3.0+

This plugin collects metrics from the configured [InfluxData Kapacitor](https://www.influxdata.com/time-series-platform/kapacitor/) instances.

[View](/telegraf/v1/input-plugins/kapacitor/)

### Kernel

Plugin ID: `inputs.kernel`
Telegraf v0.11.0+

This plugin gathers metrics about the [Linux kernel](https://kernel.org/) including, among others, the [available entropy](https://www.kernel.org/doc/html/latest/admin-guide/sysctl/kernel.html#random), [Kernel Samepage Merging](https://www.kernel.org/doc/html/latest/mm/ksm.html) and [Pressure Stall Information](https://www.kernel.org/doc/html/latest/accounting/psi.html).

[View](/telegraf/v1/input-plugins/kernel/)

### Kernel VM Statistics

Plugin ID: `inputs.kernel_vmstat`
Telegraf v1.0.0+

This plugin gathers virtual memory statistics of the [Linux kernel](https://kernel.org/) by reading `/proc/vmstat`. For a full list of available fields check the `/proc/vmstat` section of the [proc man page](http://man7.org/linux/man-pages/man5/proc.5.html) and for a detailed description about the fields see the [vmstat man page](https://man7.org/linux/man-pages/man8/vmstat.8.html).

[View](/telegraf/v1/input-plugins/kernel_vmstat/)

### Kibana

Plugin ID: `inputs.kibana`
Telegraf v1.8.0+

This plugin collects metrics about service status from [Kibana](https://www.elastic.co/kibana) instances via the server’s API.

This plugin requires Kibana version 6.0+.

[View](/telegraf/v1/input-plugins/kibana/)

### Kinesis Consumer

Plugin ID: `inputs.kinesis_consumer`
Telegraf v1.10.0+

This service input plugin consumes messages from [AWS Kinesis](https://aws.amazon.com/kinesis/) data stream in one of the supported [data formats](/telegraf/v1/data_formats/input).

[View](/telegraf/v1/input-plugins/kinesis_consumer/)

### KNX

Plugin ID: `inputs.knx_listener`
Telegraf v1.19.0+

This service plugin listens for messages on the [KNX home-automation bus](https://www.knx.org) by connecting via a KNX-IP interface. Information about supported KNX datapoint-types can be found at the underlying [`knx-go` project](https://github.com/vapourismo/knx-go).

[View](/telegraf/v1/input-plugins/knx_listener/)

### Kubernetes Inventory

Plugin ID: `inputs.kube_inventory`
Telegraf v1.10.0+

This plugin gathers metrics from [Kubernetes](https://kubernetes.io/) resources.

This plugin requires Kubernetes version 1.11+.

The gathered resources include for example daemon sets, deployments, endpoints, ingress, nodes, persistent volumes and many more.

This plugin produces high cardinality data, which when not controlled for will cause high load on your database. Please make sure to [filter](/telegraf/v1/configuration/#metric-filtering) the produced metrics or configure your database to avoid cardinality issues!

[View](/telegraf/v1/input-plugins/kube_inventory/)

### Kubernetes

Plugin ID: `inputs.kubernetes`
Telegraf v1.1.0+

This plugin gathers metrics about running pods and containers of a [Kubernetes](https://kubernetes.io/) instance via the Kubelet API.

This plugin has to run as part of a `daemonset` within a Kubernetes installation. Telegraf must run on every node within the cluster.

You should configure this plugin to talk to its locally running kubelet.

This plugin produces high cardinality data, which when not controlled for will cause high load on your database. Please make sure to [filter](/telegraf/v1/configuration/#metric-filtering) the produced metrics or configure your database to avoid cardinality issues!

[View](/telegraf/v1/input-plugins/kubernetes/)

### Arista LANZ Consumer

Plugin ID: `inputs.lanz`
Telegraf v1.14.0+

This service plugin consumes messages from the [Arista Networks’ Latency Analyzer (LANZ)](https://www.arista.com/en/um-eos/eos-latency-analyzer-lanz) by receiving the datastream on TCP (usually through port 50001) on the switch’s management IP.

You will need to configure LANZ and enable streaming LANZ data, see the [documentation](https://www.arista.com/en/um-eos/eos-section-44-3-configuring-lanz) for more details.

[View](/telegraf/v1/input-plugins/lanz/)

### LDAP

Plugin ID: `inputs.ldap`
Telegraf v1.29.0+

This plugin gathers metrics from LDAP servers’ monitoring (`cn=Monitor`) backend. Currently this plugin supports [OpenLDAP](https://www.openldap.org/) and [389ds](https://www.port389.org/) servers.

[View](/telegraf/v1/input-plugins/ldap/)

### LeoFS

Plugin ID: `inputs.leofs`
Telegraf v0.1.5+

This plugin gathers metrics of the [LEO filesystem](https://leo-project.net/leofs/) services *LeoGateway*, *LeoManager*, and *LeoStorage* via SNMP. Check the [LeoFS system monitoring documentation](https://leo-project.net/leofs/docs/admin/system_admin/monitoring/) for details.

[View](/telegraf/v1/input-plugins/leofs/)

### Libvirt

Plugin ID: `inputs.libvirt`
Telegraf v1.25.0+

This plugin collects statistics about virtualized guests on a system by using the [libvirt](https://libvirt.org/) virtualization API. Metrics are gathered directly from the hypervisor on a host system, so Telegraf doesn’t have to be installed and configured on a guest system.

[View](/telegraf/v1/input-plugins/libvirt/)

### Linux CPU

Plugin ID: `inputs.linux_cpu`
Telegraf v1.24.0+

This plugin gathers CPU metrics exposed on [Linux](https://kernel.org/) systems.

[View](/telegraf/v1/input-plugins/linux_cpu/)

### Linux Sysctl Filesystem

Plugin ID: `inputs.linux_sysctl_fs`
Telegraf v1.24.0+

This plugin gathers metrics by reading the [system filesystem](https://www.kernel.org/doc/Documentation/sysctl/fs.txt) files on [Linux](https://kernel.org/) systems.

[View](/telegraf/v1/input-plugins/linux_sysctl_fs/)

### LogQL

Plugin ID: `inputs.logql`
Telegraf v1.37.0+

This plugin gathers metrics from a [Loki](https://grafana.com/oss/loki/) endpoint using [LogQL queries](https://grafana.com/docs/loki/latest/query/) via the [HTTP API](https://grafana.com/docs/loki/latest/reference/loki-http-api/).

[View](/telegraf/v1/input-plugins/logql/)

### Logstash

Plugin ID: `inputs.logstash`
Telegraf v1.12.0+

This plugin gathers metrics from a [Logstash](https://www.elastic.co/logstash) endpoint using the [Monitoring API](https://www.elastic.co/guide/en/logstash/current/monitoring-logstash.html).

This plugin supports Logstash 5+.

[View](/telegraf/v1/input-plugins/logstash/)

### Lustre

Plugin ID: `inputs.lustre2`
Telegraf v0.1.5+

This plugin gathers metrics for the [Lustre® file system](http://lustre.org/) using its entries in the `proc` filesystem. Reference the [Lustre Monitoring and Statistics Guide](http://wiki.lustre.org/Lustre_Monitoring_and_Statistics_Guide) for the reported information.

This plugin doesn’t report *all* information available but only a limited set of items. Check the metrics section.

[View](/telegraf/v1/input-plugins/lustre2/)

### Logical Volume Manager

Plugin ID: `inputs.lvm`
Telegraf v1.21.0+

This plugin collects information about physical volumes, volume groups and logical volumes from the Logical Volume Management (LVM) of the [Linux kernel](https://www.kernel.org/).

[View](/telegraf/v1/input-plugins/lvm/)

### Mailchimp

Plugin ID: `inputs.mailchimp`
Telegraf v0.2.4+

This plugin gathers metrics from the [Mailchimp](https://mailchimp.com) service using the [Mailchimp API](https://developer.mailchimp.com/).

[View](/telegraf/v1/input-plugins/mailchimp/)

### MarkLogic

Plugin ID: `inputs.marklogic`
Telegraf v1.12.0+

This plugin gathers health status metrics from one or more [MarkLogic](https://www.progress.com/marklogic) hosts.

[View](/telegraf/v1/input-plugins/marklogic/)

### MavLink

Plugin ID: `inputs.mavlink`
Telegraf v1.35.0+

This plugin collects metrics from [MavLink](https://mavlink.io/)\-compatible flight controllers such as [ArduPilot](https://ardupilot.org/) or [PX4](https://px4.io/) to live ingest flight metrics from unmanned systems (drones, planes, boats, etc.) Currently the ArduPilot-specific Mavlink dialect is used, check the [Mavlink documentation](https://mavlink.io/en/messages/ardupilotmega.html) for more details and the various messages available.

This plugin potentially generates a large amount of data. If your output plugin cannot handle the rate of messages, use [Metric filters](/telegraf/v1/configuration/#metric-filtering) to limit the metrics written to outputs, and/or the `filters` configuration parameter to limit which Mavlink messages this plugin parses.

[View](/telegraf/v1/input-plugins/mavlink/)

### Mcrouter

Plugin ID: `inputs.mcrouter`
Telegraf v1.7.0+

This plugin gathers statistics data from [Mcrouter](https://github.com/facebook/mcrouter) instances, a protocol router, developed and maintained by Facebook, for scaling [memcached](http://memcached.org/) deployments.

[View](/telegraf/v1/input-plugins/mcrouter/)

### MD RAID Statistics

Plugin ID: `inputs.mdstat`
Telegraf v1.20.0+

This plugin gathers statistics about any [Linux MD RAID arrays](https://docs.kernel.org/admin-guide/md.html) configured on the host by reading `/proc/mdstat`. For a full list of available fields see the `/proc/mdstat` section of the [proc man page](http://man7.org/linux/man-pages/man5/proc.5.html). For details on the fields check the [mdstat wiki](https://raid.wiki.kernel.org/index.php/Mdstat).

[View](/telegraf/v1/input-plugins/mdstat/)

### Memory

Plugin ID: `inputs.mem`
Telegraf v0.1.5+

This plugin collects metrics about the system memory.

For an explanation of the difference between *used* and *actual\_used* RAM, see [Linux ate my ram](http://www.linuxatemyram.com/).

[View](/telegraf/v1/input-plugins/mem/)

### Memcached

Plugin ID: `inputs.memcached`
Telegraf v0.1.2+

This plugin gathers statistics data from [Memcached](https://memcached.org/) instances.

[View](/telegraf/v1/input-plugins/memcached/)

### Apache Mesos

Plugin ID: `inputs.mesos`
Telegraf v0.10.3+

This plugin gathers metrics from [Apache Mesos](https://mesos.apache.org/) instances. For more information, please check the [Mesos Observability Metrics](http://mesos.apache.org/documentation/latest/monitoring/) page.

[View](/telegraf/v1/input-plugins/mesos/)

### Minecraft

Plugin ID: `inputs.minecraft`
Telegraf v1.4.0+

This plugin collects score metrics from a [Minecraft](https://www.minecraft.net/) server using the RCON protocol.

This plugin supports Minecraft Java Edition versions 1.11 - 1.14. When using a version earlier than 1.13, be aware that the values for some criteria has changed and need to be modified.

[View](/telegraf/v1/input-plugins/minecraft/)

### Mock Data

Plugin ID: `inputs.mock`
Telegraf v1.22.0+

The plugin generates mock-metrics based on different algorithms like sine-wave functions, random numbers and more with the configured names and tags. Those metrics are usefull during testing (e.g. processors) or if random data is required.

[View](/telegraf/v1/input-plugins/mock/)

### Modbus

Plugin ID: `inputs.modbus`
Telegraf v1.14.0+

This plugin collects data from [Modbus](https://www.modbus.org/) registers using e.g. Modbus TCP or serial interfaces with Modbus RTU or Modbus ASCII.

[View](/telegraf/v1/input-plugins/modbus/)

### MongoDB

Plugin ID: `inputs.mongodb`
Telegraf v0.1.5+

This plugin collects metrics about [MongoDB](https://www.mongodb.com) server instances by running database commands.

This plugin supports all versions marked as supported in the [MongoDB Software Lifecycle Schedules](https://www.mongodb.com/support-policy/lifecycles).

[View](/telegraf/v1/input-plugins/mongodb/)

### Monit

Plugin ID: `inputs.monit`
Telegraf v1.14.0+

This plugin gathers metrics and status information about local processes, remote hosts, files, file systems, directories and network interfaces managed and watched over by [Monit](https://mmonit.com/).

The plugin supports Monit version 5.16+. To use this plugin you have to enable the [HTTPD TCP port](https://mmonit.com/monit/documentation/monit.html#TCP-PORT) in Monit.

[View](/telegraf/v1/input-plugins/monit/)

### MQTT Consumer

Plugin ID: `inputs.mqtt_consumer`
Telegraf v0.10.3+

This service plugin consumes messages from [MQTT](https://mqtt.org) brokers for the configured topics in one of the supported [data formats](/telegraf/v1/data_formats/input).

[View](/telegraf/v1/input-plugins/mqtt_consumer/)

### Multifile

Plugin ID: `inputs.multifile`
Telegraf v1.10.0+

This plugin reads the combined data from multiple files into a single metric, creating one field or tag per file. This is often useful creating custom metrics from the `/sys` or `/proc` filesystems.

To parse metrics from a single file you should use the [file](/telegraf/v1/plugins/#input-file) input plugin instead.

[View](/telegraf/v1/input-plugins/multifile/)

### MySQL

Plugin ID: `inputs.mysql`
Telegraf v0.1.1+

This plugin gathers statistics from [MySQL](https://www.mysql.com/) server instances.

To gather metrics from the performance schema, it must first be enabled in MySQL. See the performance schema [quick start](https://dev.mysql.com/doc/refman/8.0/en/performance-schema-quick-start.html) for details.

[View](/telegraf/v1/input-plugins/mysql/)

### NATS Server Monitoring

Plugin ID: `inputs.nats`
Telegraf v1.6.0+

This plugin gathers metrics of a [NATS](http://www.nats.io) server instance using its [monitoring endpoints](https://docs.nats.io/running-a-nats-service/nats_admin/monitoring).

[View](/telegraf/v1/input-plugins/nats/)

### NATS Consumer

Plugin ID: `inputs.nats_consumer`
Telegraf v0.10.3+

This service plugin consumes messages from [NATS](https://www.nats.io/about/) instances in one of the supported [data formats](/telegraf/v1/data_formats/input). A [Queue Group](https://www.nats.io/documentation/concepts/nats-queueing/) is used when subscribing to subjects so multiple instances of telegraf can consume messages in parallel. The plugin supports authenticating via [username/password](https://docs.nats.io/using-nats/developer/connecting/userpass), a [credentials file](https://docs.nats.io/using-nats/developer/connecting/creds) (NATS 2.0), or an [nkey seed file](https://docs.nats.io/using-nats/developer/connecting/nkey) (NATS 2.0).

[View](/telegraf/v1/input-plugins/nats_consumer/)

### Neoom Beaam

Plugin ID: `inputs.neoom_beaam`
Telegraf v1.33.0+

This plugin gathers metrics from a [Neoom Beaam gateway](https://neoom.com/en/products/beaam) using the [Beaam API](https://developer.neoom.com/reference/concepts-terms-1) with access token that can be created in the Neoom web interface. Please follow the [developer instructions](https://neoom.com/developers) to create the token.

[View](/telegraf/v1/input-plugins/neoom_beaam/)

### Neptune Apex

Plugin ID: `inputs.neptune_apex`
Telegraf v1.10.0+

This plugin gathers metrics from [Neptune Apex controller](https://www.neptunesystems.com) instances, allowing aquarium hobbyists to monitor and control their tanks based on various probes.

[View](/telegraf/v1/input-plugins/neptune_apex/)

### Network

Plugin ID: `inputs.net`
Telegraf v0.1.1+

This plugin gathers metrics about network interface and protocol usage.

[View](/telegraf/v1/input-plugins/net/)

### Network Response

Plugin ID: `inputs.net_response`
Telegraf v0.10.3+

This plugin tests UDP/TCP connection and produces metrics from the result, the response time and optionally verifies text in the response.

[View](/telegraf/v1/input-plugins/net_response/)

### Netflow

Plugin ID: `inputs.netflow`
Telegraf v1.25.0+

This service plugin acts as a collector for Netflow v5, Netflow v9 and IPFIX flow information. The Layer 4 protocol numbers are gathered from the [official IANA assignments](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml). The internal field mappings for Netflow v5 fields are defined according to [Cisco’s Netflow v5 documentation](https://www.cisco.com/c/en/us/td/docs/net_mgmt/netflow_collection_engine/3-6/user/guide/format.html#wp1006186), Netflow v9 fields are defined according to [Cisco’s Netflow v9 documentation](https://www.cisco.com/en/US/technologies/tk648/tk362/technologies_white_paper09186a00800a3db9.html) and the [ASA extensions](https://www.cisco.com/c/en/us/td/docs/security/asa/special/netflow/asa_netflow.html). Definitions for IPFIX are according to [IANA assignment document](https://www.iana.org/assignments/ipfix/ipfix.xhtml#ipfix-nat-type).

[View](/telegraf/v1/input-plugins/netflow/)

### Network Connection Statistics

Plugin ID: `inputs.netstat`
Telegraf v0.2.0+

This plugin collects statistics about TCP connection states and UDP socket counts.

[View](/telegraf/v1/input-plugins/netstat/)

### Network Filesystem

Plugin ID: `inputs.nfsclient`
Telegraf v1.18.0+

This plugin collects metrics about operations on [Network Filesystem](https://www.ietf.org/rfc/rfc1813.txt?number=1813) mounts. By default, only a limited number of general system-level metrics are collected, including basic read/write counts but more detailed metrics can be enabled.

Many of the metrics, even if tagged with a mount point, are really *per-server*. E.g. if you mount two shares: `nfs01:/vol/foo/bar` and `nfs01:/vol/foo/baz`, there will be two near identical entries in `/proc/self/mountstats`. This is a limitation of the metrics exposed by the kernel, not by this plugin.

[View](/telegraf/v1/input-plugins/nfsclient/)

### Nftables

Plugin ID: `inputs.nftables`
Telegraf v1.37.0+

This plugin gathers packets and bytes counters for rules within Linux’s [nftables](https://wiki.nftables.org/wiki-nftables/index.php/Main_Page) firewall.

Rules are identified by the associated comment so those **comments have to be unique**! Rules without comment are ignored.

[View](/telegraf/v1/input-plugins/nftables/)

### Nginx

Plugin ID: `inputs.nginx`
Telegraf v0.1.5+

This plugin gathers metrics from the open source [Nginx web server](https://www.nginx.com). Nginx Plus is a commercial version. For more information about differences between Nginx (F/OSS) and Nginx Plus, see the Nginx [documentation](https://www.nginx.com/blog/whats-difference-nginx-foss-nginx-plus/).

[View](/telegraf/v1/input-plugins/nginx/)

### Nginx Plus

Plugin ID: `inputs.nginx_plus`
Telegraf v1.5.0+

This plugin gathers metrics from the commercial [Nginx Plus web server](https://www.f5.com/products/nginx/nginx-plus) via the [status module](http://nginx.org/en/docs/http/ngx_http_status_module.html).

Using this plugin requires a license.

For more information about differences between Nginx (F/OSS) and Nginx Plus, see the Nginx [documentation](https://www.nginx.com/blog/whats-difference-nginx-foss-nginx-plus/).

[View](/telegraf/v1/input-plugins/nginx_plus/)

### Nginx Plus API

Plugin ID: `inputs.nginx_plus_api`
Telegraf v1.9.0+

This plugin gathers metrics from the commercial [Nginx Plus web server](https://www.f5.com/products/nginx/nginx-plus) via the [REST API](https://demo.nginx.com/swagger-ui/).

Using this plugin requires a license.

For more information about differences between Nginx (F/OSS) and Nginx Plus, see the Nginx [documentation](https://www.nginx.com/blog/whats-difference-nginx-foss-nginx-plus/).

[View](/telegraf/v1/input-plugins/nginx_plus_api/)

### Nginx Stream Server Traffic

Plugin ID: `inputs.nginx_sts`
Telegraf v1.15.0+

This plugin gathers metrics from the [Nginx web server](https://www.nginx.com) using the [external stream server traffic status module](https://github.com/vozlt/nginx-module-sts). This module provides access to stream host status information containing the current status of servers, upstreams and caches, similar to the live activity monitoring of Nginx plus. For module configuration details please see the [module documentation](https://github.com/vozlt/nginx-module-sts#synopsis).

[View](/telegraf/v1/input-plugins/nginx_sts/)

### Nginx Upstream Check

Plugin ID: `inputs.nginx_upstream_check`
Telegraf v1.10.0+

This plugin gathers metrics from the [Nginx web server](https://www.nginx.com) using the [upstream check module](https://github.com/yaoweibin/nginx_upstream_check_module). This module periodically sends the configured requests to servers in the Nginx’s upstream determining their availability.

[View](/telegraf/v1/input-plugins/nginx_upstream_check/)

### Nginx Virtual Host Traffic

Plugin ID: `inputs.nginx_vts`
Telegraf v1.9.0+

This plugin gathers metrics from the [Nginx web server](https://www.nginx.com) using the [external virtual host traffic status module](https://github.com/vozlt/nginx-module-vts). This module provides access to virtual host status information containing the current status of servers, upstreams and caches, similar to the live activity monitoring of Nginx plus. For module configuration details please see the [module documentation](https://github.com/vozlt/nginx-module-vts#synopsis).

[View](/telegraf/v1/input-plugins/nginx_vts/)

### Hashicorp Nomad

Plugin ID: `inputs.nomad`
Telegraf v1.22.0+

This plugin collects metrics from every [Nomad agent](https://www.nomadproject.io/) of the specified cluster. Telegraf may be present in every node and connect to the agent locally.

[View](/telegraf/v1/input-plugins/nomad/)

### NLnet Labs Name Server Daemon

Plugin ID: `inputs.nsd`
Telegraf v1.0.0+

This plugin gathers statistics from a [NLnet Labs Name Server Daemon](https://www.nlnetlabs.nl/projects/nsd/about), an authoritative DNS name server.

[View](/telegraf/v1/input-plugins/nsd/)

### Netgear Switch Discovery Protocol

Plugin ID: `inputs.nsdp`
Telegraf v1.34.0+

This plugin gathers metrics from devices via the [Netgear Switch Discovery Protocol](https://en.wikipedia.org/wiki/Netgear_Switch_Discovery_Protocol) for all available switches and ports.

[View](/telegraf/v1/input-plugins/nsdp/)

### NSQ

Plugin ID: `inputs.nsq`
Telegraf v1.16.0+

This plugin gathers metrics from [NSQ](https://nsq.io/) realtime distributed messaging platform instances using the [NSQD API](https://nsq.io/components/nsqd.html).

[View](/telegraf/v1/input-plugins/nsq/)

### NSQ Consumer

Plugin ID: `inputs.nsq_consumer`
Telegraf v0.10.1+

This service plugin consumes messages from [NSQ](https://nsq.io/) realtime distributed messaging platform brokers in one of the supported [data formats](/telegraf/v1/data_formats/input).

[View](/telegraf/v1/input-plugins/nsq_consumer/)

### Kernel Network Statistics

Plugin ID: `inputs.nstat`
Telegraf v0.13.1+

This plugin collects network metrics from `/proc/net/netstat`, `/proc/net/snmp` and `/proc/net/snmp6` files

[View](/telegraf/v1/input-plugins/nstat/)

### Network Time Protocol Query

Plugin ID: `inputs.ntpq`
Telegraf v0.11.0+

This plugin gathers metrics about [Network Time Protocol](https://ntp.org/) queries.

This plugin requires the `ntpq` executable to be installed on the system.

[View](/telegraf/v1/input-plugins/ntpq/)

### Nvidia System Management Interface (SMI)

Plugin ID: `inputs.nvidia_smi`
Telegraf v1.7.0+

This plugin collects metrics for [NVIDIA GPUs](https://www.nvidia.com/) including memory and GPU usage, temperature and other, using the [NVIDIA System Management Interface](https://developer.nvidia.com/nvidia-system-management-interface).

This plugin requires the `nvidia-smi` binary to be installed on the system.

[View](/telegraf/v1/input-plugins/nvidia_smi/)

### OPC UA Client Reader

Plugin ID: `inputs.opcua`
Telegraf v1.16.0+

This plugin gathers data from an [OPC UA](https://opcfoundation.org/about/opc-technologies/opc-ua/) server by subscribing to the configured nodes.

[View](/telegraf/v1/input-plugins/opcua/)

### OPC UA Client Listener

Plugin ID: `inputs.opcua_listener`
Telegraf v1.25.0+

This service plugin receives data from an [OPC UA](https://opcfoundation.org/about/opc-technologies/opc-ua/) server by subscribing to nodes and events.

[View](/telegraf/v1/input-plugins/opcua_listener/)

### OpenLDAP

Plugin ID: `inputs.openldap`
Telegraf v1.4.0+

This plugin gathers metrics from [OpenLDAP](https://www.openldap.org/)’s `cn=Monitor` backend. To use this plugin you must enable the [slapd monitoring](https://www.openldap.org/devel/admin/monitoringslapd.html) backend.

It is recommended to use the newer [`ldap` input plugin](/telegraf/v1/plugins/#input-ldap) instead.

[View](/telegraf/v1/input-plugins/openldap/)

### OpenNTPD

Plugin ID: `inputs.openntpd`
Telegraf v1.12.0+

This plugin gathers metrics from [OpenNTPD](http://www.openntpd.org/) using the `ntpctl` command.

The `ntpctl` binary must be present on the system and executable by Telegraf. The plugin supports using `sudo` for execution.

[View](/telegraf/v1/input-plugins/openntpd/)

### OpenSearch Query

Plugin ID: `inputs.opensearch_query`
Telegraf v1.26.0+

This plugin queries [OpenSearch](https://opensearch.org/) endpoints to derive metrics from data stored in an OpenSearch cluster like the number of hits for a search query, statistics on numeric fields, document counts, etc.

This plugins is tested against OpenSearch 2.5.0 and 1.3.7 but newer version should also work.

[View](/telegraf/v1/input-plugins/opensearch_query/)

### OpenSMTPD

Plugin ID: `inputs.opensmtpd`
Telegraf v1.5.0+

This plugin gathers statistics from [OpenSMTPD](https://www.opensmtpd.org/) using the `smtpctl` binary.

The `smtpctl` binary must be present on the system and executable by Telegraf. The plugin supports using `sudo` for execution.

[View](/telegraf/v1/input-plugins/opensmtpd/)

### OpenStack

Plugin ID: `inputs.openstack`
Telegraf v1.21.0+

This plugin collects metrics about services from [OpenStack](https://www.openstack.org/) endpoints.

Due to the large number of unique tags generated by the plugin it is **highly recommended** to use [metric filtering](/telegraf/v1/configuration/#modifiers) like `taginclude` and `tagexclude` to reduce cardinality.

[View](/telegraf/v1/input-plugins/openstack/)

### OpenTelemetry

Plugin ID: `inputs.opentelemetry`
Telegraf v1.19.0+

This service plugin receives traces, metrics, logs and profiles from [OpenTelemetry](https://opentelemetry.io) clients and compatible agents via gRPC.

Telegraf v1.32 through v1.35 support the Profiles signal using the v1 experimental API. Telegraf v1.36 supports the Profiles signal using the v1 development API before v0.1.0. Telegraf v1.37+ supports the Profiles signal using the v1 development API v0.2.0.

[View](/telegraf/v1/input-plugins/opentelemetry/)

### OpenWeatherMap

Plugin ID: `inputs.openweathermap`
Telegraf v1.11.0+

This plugin collects weather and forecast data from the [OpenWeatherMap](https://openweathermap.org) service.

To use this plugin you will need an [APP-ID](https://openweathermap.org/appid) to work.

[View](/telegraf/v1/input-plugins/openweathermap/)

### P4 Runtime

Plugin ID: `inputs.p4runtime`
Telegraf v1.26.0+

This plugin collects metrics from the data plane of network devices, such as Programmable Switches or Programmable Network Interface Cards by reading the `Counter` values of the [P4 program](https://p4.org) running on the device. Metrics are collected through a gRPC connection with the [P4 runtime](https://github.com/p4lang/p4runtime) server.

If you want to gather information about the program name, please follow the instruction in [6.2.1. Annotating P4 code with PkgInfo](https://p4.org/p4-spec/p4runtime/main/P4Runtime-Spec.html#sec-annotating-p4-code-with-pkginfo) to modify your P4 program.

[View](/telegraf/v1/input-plugins/p4runtime/)

### Passenger

Plugin ID: `inputs.passenger`
Telegraf v0.10.1+

This plugin gathers metrics from the [Phusion Passenger](https://www.phusionpassenger.com/) service.

Depending on your environment, this plugin can create a high number of series which can cause high load on your database. Please use [measurement filtering](/telegraf/v1/configuration/#metric-filtering) to manage your series cardinality!

The plugin uses the `passenger-status` command line tool.

This plugin requires the `passenger-status` binary to be installed on the system and to be executable by Telegraf.

[View](/telegraf/v1/input-plugins/passenger/)

### PF

Plugin ID: `inputs.pf`
Telegraf v1.5.0+

This plugin gathers information from the FreeBSD or OpenBSD pf firewall like the number of current entries in the table, counters for the number of searches, inserts, and removals to tables using the `pfctl` command.

This plugin requires the `pfctl` binary to be executable by Telegraf. It requires read access to the device file `/dev/pf`.

[View](/telegraf/v1/input-plugins/pf/)

### PgBouncer

Plugin ID: `inputs.pgbouncer`
Telegraf v1.8.0+

This plugin collects metrics from a [PgBouncer load balancer](https://pgbouncer.github.io) instance. Check the [documentation](https://pgbouncer.github.io/usage.html) for available metrics and their meaning.

This plugin requires PgBouncer v1.5+.

[View](/telegraf/v1/input-plugins/pgbouncer/)

### PHP-FPM

Plugin ID: `inputs.phpfpm`
Telegraf v0.1.10+

This plugin gathers statistics of the [PHP FastCGI Process Manager](https://www.php.net/manual/en/install.fpm.php) using either the HTTP status page or the fpm socket.

[View](/telegraf/v1/input-plugins/phpfpm/)

### Ping

Plugin ID: `inputs.ping`
Telegraf v0.1.8+

This plugin collects metrics on ICMP ping packets including the round-trip time, response times and other packet statistics.

When using the `exec` method the `ping` command must be available on the systems and executable by Telegraf.

[View](/telegraf/v1/input-plugins/ping/)

### Postfix

Plugin ID: `inputs.postfix`
Telegraf v1.5.0+

This plugin collects metrics on a local [Postfix](https://www.postfix.org/) instance reporting the length, size and age of the active, hold, incoming, maildrop, and deferred [queues](https://www.postfix.org/QSHAPE_README.html#queues).

[View](/telegraf/v1/input-plugins/postfix/)

### PostgreSQL

Plugin ID: `inputs.postgresql`
Telegraf v0.10.3+

This plugin provides metrics for a [PostgreSQL](https://www.postgresql.org/) Server instance. Recorded metrics are lightweight and use Dynamic Management Views supplied by PostgreSQL.

[View](/telegraf/v1/input-plugins/postgresql/)

### PostgreSQL Extensible

Plugin ID: `inputs.postgresql_extensible`
Telegraf v0.12.0+

This plugin queries a [PostgreSQL](https://www.postgresql.org/) server and provides metrics for the returned result. This is useful when using PostgreSQL extensions to collect additional metrics.

Please also check the more generic [sql input plugin](/telegraf/v1/plugins/#input-sql).

[View](/telegraf/v1/input-plugins/postgresql_extensible/)

### PowerDNS

Plugin ID: `inputs.powerdns`
Telegraf v0.10.2+

This plugin gathers metrics from [PowerDNS](https://www.powerdns.com/) servers using unix sockets.

This plugin will need access to the powerdns control socket.

[View](/telegraf/v1/input-plugins/powerdns/)

### PowerDNS Recursor

Plugin ID: `inputs.powerdns_recursor`
Telegraf v1.11.0+

This plugin gathers metrics from [PowerDNS Recursor](https://www.powerdns.com/powerdns-recursor) instances using the unix control-sockets.

Telegraf will need read and write access to the control socket and the `socket_dir`.

[View](/telegraf/v1/input-plugins/powerdns_recursor/)

### Processes

Plugin ID: `inputs.processes`
Telegraf v0.11.0+

This plugin gathers info about the total number of processes and groups them by status (zombie, sleeping, running, etc.)

On Linux this plugin requires access to procfs (/proc), on other operating systems the plugin must be able to execute the `ps` command.

[View](/telegraf/v1/input-plugins/processes/)

### Procstat

Plugin ID: `inputs.procstat`
Telegraf v0.2.0+

This plugin allows to monitor the system resource usage of one or more processes. The plugin provides metrics about the individual processes as well as accumulated metrics on the number of PIDs returned on a search. Processes can be filtered e.g. by regular expressions on the command, the user owning the process or the service that started the process.

[View](/telegraf/v1/input-plugins/procstat/)

### Prometheus

Plugin ID: `inputs.prometheus`
Telegraf v0.1.5+

This plugin gathers metrics from [Prometheus](https://prometheus.io/) metric endpoints such as applications implementing such an endpoint or node-exporter instances. This plugin also supports various service-discovery methods.

[View](/telegraf/v1/input-plugins/prometheus/)

### PromQL

Plugin ID: `inputs.promql`
Telegraf v1.37.0+

This plugin gathers metrics from a [Prometheus](https://prometheus.io/) endpoint using [PromQL queries](https://prometheus.io/docs/prometheus/latest/querying/basics/) via the [HTTP API](https://prometheus.io/docs/prometheus/latest/querying/api/).

[View](/telegraf/v1/input-plugins/promql/)

### Proxmox

Plugin ID: `inputs.proxmox`
Telegraf v1.16.0+

This plugin gathers metrics about containers and VMs running on a [Proxmox](https://www.proxmox.com) instance using the Proxmox API.

[View](/telegraf/v1/input-plugins/proxmox/)

### Puppet Agent

Plugin ID: `inputs.puppetagent`
Telegraf v0.2.0+

This plugin gathers metrics of a [Puppet agent](https://www.puppet.com/) by parsing variables from the local last-run-summary file.

[View](/telegraf/v1/input-plugins/puppetagent/)

### RabbitMQ

Plugin ID: `inputs.rabbitmq`
Telegraf v0.1.5+

This plugin gathers statistics from [RabbitMQ](https://www.rabbitmq.com) servers via the [Management Plugin](https://www.rabbitmq.com/management.html).

[View](/telegraf/v1/input-plugins/rabbitmq/)

### Radius

Plugin ID: `inputs.radius`
Telegraf v1.26.0+

This plugin collects response times for [Radius](https://datatracker.ietf.org/doc/html/rfc2865) authentication requests.

[View](/telegraf/v1/input-plugins/radius/)

### Raindrops Middleware

Plugin ID: `inputs.raindrops`
Telegraf v0.10.3+

This plugin collects statistics for [Raindrops middleware](http://raindrops.bogomips.org/Raindrops/Middleware.html) instances.

[View](/telegraf/v1/input-plugins/raindrops/)

### RAS Daemon

Plugin ID: `inputs.ras`
Telegraf v1.16.0+

This plugin gathers statistics and error counts provided by the local [RAS (reliability, availability and serviceability)](https://github.com/mchehab/rasdaemon) daemon.

This plugin requires access to SQLite3 database from `RASDaemon`. Please make sure the Telegraf user has the required permissions to this database!

[View](/telegraf/v1/input-plugins/ras/)

### RavenDB

Plugin ID: `inputs.ravendb`
Telegraf v1.18.0+

This plugin gathers metrics from [RavenDB](https://ravendb.net/) servers via the monitoring API.

This plugin requires RavenDB Server v5.2+.

[View](/telegraf/v1/input-plugins/ravendb/)

### Redfish

Plugin ID: `inputs.redfish`
Telegraf v1.15.0+

This plugin gathers metrics and status information of server hardware with enabled [DMTF’s Redfish](https://redfish.dmtf.org/) support.

[View](/telegraf/v1/input-plugins/redfish/)

### Redis

Plugin ID: `inputs.redis`
Telegraf v0.1.1+

This plugin gathers metrics from [Redis](https://redis.io/) servers.

[View](/telegraf/v1/input-plugins/redis/)

### Redis Sentinel

Plugin ID: `inputs.redis_sentinel`
Telegraf v1.22.0+

This plugin collects metrics for [Redis Sentinel](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/) instances monitoring Redis servers and replicas.

[View](/telegraf/v1/input-plugins/redis_sentinel/)

### RethinkDB

Plugin ID: `inputs.rethinkdb`
Telegraf v0.1.3+

This plugin collects metrics from [RethinkDB](https://www.rethinkdb.com/) servers.

[View](/telegraf/v1/input-plugins/rethinkdb/)

### Riak

Plugin ID: `inputs.riak`
Telegraf v0.10.4+

This plugin gathers metrics from [Riak](https://riak.com/) instances.

[View](/telegraf/v1/input-plugins/riak/)

### Riemann Listener

Plugin ID: `inputs.riemann_listener`
Telegraf v1.17.0+

This service plugin listens for messages from [Riemann](https://riemann.io/) clients using the protocol buffer format.

[View](/telegraf/v1/input-plugins/riemann_listener/)

### Siemens S7

Plugin ID: `inputs.s7comm`
Telegraf v1.28.0+

This plugin reads metrics from Siemens PLCs via the S7 protocol.

[View](/telegraf/v1/input-plugins/s7comm/)

### Salesforce

Plugin ID: `inputs.salesforce`
Telegraf v1.4.0+

This plugin gathers metrics about the limits in your [Salesforce](https://salesforce.com) organization and the remaining usage using the [limits endpoint](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_limits.htm) of Salesforce’s REST API.

[View](/telegraf/v1/input-plugins/salesforce/)

### LM Sensors

Plugin ID: `inputs.sensors`
Telegraf v0.10.1+

This plugin collects metrics from hardware sensors using [lm-sensors](https://en.wikipedia.org/wiki/Lm_sensors).

This plugin requires the lm-sensors package to be installed on the system and `sensors` to be executable from Telegraf.

[View](/telegraf/v1/input-plugins/sensors/)

### SFlow

Plugin ID: `inputs.sflow`
Telegraf v1.14.0+

This service plugin produces metrics from information received by acting as a [SFlow V5](https://sflow.org/sflow_version_5.txt) collector. Currently, the plugin can collect Flow Samples of Ethernet / IPv4, IPv4 TCP and UDP headers. Counters and other header samples are ignored. Please use the [netflow plugin](/telegraf/v1/plugins/#input-netflow) for a more modern and sophisticated implementation.

This plugin produces high cardinality data, which when not controlled for will cause high load on your database. Please make sure to [filter](/telegraf/v1/configuration/#metric-filtering) the produced metrics or configure your database to avoid cardinality issues!

[View](/telegraf/v1/input-plugins/sflow/)

### Slab

Plugin ID: `inputs.slab`
Telegraf v1.23.0+

This plugin collects details on memory consumption of [Slab cache](https://www.kernel.org/doc/gorman/html/understand/understand011.html) entries by parsing the `/proc/slabinfo` file respecting the `HOST_PROC` environment variable.

This plugin requires `/proc/slabinfo` to be readable by the Telegraf user.

[View](/telegraf/v1/input-plugins/slab/)

### SLURM

Plugin ID: `inputs.slurm`
Telegraf v1.32.0+

This plugin gather diagnoses, jobs, nodes, partitions and reservation metrics for a [SLURM](https://slurm.schedmd.com) instance using the REST API provided by the `slurmrestd` daemon.

This plugin supports the [REST API v0.0.38](https://slurm.schedmd.com/rest.html) which must be enabled in the `slurmrestd` daemon. For more information, check the [documentation](https://slurm.schedmd.com/rest_quickstart.html#customization).

[View](/telegraf/v1/input-plugins/slurm/)

### S.M.A.R.T.

Plugin ID: `inputs.smart`
Telegraf v1.5.0+

This plugin collects [Self-Monitoring, Analysis and Reporting Technology](https://en.wikipedia.org/wiki/Self-Monitoring,_Analysis_and_Reporting_Technology) information for storage devices information using the `smartmontools` package. This plugin also supports NVMe devices by using the [`nvme-cli`](https://github.com/linux-nvme/nvme-cli) package.

This plugin requires the `smartmontools` and, for NVMe devices, the [`nvme-cli`](https://github.com/linux-nvme/nvme-cli) packages to be installed on your system. The `smartctl` and `nvme` commands must to be executable by Telegraf.

[View](/telegraf/v1/input-plugins/smart/)

### smartctl JSON

Plugin ID: `inputs.smartctl`
Telegraf v1.31.0+

This plugin collects [Self-Monitoring, Analysis and Reporting Technology](https://en.wikipedia.org/wiki/Self-Monitoring,_Analysis_and_Reporting_Technology) information for storage devices information using the `smartmontools` package. Contrary to the [smart plugin](/telegraf/v1/plugins/#input-smart), this plugin does not use the [`nvme-cli`](https://github.com/linux-nvme/nvme-cli) package to collect additional information about NVMe devices.

This plugin requires `smartmontools` to be installed on your system. The `smartctl` command must to be executable by Telegraf and must supporting JSON output. JSON output was added in v7.0 and improved in subsequent releases

[View](/telegraf/v1/input-plugins/smartctl/)

### SNMP

Plugin ID: `inputs.snmp`
Telegraf v0.10.1+

This plugin gathers metrics by polling [SNMP](https://datatracker.ietf.org/doc/html/rfc1157) agents with individual OIDs or complete SNMP tables.

The path setting is shared between all instances of all SNMP plugin types!

[View](/telegraf/v1/input-plugins/snmp/)

### SNMP Trap

Plugin ID: `inputs.snmp_trap`
Telegraf v1.13.0+

This service plugin listens for [SNMP](https://datatracker.ietf.org/doc/html/rfc1157) notifications like traps and inform requests. Notifications are received on plain UDP with a configurable port.

The path setting is shared between all instances of all SNMP plugin types!

[View](/telegraf/v1/input-plugins/snmp_trap/)

### Socket Listener

Plugin ID: `inputs.socket_listener`
Telegraf v1.3.0+

This service plugin listens for messages on sockets (TCP, UDP, Unix or Unixgram) and parses the packets received in one of the supported [data formats](/telegraf/v1/data_formats/input).

[View](/telegraf/v1/input-plugins/socket_listener/)

### Socket Statistics

Plugin ID: `inputs.socketstat`
Telegraf v1.22.0+

This plugin gathers metrics for established network connections using [iproute2](https://github.com/iproute2/iproute2)’s `ss` command. The `ss` command does not require specific privileges.

This plugin produces high cardinality data, which when not controlled for will cause high load on your database. Please make sure to [filter](/telegraf/v1/configuration/#metric-filtering) the produced metrics or configure your database to avoid cardinality issues!

[View](/telegraf/v1/input-plugins/socketstat/)

### Apache Solr

Plugin ID: `inputs.solr`
Telegraf v1.5.0+

This plugin collects statistics from [Solr](http://lucene.apache.org/solr/) instances using the [MBean Request Handler](https://cwiki.apache.org/confluence/display/solr/MBean+Request+Handler). For additional details on performance statistics check the [performance statistics reference](https://cwiki.apache.org/confluence/display/solr/Performance+Statistics+Reference).

This plugin requires Apache Solr v3.5+.

[View](/telegraf/v1/input-plugins/solr/)

### SQL

Plugin ID: `inputs.sql`
Telegraf v1.19.0+

This plugin reads metrics from performing [SQL](https://www.iso.org/standard/76583.html) queries against a SQL server. Different server types are supported and their settings might differ (especially the connection parameters). Please check the list of [supported SQL drivers](/docs/SQL_DRIVERS_INPUT.md) for the `driver` name and options for the data-source-name (`dsn`) options.

[View](/telegraf/v1/input-plugins/sql/)

### Microsoft SQL Server

Plugin ID: `inputs.sqlserver`
Telegraf v0.10.1+

This plugin provides metrics for your [SQL Server](https://docs.microsoft.com/en-us/sql/sql-server) instance. Recorded metrics are lightweight and use Dynamic Management Views supplied by SQL Server.

This plugin supports SQL server versions supported by Microsoft (see [lifecycle dates](https://docs.microsoft.com/en-us/sql/sql-server/end-of-support/sql-server-end-of-life-overview?view=sql-server-ver15#lifecycle-dates)), Azure SQL Databases (Single), Azure SQL Managed Instances, Azure SQL Elastic Pools and Azure Arc-enabled SQL Managed Instances.

[View](/telegraf/v1/input-plugins/sqlserver/)

### Stackdriver Google Cloud Monitoring

Plugin ID: `inputs.stackdriver`
Telegraf v1.10.0+

This plugin collects metrics from [Google Cloud Monitoring](https://cloud.google.com/monitoring) (formerly Stackdriver) using the [Cloud Monitoring API v3](https://cloud.google.com/monitoring/api/v3/).

This plugin accesses APIs which are [chargeable](https://cloud.google.com/stackdriver/pricing#stackdriver_monitoring_services), cost might incur.

[View](/telegraf/v1/input-plugins/stackdriver/)

### StatsD

Plugin ID: `inputs.statsd`
Telegraf v0.2.0+

This service plugin gathers metrics from a [Statsd](https://github.com/statsd/statsd) server.

[View](/telegraf/v1/input-plugins/statsd/)

### Supervisor

Plugin ID: `inputs.supervisor`
Telegraf v1.24.0+

This plugin gathers information about processes running under [supervisord](https://supervisord.org/) using the [XML-RPC API](https://supervisord.org/api.html).

This plugin requires supervisor v3.3.2+.

[View](/telegraf/v1/input-plugins/supervisor/)

### Suricata

Plugin ID: `inputs.suricata`
Telegraf v1.13.0+

This service plugin reports internal performance counters of the [Suricata IDS/IPS](https://suricata.io/) engine, such as captured traffic volume, memory usage, uptime, flow counters, and much more. This plugin provides a socket for the Suricata log output to write JSON stats output to, and processes the incoming data to fit Telegraf’s format. It can also report for triggered Suricata IDS/IPS alerts.

[View](/telegraf/v1/input-plugins/suricata/)

### Swap

Plugin ID: `inputs.swap`
Telegraf v1.7.0+

This plugin collects metrics on the operating-system’s swap memory.

[View](/telegraf/v1/input-plugins/swap/)

### Synproxy

Plugin ID: `inputs.synproxy`
Telegraf v1.13.0+

This plugin gathers metrics about the Linux netfilter’s [synproxy](https://wiki.nftables.org/wiki-nftables/index.php/Synproxy) module used for mitigating SYN attacks.

[View](/telegraf/v1/input-plugins/synproxy/)

### Syslog

Plugin ID: `inputs.syslog`
Telegraf v1.7.0+

This service plugin listens for [syslog](https://en.wikipedia.org/wiki/Syslog) messages transmitted over a Unix Domain socket, [UDP](https://tools.ietf.org/html/rfc5426), [TCP](https://tools.ietf.org/html/rfc6587) or [TLS](https://tools.ietf.org/html/rfc5425) with or without the octet counting framing.

Syslog messages should be formatted according to the [syslog protocol](https://tools.ietf.org/html/rfc5424) or the [BSD syslog protocol](https://tools.ietf.org/html/rfc3164).

[View](/telegraf/v1/input-plugins/syslog/)

### System Performance Statistics

Plugin ID: `inputs.sysstat`
Telegraf v0.12.1+

This plugin collects Linux [system performance statistics](https://github.com/sysstat/sysstat) using the `sysstat` package. This plugin uses the `sadc` collector utility and and parses the created binary data file using the `sadf` utility.

This plugin requires the `sysstat` package to be installed on the system and both `sadc` and `sadf` to be executable by Telegraf.

[View](/telegraf/v1/input-plugins/sysstat/)

### System

Plugin ID: `inputs.system`
Telegraf v0.1.6+

This plugin gathers general system statistics like system load, uptime or the number of users logged in. It is similar to the unix `uptime` command.

[View](/telegraf/v1/input-plugins/system/)

### Systemd-Units

Plugin ID: `inputs.systemd_units`
Telegraf v1.13.0+

This plugin gathers the status of systemd-units on Linux, using systemd’s DBus interface.

This plugin requires systemd v230+!

[View](/telegraf/v1/input-plugins/systemd_units/)

### Tacacs

Plugin ID: `inputs.tacacs`
Telegraf v1.28.0+

This plugin collects metrics on [Terminal Access Controller Access Control System](https://datatracker.ietf.org/doc/html/rfc1492) authentication requests like response status and response time from servers such as [Aruba ClearPass](https://www.hpe.com/de/de/aruba-clearpass-policy-manager.html), [FreeRADIUS](https://www.freeradius.org/) or [TACACS+](https://datatracker.ietf.org/doc/html/rfc8907).

The plugin is primarily meant to monitor how long it takes for the server to fully handle an authentication request, including all potential dependent calls (for example to AD servers, or other sources of truth).

[View](/telegraf/v1/input-plugins/tacacs/)

### Tail

Plugin ID: `inputs.tail`
Telegraf v1.1.2+

This service plugin continuously reads a file and parses new data as it arrives similar to the [tail -f command](https://man7.org/linux/man-pages/man1/tail.1.html). The incoming messages are expected to be in one of the supported [data formats](/telegraf/v1/data_formats/input).

[View](/telegraf/v1/input-plugins/tail/)

### Teamspeak

Plugin ID: `inputs.teamspeak`
Telegraf v1.5.0+

This plugin collects statistics of one or more virtual [Teamspeak](https://www.teamspeak.com) servers using the `ServerQuery` interface. Currently this plugin only supports Teamspeak 3 servers.

For querying external Teamspeak server, make sure to add the Telegraf host to the `query_ip_allowlist.txt` file in the Teamspeak Server directory.

[View](/telegraf/v1/input-plugins/teamspeak/)

### Temperature

Plugin ID: `inputs.temp`
Telegraf v1.8.0+

This plugin gathers metrics on system temperatures.

[View](/telegraf/v1/input-plugins/temp/)

### Tengine Web Server

Plugin ID: `inputs.tengine`
Telegraf v1.8.0+

This plugin gathers metrics from the [Tengine Web Server](http://tengine.taobao.org) via the [reqstat](http://tengine.taobao.org/document/http_reqstat.html) module.

[View](/telegraf/v1/input-plugins/tengine/)

### Timex

Plugin ID: `inputs.timex`
Telegraf v1.37.0+

This plugin gathers metrics on system time using the Linux Kernel [adjtimex syscall](https://man7.org/linux/man-pages/man2/adjtimex.2.html).

The call gets the information of the kernel time variables that are controlled by the ntpd, systemd-timesyncd, chrony or other time synchronization services.

[View](/telegraf/v1/input-plugins/timex/)

### Apache Tomcat

Plugin ID: `inputs.tomcat`
Telegraf v1.4.0+

This plugin collects statistics from a [Tomcat server](https://tomcat.apache.org) instance using the manager status page. See the [Tomcat documentation](https://tomcat.apache.org/tomcat-9.0-doc/manager-howto.html#Server_Status) for details of these statistics.

[View](/telegraf/v1/input-plugins/tomcat/)

### Trig

Plugin ID: `inputs.trig`
Telegraf v0.3.0+

This plugin is for demonstration purposes and inserts sine and cosine values as metrics.

[View](/telegraf/v1/input-plugins/trig/)

### Turbostat

Plugin ID: `inputs.turbostat`
Telegraf v1.36.0+

This service plugin monitors system performance using the [turbostat](https://github.com/torvalds/linux/tree/master/tools/power/x86/turbostat) command.

This plugin requires the `turbostat` executable to be installed on the system.

[View](/telegraf/v1/input-plugins/turbostat/)

### Twemproxy

Plugin ID: `inputs.twemproxy`
Telegraf v0.3.0+

This plugin gathers statistics from [Twemproxy](https://github.com/twitter/twemproxy) servers.

[View](/telegraf/v1/input-plugins/twemproxy/)

### Unbound

Plugin ID: `inputs.unbound`
Telegraf v1.5.0+

This plugin gathers stats from an [Unbound](https://www.unbound.net) DNS resolver.

[View](/telegraf/v1/input-plugins/unbound/)

### UPSD

Plugin ID: `inputs.upsd`
Telegraf v1.24.0+

This plugin reads data of one or more Uninterruptible Power Supplies from a [Network UPS Tools](https://networkupstools.org/) daemon using its NUT network protocol.

[View](/telegraf/v1/input-plugins/upsd/)

### uWSGI

Plugin ID: `inputs.uwsgi`
Telegraf v1.12.0+

This plugin gathers metrics about [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) using its [Stats Server](https://uwsgi-docs.readthedocs.io/en/latest/StatsServer.html).

[View](/telegraf/v1/input-plugins/uwsgi/)

### Varnish

Plugin ID: `inputs.varnish`
Telegraf v0.13.1+

This plugin gathers statistics from a local [Varnish HTTP Cache](https://varnish-cache.org) instance using the `varnishstat` command.

This plugin requires the `varnishstat` executable to be installed on the system and executable by Telegraf. Furthermore, the plugin requires Varnish v6.0.2+.

[View](/telegraf/v1/input-plugins/varnish/)

### Hashicorp Vault

Plugin ID: `inputs.vault`
Telegraf v1.22.0+

This plugin collects metrics from every [Vault](https://www.hashicorp.com/de/products/vault) agent of a cluster.

This plugin requires Vault v1.8.5+

[View](/telegraf/v1/input-plugins/vault/)

### VMware vSphere

Plugin ID: `inputs.vsphere`
Telegraf v1.8.0+

This plugin gathers metrics from [vSphere](https://www.vmware.com/products/cloud-infrastructure/vsphere) servers of a vCenter including clusters, hosts, resource pools, VMs, datastores and vSAN information.

This plugin requires vSphere v7.0+.

[View](/telegraf/v1/input-plugins/vsphere/)

### Webhooks

Plugin ID: `inputs.webhooks`
Telegraf v1.0.0+

This service plugin provides an HTTP server and register for multiple webhook listeners.

[View](/telegraf/v1/input-plugins/webhooks/)

### WHOIS

Plugin ID: `inputs.whois`
Telegraf v1.35.0+

This plugin queries [WHOIS information](https://datatracker.ietf.org/doc/html/rfc3912) for configured domains and provides metrics such as expiration timestamps, registrar details and domain status from e.g. [IANA](https://www.iana.org/whois) or [ICANN](https://lookup.icann.org/) servers.

[View](/telegraf/v1/input-plugins/whois/)

### Windows Eventlog

Plugin ID: `inputs.win_eventlog`
Telegraf v1.16.0+

This plugin gathers metrics from the [Windows event log](https://learn.microsoft.com/en-us/shows/inside/event-viewer) on Windows Vista and higher.

Some event channels, like the System Log, require Administrator permissions to subscribe.

[View](/telegraf/v1/input-plugins/win_eventlog/)

### Windows Performance Counters

Plugin ID: `inputs.win_perf_counters`
Telegraf v0.10.2+

This plugin produces metrics from the collected [Windows Performance Counters](https://learn.microsoft.com/en-us/windows/win32/perfctrs/about-performance-counters).

[View](/telegraf/v1/input-plugins/win_perf_counters/)

### Windows Services

Plugin ID: `inputs.win_services`
Telegraf v1.4.0+

This plugin collects information about the status of Windows services.

Monitoring some services may require running Telegraf with administrator privileges.

[View](/telegraf/v1/input-plugins/win_services/)

### Windows Management Instrumentation

Plugin ID: `inputs.win_wmi`
Telegraf v1.26.0+

This plugin queries information or invokes methods using [Windows Management Instrumentation](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page) classes. This allows capturing and filtering virtually any configuration or metric value exposed through WMI.

The telegraf service user must have at least permission to [read](https://learn.microsoft.com/en-us/windows/win32/wmisdk/access-to-wmi-namespaces) the WMI namespace being queried.

[View](/telegraf/v1/input-plugins/win_wmi/)

### Wireguard

Plugin ID: `inputs.wireguard`
Telegraf v1.14.0+

This plugin collects statistics on a local [Wireguard](https://www.wireguard.com/) server using the [`wgctrl` library](https://github.com/WireGuard/wgctrl-go). The plugin reports gauge metrics for Wireguard interface device(s) and its peers.

[View](/telegraf/v1/input-plugins/wireguard/)

### Wireless

Plugin ID: `inputs.wireless`
Telegraf v1.9.0+

This plugin gathers metrics about wireless link quality by reading the `/proc/net/wireless` file.

[View](/telegraf/v1/input-plugins/wireless/)

### x509 Certificate

Plugin ID: `inputs.x509_cert`
Telegraf v1.8.0+

This plugin provides information about [X.509](https://en.wikipedia.org/wiki/X.509) certificates accessible e.g. via local file, tcp, udp, https or smtp protocols and the Windows Certificate Store.

When using a UDP address as a certificate source, the server must support [DTLS](https://en.wikipedia.org/wiki/Datagram_Transport_Layer_Security).

[View](/telegraf/v1/input-plugins/x509_cert/)

### Dell EMC XtremIO

Plugin ID: `inputs.xtremio`
Telegraf v1.22.0+

This plugin gathers metrics from a [Dell EMC XtremIO Storage Array](https://www.delltechnologies.com/asset/en-sa/products/storage/industry-market/h16444-introduction-xtremio-x2-storage-array-wp.pdf) instance using the [v3 Rest API](https://dl.dell.com/content/docu96624_xtremio-storage-array-x1-and-x2-cluster-types-with-xms-6-3-0-to-6-3-3-and-xios-4-0-15-to-4-0-31-and-6-0-0-to-6-3-3-restful-api-3-x-guide.pdf).

[View](/telegraf/v1/input-plugins/xtremio/)

### ZFS

Plugin ID: `inputs.zfs`
Telegraf v0.2.1+

This plugin gathers metrics from [ZFS](https://en.wikipedia.org/wiki/ZFS) filesystems using `/proc/spl/kstat/zfs` on Linux and `sysctl`, `zfs` and `zpool` on FreeBSD.

[View](/telegraf/v1/input-plugins/zfs/)

### Zipkin

Plugin ID: `inputs.zipkin`
Telegraf v1.4.0+

This service plugin implements the [Zipkin](https://zipkin.io/) HTTP server to gather trace and timing data needed to troubleshoot latency problems in microservice architectures.

This plugin produces high cardinality data, which when not controlled for will cause high load on your database. Please make sure to [filter](/telegraf/v1/configuration/#metric-filtering) the produced metrics or configure your database to avoid cardinality issues!

[View](/telegraf/v1/input-plugins/zipkin/)

### Apache Zookeeper

Plugin ID: `inputs.zookeeper`
Telegraf v0.2.0+

This plugin collects variables from [Zookeeper](https://zookeeper.apache.org) instances using the [`mntr` command](https://zookeeper.apache.org/doc/current/zookeeperAdmin.html#sc_zkCommands).

If the Prometheus Metric provider is enabled in Zookeeper use the [prometheus plugin](/telegraf/v1/plugins/#input-prometheus) instead with `http://<ip>:7000/metrics`.

[View](/telegraf/v1/input-plugins/zookeeper/)

---

## Telegraf glossary

## agent

An agent is the core part of Telegraf that gathers metrics from the declared input plugins and sends metrics to the declared output plugins, based on the plugins enabled by the given configuration.

Related entries: [input plugin](/telegraf/v1/glossary/#input-plugin), [output plugin](/telegraf/v1/glossary/#output-plugin)

## aggregator plugin

Aggregator plugins receive raw metrics from input plugins and create aggregate metrics from them. The aggregate metrics are then passed to the configured output plugins.

Related entries: [input plugin](/telegraf/v1/glossary/#input-plugin), [output plugin](/telegraf/v1/glossary/#output-plugin), [processor plugin](/telegraf/v1/glossary/#processor-plugin)

## batch size

The Telegraf agent sends metrics to output plugins in batches, not individually. The batch size controls the size of each write batch that Telegraf sends to the output plugins.

Related entries: [output plugin](/telegraf/v1/glossary/#output-plugin)

## collection interval

The default global interval for collecting data from each input plugin. The collection interval can be overridden by each individual input plugin’s configuration.

Related entries: [input plugin](/telegraf/v1/glossary/#input-plugin)

## collection jitter

Collection jitter is used to prevent every input plugin from collecting metrics simultaneously, which can have a measurable effect on the system. Each collection interval, every input plugin will sleep for a random time between zero and the collection jitter before collecting the metrics.

Related entries: [collection interval](/telegraf/v1/glossary/#collection-interval), [input plugin](/telegraf/v1/glossary/#input-plugin)

## external plugin

Programs built outside of Telegraf that run through the `execd` plugin. Provides flexibility to add functionality that doesn’t exist in internal Telegraf plugins.

## flush interval

The global interval for flushing data from each output plugin to its destination. This value should not be set lower than the collection interval.

Related entries: [collection interval](/telegraf/v1/glossary/#collection-interval), [flush jitter](/telegraf/v1/glossary/#flush-jitter), [output plugin](/telegraf/v1/glossary/#output-plugin)

## flush jitter

Flush jitter is used to prevent every output plugin from sending writes simultaneously, which can overwhelm some data sinks. Each flush interval, every output plugin will sleep for a random time between zero and the flush jitter before emitting metrics. This helps smooth out write spikes when running a large number of Telegraf instances.

Related entries: [flush interval](/telegraf/v1/glossary/#flush-interval), [output plugin](/telegraf/v1/glossary/#output-plugin)

## input plugin

Input plugins actively gather metrics and deliver them to the core agent, where aggregator, processor, and output plugins can operate on the metrics. In order to activate an input plugin, it needs to be enabled and configured in Telegraf’s configuration file.

Related entries: [aggregator plugin](/telegraf/v1/glossary/#aggregator-plugin), [collection interval](/telegraf/v1/glossary/#collection-interval), [output plugin](/telegraf/v1/glossary/#output-plugin), [processor plugin](/telegraf/v1/glossary/#processor-plugin)

## metric buffer

The metric buffer caches individual metrics when writes are failing for an output plugin. Telegraf will attempt to flush the buffer upon a successful write to the output. The oldest metrics are dropped first when this buffer fills.

Related entries: [output plugin](/telegraf/v1/glossary/#output-plugin)

## output plugin

Output plugins deliver metrics to their configured destination. In order to activate an output plugin, it needs to be enabled and configured in Telegraf’s configuration file.

Related entries: [aggregator plugin](/telegraf/v1/glossary/#aggregator-plugin), [flush interval](/telegraf/v1/glossary/#flush-interval), [input plugin](/telegraf/v1/glossary/#input-plugin), [processor plugin](/telegraf/v1/glossary/#processor-plugin)

## precision

The precision configuration setting determines how much timestamp precision is retained in the points received from input plugins. All incoming timestamps are truncated to the given precision. Telegraf then pads the truncated timestamps with zeros to create a nanosecond timestamp; output plugins will emit timestamps in nanoseconds. Valid precisions are `ns`, `us` or `µs`, `ms`, and `s`.

For example, if the precision is set to `ms`, the nanosecond epoch timestamp `1480000000123456789` would be truncated to `1480000000123` in millisecond precision and then padded with zeroes to make a new, less precise nanosecond timestamp of `1480000000123000000`. Output plugins do not alter the timestamp further. The precision setting is ignored for service input plugins.

Related entries: [aggregator plugin](/telegraf/v1/glossary/#aggregator-plugin), [input plugin](/telegraf/v1/glossary/#input-plugin), [output plugin](/telegraf/v1/glossary/#output-plugin), [processor plugin](/telegraf/v1/glossary/#processor-plugin), [service input plugin](/telegraf/v1/glossary/#service-input-plugin)

## processor plugin

Processor plugins transform, decorate, and/or filter metrics collected by input plugins, passing the transformed metrics to the output plugins.

Related entries: [aggregator plugin](/telegraf/v1/glossary/#aggregator-plugin), [input plugin](/telegraf/v1/glossary/#input-plugin), [output plugin](/telegraf/v1/glossary/#output-plugin)

## service input plugin

Service input plugins are input plugins that run in a passive collection mode while the Telegraf agent is running. They listen on a socket for known protocol inputs, or apply their own logic to ingested metrics before delivering them to the Telegraf agent.

Related entries: [aggregator plugin](/telegraf/v1/glossary/#aggregator-plugin), [input plugin](/telegraf/v1/glossary/#input-plugin), [output plugin](/telegraf/v1/glossary/#output-plugin), [processor plugin](/telegraf/v1/glossary/#processor-plugin)

---

## Get started

After you’ve [downloaded and installed Telegraf](/telegraf/v1/install/), you’re ready to begin collecting and sending data. To collect and send data, do the following:

1. [Configure Telegraf](#configure-telegraf)
2. [Start Telegraf](#start-telegraf)
3. Use [plugins available in Telegraf](/telegraf/v1/plugins/) to gather, transform, and output data.

## Configure Telegraf

Define which plugins Telegraf will use in the configuration file. Each configuration file needs at least one enabled [input plugin](/telegraf/v1/plugins/inputs/) (where the metrics come from) and at least one enabled [output plugin](/telegraf/v1/plugins/outputs/) (where the metrics go).

The following example generates a sample configuration file with all available plugins, then uses `filter` flags to enable specific plugins.

For details on `filter` and other flags, see [Telegraf commands and flags](/telegraf/v1/commands/).

1. Run the following command to create a configuration file:

    ```bash
    telegraf --sample-config > telegraf.conf
    ```

2. Locate the configuration file. The location varies depending on your system:

    - macOS [Homebrew](http://brew.sh/): `/usr/local/etc/telegraf.conf`
    - Linux debian and RPM packages: `/etc/telegraf/telegraf.conf`
    - Standalone Binary: see the next section for how to create a configuration file

    > **Note:** You can also specify a remote URL endpoint to pull a configuration file from. See [Configuration file locations](/telegraf/v1/configuration/#configuration-file-locations).

3. Edit the configuration file using `vim` or a text editor. Because this example uses [InfluxDB V2 output plugin](https://github.com/influxdata/telegraf/blob/release-1.21/plugins/outputs/influxdb_v2/README.md), we need to add the InfluxDB URL, authentication token, organization, and bucket details to this section of the configuration file.

> **Note:** For more configuration file options, see [Configuration options](/telegraf/v1/configuration/).

4. For this example, specify two inputs (`cpu` and `mem`) with the `--input-filter` flag. Specify InfluxDB as the output with the `--output-filter` flag.

```bash
telegraf --sample-config --input-filter cpu:mem --output-filter influxdb_v2 > telegraf.conf
```

The resulting configuration will collect CPU and memory data and sends it to InfluxDB V2.

For an overview of how to configure a plugin, watch the following video:

## Set environment variables

Add environment variables anywhere in the configuration file by prepending them with `$`. For strings, variables must be in quotes (for example, `"$STR_VAR"`). For numbers and Booleans, variables must be unquoted (for example, `$INT_VAR`, `$BOOL_VAR`).

You can also set environment variables using the Linux `export` command: `export password=mypassword`

> **Note:** We recommend using environment variables for sensitive information.

### Example: Telegraf environment variables

In the Telegraf environment variables file (`/etc/default/telegraf`):

```sh
USER="alice"
INFLUX_URL="http://localhost:8086"
INFLUX_SKIP_DATABASE_CREATION="true"
INFLUX_PASSWORD="monkey123"
```

In the Telegraf configuration file (`/etc/telegraf.conf`):

```sh
[global_tags]
  user = "${USER}"

[[inputs.mem]]

[[outputs.influxdb]]
  urls = ["${INFLUX_URL}"]
  skip_database_creation = ${INFLUX_SKIP_DATABASE_CREATION}
  password = "${INFLUX_PASSWORD}"
```

The environment variables above add the following configuration settings to Telegraf:

```sh
[global_tags]
  user = "alice"

[[outputs.influxdb]]
  urls = "http://localhost:8086"
  skip_database_creation = true
  password = "monkey123"
```

## Start Telegraf

Next, you need to start the Telegraf service and direct it to your configuration file:

### macOS [Homebrew](http://brew.sh/)

```bash
telegraf --config telegraf.conf
```

### Linux (systemd installations)

```bash
systemctl start telegraf
```

---

## Telegraf data formats

This section covers the input data formats and output data formats used in the Telegraf plugin-driven server agent component of the InfluxData time series platform.

## [Input data formats](/telegraf/v1/data_formats/input/)

Telegraf supports parsing input data formats into Telegraf metrics.

## [Output data formats](/telegraf/v1/data_formats/output/)

Telegraf serializes metrics into output data formats.

---

## Contribute to Telegraf

There are many ways to contribute to InfluxData open source products. Whether you want to report a bug, write a plugin, or answer support questions, the following sections will guide you through the process.

- [Open GitHub issues](#open-github-issues)
    - [File bug reports](#file-bug-reports)
    - [Open feature requests](#open-feature-requests)
    - [Ask or answer support questions](#ask-or-answer-support-questions)
- [Contribute code](#contribute-code)
    - [Create a pull request](#create-a-pull-request)
    - [Contribute an external plugin](#contribute-an-external-plugin)
- [Report security vulnerabilities](#report-security-vulnerabilities)

## Open GitHub issues

### File bug reports

1. Search [Telegraf GitHub issues](https://github.com/influxdata/telegraf/issues) for related issues that are open or have been fixed.
2. If an issue does not already exist, [create a new bug report issue](https://github.com/influxdata/telegraf/issues/new?assignees=&labels=bug&projects=&template=BUG_REPORT.yml).
3. Include all the requested details.

Do not open general support requests as GitHub issues. Support-related questions should be directed to the [InfluxDB Community Slack](https://influxdata.com/slack) or [InfluxData Community forum](https://community.influxdata.com/).

### Open feature requests

Feature requests help to prioritize work. To submit a feature request:

1. Search [Telegraf GitHub issues](https://github.com/influxdata/telegraf/issues) for issues related your feature request. Use the **feature request** label to filter issues by feature requests.
2. If an issue related to your feature request already exists, indicate your support for that feature by using the [**thumbs up** reaction](https://github.blog/2016-03-10-add-reactions-to-pull-requests-issues-and-comments/) and add a comment explaining your use case for the feature.
3. If a feature request does not already exist, [create a new feature request issue](https://github.com/influxdata/telegraf/issues/new?assignees=&labels=feature+request&projects=&template=FEATURE_REQUEST.yml). Include the following with your feature request
4. Include all the requested details.

### Ask or answer support questions

Post support questions to [InfluxDB Community Slack](https://influxdata.com/slack) or [InfluxData Community forum](https://community.influxdata.com/).

## Contribute code

### Create a pull request

1. [Sign the InfluxData CLA](https://www.influxdata.com/legal/cla/).

2. Open a [new issue](https://github.com/influxdata/telegraf/issues/new/choose) to discuss the changes you would like to make. This is not strictly required, but it may help reduce the amount of rework you need to do later.

3. Make changes or write plugins using the following plugin guidelines:

    - [Input Plugins](https://github.com/influxdata/telegraf/blob/master/docs/INPUTS.md)
    - [Processor Plugins](https://github.com/influxdata/telegraf/blob/master/docs/PROCESSORS.md)
    - [Aggregator Plugins](https://github.com/influxdata/telegraf/blob/master/docs/AGGREGATORS.md)
    - [Output Plugins](https://github.com/influxdata/telegraf/blob/master/docs/OUTPUTS.md)
4. Include unit tests and documentation for your change.

5. Open a new [pull request](https://github.com/influxdata/telegraf/compare). The pull request title needs to follow the [conventional commit format](https://www.conventionalcommits.org/en/v1.0.0/#summary).

If you have a pull request with only one commit, the commit message must follow the [conventional commit format](https://www.conventionalcommits.org/en/v1.0.0/#summary), otherwise the **Semantic Pull Request** check will fail. For single-commit pull requests, GitHub uses the commit message as the default pull request title.

### Contribute an external plugin

Input, output, and processor plugins written for Telegraf can be run as externally-compiled plugins through the [execd input](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/execd), [execd output](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/execd), and [execd processor](https://github.com/influxdata/telegraf/tree/master/plugins/processors/execd) plugins without having to change the plugin code.

For more information, see:

- [Execd Go Shim](/telegraf/v1/configure_plugins/external_plugins/shim/): Use the Go `execd` shim to compile your plugin as a separate app and run it with the respective `execd` plugin.
- [Write an external plugin](/telegraf/v1/configure_plugins/external_plugins/write_external_plugin/): Build and set up external plugins to run with `execd`.

## Report security vulnerabilities

InfluxData takes security and our users’ trust very seriously. If you believe you have found a security issue in any of our open source projects, please responsibly disclose it by contacting [security@influxdata.com](mailto:security@influxdata.com). For more information about reporting security vulnerabilities, including our GPG key, see [How to report security vulnerabilities](https://www.influxdata.com/how-to-report-security-vulnerabilities/).

---

## Configure plugins

Telegraf is a server-based agent for collecting and sending metrics and events from databases, systems, and IoT sensors.

## [Collect data with input plugins](/telegraf/v1/configure_plugins/input_plugins/)

Collect data from a variety of sources with Telegraf input plugins.

## [Integrate with external plugins](/telegraf/v1/configure_plugins/external_plugins/)

External plugins are external programs that are built outside of Telegraf that can run through an `execd` plugin.

## [Telegraf template patterns](/telegraf/v1/configure_plugins/template-patterns/)

Template patterns describe how a dot-delimited string should be mapped to and from Telegraf metrics.

## [Transform data with aggregator and processor plugins](/telegraf/v1/configure_plugins/aggregator_processor/)

Aggregator and processor plugins aggregate and process metrics.

## [Troubleshoot Telegraf](/telegraf/v1/configure_plugins/troubleshoot/)

Resolve common issues with Telegraf.

## [Write data with output plugins](/telegraf/v1/configure_plugins/output_plugins/)

Output plugins define where Telegraf delivers the collected metrics.

---

## Configuration options

Telegraf uses a configuration file to define what plugins to enable and what settings to use when Telegraf starts. Each Telegraf plugin has its own set of configuration options. Telegraf also provides global options for configuring specific Telegraf settings.

See [Get started](/telegraf/v1/get_started/) to quickly get up and running with Telegraf.

## Generate a configuration file

The `telegraf config` command lets you generate a configuration file using Telegraf’s list of plugins.

- [Create a configuration with default input and output plugins](#create-a-configuration-with-default-input-and-output-plugins)
- [Create a configuration with specific input and output plugins](#create-a-configuration-with-specific-input-and-output-plugins)
- [Windows PowerShell v5 encoding](#windows-powershell-v5-encoding)

### Create a configuration with default input and output plugins

To generate a configuration file with default input and output plugins enabled, enter the following command in your terminal:

<!-- Tabbed content: Select one of the following options -->

**Linux and macOS:**

```bash
telegraf config > telegraf.conf
```

**Windows:**

```powershell
.\telegraf.exe config > telegraf.conf
```

<!-- End tabbed content -->

The generated file contains settings for all available plugins–some are enabled and the rest are commented out.

### Create a configuration file with specific input and output plugins

To generate a configuration file that contains settings for only specific plugins, use the `--input-filter` and `--output-filter` options to specify [input plugins](/telegraf/v1/configure_plugins/input_plugins/) and [output plugins](/telegraf/v1/configure_plugins/output_plugins/). Use a colon (`:`) to separate plugin names.

#### Syntax

<!-- Tabbed content: Select one of the following options -->

**Linux and macOS:**

```bash
telegraf \
--input-filter <INPUT_PLUGIN_NAME>[:<INPUT_PLUGIN_NAME>] \
--output-filter <OUTPUT_PLUGIN_NAME>[:<OUTPUT_PLUGIN_NAME>] \
config > telegraf.conf
```

**Windows:**

```powershell
.\telegraf.exe `
--input-filter <INPUT_PLUGIN_NAME>[:<INPUT_PLUGIN_NAME>] `
--output-filter <OUTPUT_PLUGIN_NAME>[:<OUTPUT_PLUGIN_NAME>] `
config > telegraf.conf
```

<!-- End tabbed content -->

#### Example

The following example shows how to include configuration sections for the [`inputs.cpu`](/telegraf/v1/plugins/#input-cpu), [`inputs.http_listener_v2`](/telegraf/v1/plugins/#input-http_listener_v2), [`outputs.influxdb_v2`](/telegraf/v1/plugins/#output-influxdb_v2), and [`outputs.file`](/telegraf/v1/plugins/#output-file) plugins:

<!-- Tabbed content: Select one of the following options -->

**Linux and macOS:**

```bash
telegraf \
--input-filter cpu:http_listener_v2 \
--output-filter influxdb_v2:file \
config > telegraf.conf
```

**Windows:**

```powershell
.\telegraf.exe `
--input-filter cpu:http_listener_v2 `
--output-filter influxdb_v2:file `
config > telegraf.conf
```

<!-- End tabbed content -->

For more advanced configuration details, see the [configuration documentation](/telegraf/v1/administration/configuration/).

### Windows PowerShell v5 encoding

In PowerShell 5, the default encoding is UTF-16LE and not UTF-8. Telegraf expects a valid UTF-8 file. This is not an issue with PowerShell 6 or newer, as well as the Command Prompt or with using the Git Bash shell.

When using PowerShell 5 or earlier, specify the output encoding when generating a full configuration file:

```powershell
telegraf.exe config | Out-File -Encoding utf8 telegraf.conf
```

This will generate a UTF-8 encoded file with a byte-order mark (BOM). However, Telegraf correctly handles the leading BOM.

## Configuration file locations

When starting Telegraf, use the `--config` flag to specify the configuration file location:

- Filename and path, for example: `--config /etc/default/telegraf`
- Remote URL endpoint, for example: `--config "http://remote-URL-endpoint"`

Use the `--config-directory` flag to include files ending with `.conf` in the specified directory in the Telegraf configuration.

On most systems, the default locations are `/etc/telegraf/telegraf.conf` for the main configuration file and `/etc/telegraf/telegraf.d` (on Windows, `C:\"Program Files"\Telegraf\telegraf.d`) for the directory of configuration files.

Telegraf processes each configuration file separately, and the effective configuration is the union of all the files. If any file isn’t a valid configuration, Telegraf returns an error.

#### Telegraf doesn’t support partial configurations

Telegraf doesn’t concatenate configuration files before processing them. Each configuration file that you provide must be a valid configuration.

If you want to use separate files to manage a configuration, you can use your own custom code to concatenate and pre-process the files, and then provide the complete configuration to Telegraf–for example:

1. Configure plugin sections and assign partial configs a file extension different from `.conf` to prevent Telegraf loading them–for example:

    ```toml
    # main.opcua: Main configuration file
    ...
    [[inputs.opcua_listener]]
      name = "PluginSection"
      endpoint = "opc.tcp://10.0.0.53:4840"
    ...
    ```

    ```toml
    # group_1.opcua
      [[inputs.opcua_listener.group]]
      name = "SubSection1"
    ...
    ```

    ```toml
    # group_2.opcua
      [[inputs.opcua_listener.group]]
      name = "SubSection2"
    ...
    ```

2. Before you start Telegraf, run your custom script to concatenate `main.opcua`, `group_1.opcua`, `group_2.opcua` into a valid `telegraf.conf`.

3. Start Telegraf with the complete, valid `telegraf.conf` configuration.

## Set environment variables

Use environment variables anywhere in the configuration file by enclosing them in `${}`. For strings, variables must be in quotes (for example, `"test_${STR_VAR}"`). For numbers and booleans, variables must be unquoted (for example, `${INT_VAR}`, `${BOOL_VAR}`).

When using double quotes, escape any backslashes (for example: `"C:\\Program Files"`) or other special characters. If using an environment variable with a single backslash, enclose the variable in single quotes to signify a string literal (for example: `'C:\Program Files'`).

Telegraf also supports Shell parameter expansion for environment variables which allows the following:

- `${VARIABLE:-default}`: evaluates to `default` if `VARIABLE` is unset or empty in the environment.
- `${VARIABLE-default}`: evaluates to `default` only if `VARIABLE` is unset in the environment. Similarly, the following syntax allows you to specify mandatory variables:
- `${VARIABLE:?err}`: exits with an error message containing `err` if `VARIABLE` is unset or empty in the environment.
- `${VARIABLE?err}`: exits with an error message containing `err` if `VARIABLE` is unset in the environment.

When using the `.deb` or `.rpm` packages, you can define environment variables in the `/etc/default/telegraf` file.

You can also set environment variables using the Linux `export` command:

```bash
export password=mypassword
```

> **Note:** Use a secret store or environment variables to store sensitive credentials.

### Example: Telegraf environment variables

Set environment variables in the Telegraf environment variables file (`/etc/default/telegraf`).

#### For InfluxDB 1.x:

```sh
USER="alice"
INFLUX_URL="http://localhost:8086"
INFLUX_SKIP_DATABASE_CREATION="true"
INFLUX_PASSWORD="passw0rd123"
```

#### For InfluxDB OSS v2:

```sh
INFLUX_HOST="http://localhost:8086"
INFLUX_TOKEN="replace_with_your_token"
INFLUX_ORG="your_username"
INFLUX_BUCKET="replace_with_your_bucket_name"
```

#### For InfluxDB Cloud Serverless:

```sh
# For AWS West (Oregon)
INFLUX_HOST="https://us-west-2-1.aws.cloud2.influxdata.com"
# Other Cloud URLs at https://docs.influxdata.com/influxdb/cloud/reference/regions/
INFLUX_TOKEN="replace_with_your_token"
INFLUX_ORG="yourname@yourcompany.com"
INFLUX_BUCKET="replace_with_your_bucket_name"
```

In the Telegraf configuration file (`/etc/telegraf.conf`), reference the variables–for example:

```toml
[global_tags]
  user = "${USER}"

[[inputs.mem]]

# For InfluxDB 1.x:
[[outputs.influxdb]]
  urls = ["${INFLUX_URL}"]
  skip_database_creation = ${INFLUX_SKIP_DATABASE_CREATION}
  password = "${INFLUX_PASSWORD}"

# For InfluxDB OSS 2:
[[outputs.influxdb_v2]]
  urls = ["${INFLUX_HOST}"]
  token = "${INFLUX_TOKEN}"
  organization = "${INFLUX_ORG}"
  bucket = "${INFLUX_BUCKET}"

# For InfluxDB Cloud:
[[outputs.influxdb_v2]]
  urls = ["${INFLUX_HOST}"]
  token = "${INFLUX_TOKEN}"
  organization = "${INFLUX_ORG}"
  bucket = "${INFLUX_BUCKET}"
```

When Telegraf runs, the effective configuration is the following:

```toml
[global_tags]
  user = "alice"

# For InfluxDB 1.x:
[[outputs.influxdb]]
  urls = ["http://localhost:8086"]
  skip_database_creation = true
  password = "passw0rd123"

# For InfluxDB OSS 2:
[[outputs.influxdb_v2]]
  urls = ["http://localhost:8086"]
  token = "replace_with_your_token"
  organization = "your_username"
  bucket = "replace_with_your_bucket_name"

# For InfluxDB Cloud:
[[outputs.influxdb_v2]]
  urls = ["https://us-west-2-1.aws.cloud2.influxdata.com"]
  token = "replace_with_your_token"
  organization = "yourname@yourcompany.com"
  bucket = "replace_with_your_bucket_name"
```

## Secret stores

Telegraf also supports secret stores for providing credentials or similar. Configure one or more secret store plugins and then reference the secret in your plugin configurations.

Reference secrets using the following syntax:

```txt
@{<secret_store_id>:<secret_name>}
```

- `secret_store_id`: the unique ID you define for your secret store plugin.
- `secret_name`: the name of the secret to use.

Both and `secret_store_id` and `secret_name` only support alphanumeric characters and underscores.

### Example: Use secret stores

This example illustrates the use of secret stores in plugins:

```toml
[global_tags]
  user = "alice"

[[secretstores.os]]
  id = "local_secrets"

[[secretstores.jose]]
  id = "cloud_secrets"
  path = "/etc/telegraf/secrets"
  # Optional reference to another secret store to unlock this one.
  password = "@{local_secrets:cloud_store_passwd}"

[[inputs.http]]
  urls = ["http://server.company.org/metrics"]
  username = "@{local_secrets:company_server_http_metric_user}"
  password = "@{local_secrets:company_server_http_metric_pass}"

[[outputs.influxdb_v2]]
  urls = ["https://us-west-2-1.aws.cloud2.influxdata.com"]
  token = "@{cloud_secrets:influxdb_token}"
  organization = "yourname@yourcompany.com"
  bucket = "replace_with_your_bucket_name"
```

### Notes on secret stores

Not all plugins support secrets. When using plugins that support secrets, Telegraf locks the memory pages containing the secrets. Therefore, the locked memory limit has to be set to a suitable value. Telegraf will check the limit and the number of used secrets at startup and will warn if your limit is too low. In this case, please increase the limit via `ulimit -l`.

If you are running Telegraf in a jail you might need to allow locked pages in that jail by setting `allow.mlock = 1;` in your config.

## Global tags

Global tags can be specified in the `[global_tags]` section of the configuration file in `key="value"` format. Telegraf applies the global tags to all metrics gathered on this host.

## Agent configuration

The `[agent]` section contains the following configuration options:

- **interval**: Default data collection interval for all inputs.
- **round\_interval**: Rounds collection interval to `interval`. For example, if `interval` is set to `10s`, then the agent collects on :00, :10, :20, etc.
- **metric\_batch\_size**: Telegraf sends metrics to outputs in batches of at most `metric_batch_size` metrics. This controls the size of writes that Telegraf sends to output plugins.
- **metric\_buffer\_limit**: Maximum number of unwritten metrics per output. Increasing this value allows for longer periods of output downtime without dropping metrics at the cost of higher maximum memory usage. The oldest metrics are overwritten in favor of new ones when the buffer fills up.
- **collection\_jitter**: Jitter the collection by a random interval. Each plugin sleeps for a random time within the defined jitter before collecting. Use this to avoid many plugins querying things like sysfs at the same time, which can have a measurable effect on the system.
- **collection\_offset**: Shift the collection by the given interval. Use this to avoid many plugins querying constraint devices at the same time by manually scheduling them in time.
- **flush\_interval**: Default flushing interval for all outputs. Maximum `flush_interval` is `flush_interval` + `flush_jitter`.
- **flush\_jitter**: Default flush jitter for all outputs. This jitters the flush interval by a random amount. This is primarily to avoid large write spikes for users running a large number of Telegraf instances. For example, a jitter of `5s` and an interval of `10s` means flushes happen every 10-15 seconds.
- **precision**: Round collected metrics to the precision specified as an interval. Precision is *not* used for service inputs. It is up to each individual service input to set the timestamp at the appropriate precision.
- **debug**: Log at debug level.
- **quiet**: Log only error level messages.
- **logformat**: Log format controls the way messages are logged and can be one of `text`, `structured` or, on Windows, `eventlog`. The output file (if any) is determined by the `logfile` setting.
- **structured\_log\_message\_key**: Message key for structured logs, to override the default of `msg`. Ignored if `logformat` is not `structured`.
- **logfile**: Name of the file to be logged to or stderr if unset or empty. This setting is ignored for the `eventlog` format.
- **logfile\_rotation\_interval**: The logfile rotates after the time interval specified. When set to 0 no time based rotation is performed.
- **logfile\_rotation\_max\_size**: The logfile rotates when it becomes larger than the specified size. When set to 0 no size based rotation is performed.
- **logfile\_rotation\_max\_archives**: Maximum number of rotated archives to keep, any older logs are deleted. If set to -1, no archives are removed.
- **log\_with\_timezone**: Pick a timezone to use when logging or type ’local’ for local time. Example: ‘America/Chicago’. [See this page for options/formats.](https://socketloop.com/tutorials/golang-display-list-of-timezones-with-gmt)
- **hostname**: Override the default hostname, if empty use `os.Hostname()`.
- **omit\_hostname**: If set to true, do no set the “host” tag in the Telegraf agent.
- **snmp\_translator**: Method of translating SNMP objects. Can be “netsnmp” (deprecated) which translates by calling external programs `snmptranslate` and `snmptable`, or “gosmi” which translates using the built-in gosmi library.
- **statefile**: Name of the file to load the states of plugins from and store the states to. If uncommented and not empty, this file is used to save the state of stateful plugins on termination of Telegraf. If the file exists on start, the state in the file is restored for the plugins.
- **always\_include\_local\_tags**: Ensure tags explicitly defined in a plugin *always* pass tag-filtering via `taginclude` or `tagexclude`. This removes the need to specify local tags twice.
- **always\_include\_global\_tags**: Ensure tags explicitly defined in the `global_tags` section will *always* pass tag-filtering via `taginclude` or `tagexclude`. This removes the need to specify those tags twice.
- **skip\_processors\_after\_aggregators**: By default, processors are run a second time after aggregators. Changing this setting to true will skip the second run of processors.
- **buffer\_strategy**: The type of buffer to use for Telegraf output plugins. Supported modes are `memory`, the default and original buffer type, and `disk`, an experimental disk-backed buffer which serializes all metrics to disk as needed to improve data durability and reduce the chance for data loss. This is only supported at the agent level.
- **buffer\_directory**: The directory to use when in `disk` buffer mode. Each output plugin makes another subdirectory in this directory with the output plugin’s ID.

## Input configuration

The following config parameters are available for all inputs:

- **alias**: Name an instance of a plugin.
- **interval**: How often to gather this metric. Normal plugins use a single global interval, but if one particular input should be run less or more often, you can configure that here. `interval` can be increased to reduce data-in rate limits.
- **precision**: Overrides the `precision` setting of the agent. Collected metrics are rounded to the precision specified as an `interval`. When this value is set on a service input (ex: `statsd`), multiple events occurring at the same timestamp may be merged by the output database.
- **collection\_jitter**: Overrides the `collection_jitter` setting of the agent.
    Collection jitter is used to jitter the collection by a random `interval`
- **name\_override**: Override the base name of the measurement. (Default is the name of the input).
- **name\_prefix**: Specifies a prefix to attach to the measurement name.
- **name\_suffix**: Specifies a suffix to attach to the measurement name.
- **tags**: A map of tags to apply to a specific input’s measurements.

## Output configuration

- **alias**: Name an instance of a plugin.
- **flush\_interval**: Maximum time between flushes. Use this setting to override the agent `flush_interval` on a per plugin basis.
- **flush\_jitter**: Amount of time to jitter the flush interval. Use this setting to override the agent `flush_jitter` on a per plugin basis.
- **metric\_batch\_size**: Maximum number of metrics to send at once. Use this setting to override the agent `metric_batch_size` on a per plugin basis.
- **metric\_buffer\_limit**: Maximum number of unsent metrics to buffer. Use this setting to override the agent `metric_buffer_limit` on a per plugin basis.
- **name\_override**: Override the base name of the measurement. (Default is the name of the output).
- **name\_prefix**: Specifies a prefix to attach to the measurement name.
- **name\_suffix**: Specifies a suffix to attach to the measurement name.

### Data formats

Some output plugins support the `data_format` option, which specifies a serializer to convert metrics before writing. Common serializers include `json`, `influx`, `prometheus`, and `csv`.

Output plugins that support serializers may also offer `use_batch_format`, which controls whether the serializer receives metrics individually or as a batch. Batch mode enables more efficient encoding for formats like JSON arrays.

```toml
[[outputs.file]]
  files = ["stdout"]
  data_format = "json"
  use_batch_format = true
```

For available serializers and configuration options, see [output data formats](/telegraf/v1/data_formats/output/).

## Aggregator configuration

The following config parameters are available for all aggregators:

- **alias**: Name an instance of a plugin.
- **period**: The period on which to flush & clear each aggregator. All metrics that are sent with timestamps outside of this period are ignored by the aggregator.
- **delay**: The delay before each aggregator is flushed. This is to control how long for aggregators to wait before receiving metrics from input plugins, in the case that aggregators are flushing and inputs are gathering on the same interval.
- **grace**: The duration the metrics are aggregated by the plugin even though they’re outside the aggregation period. This setting is needed when the agent is expected to receive late metrics and can be rolled into the next aggregation period.
- **drop\_original**: If true, the original metric is dropped by the aggregator and not sent to the output plugins.
- **name\_override**: Override the base name of the measurement. (Default is the name of the input).
- **name\_prefix**: Specifies a prefix to attach to the measurement name.
- **name\_suffix**: Specifies a suffix to attach to the measurement name.
- **tags**: A map of tags to apply to a specific input’s measurements.

For a demonstration of how to configure SNMP, MQTT, and PostGRE SQL plugins to get data into Telegraf, see the following video:

## Processor configuration

The following config parameters are available for all processors:

- **alias**: Name an instance of a plugin.
- **order**: This is the order in which processors are executed. If not specified, then order is random.

The [metric filtering](#metric-filtering) parameters can be used to limit what metrics are handled by the processor. Excluded metrics are passed downstream to the next processor.

## Metric filtering

Filters can be configured per input, output, processor, or aggregator.

- [Filters](#filters)
- [Filtering examples](#filter-examples)

### Filters

Filters fall under two categories:

- [Selectors](#selectors)
- [Modifiers](#modifiers)

#### Selectors

Selector filters include or exclude entire metrics. When a metric is excluded from an input or output plugin, the metric is dropped. If a metric is excluded from a processor or aggregator plugin, it skips the plugin and is sent onwards to the next stage of processing.

- **namepass**: An array of glob pattern strings. Only metrics whose measurement name matches a pattern in this list are emitted. Additionally, custom list of separators can be specified using `namepass_separator`. These separators are excluded from wildcard glob pattern matching.

- **namedrop**: The inverse of `namepass`. If a match is found the metric is discarded. This is tested on metrics after they have passed the `namepass` test. Additionally, custom list of separators can be specified using `namedrop_separator`. These separators are excluded from wildcard glob pattern matching.

- **tagpass**: A table mapping tag keys to arrays of glob pattern strings. Only metrics that contain a tag key in the table and a tag value matching one of its patterns is emitted. This can either use the explicit table syntax (for example: a subsection using a `[...]` header) or inline table syntax (e.g like a JSON table with `{...}`). Please see the below notes on specifying the table.

- **tagdrop**: The inverse of `tagpass`. If a match is found the metric is discarded. This is tested on metrics after they have passed the `tagpass` test.

- **metricpass**: A Common Expression Language (CEL) expression with boolean result where `true` will allow the metric to pass, otherwise the metric is discarded. This filter expression is more general compared to `namepass` and also supports time-based filtering. Further details, such as available functions and expressions, are provided in the CEL language definition as well as in the extension documentation or the CEL language introduction.

    \*As CEL is an *interpreted* language. This type of filtering is much slower than `namepass`, `namedrop`, and others. Consider using the more restrictive filter options where possible in case of high-throughput scenarios.

#### Modifiers

Modifier filters remove tags and fields from a metric. If all fields are removed, the metric is removed and as a result not passed through to the following processors or any output plugin. Tags and fields are modified before a metric is passed to a processor, aggregator, or output plugin. When used with an input plugin the filter applies after the input runs.

- **fieldinclude**: An array of glob pattern strings. Only fields whose field key matches a pattern in this list are emitted.
- **fieldexclude**: The inverse of `fieldinclude`. Fields with a field key matching one of the patterns will be discarded from the metric. This is tested on metrics after they have passed the `fieldinclude` test.
- **taginclude**: An array of glob pattern strings. Only tags with a tag key matching one of the patterns are emitted. In contrast to `tagpass`, which will pass an entire metric based on its tag, `taginclude` removes all non matching tags from the metric. Any tag can be filtered including global tags and the agent `host` tag.
- **tagexclude**: The inverse of `taginclude`. Tags with a tag key matching one of the patterns will be discarded from the metric. Any tag can be filtered including global tags and the agent `host` tag.

#### Include tagpass and tagdrop at the end of your plugin definition

Due to the way TOML is parsed, `tagpass` and `tagdrop` parameters must be defined at the *end* of the plugin definition, otherwise subsequent plugin configuration options are interpreted as part of the tagpass and tagdrop tables.

To learn more about metric filtering, watch the following video:

## Filtering examples

#### Input configuration examples

The following example configuration collects per-cpu data, drops any fields that begin with `time_`, tags measurements with `dc="denver-1"`, and then outputs measurements at a 10 second interval to an InfluxDB database named `telegraf` at the address `192.168.59.103:8086`.

```toml
[global_tags]
  dc = "denver-1"

[agent]
  interval = "10s"

# OUTPUTS
[[outputs.influxdb]]
  url = "http://192.168.59.103:8086" # required.
  database = "telegraf" # required.
  precision = "1s"

# INPUTS
[[inputs.cpu]]
  percpu = true
  totalcpu = false
  # filter all fields beginning with 'time_'
  fielddrop = ["time_*"]
```

#### Input Config: `tagpass` and `tagdrop`

**NOTE** `tagpass` and `tagdrop` parameters must be defined at the *end* of the plugin definition, otherwise subsequent plugin configuration options are interpreted as part of the tagpass and tagdrop tables.

```toml
[[inputs.cpu]]
  percpu = true
  totalcpu = false
  fielddrop = ["cpu_time"]
  # Don't collect CPU data for cpu6 & cpu7
  [inputs.cpu.tagdrop]
    cpu = [ "cpu6", "cpu7" ]

[[inputs.disk]]
  [inputs.disk.tagpass]
    # tagpass conditions are OR, not AND.
    # If the (filesystem is ext4 or xfs) OR (the path is /opt or /home)
    # then the metric passes
    fstype = [ "ext4", "xfs" ]
    # Globs can also be used on the tag values
    path = [ "/opt", "/home*" ]
```

#### Input Config: `fieldpass` and `fielddrop`

```toml
# Drop all metrics for guest & steal CPU usage
[[inputs.cpu]]
  percpu = false
  totalcpu = true
  fielddrop = ["usage_guest", "usage_steal"]

# Only store inode related metrics for disks
[[inputs.disk]]
  fieldpass = ["inodes*"]
```

#### Input Config: `namepass` and `namedrop`

```toml
# Drop all metrics about containers for kubelet
[[inputs.prometheus]]
  urls = ["http://kube-node-1:4194/metrics"]
  namedrop = ["container_*"]

# Only store rest client related metrics for kubelet
[[inputs.prometheus]]
  urls = ["http://kube-node-1:4194/metrics"]
  namepass = ["rest_client_*"]
```

#### Input Config: `namepass` and `namedrop` with separators

```toml
# Pass all metrics of type 'A.C.B' and drop all others like 'A.C.D.B'
[[inputs.socket_listener]]
  data_format = "graphite"
  templates = ["measurement*"]

  namepass = ["A.*.B"]
  namepass_separator = "."

# Drop all metrics of type 'A.C.B' and pass all others like 'A.C.D.B'
[[inputs.socket_listener]]
  data_format = "graphite"
  templates = ["measurement*"]

  namedrop = ["A.*.B"]
  namedrop_separator = "."
```

#### Input Config: `taginclude` and `tagexclude`

```toml
# Only include the "cpu" tag in the measurements for the cpu plugin.
[[inputs.cpu]]
  percpu = true
  totalcpu = true
  taginclude = ["cpu"]

# Exclude the `fstype` tag from the measurements for the disk plugin.
[[inputs.disk]]
  tagexclude = ["fstype"]
```

#### Input config: `prefix`, `suffix`, and `override`

The following example emits measurements with the name `cpu_total`:

```toml
[[inputs.cpu]]
  name_suffix = "_total"
  percpu = false
  totalcpu = true
```

The following example emits measurements with the name `foobar`:

```toml
[[inputs.cpu]]
  name_override = "foobar"
  percpu = false
  totalcpu = true
```

#### Input config: tags

The following example emits measurements with two additional tags: `tag1=foo` and `tag2=bar`.

NOTE: Order matters; the `[inputs.cpu.tags]` table must be at the *end* of the plugin definition.

```toml
[[inputs.cpu]]
  percpu = false
  totalcpu = true
  [inputs.cpu.tags]
    tag1 = "foo"
    tag2 = "bar"
```

#### Multiple inputs of the same type

Additional inputs (or outputs) of the same type can be specified by defining these instances in the configuration file. To avoid measurement collisions, use the `name_override`, `name_prefix`, or `name_suffix` configuration options:

```toml
[[inputs.cpu]]
  percpu = false
  totalcpu = true

[[inputs.cpu]]
  percpu = true
  totalcpu = false
  name_override = "percpu_usage"
  fielddrop = ["cpu_time*"]
```

#### Output configuration examples:

```toml
[[outputs.influxdb]]
  urls = [ "http://localhost:8086" ]
  database = "telegraf"
  precision = "1s"
  # Drop all measurements that start with "aerospike"
  namedrop = ["aerospike*"]

[[outputs.influxdb]]
  urls = [ "http://localhost:8086" ]
  database = "telegraf-aerospike-data"
  precision = "1s"
  # Only accept aerospike data:
  namepass = ["aerospike*"]

[[outputs.influxdb]]
  urls = [ "http://localhost:8086" ]
  database = "telegraf-cpu0-data"
  precision = "1s"
  # Only store measurements where the tag "cpu" matches the value "cpu0"
  [outputs.influxdb.tagpass]
    cpu = ["cpu0"]
```

#### Aggregator Configuration Examples:

This will collect and emit the min/max of the system load1 metric every 30s, dropping the originals.

```toml
[[inputs.system]]
  fieldpass = ["load1"] # collects system load1 metric.

[[aggregators.minmax]]
  period = "30s"        # send & clear the aggregate every 30s.
  drop_original = true  # drop the original metrics.

[[outputs.file]]
  files = ["stdout"]
```

This will collect and emit the min/max of the swap metrics every 30s, dropping the originals. The aggregator will not be applied to the system load metrics due to the `namepass` parameter.

```toml
[[inputs.swap]]

[[inputs.system]]
  fieldpass = ["load1"] # collects system load1 metric.

[[aggregators.minmax]]
  period = "30s"        # send & clear the aggregate every 30s.
  drop_original = true  # drop the original metrics.
  namepass = ["swap"]   # only "pass" swap metrics through the aggregator.

[[outputs.file]]
  files = ["stdout"]
```

To learn more about configuring the Telegraf agent, watch the following video:

## Plugin selection via labels and selectors

You can control which plugin instances are enabled by adding labels to plugin configurations and passing one or more selectors on the command line.

### Selectors

Provide selectors with one or more `--select` flags when starting Telegraf. Each `--select` value is a semicolon-separated list of key=value pairs:

```text
<key>=<value>[;<key>=<value>]
```

- Pairs in a single `--select` value are combined with logical AND (all must match).
- Multiple `--select` flags are combined with logical OR (a plugin is enabled if it matches any selector set).

Selectors support simple glob patterns in values (for example `region=us-*`).

Example:

```console
telegraf --config config.conf --config-directory directory/ \
  --select="app=payments;region=us-*" \
  --select="env=prod" \
  --watch-config --print-plugin-config-source=true

```

### Labels

Add an optional `labels` table to a plugin, similar to `tags`. Keys and values are plain strings.

Example:

```toml
[[inputs.cpu]]
  [inputs.cpu.labels]
    app = "payments"
    region = "us-east"
    env = "prod"
```

Telegraf matches the command-line selectors against a plugin’s labels to decide whether that plugin instance should be enabled. For details on supported syntax and matching rules, see the labels selectors spec.

## Transport Layer Security (TLS)

Many Telegraf plugins support TLS configuration for secure communication. Reference the detailed TLS documentation for configuration options and examples.

---

## Telegraf commands and flags

The `telegraf` command starts and runs all the processes necessary for Telegraf to function.

## Usage

```bash
telegraf [commands]
telegraf [flags]
```

## Commands

| Command | Description |
| --- | --- |
| config | Generate and migrate Telegraf configurations |
| secrets | Manage secrets in secret stores |
| plugins | Print available plugins |
| version | Print current version to stdout |

## Global flags

| Flag | Description |
| --- | --- |
| --config <file> | Configuration file to load. |
| --config-directory <directory> | Directory containing additional *.conf files. |
| --test-wait | Number of seconds to wait for service inputs to complete in test or once mode. |
| --usage <plugin> | Print plugin usage (example: telegraf --usage mysql). |
| --pprof-addr <address> | pprof address to listen on. Disabled by default. |
| --watch-config | Restart Telegraf on local configuration changes. Use either fs notifications (notify) or polling (poll). Disabled by default. |
| --pidfile <file> | File to write PID to. |
| --password <password> | Password to unlock secret stores. |
| --old-env-behavior | Switch back to pre-v1.27 environment replacement behavior. |
| --once | Gather metrics once, write them, and exit. |
| --debug | Enable debug logging. |
| --quiet | Run in quiet mode. |
| --unprotected | Do not protect secrets in memory. |
| --test | Gather metrics once and print them. |
| --deprecation-list | Print all deprecated plugins or plugin options. |
| --input-list | Print available input plugins. |
| --output-list | Print available output plugins. |
| --version | (Deprecated) Print Telegraf version. |
| --sample-config | (Deprecated) Print full sample configuration. |
| --plugin-directory <directory> | (Deprecated) Directory containing *.so files to search recursively for plugins. Found plugins are loaded, tagged, and identified. |
| --section-filter <filter> | Filter configuration sections to output (agent, global_tags, outputs, processors, aggregators and inputs). Separator is :. |
| --input-filter <filter> | Filter input plugins to enable. Separator is :. |
| --output-filter | Filter output plugins to enable. Separator is :. |
| --aggregator-filter <filter> | Filter aggregators to enable. Separator is :. |
| --processor-filter <filter> | Filter processor plugins to enable. Separator is :. |
| --secretstore-filter <filter> | Filter secretstore plugins to enable. Separator is :. |

## Examples

- [Generate a Telegraf configuration file](#generate-a-telegraf-configuration-file)
- [Generate a configuration with only specific plugins](#generate-a-configuration-with-only-specific-plugins)
- [Run a single Telegraf configuration and output metrics to stdout](#run-a-single-telegraf-configuration-and-output-metrics-to-stdout)
- [Run Telegraf with all plugins defined in configuration file](#run-telegraf-with-all-plugins-defined-in-configuration-file)
- [Run Telegraf, but only enable specific plugins](#run-telegraf-but-only-enable-specific-plugins)
- [Run Telegraf with pprof](#run-telegraf-with-pprof)

### Generate a Telegraf configuration file

```sh
telegraf config > telegraf.conf
```

### Generate a configuration with only specific plugins

```sh
telegraf config \
  --input-filter cpu \
  --output-filter influxdb
```

### Run a single Telegraf configuration and output metrics to stdout

```sh
telegraf --config telegraf.conf --test
```

### Run Telegraf with all plugins defined in configuration file

```sh
telegraf --config telegraf.conf
```

### Run Telegraf, but only enable specific plugins

```sh
telegraf \
  --config telegraf.conf \
  --input-filter cpu:mem \
  --output-filter influxdb
```

### Run Telegraf with pprof

```sh
telegraf \
  --config telegraf.conf \
  --pprof-addr localhost:6060
```

---

## Telegraf Aggregator Plugins

Telegraf aggregator plugins aggregate data across multiple metrics. Aggregator plugins create aggregate metrics–for example, by implementing statistical functions such as mean, min, and max.

### Basic Statistics

Plugin ID: `aggregators.basicstats`
Telegraf v1.5.0+

This plugin computes basic statistics such as counts, differences, minima, maxima, mean values, non-negative differences etc. for a set of metrics and emits these statistical values every `period`.

[View](/telegraf/v1/aggregator-plugins/basicstats/)

### Derivative

Plugin ID: `aggregators.derivative`
Telegraf v1.18.0+

This plugin computes the derivative for all fields of the aggregated metrics.

[View](/telegraf/v1/aggregator-plugins/derivative/)

### Final

Plugin ID: `aggregators.final`
Telegraf v1.11.0+

This plugin emits the last metric of a contiguous series, defined as a series which receives updates within the time period in `series_timeout`. The contiguous series may be longer than the time interval defined by `period`. When a series has not been updated within the `series_timeout`, the last metric is emitted.

Alternatively, the plugin emits the last metric in the `period` for the `periodic` output strategy.

This is useful for getting the final value for data sources that produce discrete time series such as procstat, cgroup, kubernetes etc. or to downsample metrics collected at a higher frequency.

All emited metrics do have fields with `_final` appended to the field-name by default.

[View](/telegraf/v1/aggregator-plugins/final/)

### Histogram

Plugin ID: `aggregators.histogram`
Telegraf v1.4.0+

This plugin creates histograms containing the counts of field values within the configured range. The histogram metric is emitted every `period`.

In `cumulative` mode, values added to a bucket are also added to the consecutive buckets in the distribution creating a [cumulative histogram](https://en.wikipedia.org/wiki/Histogram#/media/File:Cumulative_vs_normal_histogram.svg).

By default bucket counts are not reset between periods and will be non-strictly increasing while Telegraf is running. This behavior can be by setting the `reset` parameter.

[View](/telegraf/v1/aggregator-plugins/histogram/)

### Merge

Plugin ID: `aggregators.merge`
Telegraf v1.13.0+

This plugin merges metrics of the same series and timestamp into new metrics with the super-set of fields. A series here is defined by the metric name and the tag key-value set.

Use this plugin when fields are split over multiple metrics, with the same measurement, tag set and timestamp.

[View](/telegraf/v1/aggregator-plugins/merge/)

### Minimum-Maximum

Plugin ID: `aggregators.minmax`
Telegraf v1.1.0+

This plugin aggregates the minimum and maximum values of each field it sees, emitting the aggrate every `period` seconds with field names suffixed by `_min` and `_max` respectively.

[View](/telegraf/v1/aggregator-plugins/minmax/)

### Quantile

Plugin ID: `aggregators.quantile`
Telegraf v1.18.0+

This plugin aggregates each numeric field per metric into the specified quantiles and emits the quantiles every `period`. Different aggregation algorithms are supported with varying accuracy and limitations.

[View](/telegraf/v1/aggregator-plugins/quantile/)

### Starlark

Plugin ID: `aggregators.starlark`
Telegraf v1.21.0+

This plugin allows to implement a custom aggregator plugin via a [Starlark](https://github.com/google/starlark-go) script.

The Starlark language is a dialect of Python and will be familiar to those who have experience with the Python language. However, there are major differences. Existing Python code is unlikely to work unmodified.

The execution environment is sandboxed, and it is not possible to access the local filesystem or perfoming network operations. This is by design of the Starlark language as a configuration language.

The Starlark script used by this plugin needs to be composed of the three methods defining an aggreagtor named `add`, `push` and `reset`.

The `add` method is called as soon as a new metric is added to the plugin the metrics to the aggregator. After `period`, the `push` method is called to output the resulting metrics and finally the aggregation is reset by using the `reset` method of the Starlark script.

The Starlark functions might use the global function `state` to keep aggregation information such as added metrics etc.

More details on the syntax and available functions can be found in the [Starlark specification](https://github.com/google/starlark-go/blob/d1966c6b9fcd/doc/spec.md).

[View](/telegraf/v1/aggregator-plugins/starlark/)

### Value Counter

Plugin ID: `aggregators.valuecounter`
Telegraf v1.8.0+

This plugin counts the occurrence of unique values in fields and emits the counter once every `period` with the field-names being suffixed by the unique value converted to `string`.

The fields to be counted must be configured using the `fields` setting, otherwise no field will be counted and no metric is emitted.

This plugin is useful to e.g. count the occurrances of HTTP status codes or other categorical values in the defined `period`.

Counting fields with a high number of potential values may produce a significant amounts of new fields and results in an increased memory usage. Take care to only count fields with a limited set of values.

[View](/telegraf/v1/aggregator-plugins/valuecounter/)

