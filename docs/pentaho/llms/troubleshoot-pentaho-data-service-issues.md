# Source: https://docs.pentaho.com/pdia-data-integration/data-integration-issues/troubleshoot-pentaho-data-service-issues.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-issues/troubleshoot-pentaho-data-service-issues.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-issues/troubleshoot-pentaho-data-service-issues.md

# Troubleshoot Pentaho data service issues

You can list the services running on the Pentaho Server or Carte server using the `listService` command, as shown in the following example URL:

* `http://localhost:8080/pentaho/kettle/listServices`

If the data service appears in the list, the Pentaho Server is set up correctly. Check your network and client setup.

If it does not appear in the list, try the following tasks:

* If you stored the transformation in the Pentaho Repository, check the status using this command: `http://localhost:8080/pentaho/kettle/status`. Make sure the repository name appears in the configuration details section. If the repository name is missing or an error appears, check the configuration of the **slave-server-config** and accessibility of the `repositories.xml` file.
* If you did not store the transformation in the Pentaho Repository, but instead stored it on the local file system, make sure the service name is listed and accessible from the user account that runs the Pentaho Server in: `<users home>/.pentaho/metastore/pentaho/Kettle Data Service`

If the service name (the table to query) is still missing, reopen the service transformation and check the data service in the transformation settings.
