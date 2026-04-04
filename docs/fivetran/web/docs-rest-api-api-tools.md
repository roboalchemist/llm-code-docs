# Source: https://fivetran.com/docs/rest-api/api-tools

Title: API tools for the Fivetran REST API

URL Source: https://fivetran.com/docs/rest-api/api-tools

Markdown Content:
The following tools and code sample libraries let you use the Fivetran REST API in a more efficient and easy way:

*   [Fivetran REST API Postman collection](https://fivetran.com/docs/rest-api/api-tools#fivetranrestapipostmancollection)
*   [Fivetran Iceberg REST Catalog Postman collection](https://fivetran.com/docs/rest-api/api-tools#fivetranicebergrestcatalogpostmancollection)
*   [Fivetran provider for Apache Airflow](https://fivetran.com/docs/rest-api/api-tools#fivetranproviderforapacheairflow)
*   [Fivetran provider for Terraform](https://fivetran.com/docs/rest-api/api-tools#fivetranproviderforterraform)
*   [Fivetran Webhooks project](https://fivetran.com/docs/rest-api/api-tools#fivetranwebhooksproject)

* * *

Postman collections[](https://fivetran.com/docs/rest-api/api-tools#postmancollections)
--------------------------------------------------------------------------------------

Postman is a very popular and convenient API client that makes it easy for developers to create, share and test API requests. We provide the following Postman collections:

*   Fivetran REST API Postman collection - this collection provides request templates to help you create API calls for all endpoints supported by Fivetran
*   Fivetran Iceberg REST Catalog Postman collection - this collection is designed to get metadata from tables stored in your [Fivetran Iceberg REST Catalog](https://fivetran.com/docs/destinations/managed-data-lake-service#fivetranicebergrestcatalog).

### Fivetran REST API Postman collection[](https://fivetran.com/docs/rest-api/api-tools#fivetranrestapipostmancollection)

You can use Fivetran REST API Postman collection to test API endpoints within your account. The collection contains templates to help you create API calls for all endpoints supported by Fivetran.

To use our REST API Postman collection:

1.   Download and install [Postman](https://www.postman.com/).

2.   Download and then import our [REST API Postman Collection](https://fivetran.com/assets-docs/postman/rest_api_collection.json).

Log in to your Postman account prior to starting the collection import. 
![Image 1: import](https://fivetran.com/static-assets-docs/_next/static/media/import.56f45472.webp)

Once the collection is imported, the following API requests will appear on the **Collections** tab.

![Image 2: configuring](https://fivetran.com/static-assets-docs/_next/static/media/collection-tab.e73a0e84.webp)

3.   Configure the authorization in Postman.

i. Hover over the imported Fivetran REST API collection.

ii. Click the menu icon ( ... ).

iii. Click **Edit** in the displayed menu. The Edit Collection page opens.

iv. Select the **Variables** tab.

v. Specify your API key and secret in unencoded format in the corresponding **Current Value** fields. You can find them in your Fivetran account settings. See our [REST API documentation](https://fivetran.com/docs/rest-api/getting-started#scopedapikey) to learn how to get your API key and secret. Postman encodes the API key and secret to base64 when calling an endpoint.

vi. Click **Save** to save the changes.

![Image 3: configuring](https://fivetran.com/static-assets-docs/_next/static/media/configuring.d1e64475.webp)

Don't share your key and secret. Remember that the exported collection may contain sensitive information in its parameters. 

When you complete the collection import and configuration, you will be able to run the API requests. Most of the requests require path or payload parameters that are enclosed in `{}`. You need to populate the parameters according to your needs.

* * *

### Fivetran Iceberg REST Catalog Postman collection[](https://fivetran.com/docs/rest-api/api-tools#fivetranicebergrestcatalogpostmancollection)

To use our Fivetran Iceberg REST Catalog Postman collection:

1.   Download and install [Postman](https://www.postman.com/).

2.   Download and then import our [Fivetran Iceberg REST Catalog Postman collection](https://fivetran.com/assets-docs/postman/Fivetran_Iceberg_REST_Catalog.postman_collection.json).

Log in to your Postman account prior to starting the collection import. 
![Image 4: import](https://fivetran.com/static-assets-docs/_next/static/media/import.56f45472.webp)

Once the collection is imported, the relevant API request templates will appear on the **Collections** tab.

3.   Define the [authorization parameters](https://fivetran.com/docs/rest-api/api-tools#authorization).

When you complete the collection import and configuration, you will be able to run the API requests. Most of the requests require path or payload parameters that are enclosed in `{}`. You need to populate the parameters according to your needs.

1.   Open the collection and set variables. In the collection’s **Variables** tab, fill in:

    *   `client_id` – your OAuth client ID
    *   `client_secret` – your OAuth client secret
    *   `catalog_id` – the catalog you want to query
    *   `base_url` – keep the default `https://polaris.fivetran.com/api/catalog/v1`
    *   `auth_url` – keep the default `https://polaris.fivetran.com/api/catalog/v1/oauth/tokens`(These variable names and defaults are already defined in the collection.)

2.   Set the grant type and token endpoint.

i. Go to **Fivetran Iceberg REST Catalog**>**Auth** or to **List Namespaces**>**Authorization**.ii. Set the parameters:

    *   **Type:** OAuth 2.0
    *   **Grant Type:** Client Credentials
    *   **Access Token URL:**`{{auth_url}}` (defaults to the Polaris OAuth token endpoint shown above).

3.   Provide client credentials:

    *   **Client ID:**`{{client_id}}`
    *   **Client Secret:**`{{client_secret}}`
    *   **Client Authentication:****Send as Basic Auth header** (Postman will send `Authorization: Basic base64(client_id:client_secret)` to the token endpoint).
    *   **Scope:**`PRINCIPAL_ROLE:ALL` (already present in the collection’s OAuth settings).

4.   Define the authorization header:

    *   **Add token to:****Header**
    *   **Header Prefix:****Bearer**(Postman will send `Authorization: Bearer <token>` with API requests.

5.   Click **Get New Access Token**. Postman requests a token from `{{auth_url}}` using the Client Credentials flow.

6.   Click **Use Token**.

    *   You do not need a refresh token for this flow; when the token expires, repeat **Get New Access Token**.

    *   Keep child requests set to **Inherit auth from parent**. In this collection, **Show Tables In Namespace** and **Show Table Metadata** are designed to inherit from the parent (the authorization is defined on the parent **List Namespaces** in your setup).

* * *

Fivetran provider for Apache Airflow[](https://fivetran.com/docs/rest-api/api-tools#fivetranproviderforapacheairflow)
---------------------------------------------------------------------------------------------------------------------

Apache Airflow is an open-source workflow management platform for data engineering pipelines that lets you programmatically author, schedule, and monitor workflows.

Providers are plugins that you can add to your configuration and use the resources of cloud platforms and services to provision infrastructure.

We have partnered with [Astronomer](https://www.astronomer.io/) to support an open-source async Fivetran provider for Airflow. If you have a provider-specific issue, [raise an issue](https://github.com/astronomer/airflow-provider-fivetran-async/issues) on the Github repo. If you have a Fivetran-related issue, create a [support ticket](https://support.fivetran.com/).

See the [Fivetran provider for Apache Airflow](https://github.com/astronomer/airflow-provider-fivetran-async) for details.

Our previous provider will be deprecated. See our [migration guide](https://github.com/fivetran/airflow-provider-fivetran#readme).

* * *

Fivetran provider for Terraform[](https://fivetran.com/docs/rest-api/api-tools#fivetranproviderforterraform)
------------------------------------------------------------------------------------------------------------

Terraform is an infrastructure-as-code (IaC) software tool that provides a command-line interface (CLI) workflow to manage cloud services. Terraform codifies cloud APIs into declarative configuration files.

Providers are plugins that you can add to your configuration and use the resources of cloud platforms and services to provision infrastructure.

See the [Fivetran provider for Terraform](https://registry.terraform.io/providers/fivetran/fivetran/latest/docs) page for details.

* * *

Fivetran Webhooks project[](https://fivetran.com/docs/rest-api/api-tools#fivetranwebhooksproject)
-------------------------------------------------------------------------------------------------

Webhooks are automated notifications sent from an application when an event occurs. Our [webhooks test project](https://github.com/fivetran/fivetran-webhook-example-express-js) is a simple example that demonstrates how to ingest webhooks from Fivetran.

Related articles[](https://fivetran.com/docs/rest-api/api-tools#relatedarticles)
--------------------------------------------------------------------------------

[Getting Started With Fivetran API](https://fivetran.com/docs/rest-api/getting-started)

[OpenAPI Definition And API Resources](https://fivetran.com/docs/rest-api/api-reference)

[Release Notes](https://fivetran.com/docs/rest-api/changelog)

Thanks for your feedback!

Was this page helpful?
