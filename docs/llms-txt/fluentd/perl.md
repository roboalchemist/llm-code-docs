# Source: https://docs.fluentd.org/language-bindings/perl.md

# Source: https://docs.fluentd.org/0.12/articles/perl.md

# Perl

The '[Fluent::Logger](http://github.com/fluent/fluent-logger-perl)' library is used to post records from Perl applications to Fluentd.

This article explains how to use the Fluent::Logger library.

## Prerequisites

* Basic knowledge of Perl
* Basic knowledge of Fluentd
* Perl 5.10 or higher

## Installing Fluentd

Please refer to the following documents to install fluentd.

* [Install Fluentd with rpm Package](https://docs.fluentd.org/0.12/articles/install-by-rpm)
* [Install Fluentd with deb Package](https://docs.fluentd.org/0.12/articles/install-by-deb)
* [Install Fluentd with Ruby Gem](https://docs.fluentd.org/0.12/articles/install-by-gem)
* [Install Fluentd from source](https://docs.fluentd.org/0.12/articles/install-from-source)

## Modifying the Config File

Next, please configure Fluentd to use the [forward Input plugin](https://docs.fluentd.org/0.12/articles/broken-reference) as its data source.

```
<source>
  @type forward
  port 24224
</source>
<match fluentd.test.**>
  @type stdout
</match>
```

Please restart your agent once these lines are in place.

```
# for rpm/deb only
$ sudo /etc/init.d/td-agent restart
```

## Using Fluent::Logger

First, install the [*Fluent::Logger*](http://search.cpan.org/dist/Fluent-Logger/) library via CPAN.

```
$ cpan
cpan[1]> install Fluent::Logger
```

Next, initialize and post the records as shown below.

```
# test.pl
use Fluent::Logger;
my $logger = Fluent::Logger->new(
    host => '127.0.0.1',
    port => 24224,
    tag_prefix => 'fluentd.test',
);
$logger->post("follow", { "entry1" => "value1", "entry2" => 2 });
```

Executing the script will send the logs to Fluentd.

```
$ perl test.pl
```

The logs should be output to `/var/log/td-agent/td-agent.log` or stdout of the Fluentd process via the [stdout Output plugin](https://docs.fluentd.org/0.12/articles/broken-reference).

## Production Deployments

### Output Plugins

Various [output plugins](https://docs.fluentd.org/0.12/articles/broken-reference) are available for writing records to other destinations:

* Examples
  * [Store Apache Logs into Amazon S3](https://docs.fluentd.org/0.12/articles/apache-to-s3)
  * [Store Apache Logs into MongoDB](https://docs.fluentd.org/0.12/articles/apache-to-mongodb)
  * [Data Collection into HDFS](https://docs.fluentd.org/0.12/articles/http-to-hdfs)
* List of Plugin References
  * [Output to Another Fluentd](https://docs.fluentd.org/0.12/articles/broken-reference)
  * [Output to MongoDB](https://docs.fluentd.org/0.12/articles/broken-reference) or [MongoDB ReplicaSet](https://docs.fluentd.org/0.12/articles/broken-reference)
  * [Output to Hadoop](https://docs.fluentd.org/0.12/articles/broken-reference)
  * [Output to File](https://docs.fluentd.org/0.12/articles/broken-reference)
  * [etc...](http://fluentd.org/plugin/)

### High-Availability Configurations of Fluentd

For high-traffic websites (more than 5 application nodes), we recommend using a high availability configuration of td-agent. This will improve data transfer reliability and query performance.

* [High-Availability Configurations of Fluentd](https://docs.fluentd.org/0.12/deployment/high-availability)

### Monitoring

Monitoring Fluentd itself is also important. The article below describes general monitoring methods for td-agent.

* [Monitoring Fluentd](https://docs.fluentd.org/0.12/deployment/monitoring)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
