# Source: https://help.aikido.dev/container-image-scanning/standalone-registries/cloudsmith-container-registry.md

# Cloudsmith Container Registry

You can integrate your Cloudsmith's Container Registry with Aikido, to scan your images for known vulnerabilities.

Follow the simple steps below to activate this feature:

**Step 1:** Log into your Cloudsmith account. And navigate to API Settings.

See screenshot below.

We'll have to gather an API Key. Direct URL: <https://cloudsmith.io/user/settings/api/>

![User account dropdown menu displaying settings, documentation links, and logout option.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-65a7cae7d814f681400f14ed57c1061a53f705da%2Fcloudsmith-container-registry_bb3a1b86-d787-4566-8712-e3ff29a8f9ed.png?alt=media)

You can copy the API key directly from this screen:

![API key management and restriction settings for Cloudsmith account integration and security.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2c9dd9376767e4d6f1509b84ea54b965e021412b%2Fcloudsmith-container-registry_bd01d550-c677-423f-9ebd-e9260b2833a2.png?alt=media)

**Step 2:** Enter the collected data in Aikido (direct link: <https://app.aikido.dev/settings/container-image-registry/add/cloudsmith>)

![Form to connect and authenticate a Cloudsmith container image registry account.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8d0f49570ab6edb33d118836a7c6963dc858e768%2Fcloudsmith-container-registry_794eaef4-1fac-4a30-a710-c00889f12a8f.png?alt=media)

* **Username** can be found in your user account on top (see first screenshot above)
* **Organization Namespace** can be found here:

![Organization membership management dashboard showing user role and organization options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d1abec25bef33db1635fbd4a293df3c2c92c3fab%2Fcloudsmith-container-registry_9043f1ca-03bc-472a-a2b9-51763d085696.png?alt=media)

**Step 3:** Aikido will now find all container repositories you can access and list them.

**Step 4:** Repositories can be linked to a code repository in order to perform better deduplication of findings. This step is optional!

**Step 5:** In the action menu next to the registry, click 'scan repos in registry' to get started. Results will appear in the Feed!

***
