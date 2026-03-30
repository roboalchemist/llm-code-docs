# Source: https://docs.pentaho.com/install/9.3-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp/update-the-default-documentation-version-link-post-upgrade-tasks.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp/update-the-default-documentation-version-link-post-upgrade-tasks.md

# Update the default documentation version link

The default URL of the online Pentaho documentation changes with each release. When upgrading, you may need to update this URL parameter in the `pentaho.xml` file.

1. Navigate to the `pentaho/server/pentaho-server/pentaho-solutions/system` directory and open the `pentaho.xml` file with any text editor.
2. Modify the following `<documentation-url>` line and replace the previous documentation value with the current documentation value: `<documentation-url>https://help.hitachivantara.com/Documentation/Pentaho/Data_Integration_and_Analytics/10.2</documentation-url>`.
3. Save and close the file.
