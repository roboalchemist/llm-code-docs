# Source: https://docs.testsprite.com/mcp/core/modify-tests.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.testsprite.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Modify or Update Tests

> Update existing tests to reflect changes in your application using TestSprite's interactive in-place editing capabilities.

## Overview

TestSprite gives you full control over your automated test cases with powerful in-place editing. Whether you're watching tests run live or reviewing results days later, you can fine-tune every step to match your exact requirements.

<Frame>
  <img src="https://mintcdn.com/testspriteinc/teCzVODp75jc8wZz/images/modification-hero.png?fit=max&auto=format&n=teCzVODp75jc8wZz&q=85&s=9c4dbce7439fe762caf25db8f2b703dc" alt="modification hero" width="1730" height="895" data-path="images/modification-hero.png" />
</Frame>

## Interactive Step Editing

Click on any step to see a **snapshot** of that exact moment in your test, then modify it if needed.

<Frame>
  <img src="https://mintcdn.com/testspriteinc/teCzVODp75jc8wZz/images/edit-locator.png?fit=max&auto=format&n=teCzVODp75jc8wZz&q=85&s=798d2951026c3190c29b9434bd1ce411" alt="modification hero" width="1416" height="731" data-path="images/edit-locator.png" />
</Frame>

### Edit Any Interaction

When you select a step, you can:

<Steps>
  <Step title="Change the Interaction Type">
    Switch between Click, Navigate, Input, Scroll, Assert, or modify the Selector.

    <Frame>
      <img src="https://mintcdn.com/testspriteinc/teCzVODp75jc8wZz/images/interaction-type.png?fit=max&auto=format&n=teCzVODp75jc8wZz&q=85&s=2a87c0d4d6b4bc99ada4e8f55f2c7725" alt="change interaction type" width="1730" height="895" data-path="images/interaction-type.png" />
    </Frame>
  </Step>

  <Step title="Update Input Values">
    Change what text gets entered into form fields.

    <Frame>
      <img src="https://mintcdn.com/testspriteinc/teCzVODp75jc8wZz/images/input-value.png?fit=max&auto=format&n=teCzVODp75jc8wZz&q=85&s=40349b49c4c44ace9f0a378218af4db3" alt="update input values" width="1730" height="895" data-path="images/input-value.png" />
    </Frame>
  </Step>

  <Step title="Adjust Timeouts">
    Fine-tune wait times for slow-loading elements.

    <Frame>
      <img src="https://mintcdn.com/testspriteinc/yeKotwyCFP3KWMF-/images/time-out.png?fit=max&auto=format&n=yeKotwyCFP3KWMF-&q=85&s=a7b6946bd1b87cc40ea17fd2c29d968d" alt="adjust timeouts" width="1730" height="682" data-path="images/time-out.png" />
    </Frame>
  </Step>

  <Step title="Modify Interaction Element">
    Pick a new element on the page if the current one isn't right.

    <Frame>
      <img src="https://mintcdn.com/testspriteinc/teCzVODp75jc8wZz/images/modify-interaction.png?fit=max&auto=format&n=teCzVODp75jc8wZz&q=85&s=4081a509bac80a22ec93db2fe7e58282" alt="modification hero" width="3460" height="1790" data-path="images/modify-interaction.png" />
    </Frame>
  </Step>
</Steps>

### Visual Element Selection

Don't like the current locator? Simply click any element on the page preview, and TestSprite will prompt you: *"Change locator to this element to suit your needs."*

This visual selection means you don't need to manually write CSS selectors or XPath—just point and click.

<Frame>
  <img src="https://mintcdn.com/testspriteinc/qvVl4_9ScMi7zBCG/images/change-locator.png?fit=max&auto=format&n=qvVl4_9ScMi7zBCG&q=85&s=4ac77a8f8f4d5400e1d8c5dfdbd2dec7" alt="change locator" width="1412" height="729" data-path="images/change-locator.png" />
</Frame>

### Smart Regeneration Options

TestSprite will automatically regenerate the affected steps while preserving your customizations.

<Frame>
  <img src="https://mintcdn.com/testspriteinc/teCzVODp75jc8wZz/images/run-type.png?fit=max&auto=format&n=teCzVODp75jc8wZz&q=85&s=37776b8c350ca8c93e3ebff574fa21ed" alt="smart regeneration options" width="1730" height="682" data-path="images/run-type.png" />
</Frame>

After making your edits, choose how TestSprite should handle the changes:

| Option                                     | When to Use                                                      |
| ------------------------------------------ | ---------------------------------------------------------------- |
| <kbd>Update this step only</kbd>           | Your change is isolated and doesn't affect subsequent steps      |
| <kbd>Update this and following steps</kbd> | Your change impacts the test flow, and later steps need to adapt |

## Key Benefits

<AccordionGroup>
  <Accordion title="No More Black-Box Testing">
    See exactly what your tests are doing with video recordings and step-by-step snapshots.
  </Accordion>

  <Accordion title="Fix Tests Without Rewriting Them">
    Visual editing means you can adjust locators, inputs, and actions without touching code.
  </Accordion>

  <Accordion title="Maintain Test Suites Over Time">
    As your application evolves, easily update test steps to match new UI layouts or workflows.
  </Accordion>

  <Accordion title="Debug Failures Faster">
    Pinpoint issues instantly with detailed error messages and execution recordings.
  </Accordion>
</AccordionGroup>

## Quick Reference

| Tool                                    | Purpose                                            |
| --------------------------------------- | -------------------------------------------------- |
| `testsprite_generate_code_and_execute`  | Generate and run tests with live progress tracking |
| `testsprite_open_test_result_dashboard` | Reopen dashboard to review/edit past test runs     |

## Next Step

<Columns cols={2}>
  <Card title="Progress Dashboard" href="/mcp/core/test-progress-dashboard">
    Monitor real-time test execution
  </Card>

  <Card title="Create Tests for New Change" href="/mcp/core/create-tests-new-feature">
    Test diff-scoped changes
  </Card>

  <Card title="Healing & Observability" href="/mcp/concepts/healing-observability">
    Learn about auto-healing
  </Card>

  <Card title="MCP Tools Reference" href="/mcp/core/tools">
    Explore all available tools
  </Card>
</Columns>


Built with [Mintlify](https://mintlify.com).