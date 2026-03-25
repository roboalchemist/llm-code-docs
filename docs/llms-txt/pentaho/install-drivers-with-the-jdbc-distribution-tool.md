# Source: https://docs.pentaho.com/install/9.3-install/jdbc-drivers-reference/install-drivers-with-the-jdbc-distribution-tool.md

# Source: https://docs.pentaho.com/install/10.2-install/jdbc-drivers-reference/install-drivers-with-the-jdbc-distribution-tool.md

# Install drivers with the JDBC distribution tool

To connect to a database, including the Pentaho Repository database, you will need to download and install a JDBC driver to the appropriate places for Pentaho components as well as on the the web application server that contains the Pentaho Server.

Perform the following steps to download a JDBC driver and install the JDBC driver using the JDBC Distribution Tool.

**Note:** Due to licensing restrictions, Pentaho cannot redistribute some third-party database drivers. You must download the file yourself and install it yourself.

1. Download a [JDBC driver](https://docs.pentaho.com/install/10.2-install/jdbc-drivers-reference) JAR from your database vendor or a third-party driver developer.
2. Copy the JDBC driver JAR you just downloaded to the `pentaho/jdbc-distribution` directory.
3. Open a cmd prompt or shell tool, navigate to the `pentaho/jdbc-distribution` directory and enter one of the following:
   * Windows:

     `distribute-files.bat <name of JDBC driver JAR>`
   * Linux:

     `./distribute-files.sh`
4. If you have run this utility as part of the installation process, you are done. Proceed to the next step of the installation instructions.
5. If you have run this utility so that you can connect to a new repository, restart the Pentaho Server and design tools, then try to connect to the new repository. If you cannot connect, verify that the drivers are installed as shown in the table below. Restart your Pentaho Server and client tools.

   |List of Products and Corresponding Locations for JDBC Drivers|\
   |Server or Design Tool|Directory|\
   \|-------------------------------------------------------------|\
   \|---------------------|---------|\
   |Pentaho Server|`pentaho/server/pentaho-server/tomcat/lib`|\
   |Pentaho Data Integration (Spoon)|`pentaho/design-tools/data-integration/lib`|\
   |Pentaho Report Designer (PRD)|`pentaho/design-tools/report-designer/lib/jdbc`|\
   |Pentaho Aggregation Designer (PAD)|`pentaho/design-tools/aggregation-designer/drivers`|\
   |Pentaho Schema Workbench (PSW)|`pentaho/design-tools/schema-workbench/drivers`|\
   |Pentaho Metadata Editor (PME)|`pentaho/design-tools/metadata-editor/libext/JDBC`|
