# Source: https://docs.fluentd.org/installation/install-from-source.md

# Source: https://docs.fluentd.org/0.12/articles/install-from-source.md

# Install From Source

This article explains how to install Fluentd from source code (git repository). This is useful for developers.

## Step-1: Install Ruby interpreter

Please install Ruby >= 1.9.3 and bundler on your local environment.

## Step-2: Fetch Source Code

Fetch the source code from github. The official repository is located [here](http://github.com/fluent/fluentd/).

```
$ git clone https://github.com/fluent/fluentd.git
$ cd fluentd
$ git checkout -b v0.12 origin/v0.12
```

master branch is now for v1.x development so you need to checkout v0.12 branch.

## Step-3: Build and Install

Build the package with `rake` and install it with `gem`.

```
$ bundle install
Fetching gem metadata from https://rubygems.org/.........
...
Your bundle is complete!
Use `bundle show [gemname]` to see where a bundled gem is installed.
$ bundle exec rake build
fluentd xxx built to pkg/fluentd-xxx.gem.
$ gem install pkg/fluentd-xxx.gem
```

## Step-4: Run

Run the following commands to to confirm that Fluentd was installed successfully:

```
$ fluentd --setup ./fluent
$ fluentd -c ./fluent/fluent.conf -vv &
$ echo '{"json":"message"}' | fluent-cat debug.test
```

The last command sends Fluentd a message '{"json":"message"}' with a "debug.test" tag. If the installation was successful, Fluentd will output the following message:

```
2011-07-10 16:49:50 +0900 debug.test: {"json":"message"}
```

It's HIGHLY recommended that you set up **ntpd** on the node to prevent invalid timestamps in your logs.

For large deployments, you must use [jemalloc](http://www.canonware.com/jemalloc/) to avoid memory fragmentation. This is already included in the [rpm](https://docs.fluentd.org/0.12/articles/install-by-rpm) and [deb](https://docs.fluentd.org/0.12/articles/install-by-deb) packages.

## Next Steps

You're now ready to collect your real logs using Fluentd. Please see the following tutorials to learn how to collect your data from various data sources.

* Basic Configuration
  * [Config File](https://docs.fluentd.org/0.12/configuration/config-file)
* Application Logs
  * [Ruby](https://docs.fluentd.org/0.12/articles/ruby), [Java](https://docs.fluentd.org/0.12/articles/java), [Python](https://docs.fluentd.org/0.12/articles/python), [PHP](https://docs.fluentd.org/0.12/articles/php),

    [Perl](https://docs.fluentd.org/0.12/articles/perl), [Node.js](https://docs.fluentd.org/0.12/articles/nodejs), [Scala](https://docs.fluentd.org/0.12/articles/scala)
* Examples
  * [Store Apache Log into Amazon S3](https://docs.fluentd.org/0.12/articles/apache-to-s3)
  * [Store Apache Log into MongoDB](https://docs.fluentd.org/0.12/articles/apache-to-mongodb)
  * [Data Collection into HDFS](https://docs.fluentd.org/0.12/articles/http-to-hdfs)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
