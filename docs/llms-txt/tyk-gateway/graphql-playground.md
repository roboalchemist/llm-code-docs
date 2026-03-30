# Source: https://tyk.io/docs/tyk-developer-portal/graphql-playground.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Set Up the GraphQL Playground

> Learn how to set up and use the GraphQL Playground in the Tyk Developer Portal

## Availability

| Component        | Version                                                                                 | Editions   |
| :--------------- | :-------------------------------------------------------------------------------------- | :--------- |
| Developer Portal | Available since [v1.15.0](/developer-support/release-notes/portal#1-15-0-release-notes) | Enterprise |

## Prerequisites

* **Dashboard License**: We will configure GraphQL API using Dashboard. [Contact our team](https://tyk.io/contact/) to obtain a license or get self-managed trial license by completing the registration on our [website](https://tyk.io/self-managed-trial/).
* **Working Tyk Environment:** You need access to a running Tyk instance that includes both the Tyk Gateway and Tyk Dashboard components. For setup instructions using Docker, please refer to the [Tyk Getting Started Guide](/getting-started/quick-start).
* Tyk Developer Portal v1.15.0 or later

## Instructions

Follow these steps to set up the GraphQL Playground in the Tyk Developer Portal:

### 1. Create a GraphQL API

1. In the **Tyk Dashboard**, create a new **GraphQL API** by

   * Navigating to **APIs > Add New API**
   * In the next screen, click on **Try example** and select **Star Wars GQL API** from the list.
   * Click **Use Example** to create the API.
   * **Star Wars GQL API** uses [Auth Token](/api-management/authentication/bearer-token) for authentication. Copy the **Key ID** from the pop-up and save it for later use. We will set the authorization header in the Playground using this Key ID.

2. Now, go to the **Schema** tab and download the schema.

   This schema file will be uploaded to the Developer Portal in a later step.

   <img src="https://mintcdn.com/tyk/5W_NY0b4OXjxqYfk/img/graphql-api-star-wars-schema.png?fit=max&auto=format&n=5W_NY0b4OXjxqYfk&q=85&s=9e571bc565e35c9336a1cae978a49b70" alt="GraphQL API Schema Tab" width="3024" height="1726" data-path="img/graphql-api-star-wars-schema.png" />

### 2. Create the API Catalog

The Tyk Getting Started Guide creates an API Catalog (`Public catalogue`) by default. If you don't have one, refer to this [guide](/portal/publish-api-catalog#step-1:-create-the-api-catalog) to create an API Catalog in the Developer Portal.

### 3. Create an API Product

1. Navigate to **Developer Portal > API Products**
2. Click **Add new API Product**
   <img src="https://mintcdn.com/tyk/UiKBFLPkIyNRnItY/img/dashboard/portal-management/enterprise-portal/portal-add-api-product.png?fit=max&auto=format&n=UiKBFLPkIyNRnItY&q=85&s=0885bb1e9ff32f736b7f1028850fec17" alt="Add an API Product" width="3442" height="1982" data-path="img/dashboard/portal-management/enterprise-portal/portal-add-api-product.png" />
3. On the **Details** tab, enter the basic product information:
   <img src="https://mintcdn.com/tyk/UiKBFLPkIyNRnItY/img/dashboard/portal-management/enterprise-portal/portal-product-details.png?fit=max&auto=format&n=UiKBFLPkIyNRnItY&q=85&s=c1d68a53fee5fd8f96b04d16ec71223f" alt="Configure API Product details" width="3456" height="1924" data-path="img/dashboard/portal-management/enterprise-portal/portal-product-details.png" />
   * Product name: A unique product name (e.g., "Star Wars")
   * Publish API product to catalogue: Select the catalog you created [previously](#2-create-the-api-catalog)
   * You can leave the other fields empty for now
4. On the **APIs** tab, select the `Star Wars GQL API` created in the [first step](#1-create-a-graphql-api):
5. On the **Documentation** tab:
   * Add your **GraphQL API endpoint URL** (e.g `http://localhost:8080/star-wars-api/`).

     <Note>
       You can find the endpoint URL in the **Core Settings** tab of your GraphQL API in the Dashboard.
     </Note>

   * Upload a GraphQL SDL file (in .graphql, .graphqls, .gql, or JSON format)
     <Note>
       By default, the GraphQL playground will introspect the schema from the endpoint if no SDL file is provided. However, if the API is protected, introspection will not work, and the schema will be rendered from the uploaded SDL file.
     </Note>
   <img src="https://mintcdn.com/tyk/5W_NY0b4OXjxqYfk/img/graphql-docs-tab-playground-setup.png?fit=max&auto=format&n=5W_NY0b4OXjxqYfk&q=85&s=40daece9b5d5f47068eb6c64fffca1d1" alt="GraphQL API Product Documentation Tab" width="3023" height="1731" data-path="img/graphql-docs-tab-playground-setup.png" />
6. Click **Save Changes**

### 4. View the Playground

1. Open your **Live Portal**.
2. Go to **Product Catalogues**, locate your GraphQL Product and Click **Docs**.
   <img src="https://mintcdn.com/tyk/5W_NY0b4OXjxqYfk/img/graphql-docs-live-portal.png?fit=max&auto=format&n=5W_NY0b4OXjxqYfk&q=85&s=c0c9417a946d2f6894e873af8f097132" alt="GraphQL API Docs Live Portal" width="3023" height="1730" data-path="img/graphql-docs-live-portal.png" />
3. You should now see the **GraphQL Playground**, ready for interactive query testing.

   <Note>
     To test authenticated APIs, ensure you set the required authentication headers in the Playground according to your API's authentication settings.

     For example, for the `Star Wars GQL API`, add the `Authorization` header with the value `Bearer <Key ID>` where `<Key ID>` is the token you saved earlier.

     ```json  theme={null}
     {
         "Authorization": "Bearer YOUR_KEY_ID"
     }
     ```

   </Note>

   <img src="https://mintcdn.com/tyk/5W_NY0b4OXjxqYfk/img/graphql-playground-portal.png?fit=max&auto=format&n=5W_NY0b4OXjxqYfk&q=85&s=1eb6dd914f5253765e36a1536b64c506" alt="GraphQL API Playground" width="3023" height="1723" data-path="img/graphql-playground-portal.png" />

## Troubleshooting

<AccordionGroup>
  <Accordion title="404 GraphQL API Not Found Error in Playground">
    If you encounter a `404 GraphQL API Not Found` error in the GraphQL Playground, it indicates that the Developer Portal cannot locate the specified GraphQL API.

    To resolve this issue, ensure that your API ends with a trailing slash (`/`). (e.g `http://localhost:8080/star-wars-api/`)

    <Note>
      You can find the endpoint URL in the **Core Settings** tab of your GraphQL API in the Dashboard.
    </Note>
  </Accordion>

  <Accordion title="&#x22;message&#x22;: &#x22;Failed to fetch&#x22; error in Playground">
    If you are seeing a `"message": "Failed to fetch"` error in the GraphQL Playground, it is likely due to CORS (Cross-Origin Resource Sharing) restrictions. To resolve this issue, follow these steps:

    Go to the Dashboard, and add the following CORS configuration to your GraphQL API settings:

    ```json  theme={null}
        "CORS": {
          "enable": true,
          "max_age": 24,
          "allow_credentials": true,
          "exposed_headers": [
            "*"
          ],
          "allowed_headers": [
            "*"
          ],
          "options_passthrough": true,
          "debug": false,
          "allowed_origins": [
            "http://localhost:3001"
          ],
          "allowed_methods": []
        },
    ```

    * Ensure that the `allowed_origins` field includes the URL of your Developer Portal (e.g., `http://localhost:3001` for local setups).
  </Accordion>
</AccordionGroup>

Built with [Mintlify](https://mintlify.com).
