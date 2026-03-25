# Fluentd Documentation

Source: https://docs.fluentd.org/llms-full.txt

---

# Introduction

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-M0vivFWtr3QN9VxTyV4%2F-M0vixzAJXD8GclNVYeS%2Flogo_documentation_0.12.png?generation=1582623876773978\&alt=media)

[Fluentd](https://www.fluentd.org/) is an open source data collector for unified logging layer. Fluentd allows you to unify data collection and consumption for a better use and understanding of data.

**The development/support of Fluentd v0.12 has been ended. We don't recommend to use v0.12 for the deployment. Use v1 for new deployment**

[Fluentd](https://www.fluentd.org/) is licensed under the terms of the [Apache License v2.0](http://www.apache.org/licenses/LICENSE-2.0). This project is made and sponsored by [Treasure Data](https://www.treasuredata.com).


# Overview

Let's get started with **Fluentd**! **Fluentd** is a fully free and fully open-source log collector that instantly enables you to have a '**Log Everything**' architecture with [600+ types of systems](http://fluentd.org/plugin/).

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2Fsync%2F2080cbf519d11ff536876a1e02ea0081f8c2fa35.png?generation=1615537295244056\&alt=media)

Fluentd treats logs as JSON, a popular machine-readable format. It is written primarily in C with a thin-Ruby wrapper that gives users flexibility.

Fluentd's scalability has been proven in the field: its largest user currently collects logs from **500,000+ servers**.

## Step1: Installing Fluentd

Please follow the installation/quickstart guides below that matches your environment.

* [Install Fluentd by RPM package](https://docs.fluentd.org/articles/install-by-rpm) (Redhat Linux)
* [Install Fluentd by Deb package](https://docs.fluentd.org/articles/install-by-deb) (Ubuntu/Debian Linux)
* [Install Fluentd by DMG package](https://docs.fluentd.org/articles/install-by-dmg) (Mac OS X)
* [Install Fluentd by Ruby Gem](https://docs.fluentd.org/articles/install-by-gem)
* [Install Fluentd by Chef](https://docs.fluentd.org/articles/install-by-chef)
* [Install Fluentd from source](https://docs.fluentd.org/articles/install-from-source)

Fluentd v0.12 doesn't support Windows environment. Please see [Collecting Log Data from Windows](https://docs.fluentd.org/use-cases/windows) for details. Fluentd v1.x supports Windows.

## Step2: Use Cases

The articles shown below cover the typical use cases of Fluentd. Please refer to the article(s) that suits your needs.

* Use Cases
  * [Data Search like Splunk](https://docs.fluentd.org/articles/free-alternative-to-splunk-by-fluentd)
  * [Data Filtering and Alerting](https://docs.fluentd.org/articles/splunk-like-grep-and-alert-email)
  * [Data Analytics with Treasure Data](https://docs.fluentd.org/articles/http-to-td)
  * [Data Collection to MongoDB](https://docs.fluentd.org/articles/apache-to-mongodb)
  * [Data Collection to HDFS](https://docs.fluentd.org/articles/http-to-hdfs)
  * [Data Archiving to Amazon S3](https://docs.fluentd.org/articles/apache-to-s3)
  * [Windows Event Collection](https://docs.fluentd.org/use-cases/windows)
* Basic Configuration
  * [Config File](https://docs.fluentd.org/configuration/config-file)
* Application Logs
  * [Ruby](https://docs.fluentd.org/articles/ruby), [Java](https://docs.fluentd.org/articles/java), [Python](https://docs.fluentd.org/articles/python), [PHP](https://docs.fluentd.org/articles/php),

    [Perl](https://docs.fluentd.org/articles/perl), [Node.js](https://docs.fluentd.org/articles/nodejs), [Scala](https://docs.fluentd.org/articles/scala)
* Happy Users :)
  * [Users](https://github.com/fluent/fluentd-docs-gitbook/tree/507e377b7e8e78a312dc49e76bd9a302c33fd058/articles/users.md)

## Step3: Learn More

The articles shown below will provide detailed information for you to learn more about Fluentd.

* [Architecture Overview](https://www.fluentd.org/architecture)
* [Life of a Fluentd Event](https://docs.fluentd.org/quickstart/life-of-a-fluentd-event)
* Plugin Overview
  * [Input Plugins](https://docs.fluentd.org/input)
  * [Output Plugins](https://docs.fluentd.org/output)
  * [Buffer Plugins](https://docs.fluentd.org/buffer)
  * [Filter Plugins](https://docs.fluentd.org/filter)
  * [Parser Plugins](https://docs.fluentd.org/parser)
  * [Formatter Plugins](https://docs.fluentd.org/formatter)
* [High Availability Configuration](https://docs.fluentd.org/deployment/high-availability)
* [FAQ](https://docs.fluentd.org/quickstart/faq)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Getting Started

Let's get started with **Fluentd**! **Fluentd** is a fully free and fully open-source log collector that instantly enables you to have a '**Log Everything**' architecture with [600+ types of systems](http://fluentd.org/plugin/).

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LWNPJuIG9Ym5ELlFCti%2F-LWNPOPNQ1l9hvoJ2FIp%2Ffluentd-architecture.png?generation=1547671545415964\&alt=media) Fluentd treats logs as JSON, a popular machine-readable format. It is written primarily in C with a thin-Ruby wrapper that gives users flexibility.

Fluentd's scalability has been proven in the field: its largest user currently collects logs from **500,000+ servers**.

## Step1: Installing Fluentd

Please follow the installation/quickstart guides below that matches your environment.

* [Install Fluentd by RPM package](https://docs.fluentd.org/articles/install-by-rpm) (Redhat Linux)
* [Install Fluentd by Deb package](https://docs.fluentd.org/articles/install-by-deb) (Ubuntu/Debian Linux)
* [Install Fluentd by DMG package](https://docs.fluentd.org/articles/install-by-dmg) (Mac OS X)
* [Install Fluentd by Ruby Gem](https://docs.fluentd.org/articles/install-by-gem)
* [Install Fluentd by Chef](https://docs.fluentd.org/articles/install-by-chef)
* [Install Fluentd from source](https://docs.fluentd.org/articles/install-from-source)

Fluentd v0.12 doesn't support Windows environment. Please see [Collecting Log Data from Windows](https://docs.fluentd.org/use-cases/windows) for details. Fluentd v1 supports Windows.

## Step2: Use Cases

The articles shown below cover the typical use cases of Fluentd. Please refer to the article(s) that suits your needs.

* Use Cases
  * [Data Search like Splunk](https://docs.fluentd.org/articles/free-alternative-to-splunk-by-fluentd)
  * [Data Filtering and Alerting](https://docs.fluentd.org/articles/splunk-like-grep-and-alert-email)
  * [Data Analytics with Treasure Data](https://docs.fluentd.org/articles/http-to-td)
  * [Data Collection to MongoDB](https://docs.fluentd.org/articles/apache-to-mongodb)
  * [Data Collection to HDFS](https://docs.fluentd.org/articles/http-to-hdfs)
  * [Data Archiving to Amazon S3](https://docs.fluentd.org/articles/apache-to-s3)
  * [Windows Event Collection](https://docs.fluentd.org/use-cases/windows)
* Basic Configuration
  * [Config File](https://docs.fluentd.org/configuration/config-file)
* Application Logs
  * [Ruby](https://docs.fluentd.org/articles/ruby), [Java](https://docs.fluentd.org/articles/java), [Python](https://docs.fluentd.org/articles/python), [PHP](https://docs.fluentd.org/articles/php),

    [Perl](https://docs.fluentd.org/articles/perl), [Node.js](https://docs.fluentd.org/articles/nodejs), [Scala](https://docs.fluentd.org/articles/scala)
* Happy Users :)
  * [Users](https://github.com/fluent/fluentd-docs-gitbook/tree/c21f9269df12a1f728b4ec63fa20b57ff387ba2d/articles/users.md)

## Step3: Learn More

The articles shown below will provide detailed information for you to learn more about Fluentd.

* [Architecture Overview](https://www.fluentd.org/architecture)
* [Life of a Fluentd Event](https://docs.fluentd.org/quickstart/life-of-a-fluentd-event)
* Plugin Overview
  * [Input Plugins](https://docs.fluentd.org/input)
  * [Output Plugins](https://docs.fluentd.org/output)
  * [Buffer Plugins](https://docs.fluentd.org/buffer)
  * [Filter Plugins](https://docs.fluentd.org/filter)
  * [Parser Plugins](https://docs.fluentd.org/parser)
  * [Formatter Plugins](https://docs.fluentd.org/formatter)
* [High Availability Configuration](https://docs.fluentd.org/deployment/high-availability)
* [FAQ](https://docs.fluentd.org/quickstart/faq)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Installation

## Articles

* [Before Installing Fluentd](https://docs.fluentd.org/articles/before-install)
* [Installing Fluentd with Docker](https://docs.fluentd.org/container-deployment/install-by-docker)
* [Installing Fluentd using RPM Package (Redhat Linux)](https://docs.fluentd.org/articles/install-by-rpm)
* [Installing Fluentd using DEB Package (Debian / Ubuntu Linux)](https://docs.fluentd.org/articles/install-by-deb)
* [Installing Fluentd using .dmg Package (MacOS X)](https://docs.fluentd.org/articles/install-by-dmg)
* [Installing Fluentd using Ruby Gem](https://docs.fluentd.org/articles/install-by-gem)
* [Installing Fluentd using Chef](https://docs.fluentd.org/articles/install-by-chef)
* [Installing Fluentd from Source](https://docs.fluentd.org/articles/install-from-source)
* [Installing Fluentd on Heroku](https://docs.fluentd.org/articles/install-on-heroku)
* [Installing Fluentd on AWS Elastic Beanstalk](https://docs.fluentd.org/articles/install-on-beanstalk)


# Life of a Fluentd event

The following article describe a global overview of how events are processed by [Fluentd](http://fluentd.org) using examples. It covers the complete cycle including *Setup*, *Inputs*, *Filters*, *Matches* and *Labels*.

## Basic Setup

The configuration files is the fundamental piece to connect all things together, as it allows to define which *Inputs* or listeners [Fluentd](http://fluentd.org) will have and set up common matching rules to route the *Event* data to a specific *Output*.

We will use the [in\_http](https://docs.fluentd.org/input/http) and the [out\_stdout](https://docs.fluentd.org/output/stdout) plugins as examples to describe the events cycle. The following is a basic definition on the configuration file to specify an *http* input, for short: we will be listening for **HTTP Requests**:

```
<source>
  @type http
  port 8888
  bind 0.0.0.0
</source>
```

This definition specifies that a HTTP server will be listening on TCP port 8888. Now let's define a *Matching* rule and a desired output that will just print the data that arrived on each incoming request to standard output:

```
<match test.cycle>
  @type stdout
</match>
```

The *Match* directive sets a rule that matches each *Incoming* event that arrives with a **Tag** equal to *test.cycle* will use the *Output* plugin type called *stdout*. At this point we have an *Input* type, a *Match* and an *Output*. Let's test the setup using *curl*:

```
$ curl -i -X POST -d 'json={"action":"login","user":2}' http://localhost:8888/test.cycle
HTTP/1.1 200 OK
Content-type: text/plain
Connection: Keep-Alive
Content-length: 0
```

On the Fluentd server side the output should look like this:

```
$ bin/fluentd -c in_http.conf
2015-01-19 12:37:41 -0600 [info]: reading config file path="in_http.conf"
2015-01-19 12:37:41 -0600 [info]: starting fluentd-0.12.3
2015-01-19 12:37:41 -0600 [info]: using configuration file: <ROOT>
  <source>
    @type http
    bind 0.0.0.0
    port 8888
  </source>
  <match test.cycle>
    @type stdout
  </match>
</ROOT>
2015-01-19 12:37:41 -0600 [info]: adding match pattern="test.cycle" type="stdout"
2015-01-19 12:37:41 -0600 [info]: adding source type="http"
2015-01-19 12:39:57 -0600 test.cycle: {"action":"login","user":2}
```

## Event structure

A Fluentd event consists of a tag, time and record.

* tag: Where an event comes from. For message routing
* time: When an event happens. Epoch time
* record: Actual log content. JSON object

The input plugin is responsible for generating Fluentd events from specified data sources. For example, `in_tail` generates events from text lines. If you have the following line in apache logs:

```
192.168.0.1 - - [28/Feb/2013:12:00:00 +0900] "GET / HTTP/1.1" 200 777
```

the following event is generated:

```
tag: apache.access # set by configuration
time: 1362020400   # 28/Feb/2013:12:00:00 +0900
record: {"user":"-","method":"GET","code":200,"size":777,"host":"192.168.0.1","path":"/"}
```

## Processing Events

When a *Setup* is defined, the *Router Engine* already contains several rules to apply for different input data. Internally an *Event* will pass through a chain of procedures that may alter the *Events* cycle.

Now we will expand the previous basic example and add more steps in our *Setup* to demonstrate how the *Events* cycle can be altered. We will do this through the new *Filters* implementation.

### Filters

A *Filter* aims to behave like a rule to either accept or reject an event. The following configuration adds a *Filter* definition:

```
<source>
  @type http
  port 8888
  bind 0.0.0.0
</source>

<filter test.cycle>
  @type grep
  exclude1 action logout
</filter>

<match test.cycle>
  @type stdout
</match>
```

As you can see, the new *Filter* definition added will be a mandatory step before passing control to the *Match* section. The *Filter* basically accepts or rejects the *Event* based on it *type* and the defined rule. For our example we want to discard any user `logout` action, we only care about the `login` action. The way this is accomplished is by the *Filter* doing a `grep` that will exclude any message where the `action` key has the string value "logout".

From a *Terminal*, run the following two `curl` commands (please note that each one contains a different `action` value):

```
$ curl -i -X POST -d 'json={"action":"login","user":2}' http://localhost:8888/test.cycle
HTTP/1.1 200 OK
Content-type: text/plain
Connection: Keep-Alive
Content-length: 0

$ curl -i -X POST -d 'json={"action":"logout","user":2}' http://localhost:8888/test.cycle
HTTP/1.1 200 OK
Content-type: text/plain
Connection: Keep-Alive
Content-length: 0
```

Now looking at the [Fluentd](http://fluentd.org) service output we can see that only the event with `action` equal to "login" is matched. The `logout` *Event* was discarded:

```
$ bin/fluentd -c in_http.conf
2015-01-19 12:37:41 -0600 [info]: reading config file path="in_http.conf"
2015-01-19 12:37:41 -0600 [info]: starting fluentd-0.12.4
2015-01-19 12:37:41 -0600 [info]: using configuration file: <ROOT>
<source>
  @type http
  bind 0.0.0.0
  port 8888
</source>
<filter test.cycle>
  @type grep
  exclude1 action logout
</filter>
<match test.cycle>
  @type stdout
</match>
</ROOT>
2015-01-19 12:37:41 -0600 [info]: adding filter pattern="test.cycle" type="grep"
2015-01-19 12:37:41 -0600 [info]: adding match pattern="test.cycle" type="stdout"
2015-01-19 12:37:41 -0600 [info]: adding source type="http"
2015-01-27 01:27:11 -0600 test.cycle: {"action":"login","user":2}
```

As you can see, the *Events* follow a *step-by-step cycle* where they are processed in order from top to bottom. The new engine on [Fluentd](http://fluentd.org) allows integrating as many *Filters* as needed. Considering that the configuration file might grow and start getting a bit complex, a new feature called *Labels* has been added that aims to help manage this complexity.

### Labels

The *Labels* implementation aims to reduce configuration file complexity and allows to define new *Routing* sections that do not follow the *top to bottom* order, instead acting like linked references. Using the previous example we will modify the setup as follows:

```
<source>
  @type http
  bind 0.0.0.0
  port 8888
  @label @STAGING
</source>

<filter test.cycle>
  @type grep
  exclude1 action login
</filter>

<label @STAGING>
  <filter test.cycle>
    @type grep
    exclude1 action logout
  </filter>

  <match test.cycle>
    @type stdout
  </match>
</label>
```

This new configuration contains a `@label` key on the `source` indicating that any further steps take place on the *STAGING* *Label* section. Every *Event* reported on the *Source* is routed by the *Routing* engine and continue processing on *STAGING*, skipping the old filter definition.

### Buffers

In this example, we use `stdout` non-buffered output, but in production buffered outputs are often necessary, e.g. `forward`, `mongodb`, `s3` and etc. Buffered output plugins store received events into buffers and are then written out to a destination after meeting flush conditions. Using buffered output you don't see received events immediately, unlike `stdout` non-buffered output.

Buffers are important for reliability and throughput. See [Output](https://docs.fluentd.org/output) and [Buffer](https://docs.fluentd.org/buffer) articles.

## Execution unit

This section describes the internal implementation.

Fluentd's events are processed on input plugin thread by default. For example, if you have `in_tail -> filter_grep -> out_stdout` pipeline, this pipeline is executed on in\_tail's thread. The important point is `filter_grep` and `out_stdout` plugins don't have own thread for processing.

For Buffered Output, output plugin has own threads for flushing buffer. For example, if you have `in_tail -> filter_grep -> out_forward` pipeline, this pipeline is executed on in\_tail's thread and out\_forward's flush thread. in\_tail's thread processes events until events are written into buffer. Buffer flush and its error handling is the output responsibility. This de-couples the input/output and this model has merits, separate responsibilities, easy error handling, good performance.

## Conclusion

Once the events are reported by the [Fluentd](http://fluend.org) engine on the *Source* they can be processed *step by step* or inside a referenced *Label*, with any *Event* being filtered out at any moment. The new *Routing* engine behavior aims to provide more flexibility and simplifies the processing before events reach the *Output* plugin.

## Learn More

* [Fluentd v0.12 Blog Announcement](http://www.fluentd.org/blog/fluentd-v0.12-is-released)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Support

## Mailing List (Google Groups)

Got a question? Have some cool Fluentd-related projects? The mailing list is the place to be.

* [Mailing List](https://groups.google.com/forum/#!forum/fluentd)

## Slack

Join our Slack channel and talk with Fluentd developers and users directly, now.

* [Slack](http://slack.fluentd.org/)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# FAQ

## What version of Ruby does fluentd support?

Fluentd v0.12 works on 1.9.3 or later. Since v1.x, 2.1 or later.

## Known Issue

### I use Fluentd with Ruby 2.0 but Fluentd seems deadlocked. Why?

The rubygems of Ruby 2.0-p353 has a deadlock problem ([#9224](https://bugs.ruby-lang.org/issues/9224)). If you use Ruby 2.0-p353, upgrading Ruby to latest patch level or Ruby 2.1 resolve this problem.

Please make sure that you are using either RHEL 7.1 and ruby-2.0.0.598-25.el7\_1 package or alternatively you can choose more recent Ruby provided by Red Hat Software Collections (<https://access.redhat.com/documentation/en/red-hat-software-collections/>)

Unfortunately, Ruby 2.0 package of Ubuntu 14.04 use Ruby 2.0-p353. So don't use Fluentd with Ruby 2.0 package on this environment. You can install specified Ruby version using [rbenv](https://github.com/sstephenson/rbenv).

Using td-agent is another way to avoid this problem because td-agent includes own Ruby.

## Operations

### I have millisecond timestamp log but fluentd drops subsecond. Why?

In v0.12 or earlier, fluentd's event time is second unit. It means fluentd converts millisecond/nanosecond timestamp into second timestamp.

Since v1.x, event tims has nanosecond resolution, so fluentd can handle millisecond/nanosecond timestamp properly.

Visit [v1.x document](https://docs.fluentd.org/v1.0/articles/quickstart)

### I have a weird timestamp value, what happened?

The timestamps of Fluentd and its logger libraries depend on your system's clock. It's highly recommended that you set up NTP on your nodes so that your clocks remain synced with the correct clocks.

### I installed td-agent and want to add custom plugins. How do I do it?

td-agent has own Ruby so you should install gems into td-agent's Ruby, not system Ruby.

#### td-agent:

Please use `td-agent-gem` as shown below.

```
$ /usr/sbin/td-agent-gem install <plugin name>
```

For example, issue the following command if you are adding `fluent-plugin-twitter`.

```
$ /usr/sbin/td-agent-gem install fluent-plugin-twitter
```

Now you might be wondering, "Why do I need to specify the full path?" The reason is that td-agent does not modify any host environment variable, including `PATH`. If you want to make all td-agent/fluentd related programs available without writing "/usr/lib/..." every time, you can add

```
export PATH=$PATH:/opt/td-agent/embedded/bin/
```

to your `~/.bash_profile`.

If you would like to find out more about plugin management, please take a look at the [Plugin Management](https://docs.fluentd.org/deployment/plugin-management) article.

### I installed the plugin and it updates fluentd from v0.12 to v1.x. Why?

You installed v1.0 based plugin. See [Plugin Management](https://docs.fluentd.org/deployment/plugin-management#plugin-version-management).

### How can I match (send) an event to multiple outputs?

You can use the `copy` [output plugin](https://docs.fluentd.org/quickstart/faq) to send the same event to multiple output destinations.

### How can I use environment variables to configure parameters dynamically?

Use `"#{ENV['YOUR_ENV_VARIABLE']}"`. For example,

```
some_field "#{ENV['FOO_HOME']}"
```

Note that it must be double quotes and not single quotes

### Fluentd raises an error for host:port. Why?

There are several reasons:

* If you get `Address already in use` error, other process has already

  used `host:port`. Check port conflict between processes / plugins.
* If you get `Permission denied` error, you try to use well-known

  port. Search `well-known port` for how to use well-known port. Use

  `capabilities` or something

If you get other errors, google it.

### I got "no patterns matched" in the log, why?

This means you emit the event but no `<match>` directive for emitted event. For example, if you emit the event with `foo.bar` tag, you need to define `<match>` for `foo.bar` tag like `<match foo.**>`.

See also: [Life of a Fluentd event](https://docs.fluentd.org/quickstart/life-of-a-fluentd-event) or [Config File](https://docs.fluentd.org/configuration/config-file)

### File buffer doesn't work properly, why?

`file` buffer has limitations. Check [`buf_file` article](https://docs.fluentd.org/v/0.12/buffer/file#limitation).

### I got enconding error inside plugin. How to fix it?

You may hit `"\xC3" from ASCII-8BIT to UTF-8"` like `UndefinedConversionError` in the plugin. This error happens when string encoding is set to `ASCII-8BIT` but actual content is `UTF-8`. Fluentd and almost plugins treat the logs as a `ASCII-8BIT` by default but some libraries assume the log encoding is `UTF-8`. This is why this error happens.

There are several approaches to avoid this problem.

* Set encoding correctly.
  * `tail` input has encoding related parameters to change the log

    encoding
  * Use `record_modifier` filter to change the encoding. See

    \[fluent-plugin-record-modifier

    README]\(<https://github.com/repeatedly/fluent-plugin-record-modifier#char_encoding>)
* Use `yajl` instead of `json` when error happens inside

  `JSON.parse/JSON.dump`

## Plugin Development

### How do I develop a custom plugin?

Please refer to the [Plugin Development Guide](http://docs.fluentd.org/articles/plugin-development).

## HOWTOs

### How can I parse `<my complex text log>`?

If you are willing to write Regexp, [fluentd-ui's in\_tail editor](https://github.com/fluent/fluentd-docs-gitbook/tree/507e377b7e8e78a312dc49e76bd9a302c33fd058/articles/fluentd-ui/README.md#intail-setting) or [Fluentular](http://fluentular.herokuapp.com) is a great tool to verify your Regexps.

If you do NOT want to write any Regexp, look at [the Grok parser](https://github.com/kiyoto/fluent-plugin-grok-parser).

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Use Cases


# Centralized App Logging

## Articles

* [Centralize Logs from Java Applications](https://docs.fluentd.org/articles/java)
* [Centralize Logs from Ruby Applications](https://docs.fluentd.org/articles/ruby)
* [Centralize Logs from Python Applications](https://docs.fluentd.org/articles/python)
* [Centralize Logs from PHP Applications](https://docs.fluentd.org/articles/php)
* [Centralize Logs from Perl Applications](https://docs.fluentd.org/articles/perl)
* [Centralize Logs from Node.js Applications](https://docs.fluentd.org/articles/nodejs)
* [Centralize Logs from Scala Applications](https://docs.fluentd.org/articles/scala)


# Monitoring Service Logs

## Articles

* [Free Alternative to Splunk by Fluentd + Elasticsearch](https://docs.fluentd.org/articles/free-alternative-to-splunk-by-fluentd)
* [Email Alerts like Splunk](https://docs.fluentd.org/articles/splunk-like-grep-and-alert-email)


# Data Analytics

## Articles

* [Data Analytics with Treasure Data](https://docs.fluentd.org/articles/http-to-td)
* [Data Collection to Hadoop (HDFS)](https://docs.fluentd.org/articles/http-to-hdfs)


# Connecting to Data Storages

## Articles

* [Store Apache Logs into Amazon S3](https://docs.fluentd.org/articles/apache-to-s3)
* [Store Apache Logs into MongoDB](https://docs.fluentd.org/articles/apache-to-mongodb)
* [Store Apache Logs into Riak](https://docs.fluentd.org/articles/apache-to-riak)
* [Collecting GlusterFS Logs](https://docs.fluentd.org/articles/collect-glusterfs-logs)


# Stream Processing

## Articles

* [Easy Data Stream Manipulation using Fluentd](https://docs.fluentd.org/articles/filter-modify-apache)
* [Stream Data Collection to Kinesis Stream](https://docs.fluentd.org/articles/kinesis-stream)
* [Fluentd and Norikra: Complex Event Processing](https://docs.fluentd.org/articles/cep-norikra)


# Windows Event Collection

In this article, we explain how to get started with collecting data from Windows machines (This setup has been tested on a 64-bit Windows 8 machine).

As of v10, Fluentd does NOT support Windows. However, there are times when you must collect data streams from Windows machines. For example:

1. **Tailing log files on Windows**: collect and analyze log data from

   a Windows application.
2. **Collecting Windows Event Logs**: collect event logs from your

   Windows servers for system analysis, compliance checking, etc.

**If you're not familiar with Fluentd**, please learn more about Fluentd first.

[What is Fluentd?](https://www.fluentd.org/architecture)

## Prerequisites

1. [nxlog](http://nxlog.org), an open source log management tool that

   runs on Windows.
2. A Linux server (we assume Ubuntu 12 for this article)

## Setup

### Set up a Linux server with rsyslogd and Fluentd

1. Get hold of a Linux server. In this example, we assume it is Ubuntu.
2. \*\*Make sure it has ports open for TCP. In the following example, we

   assume port 5140 is open.\*\*
3. [Install td-agent](https://docs.fluentd.org/articles/install-by-deb). (See

   [here](https://docs.fluentd.org/quickstart/installation) for various ways to install

   Fluentd/Treasure Agent)
4. Edit td-agent's configuration file located at `/etc/td-agent/td-agent.conf` and add the following lines

   ```
    <source>
      @type tcp
      format none
      port 5140
      tag windowslog
    </source>    
    <match windowslog>
      @type stdout
    </match>

    The above code listens to port 5140 (UDP) and outputs the data to stdout (which is piped to `/var/log/td-agent/td-agent.log`)
   ```
5. Start td-agent by running `sudo service td-agent start`

### Set up nxlog on Windows

1. Follow [this link](http://nxlog.org/download) and download a copy of

   nxlog onto the Windows machine you want to collect log data from.

   Open the downloaded installer and follow the instructions. By

   default, it should be installed in `C:\Program Files (x86)\nxlog`
2. Create an nxlog config file as follows and save it as `nxlog.conf`:

   ```
    #define ROOT C:\Program Files\nxlog
    define ROOT C:\Program Files (x86)\nxlog

    Moduledir %ROOT%\modules
    CacheDir %ROOT%\data
    Pidfile %ROOT%\data\nxlog.pid
    SpoolDir %ROOT%\data
    LogFile %ROOT%\data\nxlog.log

    <Input in>
      Module im_file
      File 'C:\Users\SomeUser\Desktop\nxlog_test.log' #Put the file to be tailed here.
      SavePos TRUE
      InputType LineBased
    </Input>

    <Output out>
      Module om_tcp
      Host LINUX_MACHINE_RUNNING_FLUENTD
      Port 5140
    </Output> 

    <Route r>
      Path in => out
    </Route>
   ```

   This configuration will send each line of the log file (see the File parameter inside \\\<Input in>...\\\</Input>) as a syslog message to a remote Fluentd/Treasure Agent instance.

### Test

1. Go to nxlog's directory (in Powershell or Command Prompt) and run the following command:

   ```
    \nxlog.exe -f -c  <path to nxlog.conf>
   ```

   The "-f" option runs nxlog in the foreground (this is for testing). If this is for production, you would want to turn it into a Windows Service.
2. Once nxlog is running, add a new line "Windows is awesome" into the tailed file like this:

   ```
    echo Windows is awesome >> 'C:\Users\SomeUser\Desktop\nxlog_test.log'
   ```
3. Now, go to the Linux server and run

   ```
    $ sudo tail -f /var/log/td-agent/td-agent.log
    ...
    ...
    ...
    2014-12-20 02:19:36 +0000 windowslog: {"message":"Windows is awesome \r"}
   ```
4. You successfully sent data from a Windows machine to a remote Fluentd instance running on Linux.

### Parsing JSON Logs

If you are sending JSON logs on Windows to Fluentd, Fluentd can parse them as they come in. To do, simply change Fluentd's configuration as follows. Note the change from `format none` to `format json`. (See [this article](https://docs.fluentd.org/use-cases/broken-reference) for more details about the parser plugins)

```
<source>
  @type tcp
  format json
  port 5140
  tag windowslog
</source>    
<match windowslog>
  @type stdout
</match>
```

Then, if you add a new line to the file on your windows machine like this:

```
echo {"name":"Sadayuki", "age":27} >> 'C:\Users\SomeUser\Desktop\nxlog_test.log'
```

On the Linux machine running Fluentd, you see the following line:

```
2014-12-20 02:22:44 +0000 windowslog: {"name":"Sadayuki","age":27}
```

### Next Step

This example showed that we can collect data from a Windows machine and send it to a remote Fluentd instance. However, the data is not terribly useful because each line of data is placed into the "message" field as unstructured text. For production purposes, you would probably want to write a plugin/extend the syslog plugin so that you can parse the "message" field in the event.

## Learn More

* [Fluentd Architecture](https://www.fluentd.org/architecture)
* [Fluentd Get Started](https://docs.fluentd.org/use-cases/broken-reference)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# IoT Data Logger

[Raspberry Pi](http://www.raspberrypi.org/) is a credit-card-sized single-board computer. Because it is low-cost and easy to equip with various types of sensors, using Raspberry Pi as a cloud data logger is one of its ideal use cases.

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN5dYOAF-IzE1dHrmV%2F-LXN5jkeHwg0j2w836Qk%2Fraspberry-pi-cloud-data-logger.png?generation=1548740135442948\&alt=media)

This article introduces how to transport sensor data from Raspberry Pi to the cloud, using Fluentd as the data collector. For the cloud side, we'll use the [Treasure Data](http://www.fluentd.org/treasuredata) cloud data service as an example, but you can use any cloud service in its place.

[What is Fluentd?](https://www.fluentd.org/architecture)

## Install Raspbian

[Raspbian](http://www.raspbian.org/) is a free operating system based on Debian, optimized for the Raspberry Pi. Please install Raspbian on your Raspberry Pi by following the instructions in the blog post below:

* [Getting Started with Raspberry Pi: Installing Raspbian](http://www.andrewmunsell.com/blog/getting-started-raspberry-pi-install-raspbian)

## Install Fluentd

Next, we'll install Fluentd on Raspbian. Raspbian bundles Ruby 1.9.3 by default, but we need the extra development package to install Fluentd.

```
$ sudo aptitude install ruby-dev
```

We'll now install Fluentd and the necessary plugins.

```
$ sudo gem install fluentd -v "~> 0.12.0"
$ sudo fluent-gem install fluent-plugin-td
```

## Configure and Launch Fluentd

Please sign up to Treasure Data from the [sign up page](https://console.treasuredata.com/users/sign_up). Its free plan lets you store and analyze millions of data points. You can get your account's API key from the [users page](https://console.treasuredata.com/users/current).

Please prepare the `fluentd.conf` file with the following information, including your API key.

```
<match td.*.*>
  @type tdlog
  apikey YOUR_API_KEY_HERE

  auto_create_table
  buffer_type file
  buffer_path /home/pi/fluentd/td
</match>
<source>
  @type http
  port 8888
</source>
<source>
  @type forward
</source>
```

Finally, please launch Fluentd via your terminal.

```
$ fluentd -c fluent.conf
```

## Upload Test

To test the configuration, just post a JSON message to Fluentd via HTTP.

```
$ curl -X POST -d 'json={"sensor1":3123.13,"sensor2":321.3}' \
  http://localhost:8888/td.testdb.raspberrypi
```

If you're using Python, you can use Fluentd's [python logger](https://docs.fluentd.org/articles/python) library.

Now, access the databases page to confirm that your data has been uploaded to the cloud properly.

* [Treasure Data: List of Databases](https://console.treasuredata.com/databases)

You can now issue queries against the imported data.

* [Treasure Data: New Query](https://console.treasuredata.com/query_forms/new)

For example, these queries calculate the average sensor1 value and the sum of sensor2 values.

```
SELECT AVG(sensor1) FROM raspberrypi;
SELECT SUM(sensor2) FROM raspberrypi;
```

## Conclusion

Raspberry Pi is an ideal platform for prototyping data logger hardware. Fluentd helps Raspberry Pi transfer the collected data to the cloud easily and reliably.

## Learn More

* [Fluentd Architecture](https://www.fluentd.org/architecture)
* [Fluentd Get Started](https://docs.fluentd.org/use-cases/broken-reference)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Configuration


# Config File Syntax

This article describes the basic concepts of Fluentd's configuration file syntax.

## Introduction: The Life of a Fluentd Event

Here is a brief overview of the life of a Fluentd event to help you understand the rest of this page:

The configuration file allows the user to control the input and output behavior of Fluentd by (1) selecting input and output plugins and (2) specifying the plugin parameters. The file is required for Fluentd to operate properly.

See also [Life of a Fluentd Event](https://docs.fluentd.org/quickstart/life-of-a-fluentd-event) article.

## Config File Location

#### RPM, Deb or DMG

If you installed Fluentd using the td-agent packages, the config file is located at /etc/td-agent/td-agent.conf.

```
$ sudo vi /etc/td-agent/td-agent.conf
```

#### Gem

If you installed Fluentd using the Ruby Gem, you can create the configuration file using the following commands. Sending a SIGHUP signal will reload the config file.

```
$ sudo fluentd --setup /etc/fluent
$ sudo vi /etc/fluent/fluent.conf
```

#### FLUENT\_CONF environment variable

You can change default configuration file location via `FLUENT_CONF`. For example, `/etc/td-agent/td-agent.conf` is specified via `FLUENT_CONF` inside td-agent scripts.

#### -c option

See [Command Line Option article](https://docs.fluentd.org/deployment/command-line-option).

## Character encoding

Fluentd assumes configuration file is UTF-8 or ASCII.

## List of Directives

The configuration file consists of the following directives:

1. **source** directives determine the input sources.
2. **match** directives determine the output destinations.
3. **filter** directives determine the event processing pipelines.
4. **system** directives set system wide configuration.
5. **label** directives group the output and filter for internal

   routing
6. **include** directives include other files.

Let's actually create a configuration file step by step.

## (1) "source": where all the data come from

Fluentd's input sources are enabled by selecting and configuring the desired input plugins using **source** directives. Fluentd's standard input plugins include `http` and `forward`. `http` turns fluentd into an HTTP endpoint to accept incoming HTTP messages whereas `forward` turns fluentd into a TCP endpoint to accept TCP packets. Of course, it can be both at the same time (You can add as many sources as you wish)

```
# Receive events from 24224/tcp
# This is used by log forwarding and the fluent-cat command
<source>
  @type forward
  port 24224
</source>

# http://this.host:9880/myapp.access?json={"event":"data"}
<source>
  @type http
  port 9880
</source>
```

Each **source** directive must include a `@type` parameter. The `@type` parameter specifies which input plugin to use.

#### Interlude: Routing

The `source` submits events into the Fluentd's routing engine. An event consists of three entities: **tag**, **time** and **record**. The tag is a string separated by '.'s (e.g. myapp.access), and is used as the directions for Fluentd's internal routing engine. The time field is specified by input plugins, and it must be in the Unix time format. The record is a JSON object. Fluentd accepts all non-period characters as a part of a tag. However, since the tag is sometimes used in a different context by output destinations (e.g., table name, database name, key name, etc.), **it is strongly recommended that you stick to the lower-case alphabets, digits and underscore**, e.g., `^[a-z0-9_]+$`.

In the example above, the HTTP input plugin submits the following event:

```
# generated by http://this.host:9880/myapp.access?json={"event":"data"}
tag: myapp.access
time: (current time)
record: {"event":"data"}
```

#### Didn't find your input source? You can write your own plugin!

You can add new input sources by writing your own plugins. For further information regarding Fluentd's input sources, please refer to the [Input Plugin Overview](https://docs.fluentd.org/configuration/broken-reference) article.

## (2) "match": Tell fluentd what to do!

The "match" directive looks for events with **match**ing tags and processes them. The most common use of the match directive is to output events to other systems (for this reason, the plugins that correspond to the match directive are called "output plugins"). Fluentd's standard output plugins include `file` and `forward`. Let's add those to our configuration file.

```
# Receive events from 24224/tcp
# This is used by log forwarding and the fluent-cat command
<source>
  @type forward
  port 24224
</source>

# http://this.host:9880/myapp.access?json={"event":"data"}
<source>
  @type http
  port 9880
</source>

# Match events tagged with "myapp.access" and
# store them to /var/log/fluent/access.%Y-%m-%d
# Of course, you can control how you partition your data
# with the time_slice_format option.
<match myapp.access>
  @type file
  path /var/log/fluent/access
</match>
```

Each **match** directive must include a match pattern and a `@type` parameter. Only events with a **tag** matching the pattern will be sent to the output destination (in the above example, only the events with the tag "myapp.access" is matched. See [the section below for more advanced usage](#how-match-patterns-work)). The `@type` parameter specifies the output plugin to use.

Just like input sources, you can add new output destinations by writing your own plugins. For further information regarding Fluentd's output destinations, please refer to the [Output Plugin Overview](https://docs.fluentd.org/configuration/broken-reference) article.

## (3) "filter": Event processing pipeline

The "filter" directive has same syntax as "match" but "filter" could be chained for processing pipeline. Using filters, event flow is like below:

```
Input -> filter 1 -> ... -> filter N -> Output
```

Let's add standard `record_transformer` filter to "match" example.

```
# http://this.host:9880/myapp.access?json={"event":"data"}
<source>
  @type http
  port 9880
</source>

<filter myapp.access>
  @type record_transformer
  <record>
    host_param "#{Socket.gethostname}"
  </record>
</filter>

<match myapp.access>
  @type file
  path /var/log/fluent/access
</match>
```

Received event, `{"event":"data"}`, goes to `record_transformer` filter first. `record_transformer` adds "host\_param" field to event and filtered event, `{"event":"data","host_param":"webserver1"}`, goes to `file` output.

You can also add new filters by writing your own plugins. For further information regarding Fluentd's filter destinations, please refer to the [Filter Plugin Overview](https://docs.fluentd.org/configuration/broken-reference) article.

## (4) Set system wide configuration: the "system" directive

Following configurations are set by *system* directive. You can set same configurations by fluentd options:

* log\_level
* suppress\_repeated\_stacktrace
* emit\_error\_log\_interval
* suppress\_config\_dump
* without\_source
* process\_name (only available in *system* directive. No fluentd

  option)

Here is an example:

```
<system>
  # equal to -qq option
  log_level error
  # equal to --without-source option
  without_source
  # ...
</system>
```

### process\_name

If set this parameter, fluentd's supervisor and worker process names are changed.

```
<system>
  process_name fluentd1
</system>
```

If we have this configuration, `ps` command shows the following result:

```
% ps aux | grep fluentd1
foo      45673   0.4  0.2  2523252  38620 s001  S+    7:04AM   0:00.44 worker:fluentd1
foo      45647   0.0  0.1  2481260  23700 s001  S+    7:04AM   0:00.40 supervisor:fluentd1
```

This feature requires ruby 2.1 or later.

## (5) Group filter and output: the "label" directive

The "label" directive groups filter and output for internal routing. "label" reduces the complexity of tag handling.

Here is a configuration example. "label" is built-in plugin parameter so `@` prefix is needed.

```
<source>
  @type forward
</source>

<source>
  @type tail
  @label @SYSTEM
</source>

<filter access.**>
  @type record_transformer
  <record>
    # ...
  </record>
</filter>
<match **>
  @type elasticsearch
  # ...
</match>

<label @SYSTEM>
  <filter var.log.middleware.**>
    @type grep
    # ...
  </filter>
  <match **>
    @type s3
    # ...
  </match>
</label>
```

In this configuration, `forward` events are routed to `record_transformer` filter / `elasticsearch` output and `in_tail` events are routed to `grep` filter / `s3` output inside `@SYSTEM` label.

"label" is useful for event flow separation without tag prefix.

### ERROR label

`@ERROR` label is a built-in label used for error record emitted by plugin's `emit_error_event` API.

If you set `<label @ERROR>` in the configuration, events are routed to this label when emit related error, e.g. buffer is full or invalid record.

(6) Re-use your config: the "## include" directive

Directives in separate configuration files can be imported using the **include** directive:

```
# Include config files in the ./config.d directory
@include config.d/*.conf
```

The **include** directive supports regular file path, glob pattern, and http URL conventions:

```
# absolute path
@include /path/to/config.conf

# if using a relative path, the directive will use
# the dirname of this config file to expand the path
@include extra.conf

# glob match pattern
@include config.d/*.conf

# http
@include http://example.com/fluent.conf
```

Note for glob pattern, files are expanded in the alphabetical order. If you have `a.conf` and `b.conf`, fluentd parses `a.conf` first. But you should not write the configuration depends on this order. It is so error prone. Please separate `@include` for safety.

```
# If you have a.conf,b.conf,...,z.conf and a.conf / z.conf are important...

# This is bad
@include *.conf

# This is good
@include a.conf
@include config.d/*.conf
@include z.conf
```

## How match patterns work

As described above, Fluentd allows you to route events based on their tags. Although you can just specify the exact tag to be matched (like `<filter app.log>`), there are a number of techniques you can use to manage the data flow more efficiently.

### Wildcards and Expansions

The following match patterns can be used in `<match>` and `<filter>` tags.

* `*` matches a single tag part.
  * For example, the pattern `a.*` matches `a.b`, but does not match

    `a` or `a.b.c`
* `**` matches zero or more tag parts.
  * For example, the pattern `a.**` matches `a`, `a.b` and `a.b.c`
* `{X,Y,Z}` matches X, Y, or Z, where X, Y, and Z are match patterns.
  * For example, the pattern `{a,b}` matches `a` and `b`, but does not match `c`
  * This can be used in combination with the `*` or `**` patterns. Examples include `a.{b,c}.*` and `a.{b,c.**}`
* When multiple patterns are listed inside a single tag (delimited by one or more whitespaces), it matches any of the listed patterns. For example:
  * The patterns `<match a b>` match `a` and `b`.
  * The patterns `<match a.** b.*>` match `a`, `a.b`, `a.b.c` (from the first pattern) and `b.d` (from the second pattern).

### Note on Match Order

Fluentd tries to match tags in the order that they appear in the config file. So if you have the following configuration:

```
# ** matches all tags. Bad :(
<match **>
  @type blackhole_plugin
</match>

<match myapp.access>
  @type file
  path /var/log/fluent/access
</match>
```

then `myapp.access` is never matched. Wider match patterns should be defined after tight match patterns.

```
<match myapp.access>
  @type file
  path /var/log/fluent/access
</match>

# Capture all unmatched tags. Good :)
<match **>
  @type blackhole_plugin
</match>
```

Of course, if you use two same patterns, second `match` is never matched. If you want to send events to multiple outputs, consider [out\_copy](https://docs.fluentd.org/configuration/broken-reference) plugin.

The common pitfall is when you put a `<filter>` block after `<match>`. It will never work as supposed, since events never go through the filter for the reason explained above.

```
# You should NOT put this <filter> block after the <match> block below.
# If you do, Fluentd will just emit events without applying the filter.
<filter myapp.access>
  @type record_transformer
  ...
</filter>

<match myapp.access>
  @type file
  path /var/log/fluent/access
</match>
```

## Supported Data Types for Values

Each Fluentd plugin has a set of parameters. For example, [in\_tail](https://docs.fluentd.org/configuration/broken-reference) has parameters such as `rotate_wait` and `pos_file`. Each parameter has a specific type associated with it. They are defined as follows:

Each parameter's type should be documented. If not, please let the plugin author know.

* `string` type: the field is parsed as a string. This is the most

  "generic" type, where each plugin decides how to process the string.

  * `string` has 3 literals, non-quoted one line string, `'` quoted

    string and `"` quoted string.
  * See "Format tips" section and [literal examples](https://github.com/fluent/fluentd/blob/master/example/v1_literal_example.conf).
* `integer` type: the field is parsed as an integer.
* `float` type: the field is parsed as a float.
* `size` type: the field is parsed as the number of bytes. There are

  several notational variations:

  * If the value matches `<INTEGER>k` or `<INTEGER>K`, then the

    value is the INTEGER number of kilobytes.
  * If the value matches `<INTEGER>m` or `<INTEGER>M`, then the

    value is the INTEGER number of megabytes.
  * If the value matches `<INTEGER>g` or `<INTEGER>G`, then the

    value is the INTEGER number of gigabytes.
  * If the value matches `<INTEGER>t` or `<INTEGER>T`, then the

    value is the INTEGER number of terabytes.
  * Otherwise, the field is parsed as integer, and that integer is

    the number of bytes.
* `time` type: the field is parsed as a time duration.
  * If the value matches `<INTEGER>s`, then the value is the INTEGER

    seconds.
  * If the value matches `<INTEGER>m`, then the value is the INTEGER

    minutes.
  * If the value matches `<INTEGER>h`, then the value is the INTEGER

    hours.
  * If the value matches `<INTEGER>d`, then the value is the INTEGER

    days.
  * Otherwise, the field is parsed as float, and that float is the

    number of seconds. This option is useful for specifying

    sub-second time durations such as "0.1" (=0.1 second = 100ms).
* `array` type: the field is parsed as a JSON array. It also supports

  shorthand syntax. These are same values.

  * normal: `["key1", "key2"]`
  * shorthand: `key1,key2`
* `hash` type: the field is parsed as a JSON object. It also supports

  shorthand syntax. These are same values.

  * normal: `{"key1":"value1", "key2":"value2"}`
  * shorthand: `key1:value1,key2:value2`

`array` and `hash` are JSON because almost all programming languages and infrastructure tools can generate JSON value easily than unusual format.

## Common plugin parameter

These parameters are system reserved and it has `@` prefix.

* `@type`: Specify plugin type
* `@id`: Specify plugin id. in\_monitor\_agent uses this value for

  plugin\_id field
* `@label`: Specify label symbol. See

  [label](#5-group-filter-and-output-the-ldquolabelrdquo-directive)

  section
* `@log_level`: Specify per plugin log level. See [Per Plugin Log](https://docs.fluentd.org/deployment/logging#per-plugin-log) section

`type`, `id` and `log_level` are supported for backward compatibility.

## Check configuration file

You can check your configuration without plugins start by specifying `--dry-run` option.

```
$ fluentd --dry-run -c fluent.conf
```

## Format tips

This section describes useful features in configuration format.

### Multi line support for " quoted string, array and hash values

You can write multi line value for `"` quoted string, array and hash values.

```
str_param "foo  # This line is converted to "foo\nbar". NL is kept in the parameter
bar"
array_param [
  "a", "b"
]
hash_param {
  "k":"v",
  "k1":10
}
```

Fluentd assumes `[` or `{` is a start of array / hash. So if you want to set `[` or `{` started but non-json parameter, please use `'` or `"`.

Example1: mail plugin:

```
<match **>
  @type mail
  subject "[CRITICAL] foo's alert system"
</match>
```

Example2: map plugin:

```
<match tag>
  @type map
  map '[["code." + tag, time, { "code" => record["code"].to_i}], ["time." + tag, time, { "time" => record["time"].to_i}]]'
  multi true
</match>
```

We will remove this restriction with configuration parser improvement.

### Embedded Ruby code

You can evaluate the Ruby code with `#{}` in `"` quoted string. This is useful for setting machine information like hostname.

```
host_param "#{Socket.gethostname}" # host_param is actual hostname like `webserver1`.
env_param "foo-#{ENV["FOO_BAR"]}" # NOTE that foo-"#{ENV["FOO_BAR"]}" doesn't work.
```

config-xxx mixins use "${}", not "#{}". These embedded configurations are two different things.

### In double quoted string literal, `\` is escape character

`\` is interpreted as escape character. You need `\` for setting `"`, `\r`, `\n`, `\t`, `\` or several characters in double-quoted string literal.

```
str_param "foo\nbar" # \n is interpreted as actual LF character
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Routing Examples

This article shows typical routing examples.

## Simple Input -> Filter -> Output

```
<source>
  @type forward
</source>

<filter app.**>
  @type record_transformer
  <record>
    hostname "#{Socket.gethostname}"
  </record>
</filter>

<match app.**>
  @type file
  # ...
</match>
```

### Two input cases

```
<source>
  @type forward
</source>

<source>
  @type tail
  tag system.logs
  # ...
</source>

<filter app.**>
  @type record_transformer
  <record>
    hostname "#{Socket.gethostname}"
  </record>
</filter>

<match {app.**,system.logs}>
  @type file
  # ...
</match>
```

If you want to separate data pipeline for each sources, use Label.

## Input -> Filter -> Output with Label

Label reduces complex tag handling by separating data pipeline.

```
<source>
  @type forward
</source>

<source>
  @type dstat
  @label @METRICS # dstat events are routed to <label @METRICS>
  # ...
</source>

<filter app.**>
  @type record_transformer
  <record>
    # ...
  </record>
</filter>

<match app.**>
  @type file
  # ...
</match>

<label @METRICS>
  <match **>
    @type elasticsearch
    # ...
  </match>
</label>
```

## Re-route event by tag

Use [fluent-plugin-route](https://github.com/tagomoris/fluent-plugin-route) plugin. `route` plugin rewrites tag and re-emit events to other match or Label.

```
<match worker.**>
  @type route
  remove_tag_prefix worker
  add_tag_prefix metrics.event

  <route **>
    copy # For fall-through. Without copy, routing is stopped here. 
  </route>
  <route **>
    copy
    @label @BACKUP
  </route>
</match>

<match metrics.event.**>
  @type stdout
</match>

<label @BACKUP>
  <match metrics.event.**>
    @type file
    path /var/log/fluent/bakcup
  </match>
</label>
```

## Re-route event by record content

Use [fluent-plugin-rewrite-tag-filter](https://github.com/fluent/fluent-plugin-rewrite-tag-filter).

```
<source>
  @type forward
</source>

# event example: app.logs {"message":"[info]: ..."}
<match app.**>
  @type rewrite_tag_filter
  rewriterule1 message ^\[(\w+)\] $1.${tag}
</match>

# send mail when receives alert level logs
<match alert.app.**>
  @type mail
  # ...
</match>

# other logs are stored into file
<match *.app.**>
  @type file
  # ...
</match>
```

See also [out\_rewrite\_tag\_filter](https://docs.fluentd.org/configuration/broken-reference) article.

## Re-route event to other Label

Use [out\_relabel](https://docs.fluentd.org/configuration/broken-reference) plugin. `relabel` plugin simply emits events to Label. No tag rewrite.

```
<source>
  @type forward
</source>

<match app.**>
  @type copy
  <store>
    @type forward
    # ...
  </store>
  <store>
    @type relabel
    @label @NOTIFICATION
  </store>
</match>

<label @NOTIFICATION>
  <filter app.**>
    @type grep
    regexp1 message ERROR
  </filter>

  <match app.**>
    @type mail
  </match>
</label>
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Recipes

## Articles

* [Parsing Common Log Formats](https://docs.fluentd.org/articles/common-log-formats)
* [Recipe Syslog To Treasure Data](https://docs.fluentd.org/articles/recipe-syslog-to-treasure-data)
* [Recipe Syslog To S3](https://docs.fluentd.org/articles/recipe-syslog-to-s3)
* [Recipe Apache Logs To S3](https://docs.fluentd.org/articles/recipe-apache-logs-to-s3)
* [Recipe JSON To S3](https://docs.fluentd.org/articles/recipe-json-to-s3)
* [Recipe Apache Logs To Treasure Data](https://docs.fluentd.org/articles/recipe-apache-logs-to-treasure-data)
* [Recipe CSV To Treasure Data](https://docs.fluentd.org/articles/recipe-csv-to-treasure-data)
* [Recipe Nginx To Treasure Data](https://docs.fluentd.org/articles/recipe-nginx-to-treasure-data)
* [Recipe JSON To Treasure Data](https://docs.fluentd.org/articles/recipe-json-to-treasure-data)
* [Recipe Http Rest Api To S3](https://docs.fluentd.org/articles/recipe-http-rest-api-to-s3)
* [Recipe JSON To Mongo](https://docs.fluentd.org/articles/recipe-json-to-mongo)
* [Recipe CSV To Mongo](https://docs.fluentd.org/articles/recipe-csv-to-mongo)
* [Recipe Nginx To Mongo](https://docs.fluentd.org/articles/recipe-nginx-to-mongo)
* [Recipe Http Rest Api To Elasticsearch](https://docs.fluentd.org/articles/recipe-http-rest-api-to-elasticsearch)
* [Recipe JSON To Elasticsearch](https://docs.fluentd.org/articles/recipe-json-to-elasticsearch)
* [Recipe Cloudstack To Mongodb](https://docs.fluentd.org/articles/recipe-cloudstack-to-mongodb)
* [Recipe TSV To Treasure Data](https://docs.fluentd.org/articles/recipe-tsv-to-treasure-data)
* [Recipe TSV To S3](https://docs.fluentd.org/articles/recipe-tsv-to-s3)
* [Recipe Syslog To Mongo](https://docs.fluentd.org/articles/recipe-syslog-to-mongo)
* [Recipe Nginx To Elasticsearch](https://docs.fluentd.org/articles/recipe-nginx-to-elasticsearch)
* [Recipe Syslog To Elasticsearch](https://docs.fluentd.org/articles/recipe-syslog-to-elasticsearch)
* [Recipe TSV To Elasticsearch](https://docs.fluentd.org/articles/recipe-tsv-to-elasticsearch)
* [Recipe Http Rest Api To Mongo](https://docs.fluentd.org/articles/recipe-http-rest-api-to-mongo)
* [Recipe Http Rest Api To Treasure Data](https://docs.fluentd.org/articles/recipe-http-rest-api-to-treasure-data)
* [Recipe TSV To Mongo](https://docs.fluentd.org/articles/recipe-tsv-to-mongo)
* [Recipe Apache Logs To Mongo](https://docs.fluentd.org/articles/recipe-apache-logs-to-mongo)
* [Recipe Nginx To S3](https://docs.fluentd.org/articles/recipe-nginx-to-s3)
* [Recipe CSV To Elasticsearch](https://docs.fluentd.org/articles/recipe-csv-to-elasticsearch)
* [Recipe Apache Logs To Elasticsearch](https://docs.fluentd.org/articles/recipe-apache-logs-to-elasticsearch)
* [Recipe CSV To S3](https://docs.fluentd.org/articles/recipe-csv-to-s3)


# Deployment


# Logging

This article describes Fluentd's logging mechanism.

Fluentd has two log layers: global and per plugin. Different log levels can be set for global logging and plugin level logging.

## Log Level

Shown below is the list of supported values, in increasing order of verbosity:

* `fatal`
* `error`
* `warn`
* `info`
* `debug`
* `trace`

The default log level is `info`, and Fluentd outputs `info`, `warn`, `error` and `fatal` logs by default.

## Global Logs

Global logging is used by Fluentd core and plugins that don't set their own log levels. The global log level can be adjusted up or down.

### By Command Line Option

#### Increase Verbosity Level

The `-v` option sets the verbosity to `debug` while the `-vv` option sets the verbosity to `trace`.

```
$ fluentd -v  ... # debug level
$ fluentd -vv ... # trace level
```

These options are useful for debugging purposes.

#### Decrease Verbosity Level

The `-q` option sets the verbosity to `warn` while the `-qq` option sets the verbosity to `error`.

```
$ fluentd -q  ... # warn level
$ fluentd -qq ... # error level
```

### By Config File

You can also change the logging level with `<system>` section in the config file like below.

```
<system>
  # equal to -qq option
  log_level error
</system>
```

## Per Plugin Log

The `log_level` option sets different levels of logging for each plugin. It can be set in each plugin's configuration file.

For example, in order to debug [in\_tail](https://docs.fluentd.org/deployment/broken-reference) but suppress all but fatal log messages for [in\_http](https://docs.fluentd.org/deployment/broken-reference), their respective `log_level` options should be set as follows:

```
<source>
  @type tail
  @log_level debug
  path /var/log/data.log
  ...
</source>
<source>
  @type http
  @log_level fatal
</source>
```

If you don't specify the `log_level` parameter, the plugin will use the global log level. Some plugins haven't supported per-plugin logging yet. The [logging section of the Plugin Development article](https://docs.fluentd.org/developer/plugin-development#logging) explains how to update such plugins to support the new log level system.

## Suppress repeated stacktrace

Fluentd can suppress same stacktrace with `--suppress-repeated-stacktrace`. For example, if you pass `--suppress-repeated-stacktrace` to fluentd:

```
2013-12-04 15:05:53 +0900 [warn]: fluent/engine.rb:154:rescue in emit_stream: emit transaction failed  error_class = RuntimeError error = #<RuntimeError: syslog>
  2013-12-04 15:05:53 +0900 [warn]: fluent/engine.rb:140:emit_stream: /Users/repeatedly/devel/fluent/fluentd/lib/fluent/plugin/out_stdout.rb:43:in `emit'
  [snip]
  2013-12-04 15:05:53 +0900 [warn]: fluent/engine.rb:140:emit_stream: /Users/repeatedly/devel/fluent/fluentd/lib/fluent/plugin/in_object_space.rb:63:in `run'
2013-12-04 15:05:53 +0900 [error]: plugin/in_object_space.rb:113:rescue in on_timer: object space failed to emit error = "foo.bar" error_class = "RuntimeError" tag = "foo" record = "{ ...}"
2013-12-04 15:05:55 +0900 [warn]: fluent/engine.rb:154:rescue in emit_stream: emit transaction failed  error_class = RuntimeError error = #<RuntimeError: syslog>
  2013-12-04 15:05:53 +0900 [warn]: fluent/engine.rb:140:emit_stream: /Users/repeatedly/devel/fluent/fluentd/lib/fluent/plugin/o/2.0.0/gems/cool.io-1.1.1/lib/cool.io/loop.rb:96:in `run'
  [snip]
```

logs are changed to:

```
2013-12-04 15:05:53 +0900 [warn]: fluent/engine.rb:154:rescue in emit_stream: emit transaction failed  error_class = RuntimeError error = #<RuntimeError: syslog>
  2013-12-04 15:05:53 +0900 [warn]: fluent/engine.rb:140:emit_stream: /Users/repeatedly/devel/fluent/fluentd/lib/fluent/plugin/o/2.0.0/gems/cool.io-1.1.1/lib/cool.io/loop.rb:96:in `run'
  [snip]
  2013-12-04 15:05:53 +0900 [warn]: fluent/engine.rb:140:emit_stream: /Users/repeatedly/devel/fluent/fluentd/lib/fluent/plugin/in_object_space.rb:63:in `run'
2013-12-04 15:05:53 +0900 [error]: plugin/in_object_space.rb:113:rescue in on_timer: object space failed to emit error = "foo.bar" error_class = "RuntimeError" tag = "foo" record = "{ ...}"
2013-12-04 15:05:55 +0900 [warn]: fluent/engine.rb:154:rescue in emit_stream: emit transaction failed  error_class = RuntimeError error = #<RuntimeError: syslog>
  2013-12-04 15:05:55 +0900 [warn]: plugin/in_object_space.rb:111:on_timer: suppressed same stacktrace
```

Same stacktrace is replaced with `suppressed same stacktrace` message until other stacktrace is received.

## Output to log file

Fluentd outputs logs to `STDOUT` by default. To output to a file instead, please specify the `-o` option.

```
$ fluentd -o /path/to/log_file
```

Fluentd doesn't support log rotation yet.

## Capture Fluentd logs

Fluentd marks its own logs with the `fluent` tag. You can process Fluentd logs by using `<match fluent.**>` or `<match **>`(Of course, `**` captures other logs). If you define `<match fluent.**>` in your configuration, then Fluentd will send its own logs to this match destination. This is useful for monitoring Fluentd logs.

For example, if you have the following `<match fluent.**>`:

```
# omit other source / match
<match fluent.**>
  @type stdout
</match>
```

then Fluentd outputs `fluent.info` logs to stdout like below:

```
2014-02-27 00:00:00 +0900 [info]: shutting down fluentd
2014-02-27 00:00:01 +0900 fluent.info: {"message":"shutting down fluentd"} # by <match fluent.**>
2014-02-27 00:00:01 +0900 [info]: process finished code = 0
```

### Case1: Send Fluentd logs to monitoring service

You can send Fluentd logs to a monitoring service by plugins, e.g. datadog, sentry, irc, etc.

```
# Add hostname for identifying the server
<filter fluent.**>
  @type record_transformer
  <record>
    host "#{Socket.gethostname}"
  </record>
</filter>

<match fluent.**>
  @type monitoring_plugin
  # parameters...
</match>
```

### Case2: Use aggregation/monitoring server

You can use [out\_forward](https://docs.fluentd.org/deployment/broken-reference) to send Fluentd logs to a monitoring server. The monitoring server can then filter and send the logs to your notification system: chat, irc, etc.

Leaf server example:

```
# Add hostname for identifying the server and tag to filter by log level
<filter fluent.**>
  @type record_transformer
  <record>
    host "#{Socket.gethostname}"
    original_tag ${tag}
  </record>
</filter>

<match fluent.**>
  @type forward
  <server>
    # Monitoring server parameters
  </server>
</match>
```

Monitoring server example:

```
<source>
  @type forward
  label @FLUENTD_INTERNAL_LOG
</source>

<label @FLUENTD_INTERNAL_LOG>
  # Ignore trace, debug and info log
  <filter fluent.**>
    @type grep
    regexp1 original_tag fluent.(warn|error|fatal)
  </filter>

  <match fluent.**>
    # your notification setup. This example uses irc plugin
    @type irc
    host irc.domain
    channel notify
    message notice: %s [%s] @%s %s
    out_keys original_tag,time,host,message
  </match>
</label>
```

If an error occurs, you will get a notification message in your irc `notify` channel.

```
01:01  fluentd: [11:10:24] notice: fluent.warn [2014/02/27 01:00:00] @leaf.server.domain detached forwarding server 'server.name'
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Monitoring

This article desribes how to monitor Fluentd.

## Fluentd Metrics Monitoring

Fluentd can expose internal metrics via REST API, and works with monitoring tools such as [Prometheus](https://prometheus.io/), [Datadog](https://www.datadoghq.com/), etc. Our recommendation is to use Prometheus, since we will be collaborating more in the future under the [CNCF (Cloud Native Computing Foundation)](https://www.cncf.io/).

* [Monitoring Fluentd (Prometheus)](https://docs.fluentd.org/articles/monitoring-prometheus)
* [Monitoring Fluentd (Datadog)](https://docs.datadoghq.com/integrations/fluentd/)
* [Monitoring Fluentd (REST API)](https://docs.fluentd.org/articles/monitoring-rest-api)

## Process Monitoring

Two `ruby` processes (parent and child) are executed. Please make sure that these processes are running. The example for `td-agent` is shown below.

```
/opt/td-agent/embedded/bin/ruby /usr/sbin/td-agent
  --daemon /var/run/td-agent/td-agent.pid
  --log /var/log/td-agent/td-agent.log
```

For td-agent on Linux, you can check the process statuses with the following command. Two processes should be shown if there are no issues.

```
$ ps w -C ruby -C td-agent --no-heading
32342 ?        Sl     0:00 /opt/td-agent/embedded/bin/ruby /usr/sbin/td-agent --daemon /var/run/td-agent/td-agent.pid --log /var/log/td-agent/td-agent.log
32345 ?        Sl     0:01 /opt/td-agent/embedded/bin/ruby /usr/sbin/td-agent --daemon /var/run/td-agent/td-agent.pid --log /var/log/td-agent/td-agent.log
```

## Port Monitoring

Fluentd opens several ports according to the configuration file. We recommend checking the availability of these ports. The default port settings are shown below:

* TCP 0.0.0.0 9880 (HTTP by default)
* TCP 0.0.0.0 24224 (Forward by default)

## Debug Port

A debug port for local communication is recommended for trouble shooting. Please note that the configuration below will be required.

```
<source>
  @type debug_agent
  bind 127.0.0.1
  port 24230
</source>
```

You can attach the process using the `fluent-debug` command through dRuby.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Signals

This article explains how `Fluentd` handles UNIX signals.

## Process Model

When you launch Fluentd, it creates two processes: supervisor and worker. The supervisor process controls the life cycle of the worker process. Please make sure to send any signals to the supervisor process.

## Signals

### SIGINT or SIGTERM

Stops the daemon gracefully. Fluentd will try to flush the entire memory buffer at once, but will not retry if the flush fails. Fluentd will not flush the file buffer; the logs are persisted on the disk by default.

### SIGUSR1

Forces the buffered messages to be flushed and reopens Fluentd's log. Fluentd will try to flush the current buffer (both memory and file) immediately, and keep flushing at `flush_interval`.

### SIGHUP

Reloads the configuration file by gracefully restarting the worker process. Fluentd will try to flush the entire memory buffer at once, but will not retry if the flush fails. Fluentd will not flush the file buffer; the logs are persisted on the disk by default.

### SIGCONT

Call sigdump to dump fluentd internal status. See [trouble-shooting](https://docs.fluentd.org/trouble-shooting#dump-fluentd-internal-information) article.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# RPC

This article explains how `Fluentd` handles HTTP RPC.

## Overview

HTTP RPC is one way of managing fluentd instance. Several provided RPCs are replacement of [signals](https://docs.fluentd.org/deployment/signals). The response body is JSON format.

On signal unsupported environment, e.g. Windows, you can use RPC instead of signals.

## Configuration

RPC is off by default. If you want to enable RPC, set `rpc_endpoint` in `<system>` section.

```
<system>
  rpc_endpoint 127.0.0.1:24444
</system>
```

After that, you can access to RPC like below.

```
$ curl http://127.0.0.1:24444/api/plugins.flushBuffers
{"ok":true}
```

## RPCs

### /api/processes.interruptWorkers

Replacement of signal's [SIGINT](https://docs.fluentd.org/signals#sigint-or-sigterm). Stop the daemon.

### /api/processes.killWorkers

Replacement of signal's [SIGTERM](https://docs.fluentd.org/signals#sigint-or-sigterm). Stop the daemon.

### /api/plugins.flushBuffers

Replacement of signal's [SIGUSR1](https://docs.fluentd.org/signals#sigusr1). Flushes buffered messages.

### /api/config.reload

Replacement of signal's [SIGHUP](https://docs.fluentd.org/signals#sighup). reload configuration.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# High Availability Config

For high-traffic websites, we recommend using a high availability configuration of `Fluentd`.

## Message Delivery Semantics

Fluentd is designed primarily for event-log delivery systems.

In such systems, several delivery guarantees are possible:

* *At most once*: Messages are immediately transferred. If the

  transfer succeeds, the message is never sent out again. However,

  many failure scenarios can cause lost messages (ex: no more write

  capacity)
* *At least once*: Each message is delivered at least once. In failure

  cases, messages may be delivered twice.
* *Exactly once*: Each message is delivered once and only once. This

  is what people want.

If the system "can't lose a single event", and must also transfer "*exactly once*", then the system must stop ingesting events when it runs out of write capacity. The proper approach would be to use synchronous logging and return errors when the event cannot be accepted.

That's why *Fluentd provides 'At most once' and 'At least once' transfers*. In order to collect massive amounts of data without impacting application performance, a data logger must transfer data asynchronously. This improves performance at the cost of potential delivery failures.

However, most failure scenarios are preventable. The following sections describe how to set up Fluentd's topology for high availability.

## Network Topology

To configure Fluentd for high availability, we assume that your network consists of '*log forwarders*' and '*log aggregators*'.

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-Lf2F2_ZZFRdGwiFpPg1%2F-Lf2FCbVo_U1MlhuyUMx%2Ffluentd_ha.png?generation=1558053970392763\&alt=media)

'*log forwarders*' are typically installed on every node to receive local events. Once an event is received, they forward it to the 'log aggregators' through the network.

'*log aggregators*' are daemons that continuously receive events from the log forwarders. They buffer the events and periodically upload the data into the cloud.

Fluentd can act as either a log forwarder or a log aggregator, depending on its configuration. The next sections describes the respective setups. We assume that the active log aggregator has ip '192.168.0.1' and that the backup has ip '192.168.0.2'.

## Log Forwarder Configuration

Please add the following lines to your config file for log forwarders. This will configure your log forwarders to transfer logs to log aggregators.

```
# TCP input
<source>
  @type forward
  port 24224
</source>

# HTTP input
<source>
  @type http
  port 8888
</source>

# Log Forwarding
<match mytag.**>
  @type forward

  # primary host
  <server>
    host 192.168.0.1
    port 24224
  </server>
  # use secondary host
  <server>
    host 192.168.0.2
    port 24224
    standby
  </server>

  # use longer flush_interval to reduce CPU usage.
  # note that this is a trade-off against latency.
  flush_interval 60s
</match>
```

When the active aggregator (192.168.0.1) dies, the logs will instead be sent to the backup aggregator (192.168.0.2). If both servers die, the logs are buffered on-disk at the corresponding forwarder nodes.

## Log Aggregator Configuration

Please add the following lines to the config file for log aggregators. The input source for the log transfer is TCP.

```
# Input
<source>
  @type forward
  port 24224
</source>

# Output
<match mytag.**>
  ...
</match>
```

The incoming logs are buffered, then periodically uploaded into the cloud. If upload fails, the logs are stored on the local disk until the retransmission succeeds.

## Failure Case Scenarios

### Forwarder Failure

When a log forwarder receives events from applications, the events are first written into a disk buffer (specified by buffer\_path). After every flush\_interval, the buffered data is forwarded to aggregators.

This process is inherently robust against data loss. If a log forwarder's fluentd process dies, the buffered data is properly transferred to its aggregator after it restarts. If the network between forwarders and aggregators breaks, the data transfer is automatically retried.

However, possible message loss scenarios do exist:

* The process dies immediately after receiving the events, but before

  writing them into the buffer.
* The forwarder's disk is broken, and the file buffer is lost.

### Aggregator Failure

When log aggregators receive events from log forwarders, the events are first written into a disk buffer (specified by buffer\_path). After every flush\_interval, the buffered data is uploaded into the cloud.

This process is inherently robust against data loss. If a log aggregator's fluentd process dies, the data from the log forwarder is properly retransferred after it restarts. If the network between aggregators and the cloud breaks, the data transfer is automatically retried.

However, possible message loss scenarios do exist:

* The process dies immediately after receiving the events, but before

  writing them into the buffer.
* The aggregator's disk is broken, and the file buffer is lost.

## Trouble Shooting

### "no nodes are available"

Please make sure that you can communicate with port 24224 using **not only TCP, but also UDP**. These commands will be useful for checking the network configuration.

```
$ telnet host 24224
$ nmap -p 24224 -sU host
```

Please note that there is one [known issue](http://kb.vmware.com/selfservice/microsites/search.do?language=en_US\&cmd=displayKC\&externalId=2019944) where VMware will occasionally lose small UDP packages used for heartbeat.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Failure Scenarios

This article lists various Fluentd failure scenarios. We will assume that you have configured Fluentd for [High Availability](https://docs.fluentd.org/deployment/high-availability), so that each app node has its local *forwarders* and all logs are aggregated into multiple *aggregators*.

## Apps Cannot Post Records to Forwarder

In the failure scenario, the application sometimes fails to post records to its local Fluentd instance when using logger libraries of various languages. Depending on the maturity of each logger library, some clever mechanisms have been implemented to prevent data loss.

### 1) Memory Buffering (available for [Ruby](https://docs.fluentd.org/articles/ruby), [Java](https://docs.fluentd.org/articles/java), [Python](https://docs.fluentd.org/articles/python), [Perl](https://docs.fluentd.org/articles/perl))

If the destination Fluentd instance dies, certain logger implementations will use extra memory to hold incoming logs. When Fluentd comes back, these loggers will automatically send out the buffered logs to Fluentd again. Once the maximum buffer memory size is reached, most current implementations will write the data onto the disk or throw away the logs.

### 2) Exponential Backoff (available for [Ruby](https://docs.fluentd.org/articles/ruby), [Java](https://docs.fluentd.org/articles/java))

When trying to resend logs to the local forwarder, some implementations will use exponential backoff to prevent excessive re-connect requests.

## Forwarder or Aggregator Fluentd Goes Down

What happens when a Fluentd process dies for some reason? It depends on your buffer configuration.

### buf\_memory

If you're using [buf\_memory](https://docs.fluentd.org/deployment/broken-reference), the buffered data is completely lost. This is a tradeoff for higher performance. Lowering the flush\_interval will reduce the probability of losing data, but will increase the number of transfers between forwarders and aggregators.

### buf\_file

If you're using [buf\_file](https://docs.fluentd.org/deployment/broken-reference), the buffered data is stored on the disk. After Fluentd recovers, it will try to send the buffered data to the destination again.

Please note that the data will be lost if the buffer file is broken due to I/O errors. The data will also be lost if the disk is full, since there is nowhere to store the data on disk.

## Storage Destination Goes Down

If the storage destination (e.g. Amazon S3, MongoDB, HDFS, etc.) goes down, Fluentd will keep trying to resend the buffered data. The retry logic depends on the plugin implementation.

If you're using [buf\_memory](https://docs.fluentd.org/deployment/broken-reference), aggregators will stop accepting new logs once they reach their buffer limits. If you're using [buf\_file](https://docs.fluentd.org/deployment/broken-reference), aggregators will continue accepting logs until they run out of disk space.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Performance Tuning

## Articles

* [Performance Tuning (Single Process)](https://docs.fluentd.org/articles/performance-tuning-single-process)
* [Performance Tuning (Multi Process)](https://docs.fluentd.org/articles/performance-tuning-multi-process)


# Plugin Management

This article explains how to manage Fluentd plugins, including adding 3rd party plugins.

## fluent-gem

The `fluent-gem` command is used to install Fluentd plugins. This is a wrapper around the `gem` command.

```
fluent-gem install fluent-plugin-grep
```

Ruby doesn't guarantee C extension API compatibility between its major versions. If you update Fluentd's Ruby version, you should re-install the plugins that depend on C extension.

### If Using td-agent, Use /usr/sbin/td-agent-gem

If you are using td-agent, please make sure to use td-agent's `td-agent-gem` command. Otherwise (e.g. you use the command belonging to system, rvm, etc.), you won't be able to find your "installed" plugins.

Please see [this FAQ](https://docs.fluentd.org/quickstart/faq#i-installed-td-agent-and-want-to-add-custom-plugins-how-do-i-do-it) for more information.

### Gem and native extension

Some plugins depend on natvie extension library. It means you need to install development packages to build it, e.g. gcc, make, autoconf and etc. If you see logs like below, install development packages before plugin installation.

```
Building native extensions.  This could take a while...
ERROR:  Error installing fluent-plugin-twitter:
        ERROR: Failed to build gem native extension.

    /opt/td-agent/embedded/bin/ruby extconf.rb

checking for rb_str_scrub()... yes
creating Makefile

make "DESTDIR = " clean
sh: 1: make: not found

make "DESTDIR = "
sh: 1: make: not found

make failed, exit code 127

Gem files will remain installed in /opt/td-agent/embedded/lib/ruby/gems/2.1.0/gems/string-scrub-0.0.3 for inspection.
Results logged to /opt/td-agent/embedded/lib/ruby/gems/2.1.0/extensions/x86_64-linux/2.1.0/string-scrub-0.0.3/gem_make.out
```

## "-p" option

Fluentd's `-p` option is used to add an extra plugin directory to the load path. For example, if you put the `out_foo.rb` plugin into `/path/to/plugin`, you can load the `out_foo.rb` plugin by specifying the `-p` option as shown below.

```
fluentd -p /path/to/plugin
```

You can specify the `-p` option more than once.

## Add a Plugin Via /etc/fluent/plugin

Fluentd adds the `/etc/fluent/plugin` directory to its load path by default. Thus, any additional plugins that are placed in `/etc/fluent/plugin` will be loaded automatically.

For example, if `/etc/fluent/plugin/out_foo.rb` exists, you can use `@type foo` in `<match>`.

### If Using td-agent, Use /etc/td-agent/plugin

If you are using td-agent, Fluentd uses the `/etc/td-agent/plugin` directory instead of `/etc/fluent/plugin`. Please put your plugins here instead.

## Plugin version management

Fluentd and plugins are evolving, so you may hit unexpected error with latest version, e.g. regression by new feature, removed deprecated parameter,, change library dependency, etc. Avoiding these problems, we recommend to fix fluentd and plugin version on production. If you want to update fluentd or plugins, check the behaviour first on your test environment. For example, td-agent fixes fluentd and plugins version in each release.

Fluentd plugins are rubygems and rubygems installs latest version by default. So we don't recommend to execute following commands on production:

* `gem install fluentd`
* `gem install fluent-plugin-elasticsearch`
* `gem update # This is very dangerous. Update all existing gems`

Another problem: if you install the plugin which depends on fluentd v0.14, `gem` installs fluentd v0.14 together even if you installed fluentd v0.12. This is unexpected result for fluentd v0.12 users.

You should specify target version with `-v` option.

* `gem install fluentd -v 0.12.43`
* `gem install fluent-plugin-elasticsearch -v 1.9.3`

`/usr/sbin/td-agent-gem` is also same because `/usr/sbin/td-agent-gem` uses `gem` command internally.

## "--gemfile" option

A Ruby application manages gem dependencies using Gemfile and [Bundler](http://bundler.io/). Fluentd's `--gemfile` option takes the same approach, and is useful for managing plugin versions separated from shared gems.

For example, if you have following Gemfile at /etc/fluent/Gemfile:

```
source 'https://rubygems.org'

gem 'fluentd', '0.12.43'
gem 'fluent-plugin-elasticsearch', '1.9.3'
```

You can pass this Gemfile to Fluentd via the `--gemfile` option.

```
fluentd --gemfile /etc/fluent/Gemfile
```

When specifying the `--gemfile` option, Fluentd will try to install the listed gems using Bundler. Fluentd will only load listed gems separated from shared gems, and will also prevent unexpected plugin updates.

In addition, if you update Fluentd's Ruby version, Bundler will re-install the listed gems for the new Ruby version. This allows you to avoid the C extension API compatibility problem.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Trouble Shooting

## Look at Logs

If things aren't happening as expected, please first look at your logs. For td-agent (rpm/deb), the logs are located at `/var/log/td-agent/td-agent.log`.

## Turn on Verbose Logging

You can get more information about the logs if verbose logging is turned on. Please follow the steps below.

### rpm/deb

1. Open the service setting file for td-agent (see below for its file

   path).
2. Add `-vv` to TD\_AGENT\_OPTIONS.
3. Restart td-agent.

   ```
   # Add the following settings to:
   # - /etc/sysconfig/td-agent (CentOS/RedHat)
   # - /etc/default/td-agent (Debian/Ubuntu)
   TD_AGENT_OPTIONS="-vv"
   ```

Note: The environment variable TD\_AGENT\_OPTIONS has been introduced in td-agent v2.2.1. If you are using an older version of td-agent, you need to edit `/etc/init.d/td-agent` and insert `-vv` options to TD\_AGENT\_ARGS or DAEMON\_ARGS manually.

### gem

Please add `-vv` to your command line.

```
$ fluentd .. -vv
```

## Dump fluentd internal information

Fluentd uses [sigdump](https://github.com/frsyuki/sigdump) for dumping fluentd internal information to local file, e.g. thread dump, object allocation and etc. If you have a problem with fluentd like process hang, please send `SIGCONT` to fluentd parent and child processes.

## High CPU usage issue

If fluentd suddenly hits unexpected high CPU usage problem, there are several reasons:

* a plugin has a race condition or similar bug
* dependent gems have a bug
* regular expression with broken data
* system calls has a bug, e.g. `inotify` with lots of files

In such cases, you can use `perf` tool on recent Linux to investigate the problem. See [Linux perf Examples](http://www.brendangregg.com/perf.html) page. If you want to know which call causes the problem, [pid2line.rb](https://gist.github.com/nurse/0619b6af90df140508c2) is useful.

## Check uncaught logs

You sometimes hit unexpected shutdown with non-zero exit status like below.

```
2016-01-01 00:00:00 +0800 [info]: starting fluentd-0.12.28
2016-01-01 00:00:00 +0800 [info]: reading config file path="/etc/td-agent/td-agent.conf"
[...snip...]
2016-01-01 00:00:02 +0800 [info]: process finished code=6
```

If the problem happens inside ruby, e.g. segmentation fault, C extension bug, etc, you can't get entire log when fluentd process is daemonized. For example, td-agent launches fluentd with `--daemon` option. In td-agent case, you can get entire log using following command to simulate `/etc/init.d/td-agent start` without daemonize.

```
$ sudo LD_PRELOAD=/opt/td-agent/embedded/lib/libjemalloc.so /usr/sbin/td-agent -c /etc/td-agent/td-agent.conf --user td-agent --group td-agent
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Secure Forwarding

## Overview

This is a quick tutorial on how to use the [secure forward plugin](https://github.com/fluent/fluentd-docs-gitbook/tree/507e377b7e8e78a312dc49e76bd9a302c33fd058/github.com/tagomoris/fluent-plugin-secure-forward/README.md) to **enable SSL for Fluentd-to-Fluentd data transport**.

It is intended as a quick introduction. For comprehensive documentation, including parameter definitions, please checkout out the [out\_secure\_forward](https://docs.fluentd.org/deployment/broken-reference) and [in\_secure\_forward](https://docs.fluentd.org/deployment/broken-reference).

## Setup: Receiver

First, install the secure forward plugin.

* Fluentd: `gem install fluent-plugin-secure-forward`
* td-agent v2:

  `/usr/sbin/td-agent-gem install fluent-plugin-secure-forward`
* td-agent v1:

  `/usr/lib/fluent/ruby/bin/fluent-gem install fluent-plugin-secure-forward`

Then, set up the configuration file as follows:

```
<source>
  @type secure_forward
  shared_key YOUR_SHARED_KEY
  self_hostname server.fqdn.local
  cert_auto_generate yes
</source>

<match secure.**>
  @type stdout
</match>
```

The `<match>` clause is there to print out the forwarded message into STDOUT (which is fed into `var/log/td-agent/td-agent.log` for td-agent) using [out\_stdout](https://docs.fluentd.org/deployment/broken-reference).

Then, (re)start Fluentd/td-agent.

## Setup: Sender

First, install the secure forward plugin.

* Fluentd: `fluent-gem install fluent-plugin-secure-forward`
* td-agent v2:

  `/usr/sbin/td-agent-gem install fluent-plugin-secure-forward`
* td-agent v1:

  `/usr/lib/fluent/ruby/bin/fluent-gem install fluent-plugin-secure-forward`

Then, set up the configuration file as follows:

```
<source>
  @type forward
</source>

<match secure.**>
  @type secure_forward
  shared_key YOUR_SHARED_KEY
  self_hostname "#{Socket.gethostname}"
  <server>
    host RECEIVER_IP
    port 24284
  </server>
</match>
```

The `<source>` clause is there to feed test data into Fluentd using [in\_forward](https://docs.fluentd.org/deployment/broken-reference). Make sure that `YOUR_SHARED_KEY` is same with the receiver's.

Then, (re)start td-agent.

## Confirm: Send an Event Over SSL

On the sender machine, run the following command using `fluent-cat`

* Fluentd:

  `echo '{"message":"testing the SSL forwarding"}' | fluent-cat --json secure.test`
* td-agent v2:

  `echo '{"message":"testing the SSL forwarding"}' | /opt/td-agent/embedded/bin/fluent-cat --json secure.test`
* td-agent v1:

  `echo '{"message":"testing the SSL forwarding"}' | /usr/lib/fluent/ruby/bin/fluent-cat --json secure.test`

Now, checking the receiver's Fluentd's log (for td-agent, this would be `/var/log/td-agent/td-agent.log`), there should be a line like this:

```
2014-10-21 18:18:26 -0400 secure.test: {"message":"testing the SSL forwarding"}
```

## Resources

* [in\_secure\_forward](https://docs.fluentd.org/deployment/broken-reference)
* [out\_secure\_forward](https://docs.fluentd.org/deployment/broken-reference)
* [the secure forward plugin's GitHub repo](https://github.com/fluent/fluentd-docs-gitbook/tree/507e377b7e8e78a312dc49e76bd9a302c33fd058/github.com/fluent/fluent-plugin-secure-forward/README.md)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Fluentd UI

[fluentd-ui](https://github.com/fluent/fluentd-ui) is a browser-based [fluentd](http://fluentd.org/) and [td-agent](http://docs.treasuredata.com/articles/td-agent) manager that supports following operations.

* Install, uninstall, and upgrade Fluentd plugins
* start/stop/restart fluentd process
* Configure Fluentd settings such as config file content, pid file

  path, etc
* View Fluentd log with simple error viewer

## Getting Started

If you've installed td-agent, you can start it by `td-agent-ui start` as below:

```
$ sudo /usr/sbin/td-agent-ui start
Puma 2.9.2 starting...
* Min threads: 0, max threads: 16
* Environment: production
* Listening on tcp://0.0.0.0:9292
```

Or if you use fluentd gem, install fluentd-ui via `gem` command at first.

```
$ gem install -V fluentd-ui
$ fluentd-ui start
Puma 2.9.2 starting...
* Min threads: 0, max threads: 16
* Environment: production
* Listening on tcp://0.0.0.0:9292
```

Then, open <http://localhost:9292/> by your browser.

The default account is username="admin" and password="changeme"

![fluentd-ui](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN7-r390MuHOR6esLj%2F-LXN75LobUYsnqh1DN83%2Ffluentd-ui.gif?generation=1548740488837671\&alt=media)

## Screenshots

(v0.3.9)

### Dashboard

![dashboard](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN7-r390MuHOR6esLj%2F-LXN75Lqhjda7klOWXLH%2Fdashboard.gif?generation=1548740487994706\&alt=media)

### Setting

![setting](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN7-r390MuHOR6esLj%2F-LXN75Ls4uwG3MIRBti-%2Fsetting.gif?generation=1548740489790657\&alt=media)

### in\_tail setting

![in\_tail](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN7-r390MuHOR6esLj%2F-LXN75Lu8ZFlZsWbyiba%2Fin_tail.gif?generation=1548740489728498\&alt=media)

### Plugin

![plugin](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN7-r390MuHOR6esLj%2F-LXN75LwXtZ-_EUY8A1i%2Fplugin.gif?generation=1548740489553253\&alt=media)

![ss01](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN7-r390MuHOR6esLj%2F-LXN75LySbiYP5pdVZiH%2F01.png?generation=1548740490538533\&alt=media) ![ss02](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN7-r390MuHOR6esLj%2F-LXN75M-jqdAEBlQHqQo%2F02.png?generation=1548740487994588\&alt=media) ![ss03](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN7-r390MuHOR6esLj%2F-LXN75M1tIVYzDBR2vp6%2F03.png?generation=1548740488752147\&alt=media) ![ss04](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN7-r390MuHOR6esLj%2F-LXN75M3IRX-64NbIe3n%2F04.png?generation=1548740488688874\&alt=media) ![ss05](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN7-r390MuHOR6esLj%2F-LXN75M58Do4BvU-trsj%2F05.png?generation=1548740490236453\&alt=media)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Command Line Option

This article describes built-in commands and its options

## fluentd

Invoke fluentd. Here is supported options:

```
Usage: fluentd [options]
    -s, --setup [DIR=/etc/fluent]    install sample configuration file to the directory`
    -c, --config PATH                config file path (default: /etc/fluent/fluent.conf)
        --dry-run                    Check fluentd setup is correct or not
    -p, --plugin DIR                 add plugin directory
    -I PATH                          add library path
    -r NAME                          load library
    -d, --daemon PIDFILE             daemonize fluent process
        --no-supervisor              run without fluent supervisor
        --user USER                  change user
        --group GROUP                change group
    -o, --log PATH                   log file path
    -i CONFIG_STRING,                inline config which is appended to the config file on-fly
        --inline-config
        --emit-error-log-interval SECONDS
                                     suppress interval seconds of emit error logs
        --suppress-repeated-stacktrace [VALUE]
                                     suppress repeated stacktrace
        --without-source             invoke a fluentd without input plugins
        --use-v1-config              Use v1 configuration format (default)
        --use-v0-config              Use v0 configuration format
    -v, --verbose                    increase verbose level (-v: debug, -vv: trace)
    -q, --quiet                      decrease verbose level (-q: warn, -qq: error)
        --suppress-config-dump       suppress config dumping when fluentd starts
    -g, --gemfile GEMFILE            Gemfile path
    -G, --gem-path GEM_INSTALL_PATH  Gemfile install path (default: $(dirname $gemfile)/vendor/bundle)
```

### Important options

#### --suppress-config-dump

Fluentd starts without configuration dump. If you don't want to show configuration in fluentd logs, e.g. don't show private keys, this options is useful.

#### --suppress-repeated-stacktrace

If set true, suppress stacktrace in fluentd logs. Since v0.12, this option is true by default.

#### --without-source

Fluentd starts without input plugins. This option is useful for flushing buffers with no new incoming events.

#### -i, --inline-config

If you use fluentd on XaaS which doesn't support persistent disks, this option is useful.

#### --no-supervisor

If you want to use your supervisor tools, this option avoids double supervisor.

### Set via configuration file

Several options could be set via `<system>` directive configuration file. See [configuration file article](https://docs.fluentd.org/configuration/config-file#4-set-system-wide-configuration-the-ldquosystemrdquo-directive).

## fluent-cat

Send event to fluentd's `in_forward`/`in_unix` plugin. This is useful for testing.

```
Usage: fluent-cat [options] <tag>
    -p, --port PORT                  fluent tcp port (default: 24224)
    -h, --host HOST                  fluent host (default: 127.0.0.1)
    -u, --unix                       use unix socket instead of tcp
    -s, --socket PATH                unix socket path (default: /var/run/fluent/fluent.sock)
    -f, --format FORMAT              input format (default: json)
        --json                       same as: -f json
        --msgpack                    same as: -f msgpack
        --none                       same as: -f none
        --message-key KEY            key field for none format (default: message)
```

### example

Send json message with `debug.log` tag to local fluentd:

```
% echo '{"message":"hello"}' | fluent-cat debug.log
```

Send to other machine:

```
% echo '{"message":"hello"}' | fluent-cat debug.log --host testserver --port 24225
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Container Deployment


# Docker Image

This article explains how to use [Fluentd's official Docker image](https://hub.docker.com/r/fluent/fluentd/), maintained by [Treasure Data, Inc](http://www.treasuredata.com/).

* [Fluentd's official Docker image](https://hub.docker.com/r/fluent/fluentd/)
* [Fluentd's official Docker image (Source)](https://github.com/fluent/fluentd-docker-image)

## Step 0: Install Docker

Please download and install [Docker](https://www.docker.com/) from here.

* [Docker Installation](https://docs.docker.com/engine/installation/)

## Step 1: Pull Fluentd's Docker image

Then, please download Fluentd v0.12's image by `docker pull` command.

```
$ docker pull fluent/fluentd:v0.12-debian
```

Debian and Alpine Linux version is available for Fluentd image. Debian version is recommended officially since it has jemalloc support, however Alpine image is smaller.

## Step 2: Launch Fluentd Container

To make the test simple, create the example config below at `/tmp/fluentd.conf`. This example accepts records from http, and output to stdout.

```
# /tmp/fluentd.conf
<source>
  @type http
  port 9880
  bind 0.0.0.0
</source>
<match **>
  @type stdout
</match>
```

Finally, you can run Fluentd with `docker run` command.

```
$ docker run -d \
  -p 9880:9880 -v /tmp:/fluentd/etc -e FLUENTD_CONF=fluentd.conf \
  fluent/fluentd
2017-01-30 11:52:23 +0000 [info]: reading config file path="/fluentd/etc/fluentd.conf"
2017-01-30 11:52:23 +0000 [info]: starting fluentd-0.12.31
2017-01-30 11:52:23 +0000 [info]: gem 'fluentd' version '0.12.31'
2017-01-30 11:52:23 +0000 [info]: adding match pattern="**" type="stdout"
2017-01-30 11:52:23 +0000 [info]: adding source type="http"
2017-01-30 11:52:23 +0000 [info]: using configuration file: <ROOT>
  <source>
    @type http
    port 9880
    bind 0.0.0.0
  </source>
  <match **>
    @type stdout
  </match>
</ROOT>
```

## Step3: Post Sample Logs via HTTP

Let's post sample logs via HTTP and confirm it's working. `curl` command is always your friend.

```
$ curl -X POST -d 'json={"json":"message"}' http://localhost:9880/sample.test
```

Use `docker ps` command to retrieve container ID, and use `docker logs` command to check the specific container's log.

```
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                         NAMES
b495e527850c        fluent/fluentd      "/bin/sh -c 'exec ..."   2 hours ago         Up 2 hours          5140/tcp, 24224/tcp, 0.0.0.0:9880->9880/tcp   awesome_mcnulty
$ docker logs b495e527850c | tail -n 1
2017-01-30 14:04:37 +0000 sample.test: {"json":"message"}
```

## Next Steps

Now you know how to use Fluentd via Docker. Here're a couple of Docker related documentations for Fluentd.

* [Fluentd's official Docker image](https://hub.docker.com/r/fluent/fluentd/)
* [Fluentd's official Docker image (Source)](https://github.com/fluent/fluentd-docker-image)
* [Docker Logging Driver and Fluentd](https://docs.fluentd.org/articles/docker-logging)
* [Docker Logging via EFK (Elasticsearch + Fluentd + Kibana) Stack with Docker Compose](https://docs.fluentd.org/articles/docker-logging-efk-compose)

Also, please see the following tutorials to learn how to collect your data from various data sources.

* Basic Configuration
  * [Config File](https://docs.fluentd.org/configuration/config-file)
* Application Logs
  * [Ruby](https://docs.fluentd.org/articles/ruby), [Java](https://docs.fluentd.org/articles/java), [Python](https://docs.fluentd.org/articles/python), [PHP](https://docs.fluentd.org/articles/php),

    [Perl](https://docs.fluentd.org/articles/perl), [Node.js](https://docs.fluentd.org/articles/nodejs), [Scala](https://docs.fluentd.org/articles/scala)
* Examples
  * [Store Apache Log into Amazon S3](https://docs.fluentd.org/articles/apache-to-s3)
  * [Store Apache Log into MongoDB](https://docs.fluentd.org/articles/apache-to-mongodb)
  * [Data Collection into HDFS](https://docs.fluentd.org/articles/http-to-hdfs)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Docker Logging Driver

The following article describes how to implement an unified logging system for your [Docker](http://www.docker.com) containers. Any production application requires to register certain events or problems during runtime.

The old fashion way is to write these messages to a log file, but that inherits certain problems specifically when we try to perform some analysis over the registers, or in the other side, if the application have multiple instances running, the scenario becomes even more complex.

On Docker v1.6, the concept of [**logging drivers**](https://docs.docker.com/engine/admin/logging/overview/) was introduced, which means that the Docker engine is aware about output interfaces that manage the application messages.

![](http://www.fluentd.org/assets/img/recipes/fluentd_docker.png)

For Docker v1.8, we have implemented a native [**Fluentd Docker logging driver**](https://docs.docker.com/engine/admin/logging/fluentd/), so now you are able to have an unified and structured logging system with the simplicity and high performance [Fluentd](http://fluentd.org).

Currently, fluentd logging driver doesn't support sub-second precision.

## Getting Started

Using the Docker logging mechanism with [Fluentd](http://www.fluentd.org) is a straighforward step, to get started make sure you have the following prerequisites:

* A basic understanding of [Fluentd](http://www.fluentd.org)
* A basic understanding of Docker
* A basic understanding of [Docker logging drivers](https://docs.docker.com/engine/admin/logging/overview/)
* Docker v1.8+

This article launches Fluentd as standard process, not a container. Please refer [Docker Logging via EFK (Elasticsearch + Fluentd + Kibana) Stack with Docker Compose](https://docs.fluentd.org/articles/docker-logging-efk-compose) for fully containerized environment tutorial.

### Step 1: Create the Fluentd configuration file

The first step is to prepare Fluentd to listen for the messsages that will receive from the Docker containers, for a demonstration purposes we will instruct Fluentd to write the messages to the standard output; In a later step you will find how to accomplish the same aggregating the logs into a MongoDB instance.

Create a simple file called in\_docker.conf which contains the following entries:

```
<source>
  @type forward
  port 24224
  bind 0.0.0.0
</source>

<match *>
  @type stdout
</match>
```

### Step 2: Start Fluentd

With this simple command start an instance of Fluentd:

```
$ fluentd -c in_docker.conf
```

If the service started you should see an output like this:

```
$ fluentd -c in_docker.conf
2019-07-22 12:20:36 +0900 [info]: parsing config file is succeeded path="in_docker.conf"
2019-07-22 12:20:36 +0900 [info]: using configuration file: <ROOT>
  <source>
    @type forward
    port 24224
    bind "0.0.0.0"
  </source>
  <match *>
    @type stdout
  </match>
</ROOT>
2019-07-22 12:20:36 +0900 [info]: starting fluentd-1.4.2 pid=91035 ruby="2.6.3"
2019-07-22 12:20:36 +0900 [info]: spawn command to main:  cmdline=["/Users/yuta.iwama/.rbenv/versions/2.6.3/bin/ruby", "-Eascii-8bit:ascii-8bit", "-rbundler/setup", "/Users/yuta.iwama/src/github.com/ganmacs/fluentd-confs/vendor/bundle/ruby/2.6.0/bin/fluentd", "-c", "in_docker.conf", "--under-supervisor"]
2019-07-22 12:20:36 +0900 [info]: gem 'fluentd' version '1.4.2'
2019-07-22 12:20:36 +0900 [info]: adding match pattern="*.*" type="stdout"
2019-07-22 12:20:36 +0900 [info]: adding source type="forward"
2019-07-22 12:20:36 +0900 [info]: #0 starting fluentd worker pid=91048 ppid=91035 worker=0
2019-07-22 12:20:36 +0900 [info]: #0 listening port port=24224 bind="0.0.0.0"
2019-07-22 12:20:36 +0900 [info]: #0 fluentd worker is now running worker=0
```

### Step 3: Start Docker container with Fluentd driver

By default, the Fluentd logging driver will try to find a local Fluentd instance (step #2) listening for connections on the TCP port 24224, note that the container will not start if it cannot connect to the Fluentd instance.

![](https://www.fluentd.org/assets/img/recipes/fluentd_docker_integrated.png)

The following command will run a base Ubuntu container and print some messages to the standard output, note that we have launched the container specifying the Fluentd logging driver:

```
$ docker run --log-driver=fluentd ubuntu echo "Hello Fluentd!"
Hello Fluentd!
```

### Step 4: Confirm

Now on the Fluentd output, you will see the incoming message from the container, e.g:

```
2019-07-22 03:32:42.000000000 +0000 499e83386347: {"source":"stdout","log":"Hello Fluentd!","container_id":"499e833863479de2c4a3639d0cf5aeb36333d438a42bb0959f6ed104e41354b1","container_name":"/kind_lamarr"}
```

At this point you will notice something interesting, the incoming messages have a timestamp, are tagged with the container\_id and contains general information from the source container along the message, everything in JSON format.

### Additional Step 1: Parse log message

Application log is stored into `"log"` field in the record. You can parse this log by using [filter\_parser](http://docs.fluentd.org/articles/filter_parser) filter before send to destinations.

```
<filter docker.**>
  @type parser
  format json # apache2, nginx, etc...
  key_name log
  reserve_data true
</filter>
```

Original event:

```
2019-07-22 03:36:39.000000000 +0000 6e8a14315069: {"log":"{\"key\":\"value\"}","container_id":"6e8a1431506936b8568a284f2b0dd4853c250ad85ab7a497f05c4d371f6c3ae6","container_name":"/laughing_beaver","source":"stdout"}
```

Filtered event:

```
2019-07-22 03:35:59.395952500 +0000 bac5426337a6: {"container_id":"bac5426337a611fc3b7a0b318c3c45981d2acd80f5c5651088bebb8f1f962583","container_name":"/nostalgic_euler","source":"stdout","log":"{\"key\":\"value\"}","key":"value"}
```

### Additional Step 2: Concatenate multiple lines log messages

Application log is stored into `"log"` field in the records. You can concatenate these logs by using [fluent-plugin-concat](https://github.com/fluent-plugins-nursery/fluent-plugin-concat) filter before send to destinations.

```
<filter docker.**>
  @type concat
  key log
  stream_identity_key container_id
  multiline_start_regexp /^-e:2:in `\/'/
  multiline_end_regexp /^-e:4:in/
</filter>
```

Original events:

```
2016-04-13 14:45:55 +0900 docker.28cf38e21204: {"container_id":"28cf38e212042225f5f80a56fac08f34c8f0b235e738900c4e0abcf39253a702","container_name":"/romantic_dubinsky","source":"stdout","log":"-e:2:in `/'"}
2016-04-13 14:45:55 +0900 docker.28cf38e21204: {"source":"stdout","log":"-e:2:in `do_division_by_zero'","container_id":"28cf38e212042225f5f80a56fac08f34c8f0b235e738900c4e0abcf39253a702","container_name":"/romantic_dubinsky"}
2016-04-13 14:45:55 +0900 docker.28cf38e21204: {"source":"stdout","log":"-e:4:in `<main>'","container_id":"28cf38e212042225f5f80a56fac08f34c8f0b235e738900c4e0abcf39253a702","container_name":"/romantic_dubinsky"}
```

Filtered events:

```
2016-04-13 14:45:55 +0900 docker.28cf38e21204: {"container_id":"28cf38e212042225f5f80a56fac08f34c8f0b235e738900c4e0abcf39253a702","container_name":"/romantic_dubinsky","source":"stdout","log":"-e:2:in `/'\n-e:2:in `do_division_by_zero'\n-e:4:in `<main>'"}
```

If the logs are typical stacktraces, consider [detect-exceptions plugin](https://github.com/GoogleCloudPlatform/fluent-plugin-detect-exceptions) instead.

## Driver options

The [Fluentd logging driver](https://docs.docker.com/engine/admin/logging/fluentd/) support more options through the *--log-opt* Docker command line argument:

* fluentd-address
* tag

#### fluentd-address

Specify an optional address for Fluentd, it allows to set the host and TCP port, e.g:

```
$ docker run --log-driver=fluentd --log-opt fluentd-address=192.168.2.4:24225 ubuntu echo "..."
```

#### tag

[Tags](https://docs.docker.com/engine/admin/logging/log_tags/) are a major requirement on Fluentd, they allows to identify the incoming data and take routing decisions. By default the Fluentd logging driver uses the container\_id as a tag (64 character ID), you can change it value with the *tag* option as follows:

```
$ docker run --log-driver=fluentd --log-opt tag=docker.my_new_tag ubuntu echo "..."
```

Additionally this option allows to specify some internal variables: {{.ID}}, {{.FullID}} or {{.Name}}. e.g:

```
$ docker run --log-driver=fluentd --log-opt tag=docker.{{.ID}} ubuntu echo "..."
```

## Development Environments

In a more real-world use case, you would want to use something other than the Fluentd standard output to store Docker containers messages, such as Elasticsearch, MongoDB, HDFS, S3, Google Cloud Storage and so on.

This document describes how to set up multi-container logging environment via EFK (Elasticsearch, Fluentd, Kibana) with Docker Compose.

* [Docker Logging via EFK (Elasticsearch + Fluentd + Kibana) Stack with Docker Compose](https://docs.fluentd.org/articles/docker-logging-efk-compose)

## Production Environments

In production environment, you must use one of the container orchestration tools. Currently, Kubernetes has better integration with Fluentd, and we're working on making better integrations with other tools as well.

* [Kubernetes's Logging Overview](https://kubernetes.io/docs/user-guide/logging/overview/)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Docker Compose

This article explains how to collect [Docker](https://www.docker.com/) logs to EFK (Elasticsearch + Fluentd + Kibana) stack. The example uses [Docker Compose](https://docs.docker.com/compose/) for setting up multiple containers.

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-Lk7cBlK-Nhj6kCsg9Nq%2F-Lk7cYP51y4U0jtuDvmX%2Fkibana5-screenshot.png?generation=1563512956077108\&alt=media)

[Elasticsearch](https://www.elastic.co/products/elasticsearch) is an open source search engine known for its ease of use. [Kibana](https://www.elastic.co/products/kibana) is an open source Web UI that makes Elasticsearch user friendly for marketers, engineers and data scientists alike.

By combining these three tools EFK (Elasticsearch + Fluentd + Kibana) we get a scalable, flexible, easy to use log collection and analytics pipeline. In this article, we will set up 4 containers, each includes:

* [Apache HTTP Server](https://hub.docker.com/_/httpd/)
* [Fluentd](https://hub.docker.com/r/fluent/fluentd/)
* [Elasticsearch](https://hub.docker.com/_/elasticsearch/)
* [Kibana](https://hub.docker.com/_/kibana/)

All of `httpd`'s logs will be ingested into Elasticsearch + Kibana, via Fluentd.

## Prerequisites: Docker

Please download and install Docker / Docker Compose. Well, that's it :)

* [Docker Installation](https://docs.docker.com/engine/installation/)

## Step 0: prepare docker-compose.yml

First, please prepare `docker-compose.yml` for [Docker Compose](https://docs.docker.com/compose/overview/). Docker Compose is a tool for defining and running multi-container Docker applications.

With the YAML file below, you can create and start all the services (in this case, Apache, Fluentd, Elasticsearch, Kibana) by one command.

```
version: '2'
services:
  web:
    image: httpd
    ports:
      - "80:80"
    links:
      - fluentd
    logging:
      driver: "fluentd"
      options:
        fluentd-address: localhost:24224
        tag: httpd.access

  fluentd:
    build: ./fluentd
    volumes:
      - ./fluentd/conf:/fluentd/etc
    links:
      - "elasticsearch"
    ports:
      - "24224:24224"
      - "24224:24224/udp"

  elasticsearch:
    image: elasticsearch
    expose:
      - 9200
    ports:
      - "9200:9200"

  kibana:
    image: kibana
    links:
      - "elasticsearch"
    ports:
      - "5601:5601"
```

`logging` section (check [Docker Compose documentation](https://docs.docker.com/compose/compose-file/#/logging)) of `web` container specifies [Docker Fluentd Logging Driver](https://docs.docker.com/engine/admin/logging/fluentd/) as a default container logging driver. All of the logs from `web` container will be automatically forwarded to host:port specified by `fluentd-address`.

## Step 1: Prepare Fluentd image with your Config + Plugin

Then, please prepare `fluentd/Dockerfile` with the following content, to use Fluentd's [official Docker image](https://hub.docker.com/r/fluent/fluentd/) and additionally install Elasticsearch plugin.

```
# fluentd/Dockerfile
FROM fluent/fluentd:v0.12-debian
RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-rdoc", "--no-ri", "--version", "1.9.2"]
```

Then, please prepare Fluentd's configuration file `fluentd/conf/fluent.conf`. [in\_forward](https://docs.fluentd.org/container-deployment/broken-reference) plugin is used for receive logs from Docker logging driver, and out\_elasticsearch is for forwarding logs to Elasticsearch.

```
# fluentd/conf/fluent.conf
<source>
  @type forward
  port 24224
  bind 0.0.0.0
</source>
<match *.**>
  @type copy
  <store>
    @type elasticsearch
    host elasticsearch
    port 9200
    logstash_format true
    logstash_prefix fluentd
    logstash_dateformat %Y%m%d
    include_tag_key true
    type_name access_log
    tag_key @log_name
    flush_interval 1s
  </store>
  <store>
    @type stdout
  </store>
</match>
```

## Step 2: Start Containers

Let's start all of the containers, with just one command.

```
$ docker-compose up
```

You can check to see if 4 containers are running by `docker ps` command.

```
$ docker ps
CONTAINER ID        IMAGE                      COMMAND                  CREATED             STATUS              PORTS                                                          NAMES
2d28323d77a3        httpd                      "httpd-foreground"       About an hour ago   Up 43 seconds       0.0.0.0:80->80/tcp                                             dockercomposeefk_web_1
a1b15a7210f6        dockercomposeefk_fluentd   "/bin/sh -c 'exec ..."   About an hour ago   Up 45 seconds       5140/tcp, 0.0.0.0:24224->24224/tcp, 0.0.0.0:24224->24224/udp   dockercomposeefk_fluentd_1
01e43b191cc1        kibana                     "/docker-entrypoin..."   About an hour ago   Up 45 seconds       0.0.0.0:5601->5601/tcp                                         dockercomposeefk_kibana_1
b7b439415898        elasticsearch              "/docker-entrypoin..."   About an hour ago   Up 50 seconds       0.0.0.0:9200->9200/tcp, 9300/tcp                               dockercomposeefk_elasticsearch_1
```

## Step 3: Generate httpd Access Logs

Let's access to `httpd` to generate some access logs. `curl` command is always your friend.

```
$ repeat 10 curl http://localhost:80/
<html><body><h1>It works!</h1></body></html>
<html><body><h1>It works!</h1></body></html>
<html><body><h1>It works!</h1></body></html>
<html><body><h1>It works!</h1></body></html>
<html><body><h1>It works!</h1></body></html>
<html><body><h1>It works!</h1></body></html>
<html><body><h1>It works!</h1></body></html>
<html><body><h1>It works!</h1></body></html>
<html><body><h1>It works!</h1></body></html>
<html><body><h1>It works!</h1></body></html>
```

## Step 4: Confirm Logs from Kibana

Please go to `http://localhost:5601/` with your browser. Then, you need to set up the index name pattern for Kibana. Please specify `fluentd-*` to `Index name or pattern` and press `Create` button.

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-Lk7cBlK-Nhj6kCsg9Nq%2F-Lk7cZKQksrc5aSVaLjH%2Fefk-kibana-1.png?generation=1563512956992433\&alt=media)

Then, go to `Discover` tab to seek for the logs. As you can see, logs are properly collected into Elasticsearch + Kibana, via Fluentd.

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-Lk7cBlK-Nhj6kCsg9Nq%2F-Lk7cZKSZp6XoEr5kTkx%2Fefk-kibana-2.png?generation=1563512974310491\&alt=media)

## Conclusion

This article explains how to collect logs from Apache to EFK (Elasticsearch + Fluentd + Kibana). The example code is available in this repository.

* <https://github.com/kzk/docker-compose-efk>

## Learn More

* [Fluentd Architecture](https://www.fluentd.org/architecture)
* [Fluentd Get Started](https://docs.fluentd.org/container-deployment/broken-reference)
* [Downloading Fluentd](http://www.fluentd.org/download)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Kubernetes

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LWNPJuIG9Ym5ELlFCti%2F-LWNPNc_sauS5nBsx4bE%2Ffluentd_kubernetes.png?generation=1547671553339032\&alt=media)

[Kubernetes](http://kubernetes.io) provides two logging end-points for applications and cluster logs: Stackdriver Logging for use with Google Cloud Platform and Elasticsearch. Behind the scenes there is a logging agent that take cares of log collection, parsing and distribution: [Fluentd](http://www.fluentd.org).

The following document focus on how to deploy Fluentd in Kubernetes and extend the possibilities to have different destinations for your logs.

## Getting Started

The following document assumes that you have a Kubernetes cluster running or at least a local (single) node that can be used for testing purposes.

Before to get started, make sure you understand or have a basic idea about the following concepts from Kubernetes:

* [Node](https://kubernetes.io/docs/admin/node/)

  > A node is a worker machine in Kubernetes, previously known as a minion. A node may be a VM or physical machine, depending on the cluster. Each node has the services necessary to run pods and is managed by the master components...
* [Pod](https://kubernetes.io/docs/user-guide/pods/)

  > A pod (as in a pod of whales or pea pod) is a group of one or more containers (such as Docker containers), the shared storage for those containers, and options about how to run the containers. Pods are always co-located and co-scheduled, and run in a shared context...
* [DaemonSet](https://kubernetes.io/docs/admin/daemons/)

  > A DaemonSet ensures that all (or some) nodes run a copy of a pod. As nodes are added to the cluster, pods are added to them. As nodes are removed from the cluster, those pods are garbage collected. Deleting a DaemonSet will clean up the pods it created...

Since applications runs in Pods and multiple Pods might exists across multiple nodes, we need a specific Fluentd-Pod that takes care of log collection on each node: [Fluentd DaemonSet](https://github.com/fluent/fluentd-docs-gitbook/tree/507e377b7e8e78a312dc49e76bd9a302c33fd058/articles/fluentd_daemonset.md).

## Fluentd DaemonSet

For [Kubernetes](https://kubernetes.io), a [DaemonSet](https://kubernetes.io/docs/admin/daemons/) ensures that all (or some) nodes run a copy of a *pod*. In order to solve log collection we are going to implement a Fluentd DaemonSet.

Fluentd is flexible enough and have the proper plugins to distribute logs to different third party applications like databases or cloud services, so the principal question is to know: *where the logs will be stored ?*. Once we got that question answered, we can move forward configuring our DaemonSet.

The below steps will focus on sending the logs to a Elasticsearch Pod.

### Get Fluentd DaemonSet sources

We have created a Fluentd DaemonSet that have the proper rules and container image ready to get started:

* <https://github.com/fluent/fluentd-kubernetes-daemonset>

Please grab a copy of the repository from the command line using GIT:

```
$ git clone https://github.com/fluent/fluentd-kubernetes-daemonset
```

### DaemonSet Content

The cloned repository contains the several configurations that allow to deploy Fluentd as a DaemonSet, the Docker container image distributed on the repository also comes pre-configured so Fluentd can gather all logs from the Kubernetes node environment and also it appends the proper metadata to the logs.

This repository has several presets for alpine/debian with popular outputs.

* [DaemonSet preset settings](https://github.com/fluent/fluentd-kubernetes-daemonset/tree/master/docker-image/v0.12)

## Logging to Elasticsearch

### Requirements

From the fluentd-kubernetes-daemonset/ directory, find the Yaml configuration file:

* [fluentd-daemonset-elasticsearch.yaml](https://github.com/fluent/fluentd-kubernetes-daemonset/blob/master/fluentd-daemonset-elasticsearch.yaml)

As an example let's see a part of the file content:

```
apiVersion: extensions/v1beta1
kind: DaemonSet
metadata:
  name: fluentd
  namespace: kube-system
  ...
spec:
    ...
    spec:
      containers:
      - name: fluentd
        image: quay.io/fluent/fluentd-kubernetes-daemonset
        env:
          - name:  FLUENT_ELASTICSEARCH_HOST
            value: "elasticsearch-logging"
          - name:  FLUENT_ELASTICSEARCH_PORT
            value: "9200"
        ...
```

The Yaml file have two relevant environment variables that are used by Fluentd when the container starts:

| Environment Variable        | Description                          | Default               |
| --------------------------- | ------------------------------------ | --------------------- |
| FLUENT\_ELASTICSEARCH\_HOST | Specify the host name or IP address. | elasticsearch-logging |
| FLUENT\_ELASTICSEARCH\_PORT | Elasticsearch TCP port               | 9200                  |

Any relevant change needs to be done to the Yaml file before to deploy it. Using the default values assumes that at least an Elasticsearch Pod **elasticsearch-logging** exists in the cluster.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Input Plugins

Fluentd has 6 types of plugins: [Input](https://docs.fluentd.org/input), [Parser](https://docs.fluentd.org/parser), [Filter](https://docs.fluentd.org/filter), [Output](https://docs.fluentd.org/output), [Formatter](https://docs.fluentd.org/formatter) and [Buffer](https://docs.fluentd.org/buffer). This article gives an overview of Input Plugin.

## Overview

Input plugins extend Fluentd to retrieve and pull event logs from external sources. An input plugin typically creates a thread socket and a listen socket. It can also be written to periodically pull data from data sources.

## List of Input Plugins

* [in\_forward](https://docs.fluentd.org/input/forward)
* [in\_unix](https://docs.fluentd.org/input/unix)
* [in\_http](https://docs.fluentd.org/input/http)
* [in\_tail](https://docs.fluentd.org/input/tail)
* [in\_exec](https://docs.fluentd.org/input/exec)
* [in\_syslog](https://docs.fluentd.org/input/syslog)

## Other Input Plugins

Please refer to this list of available plugins to find out about other Input plugins.

* [Fluentd plugins](http://fluentd.org/plugin/)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# tail

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LWyDIvT7Z7M06Hdqznf%2F-LWNPOu-hh314qQErrMR%2Ftail.png?generation=1548305927027164\&alt=media)

The `in_tail` Input plugin allows Fluentd to read events from the tail of text files. Its behavior is similar to the `tail -F` command.

## Example Configuration

`in_tail` is included in Fluentd's core. No additional installation process is required.

```
<source>
  @type tail
  path /var/log/httpd-access.log
  pos_file /var/log/td-agent/httpd-access.log.pos
  tag apache.access
  format apache2
</source>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

### How it Works

* When Fluentd is first configured with `in_tail`, it will start

  reading from the **tail** of that log, not the beginning.
* Once the log is rotated, Fluentd starts reading the new file from

  the beginning. It keeps track of the current inode number.
* If `td-agent` restarts, it starts reading from the last position

  td-agent read before the restart. This position is recorded in the

  position file specified by the pos\_file parameter.

## Parameters

### type (required)

The value must be `tail`.

### tag (required)

The tag of the event.

`*` can be used as a placeholder that expands to the actual file path, replacing '/' with '.'. For example, if you have the following configuration

```
path /path/to/file
tag foo.*
```

in\_tail emits the parsed events with the 'foo.path.to.file' tag.

### path (required)

The paths to read. Multiple paths can be specified, separated by ','.

`*` and strftime format can be included to add/remove watch file dynamically. At interval of `refresh_interval`, Fluentd refreshes the list of watch file.

```
path /path/to/%Y/%m/%d/*
```

If the date is 20140401, Fluentd starts to watch the files in /path/to/2014/04/01 directory. See also `read_from_head` parameter.

You should not use \\'\*\\' with log rotation because it may cause the log duplication. In such case, you should separate in\_tail plugin configuration.

### exclude\_path

The paths to exclude the files from watcher list. For example, if you want to remove compressed files, you can use following pattern.

```
path /path/to/*
exclude_path ["/path/to/*.gz", "/path/to/*.zip"]
```

### refresh\_interval

The interval of refreshing the list of watch file. Default is 60 seconds.

### limit\_recently\_modified

This parameter is available since v0.12.33.

Limit the watching files that the modification time is within the specified time range when use `*` in `path` parameter.

### skip\_refresh\_on\_startup

This parameter is available since v0.12.33.

Skip the refresh of watching list on startup. This reduces the start up time when use `*` in `path`.

### read\_from\_head

Start to read the logs from the head of file, not bottom. The default is `false`.

If you want to tail all contents with `*` or strftime dynamic path, set this parameter to `true`. Instead, you should guarantee that log rotation will not occur in `*` directory.

When this is true, in\_tail tries to read a file during start up phase. If target file is large, it takes long time and starting other plugins isn't executed until reading file is finished.

### encoding, from\_encoding

Specify the encoding of reading lines. The default is ASCII-8BIT.

By default, in\_tail emits string value as ASCII-8BIT encoding. These options change it.

* If specify only `encoding`, in\_tail changes string to `encoding`.

  This use ruby's

  [String#force\_encoding](https://docs.ruby-lang.org/en/trunk/String.html#method-i-force_encoding)
* If specify `encoding` and `from_encoding`, in\_tail tries to encode

  string from `from_encoding` to `encoding`. This uses ruby's

  [String#encode](https://docs.ruby-lang.org/en/trunk/String.html#method-i-encode)

You can get supported encoding list by typing following command:

```
$ ruby -e 'p Encoding.name_list.sort'
```

### read\_lines\_limit

The number of reading lines at each IO. Default is 1000 lines.

If you see "Size of the emitted data exceeds buffer\_chunk\_limit." log with in\_tail, set smaller value.

### multiline\_flush\_interval

The interval of flushing the buffer for multiline format. The default is disabled.

If you set `multiline_flush_interval 5s`, in\_tail flushes buffered event after 5 seconds from last emit. This option is useful when you use `format_firstline` option. Since v0.12.20 or later.

### pos\_file (highly recommended)

This parameter is highly recommended. Fluentd will record the position it last read into this file.

```
pos_file /var/log/td-agent/tmp/access.log.pos
```

`pos_file` handles multiple positions in one file so no need multiple `pos_file` parameters per `source`.

Don't share pos\_file between in\_tail configurations. It causes unexpected behavior, e.g. corrupt pos\_file content.

in\_tail removes untracked file position during startup phase. It means the content of pos\_file is growing until restart when you tails lots of files with dynamic path setting. I will fix this problem in the future. Check [this issue](https://github.com/fluent/fluentd/issues/1126).

### format (required)

The format of the log. `in_tail` uses parser plugin to parse the log. See [parser article](https://docs.fluentd.org/parser) for more detail.

### path\_key

Add watching file path to `path_key` field.

```
path /path/to/access.log
path_key tailed_path
```

With this config, generated events are like `{"tailed_path":"/path/to/access.log","k1":"v1",...,"kN":"vN"}`.

### rotate\_wait

in\_tail actually does a bit more than `tail -F` itself. When rotating a file, some data may still need to be written to the old file as opposed to the new one.

in\_tail takes care of this by keeping a reference to the old file (even after it has been rotated) for some time before transitioning completely to the new file. This helps prevent data designated for the old file from getting lost. By default, this time interval is 5 seconds.

The rotate\_wait parameter accepts a single integer representing the number of seconds you want this time interval to be.

### enable\_watch\_timer

Enable the additional watch timer. Setting this parameter to `false` will significantly reduce CPU and I/O consumption when tailing a large number of files on systems with inotify support. The default is `true` which results in an additional 1 second timer being used.

`in_tail` (via Cool.io) uses inotify on systems which support it. Earlier versions of libev on some platforms (eg Mac OS X) did not work properly; therefore, an explicit 1 second timer was used. Even on systems with inotify support, this results in additional I/O each second, for every file being tailed.

Early testing demonstrates that modern Cool.io and `in_tail` work properly without the additional watch timer. At some point in the future, depending on feedback and testing, the additional watch timer may be disabled by default.

### ignore\_repeated\_permission\_error

If you hard to exclude non-permision files from watching list, set this parameter to `true`. It suppress repeated permission error logs.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

## FAQ

### in\_tail doesn't start to read log file, why?

`in_tail` follows `tail -F` command behaviour by default, so `in_tail` reads only newer logs. If you want to read existing lines for batch use case, set `read_from_head true`.

### logrotate setting

`logrotate` has `nocreate` parameter and it doesn't create new file after triggered log rotation. It means `in_tail` can't find new file to tail.

This parameter doesn't fit typical application log cases, so check your `logrotate` setting which doesn't include `nocreate` parameter.

### What happens when in\_tail receives BufferQueueLimitError?

in\_tail stops reading new lines and pos file update until BufferQueueLimitError is resolved. After resolved BufferQueueLimitError, restart emitting new lines and pos file update.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# forward

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LX4w0SBbRIFelg25IS1%2F-LX0b10k08qLViJOflDQ%2Fforward.png?generation=1548435348479500\&alt=media)

The `in_forward` Input plugin listens to a TCP socket to receive the event stream. It also listens to an UDP socket to receive heartbeat messages.

This plugin is mainly used to receive event logs from other Fluentd instances, the fluent-cat command, or client libraries. This is by far the most efficient way to retrieve the records. Do **NOT** use this plugin for inter-DC or public internet data transfer without secure connections. To provide the reliable / low-latency transfer, we assume this plugin is only used within private networks.

If you open up the port of this plugin to the internet, the attacker can easily crash Fluentd by using the specific packet. If you require a secure connection between nodes, please consider using [in\_secure\_forward](https://docs.fluentd.org/input/secure_forward).

## Example Configuration

`in_forward` is included in Fluentd's core. No additional installation process is required.

```
<source>
  @type forward
  port 24224
  bind 0.0.0.0
</source>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

## Parameters

### type (required)

The value must be `forward`.

### port

The port to listen to. Default Value = 24224

### bind

The bind address to listen to. Default Value = 0.0.0.0 (all addresses)

### linger\_timeout

The timeout time used to set linger option. The default is 0

### chunk\_size\_limit

The size limit of the the received chunk. If the chunk size is larger than this value, then the received chunk is dropped. The default is nil (no limit).

### chunk\_size\_warn\_limit

The warning size limit of the received chunk. If the chunk size is larger than this value, a warning message will be sent. The default is nil (no warning).

### skip\_invalid\_event (v0.12.20 or later)

Skip an event if incoming event is invalid. The default is false.

This option is useful at forwarder, not aggragator. v0.12.20 or later.

### source\_hostname\_key (v0.12.28 or later)

The field name of the client's hostname. If set the value, the client's hostname will be set to its key. The default is nil (no adding hostname).

This iterates incoming events. So if you sends larger chunks to `in_forward`, it needs additional processing time.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

## Protocol

This plugin accepts both JSON or [MessagePack](http://msgpack.org/) messages and automatically detects which is used. Internally, Fluent uses MessagePack as it is more efficient than JSON.

The time value is a platform specific integer and is based on the output of Ruby's `Time.now.to_i` function. On Linux, BSD and MAC systems, this is the number of seconds since 1970.

Multiple messages may be sent in the same connection.

```
stream:
  message...

message:
  [tag, time, record]
  or
  [tag, [[time,record], [time,record], ...]]

example:
  ["myapp.access", 1308466941, {"a":1}]["myapp.messages", 1308466942, {"b":2}]
  ["myapp.access", [[1308466941, {"a":1}], [1308466942, {"b":2}]]]
```

### Communication with v1.0

v0.12 `in_forward` can't accept data from v1.0 `out_forward` because time format is different. If you want to forward data from v1.0 to v0.12, set `time_as_integer` in v1.0 `out_forward`.

## FAQ

### Why in\_forward doesn't have tag parameter?

`in_forward` uses `tag` of incoming events so no fixed `tag` parameter. See above "Protocol" section.

### How to parse incoming events?

`in_forward` doesn't provide parsing mechanism unlike `in_tail` or `in_tcp` because `in_forward` is mainly for efficient log transfer. If you want to parse incoming event, use [parser filter](https://github.com/tagomoris/fluent-plugin-parser) in your pipeline. See Docker logging driver usecase: [Docker Logging](http://www.fluentd.org/guides/recipes/docker-logging)

### I got MessagePack::UnknownExtTypeError error. Why?

This error happens when forwarder's fluentd is v0.14/v1.0 and receiver's fluentd is 0.12. To avoid this problem, set `time_as_integer` to `out_forward` setting in v0.14/v1.0 fluentd. See "Communication with v1.0".

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# secure\_forward

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN2biv5zzn1JBo8u1T%2F-LWNPOJb8nhIc4UEtHwx%2Fsecure_forward.png?generation=1548739338696876\&alt=media)

The `in_secure_forward` input plugin accepts messages via **SSL with authentication** (cf. [out\_secure\_forward](https://docs.fluentd.org/output/secure_forward)). This document doesn't describe all parameters. If you want to know full features, check the Further Reading section.

## Installation

`in_secure_forward` is **not** included in either `td-agent` package or `fluentd` gem. In order to install it, please refer to the [Plugin Management](https://docs.fluentd.org/deployment/plugin-management) article.

## Example Configurations

This section provides some example configurations for `in_secure_forward`.

### Minimalist Configuration

At first, generate private CA file by `secure-forward-ca-generate`, then copy that file to output plugin side by safe way (scp, or anyway else).

```
<source>
  @type secure_forward
  shared_key      secret_string
  self_hostname   server.fqdn.local  # This fqdn is used as CN (Common Name) of certificates
  secure true
  ca_cert_path        /path/to/certificate/ca_cert.pem
  ca_private_key_path /path/to/certificate/ca_key.pem
  ca_private_key_passphrase passphrase_for_private_CA_secret_key
</source>
```

### Check username/password from Clients

```
<source>
  @type secure_forward
  shared_key         secret_string
  self_hostname      server.fqdn.local
  secure true
  ca_cert_path        /path/to/certificate/ca_cert.pem
  ca_private_key_path /path/to/certificate/ca_key.pem
  ca_private_key_passphrase passphrase_for_private_CA_secret_key
  authentication     yes # Deny clients without valid username/password
  <user>
    username tagomoris
    password foobar012
  </user>
  <user>
    username frsyuki
    password yakiniku
  </user>
</source>
```

### Deny Unknown Source IP/hosts

```
<source>
  @type secure_forward
  shared_key         secret_string
  self_hostname      server.fqdn.local
  secure true
  ca_cert_path        /path/to/certificate/ca_cert.pem
  ca_private_key_path /path/to/certificate/ca_key.pem
  ca_private_key_passphrase passphrase_for_private_CA_secret_key
  allow_anonymous_source no  # Allow to accept from nodes of <client>
  <client>
    host 192.168.10.30
    # network address (ex: 192.168.10.0/24) NOT Supported now
  </client>
  <client>
    host your.host.fqdn.local
    # wildcard (ex: *.host.fqdn.local) NOT Supported now
  </client>
</source>
```

You can use the username/password check and client check together:

```
<source>
  @type secure_forward
  shared_key         secret_string
  self_hostname      server.fqdn.local
  secure true
  ca_cert_path        /path/to/certificate/ca_cert.pem
  ca_private_key_path /path/to/certificate/ca_key.pem
  ca_private_key_passphrase passphrase_for_private_CA_secret_key
  allow_anonymous_source no  # Allow to accept from nodes of <client>
  authentication         yes # Deny clients without valid username/password
  <user>
    username tagomoris
    password foobar012
  </user>
  <user>
    username frsyuki
    password sukiyaki
  </user>
  <user>
    username repeatedly
    password sushi
  </user
  <client>
    host 192.168.10.30      # allow all users to connect from 192.168.10.30
  </client>
  <client>
    host  192.168.10.31
    users tagomoris,frsyuki # deny repeatedly from 192.168.10.31
  </client>
  <client>
    host 192.168.10.32
    shared_key less_secret_string # limited shared_key for 192.168.10.32
    users      repeatedly         # and repeatedly only
  </client>
</source>
```

### Secure Sender-Receiver Setup

Please refer to the **Secure Sender-Receiver Setup** [sample documentation](https://docs.fluentd.org/output/secure_forward#Secure-Sender-Receiver-Setup).

## Parameters

### type

This parameter is required. Its value must be `secure_forward`.

### port (integer)

The default value is 24284.

### bind (string)

The default value is 0.0.0.0.

### secure (bool)

Indicate published connection is secure or not. Specify `yes` (or `true`) if secure encryption needed.

### self\_hostname (string)

Default value of the auto-generated certificate common name (CN).

### shared\_key (string)

Shared key between nodes.

### allow\_keepalive (bool)

Accept keepalive connection. The default value is `true`.

### allow\_anonymous\_source (bool)

Accept connections from unknown hosts.

### authentication (bool)

Require password authentication. The default value is `false`.

### ca\_cert\_path (string)

The path to the private CA certificate file, which is required to use private CA. (One of this parameter or `cert_path` is required for `secure yes` configuration.)

### ca\_private\_key\_path (string)

The path to the private key for private CA certificate key file.

### ca\_private\_key\_passphrase (string)

The passphrase string for private key file, specified by `ca_private_key_path`.

### read\_length (size)

The number of bytes read per nonblocking read. The default value is 8MB=8*1024*1024 bytes.

### read\_interval\_msec (integer)

The interval between the non-blocking reads, in milliseconds. The default value is 50.

### socket\_interval\_msec (integer)

The interval between SSL reconnects in milliseconds. The default value is 200.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

## Further Reading

* [fluent-plugin-secure-forward repository](https://github.com/tagomoris/fluent-plugin-secure-forward)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# udp

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN2biv5zzn1JBo8u1T%2F-LWNPR6ryWrwgpIBjth5%2Fudp.png?generation=1548739337535432\&alt=media)

The `in_udp` Input plugin enables Fluentd to accept UDP payload.

## Example Configuration

`in_udp` is included in Fluentd's core. No additional installation process is required.

```
<source>
  @type udp
  tag mytag # required
  format /^(?<field1>\d+):(?<field2>\w+)$/ # required
  port 20001 # optional. 5160 by default
  bind 0.0.0.0 # optional. 0.0.0.0 by default
  body_size_limit 1MB # optional. 4096 bytes by default
</source>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

We've observed the drastic performance improvements on Linux, with proper kernel parameter settings (e.g. \`net.core.rmem\_max\` parameter). If you have high-volume UDP traffic, please make sure to follow the instruction described at [Before Installing Fluentd](https://docs.fluentd.org/articles/before-install).

## Parameters

### type (required)

The value must be `udp`.

### tag (required)

tag of output events.

#### port

The port to listen to. Default Value = 5160

### bind

The bind address to listen to. Default Value = 0.0.0.0

### source\_hostname\_key

The field name of the client's hostname. If set the value, the client's hostname will be set to its key. The default is nil (no adding hostname).

If you set following configuration:

```
source_hostname_key client_host
```

then the client's hostname is set to `client_host` field.

```
{
    ...
    "foo": "bar",
    "client_host": "client.hostname.org"
}
```

### format (required)

The format of the UDP payload. `in_udp` uses parser plugin to parse the payload. See [parser article](https://docs.fluentd.org/parser) for more detail.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

## FAQ

### How to prevent request drop?

If in\_udp gots lots of packets within 1 sec, some packets are dropped. For example, you can see bigger RcvbufErrors number via `netstat -su`.

This means in\_udp with one process can't handle such traffic. Try [fluent-plugin-multiprocess](https://github.com/fluent/fluent-plugin-multiprocess) to resolve the problem. See [issue 1334](https://github.com/fluent/fluentd/issues/1334) for more detail.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# tcp

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LX0aKuKEQ8l83KlUg5z%2F-LWNPNp8xOgIEt_P8cTJ%2Ftcp.png?generation=1548362554751314\&alt=media)

The `in_tcp` Input plugin enables Fluentd to accept TCP payload.

Don't use this plugin for receiving logs from client libraries. Use `in_forward` for such cases.

## Example Configuration

`in_tcp` is included in Fluentd's core. No additional installation process is required.

```
<source>
  @type tcp
  tag tcp.events # required
  format /^(?<field1>\d+):(?<field2>\w+)$/ # required
  port 20001 # optional. 5170 by default
  bind 0.0.0.0 # optional. 0.0.0.0 by default
  delimiter \n # optional. \n (newline) by default
</source>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

We\\'ve observed the drastic performance improvements on Linux, with proper kernel parameter settings. If you have high-volume TCP traffic, please make sure to follow the instruction described at [Before Installing Fluentd](https://docs.fluentd.org/articles/before-install).

## Parameters

### type (required)

The value must be `tcp`.

### tag (required)

tag of output events.

### port

The port to listen to. Default Value = 5170

### bind

The bind address to listen to. Default Value = 0.0.0.0

### delimiter

The payload is read up to this character. By default, it is "\n".

### source\_hostname\_key

The field name of the client's hostname. If set the value, the client's hostname will be set to its key. The default is nil (no adding hostname).

If you set following configuration:

```
source_hostname_key client_host
```

then the client's hostname is set to `client_host` field.

```
{
    ...
    "foo": "bar",
    "client_host": "client.hostname.org"
}
```

### format (required)

The format of the TCP payload. Here is the example by regular expression.

```
format /^(?<field1>\d+):(?<field2>\w+)$/
```

If you execute following command:

```
$ echo '123456:awesome' | netcat 0.0.0.0 5170
```

then got parsed result like below:

```
{"field1":"123456","field2":"awesome}
```

`in_tcp` uses parser plugin to parse the payload. See [parser article](https://docs.fluentd.org/parser) for more detail.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# http

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LX0aKuKEQ8l83KlUg5z%2F-LWNPOId6AY-NZbmKavV%2Fhttp.png?generation=1548362563516894\&alt=media)

The `in_http` Input plugin enables Fluentd to retrieve records from HTTP POST. The URL path becomes the `tag` of the Fluentd event log and the POSTed body element becomes the record itself.

## Example Configuration

`in_http` is included in Fluentd's core. No additional installation process is required.

```
<source>
  @type http
  port 8888
  bind 0.0.0.0
  body_size_limit 32m
  keepalive_timeout 10s
</source>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

### Example Usage

The example below posts a record using the `curl` command.

```
$ curl -X POST -d 'json={"action":"login","user":2}'
  http://localhost:8888/test.tag.here;
```

## Parameters

### type (required)

The value must be `http`.

### port

The port to listen to. Default Value = 9880

### bind

The bind address to listen to. Default Value = 0.0.0.0 (all addresses)

### body\_size\_limit

The size limit of the POSTed element. Default Value = 32MB

### keepalive\_timeout

The timeout limit for keeping the connection alive. Default Value = 10 seconds

### add\_http\_headers

Add `HTTP_` prefix headers to the record. The default is `false`

### add\_remote\_addr

Add `REMOTE_ADDR` field to the record. The value of `REMOTE_ADDR` is the client's address. The default is `false`

If your system set multiple `X-Forwarded-For` headers in the request, `in_http` uses first one. For example:

```
X-Forwarded-For: host1, host2
X-Forwarded-For: host3
```

If send above multiple headers, `REMOTE_ADDR` value is `host1`.

### cors\_allow\_origins

White list domains for CORS. Default is no check.

If you set `["domain1", "domain2"]` to `cors_allow_origins`, `in_http` returns `403` to access from othe domains.

### format

The format of the HTTP body. The default is `default`.

* default

Accept records using `json=` / `msgpack=` style.

* regexp

Specify body format by regular expression.

```
format /^(?<field1>\d+):(?<field2>\w+)$/
```

If you execute following command:

```
$ curl -X POST -d '123456:awesome' "http://localhost:8888/test.tag.here"
```

then got parsed result like below:

```
{"field1":"123456","field2":"awesome}
```

`json`, `ltsv`, `tsv`, `csv` and `none` are also supported. Check [parser plugin overview](https://docs.fluentd.org/parser) for more details.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

## Additional Features

### time query parameter

If you want to pass the event time from your application, please use the `time` query parameter.

```
$ curl -X POST -d 'json={"action":"login","user":2}'
  "http://localhost:8888/test.tag.here?time=1392021185"
```

### Batch mode

If you use `default` format, then you can send array type of json / msgpack to in\_http.

```
$ curl -X POST -d 'json=[{"action":"login","user":2,"time":1392021185},{"action":"logout","user":2,"time":1392027356}]'
  http://localhost:8888/test.tag.here;
```

This improves the input performance by reducing HTTP access. Non `default` format doesn't support batch mode yet. Here is a simple bechmark result on MacBook Pro with ruby 2.3:

| json            | msgpack         | msgpack array(10 items) |
| --------------- | --------------- | ----------------------- |
| 2100 events/sec | 2400 events/sec | 10000 events/sec        |

Tested configuration and ruby script is [here](https://gist.github.com/repeatedly/672ac73abf7cbcb629aaec791838cf6d).

## FAQ

### Why in\_http removes '+' from my log?

This is HTTP spec, not fluentd problem. You need to encode your payload properly or use multipart request. Here is ruby example:

```
# OK
URI.encode_www_form({json: {"message" => "foo+bar"}.to_json})

# NG
"json=#{{"message" => "foo+bar"}.to_json}"
```

curl command example:

```
# OK
curl -X POST -H 'Content-Type: multipart/form-data' -F 'json={"message":"foo+bar"}' http://localhost:8888/test.tag.here

# NG
curl -X POST -F 'json={"message":"foo+bar"}' http://localhost:8888/test.tag.here
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# unix

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LWwh_8--1Ryw8aKcc_g%2F-LWNPQiUhR3aRmVTbAFG%2Funix.png?generation=1548280566526225\&alt=media)

The `in_unix` Input plugin enables Fluentd to retrieve records from the Unix Domain Socket. The wire protocol is the same as [in\_forward](https://docs.fluentd.org/input/forward), but the transport layer is different.

## Example Configuration

`in_unix` is included in Fluentd's core. No additional installation process is required.

```
<source>
  @type unix
  path /path/to/socket.sock
</source>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

## Parameters

### type (required)

The value must be `unix`.

### path (required)

The path to your Unix Domain Socket.

### backlog

The backlog of Unix Domain Socket. The default is `1024`.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# syslog

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LX0aKuKEQ8l83KlUg5z%2F-LWNPOan9s_faZVC4rLN%2Fsyslog.png?generation=1548362555327815\&alt=media)

The `in_syslog` Input plugin enables Fluentd to retrieve records via the syslog protocol on UDP or TCP.

## Example Configuration

`in_syslog` is included in Fluentd's core. No additional installation process is required.

```
<source>
  @type syslog
  port 5140
  bind 0.0.0.0
  tag system
</source>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

### Example Usage

The retrieved data is organized as follows. Fluentd's tag is generated by the `tag` parameter (tag prefix), [facility level](http://en.wikipedia.org/wiki/Syslog#Facility_Levels), and [priority](http://en.wikipedia.org/wiki/Syslog#Severity_levels). The record is parsed by the regexp [here](https://github.com/fluent/fluentd/blob/master/lib/fluent/plugin/in_syslog.rb#L25).

```
tag = "#{@tag}.#{facility}.#{priority}"

record = {
  "pri": "0",
  "time": 1353436518,
  "host": "host",
  "ident": "ident",
  "pid": "12345",
  "message": "text"
}
```

## Parameters

### type (required)

The value must be `syslog`.

### tag (required)

The prefix of the tag. The tag itself is generated by the tag prefix, [facility level](http://en.wikipedia.org/wiki/Syslog#Facility_Levels), and [priority](http://en.wikipedia.org/wiki/Syslog#Severity_levels).

### port

The port to listen to. Default Value = 5140

### bind

The bind address to listen to. Default Value = 0.0.0.0 (all addresses)

### protocol\_type

The transport protocol used to receive logs. "udp" and "tcp" are supported. "udp" by default.

### message\_length\_limit

The max bytes of syslog message. Default is `2048`. If you send larger message, change this parameter.

### message\_format

This parameter is available since v0.12.33.

Specify protocol format. Supported values are `rfc3164`, `rfc5424` and `auto`. Default is `rfc3164`. If your syslog uses `rfc5424`, use `rfc5424` instead. Here is an example of message:

```
# rfc3164
<6>Feb 28 12:00:00 192.168.0.1 fluentd[11111]: [error] Hello!
# rfc5424
<16>1 2017-02-28T12:00:00.009Z 192.168.0.1 fluentd - - - Hello!
```

`auto` is useful when `in_syslog` receives both `rfc3164` and `rfc5424` message per source. `in_syslog` detects message format by using message prefix and parse it.

### format

The format of the log. This option is used to parse non-standard syslog formats using [parser plugins](https://docs.fluentd.org/parser).

```
<source>
  @type syslog
  tag system
  format FORMAT_PARAMETER
</source>
```

Your `format` regexp should not consider the 'priority' prefix of the log. For example, if in\_syslog receives the log below:

```
 <1>Feb 20 00:00:00 192.168.0.1 fluentd[11111]: [error] hogehoge
```

then the format parser receives the following log:

```
 Feb 20 00:00:00 192.168.0.1 fluentd[11111]: [error] hogehoge
```

If the `format` parameter is missing, then the log data is assumed to have the canonical syslog format (see with\_priority).

### with\_priority

This option matters only when `format` is absent. If `with_priority` is true, then syslog messages are assumed to be prefixed with a priority tag like "\\". This option exists since some syslog daemons output logs without the priority tag preceding the message body.

If you wish to parse syslog messages of arbitrary formats, [in\_tcp](https://docs.fluentd.org/input/tcp) or [in\_udp](https://docs.fluentd.org/input/udp) are recommended.

### include\_source\_host

If true, add source host to event record. The default is `false`. This is deprecated. Use `source_hostname_key`.

### source\_hostname\_key

The field name of the client's hostname. If set the value, the client's hostname will be set to its key. The default is nil (no adding hostname).

### priority\_key

The field name of the priority. If set the value, the priority will be set to its key. The default is nil (no adding priority).

### facility\_key

The field name of the facility. If set the value, the facility will be set to its key. The default is nil (no adding facility).

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

## TCP protocol and message delimiter

This plugin assumes `\n` for delimiter character between syslog messages in one TCP connection. If you use syslog library in your application with `protocol_type tcp`, add `\n` to your syslog message. See also [rfc6587](https://tools.ietf.org/html/rfc6587#section-3.4.2).

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# exec

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LX0aKuKEQ8l83KlUg5z%2F-LWNPOKzGc--rilGU6Gf%2Fexec.png?generation=1548362554704824\&alt=media)

The `in_exec` Input plugin executes external programs to receive or pull event logs. It will then read TSV (tab separated values), JSON or MessagePack from the stdout of the program.

You can run a program periodically or permanently. To run periodically, please use the run\_interval parameter.

## Example Configuration

`in_exec` is included in Fluentd's core. No additional installation process is required.

```
<source>
  @type exec
  command cmd arg arg
  keys k1,k2,k3
  tag_key k1
  time_key k2
  time_format %Y-%m-%d %H:%M:%S
  run_interval 10s
</source>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

## Parameters

### type (required)

The value must be `exec`.

### command (required)

The command (program) to execute.

### format

The format used to map the program output to the incoming event.

The following formats are supported:

* tsv (default)
* json
* msgpack
* [parser plugin formats](https://docs.fluentd.org/parser), e.g. ltsv, none.

When using the tsv format, please also specify the comma-separated `keys` parameter.

```
keys k1,k2,k3
```

When using the json format, this plugin uses the Yajl library to parse the program output. Yajl buffers data internally so the output isn't always instantaneous.

### tag (required if tag\_key is not specified)

tag of the output events.

### tag\_key

The key to use as the event tag instead of the value in the event record. If this parameter is not specified, the `tag` parameter will be used instead.

### time\_key

The key to use as the event time instead of the value in the event record. If this parameter is not specified, the current time will be used instead.

### time\_format

The format of the event time used for the time\_key parameter. The default is UNIX time (integer).

### run\_interval

The interval time between periodic program runs. If no specify value, command script runs only once.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

## Real World Use Case: using in\_exec to scrape Hacker News Top Page

If you already have a script that runs periodically (say, via `cron`) that you wish to store the output to multiple backend systems (HDFS, AWS, Elasticsearch, etc.), in\_exec is a great choice.

The only requirement for the script is that it outputs TSV, JSON or MessagePack.

For example, the [following script](https://gist.github.com/kiyoto/1bd903ad1bdd6ac51fcc) scrapes the front page of [Hacker News](http://news.ycombinator.com) and scrapes information about each post:

Suppose that script is called `hn.rb`. Then, you can run it every 5 minutes with the following configuration

```
<source>
  @type exec
  format json
  tag hackernews
  command ruby /path/to/hn.rb
  run_interval 5m # don't hit HN too frequently!
</source>
<match hackernews>
  @type stdout
</match>
```

And if you run Fluentd with it, you will see the following output (if you are impatient, ctrl-C to flush the stdout buffer)

```
2014-05-26 21:51:35 +0000 hackernews: {"time":1401141095,"rank":1,"title":"Rap Genius Co-Founder Moghadam Fired","points":128,"user_name":"obilgic","duration":"2 hours ago  ","num_comments":108}
2014-05-26 21:51:35 +0000 hackernews: {"time":1401141095,"rank":2,"title":"Whitewood Under Siege: Wooden Shipping Pallets","points":128,"user_name":"drjohnson","duration":"3 hours ago  ","num_comments":20}
2014-05-26 21:51:35 +0000 hackernews: {"time":1401141095,"rank":3,"title":"Organic Cat Litter Chief Suspect In Nuclear Waste Accident","points":55,"user_name":"timr","duration":"2 hours ago  ","num_comments":12}
2014-05-26 21:51:35 +0000 hackernews: {"time":1401141095,"rank":4,"title":"Do We Really Know What Makes Us Healthy? (2007)","points":27,"user_name":"gwern","duration":"1 hour ago  ","num_comments":9}
```

Of course, you can use Fluentd's many output plugins to store the data into various backend systems like [Elasticsearch](https://docs.fluentd.org/articles/free-alternative-to-splunk-by-fluentd), [HDFS](https://docs.fluentd.org/articles/http-to-hdfs), [MongoDB](https://docs.fluentd.org/articles/apache-to-mongodb), [AWS](https://docs.fluentd.org/articles/apache-to-s3), etc.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# scribe

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LX0aKuKEQ8l83KlUg5z%2F-LWNPNnrAdA-dv6SFYHp%2Fscribe.png?generation=1548362555092809\&alt=media)

The `in_scribe` Input plugin enables Fluentd to retrieve records through the Scribe protocol. [Scribe](https://github.com/facebook/scribe) is another log collector daemon that is open-sourced by Facebook.

Since Scribe hasn't been well maintained recently, this plugin is useful for existing Scribe users who want to use Fluentd with an existing Scribe infrastructure.

## Install

`in_scribe` is included in td-agent by default. Fluentd gem users will need to install the fluent-plugin-scribe gem using the following command.

```
$ fluent-gem install fluent-plugin-scribe
```

## Example Configuration

```
<source>
  @type scribe
  port 1463

  bind 0.0.0.0
  msg_format json
</source>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

### Example Usage

We assume that you're already familiar with the Scribe protocol. This [Ruby example code](https://github.com/fluent/fluent-plugin-scribe/blob/master/bin/fluent-scribe-remote) posts logs to `in_scribe`.

Scribe's `category` field becomes the `tag` of the Fluentd event log and Scribe's `message` field becomes the record itself. The `msg_format` parameter specifies the format of the `message` field.

## Parameters

#### type (required)

The value must be `scribe`.

#### port

The port to listen to. Default Value = 1463

#### bind

The bind address to listen to. Default Value = 0.0.0.0 (all addresses)

#### msg\_format

The message format can be 'text', 'json', or 'url\_param' (default: text)

For `json`, Fluentd's record is organized as follows. Scribe's message field must be a valid JSON string representing Hash; otherwise, the record is ignored.

```
tag: $category
record: $message
```

For `text`, Fluentd's record is organized as follows. Scribe's message can be any arbitrary string, but JSON is recommended for ease of use with the subsequent analytics pipeline.

```
tag: $category
record: {'message': $message}
```

For `url_param`, Fluentd's record is organized as follows. Scribe's message field must contain URL parameter style key-value pairs with URL encoding (e.g. key1=val1\&key2=val2).

```
tag: $url_param
record: {$key1: $val1, $key2: $val2, ...}
```

#### is\_framed

Specifies whether to use Thrift's framed protocol or not (default: true).

#### server\_type

Chooses the server architecture. Options are 'simple', 'threaded', 'thread\_pool', or 'nonblocking' (default: nonblocking).

#### add\_prefix

The prefix string which will always be added to the tag (default: nil).

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# multiprocess

By default, Fluentd only uses a single CPU core on the system. The `in_multiprocess` Input plugin enables Fluentd to use multiple CPU cores by spawning multiple child processes. One Fluentd user is using this plugin to handle 10+ billion records / day.

## Install

`in_multiprocess` is NOT included in td-agent by default. td-agent users must install fluent-plugin-multiprocess manually.

* Fluentd: `fluent-gem install fluent-plugin-multiprocess`
* td-agent v2:

  `/usr/sbin/td-agent-gem install fluent-plugin-multiprocess`
* td-agent v1:

  `/usr/lib/fluent/ruby/bin/fluent-gem install fluent-plugin-multiprocess`

## Example Configuration

```
<source>
  @type multiprocess

  <process>
    cmdline -c /etc/fluent/fluentd_child1.conf --log /var/log/fluent/fluentd_child1.log
    sleep_before_start 1s
    sleep_before_shutdown 5s
  </process>
  <process>
    cmdline -c /etc/fluent/fluentd_child2.conf --log /var/log/fluent/fluentd_child2.log
    sleep_before_start 1s
    sleep_before_shutdown 5s
  </process>
  <process>
    cmdline -c /etc/fluent/fluentd_child3.conf --log /var/log/fluent/fluentd_child3.log
    sleep_before_start 1s
    sleep_before_shutdown 5s
  </process>
</source>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

Especially for daemonized fluentd (ex: td-agent), \`--log\` option MUST be specified to put logs of child processes.

## Parameters

### type (required)

The value must be `multiprocess`.

### graceful\_kill\_interval

The interval to send the signal to gracefully shut down the process (default: 2sec).

### graceful\_kill\_interval\_increment

The increment time, when graceful shutdown fails (default: 3sec).

### graceful\_kill\_timeout

The timeout, to identify the failure of graceful shutdown (default: 60sec).

### process (required)

The `process` section sets the command line arguments of a child process. This plugin creates one child process for each section.

### cmdline (required)

The `cmdline` option is required in a section

### sleep\_before\_start

This parameter sets the wait time before starting the process (default: 0sec).

### sleep\_before\_shutdown

This parameter sets the wait time before shutting down the process (default: 0sec).

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# dummy

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LX0aKuKEQ8l83KlUg5z%2F-LWNPOwwA91Q1GYDjciJ%2Fdummy.png?generation=1548362563677789\&alt=media)

The `in_dummy` input plugin generates dummy events. It is useful for testing, debugging, benchmarking and getting started with Fluentd.

## Example Configuration

`in_dummy` is included in Fluentd's core. No additional installation process is required.

```
<source>
  @type dummy
  dummy {"hello":"world"}
</source>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

## Parameters

### type (required)

The value must be `dummy`.

### tag (required)

The value is the tag assigned to the generated events.

### dummy (optional)

The dummy data to be generated. It should be either an array of JSON hashes or a single JSON hash. If it is an array of JSON hashes, the hashes in the array are cycled through in order. By default, the value is `[{"message":"dummy"}]` (i.e., it continues to generate events with the record {"message":"dummy"}).

### auto\_increment\_key (optional, string type)

If specified, each generated event has an auto-incremented key field. For example, with `auto_increment_key foo_key`, the first couple of events look like

```
2014-12-14 23:23:38 +0000 test: {"message":"dummy","foo_key":0}
2014-12-14 23:23:38 +0000 test: {"message":"dummy","foo_key":1}
2014-12-14 23:23:38 +0000 test: {"message":"dummy","foo_key":2}
```

### rate (optional, integer type)

It configures how many events to generate per second. The default value is 1.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Others

Please refer to this list of available plugins to find out about other Input plugins.

* [Fluentd plugins](http://fluentd.org/plugin/)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Output Plugins

Fluentd has 6 types of plugins: [Input](https://docs.fluentd.org/input), [Parser](https://docs.fluentd.org/parser), [Filter](https://docs.fluentd.org/filter), [Output](https://docs.fluentd.org/output), [Formatter](https://docs.fluentd.org/formatter) and [Buffer](https://docs.fluentd.org/buffer). This article gives an overview of Output Plugin.

## Overview

There are three types of output plugins: Non-Buffered, Buffered, and Time Sliced.

* *Non-Buffered* output plugins do not buffer data and immediately

  write out results.
* *Buffered* output plugins maintain a queue of chunks (a chunk is a

  collection of events), and its behavior can be tuned by the "chunk

  limit" and "queue limit" parameters (See the diagram below).
* *Time Sliced* output plugins are in fact a type of Bufferred plugin,

  but the chunks are keyed by time (See the diagram below).

![](http://image.slidesharecdn.com/fluentdmeetup-diveintofluentplugin-120203210125-phpapp02/95/slide-60-728.jpg)

The output plugin's buffer behavior (if any) is defined by a separate [Buffer plugin](https://docs.fluentd.org/buffer). Different buffer plugins can be chosen for each output plugin. Some output plugins are fully customized and do not use buffers.

## List of Non-Buffered Output Plugins

* [out\_copy](https://docs.fluentd.org/output/copy)
* [out\_null](https://docs.fluentd.org/output/null)
* [out\_roundrobin](https://docs.fluentd.org/output/roundrobin)
* [out\_stdout](https://docs.fluentd.org/output/stdout)

## List of Buffered Output Plugins

* [out\_exec\_filter](https://docs.fluentd.org/output/exec_filter)
* [out\_forward](https://docs.fluentd.org/output/forward)
* [out\_mongo](https://docs.fluentd.org/output/mongo) or [out\_mongo\_replset](https://docs.fluentd.org/output/mongo_replset)

## List of Time Sliced Output Plugins

* [out\_exec](https://docs.fluentd.org/output/exec)
* [out\_file](https://docs.fluentd.org/output/file)
* [out\_s3](https://docs.fluentd.org/output/s3)
* [out\_webhdfs](https://docs.fluentd.org/output/webhdfs)

## Other Plugins

Please refer to this list of available plugins to find out about other Output plugins.

* [others](http://fluentd.org/plugin/)

## Buffered Output Parameters

For advanced usage, you can tune Fluentd's internal buffering mechanism with these parameters.

### buffer\_type

The buffer type is `memory` by default ([buf\_memory](https://docs.fluentd.org/buffer/memory)) for the ease of testing, however `file` ([buf\_file](https://docs.fluentd.org/buffer/file)) buffer type is always recommended for the production deployments. If you use `file` buffer type, `buffer_path` parameter is required.

### buffer\_queue\_limit, buffer\_chunk\_limit

The length of the chunk queue and the size of each chunk, respectively. Please see the [Buffer Plugin Overview](https://docs.fluentd.org/buffer) article for the basic buffer structure. The default values are 64 and 8m, respectively. The suffixes "k" (KB), "m" (MB), and "g" (GB) can be used for buffer\_chunk\_limit.

### flush\_interval

The interval between data flushes. The default is 60s. The suffixes "s" (seconds), "m" (minutes), and "h" (hours) can be used.

### flush\_at\_shutdown

If set to true, Fluentd waits for the buffer to flush at shutdown. By default, it is set to true for Memory Buffer and false for File Buffer.

### retry\_wait, max\_retry\_wait

The initial and maximum intervals between write retries. The default values are 1.0 seconds and unset (no limit). The interval doubles (with +/-12.5% randomness) every retry until `max_retry_wait` is reached.

Since td-agent will retry 17 times before giving up by default (see the `retry_limit` parameter for details), the sleep interval can be up to approximately 131072 seconds (roughly 36 hours) in the default configurations.

### retry\_limit, disable\_retry\_limit

The limit on the number of retries before buffered data is discarded, and an option to disable that limit (if true, the value of `retry_limit` is ignored and there is no limit). The default values are 17 and false (not disabled). If the limit is reached, buffered data is discarded and the retry interval is reset to its initial value (`retry_wait`).

### num\_threads

The number of threads to flush the buffer. This option can be used to parallelize writes into the output(s) designated by the output plugin. Increasing the number of threads improves the flush throughput to hide write / network latency. The default is 1.

### slow\_flush\_log\_threshold

The threshold for checking chunk flush performance. The default value is `20.0` seconds. Note that parameter type is `float`, not `time`.

If chunk flush takes longer time than this threshold, fluentd logs warning message like below:

```
2016-12-19 12:00:00 +0000 [warn]: buffer flush took longer time than slow_flush_log_threshold: elapsed_time = 15.0031226690043695 slow_flush_log_threshold=10.0 plugin_id="foo"
```

### secondary output

At Buffered output plugin, the user can specify `<secondary>` with any output plugin in `<match>` configuration. If the retry count exceeds the buffer's `retry_limit` (and the retry limit has not been disabled via `disable_retry_limit`), then buffered chunk is output to `<secondary>` output plugin.

`<secondary>` is useful for backup when destination servers are unavailable, e.g. forward, mongo and other plugins. We strongly recommend `out_file` plugin for `<secondary>`.

## Time Sliced Output Parameters

For advanced usage, you can tune Fluentd's internal buffering mechanism with these parameters.

### time\_slice\_format

The time format used as part of the file name. The following characters are replaced with actual values when the file is created:

* \\%Y: year including the century (at least 4 digits)
* \\%m: month of the year (01..12)
* \\%d: Day of the month (01..31)
* \\%H: Hour of the day, 24-hour clock (00..23)
* \\%M: Minute of the hour (00..59)
* \\%S: Second of the minute (00..60)

The default format is `%Y%m%d%H`, which creates one file per hour.

### time\_slice\_wait

The amount of time Fluentd will wait for old logs to arrive. This is used to account for delays in logs arriving to your Fluentd node. The default wait time is 10 minutes ('10m'), where Fluentd will wait until 10 minutes past the hour for any logs that occurred within the past hour.

For example, when splitting files on an hourly basis, a log recorded at 1:59 but arriving at the Fluentd node between 2:00 and 2:10 will be uploaded together with all the other logs from 1:00 to 1:59 in one transaction, avoiding extra overhead. Larger values can be set as needed.

### buffer\_type

The buffer type is `file` by default ([buf\_file](https://docs.fluentd.org/buffer/file)). The `memory` ([buf\_memory](https://docs.fluentd.org/buffer/memory)) buffer type can be chosen as well. If you use `file` buffer type, `buffer_path` parameter is required.

### buffer\_queue\_limit, buffer\_chunk\_limit

The length of the chunk queue and the size of each chunk, respectively. Please see the [Buffer Plugin Overview](https://docs.fluentd.org/buffer) article for the basic buffer structure. The default values are 64 and 8m, respectively. The suffixes "k" (KB), "m" (MB), and "g" (GB) can be used for buffer\_chunk\_limit.

### flush\_interval

The interval between data flushes. The default is 60s. The suffixes "s" (seconds), "m" (minutes), and "h" (hours) can be used.

### flush\_at\_shutdown

If set to true, Fluentd waits for the buffer to flush at shutdown. By default, it is set to true for Memory Buffer and false for File Buffer.

### retry\_wait, max\_retry\_wait

The initial and maximum intervals between write retries. The default values are 1.0 and unset (no limit). The interval doubles (with +/-12.5% randomness) every retry until `max_retry_wait` is reached.

Since td-agent will retry 17 times before giving up by default (see the `retry_limit` parameter for details), the sleep interval can be up to approximately 131072 seconds (roughly 36 hours) in the default configurations.

### retry\_limit, disable\_retry\_limit

The limit on the number of retries before buffered data is discarded, and an option to disable that limit (if true, the value of `retry_limit` is ignored and there is no limit). The default values are 17 and false (not disabled). If the limit is reached, buffered data is discarded and the retry interval is reset to its initial value (`retry_wait`).

### num\_threads

The number of threads to flush the buffer. This option can be used to parallelize writes into the output(s) designated by the output plugin. The default is 1.

### slow\_flush\_log\_threshold

Same as Buffered Output but default value is changed to `40.0` seconds.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# file

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LX0TXFO4vCQin9tVjFa%2F-LWNPNeEkhSLIRkULLY1%2Ffile.png?generation=1548360511546518\&alt=media)

The `out_file` TimeSliced Output plugin writes events to files. By default, it creates files on a daily basis (around 00:10). This means that when you first import records using the plugin, no file is created immediately. The file will be created when the `time_slice_format` condition has been met. To change the output frequency, please modify the `time_slice_format` value.

## Example Configuration

`out_file` is included in Fluentd's core. No additional installation process is required.

```
<match pattern>
  @type file
  path /var/log/fluent/myapp
  time_slice_format %Y%m%d
  time_slice_wait 10m
  time_format %Y%m%dT%H%M%S%z
  compress gzip
  utc
</match>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

## Parameters

### type (required)

The value must be `file`.

### path (required)

The Path of the file. The actual path is path + time + ".log". The time portion is determined by the time\_slice\_format parameter, descried below.

The `path` parameter is used as `buffer_path` in this plugin.

Initially, you may see a file which looks like \\"/path/to/file.20140101.log.b4eea2c8166b147a0\\". This is an intermediate buffer file (\\"b4eea2c8166b147a0\\" identifies the buffer). Once the content of the buffer has been completely [flushed](https://docs.fluentd.org/buffer/file), you will see the output file without the trailing identifier.

### append

The flushed chunk is appended to existence file or not. The default is `false`. By default, out\_file flushes each chunk to different path.

```
# append false
log.20140608_0.log
log.20140608_1.log
log.20140609_0.log
log.20140609_1.log
```

This makes parallel file processing easy. But if you want to disable this behaviour, you can disable it by setting `append true`.

```
# append true
log.20140608.log
log.20140609.log
```

### format

The format of the file content. The default is `out_file`.

See [formatter article](https://docs.fluentd.org/formatter) for more detail.

### time\_format

The format of the time written in files. The default format is ISO-8601.

### utc

Uses UTC for path formatting. The default format is localtime.

### compress

Compresses flushed files using `gzip`. No compression is performed by default.

### symlink\_path

Create symlink to temporary buffered file when `buffer_type` is `file`. No symlink is created by default. This is useful for tailing file content to check logs.

## Time Sliced Output Parameters

For advanced usage, you can tune Fluentd's internal buffering mechanism with these parameters.

### time\_slice\_format

The time format used as part of the file name. The following characters are replaced with actual values when the file is created:

* \\%Y: year including the century (at least 4 digits)
* \\%m: month of the year (01..12)
* \\%d: Day of the month (01..31)
* \\%H: Hour of the day, 24-hour clock (00..23)
* \\%M: Minute of the hour (00..59)
* \\%S: Second of the minute (00..60)

The default format is `%Y%m%d%H`, which creates one file per hour.

### time\_slice\_wait

The amount of time Fluentd will wait for old logs to arrive. This is used to account for delays in logs arriving to your Fluentd node. The default wait time is 10 minutes ('10m'), where Fluentd will wait until 10 minutes past the hour for any logs that occurred within the past hour.

For example, when splitting files on an hourly basis, a log recorded at 1:59 but arriving at the Fluentd node between 2:00 and 2:10 will be uploaded together with all the other logs from 1:00 to 1:59 in one transaction, avoiding extra overhead. Larger values can be set as needed.

### buffer\_type

The buffer type is `file` by default ([buf\_file](https://docs.fluentd.org/buffer/file)). The `memory` ([buf\_memory](https://docs.fluentd.org/buffer/memory)) buffer type can be chosen as well. If you use `file` buffer type, `buffer_path` parameter is required.

### buffer\_queue\_limit, buffer\_chunk\_limit

The length of the chunk queue and the size of each chunk, respectively. Please see the [Buffer Plugin Overview](https://docs.fluentd.org/buffer) article for the basic buffer structure. The default values are 64 and 8m, respectively. The suffixes "k" (KB), "m" (MB), and "g" (GB) can be used for buffer\_chunk\_limit.

### flush\_interval

The interval between data flushes. The default is 60s. The suffixes "s" (seconds), "m" (minutes), and "h" (hours) can be used.

### flush\_at\_shutdown

If set to true, Fluentd waits for the buffer to flush at shutdown. By default, it is set to true for Memory Buffer and false for File Buffer.

### retry\_wait, max\_retry\_wait

The initial and maximum intervals between write retries. The default values are 1.0 and unset (no limit). The interval doubles (with +/-12.5% randomness) every retry until `max_retry_wait` is reached.

Since td-agent will retry 17 times before giving up by default (see the `retry_limit` parameter for details), the sleep interval can be up to approximately 131072 seconds (roughly 36 hours) in the default configurations.

### retry\_limit, disable\_retry\_limit

The limit on the number of retries before buffered data is discarded, and an option to disable that limit (if true, the value of `retry_limit` is ignored and there is no limit). The default values are 17 and false (not disabled). If the limit is reached, buffered data is discarded and the retry interval is reset to its initial value (`retry_wait`).

### num\_threads

The number of threads to flush the buffer. This option can be used to parallelize writes into the output(s) designated by the output plugin. The default is 1.

### slow\_flush\_log\_threshold

Same as Buffered Output but default value is changed to `40.0` seconds.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# s3

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN2biv5zzn1JBo8u1T%2F-LWNPOMRkz9GIqPkxApD%2Fs3.png?generation=1548739340461622\&alt=media)

The `out_s3` TimeSliced Output plugin writes records into the Amazon S3 cloud object storage service. By default, it creates files on an hourly basis. This means that when you first import records using the plugin, no file is created immediately. The file will be created when the `time_slice_format` condition has been met. To change the output frequency, please modify the `time_slice_format` value. This document doesn't describe all parameters. If you want to know full features, check the Further Reading section.

## Installation

`out_s3` is included in td-agent by default. Fluentd gem users will need to install the fluent-plugin-s3 gem using the following command.

```
$ fluent-gem install fluent-plugin-s3
```

## Example Configuration

```
<match pattern>
  @type s3

  aws_key_id YOUR_AWS_KEY_ID
  aws_sec_key YOUR_AWS_SECRET_KEY
  s3_bucket YOUR_S3_BUCKET_NAME
  s3_region ap-northeast-1
  path logs/
  buffer_path /var/log/fluent/s3

  time_slice_format %Y%m%d%H
  time_slice_wait 10m
  utc

  buffer_chunk_limit 256m
</match>
```

Please see the [Store Apache Logs into Amazon S3](https://docs.fluentd.org/articles/apache-to-s3) article for real-world use cases.

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

Please make sure that you have **enough space in the buffer\_path directory**. Running out of disk space is a problem frequently reported by users.

## Parameters

### type (required)

The value must be `s3`.

### aws\_key\_id (required/optional)

The AWS access key id. This parameter is required when your agent is not running on an EC2 instance with an IAM Instance Profile.

### aws\_sec\_key (required/optional)

The AWS secret key. This parameter is required when your agent is not running on an EC2 instance with an IAM Instance Profile.

### s3\_bucket (required)

The Amazon S3 bucket name.

### buffer\_path (required)

The path prefix of the log buffer files.

### s3\_region

The Amazon S3 region name. Please select the appropriate region name and confirm that your bucket has been created in the correct region. Here are the region examples.

* us-east-1
* us-west-1
* eu-central-1
* ap-southeast-1
* sa-east-1

The full list can be found [official AWS document](http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region).

### s3\_endpoint

This option is deprecated because latest aws-sdk ignores this option. Please use `s3_region` instead.

The Amazon S3 enpoint name. Please select the appropriate endpoint name from the list below and confirm that your bucket has been created in the correct region.

* s3.amazonaws.com
* s3-us-west-1.amazonaws.com
* s3-us-west-2.amazonaws.com
* s3.sa-east-1.amazonaws.com
* s3-eu-west-1.amazonaws.com
* s3-ap-southeast-1.amazonaws.com
* s3-ap-northeast-1.amazonaws.com

The most recent versions of the endpoints can be found [here](http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region).

### format

The format of the S3 object. The default is `out_file`.

See [formatter article](https://docs.fluentd.org/formatter) for more detail.

### time\_format

The format of the time written in files. The default format is ISO-8601.

### path

The path prefix of the files on S3. The default is "" (no prefix).

The actual path on S3 will be: "{path}{time\_slice\_format}\_{sequential\_index}.gz" (see \`s3\_object\_key\_format\`)

### s3\_object\_key\_format

The actual S3 path. The default value is %{path}%{time\_slice}\_%{index}.%{file\_extension}, which is interpolated to the actual path (ex: Ruby's variable interpolation).

* path: the value of the `path` parameter above
* time\_slice: the time string as formatted by `time_slice_format`
* index: the index for the given path. Incremented per buffer flush
* file\_extension: as determined by the `store_as` parameter.

For example, if

* `s3_object_key_format` is as default
* `path` is "hello"
* `time_slice_format` is "%Y%m%d"
* `store_as` is "json"

Then, "hello20141111\_0.json" would be an example actual S3 path.

This parameter is for advanced users. Most users should NOT modify it. Also, always make sure that %{index} appears in the customized \`s3\_object\_key\_format\` (Otherwise, multiple buffer flushes within the same time slice throws an error).

### utc

Uses UTC for path formatting. The default format is localtime.

### store\_as

The compression type. The default is "gzip", but you can also choose "lzo", "json", or "txt".

### proxy\_uri

The proxy url. The default is nil.

### ssl\_verify\_peer

Verify SSL certificate of the endpoint. The default is true. Set false when you want to ignore the endpoint SSL certificate.

## Time Sliced Output Parameters

For advanced usage, you can tune Fluentd's internal buffering mechanism with these parameters.

### time\_slice\_format

The time format used as part of the file name. The following characters are replaced with actual values when the file is created:

* \\%Y: year including the century (at least 4 digits)
* \\%m: month of the year (01..12)
* \\%d: Day of the month (01..31)
* \\%H: Hour of the day, 24-hour clock (00..23)
* \\%M: Minute of the hour (00..59)
* \\%S: Second of the minute (00..60)

The default format is `%Y%m%d%H`, which creates one file per hour.

### time\_slice\_wait

The amount of time Fluentd will wait for old logs to arrive. This is used to account for delays in logs arriving to your Fluentd node. The default wait time is 10 minutes ('10m'), where Fluentd will wait until 10 minutes past the hour for any logs that occurred within the past hour.

For example, when splitting files on an hourly basis, a log recorded at 1:59 but arriving at the Fluentd node between 2:00 and 2:10 will be uploaded together with all the other logs from 1:00 to 1:59 in one transaction, avoiding extra overhead. Larger values can be set as needed.

### buffer\_type

The buffer type is `file` by default ([buf\_file](https://docs.fluentd.org/buffer/file)). The `memory` ([buf\_memory](https://docs.fluentd.org/buffer/memory)) buffer type can be chosen as well. If you use `file` buffer type, `buffer_path` parameter is required.

### buffer\_queue\_limit, buffer\_chunk\_limit

The length of the chunk queue and the size of each chunk, respectively. Please see the [Buffer Plugin Overview](https://docs.fluentd.org/buffer) article for the basic buffer structure. The default values are 64 and 8m, respectively. The suffixes "k" (KB), "m" (MB), and "g" (GB) can be used for buffer\_chunk\_limit.

### flush\_interval

The interval between data flushes. The default is 60s. The suffixes "s" (seconds), "m" (minutes), and "h" (hours) can be used.

### flush\_at\_shutdown

If set to true, Fluentd waits for the buffer to flush at shutdown. By default, it is set to true for Memory Buffer and false for File Buffer.

### retry\_wait, max\_retry\_wait

The initial and maximum intervals between write retries. The default values are 1.0 and unset (no limit). The interval doubles (with +/-12.5% randomness) every retry until `max_retry_wait` is reached.

Since td-agent will retry 17 times before giving up by default (see the `retry_limit` parameter for details), the sleep interval can be up to approximately 131072 seconds (roughly 36 hours) in the default configurations.

### retry\_limit, disable\_retry\_limit

The limit on the number of retries before buffered data is discarded, and an option to disable that limit (if true, the value of `retry_limit` is ignored and there is no limit). The default values are 17 and false (not disabled). If the limit is reached, buffered data is discarded and the retry interval is reset to its initial value (`retry_wait`).

### num\_threads

The number of threads to flush the buffer. This option can be used to parallelize writes into the output(s) designated by the output plugin. The default is 1.

### slow\_flush\_log\_threshold

Same as Buffered Output but default value is changed to `40.0` seconds.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

## Further Reading

This page doesn't describe all the possible configurations. If you want to know about other configurations, please check the link below.

* [fluent-plugin-s3 repository](https://github.com/fluent/fluent-plugin-s3)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# kafka

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN2biv5zzn1JBo8u1T%2F-LWNPO9mxCceY9OkTuIS%2Fkafka.png?generation=1548739338714625\&alt=media)

The `out_kafka` Output plugin writes records into [Apache Kafka](https://kafka.apache.org/). This document doesn't describe all parameters. If you want to know full features, check the Further Reading section.

## Installation

`out_kafka` is included in td-agent2 after v2.3.3. Fluentd gem users will need to install the fluent-plugin-kafka gem using the following command.

```
$ fluent-gem install fluent-plugin-kafka
```

## Example Configuration

```
<match pattern>
  @type kafka_buffered

  # list of seed brokers
  brokers <broker1_host>:<broker1_port>,<broker2_host>:<broker2_port>

  # buffer settings
  buffer_type file
  buffer_path /var/log/td-agent/buffer/td
  flush_interval 3s

  # topic settings
  default_topic messages

  # data type settings
  output_data_type json
  compression_codec gzip

  # producer settings
  max_send_retries 1
  required_acks -1
</match>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

Please make sure that you have **enough space in the buffer\_path directory**. Running out of disk space is a problem frequently reported by users.

## Parameters

### type (required)

The value must be `kafka_buffered`.

### brokers (required/optional)

The list of all seed brokers, with their host and port information.

### default\_topic

The name of default topic (default: nil).

### default\_partition\_key

The name of default partition key (default: nil).

### default\_message\_key

The name of default message key (default: nil).

### output\_data\_type

The format of each message. The available options are `json`, `ltsv`, `msgpack`, `attr:<record name>`, `<formatter name>`. `msgpack` is recommended since it's more compact and faster.

### max\_send\_retries

The number of times to retry sending of messages to a leader (default: 1).

### required\_acks

The number of acks required per request (default: -1).

### ack\_timeout

How long the producer waits for acks. The unit is seconds (default: nil => Use default of ruby-kafka library)

### compression\_codec

The codec the producer uses to compress messages (default: nil). The available options are `gzip` and `snappy`. When you use `snappy`, you need to install `snappy` gem by `td-agent-gem` command.

## Buffered Output Parameters

For advanced usage, you can tune Fluentd's internal buffering mechanism with these parameters.

### buffer\_type

The buffer type is `memory` by default ([buf\_memory](https://docs.fluentd.org/buffer/memory)) for the ease of testing, however `file` ([buf\_file](https://docs.fluentd.org/buffer/file)) buffer type is always recommended for the production deployments. If you use `file` buffer type, `buffer_path` parameter is required.

### buffer\_queue\_limit, buffer\_chunk\_limit

The length of the chunk queue and the size of each chunk, respectively. Please see the [Buffer Plugin Overview](https://docs.fluentd.org/buffer) article for the basic buffer structure. The default values are 64 and 8m, respectively. The suffixes "k" (KB), "m" (MB), and "g" (GB) can be used for buffer\_chunk\_limit.

### flush\_interval

The interval between data flushes. The default is 60s. The suffixes "s" (seconds), "m" (minutes), and "h" (hours) can be used.

### flush\_at\_shutdown

If set to true, Fluentd waits for the buffer to flush at shutdown. By default, it is set to true for Memory Buffer and false for File Buffer.

### retry\_wait, max\_retry\_wait

The initial and maximum intervals between write retries. The default values are 1.0 seconds and unset (no limit). The interval doubles (with +/-12.5% randomness) every retry until `max_retry_wait` is reached.

Since td-agent will retry 17 times before giving up by default (see the `retry_limit` parameter for details), the sleep interval can be up to approximately 131072 seconds (roughly 36 hours) in the default configurations.

### retry\_limit, disable\_retry\_limit

The limit on the number of retries before buffered data is discarded, and an option to disable that limit (if true, the value of `retry_limit` is ignored and there is no limit). The default values are 17 and false (not disabled). If the limit is reached, buffered data is discarded and the retry interval is reset to its initial value (`retry_wait`).

### num\_threads

The number of threads to flush the buffer. This option can be used to parallelize writes into the output(s) designated by the output plugin. Increasing the number of threads improves the flush throughput to hide write / network latency. The default is 1.

### slow\_flush\_log\_threshold

The threshold for checking chunk flush performance. The default value is `20.0` seconds. Note that parameter type is `float`, not `time`.

If chunk flush takes longer time than this threshold, fluentd logs warning message like below:

```
2016-12-19 12:00:00 +0000 [warn]: buffer flush took longer time than slow_flush_log_threshold: elapsed_time = 15.0031226690043695 slow_flush_log_threshold=10.0 plugin_id="foo"
```

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

## Further Reading

This page doesn't describe all the possible configurations. If you want to know about other configurations, please check the link below.

* [fluent-plugin-kafka repository](https://github.com/fluent/fluent-plugin-kafka)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# forward

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LX4w0SBbRIFelg25IS1%2F-LWNPOLBEeeEkCbHJl5r%2Fforward.png?generation=1548435348570941\&alt=media)

The `out_forward` Buffered Output plugin forwards events to other fluentd nodes. This plugin supports load-balancing and automatic fail-over (a.k.a. active-active backup). For replication, please use the [out\_copy](https://docs.fluentd.org/output/copy) plugin.

The `out_forward` plugin detects server faults using a "φ accrual failure detector" algorithm. You can customize the parameters of the algorithm. When a server fault recovers, the plugin makes the server available automatically after a few seconds.

The `out_forward` plugin supports at-most-once and at-least-once semantics. The default is at-most-once. Do **NOT** use this plugin for inter-DC or public internet data transfer without secure connections. All the data is not encrypted, and this plugin is not designed for high-latency network environment. If you require a secure connection between nodes, please consider using [in\_secure\_forward](https://docs.fluentd.org/input/secure_forward).

## Example Configuration

`out_forward` is included in Fluentd's core. No additional installation process is required.

```
<match pattern>
  @type forward
  send_timeout 60s
  recover_wait 10s
  hard_timeout 60s

  <server>
    name myserver1
    host 192.168.1.3
    port 24224
    weight 60
  </server>
  <server>
    name myserver2
    host 192.168.1.4
    port 24224
    weight 60
  </server>
  ...

  <secondary>
    @type file
    path /var/log/fluent/forward-failed
  </secondary>
</match>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

## Parameters

### type (required)

The value must be `forward`.

### \<server> (at least one is required)

The destination servers. Each server must have following information.

* *name*: The name of the server. This parameter is used in error

  messages.
* *host* (required): The IP address or host name of the server.
* *port*: The port number of the host. The default is `24224`. Note

  that both TCP packets (event stream) and UDP packets (heartbeat

  message) are sent to this port.
* *weight*: The load balancing weight. If the weight of one server is

  20 and the weight of the other server is 30, events are sent in a

  2:3 ratio. The default weight is 60.
* *standby*: Set the destination to standby node. The default is

  `false`. standby servers will be selected when all non-standby

  servers went down.

### require\_ack\_response

Change the protocol to at-least-once. The plugin waits the ack from destination's in\_forward plugin.

### ack\_response\_timeout

This option is used when `require_ack_response` is `true`. The default is 190. This default value is based on popular tcp\_syn\_retries.

If set `0`, this plugin doesn't wait the ack response.

### \<secondary> (optional)

The backup destination that is used when all servers are unavailable.

### send\_timeout

The timeout time when sending event logs. The default is 60 seconds.

### recover\_wait

The wait time before accepting a server fault recovery. The default is 10 seconds.

### heartbeat\_type

The transport protocol to use for heartbeats. The default is "udp", but you can select "tcp" as well. Set "none" to disable heartbeat.

### heartbeat\_interval

The interval of the heartbeat packer. The default is 1 second.

### phi\_failure\_detector

Use the "Phi accrual failure detector" to detect server failure. The default value is `true`.

### phi\_threshold

The threshold parameter used to detect server faults. The default value is 16.

\`phi\_threshold\` is deeply related to \`heartbeat\_interval\`. If you are using longer \`heartbeat\_interval\`, please use the larger \`phi\_threshold\`. Otherwise you will see frequent detachments of destination servers. The default value 16 is tuned for \`heartbeat\_interval\` 1s.

### hard\_timeout

The hard timeout used to detect server failure. The default value is equal to the send\_timeout parameter.

### standby

Marks a node as the standby node for an Active-Standby model between Fluentd nodes. When an active node goes down, the standby node is promoted to an active node. The standby node is not used by the `out_forward` plugin until then.

```
<match pattern>
  @type forward
  ...

  <server>
    name myserver1
    host 192.168.1.3
    weight 60
  </server>
  <server>  # forward doesn't use myserver2 until myserver1 goes down
    name myserver2
    host 192.168.1.4
    weight 60
    standby
  </server>
  ...
</match>
```

### expire\_dns\_cache

Set TTL to expire DNS cache in seconds. Set 0 not to use DNS Cache. The default is nil (which means the persistent cache).

### dns\_round\_robin

Enable client-side DNS round robin. Uniform randomly pick an IP address to send data when a hostname has serveral IP addresses.

\`heartbeat\_type udp\` is not available with \`dns\_round\_robin true\`. Use \`heartbeat\_type tcp\` or \`heartbeat\_type none\`.

## Buffered Output Parameters

For advanced usage, you can tune Fluentd's internal buffering mechanism with these parameters.

### buffer\_type

The buffer type is `memory` by default ([buf\_memory](https://docs.fluentd.org/buffer/memory)) for the ease of testing, however `file` ([buf\_file](https://docs.fluentd.org/buffer/file)) buffer type is always recommended for the production deployments. If you use `file` buffer type, `buffer_path` parameter is required.

### buffer\_queue\_limit, buffer\_chunk\_limit

The length of the chunk queue and the size of each chunk, respectively. Please see the [Buffer Plugin Overview](https://docs.fluentd.org/buffer) article for the basic buffer structure. The default values are 64 and 8m, respectively. The suffixes "k" (KB), "m" (MB), and "g" (GB) can be used for buffer\_chunk\_limit.

### flush\_interval

The interval between data flushes. The default is 60s. The suffixes "s" (seconds), "m" (minutes), and "h" (hours) can be used.

### flush\_at\_shutdown

If set to true, Fluentd waits for the buffer to flush at shutdown. By default, it is set to true for Memory Buffer and false for File Buffer.

### retry\_wait, max\_retry\_wait

The initial and maximum intervals between write retries. The default values are 1.0 seconds and unset (no limit). The interval doubles (with +/-12.5% randomness) every retry until `max_retry_wait` is reached.

Since td-agent will retry 17 times before giving up by default (see the `retry_limit` parameter for details), the sleep interval can be up to approximately 131072 seconds (roughly 36 hours) in the default configurations.

### retry\_limit, disable\_retry\_limit

The limit on the number of retries before buffered data is discarded, and an option to disable that limit (if true, the value of `retry_limit` is ignored and there is no limit). The default values are 17 and false (not disabled). If the limit is reached, buffered data is discarded and the retry interval is reset to its initial value (`retry_wait`).

### num\_threads

The number of threads to flush the buffer. This option can be used to parallelize writes into the output(s) designated by the output plugin. Increasing the number of threads improves the flush throughput to hide write / network latency. The default is 1.

### slow\_flush\_log\_threshold

The threshold for checking chunk flush performance. The default value is `20.0` seconds. Note that parameter type is `float`, not `time`.

If chunk flush takes longer time than this threshold, fluentd logs warning message like below:

```
2016-12-19 12:00:00 +0000 [warn]: buffer flush took longer time than slow_flush_log_threshold: elapsed_time = 15.0031226690043695 slow_flush_log_threshold=10.0 plugin_id="foo"
```

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

## Troubleshooting

### "no nodes are available"

Please make sure that you can communicate with port 24224 using **not only TCP, but also UDP**. These commands will be useful for checking the network configuration.

```
$ telnet host 24224
$ nmap -p 24224 -sU host
```

Please note that there is one [known issue](http://kb.vmware.com/selfservice/microsites/search.do?language=en_US\&cmd=displayKC\&externalId=2019944) where VMware will occasionally lose small UDP packets used for heartbeat.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# secure\_forward

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXeGSWNqm-KvdcrGt9m%2F-LXeGWstkIxO53iGrSZt%2Fsecure_forward.png?generation=1549044953083653\&alt=media)

The `out_secure_forward` output plugin sends messages via **SSL with authentication** (cf. [in\_secure\_forward](https://docs.fluentd.org/input/secure_forward)). This document doesn't describe all parameters. If you want to know full features, check the Further Reading section.

## Installation

`out_secure_forward` is **not** included in either `td-agent` package or `fluentd` gem. In order to install it, please refer to the [Plugin Management](https://docs.fluentd.org/deployment/plugin-management) article.

## Example Configurations

This section provides some example configurations for `out_secure_forward`.

### Minimalist Configuration

At first, generate private CA file on side of input plugin by `secure-forward-ca-generate`, then copy that file to output plugin side by safe way (scp, or anyway else).

```
<match secret.data.**>
  @type secure_forward
  shared_key secret_string
  self_hostname client.fqdn.local
  secure true
  ca_cert_path /path/to/certificate/ca_cert.pem

  <server>
    host server.fqdn.local  # or IP
    # port 24284
  </server>
</match>
```

Without hostname ACL (not yet implemented), \`self\_hostname\` is not checked in any state. The \`"#{Socket.gethostname}"\` placeholder is available for such cases.

```
<match secret.data.**>
  @type secure_forward
  shared_key secret_string
  self_hostname "#{Socket.gethostname}"
  secure true
  ca_cert_path /path/to/certificate/ca_cert.pem

  <server>
    host server.fqdn.local  # or IP
    # port 24284
  </server>
</match>
```

### Multiple Forward Destinations over SSL

When two or more `<server>...</server>` clauses are specified, `out_secure_forward` uses these server nodes in a round-robin order. The servers with `standby yes` are NOT selected until all non-standby servers go down.

If a server requires username & password, set \`username\` and \`password\` in the \`\` section:

```
<match secret.data.**>
  @type secure_forward
  shared_key secret_string
  self_hostname client.fqdn.local
  secure true
  ca_cert_path /path/to/certificate/ca_cert.pem

  <server>
    host first.fqdn.local
    username repeatedly
    password sushi
  </server>
  <server>
    host second.fqdn.local
    username sasatatsu
    password karaage
  </server>
  <server>
    host standby.fqdn.local
    username kzk
    password hawaii
    standby  yes
  </server>
</match>
```

Use the `keepalive` parameter to specify keepalive timeouts. For example, the configuration below disconnects and re-connects its SSL connection every hour. By default, `keepalive` is set to 0 and the connection does NOT get disconnected unless there is a connection issue (This feature is for DNS name updates and refreshing SSL common keys).

```
<match secret.data.**>
  @type secure_forward
  shared_key secret_string
  self_hostname client.fqdn.local
  keepalive 3600
  secure true
  ca_cert_path /path/to/certificate/ca_cert.pem

  <server>
    host server.fqdn.local  # or IP
    # port 24284
  </server>
</match>
```

### Secure Sender-Receiver Setup

Example to send and receive several different kinds of logs (format is set to none for simplicity here).

#### Sender

```
# td-agent secured client (sender)

<source>
  @type tail
  path /appbase/logs/apache/apache_access_log
  pos_file /var/log/td-agent/tmp/apache.access.pos
  tag apache.access
  format none
</source>

<source>
  @type tail
  path /appbase/logs/apache/apache_error_log
  pos_file /var/log/td-agent/tmp/apache.error.pos
  tag apache.error
  format none
</source>

<source>
  @type tail
  path /appbase/logs/webapp/elastic_search.log
  pos_file /var/log/td-agent/tmp/elastic.search.pos
  tag elastic.search
  format none
</source>

<source>
  @type tail
  path /appbase/logs/webapp/elastic_search_poller.log
  pos_file /var/log/td-agent/tmp/elastic.search.poller.pos
  tag elastic.poller
  format none
</source>

<source>
  @type tail
  path /appbase/logs/webapp/ldap.log
  pos_file /var/log/td-agent/tmp/ldap.log.pos
  tag ldap.log
  format none
</source>



#-- Application Logs

<match apache.*>
  @type copy
  <store>
    @type secure_forward
    shared_key Supers3cr3t
    allow_self_signed_certificate true
    self_hostname frontend01.dev.company.net
    secure true
    ca_cert_path /path/to/certificate/ca_cert.pem

    <server>
      host logserver01.prd.company.net
      port 2514
    </server>
    <server>
      host logserver02.prd.company.net
      port 2514
    </server>
  </store>
</match>

<match elastic.*>
  @type copy
  <store>
    @type secure_forward
    shared_key Supers3cr3t
    allow_self_signed_certificate true
    self_hostname frontend01.dev.company.net
    secure true
    ca_cert_path /path/to/certificate/ca_cert.pem

    <server>
      host logserver01.prd.company.net
      port 2514
    </server>
    <server>
      host logserver02.prd.company.net
      port 2514
    </server>
  </store>
</match>

<match ldap.*>
  @type copy
  <store>
    @type secure_forward
    shared_key Supers3cr3t
    allow_self_signed_certificate true
    self_hostname frontend01.dev.company.net
    secure true
    ca_cert_path /path/to/certificate/ca_cert.pem

    <server>
      host logserver01.prd.company.net
      port 2514
    </server>
    <server>
      host logserver02.prd.company.net
      port 2514
    </server>
  </store>
</match>

#-- NOTE for troubleshooting any actions afer "type copy",
#-- and receive more output in td-agent.log, add:
#--       <store>
#--           @type stdout
#--       </store>


#-- Fluent Internal Logs

<match **>
  @type secure_forward
  shared_key Supers3cr3t
  self_hostname frontend01.dev.company.net
  flush_interval 8s
  secure true
  ca_cert_path /path/to/certificate/ca_cert.pem

  <server>
    host logserver01.prd.company.net
    port 2514
  </server>
  <server>
    host logserver02.prd.company.net
    port 2514
  </server>
</match>
```

#### Receiver

```
# td-agent secured receiver (server)

<source>
  @type secure_forward
  shared_key         Supers3cr3t
  self_hostname      logserver01.prd.company.net
  port 2514
  secure true
  ca_cert_path        /path/to/certificate/ca_cert.pem
  ca_private_key_path /path/to/certificate/ca_key.pem
  ca_private_key_passphrase passphrase_for_private_CA_secret_key
</source>


#-- Application Logs

<match *.access>
  @type file
  append true
  path /appbase/logs/received/access
  time_slice_format %Y%m%d
  time_slice_wait 5m
  time_format %Y%m%dT%H:%M:%S%z
</match>

<match *.error>
  @type file
  append true
  path /appbase/logs/received/error
  time_slice_format %Y%m%d
  time_slice_wait 5m
  time_format %Y%m%dT%H:%M:%S%z
</match>

<match elastic.search>
  @type file
  append true
  path /appbase/logs/received/elastic_search
  time_slice_format %Y%m%d
  time_slice_wait 5m
  time_format %Y%m%dT%H:%M:%S%z
</match>

<match elastic.poller>
  @type file
  append true
  path /appbase/logs/received/elastic_search_poller
  time_slice_format %Y%m%d
  time_slice_wait 5m
  time_format %Y%m%dT%H:%M:%S%z
</match>

<match ldap.*>
  @type file
  append true
  path /appbase/logs/received/ldap
  time_slice_format %Y%m%d
  time_slice_wait 5m
  time_format %Y%m%dT%H:%M:%S%z
</match>


#-- Fluent Internal Logs

<match fluent.info>
  @type file
  append true
  path /appbase/logs/received/fluent-info
</match>

<match fluent.warn>
  @type file
  append true
  path /appbase/logs/received/fluent-warn
</match>
```

## Parameters

### type

This parameter is required. Its value must be `secure_forward`.

### port (integer)

The default value is 24284.

### bind (string)

The default value is 0.0.0.0.

### secure (bool)

Indicate published connection is secure or not. Specify `yes` (or `true`) if secure encryption needed.

### ca\_cert\_path (string)

The file path of private CA certificate file. This file must be shared with input plugin. The default is blank, but this parameter must be specified except for the case to use certificates signed by public CA.

### self\_hostname (string)

Default value of the auto-generated certificate common name (CN).

### shared\_key (string)

Shared key between nodes..

### keepalive (time)

The duration for keepalive. If this parameter is not specified, keepalive is disabled.

### send\_timeout (time)

The send timeout value for sockets. The default value is 60 seconds.

### reconnect\_interval (time)

The interval between SSL reconnects. The default value is 5 seconds.

### read\_length (integer)

The number of bytes read per nonblocking read. The default value is 8MB=8*1024*1024 bytes.

### read\_interval\_msec (integer)

The interval between the non-blocking reads, in milliseconds. The default value is 50.

### socket\_interval\_msec (integer)

The interval between SSL reconnects in milliseconds. The default value is 200.

## Buffered Output Parameters

For advanced usage, you can tune Fluentd's internal buffering mechanism with these parameters.

### buffer\_type

The buffer type is `memory` by default ([buf\_memory](https://docs.fluentd.org/buffer/memory)) for the ease of testing, however `file` ([buf\_file](https://docs.fluentd.org/buffer/file)) buffer type is always recommended for the production deployments. If you use `file` buffer type, `buffer_path` parameter is required.

### buffer\_queue\_limit, buffer\_chunk\_limit

The length of the chunk queue and the size of each chunk, respectively. Please see the [Buffer Plugin Overview](https://docs.fluentd.org/buffer) article for the basic buffer structure. The default values are 64 and 8m, respectively. The suffixes "k" (KB), "m" (MB), and "g" (GB) can be used for buffer\_chunk\_limit.

### flush\_interval

The interval between data flushes. The default is 60s. The suffixes "s" (seconds), "m" (minutes), and "h" (hours) can be used.

### flush\_at\_shutdown

If set to true, Fluentd waits for the buffer to flush at shutdown. By default, it is set to true for Memory Buffer and false for File Buffer.

### retry\_wait, max\_retry\_wait

The initial and maximum intervals between write retries. The default values are 1.0 seconds and unset (no limit). The interval doubles (with +/-12.5% randomness) every retry until `max_retry_wait` is reached.

Since td-agent will retry 17 times before giving up by default (see the `retry_limit` parameter for details), the sleep interval can be up to approximately 131072 seconds (roughly 36 hours) in the default configurations.

### retry\_limit, disable\_retry\_limit

The limit on the number of retries before buffered data is discarded, and an option to disable that limit (if true, the value of `retry_limit` is ignored and there is no limit). The default values are 17 and false (not disabled). If the limit is reached, buffered data is discarded and the retry interval is reset to its initial value (`retry_wait`).

### num\_threads

The number of threads to flush the buffer. This option can be used to parallelize writes into the output(s) designated by the output plugin. Increasing the number of threads improves the flush throughput to hide write / network latency. The default is 1.

### slow\_flush\_log\_threshold

The threshold for checking chunk flush performance. The default value is `20.0` seconds. Note that parameter type is `float`, not `time`.

If chunk flush takes longer time than this threshold, fluentd logs warning message like below:

```
2016-12-19 12:00:00 +0000 [warn]: buffer flush took longer time than slow_flush_log_threshold: elapsed_time = 15.0031226690043695 slow_flush_log_threshold=10.0 plugin_id="foo"
```

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

## Further Reading

* [fluent-plugin-secure-forward repository](https://github.com/tagomoris/fluent-plugin-secure-forward)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# exec

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LX0aKuKEQ8l83KlUg5z%2F-LWNPNc7NZa9OMtQiGBD%2Fexec.png?generation=1548362557103314\&alt=media)

The `out_exec` TimeSliced Output plugin passes events to an external program. The program receives the path to a file containing the incoming events as its last argument. The file format is tab-separated values (TSV) by default.

## Example Configuration

`out_exec` is included in Fluentd's core. No additional installation process is required.

```
<match pattern>
  @type exec
  command cmd arg arg
  format tsv
  keys k1,k2,k3
  tag_key k1
  time_key k2
  time_format %Y-%m-%d %H:%M:%S
</match>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

## Example: Running FizzBuzz against data stream

This example illustrates how to run FizzBuzz with out\_exec.

We assume that the input file is specified by the last argument in the command line ("ARGV\[-1]"). The following script `fizzbuzz.py` runs [FizzBuzz](http://en.wikipedia.org/wiki/Fizz_buzz) against the new-line delimited sequence of natural numbers (1, 2, 3...) and writes the output to "foobar.out".

```
#!/usr/bin/env python
import sys
input = file(sys.argv[-1])
output = file("foobar.out", "a")
for line in input:
    fizzbuzz = int(line.split("\t")[0])
    s = ''
    if fizzbuzz%3 == 0:
        s += 'fizz'
    if fizzbuzz%5 == 0:
        s += 'buzz'
    if len(s) > 0:
        output.write(s+"\n")
    else:
        output.write(str(fizzbuzz)+"\n")
output.close
```

Note that this program is written in Python. For out\_exec (as well as out\_exec\_filter and in\_exec), **the program can be written in any language, not just Ruby.**

Then, configure Fluentd as follows

```
<source>
  @type forward
</source>
<match fizzbuzz>
  @type exec
  command python /path/to/fizzbuzz.py
  buffer_path    /path/to/buffer_path
  format tsv
  keys fizzbuzz
  flush_interval 5s # for debugging/checking
</match>
```

The "format tsv" and "keys fizzbuzz" tells Fluentd to extract the "fizzbuzz" field and output it as TSV. This simple example has a single key, but you can of course extract multiple fields and use "format json" to output newline-delimited JSONs.

The intermediary TSV is at `buffer_path`, and the command `python /path/to/fizzbuzz.py /path/to/buffer_path` is run. This is why in `fizzbuzz.py`, it's reading the file at `sys.argv[-1]`.

If you start Fluentd and run

```
$ for i in `seq 15`; do echo "{\"fizzbuzz\":$i}" | fluent-cat fizzbuzz; done
```

Then, after 5 seconds, you get a file named `foobar.out`.

```
$ cat foobar.out
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
```

## Parameters

### type (required)

The value must be `exec`.

### command (required)

The command (program) to execute. The exec plugin passes the path of a TSV file as the last argument.

### format

The format used to map the incoming events to the program input.

The following formats are supported:

* tsv (default)

When using the tsv format, please also specify the comma-separated `keys` parameter.

```
keys k1,k2,k3
```

* json
* msgpack

### tag\_key

The name of the key to use as the event tag. This replaces the value in the event record.

### time\_key

The name of the key to use as the event time. This replaces the the value in the event record.

### time\_format

The format for event time used when the `time_key` parameter is specified. The default is UNIX time (integer).

## Time Sliced Output Parameters

For advanced usage, you can tune Fluentd's internal buffering mechanism with these parameters.

### time\_slice\_format

The time format used as part of the file name. The following characters are replaced with actual values when the file is created:

* \\%Y: year including the century (at least 4 digits)
* \\%m: month of the year (01..12)
* \\%d: Day of the month (01..31)
* \\%H: Hour of the day, 24-hour clock (00..23)
* \\%M: Minute of the hour (00..59)
* \\%S: Second of the minute (00..60)

The default format is `%Y%m%d%H`, which creates one file per hour.

### time\_slice\_wait

The amount of time Fluentd will wait for old logs to arrive. This is used to account for delays in logs arriving to your Fluentd node. The default wait time is 10 minutes ('10m'), where Fluentd will wait until 10 minutes past the hour for any logs that occurred within the past hour.

For example, when splitting files on an hourly basis, a log recorded at 1:59 but arriving at the Fluentd node between 2:00 and 2:10 will be uploaded together with all the other logs from 1:00 to 1:59 in one transaction, avoiding extra overhead. Larger values can be set as needed.

### buffer\_type

The buffer type is `file` by default ([buf\_file](https://docs.fluentd.org/buffer/file)). The `memory` ([buf\_memory](https://docs.fluentd.org/buffer/memory)) buffer type can be chosen as well. If you use `file` buffer type, `buffer_path` parameter is required.

### buffer\_queue\_limit, buffer\_chunk\_limit

The length of the chunk queue and the size of each chunk, respectively. Please see the [Buffer Plugin Overview](https://docs.fluentd.org/buffer) article for the basic buffer structure. The default values are 64 and 8m, respectively. The suffixes "k" (KB), "m" (MB), and "g" (GB) can be used for buffer\_chunk\_limit.

### flush\_interval

The interval between data flushes. The default is 60s. The suffixes "s" (seconds), "m" (minutes), and "h" (hours) can be used.

### flush\_at\_shutdown

If set to true, Fluentd waits for the buffer to flush at shutdown. By default, it is set to true for Memory Buffer and false for File Buffer.

### retry\_wait, max\_retry\_wait

The initial and maximum intervals between write retries. The default values are 1.0 and unset (no limit). The interval doubles (with +/-12.5% randomness) every retry until `max_retry_wait` is reached.

Since td-agent will retry 17 times before giving up by default (see the `retry_limit` parameter for details), the sleep interval can be up to approximately 131072 seconds (roughly 36 hours) in the default configurations.

### retry\_limit, disable\_retry\_limit

The limit on the number of retries before buffered data is discarded, and an option to disable that limit (if true, the value of `retry_limit` is ignored and there is no limit). The default values are 17 and false (not disabled). If the limit is reached, buffered data is discarded and the retry interval is reset to its initial value (`retry_wait`).

### num\_threads

The number of threads to flush the buffer. This option can be used to parallelize writes into the output(s) designated by the output plugin. The default is 1.

### slow\_flush\_log\_threshold

Same as Buffered Output but default value is changed to `40.0` seconds.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# exec\_filter

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LX0aKuKEQ8l83KlUg5z%2F-LWNPQt-L66dpSpIQkYB%2Fexec_filter.png?generation=1548362555068010\&alt=media)

The `out_exec_filter` Buffered Output plugin (1) executes an external program using an event as input and (2) reads a new event from the program output. It passes tab-separated values (TSV) to stdin and reads TSV from stdout by default.

## Example Configuration

`out_exec_filter` is included in Fluentd's core. No additional installation process is required.

```
<match pattern>
  @type exec_filter
  command cmd arg arg
  in_keys k1,k2,k3
  out_keys k1,k2,k3,k4
  tag_key k1
  time_key k2
  time_format %Y-%m-%d %H:%M:%S
</match>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

## Parameters

### type (required)

The value must be `exec_filter`.

### command (required)

The command (program) to execute. The `out_exec_filter` plugin passes the incoming event to the program input and receives the filtered event from the program output.

### num\_children

The number of spawned process for `command`. Default is 1.

If the number is larger than 2, fluentd uses spawned processes by round robin fashion.

### child\_respawn

Respawn command when command exit. Default is disabled.

If you specify a positive number, try to respawn until specified times. If you specify `inf` or `-1`, try to respawn forever.

### in\_format

The format used to map the incoming event to the program input.

The following formats are supported:

* tsv (default)

When using the tsv format, please also specify the comma-separated `in_keys` parameter.

```
in_keys k1,k2,k3
```

* json
* msgpack

### out\_format

The format used to process the program output.

The following formats are supported:

* tsv (default)

When using the tsv format, please also specify the comma-separated `out_keys` parameter.

```
out_keys k1,k2,k3,k4
```

* json
* msgpack

When using the json format, this plugin uses the Yajl library to parse the program output. Yajl buffers data internally so the output isn't always instantaneous.

### tag\_key

The name of the key to use as the event tag. This replaces the value in the event record.

### time\_key

The name of the key to use as the event time. This replaces the the value in the event record.

### time\_format

The format for event time used when the `time_key` parameter is specified. The default is UNIX time (integer).

## Buffered Output Parameters

For advanced usage, you can tune Fluentd's internal buffering mechanism with these parameters.

### buffer\_type

The buffer type is `memory` by default ([buf\_memory](https://docs.fluentd.org/buffer/memory)) for the ease of testing, however `file` ([buf\_file](https://docs.fluentd.org/buffer/file)) buffer type is always recommended for the production deployments. If you use `file` buffer type, `buffer_path` parameter is required.

### buffer\_queue\_limit, buffer\_chunk\_limit

The length of the chunk queue and the size of each chunk, respectively. Please see the [Buffer Plugin Overview](https://docs.fluentd.org/buffer) article for the basic buffer structure. The default values are 64 and 8m, respectively. The suffixes "k" (KB), "m" (MB), and "g" (GB) can be used for buffer\_chunk\_limit.

### flush\_interval

The interval between data flushes. The default is 60s. The suffixes "s" (seconds), "m" (minutes), and "h" (hours) can be used.

### flush\_at\_shutdown

If set to true, Fluentd waits for the buffer to flush at shutdown. By default, it is set to true for Memory Buffer and false for File Buffer.

### retry\_wait, max\_retry\_wait

The initial and maximum intervals between write retries. The default values are 1.0 seconds and unset (no limit). The interval doubles (with +/-12.5% randomness) every retry until `max_retry_wait` is reached.

Since td-agent will retry 17 times before giving up by default (see the `retry_limit` parameter for details), the sleep interval can be up to approximately 131072 seconds (roughly 36 hours) in the default configurations.

### retry\_limit, disable\_retry\_limit

The limit on the number of retries before buffered data is discarded, and an option to disable that limit (if true, the value of `retry_limit` is ignored and there is no limit). The default values are 17 and false (not disabled). If the limit is reached, buffered data is discarded and the retry interval is reset to its initial value (`retry_wait`).

### num\_threads

The number of threads to flush the buffer. This option can be used to parallelize writes into the output(s) designated by the output plugin. Increasing the number of threads improves the flush throughput to hide write / network latency. The default is 1.

### slow\_flush\_log\_threshold

The threshold for checking chunk flush performance. The default value is `20.0` seconds. Note that parameter type is `float`, not `time`.

If chunk flush takes longer time than this threshold, fluentd logs warning message like below:

```
2016-12-19 12:00:00 +0000 [warn]: buffer flush took longer time than slow_flush_log_threshold: elapsed_time = 15.0031226690043695 slow_flush_log_threshold=10.0 plugin_id="foo"
```

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

## Script example

Here is an example writtein in ruby.

```
require 'json'
require 'msgpack'

begin
  while line = STDIN.gets # continue to read a event from stdin
    line.chomp!

    # Input format depends on exec_filter's in_format setting
    json = JSON.parse(line)

    # main processing. You can do anything, mutate record, access to database and etc.
    json['new_field'] = "Hey from exec_filter script!"

    # Write data to stdout. Output format depends on exec_filter's out_format setting
    STDOUT.print MessagePack.pack(json)

    # Call flush to avoid buffering events
    STDOUT.flush
  end
rescue Interrupt # Ignore Interrupt exception because it happens during exec_filter shutdown
end
```

Corresponding configuration is below:

```
<match test.**>
  @type exec_filter
  command ruby /path/to/ruby_script.rb
  in_format json
  out_format msgpack
  flush_interval 10s
  tag filtered.exec
</match>
```

If you want to use other language, translate above script example into your language.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# copy

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN2biv5zzn1JBo8u1T%2F-LWNPNcdtuUq_M7zUmC9%2Fcopy.png?generation=1548739338211471\&alt=media)

The `copy` output plugin copies events to multiple outputs.

## Example Configuration

`out_copy` is included in Fluentd's core. No additional installation process is required.

```
<match pattern>
  @type copy
  <store>
    @type file
    path /var/log/fluent/myapp1
    ...
  </store>
  <store>
    ...
  </store>
  <store>
    ...
  </store>
</match>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

Here is an example set up to send events to both a local file under `/var/log/fluent/myapp` and the collection `fluentd.test` in a local MongoDB instance (Please see the [out\_file](https://docs.fluentd.org/output/file) and [out\_mongo](https://docs.fluentd.org/output/mongo) articles for more details about the respective plugins.)

```
<match myevent.file_and_mongo>
  @type copy
  <store>
    @type file
    path /var/log/fluent/myapp
    time_slice_format %Y%m%d
    time_slice_wait 10m
    time_format %Y%m%dT%H%M%S%z
    compress gzip
    utc
  </store>
  <store>
    @type mongo
    host fluentd
    port 27017
    database fluentd
    collection test
  </store>
</match>
```

## Parameters

### type (required)

The value must be `copy`.

### deep\_copy

`out_copy` shares a record between `store` plugins by default.

When `deep_copy` is true, `out_copy` passes different record to each `store` plugin.

### \<store> (at least one required)

Specifies the storage destinations. The format is the same as the \ directive.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

## FAQ

### How to ignore each error in \\\\?

If one `store` raises an error, it affects other `<store>`. If you want to ignore an exception from less important `<store>`, you can use 3rd party [out\_copy\_ex](https://github.com/sonots/fluent-plugin-copy_ex) instead.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# geoip

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN2biv5zzn1JBo8u1T%2F-LWNPODi1ARKEG9qo0ou%2Fgeoip.png?generation=1548739341667223\&alt=media)

The `out_geoip` Buffered Output plugin adds geographic location information to logs using the Maxmind GeoIP databases. This document doesn't describe all parameters. If you want to know full features, check the Further Reading section.

## Prerequisites

* The GeoIP library.

  :::term # for RHEL/CentOS $ sudo yum install geoip-devel --enablerepo=epel

  \# for Ubuntu/Debian $ sudo apt-get install libgeoip-dev

  \# for MacOSX (brew) $ brew install geoip

## Install

`out_geoip` is not included in td-agent. All users must install the fluent-plugin-geoip gem using the following command.

```
$ fluent-gem install fluent-plugin-geoip
$ sudo /usr/sbin/td-agent-gem install fluent-plugin-geoip
```

## Example Configuration

The configuration shown below adds geolocation information to apache.access

```
<match test.message>
  @type geoip
  geoip_lookup_key        host
  enable_key_country_code geoip_country
  enable_key_city         geoip_city
  enable_key_latitude     geoip_lat
  enable_key_longitude    geoip_lon
  remove_tag_prefix       test.
  add_tag_prefix          geoip.
  flush_interval          5s
</match>


:::text
# original record
test.message {
  "host":"66.102.9.80",
  "message":"test"
}

# output record
geoip.message: {
  "host":"66.102.9.80",
  "message":"test",
  "geoip_country":"US",
  "geoip_city":"Mountain View",
  "geoip_lat":37.4192008972168,
  "geoip_lon":-122.05740356445312
}
```

Please see the [fluent-plugin-geoip README](https://github.com/y-ken/fluent-plugin-geoip#readme) for further details.

## Parameters

### geoip\_lookup\_key (required)

Specifies the geoip lookup field (default: host) If accessing a nested hash value, delimit the key with '.', as in 'host.ip'.

### remove\_tag\_prefix / add\_tag\_prefix (requires one or the other)

Set tag replace rule.

### enable\_key\_\*\*\* (requires at least one)

Specifies the geographic data that will be added to the record. The supported parameters are shown below:

* enable\_key\_city
* enable\_key\_latitude
* enable\_key\_longitude
* enable\_key\_country\_code3
* enable\_key\_country\_code
* enable\_key\_country\_name
* enable\_key\_dma\_code
* enable\_key\_area\_code
* enable\_key\_region

### include\_tag\_key

Set to `true` to include the original tag name in the record. (default: false)

### tag\_key

Adds the tag name into the record using this value as the key name When `include_tag_key` is set to `true`.

## Buffer Parameters

For advanced usage, you can tune Fluentd's internal buffering mechanism with these parameters.

### buffer\_type

The buffer type is `memory` by default ([buf\_memory](https://docs.fluentd.org/buffer/memory)). The `file` ([buf\_file](https://docs.fluentd.org/buffer/file)) buffer type can be chosen as well. Unlike many other output plugins, the `buffer_path` parameter MUST be specified when using `buffer_type file`.

### buffer\_queue\_limit, buffer\_chunk\_limit

The length of the chunk queue and the size of each chunk, respectively. Please see the [Buffer Plugin Overview](https://docs.fluentd.org/buffer) article for the basic buffer structure. The default values are 64 and 256m, respectively. The suffixes "k" (KB), "m" (MB), and "g" (GB) can be used for buffer\_chunk\_limit.

### flush\_interval

The interval between forced data flushes. The default is nil (don't force flush and wait until the end of time slice + time\_slice\_wait). The suffixes "s" (seconds), "m" (minutes), and "h" (hours) can be used.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

## Use Cases

#### Plot real time access statistics on a world map using Elasticsearch and Kibana

The `country_code` field is needed to visualize access statistics on a world map using [Kibana](http://www.elasticsearch.org/overview/kibana/).

Note: The following plugins are required: \* fluent-plugin-geoip \* fluent-plugin-elasticsearch

```
<match td.apache.access>
  @type geoip

  # Set key name for the client ip address values
  geoip_lookup_key     host

  # Specify key name for the country_code values
  enable_key_country_code  geoip_country

  # Swap tag prefix from 'td.' to 'es.'
  remove_tag_prefix    td.
  add_tag_prefix       es.
</match>

<match es.apache.access>
  @type            elasticsearch
  host            localhost
  port            9200
  type_name       apache
  logstash_format true
  flush_interval  10s
</match>
```

## Further Reading

* [fluent-plugin-geoip repository](https://github.com/y-ken/fluent-plugin-geoip)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# roundrobin

The `roundrobin` Output plugin distributes events to multiple outputs using a round-robin algorithm.

## Example Configuration

`out_roundrobin` is included in Fluentd's core. No additional installation process is required.

```
<match pattern>
  @type roundrobin

  <store>
    @type tcp
    host 192.168.1.21
    ...
  </store>
  <store>
    ...
  </store>
  <store>
    ...
  </store>
</match>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

## Parameters

### type (required)

The value must be `roundrobin`.

### \<store> (required at least one)

Specifies the storage destinations. The format is the same as the \ directive.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# stdout

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LX0aKuKEQ8l83KlUg5z%2F-LWNPOdBSQRXROLDre1M%2Fstdout.png?generation=1548362554725017\&alt=media)

The `stdout` output plugin prints events to stdout (or logs if launched with daemon mode). This output plugin is useful for debugging purposes.

## Example Configuration

`out_stdout` is included in Fluentd's core. No additional installation process is required.

```
<match pattern>
  @type stdout
</match>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

## Parameters

### type (required)

The value must be `stdout`.

### output\_type

Output format. The following formats are supported:

* json
* hash (Ruby's hash)

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# null

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LX0aKuKEQ8l83KlUg5z%2F-LWNPOgdk7DiG82oAkG1%2Fnull.png?generation=1548362563180387\&alt=media)

The `null` output plugin just throws away events.

## Example Configuration

`out_null` is included in Fluentd's core. No additional installation process is required.

```
<match pattern>
  @type null
</match>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

## Parameters

### type (required)

The value must be `null`.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# webhdfs

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN2biv5zzn1JBo8u1T%2F-LWNPNcVy9dTkicjR66_%2Fwebhdfs.png?generation=1548739338161694\&alt=media)

The `out_webhdfs` TimeSliced Output plugin writes records into HDFS (Hadoop Distributed File System). By default, it creates files on an hourly basis. This means that when you first import records using the plugin, no file is created immediately. The file will be created when the `time_slice_format` condition has been met. To change the output frequency, please modify the `time_slice_format` value. This document doesn't describe all parameters. If you want to know full features, check the Further Reading section.

## Install

`out_webhdfs` is included in td-agent by default (v1.1.10 or later). Fluentd gem users will have to install the fluent-plugin-webhdfs gem using the following command.

```
$ fluent-gem install fluent-plugin-webhdfs
```

## HDFS Configuration

Append operations are not enabled by default on CDH. Please put these configurations into your hdfs-site.xml file and restart the whole cluster.

```
<property>
  <name>dfs.webhdfs.enabled</name>
  <value>true</value>
</property>

<property>
  <name>dfs.support.append</name>
  <value>true</value>
</property>

<property>
  <name>dfs.support.broken.append</name>
  <value>true</value>
</property>
```

## Example Configuration

```
<match access.**>
  @type webhdfs
  host namenode.your.cluster.local
  port 50070
  path "/path/on/hdfs/access.log.%Y%m%d_%H.#{Socket.gethostname}.log"
  flush_interval 10s
</match>
```

Please see the [Fluentd + HDFS: Instant Big Data Collection](https://docs.fluentd.org/articles/http-to-hdfs) article for real-world use cases.

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

## Parameters

### type (required)

The value must be `webhfds`.

### host (required)

The namenode hostname.

### port (required)

The namenode port number.

### path (required)

The path on HDFS. Please include `"#{Socket.gethostname}"` in your path to avoid writing into the same HDFS file from multiple Fluentd instances. This conflict could result in data loss.

Path value can contain time placeholders (see `time_slice_format` section). If path contains time placeholders, webhdfs output configures `time_slice_format` automatically with these placeholders.

## Time Sliced Output Parameters (and overwritten values by out\_webhdfs)

For advanced usage, you can tune Fluentd's internal buffering mechanism with these parameters.

### time\_slice\_format

The time format used as part of the file name. The following characters are replaced with actual values when the file is created:

* \\%Y: year including the century (at least 4 digits)
* \\%m: month of the year (01..12)
* \\%d: Day of the month (01..31)
* \\%H: Hour of the day, 24-hour clock (00..23)
* \\%M: Minute of the hour (00..59)
* \\%S: Second of the minute (00..60)

The default format is `%Y%m%d%H`, which creates one file per hour. This parameter may be overwritten by `path` configuration.

### time\_slice\_wait

The amount of time Fluentd will wait for old logs to arrive. This is used to account for delays in logs arriving to your Fluentd node. The default wait time is 10 minutes ('10m'), where Fluentd will wait until 10 minutes past the hour for any logs that occurred within the past hour.

For example, when splitting files on an hourly basis, a log recorded at 1:59 but arriving at the Fluentd node between 2:00 and 2:10 will be uploaded together with all the other logs from 1:00 to 1:59 in one transaction, avoiding extra overhead. Larger values can be set as needed.

### buffer\_type

The buffer type is `memory` by default ([buf\_memory](https://docs.fluentd.org/buffer/memory)). The `file` ([buf\_file](https://docs.fluentd.org/buffer/file)) buffer type can be chosen as well. If you use `file` buffer type, `buffer_path` parameter is required.

### buffer\_queue\_limit, buffer\_chunk\_limit

The length of the chunk queue and the size of each chunk, respectively. Please see the [Buffer Plugin Overview](https://docs.fluentd.org/buffer) article for the basic buffer structure. The default values are 64 and 8m, respectively. The suffixes "k" (KB), "m" (MB), and "g" (GB) can be used for buffer\_chunk\_limit.

### flush\_interval

The interval between data flushes. The default is unspecified, and buffer chunks will be flushed at the end of time slices. The suffixes "s" (seconds), "m" (minutes), and "h" (hours) can be used.

### flush\_at\_shutdown

The boolean value to specify whether to flush buffer chunks at shutdown time, or not. The default is true. Specify true if you use `memory` buffer type.

### retry\_wait, max\_retry\_wait

The initial and maximum intervals between write retries. The default values are 1.0 and unset (no limit). The interval doubles (with +/-12.5% randomness) every retry until `max_retry_wait` is reached.

Since td-agent will retry 17 times before giving up by default (see the `retry_limit` parameter for details), the sleep interval can be up to approximately 131072 seconds (roughly 36 hours) in the default configurations.

### retry\_limit, disable\_retry\_limit

The limit on the number of retries before buffered data is discarded, and an option to disable that limit (if true, the value of `retry_limit` is ignored and there is no limit). The default values are 17 and false (not disabled). If the limit is reached, buffered data is discarded and the retry interval is reset to its initial value (`retry_wait`).

### num\_threads

The number of threads to flush the buffer. This option can be used to parallelize writes into the output(s) designated by the output plugin. The default is 1.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

## Further Reading

* [fluent-plugin-webhdfs repository](https://github.com/fluent/fluent-plugin-webhdfs)
* [Slides: Fluentd and WebHDFS](http://www.slideshare.net/tagomoris/fluentd-and-webhdfs)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# splunk

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN2biv5zzn1JBo8u1T%2F-LWNPO4hXIKGwF5htlCv%2Fsplunk.png?generation=1548739341021486\&alt=media)

The `out_splunk` Buffered Output plugin allows you to send data to a Splunk HTTP Event Collector or send data to Splunk Enterprise via TCP.

Visit <https://github.com/fluent/fluent-plugin-splunk> for details.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# mongo

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN2biv5zzn1JBo8u1T%2F-LWNPOlo20qnYeb4YqbA%2Fmongo.png?generation=1548739341480210\&alt=media)

The `out_mongo` Buffered Output plugin writes records into [MongoDB](http://mongodb.org/), the emerging document-oriented database system. If you're using ReplicaSet, please see the [out\_mongo\_replset](https://docs.fluentd.org/output/mongo_replset) article instead.

This document doesn't describe all parameters. If you want to know full features, check the Further Reading section.

## Why Fluentd with MongoDB?

Fluentd enables your apps to insert records to MongoDB asynchronously with batch-insertion, unlike direct insertion of records from your apps. This has the following advantages:

1. less impact on application performance
2. higher MongoDB insertion throughput while maintaining JSON record

   structure

## Install

`out_mongo` is included in td-agent by default. Fluentd gem users will need to install the fluent-plugin-mongo gem using the following command.

```
$ fluent-gem install fluent-plugin-mongo
```

## Example Configuration

```
# Single MongoDB
<match mongo.**>
  @type mongo
  host fluentd
  port 27017
  database fluentd
  collection test

  # for capped collection
  capped
  capped_size 1024m

  # authentication
  user michael
  password jordan

  # key name of timestamp
  time_key time

  # flush
  flush_interval 10s
</match>
```

Please see the [Store Apache Logs into MongoDB](https://docs.fluentd.org/articles/apache-to-mongodb) article for real-world use cases.

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

## Parameters

### type (required)

The value must be `mongo`.

### host (required)

The MongoDB hostname.

### port (required)

The MongoDB port.

### database (required)

The database name.

### collection (required, if not tag\_mapped)

The collection name.

### capped

This option enables capped collection. This is always recommended because MongoDB is not suited to storing large amounts of historical data.

#### capped\_size

Sets the capped collection size.

### user

The username to use for authentication.

### password

The password to use for authentication.

### time\_key

The key name of timestamp. (default is "time")

### tag\_mapped

This option will allow out\_mongo to use Fluentd's tag to determine the destination collection. For example, if you generate records with tags 'mongo.foo', the records will be inserted into the `foo` collection within the `fluentd` database.

```
<match mongo.*>
  @type mongo
  host fluentd
  port 27017
  database fluentd

  # Set 'tag_mapped' if you want to use tag mapped mode.
  tag_mapped

  # If the tag is "mongo.foo", then the prefix "mongo." is removed.
  # The inserted collection name is "foo".
  remove_tag_prefix mongo.

  # This configuration is used if the tag is not found. The default is 'untagged'.
  collection misc
</match>
```

This option is useful for flexible log collection.

## Buffered Output Parameters

For advanced usage, you can tune Fluentd's internal buffering mechanism with these parameters.

### buffer\_type

The buffer type is `memory` by default ([buf\_memory](https://docs.fluentd.org/buffer/memory)) for the ease of testing, however `file` ([buf\_file](https://docs.fluentd.org/buffer/file)) buffer type is always recommended for the production deployments. If you use `file` buffer type, `buffer_path` parameter is required.

### buffer\_queue\_limit, buffer\_chunk\_limit

The length of the chunk queue and the size of each chunk, respectively. Please see the [Buffer Plugin Overview](https://docs.fluentd.org/buffer) article for the basic buffer structure. The default values are 64 and 8m, respectively. The suffixes "k" (KB), "m" (MB), and "g" (GB) can be used for buffer\_chunk\_limit.

### flush\_interval

The interval between data flushes. The default is 60s. The suffixes "s" (seconds), "m" (minutes), and "h" (hours) can be used.

### flush\_at\_shutdown

If set to true, Fluentd waits for the buffer to flush at shutdown. By default, it is set to true for Memory Buffer and false for File Buffer.

### retry\_wait, max\_retry\_wait

The initial and maximum intervals between write retries. The default values are 1.0 seconds and unset (no limit). The interval doubles (with +/-12.5% randomness) every retry until `max_retry_wait` is reached.

Since td-agent will retry 17 times before giving up by default (see the `retry_limit` parameter for details), the sleep interval can be up to approximately 131072 seconds (roughly 36 hours) in the default configurations.

### retry\_limit, disable\_retry\_limit

The limit on the number of retries before buffered data is discarded, and an option to disable that limit (if true, the value of `retry_limit` is ignored and there is no limit). The default values are 17 and false (not disabled). If the limit is reached, buffered data is discarded and the retry interval is reset to its initial value (`retry_wait`).

### num\_threads

The number of threads to flush the buffer. This option can be used to parallelize writes into the output(s) designated by the output plugin. Increasing the number of threads improves the flush throughput to hide write / network latency. The default is 1.

### slow\_flush\_log\_threshold

The threshold for checking chunk flush performance. The default value is `20.0` seconds. Note that parameter type is `float`, not `time`.

If chunk flush takes longer time than this threshold, fluentd logs warning message like below:

```
2016-12-19 12:00:00 +0000 [warn]: buffer flush took longer time than slow_flush_log_threshold: elapsed_time = 15.0031226690043695 slow_flush_log_threshold=10.0 plugin_id="foo"
```

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

## Further Reading

* [fluent-plugin-mongo repository](https://github.com/fluent/fluent-plugin-mongo)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# mongo\_replset

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LX0eEDjAXByif3zFqAa%2F-LWNPNdkR349qf4JvhnM%2Fmongo_replset.png?generation=1548363579011042\&alt=media)

The `out_mongo_replset` Buffered Output plugin writes records into [MongoDB](http://mongodb.org/), the emerging document-oriented database system. This plugin is for users using ReplicaSet. If you are not using ReplicaSet, please see the [out\_mongo](https://docs.fluentd.org/output/mongo) article instead.

## Why Fluentd with MongoDB?

Fluentd enables your apps to insert records to MongoDB asynchronously with batch-insertion, unlike direct insertion of records from your apps. This has the following advantages:

1. less impact on application performance
2. higher MongoDB insertion throughput while maintaining JSON record

   structure

## Install

`out_mongo_replset` is included in td-agent by default. Fluentd gem users will need to install the fluent-plugin-mongo gem using the following command.

```
$ fluent-gem install fluent-plugin-mongo
```

## Example Configuration

```
# Single MongoDB
<match mongo.**>
  @type mongo_replset
  database fluentd
  collection test
  nodes localhost:27017,localhost:27018,localhost:27019

  # flush
  flush_interval 10s
</match>
```

Please see the [Store Apache Logs into MongoDB](https://docs.fluentd.org/articles/apache-to-mongodb) article for real-world use cases.

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

## Parameters

### type (required)

The value must be `mongo`.

### nodes (required)

The comma separated node strings (e.g. host1:27017,host2:27017,host3:27017).

### database (required)

The database name.

### collection (required if not tag\_mapped)

The collection name.

### capped

This option enables capped collection. This is always recommended because MongoDB is not suited to storing large amounts of historical data.

### capped\_size

Sets the capped collection size.

### user

The username to use for authentication.

### password

The password to use for authentication.

### tag\_mapped

This option will allow out\_mongo to use Fluentd's tag to determine the destination collection.

For example, if you generate records with tags 'mongo.foo', the records will be inserted into the `foo` collection within the `fluentd` database.

```
<match mongo.*>
  @type mongo_replset
  database fluentd
  nodes localhost:27017,localhost:27018,localhost:27019

  # Set 'tag_mapped' if you want to use tag mapped mode.
  tag_mapped

  # If the tag is "mongo.foo", then the prefix "mongo." is removed.
  # The inserted collection name is "foo".
  remove_tag_prefix mongo.

  # This configuration is used if the tag is not found. The default is 'untagged'.
  collection misc
</match>
```

### name

The ReplicaSet name.

### read

The ReplicaSet read preference (e.g. secondary, etc).

### refresh\_mode

The ReplicaSet refresh mode (e.g. sync, etc).

### refresh\_interval

The ReplicaSet refresh interval.

### num\_retries

The ReplicaSet failover threshold. The default threshold is 60. If the retry count reaches this threshold, the plugin raises an exception.

## Buffered Output Parameters

For advanced usage, you can tune Fluentd's internal buffering mechanism with these parameters.

### buffer\_type

The buffer type is `memory` by default ([buf\_memory](https://docs.fluentd.org/buffer/memory)) for the ease of testing, however `file` ([buf\_file](https://docs.fluentd.org/buffer/file)) buffer type is always recommended for the production deployments. If you use `file` buffer type, `buffer_path` parameter is required.

### buffer\_queue\_limit, buffer\_chunk\_limit

The length of the chunk queue and the size of each chunk, respectively. Please see the [Buffer Plugin Overview](https://docs.fluentd.org/buffer) article for the basic buffer structure. The default values are 64 and 8m, respectively. The suffixes "k" (KB), "m" (MB), and "g" (GB) can be used for buffer\_chunk\_limit.

### flush\_interval

The interval between data flushes. The default is 60s. The suffixes "s" (seconds), "m" (minutes), and "h" (hours) can be used.

### flush\_at\_shutdown

If set to true, Fluentd waits for the buffer to flush at shutdown. By default, it is set to true for Memory Buffer and false for File Buffer.

### retry\_wait, max\_retry\_wait

The initial and maximum intervals between write retries. The default values are 1.0 seconds and unset (no limit). The interval doubles (with +/-12.5% randomness) every retry until `max_retry_wait` is reached.

Since td-agent will retry 17 times before giving up by default (see the `retry_limit` parameter for details), the sleep interval can be up to approximately 131072 seconds (roughly 36 hours) in the default configurations.

### retry\_limit, disable\_retry\_limit

The limit on the number of retries before buffered data is discarded, and an option to disable that limit (if true, the value of `retry_limit` is ignored and there is no limit). The default values are 17 and false (not disabled). If the limit is reached, buffered data is discarded and the retry interval is reset to its initial value (`retry_wait`).

### num\_threads

The number of threads to flush the buffer. This option can be used to parallelize writes into the output(s) designated by the output plugin. Increasing the number of threads improves the flush throughput to hide write / network latency. The default is 1.

### slow\_flush\_log\_threshold

The threshold for checking chunk flush performance. The default value is `20.0` seconds. Note that parameter type is `float`, not `time`.

If chunk flush takes longer time than this threshold, fluentd logs warning message like below:

```
2016-12-19 12:00:00 +0000 [warn]: buffer flush took longer time than slow_flush_log_threshold: elapsed_time = 15.0031226690043695 slow_flush_log_threshold=10.0 plugin_id="foo"
```

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

## Further Readings

* [fluent-plugin-webhdfs mongo](https://github.com/fluent/fluent-plugin-mongo)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# relabel

The `relabel` output plugin re-labels events.

## Example Configuration

`out_relabel` is included in Fluentd's core. No additional installation process is required.

```
<match pattern>
  @type relabel
  @label @foo
</match>

<label @foo>
  <match patter>
    ...
  </match>
</label>
```

The above example puts a label `@foo` to matched events, and the `label` directive can take care of these events.

FYI: All of input and output plugins also have `@label` parameter provided by Fluentd core. The `relabel` plugin is a plugin which actually does nothing, but supports only `@label` parameter.

## Parameters

### type (required)

The value must be `relabel`.

### label

The label.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# rewrite\_tag\_filter

The `out_rewrite_tag_filter` Output plugin has designed to rewrite tag like mod\_rewrite. Re-emit a record with rewrited tag when a value matches/unmatches with the regular expression. Also you can change a tag from apache log by domain, status-code(ex. 500 error), user-agent, request-uri, regex-backreference and so on with regular expression.

## How it works

It is a sample to arrange the tags by the regexp matched value of 'message'.

```
# Configuration
<match app.message>
  @type rewrite_tag_filter
  <rule>
    key message
    pattern ^\[(\w+)\] $1.${tag}
    tag $1.${tag}
  </rule>
</match>

:::text
+----------------------------------------+        +----------------------------------------------+
| original record                        |        | rewrited tag record                          |
|----------------------------------------|        |----------------------------------------------|
| app.message {"message":"[info]: ..."}  | +----> | info.app.message {"message":"[info]: ..."}   |
| app.message {"message":"[warn]: ..."}  | +----> | warn.app.message {"message":"[warn]: ..."}   |
| app.message {"message":"[crit]: ..."}  | +----> | crit.app.message {"message":"[crit]: ..."}   |
| app.message {"message":"[alert]: ..."} | +----> | alert.app.message {"message":"[alert]: ..."} |
+----------------------------------------+        +----------------------------------------------+
```

## Install

`out_rewrite_tag_filter` is included in td-agent by default (v1.1.18 or later). Fluentd gem users will have to install the fluent-plugin-rewrite-tag-filter gem using the following command.

```
$ fluent-gem install fluent-plugin-rewrite-tag-filter
```

## Example Configuration

Configuration design is dropping some pattern record first, then re-emit other matched record as new tag name.

```
<match apache.access>
  @type rewrite_tag_filter
  capitalize_regex_backreference yes
  <rule>
    key     path
    pattern \.(gif|jpe?g|png|pdf|zip)$
    tag     clear
  </rule>
  <rule>
    key     status
    pattern ^200$
    tag     clear
    invert  true
  </rule>
  <rule>
    key     domain
    pattern ^.+\.com$
    tag     clear
    invert  true
  </rule>
  <rule>
    key     domain
    pattern ^maps\.example\.com$
    tag     site.ExampleMaps
  </rule>
  <rule>
    key     domain
    pattern ^news\.example\.com$
    tag     site.ExampleNews
  </rule>
  # it is also supported regexp back reference.
  <rule>
    key     domain
    pattern ^(mail)\.(example)\.com$
    tag     site.$2$1
  </rule>
  <rule>
    key     domain
    pattern .+
    tag     site.unmatched
  </rule>
</match>

<match clear>
  @type null
</match>
```

Please see the [README.md](https://github.com/fluent/fluent-plugin-rewrite-tag-filter) for further details.

## Parameters

### rewriteruleN (required at least one)

This is deprecated since 1.6.0. Use \ section.

`rewriterule<num> <key> <regex_pattern> <new_tag>`

It works with the order \ ascending, regexp matching \ for the values of \ from each record, re-emit with \\.

### capitalize\_regex\_backreference

Capitalize letter for every matched regex backreference. (ex: maps -> Maps)

### hostname\_command

Override hostname command for placeholder. (default setting is long hostname)

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

### \<rule> section (optional) (multiple)

* **key** (string) (required): The field name to which the regular

  expression is applied
* **pattern** (regexp) (required): The regular expression
* **tag** (string) (required): New tag
* **invert** (bool) (optional): If true, rewrite tag when unmatch

  pattern

  * Default value: `false`

It works with the order of appearance, regexp matching `rule/pattern` for the values of `rule/key` from each record, re-emit with `rule/tag`.

## Placeholders

It is supported these placeholder for new\_tag (rewrited tag). See more details at [README.md](https://github.com/fluent/fluent-plugin-rewrite-tag-filter#tag-placeholder)

* ${tag}
* \_\_TAG\_\_
* {$tag\_parts\[n]}
* \_\_TAG\_PARTS\[n]\_\_
* ${hostname}
* \_\_HOSTNAME\_\_

## Use cases

* Aggregate + display 404 status pages by URL and referrer to find and

  fix dead links.
* Send an IRC alert for 5xx status codes on exceeding thresholds.

#### Aggregate + display 404 status pages by URL and referrer to find and fix dead links.

* Collect access log from multiple application servers (config1)
* Sum up the 404 error and output to mongoDB (config2)

Note: These plugins are required to be installed. \* fluent-plugin-rewrite-tag-filter \* fluent-plugin-mongo

**\[Config1] Application Servers**

```
# Input access log to fluentd with embedded in_tail plugin
<source>
  @type tail
  path /var/log/httpd/access_log
  format apache2
  time_format %d/%b/%Y:%H:%M:%S %z
  tag apache.access
  pos_file /var/log/td-agent/apache_access.pos
</source>

# Forward to monitoring server
<match apache.access>
  @type forward
  flush_interval 5s
  <server>
    name server_name
    host 10.100.1.20
  </server>
</match>
```

**\[Config2] Monitoring Server**

```
# built-in TCP input
<source>
  @type forward
</source>

# Filter record like mod_rewrite with fluent-plugin-rewrite-tag-filter
<match apache.access>
  @type rewrite_tag_filter
  <rule>
    key     status
    pattern ^(?!404)$
    tag     clear
  </rule>
  <rule>
    key      path
    pattern .+
    tag      mongo.apache.access.error404
  </rule>
</match>

# Store deadlinks log into mongoDB
<match mongo.apache.access.error404>
  @type        mongo
  host        10.100.1.30
  database    apache
  collection  deadlinks
  capped
  capped_size 50m
</match>

# Clear tag
<match clear>
  @type null
</match>
```

#### Send an IRC alert for 5xx status codes on exceeding thresholds.

* Collect access log from multiple application servers (config1)
* Sum up the 500 error and notify IRC and logging details to mongoDB

  (config2)

Note: These plugins are required to be installed. \* fluent-plugin-rewrite-tag-filter \* fluent-plugin-datacounter \* fluent-plugin-notifier \* fluent-plugin-parser \* fluent-plugin-mongo \* fluent-plugin-irc

**\[Config1] Application Servers**

```
# Input access log to fluentd with embedded in_tail plugin
# sample results: {"host":"127.0.0.1","user":null,"method":"GET","path":"/","code":500,"size":5039,"referer":null,"agent":"Mozilla"}
<source>
  @type tail
  path /var/log/httpd/access_log
  format apache2
  time_format %d/%b/%Y:%H:%M:%S %z
  tag apache.access
  pos_file /var/log/td-agent/apache_access.pos
</source>

# Forward to monitoring server
<match apache.access>
  @type forward
  flush_interval 5s
  <server>
    name server_name
    host 10.100.1.20
  </server>
</match>
```

**\[Config2] Monitoring Server**

```
# built-in TCP input
<source>
  @type forward
</source>

# Filter record like mod_rewrite with fluent-plugin-rewrite-tag-filter
<match apache.access>
  @type copy
  <store>
    @type rewrite_tag_filter
    # drop static image record and redirect as 'count.apache.access'
    <rule>
      key     path
      pattern ^/(img|css|js|static|assets)/
      tag     clear
    </rule>
    <rule>
      key     path
      pattern .+
      tag     count.apache.access
    </rule>
  </store>
  <store>
    @type rewrite_tag_filter
    <rule>
      key     code
      pattern ^5\d\d$
      tag     mongo.apache.access.error5xx
    </rule>
  </store>
</match>

# Store 5xx error log into mongoDB
<match mongo.apache.access.error5xx>
  @type        mongo
  host        10.100.1.30
  database    apache
  collection  error_5xx
  capped
  capped_size 50m
</match>

# Count by status code
# sample results: {"unmatched_count":0,"unmatched_rate":0.0,"unmatched_percentage":0.0,"200_count":0,"200_rate":0.0,"200_percentage":0.0,"2xx_count":0,"2xx_rate":0.0,"2xx_percentage":0.0,"301_count":0,"301_rate":0.0,"301_percentage":0.0,"302_count":0,"302_rate":0.0,"302_percentage":0.0,"3xx_count":0,"3xx_rate":0.0,"3xx_percentage":0.0,"403_count":0,"403_rate":0.0,"403_percentage":0.0,"404_count":0,"404_rate":0.0,"404_percentage":0.0,"410_count":0,"410_rate":0.0,"410_percentage":0.0,"4xx_count":0,"4xx_rate":0.0,"4xx_percentage":0.0,"5xx_count":1,"5xx_rate":0.01,"5xx_percentage":100.0}
<match count.apache.access>
  @type datacounter
  unit minute
  outcast_unmatched false
  aggregate all
  tag threshold.apache.access
  count_key code
  pattern1 200 ^200$
  pattern2 2xx ^2\d\d$
  pattern3 301 ^301$
  pattern4 302 ^302$
  pattern5 3xx ^3\d\d$
  pattern6 403 ^403$
  pattern7 404 ^404$
  pattern8 410 ^410$
  pattern9 4xx ^4\d\d$
  pattern10 5xx ^5\d\d$
</match>

# Determine threshold
# sample results: {"pattern":"code_500","target_tag":"apache.access","target_key":"5xx_count","check_type":"numeric_upward","level":"warn","threshold":1.0,"value":1.0,"message_time":"2014-01-28 16:47:39 +0900"}
<match threshold.apache.access>
  @type notifier
  input_tag_remove_prefix threshold
  <def>
    pattern code_500
    check numeric_upward
    warn_threshold  10
    crit_threshold  40
    tag alert.http_5xx_error
    target_key_pattern ^5xx_count$
  </def>
</match>

# Generate message
# sample results: {"message":"HTTP Status warn [5xx_count] apache.access: 1.0 (threshold 1.0)"}
<match alert.http_5xx_error>
  @type deparser
  tag irc.http_5xx_error>
  format_key_names level,target_key,target_tag,value,threshold
  format HTTP Status %s [%s] %s: %s (threshold %s)
  key_name message
  reserve_data no
</match>

# Send IRC message
<match irc.http_5xx_error>
  @type irc
  host localhost
  port 6667
  channel fluentd
  nick fluentd
  user fluentd
  real fluentd
  message %s
  out_keys message
</match>

# Clear tag
<match clear>
  @type null
</match>
```

## FAQ

### With rewrite-tag-filter, logs are not forwarded. Why?

If you have following configuration, it doesn't work:

```
<match app.**>
  @type rewrite_tag_filter
  <rule>
    key     level
    pattern (.+)
    tag     app.$1
  </rule>
<match>

<match app.**>
  @type forward
  # ...
</match>
```

In this case, `rewrite_tag_filter` causes infinite loop because fluentd's routing is executed from top to bottom. So you need to change tag like below:

```
<match app.**>
  @type rewrite_tag_filter
  <rule>
    key     level
    pattern (.+)
    tag     level.app.$1
  </rule>
<match>

<match level.app.**>
  @type forward
  # ...
</match>
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Others

Please refer to this list of available plugins to find out about other Output plugins.

* [Fluentd plugins](http://fluentd.org/plugin/)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Buffer Plugins

Fluentd has 6 types of plugins: [Input](https://docs.fluentd.org/input), [Parser](https://docs.fluentd.org/parser), [Filter](https://docs.fluentd.org/filter), [Output](https://docs.fluentd.org/output), [Formatter](https://docs.fluentd.org/formatter) and [Buffer](https://docs.fluentd.org/buffer). This article will provide a high-level overview of Buffer plugins.

## Buffer Plugin Overview

Buffer plugins are used by output plugins. For example, `out_s3` uses `buf_file` plugin by default to store incoming stream temporally before transmitting to S3.

Buffer plugins are, as you can tell by the name, *pluggable*. So you can choose a suitable backend based on your system requirements.

## Buffer Structure

A buffer is essentially a set of "chunks". A chunk is a collection of records concatenated into a single blob. Chunks are periodically flushed to the output queue and then sent to the specified destination. Here is the diagram of how it works:

[![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LkRmVyw0vEoFO0R2Z5g%2F-LkRmhtSsrJifstwe6H_%2Fbuffer-internal-and-parameters.png?generation=1563851157892061\&alt=media)](https://github.com/fluent/fluentd-docs-gitbook/tree/a50cb1d564e1285c59b91c7fade2bf80f05394ce/images/buffer-internal-and-parameters.png)

### Common Parameters

Buffer plugins allow fine-grained controls over the buffering behaviours through config options.

#### `buffer_type`

* This option specifies which plugin to use as the backend.
* In default installations, supported values are `file` and `memory`.

#### `buffer_chunk_limit`

* The maximum size of a chunk allowed (default: 8MB)
* If a chunk grows more than the limit, it gets flushed to the output

  queue automatically.

#### `buffer_queue_limit`

* The maximum length of the output queue (default: 256)
* If the limit gets exceeded, Fluentd will invoke an error handling

  mechanism (See "Handling queue overflow" below for details).

#### `flush_interval`

* The interval in seconds to wait before invoking the next buffer

  flush (default: 60)

### Handling queue overflow

The `buffer_queue_full_action` option controls the behaviour when the queue becomes full. For now, three modes are supported:

1. *exception* (default)
   * This mode raises a `BufferQueueLimitError` exception to the

     input plugin.
   * This mode is suitable for data streaming.
   * It's up to the input plugin to decide how to handle raised

     exceptions.
2. *block*
   * This mode blocks the thread until the free space is vacated.
   * This mode is good for batch-like use-case.
   * DO NOT use this option casually just for avoiding

     `BufferQueueLimitError` exceptions (see the deployment tips

     below).
3. *drop\_oldest\_chunk*
   * This mode drops the oldest chunks.
   * This mode might be useful for monitoring systems, since newer

     events are much more important than the older ones in this

     context.

#### Deployment tips

If your Fluentd daemon experiences overflows frequently, it means that your destination is insufficient for your traffic. There are several measures you can take:

1. Upgrade the destination node to provide enough data-processing

   capacity.
2. Use an `@ERROR` label to route overflowed events to another backup

   destination.
3. Use a `<secondary>` tag to route overflowed events to another backup

   destination.

### Handling write failures

The chunks in the output queue are written out to the destination one by one. However, the problem is that there might occur an error while writing out a chunk. For such cases, buffer plugins are equipped with a "retry" mechanism that handles write failures gracefully.

Here is how it works. If Fluentd fails to write out a chunk, the chunk will not be purged from the queue, and then, after a certain interval, Fluentd will retry to write the chunk again. The intervals between retry attempts are determined by the exponential backoff algorithm, and we can control the behaviour finely through the following options:

#### `retry_limit`

* The maximum number of retries for sending a chunk (default: 17)
* If `retry_limit` is exceeded, Fluentd will discard the given chunk.

#### `disable_retry_limit`

* If set true, it disables `retry_limit` and make Fluentd retry

  indefinitely (default: false).

#### `retry_wait`

* The number of seconds the first retry will wait (default: 1.0)
* This is the seed value used by the exponential backoff algorithm;

  The wait interval will be doubled on each retry.

#### `max_retry_wait`

* The maximum interval seconds to wait between retries (default:

  unset)
* If the wait interval reaches this limit, the exponentiation stops.

## Slicing Data by Time

Buffer plugins support a special mode that groups the incoming data by time frames. For example, you can group the incoming access logs by date and save them to separate files. Under this mode, a buffer plugin will behave quite differently in a few key aspects:

1. It supports the additional `time_slice_*` options (See Q1/Q2 below

   for details)
2. Chunks will be flushed "lazily" based on the settings of the

   `time_slice_format` option. See Q2 for the relationship of this

   option and `flush_interval`.
3. The default value of `buffer_chunk_limit` becomes 256mb.

Normally, the output plugin determines in which mode the buffer plugin operates. For example, `out_s3` and `out_file` will enable the time-slicing mode. For the list of output plugins which enable the time-slicing mode, see [this page](https://docs.fluentd.org/output#list-of-time-sliced-output-plugins).

### FAQ

#### Q1. How do we specify the granularity of time chunks?

This is done through the `time_slice_format` option, which is set to "%Y%m%d" (daily) by default. If you want your chunks to be hourly, "%Y%m%d%H" will do the job.

#### Q2. What if new logs come after the time corresponding the current chunk?

For example, what happens to an event, timestamped at 2013-01-01 02:59:45 UTC, comes in at 2013-01-01 03:00:15 UTC? Would it make into the 2013-01-01 02:00:00-02:59:59 chunk?

This issue is addressed by setting the `time_slice_wait` parameter. `time_slice_wait` sets, in seconds, how long fluentd waits to accept "late" events into the chunk *past the max time corresponding to that chunk*. The default value is 600, which means it waits for 10 minutes before moving on. So, in the current example, as long as the events come in before 2013-01-01 03:10:00, it will make it in to the 2013-01-01 02:00:00-02:59:59 chunk.

Alternatively, you can also flush the chunks regularly using `flush_interval`. Note that `flush_interval` and `time_slice_wait` are mutually exclusive. If you set `flush_interval`, `time_slice_wait` will be ignored and fluentd would issue a warning.

## List of Buffer Plugins

* [buf\_memory](https://docs.fluentd.org/buffer/memory)
* [buf\_file](https://docs.fluentd.org/buffer/file)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# memory

The `memory` buffer plugin provides a fast buffer implementation. It uses memory to store buffer chunks. When Fluentd is shut down, buffered logs that can't be written quickly are deleted.

## Example Config

```
<match pattern>
  buffer_type memory
</match>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

## Parameters

### buffer\_type (required)

The value must be `memory`.

### buffer\_chunk\_limit

The size of each buffer chunk. The default is 8m. The suffixes "k" (KB), "m" (MB), and "g" (GB) can be used. Please see the [Buffer Plugin Overview](https://docs.fluentd.org/buffer) article for the basic buffer structure.

### buffer\_queue\_limit

The length limit of the chunk queue. Please see the [Buffer Plugin Overview](https://docs.fluentd.org/buffer) article for the basic buffer structure. The default limit is 64 chunks.

### flush\_interval

The interval between data flushes. The suffixes "s" (seconds), "m" (minutes), and "h" (hours) can be used

### flush\_at\_shutdown

If true, queued chunks are flushed at shutdown process. The default is `true`. If false, queued chunks are discarded unlike `buf_file`.

### retry\_wait

The interval between retries. The suffixes "s" (seconds), "m" (minutes), and "h" (hours) can be used.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# file

The `file` buffer plugin provides a persistent buffer implementation. It uses files to store buffer chunks on disk.

## Example Config

```
<match pattern>
  buffer_type file
  buffer_path /var/log/fluent/myapp.*.buffer
</match>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

## Parameters

### buffer\_type (required)

The value must be `file`.

### buffer\_path (required)

The path where buffer chunks are stored. The '\*' is replaced with random characters. This parameter is require

This parameter must be unique to avoid race condition problem. For example, you can't use fixed buffer\_path parameter in fluent-plugin-forest. `${tag}` or similar placeholder is needed. Of course, this parameter must also be unique between fluentd instances.

In addition, `buffer_path` should not be an other `buffer_path` prefix. For example, the following conf doesn't work well. `/var/log/fluent/foo` resumes `/var/log/fluent/foo.bar`'s buffer files during start phase and it causes `No such file or directory` in `/var/log/fluent/foo.bar` side.

```
<match pattern1>
    buffer_path /var/log/fluent/foo
</match>

<match pattern2>
    buffer_path /var/log/fluent/foo.bar
</match>
```

Here is the correct version to avoid prefix problem.

```
<match pattern1>
    buffer_path /var/log/fluent/foo.baz
</match>

<match pattern2>
    buffer_path /var/log/fluent/foo.bar
</match>
```

### buffer\_chunk\_limit

The size of each buffer chunk. The default is 8m. The suffixes "k" (KB), "m" (MB), and "g" (GB) can be used. Please see the [Buffer Plugin Overview](https://docs.fluentd.org/buffer) article for the basic buffer structure.

The default value for Time Sliced Plugin is overwritten as 256m.

### buffer\_queue\_limit

The length limit of the chunk queue. Please see the [Buffer Plugin Overview](https://docs.fluentd.org/buffer) article for the basic buffer structure. The default limit is 256 chunks.

### flush\_interval

The interval between data flushes. The suffixes "s" (seconds), "m" (minutes), and "h" (hours) can be used

### flush\_at\_shutdown

If true, queued chunks are flushed at shutdown process. The default is `false`.

### retry\_wait

The interval between retries. The suffixes "s" (seconds), "m" (minutes), and "h" (hours) can be used.

## Limitation

Caution:

`file` buffer implementation depends on the characteristics of local file system. Don't use `file` buffer on remote file system, e.g. NFS, GlusterFS, HDFS and etc. We observed major data loss by using remote file system.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Filter Plugins

Fluentd has 6 types of plugins: [Input](https://docs.fluentd.org/input), [Parser](https://docs.fluentd.org/parser), [Filter](https://docs.fluentd.org/filter), [Output](https://docs.fluentd.org/output), [Formatter](https://docs.fluentd.org/formatter) and [Buffer](https://docs.fluentd.org/buffer). This article gives an overview of Filter Plugin.

## Overview

Filter plugins enables Fluentd to modify event streams. Example use cases are:

1. Filtering out events by grepping the value of one or more fields.
2. Enriching events by adding new fields.
3. Deleting or masking certain fields for privacy and compliance.

## How to Use

It is used with the `<filter>` directive as follows:

```
<filter foo.bar>
  @type grep
  regexp1 message cool
</filter>
```

The above directive matches events with the tag "foo.bar", and if the "message" field's value contains "cool", the events go through the rest of the configuration.

Like the `<match>` directive for output plugins, `<filter>` matches against a tag. Once the event is processed by the filter, the event proceeds through the configuration top-down. Hence, if there are multiple filters for the same tag, they are applied in descending order. Hence, in the following example,

```
<filter foo.bar>
  @type grep
  regexp1 message cool
</filter>

<filter foo.bar>
  @type record_transformer
  <record>
    hostname "#{Socket.gethostname}"
  </record>
</filter>
```

Only the events whose "message" field contain "cool" get the new field "hostname" with the machine's hostname as its value.

Users can create their own custom plugins with a bit of Ruby. See [this section](https://docs.fluentd.org/developer/plugin-development#filter-plugins) for more information.

## List of Filter Plugins

* [grep](https://docs.fluentd.org/filter/grep)
* [record-transformer](https://docs.fluentd.org/filter/record_transformer)
* [filter\_stdout](https://docs.fluentd.org/filter/stdout)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# record\_transformer

The `filter_record_transformer` filter plugin mutates/transforms incoming event streams in a versatile manner. If there is a need to add/delete/modify events, this plugin is the first filter to try.

## Example Configurations

`filter_record_transformer` is included in Fluentd's core. No installation required.

```
<filter foo.bar>
  @type record_transformer
  <record>
    hostname "#{Socket.gethostname}"
    tag ${tag}
  </record>
</filter>
```

The above filter adds the new field "hostname" with the server's hostname as its value (It is taking advantage of Ruby's string interpolation) and the new field "tag" with tag value. So, an input like

```
{"message":"hello world!"}
```

is transformed into

```
{"message":"hello world!", "hostname":"db001.internal.example.com", "tag":"foo.bar"}
```

Here is another example where the field "total" is divided by the field "count" to create a new field "avg":

```
<filter foo.bar>
  @type record_transformer
  enable_ruby
  <record>
    avg ${record["total"] / record["count"]}
  </record>
</filter>
```

It transforms an event like

```
{"total":100, "count":10}
```

into

```
{"total":100, "count":10, "avg":"10"}
```

With the `enable_ruby` option, an arbitrary Ruby expression can be used inside `${...}`. Note that the "avg" field is typed as string in this example. You may use `auto_typecast true` option to treat the field as a float.

You can also use this plugin to modify your existing fields as

```
<filter foo.bar>
  @type record_transformer
  <record>
    message yay, ${record["message"]}
  </record>
</filter>
```

An input like

```
{"message":"hello world!"}
```

is transformed into

```
{"message":"yay, hello world!"}
```

Finally, this configuration embeds the value of the second part of the tag in the field "service\_name". It might come in handy when aggregating data across many services.

```
<filter web.*>
  @type record_transformer
  <record>
    service_name ${tag_parts[1]}
  </record>
</filter>
```

So, if an event with the tag "web.auth" and record `{"user_id":1, "status":"ok"}` comes in, it transforms it into `{"user_id":1, "status":"ok", "service_name":"auth"}`.

## Parameters

### \<record> directive

Parameters inside `<record>` directives are considered to be new key-value pairs:

```
<record>
  NEW_FIELD NEW_VALUE
</record>
```

For NEW\_FIELD and NEW\_VALUE, a special syntax `${}` allows the user to generate a new field dynamically. Inside the curly braces, the following variables are available:

* The incoming event's existing values can be referred by their field

  names. So, if the record is `{"total":100, "count":10}`, then

  `record["total"]=100` and `record["count"]=10`.
* `tag` refers to the whole tag.
* `time` refers to stringanized event time.
* `hostname` refers to machine's hostname. The actual value is result

  of

  [Socket.gethostname](https://docs.ruby-lang.org/en/trunk/Socket.html#method-c-gethostname).

You can also access to a certain potion of a tag using the following notations:

* `tag_parts[N]` refers to the Nth part of the tag.
* `tag_prefix[N]` refers to the \[0..N] part of the tag.
* `tag_suffix[N]` refers to the \[N..] part of the tag.

All indices are zero-based. For example, if you have an incoming event tagged `debug.my.app`, then `tag_parts[1]` will represent "my". Also in this case, `tag_prefix[N]` and `tag_suffix[N]` will work as follows:

```
tag_prefix[0] = debug          tag_suffix[0] = debug.my.app
tag_prefix[1] = debug.my       tag_suffix[1] = my.app
tag_prefix[2] = debug.my.app   tag_suffix[2] = app
```

### enable\_ruby (optional)

When set to true, the full Ruby syntax is enabled in the `${...}` expression. The default value is false.

With `true`, additional variables could be used inside `${}`.

* `record` refers to the whole record.
* `time` refers to event time as Time object, not stringanized event

  time.

Here is the examples:

```
jsonized_record ${record.to_json}
avg ${record["total"] / record["count"]}
formatted_time ${time.strftime('%Y-%m-%dT%H:%M:%S%z')}
escaped_tag ${tag.gsub('.', '-')}
last_tag ${tag_parts.last}
foo_${record["key"]} bar_${record["value"]}
```

### auto\_typecast (optional)

Automatically cast the field types. Default is false.

LIMITATION: This option is effective only for field values comprised of a single placeholder.

Effective Examples:

```
foo ${record["foo"]}
```

Non-Effective Examples:

```
foo ${record["foo"]}${record["bar"]}
foo ${record["foo"]}bar
foo 1
```

Internally, this keeps the original value type only when a single placeholder is used.

### renew\_record (optional)

By default, the record transformer filter mutates the incoming data. However, if this parameter is set to true, it modifies a new empty hash instead.

### renew\_time\_key (optional, string type)

`renew_time_key foo` overwrites the time of events with a value of the record field `foo` if exists. The value of `foo` must be a unix time.

### keep\_keys (optional, array type)

A list of keys to keep. Only relevant if `renew_record` is set to true.

### remove\_keys (optional, array type)

A list of keys to delete.

## Need more performance?

[filter\_record\_modifier](https://github.com/repeatedly/fluent-plugin-record-modifier) is light-weight and faster version of `filter_record_transformer`. `filter_record_modifier` doesn't provide several `filter_record_transformer` features, but it covers popular cases. If you need better performace for mutating records, consider `filter_record_modifier` instead.

## FAQ

### What are the differences between `${record["key"]}` and `${key}`?

`${key}` is short-cut for `${record["key"]}`. This is error prone because `${tag}` is unclear for event tag or `record["tag"]`. So the `${key}` syntax is now deprecated for avoiding this problem. Don't use `${key}` short-cut syntax on the production.

Since v0.14, `${key}` short-cut syntax is removed.

## Learn More

* [Filter Plugin Overview](https://docs.fluentd.org/filter)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# grep

The `filter_grep` filter plugin "greps" events by the values of specified fields.

## Example Configurations

`filter_grep` is included in Fluentd's core. No installation required.

```
<filter foo.bar>
  @type grep
  <regexp>
    key message
    pattern cool
  </regexp>
  <regexp>
    key hostname
    pattern ^web\d+\.example\.com$
  </regexp>
  <exclude>
    key message
    pattern uncool
  </exclude>
</filter>
```

The above example matches any event that satisfies the following conditions:

1. The value of the "message" field contains "cool"
2. The value of the "hostname" field matches

   `web<INTEGER>.example.com`.
3. The value of the "message" field does NOT contain "uncool".

Hence, the following events are kept:

```
{"message":"It's cool outside today", "hostname":"web001.example.com"}
{"message":"That's not cool", "hostname":"web1337.example.com"}
```

whereas the following examples are filtered out:

```
{"message":"I am cool but you are uncool", "hostname":"db001.example.com"}
{"hostname":"web001.example.com"}
{"message":"It's cool outside today"}
```

## Parameters

### \<regexp> directive (optional)

Specify filtering rule. This directive contains two parameters. This parameter is available since v0.12.38.

* key

The field name to which the regular expression is applied.

* pattern

The regular expression.

For example, the following filters out events unless the field "price" is a positive integer.

```
<regexp>
  key price
  pattern [1-9]\d*
</regexp>
```

The grep filter filters out UNLESS all `<regexp>`s are matched. Hence, if you have

```
<regexp>
  key price
  pattern [1-9]\d*
</regexp>
<regexp>
  key item_name
  pattern ^book_
</regexp>
```

unless the event's "item\_name" field starts with "book\_" and the "price" field is an integer, it is filtered out.

For OR condition, you can use `|` operator of regular expressions. For example, if you have

```
<regexp>
  key item_name
  pattern (^book_|^article)
</regexp>
```

unless the event's "item\_name" field starts with "boo&#x6B;*" or "article*", it is filtered out.

Learn regular expressions for more patterns.

### regexpN (optional)

This is deprecated parameter. Use `<regexp>` instead if you use v0.12.38 or later.

The "N" at the end should be replaced with an integer between 1 and 20 (ex: "regexp1"). regexpN takes two whitespace-delimited arguments.

Here is `regexpN` version of `<regexp>` example:

```
regexp1 price [1-9]\d*
regexp2 item_name ^book_
```

### \<exclude> directive (optional)

Specify filtering rule to reject events. This directive contains two parameters. This parameter is available since v0.12.38.

* key

The field name to which the regular expression is applied.

* pattern

The regular expression.

For example, the following filters out events whose "status\_code" field is 5xx.

```
<exclude>
  key status_code
  pattern ^5\d\d$
</exclude>
```

The grep filter filters out if any `<exclude>` is matched. Hence, if you have

```
<exclude>
  key status_code
  pattern ^5\d\d$
</exclude>
<exclude>
  key url
  pattern \.css$
</exclude>
```

Then, any event whose "status\_code" is 5xx OR "url" ends with ".css" is filtered out.

### excludeN (optional)

This is deprecated parameter. Use `<exclude>` instead if you use v0.12.38 or later.

The "N" at the end should be replaced with an integer between 1 and 20 (ex: "exclude1"). excludeN takes two whitespace-delimited arguments.

Here is `excludeN` version of `<exclude>` example:

```
exclude1 status_code ^5\d\d$
exclude2 url \.css$
```

If `<regexp>` and `<exclude>` are used together, both are applied.

## Learn More

* [Filter Plugin Overview](https://docs.fluentd.org/filter)
* [record\_transformer Filter Plugin](https://docs.fluentd.org/filter/record_transformer)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# parser

The `filter_parser` filter plugin "parses" string field in event records and mutates its event record with parsed result.

## Example Configurations

`filter_parser` is included in Fluentd's core since v0.12.29. No installation required. If you want to use `filter_parser` with lower fluentd versions, need to install `fluent-plugin-parser`.

`filter_parser` has just same with `in_tail` about `format` and `time_format`:

```
<filter foo.bar>
  @type parser
  format /^(?<host>[^ ]*) [^ ]* (?<user>[^ ]*) \[(?<time>[^\]]*)\] "(?<method>\S+)(?: +(?<path>[^ ]*) +\S*)?" (?<code>[^ ]*) (?<size>[^ ]*)$/
  time_format %d/%b/%Y:%H:%M:%S %z
  key_name message
</filter>
```

`filter_parser` uses built-in parser plugins and your own customized parser plugin, so you can re-use pre-defined format like `apache`, `json` and etc. See document page for more details: [Parser Plugin Overview](https://docs.fluentd.org/parser)

## Parameters

### format

This is required parameter. Specify parser format or regexp pattern.

### key\_name

This is required parameter. Specify field name in the record to parse.

### reserve\_data

Keep original key-value pair in parsed result. Default is `false`.

```
<filter foo.bar>
  @type parser
  format json
  key_name log
  reserve_data true
</filter>
```

With above configuration, result is below:

```
# input data:  {"key":"value","log":"{\"user\":1,\"num\":2}"}
# output data: {"key":"value","log":"{\"user\":1,\"num\":2}","user":1,"num":2}
```

Without `reserve_data`, result is below

```
# input data:  {"key":"value","log":"{\"user\":1,\"num\":2}"}
# output data: {"user":1,"num":2}
```

### suppress\_parse\_error\_log

If `true`, a plugin suppresses `pattern not match` warning log. Default is `false`.

This parameter is useful for parsing mixed logs and you want to ignore non target lines.

### ignore\_key\_not\_exist

Ignore "key not exist" log. Default is `false`.

Useful case is same with `suppress_parse_error_log`.

### replace\_invalid\_sequence

If `true`, invalid string is replaced with safe characters and re-parse it. Default is `false`.

### inject\_key\_prefix

Store parsed values with specified key name prefix. Default is `nil`.

```
<filter foo.bar>
  @type parser
  format json
  key_name log
  reserve_data true
  inject_key_prefix data.
</filter>
```

With above configuration, result is below:

```
# input data:  {"log": "{\"user\":1,\"num\":2}"}
# output data: {"log":"{\"user\":1,\"num\":2}","data.user":1, "data.num":2}
```

### hash\_value\_field

Store parsed values as a hash value in a field. Default is `nil`.

```
<filter foo.bar>
  @type parser
  format json
  key_name log
  hash_value_field parsed
</filter>
```

With above configuration, result is below:

```
# input data:  {"log": "{\"user\":1,\"num\":2}"}
# output data: {"parsed":{"user":1,"num":2}}
```

### time\_parse

If false, time parsing is disabled in the parser. Default is true.

### emit\_invalid\_record\_to\_error

Emit invalid record to `@ERROR` label. Default is `false`. Invalid cases are

* key not exist
* format is not matched
* unexpected error

You can rescue unexpected format logs in `@ERROR` label.

## Learn More

* [Filter Plugin Overview](https://docs.fluentd.org/filter)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# stdout

The `filter_stdout` filter plugin prints events to stdout (or logs if launched with daemon mode). This filter plugin is useful for debugging purposes.

## Example Configurations

`filter_stdout` is included in Fluentd's core. No installation required.

```
<filter pattern>
  @type stdout
</filter>
```

A sample output is as follows:

```
2015-05-02 12:12:17 +0900 tag: {"field1":"value1","field2":"value2"}
```

where the first part shows the output time, the second part shows the tag, and the third part shows the record. The first part shows the \*\*output\*\* time, not the time attribute of message event structure as \`out\_stdout\` does.

## Parameters

### type (required)

The value must be `stdout`.

### format

The format of the output. The default is `stdout`.

### output\_type

This is the option of `stdout` format. Configure the format of record (third part). Any formatter plugins can be specified. The default is `json`.

### out\_file

Output time, tag and json record separated by a delimiter:

```
time[delimiter]tag[delimiter]record\n
```

Example:

```
2014-06-08T23:59:40[TAB]file.server.logs[TAB]{"field1":"value1","field2":"value2"}\n
```

`out_file` format has several options to customize the format.

```
delimiter SPACE   # Optional, SPACE or COMMA. "\t"(TAB) is used by default
output_tag false  # Optional, defaults to true. Output the tag field if true.
output_time true  # Optional, defaults to true. Output the time field if true.
```

For this format, the following common parameters are also supported.

* **include\_time\_key** (Boolean, Optional, defaults to false) If

  true, the time field (as specified by the `time_key` parameter) is

  kept in the record.
* **time\_key** (String, Optional, defaults to "time") The field name

  for the time key.
* **time\_format** (String. Optional) By default, the output format is

  iso8601 (e.g. "2008-02-01T21:41:49"). One can specify their own

  format with this parameter.
* **include\_tag\_key** (Boolean. Optional, defaults to false) If

  true, the tag field (as specified by the `tag_key` parameter) is

  kept in the record.
* **tag\_key** (String, Optional, defaults to "tag") The field name

  for the tag key.
* **localtime** (Boolean. Optional, defaults to true) If true, use

  local time. Otherwise, UTC is used. This parameter is overwritten by

  the `utc` parameter.
* **timezone** (String. Optional) By setting this parameter, one can parse the time value in the specified timezone. The following formats are accepted:

  1. \[+-]HH:MM (e.g. "+09:00")
  2. \[+-]HHMM (e.g. "+0900")
  3. \[+-]HH (e.g. "+09")
  4. Region/Zone (e.g. "Asia/Tokyo")
  5. Region/Zone/Zone (e.g. "America/Argentina/Buenos\_Aires")

  **The timezone set in this parameter takes precedence over `localtime`**, e.g., if `localtime` is set to `true` but `timezone` is set to `+0000`, UTC would be used.

### json

Output a json record without the time or tag field:

```
{"field1":"value1","field2":"value2"}\n
```

For this format, the following common parameters are also supported.

* **include\_time\_key** (Boolean, Optional, defaults to false) If

  true, the time field (as specified by the `time_key` parameter) is

  kept in the record.
* **time\_key** (String, Optional, defaults to "time") The field name

  for the time key.
* **time\_format** (String. Optional) By default, the output format is

  iso8601 (e.g. "2008-02-01T21:41:49"). One can specify their own

  format with this parameter.
* **include\_tag\_key** (Boolean. Optional, defaults to false) If

  true, the tag field (as specified by the `tag_key` parameter) is

  kept in the record.
* **tag\_key** (String, Optional, defaults to "tag") The field name

  for the tag key.
* **localtime** (Boolean. Optional, defaults to true) If true, use

  local time. Otherwise, UTC is used. This parameter is overwritten by

  the `utc` parameter.
* **timezone** (String. Optional) By setting this parameter, one can parse the time value in the specified timezone. The following formats are accepted:

  1. \[+-]HH:MM (e.g. "+09:00")
  2. \[+-]HHMM (e.g. "+0900")
  3. \[+-]HH (e.g. "+09")
  4. Region/Zone (e.g. "Asia/Tokyo")
  5. Region/Zone/Zone (e.g. "America/Argentina/Buenos\_Aires")

  **The timezone set in this parameter takes precedence over `localtime`**, e.g., if `localtime` is set to `true` but `timezone` is set to `+0000`, UTC would be used.

### hash

Output a record as ruby hash without the time or tag field:

```
{"field1"=>"value1","field2"=>"value2"}\n
```

For this format, the following common parameters are also supported.

* **include\_time\_key** (Boolean, Optional, defaults to false) If

  true, the time field (as specified by the `time_key` parameter) is

  kept in the record.
* **time\_key** (String, Optional, defaults to "time") The field name

  for the time key.
* **time\_format** (String. Optional) By default, the output format is

  iso8601 (e.g. "2008-02-01T21:41:49"). One can specify their own

  format with this parameter.
* **include\_tag\_key** (Boolean. Optional, defaults to false) If

  true, the tag field (as specified by the `tag_key` parameter) is

  kept in the record.
* **tag\_key** (String, Optional, defaults to "tag") The field name

  for the tag key.
* **localtime** (Boolean. Optional, defaults to true) If true, use

  local time. Otherwise, UTC is used. This parameter is overwritten by

  the `utc` parameter.
* **timezone** (String. Optional) By setting this parameter, one can parse the time value in the specified timezone. The following formats are accepted:

  1. \[+-]HH:MM (e.g. "+09:00")
  2. \[+-]HHMM (e.g. "+0900")
  3. \[+-]HH (e.g. "+09")
  4. Region/Zone (e.g. "Asia/Tokyo")
  5. Region/Zone/Zone (e.g. "America/Argentina/Buenos\_Aires")

  **The timezone set in this parameter takes precedence over `localtime`**, e.g., if `localtime` is set to `true` but `timezone` is set to `+0000`, UTC would be used.

### ltsv

Output the record as [LTSV](http://ltsv.org):

```
field1[label_delimiter]value1[delimiter]field2[label_delimiter]value2\n
```

`ltsv` format supports `delimiter` and `label_delimiter` options.

```
format ltsv
delimiter SPACE   # Optional. "\t"(TAB) is used by default
label_delimiter = # Optional. ":" is used by default
```

For this format, the following common parameters are also supported.

* **include\_time\_key** (Boolean, Optional, defaults to false) If

  true, the time field (as specified by the `time_key` parameter) is

  kept in the record.
* **time\_key** (String, Optional, defaults to "time") The field name

  for the time key.
* **time\_format** (String. Optional) By default, the output format is

  iso8601 (e.g. "2008-02-01T21:41:49"). One can specify their own

  format with this parameter.
* **include\_tag\_key** (Boolean. Optional, defaults to false) If

  true, the tag field (as specified by the `tag_key` parameter) is

  kept in the record.
* **tag\_key** (String, Optional, defaults to "tag") The field name

  for the tag key.
* **localtime** (Boolean. Optional, defaults to true) If true, use

  local time. Otherwise, UTC is used. This parameter is overwritten by

  the `utc` parameter.
* **timezone** (String. Optional) By setting this parameter, one can parse the time value in the specified timezone. The following formats are accepted:

  1. \[+-]HH:MM (e.g. "+09:00")
  2. \[+-]HHMM (e.g. "+0900")
  3. \[+-]HH (e.g. "+09")
  4. Region/Zone (e.g. "Asia/Tokyo")
  5. Region/Zone/Zone (e.g. "America/Argentina/Buenos\_Aires")

  **The timezone set in this parameter takes precedence over `localtime`**, e.g., if `localtime` is set to `true` but `timezone` is set to `+0000`, UTC would be used.

### single\_value

Output the value of a single field instead of the whole record. Often used in conjunction with [in\_tail](https://docs.fluentd.org/input/tail)'s `format none`.

```
value1\n
```

`single_value` format supports the `add_newline` and `message_key` options.

```
add_newline false # Optional, defaults to true. If there is a trailing "\n" already, set it "false"
message_key my_field # Optional, defaults to "message". The value of this field is outputted.
```

### csv

Output the record as CSV/TSV:

```
"value1"[delimiter]"value2"[delimiter]"value3"\n
```

`csv` format supports the `delimiter` and `force_quotes` options.

```
format csv
fields field1,field2,field3
delimiter \t   # Optional. "," is used by default.
force_quotes false # Optional. true is used by default. If false, value won't be framed by quotes.
```

For this format, the following common parameters are also supported.

* **include\_time\_key** (Boolean, Optional, defaults to false) If

  true, the time field (as specified by the `time_key` parameter) is

  kept in the record.
* **time\_key** (String, Optional, defaults to "time") The field name

  for the time key.
* **time\_format** (String. Optional) By default, the output format is

  iso8601 (e.g. "2008-02-01T21:41:49"). One can specify their own

  format with this parameter.
* **include\_tag\_key** (Boolean. Optional, defaults to false) If

  true, the tag field (as specified by the `tag_key` parameter) is

  kept in the record.
* **tag\_key** (String, Optional, defaults to "tag") The field name

  for the tag key.
* **localtime** (Boolean. Optional, defaults to true) If true, use

  local time. Otherwise, UTC is used. This parameter is overwritten by

  the `utc` parameter.
* **timezone** (String. Optional) By setting this parameter, one can parse the time value in the specified timezone. The following formats are accepted:

  1. \[+-]HH:MM (e.g. "+09:00")
  2. \[+-]HHMM (e.g. "+0900")
  3. \[+-]HH (e.g. "+09")
  4. Region/Zone (e.g. "Asia/Tokyo")
  5. Region/Zone/Zone (e.g. "America/Argentina/Buenos\_Aires")

  **The timezone set in this parameter takes precedence over `localtime`**, e.g., if `localtime` is set to `true` but `timezone` is set to `+0000`, UTC would be used.

### stdout

This format is aimed to be used by stdout plugins.

Output time, tag and formatted record as follows:

```
time tag: formatted_record\n
```

Example:

```
2015-05-02 12:12:17 +0900 tag: {"field1":"value1","field2":"value2"}\n
```

`stdout` format has a following option to customize the format of the record part.

```
output_type format # Optional, defaults to "json". The format of
`formatted_record`. Any formatter plugins can be specified.
```

For this format, the following common parameters are also supported.

* **include\_time\_key** (Boolean, Optional, defaults to false) If

  true, the time field (as specified by the `time_key` parameter) is

  kept in the record.
* **time\_key** (String, Optional, defaults to "time") The field name

  for the time key.
* **time\_format** (String. Optional) By default, the output format is

  iso8601 (e.g. "2008-02-01T21:41:49"). One can specify their own

  format with this parameter.
* **include\_tag\_key** (Boolean. Optional, defaults to false) If

  true, the tag field (as specified by the `tag_key` parameter) is

  kept in the record.
* **tag\_key** (String, Optional, defaults to "tag") The field name

  for the tag key.
* **localtime** (Boolean. Optional, defaults to true) If true, use

  local time. Otherwise, UTC is used. This parameter is overwritten by

  the `utc` parameter.
* **timezone** (String. Optional) By setting this parameter, one can parse the time value in the specified timezone. The following formats are accepted:

  1. \[+-]HH:MM (e.g. "+09:00")
  2. \[+-]HHMM (e.g. "+0900")
  3. \[+-]HH (e.g. "+09")
  4. Region/Zone (e.g. "Asia/Tokyo")
  5. Region/Zone/Zone (e.g. "America/Argentina/Buenos\_Aires")

  **The timezone set in this parameter takes precedence over `localtime`**, e.g., if `localtime` is set to `true` but `timezone` is set to `+0000`, UTC would be used.

### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/deployment/logging) for further details.

## Learn More

* [Filter Plugin Overview](https://docs.fluentd.org/filter)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Parser Plugins

Fluentd has 6 types of plugins: [Input](https://docs.fluentd.org/input), [Parser](https://docs.fluentd.org/parser), [Filter](https://docs.fluentd.org/filter), [Output](https://docs.fluentd.org/output), [Formatter](https://docs.fluentd.org/formatter) and [Buffer](https://docs.fluentd.org/buffer). This article gives an overview of Parser Plugin.

## Overview

Sometimes, the `format` parameter for input plugins (ex: [in\_tail](https://docs.fluentd.org/input/tail), [in\_syslog](https://docs.fluentd.org/input/syslog), [in\_tcp](https://docs.fluentd.org/input/tcp) and [in\_udp](https://docs.fluentd.org/input/udp)) cannot parse the user's custom data format (for example, a context-dependent grammar that can't be parsed with a regular expression). To address such cases. Fluentd has a pluggable system that enables the user to create their own parser formats.

## How To Use

* Write a custom format plugin. [See here for more information](https://docs.fluentd.org/developer/plugin-development#parser-plugins).
* From any input plugin that supports the "format" field, call the

  custom plugin by its name.

Here is a simple example to read Nginx access logs using `in_tail` and `parser_nginx`:

```
<source>
  @type tail
  path /path/to/input/file
  format nginx
  keep_time_key true
</source>
```

## List of Built-in Parsers

* [regexp](https://docs.fluentd.org/parser/regexp)
* [apache2](https://docs.fluentd.org/parser/apache2)
* [apache\_error](https://docs.fluentd.org/parser/apache_error)
* [nginx](https://docs.fluentd.org/parser/nginx)
* [syslog](https://docs.fluentd.org/parser/syslog)
* [csv](https://docs.fluentd.org/parser/csv)
* [tsv](https://docs.fluentd.org/parser/tsv)
* [ltsv](https://docs.fluentd.org/parser/ltsv)
* [json](https://docs.fluentd.org/parser/json)
* [multiline](https://docs.fluentd.org/parser/multiline)
* [none](https://docs.fluentd.org/parser/none)

### 3rd party Parsers

* [grok](https://github.com/fluent/fluent-plugin-grok-parser)

If you are familiar with grok patterns, grok-parser plugin is useful. Use `< 1.0.0` versions for fluentd v0.12.

## List of Core Input Plugins with Parser support

with `format` parameter.

* [in\_tail](https://docs.fluentd.org/input/tail)
* [in\_tcp](https://docs.fluentd.org/input/tcp)
* [in\_udp](https://docs.fluentd.org/input/udp)
* [in\_syslog](https://docs.fluentd.org/input/syslog)
* [in\_http](https://docs.fluentd.org/input/http)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# regexp

The `regexp` parser plugin parses logs by given regexp pattern. If the parameter value starts and ends with "/", it is considered to be a regexp. The regexp must have at least one named capture (?\PATTERN). If the regexp has a capture named `time`, this is configurable, it is used as the time of the event. You can specify the time format using the time\_format parameter.

```
format /.../ # regexp parser is used
format json  # json parser is used
```

## Parameters

### time\_key

Specify the field for event time. Default is `time`.

### time\_format

Specify time format for `time_key`.

See [Time#strptime](http://ruby-doc.org/stdlib-2.4.1/libdoc/time/rdoc/Time.html#method-c-strptime) for additional format information.

### keep\_time\_key

If you want to keep time field in the record, set `true`. Default is `false`.

### types

Although every parsed field has type `string` by default, you can specify other types. This is useful when filtering particular fields numerically or storing data with sensible type information.

The syntax is

```
types <field_name_1>:<type_name_1>,<field_name_2>:<type_name_2>,...
```

e.g.,

```
types user_id:integer,paid:bool,paid_usd_amount:float
```

As demonstrated above, "," is used to delimit field-type pairs while ":" is used to separate a field name with its intended type.

Unspecified fields are parsed at the default string type.

The list of supported types are shown below:

* string
* bool
* integer ("int" would NOT work!)
* float
* time
* array

For the `time` and `array` types, there is an optional third field after the type name. For the "time" type, you can specify a time format like you would in `time_format`.

For the "array" type, the third field specifies the delimiter (the default is ","). For example, if a field called "item\_ids" contains the value "3,4,5", `types item_ids:array` parses it as \["3", "4", "5"]. Alternatively, if the value is "Adam|Alice|Bob", `types item_ids:array:|` parses it as \["Adam", "Alice", "Bob"].

## Example

```
format /^\[(?<logtime>[^\]]*)\] (?<name>[^ ]*) (?<title>[^ ]*) (?<id>\d*)$/
time_key logtime
time_format %Y-%m-%d %H:%M:%S %z
types id:integer
```

With this config:

```
[2013-02-28 12:00:00 +0900] alice engineer 1
```

This incoming log is parsed as:

```
time:
1362020400 (2013-02-28 12:00:00 +0900)

record:
{
  "name" : "alice",
  "title": "engineer",
  "id"   : 1
}
```

## FAQ

### How to debug my regexp pattern?

[fluentd-ui's in\_tail editor](https://docs.fluentd.org/deployment/fluentd-ui#intail-setting) helps your regexp testing. Another way, [Fluentular](http://fluentular.herokuapp.com/) is a great website to test your regexp for Fluentd configuration.

NOTE: You may hit Application Error at Fluentular due to [heroku free plan limitation](https://www.heroku.com/pricing). Retry a few hours later or use fluentd-ui instead.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# apache2

The `apache2` parser plugin parses apache2 logs.

## Parameters

### keep\_time\_key

If you want to keep time field in the record, set `true`. Default is `false`.

## Regexp patterns

This is regexp and time format patterns of this plugin:

```
format /^(?<host>[^ ]*) [^ ]* (?<user>[^ ]*) \[(?<time>[^\]]*)\] "(?<method>\S+)(?: +(?<path>[^ ]*) +\S*)?" (?<code>[^ ]*) (?<size>[^ ]*)(?: "(?<referer>[^\"]*)" "(?<agent>[^\"]*)")?$/
time_format %d/%b/%Y:%H:%M:%S %z
```

`host`, `user`, `method`, `path`, `code`, `size`, `referer` and `agent` are included in the event record. `time` is used for the event time.

`code` and `size` fields are converted into integer type automatically. And if the field value is `-`, it is interpreted as `nil`. See "Result Example".

## Example

```
192.168.0.1 - - [28/Feb/2013:12:00:00 +0900] "GET / HTTP/1.1" 200 777 "-" "Opera/12.0"
```

This incoming event is parsed as:

```
time:
1362020400 (28/Feb/2013:12:00:00 +0900)

record:
{
  "user"   : nil,
  "method" : "GET",
  "code"   : 200,
  "size"   : 777,
  "host"   : "192.168.0.1",
  "path"   : "/",
  "referer": nil,
  "agent"  : "Opera/12.0"
}
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# apache\_error

The `apache_error` parser plugin parses apache error logs.

## Parameters

### keep\_time\_key

If you want to keep time field in the record, set `true`. Default is `false`.

### types

Although every parsed field has type `string` by default, you can specify other types. This is useful when filtering particular fields numerically or storing data with sensible type information.

The syntax is

```
types <field_name_1>:<type_name_1>,<field_name_2>:<type_name_2>,...
```

e.g.,

```
types user_id:integer,paid:bool,paid_usd_amount:float
```

As demonstrated above, "," is used to delimit field-type pairs while ":" is used to separate a field name with its intended type.

Unspecified fields are parsed at the default string type.

The list of supported types are shown below:

* string
* bool
* integer ("int" would NOT work!)
* float
* time
* array

For the `time` and `array` types, there is an optional third field after the type name. For the "time" type, you can specify a time format like you would in `time_format`.

For the "array" type, the third field specifies the delimiter (the default is ","). For example, if a field called "item\_ids" contains the value "3,4,5", `types item_ids:array` parses it as \["3", "4", "5"]. Alternatively, if the value is "Adam|Alice|Bob", `types item_ids:array:|` parses it as \["Adam", "Alice", "Bob"].

## Regexp patterns

This is regexp pattern of this plugin:

```
format /^\[[^ ]* (?<time>[^\]]*)\] \[(?<level>[^\]]*)\](?: \[pid (?<pid>[^\]]*)\])? \[client (?<client>[^\]]*)\] (?<message>.*)$/
```

`level`, `pid`, `client` and `message` are included in the event record. `time` is used for the event time.

## Example

```
[Wed Oct 11 14:32:52 2000] [error] [client 127.0.0.1] client denied by server configuration
```

This incoming event is parsed as:

```
time:
971242372 (Wed Oct 11 14:32:52 2000)

record:
{
  "level"  : "error",
  "client" : "127.0.0.1",
  "message": "client denied by server configuration"
}
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# nginx

The `nginx` parser plugin parses default nginx logs.

## Parameters

### keep\_time\_key

If you want to keep time field in the record, set `true`. Default is `false`.

### types

Although every parsed field has type `string` by default, you can specify other types. This is useful when filtering particular fields numerically or storing data with sensible type information.

The syntax is

```
types <field_name_1>:<type_name_1>,<field_name_2>:<type_name_2>,...
```

e.g.,

```
types user_id:integer,paid:bool,paid_usd_amount:float
```

As demonstrated above, "," is used to delimit field-type pairs while ":" is used to separate a field name with its intended type.

Unspecified fields are parsed at the default string type.

The list of supported types are shown below:

* string
* bool
* integer ("int" would NOT work!)
* float
* time
* array

For the `time` and `array` types, there is an optional third field after the type name. For the "time" type, you can specify a time format like you would in `time_format`.

For the "array" type, the third field specifies the delimiter (the default is ","). For example, if a field called "item\_ids" contains the value "3,4,5", `types item_ids:array` parses it as \["3", "4", "5"]. Alternatively, if the value is "Adam|Alice|Bob", `types item_ids:array:|` parses it as \["Adam", "Alice", "Bob"].

## Regexp patterns

This is regexp and time format patterns of this plugin:

```
format /^(?<remote>[^ ]*) (?<host>[^ ]*) (?<user>[^ ]*) \[(?<time>[^\]]*)\] "(?<method>\S+)(?: +(?<path>[^\"]*) +\S*)?" (?<code>[^ ]*) (?<size>[^ ]*)(?: "(?<referer>[^\"]*)" "(?<agent>[^\"]*)")?$/
time_format %d/%b/%Y:%H:%M:%S %z
```

`remote`, `user`, `method`, `path`, `code`, `size`, `referer` and `agent` are included in the event record. `time` is used for the event time.

## Example

```
127.0.0.1 192.168.0.1 - [28/Feb/2013:12:00:00 +0900] "GET / HTTP/1.1" 200 777 "-" "Opera/12.0"
```

This incoming event is parsed as:

```
time:
1362020400 (28/Feb/2013:12:00:00 +0900)

record:
{
  "remote" : "127.0.0.1",
  "host"   : "192.168.0.1",
  "user"   : "-",
  "method" : "GET",
  "path"   : "/",
  "code"   : "200",
  "size"   : "777",
  "referer": "-",
  "agent"  : "Opera/12.0"
}
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# syslog

The `syslog` parser plugin parses syslog generated logs. This plugin supports two RFC formats, rfc3164 and rfc5424.

## Parameters

### time\_format

Specify time format for event time. Default is "%b %d %H:%M:%S" for rfc3164 protocol.

### message\_format

Specify protocol format. Supported values are `rfc3164`, `rfc5424` and `auto`. Default is `rfc3164`. If your syslog uses `rfc5424`, use `rfc5424` instead.

`auto` is useful when this parser receives both `rfc3164` and `rfc5424` message. `syslog` parser detects message format by using message prefix.

This parameter is used inside `in_syslog` plugin because the file logs via syslog don't have `<9>` like priority prefix.

### with\_priority

If the incoming logs have priority prefix, e.g. \\, set `true`. Default is `false`.

### keep\_time\_key

If you want to keep time field in the record, set `true`. Default is `false`.

## Regexp patterns

### rfc3164 pattern

```
format /^\<(?<pri>[0-9]+)\>(?<time>[^ ]* {1,2}[^ ]* [^ ]*) (?<host>[^ ]*) (?<ident>[a-zA-Z0-9_\/\.\-]*)(?:\[(?<pid>[0-9]+)\])?(?:[^\:]*\:)? *(?<message>.*)$/
time_format "%b %d %H:%M:%S"
```

`pri`, `host`, `ident`, `pid` and `message` are included in the event record. `time` is used for the event time.

`pri` value is converted into integer type.

If `with_priority` is `false`, `^\<(?<pri>[0-9]+)\>` is removed from the pattern.

### rfc5424 pattern

```
format /\A^\<(?<pri>[0-9]{1,3})\>[1-9]\d{0,2} (?<time>[^ ]+) (?<host>[^ ]+) (?<ident>[^ ]+) (?<pid>[-0-9]+) (?<msgid>[^ ]+) (?<extradata>(\[(.*)\]|[^ ])) (?<message>.+)$\z/
time_format "%Y-%m-%dT%H:%M:%S.%L%z"
```

`pri`, `host`, `ident`, `pid`, `msgid`, `extradata` and `message` are included in the event record. `time` is used for the event time.

`pri` value is converted into integer type.

## Example

### rfc3164 log

```
<6>Feb 28 12:00:00 192.168.0.1 fluentd[11111]: [error] Syslog test
```

This incoming event is parsed as:

```
time:
1362020400 (Feb 28 12:00:00)

record:
{
  "pri"    : 6,
  "host"   : "192.168.0.1",
  "ident"  : "fluentd",
  "pid"    : "11111",
  "message": "[error] Syslog test"
}
```

### rfc5424 log

```
<16>1 2013-02-28T12:00:00.003Z 192.168.0.1 fluentd 11111 ID24224 [exampleSDID@20224 iut="3" eventSource="Application" eventID="11211"] Hi, from Fluentd!
```

This incoming event is parsed as:

```
time:
1362052800 (2013-02-28T12:00:00.003Z)

record:
{
  "pri"      : 16,
  "host"     : "192.168.0.1",
  "ident"    : "fluentd",
  "pid"      : "11111",
  "msgid"    : "ID24224",
  "extradata": "[exampleSDID@20224 iut=\"3\" eventSource=\"Application\" eventID=\"11211\"]",
  "message"  : "Hi, from Fluentd!"
}
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# ltsv

The `ltsv` parser plugin parses [LTSV](http://ltsv.org/) format.

## Parameters

### delimiter

Specify field delimiter. Default is `\t`.

### label\_delimiter

Specify key-value delimiter. Default is `:`.

### time\_key

Specify time field for event time. Default is `time`.

If there is no time field in the record, this parser uses current time as an event time.

### time\_format

If time field value is formatted string, e.g. "28/Feb/2013:12:00:00 +0900", you need to specify this parameter to parse it.

Default is `nil` and it uses `Time.parse` method to parse the field.

See [Time#strptime](http://ruby-doc.org/stdlib-2.4.1/libdoc/time/rdoc/Time.html#method-c-strptime) for additional format information.

### null\_value\_pattern

Specify null value pattern. Default is `nil`.

If given field value is matched with this pattern, the field value is replaced with `nil`.

### null\_empty\_string

If `true`, empty string field is replaced with `nil`. Default is `false`.

### types

Although every parsed field has type `string` by default, you can specify other types. This is useful when filtering particular fields numerically or storing data with sensible type information.

The syntax is

```
types <field_name_1>:<type_name_1>,<field_name_2>:<type_name_2>,...
```

e.g.,

```
types user_id:integer,paid:bool,paid_usd_amount:float
```

As demonstrated above, "," is used to delimit field-type pairs while ":" is used to separate a field name with its intended type.

Unspecified fields are parsed at the default string type.

The list of supported types are shown below:

* string
* bool
* integer ("int" would NOT work!)
* float
* time
* array

For the `time` and `array` types, there is an optional third field after the type name. For the "time" type, you can specify a time format like you would in `time_format`.

For the "array" type, the third field specifies the delimiter (the default is ","). For example, if a field called "item\_ids" contains the value "3,4,5", `types item_ids:array` parses it as \["3", "4", "5"]. Alternatively, if the value is "Adam|Alice|Bob", `types item_ids:array:|` parses it as \["Adam", "Alice", "Bob"].

## Example

```
time:2013/02/28 12:00:00\thost:192.168.0.1\treq_id:111\tuser:-
```

This incoming event is parsed as:

```
time:
1362020400 (2013/02/28/ 12:00:00)

record:
{
  "host"   : "192.168.0.1",
  "req_id" : "111",
  "user"   : "-"
}
```

If you set `null_value_pattern '-'` in the configuration, `user` field becomes `nil` instead of `"-"`.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# csv

The `csv` parser plugin parses CSV format.

This plugin uses [CSV.parse\_line](http://ruby-doc.org/stdlib-2.4.1/libdoc/csv/rdoc/CSV.html#method-c-parse_line) method.

## Parameters

### time\_key

Specify time field for event time. Default is `nil`.

If there is no time field in the record, this parser uses current time as an event time.

### time\_format

If time field value is formatted string, e.g. "28/Feb/2013:12:00:00 +0900", you need to specify this parameter to parse it.

Default is `nil` and it uses `Time.parse` method to parse the field.

See [Time#strptime](http://ruby-doc.org/stdlib-2.4.1/libdoc/time/rdoc/Time.html#method-c-strptime) for additional format information.

### null\_value\_pattern

Specify null value pattern. Default is `nil`.

If given field value is matched with this pattern, the field value is replaced with `nil`.

### null\_empty\_string

If `true`, empty string field is replaced with `nil`. Default is `false`.

### types

Although every parsed field has type `string` by default, you can specify other types. This is useful when filtering particular fields numerically or storing data with sensible type information.

The syntax is

```
types <field_name_1>:<type_name_1>,<field_name_2>:<type_name_2>,...
```

e.g.,

```
types user_id:integer,paid:bool,paid_usd_amount:float
```

As demonstrated above, "," is used to delimit field-type pairs while ":" is used to separate a field name with its intended type.

Unspecified fields are parsed at the default string type.

The list of supported types are shown below:

* string
* bool
* integer ("int" would NOT work!)
* float
* time
* array

For the `time` and `array` types, there is an optional third field after the type name. For the "time" type, you can specify a time format like you would in `time_format`.

For the "array" type, the third field specifies the delimiter (the default is ","). For example, if a field called "item\_ids" contains the value "3,4,5", `types item_ids:array` parses it as \["3", "4", "5"]. Alternatively, if the value is "Adam|Alice|Bob", `types item_ids:array:|` parses it as \["Adam", "Alice", "Bob"].

## Example

```
format csv
keys time,host,req_id,user
time_key time
```

With this configuration:

```
2013/02/28 12:00:00,192.168.0.1,111,-
```

This incoming event is parsed as:

```
time:
1362020400 (2013/02/28/ 12:00:00)

record:
{
  "host"   : "192.168.0.1",
  "req_id" : "111",
  "user"   : "-"
}
```

If you set `null_value_pattern '-'` in the configuration, `user` field becomes `nil` instead of `"-"`.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# tsv

The `tsv` parser plugin parses TSV format.

## Parameters

### time\_key

Specify time field for event time. Default is `nil`.

If there is no time field in the record, this parser uses current time as an event time.

### time\_format

If time field value is formatted string, e.g. "28/Feb/2013:12:00:00 +0900", you need to specify this parameter to parse it.

Default is `nil` and it uses `Time.parse` method to parse the field.

See [Time#strptime](http://ruby-doc.org/stdlib-2.4.1/libdoc/time/rdoc/Time.html#method-c-strptime) for additional format information.

### null\_value\_pattern

Specify null value pattern. Default is `nil`.

If given field value is matched with this pattern, the field value is replaced with `nil`.

### null\_empty\_string

If `true`, empty string field is replaced with `nil`. Default is `false`.

### types

Although every parsed field has type `string` by default, you can specify other types. This is useful when filtering particular fields numerically or storing data with sensible type information.

The syntax is

```
types <field_name_1>:<type_name_1>,<field_name_2>:<type_name_2>,...
```

e.g.,

```
types user_id:integer,paid:bool,paid_usd_amount:float
```

As demonstrated above, "," is used to delimit field-type pairs while ":" is used to separate a field name with its intended type.

Unspecified fields are parsed at the default string type.

The list of supported types are shown below:

* string
* bool
* integer ("int" would NOT work!)
* float
* time
* array

For the `time` and `array` types, there is an optional third field after the type name. For the "time" type, you can specify a time format like you would in `time_format`.

For the "array" type, the third field specifies the delimiter (the default is ","). For example, if a field called "item\_ids" contains the value "3,4,5", `types item_ids:array` parses it as \["3", "4", "5"]. Alternatively, if the value is "Adam|Alice|Bob", `types item_ids:array:|` parses it as \["Adam", "Alice", "Bob"].

## Example

```
format tsv
keys time,host,req_id,user
time_key time
```

With this configuration:

```
2013/02/28 12:00:00\t192.168.0.1\t111\t-
```

This incoming event is parsed as:

```
time:
1362020400 (2013/02/28/ 12:00:00)

record:
{
  "host"   : "192.168.0.1",
  "req_id" : "111",
  "user"   : "-"
}
```

If you set `null_value_pattern '-'` in the configuration, `user` field becomes `nil` instead of `"-"`.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# json

The `json` parser plugin parses JSON logs. One JSON map per line.

## Parameters

### time\_key

Specify time field for event time. Default is `time`.

If there is no time field in the record, this parser uses current time as an event time.

### time\_format

If time field value is formatted string, e.g. "28/Feb/2013:12:00:00 +0900", you need to specify this parameter to parse it.

Default is `nil` and it means time field value is a second integer like `1497915137`.

See [Time#strptime](http://ruby-doc.org/stdlib-2.4.1/libdoc/time/rdoc/Time.html#method-c-strptime) for additional format information.

### keep\_time\_key

If you want to keep time field in the record, set `true`. Default is `false`.

## Example

```
{"time":1362020400,"host":"192.168.0.1","size":777,"method":"PUT"}
```

This incoming event is parsed as:

```
time:
1362020400 (2013-02-28 12:00:00 +0900)

record:
{
  "host"  : "192.168.0.1",
  "size"  : 777,
  "method": "PUT",
}
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# multiline

The `multiline` parser plugin parses multiline logs. This plugin is multiline version of `regexp` parser.

The `multiline` parser parses log with `formatN` and `format_firstline` parameters. `format_firstline` is for detecting start line of multiline log. `formatN`, N's range is 1..20, is the list of Regexp format for multiline log. Unlike other parser plugins, this plugin needs special code in input plugin, e.g. handle format\_firstline. So currently, in\_tail plugin works with \`multiline\` but other input plugins don't work with \`multiline\`.

## Parameters

### time\_key

Specify the field for event time. Default is `time`.

### time\_format

Specify time format for `time_key`.

See [Time#strptime](http://ruby-doc.org/stdlib-2.4.1/libdoc/time/rdoc/Time.html#method-c-strptime) for additional format information.

### format\_firstline

Specify regexp pattern for start line of multiple lines. Input plugin can skip the logs until `format_firstline` is matched. Default is `nil`.

If `format_firstline` is not specified, input plugin should store unmatched new lines in temporary buffer and try to match buffered logs with each new line.

### formatN

Specify regexp patterns. For readability, you can separate regexp patterns into multiple regexpN parameters, See "Rails log" example. These patterns are joined and constructs regexp pattern with multiline mode.

### keep\_time\_key

If you want to keep time field in the record, set `true`. Default is `false`.

## Example

### Rails log

```
format multiline
format_firstline /^Started/
format1 /Started (?<method>[^ ]+) "(?<path>[^"]+)" for (?<host>[^ ]+) at (?<time>[^ ]+ [^ ]+ [^ ]+)\n/
format2 /Processing by (?<controller>[^\u0023]+)\u0023(?<controller_method>[^ ]+) as (?<format>[^ ]+?)\n/
format3 /(  Parameters: (?<parameters>[^ ]+)\n)?/
format4 /  Rendered (?<template>[^ ]+) within (?<layout>.+) \([\d\.]+ms\)\n/
format5 /Completed (?<code>[^ ]+) [^ ]+ in (?<runtime>[\d\.]+)ms \(Views: (?<view_runtime>[\d\.]+)ms \| ActiveRecord: (?<ar_runtime>[\d\.]+)ms\)/
```

With this configuration:

```
Started GET "/users/123/" for 127.0.0.1 at 2013-06-14 12:00:11 +0900
Processing by UsersController#show as HTML
  Parameters: {"user_id"=>"123"}
  Rendered users/show.html.erb within layouts/application (0.3ms)
Completed 200 OK in 4ms (Views: 3.2ms | ActiveRecord: 0.0ms)
```

This incoming event is parsed as:

```
time:
1371178811 (2013-06-14 12:00:11 +0900)

record:
{
  "method"           :"GET",
  "path"             :"/users/123/",
  "host"             :"127.0.0.1",
  "controller"       :"UsersController",
  "controller_method":"show",
  "format"           :"HTML",
  "parameters"       :"{ \"user_id\":\"123\"}",
  ...
}
```

### Java stacktrace log

```
format multiline
format_firstline /\d{4}-\d{1,2}-\d{1,2}/
format1 /^(?<time>\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}) \[(?<thread>.*)\] (?<level>[^\s]+)(?<message>.*)/
```

With this configuration:

```
2013-3-03 14:27:33 [main] INFO  Main - Start
2013-3-03 14:27:33 [main] ERROR Main - Exception
javax.management.RuntimeErrorException: null
    at Main.main(Main.java:16) ~[bin/:na]
2013-3-03 14:27:33 [main] INFO  Main - End
```

These incoming events are parsed as:

```
time:
2013-03-03 14:27:33 +0900
record:
{
  "thread" :"main",
  "level"  :"INFO",
  "message":"  Main - Start"
}

time:
2013-03-03 14:27:33 +0900
record:
{
  "thread" :"main",
  "level"  :"ERROR",
  "message":" Main - Exception\njavax.management.RuntimeErrorException: null\n    at Main.main(Main.java:16) ~[bin/:na]"
}

time:
2013-03-03 14:27:33 +0900
record:
{
  "thread" :"main",
  "level"  :"INFO",
  "message":"  Main - End"
}
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# none

The `none` parser plugin parses the line as-is with single field. This format is to defer parsing/structuring the data.

## Parameters

### message\_key

Specify field name to contain logs. Default is `message`.

## Example

```
Hello world. I am a line of log!
```

This incoming event is parsed as:

```
time:
1362020400 (current time)

record:
{"message":"Hello world. I am a line of log!"}
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Formatter Plugins

Fluentd has 6 types of plugins: [Input](https://docs.fluentd.org/input), [Parser](https://docs.fluentd.org/parser), [Filter](https://docs.fluentd.org/filter), [Output](https://docs.fluentd.org/output), [Formatter](https://docs.fluentd.org/formatter) and [Buffer](https://docs.fluentd.org/buffer). This article gives an overview of Formatter Plugin.

## Overview

Sometimes, the output format for an output plugin does not meet one's needs. Fluentd has a pluggable system called Text Formatter that lets the user extend and re-use custom output formats.

## How To Use

For an output plugin that supports Text Formatter, the `format` parameter can be used to change the output format.

For example, by default, [out\_file](https://docs.fluentd.org/output/file) plugin outputs data as

```
2014-08-25 00:00:00 +0000<TAB>foo.bar<TAB>{"k1":"v1", "k2":"v2"}
```

However, if you set `format json` like this

```
<match foo.bar>
  @type file
  path /path/to/file
  format json
</match>
```

The output changes to

```
{"time": "2014-08-25 00:00:00 +0000", "tag":"foo.bar", "k1:"v1", "k2":"v2"}
```

i.e., each line is a single JSON object with "time" and "tag fields to retain the event's timestamp and tag.

See [this section](https://docs.fluentd.org/developer/plugin-development#text-formatter-plugins) to learn how to develop a custom formatter.

## List of Built-in Formatters

* [out\_file](https://docs.fluentd.org/formatter/out_file)
* [json](https://docs.fluentd.org/formatter/json)
* [ltsv](https://docs.fluentd.org/formatter/ltsv)
* [csv](https://docs.fluentd.org/formatter/csv)
* [msgpack](https://docs.fluentd.org/formatter/msgpack)
* [hash](https://docs.fluentd.org/formatter/hash)
* [single\_value](https://docs.fluentd.org/formatter/single_value)

## List of Output Plugins with Text Formatter Support

* [out\_file](https://docs.fluentd.org/output/file)
* [out\_s3](https://docs.fluentd.org/output/s3)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# out\_file

The `out_file` formatter plugin outputs time, tag and json record separated by a delimiter.

```
time[delimiter]tag[delimiter]record\n
```

This format is a default format of `out_file` plugin.

## Parameters

### delimiter (String, Optional, default to "\t"(TAB))

Delimiter for each field. "SPACE"(' ') and "COMMA"(',') are supported.

### output\_tag (Boolean, Optional, defaults to true)

Output tag field if true,

### output\_time (Boolean, Optional, defaults to true)

Output time field if true,

### include\_time\_key (Boolean, Optional, defaults to false)

If true, the time field (as specified by the `time_key` parameter) is kept in the record.

### time\_key (String, Optional, defaults to "time")

The field name for the time key.

### time\_format (String. Optional)

By default, the output format is iso8601 (e.g. "2008-02-01T21:41:49"). One can specify their own format with this parameter.

### include\_tag\_key (Boolean. Optional, defaults to false)

If true, the tag field (as specified by the `tag_key` parameter) is kept in the record.

### tag\_key (String, Optional, defaults to "tag")

The field name for the tag key.

### localtime (Boolean. Optional, defaults to true)

If true, use local time. Otherwise, UTC is used. This parameter is overwritten by the `utc` parameter.

### timezone (String. Optional)

By setting this parameter, one can parse the time value in the specified timezone. The following formats are accepted:

1. \[+-]HH:MM (e.g. "+09:00")
2. \[+-]HHMM (e.g. "+0900")
3. \[+-]HH (e.g. "+09")
4. Region/Zone (e.g. "Asia/Tokyo")
5. Region/Zone/Zone (e.g. "America/Argentina/Buenos\_Aires")

The timezone set in this parameter takes precedence over `localtime`\*\*, e.g., if `localtime` is set to `true` but `timezone` is set to `+0000`, UTC would be used.

## Example

```
tag:    app.event
time:   1362020400t
record: {"host":"192.168.0.1","size":777,"method":"PUT"}
```

This incoming event is formatted to:

```
2013-02-28T12:00:00+09:00\tapp.event\t{"host":"192.168.0.1","size":777,"method":"PUT"}
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# json

The `json` formatter plugin converts an event to json.

By default, `json` formatter result doesn't contain `tag` and `time` field.

## Parameters

### add\_newline (Boolean, Optional, defaults to true)

Add `\n` to the result.

### include\_time\_key (Boolean, Optional, defaults to false)

If true, the time field (as specified by the `time_key` parameter) is kept in the record.

### time\_key (String, Optional, defaults to "time")

The field name for the time key.

### time\_format (String. Optional)

By default, the output format is iso8601 (e.g. "2008-02-01T21:41:49"). One can specify their own format with this parameter.

### include\_tag\_key (Boolean. Optional, defaults to false)

If true, the tag field (as specified by the `tag_key` parameter) is kept in the record.

### tag\_key (String, Optional, defaults to "tag")

The field name for the tag key.

### localtime (Boolean. Optional, defaults to true)

If true, use local time. Otherwise, UTC is used. This parameter is overwritten by the `utc` parameter.

### timezone (String. Optional)

By setting this parameter, one can parse the time value in the specified timezone. The following formats are accepted:

1. \[+-]HH:MM (e.g. "+09:00")
2. \[+-]HHMM (e.g. "+0900")
3. \[+-]HH (e.g. "+09")
4. Region/Zone (e.g. "Asia/Tokyo")
5. Region/Zone/Zone (e.g. "America/Argentina/Buenos\_Aires")

The timezone set in this parameter takes precedence over `localtime`\*\*, e.g., if `localtime` is set to `true` but `timezone` is set to `+0000`, UTC would be used.

### time\_as\_epoch (Boolean, Optional, defaults to false)

Set integer event time instead of stringanized time to `time_key`.

## Example

```
tag:    app.event
time:   1362020400
record: {"host":"192.168.0.1","size":777,"method":"PUT"}
```

This incoming event is formatted to:

```
{"host":"192.168.0.1","size":777,"method":"PUT"}
```

With `include_tag_key true` and `tag_key event_tag`, result is:

```
{"host":"192.168.0.1","size":777,"method":"PUT","event_tag":"app.event"}
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# ltsv

The `ltsv` formatter plugin output an event as [LTSV](http://ltsv.org).

```
field1[label_delimiter]value1[delimiter]field2[label_delimiter]value2\n
```

## Parameters

### delimiter (String, Optional. defaults to "\t"(TAB))

Delimiter for fields.

### label\_delimiter (String, Optional. defaults to ":")

Delimiter for key value field.

### add\_newline (Boolean, Optional, defaults to true)

Add `\n` to the result.

### include\_time\_key (Boolean, Optional, defaults to false)

If true, the time field (as specified by the `time_key` parameter) is kept in the record.

### time\_key (String, Optional, defaults to "time")

The field name for the time key.

### time\_format (String. Optional)

By default, the output format is iso8601 (e.g. "2008-02-01T21:41:49"). One can specify their own format with this parameter.

### include\_tag\_key (Boolean. Optional, defaults to false)

If true, the tag field (as specified by the `tag_key` parameter) is kept in the record.

### tag\_key (String, Optional, defaults to "tag")

The field name for the tag key.

### localtime (Boolean. Optional, defaults to true)

If true, use local time. Otherwise, UTC is used. This parameter is overwritten by the `utc` parameter.

### timezone (String. Optional)

By setting this parameter, one can parse the time value in the specified timezone. The following formats are accepted:

1. \[+-]HH:MM (e.g. "+09:00")
2. \[+-]HHMM (e.g. "+0900")
3. \[+-]HH (e.g. "+09")
4. Region/Zone (e.g. "Asia/Tokyo")
5. Region/Zone/Zone (e.g. "America/Argentina/Buenos\_Aires")

The timezone set in this parameter takes precedence over `localtime`\*\*, e.g., if `localtime` is set to `true` but `timezone` is set to `+0000`, UTC would be used.

## Example

```
tag:    app.event
time:   1362020400
record: {"host":"192.168.0.1","size":777,"method":"PUT"}
```

This incoming event is formatted to:

```
host:192.168.0.1\tsize:777\tmethod:PUT\n
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# csv

The `csv` formatter plugin output an event as CSV.

```
"value1"[delimiter]"value2"[delimiter]"value3"\n
```

## Parameters

### fields (Array of String, Required. defaults to "\t"(TAB))

Specify output fields

### delimiter (String, Optional. defaults to ",")

Delimiter for values.

### force\_quotes (Boolean, Optional, defaults to true)

If false, value won't be framed by quotes.

### add\_newline (Boolean, Optional, defaults to true)

Add `\n` to the result.

### include\_time\_key (Boolean, Optional, defaults to false)

If true, the time field (as specified by the `time_key` parameter) is kept in the record.

### time\_key (String, Optional, defaults to "time")

The field name for the time key.

### time\_format (String. Optional)

By default, the output format is iso8601 (e.g. "2008-02-01T21:41:49"). One can specify their own format with this parameter.

### include\_tag\_key (Boolean. Optional, defaults to false)

If true, the tag field (as specified by the `tag_key` parameter) is kept in the record.

### tag\_key (String, Optional, defaults to "tag")

The field name for the tag key.

### localtime (Boolean. Optional, defaults to true)

If true, use local time. Otherwise, UTC is used. This parameter is overwritten by the `utc` parameter.

### timezone (String. Optional)

By setting this parameter, one can parse the time value in the specified timezone. The following formats are accepted:

1. \[+-]HH:MM (e.g. "+09:00")
2. \[+-]HHMM (e.g. "+0900")
3. \[+-]HH (e.g. "+09")
4. Region/Zone (e.g. "Asia/Tokyo")
5. Region/Zone/Zone (e.g. "America/Argentina/Buenos\_Aires")

The timezone set in this parameter takes precedence over `localtime`\*\*, e.g., if `localtime` is set to `true` but `timezone` is set to `+0000`, UTC would be used.

## Example

```
format csv
fields host,method
```

With this configuration:

```
tag:    app.event
time:   1362020400
record: {"host":"192.168.0.1","size":777,"method":"PUT"}
```

This incoming event is formatted to:

```
"192.168.0.1","PUT"\n
```

With `force_quotes false`, the result is:

```
192.168.0.1,PUT\n
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# msgpack

The `msgpack` formatter plugin converts an event to msgpack binary.

## Parameters

### include\_time\_key (Boolean, Optional, defaults to false)

If true, the time field (as specified by the `time_key` parameter) is kept in the record.

### time\_key (String, Optional, defaults to "time")

The field name for the time key.

### time\_format (String. Optional)

By default, the output format is iso8601 (e.g. "2008-02-01T21:41:49"). One can specify their own format with this parameter.

### include\_tag\_key (Boolean. Optional, defaults to false)

If true, the tag field (as specified by the `tag_key` parameter) is kept in the record.

### tag\_key (String, Optional, defaults to "tag")

The field name for the tag key.

### localtime (Boolean. Optional, defaults to true)

If true, use local time. Otherwise, UTC is used. This parameter is overwritten by the `utc` parameter.

### timezone (String. Optional)

By setting this parameter, one can parse the time value in the specified timezone. The following formats are accepted:

1. \[+-]HH:MM (e.g. "+09:00")
2. \[+-]HHMM (e.g. "+0900")
3. \[+-]HH (e.g. "+09")
4. Region/Zone (e.g. "Asia/Tokyo")
5. Region/Zone/Zone (e.g. "America/Argentina/Buenos\_Aires")

The timezone set in this parameter takes precedence over `localtime`\*\*, e.g., if `localtime` is set to `true` but `timezone` is set to `+0000`, UTC would be used.

### time\_as\_epoch (Boolean, Optional, defaults to false)

Set integer event time instead of stringanized time to `time_key`.

## Example

```
tag:    app.event
time:   1362020400
record: {"host":"192.168.0.1","size":777,"method":"PUT"}
```

This incoming event is formatted to:

```
{"host":"192.168.0.1","size":777,"method":"PUT"}
```

With `include_tag_key true` and `tag_key event_tag`, result is:

```
\x83\xA4host\xAB192.168.0.1\xA4size\xCD\x03\t\xA6method\xA3PUT
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# hash

The `hash` formatter plugin converts an event to ruby hash.

By default, `hash` formatter result doesn't contain `tag` and `time` field.

## Parameters

### add\_newline (Boolean, Optional, defaults to true)

Add `\n` to the result.

### include\_time\_key (Boolean, Optional, defaults to false)

If true, the time field (as specified by the `time_key` parameter) is kept in the record.

### time\_key (String, Optional, defaults to "time")

The field name for the time key.

### time\_format (String. Optional)

By default, the output format is iso8601 (e.g. "2008-02-01T21:41:49"). One can specify their own format with this parameter.

### include\_tag\_key (Boolean. Optional, defaults to false)

If true, the tag field (as specified by the `tag_key` parameter) is kept in the record.

### tag\_key (String, Optional, defaults to "tag")

The field name for the tag key.

### localtime (Boolean. Optional, defaults to true)

If true, use local time. Otherwise, UTC is used. This parameter is overwritten by the `utc` parameter.

### timezone (String. Optional)

By setting this parameter, one can parse the time value in the specified timezone. The following formats are accepted:

1. \[+-]HH:MM (e.g. "+09:00")
2. \[+-]HHMM (e.g. "+0900")
3. \[+-]HH (e.g. "+09")
4. Region/Zone (e.g. "Asia/Tokyo")
5. Region/Zone/Zone (e.g. "America/Argentina/Buenos\_Aires")

The timezone set in this parameter takes precedence over `localtime`\*\*, e.g., if `localtime` is set to `true` but `timezone` is set to `+0000`, UTC would be used.

### time\_as\_epoch (Boolean, Optional, defaults to false)

Set integer event time instead of stringanized time to `time_key`.

## Example

```
tag:    app.event
time:   1362020400
record: {"host":"192.168.0.1","size":777,"method":"PUT"}
```

This incoming event is formatted to:

```
{"host"=>"192.168.0.1","size"=>777,"method"=>"PUT"}
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# single\_value

The `single_value` formatter plugin output the value of a single field instead of the whole record.

This formatter is often used in conjunction with [in\_tail](https://docs.fluentd.org/input/tail)'s `format none`.

## Parameters

### add\_newline (Boolean, Optional, defaults to true)

Add `\n` to the result. If there is a trailing "\n" already, set it "false"

### message\_key (String, Optional, defaults to "message")

The value of this field is outputted.

## Example

```
tag:    app.event
time:   1362020400
record: {"message":"Hello from Fluentd!"}
```

This incoming event is formatted to:

```
Hello from Fluentd!\n
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.


# Developer




---

[Next Page](/llms-full.txt/1)

