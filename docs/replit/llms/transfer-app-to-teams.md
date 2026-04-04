# Source: https://docs.replit.com/teams/identity-and-access-management/transfer-app-to-teams.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Transfer App to Teams

> Move personal apps to team workspaces for collaboration

Transfer your personal Replit Apps to team workspaces to enable collaboration and centralized project management. This process allows you to:

* Share apps with team members instantly
* Centralize project management within your organization
* Maintain deployment uptime and URLs during transfer

## What is app transfer?

App transfer moves ownership of a Replit App from your personal workspace to a team workspace. Once transferred, the app becomes accessible to team members according to workspace permissions and is managed under the team's resources and billing.

The transfer process is immediate and irreversible, but maintains all deployment configurations and URLs.

## Getting started

You must be a member of the target team workspace before transferring apps. Verify your team membership by selecting your profile or workspace selector in the upper-right corner to view available teams.

<Note>
  * Transferring a Replit App to a team workspace is irreversible
  * Published apps experience zero downtime during transfer
  * Deployment URLs remain unchanged
  * You must be a member of the team you want to transfer the app to before initiating transfer
</Note>

## How it works

<Steps>
  <Step title="Access your Apps">
    Navigate to your personal Apps by selecting the **Apps** tab from your Replit home page.
  </Step>

  <Step title="Select the app">
    Locate the application you want to transfer in your Apps list.
  </Step>

  <Step title="Open transfer options">
    Select the **three dots (•••)** menu next to the app name.

    <Frame>
      <img src="https://mintcdn.com/replit/Ey8_iLkPLqrKZFjt/images/teams/transfer-app-to-org.png?fit=max&auto=format&n=Ey8_iLkPLqrKZFjt&q=85&s=bc7b26f9201cfc8e6f90378bbd1cda01" alt="Three dots menu next to app name showing transfer options" data-og-width="2606" width="2606" data-og-height="1220" height="1220" data-path="images/teams/transfer-app-to-org.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/Ey8_iLkPLqrKZFjt/images/teams/transfer-app-to-org.png?w=280&fit=max&auto=format&n=Ey8_iLkPLqrKZFjt&q=85&s=f3d8034873ab7f74f81b3a1dd874c570 280w, https://mintcdn.com/replit/Ey8_iLkPLqrKZFjt/images/teams/transfer-app-to-org.png?w=560&fit=max&auto=format&n=Ey8_iLkPLqrKZFjt&q=85&s=1e921cec2d23841360eed14f22c2039f 560w, https://mintcdn.com/replit/Ey8_iLkPLqrKZFjt/images/teams/transfer-app-to-org.png?w=840&fit=max&auto=format&n=Ey8_iLkPLqrKZFjt&q=85&s=f254228c448fc82c463fb056c42c943f 840w, https://mintcdn.com/replit/Ey8_iLkPLqrKZFjt/images/teams/transfer-app-to-org.png?w=1100&fit=max&auto=format&n=Ey8_iLkPLqrKZFjt&q=85&s=912b45a2e09238b59df91ec6cca2b21a 1100w, https://mintcdn.com/replit/Ey8_iLkPLqrKZFjt/images/teams/transfer-app-to-org.png?w=1650&fit=max&auto=format&n=Ey8_iLkPLqrKZFjt&q=85&s=fd068ec0be7ca79972ea3931a8f3c262 1650w, https://mintcdn.com/replit/Ey8_iLkPLqrKZFjt/images/teams/transfer-app-to-org.png?w=2500&fit=max&auto=format&n=Ey8_iLkPLqrKZFjt&q=85&s=5a34a08692fe6e6902404a8f9918ab60 2500w" />
    </Frame>
  </Step>

  <Step title="Choose transfer option">
    Select **Transfer To Organization** from the dropdown menu.
  </Step>

  <Step title="Select destination">
    Choose the target team workspace from the available organizations dialog.
  </Step>

  <Step title="Confirm transfer">
    Select **Transfer To Organization** to confirm the action.
  </Step>

  <Step title="Verify completion">
    You'll see a "Transfer success" notification in the bottom-right corner of the page. Refresh your Apps page to verify the app no longer appears in your personal workspace, then navigate to your team workspace to confirm the app appears there.
  </Step>
</Steps>

## Bulk transfer options

For transferring multiple applications, use CLUI commands:

* **Core to team workspace**: Use `org transfer-repls`
* **Team to team workspace**: Use `org transfer-repls-org-to-org`

## Next steps

To learn more about team collaboration and workspace management, see the following resources:

* [Replit Teams overview](https://docs.replit.com/category/teams) - Learn about team workspace features
* [CLUI commands reference](https://docs.replit.com/additional-resources/clui-graphical-cli) - Explore bulk transfer options
