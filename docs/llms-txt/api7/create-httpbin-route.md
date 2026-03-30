# Source: https://docs.api7.ai/cloud/getting-started/create-httpbin-route.md

# Create Route for HTTPBIN Service

Now we have created the HTTPBIN service successfully, specifying the upstream URL. But we don't have any [routes](https://docs.api7.ai/cloud/concepts/route.md).

In this section, we'll create a route that returns a JSON string from <https://httpbin.org>. To create such a route, do the following steps:

1. Open the [API7 Cloud console](https://console.api7.cloud).

2. From the left navigation bar, choose **API Management**, then select **Services** from the secondary menu.

3. Click on the name of the HTTPBIN service.

4. On the service details page, click on the **Create Route**

5. Fill the form to create the target route.

   <!-- -->

   * Set the *Path* field to `/json`.
   * Select the *Strip Path Prefix* option, which means the `/v1/json` will be rewritten to "/json" before proxying to the backend;
   * Only allow `GET` method.

Congratulations! You have created the JSON route. Now, let's send some requests to verify if it works!

## Next[â](#next "Direct link to Next")

[Send Requests To Verify](https://docs.api7.ai/cloud/getting-started/send-requests-to-verify.md).
