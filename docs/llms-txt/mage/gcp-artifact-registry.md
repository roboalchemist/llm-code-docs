# Source: https://docs.mage.ai/production/deploying-to-cloud/gcp/gcp-artifact-registry.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Push Docker Image to GCP Artifact Registry

While you may pull an image directly from Docker Hub, here are our legacy instructions for pushing a Docker image to GCP Artifact Registry:

1. Create a repository on
   [GCP Artifact Registry](https://console.cloud.google.com/artifacts) by
   clicking the **`+ CREATE REPOSITORY`** button.

   * Fill in the **Name**
   * Choose Docker as the **Format**
   * Choose any **Location type**
   * Choose any **Encryption**
   * Click **`CREATE`**

2. Click on the newly created repository (e.g. `mage-docker`).

3. Near the top of the page, click the link **`SETUP INSTRUCTIONS`** or read these
   [instructions](https://cloud.google.com/artifact-registry/docs/docker/authentication)
   to set up authentication for Docker.

   * Run the following command in your terminal:

     ```bash  theme={"system"}
     gcloud auth configure-docker [region]-docker.pkg.dev
     ```

   * An example command could look like this:

     ```bash  theme={"system"}
     gcloud auth configure-docker us-west2-docker.pkg.dev
     ```

4. Pull the Mage Docker image:

   ```bash  theme={"system"}
   docker pull mageai/mageai:latest
   ```

   * If your local workstation is using macOS and a silicon chip (e.g. M1, M2,
     etc), then run this command instead:

     ```bash  theme={"system"}
     docker pull --platform linux/amd64 mageai/mageai:latest
     ```

5. Tag the pulled Mage docker image or use a previously tagged Docker image you
   built when following this [CI/CD guide](/production/ci-cd):

   * Sample commands if using vanilla Mage Docker image:

     ```bash  theme={"system"}
     docker tag mageai/mageai:latest [region]-docker.pkg.dev/[project_id]/[repository]/mageai:latest
     ```

     * An example command could look like this:

       ```bash  theme={"system"}
       docker tag mageai/mageai:latest us-west2-docker.pkg.dev/materia-284023/mage-docker/mageai:latest
       ```

   * Sample commands if using previously tagged a custom Docker image using the tag `mageprod:latest`:

     ```bash  theme={"system"}
     docker tag mageprod:latest [region]-docker.pkg.dev/[project_id]/[repository]/mageai:latest
     ```

     * An example command could look like this if you previously tagged your custom Docker image with the tag `mageprod:latest`:

       ```bash  theme={"system"}
       docker tag mageprod:latest us-west2-docker.pkg.dev/materia-284023/mage-docker/mageai:latest
       ```

6. Push the local Docker image to GCP Artifact Registry:

   ```bash  theme={"system"}
   docker push [region]-docker.pkg.dev/[project_id]/[repository]/mageai:latest
   ```

   * An example command could look like this:

     ```bash  theme={"system"}
     docker push us-west2-docker.pkg.dev/materia-284023/mage-docker/mageai:latest
     ```


Built with [Mintlify](https://mintlify.com).