# Source: https://docs.anyscale.com/container-image/build-image-tutorial.md

# Tutorial: Build a custom container image

[View Markdown](/container-image/build-image-tutorial.md)

# Tutorial: Build a custom container image

This tutorial guides you through the process of building a custom Docker image on your personal machine, such as a laptop, loading the image to a Docker Hub repository, and launching a Ray cluster on Anyscale with the image.

The tutorial provides a gentle introduction to working with custom images. Review the following to learn more about custom images:

* For a general overview of using custom images, see [Custom images on Anyscale](/container-image/custom-image.md).
* This tutorial extends an Anyscale base image, but you can also bring your own Ray image. See [Requirements for an Anyscale container image](/container-image/image-requirement.md).
* You can also extend Anyscale base images using the build farm in the Anyscale console. See [Build a custom image on Anyscale](/container-image/build-image.md).
* This tutorial uses a public Docker Hub repository. You can use private repositories such as Amazon ECR, Azure Container Registry, and Google Artifact Registry. See [Use container images from an external registry](/container-image/image-registry.md).

## Requirements[​](#requirements "Direct link to Requirements")

This tutorial depends on the following requirements outside Anyscale:

* Docker installed and configured for the terminal on your personal machine. See [Get Docker](https://docs.docker.com/get-started/get-docker/).
* A Docker account. Follow [Docker's account creation flow](https://app.docker.com/signup).
* A public Docker Hub repository. See [Create a repository](https://docs.docker.com/docker-hub/repos/create/).

## Step 1: Define a Dockerfile[​](#step-1-define-a-dockerfile "Direct link to Step 1: Define a Dockerfile")

On your personal machine, create an empty file named `Dockerfile` in your current working directory. The following command creates and opens this file:

```
touch Dockerfile
open Dockerfile
```

Copy the following example Dockerfile definition into your file and save the file:

```
# Use Anyscale base image.
FROM anyscale/ray:2.46.0-slim-py312

RUN sudo apt-get update && sudo apt-get install -y axel nfs-common zip unzip awscli && sudo apt-get clean

RUN pip install --no-cache-dir -U sympy

# (Optional) Verify that dependencies from the base image still work. This
# is useful for catching dependency conflicts at build time.
RUN echo "Testing Ray Import..." && python -c "import ray"
RUN ray --version
RUN jupyter --version
RUN anyscale --version
```

## Step 2: Construct your image reference and build the image[​](#step-2-construct-your-image-reference-and-build-the-image "Direct link to Step 2: Construct your image reference and build the image")

An *image reference* is a unique Docker identifier that is the combination of a registry, repository, and tag. The following is an example:

```
registryname/reponame:imagetag
```

Replace the variables in the following example syntax to construct your image reference, then run the command to build your image:

* `<your-registry>`: The name of your Docker Hub registry.
  <!-- -->
  * **Note**: Docker creates a registry with your username for you when you create an account.
* `<your-repository>`: The name of the target repository in your registry.
* `<your-tag>`: A tag for your image.

note

The following code example includes the `--platform linux/amd64` flag. This is the platform architecture used by many virtual machine types supported by Anyscale. You might need to specify a different platform architecture depending on the compute infrastructure you use to deploy your Anyscale cluster.

```
docker build . --platform linux/amd64 -t <your-registry>/<your-repository>:<your-tag>
```

Once your image build finishes, run the following command to see details about your image:

```
docker images
```

Example output:

```
REPOSITORY     TAG      IMAGE ID       CREATED          SIZE
test/test      test     aaa999eee888   2 minutes ago    1.1GB
```

## Step 3: Upload the image to Docker Hub registry[​](#step-3-upload-the-image-to-docker-hub-registry "Direct link to Step 3: Upload the image to Docker Hub registry")

Substitute your image reference into the following example syntax and run the command to push the image to your public Docker Hub repository:

note

The image is around 1GB. This step might take several minutes depending on your network speed.

```
docker push <your-registry>/<your-repository>:<your-tag>
```

View your [repository on Docker Hub](https://hub.docker.com/repositories) to confirm the image has uploaded successfully.

## Step 4: Create a workspace with your image[​](#step-4-create-a-workspace-with-your-image "Direct link to Step 4: Create a workspace with your image")

You can now use your image in any cluster you launch on Anyscale.

Complete the following steps to launch a new workspace using your custom image:

1. [Log in to the Anyscale console](https://console.anyscale.com/).
2. Click **Workspaces**.
3. Click **+ Create** and select **Custom blank workspace**. The **New workspace** dialog appears.
4. In the **Name** field, enter a name for the workspace.
5. In the **Select image** field, select **Use an image from an external registry**.
6. In the **Image URI** field, enter the image reference for the image you loaded to your public repository.
7. Make sure the **Ray version** field reflects the version of Ray in your image. In the example Dockerfile provided, this is version **2.46.0**.
8. Click **Create**.

You can use the **Events** output to monitor your cluster deploying. The following are example messages that report actions related to pulling your image and using it to deploy a container for a node in a Ray cluster:

```
[head] Node launched
[head] Pulling image for Ray container.
[head] Pulled image for Ray container (image size: 1.1 GB), took 11.665s.
[head] Created Ray container, took 124.920991ms.
[head] Started Ray container, took 80.046074ms.
```
