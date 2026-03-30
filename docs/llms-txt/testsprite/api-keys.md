# Source: https://docs.testsprite.com/web-portal/admin/api-keys.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.testsprite.com/llms.txt
> Use this file to discover all available pages before exploring further.

# API Keys & MCP Integration

> Manage your TestSprite API keys in the Web Portal and view test results from MCP Server executions.

## Generating API Keys

Generate API keys for MCP Server integration and other third-party tools.

<Steps>
  <Step title="Navigate to Settings">
    Go to <kbd>SETTINGS > API Keys</kbd> and click <kbd>Generate New API Key</kbd>.

    <Frame>
      <img src="https://mintcdn.com/testspriteinc/ex3lblqbetJSa-ak/images/api-key.png?fit=max&auto=format&n=ex3lblqbetJSa-ak&q=85&s=2eff7c464eed4a61fdabd6c0322f91be" alt="API Key" width="1730" height="895" data-path="images/api-key.png" />
    </Frame>
  </Step>

  <Step title="Configure and Save">
    Provide a **descriptive name** (e.g., "MCP Integration") and <kbd>Copy</kbd> the generated API key immediately.

    <Warning>
      Store it securely. It won't be shown again
    </Warning>

    <Frame>
      <img src="https://mintcdn.com/testspriteinc/QYauUtR7JhW8Lgzr/images/created-api-key.png?fit=max&auto=format&n=QYauUtR7JhW8Lgzr&q=85&s=691663a5f9acf1ba76ad65456e77f489" alt="API Key" width="1642" height="754" data-path="images/created-api-key.png" />
    </Frame>
  </Step>
</Steps>

## Managing API Keys

<Frame>
  <img src="https://mintcdn.com/testspriteinc/QYauUtR7JhW8Lgzr/images/api-key-info.png?fit=max&auto=format&n=QYauUtR7JhW8Lgzr&q=85&s=be6b25ce2fc02dfa2e3f077318fb17a7" alt="API Key" width="1642" height="261" data-path="images/api-key-info.png" />
</Frame>

<Tabs>
  <Tab title="Each API Key Shows">
    Each API key displays key information fields that help you identify, track, and manage your keys effectively.

    | Field                   | Description                                        |
    | :---------------------- | :------------------------------------------------- |
    | <kbd>Key Name</kbd>     | Descriptive identifier                             |
    | <kbd>Key Value</kbd>    | Partially hidden (e.g., `sk_test_****...****abcd`) |
    | <kbd>Created Date</kbd> | When generated                                     |
    | <kbd>Last Used</kbd>    | Most recent usage                                  |
  </Tab>

  <Tab title="Available Actions">
    Manage your API keys with these actions to control access, monitor usage, and maintain security.

    | Action                  | Description                    |
    | :---------------------- | :----------------------------- |
    | <kbd>View Details</kbd> | See usage statistics           |
    | <kbd>Revoke</kbd>       | Immediately disable the key    |
    | <kbd>Delete</kbd>       | Remove the API key permanently |
  </Tab>
</Tabs>

## Viewing MCP Test Results

When you run tests through MCP Server in your IDE, view the results in your Web Portal dashboard.

Go to <kbd>TESTING > MCP Tests</kbd> and view all tests executed through MCP Server

<Frame>
  <img src="https://mintcdn.com/testspriteinc/etE5QHi14YOHx37z/images/mcp-result.png?fit=max&auto=format&n=etE5QHi14YOHx37z&q=85&s=7ff56609543bfc53d572a21063508557" alt="API Key" width="1642" height="742" data-path="images/mcp-result.png" />
</Frame>

Test Information Displayed:

| Field              | Description                      |
| :----------------- | :------------------------------- |
| **Test Name**      | Description of the executed test |
| **Execution Time** | When the test was run            |
| **Duration**       | Test execution time              |
| **Status**         | Passed, Failed, or In Progress   |
| **Test Type**      | Frontend, Backend, or Mixed      |

### Test Reports

Click on any test result to view **detailed test execution logs**, **individual test case results**, **error messages and debugging information**, and **performance metrics**.

<Frame>
  <img src="https://mintcdn.com/testspriteinc/teCzVODp75jc8wZz/images/report.png?fit=max&auto=format&n=teCzVODp75jc8wZz&q=85&s=0556a2b9c0381eb80323dcc57a13adb2" alt="Report" width="1730" height="895" data-path="images/report.png" />
</Frame>

<br />

<Card title="View Example Test Report" icon="file" href="../../learn/mcp-demo#test-report-example">
  Click to see a detailed example of TestSprite test reports with execution logs and performance metrics.
</Card>

## Next Steps

<Info>Your API key is used in the MCP Server configuration to authenticate with TestSprite's testing engine.</Info>

<CardGroup cols={2}>
  <Card title="Start Your First Test" href="../../mcp/getting-started/first-test">
    Get hands-on experience with TestSprite MCP
  </Card>

  <Card title="MCP Server Documentation" href="../../mcp/getting-started/overview">
    Complete TestSprite MCP Server guide
  </Card>

  <Card title="Installation Guide" href="../../mcp/getting-started/installation">
    Step-by-step setup instructions
  </Card>

  <Card title="Workflow Examples" href="../../mcp/concepts/test-type-lifecycle">
    Learn TestSprite MCP Server workflows
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).