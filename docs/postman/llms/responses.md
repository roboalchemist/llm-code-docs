# API response structure in Postman

The Postman response viewer helps you visualize and check the correctness of API responses. An API response consists of the response body, headers, cookies, and the HTTP status code. You can view details about the response, including test results, network information, response size, response time, and security warnings. You can also save responses as examples or files.

## Response body

The Postman **Body** tab gives you several tools to help you understand the response, including a data type selector, preview, search, filter, and Postbot-powered visualization.

### Data type selector

When you send a request, Postman automatically displays the data type of your response. For example, JSON responses are automatically shown in the JSON mode. Syntax is highlighted depending on the data type. You can select a different type: **JSON**, **XML**, **HTML**, **Raw**, **Base64**, or **Hex**.

If your response contains a link, it's highlighted. Selecting it loads a `GET` request.

![Select data type](https://assets.postman.com/postman-docs/v11/data-type-selector-v11.23.jpg)

**Force JSON formatting**. You can choose to have Postman auto-select your response data type or force JSON formatting. To update your selection, go to ![Settings](https://assets.postman.com/postman-docs/aether-icons/descriptive-setting-stroke.svg#icon) **Settings** in the Postman header, then select **Settings**. Under **General > Request > Response format detection**, select **JSON**.

### Preview

The ![Play AI icon](https://assets.postman.com/postman-docs/aether-icons/action-playAI-stroke.svg#icon) **Preview** tab provides a friendlier view into the data that's being sent and helps you understand any errors that occur. It supports many file formats, including **audio**, **video**, **script**, **image**, **plain**, and **embed**. JSON and XML data types display as tables.

![Response preview](https://assets.postman.com/postman-docs/v11/response-pane-preview-v11.23b.jpg)

### Search

You can use search phrases to find content of interest in your response. Click ![Search icon](https://assets.postman.com/postman-docs/aether-icons/action-search-stroke.svg#icon) **Search** in the response pane. You can also place your cursor in the response and press **â+F** or **Ctrl+F**.

![Response search](https://assets.postman.com/postman-docs/v11/response-pane-search-v11-35-4.jpg)

### Filter

To improve readability, you can filter your responses to show only relevant information. Use [JSONPath](https://datatracker.ietf.org/doc/html/rfc9535/) to filter JSON responses. Use [XPath](https://www.w3.org/TR/2010/REC-xpath20-20101214/) to filter XML and HTML responses.

With **JSON**, **XML**, or **HTML** selected in the data type selector, select ![Filter icon](https://assets.postman.com/postman-docs/aether-icons/action-filter-stroke.svg#icon) **Filter** in the response pane. Then enter a JSONPath expression to filter JSON or an XPath expression to filter XML or HTML. For JSONPath expressions, Postman suggests autocomplete options based on keys in the response. The response automatically displays the results of your expression.

If you enter an expression that doesn't return results, Postman will flag it with a yellow underline. If you enter an expression that isn't valid, Postman will flag it with a red underline. Hover over the expression to view a tooltip about the issue.

The expression persists in the response unless you close the request or clear the expression. A green dot on ![Filter icon](https://assets.postman.com/postman-docs/aether-icons/action-filter-stroke.svg#icon) indicates that the response is being filtered with an expression. Select ![Clear icon](https://assets.postman.com/postman-docs/aether-icons/action-clear-stroke.svg#icon) to clear the expression and display the full response.

When you enter an XPath expression, you can use it with both the **XML** and **HTML** data types.

![Response filter](https://assets.postman.com/postman-docs/v11/response-pane-filter-v11-35-4.jpg)

### Visualization

The ![Image icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-image-stroke.svg#icon) **Visualization** tab renders the data in the API response according to visualization code that you add to the **Scripts > Post-response** tab. You can also use Postbot to generate visualizations for you. For details on how to add, use, and debug visualization code, see [Visualize request responses using Postman Visualizer](/docs/sending-requests/response-data/visualizer/).

![Response visualization](https://assets.postman.com/postman-docs/v11/response-pane-visualization-v11.23.jpg)

## Server-sent events

Server-sent events (SSE) is a standard server-push technology for real-time communication between a client and a server over HTTP/S. SSE supports efficient and low-latency data transmission, making it a popular choice for applications that require real-time updates, such as chat apps and live sports updates.

You can test, debug, and document your SSE-based APIs along with your other APIs in Postman.

Consume server-sent events by creating a new HTTP request. Postman establishes the SSE connection and then streams and displays the events. You can drill into, search through, and clear the SSE messages in the response section. You can also save the response.

To try SSE communication, use the following Postman Echo service endpoint: `https://postman-echo.com/server-events/:numberOfEvents`.

![SSE endpoint test](https://assets.postman.com/postman-docs/v11/sse-endpoint-test-v11.jpg)

## Cookies

You can select **Cookies** to inspect cookies sent by the server. A cookie's entry includes its name, value, the associated domain and path, and other information about the cookie.

To learn more about working with cookies in Postman, see [Create and capture cookies using Postman's cookie manager](/docs/sending-requests/response-data/cookies/).

## Headers

Headers are displayed as key-value pairs under the **Headers** tab. Hover over the information icon ![Info icon](https://assets.postman.com/postman-docs/aether-icons/state-info-stroke.svg#icon) next to the header name to get a description of the header according to the HTTP specification.

## Test results

If the API request you are viewing had any tests, the results are displayed in the **Test Results** tab.

To learn more about running tests against API requests in Postman, see [Write scripts to test API response data in Postman](/docs/tests-and-scripts/write-scripts/test-scripts/).

## Network information

Postman displays network information when your API returns a response. Hover over the network icon ![Connection secure icon](https://assets.postman.com/postman-docs/aether-icons/state-connectionSecure-stroke.svg#icon) to get the local and remote IP addresses for the request you sent.

When you make an `https` request, the network icon includes a padlock. When you hover over the icon, the network information will show more information including the [HTTP version](/docs/sending-requests/response-data/troubleshooting-api-requests/#debugging-by-http-version) and [certificate verification](/docs/sending-requests/authorization/certificates/) details.

![Hover over the network icon for network information](https://assets.postman.com/postman-docs/v11/https-network-info-response-v11.23.jpg)

### SSL verification errors

If SSL verification is enabled and verification fails, the response area displays an error message. Select the link to open the Console and view more information about the error.

![Verification error](https://assets.postman.com/postman-docs/v11/response-error-disable-ssl-v11.23.jpg)

If needed, you can turn off SSL verification for the request or turn it off globally in Postman:

* To turn off SSL verification for a request, select **Disable SSL Verification** in the response error message.
* To turn off SSL verification globally, select ![Setting icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-setting-stroke.svg#icon) **Settings** in the header and under **Settings > Request** turn off **SSL certificate verification**.

If you have **SSL verification** turned off and your request returns a certificate verification error, you can hover over the network information for details about the error.

![Certificate error](https://assets.postman.com/postman-docs/v11/network-ssl-error-v11.23b.jpg)

For requests that are successful and return data but with a certificate verification failure, the [Console](/docs/sending-requests/response-data/troubleshooting-api-requests/) displays a warning.

## Response code

Postman displays the response code returned by the API. Hover over the response code to get a short description of the code and what it means.

![Hover over the response code to get a description](https://assets.postman.com/postman-docs/v11/response-code-v11.23.jpg)

Some API responses also contain custom messages that can help you understand response codes. For example, if you receive a `401 Unauthorized` response, the message might tell you to check the token you used in the request. If custom messages are returned, they're displayed in the **Body** of the response.

## Response time

Postman automatically calculates the time in milliseconds it took for the response to arrive from the server. This information can be useful for some preliminary performance testing. Hover over the response time for a graph with information on how long each event in the process took.

![Hover over the response code for a description](https://assets.postman.com/postman-docs/v11/response-time-v11.23.jpg)

## Response size

Postman displays the size of the response. Hover over the response size to get a breakdown by body and header sizes.

## Saving responses

If a request has been saved in a collection, you can save responses for that request. Once the response has been returned, you can:

* Select ![Example icon](https://assets.postman.com/postman-docs/aether-icons/entity-example-stroke.svg#icon) **Save Response** to save the response as an [example](/docs/sending-requests/response-data/examples/) that you can access later.
* Select ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions > Save response to file** to save the response as a JSON file.
* Select ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions > Clear response** to remove any data in the response viewer. Note that for event-based requests, this is available after the stream is closed.

![Save an API response as an example or file](https://assets.postman.com/postman-docs/v11/save-response-v11.23.jpg)

## Security warnings

Postman applies security rules configured for your [API requests](/docs/api-governance/api-testing/api-testing-warnings/) when you send requests to any API using either the Postman web app or the Postman desktop app. A security warning indicates that there are potential security risks the API might be vulnerable to, but they don't mean the API is broken.

To view the specific security warnings that Postman applies to all requests, see [Security warnings](/docs/api-governance/api-testing/security-warnings/).

If it finds any potential security risks, Postman adds the number of warnings to the **Security** tab in the response.

![Security tab showing one warning](https://assets.postman.com/postman-docs/v11/api-response-security-tab-v11.23.jpg)

To view the list of security warnings and to get more information about specific warnings, do the following:

1. Select **Security** to view the warnings.
1. For more details, select a warning to expand it.
1. Select **Possible fix** to learn about possible ways to fix the underlying problem.

![Select Possible fix in a security warning](https://assets.postman.com/postman-docs/v11/api-response-security-tab-possible-fix-v11.23.jpg)

### Hide security warnings

To turn a warning off for the current API response, do the following:

1. Select **Hide warning**.
1. Choose a reason for hiding it, then select **Hide**.

This will turn the warning off for all members of your team for this response.

To turn a warning off globally for your team, you can [configure your API Security rules](/docs/api-governance/configurable-rules/configuring-api-governance-rules/) (available for [Enterprise teams](https://www.postman.com/pricing/)).

![Select Hide warning in a security warning](https://assets.postman.com/postman-docs/v11/api-response-security-tab-hide-warning-v11.23.jpg)

When you or another member of your team has hidden a warning, Postman shows a message in the **Security** tab to indicate how many are hidden.

To turn this warning back on later, do the following:

1. Select **Review** in the **Security** tab.
1. Review your hidden warnings and select the eye icon ![Eye icon](https://assets.postman.com/postman-docs/eye.jpg#icon) next to the one you want to turn back on.

![Review hidden security warnings](https://assets.postman.com/postman-docs/v10/api-response-security-tab-review-hidden-warnings-v10-18.jpg)