# Source: https://docs.fluentd.org/0.12/quickstart/getting-started.md

# Getting Started

Let's get started with **Fluentd**! **Fluentd** is a fully free and fully open-source log collector that instantly enables you to have a '**Log Everything**' architecture with [600+ types of systems](http://fluentd.org/plugin/).

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LWNPJuIG9Ym5ELlFCti%2F-LWNPOPNQ1l9hvoJ2FIp%2Ffluentd-architecture.png?generation=1547671545415964\&alt=media) Fluentd treats logs as JSON, a popular machine-readable format. It is written primarily in C with a thin-Ruby wrapper that gives users flexibility.

Fluentd's scalability has been proven in the field: its largest user currently collects logs from **500,000+ servers**.

## Step1: Installing Fluentd

Please follow the installation/quickstart guides below that matches your environment.

* [Install Fluentd by RPM package](https://docs.fluentd.org/0.12/articles/install-by-rpm) (Redhat Linux)
* [Install Fluentd by Deb package](https://docs.fluentd.org/0.12/articles/install-by-deb) (Ubuntu/Debian Linux)
* [Install Fluentd by DMG package](https://docs.fluentd.org/0.12/articles/install-by-dmg) (Mac OS X)
* [Install Fluentd by Ruby Gem](https://docs.fluentd.org/0.12/articles/install-by-gem)
* [Install Fluentd by Chef](https://docs.fluentd.org/0.12/articles/install-by-chef)
* [Install Fluentd from source](https://docs.fluentd.org/0.12/articles/install-from-source)

Fluentd v0.12 doesn't support Windows environment. Please see [Collecting Log Data from Windows](https://docs.fluentd.org/0.12/use-cases/windows) for details. Fluentd v1 supports Windows.

## Step2: Use Cases

The articles shown below cover the typical use cases of Fluentd. Please refer to the article(s) that suits your needs.

* Use Cases
  * [Data Search like Splunk](https://docs.fluentd.org/0.12/articles/free-alternative-to-splunk-by-fluentd)
  * [Data Filtering and Alerting](https://docs.fluentd.org/0.12/articles/splunk-like-grep-and-alert-email)
  * [Data Analytics with Treasure Data](https://docs.fluentd.org/0.12/articles/http-to-td)
  * [Data Collection to MongoDB](https://docs.fluentd.org/0.12/articles/apache-to-mongodb)
  * [Data Collection to HDFS](https://docs.fluentd.org/0.12/articles/http-to-hdfs)
  * [Data Archiving to Amazon S3](https://docs.fluentd.org/0.12/articles/apache-to-s3)
  * [Windows Event Collection](https://docs.fluentd.org/0.12/use-cases/windows)
* Basic Configuration
  * [Config File](https://docs.fluentd.org/0.12/configuration/config-file)
* Application Logs
  * [Ruby](https://docs.fluentd.org/0.12/articles/ruby), [Java](https://docs.fluentd.org/0.12/articles/java), [Python](https://docs.fluentd.org/0.12/articles/python), [PHP](https://docs.fluentd.org/0.12/articles/php),

    [Perl](https://docs.fluentd.org/0.12/articles/perl), [Node.js](https://docs.fluentd.org/0.12/articles/nodejs), [Scala](https://docs.fluentd.org/0.12/articles/scala)
* Happy Users :)
  * [Users](https://github.com/fluent/fluentd-docs-gitbook/tree/c21f9269df12a1f728b4ec63fa20b57ff387ba2d/articles/users.md)

## Step3: Learn More

The articles shown below will provide detailed information for you to learn more about Fluentd.

* [Architecture Overview](https://www.fluentd.org/architecture)
* [Life of a Fluentd Event](https://docs.fluentd.org/0.12/quickstart/life-of-a-fluentd-event)
* Plugin Overview
  * [Input Plugins](https://docs.fluentd.org/0.12/input)
  * [Output Plugins](https://docs.fluentd.org/0.12/output)
  * [Buffer Plugins](https://docs.fluentd.org/0.12/buffer)
  * [Filter Plugins](https://docs.fluentd.org/0.12/filter)
  * [Parser Plugins](https://docs.fluentd.org/0.12/parser)
  * [Formatter Plugins](https://docs.fluentd.org/0.12/formatter)
* [High Availability Configuration](https://docs.fluentd.org/0.12/deployment/high-availability)
* [FAQ](https://docs.fluentd.org/0.12/quickstart/faq)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
