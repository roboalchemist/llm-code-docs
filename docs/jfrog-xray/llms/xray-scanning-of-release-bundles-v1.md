# Source: https://docs.jfrog.com/artifactory/docs/xray-scanning-of-release-bundles-v1.md

# Xray Scanning of Release Bundles (v1)

<Callout icon="❗️" theme="error">
  **Important**

  Xray scanning is available for Release Bundles v1 and Release Bundles v2. Support for Release Bundles v2 was introduced with the release of Artifactory 7.68.6 and Xray 3.81.2. For more information, see <Anchor label="Scan Release Bundle v2 Versions with Xray" target="_blank" href="/governance/docs/scan-release-bundle-v2-versions-with-xray">Scan Release Bundle v2 Versions with Xray</Anchor>.
</Callout>

JFrog Xray supports the scanning of Release Bundles as well as setting Policies and Watches on Release Bundles.

Before scanning your Release Bundles, you will need to:

1. Add the Release Bundles to the list of Xray-indexed resources. For more information, see <Anchor label="Index Xray Resources" target="_blank" href="/security/docs/index-xray-resources">Index Xray Resources</Anchor>.
2. Create a Policy containing specific rules that, if met, will trigger one or more defined actions (block Release Bundle promotion (v2 only), block Release Bundle distribution to Edge nodes (v1 & v2)). For more information, see <Anchor label="Create Policies" target="_blank" href="/security/docs/create-policies">Create Policies</Anchor>.
3. Configure a Watch that applies a Policy to specific Release Bundles. For more information, see <Anchor label="Create Watches" target="_blank" href="/security/docs/create-watches">Create Watches</Anchor>.

For information about viewing scanning results, see [View Xray Data of Scanned Release Bundles (v1)](#view-xray-data-of-scanned-release-bundles-v1).

## View Xray Data of Scanned Release Bundles (v1)

In the Release Bundles version list, you can view the status of your scanned Release Bundle v1 versions in the **Xray Status** column.

<Image align="center" alt="release bundle with xray vulnerability.png" border={true} width="70% " src="https://files.readme.io/c5417ee20c16f43022dd934115c7a982bab0bdb9f89cc3c2b674a848292aaab2-uuid-1ad1b0d3-9c53-f7ee-e588-aa4205213a29.png" className="border" />

Click the Release Bundle version to view detailed information in the **Xray Data** tab. This tab displays any violations, security issues, or license issues that may have been detected on the distributed version. You can run the following Xray-related actions on the version:

* Scan for Violations
* Assign Custom Issue
* Assign Custom License
* Export Scan Data
* Switch to Old Xray (reverts to the table view of scan results)

For detailed information about each tab, see <Anchor label="Understanding and Analyzing Xray Scan Results" target="_blank" href="/security/docs/understanding-and-analyzing-xray-scan-results-p">Understanding and Analyzing Xray Scan Results</Anchor>.

<Image align="center" alt="RBv1_Xray-scan-violations_spliced.png" border={false} width="70% " src="https://files.readme.io/18d7d7ea64bf95d2d0722f524c43db8427aa48cb50a98482b1d0cbfa97bdbeb4-uuid-aa08fdd9-9284-bd31-bada-e4ce840d3a38.png" />

## Block Promotion and Distribution of Release Bundles

You can set the Block actions in an Xray Policy to prevent Release Bundles containing security vulnerabilities from being promoted and distributed. For more information, see <Anchor label="Configure Xray" target="_blank" href="/security/docs/configure-xray">Configure Xray</Anchor>.

<Image align="center" alt="Xray_RB-blocking-actions.png" border={false} width="40% " src="https://files.readme.io/c10ae6f405f47dd380d4190c25f630bf46a486360bcb2565aa8dd198e4eabbd8-uuid-a74f2afa-eb9c-0a4e-ec7d-4f523f3c94f6.png" />

<Callout icon="📘" theme="info">
  **Note**

  The blocked Release Bundle appears in the Actions Tracking tab with the promotion or distribution status of Failed.
</Callout>