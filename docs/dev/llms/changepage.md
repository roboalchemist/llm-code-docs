# Source: https://dev.writer.com/blueprints/changepage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Change page

Navigates the user to another page in the app. Requires a valid page key.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/change-page-block.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=8832b5bfbb278334f7afe136a09b7f8a" alt="" data-og-width="2310" width="2310" data-og-height="1490" height="1490" data-path="images/agent-builder/blueprints/change-page-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/change-page-block.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=2be811817153d5cfb1ebbbaf861691b5 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/change-page-block.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=f43702e535f427a5d3dd0a47e2c2c5bc 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/change-page-block.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=b21806deacaffbea9957a957950fb138 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/change-page-block.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=cbf633136597eaf8701b7acc4039b17a 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/change-page-block.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=534598e0711f3951df4e33f5b529ded7 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/change-page-block.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=e18957dc48c12bed555b1ec3056376e8 2500w" />

## Overview

The **Change page** block navigates the user to a different page in the application. Use it to control the flow of your app, redirect after actions, or guide users through multi-step processes.

You can specify the target page and optionally pass parameters.

## Common use cases

* Redirecting users after form submission
* Navigating between steps in a multi-step workflow
* Sending users to a confirmation or error page
* Guiding users through onboarding or tutorials

## How it works

1. **Page**: Enter the name or path of the page to navigate to. Each page needs a unique key to identify it in the blueprint.
2. **Parameters**: Optionally specify parameters to pass to the new page.

The block triggers a navigation event, sending the user to the specified page.

## Examples

### Post-submission redirect

**Interface:**

1. A page with text inputs for name and email, and a button to submit the form.
2. A second page with the key `confirmation_page`. It contains a message to confirm the form submission with more details about the form submission.

**Blueprint Flow:**

1. **UI Trigger** → User presses button to submit a form
2. **Change page** → Navigates to the page with the key `confirmation`

**Block Configuration:**

* **Page key:** `confirmation`

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/change-page-workflow.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=d4a55d03e5ea0bef1e66c3b895286089" alt="" data-og-width="1846" width="1846" data-og-height="836" height="836" data-path="images/agent-builder/blueprints/change-page-workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/change-page-workflow.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=4b48e5f89d8cdaf5c3c890eb98f9ee5c 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/change-page-workflow.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=eb7c36c1ffe9c6ce4d235615bae41ab0 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/change-page-workflow.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=18280255f282d82e037db881faacb255 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/change-page-workflow.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=e7a35e35ccc150d0d0840ee76e558b40 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/change-page-workflow.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=6e18f1db3b6fc0d1aa4c8dfe62a348a1 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/change-page-workflow.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=a93d301c023e87f5244751f741c641ec 2500w" />

This workflow ensures users are directed to the confirmation page after submitting the form.

## Fields

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Type</th>
    <th>Control</th>
    <th>Default</th>
    <th>Description</th>
    <th>Options</th>
    <th>Validation</th>
  </thead>

  <tbody>
    <tr>
      <td>Page key</td>
      <td>Text</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>The identifying key of the target page.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>
  </tbody>
</table>

## End states

Below are the possible end states of the block call.

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
  </thead>

  <tbody>
    <tr>
      <td>Success</td>
      <td>-</td>
      <td>success</td>
      <td>The page change was successful.</td>
    </tr>

    <tr>
      <td>Error</td>
      <td>-</td>
      <td>error</td>
      <td>There was an error changing the page.</td>
    </tr>
  </tbody>
</table>
