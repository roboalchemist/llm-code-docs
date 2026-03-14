# Portainer Documentation

Source: https://docs.portainer.io/llms-full.txt

---

# Welcome

Welcome to Portainer's official documentation site.

## About Portainer

**Portainer Community Edition (CE)** is our foundation. With over half a million regular users, CE is a powerful, open source toolset that allows you to easily build and manage containers in Docker, Docker Swarm, Kubernetes and Azure ACI.

**Portainer Business Edition (BE)** is our commercial offering. With features geared towards businesses and larger organizations such as [Role-Based Access Control](https://docs.portainer.io/admin/user/roles), [registry management](https://docs.portainer.io/admin/registries/browse), and [dedicated support](#getting-support), Portainer BE is a powerful toolset that allows you to easily build and manage containers in Docker, Docker Swarm, Kubernetes, Podman and Azure ACI.

{% hint style="info" %}
Portainer Business Edition requires a license key to install and use. If you don't currently have a license key, you can [request three nodes free](https://www.portainer.io/get-a-license) of Portainer Business Edition or [purchase a license](https://www.portainer.io/pricing).
{% endhint %}

Portainer hides the complexity of managing containers behind an easy-to-use UI. By removing the need to use the CLI, write YAML or understand manifests, Portainer makes deploying apps and troubleshooting problems so easy that anyone can do it.

Our team is here to help you on your journey. Community and five/three nodes free users can get assistance through our [community support channels](#community-edition-five-three-node-free-and-home-and-student-users), and paid Business customers through our [business support channels](#business-edition-customers).

## Documentation

We're working hard to ensure that our documentation keeps up with our ever-growing Portainer community. If you have a question we encourage you to start with the documentation (right here!). If you can't find what you're looking for, please raise a question in one of our [support channels](#getting-support).

For more detailed step-by-step guides to Portainer, we're building out the [Portainer Academy](https://academy.portainer.io) with more courses regularly.

{% hint style="info" %}
As an open source product we rely on users in our community to support one another by asking questions, engaging in discussions and sharing knowledge. Together with the documentation found on this site and our [YouTube channel](https://www.youtube.com/channel/UC7diMJcrULjDseq5yhSUZgg), we cover a lot of ground but there may be gaps.
{% endhint %}

## Getting support

### Community Edition, Five/Three Node Free and Home & Student Users

Community Edition, five/three nodes free and Home & Student users can get support through the following channels:

* **Ask our AI bot** by clicking the **Ask AI** button in the bottom right of this documentation site. Our AI chatbot pulls from a number of sources and is a great place to start when looking for help.
* **Ask questions** either in our [GitHub Discussions](https://github.com/orgs/portainer/discussions/categories/help) forum or the [community Slack channel](https://portainer.io/slack). Other platforms exist (Reddit, Discord, Stack Overflow) but we are less active in those spaces.
* **Log bugs** in [GitHub Issues](https://github.com/portainer/portainer/issues) so they can be properly managed.
* **Report any security vulnerabilities** by emailing <security@portainer.io> or by [opening a vulnerability report in GitHub](https://github.com/portainer/portainer/security/advisories/new) so the issue can be reviewed and addressed as quickly as possible.
* **Flag documentation issues** via our [GitHub documentation channel](https://github.com/portainer/portainer-docs/issues) (or start [contributing](https://docs.portainer.io/contribute/contribute) and make our documentation better!).

### Business Edition Customers

If you are a Professional or Enterprise tier Portainer Business Edition customer, you can log tickets directly with our team via [email](mailto:businesssupport@portainer.io) or filling out the [Request Support form](https://www.portainer.io/portainer-business-support). You can report a bug, ask a question, tell us about an issue with documentation, or request a feature. Tickets are checked and resolved by Portainer staff within the SLA.


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


# Release Notes

The following release notes are for the **Business Edition** of Portainer. For **Community Edition** release notes, refer to the [GitHub releases page](https://github.com/portainer/portainer/releases).

## Release 2.39.0 LTS

February 26, 2026

#### Known issues

* On Async Edge environments, an invalid update schedule date can be displayed when browsing a snapshot

**Known issues with Podman support**

* Auto onboarding a Podman environment defaults to “Standard” and not “Podman”
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

**Known issues with Talos clusters managed by Omni (BE only)**

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster

### New in this Release

* Fixed an issue preventing environment group changes for Kubernetes standard agents from the environment details view
* Addressed security vulnerability disclosure
* Updated form behavior to only show errors after the input has been touched/visited or submitted
* Improved HTTP response code handling via the Portainer API
* Added default alphabetical sorting to the namespace dropdown list
* Fixed a UI issue where the dropdown form elements were overlapping with the footer
* Updated styling of shared tabs used throughout Portainer
* Improved TLS initialization for custom registries
* Fixed a memory leak in kubectl delete
* Fixed an issue where a “”Release: not found” error was presented when installing a Traefik ingress
* Fixed an issue when editing an environment that could inadvertently remove unix:// from URLs
* Reordered the agent options in the “Add Environment” interface
* Fixed an issue where Portainer was unable to pull from a private registry with a port in the URL
* Fixed an issue where a webhook was missing during the initial deployment
* Fixed an issue where the API response code from /docker/containers/create was returning 200 instead of 201
* Improved visibility of the "New version available" alert in light mode
* Upgraded package versions to mitigate potential frontend vulnerabilities
* Associated environments in a group will now only be saved when submitting the form
* Updated the documentation link supplied in the Portainer logs when a user tries to start Portainer BE with a CE database
* Fixed a 500 issue when loading Docker in the dashboard
* Fixed a problem with GitOps removing containers when image pull fails
* Fixed incorrect transaction usage around webhooks
* Fixed incorrect transaction usage when deleting endpoints
* Moved Fleet Governance Policies out of experimental, standardizing naming and presentation in-app
* Fixed a formatting issue where backup download error messages were displaying as \[object

ArrayBuffer] instead of human-readable text

* Fixed an error when creating a new environment group
* Fixed an issue where Podman environments were appearing in auto onboarding as Docker
* Moved “Policy based management” from Additional functionality to “Policies” within the Environment-related menu
* Updated misleading license overuse error messages
* Improved styling for the policy views
* Fixed dead-ends when creating policies on a fresh Portainer instance
* Removed “recommended” sentence from automatic patch updates
* Improved policy status performance
* Added a read only policy view for Docker environments
* Fixed an issue with read only policy view for regular users
* Stabilized the Policy Status states on the attachment section of the policy detail page
* Fixed an issue that could cause namespace errors when a Registry policy was applied
* Updated behavior for the Unassigned group within the Environment Groups list page
* Improved updating Edge client policy status state
* Set policy default overcommit to enabled for Kubernetes environments
* Fixed an issue with policy selection when there are more than 100 environments
* Fixed a policy status update edge case issue
* Fixed an issue where pod security constraints were not being properly created when policies were associated with an environment group
* Fixed an issue where the docker security policy with no rules prevents container creation for users
* Fixed incorrect policy plural in copy
* Ensured RBAC policies properly override environment and group level RBAC settings
* Fixed pagination issues in policy groups with large numbers of endpoints
* Improved policy status performance
* Updated security constraints port range to be visually wider
* Fixed an issue where some users were not able to add a Team to a Namespace after the 2.33.3 fix&#x20;
* Fixed incorrect enabled disabled wording in Docker read only policy view
* Fixed inconsistent styling of the notice about settings being managed by a policy
* Fixed a data race in the alert manager
* Fixed a data race in the Omni service
* Fixed a deadlock in the auto onboarding code
* Fixed a timing attack in hash comparisons
* Fixed data races in the token cache manager
* Fixed improper logging in the Omni service
* Fixed incorrect transaction usage in the Pending Actions service
* Added the ability to bulk add existing environments to an environment group
* Removed the retry button from policy actions
* Resolved the following CVEs:
  * CVE-2025-61726
  * CVE-2025-68121
  * GO-2026-4337
  * CVE-2025-15467

## Release 2.38.1 STS

February 13, 2026

#### Known issues

* On Async Edge environments, an invalid update schedule date can be displayed when browsing a snapshot

**Known issues with Podman support**

* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

**Known issues with Talos clusters managed by Omni (BE only)**

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster

### New in this Release

* Fixed an issue around changing an environment group for Kubernetes standard agent within the environment details view
* Fixed an issue where local environments using Docker would have their protocol removed
* Improved the namespace dropdown list to be sorted alphabetically by default
* Fixed an issue where environment changes were applied immediately instead of waiting for the Update group action
* Fixed an issue where Pod Security Constraints related policies were not correctly created
* Fixed an issue where policy selection was blocked when managing more than 100 environments and a supported environment was not detected
* Fixed an issue where resource overcommit was not enabled by default in the setup policy
* Worked on ensuring an RBAC policy will override the environment / group level RBAC settings
* Improved validation to ensure policy name is unique
* Improved the UX for policy status updates
* Re-added Policy based management under environment related menu
* Removed retry button from policy attachments table, replaced it with a timestamp of when it was last attempted to install
* Fixed an issue where a permissive Docker security policy was restricting standard users from managing containers
* Fixed an issue where standard users were seeing errors when viewing the policies applied to the Kubernetes environment they were in
* Resolved the following CVEs:
  * CVE-2025-61726
  * CVE-2025-61728
  * CVE-2025-61730

## Release 2.38.0 STS

January 29, 2026

#### Known issues

* On Async Edge environments, an invalid update schedule date can be displayed when browsing a snapshot

**Known issues with Policy Based Management (BE only)**

* When creating a Kubernetes Security Policy, the security setting for 'Restrict Proc Mount types' does not allow you to select Allowed Proc Mount types as it should
* The Kubernetes setup policy currently defaults to resource over-commit off. This diverges from the default Kubernetes over-commit setting. When creating a Kubernetes setup policy consider toggling resource over-commit on to match the Kubernetes default, otherwise you may experience an impact on existing workloads that rely on resource over-commit. In a future release we will adjust the policy default to match the Kubernetes default
* Currently, RBAC policies do not override environment or group-level settings, as they create non-conflicting role bindings. This may result in users retaining higher privileges (e.g. Environment Administrator) even when a policy is applied to restrict them to a Standard User role

**Known issues with Podman support**

* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

**Known issues with Talos clusters managed by Omni (BE only)**

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster

### New in this Release

* Changed [Policy Based Management](https://docs.portainer.io/admin/environments/policies) from experimental to beta, to indicate that it is ready for you to test against your environments
* Fixed an issue where starting Stack is failed when the private image referenced by the stack was removed from the environment
* Fixed an issue where deploying a Stack in Kubernetes caused a memory leak
* Fixed a UI issue when updating edge stacks
* Changed the Docker security settings to safer default values
* Fixed a panic in Edge Group creation
* Fixed quote handling in TLS CLI flags
* Fixed error in GitOps while updating Stacks
* Fixed a problem that would cause for the Containers page to not load
* Bumped up the max Docker API version in the proxy
* Fixed a problem while duplicating/editing containers related to persistent MAC addresses
* Added correct propagation of Docker error messages back to the frontend
* Added missing validations for Swarm environments security settings
* Optimized server allocations for a faster startup
* Fixed GO-2025-3460
* Upgraded to Compose v2.40.3 to fix a panic
* Fixed a problem in config removal
* Upgraded Git library to fix compatibility problem with gitee
* Removed all the Matomo code to no longer collect user statistics
* Removed confusing Podman log message in Docker environments
* Replaced [gopkg.in/yaml.v3](http://gopkg.in/yaml.v3) with [go.yaml.in/yaml/v3](http://go.yaml.in/yaml/v3)&#x20;
* Ensured the surfacing of Edge Stack file not found errors to the UI
* Changed the code to avoid creating updater networks
* Fixed registry selection recall for Stacks pages
* Fixed a nil pointer dereference error in FilterEndpoints()
* Fixed a nil pointer dereference error in deleteEndpointGroup()
* Fixed a nil pointer dereference error in CopyPath()
* Improved visibility on proxy errors
* Fixed a problem while renaming stacks on Swarm&#x20;
* Fixed a problem that could cause encrypting an existing Portainer database to fail
* Improved the Azure Container Instance (ACI) experience with a new environment variables section in the creation form and a corresponding table in the instance view
* Updated the Portainer logo and favicon throughout the application to the new branding
* Upgraded the golang/stdlib to version 1.24.11 to the following CVEs in the Portainer agent:
  * CVE-2025-61729
  * CVE-2025-61727
  * CVE-2025-47914
* Fixed an issue where Web Editor based Kubernetes app deployment ignores the selected namespace
* Fixed an issue where Edit/Upgrade buttons not functioning on Helm chart details page
* Fixed an issue where the docker-compose file was excluded for certain Git repository structures during Edge Stack deployment when Git Edge configuration was enabled, resulting in an “EntryFileName not found in DirEntries” error
* Fixed an issue where the Async Edge environment status could occasionally be cleared during Edge Stack deployment, causing the Edge Stack progress indicator to become stuck
* Enforced Async Snapshot data filtering by user role
* Fixed the Docker snapshot diff check in the Async Agent
* Fixed a problem in the Async Edge Config updates that would not let the previous files to be removed
* Added support for S3 backups via IRSA in EKS
* Fixed a problem with S3 backups and trailing slashes
* Added input validation to the `rollbackTo` query parameter
* Improved the overall experience of the Fleet management feature.
* Fixed an issue where the number of environments displayed in the policy view are capped at 99.&#x20;
* Fixed an issue where the 'Allowed proc mount types' was missing from the policy screen.
* Fixed an issue where Namespace access table remains empty despite user additions.
* Improved the overall policy status filter.
* Fixed an issue where policy setup view incorrectly hides policy types.
* Improved the policy attachments to allow all environment groups as options.&#x20;
* Improved stability of Kubernetes RBAC resources being applied and restored using a policy.
* Improved the policy feature with a status field to display the number of applied environments efficiently.
* Fixed an issue where incorrect environment group policy status may be displayed.
* Improved the environment summary view to contain list of associated policies.
* Fixed an issue where detaching a policy did not restore to the previous state.&#x20;
* Improved the Policy creation experience to include sticky header and footers.
* Fixed an issue where policy view tries to open tunnel to async edge environment.
* Improved the policy creation to show the full preview of what will happen when a policy is applied.

## Release 2.37.0 STS

December 11, 2025

#### Known issues <a href="#known-issues" id="known-issues"></a>

* On Async Edge environments, an invalid update schedule date can be displayed when browsing a snapshot

**Known issues with Fleet Management (BE only)**

* The Policy Details screen displays at most 99 environments. However, the policy is applied to all environments associated with the selected environment groups
* When creating a Kubernetes Security Policy, the security setting for 'Restrict Proc Mount types' does not allow you to select Allowed Proc Mount types as it should

**Known issues with Podman support**

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

**Known issues with Talos clusters managed by Omni**

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster

### New in this Release <a href="#new-in-this-release" id="new-in-this-release"></a>

* Introduced [Fleetwide Policies](https://docs.portainer.io/admin/environments/policies), a new feature allowing administrators to centrally configure reusable settings that are automatically applied and across all environments in a group. **This feature is experimental**
* Fixed an issue where a standard stack could not pull private images from a private registry during a GitOps update (polling/webhook) when "Re-pull image" was enabled and a relative path was configured
* Fixed an issue where the Update the Stack button was disabled when editing a standard stack deployed via the Web Editor
* Fixed Service view display for Docker Swarm
* Fixed a regression in the stack updates view
* Fixed the disabled Save button for GitHub Credentials Authentication
* Fixed the undesired regeneration of the webhook IDs
* Fixed the disabled Update stack button
* Fixed missing Compose configs for stacks
* Removed the environment names from error responses
* Fixed Edge Job logs API documentation
* Increased the validations in the Edge Jobs logs API
* Fixed an improper display of the editor search bar over a confirmation dialog
* Changed the Volumes Browser to prevent it from adding `.txt` extension when downloading files
* Removed the option to access host volumes for users that are not allowed to do it
* Added a check to avoid an empty EdgeID when polling in async mode
* Added a check to reject async environments in the Edge Jobs logs API
* Fixed a data-race related with alerting

## Release 2.33.5 LTS <a href="#release-2.33.4-lts" id="release-2.33.4-lts"></a>

November 27, 2025

#### Known issues <a href="#known-issues" id="known-issues"></a>

* On Async Edge environments, an invalid update schedule date can be displayed when browsing a snapshot

**Known issues with Podman support**

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

**Known issues with Talos clusters managed by Omni**

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

#### New in this Release <a href="#new-in-this-release" id="new-in-this-release"></a>

* Added support for Docker v29

**Breaking change**

* Removed the optional raw snapshot response from some endpoint requests

## Release 2.36.0 STS

November 27, 2025

### Known issues

* On Async Edge environments, an invalid update schedule date can be displayed when browsing a snapshot

**Known issues with Podman support**

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

**Known issues with Talos clusters managed by Omni**

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

### New in this Release

* Fixed an issue where Edge Stack GitOps Force Redeployment was not working
* Fixed an issue where Edge Stacks deployed via Git Repository were not redeployed when a new commit was pushed and the GitOps update was triggered
* Hid the Git credentials and PAT when the stored ones are being used
* Added resiliency for power interruptions in the Async Edge Agent
* Added Users and Environment filters for the Activity Logs
* Added support for Helm Chart folders in the root Git directory
* Fixed a nil pointer dereference when adding team accesses to namespaces in Kubernetes environments
* Fixed Edge Stacks list inconsistent counts
* Fixed the Edge Stack relations reconciliation when updating endpoint groups
* Added the support for Kubernetes CRDs&#x20;
* Fixed local development build scripts for community contributors with Apple M series chips
* Improved ECR session management in the Agent
* Added support for Docker v29
* Improved the consistency for GitOps across different scenarios
* Fixed the External label for Kubernetes environments
* Fixed namespace selection in the registry access page
* Improve the registry credential handling in compose files
* Fixed CVEs in the password reset helper
* Fixed the Prune services toggle for Swarm
* Added a `--data-path` flag to the password reset helper
* Fixed oversized custom icons in the templates view
* Added an access token connection test for DockerHub before registry creation
* Fixed the ability to uncheck filters after deleting filtered containers in the Container list view
* Fixed the Insecure toggle for custom registries
* Added the ability to rename Stacks
* Fixed the date picker calendar to display the 7 days of the week without overflowing
* Updated the privacy policy link
* Added auto-onboarding script for Podman
* Improved to display 'title' or 'tooltip' in all places that text is truncated in the UI
* Fixed the navigation bar to display Portainer correctly
* Fixed incorrect command syntax for Windows Edge agent deployment instructions
* Fixed Helm install docs link
* Fixed order of environment types
* Resolved the following CVEs:
  * CVE-2025-62725
  * CVE-2024-25621
  * CVE-2025-47913
  * CVE-2025-47906
  * CVE-2025-47910
  * CVE-2025-47907
  * CVE-2025-47912
  * CVE-2025-58183
  * CVE-2025-58185
  * CVE-2025-58186
  * CVE-2025-58187
  * CVE-2025-58188
  * CVE-2025-58189
  * CVE-2025-61723
  * CVE-2025-61724
  * CVE-2025-61725
  * CVE-2020-8911
  * CVE-2020-8912

### Deprecated and removed features

* Deprecated OpenAMT support

## Release 2.33.4 LTS <a href="#release-2.33.4-lts" id="release-2.33.4-lts"></a>

November 20, 2025

### Known issues <a href="#known-issues" id="known-issues"></a>

* On Async Edge environments, an invalid update schedule date can be displayed when browsing a snapshot

**Known issues with Podman support**

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

**Known issues with Talos clusters managed by Omni**

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

### New in this Release

* Fixed an issue of broken manual stack force deployment
* Fixed an issue that caused the calendar widget to render incorrectly
* Resolved the following CVEs:
  * CVE-2024-25621
  * CVE-2025-47913
  * CVE-2025-47906
  * CVE-2025-47910
  * CVE-2025-47907
  * CVE-2025-47912
  * CVE-2025-58183
  * CVE-2025-58185
  * CVE-2025-58186
  * CVE-2025-58187
  * CVE-2025-58188
  * CVE-2025-58189
  * CVE-2025-61723
  * CVE-2025-61724
  * CVE-2025-61725

## Release 2.33.3 LTS <a href="#release-2.33.3-lts" id="release-2.33.3-lts"></a>

October 30, 2025

### Known issues <a href="#known-issues-1" id="known-issues-1"></a>

* On Async Edge environments, an invalid update schedule date can be displayed when browsing a snapshot

**Known issues with Podman support**

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

**Known issues with Talos clusters managed by Omni**

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

### New in this Release

* Improved stability by attempting to compact using a read-only database
* Fixed an issue where WebSocket upgrade failed with Portainer generated `kubeconfig`
* Fixed an issue where a memory leak occurred during Kubernetes stack auto redeployment
* Fixed missing dependency versions displayed in the popup
* Fixed an issue where adding a team access to a namespace threw a panic error
* Fixed typos in Content-Security-Policy
* Improved the Activity Logs Date and Time filter
* Resolved CVE-2025-62725

## Release 2.35.0 STS

October 16, 2025

### Known issues

* On Async Edge environments, an invalid update schedule date can be displayed when browsing a snapshot

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### Known issues with Talos clusters managed by Omni

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.&#x20;

### New in this Release

* Fixed a bug where the Edit Ingress page wasn’t displaying updated information immediately after making an update
* Fixed an issue where GitOps webhook URLs could be reused
* Fixed a data race issue caused by the Kubernetes client
* Fixed an issue that caused a memory leak when redeploying a Kubernetes stack
* Fixed an issue where the environment status filter did not properly handle the "Failed" state when used with Edge Stacks
* Added support for IPV6 network configuration for IPvlan Docker networks
* Added a new command flag `--compact-db` to allow database compaction on startup
* Fixed typos in Content-Security-Policy
* Added support for Helm GitOps allowing automatic upgrades based on changes to a Helm chart and/or Helm override files in a Git repository
* Fixed an issue with access control when users attempted to view resources in namespaces they don’t have access to
* Fixed an issue where WebSocket connections were not forwarded correctly to the Kubernetes API
* Fixed missing dependency versions in popup
* Fixed an error when deleting the last tag in a Github registry repository
* Added a toggle "Always clone Git repository" under the Edge Stack relative path setting to enforce cloning the latest Git repository during each redeployment
* Fixed an issue where the frontend proxied the registry tag list request with an encoded URL, which could cause a 404 error in certain Portainer server setups when listing registry tags
* Added a new automatic patch update feature (disabled by default) to ensure Portainer stays secure and consistent without manual intervention. This mechanism automatically applies patch releases (e.g. *x.x.n*), reducing version fragmentation and improving supportability.
* Added a help tooltip to the git Authorization type field
* Fixed an error where updating Portainer in Swarm would lead to portainer-updater being unable to execute the update
* Resolved the following CVEs:&#x20;
  * CVE-2025-7783
  * CVE-2022-37601
  * CVE-2025-22868

### Deprecated and removed features

* None

## Release 2.33.2 LTS <a href="#release-2.33.2-lts" id="release-2.33.2-lts"></a>

September 25, 2025

### Known issues <a href="#known-issues-2" id="known-issues-2"></a>

* On Async Edge environments an invalid update schedule date can be displayed when browsing a snapshot

**Known issues with Podman support**

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

**Known issues with Talos clusters managed by Omni**

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

### New in this Release

* Fixed an issue where Standard Users could not join a container to a network
* Fixed an issue where the database encryption secret was incorrectly set
* Fixed an issue with Kubernetes Access Control
* Fixed an issue where GitOps webhook URLs could be reused
* Improved Helm repository validation to align with the behavior of the CLI
* Fixed an issue where the environment status filter did not properly handle the "Failed" state when used with Edge Stacks
* Fixed an issue where registry list API was returning back passwords
* Fixed a data race issue caused by the Kubernetes client
* Fixed an issue where the GitOps interval could be set to less than one minute
* Fixed an issue where the Edge stack for GitOps updates was not correctly saved to the edge agent’s stack folder
* Fixed an issue where SMTP authentication settings were not properly applied to the internal Alertmanager configuration file
* Fixed an issue where false-positive alerts were being triggered by the Backup alert rule
* Fixed an issue where Activity Log exports were limited to 2,000 items and search functionality was not working correctly
* Fixed an issue where invalid Docker Swarm warning shows up in Docker standalone environment
* Fixed an issue where Helm values fails to load when the repo contains mixed media types
* Bumped the following NPM dependencies to resolve vulnerabilities
  * axios → 1.7
  * coverage-v8 → \~2.1.9
  * vitest → 2.1.9
* Resolved the following CVEs:
  * CVE-2025-4676
  * CVE-2025-47907

#### Deprecated and removed features <a href="#deprecated-and-removed-features" id="deprecated-and-removed-features"></a>

* We have deprecated the `--sslcert` and `--sslkey` CLI options in favor of the `--tlscert` and `--tlskey` options respectively, and will be removing the `--sslcert` and `--sslkey` options in a future release.

## Release 2.34.0 STS

September 18, 2025

### Known issues

* On Async Edge environments, an invalid update schedule date can be displayed when browsing a snapshot

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### Known issues with Talos clusters managed by Omni

* It is not currently possible to upgrade either the Kubernetes or Talos versions under the Cluster settings page
* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

### New in this release

* Increased Content-Security-Policy restrictions
* Added enforcement of a minimum polling interval value for GitOps
* Fixed environment type detection for the image status indicator
* Fixed an access control bug in Custom Templates
* Fixed inaccurate display of healthy containers count in environment listing
* Implemented higher priority for interactive database transactions over background processes like edge agent polling
* Fixed a data race in the job scheduler
* Removed the password from the response of the registry update request
* Fixed a problem that prevented the deployment of stacks from private repositories when Git credentials were entered manually
* Fixed a failure when deploying a stack that referred to multiple private registries under the same provider
* Fixed the display of Edge Groups when the number of environments is high
* Fixed the network connection to containers by Standard Users
* Removed `mingit` binary from Windows images
* Added `windows-2025` builds of the Portainer image
* Fixed an inconsistency while adding new edge environments
* Fixed Helm repository validation to match the library behavior
* Improved the view for editing registry repositories
* Fixed tab swapping in the Node details view
* Fixed inconsistencies in the display of Namespace resource limits
* Fixed Helm failures when the repository contains mixed media types
* Fixed the browsing of custom registries when using public TLS certificates
* Added support for shared credentials for Git operations
* Fixed the resource request slider
* Fixed the default DB encryption secret path
* Changed the filename of the downloaded async edge stacks logs to include the date and environment name
* Moved the Observability Alerting feature out of experimental:
  * Fixed a panic error caused by attempting to re-enable the internal alert manager after it had been disabled (`duplicate metrics collector registration attempted`)
  * Fixed an issue where disabling the notification channel toggle did not apply correctly
  * Fixed a false-positive condition where a backup alert would fire even when the backup completed successfully
  * Fixed the Environment Down alert rule not triggering correctly for Edge agents

### Deprecated and removed features

* None

## Release 2.33.1 LTS

August 27, 2025

### Known issues

* On Async Edge environments an invalid update schedule date can be displayed when browsing a snapshot

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### Known issues with Talos clusters managed by Omni

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

### New in this Release

* Fixed an issue where the environment status was not updating in a timely fashion for Standard Edge Agent
* Fixed an issue where the `--tlscert` and `--tlskey` CLI options did not work unless `--sslcert` and `--sslkey` were also provided
* Fixed an issue where Edge Stacks with GitOps enabled were not being updated correctly
* Fixed an issue where the container engine defaulted to Docker when associating the first Kubernetes environment
* Fixed an issue preventing updates from being scheduled when another update was already in progress
* Fixed an issue with upgrading Kubernetes version or Talos version for Omni managed environments
* Removed the requirement for authentication when using the SMTP alert notification type
* Fixed an issue where users were unable to deploy a stack from a private repository when Git credentials were entered manually
* Resolved the following CVEs:
  * CVE-2025-22871
  * CVE-2025-22868
  * CVE-2025-22869
  * CVE-2025-4673
  * CVE-2024-45341
  * CVE-2024-45336
  * CVE-2025-0913
  * CVE-2024-45338
  * CVE-2025-22872
  * CVE-2024-40635
  * CVE-2025-22870
  * CVE-2025-22866
  * CVE-2025-54410
  * GHSA-2464-8j7c-4cjm

## Release 2.33.0 LTS

August 20, 2025

### Known issues

* On Async Edge environments an invalid update schedule date can be displayed when browsing a snapshot

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### Known issues with Talos clusters managed by Omni

* It is not currently possible to upgrade either the Kubernetes or Talos versions under the Cluster settings page
* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

### New in this release

* Improved the dropdown behavior when there are more than 1000 items
* Improved the YAML web editor
* Introduced the ability to add bearer token authentication support for Bitbucket Repositories
* Fixed an issue where duplicated events could be created by pending events
* Moved the kubectl shell feature to a pop-up window
* Improved performance by optimizing Edge Group endpoint relations
* Added Permissions-Policy header to improve security
* Fixed an issue where the log viewer could crash when rendering long multiline logs
* Fixed an issue where Portainer generated kubeconfig causes `kubectl exec` to fail
* Fixed an issue with custom logos not being aligned correctly
* Fixed an issue where Helm preview (dry run) errors could block some valid Helm installs
* Fixed an issue where Kubernetes environment stats were missing in the Home View
* Fixed an issue where the environment count could overlap with the other UI components in the Edge Configuration list view
* Fixed an issue with links to Secrets when there is a ConfigMap and a Secret with the same names
* Fixed an issue where edge stacks could show a status of unavailable when they were properly deployed
* Fixed an issue where Helm applications with the same workload name would get combined in the Applications page
* Fixed an issue where a standard user with access to a Helm registry could not load OCI Helm charts
* Fixed Swagger documentation
* Optimized the async edge devices snapshot processing
* Optimized the async edge device auto-onboarding process
* Improved the Kubernetes resource settings allow setting a request and no limit
* Improved server-side snapshot processing performance by filtering out noisy Docker snapshot fields for older agent versions
* Fixed an issue where Portainer failed to deploy a stack that refers to multiple private registries under the same provider
* Fixed an issue where Portainer was unable to get Helm charts (repos) from custom Helm registries with a custom TLS configuration
* Fixed an issue where the Edge Jobs page would crash at scale
* Fixed an issue where the Update and Rollback page could become unresponsive at scale
* Fixed an issue where deleting a user did not create a corresponding pending action
* Fixed an issue where a Git deployed application with a token reverted back to the basic auth type
* Fixed an issue where the edge group filter failed to fetch environments in the waiting room
* Fixed an issue where a failed async remote update could cause issues
* Fixed the time format to handle the timeout properly for the remote update
* Fixed an issue where an edge job cannot be deleted if the related endpoint is missing
* Resolved the following CVEs:
  * CVE-2025-55198
  * CVE-2025-55199
  * CVE-2025-54388
  * CVE-2020-8552
  * CVE-2025-8556
  * GHSA-fv92-fjc5-jj9h

### Deprecated and removed features

* The OpenAI integration experimental feature has been removed in this release.
* As previously announced, support for the Docker manifest list format (`application/vnd.docker.distribution.manifest.list.v2+json`) has been removed. All published container images now exclusively use the OCI image index format (`application/vnd.oci.image.index.v1+json`). Tooling that relied on Docker-specific media types should be updated to ensure compatibility with OCI-compliant image indexes.

## Release 2.32.0 STS

July 24, 2025

### Known issues <a href="#known-issues" id="known-issues"></a>

#### **Known issues with Podman support**

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### **Known issues with Talos clusters managed by Omni**

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration and does not affect authentication for any other functionality in the cluster.

### New in this release

* Application rebranding
  * Updated Message of the day application banner to reflect new branding
  * Updated background colors across the application
  * Updated dark/light mode button colors
  * Updated dark/light mode colors in the nav side bar
  * Updated the logo for both narrow and wide sidebars and login screens
* Added a `--trusted-origins` flag to allow for CSRF protection in more complex setups
* Fixed error handling when creating a new Kubernetes application
* Updated the Docker binary version from v27.5.1 to v28.1.0
* Improved frontend services datatable tests
* Fixed an issue where the Kubernetes client cache was not cleared and created correctly per user
* Fixed an issue where Kubernetes namespace access changes were not reflected for API users after sign-in
* Fixed an issue where edge Kubernetes stacks were not deploying
* Fixed an issue where v3 templates were not accepting empty values in the form
* Fixed an issue where the image indicator was not displaying in swarm stacks and services page for private registries
* Replaced deprecated methods pkix.CertificateList, issuer.CheckCRLSignature, and x509.ParseCRL
* Enabled CSP by default
* Added the display of an event warning count when viewing Kubernetes resource lists
* Fixed a UI issue where table pagination was not working for edge environments
* Added basic support for viewing Kubernetes CRDs of type cloudNativePG
* Fixed an issue that prevented the use of and loading of values.yaml for Helm charts from custom registries
* Improved error handling for edge stack status when edge agent added to group
* Restructured user authorized environments for scaling and performance improvements
* UI Improvements to edge agent updates views (update and rollback)
  * New environments view for edge agents updates
  * New schedules view
* Migrated the Registries Repository page to React
* Deploying and upgrading a Helm application from an OCI Registry
  * Improved Helm chart references on install and upgrade
* Fixed an issue where the remote updater would show as successful when an unavailable updater image tag is used and the agent version remains unchanged
* Fixed an invalid date issue present when updating agents created from older versions
* Added a filter to exclude untrusted environments from edge agent updates so environments in the waiting room are not added
* Fixed an issue where the pod console was not working for users with Operator and Namespace Operator roles
* Moved endpoint relation configuration to environment creation to simplify endpoint relation workflow
* Added the display of the image creation date in the registry repository page
* Removed the display of the SHA-1 fingerprint when viewing a certificate
* Added Alerting functionality as an experimental feature
* Resolved the following CVEs:
  * CVE-2025-53547
  * CVE-2025-22874
  * CVE-2025-22781
  * CVE-2025-22871

### Deprecated and removed features

* The OpenAI integration experimental feature is deprecated in this release and will be removed in 2.33 LTS.
* As previously announced, support for the Docker manifest list format (`application/vnd.docker.distribution.manifest.list.v2+json`) has been removed. All published container images now exclusively use the OCI image index format (`application/vnd.oci.image.index.v1+json`). Tooling that relied on Docker-specific media types should be updated to ensure compatibility with OCI-compliant image indexes.

## Release 2.31.3 STS

July 3, 2025

### Known issues <a href="#known-issues" id="known-issues"></a>

#### **Known issues with Podman support**

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### **Known issues with Talos clusters managed by Omni**

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration and does not affect authentication for any other functionality in the cluster.

### Changes <a href="#changes" id="changes"></a>

* Added the `--trusted-origins` CLI option and `TRUSTED_ORIGINS` environment variable to specify (in a comma-separated list) the domain(s) used to access Portainer when it is behind a reverse proxy. Use this option if Portainer is behind a reverse proxy and you are getting "Origin invalid" errors.

## Release 2.27.9 LTS

July 2, 2025

### Known issues <a href="#known-issues" id="known-issues"></a>

#### **Known issues with Podman support**

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### **Known issues with Talos clusters managed by Omni**

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration and does not affect authentication for any other functionality in the cluster.

### Changes <a href="#changes" id="changes"></a>

* Added the `--trusted-origins` CLI option and `TRUSTED_ORIGINS` environment variable to specify (in a comma-separated list) the domain(s) used to access Portainer when it is behind a reverse proxy. Use this option if Portainer is behind a reverse proxy and you are getting "Origin invalid" errors.

## Release 2.31.2 <a href="#release-2.27.7" id="release-2.27.7"></a>

June 26, 2025

### Known issues

* Users with Portainer deployed behind a reverse proxy may encounter "Origin invalid" issues under some configurations. We recommend updating to 2.31.3 which provides a workaround to this issue.

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### Known issues with Talos clusters managed by Omni

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

### Changes

* Fixed an issue that prevented the use of and loading of values.yaml for Helm charts from custom registries

## Release 2.27.8 <a href="#release-2.27.7" id="release-2.27.7"></a>

June 25, 2025

### Known issues <a href="#known-issues" id="known-issues"></a>

* Users with Portainer deployed behind a reverse proxy may encounter "Origin invalid" issues under some configurations. We recommend updating to 2.27.9 which provides a workaround to this issue.

#### **Known issues with Podman support**

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### **Known issues with Talos clusters managed by Omni**

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration and does not affect authentication for any other functionality in the cluster.

### Changes <a href="#changes" id="changes"></a>

* Fixed an issue where the Kubernetes client cache was not cleared and created correctly per user
* Fixed an issue where Kubernetes namespace access changes were not reflected for API users after sign-in

## Release 2.31.1 <a href="#release-2.27.7" id="release-2.27.7"></a>

June 19, 2025

### Known issues

* Users with Portainer deployed behind a reverse proxy may encounter "Origin invalid" issues under some configurations. We recommend updating to 2.31.3 which provides a workaround to this issue.

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### Known issues with Talos clusters managed by Omni

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

### Changes

* Added basic support for viewing Kubernetes CRDs of type cloudNativePG

## Release 2.27.7 <a href="#release-2.27.7" id="release-2.27.7"></a>

June 17, 2025

### Known issues <a href="#known-issues" id="known-issues"></a>

* Users with Portainer deployed behind a reverse proxy may encounter "Origin invalid" issues under some configurations. We recommend updating to 2.27.9 which provides a workaround to this issue.

#### **Known issues with Podman support**

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### **Known issues with Talos clusters managed by Omni**

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration and does not affect authentication for any other functionality in the cluster.

### Changes <a href="#changes" id="changes"></a>

* Resolved the following CVEs:
  * CVE-2025-22871
  * CVE-2025-22874
  * CVE-2025-49593

## Release 2.31.0

June 12, 2025

### Known issues

* Users with Portainer deployed behind a reverse proxy may encounter "Origin invalid" issues under some configurations. We recommend updating to 2.31.3 which provides a workaround to this issue.

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### Known issues with Talos clusters managed by Omni

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

### New in this release

* Made improvements to the Helm feature:
  * Replaced Helm logo with information about registry URL
  * Improved Helm install view to be able to select a desired chart version
  * Added registry drop down to filter Helm charts
  * Now displays more than 10 workloads under Helm expand in the Applications view
  * Improved performance for getting available versions for a release
* Added allow list of headers to send when proxying a request outside Portainer, all others are removed
* For Kubernetes config map and secret operations, make the request via the Portainer server and not directly from the browser
* Fixed an issue that caused Edge Agent mTLS certificates to be rejected incorrectly due to DNS name
* Fixed an error that could occur when associating edge agents that did not already have an edge group configured
* Fixed an error when viewing the results of an edge job with a large number of target environments
* Fixed a problem that could prevent removing an async environment from an edge group
* Improved mTLS performance by removing redundant validation step
* Upgraded dependencies to fix issue that caused Podman to redeploy all services when only one is changed
* Adjusted the behavior of the async agent to not waste effort sending compressed payloads when the compressed version is not smaller
* Added automated tests for edge update schedule
* Fixed an issue where Portainer would crash on snapshot with `--device nvidia.com/gpu=all` set
* Fixed an issue that caused the portainer-updater to get stuck in a retry loop when it failed to start the new image
* Fixed an issue where redeploying an Edge stack with a GitOps Edge configuration removed files and folders in the mounted directory
* Added a confirmation dialog with the option to re-pull the image and redeploy when using the Git repository method for Edge stack redeployment

### Deprecated and removed features

* We are transitioning our published container images to use the **OCI image index format** (`application/vnd.oci.image.index.v1+json`) instead of the traditional Docker manifest list format (`application/vnd.docker.distribution.manifest.list.v2+json`) in a future release. Any tooling relying on Docker-specific media types should be checked for compatibility, although most OCI-compliant tools already support this format.
* We are deprecating our image builds of Portainer Server CE and BE for Windows Server platform from this release. The Portainer Agent images will still be built for Windows Server - this only affects the Portainer Server container images.

## Release 2.30.1

May 20, 2025

### Known issues

* Users with Portainer deployed behind a reverse proxy may encounter "Origin invalid" issues under some configurations. We recommend updating to 2.31.3 which provides a workaround to this issue.

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### Known issues with Talos clusters managed by Omni

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

### Changes

* Fixed an issue where the server rejected agent connections if the agent mTLS certificate DNS name did not match the Portainer API server URL in Edge compute settings.

## Release 2.30.0

May 15, 2025

### Known issues

* Users with Portainer deployed behind a reverse proxy may encounter "Origin invalid" issues under some configurations. We recommend updating to 2.31.3 which provides a workaround to this issue.

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### Known issues with Talos clusters managed by Omni

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

### New in this release

* Made improvements to the Helm feature:
  * Added the ability to upgrade, rollback, and uninstall a Helm chart
  * Added the ability to display if a new chart version exists
  * Added the ability to show differentials with previous revision
  * Added Helm revision panel
  * Added Events tab
* Replaced the `kubectl` binary with the upstream SDK
* Added support for passing `PORTAINER_` prefixed environment variables from the edge agent to the edge stacks
* Fixed an issue where users were unable to perform a rolling restart for a deployment
* Enhanced the log collection and viewing for individual containers in async environments
* Fixed a missing `PORTAINER_EDGE_ID` variable in async environments
* Improved the visibility of errors when performing edge agent updates
* Optimized TLS validation for async environments
* Optimized the web editor performance
* Added Kerberos support for Windows AD Authentication
* Resolved the following CVEs:
  * CVE-2025-22871
  * CVE-2025-24358

### **Deprecated and removed features**

**Deprecated features**

* We are deprecating the provisioning features for Kubernetes as a service (KaaS) in this release, and the feature will be removed in a future release. You will still be able to use your existing KaaS clusters as normal.
* We are deprecating the provisioning and cluster management features for MicroK8s in this release, and the feature will be removed in a future release. You will still be able to use your existing MicroK8s clusters as normal, but additional MicroK8s management functionality will be removed in the future.

**Removed features**

None

## Release 2.27.6

May 9, 2025

### Known issues <a href="#known-issues" id="known-issues"></a>

#### **Known issues with Podman support**

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### **Known issues with Talos clusters managed by Omni**

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration and does not affect authentication for any other functionality in the cluster.

### Changes <a href="#changes" id="changes"></a>

*

## Release 2.27.5

May 2, 2025

### Known issues <a href="#known-issues" id="known-issues"></a>

#### **Known issues with Podman support**

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### **Known issues with Talos clusters managed by Omni**

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration and does not affect authentication for any other functionality in the cluster.

### Changes <a href="#changes" id="changes"></a>

* Fixed an issue where the PORTAINER\_EDGE\_ID variable was not being set properly

## Release 2.29.2

April 24, 2025

### Known issues

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### Known issues with Talos clusters managed by Omni

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

### Changes

* Reverted the [github.com/gorilla/csrf](http://github.com/gorilla/csrf) library version bump

## Release 2.29.1

April 23, 2025

### Known issues

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### Known issues with Talos clusters managed by Omni

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

### Changes

* Fixed an issue where a user with the Namespace Operator role was not able to view Git based applications and registries
* Fixed an issue on the namespace creation view when fetching services from an empty namespace
* Resolved the following CVEs:
  * CVE-2025-22871
  * CVE-2025-22872
  * CVE-2025-22870
  * CVE-2025-22866
  * CVE-2024-45338

## Release 2.29.0

April 16, 2025

### Known issues

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### Known issues with Talos clusters managed by Omni

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

### New in this release

* Added code auto-completion in the Stack web editor.
* Improved the Helm details view to provide more comprehensive information about Helm releases.
* Added an informational message on the Edge Stack page regarding edge config file interpolation.
* Improved performance by skipping the processing of raw Docker snapshots when possible.
* Refactored the Helm upgrade implementation for improved stability and maintainability.
* Fixed an issue where Edge groups with more than 10k environments could not be edited.
* Fixed an issue where brackets and braces in URLs were incorrectly encoded.
* Fixed an issue where `libstack` used an incorrect working directory in some scenarios.
* Fixed an issue that prevented stack deployment when the Compose file contained profiles.
* Fixed an issue where HTTP panics were being suppressed, reducing visibility of failures.
* Fixed an issue where updating an Edge stack caused the process to get stuck.
* Fixed an issue where all ConfigMaps and Secrets in Kubernetes environments were incorrectly labeled as unused.
* Fixed an issue where Kubernetes cluster reservations were not being displayed.
* Fixed an issue where master/control plane nodes appeared as worker nodes on the cluster information page.
* Fixed a UI issue where the sub-table was misaligned compared to the main table items on the Kubernetes application list page.
* Fixed a UI alignment issue with tags in the Kubernetes ConfigMap and Secret views.
* Resolved the following CVEs:
  * CVE-2025-22868
  * CVE-2025-30204
  * CVE-2025-32386
  * CVE-2025-32387
* Implemented functionality to provide an additional method to update Team Memberships from external auth using API keys.
* Fixed an issue where user access was lost due to the `--disable-role-sync` flag in Kubernetes environments.
* Added the ability to assign a new role, Namespace Operator, for Kubernetes.
* Added support to view details of mTLS CA and server certificates in the Edge Compute settings.
* Added a feature to display mTLS certificate information for each environment on the home page.
* Added the ability to view mTLS certificate errors by hovering over the mTLS label on the home page.
* Introduced build-time validation for RBAC authorization usage in the frontend.
* Added additional options for Edge agent async check-in intervals.
* Improved performance when updating Edge groups in Edge Stacks with configured Edge configurations.
* Improved performance when resolving endpoints based on Edge groups.
* Removed redundant status updates for async Edge agents.
* Fixed an issue where remote agent updates could not be scheduled properly for large Edge groups (>10k).
* Fixed an issue where the Environment Details page could not be opened for async Edge agents.
* Fixed an issue where async Edge agents did not use the default intervals.
* Fixed an issue where the Environment Group Access page failed to render the list view in large-scale environments.
* Fixed an issue with separating CPU and memory requests and limits.
* Fixed an issue where a false error message "Endpoint is not in async mode" was displayed.
* Fixed a data loss issue when updating stacks with relative path enabled.
* Fixed an error that occurred when updating user theme settings in the profile page.
* Fixed an issue where the container image form disappeared after a hard page refresh.
* Fixed an issue where admin users encountered an error when visiting a specific page.
* Fixed an issue where updating Edge groups in Edge Stacks failed when Edge configuration was set.
* Fixed an issue where Edge configurations were not being deleted.
* Fixed an issue where the container snapshot from async agents did not display environment variable information.
* Fixed an issue where an "edge secret is not allowed to transmit over HTTP” error could appear when pushing a change to an Edge Configuration using the API
* Fixed an index-out-of-range issue resulting in a panic when using ECR registry.
* Fixed a UI issue with missing left spacing for form labels in the container details view for async Edge environments.

### **Deprecated and removed features**

**Deprecated features**

None

**Removed features**

None

## Release 2.27.4

April 15, 2025

### Known issues <a href="#known-issues" id="known-issues"></a>

#### **Known issues with Podman support**

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### **Known issues with Talos clusters managed by Omni**

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration and does not affect authentication for any other functionality in the cluster.

### Changes <a href="#changes" id="changes"></a>

* Implemented functionality to provide a method to update Team Memberships from external auth
* Fixed an issue where an "edge secret is not allowed to transmit over HTTP” error could appear when pushing a change to an Edge Configuration using the API
* Resolved the following CVEs:
  * CVE-2025-22868
  * CVE-2025-30204
  * CVE-2025-32386
  * CVE-2025-32387

## Release 2.28.1

March 20, 2025

### Known issues

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### Known issues with Talos clusters managed by Omni

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

### Changes

* Fixed "unable to retrieve namespace" errors visible in Kubernetes environments using CA-signed TLS certificates

## Release 2.28.0

March 19, 2025

This is a STS (Short Term Support) release that includes all the changes added up to and including the 2.27.2 patch release as well as various fixes aimed at enhancing the stability and scalability of Portainer. For more details on what is included from the 2.27 release, refer to the [2.27 release notes](#release-2.27.0).

### Known issues

* We are aware of an issue in 2.28.0 for Kubernetes environments with CA-signed TLS certificates configured. A patch release is coming for this issue but we do not recommend users with this configuration update to 2.28.0 at this time.

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### Known issues with Talos clusters managed by Omni

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

### New in this release

* Fixed an issue where users were unable to view details of the Portainer Server image
* Fixed an issue where Swarm stacks that had recently been stopped were unable to be restarted
* Optimized the update of endpoint relations
* Added the display of external Load Balancer information in the UI
* Fixed an issue where mTLS certs uploaded in the app were ignored on server restart
* Switched to using the official Helm SDK rather than Helm Binary
* Converted the Cluster Details view to React
* Added a mTLS status icon to environments
* Fixed an issue where the select all checkbox didn't reflect the selected state
* Fixed an issue with Kubeconfig generation when using real SSL certs
* Added the ability to view the mTLS certificate in the UI
* Converted the Helm details view to React
* Fixed an issue where the Edge stack count could be doubled
* Optimized Edge Stack performance
* Added the ability to dynamically choose env files to include in Docker Compose
* Ensured all list API calls; namespaces, applications, configMaps etc filter out system resources for all non-admin users
* Fixed an issue where invalid deployments could fail silently
* Migrated the Helm templates list to React
* Added the ability to view the mTLS CA certificate in the UI
* Fixed an issue where the namespaces dropdown could list namespaces the user did not have access to
* Optimized automatic team memberships
* Fixed an issue where adding Omni nodes wasn't showing available machines
* Fixed user access loss due to `--disable-role-sync` flag
* Fixed an issue where Edge Stacks with Edge Configurations could get stuck in a pending state when the Edge Configurations folder was not in the root of the repo

## Release 2.27.2

March 19, 2025

### Known issues

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### Known issues with Talos clusters managed by Omni

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

### Changes

* Fixed an issue on Kubernetes environments where invalid deployments could fail silently
* Fixed an issue on Kubernetes environments where namespaces that the user did not have access to could be shown
* Fixed an issue where the select all checkbox didn't reflect the selected state
* Resolved CVE-2025-22869
* Optimized OAuth automatic team memberships
* Fixed an issue where adding Omni nodes wasn't showing available machines
* Fixed user access loss due to `--disable-role-sync` flag

## Release 2.27.1

February 27, 2025

### Known issues

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### Known issues with Talos clusters managed by Omni

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

### **Changes**

* Security: Resolved CVE-2024-50338
* Fixed an issue where Compose files were not interpolated with .env
* Fixed an issue where team(s) added to namespace access disappeared when a new team was added to environment
* Added server certificate revalidation for mTLS connections
* Added a mTLS status indicator icon for Edge Agent environments

## Release 2.27.0

February 20, 2025

### Known issues

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### Known issues with Talos clusters managed by Omni

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

### New in this release

* Security: CVE-2025-21614, CVE-2025-21613, CVE-2024-45337, and CVE-2024-11053
* Fix: Early exit optimization does not return the correct error
* Fix: 2.19.5 - 2.21 Migration fails with "`StorageError: invalid object`"
* Optimization: Investigate the web editor slowdown while typing
* Improvement: Edge stack missing value warning improvement
* Fix: Removing an edge stack makes the backend panic
* Fix: Object not found inside the database (bucket=endpoint\_relations, key=8)
* Improvement: use an Edge Stack Status Update coordinator
* Fix: High memory usage when counting nodes and CPUs
* Fix: Unable to add environment to static Edge group
* Fix: Removing an edge stack makes the backend panic
* Fix: Error “failed to find local environment” occurs if there is at least one environment configured but no local environment
* Fix: Bitnami Helm Charts location has moved
* Fix: Edge stack "deployment received" counting is not correct with large scale deployments
* Fix: Unable to deploy a git edge stack
* Fix: RegistryList API operation returns password in clear text
* Fix: Agent Edge stack status watcher errors on Swarm
* Fix: edge\_stack folder in volume is not deleted after Edge stack is removed
* Fix: Swarm: Empty/incorrect value in Host column of Images list
* Fix: Unpopulated Volumes Dropdown in App Templates in Portainer 2.21.4
* Fix: "Select all" should select only elements of the current page
* Fix: podman doesnt appear in the option to filter by platform in the homepage
* Fix: Edge stack webhooks cannot be disabled once created
* Fix: Unable to expand application list rows to view published URLs
* Improvement: Change docs URL schema to LTS / STS
* Fix: Group membership synchronization between Portainer and Azure OAuth appears to be broken
* Fix: Adding environment variables to an application with a configmap moves the configmap to the secrets section and brings down the app
* Improvement: Kubernetes - Rename `Create from file` to `Create from code`
* Fix: Incorrect Replicated count while performing rolling restart on deployment
* Fix: Kubernetes - Broken Cluster View
* Fix: Podman - Unable to create an image from a container
* Fix: User gets duplicated in a Team for each login, once it reaches 12 duplicates user unable to use any functions in Portainer
* Improvement: Unit test the docker RBAC layer in BE
* Improvement: Associating async Edge agent based devices in the waiting room outputs tunnel error
* Optimization: Remove useless pending actions on startup
* Fix: Edge Stack update not working
* Fix: Async snapshots are discarded from the server when the agent doesn't send them
* Fix: Update & Rollback schedules are not executed on standard edge agents
* Fix: Edge Stack update not working
* Fix: Unable to successfully update async edge stack using parallel update
* Fix: Edge stack webhook does not update and pass env variables at the same time
* Fix: Unable to redeploy stack if repo ref is changed
* Fix: Edge settings don't persist when restarting Portainer
* Fix: Can't Delete Image from Swarm Cluster
* Improvement: Stabilise the overall diagnostics data collection
* Improvement: Improve validations for Omni Credentials
* Fix: RoleBinding and ClusterRoleBinding removal issues
* Improvement: Refresh available machines when switching Omni credentials

### Deprecated and removed Features

**Deprecated features**

* Reminder: `<platform>-<arch>` image tags were deprecated in 2.21

**Removed features**

The following API endpoints have been removed:

* POST /endpoints/{id}/edge/trust
* GET /edge\_templates
* POST /templates/file
* POST /endpoints/{id}/kubernetes/helm/repositories
* GET /endpoints/{id}/kubernetes/helm/repositories
* GET /kubernetes/{id}/namespaces/{namespace}/configuration
* POST /cloud/{provider}/cluster
* GET /cloudcredentials
* POST /cloudcredentials
* GET /cloudcredentials/{id}
* DELETE /cloudcredentials/{id}
* PUT /cloudcredentials/{id}
* POST /custom\_templates
* POST /edge\_jobs
* GET /cloud/microk8s/addons
* POST /stacks
* DELETE /edge\_stacks/{id}/status/{environmentId}
* POST /edge\_stacks
* GET /status/version
* GET /status/nodes

## Release 2.26.1

January 21, 2025

### Known issues

#### Known issues with Docker support

* Service pruning does not work with stacks using relative paths

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### Known issues with Talos clusters managed by Omni

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

#### Known issues with Kubernetes

* Displaying job executions of cron jobs are limited to 3.

### Changes

* Fixed issues relating to the Omni / Talos integration:
  * Implemented additional validation when adding Omni credentials in Portainer to ensure the Service Account key is correct, that it has an admin role, and that it is not expired.
  * Prevent the deletion of Omni credentials if they are still in use with an Omni environment within Portainer.
  * Do not apply Machine Config patches when ‘Override network settings’ is disabled.

## Release 2.26.0

January 15, 2025

This is a STS (Short Term Support) release that includes all the changes added up to and including the 2.25.1 patch release as well as various fixes aimed at enhancing the stability and scalability of Portainer. For more details on what is included from the 2.25 release, refer to the [2.25 release notes](#release-2.25.0).

### Known issues

#### Known issues with Docker support

* Service pruning does not work with stacks using relative paths

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

#### Known issues with Talos clusters managed by Omni

* Loading Omni specific information in the Cluster Details view and configuring an existing Talos cluster is currently restricted to Portainer Admins. Environment Admins will get a forbidden error when attempting to do this. This only applies to Omni configuration, and does not affect authentication for any other functionality in the cluster.

#### Known issues with Kubernetes

* Displaying job executions of cron jobs are limited to 3.

### New in this release

* Added the ability to remove associated volumes when deleting a stack
* Improved the performance for edge:
  * Optimized the server polling handler
  * Optimized the snapshot diff for async
  * Optimized AddEnvironmentToEdgeGroups()
  * Made the async polling handler work concurrently in an optimistic way to allow for more parallelism
  * Optimized the async command creation to reduce DB lookups
  * Optimized the concurrent Edge Stack retrieval by the agent
  * Optimized the Edge Stack status update by the agent
* Fixed a goroutine leak in the Agent that would exhaust the resources over time
* Fixed Edge Stack status updates so that it doesn’t cause wrong counts
* Updated compose-unpacker so it doesn’t rely on the docker-compose binary
* Fixed data races:
  * GetPlatform()
  * Docker transport
  * Agent stack manager
  * Edge auto-onboarding
* Fixed potential logic problems related to edge environment configurations
* Fixed the async snapshot diff logic for Kubernetes environments
* Fixed the router for Kubernetes requests
* Fixed a problem that prevented the assignment of multiple edge groups to async agents on association
* Fixed a problem that prevented the association of async devices without groups
* Fixed a problem that would cause for the edge stack local filesystem path to not be retained when using GitOps edge configs
* Fixed the volume list retrieval and app template deployment when the environment snapshot doesn’t exist
* Standardized the lower case string comparison method
* Fixed a problem that prevented the update of edge stacks when using webhooks with async environments
* Added a new feature to integrate with Sidero Omni
* Added a feature behind a feature flag to disable automatic sync of the built-in Kubernetes roles
* Added a 30 minutes time interval to the OAuth session timeout options
* Added a new Kubernetes view for Jobs and Cron Jobs
* Fixed update create from file option order

### Deprecated and removed features

#### Deprecated features

None

#### Removed features

None

## Release 2.25.1

December 20, 2024

### Known issues

#### Known issues with Docker support

* Service pruning does not work with stacks using relative paths

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

### Resolved CVEs

* CVE-2024-45337 \[[BE-11511](https://linear.app/portainer/issue/BE-11511/cve-2024-45337)]

### Changes

* Fixed an issue where excessive warnings were logged if agents weren’t updated to match server version \[[BE-11498](https://linear.app/portainer/issue/BE-11498/snapshots-not-forming-for-edge-agents)]

## Release 2.21.5

December 20, 2024

### Resolved CVEs <a href="#resolved-cves" id="resolved-cves"></a>

* CVE-2024-45337

### Changes <a href="#changes" id="changes"></a>

* Fixed an issue that omitted copying the IP address in container port mapping when provided during the Edit/Duplicate operation for an existing container.
* Fixed an issue with images that included files failing to build.
* Fixed a resource leak that prevented the backup process from finishing under some specific circumstances.
* Optimized the space used by Git repositories.
* Fixed aggressive image pulling retry.
* Fixed an issue where LDAP users get duplicated in a Team for each login.

## Release 2.25.0

December 16, 2024

This is a [STS (Short Term Support) release](https://docs.portainer.io/start/lifecycle#sts-versus-lts) that includes all the changes added up to and including the 2.24.1 patch release as well as various fixes aimed at enhancing the stability and scalability of Portainer. For more details on what is included from the 2.24 release, refer to the [2.24 release notes](#release-2.24.0).

### Known issues

#### **Known issues with Docker support**

* Service pruning does not work with stacks using relative paths

#### **Known issues with Podman support**

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

### New in this release

* Added the ability to prune services while updating Compose Edge Stacks
* Updated Compose to v2.31
* Optimized the HTTP request/response compressor to reduce allocations and improve performance
* Async Edge Agent: cleaned up executed commands to improve performance
* Reduced the total locking time for the backup process and improved the error messages
* Stopped preventing the server startup when `docker_config/config.json` file is corrupted
* Added the ability for users to specify Portainer agent and updater images from their private registry when creating a remote update or rollback schedule for agents
* Fixed a problem that prevented interaction with Swarm volumes
* Fixed a problem that prevented the GitOps edge configurations from working properly
* Fixed the missing IP binding of published ports when editing a container
* Enforced timeouts for offline environments when doing parallel edge deployments
* Fixed a resource leak that prevented the backup process from finishing under some specific circumstances
* Removed incorrect persistence of filters when interacting with Services and Stack pages
* Restored the remember functionality in the filtered stacks search results
* Enforced Edge Stack naming rules
* Fixed an issue with images that included files failing to build
* Ensured proper Edge Stack removal after a power interruption in the Agent
* Fixed an issue where Git stacks using sub-directories and environment files could not be edited
* Fixed an issue where an extra network is created when deploying a stack with only external networks defined
* Fixed an issue where the `env_file` field in Compose files were being ignored
* Fixed an issue where a stack that built an image that it then referenced would fail to deploy with a "no such image" error
* Ensured that the `PORTAINER_EDGE_ID` variable is properly exposed when using Edge Configurations
* Added a new feature called Download Support Bundle
* Added a new feature to enable/disable debug logging within the Portainer UI
* Added a new button in the Licenses Page to support renewal
* Fixed an issue where Helm status was not correctly shown for deployments
* Fixed an issue where the date picker was unusable for activity logs in the dark mode
* Fixed an issue where the namespace level access not being applied to teams
* Fixed an issue where edge stack fails to be deleted when K8s job is set with TTL
* Fixed an issue where LDAP users get duplicated in a Team for each login
* Improved kapa.ai landing page
* Migrated a handful of legacy Angular based Kubernetes pages to React

### Deprecated and removed features

#### Deprecated features

* `PUT /kubernetes/{id}/namespaces` API endpoint

#### Removed features

None

## Release 2.24.1

December 3, 2024

### Known issues

#### **Known issues with Docker support**

* Service pruning does not work with stacks using relative paths

#### **Known issues with Podman support**

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

### Changes

* Fixed an issue where Git stacks using subdirectories and environment files could not be edited.
* Fixed an issue where an extra network was being created when deploying a stack with only external networks defined.
* Fixed an issue where the `env_file` field in Compose files was being ignored.
* Fixed an issue where users were unable to pull images from private registries as expected.
* Fixed an issue where a stack that built an image that it then referenced would fail to deploy with a "no such image" error.
* Fixed an infinite recursion issue in an RBAC route when switching users and connecting to an agent endpoint.
* Fixed an issue that omitted copying the IP address in container port mapping when provided during the Edit/Duplicate operation for an existing container.
* Fixed an issue with images that included files failing to build.
* Fixed an issue where activity logs shown in the Portainer UI were encoded with base64.

## Release 2.24.0

November 20, 2024

This is a [STS (Short Term Support) release](https://docs.portainer.io/start/lifecycle#sts-versus-lts) that includes all the changes added up to the 2.23 release and 2.21.4 LTS patch release, as well as various fixes aimed at enhancing the stability and scalability of Portainer. For more details on what is included from the 2.23 release, refer to the [2.23 release notes](#release-2.23.0).

### Known issues

**Known issues with Docker support**

* Service pruning does not work with stacks using relative paths

**Known issues with Podman support**

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful

### New in this release

* Bumped Go version to 1.23
* Improved the status tracking for Kubernetes Edge Stacks
* Rewrote the stack deployment code to remove the need for the docker-compose binary
* Clean-up and compact user activity DB on start-up
* Added the ability to prune services while deploying Compose stacks
* Added a retry period to Edge Stack deployments
* Fixed user authentication log sorting
* Defaulted to descending timestamp order in the user activity log
* Fixed user activity log sorting
* Fixed aggressive image pulling retry
* Relocated the GitOps TLS toggle so it’s harder to overlook
* Added timeouts to OAuth requests
* Fixed problem that prevented environment association in the waiting room
* Fixed a problem that prevented the Docker image exporting
* Improved the Kubernetes Cluster node view to display conditions
* Migrated more Angular based pages to React
* Fixed the following Kubernetes regressions:
  * Standard user can't get cluster scoped ingress controllers
  * CPU/Memory Limit & Reservation values not multiplied by replica count on "Applications running on this node" table
  * Application rollout restart isn’t functional

### Deprecated and removed features

#### Deprecated features

None

#### Removed features

None

## Release 2.21.4 <a href="#release-2.21.4" id="release-2.21.4"></a>

October 25, 2024

### Changes <a href="#changes" id="changes"></a>

* Ported client API negotiation changes to ensure LTS can be compatible with future Docker versions.
* Improved the Edge-related API error response by including environment ID and name.
* Added the display of the missing Edge stack deployment errors on the Edge stack environment status page.
* Fixed an issue that prevented the removal of older files when updating an Edge configuration.
* Fixed an issue that prevented consecutive updates of Swarm services from reloading the page.

## Release 2.23.0

October 16, 2024

This is a [STS (Short Term Support) release](https://docs.portainer.io/start/lifecycle#sts-versus-lts) that includes all the changes added up to and including the 2.22.0 release, as well as various fixes aimed at enhancing the stability and scalability of Portainer. For more details on what is included from the 2.22 release, refer to the [2.22 release notes](#release-2.22.0).

### Known issues

#### Known issues with Docker support

* Image export is not functioning

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful
* Unable to create an image from a container

#### Known issues with Kubernetes support

* Service accounts, Cluster Roles/Bindings, Roles/Role Bindings) show system resources when toggle is off
* Standard user can't get cluster scoped ingress controllers
* CPU/Memory Limit & Reservation values not multiplied by replica count on "Applications running on this node" table
* Application rollout restart is not functioning

### New in this release

* Improved the Home page search speed
* Improved OAuth logging to help diagnose errors
* Increased the CRL request timeout in the Agent to 30s
* Moved the webhook deploying logic to the background to avoid timeouts
* Optimized the space used by Git repositories
* Improved the Edge-related API error response by including environment ID and name
* Fixed the removal of old files when doing an Edge Config update
* Added the display of the missing Edge stack deployment errors on the Edge stack environment status page
* Fixed the Pending status getting stuck for Edge stacks when re-associating environments
* Fixed issues with Kubernetes resources not showing information correctly
* Improved the overall experience for Kubernetes

### Deprecated and removed features

#### Deprecated features

None

#### Removed features

* **Platform and Architecture-Specific Images**:
  * We have removed image tags named for various architectures using the convention `<platform>-<arch>`. These images tags were deprecated in a previous release. This change ensures further standardization and consistency across our software distribution.

## Release 2.21.3 <a href="#release-2.21.3" id="release-2.21.3"></a>

October 8, 2024

### Changes <a href="#changes-1" id="changes-1"></a>

* Improved home page search performance, addressing slow response times in certain environments.
* Fixed an issue where the Edge admin role would be removed after login when authenticating via OAuth.
* Fixed an issue where the CRL (Certificate Revocation List) request timeout may be too short, causing potential connection issues.

## Release 2.22.0

October 3, 2024

This is a [STS (Short Term Support) release](https://docs.portainer.io/start/lifecycle#sts-versus-lts) that includes all the changes added up to and including the 2.21.2 release, as well as various fixes aimed at enhancing the stability and scalability of Portainer. For more details on what is included from the 2.21 release, refer to the [2.21 release notes](#release-2.21.2).

### Breaking changes

As part of the changes on the Kubernetes experiences, some API operations for Kubernetes management may have changed slightly.

### Known issues

#### Known issues with Podman support

* Podman environments aren't supported by auto-onboarding script
* It's not possible to add Podman environments via socket, when running a Portainer server on Docker (and vice versa)
* Support for only CentOS 9, Podman 5 rootful
* Unable to create an image from a container

#### Known issues with Kubernetes management

* Applications deployed via helm chart are no longer grouped on the App list screen
* Service accounts, Cluster Roles/Bindings, Roles/Role Bindings) show system resources when toggle is off
* Standard user can't get cluster scoped ingress controllers
* Unused label incorrectly showing on used volumes, and Used by column is blank
* NaN value on Memory & CPU used bars on Node Details screen
* CPU/Memory Limit/Reservation values on **Applications running on this node** table rounding down
* Volumes created within Portainer are incorrectly labelled as External

### New in this release

* **Podman Support**:
  * Portainer now supports Podman. It can be installed on Podman and manage Podman environments. Initial support includes Podman 5.x running on CentOS environments.
* **ACI Enhancements**:
  * Enhancements to ACI management include support for GPUs, private IPs, persistence, and the ability to start, stop, and restart container instances, among other improvements.
* **Better Kubernetes Management Experience**:
  * The Kubernetes management experience has been overhauled by relocating most of the logic from the client to the server, improving client speed and responsiveness. This update also introduces the ability to manage all Kubernetes resources via a simplified, abstracted API.
* **Security Controls for Kubernetes**:
  * New security controls allow administrators to disable access to downloading Kubeconfig files and interacting with the Kubernetes shell for non-administrator users.
* **Edge Capabilities Improvements**:
  * Enhancements to the Edge features have resulted in a more stable, performant, and reliable experience when using Edge capabilities.
* **Stability Improvements**:
  * Various fixes have been applied to increase the overall stability of Portainer.
* **Scalability Enhancements**:
  * Adjustments have been made to improve Portainer's performance and reliability at scale, especially in larger environments.
* **Security**:
  * Critical and high-security vulnerabilities (CVEs) in dependencies shipped within the Portainer images have been addressed. Key components, such as the Docker client and kubectl, have been updated to ensure a secure environment.

### Deprecated and removed features

#### Deprecated features

* **Platform and Architecture-Specific Images**:
  * We are deprecating image tags named for various architectures using the convention `<platform>-<arch>`. This change ensures further standardization and consistency across our software distribution.

#### Removed features

* **Platform and Architecture-Specific Images**:
  * We are removing images named using the convention `<platform>-<arch>-<version>`. These images were deprecated in a previous release in favor of the newer convention `<version>-<platform>-<arch>`. This change ensures standardization and consistency across our software distribution.
* **Kompose Logic**:
  * All logic related to **Kompose** has been removed, following its deprecation in a previous version.
* **Nomad Support**:
  * All logic related to **Nomad** support has been removed after it was deprecated and subsequently removed from the client in version 2.20.

## Release 2.21.2

September 24, 2024

### Changes

* Updated Linode branding to align with the new “Akamai Connected Cloud”.
* Fixed an issue with stack deployment on Docker when using a .env file from a Git Repository and referencing it in the Compose file.

## Release 2.21.1

September 10, 2024

### Changes

* Fixed an issue where Portainer would crash when cloning a large Git repository
* Introduced a JWT revocation mechanism to revoke JWTs after logout
* Fixed an issue when re-creating a container on Docker 24
* Fixed an issue with stack deployment on Docker when using environment variables in the volumes section of the Compose file

## Release 2.21.0

August 27, 2024

This is our first Long-Term Support (LTS) release, which includes all the changes that have been added up to the 2.20.3 release, as well as various fixes aimed at enhancing the stability and scalability of Portainer.

### What’s Included

* **Changes from 2.20.x**:
  * This LTS release incorporates all the features, improvements, and bug fixes from the 2.20.x series of releases.
  * For detailed information about the changes included in the 2.20.x releases, please refer to the [2.20.x release notes](#release-2.20.0).

### New in this Release

* **Stability Improvements**: Various fixes have been applied to increase the overall stability of Portainer.
* **Scalability Enhancements**: Specific adjustments have been made to improve the usage of Portainer at scale, ensuring better performance and reliability in larger environments.
* **Security**: Critical and high security vulnerabilities (CVEs) associated with dependencies shipped within the Portainer images have been addressed. This includes updates to key components like the Docker client and kubectl to ensure a secure environment.

### Deprecated Capabilities and Features

* We’re deprecating the platform and architecture-specific images named using the convention `<platform>-<arch>-<version>` in favor of the newer convention `<version>-<platform>-<arch>`. This change ensures standardization and consistency across our software distribution. In the future, we’ll only build and publish images using the new tag convention.

## Release 2.20.3

May 21, 2024

This is an STS (Short-Term Support) release. Read more in our ["Portainer 2.20 STS" blog post](https://www.portainer.io/blog/portainer-2.20-release).

### Important Notice

On update to this Portainer version, stacks and edge stacks will have their containers restarted after updating them. This is caused by the use of Docker Compose 2.26.1, which requires this restart. Note: If you already updated to 2.20.0, 2.20.1 or 2.20.2 previously, stacks and edge stacks that DO NOT use relative paths may already have had their containers restarted on update of them, and you would not then see a restart again.

### Edge

* Resolved an issue where edge configuration files were not being backed up.
* Resolved an issue where device registration via the waiting room was extremely slow during large-scale edge deployment.
* Resolved an issue where users were unable to remove or update an edge configuration that was pending deployment on a device.

### Docker

* Resolved an issue introduced in 2.20.0 where stopped Docker containers were incorrectly shown with an Unused badge. [portainer/portainer#11797](https://github.com/portainer/portainer/issues/11797)

### Swarm

* Resolved an issue where the Edit Container page on Swarm environments was not loading properly. [portainer/portainer#11830](https://github.com/portainer/portainer/issues/11830)

### Kubernetes

* Resolved an issue introduced in 2.20.0 where, when a placement rule was created for a Kubernetes application, if it was not met for a node, then it would not show up in the expand rows of the Application Details Placement constraints/preferences table. [portainer/portainer#11826](https://github.com/portainer/portainer/issues/11826)
* Resolved an issue when creating a MicroK8s cluster where using a hyphen to specify an IP range had stopped working in 2.19.
* Resolved an issue where the "More resources" views in Kubernetes would redirect to the Dashboard upon refresh.
* Resolved an issue in the Kubernetes Applications List page where the namespace filter selection of a system namespace did not persist on refresh or revisit. [portainer/portainer#11798](https://github.com/portainer/portainer/issues/11798)
* Introduced a tooltip to the 'Rollback to previous configuration' button in the Kubernetes Application Details screen to explain how rollback works. [portainer/portainer#11804](https://github.com/portainer/portainer/issues/11804)
* Prevented a panic from occurring when mistakenly attempting to deploy a Kubernetes application and supplying a docker-compose.yaml instead of a Kubernetes manifest. [portainer/portainer#11796](https://github.com/portainer/portainer/issues/11796)

### MicroK8s

* Applied updates and ensured confirmed Kubernetes 1.30 support with creation of MicroK8s clusters.
* Introduced an offline mode for creation of a MicroK8s Kubernetes cluster on air-gapped nodes.

### Portainer

* Resolved an issue where pending actions to be run on environments could end up in a panic state. [portainer/portainer#11818](https://github.com/portainer/portainer/issues/11818)
* Resolved an issue where the subpath of an image tag was incorrectly truncated. [portainer/portainer#11831](https://github.com/portainer/portainer/issues/11831)
* Resolved an issue around excessive GitHub API Portainer version checking on page loads. [portainer/portainer#11795](https://github.com/portainer/portainer/issues/11795)
* Resolved an issue where loading a large number of volumes took an unreasonable amount of time [portainer/portainer#11829](https://github.com/portainer/portainer/issues/11829)
* Resolved an issue in the agent where removing an undeployed stack resulted in errors. [portainer/portainer#11828](https://github.com/portainer/portainer/issues/11828)
* Corrected the title wording and some UI styling in the Authentication Logs and Activity Logs screens. [portainer/portainer#11807](https://github.com/portainer/portainer/issues/11807)
* Resolved an issue with deploying of containers via Portainer running on Windows Server 2022, where an error regarding CAP\_AUDIT\_WRITE was occurring. [portainer/portainer#11805](https://github.com/portainer/portainer/issues/11805)

### API Changes

<details>

<summary>New endpoints: 1</summary>

* `POST /endpoints/edge/trust` Associate one or more Edge environments in the waiting room to environments

</details>

<details>

<summary>Deprecated endpoints: 1</summary>

* `POST /endpoints/{id}/edge/trust` Associate an Edge environment in the waiting room to an environment
  * Use `POST /endpoints/edge/trust` instead

</details>

## Release 2.20.2

May 1, 2024

This is an STS (Short-Term Support) release. Read more in our ["Portainer 2.20 STS" blog post](https://www.portainer.io/blog/portainer-2.20-release).

### Resolved CVEs

* Resolved CVE vulnerabilities for Windows images [portainer/portainer#11716](https://github.com/portainer/portainer/issues/11716)
* Updated kubectl to resolve CVEs. [portainer/portainer#11741](https://github.com/portainer/portainer/issues/11741)
* Resolved CVE vulnerabilities for docker binary [portainer/portainer#11717](https://github.com/portainer/portainer/issues/11717)
* Resolved CVE vulnerabilities for protobuf [portainer/portainer#11718](https://github.com/portainer/portainer/issues/11718)
* Resolved CVE vulnerabilities for crypto [portainer/portainer#11719](https://github.com/portainer/portainer/issues/11719)
* Updated [k8s.io/apiserver](http://k8s.io/apiserver) and Helm to resolve CVEs. [portainer/portainer#11740](https://github.com/portainer/portainer/issues/11740)
* Resolved CVE vulnerabilities for containerd
* Updated Docker client library to resolve CVEs. [portainer/portainer#11738](https://github.com/portainer/portainer/issues/11738)
* Resolved CVE vulnerabilities for otelgrpc
* Resolved CVE vulnerabilities for stdlib [portainer/portainer#11720](https://github.com/portainer/portainer/issues/11720)
* Resolved CVE-2024-29296 by creating uniform response time for login attempts. [portainer/portainer#11736](https://github.com/portainer/portainer/issues/11736)
* Resolved a CVE regarding data encryption. [portainer/portainer#11737](https://github.com/portainer/portainer/issues/11737)
* Updated Docker Compose to resolve CVEs. [portainer/portainer#11739](https://github.com/portainer/portainer/issues/11739)
* Updated OPA Gatekeeper for Pod security constraints feature in order to resolve CVEs.

### Edge

* Resolved an issue with the edge post initiation migration runner to ensure it runs migrations at the appropriate time, when connection between an edge environment and Portainer server has been established. [portainer/portainer#11733](https://github.com/portainer/portainer/issues/11733)

### Docker

* Resolved an issue that caused errors when users attempted to connect to their Docker environment via API using HTTPS [portainer/portainer#11721](https://github.com/portainer/portainer/issues/11721)
* Provided info text in the UI to clearly explain environment variables stack.env file usage when deploying Docker stacks via Git vs. other methods. [portainer/portainer#11732](https://github.com/portainer/portainer/issues/11732)

### Kubernetes

* Ensured confirmed support of vanilla Kubernetes 1.30 clusters. [portainer/portainer#11730](https://github.com/portainer/portainer/issues/11730)
* Fixed a bug with 2.20 migrating of Kubernetes secrets ownership to an improved model where the migration was not being flagged as complete.
* Resolved an issue with Kubernetes environments that have a significant number of services where the Dashboard services panel never completed loading and the loading spinner was indefinitely displayed. [portainer/portainer#11734](https://github.com/portainer/portainer/issues/11734)

### KaaS

* Ensured Kubernetes 1.29 is supported with Azure Kubernetes Service (AKS) provisioning of KaaS clusters.
* Ensured Kubernetes 1.29 is supported with Linode Kubernetes Engine (LKE) provisioning of KaaS clusters.

### Portainer

* Fixed an issue introduced in 2.20.0 where a user logged in using external SSO could no longer create a Portainer API access token. [portainer/portainer#11731](https://github.com/portainer/portainer/issues/11731)
* Resolved an issue where pending actions to be run on environments would still be considered for deleted environments (although not actually run). [portainer/portainer#11735](https://github.com/portainer/portainer/issues/11735)
* Resolved issue where containers that exited with code 0 were incorrectly marked as failed deployments [portainer/portainer#11724](https://github.com/portainer/portainer/issues/11724)
* Introduced an additional option to automatically detect the authentication style for OAuth [portainer/portainer#11725](https://github.com/portainer/portainer/issues/11725)

### API Changes

* Fixed the content type for responses from the API endpoint used for token generation [portainer/portainer#11723](https://github.com/portainer/portainer/issues/11723)

<details>

<summary>Modified endpoints: 4</summary>

* `PUT /settings` Update Portainer settings
  * Parameters
    * Added: `body.OAuthSettings.AuthStyle`
  * Return Type
    * Added: `OAuthSettings.AuthStyle`
* `GET /settings` Retrieve Portainer settings
  * Return Type
    * Added: `OAuthSettings.AuthStyle`
* `PUT /settings/default_registry` Update Portainer default registry settings
  * Return Type
    * Added: `OAuthSettings.AuthStyle`
* `POST /users/{id}/tokens` Generate an API key for a user
  * Return Type
    * Added: `apiKey`
    * Added: `rawAPIKey`

</details>

## Release 2.19.5

April 22, 2024

### Portainer

* Resolved CVE-2024-29296 by creating uniform response time for login attempts

## Release 2.20.1

April 5, 2024

This is an STS (Short-Term Support) release. Read more in our ["Portainer 2.20 STS" blog post](https://www.portainer.io/blog/portainer-2.20-release).

### Important Note Regarding Docker 26 Support

Please be aware that support for Docker 26 is provided on an "as-is" basis and is primarily driven by best-effort principles. Minimal regression testing has been conducted to ensure basic functionality. Users should proceed with caution and report any issues they encounter.

### Docker

* Resolved an issue where Docker 25/26 API changes affected container-related pages and image size display [portainer/portainer#11504](https://github.com/portainer/portainer/issues/11504)

### Kubernetes

* Resolved an issue where deploying GitOps edge stacks on a Kubernetes edge device resulted in error [portainer/portainer#11503](https://github.com/portainer/portainer/issues/11503)
* Resolved an issue where the secret owner migration process could lead to a deadlock, preventing the HTTP(S) server from starting. [portainer/portainer#11501](https://github.com/portainer/portainer/issues/11501)

### Portainer

* Fixed an issue where local stacks were being overwritten by orphaned stacks with the same name in the regular stack listing page [portainer/portainer#11502](https://github.com/portainer/portainer/issues/11502)

## Release 2.20.0

March 19, 2024

### Overview of changes

Introducing the new Portainer BE 2.20.0 release. This is an STS (Short-Term Support) release.

As you gear up for the transition to Portainer BE 2.20.0, our latest STS (Short-Term Support) installment, ensuring a smooth upgrade is key. We urge you to [back up your configurations](https://docs.portainer.io/admin/settings/general#back-up-portainer) via the Portainer UI beforehand. This backup acts as your safety net, ensuring you can gracefully revert to the prior version or state if the new frontier proves too wild. Additionally, pore over the release notes for catching any compatibility issues, understanding deprecated functionalities, and identifying essential tweaks to your current setup. Your diligence will pave the way for a seamless update.

A Short-Term Support release can be considered as "bleeding-edge" as it will contain the latest features and functionality we've developed. The STS releases (including this one) will go through a significant amount of pre-release testing, but there may be changes that could cause regressions and features that might see further iterations. As such, if stability is a crucial concern for your setup we wouldn't recommend deploying STS releases on production environments.

Read more in our ["Portainer 2.20 STS" blog post](https://www.portainer.io/blog/portainer-2.20-release).

### Breaking changes

* Discontinued Nomad support in this release. Users won't be able to create new Nomad environments from the UI, and existing Nomad environments are hidden, ceasing their management through Portainer
* Introduced a requirement to specify the current user's password when adding an API token via the UI or the POST /users/{id}/tokens API endpoint.
* Fixed issue when deploying Docker stacks from Git-based custom templates where a user could edit the content via the web editor, when they should only have been able to deploy the content from Git.

### Deprecation notice

* DEPRECATED API endpoint `GET /kubernetes/{id}/namespaces/{namespace}/configuration`. Following Portainer 2.19 split of K8s ConfigMaps and Secrets to two UI tabs and K8s API proxy use, the original endpoint combining both resource types is marked deprecated.
* DEPRECATED API endpoint `GET+POST /endpoints/{id}/kubernetes/helm/repositories`, MOVED Helm UI option to Advanced Deployment/Create from Manifest screen + now allow users to delete their Helm repos. New endpoint `GET+POST /users/{id}/helm/repositories` added.

### Resolved CVEs

* Updated various packages to resolve CVEs. [portainer/portainer#9224](https://github.com/portainer/portainer/issues/9224)
* Resolved CVEs for Portainer Agent
* Resolved CVEs for Portainer CE and BE

### Edge

* Addressed CVEs affecting Nomad, enhancing security and stability
* Fixed an issue where edge stacks deployed with retry policy and failing to deploy would remain stuck indefinitely after 1 hour of retries
* Fixed issue where edge stacks with GitOps enabled, would stop polling after restarting the server.
* Fixed issue where confirmation modal was missing when user was trying to update edge stacks.
* Resolving an issue where newer versions of images were not being pulled from the registry as expected when re-pull option was turned on.
* Fixed issue where pre-pull image and retry deployment options were missing after edge stack was deployed
* Fixed an issue where clicking to filter ascending/descending by a column on the waiting room page did not result in any sorting.
* Fixed issue where admin users were unable to update a Git-based edge stack created by another user.
* Fixed an issue where, upon disabling the waiting room feature, existing devices in the waiting room are now automatically associated to prevent them from remaining unassociated
* Implemented a new "Edge Admin" role, enabling users to administer the edge compute feature without altering Portainer settings.
* Fixed issue where the "Retry deployment" toggle did not persist when editing an edge stack.
* Improved UX of making "GitOps Edge Configuration" stand independently, simplifying access and allowing users to effortlessly enable relative paths during configuration.
* Resolved an issue where the count of configurations pushed to edge devices was inaccurately displayed. We now prevent double counting and ensure accurate representation
* Updated app template version to 3.0, now supporting edge apps in templates.
* Corrected the incorrect icon style for edge groups in the UI
* Enhanced the tooltips in the auto onboarding page to provide clear instructions on how to use the "Edge ID" field. Users will now receive guidance on the specific command to run in the script for generating the edge ID
* Resolved an issue where the waiting room remained visible in the sidebar menu despite being disabled by the administrator. The waiting room now correctly hides when disabled.
* Simplified scheduler time settings by removing seconds, providing users with a more straightforward configuration experience.
* Fixed issue where searching for edge groups in the waiting room returned no results
* Fixed issue where non-trusted environments were incorrectly counted for static edge groups
* Implemented the ability for users to upload and manage edge configurations grouped by folders, allowing seamless deployment based on matching edge group names rather than individual devices.
* Resolved an issue by implementing timeouts for the agent during snapshot building, preventing it from getting stuck indefinitely or taking excessive time in unresponsive Docker daemon scenarios
* Fixed an issue where the Edge Agent was resetting EndpointId to 0 and polling global-key incorrectly when disconnected from Portainer server, even with disabled edge compute features
* Introduced Edge App Templates and Custom Templates to address the absence of app and custom templates for edge stacks in Portainer
* Fixed an issue where a dynamic edge group would erroneously create a stack even if no environment was present
* Decoupled the display of Portainer API server URL and tunnel server address from the Edge Compute feature toggle, ensuring clear visibility regardless of the Edge Compute setting, addressing potential user confusion.

### Swarm

* Resolved an issue with the Docker Swarm Service List screen where image up to date indicators were not always correct.
* Fixed issue where relative path volumes in Docker Swarm environments did not update when new commits were pushed to the upstream repository and the user clicked "Pull and redeploy" in stacks with GitOps updates enabled.
* Updated the documentation link for Swarm agent setup in the UI to ensure it directs users to the correct documentation.
* Updated the Quick Setup wizard to provide a more accurate message, eliminating misleading connection failure notifications when adding the local environment via Agent deployment.
* Resolved an issue where deleting a Docker Swarm agent stack caused continuous error messages in logs [portainer/portainer#7937](https://github.com/portainer/portainer/issues/7937)
* Resolved an issue where a Swarm stack failed to restart after being stopped when using private images. [portainer/portainer#8262](https://github.com/portainer/portainer/issues/8262)

### Docker

* Introduced the ability to trigger reload of image up to date indicators in the UI.
* Fixed issue where Docker Images List breaks when an image has no tags.
* Resolved inconsistencies between image up to date indicators of Docker Container List, Stack List and Stack Details screens.

### Kubernetes

* Introduced warning that Civo KaaS provisioning for a Kubernetes 1.27+ cluster on Extra Small node size may no longer complete as the compute resources are now too limited for required workloads.
* Ensured that, when enabling addons on a MicroK8s cluster during initial set-up of that cluster, any errors that arise are now shown in the UI.
* Ensured that, when enabling addons on a MicroK8s cluster post set-up of that cluster, any errors that arise are now shown in the UI.
* Disabled GKE functionality's Google API client telemetry.
* Updated the version of the kubectl client in the kubectl shell console. [portainer/portainer#11303](https://github.com/portainer/portainer/issues/11303)
* Fixed the stripping of labels from certain Kubernetes resources - Ingress, ConfigMap or Secret - when form-editing them. [portainer/portainer#11147](https://github.com/portainer/portainer/issues/11147)
* Resolved inconsistency in Kubernetes deployment behavior between standard and async agents regarding the 'Use namespace(s) specified from manifest' switch
* Fixed an issue where namespaces 'set to system' from within Portainer weren't being detected as system. [portainer/portainer#11146](https://github.com/portainer/portainer/issues/11146)
* Fixed 'Unable to determine which association to use to convert form' error when adding a service to a Kubernetes pod that had been deployed external to Portainer. [portainer/portainer#11136](https://github.com/portainer/portainer/issues/11136)
* Fixed an issue introduced in 2.19.0 where a Kubernetes application deployed from Git required re-entry of Git credentials when changing the deployment.
* Corrected a minor UI issue introduced in 2.19.0, where, on create of Kubernetes application, if the user scrolled down and clicked 'Add persisted folder' without populating name and image fields, the focus would jump up to the first empty required field. [portainer/portainer#11155](https://github.com/portainer/portainer/issues/11155)
* Fixed an issue introduced in 2.19 in the ConfigMaps and Secrets lists where a check was no longer made against them for deployments of type Pod and hence an 'Unused' badge in those instances was then not shown. [portainer/portainer#11145](https://github.com/portainer/portainer/issues/11145)
* Fixed a 'this.formValues.Services is undefined' error that was shown when editing a pod created via manifest. [portainer/portainer#11152](https://github.com/portainer/portainer/issues/11152)
* Resolved an issue where ConfigMaps and Secrets created via manifest were incorrectly shown with the 'External' badge. [portainer/portainer#11169](https://github.com/portainer/portainer/issues/11169)
* Fixed issues that occurred when creating a Kubernetes namespace after disabling cluster's over-commit setting, including "Value must be between 0 and -x." warning that was incorrectly shown.
* Introduced a per-user option to enable five-minute data caching for non-edge Kubernetes environments - to improve performance. [portainer/portainer#11118](https://github.com/portainer/portainer/issues/11118)
* Resolved an issue with deploying of an edge stack to a Kubernetes async device failing.
* Fixed the Kubernetes Application details screen not showing referenced resources for an app that had used 'envFrom:' in its manifest to load an entire ConfigMap or Secret as environment variables instead of referencing individual values via 'valueFrom:'. [portainer/portainer#11144](https://github.com/portainer/portainer/issues/11144)
* Introduced a setting to turn off the Stacks functionality within the Kubernetes side of Portainer. [portainer/portainer#11119](https://github.com/portainer/portainer/issues/11119)
* Renamed the Kubernetes Advanced Deployment screen to be 'Create from Manifest'. [portainer/portainer#11128](https://github.com/portainer/portainer/issues/11128)
* Corrected display of a very high 'CPU used' value in the Kubernetes Cluster details screen when micro-CPU units were being used. [portainer/portainer#11154](https://github.com/portainer/portainer/issues/11154)
* DEPRECATED API endpoint `GET+POST /endpoints/{id}/kubernetes/helm/repositories`, MOVED Helm UI option to Advanced Deployment/Create from Manifest screen + now allow users to delete their Helm repos. New endpoint `GET+POST /users/{id}/helm/repositories` added. [portainer/portainer#11127](https://github.com/portainer/portainer/issues/11127)
* Introduced an option to enforce admin-only viewing/editing of Kubernetes Secret contents in the UI (where the user did not create that Secret).
* Resolved issues that occurred around editing a Kubernetes application when a namespace had resource quotas set, where the application's (pre-edit) existing resource usage was not being taken into account. [portainer/portainer#11143](https://github.com/portainer/portainer/issues/11143)
* Introduced a change so that, on deletion of an ECR or other registry, any related Kubernetes registry secret will now be removed. Note that this type of secret is auto created when assigning a registry to a namespace in a Kubernetes environment. [portainer/portainer#11158](https://github.com/portainer/portainer/issues/11158)
* Migrated the Kubernetes Application Details screen's YAML, Events and Containers sections plus any of the screen's remaining code from Angular to React. [portainer/portainer#11121](https://github.com/portainer/portainer/issues/11121)
* Fixed an issue around the display of incorrect search results for Kubernetes applications that are exposed via an ingress. [portainer/portainer#11160](https://github.com/portainer/portainer/issues/11160)
* Corrected the Kubernetes Volume Details screen to show the Shared Access Policy of the Volume rather than (erroneously) of the StorageClass. [portainer/portainer#11163](https://github.com/portainer/portainer/issues/11163)
* Corrected the deploying of a Kubernetes Daemonset with shared storage so that RWX access is granted to the Persistent Volume Claim, as relevant. [portainer/portainer#11168](https://github.com/portainer/portainer/issues/11168)
* Migrated the Kubernetes Cluster Setup screen from Angular to React and improved loading of its elements. [portainer/portainer#11122](https://github.com/portainer/portainer/issues/11122)
* Introduced a change so that, on assigning a user access to a Kubernetes environment that is down, the access is enabled when the environment next connects. [portainer/portainer#11157](https://github.com/portainer/portainer/issues/11157)
* Fixed a console error that could arise in the Kubernetes Add/Edit Application screen when updating resource sliders. [portainer/portainer#11159](https://github.com/portainer/portainer/issues/11159)
* Resolved error shown on editing a Kubernetes namespace when the cluster's 'Allow resource over-commit' setting had been turned off where the namespace had originally been created when the cluster's setting was on.
* Corrected the labelling of the Stack field in the Kubernetes Advanced Deployment (now 'Create from Manifest') screen. Also clarified the labelling of Namespace and Name concepts. [portainer/portainer#11120](https://github.com/portainer/portainer/issues/11120)
* Introduced new screen for listing, searching and deleting Kubernetes Cluster Roles and their Bindings.
* Introduced new screen for listing, searching and deleting Kubernetes Roles and their Bindings.
* Updated the Ingress list screen to indicate system resources correctly. [portainer/portainer#11162](https://github.com/portainer/portainer/issues/11162)
* Fixed incorrect display of an error message when adding a Kubernetes secret under certain circumstances. [portainer/portainer#11156](https://github.com/portainer/portainer/issues/11156)
* Made changes to allow stopping of a replicated Kubernetes application by scaling it to zero instances. [portainer/portainer#11117](https://github.com/portainer/portainer/issues/11117)
* Introduced new screen for listing, searching and deleting Kubernetes Service Accounts.
* Migrated most of the components of the Kubernetes Create and Edit application screens from Angular to React. [portainer/portainer#11123](https://github.com/portainer/portainer/issues/11123)
* Migrated the Kubernetes Add Namespace screen from Angular to React. [portainer/portainer#11124](https://github.com/portainer/portainer/issues/11124)

### KaaS

* Ensured Kubernetes 1.28 is supported with Linode Kubernetes Engine (LKE) provisioning of KaaS clusters.
* Ensured Kubernetes 1.29 is supported with DigitalOcean Kubernetes (DOKS) provisioning of KaaS clusters.
* Applied updates and ensured Kubernetes 1.29 is supported with Amazon Elastic Kubernetes Service (EKS) provisioning of KaaS clusters.
* Ensured Kubernetes 1.28 is supported with Civo Kubernetes provisioning of KaaS clusters.
* Ensured Kubernetes 1.28 is supported with Google Kubernetes Engine (GKE) provisioning of KaaS clusters.
* Ensured Kubernetes 1.27 is supported with Civo Kubernetes provisioning of KaaS clusters.
* Ensured Kubernetes 1.27 is supported with Linode Kubernetes Engine (LKE) provisioning of KaaS clusters.
* Ensured Kubernetes 1.28 is supported with Azure Kubernetes Service (AKS) provisioning of KaaS clusters.
* Ensured Kubernetes 1.28 is supported with DigitalOcean Kubernetes (DOKS) provisioning of KaaS clusters.
* Applied updates and ensured Kubernetes 1.28 is supported with Amazon Elastic Kubernetes Service (EKS) provisioning of KaaS clusters.
* Corrected access to Add Shared Credentials screen to prevent standard users from navigating to it (although note that it was already correctly disallowing add or view of credentials).
* Removed the possibility of a race condition occurring on use of the eksctl binary for Amazon EKS KaaS cluster provisioning.
* Ensured confirmed support of vanilla Kubernetes 1.29 clusters. [portainer/portainer#11129](https://github.com/portainer/portainer/issues/11129)

### MicroK8s

* Applied updates and ensured confirmed Kubernetes 1.29 support with creation of MicroK8s clusters.
* Corrected the grammar of a MicroK8s version retrieval error message.
* Ensured confirmed Kubernetes 1.28 support with creation of MicroK8s clusters.
* Introduced the ability for admins to enable the mayastor addon (that has prerequisites) for a MicroK8s cluster, and for admins and environments admins to enable or disable the mayastor addon for a MicroK8s cluster, after is has been provisioned.
* Introduced the ability for admins to enable the minio addon (that has prerequisites) for a MicroK8s cluster, and for admins and environments admins to enable or disable the minio addon for a MicroK8s cluster, after is has been provisioned.
* Resolved a Portainer and MicroK8s issue where, on installing Portainer Agent, the microk8s status command incorrectly shows Portainer Server as enabled. Note, this is fixed in fresh MicroK8s 1.29 installs (and is unrelated to the Portainer version).

### Portainer

* Fixed an issue where the "Force HTTPS only" toggle in the SSL certificates section was not functioning as expected.
* Fixed an issue that caused local stacks to be overwritten by orphaned stacks with the same name on the regular stack listing page
* Added version path to in-app documentation links to support long-term support (LTS) vs. short-term support (STS) releases. [portainer/portainer#11375](https://github.com/portainer/portainer/issues/11375)
* Fixed issue where users could erroneously edit web editor content in Git-based custom templates.
* Improved logging of in-app Kubernetes CE to BE upgrade.
* Resolved an issue with restoring from backup where portainer\_data was stored on a network volume. [portainer/portainer#11150](https://github.com/portainer/portainer/issues/11150)
* Fixed web editor errors when selecting between templates with identical Mustache variables and default values.
* Added experimental feature (behind a feature flag) to stream Syslog-formatted user activity and authentication logs to an external Security Information and Event Management (SIEM) system.
* Fixed issue where Bitbucket commit links were broken due to incorrect URL formatting.
* Resolved 'Unable to download backup' error that sometimes occurred when initiating database backup if portainer\_data was sited on a network volume. [portainer/portainer#11153](https://github.com/portainer/portainer/issues/11153)
* Fixed an issue where a webhook error occurred during the redeployment of a stack created from a private Git repository with relative path enabled.
* Fixed an issue where the cursor would jump to the end of the field after entering a character while editing environment variables for a stack.
* Fixed issue where sorting images by tags in the Images view of a Docker/Swarm environment had no effect, ensuring that images are now sorted in tag order when clicking on the Tags column header.
* Fixed an issue where users were unable to edit the YAML provided by a selected Custom template when deploying a stack.
* Improved GitOps auto updates to prevent piling up when the deployment time exceeds the polling interval.
* Resolved an issue with the upgrade and rollback process where the database was being backed up to a name that the rollback was not expecting. [portainer/portainer#10751](https://github.com/portainer/portainer/issues/10751)
* Fixed an issue with the Log viewer where lines that only contained numerical values were not shown.
* Fixed a minor typo in the 'Back up Portainer' settings section. [portainer/portainer#11138](https://github.com/portainer/portainer/issues/11138)
* Fixed a UI issue in Backup settings where, on reopening, they would revert to the default view after saving as S3.
* Fixed an invalid commit link in the Stack details screen that could occur if the original copy/pasted Git URL of the stack was a GitHub repo URL with an extension of .git. [portainer/portainer#11140](https://github.com/portainer/portainer/issues/11140)
* Fixed an issue where triggering a non-admin container's webhook changed the permission to admin-only.
* Resolved repository reference display discrepancy on deployed Environment Stacks details page
* Fixed inconsistency in container counting between the environment tile on the home page and the containers tile on the environment's Dashboard.
* Introducing 'Auto-Complete' branch selection for Git repositories in stack creation
* Introduced a UI fix to show a 'disabled input' cursor on hover of a toggle that's disabled for change (similar to existing disabled fill-ins, etc.). [portainer/portainer#11165](https://github.com/portainer/portainer/issues/11165)
* Provided information text to notify users that the GPU feature supports only Nvidia graphics cards, addressing any potential confusion
* Changed the "Upgrade Licenses" button to "Buy more nodes" for accurate representation of the action, as it reflects the purchase of additional licenses for expanding the number of nodes.
* Resolved an issue in GitLab registry handling, ensuring that Portainer continues loading images seamlessly despite errors such as deleted repositories, preventing 401 errors from affecting the display.
* Discontinued Nomad support in this release. Users won't be able to create new Nomad environments from the UI, and existing Nomad environments are hidden, ceasing their management through Portainer
* Enhanced version details popup to display the current Git commit hash and specific server environment variables for improved transparency and troubleshooting.
* Resolved an issue where an invalid IP address caused an error when the PORT environment variable was used during stack deployment
* Fixed a minor UI issue with the Environment -> Manage access screen enabling the 'Create access' button even though no changes had been made. [portainer/portainer#11141](https://github.com/portainer/portainer/issues/11141)
* Fixed issue where editing stacks or edge stacks didn't display relative path information. We now ensure clarity on the mounting point used, despite users being unable to modify the relative path during the editing process
* Adjusted license check-in.
* Enlarged a too-small font used in the Web editor's search/replace feature. [portainer/portainer#11175](https://github.com/portainer/portainer/issues/11175)
* Improved authentication and activity logs exported content.
* Improved security by storing sensitive JWT tokens in a more secure manner, enhancing protection for user authentication in the local browser storage
* Implemented improvements to restrict access to specific environment group details
* Enhanced measures to prevent global admins from accessing each other's tokens through direct HTTP requests. This ensures data privacy and aligns with intended access levels in the User Interface.
* Fixed an issue where the "Save Settings" button remained disabled after changing Advanced Options for a Git stack
* Disabled ability to edit orphaned stacks, ensuring consistency and preventing unintended modifications from the UI.
* Fixed issue where sorting by the "Updated" column in the Stacks view of a Docker environment incorrectly sorted based on the "Created" column instead.
* Implemented displaying of the exit code for containers in the Portainer UI.
* Improved Portainer navigation so all submenus now have their top-level option moved down to be the first option within their submenu and they always open to that. Implemented several other small menu improvements. [portainer/portainer#11116](https://github.com/portainer/portainer/issues/11116)
* Fixed an issue where the client secret field appeared blank when editing an OAuth configuration under 'Settings - Authentication'.
* Improved the functionality around changing a linked environment's IP address so Portainer Server no longer needs restarting for the update to apply. [portainer/portainer#11151](https://github.com/portainer/portainer/issues/11151)
* Improved security by adding a dropdown to hide environment variables in the stack UI on the details page, preventing potential exposure of sensitive information in public or share environments.
* Resolved an issue where information was missing on the registry tag view due to certain registry servers not providing manifest v1 json
* Resolved an issue where hiding a container would incorrectly label the associated container image as Unused. We now ensure accurate representation and address potential user confusion and unintended image deletion.
* Introduced 'noindex' meta-tag to the Portainer login page to denote to search engines that the page should not be indexed and served in search results. [portainer/portainer#11164](https://github.com/portainer/portainer/issues/11164)
* Fixed a console error that occurred when resizing the browser window on the containers page, particularly during an active exec console session.
* Improved styling and layout of headings and sub-headings throughout the user interface to improve legibility and hierarchy within pages. [portainer/portainer#11166](https://github.com/portainer/portainer/issues/11166)
* Resolved an issue in Container Logs with the Wrap Lines toggle on, where the log display could be mangled and end up unreadable.
* Introduced success notification that was missing when adding a user to a team. [portainer/portainer#11170](https://github.com/portainer/portainer/issues/11170)
* Improved styling of toggles throughout the user interface to make it clearer whether they are on or off, both when they are enabled for change or disabled for change. [portainer/portainer#11167](https://github.com/portainer/portainer/issues/11167)
* Improved high contrast mode so that field borders, box selector text and expiry banners are easier to make out. [portainer/portainer#11173](https://github.com/portainer/portainer/issues/11173)
* Improved high contrast mode to introduce a border around modals and tooltips so they are easier to distinguish from the rest of the screen. [portainer/portainer#11174](https://github.com/portainer/portainer/issues/11174)
* Resolved an issue where adding an environment to a newly created group didn't move it from 'available environment' to 'associated environment'; this now functions correctly.
* Introduced support for input, copy and paste of extended Unicode characters in Docker container and Kubernetes kubectl shell consoles. [portainer/portainer#5780](https://github.com/portainer/portainer/issues/5780)

### Development

* Updated Chisel to version 1.9 to facilitate the upgrade of Golang to version 1.20 for improved performance and compatibility
* Updated the logging library to restore colored console logs from the Portainer binary, enhancing readability and improving visibility for users.

### API Docs

* Corrected Swagger API documentation for the Stack image status endpoint, which should be `/stacks/{id}/images_status` (rather than `/docker/{environmentId}/stacks/{id}/images_status`).
* Corrected Swagger API documentation for the `GET+POST /users/{id}/tokens` endpoint so the example response describes the digest format correctly as a string, rather than (erroneously) as a list of integers. [portainer/portainer#11172](https://github.com/portainer/portainer/issues/11172)
* Corrected Swagger API documentation for the Docker container, service and stack image status endpoints so they now include example responses and a status explanation.
* Corrected Swagger API documentation for various /cloud (KaaS) endpoints and around an edge generate key endpoint.
* Corrected Swagger API documentation for the `GET /edge_update_schedules` endpoint so it now describes the includeEdgeStacks parameter, and the `/edge_update_schedules/active` endpoint which is a POST request but was (erroneously) described as a GET request.
* Corrected Swagger API documentation which listed creation of custom template POST endpoints as `/custom_templates/file` (or repository or string), but should have listed them as `/custom_templates/create/file` (or repository or string). [portainer/portainer#11149](https://github.com/portainer/portainer/issues/11149)
* Corrected API endpoint GET /webhooks documentation to describe filters parameter as a JSON string. [portainer/portainer#11148](https://github.com/portainer/portainer/issues/11148)
* Resolved further Swagger API documentation problems including issues definition of `GET /edge_stacks/{id}/logs/{endpoint_id}/file`, `GET /kubernetes/{id}/max_resource_limits` and `GET /kubernetes/{id}/namespaces/{namespace}/role_bindings`. [portainer/portainer#11171](https://github.com/portainer/portainer/issues/11171)
* Fixed Swagger API documentation to accurately reflect the path where the 'environmentId' should be passed, addressing inconsistencies between the documentation and the actual implementation.
* Updated Swagger API documentation to ensure consistency in property naming conventions by using PascalCase instead of camelCase.
* Fixed Swagger API documentation issue where the kaas version and system version APIs erroneously shared the same swaggo ID.

### REST API Changes

* Introduced a requirement to specify the current user's password when adding an API token via the UI or the `POST /users/{id}/tokens` API endpoint. [portainer/portainer#11126](https://github.com/portainer/portainer/issues/11126)
* Enhanced the system version API endpoint's response to now include the Portainer version type, distinguishing between Community Edition and Business Edition.

<details>

<summary>Deprecated Endpoints: 8</summary>

* `POST /custom_templates/file` Create a custom template
* `POST /custom_templates/repository` Create a custom template
* `POST /custom_templates/string` Create a custom template
* `GET /docker/{environmentId}/stacks/{id}/images_status` Fetch image status for stack
* `POST /cloud/credentials/{id}/delete` delete a cloud credential by ID
* `PUT /edge_configurations` Update an Edge Configuration
* `GET /edge_update_schedules/active` Fetches the list of Active Edge Update Schedules
* `POST /kubernetes/{id}/namespaces/{namespace}` Create a kubernetes namespace

</details>

<details>

<summary>New Endpoints: 33</summary>

* `POST /custom_templates/create/file` Create a custom template
* `POST /custom_templates/create/repository` Create a custom template
* `POST /custom_templates/create/string` Create a custom template
* `POST /docker/{environmentId}/containers/image_status/clear` Clear container image status cache
* `GET /docker/{environmentId}/images` Fetch images
* `POST /docker/{environmentId}/services/image_status/clear` Clear service image status cache
* `GET /edge_stacks/{id}/logs/{endpoint_id}/file` Downloads the available logs for a given edge stack and endpoint
* `POST /edge_stacks/parse_registries` Parse registries from a stack file
* `GET /kubernetes/{id}/cluster_role_bindings` Get a list of cluster role bindings
* `POST /kubernetes/{id}/cluster_role_bindings/delete` Delete the provided cluster role bindings
* `GET /kubernetes/{id}/cluster_roles` Get a list of cluster roles
* `POST /kubernetes/{id}/cluster_roles/delete` Delete the provided cluster roles
* `GET /kubernetes/{id}/max_resource_limits` Get max unused CPU and memory limits of all nodes within k8s cluster
* `GET /kubernetes/{id}/namespaces/{namespace}/configuration` Get ConfigMaps and Secrets
* `GET /kubernetes/{id}/namespaces/{namespace}/role_bindings` Get a list of role bindings
* `GET /kubernetes/{id}/namespaces/{namespace}/roles` Get a list of roles
* `GET /kubernetes/{id}/namespaces/{namespace}/service_accounts` Get a list of service accounts
* `POST /kubernetes/{id}/role_bindings/delete` Delete the provided role bindings
* `POST /kubernetes/{id}/roles/delete` Delete the provided roles
* `POST /kubernetes/{id}/service_accounts/delete` Delete the provided service accounts
* `PUT /settings/default_registry` Update Portainer default registry settings
* `GET /stacks/{id}/images_status` Fetch image status for stack
* `POST /stacks/image_status/clear` Clear stack image status cache
* `DELETE /stacks/name/{name}` Remove Kubernetes stacks by name
* `POST /templates/{id}/file` Get a template's file
* `GET /users/{id}/helm/repositories` List a users helm repositories
* `POST /users/{id}/helm/repositories` Create a user helm repository
* `DELETE /users/{id}/helm/repositories/{repositoryID}` Delete a users helm repository
* `GET /users/me` Inspect the current user user
* `DELETE /cloud/credentials/{id}` Delete a cloud credential
* `PUT /edge_configurations/{id}` Update an Edge Configuration
* `POST /edge_update_schedules/active` Fetches the list of Active Edge Update Schedules
* `POST /kubernetes/{id}/namespaces` Create a kubernetes namespace

</details>

<details>

<summary>Modified Endpoints: 19</summary>

* `POST /auth` Authenticate
* `POST /auth/oauth/validate` Authenticate with OAuth
* `POST /cloud/{provider}/cluster` Provision a new KaaS cluster and create an environment
* `GET /cloud/{provider}/info` Get information about the provisioning options for a cloud provider.
* `GET /custom_templates` List available custom templates
* `POST /custom_templates` Create a custom template
* `PUT /custom_templates/{id}` Update a template
* `GET /custom_templates/{id}` Inspect a custom template
* `GET /docker/{environmentId}/containers/{containerId}/image_status` Fetch image status for container
* `GET /docker/{environmentId}/services/{serviceId}/image_status` Fetch image status for service
* `GET /edge_configurations` List available Edge Configurations
* `POST /edge_configurations` Create an Edge Configuration
* `GET /edge_configurations/{id}` Inspect an Edge configuration
* `GET /edge_groups` list EdgeGroups
* `GET /edge_jobs` Fetch EdgeJobs list
* `GET /edge_jobs/{id}` Inspect an EdgeJob
* `POST /edge_jobs/{id}` Update an EdgeJob
* `GET /edge_stacks` Fetches the list of EdgeStacks
* `POST /edge_stacks` Create an EdgeStack

</details>

## Release 2.19.4

December 6, 2023

### Swarm

* Resolved the inability to change the replica set for a swarm service, addressing errors related to invalid CredentialSpec (A refresh of your browser cache may be required) [portainer/portainer#10702](https://github.com/portainer/portainer/issues/10702)

## Release 2.19.3

November 22, 2023

### Portainer

* Resolved an issue where polling and webhook methods failed to update the Stack [portainer/portainer#10673](https://github.com/portainer/portainer/issues/10673)

## Release 2.19.2

November 13, 2023

### Breaking changes

* Deprecation notice of Nomad support in next minor release.

### Edge

* Fixed bug around Update and Rollback menu showing when Edge Compute feature is disabled.
* Resolved an issue where edge group details were missing from the update and rollback table.
* Resolved an issue where searching on the Update & Rollback page caused the screen to go blank
* Resolved an issue where users were unable to delete any failed remote update scheduler entries.
* Resolved an issue where edge stack rollback and pause updates remained stuck in the pending state
* Resolved an issue where the update scheduler would stay in a "pending" state indefinitely, even when some edge agents were already running the latest version in the target edge group.
* Added a deprecation notice to inform users about the upcoming removal of Nomad support in next minor release.

### Swarm

* Resolved an issue where the Docker service page could not load correctly when the deployment was created using the GMSA credential spec parameter. [portainer/portainer#10571](https://github.com/portainer/portainer/issues/10571)

### Kubernetes

* Introduced the ability for Helm chart repository searching and registry browsing to operate behind a forward proxy. [portainer/portainer#10432](https://github.com/portainer/portainer/issues/10432)

### Portainer

* Improved security around non-admin user environment information access. [portainer/portainer#10434](https://github.com/portainer/portainer/issues/10434)
* Fixed 'unable to upgrade' error that could potentially occur when upgrading from CE to BE.
* Resolved an issue where stacks that were initially deployed from a template could not be modified. [portainer/portainer#10563](https://github.com/portainer/portainer/issues/10563)
* Resolved an issue where users couldn't define a proxy for the agent and edge agent when their network relied on a proxy for internet access. [portainer/portainer#10564](https://github.com/portainer/portainer/issues/10564)
* Resolved an issue where pulling and redeploying Git stacks took longer than expected. [portainer/portainer#10565](https://github.com/portainer/portainer/issues/10565)
* Resolved an issue where stacks triggered from webhooks were marked as inactive status, even though they were running as expected [portainer/portainer#10567](https://github.com/portainer/portainer/issues/10567)
* Improved storage efficiency by retaining only one copy of Git repositories for versioning, preventing excessive disk usage.
* Fixed an issue where authentication failures occurred when editing stacks deployed from Git repositories created with version 2.19.0 or 2.19.1.
* Fixed an issue introduced in 2.19.0 when deploying from a custom template that was set up via API, where defined mustache variables are not always being prompted for.
* Resolved an issue where users could interact with a console even after logging out from another tab in the browser [portainer/portainer#10568](https://github.com/portainer/portainer/issues/10568)
* Resolved an issue where there was no warning for version mismatch between the server and edge agent, now UI clearly indicates matching server and edge agent versions are required for feature availability. [portainer/portainer#10569](https://github.com/portainer/portainer/issues/10569)
* Resolved an issue where containers were not deleted when users removed them from asynchronous environments by browsing snapshots.

### REST API Changes

* Improved security around non-admin users and their permissions. [portainer/portainer#10434](https://github.com/portainer/portainer/issues/10434)

<details>

<summary>New Endpoints: 1</summary>

* POST `/edge_update_schedules/{id}`

</details>

<details>

<summary>Modified Endpoints: 3</summary>

* POST `/auth/logout`
  * Description changed from '**Access policy**: authenticated' to '**Access policy**: public'
* POST `/edge_update_schedules`
  * Responses changed
    * New response: `200`
    * Deleted response: `204`
* GET `/edge_update_schedules/previous_versions`
  * New query param: `environmentIds`
  * Deleted query param: `skipScheduleID`

</details>

## Release 2.19.1

September 20, 2023

### Breaking changes

* Changes to API format and checking of some requests - See [REST API Changes](#rest-api-changes) below for more details.

### Edge

* Resolved an issue with snapshots between Edge Agent versions 2.18.2 and Portainer Server 2.19.0, which caused dropping of remote commands in async mode due to mismatches.
* Database migration for edge URLs now includes a check to verify if the edge feature is enabled. This fix ensures a more accurate and controlled upgrade process.
* Fixed an issue where the migration of Edge Tunnel URLs was broken when the Portainer API URL did not contain a port.
* We've improved the transparency of Edge Agent update scheduler and rollback statuses. Now, you'll have clear explanations for each status, simplifying monitoring and management.
* We've added a info notice to clarify that the option to update edge agent from a private registry is exclusively available in Edge Agent version 2.18.1 or newer.
* Fixed an issue where edge devices in the waiting room were incorrectly counted as part of the dynamic edge group.

### Kubernetes

* Fixed an issue introduced in 2.19.0 where standard and read-only users could no longer view node stats on a Kubernetes cluster.
* Fixed an issue introduced in 2.19.0 where the Kubernetes Create Application screen no longer showed in the bottom of page summary when a Deployment would be created.

### MicroK8s

* Fixed an issue introduced in 2.19.0 where MicroK8s cluster creation would fail if the SSH access used a passworded login and sudo access required the password.

### Portainer

* Fixed an issue where backup files were missing the Chisel private key. This could have disrupted communication between the Portainer server and agent after a restoration from backup. [portainer/portainer#10335](https://github.com/portainer/portainer/issues/10335)
* Improved the upgrade process for the Portainer server, upgrade process now halts on database migration errors, preventing database version mismatches for a more stable environment. [portainer/portainer#10336](https://github.com/portainer/portainer/issues/10336)
* Fixed an issue when chatbot integration was enabled globally, where a user who then set a chatbot key could not subsequently clear out their key to turn off the feature for themselves.
* Fixed an issue introduced in 2.19.0 when the chatbot integration feature was enabled for a user, where container logs did not display in the log viewer unless in full-screen mode.
* Fixed an issue where webhooks were failing when updating a stack deployed from a private Git repository.
* We've added a backup reminder for in-app updates, ensuring data safety during the update process.
* Resolved issue where failed stack status persists after incorrect compose from Git. Now auto-recovers with the next successful update.
* Fixed an issue where usernames and passwords were being stored along with Git stack configurations when Git credentials were used.
* Fixed an issue where using spaces in an Organizational Unit (OU) or Common Name (CN) name caused incorrect data to be displayed in the Active Directory configuration.
* Fixed an issue where toggles could be activated outside of their intended component area, potentially leading to inadvertent toggling. [portainer/portainer#10324](https://github.com/portainer/portainer/issues/10324)

### REST API Changes

* Fixed API endpoints that were broken in the 2.19.0 release, ensuring that they retain their previous functionality. [portainer/portainer#10337](https://github.com/portainer/portainer/issues/10337)
* Fixed an issue introduced in 2.19.0 when Kubernetes environment metrics API features were enabled, where these features would return an 'Unable to reach metrics API' error.
* Introduced new format around the change of a user's password via API. [portainer/portainer#10326](https://github.com/portainer/portainer/issues/10326)
* Updated the checking around change of a user via API. [portainer/portainer#10326](https://github.com/portainer/portainer/issues/10326)

## Release 2.19.0

August 31, 2023

### Breaking changes

* Introduced the ability for admins and environment admins to enable/disable community addons on a MicroK8s cluster created via Portainer. Note: On upgrade to this release, existing MicroK8s clusters created via Portainer are set to allow community addons.
* A number of components/views have been migrated from Angular to React.
* Helm, eksctl, and docker-compose have been updated to newer versions.
* Internal versioning on stacks feature has introduced file structure changes in 2.19.
* We have addressed an API issue in which an incorrect parameter was being used for API endpoint `/edge_groups`. Users relying on the HasEdgeGroup parameter should now use HasEdgeJob to achieve the intended functionality.
* Select API endpoints are broken and will be restored in the next release:- see [REST API changes](#rest-api-changes) for specific details.

### Resolved CVEs

* Updated the Docker Compose binary to v2.20.2, to resolve CVEs. [portainer/portainer#10099](https://github.com/portainer/portainer/issues/10099)
* Updated the Helm binary to v3.12.2, to resolve CVEs. [portainer/portainer#10100](https://github.com/portainer/portainer/issues/10100)
* Resolve identified CVEs.
* Updated various packages to resolve CVEs. [portainer/portainer#9224](https://github.com/portainer/portainer/issues/9224)
* Updated various packages in the agent, to resolve CVEs.

### Edge

* Fixed an issue where the edge agent was getting disconnected due to user updates to their remote update scheduler.
* Resolved an issue where users were unable to create a rollback and subsequently edit it from the scheduler.
* Introduced visual enhancement of dynamic progress bar for clearer edge stack status tracking. Get real-time deployment progress at a glance.
* Fixed an issue where deploying a large volume edge stack triggered a 'URI too large' error. [portainer/portainer#10128](https://github.com/portainer/portainer/issues/10128)
* Resolved an issue where edge devices were not fully shown in the waiting room when the total amount exceeded 100
* Introducing new statuses - 'Running', 'Deploying', and 'Partially running' - for increased transparency in edge stack monitoring.
* Introduced staggered deployment & rollback for edge stacks. Update in stages, reduce risks & revert failed updates seamlessly.
* Introduced internal versioning & Git commit ID as edge stack version. Clearer version tracking for Git-deployed stacks.
* Added support for relative paths in Git-deployed edge stacks.
* Resolved an issue where the 'change windows setting' option was shifting outside of the div when a user was using a smaller screen
* Fixed an API issue where the incorrect parameter HasEdgeGroup was being used instead of HasEdgeJob for endpoint /edge\_groups. Users relying on the HasEdgeGroup parameter should now use HasEdgeJob to achieve the intended functionality.
* Introducing the ability to use environment variables for edge stack.
* Introducing a new feature: [GitOps Edge Configurations](https://docs.portainer.io/user/edge/stacks/add#gitops-edge-configurations), which simplify edge device configurations with GitOps. Effortlessly manage settings via version-controlled Git repositories for enhanced configuration control.
* Introducing the latest commit ID display in edge stacks. Perfect for GitOps updates, this feature lets you easily track your running version. Stay informed and up-to-date effortlessly.
* Introduced ability to push per-device configurations effortlessly. Bundle settings in a zip package, Portainer matches and delivers to edge devices. Simplify management, enhance precision.
* Fixed an issue where the count of edge stack deployments was incorrect when dealing with asynchronous devices exceeding 100.
* Fixed an issue where the order of the list changed while logs were being retrieved, and where previously cleared logs were reappearing after retrieving logs for a different environment.
* Improved logging for edge agent when polling fails. This enhancement provides more informative and detailed logs when polling encounters failures, aiding in quicker identification and resolution of issues. [portainer/portainer#10143](https://github.com/portainer/portainer/issues/10143)
* Introduced a feature that empowers you to associate edge devices with newly selected or dynamically generated meta values. Enhance flexibility and precision in device management with this innovative addition.
* Introduced an informative enhancement to the waiting room experience. With the addition of the 'Last Check-In' field, users now have valuable insights into when edge devices last communicated with the Portainer server.
* Introduced ability to remove edge devices that you no longer want sitting in the waiting room. This feature empowers you with streamlined waiting room management, enabling you to maintain a dynamic and optimised edge environment.
* Resolved an issue where editing an existing scheduler caused an error due to a missing edge stack on a related endpoint.
* Resolved an issue where users were able to create schedulers with an empty edge group, which is no longer allowed to ensure proper functionality and avoid potential errors [portainer/portainer#10149](https://github.com/portainer/portainer/issues/10149)
* Resolved an issue with Portainer tunnel server address validation error during migration. This fix ensures that when migrating, tunnel server addresses are validated correctly.
* Fixed an issue where Edge groups were incorrectly marked as 'in use' after a scheduler was executed.
* Addressed an issue where snapshot information was not reliable when the environment was offline. This fix ensures that snapshot information is now accurately presented even when the environment is offline.
* Resolved an issue where the count for acknowledged edge stacks was dropping after deployment.
* Resolved an issue where the edge agent default poll frequency selector was not lining up correctly [portainer/portainer#10150](https://github.com/portainer/portainer/issues/10150)
* Resolved an issue where users were unable to create an edge group when there were no members present in that group. Edge groups can now be created without requiring initial members, offering greater flexibility in edge device and configuration management. [portainer/portainer#10153](https://github.com/portainer/portainer/issues/10153)
* Introduce an enhancement to our snapshot creation process for edge devices which streamlines the snapshot creation experience, providing users with a more efficient and user-friendly way to capture snapshots on edge devices. [portainer/portainer#10154](https://github.com/portainer/portainer/issues/10154)
* Introduced ability to seamlessly browse snapshots for your asynchronous environment and access detailed stack information.
* Fixed an issue where environment files were not functioning properly in Git deployments for edge stacks. [portainer/portainer#10171](https://github.com/portainer/portainer/issues/10171)
* Introduced webhooks for edge stack, you can now set up webhooks for your edge stacks, enabling automated polling for GitOps updates. [portainer/portainer#10178](https://github.com/portainer/portainer/issues/10178)

### Docker

* Addressed an issue where the Docker client was not utilizing version negotiation. [portainer/portainer#10125](https://github.com/portainer/portainer/issues/10125)
* Resolved an issue where the image name was displayed incorrectly when a user tried to duplicate or edit a container [portainer/portainer#10126](https://github.com/portainer/portainer/issues/10126)
* Fixed an issue in the API where sending files to a Docker endpoint resulted in a panic. [portainer/portainer#10129](https://github.com/portainer/portainer/issues/10129)
* Resolved an issue with Docker Proxy's performance, resulting in improved overall performance and responsiveness when using the Docker Proxy feature. [portainer/portainer#10131](https://github.com/portainer/portainer/issues/10131)
* Resolved an issue in the Docker Container List where searching by published ports was no longer working. [portainer/portainer#6656](https://github.com/portainer/portainer/issues/6656)
* Resolved an issue where '.' was not allowed in the image name (but should be) when building a Docker image via the UI. [portainer/portainer#8047](https://github.com/portainer/portainer/issues/8047)
* Resolved some minor UI issues in Docker Services-related screens. [portainer/portainer#10117](https://github.com/portainer/portainer/issues/10117)

### Swarm

* Fixed an issue in Docker Swarm version 24.0.0 where image tags were not being displayed. [portainer/portainer#10134](https://github.com/portainer/portainer/issues/10134)
* Resolved an issue where clicking into the details page of a Swarm stack would redirect users to the service section instead of the top of the page [portainer/portainer#10151](https://github.com/portainer/portainer/issues/10151)

### Kubernetes

* Resolved an issue around Operator role users not being able to perform rolling restart, redeploy and rollback to previous version for Deployment, DaemonSet and StatefulSet resources.
* Resolved an issue introduced in 2.18 that prevented the use of Amazon EKS provisioning of a Kubernetes as a Service (KaaS) cluster.
* Fixed a Kubernetes environment issue when restricting access to the default namespace, where any other namespace with a resource quota may have the resource reservations of its apps incorrectly calculated, preventing standard users from editing the apps.
* Amended the path for the eksctl binary (used by Amazon EKS KaaS cluster provisioning functionality) to a new expected location.
* Adjusted Kubernetes Cluster setup screen's ingress settings to be clearer and to give info on ingress defaults. [portainer/portainer#10101](https://github.com/portainer/portainer/issues/10101)
* Resolved an issue with Kubernetes ECR image pull where the secret token was not updating on manifest deployment. [portainer/portainer#10119](https://github.com/portainer/portainer/issues/10119)
* Resolved an issue on use of the 'Restrict Proc Mount Types' Kubernetes pod security constraint where the restriction was not being applied.
* Resolved an issue in the Kubernetes Advanced deployment screen, where a backend panic could occur when deploying some invalid YAML manifests.
* Updated the link to Portainer documentation (following docs reorganization) for Kubernetes Add Environment via kubeconfig Import.
* Resolved an issue where Node stats for a Google Kubernetes Engine (GKE) cluster gave an error 'unable to retrieve node metrics'.
* Migrated the Kubernetes Add/Edit Application screen's Services section from Angular to React. [portainer/portainer#9235](https://github.com/portainer/portainer/issues/9235)
* Reintroduced the ability to specify and use (via Add/Edit Application) ingress defaults (hostname and annotations). [portainer/portainer#10030](https://github.com/portainer/portainer/issues/10030)
* Reintroduced the ability to publish via ingress from the Add/Edit Application screen. [portainer/portainer#10103](https://github.com/portainer/portainer/issues/10103)
* Introduced the ability to force setting of a note when creating/editing a Kubernetes application (via form), so it can immediately be labelled with its intended use.
* Introduced correct redirecting of the user, following deployment of a Kubernetes manifest. Previously the user was always returned to the Applications List but will now arrive back at the screen from which they accessed the Advanced Deployment function. [portainer/portainer#10115](https://github.com/portainer/portainer/issues/10115)
* Migrated the Kubernetes Application Details screen's Summary and Details sections from Angular to React. [portainer/portainer#10102](https://github.com/portainer/portainer/issues/10102)
* Introduced a loading spinner to the Add/Edit ingress screen's ingress class dropdown, to indicate that available options are still being retrieved. [portainer/portainer#10000](https://github.com/portainer/portainer/issues/10000)
* Resolved an issue that was occurring on the exposing of Portainer over a subpath, where Kubernetes Cluster Setup and other screens failed to load and reported an error. [portainer/portainer#10112](https://github.com/portainer/portainer/issues/10112)
* Resolved an issue around limiting of Kubernetes pod security constraints updates.
* Split the Kubernetes ConfigMaps & Secrets functionality in order to provide better performance and a clearer user experience. We now have separate tabs in the list screen and separate add/edit functions. [portainer/portainer#9222](https://github.com/portainer/portainer/issues/9222)
* Introduced the ability to set annotations against Kubernetes Services, so they can be configured for service meshes and other tools.
* Resolved an issue with Kubernetes pages where a warning showed in the browser console ('findDOMNode is deprecated in StrictMode') when resource assignment was first toggled on for the namespace. [portainer/portainer#10111](https://github.com/portainer/portainer/issues/10111)
* Updated BE Kubernetes Add/Edit Ingress screen to allow use of NodePort or LoadBalancer service types (in addition to existing ClusterIP).
* Updated Kubernetes ConfigMaps & Secrets terminology that was previously shown as Configurations, so as to align more clearly with Kubernetes. [portainer/portainer#10025](https://github.com/portainer/portainer/issues/10025)
* Introduced the ability to specify a manifest to be auto deployed to a Kubernetes cluster when connecting or provisioning one. This allows the environment to be initialized with users, namespaces, secrets, etc., as required.
* In the Dashboard screen of Kubernetes environments, Ingresses and Services panels have now been introduced, providing a count of these resources and an easy means to click through and access their list screens. [portainer/portainer#9223](https://github.com/portainer/portainer/issues/9223)
* Introduced showing of the error that occurs when a Kubernetes deployment is prevented by any pod security constraints that have been enabled.
* Migrated Kubernetes Application console page from Angular to React. [portainer/portainer#9177](https://github.com/portainer/portainer/issues/9177)
* Resolved a Node details issue where nodes showed incorrect role of 'Worker' due to deprecated 'node-role.kubernetes.io/master' K8s label (now 'control-plane'). Also where MicroK8s cluster nodes were incorrectly identified (though not due to labels). [portainer/portainer#10104](https://github.com/portainer/portainer/issues/10104)

### KaaS

* Ensured Kubernetes 1.27 is supported with Google Kubernetes Engine (GKE) provisioning of KaaS clusters.
* Ensured Kubernetes 1.26 is supported with Google Kubernetes Engine (GKE) provisioning of KaaS clusters.
* Ensured Kubernetes 1.27 is supported with Azure Kubernetes Service (AKS) provisioning of KaaS clusters.
* Ensured Kubernetes 1.27 is supported with Digital Ocean Kubernetes (DOKS) provisioning of KaaS clusters.
* Ensured Kubernetes 1.26 is supported with Linode Kubernetes Engine (LKE) provisioning of KaaS clusters.
* Applied updates and ensured Kubernetes 1.27 is supported with Amazon Elastic Kubernetes Service (EKS) provisioning of KaaS clusters.

### MicroK8s

* Added Beta support for MicroK8s version 1.28 when creating and managing MicroK8s clusters. Note that 1.27 is still the default option for now, as only limited testing of 1.28 has been performed.
* Introduced the ability for admins to enable the nfs addon (that has prerequisites) for a MicroK8s cluster, and for admins and environments admins to enable or disable the nfs addon for a MicroK8s cluster, after is has been provisioned.
* Introduced the ability for admins to enable the openebs addon (that has prerequisites) for a MicroK8s cluster, and for admins and environments admins to enable or disable the openebs addon for a MicroK8s cluster, after is has been provisioned.
* Introduced the ability for admins and environment admins to retrieve a status report on each control plane node of a MicroK8s cluster.
* Introduced the ability for admins and environment admins to enable and disable addons that require arguments and generally specify arguments for addons for a MicroK8s cluster.
* Introduced the ability for admins and environment admins to connect via SSH console to nodes in a MicroK8s cluster.
* Introduced the ability for admins and environment admins to enable/disable community addons on a MicroK8s cluster created via Portainer. Note: On upgrade to this release, existing MicroK8s clusters created via Portainer are set to allow community addons.
* Introduced the ability for admins and environment admins to enable or disable addons for a MicroK8s cluster, after it has been provisioned.
* Introduced the ability for admins, when removing a MicroK8s environment, to also delete the cluster on the nodes, leaving them in a fresh state, ready to begin again.
* Introduced the ability for admins and environment admins to horizontally scale up or down a MicroK8s cluster (i.e. add or remove nodes), after it has been provisioned.
* Introduced the ability for admins and environment admins to upgrade the version of a MicroK8s cluster.
* Added support for MicroK8s version 1.27 when creating MicroK8s clusters and removed warnings in the UI around a Metrics Server issue with MicroK8s 1.25 and 1.26, now that they've been patched to resolve the issue.
* Fixed an issue in Environment and Cluster Details screens for a MicroK8s cluster that failed to provision via Portainer. In this scenario, the display of enabled addons no longer triggers (whereas, it would previously still attempt it, causing a problem).
* Added info text to Kubernetes MicroK8s functionality to inform that nodes must be internet routable and open on certain ports.

### Portainer

* Fixed an issue where a bad gateway response occurred when updating an environment with an empty URL. [portainer/portainer#10123](https://github.com/portainer/portainer/issues/10123)
* Resolved an issue where users were unable to deploy a stack when utilising an image from a private GitLab registry. [portainer/portainer#10124](https://github.com/portainer/portainer/issues/10124)
* To identify Portainer submenus more clearly, their sub-options are now indented. [portainer/portainer#9216](https://github.com/portainer/portainer/issues/9216)
* Added a link to the Portainer Assistant/Chatbot settings taking you to an explanatory blogpost.
* Fixed an issue where the Portainer Assistant/Chatbot icon could eclipse list table screens' pagination.
* Introducing a new feature that enhances version tracking and clarity for stacks deployed from Git repositories.
* Resolved an issue around orphaned environments being included in the total count of nodes.
* Renamed "Automatic updates" in Git deployment section to "GitOps Updates" to clarify the feature at first glance for users. Please note this is a name change only and no functionality has been altered. [portainer/portainer#10175](https://github.com/portainer/portainer/issues/10175)
* Resolved an issue with the App Templates screen, where a Kubernetes icon was incorrectly showing for Docker Swarm stacks. Also updated the Swagger API documentation to detail the existence of a 'Compose edge stack' App Template (numbered 4) type. [portainer/portainer#10028](https://github.com/portainer/portainer/issues/10028)
* Fixed an issue where saving Git credentials and subsequently redeploying a stack resulted in an error.
* Resolved a minor UI issue where warning icons were smaller in size in multi-line warning messages. [portainer/portainer#10118](https://github.com/portainer/portainer/issues/10118)
* Fixed an issue where standard users were unable to create Azure Container Instances (ACI) resources. [portainer/portainer#10152](https://github.com/portainer/portainer/issues/10152)
* Fixed an issue where line break HTML tags were showing in some pop-up dialogs instead of actual line breaks. [portainer/portainer#9226](https://github.com/portainer/portainer/issues/9226)
* Improved App Templates page with enhanced cursor icon and tile highlighting [portainer/portainer#10136](https://github.com/portainer/portainer/issues/10136)
* Improved rolling back to CE from a CE to BE migration, by providing better logging and performing a check that the db file exists. [portainer/portainer#9225](https://github.com/portainer/portainer/issues/9225)
* Fixed an issue where edge devices were incorrectly counted as nodes while in the waiting room. Now, waiting room devices are excluded from node count, ensuring accurate resource allocation and adherence to policy.
* Fixed an issue where the primary environment remained permanently down after restoring from backup. [portainer/portainer#10137](https://github.com/portainer/portainer/issues/10137)
* Introduced validation to prevent the use of invalid names when creating or editing Kubernetes or Docker Custom Templates. [portainer/portainer#10113](https://github.com/portainer/portainer/issues/10113)
* Fixed an issue where the 'Skip TLS Verification' option was not functioning properly for custom templates. [portainer/portainer#10138](https://github.com/portainer/portainer/issues/10138)
* Resolved a minor UI issue where multi-line text-tip and form-error icons were incorrectly vertically center-aligned rather than top-aligned. [portainer/portainer#10118](https://github.com/portainer/portainer/issues/10118)
* Fixed an issue where the hover interaction for the environment tile on the homepage was missing [portainer/portainer#10136](https://github.com/portainer/portainer/issues/10136)
* Fixed a security issue where usernames and passwords were displayed in responses. [portainer/portainer#10140](https://github.com/portainer/portainer/issues/10140)
* Improved error logging in libhttp to provide more useful context. [portainer/portainer#10142](https://github.com/portainer/portainer/issues/10142)
* Addressed an issue where TLS handshake error messages were being logged, which should only occur when using the DEBUG log level. [portainer/portainer#10144](https://github.com/portainer/portainer/issues/10144)
* Fixed an issue where using spaces in an Organizational Unit (OU) or Common Name (CN) name caused incorrect data to be displayed in the Active Directory configuration.
* Fixed an issue where Git deployment did not synchronize authentication status.
* Resolved an issue where unnecessary snapshots were being loaded on the home page, leading to improved loading times and a smoother user experience [portainer/portainer#10147](https://github.com/portainer/portainer/issues/10147)
* Resolved an issue where users were not being notified about the proper referencing of their uploaded .env files, requiring them to now utilize "stack.env" for appropriate referencing [portainer/portainer#10148](https://github.com/portainer/portainer/issues/10148)
* Introduced a 'copy to clipboard' button to web editors within the Portainer UI. [portainer/portainer#10116](https://github.com/portainer/portainer/issues/10116)
* Introduced the ability to manage time in seconds or milliseconds for container logs, expanding your time management options beyond seconds for more insightful troubleshooting. [portainer/portainer#10176](https://github.com/portainer/portainer/issues/10176)
* Resolved a logging issue with database migrations, where, if an error occurred causing a rollback to the pre-upgrade version of the database, that error was no longer output to the console. [portainer/portainer#10110](https://github.com/portainer/portainer/issues/10110)
* Provided icons for 'image up to date' indicators (in place of the previous colored circles) shown in Docker Stacks, Services and Containers list screens. This improves accessibility for color-blind users.
* Resolved an issue that prevented users from stopping stacks with invalid project names during their upgrade from versions 2.6 or 2.7 to 2.13, 2.14, 2.15, 2.16, and subsequent versions. [portainer/portainer#10163](https://github.com/portainer/portainer/issues/10163)
* Resolved an issue that prevented users from deleting stacks with invalid project names during their upgrade from versions 2.6 or 2.7 to 2.13, 2.14, 2.15, 2.16, and subsequent versions. [portainer/portainer#10164](https://github.com/portainer/portainer/issues/10164)
* Resolved an issue where users were unable to browse image tags in a private Sonatype registry.
* Resolved an issue where mouse clicks were not functioning within the "Display Users" section of Active Directory under authentication settings.
* Resolved an issue where users were encountering difficulties when attempting to push images using a service principal account on Azure Registry. [portainer/portainer#10155](https://github.com/portainer/portainer/issues/10155)
* Fixed an issue where delete confirmation modals were absent for edge stacks, Docker images, environment groups, and tags. [portainer/portainer#10156](https://github.com/portainer/portainer/issues/10156)
* Fixed an issue where the creation of manifest file paths slice was incorrect. [portainer/portainer#10170](https://github.com/portainer/portainer/issues/10170)
* Resolved a minor grammatical issue with a log line recorded when the Docker image up to date indicator check runs but there are no registries defined.
* Community contribution - The enhancement ensures that the response rewrite operation is properly wrapped with a valid status check, contributing to a more robust and reliable system behavior. [portainer/portainer#2705](https://github.com/portainer/portainer/issues/2705)
* Fixed an issue where enabling GPU support on existing containers resulted in errors. [portainer/portainer#10174](https://github.com/portainer/portainer/issues/10174)
* Addressed an issue where users were unable to update the TLS certificate for the Docker API environment. [portainer/portainer#10166](https://github.com/portainer/portainer/issues/10166)
* Resolved an issue where incorrect AWS ECR icon was used when creating registry [portainer/portainer#10162](https://github.com/portainer/portainer/issues/10162)
* Added a feature that allows users to update to the latest Portainer Business Edition version directly from within the app
* Improved the way ANSI escape codes are handled in logs. With this enhancement, logs will now provide clearer and more readable information by effectively stripping out ANSI escape codes.
* Fixed a user interface issue where only up to 100 groups were being displayed. [portainer/portainer#10160](https://github.com/portainer/portainer/issues/10160)
* Addressed an issue where using incorrect Azure registry credentials resulted in errors, even after updating with correct credentials, the issue persisted. [portainer/portainer#10159](https://github.com/portainer/portainer/issues/10159)
* Resolved an issue where custom templates created from Git were not being pulled again at deploy time. This improvement has also been extended to Kubernetes custom templates. [portainer/portainer#10157](https://github.com/portainer/portainer/issues/10157)

### Development

* Resolved an issue with new React version list screens where filter icons were not positioned next to the correct column heading but were abutting the next heading along. [portainer/portainer#10098](https://github.com/portainer/portainer/issues/10098)
* Applied changes to the helper-reset-password utility to prevent it being accidentally used with the Docker Desktop Extension version of Portainer (where it could break access to the Portainer instance). [portainer/portainer#10109](https://github.com/portainer/portainer/issues/10109)
* Replaced archived gorilla/securecookie library with just the function that we need extracted out. [portainer/portainer#10008](https://github.com/portainer/portainer/issues/10008)
* Transitioned Edge stack environments table to React, delivering a more dynamic user experience with modernized interface, improved performance, and interactive management. [portainer/portainer#10210](https://github.com/portainer/portainer/issues/10210)

### REST API Changes

* Corrected API method from 'GET' to 'POST' and path for generate edge key in Swagger API docs
* Documented 'excludeSnapshots' in Swagger API docs [portainer/portainer#10130](https://github.com/portainer/portainer/issues/10130)
* Documented webhook types in Swagger API docs [portainer/portainer#9121](https://github.com/portainer/portainer/issues/9121)
* Resolved a 2.0 validation error in our Swagger API documentation [portainer/portainer#10135](https://github.com/portainer/portainer/issues/10135)
* Corrected an error in our Swagger API documentation where 'EdgeTunnelServerAddress' was marked as required. It is now correctly marked as optional
* We have updated the response for /endpoint to correctly reference 'EdgeCheckinInterval' in line with the accurate API Swagger documentation [portainer/portainer#10139](https://github.com/portainer/portainer/issues/10139)
* Corrected missing type and 'file' to 'File' in Swagger API documentation for custom templates [portainer/portainer#10141](https://github.com/portainer/portainer/issues/10141)
* Added descriptions to the Swagger API documentation for Kubernetes API endpoints that were previously missing from the docs. [portainer/portainer#10106](https://github.com/portainer/portainer/issues/10106)
* Fixed an API issue where requests to create edge stacks with invalid deployment types were erroneously accepted [portainer/portainer#10168](https://github.com/portainer/portainer/issues/10168)
* Addressed an issue in the 'edgeStackCreate' API where sending an incorrect request resulted in a 500 error response instead of the expected 400 error. [portainer/portainer#10169](https://github.com/portainer/portainer/issues/10169)
* Fixed an issue in Swagger API documentation where 'endpointId' was incorrectly marked as optional. It is now correctly set as a required field [portainer/portainer#10173](https://github.com/portainer/portainer/issues/10173)
* Removed the incorrect documentation for the DELETE method on the license API, as it is not supported. Documented the correct way to perform the operation using the POST method on the license API in Swagger API documentation.
* Corrected Swagger API documentation for starting or stopping stacks [portainer/portainer#8001](https://github.com/portainer/portainer/issues/8001)
* Corrected 'ResourceId' and 'endpointId' as required instead of optional in Swagger API documentation for webhooks [portainer/portainer#9121](https://github.com/portainer/portainer/issues/9121)
* Fixed the Swagger API documentation to require 'endpointId' when updating a stack [portainer/portainer#10161](https://github.com/portainer/portainer/issues/10161)
* Corrected 'Endpoints' to be listed in alphabetical order in Swagger API docs [portainer/portainer#10158](https://github.com/portainer/portainer/issues/10158)

<details>

<summary>Broken endpoints: 10</summary>

* GET `/cloud/microk8s/addons`
* POST `/cloud/{provider}`
* GET `/cloudcredentials`
* POST `/cloudcredentials`
* PUT `/cloudcredentials`
* POST `/custom_templates`
* POST `/edge_jobs`
* POST `/edge_stacks`
* GET `/endpoints/{id}/edge/generate-key`
* POST `/stacks`

</details>

<details>

<summary>New endpoints: 70</summary>

* GET `/cloud/credentials`
* POST `/cloud/credentials`
* PUT `/cloud/credentials`
* GET `/cloud/endpoints/{endpointid}/nodes/nodestatus`
* GET `/cloud/endpoints/{environmentid}/addons`
* POST `/cloud/endpoints/{environmentid}/addons`
* POST `/cloud/endpoints/{environmentid}/nodes/add`
* POST `/cloud/endpoints/{environmentid}/nodes/remove`
* POST `/cloud/endpoints/{environmentid}/upgrade`
* GET `/cloud/endpoints/{environmentid}/version`
* POST `/cloud/testssh`
* POST `/custom_templates/file`
* POST `/custom_templates/repository`
* POST `/custom_templates/string`
* PUT `/custom_templates/{id}/git_fetch`
* GET `/edge_configurations`
* POST `/edge_configurations`
* PUT `/edge_configurations`
* DELETE `/edge_configurations/{id}`
* GET `/edge_configurations/{id}`
* GET `/edge_configurations/{id}/files`
* PUT `/edge_configurations/{id}/{state}`
* POST `/edge_jobs/create/file`
* POST `/edge_jobs/create/string`
* POST `/edge_stacks/create/file`
* POST `/edge_stacks/create/repository`
* POST `/edge_stacks/create/string`
* POST `/edge_stacks/webhooks/{webhookID}`
* PUT `/edge_stacks/{id}/git`
* GET `/edge_stacks/{id}/stagger/status`
* POST `/endpoints/edge/generate-key`
* PUT `/endpoints/relations`
* POST `/gitops/repo/file/preview`
* GET `/kubernetes/{endpointId}/opa`
* GET `/kubernetes/{id}/ingresscontrollers`
* PUT `/kubernetes/{id}/ingresscontrollers`
* POST `/kubernetes/{id}/ingresses/delete`
* GET `/kubernetes/{id}/metrics/nodes`
* GET `/kubernetes/{id}/metrics/nodes/{name}`
* GET `/kubernetes/{id}/metrics/pods/{namespace}`
* GET `/kubernetes/{id}/metrics/pods/{namespace}/{name}`
* GET `/kubernetes/{id}/namespaces`
* DELETE `/kubernetes/{id}/namespaces/{namespace}`
* GET `/kubernetes/{id}/namespaces/{namespace}`
* POST `/kubernetes/{id}/namespaces/{namespace}`
* PUT `/kubernetes/{id}/namespaces/{namespace}`
* GET `/kubernetes/{id}/namespaces/{namespace}/ingresscontrollers`
* PUT `/kubernetes/{id}/namespaces/{namespace}/ingresscontrollers`
* GET `/kubernetes/{id}/namespaces/{namespace}/ingresses`
* POST `/kubernetes/{id}/namespaces/{namespace}/ingresses`
* PUT `/kubernetes/{id}/namespaces/{namespace}/ingresses`
* GET `/kubernetes/{id}/namespaces/{namespace}/services`
* POST `/kubernetes/{id}/namespaces/{namespace}/services`
* PUT `/kubernetes/{id}/namespaces/{namespace}/services`
* PUT `/kubernetes/{id}/opa`
* POST `/kubernetes/{id}/services/delete`
* POST `/stacks/create/kubernetes/repository`
* POST `/stacks/create/kubernetes/string`
* POST `/stacks/create/kubernetes/url`
* POST `/stacks/create/standalone/file`
* POST `/stacks/create/standalone/repository`
* POST `/stacks/create/standalone/string`
* POST `/stacks/create/swarm/file`
* POST `/stacks/create/swarm/repository`
* POST `/stacks/create/swarm/string`
* POST `/system/update`
* POST `/webhooks/{id}`
* DELETE `/webhooks/{token}`
* PUT `/webhooks/{token}`
* GET `/websocket/microk8s-shell`

</details>

<details>

<summary>Modified endpoints: 56</summary>

* GET `/cloud/{provider}/info`
  * New path param: provider
  * Deleted query param: credentialId
* PUT `/custom_templates/{id}`
* GET `/docker/{environmentId}/containers/{containerID}/image_status`
  * New path param: containerId
  * New path param: environmentId
* GET `/docker/{environmentId}/services/{serviceID}/image_status`
  * New path param: environmentId
  * New path param: serviceId
* GET `/docker/{environmentId}/snapshot/containers/{containerId}`
  * New path param: containerId
* GET `/docker/{environmentId}/stacks/{id}/images_status`
  * New path param: environmentId
  * New path param: id
* PUT `/edge_stacks/{id}`
* GET `/edge_stacks/{id}/file`
  * New query param: commitHash
  * New query param: version
* PUT `/edge_stacks/{id}/status`
* DELETE `/edge_stacks/{id}/status/{endpoint_id}`
  * New path param: environmentId
  * Deprecated changed from false to true
* GET `/edge_update_schedules/previous_versions`
  * New query param: skipScheduleID
* DELETE `/edge_update_schedules/{id}`
  * New path param: id
* GET `/edge_update_schedules/{id}`
  * New path param: id
* GET `/endpoints`
  * New query param: edgeCheckInPassedSeconds
  * New query param: edgeStackStatus
  * New query param: excludeSnapshots
* POST `/endpoints`
* POST `/endpoints/edge/async`
  * Deleted path param: id
* DELETE `/endpoints/{id}`
  * Responses changed
    * New response: 403
* PUT `/endpoints/{id}`
* GET `/endpoints/{id}/edge/stacks/{stackId}`
  * New query param: version
* PUT `/endpoints/{id}/pools/{rpn}/access`
  * Description changed from 'update the access on the resource pool in the current environment **Access policy**: restricted' to 'update the access on the namespace in the current environment **Access policy**: restricted'
* POST `/fdo/configure/{guid}`
  * New path param: guid
* DELETE `/fdo/profiles/{id}`
  * New path param: id
* GET `/fdo/profiles/{id}`
  * New path param: id
* PUT `/fdo/profiles/{id}`
  * New path param: id
* POST `/fdo/profiles/{id}/duplicate`
  * New path param: id
* POST `/gitops/repo/files/search`
* GET `/kubernetes/config`
  * Description changed from 'Generates kubeconfig file enabling client communication with k8s api server **Access policy**: authenticated' to 'Generate a kubeconfig file enabling client communication with k8s api server **Access policy**: authenticated'
* PUT `/kubernetes/{endpointId}/opa`
  * New path param: environmentId
  * Deleted path param: id
* GET `/kubernetes/{id}/namespaces/{namespace}/applications`
  * New path param: namespace
  * Deleted query param: namespace
* GET `/kubernetes/{id}/opa`
  * Modified path param: id
    * Description changed from 'Environment(Endpoint) identifier' to 'Environment identifier'
* GET `/nomad/endpoints/{endpointID}/allocation/{id}/events`
  * New path param: environmentId
  * New path param: id
* GET `/nomad/endpoints/{endpointID}/allocation/{id}/logs`
  * New path param: environmentId
  * New path param: id
* GET `/nomad/endpoints/{endpointID}/dashboard`
  * New path param: environmentId
* GET `/nomad/endpoints/{endpointID}/jobs`
  * New path param: environmentId
* DELETE `/nomad/endpoints/{endpointID}/jobs/{id}`
  * New path param: environmentId
  * New path param: id
* GET `/nomad/endpoints/{endpointID}/leader`
  * New path param: environmentId
* POST `/open_amt/{id}/activate`
  * Modified path param: id
    * Description changed from 'Environment(Endpoint) identifier' to 'Environment identifier'
* POST `/open_amt/{id}/devices/{deviceId}/action`
  * New path param: deviceId
  * New path param: id
* POST `/open_amt/{id}/devices_features/{deviceId}`
  * New path param: deviceId
  * New path param: id
* GET `/open_amt/{id}/info`
  * New path param: id
* DELETE `/registries/{id}/ecr/repositories/{repositoryName}/tags`
  * New path param: repositoryName
* PUT `/settings`
* PUT `/ssl`
* POST `/stacks/webhooks/{webhookID}`
* DELETE `/stacks/{id}`
  * Modified query param: endpointId
    * Description changed from 'Environment(Endpoint) identifier used to remove an external stack (required when external is set to true)' to 'Environment identifier'
    * Required changed from false to true
* PUT `/stacks/{id}`
  * Modified query param: endpointId
    * Description changed from 'Stacks created before version 1.18.0 might not have an associated environment(endpoint) identifier. Use this optional parameter to set the environment(endpoint) identifier used by the stack.' to 'Environment identifier'
    * Required changed from false to true
* PUT `/stacks/{id}/associate`
  * Modified query param: endpointId
    * Description changed from 'Stacks created before version 1.18.0 might not have an associated environment(endpoint) identifier. Use this optional parameter to set the environment(endpoint) identifier used by the stack.' to 'Environment identifier'
* GET `/stacks/{id}/file`
  * New query param: commitHash
  * New query param: version
* POST `/stacks/{id}/start`
  * New query param: endpointId
* POST `/stacks/{id}/stop`
  * New query param: endpointId
* POST `/tags`
* GET `/webhooks`
  * Modified query param: EndpointID
    * Required changed from false to true
  * Modified query param: ResourceID
    * Required changed from false to true
* POST `/webhooks`
* PUT `/webhooks/{id}`
  * New path param: id
* PUT `/webhooks/{id}/reassign`
  * New path param: id
* POST `/webhooks/{token}`
  * Modified path param: token

</details>

## Release 2.18.4

July 7, 2023

This release includes an experimental ChatGPT integration. Although it promises exciting possibilities, it's in the early stages of development. We recommend its use for testing and development, and urge caution in production environments. We greatly appreciate your feedback and understanding during this phase. [portainer/portainer#9116](https://github.com/portainer/portainer/issues/9116)

### Resolved CVEs

<details>

<summary>Portainer dependencies</summary>

* CVE-2023-28840 [portainer/portainer#9058](https://github.com/portainer/portainer/issues/9058)

</details>

### Docker

* Upgraded Docker Compose version to v2.17.2 for Portainer Agent. [portainer/portainer#9095](https://github.com/portainer/portainer/issues/9095)
* Resolve a problem building Portainer due to an issue with v1.53.0 of golangci-lint. [portainer/portainer#9057](https://github.com/portainer/portainer/issues/9057)

### Swarm

* Resolved an issue where users were unable to migrate or duplicate their swarm stack. [portainer/portainer#9097](https://github.com/portainer/portainer/issues/9097)

### Portainer

* Resolved an issue where the static IP addresses in a macvlan were unexpectedly changed. [portainer/portainer#9101](https://github.com/portainer/portainer/issues/9101)
* Enhanced the user experience of the 'Skip TLS Verification' feature by adding a confirmation modal. [portainer/portainer#9098](https://github.com/portainer/portainer/issues/9098)
* Resolved an issue where recreate containers fail when it has a shared and external volumes. [portainer/portainer#9102](https://github.com/portainer/portainer/issues/9102)
* Fixed issue where registry credential does not sync between registry configuration page and registry details page.
* Fixed an issue around prompting for a new license.
* Improved the way node count shows for trial licenses.
* Resolved an issue where update or rollback was only executed when connection was re-established.
* Introduced a change to allow removal of all Portainer licenses.
* Fixed an issue where a warning banner was not always showing in the Homepage or Licenses page when licenses were close to expiring.

### REST API Changes

* Resolved an issue where the response from the API was inconsistent when querying all endpoints and a specific endpoint. [portainer/portainer#9096](https://github.com/portainer/portainer/issues/9096)
* Corrected 'container' to 'containers' in Swagger API docs (Business Edition).

## Release 2.18.3

May 22, 2023

In this release, we introduce an experimental ChatGPT integration. Although it promises exciting possibilities, it's in the early stages of development. We recommend its use for testing and development, and urge caution in production environments. We greatly appreciate your feedback and understanding during this phase.

### Edge

* Fixed issue preventing configuration of Portainer authentication settings with an alternative mTLS certificate
* Resolved issue causing edge agent to skip command processing during full snapshot resend

### Kubernetes

* Restored options and wording in the Kubernetes Advanced deployment screen's Automatic updates section, following regression from changes in 2.17. ([portainer/portainer#8950](https://github.com/portainer/portainer/issues/8950))

### Docker

* Resolved issue preventing correct display of network details when containers are running on an unexpected Docker swarm node. ([portainer/portainer#8981](https://github.com/portainer/portainer/issues/8981))

### Portainer

* Introduced ChatGPT integration as an experimental feature, currently not recommended for production environment use
* Fixed issue preventing LDAP server from creating a connection when using TLS 1.2. ([portainer/portainer#8980](https://github.com/portainer/portainer/issues/8980))
* Implemented minor UI changes to clarify existing experimental and beta features, ensuring accurate icon and wording display. ([portainer/portainer#8951](https://github.com/portainer/portainer/issues/8951))
* Corrected an issue causing the polling indicator to float incorrectly in UI when pulling Git repo list on the stack creation page. ([portainer/portainer#8982](https://github.com/portainer/portainer/issues/8982))
* Resolved syntax styling display issue in web editor. ([portainer/portainer#8984](https://github.com/portainer/portainer/issues/8984))
* Improved button color contrast in web editor. ([portainer/portainer#8985](https://github.com/portainer/portainer/issues/8985))
* Fixed visual hierarchy in web editor selection behavior. ([portainer/portainer#8986](https://github.com/portainer/portainer/issues/8986))

### REST API Changes

* Corrected 'team' to 'teams' in Swagger API docs. ([portainer/portainer#8983](https://github.com/portainer/portainer/issues/8983))

## Release 2.18.2

May 1, 2023

### Upgrade notice

* Users upgrading from 2.16.x should note that a bug was introduced then which prevented enforcing of TLS verifications. This has now been fixed but, in circumstances where certificates were not set up correctly and appeared to work due to the bug, you may now need to resolve the certificate issue or deliberately set the new ‘Skip verification’ toggle.

### Edge

* Fixed issue where users were unable to update their Edge Agent to the latest version because the corresponding option was not available when creating a scheduled update

### Kubernetes

* Increased potential success rate of updating Portainer with larger databases by changing Kubernetes manifest and Helm chart for Portainer to have `initialDelaySeconds` of 45 (sec) and `failureThreshold` of 3. [portainer/portainer#8860](https://github.com/portainer/portainer/issues/8860)

### Docker

* Fixed issue where users were unable to pull the latest image from the image details page [portainer/portainer#8847](https://github.com/portainer/portainer/issues/8847)

### Portainer

* Fixed issue where the option to skip TLS verification was missing when editing a stack created from git. Additionally, to adhere to security best practices, the option’s default value has been corrected to be set to off during migration [portainer/portainer#8853](https://github.com/portainer/portainer/issues/8853)
* Fixed issue where TLS verification was being skipped when creating / editing stacks created from git in version 2.16.x [portainer/portainer#8853](https://github.com/portainer/portainer/issues/8853)
* Fixed issue where the port number in the displayed webhook link was incorrect when Portainer was running behind a reverse proxy
* Resolved an issue with the updated web editor component, where it was not loading long YAML files correctly [portainer/portainer#8848](https://github.com/portainer/portainer/issues/8848)

## Release 2.18.1

April 18, 2023

Please note 2.18.0 is not publicly available. This release is 2.18.1 and is our next GA release since "2.17.x". This was done due to the need to provide an upgradeable preview image to a customer.

### Breaking changes

* For breaking changes in the API, please see the [REST API changes](#rest-api-changes) section.
* The Kompose functionality in Kubernetes has been removed since 2.17.0. Compose yaml can no longer be deployed on Kubernetes.
* Moved edge devices to the homepage view and removed edge devices menu option under edge compute.
* Add devices button is replaced with new UX in environment wizard.

### Resolved CVEs

<details>

<summary>Portainer dependencies</summary>

* SNYK-JS-BOOTBOX-174704
* SNYK-JS-FASTJSONPATCH-3182961
* SNYK-JS-MINIMATCH-3050818
* SNYK-JS-SANITIZEHTML-2957526
* SNYK-JS-XMLDOMXMLDOM-3042243
* SNYK-JS-XMLDOMXMLDOM-3092934
* CVE-2022-23471
* CVE-2021-41092
* CVE-2022-41717
* CVE-2022-32149
* CVE-2022-27664
* SNYK-GOLANG-GOLANGORGXNETHTTP2-3160322

</details>

<details>

<summary>Agent dependencies</summary>

* CVE-2022-41717
* SNYK-GOLANG-GOLANGORGXNETHTTP2-3160322

</details>

### Upgrade notice

* Since release 2.17.x we have added the ability to upgrade Edge Agents from Portainer when running on Docker Standalone / Docker Swarm / Nomad. Before using this feature we strongly advise to test this on a non-production environment first and have an alternative method available to connect to the Edge Device.
* Any clusters connected to Portainer of version 1.23 Kubernetes and above will have their Pod Security Policies (if they have any and are using the pod security constraints feature) updated to the Pod Security Standards

### Edge

* Introduced a retry policy for edge stack deployment to improve success rate
* Fixed issue where browse snapshot button was clickable for Kubernetes and Nomad edge agents in async mode
* Fixed issue where upgrading edge agent from ECR private registry using certificates failed
* Fixed issue when browsing async edge agents before first snapshot is received.
* Provide feature flag for FDO feature to be shown in UI [portainer/portainer#8696](https://github.com/portainer/portainer/issues/8696)
* Fixed issue when browsing non-existent async agent snapshot cause backend panic
* Fixed issue for remote update schedules error incorrectly displaying for non admin users
* Fixed the issue where the edge stack is not removed from edge agent when it has been deleted while edge agent is offline
* Fixed issue where live connect button is clickable for async environment when it shouldn't be [portainer/portainer#8697](https://github.com/portainer/portainer/issues/8697)
* Fixed issue where edge agent panics with malformed edge key
* Introduced ability to view container's environment variable when browsing snapshot
* Removed "Add Edge devices" from Edge Compute and introduced to Environment wizard by renaming Edge Agent to Edge Agent Standard and introduced Edge Agent Async UI options [portainer/portainer#8783](https://github.com/portainer/portainer/issues/8783)
* Fixed an issue where "copy token" button was missing from edge agent environment wizard [portainer/portainer#8554](https://github.com/portainer/portainer/issues/8554)
* Introduced remote updating edge agent from a private registry for docker standalone environment
* Introduced ability to assign group, edge groups and tags to edge environment when using AEEC script
* Fixed issue where live connect button is clickable for async environment when it shouldn't be [portainer/portainer#8697](https://github.com/portainer/portainer/issues/8697)
* Fixed issue where edge job logs was not retrieved correctly when edge groups contain async devices
* Changed default value for async check-in intervals from disabled to 1 minute to improve success rate of initial edge agent connection
* Renamed AEEC to "Auto onboarding" for better user understanding

### Kubernetes

* Introduced a new feature to allow creating of a MicroK8s Kubernetes cluster on existing machines.
* Improved performance of Kubernetes screens by adjusting rate limiting of Kubernetes go client. [portainer/portainer#8682](https://github.com/portainer/portainer/issues/8682)
* Fixed an issue when provisioning a Civo Kubernetes cluster with the Kubernetes version left as the latest, due to Civo introducing Talos as a new Kubernetes cluster type (instead of K3s on Alpine) which then only applied to the latest Kubernetes version.
* Improved Kubernetes Applications page performance by introducing a namespace filter. [portainer/portainer#8637](https://github.com/portainer/portainer/issues/8637)
* Improved Kubernetes Dashboard page performance. [portainer/portainer#8635](https://github.com/portainer/portainer/issues/8635)
* Improved the load time of various Kubernetes pages by removing existing API calls that retrieve namespace resource quota information, where they are not needed. [portainer/portainer#8571](https://github.com/portainer/portainer/issues/8571)
* Introduced the ability to set annotations against various different Kubernetes objects via the existing form pages.
* Introduced a new Services screen in Kubernetes environments to improve the visibility of all services that may exist in a cluster, and enable removing where they've inadvertently been left behind after manual removal of applications/deployments. [portainer/portainer#8613](https://github.com/portainer/portainer/issues/8613)
* Introduced the ability to upload an internal SSL/TLS certificate which can then be used to access a Helm repository hosted on a private server.
* Updated the pod security constraints feature to use newer OPA Gatekeeper 2.9 and moved the feature away from using Pod Security Policy resources with Kubernetes clusters of 1.23 and above (as they are now removed in Kubernetes 1.25 and above).
* Added migration to ensure existing pod security constraints work on environments with new Pod Security Standards of updated OPA Gatekeeper 2.9. This includes migrating edge environments on post-upgrade connect that may occur on clicking into via Homepage.
* Resolved an issue where pod security constraints were not being enforced (since 2.16).

### Docker

* Fixed issue where users are not able to re-create container with multiple networks
* Fixed issue with relative path not working when private registry is used, due to private registry credentials not passing to unpacker
* Resolved an issue where default storage detection logic that runs on Kubernetes environment connection was incorrectly running on Docker environment connection, and was therefore causing an error to be output to the logs (but was otherwise benign). [portainer/portainer#8606](https://github.com/portainer/portainer/issues/8606)
* Improved the existing UI around GPU support for Docker Standalone environments, introduced an overall toggle to turn this on or off and generally improved performance in Docker Containers and Stacks screens where GPU columns may show. [portainer/portainer#8646](https://github.com/portainer/portainer/issues/8646)
* Defaulted the image up to date indicator to on for new Docker environments added, or on upgrade from CE to BE for all Docker environments (now that caching and Ajax load performance improvements have been applied to this feature).
* Fixed an issue where stack name validation was missing, causing deployments to fail [portainer/portainer#8629](https://github.com/portainer/portainer/issues/8629)

### Nomad

* Fixed issue where Nomad Edge Agent install script causes error when using environment variables
* Introduced ability to upgrade edge agent in Nomad environment from within portainer UI

### Portainer

* Fixed issue where container log not showing when logs contain NULL value
* Added form validation for S3 compatible host field
* Resolved a minor UI issue with the Container details page's container health panel alignment and content label wrapping. [portainer/portainer#8636](https://github.com/portainer/portainer/issues/8636)
* Fixed a typo in the placeholder text for the access control component's Authorized users dropdown where it said 'teams' but should have said 'users'. [portainer/portainer#8565](https://github.com/portainer/portainer/issues/8565)
* Fixed issue where stack can not be deleted if relative path is removed from the mount point
* Fixed issue where logs in JSON format displayed incorrectly in log viewer [portainer/portainer#8787](https://github.com/portainer/portainer/issues/8787)
* Resolved an issue with slow performance of certain actions (such as bulk removing of unused container volumes or adding of Kubernetes ingresses) when a user has a long list of notifications (shown via the bell icon in the page header). [portainer/portainer#8604](https://github.com/portainer/portainer/issues/8604)
* Fixed issue where you can not connect or configure Azure private registry from Portainer while registry is empty
* Added release testing of ARM32 architecture for Portainer Agent
* Resolved an issue that occurred when updating user preferences. [portainer/portainer#8570](https://github.com/portainer/portainer/issues/8570)
* Introduced UI mechanism for automatic retrying of tunnel connection when it fails due to high latency [portainer/portainer#8784](https://github.com/portainer/portainer/issues/8784)
* Added certificate support of AWS IAM Role Anywhere authentication for Agent and Edge Agent [portainer/portainer#8789](https://github.com/portainer/portainer/issues/8789)
* Updated hide internal authentication prompt option to default to off
* Fixed issue where searching is not functional in associated edge environment when creating edge group [portainer/portainer#8589](https://github.com/portainer/portainer/issues/8589)
* Fixed issue with Docker Swarm environment where containers count weren't displaying correctly in homepage. [portainer/portainer#8695](https://github.com/portainer/portainer/issues/8695)
* Fixed issue where skipping https verification was default to true for Azure git deployment [portainer/portainer#8698](https://github.com/portainer/portainer/issues/8698)
* Fixed issue where TLS Min Version was not fully enforced [portainer/portainer#8788](https://github.com/portainer/portainer/issues/8788)
* Fixed a minor issue on restarting a container where the toaster pop-up message shown had an extraneous slash in front of the container name. [portainer/portainer#8563](https://github.com/portainer/portainer/issues/8563)
* Introduced ability to use different certificate for mTLS communication between Portainer server and agent.
* Fixed an issue while in dark mode, where, with any auto-filled text in fill-ins, the cursor completely disappeared until you started typing again. [portainer/portainer#8564](https://github.com/portainer/portainer/issues/8564)
* Resolved a minor issue in the Browse Registry screen on Kubernetes environments, where the Registries breadcrumb link would take non-admin users back to the Homepage instead of the Registries list screen.
* Provide feature flag for FDO feature to be shown in UI [portainer/portainer#8696](https://github.com/portainer/portainer/issues/8696)
* Fixed issue of missing requirement of TLS definition for endpoint creation and correct tagids parameter in swagger API [portainer/portainer#8780](https://github.com/portainer/portainer/issues/8780)
* Improved Edge Agent Health status indicator and keep consistency with API response [portainer/portainer#8781](https://github.com/portainer/portainer/issues/8781)
* Fixed issue where git deployment failed to edit or redeploy when compose path begin with slash [portainer/portainer#8782](https://github.com/portainer/portainer/issues/8782)
* Fixed an issue in the restore from backup function, where a timeout error can occur and Portainer does not restart with the backup restored. [portainer/portainer#8792](https://github.com/portainer/portainer/issues/8792)

### Development

* Improved the layering of the Portainer Dockerfile to ensure internal development-related aspects are excluded where possible. [portainer/portainer#8559](https://github.com/portainer/portainer/issues/8559)
* Migrated git deployment page form Angular to React [portainer/portainer#8785](https://github.com/portainer/portainer/issues/8785)
* Migrated code editor component from Angular to React [portainer/portainer#8786](https://github.com/portainer/portainer/issues/8786)
* Introduced Tailwind prettier which will group utility classes project-wide and order them in a recommended way, making it easier to work with them. [portainer/portainer#8560](https://github.com/portainer/portainer/issues/8560)
* Introduced replacement for bootbox with react components [portainer/portainer#8588](https://github.com/portainer/portainer/issues/8588)
* Improved the feature flag architecture to make it easier to use. [portainer/portainer#8562](https://github.com/portainer/portainer/issues/8562)
* Resolved incorrect usage of log.fatal to ensure the application exits only as necessary. [portainer/portainer#8561](https://github.com/portainer/portainer/issues/8561)

### REST API Changes

* Fixed the API Swagger/OpenAPI documentation for some IDs that were defined as strings but should be integers. [portainer/portainer#8794](https://github.com/portainer/portainer/issues/8794)
* Added to the API Swagger/OpenAPI documentation that you can upload a file to a Docker Standalone host when the host management feature is enabled. [portainer/portainer#8793](https://github.com/portainer/portainer/issues/8793)

<details>

<summary>New Endpoints: 2</summary>

* GET `/edge_update_schedules/previous_versions`
* POST `/sshkeygen`

</details>

<details>

<summary>Deleted Endpoints: 2</summary>

* GET `/system/info`
* POST `/system/upgrade`

</details>

<details>

<summary>Modified Endpoints: 39</summary>

* POST `/cloud/{provider}`
* POST `/cloudcredentials`
  * Description changed from 'Create a cloud credential **Access policy**: authenticated' to 'delete delete a cloud credential by ID **Access policy**: authenticated'
  * New query param: `id`
* POST `/custom_templates`
* PUT `/custom_templates/{id}`
* POST `/edge_groups`
* PUT `/edge_groups/{id}`
* POST `/edge_jobs`
* POST `/edge_jobs/{id}`
* POST `/edge_stacks`
* PUT `/edge_stacks/{id}`
* POST `/edge_update_schedules`
* GET `/edge_update_schedules/active`
* GET `/edge_update_schedules/agent_versions`
* POST `/endpoint_groups`
* PUT `/endpoint_groups/{id}`
* GET `/endpoints`
  * New query param: `edgeAsync`
  * Deleted query param: `edgeDevice`
  * Modified query param: `edgeDeviceUntrusted`
    * Description changed from 'if true, show only untrusted endpoints, if false show only trusted (relevant only for edge devices, and if edgeDevice is true)' to 'if true, show only untrusted edge agents, if false show only trusted edge agents (relevant only for edge agents)'
* POST `/endpoints`
* PUT `/endpoints/{id}`
* POST `/endpoints/{id}/docker/v2/browse/put`
  * Description changed from 'Upload a file under a specific path on the file system of an environment (endpoint). **Access policy**: authenticated' to 'Use this environment(endpoint) to upload TLS files. **Access policy**: administrator'
  * Responses changed
    * New response: `204`
    * Deleted response: `200`
* GET `/endpoints/{id}/kubernetes/helm`
  * Modified query param: `filter`
    * Required changed from `true` to `false`
  * Modified query param: `namespace`
    * Required changed from `true` to `false`
  * Modified query param: `selector`
    * Required changed from `true` to `false`
* DELETE `/endpoints/{id}/kubernetes/helm/{release}`
  * Modified query param: `namespace`
    * Required changed from `true` to `false`
* PUT `/endpoints/{id}/registries/{registryId}`
* PUT `/endpoints/{id}/settings`
* POST `/gitops/repo/files/search`
* POST `/gitops/repo/refs`
* POST `/ldap/admin-groups`
* POST `/ldap/check`
* POST `/ldap/groups`
* POST `/ldap/test`
* POST `/ldap/users`
* POST `/registries`
* PUT `/registries/{id}`
* POST `/resource_controls`
* PUT `/settings`
* POST `/stacks`
* POST `/team`
* POST `/webhooks`
* PUT `/webhooks/{id}`
* PUT `/webhooks/{id}/reassign`

</details>

## Release 2.17.1

February 22, 2023

### Resolved CVEs

* Resolved the false positive report of Portainer binaries from VirusTotal. [portainer/portainer#8519](https://github.com/portainer/portainer/issues/8519)

### Docker

* Fixed issue with recreating containers in the Portainer UI if they have been originally created via the CLI. [portainer/portainer#8507](https://github.com/portainer/portainer/issues/8507)

### Portainer

* Fixed an issue where upgrading to Business Edition leaves behind limited stack. [portainer/portainer#8516](https://github.com/portainer/portainer/issues/8516)
* Fixed an issue where Edge Agent updater leaves behind limited stack.
* Fixed grammar of placeholder for region field in S3 backup configuration. [portainer/portainer#8515](https://github.com/portainer/portainer/issues/8515)
* Fixed an issue where an error occurred for upgrading Portainer to 2.17.0 version when Docker engine version is 19.03. [portainer/portainer#8514](https://github.com/portainer/portainer/issues/8514)
* Fixed an issue where node enforcement message displayed incorrectly for trial license users.
* Fixed an issue where git credentials are not selected when editing stack deployed from git repository.

## Release 2.17.0

February 7, 2023

### Known issues

* Running Portainer with Docker Engine <= 19.03 (Docker API <= 1.40) will cause a fatal error similar to `failed initializing upgrade service | error="failed to determine container platform: failed to retrieve docker info: Error response from daemon: client version 1.41 is too new. Maximum supported API version is 1.40"`

### Breaking changes

* For breaking changes in the API, please see the [REST API changes](#rest-api-changes) section
* The Kompose functionality in Kubernetes has been removed. Compose yaml can no longer be deployed on Kubernetes.
* Moved Edge Devices to the homepage view and removed Edge Devices menu option under Edge Compute
* Add devices button is temporarily located on the Edge Compute Settings page

### Resolved CVEs

#### Portainer dependencies

* [SNYK-GOLANG-GITHUBCOMURFAVENEGRONI-1658297](https://security.snyk.io/vuln/SNYK-GOLANG-GITHUBCOMURFAVENEGRONI-1658297) - Negroni
* [CVE-2022-27191](https://nvd.nist.gov/vuln/detail/CVE-2022-27191) - golang.org/x/crypto/ssh in Go
* [GHSA-8c26-wmh5-6g9v](https://github.com/advisories/GHSA-8c26-wmh5-6g9v) - golang.org/x/crypto/ssh in Go
* [CVE-2022-27664](https://nvd.nist.gov/vuln/detail/CVE-2022-27664) - net/http in Go
* [CVE-2022-29526](https://nvd.nist.gov/vuln/detail/CVE-2022-29526) - Go
* [SNYK-JS-XMLDOMXMLDOM-3092934](https://security.snyk.io/vuln/SNYK-JS-XMLDOMXMLDOM-3092934) - javascript
* [CVE-2022-23806](https://nvd.nist.gov/vuln/detail/CVE-2022-23806) - kompose
* [CVE-2022-41720](https://nvd.nist.gov/vuln/detail/CVE-2022-41720) - kompose
* [CVE-2022-41716](https://nvd.nist.gov/vuln/detail/CVE-2022-41716) - kompose
* [CVE-2022-41715](https://nvd.nist.gov/vuln/detail/CVE-2022-41715) - kompose
* [CVE-2022-32189](https://nvd.nist.gov/vuln/detail/CVE-2022-32189) - kompose
* [CVE-2022-30635](https://nvd.nist.gov/vuln/detail/CVE-2022-30635) - kompose
* [CVE-2022-30634](https://nvd.nist.gov/vuln/detail/CVE-2022-30634) - kompose
* [CVE-2022-30633](https://nvd.nist.gov/vuln/detail/CVE-2022-30633) - kompose
* [CVE-2022-30632](https://nvd.nist.gov/vuln/detail/CVE-2022-30632) - kompose
* [CVE-2022-30631](https://nvd.nist.gov/vuln/detail/CVE-2022-30631) - kompose
* [CVE-2022-30630](https://nvd.nist.gov/vuln/detail/CVE-2022-30630) - kompose
* [CVE-2022-30580](https://nvd.nist.gov/vuln/detail/CVE-2022-30580) - kompose
* [CVE-2022-29804](https://nvd.nist.gov/vuln/detail/CVE-2022-29804) - kompose
* [CVE-2022-2880](https://nvd.nist.gov/vuln/detail/CVE-2022-2880) - kompose
* [CVE-2022-2879](https://nvd.nist.gov/vuln/detail/CVE-2022-2879) - kompose
* [CVE-2022-28327](https://nvd.nist.gov/vuln/detail/CVE-2022-28327) - kompose
* [CVE-2022-28131](https://nvd.nist.gov/vuln/detail/CVE-2022-28131) - kompose
* [CVE-2022-27664](https://nvd.nist.gov/vuln/detail/CVE-2022-27664) - kompose
* [CVE-2022-24921](https://nvd.nist.gov/vuln/detail/CVE-2022-24921) - kompose
* [CVE-2022-24675](https://nvd.nist.gov/vuln/detail/CVE-2022-24675) - kompose
* [CVE-2022-23772](https://nvd.nist.gov/vuln/detail/CVE-2022-23772) - kompose
* [CVE-2021-44716](https://nvd.nist.gov/vuln/detail/CVE-2021-44716) - kompose
* [CVE-2021-41772](https://nvd.nist.gov/vuln/detail/CVE-2021-41772) - kompose
* [CVE-2021-41771](https://nvd.nist.gov/vuln/detail/CVE-2021-41771) - kompose
* [CVE-2021-39293](https://nvd.nist.gov/vuln/detail/CVE-2021-39293) - kompose
* [CVE-2021-33198](https://nvd.nist.gov/vuln/detail/CVE-2021-33198) - kompose
* [CVE-2021-33196](https://nvd.nist.gov/vuln/detail/CVE-2021-33196) - kompose
* [CVE-2021-33195](https://nvd.nist.gov/vuln/detail/CVE-2021-33195) - kompose
* [CVE-2021-27918](https://nvd.nist.gov/vuln/detail/CVE-2021-27918) - kompose
* [CVE-2020-16845](https://nvd.nist.gov/vuln/detail/CVE-2020-16845) - kompose
* [CVE-2022-41717](https://nvd.nist.gov/vuln/detail/CVE-2022-41717) - kompose
* [CVE-2022-32148](https://nvd.nist.gov/vuln/detail/CVE-2022-32148) - kompose
* [CVE-2022-29526](https://nvd.nist.gov/vuln/detail/CVE-2022-29526) - kompose
* [CVE-2022-1962](https://nvd.nist.gov/vuln/detail/CVE-2022-1962) - kompose
* [CVE-2022-1705](https://nvd.nist.gov/vuln/detail/CVE-2022-1705) - kompose
* [CVE-2021-44717](https://nvd.nist.gov/vuln/detail/CVE-2021-44717) - kompose
* [CVE-2021-36221](https://nvd.nist.gov/vuln/detail/CVE-2021-36221) - kompose
* [CVE-2021-34558](https://nvd.nist.gov/vuln/detail/CVE-2021-34558) - kompose
* [CVE-2021-33197](https://nvd.nist.gov/vuln/detail/CVE-2021-33197) - kompose
* [CVE-2021-31525](https://nvd.nist.gov/vuln/detail/CVE-2021-31525) - kompose
* [CVE-2021-3114](https://nvd.nist.gov/vuln/detail/CVE-2021-3114) - kompose
* [CVE-2020-24553](https://nvd.nist.gov/vuln/detail/CVE-2020-24553) - kompose
* [CVE-2020-15586](https://nvd.nist.gov/vuln/detail/CVE-2020-15586) - kompose
* [CVE-2020-14039](https://nvd.nist.gov/vuln/detail/CVE-2020-14039) - kompose
* [CVE-2022-30629](https://nvd.nist.gov/vuln/detail/CVE-2022-30629) - kompose

#### Agent dependencies

* [CVE-2022-27664](https://nvd.nist.gov/vuln/detail/CVE-2022-27664) - net/http in Go

### Upgrade notice

* This release has added the ability to upgrade Edge Agents from Portainer when running on Docker Standalone. Before using this feature we strongly advise to test this on a non-production environment first and have an alternative method available to connect to the Edge Device.

### Edge

* Introduced the ability to remotely update edge agents from within Portainer
* Moved Edge Devices to the homepage view: [portainer/portainer#8333](https://github.com/portainer/portainer/issues/8333)
* Introduced the ability to browse snapshots of async edge environments from homepage view: [portainer/portainer#8336](https://github.com/portainer/portainer/issues/8336)
* Optimized performance for scaling large numbers of edge agents: [portainer/portainer#8349](https://github.com/portainer/portainer/issues/8349)
* Introduced option for pre-pull of images for edge stack deployment to increase deployment success rate
* Added edge group support in edge jobs to allow execution across many devices
* Introduce the ability to edit edge agent tunnel URL and API server URL from within Portainer
* Introduced improved environment tile layout to address consistency when edge devices moved to homepage: [portainer/portainer#8334](https://github.com/portainer/portainer/issues/8334)
* Clarified UX around polling intervals and poll frequency option in edge compute settings between async and normal edge agents.
* Added info text to waiting room view
* Fixed issue where edge stack incorrectly deployed to default namespace when there is a specified namespace defined in the manifest: [portainer/portainer#8346](https://github.com/portainer/portainer/issues/8346)
* Fixed issue where select all checkbox is missing for edge stack and edge job tables: [portainer/portainer#8029](https://github.com/portainer/portainer/issues/8029)
* Fixed issue with Edge device tags not showing on Create Edge Group screen: [portainer/portainer#7936](https://github.com/portainer/portainer/issues/7936)
* Fixed issue where delete edge device does not remove it from the edge groups mapping: [portainer/portainer#8348](https://github.com/portainer/portainer/issues/8348)
* Fixed issue where edge stack failed to deploy with private registry in async mode
* Fixed issue where actions icon under edit edge stack page is not consistent

### Kubernetes

* Introduced new log viewer to Portainer Business Edition
* Introduced the ability to edit the YAML manifest of Kubernetes objects and apply the changes via the Kubernetes patch function
* Introduced global and cluster-level options to allow enforcing of code-based deployment of Kubernetes objects, preventing the use of Portainer forms and other less easy-to-repeat workflows
* Introduced a new setting in the Cluster setup screen of a Kubernetes environment to allow enforcing of admin-only deploying of ingresses
* Introduced the ability to specify updates to existing environment variables of a deployment via query string parameters on the Kubernetes application redeploy webhook
* Added a rolling restart button to the Kube application UI
* Introduced a new rollout-restart parameter to Kube application redeploy webhooks to allow remote initiating of zero-downtime deployment rolling restarts
* Introduced an alternate means of authenticating connections to the Google Cloud platform (used by our KaaS provisioning of Google Kubernetes Engine environments), following their deprecation of the gcp auth plugin in Kubernetes v1.22 and removal in v1.26
* Introduced experimental Kubernetes functionality (behind a feature flag) to allow installing of MicroK8s to existing machines
* The Kubernetes deployment option for docker-compose format manifests and the Kompose conversion tool that enabled this have now been removed due to long-standing Common Vulnerabilities and Exposures (CVEs) in Kompose: [portainer/portainer#8355](https://github.com/portainer/portainer/issues/8355)
* Improved the explanatory tooltips and info text for Kube application automatic updates functionality: [portainer/portainer#8223](https://github.com/portainer/portainer/issues/8223)
* Updated Kubernetes as a Service (KaaS) cluster provisioning to use the latest eksctl tool for the AWS EKS platform, and support up to v1.23 of Kubernetes (use of this version was previously failing)
* Resolved an issue where Kubernetes secrets were no longer shown in an expand panel for each application listed in the Applications list screen: [portainer/portainer#8118](https://github.com/portainer/portainer/issues/8118)
* Improved config setting defaults when connecting clusters: ingress controllers (with a class) are auto detected/set as allowed, metrics API features setting is on (if metrics server is deployed), and storage classes with the 'default' annotation are on: [portainer/portainer#8240](https://github.com/portainer/portainer/issues/8240)
* The Kubernetes Operator role is not intended to have secrets update permission and hence, as a security consideration, this permission is now removed from Portainer
* Corrected the look of the fallback icon used for Helm charts that don't have their own icon: [portainer/portainer#8116](https://github.com/portainer/portainer/issues/8116)
* Made a change to default the resource quota's resource assignment setting to off for new Kubernetes namespaces but always show the toggle (although it can be disabled for change if the cluster's (BE only) allow over-commit setting is off): [portainer/portainer#8122](https://github.com/portainer/portainer/issues/8122)
* In the Kubernetes Add ingress screen, corrected the namespace selection dropdown to only show those that the user has access to: [portainer/portainer#8150](https://github.com/portainer/portainer/issues/8150)
* Added a check in Kube Cluster setup and Namespace -> Manage access to see if Kube RBAC addon is enabled in the cluster, and if not, show a warning that Portainer RBAC functionality will be limited. Warning also gives info on enabling RBAC in the cluster: [portainer/portainer#8171](https://github.com/portainer/portainer/issues/8171)
* Resolved an issue that was causing an 'Unable to get k8s environment access' error on deleting of a Kubernetes edge environment
* When connecting a Kubernetes environment to Portainer via kubeconfig import, stop deleting of any extant 'portainer' namespace in the cluster
* When using Kubernetes (KaaS) cluster provisioning and choosing the Azure Kubernetes Service (AKS) option, only node size options that are valid for provisioning now show. Previously, there was at least one option which gave an error on use
* Resolved two scenarios where importing of the kubeconfig of a Kubernetes cluster raised an error that caused a stuck 'Deploying' status
* In Kube Create namespace and Namespace details screens, made the resource assignment toggle always visible - even when the cluster's resource over-commit option is off (when it will show but be disabled for change)
* Fixed an issue introduced in 2.16, where deploying of an ingress via the Portainer Add ingress form does not label the ingress object in the cluster with a Portainer 'internal' deployment label. Any deployment of ingress via Portainer should have this: [portainer/portainer#8337](https://github.com/portainer/portainer/issues/8337)
* Fixed an issue introduced in 2.16, where, when attaching a ConfigMap to an application being deployed via the Portainer Add application form, the ConfigMap is wrongly included as a Secret in the manifest and the deployment could therefore fail: [portainer/portainer#8323](https://github.com/portainer/portainer/issues/8323)
* Fixed an incorrect mention in the UI of a 'docker-compose file' which was showing when editing a Kube application deployed from git: [portainer/portainer#8228](https://github.com/portainer/portainer/issues/8228)
* Fixed an issue preventing adding of a Helm repo that has a redirect: [portainer/portainer#7892](https://github.com/portainer/portainer/issues/7892)
* Fixed an issue where the kubectl shell does not work when Istio Proxy is installed in the cluster: [portainer/portainer#8321](https://github.com/portainer/portainer/issues/8321)
* Fixed an issue introduced in 2.16 where the Kube Create namespace screen's CPU and Memory resource allocation max limits did not have other namespaces' resource amounts subtracted when the cluster's allow resource over-commit option was turned off

### Docker

* Introduced support of relative paths for volumes when creating a Docker Standalone or Swarm stack that uses a git repository. Support in edge stacks is excluded at present: [portainer/portainer#6390](https://github.com/portainer/portainer/issues/6390)
* Introduced new log viewer to Portainer Business Edition
* Introduced pull image param for stack webhook to turn pull-image on and off
* Introduced 24 hour caching for new image notification
* Upgraded docker compose to v2.13.0: [portainer/portainer#8289](https://github.com/portainer/portainer/issues/8289)
* Provided clarification and rewording in the UI around the 'Pull latest image' toggle in Stacks, Swarm Services and Service details update and Container recreate: [portainer/portainer#8226](https://github.com/portainer/portainer/issues/8226)
* Updated embedded docker binaries in Portainer and agent from 20.10.13 to 20.10.18: [portainer/portainer#8290](https://github.com/portainer/portainer/issues/8290)
* Fixed issue of not been able to associate stack created from other docker environments: [portainer/portainer#8030](https://github.com/portainer/portainer/issues/8030)
* Fixed issue where content overlap edge of screen and left column becomes too narrow: [portainer/portainer#8161](https://github.com/portainer/portainer/issues/8161)
* Fixed issue where default option for access control is not selected when editing public resource: [portainer/portainer#8162](https://github.com/portainer/portainer/issues/8162)
* Fixed incorrect wording for private box selector under user access control: [portainer/portainer#7969](https://github.com/portainer/portainer/issues/7969)
* Fixed issue where text input jumps to the end of the input box in repository form: [portainer/portainer#8214](https://github.com/portainer/portainer/issues/8214)
* Fixed issue where scrollbar always visible in web editor form regardless contents of web editor: [portainer/portainer#7968](https://github.com/portainer/portainer/issues/7968)
* Fixed issue where number of stopped container does not display in dashboard correctly: [portainer/portainer#7925](https://github.com/portainer/portainer/issues/7925)
* Fixed an issue where deleting a network, config or secret did not show a confirmation warning modal: [portainer/portainer#7920](https://github.com/portainer/portainer/issues/7920)
* Fixed an issue where a user cannot upload a stack file as a custom template: [portainer/portainer#7921](https://github.com/portainer/portainer/issues/7921)
* Fixed an issue where the old-style UI was still being used in a Docker template-related page: [portainer/portainer#7950](https://github.com/portainer/portainer/issues/7950)
* Fixed issue where container webhook URL always changed on each recreation
* Fixed issue where new image notification only relies on checking first digest which is not always accurate: [portainer/portainer#7148](https://github.com/portainer/portainer/issues/7148)

### Portainer

* Introduced support for S3 compatible hosts for backup and restore: [portainer/portainer#6555](https://github.com/portainer/portainer/issues/6555)
* Introduced support for GitHub container registry as a registry type
* On the header context sensitive help icon, the red dot notification has been removed. This was put there to highlight the new feature in 2.16: [portainer/portainer#8167](https://github.com/portainer/portainer/issues/8167)
* Updated Portainer dependencies of Business Edition
* Upgraded version of golang.org/x/net from v0.0.0 to v0.1.0 for agent: [portainer/portainer#8073](https://github.com/portainer/portainer/issues/8073)
* Upgraded jwt version to 4.4.2: [portainer/portainer#7970](https://github.com/portainer/portainer/issues/7970)
* Improved Portainer tooltips to allow them to stay open long enough for clicking of links and selecting of text in them. Also left-justified them for better readability: [portainer/portainer#8224](https://github.com/portainer/portainer/issues/8224)
* Resolved an issue related to revoking of user permissions: [portainer/portainer#8338](https://github.com/portainer/portainer/issues/8338)
* Fixed issue where password could be leaked to the log files when errors occur: [portainer/portainer#8343](https://github.com/portainer/portainer/issues/8343)
* Fixed issue when navigating to the login page log as a unique visitor in Matomo: [portainer/portainer#8344](https://github.com/portainer/portainer/issues/8344)
* Fixed an svg attribute height error in the page (visible via the browser console): [portainer/portainer#8105](https://github.com/portainer/portainer/issues/8105)
* Fixed typo where "occured" is used in error message instead of "occurred": [portainer/portainer#8027](https://github.com/portainer/portainer/issues/8027)
* Fixed issue where long notification is pushed out of table making it hard to read: [portainer/portainer#8215](https://github.com/portainer/portainer/issues/8215)
* Fixed incorrect link for other settings and agent setup: [portainer/portainer#8347](https://github.com/portainer/portainer/issues/8347)
* Fixed issue where deleted environment does not clear in table and sidebar when deleting current selected environment: [portainer/portainer#8291](https://github.com/portainer/portainer/issues/8291)
* Fixed issue where standard users were not able to change ownership to their own team: [portainer/portainer#8216](https://github.com/portainer/portainer/issues/8216)
* Fixed issue where user encountered an error by deleting tags associated to deleted environments: [portainer/portainer#8089](https://github.com/portainer/portainer/issues/8089)
* Fixed an issue where the 'hide for all users' button styling behaves differently in dark mode: [portainer/portainer#7926](https://github.com/portainer/portainer/issues/7926)
* Fixed a minor issue where the pages and items per page elements in data table pagination controls did not quite vertically align with each other: [portainer/portainer#8227](https://github.com/portainer/portainer/issues/8227)
* Fixed issue where team lead feature is unexpectedly enabled when external authentication is enabled with team sync: [portainer/portainer#7972](https://github.com/portainer/portainer/issues/7972)
* Fixed issue where response from API when creating edge environments wasn't clearly specifying that URL is compulsory: [portainer/portainer#7997](https://github.com/portainer/portainer/issues/7997)
* Fixed issue where internal authentication setting is not saved when switch from other authentication method without refreshing browser manually: [portainer/portainer#8028](https://github.com/portainer/portainer/issues/8028)
* Fixed issue where admin users are not able to delete expired or revoked license
* Fixed issue where user unable to remove group configuration with active directory authentication: [portainer/portainer#7558](https://github.com/portainer/portainer/issues/7558)
* Fixed issue where user is not removed from team when removed from LDAP group

### Nomad

* Fixed issue around task logs not loading if they are empty
* Fixed issue where old UI components were still being used for Nomad related pages

### Development

* Replaced Feather svg icon set with Lucide, a Feather fork that is actively maintained and has a larger and improved range of icons: [portainer/portainer#8121](https://github.com/portainer/portainer/issues/8121)
* Removed Font Awesome and all remaining references to it. All icons are now svg-based: [portainer/portainer#8120](https://github.com/portainer/portainer/issues/8120)
* Redesigned Portainer database migration versioning to improve the robustness of the upgrade process: [portainer/portainer#8153](https://github.com/portainer/portainer/issues/8153)
* Replaced aws-sdk-go with aws-sdk-go-v2
* Fixed issue where random number generator is not seeded causing predictable outputs: [portainer/portainer#8342](https://github.com/portainer/portainer/issues/8342)
* Resolved issues building Portainer (caused by third-party deletion of the github.com/rkl-/digest package) by replacing the package with imported code. This provides HTTP Digest Authentication for Portainer's FIDO Device Onboard (FDO) protocol support: [portainer/portainer#8177](https://github.com/portainer/portainer/issues/8177)
* Corrected a minor UI issue around a corrupted file-code.svg icon: [portainer/portainer#8117](https://github.com/portainer/portainer/issues/8117)
* Removed the Go experimental module golang.org/x/exp, replacing the small amount of functionality that we use from it with direct code: [portainer/portainer#8176](https://github.com/portainer/portainer/issues/8176)
* Deprecated the github.com/portainer/libhelm Helm wrapper and moved the code into CE, since EE can now share from CE. This is used by Portainer's Helm functionality: [portainer/portainer#8178](https://github.com/portainer/portainer/issues/8178)
* Fixed issue where struct tag is malformed with incorrect blank space in template\_file.go: [portainer/portainer#7923](https://github.com/portainer/portainer/issues/7923)
* (swagger) fix licenses attach route

### REST API changes

#### New Endpoints

* GET `/docker/{environmentId}/containers/{containerID}/image_status`
* GET `/docker/{environmentId}/services/{serviceID}/image_status`
* GET `/docker/{environmentId}/stacks/{id}/images_status`
* GET `/kubernetes/{id}/namespaces/{namespace}/applications`
* GET `/kubernetes/{id}/namespaces/{namespace}/applications/{kind}/{name}`
* GET `/kubernetes/{id}/rbac_enabled`
* GET `/nomad/endpoints/{endpointID}/leader`
* GET `/system/info`
* GET `/system/nodes`
* GET `/system/status`
* POST `/system/upgrade`
* GET `/system/version`
* PUT `/webhooks/{id}/reassign`

#### Deleted Endpoints

* GET `/nomad/endpoints/{endpointID}/status`

#### Deprecated Endpoints

* GET `/status` - Deprecated: use the `/system/status` endpoint instead to retrieve the Portainer status.
* GET `/status/nodes` - Deprecated: use the `/system/nodes` endpoint instead.
* GET `/status/version` - Deprecated: use the `/system/version` endpoint instead to check if portainer has an update available.

#### Modified Endpoints

* POST `/backup/s3/execute`
* POST `/backup/s3/restore`
* POST `/backup/s3/settings`
* POST `/edge_jobs`
* POST `/edge_jobs/{id}`
* POST `/edge_stacks`
* PUT `/edge_stacks/{id}`
* POST `/edge_update_schedules`
* GET `/edge_update_schedules/active`
* PUT `/endpoints/{id}`
* PUT `/endpoints/{id}/settings`
* POST `/registries`
* PUT `/registries/{id}`
* PUT `/settings`
* POST `/stacks`

## Release 2.16.2

November 21, 2022

### Edge

* Fixed issue where the Git repository section is missing when creating an Edge Stack via the Git repository option. [portainer/portainer#8072](https://github.com/portainer/portainer/issues/8072)

### Portainer

* Fixed issue where the effective viewer is not showing the correct user access role of environments they have access to. [portainer/portainer#8070](https://github.com/portainer/portainer/issues/8070)

## Release 2.16.1

November 9, 2022

### Kubernetes

* Fixed an issue with view/edit of an external application (i.e. one originally added to the cluster outside of Portainer) where a 'cannot read properties' error was shown.
* Fixed an issue with view/edit of Kubernetes namespaces where memory and CPU resource limit sliders were positioned incorrectly and erroneous warnings were shown.

### Docker

* Fixed issue of update stack button being disabled when updating an existing stack.

### Portainer

* Fixed license key issue where node counts were not updated when environments are deleted.
* Fixed issue with JSON formatted logs failing in 2.16.0.

## Release 2.16.0

October 31, 2022

### Deprecation notice

* Proposing to deprecate ACI (Azure Container Instances) and remove the functionality to connect to ACI, view existing containers and deploy new containers.

### Upgrade notice

* `portainer/portainer:latest` moved to `portainer/portainer:2.16`.

### React migration

* Migrated from Angular to React: Tag selector for Environment Details view.
* Migrated from Angular to React: Teams view.

### Kubernetes

* When upgrading to 2.16, if you already have ingress controllers in a Kubernetes cluster/environment linked to Portainer and used Portainer to set them at the cluster and namespace level, and if these ingress controllers were not used by any ingresses, after the upgrade, you may end up with dummy ingresses visible in the new Ingresses screen in Portainer (that are not actually used for any deployment). This is simply an artifact of how we retained information about ingress controllers in earlier Portainer releases. If you find these kinds of dummy ingresses, you can safely delete them.
* Introduced the ability to auto-detect ingress classes in the environment. [portainer/portainer#7827](https://github.com/portainer/portainer/issues/7827)
* Added an Ingress menu option in the sidebar that lists all Ingresses in the cluster. [portainer/portainer#7839](https://github.com/portainer/portainer/issues/7839)
* Introduced the ability to set the type of a Kubernetes secret (e.g. TLS or a user-defined/custom type). Existing secrets were previously always of type Opaque (which remains the default). [portainer/portainer#7842](https://github.com/portainer/portainer/issues/7842)
* Improved ingress options on the cluster setup page, allowing admins to define ingresses without assigning them to a namespace. [portainer/portainer#7832](https://github.com/portainer/portainer/issues/7832)
* Introduce TLS and HTTPS support for ingresses. [portainer/portainer#7843](https://github.com/portainer/portainer/issues/7843)
* Moved the Ingress management from the Application details page to a new Ingress section. [portainer/portainer#7828](https://github.com/portainer/portainer/issues/7828)
* Resolved an issue when OAuth is in use and Kubernetes updates are deployed via manifest from git. The user email address used in labels/annotations for Kube objects now has disallowed characters (such as the at symbol) replaced with a dot (period symbol). [portainer/portainer#7720](https://github.com/portainer/portainer/issues/7720)
* The Homepage's kubeconfig download dialog now only includes those environments that show on the Homepage. Those with a connection error or provisioning error (these states were introduced in recent releases) are now excluded.
* Resolved an issue where Node stats would not work for Google Kubernetes Engine (GKE) clusters. [portainer/portainer#7668](https://github.com/portainer/portainer/issues/7668)
* Fixed the issue of missing Kubernetes definition for Kubernetes application deployment in the swagger API documentation. [portainer/portainer#7741](https://github.com/portainer/portainer/issues/7741)
* Fixed issue with deploying custom templates on Kubernetes that are using mustache variables.

### Docker

* Updated the Compose version to 2.10.2. [portainer/portainer#7838](https://github.com/portainer/portainer/issues/7838)
* Added support for shared memory when creating or editing a container by allowing to set --shm-size from portainer. [portainer/portainer#4992](https://github.com/portainer/portainer/issues/4992)
* Introduced support for uploading of local files to be included in a Docker image when using Portainer to build an image. [portainer/portainer#7796](https://github.com/portainer/portainer/issues/7796)
* Set notification of new image for docker default to off.
* Introduced a setting to turn on/off per host showing of out-of-date image indicators. [portainer/portainer#7219](https://github.com/portainer/portainer/issues/7219)
* Resolved an issue in Docker Services, Containers, and Stacks, where loading of the recently added out-of-date image indicator delayed showing of a row's action icons.
* Added information for rebuilding images from stacks on docker standalone environments. [portainer/portainer#7829](https://github.com/portainer/portainer/issues/7829)
* Added information to the build image from the URL page, including a link to additional documentation. [portainer/portainer#7771](https://github.com/portainer/portainer/issues/7771)
* Fixed an issue where environment variables for stacks could not be set to empty. [portainer/portainer#7780](https://github.com/portainer/portainer/issues/7780)
* Fixed an issue where assigning user access to a stack, showed users that don't have access to the Environment. [portainer/portainer#7695](https://github.com/portainer/portainer/issues/7695)
* Fixed the issue of missing agent deployment script for the docker standalone environment. [portainer/portainer#7757](https://github.com/portainer/portainer/issues/7757)
* Fixed the issue of the misconfigured stack being saved and subsequently can not be deleted. [portainer/portainer#7798](https://github.com/portainer/portainer/issues/7798)
* Fixed an issue where the Swarm secret values incorrectly were being trimmed. [portainer/portainer#7772](https://github.com/portainer/portainer/issues/7772)
* Fixed the issue where the container webhook toggle was not being saved.
* Fixed an issue where the Docker API section in the add environment wizard incorrectly was showing the docker.sock code block. [portainer/portainer#7650](https://github.com/portainer/portainer/issues/7650)
* Fixed an issue where a console error was showing for GPU when using Swarm because GPU is not supported on Swarm.
* Fixed an issue where renaming a deployed container resulted in an error. [portainer/portainer#7778](https://github.com/portainer/portainer/issues/7778)
* Fixed an issue where the image pull limits weren't being shown for standard users.
* Fixed error message when adding new docker environments with invalid CA certs for TLS. [portainer/portainer#7934](https://github.com/portainer/portainer/issues/7934)
* Adjusted the "remove" buttons as per the UI guidelines that were introduced in the 2.15 release. [portainer/portainer#7739](https://github.com/portainer/portainer/issues/7739)

### Gitops

* Introduced the offering of auto-suggestions retrieved from the git repo when entering the Compose path.
* Added the ability to store git credentials in user settings.

### Portainer

* Introduced a new section that shows past toaster notifications, which are stored in the browser's local storage. [portainer/portainer#7756](https://github.com/portainer/portainer/issues/7756)
* Introduced a context sensitive help button that links to the relevant documentation based on the current page. [portainer/portainer#7744](https://github.com/portainer/portainer/issues/7744)
* Introduced login screen banner to the login page.
* Added banner for "new version available" in portainer business edition.
* Updated dependencies of PCIDB/GHW for the portainer agent. [portainer/portainer#7705](https://github.com/portainer/portainer/issues/7705)
* Updated version of chart.js to 2.9.4 and moment to 2.29.4. [portainer/portainer#7681](https://github.com/portainer/portainer/issues/7681)
* Update golang and image dependencies for API and portainer binary ( EE ).
* Updated binary version for docker-compose and helm (to v3.9.3). [portainer/portainer#7704](https://github.com/portainer/portainer/issues/7704)
* Updated the agent library dependencies. [portainer/portainer#7420](https://github.com/portainer/portainer/issues/7420)
* Fixed an issue where the Microsoft OAuth information was not being retrieved correctly when editing the settings.
* Fixed select all behavior in environments page.
* Fixed the issue of handling images built by buildx or buildkit in the registry browser.
* Fixed an issue where the browser tab title did not update with the actually selected environment. [portainer/portainer#7651](https://github.com/portainer/portainer/issues/7651)
* Fixed issue with text color and text background color on auto-filled text.
* Fixed issue where the dropdown menu has incorrect background color in dark mode. [portainer/portainer#7678](https://github.com/portainer/portainer/issues/7678)
* Fixed styling issues in the Runtime & Resources tab. [portainer/portainer#7779](https://github.com/portainer/portainer/issues/7779)
* Fixed an issue where the new styling wasn't being applied to links. [portainer/portainer#7740](https://github.com/portainer/portainer/issues/7740)
* Adjusted the warning text color as per the UI guidelines that were introduced in the 2.15 release. [portainer/portainer#7667](https://github.com/portainer/portainer/issues/7667)
* Introduced UI info components while browsing snapshots.

### Edge

* Introduced the ability to run remote commands on edge environments connected via Async using mTLS.
* Introduced UI info components while browsing snapshots.

### Nomad

* Fixed issue around Home page loading time when you have Nomad environments connected.
* Removed extension validation from compose path field. [portainer/portainer#7652](https://github.com/portainer/portainer/issues/7652)
* Fixed an issue where the Group and Tag could not be set for Nomad environments when adding it via the wizard. [portainer/portainer#7703](https://github.com/portainer/portainer/issues/7703)
* Fixed an issue where Nomad system jobs would prevent other jobs from being shown. [portainer/portainer#7229](https://github.com/portainer/portainer/issues/7229)

### Development

* Improved unit tests by using T.TempDir to create a temporary test directory. [portainer/portainer#7675](https://github.com/portainer/portainer/issues/7675)
* Replaced the logrus logging framework with Zerolog. [portainer/portainer#7935](https://github.com/portainer/portainer/issues/7935)
* Fixed an issue where new installations that use the develop branch didn't apply the analytics setting correctly. [portainer/portainer#7584](https://github.com/portainer/portainer/issues/7584)

## Release 2.15.1

September 16, 2022

### Docker

* Fixed an issue with connecting to the local Docker environment when using Windows Container Services. [portainer/portainer#7618](https://github.com/portainer/portainer/issues/7618)
* Fixed an issue where the build image button would stay inactive when using a tar file. [portainer/portainer#7624](https://github.com/portainer/portainer/issues/7624)

### Portainer

* Fixed an issue where some colors in dark mode appeared too brown. [portainer/portainer#7616](https://github.com/portainer/portainer/issues/7616)
* Fixed an issue when using leading or trailing spaces in a password would break the login process. [portainer/portainer#7621](https://github.com/portainer/portainer/issues/7621)

## Release 2.15.0

September 6, 2022

### Deprecation notice

* Proposing to deprecate Kompose and remove the functionality to deploy compose yaml on Kubernetes. [portainer/portainer#7514](https://github.com/portainer/portainer/issues/7514)

### Breaking changes

* Breaking change in API where the endpoint filter `edgeDeviceFilter` has been replaced by `edgeDevice` and `edgeDeviceUntrusted`.

### Browser cache

* Improved caching to prepare a resolution for an issue where certain browsers need a manual browser refresh for new version assets to load. The change only takes effect for upgrades subsequent to migration to 2.15. [portainer/portainer#7443](https://github.com/portainer/portainer/issues/7443)

### React migration

* Migrated docker/containers/list views to React.
* Migrated the Docker console.
* Migrated Azure Container Instances views to React.
* Migrated the sidebar menu and adjusted the Settings page.
* Migrated the Kubectl shell window.
* Migrated tooltip into react component.
* Migrated page header into React component.

### Kubernetes

* Introduced the ability to define pod security constraints per Kubernetes cluster.
* Introduced an option to forcibly remove a Kubernetes namespace that's in a 'Terminating' state. [portainer/portainer#4580](https://github.com/portainer/portainer/issues/4580)
* Improved the kubeconfig download dialog by providing pagination (including choosing of the number of items per page), an option to 'select all in page' and selection across multiple pages. [portainer/portainer#7261](https://github.com/portainer/portainer/issues/7261)
* Resolved an issue where the link shown for an application that is exposed via an ingress was including an incorrect port (the servicePort). [portainer/portainer#7337](https://github.com/portainer/portainer/issues/7337)
* Resolved some errors and wording issues in recent KaaS cluster provisioning and import kubeconfig functionality.
* When using Kubernetes (KaaS) cluster provisioning and choosing the DigitalOcean option, only node size options that are valid for provisioning now show. Previously, there was at least one option which gave an 'invalid droplet size' error on use.

### Docker

* Added GPU support to Docker containers. [portainer/portainer#3143](https://github.com/portainer/portainer/issues/3143)
* Introduced the ability to disable use of the anonymous Docker Hub registry option via the Portainer UI for all users.
* Added support to read value from .env in subfolder for git deployment in Docker Standalone Environment. [portainer/portainer#7265](https://github.com/portainer/portainer/issues/7265)
* Added message explaining that changed env values only take effect after redeployment or auto update via webhook. [portainer/portainer#7242](https://github.com/portainer/portainer/issues/7242)
* Provided prune option for stack deployment from Git. [portainer/portainer#7224](https://github.com/portainer/portainer/issues/7224)
* Removed "Show Container Template" toggle on App templates page and introduced filter and sort by dropdown options. [portainer/portainer#7394](https://github.com/portainer/portainer/issues/7394)
* Fixed recreate of container so it pulls the image using the SHA256 hash if its tag no longer exists, and if the image is still inaccessible (as it no longer exists or the tag or name is now incorrect) warn the user and disable 'Pull latest image' option. [portainer/portainer#6566](https://github.com/portainer/portainer/issues/6566)
* Introduced support for checking images held in private registries to the recently added functionality that shows a visual image indication on stacks, services and containers that are running with an out-of-date image.
* Introduced improved validation to the Docker build image function, to prevent invalid image names. [portainer/portainer#7463](https://github.com/portainer/portainer/issues/7463)
* Fixed host info being sent when host management feature is turned off. [portainer/portainer#7277](https://github.com/portainer/portainer/issues/7277)
* Following the introduction of v2 Docker Compose, changed any front-end wording that mentions 'docker-compose' to say 'docker compose', to clarify and bring in line with official documentation. [portainer/portainer#7141](https://github.com/portainer/portainer/issues/7141)

### Portainer

* Introduced license enforcement for 5 nodes free in business edition.
* Introduced new styling for Portainer. [portainer/portainer#7528](https://github.com/portainer/portainer/issues/7528)
* Introduced Portainer UI redesign with changes for common configuration pages. [portainer/portainer#7527](https://github.com/portainer/portainer/issues/7527)
* Included build information in Portainer for easier debug. [portainer/portainer#7317](https://github.com/portainer/portainer/issues/7317)
* Introduced the ability to show/hide the password you are entering on login. [portainer/portainer#7461](https://github.com/portainer/portainer/issues/7461)
* Introduced CTRL+F (or CMD+F on MacOS) to search in web editors. [portainer/portainer#6537](https://github.com/portainer/portainer/issues/6537)
* Introduced the ability to filter connection type and agent version on the home page. [portainer/portainer#7468](https://github.com/portainer/portainer/issues/7468)
* Improved environment address entry to handle http\:// or https\:// prefixes when adding an environment via Docker or Kubernetes (agent) options. [portainer/portainer#7462](https://github.com/portainer/portainer/issues/7462)
* Introduced a change to the Homepage's multi-select filters to keep the dropdown open after a single selection until the user closes it themselves, or the last remaining option is selected. [portainer/portainer#7548](https://github.com/portainer/portainer/issues/7548)
* Added tips for entering Portainer license key.
* Updated the agent library dependencies [portainer/portainer#7420](https://github.com/portainer/portainer/issues/7420)
* Fixed issue where Automatic team membership did not always work for Azure.
* Fixed an issue where auto populate team admins LDAP feature didn't work on upgrade from CE to BE.
* Fixed issue of authentication logs not working behind reverse proxy. [portainer/portainer#7120](https://github.com/portainer/portainer/issues/7120)
* Fixed license expiry message flashing even license is not expired or close to expiring.
* Fixed a few typos in various locations. [portainer/portainer#7243](https://github.com/portainer/portainer/issues/7243)
* Fixed issue with environment page table losing selection on table refresh. [portainer/portainer#7395](https://github.com/portainer/portainer/issues/7395)
* Fixed missing BE feature indicators. [portainer/portainer#7396](https://github.com/portainer/portainer/issues/7396)
* Fixed issue where certificate uploading is not functional for StartTLS/TLS in LDAP configuration. [portainer/portainer#6271](https://github.com/portainer/portainer/issues/6271)
* Reworded error message for JWT token missing to more user-friendly message.

### Edge

* Introduced the ability to get logs for edge stacks of specific environments.
* Fixed connection issue ("Environment is unreachable") after deploying Nomad environment with AEEC script.
* Updated UI of Add devices page to match the Add environment page. [portainer/portainer#7393](https://github.com/portainer/portainer/issues/7393)
* Fixed issue where editing edge jobs changed the configured cron expression. [portainer/portainer#7432](https://github.com/portainer/portainer/issues/7432)
* Fixed known issue with manually adding an Edge Device environment through the edge device page when using Async mode, does not retain Async settings and needs to be manually added through the environment details page.
* Removed Beta label on Edge Jobs. [portainer/portainer#7162](https://github.com/portainer/portainer/issues/7162)
* Improved image parsing for Kubernetes Edge Stacks that use private registries so that the same parsing as Docker ones is used.

### Registry

* Improved Registry details screen with better prompting for relevant fields. [portainer/portainer#3015](https://github.com/portainer/portainer/issues/3015)
* Resolved an issue around not being able to add multiple Quay registries. [portainer/portainer#7430](https://github.com/portainer/portainer/issues/7430)
* Improved the Registry details screen to show the registry provider and made the Add registry screen default to Docker Hub as the provider. [portainer/portainer#7246](https://github.com/portainer/portainer/issues/7246)

### Nomad

* Standardized the behavior of Nomad edge environments to be the same as non-Nomad edge environments.

## Release 2.14.2

July 26, 2022

### Known issues

* Known issue with manually adding an Edge Device environment through the Edge Device page when using Async mode, does not retain Async settings and needs to be manually added through the environment details page.
* Image update notifications are currently not supported for private registries and private images in DockerHub. This is due to be fixed in our next major version.

### Kubernetes

* Fixed an issue where the kubeconfig downloadable from Portainer always had port 9443 in its URLs, even though the actual Portainer instance was being accessed via another port. [portainer/portainer#7059](https://github.com/portainer/portainer/issues/7059)

### Docker

* Fixed certificate file validation for .pem files [portainer/portainer#7183](https://github.com/portainer/portainer/issues/7183)
* Fixed an issue when using a Mustache variable (e.g. {{service}}) multiple times in the YAML, where the UI should prompt for it only once and then reuse it (rather than prompting for it multiple times).
* Fixed an issue when using a Mustache variable (e.g. {{path}}) with special characters in the value, where the resulting value would end up being HTML encoded.
* Fixed issue around access control labels being ignored.

### Portainer

* Fixed an issue where the original admin user was unable to change their password when external authentication is enabled. [portainer/portainer#7291](https://github.com/portainer/portainer/issues/7291)
* Fixed toggle state reset issue for custom logo and anonymous statistics. [portainer/portainer#7278](https://github.com/portainer/portainer/issues/7278)
* Fixed issue with not being able to add users to teams while LDAP authentication is enabled without auto teams population. [portainer/portainer#7252](https://github.com/portainer/portainer/issues/7252)
* Fixed an issue where auto populate team admins LDAP feature didn't work on upgrade from CE to BE.
* Resolved an issue where new installs of recent Portainer releases had an extraneous (although innocuous) db version update on restart.

### Edge&#x20;

* Fixed pagination issue on Add edge jobs page for listed environments. [portainer/portainer#7312](https://github.com/portainer/portainer/issues/7312)

## Release 2.14.1

July 12, 2022

### Known issues

* Known issue with manually adding an Edge Device environment through the Edge Device page when using Async mode, does not retain Async settings and needs to be manually added through the environment details page.
* Image update notifications are currently not supported for private registries and private images in DockerHub. This is due to be fixed in our next major version.
* When using a Mustache variable (e.g. `{{ service }}`) multiple times in the YAML, the UI also prompts for it multiple times, rather than prompting for it a single time and then reusing it.

### Kubernetes

* Improved KaaS cluster provisioning's cluster name validation to enforce restrictions that Google GKE expects.
* Fixed issue of variable inputs not showing on deployment view when using custom templates.
* Improved Portainer logging to better record the output from eksctl, the CLI tool used for Amazon EKS (KaaS) cluster provisioning.
* Fixed an issue where, upon initiating AWS KaaS cluster/environment provisioning and subsequently restarting Portainer in a short space of time, the requested environment would become stuck and unusable in Portainer, and couldn't be deleted.

### Docker

* Resolved an issue where users running Portainer with non-root access were receiving a 'Permission denied on docker-compose' error since the recent update to Docker Compose V2. [portainer/portainer#6906](https://github.com/portainer/portainer/issues/6906)

### Portainer

* Fix to improve LDAP, etc. authentication/login speed when there are many thousands of users.
* Resolved an issue where users upgrading a Portainer install, where the portainer\_data volume is stored on a network volume, receive a 'Permission denied' error when the upgrade attempts a backup of the database. [portainer/portainer#7144](https://github.com/portainer/portainer/issues/7144)
* Fixed "Create user" button in disabled stage when external Auth enabled. [portainer/portainer#7214](https://github.com/portainer/portainer/issues/7214)

### Edge

* Fixed issue where the edge agent could not connect when running Portainer behind a reverse proxy only supporting TLS v1.2. [portainer/portainer#7167](https://github.com/portainer/portainer/issues/7167)

## Release 2.14.0

June 28, 2022

### Known issues

* Known issue with manually adding an Edge Device environment through the Edge Device page when using Async mode, does not retain Async settings and needs to be manually added through the environment details page.
* Image update notifications are currently not supported for private registries and private images in DockerHub. This is due to be fixed in our next major version.

### Breaking changes

* With the upgrade to Docker Compose V2, container names now use hyphens as separators instead of underscores. This may affect you if you are generating container names instead of explicitly defining them, then using them as references.

### Kubernetes

* Introduced ability to set up a new Kubernetes environment in Portainer via upload of a kubeconfig file for an existing on premises or on-cloud cluster.
* Fixed issue around Git clone working with Main (in addition to existing Master) branch type. [portainer/portainer#6002](https://github.com/portainer/portainer/issues/6002)
* Updated packaged components to recent stable release versions: Docker 20.10.9, Docker Compose plugin 2.5.1, kubectl 1.24.1, Helm 3.9.0. [portainer/portainer#6074](https://github.com/portainer/portainer/issues/6074)
* Administrators can now set up cloud provider settings via a list page and separate add page in a similar way to other records in Portainer.
* Introduced support for provisioning of a Kubernetes cluster on the Amazon (AWS) EKS platform from within Portainer, alleviating the need to do so in the cloud provider's portal. The AWS eksctl binary is auto downloaded when first using this functionality.
* Introduced support for provisioning of a Kubernetes cluster on the Microsoft Azure AKS platform from within Portainer, alleviating the need to do so in the cloud provider's portal.
* Introduced support for provisioning of a Kubernetes cluster on the Google Cloud GKE platform from within Portainer, alleviating the need to do so in the cloud provider's portal.
* Fixed a typo in the Kubernetes -> Namespaces -> Create from manifest (advanced deployment) page. [portainer/portainer#6968](https://github.com/portainer/portainer/issues/6968)
* Fixed an issue with cluster provisioning via Civo KaaS, where if the Civo account has an issue with its defined networks, the environment was stuck waiting to complete provisioning and never ultimately errored.
* Introduced the ability to set the group and tags against the environment in Portainer when an admin provisions a Kubernetes as a Service cluster.
* Introduced slight improvements to editing of sensitive cloud credentials values.
* Fixed an issue in the Settings -> Environments page, where an environment that was disabled or still being provisioned could be selected for removal and then removed.
* Added the ability to manually refresh pulling of Kubernetes as a Service cluster provisioning options from cloud providers.
* Improved error handling around KaaS provisioning in the environment wizard.
* Kubernetes as a Service (cloud) provisioned environments will now appear in the 'new environments' side panel in the environments wizard.

### Docker

* Introduced a visual indication of stacks, services and containers that are running with an out-of-date image. [portainer/portainer#1304](https://github.com/portainer/portainer/issues/1304)
* Fixed issue around Git clone working with Main (in addition to existing Master) branch type. [portainer/portainer#6002](https://github.com/portainer/portainer/issues/6002)
* Updated packaged components to recent stable release versions: Docker 20.10.9, Docker Compose plugin 2.5.1, kubectl 1.24.1, Helm 3.9.0. [portainer/portainer#6074](https://github.com/portainer/portainer/issues/6074)
* Fixed issue for standard user having an empty network as default when creating containers on Windows environments [portainer/portainer#6959](https://github.com/portainer/portainer/issues/6959)
* Introduced ability to pass environment variables on the webhooks in Docker stack deployment.
* Provide a stack template for dokku deployment within portainer. [portainer/portainer#7011](https://github.com/portainer/portainer/issues/7011)
* Resolved an issue when updating an application and changing its service from replicated to global, where an error occurs and the deployed application is deleted. [portainer/portainer#7056](https://github.com/portainer/portainer/issues/7056)
* Third-party developer Inedo has fixed their ProGet registry software to resolve an intermittent error admins were experiencing in Portainer on retag or delete of a tagged image. This is planned to ship 10 June 2022 in ProGet 6.0.16, before Portainer 2.14.
* Introduced support in the container webhook for pull/recreate of containers from images residing in private registries.
* Fixed an issue in the Containers page, where choosing 'Recreate' enabled the webhook for the container, even though it was not currently turned on.
* Fixed an issue where, when calling Swarm update API through Portainer, incorrect overriding of the registry authentication header occurred, preventing pull of an image. [portainer/portainer#7095](https://github.com/portainer/portainer/issues/7095)

### Portainer

* Redesigned team leader feature. [portainer/portainer#7093](https://github.com/portainer/portainer/issues/7093)
* Fixed an issue where the delete environment confirmation dialog was positioned too low on-screen. [portainer/portainer#6983](https://github.com/portainer/portainer/issues/6983)
* Fixed an issue where agent and edge agent install command instructions do not list the agent\_secret option. [portainer/portainer#6801](https://github.com/portainer/portainer/issues/6801)
* Fixed an issue where the home (environments) page no longer showed the words 'No tags' for environments without tags. [portainer/portainer#6967](https://github.com/portainer/portainer/issues/6967)
* Introduced support for provisioning of a Kubernetes cluster on the Amazon (AWS) EKS platform from within Portainer, alleviating the need to do so in the cloud provider's portal. The AWS eksctl binary is auto downloaded when first using this functionality.
* The Add environment page and Environment wizard are now consolidated into a single consistent, improved wizard-style experience. [portainer/portainer#7022](https://github.com/portainer/portainer/issues/7022)
* Introduced support for provisioning of a Kubernetes cluster on the Microsoft Azure AKS platform from within Portainer, alleviating the need to do so in the cloud provider's portal.
* Introduced support for provisioning of a Kubernetes cluster on the Google Cloud GKE platform from within Portainer, alleviating the need to do so in the cloud provider's portal.
* Fixed Go panic state for the environments list handler [portainer/portainer#7047](https://github.com/portainer/portainer/issues/7047)
* Introduced ability for admin to set required password length. [portainer/portainer#7055](https://github.com/portainer/portainer/issues/7055)
* Fixed an issue recently introduced in the environments page where the name of an environment that was down no longer linked through to its details page.
* Resolved an issue preventing migration from EE 2.12 to 2.13 (or now 2.14) for Portainer instances that had previously migrated to EE from a CE instance with Allow Volume Browser for Regular Users toggled on for an environment.
* Increased the click/touch area in expandable panels so it's easier to open/close them. [portainer/portainer#7036](https://github.com/portainer/portainer/issues/7036)
* Fixed propagation of Portainer agent polling frequency when changed before deploying via automatic edge environment creation
* Introduced the ability to paste in an existing license, revalidate with the license server and replace it in the database. This can be used to fix a corrupted license.

### Edge

* Fixed issue with status indicator on Edge Stacks not updating when removing tags from edge environments/groups [portainer/portainer#6950](https://github.com/portainer/portainer/issues/6950)
* Introduced the ability to define the 3 polling intervals for Async
* For edge agents, the URL shown in the Environment summary page (access from the Home page) has now been removed, as it caused confusion since it simply showed the Portainer Server URL. [portainer/portainer#6978](https://github.com/portainer/portainer/issues/6978)
* Fixed Data race in the operations of the edge key in the Edge Agent [portainer/portainer#7024](https://github.com/portainer/portainer/issues/7024)
* Added "goto page" to the Edge devices page view [portainer/portainer#6982](https://github.com/portainer/portainer/issues/6982)
* Added the ability to add edge agents in the environment wizard [portainer/portainer#7023](https://github.com/portainer/portainer/issues/7023)

### Nomad

* Added HTTPS support for Nomad Edge Agent.
* Added display of BE feature highlights in CE for new Nomad, KaaS provisioning and kubeconfig import functionality. [portainer/portainer#7051](https://github.com/portainer/portainer/issues/7051)

## Release 2.13.1

May 12, 2022

### Portainer

* Changed the minimum TLS version of Portainer from 1.3 to 1.2 to avoid issues with nginx reverse proxies: [portainer/portainer#6902](https://github.com/portainer/portainer/issues/6902)
* Fixed issue with the Portainer authentication settings page not being able to save: [portainer/portainer#6899](https://github.com/portainer/portainer/issues/6899)
* Changed the password policy to require 12 characters for all Portainer internal users: [portainer/portainer#6904](https://github.com/portainer/portainer/issues/6904)

## Release 2.13.0

May 9. 2022

### Known issues

* When provisioning a Civo cluster while there are multiple default networks defined on the Civo account, the environment will fail to provision and Portainer will end up waiting for the environment to be ready indefinitely. This can be resolved from the Civo console by deleting the cluster and using a non-default network for the provision.

### Breaking changes

* The minimum TLS version of Portainer was changed from 1.2 to 1.3. If you are running a proxy in front of Portainer with HTTPS you will need to ensure it is configured to support TLS 1.3.
* Standard users can browse registries including edit and delete
* Introduced the ability for non admin users to browse image registries
* Added strong password policy for all Portainer internal users. When using a weak password and logging in you will be required to update your password.

### Kubernetes

* Improve how Portainer helps you set up ingresses (especially Nginx ones), including support of regular expressions in paths - by assisting with required annotations and correcting a rewrite issue: [portainer/portainer#6854](https://github.com/portainer/portainer/issues/6854)
* Introduce support for provisioning of a Kubernetes cluster on a cloud provider's KaaS offering from within Portainer, alleviating the need to do so in the provider's own portal. Initial supported providers are Civo, DigitalOcean and Linode.
* Fixed an issue where, on setting up (on a namespace) an ingress controller for a k8s cluster and I create an app with two ingress routes on the controller, app details show only the second of the paths: [portainer/portainer#6856](https://github.com/portainer/portainer/issues/6856)
* Fixed an issue where Portainer's validation of a K8s namespace's hostnames was disallowing wildcards (e.g. \*abc.com): [portainer/portainer#6855](https://github.com/portainer/portainer/issues/6855)
* Fixed issue with default helm repo not populating in settings page: [portainer/portainer#6849](https://github.com/portainer/portainer/issues/6849)
* Created documentation around using GKE ingress with Portainer: [portainer/portainer#6848](https://github.com/portainer/portainer/issues/6848)
* Added input validation for kubernetes workload names: [portainer/portainer#5363](https://github.com/portainer/portainer/issues/5363)
* Fixed issue where changing Portainer to HTTPS crashed Portainer: portainer/portainer#6836
* Fixed issue where Helm Charts could not be deployed when using SSL certs with Portainer: [portainer/portainer#6742](https://github.com/portainer/portainer/issues/6742)
* Fixed issue of not being able to use a name previously used for kubernetes resources: [portainer/portainer#6830](https://github.com/portainer/portainer/issues/6830)
* Fixed issue where the Kube cluster resource stats had a rounding issue: [portainer/portainer#6472](https://github.com/portainer/portainer/issues/6472)
* Fixed an issue when deploying Portainer client with AGENT\_SECRET without configuring Kubernetes agent with AGENT\_SECRET where an "Failure unknown" error shows rather than "agent already paired" : [portainer/portainer#6791](https://github.com/portainer/portainer/issues/6791)

### Docker

* Standard users can browse registries including edit and delete
* Introduced the ability for non admin users to browse image registries
* Fixed issue where the Disable bind mounts for non-administrators setting would prevent existing volumes from being used: [portainer/portainer#6387](https://github.com/portainer/portainer/issues/6387)
* Fixed issue with creating a CIFS volume that uses a hostname: [portainer/portainer#6338](https://github.com/portainer/portainer/issues/6338)
* Fixed issue where webhooks for services were accepting invalid tags: [portainer/portainer#6493](https://github.com/portainer/portainer/issues/6493)
* Fixed issue with libcompose logging where error output is attempted to be included when an error did not occur: [portainer/portainer#6857](https://github.com/portainer/portainer/issues/6857)
* Fixed an issue where 'Pull and Redeploy' and 'Force redeploy' don't work on ARM: [portainer/portainer#6788](https://github.com/portainer/portainer/issues/6788)
* Documented deviation from the Docker standard when using the /docker/images/create API endpoint in conjunction with a private registry: [portainer/portainer#6712](https://github.com/portainer/portainer/issues/6712)
* Fixed issue where credentials from different registries were being used: [portainer/portainer#6087](https://github.com/portainer/portainer/issues/6087)
* Fixed issue where stack name was stated inaccurately in the message which informs users that a container/service inherited its access control settings from a specific stack: [portainer/portainer#6478](https://github.com/portainer/portainer/issues/6478)
* Fixed issue with displaying container template when connected to docker swarm in the app templates page view: [portainer/portainer#6837](https://github.com/portainer/portainer/issues/6837)
* Fixed text color on modal when updating a service: [portainer/portainer#6839](https://github.com/portainer/portainer/issues/6839)
* Fixed issue where Watchtower did not work for standalone stacks on Arm64: [portainer/portainer#5799](https://github.com/portainer/portainer/issues/5799)

### Portainer

* Enforced strong password policy for all Portainer Users: [portainer/portainer#6846](https://github.com/portainer/portainer/issues/6846)
* Improved the database migration to become more resilient: [portainer/portainer#6778](https://github.com/portainer/portainer/issues/6778)
* Introduced the ability to filter and sort environments on the Home page: [portainer/portainer#6823](https://github.com/portainer/portainer/issues/6823)
* When changing the user password the user gets redirected to the login page: [portainer/portainer#6456](https://github.com/portainer/portainer/issues/6456)
* Fixed issue where upgrading to the Business Edition and then downgrading back to the Community Edition did not work
* Improved security for custom templates when using Git repos that contain symlinks: [portainer/portainer#6847](https://github.com/portainer/portainer/issues/6847)
* Improved how the installation page times out: [portainer/portainer#6740](https://github.com/portainer/portainer/issues/6740)
* Improved file type validation when selecting multiple files when deploying from Git repository
* Removed superfluous warning message for the Enable Change Window setting
* Fixed bug relating to environment status in home page: [portainer/portainer#6047](https://github.com/portainer/portainer/issues/6047)
* Improved concurrency in agent code to prevent race conditions: [portainer/portainer#6677](https://github.com/portainer/portainer/issues/6677)
* Improved concurrency in backend code to prevent race conditions: [portainer/portainer#6677](https://github.com/portainer/portainer/issues/6677)
* Fixed duplicate naming issue for registries: [portainer/portainer#6838](https://github.com/portainer/portainer/issues/6838)
* Fixed issue around user accessing agent environment after changing an invalid environment url to a valid one: [portainer/portainer#6824](https://github.com/portainer/portainer/issues/6824)
* Fixed issue with the menu when connecting to another environment fails: [portainer/portainer#6449](https://github.com/portainer/portainer/issues/6449)
* Updated registry form wording from Password to "Dockerhub access token" : [portainer/portainer#6308](https://github.com/portainer/portainer/issues/6308)
* Fixed text color for change window warning text
* Fixed an issue where the hover-over tooltip for nav menu items always just showed 'Settings' rather than the menu item text: [portainer/portainer#6779](https://github.com/portainer/portainer/issues/6779)
* Fixed issue where the green success notification was not showing up after deleting a custom app template: [portainer/portainer#6724](https://github.com/portainer/portainer/issues/6724)
* Improved UX for setting themes by removing save button: [portainer/portainer#6840](https://github.com/portainer/portainer/issues/6840)

### Edge

* Renamed Trust on first connect to "Waiting Room"
* Introduced the ability to pass env variables from local system to edge stacks for Kubernetes environments
* Created the ability for Automatic Edge Environment Creation (AEEC) within Portainer Server
* Introduced support for using credentials with private registries for edge stacks
* Resolved data race on stack deploy for edge agents: [portainer/portainer#6677](https://github.com/portainer/portainer/issues/6677)
* Added environment variable to the agent to adjust the probe timeout and interval: [portainer/agent#293](https://github.com/portainer/agent/issues/293)
* Introduce the ability to pass env variables from a local system on edge devices to the edge stack: [portainer/portainer#6832](https://github.com/portainer/portainer/issues/6832)
* Fixed issue with edge environments having faulty heartbeat on Edge Devices page: [portainer/portainer#6825](https://github.com/portainer/portainer/issues/6825)
* Improved concurrency in edge code to prevent race conditions: [portainer/portainer#6677](https://github.com/portainer/portainer/issues/6677)
* Fixed data race in poll service on Edge Agent: [portainer/portainer#6677](https://github.com/portainer/portainer/issues/6677)
* Resolved some race conditions with the edge agent: [portainer/portainer#6677](https://github.com/portainer/portainer/issues/6677)
* Resolved data race on tunnels for edge agents: [portainer/portainer#6677](https://github.com/portainer/portainer/issues/6677)
* Resolved data race with activity timer for edge agents: [portainer/portainer#6677](https://github.com/portainer/portainer/issues/6677)
* Fixed issue with displaying AMT device table for non-activated devices: [portainer/portainer#6835](https://github.com/portainer/portainer/issues/6835)
* Fixed minor UI issues in Edge devices page view around Action buttons: [portainer/portainer#6844](https://github.com/portainer/portainer/issues/6844)
* Fixed issue when creating edge job from file returning 404: [portainer/portainer#6826](https://github.com/portainer/portainer/issues/6826)

### Development

* Updated the Go library dependencies: [portainer/portainer#6777](https://github.com/portainer/portainer/issues/6777)
* Migrated AngularJS components to ReactJS: [portainer/portainer#6031](https://github.com/portainer/portainer/issues/6031)
* Reorganized the file structure of the agent installation yaml files: [portainer/portainer#6776](https://github.com/portainer/portainer/issues/6776)
* Removed the integration with Storidge clusters: [portainer/portainer#6512](https://github.com/portainer/portainer/issues/6512)

## Release 2.12.2

April 4, 2022

### Nomad

* Introduced Nomad integration
* Allows Nomad to be added as an environment in Portainer by using the Edge Agent
* Allows Edge Stacks to be deployed on Nomad as Nomad Jobs
* Allows Nomad Jobs and Tasks to be listed
* Allows Nomad logs and events to be viewed for Tasks

### Kubernetes

* Fixed issue where changing Portainer to HTTPS crashed Portainer
* Fixed issue around deploying in default namespace via manifest using the portainer namespace instead
* Fixed bug causing domain names to not displaying correctly under publish application options
* Fixed issue with first service naming having a suffix attached.
* Improved error message being displayed when deploying a malformed Kubernetes manifest from GitOps

### Portainer

* Fixed issue with GitOps automatic update
* Fixed issues around migration path for CE to BE
* Fixed missing operator role when migrating from 1.x
* Improved concurrency in edge code to prevent race conditions: [portainer/portainer#6677](https://github.com/portainer/portainer/issues/6677)

### Edge

* Resolved some race conditions with the Edge Agent

## Release 2.12.1

March 9, 2022

### Portainer

* Fixed bug where redeploying a stack causes an error and success message at the same time.
* Fixed bug that was preventing ability to edit application with persisted folder on Kubernetes.

## Release 2.12.0

March 8, 2022

### Breaking changes

* When OAuth is enabled, Portainer users can no longer use their Portainer internal password: [portainer/portainer#5889](https://github.com/portainer/portainer/issues/5889)
* Deploying a manifest without a namespace definition and selecting the Default namespace in Portainer may deploy the application into the portainer namespace in certain circumstances

### Kubernetes

* Added input validation for kubernetes workload names: [portainer/portainer#5363](https://github.com/portainer/portainer/issues/5363)
* Fixed issue where the Kube cluster resource stats had a rounding issue: [portainer/portainer#6472](https://github.com/portainer/portainer/issues/6472)
* Migrated to use the networking.k8s.io/v1 ingress API, available from Kubernetes v1.19: [portainer/portainer#6396](https://github.com/portainer/portainer/issues/6396)
* Allow Services to be managed for Kubernetes applications, which can be deployed within Portainer or outside of it: [portainer/portainer#5941](https://github.com/portainer/portainer/issues/5941)
* Restarting Portainer will no longer result in invalid kubeconfig credentials, which would have required the user to download a new kubeconfig file again: [portainer/portainer#5940](https://github.com/portainer/portainer/issues/5940)
* Provides a single process so that users can gain access to all their environments contexts from within the Portainer UI: [portainer/portainer#5945](https://github.com/portainer/portainer/issues/5945)
* Improved how a namespace gets selected when using Advanced deployment: [portainer/portainer#5557](https://github.com/portainer/portainer/issues/5557)
* Added warning that a secret will be created when adding registry access to a namespace: [portainer/portainer#5845](https://github.com/portainer/portainer/issues/5845)
* Fixed issue where selecting a Helm chart did not scroll to the top: [portainer/portainer#6146](https://github.com/portainer/portainer/issues/6146)
* Fixed issue when clearing Helm repo in global settings and added text notification in Helm charts page: [portainer/portainer#5996](https://github.com/portainer/portainer/issues/5996)
* Fixed issue where Helm charts fail to load in ARM cloud environments: [portainer/portainer#5937](https://github.com/portainer/portainer/issues/5937)
* Fixed issue where the kubectl shell wasn't working when Portainer runs on ARM64: [portainer/portainer#5723](https://github.com/portainer/portainer/issues/5723)
* Fixed bug so that Kubernetes terminology is used when deploying through Kubernetes: [portainer/portainer#6099](https://github.com/portainer/portainer/issues/6099)
* Fixed issue where error notice was coming up when deleting an application through kubeshell: [portainer/portainer#5939](https://github.com/portainer/portainer/issues/5939)
* Fixed issue where Portainer stacks were not being removed when removing a namespace: [portainer/portainer#5897](https://github.com/portainer/portainer/issues/5897)
* Fixed issue where standard users were unable to access the pod and node stats view: [portainer/portainer#5898](https://github.com/portainer/portainer/issues/5898)
* Fixed issue where the namespace details page showed an object object error: [portainer/portainer#5802](https://github.com/portainer/portainer/issues/5802)
* Fixed issue when selecting Cluster Setup in the menu: [portainer/portainer#6033](https://github.com/portainer/portainer/issues/6033)
* Fixed order of registries to be alphabetical in the select registry dropdown in namespaces: [portainer/portainer#6175](https://github.com/portainer/portainer/issues/6175)
* Fixed issue with publishing method defaulting to Ingress when changing to Cluster IP: [portainer/portainer#6190](https://github.com/portainer/portainer/issues/6190)

### Docker

* Introduced the ability to pull latest images when redeploying: [portainer/portainer#6155](https://github.com/portainer/portainer/issues/6155)
* Fixed issue where webhooks for services were accepting invalid tags: [portainer/portainer#6493](https://github.com/portainer/portainer/issues/6493)
* When updating a Swarm service and enabling Pull latest image, it would change the tag to latest: [portainer/portainer#6352](https://github.com/portainer/portainer/issues/6352)
* Fixed issue with displaying container template when connected to docker swarm in the app templates page view
* Fixed issue where updating the Stack always recreated the containers: [portainer/portainer#6306](https://github.com/portainer/portainer/issues/6306)
* Added the ability to filter the Swarm services published ports column: [portainer/portainer#6161](https://github.com/portainer/portainer/issues/6161)
* Added a warning when the same Swarm secret is assigned multiple times to a service: [portainer/portainer#2821](https://github.com/portainer/portainer/issues/2821)
* Added the option to detach Stacks deployed from Git to make them editable: [portainer/portainer#5748](https://github.com/portainer/portainer/issues/5748)
* Removed the ability to edit the Portainer container: [portainer/portainer#5121](https://github.com/portainer/portainer/issues/5121)
* Fixed issue where an error message would not be shown when failing to pull an image: [portainer/portainer#6239](https://github.com/portainer/portainer/issues/6239)
* Fixed issue where the default user for the container console was incorrectly auto filled: [portainer/portainer#6315](https://github.com/portainer/portainer/issues/6315)
* Fixed issue where uploading large files to a volume would fail: [portainer/portainer#4453](https://github.com/portainer/portainer/issues/4453)
* Fixed issue where stacks deployed from App Templates behaved as if they were deployed from Git: [portainer/portainer#5748](https://github.com/portainer/portainer/issues/5748)
* Fixed issue where stacks with environment variables in the networks section could not be removed: [portainer/portainer#5779](https://github.com/portainer/portainer/issues/5779)
* Allow the resource settings of a container to be updated without redeploying the container: [portainer/portainer#5906](https://github.com/portainer/portainer/issues/5906)
* Added support for .bz2 and .xz compression formats when importing Docker images: [portainer/portainer#5220](https://github.com/portainer/portainer/issues/5220)
* Enhancement of the Docker image import feature to support manually adding tags to the imported image: [portainer/portainer#5944](https://github.com/portainer/portainer/issues/5944)
* Improved how to change the image when editing a Service by pre-populating the fields in the UI: [portainer/portainer#5150](https://github.com/portainer/portainer/issues/5150)
* Fixed issue where automatic updates of stacks fail after restarting Portainer: [portainer/portainer#5914](https://github.com/portainer/portainer/issues/5914)
* Fixed issue where pull and redeploy button was not functioning as expected: [portainer/portainer#5948](https://github.com/portainer/portainer/issues/5948)
* Fixed UI issue when using a personal access token to deploy from Git: [portainer/portainer#5847](https://github.com/portainer/portainer/issues/5847)
* Fixed issue where certain docker events showed as Unsupported: [portainer/portainer#2717](https://github.com/portainer/portainer/issues/2717)
* Fixed issue with stack names when migrating from Swarm to docker standalone: [portainer/portainer#6139](https://github.com/portainer/portainer/issues/6139)
* Fixed issue where migrating a stack shows up twice: [portainer/portainer#5159](https://github.com/portainer/portainer/issues/5159)
* Fixed issue where using a webhook with an image registry running on a custom port did not work: [portainer/portainer#4526](https://github.com/portainer/portainer/issues/4526)
* Fixed issue where downloading container log files added extra carriage returns: [portainer/portainer#5312](https://github.com/portainer/portainer/issues/5312)
* Fixed issue where copying container log files added trailing commas: [portainer/portainer#4318](https://github.com/portainer/portainer/issues/4318)
* Fixed issue where the scale labels of the stats graph was showing multiple times: [portainer/portainer#5843](https://github.com/portainer/portainer/issues/5843)
* Fixed issue where stats were not working on windows containers: [portainer/portainer#5826](https://github.com/portainer/portainer/issues/5826)
* Fixed UI issue with empty stack dropdown when deploying an application via the form: [portainer/portainer#5848](https://github.com/portainer/portainer/issues/5848)
* Fixed issue with Custom Template on Docker being created when the file does not exist on a git repo: [portainer/portainer#6184](https://github.com/portainer/portainer/issues/6184)

### Portainer

* Fixed issue where upgrading from CE to BE failed due to missing RBAC roles
* Fixed trivy Helm and Portainer vulnerabilities relating to direct dependencies. [portainer/portainer#6342](https://github.com/portainer/portainer/issues/6342)
* Standard users will no longer be able to remove or export images. Also, Operators, Help Desk, and ready only users will no longer be able to export images.
* When changing the user password the user gets redirected to the login page: [portainer/portainer#6456](https://github.com/portainer/portainer/issues/6456)
* Fixed issue with default helm repo not populating in settings page
* Fixed ability for a Standard User to start/stop stacks [portainer/portainer#6369](https://github.com/portainer/portainer/issues/6369)
* Removed the integration with Storidge clusters: [portainer/portainer#6512](https://github.com/portainer/portainer/issues/6512)
* Changed the default Microsoft OAuth logout URL: [portainer/portainer#6405](https://github.com/portainer/portainer/issues/6405)
* Portainer users can no longer use their Portainer internal password when OAuth is enabled: [portainer/portainer#5889](https://github.com/portainer/portainer/issues/5889)
* Option to encrypt values in Portainer database: [portainer/portainer#6412](https://github.com/portainer/portainer/issues/6412)
* Added the ability to override the "Force HTTPS only" option: [portainer/portainer#6126](https://github.com/portainer/portainer/issues/6126)
* Supporting the ability for Portainer to run inside a subpath: [portainer/portainer#3901](https://github.com/portainer/portainer/issues/3901)
* Updated the defaults for the Git authentication toggles: [portainer/portainer#6406](https://github.com/portainer/portainer/issues/6406)
* Fixed display issue for environment tags in the Home page view [portainer/portainer#6276](https://github.com/portainer/portainer/issues/6276)
* Fixed issue where scrollbars would show in confirmation dialogs: [portainer/portainer#6257](https://github.com/portainer/portainer/issues/6257)
* Fixed issue where the `--sslcert` flag was being ignored: [portainer/portainer#6021](https://github.com/portainer/portainer/issues/6021)
* The ability for users to easily interact with the Portainer API through the use of Personal Access Tokens: [portainer/portainer#813](https://github.com/portainer/portainer/issues/813)
* Automatically sync Portainer dark/light theme with the browser dark/light theme settings: [portainer/portainer#5753](https://github.com/portainer/portainer/issues/5753)
* Fixed issue where the CPU and memory were not shown on the Home screen: [portainer/portainer#6143](https://github.com/portainer/portainer/issues/6143)
* Added confirmation modal when deleting an Environment: [portainer/portainer#5952](https://github.com/portainer/portainer/issues/5952)
* Fixed issue where removing an environment did not update the tree: [portainer/portainer#6127](https://github.com/portainer/portainer/issues/6127)
* Fixed issue where the DockerHub anonymous registry was being used instead of one with an account: [portainer/portainer#5896](https://github.com/portainer/portainer/issues/5896)
* Fixed issue where environment displayed as offline after starting Portainer: [portainer/portainer#5732](https://github.com/portainer/portainer/issues/5732)
* Fixed issue where the custom logo settings showed incorrectly in the UI: [portainer/portainer#4437](https://github.com/portainer/portainer/issues/4437)
* Fixed issue where uploading a backup file could not select a file on Mac: [portainer/portainer#5357](https://github.com/portainer/portainer/issues/5357)
* Fixed issue where apple touch Portainer icon had non standard image dimensions [portainer/portainer#5887](https://github.com/portainer/portainer/issues/5887)
* Fixed issue with widget header not displaying correctly for application settings: [portainer/portainer#6191](https://github.com/portainer/portainer/issues/6191)

### Edge

* Introduce the ability to pass env variables from a local system on edge devices to the edge stack
* Fixed minor UI behavior with toggles in Edge Compute settings view
* Fixed issue with displaying AMT device table for non-activated devices
* Fixed minor UI issues in Edge devices page view around Action buttons
* Introduced the ability to control and interact with OpenAMT: devices [portainer/portainer#6444](https://github.com/portainer/portainer/issues/6444)
* Introduce the ability to add edge devices through FDO: [portainer/portainer#6445](https://github.com/portainer/portainer/issues/6445)
* Added behavior for Edge agents to reject connections if not connected to within 72hrs: [portainer/portainer#6420](https://github.com/portainer/portainer/issues/6420)
* Optimize disk performance for Edge Agent [portainer/portainer#6455](https://github.com/portainer/portainer/issues/6455)
* Fixed issues with the Edge Agent reverse tunnel timing out: [portainer/portainer#5725](https://github.com/portainer/portainer/issues/5725)
* Fixed issue where the URL of an Environment would change to localhost: [portainer/portainer#5803](https://github.com/portainer/portainer/issues/5803)

### Registry

* Fixed issue with duplicating registries during upgrade process. [portainer/portainer#6062](https://github.com/portainer/portainer/issues/6062)
* Bring users the ability to use Amazon Elastic Container Registry: [portainer/portainer#1533](https://github.com/portainer/portainer/issues/1533)

### ACI

* Fixed issue where ACI stopped working when the number of exposed ports and container ports were different: [portainer/portainer#5335](https://github.com/portainer/portainer/issues/5335)

### Development

* Upgraded golang version to 1.17 [portainer/portainer#6342](https://github.com/portainer/portainer/issues/6342)
* Updated the Swagger documentation: [portainer/portainer#6019](https://github.com/portainer/portainer/issues/6019)
* Deprecated EndpointProvider in the code and moving away from its use: [portainer/portainer#5524](https://github.com/portainer/portainer/issues/5524)
* Introduced ReactJS support in the frontend: [portainer/portainer#6031](https://github.com/portainer/portainer/issues/6031)
* Updated docker and kubernetes library dependencies: [portainer/portainer#6137](https://github.com/portainer/portainer/issues/6137)
* Updated the Swagger documentation: [portainer/portainer#5338](https://github.com/portainer/portainer/issues/5338)
* Added logging to migrations: [portainer/portainer#6183](https://github.com/portainer/portainer/issues/6183)

## Release 2.10.0

November 15, 2021

### Known issues

* Both Portainer and the Agent need to be upgraded at the same time: [portainer/agent#187](https://github.com/portainer/agent/issues/187)
* Restarting Portainer will invalidate all downloaded Kubeconfig files: [portainer/portainer#5574](https://github.com/portainer/portainer/issues/5574)
* Access can not be assigned to registries when defining multiple registries with the same URL
* Browser cache causes UI abnormalities after upgrading from a prior version. Force a cache refresh (Ctrl-Shift-R) to remedy

### Breaking changes

* Default HTTPS support has been added: [portainer/portainer#5462](https://github.com/portainer/portainer/issues/5462)

  As a consequence the `--ssl` flag has been deprecated. If you are using the `--sslcert` and `--sslkey` flags, then after the upgrade port `9000` will serve `http` and port `9443` will serve `https` with the provided certificate. To retain the old behavior consider using the port mapping `-p 9000:9443` instead.
* The `/stacks` API has renamed from `ComposeFilePathInRepository` to `ComposeFile`, and the non-mandatory fields `AdditionalFiles` and `AutoUpdate` were added: [portainer/portainer#5461](https://github.com/portainer/portainer/issues/5461)

### Security

* It is advisable to upgrade to this version, since some security improvements have been made with regards to embedding images: [portainer/portainer#5805](https://github.com/portainer/portainer/issues/5805)

### Kubernetes

* Introduced the ability to keep the deployments of stacks and applications in sync with the definitions in Git
* Introduced the ability to open a shell in Portainer to use kubectl: [portainer/portainer#5574](https://github.com/portainer/portainer/issues/5574)
* Introduced the ability to download a kubeconfig file and use Portainer as a proxy: [portainer/portainer#5574](https://github.com/portainer/portainer/issues/5574)
* Introduced the ability to install Helm charts: [portainer/portainer#5479](https://github.com/portainer/portainer/issues/5479)
* Introduced the ability to use any public Helm repository: [portainer/portainer#5480](https://github.com/portainer/portainer/issues/5480)
* Introduced the ability to automatically sync a manifest from a git repository: [portainer/portainer#5494](https://github.com/portainer/portainer/issues/5494)
* Introduced a visual indicator for applications to see if they're fully replicated: [portainer/portainer#5718](https://github.com/portainer/portainer/issues/5718)
* Introduced the ability to filter Kubernetes applications by type: [portainer/portainer#5726](https://github.com/portainer/portainer/issues/5726)
* Introduced the ability to remove all workloads of a manifest based deployment: [portainer/portainer#5715](https://github.com/portainer/portainer/issues/5715)
* Added the ability to display Helm chart deployments in the applications list: [portainer/portainer#5478](https://github.com/portainer/portainer/issues/5478)
* Added the ability to update and redeploy an application created from a git repository: [portainer/portainer#5486](https://github.com/portainer/portainer/issues/5486)
* Added support for deploying images stored on private registries for Docker and Kubernetes: [portainer/portainer#4393](https://github.com/portainer/portainer/issues/4393)&#x20;
* Introduced the ability to mark and unmark namespaces as system: [portainer/portainer#4389](https://github.com/portainer/portainer/issues/4389)
* Added functionality to define a manifest as custom template: [portainer/portainer#5489](https://github.com/portainer/portainer/issues/5489)
* Added the ability to deploy a manifest from a URL: [portainer/portainer#5556](https://github.com/portainer/portainer/issues/5556)
* Added memory and CPU usage indicators to the namespace and cluster details: [portainer/portainer#5460](https://github.com/portainer/portainer/issues/5460)
* Added status information to list of namespaces: [portainer/portainer#5555](https://github.com/portainer/portainer/issues/5555)
* Added Pod IP address information to the application details: [portainer/portainer#5713](https://github.com/portainer/portainer/issues/5713)
* Added input validation when adding an ingress: [portainer/portainer#5716](https://github.com/portainer/portainer/issues/5716)
* Improved the validation of resource allocation available on any of the nodes when adding an application: [portainer/portainer#5530](https://github.com/portainer/portainer/issues/5530)
* Improved UI so that accessing the advanced deployment functionality is similar to accessing the form: [portainer/portainer#5558](https://github.com/portainer/portainer/issues/5558)
* Renamed configuration and the networking area in the UI: [portainer/portainer#5804](https://github.com/portainer/portainer/issues/5804)
* Improved UI for the metrics API toggle in the cluster setup: [portainer/portainer#5508](https://github.com/portainer/portainer/issues/5508)
* Removed validation of any ingresses that are already in use in other namespaces: [portainer/portainer#5526](https://github.com/portainer/portainer/issues/5526)
* Introduced the ability to use Edge Stacks on Kubernetes via edge agents: [portainer/portainer#5472](https://github.com/portainer/portainer/issues/5472)
* Added warning that a secret will be created when adding registry access to a namespace: [portainer/portainer#5845](https://github.com/portainer/portainer/issues/5845)
* Fixed issue where the metrics server API was being queried when disabled: [portainer/portainer#5523](https://github.com/portainer/portainer/issues/5523)
* Fixed issue where the node events would not be showing: [portainer/portainer#5474](https://github.com/portainer/portainer/issues/5474)
* Fixed issue where applications deployed via Helm in Portainer were marked as external: [portainer/portainer#5727](https://github.com/portainer/portainer/issues/5727)
* Fixed issue where the kubectl shell would close when performing other actions: [portainer/portainer#5721](https://github.com/portainer/portainer/issues/5721)
* Fixed issue where the kubectl shell wasn't working when Portainer runs on ARM64: [portainer/portainer#5723](https://github.com/portainer/portainer/issues/5723)
* Fixed issue where the cluster status was incorrectly shown: [portainer/portainer#5293](https://github.com/portainer/portainer/issues/5293)
* Fixed issue where the application details incorrectly showed how it was deployed : [portainer/portainer#5728](https://github.com/portainer/portainer/issues/5728)
* Fixed issue where standard users were unable to access the pod and node stats view: [portainer/portainer#5898](https://github.com/portainer/portainer/issues/5898)
* Fixed issue where editing an application could not expose it via Ingress: [portainer/portainer#5915](https://github.com/portainer/portainer/issues/5915)
* Fixed issue when clearing Helm repo in global settings and added text notification in Helm charts page: [portainer/portainer#5996](https://github.com/portainer/portainer/issues/5996)
* Fixed issue where Helm charts fail to load in ARM cloud environments: [portainer/portainer#5937](https://github.com/portainer/portainer/issues/5937)
* Fixed issue where the namespace details page showed an object object error: [portainer/portainer#5802](https://github.com/portainer/portainer/issues/5802)
* Fixed issue where Environment variables with empty values are not showing when editing a Kubernetes application
* Fixed issue where standard users could not see the quota set in the namespace details page

### Docker

* Introduced the ability to keep the deployments of stacks and applications in sync with the definitions in Git
* Introduced the ability to automatically sync a stack from a git repository: [portainer/portainer#5461](https://github.com/portainer/portainer/issues/5461)
* Introduced the ability to use stacks on docker standalone on ARM64: [portainer/portainer#4776](https://github.com/portainer/portainer/issues/4776)
* Introduced the ability to use Edge Stacks on ARM64: [portainer/portainer#4776](https://github.com/portainer/portainer/issues/4776)
* Added support for deploying images stored on private registries for Docker and Kubernetes: [portainer/portainer#4393](https://github.com/portainer/portainer/issues/4393)
* Added the ability to edit a stopped stack: [portainer/portainer#4944](https://github.com/portainer/portainer/issues/4944)
* Added the ability to edit environment variables for stacks on docker standalone: [portainer/portainer#3441](https://github.com/portainer/portainer/issues/3441)
* Docker container stats graphs now support cgroups v2: [portainer/portainer#4818](https://github.com/portainer/portainer/issues/4818)
* Improved how to change the image when editing a Service by pre-populating the fields in the UI: [portainer/portainer#5150](https://github.com/portainer/portainer/issues/5150)
* Fixed issue where all images regardless of their tag would be pulled: [portainer/portainer#4870](https://github.com/portainer/portainer/issues/4870)
* Fixed issue where volumes would lose their access control settings: [portainer/portainer#4851](https://github.com/portainer/portainer/issues/4851)
* Fixed issue where standard users were unable to browse volumes created by stacks: [portainer/portainer#4929](https://github.com/portainer/portainer/issues/4929)
* Fixed issue where ports would show for IPv4 as well as IPv6: [portainer/portainer#5038](https://github.com/portainer/portainer/issues/5038)
* Fixed issue where `container_name` validation would not take stopped containers into account: [portainer/portainer#5522](https://github.com/portainer/portainer/issues/5522)
* Fixed issue where editing a stack would warn about the container name being in use: [portainer/portainer#5130](https://github.com/portainer/portainer/issues/5130)
* Fixed issue where navigating away incorrectly showed a changes not saved popup: [portainer/portainer#5512](https://github.com/portainer/portainer/issues/5512)
* Fixed issue where the stack name would contain spaces or upper case characters: [portainer/portainer#5153](https://github.com/portainer/portainer/issues/5153)
* Fixed issue where the UI would incorrectly report that an image was successfully pulled: [portainer/portainer#3123](https://github.com/portainer/portainer/issues/3123)
* Fixed issue where the Stack editor would not always load its content: [portainer/portainer#5102](https://github.com/portainer/portainer/issues/5102)
* Fixed issue where environment variables were incorrectly showing when the value contained an equals sign: [portainer/portainer#5395](https://github.com/portainer/portainer/issues/5395)
* Fixed issue where the browser console would show errors in the container and image details view: [portainer/portainer#5511](https://github.com/portainer/portainer/issues/5511)
* Fixed issue where dashes and underscores in stack names were being removed: [portainer/portainer#5759](https://github.com/portainer/portainer/issues/5759)
* Fixed UI issue where adding a Service with a mix of TCP and UDP was being prevented: [portainer/portainer#5521](https://github.com/portainer/portainer/issues/5521)
* Fixed issue where images could be used in custom templates notes: [portainer/portainer#5805](https://github.com/portainer/portainer/issues/5805)
* Fixed issue where automatic updates would keep polling when the user that created the stack is removed: [portainer/portainer#5719](https://github.com/portainer/portainer/issues/5719)
* Fixed issue where automatic updates of stacks fail after restarting Portainer: [portainer/portainer#5914](https://github.com/portainer/portainer/issues/5914)
* Fixed issue where stack names were not being validated when using custom templates: [portainer/portainer#5841](https://github.com/portainer/portainer/issues/5841)
* Fixed issue where stats were not working on windows containers: [portainer/portainer#5826](https://github.com/portainer/portainer/issues/5826)
* Fixed issue where the scale labels of the stats graph was showing multiple times: [portainer/portainer#5843](https://github.com/portainer/portainer/issues/5843)
* Fixed UI issue when using a personal access token to deploy from Git: [portainer/portainer#5847](https://github.com/portainer/portainer/issues/5847)
* Fixed UI issue with empty stack dropdown when deploying an application via the form: [portainer/portainer#5848](https://github.com/portainer/portainer/issues/5848)
* Fixed issue where migrating a stack shows up twice: [portainer/portainer#5159](https://github.com/portainer/portainer/issues/5159)
* Fixed issue where switching from docker standalone to swarm would show duplicate stacks

### Portainer

* Added automatic updates of stacks and applications to the activity logs
* Introduced the ability to define a time based change window in which automatic updates of stacks and applications can take place
* Introduced the ability to automatically set OAuth users as a Portainer Admin
* Introduced the ability to automatically set LDAP users as a Portainer Admin
* Added a Portainer and Agent Juju Charm to the Charmhub marketplace
* Introduced dark theme and high contrast mode: [portainer/portainer#5493](https://github.com/portainer/portainer/issues/5493)
* Introduced the ability to access Portainer via HTTPS: [portainer/portainer#5462](https://github.com/portainer/portainer/issues/5462)
* Renamed Endpoints to Environments in the UI: [portainer/portainer#5492](https://github.com/portainer/portainer/issues/5492)
* Improved the menu UI to indicate the existence of sub items: [portainer/portainer#5528](https://github.com/portainer/portainer/issues/5528)
* Improved UI how to add environments to Portainer when doing a new installation: [portainer/portainer#5477](https://github.com/portainer/portainer/issues/5477)
* Added functionality to copy error messages from toast notifications: [portainer/portainer#5720](https://github.com/portainer/portainer/issues/5720)
* Improved how a Portainer upgrade can be rolled back: [portainer/portainer#5482](https://github.com/portainer/portainer/issues/5482)
* Improved UI where the table background wasn't working very well in dark mode: [portainer/portainer#5714](https://github.com/portainer/portainer/issues/5714)
* Fixed issue where Git content could not be cloned when Portainer is behind a proxy: [portainer/portainer#3286](https://github.com/portainer/portainer/issues/3286)
* Fixed issue where the SSL certificates were not included in the Portainer backup: [portainer/portainer#5497](https://github.com/portainer/portainer/issues/5497)
* Fixed issue where editing an endpoint results in errors: [portainer/portainer#5318](https://github.com/portainer/portainer/issues/5318)
* Fixed upgrade issue where disconnected endpoints caused the upgrade to fail: [portainer/portainer#5764](https://github.com/portainer/portainer/issues/5764)
* Fixed issue with the layout of the add Environment Wizard: [portainer/portainer#5801](https://github.com/portainer/portainer/issues/5801)
* Fixed issue where the custom logo was not used in all places: [portainer/portainer#5447](https://github.com/portainer/portainer/issues/5447)
* Fixed issue where the DockerHub anonymous registry was being used instead of one with an account: [portainer/portainer#5896](https://github.com/portainer/portainer/issues/5896)
* Fixed issue where upgrade fails: [portainer/portainer#5969](https://github.com/portainer/portainer/issues/5969)
* Fixed issue where the Quick Setup wizard wasn't showing correctly when using the dark theme: [portainer/portainer#5842](https://github.com/portainer/portainer/issues/5842)
* Fixed issue where uploading a backup file could not select a file on Mac: [portainer/portainer#5357](https://github.com/portainer/portainer/issues/5357)
* Fixed issue where the URL of an Environment would change to localhost: [portainer/portainer#5803](https://github.com/portainer/portainer/issues/5803)
* Fixed issue where RBAC settings would be retained after removing an Environment from Portainer
* Fixed issue where certificates would end up in the activity logs
* Fixed issue when exporting activity logs as CSV without a data range set
* Added a build for Windows Server 20H2: [portainer/portainer#4971](https://github.com/portainer/portainer/issues/4971)
* Added a build for Windows Server 21H2: [portainer/portainer#5763](https://github.com/portainer/portainer/issues/5763)

### Registries

* Improved UI to provide information for correctly using a ProGet registry: [portainer/portainer#5510](https://github.com/portainer/portainer/issues/5510)
* Fixed UI issue where the registry list incorrectly showed that there's no registry available: [portainer/portainer#5731](https://github.com/portainer/portainer/issues/5731)

### ACI

* Fixed issue where ACI stopped working when the number of exposed ports and container ports were different: [portainer/portainer#5335](https://github.com/portainer/portainer/issues/5335)
* Fixed issue where ACI would show errors when a resource group had multiple containers: [portainer/portainer#5335](https://github.com/portainer/portainer/issues/5335)

### Edge

* Introduced the ability to use Edge Stacks on Kubernetes via Edge Agents: [portainer/portainer#5472](https://github.com/portainer/portainer/issues/5472)
* Introduced the ability to re-associate an edge endpoint to a new Edge Agent: [portainer/portainer#5473](https://github.com/portainer/portainer/issues/5473)
* Improved the REST API access of the Edge Agent in Docker standalone: [portainer/agent#187](https://github.com/portainer/agent/issues/187)
* Fixed issue where the heartbeat indicator was not reliable: [portainer/portainer#5569](https://github.com/portainer/portainer/issues/5569)
* Fixed issues with the Edge Agent reverse tunnel timing out: [portainer/portainer#5725](https://github.com/portainer/portainer/issues/5725)

### Development

* Added the ability to query the endpoints by type through the Portainer API: [portainer/portainer#4786](https://github.com/portainer/portainer/issues/4786)
* Integrated with Logrus for the internal logging mechanism: [portainer/portainer#5509](https://github.com/portainer/portainer/issues/5509)
* Updated the Golang version to 1.16: [portainer/portainer#5463](https://github.com/portainer/portainer/issues/5463)
* Improved the Portainer API documentation for adding users: [portainer/portainer#5136](https://github.com/portainer/portainer/issues/5136)
* Fixed inconsistencies in the Portainer API documentation: [portainer/portainer#5527](https://github.com/portainer/portainer/issues/5527)
* Updated the Swagger documentation: [portainer/portainer#5338](https://github.com/portainer/portainer/issues/5338)

## Release 2.7.0

July 29, 2021

### **Docker**

* Added the ability to update and redeploy a stack created from a git repository
* Added I/O usage to the container statistics
* Enhanced environment variables UI/UX for Docker
* sysctl options are available when creating a container
* Show the number of Swarm nodes for the endpoint on the Home page
* Show how many Docker pulls are remaining for DockerHub to avoid exceeding the quota
* Introduced support for compose version 3.8 on docker swarm environments
* Display the container IP address(es) in the list of containers
* Improved layout of the toggles on the create container setting tab
* For Docker Standalone, prevent a stack from being created if the Compose has a container\_name that already exists
* Creating a container from a DockerHub image will show a search button in the UI
* Fixed issue where deploying a stack from Git did not work for Azure DevOps
* Fixed issue where stacks with a status of 0 are hidden in the UI
* Fixed issue where pulling a large image is failing when using an Agent due to a timeout
* Fixed issue where listing the services with Auto-refresh on collapses all services after refresh
* Fixed issue where dash characters got removed from the stack name on Docker Standalone
* Fixed issue where access control management via labels was not fault tolerant
* Fixed issue where the label showing the default location of secrets was incorrect for Windows
* Fixed typo in the error message "Unable to start stack"

### **Registries**

* Added ProGet as a specific registry type when adding a registry
* Fixed issue where pushing to a quay.io registry failed due to not including the username in the quay registry URL

### **Templates**

* Fixed issue where creating a custom template from uploading a compose file failed
* Fixed issue where switching custom template in the template tab of stack create view doesn't update editor
* Fixed issue with an invalid template documentation URL in the Settings

### **Volumes**

* Added validation to prevent adding empty mount to an existing service
* Fixed issue with the MountType and nfsvers when creating NFS4 volumes
* Fixed issue where editing the properties of volumes on a service did not enable the apply button

### **Kubernetes**

* Introduced the ability to deploy a manifest from a git repository when using advanced deployment
* The advanced deployment feature has been made available to standard users
* Introduced a summary of Kubernetes actions when deploying a Kubernetes resource
* Added the ability to display realtime node metrics in Kubernetes
* Added functionality to allow multiple ingress networks per kubernetes namespace, with a differing config per ingress
* Added the ability to redeploy an externally deployed application
* Added the ability to expand the YAML tab of a Kubernetes application to full size
* Added the ability to cordon/uncordon/drain nodes
* Added a warning in the placement tab when an application can't be scheduled on the cluster
* Renamed Resource Pools to Namespaces in the UI
* Improved UI for the placement policies when creating an application
* Improved how application image names are shown
* Form validation has been added for Configuration keys
* Environment variable are sorted alphabetically to improve the readability
* Display the ImagePull policy in the details of an application
* Default to the kube-system namespace in the advanced deployment view on ARM
* Fixed minor UI inconsistency when creating an application with an ingress
* Fixed issue with the UI layout when creating an application with ingress
* Fixed issue where updating the Kubernetes endpoint URL did not get persisted
* Fixed issue where the endpoint url is not updated when updating a kubernetes local endpoint
* Fixed issue where renaming the endpoint of a kubernetes agent breaks the endpoint
* Fixed issue where environment variables with empty values are not showing when editing a kubernetes application
* Fixed issue where environment variable validation when creating an application was too restrictive
* Fixed issue where creating an application with two different ingresses incorrectly populates the hostname UI fields
* Fixed issue where an application with persisted data can't update, after the storage option is disabled in the cluster settings
* Fixed issue where adding an ingress route is not prevented when editing an application with existing ingress route and ingress is disabled
* Fixed issue where adding an application does not allow Global to be set

### **ACI**

* Fixed issue where ACI stops working after persistence or networking gets added

### **Edge**

* Added the ability to deploy Edge stacks on Docker standalone Edge endpoints
* Show the status of the edge agent check-in on the home page dashboard
* Hide the webhook UI in the service creation view of an edge endpoint, since it's not applicable
* Fixed issue where accessing a down Kubernetes Edge endpoint should redirect the user to the home view

### **Portainer**

* Added the ability to sync Portainer teams with group memberships provided via OAuth
* Added SSO support for OAuth and do not enforce a login prompt. Use `<portainer_url>/#!/internal-auth` to login with internal admin.
* Added the ability to manage orphaned stacks when Portainer has the compose file
* Added the option to specify the local socket location when adding a docker endpoint
* Search filters are retained within the browser session
* Properly expose backend error when using image management features
* Prevent web editor related views from being accidentally closed
* Improved descriptions for Portainer initialization errors
* Disable sysctl settings for non-administrators incorrectly defaults to being on
* Fixed issue where the File select windows gets shown when pressing enter in text fields
* Fixed issue where restoring Portainer from a backup file fails in certain circumstances related to the activity logs
* Fixed issue where a custom snapshot interval cannot be changed
* Fixed issue with incorrect Windows agent deployment command in the agent endpoint creation tab

### **Podman**

* Introduced initial experimental support for Podman. Known limitations are listed in <https://github.com/portainer/portainer/issues/5188>

### **Development**

* Introduce buildx to support Windows 1903+ Base Images
* Added the ability to debug through VSCode
* Added check for missing angularJS inject annotation
* Removed grunt-karma ang grunt-html2js dependencies
* Fixed issue where webpack complains about charset source maps
* Fixed issue where babel complains about missing core-js dependency

### **Known Issues**

* Logging into Portainer as a Standard User fails to load home page when using 'microk8s v1.21.3-3+6343a564e351b0'
* Host Management features do not work on Windows Hosts [#4450](https://github.com/portainer/portainer/issues/4450)
* Host Browser function does not work for Non-Admin users.

## Release 2.4.0

May 4, 2021

### **Kubernetes​**

* Pods without workloads are now displayed as applications
* Improved UI/UX of configurations for creation / edition
* Introduced request of confirmation upon volume removal
* Introduced the advanced deployment panel to each resource list view
* Updated validation to prevent a user from exposing an application over an external load balancer with mixed protocols
* Introduced the ability to display the access policy associated to the storage of a volume
* Clarified advanced deployment feature
* Clarified sensitive configuration creation
* Clarified ingress controller configuration in the cluster setup view
* Renamed the create entry from file button when creating a configuration
* Improved validation warnings in the application creation / edition views
* Removed extra whitespace in stacks and storage datatables
* Fixed issue with access management feature on resource pools
* Fixed issue with ability to retrieve configs when a config is a binary file
* Fixed issue with advanced deployment feature on agent and Edge agent endpoints
* Fixed an issue that would mark a sensitive configuration as external without owner after an update
* Fixed issue with access to configuration details view for a configuration containing binary data
* Fixed labels to display system labels first in the node details view
* Fixed refresh issue on the view with the YAML panel selected
* Fixed invalid display issue when accessing the load balancer panel from the application panel
* Fixed issue when accessing the cluster setup incorrectly expanding the Endpoint sidebar
* Fixed issue with exposed configuration keys over filesystem inside an application not being applied
* Fixed issue when Adding a key to existing used configuration that would throw an error when editing an application using that configuration
* Fixed an issue with the form validation in the configuration creation view
* Fixed issue with resource pool “created” attribute not showing actual creation time
* Fixed issue with ability to apply a note to a Pod type application
* Fixed issue with creating Kubernetes resources with a username longer than 63 characters
* Fixed issue with special characters in usernames when creating Kubernetes resources
* Fixed issue with ability to retrieve config map error when trying to manager newly create resource pool​

### **Activity Logging ​**

* Introduced user authentication activity logging
* Introduced user activity logging​

### **RBAC ​**

* Introduced new RBAC “Operator” Role
* Fixed issue with user in 2 team with mix of helpdesk & endpoint admin resulting in the user having permissions of endpoint admin​

### **Registries ​**

* Fixed issue causing Portainer to forget the password associated to a registry after an update
* Fixed issue preventing the registry manager feature to work properly with a ProGet registry
* Improved description for advanced mode usage with private registries​

### **Swarm ​**

* Introduced validation to prevent adding a mount with nothing filled to and exiting service
* Fixed issue in service creation, switching to bind mode from volume mode with a volume selected fills the host field with {object Object}​

### **Stacks ​**

* Introduced support for creating stacks with the same name across different endpoints
* Introduced extra stack information: creation, last update time and user who created the stack
* Minor UX change for the start/stop stack action
* Fixed issue with ability to use private registries with Standalone stacks
* Fixed issue showing editor tab on limited stacks when it should not
* Fixed issue when editing a stack, hitting backspace or delete keys with contents of web editor selected hides the entire editor UI element
* Fixed issue with stack create via API with a regular user account are incorrectly marked as administrator only
* Fixed issue of error being displayed when creating a stack on docker standalone despite the stack is created
* Fixed issue of stacks being created via API incorrectly marked private with no owner​

### **Docker ​**

* Introduced support for Compose > v2 when deploying a stack on a Docker standalone environment
* Introduced the ability to download log file from Docker container/service views
* Display labels in Image Details
* Clarify the description of the restrict external access to the network property when creating a network​

### **User Management ​**

* Automatically lowercase username when authenticating users
* Update the authentication UX to put an emphasis on OAuth when OAuth is enabled​

### **Portainer**

* Introduced the ability to backup / restore Portainer
* Fixed issue of version not being shown correctly after update
* Support starting Portainer without having to specify any endpoint​

### **ACI**

* Introduced RBAC to ACI
* Introduced UAC to ACI​

### **Minor Changes​**

* Removed the new version check
* Changed the license server errors to be a silent fail for offline environments
* Added JS source map for Portainer UI

## Release 2.0.1

February 22, 2021

### **Fixes**

* **Fix an issue preventing a user from creating Kubernetes resources if they have a `@` character in their username**\
  Users with a `@` character in their username were not able to create the following Kubernetes resources:
  * Resource pool
  * Application
  * Configuration
* **Fix platform issues with the Docker image for Portainer Business**\
  The Docker image can now be successfully deployed on the following platforms:
  * Linux ARM64
  * Linux ARM
* **Minor update to the license server mechanism**\
  The license server mechanism has been updated.

## Release 2.0.0

December 3, 2020

Initial release of Portainer Business


# Introduction

This section explains the Portainer architecture and how to install it. We recommend that you read the entire section to ensure your installation goes smoothly.

Learn about the [architecture](https://docs.portainer.io/start/architecture) first, get familiar with the [prerequisites to installation](https://docs.portainer.io/start/requirements-and-prerequisites), then finally, step through how to [install the product](https://docs.portainer.io/start/install) in your environment.

{% content-ref url="architecture" %}
[architecture](https://docs.portainer.io/start/architecture)
{% endcontent-ref %}


# Portainer architecture

## Overview of Portainer architecture

Portainer consists of two elements: the Portainer Server and the Portainer Agent. Both run as lightweight containers on your existing containerized infrastructure. The Portainer Agent should be deployed to each node in your cluster and configured to report back to the Portainer Server container.

{% hint style="info" %}
For a deeper dive into the architecture of Portainer, have a look at our [technical architecture overview](https://dl.portainer.io/dl/whitepapers/portainer-technical-architecture.pdf).
{% endhint %}

A single Portainer Server will accept connections from any number of Portainer Agents, providing the ability to manage multiple clusters from one centralized interface. To do this, the Portainer Server container requires data persistence. The Portainer Agents are stateless, with data being shipped back to the Portainer Server container.

<figure><img src="https://2837857291-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxdTQRpMuktD2l0URtOJO%2Fuploads%2FyEAvW327tFa9AoEfRcen%2F2.38-portainer-architecture-detailed.png?alt=media&#x26;token=84ca8e46-7b8c-4600-8676-5f80694da60c" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
We don't currently support running multiple instances of the Portainer Server container to manage the same clusters. We recommend running the Portainer Server on a specific management node, with Portainer Agents deployed across the remaining nodes.
{% endhint %}

## Agent vs Edge Agent

In most instances we recommend using the Edge Agent rather than the classic Agent when managing environments. With the Edge Agent, rather than the Portainer Server needing seamless access to the remote environment, only the remote environments need to be able to access the Portainer Server. This communication is performed over an encrypted TLS tunnel. This is important in Internet-connected configurations where there is no desire to expose the Portainer Agent to the internet.

In contrast, in classic Agent deployments the central Portainer Server accesses the environments, i.e. Portainer → Agents. As such, any environments it manages are assumed to be on the same network as the Portainer Server so it can securely communicate with Portainer Agents.

The classic Agent option remains for legacy purposes, and can still be used for local network scenarios, but it is worth noting that features such as Fleet Governance Policies are not available with the classic Agent.

## Security and compliance

Portainer runs exclusively on your servers, within your network, behind your own firewalls. As a result, we do not currently hold any SOC or PCI/DSS compliance because we do not host any of your infrastructure. You can even run Portainer completely disconnected (air-gapped) without any impact on functionality.

{% content-ref url="lifecycle" %}
[lifecycle](https://docs.portainer.io/start/lifecycle)
{% endcontent-ref %}


# Lifecycle policy

Portainer makes this policy public so customers and partners can effectively plan, deploy, and support their container management infrastructure effectively using Portainer. It is published in an effort to provide as much transparency as possible but Portainer has the discretion to make exceptions from this policy should that be in Portainer’s or our customer’s best interests.

Any release dates are provided for guidance only and the exact dates may change.

## The Portainer lifecycle

Portainer releases approximately follow a monthly cadence for minor releases (X.Y) which can introduce feature enhancements and new features but endeavor to maintain backward compatibility.

Micro or patch releases (X.Y.z) are released as needed and are limited to backward compatible bug fixes only.

Major versions (X) will be much less frequent, will include potential breaking changes, and may require an upgrade or migration process from previous versions.

All releases are cumulative - all previous enhancements and fixes are included in each release.

## Terminology

### Supported versus maintained

When we say “supported”, we are referring to the commercial support that is included with Portainer Business Edition subscriptions at the Scale and Enterprise level. This includes access to all STS and LTS releases and patches. Our [support terms](https://www.portainer.io/support-terms) have more detail on what is and isn’t covered by our support.

For Starter, Home & Student, our free Business Edition offerings, and our Community Edition, support is provided through our [community support channels](https://www.portainer.io/get-support-for-portainer).

The term “maintained” refers to the act of releasing updated versions of our releases, for example patches to resolve bugs or security issues. All editions of Business Edition and Community Edition will be maintained according to each release’s respective lifecycle.

Portainer always recommends updating to the latest version in the release stream to ensure you have the latest security fixes, bug fixes, and performance improvements. It is at Portainer’s discretion to backport fixes to any version outside of the supported version window.

### STS versus LTS

Portainer has two release streams, STS and LTS and it’s important you know the differences so you can choose accordingly.

#### **Short Term Support (STS) releases**

Short Term Support releases are identified with an “STS” suffix.

These are supported and maintained until the release of the next STS or LTS version. Use STS versions if you are interested in getting the latest features faster and don’t mind upgrading more frequently, and are fine with potential bugs that weren't picked up in testing.

{% hint style="info" %}
While we *do* perform automated and manual testing on STS releases, the testing is not as intense as that done for our LTS releases.
{% endhint %}

#### **Long Term Support (LTS) releases**

Long Term Support releases are identified with an “LTS” suffix.

These releases are supported and maintained until the release of the next LTS version plus a three month migration window so are more suitable for environments where adding new features on a frequent basis is less desirable. They also undergo intense testing before release, more so than the STS releases.

{% hint style="info" %}
Portainer LTS releases focus less on new features and more on stability so Portainer recommends LTS releases for production workloads.
{% endhint %}

## Current and planned releases

Each stream (LTS and STS) will have a number of patch releases throughout it’s life. The current LTS release is highlighted in bold.

### Current releases

| Release      | Release Date | End of support/maintenance |
| ------------ | ------------ | -------------------------- |
| **2.33 LTS** | **Aug 2025** | **May 2026**               |
| **2.39 LTS** | **Feb 2026** | **Nov 2026**               |

### Planned releases

We intend to release a new version every month, with a new LTS release (in bold below) every 6 months.

| Release      | Release Date | End of support/maintenance |
| ------------ | ------------ | -------------------------- |
| 2.40 STS     | Mar 2026     | Apr 2026                   |
| 2.41 STS     | Apr 2026     | May 2026                   |
| 2.42 STS     | May 2026     | Jun 2026                   |
| 2.43 STS     | Jun 2026     | Jul 2026                   |
| 2.44 STS     | Jul 2026     | Aug 2026                   |
| **2.45 LTS** | **Aug 2026** | **May 2027**               |

<figure><img src="https://2837857291-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxdTQRpMuktD2l0URtOJO%2Fuploads%2Fqme8vGbdmDkU2cEIhx3x%2F2.39-release-schedule.png?alt=media&#x26;token=91bbc770-2a2a-4023-8b2f-b895cd9872d2" alt=""><figcaption></figcaption></figure>

Sitting on an older release that is no longer maintained or supported is strongly discouraged and users take full responsibility for doing so. Users are strongly encouraged to ensure they are running the latest patch release for a given stream.

## Older releases that are no longer supported or maintained

The following releases have passed the end of support date and are no longer maintained or supported. If you are using one of these versions (or older), we recommend that you [update](https://docs.portainer.io/start/upgrade) as soon as possible.

| Release      | Release Date | End of support/maintenance |
| ------------ | ------------ | -------------------------- |
| 2.38 STS     | Jan 2026     | Feb 2026                   |
| 2.37 STS     | Dec 2025     | Jan 2026                   |
| 2.36 STS     | Nov 2025     | Dec 2025                   |
| 2.35 STS     | Oct 2025     | Nov 2025                   |
| 2.34 STS     | Sep 2025     | Oct 2025                   |
| 2.32 STS     | Jul 2025     | Aug 2025                   |
| 2.31 STS     | Jun 2025     | Jul 2025                   |
| 2.30 STS     | May 2025     | Jun 2025                   |
| 2.29 STS     | Apr 2025     | May 2025                   |
| 2.28 STS     | Mar 2025     | Apr 2025                   |
| **2.27 LTS** | **Feb 2025** | **Nov 2025**               |
| 2.26 STS     | Jan 2025     | Feb 2025                   |

## Notes

Portainer uses the [semantic versioning scheme](https://semver.org/) and while Portainer endeavors to follow best practices, we reserve the right to make exceptions should that be in Portainer’s and our user’s best interests.

For information on the available options and best practices for updating Portainer deployments, [refer to our update documentation](https://docs.portainer.io/start/upgrade).

{% content-ref url="requirements-and-prerequisites" %}
[requirements-and-prerequisites](https://docs.portainer.io/start/requirements-and-prerequisites)
{% endcontent-ref %}


# Requirements and prerequisites

Requirements specific to your environment will be covered in the installation process.

## Valid configurations

Every Portainer release goes through functional, release and post-release testing to ensure it works as expected. Because we cannot test against every configuration variant out there, we test against a subset.

The following tables list all of the configurations that we have tested, validated and consider to be functional. If a variant is not listed, it doesn't mean it won't work, it just means it hasn't been tested.

### Portainer Business Edition (BE)

| Portainer Version                                                                   | Release Date       | Docker Version            | Kubernetes Version | Podman Version | Architectures                                                                                          |
| ----------------------------------------------------------------------------------- | ------------------ | ------------------------- | ------------------ | -------------- | ------------------------------------------------------------------------------------------------------ |
| [Business 2.39.0 LTS](https://docs.portainer.io/release-notes#release-2.39.0-lts)   | February 26, 2026  | 28.5.1 29.2.1             | 1.32 1.33 1.34     | 5.6.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.38.1 STS](https://docs.portainer.io/release-notes#release-2.38.1-sts)   | February 13, 2026  | 28.5.1 29.2.1             | 1.32 1.33 1.34     | 5.6.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.38.0 STS](https://docs.portainer.io/release-notes#release-2.38.0-sts)   | January 29, 2026   | 28.5.1 29.1.2             | 1.32 1.33 1.34     | 5.6.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.37.0 STS](https://docs.portainer.io/release-notes)                      | December 11, 2025  | 28.5.1 29.1.1             | 1.32 1.33 1.34     | 5.6.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.33.5 LTS](https://docs.portainer.io/release-notes#release-2.33.4-lts)   | November 27, 2025  | 28.5.1 29.0.0             | 1.32 1.33 1.34     | 5.6.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.36.0 STS](https://docs.portainer.io/release-notes#release-2.36.0-sts)   | November 27, 2025  | 28.5.1 29.0.0             | 1.32 1.33 1.34     | 5.6.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.33.4 LTS](https://docs.portainer.io/release-notes#release-2.33.4-lts-1) | November 20, 2025  | 27.5.1 28.5.1             | 1.32 1.33 1.34     | 5.6.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.33.3 LTS](https://docs.portainer.io/release-notes#release-2.33.3-lts)   | October 30, 2025   | 27.5.1 28.5.1             | 1.32 1.33 1.34     | 5.6.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.35.0 STS](https://docs.portainer.io/release-notes#release-2.35.0-sts)   | October 16, 2025   | 27.5.1 28.4.0             | 1.31 1.32 1.33     | 5.6.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.33.2 LTS](https://docs.portainer.io/release-notes#release-2.33.2-lts)   | September 25, 2025 | 27.5.1 28.4.0             | 1.31 1.32 1.33     | 5.6.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.34.0 STS](https://docs.portainer.io/release-notes#release-2.34.0-sts)   | September 18, 2025 | 27.5.1 28.3.3             | 1.31 1.32 1.33     | 5.5.1          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.33.1 LTS](https://docs.portainer.io/release-notes#release-2.33.1-lts)   | August 27, 2025    | 27.5.1 28.3.2             | 1.31 1.32 1.33     | 5.5.1          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.33.0 LTS](https://docs.portainer.io/release-notes#release-2.33.0-lts)   | August 20, 2025    | 27.5.1 28.3.2             | 1.31 1.32 1.33     | 5.5.1          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.32.0](https://docs.portainer.io/release-notes#release-2.32.0-sts)       | July 24, 2025      | 27.5.1 28.2.2             | 1.31 1.32 1.33     | 5.4.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.31.3](https://docs.portainer.io/release-notes#release-2.31.3-sts)       | July 3, 2025       | 27.5.1 28.1.1             | 1.31 1.32 1.33     | 5.4.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.27.9 LTS](https://docs.portainer.io/release-notes#release-2.27.9-lts)   | July 2, 2025       | 26.0.2 27.0.3             | 1.29 1.30 1.31     | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.31.2](https://docs.portainer.io/release-notes#release-2.27.7)           | June 26, 2025      | 27.5.1 28.1.1             | 1.31 1.32 1.33     | 5.4.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.27.8 LTS](https://docs.portainer.io/release-notes#release-2.27.7-1)     | June 25, 2025      | 26.0.2 27.0.3             | 1.29 1.30 1.31     | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.31.1](https://docs.portainer.io/release-notes#release-2.27.7)           | June 19, 2025      | 27.5.1 28.1.1             | 1.31 1.32 1.33     | 5.4.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.27.7 LTS](https://docs.portainer.io/release-notes#release-2.27.7-1)     | June 17, 2025      | 26.0.2 27.0.3             | 1.29 1.30 1.31     | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.31.0](https://docs.portainer.io/release-notes#release-2.31.0)           | June 12, 2025      | 27.5.1 28.1.1             | 1.31 1.32 1.33     | 5.4.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.30.1](https://docs.portainer.io/release-notes#release-2.30.1)           | May 20, 2025       | 27.5.1 28.1.1             | 1.30 1.31 1.32     | 5.4.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.30.0](https://docs.portainer.io/release-notes#release-2.30.0)           | May 15, 2025       | 27.5.1 28.1.1             | 1.30 1.31 1.32     | 5.4.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.27.6 LTS](https://docs.portainer.io/release-notes#release-2.27.6)       | May 9, 2025        | 26.0.2 27.0.3             | 1.29 1.30 1.31     | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.27.5. LTS](https://docs.portainer.io/release-notes#release-2.27.5)      | May 2, 2025        | 26.0.2 27.0.3             | 1.29 1.30 1.31     | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.29.2](https://docs.portainer.io/release-notes#release-2.29.2)           | April 24, 2025     | 27.0.3 28.0.0             | 1.30 1.31 1.32     | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.29.1](https://docs.portainer.io/release-notes#release-2.29.1)           | April 23, 2025     | 27.0.3 28.0.0             | 1.30 1.31 1.32     | 5.23           | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.29.0](https://docs.portainer.io/release-notes#release-2.29.0)           | April 16, 2025     | 27.0.3 28.0.0             | 1.30 1.31 1.32     | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.27.4 LTS](https://docs.portainer.io/release-notes#release-2.27.4)       | April 15, 2025     | 26.0.2 27.0.3             | 1.29 1.30 1.31     | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.28.1](https://docs.portainer.io/release-notes#release-2.28.1)           | March 20, 2025     | 26.0.2 27.0.3             | 1.29 1.30 1.31     | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.28.0](https://docs.portainer.io/release-notes#release-2.28.0)           | March 19. 2025     | 26.0.2 27.0.3             | 1.29 1.30 1.31     | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.27.2 LTS](https://docs.portainer.io/release-notes#release-2.27.2)       | March 19, 2025     | 26.0.2 27.0.3             | 1.29 1.30 1.31     | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.27.1 LTS](https://docs.portainer.io/release-notes#release-2.27.1)       | February 27, 2025  | 26.0.2 27.0.3             | 1.29 1.30 1.31     | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.27.0 LTS](https://docs.portainer.io/release-notes#release-2.27.0)       | February 20, 2025  | 26.0.2 27.0.3             | 1.29 1.30 1.31     | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.26.1](https://docs.portainer.io/release-notes#release-2.26.1)           | January 21, 2025   | 26.0.2 27.0.1             | 1.28 1.29 1.30     | 5.2.2          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.26.0](https://docs.portainer.io/release-notes#release-2.26.0)           | January 15, 2025   | 26.0.2 27.0.1             | 1.28 1.29 1.30     | 5.2.2          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.25.1](https://docs.portainer.io/release-notes#release-2.25.1)           | December 20, 2024  | 26.0.2 27.0.1             | 1.28 1.29 1.30     | 5.2.2          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.21.5](https://docs.portainer.io/release-notes#release-2.21.5)           | December 20, 2024  | 26.0.2 27.0.1             | 1.28 1.29 1.30     | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.25.0](https://docs.portainer.io/release-notes#release-2.25.0)           | December 16, 2024  | 26.0.2 27.0.1             | 1.28 1.29 1.30     | 5.2.2          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.24.1](https://docs.portainer.io/release-notes#release-2.24.1)           | December 3, 2024   | 26.0.2 27.0.1             | 1.28 1.29 1.30     | 5.2.2          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.24.0](https://docs.portainer.io/release-notes#release-2.24.0)           | November 20, 2024  | 26.0.2 27.0.1             | 1.28 1.29 1.30     | 5.2.2          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.21.4 LTS](https://docs.portainer.io/release-notes#release-2.21.4)       | October 25, 2024   | 26.0.2 27.0.1             | 1.28 1.29 1.30     | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.23.0](https://docs.portainer.io/release-notes#release-2.23.0)           | October 16, 2024   | 26.0.2 27.0.1             | 1.28 1.29 1.30     | 5.2.2          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.21.3 LTS](https://docs.portainer.io/release-notes#release-2.21.3)       | October 8, 2024    | 26.0.2 27.0.1             | 1.28 1.29 1.30     | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.22.0](https://docs.portainer.io/release-notes#release-2.22.0)           | October 3, 2024    | 26.0.2 27.0.1             | 1.28 1.29 1.30     | 5.2.2          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.21.2 LTS](https://docs.portainer.io/release-notes#release-2.21.2)       | September 24, 2024 | 26.0.2 27.0.1             | 1.28 1.29 1.30     | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.21.1 LTS](https://docs.portainer.io/release-notes#release-2.21.1)       | September 10, 2024 | 26.0.2 27.0.1             | 1.28 1.29 1.30     | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.21.0 LTS](https://docs.portainer.io/release-notes#release-2.21.0)       | August 27, 2024    | 26.0.2 27.0.1             | 1.28 1.29 1.30     | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.20.3](https://docs.portainer.io/release-notes#release-2.20.3)           | May 21, 2024       | 25.0.5                    | 1.24 1.26 1.27     | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.20.2](https://docs.portainer.io/release-notes#release-2.20.2)           | May 1, 2024        | 25.0.5                    | 1.24 1.26 1.27     | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.19.5](https://docs.portainer.io/release-notes#release-2.19.5)           | April 22, 2024     | 23.0.6 24.0.4             | 1.23 1.24 1.26     | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.20.1](https://docs.portainer.io/release-notes#release-2.20.1)           | April 5, 2024      | 23.0.6 24.0.6             | 1.24 1.26 1.27     | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.20.0](https://docs.portainer.io/release-notes#release-2.20.0)           | March 19, 2024     | 23.0.6 24.0.6             | 1.24 1.26 1.27     | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.19.4](https://docs.portainer.io/release-notes#release-2.19.4)           | December 6, 2023   | 23.0.6 24.0.4             | 1.23 1.24 1.26     | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.19.3](https://docs.portainer.io/release-notes#release-2.19.3)           | November 22, 2023  | 23.0.6 24.0.4             | 1.23 1.24 1.26     | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.19.2](https://docs.portainer.io/release-notes#release-2.19.2)           | November 13, 2023  | 23.0.6 24.0.4             | 1.23 1.24 1.26     | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.19.1](https://docs.portainer.io/release-notes#release-2.19.1)           | September 20, 2023 | 23.0.6 24.0.4             | 1.23 1.24 1.26     | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.19.0](https://docs.portainer.io/release-notes#release-2.19.0)           | August 31, 2023    | 23.0.6 24.0.4             | 1.23 1.24 1.26     | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.18.4](https://docs.portainer.io/release-notes#release-2.18.4)           | July 7, 2023       | 23.0.6 24.0.4             | 1.22 1.23 1.24     | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.18.3](https://docs.portainer.io/release-notes#release-2.18.3)           | May 22, 2023       | 20.10.9 20.10.13 20.10.17 | 1.22 1.23 1.24     | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| [Business 2.18.2](https://docs.portainer.io/release-notes#release-2.18.2)           | May 1, 2023        | 20.10.9 20.10.13 20.10.17 | 1.22 1.23 1.24     | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |

### Portainer Community Edition (CE)

| Portainer Version    | Release Date       | Docker Version            | Kubernetes Version       | Podman Version | Architectures                                                                                          |
| -------------------- | ------------------ | ------------------------- | ------------------------ | -------------- | ------------------------------------------------------------------------------------------------------ |
| Community 2.39.0 LTS | February 26, 2026  | 28.5.1 29.2.1             | 1.32 1.33 1.34           | 5.6.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.38.1 STS | February 13, 2026  | 28.5.1 29.2.1             | 1.32 1.33 1.34           | 5.6.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.38.0 STS | January 29, 2026   | 28.5.1 29.1.2             | 1.32 1.33 1.34           | 5.6.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.37.0 STS | December 11, 2025  | 28.5.1 29.1.1             | 1.32 1.33 1.34           | 5.6.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.33.5 LTS | November 27, 2025  | 28.5.1 29.0.0             | 1.32 1.33 1.34           | 5.6.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.36.0 STS | November 27, 2025  | 28.5.1 29.0.0             | 1.32 1.33 1.34           | 5.6.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.33.4 LTS | November 20, 2025  | 28.5.1 29.0.0             | 1.32 1.33 1.34           | 5.6.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.33.3 LTS | October 30, 2025   | 27.5.1 28.5.1             | 1.32 1.33 1.34           | 5.6.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.35.0 STS | October 16, 2025   | 27.5.1 28.4.0             | 1.31 1.32 1.33           | 5.6.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.33.2 LTS | September 25, 2025 | 27.5.1 28.4.0             | 1.31 1.32 1.33           | 5.6.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.34.0 STS | September 18, 2025 | 27.5.1 28.3.3             | 1.31 1.32 1.33           | 5.5.1          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.33.1 LTS | August 27, 2025    | 27.5.1 28.3.2             | 1.31 1.32 1.33           | 5.5.1          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.33.0 LTS | August 20, 2025    | 27.5.1 28.3.2             | 1.31 1.32 .133           | 5.5.1          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.32.0     | July 24, 2025      | 27.5.1 28.2.2             | 1.31 1.32 1.33           | 5.4.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.31.3     | July 3, 2025       | 27.5.1 28.1.1             | 1.31 1.32 1.33           | 5.4.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.27.9 LTS | July 2, 2025       | 26.0.2 27.0.3             | 1.29 1.30 1.31           | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.31.2     | June 26, 2025      | 27.5.1 28.1.1             | 1.31 1.32 1.33           | 5.4.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.27.8 LTS | June 25, 2025      | 26.0.2 27.0.3             | 1.29 1.30 1.31           | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.31.1     | June 19, 2025      | 27.5.1 28.1.1             | 1.31 1.32 1.33           | 5.4.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.27.7 LTS | June 17. 2025      | 26.0.2 27.0.3             | 1.29 1.30 1.31           | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.31.0     | June 12, 2025      | 27.5.1 28.1.1             | 1.31 1.32 1.33           | 5.4.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.30.1     | May 20, 2025       | 27.5.1 28.1.1             | 1.30 1.31 1.32           | 5.4.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.30.0     | May 15, 2025       | 27.5.1 28.1.1             | 1.30 1.31 1.32           | 5.4.0          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.27.6 LTS | May 9, 2025        | 26.0.2 27.0.3             | 1.29 1.30 1.31           | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.27.5 LTS | May 2, 2025        | 26.0.2 27.0.3             | 1.29 1.30 1.31           | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.29.2     | April 24, 2025     | 27.0.3 28.0.0             | 1.30 1.31 1.32           | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.29.1     | April 23, 2025     | 27.0.3 28.0.0             | 1.30 1.31 1.32           | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.29.0     | April 16, 2025     | 27.0.3 28.0.0             | 1.30 1.31 1.32           | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.27.4 LTS | April 15, 2025     | 26.0.2 27.0.3             | 1.29 1.30 1.31           | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.28.1     | March 20, 2025     | 26.0.2 27.0.3             | 1.29 1.30 1.31           | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.28.0     | March 19, 2025     | 26.0.2 27.0.3             | 1.29 1.30 1.31           | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.27.2 LTS | March 19, 2025     | 26.0.2 27.0.3             | 1.29 1.30 1.31           | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.27.1 LTS | February 27, 2025  | 26.0.2 27.0.3             | 1.29 1.30 1.31           | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.27.0 LTS | February 20, 2025  | 26.0.2 27.0.3             | 1.29 1.30 1.31           | 5.2.3          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.26.1     | January 21, 2025   | 26.0.2 27.0.1             | 1.28 1.29 1.30           | 5.2.2          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.26.0     | January 15, 2025   | 26.0.2 27.0.1             | 1.28 1.29 1.30           | 5.2.2          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.25.1     | December 20, 2024  | 26.0.2 27.0.1             | 1.28 1.29 1.30           | 5.2.2          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.21.5     | December 20, 2024  | 26.0.2 27.0.1             | 1.28 1.29 1.30           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.25.0     | December 16, 2024  | 26.0.2 27.0.1             | 1.28 1.29 1.30           | 5.2.2          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.24.1     | December 3, 2024   | 26.0.2 27.0.1             | 1.28 1.29 1.30           | 5.2.2          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.24.0     | November 15, 2024  | 26.0.2 27.0.1             | 1.28 1.29 1.30           | 5.2.2          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.21.4     | October 25, 2024   | 26.0.2 27.0.1             | 1.28 1.29 1.30           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.23.0     | October 16, 2024   | 26.0.2 27.0.1             | 1.28 1.29 1.30           | 5.2.2          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.21.3     | October 8, 2024    | 26.0.2 27.0.1             | 1.28 1.29 1.30           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.22.0     | October 3, 2024    | 26.0.2 27.0.1             | 1.28 1.29 1.30           | 5.2.2          | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.21.2     | September 24, 2024 | 26.0.2 27.0.1             | 1.28 1.29 1.30           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.21.1     | September 10, 2024 | 26.0.2 27.0.1             | 1.28 1.29 1.30           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.21.0     | August 27, 2024    | 26.0.2 27.0.1             | 1.28 1.29 1.30           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.20.3     | May 21, 2024       | 25.0.5                    | 1.24 1.26 1.27           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.20.2     | May 1, 2024        | 25.0.5                    | 1.24 1.26 1.27           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.19.5     | April 22, 2024     | 23.0.6 24.0.4             | 1.23 1.24 1.26           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.20.1     | April 5, 2024      | 23.0.6 24.0.6             | 1.24 1.26 1.27           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.20.0     | March 19, 2024     | 23.0.6 24.0.6             | 1.24 1.26 1.27           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.19.4     | December 6, 2023   | 23.0.6 24.0.4             | 1.23 1.24 1.26           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.19.3     | November 22, 2023  | 23.0.6 24.0.4             | 1.23 1.24 1.26           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.19.2     | November 13, 2023  | 23.0.6 24.0.4             | 1.23 1.24 1.26           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.19.1     | September 20, 2023 | 23.0.6 24.0.4             | 1.23 1.24 1.26           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.19.0     | August 31, 2023    | 23.0.6 24.0.4             | 1.23 1.24 1.26           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.18.4     | July 7, 2023       | 23.0.6 24.0.4             | 1.22 1.23 1.24           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.18.3     | May 22, 2023       | 20.10.9 20.10.13 20.10.17 | 1.22 1.23 1.24           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.18.2     | May 1, 2023        | 20.10.9 20.10.13 20.10.17 | 1.22 1.23 1.24           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.18.1     | April 18, 2023     | 20.10.9 20.10.13 20.10.17 | 1.22 1.23 1.24           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.17.1     | February 22, 2023  | 20.10.9 20.10.13 20.10.17 | 1.22 1.23 1.24           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.17.0     | February 7, 2023   | 20.10.9 20.10.13 20.10.17 | 1.22 1.23 1.24           | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.16.2     | November 21, 2022  | 20.10.9 20.10.13 20.10.17 | 1.21.7 1.22 1.23         | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.16.1     | November 9, 2022   | 20.10.9 20.10.13 20.10.17 | 1.21.7 1.22 1.23         | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.16.0     | October 31, 2022   | 20.10.9 20.10.13 20.10.17 | 1.21.7 1.22 1.23         | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.15.1     | September 16, 2022 | 20.10.9 20.10.12 20.10.13 | 1.21.7 1.22 1.23         | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.15.0     | September 6, 2022  | 20.10.9 20.10.12 20.10.13 | 1.21.7 1.22 1.23         | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.14.2     | July 26, 2022      | 20.10.9 20.10.12 20.10.13 | 1.21.7 1.22 1.23         | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.14.1     | July 12, 2022      | 20.10.9 20.10.12 20.10.13 | 1.21.7 1.22 1.23         | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.14.0     | June 28, 2022      | 20.10.9 20.10.12 20.10.13 | 1.21.7 1.22 1.23         | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.13.1     | May 12, 2022       | 20.10.9 20.10.12 20.10.13 | 1.21.7 1.22 1.23         | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.13.0     | May 9, 2022        | 20.10.9 20.10.12 20.10.13 | 1.21.7 1.22 1.23         | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.11.1     | February 8, 2022   | 20.10.8 20.10.11 20.10.12 | 1.20.13 1.21.7 1.22.4    | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.11.0     | December 9, 2021   | 20.10.6 20.10.8 20.10.11  | 1.19.11 1.20.7 1.21 1.22 | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.9.3      | November 22, 2021  | 20.10.5 20.10.6           | 1.19.11 1.20.7 1.21 1.22 | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.9.2      | October 26, 2021   | 20.10.5 20.10.6           | 1.19 1.20 1.21 1.22      | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.9.1      | October 11, 2021   | 20.10.5 20.10.6           | 1.19 1.20 1.21 1.22      | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.9.0      | September 23, 2021 | 20.10.5 20.10.6           | 1.19 1.20 1.21 1.22      | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.6.3      | August 27, 2021    | 20.10.5 20.10.6           | 1.19 1.20 1.21 1.22      | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.6.2      | August 2, 2021     | 20.10.5 20.10.6           | 1.19 1.20.2 1.21         | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.6.1      | July 12, 2021      | 20.10.5 20.10.6           | 1.19 1.20.2 1.21         | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.6.0      | June 25, 2021      | 20.10.5 20.10.6           | 1.19 1.20.2 1.21         | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.5.1      | May 18, 2021       | 20.10.5 20.10.6           | 1.19 1.20.2 1.21         | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.5.0      | May 18, 2021       | 20.10.5                   | 1.19 1.20.2 1.21         | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |
| Community 2.1.x      | February 2, 2021   | 20.10.2                   | 1.20.0                   | N/A            | [ARM64](https://portal.portainer.io/knowledge/which-arm-architectures-does-portainer-support), x86\_64 |

{% hint style="info" %}
If you find an issue with an unlisted configuration, before reporting a bug, update your environment to a valid configuration and try to replicate the issue.
{% endhint %}

## Persistent storage

The Portainer Server requires persistent storage in order to maintain the database and configuration information it needs to function. The installation process provides a basic storage configuration for your platform. By default, both Docker and Kubernetes provide local (to the node) storage only, and if cluster-wide persistent storage is desired we recommend implementing it at the infrastructure level.

Additionally, you will want to ensure that your persistent storage for Portainer's data volume is right-sized for your needs. If you intend to use Portainer's Git deployment functionality for example, you will need to be aware that as part of the deployment from Git, Portainer will clone the remote repository locally to the Portainer data volume, which in the case of larger or multiple Git repos may consume significant amounts of disk space.

For larger or performance-critical deployments, we suggest you look to provision persistent storage with the highest possible throughput and lowest available latency. SSD-level performance (\~3.5 MB/s, 30,000 IOPS or above, under 10ms write IO latency) is ideal. Be careful when using cloud provider storage both in terms of latency and "burstable" or noisy-neighbor performance characteristics.

If you would like more assistance with verifying your scaled deployment please [get in touch](https://www.portainer.io/contact-sales) with our team.

## Ports

In order to access the UI and API, and for the Portainer Server instance and the Portainer Agents to communicate, certain ports need to be accessible.

On the Portainer Server the following ports must be open:

* TCP port `9443` (or `30779` for Kubernetes with NodePort) for the UI and API
* TCP port `8000` (or `30776` for Kubernetes with NodePort) for the TCP tunnel server for Edge Agents. This port is optional and only required if using Edge Compute features with Edge Agents.

For the Portainer Agent:

* TCP port `9001` (or `30778` for Kubernetes with NodePort) must be accessible on the Agent from the Portainer Server instance.

The Portainer Edge Agent does not require any open ports.

{% hint style="info" %}
All ports can be changed during installation.
{% endhint %}

{% content-ref url="install" %}
[install](https://docs.portainer.io/start/install)
{% endcontent-ref %}

{% content-ref url="install-ce" %}
[install-ce](https://docs.portainer.io/start/install-ce)
{% endcontent-ref %}


# Install Portainer BE

{% hint style="info" %}
These installation instructions are for Portainer Business Edition (BE). For Portainer Community Edition (CE) refer to the [CE install documentation](https://docs.portainer.io/start/install-ce).
{% endhint %}

Portainer Business Edition is straightforward to install. There are two options: installing new or adding an environment to an existing installation.

For a detailed, step-by-step guide to setting up Portainer for production, have a look at our [Best Practice Install Guide](https://academy.portainer.io/install/) in the Portainer Academy.

{% hint style="info" %}
If you haven't already, please check that your environments meet [our requirements](https://docs.portainer.io/start/requirements-and-prerequisites) before proceeding.
{% endhint %}

{% content-ref url="install/server" %}
[server](https://docs.portainer.io/start/install/server)
{% endcontent-ref %}

{% content-ref url="agent" %}
[agent](https://docs.portainer.io/start/agent)
{% endcontent-ref %}


# Set up a new Portainer BE Server installation

{% hint style="info" %}
These installation instructions are for Portainer Business Edition (BE). For Portainer Community Edition (CE) refer to the [CE install documentation](https://docs.portainer.io/start/install-ce/server).
{% endhint %}

Select the environment for your new Portainer installation:

{% content-ref url="server/docker" %}
[docker](https://docs.portainer.io/start/install/server/docker)
{% endcontent-ref %}

{% content-ref url="server/swarm" %}
[swarm](https://docs.portainer.io/start/install/server/swarm)
{% endcontent-ref %}

{% content-ref url="server/podman" %}
[podman](https://docs.portainer.io/start/install/server/podman)
{% endcontent-ref %}

{% content-ref url="server/kubernetes" %}
[kubernetes](https://docs.portainer.io/start/install/server/kubernetes)
{% endcontent-ref %}


# Docker Standalone

{% hint style="info" %}
These installation instructions are for Portainer Business Edition (BE). For Portainer Community Edition (CE) refer to the [CE install documentation](https://docs.portainer.io/start/install-ce/server/docker).
{% endhint %}

Installation instructions can differ between platforms. Please choose your platform below:

{% content-ref url="docker/linux" %}
[linux](https://docs.portainer.io/start/install/server/docker/linux)
{% endcontent-ref %}

{% content-ref url="docker/wsl" %}
[wsl](https://docs.portainer.io/start/install/server/docker/wsl)
{% endcontent-ref %}

{% content-ref url="docker/wcs" %}
[wcs](https://docs.portainer.io/start/install/server/docker/wcs)
{% endcontent-ref %}


# Install Portainer BE with Docker on Linux

{% hint style="info" %}
These installation instructions are for Portainer Business Edition (BE). For Portainer Community Edition (CE) refer to the [CE install documentation](https://docs.portainer.io/start/install-ce/server/docker/linux).
{% endhint %}

## Introduction

Portainer consists of two elements, the *Portainer Server*, and the *Portainer Agent*. Both elements run as lightweight Docker containers on a Docker engine. This document will help you install the Portainer Server container on your Linux environment. To add a new Linux environment to an existing Portainer Server installation, please refer to the [Portainer Agent installation instructions](https://docs.portainer.io/admin/environments/add/docker/agent).

To get started, you will need:

* The latest version of Docker installed and working. We recommend following the [official installation instructions](https://docs.docker.com/engine/install/) for Docker - in particular, we advise *against* installing Docker via snap on Ubuntu distributions as you may run into compatibility issues.
* sudo access on the machine that will host your Portainer Server instance
* By default, Portainer Server will expose the UI over port `9443` and expose a TCP tunnel server over port `8000`. The latter is optional and is only required if you plan to use the Edge compute features with Edge agents.
* A license key for Portainer Business Edition.

The installation instructions also make the following assumptions about your environment:

* Your environment meets [our requirements](https://docs.portainer.io/start/requirements-and-prerequisites). While Portainer may work with other configurations, it may require configuration changes or have limited functionality.
* You are accessing Docker via Unix sockets. Alternatively, you can also connect via TCP.
* SELinux is disabled on the machine running Docker. If you require SELinux, you will need to pass the `--privileged` flag to Docker when deploying Portainer.
* Docker is running as root. Portainer with rootless Docker has some limitations, and requires additional configuration.

## Deployment

You can choose to deploy Portainer using `docker run` or via Docker Compose.

{% tabs %}
{% tab title="docker run" %}
To install using `docker run`, first create the volume that Portainer Server will use to store its database:

```bash
docker volume create portainer_data
```

Then, download and install the Portainer Server container:

<pre><code><strong>docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ee:sts
</strong></code></pre>

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-docker-standalone) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}

{% hint style="info" %}
If you require HTTP port `9000` open for legacy reasons, add the following to your `docker run` command:

`-p 9000:9000`
{% endhint %}

Portainer Server has now been installed. You can check to see whether the Portainer Server container has started by running `docker ps`:

```bash
root@server:~# docker ps
CONTAINER ID   IMAGE                        COMMAND        CREATED         STATUS         PORTS                                                                                                NAMES
7963585688a9   portainer/portainer-ee:sts   "/portainer"   8 seconds ago   Up 8 seconds   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp, 0.0.0.0:9443->9443/tcp, [::]:9443->9443/tcp, 9000/tcp   portainer
```

{% endtab %}

{% tab title="Docker Compose" %}
To install using Docker Compose, download the compose file using the following `curl` command:

```
curl -L https://downloads.portainer.io/ee-sts/portainer-compose.yaml -o portainer-compose.yaml
```

Alternatively, create a `portainer-compose.yaml` file with the following contents:

```
services:
  portainer:
    container_name: portainer
    image: portainer/portainer-ee:sts
    restart: always
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - portainer_data:/data
    ports:
      - 9443:9443
      - 8000:8000  # Remove if you do not intend to use Edge Agents

volumes:
  portainer_data:
    name: portainer_data

networks:
  default:
    name: portainer_network
```

Once you have created or downloaded the compose file, you can deploy it with the following command:

```
docker compose -f portainer-compose.yaml up -d
```

Docker Compose will create the necessary resources and deploy Portainer. You can check to see whether the Portainer Server container has started by running `docker ps`:

```
root@server:~# docker ps
CONTAINER ID   IMAGE                        COMMAND        CREATED         STATUS         PORTS                                                                                                NAMES
7963585688a9   portainer/portainer-ee:sts   "/portainer"   8 seconds ago   Up 8 seconds   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp, 0.0.0.0:9443->9443/tcp, [::]:9443->9443/tcp, 9000/tcp   portainer
```

{% endtab %}
{% endtabs %}

## Logging In

Now that the installation is complete, you can log into your Portainer Server instance by opening a web browser and going to:

```bash
https://localhost:9443
```

Replace `localhost` with the relevant IP address or FQDN if needed, and adjust the port if you changed it earlier.

You will be presented with the initial setup page for Portainer Server.

{% content-ref url="../setup" %}
[setup](https://docs.portainer.io/start/install/server/setup)
{% endcontent-ref %}


# Install Portainer BE with Docker on WSL / Docker Desktop

{% hint style="info" %}
These installation instructions are for Portainer Business Edition (BE). For Portainer Community Edition (CE) refer to the [CE install documentation](https://docs.portainer.io/start/install-ce/server/docker/wsl).
{% endhint %}

## Introduction

Portainer consists of two elements, the *Portainer Server*, and the *Portainer Agent*. Both elements run as lightweight Docker containers on a Docker engine. This document will help you install the Portainer Server container on your Windows environment with WSL and Docker Desktop. To add a new WSL / Docker Desktop environment to an existing Portainer Server installation, please refer to the [Portainer Agent installation instructions](https://docs.portainer.io/admin/environments/add/docker/agent).

To get started, you will need:

* The latest version of Docker Desktop installed and working.
* Administrator access on the machine that will host your Portainer Server instance.
* Windows Subsystem for Linux (WSL) installed and a Linux distribution selected. For a new installation we recommend WSL2.
* By default, Portainer Server will expose the UI over port `9443` and expose a TCP tunnel server over port `8000`. The latter is optional and is only required if you plan to use the Edge compute features with Edge agents.
* A license key for Portainer Business Edition.

The installation instructions also make the following assumptions about your environment:

* Your environment meets [our requirements](https://docs.portainer.io/start/requirements-and-prerequisites). While Portainer may work with other configurations, it may require configuration changes or have limited functionality.
* You are accessing Docker via Unix sockets. Alternatively, you can also connect via TCP.
* SELinux is disabled within the Linux distribution used by WSL. If you require SELinux, you will need to pass the `--privileged` flag to Docker when deploying Portainer.
* Docker is running as root. Portainer with rootless Docker has some limitations, and requires additional configuration.

## Deployment

First, create the volume that Portainer Server will use to store its database:

```bash
docker volume create portainer_data
```

Then, download and install the Portainer Server container:

```
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ee:lts
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-docker-standalone) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}

{% hint style="info" %}
If you require HTTP port `9000` open for legacy reasons, add the following to your `docker run` command:

`-p 9000:9000`
{% endhint %}

Portainer Server has now been installed. You can check to see whether the Portainer Server container has started by running `docker ps`:

```bash
root@server:~# docker ps
CONTAINER ID   IMAGE                                              COMMAND                  CREATED        STATUS        PORTS                                                                                  NAMES
f4ab79732007   portainer/portainer-ee:lts                         "/portainer"             2 weeks ago    Up 29 hours   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp, 0.0.0.0:9443->9000/tcp, :::9443->9443/tcp   portainer
```

## Logging In

Now that the installation is complete, you can log into your Portainer Server instance by opening a web browser and going to:

```bash
https://localhost:9443
```

Replace `localhost` with the relevant IP address or FQDN if needed, and adjust the port if you changed it earlier.

You will be presented with the initial setup page for Portainer Server.

{% content-ref url="../setup" %}
[setup](https://docs.portainer.io/start/install/server/setup)
{% endcontent-ref %}


# Install Portainer BE with Docker on Windows Container Service

{% hint style="info" %}
These installation instructions are for Portainer Business Edition (BE). For Portainer Community Edition (CE) refer to the [CE install documentation](https://docs.portainer.io/start/install-ce/server/docker/wcs).
{% endhint %}

## Introduction

Portainer consists of two elements, the *Portainer Server*, and the *Portainer Agent*. Both elements run as lightweight Docker containers on a Docker engine. This document will help you install the Portainer Server container on your Windows server with Windows Containers. To add a new WCS environment to an existing Portainer Server installation, please refer to the [Portainer Agent installation instructions](https://docs.portainer.io/admin/environments/add/docker/agent).

To get started, you will need:

* Administrator access on the machine that will host your Portainer Server instance
* By default, Portainer Server will expose the UI over port `9443` and expose a TCP tunnel server over port `8000`. The latter is optional and is only required if you plan to use the Edge compute features with Edge agents.
* A license key for Portainer Business Edition.

The installation instructions also make the following assumption about your environment:

* Your environment meets [our requirements](https://docs.portainer.io/start/requirements-and-prerequisites). While Portainer may work with other configurations, it may require configuration changes or have limited functionality.

## Preparation

To run Portainer Server in a Windows Server/Desktop Environment you need to create exceptions in the firewall. These can easily be added through PowerShell by running the following commands:

```
netsh advfirewall firewall add rule name="cluster_management" dir=in action=allow protocol=TCP localport=2377
netsh advfirewall firewall add rule name="node_communication_tcp" dir=in action=allow protocol=TCP localport=7946
netsh advfirewall firewall add rule name="node_communication_udp" dir=in action=allow protocol=UDP localport=7946
netsh advfirewall firewall add rule name="overlay_network" dir=in action=allow protocol=UDP localport=4789
netsh advfirewall firewall add rule name="swarm_dns_tcp" dir=in action=allow protocol=TCP localport=53
netsh advfirewall firewall add rule name="swarm_dns_udp" dir=in action=allow protocol=UDP localport=53
```

You will also need to install the Windows Container Host Service and install Docker. Microsoft have [provided](https://learn.microsoft.com/en-us/virtualization/windowscontainers/quick-start/set-up-environment?tabs=dockerce#windows-server-1) a PowerShell script to perform the necessary actions. You can download the script and run it with the following commands:

```
Invoke-WebRequest -UseBasicParsing "https://raw.githubusercontent.com/microsoft/Windows-Containers/Main/helpful_tools/Install-DockerCE/install-docker-ce.ps1" -o install-docker-ce.ps1
.\install-docker-ce.ps1
```

Once this is complete you will need to restart your Windows server. After the restart completes, you're ready to install Portainer itself.

## Deployment

First, create the volume that Portainer Server will use to store its database. Using PowerShell:

```
docker volume create portainer_data
```

Then, download and install the Portainer Server container:

```
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart always -v \\.\pipe\docker_engine:\\.\pipe\docker_engine -v portainer_data:C:\data portainer/portainer-ee:lts
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}

{% hint style="warning" %}
If you see an error message similar to:&#x20;

`"\\.\pipe\dockerDesktopEngine" includes invalid characters for a local volume name`

then you may not have Windows containers properly enabled. If you are using Docker Desktop, right click the icon in your tray and select **Switch to Windows Containers**.
{% endhint %}

{% hint style="info" %}
If you require HTTP port `9000` open for legacy reasons, add the following to your `docker run` command:

`-p 9000:9000`
{% endhint %}

## Logging In

Now that the installation is complete, you can log into your Portainer Server instance by opening a web browser and going to:

```bash
https://localhost:9443
```

Replace `localhost` with the relevant IP address or FQDN if needed, and adjust the port if you changed it earlier.

You will be presented with the initial setup page for Portainer Server.

{% content-ref url="../setup" %}
[setup](https://docs.portainer.io/start/install/server/setup)
{% endcontent-ref %}


# Docker Swarm

{% hint style="info" %}
These installation instructions are for Portainer Business Edition (BE). For Portainer Community Edition (CE) refer to the [CE install documentation](https://docs.portainer.io/start/install-ce/server/swarm).
{% endhint %}

Installation instructions can differ between platforms. Please choose your platform below:

{% content-ref url="swarm/linux" %}
[linux](https://docs.portainer.io/start/install/server/swarm/linux)
{% endcontent-ref %}

{% content-ref url="swarm/wsl" %}
[wsl](https://docs.portainer.io/start/install/server/swarm/wsl)
{% endcontent-ref %}

{% content-ref url="swarm/wcs" %}
[wcs](https://docs.portainer.io/start/install/server/swarm/wcs)
{% endcontent-ref %}


# Install Portainer BE with Docker Swarm on Linux

{% hint style="info" %}
These installation instructions are for Portainer Business Edition (BE). For Portainer Community Edition (CE) refer to the [CE install documentation](https://docs.portainer.io/start/install-ce/server/swarm/linux).
{% endhint %}

## Introduction <a href="#introduction" id="introduction"></a>

Portainer consists of two elements, the *Portainer Server* and the *Portainer Agent*. Both elements run as lightweight Docker containers on a Docker engine. This document will help you deploy the Portainer Server and Agent containers on your Linux environment. To add a new Linux Swarm environment to an existing Portainer Server installation, please refer to the [Portainer Agent installation instructions](https://docs.portainer.io/admin/environments/add/swarm/agent).

To get started, you will need:

* The latest version of Docker installed and working. We recommend following the [official installation instructions](https://docs.docker.com/engine/install/) for Docker - in particular, we advise *against* installing Docker via snap on Ubuntu distributions as you may run into compatibility issues.
* Swarm mode [enabled](https://docs.docker.com/engine/swarm/swarm-mode/) and working, including the overlay network for the swarm service communication
* `sudo` access on the manager node of your swarm cluster
* By default, Portainer will expose the UI over port `9443` and expose a TCP tunnel server over port `8000`. The latter is optional and is only required if you plan to use the Edge compute features with Edge agents.
* The manager and worker nodes must be able to communicate with each other over port `9001`.
* A license key for Portainer Business Edition.

The installation instructions also make the following assumptions about your environment:

* Your environment meets [our requirements](https://docs.portainer.io/start/requirements-and-prerequisites). While Portainer may work with other configurations, it may require configuration changes or have limited functionality.
* You are accessing Docker via Unix sockets. Connecting via TCP is not supported in Docker Swarm.
* SELinux is disabled on the machine running Docker.
* Docker is running as root. Portainer with rootless Docker has some limitations, and requires additional configuration.
* You are running a single manager node in your swarm. If you have more than one, please [read this knowledge base article](https://portal.portainer.io/knowledge/how-can-i-ensure-portainers-configuration-is-retained) before proceeding.
* If your nodes are using DNS records to communicate, that all records are resolvable across the cluster.

## Deployment <a href="#deployment" id="deployment"></a>

{% embed url="<https://www.youtube.com/watch?v=S2VuHKxrT3s>" %}

Portainer can be directly deployed as a service in your Docker cluster. Note that this method will automatically deploy a single instance of the Portainer Server, and deploy the Portainer Agent as a global service on every node in your cluster.

{% hint style="danger" %}
Only do this **once** for your environment, regardless of how many nodes are in the cluster. You **do not** need to add each node in your cluster as a separate environment in Portainer. Deploying the manifest to your swarm will include every node in the cluster automatically. Adding each node as a separate environment will also consume more of your licensed node count than you may expect.
{% endhint %}

First, retrieve the stack YML manifest:

```
curl -L https://downloads.portainer.io/ee-sts/portainer-agent-stack.yml -o portainer-agent-stack.yml
```

Then use the downloaded YML manifest to deploy your stack:

```
docker stack deploy -c portainer-agent-stack.yml portainer
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-docker-swarm) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}

Portainer Server and the Agents have now been installed. You can check to see whether the Portainer Server and Agent containers have started by running `docker ps`:

```
root@manager01:~# docker ps
CONTAINER ID   IMAGE                           COMMAND                  CREATED              STATUS              PORTS                NAMES
59ee466f6b15   portainer/agent:sts             "./agent"                About a minute ago   Up About a minute                        portainer_agent.xbb8k6r7j1tk9gozjku7e43wr.5sa6b3e8cl6hyu0snlt387sgv
2db7dd4bfba0   portainer/portainer-ee:sts      "/portainer -H tcp:/…"   About a minute ago   Up About a minute   8000/tcp, 9443/tcp   portainer_portainer.1.gpuvu3pqmt1m19zxfo44v7izx
```

## Logging In <a href="#logging-in" id="logging-in"></a>

Now that the installation is complete, you can log into your Portainer Server instance by opening a web browser and going to:

```
https://localhost:9443
```

Replace `localhost` with the relevant IP address or FQDN if needed, and adjust the port if you changed it earlier.

You will be presented with the initial setup page for Portainer Server.

{% content-ref url="../setup" %}
[setup](https://docs.portainer.io/start/install/server/setup)
{% endcontent-ref %}


# Install Portainer BE with Docker Swarm on WSL / Docker Desktop

{% hint style="info" %}
These installation instructions are for Portainer Business Edition (BE). For Portainer Community Edition (CE) refer to the [CE install documentation](https://docs.portainer.io/start/install-ce/server/swarm/wsl).
{% endhint %}

## Introduction

Portainer consists of two elements, the *Portainer Server*, and the *Portainer Agent*. Both elements run as lightweight Docker containers on a Docker engine. This document will help you install the Portainer Server container on your Windows environment with WSL and Docker Desktop. To add a new WSL / Docker Desktop Swarm environment to an existing Portainer Server installation, please refer to the [Portainer Agent installation instructions](https://docs.portainer.io/admin/environments/add/swarm/agent).

To get started, you will need:

* The latest version of Docker Desktop installed and working.
* Swarm mode [enabled](https://docs.docker.com/engine/swarm/swarm-mode/) and working, including the overlay network for the swarm service communication.
* Administrator access on the manager node of your Swarm cluster.
* Windows Subsystem for Linux (WSL) installed and a Linux distribution selected. For a new installation we recommend WSL2.
* By default, Portainer will expose the UI over port `9443` and expose a TCP tunnel server over port `8000`. The latter is optional and is only required if you plan to use the Edge compute features with Edge agents.
* The manager and worker nodes must be able to communicate with each other over port `9001`.
* A license key for Portainer Business Edition.

The installation instructions also make the following assumptions about your environment:

* Your environment meets [our requirements](https://docs.portainer.io/start/requirements-and-prerequisites). While Portainer may work with other configurations, it may require configuration changes or have limited functionality.
* You are accessing Docker via Unix sockets. Alternatively, you can also connect via TCP.
* SELinux is disabled within the Linux distribution used by WSL.
* Docker is running as root. Portainer with rootless Docker has some limitations, and requires additional configuration.
* You are running a single manager node in your swarm. If you have more than one, please [read this article](https://docs.portainer.io/faqs/installing/how-can-i-ensure-portainers-configuration-is-retained) before proceeding.
* If your nodes are using DNS records to communicate, that all records are resolvable across the cluster.

## Deployment

Portainer can be directly deployed as a service in your Docker Swarm cluster. Note that this method will automatically deploy a single instance of the Portainer Server, and deploy the Portainer Agent as a global service on every node in your cluster.

{% hint style="danger" %}
Only do this **once** for your environment, regardless of how many nodes are in the cluster. You **do not** need to add each node in your cluster as a separate environment in Portainer. Deploying the manifest to your swarm will include every node in the cluster automatically. Adding each node as a separate environment will also consume more of your licensed node count than you may expect.
{% endhint %}

To begin the installation, first retrieve the stack YML manifest:

```
curl -L https://downloads.portainer.io/ee-lts/portainer-agent-stack.yml -o portainer-agent-stack.yml
```

Then use the downloaded YML manifest to deploy your stack:

```bash
docker stack deploy -c portainer-agent-stack.yml portainer
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-docker-swarm) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}

## Logging In

Now that the installation is complete, you can log into your Portainer Server instance by opening a web browser and going to:

```bash
https://localhost:9443
```

Replace `localhost` with the relevant IP address or FQDN if needed, and adjust the port if you changed it earlier.

You will be presented with the initial setup page for Portainer Server.

{% content-ref url="../setup" %}
[setup](https://docs.portainer.io/start/install/server/setup)
{% endcontent-ref %}


# Install Portainer BE with Docker Swarm on Windows Container Service

{% hint style="info" %}
These installation instructions are for Portainer Business Edition (BE). For Portainer Community Edition (CE) refer to the [CE install documentation](https://docs.portainer.io/start/install-ce/server/swarm/wcs).
{% endhint %}

## Introduction

Portainer consists of two elements, the *Portainer Server*, and the *Portainer Agent*. Both elements run as lightweight Docker containers on a Docker engine. This document will help you install the Portainer Server container on your Windows server with Windows Containers. To add a new WCS environment to an existing Portainer Server installation, please refer to the [Portainer Agent installation instructions](https://docs.portainer.io/admin/environments/add/swarm/agent).

To get started, you will need:

* The latest version of Docker installed and working.
* Swarm mode [enabled](https://docs.docker.com/engine/swarm/swarm-mode/) and working, including the overlay network for the swarm service communication.
* Administrator access on the manager node of your Swarm cluster.
* By default, Portainer will expose the UI over port `9443` and expose a TCP tunnel server over port `8000`. The latter is optional and is only required if you plan to use the Edge compute features with Edge agents.
* The manager and worker nodes must be able to communicate with each other over port `9001`.
* A license key for Portainer Business Edition.

The installation instructions also make the following assumptions about your environment:

* Your environment meets [our requirements](https://docs.portainer.io/start/requirements-and-prerequisites). While Portainer may work with other configurations, it may require configuration changes or have limited functionality.
* You are running a single manager node in your swarm. If you have more than one, please [read this article](https://docs.portainer.io/faqs/installing/how-can-i-ensure-portainers-configuration-is-retained) before proceeding.
* If your nodes are using DNS records to communicate, that all records are resolvable across the cluster.

## Preparation

To run Portainer Server in a Windows Server/Desktop Environment you need to create exceptions in the firewall. These can easily be added through PowerShell by running the following commands:

```
netsh advfirewall firewall add rule name="cluster_management" dir=in action=allow protocol=TCP localport=2377
netsh advfirewall firewall add rule name="node_communication_tcp" dir=in action=allow protocol=TCP localport=7946
netsh advfirewall firewall add rule name="node_communication_udp" dir=in action=allow protocol=UDP localport=7946
netsh advfirewall firewall add rule name="overlay_network" dir=in action=allow protocol=UDP localport=4789
netsh advfirewall firewall add rule name="swarm_dns_tcp" dir=in action=allow protocol=TCP localport=53
netsh advfirewall firewall add rule name="swarm_dns_udp" dir=in action=allow protocol=UDP localport=53
```

You will also need to install the Windows Container Host Service and install Docker. Microsoft have [provided](https://learn.microsoft.com/en-us/virtualization/windowscontainers/quick-start/set-up-environment?tabs=dockerce#windows-server-1) a PowerShell script to perform the necessary actions. You can download the script and run it with the following commands:

```
Invoke-WebRequest -UseBasicParsing "https://raw.githubusercontent.com/microsoft/Windows-Containers/Main/helpful_tools/Install-DockerCE/install-docker-ce.ps1" -o install-docker-ce.ps1
.\install-docker-ce.ps1
```

Once this is complete you will need to restart your Windows server. After the restart completes, you're ready to install Portainer itself.

## Deployment

Portainer can be directly deployed as a service in your Docker cluster. Note that this method will automatically deploy a single instance of the Portainer Server, and deploy the Portainer Agent as a global service on every node in your cluster.

{% hint style="danger" %}
Only do this **once** for your environment, regardless of how many nodes are in the cluster. You **do not** need to add each node in your cluster as a separate environment in Portainer. Deploying the manifest to your swarm will include every node in the cluster automatically. Adding each node as a separate environment will also consume more of your licensed node count than you may expect.
{% endhint %}

You can use our YML manifest to run Portainer in Windows using Windows Containers. In PowerShell, run:

```
curl https://downloads.portainer.io/ee-lts/portainer_windows_stack.yml -o portainer-windows-stack.yml
```

Then use the downloaded YML manifest to deploy your stack:

```bash
docker stack deploy --compose-file=portainer-windows-stack.yml portainer
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-docker-swarm) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}

## Logging In

Now that the installation is complete, you can log into your Portainer Server instance by opening a web browser and going to:

```bash
https://localhost:9443
```

Replace `localhost` with the relevant IP address or FQDN if needed, and adjust the port if you changed it earlier.

You will be presented with the initial setup page for Portainer Server.

{% content-ref url="../setup" %}
[setup](https://docs.portainer.io/start/install/server/setup)
{% endcontent-ref %}


# Podman

{% hint style="info" %}
These installation instructions are for Portainer Business Edition (BE). For Portainer Community Edition (CE) refer to the [CE install documentation](https://docs.portainer.io/start/install-ce/server/podman).
{% endhint %}

Installation instructions can differ between platforms. Please choose your platform below:

{% content-ref url="podman/linux" %}
[linux](https://docs.portainer.io/start/install/server/podman/linux)
{% endcontent-ref %}


# Install Portainer BE with Podman on Linux

{% hint style="info" %}
These installation instructions are for Portainer Business Edition (BE). For Portainer Community Edition (CE) refer to the [CE install documentation](https://docs.portainer.io/start/install-ce/server/podman/linux).
{% endhint %}

## Introduction

Portainer consists of two elements, the *Portainer Server*, and the *Portainer Agent*. Both elements run as lightweight containers on a Podman engine. This document will help you install the Portainer Server container on your Linux environment. To add a new Linux environment to an existing Portainer Server installation, please refer to the [Portainer Agent installation instructions](https://docs.portainer.io/admin/environments/add/podman/agent).

To get started, you will need:

* CentOS 9 with the latest version of Podman 5.x installed and working on your Podman host. Other Podman versions and Linux distros may work but we currently only support the above. We recommend following the [official installation instructions](https://podman.io/docs/installation#installing-on-linux) for Podman.
* Sudo access on the machine that will host your Portainer Server instance
* By default, Portainer Server will expose the UI over port `9443` and expose a TCP tunnel server over port `8000`. The latter is optional and is only required if you plan to use the Edge compute features with Edge agents.
* A license key for Portainer Business Edition.

The installation instructions also make the following assumptions about your environment:

* Your environment meets [our requirements](https://docs.portainer.io/start/requirements-and-prerequisites). While Portainer may work with other configurations, it may require configuration changes or have limited functionality.
* You are accessing Podman via Unix sockets.
* Podman is running as root. Portainer with rootless Podman may work but is currently not officially supported.

## Deployment

First, ensure the Podman socket is enabled:

```
systemctl enable --now podman.socket
```

Next, create the volume that Portainer Server will use to store its database:

```bash
podman volume create portainer_data
```

Then, download and install the Portainer Server container:

<pre><code><strong>podman run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always --privileged -v /run/podman/podman.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ee:lts
</strong></code></pre>

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-docker-standalone) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}

{% hint style="info" %}
If you require HTTP port `9000` open for legacy reasons, add the following to your `podman run` command:

`-p 9000:9000`
{% endhint %}

Portainer Server has now been installed. You can check to see whether the Portainer Server container has started by running `podman ps`:

```bash
root@server:~# podman ps
CONTAINER ID   IMAGE                          COMMAND                  CREATED       STATUS      PORTS                                                                                  NAMES             
de5b28eb2fa9   portainer/portainer-ee:lts     "/portainer"             2 weeks ago   Up 9 days   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp, 0.0.0.0:9443->9443/tcp, :::9443->9443/tcp   portainer
```

## Logging In

Now that the installation is complete, you can log into your Portainer Server instance by opening a web browser and going to:

```bash
https://localhost:9443
```

Replace `localhost` with the relevant IP address or FQDN if needed, and adjust the port if you changed it earlier.

You will be presented with the initial setup page for Portainer Server.

{% content-ref url="../setup" %}
[setup](https://docs.portainer.io/start/install/server/setup)
{% endcontent-ref %}


# Kubernetes

{% hint style="info" %}
These installation instructions are for Portainer Business Edition (BE). For Portainer Community Edition (CE) refer to the [CE install documentation](https://docs.portainer.io/start/install-ce/server/kubernetes).
{% endhint %}

Installation instructions can differ between platforms. Please choose your platform below:

{% content-ref url="kubernetes/baremetal" %}
[baremetal](https://docs.portainer.io/start/install/server/kubernetes/baremetal)
{% endcontent-ref %}

{% content-ref url="kubernetes/wsl" %}
[wsl](https://docs.portainer.io/start/install/server/kubernetes/wsl)
{% endcontent-ref %}


# Install Portainer BE on your Kubernetes environment

{% hint style="info" %}
These installation instructions are for Portainer Business Edition (BE). For Portainer Community Edition (CE) refer to the [CE install documentation](https://docs.portainer.io/start/install-ce/server/kubernetes/baremetal).
{% endhint %}

## Introduction

Portainer consists of two elements, the *Portainer Server* and the *Portainer Agent*. Both elements run as lightweight containers on Kubernetes.

To get started, you will need:

* A working and up to date Kubernetes cluster.
* Access to run `helm` or `kubectl` commands on your cluster.
* Cluster Admin rights on your Kubernetes cluster. This is so Portainer can create the necessary `ServiceAccount` and `ClusterRoleBinding` for it to access the Kubernetes cluster.
* A `default` StorageClass configured (see below).
* A license key for Portainer Business Edition.

The installation instructions also make the following assumptions about your environment:

* Your environment meets [our requirements](https://docs.portainer.io/start/requirements-and-prerequisites). While Portainer may work with other configurations, it may require configuration changes or have limited functionality.
* Kubernetes RBAC is enabled and working (this is required for the access control functionality in Portainer).
* You will be using the `portainer` namespace for Portainer. At present this is a requirement - other namespaces are currently unsupported.
* Kubernetes' metrics server is installed and working (if you wish to use the metrics within Portainer).

## Data Persistence

Portainer requires data persistence, and as a result needs at least one StorageClass available to use. Portainer will attempt to use the default StorageClass during deployment. If you do not have a StorageClass tagged as `default` the deployment will likely fail.

{% hint style="info" %}
We recommend using block storage for Kubernetes rather than network storage for the best performance and reliability, but do pay attention to the IOPS of your block storage devices when choosing the volume to use as some options are slower than others.
{% endhint %}

You can check if you have a default StorageClass by running the following command on your cluster:

```
kubectl get sc
```

and looking for a StorageClass with `(default)` after its name:

```
root@kubemaster01:~# kubectl get sc
NAME                            PROVISIONER                                   RECLAIMPOLICY   VOLUMEBINDINGMODE   ALLOWVOLUMEEXPANSION   AGE
managed-nfs-storage (default)   k8s-sigs.io/nfs-subdir-external-provisioner   Delete          Immediate           false                  11d
```

To set a StorageClass as default, you can use the following:

```
kubectl patch storageclass <storage-class-name> -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
```

replacing `<storage-class-name>` with the name of your StorageClass. Alternatively, if you are installing using our Helm chart, you can pass the following parameter in your helm install command to specify the StorageClass to use for Portainer:

```
--set persistence.storageClass=<storage-class-name>
```

{% hint style="info" %}
In some Kubernetes clusters (for example microk8s), the default StorageClass simply creates hostPath volumes, which are not explicitly tied to a particular node. In a multi-node cluster, this can create an issue when the pod is terminated and rescheduled on a different node, "leaving" all the persistent data behind and starting the pod with an "empty" volume.

While this behavior is inherently a limitation of using hostPath volumes, a suitable workaround is to use add a nodeSelector to the deployment, which effectively "pins" the Portainer pod to a particular node. You can do this by editing your own values.yaml file to set the nodeSelector value:

`nodeSelector: kubernetes.io/hostname: \<YOUR_NODE_NAME>`

or alternatively follow the instructions below for each deployment method.
{% endhint %}

## Deployment

To deploy Portainer within a Kubernetes cluster you can use our provided Helm charts or YAML manifests.

### Deploy using Helm

{% hint style="info" %}
Ensure you're using at least Helm v3.2, which includes support for the `--create-namespace` argument.
{% endhint %}

First add the Portainer Helm repository by running the following commands:

```
helm repo add portainer https://portainer.github.io/k8s/
helm repo update
```

Once the update completes, you're ready to begin the installation. Which method you choose will depend on how you wish to expose the Portainer service:

{% tabs %}
{% tab title="Expose via NodePort" %}
Using the following command, Portainer will be available on port `30779` for HTTPS:

```
helm upgrade --install --create-namespace -n portainer portainer portainer/portainer \
    --set enterpriseEdition.enabled=true \
    --set enterpriseEdition.image.tag=lts \
    --set tls.force=true
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `30779`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-kubernetes-via-helm) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}

{% hint style="info" %}
If you need to access Portainer via HTTP on port `30777`, remove the `--set tls.force=true` option.
{% endhint %}
{% endtab %}

{% tab title="Expose via Ingress" %}
In this example, Portainer will be deployed to your cluster and assigned a Cluster IP, with an nginx Ingress Controller at the defined hostname. For more on Ingress options, refer to the list of [Chart Configuration Options](https://docs.portainer.io/advanced/helm-chart-configuration-options).

```
helm upgrade --install --create-namespace -n portainer portainer portainer/portainer \
    --set enterpriseEdition.enabled=true \
    --set enterpriseEdition.image.tag=lts \
    --set service.type=ClusterIP \
    --set tls.force=true \
    --set ingress.enabled=true \
    --set ingress.ingressClassName=<ingressClassName (eg: nginx)> \
    --set ingress.annotations."nginx\.ingress\.kubernetes\.io/backend-protocol"=HTTPS \
    --set ingress.hosts[0].host=<fqdn (eg: portainer.example.io)> \
    --set ingress.hosts[0].paths[0].path="/"
```

{% hint style="info" %}
If you need to access Portainer via HTTP, remove the `--set tls.force=true` option.
{% endhint %}
{% endtab %}

{% tab title="Expose via Load Balancer" %}
Using the following command, Portainer will be available at an assigned Load Balancer IP on port `9443` for HTTPS:

```
helm upgrade --install --create-namespace -n portainer portainer portainer/portainer \
    --set service.type=LoadBalancer \
    --set enterpriseEdition.enabled=true \
    --set enterpriseEdition.image.tag=lts \
    --set tls.force=true
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-kubernetes-via-helm) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}

{% hint style="info" %}
If you need to access Portainer via HTTP on port `9000`, remove the `--set tls.force=true` option.
{% endhint %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
If you want to explicitly set the target node when deploying the Helm chart on the CLI, include `--set nodeSelector.kubernetes\.io/hostname=<YOUR NODE NAME>` in your `helm install` command.
{% endhint %}

### Deploy using YAML manifests

Our YAML manifests support exposing Portainer via either NodePort or Load Balancer.

{% tabs %}
{% tab title="Expose via NodePort" %}
To expose via NodePort, you can use the following command (Portainer will be available on port `30777`  for HTTP and `30779` for  HTTPS):

```
kubectl apply -n portainer -f https://downloads.portainer.io/ee-lts/portainer.yaml
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `30779`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-kubernetes-via-helm) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}
{% endtab %}

{% tab title="Expose via Load Balancer" %}
To expose via Load Balancer, use the following command to provision Portainer at an assigned Load Balancer IP on port `9000` for HTTP and `9443` for HTTPS:

```
kubectl apply -n portainer -f https://downloads.portainer.io/ee-lts/portainer-lb.yaml
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-kubernetes-via-helm) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
If you want to explicitly set the target node when deploying using YAML manifests, run the following one-liner to "patch" the deployment, forcing the pod to always be scheduled on the node it's currently running on:
{% endhint %}

```
kubectl patch deployments -n portainer portainer -p '{"spec": {"template": {"spec": {"nodeSelector": {"kubernetes.io/hostname": "'$(kubectl get pods -n portainer -o jsonpath='{ ..nodeName }')'"}}}}}' || (echo Failed to identify current node of portainer pod; exit 1)
```

## Logging In

Now that the installation is complete, you can log into your Portainer Server instance. Depending on how you chose to expose your Portainer installation, open a web browser and navigate to the following URL:

{% tabs %}
{% tab title="NodePort" %}

```bash
https://localhost:30779/ or http://localhost:30777/
```

Replace `localhost` with the relevant IP address or FQDN if needed, and adjust the port if you changed it earlier.
{% endtab %}

{% tab title="Ingress" %}

```bash
https://<FQDN>/
```

Replace `<FQDN>` with the FQDN of your Portainer instance.
{% endtab %}

{% tab title="Load Balancer" %}

```bash
https://<loadbalancer IP>:9443/ or http://<loadbalancer IP>:9000/
```

Replace `<loadbalancer IP>` with the IP address or FQDN of the load balancer, and adjust the port if you changed it earlier.
{% endtab %}
{% endtabs %}

You will be presented with the initial setup page for Portainer Server.

{% content-ref url="../setup" %}
[setup](https://docs.portainer.io/start/install/server/setup)
{% endcontent-ref %}


# Install Portainer BE with Kubernetes on WSL / Docker Desktop

{% hint style="info" %}
These installation instructions are for Portainer Business Edition (BE). For Portainer Community Edition (CE) refer to the [CE install documentation](https://docs.portainer.io/start/install-ce/server/kubernetes/wsl).
{% endhint %}

## Introduction

The following instructions will guide you in setting up *Portainer Server* with Kubernetes running on Docker Desktop with WSL.

{% hint style="info" %}
This scenario is for testing purposes only.
{% endhint %}

{% hint style="warning" %}
We are aware of an issue where namespace and application access privileges are not fully implemented when running Kubernetes via Docker Desktop. We are looking into the root cause and hope to have a resolution soon.
{% endhint %}

## Preparation

Before you start, you must make sure that Kubernetes is enabled and running within your Docker Desktop installation. To enable Kubernetes in Docker Desktop, you need to open the dashboard of Docker Desktop. Right click the Docker icon in the system tray and click **Dashboard**:

![](https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/2cj7YDrwIHF2wN0I7e07/kube-wsl-1.png)

Click **Settings**, then select **Kubernetes**, tick **Enable Kubernetes**, then click **Apply and Restart** (clicking **Install** in the dialog to install Kubernetes):

![](https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/yDznBTk5mlUQEtbooD3F/kube-wsl-2.gif)

After a few minutes, you will see that Kubernetes is running in the bottom left status bar of Docker Desktop:

![Docker is on the left, Kubernetes is on the right](https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/rnHRXDgudrM025bWte2z/kube-wsl-4.png)

## Deployment

To deploy Portainer within a Kubernetes cluster you can use our provided Helm charts or YAML manifests.

### Deploy using Helm

{% hint style="info" %}
Ensure you're using at least Helm v3.2, which includes support for the `--create-namespace` argument.
{% endhint %}

First add the Portainer Helm repository by running the following commands:

```
helm repo add portainer https://portainer.github.io/k8s/
helm repo update
```

Once the update completes, you're ready to begin the installation. Which method you choose will depend on how you wish to expose the Portainer service:

{% tabs %}
{% tab title="Expose via NodePort" %}
Using the following command, Portainer will be available on port `30777` for HTTP and `30779` for HTTPS:

```
helm upgrade --install --create-namespace -n portainer portainer portainer/portainer \
    --set enterpriseEdition.enabled=true \
    --set enterpriseEdition.image.tag=lts
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-kubernetes-via-helm) or [via the Portainer UI](https://app.gitbook.com/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}
{% endtab %}

{% tab title="Expose via Ingress" %}
In this example, Portainer will be deployed to your cluster and assigned a Cluster IP, with an nginx Ingress Controller at the defined hostname. For more on Ingress options, refer to the list of [Chart Configuration Options](https://docs.portainer.io/advanced/helm-chart-configuration-options).

```
helm upgrade --install --create-namespace -n portainer portainer portainer/portainer \
    --set enterpriseEdition.enabled=true \
    --set enterpriseEdition.image.tag=lts \
    --set service.type=ClusterIP \
    --set tls.force=true \
    --set ingress.enabled=true \
    --set ingress.ingressClassName=<ingressClassName (eg: nginx)> \
    --set ingress.annotations."nginx\.ingress\.kubernetes\.io/backend-protocol"=HTTPS \
    --set ingress.hosts[0].host=<fqdn (eg: portainer.example.io)> \
    --set ingress.hosts[0].paths[0].path="/"
```

{% endtab %}

{% tab title="Expose via Load Balancer" %}
Using the following command, Portainer will be available at an assigned Load Balancer IP on port `9000` for HTTP and `9443` for HTTPS:

```
helm upgrade --install --create-namespace -n portainer portainer portainer/portainer \
    --set service.type=LoadBalancer \
    --set enterpriseEdition.enabled=true \
    --set enterpriseEdition.image.tag=lts
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-kubernetes-via-helm) or [via the Portainer UI](https://app.gitbook.com/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
To explicitly set the target node when deploying the Helm chart on the CLI, include `--set nodeSelector.kubernetes.io/hostname=<YOUR NODE NAME>` in your `helm install` command.
{% endhint %}

### Deploy using YAML manifests

Our YAML manifests support exposing Portainer via either NodePort or Load Balancer.

{% tabs %}
{% tab title="Expose via NodePort" %}
To expose via NodePort, you can use the following command (Portainer will be available on port `30777`  for HTTP and `30779` for  HTTPS):

```
kubectl apply -n portainer -f https://downloads.portainer.io/ee-lts/portainer.yaml
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `30779`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-kubernetes-via-helm) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}
{% endtab %}

{% tab title="Expose via Load Balancer" %}
To expose via Load Balancer, use the following command to provision Portainer at an assigned Load Balancer IP on port `9000` for HTTP and `9443` for HTTPS:

```
kubectl apply -n portainer -f https://downloads.portainer.io/ee-lts/portainer-lb.yaml
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-kubernetes-via-helm) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
To explicitly set the target node when deploying using YAML manifests, run the following one-liner to "patch" the deployment, forcing the pod to always be scheduled on the node it's currently running on:
{% endhint %}

```
kubectl patch deployments -n portainer portainer -p '{"spec": {"template": {"spec": {"nodeSelector": {"kubernetes.io/hostname": "'$(kubectl get pods -n portainer -o jsonpath='{ ..nodeName }')'"}}}}}' || (echo Failed to identify current node of portainer pod; exit 1)
```

## Logging In

Now that the installation is complete, you can log into your Portainer Server instance. Depending on how you chose to expose your Portainer installation, open a web browser and navigate to the following URL:

{% tabs %}
{% tab title="NodePort" %}

```bash
https://localhost:30779/ or http://localhost:30777/
```

Replace `localhost` with the relevant IP address or FQDN if needed, and adjust the port if you changed it earlier.
{% endtab %}

{% tab title="Ingress" %}

```bash
https://<FQDN>/
```

Replace `<FQDN>` with the FQDN of your Portainer instance.
{% endtab %}

{% tab title="Load Balancer" %}

```bash
https://<loadbalancer IP>:9443/ or http://<loadbalancer IP>:9000/
```

Replace `<loadbalancer IP>` with the IP address or FQDN of the load balancer, and adjust the port if you changed it earlier.
{% endtab %}
{% endtabs %}

You will be presented with the initial setup page for Portainer Server.

{% content-ref url="../setup" %}
[setup](https://docs.portainer.io/start/install/server/setup)
{% endcontent-ref %}


# Initial setup

Once the Portainer Server has been deployed, and you have navigated to the instance's URL, you are ready for the initial setup.

## Creating the first user

Your first user will be an administrator. The username defaults to `admin` but you can change it if you prefer. The password must be at least 12 characters long and meet the listed password requirements.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/EHz2CveqyeJ5vIv4RGRB/2.32-initial-setup-username.png" alt=""><figcaption></figcaption></figure>

## Add your license key

You will now be asked to provide your license key. You will have been provided this when signing up for Business Edition or the free trial. If you don't have a license key, you can either click the **Don't have a license?** link or [get in touch with our team](mailto:success@portainer.io).

Paste the license key you were provided into the box and click **Submit**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/0t58yH4xxf576jMyQhkN/2.32-initial-setup-license.png" alt=""><figcaption></figcaption></figure>

## Connecting Portainer to your environments

Once the admin user has been created, the **Environment Wizard** will automatically launch. The wizard will help get you started with Portainer.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/U0Pp6FvY7vr2m4A6df9v/2.32-initial-setup-welcome.png" alt=""><figcaption></figcaption></figure>

The installation process automatically detects your local environment and sets it up for you. If you want to add additional environments to manage with this Portainer instance, click **Add Environments**. Otherwise, click **Get Started** to start using Portainer!


# Install Portainer CE

{% hint style="info" %}
These installation instructions are for Portainer Community Edition (CE). For Portainer Business Edition (BE) refer to the [BE install documentation](https://docs.portainer.io/start/install).
{% endhint %}

Portainer Community Edition is straightforward to install. There are two options: installing new or adding an environment to an existing installation.

{% hint style="info" %}
If you haven't already, please check that your environments meet [our requirements](https://docs.portainer.io/start/requirements-and-prerequisites) before proceeding.
{% endhint %}

{% content-ref url="install-ce/server" %}
[server](https://docs.portainer.io/start/install-ce/server)
{% endcontent-ref %}

{% content-ref url="agent" %}
[agent](https://docs.portainer.io/start/agent)
{% endcontent-ref %}


# Set up a new Portainer CE Server installation

{% hint style="info" %}
These installation instructions are for Portainer Community Edition (CE). For Portainer Business Edition (BE) refer to the [BE install documentation](https://docs.portainer.io/start/install/server).
{% endhint %}

Select the environment for your new Portainer installation:

{% content-ref url="server/docker" %}
[docker](https://docs.portainer.io/start/install-ce/server/docker)
{% endcontent-ref %}

{% content-ref url="server/swarm" %}
[swarm](https://docs.portainer.io/start/install-ce/server/swarm)
{% endcontent-ref %}

{% content-ref url="server/podman" %}
[podman](https://docs.portainer.io/start/install-ce/server/podman)
{% endcontent-ref %}

{% content-ref url="server/kubernetes" %}
[kubernetes](https://docs.portainer.io/start/install-ce/server/kubernetes)
{% endcontent-ref %}


# Docker Standalone

{% hint style="info" %}
These installation instructions are for Portainer Community Edition (CE). For Portainer Business Edition (BE) refer to the [BE install documentation](https://docs.portainer.io/start/install/server/docker).
{% endhint %}

Installation instructions can differ between platforms. Please choose your platform below:

{% content-ref url="docker/linux" %}
[linux](https://docs.portainer.io/start/install-ce/server/docker/linux)
{% endcontent-ref %}

{% content-ref url="docker/wsl" %}
[wsl](https://docs.portainer.io/start/install-ce/server/docker/wsl)
{% endcontent-ref %}

{% content-ref url="docker/wcs" %}
[wcs](https://docs.portainer.io/start/install-ce/server/docker/wcs)
{% endcontent-ref %}


# Install Portainer CE with Docker on Linux

{% hint style="info" %}
These installation instructions are for Portainer Community Edition (CE). For Portainer Business Edition (BE) refer to the [BE install documentation](https://docs.portainer.io/start/install/server/docker/linux).
{% endhint %}

## Introduction

Portainer consists of two elements, the *Portainer Server*, and the *Portainer Agent*. Both elements run as lightweight Docker containers on a Docker engine. This document will help you install the Portainer Server container on your Linux environment. To add a new Linux environment to an existing Portainer Server installation, please refer to the [Portainer Agent installation instructions](https://docs.portainer.io/admin/environments/add/docker/agent).

To get started, you will need:

* The latest version of Docker installed and working. We recommend following the [official installation instructions](https://docs.docker.com/engine/install/) for Docker - in particular, we advise *against* installing Docker via snap on Ubuntu distributions as you may run into compatibility issues.
* sudo access on the machine that will host your Portainer Server instance
* By default, Portainer Server will expose the UI over port `9443` and expose a TCP tunnel server over port `8000`. The latter is optional and is only required if you plan to use the Edge compute features with Edge agents.

The installation instructions also make the following assumptions about your environment:

* Your environment meets [our requirements](https://docs.portainer.io/start/requirements-and-prerequisites). While Portainer may work with other configurations, it may require configuration changes or have limited functionality.
* You are accessing Docker via Unix sockets. Alternatively, you can also connect via TCP.
* SELinux is disabled on the machine running Docker. If you require SELinux, you will need to pass the `--privileged` flag to Docker when deploying Portainer.
* Docker is running as root. Portainer with rootless Docker has some limitations, and requires additional configuration.

## Deployment

You can choose to deploy Portainer using `docker run` or via Docker Compose.

{% tabs %}
{% tab title="docker run" %}
To install using `docker run`, first create the volume that Portainer Server will use to store its database:

```bash
docker volume create portainer_data
```

Then, download and install the Portainer Server container:

```
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:sts
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-docker-standalone) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}

{% hint style="info" %}
If you require HTTP port `9000` open for legacy reasons, add the following to your `docker run` command:

`-p 9000:9000`
{% endhint %}

Portainer Server has now been installed. You can check to see whether the Portainer Server container has started by running `docker ps`:

```bash
root@server:~# docker ps
CONTAINER ID   IMAGE                        COMMAND        CREATED         STATUS         PORTS                                                                                                NAMES
7963585688a9   portainer/portainer-ce:sts   "/portainer"   8 seconds ago   Up 8 seconds   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp, 0.0.0.0:9443->9443/tcp, [::]:9443->9443/tcp, 9000/tcp   portainer
```

{% endtab %}

{% tab title="Docker Compose" %}
To install using Docker Compose, download the compose file using the following `curl` command:

```
curl -L https://downloads.portainer.io/ce-sts/portainer-compose.yaml -o portainer-compose.yaml
```

Alternatively, create a `portainer-compose.yaml` file with the following contents:

```
services:
  portainer:
    container_name: portainer
    image: portainer/portainer-ce:sts
    restart: always
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - portainer_data:/data
    ports:
      - 9443:9443
      - 8000:8000  # Remove if you do not intend to use Edge Agents

volumes:
  portainer_data:
    name: portainer_data

networks:
  default:
    name: portainer_network
```

Once you have created or downloaded the compose file, you can deploy it with the following command:

```
docker compose -f portainer-compose.yaml up -d
```

Docker Compose will create the necessary resources and deploy Portainer. You can check to see whether the Portainer Server container has started by running `docker ps`:

```
root@server:~# docker ps
CONTAINER ID   IMAGE                        COMMAND        CREATED         STATUS         PORTS                                                                                                NAMES
7963585688a9   portainer/portainer-ce:sts   "/portainer"   8 seconds ago   Up 8 seconds   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp, 0.0.0.0:9443->9443/tcp, [::]:9443->9443/tcp, 9000/tcp   portainer
```

{% endtab %}
{% endtabs %}

## Logging In

Now that the installation is complete, you can log into your Portainer Server instance by opening a web browser and going to:

```bash
https://localhost:9443
```

Replace `localhost` with the relevant IP address or FQDN if needed, and adjust the port if you changed it earlier.

You will be presented with the initial setup page for Portainer Server.

{% content-ref url="../setup" %}
[setup](https://docs.portainer.io/start/install-ce/server/setup)
{% endcontent-ref %}


# Install Portainer CE with Docker on WSL / Docker Desktop

{% hint style="info" %}
These installation instructions are for Portainer Community Edition (CE). For Portainer Business Edition (BE) refer to the [BE install documentation](https://docs.portainer.io/start/install/server/docker/wsl).
{% endhint %}

## Introduction

Portainer consists of two elements, the *Portainer Server*, and the *Portainer Agent*. Both elements run as lightweight Docker containers on a Docker engine. This document will help you install the Portainer Server container on your Windows environment with WSL and Docker Desktop. To add a new WSL / Docker Desktop environment to an existing Portainer Server installation, please refer to the [Portainer Agent installation instructions](https://docs.portainer.io/admin/environments/add/docker/agent).

To get started, you will need:

* The latest version of Docker Desktop installed and working.
* Administrator access on the machine that will host your Portainer Server instance.
* Windows Subsystem for Linux (WSL) installed and a Linux distribution selected. For a new installation we recommend WSL2.
* By default, Portainer Server will expose the UI over port `9443` and expose a TCP tunnel server over port `8000`. The latter is optional and is only required if you plan to use the Edge compute features with Edge agents.

The installation instructions also make the following assumptions about your environment:

* Your environment meets [our requirements](https://docs.portainer.io/start/requirements-and-prerequisites). While Portainer may work with other configurations, it may require configuration changes or have limited functionality.
* You are accessing Docker via Unix sockets. Alternatively, you can also connect via TCP.
* SELinux is disabled within the Linux distribution used by WSL. If you require SELinux, you will need to pass the `--privileged` flag to Docker when deploying Portainer.
* Docker is running as root. Portainer with rootless Docker has some limitations, and requires additional configuration.

## Deployment

First, create the volume that Portainer Server will use to store its database:

```bash
docker volume create portainer_data
```

Then, download and install the Portainer Server container:

```
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:lts
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-docker-standalone) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}

{% hint style="info" %}
If you require HTTP port `9000` open for legacy reasons, add the following to your `docker run` command:

`-p 9000:9000`
{% endhint %}

Portainer Server has now been installed. You can check to see whether the Portainer Server container has started by running `docker ps`:

```bash
root@server:~# docker ps
CONTAINER ID   IMAGE                                              COMMAND                  CREATED        STATUS        PORTS                                                                                  NAMES
f4ab79732007   portainer/portainer-ce:lts                         "/portainer"             2 weeks ago    Up 29 hours   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp, 0.0.0.0:9443->9000/tcp, :::9443->9443/tcp   portainer
```

## Logging In

Now that the installation is complete, you can log into your Portainer Server instance by opening a web browser and going to:

```bash
https://localhost:9443
```

Replace `localhost` with the relevant IP address or FQDN if needed, and adjust the port if you changed it earlier.

You will be presented with the initial setup page for Portainer Server.

{% content-ref url="../setup" %}
[setup](https://docs.portainer.io/start/install-ce/server/setup)
{% endcontent-ref %}


# Install Portainer CE with Docker on Windows Container Service

{% hint style="info" %}
These installation instructions are for Portainer Community Edition (CE). For Portainer Business Edition (BE) refer to the [BE install documentation](https://docs.portainer.io/start/install/server/docker/wcs).
{% endhint %}

## Introduction

Portainer consists of two elements, the *Portainer Server*, and the *Portainer Agent*. Both elements run as lightweight Docker containers on a Docker engine. This document will help you install the Portainer Server container on your Windows server with Windows Containers. To add a new WCS environment to an existing Portainer Server installation, please refer to the [Portainer Agent installation instructions](https://docs.portainer.io/admin/environments/add/docker/agent).

To get started, you will need:

* Administrator access on the machine that will host your Portainer Server instance
* By default, Portainer Server will expose the UI over port `9443` and expose a TCP tunnel server over port `8000`. The latter is optional and is only required if you plan to use the Edge compute features with Edge agents.

The installation instructions also make the following assumption about your environment:

* Your environment meets [our requirements](https://docs.portainer.io/start/requirements-and-prerequisites). While Portainer may work with other configurations, it may require configuration changes or have limited functionality.

## Preparation

To run Portainer Server in a Windows Server/Desktop Environment you need to create exceptions in the firewall. These can easily be added through PowerShell by running the following commands:

```
netsh advfirewall firewall add rule name="cluster_management" dir=in action=allow protocol=TCP localport=2377
netsh advfirewall firewall add rule name="node_communication_tcp" dir=in action=allow protocol=TCP localport=7946
netsh advfirewall firewall add rule name="node_communication_udp" dir=in action=allow protocol=UDP localport=7946
netsh advfirewall firewall add rule name="overlay_network" dir=in action=allow protocol=UDP localport=4789
netsh advfirewall firewall add rule name="swarm_dns_tcp" dir=in action=allow protocol=TCP localport=53
netsh advfirewall firewall add rule name="swarm_dns_udp" dir=in action=allow protocol=UDP localport=53
```

You will also need to install the Windows Container Host Service and install Docker. Microsoft have [provided](https://learn.microsoft.com/en-us/virtualization/windowscontainers/quick-start/set-up-environment?tabs=dockerce#windows-server-1) a PowerShell script to perform the necessary actions. You can download the script and run it with the following commands:

```
Invoke-WebRequest -UseBasicParsing "https://raw.githubusercontent.com/microsoft/Windows-Containers/Main/helpful_tools/Install-DockerCE/install-docker-ce.ps1" -o install-docker-ce.ps1
.\install-docker-ce.ps1
```

Once this is complete you will need to restart your Windows server. After the restart completes, you're ready to install Portainer itself.

## Deployment

First, create the volume that Portainer Server will use to store its database. Using PowerShell:

```
docker volume create portainer_data
```

Then, download and install the Portainer Server container:

```
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart always -v \\.\pipe\docker_engine:\\.\pipe\docker_engine -v portainer_data:C:\data portainer/portainer-ce:lts
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}

{% hint style="warning" %}
If you see an error message similar to:&#x20;

`"\\.\pipe\dockerDesktopEngine" includes invalid characters for a local volume name`

then you may not have Windows containers properly enabled. If you are using Docker Desktop, right click the icon in your tray and select **Switch to Windows Containers**.
{% endhint %}

{% hint style="info" %}
If you require HTTP port `9000` open for legacy reasons, add the following to your `docker run` command:

`-p 9000:9000`
{% endhint %}

## Logging In

Now that the installation is complete, you can log into your Portainer Server instance by opening a web browser and going to:

```bash
https://localhost:9443
```

Replace `localhost` with the relevant IP address or FQDN if needed, and adjust the port if you changed it earlier.

You will be presented with the initial setup page for Portainer Server.

{% content-ref url="../setup" %}
[setup](https://docs.portainer.io/start/install-ce/server/setup)
{% endcontent-ref %}


# Docker Swarm

{% hint style="info" %}
These installation instructions are for Portainer Community Edition (CE). For Portainer Business Edition (BE) refer to the [BE install documentation](https://docs.portainer.io/start/install/server/swarm).
{% endhint %}

Installation instructions can differ between platforms. Please choose your platform below:

{% content-ref url="swarm/linux" %}
[linux](https://docs.portainer.io/start/install-ce/server/swarm/linux)
{% endcontent-ref %}

{% content-ref url="swarm/wsl" %}
[wsl](https://docs.portainer.io/start/install-ce/server/swarm/wsl)
{% endcontent-ref %}

{% content-ref url="swarm/wcs" %}
[wcs](https://docs.portainer.io/start/install-ce/server/swarm/wcs)
{% endcontent-ref %}


# Install Portainer CE with Docker Swarm on Linux

{% hint style="info" %}
These installation instructions are for Portainer Community Edition (CE). For Portainer Business Edition (BE) refer to the [BE install documentation](https://docs.portainer.io/start/install/server/swarm/linux).
{% endhint %}

## Introduction <a href="#introduction" id="introduction"></a>

Portainer consists of two elements, the *Portainer Server* and the *Portainer Agent*. Both elements run as lightweight Docker containers on a Docker engine. This document will help you deploy the Portainer Server and Agent containers on your Linux environment. To add a new Linux Swarm environment to an existing Portainer Server installation, please refer to the [Portainer Agent installation instructions](https://docs.portainer.io/admin/environments/add/swarm/agent).

To get started, you will need:

* The latest version of Docker installed and working. We recommend following the [official installation instructions](https://docs.docker.com/engine/install/) for Docker - in particular, we advise *against* installing Docker via snap on Ubuntu distributions as you may run into compatibility issues.
* Swarm mode [enabled](https://docs.docker.com/engine/swarm/swarm-mode/) and working, including the overlay network for the swarm service communication
* `sudo` access on the manager node of your swarm cluster
* By default, Portainer will expose the UI over port `9443` and expose a TCP tunnel server over port `8000`. The latter is optional and is only required if you plan to use the Edge compute features with Edge agents.
* The manager and worker nodes must be able to communicate with each other over port `9001`.

The installation instructions also make the following assumptions about your environment:

* Your environment meets [our requirements](https://docs.portainer.io/start/requirements-and-prerequisites). While Portainer may work with other configurations, it may require configuration changes or have limited functionality.
* You are accessing Docker via Unix sockets. Connecting via TCP is not supported in Docker Swarm.
* SELinux is disabled on the machine running Docker.
* Docker is running as root. Portainer with rootless Docker has some limitations, and requires additional configuration.
* You are running a single manager node in your swarm. If you have more than one, please [read this article](https://docs.portainer.io/faqs/installing/how-can-i-ensure-portainers-configuration-is-retained) before proceeding.
* If your nodes are using DNS records to communicate, that all records are resolvable across the cluster.

## Deployment <a href="#deployment" id="deployment"></a>

{% embed url="<https://www.youtube.com/watch?v=S2VuHKxrT3s>" %}

Portainer can be directly deployed as a service in your Docker cluster. Note that this method will automatically deploy a single instance of the Portainer Server, and deploy the Portainer Agent as a global service on every node in your cluster.

{% hint style="danger" %}
Only do this **once** for your environment, regardless of how many nodes are in the cluster. You **do not** need to add each node in your cluster as a separate environment in Portainer. Deploying the manifest to your swarm will include every node in the cluster automatically. Adding each node as a separate environment will also consume more of your licensed node count than you may expect.
{% endhint %}

First, retrieve the stack YML manifest:

```
curl -L https://downloads.portainer.io/ce-lts/portainer-agent-stack.yml -o portainer-agent-stack.yml
```

Then use the downloaded YML manifest to deploy your stack:

```
docker stack deploy -c portainer-agent-stack.yml portainer
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-docker-swarm) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}

Portainer Server and the Agents have now been installed. You can check to see whether the Portainer Server and Agent containers have started by running `docker ps`:

```
root@manager01:~# docker ps
CONTAINER ID   IMAGE                           COMMAND                  CREATED              STATUS              PORTS                NAMES
59ee466f6b15   portainer/agent:lts             "./agent"                About a minute ago   Up About a minute                        portainer_agent.xbb8k6r7j1tk9gozjku7e43wr.5sa6b3e8cl6hyu0snlt387sgv
2db7dd4bfba0   portainer/portainer-ce:lts      "/portainer -H tcp:/…"   About a minute ago   Up About a minute   8000/tcp, 9443/tcp   portainer_portainer.1.gpuvu3pqmt1m19zxfo44v7izx
```

## Logging In <a href="#logging-in" id="logging-in"></a>

Now that the installation is complete, you can log into your Portainer Server instance by opening a web browser and going to:

```
https://localhost:9443
```

Replace `localhost` with the relevant IP address or FQDN if needed, and adjust the port if you changed it earlier.

You will be presented with the initial setup page for Portainer Server.

{% content-ref url="../setup" %}
[setup](https://docs.portainer.io/start/install-ce/server/setup)
{% endcontent-ref %}


# Install Portainer CE with Docker Swarm on WSL / Docker Desktop

{% hint style="info" %}
These installation instructions are for Portainer Community Edition (CE). For Portainer Business Edition (BE) refer to the [BE install documentation](https://docs.portainer.io/start/install/server/swarm/wsl).
{% endhint %}

## Introduction

Portainer consists of two elements, the *Portainer Server*, and the *Portainer Agent*. Both elements run as lightweight Docker containers on a Docker engine. This document will help you install the Portainer Server container on your Windows environment with WSL and Docker Desktop. To add a new WSL / Docker Desktop Swarm environment to an existing Portainer Server installation, please refer to the [Portainer Agent installation instructions](https://docs.portainer.io/admin/environments/add/swarm/agent).

To get started, you will need:

* The latest version of Docker Desktop installed and working.
* Swarm mode [enabled](https://docs.docker.com/engine/swarm/swarm-mode/) and working, including the overlay network for the swarm service communication.
* Administrator access on the manager node of your Swarm cluster.
* Windows Subsystem for Linux (WSL) installed and a Linux distribution selected. For a new installation we recommend WSL2.
* By default, Portainer will expose the UI over port `9443` and expose a TCP tunnel server over port `8000`. The latter is optional and is only required if you plan to use the Edge compute features with Edge agents.
* The manager and worker nodes must be able to communicate with each other over port `9001`.

The installation instructions also make the following assumptions about your environment:

* Your environment meets [our requirements](https://docs.portainer.io/start/requirements-and-prerequisites). While Portainer may work with other configurations, it may require configuration changes or have limited functionality.
* You are accessing Docker via Unix sockets. Alternatively, you can also connect via TCP.
* SELinux is disabled within the Linux distribution used by WSL.
* Docker is running as root. Portainer with rootless Docker has some limitations, and requires additional configuration.
* You are running a single manager node in your swarm. If you have more than one, please [read this article](https://docs.portainer.io/faqs/installing/how-can-i-ensure-portainers-configuration-is-retained) before proceeding.
* If your nodes are using DNS records to communicate, that all records are resolvable across the cluster.

## Deployment

Portainer can be directly deployed as a service in your Docker Swarm cluster. Note that this method will automatically deploy a single instance of the Portainer Server, and deploy the Portainer Agent as a global service on every node in your cluster.

{% hint style="danger" %}
Only do this **once** for your environment, regardless of how many nodes are in the cluster. You **do not** need to add each node in your cluster as a separate environment in Portainer. Deploying the manifest to your swarm will include every node in the cluster automatically. Adding each node as a separate environment will also consume more of your licensed node count than you may expect.
{% endhint %}

To begin the installation, first retrieve the stack YML manifest:

```
curl -L https://downloads.portainer.io/ce-lts/portainer-agent-stack.yml -o portainer-agent-stack.yml
```

Then use the downloaded YML manifest to deploy your stack:

```bash
docker stack deploy -c portainer-agent-stack.yml portainer
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-docker-swarm) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}

## Logging In

Now that the installation is complete, you can log into your Portainer Server instance by opening a web browser and going to:

```bash
https://localhost:9443
```

Replace `localhost` with the relevant IP address or FQDN if needed, and adjust the port if you changed it earlier.

You will be presented with the initial setup page for Portainer Server.

{% content-ref url="../setup" %}
[setup](https://docs.portainer.io/start/install-ce/server/setup)
{% endcontent-ref %}


# Install Portainer CE with Docker Swarm on Windows Container Service

{% hint style="info" %}
These installation instructions are for Portainer Community Edition (CE). For Portainer Business Edition (BE) refer to the [BE install documentation](https://docs.portainer.io/start/install/server/swarm/wcs).
{% endhint %}

## Introduction

Portainer consists of two elements, the *Portainer Server*, and the *Portainer Agent*. Both elements run as lightweight Docker containers on a Docker engine. This document will help you install the Portainer Server container on your Windows server with Windows Containers. To add a new WCS environment to an existing Portainer Server installation, please refer to the [Portainer Agent installation instructions](https://docs.portainer.io/admin/environments/add/swarm/agent).

To get started, you will need:

* The latest version of Docker installed and working.
* Swarm mode [enabled](https://docs.docker.com/engine/swarm/swarm-mode/) and working, including the overlay network for the swarm service communication.
* Administrator access on the manager node of your Swarm cluster.
* By default, Portainer will expose the UI over port `9443` and expose a TCP tunnel server over port `8000`. The latter is optional and is only required if you plan to use the Edge compute features with Edge agents.
* The manager and worker nodes must be able to communicate with each other over port `9001`.

The installation instructions also make the following assumptions about your environment:

* Your environment meets [our requirements](https://docs.portainer.io/start/requirements-and-prerequisites). While Portainer may work with other configurations, it may require configuration changes or have limited functionality.
* You are running a single manager node in your swarm. If you have more than one, please [read this article](https://docs.portainer.io/faqs/installing/how-can-i-ensure-portainers-configuration-is-retained) before proceeding.
* If your nodes are using DNS records to communicate, that all records are resolvable across the cluster.

## Preparation

To run Portainer Server in a Windows Server/Desktop Environment you need to create exceptions in the firewall. These can easily be added through PowerShell by running the following commands:

```
netsh advfirewall firewall add rule name="cluster_management" dir=in action=allow protocol=TCP localport=2377
netsh advfirewall firewall add rule name="node_communication_tcp" dir=in action=allow protocol=TCP localport=7946
netsh advfirewall firewall add rule name="node_communication_udp" dir=in action=allow protocol=UDP localport=7946
netsh advfirewall firewall add rule name="overlay_network" dir=in action=allow protocol=UDP localport=4789
netsh advfirewall firewall add rule name="swarm_dns_tcp" dir=in action=allow protocol=TCP localport=53
netsh advfirewall firewall add rule name="swarm_dns_udp" dir=in action=allow protocol=UDP localport=53
```

You will also need to install the Windows Container Host Service and install Docker. Microsoft have [provided](https://learn.microsoft.com/en-us/virtualization/windowscontainers/quick-start/set-up-environment?tabs=dockerce#windows-server-1) a PowerShell script to perform the necessary actions. You can download the script and run it with the following commands:

```
Invoke-WebRequest -UseBasicParsing "https://raw.githubusercontent.com/microsoft/Windows-Containers/Main/helpful_tools/Install-DockerCE/install-docker-ce.ps1" -o install-docker-ce.ps1
.\install-docker-ce.ps1
```

Once this is complete you will need to restart your Windows server. After the restart completes, you're ready to install Portainer itself.

## Deployment

Portainer can be directly deployed as a service in your Docker cluster. Note that this method will automatically deploy a single instance of the Portainer Server, and deploy the Portainer Agent as a global service on every node in your cluster.

{% hint style="danger" %}
Only do this **once** for your environment, regardless of how many nodes are in the cluster. You **do not** need to add each node in your cluster as a separate environment in Portainer. Deploying the manifest to your swarm will include every node in the cluster automatically. Adding each node as a separate environment will also consume more of your licensed node count than you may expect.
{% endhint %}

You can use our YML manifest to run Portainer in Windows using Windows Containers. In PowerShell, run:

```
curl https://downloads.portainer.io/ce-lts/portainer_windows_stack.yml -o portainer-windows-stack.yml
```

Then use the downloaded YML manifest to deploy your stack:

```bash
docker stack deploy --compose-file=portainer-windows-stack.yml portainer
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-docker-swarm) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}

## Logging In

Now that the installation is complete, you can log into your Portainer Server instance by opening a web browser and going to:

```bash
https://localhost:9443
```

Replace `localhost` with the relevant IP address or FQDN if needed, and adjust the port if you changed it earlier.

You will be presented with the initial setup page for Portainer Server.

{% content-ref url="../setup" %}
[setup](https://docs.portainer.io/start/install-ce/server/setup)
{% endcontent-ref %}


# Podman

{% hint style="info" %}
These installation instructions are for Portainer Community Edition (CE). For Portainer Business Edition (BE) refer to the [BE install documentation](https://docs.portainer.io/start/install/server/podman).
{% endhint %}

Installation instructions can differ between platforms. Please choose your platform below:

{% content-ref url="podman/linux" %}
[linux](https://docs.portainer.io/start/install-ce/server/podman/linux)
{% endcontent-ref %}


# Install Portainer CE with Podman on Linux

{% hint style="info" %}
These installation instructions are for Portainer Community Edition (CE). For Portainer Business Edition (BE) refer to the [BE install documentation](https://docs.portainer.io/start/install/server/podman/linux).
{% endhint %}

## Introduction

Portainer consists of two elements, the *Portainer Server*, and the *Portainer Agent*. Both elements run as lightweight containers on a Podman engine. This document will help you install the Portainer Server container on your Linux environment. To add a new Linux environment to an existing Portainer Server installation, please refer to the [Portainer Agent installation instructions](https://docs.portainer.io/admin/environments/add/podman/agent).

To get started, you will need:

* CentOS 9 with the latest version of Podman 5.x installed and working on your Podman host. Other Podman versions and Linux distros may work but we currently only support the above. We recommend following the [official installation instructions](https://podman.io/docs/installation#installing-on-linux) for Podman.
* sudo access on the machine that will host your Portainer Server instance
* By default, Portainer Server will expose the UI over port `9443` and expose a TCP tunnel server over port `8000`. The latter is optional and is only required if you plan to use the Edge compute features with Edge agents.

The installation instructions also make the following assumptions about your environment:

* Your environment meets [our requirements](https://docs.portainer.io/start/requirements-and-prerequisites). While Portainer may work with other configurations, it may require configuration changes or have limited functionality.
* You are accessing Podman via Unix sockets.
* Podman is running as root. Portainer with rootless Podman may work but is currently not officially supported.

## Deployment

First, ensure the Podman socket is enabled:

```
systemctl enable --now podman.socket
```

Next, create the volume that Portainer Server will use to store its database:

```bash
podman volume create portainer_data
```

Then, download and install the Portainer Server container:

<pre><code><strong>podman run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always --privileged -v /run/podman/podman.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:lts
</strong></code></pre>

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-docker-standalone) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}

{% hint style="info" %}
If you require HTTP port `9000` open for legacy reasons, add the following to your `podman run` command:

`-p 9000:9000`
{% endhint %}

Portainer Server has now been installed. You can check to see whether the Portainer Server container has started by running `podman ps`:

```bash
root@server:~# podman ps
CONTAINER ID   IMAGE                          COMMAND                  CREATED       STATUS      PORTS                                                                                  NAMES             
de5b28eb2fa9   portainer/portainer-ce:lts     "/portainer"             2 weeks ago   Up 9 days   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp, 0.0.0.0:9443->9443/tcp, :::9443->9443/tcp   portainer
```

## Logging In

Now that the installation is complete, you can log into your Portainer Server instance by opening a web browser and going to:

```bash
https://localhost:9443
```

Replace `localhost` with the relevant IP address or FQDN if needed, and adjust the port if you changed it earlier.

You will be presented with the initial setup page for Portainer Server.

{% content-ref url="../setup" %}
[setup](https://docs.portainer.io/start/install-ce/server/setup)
{% endcontent-ref %}


# Kubernetes

{% hint style="info" %}
These installation instructions are for Portainer Community Edition (CE). For Portainer Business Edition (BE) refer to the [BE install documentation](https://docs.portainer.io/start/install/server/kubernetes).
{% endhint %}

Installation instructions can differ between platforms. Please choose your platform below:

{% content-ref url="kubernetes/baremetal" %}
[baremetal](https://docs.portainer.io/start/install-ce/server/kubernetes/baremetal)
{% endcontent-ref %}

{% content-ref url="kubernetes/wsl" %}
[wsl](https://docs.portainer.io/start/install-ce/server/kubernetes/wsl)
{% endcontent-ref %}


# Install Portainer CE on your Kubernetes environment

{% hint style="info" %}
These installation instructions are for Portainer Community Edition (CE). For Portainer Business Edition (BE) refer to the [BE install documentation](https://docs.portainer.io/start/install/server/kubernetes/baremetal).
{% endhint %}

## Introduction

Portainer consists of two elements, the *Portainer Server* and the *Portainer Agent*. Both elements run as lightweight containers on Kubernetes.

To get started, you will need:

* A working and up to date Kubernetes cluster.
* Access to run `helm` or `kubectl` commands on your cluster.
* Cluster Admin rights on your Kubernetes cluster. This is so Portainer can create the necessary `ServiceAccount` and `ClusterRoleBinding` for it to access the Kubernetes cluster.
* A `default` StorageClass configured (see below).

The installation instructions also make the following assumptions about your environment:

* Your environment meets [our requirements](https://docs.portainer.io/start/requirements-and-prerequisites). While Portainer may work with other configurations, it may require configuration changes or have limited functionality.
* Kubernetes RBAC is enabled and working (this is required for the access control functionality in Portainer).
* You will be using the `portainer` namespace for Portainer. At present this is a requirement - other namespaces are currently unsupported.
* Kubernetes' metrics server is installed and working (if you wish to use the metrics within Portainer).

## Data Persistence

Portainer requires data persistence, and as a result needs at least one StorageClass available to use. Portainer will attempt to use the default StorageClass during deployment. If you do not have a StorageClass tagged as `default` the deployment will likely fail.

{% hint style="info" %}
We recommend using block storage for Kubernetes rather than network storage for the best performance and reliability, but do pay attention to the IOPS of your block storage devices when choosing the volume to use as some options are slower than others.
{% endhint %}

You can check if you have a default StorageClass by running the following command on your cluster:

```
kubectl get sc
```

and looking for a StorageClass with `(default)` after its name:

```
root@kubemaster01:~# kubectl get sc
NAME                            PROVISIONER                                   RECLAIMPOLICY   VOLUMEBINDINGMODE   ALLOWVOLUMEEXPANSION   AGE
managed-nfs-storage (default)   k8s-sigs.io/nfs-subdir-external-provisioner   Delete          Immediate           false                  11d
```

To set a StorageClass as default, you can use the following:

```
kubectl patch storageclass <storage-class-name> -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
```

replacing `<storage-class-name>` with the name of your StorageClass. Alternatively, if you are installing using our Helm chart, you can pass the following parameter in your helm install command to specify the StorageClass to use for Portainer:

```
--set persistence.storageClass=<storage-class-name>
```

{% hint style="info" %}
In some Kubernetes clusters (for example microk8s), the default StorageClass simply creates hostPath volumes, which are not explicitly tied to a particular node. In a multi-node cluster, this can create an issue when the pod is terminated and rescheduled on a different node, "leaving" all the persistent data behind and starting the pod with an "empty" volume.

While this behavior is inherently a limitation of using hostPath volumes, a suitable workaround is to use add a nodeSelector to the deployment, which effectively "pins" the Portainer pod to a particular node. You can do this by editing your own values.yaml file to set the nodeSelector value:

`nodeSelector: kubernetes.io/hostname: \<YOUR_NODE_NAME>`

or alternatively follow the instructions below for each deployment method.
{% endhint %}

## Deployment

To deploy Portainer within a Kubernetes cluster you can use our provided Helm charts or YAML manifests.

### Deploy using Helm

{% hint style="info" %}
Ensure you're using at least Helm v3.2, which includes support for the `--create-namespace` argument.
{% endhint %}

First add the Portainer Helm repository by running the following commands:

```
helm repo add portainer https://portainer.github.io/k8s/
helm repo update
```

Once the update completes, you're ready to begin the installation. Which method you choose will depend on how you wish to expose the Portainer service:

{% tabs %}
{% tab title="Expose via NodePort" %}
Using the following command, Portainer will be available on port `30779` for HTTPS:

```
helm upgrade --install --create-namespace -n portainer portainer portainer/portainer \
    --set tls.force=true \
    --set image.tag=lts
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `30779`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-kubernetes-via-helm) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}

{% hint style="info" %}
If you need to access Portainer via HTTP on port `30777`, remove the `--set tls.force=true` option.
{% endhint %}
{% endtab %}

{% tab title="Expose via Ingress" %}
In this example, Portainer will be deployed to your cluster and assigned a Cluster IP, with an nginx Ingress Controller at the defined hostname. For more on Ingress options, refer to the list of [Chart Configuration Options](https://docs.portainer.io/advanced/helm-chart-configuration-options).

```
helm upgrade --install --create-namespace -n portainer portainer portainer/portainer \
    --set service.type=ClusterIP \
    --set tls.force=true \
    --set image.tag=lts \
    --set ingress.enabled=true \
    --set ingress.ingressClassName=<ingressClassName (eg: nginx)> \
    --set ingress.annotations."nginx\.ingress\.kubernetes\.io/backend-protocol"=HTTPS \
    --set ingress.hosts[0].host=<fqdn (eg: portainer.example.io)> \
    --set ingress.hosts[0].paths[0].path="/"
```

{% hint style="info" %}
If you need to access Portainer via HTTP, remove the `--set tls.force=true` option.
{% endhint %}
{% endtab %}

{% tab title="Expose via Load Balancer" %}
Using the following command, Portainer will be available at an assigned Load Balancer IP on port `9443` for HTTPS:

```
helm upgrade --install --create-namespace -n portainer portainer portainer/portainer \
    --set service.type=LoadBalancer \
    --set tls.force=true \
    --set image.tag=lts
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-kubernetes-via-helm) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}

{% hint style="info" %}
If you need to access Portainer via HTTP on port `9000`, remove the `--set tls.force=true` option.
{% endhint %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
If you want to explicitly set the target node when deploying the Helm chart on the CLI, include `--set nodeSelector.kubernetes\.io/hostname=<YOUR NODE NAME>` in your `helm install` command.
{% endhint %}

### Deploy using YAML manifests

Our YAML manifests support exposing Portainer via either NodePort or Load Balancer.

{% tabs %}
{% tab title="Expose via NodePort" %}
To expose via NodePort, you can use the following command (Portainer will be available on port `30777`  for HTTP and `30779` for  HTTPS):

```
kubectl apply -n portainer -f https://downloads.portainer.io/ce-lts/portainer.yaml
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `30779`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-kubernetes-via-helm) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}
{% endtab %}

{% tab title="Expose via Load Balancer" %}
To expose via Load Balancer, use the following command to provision Portainer at an assigned Load Balancer IP on port `9000` for HTTP and `9443` for HTTPS:

```
kubectl apply -n portainer -f https://downloads.portainer.io/ce-lts/portainer-lb.yaml
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-kubernetes-via-helm) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
If you want to explicitly set the target node when deploying using YAML manifests, run the following one-liner to "patch" the deployment, forcing the pod to always be scheduled on the node it's currently running on:
{% endhint %}

```
kubectl patch deployments -n portainer portainer -p '{"spec": {"template": {"spec": {"nodeSelector": {"kubernetes.io/hostname": "'$(kubectl get pods -n portainer -o jsonpath='{ ..nodeName }')'"}}}}}' || (echo Failed to identify current node of portainer pod; exit 1)
```

## Logging In

Now that the installation is complete, you can log into your Portainer Server instance. Depending on how you chose to expose your Portainer installation, open a web browser and navigate to the following URL:

{% tabs %}
{% tab title="NodePort" %}

```bash
https://localhost:30779/ or http://localhost:30777/
```

Replace `localhost` with the relevant IP address or FQDN if needed, and adjust the port if you changed it earlier.
{% endtab %}

{% tab title="Ingress" %}

```bash
https://<FQDN>/
```

Replace `<FQDN>` with the FQDN of your Portainer instance.
{% endtab %}

{% tab title="Load Balancer" %}

```bash
https://<loadbalancer IP>:9443/ or http://<loadbalancer IP>:9000/
```

Replace `<loadbalancer IP>` with the IP address or FQDN of the load balancer, and adjust the port if you changed it earlier.
{% endtab %}
{% endtabs %}

You will be presented with the initial setup page for Portainer Server.

{% content-ref url="../setup" %}
[setup](https://docs.portainer.io/start/install-ce/server/setup)
{% endcontent-ref %}


# Install Portainer CE with Kubernetes on WSL / Docker Desktop

{% hint style="info" %}
These installation instructions are for Portainer Community Edition (CE). For Portainer Business Edition (BE) refer to the [BE install documentation](https://docs.portainer.io/start/install/server/kubernetes/wsl).
{% endhint %}

## Introduction

The following instructions will guide you in setting up *Portainer Server* with Kubernetes running on Docker Desktop with WSL.

{% hint style="info" %}
This scenario is for testing purposes only.
{% endhint %}

{% hint style="warning" %}
We are aware of an issue where namespace and application access privileges are not fully implemented when running Kubernetes via Docker Desktop. We are looking into the root cause and hope to have a resolution soon.
{% endhint %}

## Preparation

Before you start, you must make sure that Kubernetes is enabled and running within your Docker Desktop installation. To enable Kubernetes in Docker Desktop, you need to open the dashboard of Docker Desktop. Right click the Docker icon in the system tray and click **Dashboard**:

![](https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/2cj7YDrwIHF2wN0I7e07/kube-wsl-1.png)

Click **Settings**, then select **Kubernetes**, tick **Enable Kubernetes**, then click **Apply and Restart** (clicking **Install** in the dialog to install Kubernetes):

![](https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/yDznBTk5mlUQEtbooD3F/kube-wsl-2.gif)

After a few minutes, you will see that Kubernetes is running in the bottom left status bar of Docker Desktop:

![Docker is on the left, Kubernetes is on the right](https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/rnHRXDgudrM025bWte2z/kube-wsl-4.png)

## Deployment

To deploy Portainer within a Kubernetes cluster you can use our provided Helm charts or YAML manifests.

### Deploy using Helm

{% hint style="info" %}
Ensure you're using at least Helm v3.2, which includes support for the `--create-namespace` argument.
{% endhint %}

First add the Portainer Helm repository by running the following commands:

```
helm repo add portainer https://portainer.github.io/k8s/
helm repo update
```

Once the update completes, you're ready to begin the installation. Which method you choose will depend on how you wish to expose the Portainer service:

{% tabs %}
{% tab title="Expose via NodePort" %}
Using the following command, Portainer will be available on port `30777` for HTTP and `30779` for HTTPS:

```
helm upgrade --install --create-namespace -n portainer portainer portainer/portainer \
    --set image.tag=lts
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-kubernetes-via-helm) or [via the Portainer UI](https://app.gitbook.com/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}
{% endtab %}

{% tab title="Expose via Ingress" %}
In this example, Portainer will be deployed to your cluster and assigned a Cluster IP, with an nginx Ingress Controller at the defined hostname. For more on Ingress options, refer to the list of [Chart Configuration Options](https://docs.portainer.io/advanced/helm-chart-configuration-options).

```
helm upgrade --install --create-namespace -n portainer portainer portainer/portainer \
    --set service.type=ClusterIP \
    --set tls.force=true \
    --set image.tag=lts \
    --set ingress.enabled=true \
    --set ingress.ingressClassName=<ingressClassName (eg: nginx)> \
    --set ingress.annotations."nginx\.ingress\.kubernetes\.io/backend-protocol"=HTTPS \
    --set ingress.hosts[0].host=<fqdn (eg: portainer.example.io)> \
    --set ingress.hosts[0].paths[0].path="/"
```

{% endtab %}

{% tab title="Expose via Load Balancer" %}
Using the following command, Portainer will be available at an assigned Load Balancer IP on port `9000` for HTTP and `9443` for HTTPS:

```
helm upgrade --install --create-namespace -n portainer portainer portainer/portainer \
    --set service.type=LoadBalancer \
    --set image.tag=lts
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-kubernetes-via-helm) or [via the Portainer UI](https://app.gitbook.com/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
To explicitly set the target node when deploying the Helm chart on the CLI, include `--set nodeSelector.kubernetes.io/hostname=<YOUR NODE NAME>` in your `helm install` command.
{% endhint %}

### Deploy using YAML manifests

Our YAML manifests support exposing Portainer via either NodePort or Load Balancer.

{% tabs %}
{% tab title="Expose via NodePort" %}
To expose via NodePort, you can use the following command (Portainer will be available on port `30777`  for HTTP and `30779` for  HTTPS):

```
kubectl apply -n portainer -f https://downloads.portainer.io/ce-lts/portainer.yaml
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `30779`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-kubernetes-via-helm) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}
{% endtab %}

{% tab title="Expose via Load Balancer" %}
To expose via Load Balancer, use the following command to provision Portainer at an assigned Load Balancer IP on port `9000` for HTTP and `9443` for HTTPS:

```
kubectl apply -n portainer -f https://downloads.portainer.io/ce-lts/portainer-lb.yaml
```

{% hint style="info" %}
By default, Portainer generates and uses a self-signed SSL certificate to secure port `9443`. Alternatively you can provide your own SSL certificate [during installation](https://docs.portainer.io/advanced/ssl#using-your-own-ssl-certificate-on-kubernetes-via-helm) or [via the Portainer UI](https://docs.portainer.io/admin/settings#ssl-certificate) after installation is complete.
{% endhint %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
To explicitly set the target node when deploying using YAML manifests, run the following one-liner to "patch" the deployment, forcing the pod to always be scheduled on the node it's currently running on:
{% endhint %}

```
kubectl patch deployments -n portainer portainer -p '{"spec": {"template": {"spec": {"nodeSelector": {"kubernetes.io/hostname": "'$(kubectl get pods -n portainer -o jsonpath='{ ..nodeName }')'"}}}}}' || (echo Failed to identify current node of portainer pod; exit 1)
```

## Logging In

Now that the installation is complete, you can log into your Portainer Server instance. Depending on how you chose to expose your Portainer installation, open a web browser and navigate to the following URL:

{% tabs %}
{% tab title="NodePort" %}

```bash
https://localhost:30779/ or http://localhost:30777/
```

Replace `localhost` with the relevant IP address or FQDN if needed, and adjust the port if you changed it earlier.
{% endtab %}

{% tab title="Ingress" %}

```bash
https://<FQDN>/
```

Replace `<FQDN>` with the FQDN of your Portainer instance.
{% endtab %}

{% tab title="Load Balancer" %}

```bash
https://<loadbalancer IP>:9443/ or http://<loadbalancer IP>:9000/
```

Replace `<loadbalancer IP>` with the IP address or FQDN of the load balancer, and adjust the port if you changed it earlier.
{% endtab %}
{% endtabs %}

You will be presented with the initial setup page for Portainer Server.

{% content-ref url="../setup" %}
[setup](https://docs.portainer.io/start/install-ce/server/setup)
{% endcontent-ref %}


# Initial setup

Once the Portainer Server has been deployed, and you have navigated to the instance's URL, you are ready for the initial setup.

## Creating the first user

Your first user will be an administrator. The username defaults to `admin` but you can change it if you prefer. The password must be at least 12 characters long and meet the listed password requirements.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/EHz2CveqyeJ5vIv4RGRB/2.32-initial-setup-username.png" alt=""><figcaption></figcaption></figure>

## Connecting Portainer to your environments

Once the admin user has been created, the **Environment Wizard** will automatically launch. The wizard will help get you started with Portainer.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/s1u0HYVXDH7IofHtOlFV/2.32-initial-setup-welcome-ce.png" alt=""><figcaption></figcaption></figure>

The installation process automatically detects your local environment and sets it up for you. If you want to add additional environments to manage with this Portainer instance, click **Add Environments**. Otherwise, click **Get Started** to start using Portainer!


# Add an environment to an existing installation

If you want to add another environment to your existing Portainer installation, first select the type of environment you would like to add.&#x20;

You can choose to connect to existing environments:

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>Docker Standalone</strong></td><td>Connect to Docker Standalone via URL/IP, API or Socket</td><td></td><td><a href="../admin/environments/add/docker">docker</a></td><td><a href="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/EM13N532ugyNe0wUJ2wW/card-docker.png">card-docker.png</a></td></tr><tr><td><strong>Docker Swarm</strong></td><td>Connect to Docker Swarm via URL/IP, API or Socket</td><td></td><td><a href="../admin/environments/add/swarm">swarm</a></td><td><a href="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/EM13N532ugyNe0wUJ2wW/card-docker.png">card-docker.png</a></td></tr><tr><td><strong>Kubernetes</strong></td><td>Connect to a Kubernetes environment via URL/IP or via kubeconfig import</td><td></td><td><a href="../admin/environments/add/kubernetes">kubernetes</a></td><td><a href="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/unu9UMzXf6iUcMYH3crY/card-kubernetes.png">card-kubernetes.png</a></td></tr><tr><td><strong>Podman</strong></td><td>Connect to a Podman environment via URL/IP or Socket</td><td></td><td><a href="../admin/environments/add/podman">podman</a></td><td><a href="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/RqSk9QNXNLlvoUe8bJrw/podman-logo-tile.png">podman-logo-tile.png</a></td></tr><tr><td><strong>Azure ACI</strong></td><td>Connect to an Azure ACI environment via API</td><td></td><td><a href="../admin/environments/add/aci">aci</a></td><td><a href="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/x2qQNIgeAUjU27j9GPkT/card-aci.png">card-aci.png</a></td></tr></tbody></table>

Or alternatively set up new environments:

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>Provision KaaS Cluster</strong></td><td>Provision a Kubernetes cluster via a cloud provider's Kubernetes as a Service</td><td></td><td><a href="../admin/environments/add/kaas">kaas</a></td><td><a href="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/57qkZQh2xWeqWdeZGRzf/card-kaas-large.png">card-kaas-large.png</a></td></tr><tr><td><strong>Create a Kubernetes cluster</strong></td><td>Create a Kubernetes cluster on existing infrastructure</td><td></td><td><a href="../admin/environments/add/kube-create">kube-create</a></td><td><a href="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/k1qSfWpknB9PLZp7JzLQ/card-kube-create-large.png">card-kube-create-large.png</a></td></tr></tbody></table>


# Updating Portainer

Portainer releases contain new features and bug fixes so it's important to keep your installation up to date. We have [tested and validated](https://docs.portainer.io/requirements-and-prerequisites#valid-configurations) all Portainer version upgrades from 2.0.0 up to the latest release.

While it's possible that an untested unvalidated update path might work, we recommend that all update paths are tested and validated on a non-critical system before applying them to your production systems.

{% hint style="info" %}
We added a [backup and restore feature](https://docs.portainer.io/admin/settings#backup-portainer) to Portainer BE 2.7 and strongly recommend that you take a backup of your Portainer instance before updating.
{% endhint %}

{% hint style="info" %}
Starting with CE 2.9 and BE 2.10 Portainer is HTTPS enabled by default and uses port `9443` to serve the UI. HTTP can still be enabled on port `9000` if required.
{% endhint %}

## Update order

In general, we recommend updating your Portainer Server deployment *before* you update the Portainer Agents. When we release new versions of Portainer we ensure that Portainer Server is able to talk to older versions of the Agent, and in most cases the reverse is true, but in some instances we make changes to the Agent that are not fully backward compatible with older versions of Portainer Server.

## Updating Portainer

### From within Portainer

{% hint style="warning" %}
Updating from within Portainer to STS versions (or within STS versions) is currently not available. Only LTS versions will be offered through the in-app update. To switch to or update to STS versions, follow the [manual instructions](#manually-update-portainer) below.
{% endhint %}

From 2.19, Business Edition users are able to update their Portainer installation directly from within Portainer. To do so, click the **Update now** link in the update notification in the bottom left of the Portainer UI.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/BiAodOBcqOcpgv9wynd0/2.19-update-notification.png" alt=""><figcaption></figcaption></figure>

In the confirmation dialog, click **Start update** to proceed with the update.

{% hint style="warning" %}
Remember to [back up your Portainer installation](https://docs.portainer.io/admin/settings#backup-portainer) before updating!
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/dGCoQWhdKjTUkOmPcqLP/2.19-update-confirmation.png" alt=""><figcaption></figcaption></figure>

### Manually update Portainer

If you would prefer to manually update your Portainer installation, choose your platform then follow the instructions:

{% content-ref url="upgrade/docker" %}
[docker](https://docs.portainer.io/start/upgrade/docker)
{% endcontent-ref %}

{% content-ref url="upgrade/swarm" %}
[swarm](https://docs.portainer.io/start/upgrade/swarm)
{% endcontent-ref %}

{% content-ref url="upgrade/podman" %}
[podman](https://docs.portainer.io/start/upgrade/podman)
{% endcontent-ref %}

{% content-ref url="upgrade/kubernetes" %}
[kubernetes](https://docs.portainer.io/start/upgrade/kubernetes)
{% endcontent-ref %}

### Update the Portainer Agent

To update the standard (non-Edge) Portainer Agent, you can find instructions in the above platform-specific links ([Docker Standalone](https://docs.portainer.io/start/docker#agent-only-upgrade), [Docker Swarm](https://docs.portainer.io/start/upgrade/swarm), [Podman](https://docs.portainer.io/start/upgrade/podman) and [Kubernetes](https://docs.portainer.io/start/upgrade/kubernetes)).

If you are using the Portainer Edge Agent, we have specific update instructions for you:

{% content-ref url="upgrade/edge" %}
[edge](https://docs.portainer.io/start/upgrade/edge)
{% endcontent-ref %}

### Upgrading to Business Edition

If you are coming from Portainer CE or the 1.24.x branch, we have guides for you as well.

{% content-ref url="upgrade/tobe" %}
[tobe](https://docs.portainer.io/start/upgrade/tobe)
{% endcontent-ref %}


# Updating on Docker Standalone

{% hint style="info" %}
Always match the agent version to the Portainer Server version. In other words, when you're installing or updating to Portainer 2.39.0 make sure all of the agents are also on version 2.39.0.
{% endhint %}

{% hint style="danger" %}
If you are updating from the 1.x version of Portainer, you **must** first [update to 2.0.0](https://docs.portainer.io/start/upgrade/from-1.x) **before** updating to the newest version or you will run into issues.
{% endhint %}

{% hint style="danger" %}
Before beginning any update, we highly recommend [taking a backup](https://docs.portainer.io/admin/settings/general#back-up-portainer) of your current Portainer configuration.
{% endhint %}

## Updating your Portainer Server

{% hint style="warning" %}
Starting from Portainer CE 2.9 and BE 2.10, HTTPS is enabled by default on port `9443`. These instructions will configure Portainer to use 9443 for HTTPS and do not expose 9000 for HTTP. If you need to retain HTTP access, you can add:

`-p 9000:9000`

to your command.

You can also choose to [completely disable HTTP](https://github.com/portainer/portainer-docs/blob/2.21/admin/settings/general/README.md#force-https-only) after the update. Before you make Portainer HTTPS only, make sure you have all your Agents and Edge Agents already communicating with Portainer using HTTPS.
{% endhint %}

{% hint style="info" %}
This article assumes that you used our recommended deployment scripts.
{% endhint %}

To update to the latest version of Portainer Server, use the following commands to stop then remove the old version. Your other applications/containers will not be removed.

```
docker stop portainer
```

```
docker rm portainer
```

Now that you have stopped and removed the old version of Portainer, you must ensure that you have the most up to date version of the image locally. You can do this with a `docker pull` command:

{% tabs %}
{% tab title="Business Edition" %}

```
docker pull portainer/portainer-ee:lts
```

{% endtab %}

{% tab title="Community Edition" %}

```
docker pull portainer/portainer-ce:lts
```

{% endtab %}
{% endtabs %}

Finally, deploy the updated version of Portainer:

{% tabs %}
{% tab title="Business Edition" %}

```
docker run -d -p 8000:8000 -p 9443:9443 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ee:lts
```

{% endtab %}

{% tab title="Community Edition" %}

```
docker run -d -p 8000:8000 -p 9443:9443 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:lts
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
These `docker run` commands include opening port `8000` which is used for Edge Agent communication as included in our [installation instructions](https://docs.portainer.io/start/install/server/docker/linux). If you do not need this port open, you can remove it from the command.
{% endhint %}

{% hint style="info" %}
To provide your own SSL certs you may use `--sslcert` and `--sslkey` flags as below to provide the certificate and key files. The certificate file needs to be the full chain and in PEM format. For example, for Business Edition:

```
docker run -d -p 8000:8000 -p 9443:9443 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ee:lts --sslcert /path/to/cert/portainer.crt --sslkey /path/to/cert/portainer.key
```

{% endhint %}

The newest version of Portainer will now be deployed on your system, using the persistent data from the previous version, and will also upgrade the Portainer database to the new version.

When the deployment is finished, go to `https://your-server-address:9443` or `http://your-server-address:9000` and log in. You should notice that the update notification has disappeared and the version number has been updated.

## Agent-only update

To update to the latest version of Portainer Agent, use the following commands to stop then remove the old version. Your other applications/containers will not be removed.

```
docker stop portainer_agent
```

```
docker rm portainer_agent
```

Next, pull the updated version of the image:

```
docker pull portainer/agent:lts
```

Finally, start the agent with the updated image:

```
docker run -d -p 9001:9001 --name portainer_agent --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker/volumes:/var/lib/docker/volumes portainer/agent:lts
```

{% hint style="warning" %}
If you have set a custom `AGENT_SECRET` on your Portainer Server instance (by specifying an `AGENT_SECRET` environment variable when starting the Portainer Server container) you must remember to explicitly provide the same secret to your Agent in the same way (as an environment variable) when updating your Agent:

`-e AGENT_SECRET=yoursecret`
{% endhint %}


# Updating on Docker Swarm

{% hint style="info" %}
Always match the agent version to the Portainer Server version. In other words, when you're installing or updating to Portainer 2.39.0 make sure all of the agents are also on version 2.39.0.
{% endhint %}

{% hint style="warning" %}
Starting from Portainer CE 2.9 and BE 2.10, HTTPS is enabled by default on port `9443`. These instructions will configure Portainer to use 9443 for HTTPS  and 9000 for HTTP. You can choose to [completely disable HTTP](https://docs.portainer.io/admin/settings#force-https-only) after the update.&#x20;

Before you make Portainer HTTPS only, make sure you have all your Agents and Edge Agents already communicating with Portainer using HTTPS.&#x20;
{% endhint %}

{% hint style="danger" %}
If you are updating from the 1.x version of Portainer, you **must** first [update to 2.0.0](https://docs.portainer.io/start/upgrade/from-1.x) **before** updating to the newest version or you will run into issues.
{% endhint %}

{% hint style="danger" %}
Before beginning any update, we highly recommend [taking a backup](https://docs.portainer.io/admin/settings/general#back-up-portainer) of your current Portainer configuration.
{% endhint %}

To update the Portainer Server and the agents on Docker Swarm, first run the following command on the manager node of your Docker Swarm cluster:

```
docker service ls 
```

Make note of the service names for Portainer. You will need them later.

```
ID             NAME                    MODE         REPLICAS   IMAGE                          PORTS
tb9gtxc647fw   portainer-agent_agent   global       3/3        portainer/agent:2.39.0
m3a3mtuy55ed   portainer_portainer     replicated   1/1        portainer/portainer-ee:2.39.0  *:8000->8000/tcp, *:9000->9000/tcp
```

To update Portainer Server to the most recent version, run one of the sets of commands below depending on your edition of Portainer (replace the `portainer_portainer` service name if your setup differs):

{% tabs %}
{% tab title="Business Edition" %}

```
docker pull portainer/portainer-ee:lts
docker service update --image portainer/portainer-ee:lts --publish-add 9443:9443 --force portainer_portainer
```

{% endtab %}

{% tab title="Community Edition" %}

```
docker pull portainer/portainer-ce:lts
docker service update --image portainer/portainer-ce:lts --publish-add 9443:9443 --force portainer_portainer
```

{% endtab %}
{% endtabs %}

To update the Portainer Agent to the latest version, run the commands below (replace the `portainer_agent` service name if your setup differs):

```
docker pull portainer/agent:lts
docker service update --image portainer/agent:lts --force portainer_agent 
```

This will deploy the newest version of Portainer and the agent across your swarm and upgrade the Portainer database to match.

When this is finished, go to `https://your-server-address:9443` or `http://your-server-address:9000` and log in. You should notice that the update notification has disappeared and the version number has been updated.


# Updating on Podman

{% hint style="info" %}
Always match the agent version to the Portainer Server version. In other words, when you're installing or updating to Portainer 2.39.0 make sure all of the agents are also on version 2.39.0.
{% endhint %}

{% hint style="danger" %}
Before beginning any update, we highly recommend [taking a backup](https://docs.portainer.io/admin/settings/general#back-up-portainer) of your current Portainer configuration.
{% endhint %}

## Updating your Portainer Server

{% hint style="warning" %}
Starting from Portainer CE 2.9 and BE 2.10, HTTPS is enabled by default on port `9443`. These instructions will configure Portainer to use 9443 for HTTPS and do not expose 9000 for HTTP. If you need to retain HTTP access, you can add:

`-p 9000:9000`

to your command.

You can also choose to [completely disable HTTP](https://github.com/portainer/portainer-docs/blob/2.21/admin/settings/general/README.md#force-https-only) after the update. Before you make Portainer HTTPS only, make sure you have all your Agents and Edge Agents already communicating with Portainer using HTTPS.
{% endhint %}

{% hint style="info" %}
This article assumes that you used our recommended deployment scripts.
{% endhint %}

To update to the latest version of Portainer Server, use the following commands to stop then remove the old version. Your other applications/containers will not be removed.

```
podman stop portainer
```

```
podman rm portainer
```

Now that you have stopped and removed the old version of Portainer, you must ensure that you have the most up to date version of the image locally. You can do this with a `podman pull` command:

{% tabs %}
{% tab title="Business Edition" %}

```
podman pull portainer/portainer-ee:lts
```

{% endtab %}

{% tab title="Community Edition" %}

```
podman pull portainer/portainer-ce:lts
```

{% endtab %}
{% endtabs %}

Finally, deploy the updated version of Portainer:

{% tabs %}
{% tab title="Business Edition" %}

```
podman run -d -p 8000:8000 -p 9443:9443 --name=portainer --restart=always --privileged -v /run/podman/podman.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ee:lts
```

{% endtab %}

{% tab title="Community Edition" %}

```
podman run -d -p 8000:8000 -p 9443:9443 --name=portainer --restart=always --privileged -v /run/podman/podman.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:lts
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
These `podman run` commands include opening port `8000` which is used for Edge Agent communication as included in our [installation instructions](https://docs.portainer.io/start/install/server/docker/linux). If you do not need this port open, you can remove it from the command.
{% endhint %}

{% hint style="info" %}
To provide your own SSL certs you may use `--sslcert` and `--sslkey` flags as below to provide the certificate and key files. The certificate file needs to be the full chain and in PEM format. For example, for Business Edition:

```
podman run -d -p 8000:8000 -p 9443:9443 --name=portainer --restart=always --privileged -v /run/podman/podman.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ee:lts --sslcert /path/to/cert/portainer.crt --sslkey /path/to/cert/portainer.key
```

{% endhint %}

The newest version of Portainer will now be deployed on your system, using the persistent data from the previous version, and will also upgrade the Portainer database to the new version.

When the deployment is finished, go to `https://your-server-address:9443` or `http://your-server-address:9000` and log in. You should notice that the update notification has disappeared and the version number has been updated.

## Agent-only update

To update to the latest version of Portainer Agent, use the following commands to stop then remove the old version. Your other applications/containers will not be removed.

```
podman stop portainer_agent
```

```
podman rm portainer_agent
```

Next, pull the updated version of the image:

```
podman pull portainer/agent:lts
```

Finally, start the agent with the updated image:

```
podman run -d -p 9001:9001 --name portainer_agent --restart=always --privileged -v /run/podman/podman.sock:/var/run/docker.sock -v /var/lib/containers/storage/volumes:/var/lib/docker/volumes portainer/agent:lts
```

{% hint style="warning" %}
If you have set a custom `AGENT_SECRET` on your Portainer Server instance (by specifying an `AGENT_SECRET` environment variable when starting the Portainer Server container) you must remember to explicitly provide the same secret to your Agent in the same way (as an environment variable) when updating your Agent:

`-e AGENT_SECRET=yoursecret`
{% endhint %}


# Updating on Kubernetes

{% hint style="info" %}
Always match the agent version to the Portainer Server version. In other words, when you're installing or updating to Portainer 2.39.0 make sure all of the agents are also on version 2.39.0.
{% endhint %}

{% hint style="warning" %}
Starting from Portainer CE 2.9 and BE 2.10, HTTPS is enabled by default on port `9443`. These instructions will configure Portainer to use both `9443` for HTTPS and `9000` for HTTP. You can choose to [completely disable HTTP](https://docs.portainer.io/admin/settings#force-https-only) after the update.&#x20;

Before you make Portainer HTTPS only, make sure you have all your Agents and Edge Agents already communicating with Portainer using HTTPS.&#x20;
{% endhint %}

{% hint style="danger" %}
Before beginning any update, we highly recommend [taking a backup](https://docs.portainer.io/admin/settings/general#back-up-portainer) of your current Portainer configuration.
{% endhint %}

Select the Portainer update method which matches the original installation method used.

## Method 1: Updating using Helm

{% hint style="info" %}
This article assumes that you installed originally using our [install instructions](https://docs.portainer.io/install/server/kubernetes/baremetal#deploy-using-helm).
{% endhint %}

Add the Portainer Helm repository by running the following commands. Ignore any warnings about the repo already being there:

```
helm repo add portainer https://portainer.github.io/k8s/
helm repo update
```

Next, run one of the following commands to update Portainer:

{% tabs %}
{% tab title="Business Edition" %}

```
helm upgrade -n portainer portainer portainer/portainer \
    --set tls.force=true --set enterpriseEdition.image.tag=lts --set enterpriseEdition.enabled=true
```

{% endtab %}

{% tab title="Community Edition" %}

```
helm upgrade -n portainer portainer portainer/portainer \
    --set tls.force=true --set image.tag=lts
```

{% endtab %}
{% endtabs %}

## Method 2: Updating using YAML Manifest

### Option 1: Via the Portainer UI

The easiest way to update is to use the Portainer UI along with our manifest files. Copy the contents of the manifest file that matches the method you used to deploy Portainer:

{% tabs %}
{% tab title="NodePort" %}
Copy the contents of the relevant NodePort manifest file:

**Business Edition:**

```
https://downloads.portainer.io/ee-lts/portainer.yaml
```

**Community Edition:**

```
https://downloads.portainer.io/ce-lts/portainer.yaml
```

For an agent-only deployment, use one of the following manifests instead:

**Business Edition:**

```
https://downloads.portainer.io/ee-lts/portainer-agent-k8s-nodeport.yaml
```

**Community Edition:**

```
https://downloads.portainer.io/ce-lts/portainer-agent-k8s-nodeport.yaml
```

{% hint style="warning" %}
If you have set a custom `AGENT_SECRET` on your Portainer Server instance (by specifying an `AGENT_SECRET` environment variable when starting the Portainer Server container) you must remember to explicitly provide the same secret to your Agent in the same way (as an environment variable) in the YAML when updating your Agent:

`environment:`\
&#x20; `- AGENT_SECRET: yoursecret`
{% endhint %}
{% endtab %}

{% tab title="Load Balancer" %}
Copy the contents of the relevant Load Balancer manifest file:

**Business Edition:**

```
https://downloads.portainer.io/ee-lts/portainer-lb.yaml
```

**Community Edition:**

```
https://downloads.portainer.io/ce-lts/portainer-lb.yaml
```

For an agent-only deployment, use one of the following manifests instead:

**Business Edition:**

```
https://downloads.portainer.io/ee-lts/portainer-agent-k8s-lb.yaml
```

**Community Edition:**

```
https://downloads.portainer.io/ce-lts/portainer-agent-k8s-lb.yaml
```

{% hint style="warning" %}
If you have set a custom `AGENT_SECRET` on your Portainer Server instance you must remember to explicitly provide this in the YAML when updating your agent:

`environment:`

&#x20; `- AGENT_SECRET: yoursecret`
{% endhint %}
{% endtab %}
{% endtabs %}

Log into Portainer and connect to the Kubernetes environment where Portainer is installed. From the menu select **Applications** then select **Create from manifest**. Toggle **Use namespace(s) specified from manifest** to on, then enter `portainer` in the **Name** field.&#x20;

{% hint style="warning" %}
If you used a different name for your Portainer deployment, use that instead.
{% endhint %}

From the **Build method** selection choose **Web Editor** and ensure **Kubernetes** is selected as the **Deploy type**. Paste the contents of the YAML file then click **Deploy**. Portainer will process the manifest and should return you to the login page once the update is complete.

### Option 2: Via the command line

If you prefer to use the command line to update, you can do so using `kubectl` commands:

{% tabs %}
{% tab title="NodePort" %}
Log into the control node of your Kubernetes cluster and run one of the following commands:

**Business Edition:**

```
kubectl apply -n portainer -f https://downloads.portainer.io/ee-lts/portainer.yaml
```

**Community Edition:**

```
kubectl apply -n portainer -f https://downloads.portainer.io/ce-lts/portainer.yaml
```

For an agent-only deployment, use one of the following commands instead:

**Business Edition:**

```
kubectl apply -n portainer -f https://downloads.portainer.io/ee-lts/portainer-agent-k8s-nodeport.yaml
```

**Community Edition:**

```
kubectl apply -n portainer -f https://downloads.portainer.io/ce-lts/portainer-agent-k8s-nodeport.yaml
```

{% hint style="warning" %}
If you have set a custom `AGENT_SECRET` on your Portainer Server instance (by specifying an `AGENT_SECRET` environment variable when starting the Portainer Server container) you must remember to explicitly provide the same secret to your Agent in the same way (as an environment variable) in the YAML when updating your Agent:

`environment:`\
&#x20; `- AGENT_SECRET: yoursecret`
{% endhint %}
{% endtab %}

{% tab title="Load Balancer" %}
Log into the control node of your Kubernetes cluster and run one of the following commands:

**Business Edition:**

```
kubectl apply -n portainer -f https://downloads.portainer.io/ee-lts/portainer-lb.yaml
```

**Community Edition:**

```
kubectl apply -n portainer -f https://downloads.portainer.io/ce-lts/portainer.yaml
```

For an agent-only deployment, use one of the following commands instead:

**Business Edition:**

```
kubectl apply -n portainer -f https://downloads.portainer.io/ee-lts/portainer-agent-k8s-lb.yaml
```

**Community Edition:**

```
kubectl apply -n portainer -f https://downloads.portainer.io/ce-lts/portainer-agent-k8s-lb.yaml
```

{% hint style="warning" %}
If you have set a custom `AGENT_SECRET` on your Portainer Server instance you must remember to explicitly provide this in the YAML when updating your agent:

`environment:`

&#x20; `- AGENT_SECRET: yoursecret`
{% endhint %}
{% endtab %}
{% endtabs %}

When the deployment is finished you will be able to log into Portainer. You should notice the new version number at the bottom-left of the Portainer UI.

## Method 3: Force an update

If Portainer does not update after running the above commands, you can force a download of the latest image by running the following command:

```
kubectl -n portainer rollout restart deployment.apps/portainer
```

Or, for an agent-only deployment, use this command instead:

```
kubectl -n portainer rollout restart deployment.apps/portainer-agent
```


# Updating on Nomad

In our ongoing efforts to refine and optimize Portainer, we have made the decision to discontinue support for HashiCorp Nomad as an environment type from Portainer version 2.20.0. This decision is based on limited user adoption and the considerable development resources required to maintain Nomad support.


# Updating the Edge Agent

To update the Portainer Edge Agent to the latest version, follow the below instructions for your Edge environment.

{% hint style="info" %}
Always match the agent version to the Portainer Server version. In other words, when you're installing or updating to Portainer 2.39.0 make sure all of the agents are also on version 2.39.0.
{% endhint %}

{% hint style="danger" %}
Before beginning any update, we highly recommend [taking a backup](https://docs.portainer.io/admin/settings/general#back-up-portainer) of your current Portainer configuration.
{% endhint %}

## Docker Standalone

{% hint style="info" %}
Portainer now also has the ability to update Edge Agents on Docker Standalone [directly from within the UI](https://docs.portainer.io/admin/environments/update).
{% endhint %}

To upgrade the Portainer Edge Agent on a Docker Standalone platform, you will first need to note the **Edge identifier** and the **Edge key** for the Edge environment. To find these values, log into Portainer and click **Environments**, then click the name of the environment you are updating.

At the top of the page in the **Edge information** section, you will see the two values you require in the next steps.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/5cMLPGDedyM8CjSeitfy/2.15-upgrade-edge-edgeinfo.png" alt=""><figcaption></figcaption></figure>

Next, on the Edge environment, we need to stop and remove the Edge Agent container.

```
docker stop portainer_edge_agent
docker rm portainer_edge_agent
```

We also want to ensure we have the updated version of the container image locally:

```
docker pull portainer/agent:lts
```

To deploy the updated Edge Agent, replace the `your-edge-identifier-here` and `your-edge-key-here` values in the following command with those you retrieved earlier, then run the command:

```
docker run -d -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker/volumes:/var/lib/docker/volumes -v /:/host -v portainer_agent_data:/data --restart always -e EDGE=1 -e EDGE_ID=your-edge-identifier-here -e EDGE_KEY=your-edge-key-here -e EDGE_INSECURE_POLL=1 --name portainer_edge_agent portainer/agent:lts
```

## Docker Swarm

To update the Portainer Edge Agent on a Docker Swarm environment, run the following commands.

First, to ensure you have the updated container image locally, pull the image:

```
docker pull portainer/agent:lts
```

Then, update the service to use the new image version:

```
docker service update --image portainer/agent:lts --force portainer_edge_agent 
```

## Kubernetes

To update the Portainer Edge Agent on a Kubernetes environment, you will need to first download an updated YAML manifest, then apply that manifest to your existing environment.

To download the manifest, you can use one of the following commands:

{% tabs %}
{% tab title="Business Edition" %}

```
curl -L https://downloads.portainer.io/ee-lts/portainer-agent-edge-k8s.yaml  -o portainer-agent-edge-k8s.yaml
```

{% endtab %}

{% tab title="Community Edition" %}

```
curl -L https://downloads.portainer.io/ce-lts/portainer-agent-edge-k8s.yaml -o portainer-agent-edge-k8s.yaml  
```

{% endtab %}
{% endtabs %}

To apply this manifest to your environment, run the following command:

```
kubectl apply -f portainer-agent-edge-k8s.yaml
```


# Updating from Portainer 1.x

If you are updating a Portainer install that is currently running an image from the 1.x series, there are additional steps you must first take before updating to the most recent version. This document covers the steps depending on your current version - start from the instructions for your current version and work your way down.

* [Version 1.24.0 or older](#updating-from-versions-older-than-1.24.1)
* [Version 1.24.1 or 1.24.2](#updating-from-1.24.1-and-1.24.2)

{% hint style="info" %}
We only provide instructions for Docker Standalone and Docker Swarm environments here, as Portainer 1.x did not support Kubernetes environments.
{% endhint %}

## **Updating from versions older than 1.24.1** <a href="#updating-from-versions-older-than-1.24.1" id="updating-from-versions-older-than-1.24.1"></a>

If you are running a version prior to 1.24.1, you must first update to `portainer/portainer:1.24.2`. Your other applications/containers will not be removed.

### Docker Standalone <a href="#docker-standalone" id="docker-standalone"></a>

Use the following commands to stop then remove the old version, then run Portainer release 1.24.2.

```
docker stop portainer

docker rm portainer

docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer:1.24.2
```

### Docker Swarm <a href="#docker-swarm" id="docker-swarm"></a>

Run the following command to update the Portainer service to 1.24.2. This assumes your service is named `portainer_portainer` (you can confirm this by checking the output of `docker service ls`).

```
docker service update --image portainer/portainer:1.24.2 --force portainer_portainer
```

Verify that you are running version 1.24.2 by logging into Portainer and reading the version number on the bottom-left of the UI. You should now proceed to [update to version 2.0.0](#updating-from-1.24.1-and-1.24.2).

## Updating from 1.24.1 and 1.24.2 <a href="#updating-from-1.24.1-and-1.24.2" id="updating-from-1.24.1-and-1.24.2"></a>

If you are running version 1.24.1 or 1.24.2 and want to update to the latest Portainer release, you must first update to `portainer/portainer-ce:2.0.0`. Use the following commands to stop then remove the old version. Your other applications/containers will not be removed.

### Docker Standalone <a href="#docker-standalone-1" id="docker-standalone-1"></a>

```
docker stop portainer
docker rm portainer
```

Now that you have stopped and removed the old version of Portainer, you must ensure that you have the latest version of the 2.0.0 image locally. You can do this with a `docker pull` command:

```
docker pull portainer/portainer-ce:2.0.0
```

Finally, deploy the updated version of Portainer:

```
docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:2.0.0
```

### Docker Swarm <a href="#docker-swarm-1" id="docker-swarm-1"></a>

Run the following command to update the Portainer service to 2.0.0. This assumes your service is named `portainer_portainer` (you can confirm this by checking the output of `docker service ls`).

```
docker service update --image portainer/portainer-ce:2.0.0 --force portainer_portainer
```

Portainer CE 2.0.0 will now be deployed on your system, using the persistent data from the previous version, and will also update the Portainer database to the new version.

When the deployment is finished, go to `http://your-server-address:9000` and log in. Verify that you are running version 2.0.0 by logging into Portainer and reading the version number on the bottom-left of the UI.

## Updating from 2.0.0 <a href="#updating-from-2.0.0" id="updating-from-2.0.0"></a>

Once you have updated to 2.0.0 you can proceed with the [standard update instructions](https://docs.portainer.io/start/upgrade) for your platform, or if you are moving to Business Edition you can follow the [upgrade instructions](https://docs.portainer.io/start/upgrade/tobe).


# Switching to Portainer Business Edition

It’s easy and quick to upgrade from Portainer CE (both 1.x and 2.x branches) to Portainer Business Edition without losing your data. The following instructions apply whether you’re using a 5 node free license or you’ve purchased a license for Portainer Business Edition.

From version 2.17, you can upgrade your Portainer CE installation to Portainer BE from within Portainer itself.

{% content-ref url="tobe/inapp" %}
[inapp](https://docs.portainer.io/start/upgrade/tobe/inapp)
{% endcontent-ref %}

If you would like to upgrade manually, you can find instructions for your environment at the following links:

{% content-ref url="tobe/docker" %}
[docker](https://docs.portainer.io/start/upgrade/tobe/docker)
{% endcontent-ref %}

{% content-ref url="tobe/swarm" %}
[swarm](https://docs.portainer.io/start/upgrade/tobe/swarm)
{% endcontent-ref %}

{% content-ref url="tobe/kubernetes" %}
[kubernetes](https://docs.portainer.io/start/upgrade/tobe/kubernetes)
{% endcontent-ref %}

For Agent-only deployments, you do not need to upgrade the Agent to Business Edition.

{% content-ref url="tobe/agent" %}
[agent](https://docs.portainer.io/start/upgrade/tobe/agent)
{% endcontent-ref %}


# Upgrade to Business Edition from within Portainer Community Edition

To upgrade from Portainer Community Edition to Portainer Business Edition from within Portainer, log in as an administrator and click the **Upgrade to Business Edition** message in the top left.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/w0C8BG2NwMgd8s2pMcDl/2.32-start-upgradetobe.gif" alt=""><figcaption></figcaption></figure>

If you already have a license for Portainer Business Edition, paste it in the box and click **Start upgrade** to begin the upgrade process.

If you do not currently have a license, click **Get a license** and fill out the form to receive a trial key.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/A7w6CmBFpCgPYSWvH38x/2.17-upgrade-tobe-inapp-licenseform.png" alt=""><figcaption></figcaption></figure>

Your trial key will be sent to the email address you provided and you will be returned to the license entry form.

{% hint style="info" %}
Your license should be sent automatically within a few minutes. If you have not received it please check your spam folders, or [get in touch with our team](mailto:success@portainer.io) if you have not received it in 24 hours.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/D9uLCgf7m3XD08O7oHME/2.17-upgrade-tobe-inapp-licensesent.png" alt=""><figcaption></figcaption></figure>

When you receive your license, paste the key into the box and click **Start upgrade** to begin the upgrade process.


# Docker Standalone

{% hint style="warning" %}
This article assumes that you used our recommended deployment scripts.
{% endhint %}

{% hint style="info" %}
Before you begin, copy the license key from the email we sent you.
{% endhint %}

The process for switching to Portainer Business Edition is straightforward but does depend on which version of Portainer you are currently running. Start from the instructions for your current version and work your way down.

* [Version 1.24.0 or older](#upgrading-from-versions-older-than-1.24.1)
* [Version 1.24.1 or 1.24.2](#upgrading-from-1.24.1-and-1.24.2)
* [Version 2.0.0 or newer](#upgrading-from-version-2.0.0-and-later)

## **Upgrading from versions older than 1.24.1**

If you are running a version prior to 1.24.1, you must first upgrade to `portainer/portainer:1.24.2`. Your other applications/containers will not be removed. Use the following commands to stop then remove the old version, then run Portainer release 1.24.2:

```
docker stop portainer

docker rm portainer

docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer:1.24.2
```

Verify that you are running version 1.24.2 by logging into Portainer and reading the version number on the bottom-left of the UI. You should now proceed to [upgrade to version 2.0.0](#upgrading-from-1.24.1-and-1.24.2).

## Upgrading from 1.24.1 and 1.24.2

If you are running a version prior to 1.24.1 and want to upgrade to the latest Portainer release, you must first upgrade to `portainer/portainer-ce:2.0.0`, use the following commands to stop then remove the old version. Your other applications/containers will not be removed.

```
docker stop portainer
```

```
docker rm portainer
```

Now that you have stopped and removed the old version of Portainer, you must ensure that you have the latest version of the image locally. You can do this with a `docker pull` command:

```
docker pull portainer/portainer-ce:2.0.0
```

Finally, deploy the updated version of Portainer:

```
docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:2.0.0
```

Portainer CE 2.0.0 will now be deployed on your system, using the persistent data from the previous version, and will also upgrade the Portainer database to the new version.

When the deployment is finished, go to `http://your-server-address:9000` and log in. Verify that you are running version 2.0.0 by logging into Portainer and reading the version number on the bottom-left of the UI. You can now [upgrade to the latest version](#upgrading-from-version-2.0.0-and-later) of Portainer Business Edition.

## Upgrading from version 2.0.0 and later

To upgrade to Portainer Business Edition for Docker Standalone, use the following commands to stop then remove the old version. Your other applications/containers will not be removed.

```
docker stop portainer
docker rm portainer
```

Now that you have stopped and removed the old version of Portainer, run this command to deploy the most up to date version of Portainer Business:

```
docker run -d -p 8000:8000 -p 9000:9000 -p 9443:9443 --name=portainer --restart=always --pull=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ee:lts
```

Log out of Portainer (if currently logged in) then log back in. When you log in for the first time, you'll be asked to enter your license key. Paste this in from the email we sent you.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/40NW14ZftG24CEtTqIT7/2.20-initial-setup-license.png" alt=""><figcaption></figcaption></figure>

'Business Edition' now appears in the bottom-left corner.


# Docker Swarm

{% hint style="warning" %}
This article assumes that you used our recommended deployment scripts.
{% endhint %}

{% hint style="info" %}
Before you begin, copy the license key from the email we sent you.
{% endhint %}

To upgrade to Portainer Business Edition for Docker Swarm, use the following commands to deploy the newest version of Portainer Business on your Swarm Cluster:

```
docker service update --image portainer/portainer-ee:sts --force portainer_portainer
```

Log out of Portainer (if currently logged in) then log back in. When you log in for the first time, you'll be asked to enter your license key. Paste this in from the email we sent you.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/40NW14ZftG24CEtTqIT7/2.20-initial-setup-license.png" alt=""><figcaption></figcaption></figure>

'Business Edition' now appears in the bottom-left corner.


# Podman

{% hint style="warning" %}
This article assumes that you used our recommended deployment scripts.
{% endhint %}

{% hint style="info" %}
Before you begin, copy the license key from the email we sent you.
{% endhint %}

To upgrade to Portainer Business Edition for Podman, use the following commands to stop then remove the old version. Your other applications/containers will not be removed.

```
podman stop portainer
podman rm portainer
```

Now that you have stopped and removed the old version of Portainer, run this command to deploy the most up to date version of Portainer Business:

```
podman run -d -p 8000:8000 -p 9000:9000 -p 9443:9443 --name=portainer --restart=always --pull=always --privileged -v /run/podman/podman.sock:/run/podman/podman.sock -v portainer_data:/data portainer/portainer-ee:sts
```

Log out of Portainer (if currently logged in) then log back in. When you log in for the first time, you'll be asked to enter your license key. Paste this in from the email we sent you.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/40NW14ZftG24CEtTqIT7/2.20-initial-setup-license.png" alt=""><figcaption></figcaption></figure>

'Business Edition' now appears in the bottom-left corner.


# Kubernetes

{% hint style="info" %}
Select the Portainer CE to Portainer Business upgrade method below which matches the original installation method used.
{% endhint %}

## Method 1: Upgrade via Helm

To update your Helm repository, run this command first:

```
helm repo update
```

Run this command next to deploy the latest version of Portainer Business on your Kubernetes cluster with all of the settings used in your Helm deployment:

```
helm upgrade -n portainer portainer portainer/portainer --set enterpriseEdition.enabled=true
```

## Method 2: Upgrade via YAML Manifests

Choose the right YAML manifest based on your original deployment:

{% tabs %}
{% tab title="NodePort" %}
Use the following `kubectl` command to update a NodePort deployment:

```
kubectl apply -n portainer -f https://downloads.portainer.io/ee-sts/portainer.yaml
```

{% endtab %}

{% tab title="Load Balancer" %}
Use the following `kubectl` command to update a Load Balancer deployment:

```
kubectl apply -n portainer -f https://downloads.portainer.io/ee-sts/portainer-lb.yaml
```

{% endtab %}
{% endtabs %}

This will deploy the newest version of Portainer Business on your Kubernetes cluster.

## Logging back in

When the upgrade is complete, log out of Portainer (if currently logged in) then log back in. When you log in for the first time, you'll be asked to enter your license key. Paste this in from the email we sent you.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/40NW14ZftG24CEtTqIT7/2.20-initial-setup-license.png" alt=""><figcaption></figcaption></figure>

'Business Edition' now appears in the bottom-left corner.


# Upgrading Agent-only deployments

Both Portainer Community Edition and Portainer Business Edition use the same Portainer Agent container image to run, so if you are upgrading from CE to BE and have Agent-only environments, you don't need to upgrade them as well - just ensure they are on the same version (for example, if the Portainer Server is version 2.39.0 then the Portainer Agent should be 2.39.0 as well).


# Home

The **Home** page is the first page you will see after logging into Portainer. This page provides an overview of your environments along with vital statistics about each. You can search and filter your list of environments using the options at the top of the list.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/ouCCdcpPdb0PcMO8pVkh/2.32-user-home.png" alt=""><figcaption></figcaption></figure>

Your currently selected environment (if any) will be shown by the **Connected** status on the right. To choose an environment, either click on the tile for the environment or the **Live connect** or **Browse snapshot** button (for [Edge Devices in async mode](https://docs.portainer.io/user/home/snapshot)). You can click the pencil icon to edit the environment's connection configuration, and the cog button to go to the environment's settings page (if the environment is directly accessible).

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/uyIU7fF5cgc7zeczR1Hx/2.32-user-home-buttons.png" alt=""><figcaption></figcaption></figure>

## Build information

You can view the build information for your Portainer installation by clicking on the Portainer version number in the bottom left of the UI. This may be helpful when troubleshooting issues with the Portainer support team.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/foTSECDNBpEXWH6zzstm/2.32-user-home-buildinfo.png" alt=""><figcaption></figcaption></figure>

In the box that appears you can see the server version, database version, build number and image tag, as well as the versions of the compilation tools, dependencies, and environment variables used to build Portainer.&#x20;

## Getting help

From any page in the Portainer UI, you can click on the **question mark icon** in the top right next to your username to access the related section of this documentation. You can also click the **robot icon** to start a conversation with our [AI chatbot](https://portainer.io/ask-the-ai).&#x20;

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/NniPxCS2jxZytIuH8lBY/2.25.0-icons.png" alt=""><figcaption></figcaption></figure>


# Snapshot browsing

Snapshot browsing allows the ability to run remote commands on your Edge devices that are in Async mode. You can browse your device as well as run commands like start, stop, restart, and delete on your containers, stacks and volumes.

To browse your Edge device, on the [home page](https://docs.portainer.io/user/home) locate your Edge device and click the **Browse snapshot** button.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/fUQvuFYZHOMqVfPqKuU2/2.33-home-edge-async-tile.png" alt=""><figcaption></figcaption></figure>

You will be directed to the dashboard for the Edge device, with a **Browsing snapshot** drop down that details the last updated and next updated date, how often the snapshots are taken and the environment status.  You can refer to the [deployment sync options ](https://docs.portainer.io/admin/settings/edge#deployment-sync-options)for more details.&#x20;

{% hint style="warning" %}
The information displayed in Portainer for your Edge device is up to date as of the time the latest snapshot (as indicated in the dropdown) was taken. Depending on the [age of the snapshot](https://docs.portainer.io/admin/settings/edge#deployment-sync-options) and the environment, this may not be an up to date representation of the current state of the device, so bear this in mind when taking actions on the device.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/2bTtUQ3qFSGVcWJW6w6c/2.33-snapshot-browse-details.png" alt=""><figcaption></figcaption></figure>

From here, you can browse the device as you would a regular environment.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/V9RRFgtwCIzxYgBhFT07/2.33-snapshot-browse.gif" alt=""><figcaption></figcaption></figure>


# OpenAMT

{% hint style="danger" %}
OpenAMT integration is now deprecated and will be removed in a future release.
{% endhint %}

OpenAMT allows you to remotely manage your compatible Edge devices from Portainer, letting you start, stop, restart and access the device console directly from within the Portainer UI.

## Preparation

To associate an Edge device with OpenAMT you must first add a compatible device. To do this, first [deploy the Edge Agent](https://docs.portainer.io/admin/environments/add) to your device based on the appropriate method for your environment type.

Once the Edge Agent has been set up and deployed on the remote device, the device is ready to be associated with OpenAMT.

## Associate your device

To associate an existing Edge Agent deployment with OpenAMT, from the Home page click the **Associate with OpenAMT** button.&#x20;

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/kiVZEKynvX0lBi1TswbP/2.18-home-openamt-associate-button.png" alt=""><figcaption></figcaption></figure>

Check the box next to the device(s) you want to associate, then click the **Associate Devices** button. The activation process will now begin.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/uDHsMlVwX5XEl7Mff00I/2.18-home-openamt-associate-dialog.png" alt=""><figcaption></figcaption></figure>

Once activation completes you will be returned to the Home page.&#x20;

## Interact with your device

Once an OpenAMT device has been associated with an Edge Device in Portainer, you are able to interact directly with that device. To do so, go to the Home page and use the options on the right hand side of the tile to interact as required.

* **Power ON**: Will power on the device if it is currently switched off.
* **Power OFF**: Will power off the device if it is currently switched on.
* **Restart**: Will initiate a restart of the device.
* **KVM**: Will open a remote KVM (keyboard, video, mouse) session with the device.


# Docker/Swarm/Podman

The following sections describe how to manage a Docker Standalone, Docker Swarm or Podman environment using menu options available in the Portainer Server.

{% content-ref url="docker/dashboard" %}
[dashboard](https://docs.portainer.io/user/docker/dashboard)
{% endcontent-ref %}

{% content-ref url="docker/templates" %}
[templates](https://docs.portainer.io/user/docker/templates)
{% endcontent-ref %}

{% content-ref url="docker/stacks" %}
[stacks](https://docs.portainer.io/user/docker/stacks)
{% endcontent-ref %}

{% content-ref url="docker/services" %}
[services](https://docs.portainer.io/user/docker/services)
{% endcontent-ref %}

{% content-ref url="docker/containers" %}
[containers](https://docs.portainer.io/user/docker/containers)
{% endcontent-ref %}

{% content-ref url="docker/images" %}
[images](https://docs.portainer.io/user/docker/images)
{% endcontent-ref %}

{% content-ref url="docker/networks" %}
[networks](https://docs.portainer.io/user/docker/networks)
{% endcontent-ref %}

{% content-ref url="docker/volumes" %}
[volumes](https://docs.portainer.io/user/docker/volumes)
{% endcontent-ref %}

{% content-ref url="docker/configs" %}
[configs](https://docs.portainer.io/user/docker/configs)
{% endcontent-ref %}

{% content-ref url="docker/secrets" %}
[secrets](https://docs.portainer.io/user/docker/secrets)
{% endcontent-ref %}

{% content-ref url="docker/events" %}
[events](https://docs.portainer.io/user/docker/events)
{% endcontent-ref %}

{% content-ref url="docker/host" %}
[host](https://docs.portainer.io/user/docker/host)
{% endcontent-ref %}

{% content-ref url="docker/swarm" %}
[swarm](https://docs.portainer.io/user/docker/swarm)
{% endcontent-ref %}


# Dashboard

The Docker/Swarm dashboard summarizes your Docker Standalone or Docker Swarm environment and shows the components that make up the environment.&#x20;

## Environment info

{% hint style="info" %}
This section is visible only to Docker Standalone and Podman environments.
{% endhint %}

This section shows the environment name, its URL and port along with any [tags](https://docs.portainer.io/admin/environments/tags#tagging-an-environment). You can also see the number of CPU cores (and their available memory), the Docker/Podman version, and whether or not the Portainer Agent is installed.&#x20;

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/aO9bH5mkOTmYJ7nWHolQ/2.15-docker-standalone-dashboard.png" alt=""><figcaption></figcaption></figure>

## Cluster information

{% hint style="info" %}
This section is visible only to Docker Swarm environments.
{% endhint %}

This section shows how many nodes are in the cluster and a link to the [cluster visualizer](https://docs.portainer.io/user/docker/swarm/cluster-visualizer).

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/yIncfFFEkravONKFMOlQ/2.15-docker-dashboard-swarm.png" alt=""><figcaption></figcaption></figure>

## Summary tiles

The remaining dashboard is made up of tiles showing the number of [stacks](https://docs.portainer.io/user/docker/stacks), [services](https://docs.portainer.io/user/docker/services) (for Docker Swarm), [containers](https://docs.portainer.io/user/docker/containers) (including health and running-status metrics), [images](https://docs.portainer.io/user/docker/images) (and how much disk space they consume), [volumes](https://docs.portainer.io/user/docker/volumes) and [networks](https://docs.portainer.io/user/docker/networks), and GPUs (if enabled).

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/xtWJ9ReVFkGotkWwgnZf/2.15-docker-dashboard-tiles.png" alt=""><figcaption></figcaption></figure>


# Templates

Templates let you deploy a container (or a stack of containers) to an environment with a set of predetermined configuration values while still allowing you to customize the configuration (for example, environment variables).

{% content-ref url="templates/application" %}
[application](https://docs.portainer.io/user/docker/templates/application)
{% endcontent-ref %}

{% content-ref url="templates/custom" %}
[custom](https://docs.portainer.io/user/docker/templates/custom)
{% endcontent-ref %}


# Application

An application template lets you deploy a container (or a stack of containers) to an environment with a set of predetermined configuration values while still allowing you to customize the configuration (for example, environment variables). This page lists the application templates available to deploy on your environment.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/HgyiNIevdPVlMRzP2r88/2.20-templates-application-list.png" alt=""><figcaption></figcaption></figure>

Portainer supports templates of both individual containers and stacks of containers.

{% content-ref url="deploy-stack" %}
[deploy-stack](https://docs.portainer.io/user/docker/templates/deploy-stack)
{% endcontent-ref %}

{% content-ref url="deploy-container" %}
[deploy-container](https://docs.portainer.io/user/docker/templates/deploy-container)
{% endcontent-ref %}

By default, Portainer provides a pre-built set of app templates, but you are free to modify or [replace these with your own](https://docs.portainer.io/advanced/app-templates/build). You can also create your own custom templates either manually or from an existing stack.


# Custom templates

A custom template can be used to help streamline the deployment of a container or stack.

{% hint style="info" %}
You can also [create a template from an existing deployed stack](https://docs.portainer.io/user/docker/stacks/template).
{% endhint %}

## Viewing the list of custom templates

To view a list of custom templates, from the menu expand **Templates** then select **Custom**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/TthGKuyX2cQgz6Bb35Ke/custom-templates-new.gif" alt=""><figcaption></figcaption></figure>

## Creating a new custom template

### Entering the basic information

Click **Add Custom Template** then complete the details, using the table below as a guide.

| Field/Option | Overview                                                                                    |
| ------------ | ------------------------------------------------------------------------------------------- |
| Title        | Give the template a descriptive name.                                                       |
| Description  | Enter a brief description of what your template includes.                                   |
| Note         | Note any extra information about the template (optional).                                   |
| Logo         | Enter the URL to a logo to be used for the template when it appears in the list (optional). |
| Platform     | Select the compatible platform for the template. Options are **Linux** or **Windows**.      |
| Type         | Select the type of template. Options are **Standalone / Podman** or **Swarm**.              |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/XV1LOKmo9NbCIad0mYYb/2.22.0-templates-custom-new.png" alt=""><figcaption></figcaption></figure>

### Selecting the build method

Next, choose the build method that suits your needs. You can use the web editor to manually enter your docker-compose file, upload a `docker-compose.yml` file from your local computer, or pull the compose file from a Git repository.

#### Web editor

Paste the contents of your docker-compose file into the box provided. Once all the details have been completed, click **Create custom template**.

{% hint style="info" %}
You can search within the web editor at any time by pressing `Ctrl-F` (or `Cmd-F` on Mac).
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/LRUdPArJU3kHv1WlYoF5/2.20-templates-custom-add-webeditor.png" alt=""><figcaption></figcaption></figure>

#### Upload

Click **Select file** to browse for a docker-compose file to upload. Once all the details have been completed, click **Create custom template**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/ZSGIoUhpPtvKUFJRfQ3S/2.20-templates-custom-add-upload.png" alt=""><figcaption></figcaption></figure>

#### Git repository

Fill in the details for your Git repository.

| Field/Option          | Overview                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authentication        | Enable this if your Git repository requires authentication.                                                                                                                                                                                                                                                                                                                                                                                           |
| Git Credentials       | If the **Authentication** toggle is enabled and you have configured [individual](https://docs.portainer.io/account-settings#git-credentials) or [shared](https://docs.portainer.io/admin/settings/credentials/git) Git credentials, you can select them from this dropdown. Shared Git credentials can be identified with the **Shared** tag, and are only available to administrators at present. Leave this field unset to provide new credentials. |
| Username              | When Authentication is enabled, enter your Git username.                                                                                                                                                                                                                                                                                                                                                                                              |
| Personal Access Token | When Authentication is enabled, enter your personal access token or password.                                                                                                                                                                                                                                                                                                                                                                         |
| Save credential       | When Authentication is enabled and you have provided new credentials, you can tick this box and enter a name to save those credentials for future use.                                                                                                                                                                                                                                                                                                |
| Repository URL        | Enter the URL to your Git repository.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Repository reference  | Select the repository reference to define the branch or tag to pull from.                                                                                                                                                                                                                                                                                                                                                                             |
| Compose path          | Enter the path within the repository to your docker-compose file.                                                                                                                                                                                                                                                                                                                                                                                     |
| Skip TLS Verification | Enable this option to skip verification of your Git repository's TLS certificate.                                                                                                                                                                                                                                                                                                                                                                     |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/tdB0z8SjWC9UJC0KCyYO/2.20-templates-custom-add-git.png" alt=""><figcaption></figcaption></figure>

When all the details have been entered, click **Create custom template**.

## Variables in templates

Custom templates support the use of variables to provide further customization of the deployed stack. A stack can define a variable that can then be adjusted by the user at deployment.

{% hint style="info" %}
This feature is only available in Portainer Business Edition.
{% endhint %}

Variables are identified in stacks with `{{ }}`. For example, the following stack provides a `MYSQL_PASSWORD` variable:

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/eAA0K1vWESbWoyIXsx2g/2.15-docker-templates-custom-variables-set.png" alt=""><figcaption></figcaption></figure>

When a variable is defined, options appear to customize how the variable appears when deploying the stack. You can set the **label**, **description** and **default value**.

When a template is deployed, any variables that have been configured are editable:

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/A3xvQWiDSo5hp94fI936/2.15-docker-templates-custom-variables-create.png" alt=""><figcaption></figcaption></figure>


# Deploy a stack

Portainer lets you deploy an entire stack from either a default template or a custom template.

{% hint style="info" %}
You can also [create a template from a stack](https://docs.portainer.io/user/docker/stacks/template).
{% endhint %}

From the menu expand **Templates**, select **Application** or **Custom** (depending on the template) then select the template you want to deploy. In this example we'll create a WordPress stack.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/Cs3XXcwlzhjH0WhmIWwA/deploy-a-stack-new.gif" alt=""><figcaption></figcaption></figure>

Enter a name for the stack and set any required configuration values (these will differ from template to template). Toggle **Enable access control** on or off as required.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/uM3SdEaL2reGhH03gkJv/2.15-docker-deploy-stack-wordpress.png" alt=""><figcaption></figcaption></figure>

Click **Deploy the stack** then wait for the deployment to finish. If the deployment is successful, the new stack will appear in the list. Select it to view the [deployment details](https://docs.portainer.io/user/docker/stacks/edit).

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/txXhbiQ8l65EGou55VcO/2.20-templates-deploy-stack-stacklist.png" alt=""><figcaption></figcaption></figure>


# Deploy a container

Portainer lets you deploy a standalone container from the default templates list.

From the menu expand **Templates** then select **Application** or **Custom** (depending on the container). On the Application templates page you can choose to display only Container templates using the **Type** dropdown.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/knNJAqK3HgGZoLVUJoYs/deploy-a-container-new.gif" alt=""><figcaption></figcaption></figure>

Then, select the container template you want to deploy. Define a name, a network, port mapping and volumes, and toggle **Enable access control** on if needed.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/qYqhbrpKgIABXcpiRq1P/2.15-docker_deploy_container_nginx.png" alt=""><figcaption></figcaption></figure>

You can also make changes to container settings such as port and volume mapping, host file entries, labels and the hostname by clicking **Show advanced options**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/D0n3489G0NNNHMT7iVMz/2.15-docker_deploy_container_nginx_adv_opts.png" alt=""><figcaption></figcaption></figure>

Once you have configured the container, click **Deploy the container**.


# Stacks

A stack is a collection of services, usually related to one application or usage. For example, a WordPress stack definition may include a web server container (such as nginx) and a database container (such as MySQL).

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/VxAo6ujlxheJEb0fQPRO/2.20-stacks-list.png" alt=""><figcaption></figcaption></figure>

Within the Stacks list, you’ll see all stacks that have been previously created in the selected environment. If an environment is deleted, any stacks that belonged to it become orphaned. To display any orphaned stacks, click the three dots in the top right corner and select **Show all orphaned stacks**, [the stack will need to be re-associated](https://docs.portainer.io/faqs/troubleshooting/stacks-deployments-and-updates/how-do-i-recover-orphaned-stacks-from-a-previously-deleted-environment) to be fully recovered.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/xVALKOYBQRMNMmbXD1rS/Show-orphaned-stacks-FAQ.png" alt=""><figcaption></figcaption></figure>

When the [new image indicator](https://docs.portainer.io/user/host/setup#other) feature is enabled, the **Images up to date** column indicates whether the local images in the stack are up to date, with a green tick indicating they are up to date and an orange cross indicating that there is a newer version of an image available at the remote registry. A grey hyphen indicates Portainer was unable to determine whether there is an update available for the images.

You can click the **Reload image indicators** button to recheck the images for your stacks for updates, or to recheck a single stack's images you can click the image indicator icon for that stack.

For more on how this works, have a look at [this article](https://docs.portainer.io/faqs/troubleshooting/stacks-deployments-and-updates/how-does-the-image-update-notification-icon-work).

{% content-ref url="stacks/add" %}
[add](https://docs.portainer.io/user/docker/stacks/add)
{% endcontent-ref %}

{% content-ref url="stacks/edit" %}
[edit](https://docs.portainer.io/user/docker/stacks/edit)
{% endcontent-ref %}

{% content-ref url="stacks/template" %}
[template](https://docs.portainer.io/user/docker/stacks/template)
{% endcontent-ref %}

{% content-ref url="stacks/webhooks" %}
[webhooks](https://docs.portainer.io/user/docker/stacks/webhooks)
{% endcontent-ref %}

{% content-ref url="stacks/migrate" %}
[migrate](https://docs.portainer.io/user/docker/stacks/migrate)
{% endcontent-ref %}

{% content-ref url="stacks/remove" %}
[remove](https://docs.portainer.io/user/docker/stacks/remove)
{% endcontent-ref %}


# Add a new stack

There are four ways to deploy a new stack from Portainer:

| Option                                     | Overview                                                                                                                                 |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| [Web editor](#option-1-web-editor)         | Use our web editor to define the services for the stack using a docker-compose format.                                                   |
| [Upload](#option-2-upload)                 | If you have a `stack.yml` file, you can upload it from your computer and use it to deploy the stack.                                     |
| [Git repository](#option-3-git-repository) | You can use a docker-compose format file hosted in a Git repository.                                                                     |
| Custom template                            | If you have created a [custom stack template](https://docs.portainer.io/user/docker/templates/custom), you can deploy using this option. |

## Option 1: Web editor

From the menu select **Stacks**, click **Add stack**, give the stack a descriptive name then select **Web editor**. Use the web editor to define the services.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/7MdJ4fT4M0Vp59kB0eTh/stacks-web-editor-new-1.gif" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
You can search within the web editor at any time by pressing `Ctrl-F` (or `Cmd-F` on Mac).
{% endhint %}

As part of the stack creation you can enable a stack webhook, allowing you to remotely trigger redeployments of the stack from your repository, for example. You can read more on this in our documentation on [stack webhooks](https://docs.portainer.io/user/docker/stacks/webhooks).

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/pLr3E59z0srizFibrUUZ/2.15-docker_stack_web_editor_webhook.png" alt=""><figcaption></figcaption></figure>

As an optional step, you can also use the web editor to define environment variables. You can use these to define values in your compose file that would vary between deployments (for example, hostnames, database names, etc).

Environment variables can be set individually within Portainer or you can use **Load variables from .env file** to upload a file containing your environment variables. Environment variables you define (either individually or via a .env file) will be available to use in your compose file using an `environment` definition:

```
environment:
  MY_ENVIRONMENT_VARIABLE: ${MY_ENVIRONMENT_VARIABLE}
```

Alternatively, on Docker Standalone and Podman environments you can add `stack.env` as an `env_file` definition to add all the environment variables that you have defined individually as well as those included in an uploaded .env file:

```
env_file:
  - stack.env
```

**Note:** Using `env_file` to define a file does not work in Docker Swarm due to the lack of `env_file` support in `docker stack deploy` (used on Swarm environments to deploy your stack). On Docker Swarm, you will need to define each environment variable manually.

{% hint style="info" %}
Note the compose file is not changed when environment variables are used - this allows variables to be updated within Portainer without editing the compose file itself. You will still see the `${MY_ENVIRONMENT_VARIABLE}` style entry in the compose file.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/14GwAm1rZRurPvzhWofw/2.15-docker_stack_wed_editor_env_var.png" alt=""><figcaption></figcaption></figure>

You can also select the registries to use when deploying the stack. This is useful when your stack deploys multiple images from different registries that require authentication.

{% hint style="info" %}
By default, all configured registries are used. However, when you have multiple registries from the same provider (like multiple ghcr.io registries), Docker's authentication system may use the wrong credentials during deployment. Explicitly selecting the specific registry ensures the correct credentials are used.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/PlJ0SDdU8VTwHu8GqWRe/2.33-stacks-add-registries.png" alt=""><figcaption></figcaption></figure>

When you're ready, click **Deploy the stack**.

## Option 2: Upload

In Portainer you can create stacks from Compose YML files. To do this, from the menu select **Stacks**, click **Add stack**, then give the stack a descriptive name.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/0bblMhqQDhzjuM9xj1ZH/stacks-upload-new.gif" alt=""><figcaption></figcaption></figure>

Select **Upload** then select the Compose file from your computer.

As part of the stack creation you can enable a stack webhook, allowing you to remotely trigger redeployments of the stack from your repository, for example. You can read more on this in our documentation on [stack webhooks](https://docs.portainer.io/user/docker/stacks/webhooks).

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/pLr3E59z0srizFibrUUZ/2.15-docker_stack_web_editor_webhook.png" alt=""><figcaption></figcaption></figure>

As an optional step, enter any environment variables. You can use these to define values in your compose file that would vary between deployments (for example, hostnames, database names, etc).

Environment variables can be set individually within Portainer or you can use **Load variables from .env file** to upload a file containing your environment variables. Environment variables you define (either individually or via a .env file) will be available to use in your compose file using an `environment` definition:

```
environment:
  MY_ENVIRONMENT_VARIABLE: ${MY_ENVIRONMENT_VARIABLE}
```

Alternatively, you can add `stack.env` as an `env_file` definition to add all the environment variables that you have defined individually as well as those included in an uploaded .env file:

```
env_file:
  - stack.env
```

{% hint style="info" %}
Note the compose file is not changed when environment variables are used - this allows variables to be updated within Portainer without editing the compose file itself which would take it out of sync with your local copy. You will still see the `${MY_ENVIRONMENT_VARIABLE}` style entry in the compose file.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/8vFUlfGYhZnH4k5mnKsE/2.15-docker_add_stack_upload_env_var.png" alt=""><figcaption></figcaption></figure>

When you're ready click **Deploy the stack**.

## Option 3: Git repository

If your Compose file is hosted in a Git repository, you can deploy from there. From the menu select **Stacks**, click **Add stack**, then give the stack a descriptive name.

{% hint style="warning" %}
When a stack is deployed from Git, Portainer will clone the entire Git repository as part of the deployment process. Ensure you have enough free space to accommodate this.
{% endhint %}

{% hint style="warning" %}
Portainer's Git deployment functionality does not currently support the use of Git submodules. If your repository includes submodules, they will not be pulled as part of the deployment. We [hope to add support](https://github.com/orgs/portainer/discussions/9767) for submodules in a future release.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/M7uZudH76f3XQzieaBmK/stacks-git-new.gif" alt=""><figcaption></figcaption></figure>

Select **Git Repository** then enter information about your Git repo.

{% hint style="info" %}
Any Git-compatible repository should work here. Substitute the details as required.
{% endhint %}

| Field/Option          | Overview                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authentication        | Toggle this on if your Git repository requires authentication.                                                                                                                                                                                                                                                                                                                                                                                        |
| Git Credentials       | If the **Authentication** toggle is enabled and you have configured [individual](https://docs.portainer.io/account-settings#git-credentials) or [shared](https://docs.portainer.io/admin/settings/credentials/git) Git credentials, you can select them from this dropdown. Shared Git credentials can be identified with the **Shared** tag, and are only available to administrators at present. Leave this field unset to provide new credentials. |
| Authorization type    | Select either **Basic** or **Token** authorization depending on what your Git repository requires. For example, GitHub, GitLab, and Bitbucket Cloud expect Basic Auth, even when using an API or access token.                                                                                                                                                                                                                                        |
| Username              | Enter your Git username.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Personal Access Token | Enter your personal access token or password.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Save credential       | Check this option to save the credentials entered above for future use under the name provided in the **credential name** field.                                                                                                                                                                                                                                                                                                                      |

{% hint style="info" %}
If you have 2FA configured in GitHub, your passcode is your password.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/z3uZr2HPDfrpLSuIWKjh/2.35-stacks-add-git-auth.png" alt=""><figcaption></figcaption></figure>

| Field/Option          | Overview                                                                                                                                                                                                                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Repository URL        | Enter the repository URL. If you have enabled Authentication above the credentials will be used to access the repository. The below options will be populated by what is found in the repository.                                                                                    |
| Skip TLS verification | Toggle this on to skip the verification of TLS certificates used by your repository. This is useful if your repo uses a self-signed certificate.                                                                                                                                     |
| Repository reference  | Select the reference to use when deploying the stack (for example, the branch).                                                                                                                                                                                                      |
| Compose path          | Enter the path to the Compose file from the root of the repository.                                                                                                                                                                                                                  |
| Additional paths      | Click **Add file** to add additional YAML files to be parsed by the build. This is the equivalent of passing multiple `-f` options to `docker compose`, and abides by the same [merging rules](https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/#merging-rules). |
| GitOps updates        | Toggle this on to enable GitOps updates (see below).                                                                                                                                                                                                                                 |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/p1fPRx3nprvXwuIYK8Mh/2.24.0-docker-stacks-add-git.png" alt=""><figcaption></figcaption></figure>

### GitOps updates

Portainer supports automatically updating your stacks deployed from Git repositories. To enable this, toggle on **GitOps updates** and configure your settings.

{% hint style="info" %}
For more detail on how GitOps updates function under the hood, have a look at [this article](https://docs.portainer.io/faqs/troubleshooting/stacks-deployments-and-updates/how-do-automatic-updates-for-stacks-applications-work).
{% endhint %}

| Field/Option   | Overview                                                                                                                                                                                                                                                                            |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mechanism      | Select the method to use when checking for updates:                                                                                                                                                                                                                                 |
|                | <p><strong>Polling:</strong> Periodically poll the Git repository from Portainer to check for updates to the repository.</p><p><strong>Webhook:</strong> Generate a webhook URL to add to your Git repository to trigger the update on demand (for example via GitHub actions).</p> |
| Fetch interval | If **Polling** is selected, how often Portainer will check the Git repository for updates.                                                                                                                                                                                          |
| Webhook        | When **Webhook** is selected, displays the webhook URL to use in your integration. Click **Copy link** to copy the webhook URL to the clipboard.                                                                                                                                    |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/4AskPw1azRdJMQevX1Sy/2.19-stacks-add-git-polling.png" alt=""><figcaption><p>Automatic updates when using polling</p></figcaption></figure>

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/iz1J1LKHTL8WcUueJwT6/2.19-stacks-add-git-webhook.png" alt=""><figcaption><p>Automatic updates when using webhooks</p></figcaption></figure>

| Field/Option       | Overview                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Re-pull image      | <p>Enable this setting to always pull the most recent version of container images when updating the stack. This is equivalent to the <code>--pull=always</code> flag for <code>docker run</code>.<br>This option was previously labeled as <strong>Pull latest image</strong>.</p>                                                                                                                                                                                                                                                                          |
| Force redeployment | <p>Enable this setting to force the redeployment of your stack at the specified interval (or when the webhook is triggered), overwriting any changes that have been made in the local environment, even if there has been no update to the stack in Git. This is useful if you want to ensure that your Git repository is the source of truth for your stacks and are happy with the local stack being replaced.</p><p>If this option is left disabled, automatic updates will only trigger if Portainer detects a change in the remote Git repository.</p> |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/cPBjSqEdNk4iNExL5Ok5/2.19-stacks-add-git-repull-force.png" alt=""><figcaption></figcaption></figure>

### Relative path volumes

When you toggle **Enable relative path volumes** to on, you are able to specify relative path references in your compose files. Portainer will create the required directory structure and populate the directories with the relevant files from your Git repository.

{% hint style="info" %}
This feature is only available in Portainer Business Edition.
{% endhint %}

On Docker Standalone and Podman environments, specify the path at which you want your files to be created on your host filesystem in the **Local filesystem path** field.

{% hint style="warning" %}
Ensure this directory exists on your local filesystem and is writable.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/AvFdROnyXcwKinZwbtlE/2.17-stacks-add-relativepath.png" alt=""><figcaption></figcaption></figure>

On Docker Swarm environments, specify the path at which you want your files to be created in the Network filesystem path field.

{% hint style="warning" %}
Ensure that this path is available on all of your Docker Swarm nodes and is writable.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/CQ7KAftn6X855td2LoF7/2.17-stacks-add-relativepath-swarm.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
For more detail on how this feature works, have a look at [this article](https://docs.portainer.io/advanced/relative-paths).
{% endhint %}

### Environment variables

As an optional step, you can also set environment variables. You can use these to define values in your compose file that would vary between deployments (for example, hostnames, database names, etc).

Environment variables can be set individually within Portainer or you can use **Load variables from .env file** to upload a file containing your environment variables. Environment variables you define (either individually or via a .env file) will be available to use in your compose file using an `environment` definition:

```
environment:
  MY_ENVIRONMENT_VARIABLE: ${MY_ENVIRONMENT_VARIABLE}
```

Alternatively, you can add `stack.env` as an `env_file` definition to add all the environment variables that you have defined individually as well as those included in an uploaded .env file:

```
env_file:
  - stack.env
```

{% hint style="info" %}
Note the compose file is not changed when environment variables are used - this allows variables to be updated within Portainer without editing the compose file itself which would take it out of sync with the Git repository. You will still see the `${MY_ENVIRONMENT_VARIABLE}` style entry in the compose file.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/14GwAm1rZRurPvzhWofw/2.15-docker_stack_wed_editor_env_var.png" alt=""><figcaption></figcaption></figure>

Enter environment variables if required then click **Deploy the stack**.


# Inspect or edit a stack

## Inspecting a stack

From the menu select **Stacks** then select the stack you want to inspect.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/3LXrPe4TMj6585xaVfyM/view-stack-new.gif" alt=""><figcaption></figcaption></figure>

From here you can stop, delete or [create a template from the stack](https://docs.portainer.io/user/docker/stacks/template), and if deployed from Git you can [detach the stack from the Git repository](#detach-from-git).

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/d3GDJJ1vmwKJwsWIDFNf/2.20-stacks-edit-options.png" alt=""><figcaption></figcaption></figure>

If the stack was deployed from a Git repository, you can:

* Configure [GitOps updates](https://docs.portainer.io/user/docker/add#gitops-updates) or manually pull and redeploy the stack.
* View and edit the stack's environment variables.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/eGiuPUR3P6YHmiQc5D4A/2.20-stacks-edit-git.png" alt=""><figcaption></figcaption></figure>

If the stack was deployed using the [Web Editor](https://docs.portainer.io/user/docker/add#option-1-web-editor) or [uploaded](https://docs.portainer.io/user/docker/add#option-2-upload), you will have the option to [edit your compose file manually](#editing-a-stack).

Regardless of the deployment method used, you can also [migrate or duplicate](https://docs.portainer.io/user/docker/stacks/migrate) the stack.

### Docker Standalone / Podman

When using Docker Standalone or Podman, you can:

* View the containers that make up the stack.
* Check to see if they are running or stopped.
* Get access to logs.
* Inspect individual containers.
* View container statistics.
* Get access to the container's console.

You can also see the image update indicator for each container in the stack. To recheck the image update status for all containers in the stack you can click the reload button next to the search box, or to recheck a single container's image, click the image update indicator icon for that container.&#x20;

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/SRda3b3OyiAikeQfeMcP/2.20-stacks-edit-containers.png" alt=""><figcaption></figcaption></figure>

### Docker Swarm

When using Docker Swarm, you can:

* View the services that make up the stack, and the individual tasks that make up each service.
* Check to see if they are running or stopped.
* See how many replicas are running on each host.
* Get access to logs.
* Inspect individual services.
* View service statistics.
* Get access to the service's console.

You can also see the image update indicator for each service in the stack. To recheck the image update status for all services in the stack you can click the Reload image indicators button, or to recheck a single service's image, click the image update indicator icon for that service.&#x20;

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/UMQrFGMQO8EuyrW5xQKK/2.20-stacks-edit-services.png" alt=""><figcaption></figcaption></figure>

## Editing a stack

Editing a stack allows you to make changes to the configuration and redeploy those changes. To edit a stack, from the menu select **Stacks**, select the stack you want to edit, then select the **Editor** tab.

{% hint style="info" %}
The Editor tab is only available for stacks that were deployed using the [Web Editor](https://docs.portainer.io/user/docker/add#option-1-web-editor). For stacks deployed from a Git repository, the compose file must be edited in the repository itself.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/dTRSmmeAk0U7DrBqpLgr/2.19-stacks-edit-webeditor.png" alt=""><figcaption></figcaption></figure>

Here, you can edit the Compose file for the stack to suit your needs. Using the **Version** dropdown you can also select a previous version of your stack file (if one exists) to switch back to if required. Selecting a different version from the dropdown will replace the contents of the editor with that of the selected version.&#x20;

{% hint style="info" %}
You can search within the web editor at any time by pressing `Ctrl-F` (or `Cmd-F` on Mac).
{% endhint %}

In this section you can expand the Environment variables section to view and make changes to the stack's environment variables.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/Dh9ZWMRMzyolEfXXDByt/2.20-stacks-edit-envvars.png" alt=""><figcaption></figcaption></figure>

You can also toggle the stack [webhook](https://docs.portainer.io/user/docker/stacks/webhooks) and retrieve the webhook URL:&#x20;

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/mQTBxCpNEBpiz2ipgu0z/2.20-stacks-edit-webhook.png" alt=""><figcaption></figcaption></figure>

You can choose to **Prune services** if you have made changes that remove some services from the stack.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/dwP3UkPnLauYOCeuZDxn/2.20-stacks-edit-swarm-prune.png" alt=""><figcaption></figcaption></figure>

When you have finished making changes, click **Update the stack**.

## Detach from Git

If your stack was created from a Git repository, you have the option to detach the stack from the repository. This means you can [edit the stack directly within Portainer](#editing-a-stack), but it does mean that the stack can't be updated from Git anymore. This action also cannot be reversed.

{% hint style="info" %}
Detaching downloads the main compose file for the stack and stores it in Portainer. It does not download any additional compose files or `.env` files that may be contained within the repository.
{% endhint %}

Click **Detach from Git** to detach. You will be asked to confirm the action - click **Detach** to do so.


# Create a template from a deployed stack

In Portainer you can create an [app template](https://docs.portainer.io/user/docker/templates) from deployed stacks. This is useful if you need to deploy the same stack several times.

From the menu select **Stacks**, select the already-deployed stack, then click **Create template from stack**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/3RSLacFKxZgXDzCIQ2yS/create-template-from-stack-new.gif" alt=""><figcaption></figcaption></figure>

Define some properties for the new template, using the table below as a guide.

| Field/Option | Overview                                                                                    |
| ------------ | ------------------------------------------------------------------------------------------- |
| Title        | Give the template a descriptive name.                                                       |
| Description  | Enter a brief description of what your template includes.                                   |
| Note         | Note any extra information about the template (optional).                                   |
| Logo         | Enter the URL to a logo to be used for the template when it appears in the list (optional). |
| Platform     | Select the compatible platform for the template. Options are **Linux** or **Windows**.      |
| Type         | Select the type of template. Options are **Standalone / Podman** or **Swarm**.              |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/XV1LOKmo9NbCIad0mYYb/2.22.0-templates-custom-new.png" alt=""><figcaption></figcaption></figure>

The **Web editor** will be pre-populated with the Compose file for your stack. Make any changes you need here.

{% hint style="info" %}
You can search within the web editor at any time by pressing `Ctrl-F` (or `Cmd-F` on Mac).
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/RzQ3PsorZoKtOZ7ZY1kh/2.20-stacks-template-webeditor.png" alt=""><figcaption></figcaption></figure>

When you're ready, click **Create custom template**.


# Webhooks

A webhook is a POST request sent to a URL that you define in Docker Hub or another registry. Use webhooks to trigger an action in response to an event such as a repository push.

{% hint style="info" %}
This functionality is only available in [Portainer Business Edition](https://www.portainer.io/business-upsell?from=stack-webhook).
{% endhint %}

{% hint style="info" %}
Webhooks are only available on non-Edge environments (environments running Portainer Server or Portainer Agent, not the Portainer Edge Agent). This is because the tunnel to the Portainer Edge Agent is only opened on-demand, and therefore would mean there is no way to expose a webhook permanently.
{% endhint %}

## Enabling a stack webhook

From the menu select **Stacks** then select the container that you want to configure the webhook for. Then select the **Editor** tab.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/LV7E9Z7tIoLgDlZeduXJ/Enabling-a-stack-webhook.gif" alt=""><figcaption></figcaption></figure>

Scroll down to the **Webhooks** section and toggle the **Create a stack webhook** option on. When the URL appears, click **Copy link**. This URL will be used to configure the webhook in your chosen registry.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/QXS0dGcGM4DHvQgHU8Jw/2.15-docker_stack_create_webhook.png" alt=""><figcaption></figcaption></figure>

This example shows how to trigger the webhook using `redeploy`:

```
<form action="https://portainer:9443/api/stacks/webhooks/638e6967-ef77-4906-8af8-236800621360" method="post">
  Redeploy stack containers with latest image of same tag <input type="submit" />
</form>
```

This example shows how to trigger the webhook to update the stack to use a different image tag:

```
<form action="https://portainer:9443/api/stacks/webhooks/638e6967-ef77-4906-8af8-236800621360?tag=latest" method="post">
  Update stack container images with different tag <input type="submit" />
</form>
```

## Preventing a pull

In some cases you may want to override the pulling of images when using the webhook to do a redeploy. In that scenario, you can specify `pullimage=false` as a parameter on your webhook to disable pulling of images.&#x20;

{% hint style="info" %}
This option is only available in Portainer Business Edition.
{% endhint %}

```
<form action="https://portainer:9443/api/stacks/webhooks/638e6967-ef77-4906-8af8-236800621360?pullimage=false" method="post">
  Update stack without pulling images <input type="submit" />
</form>
```

## Using environment variables with webhooks

When triggering a webhook, environment variables can be passed through the endpoint and referenced within stacks' compose files.

To specify an environment variable on a webhook, add it as a variable to the URL. For example, to pass a `SERVICE_TAG` variable with the value `development`:

```
https://portainer:9443/api/stacks/webhooks/1d251d96-fb34-4172-a0a1-d0655467b897?SERVICE_TAG=development
```

To reference the `SERVICE_TAG` variable in your compose file with a fallback to the value `stable`:

```
services:
  my-service:
    image: repository/image:${SERVICE_TAG:-stable}
```

## Configuring the webhook in Docker Hub

To finish the configuration, refer to [Docker's own documentation](https://docs.docker.com/docker-hub/webhooks/).


# Migrate, duplicate or rename a stack

To migrate, duplicate, or rename a stack, open your environment, go to **Stacks**, and select the stack you want to change.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/zXL5F6cBTC6qDi0RqMr4/2.36.0-duplicate-migrate-stacks.gif" alt=""><figcaption></figcaption></figure>

## Migrating a stack

In the **Stack duplication / migration** section, select the destination environment for the stack, and optionally define a new name for the stack. Click **Migrate**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/lQjo4j0KUh5scrYsNsRu/2.36.0-stacks-migrate.png" alt=""><figcaption></figcaption></figure>

Migrating does not relocate the content of any persistent volumes that may be attached to the stack. Acknowledge this warning and confirm the migration by clicking **Migrate**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/S9mhqbZ48QcJFrCF12cR/2.15-stack-migrate-confirm.png" alt=""><figcaption></figcaption></figure>

## Duplicating a stack

In the **Stack duplication / migration** section, give the new stack a descriptive name then select the environment the stack should duplicate to. When you're ready, click **Duplicate**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/lQjo4j0KUh5scrYsNsRu/2.36.0-stacks-migrate.png" alt=""><figcaption></figcaption></figure>

## Rename a stack

In the **Stack duplication / migration** section, give the stack a new descriptive name and select the environment that the stack is currently on. When you're ready, click **Rename**.&#x20;

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/3IXtWVrkhJTa21tmttkZ/2.36.0-stacks-rename.png" alt=""><figcaption></figcaption></figure>

Renaming creates a new stack instance and does not transfer the content of any persistent volumes that may be attached to the stack. Acknowledge this warning and confirm the migration by clicking **Rename**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/y3kBag9h8yeQAIt1m0Yk/2.38-Stack-rename.png" alt=""><figcaption></figcaption></figure>


# Remove a stack

From the menu select **Stacks**, tick the checkbox next to the stack you want to remove, then click **Remove**.&#x20;

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/MC1xO8XMEQDCugfxImB9/Remove-a-stack.gif" alt=""><figcaption></figcaption></figure>

When the confirmation message appears, click **Remove**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/SY7eTsEeu7VsUmQPUeJd/2.15-stack-remove-confirm.png" alt=""><figcaption></figcaption></figure>


# Services

{% hint style="info" %}
The **Services** menu is only available to Docker Swarm endpoints.
{% endhint %}

A service consists of an image definition and container configuration as well as instructions on how those containers will be deployed across a Swarm cluster.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/gq3I1TkB0RO9cTvF4yap/2.20-services-list.png" alt=""><figcaption></figcaption></figure>

When the [new image indicator](https://docs.portainer.io/user/swarm/setup#other) feature is enabled, the **Images up to date** column indicates whether the local images in the service are up to date, with a green tick indicating they are up to date and an orange cross indicating that there is a newer version of an image available at the remote registry. A grey hyphen indicates Portainer was unable to determine whether there is an update available for the images.

You can click the **Reload image indicators** button to recheck the images for all your services for updates, or to recheck a single service's images you can click the image indicator icon for that service.

For more on how this works, have a look at [this article](https://docs.portainer.io/faqs/troubleshooting/stacks-deployments-and-updates/how-does-the-image-update-notification-icon-work).

{% content-ref url="services/add" %}
[add](https://docs.portainer.io/user/docker/services/add)
{% endcontent-ref %}

{% content-ref url="services/configure" %}
[configure](https://docs.portainer.io/user/docker/services/configure)
{% endcontent-ref %}

Once a service has been created you can scale it to meet your needs, as well as view individual task status and logs.

{% content-ref url="services/scale" %}
[scale](https://docs.portainer.io/user/docker/services/scale)
{% endcontent-ref %}

{% content-ref url="services/tasks" %}
[tasks](https://docs.portainer.io/user/docker/services/tasks)
{% endcontent-ref %}

{% content-ref url="services/logs" %}
[logs](https://docs.portainer.io/user/docker/services/logs)
{% endcontent-ref %}

If you need to undo some changes to a service, you can roll it back.

{% content-ref url="services/rollback" %}
[rollback](https://docs.portainer.io/user/docker/services/rollback)
{% endcontent-ref %}

You can also configure webhooks for your services.

{% content-ref url="services/webhooks" %}
[webhooks](https://docs.portainer.io/user/docker/services/webhooks)
{% endcontent-ref %}


# Add a new service

From the menu click **Services** then click **Add service**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/So9VvTLJEkjXLj1wSUY2/Add-service-new.gif" alt=""><figcaption></figcaption></figure>

Complete the fields, using the table below as a guide.

| Field/Option             | Overview                                                                                                                                                                                                                         |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                     | Give the service a descriptive name.                                                                                                                                                                                             |
| Registry                 | Select the registry that contains the image you wish to use for the service.                                                                                                                                                     |
| Image                    | Enter the name of the image. If you're using Docker Hub you can also search for images from here.                                                                                                                                |
| Scheduling mode          | Select either to replicate the service on the same host or deploy it globally with one container on each host.                                                                                                                   |
| Replicas                 | Set the number of replicas (only if the scheduling mode is set to **Replicated**).                                                                                                                                               |
| Port mapping             | Define the ports to expose on the new service.                                                                                                                                                                                   |
| Create a service webhook | Toggle on to create a [webhook](https://docs.portainer.io/user/docker/services/webhooks) for the service. You can send a POST request to this endpoint to automate pulling the most up-to-date image and re-deploy your service. |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/m4ozaWBAeIsz9Gsfh3RA/2.15-docker_service_create_service.png" alt=""><figcaption></figcaption></figure>

You can also configure any advanced options for the service in the bottom section.

When you're finished click **Create the service**.


# Configure service options

From the menu select **Services** then select the service you want to configure.&#x20;

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/mMkgb1eNe712DRVqFgWl/Select-service-new.gif" alt=""><figcaption></figcaption></figure>

## Service details

In this section you can:

* View a summary of the details about the service.
* Configure the number of replicas.
* Toggle the [service webhook](https://docs.portainer.io/user/docker/services/webhooks) on or off.
* View the [service logs](https://docs.portainer.io/user/docker/services/logs).
* Update, [roll back](https://docs.portainer.io/user/docker/services/rollback) or delete the service.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/LQMFpqG9ZZxRu5IcraZJ/2.15-docker_services_service_details.png" alt=""><figcaption></figcaption></figure>

## Container specification configuration options

### Change container image

Here you can replace the container image with a different image. Select the registry, enter the image name, then click **Apply changes**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/u5gAGmRI2Owopjd9klQn/2.15-docker_services_change_container_image.png" alt=""><figcaption></figcaption></figure>

### Environment variables

It's best to set environment variables when you [create a container](https://docs.portainer.io/user/docker/containers/add) and before deployment. You can still set or edit these variables after deployment if you wish.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/erfr6kwYSSv0Q1Q4nCpg/2.15-docker_services_service_env_var.png" alt=""><figcaption></figcaption></figure>

### Container labels

Labels give you a way to record information about a container, such as the way it's configured. Labels can also be used by Portainer to [hide containers from the interface](https://docs.portainer.io/admin/settings#hidden-containers).

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/aM3LlpXN5hnCr2SJv8Xm/2.15-docker_services_service_container_labels.png" alt=""><figcaption></figcaption></figure>

### Mounts

You have the option to either mount or bind volumes in Portainer, and you can also make them read only. To add a mount, first select either **Volume** or **Bind** from the **Type** dropdown.

#### For volume mounts:

Select the volume from the **Source** dropdown, enter the container path in the **Target** field tick **Read only** if required then click **Apply changes**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/7RtHNb8ly3ORacpxrgsC/2.15-docker_services_service_mounts_volume.png" alt=""><figcaption></figcaption></figure>

#### For bind mounts:

Enter the source path in the **Source** field, enter the container path in the **Target** field, tick **Read only** if required then click **Apply changes**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/jWeQrwLxv3keiaew9gtT/2.15-docker_services_service_mounts_bind.png" alt=""><figcaption></figcaption></figure>

## Networks & ports configuration options

### Networks

You can define one or more networks for a service either before or after deployment. Simply select the network from the dropdown then click **Apply changes**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/RLWSVRbzEA4nhRdea5zF/2.15-docker_services_service_networks.png" alt=""><figcaption></figcaption></figure>

### Published ports

Use this setting to publish ports so they can access a container from outside of the host. You can either add new ports or update existing ports.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/sgCORXo5MLTyTMGrNdAm/2.15-docker_services_service_published_ports.png" alt=""><figcaption></figcaption></figure>

### Hosts file entries

Lets you manually specify a hostname or URL and associate the URL to an internal or external IP address.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/Bs2ZOOi6U9l9DNsOsB1E/2.15-docker_services_service_host_entries.png" alt=""><figcaption></figcaption></figure>

## Service specification settings

### Resource limits and reservations

Sets limits on resource utilization, such as memory, CPU reservation and CPU limit.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/pQIalKA2xqDzhATSRJlL/2.15-docker_services_service_resource_limits.png" alt=""><figcaption></figcaption></figure>

### Placement constraints

Use placement constraints to control which nodes a service can be assigned to.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/qXBgwY3l2uBemJCnmWNd/2.15-docker_services_service_placement_constraint.png" alt=""><figcaption></figcaption></figure>

### Placement preferences

While placement constraints limit the nodes a service can run on, placement preferences attempt to place tasks on appropriate nodes in an algorithmic way (by default they are spread evenly).

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/iJ5kRiSBfb1TemgkZit3/2.15-docker_services_service_placement_pref.png" alt=""><figcaption></figcaption></figure>

### Restart policy

Docker's restart policies ensure that linked containers are restarted in the correct order, and control the conditions under which they are restarted:

* **Any**: Restart the container under any conditions (restarted host or Docker daemon).
* **On Failure**: Restart the container if it exits due to an error which manifests as a non-zero exit code.
* **None**: Do not automatically restart the container.

You can also adjust the restart delay, maximum attempts and restart window.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/UNkX0RWmgTmcS59Pb6j3/2.15-docker_services_service_restart_policy.png" alt=""><figcaption></figcaption></figure>

### Update configuration

Updates a service according to the parameters you specify. The parameters specified here are the same as `docker service create` (see [Docker's own documentation](https://docs.docker.com/engine/reference/commandline/service_create/) for more information).

Normally, updating a service will only cause the service’s tasks to be replaced with new ones if a change to the service requires recreating the tasks for it to take effect.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/ydX6lZGK0fzgO29F95zx/2.15-docker_services_service_update_config.png" alt=""><figcaption></figcaption></figure>

### Logging driver

Docker includes logging mechanisms called *logging drivers* that get information from the containers and services you're running. Each Docker daemon has a default logging driver which each container will use, unless you configure them to use a different logging driver.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/RnnTGeo1UxeBK1JbPiKP/2.15-docker_services_service_logging_driver.png" alt=""><figcaption></figcaption></figure>

### Service labels

Lets you add metadata to containers using Docker labels either via an array or a dictionary. We recommend that you use reverse-DNS notation to stop labels from conflicting with those used by other software.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/24fAi88KqASCzShZSik2/2.15-docker_services_service_labels.png" alt=""><figcaption></figcaption></figure>

### Configs

Docker 17.06 introduced Swarm service configs. These allow you to store non-sensitive information such as configuration files outside a service’s image or running containers. This keeps images as generic as possible and removes the need to bind-mount configuration files into containers or use environment variables.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/VnJMX6c7DAXmhzcZ4rIj/2.15-docker_services_service_configs.png" alt=""><figcaption></figcaption></figure>

### Secrets

In the context of Docker Swarm services, a secret is a blob of data such as a password, SSH private key, SSL certificate, or another piece of data that should not be transmitted over a network or stored unencrypted in a Dockerfile or in your application’s source code.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/IwTXYiYPxJubJxkpmtub/2.15-docker_services_service_secrets.png" alt=""><figcaption></figcaption></figure>


# Scale a service

From the menu select **Services** then select **scale** next to the service you want to scale (in the **Scheduling Mode** column).

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/e9Vb5aAfzNyBeQyOCQBu/Scale-a-service-new.gif" alt=""><figcaption></figcaption></figure>

Select the number of replicas you want to create for the service then click the tick icon to apply. If scaling is successful, a success message will appear at the top-right of the screen. Refresh the page until the running replicas appear.

{% hint style="info" %}
Depending on container size, there might be a slight delay before the replicas appear on screen.
{% endhint %}


# View the status of a service task

Services in a Docker Swarm environment are a collection of tasks (or individual containers). This article explains how to quickly see the status of the containers that make up each service.

From the menu select **Services** then click the down-arrow to the left of the service you want to inspect. The tasks that make up the service will be shown.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/VzWlO6juC6bhWbBdtcHZ/Service-status-new.gif" alt=""><figcaption></figcaption></figure>

Select any individual task to go to the container details page for that task. You can also perform various actions on individual tasks by using the icons in the **Actions** column.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/kGg9NqXQ59f8wFR3OMlV/2.15-docker_services_service_actions.png" alt=""><figcaption></figcaption></figure>


# View service logs

From the menu select **Services**, select the service whose logs you want to view then click **Service logs**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/b6qd6vBZ5uBkqZpyWMLM/Service-logs-new.gif" alt=""><figcaption></figcaption></figure>

Here you can see the contents of the Docker logs for your service.&#x20;

<table><thead><tr><th width="236">Field/Option</th><th>Overview</th></tr></thead><tbody><tr><td>Search</td><td>Enter a string to search the log output. You can see the number of results for your search and move through each result with the up and down arrows.</td></tr><tr><td>Filter search results</td><td>When enabled, display only the log lines that contain your search string.</td></tr><tr><td>Copy</td><td>Click this button to copy the currently displayed log lines to your clipboard.</td></tr><tr><td>Download logs</td><td>Click this button to download your log.</td></tr></tbody></table>

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/PIer3yhXY7Xz2ye32V1A/2.17-containers-logs-search.png" alt=""><figcaption></figcaption></figure>

You can also set various options for how the logs are displayed:

<table><thead><tr><th width="238">Field/Option</th><th>Overview</th></tr></thead><tbody><tr><td>Date picker</td><td>Select the time period from which to retrieve the logs.</td></tr><tr><td>Lines</td><td>Limit the number of lines per log file (the default is 1000).</td></tr><tr><td>Line numbers</td><td>When enabled, display line numbers for each log line.</td></tr><tr><td>Timestamp</td><td>When enabled, display a timestamp before each log line.</td></tr><tr><td>Wrap lines</td><td>When enabled, lines longer than the screen width will be wrapped onto the next line.</td></tr><tr><td>Auto refresh</td><td>Enable this option to automatically refresh the log view. When off, you can click the refresh icon to the right of the button to manually refresh the view.</td></tr><tr><td>Full screen</td><td>Click the full screen icon to expand the log display to fill your screen.</td></tr></tbody></table>

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/6t7VLO7eWxK5gXEpFI8A/2.30-containers-logs-options.png" alt=""><figcaption></figcaption></figure>


# Roll back a service

If you make a change to a service in Docker Swarm and your applications are no longer working as you expect, you can roll back to the previous state.

From the menu select **Services**, select the service to roll back then click **Rollback the service**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/t8vqaNyavBGqkpqanVDv/Rollback-service-new.gif" alt=""><figcaption></figcaption></figure>

When the confirmation message appears, click **Yes**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/C7ypXvQinUAIhorOqdqH/2.15-service-rollback-confirm.png" alt=""><figcaption></figcaption></figure>


# Webhooks

A webhook is a POST request sent to a URL that you define in Docker Hub or another registry. Use webhooks to trigger an action or a service in response to a repository push event.

{% hint style="info" %}
Webhooks are only available on non-Edge environments (environments running Portainer Server or Portainer Agent, not the Portainer Edge Agent). This is because the tunnel to the Portainer Edge Agent is only opened on-demand, and therefore would mean there is no way to expose a webhook permanently.
{% endhint %}

## Enabling a service webhook

From the menu select **Services** then select the service that you want to configure the webhook for.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/7knQYDjML8AYcJPYALbk/Webhook-service-new.gif" alt=""><figcaption></figcaption></figure>

In the **Service details** screen toggle the **Service webhook** option on. When the URL appears, click **Copy link**. This URL will be used to configure the webhook in your chosen registry.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/Mg2Lv0dl6c6hBl8KL26k/2.15-docker_services_service_webhook.png" alt=""><figcaption></figcaption></figure>

This example shows how to trigger the webhook using `redeploy`:

```
<form action="https://portainer:9443/api/webhooks/638e6967-ef77-4906-8af8-236800621360" method="post">
  Redeploy with latest image of same tag <input type="submit" />
</form>
```

This example shows how to trigger the webhook using `update service image with a different tag`:

```
<form action="https://portainer:9443/api/webhooks/638e6967-ef77-4906-8af8-236800621360?tag=latest" method="post">
  Update Service image with different tag <input type="submit" />
</form>
```

## Using environment variables with webhooks

When triggering a webhook, environment variables can be passed through the endpoint and referenced within services' compose files.

{% hint style="info" %}
This functionality is only available in Portainer Business Edition.
{% endhint %}

To specify an environment variable on a webhook, add it as a variable to the URL. For example, to pass a `SERVICE_TAG` variable with the value `development`:

```
https://portainer:9443/api/webhooks/1d251d96-fb34-4172-a0a1-d0655467b897?SERVICE_TAG=development
```

To reference the `SERVICE_TAG` variable in your compose file with a fallback to the value `stable`:

```
services:
  my-service:
    image: repository/image:${SERVICE_TAG:-stable}
```

## Configuring the webhook in Docker Hub

To finish the configuration, refer to [Docker's own documentation](https://docs.docker.com/docker-hub/webhooks/).


# Containers

Put simply, a container is a runnable instance of an image. Containers do not hold any persistent data and therefore can be destroyed and recreated as needed.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/FH1qkKCEBLU9oR9pms6d/2.20-containers-list.png" alt=""><figcaption></figcaption></figure>

When the [new image indicator](https://docs.portainer.io/user/host/setup#other) feature is enabled, the **Images up to date** column indicates whether the local images in the container are up to date, with a green tick indicating they are up to date and an orange cross indicating that there is a newer version of an image available at the remote registry. A grey hyphen indicates Portainer was unable to determine whether there is an update available for the images.

You can click the reload button next to the search box to recheck the images for all your containers for updates, or to recheck a single container's image you can click the image indicator icon for that container.

For more on how this works, have a look at [this FAQ article](https://docs.portainer.io/faqs/troubleshooting/stacks-deployments-and-updates/how-does-the-image-update-notification-icon-work).

To add a new container, click **Add container**.

{% content-ref url="containers/add" %}
[add](https://docs.portainer.io/user/docker/containers/add)
{% endcontent-ref %}

Once a container has been created you can inspect it, edit or duplicate it, toggle a container webhook, attach volumes, view logs and statistics, edit ownership, and access its console.

{% content-ref url="containers/view" %}
[view](https://docs.portainer.io/user/docker/containers/view)
{% endcontent-ref %}

{% content-ref url="containers/inspect" %}
[inspect](https://docs.portainer.io/user/docker/containers/inspect)
{% endcontent-ref %}

{% content-ref url="containers/edit" %}
[edit](https://docs.portainer.io/user/docker/containers/edit)
{% endcontent-ref %}

{% content-ref url="containers/advanced" %}
[advanced](https://docs.portainer.io/user/docker/containers/advanced)
{% endcontent-ref %}

{% content-ref url="containers/webhooks" %}
[webhooks](https://docs.portainer.io/user/docker/containers/webhooks)
{% endcontent-ref %}

{% content-ref url="containers/attach-volume" %}
[attach-volume](https://docs.portainer.io/user/docker/containers/attach-volume)
{% endcontent-ref %}

{% content-ref url="containers/logs" %}
[logs](https://docs.portainer.io/user/docker/containers/logs)
{% endcontent-ref %}

{% content-ref url="containers/ownership" %}
[ownership](https://docs.portainer.io/user/docker/containers/ownership)
{% endcontent-ref %}

{% content-ref url="containers/stats" %}
[stats](https://docs.portainer.io/user/docker/containers/stats)
{% endcontent-ref %}

{% content-ref url="containers/console" %}
[console](https://docs.portainer.io/user/docker/containers/console)
{% endcontent-ref %}

If you no longer need a container, you can remove it.

{% content-ref url="containers/remove" %}
[remove](https://docs.portainer.io/user/docker/containers/remove)
{% endcontent-ref %}


# Add a new container

Select **Containers** from the menu then click **Add container**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/ahFqiF8ooyJYP2kCH1SL/Add-container-new.gif" alt=""><figcaption></figcaption></figure>

Configure the container settings as required.

## Image configuration section

| Field/Option          | Overview                                                                                                                                   |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Name                  | Give the container a descriptive name.                                                                                                     |
| Registry              | Select the registry that contains the image that you want to use for your container.                                                       |
| Image                 | Enter the name of the image you want to use.                                                                                               |
| Always pull the image | Toggle on to enforce pulling the image from the registry instead of using the locally cached copy (if you have used the image previously). |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/aahewL9EdmZQ77Wqs1bd/2.15-docker_containers_image_config.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
When using Docker Hub you can use the **Search** button to search for the image you have entered, and ensure that you have the correct name and tag. Portainer also displays the number of pulls remaining for your Docker Hub account when using an anonymous account.
{% endhint %}

Alternatively you can switch to advanced mode to manually enter registry and image details. This is useful if you want to do a one-off container deployment from a registry that isn't configured within Portainer.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/tUL7m9duT3e1ukpa5YaY/2.15-docker_containers_image_config_simple.png" alt=""><figcaption></figcaption></figure>

## Webhooks

Toggle **Create a container webhook** on to create a [webhook](https://docs.portainer.io/user/docker/containers/webhooks) for the container. You can send a POST request to this endpoint to automate pulling the most up-to-date image and re-deploy your container.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/4a4avKlaSoLG9JfKarxv/2.15-docker_container_webhook.png" alt=""><figcaption></figcaption></figure>

## Network ports configuration section

| Field/Option                                           | Overview                                                                                                 |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| Publish all exposed network ports to random host ports | Toggle on to allow Portainer to randomly assign ports on the host to the exposed ports in the container. |
| Manual network port publishing                         | Click **publish a new network port** to create manual port mappings for the container.                   |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/oQnPFSout2czDcSPRlb3/2.15-docker_container_network_port_config.png" alt=""><figcaption></figcaption></figure>

## Actions section

| Field/Option | Overview                                                                                                                            |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| Auto remove  | Toggle this option on to automatically remove the container once it exits. This is useful if you want to run a container only once. |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/PzbMhqdeNQ1h7CpTYzTW/2.15-docker_container_actions.png" alt=""><figcaption></figcaption></figure>

Once complete, set any advanced options (see below) then click **Deploy the container.** If successful your container will be shown in the container list.

## Advanced container settings

Choose from a [range of options](https://docs.portainer.io/user/docker/containers/advanced) to customize the deployment.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/ST78PdY1O1c3eEsm7whF/2.15-containers-advanced.png" alt=""><figcaption></figcaption></figure>


# View a container's details

From the menu select **Containers**, then select the container you want to view.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/CGk1F9rfGIqsKqLFvsiP/Container-details-new.gif" alt=""><figcaption></figcaption></figure>

Here you can view the container's status and details, including port configurations, environment variables, labels, attached volumes and networks, and more. You also have a number of actions available, including starting, stopping and removing the container.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/QauUuz3tvLnKfT1eMGwc/2.15-docker_containers_details_actions.png" alt=""><figcaption></figcaption></figure>

You can also toggle the container [webhook](https://docs.portainer.io/user/docker/containers/webhooks), view the [container logs](https://docs.portainer.io/user/docker/containers/logs), [inspect](https://docs.portainer.io/user/docker/containers/inspect) the container's configuration, view container [stats](https://docs.portainer.io/user/docker/containers/stats), access the [console](https://docs.portainer.io/user/docker/containers/console), and (if the container is running in interactive mode) attach to the running container.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/bSHIYJZZpTh0d4LKrUuy/2.15-docker_containers_container_status.png" alt=""><figcaption></figcaption></figure>

You can create an image from a deployed container to use when creating other containers.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/lHM7GfF5dil67JEygu2O/2.15-docker_containers_container_create_image.png" alt=""><figcaption></figcaption></figure>


# Inspect a container

View information about any container, such as network settings, volumes and images.

From the menu select **Containers**, select the container then select **Inspect**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/2oOCn8y3rRspEcUOL3Nm/Inspect-container-new.gif" alt=""><figcaption></figcaption></figure>

All of the information about the container will display in a tree view. Select any parameter to show more details (if available).

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/9rPqsnXYkf8ozIlbFPfc/2.15-docker_containers_container_inspect.png" alt=""><figcaption></figcaption></figure>

You can also inspect the container in a raw JSON format by clicking **Text**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/0nVF5UrrNSUc0xSmefFg/2.15-docker_containers_container_inspect_text.png" alt=""><figcaption></figcaption></figure>


# Edit or duplicate a container

{% hint style="warning" %}
Editing a container effectively creates a new container with the updated settings and replaces the old container.
{% endhint %}

## Editing a running container

From the menu select **Containers**, select the container you want to edit then click **Duplicate/Edit**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/Fiox1VcQk3XAgpqD2fPi/duplicate-container.gif" alt=""><figcaption></figcaption></figure>

Make the required changes to the container configuration. When you're finished, click **Deploy the container**. When the confirmation message appears, click **Replace**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/PNcWAKjVcQJfFcPI2LGU/2.15-container-edit-confirm.png" alt=""><figcaption></figcaption></figure>

If successful, a message will appear confirming that a new container has been created with the new settings, replacing the old container.

## Duplicating a running container

From the menu select **Containers**, select the container you want to duplicate then click **Duplicate/Edit**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/Fiox1VcQk3XAgpqD2fPi/duplicate-container.gif" alt=""><figcaption></figcaption></figure>

Make the required changes to the container configuration, making sure you enter a new container name in order to create a duplicate. When you're finished, click **Deploy the container**.


# Advanced container settings

When creating or editing a container you can configure a number of additional settings in the **Advanced container settings** section.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/ST78PdY1O1c3eEsm7whF/2.15-containers-advanced.png" alt=""><figcaption></figcaption></figure>

## Command & logging

In this section you can configure the command that runs when the container starts as well as configure logging for the container.

| Field/Option | Overview                                                                                                                                                                                                        |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Command      | Set the command that is run when the container starts. Select `Default` to use the default command provided by the container's image, or select `Override` and provide a command to override the default value. |
| Entrypoint   | Set the entrypoint for the container. Select `Default` to use the default entrypoint provided by the container's image, or select `Override` and provide an entrypoint to override the default value.           |
| Working Dir  | Set the working directory your container should start in (within the container's filesystem).                                                                                                                   |
| User         | Specify the user that the container's command should run as.                                                                                                                                                    |
| Console      | Set the console configuration for your container.                                                                                                                                                               |
| Driver       | Select the logging driver to use for your container. Available options will depend on the logging drivers configured on your Docker host.                                                                       |
| Options      | Set additional options for your logging driver. To add a new option click **add logging driver option** and configure accordingly.                                                                              |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/E7t8eXCp1r14jZD8I12O/2.15-containers-advanced-command.png" alt=""><figcaption></figcaption></figure>

## Volumes

Here you can configure volume mappings for your container. You can map to [existing named volumes](https://docs.portainer.io/user/docker/volumes) or bind mount to locations on your Docker host.

| Field/Option         | Overview                                                                                                                                                            |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Container path       | Specify where you want to make the volume or bind mount available within the container's filesystem.                                                                |
| Mapping type         | Select `Volume` to map a named volume, or select `Bind` to map a bind mount.                                                                                        |
| Volume               | If using the `Volume` mapping type, select the named volume to mount from the dropdown.                                                                             |
| Host path            | If using the `Bind` mapping type, specify the path on the Docker host you want to bind mount in the container.                                                      |
| Writable / Read-only | Select `Writable` if you want the container to be able to write to the mapping. Select `Read-only` if the container should **not** be able to write to the mapping. |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/UtD0mfSas9kb6AfJIDnJ/2.15-containers-advanced-volumes.png" alt=""><figcaption></figcaption></figure>

## Network

In this section you can configure the network settings for the container.&#x20;

{% hint style="warning" %}
Note that you cannot assign a static IP address to a container that is in Docker's default `bridge` network. This is a Docker limitation rather than Portainer. If you need to specify the IP for your container then you will need to [create a custom network](https://docs.portainer.io/user/docker/networks/add) and assign the container to it.
{% endhint %}

| Field/Option         | Overview                                                                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Network              | Select the [network](https://docs.portainer.io/user/docker/networks) to attach the container to from the dropdown.                                                              |
| Hostname             | Specify the hostname for the container.                                                                                                                                         |
| Domain Name          | Specify the domain name for the container.                                                                                                                                      |
| Mac Address          | Specify the MAC address to set on the container.                                                                                                                                |
| IPv4 Address         | Specify the IPv4 address to use for the container. This must be within the range for the chosen network and should not be already assigned to a container.                      |
| IPv6 Address         | Specify the IPv6 address to use for the container. This must be within the range for the chosen network and should not be already assigned to a container.                      |
| Primary DNS Server   | Specify the primary DNS server to use within the container.                                                                                                                     |
| Secondary DNS Server | Specify the secondary DNS server to use within the container.                                                                                                                   |
| Hosts file entries   | Click **add additional entry** to add a new host file entry for the container. Host file values should be formatted as `hostname:address` (for example `database:192.168.1.1`). |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/90Z5U6b6BCeA5W8yW30g/2.15-containers-advanced-network.png" alt=""><figcaption></figcaption></figure>

## Environment Variables

Use this section to add or edit environment variables made available in the container. Click **Add an environment variable** to create a new variable, or edit an existing variable with the fields provided. You can also click **Load variables from .env file** to import an existing .env file with your variables. To remove a variable, click the trash can icon to the right of the variable to remove.

| Field/Option | Overview                                    |
| ------------ | ------------------------------------------- |
| Name         | Set the name for the environment variable.  |
| Value        | Set the value for the environment variable. |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/VmMiBnMqiNeYNXl9LogZ/2.15-containers-advanced-env.png" alt=""><figcaption></figcaption></figure>

If you want to add multiple variables at once, click on **Advanced mode** to switch to an editor view where you can paste a block of variables and values.

## Labels

You can set labels on your container using this section. Click add label to add a new label, or edit an existing label using the fields provided. To remove a label, click the trash can icon to the right of the label to remove.

| Field/Option | Overview                     |
| ------------ | ---------------------------- |
| Name         | Set the name for the label.  |
| Value        | Set the value for the label. |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/lGsm3vmGI3C2hRsvDNDs/2.15-containers-advanced-labels.png" alt=""><figcaption></figcaption></figure>

## Restart policy

Use this section to configure the restart policy for your container. Possible options are:

* **Never**: Do not automatically restart the container when it exits. This is the default.
* **Always**: Always restart the container regardless of the exit status. When you specify always, Docker will try to restart the container indefinitely. The container will also always start on Docker startup, regardless of the current state of the container.
* **On failure**: Restart only if the container exits with a non-zero exit status.
* **Unless stopped**: Always restart the container regardless of the exit status, including on Docker startup, except if the container was put into a stopped state before Docker was stopped.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/GQcYGZTiNiaQRyUpdUkS/2.15-containers-advanced-restart.png" alt=""><figcaption></figcaption></figure>

## Runtime & Resources

This section lets you configure runtime options for your container, add or configure GPUs for use within the container, and specify resource limitations on the container.

### Runtime

Here you can configure runtime options for the container.

| Field/Option       | Overview                                                                                                                                                                                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Privileged mode    | Enable this option to run the container in [privileged mode](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities).                                                                                                              |
| Init               | Enable this option to tell Docker that an init process should be used as PID 1 in the container.                                                                                                                                                                   |
| Type               | Select the runtime type to use to start the container. Options will depend on available runtimes on your Docker host.                                                                                                                                              |
| Devices            | Use this option to make devices on your Docker host available within the container. Click **add device** to add a new device, and define the **host** path for the device and the **container** path for where you want the device to appear within the container. |
| Sysctls            | Use this option to specify sysctls to make available within the container. Click **add sysctl** to add a new sysctl, and set the **name** and **value** for your sysctl as required.                                                                               |
| Shared memory size | Specify the size (in MB) of the shared memory device (`/dev/shm`) for the container.                                                                                                                                                                               |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/dJmv8SLdppomQTQLJExT/2.20-containers-advanced-runtime.png" alt=""><figcaption></figcaption></figure>

### GPU

Here you can enable GPU access for the container and configure the GPU settings as required.

{% hint style="info" %}
GPU support is currently only available on Docker Standalone environments, and only supports NVIDIA GPUs.
{% endhint %}

| Field/Option | Overview                                                                                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enable GPU   | Toggle this option on to enable GPU access for the container.                                                                                                       |
| GPU selector | Select the GPU(s) to make available to the container, or choose `Use All GPUs` to provide access to all the GPUs on the Docker host.                                |
| Capabilities | Select the capabilities you want to use with the container. Portainer preselects `compute` and `utility` as they are the defaults when not specifying capabilities. |
| Control      | View a generated equivalent of the Docker CLI's `--gpus` option based on your selections above.                                                                     |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/AgjRUHawNh7CUZaVfxsG/2.20-containers-advanced-gpu.png" alt=""><figcaption></figcaption></figure>

### Resources

Here you can configure resource limits for your container. You can use the sliders to set the value or enter a value in the fields.

| Field/Option            | Overview                                                                                                                                                      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Memory reservation (MB) | Specify the amount of memory (in MB) to reserve for the container.                                                                                            |
| Memory limit (MB)       | Specify the maximum amount of memory (in MB) the container is allowed to use.                                                                                 |
| Maximum CPU usage       | Specify the maximum amount of CPU the container is allowed to use. This is specified based on the number of processing threads available on your Docker host. |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/R9IcuBpTcnpgdCWBbKdm/2.15-containers-advanced-resources.png" alt=""><figcaption></figcaption></figure>

## Capabilities

In this section you can configure the individual capabilities for your container. For more information refer to the [Docker documentation](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities).

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/gDPFUMVLhctdLplDc9Gu/2.15-containers-advanced-capabilities.png" alt=""><figcaption></figcaption></figure>


# Webhooks

A webhook is a POST request sent to a URL that you define in Docker Hub or another registry. Use webhooks to trigger an action in response to an event such as a repository push.

{% hint style="info" %}
This functionality is only available in [Portainer Business Edition](https://www.portainer.io/business-upsell?from=container-webhook).
{% endhint %}

{% hint style="info" %}
Webhooks are only available on non-Edge environments (environments running Portainer Server or Portainer Agent, not the Portainer Edge Agent). This is because the tunnel to the Portainer Edge Agent is only opened on-demand, and therefore would mean there is no way to expose a webhook permanently.
{% endhint %}

## Enabling a container webhook

From the menu select **Containers** then select the container that you want to configure the webhook for.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/nufBlEbvfT3bGweGMf3b/Container-webhook-new.gif" alt=""><figcaption></figcaption></figure>

In the **Container details** screen toggle the **Container webhook** option on. When the URL appears, click **Copy link**. This URL will be used to configure the webhook in your chosen registry.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/i4xA0SpiuRmBEWhOmUoo/2.15-docker_containers_container_webhook.png" alt=""><figcaption></figcaption></figure>

This example shows how to trigger the webhook using `redeploy`:

```
<form action="https://portainer:9443/api/webhooks/638e6967-ef77-4906-8af8-236800621360" method="post">
  Redeploy with latest image of same tag <input type="submit" />
</form>
```

This example shows how to trigger the webhook to update the container to use a different image tag:

```
<form action="https://portainer:9443/api/webhooks/638e6967-ef77-4906-8af8-236800621360?tag=latest" method="post">
  Update container image with different tag <input type="submit" />
</form>
```

## Configuring the webhook in Docker Hub

To finish the configuration, refer to [Docker's own documentation](https://docs.docker.com/docker-hub/webhooks/).


# Attach a volume to a container

{% hint style="danger" %}
This article explains how to attach a new [volume](https://docs.portainer.io/user/docker/volumes) to a running container. This operation destroys the running container and starts a new one with the volume attached.

**Always back up your data before running this operation.**
{% endhint %}

From the menu select **Containers**, select the container that you want to attach a volume to, then click **Duplicate/Edit**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/Fiox1VcQk3XAgpqD2fPi/duplicate-container.gif" alt=""><figcaption></figcaption></figure>

Scroll down to **Advanced container settings**. Click **Volumes** then click **map additional volume**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/gF23qomNVcMaBMnqREAc/2.15-docker_containers_container_add_volumes.png" alt=""><figcaption></figcaption></figure>

In the **container** field enter the path. In the **volume** field enter the volume to attach to the container.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/J6gBvWsLsbqwugbbnhZR/2.15-docker_containers_container_adv_volume_mapping.png" alt=""><figcaption></figcaption></figure>

When you're ready, click **Deploy the container**. When the confirmation message appears, click **Replace**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/PNcWAKjVcQJfFcPI2LGU/2.15-container-edit-confirm.png" alt=""><figcaption></figcaption></figure>


# View container logs

From the menu select **Containers**, select the container then select **Logs**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/53Z8yQB5wgRXHbTyr7Zw/Container-logs-new.gif" alt=""><figcaption></figcaption></figure>

Here you can see the contents of the Docker logs for your container.&#x20;

<table><thead><tr><th width="241">Field/Option</th><th>Overview</th></tr></thead><tbody><tr><td>Search</td><td>Enter a string to search the log output. You can see the number of results for your search and move through each result with the up and down arrows.</td></tr><tr><td>Filter search results</td><td>When enabled, display only the log lines that contain your search string.</td></tr><tr><td>Copy</td><td>Click this button to copy the currently displayed log lines to your clipboard.</td></tr><tr><td>Download logs</td><td>Click this button to download your log.</td></tr></tbody></table>

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/PIer3yhXY7Xz2ye32V1A/2.17-containers-logs-search.png" alt=""><figcaption></figcaption></figure>

You can also set various options for how the logs are displayed:

<table><thead><tr><th width="244">Field/Option</th><th>Overview</th></tr></thead><tbody><tr><td>Date picker</td><td>Select the time period from which to retrieve the logs.</td></tr><tr><td>Lines</td><td>Limit the number of lines per log file (the default is 1000).</td></tr><tr><td>Line numbers</td><td>When enabled, display line numbers for each log line.</td></tr><tr><td>Timestamp</td><td>When enabled, display a timestamp before each log line.</td></tr><tr><td>Wrap lines</td><td>When enabled, lines longer than the screen width will be wrapped onto the next line.</td></tr><tr><td>Auto refresh</td><td>Enable this option to automatically refresh the log view. When off, you can click the refresh icon to the right of the button to manually refresh the view.</td></tr><tr><td>Full screen</td><td>Click the full screen icon to expand the log display to fill your screen.</td></tr></tbody></table>

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/6t7VLO7eWxK5gXEpFI8A/2.30-containers-logs-options.png" alt=""><figcaption></figcaption></figure>


# View container statistics

From the menu select **Containers**, select the container then select **Stats**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/QI1lbeXjcNcFDdR5EEBB/Container-stats-new.gif" alt=""><figcaption></figcaption></figure>

The information available includes:

* Memory usage.
* CPU usage.
* Network usage (RX and TX).
* I/O usage.
* Processes running in the container

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/bPY6mcgUOSLWJJ1Ld5Vh/2.15-docker_containers_container_stats_usage.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/PliwSpgb9GjIF35H0TtO/2.15-docker_containers_container-stats-proc.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
You can change the refresh rate at any time.
{% endhint %}


# Access a container's console

From the menu select **Containers**, select the container then select **Console**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/ydk0cLR2M3CnFR0zxTAr/Container-console-new.gif" alt=""><figcaption></figcaption></figure>

Select the command and the user you want to give access to, then click **Connect**.

{% hint style="info" %}
For Alpine Linux containers, you must select the`/bin/ash` command.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/Wu9tG73ZOXe10tfuNov7/2.15-docker_containers_container_console_execute.png" alt=""><figcaption></figcaption></figure>

If you need to define a command other than those provided, toggle the **Use custom command** option on. Once connected, you can run commands in the console the same as any other Linux system.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/ZisBQ0gnHCvfgASZzqNG/2.20-containers-console-connected.png" alt=""><figcaption></figcaption></figure>

To disconnect from the console session, click the **Disconnect** button.


# Change container ownership

Portainer allows you to limit container management to specific teams or users.

From the menu select **Containers** then select the container whose ownership you want to change.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/h36vzbAMEpXlvNaz8DTe/Container-change-ownership.gif" alt=""><figcaption></figcaption></figure>

Under the **Access control** section tick the **Change ownership** checkbox then select the new ownership type, using the table below as a guide.

| Ownership Type | Overview                                                                                                                                |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Administrators | Only Portainer administrators can manage the container.                                                                                 |
| Restricted     | Only teams or users you specify can manage the container.                                                                               |
| Public         | Anyone who has [access to the environment](https://docs.portainer.io/user/docker/containers/broken-reference) can manage the container. |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/5h0Zm4WMylPG537QuneC/2.15-docker_containers_container_access_control.png" alt=""><figcaption></figcaption></figure>

When you've made your selection, click **Update ownership**. When the confirmation message appears, click **Change ownership**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/K7hkzzDAICQpipNsgODq/2.15-container-ownership-confirm.png" alt=""><figcaption></figcaption></figure>


# Remove a container

From the menu select **Containers**, tick the checkbox next to the container you want to remove then click **Remove**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/In7FuTQR3k17fBDjlXzu/2.38-new-remove-container.gif" alt=""><figcaption></figcaption></figure>

When the confirmation message appears, opt whether or not to automatically remove non-persistent volumes then click **Remove**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/DtFrLBz5U2EL4bL5rmpP/2.15-container-remove-confirm.png" alt=""><figcaption></figcaption></figure>


# Images

Images are what is used to build containers. Each image defines the pieces required to build and configure a container and can be reused many times. The **Images** section in Portainer lets you interact with the images in an environment.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/XzMDpPp0FBidmVMGc5fC/2.15-images-splash.png" alt=""><figcaption></figcaption></figure>

You can pull images from Docker Hub or any other [registry](https://docs.portainer.io/admin/registries/add):

{% content-ref url="images/pull" %}
[pull](https://docs.portainer.io/user/docker/images/pull)
{% endcontent-ref %}

You can also view a list of the images that are currently available in an environment, including their IDs, usage states, tags, sizes and creation dates. There are many other options available:

{% content-ref url="images/build" %}
[build](https://docs.portainer.io/user/docker/images/build)
{% endcontent-ref %}

{% content-ref url="images/import" %}
[import](https://docs.portainer.io/user/docker/images/import)
{% endcontent-ref %}

{% content-ref url="images/export" %}
[export](https://docs.portainer.io/user/docker/images/export)
{% endcontent-ref %}


# Pull an image

You can pull images from any registry that has been [added to Portainer](https://docs.portainer.io/admin/registries), or using advanced mode, from a custom external registry.

{% hint style="info" %}
On a multi-node environment, the pulled image will only be available on the node you select in the **Deployment** section. To make the image available to all nodes, consider [adding a registry](https://docs.portainer.io/admin/registries/add) to Portainer.
{% endhint %}

## Method 1: Pulling images in simple mode

This method lets you pull images from Docker Hub or from another registry that you have connected with before.

From the menu select **Images**. Select the registry to use then enter the name of the image. On a multi-node environment, select the node to deploy to.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/UlY1EbU8WUCye241M7g2/2.15-docker_images_pull_images.png" alt=""><figcaption></figcaption></figure>

When you're ready, click **Pull the image**.

## Method 2: Pulling images in advanced mode

Using advanced mode, you can define a custom registry URL, port and image. This is ideal if you run your own private registry but don't want to add it to the [registries](https://docs.portainer.io/admin/registries) list in Portainer.

From the menu select **Images** then select **Advanced mode**. Next, enter the registry, port and image in the **Image** box. On a multi-node environment, select the node to deploy to.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/osUhYco6SC53yYSxyUAh/2.15-docker_images_pull_image_simple.png" alt=""><figcaption></figcaption></figure>

When you're ready, click **Pull the image**.


# Build a new image

There are three ways you can build new images.

{% hint style="info" %}
On a multi-node environment, the built image will only be available on the node you select in the **Deployment** section. To make the image available to all nodes, consider [adding a registry](https://docs.portainer.io/admin/registries/add) to Portainer.
{% endhint %}

{% hint style="warning" %}
When building an image with Portainer, you are unable to use `ADD` or `COPY` commands referencing files on the host. We recommend using `wget` or similar to retrieve files from a HTTP/S URL instead.
{% endhint %}

## Method 1: Using the Portainer web editor

From the menu select **Images** then click **Build a new image**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/Nr5RK534hB8TMUpZnSDC/Build-new-image.gif" alt=""><figcaption></figcaption></figure>

Next, give the image a descriptive name (you can enter multiple names), select the **Web editor** option under **Build method**, then write your Dockerfile in the web editor.

{% hint style="info" %}
You can search within the web editor at any time by pressing `Ctrl-F` (or `Cmd-F` on Mac).
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/FfKHrQ1uJyjLfLCW01mM/2.15-docker_images_build_web_editor.png" alt=""><figcaption></figcaption></figure>

Optionally, you can upload one or more local files to be included in an image by clicking **Select files** and selecting the files to include. You can then reference them in your Dockerfile.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/NA4Pe3p6SCq07brE1JNv/2.16-images-build-upload.png" alt=""><figcaption></figcaption></figure>

Select the node you want to save the image on (if on a multi-node environment) then click **Build the image**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/g1Rhn2OoG7PTghZCPZhq/2.15-docker_images_build_deployment.png" alt=""><figcaption></figcaption></figure>

When the build is finished, select the **Output** tab to view the build history and the result.

## Method 2: Uploading a Dockerfile

If you have an existing Dockerfile, you can upload it to Portainer and use it to build the image.

From the menu select **Images** then click **Build a new image**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/un6IYZjxlqCQ0YghPAYJ/Build-new-image-upload.gif" alt=""><figcaption></figcaption></figure>

Next, give the image a descriptive name (you can enter multiple names), select the **Upload** option under **Build method**, then browse to and upload the Dockerfile.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/EkMNSpZXBV1JnxJ7HUIG/2.15-docker_images_build_upload.png" alt=""><figcaption></figcaption></figure>

Scroll down and select the node you want to save the image on (if on a multi-node environment) then click **Build the image**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/g1Rhn2OoG7PTghZCPZhq/2.15-docker_images_build_deployment.png" alt=""><figcaption></figcaption></figure>

When the build is finished, select the **Output** tab to view the build history and the result.

## Method 3: Providing a Dockerfile from a URL

If the Dockerfile is hosted on the Internet (either in a tarball or a public GitHub repository), you can download it directly to Portainer via its URL.

From the menu select **Images** then click **Build a new image**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/CTpMz2S3Z2seeoSsuBW9/Build-new-image-url.gif" alt=""><figcaption></figcaption></figure>

Next, give the image a descriptive name (you can enter multiple names), select the **Upload** option under **Build method**, then enter the **URL** of the file and the **Dockerfile path** within the tarball or repository.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/bessP9grUuNcseAwz7iY/2.15-docker_images_build_URL.png" alt=""><figcaption></figcaption></figure>

Scroll down and select the node you want to save the image on (if on a multi-node environment) click **Build the image**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/g1Rhn2OoG7PTghZCPZhq/2.15-docker_images_build_deployment.png" alt=""><figcaption></figcaption></figure>

When the build is finished, select the **Output** tab to view the build history and the result.


# Import an image

You can import images from other Portainer instances, the Docker CLI or the Docker Swarm CLI.

From the menu select **Images** then click **Import**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/Hy16gjUy6i3gbJNg49vM/Import-image.gif" alt=""><figcaption></figcaption></figure>

Click **Select file** to browse for the image file to upload. Portainer supports `.tar`, `.tar.gz`, `.tar.bz2` and `.tar.xz` files. If you are on a multi-node environment, select the node where you wish to save the image.

{% hint style="info" %}
On a multi-node environment, the image you import will only be available on the node selected under **Deployment**. If you want to make the image available to all nodes, consider [adding a registry](https://docs.portainer.io/admin/registries/add) to Portainer.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/A1u2MMzuz45DOhYXd5i2/2.15-docker_images_upload_file.png" alt=""><figcaption></figcaption></figure>

When importing an image you can also select to tag the image using a registry you have preconfigured in Portainer. Select the **Registry** from the dropdown and enter the image name and tag.&#x20;

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/bVzd7jPCWLRINFtMD1bq/2.15-docker_images_upload_file_tag_image.png" alt=""><figcaption></figcaption></figure>

If you wish to tag the image with a registry that is not configured within Portainer, click **Advanced mode** and enter the registry, port, image and tag as required.

{% hint style="info" %}
If you want to tag the image locally rather than in a registry, use **Advanced mode** and simply specify the image name and tag, without a registry.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/LdTkPwlWmHvnvk2uuSLs/2.15-docker_images_import_simple.png" alt=""><figcaption></figcaption></figure>

When you're ready, click **Upload** to import your image.


# Export an image

You can export any Docker image stored on any node. This is useful when you need to move a container from one host to another, or simply make a backup of the images.

{% hint style="warning" %}
If you export a container to a tar file, the volumes won't get exported with it. You will need to save the data from those volumes using a different method.
{% endhint %}

From the menu select **Images**, select the image you want to export then click **Export this image**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/N2GmJQxzkqBA6OWIGEQS/Export-image-1.gif" alt=""><figcaption></figcaption></figure>

When the warning message appears, click **Continue**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/l2AXaqt7afdRJ2Pkt6d9/2.15-images-export-confirm.png" alt=""><figcaption></figcaption></figure>

When the image has downloaded, a success message will appear, and your browser should automatically download the resulting tar file.<br>


# Networks

Portainer lets you add, remove and manage networks in your environment.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/L8MbM5PKiESB15iDmPqt/2.20-networks-list.png" alt=""><figcaption></figcaption></figure>

{% content-ref url="networks/add" %}
[add](https://docs.portainer.io/user/docker/networks/add)
{% endcontent-ref %}

{% content-ref url="networks/remove" %}
[remove](https://docs.portainer.io/user/docker/networks/remove)
{% endcontent-ref %}

## Supported network types

Portainer supports these types of networks:

### bridge

If you don’t specify a driver, this type of network will be created by default. Bridge networks are normally used when your applications run in standalone containers that need to communicate with each other.

### macvlan

macvlan networks allow you to assign a MAC address to a container, making it appear as a physical device on your network. The Docker daemon routes traffic to containers based on their MAC addresses. Using the macvlan driver is sometimes the best choice when dealing with legacy applications that expect to be directly connected to the physical network, rather than routed through the Docker host’s network stack.

### ipvlan

Similar to macvlan, the key difference being that the endpoints have the same MAC address. ipvlan supports L2 and L3 modes. In ipvlan L2 mode, each endpoint gets the same MAC address but different IP addresses. In ipvlan L3 mode, packets are routed between endpoints, giving better scalability.

### overlay

overlay networks connect multiple Docker daemons together and enable swarm services to communicate with each other. You can also use overlay networks to facilitate communication between a swarm service and a standalone container, or between two standalone containers on different Docker daemons.


# Add a new network

From the menu select **Networks** then click **Add network**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/1YnhG7k7wfeBZKVHhBlm/Add-networks.gif" alt=""><figcaption></figcaption></figure>

Define the new network, using the table below as a guide.

| Field/Option                       | Overview                                                                                                                                                                                                                                                  |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                               | Give the network a descriptive name.                                                                                                                                                                                                                      |
| Driver                             | Define the [type of network](https://docs.portainer.io/user/docker/networks/..#supported-network-types) you will use.                                                                                                                                     |
| Driver options                     | Set in place any options related to your network driver, if required.                                                                                                                                                                                     |
| IPv4 Network configuration         | <p>Define IPv4 range, subnet, gateway and exclude IP. If no information is entered here, Docker will automatically assign an IPv4 range.<br>If you need to exclude IPs from the range, click <strong>Add excluded IP</strong> and complete the field.</p> |
| IPv6 Network configuration         | <p>Define IPv6 range, subnet, gateway and exclude IP. If no information is entered here, Docker will automatically assign an IPv6 range.<br>If you need to exclude IPs from the range, click <strong>Add excluded IP</strong> and complete the field.</p> |
| Labels                             | Click **Add label** and complete the name and value fields to specify a label for the network.                                                                                                                                                            |
| Isolated network                   | Toggle this option on to isolate any containers created in this network to this network only, with no inbound or outbound connectivity.                                                                                                                   |
| Enable manual container attachment | Toggle this option on to allow users to attach the network to running containers.                                                                                                                                                                         |
| Deployment                         | On multi-node clusters, select the node where the network will be created.                                                                                                                                                                                |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/FLFlVm1EoYAvchXVqMZM/2.20-networks-add-details.png" alt=""><figcaption></figcaption></figure>

When you're finished, click **Create the network**.




---

[Next Page](/llms-full.txt/1)

