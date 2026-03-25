# Source: https://docs.jit.io/docs/integrating-with-linear.md

# Linear Integration

Integrating with Linear

Integrating **Linear** into Jit enables you to efficiently assign security-related tickets from Jit directly to Engineering and Security teams. Learn more [here](https://docs.jit.io/docs/integrating-with-tms).

# Web App Integration

## Quickstart

1. In the Jit web app, go to the **Integrations** page.

2. Find the **Linear** card and click **Connect**.

   ![](https://files.readme.io/8dad7c712035c41f3cd3e7c49fc814879c0c35a1923bf2e139eeb7eaea7e4440-Screenshot_2025-09-11_at_08.59.21.png)

3. A connection window will appear. Click **Connect** in the top-right corner.

[block:image]{"images":[{"image":["https://files.readme.io/0734f084848efaba7168defbcaa95845e97900fc799156e1f02d5bfff81525d5-Screenshot_2025-09-11_at_09.00.09.png",null,""],"align":"center","sizing":"700px"}]}[/block]

4. After clicking connect, Linear will automatically integrate you. You have to authorize the Jit application.

[block:image]{"images":[{"image":["https://files.readme.io/9fae22cf8a9f971c2fec8ffe68aaac3fe5d1ff2a88e24b8a4d5ebb5dca06c8ba-Screenshot_2025-09-11_at_09.37.51.png",null,""],"align":"center","sizing":"600px"}]}[/block]

5. Configure the integration:

   * **Default Team and Project** – Choose the team, and an optional project within the picked team (you can't choose a project from a different team).
   * **Close Linear Tickets From Findings** – You can enable a workflow that will move tickets created from findings to the finish status of your choice when they are fixed. You have to use the team picked in the first step and specify the finished column.

   ![](https://files.readme.io/3c8671e8469a24a9cf44031ad2aede23259dd5d351bad2b3dacab984f8615a2f-Screenshot_2025-09-11_at_09.05.35.png)

> ❗️ **Important**
>
> * Values must match their field types.
> * The selected team must match in both sections.
> * If not all fields appear, refresh the browser and reopen the integration.

## Features

### Create Tickets from Findings

From the **Findings** page, create items and select the target project.

### Auto-Close Tickets

Enable this option to automatically move items to **Done** when findings are fixed.

### Workflows

Integrate Linear into your workflows to automate ticket creation.

1. After connecting, set a default project and optionally add more project configurations.
2. Go to **Settings → Workflows** to create automation rules.

   ![](https://files.readme.io/5833123f2dd1740d20619605731624f18a4f743dc04a27c427ee590f404c68e8-Screenshot_2025-09-11_at_09.13.03.png)

<br />

### Sync Ticket Status

When moving a ticket to **Completed**, Jit should ideally update the status on the corresponding finding. However, this requires the `admin` [scope in Linear](https://linear.app/developers/webhooks), which is overly broad and generally not recommended.

As a result, this functionality is not currently supported. If you require this capability, please contact Jit for assistance.

<br />

## Sample Item

![](https://files.readme.io/82b0533ad9dc7faafe5aa7a2d7b005beae18c174e1588436e44c38d76f2b0705-Screenshot_2025-09-11_at_09.12.17.png)