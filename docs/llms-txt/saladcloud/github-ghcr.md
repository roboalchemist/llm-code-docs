# Source: https://docs.salad.com/container-engine/how-to-guides/registries/github-ghcr.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# GitHub Container Registry

*Last Updated: October 15, 2024*

[GitHub Container Registry](https://ghcr.io) (GHCR) is a powerful platform for hosting and managing container images.
You can store and manage Docker in the Container registry.

### Prerequisites

Before you begin, make sure you have the following:

* A [GitHub](https://www.github.com) account
* A Docker image that you want to publish to GHCR
* Docker installed on your local machine

To deploy image from GitHub Container Registry (GHCR) to SaladCloud Portal, follow these steps:

### Step 1 : Create a [Personal Access Token ](https://docs.github.com/en/enterprise-server@3.6/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)(PAT)

1. Go to your GitHub Settings page.
2. In the left sidebar, click on "Security & admin."
3. Under "Personal access tokens," click "Generate new token."
4. Provide a descriptive name for your token and select the packages:write permission.
5. Click "Generate token" and make sure to copy the generated PAT to a safe place. You won't be able to see it again.

<img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/ghcr-get-credentials.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=1a3d967ae1d9cde70376513cb87e79bd" data-og-width="1142" width="1142" data-og-height="404" height="404" data-path="container-engine/images/ghcr-get-credentials.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/ghcr-get-credentials.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=aa33336647ea78583c0091ead3248489 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/ghcr-get-credentials.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=90c7165c1ba431b105003e5217d8cec6 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/ghcr-get-credentials.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=b6e78c940f453c16f639ccad2228909c 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/ghcr-get-credentials.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=9021aae9bc4252df8414fc5655daf1e1 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/ghcr-get-credentials.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=d96d32d9bf93d3a2f50cf10696290029 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/ghcr-get-credentials.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=29f06f4c42045e2064caf5faf781d115 2500w" />

### Step 2 : Authenticate to the Registry

You can authenticate to GHCR using either the Docker CLI or the GitHub CLI.

1. Authenticate using the Docker CLI: Open your terminal and run the following command, replacing your\_username and
   your\_PAT with your GitHub username and the PAT you generated: `docker login ghcr.io -u your_username -p your_PAT`
2. Authenticate using the GitHub CLI : If you prefer using the GitHub CLI, run this command and replace your\_PAT with
   your PAT: `gh auth login --with-token your_PAT`

### Step 3: Tag Your Docker Image

To prepare your Docker image for GHCR, you need to tag it with the appropriate name. Replace your\_image, your\_username,
your\_repo, and tag\_name with your image's name and your GitHub information:

`docker tag your_image ghcr.io/your_username/your_repo:tag_name`

### Step 4 : Push Your Image to the Registry

Now that your image is tagged correctly, you can push it to GHCR:

`docker push ghcr.io/your_username/your_repo:tag_name`

### Step 5: Configure SaladCloud Container Environment (SCE)

Access the SaladCloud portal and configure your SCE with the following information:

1. Username and Personal Access Token that we generated in the beginning.
2. Image name from your private registry.

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-ghcr.png?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=20ca06375e5f32296f9e99abe4eccd51" data-og-width="1513" width="1513" data-og-height="902" height="902" data-path="container-engine/images/configure-ghcr.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-ghcr.png?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=93d6f066e8fd36d0bc9a505bc1f02e7a 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-ghcr.png?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=608aa7230e3e4bb28c94cf6e9bd683eb 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-ghcr.png?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=9320aeaffee2f4c5a050d771ea7499e7 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-ghcr.png?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=6b04f522d9b1835345d0a2830a5ffb7f 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-ghcr.png?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=48a920e8c97afec56ba9f98ded623dd5 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-ghcr.png?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=fe0571a85c6b35c8367c2e04dc99e372 2500w" />

### Step 6 : Start the Container

With all configurations in place, click the "Start" button in the SaladCloud portal to launch your container using the
private Github registry image.

<img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/ghcr-running-group.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=5c2b1aeedee5cdc2e6c2f42e123ed899" data-og-width="1635" width="1635" data-og-height="500" height="500" data-path="container-engine/images/ghcr-running-group.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/ghcr-running-group.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=0004a1a9802a1887256555ad35d44e56 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/ghcr-running-group.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=5c7355b92efecf2dcb4fa942420d4d73 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/ghcr-running-group.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=6806cfaeac33cf2d2a29f7986593ad1a 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/ghcr-running-group.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=67881477df59860d5da46c79b5584bc7 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/ghcr-running-group.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=77e14dae1c8fc189b9acad1f44f64969 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/ghcr-running-group.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=77518e332f316a39b0e1e0a9391e471d 2500w" />

> 👍 Congratulations!
>
> Your container is now up and running, utilizing the image stored securely in your private Github container registry.
