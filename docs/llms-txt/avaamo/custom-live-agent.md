# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent/custom-live-agent.md

# Custom live agent

Avaamo Platform provides pre-built live agent integration with Avaamo, Oracle Right Now, and Zendesk. However, if you wish to transfer to a live agent other than those available, then you can configure a custom live agent. When you configure a custom live agent in the Avaamo platform, you also provide a webhook URL that is used as an endpoint to send and receive requests and responses to and from the Avaamo platform.&#x20;

When the user interacts with the virtual assistant and requests to speak to a live agent, the request is sent to the live agent (chat application) via a webhook call. The **Live agent integrator** is used to transform the payloads to and from the Avaamo platform and the **Custom live agent** respectively.&#x20;

The following diagram illustrates the data flow between the user, Avaamo platform, and Custom live agent:&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbHax3GgGAsZ5nE5ZRA%2F-MbK2v7ADjvj-97JwFFi%2F5.7-custom-live-agent.png?alt=media\&token=0eef72a3-9efa-48a2-a17d-3a58a7f17722)

{% hint style="info" %}
**Note**: Currently, you cannot [transfer to a live agent](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent) that is configured in the Avaamo Platform from the C-IVR channel. Instead, it is recommended that you use [Call forward](https://docs.avaamo.com/user-guide/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses#call-forward) for connecting to live agents.
{% endhint %}

## Configure custom live agent

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can configure a custom live agent immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.
* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing.
    {% endhint %}

**To configure a custom live agent:**

* In the **Agent** page, navigate to the **Configuration -> Live Agent** option in the left navigation menu.
* Move the slider to **Yes** to **enable** the live agent feature.
* In the **Select a Live Agent System** dropdown, select **Custom** from the dropdown list.
* Enter the **Webhook URL** of the live agent application you are using.
* Enter any additional key-value pairs in the format `key:value` that must be passed in the **Header** for authenticating the request from the Avaamo platform to the live agent application. This field is optional and currently, only one key-value pair is supported.
* Click **Save** to save custom live agent settings. An API **Access Token** is generated that is used for communication between Avaamo Platform and custom live agent.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-Q6SJHntlRMcWD_Js8%2F-M-Q81c63Xu1iAkOCV8R%2Fcustom-live-agent-configuration.png?alt=media\&token=38adc4f4-51e7-4420-ae92-51952d489aa4)

{% hint style="info" %}
**Notes:**

* You can configure only a single live agent for an Avaamo Agent.
* You cannot delete the configured live agent on the platform, you can only disable it. Move the **Enable** slider button on the top. It moves to **No**.
* To change a live agent, you can edit the agent in the **Agent** page and select a new live agent.
* You can also configure a **Live agent avatar**, **Automated Messages**, **Live Agent Transfer Rules**, **Working Hours**, **Callbacks**, and **Agent Transcripts**. See [Pre-built Live Agent](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent/pre-built-live-agent), for more information.
  {% endhint %}

{% hint style="success" %}
**Key Point**: Make a note of the **API access token** and **Webhook URL**. These are used for communications between the Avaamo Platform and custom live agents.
{% endhint %}

## OAuth2 authorization

In scenarios where the connection to the custom live agent is not directly exposed and available only through an OAuth2 provider, the Avaamo platform provides you the option to connect to a custom live agent using the authorization token issued by the OAuth2 provider.&#x20;

### Pre-requisite

* The first step is to register the Avaamo application with the OAuth2 provider. Registration allows the OAuth2 provider to uniquely identify the Avaamo application.&#x20;
* Make a note of the client ID and client secret. The app needs these keys when negotiating for access tokens with the authorization server.

### Enable **OAuth2 authorization**&#x20;

After registering the application with the OAuth2 provider, the next step is to configure the custom live agent system with OAuth2 details in the Avaamo platform:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbK5agJziLQ5w8dZf3B%2F-MbK5rzq-sl7CnXt5rMF%2F5.7-custom-live-agent-oauth2-settings.png?alt=media\&token=f2119127-5db8-40c9-ab30-4c290915f61f)

**To enable OAuth2 authorization in custom live agent**:

* In the **Live agent** page, toggle the OAuth2 authorization slider to enable OAuth2 authorization. Note that this is visible only when you select **Custom** as the Live agent.
* Specify the following details for OAuth2 authorization:

