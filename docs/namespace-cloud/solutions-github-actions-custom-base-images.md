<!-- Source: https://namespace.so/docs/solutions/github-actions/custom-base-images -->

# Custom Base Images for GitHub Actions

Accelerate your workflows by pre-installing dependencies directly into your runner's base image.
Instead of installing packages at runtime during every job, custom base images let you create optimized runners with your tools already available, eliminating repetitive setup steps and reducing job execution time.

## Preinstalled packages

#### Enable custom base image

Go to the desired [Runner Profile](https://cloud.namespace.so/workspace/actions/profiles) and select a customizable base image.

#### Select APT packages

Type the Ubuntu packages to install.

![Select APT packages](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Faptpackages.0255795a.png&w=1200&q=75)

You can find the list of available packages from the [Ubuntu website](https://packages.ubuntu.com/jammy/allpackages?format=txt.gz).

#### Submit the profile

After updating your profile definition the custom base image will be built.
Once the image is ready to use, you will see a confirmation in the profile editor.

![APT packages ready](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Faptpackagesready.e5df5a17.png&w=1200&q=75)

You can modify the list of pre-installed packages at any time. Any update to the selection will automatically update the base image.

## Custom Dockerfile base

Using a custom Dockerfile, you can add any dependencies on top of the Namespace base image.
Dockerfile syntax is fully supported, allowing customization beyond pre-installing APT packages.

Important to know:

- The final layer **must** be based on NAMESPACE\_BASE\_IMAGE\_REF.
  The base image contains the software required to integrate with GitHub, without it your workflows won't start.
- The user in the final image **must** be runner.
  GitHub's runner software expects to run as this user.
- After an image is built, it needs to be distributed and optimized.
  Workflows using this profile may take longer to start than normal while this is still in progress.

To get started with a Dockerfile-based custom image:

#### Enable custom base image

Go to the desired [Runner Profile](https://cloud.namespace.so/workspace/actions/profiles) and select a customizable base image.

#### Add customization steps

Add your custom Dockerfile steps to the input. Make sure to build on NAMESPACE\_BASE\_IMAGE\_REF in your final layer:

```
ARG NAMESPACE_BASE_IMAGE_REF=""
FROM ${NAMESPACE_BASE_IMAGE_REF} AS base
```

![Custom Dockerfile](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fdockerfile-based-custom-image.38f2b805.png&w=1200&q=75)

#### Submit the profile

After updating your profile definition the custom base image will be built.
Once the image is ready to use, you will see a confirmation in the profile editor.

![Custom Dockerfile ready](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fdockerfile-based-custom-image-ready.0a7167ab.png&w=1200&q=75)

You can modify the Dockerfile at any time. Any update will automatically rebuild the base image.

After a new image is built, it needs to be distributed and optimized before it can be used.
This ensures your custom base images start with the same fast performance as Namespace's standard base images.

Last updated March 5, 2026
