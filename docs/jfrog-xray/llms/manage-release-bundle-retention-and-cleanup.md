# Source: https://docs.jfrog.com/artifactory/docs/manage-release-bundle-retention-and-cleanup.md

# Manage Release Bundle Retention and Cleanup

<Callout icon="📘" theme="info">
  **Subscription Information**

  This feature is supported with the **Enterprise+** license.
</Callout>

As customers adopt and scale with JFrog Distribution and Distribution Edge nodes, managing the lifecycle and number of Release Bundles has become challenging. To help admins manage Release Bundles (v1 & v2) and clean up older items, JFrog has created an automated cleanup process for received Release Bundles, which enables deleting **target Release Bundles** that were distributed to a specific Artifactory Edge instance. These retention policies are set up using the [RETENTION (Release Bundle v1)](/reference/getretentionpolicyconfiguration) REST APIs, and can be customized as needed.

In addition to automated retention and cleanup using REST APIs, JFrog also developed a new UI functionality that enables you to manage these Release Bundles in the JFrog Platform. See [Manage Release Bundle Retention Policies in the JFrog Platform UI](/docs/manage-release-bundles-in-the-jfrog-platform-ui).

The Release Bundle retention policies also enable you to configure a policy to keep a Release Bundle (i.e., keep the Release Bundle indefinitely, which prevents it from being deleted), not to keep it (set the item to Don’t Keep so that it is eligible for deletion), and to delete Release Bundles received by the Artifactory Edge.

The implementation of this feature provides the following enhancements:

* Saves storage
* Removes redundant releases
* Enable distribution of releases that holds different artifacts under the same path (e.g., Docker pages with latest tags)
* Security - makes sure that distributed artifacts are certified again (by requiring redistribution of old bundles)

### Prerequisites

Setting retention policies, and using the Cleanup Report (and Cleanup History function) require an admin-level user. In addition, the functionality must be enabled by setting the [Set Retention Policies to Enabled](/administration/reference/setRetentionPoliciesToEnabled) REST API to **true**.