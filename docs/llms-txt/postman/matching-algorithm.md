# matching-algorithm

When you create a mock server, Postman associates a collection (and optionally an environment) with the new mock server. When you call it using its URL (for example, `https://M1.mock.pstmn.io`), the mock service retrieves all saved examples (responses) for the associated collection before it begins the matching process.

After the mock service gets the collection's examples, it iteratively pairs the incoming request with the closest matching example.

Incoming requests can have configurable variables, such as `requestMethod`, `requestPath`, `requestHeaders`, `requestBody`, and `requestParams`. The `requestMethod` variable corresponds to any valid HTTP request method, and the `requestPath` refers to any valid string path (such as `/` or `/test`).

You can also use optional headers, like `x-mock-response-name` or `x-mock-response-id`, to further specify the example returned, based on the example's name or UID respectively. You can use the Postman API to [get a collection](https://www.postman.com/postman/postman-public-workspace/request/ypuwpio/get-a-collection), then find your example's UID (in `<userId>-<responseId>` format) in the response.

![Image 1: Mock request configurable elements](https://assets.postman.com/postman-docs/v11/mock-configurable-elements-v11.jpg)

## How it works

To match an incoming request with the closest matching example, Postman uses the following algorithm:

### 1. Fetch all examples

The mock service fetches all examples in the associated collection and converts them into Postman response objects using the [Postman Collection SDK](/docs/developer/collection-sdk/). If process fails, resulting in a response that isn't in the expected format, the example is removed from the matching process.

The mock service also fetches the environment associated with the mock server (if there is one). Collection variables and environment variables in the examples are then populated with data.

### 2. Filter by HTTP method

Any responses that aren't the same HTTP method type as the incoming request are removed from the matching process. For example, if the mock request was a POST to `https://M1.mock.pstmn.io/test`, all examples that aren't the POST method are disregarded.

### 3. Filter by custom headers

The matching algorithm checks any custom headers passed in the incoming request in the following order:

1. If the `x-mock-response-code` header is provided, the algorithm filters out all examples that don't have a matching response status code.
1. If the `x-mock-response-id` header is provided, the algorithm selects the example with the matching response ID and returns the example as the response. If no example is found with a matching ID, the matching process stops and Postman returns an error.
1. If the `x-mock-response-name` header is provided, the algorithm selects the example with the matching name and returns the example as the response.

* If more than one example in the mocked collection has the same name, Postman sorts the examples by ID and returns the first example in the list with a `200` response status code.
* If none of the matching examples has a `200` response status code, Postman returns the first example in the sorted list.
* If no example is found with a matching name, the matching process stops and Postman returns an error.

### 4. Filter by URL

The matching algorithm compares the incoming request's path with each saved example's path. The algorithm then assigns a score to each example based on how close the paths match.

An example starts with a score of 100. The algorithm goes through the matching process, stopping only when a match is made. The score is then adjusted based on the step that resulted in a match. If a match can't be made, the example is removed from the matching process.

### 5. Filter by parameters

After matching URLs, the algorithm examines the parameters for each example (for example, `{{url}}/path?status=pass`). The matching score is further adjusted based on the number of parameter matches, partial parameter matches, and missing parameters.

* **Parameter match** - A key-value pair in the example matches a key-value pair in the incoming request.
* **Partial parameter match** - A key in the example matches a key in the incoming request, but the values for the keys don't match.
* **Missing parameter** - A key is present in the example or the incoming request but not in both.

The number of matching parameters is used to calculate the matching percentage. The percentage equals the number of parameter matches divided by the sum of all parameter matches, partial parameter matches, and missing parameters.

### 6. Check for header and body matching

You can [enable header and request body matching](/docs/design-apis/mock-apis/set-up-mock-servers/#match-request-body-and-headers) in the mock server configuration. You can also enable header and body matching by passing the `x-mock-match-request-body` or `x-mock-match-request-headers` custom header with the request. These custom headers have higher precedence than header or body matching values specified in the mock server configuration.

If you enable request body matching, you must add the `Content-Type` header to your examples and use the same value as your request, such as `application/json`.

When header and body matching are enabled, the algorithm:

1. Filters out all examples that don't match the specified request headers. Header matching is case insensitive.
1. Filters out all examples that don't match the request body.

### 7. Select the highest matching score

The matching algorithm checks the matching scores of the remaining examples and returns the example with the highest score.

* If more than one example has the highest score, Postman sorts the examples by ID and returns the first example in the list with a `200` response status code.
* If none of the highest-scoring examples has a `200` response status code, Postman returns the first example in the sorted list.

## Use wildcard variables

All variables in an example's request that don't exist in the mock server's associated collection or environment are treated as _wildcard variables_. Wildcard variables act as capture groups for dynamic URL segments and applies to entire URL path segments. This is useful if some segments of the API's URL map to resource identifiers, like user IDs, user names, or file names.

For example, you can mock an endpoint that returns a user profile by ID. The endpoint takes in the user ID from the URL and returns the user ID in the response. On calling the GET `{{url}}/users/{{userId}}` endpoint, it returns:

```json
{
  "id": 2,
  "name": "Carol"
}
```

### Wildcard variables in responses

Wildcards in response bodies aren't part of the matching algorithm.

You can add the same variables in the example's response to use their captured values. For example, you can add a request body for the previous example:

```js
{
  "id": {{userId}},
  "name": "Carol"
}
```

This passes the value captured from the wildcard segment to the same variable name into the response.

## Troubleshooting mock server responses

If the mock server isn't returning the example you expect for a request, try the following:

* **Add different path variables to your examples.** Two examples with the same path variables are assigned the same matching score. In this case, Postman returns one of the examples. To make sure more than one example isn't assigned the same matching score, use different path variables for each of your examples.
* **Use request body matching to return a specific example.** When you [enable request body matching](/docs/design-apis/mock-apis/set-up-mock-servers/#match-request-body-and-headers), Postman returns the example that has the same body as your request. Your request uses the `Content-Type` header with a value like `application/json`, if the body is in JSON format. For Postman to return the correct example, you must use the `Content-Type` header in your example with the same value as your request.
* **Use optional headers to return a specific example.** You can make sure the mock server returns a specific example by using the `x-mock-response-name` or `x-mock-response-id` header in your request. Postman returns the example with the matching name or UID.
* **Make sure to use unique names for all saved examples in the mocked collection.** If more than one example in the collection has the same name, you may not get the expected response when using the `x-mock-response-name` header. Optionally, use the `x-mock-response-id` header to get the correct response. To find the ID of a saved example, select it in the sidebar, then click ![Image 2: Info icon](https://assets.postman.com/postman-docs/aether-icons/state-info-stroke.svg#icon) **Info** in the right sidebar.
* **Filter out examples by response status code.** You can use the `x-mock-response-code` header in your request to specify the response status code you want. Any examples that don't have the matching response status code are removed from the matching process.