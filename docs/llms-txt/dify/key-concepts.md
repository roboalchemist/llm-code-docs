# Source: https://docs.dify.ai/en/use-dify/getting-started/key-concepts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Key Concepts

> Quick overview of essential Dify concepts 

### Dify App

Dify is made for agentic app building. In **Studio**, you can quickly build agentic workflows via a drag & drop interface and publish them as apps. You can access published apps via API, the web, or as an [MCP server](/en/use-dify/publish/publish-mcp). Dify offers two main app types: workflow and chatflow. You will need to choose an app type when creating a new app.

<Info>
  We recommend choosing Workflow or Chatflow your app type. But in addition to these, Dify also offers 3 more basic app types: Chatbot, Agent, and Text Generator.

  <img src="https://mintcdn.com/dify-6c0370d8/pukb9aJrVFLyeNW1/images/22087830d0a6478d42d0c60e6eb88d19bca27be3c645f2bb0968d51330b7da72.png?fit=max&auto=format&n=pukb9aJrVFLyeNW1&q=85&s=b1fa00713a5beb1fa1ae9601e31d8a29" alt="22087830d0a6478d42d0c60e6eb88d19bca27be3c645f2bb0968d51330b7da72.png" title="22087830d0a6478d42d0c60e6eb88d19bca27be3c645f2bb0968d51330b7da72.png" className="mt-1" style={{ width:"100%" }} width="1488" height="558" data-path="images/22087830d0a6478d42d0c60e6eb88d19bca27be3c645f2bb0968d51330b7da72.png" />

  These app types run on the same workflow engine underneath, but comes with simpler legacy interfaces:

  <img src="https://mintcdn.com/dify-6c0370d8/pukb9aJrVFLyeNW1/images/chatbot-interface.png?fit=max&auto=format&n=pukb9aJrVFLyeNW1&q=85&s=342873c2954ac135b1b5737828b99eab" alt="chatbot-interface.png" title="chatbot-interface.png" className="mt-1" style={{ width:"100%" }} width="1225" height="896" data-path="images/chatbot-interface.png" />
</Info>

### Workflow

Build workflow apps to handle single-turn tasks. The webapp interface and API provides easy access to batch execute many tasks at once.

<Info>
  Underneath it all, workflow forms the basis for all other app types in Dify.
</Info>

You can specify how and when to start your workflow. There are two types of Start nodes:

* **[User Input](/en/use-dify/nodes/user-input)**: Direct user interaction or API call invokes the app.

* **[Trigger](/en/use-dify/nodes/trigger/overview)**: The application runs automatically on a schedule or in response to a specific third-party event.

User Input and Trigger Start nodes are mutually exclusive—they cannot be used on the same canvas. To switch between them, right-click the current start node > **Change Node**. Alternatively, delete the current start node and add a new one.

<Note>
  Only workflows started by User Input can be published as standalone web apps or MCP servers, exposed through backend service APIs, or used as tools in other Dify applications.
</Note>

### Chatflow

Chatflow is a special type of workflow app that gets triggered at every turn of a conversation. Other than workflow features, chatflow comes with the ability to store and update custom conversation-specific variables, enable memory in LLM nodes, and stream formatted text, images, and files at different points throughout the chatflow run.

Unlike workflow, chatflow can't use [Trigger](/en/use-dify/nodes/trigger/overview) to start.

### Dify DSL

All Dify apps can be exported into a YAML file in Dify's own DSL (Domain-Specific Language) and you may create Dify apps from these DSL files directly. This makes it easy to port apps to other Dify instances and share with others.

### Variables

A variable is a labeled container to store information, so you can find and use that information later by referencing its name. You'll come across different types of variables when building a Dify app:

**Inputs**: You can specify any number of input variables at the [User Input](/en/use-dify/nodes/user-input) node for your app's end users to fill in.

<img src="https://mintcdn.com/dify-6c0370d8/pukb9aJrVFLyeNW1/images/CleanShot2025-08-04at14.34.04@2x.png?fit=max&auto=format&n=pukb9aJrVFLyeNW1&q=85&s=490a873415d5a7b72b2eea8edf442dd5" alt="CleanShot 2025-08-04 at 14.34.04@2x.png" title="CleanShot 2025-08-04 at 14.34.04@2x.png" className="mx-auto" style={{ width:"51%" }} width="726" height="616" data-path="images/CleanShot2025-08-04at14.34.04@2x.png" />

Additionally, the User Input node comes with a set of input variables that you can reference later in the flow. Depending on the app type (workflow or chatflow), different variables are provided.

