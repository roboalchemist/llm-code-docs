# Source: https://docs.jfrog.com/artifactory/docs/distribute-release-bundles-v1-in-an-air-gap-environment.md

# Distribute Release Bundles (v1) in an Air Gap Environment

<Callout icon="📘" theme="info">
  **Subscription Information**

  This feature is supported on the **Self-Hosted** platform, with an **Enterprise+** license.
</Callout>

<Callout icon="📘" theme="info">
  **Note**

  For information about distributing Release Bundles **v2** in an Air Gap Environment, see <Anchor label="Distribute Release Bundle v2 Versions in an Air Gap Environment" target="_blank" href="/governance/docs/distribute-release-bundle-v2-versions-in-an-air-gap-environment">Distribute Release Bundle v2 Versions in an Air Gap Environment</Anchor>.
</Callout>

JFrog Distribution supports distributing your Release Bundles to remote Distribution Edge nodes within an Air Gap environment. This use case is mainly intended for organizations such as financial institutions and military installations that have two or more JFrog Artifactory instances that have no network connection between them.

Distributing Release Bundles v1 in an Air Gap environment involves these main steps:

1. Create and sign a Release Bundle.
2. Export the Release Bundle as an archive (zip file) from your JFrog Distribution.
3. Copy the archive to an external device, such as a hard drive or USB flash drive, and transfer to the Air Gap environment (the network where the destination Artifactory is located)
4. Directly import the archive in the destination Artifactory node.

Importing and exporting your Release Bundles can be performed using one of these methods:

* [Directly on the Distribution page in the platform UI](/docs/export-and-import-release-bundles-v1-in-the-ui)
* [Using a set of dedicated Export and Import REST API commands](/docs/export-and-import-release-bundles-v1-using-the-rest-api)

<Callout icon="📘" theme="info">
  **Supported Product Versions**

  The Air Gap Distribution feature is supported from Distribution 2.5 and requires Artifactory 7.9.
</Callout>