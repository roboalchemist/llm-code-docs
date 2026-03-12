# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/google-analytics-v4/google-analytics-v4-options/google-analytics-v4-connection-tab.md

# Connection tab

Use this tab to select a method to provide the credentials to connect to Google Analytics.

![Google Analytics step Connection tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-478fbcb1d0b4ffb6920ee4897a6cb7522a1e8387%2FPDI%20Google%20Analytics%20step%20Connection%20tab.png?alt=media)

| Field               | Description                                                                                                                                                           |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Default**         | Select to use a key file you have referenced from the *GOOGLE\_APPLICATION\_CREDENTIALS* environment variable or automatically acquired from a Google cloud instance. |
| **JSON key file**   | Select to read the credentials for a service account from a previously generated key file. Click **Browse** to navigate to the source file                            |
| **Property id**     | Specifies the **Property id** of the Google Analytics values you want to query with the step. This is unique for every project in Google Analytics.                   |
| **Test Connection** | Click to test the connection.                                                                                                                                         |
