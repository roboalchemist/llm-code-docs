# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/embed-pentaho-server-functionality-into-web-applications/get-started-with-the-embedded-samples.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-pentaho-server-functionality-into-web-applications/get-started-with-the-embedded-samples.md

# Get started with the embedded samples

To download and deploy the samples to your Pentaho Server, perform the following steps:

1. On the [Support Portal](https://support.pentaho.com/home), sign in using the Pentaho support user name and password provided in your Pentaho Welcome Packet.
2. Click **Downloads**, then navigate to the Pentaho GA Release page, which matches your version of the software.
3. On the bottom of the Pentaho GA Release page, in the file component section, click the **SDK** folder and download the `pentaho-sdk- 10.2.0.zip` file.

   The readme file contains the information for deployment.
4. Stop the Pentaho Server.
5. Run **SDK** > **Installer.bat** (or the corresponding script for your OS) to uncompress these two folders to your selected location: `integration-examples` and `platform-plugins`.
6. Copy the `integration-examples` directory to your `pentaho-server/tomcat/webapps` directory.
7. Open the `platform-plugins` directory and copy the following two directories: `example-visualization` and `oem-tools`.
8. Paste the `example-visualization` and `oem-tools` directories into the `pentaho-server/pentaho-solutions/system` directory.
9. Restart the Pentaho Server.

The samples are deployed and can be accessed by opening a web browser and navigating to <http://localhost:8080/integration-examples>. If you want to access the OEM tools, browse to [http://localhost:8080/pentaho/conten...web/index.html](http://localhost:8080/pentaho/content/oem-tools/resources/web/index.html). If you want to access the example-visualization, look under the **Charts** menu in Analyzer. It will be listed as **Example KPI**.

To deliver content as well as expose various services, we use a REST web interface. These sections comment on the various samples and how they use the REST URLs. For the full reference of the Pentaho REST API, please refer to [http://javadoc.pentaho.com](http://javadoc.pentaho.com/).

**Note:** The REST APIs often allow interaction with repository files. The REST API expects references to repository files to be specified using the `:` character as file separator.
