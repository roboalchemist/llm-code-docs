# Source: https://pipedream.com/docs/workflows/building-workflows/control-flow/switch.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Switch

## Overview

**Switch** is single path branching operator. You can create multiple execution branches, but Pipedream will execute the **first** branch that matches the configured rules. **The order in which rules are defined will affect the path of execution.**

Switch is useful when you need to make a branching decision based on the value of a **single input variable** (e.g., based on the path of an inbound request). You can define the input variable once and then branch based on the value(s). If you need to branch based on the values of **multiple input variables** use the [If/Else operator](/workflows/building-workflows/control-flow/ifelse/).

<Frame>
  <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/b50a91f3-image.png?fit=max&auto=format&n=Acz4Z1ch6TM7-aI8&q=85&s=c2c24eff02fe8579482ead726153dfd3" width="1871" height="899" data-path="images/b50a91f3-image.png" />
</Frame>

## Capabilities

* Define cases to conditionally execute one of many branches
* Define the expression to evaluate once and configure cases to compare values (use boolean operators to combine multiple rules for each case)
* Use the **Default** case as a fallback
* Merge and continue execution in the parent flow after the branching operation

<Note>
  If you disable the **Default** branch and there are no matching cases, the workflow will continue execution in the parent workflow after the **end** phase of the Switch block
</Note>

<Note>
  The Switch operator is a control flow **Block** with **start** and **end** phases. [Learn more about Blocks](/workflows/building-workflows/control-flow/#blocks).
</Note>

## Getting Started

<Steps>
  <Step title="Generate a test event">
    Add a trigger and generate an event to help you build and test your workflow:

    <Frame>
      <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/833a5739-image.gif?s=2405f323461a6a2cf00968aa549b7cb4" width="2054" height="1196" data-path="images/833a5739-image.gif" />
    </Frame>
  </Step>

  <Step title="Add the Switch control flow block">
    Click the + button to add a step to the canvas and select Switch from the Control Flow section on the right. In the “start” phase, configure rules for a case.

    <Frame>
      <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/a9c2ad3e-image.gif?s=2368c4997e6cef82b5d1753a024971f8" width="2054" height="1196" data-path="images/a9c2ad3e-image.gif" />
    </Frame>

    **IMPORTANT:** If you disable the **Default** condition and an event does not match any of the rules, the workflow will continue to the next step after the **Switch** section. If you want to end workflow execution if no other conditions evaluate to `true`, enable the Default condition and add a **Terminate Workflow** action.
  </Step>

  <Step title="Optionally add additional cases">
    To add additional cases, click the **+** button.

    <Frame>
      <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/60155fa5-image.gif?s=8e2c3b81f1b0c09f940d97d04e9df394" width="2054" height="1196" data-path="images/60155fa5-image.gif" />
    </Frame>
  </Step>

  <Step title="Test and build along the execution path">
    Test the **start** phase and add a step to the branch in the execution path,

    <Frame>
      <img src="https://mintcdn.com/pipedream/nKh6d_6A4aXFb6xD/images/e20cbcf0-image.gif?s=bc77061c38e7527fd3ecd875afde43f3" width="2054" height="1196" data-path="images/e20cbcf0-image.gif" />
    </Frame>
  </Step>

  <Step title="Optionally merge and continue the parent flow">
    Test the **end** phase to export the results of the last step in the execution path. This makes them available to reference in the parent flow.

    <Frame>
      <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/c792ab29-image.gif?s=f74a8c8a265451eb9175f9f03d3f0e24" width="2054" height="1196" data-path="images/c792ab29-image.gif" />
    </Frame>
  </Step>

  <Step title="Scaffold alternate paths">
    You may add steps to alternate paths and test them. Pipedream will signal that the results may not be reliable if the branch is not in the execution path.

    <Frame>
      <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/d53f39d1-image.gif?s=54a97e423aa6adb1dc672e9e9cf8e779" width="2054" height="1196" data-path="images/d53f39d1-image.gif" />
    </Frame>
  </Step>

  <Step title="Validate alternate paths">
    Generate or select alternate events to trigger and validate alternate paths.

    <Frame>
      <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/884374c0-image.gif?s=5ae3745fe0e7e611e9b6da729783899b" width="2054" height="1196" data-path="images/884374c0-image.gif" />
    </Frame>
  </Step>

  <Step title="Deploy and test the live workflow">
    Deploy the workflow and trigger it to inspect the executions.

    <Frame>
      <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/913de555-image.gif?s=74ba48bc6d35d609a46f186c952317de" width="2054" height="1196" data-path="images/913de555-image.gif" />
    </Frame>
  </Step>
</Steps>

Built with [Mintlify](https://mintlify.com).
