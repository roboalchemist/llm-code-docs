# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-repository/set-pdi-version-control-and-comment-tracking-options.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/manage-the-pentaho-system/manage-the-pentaho-repository/set-pdi-version-control-and-comment-tracking-options.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-repository/set-pdi-version-control-and-comment-tracking-options.md

# Set PDI version control and comment tracking options

Pentaho Data Integration (PDI) can track versions and comments for jobs, transformations, and connection information when you save them. You can turn version control and comment tracking on or off by modifying their related statements in the `repository.spring.properties` text file.

**Note:** By default, version control and comment tracking are disabled (set to false).

## Editing the version control statement

1. Exit from the PDI client (also called Spoon).
2. Stop the Pentaho Server.

   See the **Install Pentaho Data Integration and Analytics** document for instructions on starting and stopping the Pentaho Server..
3. Open the `pentaho-server/pentaho-solution/system/repository.spring.properties` file in a text editor.
   * To enable version control: Edit the **versioningEnabled** statement and set it to: `true`

     ```
     versioningEnabled=true
     ```
   * To disable version control: Edit the **versioningEnabled** statement and set it to: `false`

     ```
     versioningEnabled=false
     ```

     **Note:** If you disable version control, comment tracking is also disabled.
4. Save and close the file.
5. Start the Pentaho Server.

   See the **Install Pentaho Data Integration and Analytics** document for instructions on starting and stopping the Pentaho Server..
6. Start the PDI client.
7. Verify that version control is set as you intended.

### Verifying the version control option

1. Connect to the Pentaho Repository.
2. In the PDI client, click **Tools** > **Explore**.
3. In the Repository Explorer window, click on the **Browse** tab, then click on a file name.
4. Verify that version control is enabled or disabled:
   * **Enabled**

     You can see the **Access Control** tab, and the **Version History** tab is visible.

     ![Version History tab in the PDI client](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-914cd4a0febbba7a039c29aa67aa35ddbeb307c2%2FAccess_Tab_-_With_History_001.png?alt=media)
   * **Disabled**

     You can see the **Access Control** tab, but the **Version History** tab is hidden.

     ![Access Control tab in the PDI client](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-ff0ac1c2d6301db72faf421538dfabcbe24b21b2%2FAccess_Tab_-_No_History_002.png?alt=media)

## Editing the comment tracking statement

1. Exit from the PDI client (also called Spoon).
2. Stop the Pentaho Server.
3. Open the `pentaho-server/pentaho-solution/system/repository.spring.properties` file in a text editor.
   * To enable comment tracking: Edit the **versionCommentsEnabled** statement and set it to `true`.

     ```
     versionCommentsEnabled=true
     ```
   * To disable comment tracking: If you want version control, but not comment tracking:

     * Edit the **versioningEnabled** statement and set it to `true`.
     * Edit the **versionCommentsEnabled** statement and set it to `false`.

     ```
     versioningEnabled=true
     versionCommentsEnabled=false
     ```
4. Save and close the file.
5. Start the Pentaho Server.
6. Start the PDI client.

Verify that Version Control and Comment Tracking are set as you intended.

### Verifying the comment tracking option

1. Connect to the Pentaho Repository.
2. In the PDI client, click **Tools** > **Explore**.
3. In the Repository Explorer window, click on the **Browse** tab, then click on a file name.
4. Verify that comment tracking is enabled or disabled:
   * **Enabled**

     The **Version History** tab appears with the **Comments** field. When you save a transformation, job, or connection information, you are prompted to enter a comment.

     ![Version History tab showing the Comments column in the PDI client](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-fb81a70911dbe9ebf1d6a5d0eef6177db3f8bc78%2FComment_Field_Enabled_-_003.png?alt=media)
   * **Disabled**

     The **Version History** tab appears and the **Comment** field is hidden. When you save a transformation, job, or connection information, you are no longer prompted to enter a comment.

     ![Version History tab with the Comments column hidden in the PDI client](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-c7c3305c28d3af0404125b03c7f6c0e17ffd4d38%2FComment_Field_Hidden_-_004.png?alt=media)
