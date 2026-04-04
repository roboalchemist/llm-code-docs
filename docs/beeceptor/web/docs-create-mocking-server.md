# Source: https://beeceptor.com/docs/create-mocking-server/

Title: Mock Rules & Request Matching | Beeceptor

URL Source: https://beeceptor.com/docs/create-mocking-server/

Markdown Content:
Beeceptor is a robust mock server that empowers you to [create mock APIs](https://beeceptor.com/) with zero coding required. This no-code solution enables you to deploy a dedicated sub-domain to serve as your API or server endpoint.

Creating a mock rule[​](https://beeceptor.com/docs/create-mocking-server/#creating-a-mock-rule "Direct link to Creating a mock rule")
-------------------------------------------------------------------------------------------------------------------------------------

To manage mock server routes, use the **Mocking Rules** link on the endpoint's dashboard. Creating a rule involves two steps.

tip

Beeceptor also supports mock rules for [GraphQL](https://beeceptor.com/docs/graphql-mock-server/) and [gRPC](https://beeceptor.com/docs/grpc-mock-server/) based services.

Matching requests[​](https://beeceptor.com/docs/create-mocking-server/#matching-requests "Direct link to Matching requests")
----------------------------------------------------------------------------------------------------------------------------

When a request arrives at the Beeceptor endpoint, it is evaluated against the mock rules. The first rule that matches the request is selected, and the corresponding mock response is sent back to the client. You have the flexibility to modify the order of these rules and set priority.

### Matching with request parameters[​](https://beeceptor.com/docs/create-mocking-server/#matching-with-request-parameters "Direct link to Matching with request parameters")

A mock rule can be defined using one or more of the following matching criteria:

| Condition Type | Value & Example Usage |
| --- | --- |
| Request path exactly matches given text | Value: `/api/users/123` Example requests matched: * `/api/users/123` |
| Request path starts with given text | Value: `/api/users` Example requests matched: * `/api/users/123` * `/api/users/profile` |
| Request path contains given text | Value: `users` Example requests matched: * `/api/users/123` * `/admin/users/list` |
| Request path matches a regular expression | Value: `/api/users/\d+` Example requests matched: * `/api/users/123` * `/api/users/456` |
| Request body contains some text | Example: `user_id=123` Matches requests where the request body contains the specified text. |
| Request body matches a regular expression | Example: `user_id=\d+` Matches requests where the body content fits the given regular expression. |
| Request header value matches a regular expression | Example: `Authorization` with `Bearer .*` Matches requests with a header value matching the specified pattern. |
| Request body parameter matches specific value | Example: `user.email` equals `"john@example.com"` Matches requests where a JSON or form field has the specified value. |
| SOAPAction matches | Example: `http://example.org/orders/GetOrder` Matches SOAP requests with this SOAPAction header. |
| GraphQL query matches | Example: `query GetUser { user { id name } }` Matches GraphQL requests containing this specific query. |

Here are a couple of advanced strategies to optimize request matching features within Beeceptor:

#### Multiple conditions using AND[​](https://beeceptor.com/docs/create-mocking-server/#multiple-conditions-using-and "Direct link to Multiple conditions using AND")

Imagine a scenario where you are building a `POST` request at the endpoint `/login` and you want to simulate success and failure scenarios.

*   If the entering request body contains the word 'alex' as a username the call should success with `200 OK`.
*   Else, the call should be failed with `401 Unauthorized`.

With Beeceptor, you can craft a condition that triggers a successful login response specifically for Alex. Anyone else will fail the login attempt. This flexibility empowers you to simulate diverse scenarios, enhancing your testing and development workflow.

You can introduce AND conditions to incorporate supplementary conditions during the request matching process. Here's a brief demonstration showcasing this functionality in action.

Adding multiple conditions in a mock rule.

Beeceptor provides a pre-built [JSON Mock Server for the above login behavior](https://app.beeceptor.com/mock-server/json-placeholder). You should give it a try.

#### Path parameters[​](https://beeceptor.com/docs/create-mocking-server/#path-parameters "Direct link to Path parameters")

If you are matching a request using regular expression (RegEx) on the request path, you can use named groups. All the named groups and their values are available as template variables.

![Image 1: path parameter match using regular expression](https://beeceptor.com/docs/assets/images/matching-path-parameters-60b6f74e70d343952a5968308eaf7bf5.png)

The above example considers that you are [building an API mock](https://beeceptor.com/) for Company entity. You can match all the requests paths for Company entity and extract the company-id as path parameter.

**Regular expression examples**

*   `/companies/(?<company_id>[a-zA-Z0-9-]+)` - for matching alphanumeric company-ids. Example request path `/companies/be32a3a3-c2af-493c-adbd-ae2d09d8a0b8`
*   `/companies/(?<company_id>[0-9]+)` - for matching numeric company-ids. Example request path `/companies/123`

**Using path parameters in templates**

The named groups are available to be used as path parameters in templated response. You should use the following syntax.

`{{pathParam 'group-name' 'default-value'}}`

Example:

`{{pathParam 'company_id' '123'}}`

### Matching with state data[​](https://beeceptor.com/docs/create-mocking-server/#matching-with-state-data "Direct link to Matching with state data")

Beeceptor is a [stateful mock server](https://beeceptor.com/docs/mock-data-management/), allowing you to save, update, and share state data across multiple requests. This enables you to design context-aware responses that reflect real-world API behavior. You can also combine state-based filters with standard request filters to build rules that respond dynamically based on previously stored values or counters.

![Image 2: adding-state-filters-in-mock-rules](https://beeceptor.com/docs/assets/images/state-filters-in-mock-rules-7833c7a93aeb99c2ef66b2b16b9d9cb4.png)

Beeceptor supports three types of state variables:

*   **Datastore** (key–value pairs),
*   **List**, and
*   **Counter**.

The type Datastore (key–value pairs) is ideal for storing simple attributes, such as user preferences or feature flags. For a deeper dive into using state variables inside response templates refer [to this comprehensive guide](https://beeceptor.com/docs/template-stateful-mocks/).

Generating a response[​](https://beeceptor.com/docs/create-mocking-server/#generating-a-response "Direct link to Generating a response")
----------------------------------------------------------------------------------------------------------------------------------------

The second section in the create rule form defines what to send as HTTP response when the given rule is matched. You can define following things in this section.

1.   Response HTTP status code: Enter a valid [HTTP status code between 200 and 599](https://beeceptor.com/docs/concepts/http-status-codes/#classification-of-http-status-codes).
2.   Response Headers: Specify multiple response headers in JSON format.
3.   Response Body/Payload: Define the content for the response.

When configuring a mock rule within Beeceptor, you're presented with two options: Single Response and Weighted Response. This choice allows you to precisely define how your mock rule will handle incoming requests.

### Single response[​](https://beeceptor.com/docs/create-mocking-server/#single-response "Direct link to Single response")

Single Response is straightforward; you specify a single response, including the status code, response payload, and HTTP headers, to be returned consistently for all incoming requests.

![Image 3: single-response](https://beeceptor.com/docs/assets/images/mocking-rule-create-1b41830ad67794856a5e832d4dce4e94.png).

### Weighted response[​](https://beeceptor.com/docs/create-mocking-server/#weighted-response "Direct link to Weighted response")

Weighted Response introduces a dynamic element. In this mode, you have the flexibility to declare multiple responses, each with its own set of parameters (status code, response payload, and HTTP headers). What's unique is that Beeceptor randomly selects one of these responses based on defined weights.

*   For each additional response, you can assign a name and specify a weight in terms of percentage probability.
*   You must have at least one response defined.
*   The sum of all response weights must precisely equal 100%.
*   The selection of responses is entirely random. While it will closely approximate the defined weights, it may not be exact in every instance.

**Use case**

Suppose you want to create a mock rule where there's a 1% chance of failure and a 99% chance of a successful response for incoming calls. You can set this up in the Weighted Response configuration as shown below:

### Introducing delay[​](https://beeceptor.com/docs/create-mocking-server/#introducing-delay "Direct link to Introducing delay")

In the response section, you have the option to introduce a delay for the response. The caller will receive the response after a specific number of seconds.

tip

Beeceptor handles this delay computation on the server and attempts to match the specified seconds. However, please be aware that requests may take slightly longer than the exact time specified. This variance is influenced by factors such as network latency, server load, and other related variables.

Find which rule matched[​](https://beeceptor.com/docs/create-mocking-server/#find-which-rule-matched "Direct link to Find which rule matched")
----------------------------------------------------------------------------------------------------------------------------------------------

When dealing with multiple rules that share similar or slightly varied request paths, it can be challenging to pinpoint which rule was matched. Beeceptor simplifies this process by helping you identify the exact rule that matched.

### Rule Priority and Reordering[​](https://beeceptor.com/docs/create-mocking-server/#rule-priority-and-reordering "Direct link to Rule Priority and Reordering")

Beeceptor evaluates incoming requests strictly in a top-down manner, checking each mock rule in the order they appear in the dashboard. As soon as the first matching rule is found, Beeceptor applies its configured behavior, and stops evaluating any further rules. This means the visual order of rules directly determines which one takes precedence, making the “first match wins” approach central to how mock behavior is resolved.

To manage this priority, you can reorder rules using the drag-and-drop interface in the dashboard. As a best practice, place specific or narrow rules at the top and keep broader or catch-all rules toward the bottom. This ensures your intended mock responses are applied correctly, especially when multiple rules could match a similar request.

### Dashboard visibility[​](https://beeceptor.com/docs/create-mocking-server/#dashboard-visibility "Direct link to Dashboard visibility")

When a rule is successfully matched for a mocked response, a tickmark icon will appear alongside the request log on the dashboard. A single click allows you to review the specific rule that produced this match. To illustrate this feature, here's a quick demo.

### Programmatic insight[​](https://beeceptor.com/docs/create-mocking-server/#programmatic-insight "Direct link to Programmatic insight")

For those who programmatically utilize Beeceptor APIs to configure mock rules, you can find an HTTP header named `x-beeceptor-rule-id` within the mocked response. This header contains the rule ID that was matched to generate the HTTP response, providing you with invaluable insights for debugging and troubleshooting.
