# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/table-input/ael-considerations/connect-to-an-impala-database.md

# Connect to an Impala database

We support Impala versions 2.2.x. Before you can use the **Table Input** step to connect to an Impala database through AEL, you must download and install the Cloudera Impala driver.

**Note:** See the **Administer Pentaho Data Integration and Analytics** document for instructions on stopping and restarting rhe AEL daemon.

Perform the following steps to download and install the Cloudera Impala driver:

1. Stop the AEL daemon.
2. Go to <https://www.cloudera.com/>, select Downloads and click **Impala JDBC Driver Downloads**.
3. Select **Impala JDBC Connector 2.5.42** from the menu and follow the site's instructions for downloading.

   A ZIP file containing the Impala\_jdbc\_2.5.42 driver is downloaded.
4. Unzip the `impala_jdbc_2.5.42.zip` file to a local folder.

   The contents of the ZIP file are extracted to the folder. The unpacked contents include a documentation folder and two ZIP files. You only need the `ImpalaJDBC41-2.5.42.zip`.
5. Open the `ClouderaImpalaJDBC-2.5.42` folder and unzip the `ClouderaImpalaJDBC41_2.5.42.zip` file to a local folder.

   The associated JAR files are extracted from the ZIP file.
6. Copy all the JAR files, except `log4j-1.2.14.jar`, to the `pentaho/design-tools/data-integration/adaptive-execution/extra` folder.

   **CAUTION:**

   The `log4j-1.2.14.jar` file should not be copied as it is already present and will cause conflicts.
7. Save and close the file.

   The Cloudera Impala driver is installed.
8. Restart the AEL daemon.

You can now use the **Table Input** step to connect to an Impala database through AEL
