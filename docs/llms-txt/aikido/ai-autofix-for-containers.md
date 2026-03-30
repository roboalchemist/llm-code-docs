# Source: https://help.aikido.dev/aikido-autofix/ai-autofix-for-containers.md

# AutoFix for Containers

The goal is simple: fix more, faster—with less noise. AI Autofix helps you patch container vulnerabilities in bulk by suggesting safe, reviewable Dockerfile updates.

### In Short <a href="#in-short" id="in-short"></a>

* **Base Image Updates:** When vulnerabilities are found in a container's base image, Autofix suggests update options—patch, minor, or major.
* **Multiple Patch Options**: Get 3–5 Dockerfile variants, each tied to a different base image. For each, see which vulnerabilities are fixed—and if any new ones are introduced.
* **Extended Lifecycle Support Images:** When available, AutoFix will propose an Aikido-maintained version of the base image where **HIGH** and **CRITICAL** severity issues have been remediated. [Learn more](https://help.aikido.dev/aikido-autofix/autofix-for-containers-using-hardened-images) about using ELS images.
* **Use Your Judgment**: Major updates often fix more, but may require manual changes. Choose what fits your stack best.

### Key Features of AI Autofix for Containers <a href="#key-features-of-ai-autofix-for-containers" id="key-features-of-ai-autofix-for-containers"></a>

* **Preview Changes Before You Fix:** Review detailed previews of AI-generated fixes before implementing them.
* **Create Pull Requests (PRs):** Generate pull requests directly in your Source Control Management (SCM) system

  ![Autofix preview updating nginx version to resolve critical security vulnerabilities.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c3e056e1e46a76dc06a2f1aacfae8c760b6166aa%2Fai-autofix-for-containers_ce5debd2-2d49-43bb-88c9-67d1bf113ee8.png?alt=media)

***

### Good to Know <a href="#good-to-know" id="good-to-know"></a>

* **Processing Time:** It can take up to 5 minutes for Autofix to generate suggestions, as it scans all potential base image updates for vulnerabilities.
* **Public and Private Base Images**: Container Autofix can update both public base images and private base images. The private base images need to be scanned by Aikido. Supported registries for private base images are: Docker Hub, GitHub Container Registry, AWS Elastic Container Registry, Azure Container Registry, GCP Container Registry.
* **Dockerfile Linking**: We auto-detect the Dockerfile from your repo. If there’s ambiguity, you’ll be asked to set the correct path in the UI.
* **Privacy First**: code snippets are sent securely to AWS Bedrock via encrypted channels. Neither Aikido **nor** [AWS Bedrock](https://aws.amazon.com/bedrock/security-compliance/) use your code for training or fine-tuning AI models.

### How to use the AI Autofix functionality <a href="#how-to-use-the-ai-autofix-functionality" id="how-to-use-the-ai-autofix-functionality"></a>

* **Step 1**. **Go to the** [**Container Autofix Page**](https://app.aikido.dev/issues/fix/container)[.](https://app.aikido.dev/issues/fix/sast)

  See a list of containers with the option to **Generate Preview**. If a container isn’t linked to a repo, or if the Dockerfile path is unclear, you’ll be prompted to configure it manually.

  ![Dashboard showing critical security issues in container images and options to generate autofix previews.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-7f47661f291d6d8f8a44b261d32b358ae23006bc%2Fai-autofix-for-containers_fbe60ffd-b48c-45a7-8e0a-31af9461a33d.png?alt=media)
* **Step 2.** **Review and Select a Patch Option**

  Each option shows what it fixes and if it introduces new issues. Pick the one that fits your setup.

  ![Security update preview for nginx-web Dockerfile, showing resolved vulnerabilities and suggested version upgrade.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-093718bad4ded25427a76ab6b871ced55fe5f755%2Fai-autofix-for-containers_c4fbd328-59c8-47e7-9a1b-56ebb61cafc9.png?alt=media)
* **Step 3. Create PR**

  Autofix generates a pull request directly in your SCM with the updated Dockerfile.

***
