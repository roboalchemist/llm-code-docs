# Source: https://archivedocs.stackstate.com/5.1/setup/data-management/clear_stored_data.md

# Source: https://archivedocs.stackstate.com/self-hosted-setup/data-management/clear_stored_data.md

# Clear stored data

The data in StackState is divided into four different sets:

* Elasticsearch data
* Kafka Topic data
* StackGraph data
* Metrics data

With this much data to store, it's important to have the means to manage it. There is a standard 30 days data retention period set in StackState. This can be configured according to your needs using the StackState CLI. Find out more about [StackState data retention](https://archivedocs.stackstate.com/self-hosted-setup/data-management/data_retention).

## Clear data manually

To clear stored data in StackState running on Kubernetes, it's recommended to run a clean install:

1. [Uninstall StackState](https://archivedocs.stackstate.com/uninstall#un-install-the-helm-chart)
2. [Remove all PVC's](https://archivedocs.stackstate.com/uninstall#remove-remaining-resources)
3. Install StackState again using the same configuration as before, on [Kubernetes](https://archivedocs.stackstate.com/install-stackstate/kubernetes_openshift/kubernetes_install#deploy-stackstate-with-helm) or [OpenShift](https://archivedocs.stackstate.com/install-stackstate/kubernetes_openshift/openshift_install#deploy-stackstate-with-helm).
