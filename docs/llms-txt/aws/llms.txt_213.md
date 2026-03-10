# Source: https://docs.aws.amazon.com/codebuild/latest/userguide/llms.txt

# AWS CodeBuild User Guide

> Describes how you can use AWS CodeBuild, an AWS service that builds your software applications in the AWS cloud.

- [Getting started](https://docs.aws.amazon.com/codebuild/latest/userguide/getting-started-overview.html)
- [Run Windows samples](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-windows.html)
- [Plan a build](https://docs.aws.amazon.com/codebuild/latest/userguide/planning.html)
- [Troubleshooting](https://docs.aws.amazon.com/codebuild/latest/userguide/troubleshooting.html)
- [Quotas](https://docs.aws.amazon.com/codebuild/latest/userguide/limits.html)
- [Document history](https://docs.aws.amazon.com/codebuild/latest/userguide/history.html)

## [What is AWS CodeBuild?](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)

- [Concepts](https://docs.aws.amazon.com/codebuild/latest/userguide/concepts.html): Explains important concepts for working with AWS CodeBuild.


## [Use case-based samples](https://docs.aws.amazon.com/codebuild/latest/userguide/use-case-based-samples.html)

### [Cross-service samples](https://docs.aws.amazon.com/codebuild/latest/userguide/cross-service-samples.html)

Provides information about cross-service samples that are designed to work with AWS CodeBuild.

- [Amazon ECR sample](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-ecr.html): Provides information about the Amazon ECR sample that is designed to work with AWS CodeBuild.

### [Amazon EFS sample](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-efs.html)

Provides information about how to use Amazon EFS with build containers.

- [Troubleshoot the Amazon EFS integration](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-efs-troubleshooting.html): The following are errors you might encounter when setting up Amazon EFS with CodeBuild.
- [AWS CodePipeline samples](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-codepipeline.html): Provides information about CodePipeline samples that is designed to work with AWS CodeBuild.
- [AWS Config sample](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-integrate-config.html): Demonstrates how to integrate AWS Config with AWS CodeBuild.

### [Build notifications sample](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-build-notifications.html)

Provides information about the build notifications sample that is designed to work with AWS CodeBuild.

- [Build notifications input format reference](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-build-notifications-ref.html): CloudWatch delivers notifications in JSON format.

### [Build badges sample](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-build-badges.html)

Provides information about AWS CodeBuild build badges.

- [Access AWS CodeBuild build badges](https://docs.aws.amazon.com/codebuild/latest/userguide/access-badges.html): You can use AWS CodeBuild console or the AWS CLI to access build badges.
- [Publish CodeBuild build badges](https://docs.aws.amazon.com/codebuild/latest/userguide/publish-badges.html): You can display the status of the latest build in a markdown file using your build badge URL in a markdown image.
- [CodeBuild badge statuses](https://docs.aws.amazon.com/codebuild/latest/userguide/badge-statuses.html): The CodeBuild build badge can have one of the following statuses.
- [Test report sample](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-test-report-cli.html): Tests that you specify in your buildspec file are run during your build.

### [Docker samples for CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-docker-section.html)

Provides information about Docker samples that are designed to work with AWS CodeBuild.

- [Docker in custom image sample](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-docker-custom-image.html): Provides information about the Docker in custom image sample that is designed to work with AWS CodeBuild.
- [Docker image build server sample](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-docker-server.html): Provides information about Docker builds in a managed image build server with AWS CodeBuild.
- [Windows Docker builds sample](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-windows-docker-custom-image.html): Provides information about the Windows Docker build sample that is designed to work with AWS CodeBuild.

### ['Publish Docker image to Amazon ECR' sample](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-docker.html)

Provides information about the Docker sample that is designed to work with AWS CodeBuild.

- [Adapt the sample to Docker Hub](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-docker-docker-hub.html): To adapt the 'Publish Docker image to Amazon ECR' sample so that the Docker image is pushed to Docker Hub instead of Amazon ECR, edit the sample's code.

### [Private registry with AWS Secrets Manager sample](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-private-registry.html)

This sample shows you how to use a Docker image that is stored in a private registry as your AWS CodeBuild runtime environment.

- [Create a CodeBuild project with a private registry](https://docs.aws.amazon.com/codebuild/latest/userguide/private-registry-sample-create-project.html)
- [Configure a private registry credential for self-hosted runners](https://docs.aws.amazon.com/codebuild/latest/userguide/private-registry-sample-configure-runners.html): Use the following instructions to configure a registry credential for a self-hosted runner.
- [Host build output in an S3 bucket](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-disable-artifact-encryption.html): Demonstrates how to publish a static website using build output in an S3 bucket.

### [Multiple inputs and outputs sample](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-multi-in-out.html)

Demonstrates how to create a build project with multiple input sources and multiple output artifacts.

- [Create a build project with multiple inputs and outputs](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-multi-in-out-create.html): Use the following procedure to create a build project with multiple inputs and outputs.
- [Create a project without a source](https://docs.aws.amazon.com/codebuild/latest/userguide/no-source.html): Demonstrates how to create a build project that does not have a source.

### [Runtime versions in buildspec file sample](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-runtime-versions.html)

If you use the Amazon Linux 2 (AL2) standard image version 1.0 or later, or the Ubuntu standard image version 2.0 or later, you can specify one or more runtimes in the runtime-versions section of your buildspec file.

- [Update the runtime version in the buildspec file](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-runtime-update-version.html): You can modify the runtime used by your project to a new version by updating the runtime-versions section of your buildspec file.
- [Specify two runtimes](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-runtime-two-major-version-runtimes.html): You can specify more than one runtime in the same CodeBuild build project.

### [Source version sample](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html)

Provides information about how to specify the version of the source in your AWS CodeBuild build project.

- [Specify a GitHub repository version with a commit ID](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version-github.html): Provides information about how to specify the version of the source in your AWS CodeBuild build project.
- [Specify a GitHub repository version with a reference and commit ID](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version-github-ref.html): Provides information about how to specify the version of the source in your AWS CodeBuild build project.

### [Third-party source repository samples](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-third-party-source.html)

Provides information about third-party source repository samples that are designed to work with AWS CodeBuild.

- [Run the Bitbucket sample](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-bitbucket-pull-request.html): Provides information about how to create Bitbucket pull requests with webhooks using AWS CodeBuild.
- [Run the GitHub Enterprise Server sample](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-github-enterprise.html): Provides information about the GitHub pull request sample that is designed to work with AWS CodeBuild.
- [Run the GitHub pull request and webhook filter sample](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-github-pull-request.html): Provides information about the GitHub pull request sample that is designed to work with AWS CodeBuild.
- [Tutorial: Apple code signing with Fastlane in CodeBuild using S3 for certificate storage](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-fastlane.html): fastlane is a popular open source automation tool to automate beta deployments and releases for your iOS and Android apps.
- [Tutorial: Apple code signing with Fastlane in CodeBuild Using GitHub for certificate storage](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-fastlane-github.html): fastlane is a popular open source automation tool to automate beta deployments and releases for your iOS and Android apps.
- [Set artifact names at build time](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-buildspec-artifact-naming.html): Shows how to create artifact names with semantic versioning at build time using Shell commands and the buildspec file.


## [Buildspec reference](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html)

- [Batch buildspec reference](https://docs.aws.amazon.com/codebuild/latest/userguide/batch-build-buildspec.html): Learn about buildspec entries for batch builds in AWS CodeBuild.


## [Build environment reference](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref.html)

### [Docker images provided by CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available.html)

A supported image is the latest major version of an image available in CodeBuild and is updated with minor and patch version updates.

- [Obtain the list of current Docker images](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available-get.html): CodeBuild frequently updates the list of Docker images to add the latest images and deprecate old images.
- [EC2 compute images](https://docs.aws.amazon.com/codebuild/latest/userguide/ec2-compute-images.html): AWS CodeBuild supports the following Docker images that are available for EC2 compute in CodeBuild.
- [Lambda compute images](https://docs.aws.amazon.com/codebuild/latest/userguide/lambda-compute-images.html): AWS CodeBuild supports the following Docker images that are available for AWS Lambda compute in CodeBuild.
- [Deprecated CodeBuild images](https://docs.aws.amazon.com/codebuild/latest/userguide/deprecated-images.html): A deprecated image is an image that is no longer cached or updated by CodeBuild.
- [Available runtimes](https://docs.aws.amazon.com/codebuild/latest/userguide/available-runtimes.html): You can specify one or more runtimes in the runtime-versions section of your buildspec file.
- [Runtime versions](https://docs.aws.amazon.com/codebuild/latest/userguide/runtime-versions.html): When you specify a runtime in the runtime-versions section of your buildspec file, you can specify a specific version, a specific major version and the latest minor version, or the latest version.
- [Build environment compute modes and types](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html): In CodeBuild, you can specify the compute and runtime environment image that CodeBuild uses to run your builds.
- [Shells and commands in build environments](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-cmd.html): You provide a set of commands for AWS CodeBuild to run in a build environment during the lifecycle of a build (for example, installing build dependencies and testing and compiling your source code).
- [Environment variables in build environments](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-env-vars.html): Learn about environment variables that you can use to build commands.
- [Background tasks in build environments](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-background-tasks.html): Learn you can run background tasks in build environments.


## [Build projects](https://docs.aws.amazon.com/codebuild/latest/userguide/working-with-build-projects.html)

- [Create a build project](https://docs.aws.amazon.com/codebuild/latest/userguide/create-project.html): Describes how to create a build project in AWS CodeBuild.
- [Create a notification rule](https://docs.aws.amazon.com/codebuild/latest/userguide/notification-rule-create.html): Learn how to create a notification rule for AWS CodeBuild.
- [Change build project settings](https://docs.aws.amazon.com/codebuild/latest/userguide/change-project.html): Describes how to change a build project's settings in AWS CodeBuild.
- [Multiple access tokens](https://docs.aws.amazon.com/codebuild/latest/userguide/multiple-access-tokens.html): Learn more about working with multiple access tokens in CodeBuild.
- [Delete build projects](https://docs.aws.amazon.com/codebuild/latest/userguide/delete-project.html): Describes how to delete a build project in AWS CodeBuild.
- [Get public build project URLs](https://docs.aws.amazon.com/codebuild/latest/userguide/public-builds.html): Learn about public build projects in AWS CodeBuild.

### [Share build projects](https://docs.aws.amazon.com/codebuild/latest/userguide/project-sharing.html)

Working with shared projects.

- [Access shared projects](https://docs.aws.amazon.com/codebuild/latest/userguide/project-sharing-access-prereqs.html): To access a shared project, a consumer's IAM role requires the BatchGetProjects permission.
- [Unshare a shared project](https://docs.aws.amazon.com/codebuild/latest/userguide/project-sharing-unshare.html): An unshared project, including its builds, can be accessed only by its owner.
- [Identify a shared project](https://docs.aws.amazon.com/codebuild/latest/userguide/project-sharing-identify.html): Owners and consumers can use the AWS CLI to identify shared projects.
- [Shared project permissions](https://docs.aws.amazon.com/codebuild/latest/userguide/project-sharing-perms.html)

### [Tag build projects](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-tag-project.html)

Describes how to tag resources in AWS CodeBuild.

- [Add a tag to a project](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-tag-project-add.html): Adding tags to a project can help you identify and organize your AWS resources and manage access to them.
- [View tags for a project](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-tag-project-list.html): Tags can help you identify and organize your AWS resources and manage access to them.
- [Edit tags for a project](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-tag-project-update.html): You can change the value for a tag associated with a project.
- [Remove a tag from a project](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-tag-project-delete.html): You can remove one or more tags associated with a project.

### [Use runners](https://docs.aws.amazon.com/codebuild/latest/userguide/runners.html)

Provides information about using runners with AWS CodeBuild.

### [GitHub Actions](https://docs.aws.amazon.com/codebuild/latest/userguide/action-runner-overview.html)

Learn about setting up self-hosted GitHub Actions runners in AWS CodeBuild.

- [About the CodeBuild-hosted GitHub Actions runner](https://docs.aws.amazon.com/codebuild/latest/userguide/action-runner-questions.html): Learn about the CodeBuild-hosted GitHub Actions runner in AWS CodeBuild.
- [Tutorial: Configure a CodeBuild-hosted GitHub Actions runner](https://docs.aws.amazon.com/codebuild/latest/userguide/action-runner.html): This tutorial shows you how to configure your CodeBuild projects to run GitHub Actions jobs.
- [Troubleshoot the webhook](https://docs.aws.amazon.com/codebuild/latest/userguide/action-runner-troubleshoot-webhook.html): Learn how you can troubleshoot the webhook.
- [Supported label overrides](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-github-action-runners-update-labels.html): Learn how you can provide a variety of label overrides that modify your self-hosted runner build.
- [Supported compute images](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-github-action-runners-update-yaml.images.html): Learn how compute images support CodeBuild-hosted GitHub Actions runner.

### [GitLab runners](https://docs.aws.amazon.com/codebuild/latest/userguide/gitlab-runner.html)

Learn about setting up self-managed GitLab runners in AWS CodeBuild.

- [About the CodeBuild-hosted GitLab runner](https://docs.aws.amazon.com/codebuild/latest/userguide/gitlab-runner-questions.html): Learn about the CodeBuild-hosted GitLab runner in AWS CodeBuild.
- [Tutorial: Configure a CodeBuild-hosted GitLab runner](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-gitlab-runners.html): This tutorial shows you how to configure your CodeBuild projects to run GitLab CI/CD pipeline jobs.
- [Supported label overrides](https://docs.aws.amazon.com/codebuild/latest/userguide/gitlab-runners-update-labels.html): In your GitLab CI/CD pipeline YAML, you can provide a variety of label overrides that modify your self-managed runner build.
- [Supported compute images](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-gitlab-runners-gitlab-ci.images.html): Learn how compute images support CodeBuild-hosted GitHub runner.

### [Buildkite runner](https://docs.aws.amazon.com/codebuild/latest/userguide/buildkite-runner.html)

Learn about setting up self-managed Buildkite runner in AWS CodeBuild.

- [About the CodeBuild-hosted Buildkite runner](https://docs.aws.amazon.com/codebuild/latest/userguide/buildkite-runner-about.html): The following are some common questions about the CodeBuild-hosted Buildkite runner.
- [Tutorial: Configure a CodeBuild-hosted Buildkite runner](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-runner-buildkite.html): This tutorial shows you how to configure your CodeBuild projects to run Buildkite jobs.
- [Run buildspec commands for the INSTALL, PRE_BUILD, and POST_BUILD phases](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-runner-buildkite-buildspec.html): By default, CodeBuild ignores any buildspec commands when running a self-hosted Buildkite runner build.
- [Setting up a Buildkite runner programmatically](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-runner-buildkite-CLI.html): In order to configure a Buildkite runner project programatically, you will need to configure the following resources:
- [Troubleshoot the webhook for failed builds or a hanging job](https://docs.aws.amazon.com/codebuild/latest/userguide/buildkite-runner-troubleshoot-webhook.html): Issue:
- [Troubleshoot the webhook permission issues](https://docs.aws.amazon.com/codebuild/latest/userguide/buildkite-runner-troubleshoot-webhook-permissions.html): Issue:
- [Label overrides supported with the CodeBuild-hosted Buildkite runner](https://docs.aws.amazon.com/codebuild/latest/userguide/buildkite-runner-update-labels.html): In your Buildkite pipeline steps agent tag labels, you can provide a variety of label overrides that modify your self-hosted runner build.
- [Supported compute images for Buildkite runner](https://docs.aws.amazon.com/codebuild/latest/userguide/buildkite-runner-update-yaml.images.html): Learn how compute images support CodeBuild-hosted Buildkite runner.

### [Use webhooks](https://docs.aws.amazon.com/codebuild/latest/userguide/webhooks.html)

Provides information about using webhooks with AWS CodeBuild.

### [Bitbucket webhook events](https://docs.aws.amazon.com/codebuild/latest/userguide/bitbucket-webhook.html)

You can use webhook filter groups to specify which Bitbucket webhook events trigger a build.

- [Filter Bitbucket webhook events (console)](https://docs.aws.amazon.com/codebuild/latest/userguide/bitbucket-webhook-events-console.html): To use the AWS Management Console to filter webhook events:
- [Filter Bitbucket webhook events (SDK)](https://docs.aws.amazon.com/codebuild/latest/userguide/bitbucket-webhook-events-sdk.html): To use the AWS CodeBuild SDK to filter webhook events, use the filterGroups field in the request syntax of the CreateWebhook or UpdateWebhook API methods.
- [Filter Bitbucket webhook events (CloudFormation)](https://docs.aws.amazon.com/codebuild/latest/userguide/bitbucket-webhook-events-cfn.html): To use an CloudFormation template to filter webhook events, use the AWS CodeBuild project's FilterGroups property.

### [GitHub global and organization webhooks](https://docs.aws.amazon.com/codebuild/latest/userguide/github-global-organization-webhook.html)

You can use CodeBuild GitHub global or organization webhooks to start builds on webhook events from any repository within a GitHub organization or enterprise.

- [Set up a global or organization GitHub webhook](https://docs.aws.amazon.com/codebuild/latest/userguide/github-global-organization-webhook-setup.html): The high-level steps to set up a global or organization GitHub webhook are as follows.
- [Filter GitHub global or organization webhook events (console)](https://docs.aws.amazon.com/codebuild/latest/userguide/github-global-organization-webhook-events-console.html): When creating a GitHub project through the console, select the following options to create a GitHub global or organization webhook within the project.
- [Filter GitHub organization webhook events (CloudFormation)](https://docs.aws.amazon.com/codebuild/latest/userguide/github-organization-webhook-events-cfn.html): To use an CloudFormation template to filter organization webhook events, use the AWS CodeBuild project's ScopeConfiguration property.
- [GitHub manual webhooks](https://docs.aws.amazon.com/codebuild/latest/userguide/github-manual-webhook.html): You can configure manual GitHub webhooks to prevent CodeBuild from automatically attempting to create a webhook within GitHub.

### [GitHub webhook events](https://docs.aws.amazon.com/codebuild/latest/userguide/github-webhook.html)

You can use webhook filter groups to specify which GitHub webhook events trigger a build.

- [Filter GitHub webhook events (console)](https://docs.aws.amazon.com/codebuild/latest/userguide/github-webhook-events-console.html): Use the following instructions to filter GitHub webhook events using the AWS Management Console.
- [Filter GitHub webhook events (SDK)](https://docs.aws.amazon.com/codebuild/latest/userguide/github-webhook-events-sdk.html): To use the AWS CodeBuild SDK to filter webhook events, use the filterGroups field in the request syntax of the CreateWebhook or UpdateWebhook API methods.
- [Filter GitHub webhook events (CloudFormation)](https://docs.aws.amazon.com/codebuild/latest/userguide/github-webhook-events-cfn.html): To use an CloudFormation template to filter webhook events, use the AWS CodeBuild project's FilterGroups property.

### [GitLab group webhooks](https://docs.aws.amazon.com/codebuild/latest/userguide/gitlab-group-webhook.html)

You can use CodeBuild GitLab group webhooks to start builds on webhook events from any repository within a GitLab group.

- [Set up a group GitLab webhook](https://docs.aws.amazon.com/codebuild/latest/userguide/gitlab-group-webhook-setup.html): The high-level steps to set up a group GitLab webhook are as follows.
- [Filter GitLab group webhook events (console)](https://docs.aws.amazon.com/codebuild/latest/userguide/gitlab-group-webhook-events-console.html): When creating a GitLab project through the console, select the following options to create a GitLab group webhook within the project.
- [Filter GitLab group webhook events (CloudFormation)](https://docs.aws.amazon.com/codebuild/latest/userguide/gitlab-group-webhook-events-cfn.html): To use an CloudFormation template to filter group webhook events, use the AWS CodeBuild project's ScopeConfiguration property.
- [GitLab manual webhooks](https://docs.aws.amazon.com/codebuild/latest/userguide/gitlab-manual-webhook.html): You can configure manual GitLab webhooks to prevent CodeBuild from automatically attempting to create a webhook within GitLab.

### [GitLab webhook events](https://docs.aws.amazon.com/codebuild/latest/userguide/gitlab-webhook.html)

You can use webhook filter groups to specify which GitLab webhook events trigger a build.

- [Filter GitLab webhook events (console)](https://docs.aws.amazon.com/codebuild/latest/userguide/gitlab-webhook-events-console.html): Use the following instructions to use the AWS Management Console to filter webhook events.
- [Filter GitLab webhook events (SDK)](https://docs.aws.amazon.com/codebuild/latest/userguide/gitlab-webhook-events-sdk.html): To use the AWS CodeBuild SDK to filter webhook events, use the filterGroups field in the request syntax of the CreateWebhook or UpdateWebhook API methods.
- [Filter GitLab webhook events (CloudFormation)](https://docs.aws.amazon.com/codebuild/latest/userguide/gitlab-webhook-events-cfn.html): To use an CloudFormation template to filter webhook events, use the AWS CodeBuild project's FilterGroups property.
- [Buildkite manual webhooks](https://docs.aws.amazon.com/codebuild/latest/userguide/buildkite-manual-webhook.html): Currently, CodeBuild requires all Buildkite webhooks to be created manually.
- [Pull request comment approval](https://docs.aws.amazon.com/codebuild/latest/userguide/pull-request-build-policy.html): CodeBuild supports pull request build policies that provide additional control over builds triggered by pull requests.
- [View build project details](https://docs.aws.amazon.com/codebuild/latest/userguide/view-project-details.html): Describes how to view a build project's details in AWS CodeBuild.
- [View build project names](https://docs.aws.amazon.com/codebuild/latest/userguide/view-project-list.html): Describes how to view a list of build project names in AWS CodeBuild.


## [Builds](https://docs.aws.amazon.com/codebuild/latest/userguide/builds-working.html)

### [Run builds manually](https://docs.aws.amazon.com/codebuild/latest/userguide/run-build.html)

Describes how to run a build in AWS CodeBuild.

- [Run a build locally](https://docs.aws.amazon.com/codebuild/latest/userguide/use-codebuild-agent.html): Provides information about how to build locally with the AWS CodeBuild agent.
- [Run a build (console)](https://docs.aws.amazon.com/codebuild/latest/userguide/run-build-console.html): To use AWS CodePipeline to run a build with CodeBuild, skip these steps and follow the instructions in .
- [Run a build (AWS CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/run-build-cli.html)
- [Run a batch build (AWS CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/run-batch-build-cli.html): Describes how to run a batch build in AWS CodeBuild.
- [Start running builds automatically (AWS CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/run-build-cli-auto-start.html): If your source code is stored in a GitHub or a GitHub Enterprise Server repository, you can use GitHub webhooks to have AWS CodeBuild rebuild your source code whenever a code change is pushed to the repository.
- [Stop running builds automatically (AWS CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/run-build-cli-auto-stop.html): If your source code is stored in a GitHub or a GitHub Enterprise Server repository, you can set up GitHub webhooks to have AWS CodeBuild rebuild your source code whenever a code change is pushed to the repository.
- [Run a build (AWS SDKs)](https://docs.aws.amazon.com/codebuild/latest/userguide/run-build-sdks.html): To use CodePipeline to run a build with AWS CodeBuild, skip these steps and follow the instructions in instead.

### [Run builds on Lambda compute](https://docs.aws.amazon.com/codebuild/latest/userguide/lambda.html)

Learn about the AWS Lambda compute in AWS CodeBuild.

- [Deploy a Lambda function using AWS SAM with CodeBuild Lambda Java](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-lambda-sam-gradle.html): Provides information about deploying a Lambda function using AWS SAM with CodeBuild Lambda Java.
- [Create a single page React app with CodeBuild Lambda Node.js](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-lambda-react-nodejs.html): Provides information about creating a single page React app with CodeBuild Lambda Node.js
- [Update a Lambda function configuration with CodeBuild Lambda Python](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-lambda-boto3-python.html): Provides information about updating a Lambda function configuration with CodeBuild Lambda Python.

### [Run builds on reserved capacity fleets](https://docs.aws.amazon.com/codebuild/latest/userguide/fleets.html)

How to configure and use reserved capacity fleets in CodeBuild.

- [Reserved capacity fleet properties](https://docs.aws.amazon.com/codebuild/latest/userguide/fleets.reserved-capacity-fleets.html): A reserved capacity fleet contains the following properties.
- [Reserved capacity samples](https://docs.aws.amazon.com/codebuild/latest/userguide/reserved-capacity-samples.html): Learn how to use reserved capacity fleets in your CodeBuild project.
- [Run batch builds](https://docs.aws.amazon.com/codebuild/latest/userguide/batch-build.html): Learn about batch builds in AWS CodeBuild.

### [Execute parallel tests](https://docs.aws.amazon.com/codebuild/latest/userguide/parallel-test.html)

Learn about parallel tests in AWS CodeBuild.

- [Enable parallel test execution in batch builds](https://docs.aws.amazon.com/codebuild/latest/userguide/parallel-test-enable.html): To run tests in parallel, update the batch build buildspec file to include the build-fanout field and the number of parallel builds to split the test suite in the parallelism field as shown below.
- [Use the codebuild-tests-run CLI command](https://docs.aws.amazon.com/codebuild/latest/userguide/parallel-test-tests-run.html): AWS CodeBuild provides CLI that will take test command and test file location as input.
- [Use the codebuild-glob-search CLI command](https://docs.aws.amazon.com/codebuild/latest/userguide/parallel-test-glob-search.html): AWS CodeBuild provides a built-in CLI tool called codebuild-glob-search that allows you to search for files in your working directory based on one or more glob patterns.
- [About test splitting](https://docs.aws.amazon.com/codebuild/latest/userguide/parallel-test-splitting.html): AWS CodeBuild's test splitting feature allows you to parallelize your test suite execution across multiple compute instances, reducing the overall test run time.
- [Automatically merge individual build reports](https://docs.aws.amazon.com/codebuild/latest/userguide/parallel-test-auto-merge.html): In fanout batch builds, AWS CodeBuild supports automatic merging of individual build reports into a consolidated batch-level report.

### [Parallel test execution samples](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-parallel-test.html)

Demonstrates how to use the codebuild-tests-run command to split and run your tests across parallel execution environments.

- [Configure parallel tests with Django](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-parallel-test-django.html): The following is sample of a buildspec.yml that shows parallel test execution with Django on an Ubuntu platform:
- [Configure parallel tests with Elixir](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-parallel-test-elixir.html): The following is sample of a buildspec.yml that shows parallel test execution with Elixir on an Ubuntu platform:
- [Configure parallel tests with Go](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-parallel-test-go.html): The following is sample of a buildspec.yml that shows parallel test execution with Go on an Linux platform:
- [Configure parallel tests withJava (Maven)](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-parallel-test-java-maven.html): The following is sample of a buildspec.yml that shows parallel test execution with Java on an Linux platform:
- [Configure parallel tests with Javascript (Jest)](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-parallel-test-javascript.html): The following is sample of a buildspec.yml that shows parallel test execution with Javascript on an Ubuntu platform:
- [Configure parallel tests with Kotlin](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-parallel-test-kotlin.html): The following is sample of a buildspec.yml that shows parallel test execution with Kotlin on an Linux platform:
- [Configure parallel tests with PHPUnit](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-parallel-test-phpunit.html): The following is sample of a buildspec.yml that shows parallel test execution with PHPUnit on an Linux platform:
- [Configure parallel tests with Pytest](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-parallel-test-python.html): The following is sample of a buildspec.yml that shows parallel test execution with Pytest on an Ubuntu platform:
- [Configure parallel tests with Ruby (Cucumber)](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-parallel-test-ruby-cucumber.html): The following is sample of a buildspec.yml that shows parallel test execution with Cucumber on an Linux platform:
- [Configure parallel tests with Ruby (RSpec)](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-parallel-test-ruby.html): The following is sample of a buildspec.yml that shows parallel test execution with RSpec on an Ubuntu platform:

### [Cache builds](https://docs.aws.amazon.com/codebuild/latest/userguide/build-caching.html)

Learn about caching in AWS CodeBuild.

- [Amazon S3 caching](https://docs.aws.amazon.com/codebuild/latest/userguide/caching-s3.html): Amazon S3 caching stores the cache in an Amazon S3 bucket that is available across multiple build hosts.
- [Local caching](https://docs.aws.amazon.com/codebuild/latest/userguide/caching-local.html): Local caching stores a cache locally on a build host that is available to that build host only.
- [Specify a local cache](https://docs.aws.amazon.com/codebuild/latest/userguide/specify-caching-local.html): You can use the AWS CLI, console, SDK, or CloudFormation to specify a local cache.

### [Debug builds](https://docs.aws.amazon.com/codebuild/latest/userguide/debug-builds.html)

Learn how to debug builds in AWS CodeBuild.

### [Debug builds with CodeBuild sandbox](https://docs.aws.amazon.com/codebuild/latest/userguide/sandbox.html)

Use CodeBuild sandbox to debug a running CodeBuild build.

- [Tutorial: Connecting to a sandbox using SSH](https://docs.aws.amazon.com/codebuild/latest/userguide/sandbox-ssh-tutorial.html): This tutorial shows you how to connect to a CodeBuild sandbox using an SSH client.
- [Troubleshooting AWS CodeBuild sandbox SSH connection issues](https://docs.aws.amazon.com/codebuild/latest/userguide/sandbox-troubleshooting.html): Use the information in this topic to help you identify, diagnose, and address CodeBuild sandbox SSH connection issues.
- [Debug builds with Session Manager](https://docs.aws.amazon.com/codebuild/latest/userguide/session-manager.html): Use Session Manager to debug a running CodeBuild build.
- [Delete builds](https://docs.aws.amazon.com/codebuild/latest/userguide/delete-builds.html): Describes how to delete builds in AWS CodeBuild.
- [Retry builds manually](https://docs.aws.amazon.com/codebuild/latest/userguide/retry-build.html): Describes how to retry a build manually in AWS CodeBuild.
- [Retry builds automatically](https://docs.aws.amazon.com/codebuild/latest/userguide/auto-retry-build.html): Describes how to automatically retry a build in AWS CodeBuild.
- [Stop builds](https://docs.aws.amazon.com/codebuild/latest/userguide/stop-build.html): Describes how to stop a build in AWS CodeBuild.
- [Stop batch builds](https://docs.aws.amazon.com/codebuild/latest/userguide/stop-batch-build.html): Describes how to stop a batch build in AWS CodeBuild.

### [Trigger builds automatically](https://docs.aws.amazon.com/codebuild/latest/userguide/build-triggers.html)

Learn about build triggers in AWS CodeBuild.

- [Edit build triggers](https://docs.aws.amazon.com/codebuild/latest/userguide/triggers-edit.html): Specifies how to edit AWS CodeBuild triggers.

### [View build details](https://docs.aws.amazon.com/codebuild/latest/userguide/view-build-details.html)

Describes how to get details about builds managed by AWS CodeBuild.

- [Build phase transitions](https://docs.aws.amazon.com/codebuild/latest/userguide/view-build-details-phases.html): Builds in AWS CodeBuild proceed in phases:
- [View build IDs](https://docs.aws.amazon.com/codebuild/latest/userguide/view-build-list.html): Describes how to get a list of build IDs managed by AWS CodeBuild.
- [View build IDs for a build project](https://docs.aws.amazon.com/codebuild/latest/userguide/view-builds-for-project.html): Describes how to view a list of build IDs for a build project in AWS CodeBuild.


## [Test reports](https://docs.aws.amazon.com/codebuild/latest/userguide/test-reporting.html)

- [Create test reports](https://docs.aws.amazon.com/codebuild/latest/userguide/report-create.html): To create a test report, you run a build project that is configured with one to five report groups in its buildspec file.
- [Create code coverage reports](https://docs.aws.amazon.com/codebuild/latest/userguide/code-coverage-report.html): Generate a code coverage report in CodeBuild.
- [Discover reports automatically](https://docs.aws.amazon.com/codebuild/latest/userguide/report-auto-discover.html): Auto-discover reports in CodeBuild.

### [Report groups](https://docs.aws.amazon.com/codebuild/latest/userguide/test-report-group.html)

A report group contains test reports and specifies shared settings.

- [Create a report group](https://docs.aws.amazon.com/codebuild/latest/userguide/report-group-create.html): You can use the CodeBuild console, the AWS CLI, or a buildspec file to create a report group.
- [Report group naming](https://docs.aws.amazon.com/codebuild/latest/userguide/test-report-group-naming.html): When you use the AWS CLI or the AWS CodeBuild console to create a report group, you specify a name for the report group.

### [Share report groups](https://docs.aws.amazon.com/codebuild/latest/userguide/report-groups-sharing.html)

Learn how to share report groups.

- [Access shared report groups](https://docs.aws.amazon.com/codebuild/latest/userguide/report-groups-sharing-access-prereqs.html): To access a shared report group, a consumer's IAM role requires the BatchGetReportGroups permission.
- [Unshare a shared report group](https://docs.aws.amazon.com/codebuild/latest/userguide/report-groups-sharing-unshare.html): An unshared report group, including its reports and their test case results, can be accessed only by its owner.
- [Identify a shared report group](https://docs.aws.amazon.com/codebuild/latest/userguide/report-groups-sharing-identify.html): Owners and consumers can use the AWS CLI to identify shared report groups.
- [Shared report group permissions](https://docs.aws.amazon.com/codebuild/latest/userguide/report-groups-sharing-perms.html)
- [Specify test files](https://docs.aws.amazon.com/codebuild/latest/userguide/report-group-test-cases.html): You specify the test result files and their location for each report group in the reports section of your build project's buildspec file.
- [Specify test commands](https://docs.aws.amazon.com/codebuild/latest/userguide/report-group-test-case-commands.html): You specify the commands that run your test cases in the commands section of your buildspec file.

### [Tag a report group](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-tag-report-group.html)

Describes how to tag resources in AWS CodeCommit.

- [Add tags to a report group](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-tag-report-group-add.html): Adding tags to a report group can help you identify and organize your AWS resources and manage access to them.
- [View tags for a report group](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-tag-report-group-list.html): Tags can help you identify and organize your AWS resources and manage access to them.
- [Edit tags for a report group](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-tag-report-group-update.html): You can change the value for a tag associated with a report group.
- [Remove tags from a report group](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-tag-report-group-delete.html): You can remove one or more tags associated with a report group.
- [Update a report group](https://docs.aws.amazon.com/codebuild/latest/userguide/report-group-export-settings.html): When you update a report group, you can specify information about whether to export the raw test result data to files in an Amazon S3 bucket.

### [Test frameworks](https://docs.aws.amazon.com/codebuild/latest/userguide/test-framework-reporting.html)

Set up test reporting in AWS CodeBuild using various test frameworks, including Jasmine, Jest, pytest, and RSpec.

- [Set up Jasmine](https://docs.aws.amazon.com/codebuild/latest/userguide/test-report-jasmine.html): Set up test reporting in CodeBuild with the Jasmine testing framework.
- [Set up Jest](https://docs.aws.amazon.com/codebuild/latest/userguide/test-report-jest.html): Set up test reporting in CodeBuild with the Jest testing framework.
- [Set up pytest](https://docs.aws.amazon.com/codebuild/latest/userguide/test-report-pytest.html): Set up test reporting in CodeBuild with the pytest testing framework.
- [Set up RSpec](https://docs.aws.amazon.com/codebuild/latest/userguide/test-report-rspec.html): Set up test reporting in CodeBuild with the RSpec testing framework.

### [View test reports](https://docs.aws.amazon.com/codebuild/latest/userguide/test-view-reports.html)

You can view details about a test report, such as information about its test cases, pass and fail numbers, and how long it took for it to run.

- [View test reports for a build](https://docs.aws.amazon.com/codebuild/latest/userguide/test-view-project-reports.html)
- [View test reports for a report group](https://docs.aws.amazon.com/codebuild/latest/userguide/test-view-report-group-reports.html)
- [View test reports in your AWS account](https://docs.aws.amazon.com/codebuild/latest/userguide/test-view-account-reports.html)
- [Test report permissions](https://docs.aws.amazon.com/codebuild/latest/userguide/test-permissions.html): This topic describes important information about permissions related to test reporting.
- [Test report statuses](https://docs.aws.amazon.com/codebuild/latest/userguide/test-report.html): The status of a test report can be one of the following:


## [VPC support](https://docs.aws.amazon.com/codebuild/latest/userguide/vpc-support.html)

- [Allow Amazon VPC access in your CodeBuild projects](https://docs.aws.amazon.com/codebuild/latest/userguide/enabling-vpc-access-in-projects.html): Include these settings in your VPC configuration:
- [Troubleshoot your VPC setup](https://docs.aws.amazon.com/codebuild/latest/userguide/troubleshooting-vpc.html): Use the information that appears in the error message to help you identify, diagnose, and address issues.
- [Use VPC endpoints](https://docs.aws.amazon.com/codebuild/latest/userguide/use-vpc-endpoints-with-codebuild.html): You can improve the security of your builds by configuring AWS CodeBuild to use an interface VPC endpoint.
- [Use a CodeBuild managed proxy server](https://docs.aws.amazon.com/codebuild/latest/userguide/run-codebuild-in-managed-proxy-server.html): To run AWS CodeBuild reserved capacity fleets in a managed proxy server, you must configure the proxy server to allow or deny traffic to and from external sites using proxy rules.

### [Use a proxy server](https://docs.aws.amazon.com/codebuild/latest/userguide/use-proxy-server.html)

Provides information about how to use CodeBuild with a proxy server.

- [Set up components required to run CodeBuild in a proxy server](https://docs.aws.amazon.com/codebuild/latest/userguide/use-proxy-server-transparent-components.html): You need these components to run AWS CodeBuild in a transparent or explicit proxy server:
- [Run CodeBuild in an explicit proxy server](https://docs.aws.amazon.com/codebuild/latest/userguide/run-codebuild-in-explicit-proxy-server.html): To run AWS CodeBuild in an explicit proxy server, you must configure the proxy server to allow or deny traffic to and from external sites, and then configure the HTTP_PROXY and HTTPS_PROXY environment variables.
- [Run CodeBuild in a transparent proxy server](https://docs.aws.amazon.com/codebuild/latest/userguide/run-codebuild-in-transparent-proxy-server.html): To run AWS CodeBuild in a transparent proxy server, you must configure the proxy server with access to the websites and domains it interacts with.
- [Run a package manager and other tools in a proxy server](https://docs.aws.amazon.com/codebuild/latest/userguide/use-proxy-server-tools.html): Use the following procedures to run a package manager and other tools in a proxy server.
- [CloudFormation VPC template](https://docs.aws.amazon.com/codebuild/latest/userguide/cloudformation-vpc-template.html): An CloudFormation template to create and provision a VPC to use AWS CodeBuild.


## [Logging and monitoring](https://docs.aws.amazon.com/codebuild/latest/userguide/logging-monitoring.html)

### [Log CodeBuild API calls](https://docs.aws.amazon.com/codebuild/latest/userguide/cloudtrail.html)

Learn about logging CodeBuild with AWS CloudTrail.

- [About AWS CodeBuild information in CloudTrail](https://docs.aws.amazon.com/codebuild/latest/userguide/service-name-info-in-cloudtrail.html): CloudTrail is enabled on your AWS account when you create the account.
- [About AWS CodeBuild log file entries](https://docs.aws.amazon.com/codebuild/latest/userguide/understanding-service-name-entries.html): A trail is a configuration that enables delivery of events as log files to an S3 bucket that you specify.

### [Monitor builds](https://docs.aws.amazon.com/codebuild/latest/userguide/monitoring-builds.html)

Describes how to monitor AWS CodeBuild builds with Amazon CloudWatch.

- [CloudWatch metrics](https://docs.aws.amazon.com/codebuild/latest/userguide/cloudwatch_metrics-codebuild.html): The following metrics can be tracked per AWS account or build project.
- [CloudWatch resource utilization metrics](https://docs.aws.amazon.com/codebuild/latest/userguide/cloudwatch-utilization-metrics.html)
- [CloudWatch dimensions](https://docs.aws.amazon.com/codebuild/latest/userguide/codebuild-cloudwatch-dimensions.html): CodeBuild provides the following CloudWatch metric dimensions.
- [CloudWatch alarms](https://docs.aws.amazon.com/codebuild/latest/userguide/codebuild_cloudwatch_alarms.html): You can use the CloudWatch console to create alarms based on CodeBuild metrics so you can react if something goes wrong with your builds.
- [View CodeBuild metrics](https://docs.aws.amazon.com/codebuild/latest/userguide/monitoring-metrics.html): View AWS CodeBuild metrics using CloudWatch or CodeBuild.
- [View CodeBuild resource utilization metrics](https://docs.aws.amazon.com/codebuild/latest/userguide/monitoring-utilization-metrics.html): View AWS CodeBuild resource utilization metrics using CloudWatch or CodeBuild.
- [Create CodeBuild alarms in CloudWatch](https://docs.aws.amazon.com/codebuild/latest/userguide/monitoring-alarms.html): Create CloudWatch alarms for AWS CodeBuild.


## [Security](https://docs.aws.amazon.com/codebuild/latest/userguide/security.html)

### [Data protection](https://docs.aws.amazon.com/codebuild/latest/userguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in CodeBuild.

- [Data encryption](https://docs.aws.amazon.com/codebuild/latest/userguide/security-encryption.html): Encryption is an important part of CodeBuild security.
- [Key management](https://docs.aws.amazon.com/codebuild/latest/userguide/security-key-management.html): You can protect your content from unauthorized use through encryption.
- [Traffic privacy](https://docs.aws.amazon.com/codebuild/latest/userguide/security-traffic-privacy.html): You can improve the security of your builds by configuring CodeBuild to use an interface VPC endpoint.

### [Identity and access management](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control.html)

Control user access using IAM policies to specify which AWS CodeBuild actions a user in your AWS account can perform.

- [Overview of managing access](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html): Describes how account administrators can manage access to resources by attaching permissions policies to IAM identities.
- [Using identity-based policies](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html): Provides examples of IAM identity-based policies for controlling access to AWS CodeBuild.
- [AWS CodeBuild permissions reference](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-permissions-reference.html): Describes the AWS CodeBuild API operations and the corresponding actions you grant permissions to perform.
- [Using tags to control access to AWS CodeBuild resources](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-using-tags.html): Conditions in IAM policy statements are part of the syntax that you can use to specify permissions to CodeBuild project-based actions.
- [Viewing resources in the console](https://docs.aws.amazon.com/codebuild/latest/userguide/console-resources.html): Describes permissions required to view resources in the console for CodeBuild.
- [Compliance validation](https://docs.aws.amazon.com/codebuild/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/codebuild/latest/userguide/codebuild-disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS CodeBuild features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/codebuild/latest/userguide/infrastructure-security.html): Learn how AWS CodeBuild isolates service traffic.

### [Source provider access](https://docs.aws.amazon.com/codebuild/latest/userguide/access-tokens.html)

Provides information about how to use a personal access token, app password, a Secrets Manager secret, a connection, or OAuth app in AWS CodeBuild to connect to GitHub or Bitbucket.

- [Create and store a token in a Secrets Manager secret](https://docs.aws.amazon.com/codebuild/latest/userguide/asm-create-secret.html): If you choose to use to store your access token using Secrets Manager, you can use either an existing secret connection or create a new secret.

### [GitHub and GitHub Enterprise Server access](https://docs.aws.amazon.com/codebuild/latest/userguide/access-tokens-github-overview.html)

Provides information about how to use a personal access token, a Secrets Manager secret, OAuth app, or GitHub App in AWS CodeBuild to connect to GitHub or GitHub Enterprise.

- [GitHub App connections](https://docs.aws.amazon.com/codebuild/latest/userguide/connections-github-app.html): Create a connection to GitHub App using the CodeBuild console or the AWS CLI.
- [GitHub and GitHub Enterprise Server access token](https://docs.aws.amazon.com/codebuild/latest/userguide/access-tokens-github.html)
- [GitHub OAuth app](https://docs.aws.amazon.com/codebuild/latest/userguide/oauth-app-github.html)

### [Bitbucket access](https://docs.aws.amazon.com/codebuild/latest/userguide/access-tokens-bitbucket-overview.html)

Provides information about how to use an access token, an app password, an OAuth app, or a Bitbucket connection in AWS CodeBuild to connect to Bitbucket.

- [Bitbucket App connections](https://docs.aws.amazon.com/codebuild/latest/userguide/connections-bitbucket-app.html): Create a connection to Bitbucket App using the AWS Management Console or the AWS CLI.
- [Bitbucket app password or access token](https://docs.aws.amazon.com/codebuild/latest/userguide/access-tokens-bitbucket.html)
- [Bitbucket OAuth app](https://docs.aws.amazon.com/codebuild/latest/userguide/oauth-app-bitbucket.html)
- [GitLab access](https://docs.aws.amazon.com/codebuild/latest/userguide/access-tokens-gitlab-overview.html): Provides information about how to use a GitLab connection in AWS CodeBuild to connect to GitLab
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/codebuild/latest/userguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.


## [Advanced topics](https://docs.aws.amazon.com/codebuild/latest/userguide/advanced-topics.html)

- [Allow users to interact with CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/setting-up-service-permissions-group.html): If you follow the steps in to access AWS CodeBuild for the first time, you most likely do not need the information in this topic.
- [Allow CodeBuild to interact with other AWS services](https://docs.aws.amazon.com/codebuild/latest/userguide/setting-up-service-role.html): If you follow the steps in to access AWS CodeBuild for the first time, you most likely do not need the information in this topic.
- [Encrypt build outputs](https://docs.aws.amazon.com/codebuild/latest/userguide/setting-up-kms.html): If you follow the steps in to access AWS CodeBuild for the first time, you most likely do not need the information in this topic.
- [Interact with CodeBuild using the AWS CLI](https://docs.aws.amazon.com/codebuild/latest/userguide/setting-up-cli.html): If you follow the steps in to access AWS CodeBuild for the first time, you most likely do not need the information in this topic.
- [Command line reference](https://docs.aws.amazon.com/codebuild/latest/userguide/cmd-ref.html): Provides information about working with the AWS Command Line Interface (AWS CLI) to automate AWS CodeBuild.
- [AWS SDKs and tools reference](https://docs.aws.amazon.com/codebuild/latest/userguide/sdk-ref.html): Provides information about working with the AWS SDKs and tools for CodeBuild.
- [Working with AWS SDKs](https://docs.aws.amazon.com/codebuild/latest/userguide/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.
- [Specify the CodeBuild endpoint](https://docs.aws.amazon.com/codebuild/latest/userguide/endpoint-specify.html): Describes how to specify the endpoint used by AWS CodeBuild.

### [Use CodeBuild with CodePipeline](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-create-pipeline.html)

Demonstrates how to use AWS CodePipeline with AWS CodeBuild to automate builds.

- [Create a pipeline (console)](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-create-pipeline-console.html): Use the following procedure to create a pipeline that uses CodeBuild to build and deploy your source code.
- [Create a pipeline (AWS CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-create-pipeline-cli.html): Use the following procedure to create a pipeline that uses CodeBuild to build your source code.
- [Add a build action](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-create-pipeline-add.html)
- [Add a test action](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-create-pipeline-add-test.html)
- [Use CodeBuild with Codecov](https://docs.aws.amazon.com/codebuild/latest/userguide/codecov-integration.html): Describes how to use CodeBuild with Codecov and upload reports and test cases to a CodeCov account for analysis.
- [Use CodeBuild with Jenkins](https://docs.aws.amazon.com/codebuild/latest/userguide/jenkins-plugin.html): Introduces the AWS CodeBuild Jenkins plugin, which you can use to run builds in CodeBuild from your Jenkins server.
- [Use CodeBuild with serverless apps](https://docs.aws.amazon.com/codebuild/latest/userguide/serverless-applications.html): Provides information about building serverless applications with AWS CodeBuild.
- [Third party notices](https://docs.aws.amazon.com/codebuild/latest/userguide/notice.html): Provides third party legal terms that govern the use of third-party packages and modules for using AWS CodeBuild for Windows.
- [Use CodeBuild condition keys as IAM service role variables](https://docs.aws.amazon.com/codebuild/latest/userguide/permissions-conditionkeys-variables.html): Provides information about using build project ARN IAM variables to scope resource access.
- [AWS CodeBuild condition keys](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html): Provides information about using context keys to customize IAM policies.


## [Code examples](https://docs.aws.amazon.com/codebuild/latest/userguide/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/codebuild/latest/userguide/service_code_examples_basics.html)

The following code examples show how to use the basics of CodeBuild with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/codebuild/latest/userguide/service_code_examples_actions.html)

The following code examples show how to use CodeBuild with AWS SDKs.

- [CreateProject](https://docs.aws.amazon.com/codebuild/latest/userguide/example_codebuild_CreateProject_section.html): Use CreateProject with an AWS SDK or CLI
- [ListBuilds](https://docs.aws.amazon.com/codebuild/latest/userguide/example_codebuild_ListBuilds_section.html): Use ListBuilds with an AWS SDK or CLI
- [ListProjects](https://docs.aws.amazon.com/codebuild/latest/userguide/example_codebuild_ListProjects_section.html): Use ListProjects with an AWS SDK or CLI
- [StartBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/example_codebuild_StartBuild_section.html): Use StartBuild with an AWS SDK or CLI
