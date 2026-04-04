# Source: https://archivedocs.stackstate.com/5.1/setup/install-stackstate/linux/before_you_install.md

# Before you install

{% hint style="info" %}
StackState prefers Kubernetes!\
In the future we will move away from Linux support. Read how to [migrate from the Linux install of StackState to the Kubernetes install](https://archivedocs.stackstate.com/5.1/setup/install-stackstate/kubernetes_openshift/migrate_from_linux).
{% endhint %}

StackState can be installed either with Linux packages on one or two Linux machines or with Helm on a [Kubernetes cluster](https://archivedocs.stackstate.com/5.1/setup/install-stackstate/kubernetes_openshift).

## Choosing your installation type

Before setting up StackState, you need to choose whether you want to run StackState in Development, POC, or Production mode.

* **Development setup:** requires only one machine, but will be limited to 1000 components/relations per view, due to the limited setup. This is recommended for small trials.
* **POC setup:** used for bigger installations, giving almost the same power as production, but isn't suited for processing perpetual data streams.
* **Production setup:** used when bringing StackState to production or when the other environments are too limiting.

## Requirements

Before starting the installation, ensure your system(s) meet the StackState [installation requirements](https://archivedocs.stackstate.com/5.1/setup/install-stackstate/requirements).

## Packages

There is an RPM package available that provides easy installation and upgrade of StackState on Fedora, Red Hat or CentOS. For Debian and Ubuntu, there is a DEB package available. Packages can be obtained from our [distribution website](https://archivedocs.stackstate.com/5.1/setup/install-stackstate/linux/download).

## Installation

StackState supports three different installation configurations:

* [Production setup](https://archivedocs.stackstate.com/5.1/setup/install-stackstate/linux/production-installation) suitable for production use.
* [Proof-of-concept (POC) setup](https://archivedocs.stackstate.com/5.1/setup/install-stackstate/linux/poc-installation) suitable for proof of concepts. This isn't suited for processing perpetual data streams.
* [Development setup](https://archivedocs.stackstate.com/5.1/setup/install-stackstate/linux/development-installation) suitable for a pilot or demo. This setup can deal with limited amounts of topology (max 1000 components/relations per view).

## Upgrading

To upgrade your StackState installation, see the instructions in our [upgrading guide](https://archivedocs.stackstate.com/5.1/setup/upgrade-stackstate/steps-to-upgrade).

## Authentication and Authorization

StackState provides Role Based Access Control functionality that works with different authentication providers. See the [Authentication](https://archivedocs.stackstate.com/5.1/configure/security/authentication/authentication_options) and [RBAC](https://archivedocs.stackstate.com/5.1/configure/security/rbac/role_based_access_control) pages for more information on the topic.

## Troubleshooting

If you have any issues installing StackState, refer to our [troubleshooting guide](https://archivedocs.stackstate.com/5.1/setup/install-stackstate/troubleshooting) or contact our technical support.
