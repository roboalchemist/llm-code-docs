# Source: https://momentic.ai/docs/steps/conditional.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Conditional

> Execute an "if statement" and perform steps if true

This step evaluates a condition and runs child steps when it passes. You can
choose an AI Assertion, JavaScript condition, or Page Check. To add child steps,
hover over the Conditional step and in the action bar, click Add Child.

If the condition is false, the Conditional step will be marked as having passed,
skip nested steps, and continue with the test.

## Inputs

<ResponseField name="Conditional type" type="dropdown" required>
  The type of condition to check.
</ResponseField>

<Tabs>
  <Tab title="AI Assertion">
    <ResponseField name="Assertion" type="string" required>
      Describe the condition in plain English. The assertion can be as specific
      or as broad as you like.
    </ResponseField>
  </Tab>

  <Tab title="JavaScript">
    <ResponseField name="JavaScript" type="string" required>
      Write code that returns a truthy or falsy value. Truthy executes the
      block, falsy skips it. Errors fail the Conditional step.
    </ResponseField>
  </Tab>

  <Tab title="Page Check">
    <ResponseField name="Page check" type="string" required>
      Define the page content assertion. If the check fails, the block is
      skipped and the Conditional step still passes. Errors fail the Conditional
      step.
    </ResponseField>
  </Tab>
</Tabs>

## Configs

<ResponseField name="Disable caching" type="boolean" default={false}>
  Disable [caching](/step-cache) for this step. Useful for elements that should
  always be located dynamically, such as table rows, search results, or graph
  nodes that may be re-ordered.
</ResponseField>

<ResponseField name="Timeout" type="number" default={5}>
  Max number of seconds for the action to finish.
</ResponseField>

<ResponseField name="AI context mode" type="string" default="HTML & screenshot">
  Choose between a general-purpose AI model that can understand both HTML &
  screenshots, or an advanced vision-only model optimized for visual attributes.
</ResponseField>

<SaveToEnv />


Built with [Mintlify](https://mintlify.com).