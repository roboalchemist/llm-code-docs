# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/use-a-pentaho-repository-in-pdi/manage-repositories-in-the-pdi-client.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi/manage-repositories-in-the-pdi-client.md

# Manage repositories in the PDI client

After a repository is created, a menu appears next to the **Connect** link. You can use the menu to connect to any repository you created. If you connect to a repository, the **Connect** link in the PDI client toolbar is replaced by your user name and the display name of the repository.

This menu can also be used to access the Repository Manager or disconnect from your current repository.

## Repository Manager

You can **Add**, **Edit**, or **Delete** your repositories through the Repository Manager dialog box.

![Repository Manager dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-0e11da904b1a05a687555fd9d40bacff3565e7ec%2FssPDIRepository_Manager_9.4.png?alt=media)

If you set a repository as the default on startup, you can clear this behavior by checking **Launch connection on startup** again.

You can also click on an item in the list to select it. Once selected, you can either **Edit** or **Delete** that repository. If you choose **Edit**, the Connection Details dialog box will appear.

## Connection details

Use the Connection Details dialog box to specify the settings of your repository.

| Setting                          | Description                                                                                                                                                                                        |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Display Name**                 | Identifies the repository within the PDI client.                                                                                                                                                   |
| **URL**                          | Defines the web address of the repository. The default value is `http://localhost:8080/pentaho`. You can change this setting to any web address pertaining to your specific collaboration project. |
| **Description**                  | Describes the repository, such as its type and any other useful information.                                                                                                                       |
| **Launch connection on startup** | Indicates the repository should open by default when starting the PDI client.                                                                                                                      |
