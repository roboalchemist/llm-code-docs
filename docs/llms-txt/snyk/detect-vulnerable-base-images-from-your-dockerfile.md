# Source: https://docs.snyk.io/scan-with-snyk/snyk-container/scan-your-dockerfile/detect-vulnerable-base-images-from-your-dockerfile.md

# Detect vulnerable base images from your Dockerfile

{% hint style="info" %}
You can add a single Dockerfile to each image that you have imported.
{% endhint %}

## **Prerequisites for adding a Dockerfile**

To receive base image fix advice, including major, minor, and alternative upgrades, as well as advice when you need to rebuild your image, ensure you:

* Have configured your preferred Git repository
* Have imported the repository that contains the relevant Dockerfile.

## **Add a Dockerfile**

To add a Dockerfile for additional fix advice:

1. In the **Projects** tab, find your Project by using a filter and navigate to the Project page.
2. On the Project page, navigate to **Settings**.
3. On the **Settings** page, under **Dockerfile**, click **Configure Dockerfile** and select the relevant Git repository from the dropdown.

<div align="left"><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-d90cb8f01bff2133c699d553ead3e0c9870f0ad7%2Fconfigure_dockerfile.png?alt=media" alt="Configure your Dockerfile by selecting the relevant repository."><figcaption><p>Configure Dockerfile</p></figcaption></figure></div>

4. On the page listing the available repositories, select the relevant repository which contains your Dockerfile.
5. Under **Path to your Dockerfile**, add the relative path to your Dockerfile, in the following format: /path/dockerfile.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-723b85733fc5d1ee5a748a7abd1ef749b6c96b5b%2Fpath_to_docker_file_update.png?alt=media" alt="Enter the path to your Dockerfile"><figcaption><p>Add the path to your Dockerfile</p></figcaption></figure>

6. Click **Update your Dockerfile**.

Snyk scans the Project again and provides relevant base image fix advice. You can see the fix advice on the Project page, under **Recommendations for upgrading the base image.**

The following information is displayed: **Current image**, **Minor upgrades**, **Major Upgrades**, **Alternative upgrades**, the number of vulnerabilities for each, and a severity ranking.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1982ab62e1ab7427ac53cac0f50d89489933439d%2Frecommendations_base_image.png?alt=media" alt="Recommendations for base image upgrade"><figcaption><p>Recommendations for upgrading the base image</p></figcaption></figure>

## Scan the base image from a Dockerfile

Snyk detects vulnerable base images by scanning your Dockerfile when you import a Git repository. This allows you to examine security issues before building the image and thus helps solve potential problems before they land in your registry or in production.

{% hint style="info" %}
When scanning Dockerfiles, Snyk can provide vulnerability information and base image recommendations for supported base images. If you need help, contact [Snyk Support](https://support.snyk.io).
{% endhint %}

After you [integrate your Git repository with Snyk](https://docs.snyk.io/developer-tools/scm-integrations/organization-level-integrations), any Dockerfiles in that repository are automatically identified and shown in the Web UI as Projects.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-35a28641375c6cf937bccae01c8309736fa3b3d3%2Fdockerfiles_projects.png?alt=media" alt=""><figcaption><p>Dockerfiles displayed in the Project list</p></figcaption></figure>

For details about detecting vulnerable base images in containers and fix recommendations, see [Detect the container base image](https://docs.snyk.io/scan-with-snyk/snyk-container/use-snyk-container/detect-the-container-base-image).
