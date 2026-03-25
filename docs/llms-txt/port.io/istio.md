# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/templates/istio.md

# Istio

[Istio](https://istio.io/latest/docs/setup/getting-started/) is an open-source service mesh that provides a uniform way to connect, manage, and secure microservices.

Using Port's Kubernetes Exporter, you can keep track of all Istio resources across your different clusters and export all the data to Port. You will use built in metadata from your kubernetes resources and CRDs to create Entities in Port and keep track of their state.

tip

Get to know the basics of our Kubernetes exporter [here!](/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/.md)

![](/img/build-your-software-catalog/sync-data-to-catalog/kubernetes/k8sIstioView.png)

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* This guide assumes you have completed the [visualize your services' k8s runtime guide](https://docs.port.io/guides/all/visualize-service-k8s-runtime/)
* [Helm](https://helm.sh) must be installed to use the chart. Please refer to Helm's [documentation](https://helm.sh/docs) to get started
* The `jq` command must installed
* The `yq` command must installed
* The `kubectl` command must be installed
* Have your [Port credentials](/build-your-software-catalog/custom-integration/api/.md#find-your-port-credentials) ready.

In this use-case, you will use a custom bash script which will assist you in the process of installing Port's K8s exporter.

The script will install the helm chart to the Kubernetes cluster which is currently in kubectl context. To view the context name of the cluster the exporter will be installed on, run:

```
kubectl config current-context
```

## Setting up blueprints & resource mapping[â](#setting-up-blueprints--resource-mapping "Direct link to Setting up blueprints & resource mapping")

The following section will guide you through the process of setting up your blueprints and resource mapping using the installation script. You can read more about the installation script [here](#how-does-the-installation-script-work).

### Creating blueprints[â](#creating-blueprints "Direct link to Creating blueprints")

The installation script provides a convenient way to create your blueprints. Using the `CUSTOM_BP_PATH` environment variable, you can fetch a pre-defined `blueprints.json` to create your blueprints. For this use-case, you will use [this file](https://github.com/port-labs/template-assets/blob/main/kubernetes/blueprints/istio-blueprints.json) to define your blueprints. Do this by running:

```
export CUSTOM_BP_PATH="https://raw.githubusercontent.com/port-labs/template-assets/main/kubernetes/blueprints/istio-blueprints.json"
```

This `blueprints.json` file defines the following blueprints:

* Cluster
* Namespace
* Workload
* Istio Gateway
* Istio Virtual Service

Workload blueprint components

* `Workload` is an abstraction of Kubernetes objects which create and manage pods. By creating this blueprint, you can avoid creating a dedicated blueprint per Workload type, all of which will likely look pretty similar. Here is the list of kubernetes objects `Workload` will represent:

  * Deployment
  * ReplicaSet
  * StatefulSet
  * DaemonSet

Below are the Istio blueprint schemas used in the exporter:

**Istio gateway blueprint (click to expand)**

Create in Port

```
{
  "identifier": "gateways",
  "description": "This blueprint represents a service in our software catalog",
  "title": "Istio Gateways",
  "icon": "Cloud",
  "schema": {
    "properties": {
      "name": {
        "type": "string"
      },
      "ports": {
        "type": "array"
      },
      "labels": {
        "type": "object"
      },
      "selector": {
        "type": "object"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {
    "namespace": {
      "target": "namespace",
      "required": true,
      "many": false
    }
  }
}
```

**Istio virtual service blueprint (click to expand)**

Create in Port

```
{
  "identifier": "virtualServices",
  "description": "This blueprint represents a service in our software catalog",
  "title": "Virtual Services",
  "icon": "Istio",
  "schema": {
    "properties": {
      "hosts": {
        "type": "array"
      },
      "match": {
        "type": "array"
      },
      "labels": {
        "type": "object"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {
    "gateways": {
      "target": "gateways",
      "many": true
    }
  }
}
```

### Exporting custom resource mapping[â](#exporting-custom-resource-mapping "Direct link to Exporting custom resource mapping")

Using the `CONFIG_YAML_URL` parameter, you can define a custom resource mapping to use when installing the exporter.

In this use-case you will be using the **[this configuration file](https://github.com/port-labs/template-assets/blob/main/kubernetes/templates/istio-kubernetes_v1_config.yaml)**. To achieve this, run:

```
export CONFIG_YAML_URL="https://raw.githubusercontent.com/port-labs/template-assets/main/kubernetes/templates/istio-kubernetes_v1_config.yaml"
```

Below is the mapping for the Istio resources:

**Istio gateway mapping (click to expand)**

```
- kind: networking.istio.io/v1beta1/gateways
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        - identifier: .metadata.name + "-" + .metadata.namespace
          blueprint: '"gateways"'
          properties:
            title: .metadata.name
            ports: .spec.servers[].port.number
            name: .metadata.name
            labels: .metadata.labels
            selector: .spec.selector
          relations:
            namespace: .metadata.namespace
```

**Istio virtual service mapping (click to expand)**

```
- kind: networking.istio.io/v1beta1/virtualservices
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        - identifier: .metadata.name + "-" + .metadata.namespace
          blueprint: '"virtualServices"'
          properties:
            title: .metadata.name
            hosts: .spec.hosts
            match: .spec.http[].match
            labels: .metadata.labels
          relations:
            gateways: .spec.gateways[] + "-" + .metadata.namespace
            services: .metadata.namespace as $namespace | .spec.http[].route[].destination.host + "-" + $namespace
```

You can now browse to your Port environment to see that your blueprints have been created, and your k8s and Istio resources are being reported to Port using the freshly installed k8s exporter.
