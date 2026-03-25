# Source: https://pipedream.com/docs/workflows/building-workflows/control-flow.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

Pipedream is adding powerful control flow operators so you can build and run non-linear workflows to unlock use cases that require advanced orchestration.

<Frame>
  <iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/HtXoXWbXO3g" title="If/Else Demo" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</Frame>

## Operators

| Operator                                                                 | Description                                                                              |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| [If/Else (beta)](/workflows/building-workflows/control-flow/ifelse/)     | Supports single-path, logical branching orchestration.                                   |
| [Delay](/workflows/building-workflows/control-flow/delay/)               | Add a delay from 1 millisecond to 1 year before the next step of your workflow proceeds. |
| [Filter](/workflows/building-workflows/control-flow/filter/)             | Define rules to stop or continue workflow execution.                                     |
| [End Workflow](/workflows/building-workflows/control-flow/end-workflow/) | Terminate the workflow prior to the last step.                                           |

More operators (including parallel and looping) are coming soon.

## Key Capabilities

* Orchestrate execution of linear and non-linear workflows
* Normalize results and continue after a non-linear operation
* Nest control flow operators for advanced use cases
* Return HTTP responses during or after most non-linear operations
* Execute long running workflows (workflow timeout resets at each control flow boundary)

## Execution Path

### Context

The execution path represents the specific steps (and the order of steps) that run when a workflow is triggered.

* Simple linear workflows are executed from top to bottom — every step is in the execution path.

  <Frame>
    <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/3f08589d-image.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=9f16b6180c41105ecfeaeac416ee0cc4" width="2000" height="1042" data-path="images/3f08589d-image.png" />
  </Frame>

* With the introduction of non-linear workflows, steps may or may not be executed depending on the rules configured for control flow operators and the results exported from prior steps.

  <Frame>
    <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/07791db0-image.png?fit=max&auto=format&n=NF77kliJSewMqg65&q=85&s=0cc4d46d5b699b96466c7f1001ea4205" width="2000" height="1197" data-path="images/07791db0-image.png" />
  </Frame>

  Therefore, we introduced new patterns to signal the execution path and help you build, test and inspect workflows.

### Executed Path

Step borders, backgrounds and connectors now highlight the **executed path** — the steps that are executed on the execution path. If a non-execution path step is tested, it will not be reflected as being on the execution path.

<Frame>
  <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/6c5c8a70-image.png?fit=max&auto=format&n=anb6FA0wpd8jtdUB&q=85&s=a17016b505595d2e7c486d2df3e1e1ac" width="2000" height="1154" data-path="images/6c5c8a70-image.png" />
</Frame>

### Building and Testing in an Unknown or Non-Execution Path

You may add and test steps in any path. However, Pipedream highlights that the results may not be reliable if the step is outside the executed path; the results may not match the outcome if the steps were in a known execution path and may lead to invalid or misleading results.

<Frame>
  <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/41c5a455-image.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=15f046dcf0e091d0d3d7cc302593644c" width="2000" height="1285" data-path="images/41c5a455-image.png" />
</Frame>

### Signaling Steps are “Out of Date”

If prior steps in a workflow are modified or retested, Pipedream marks later steps in the execution path as *stale* to signal that the results may be out of date. In the non-linear model, Pipedream only marks steps that are in the confirmed execution path as stale.

* If a change is made to a prior step, then the executed path is cleared.

  <Frame>
    <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/2046f94c-image.gif?s=d3509f58d865a821cfb0446e13d944e9" width="4098" height="2388" data-path="images/2046f94c-image.gif" />
  </Frame>

* Steps in the known execution path are immediately marked as stale

* State within conditional blocks is not updated until the start phase is tested and execution path is identified.

  <Frame>
    <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/d5a6e35c-image.gif?s=c3d2ddc2871ca26170846c47c34f6e0e" width="4110" height="2390" data-path="images/d5a6e35c-image.gif" />
  </Frame>

### Test State vs Execution Path

Steps may be tested whether or not they are in the execution path. The test state for a step reflects whether a step was successfully tested or needs attention (the step may have errored, the results may be out of date, etc) and is denoted by the icon at the top left of each step.

* Last test was successful

  <Frame>
    <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/d052e2df-image.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=497bc16ad4786fbe04c389d9af30833d" width="2000" height="489" data-path="images/d052e2df-image.png" />
  </Frame>

* Results may be stale, step may be untested, etc

  <Frame>
    <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/b093e7e0-image.png?fit=max&auto=format&n=Acz4Z1ch6TM7-aI8&q=85&s=9aba60d442a5f9f50fe31ae8458d3217" width="2000" height="550" data-path="images/b093e7e0-image.png" />
  </Frame>

