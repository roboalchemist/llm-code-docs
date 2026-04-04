# Source: https://plivo.com/docs/aiagent/aistudio/path.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Paths

> Paths define the agent progression through the flow based on specified intent and conditions.

**Paths** define the connections between two nodes and the conditions that determine the transitions from one node to another. Think of a path as a route the agent takes as it navigates through the flow.

<Frame>
  <img src="https://mintcdn.com/plivo/R0bB3pSVhMhsNJEx/aiagent/images/path.gif?s=82b7968a06182f0bcbb7a5c5fe8e2989" width="2386" height="1640" data-path="aiagent/images/path.gif" />
</Frame>

The connection between two nodes is represented by a dotted line. This dotted line visually indicates the path and its direction from one node to another.

**Configuring Path Conditions**

To create a path from a node to continue the workflow, click on the circle at the bottom of the source node and select the next node of your preference. Depending on the node, you will get to choose the path condition based on. For the AI Conversation and Action node, you specify the condition based on which the flow should take that path.

**How Pathways Work**

The agent begins at the first node and then moves to the next node based on the conditions specified in the paths. The agent evaluates the conditions on each path and selects the appropriate one. Once the agent reaches a node, it will execute the instructions in that node (e.g., delivering dialogue or performing actions). The agent then proceeds to the next node, continuing this process until the flow is completed or ended.

**Best Practices for Using Paths**

* **Label Paths Clearly**: Use descriptive labels to help you track what each path does (e.g., ‘User provides order info’ or ‘Timeout reached’).
* **Simplify Conditions**: Make the conditions simple to evaluate, and keep the logic clear. Too many conditions can lead to a complex and confusing flow.
* **Test Paths Thoroughly**: Ensure that each path works as expected by running tests with various conditions and inputs. This helps to confirm that the agent follows the correct path and behaves as intended.

**Avoid Overcomplicating Paths**: Always try to keep the flow straightforward. If you need multiple conditional checks, consider breaking down the flow into more manageable nodes.
