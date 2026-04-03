# Source: https://docs.jfrog.com/artifactory/docs/jfrog-distribution.md

# JFrog Distribution

<Callout icon="📘" theme="info">
  **Subscription Information**

  This feature is supported with the **Enterprise+** license.
</Callout>

JFrog Distribution is a centralized platform that lets you provision software release distribution. It is a core part of JFrog Enterprise+, managing Release Bundles and their distribution processes, including release content, permission levels, and target destinations.

Distribution provides a secure and structured platform to distribute release binaries to multiple remote locations and update them as new release versions are produced. As part of the release flow, Release Bundles are verified by the target destination to ensure that they are signed correctly and safe to use.

JFrog Distribution securely manages the distribution of your software releases offering the following benefits:

* A **structured platform** to distribute release binaries as a single coherent release bundle.
* Support for [**Hybrid Deployment**](/docs/hybrid-deployment) ,allowing you to distribute your Release Bundles from the JFrog Platform on the Cloud to multiple Cloud and Self-hosted Edge nodes within the same organization, and from JFrog Self-Hosted to additional JFrog Artifactory instances in the cloud.

  * Hybrid Distribution to Artifactory Edge allows JFrog Cloud customers to distribute Release Bundles to both cloud and self-hosted Edge locations within the same organization. External distribution via hybrid edge nodes requires purchasing one Edge node per one 3rd party.
* Secure delivery and distribution through **signed** Release Bundles.
* **Auditing and traceability** by tracking all changes associated with a Release Bundle.
* **[Secure and protected Release Bundles](/docs/distribute-release-bundles-v1)**: JFrog Xray supports indexing and scanning of Release Bundles as well as defining Watches and Policies on Release Bundles. You can apply a policy on a Watch containing a Block Release Bundle Distribution action to prevent distributing a Release Bundle to edge nodes if it meets a security or License policy defined in JFrog Xray (see [Xray Scanning of Release Bundles (v1)](/docs/xray-scanning-of-release-bundles-v1)).

  To scan your Release Bundle by JFrog Xray, the Release Bundle must first be declared as an indexed resource. For more information, see <Anchor label="Index Xray Resources" target="_blank" href="/security/docs/index-xray-resources">Index Xray Resources</Anchor>.
* [Comprehensive REST APIs](/reference/getallbundles-1) to support the Distribution process.
* [Edge-based Software Distribution](/docs/distribute-release-bundles-v1)
* Third-Party Access (read-only):

  * Cloud instances are licensed to support multiple third-party customers per Edge. Edge nodes are restricted to distributing customer content only.
  * Access to Edge nodes is limited to read-only access for third parties and restricted to distributing customer content only, with the requirement of a single Edge per 3rd party for self-hosted instances.

<Callout icon="📘" theme="info">
  **Note**

  JFrog Distribution requires installation on a dedicated server. For more information, see <Anchor label="Installing Distribution" target="_blank" href="/installation/docs/installing-distribution">Installing Distribution</Anchor>.
</Callout>