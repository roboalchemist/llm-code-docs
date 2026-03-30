# Source: https://docs.salad.com/container-engine/how-to-guides/registries/dockerhub.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dockerhub

*Last Updated: October 15, 2024*

Dockerhub Private Registry is a secure platform for hosting and managing container images. With this registry, you can
store and manage Docker images while keeping them private. This guide will walk you through the process of deploying
containers from Dockerhub Private Registry to the SaladCloud Portal.

### Step 1: Generate a Dockerhub Access Token

1. Begin by signing in to your
   [Docker Hub account](https://hub.docker.com/?_gl=1*1wtacu5*_ga*MTQ4MTE2NjExNC4xNjk0ODY0OTAy*_ga_XJWPQMJYHQ*MTY5NzgwNjc1MC41LjEuMTY5NzgwNzUzOC41OC4wLjA.).
2. In the top-right corner, locate and click on your username. From the drop-down menu, select "Account Settings."
3. In Account Settings, navigate to the "Security" tab.
4. Within the Security tab, find the option to create a "New Access Token."
5. Provide a description for your token that clearly indicates its use case or purpose.
6. Next, configure the access permissions. These permissions are essentially scopes that define restrictions within your
   repositories. For instance, with "Read & Write" permissions, an automation pipeline can build an image and push it to
   a repository but cannot delete the repository.
7. After configuring the token, select "Generate." Copy the token that appears on the screen and be sure to save it in a
   secure location. It's important to note that once you close this prompt, you won't be able to retrieve the token
   again.

For detail information, please follow official documentation
to[ Generate A Dockerhub Access Token](https://docs.docker.com/security/for-developers/access-tokens/).

### Step 2: Configure SaladCloud Container Environment (SCE)

Access the SaladCloud portal, Set up your SCE by selecting the private registry tab when setting the image source. In
the service dropdown option, choose "Docker Hub" and provide the following information:

* Image name (example: `docker.io/{username}/{my-container-image}:{version/latest}`)
* Username and Personal Access Token(PAT).

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-dockerhub.png?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=4ed98e9eb26877ac3a727d2da50b9ccb" data-og-width="1835" width="1835" data-og-height="937" height="937" data-path="container-engine/images/configure-dockerhub.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-dockerhub.png?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=21fbb2f43c00bd8a15c9650d2d4d24f8 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-dockerhub.png?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=7637676a91e8675a5b92570e062c9f2b 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-dockerhub.png?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=76c785add37f421973be2d296a1d3544 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-dockerhub.png?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=2b3edfc48783f64dbbd8c25f1a248d7d 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-dockerhub.png?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=697f4b2dedefe8c252c2c5dbfd83e75b 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/configure-dockerhub.png?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=a50f963328f3f3ce7cfde3e6a145c058 2500w" />

> 👍 Congratulations!
>
> You have successfully configured the private container registry using Docker Hub. Now, you can proceed to configure
> and deploy your container group.
