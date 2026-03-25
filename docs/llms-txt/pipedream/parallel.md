# Source: https://pipedream.com/docs/workflows/building-workflows/control-flow/parallel.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Parallel

## Overview

**Parallel** is multi-path branching operator. It allows you to create multiple execution branches with optional filtering rules and Pipedream will execute **all** matching branches. Unlike [Switch](/workflows/building-workflows/control-flow/switch/) and [If/Else](/workflows/building-workflows/control-flow/ifelse/), the order in which rules are defined will not affect the path of execution.

<Frame>
  <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/138f6007-image.png?fit=max&auto=format&n=NF77kliJSewMqg65&q=85&s=15b7281eb17c7bac59a776f45338ab2c" width="1758" height="1024" data-path="images/138f6007-image.png" />
</Frame>

## Capabilities

* Create non-linear workflows that execute steps in parallel branches
* Define when branches run — always, conditionally or never (to disable a branch)
* Merge and continue execution in the parent flow after the branching operation

<Note>
  The Parallel operator is a control flow **Block** with **start** and **end** phases. [Learn more about Blocks](/workflows/building-workflows/control-flow/#blocks).
</Note>

### Add Parallel operator to workflow

Select **Parallel** from the **Control Flow** section of the step selector:

<Frame>
  <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/c00b4f12-image.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=c6b7463f4a17907c977cad06c4897bc0" width="1758" height="1024" data-path="images/c00b4f12-image.png" />
</Frame>

### Create Branches

To create new branches, click the `+` button:

<Frame>
  <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/c0c411a7-image.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=b0279d5e194de1f1e7c62895b40e23f2" width="1758" height="1024" data-path="images/c0c411a7-image.png" />
</Frame>

### Rename Branches

Edit the branch’s nameslug on the canvas or in the right pane after selecting the **Start** phase of the parallel block. The nameslug communicates the branch’s purpose and affects workflow execution—the end phase exports an object, with each key corresponding to a branch name.

<Frame>
  <img src="https://mintcdn.com/pipedream/nKh6d_6A4aXFb6xD/images/f41b18cc-image.png?fit=max&auto=format&n=nKh6d_6A4aXFb6xD&q=85&s=6cb93ced713e92b1e6cb93846a370cdf" width="1758" height="1024" data-path="images/f41b18cc-image.png" />
</Frame>

### Export Data to the Parent Flow

You can export data from a parallel operation and continue execution in the parent flow.

* The parallel block exports data as a JSON object
* Branch exports are assigned to a key corresponding to the branch name slug (in the object exported from the block)
* Only the exports from the last step of each executed branch are included in the parallel block’s return value
* To preview the exported data, test the **End** phase of the parallel block

### Beta Limitations

Workflow queue settings (concurrency, execution rate) may not work as expected with workflows using the parallel operator.

## Getting Started

<Steps>
  <Step title="Generate a test event">
    Add a trigger and generate an event to help you build and test your workflow:

    <Frame>
      <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/d57964b7-image.gif?s=c65823a030a4f7f6bd83652d875cffc3" width="2054" height="1196" data-path="images/d57964b7-image.gif" />
    </Frame>
  </Step>

  <Step title="Add the Parallel control flow block">
    Click the + button to add a step to the canvas and select Parallel from the Control Flow section on the right. You can optionally add or remove branches and configure conditions defining when each branch should run.

    <Frame>
      <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/6a3de974-image.gif?s=c637b9746ab08453fac47d57916806e7" width="2054" height="1196" data-path="images/6a3de974-image.gif" />
    </Frame>
  </Step>

  <Step title="Test to identify the execution path(s)">
    Test the **Start** phase to identify which branches will execute for the current event.

    <Frame>
      <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/84029e1c-image.gif?s=6150a57caffce56af6f3b305e519c70a" width="2054" height="1196" data-path="images/84029e1c-image.gif" />
    </Frame>
  </Step>

  <Step title="Add steps to branches">
    Add steps to the branches. These steps will be executed in parallel when the workflow runs.

    <Frame>
      <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/382b338a-image.gif?s=671b484163f85321d61c5954ca0a8f79" width="2054" height="1196" data-path="images/382b338a-image.gif" />
    </Frame>
  </Step>

  <Step title="Optionally merge and continue to the parent flow">
    Test the **End** phase to export the results of the last step of each branch that was executed. This makes data from the branches available to reference in the parent flow.

    <Frame>
      <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/64bc6a7e-image.gif?s=35136d765678a18f6896a8c1b0e9c872" width="2054" height="1196" data-path="images/64bc6a7e-image.gif" />
    </Frame>
  </Step>

  <Step title="Use exports in parent flow">
    Optionally add steps after the parallel block and use data from individual branches by referencing the return value of the **End** phase.

    <Frame>
      <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/13b91cd2-image.gif?s=de322586ed3222fd0bf483ec44369602" width="2054" height="1196" data-path="images/13b91cd2-image.gif" />
    </Frame>
  </Step>

  <Step title="Deploy and test the live workflow">
    Deploy the workflow and trigger it to inspect the executions.

    <Frame>
      <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/8d9ba823-image.gif?s=0f333305831b50a60834ce09fd01af49" width="2054" height="1196" data-path="images/8d9ba823-image.gif" />
    </Frame>
  </Step>
</Steps>

Built with [Mintlify](https://mintlify.com).
