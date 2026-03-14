# Source: https://docs.fluentd.org/0.12/articles/install-by-chef.md

# Install By Chef

This article explains how to install Fluentd using Chef.

## Step0: Before Installation

Please follow the [Preinstallation Guide](https://docs.fluentd.org/0.12/articles/before-install) to configure your OS properly. This will prevent many unnecessary problems.

## Step1: Import Recipe

The chef recipe to install td-agent can be found [here](https://github.com/treasure-data/chef-td-agent). Please import the recipe, add it to run\_list, and upload it to the Chef Server.

## Step2: Run chef-client

Please run chef-client to install td-agent across your machines.

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
