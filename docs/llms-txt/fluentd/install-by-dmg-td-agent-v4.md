# Source: https://docs.fluentd.org/installation/obsolete-installation/treasure-agent-v4-eol-installation/install-by-dmg-td-agent-v4.md

# Install by .dmg Package v4 (macOS)

This article explains how to install `td-agent`, the stable Fluentd distribution package maintained by [Treasure Data, Inc](https://www.treasuredata.com/), on macOS.

## What is `td-agent`?

Fluentd is written in Ruby for flexibility, with performance-sensitive parts in C. However, some users may have difficulty installing and operating a Ruby daemon.

That is why [Treasure Data, Inc](http://www.treasuredata.com/) provides **the stable distribution of Fluentd**, called `td-agent`. The differences between Fluentd and `td-agent` can be found [here](https://www.fluentd.org/faqs).

For macOS, `td-agent` is distributed as `.dmg` installer.

## Step 1: Install `td-agent`

{% hint style="danger" %}
This article contains deprecated td-agent (EOL) information: SHOULD NOT use td-agent anymore.

* `fluent-package` (successor of `td-agent`) for macOS is not be shipped yet, we plan to migrate to homebrew ecosystem in the future.
* Package archive was migrated from [packages.treasuredata.com](https://packages.treasuredata.com) to [fluentd.cdn.cncf.io](https://fluentd.cdn.cncf.io/index.html).
  {% endhint %}

Download and install the `.dmg` package:

* [td-agent v4](https://td-agent-package-browser.herokuapp.com/4/macosx)

NOTE: If your OS is not supported, consider [gem installation](https://docs.fluentd.org/installation/install-by-gem) instead.

## Step 2: Launch `td-agent`

Use `launchctl` command to launch `td-agent`. Make sure that the daemon is started correctly. Checks logs (`/var/log/td-agent/td-agent.log`).

```
$ sudo launchctl load /Library/LaunchDaemons/td-agent.plist
$ less /var/log/td-agent/td-agent.log
2018-01-01 16:55:03 -0700 [info]: starting fluentd-1.0.2
2018-01-01 16:55:03 -0700 [info]: reading config file path="/etc/td-agent/td-agent.conf"
```

The configuration file is located at `/etc/td-agent/td-agent.conf` and the plugin directory is at `/etc/td-agent/plugin`.

To stop the agent, run this command:

```
$ sudo launchctl unload /Library/LaunchDaemons/td-agent.plist
```

## Step 3: Post Sample Logs via HTTP

The default configuration (`/etc/td-agent/td-agent.conf`) is to receive logs at an HTTP endpoint and route them to `stdout`. For `td-agent` logs, see `/var/log/td-agent/td-agent.log`.

You can post sample log records with `curl` command:

```
$ curl -X POST -d 'json={"json":"message"}' http://localhost:8888/debug.test
$ tail -n 1 /var/log/td-agent/td-agent.log
2018-01-01 17:51:47 -0700 debug.test: {"json":"message"}
```

## Uninstall td-agent

On macOS, `td-agent` does not provide any uninstallation app like `rpm` / `deb` on Ubuntu.

To uninstall `td-agent` from macOS, remove these files / directories:

* `/Library/LaunchDaemons/td-agent.plist`
* `/etc/td-agent`
* `/opt/td-agent`
* `/var/log/td-agent`

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

For further steps, follow these:

* [ChangeLog of `td-agent`](https://docs.treasuredata.com/display/public/PD/The+td-agent+Change+Log)
* [Chef Cookbook](https://github.com/treasure-data/chef-td-agent/)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is an open-source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
