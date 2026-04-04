# Source: https://docs.api7.ai/enterprise/api-portal/productize-services.md

# Source: https://docs.api7.ai/enterprise/3.8.x/api-portal/productize-services.md

# Source: https://docs.api7.ai/enterprise/3.7.x/api-portal/productize-services.md

# Source: https://docs.api7.ai/enterprise/3.6.x/api-portal/productize-services.md

# Source: https://docs.api7.ai/enterprise/3.5.x/api-portal/productize-services.md

# Source: https://docs.api7.ai/enterprise/3.4.x/api-portal/productize-services.md

# Source: https://docs.api7.ai/enterprise/3.3.x/api-portal/productize-services.md

# Productize Services

Create and manage [API products](https://docs.api7.ai/enterprise/3.3.x/key-concepts/api-products.md) to productize your published services. Each API product consists of at least one published service with OpenAPI specification.

Creating API Products from published API7 Gateway services streamlines development workflows. Changes to published services are automatically reflected in the associated API Products, eliminating the need for manual updates and saving significant time and effort. Developers can focus solely on API consumption without being concerned with underlying service configurations or plugin details.

This tutorial demonstrates how to create an API product for internal developers and outlines the subscription process.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
2. Activate license with API7 Portal enabled.
3. [Have a running published service](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md).

## Add OpenAPI Specification[â](#add-openapi-specification "Direct link to Add OpenAPI Specification")

1. Select **Published Services** of your gateway group from the side navigation bar, then click the service you want to modify, for example, a no-version `httpbin` service.

2. Under the published service, select **OpenAPI Specification** from the side navigation bar.

3. Click **Upload OpenAPI Specification**.

4. Fill in the form:

   * Use the following OpenAPI specification:

   httpbin.yaml

   ```
   openapi: 3.0.0
   info:
   title: HTTPBin
   description: A simple HTTP request and response service.
   version: 1.0.0
   servers:
   - url: https://httpbin.org

   paths:
   /ip:
       get:
       summary: Returns GET request information
       responses:
           '200':
           description: Successful response
           content:
               application/json:
               schema:
                   $ref: '#/components/schemas/Get'

   components:
   schemas:
       Get:
       type: object
       properties:
           args:
           type: object
           headers:
           type: object
           origin:
           type: string
   ```

5. Click **Save**.

6. To avoid authentication conflicts, please do not enable any authentication plugins within the published service. API Product configurations will handle authentication.

note

Please make sure that the OpenAPI specification matches your published services:

* The `Servers` field in the OpenAPI specification corresponds to the `Hosts` field in the published service.
* Each `Path` defined in the OpenAPI specification must match a specific `path` and `method` combination within a route.

## Add API Product[â](#add-api-product "Direct link to Add API Product")

1. Switch to API7 Provider Portal using the button on the top-left corner of the navigation bar.

2. Click **Add API Product**, then select **From API7 Gateway**.

3. Fill in the form:

   <!-- -->

   * In the **Name** field, enter `httpbin`.

   * In the **Authentication Type** field, choose `Key Authentication`.

   * Close the **Subscription Auto Approval** switch.

   * In the **API Hub List Visibility** field, choose `Visible to logged-in developers only`.

   * Open the **Unsubscribed developers can view API details** switch.

   * Click **Add Linked Gateway Service**.

   * From the dialog box, do the following:

     <!-- -->

     * In the **Gateway Group** field, choose your target gateway group. For example, `default`.
     * In the **Published Services** field, choose your target service. For example, `httpbin`.
     * Click **Add**.

4. Click **Add**.

5. By default, newly created API Products are in a `draft` state and are not visible on the Developer Portal. Click **Actions** button at the top, then select **Publish**.

6. Click **Confirm**.

## Developer Requests Subscription[â](#developer-requests-subscription "Direct link to Developer Requests Subscription")

1. Use a developer account to log in to the Developer Portal.
2. Select **API Hub** from the top navigation bar.
3. Select `httpbin`.
4. Explore the API details to ensure they meet specific needs.
5. Click **Subscribe Now**.
6. Wait for approval.

## Provider Accepts Approval[â](#provider-accepts-approval "Direct link to Provider Accepts Approval")

1. Select **Organization** from the top navigation bar, and then select **Approvals**.
2. Click **Accept** for the specific request.

## Developer Validates API[â](#developer-validates-api "Direct link to Developer Validates API")

1. Use a developer account to log in to the Developer Portal.
2. Select **API Hub** from the top navigation bar.
3. Select `httpbin`.
4. Click **Test Request**.
5. The **Auth Type** is pre-selected, and the API key is automatically filled in, copied from the developer's credential.
6. Click **Send**.
7. Receive a `200` response.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts

  <!-- -->

  * [API Products](https://docs.api7.ai/enterprise/3.3.x/key-concepts/api-products.md)
  * [Developers](https://docs.api7.ai/enterprise/3.3.x/key-concepts/developers.md)
