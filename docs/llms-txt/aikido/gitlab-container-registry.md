# Source: https://help.aikido.dev/container-image-scanning/standalone-registries/gitlab-container-registry.md

# Gitlab Container Registry

You can now integrate your (cloud) Gitlab Container Registry with Aikido to scan your containers for known vulnerabilities.

Follow the simple steps below to activate this feature:

**Step 1:** Log into your Gitlab account to gather some data.

We'll have to gather your username (see screenshot)

![User profile dropdown displaying name, username, and status option in a web application.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-0af8953d661da3d27bd7aac01cc1adcd97b50a70%2Fgitlab-container-registry_7a56ad48-6f3c-4291-97c1-b36896ef0de0.png?alt=media)

**Step 2:** Copy the group ID where the container registry resides (see screenshot)

![Organization profile showing group name, privacy status, plan type, and group ID.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-df1cc77167c9a675613b9ae735d3408906f102b7%2Fgitlab-container-registry_d24c6206-b2dc-46f9-9853-088e55e58f1f.png?alt=media)

**Step 3:** Under personal preferences, Access tokens, create a new token for Aikido (direct link: <https://gitlab.com/-/user_settings/personal_access_tokens>).

The scopes included must be: read\_api, read\_registry

See screenshot:

![Form for creating a new personal access token with selectable API access scopes.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-a1cbdb7c980480d5a2ad4f72e88c9f5f7d11dfc2%2Fgitlab-container-registry_3517ec50-78f0-4a11-b196-5c0652c97a93.png?alt=media)

**Step 4:** Enter the collected data in Aikido (direct link: <https://app.aikido.dev/settings/container-image-registry/add/gitlab>)

![GitLab container registry connection form: enter username, access token, and group ID.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-306a6f71f05112c9098492d79260911101bc9d1a%2Fgitlab-container-registry_88cde87d-a1da-4a9a-9443-f1befbf61c9f.png?alt=media)

**Step 5:** Aikido will now find all container repositories you can access and list them.

**Step 6:** Repositories can be linked to a code repository in order to perform better deduplication of findings. This step is optional!

**Step 7:** In the action menu next to the registry, click 'scan repos in registry' to get started. Results will appear in the Feed!

***
