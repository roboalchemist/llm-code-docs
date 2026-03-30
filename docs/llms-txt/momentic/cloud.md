# Source: https://momentic.ai/docs/quickstart/cloud.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Cloud

> This quickstart guide will walk you through building and running your first test on Momentic Cloud

## Log in

1. [Log in](https://app.momentic.ai) to your account
2. Select **Repository** on the left sidebar

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/repository.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=0e1b43088833b5c0e91a01d2b07f11d9" width="3636" height="2452" data-path="images/repository.png" />
</Frame>

## Create a test

Click on the **Create test** button in the top-right corner.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/cloud-create-test.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=0d5676a1cb8cebca76457547071a7825" width="3622" height="2438" data-path="images/cloud-create-test.png" />
</Frame>

Enter these details:

* **Name**: `example-test`
* **Base URL**: `https://practicetestautomation.com/practice-test-login/` (a
  demo site for testing)

This will open the Momentic Editor, where you can add instructions in natural
language. Click **Run from start** to execute the test live.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/example-test-editor.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=a586e8d81276469c7d97121e17b3571f" width="3614" height="2430" data-path="images/example-test-editor.png" />
</Frame>

Changes are saved automatically, so you don't need to worry about losing your
work.

## Run the test

You can run any tests you create by clicking on the **Run** button in the panel.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/run-button-panel.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=6fa4d91c2b9d878f181b7c348de25817" width="3636" height="2452" data-path="images/run-button-panel.png" />
</Frame>

You can also schedule tests to run automatically at specific times or intervals
using a [cron expression](https://crontab.guru/). To do this, click on the
**Schedule test** button in the panel and input the desired schedule.

## Next steps

Congratulations! You have successfully built and ran your first test with
Momentic. Here are suggested next steps:

<Card title="CLI" icon="terminal" horizontal href="/quickstart/cli">
  Install the Momentic CLI to build and run tests locally
</Card>

<Card title="Variables" icon="square-root-variable" horizontal href="/variables">
  Learn how to use variables to make your tests more dynamic and reusable
</Card>


Built with [Mintlify](https://mintlify.com).