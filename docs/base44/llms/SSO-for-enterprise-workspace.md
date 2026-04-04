# Source: https://docs.base44.com/Enterprise/SSO-for-enterprise-workspace.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting up SSO for your enterprise workspace

> Connect your trusted identity provider to keep workspace access secure and simple for your team.

***

## SSO for workspaces

Single Sign-On (SSO) lets your organization’s members access Base44 using your company’s login credentials instead of separate passwords. When you enable SSO, your team can sign in using your organization’s identity provider (such as Google or Azure), which streamlines onboarding and reduces security risks from weak or reused passwords.

<Info>
  **Note:** When SSO is enabled, anyone with the configured email domain can log in only through SSO. After they log in, they are automatically added to the workspace as members with the Viewer seat type.
</Info>

***

## Setting up SSO

Follow the steps below to connect your workspace to your identity provider and enable SSO for your team.

<Note>
  **Before you begin:**

  Find your workspace ID. You will need it to complete step 4 below. Your workspace ID is the number and letter string after`/workspace/`in your enterprise workspace URL.
</Note>

**To set up SSO:**

1. Click your profile icon at the top right of your account.
2. Click the relevant workspace name.
3. Click **Settings** in your profile menu.
4. Click **Auth and security**.
5. Enable the toggle next to **Single Sign-On Configuration**.
6. Follow our guide on [Setting up SSO](https://docs.base44.com/Guides/Setting-up-SSO) according to your identity provider.

<Warning>
  Important:

  * When following the guide, replace the article’s redirect URI  `https://app.base44.com/api/apps/{{APP_ID}}/auth/sso/callback`with 

    `https://app.base44.com/api/workspaces/{{WORKSPACE_ID}}/auth/sso/callback.`
  * Note that  in the redirect URI,`APP_ID` is replaced by `WORKSPACE_ID`, and the path `/apps/` is changed to `/workspaces/`.
</Warning>

5. Enter your details in the **SSO** section of your enterprise workspace.
6. Click **Enable SSO**.

<Tip>
  Tip: After you have completed the set up, [test that your SSO works](https://docs.base44.com/Guides/Setting-up-SSO#step-3--test-your-sso-login).
</Tip>

***

## FAQs

Select a question below to learn more.

<AccordionGroup>
  <Accordion title="Can I enable SSO for only some members of my workspace?">
    No. Once SSO is enabled for your workspace, all members with a matching email domain are required to use SSO for login.
  </Accordion>

  <Accordion title="How do I test that SSO is working after setup?">
    Invite a colleague with the approved email domain to log in using SSO. If they can sign in and are added as a member, your SSO configuration is working.
  </Accordion>

  <Accordion title="Can I disable SSO later if my organization’s needs change?">
    Yes. Workspace admins can disable SSO from the **SSO** tab in your workspace settings at any time.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).