# Source: https://docs.xano.com/building/logic/apis.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Building APIs in Xano

> Learn how to build APIs with no code, with code, or with AI, all in Xano

<Tip>
  Before continuing, make sure you're familiar with:

  * [Core Components](/building/logic/core-components)
  * [Working with Data](/building/logic/working-with-data)

  If you need a primer on what an API is, we've added a quick summary below. For more detailed information, check out [What is an API](/before-you-begin/key-concepts#-api) in the Before You Begin section.
</Tip>

## Building APIs in Xano

APIs are a core part of any backend. They allow you to connect your backend to other services and applications.

Each API is assigned a name, a verb, and a URL.

* The name is the unique identifier for the API. For example, `user_list`. We'll be referencing this sample API throughout the rest of this page.
* The verb is the HTTP verb that will be used to make the request. For example, `GET`.
* The URL is the endpoint that the API will be accessed at. For example, `https://myapi.com/user_list`.

APIs in Xano are built in three parts:

* Inputs
  \-- Inputs are the data that the API will accept. For example, `name` and `email`.

* Logic
  \-- The logic is the logic that will be executed when the API is called. For example, retrieving a record from your database or calculating a user's age.

* Response
  \-- The response is the data that the API will return. For our `user_list` API, it might return a list of users, or a single user.

## API Groups

APIs live inside of API groups. Think of groups as folders that you can use to organize all of your different APIs. For example, you might have a group for your authentication APIs, a group for your user APIs, and a group for file storage APIs.

### Creating a new API Group

<Steps>
  <Step>
    From the left-hand menu, click **API**, and then click **+ Add API Group**.
    <Frame>    <img src="https://mintcdn.com/xano-997cb9ee/_YwYe_syRaE7iZGt/images/apis-20251013-101018.png?fit=max&auto=format&n=_YwYe_syRaE7iZGt&q=85&s=5dcab9d35c81dc5a15487cfa7dea2796" alt="apis-20251013-101018" width="1437" height="546" data-path="images/apis-20251013-101018.png" /></Frame>
  </Step>

  <Step>
    In the panel that opens, give your API group a name. You can also provide a description, tags for organization, and choose whether or not to make auto-generated API documentation available for this group.

    <Tabs>
      <Tab title="Visually" icon="hammer-brush">
        <Frame>        <img src="https://mintcdn.com/xano-997cb9ee/_YwYe_syRaE7iZGt/images/apis-20251013-101155.png?fit=max&auto=format&n=_YwYe_syRaE7iZGt&q=85&s=c7c138aa47de4826d89cffbb9beecf46" alt="apis-20251013-101155" width="490" height="529" data-path="images/apis-20251013-101155.png" /></Frame>

        | Parameter                       | Description                                                                                                                                                                                                                                                                        |
        | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        | name                            | The name of the API group. This comes immediately after the `api_group` definition, and before the opening curly brace.                                                                                                                                                            |
        | description                     | A description of the API group.                                                                                                                                                                                                                                                    |
        | tags                            | Tags for organization.                                                                                                                                                                                                                                                             |
        | Swagger (OpenAPI) Documentation | Options for auto-generated API documentation. By default, it will be public, non-tokenized documentation. You can switch to tokenized documentation by clicking the toggle and choosing "Private (requires token)", or disable it by clicking the toggle and selecting "Disabled". |
      </Tab>

      <Tab title="With Code" icon="code">
        You can also create an API group using XanoScript.

        ```javascript  theme={null}
            api_group my_new_API_group {
                description = "This is an awesome API group with awesome APIs"
                tags = ["awesome"]
                canonical = "awesome"
                history = {inherit: true}
                }
        ```

        | Parameter   | Description                                                                                                                                                                                                                                                                                            |
        | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
        | name        | The name of the API group. This comes immediately after the `api_group` definition, and before the opening curly brace.                                                                                                                                                                                |
        | description | A description of the API group.                                                                                                                                                                                                                                                                        |
        | canonical   | The canonical ID of the API group.                                                                                                                                                                                                                                                                     |
        | swagger     | Options for auto-generated API documentation. If not provided, it will default to public, non-tokenized documentation.<br /><br />Use `swagger = {token: "<token_here>"}` to create tokenized documentation.<br /><br />Use `  swagger = {active: false}` to disable auto-generated API documentation. |
        | tags        | Tags for organization.                                                                                                                                                                                                                                                                                 |
        | history     | The request history settings for the API group. Defaults to `{inherit: true}`, which means it will inherit the request history settings from the workspace.                                                                                                                                            |

        <Info>
          The canonical ID is used to generate the endpoint URLs for the APIs in this group. If not provided, Xano will auto-generate one for you.

          For example, if the canonical ID is set to `awesome`, the base URL for the APIs in this group will be `https://yourdomain.com/api:awesome/api_name`.
        </Info>
      </Tab>
    </Tabs>
  </Step>
</Steps>

## Creating a new API

Clicking the **+ Add API Endpoint** button will open a panel that allows you to create a new API.

You can choose from one of the following options:

| Type                                                            | Description                                                                                                |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| <Icon icon="pen-to-square" size={18} /> **Custom Endpoint**     | Creates a blank canvas for you to build your API from scratch.                                             |
| <Icon icon="plug" size={18} /> **External API request**         | Creates a pre-built API for making requests to external APIs.                                              |
| <Icon icon="database" size={18} /> **CRUD Database Operations** | Creates a pre-built API for performing CRUD operations (Create, Read, Update, Delete) on a database table. |
| <Icon icon="webhook" size={18} /> **Webhook**                   | Creates a pre-built API for receiving webhooks from external services.                                     |
| <Icon icon="user" size={18} /> **Authentication**               | Creates a pre-built API for authentication.                                                                |
| <Icon icon="upload" size={18} /> **Upload Content**             | Creates a pre-built API for uploading files, such as images or attachments.                                |
| <Icon icon="file-code" size={18} /> **HTML Page**               | Creates a pre-built API for serving HTML pages.                                                            |
| <Icon icon="code" size={18} /> **Use XanoScript**               | Opens the XanoScript editor so you can build your API from scratch.                                        |

