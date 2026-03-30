# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/templates/full-kubernetes-exporter.md

# Kubernetes (advanced)

info

This use-case is an extension of the [basic Kubernetes use-case](/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/.md). If you haven't already, we recommend you to read it first.

Kubernetes has become one of the most popular ways to deploy microservice based applications. As the number of your microservices grow, and more clusters are deployed across several regions, it becomes complicated and tedious to keep track of all of your deployments, services, and jobs.

Using Port's Kubernetes Exporter, you can keep track of your K8s resources and export all the data to Port. You will use K8s' built in metadata to create Entities in Port and keep track of their state.

tip

Get to know the basics of our Kubernetes exporter [here!](/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/.md)

![](/img/build-your-software-catalog/sync-data-to-catalog/kubernetes/k8sAdvancedView.png)

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

The installation script provides a convenient way to create your blueprints. Using the `CUSTOM_BP_PATH` environment variable, you can fetch a pre-defined `blueprints.json` to create your blueprints. For this use-case, you will use [this file](https://github.com/port-labs/template-assets/blob/main/kubernetes/blueprints/kubernetes_complete_usecase_bps.json) to define your blueprints. Do this by running:

```
export CUSTOM_BP_PATH="https://raw.githubusercontent.com/port-labs/template-assets/main/kubernetes/blueprints/kubernetes_complete_usecase_bps.json"
```

This `blueprints.json` file defines the following blueprints:

* Cluster;
* Namespace;
* Node;
* Pod;
* ReplicaSet
* Workload \*;

note

* `Workload` is an abstraction of Kubernetes objects which create and manage pods. By creating this blueprint, you can avoid creating a dedicated blueprint per Workload type, all of which will likely look pretty similar. Here is the list of kubernetes objects `Workload` will represent:

  * Deployment;
  * StatefulSet;
  * DaemonSet.

### Exporting custom resource mapping[â](#exporting-custom-resource-mapping "Direct link to Exporting custom resource mapping")

Using the `CONFIG_YAML_URL` parameter, you can define a custom resource mapping to use when installing the exporter.

In this use-case you will be using **[this configuration file](https://github.com/port-labs/template-assets/blob/main/kubernetes/kubernetes_v1_config.yaml)**. To achieve this, run:

```
export CONFIG_YAML_URL="https://raw.githubusercontent.com/port-labs/template-assets/main/kubernetes/kubernetes_v1_config.yaml"
```

You can now run the installation script using the following code snippet:

```
export CLUSTER_NAME="my-cluster"
export PORT_CLIENT_ID="my-port-client-id"
export PORT_CLIENT_SECRET="my-port-client-secret"
curl -s https://raw.githubusercontent.com/port-labs/template-assets/main/kubernetes/install.sh | bash
```

That's it! You can now browse to your Port environment to see that your blueprints have been created, and entities are being reported to Port using the freshly installed k8s exporter.

## Summary[â](#summary "Direct link to Summary")

In this use-case, using the installation script, you:

* set up your Port environment by creating blueprints defining different k8s resources;
* installed Port's k8s exporter with a configuration allowing you to export important data from your cluster;
* fetched k8s resources from you cluster as entities to your Port environment

## How does the installation script work?[â](#how-does-the-installation-script-work "Direct link to How does the installation script work?")

Port's K8s exporter installation script will assist you in the process of installing Port's K8s exporter template using helm chart.

This script will help you with:

* setting up your custom Port [blueprints](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/.md);
* installing Port's k8s exporter using helm (check out the Helm chart's [source code](https://github.com/port-labs/helm-charts/tree/main/charts/port-k8s-exporter));
* deploying your custom [integration resources configuration](/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/.md#exporter-configuration-structure)

tip

You can view the bash script [here](https://github.com/port-labs/template-assets/blob/main/kubernetes/install.sh).

### General installation configuration[â](#general-installation-configuration "Direct link to General installation configuration")

The script supports configuration via environment variables.

For each variable you'd like to set, run the following command before running the script:

```
export {VARIABLE_NAME}={value}
```

| Environment Variable | Description                                                                                                                                                                                                                  | Default                                                                                    |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `PORT_CLIENT_ID`     | **Required** - Your Port organization's Client ID used to authenticate the exporter to Port                                                                                                                                  |                                                                                            |
| `PORT_CLIENT_SECRET` | **Required** - Your Port organization's Client Secret used to authenticate the exporter to Port                                                                                                                              |                                                                                            |
| `CUSTOM_BP_PATH`     | **Required** - The URL/path to a json file with an array of blueprint objects to create. Can be either a `https://domain.com/path/to/blueprint.json` format URL, or a local path to a file `envs/production/blueprint.json`. |                                                                                            |
| `CONFIG_YAML_URL`    | **Required** - The URL/path to the desired integration resource mapping. Can be either an https format URL`https://domain.com/path/to/config.yaml`, or a local path to a file `envs/production/config.yaml`                  | `https://github.com/port-labs/template-assets/blob/main/kubernetes/kubernetes_config.yaml` |
| `TARGET_NAMESPACE`   | **Optional** - The Kubernetes namespace in which the exporter will be installed                                                                                                                                              | `port-k8s-exporter`                                                                        |
| `DEPLOYMENT_NAME`    | **Optional** - The Kubernetes deployment name the exporter will be installed as                                                                                                                                              | `port-k8s-exporter`                                                                        |
| `CLUSTER_NAME`       | **Optional** - The cluster's name as it will be exported to. Check out the note bellow for more information.                                                                                                                 | `my-cluster`                                                                               |

note

* **CLUSTER\_NAME:** The script will set the cluster's name as the `CLUSTER_NAME` environment variable. This name will be used as the cluster's name in integration resources configuration. If you'd like to change the cluster's name, you can do so by setting the `CLUSTER_NAME` environment variable before running the script.
* **CUSTOM\_BP\_PATH:** It is important to order the blueprints while taking in to account the necessary relations for each blueprint. Once a blueprint was created, attempting to recreate it using the script will fail. To recreate a blueprint using the script, first delete the blueprint.
