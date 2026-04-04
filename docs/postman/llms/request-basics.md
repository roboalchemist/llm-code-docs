# Send a request with the Postman API client

Postman supports sending requests using HTTP, [GraphQL](/docs/sending-requests/graphql/graphql-overview/), [gRPC](/docs/sending-requests/grpc/grpc-client-overview/), [WebSocket](/docs/sending-requests/websocket/websocket-overview/), [MQTT](/docs/sending-requests/mqtt-client/mqtt-client-overview/), and [SOAP](/docs/sending-requests/soap/making-soap-requests/) protocols. Postman also supports AI-driven development with [AI requests in collections](/docs/postman-ai/ai-requests/overview/) and [AI Request blocks in Postman Flows](/docs/postman-ai/ai-request-blocks/overview/). You can also use Postman as your Model Context Protocol (MCP) client and [send requests to MCP servers](/docs/postman-ai/mcp-requests/overview/).

Start a new request by specifying the request type, then fill the details and test the request by clicking **Send**. After you save the request, you can share it with your team. You can also refer to [requests from publicly maintained workspaces](#leverage-public-api-examples) for the APIs you're testing and integrating with.

This topic primarily covers creating and sharing HTTP requests. For more detail about sending requests using other protocols, follow the respective links above.

## Create a new request

Your requests can include multiple details determining the data Postman sends to the API you're working with. Depending on the type of request, enter a URL and select a method (HTTP, GraphQL, gRPC, WebSocket, Socket.IO, or MQTT request) or select a model (AI request) or enter a command (MCP request), then specify other details.

You can create a new request from a workspace by clicking **New** and selecting the request type.

![Create new request](https://assets.postman.com/postman-docs/v11/create-new-http-v11-1.jpg)

Alternatively, click ![Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add** next to an open tab.

You can switch your request type by clicking the request icon next to the request name.

![Switch request type](https://assets.postman.com/postman-docs/v11/switch-request-type-v11.51.png)

You can't change the request protocol after you click **Save**.

To open an HTTP request quickly, click ![Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add request** from a collection in the sidebar.

![Add a request from a collection](https://assets.postman.com/postman-docs/v11/add-request-from-collection-v11.51.png)

Click **Save** to save your request. You can give your request a name and description, and choose or create a [collection](/docs/sending-requests/create-requests/intro-to-collections/) to save it in.

You can also specify values such as authorization, parameters and body data, and headers.

To test sending a request in Postman, set the URL to the [Postman Echo](/docs/developer/echo-api/) `https://postman-echo.com/get` endpoint, select the GET method, then click **Send**.

![New Request](https://assets.postman.com/postman-docs/v11/empty-request-v11-2.jpg)

You can turn on autosave to automatically save your changes to requests. Learn more about [autosave](/docs/getting-started/installation/settings/#application).

### Specify request URLs

Most requests you send in Postman require a URL that represents the API endpoint you're working with. Each operation you can perform using an API is typically associated with an endpoint. Each endpoint in an API is available at a specific URL. This is what you enter into Postman to access the API.

* If you're building an API, the URL is typically the base location plus path. For example, in the `https://postman-echo.com/get` request, `https://postman-echo.com` is the base URL, and `/get` is the endpoint path.
* If youâre using a public API, your API provider supplies the URLs you need, often located in their developer documentation.

As you start typing in the URL box, Postman displays a dropdown list of requests you've used before in your current workspace. The dropdown list also includes requests used in collections in your current workspace. Choose a request from the list of suggestions to autofill your request with details, such as parameters and authorizations.

If you're using a public API from a [verified team](/docs/postman-api-network/explore/consume/#choose-public-elements), suggestions display in the URL box after you enter the base URL, such as `https://api.getpostman.com`. You can click a suggested endpoint to autofill your request with a template of what you need to get started, such as parameters and authorization. Your request may autofill with an empty variable if the API publisher didn't define a value for the variable. Learn how to [set a value for an empty variable](/docs/sending-requests/variables/variables/#setting-values-for-variables-without-a-scope).

![Auto-suggest public API endpoints](https://assets.postman.com/postman-docs/v11/auto-suggest-public-api-v11-43.jpg)

Postman automatically adds `http://` to the start of your URL if you don't specify a protocol.

You can optionally enter *query* parameters in the URL box or enter them in the **Params** tab. If your request uses *path* parameters, you can enter them in the URL box. Learn more about [sending parameters and body data with API requests in Postman](/docs/sending-requests/create-requests/parameters/).

You can use [next generation URL encoding](/docs/sending-requests/create-requests/request-settings/#encode-your-request-urls) in your requests.

### Select request methods

By default, Postman selects the GET method for new request. GET methods typically retrieve data from an API. You can use a variety of other methods to send data to your APIs, including:

* **POST** - Add new data.
* **PUT** - Replace existing data.
* **PATCH** - Update existing data fields.
* **DELETE** - Delete existing data.

For example, if you're working with an API for a to-do list application, you might use a GET method to get the current list of tasks. You can then use a POST method to create a new task or use a PUT or PATCH method to edit an existing task.

Postman supports a number of extra request methods by default, and you can use custom methods. Click the method dropdown list, edit the method name text, and save your new method. To delete a method, hover over it in the list and click the delete icon ![Delete icon](https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke-small.svg#icon).

The same location (sometimes called *route*) can provide more than one endpoint by accepting different methods. For example, an API might have a POST `/customer` endpoint for adding a new customer, and a GET `/customer` endpoint for retrieving an existing customer.

## Send a request

After you specify the request protocol, method, and URL, add any other details required by the API you're sending the request to:

* Specify any [parameters and body data](/docs/sending-requests/create-requests/parameters/) or request [headers](/docs/sending-requests/create-requests/headers/) you need to send with the request.
* Set up any required [authentication and authorization](/docs/sending-requests/authorization/authorization/).
* You can also [use cookies with your requests](/docs/sending-requests/response-data/cookies/) by clicking **Cookies** (under **Send**).

After you enter all the request details, click **Send** to send the request to the API server. You can view the response from the server in the response pane. There you can use several tools to help you understand the response, like [search specific phrases](/docs/sending-requests/response-data/responses/#search) or [filter relevant information](/docs/sending-requests/response-data/responses/#filter) with JSONPath and XPath. Learn more about [API response structure in Postman](/docs/sending-requests/response-data/responses/).

You can view requests you've sent in **History** in the sidebar and send them again. You can also save and organize requests in a [collection](/docs/sending-requests/create-requests/intro-to-collections/).

![Send a request](https://assets.postman.com/postman-docs/v11/send-first-request-v11-35-4.jpg)

## Share your requests

You can share requests with collaborators by opening the request you want to share in the sidebar. Click ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** next to the request, then click **Share**. Learn more about [sharing your work in Postman](/docs/collaborating-in-postman/sharing/).

![Share request](https://assets.postman.com/postman-docs/v11/share-request-v11.24.jpg)

![Collections icon](https://assets.postman.com/postman-docs/Collections.png#icon) To try out a collection template that has a typical REST API, select [REST API Basics](https://www.postman.com/templates/collections/rest-api-basics/).

## Leverage public API examples

To help you get started faster, as you create requests, Postman searches the [Postman API Network](http://postman.com/explore) in the background for related content from popular collections and from collections owned by verified teams. If you're testing and integrating with public APIs and their relevant content is found, it shows up in the **Related requests** tab in the right sidebar.

For example, suppose you're testing an integration with Notion. Notion is a verified team, so you know you can trust their content.

1. Enter `api.notion.com/search` in the URL box. A dot appears next to ![Request icon](https://assets.postman.com/postman-docs/aether-icons/entity-request-stroke.svg#icon) **Related requests**.

    ![Trigger related requests](https://assets.postman.com/postman-docs/v11/related-requests-trigger-v11-14.jpg)

1. Click ![Related requests icon](https://assets.postman.com/postman-docs/v11/icon-related-request.jpg#icon) **Related requests**. A pane opens displaying Notion's example search-related requests with links to the API collections.

    ![Open related requests](https://assets.postman.com/postman-docs/v11/related-requests-open-v11-14.jpg)

You can view related documentation and example responses in place without navigating to a different page or window. You can also fork a collection and use it in your own workspace to test and reuse requests.

![Collections icon](https://assets.postman.com/postman-docs/Collections.png#icon) To try out a collection template that has a typical REST API, select [REST API Basics](https://www.postman.com/templates/collections/rest-api-basics/).

## Leverage public API examples

To help you get started faster, as you create requests, Postman searches the [Postman API Network](http://postman.com/explore) in the background for related content from popular collections and from collections owned by verified teams. If you're testing and integrating with public APIs and their relevant content is found, it shows up in the **Related requests** tab in the right sidebar.

For example, suppose you're testing an integration with Notion. Notion is a verified team, so you know you can trust their content.

1. Enter `api.notion.com/search` in the URL box. A dot appears next to ![Request icon](https://assets.postman.com/postman-docs/aether-icons/entity-request-stroke.svg#icon) **Related requests**.

    ![Trigger related requests](https://assets.postman.com/postman-docs/v11/related-requests-trigger-v11-14.jpg)

1. Click ![Related requests icon](https://assets.postman.com/postman-docs/v11/icon-related-request.jpg#icon) **Related requests**. A pane opens displaying Notion's example search-related requests with links to the API collections.

    ![Open related requests](https://assets.postman.com/postman-docs/v11/related-requests-open-v11-14.jpg)

You can view related documentation and example responses in place without navigating to a different page or window. You can also fork a collection and use it in your own workspace to test and reuse requests.

![Collections icon](https://assets.postman.com/postman-docs/Collections.png#icon) To try out a collection template that has a typical REST API, select [REST API Basics](https://www.postman.com/templates/collections/rest-api-basics/).

## Leverage public API examples

To help you get started faster, as you create requests, Postman searches the [Postman API Network](http://postman.com/explore) in the background for related content from popular collections and from collections owned by verified teams. If you're testing and integrating with public APIs and their relevant content is found, it shows up in the **Related requests** tab in the right sidebar.

For example, suppose you're testing an integration with Notion. Notion is a verified team, so you know you can trust their content.

1. Enter `api.notion.com/search` in the URL box. A dot appears next to ![Request icon](https://assets.postman.com/postman-docs/aether-icons/entity-request-stroke.svg#icon) **Related requests**.

    ![Trigger related requests](https://assets.postman.com/postman-docs/v11/related-requests-trigger-v11-14.jpg)

1. Click ![Related requests icon](https://assets.postman.com/postman-docs/v11/icon-related-request.jpg#icon) **Related requests**. A pane opens displaying Notion's example search-related requests with links to the API collections.

    ![Open related requests](https://assets.postman.com/postman-docs/v11/related-requests-open-v11-14.jpg)

You can view related documentation and example responses in place without navigating to a different page or window. You can also fork a collection and use it in your own workspace to test and reuse requests.

![Collections icon](https://assets.postman.com/postman-docs/Collections.png#icon) To try out a collection template that has a typical REST API, select [REST API Basics](https://www.postman.com/templates/collections/rest-api-basics/).

## Leverage public API examples

To help you get started faster, as you create requests, Postman searches the [Postman API Network](http://postman.com/explore) in the background for related content from popular collections and from collections owned by verified teams. If you're testing and integrating with public APIs and their relevant content is found, it shows up in the **Related requests** tab in the right sidebar.

For example, suppose you're testing an integration with Notion. Notion is a verified team, so you know you can trust their content.

1. Enter `api.notion.com/search` in the URL box. A dot appears next to ![Request icon](https://assets.postman.com/postman-docs/aether-icons/entity-request-stroke.svg#icon) **Related requests**.

    ![Trigger related requests](https://assets.postman.com/postman-docs/v11/related-requests-trigger-v11-14.jpg)

1. Click ![Related requests icon](https://assets.postman.com/postman-docs/v11/icon-related-request.jpg#icon) **Related requests**. A pane opens displaying Notion's example search-related requests with links to the API collections.

    ![Open related requests](https://assets.postman.com/postman-docs/v11/related-requests-open-v11-14.jpg)

You can view related documentation and example responses in place without navigating to a different page or window. You can also fork a collection and use it in your own workspace to test and reuse requests.

![Collections icon](https://assets.postman.com/postman-docs/Collections.png#icon) To try out a collection template that has a typical REST API, select [REST API Basics](https://www.postman.com/templates/collections/rest-api-basics/).

## Leverage public API examples

To help you get started faster, as you create requests, Postman searches the [Postman API Network](http://postman.com/explore) in the background for related content from popular collections and from collections owned by verified teams. If you're testing and integrating with public APIs and their relevant content is found, it shows up in the **Related requests** tab in the right sidebar.

For example, suppose you're testing an integration with Notion. Notion is a verified team, so you know you can trust their content.

1. Enter `api.notion.com/search` in the URL box. A dot appears next to ![Request icon](https://assets.postman.com/postman-docs/aether-icons/entity-request-stroke.svg#icon) **Related requests**.

    ![Trigger related requests](https://assets.postman.com/postman-docs/v11/related-requests-trigger-v11-14.jpg)

1. Click ![Related requests icon](https://assets.postman.com/postman-docs/v11/icon-related-request.jpg#icon) **Related requests**. A pane opens displaying Notion's example search-related requests with links to the API collections.

    ![Open related requests](https://assets.postman.com/postman-docs/v11/related-requests-open-v11-14.jpg)

You can view related documentation and example responses in place without navigating to a different page or window. You can also fork a collection and use it in your own workspace to test and reuse requests.

![Collections icon](https://assets.postman.com/postman-docs/Collections.png#icon) To try out a collection template that has a typical REST API, select [REST API Basics](https://www.postman.com/templates/collections/rest-api-basics/).

## Leverage public API examples

To help you get started faster, as you create requests, Postman searches the [Postman API Network](http://postman.com/explore) in the background for related content from popular collections and from collections owned by verified teams. If you're testing and integrating with public APIs and their relevant content is found, it shows up in the **Related requests** tab in the right sidebar.

For example, suppose you're testing an integration with Notion. Notion is a verified team, so you know you can trust their content.

1. Enter `api.notion.com/search` in the URL box. A dot appears next to ![Request icon](https://assets.postman.com/postman-docs/aether-icons/entity-request-stroke.svg#icon) **Related requests**.

    ![Trigger related requests](https://assets.postman.com/postman-docs/v11/related-requests-trigger-v11-14.jpg)

1. Click ![Related requests icon](https://assets.postman.com/postman-docs/v11/icon-related-request.jpg#icon) **Related requests**. A pane opens displaying Notion's example search-related requests with links to the API collections.

    ![Open related requests](https://assets.postman.com/postman-docs/v11/related-requests-open-v11-14.jpg)

You can view related documentation and example responses in place without navigating to a different page or window. You can also fork a collection and use it in your own workspace to test and reuse requests.

![Collections icon](https://assets.postman.com/postman-docs/Collections.png#icon) To try out a collection template that has a typical REST API, select [REST API Basics](https://www.postman.com/templates/collections/rest-api-basics/).

## Leverage public API examples

To help you get started faster, as you create requests, Postman searches the [Postman API Network](http://postman.com/explore) in the background for related content from popular collections and from collections owned by verified teams. If you're testing and integrating with public APIs and their relevant content is found, it shows up in the **Related requests** tab in the right sidebar.

For example, suppose you're testing an integration with Notion. Notion is a verified team, so you know you can trust their content.

1. Enter `api.notion.com/search` in the URL box. A dot appears next to ![Request icon](https://assets.postman.com/postman-docs/aether-icons/entity-request-stroke.svg#icon) **Related requests**.

    ![Trigger related requests](https://assets.postman.com/postman-docs/v11/related-requests-trigger-v11-14.jpg)

1. Click ![Related requests icon](https://assets.postman.com/postman-docs/v11/icon-related-request.jpg#icon) **Related requests**. A pane opens displaying Notion's example search-related requests with links to the API collections.

    ![Open related requests](https://assets.postman.com/postman-docs/v11/related-requests-open-v11-14.jpg)

You can view related documentation and example responses in place without navigating to a different page or window. You can also fork a collection and use it in your own workspace to test and reuse requests.

![Collections icon](https://assets.postman.com/postman-docs/Collections.png#icon) To try out a collection template that has a typical REST API, select [REST API Basics](https://www.postman.com/templates/collections/rest-api-basics/).

## Leverage public API examples

To help you get started faster, as you create requests, Postman searches the [Postman API Network](http://postman.com/explore) in the background for related content from popular collections and from collections owned by verified teams. If you're testing and integrating with public APIs and their relevant content is found, it shows up in the **Related requests** tab in the right sidebar.

For example, suppose you're testing an integration with Notion. Notion is a verified team, so you know you can trust their content.

1. Enter `api.notion.com/search` in the URL box. A dot appears next to ![Request icon](https://assets.postman.com/postman-docs/aether-icons/entity-request-stroke.svg#icon) **Related requests**.

    ![Trigger related requests](https://assets.postman.com/postman-docs/v11/related-requests-trigger-v11-14.jpg)

1. Click ![Related requests icon](https://assets.postman.com/postman-docs/v11/icon-related-request.jpg#icon) **Related requests**. A pane opens displaying Notion's example search-related requests with links to the API collections.

    ![Open related requests](https://assets.postman.com/postman-docs/v11/related-requests-open-v11-14.jpg)

You can view related documentation and example responses in place without navigating to a different page or window. You can also fork a collection and use it in your own workspace to test and reuse requests.

![Collections icon](https://assets.postman.com/postman-docs/Collections.png#icon) To try out a collection template that has a typical REST API, select [REST API Basics](https://www.postman.com/templates/collections/rest-api-basics/).

## Leverage public API examples

To help you get started faster, as you create requests, Postman searches the [Postman API Network](http://postman.com/explore) in the background for related content from popular collections and from collections owned by verified teams. If you're testing and integrating with public APIs and their relevant content is found, it shows up in the **Related requests** tab in the right sidebar.

For example, suppose you're testing an integration with Notion. Notion is a verified team, so you know you can trust their content.

1. Enter `api.notion.com/search` in the URL box. A dot appears next to ![Request icon](https://assets.postman.com/postman-docs/aether-icons/entity-request-stroke.svg#icon) **Related requests**.

    ![Trigger related requests](https://assets.postman.com/postman-docs/v11/related-requests-trigger-v11-14.jpg)

1. Click ![Related requests icon](https://assets.postman.com/postman-docs/v11/icon-related-request.jpg#icon) **Related requests**. A pane opens displaying Notion's example search-related requests with links to the API collections.

    ![Open related requests](https://assets.postman.com/postman-docs/v11/related-requests-open-v11-14.jpg)

You can view related documentation and example responses in place without navigating to a different page or window. You can also fork a collection and use it in your own workspace to test and reuse requests.

![Collections icon](https://assets.postman.com/postman-docs/Collections.png#icon) To try out a collection template that has a typical REST API, select [REST API Basics](https://www.postman.com/templates/collections/rest-api-basics/).

## Leverage public API examples

To help you get started faster, as you create requests, Postman searches the [Postman API Network](http://postman.com/explore) in the background for related content from popular collections and from collections owned by verified teams. If you're testing and integrating with public APIs and their relevant content is found, it shows up in the **Related requests** tab in the right sidebar.

For example, suppose you're testing an integration with Notion. Notion is a verified team, so you know you can trust their content.

1. Enter `api.notion.com/search` in the URL box. A dot appears next to ![Request icon](https://assets.postman.com/postman-docs/aether-icons/entity-request-stroke.svg#icon) **Related requests**.

    ![Trigger related requests](https://assets.postman.com/postman-docs/v11/related-requests-trigger-v11-14.jpg)

1. Click ![Related requests icon](https://assets.postman.com/postman-docs/v11/icon-related-request.jpg#icon) **Related requests**. A pane opens displaying Notion's example search-related requests with links to the API collections.

    ![Open related requests](https://assets.postman.com/postman-docs/v11/related-requests-open-v11-14.jpg)

You can view related documentation and example responses in place without navigating to a different page or window. You can also fork a collection and use it in your own workspace to test and reuse requests.

![Collections icon](https://assets.postman.com/postman-docs/Collections.png#icon) To try out a collection template that has a typical REST API, select [REST API Basics](https://www.postman.com/templates/collections/rest-api-basics/).

## Leverage public API examples

To help you get started faster, as you create requests, Postman searches the [Postman API Network](http://postman.com/explore) in the background for related content from popular collections and from collections owned by verified teams. If you're testing and integrating with public APIs and their relevant content is found, it shows up in the **Related requests** tab in the right sidebar.

For example, suppose you're testing an integration with Notion. Notion is a verified team, so you know you can trust their content.

1. Enter `api.notion.com/search` in the URL box. A dot appears next to ![Request icon](https://assets.postman.com/postman-docs/aether-icons/entity-request-stroke.svg#icon) **Related requests**.

    ![Trigger related requests](https://assets.postman.com/postman-docs/v11/related-requests-trigger-v11-14.jpg)

1. Click ![Related requests icon](https://assets.postman.com/postman-docs/v11/icon-related-request.jpg#icon) **Related requests**. A pane opens displaying Notion's example search-related requests with links to the API collections.

    ![Open related requests](https://assets.postman.com/postman-docs/v11/related-requests-open-v11-14.jpg)

You can view related documentation and example responses in place without navigating to a different page or window. You can also fork a collection and use it in your own workspace to test and reuse requests.

![Collections icon](https://assets.postman.com/postman-docs/Collections.png#icon) To try out a collection template that has a typical REST API, select [REST API Basics](https://www.postman.com/templates/collections/rest-api-basics/).

## Leverage public API examples

To help you get started faster, as you create requests, Postman searches the [Postman API Network](http://postman.com/explore) in the background for related content from popular collections and from collections owned by verified teams. If you're testing and integrating with public APIs and their relevant content is found, it shows up in the **Related requests** tab in the right sidebar.

For example, suppose you're testing an integration with Notion. Notion is a verified team, so you know you can trust their content.

1. Enter `api.notion.com/search` in the URL box. A dot appears next to ![Request icon](https://assets.postman.com/postman-docs/aether-icons/entity-request-stroke.svg#icon) **Related requests**.

    ![Trigger related requests](https://assets.postman.com/postman-docs/v11/related-requests-trigger-v11-14.jpg)

1. Click ![Related requests icon](https://assets.postman.com/postman-docs/v11/icon-related-request.jpg#icon) **Related requests**. A pane opens displaying Notion's example search-related requests with links to the API collections.

    ![Open related requests](https://assets.postman.com/postman-docs/v11/related-requests-open-v11-14.jpg)

You can view related documentation and example responses in place without navigating to a different page or window. You can also fork a collection and use it in your own workspace to test and reuse requests.

![Collections icon](https://assets.postman.com/postman-docs/Collections.png#icon) To try out a collection template that has a typical REST API, select [REST API Basics](https://www.postman.com/templates/collections/rest-api-basics/).

## Leverage public API examples

To help you get started faster, as you create requests, Postman searches the [Postman API Network](http://postman.com/explore) in the background for related content from popular collections and from collections owned by verified teams. If you're testing and integrating with public APIs and their relevant content is found, it shows up in the **Related requests** tab in the right sidebar.

For example, suppose you're testing an integration with Notion. Notion is a verified team, so you know you can trust their content.

1. Enter `api.notion.com/search` in the URL box. A dot appears next to ![Request icon](https://assets.postman.com/postman-docs/aether-icons/entity-request-stroke.svg#icon) **Related requests**.

    ![Trigger related requests](https://assets.postman.com/postman-docs/v11/related-requests-trigger-v11-14.jpg)

1. Click ![Related requests icon](https://assets.postman.com/postman-docs/v11/icon-related-request.jpg#icon) **Related requests**. A pane opens displaying Notion's example search-related requests with links to the API collections.

    ![Open related requests](https://assets.postman.com/postman-docs/v11/related-requests-open-v11-14.jpg)

You can view related documentation and example responses in place without navigating to a different page or window. You can also fork a collection and use it in your own workspace to test and reuse requests.

![Collections icon](https://assets.postman.com/postman-docs/Collections.png#icon) To try out a collection template that has a typical REST API, select [REST API Basics](https://www.postman.com/templates/collections/rest-api-basics/).

## Leverage public API examples

To help you get started faster, as you create requests, Postman searches the [Postman API Network](http://postman.com/explore) in the background for related content from popular collections and from collections owned by verified teams. If you're testing and integrating with public APIs and their relevant content is found, it shows up in the **Related requests** tab in the right sidebar.

For example, suppose you're testing an integration with Notion. Notion is a verified team, so you know you can trust their content.

1. Enter `api.notion.com/search` in the URL box. A dot appears next to ![Request icon](https://assets.postman.com/postman-docs/aether-icons/entity-request-stroke.svg#icon) **Related requests**.

    ![Trigger related requests](https://assets.postman.com/postman-docs/v11/related-requests-trigger-v11-14.jpg)

1. Click ![Related requests icon](https://assets.postman.com/postman-docs/v11/icon-related-request.jpg#icon) **Related requests**. A pane opens displaying Notion's example search-related requests with links to the API collections.

    ![Open related requests](https://assets.postman.com/postman-docs/v11/related-requests-open-v11-14.jpg)

You can view related documentation and example responses in place without navigating to a different page or window. You can also fork a collection and use it in your own workspace to test and reuse requests.

![Collections icon](https://assets.postman.com/postman-docs/Collections.png#icon) To try out a collection template that has a typical REST API, select [REST API Basics](https://www.postman.com/templates/collections/rest-api-basics/).

## Leverage public API examples

To help you get started faster, as you create requests, Postman searches the [Postman API Network](http://postman.com/explore) in the background for related content from popular collections and from collections owned by verified teams. If you're testing and integrating with public APIs and their relevant content is found, it shows up in the **Related requests** tab in the right sidebar.

For example, suppose you're testing an integration with Notion. Notion is a verified team, so you know you can trust their content.

1. Enter `api.notion.com/search` in the URL box. A dot appears next to ![Request icon](https://assets.postman.com/postman-docs/aether-icons/entity-request-stroke.svg#icon) **Related requests**.

    ![Trigger related requests](https://assets.postman.com/postman-docs/v11/related-requests-trigger-v11-14.jpg)

1. Click ![Related requests icon](https://assets.postman.com/postman-docs/v11/icon-related-request.jpg#icon) **Related requests**. A pane opens displaying Notion's example search-related requests with links to the API collections.

    ![Open related requests](https://assets.postman.com/postman-docs/v11/related-requests-open-v11-14.jpg)

You can view related documentation and example responses in place without navigating to a different page or window. You can also fork a collection and use it in your own workspace to test and reuse requests.

![Collections icon](https://assets.postman.com/postman-docs/Collections.png#icon) To try out a collection template that has a typical REST API, select [REST API Basics](https://www.postman.com/templates/collections/rest-api-basics/).

## Leverage public API examples

To help you get started faster, as you create requests, Postman searches the [Postman API Network](http://postman.com/explore) in the background for related content from popular collections and from collections owned by verified teams. If you're testing and integrating with public APIs and their relevant content is found, it shows up in the **Related requests** tab in the right sidebar.

For example, suppose you're testing an integration with Notion. Notion is a verified team, so you know you can trust their content.

1. Enter `api.notion.com/search` in the URL box. A dot appears next to ![Request icon](https://assets.postman.com/postman-docs/aether-icons/entity-request-stroke.svg#icon) **Related requests**.

    ![Trigger related requests](https://assets.postman.com/postman-docs/v11/related-requests-trigger-v11-14.jpg)

1. Click ![Related requests icon](https://assets.postman.com/postman-docs/v11/icon-related-request.jpg#icon) **Related requests**. A pane opens displaying Notion's example search-related requests with links to the API collections.

    ![Open related requests](https://assets.postman.com/postman-docs/v11/related-requests-open-v11-14.jpg)

You can view related documentation and example responses in place without navigating to a different page or window. You can also fork a collection and use it in your own workspace to test and reuse requests.

![Collections icon](https://assets.postman.com/postman-docs/Collections.png#icon) To try out a collection template that has a typical REST API, select [REST API Basics](https://www.postman.com/templates/collections/rest-api-basics/).

## Leverage public API examples

To help you get started faster, as you create requests, Postman searches the [Postman API Network](http://postman.com/explore) in the background for related content from popular collections and from collections owned by verified teams. If you're testing and integrating with public APIs and their relevant content is found, it shows up in the **Related requests** tab in the right sidebar.

For example, suppose you're testing an integration with Notion. Notion is a verified team, so you know you can trust their content.

1. Enter `api.notion.com/search` in the URL box. A dot appears next to ![Request icon](https://assets.postman.com/postman-docs/aether-icons/entity-request-stroke.svg#icon) **Related requests**.

    ![Trigger related requests](https://assets.postman.com/postman-docs/v11/related-requests-trigger-v11-14.jpg)

1. Click ![Related requests icon](https://assets.postman.com/postman-docs