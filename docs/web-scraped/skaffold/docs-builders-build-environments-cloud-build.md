# Source: https://skaffold.dev/docs/builders/build-environments/cloud-build/

Title: Google Cloud Build

URL Source: https://skaffold.dev/docs/builders/build-environments/cloud-build/

Markdown Content:
Skaffold supports building remotely with Google Cloud Build.

[Cloud Build](https://cloud.google.com/cloud-build/) is a [Google Cloud Platform](https://cloud.google.com/) service that executes your builds using Google infrastructure. To get started with Cloud Build, see [Cloud Build Quickstart](https://cloud.google.com/cloud-build/docs/quickstart-docker).

Skaffold automatically connects to Cloud Build and runs your builds with it. After Cloud Build finishes building your artifacts, they are saved to the specified remote registry, such as [Google Container Registry](https://cloud.google.com/container-registry/).

Skaffold’s Cloud Build process differs from the gcloud command [`gcloud builds submit`](https://cloud.google.com/sdk/gcloud/reference/builds/submit). Skaffold does the following:

*   Creates a list of dependent files
*   Uploads a tar file of the dependent files to Google Cloud Storage
*   Submits the tar file to Cloud Build
*   Generates a single-step `cloudbuild.yaml`
*   Starts the build

Skaffold does not honor `.gitignore` or `.gcloudignore` exclusions. If you need to ignore files, use `.dockerignore`. Any `cloudbuild.yaml` found will not be used in the build process.

Configuration
-------------

To use Cloud Build, add build type `googleCloudBuild` to the `build` section of `skaffold.yaml`.

```
build:
  googleCloudBuild: {}
```

The following options can optionally be configured:

| Option | Description | Default |
| --- | --- | --- |
| `projectId` | ID of your Cloud Platform Project. If it is not provided, Skaffold will guess it from the image name. For example, given the artifact image name `gcr.io/myproject/image`, Skaffold will use the `myproject` GCP project. |  |
| `diskSizeGb` | disk size of the VM that runs the build. See [Cloud Build Reference](https://cloud.google.com/cloud-build/docs/api/reference/rest/v1/projects.builds#buildoptions). |  |
| `machineType` | type of the VM that runs the build. See [Cloud Build Reference](https://cloud.google.com/cloud-build/docs/api/reference/rest/v1/projects.builds#buildoptions). |  |
| `timeout` | amount of time (in seconds) that this build should be allowed to run. See [Cloud Build Reference](https://cloud.google.com/cloud-build/docs/api/reference/rest/v1/projects.builds#resource-build). |  |
| `logging` | specifies the logging mode. Valid modes are: `LOGGING_UNSPECIFIED`: The service determines the logging mode. `LEGACY`: Stackdriver logging and Cloud Storage logging are enabled (default). `GCS_ONLY`: Only Cloud Storage logging is enabled. See [Cloud Build Reference](https://cloud.google.com/cloud-build/docs/api/reference/rest/v1/projects.builds#loggingmode). |  |
| `logStreamingOption` | specifies the behavior when writing build logs to Google Cloud Storage. Valid options are: `STREAM_DEFAULT`: Service may automatically determine build log streaming behavior. `STREAM_ON`: Build logs should be streamed to Google Cloud Storage. `STREAM_OFF`: Build logs should not be streamed to Google Cloud Storage; they will be written when the build is completed. See [Cloud Build Reference](https://cloud.google.com/cloud-build/docs/api/reference/rest/v1/projects.builds#logstreamingoption). |  |
| `dockerImage` | image that runs a Docker build. See [Cloud Builders](https://cloud.google.com/cloud-build/docs/cloud-builders). | `gcr.io/cloud-builders/docker` |
| `kanikoImage` | image that runs a Kaniko build. See [Cloud Builders](https://cloud.google.com/cloud-build/docs/cloud-builders). | `gcr.io/kaniko-project/executor` |
| `mavenImage` | image that runs a Maven build. See [Cloud Builders](https://cloud.google.com/cloud-build/docs/cloud-builders). | `gcr.io/cloud-builders/mvn` |
| `gradleImage` | image that runs a Gradle build. See [Cloud Builders](https://cloud.google.com/cloud-build/docs/cloud-builders). | `gcr.io/cloud-builders/gradle` |
| `packImage` | image that runs a Cloud Native Buildpacks build. See [Cloud Builders](https://cloud.google.com/cloud-build/docs/cloud-builders). | `gcr.io/k8s-skaffold/pack` |
| `koImage` | image that runs a ko build. The image must contain Skaffold, Go, and a shell (runnable as `sh`) that supports here documents. See [Cloud Builders](https://cloud.google.com/cloud-build/docs/cloud-builders). | `gcr.io/k8s-skaffold/skaffold` |
| `bucket` | specifies the Cloud Storage bucket to store the staged build sources. |  |
| `concurrency` | how many artifacts can be built concurrently. 0 means “no-limit”. | `0` |
| `workerPool` | configures a pool of workers to run the build. |  |
| `region` | configures the region to run the build. If WorkerPool is configured, the region will be deduced from the WorkerPool configuration. If neither WorkerPool nor Region is configured, the build will be run in global(non-regional). See [Cloud Build locations](https://cloud.google.com/build/docs/locations). |  |
| `platformEmulatorInstallStep` | specifies a pre-build step to install the required tooling for QEMU emulation on the GoogleCloudBuild containers. This enables performing cross-platform builds on GoogleCloudBuild. If unspecified, Skaffold uses the `docker/binfmt` image by default. |  |
| `serviceAccount` | Google Cloud platform service account used by Cloud Build. If unspecified, it defaults to the Cloud Build service account generated when the Cloud Build API is enabled. |  |

Faster builds
-------------

By default, Cloud Build (invoked by Skaffold) builds all artifacts in parallel. Set `concurrency` to a non-zero value to specify the maximum number of artifacts to build concurrently. Consider reducing `concurrency` if you hit a quota restriction.

Restrictions
------------

Skaffold currently supports the following [builder types](https://skaffold.dev/docs/builders/builder-types/) when building remotely with Cloud Build:

*   [Docker](https://skaffold.dev/docs/builders/builder-types/docker/#dockerfile-remotely-with-google-cloud-build)
*   [Jib](https://skaffold.dev/docs/builders/builder-types/jib/#remotely-with-google-cloud-build)
