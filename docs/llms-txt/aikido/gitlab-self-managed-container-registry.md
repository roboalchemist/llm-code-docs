# Source: https://help.aikido.dev/container-image-scanning/standalone-registries/gitlab-self-managed-container-registry.md

# Gitlab Self Managed Container Registry

You can integrate your Gitlab Self Managed Container Registry with Aikido to scan your containers for known vulnerabilities.

Follow the simple steps below to activate this feature:

**Step 1:** Log into your Gitlab account to gather some data.

We'll have to gather your username (see screenshot)

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-0af8953d661da3d27bd7aac01cc1adcd97b50a70%2Fgitlab-self-managed-container-registry_ee118282-ecab-4687-8d5e-9885f6bf5aad.png?alt=media)

**Step 2:** Copy the group ID where the container registry resides (see screenshot)

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-df1cc77167c9a675613b9ae735d3408906f102b7%2Fgitlab-self-managed-container-registry_9c7c898a-dc4e-4169-82c2-708df1c479f1.png?alt=media)

**Step 3:** Go to **Personal Preferences** >>  **Access tokens**, and create a new personal access token for Aikido ([direct link](https://gitlab.com/-/user_settings/personal_access_tokens)). Make sure to set the correct scopes: `read_api`, `read_registry`

{% hint style="warning" %}
Make sure to create a **Personal Access Token**, and not an **Impersonation Token**.
{% endhint %}

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-a1cbdb7c980480d5a2ad4f72e88c9f5f7d11dfc2%2Fgitlab-self-managed-container-registry_167e7af9-436c-43f9-a585-a6bd0d693234.png?alt=media)

**Step 4:** Enter the collected data in Aikido (direct link: <https://app.aikido.dev/settings/container-image-registry/add/gitlab-self>)

![Form to connect GitLab self-hosted container image registry with required credentials.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1d7d325723206eb09c82e4f65505054774ab3ecf%2Fgitlab-self-managed-container-registry_1d74b1b9-dacb-49e5-840f-1d3e7e38ab6e.png?alt=media)

**Step 5:** Aikido will now find all container repositories you can access and list them.

**Step 6:** Repositories can be linked to a code repository in order to perform better deduplication of findings. This step is optional!

**Step 7:** In the action menu next to the registry, click 'scan repos in registry' to get started. Results will appear in the Feed!

***
