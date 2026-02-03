# Set up a Postman mock server

Create _mock servers_ in Postman to help with API development and testing. A mock server simulates a real API server by accepting requests and returning responses. By configuring a mock server for your [collection](/docs/sending-requests/create-requests/intro-to-collections/) and adding [examples](/docs/sending-requests/response-data/examples/) to your requests, you can simulate the behavior of a real API.

When you send a request to a mock server, Postman matches the request to a saved example in your collection. Postman then responds with the data in the example. To view existing mock servers in your workspace, click **Mock servers** in the sidebar.

Mock servers can be private or public. Private mock servers require a Postman API key in the request header. Public mock servers can receive requests from anyone and anywhere (such as a browser, application code, or a curl command). New mock servers are public by default. [Super Admins and Team Admins](/docs/administration/roles-and-permissions/#team-roles) can enable or prohibit users from creating public mock servers. See [Manage mock server privacy](/docs/administration/managing-your-team/manage-team-workspaces/#manage-mock-server-privacy) to learn more.

Postman mock servers only support HTTP collections. You can't use mock servers with multi-protocol collections.

## Create mock servers

You can create a mock server in the following ways:

1. Create a [new mock server](#create-a-mock-server) from scratch.
2. Create a mock server from an [API call](#create-a-mock-server-from-an-api-call).
3. Create a mock server from [your request history](#create-a-mock-server-from-history).

### Create a mock server

1. Click **Mock servers** in the sidebar, then click **Create mock server**. You can also click **View more actions** next to the collection you want to mock and select **More > Mock**.
   
   ![Image 1: Create Postman Mock Server](https://assets.postman.com/postman-docs/v11/mock-server-create-v11.png)
   
2. Select an existing collection from the dropdown list. Or you can choose **Create a new collection**, then add requests in the **Add requests** section.
   
3. Configure your [mock server details](#configure-mock-server-details).

### Create a mock server from an API call

1. In Postman, send an HTTP request to an API (for example, `https://postman-echo.com/get`).
2. Click **Save** and save the request to a collection.
3. In the response pane, click **Save Response**. Postman automatically populates the example with the response you received when you sent the request.
4. Click **Collections** in the sidebar. Click **View more actions** next to the collection where the request was saved and select **More > Mock**.
5. Give your mock a name and leave the other settings at their defaults. Click **Create Mock Server**.
6. Click **Copy URL** to copy the mock URL, then go back to your request. Replace the base part of the URL with the mock server URL (everything before the path, for example, up to `/get`).
7. Add your [Postman API key](/docs/developer/postman-api/authentication/#generate-a-postman-api-key) to the request as an `x-api-key` header in the **Headers** tab.
8. Click **Send**. Postman returns the example response you saved for the request, this time from the mock server.
9. Open the example and change the response, then save the example and send the request again. Postman returns your edited mock response.

### Create a mock server from history

You can build a collection and mock server based on requests from your Postman history.

1. Click **History** in the sidebar.
2. Click **View more actions** next to a request and select **Mock Request**. You can also mock all requests for a specific date. Postman creates a new collection for the mocked request or requests.
3. [Configure](#configure-mock-server-details) the mock server's details. Enter a server name, (optionally) select an environment, choose whether to enable **Make this mock server private** and **Save the mock server URL as an environment variable**, and select a response delay or enter a custom delay.
4. Click **Create Mock Server**.

## Configure mock server details

Some configuration options may be different, depending on the method you used to [create the mock server](#create-mock-servers).

1. To finish creating a mock server, specify the following details:
   
   * **Mock Server Name** - Enter a name for your mock server.
   * **Collection** - The collection used for the mock server. To choose a different collection, click **Back**.
   * **Environment** - (Optional) Select an [environment](/docs/sending-requests/variables/managing-environments/) to use environment variables with your mock server.
   * **Simulate a fixed network delay** - Select a response delay or enter a custom delay. The mock server waits the specified time before sending the response.
   * **Save the mock server URL as a new environment variable** - Select this option to save the mock server URL as a variable in a new environment. You can then reference the variable in your requests. Learn more about [using variables with mock servers](/docs/design-apis/mock-apis/create-dynamic-responses/#use-postman-variables-with-mock-servers).
   * **Make mock server private** - Select this option to make your mock server private. You must specify an API key in the request header when sending requests to a private mock server. Learn more about [making calls to a private mock server](/docs/design-apis/mock-apis/mock-server-calls/#make-calls-to-a-private-mock-server).

   If the **Make mock server private** option is unavailable, it may be turned off in [Team resources](http://go.postman.co/settings/team/team-resources). A [Team Admin or Super Admin](/docs/administration/roles-and-permissions/#team-roles) can turn it back on.

2. Click **Create Mock Server**.

   Postman displays the details you need to use the mock server. You can get these details at any time by clicking **Mock servers** in the sidebar and selecting the mock server.

   ![Image 2: Configuring mock server details](https://assets.postman.com/postman-docs/v11/mock-server-configure-details-v11-20.png)

3. Click **Copy URL** to begin [making calls to your mock server](/docs/design-apis/mock-apis/mock-server-calls/).

### Edit the mock server configuration

You can change the configuration for a mock server at any time.

1. Click **Mock servers** in the sidebar.
2. Select a mock server and click **Edit Configuration**.

   ![Image 3: Editing mock server configuration](https://assets.postman.com/postman-docs/v11/mock-server-edit-configuration-v11-8.jpg)

3. Make any changes to the mock server configuration. You can change the mock server's name, environment, network delay, and privacy setting. You can also [specify options for response matching](#match-request-body-and-headers).

   You can't change the mock server's collection. If you need to mock a different collection, [create a new mock server](#create-mock-servers).

4. When you are done making configuration changes, click **Update Mock Server**.

### Match request body and headers

When you send a request to the mock server, Postman uses a [matching algorithm](/docs/design-apis/mock-apis/matching-algorithm/#6-check-for-header-and-body-matching) to decide which example to return in a response.

By default, the matching algorithm doesn't consider the request's body or headers when selecting the best response to return. You can change this behavior in the mock server's configuration. Using body or header matching, you can specify the exact response you want the mock server to return by matching the body or headers of the saved example.

If you enable request body matching, you must add the `Content-Type` header to your examples and use the same value as your request, such as `application/json`.

To use body or header matching with a mock server, do the following:

1. Click **Mock servers** in the sidebar, select a mock server, and click **Edit Configuration**.
2. Under **Response Matching**, select the matching options you want to use:
   
   * **Request body** - The mock server matches the request's body to the body of the saved examples.
   * **Headers** - The mock server matches the request's headers to the headers of the saved examples. In the box, add a comma-separated list of the header keys that you want the mock server to match. Header matching isn't case-sensitive.

3. Click **Update Mock Server**.

### Delete a mock server

To delete a mock server, click **Mock servers** in the sidebar. Click **View more actions** next to the mock server's name and click **Delete**.

## Next steps

To learn more about mock servers, see the following resources:

* [Make calls to your mock server](/docs/design-apis/mock-apis/mock-server-calls/)
* [Mock APIs with response examples](/docs/design-apis/mock-apis/tutorials/mock-with-examples/)
* [Create and use a mock server using the Postman API](/docs/design-apis/mock-apis/tutorials/mock-with-api/)
* [How a Postman mock server matches requests to saved examples](/docs/design-apis/mock-apis/matching-algorithm/)