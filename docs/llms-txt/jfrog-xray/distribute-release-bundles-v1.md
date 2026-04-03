# Source: https://docs.jfrog.com/artifactory/docs/distribute-release-bundles-v1.md

# Distribute Release Bundles (v1)

<Callout icon="📘" theme="info">
  **Subscription Information**

  This feature is supported with the **Enterprise+** license.
</Callout>

<Callout icon="❗️" theme="error">
  **Important**

  This section describes how to distribute Release Bundles v1. For information about distributing Release Bundles v2, which were introduced in Artifactory 7.63.2 and Distribution 2.19.1, see <Anchor label="Distribute Release Bundles (v2)" target="_blank" href="/governance/docs/distribute-release-bundles-v2">Distribute Release Bundles (v2)</Anchor>.
</Callout>

Release Bundles group together the contents that are part of your release, providing the bill of materials for your software releases. For example, you can group together the different build artifacts, such as Docker images, that make up your software release and push them to your point-of-sale devices.

A Release Bundle plays a central role in the distribution flow. It specifies the different files and packages that comprise a release, along with their metadata, and is created and managed in [JFrog Distribution](/docs/jfrog-distribution). Release Bundles are generally distributed from a source Artifactory instance to an Artifactory Edge node.

Since all the files specified in a Release Bundle are required to keep the release coherent, a Release Bundle must be immutable. Effectively, this means that once a file has been included in a Release Bundle, the file cannot be deleted from the target JPD (but can be removed from the source JPD).

In the JFrog Platform UI, Release Bundles are managed using the **Application** module, under **Distribution > Release Bundles**, as follows:

* **Source Artifactory:** Includes two dedicated tabs:

  * **Distributable**: Users with the appropriate permissions can create, distribute, and track release bundles.
  * **Received**: Contains the release bundles received by an Artifactory Edge

* **Artifactory Edge:** Displays a single tab displaying containing Release Bundles received by the Artifactory Edge.

### Comprehensive Tracking of Your Release Bundle Versions

All the information regarding your Release Bundle version is consolidated and displayed in one central area. This view is intuitive and provides quick access to all aspects of your Release Bundle, including Distribution Tracking, Xray data, and Effective Permissions.

### Secure and Protected Release Bundles

JFrog Xray supports indexing and scanning of Release Bundles as well as defining Watches and Policies on Release Bundles. You can apply a policy on a Watch containing a Block Release Bundle Distribution action to prevent distributing a Release Bundle to edge nodes if it meets a security or License policy defined in JFrog Xray. For more information, see Xray Scanning of Release Bundles.