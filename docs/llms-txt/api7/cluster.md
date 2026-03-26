# Source: https://docs.api7.ai/cloud/concepts/cluster.md

# What is Cluster

A typical architecture for API Gateway is composed of the control plane and data plane. The data plane is always acted by the proxy component (aka the gateway), which governs and forwards the user traffic; The control plane, as the name implies, controls the behaviors of the data plane (gateway instance) by delivering configurations like route and upstream. In addition, it also collects telemetry data from the data plane and visualizes them.

The control plane and data plane make up the gateway cluster. API7 Cloud provides the gateway cluster with managed control plane part and users themselves hosted data plane instances (i.e. [Apache APISIX](https://apisix.apache.org/)).

These gateway instances will attach to the cluster and share the same configurations like [service](https://docs.api7.ai/cloud/concepts/service.md), [route](https://docs.api7.ai/cloud/concepts/route.md), [consumer](https://docs.api7.ai/cloud/concepts/consumer.md), and [SSL](https://docs.api7.ai/cloud/concepts/ssl.md). Gateway instances' metrics are also collected to the cluster so that you can see them on the API7 Cloud monitoring page directly.

## How to Create a Cluster[â](#how-to-create-a-cluster "Direct link to How to Create a Cluster")

The cluster will be created with the organization automatically. So you don't have to create it by yourself.

tip

You'll be asked to create an organization when you log in to API7 Cloud for the first time.

## Plugins on Cluster[â](#plugins-on-cluster "Direct link to Plugins on Cluster")

You can also create [plugins](https://docs.api7.ai/cloud/concepts/plugin.md) on the cluster level, in case plugins will run for all API requests.

## What's Next[â](#whats-next "Direct link to What's Next")

* Learn about [Service](https://docs.api7.ai/cloud/concepts/service.md).
* Learn about [Plugin](https://docs.api7.ai/cloud/concepts/plugin.md).
