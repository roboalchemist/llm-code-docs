# Source: https://docs.dify.ai/en/use-dify/nodes/output.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Output

> Define workflow outputs and termination points

<Info>
  The Output node was previously called End. It's now *optional* in a workflow and used only to explicitly output data to the end user.

  End nodes are only for Workflow applications. Chatflows use the [Answer](/en/use-dify/nodes/answer) node instead to deliver responses during the conversation flow.
</Info>

## Output Configuration

In an Output node, you can define what data from your workflow should be returned to users by adding output variables, such as an LLM's response. At least one output variable must be specified; otherwise, nothing will be returned.

When exposed as a backend service API, workflows without an Output node will not return any values to API callers.


Built with [Mintlify](https://mintlify.com).