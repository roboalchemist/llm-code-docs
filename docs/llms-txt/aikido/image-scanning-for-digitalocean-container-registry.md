# Source: https://help.aikido.dev/container-image-scanning/cloud-provider-registries/image-scanning-for-digitalocean-container-registry.md

# DigitalOcean Container Registry

You can integrate your DigitalOcean Container Registry with Aikido to scan your containers for known vulnerabilities.

Follow the simple steps below to activate this feature:

**Step 1:** Log into your DigitalOcean account to gather some data.

We'll have to gather only a Personal Access Token (PAT). Direct URL: <https://cloud.digitalocean.com/account/api/tokens> (see screenshot below)

![Form to create a new personal access token with scope and expiration options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-cb44c25bfe8ab8dc6c51683770159008ade28a57%2Fimage-scanning-for-digitalocean-container-registry_34100e62-59be-4a33-902d-20c0ebbd4418.png?alt=media)

**Step 2:** Enter the collected data in Aikido (direct link: <https://app.aikido.dev/settings/container-image-registry/add/digitalocean>)

![Form to connect DigitalOcean container image registry with nickname and access token.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9a6ae90feb2a8c4ba1b07de8e0198980d5da0710%2Fimage-scanning-for-digitalocean-container-registry_937e0175-88c2-4c79-94f8-d015e01bdf18.png?alt=media)

**Step 3:** Aikido will now find all container repositories you can access and list them.

**Step 4:** Repositories can be linked to a code repository in order to perform better deduplication of findings. This step is optional!

**Step 5:** In the action menu next to the registry, click 'scan repos in registry' to get started. Results will appear in the Feed!

***
