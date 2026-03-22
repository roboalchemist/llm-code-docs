# Source: https://docs.testsprite.com/mcp/maintenance/migration-from-other-platforms.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.testsprite.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Import Existing Tests

> Migrate your existing tests from other testing platforms to TestSprite.

## The Simple Path

Already have tests (e.g., Playwright, Cypress, Jest, Postman collections)? You don’t need to rewrite them.

<Steps>
  <Step title="Add to Test Plan">
    Include your existing tests in the TestSprite test plan alongside generated ones
    <Info>Keep the same IDs/titles where possible for clarity</Info>

    <Frame>
      <img src="https://mintcdn.com/testspriteinc/ex3lblqbetJSa-ak/images/frontend-json.png?fit=max&auto=format&n=ex3lblqbetJSa-ak&q=85&s=9e379b8f7e5ef1a9c6fcc32c1c199627" alt="plan" width="1906" height="1031" data-path="images/frontend-json.png" />
    </Frame>
  </Step>

  <Step title="Regenerate Test Code">
    Regenerate the test code to incorporate the imported tests. TestSprite will reference them during code generation and execution

    ```text Example Prompt theme={null}
    Import these UI tests and add them to the TestSprite frontend testing plan, 
    then regenerate the test code and run it.
    ```
  </Step>

  <Step title="Run">
    Execute like any other plan. Results and reports will include both generated and imported tests
  </Step>
</Steps>

## Best Practices

<AccordionGroup>
  <Accordion title="Keep Tests in Repository">
    Keep imported tests in your repo so the runner can access them
  </Accordion>

  <Accordion title="Map Environment Variables">
    If needed, map environment variables/credentials in the TestSprite portal
  </Accordion>

  <Accordion title="Use Consistent Naming">
    Use consistent naming so maintenance is straightforward
  </Accordion>
</AccordionGroup>

## Related

<Columns cols={2}>
  <Card title="Create Tests for New Projects" href="/mcp/core/create-tests-new-project">
    Learn how to create tests for new projects
  </Card>

  <Card title="Create Tests for New Change" href="/mcp/core/create-tests-new-feature">
    Learn how to create tests for new features and changes
  </Card>

  <Card title="Modify or Update Tests" href="/mcp/core/modify-tests">
    Learn how to modify and update existing tests
  </Card>

  <Card title="MCP Tools Reference" href="/mcp/core/tools">
    Reference guide for MCP tools and commands
  </Card>
</Columns>


Built with [Mintlify](https://mintlify.com).