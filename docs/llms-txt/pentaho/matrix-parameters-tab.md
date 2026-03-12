# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/rest-client-step/options-rest-client/matrix-parameters-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/rest-client-step/options-rest-client/matrix-parameters-tab.md

# Matrix Parameters tab

![Matrix Parameters tab in REST client](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-5a5fcd71e7cf50a7a80ca12b509d167565286ddb%2FPDITransStep_RESTClient_MatrixParametersTab.png?alt=media)

Use the **Matrix Parameters** tab to define matrix parameter values for **POST**, **PUT**, **DELETE**, and **PATCH** requests.

The **Matrix Parameters** tab contains the following columns:

| Column        | Description                                                                           |
| ------------- | ------------------------------------------------------------------------------------- |
| **Parameter** | The field from the incoming PDI stream that contains the matrix parameter information |
| **Parameter** | The name of the outgoing PDI field from this step                                     |

Use the **Get** button to populate the table with fields from the incoming PDI stream.

**Note:** The matrix parameters table and the **Get** button are only available when the **HTTP method** in the **General** tab is set to **POST**, **PUT**, **DELETE**, or **PATCH**.
