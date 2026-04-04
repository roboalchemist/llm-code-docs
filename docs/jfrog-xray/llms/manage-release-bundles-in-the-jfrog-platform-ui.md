# Source: https://docs.jfrog.com/artifactory/docs/manage-release-bundles-in-the-jfrog-platform-ui.md

# Manage Release Bundle Retention Policies in the JFrog Platform UI

<Callout icon="📘" theme="info">
  **Subscription Information**

  This feature is supported with the **Enterprise+** license.
</Callout>

<Callout icon="❗️" theme="error">
  **Important**

  This section describes how to manage Release Bundles v1. For information about managing Release Bundles v2, which were introduced in Artifactory 7.63.2 and Distribution 2.19.1, see <Anchor label="Release Lifecycle Management" target="_blank" href="/governance/docs/release-lifecycle-management">Release Lifecycle Management</Anchor>.
</Callout>

If the retention policies feature has been [enabled](/docs/manage-release-bundle-retention-and-cleanup), navigating to the **Received** tab displays a **Cleanup** button (available only to admin users), which opens a Cleanup Candidates window, where you can now do the following:

* [Set a Release Bundle to Keep or Don't Keep](#set-a-release-bundle-to-keep-or-dont-keep)
* [Clean up (i.e., delete) Release Bundles that meet the retention policies](#clean-up-release-bundles-from-edge-nodes)

In addition to automated retention and cleanup using REST APIs, you can manage Release Bundles in the JFrog platform UI using the **Distribution > Release Bundles > Received** tab.

## Set a Release Bundle to Keep or Don't Keep

The Platform UI provides an easy-to-use interface that lets you determine which Release Bundles (v1 & v2) should be deleted and which should be kept, regardless of whether that Release Bundle meets the deletion criteria (see Cleaning up Artifactory Edge Release Bundles). You can also access the Cleanup History tab from this space (see Cleanup History Tab).

1. Go to the **Received** tab and click the **Cleanup** button.

   <Image align="center" alt="180127966.png" border={false} width="70% " src="https://files.readme.io/04da38e6348895de8360db67ded21e3a55cd98e7748532981a082099028af25b-uuid-00ef7174-233b-adbf-2504-b22388484550.png" />

   This displays the Cleanup Candidates window, which is comprised of two tabs: **By Days** and **By Versions**.

<Callout icon="📘" theme="info">
  **Note**

  The two tabs in the Cleanup Candidates provide you with the same functionality for the purpose of cleaning up the Release Bundles. You can choose to work in either tab depending on your preference: days or versions.

  You can also search for a specific Release Bundle using the name or a wildcard + name in the search field.
</Callout>

<Image align="center" alt="180127965.png" border={false} width="70% " src="https://files.readme.io/4e879eab4668d0ebe7f775cd3a3d0c8c4875c3424d390db6e64fd1af854a8814-uuid-8e27ae3f-0dde-e68f-00e1-f9c9a4848fba.png" />

<Callout icon="📘" theme="info">
  **Note**

  The Release Bundles that are currently marked to keep show a **closed lock** in the Keep column while those that can be deleted show an **open lock**.

  By default, the checkbox to show the kept items (so that you don't try to inadvertently delete a Release Bundle that is marked Keep) is selected.
</Callout>

2. To change a Release Bundle's status from **Don't Keep** to **Keep** (or from **Keep** to **Don't Keep**), click the lock or unlock icon in the Keep column. Note that standing on the lock/unlock icon displays a tooltip that tells you the current status of the Release Bundle.

3. Once you have set the Release Bundles to their correct status, click **Continue**.

4. You can now continue to deleting Release Bundles, or go to the **Cleanup History** tab to view your changes.

<Callout icon="📘" theme="info">
  **Note**

  Any changes you make to the Release Bundle's status will be automatically noted as an action in the Cleanup History tab and you will not be asked to confirm them.
</Callout>

## Clean up Release Bundles from Edge Nodes

1. To clean up (delete) Release Bundles (v1 & v2) from Distribution Edge nodes, go to **Distribution > Release Bundles** and select the **Received** tab.

2. Select one of the tabs in the Cleanup Candidates window (By Days or By Versions).

<Callout icon="📘" theme="info">
  **Note**

  The two tabs of the Cleanup Report provide you with the same functionality for the purpose of cleaning up the Release Bundles. You can choose to work in either tab depending on your preference: search for Release Bundles according to the number of days that the Release Bundle has been released (time) or according to the version of the release bundle.

  You can also search for a specific Release Bundle using the name or a wildcard + name in the **search** field.
</Callout>

3. In the **Name** column, select the checkboxes of the Release Bundles you wish to delete.

<Callout icon="📘" theme="info">
  **Note**

  You will only be able to select the checkboxes of Release Bundles that are marked **Don't Keep**. Items marked for keeping will appear grayed-out.
</Callout>

<Image border={false} src="https://files.readme.io/e7f1bbdd735d9e871f69b271c64a09f3f6acb9f106e5a35294bb20108c445b43-uuid-bc7177d1-db3e-1b32-2fb7-67ac3eb657db.png" />

4. Click **Continue**.
5. Any Release Bundles you delete through the UI cannot be retrieved. This operation is permanent and **cannot** be undone. Therefore, you will now need to verify your selection, and confirm the deletion by clicking **Delete** in the Confirm Release Bundle Deletion popup.

<Callout icon="📘" theme="info">
  **Note**

  Sometimes simply selecting a Release Bundle for deletion - even if it meets the deletion criteria - does not always mean the Release Bundle will be deleted. Because this operation is asynchronous, there might be situations where items you selected to delete are no longer available or cannot be deleted for other reasons.

  In this case, a Deletion Failure window will be displayed instead. You will need to go back to the list of Release Bundles and clear the selection of those that cannot be deleted.

  Once your selection is approved and confirmed, the deletion process will begin, and you will receive a notification that the process has begun.
</Callout>

6. Once the deletion process is completed, you can view the results of your actions in the **Cleanup History** tab. As explained above, this operation is asynchronous, and may take some time depending on the amount of bundles and artifacts that are being deleted.

<Callout icon="📘" theme="info">
  **Note**

  If an artifact is included in more than one Release Bundle, when you delete a Release Bundle that contains that artifact, the artifact will remain via the remaining Release Bundle.
</Callout>

### Best Practice

For the best performance of the clean-up process, it is recommended to bulk Release Bundles into smaller groups and to delete a group at a time.

## Cleanup History Tab

Use the **Cleanup History** tab to view the changes you apply to Release Bundles through the Cleanup Report, including deletions, and status changes from Keep to Don’t Keep or from Don't Keep to Keep.

<Image alt="180127975.png" border={false} src="https://files.readme.io/e2e2638d3861b5f61acc992ac548b2825bde656725666ead5892e7817a04fc13-uuid-7f9505e8-aee0-f753-e51a-9fef8b5e488d.png" />

<Callout icon="📘" theme="info">
  **Note**

  Release Bundle v1 deletions from the source Artifactory using JFrog Distribution will not be listed here.
</Callout>

The columns in this history tab can be sorted, and you can paginate through the complete list of actions taken.