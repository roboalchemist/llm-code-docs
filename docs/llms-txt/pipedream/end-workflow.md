# Source: https://pipedream.com/docs/workflows/building-workflows/control-flow/end-workflow.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# End Workflow

To terminate the workflow prior to the last step, use the **End Workflow** pre-built action or `$.flow.exit()` in code.

<Frame>
  <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/3f0ef77c-image.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=173ecee80f60abef92ede3fc6a295dbd" width="2000" height="1208" data-path="images/3f0ef77c-image.png" />
</Frame>

## End Workflow Using a Pre-Built Action

* Select and configure the End Workflow action from the step selector

* When the step runs, the workflow execution will stop

* You may configure an optional reason for ending the workflow execution. This reason will be surfaced when inspecting the event execution.

  <Frame>
    <img src="https://mintcdn.com/pipedream/nKh6d_6A4aXFb6xD/images/e88769bc-image.png?fit=max&auto=format&n=nKh6d_6A4aXFb6xD&q=85&s=f0cbbb9e80d84b5780bd857d3c34be41" width="2000" height="325" data-path="images/e88769bc-image.png" />
  </Frame>

## End Workflow in Code

Check the reference for your preferred language to learn how to end the workflow execution in code.

* [Ending a workflow in Node.js](/workflows/building-workflows/code/nodejs/#ending-a-workflow-early)
* [Ending a workflow in Python](/workflows/building-workflows/code/python/#ending-a-workflow-early)

Built with [Mintlify](https://mintlify.com).
