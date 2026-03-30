# Source: https://firebase.google.com/docs/app-hosting/build.md.txt

Firebase App Hosting utilizes Cloud Build to transform your
application source code into a containerized format suitable for deployment on
Cloud Run.

The build process operates through the following key stages:

1. **ubuntu**: Workspace initialization.

2. **preparer**: Gathers your application source code and configuration.

3. **pre-buildpack**: Prepares the buildpack environment.

4. **build**: Installs dependencies and builds your application.

5. **publisher** : Finalizes the production Cloud Run container.

These five steps correspond directly to build steps as displayed in
Cloud Build in the Google Cloud Console:

![A screen capture of a Google Cloud console view of Cloud Build steps](https://firebase.google.com/static/docs/app-hosting/images/build-steps-lifecycle.png)

## Workspace Initialization

This stage corresponds to the ubuntu build step.
It initializes the build workspace, ensuring the correct file permissions
are set for the directories used by the subsequent build steps.

## Preparer

This stage is responsible for handling pre-build logic. It reads, sanitizes, and
writes user-defined environment variables. It also dereferences and pins any
secrets specified in the `apphosting.yaml` file.

## Pre-buildpack

This step prepares the environment for the [Cloud Native Buildpacks](https://cloud.google.com/docs/buildpacks/overview)
lifecycle.
This involves running a shim that translates the configurations and environment
variables prepared in the previous stage
into the format expected by the CNB tools.

## Build

This is the core of the build process, responsible for generating a runnable
container image and a `bundle.yaml` file defining your build configuration.
It utilizes the Cloud Native Buildpacks
and the [lifecycle creator](https://buildpacks.io/docs/for-platform-operators/concepts/lifecycle/create/)
binary to package the
application efficiently. More information on the `bundle.yaml` file can be found
on [github](https://github.com/firebase/apphosting-adapters).

Buildpacks are responsible for transforming your application source code into
production ready container images. Firebase App Hosting chains together
several buildpacks to complete the build process:

1. **Runtime Buildpack**: Ensures all necessary components for running a basic Node.js application are included and dependencies are installed.
2. **Monorepo Buildpack**: Configures subsequent buildpacks to handle different monorepo scenarios.
3. **Framework Buildpack**: Installs the correct framework adapter (like
   Angular or Next.js) and prepares subsequent buildpacks.

   Framework adapters are in charge of running the productionized build
   command and mapping any relevant framework-specific config values to a
   standard format readable by App Hosting.
4. **Package Manager Buildpack**: Executes the installation of dependencies and
   builds the app using npm, yarn, or pnpm.

5. **Output Bundle Buildpack**: Defines the run command and prepares the output
   bundle for execution.

## Publisher

This final stage packages all the information extracted from the application
source code plus the build container image and sends it to the App Hosting
backend. The App Hosting backend then uses this information to set up
Cloud Run with the proper configurations.

## Learn more

The entire App Hosting build process is open source.

- The buildpack code is in [the Google Cloud buildpacks repo](https://github.com/GoogleCloudPlatform/buildpacks)
- Code for framework adapters is in the [firebase-framework-tools repo](https://github.com/firebase/apphosting-adapters)
- Learn more about [Cloud Native buildpacks](https://cloud.google.com/docs/buildpacks/overview) and [Cloud Build](https://cloud.google.com/build/docs/overview)