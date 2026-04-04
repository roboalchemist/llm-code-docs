# Source: https://docs.jfrog.com/artifactory/docs/create-release-bundles-v1.md

# Create Release Bundles (v1)

<Callout icon="❗️" theme="error">
  **Important**

  This section describes how to create Release Bundles v1. For information about creating Release Bundles v2, which were introduced in Artifactory 7.63.2 as part of <Anchor label="Release Lifecycle Management" target="_blank" href="/governance/docs/release-lifecycle-management">Release Lifecycle Management</Anchor>, see <Anchor label="Create Release Bundles (v2)" target="_blank" href="/governance/docs/create-release-bundles-v2">Create Release Bundles (v2)</Anchor>.
</Callout>

JFrog Distribution enables creating and distributing Release Bundles from the Artifactory service. Each Release Bundle may only contain artifacts from a single Artifactory service.

To create a Release Bundle, Distribution runs queries against the JPD in order to retrieve the required artifact references and their properties. Fetching the artifacts is performed according to the security privileges of the user who made the request.

To prevent tampering with the Release Bundle, it is signed by JFrog Distribution using a **[GPG key](/docs/gpg-signing)**. The same GPG key is then used by the Artifactory Edge to validate the Release Bundle before it is accepted.

<Image align="center" alt="CreateRB.png" width="70% " src="https://files.readme.io/a0c92e4dd1a4597bc5c6e69dc826b6e4691496475ea6c06eb92a49a4f0157a12-uuid-6866c9f1-ba28-23ad-ab88-e0e6a0c4eec0.png" />

<Callout icon="📘" theme="info">
  **Note**

  A Release Bundle version can include up to 3,000 artifacts. This number is not limited by the product, but exceeding it is not recommended.
</Callout>

## Methods for Creating Release Bundles

There are two methods for creating Release Bundles v1:

