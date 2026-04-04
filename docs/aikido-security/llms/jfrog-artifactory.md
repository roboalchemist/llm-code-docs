# Source: https://help.aikido.dev/container-image-scanning/standalone-registries/jfrog-artifactory.md

# JFrog Artifactory

You can integrate your JFrog Artifactory with Aikido to scan your images for known vulnerabilities.

Follow the simple steps below to activate this feature:

**Step 1:** In JFrog , we have to collect some data including your username and a JWT access token. The username is the value displayed in the Users table. To start, click 'User Management' on the top right.

![Platform configuration menu with options for projects, user management, and security settings.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5d726e52f657df9010bf56a63a9402576feef33f%2Fjfrog-artifactory_60292b5b-d3ea-419e-bd9a-de1ae813979d.png?alt=media)

Then, click 'Access Tokens' on the left menu:

![Platform configurations sidebar showing user management and security access token options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-b1fcd6ac811f5a9540bb822bfd89d6c280e6d0d0%2Fjfrog-artifactory_b129e49d-ddcd-4d3c-91a0-e8a6985bb250.png?alt=media)

In the top-right corner, click 'Generate token' and fill out the settings as below:

![Generate Token window for creating a scoped user access token with custom settings.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-011098d9408932743934710b19e384e20cfdc0c1%2Fjfrog-artifactory_4b6a8174-27ee-4951-b337-d07c26e15f32.png?alt=media)

**Step 2:** Enter the collected data in Aikido (direct link: <https://app.aikido.dev/settings/container-image-registry/add/artifactory>)

![Form for connecting to JFrog Artifactory container image registry using credentials and URL.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9328ba35290019de7993ee30972daffe5909d326%2Fjfrog-artifactory_8e0d84ce-752d-41b6-9d68-7767d65d4f2d.png?alt=media)

**Step 3:** Aikido will now find all container repositories you can access and list them.

**Step 4:** Repositories can be linked to a code repository in order to perform better deduplication of findings. This step is optional!

**Step 5:** In the action menu next to the registry, click 'scan repos in registry' to get started. Results will appear in the Feed!

***