<Tabs>
  <Tab title="Workflow">
    | Variable Name         | <div style={{width: '70px'}}>Data Type</div> | Description                                                                                                                                                      | Notes                                                                                                                                          |
    | :-------------------- | :------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
    | `sys.user_id`         | String                                       | User ID: A unique identifier automatically assigned by the system to each user when they use a workflow application. It is used to distinguish different users.  |                                                                                                                                                |
    | `sys.app_id`          | String                                       | App ID: A unique identifier automatically assigned by the system to each App. This parameter is used to record the basic information of the current application. | This parameter is used to differentiate and locate distinct Workflow applications for users with development capabilities.                     |
    | `sys.workflow_id`     | String                                       | Workflow ID: This parameter records information about all nodes information in the current Workflow application.                                                 | This parameter can be used by users with development capabilities to track and record information about the nodes contained within a Workflow. |
    | `sys.workflow_run_id` | String                                       | Workflow Run ID: Used to record the runtime status and execution logs of a Workflow application.                                                                 | This parameter can be used by users with development capabilities to track the application's historical execution records.                     |
    | `sys.timestamp`       | Number                                       | The start time of each workflow execution.                                                                                                                       |                                                                                                                                                |
  </Tab>

  <Tab title="Chatflow">
    | Variable Name         | <div style={{width: '70px'}}>Data Type</div> | Description                                                                                                                                                                                                                                                                                                                                                           | Notes                                                                                                                                                                              |
    | :-------------------- | :------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `sys.conversation_id` | String                                       | A unique ID for the chatting box interaction session, grouping all related messages into the same conversation, ensuring that the LLM continues the chatting on the same topic and context.                                                                                                                                                                           |                                                                                                                                                                                    |
    | `sys.dialogue_count`  | Number                                       | The number of conversations turns during the user's interaction with a Chatflow application. The count automatically increases by one after each chat round and can be combined with if-else nodes to create rich branching logic.<br /><br />For example, LLM will review the conversation history at the X conversation turn and automatically provide an analysis. |                                                                                                                                                                                    |
    | `sys.user_id`         | String                                       | A unique ID is assigned for each application user to distinguish different conversation users.                                                                                                                                                                                                                                                                        | The Service API does not share conversations created by the WebApp. This means users with the same ID will have separate conversation histories between API and WebApp interfaces. |
    | `sys.app_id`          | String                                       | App ID: A unique identifier automatically assigned by the system to each App. This parameter is used to record the basic information of the current application.                                                                                                                                                                                                      | This parameter is used to differentiate and locate distinct Workflow applications for users with development capabilities.                                                         |
    | `sys.workflow_id`     | String                                       | Workflow ID: This parameter records information about all nodes information in the current Workflow application.                                                                                                                                                                                                                                                      | This parameter can be used by users with development capabilities to track and record information about the nodes contained within a Workflow.                                     |
    | `sys.workflow_run_id` | String                                       | Workflow Run ID: Used to record the runtime status and execution logs of a Workflow application.                                                                                                                                                                                                                                                                      | This parameter can be used by users with development capabilities to track the application's historical execution records.                                                         |
  </Tab>
</Tabs>

User inputs are set at the start of each workflow run and cannot be updated.

**Outputs**: Each node produces one or more outputs that can be referenced in subsequent nodes. For instance, the LLM node has outputs:

<img src="https://mintcdn.com/dify-6c0370d8/pukb9aJrVFLyeNW1/images/CleanShot2025-08-04at14.28.57@2x.png?fit=max&auto=format&n=pukb9aJrVFLyeNW1&q=85&s=84ccd0f3c367e6a866f6fdb6e4d98cd7" alt="CleanShot 2025-08-04 at 14.28.57@2x.png" title="CleanShot 2025-08-04 at 14.28.57@2x.png" className="mx-auto" style={{ width:"45%" }} width="508" height="300" data-path="images/CleanShot2025-08-04at14.28.57@2x.png" />

Like inputs, node outputs cannot be updated either.

**Environment Variables**: Use environment variable to store sensitive information like API keys specific to your app. This allows a clean separation between secrets and the Dify app itself, so you don't have to risk exposing passwords and keys when sharing your app's DSL. Environment variables are also constants and cannot be updated.

**Conversation Variables (Chatflow only)**: These variables are conversation-specific -- meaning they persist over multi-turn chatflow runs in a single conversation so you can store and access dynamic information like to-do list and token cost. You can update the value of a conversation variable via the Variable Assigner node:

<img src="https://mintcdn.com/dify-6c0370d8/pukb9aJrVFLyeNW1/images/2935cb58851e5c5407a08dde49f7d9738bb13aa0e64df24278e2104b316f6af6.png?fit=max&auto=format&n=pukb9aJrVFLyeNW1&q=85&s=0ef4c7277da21cce3e3463a0889fb2b1" alt="2935cb58851e5c5407a08dde49f7d9738bb13aa0e64df24278e2104b316f6af6.png" title="2935cb58851e5c5407a08dde49f7d9738bb13aa0e64df24278e2104b316f6af6.png" className="mx-auto" style={{ width:"70%" }} width="834" height="756" data-path="images/2935cb58851e5c5407a08dde49f7d9738bb13aa0e64df24278e2104b316f6af6.png" />

### Variable Referencing

You can easily pass variables to any node when configuring its input field by selecting from a dropdown:

<img src="https://mintcdn.com/dify-6c0370d8/pukb9aJrVFLyeNW1/images/CleanShot2025-08-04at15.13.33@2x.png?fit=max&auto=format&n=pukb9aJrVFLyeNW1&q=85&s=b0eedd42b5c49a28dbb27b4d70b6294c" alt="CleanShot 2025-08-04 at 15.13.33@2x.png" title="CleanShot 2025-08-04 at 15.13.33@2x.png" className="mx-auto" style={{ width:"70%" }} width="894" height="900" data-path="images/CleanShot2025-08-04at15.13.33@2x.png" />

You can also insert variable values into complex text inputs by typing `/` slash, and selecting the desired variable from the dropdown.

<img src="https://mintcdn.com/dify-6c0370d8/6mOfaeljpmK9sOmc/images/image.png?fit=max&auto=format&n=6mOfaeljpmK9sOmc&q=85&s=9889baf5b02ca41afb8607db4fddc504" alt="image.png" title="image.png" className="mx-auto" style={{ width:"73%" }} width="1048" height="1264" data-path="images/image.png" />


Built with [Mintlify](https://mintlify.com).