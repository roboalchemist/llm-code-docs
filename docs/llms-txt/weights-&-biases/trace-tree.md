# Source: https://docs.wandb.ai/weave/guides/tracking/trace-tree.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Navigate the Weave Trace view

> Use Weave's Trace view to make sense of complex execution paths in your LLM and agentic apps.

The Weave Trace view is designed to help you make sense of complex execution paths in your LLM and agentic apps. Whether you're debugging an agentic app with dozens of nested calls, or tracking the flow of a single model prediction, the Trace view provides a clear visualization of what happened. It also provides alternate ways to view and understand your application flow.

This guide describes how to move through the trace stack, filter and search for functions called by your code, switch between visual representations, and more.

## Get started

To enter the Trace view:

1. Navigate to [https://wandb.ai](https://wandb.ai) and select your project.
2. In the sidebar menu, select **Traces** to view all traces saved for your project.
3. Select a trace to open the Trace Details view. The Trace Details view displays additional panels with a hierarchical breakdown of the trace execution.

## Traces page overview

The Traces page is composed of three core panels:

* **Left panel**: A sortable, paginated list of all traces for the project.
  * This traces table includes additional data such as tokens, cost, and latency.
* **Center panel**: Interactive trace view for a selected trace. The trace tree shows a hierarchy of all the methods tracked within the trace.
  * The trace tree displays [ops](/weave/guides/tracking/ops#automatically-track-function-calls-using-ops), which are `@weave.op()`-decorated functions, that were called during the trace.
* **Right panel**: Details for a selected op within the selected trace.

<Frame>
    <img src="https://mintcdn.com/wb-21fd5541/M79FAxH2Aq0Q8-x2/weave/guides/tracking/imgs/trace-tree-full.png?fit=max&auto=format&n=M79FAxH2Aq0Q8-x2&q=85&s=054e9d8cb21d9f9e86337cf002483ea7" alt="Traces page showing a selected trace and selected op details " width="2062" height="590" data-path="weave/guides/tracking/imgs/trace-tree-full.png" />
</Frame>

### Filter within a trace

* **Regex filter by name(s)**: Use the text field above the trace tree to filter ops by name or type, such as `tool`, `openai.response.create`.
* **Metrics**: Control whether to display the following data metrics when available: cost, tokens, and latency.

### Navigate a trace

The trace tree shows a hierarchy of all the methods tracked within the trace. To move up/down the tree, use `Cmd` (macOS) or `Alt` (Windows/Linux) + Up Arrow (↑) / Down Arrow (↓).

There are several scrubbers below the trace tree that provide rapid navigation across states within it.  You can use the sliders to strategically navigate through your trace.

Expand the panel to see all available scrubbers:

* **Timeline**: Chronological order of events within the trace.
* **Peers**: Ops sharing the same type. For example, if you were examining details of a function called `predict`, you can use this scrubber to immediately jump to the next execution of `predict` within the trace.
* **Siblings**: Ops with the same parent.  Use this scrubber to iterate over ops nested under the parent function call.
* **Stack**: Traverse up/down the call stack.
* **Path**: (Only available in code composition view) Iterate through all calls with the same code path as the selected call.

<Frame>
    <img src="https://mintcdn.com/wb-21fd5541/M79FAxH2Aq0Q8-x2/weave/guides/tracking/imgs/trace-tree-scrubbers.png?fit=max&auto=format&n=M79FAxH2Aq0Q8-x2&q=85&s=0fb6a2843b18d120ec3ea8087c163126" alt="Trace tree panel showing search filter and scrubbers" width="422" height="541" data-path="weave/guides/tracking/imgs/trace-tree-scrubbers.png" />
</Frame>

### Alternative trace tree views

At the top of the panel, you can switch between multiple visual representations of the trace tree depending on your needs. Switch between views based on your debugging needs. Use **code composition view** to understand call logic, **flame graph view** for to understand performance over time, and **graph view** to understand structure.

#### Traces (default)

The default view of the trace tree shows stack hierarchy, cost per op (if available), execution time, and status indicators.

#### Code composition view

In the code composition view, boxes represent ops and their nested calls. This is helpful for visualizing flow of function calls. In this view, you can select a box to drill into that op and filter the call path.

<Frame>
    <img src="https://mintcdn.com/wb-21fd5541/M79FAxH2Aq0Q8-x2/weave/guides/tracking/imgs/trace-tree-code-view.png?fit=max&auto=format&n=M79FAxH2Aq0Q8-x2&q=85&s=997c9e06ae7a1307edc6dfbb02fb5af1" alt="Trace view showing the code view of a trace" width="538" height="640" data-path="weave/guides/tracking/imgs/trace-tree-code-view.png" />
</Frame>

#### Flame graph

The flame graph view provides a timeline-based visualization of execution depth and duration. This is helpful for when trying to understand performance diagnostics over time. You can select into frames to isolate sub-traces.

<Frame>
    <img src="https://mintcdn.com/wb-21fd5541/M79FAxH2Aq0Q8-x2/weave/guides/tracking/imgs/trace-tree-flame-view.png?fit=max&auto=format&n=M79FAxH2Aq0Q8-x2&q=85&s=aff5f74a187351f58c81935df329d17c" alt="Trace view showing a flame graph of ops within a trace" width="731" height="214" data-path="weave/guides/tracking/imgs/trace-tree-flame-view.png" />
</Frame>

#### Graph view

The graph view shows hierarchical relationships between ops. This is useful for understanding parent/child relationships.

<Frame>
    <img src="https://mintcdn.com/wb-21fd5541/M79FAxH2Aq0Q8-x2/weave/guides/tracking/imgs/trace-tree-graph-view.png?fit=max&auto=format&n=M79FAxH2Aq0Q8-x2&q=85&s=c690665493ec4cccf90e1d3c1bd77183" alt="Trace view showing a functional graph view of ops and relationships within a trace" width="734" height="598" data-path="weave/guides/tracking/imgs/trace-tree-graph-view.png" />
</Frame>

### View details for a trace op

After you have selected an op in the trace tree, details for that op display in the next panel. These details are grouped into the following tabs:

* **Call**: The input and output to the op execution.
* **Code**: The code that was used when the call was made.
* **Feedback**: Any available [feedback](/weave/guides/tracking/feedback) for the op. You can provide feedback directly within Weave or through the API.
* **Scores**: Any available [scores](/weave/guides/evaluation/scorers) for the op. Calls are scored by running Evaluations.
* **Summary**:  General information about the op.
* **Use:** Code snippets that you can use to programmatically retrieve the call and add reactions, notes, or feedback.