* **Step has an error or is not configured**

  <Frame>
    <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/de5c22ac-image.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=92618ace0999ca5c596a85b0c343a724" width="2000" height="496" data-path="images/de5c22ac-image.png" />
  </Frame>

## Workflow Segments

### Context

Workflow segments are a linear series of steps that with no control flow operators.

* A simple linear workflow is composed of a single workflow segment.

  <Frame>
    <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/d052e2df-image.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=497bc16ad4786fbe04c389d9af30833d" width="2000" height="489" data-path="images/d052e2df-image.png" />
  </Frame>

* When a control flow operator is introduced, then the workflow contains multiple segments. For example, when a Delay operator is added to the simple linear workflow above the workflow goes from 1 to 2 segments.

  <Frame>
    <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/58480aaf-image.png?fit=max&auto=format&n=anb6FA0wpd8jtdUB&q=85&s=e55c7e96be162bb6b132f48c4db554f4" width="2000" height="1103" data-path="images/58480aaf-image.png" />
  </Frame>

* The following example using If/Else contains 5 workflow segments. However, since only 1 branch within the If/Else control flow block is run on each workflow execution, the maximum number of segments that will be executed for each trigger event is 3.

  <Frame>
    <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/9097daa2-image.png?fit=max&auto=format&n=grEzwYhEB2vZSwGw&q=85&s=0c2aff6e16e0f810a7695945f1899d39" width="2000" height="1108" data-path="images/9097daa2-image.png" />
  </Frame>

### Billing

Pipedream compiles each workflow segment into an executable function to optimize performance and reduce credit usage; credit usage is calculated independently for each workflow segment independent of the number of steps (rather than per step like many other platforms).

* For example, the two workflow segments below both use a single credit:

  * **Trigger + 1 step workflow segment (1 credit)**

    <Frame>
      <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/1e5d642d-image.png?fit=max&auto=format&n=NF77kliJSewMqg65&q=85&s=e150bcf1759fc0ba22720ab96425dad7" width="2000" height="1246" data-path="images/1e5d642d-image.png" />
    </Frame>

  * **Trigger + 5 step workflow segment (1 credit)**

    <Frame>
      <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/ba0eb7d2-image.png?fit=max&auto=format&n=Acz4Z1ch6TM7-aI8&q=85&s=ccb5f81a6e74af14f4bcea8ca636f55f" width="2000" height="1110" data-path="images/ba0eb7d2-image.png" />
    </Frame>

* The If/Else example above that contains 5 workflow segments, but only 3 workflow segments in any given execution path will only incur 3 credits of usage per execution.

  <Frame>
    <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/b9ca2dd4-image.png?fit=max&auto=format&n=Acz4Z1ch6TM7-aI8&q=85&s=0011dc876193a5933a26edf22e40ae59" width="2000" height="1108" data-path="images/b9ca2dd4-image.png" />
  </Frame>

### Timeout and Memory

For the preview, all workflow segments inherit the global timeout and memory settings. In the future, Pipedream will support customization of timeout and memory settings for each segment. For example, if you need expanded memory for select steps, you will be able to restrict higher memory execution to that segment instead of having to run the entire workflow with the higher memory settings. This can help you reduce credit usage.

### Long Running Workflows

Users may create long running workflows that greatly exceed the upper bound timeout of 12 minutes for current workflow (each workflow segment has an upper bound of 12 minutes).

### `/tmp` directory access

`tmp` directory access is scoped per workflow segment (since each segment is executed as an independent function). If you need to persist files across multiple segments (or workflow executions) use File Stores.

### Warm Workers

Warm workers are globally configured per segment. For example, if you have a workflow with 3 segments and you configure your workflow to use 1 warm worker per segment, 3 warm workers will be used.

### Segment Relationships

Steps may only reference prior steps in the same workflow segment or it’s direct ancestors.

| Type   | Description                                                                                                                                                                                                                   |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Root   | The root segment is the top level for a workflow — it may have children but no parents. If you do not include any control flow blocks in your workflow, your entire workflow definition is contained within the root segment. |
| Parent | A segment that has a child.                                                                                                                                                                                                   |
| Child  | A flow that has a parent.                                                                                                                                                                                                     |

## Blocks

### Context

**Blocks** are compound steps that are composed of a **start** and an **end** phase. Blocks may contain one or more workflow segments between the phases.

* Most non-linear control flow operators will be structured as blocks (vs. standard steps)

