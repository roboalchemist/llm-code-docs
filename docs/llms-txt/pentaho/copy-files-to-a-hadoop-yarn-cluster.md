# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/advanced-topics/copy-files-to-a-hadoop-yarn-cluster.md

# Source: https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/advanced-topics/copy-files-to-a-hadoop-yarn-cluster.md

# Copy files to a Hadoop YARN cluster

If you start a job that will run on a YARN cluster, but it needs other files to execute (such as variables from your local copy of `kettle.properties`) those files will need to be copied to the YARN cluster. An easy way to do this is to add those files to the YARN Workspace folder. At runtime PDI copies all of the files in the **YARN Workspace**folder to the YARN cluster. This feature is well-suited for jobs that move through the development, testing, and staging lifecycle because the job uses the appropriate configuration files in the `KETTLE_HOME` directory for the environment in which it runs.

**CAUTION:**

Files in the **YARN Workspace** folder are copied to the YARN cluster every time you run a job that starts the YARN Kettle Cluster. If you don't want to overwrite files that have the same names that are already on the YARN Kettle Cluster, delete files from the **YARN Workspace** folder. Then, in the Start a PDI Cluster on YARN step window, deselect the appropriate checkboxes in the **Copy Local Resource Files to YARN** section of the window.