<table><thead><tr><th width="169.9442832269298">Parameters</th><th width="588.4285714285713">Description</th></tr></thead><tbody><tr><td>Client ID</td><td>The client ID obtained after registering the Avaamo application with the OAuth2 provider. </td></tr><tr><td>Client secret key</td><td>The client secret key obtained after registering the Avaamo application with the OAuth2 provider. </td></tr><tr><td>Authorization URL</td><td>This is the URL from the OAuth2 provider used to obtain authorization for the Avaamo application.</td></tr></tbody></table>

* Click **Save** to the OAuth2 details.

### How does **OAuth2 authorization work?**

The following diagram illustrates the steps on how the authorization token can be obtained from the OAuth2 provider and passed through different layers when a live agent chat with the custom live agent is requested from an Avaamo agent:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbK4SW4p-4ehZ30bO_I%2F-MbK4ojqxXJTSOg7I4Ed%2F5.7-custom-live-agent-oauth2-flow.png?alt=media\&token=99744129-16ee-48a2-97ee-ee5b5d3631d5)

* User requests transfer to the custom live agent
* Avaamo requests an authorization token from the OAuth2 provider using the Authorization URL, Client ID, and Client secret key. See [Enable OAuth2 authorization](#enable-oauth2-authorization), for more information.
* OAuth2 provides the authorization token.
* Avaamo connects to the custom live agent using the authorization token. The "Authorization: Bearer \<token>" will be sent as a part of the request headers while making HTTP requests to the custom live agent webhook URL.

{% hint style="info" %}
**Note:** Making API calls using the OAuth 2.0 access token may encounter errors if the access token is no longer valid because the token expired or was revoked. In this case, the resource server will return a 4xx error code. In this case, steps 2 and 3 get repeated, to get the new access token using the client secret key.
{% endhint %}

## Live agent request

When a user requests a transfer of the conversation from the **Avaamo Agent** to the **Live Agent**, the **Avaamo Agent** sends a webhook call via the webhook endpoint to the chat application used for the live agent. The live agent then responds with API to accept the request. The basic flow of the live agent request is illustrated in the diagram below:

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LrCijkwNUzYwRBxLEtQ%2F-LrD9K9PzmIo5qIUq5BG%2Flive-agent-basic-flow.png?alt=media&#x26;token=cfdf06bc-fedb-4138-92d2-53dd7e04014b" alt=""></div>

The four requests that get processed during the interaction between Avaamo Platform and custom live agent are:

* [Chat request](#chat-request): New chat request sent over the Webhook URL.
* [Accept request](#accept-request): Chat request is accepted by sending an API request to accept the chat in response to the webhook call request. A corresponding payload is sent over the Webhook URL once the chat is accepted.
* [Chat in-progress](#chat-in-progress): After the request is accepted by the custom live agent, the user can communicate with the custom live agent by sending messages via the Avaamo Agent. The live agent responds by sending a message to the user from the live agent via API.
* [End request](#end-request): A live agent session can be terminated via API request and the corresponding message is received by the user interacting with the Avaamo Agent.

### Chat request

Consider that you wish to transfer to a live agent while interacting with **Mac Pizza Agent**:

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LrDChbKuJR61xBqUqYW%2F-LrDCsOjFUfP_Pl4-nRj%2Flive-agent-transfer.png?alt=media&#x26;token=9ee71636-93c3-4ab4-8c6f-043b42cc0da7" alt=""></div>

When a user sends a transfer request to a custom live agent, the following payload is sent over the Webhook URL:

```yaml
{
  "event": {
    "uuid": "3bb91e19-e734-4593-b458-9b4a4b8b777b",
    "event_type": "new_chat_request",
    "created_at": 1571122425.9567587,
    "chat_request": {
      "uuid": "6a2d01cc-126d-4f00-bbcf-4c281bff4374"
    },
    "conversation": {
      "uuid": "e3889415d95b7ffc7a00e0048265c4b9",
      "display_name": "John,Mac Pizza Agent"
    },
    "bot": {
      "uuid": "4a94ec00-c368-4e1b-946a-e8cc04172812",
      "display_name": "Mac Pizza Agent ",
      "description": "Order Pizzas and more"
    },
    "user": {
      "first_name": "John",
      "last_name": "C",
      "email": null,
      "custom_properties": {},
      "display_name": "John C",
      "layer_id": "dashboard_admin_test_user_273",
      "device": {
        "device_uuid": "fc12568a-f5dd-468c-bc88-d800ce2d362c",
        "channel_name": "web",
        "last_visited_page": "https://cx.avaamo.com/"
      }
    }
  }
}
```

See [Payload parameters](#payload-parameters), for more details on the payload parameters.

#### **Retrieve requests**

You can retrieve all of the current chat requests sent by the **Avaamo agent** to the live agent using the following API:

* **URL:** `https://cx.avaamo.com/live_agent/custom/conversations/requests.json?access_token=<token>`, **access\_token** is the API Access Token as generated by Avaamo Platform while configuring a custom live agent. See [Configure Custom Live Agent](#configure-custom-live-agent), for more information.
* **Method**: GET
* **Success response code:** 200
* **Response**: In response, the requests are an array of all the chat requests sent by the **Avaamo agent** to the live agent. The following is a sample JSON response received:

```yaml
{
  "requests": [
    {
      "uuid": "6a2d01cc-126d-4f00-bbcf-4c281bff4374",
      "created_at": 1571122425,
      "conversation": {
        "uuid": "e3889415d95b7ffc7a00e0048265c4b9",
        "display_name": "John,Mac Pizza Agent"
      },
      "user": {
        "first_name": "John",
        "last_name": "C",
        "email": null,
        "custom_properties": {
          "email": "john@avaamo.com"
        },
        "display_name": "John C",
        "layer_id": "dashboard_admin_test_user_273",
        "device": {
          "device_uuid": "fc12568a-f5dd-468c-bc88-d800ce2d362c",
          "channel_name": "web",
          "last_visited_page": "https://cx.avaamo.com/"
        }
      }
    }
  ]
}
```

See [Payload parameters](#payload-parameters), for more details on the parameters sent in the API.&#x20;

{% hint style="success" %}
**Key Points**:

* The event\_type for a new chat request is **new\_chat\_request**.
* Make a note of **conversation\_uuid**. This is used in the API when a chat request is accepted
  {% endhint %}

### Accept request

The live agent request is accepted by sending the following API in response to the webhook call request:

* **URL**: `https://cx.avaamo.com/live_agent/custom/conversations/<conversation_uuid>/accept_chat.json?access_token=<token>`
  * **access\_token** is the API Access Token as generated by the Avaamo platform while configuring custom live agents. See [Configure Custom Live Agent](#configure-custom-live-agent), for more information.
  * **conversation\_uuid** is the unique conversation identifier generated per user. Use the conversation\_uuid as generated when a chat request is sent. See [Chat Request](#chat-request), for more information.
* **Method**: PUT
* **Success response code:** 200
* **Response**: The following is a sample JSON response:

```yaml
{
  "conversation": {
    "uuid": "e3889415d95b7ffc7a00e0048265c4b9",
    "display_name": "John,Mac Pizza Agent"
  }
}
```

See [Payload parameters](#payload-parameters), for more details on the response parameters.

When the live agent chat request is accepted the following payload is sent over the Webhook URL:

```yaml
{
  "event": {
    "uuid": "ac8a48f9-020a-40c4-a254-d7e34b79cc83",
    "event_type": "chat_request_accepted",
    "created_at": 1571123874.0260987,
    "chat_request": {
      "uuid": "6a2d01cc-126d-4f00-bbcf-4c281bff4374"
    },
    "conversation": {
      "uuid": "e3889415d95b7ffc7a00e0048265c4b9",
      "display_name": "John,Mac Pizza Agent"
    }
  }
}
```

See [Payload parameters](#payload-parameters), for more details on the payload parameters.

{% hint style="success" %}
**Key Points**:

* The event\_type for an accepted chat request is **chat\_request\_accepted.**
* Chat requests must be accepted for users to interact with a live agent. If a chat request is on hold or rejected, then the corresponding messages as configured in the live agent are displayed and the conversation is returned back to the **Avaamo Agent**.
  {% endhint %}

### Chat in-progress

After the request is accepted by the custom live agent, the user can communicate with the custom live agent by sending a message via the Avaamo Agent.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LrDIwQ4H0pQC7je0cmB%2F-LrDKPOUiyVUNtH6FZ4g%2Fchat-in-progress.png?alt=media&#x26;token=7e8de8d2-e8d8-4a57-9b45-e17cf8505483" alt=""></div>

The following payload is sent over the Webhook URL:

```yaml
{
  "event": {
    "uuid": "52e82a8b-76e6-4acf-aac1-36f64ec11a9e",
    "event_type": "user_message",
    "created_at": 1571124083.4281275,
    "conversation": {
      "uuid": "e3889415d95b7ffc7a00e0048265c4b9",
      "display_name": "John,Mac Pizza Agent"
    },
    "message": {
      "uuid": "a7b34601-8031-49ac-a9d7-6c4c5e9d93b3",
      "content": "I am unable to place order",
      "content_type": "text",
      "created_at": 1571124082.887109
    }
  }
}
```

* In the URL, access\_token is the API Access Token as generated by the Avaamo platform while configuring custom live agents. See [Configure custom live agent](#configure-custom-live-agent), for more information.
* See [Payload parameters](#payload-parameters), for more details on the payload parameters.

The live agent responds by sending a message to the user from the live agent via API:

* **URL**: `https://cx.avaamo.com/live_agent/custom/messages.json?access_token=<token>`
* **Method**: POST
* **Data**:

```yaml
{
  "message": {
    "conversation": {
      "uuid": "e3889415d95b7ffc7a00e0048265c4b9"
    },
    "content": "Can you elaborate more on the order you were trying to place?",
    "content_type": "text"
  }
}

Response: HTTP 200 - Success
{
  "message": {
    "uuid": "535b13ab-b8a4-4592-83a6-2a051228c0fd",
    "content": "Can you elaborate more on the order you were trying to place?",
    "content_type": "text",
    "created_at": 1571124908.184577
  }
}

```

See [Payload parameters](#payload-parameters), for more details on the API request and responses.

Correspondingly, the following message is received in the Avaamo Agent:

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LrDIwQ4H0pQC7je0cmB%2F-LrDLbEsBAXcCZtJGGjp%2FScreenshot%202019-10-15%20at%201.07.53%20PM.png?alt=media&#x26;token=bd3a8bd1-41c3-4cfc-8ffe-f41144a7afbd" alt=""></div>

### End request

A live agent session can be terminated using the following API:

* **URL**: `https://cx.avaamo.com/live_agent/custom/conversations/<conversation_uuid>/end_chat.json?access_token=<token>`
  * **access\_token** is the API Access Token as generated by the Avaamo platform while configuring custom live agents. See [Configure Custom Live Agent](https://docs.avaamo.com/user-guide/how-to/build-agents/deploy/custom-channel#configure-custom-channel), for more information.
  * **conversation\_uuid** is the unique conversation identifier generated per user. Use the conversation\_uuid as generated when a chat request is sent. See [Chat Request](#chat-request), for more information.
* **Method:** DELETE
* **Response:** HTTP 204 No content - Success

Correspondingly, the following message is received in the Avaamo Agent:

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LrDIwQ4H0pQC7je0cmB%2F-LrDMp0et2Eusys94QF4%2FScreenshot%202019-10-15%20at%201.12.54%20PM.png?alt=media&#x26;token=fc35b4d4-1098-411d-9f09-c967ffa747ec" alt=""></div>

When the live agent chat is terminated, the following payload is sent over the webhook URL -

```yaml
{
  "event": {
    "uuid": "049c4d77-ec3d-4e89-954d-7242836a9bd0",
    "event_type": "chat_terminated",
    "created_at": 1571125260.8660843,
    "conversation": {
      "uuid": "e3889415d95b7ffc7a00e0048265c4b9",
      "display_name": "John,Mac Pizza Agent"
    },
    "bot": {
      "uuid": "4a94ec00-c368-4e1b-946a-e8cc04172812",
      "display_name": "Mac Pizza Agent ",
      "description": "Order Pizzas and more"
    },
    "user": {
      "first_name": "John",
      "last_name": "C",
      "email": null,
      "custom_properties": {},
      "display_name": "John C",
      "layer_id": "dashboard_admin_test_user_273",
      "device": {
        "device_uuid": "fc12568a-f5dd-468c-bc88-d800ce2d362c",
        "channel_name": "web",
        "last_visited_page": "https://cx.avaamo.com/"
      }
    }
  }
}
```

See [Payload Parameters](#payload-parameters), for more details on the payload parameters.

{% hint style="info" %}
**Note -** The message uuid, event uuid, conversation uuid, user uuid, are all unique identifiers and help differentiate between users and conversations.
{% endhint %}

### **Payload parameters**

The webhook calls and APIs use the following parameters to process a request:

<table><thead><tr><th width="220.83408154351974">Parameters</th><th width="543.484516489973">Description</th></tr></thead><tbody><tr><td>event</td><td><p>Indicates the event details -</p><ul><li><strong>uuid</strong>: Indicates a unique Id assigned for the event.</li><li><strong>event_type</strong>: Indicates the type of event. The following are the supported event types - new_chat_request, chat_request_accepted, user_message, and chat_terminated.</li><li><strong>created_at</strong>: Indicates the created date and time of the event in seconds.</li><li><strong>chat_request/uuid</strong>: Indicates a unique Id of the chat request.</li></ul></td></tr><tr><td>conversation/uuid</td><td>Indicates a unique identifier of conversation per user. Note that conversation/uuid is different for each user.</td></tr><tr><td>display_name</td><td>Indicates display name of the conversation in the following format: <strong>&#x3C;&#x3C;Avaamo Agent Display Name>>, &#x3C;&#x3C;User First Name>></strong>.</td></tr><tr><td>bot</td><td><p>Indicated the details of the <strong>Avaamo Agent</strong>.</p><ul><li><strong>bot_uuid</strong>: Indicates a unique identifier of the agent.</li><li><strong>display_name</strong>: Indicates the display name of the agent as specified while creating the agent.</li><li><strong>description</strong>: Indicates the description of the agent as specified while creating the agent.</li></ul></td></tr><tr><td>user</td><td><p>Indicates the user details sending the request to the <strong>Avaamo Agent</strong> -</p><ul><li><strong>uuid</strong>: Indicates a unique Id assigned to the user.</li><li><strong>first_name</strong>: Indicates the first name sent in the incoming request by the user.</li><li><strong>last_name</strong>: Indicates the last name sent in the incoming request by the user. If the last name is not available, then the last name is null.</li><li><strong>email</strong>: Indicates the user’s email address.</li><li><strong>layer_id</strong>: Indicates an internal user Id used by the Avaamo platform.</li><li><strong>custom_properties</strong>: Indicates any custom key-value pairs that are sent in the payload by the custom channel and returned in the callbacks.</li><li><strong>display_name</strong>: Indicates the display name of the user.</li></ul></td></tr><tr><td>device</td><td><p>Indicated the details of the device -</p><ul><li><strong>device_uuid</strong>: Indicates a unique identifier of the device.</li><li><strong>channel_name</strong>: Indicates the channel where the user is interacting with the <strong>Avaamo Agent</strong>.</li><li><strong>last_visited_page</strong>: Indicates the URL of the last page visited by the user.</li></ul></td></tr><tr><td>message</td><td><p>Indicates the message details by the user and the <strong>Avaamo Agent</strong>.</p><ul><li><strong>uuid</strong>: Indicates a unique identifier of the message</li><li><strong>content</strong>: Indicates the content of the message.</li><li><strong>content_type</strong>: Indicates the content type of the message. Currently, only text is supported.</li><li><strong>created_at</strong>: Indicates the created date and time of the event in seconds.</li></ul></td></tr></tbody></table>

## Test custom live agent

With the custom live agent configured for your **Avaamo agent**, you can test the live agent to gain user perspective:

* Test the agent by clicking on the icon at the bottom right corner of the **Dialog Studio** page.
* Ask for a live agent and check if the **Avaamo agent** is able to transfer the conversation.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LrDChbKuJR61xBqUqYW%2F-LrDCsOjFUfP_Pl4-nRj%2Flive-agent-transfer.png?alt=media&#x26;token=9ee71636-93c3-4ab4-8c6f-043b42cc0da7" alt=""></div>

* Check if the appropriate payload is sent over the Webhook URL as configured in the custom live agent settings.
* You can retrieve all of the current chat requests sent by the **Avaamo agent** on the live agent with the following API: `https://cx.avaamo.com/live_agent/custom/conversations/requests.json?access_token=<token>`
* Check on your live agent if the agent is able to accept the conversation. When the chat request is accepted, a payload is sent over the Webhook URL as configured in the custom live agent settings.
* Test for the payload sent over the Webhook URL and the response from the live agent via API during chat conversations, once the request is accepted. See [Chat In-Progress](#chat-in-progress), for more information.

{% hint style="success" %}
**Key Points**:

* You can test the APIs using a tool like **Postman**.
* You can test webhooks by generating a sample API URL from any webhook tester sites such as from **Webhook.site**.
  {% endhint %}

## Troubleshooting tips

In cases where you are unable to receive the expected **Avaamo agent** response, refer to the following troubleshooting tips:

1. Ensure that the live agent feature is enabled.
2. Ensure the right webhook URL is entered.
3. Ensure the correct API token is used parsed.
4. You can retrieve all of the current chat requests sent by the **Avaamo Agent** on the live agent using the following API: `https://cx.avaamo.com/live_agent/custom/conversations/requests.json?access_token=<token>`
5. You can also use **ngrok** to help with development and debugging.
6. If you are using any tool such as **Postman** to verify the HTTP request, then you can also check for the standard HTTP error codes in the response. Contact **Avaamo Operations Team**, for further assistance.
