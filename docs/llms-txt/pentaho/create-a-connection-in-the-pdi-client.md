# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/use-a-pentaho-repository-in-pdi/create-a-connection-in-the-pdi-client.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi/create-a-connection-in-the-pdi-client.md

# Create a connection in the PDI client

To access the repository items through the PDI client, perform the following steps to create a connection to a Pentaho Repository:

1. Verify the Pentaho Server is running, and then start the PDI client.
2. Click **Connect** in the upper right corner of the PDI client toolbar.

   The **Repository Manager** dialog box opens.

   **Note:** If **Connect** is replaced by a different link name, you are already connected to a repository.
3. Click **Add**.
4. Select from the following options:
   * **Pentaho Repository** - Uses a central environment through the Pentaho Server to store transformations, jobs, and schedules. This is the recommended repository to be used.
   * **File Repository** - Uses your local file system to store the metadata.
   * **Database Repository** - Uses a central relational database to store your ETL metadata.**Note:** Database and file repositories are not supported or recommended for production use.
5. Enter or update the **Display Name** property.
6. Modify the URL associated with your repository, if necessary.
7. (Optional) Provide description in the **Description** field.
8. Click **Save** to create repository.

   The repository is created and is listed in the Repository Manager dialog box.

You can either click **Connect**, to connect to the repository, or click **Close** to close the dialog box. If you chose to connect, see [Connect to a Pentaho Repository](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi/connect-to-a-pentaho-repository) and follow the procedure from step 2.

If you choose to close, you can connect to the repository later through the menu next to the **Connect** link in the upper right corner of the PDI client toolbar.
