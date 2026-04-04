# Source: https://help.aikido.dev/container-image-scanning/configuration/link-repository-to-container.md

# Manually Link Repository to Container

Linking your container images to their corresponding code repositories centralizes related vulnerabilities, so you can view, triage, and fix them in the right context. Once linked:

* Container issues will appear directly within the relevant repo.
* You'll unlock Container Autofix, which updates Dockerfiles automatically with available fixes.

#### Ways to Link Containers

You can link containers to repositories in two ways:

* **Manual Linking** – Link specific repos to containers one by one.
* **Smart Suggestions** – Automatically link multiple containers using intelligent repo suggestions. [Learn more here →](https://help.aikido.dev/container-image-scanning/configuration/container-autolink)

## Manually link a repository to a container <a href="#how-to-link-a-repository-to-a-container" id="how-to-link-a-repository-to-a-container"></a>

**Step 1**: Navigate to [Settings > Containers](https://app.aikido.dev/settings/container-image-registry) via the top right corner of the Aikido interface.

**Step 2:** Click the 🔗 **Link** button next to the container you want to connect.\
Use the search bar to find and select the correct repository.

![Docker image "openscurity/mobsfscan:latest" prompts to link an unlinked code repository.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-520e5795256974fbed54be26a54c368ffdc2bb90%2Flink-repository-to-container_74ab9881-0f6d-4c05-a475-281c18baaaa3.png?alt=media)

![Dialog for linking a cloud image to the "Spoon-Knife" code repository.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-fb2c0e505b35b3c7373953e1a79676c89d63a89b%2Flink-repository-to-container_49a82ebf-5f16-4aa5-8044-fc7036e1c3e0.png?alt=media)

**Step 3**: To see all repositories linked to a container, go to in [Settings > Containers](https://app.aikido.dev/settings/container-image-registry). Use the `⋮` **three-dot menu** next to any linked repo to unlink it.
