# Source: https://northflank.com/docs/v1/application/observe/see-builds.md

# See builds

You can find a list of [builds](https://northflank.com/docs/v1/application/build/build-code-from-a-git-repository#build-from-a-repository) on combined and build services, and [jobs](https://northflank.com/docs/v1/application/run/run-an-image-once-or-on-a-schedule) that deploy from a repository. The overview for your service will display the latest builds, and you can navigate to the builds page for a full history of builds.

Each listed build includes information including the branch, commit hash, and duration of the build, as well as buttons to start a new build, abort a build in progress, or deploy a specific build (in a combined service or job).

When a build is successful it is pushed to the [Northflank container registry](https://northflank.com/docs/v1/application/build/pull-images-from-Northflank), ready to be deployed. The new build will be automatically deployed to any linked services with [CD configured](https://northflank.com/docs/v1/application/release/manage-ci-cd).

You can click through on each build to view live detailed [logs](view-logs) and [metrics](view-metrics).

You can also [build the image again](https://northflank.com/docs/v1/application/build/build-code-from-a-git-repository) and pull the image from the [Northflank container registry](https://northflank.com/docs/v1/application/build/pull-images-from-Northflank) from the individual build view.

![Viewing a list of builds on a build service in the Northflank application](https://assets.northflank.com/documentation/v1/application/observe/see-builds/build-list.png)

### Build statuses

Pending: the build is queued to start
Starting: the build process is starting
Cloning: the repository is being cloned
Building: the build is in progress
Uploading: the build was successful, and the image is being uploaded to Northflank
Successful: the build was completed, and the image is available on Northflank
Aborted: the build was cancelled by the user
Failed: the build could not be completed
 

## Next steps

- [View logs: View detailed, real-time logs from builds, deployments, and more.](/v1/application/observe/view-logs)
- [View metrics: View detailed, real-time metrics from builds, deployments, and more.](/v1/application/observe/view-metrics)
- [Configure health checks: Monitor the uptime and success of your deployed services and builds to ensure your code runs correctly and is always available.](/v1/application/observe/configure-health-checks)
- [Increase CPU and memory: Power-up your services by adding memory and moving from shared to dedicated CPU usage.](/v1/application/scale/scale-cpu-and-memory)
- [Build from a Git repository: Start building from your linked Git repositories in minutes.](/v1/application/build/build-code-from-a-git-repository)
- [Pull an image from Northflank: Pull images built on Northflank locally, or use built images as the base image in your Dockerfile.](/v1/application/build/pull-images-from-Northflank)
