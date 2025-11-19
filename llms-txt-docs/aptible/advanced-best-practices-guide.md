# Source: https://www.aptible.com/docs/how-to-guides/platform-guides/advanced-best-practices-guide.md

# Advanced Best Practices Guide

> Learn how to take your infrastructure to the next level with advanced best practices

# Overview

> 📘 Read our [Best Practices Guide](/how-to-guides/platform-guides/best-practices-guide) before proceeding.

This guide will provide advanced information for users who want to maximize the value and usage of the Aptible platform. With these advanced best practices, you'll be able to deploy your infrastructure with best practices for performance, reliability, developer efficiency, and security.

## Planning

### Authentication

* Set up [SSO](/core-concepts/security-compliance/authentication/sso).
  * Using an SSO provider can help enforce login policies, including password rotation, MFA requirements, and improve users' ability to audit and verify access is revoked upon workforce changes.

### Disaster Recovery

* Plan for Regional failure using our [Business Continuity guide](/how-to-guides/platform-guides/minimize-downtown-outages)
  * While unprecedented, an AWS Regional failure will test the preparedness of any team. If the Recovery time objective and recovery point objective set by users are intended to cover a regional disaster, Aptible recommends creating a dedicated stack in a separate region as a baseline ahead of a potential regional failure.

### CI/CD Strategy

* Align the release process across staging and production
  * To minimize issues experienced in production, users should repeat the established working process for releasing a staging environment. This not only gives users confidence when deploying to production but should also allow users to reproduce any issues that arise in production within the staging environment. Follow [these steps](/how-to-guides/app-guides/integrate-aptible-with-ci/overview) to integrate Aptible with a CI Platform.
* Use a build artifact for deployment.
  * Using [image-based deployment](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy) allows users to ensure the exact image that passed the testing process is deployed to production, and users may retain that exact image for any future needs. Docker provides users the ability to [tag images](https://docs.docker.com/engine/reference/commandline/tag/), which allows images to be uniquely identified and reused when needed.   Each git-based deployment introduces a chance that the resulting image may differ. If code passes internal testing and is deployed to staging one week and then production the next, the image build process may have a different result even if dependencies are pinned. The worst case scenario may be that users need to roll back to a prior version, but due to external circumstances that image can no longer be built.

## Operational Practices

### Apps

* Ensure your migrations backwards compatible
  * For services with HTTP(S) Endpoint, Aptible employs a zero downtime strategy whereby for a brief period, both new and old containers are running simultaneously. While the migrations in `before_release` are run before the new containers are added to the load balancing pool, this does mean any migrations not compatible with the old running code may result in noticeable errors or downtime during deployment. It is important that migrations are backwards compatible to avoid these errors. More on the release process [here](/core-concepts/apps/deploying-apps/releases/overview#services-with-endpoints).
* Configure processes to run as PID 1 to handle signals properly
  * Since Docker is essentially a process manager, it is important to properly configure Containers to handle signals. Docker (and by extension all Aptible platform features) will send signals to PID 1 in the container to instruct it to stop. If PID 1 is not in the process, or the process doesn't respond to SIGTERM well, users may notice undesirable effects when restarting, scaling, deploying your Apps, or when the container exceeds the memory limits. More on PID 1 [here](/how-to-guides/app-guides/define-services#advanced-pid-1-in-your-container-is-a-shell).
* Use `exec` in the Procfile
  * When users specify a Procfile, but do not have an ENTRYPOINT, the [commands are interpreted by a shell](/how-to-guides/app-guides/define-services#procfile-commands). Use `exec` to ensure the process assumes PID 1. More on PID 1 and `exec` [here](/how-to-guides/app-guides/define-services#advanced-pid-1-in-your-container-is-a-shell).

### Services

* Use the APTIBLE\_CONTAINER\_SIZE variable where appropriate
  * Some types of processes, particularly Java applications, require setting the size of a memory heap.  Users can use the environment variable set by Aptible to ensure the process knows what the container size is.  This helps avoid over-allocating memory and ensures users can quickly scale the application without having to set the memory amount manually in your App. Learn more about this variable [here](/core-concepts/scaling/memory-limits#how-do-i-know-the-memory-limit-for-a-container).
* Host static assets externally and use consistent naming conventions
  * There are two cases where the naming and or storage of static assets may cause issues:
    1. If each container generates static assets within itself when it starts, randomly assigned static assets will cause errors for services scaled to >1 container
    2. If assets are stored in the container image (as opposed to S3, for example), users may have issues during zero-downtime deployments where requests for static assets fail due to two incompatible code-bases running at the same time.
  * Learn more about serving static assets in [this tutorial](/how-to-guides/app-guides/serve-static-assets)

### Databases

* Upgrade all Database volumes to GP3
  * Newly provisioned databases are automatically provisioned on GP3 volumes. The GP3 volume type provides a higher baseline of IO performance but, more importantly, allows ONLINE scaling of IOPs and throughput, so users can alleviate capacity issues without restarting the database. Users can upgrade existing databases with zero downtime using these [steps](https://www.aptible.com/changelog#content/changelog/easily-modify-databases-without-disruption-with-new-cli-command-aptible-db-modify.mdx). The volume type of existing databases can be confirmed at the top of each database page in the Aptible dashboard.

### Endpoints

* Use strict runtime health checks
  * By default, Aptible health checks only ensure a service is returning responses to HTTP requests, not that those requests are free of errors. By enabling strict health checks, Aptible will only route requests to containers if those containers return a 200 response to `/healthcheck`. Enabling strict health checks also allows users to configure the route Aptible checks to return healthy/unhealthy using the criteria established by the user. Enable strict runtime health checks using the steps [here](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/health-checks#strict-health-checks).

### Dependency Vulnerability Scanning

* Use an image dependency vulnerability scanner before deploying to production.
  * The built-in security scanner is designed for git-based deployments, where Aptible builds the image and users have no method to inspect it directly. It can only be inspected after being deployed. Aptible recommends scanning images before deploying to production. Using image-based deployment will be the easiest way to scan an image and integrate the scans into the CI/CD pipeline. Quay and ECS can scan images automatically and support alerting. Otherwise, users will need to scan the deployed staging image before deploying that commit to production.
