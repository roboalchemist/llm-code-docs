# Source: https://pipedream.com/docs/workflows/building-workflows/control-flow/ifelse.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# If/Else

## Overview

**If/Else** is single path branching operator. You can create multiple execution branches, but Pipedream will execute the **first** branch that matches the configured rules. **The order in which rules are defined will affect the path of execution.**

If/Else operator is useful when you need to branch based on the value of **multiple input variables**. You must define both the input variable and condition to evaluate for every rule. If you only need to test for the value of a **single input variable** (e.g., if you are branching based on the path of an inbound request), the [Switch operator](/workflows/building-workflows/control-flow/switch/) may be a better choice.

<Frame>
  <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/63f35f8b-image.png?fit=max&auto=format&n=anb6FA0wpd8jtdUB&q=85&s=72847b2ee4e327d21922239428230330" width="1871" height="901" data-path="images/63f35f8b-image.png" />
</Frame>

## Capabilities

* Define rules to conditionally execute one of many branches
* Evaluate one or more expressions for each condition (use boolean operators to combine multiple rules)
* Use the **Else** condition as a fallback
* Merge and continue execution in the parent flow after the branching operation

<Note>
  If you disable the **Else** branch and there are no matching cases, the workflow will continue execution in the parent workflow after the **end** phase of the If/Else block
</Note>

<Note>
  The If/Else operator is a control flow **Block** with **start** and **end** phases. [Learn more about Blocks](/workflows/building-workflows/control-flow/#blocks).
</Note>

## Demo

<Frame>
  <iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/HtXoXWbXO3g" title="If/Else Demo" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</Frame>

## Getting Started

<Steps>
  <Step title="Generate a test event">
    Add a trigger and generate an event to help you build and test your workflow:

    <Frame>
      <img src="https://mintcdn.com/pipedream/nKh6d_6A4aXFb6xD/images/e7b7f0b7-image.gif?s=2cf0cda8214cfc4f4516f67175b179ec" width="3600" height="2096" data-path="images/e7b7f0b7-image.gif" />
    </Frame>
  </Step>

  <Step title="Add the If/Else control flow block">
    Click the + button to add a step to the canvas and select If/Else from the Control Flow section on the right. In the “start” phase, configure rules for each branch (optionally toggle the else branch) and then test the step.

    <Frame>
      <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/129d3ce6-image.gif?s=c2ccb4bd0185698934a9d5162647eee6" width="3600" height="2096" data-path="images/129d3ce6-image.gif" />
    </Frame>

    <Note>
      **IMPORTANT:** If you disable the **Else** condition and an event does not match any of the rules, the workflow will continue to the next step after the **If/Else** section. If you want to end workflow execution if no other conditions evaluate to `true`, enable the Else condition and add a **Terminate Workflow** action.
    </Note>
  </Step>

  <Step title="Build and test along the execution path">
    Add a step to the success branch and test it

    <Frame>
      <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/650cd513-image.gif?s=115adb98a09dc6056ebdcefc27cd2032" width="3600" height="2096" data-path="images/650cd513-image.gif" />
    </Frame>
  </Step>

  <Step title="Merge and continue the parent flow after the branching operation">
    Test the end phase to export results from the If/Else control flow block.

    <Frame>
      <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/dc66b832-image.gif?s=d0eef56a110cb2f0f5d445bb339bdcc0" width="3600" height="2096" data-path="images/dc66b832-image.gif" />
    </Frame>

    Add a step and reference the exports from `ifelse` using the steps object.

    <Frame>
      <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/bc77e2b1-image.gif?s=6abd7d566290d6680e14638d62762abb" width="3600" height="2096" data-path="images/bc77e2b1-image.gif" />
    </Frame>
  </Step>

  <Step title="Build and test alternate paths">
    Generate or select an alternate event to generate data to help you test other branches as you build. When you select a new event, the steps in the root workflow segments go stale. Steps in control flow blocks will only go stale if they are in the known path of execution; i.e., if you test a start phase, the steps in the success path will become stale.

    <Frame>
      <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/daa47168-image.gif?s=894ee219a0ebe24ea5f1563c2d6282fb" width="3600" height="2096" data-path="images/daa47168-image.gif" />
    </Frame>

    Build, test and deploy the workflow.

    <Frame>
      <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/4ddd0d4a-image.gif?s=a383805287da95e75babbab736690a7b" width="3600" height="2096" data-path="images/4ddd0d4a-image.gif" />
    </Frame>
  </Step>

  <Step title="Test the deployed workflow">
    Generate test events to trigger the deployed workflow and inspect the executions.

    <Frame>
      <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/5eb73756-image.gif?s=639e2c776f1e3b855ac744a4c5d1bf6e" width="3600" height="2096" data-path="images/5eb73756-image.gif" />
    </Frame>
  </Step>
</Steps>

Built with [Mintlify](https://mintlify.com).
