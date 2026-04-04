# Source: https://docs.jfrog.com/artifactory/docs/export-and-import-release-bundles-v1-in-the-ui.md

# Export and Import Release Bundles (v1) in the UI

The following topics describe how to use the platform UI to export and import Release Bundles v1:

* [Export a Release Bundle (v1) Version in the UI](/docs/export-and-import-release-bundles-v1-in-the-ui#export-a-release-bundle-v1-version-in-the-ui) I
* [Import a Release Bundle (v1) Version in the UI](/docs/export-and-import-release-bundles-v1-in-the-ui#import-a-release-bundle-v1-version-in-the-ui)

## Export a Release Bundle (v1) Version in the UI

In Distribution, you export the Release Bundle version as a downloadable `.zip` file and then proceed to download the archived Release Bundle from the Actions list on the Distributable page.

<Callout icon="📘" theme="info">
  **Release Bundle Export Rules and Guidelines**

  * Only a signed Release Bundle labeled as **Ready** can be exported.
  * Only a single Export archived file can be exported as Release Bundles are immutable.
  * Exporting Release Bundles requires the  <Anchor label="Distribute Bundles Permission" target="_blank" href="/administration/docs/permissions">Distribute Bundles Permission</Anchor>.
</Callout>

To export a Release Bundle version from the Source Artifactory instance:

1. From the Application module, navigate to **Distribution** > **Release Bundles** > **Distributable**.

2. Create and sign a Release Bundle.

   Wait for the Release Bundle state to change to **Ready**.

3. Navigate to the Release Bundle version you wish to export, and select **Export Version** from the **Version Actions** list.

   <Image align="center" alt="export_RB_Version_action.png" border={false} width="50% " src="https://files.readme.io/c3f7c0c1fd801330b29cd2de48fbfc5fe6f31cb487a4cc08b1194550382f6492-uuid-20435601-de33-1ab1-d9fa-9c86014ecfbf.png" />

   Note that this process may take a few minutes.

4. From the **Version Actions** list, select **Download Version**.

   <Image align="center" alt="airgap_download_exported_RB.png" border={false} width="50% " src="https://files.readme.io/9765a5256c19caed388415d43503d5bdbfecf40ab8f3d5b3d6f5412a7759da69-uuid-aacc1b98-5099-507a-c877-94cb76bfce72.png" />

   You can download the `<Release Bundle Name>.zip`file to your local drive.

<Callout icon="📘" theme="info">
  **Deleting an Exported Version**

  After the Export process has completed, the **Delete Exported File** action is displayed in the **Version Actions** list.
</Callout>

5. Copy the download `<Release Bundle Name>.zip` file to an external device (such as a hard drive or USB flash drive).

## Import a Release Bundle (v1) Version in the UI

<Callout icon="📘" theme="info">
  **Note**

  Importing Release Bundles requires Admin permissions.
</Callout>

To import a Release Bundle on the target Artifactory instance:

1. Access the target Artifactory and copy the `<Release Bundle Name>.zip` to the local machine.
2. From the **Application** module, navigate to the **Release Bundles** > **Distribution** > **Received**.

   <Image align="center" alt="DIST_RB_Received.png" border={false} width="70% " src="https://files.readme.io/32c1a4ccdeca5212830230eb07e0d17d52fcdb65b369dcecb8e30f475aec7ba8-uuid-eeca1214-2874-1d43-161e-17deadd50e38.png" />
3. Click **+** **Import**.

   This displays the Import Release Bundle dialog.
4. You can now select an import file using one of the following methods:

   1. Import directly from your local drive using the **Files** option.

      <Image align="center" alt="import_RB_Edge.png" border={true} width="40% " src="https://files.readme.io/c957311e987ca42e1fcfcf2f26bb759599b5bb89e3deeab362df32701e878985-uuid-ed6e7dc3-2be4-ea91-e63d-bdf27867b962.png" className="border" />

   2. Import the Release Bundle from a predefined path location.

      Prerequisite: Save your Release Bundle in the root of your user-defined `ARTIFACTORY_HOME/var/data/artifactory/import/` folder.

      Note that as part of storage optimization, the file will automatically be deleted from the /imports folder after the Release Bundle has been successfully imported.

<Callout icon="📘" theme="info">
  **Importing Release Bundles in an HA Cluster Environement**

  In an HA environment, you have an option to save the exported Release Bundle on a different node in the cluster as long as the Release Bundle is saved in the root of the `/import` folder.
</Callout>

<Image align="center" border={true} width="40% " src="https://files.readme.io/bbb5572d937475181e5fc1a705a7f629136d792bf322e6a821cb7ba4552c3746-uuid-592967ea-4230-be2b-bba8-a5cc9e7ae5ba.png" className="border" />

5. Click **Import**. A progress bar displays the import process.

<Image align="center" alt="advance bar for importing RB.png" border={true} width="30% " src="https://files.readme.io/49bc54c654cd9e455d3c5d6c0ca7aac326e6ff721cbc496b47dd610c12dc5c2c-uuid-85e174b1-fe60-d20a-ffc5-667d71f40b2a.png" className="border" />

The imported Release Bundle is added to the **Received** tab.