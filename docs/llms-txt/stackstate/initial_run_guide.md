# Source: https://archivedocs.stackstate.com/5.1/setup/install-stackstate/initial_run_guide.md

# Source: https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/initial_run_guide.md

# Initial run guide

## Overview

This page provides all the information you need to install and run StackState.

## Installation instructions

{% tabs %}
{% tab title="Kubernetes" %}
Install StackState on [Kubernetes](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift).
{% endtab %}

{% tab title="OpenShift" %}
Install StackState on [OpenShift](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/openshift_install).
{% endtab %}
{% endtabs %}

## Address and port

{% tabs %}
{% tab title="Kubernetes" %}
To access the StackState UI:

1. [Enable a port-forward](https://archivedocs.stackstate.com/self-hosted-setup/kubernetes_openshift/kubernetes_install#access-the-stackstate-ui).
2. Access the StackState UI at: <https://localhost:8080>
   {% endtab %}

{% tab title="OpenShift" %}
To access the StackState UI:

1. [Enable a port-forward](https://archivedocs.stackstate.com/self-hosted-setup/kubernetes_openshift/openshift_install#access-the-stackstate-ui).
2. Access the StackState UI at: <https://localhost:8080>
   {% endtab %}
   {% endtabs %}

## Default username and password

{% tabs %}
{% tab title="Kubernetes" %}
StackState is configured by default with the following administrator account:

* **username:** `admin`
* **password:** Set during installation. This is collected by the `generate_values.sh` script and stored in MD5 hash format in `values.yaml`
  {% endtab %}

{% tab title="OpenShift" %}
StackState is configured by default with the following administrator account:

* **username:** `admin`
* **password:** Set during installation. This is collected by the `generate_values.sh` script and stored in MD5 hash format in `values.yaml`
  {% endtab %}
  {% endtabs %}

## Troubleshooting

If you run into any problems during the installation of StackState or first run, check the [StackState installation troubleshooting guide](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/troubleshooting).

## Next steps

Once you have StackState up and running, you can get started setting up integrations

* [Install StackPacks to integrate with external systems](https://archivedocs.stackstate.com/get-started/k8s-quick-start-guide)
* [Explore your Kubernetes cluster](https://archivedocs.stackstate.com/views/k8s-views)
