# Source: https://docs.jfrog.com/artifactory/docs/export-and-import-release-bundles-v1-using-the-rest-api.md

# Export and Import Release Bundles (v1) Using the REST API

<Callout icon="📘" theme="info">
  **Note**

  For information about exporting and importing Release Bundles v2 using the REST API, see <Anchor label="Export and Import Release Bundles v2 using REST APIs" target="_blank" href="/governance/docs/export-and-import-release-bundle-v2-versions-using-rest-apis">Export and Import Release Bundles v2 using REST APIs</Anchor>.
</Callout>

Exporting and importing your Release Bundles (v1) is performed in two stages, whereby you export the Release Bundles from Distribution and import the Release Bundles on your Artifactory node.

Run these export Release Bundle v1 commands using the **Distribution** REST APIs:

1. [Export Release Bundle v1 Version](/reference/exportreleasebundlev1version)

2. [Get Exported Release Bundle v1 Version Status](/reference/getexportedreleasebundlev1status)

3. Download the Exported Release Bundle Archive: Use the `download_URL` field to download the exported archive when the Status is set to `COMPLETED`.

<Callout icon="📘" theme="info">
  **\[Optional]**

  You can use the REST API to [Delete Exported Release Bundle v1 Archive File](/reference/deleteexportedreleasebundlev1file) from Distribution.
</Callout>

Run these import Release Bundle commands using the **Artifactory** REST APIs:

1. [Import Release Bundle v1 Version](/reference/importreleasebundlev1version)
2. [Get Release Bundle Version Import Status](/reference/getreleasebundleversionimportstatus)