You'll be asked to provide some basic information about your API before continuing.

<Frame><img src="https://mintcdn.com/xano-997cb9ee/_YwYe_syRaE7iZGt/images/apis-20251013-103441.png?fit=max&auto=format&n=_YwYe_syRaE7iZGt&q=85&s=7d3cb2312eb22a47bb78b74123649d7f" alt="apis-20251013-103441" width="487" height="483" data-path="images/apis-20251013-103441.png" /></Frame>

| Parameter      | Description                                                                                           |
| -------------- | ----------------------------------------------------------------------------------------------------- |
| Name           | The name of the API.                                                                                  |
| Verb           | The HTTP verb that will be used to make the request.                                                  |
| Description    | A description of the API.                                                                             |
| Tags           | Tags for organization.                                                                                |
| Authentication | Choose whether this endpoint requires a valid authentication token present in the headers to execute. |

You can build APIs in Xano in three different ways. Choose the one that best fits your needs. You can switch between them at any time.

<Tabs>
  <Tab title="Canvas View" icon="hammer-brush">
    ## The Canvas View

    <Tip>
      The canvas view is a visual representation of your API in a node-based format. If you're new to the canvas view, review the [Canvas View](/building/build-visually/canvas-view) basics first.
    </Tip>

    <Steps>
      <Step title="Add Inputs to define what your API accepts">
        <Frame>        <img src="https://mintcdn.com/xano-997cb9ee/_YwYe_syRaE7iZGt/images/apis-20251013-103714.png?fit=max&auto=format&n=_YwYe_syRaE7iZGt&q=85&s=9be1c801b5c70e2272265b342f158b59" alt="apis-20251013-103714" width="1147" height="684" data-path="images/apis-20251013-103714.png" /></Frame>

        <Card title="Learn how to work with Inputs" href="/building/logic/core-components/inputs">
          Inputs define the data your API expects. Learn how to add and configure them.
        </Card>
      </Step>

      <Step title="Build your logic in the Function Logic or Canvas View">
        <Card title="Learn how to work with Functions" href="/building/logic/core-components/functions">
          Functions define the behavior of your API. Add and arrange functions to process inputs and fetch data.
        </Card>
      </Step>

      <Step title="Define what your API returns with the Response">
        <Card title="Learn how to configure Responses" href="/building/logic/core-components/response">
          Control exactly what data your API sends back.
        </Card>
      </Step>
    </Steps>

    <Frame caption="Here's an example of a basic API in the canvas view">    <img src="https://mintcdn.com/xano-997cb9ee/_YwYe_syRaE7iZGt/images/apis-20251013-112630.png?fit=max&auto=format&n=_YwYe_syRaE7iZGt&q=85&s=fd03ddedf36e58cf8f6305714a0f632b" alt="apis-20251013-112630" width="1362" height="449" data-path="images/apis-20251013-112630.png" /></Frame>
  </Tab>

  <Tab title="Function Stack" icon="code">
    <Steps>
      <Step title="Add Inputs to define what your API accepts">
        <Frame>        <img src="https://mintcdn.com/xano-997cb9ee/NgWyYUIOE6OPGYha/images/inputs-20251013-105146.png?fit=max&auto=format&n=NgWyYUIOE6OPGYha&q=85&s=4a81cfc50ad2023829f3b5b6252e00a2" alt="apis-20251013-103714" width="995" height="558" data-path="images/inputs-20251013-105146.png" /></Frame>

        <Card title="Learn how to work with Inputs" href="/building/logic/core-components/inputs">
          Inputs define the data your API expects. Learn how to add and configure them.
        </Card>
      </Step>

      <Step title="Build your logic in the Function Stack or Canvas View">
        <Card title="Learn how to work with Functions" href="/building/logic/core-components/functions">
          Functions define the behavior of your API. Add and arrange functions to process inputs and fetch data.
        </Card>
      </Step>

      <Step title="Define what your API returns with the Response">
        <Card title="Learn how to configure Responses" href="/building/logic/core-components/response">
          Control exactly what data your API sends back.
        </Card>
      </Step>
    </Steps>

    <Frame caption="Here's an example of a basic API in the function stack">    <img src="https://mintcdn.com/xano-997cb9ee/_YwYe_syRaE7iZGt/images/apis-20251013-112603.png?fit=max&auto=format&n=_YwYe_syRaE7iZGt&q=85&s=c329b64e805cb663b602f9ab9d8704db" alt="apis-20251013-112603" width="1359" height="705" data-path="images/apis-20251013-112603.png" /></Frame>
  </Tab>

  <Tab title="XanoScript" icon="code">
    A basic API in XanoScript has three parts — **inputs**, **functions**, and **response** — just like in the visual builder:

    ```javascript lines icon="code" Example of a basic API in XanoScript theme={null}
    query user_list verb=GET {
      description = "Query all user records"

      input {
        text name? filters=trim
      }

      stack {
        db.query user {
          search = $db.user.name ==? $input.name
          return = {type: "list"}
        } as $model
      }

      response {
        value = $model
      }

      history = {inherit: true}
    }
    ```

    <Card title="Learn how to build APIs in XanoScript" icon="code" horizontal href="/xanoscript/api">
      For more information on how to build APIs in XanoScript, see the XanoScript API documentation.
    </Card>
  </Tab>
</Tabs>


Built with [Mintlify](https://mintlify.com).