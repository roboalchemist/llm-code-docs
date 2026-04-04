# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/use-a-pentaho-repository-in-pdi/unsupported-repositories.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi/unsupported-repositories.md

# Unsupported repositories

You can also create either a database repository (which uses a central relational database to store your ETL metadata) or a file repository (which uses your local file system to store the metadata). You can create these types of repositories through the **Other Repositories** link in the Pentaho Repository welcome dialog box.

From the Other Repositories dialog box, you can **Get Started** by selecting either the **Database Repository** or the **File Repository** from the list.

**Note:** Database and file repositories are not supported or recommended for production use.

## Database repository

Similar to the Pentaho Repository, you connect to the database repository by entering a **Display Name** into the Connection Details dialog box. After specifying a name, you need to select **Database Connection**, which leads to a list in the Select a database connection dialog box. From this dialog box, you can either create a new database, or **Edit** and **Delete** an existing connection. When you create a new connection or **Edit**, the Database Connection dialog box appears. Use this dialog box to specify your database connection, then select **Test** and click **OK**. In the Select a database connection dialog box, click on what database connection you want to use and then go **Back** to the Connection Details dialog box. After **Display Name** and the **Database Connection** are specified, click **Finish** to test the connection to repository.

## File Repository

Besides entering in a **Display Name**, you will need to specify the **Location** of the local file system that you want to use as a file repository. You can **Browse** to this location from the Connection Details dialog box. After you specify a repository name and file system location, you can click **Finish** to test the connection. Unlike with other repositories, when you connect to a file repository, the link in the upper right corner will only show the display name of file repository.
