# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-cloudera-data-platform/edit-configuration-files-for-users-cdp/edit-yarn-site-xml-file-cdp.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-cloudera-data-platform/edit-configuration-files-for-users-cdp/edit-yarn-site-xml-file-cdp.md

# Edit YARN site XML file

If you are using YARN, you must verify that the following parameters are set in the `yarn-site.xml` file.

Perform the following steps to edit the `yarn-site.xml` file:

1. Navigate to the `*&lt;username&gt;*/.pentaho/metastore/pentaho/NamedCluster/Configs/*&lt;user-defined connection name&gt;*` directory and open the `yarn-site.xml` file.
2. Add the following values:

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Parameter</td><td>Value</td></tr><tr><td><strong>yarn.application.classpath</strong></td><td>Add the classpaths you need to run YARN applications. Use commas to separate multiple paths.</td></tr><tr><td><strong>yarn.resourcemanager.hostname</strong></td><td>Change to the hostname of the resource manager in your environment.</td></tr><tr><td><strong>yarn.resourcemanager.address</strong></td><td>Change to the hostname and port for your environment.</td></tr><tr><td><strong>yarn.resourcemanager.admin.address</strong></td><td>Change to the hostname and port for your environment.</td></tr><tr><td><strong>yarn.resourcemanager.proxy-user-privileges.enabled</strong></td><td><p>Add this property if you are using a proxy user for security.```xmlyarn.resourcemanager.proxy-user-privileges.enabledtrue</p><pre><code>
&#x3C;/td>&#x3C;/tr>&#x3C;/tbody>
&#x3C;/table>3.  Save and close the file.

</code></pre></td></tr></tbody></table>
