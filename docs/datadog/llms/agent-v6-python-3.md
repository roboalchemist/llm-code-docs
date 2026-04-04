# Source: https://docs.datadoghq.com/agent/guide/agent-v6-python-3.md

---
title: Python Version Management
description: >-
  Configure Datadog Agent v6 to use Python 3 runtime for Agent checks and
  integrations instead of the default Python 2.
breadcrumbs: Docs > Agent > Agent Guides > Python Version Management
---

# Python Version Management

If you are using Agent v6, Datadog recommends that you [upgrade to Agent v7](https://docs.datadoghq.com/agent/versions/upgrade_to_agent_v7/?tab=linux). Agent v7 only includes support for Python 3.

However, there may be a case where you wish to continue using Agent v6 while updating to Python 3. Starting with Datadog Agent v6.14.0, Agent v6 integrates both Python 2 and Python 3 runtimes. This means that Agent Checks can be run either with Python 2 or Python 3, depending on the Agent configuration.

## Use Python 3 with Datadog Agent v6{% #use-python-3-with-datadog-agent-v6 %}

By default, the Agent v6 uses the Python 2 runtime. Below are instructions for how to configure Agent v6 to use the Python 3 runtime:

- Host Agent
- Container Agent
  - Helm
  - Datadog Operator
  - DaemonSet
- Deployment tools
  - Chef
  - Puppet
  - Ansible

This configuration is not supported for the Azure VM Extension.

### Host Agent{% #host-agent %}

1. Set the `python_version` configuration option in your [`datadog.yaml`](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/#agent-main-configuration-file) configuration file:

   ```yaml
   python_version: 3
   ```

1. [Restart the Agent](https://docs.datadoghq.com/agent/configuration/agent-commands/#restart-the-agent).

Alternatively, specify which Python runtime you want to use by setting the `DD_PYTHON_VERSION` environment variable to `2` or `3`. Environment variables take precedence over configuration options in `datadog.yaml`. For example, by setting the `DD_PYTHON_VERSION` environment variable, the `python_version` option in `datadog.yaml` is ignored.

This is an Agent-wide configuration option. **All Python checks launched by an Agent use the same Python runtime**.

### Container Agent{% #container-agent %}

Datadog provides Agent container images for Python 2 and Python 3.

- Image tags starting with `6.`, like `6.34.0` or `6.34.0-jmx`, are images containing the Python 2 runtime.
- Image tags starting with `7.`, like `7.34.0` or `7.34.0-jmx`, are images containing the Python 3 runtime.

To switch from Python 2 to Python 3, update the image tag used to deploy the Agent.

{% tab title="Helm" %}
By default, the [Datadog Helm chart](https://artifacthub.io/packages/helm/datadog/datadog/) uses the Agent 7 image that embeds the Python 3 runtime.

To keep the Datadog Agent updated, edit your `datadog-values.yaml` to remove any information under the `agent.image` and the `clusterChecksRunner.image` sections.

To use a specific container registry, set it with `agent.image.repository` and `clusterChecksRunner.image.repository`. Ensure that `agents.image.tag` and `clusterChecksRunner.image.tag` are undefined.

The default registry is `gcr.io/datadoghq/agent`.

```yaml
agent:
  image:
    repository: public.ecr.aws/datadog/agent

clusterChecksRunner:
  image:
    repository: public.ecr.aws/datadog/agent
```

To set the Agent to a specific version, set `agents.image.tag` and `clusterChecksRunner.image.tag`. All image tags starting with `7.*` embed the Python 3 runtime.

```yaml
agent:
  image:
    tag: 7.34.0

clusterChecksRunner:
  image:
    tag: 7.34.0
```

You can use both options at the same time.

```yaml
agent:
  image:
    repository: public.ecr.aws/datadog/agent
    tag: 7.34.0

clusterChecksRunner:
  image:
    repository: public.ecr.aws/datadog/agent
    tag: 7.34.0
```

{% /tab %}

{% tab title="Datadog Operator" %}
By default, the [Datadog Operator](https://github.com/DataDog/datadog-operator) uses an `agent:7.*.*` image that embeds the Python 3 runtime.

If the image information is not specified in the `DatadogAgent` resource, the Operator deploys a Python 3 Datadog Agent image.

If you have previously pinned the image version:

```yaml
apiVersion: datadoghq.com/v2alpha1
metadata:
  name: datadog
spec:
  override:
    clusterChecksRunner:
      image:
        tag: 6.33.0
    nodeAgent:
      image:
        tag: 6.33.0
```

or you are using `image.name`:

```yaml
apiVersion: datadoghq.com/v2alpha1
metadata:
  name: datadog
spec:
  global:
    credentials:
      apiKey: <DATADOG_API_KEY>
      appKey: <DATADOG_APP_KEY>
  override:
    # ...
    nodeAgent:
      image:
        name: gcr.io/datadoghq/agent:6.33.0
    # ...
    clusterChecksRunner:
      image:
        name: gcr.io/datadoghq/agent:6.33.0
```

Use the `spec.global.registry` if you need to change the default registry. The default is `gcr.io/datadoghq/agent`.

Then, pin the Agent 7 image tag in `spec.override.nodeAgent.image.tag`.

If you have enabled cluster check runners deployment, also pin the Agent 7 image tag in `spec.override.clusterChecksRunner.image.tag`.

```yaml
apiVersion: datadoghq.com/v2alpha1
metadata:
  name: datadog
spec:
  # ...
  global:
    registry: public.ecr.aws/datadog
  override:
    # ...
    nodeAgent:
      image:
        tag: 7.33.0
    # ...
    clusterChecksRunner:
      image:
        tag: 7.33.0
```

**Note**: Datadog recommends that you do not set the `*.image.tag`. Instead, let the Datadog Operator keep the Agent image tag up-to-date with an Agent 7 image.

If you need to use an Agent JMX image, you can set it without specifying the Agent `*.image.tag`:

```yaml
apiVersion: datadoghq.com/v2alpha1
metadata:
  name: datadog
spec:
  # ...
  global:
    registry: public.ecr.aws/datadog
  override:
    # ...
    nodeAgent:
      image:
        jmxEnabled: true
    clusterChecksRunner:
      image:
        jmxEnabled: true
```

{% /tab %}

{% tab title="Manual (DaemonSet)" %}
In your DaemonSet manifest, update the image tag in each container definition:

- Each `spec.template.spec.containers[*].image` value
- Each `spec.template.spec.initContainers[*].image` value

For example, if your previous image value was `gcr.io/datadoghq/agent:6.33.0`, update it to `gcr.io/datadoghq/agent:7.33.0`.

**Before**:

```yaml
apiVersion: apps/v1
spec:
  template:
    spec:
      containers:
      - name: agent
        image: gcr.io/datadoghq/agent:6.33.0
        # ...
```

**After**:

```yaml
apiVersion: apps/v1
spec:
  template:
    spec:
      containers:
      - name: agent
        image: gcr.io/datadoghq/agent:7.33.0
        # ...
```

{% /tab %}

### Deployment tools{% #deployment-tools %}

{% tab title="Chef" %}
Use the `extra_config` field to set the `python_version` field to `3`:

```
default_attributes(
   'datadog' => {
     'extra_config' => {
       'python_version' => '3'
     }
   }
 )
```

{% /tab %}

{% tab title="Puppet" %}
Use the `agent_extra_config` field to set the `python_version`field to `3`:

```
class { "datadog_agent":
    agent_extra_options => {
        python_version => 3,
    },
}
```

{% /tab %}

{% tab title="Ansible" %}
Set the `python_version` to `3` inside of your `datadog_config`:

```
datadog_config:
  python_version: 3
```

{% /tab %}

## Further Reading{% #further-reading %}

- [Upgrade to Agent v7](https://docs.datadoghq.com/agent/versions/upgrade_to_agent_v7/)
