# Source: https://docs.datadoghq.com/developers/custom_checks/write_agent_check.md

---
title: Writing a Custom Agent Check
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Developers > Custom Checks > Writing a Custom Agent Check
---

# Writing a Custom Agent Check

## Overview{% #overview %}

This page takes you through the process of building a basic "Hello world!" custom Agent check. It also shows you how to change the minimum collection interval for the check.

## Setup{% #setup %}

### Installation{% #installation %}

Before you create a custom Agent check, install the [Datadog Agent](http://app.datadoghq.com/account/settings/agent/latest).

{% alert level="danger" %}
To work with the latest version of the Agent, your custom Agent check must be Python 3 compatible.
{% /alert %}

### Configuration{% #configuration %}

1. Change to the `conf.d` directory on your system. For more information about where to find the `conf.d` directory, see [Agent configuration files](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/#check-configuration-files).

1. In the `conf.d` directory, create a new config file for your new Agent check. Name the file `custom_checkvalue.yaml`.

1. Edit the file to include the following:

In the `conf.d/custom_checkvalue.yaml` file:

   ```yaml
   init_config:
   instances:
     [{}]
```



1. Create a check file in the `checks.d` directory. Name the file `custom_checkvalue.py`.
Important alert (level: info): **Naming your checks:**
   - It's a good idea to prefix your check with `custom_` to avoid conflicts with the name of a pre-existing Datadog Agent integration. For example, if you have a custom Postfix check, name your check files `custom_postfix.py` and `custom_postfix.yaml` instead of `postfix.py` and `postfix.yaml`.
   - The names of the configuration and check files must match. If your check is called `custom_checkvalue.py`, your configuration file must be named `custom_checkvalue.yaml`.

1. Edit the file to include the following:

In the `checks.d/custom_checkvalue.py` file:

   ```python
   from checks import AgentCheck
   class HelloCheck(AgentCheck):
     def check(self, instance):
       self.gauge('hello.world', 1)
```



1. [Restart the Agent](https://docs.datadoghq.com/agent/configuration/agent-commands/?tab=agentv6v7#restart-the-agent) and wait for a new metric named `hello.world` to show up in the [Metric Summary](https://app.datadoghq.com/metric/summary).

If you're having issues getting your custom check working, check the file permissions. The check file must be readable and executable by the Agent user. For more troubleshooting steps, see [Troubleshoot an Agent Check](https://docs.datadoghq.com/agent/troubleshooting/agent_check_status/).

### Updating the collection interval{% #updating-the-collection-interval %}

To change the collection interval of your check, use the `min_collection_interval` setting in your `custom_checkvalue.yaml` file and specify a setting in seconds. The default value is 15 seconds. You must add the `min_collection_interval` at an instance level. If your custom check is set up to monitor multiple instances, you must configure the interval individually per instance.

Setting the `min_collection_interval` to `30` does not guarantee that the metric is collected every 30 seconds. The Agent collector tries to run the check every 30 seconds, but the check might end up queued behind other integrations and checks, depending on how many integrations and checks are enabled on the same Agent. If a `check` method takes more than 30 seconds to complete, the Agent notices that the check is still running and skips its execution until the next interval.

#### Set a collection interval{% #set-a-collection-interval %}

For a single instance, use this configuration to set the collection interval to 30 seconds:

In the `conf.d/custom_checkvalue.yaml` file:

```yaml
init_config:

instances:
  - min_collection_interval: 30
```

The example below demonstrates changing the interval for a hypothetical custom check that monitors a service named `my_service` on two separate servers:

```yaml
init_config:

instances:
  - host: "http://localhost/"
    service: my_service
    min_collection_interval: 30

  - host: "http://my_server/"
    service: my_service
    min_collection_interval: 30
```

### Verifying your check{% #verifying-your-check %}

To verify your check is running, use the following command:

```shell
sudo -u dd-agent -- datadog-agent check <CHECK_NAME>
```

After you verify that your check is running, [restart the Agent](https://docs.datadoghq.com/agent/configuration/agent-commands/?tab=agentv6v7#restart-the-agent) to include the check and start reporting data.

## Writing checks that run command-line programs{% #writing-checks-that-run-command-line-programs %}

It's possible to create a custom check that runs a command-line program and captures its output as a custom metric. For example, a check can run the `vgs` command to report information about volume groups.

Because the Python interpreter that runs the checks is embedded in the multi-threaded Go runtime, using the `subprocess` or `multithreading` modules from the Python standard library is not supported. To run a subprocess within a check, use the [`get_subprocess_output()` function](https://github.com/DataDog/integrations-core/blob/9414403b361e583e8f1ebcdee2f006c384c61045/datadog_checks_base/datadog_checks/base/utils/subprocess_output.py#L22) from the module `datadog_checks.base.utils.subprocess_output`. The command and its arguments are passed to `get_subprocess_output()` in the form of a list, with the command and its arguments as a string within the list.

For example, a command that is entered at the command prompt like this:

```shell
vgs -o vg_free
```

must be passed to `get_subprocess_output()` like this:

```python
out, err, retcode = get_subprocess_output(["vgs", "-o", "vg_free"], self.log, raise_on_empty_output=True)
```

When you run the command-line program, the check captures the same output as running on the command line in the terminal. Do string processing on the output and call `int()` or `float()` on the result to return a numerical type.

If you do not do string processing on the output of the subprocess, or if it does not return an integer or a float, the check appears to run without errors but doesn't report any metrics or events. The check also fails to return metrics or events if the Agent user does not have the correct permissions on any files or directories referenced in the command, or the correct permissions to run the command passed as an argument to `get_subprocess_output()`.

Here is an example of a check that returns the results of a command-line program:

```python
# ...
from datadog_checks.base.utils.subprocess_output import get_subprocess_output

class LSCheck(AgentCheck):
    def check(self, instance):
        files, err, retcode = get_subprocess_output(["ls", "."], self.log, raise_on_empty_output=True)
        file_count = len(files.split('\n')) - 1  #len() returns an int by default
        self.gauge("file.count", file_count,tags=['TAG_KEY:TAG_VALUE'] + self.instance.get('tags', []))
```

## Sending data from a load balancer{% #sending-data-from-a-load-balancer %}

A common use case for writing a custom Agent check is to send Datadog metrics from a load balancer. Before you get started, follow the steps in Configuration.

To expand the files to send data from your load balancer:

1. Replace the code in `custom_checkvalue.py` with the following (replacing the value of `lburl` with the address of your load balancer):

In the `checks.d/custom_checkvalue.py` file:

   ```python
   import urllib2
   import simplejson
   from checks import AgentCheck

   class CheckValue(AgentCheck):
     def check(self, instance):
       lburl = instance['ipaddress']
       response = urllib2.urlopen("http://" + lburl + "/rest")
       data = simplejson.load(response)

       self.gauge('coreapp.update.value', data["value"])
```



1. Update the `custom_checkvalue.yaml` file (replacing `ipaddress` with your load balancer's IP address):

In the `conf.d/custom_checkvalue.yaml` file:

   ```yaml
   init_config:

   instances:
     - ipaddress: 1.2.3.4
```



1. [Restart your Agent](https://docs.datadoghq.com/agent/configuration/agent-commands/?tab=agentv6v7#restart-the-agent). Within a minute, you should see a new metric show up in the [Metric Summary](https://app.datadoghq.com/metric/summary) called `coreapp.update.value` that sends the metrics from your load balancer.

1. [Create a dashboard](https://docs.datadoghq.com/dashboards/) for this metric.

## Agent versioning{% #agent-versioning %}

Use the following try/except block to make the custom check compatible with any Agent version:

```python
try:
    # first, try to import the base class from new versions of the Agent
    from datadog_checks.base import AgentCheck
except ImportError:
    # if the above failed, the check is running in Agent version < 6.6.0
    from checks import AgentCheck

# content of the special variable __version__ will be shown in the Agent status page
__version__ = "1.0.0"

class HelloCheck(AgentCheck):
    def check(self, instance):
        self.gauge('hello.world', 1, tags=['TAG_KEY:TAG_VALUE'] + self.instance.get('tags', []))
```

## Further Reading{% #further-reading %}

- [Developing on Datadog](https://docs.datadoghq.com/developers/)
