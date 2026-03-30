# Source: https://help.aikido.dev/container-image-scanning/standalone-registries/scaleway-container-registry.md

# Scaleway Container Registry

You can integrate your Scaleway Container Registry with Aikido to scan your containers for known vulnerabilities.

Follow the simple steps below to activate this feature:

**Step 1:** Log into your Scaleway account to gather some data.

We'll have to create an API key. Direct URL: <https://console.scaleway.com/iam/api-keys> (see screenshots below)

![User profile dropdown menu showing organization and account management options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-3e9f62a0f9ab9508491b7cede54aee3e48cc99b1%2Fscaleway-container-registry_3f7b7754-adbc-4804-94ef-440983cfddc7.png?alt=media)

![IAM dashboard for managing users, API keys, and access permissions in an organization.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-34d225fcd378b594434aa612621c9f109990ee0e%2Fscaleway-container-registry_450023c8-2142-4d95-adf4-3a04e5fc81a6.png?alt=media)

![API key generation form with user options and expiration settings.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-188fb23243c4c32fd9362047db70661e9b9f1a5c%2Fscaleway-container-registry_8372224e-4e80-46b1-9b6d-6cfb559de972.png?alt=media)

**Step 2:** Enter the collected data in Aikido (direct link: <https://app.aikido.dev/settings/container-image-registry/add/scaleway>)

![Form to connect and configure a Scaleway container image registry.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-941f91cc9fbf1dd8b46e54fea2ad42c90adbf430%2Fscaleway-container-registry_4cab47d9-c92e-4555-9c51-ac0766b728f6.png?alt=media)

**Step 3:** Aikido will now find all container repositories you can access and list them.

**Step 4:** Repositories can be linked to a code repository in order to perform better deduplication of findings. This step is optional!

**Step 5:** In the action menu next to the registry, click 'scan repos in registry' to get started. Results will appear in the Feed!

***
