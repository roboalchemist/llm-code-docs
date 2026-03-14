# Source: https://plivo.com/docs/aiagent/aistudio/nodereference/function.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Functions

> Function Nodes enable routing, task creation, business hour checks, and API requests

Function Nodes are critical components in the Plivo Agent Builder, enabling you to execute a variety of operations within your conversational flows. These nodes enhance the flexibility of your AI workflows by allowing you to route conversations, check business hours, create tasks, and send API requests to external services. Below are the four key Function Nodes and their configurations:

<Frame>
  <img src="https://mintcdn.com/plivo/R0bB3pSVhMhsNJEx/aiagent/images/Functions-Image1.png?fit=max&auto=format&n=R0bB3pSVhMhsNJEx&q=85&s=d4c507fe6c8764d7cdfe5b0de2ae12b6" width="1200" height="688" data-path="aiagent/images/Functions-Image1.png" />
</Frame>

### 1. **Assign to Human Node**

The **Assign to Human Node** routes the conversation to a human specialist for manual intervention. You can assign the conversation to a specific agent or a team, based on predefined criteria.

**Configuration Steps**:

1. **Select the Queue**: Choose a queue where the conversation will wait until a human agent is available.
2. **Advanced Settings**:
   * **Routing Strategy**: Choose from multiple routing strategies:
     * **Highest Idle Time**: Routes to the agent who has been idle for the longest.
     * **Simultaneous Conversations**: Routes based on how many conversations the agent can handle simultaneously.
     * **Lowest Conversations Handled**: Routes to the agent with the least number of handled conversations.
     * **Lowest Conversation Handle Time**: Routes to the agent with the lowest handling time.
   * **Simultaneous Conversation Recipients**: Specify how many agents can handle the conversation at the same time.
   * **Conversation Assignment Retry**: Set the retry count for unsuccessful assignments.
   * **Sticky Routing**: Enable sticky routing to route the conversation to the same agent.
   * **Sticky Routing Expiry**: Set an expiry time for sticky routing.

**Possible Paths After This Node**:

* **Conversation Completed**
* **Enqueue Failed**
* **Timeout**
* **Assignment Failed**

### 2. **Business Hour Node**

The **Business Hour Node** checks if the current time is within your configured working hours and routes conversations accordingly.

**Configuration Steps**:

1. **Select Business Hours**: Choose from your pre-configured business hours to determine whether the conversation happens during business hours.

**Possible Paths After This Node**:

* **During Business Hours**: If the conversation occurs within business hours.
* **Outside Business Hours**: If the conversation occurs outside business hours.

### 3. **Create Task Node**

The **Create Task Node** creates a follow-up task within Plivo's platform for further action or tracking.

**Configuration Steps**:

1. **Task Type**: Choose the type of task (e.g., follow-up, support, sales).
2. **Channel**: Specify the communication channel for the task.
3. **Description**: Provide a brief description of the task.
4. **Priority**: Set the task’s priority (e.g., high, medium, low).
5. **Due Date**: Specify the due date for completing the task.

**Possible Paths After This Node**:

* **Success**: Task creation was successful.
* **Failure**: Task creation failed due to an error.

### 4. **HTTP Request Node**

The **HTTP Request Node** allows you to send API requests to external services and process the response.

**Configuration Steps**:

1. **API URL and Method**: Define the endpoint URL and HTTP method (GET, POST, etc.).
2. **Authentication**: Choose the authentication type (None, Basic Auth, or Bearer Token).
3. **Timeout and Retries**: Set a timeout period and retry attempts for the request.
4. **Parameters**: Define the key-value pairs for parameters, headers, and body of the request.

**Possible Paths After This Node**:

* **Success**: Proceed if the request is successful.
* **Failure**: Proceed if the request fails.

These **Function Nodes** enable you to create dynamic, responsive workflows that handle manual interventions, business hour checks, task assignments, and external API integrations. By leveraging these nodes, you can enhance the efficiency and complexity of your conversational flows.
