# Source: https://firebase.google.com/docs/build.md.txt

# Source: https://firebase.google.com/docs/app-hosting/build.md.txt

# Source: https://firebase.google.com/docs/build.md.txt

# Source: https://firebase.google.com/docs/app-hosting/build.md.txt

<br />

Firebase App HostingutilizesCloud Buildto transform your application source code into a containerized format suitable for deployment onCloud Run.

The build process operates through the following key stages:

1. **Ingest**: Gathers your application source code and configuration.

2. **Build**: Installs dependencies and builds your application.

3. **Handoff** : Finalizes the productionCloud Runcontainer.

These three steps correspond directly to build steps 1, 2 and 3 as displayed inCloud Buildin the Google Cloud Console:

![A screen capture of a Google Cloud console view of Cloud Build steps](https://firebase.google.com/static/docs/app-hosting/images/build-steps.png)

## Ingest stage

This stage is responsible for handling pre-build logic. It reads, sanitizes, and writes user-defined environment variables. It also dereferences and pins any secrets specified in the`apphosting.yaml`file.

## Build stage

This is the core of the build process, responsible for generating a runnable container image and a`bundle.yaml`file defining your build configuration. It utilizes[Cloud Native Buildpacks](https://cloud.google.com/docs/buildpacks/overview)to package the application efficiently. More information on the`bundle.yaml`file can be found on[github](https://github.com/FirebaseExtended/firebase-framework-tools).

Buildpacks are responsible for transforming your application source code into production ready container images.Firebase App Hostingchains together several buildpacks to complete the build process:

1. **Runtime Buildpack**: Ensures all necessary components for running a basic Node.js application are included and dependencies are installed.
2. **Monorepo Buildpack**: Configures subsequent buildpacks to handle different monorepo scenarios.
3. **Framework Buildpack**: Installs the correct framework adapter (like Angular or Next.js) and prepares subsequent buildpacks.

   Framework adapters are in charge of running the productionized build command and mapping any relevant framework-specific config values to a standard format readable byApp Hosting.
4. **Package Manager Buildpack**: Executes the installation of dependencies and builds the app using npm, yarn, or pnpm.

5. **Output Bundle Buildpack**: Defines the run command and prepares the output bundle for execution.

## Handoff stage

This final stage packages all the information extracted from the application source code plus the build container image and sends it to theApp Hostingbackend. TheApp Hostingbackend then uses this information to set upCloud Runwith the proper configurations.

## Learn more

The entireApp Hostingbuild process is open source.

- The buildpack code is in[the Google Cloud buildpacks repo](https://github.com/GoogleCloudPlatform/buildpacks)
- Code for framework adapters is in the[firebase-framework-tools repo](https://github.com/FirebaseExtended/firebase-framework-tools)
- Learn more about[Cloud Native buildpacks](https://cloud.google.com/docs/buildpacks/overview)and[Cloud Build](https://cloud.google.com/build/docs/overview)