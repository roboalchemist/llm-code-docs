# Source: https://help.aikido.dev/container-image-scanning/standalone-registries/harbor-container-registry.md

# Harbor Container Registry

You can now integrate your Harbor Container Registry with Aikido, to scan your images for known vulnerabilities.

Follow the simple steps below to activate this feature:

**Step 1:** In Harbor, under Administration, then 'Robot Accounts', create a new Robot Account for Aikido that has access to the 'List repository', 'Pull Repository' and 'List Artifacts' scope. After creation, copy the secret, then the name from the table of robot accounts.

![Creating a system robot account with selected permissions for all projects.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-102ba94feccdf48b42b3ac681ba5c66b986ebe8c%2Fharbor-container-registry_034631db-6fb7-460f-8af3-57c5fa94db85.png?alt=media)

**Step 2:** Enter the collected data in Aikido (direct link: <https://app.aikido.dev/settings/container-image-registry/add/harbor>)

![Form to connect and authenticate with a Harbor container image registry.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-70da86c0734cb61b6ae74af59020f3f8bd55f5a0%2Fharbor-container-registry_22c23924-d0cf-4564-8a8c-97cc8173fcc1.png?alt=media)

**Step 3:** Aikido will now find all container repositories you can access and list them.

**Step 4:** Repositories can be linked to a code repository in order to perform better deduplication of findings. This step is optional!

**Step 5:** In the action menu next to the registry, click 'scan repos in registry' to get started. Results will appear in the Feed!

***
