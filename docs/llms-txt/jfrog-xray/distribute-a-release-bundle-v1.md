# Source: https://docs.jfrog.com/artifactory/docs/distribute-a-release-bundle-v1.md

# Distribute a Release Bundle (v1)

<Callout icon="❗️" theme="error">
  **Important**

  This section describes how to distribute Release Bundles v1. For information about distributing Release Bundles v2, which were introduced in Artifactory 7.63.2 and Distribution 2.19.1, see <Anchor label="Distribute Release Bundles (v2)" target="_blank" href="/governance/docs/distribute-release-bundles-v2">Distribute Release Bundles (v2)</Anchor>.
</Callout>

After you have created your Release Bundle v1, you can distribute it to the Distribution Edges to which you have distribution permissions. Distribution can be performed using the JFrog Platform UI or the <Anchor label="Distribute Release Bundle v1 Version" target="_blank" href="/reference/distributereleasebundlev1version">Distribute Release Bundle v1 Version</Anchor> REST API.

Distribution is responsible for triggering the replication process that happens from the source Artifactory to the Distribution edges. First, it replicates the Release Bundle info to each Edge node, and then initiates the replication process in the source Artifactory. For more details, see [The Distribution Flow](/docs/the-distribution-flow).

<Callout icon="⚠️" theme="warning">
  **Warning**

  When a JPD is offline a Release Bundle can not be distributed to an Edge node. This will be a critical error as before every distribution the system checks with Mission Control for available Edges.
</Callout>

## Prerequisites

Use one of the following methods to connect Artifactory and the Edge nodes:

