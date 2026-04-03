# Source: https://docs.jfrog.com/artifactory/docs/release-bundle-v1-tasks.md

# Release Bundle (v1) Tasks

You can perform the following tasks on Release Bundle v1 versions:

* [View Release Bundle version details](#view-release-bundle-v1-version-details)
* [Search for Release Bundles](#search-for-release-bundle-v1-versions)
* [Download Release Bundle contents](#download-release-bundle-contents)
* [Edit Release Bundles](#edit-a-release-bundle-v1)
* [Clone Release Bundles](#clone-release-bundles-v1)
* [Delete Release Bundles](#delete-a-release-bundle-v1)

<Callout icon="📘" theme="info">
  **Note**

  To search for a specific Release Bundle by name or by the latest version, use the filter search (from 2.14.1).

  The total count for both Distributable and Received Release Bundles is displayed in the UI (from 2.14.1).
</Callout>

## View Release Bundle v1 Version Details

To view a version of a Release Bundle v1, select a Release Bundle and then select the required version.

<Image align="center" alt="RBv1_versions_table.png" width="70% " src="https://files.readme.io/596dbce3cf87330d7de631601fc14f5855202e7aadc6e75fcea6e23eccda9db7-uuid-f40503e9-69fa-8e71-792d-c5539a4e365e.png" />

The page for a selected Release Bundle version displays the following information:

**General Info:** The panel along the top of the screen displays general information such as the version, creation date, status, delivery summary, and the size of the Release Bundle

**Details:** This panel displays details about the selected Release Bundle version in a series of tabs: **Actions Tracking,** **Content**, **Release Notes**, **Xray Data, Pipelines, Spec,** and **Effective Permissions**.

<Image align="center" alt="RBv1_version-details.png" width="70% " src="https://files.readme.io/b55e2f253f68b2b234ee2cae519248a3498073bc908e714f06d2e56f6bec2596-uuid-4a9135cc-40fc-24c5-25f7-d3e93b76b847.png" />

### Actions Tracking Tab

The **Actions Tracking** tab provides a history for this Release Bundle version.

<Image align="center" alt="RBv1_Actions-Tracking-tab.png" width="70% " src="https://files.readme.io/9817a578c26a4563af6048bffd0d8d7c292f8ec451c641deca1736cc13be1a66-uuid-1537ef7b-3bbe-df71-d685-058bf012fdea.png" />

<Table>
  <thead>
    <tr>
      <th>
        Item
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **ID**
      </td>

      <td>
        The ID of the distribution action.

        <Callout icon="📘" theme="info">
          **Multiple rows with the same ID**

          You may see multiple rows in this table with the same ID because a single distribution action may distribute a Release Bundle to several target nodes.
        </Callout>
      </td>
    </tr>

    <tr>
      <td>
        **Distribution Target**
      </td>

      <td>
        The number of distribution targets. When expanded, this column shows the name of the target.

        <Callout icon="✅" theme="okay">
          **Click for direct access**

          Click on the distribution target name to be redirected directly to its UI.
        </Callout>
      </td>
    </tr>

    <tr>
      <td>
        **Action**
      </td>

      <td>
        The action that was performed.
      </td>
    </tr>

    <tr>
      <td>
        **Started**
      </td>

      <td>
        The date and time when the action started.
      </td>
    </tr>

    <tr>
      <td>
        **Finished**
      </td>

      <td>
        The date and time when the action finished.
      </td>
    </tr>

    <tr>
      <td>
        **Duration**
      </td>

      <td>
        The duration of the distribution action.
      </td>
    </tr>

    <tr>
      <td>
        **Status**
      </td>

      <td>
        The status of the action.
      </td>
    </tr>

    <tr>
      <td>
        **Artifacts Progress**
      </td>

      <td>
        The percent completion of the action and number of attempts at completion.
      </td>
    </tr>

    <tr>
      <td>
        **Details**
      </td>

      <td>
        Summary of some details about the action.

        <Callout icon="✅" theme="okay">
          **Click for details**

          Click on this field to get full details of the action. This is where you can get more details in case of an error.
        </Callout>
      </td>
    </tr>
  </tbody>
</Table>

### Content Tab

The **Content** tab displays the artifacts, builds, and metadata that comprise the Release Bundle.

Click any artifact or build to view details about it in the right panel in the tab.

<Callout icon="✅" theme="okay">
  **Click for direct access**

  Click an artifact's source path to be redirected to the right location in the tree browser of the corresponding Artifactory service.
</Callout>

<Image align="center" alt="RBv1_Content-tab_artifact-details.png" width="70% " src="https://files.readme.io/facdfddd9c4aecc421db79eed6c2baa86834670f75ed7af8f790e2236dff7742-uuid-795a626e-a007-9c17-d792-5a27fd9e9e28.png" />

If the artifact has been blocked for download by JFrog Xray (in which case, you will not be able to distribute the Release Bundle), this will be indicated in the **Xray Status** field for the selected artifact in the **Content** tab.

<Image align="center" alt="BlockedArtifact.png" width="70% " src="https://files.readme.io/dba6c1396a36e094d1f6546e8efdfc66f447dec549fed5594eaa3bce2c2f58df-uuid-bce2b8b7-56b7-decd-5c7b-39f4b9e0a796.png" />

### Release Notes Tab

The **Release Notes** tab displays release notes for the bundle. These can be written in markdown, ASCII doc, or plain text.

<Image align="center" alt="RBv1_Release-Notes-tab.png" width="80% " src="https://files.readme.io/3d33b8828ca6dedd6efbf08a6152f0bb1760205b1edf384062cbf9f36acd4134-uuid-7a9b5f61-9c66-ea5a-3b93-754c5131e5c5.png" />

### Xray Data Tab

The **Xray Data** tab displays the results of the scan performed by Xray on the Release Bundle, including policy violations and other security vulnerabilities that were discovered.

<Image align="center" alt="RBv1_Xray-data-tab_spliced.png" width="70% " src="https://files.readme.io/61d928652cf7a900d18aad6a0926bc7583fe8e2deca3d0cd4bf74b9f8e979165-uuid-19ca8403-96a7-3d3c-4f3b-e286bf28be79.png" />

#### Pipelines Tab

The **Pipelines** tab is a verification system that determines which pipelines/steps generated a specific artifact. It provides users with a way to ensure that their artifacts have not been tampered with before these artifacts are promoted through the CI/CD workflow.

<Image align="center" alt="RBv1_Pipelines-tab.png" width="70% " src="https://files.readme.io/6a32830cd0f1f396a319c5548892918ec0461b3a55513df6d81f73445c1ba255-uuid-22d1c9b5-4094-4240-04b6-2a664a74aeca.png" />

For more information, see <Anchor label="Signed Pipelines" target="_blank" href="/pipelines/docs/signed-pipelines">Signed Pipelines</Anchor>.

#### Spec Tab

The **Spec** tab displays the source Artifactory service from which the artifacts of this Release Bundle were assembled as well as the list of queries that assembled the artifacts.

<Image align="center" alt="SpecTab.gif" width="70% " src="https://files.readme.io/da14f14b33ccef9ab7feffbaa56ee8de969ab7873ec28d3c57d502c0a321d206-uuid-3498b6fb-0953-3e70-e4b6-fcfd81377b2a.gif" />

<Callout icon="✅" theme="okay">
  **Click the Artifactory service**

  Clicking the Artifactory service opens a new tab on the home screen of that service.
</Callout>

Clicking on any of the queries expands it displaying the details of the query that governed the assembly of the Release Bundle artifacts.

You can select the **AQL** checkbox to see the final AQL query that was used to assemble the artifacts.

#### Effective Permissions Tab

The **Effective Permissions** tab displays the effective permissions assigned for the selected Release Bundle. For more information, see <Anchor label="Permissions" target="_blank" href="/administration/docs/permissions">Permissions</Anchor>.

<Image align="center" alt="RBv1_Effective-Permissions-tab.png" width="70% " src="https://files.readme.io/21ad1fd9f7c864ded0c717f03c3fac26588287ed0505d90122e3bbdda4c5e184-uuid-575252ec-3681-2c37-ab16-9bebc586bdb4.png" />

## View Release Bundle v1 Versions on the Source Node

<Image align="center" alt="DIST_Release_Bundle_main.png" width="70% " src="https://files.readme.io/286d72a6197090eb9db0398abf62e494f8eb23172e7743ddb70c53551545d932-uuid-cd51c771-6add-38a8-0fbf-c74a18dede66.png" />

| Item                | Description                                                                                     |
| ------------------- | ----------------------------------------------------------------------------------------------- |
| **Name**            | The Release Bundle name.                                                                        |
| **Latest Version**  | The Release Bundle's latest version.                                                            |
| **Distribution ID** | The sequential number of the distribution job. Only the last 3 distribution jobs are displayed. |
| **Started**         | The time the distribution began                                                                 |
| **Status**          | The distribution job status.                                                                    |
| **Progress**        | The distribution progress percentage.                                                           |

## Search for Release Bundle v1 Versions

The Platform supports searching for Release Bundle v1 versions using the following methods:

* **Dedicated Platform Release Bundle Search**: You can search for distributable and received Release Bundles within a specified time page. For more information, see [Application Search](/docs/application-search).

  <Image align="center" width="60% " src="https://files.readme.io/24f19d85c4859bcb80b5034e2812db75d68b069611477f189ae9031dea6de030-image.png" />

  <br />
* **AQL Search for Release Bundles:** To search for Release Bundles on an Edge node, you can use the **release** and **release\_artifact** domains introduced to AQL. For details, please refer to [AQL Entities and Fields](https://docs.jfrog.com/artifactory/docs/artifactory-query-language#aql-entities-and-fields).

## Download Release Bundle Contents

When you are ready to deploy a software release, you can download the contents of a Release Bundle from Artifactory using the CLI command:

```
jf rt dl --bundle
```

Where the value format of `--bundle` is `bundleName/bundleVersion`.

#### Download from a Source Artifactory

When downloading the contents of a Release Bundle (v1 only) from a source Artifactory instance, the directory structure is as follows:

`bundleName > bundleVersion > repositoryName > artifacts > ...`

For example:

```
.
├── BD-131253-835.                        #bundleName
│   └── 1                                 #bundleVersion
│       └── generic-repo-1722507172888    #repositoryName
│           └── artifacts
│               └── maven
│                   └── commons-4.69.jar
```

#### Download from a Target Artifactory

When downloading the contents of a Release Bundle (v1 or v2) from a target Artifactory (for example, an Edge node), the directory structure does not include the `bundleName` and `bundleVersion`. For example:

```
└── artifacts
    └── maven
        └── commons-4.69.jar
```

For more information about downloading files from Artifactory using the JFrog CLI, see [Downloading Files](/docs/generic-files#downloading-files).

## Edit a Release Bundle (v1)

You can edit Release Bundles that have been saved with 'Create' as a draft and have not yet been signed.

From the **Application** module under **Distribution**, go to **Distributable > \[Bundle\_Name] | \[Bundle\_Version]**, click **Actions** , and select **Edit Version**.

<Image align="center" alt="editing a release bundle.png" border={true} width="70% " src="https://files.readme.io/aa1af2f60229cc98b54be8cfa80d212c232b5a39e938660c9d0f07db0088c001-uuid-79927d9d-769f-1fea-9f3c-b44121993656.png" className="border" />

## Clone Release Bundles (v1)

To clone an existing Release Bundle v1 version, select **Clone Version** from the **Actions** menu.

This will copy the Release Bundle spec, including its name and queries, into a new Release Bundle page. Details on the page can then be adjusted and saved accordingly.

<Image align="center" alt="RBv1_Clone-RB_menu-option.png" border={true} width="80% " src="https://files.readme.io/d337380ba6ce2465783d4cbe068588e3637849fa1973943788689278a9e758b1-uuid-b0ce1876-1692-cdc0-c341-061783e17ca0.png" className="border" />

## Delete a Release Bundle (v1)

You can delete Release Bundles v1 using the platform UI or the [Delete Release Bundle v1 Version](/reference/deletereleasebundlev1versionfromdistributionedges) REST API. This function is available for users with <Anchor label="Release Bundle delete permissions" target="_blank" href="/administration/docs/permissions">Release Bundle delete permissions</Anchor>.

**To delete an existing Release Bundle v1 version:**

1. Select **Delete Version** from the **Actions** menu.

   <Image align="center" alt="RB_delete_RB_version.png" border={true} width="70% " src="https://files.readme.io/e11f80fd56ee85b0dc0c7108c2a838c619d05b2c8b2521ca845a7a85afbb5bd4-uuid-72cbd1b5-05a5-1562-53d8-7bb0a1e77160.png" className="border" />
2. Select the Edge nodes from which the Release Bundle version should be deleted.
3. \[optional] Select the **Delete also from JFrog Distribution** checkbox to delete the Release Bundle locally from JFrog Distribution in addition to the selected Edge nodes.

   <Image align="center" alt="Remote-Delete_2_21_0.png" width="50% " src="https://files.readme.io/c08534ecd1af9fc447a240681728ca3b5c2ff8c341e7b922495ecf25fc5d4361-uuid-2a5e8ab7-0657-ab13-9136-0c1aaaaec4d2.png" />
4. Click **Delete**.

<Callout icon="📘" theme="info">
  **Note**

  From Artifactory release 7.39.1, you can verify that the empty folders of a Release Bundle are deleted as part of its deletion from both target Repositories and Release Bundles Repository. This is done through a parameter in the Artifactory `system.yaml` file called `releasebundle.cleanup.deleteEmptyFolder`, which is set to `true` by default.
</Callout>