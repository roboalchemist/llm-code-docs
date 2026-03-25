# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/publish-a-pentaho-data-service.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/publish-a-pentaho-data-service.md

# Publish a Pentaho Data Service

To publish your data service, save the transformation containing the data service to the Pentaho Repository.

Perform the following steps to validate that your data service has been published:

1. Since the Pentaho Repository is in the Pentaho Server ensure any external assets needed by the transformation can be accessed remotely, even if the transformation is run by a different user.
2. Open a browser, go to the Pentaho Server, and log in. If you have installed the Pentaho Server locally, the URL is usually `localhost:8080`.
3. Validate that your data service was published by listing the data services on the server, as shown in the following example:

   ```
   http://<*Pentaho Server Host:Port*>/pentaho/kettle/listServices

   ```

You are now ready to share the data service with others.
