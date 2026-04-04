# Source: https://docs.jit.io/docs/azure-devops-integration.md

# Azure Devops Integration

Integrating with Azure Devops

Integrating **Azure DevOps** with Jit allows you to assign security-related findings directly to Engineering and Security teams from the Jit platform. Learn more about this [here](https://docs.jit.io/docs/integrating-with-tms).

# Web App Integration

## Quickstart

1. In the Jit web app, go to the **Integrations** page.

2. Find the **Azure DevOps** card and click **Connect**.

[block:image]{"images":[{"image":["https://files.readme.io/f4d886af49b6d5be108690c6957223b2bb564e86cc5a8f0a1401bf673fe94277-Screenshot_2025-08-03_at_17.32.14.png","",""],"align":"center"}]}[/block]

3. A connection window will appear. Click **Connect** in the top-right corner.

   ![](https://files.readme.io/90e9787e3c338fc2aaf77db5db4834b927ee59a931fcff594f218e2f6a622331-image.png)

4. Generate and provide a **Personal Access Token (PAT)**:

   1. Log into your Azure DevOps account.

   2. Go to **User Settings** → **Personal Access Tokens**.\
      ![](https://files.readme.io/4e1a616651141bc6ae5dd1b7baeb9c6ff094861e96ba2d8fce9fc6d7d9e01ad2-image.png)

   3. Create a new token: set a name, expiration date, and under **Work Items**, select **Read, write, & manage** permissions.\
      ![](https://files.readme.io/fe5335ceefc497d3b58775567f3ef3d99c67388065393844088fc6727d901d2b-image.png)

   4. Copy the token and paste it in the **Personal Access Token** field.

   5. Enter the server URL (typically `https://dev.azure.com/ORGANIZATION_NAME`).

   > ❗️ Note your token expiration
   >
   > Make note on the expiration - You will need to reconnect when expiration is reached.

5. Configure the integration:

   * **Default Board and State** – Choose the board, work item type, and states for your tickets.
   * **Create Item Fields** – If your items use [custom fields](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/work/add-custom-field?view=azure-devops), select the project and provide the required values.

     ![](https://files.readme.io/0942909270e09ea55b1dbaee3e6e357e19aa37f7766ce4db507a52b40a7b80fa-image.png)

     <br />

     > ❗️ **Important**
     >
     > * Values must match their field types.
     > * The selected project must match in both sections.
     > * If not all fields appear, refresh the browser and reopen the integration.

***

## Features

### Create Items from Findings

From the **Backlog** page, create items and select the target project.\
![](https://files.readme.io/20c5bee5132dce9a85bc93c231fe7a540c3a29ef392401b88b1421f5516e2158-image.png)

<br />

### Auto-Close Items

Enable this option to automatically move items to **Completed** when findings are fixed.

<br />

### Sync Ticket Status

Enable webhook syncing to update the ticket status in Jit when items are completed.

> ❗️ Make sure the relevant project is selected in **Create Item Fields**, even if no custom fields are needed.

<br />

### Workflows

Integrate Azure DevOps into your workflows to automate ticket creation.

1. After connecting, set a default project and optionally add more project configurations.
2. Go to **Settings → Workflows** to create automation rules.

   ![](https://files.readme.io/e8546f61a946069ccad3aeaad0ae9ca6032bcd86cab8e3026d73551d252a3e77-image.png)

<br />
<br />

## Sample Item

![](https://files.readme.io/7201bbb1f4c0acb11e2500afa969800ca9f278f456fcea3e4a64dcd35f89f1be-image.png)

<br />

## Notes

* A label `Opened-by-jit` will be added to every created item to help Jit track tickets in your board.