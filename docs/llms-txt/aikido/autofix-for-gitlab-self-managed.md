# Source: https://help.aikido.dev/aikido-autofix/configure/autofix-for-gitlab-self-managed.md

# AutoFix for GitLab Self Managed

## Introduction

Aikdo Autofix is a tool you can use to have Aikido fix vulnerabilities in 3rd party dependencies in your projects. It will do this by creating pull requests that remove the vulnerability via package updates or by other means. In some cases an Aikido Autofix can remove a whole class of vulnerabilities instead of just 1 issue.

## Setup Autofix for GitLab Self Managed

By default, Aikido only has read access on your Gitlab Self Managed instance. To use Aikido Autofix a separate access token with write access is required.

**Step 1.** Enable Autofix on the [Autofix Settings](https://app.aikido.dev/settings/integrations/autofix) page or go to [Autofix Page](https://app.aikido.dev/issues/fix) and click on `Enable Autofix`.

**Step 2.** Click **Authorize**, and you will see this modal:

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-ffe05573d8848a62cde8f2467de7b83f7343f8c4%2Fautofix-for-gitlab-self-managed_847dce22-b557-4a36-8592-c8b97e558f46.png?alt=media)

**Step 3.** Head over to your Self Managed Gitlab account. Click on your personal account icon top left and go to preferences.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-733c8d013b17a93ee8982306c599fd6710522189%2Fautofix-for-gitlab-self-managed_1aa79b23-ea0e-473c-beb6-e60b3ff03d73.png?alt=media)

**Step 4.** In the sidebar, select Access Token. Then click the "Add new token"-button

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f694bf86108ac5ac18d1d436aabf1edfc548f5b3%2Fautofix-for-gitlab-self-managed_696b35be-f6ea-4bce-978d-0bede8b663ee.png?alt=media)

**Step 5.** Name the token 'Aikido Autofix' and add the following permissions: `api` & `write_repository`

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-39121ea57866ac8269739b8f0183f346dd8d5e25%2Fautofix-for-gitlab-self-managed_0a39f5aa-0e23-4e69-91a3-c94163f81db7.png?alt=media)

**Step 6.** Copy the newly created token and paste it into the modal in Aikido.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-64c318e10c8ba4d83dd33babf7eef03eeeedd4af%2Fautofix-for-gitlab-self-managed_75bb003e-2ebf-4687-8b8c-3c6049717027.png?alt=media)

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-b9cea0a66b77523b568bcb9fb8c897fb1a56bd03%2Fautofix-for-gitlab-self-managed_c1669df1-17da-4e97-b521-c71fc46b8e5d.png?alt=media)

**Step 7.** Click save and you are all set. You will now be able to execute autofix PRs from the [Autofix page](https://app.aikido.dev/issues/fix) or from the action menu for subissues in the sidebar.

***
