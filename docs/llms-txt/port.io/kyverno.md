# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/templates/kyverno.md

# Kyverno

[Kyverno](https://kyverno.io/) is a policy engine designed for Kubernetes. Kyverno policies can validate, mutate, generate, and cleanup Kubernetes resources, allowing cluster administrators to enforce configuration best practices for their clusters.

Using Port's Kubernetes Exporter, you can keep track of all Kyverno resources across your different clusters and export all the policies and reports to Port. You will use built in metadata from your kubernetes resources and CRDs to create entities in Port and keep track of their state.

Our Kubernetes exporter basics

Get to know the basics of our Kubernetes exporter [here!](/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/.md)

![](/img/build-your-software-catalog/sync-data-to-catalog/kubernetes/k8sKyvernoView.png)

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

The installation script provides a convenient way to create your blueprints. Using the `CUSTOM_BP_PATH` environment variable, you can fetch a pre-defined `blueprints.json` to create your blueprints. For this use-case, you will use [this file](https://github.com/port-labs/template-assets/blob/main/kubernetes/blueprints/kyverno-blueprints.json) to define your blueprints. Do this by running:

```
export CUSTOM_BP_PATH="https://github.com/port-labs/template-assets/blob/main/kubernetes/blueprints/kyverno-blueprints.json"
```

This `blueprints.json` file defines the following blueprints:

* Cluster
* Namespace
* Workload
* Kyverno Policy
* Kyverno Policy Report

Blueprint information

* `Workload` is an abstraction of Kubernetes objects which create and manage pods. By creating this blueprint, you can avoid creating a dedicated blueprint per Workload type, all of which will likely look pretty similar. Here is the list of kubernetes objects `Workload` will represent:

  * Deployment
  * StatefulSet
  * DaemonSet

* `Kyverno Policy` is one of the most important Kyverno resources, giving developers the capability to set and enforce policy rules in their Kubernetes cluster.

* `Kyverno Policy Report` is another important Kyverno resource that contains the results of applying the policies to the Kubernetes cluster.

Below are the Kyverno blueprint schemas used in the exporter:

**Kyverno policy blueprint (click to expand)**

Create in Port

```
  {
    "identifier":"kyvernoPolicy",
    "title":"Kyverno Policy",
    "icon":"Cluster",
    "schema":{
        "properties":{
          "admission":{
              "title":"Admission",
              "type":"boolean",
              "icon":"DefaultProperty"
          },
          "background":{
              "title":"Background",
              "type":"boolean",
              "icon":"DefaultProperty"
          },
          "createdAt":{
              "title":"Created At",
              "type":"string",
              "format":"date-time",
              "icon":"DefaultProperty"
          },
          "validationFailureAction":{
              "icon":"DefaultProperty",
              "title":"Validation Failure Action",
              "type":"string",
              "enum":[
                "Audit",
                "Enforce"
              ],
              "enumColors":{
                "Audit":"lightGray",
                "Enforce":"lightGray"
              }
          }
        },
        "required":[]
    },
    "mirrorProperties":{},
    "calculationProperties":{},
    "aggregationProperties":{},
    "relations":{
        "namespace":{
          "title":"Namespace",
          "target":"namespace",
          "required":false,
          "many":false
        }
    }
  }
```

**Kyverno policy report blueprint (click to expand)**

Create in Port

```
  {
    "identifier":"kyvernoPolicyReport",
    "title":"Kyverno Policy Report",
    "icon":"Cluster",
    "schema":{
        "properties":{
          "createdAt":{
              "title":"Created At",
              "type":"string",
              "format":"date-time"
          },
          "pass":{
              "title":"Pass",
              "type":"number"
          },
          "fail":{
              "title":"Fail",
              "type":"number"
          },
          "warn":{
              "title":"Warn",
              "type":"number"
          },
          "error":{
              "title":"Error",
              "type":"number"
          },
          "skip":{
              "title":"Skip",
              "type":"number"
          }
        },
        "required":[]
    },
    "mirrorProperties":{},
    "calculationProperties":{},
    "aggregationProperties":{},
    "relations":{
        "namespace":{
          "title":"Namespace",
          "target":"namespace",
          "required":false,
          "many":false
        }
    }
  }
```

### Exporting custom resource mapping[â](#exporting-custom-resource-mapping "Direct link to Exporting custom resource mapping")

Using the `CONFIG_YAML_URL` parameter, you can define a custom resource mapping to use when installing the exporter.

In this use-case you will be using the **[this configuration file](https://github.com/port-labs/template-assets/blob/main/kubernetes/templates/kyverno-kubernetes_v1_config.yaml)**. To achieve this, run:

```
export CONFIG_YAML_URL="https://github.com/port-labs/template-assets/blob/main/kubernetes/templates/kyverno-kubernetes_v1_config.yaml"
```

Below is the mapping for the Kyverno resources:

**Kyverno policy mapping (click to expand)**

```
- kind: kyverno.io/v1/policies
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        - identifier: .metadata.name + "-" + .metadata.namespace + "-" + env.CLUSTER_NAME
          title: .metadata.name
          icon: '"Cluster"'
          blueprint: '"kyvernoPolicy"'
          properties:
            admission: .spec.admission
            background: .spec.background
            validationFailureAction: .spec.validationFailureAction
            createdAt: .metadata.creationTimestamp
          relations:
            namespace: .metadata.namespace + "-" + env.CLUSTER_NAME

- kind: kyverno.io/v1/clusterpolicies
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        - identifier: .metadata.name + "-" + env.CLUSTER_NAME
          title: .metadata.name
          icon: '"Cluster"'
          blueprint: '"kyvernoPolicy"'
          properties:
            admission: .spec.admission
            background: .spec.background
            validationFailureAction: .spec.validationFailureAction
            createdAt: .metadata.creationTimestamp
```

**Kyverno policy report mapping (click to expand)**

```
- kind: wgpolicyk8s.io/v1alpha2/policyreports
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        - identifier: .metadata.name + "-" + .metadata.namespace + "-" + env.CLUSTER_NAME
          title: .scope.name
          icon: '"Cluster"'
          blueprint: '"kyvernoPolicyReport"'
          properties:
            pass: .summary.pass
            fail: .summary.fail
            warn: .summary.warn
            error: .summary.error
            skip: .summary.skip
            createdAt: .metadata.creationTimestamp
          relations:
            namespace: .metadata.namespace + "-" + env.CLUSTER_NAME

- kind: wgpolicyk8s.io/v1alpha2/clusterpolicyreports
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        - identifier: .metadata.name + "-" + env.CLUSTER_NAME
          title: .scope.name
          icon: '"Cluster"'
          blueprint: '"kyvernoPolicyReport"'
          properties:
            pass: .summary.pass
            fail: .summary.fail
            warn: .summary.warn
            error: .summary.error
            skip: .summary.skip
            createdAt: .metadata.creationTimestamp
```

You can now browse to your Port environment to see that your blueprints have been created, and your k8s and Kyverno resources are being reported to Port using the freshly installed k8s exporter.
