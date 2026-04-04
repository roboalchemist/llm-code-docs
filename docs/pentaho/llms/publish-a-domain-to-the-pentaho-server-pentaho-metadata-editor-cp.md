# Source: https://docs.pentaho.com/pba-metadata-editor/publish-a-domain-to-the-pentaho-server-pentaho-metadata-editor-cp.md

# Source: https://docs.pentaho.com/pba-metadata-editor/pdia-9.3-metadata-editor/publish-a-domain-to-the-pentaho-server-pentaho-metadata-editor-cp.md

# Source: https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/publish-a-domain-to-the-pentaho-server-pentaho-metadata-editor-cp.md

# Publish a domain to the Pentaho Server

You can share an XML representation of your domain with a Pentaho solution that your Pentaho Server recognizes, so that the server can access the metadata domain and its contents.

The implementation of metadata in the Pentaho Server requires that you follow some basic rules:

* There can only be one metadata domain per Pentaho solution.
* The metadata domain is associated with the solution by placing the XML format of the domain in the root directory of the solution.
* The domain XML file must be `[myBusinessModel].xmi`, where `[myBusinessModel]` is any name you want to give the model.

You can accomplish this by using the Pentaho Metadata Editor Publish feature, or you can [export your domain file](https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/get-started-with-pentaho-metadata-editor-cp/importing-and-exporting-domains#export-a-domain) and copy it manually to the solution repository folder associated with the solution.

Once you have published a model, it becomes available as a public data source, unless you add [security](https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/metadata-security-pentaho-metadata-editor-cp) to the metadata business objects. Published models appear as data sources for these Pentaho design tools and components:

* Report Designer
* Interactive Reports
* Dashboard Designer

## Before you begin

Before you publish a domain make sure you have this information available:

* The user name and password for the Pentaho Server. The default user name is admin.
* The base URL for your Pentaho Server. This consists of all URL information up to and including the Web application context. For example, the base URL of the Pentaho demo server is `http://localhost:8080/pentaho`. For publishing, you must append the base URL with the name of the publish service. The default is `http://localhost:8080/pentaho/plugin...etadata/import`. This is the value you must use, unless your server administrator has changed the service name.
* The solution to which you want to publish the domain. For example, the Pentaho demo server ships with two different solutions, the Samples solution and the Steel Wheels solution. No slashes are required.

## Make a model available as a data source

After you have created a domain with at least one model using the Metadata Editor, you can make it appear in the data source lists for the User Console and client tools by publishing the model to the Pentaho Server. Save the model before you try to publish it.

1. In the Pentaho Metadata Editor go to **File** > **Publish to Server**.

   The Publish to Server dialog box appears.

   ![Publish to Server dialog box](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-df42498f6bfeecd6cdbbbb87084e497161300340%2Fpublish.png?alt=media)
2. Enter the **Web Publish URL**, which is the Pentaho Server base URL followed by the publish service name.

   RepositoryFilePublisher is the default.
3. Enter the **Server Userid**.

   The default is admin.
4. Enter the **Server Password**.

   The default is password.
5. Enter the **Domain Name**, which is the domain name of the solution to which you want to publish.
6. Click **OK** to save and exit the dialog box.

The model is saved to the Pentaho Server in the solution repository as an XMI file. If this file already exists, you are prompted to overwrite it.

<br>
