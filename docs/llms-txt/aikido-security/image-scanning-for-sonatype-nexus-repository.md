# Source: https://help.aikido.dev/container-image-scanning/standalone-registries/image-scanning-for-sonatype-nexus-repository.md

# Image scanning for Sonatype Nexus Repository

You can connect your Sonatype Nexus Repository with Aikido to scan your containers for known vulnerabilities.

Follow the simple steps below to activate this feature:

**Step 1**: Log into your Sonatype Nexus Repository. We'll have to gather the instance url, the registry name and credentials

The **instance url** is the url that you need to access your Sonatype Nexus Repository. This includes `http(s)://` and the port of your instance. For example: `https://my-awesome-nexus-repository.com:8081`

The **registry name** is the name of the hosted docker repository of which we should scan your images. This can be found when browsing your repositories.

![Asset browser interface displaying repository names, types, formats, and online statuses.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9d3d659eedcc1b234fcb3b65b44dc43ee42e7b1e%2Fimage-scanning-for-sonatype-nexus-repository_4cb12899-8114-4d1a-aae8-7159b9735410.png?alt=media)

In this example the name of the registry is *docker-hosted*

The **credentials** can be either User tokens (recommended) or User credentials.

Go to your profile in the upper-right corner

![Admin profile section with a "Sign out" button.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-7d82c5a1ef2c2cb209f07527bb2045e77df90c48%2Fimage-scanning-for-sonatype-nexus-repository_7c62ac69-abed-4c00-9052-647cac37db8b.png?alt=media)

In the left sidebar, click User token. Then click the "Access user token"-button

![User Token management interface for generating or resetting Sonatype Nexus Repository tokens.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8ec310abe2df11c531b4e3e16243c79d7eed0531%2Fimage-scanning-for-sonatype-nexus-repository_3d027f49-9f83-4f4e-b8bb-06e2e63fe3c3.png?alt=media)

Authenticate and get the **user token name code** and the **user token pass code** from the modal

![User token code display with clipboard copy and security warning.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-30bdef19c4f3a106fbfc7590b400dc8da4c24042%2Fimage-scanning-for-sonatype-nexus-repository_bfa51fb6-1df1-4f64-8c67-284250f89dd1.png?alt=media)

![User token pass code display with copy to clipboard options for secure access.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-72c62de9e5de6d6c6b69ce9442bac02dfd560955%2Fimage-scanning-for-sonatype-nexus-repository_a4448113-72d4-418c-8c74-5bb425a978fc.png?alt=media)

**Note:** When User tokens are not enabled in your Sonatype Nexus Repository, you can also use your login credentials. We do not recommend this since using user tokens are generally safer and easier to reset.

**Step 2**: Enter the collected data into the matching fields and click save

![Form to connect and configure a Sonatype Nexus container image registry.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-14ce49570dec6aa60bb1e3c2be2044045dd849fc%2Fimage-scanning-for-sonatype-nexus-repository_289cbcc3-0f71-4e08-97a0-30a4d97aaa0a.png?alt=media)

**Step 3:** Aikido will now find all container repositories you can access and list them.

**Step 4:** Repositories can be linked to a code repository in order to perform better deduplication of findings. This step is optional!

**Step 5:** In the action menu next to the registry, click 'scan repos in registry' to get started. Results will appear in the Feed!
