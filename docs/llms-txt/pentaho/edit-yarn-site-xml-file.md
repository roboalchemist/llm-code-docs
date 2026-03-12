# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-cloudera-cluster/edit-the-configuration-files-for-users-cloudera/edit-yarn-site-xml-file.md

# Edit YARN site XML file

If you are using YARN, you must verify that the following parameters are set in the `yarn-site.xml` file.

Perform the following steps to edit the `yarn-site.xml` file:

1. Navigate to the `*&lt;username&gt;*/.pentaho/metastore/pentaho/NamedCluster/Configs/*&lt;user-defined connection name&gt;*` directory and open the `yarn-site.xml` file.
2. Add the following values:

   | Parameter                              | Value                                                                                        |
   | -------------------------------------- | -------------------------------------------------------------------------------------------- |
   | **yarn.application.classpath**         | Add the classpaths you need to run YARN applications. Use commas to separate multiple paths. |
   | **yarn.resourcemanager.hostname**      | Change to the hostname of the resource manager in your environment.                          |
   | **yarn.resourcemanager.address**       | Change to the hostname and port for your environment.                                        |
   | **yarn.resourcemanager.admin.address** | Change to the hostname and port for your environment.                                        |
3. Save and close the file.
