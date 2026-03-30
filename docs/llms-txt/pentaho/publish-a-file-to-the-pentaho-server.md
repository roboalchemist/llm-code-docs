# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/embed-pentaho-server-functionality-into-web-applications/publish-a-file-to-the-pentaho-server.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-pentaho-server-functionality-into-web-applications/publish-a-file-to-the-pentaho-server.md

# Publish a file to the Pentaho Server

Follow this process if you want to publish a file to the Pentaho Server:

Click the link that publishes a file to the Pentaho Server: `http://localhost:8080/api/repo/publish/publishfile`. This publishes the file to the provided path in the repository. Note that the file will be overwritten if the overwrite flag is set to `true`.

| Name              | Description                                                                         | Type     | Default |
| ----------------- | ----------------------------------------------------------------------------------- | -------- | ------- |
| **pathId**        | (colon separated path for the repository file)                                      | formdata | false   |
| **fileContents**  | (input stream containing the data)                                                  | formdata | false   |
| **overwriteFile** | (flag to determine whether to overwrite the existing file in the repository or not) | formdata | false   |
| **fileInfo**      | (information about the file being imported)                                         | formdata | false   |

Sample code for reference purposes can be found at [Github for Pentaho](https://github.com/pentaho). Look for the file called `PublishRestUtil.java` under the **pentaho-reporting** repostitory.

The file is now published to the Pentaho Server and is available to users.
