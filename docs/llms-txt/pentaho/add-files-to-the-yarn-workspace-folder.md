# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/advanced-topics/copy-files-to-a-hadoop-yarn-cluster/add-files-to-the-yarn-workspace-folder.md

# Source: https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/advanced-topics/copy-files-to-a-hadoop-yarn-cluster/add-files-to-the-yarn-workspace-folder.md

# Add files to the YARN Workspace folder

These instructions explain how to configure the Start a PDI Cluster on YARNentry so that following files are copied at runtime, to the **YARN Workspace** folder and then to the YARN cluster: `kettle.properties`, `shared.xml`, and `repositories.xml`. These instructions also explain how to manually copy additional files to the folder.

If the job is run from your local installation, the configuration files from your `KETTLE_HOME` directory are copied to the `YARN Workspace`folder. If the job is scheduled or is run on a Pentaho Server, the configuration files from the server's configured `KETTLE_HOME` are copied to the `YARN Workspace` folder.

Complete these steps:

1. Set the active YARN Hadoop cluster using the instructions found in [Configuring Pentaho for Your Hadoop Distro and Version](http://wiki.pentaho.com/display/BAD/Configuring+Pentaho+for+your+Hadoop+Distro+and+Version).
2. Complete the instructions in the [Additional Configuration for YARN shims](http://wiki.pentaho.com/display/BAD/Additional+Configuration+for+YARN+Shims) article.
3. In Spoon, create or open a job that contains the Start a YARN Kettle Cluster entry.
4. Open the Start a PDI Cluster on YARN entry.
5. Select any combination of the `kettle.properties`, `shared.xml`, and `repository.xml`checkboxes in the **Copy Local Resource Files to YARN** section of the window.
6. Save and close the Start a PDI Cluster on YARN entry.
7. If you want to copy other files to the cluster, manually copy them to the `YARN Workspace` folder here: `pentaho-big-data-plugin/plugins/pentaho-kettle-yarn-plugin/workspace`.
8. Save and run the job.

At runtime, the `kettle.properties`, `shared.xml`, and `repositories.xml` files (whatever was selected) are copied to the `YARN Workspace` folder and then to the YARN cluster.
