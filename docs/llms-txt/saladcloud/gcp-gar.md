# Source: https://docs.salad.com/container-engine/how-to-guides/registries/gcp-gar.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Artifact Registry

*Last Updated: November 22, 2024*

Service accounts are used by applications to make authorized APIs calls on the Google Cloud Platform (GCP). In order for
the SaladCloud portal to interact with GCP through APIs, a JSON key for a service account is required.

### Step 1: Generate a Google Cloud Platform JSON Key

1. Start by logging in to your Google Cloud Platform (GCP) account.
2. Access the GCP [Console home page](https://console.cloud.google.com), Click on 'Go to project settings' to proceed.
3. On the left navigation bar, find and select the 'Service Accounts' menu.
4. Choose 'Create Service Account' to initiate the process.
5. Provide a name and description for the service account, grant it `Artifact Registry Reader` access to your project,
   and proceed to create the account. *(Note: Most read/write permissions should work, except Basic - Browser which does
   **NOT** work)*
6. Select the newly created service account, and navigate to the 'KEYS' tab.
7. From the 'ADD KEY' dropdown, opt for 'Create New Key' and select JSON as the key type. Your service account key JSON
   file will be automatically downloaded to your local machine.

### Step 2: Configure SaladCloud Container Environment (SCE)

Access the SaladCloud portal, Set up your SCE by selecting the private registry tab when setting the image source. In
the service dropdown option, choose "Google Artifact Registry" and provide the following information:

* Image name (example: `us-central1-docker.pkg.dev/{my-project}/{my-registry}/{my-container-image}:{version/latest}`)
* JSON Key (generated or downloaded in step 1)

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-gar.png?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=e069309226d960b26fc08cf1693b453a" data-og-width="560" width="560" data-og-height="1215" height="1215" data-path="container-engine/images/configure-gar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-gar.png?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=264868af7a4cee8ff5c0a24f418f08a8 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-gar.png?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=2f03315885d55b5e353e6b2e22473052 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-gar.png?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=f5c5614c3b4a43e465a4ed3ee2f78cbe 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-gar.png?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=f82f0e5d729e7dc0f2b9ca84242ef7a4 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-gar.png?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=5543509183dadeb0309db7e4150b41c7 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-gar.png?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=ce6dc417381c25387ed8e84babc83ef0 2500w" />

> 👍 Congratulations!
>
> You have successfully configured the private container registry using Google Artifact Registry. Now, you can proceed
> to configure and deploy your container group.