* You may add steps or blocks to [workflow segments](/workflows/building-workflows/control-flow/#workflow-segments) between start and end phases of a block

* The start and end phases are independently testable

  * The start phase evaluates the rules/configuration for a block; the results may influence the execution path
  * The end phase exports results from the control flow block that can be referenced in future workflow steps
  * For example, for the If/Else control flow operator, the start phase evaluates the branching rules while the end phase exports the results from the executed branch.

### Testing

When building a workflow with a control flow block, we recommend testing the start phase, followed by steps in the execution path followed by the end phase.

<Frame>
  <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/23d25642-image.gif?s=999a2e381b8be4de5d79683b05988310" width="4108" height="2398" data-path="images/23d25642-image.gif" />
</Frame>

For a conditional operator like if/else, we then recommend generating events that trigger alternate conditions and testing those.

<Frame>
  <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/0305731a-image.gif?s=15c582ad343834bee336d38d1781ccec" width="4110" height="2398" data-path="images/0305731a-image.gif" />
</Frame>

#### Passing data to steps in a control flow block

Steps may only reference prior steps in the same workflow segment or it’s direct ancestors. In the following example, `step_c` and `step_d` (within the if/else control flow block) can directly reference any exports from `trigger`, `step_a`, or `step_b` (in the parent/root workflow segment) via the steps object. `step_c` and `step_d` are siblings and cannot reference exports from each other.

<Frame>
  <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/3d96c51a-image.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=28ad09d47ffd14b80a39efa3e4de25f7" width="2000" height="2065" data-path="images/3d96c51a-image.png" />
</Frame>

#### Referencing data from steps in a previous block

Steps after the end phase may not directly reference steps within a control flow block (between the start and end phases). E.g., in the following workflow there are two branches:

<Frame>
  <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/340d4c22-image.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=c70fe1872588736c26db82bdda1d05bd" width="2000" height="2392" data-path="images/340d4c22-image.png" />
</Frame>

In this example, `step_f` is executed after a control flow block. It can directly reference prior steps in the root workflow segment (`trigger`, `step_a` and `step_b` using the `steps` object).

However, `step_f` cannot reference directly reference data exported by `step_c` or `step_d`. The reason is that due to the non-linear execution, `step_c` and `step_d` are not guaranteed to execute for every event. **To reference data from a control flow block, reference the exports of the end phase.** Refer to the documentation to understand how data is exported for each control flow operator (e.g., for if/else, the exports of the last step in the branch are returned as the exports for the end phase; you can easily normalize the results across branches using a code step).

In this example, `step_f` can reference the exported data for an executed branch by referencing `steps.ifelse.$return_value`.

### Nesting

Control flow blocks may be nested within other control flow blocks:

* If/Else blocks may be nested within other If/Else blocks
* In the future, Loops may be nested within If/Else blocks and vice versa.

There is currently no limit on the number of nested elements.

<Frame>
  <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/2a2b9582-image.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=f9b2870ddf51bb775a90b708904326fc" width="2000" height="1464" data-path="images/2a2b9582-image.png" />
</Frame>

## Rule Builder

### Context

Pipedream is introducing a rule builder for comparative operations. The rule builder is currently only supported by the If/Else operator, but it will be extended to other operators including Switch and Filter.

<Frame>
  <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/76436b3d-image.png?fit=max&auto=format&n=grEzwYhEB2vZSwGw&q=85&s=13303dc321d84ca2263736d23109a148" width="2000" height="1232" data-path="images/76436b3d-image.png" />
</Frame>

### Simple conditions

Compare values using supported operators.

<Frame>
  <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/dc12c9c1-image.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=562b35e74454f1ca0a73bdfa8b68c7d6" width="2000" height="591" data-path="images/dc12c9c1-image.png" />
</Frame>

### Combine multiple conditions using AND / OR

Click “Add condition” using the menu on the right to add multiple conditions. Click on AND / OR to toggle the operator.

<Frame>
  <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/74b858f6-image.png?fit=max&auto=format&n=grEzwYhEB2vZSwGw&q=85&s=1339de7288f27da334521d4c7cc01b2c" width="2000" height="1086" data-path="images/74b858f6-image.png" />
</Frame>

### Test for multiple conditions using Groups

Create and manage groups using the menu options to “Add group”, “Make condition into group”, “Nest group” and “Remove group”.

<Frame>
  <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/8557546e-image.png?fit=max&auto=format&n=grEzwYhEB2vZSwGw&q=85&s=a6ef6293260e07667d0a5a13bf8796f2" width="2000" height="1607" data-path="images/8557546e-image.png" />
</Frame>

### Supported Operators

* Exists

* Doesn’t exist

* String

  * Equals
  * Doesn’t equal
  * Is blank
  * Is not blank
  * Starts with
  * Contains
  * Ends with

* Number

  * Equals
  * Does not equal
  * Is greater than
  * Is greater than or equal to
  * Is less than
  * Is less than or equal to

* Boolean (equals)

* Type checks

  * Is null
  * Is not null
  * Is string
  * Is not a string
  * Is a number
  * Is not a number
  * Is a boolean
  * Is not a boolean

* Value checks

  * Is true
  * Is false

Built with [Mintlify](https://mintlify.com).
