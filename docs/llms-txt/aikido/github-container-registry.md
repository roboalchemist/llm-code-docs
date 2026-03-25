# Source: https://help.aikido.dev/container-image-scanning/standalone-registries/github-container-registry.md

# GitHub Container Registry

You can integrate your Github Container Registry with Aikido to scan your containers for known vulnerabilities.

Follow the simple steps below to activate this feature:

**Step 1:** Log into your Github account to gather some data.

We'll have to gather your username (see screenshot)

![GitHub user profile overview with avatar, username, followers, and edit profile option.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-cc408cfbbf44b0b5c5c09da9c6e7c57449236680%2Fgithub-container-registry_bcdcbd95-3e97-4fa5-823a-23e54cc5005d.png?alt=media)

**Step 2:** Copy the organisation name where the container registry resides. This is visible in the github-url (see screenshot)

![URL input field displaying "https://github.com/Organization" for organization link entry.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-af9f2365771e2c1efe8082580f71f0cae4c8187b%2Fgithub-container-registry_42637ec3-0ed2-4016-9418-29470dee6e88.png?alt=media)

**Step 3:** Under profile settings, developer settings, Personal access tokens, Tokens (classic), generate a new classic token for Aikido

(direct link: <https://github.com/settings/tokens>).

the scope includes: `read:packages`

![GitHub token creation: No expiration, read package access scope selected.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f68a2fb2764e2063948e7b9d08208a3ab5019940%2Fgithub-container-registry_65b9dd8b-d552-46cc-b265-c9e0da804f01.png?alt=media)

**Step 4:** Enter the collected data in Aikido (direct link: <https://app.aikido.dev/settings/container-image-registry/add/github>)

![Form to connect and authenticate a Github container image registry.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-21a7b25240b1788ccdd53ef81e4ac97c0f194fcd%2Fgithub-container-registry_1030004f-c2f0-436e-9e0b-e1af4dbaa814.png?alt=media)

**Step 5:** Aikido will now find all container repositories you can access and list them.

**Step 6:** Repositories can be linked to a code repository in order to perform better deduplication of findings. This step is optional!

**Step 7:** In the action menu next to the registry, click 'scan repos in registry' to get started. Results will appear in the Feed!

### &#x20;<a href="#set-up-github-container-registry-scanning" id="set-up-github-container-registry-scanning"></a>
