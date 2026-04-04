# Source: https://docs.testsprite.com/mcp/core/deploy-to-production.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.testsprite.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy MCP Tests

> Learn how to deploy and run your MCP tests against staging and production environments.

Once you've created and validated tests, you can deploy them to run against your staging or production environments. This guide walks you through pushing your tests to the MCP Tests web portal for continuous monitoring of your deployed applications.

## Prerequisites

Before deploying your tests, ensure you have:

* Successfully created and run tests locally using MCP
* Access to the MCP Tests web portal
* The URL of your deployed application (staging or production)

## Deployment Steps

<Steps>
  <Step title="Access the MCP Tests Web Portal">
    Log in to the MCP Tests web portal and navigate to your project. You'll see a list of all test suites that have been created locally.

    <Frame>
      <img src="https://mintcdn.com/testspriteinc/etE5QHi14YOHx37z/images/mcp-portal.png?fit=max&auto=format&n=etE5QHi14YOHx37z&q=85&s=da7abed45cde660da06c924606b710f0" alt="plan" width="1444" height="600" data-path="images/mcp-portal.png" />
    </Frame>
  </Step>

  <Step title="Initiate Test Deployment">
    Locate the test suite you want to deploy and click the **"Deploy Tests"** button next to it. This opens the test selection interface.

    <Frame>
      <img src="https://mintcdn.com/testspriteinc/etE5QHi14YOHx37z/images/initiate-deploy.png?fit=max&auto=format&n=etE5QHi14YOHx37z&q=85&s=79de37e157e6e750b2b3caca7a9eb0bc" alt="plan" width="1444" height="461" data-path="images/initiate-deploy.png" />
    </Frame>
  </Step>

  <Step title="Select Tests to Deploy">
    Review the available tests and use the checkboxes to select which ones you want to deploy. You can select individual tests or multiple tests at once depending on your deployment strategy.

    <Tip>Consider starting with a subset of critical tests before deploying your entire test suite to production.</Tip>

    <Frame>
      <img src="https://mintcdn.com/testspriteinc/etE5QHi14YOHx37z/images/select-test.png?fit=max&auto=format&n=etE5QHi14YOHx37z&q=85&s=225bef5818b96700a219ebcac19c42ad" alt="plan" width="1444" height="646" data-path="images/select-test.png" />
    </Frame>
  </Step>

  <Step title="Confirm Test Selection">
    After selecting your tests, click the **"Deploy Tests"** button in the upper right corner to proceed with the deployment.

    <Frame>
      <img src="https://mintcdn.com/testspriteinc/etE5QHi14YOHx37z/images/select-deploy.png?fit=max&auto=format&n=etE5QHi14YOHx37z&q=85&s=d65a4b3e62fce1f41e85136944628bfa" alt="plan" width="1444" height="646" data-path="images/select-deploy.png" />
    </Frame>
  </Step>

  <Step title="Configure Target Environment">
    Enter the URL of your deployed application where the tests will run (e.g., `https://your-app.com` or `https://staging.your-app.com`). This URL becomes the target environment for all test executions.

    <Warning>Ensure the URL is accessible and that any required authentication credentials are properly configured.</Warning>

    <Frame>
      <img src="https://mintcdn.com/testspriteinc/QYauUtR7JhW8Lgzr/images/configure-env.png?fit=max&auto=format&n=QYauUtR7JhW8Lgzr&q=85&s=75a56b51c699a36c0b9ceb8aed5c539d" alt="plan" width="467" height="315" data-path="images/configure-env.png" />
    </Frame>
  </Step>

  <Step title="Monitor Test Execution">
    Navigate to the **"All Tests"** page to monitor your test results in real-time.

    <Frame>
      <img src="https://mintcdn.com/testspriteinc/QYauUtR7JhW8Lgzr/images/depoly-all-test.png?fit=max&auto=format&n=QYauUtR7JhW8Lgzr&q=85&s=0445bd6c1da2434ddb4c8f1fe26b69f4" alt="plan" width="2223" height="907" data-path="images/depoly-all-test.png" />
    </Frame>

    Here you can:

    * View detailed test execution logs
    * Analyze test visualizations and screenshots
    * Review any failures or issues
    * Track test performance over time
  </Step>
</Steps>

## Next Steps

After deploying your tests to production, you can **configure alerts to notify your team of test failures**, or follow the steps below:

<Columns cols={2}>
  <Card title="Set up continuous monitoring" href="/mcp/core/continuous-monitoring">
    Run tests automatically on a schedule
  </Card>

  <Card title="Review test maintenance guide" href="/mcp/maintenance/test-maintenance">
    Best practices for keeping your tests up to date
  </Card>
</Columns>


Built with [Mintlify](https://mintlify.com).