* Using the [REST API](/reference/createreleasebundlev1version)
* Using the [JFrog Platform UI](#create-a-new-release-bundle-through-the-platform-ui)

In either case, you define the artifacts to be included in the Release Bundle through a set of queries you can define.

In the final stages of creating a Release Bundle v1 in the JFrog UI, you can opt to save the Release Bundle in the following modes:

* Draft version: You can create a draft version that can be edited by clicking **Create.**
* Signed version (Unmodifiable): You can skip the draft phase by clicking **Create & Sign** to sign and finalize the process without a draft phase.
* To search for a specific Release Bundle by name or by the latest version, use the filter search.
* The total count for both Distributable and Received Release Bundles is also displayed in the UI.

## Prerequisites

Creating a Release Bundle requires the <Anchor label="Release Bundle 'Write' permissions" target="_blank" href="/administration/docs/permissions">Release Bundle 'Write' permissions</Anchor>.

<Callout icon="📘" theme="info">
  **Note**

  When creating a Release Bundle, <Anchor label="matrix properties" target="_blank" href="/artifactory/docs/jfrog-properties#use-cases-for-jfrog-properties">matrix properties</Anchor> already defined for the artifacts are added to the Release Bundle. Additional custom properties can be added during the initial Release Bundle version created using the [Create Release Bundle](/reference/createreleasebundlev1version) REST API. These properties are transferred over to the Edge Node as part of the distribution process.
</Callout>

## Create a New Release Bundle through the Platform UI

<Callout icon="❗️" theme="error">
  **Important**

  This section describes how to create Release Bundles v1. For information about creating Release Bundles v2, which were introduced in Artifactory 7.63.2 as part of <Anchor label="Release Lifecycle Management" target="_blank" href="/governance/docs/release-lifecycle-management">Release Lifecycle Management</Anchor>, see <Anchor label="Create Release Bundles (v2)" target="_blank" href="/governance/docs/create-release-bundles-v2">Create Release Bundles (v2)</Anchor>.
</Callout>

You can use the platform UI to create a Release Bundle containing the artifacts to be distributed. This includes general details about the Release Bundle, the AQL queries that define its contents, and optional release notes containing additional information about the Release Bundle.

**To create a Release Bundle v1 using the platform UI:**

1. From the **Application** module, select **Distribution** > **Distributable**, and then click **New Release Bundle**.

   <Image align="center" alt="DIST_Release_Bundle_main.png" width="70% " src="https://files.readme.io/286d72a6197090eb9db0398abf62e494f8eb23172e7743ddb70c53551545d932-uuid-cd51c771-6add-38a8-0fbf-c74a18dede66.png" />

   This displays the New Release Bundle window.

   <Image align="center" alt="new_release_bundles.png" width="70% " src="https://files.readme.io/9a4d9ef9ef1bf6bd2312f7ef94307539a73dbd4e75016b06cc067ef296c23c0f-uuid-a7934faf-f154-a67b-7fed-20aeb01973a3.png" />
2. Enter the Release Bundle details according to the general details below, and then click **Create Query** (see [Adding a Query](#adding-a-query) for details).

The Release Bundle page is divided into three panels: **General Details**, **Spec** , and **Release Notes**.

**General Details**

| Field       | Description                                                                                                                                                                                                |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name        | The Release Bundle name. The Release Bundle name must start with an alphanumeric character followed by an alphanumeric or one of the following characters: `- _ :` . The maximum length is 255 characters. |
| Version     | The Release Bundle version. The maximum length is 255 characters.                                                                                                                                          |
| Description | The Release Bundle description.                                                                                                                                                                            |

**Spec**

This section specifies the Artifactory service from which the Release Bundle will be assembled (remember, a Release Bundle can only be assembled from a single Artifactory service) and the different queries that will be used to assemble the artifacts. For more details on how to define the queries, see [Adding a Query](#adding-a-query).

| Field | Description        |
| ----- | ------------------ |
| Name  | The query name.    |
| Query | The query details. |

**Release Notes**

This section specifies release notes for the Release Bundle.

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Type
      </td>

      <td>
        The release notes format. Supported types include **Markdown**, **Asciidoc** and **Plain** **Text**.

        <Callout icon="⚠️" theme="warning">
          **Warning**

          Starting with Distribution 2.26.1, users are restricted from adding HTML tags to release notes written in Markdown. This behavior is controlled by the `enable-sanitize-release-notes` configuration [property](/installation/docs/distribution-application-config-yaml-file), which is set to `true` by default.

          To keep the platform safe against possible cross-site scripting (XSS) attacks, it is recommended to not change this setting.
        </Callout>
      </td>
    </tr>

    <tr>
      <td>
        Edit | Preview
      </td>

      <td>
        Use these links to edit the release notes in your selected format and then preview how they will look once rendered.
      </td>
    </tr>
  </tbody>
</Table>

### Adding a Query

There are two ways to build a query:

* [Use a simple query builder](#use-the-query-builder)
* [Use AQL (Artifactory Query Language)](#use-aql)

To select the way you want to build your query, hover over Create Query and select either **Add Query** or **Add AQL Query**.

#### Use the Query Builder

The query builder lets you build your query by filling in a simple form. The parameters you enter are eventually translated into an AQL query which you can view by setting the **Show AQL** checkbox at the end of the form.

1. To use the query builder, hover over the **Create Query** button and select **Add Query**. This will launch a multi-step wizard.

   <Image align="center" alt="add-query_menu-option.png" width="60% " src="https://files.readme.io/88ec1e3a1006ecf4f2becf13213cf247f8791138c6d185cb217bbcc10c0a74d4-uuid-26f4856f-333b-6659-d948-4f9542eedf63.png" />
2. In the **Query Details** step, start by giving your query a name. You can then specify different search criteria including:

   * Repository names
   * Build names and numbers
   * Properties with specific values
   * Include and Exclude patterns![](https://files.readme.io/05b758cbf941446d8ca30758423f51def92e15213ce5165f5c8f78a057b254b8-uuid-236f1168-62f8-bd36-1c11-7b67920e38da.png)
3. To specify multiple values for each of these parameters, click the '+' button to the right of the parameter.
4. Using the **And | Or** options, you can add multiple properties in a single click of a button.

#### Use AQL

1. To add an AQL query, under Create Query, select **Add AQL Query**.

   This will launch a multi-step wizard.
2. In the **Query Details** step, name your query and provide the AQL expression that will be used for assembling the artifacts, for example:

   <Image align="center" alt="AddAQLQuery.png" width="70% " src="https://files.readme.io/ca74d66779b54eaf6d40ea6e357841b35b4c98322dfe3d7a5d86516a8f028d8c-uuid-755965bb-7a2e-1905-4e06-16097b79c249.png" />
3. Click **Next**.

#### Preview Artifacts

After specifying your query details (whether using an AQL query or the query builder), you can view the artifacts that will be included in your Release Bundle under the **Preview Artifacts** tab.

<Callout icon="📘" theme="info">
  **Note**

  If the source or target Artifactory service specified for the Release Bundle does not have a correct and valid license, Distribution will display an error that it cannot create the Release Bundle.
</Callout>

#### Additional Details Tab

The Additional Details tab lets you specify two more parameters for your Release Bundle:

| Parameter             | Description                                                                                                                                                                                                                                                           |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Additional Properties | Specify a list of properties that will be attached to all artifacts in your Release Bundle during the distribution process, in addition to those that they already have.                                                                                              |
| Path Mappings         | Specify a list of mappings to govern where artifacts will be placed in your target Artifactory service according to their location in your source Artifactory service. You may use any of the Path Mapping Templates provided, or set up custom mappings of your own. |

#### Path Mapping Templates

As a convenience, JFrog Distribution provides a set of commonly used templates you can use to set up your path mappings. Simply select one of the templates listed under Use Template, and then modify the placeholders to correspond with your setup.

The templates provided are:

| Template          | Description                                                                                                              |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Change Repository | All files in a specific repository on the source Artifactory service are mapped to a different repository on the target. |
| Change Folder     | All files are moved to a specific folder in the target.                                                                  |
| Rename Folder     | All files in a specific folder on the source Artifactory service are mapped to a different folder on the target.         |

![PathMappingTemplates.gif](https://files.readme.io/2c3c01c54cb3b014a724d1df1d0dcfd175d508610a6fc499fcfaa484d04cc4ea-uuid-f4afb3c3-ebf2-dfac-70e7-ee33da40a5f5.png)

Click **Save** and then click **Create**. This will create a draft Release Bundle that can be edited, signed, and then finally distributed.

Alternatively, you can skip the draft phase by clicking **Create & Sign** to sign and finalize the process without a draft phase (continue to Signing a Release Bundle).

### Including Docker Images in a Release Bundle

To include Docker image in the Release Bundle, it is sufficient to specify query criteria that will match the manifest.json of the desired docker image. Distribution will include all the Docker layers of the Docker image associated with that manifest.json file.

For example, we have a Docker image of a PostgreSQL version 11.1 in a Docker repository called `docker-local`.

The content of the repository has the following hierarchy:

The `manifest.json` file includes the following property:

docker.manifest.digest `=` sha256:acb7f2b2e9bd560a32c0ba01991870f56f89deeff5f3224bc50aac2a98b7f73e

All the other files under `docker-local/postgres/11.1` are the layers composing this specific image.

<Callout icon="📘" theme="info">
  **Docker digest**

  The “digest” parameter is designed as an opaque parameter to support verification of a successful transfer. For example, an HTTP URI parameter might be as follows:

  sha256:6c3c624b58dbbcd3c0dd82b4c53f04194d1247c6eebdaab7c610cf7d66709b3b

  Given this parameter, the registry will verify that the provided content does match this digest.
</Callout>

To include all the artifacts in the image (manifest and layers) it is sufficient to specify a query criteria that will match the `manifest.json` of the desired Docker image:

<Image align="center" alt="Screen Shot 2020-05-18 at 12.26.28.png" width="60% " src="https://files.readme.io/8afd9ae00e2a74f94a5f7e45cd0b6670ddcd501cc41c5a7904facd3491d52fdb-uuid-7a957630-d9e0-3f0d-1138-ee4e529c4f37.png" />

**AQL example**

```
items.find({
    "$and": [
        {
            "$or": [
                {
                    "repo": {
                        "$eq": "docker-local"
                    }
                }
            ]
        },
        {
            "$or": [
                {
                    "@docker.manifest.digest": "sha256:acb7f2b2e9bd560a32c0ba01991870f56f89deeff5f3224bc50aac2a98b7f73e"
                }
            ]
        }
    ]
})
```

#### Include a List of Manifests in a Release Bundle

To include a multi-architecture Docker image in a Release Bundle, specify query criteria that will match the `list.manifest.json` file of the desired image. This file (also known as a **fat manifest file**), and all referenced images and manifest files, will be included in the Release Bundle v1.

### Signing a Release Bundle

<Callout icon="❗️" theme="error">
  **Important**

  This section is relevant for Release Bundles v1 only.
</Callout>

Signing a Release Bundle finalizes the process of creating a Release Bundle. This sets the Release Bundle status to **Signed** and the Release Bundle can no longer be edited.

<Callout icon="📘" theme="info">
  **Note**

  Signing a Release Bundle will trigger the Artifactory to clone the contents of the signed Release Bundle into an [isolated Release Bundle Repository](/docs/release-bundle-repositories).
</Callout>

1. You can sign a Release Bundle from the Edit Release Bundle page or from the New Release Bundle page.
2. From Distribution release 2.14.1, if you are using multiple GPG signing keys in Distribution, you can now select which signing key to use in the Platform UI (previously available only from the REST API). If no key is selected, the default/primary key will be used to sign the Release Bundle.
3. Click **Sign Version**.
4. In the Sign Version window, you will see the name of the Release Bundle and its version. From the Select Signing Key dropdown, select the signing key.

   <Image align="center" alt="DIST_GPG-Sign-Version.png" width="50% " src="https://files.readme.io/8bf5d041769884b41d702394f57eb09da84dd9dfffb3f8c39e47a96606d4643c-uuid-d799e17b-f3a4-f24f-ac82-59fc9b67ab07.png" />
5. If the signing key was created with a passphrase, JFrog Distribution will prompt you to enter the passphrase.

   <Image align="center" alt="DIST-sign-version-with-pass.png" width="50% " src="https://files.readme.io/81325ebca3823e9afd665703483291b26a95366a006bc9c02f71bb34648f6ab8-uuid-716d41c3-c39e-ae71-4aed-a0f4536f6fce.png" />

<Callout icon="❗️" theme="error">
  **Important**

  Once you sign a version, you will not be able to edit it.
</Callout>

6. Click **Sign** to sign your version.
7. Next, continue to distributing your Release Bundle when ready.