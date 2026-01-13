# Source: https://docs.datadoghq.com/agent/guide/use-community-integrations.md

---
title: Use Community and Marketplace Integrations
description: >-
  Installation and configuration guide for community-developed and Marketplace
  integrations with the Datadog Agent across different environments.
breadcrumbs: Docs > Agent > Agent Guides > Use Community and Marketplace Integrations
source_url: https://docs.datadoghq.com/guide/use-community-integrations/index.html
---

# Use Community and Marketplace Integrations

## Overview{% #overview %}

Community developed integrations for the Datadog Agent are stored in the Datadog [integrations-extra](https://github.com/DataDog/integrations-extras) GitHub repository. They are not packaged with the Agent, but can be installed as add-ons.

## Setup{% #setup %}

Follow the installation method for your environment.

{% tab title="Host installation" %}
For Agent v7.21+ / v6.21+:

1. Run the following command to install the Agent integration:

   ```
   sudo -u dd-agent datadog-agent integration install -t datadog-<INTEGRATION_NAME>==<INTEGRATION_VERSION>
   ```

The version for the integration can be found in the respective changelog on the integration's GitHub repository.

1. Manage your integration configuration files in the same way as [core integrations](https://docs.datadoghq.com/getting_started/integrations/), placing each configuration in `/etc/datadog-agent/conf.d/<INTEGRATION_NAME>.d/conf.yaml`.

1. [Restart the Agent](https://docs.datadoghq.com/agent/configuration/agent-commands/#restart-the-agent).

{% /tab %}

{% tab title="Containerized installation" %}
#### Build the image{% #build-the-image %}

To use a community or Marketplace integration in a containerized environment, build a custom Agent image that includes your desired integration.

Building a custom image ensures the integration persists across deployments each time a container starts.

Use the following Dockerfile to build a custom version of the Agent that includes the `<INTEGRATION_NAME>` from [integrations-extras](https://github.com/DataDog/integrations-extras). If you are installing a Marketplace integration, the `<INTEGRATION_NAME>` is available in the configuration instructions.

```dockerfile
FROM gcr.io/datadoghq/agent:latest
RUN agent integration install -r -t datadog-<INTEGRATION_NAME>==<INTEGRATION_VERSION>
```

Build and push the image:

```
docker build -t <RepoName>/agent:<version>-custom .
docker push <RepoName>/agent:<version>-custom
```

If you use both `amd64` and `arm` host architectures, you can also [build multi-architecture images](https://docs.docker.com/build/building/multi-platform/).

#### Deploy the image{% #deploy-the-image %}

To deploy the custom image in Kubernetes, update your Helm chart or Datadog Operator configuration to pull the image.

##### Helm:{% #helm %}

```yaml
agents:
  image:
    tag: <version>
    tagSuffix: "custom"
    repository: <Registry>/<RepoName>/agent
```

##### Operator:{% #operator %}

```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  global:
    registry: <Registry>/<RepoName>
    #(...)  
  override:
    nodeAgent:
      image:
        name: agent
        tag: <version>-custom
```

Use [Autodiscovery](https://docs.datadoghq.com/agent/autodiscovery/) to enable and configure the integration.
{% /tab %}

If your site restricts network access, ensure you have added all of the [`ip-ranges`](https://docs.datadoghq.com/agent/configuration/network) to your inclusion list, or download the integration manually.

## Further Reading{% #further-reading %}

- [Agent Troubleshooting](https://docs.datadoghq.com/agent/troubleshooting/)
- [Create a New Integration](https://docs.datadoghq.com/developers/integrations/agent_integration)
