# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/salesforce-bulk-operation/options-salesforce-bulk-operation/connection-tab-salesforce-bulk-operation.md

# Connection tab

Use this tab to provide the credentials to connect to Salesforce. The **Client id** and **Client secret** are used for the service account, and the **Username** and **Password** credentials provide the user that the service account impersonates.

![PDI Salesforce bulk operation step Connection tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-7f4b13b3a9cc9c9383ef49deb7911265ddd83388%2FPDI%20Salesforce%20bulk%20operation%20step%20Connection%20tab.png?alt=media)

| Field                     | Description                                                                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **OAuth2 login endpoint** | The endpoint to retrieve a token from Salesforce.                                                                                   |
| **Client id**             | Client identifier required to get the authentication token from the Salesforce Oauth endpoint. This is set up in Salesforce.        |
| **Client secret**         | Client Secret credential required to get the authentication token from the Salesforce Oauth endpoint. This is set up in Salesforce. |
| **Username**              | Specify the username for authenticating to Salesforce.                                                                              |
| **Password**              | Specify the password for authenticating to Salesforce.                                                                              |
| **Test connection**       | Click to verify the connection can be made to the Salesforce Webservice URL you specified.                                          |
