# Source: https://docs.xano.com/the-function-stack/functions.md

# Source: https://docs.xano.com/building/logic/core-components/functions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Functions

> The functions that make up your logic

Functions are the building blocks of logic. They can be used to perform actions, such as retrieving a record from the database, or generating a random number.

## Adding a Function

<Tabs>
  <Tab title="Canvas View" icon="hammer-brush">
    Hover over a node and click the plus icon to insert a new function after it. You can also hover over the connecting lines to insert a function at that point in the flow.

    <Frame caption="Adding new functions">
            <img src="https://mintcdn.com/xano-997cb9ee/4xy0p5vdU3hAE_8U/images/visual-canvas-20251010-142619.png?fit=max&auto=format&n=4xy0p5vdU3hAE_8U&q=85&s=b10128d1ee5892681f4293652261ace3" alt="visual-canvas-20251010-142619" width="915" height="312" data-path="images/visual-canvas-20251010-142619.png" />
    </Frame>

    In the panel that opens on the right, you can select the function you want to add. Use the search at the top, or navigate through the function categories.

    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/bCVIC1Tg3ccBy86J/images/function-stack-20251008-154357.png?fit=max&auto=format&n=bCVIC1Tg3ccBy86J&q=85&s=323337139c844dbc757640e2fcae1762" alt="function-stack-20251008-154357" width="1164" height="1048" data-path="images/function-stack-20251008-154357.png" />
    </Frame>

    <br />

    Each function will have a different set of options available to you, so it's best to consult that function's specific documentation for more information.
  </Tab>

  <Tab title="Function Stack" icon="code">
    Add a function by clicking the **+ Add Function** button below the function stack, hover over a function and click the **+** sign, or use your up and down arrow keys to select a row, and press A on your keyboard to add a new function.

    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/bCVIC1Tg3ccBy86J/images/function-stack-20251008-154316.png?fit=max&auto=format&n=bCVIC1Tg3ccBy86J&q=85&s=171f653b607bbe5b9ff0d9ae121432f5" alt="function-stack-20251008-154316" width="962" height="525" data-path="images/function-stack-20251008-154316.png" />
    </Frame>

    In the panel that opens on the right, you can select the function you want to add. Use the search at the top, or navigate through the function categories.

    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/bCVIC1Tg3ccBy86J/images/function-stack-20251008-154357.png?fit=max&auto=format&n=bCVIC1Tg3ccBy86J&q=85&s=323337139c844dbc757640e2fcae1762" alt="function-stack-20251008-154357" width="1164" height="1048" data-path="images/function-stack-20251008-154357.png" />
    </Frame>

    <br />

    Each function will have a different set of options available to you, so it's best to consult that function's specific documentation for more information.

    After you add a function, Xano will sometimes suggest the most likely next step; for example, adding a Query All Records will suggest a loop after. You can choose to add the suggestion, ignore it, or just continue working and Xano will dismiss the suggestion automatically.

    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/bCVIC1Tg3ccBy86J/images/function-stack-20251008-154710.png?fit=max&auto=format&n=bCVIC1Tg3ccBy86J&q=85&s=36a35184964106ead1cfe174655499e2" alt="function-stack-20251008-154710" width="973" height="239" data-path="images/function-stack-20251008-154710.png" />
    </Frame>
  </Tab>

  <Tab title="XanoScript" icon="code">
    Functions are defined in the `stack` block, placed immediately after the declaration and accompanying parameters, such as the description.

    ```javascript lines icon="code" Example of the stack block and positioning theme={null}
    stack {
        db.query user {
            search = $db.user.name ==? $input.name
            return = {type: "list"}
        } as $model
    }
    ```

    Functions begin with a **namespace** — basically, a category that the function is a part of. Each namespace is followed by a period, with the function name immediately after. After that, you'll declare any parameters the function requires. Functions can also have a description, which is optional.

    ```javascript lines icon="code" Stack with function declaration theme={null}
    stack {
        function_namespace.function_name {
            description = "<description>"
            <parameter_name> = <parameter_value>
        }
    }
    ```
  </Tab>
</Tabs>

## Function Reference

Review all available functions below by selecting the section you're interested in.

<Columns col={2}>
  <Card title="Database Requests" icon="table" href="/the-function-stack/functions/database-requests">
    Database Requests are used perform operations against your database tables,
    such as retrieving, creating, updating, and deleting records.
  </Card>

  <Card title="Data Manipulation" icon="swap-arrows" href="/the-function-stack/functions/data-manipulation">
    Data Manipulation is used to parse and manipulate data, such as looping,
    filtering, sorting, and transforming data.
  </Card>

  <Card title="Security" icon="lock-keyhole" href="/the-function-stack/functions/security">
    Security is used to secure your data, such as encrypting data, and validating
    data.
  </Card>

  <Card title="APIs and Lambdas" icon="plug" href="/the-function-stack/functions/apis-and-lambdas">
    APIs and Lambdas are used to create APIs and lambdas, such as creating APIs
    and lambdas.
  </Card>

  <Card title="AI Tools" icon="robot" href="/the-function-stack/functions/ai-tools">
    Functions for using AI and related tools, such as Agents, the Template Engine,
    and MCP Servers.
  </Card>

  <Card title="Data Caching (Redis)" icon="binary-circle-check" href="/the-function-stack/functions/data-caching-redis">
    Data Caching (Redis) is used to cache data, such as caching data in Redis.
  </Card>

  <Card title="Actions" icon="block-brick" href="/xano-actions/what-are-actions">
    Actions are reusable building blocks by the Xano team and community that you
    can use in your own workspace.
  </Card>

  <Card title="Custom Functions" icon="function" href="/the-function-stack/functions/custom-functions">
    Custom Functions contain all of the custom functions you've created.
  </Card>

  <Card title="Utility Functions" icon="screwdriver-wrench" href="/the-function-stack/functions/utility-functions">
    Utility Functions are used for things like debugging, error handling,
    grouping, and more.
  </Card>

  <Card title="File Storage" icon="floppy-disks" href="/the-function-stack/functions/file-storage">
    File Storage functions are used to store, retrieve, and manage files in your
    Xano files library.
  </Card>

  <Card title="Cloud Services" icon="clouds" href="/the-function-stack/functions/cloud-services">
    Cloud Services are used to connect to cloud services, such as Algolia, AWS
    OpenSearch, S3, and more.
  </Card>
</Columns>


Built with [Mintlify](https://mintlify.com).