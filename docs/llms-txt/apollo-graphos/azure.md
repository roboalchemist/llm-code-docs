# Source: https://www.apollographql.com/docs/graphos/routing/self-hosted/containerization/azure.md

# Deploying GraphOS Router on Azure

Learn how to deploy the router for development on Azure as a Container App.

You will:

* Build a router image with a Dockerfile.
* Set up an Azure Container Registry and push your router image to it.
* Create and deploy an Azure Container App for your router.

If your organization uses a corporate proxy with TLS inspection, [add your proxy's root certificate to the container](https://www.apollographql.com/docs/graphos/routing/self-hosted/containerization/proxy-certificates).

## Prerequisites

Before you start:

1. [Set up a GraphQL API in GraphOS](https://www.apollographql.com/docs/graphos/get-started/guides/graphql#step-1-set-up-your-graphql-api).
   * Save your `APOLLO_KEY` and `APOLLO_GRAPH_REF`. You'll need them when deploying the router.
2. Install [Docker](https://www.docker.com/get-started/) locally.
3. Login to or create an [Azure account](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account).
4. Install [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).
5. Choose a version of the router to deploy (for example, `v1.61.0`). You'll need it when specifying the router image to deploy.

## Build router image

To deploy your own router, start by customizing and building a router image, using a Dockerfile and a router configuration file:

1. In a local directory, create a `router.yaml` file and copy-paste the following configuration into the file:

   ```yaml title=router.yaml
   supergraph:
       listen: 0.0.0.0:4000
   health_check:
       listen: 0.0.0.0:8088
   ```

   The router's default HTTP and health check endpoint addresses are localhost, so they wouldn't be reachable when deployed. This configuration enables the router to listen to all addresses.

2. Create a `Dockerfile` file and copy-paste the following into the file:

   ```text
   # Use the official Apollo Router Core image as the base.
   # Set the image tag to the desired router version (e.g. v1.61.0)
   FROM ghcr.io/apollographql/router:v1.61.0

   # Replace the default router config with the local, customized router.yaml
   COPY router.yaml /dist/config/router.yaml
   ```

   The Dockerfile sources the base router image from the GitHub container registry, using the version of router you specify. It then copies your customized `router.yaml` configuration file to overwrite the default router configuration file.

3. From the same local directory, use `docker buildx build` to build a new router image for a specific platform. Choose a name and tag for the image, for example `router:v1.61.0`.

   ```bash
   docker buildx build --platform linux/amd64  -t router:v1.61.0 --load .
   ```

   * The `--load` option loads the built image to `docker images`.

4. Run `docker images` and validate that your router image is in the returned list of images.

## Push router image to container registry

Create an Azure Container Registry as needed, then push your router image to it.

### Create new container registry

If you don't have an existing container registry, create a new one:

1. Log in to the Azure Portal and go to [Container registries](https://portal.azure.com/?quickstart=true#browse/Microsoft.ContainerRegistry%2Fregistries).

2. Click **Create container registry**.

3. Fill in the details:
   * **Subscription**: Select your subscription
   * **Resource group**: Select existing group or create new
   * **Registry name**: Enter a unique name for your registry (for example, `myapolloregistry`)
   * **Location**: Select an appropriate region
   * **Pricing plan**: Select an appropriate plan

4. Click **Review + create**, then click **Create**.

5. Your registry should now be created. Click on your registry to go to its portal page.

### Log in to container registry

1. In a terminal, sign in to Azure CLI:

   ```bash
   az login
   ```

2. Log in and authenticate to your registry (for example, `myapolloregistry`):

   ```bash
   az acr login --name myapolloregistry
   ```

### Tag and push image to registry

1. Use `docker tag` to create an alias of the image with the fully qualified path to your registry (for example, `myapolloregistry.azurecr.io`):

   ```bash
   docker tag router:v1.61.0 myapolloregistry.azurecr.io/router:v1.61.0
   ```

2. Push the image to the registry:

   ```bash
   docker push myapolloregistry.azurecr.io/router:v1.61.0
   ```

3. Use `az acr repository list` to verify your image is now in the registry:

   ```bash
   az acr repository list --name myapolloregistry
   ```

```bash
[
  "myapolloregistry"
]
```

### Deploy the router

Create and deploy a container app to run the router in Azure:

1. Log in to the Azure Portal, then go to [Create Container App](https://portal.azure.com/#create/Microsoft.ContainerApp)

2. Fill in the details for the **Basics** tab:
   * Subscription: Select your subscription
   * Resource Group: Select existing group or create new
   * Name: Enter a unique name for your web app.
   * Publish: Choose **Container**
   * Operating System: Choose **Linux**
   * Region: Select an appropriate region
   * App Service Plan: Select existing plan or create new

3. Fill in the details for the **Container** tab:
   * **Subscription**: Select your subscription
   * **Registry**: Select your registry
   * **Image**: Select your router image
   * **Image tag**: Select your router image's tag
   * **Arguments override**: Enter `--dev, --config, /dist/config/router.yaml`
   * **Environment variables**: Enter `APOLLO_GRAPH_REF` and `APOLLO_KEY` with your graph ref and API key, respectively

4. Fill in the details for the **Ingress** tab:
   * **Ingress**: Check **Enabled**
   * **Ingress traffic**: Select **Accepting traffic from anywhere**
   * **Ingress type**: Select **HTTP**
   * **Target port**: Enter `4000` (must match your router's `supergraph.listen` port)

5. Click **Review + create**.

6. Click **Create**, then wait for your deployment to complete.

7. Click **Go to resource** to open the portal page for your deployed container, then click on the **Application Url** to verify that your router's Sandbox is running successfully.

Congrats, you've successfully deployed the router!
