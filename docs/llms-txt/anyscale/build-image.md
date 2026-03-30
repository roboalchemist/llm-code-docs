# Source: https://docs.anyscale.com/container-image/build-image.md

# Build a custom image on Anyscale

[View Markdown](/container-image/build-image.md)

# Build a custom image on Anyscale

You can build custom images that extend the functionality of base images provided by Anyscale. This page provides an overview of this functionality and an example of building a custom image with the console. To use the CLI or SDK, see [Image API Reference](/reference/image.md).

Anyscale generates a new version each time you build your image. You can view the definitions for all versions of images from the **Container images** page in the console.

You can select your custom images from the console when defining workspaces or use the image URI when using the CLI or SDK to start Ray clusters.

note

The Anyscale custom image build tools only support extending Anyscale base images. Contact [Anyscale Support](mailto:support@anyscale.com) if you need to use other images when building images on Anyscale.

important

Non-slim Anyscale base images for Ray 2.47.0 or later are multi-platform images, supporting both `x86` and `AArch64` architectures. For details on multi-platform images, see the [Docker docs](https://docs.docker.com/build/building/multi-platform/#difference-between-single-platform-and-multi-platform-images).

When you customize a base image on Anyscale, the resulting image is a single-platform `x86` image.

If you need to use the `AArch64` architecture to support ARM-based virtual machines, you must use external build tools and an external image registry. See [Use container images from an external registry](/container-image/image-registry.md).

## Define a custom image for Anyscale[​](#syntax "Direct link to Define a custom image for Anyscale")

Anyscale uses a subset of Dockerfile syntax to customize images.

Use the following Dockerfile instructions when defining your custom image:

| Supported instructions | Description                                                                                                                                                                     |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `FROM`                 | Create a new build from an existing Anyscale base image.                                                                                                                        |
| `ENV`                  | Set environment variables.                                                                                                                                                      |
| `ARG`                  | Set build-time only variables. You must specify a default value because there's no interactive mode when building on Anyscale, for example `ARG variable_name=some_value`.      |
| `WORKDIR`              | Change the working directory. **Note**: This is only for **build time** and doesn't affect where Anyscale starts your job, service, or the workspace default working directory. |
| `COPY`                 | Copy files and directories from a previous build stage, not from local storage.                                                                                                 |
| `RUN`                  | Execute build commands.                                                                                                                                                         |

## Build a custom image in the console[​](#build-farm "Direct link to Build a custom image in the console")

Complete the following steps to create a simple custom image in the Anyscale console:

1. From the console home screen, select **Advanced > Container images**.
2. Click **+ Build**.
3. In the **Name** field, provide a unique name for the image.
   <!-- -->
   * The URI of the image generates automatically. Use this URI to reference this image when you create a workspace, job, or service.
4. The editor displays template text to help you define your image. For example, update the definition to the following:
   <!-- -->
   ```
   FROM anyscale/ray:2.47.1-slim-py312
   RUN pip install --no-cache-dir --upgrade emoji
   ```
5. Click **Build**.

note

You must have sufficient permissions to build custom images. See [Container image roles](/administration/organization/permissions.md#container-image).
