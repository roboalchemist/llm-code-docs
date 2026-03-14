# Source: https://docs.portainer.io/2.33-lts/whats-new.md

# Source: https://docs.portainer.io/sts/whats-new.md

# Source: https://docs.portainer.io/whats-new.md

# What's new in version 2.39

Portainer version 2.39 includes a number of new fixes and updates, bringing the changes from the previous STS releases into the LTS stream. For a full list of changes, please refer to our [release notes](https://docs.portainer.io/release-notes).

{% embed url="<https://www.youtube.com/watch?v=9vrzqMWHSq8>" %}

## Long Term Support (LTS)

2.39 is a Long Term Support, or "LTS", release of Portainer. LTS releases are intended to to be solid, tested, production-ready versions of Portainer, suitable for running in both testing and production environments. LTS releases generally do not have any additional features as compared to the previous STS release, but rather are a consolidation of all the new features and changes that have gone into the previous STS releases but with additional polishing and testing.

You can read more about our release principles in our [lifecycle policy](https://docs.portainer.io/start/lifecycle).

## New in this release

### Fleet Governance Policies  ![](https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/SVIkwsLgV0f8U86tTOQa/button_be.png)

With this release we’re introducing [Fleet Governance Policies](https://docs.portainer.io/admin/environments/policies) - a new way to govern container infrastructure at scale.

As organizations grow, it’s common to end up managing tens or even hundreds of clusters, each configured slightly differently, which quickly turns into an operational and security headache. Fleet Governance Policies help you define security, access, and configuration standards once, then automatically enforce them across your entire fleet, regardless of cloud, region, or deployment model. Policies stay continuously enforced, correct drift automatically, and apply instantly to new clusters as they’re onboarded. With prebuilt policy templates for production and development environments, it’s easier than ever to get started - and this is just the first step toward true fleet-wide cluster management in Portainer.

<figure><img src="https://2837857291-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxdTQRpMuktD2l0URtOJO%2Fuploads%2FQga9t4jHTmwdIEK6nE5g%2F2.39-policies-list.png?alt=media&#x26;token=91529b4d-a3a8-45fb-86b7-9fce595797f3" alt=""><figcaption></figcaption></figure>

We're really excited about where this will lead in the future - give it a try and let us know your feedback!

### Alerting graduates from experimental  ![](https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/SVIkwsLgV0f8U86tTOQa/button_be.png)

In earlier releases, we introduced [alerting](https://docs.portainer.io/user/observability/alerting) as an experimental feature, allowing administrators to configure alerts based on conditions such as environments going offline, failed backups, or high resource usage. Since then, we’ve refined and improved the feature, and in 2.39 alerting is now generally available. Administrators can enable alerting under **Observability** from the [Additional Functionality](https://docs.portainer.io/admin/settings/general#additional-functionality) section, making it easier to monitor environment health and react to issues without relying solely on external tooling.

<figure><img src="https://2837857291-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxdTQRpMuktD2l0URtOJO%2Fuploads%2Ft7fXCiH3fPFS5uPMjZFv%2F2.39-alerting-rules.png?alt=media&#x26;token=46ca6250-230d-4881-be43-f34e94f08575" alt=""><figcaption></figcaption></figure>

### Docker stack renaming  ![](https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/SVIkwsLgV0f8U86tTOQa/button_be.png) ![](https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/TQPpHSAY8u9AomqYL2Jv/button_ce.png)

You can now rename an existing Docker stack as part of the [Stack duplication or migration workflow](https://docs.portainer.io/user/docker/stacks/migrate). This makes it easier to reorganize or migrate stacks without needing to recreate them from scratch.

<figure><img src="https://2837857291-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxdTQRpMuktD2l0URtOJO%2Fuploads%2FP4QltuVvlBdOcYI5Nw99%2F2.39-stack-rename.png?alt=media&#x26;token=023c9c64-1385-4ad3-84f7-891c32089352" alt=""><figcaption></figcaption></figure>

### Shared Git credentials  ![](https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/SVIkwsLgV0f8U86tTOQa/button_be.png)

You can now create and manage shared Git credentials directly from the [Shared Credentials](https://docs.portainer.io/admin/settings/credentials) view. These credentials can be reused across deployments and templates by any admin-level user, without exposing the underlying secrets. Once added, shared Git credentials can be selected when setting up a deployment or when creating a custom Docker template, reducing duplication and simplifying Git-based workflows.

<figure><img src="https://2837857291-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxdTQRpMuktD2l0URtOJO%2Fuploads%2FA2QpQPRzEpy1WeZkiemI%2F2.39-shared-credentials-git.png?alt=media&#x26;token=698c5544-d441-4fe0-9aa8-411e6d3ee810" alt=""><figcaption></figcaption></figure>

### Registry management improvements  ![](https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/SVIkwsLgV0f8U86tTOQa/button_be.png)

As part of our ongoing transition from Angular to React, we’ve refactored the [registry repository management view](https://docs.portainer.io/admin/registries/browse). Managing repository tags is now significantly simpler. We’ve streamlined how tags are loaded, added, and removed, eliminating the need for manual batch loading and making registry management faster and more intuitive - especially when working with large repositories.

### Inspect Kubernetes CRDs and custom resources  ![](https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/SVIkwsLgV0f8U86tTOQa/button_be.png)

Administrators can now inspect [Kubernetes Custom Resource Definitions](https://docs.portainer.io/user/kubernetes/more-resources/custom-resources) and their associated custom resources directly from the Portainer UI. You can view resources as raw YAML or see a detailed summary equivalent to `kubectl describe`, making it easier to understand and troubleshoot custom resources without leaving Portainer.

<figure><img src="https://2837857291-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxdTQRpMuktD2l0URtOJO%2Fuploads%2Fh9FBN4vCYm1Bl9WsfYG4%2F2.39-kubernetes-custom-resources.png?alt=media&#x26;token=6fcaaa07-338f-42e9-b7b1-f5b90496be74" alt=""><figcaption></figcaption></figure>

### Node YAML editor  ![](https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/SVIkwsLgV0f8U86tTOQa/button_be.png) ![](https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/TQPpHSAY8u9AomqYL2Jv/button_ce.png)

We’ve added the ability to view node YAML directly from the [Node details](https://docs.portainer.io/user/kubernetes/cluster/details/node) view. For Portainer Business Edition users, this goes a step further - you can now apply changes to the node YAML directly from the UI, making it easier to inspect and manage node-level configuration without switching tools or contexts.

<figure><img src="https://2837857291-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxdTQRpMuktD2l0URtOJO%2Fuploads%2FgAMqCg1gz0A69QV06cBW%2F2.39-kubernetes-node-details-yaml.png?alt=media&#x26;token=fb7beda9-5c81-4bf9-a7e1-8d26d17cc6f9" alt=""><figcaption></figcaption></figure>

### Git-based Helm deployments  ![](https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/SVIkwsLgV0f8U86tTOQa/button_be.png)

Helm chart deployments can now be managed directly from Git. You can [deploy Helm charts from a Git repository](https://docs.portainer.io/user/kubernetes/applications/manifest/helm#git-repository), track whether a release is in sync with its source, and view Git details for deployed releases. Applications created from Git can also be updated by modifying the Git settings directly within the application view, bringing Helm workflows more closely in line with GitOps practices.

<figure><img src="https://2837857291-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxdTQRpMuktD2l0URtOJO%2Fuploads%2FKdc5y7MhJHM11MQOwfJ6%2F2.39-kubernetes-applications-add-helm-git.png?alt=media&#x26;token=822e5360-4150-4b73-b55c-060e6d0b0aea" alt=""><figcaption></figcaption></figure>

### Helm manifest preview  ![](https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/SVIkwsLgV0f8U86tTOQa/button_be.png) ![](https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/TQPpHSAY8u9AomqYL2Jv/button_ce.png)

When creating or upgrading a Helm chart, you’ll now see a [Manifest preview](https://docs.portainer.io/user/kubernetes/applications/inspect-helm#manifest) alongside the values YAML. This allows you to inspect exactly what Kubernetes resources will be applied before committing a deployment or upgrade, helping catch configuration issues earlier and making Helm-based workflows more transparent.

### Always clone option for Edge stacks  ![](https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/SVIkwsLgV0f8U86tTOQa/button_be.png)

For Edge stacks that use relative path volumes, there’s now an [Always clone](https://docs.portainer.io/user/edge/stacks/add#always-clone-git-repository) option. When enabled, Portainer will automatically pull the latest content from the Git repository during deployment, ensuring that Edge environments always receive the most up-to-date configuration and files.
