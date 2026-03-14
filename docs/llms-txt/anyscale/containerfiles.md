# Source: https://docs.anyscale.com/dependency-management/containerfiles.md

# Iterate on workspace container images

[View Markdown](/dependency-management/containerfiles.md)

# Iterate on workspace container images

You can use containerfile syntax to iteratively edit and build container images while developing in an Anyscale workspace.

info

This feature is a beta release. It's only available for workspaces backed by virtual machines.

The following is a high-level flow for how to use this feature:

1. Launch an Anyscale workspace using any container image.
2. Use Anyscale console features and containerfile syntax to extend the image.
3. Apply the changes to build a new container image.
4. Restart the workspace using the new container image.

You can continue to iterate on the containerfile definition and build new images, automatically restarting the workspace cluster to apply changes after each build. If the containerfile syntax is invalid, the build fails and the cluster doesn't restart.

Use this feature if you feel comfortable working with containerfile syntax or need to add simple dependencies that aren't possible with runtime environment features, such as system packages. See [Define a custom image for Anyscale](/container-image/build-image.md#syntax).

important

This image build process takes place in the customer data plane and has access permissions configured in your Anyscale cloud. Images built through this flow are only available in the workspace where the image builds.

This differs from the standard Anyscale tools for building custom images, where images build in the Anyscale control plane and are available to all users and clouds in an organization.

## Modify and apply changes to a workspace container image[​](#modify-and-apply-changes-to-a-workspace-container-image "Direct link to Modify and apply changes to a workspace container image")

You must have a running workspace to edit containerfiles, as Anyscale uses the workspace compute to build the new image.

Complete the following steps to edit a containerfile, build an image, and relaunch your workspace:

1. [Log in to the Anyscale console](https://console.anyscale.com/).

2. Click **Workspaces**.

3. Click the name of the workspace you want to modify.

4. If the workspace isn't running, click **Start**.

5. Click **Dependencies**.

6. Under **Container image**, click **Build custom image**. The containerfile appears in a hosted text editor.

7. To change the base image, click the edit icon ![Edit icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAUCAYAAACAl21KAAABU2lDQ1BJQ0MgUHJvZmlsZQAAGJVtkD0sQ2EUhp9WpZQIYTR0EH8pkdJgrA4iQZqi/qbb26ombd3cXhGJTSIWIxOLwWyrUcRELAiJ3WCSkHShrnNbtMVJ3pwnb97vy5sDdhRNSzqAVNrQQ6Mj7rn5BbfzCSc2amlmSFEzmj8YHJcI37tycneSlbnpsf46POjYfd4JP17WvFwsnnW7/uYrxhWNZVTZ76J2VdMNsLUJB9cMzWIRLbqUEt62OF7kfYsjRT4uZKZDAeFz4UZ1WYkK3wp7ImV+vIxTyVX1q4PVvj6Wnpmy+ohaCTOJl0GG5S7/5wYKuQAraKyjkyDOMgZu/OJoJIkJj5FGpRePsJc+kc+67++7lbzEFvhE9uuSF72Ckw2pPFHyOjeh6QNOGzRFV36uacs5Mkv93iLXZaF6zzRfZ8HZBfl703zLmmb+CKoe5G3uE9a9YtwqEWfPAAAARGVYSWZNTQAqAAAACAACARIAAwAAAAEAAQAAh2kABAAAAAEAAAAmAAAAAAACoAIABAAAAAEAAAASoAMABAAAAAEAAAAUAAAAAN+Z0lsAAAICaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA2LjAuMCI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIgogICAgICAgICAgICB4bWxuczpleGlmPSJodHRwOi8vbnMuYWRvYmUuY29tL2V4aWYvMS4wLyI+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDxleGlmOlBpeGVsWERpbWVuc2lvbj4xODwvZXhpZjpQaXhlbFhEaW1lbnNpb24+CiAgICAgICAgIDxleGlmOlBpeGVsWURpbWVuc2lvbj4yMDwvZXhpZjpQaXhlbFlEaW1lbnNpb24+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgo46BEmAAAAxUlEQVQ4Ea3Uiw2EIAwG4Hq5SWAWZmElmIVZYJU7f5ISwGp9NVFB6icvXX5r0AvxuWKUUnbTT0MpJQohUIxRxE5BQHBYaynnLGIqxIhzjrz3hKuEHUI9AgDB82SMGYa4C0kI5ge9AcowayJ0FQG2ge4gG+guMkBPkAY9RRqEAgIbDnG0OjVBOH37e+gZYm+J+9y5PEAAENI+mR+c68tbv5HaI2x77s38Jq2OecXnUiEgPD/ag1I7oDY0/hilRO3eAGnJWvsfEn+dcYp+Fp8AAAAASUVORK5CYII=).

   <!-- -->

   * Select an image from the drop down.
   * Click **Apply**.

8. Edit the containerfile using standard Dockerfile syntax.
   <!-- -->
   * For a list of supported syntax, see [Define a custom image for Anyscale](/container-image/build-image.md#syntax).

9. Click **Build image**. The **Build and apply the image?** dialog appears.

10. Click **Build and apply**.

The **Container image build logs** display the build status. When complete, a dialog appears telling you the workspace is restarting to use the new image.

note

The container image now displays as **Built from containerfile**. Click **Edit containerfile** to modify the containerfile and rebuild the workspace container image.

### Example containerfile syntax[​](#example-containerfile-syntax "Direct link to Example containerfile syntax")

The following is an example containerfile definition that installs uv, vLLM, and FFmpeg:

```
FROM anyscale/ray:2.47.1-slim-py312-cu128

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

RUN sudo apt-get update -y \
  && sudo apt-get install --no-install-recommends -y ffmpeg \
  && sudo rm -f /etc/apt/sources.list.d/*

RUN uv pip install --system vllm
```

## Interact with the working directory in your containerfile[​](#interact-with-the-working-directory-in-your-containerfile "Direct link to Interact with the working directory in your containerfile")

When you develop in an Anyscale workspace, Anyscale injects all files and code assets present in the default path for Ray (`/home/ray/default`) using the `working_dir` runtime environment feature. Anyscale persists these files during cluster restart.

You can programmatically interact with this directory in your containerfile to read or write files, such as cloning private Git repositories and installing editable packages.

Add the following line to your containerfile to add programmatic access to your workspace files:

```
COPY --chown=ray:ray working_dir /home/ray/default
```

The following example syntax installs an editable Python package name `my_module` from the workspace directory:

```
FROM anyscale/ray:2.47.1-slim-py312-cu128

COPY --chown=ray:ray working_dir /home/ray/default
RUN cd /home/ray/default/my_module && pip install -e .
```

### Example: Clone and install an editable package from GitHub[​](#example-clone-and-install-an-editable-package-from-github "Direct link to Example: Clone and install an editable package from GitHub")

The following example clones a repository directly in the containerfile then installs it as an editable package:

```
# Mount the working directory of the workspace into the image.
COPY --chown=ray:ray working_dir /home/ray/default/

# Check if Git repo is cloned and clone if not. 
RUN cd /home/ray/default && \
    [ -d sampleproject ] || git clone https://github.com/pypa/sampleproject

# Install Python module from cloned repo.
RUN cd /home/ray/default/sampleproject && pip install -e .
```

note

This pattern contains syntax to validate that the target repository doesn't yet exist in your workspace before cloning.
