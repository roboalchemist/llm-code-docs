# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/use-version-history-cp.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/use-version-history-cp.md

# Use version history

Retaining a [repository](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi) version history enables you to show what is different from one version to another, or to restore a previous version if you want to revert back to a specific point in time. By default, each time you save in PDI, a version of your file is committed to the repository.

## Use version history

Versions of a file can be tracked through the Repository Explorer in the PDI client (Spoon). These versions are listed in a tab of the explorer.

To access this version history tab:

1. In the PDI client menubar, go to **Tools** > **Repository** > **Explore**.

   The Repository Explorer window opens to the **Browse** tab.
2. In the left navigation panel of the **Browse** tab, locate and click on a folder to access the file containing your transformation or job.
3. Select your file when it appears in the upper right panel. The versions of this file are shown under the **Version History** tab in the lower right panel.

   ![Version History tab, Repository explorer window](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-faff923279154658ca2f5dc63d2e80c68a6cd7ce%2FssPDIRepository_ExplorerVersionHistoryTab.png?alt=media)

   You can use this history to:

   * [Open a version of a file](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/broken-reference)
   * [Restore a version of a file](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/broken-reference)\
     While saving a file, you are prompted to provide comments. These comments are also included in the **Version History** tab.

   This tab appears in the explorer when version history tracking is enabled. The tab is hidden with tracking is disabled. You can enable or disable tracking of version history and comments through a properties file. See [Enable or disable tracking of version history and comments](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/broken-reference) for more details.

## Open a version of a file

If you want to show differences between each version or you need to remember the details of previous changes, you can open it through the **Version History** tab.

To open a version of a file:

1. Right-click on a version under the **Version History** tab in the Repository Explorer.
2. Choose **Open** to access that version in the PDI client.

It opens as a separate file with the same name but the version number is added to the title on the PDI client canvas tab. If the current version of the file is already open in the PDI client, the latest version number is appended to its title.

## Restore a version of a file

If you do not like a change you made to your file, you can choose to restore to a previous version based on your descriptive comments. You must have administrator privileges to restore a version of a file.

1. Right-click on a version under the **Version History** tab in the Repository Explorer.
2. Select **Restore**.

   ![Restoring a file](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-cb63625056510388872630fd4d87a1ff713903bc%2FssPDIRestoring_a_Previous_Version.png?alt=media)
3. Follow the remaining prompts and click **OK**.

The restored version becomes the latest version of your file. The next time you open the file, you will see the restored version as the most recent one along with all the previous versions.

![Restoring a file result](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-36c26ec28d09c0cdd73f92284cd73b3daddfe7c0%2FssPDIResults_of_Restoring_a_Previous_Version.png?alt=media)

## Enable or disable tracking of version history and comments

You can enable or disable tracking of version history or comments for all users by modifying the **versioningEnabled** and **versionCommentsEnabled** fields within the `server/pentaho-server/pentaho-solutions/system/repository.spring.properties` text file:

| Action (All Users)           | Status                        | Final Setting                  |
| ---------------------------- | ----------------------------- | ------------------------------ |
| **Version History Tracking** | Off                           | `versioningEnabled=false`      |
| On                           | `versioningEnabled=true`      |                                |
| **Comment Tracking**         | Off                           | `versionCommentsEnabled=false` |
| On                           | `versionCommentsEnabled=true` |                                |

When you disable version history tracking, comments are automatically no longer tracked.

To enable or disable tracking:

1. Exit the PDI client.
2. Stop the Pentaho Server.
3. Open the `server/pentaho-server/pentaho-solutions/system/repository.spring.properties` file in a text editor.
4. Change the fields to enable or disable either version history or comment tracking.
5. Start the Pentaho Server.
6. Start the PDI client.
