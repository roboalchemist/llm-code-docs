# Source: https://docs.anyscale.com/container-image/custom-image.md

# Custom images on Anyscale

[View Markdown](/container-image/custom-image.md)

# Custom images on Anyscale

Anyscale recommends building a custom image before moving any workload from development to production.

Custom images package environment variables, dependencies, and code assets into an immutable container image. Anyscale provides the following options for building, uploading, and configuring access to custom images:

* Build an image using the Anyscale console, SDK, or CLI. See [Build a custom image on Anyscale](/container-image/build-image.md).
* Reference an image from an external image registry. See [Use container images from an external registry](/container-image/image-registry.md).
* Register a custom image in your Anyscale organization. See [Register a custom image](/container-image/image-registry.md#register).

For a tutorial on building custom images and referencing them from an external registry, see [Tutorial: Build a custom container image](/container-image/build-image-tutorial.md).

note

You can also edit and use a containerfile to build a custom image during interactive development in an Anyscale workspace. See [Iterate on workspace container images](/dependency-management/containerfiles.md).

## Anyscale-compatible custom images[​](#compatibility "Direct link to Anyscale-compatible custom images")

Most custom images extend a base image provided by Anyscale. For a full list of base images and their dependencies, see [Anyscale base images](/reference/base-images.md).

You can build an image that's not based on an Anyscale base image, but must follow minimum specifications. See [Requirements for an Anyscale container image](/container-image/image-requirement.md).

If you're building your custom image on Anyscale, you can use init scripts to run arbitrary programs as part of the build process. See [Use init scripts with custom images](/dependency-management/init-scripts.md).

The Anyscale base images come with a default entrypoint set. Overwriting this entrypoint may break the web terminal and Jupyter notebook server when you launch your cluster.
