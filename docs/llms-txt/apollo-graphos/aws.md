# Source: https://www.apollographql.com/docs/graphos/routing/self-hosted/containerization/aws.md

# Deploying GraphOS Router on AWS

Learn how to deploy the router for development on AWS with Elastic Container Service (ECS).

You will:

* Build a router image with a Dockerfile.
* Set up an Elastic Cloud Registry and push your router image to it.
* Create an ECS task definition for your router and deploy it.

If your organization uses a corporate proxy with TLS inspection, [add your proxy's root certificate to the container](https://www.apollographql.com/docs/graphos/routing/self-hosted/containerization/proxy-certificates).

## Prerequisites

Before you start:

1. [Set up a GraphQL API in GraphOS](https://www.apollographql.com/docs/graphos/get-started/guides/graphql#step-1-set-up-your-graphql-api).
   * Save your `APOLLO_KEY` and `APOLLO_GRAPH_REF`. You'll need them when deploying the router.
2. Install [Docker](https://www.docker.com/get-started/) locally.
3. Set up your [AWS environment](https://aws.amazon.com/getting-started/guides/setup-environment/)
   * Install the AWS CLI.
   * Use an existing Create an Amazon
4. Choose a version of the router to deploy (for example, `v1.61.0`). You'll need it when specifying the router image to deploy.

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

3. From the same local directory, run the following `docker` CLI command to build a new router image. Choose a name and tag for the image, for example `router-aws:v1.61.0`.

   ```bash
   docker buildx build --platform linux/amd64  -t router-aws:v1.61.0 --load .
   ```

   * Because Cloud Run only supports AMD64-based images, the `docker buildx build --platform linux/amd64` command ensures the image is built for AMD64 and is compatible.
   * The `--load` option loads the built image to `docker images`.

4. Run `docker images` and validate that your router image is in the returned list of images.

## Push router image to registry

Now that you have a built router image, create a repository in Elastic Cloud Registry (ECR) and push your image to it:

1. In a local terminal, run the AWS CLI command to create a new ECR repository:

   * For `--repository-name`, set a name for your repository (for example, `router-repo`)
   * For `--region`, set your AWS region (for example, `us-west-1`)

   ```bash
   aws ecr create-repository \
       --repository-name router-repo \
       --region us-west-1
   ```

2. In AWS CLI, authenticate your Docker CLI to ECR.

   * For `--region`, use your AWS regions (for example, `us-west-1`)
   * Use your ECR repository URI, which you can copy from your ECR Repositories Console (for example, `0123456789000.dkr.ecr.us-west-1.amazonaws.com`)

   ```bash
   aws ecr get-login-password --region us-west-1 | docker login --username AWS --password-stdin 0123456789000.dkr.ecr.us-west-1.amazonaws.com
   ```

   > To troubleshoot ECR authentication, go to [AWS documentation](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html#cli-authenticate-registry).

3. Run `docker tag` to tag the image before pushing it to ECR.

   ```bash
   docker tag router-aws:v1.61.0 0123456789000.dkr.ecr.us-west-1.amazonaws.com/router-repo:v1.61.0
   ```

4. Run `docker push` to push the router image to your ECR repository URI, using a tag (e.g., `:v1.61.0`):

   ```bash
   docker push 0123456789000.dkr.ecr.us-west-1.amazonaws.com/router-repo:v1.61.0
   ```

5. Run `aws ecr list-images` and validate that your image is in the list of images in your ECR repository:

   ```bash
   aws ecr list-images --repository-name router-repo
   ```

## Create and deploy ECS task

With your image pushed to your ECR repository, in ECS you can define a task for the router and deploy it as a service.

### Create cluster

You need an ECS cluster to deploy the router.

If you don't have a cluster, you can create one with default settings:

1. In the AWS Console, go to the Amazon ECS Console, then click **Create cluster**.
2. Enter a name for your cluster.
3. Click **Create**.

### Create task definition

Create an ECS task definition for your router:

1. In the AWS ECS Console, go to **Task definitions** from the left navigation panel, then click **Create new task definition** and select **Create new task definition**.
2. Fill in the details for **Container - 1**:
   * **Name**: Enter a container name
   * **Image URI**: Select the URI of your router image
   * **Port mappings**:
     * **Container port**: Enter `4000` (must match ) and
     * **Port name**: Enter a port name
   * **Environment variables**: Enter the environment variables `APOLLO_KEY` and `APOLLO_GRAPH_REF` and set them to your graph API key and graph ref, respectively
3. In `Docker configuration - optional`, enter the command options to configure the router and run it in development mode:

   ```text
   --dev, --config, /dist/config/router.yaml
   ```
4. Click **Create**.

### Deploy router

Deploy the router in your ECS cluster:

1. In AWS ECS Console under **Task definitions**, select your defined task, then click **Deploy** and select **Create service**.
2. Fill in  the fields for the service:
   * **Existing cluster**: Select your cluster
   * **Service name**: Enter a name for your service
3. Click **Create** to create the service. ECS will start deploying the service for the router.
4. After AWS finishes deploying, click on the service to go to its page in Console. Check the service logs for messages from the running router. For example:

   ```text title=Example router log message
   {"timestamp":"2025-04-04T17:32:14.928608731Z","level":"INFO","message":"Apollo Router v1.61.0 // (c) Apollo Graph, Inc. // Licensed as ELv2 (https://go.apollo.dev/elv2)","target":"apollo_router::executable","resource":{}}
   ```
5. Go to the service URL and validate the the router's development Sandbox is running successfully.

Congrats, you've successfully deployed the router!
