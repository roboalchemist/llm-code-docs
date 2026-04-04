# Source: https://docs.base44.com/documentation/account-and-billing/managing-your-workspace-members.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting up a workspace

> Set up your workspaces exactly as you need.

Setting up your workspace helps you organize collaboration, security, and branding before you start building apps with your team. From your workspace settings, you can create shared workspaces, control who has access, connect a branded domain, and configure security options such as SSO.

<Note>
  **Note:** The settings in this article apply only to shared workspaces. [Learn more about the difference between shared and personal workspaces](/documentation/account-and-billing/about-workspaces).
</Note>

***

## Creating a new workspace

When you create a new shared workspace, you are automatically the workspace owner and only you can manage the workspace.

<Note>
  You can create up to 2 shared workspaces per Base44 account.
</Note>

**To create a workspace:**

1. Click your profile icon at the top right of your account.
2. Click the <Icon icon="square-plus" /> icon next to **My Workspaces**.
3. Enter a name for your workspace.
4. Click **Create Workspace**.

<Frame caption="Creating a new workspace in your Base44 account">
    <img src="https://mintcdn.com/base44/KKc6awBfhSg9Deqm/images/createnewworkspace.png?fit=max&auto=format&n=KKc6awBfhSg9Deqm&q=85&s=89161fc1b2dde7454f26f9af3ff9bc81" alt="Creating a new workspace in your Base44 account" width="2168" height="1230" data-path="images/createnewworkspace.png" />
</Frame>

***

## Setting up a workspace

As an owner or admin of a workspace, you can customize your workspace settings to match your team’s needs. From the workspace settings, you can manage your workspace name and description, plan and billing, credit usage, seats and members, and authentication and security. In enterprise workspaces, you can also configure app level options from **Apps Configuration**.

You can also see your current plan, check your credit usage based on your assigned seat, and easily upgrade your plan.

**To set up your workspace:**

1. Click your profile icon at the top-right of your account.
2. Click the relevant workspace name.
3. Click **Settings** on your account menu.
4. Under **Workspace**, click **Basic information**.
5. Update your settings, including your **Workspace name** and **Workspace description**.

<Frame caption="Setting up your workspace information">
    <img src="https://mintcdn.com/base44/lEIH06mxdFyhpTHF/images/basicinfoshared.png?fit=max&auto=format&n=lEIH06mxdFyhpTHF&q=85&s=f2e035b5ed375e0b685d001700db76bf" alt="Setting up your workspace information" width="1778" height="456" data-path="images/basicinfoshared.png" />
</Frame>

***

## Setting up SSO for your workspace

Single Sign-On (SSO) lets everyone in your organization access Base44 with your company login instead of separate passwords. When you enable SSO for your workspace, your identity provider (such as Google or Microsoft) controls who can sign in, which helps keep access secure and onboarding simple.

To connect your workspace to your identity provider and turn on SSO, follow the steps in the article [Setting up SSO](https://docs.base44.com/Setting-up-your-app/Setting-up-SSO).

***

## Verifying your workspace domain

Verifying your workspace domain confirms that you control the domain you entered and lets you safely use it with SSO and email-based access rules in your workspace.

<Note>
  **Note:** DNS verification can take a few minutes, depending on your domain provider. Once your DNS records are updated, Base44 automatically verifies your domain. If verification does not complete after some time, click **Reset** in the Domain Verification section to generate a new TXT record and try again.
</Note>

**To verify your workspace domain:**

1. Click your profile icon at the top-right of your account.
2. Click the relevant workspace name.
3. Click **Settings** on your account menu.
4. Click **Auth and Security** under **Workspace.**
5. Update the **Workspace domain** field.
6. Click **Check**.
7. In the **Add DNS records for \[your-domain]** panel, copy the **Host / Name** and **Value** details for the TXT record.
8. In a new tab, sign in to your domain provider:
   1. Go to the DNS settings for your domain.
   2. Add a new **TXT** record using the exact **Host / Name** and **Value** shown in your workspace.
   3. Save your DNS changes with your domain provider.
9. Return to your workspace and wait while Base44 checks your DNS records. You see the status update under **Domain Verification**.

<Frame caption="Verifying your workspace domain">
    <img src="https://mintcdn.com/base44/VWcvQeFrNEj4Viek/images/domainver.png?fit=max&auto=format&n=VWcvQeFrNEj4Viek&q=85&s=d18e27139de6a783ab37f19d4382a734" alt="Verifying your workspace domain" width="1795" height="628" data-path="images/domainver.png" />
</Frame>

***

## FAQs

<AccordionGroup>
  <Accordion title="Can I delete a workspace?">
    No, you can’t delete a workspace. You can remove all members and apps from it, but the workspace itself stays active.
  </Accordion>

  <Accordion title="How do I rename a workspace?">
    Only workspace admins can rename a workspace.

    **To rename a workspace:**

    1. Click your profile icon at the top right of your account.
    2. Click your workspace name.
    3. Click **Settings** on your account menu.
    4. Under **Workspace**, click **Basic information**.
    5. Enter a new name under **Workspace name**.

    <Note>
      You can’t rename your personal workspace.
    </Note>

    <img src="https://mintcdn.com/base44/oUaRpzSyJvMVshj9/images/RenameWorkspace.png?fit=max&auto=format&n=oUaRpzSyJvMVshj9&q=85&s=24d734b88207e5250be5dc50b3349ff9" alt="Rename workspace panel" style={{ width:"100%" }} width="1021" height="331" data-path="images/RenameWorkspace.png" />
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).