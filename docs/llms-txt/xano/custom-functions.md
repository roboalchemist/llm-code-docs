# Source: https://docs.xano.com/xanoscript/function-reference/custom-functions.md

# Source: https://docs.xano.com/xanoscript/custom-functions.md

# Source: https://docs.xano.com/the-function-stack/functions/custom-functions.md

# Source: https://docs.xano.com/building/logic/custom-functions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Building Custom Functions in Xano

> Learn how to build Custom Functions (reusable logic)

<Tip>
  Before continuing, make sure you're familiar with:

  * [Core Components](/building/logic/core-components)
  * [Working with Data](/building/logic/working-with-data)
</Tip>

## Building Custom Functions in Xano

Custom Functions are a way to build reusable logic that you can utilize in other workflows. They allow you to build a set of steps once, use them in multiple places, and maintain them in one place.

Custom Functions in Xano are built in three parts:

* Inputs
  \-- Inputs are the data that the Custom Function will accept. For example, `name` and `email`.

* Logic
  \-- The logic is the logic that will be executed when the Custom Function is called. For example, retrieving a record from your database or calculating a user's age.

* Response
  \-- The response is the data that the Custom Function will return. For our `user_list` Custom Function, it might return a list of users, or a single user.

## Custom Function Folders

You can organize your Custom Functions into folders for better organization by adding a folder name to the Custom Function name -- for example, `utilities/user_list` instead of just `user_list`.

You can select <span class="ui-bubble"><Icon icon="folder-tree" /> Move functions</span> to move your Custom Functions into a folder, and <span class="ui-bubble"><Icon icon="folder-plus" /> Add Folder</span> to add a new folder.

## Creating a new Custom Function

From the left-hand menu, click **Library** and then **Custom Functions**.

Clicking the **+ Add Function** button will open a panel that allows you to create a new Custom Function.

You'll be asked to provide some basic information about your Custom Function before continuing.

<Frame><img src="https://mintcdn.com/xano-997cb9ee/cecR9MdyjjLVeP7i/images/custom-functions-20251013-183827.png?fit=max&auto=format&n=cecR9MdyjjLVeP7i&q=85&s=2d8fe7a9195ff6e8fb3184c06e146ac4" alt="custom-functions-20251013-183827" width="484" height="638" data-path="images/custom-functions-20251013-183827.png" /></Frame>

| Parameter       | Description                                                                                                 |
| --------------- | ----------------------------------------------------------------------------------------------------------- |
| Name            | The name of the Custom Function.                                                                            |
| Description     | A description of the Custom Function.                                                                       |
| Folder Path     | The folder path for the Custom Function; this is optional and you don't need to use a folder if you prefer. |
| Tags            | Tags for organization.                                                                                      |
| Request History | The request history settings for the Custom Function.                                                       |

You can build Custom Functions in Xano in three different ways. Choose the one that best fits your needs. You can switch between them at any time.

<Tabs>
  <Tab title="Canvas View" icon="hammer-brush">
    ## The Canvas View

    <Tip>
      The canvas view is a visual representation of your custom function in a node-based format. If you're new to the canvas view, review the [Canvas View](/building/build-visually/canvas-view) basics first.
    </Tip>

    <Steps>
      <Step title="Add Inputs to define what your custom function accepts">
        <Frame>        <img src="https://mintcdn.com/xano-997cb9ee/_YwYe_syRaE7iZGt/images/apis-20251013-103714.png?fit=max&auto=format&n=_YwYe_syRaE7iZGt&q=85&s=9be1c801b5c70e2272265b342f158b59" alt="apis-20251013-103714" width="1147" height="684" data-path="images/apis-20251013-103714.png" /></Frame>

        <Card title="Learn how to work with Inputs" href="/building/logic/core-components/inputs">
          Inputs define the data your custom function expects. Learn how to add and configure them.
        </Card>
      </Step>

      <Step title="Build your logic in the Function Logic or Canvas View">
        <Card title="Learn how to work with Functions" href="/building/logic/core-components/functions">
          Functions define the behavior of your custom function. Add and arrange functions to process inputs and fetch data.
        </Card>
      </Step>

      <Step title="Define what your custom function returns with the Response">
        <Card title="Learn how to configure Responses" href="/building/logic/core-components/response">
          Control exactly what data your custom function sends back.
        </Card>
      </Step>
    </Steps>

    <Frame caption="Here's an example of a basic custom function in the canvas view">    <img src="https://mintcdn.com/xano-997cb9ee/cecR9MdyjjLVeP7i/images/custom-functions-20251013-183546.png?fit=max&auto=format&n=cecR9MdyjjLVeP7i&q=85&s=0c6662f21607209a4b13294926e10373" alt="custom-functions-20251013-183546" width="1339" height="538" data-path="images/custom-functions-20251013-183546.png" /></Frame>
  </Tab>

  <Tab title="Function Stack" icon="code">
    <Steps>
      <Step title="Add Inputs to define what your custom function accepts">
        <Frame>        <img src="https://mintcdn.com/xano-997cb9ee/NgWyYUIOE6OPGYha/images/inputs-20251013-105146.png?fit=max&auto=format&n=NgWyYUIOE6OPGYha&q=85&s=4a81cfc50ad2023829f3b5b6252e00a2" alt="apis-20251013-103714" width="995" height="558" data-path="images/inputs-20251013-105146.png" /></Frame>

        <Card title="Learn how to work with Inputs" href="/building/logic/core-components/inputs">
          Inputs define the data your custom function expects. Learn how to add and configure them.
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

    <Frame caption="Here's an example of a basic custom function in the function stack">    <img src="https://mintcdn.com/xano-997cb9ee/cecR9MdyjjLVeP7i/images/custom-functions-20251013-183622.png?fit=max&auto=format&n=cecR9MdyjjLVeP7i&q=85&s=dc13e14da9ac33f00cc9afdcd09f96e7" alt="custom-functions-20251013-183622" width="1333" height="1097" data-path="images/custom-functions-20251013-183622.png" /></Frame>
  </Tab>

  <Tab title="XanoScript" icon="code">
    A basic custom function in XanoScript has three parts — **inputs**, **functions**, and **response** — just like in the visual builder:

    ```javascript lines icon="code" Example of a basic custom function in XanoScript theme={null}
    function utilities/format_timestamp {
      description = "Makes a timestamp human readable"

      input {
        timestamp? timestamp?
      }

      stack {
        var $readable_timestamp {
          value = $input.timestamp|format_timestamp:"r":"UTC"
        }
      }

      response {
        value = $readable_timestamp
      }

      middleware = {pre: [], post: []}
    }
    ```

    <Card title="Learn how to build custom functions in XanoScript" icon="code" horizontal href="/xanoscript/custom-functions">
      For more information on how to build custom functions in XanoScript, see the XanoScript custom functions documentation.
    </Card>
  </Tab>
</Tabs>


Built with [Mintlify](https://mintlify.com).