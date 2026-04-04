# Source: https://docs.jfrog.com/artifactory/docs/view-release-bundles-on-edge-nodes.md

# View Release Bundles on Edge Nodes

The Release Bundles **Received** tab contains a table of all distributed Release Bundles (v1 and v2) that were received by the device (either an Artifactory instance or more typically, an [Edge node](/installation/docs/installing-artifactory-edge)). See the sections below for details about the information displayed for each Release Bundle type:

* [Release Bundles v2](/docs/view-release-bundles-on-edge-nodes#view-release-bundles-v2-on-edge-nodes)
* [Release Bundles v1](/docs/view-release-bundles-on-edge-nodes#view-release-bundles-v1-on-edge-nodes)

<Callout icon="📘" theme="info">
  **Note**

  You must be an admin user to view Release Bundles received by Edge nodes.
</Callout>

### View Release Bundles v2 on Edge Nodes

You can view a list of distributed Release Bundles v2 that were received by this device by turning on a toggle switch. From the list of Release Bundles, you can drill down to view a list of distributed versions. You can also drill down into a version to view the list of artifacts contained in the version.

**To view a list of received Release Bundles v2:**

1. In the **Applications** module, select **Distribution > Release Bundles**.
2. Turn on the **Show Release Bundle v2** toggle.

   The table displays a list of received Release Bundles v2. Each row includes the name of the Release Bundle, the latest version received, the total number of versions received, and the date when the latest version was received.

   <Image align="center" alt="Received-tab_v2a.png" border={true} width="60% " src="https://files.readme.io/b7ac200e2415af7c02b272a2a5fe15bc32cad9206696e481eea2d857a1652ffd-uuid-e749c55c-b42e-1074-28a3-3dc1d37d47bd.png" className="border" />

<Callout icon="✅" theme="okay">
  **Tip**

  Click **Import Release Bundle** to import a Release Bundle version into the device. This is typically used in an air gap environment. For more information, see [Import a Release Bundle (v1) Version in the UI](/docs/export-and-import-release-bundles-v1-in-the-ui#import-a-release-bundle-v1-version-in-the-ui).
</Callout>

3. Click the name of a Release Bundle to view a list of received versions.

   <Image align="center" alt="Received-tab_v2a_version-list.png" border={true} width="60% " src="https://files.readme.io/0b3ea91698ad87d2a093a61615e9dc3adccd1a7087112331619493eaa27b703e-uuid-00178b75-869d-ba10-767b-fd5ebcbf1203.png" className="border" />

<Callout icon="✅" theme="okay">
  **Tip**

  To delete a Release Bundle version from the device, click the trash can icon.
</Callout>

4. Click a specific version to view the contents of that version.

   <Image align="center" alt="Received-tab_v2a_version-contents.png" border={false} width="40% " src="https://files.readme.io/b6aa7317162477ab8bd5917fa3d9a5fd59f2a582cfeed7d2e5a790cc38429f32-uuid-43ab1fa4-0208-a97d-2791-13f3c7e13392.png" />

### View Release Bundles v1 on Edge Nodes

You can view a list of distributed [Release Bundles v1](/docs/distribute-a-release-bundle-v1) that were received by this device.

**To view a list of received Release Bundles v1:**

1. In the **Applications** module, select **Distribution > Release Bundles**.
2. Turn off the **Show Release Bundle v2** toggle.

   The table displays a list of received Release Bundles v1. Each row includes the name of the Release Bundle, the latest version, and the date it was received.

   <Image align="center" alt="Received-tab_v1a.png" border={true} width="50% " src="https://files.readme.io/c0590b9e85a1c0f05c189686110d0fcdebef452aa10d92935a5ec061b8c13b1d-uuid-fe2ab5eb-c6e9-a849-66f5-e6ea9e8f8cb7.png" className="border" />

<Callout icon="✅" theme="okay">
  **Tip**

  Click **Import Release Bundle** to import a Release Bundle version into the device. This is typically used in an air gap environment. For more information, see [Import a Release Bundle (v1) Version in the UI](/docs/export-and-import-release-bundles-v1-in-the-ui#import-a-release-bundle-v1-version-in-the-ui).
</Callout>

3. Click the name of a Release Bundle to view a list of received versions.

   <Image align="center" alt="Received-tab_v1_version-list.png" border={false} width="40% " src="https://files.readme.io/e79c7811ec84328e96e326083d5008eb8200255c7fe66b930a41a77e784166e6-uuid-afd69c89-fb0d-b4be-c683-2ffdf36fbc66.png" />

<Callout icon="✅" theme="okay">
  **Tip**

  To delete a Release Bundle version from the device, click the trash can icon.
</Callout>

### Additional Details

* The Search feature (added in release 2.15.0) enables you to find any Release Bundle by name or by using a wildcard with other Release Bundle details.
* All Release Bundles are pulled using the REST API, ensuring you can search for any Release Bundle regardless of when it was released (available from release 2.15).
* Release Bundles can be sorted according to name, latest version, or creation date (available from release 2.15.0).

From Artifactory 7.55.6, a new Cleanup function has been introduced that lets you determine which Release Bundles should be deleted and which should be kept, regardless of whether that Release Bundle meets the deletion criteria.

In addition, a Cleanup History tab has been added next to the Received tab, which records any changes you apply to the Release Bundles through the Cleanup function, including deletions, changing an item’s status from Keep to Don’t Keep, and changing an item’s status from Don’t Keep to Keep.

To learn more, see [Manage Release Bundles in the JFrog Platform UI](/docs/manage-release-bundles-in-the-jfrog-platform-ui).

<Callout icon="📘" theme="info">
  **Note**

  The Cleanup Report and Cleanup History tab are available only to admin users.
</Callout>

<Image align="center" alt="artifactory_Edge_distribution_page.png" border={false} width="70% " src="https://files.readme.io/61c0f1122457b9b586c292c174185e5e87f9487ebe2f4bd5e8f9eeaf3d2be42e-uuid-159ea1e0-8c96-281d-80fd-bbe31193f836.png" />

<Callout icon="📘" theme="info">
  **Note**

  The Received tab does not display the source project of Release Bundles v2 that were [created](/governance/docs/create-release-bundles-v2) within the scope of a specific [project](/projects/docs/projects).
</Callout>