# Source: https://archivedocs.stackstate.com/5.1/develop/developer-guides/monitors/create-custom-monitors.md

# Create monitors

## Overview

Monitors can be attached to any number of elements in the StackState topology to calculate a health state based on 4T data. Each monitor consists of a monitor definition and a monitor function. Monitors are created and managed by StackPacks, you can also create custom monitors and monitor functions outside of a StackPack without having to modify any configuration.

The example on this page creates a CPU metric monitor using an example monitor function.

➡️ [Learn more about the STJ file format used for monitor definitions](https://archivedocs.stackstate.com/5.1/develop/developer-guides/monitors/monitor-stj-file-format)

## Example - CPU metric monitor

To create the example CPU metric custom monitor in StackState we will:

1. [Create a new STJ import file.](#create-a-new-stj-import-file)
2. [Populate the monitor node.](#populate-the-monitor-node)
3. [Populate the parameters of the monitor function invocation.](#populate-the-parameters-of-the-monitor-function-invocation)
4. [Apply the newly created monitor in StackState.](#apply-the-newly-created-monitor-in-stackstate)
5. [Verify that your newly created monitor is working correctly.](#verify-that-your-newly-created-monitor-is-working-correctly)

### Create a new STJ import file

```json
{
  "_version": "1.0.39",
  "timestamp": "2022-05-23T13:16:27.369269Z[GMT]",
  "nodes": [
    ...
  ]
}
```

You can place multiple monitors on the same STJ file. You can also add other node types on the same import file.

➡️ [Learn more about the STJ file format used for monitor definitions](https://archivedocs.stackstate.com/5.1/develop/developer-guides/monitors/monitor-stj-file-format)

### Populate the monitor node

A monitor node of type `Monitor` needs to be added to the import file. This type of node is supported in API version 1.0.39 and above. The required fields are the `name`, `identifier` and `description`. The `identifier` should be a value that uniquely identifies this specific monitor definition. `intervalSeconds`, `function` and [`arguments`](https://archivedocs.stackstate.com/5.1/develop/developer-guides/monitor-stj-file-format#arguments) determine what validation rule and how often it's run. An optional parameter of `remediationHint` can be specified - it's a Markdown-encoded instruction of what to do if this monitor produces an unhealthy health state. It's displayed on the interface together with the monitor result panel.

Configuring the monitor function is best done by utilizing the [`get` helper function](https://archivedocs.stackstate.com/5.1/reference/stj/stj_reference#get) paired with the `identifier` of the function itself. In this example the function is named `Metric above threshold` and its identifier is `urn:system:default:monitor-function:metric-above-threshold`.

```json
{
  "_version": "1.0.39",
  "timestamp": "2022-05-23T13:16:27.369269Z[GMT]",
  "nodes": [
    {
      "_type": "Monitor",
      "name": "CPU Usage",
      "description": "A simple CPU-usage monitor. If the metric is above a given threshold, the state is set to CRITICAL.",
      "identifier": "urn:system:default:monitor:cpu-usage",
      "remediationHint": "Turn it off and on again.",
      "function": {{ get "urn:system:default:monitor-function:metric-above-threshold" }},
      "arguments": [
        ...
      ],
      "intervalSeconds": 60
    }
  ]
}
```

The invocation of the `get` helper function will automatically resolve to the ID of the desired function during import time.

➡️ [Learn more about the STJ file format used for monitor definitions](https://archivedocs.stackstate.com/5.1/develop/developer-guides/monitors/monitor-stj-file-format)

### Populate the parameters of the monitor function invocation

The parameters are different for each monitor function. In the case of `Metric above threshold` we need to populate `threshold`, `metrics` and `topologyIdentifierPattern`:

```json
{
  "_version": "1.0.39",
  "timestamp": "2022-05-23T13:16:27.369269Z[GMT]",
  "nodes": [
    {
      "_type": "Monitor",
      "name": "CPU Usage",
      "description": "A simple CPU-usage monitor. If the metric is above a given threshold, the state is set to CRITICAL.",
      "identifier": "urn:system:default:monitor:cpu-usage",
      "remediationHint": "Turn it off and on again.",
      "function": {{ get "urn:system:default:monitor-function:metric-above-threshold" }},
      "arguments": [{
        "_type": "ArgumentDoubleVal",
        "parameter": {{ get "urn:system:default:monitor-function:metric-above-threshold" "Type=Parameter;Name=threshold" }},
        "value": 90.0
      }, {
         "_type": "ArgumentStringVal",
        "parameter": {{ get "urn:system:default:monitor-function:metric-above-threshold" "Type=Parameter;Name=topologyIdentifierPattern" }},
        "value": "urn:host:/${tags.host}"
      }, {
        "_type": "ArgumentScriptMetricQueryVal",
        "parameter": {{ get "urn:system:default:monitor-function:metric-above-threshold" "Type=Parameter;Name=metrics" }},
        "script": "Telemetry\n.query(\"StackState Metrics\", \"\")\n.metricField(\"system.cpu.system\")\n.groupBy(\"tags.host\")\n.start(\"-1m\")\n.aggregation(\"mean\", \"15s\")"
      }],
      "intervalSeconds": 60
    }
  ]
}
```

Similar to the `function`, parameters can be referred to by utilizing the `get` helper function.

For further details of defining arguments in the monitor definition and how to work with commonly used parameters such as a metrics query or topology identifier, see [monitor STJ file format > Arguments](https://archivedocs.stackstate.com/5.1/develop/developer-guides/monitor-stj-file-format#arguments).

### Apply the newly created monitor in StackState

This can be achieved by using the dedicated StackState CLI command:

{% tabs %}
{% tab title="CLI: sts" %}

```
sts monitor apply -f path/to/the/file.stj
```

From StackState v5.0, the old `sts` CLI has been renamed to `stac` and there is a new `sts` CLI. The command(s) provided here are for use with the new `sts` CLI.

➡️ [Check which version of the `sts` CLI you are running](https://archivedocs.stackstate.com/5.1/setup/cli/cli-comparison#which-version-of-the-cli-am-i-running)
{% endtab %}

{% tab title="CLI: stac (deprecated)" %}
`stac monitor apply < path/to/the/file.stj`

⚠️ **From StackState v5.0, the old `sts` CLI is called `stac`. The old CLI is now deprecated.**

The new `sts` CLI replaces the `stac` CLI. It's advised to install the new `sts` CLI and upgrade any installed instance of the old `sts` CLI to `stac`. For details see:

* [Which version of the `sts` CLI am I running?](https://archivedocs.stackstate.com/5.1/setup/cli/cli-comparison#which-version-of-the-cli-am-i-running)
* [Install the new `sts` CLI and upgrade the old `sts` CLI to `stac`](https://archivedocs.stackstate.com/5.1/setup/cli/cli-sts#install-the-new-sts-cli)
* [Comparison between the CLIs](https://archivedocs.stackstate.com/5.1/setup/cli/cli-comparison)
  {% endtab %}
  {% endtabs %}

An alternative way is to include the newly created monitor in a custom StackPack and installing it.

### Verify that your newly created monitor is working correctly

You can check if your monitor is working correctly by invoking the CLI command:

{% tabs %}
{% tab title="CLI: sts" %}

```
# By ID
sts monitor status --id <id-of-a-monitor>
# By Identifier
sts monitor status --identifier <identifier-of-a-monitor>
```

From StackState v5.0, the old `sts` CLI has been renamed to `stac` and there is a new `sts` CLI. The command(s) provided here are for use with the new `sts` CLI.

➡️ [Check which version of the `sts` CLI you are running](https://archivedocs.stackstate.com/5.1/setup/cli/cli-comparison#which-version-of-the-cli-am-i-running)
{% endtab %}

{% tab title="CLI: stac (deprecated)" %}
`stac monitor status <id-or-identifier-of-a-monitor>`

⚠️ **From StackState v5.0, the old `sts` CLI is called `stac`. The old CLI is now deprecated.**

The new `sts` CLI replaces the `stac` CLI. It's advised to install the new `sts` CLI and upgrade any installed instance of the old `sts` CLI to `stac`. For details see:

* [Which version of the `sts` CLI am I running?](https://archivedocs.stackstate.com/5.1/setup/cli/cli-comparison#which-version-of-the-cli-am-i-running)
* [Install the new `sts` CLI and upgrade the old `sts` CLI to `stac`](https://archivedocs.stackstate.com/5.1/setup/cli/cli-sts#install-the-new-sts-cli)
* [Comparison between the CLIs](https://archivedocs.stackstate.com/5.1/setup/cli/cli-comparison)
  {% endtab %}
  {% endtabs %}

You can also preview the results it generates by invoking the CLI command:

{% tabs %}
{% tab title="CLI: sts" %}

```
# By ID
sts monitor run --id <id-of-a-monitor>
# By Identifier
sts monitor run --identifier <identifier-of-a-monitor>
```

From StackState v5.0, the old `sts` CLI has been renamed to `stac` and there is a new `sts` CLI. The command(s) provided here are for use with the new `sts` CLI.

➡️ [Check which version of the `sts` CLI you are running](https://archivedocs.stackstate.com/5.1/setup/cli/cli-comparison#which-version-of-the-cli-am-i-running)
{% endtab %}

{% tab title="CLI: stac (deprecated)" %}
`stac monitor preview <id-or-identifier-of-a-monitor>`

⚠️ **From StackState v5.0, the old `sts` CLI is called `stac`. The old CLI is now deprecated.**

The new `sts` CLI replaces the `stac` CLI. It's advised to install the new `sts` CLI and upgrade any installed instance of the old `sts` CLI to `stac`. For details see:

* [Which version of the `sts` CLI am I running?](https://archivedocs.stackstate.com/5.1/setup/cli/cli-comparison#which-version-of-the-cli-am-i-running)
* [Install the new `sts` CLI and upgrade the old `sts` CLI to `stac`](https://archivedocs.stackstate.com/5.1/setup/cli/cli-sts#install-the-new-sts-cli)
* [Comparison between the CLIs](https://archivedocs.stackstate.com/5.1/setup/cli/cli-comparison)
  {% endtab %}
  {% endtabs %}

## See also

* [Custom monitor functions](https://archivedocs.stackstate.com/5.1/develop/developer-guides/custom-functions/monitor-functions)
* [StackState `sts` CLI](https://archivedocs.stackstate.com/5.1/setup/cli/cli-sts)
* [StackState Template JSON (STJ)](https://archivedocs.stackstate.com/5.1/develop/reference/stj)
* [Develop your own StackPacks](https://archivedocs.stackstate.com/5.1/stackpacks/sdk)
* [Integrations](https://archivedocs.stackstate.com/5.1/stackpacks/integrations)
