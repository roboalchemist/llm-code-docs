# Mock APIs with response examples

[Mock servers](/docs/design-apis/mock-apis/set-up-mock-servers/) simulate an API server by returning predefined data, so you can develop or test an API before it's ready for production. In Postman, mock servers use [examples](/docs/sending-requests/response-data/examples/) saved in an HTTP collection to return mock data.

In this tutorial, you'll learn how mock servers and examples work together and how to integrate them into your API workflow.

## Create a new collection and request

To get started, you'll need to create a collection and an example response.

1. Click ![Image 1: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) in the sidebar. Select **Blank collection** and give it the "C1" name.
2. In the collection, click **Add a request** to create a request. Optionally, you can rename the request.
3. Select the **GET** method, then enter `https://postman-echo.com/get?test=123` as the request URL.
4. Click **Send**, then click ![Image 2: Save icon](https://assets.postman.com/postman-docs/aether-icons/action-save-stroke.svg#icon) **Save** to save the request in the **C1** collection.

![Image 3: Send a request](https://assets.postman.com/postman-docs/v11/mock-examples-step1-v11.png)

## Save a response as an example

Save the response you received from the Postman Echo service as an example.

1. Click ![Image 4: Example icon](https://assets.postman.com/postman-docs/aether-icons/entity-example-stroke.svg#icon) **Save Response** to save the example in the request.
2. (Optional) Rename the example (for example, "E1"). The request method, URL, and status code are all saved as part of the example. Postman uses these items to decide which responses the mock server returns.

## Send a request to the mock server

Next, create a mock server for the **C1** collection.

1. Click **Mock servers** in the sidebar.
2. [Create a mock server](/docs/design-apis/mock-apis/set-up-mock-servers/#create-a-mock-server) for the **C1** collection. For this tutorial, name the mock server "M1".
3. Click ![Image 5: Save icon](https://assets.postman.com/postman-docs/aether-icons/action-save-stroke.svg#icon) **Save** to save the mock server.
4. Click ![Image 6: Copy icon](https://assets.postman.com/postman-docs/aether-icons/action-copy-stroke.svg#icon) **Copy URL** to copy the "M1" mock server's URL.

    ![Image 7: Copy mock URL](https://assets.postman.com/postman-docs/v11/mock-examples-step5a-v11.23.jpg)

1. In the **C1** collection, create a new request.
2. Paste the mock URL as the request's URL, then click **Send**.

    ![Image 8: Mock server error response](https://assets.postman.com/postman-docs/v11/mock-examples-step5b-v11-42.jpg)

    The request returns an error because the mock server's URL doesn't have a defined path. The path appended to the end of the mock server URL must match the path in the example's request URL (`/get`). The method selected in the mock server and example must also match. Responses returned by the mock service depend on the URL and method in your saved examples.

1. To send a request to the mock server, add `/get` to the end of the mock server's URL, then click **Send**.

    ![Image 9: Mock server correct response](https://assets.postman.com/postman-docs/v11/mock-examples-step5c-v11-42.jpg)

### Add another example

You can add another example to test how responses from the mock service depend on saved examples.

1. [Create and send a request](#send-a-request-to-the-mock-server). Select the **GET** method, then enter `https://postman-echo.com/test` as the request URL.
2. Save the request to the **C1** collection.
3. [Save the response as an example](#save-a-response-as-an-example). Rename the example to "E2".

    ![Image 10: Add a second example](https://assets.postman.com/postman-docs/v11/mock-examples-step6a-v11.23.jpg)

4. [Send a request to the mock server](#send-a-request-to-the-mock-server). Update the path at the end of the mock server URL to `/test` and click **Send**. The mock server returns the expected HTTP 404 Not Found status code.

    ![Image 11: Send another request to the mock server](https://assets.postman.com/postman-docs/v11/mock-examples-step6b-v11-42.jpg)

**Your examples can vary depending on the URL endpoint, request method, or status code.** If you have multiple examples, you can choose to save each example under a unique endpoint URL, like you saw in this demonstration with `/get` and `/test`. If you've saved examples with different response status codes, you can send an authenticated request to the mock server along with the `x-mock-response-code` header specifying which integer response code your returned response needs to match.

## Use query parameters

Postman's mock service uses a [matching algorithm](/docs/design-apis/mock-apis/matching-algorithm/) to select the best saved example to return in response to a request. As part of this algorithm, the mock server looks at the request's path and query parameters, and then matches the request to a saved example. If you have examples with the same request path but different query parameters, you can mock different responses for different query parameters on the same request path.

The following scenario demonstrates how the matching algorithm selects the best saved example:

* A mocked collection has one request named **Request1** with two examples named **Example1** and **Example2**.
* In **Example1**, the `id` parameter has a `1` value.

    ![Image 12: Query parameters example 1](https://assets.postman.com/postman-docs/v11/mock-examples-params1-v11.23.jpg)

* In **Example2**, the `id` parameter has a `5` value.

    ![Image 13: Query parameters example 2](https://assets.postman.com/postman-docs/v11/mock-examples-params2-v11.23.jpg)

* In this scenario, **Example1** and **Example2** have the same request path (`/get`), but they each have an `id` query parameter with different values. When you send a request to the mock server URL and pass these different query parameters, Postman returns the exact response that matches both the path and the query parameters.

    ![Image 14: Query parameters mock response](https://assets.postman.com/postman-docs/v11/mock-examples-params3-v11-42.jpg)

If no exact match is found, Postman returns the best response based on its [matching algorithm](/docs/design-apis/mock-apis/matching-algorithm/).

## Mock GraphQL queries

Postman's mock service enables you to mock GraphQL queries. To mock GraphQL queries, make a request to the mock server using the request path and request body saved in the examples in the mocked collection.

Make sure to set the `Content-type: application/json` header to in your examples.

![Image 15: Query parameters example](https://assets.postman.com/postman-docs/v11/mock-examples-graphql1-v11.23.jpg)