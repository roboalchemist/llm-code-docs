# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/big-data-issues/use-yarn-with-s3.md

# Source: https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/big-data-issues/use-yarn-with-s3.md

# Use YARN with S3

When using the [Start a PDI cluster on YARN](https://pentaho-public.atlassian.net/wiki/spaces/EAI/pages/388312923/Start+a+PDI+Cluster+on+YARN) and [Stop a PDI cluster on YARN job](https://pentaho-public.atlassian.net/wiki/spaces/EAI/pages/388312925/Stop+a+PDI+Cluster+on+YARN) entries to run a transformation that attempts to read data from an Amazon S3 bucket, the transformation fails. The transformation fails because the Pentaho metastore is not accessible to PDI on the cluster. To resolve this problem, verify that the Pentaho metastore is accessible to PDI on the cluster.

Perform the following steps to make the Pentaho metastore accessible to PDI:

1. Navigate to the `<user>/.pentaho/metastore` directory on the machine with the PDI client.
2. On the cluster where the Yarn server is located, create a new directory in the `design-tools/data-integration/plugins/pentaho-big-data-plugin` directory, then copy the metastore directory into this location. This directory is the *\<NEW\_META\_FOLDER\_LOCATION>* variable.
3. Navigate to the `design-tools/data-integration` directory and open the `carte.sh` file with any text editor.
4. Add the following code in the line before the `export OPT` line: `OPT="$OPT -DPENTAHO_METASTORE_FOLDER=<NEW_META_FOLDER_LOCATION>"`, then save and close the file.
5. Create a zip file containing the contents of the `data-integration` directory.
6. In your Start a PDI cluster on YARN job entry, go to the **Files** tab of the Properties window, then locate the **PDI Client Archive** field. Enter the filepath for the zip file.

This task resolves S3 access issues for the following tranformation steps:

* Avro Input
* Avro Output
* Orc Input
* Orc Output
* Parquet Input
* Parquet Output
* Text File Input
* Text File Output
