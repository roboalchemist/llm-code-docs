# Source: https://help.aikido.dev/container-image-scanning/standalone-registries/quayio-cloud-registry.md

# Quay.io Cloud Registry

You can integrate your Quay.io container registry with Aikido to scan your containers for known vulnerabilities. Note that this only works for organization accounts, not for user accounts.

Follow the simple steps below to activate this feature:

**Step 1:** Log into your Quay account, go to Repositories via the top menu. On the right there should be a menu that lists the organizations. Click the organization you wish to link.

![Select a user or organization to create a new repository or organization.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-ce296027fd0496119143fa2a5af5592017b6384d%2Fquayio-cloud-registry_47f7b1df-6578-446d-a0b0-34cd464dbe41.png?alt=media)

**Step 2:** On the left-hand side menu, click 'Robot Accounts'. Then create a new Robot Account called Aikido. Grant it permissions to your repositories.

![Form to create a new robot account with name input and validation requirements.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9832e2e7fdb39251778b92f096918470ad2504cb%2Fquayio-cloud-registry_d39f90d5-61c7-479a-b77a-c90234cabb8b.png?alt=media)

**Step 3:** Click the name of the bot you just created to view credentials, copy the name and token.\
​

**Step 4:** Back in the organisation detail page, then click 'Applications' on the left-hand side menu.

![Sidebar icon labeled "Applications" with a tooltip displayed.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f9713973c4f899ea5055d6bba0640c61c55f67c0%2Fquayio-cloud-registry_8f077c3e-18f4-48bb-bfbd-f72f0e271ba2.png?alt=media)

**Step 5:** Create a new app called 'aikido'. Then click generate token on the left. Add the scope "**View all visible repositories",** then click 'Generate token', and copy the access token from the resulting screen.

![OAuth 2 Access Token permissions selection for user "aikidodev" in a repository management interface.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-59a79fb1e42f68f090753b81cea690b290b66c46%2Fquayio-cloud-registry_685fec8f-7736-475e-9ef1-a7e8000d8b00.png?alt=media)

**Step 6:** Enter the collected data in Aikido (direct link: <https://app.aikido.dev/settings/container-image-registry/add/quay>)

Copy the organization name from the top of the page in Quay.

​

**Step 7:** Aikido will now find all container repositories you can access and list them.

**Step 8:** Repositories can be linked to a code repository in order to perform better deduplication of findings. This step is optional!

**Step 9:** In the action menu next to the registry, click 'scan repos in registry' to get started. Results will appear in the Feed!

### &#x20;<a href="#set-up-quay-container-scanning" id="set-up-quay-container-scanning"></a>
