# Source: https://docs.base44.com/documentation/using-your-workspaces/managing-your-workspace-apps.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing your workspace apps

> Move apps between workspaces, control who can transfer apps out, and manage app ownership.

Your apps live inside your Base44 workspaces, where you and your team build, test, and ship together. You can move apps between workspaces and manage ownership when responsibilities change.

***

## Moving an app between workspaces

Move an app from its current workspace to another workspace you belong to. After the move, the app follows the target workspace's permissions and settings, and you remain the app owner.

<Check>
  **Before you begin:**

  * You must be the **app owner**.
  * You must be a member of the target workspace, and it must be different from the current workspace.
  * App transfers must be enabled in the current workspace.
  * The app cannot be a purchased app.
</Check>

**To move your app:**

1. Open your app in its current workspace.
2. Go to your app's dashboard and click **Overview**.
3. Click **Move App** next to **Move to Workspace**.
4. Select the workspace to move your app to.
5. Click **Move App** to confirm.

<Frame caption="Moving an app between workspaces">
  <img src="https://mintcdn.com/base44/4OPwWJTa9SAkAhBo/images/MoveApp.png?fit=max&auto=format&n=4OPwWJTa9SAkAhBo&q=85&s=8ac6e41deb79c29ba1054ebcb73b51dd" alt="Moving an app between workspaces" className="mx-auto" width="788" height="370" data-path="images/MoveApp.png" />
</Frame>

***

## Transferring app ownership

App owners can transfer ownership of an app to another collaborator so the right person manages billing, permissions, and app settings. This is useful when responsibilities shift or when someone changes roles.

The new owner must accept the transfer by email before it takes effect.

<Check>
  **Before you begin:** The new owner must be a member of the workspace and have a paid plan or seat.
</Check>

<Warning>
  **Important:**

  * Only the current app owner can transfer ownership.
  * Both the current and new app owner must be on a **Builder** plan or higher. The app will follow the new owner's current plan limits and features.
  * If the new owner's plan does not support features already used in the app, those features may not work as expected.
  * After the transfer, all future edits, updates, and app usage use credits from the new owner's account.
  * Transferring ownership does not move the app between workspaces or change its visibility.
</Warning>

**To transfer ownership of your app:**

1. Go to your app editor.
2. Click the **Invite collaborators** icon <Icon icon="circle-plus" /> at the top right.
3. Find the collaborator you want to transfer ownership to.
4. Click the **More Actions** icon <Icon icon="ellipsis" /> next to their name and click **Make app owner**.
5. Confirm the transfer details:
   * Select the checkbox to confirm that the selected person becomes the new owner, including all app data, media, and connected third-party services and accounts.
   * Select the **Disconnect integrations after transfer** checkbox if you want to remove existing external connections for security. The new owner can reconnect their own accounts after the transfer.
6. Click **Change Ownership**.
7. Ask the new owner to open the email from Base44 and click the confirmation link to accept the new ownership.

<Frame caption="Transferring app ownership to another collaborator">
  <img src="https://mintcdn.com/base44/4A7u6YLc4Mb03Ghd/images/appownertransfer.png?fit=max&auto=format&n=4A7u6YLc4Mb03Ghd&q=85&s=67a5924e1fab637a0604cf9ed80f933c" alt="Transferring app ownership to another collaborator from the collaborators modal" className="mx-auto" width="619" height="424" data-path="images/appownertransfer.png" />
</Frame>

***

## FAQs

Click a question below to learn more.

<AccordionGroup>
  <Accordion title="What happens after I move an app to a different workspace?">
    After moving an app to another workspace:

    * The app follows the target workspace's permissions and settings.
    * The published app URL does not change.
    * All app data, media, and configurations remain with the app.
    * Credits do not transfer with the app. Each workspace member uses credits from their own plan. Learn more about [using credits with teams](/Account-and-billing/Credits#using-credits-with-teams).
  </Accordion>

  <Accordion title="Can I move my app back after transferring it to another workspace?">
    Yes. You can move an app again as long as:

    * You are the app owner.
    * App transfers must be enabled in the current workspace.
    * You are a member of the target workspace.

    If transfer policies restrict moving the app out, you may need a workspace admin to adjust the settings.
  </Accordion>

  <Accordion title="Can I move an app from a shared workspace to a personal workspace?">
    Yes. You can move an app to any workspace you are a member of, including your personal workspace, as long as you are the app owner and app transfers are enabled in the current workspace.
  </Accordion>

  <Accordion title="Why can't I move my app to another workspace?">
    You may not be able to move an app if:

    * You are not the app owner.
    * The app is a purchased app.
    * App transfers are disabled in the current workspace.
    * You are not a member of the target workspace.
  </Accordion>

  <Accordion title="How do I enable app transfers in my workspace?">
    Workspace owners can control who is allowed to move apps out of the workspace to another workspace.

    **To enable app transfers in your workspace:**

    1. Click your **profile icon** at the top-right of your account.
    2. Click the relevant **workspace name**.
    3. Click **Account Settings** on your account menu.
    4. Under **Workspace**, click **Apps configuration**.
    5. Under **App Transfers**, choose who can move apps out of this workspace:
       * **Workspace admins and owners**
       * **Workspace owners only**
       * **Disabled**

    <Frame caption="Enabling app transfers in workspace settings">
      <img src="https://mintcdn.com/base44/XjZSvMbKIsBP3mXg/images/apptransfersworkspaces-1.png?fit=max&auto=format&n=XjZSvMbKIsBP3mXg&q=85&s=e14ca0d83ea4ade7509cc324aabb7f38" alt="Choosing who can move apps out of the workspace." className="mx-auto" className="mx-auto" width="918" height="429" data-path="images/apptransfersworkspaces-1.png" />
    </Frame>
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).