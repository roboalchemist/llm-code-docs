# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-publish-model-job-entry-for-sdr/use-the-publish-model-job-entry.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-publish-model-job-entry-for-sdr/use-the-publish-model-job-entry.md

# Use the Publish Model job entry

This task assumes you are in the job canvas in Pentaho Data Integration. You must have permissions to **Publish Content** and **Manage Data Sources** in the Pentaho Server in order to use this job entry. If you are using a data service as the source in your Build Model job entry, you must be connected to a Pentaho Repository to successfully publish your model.

Use this job entry to publish the data source created with the Build Model job entry.

1. In the **Design** tab, click the **Modeling** folder, and then double-click the Publish Model job entry. Alternatively, you can drag the job entry icon to the job canvas.

   ![Publish Model job entry](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-874f4b0740caf548b47c7727e3c7885ca735153c%2FSDR_PublishModel_Icon.png?alt=media)
2. Double-click the **Publish Model** icon to open the Publish Model dialog box.
3. Enter a name for the entry in the **Entry name** field.
4. (Optional) Select the **Replace Existing Published Model** check box to overwrite an existing Data Source Wizard data source and database connection.

   **Note:** To successfully complete an SDR job, it is recommended that you select this check box. If this check box is cleared and you attempt to publish a model with the same name, the Publish Data Source job entry will fail.
5. Fill in or edit the fields in the **Pentaho Server Connection** section and then test your connection:

   | Option              | Description                                                                                                                                                                                                                                                        |
   | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | **URL**             | The base URL string used to connect to the server.                                                                                                                                                                                                                 |
   | **User Name**       | The user name required to access the server.                                                                                                                                                                                                                       |
   | **Password**        | The password associated with the provided user name which is passed during the authentication process.                                                                                                                                                             |
   | **Test Connection** | Click to test the connection to the Pentaho Server using the information provided in the above fields. When you click this button, the system will also check that the associated user is granted the **Publish Content** and **Manage Data Sources** permissions. |
6. Fill in or edit the fields in the **Share** section:

| Field               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Grant Access To** | <p>Grant access to the data model to everyone, specific users, or specific roles.</p><p>The permission granted is read-only. From the drop-down menu, you can select <strong>Everyone</strong>, <strong>User</strong>, or <strong>Role</strong>. If you select <strong>User</strong> or <strong>Role</strong>, the<strong>User/Role Name</strong> field is available.</p><p>You can use variables to populate this field. The variable can contain one of three values: everyone, user, or role. These values must be lower-case to work properly.</p> |
| **User/Role Name**  | Enter the name of the user or role who will have access to the model.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

7\. When finished, click \*\*OK\*\* to save your changes and close the dialog box, or click \*\*Cancel\*\* to discard your changes and close the dialog box.

This is an example of the Publish Model dialog box.

![Publish Model dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-9a738e969ace0a6fa3402c9dae3017e2b3a34d4a%2FSDR_PublishModel_db.png?alt=media)
