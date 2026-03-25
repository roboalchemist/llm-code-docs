# Source: https://help.aikido.dev/aikido-autofix/configure/autofix-for-azure-devops.md

# AutoFix for Azure DevOps

Aikdo Autofix is a tool you can use to have Aikido fix vulnerabilities in 3rd party dependencies in your projects. It will do this by creating pull requests that remove the vulnerability via package updates or by other means. In some cases an Aikido Autofix can remove a whole class of vulnerabilities instead of just 1 issue.

**Setup Autofix for Azure DevOps**

> All users within your workspace will need to setup Autofix individually.

By default, Aikido only has read access on your Azure DevOps instance. To use Aikido Autofix, a separate access token with write access is required. Please make sure that "Third-party application access via Oauth" is enabled for your organization, by going to "Organization settings" and then clicking "Policies".

![Organization security policies for application access, public projects, and user invitations.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5838be9321d66745e34538f24fbe49aa8a9d87b3%2Fautofix-for-azure-devops_de2304d7-85d2-4b8b-8d71-24259117f59d.png?alt=media)

**Step 1. Enable Autofix on the** [**Autofix Settings**](https://app.aikido.dev/settings/integrations/autofix) **page or go to** [**Autofix Page**](https://app.aikido.dev/issues/fix) **and click on Enable Autofix.**

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-fa22c0fe756aa9b8798105f9eb95615910b3b1aa%2Fautofix-for-azure-devops_9ac87091-7eef-4f05-86a1-a137f2ddf68c.png?alt=media)

**Step 2.** Click **Authorize**

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8e0bfca4d503fe03033049c4e9acef167939d78a%2Fautofix-for-azure-devops_8a0e9ba1-c135-4e5f-a37b-3de7ddee86d0.png?alt=media)

**Step 3.** Grant Aikido permissions to **Write**

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-30e1ec1c11d447e28ee9cab714f33707a17210a0%2Fautofix-for-azure-devops_ad9f2ecc-7a4f-4c78-8e74-2429a4b8e7a8.png?alt=media)

**Step 4.** Click save and you are all set. You will now be able to execute autofix PRs from the [Autofix page](https://app.aikido.dev/issues/fix) or from the action menu for subissues in the sidebar ([read more here](https://help.aikido.dev/aikido-autofix/autofix-for-open-source-dependencies)).
