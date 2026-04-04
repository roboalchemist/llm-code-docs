# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/install-jdbc-driver-as-a-module-in-jboss/step-6-remove-jndi-resource-references-in-jboss.md

# Step 7: Remove JNDI resource references in JBoss

Because JBoss has its own mechanism for referencing JNDI data sources, the **resource-ref** entries in the `web.xml` file located in the `pentaho.war` are not needed.

You must remove these **resource-ref** entries for the Pentaho Repository to operate properly.

1. Navigate to the `pentaho/server/pentaho-server/<your jboss installation directory>/standalone/deployments` directory.
2. Use a ZIP extraction utility (such as 7-Zip, WinZip, or Archive) to view the contents of the `pentaho.war` file. Do not unzip or extract the contents of the file.
3. Navigate to the `WEB-INF` directory and open the `web.xml` file in a text editor.
4. Delete all **\<resource-ref>** tagged entries including everything between the **\<resource-ref>** and **\</resource ref>** tags.
5. Save and close the file.
6. The ZIP extraction utility that you used might show a prompt that asks whether you would like to update the file in the `pentaho.war` archive. If this prompt appears, confirm that you would like to update the file.