* **<Anchor label="Using Scope Tokens (Pairing Tokens)" target="_blank" href="/administration/docs/access-tokens/#generate-scoped-tokens">Using Scope Tokens (Pairing Tokens)</Anchor>**: Connect the source Artifactory and the Edge nodes using the JFrog Platform scoped tokens function. This function is available from Artifactory version 7.29.7 with the release of the [Distribution Edges Add-on](/docs/hybrid-deployment#hybrid-distribution-from-jfrog-platform-self-hosted) and is the default option used for connecting the source and node (if you are unable to upgrade your self-hosted instance, or need to continue using the Circle of Trust, see next method).
* **<Anchor label="Circle of Trust" target="_blank" href="/administration/docs/access-tokens#circle-of-trust-cross-instance-authentication">Circle of Trust</Anchor>**: Establish a circle of trust between your source Artifactory and Artifactory Edge nodes. This should be applied to both the source and target Artifactory nodes.

## Distribute Release Bundle Versions to Targets

To distribute Release Bundle versions to targets (in Distribution version 2.14.1 and later):

1. In the Application module, select **Distribution > Release Bundles > Distributable**.
2. Locate the Release Bundle to distribute, and click the **Distribute** icon. Distribution fetches the available Edge Nodes from Mission Control, and displays a list of the available Edge Nodes according to the specific user permissions.

   <Image align="center" alt="RBv1_distribute-icon.png" width="70% " src="https://files.readme.io/7867ccea4b9dcc9ad4f7b31790b2728293c6aa5f1feff279f419bd352071d556-uuid-4123047c-e0e3-095d-8e4e-739f40ee01c4.png" />
3. In the Distribute Release Bundle window, the targets are displayed in a list:

   1. To distribute to one or more specific targets, select them from the list. As you select targets, your selections appear at the bottom of the window.
   2. To distribute to all targets, select the **Select All** checkbox.

      <Image align="center" alt="DIST-Distribute_RB.png" width="50% " src="https://files.readme.io/d36b4a28bbd8e752357474edb6030310cf842409b673b7388fb764c7b019189e-uuid-b26d7385-28ba-c5d1-6049-d8ab46db62ee.png" />

<Callout icon="✅" theme="okay">
  **Tip**

  You can also search for specific targets in the search field.
</Callout>

4. \[optional] Select the **Auto create missing repositories** checkbox to ensure you do not attempt to distribute to repositories that do not exist, which will cause distribution to fail. Leave this option unselected if there is a need for greater control over the creation of repositories in the Edge nodes.
5. Click **Distribute** to distribute the Release Bundle version.

<Callout icon="📘" theme="info">
  **Note**

  If the distribution operation included multiple targets, and one or more targets did not receive the Release Bundle version successfully, users will still be able to download the artifacts from those targets that successfully received it.
</Callout>

## Distribute Older Release Bundle Versions

To distribute an older version of your Release Bundle, click it from the Release Bundle module, select the version you want to distribute, and click **Distribute.**

<Image align="center" alt="distribute_RB_version.png" border={true} width="100% " src="https://files.readme.io/d248610a0d6cb3b7fc94dad1d51351772bf4dd4809138e0c9472904c3c7e28d6-uuid-e2a1fe32-ecbb-5e58-9eda-649cfe707275.png" className="border" />

## Redistribute a Release Bundle

Distributing a Release Bundle may fail for different reasons such as network issues or outage of a target Artifactory service. Once you have remediated the problem preventing distribution, you can redistribute the Release Bundles to the services where distribution failed.

To redistribute Release Bundles, first select them. Distribution presents a **Redistribute** icon for each distribution selected. Click that icon to redistribute each Release Bundle individually to the specified target service, or select the **Redistribute** button at the top of the list to redistribute the Release Bundle to all target services selected in a batch process.

<Callout icon="✅" theme="okay">
  **Tip**

  Use the filter to display only those distributions that have failed.
</Callout>

## Automatically Create Missing Repositories

Distribution fails when the target Edge node or source Artifactory does not contain any repositories. From JFrog Distribution release 2.8.1, Distribution enables you to create missing target repositories automatically on the target Edge nodes or source Artifactory when distributing Release Bundles to expedite the distribution flow.

<Callout icon="📘" theme="info">
  **Note**

  This feature requires Artifactory version 7.38.8 or later.
</Callout>

**How does it work?**

During the distribution flow, select the **Auto create missing repositories** checkbox to create missing repositories automatically (prior to release 2.14.1, this checkbox was called Target Repository Auto-Creation).

Automatic creation of missing repositories is particularly useful when you first begin using Distribution. By default this function is not selected to give you better control of the targets where you are distributing Release Bundles.

<Image align="center" alt="DIST-Distribute_RB.png" width="50% " src="https://files.readme.io/d36b4a28bbd8e752357474edb6030310cf842409b673b7388fb764c7b019189e-uuid-b26d7385-28ba-c5d1-6049-d8ab46db62ee.png" />

This feature works according to the path mapping that exists from the source to the target. If advanced path mapping was detected, the target repository cannot be auto-created. To enable automatic creation, set the`distribute.auto-create-target-repo-advance` flag to **true** in the <Anchor label="Distribution Application Config YAML File" target="_blank" href="/installation/docs/distribution-application-config-yaml-file">Distribution Application Config YAML File</Anchor>.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Repositories
      </th>

      <th>
        Without Path Mapping
      </th>

      <th>
        With Path Mapping
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        One Repository
      </td>

      <td>
        If the target repository name and type are the same as the source repository, the repository is created automatically.
      </td>

      <td>
        If there is a one-to-one path mapping between the source repository and target repository, the target repository type will be the same as the source repository type.
      </td>
    </tr>

    <tr>
      <td>
        Multiple Repositories
      </td>

      <td>
        If the target repositories names and types are the same as the source repositories, the repositories are created automatically.
      </td>

      <td>
        * If all repositories are the same repository type in the source and are mapped to one target repository, the target repository created will be the same type as the source with the name specified by the user.
        * If all repositories in the source are different repository types and are mapped to one target repository, the target repository created will be a generic repository.
      </td>
    </tr>
  </tbody>
</Table>

#### Examples

**Example 1: From source to target repository without path mapping**

A Docker image from a Docker repository in the source will be mapped to the Docker repository in the target.

**Example 2**: **From source to target repository with path mapping**

A Docker image from a Docker repository named `docker-local` in the source will be mapped to a Docker repository named `mapped-docker-loca` in the target.

**Example 3**: **Multiple repositories on the source to one target repository with path mapping**

Multiple Docker images from multiple Docker repositories in the source are mapped to a single Docker repository in the target.

**Example 4**: **Multiple repository types on the source to one target repository with path mapping**

A Docker image from a Docker repository and a Helm chart from a Helm repository in the source will be mapped to one generic repository.

## Distribution Target Troubleshooting

If you receive the message, **No distribution targets are available** when attempting to distribute a Release Bundle (v1 or v2), check the following possible causes:

* No distribution targets, in particular Edge nodes, have been installed. For more information, see <Anchor label="Installing Artifactory Edge" target="_blank" href="/installation/docs/installing-artifactory-edge">Installing Artifactory Edge</Anchor>.
* Edge nodes have been installed but have not been added to your JPD. To perform this procedure, see <Anchor label="Register a Platform Deployment" target="_blank" href="/administration/docs/manage-platform-deployments#register-a-platform-deployment">Register a Platform Deployment</Anchor>.
* You do not have the required permissions to view the available Edge nodes and other distribution targets. In that case, contact your platform administrator.
* There are connectivity issues between your JPD and the Edge nodes.