# Source: https://docs.fluentd.org/installation/install-fluent-package/install-by-dmg-fluent-package.md

# .dmg Package (macOS)

This article explains how to install stable versions of `fluent-package` dmg packages, the stable Fluentd distribution packages maintained by [Fluentd Project](https://www.fluentd.org/) on macOS.

## What is `fluent-package`?

Please see [fluent-package-v5-vs-td-agent](https://docs.fluentd.org/quickstart/fluent-package-v5-vs-td-agent).

## How to install `fluent-package`

{% hint style="info" %}
NOTE:

* `fluent-package` is not be shipped yet, we plan to migrate to homebrew ecosystem in the future.
  {% endhint %}

{% hint style="danger" %}
The following are deprecated td-agent (EOL) information:

* About Treasure Agent (td-agent) v4, see [Install by .dmg Package (macOS)](https://docs.fluentd.org/installation/obsolete-installation/treasure-agent-v4-eol-installation/install-by-dmg-td-agent-v4).
* About deprecated [Treasure Agent (td-agent) 3 will not be maintained anymore](https://www.fluentd.org/blog/schedule-for-td-agent-3-eol), see [Install by DEB Package v3](https://docs.fluentd.org/installation/obsolete-installation/treasure-agent-v3-eol-installation/install-by-deb-td-agent-v3).
  {% endhint %}

## Next Steps

You are now ready to collect real logs with Fluentd. Refer to the following tutorials on how to collect data from various sources:

* Basic Configuration
  * [Config File](https://docs.fluentd.org/configuration/config-file)
* Application Logs
  * [Ruby](https://docs.fluentd.org/language-bindings/ruby), [Java](https://docs.fluentd.org/language-bindings/java), [Python](https://docs.fluentd.org/language-bindings/python), [PHP](https://docs.fluentd.org/language-bindings/php),

    [Perl](https://docs.fluentd.org/language-bindings/perl), [Node.js](https://docs.fluentd.org/language-bindings/nodejs), [Scala](https://docs.fluentd.org/language-bindings/scala)
* Examples
  * [Store Apache Log into Amazon S3](https://docs.fluentd.org/how-to-guides/apache-to-s3)
  * [Store Apache Log into MongoDB](https://docs.fluentd.org/how-to-guides/apache-to-mongodb)
  * [Data Collection into HDFS](https://docs.fluentd.org/how-to-guides/http-to-hdfs)

{% hint style="info" %}
There are some commercial supports for Fluentd, see [Enterprise Services](https://www.fluentd.org/enterprise_services). If you use Fluentd on production, Let's share your use-case/testimonial on [Testimonials](https://www.fluentd.org/testimonials) page. Please consider to feedback via [GitHub](https://github.com/fluent/fluentd-website/issues/new?template=testimonials.yml).
{% endhint %}

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is an open-source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
