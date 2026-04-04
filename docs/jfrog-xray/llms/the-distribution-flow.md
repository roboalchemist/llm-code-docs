# Source: https://docs.jfrog.com/artifactory/docs/the-distribution-flow.md

# The Distribution Flow

The high-level distribution flow has the following main steps:

* [Step 1: Create a Release Bundle](/docs/the-distribution-flow#step-1-create-a-release-bundle)
* [Step 2: Distribute a Release Bundle](/docs/the-distribution-flow#step-2-distribute-a-release-bundle)
* [Step 3: Download a Release Bundle](/docs/the-distribution-flow#step-3-download-a-release-bundle)

### Step 1: Create a Release Bundle

A Release Bundle can be created using the JFrog Platform UI or by calling the [Create Release Bundle v1 Version](/reference/createreleasebundlev1version) REST API endpoint in JFrog Distribution. This call specifies a variety of parameters, including the files comprising the Release Bundle and various properties associated with it. Since a Release Bundle is immutable, any file included in a Release Bundle cannot be deleted from Artifactory - they are automatically copied and saved into the Release Bundle repository, where their contents cannot be edited or removed. JFrog Distribution collects the required metadata about the artifacts specified in the request by using an AQL query.

To have JFrog Xray scan your Release Bundle, the Release Bundle must first be declared as an indexed resource. For more information, see <Anchor label="Index Xray Resources" target="_blank" href="/security/docs/index-xray-resources">Index Xray Resources</Anchor>.

![CreateRB.png](https://files.readme.io/f2361e8e84e79b04e68aafb8097df6aaa1c52b91166be752484d35cfce09377b-uuid-9f8eb5ab-4377-42cd-48a5-fe6850909ff6.png)

### Step 2: Distribute a Release Bundle

A Release Bundle can distributed using the JFrog Platform UI or by calling the [Distribute Release Bundle](/reference/distributereleasebundlev1version) REST API endpoint in JFrog Distribution.

<Callout icon="📘" theme="info">
  **Blocking Release Bundle Distribution**

  Setting a Watch on a Release Bundle containing a Policy set with a Block Distributing action, will automatically block distributing the infected Release Bundle based on the Xray scanning results. For more information, see [Distribute Release Bundles (v1)](https://docs.jfrog.com/artifactory/docs/distribute-release-bundles-v1).
</Callout>

The distribution process includes the following steps:

1. **Start a distribution transaction**

   In steps 1-4, JFrog Distribution queries JFrog Mission Control for details of the distribution target nodes: <Anchor label="JFrog Artifactory Edges" target="_blank" href="/installation/docs/installing-artifactory-edge">JFrog Artifactory Edges</Anchor> ("Edge nodes"). It then primes the Edge nodes to receive the distributed packages by providing information about distributed files such as their checksum, and provides a GPG key to validate the authenticity of the bundle as a whole.

   <Image align="center" alt="Distribution Graphic Update.png" width="70% " src="https://files.readme.io/3433e471351c350e990c1fd40305920a9a00b1a24b9c99d1b49fd495e0779329-uuid-48f82aaf-9e21-e27b-da11-7fcc45127fd2.png" />
2. **Transfer files with smart replication**

   In steps 5-6, JFrog Distribution copies the contents of the Release Bundle from the source Artifactory to the Edge nodes. By default, the destination repositories on Edge nodes will match the source repositories.
3. **End a distribution transaction**

   In step 7, JFrog Distribution notifies the Edge nodes that the transaction is complete. In turn, each Edge node validates the authenticity of the transferred bundle using the GPG key provided when the transaction started. The Edge nodes then validate the integrity of the transferred files by validating the checksum and hosting the files in their proper location, as specified in the Release Bundle.

   ![DistributeRB2.png](https://files.readme.io/979886e7ff9bf3e2fb3985c4b5c79e947b3c3d2ddd4f1eaf4bb0182e488a8afc-uuid-8cf77387-a4e3-ebde-c4be-a086887e88e3.png)

### Step 3: Download a Release Bundle

The artifacts distributed as a Release Bundle to Artifactory or Artifactory Edge can be downloaded using different package clients, such as a Docker client, npm client, etc. In addition, artifacts can be downloaded using the [JFrog CLI](/docs/distribution-through-cli):

```
jfrog rt dl --bundle bundle_name/bundle_version
```

The JFrog CLI provides additional options for download. For example, the Release Bundle Bill of Materials can be filtered out to download zip files belonging to a specific Release Bundle version:

```
jfrog rt dl "*.zip" --bundle bundle_name/bundle_version
```