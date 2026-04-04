# Source: https://docs.aws.amazon.com/codepipeline/latest/userguide/llms.txt

# AWS CodePipeline User Guide

> A user guide that describes how developers can use AWS CodePipeline to model, visualize, and automate the steps required to release software.

- [Getting started](https://docs.aws.amazon.com/codepipeline/latest/userguide/getting-started-codepipeline.html)
- [Best practices and use cases](https://docs.aws.amazon.com/codepipeline/latest/userguide/best-practices.html)
- [Use CodePipeline with Amazon VPC](https://docs.aws.amazon.com/codepipeline/latest/userguide/vpc-support.html)
- [](https://docs.aws.amazon.com/codepipeline/latest/userguide/change-detection-methods.html)
- [Configure conditions for a stage](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html)
- [Working with stage transitions](https://docs.aws.amazon.com/codepipeline/latest/userguide/transitions.html)
- [Troubleshooting](https://docs.aws.amazon.com/codepipeline/latest/userguide/troubleshooting.html)
- [Integration model reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-integrations.html)
- [Image definitions file reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/file-reference.html)
- [Variables reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-variables.html)
- [Working with glob patterns in syntax](https://docs.aws.amazon.com/codepipeline/latest/userguide/syntax-glob.html)
- [Update polling pipelines to the recommended change detection method](https://docs.aws.amazon.com/codepipeline/latest/userguide/trigger-S3-migration-cwe.html)
- [Update a GitHub (via OAuth app) source action to a GitHub (via GitHub App) source action](https://docs.aws.amazon.com/codepipeline/latest/userguide/update-github-action-connections.html)
- [Quotas](https://docs.aws.amazon.com/codepipeline/latest/userguide/limits.html)
- [Appendix A: GitHub (via OAuth app) source actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/appendix-github-oauth.html)
- [Document history](https://docs.aws.amazon.com/codepipeline/latest/userguide/history.html)
- [CodePipeline feature reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/feature-reference.html)

## [What is CodePipeline?](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)

- [Continuous delivery and continuous integration](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-continuous-delivery-integration.html): CodePipeline is a continuous delivery service that automates the building, testing, and deployment of your software into production.
- [What can I do with CodePipeline?](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome-what-can-I-do.html): You can use CodePipeline to help you automatically build, test, and deploy your applications in the cloud.
- [A quick look at CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome-introducing.html)
- [How do I get started with CodePipeline?](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome-get-started.html): To get started with CodePipeline:
- [Concepts](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html): Provides important conceptual details about CodePipeline.
- [DevOps pipeline example](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-devops-example.html): As an example of a DevOps pipeline, a two-stage pipeline might have a source stage called Source and a second stage called Prod.
- [How pipeline executions work](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works.html): This section provides an overview of the way CodePipeline processes a set of changes.
- [Input and output artifacts](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome-introducing-artifacts.html): CodePipeline integrates with development tools to check for code changes and then build and deploy through all of the stages of the continuous delivery process.
- [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html): For each condition that specifies a rule, the rule is run.
- [Pipeline types](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-types.html): CodePipeline provides the following pipeline types, which differ in characteristics and price, so that you can tailor your pipeline features and cost to the needs of your applications.
- [What type of pipeline is right for me?](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-types-planning.html): The pipeline type is determined by the set of characteristics and features supported by each pipeline version.


## [Product and service integrations](https://docs.aws.amazon.com/codepipeline/latest/userguide/integrations.html)

- [Integrations with CodePipeline action types](https://docs.aws.amazon.com/codepipeline/latest/userguide/integrations-action-type.html): Learn about CodePipeline integrations with other AWS services and AWS Partner products and services based on action type.
- [General integrations with CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/integrations-general.html): Learn about CodePipeline integrations with other AWS services that are not based on action types.

### [Examples from the community](https://docs.aws.amazon.com/codepipeline/latest/userguide/integrations-community.html)

Learn more about CodePipeline integrations through blog posts, articles, and community-provided examples.

- [Blog posts](https://docs.aws.amazon.com/codepipeline/latest/userguide/integrations-community-blogposts.html)


## [Tutorials](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials.html)

- [Tutorial: Deploy to Amazon EC2 instances with CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-ec2-deploy.html): This tutorial helps you to create a deploy action in CodePipeline that deploys your code to instances you have configured in Amazon EC2.
- [Tutorial: Build and push a Docker image to Amazon ECR with CodePipeline (V2 type)](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-ecr-build-publish.html): This tutorial helps you to create a build action in CodePipeline that runs and pushes your Docker image to Amazon ECR after a change to your source code.
- [Tutorial: Deploy to Amazon EKS with CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-eks-deploy.html): This tutorial helps you to create a deploy action in CodePipeline that deploys your code to a cluster you have configured in Amazon EKS.
- [Tutorial: Create a pipeline that runs commands with compute (V2 type)](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-commands.html): Describes how to use the console to create a pipeline that uses GitHub as a source and uses the Commands action to run shell commands
- [Tutorial: Use Git tags to start your pipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-github-tags.html): Add a GitHub source action in CodePipeline that is configured with the trigger type for Git tags.
- [Tutorial: Filter on branch names for pull requests to start your pipeline (V2 type)](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-github-featurebranches.html): In this tutorial, you will create a pipeline that connects to your GitHub.com repository where the source action is configured to start your pipeline with a trigger configuration that filters on pull requests.
- [Tutorial: Use pipeline-level variables](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-pipeline-variables.html): Create a pipeline with a CodeCommit source action and a CodeBuild build action in CodePipeline where the pipeline uses an example variable at the pipeline level.
- [Tutorial: Create a simple pipeline (S3 bucket)](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-simple-s3.html): Follow the steps in this CodePipeline tutorial to create a simple two-stage pipeline using an S3 bucket as a code repository.
- [Tutorial: Create a simple pipeline (CodeCommit repository)](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-simple-codecommit.html): Follow the steps in this CodePipeline tutorial to create a simple two-stage pipeline using a CodeCommit repository as your code source.
- [Tutorial: Create a four-stage pipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-four-stage-pipeline.html): Follow the steps in this CodePipeline tutorial to create a four-stage pipeline that uses a GitHub repository for your source, a Jenkins build server to build the project, and a CodeDeploy application to deploy the built code to a staging server.
- [Tutorial: Set up a CloudWatch Events rule to receive email notifications for pipeline state changes](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-cloudwatch-sns-notifications.html): Follow the steps in this CodePipeline tutorial to create a CloudWatch Events notification rule for CodePipeline that targets Amazon SNS.
- [Tutorial: Build and test an Android app with AWS Device Farm](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-codebuild-devicefarm.html): Learn how to use AWS CodePipeline to build your Android app with CodeBuild and test it with AWS Device Farm every time you push a commit to your GitHub repository.
- [Tutorial: Test an iOS app with AWS Device Farm](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-codebuild-devicefarm-S3.html): Learn how to use AWS CodePipeline to test your iOS app with AWS Device Farm every time you save a change in your S3 source bucket.
- [Tutorial: Create a pipeline that deploys to Service Catalog](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-S3-servicecatalog.html): Learn how to use AWS CodePipeline to deploy to Service Catalog.

### [Tutorial: Create a pipeline with AWS CloudFormation](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-cloudformation.html)

Learn how to use AWS CloudFormation to create a pipeline that deploys your application to your instances each time the source code changes.

- [Example 1: Create an AWS CodeCommit pipeline with AWS CloudFormation](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-cloudformation-codecommit.html): This walkthrough shows you how to use the AWS CloudFormation console to create infrastructure that includes a pipeline connected to a CodeCommit source repository.
- [Example 2: Create an Amazon S3 pipeline with AWS CloudFormation](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-cloudformation-s3.html): This walkthrough shows you how to use the AWS CloudFormation console to create infrastructure that includes a pipeline connected to an Amazon S3 source bucket.
- [Tutorial: Create a pipeline that uses variables from AWS CloudFormation deployment actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-cloudformation-action.html): Learn how to use AWS CloudFormation to create a pipeline that deploys a CloudFormation template that creates and then deletes a stack.
- [Tutorial: Amazon ECS Standard Deployment with CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/ecs-cd-pipeline.html): This tutorial helps you to create a complete, end-to-end continuous deployment (CD) pipeline with Amazon ECS with CodePipeline.
- [Tutorial: Create a pipeline with an Amazon ECR source and ECS-to-CodeDeploy deployment](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-ecs-ecr-codedeploy.html): Describes how to use the console to create a pipeline with an Amazon ECR source and ECS-to-CodeDeploy deployment.
- [Tutorial: Create a pipeline that deploys an Amazon Alexa skill](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-alexa-skills-kit.html): Describes how to use the console to create a pipeline that uses Alexa Skills Kit as the deployment provider.
- [Tutorial: Create a pipeline that uses Amazon S3 as a deployment provider](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-s3deploy.html): Describes how to use the console to create a pipeline that uses Amazon S3 as the deployment provider.
- [Tutorial: Publish applications to the AWS Serverless Application Repository](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-serverlessrepo-auto-publish.html): Learn how to use AWS CodePipeline to continuously publish your serverless application to AWS Serverless Application Repository.
- [Tutorial: Lambda function deployments with CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-lambda-deploy.html): This tutorial helps you to create a deploy action in CodePipeline that deploys your code to your function you have configured in Lambda.
- [Tutorial: Using variables with Lambda invoke actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-lambda-variables.html): A Lambda invoke action can use variables from another action as part of its input and return new variables along with its output.
- [Tutorial: Use an AWS Step Functions invoke action](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-step-functions.html): Add an AWS Step Functions invoke action in CodePipeline to activate state machine executions from a pipeline.
- [Tutorial: Create a pipeline that uses AppConfig as a deployment provider](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-AppConfig.html): Describes how to use the console to create a pipeline that uses AWS AppConfig as the deployment provider.
- [Tutorial: Use full clone with a GitHub pipeline source](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-github-gitclone.html): Add a GitHub source action in CodePipeline to run CodeBuild commands for Git metadata in your pipeline build action.
- [Tutorial: Use full clone with a CodeCommit pipeline source](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-codecommit-gitclone.html): Add a CodeCommit source action in CodePipeline to allow CodeBuild to access Git metadata in your pipeline build action.
- [Tutorial: Create a pipeline with AWS CloudFormation StackSets deployment actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-stackset-deployment.html): Learn how to use AWS CloudFormation to create a pipeline that deploys a CloudFormation stack set and then creates and updates stack instances for the deployment.
- [Create a variable check rule for a pipeline as an entry condition](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-varcheckrule.html): Describes how to use the console to create a variable check rule for a pipeline that uses GitHub as the source provider.


## [Define CI/CD pipelines with stages and actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines.html)

- [Create a pipeline, stages, and actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create.html): Describes how to create a pipeline, which is an automated workflow of continuous integration and release events, in CodePipeline by using the console or the AWS CLI.
- [Edit a pipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-edit.html): Describes how to edit a pipeline, including adding or removing stages.

### [View pipelines and details](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-view.html)

Describes how to use the console or the AWS CLI to view details about a pipeline.

- [View pipelines (console)](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-view-console.html): You can view status, transitions, and artifact updates for a pipeline.
- [View action details in a pipeline (console)](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-view-details-console.html): You can view details for a pipeline, including details for actions in each stage.
- [View the pipeline ARN and service role ARN (console)](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-settings-console.html): You can use the console to view pipeline settings, such as the pipeline ARN, the service role ARN, and the pipeline artifact store.
- [View pipeline details and history (CLI)](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-view-cli.html): You can run the following commands to view details about your pipelines and pipeline executions:
- [View rule results for stage conditions in execution history](https://docs.aws.amazon.com/codepipeline/latest/userguide/w2aac19c19c21.html): You can view the rule results for an execution where a stage condition ran a rule and engaged a result for the stage, such as rollback or failure.
- [Delete a pipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-delete.html): Describes how to use the console or AWS CLI to delete a pipeline.
- [Create a pipeline that uses resources from another account](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create-cross-account.html): Describes how to create a pipeline in CodePipeline that uses resources from another AWS account.
- [Migrate polling pipelines to use event-based change detection](https://docs.aws.amazon.com/codepipeline/latest/userguide/update-change-detection.html): Describes how to update a pipeline for event-based change detection by source type.

### [Create the CodePipeline service role](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create-service-role.html)

Describes how to create the CodePipeline service role.

- [Create the CodePipeline service role (console)](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create-service-role-console.html): When you use the console to create a pipeline, you create the CodePipeline service role with the pipeline creation wizard.
- [Create the CodePipeline service role (CLI)](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create-service-role-cli.html): Before you create a pipeline with the AWS CLI or CloudFormation, you must create a CodePipeline service role for your pipeline and attach the service role policy and the trust policy.
- [Tagging resources](https://docs.aws.amazon.com/codepipeline/latest/userguide/tag-resources.html): Describes how to identity and organize your resources with tagging in CodePipeline.
- [Tag a pipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-tag.html): Describes how to tag pipeline resources in CodePipeline.
- [Create a notification rule](https://docs.aws.amazon.com/codepipeline/latest/userguide/notification-rule-create.html): Learn how to create a notification rule for AWS CodePipeline.


## [Connect to first-party source providers using source actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-sources.html)

### [Amazon ECR source actions and EventBridge](https://docs.aws.amazon.com/codepipeline/latest/userguide/create-cwe-ecr-source.html)

Learn how to start pipelines when EventBridge detects source code changes.

- [Create an EventBridge rule for an Amazon ECR source (console)](https://docs.aws.amazon.com/codepipeline/latest/userguide/create-cwe-ecr-source-console.html)
- [Create an EventBridge rule for an Amazon ECR source (CLI)](https://docs.aws.amazon.com/codepipeline/latest/userguide/create-cwe-ecr-source-cli.html): Call the put-rule command, specifying:
- [Create an EventBridge rule for an Amazon ECR source (CloudFormation template)](https://docs.aws.amazon.com/codepipeline/latest/userguide/create-cwe-ecr-source-cfn.html)

### [Connecting to Amazon S3 source actions that use EventBridge events](https://docs.aws.amazon.com/codepipeline/latest/userguide/create-S3-source-events.html)

Learn how to create an EventBridge rule enabled for events to start pipelines with an Amazon S3 source.

- [Create pipelines with an S3 source enabled for events (CLI)](https://docs.aws.amazon.com/codepipeline/latest/userguide/create-S3-source-events-cli.html): Follow these steps to create a pipeline with an S3 source that uses an event in EventBridge for change detection.
- [Create pipelines with an S3 source enabled for events (CloudFormation template)](https://docs.aws.amazon.com/codepipeline/latest/userguide/create-S3-source-events-cfn.html): This procedure is for a pipeline where the source bucket has events enabled.

### [Connecting to Amazon S3 source actions that use EventBridge and AWS CloudTrail](https://docs.aws.amazon.com/codepipeline/latest/userguide/create-cloudtrail-S3-source.html)

Learn how to create an EventBridge rule and AWS CloudTrail trail to start pipelines with an Amazon S3 source.

- [Create an EventBridge rule for an Amazon S3 source (console)](https://docs.aws.amazon.com/codepipeline/latest/userguide/create-cloudtrail-S3-source-console.html): Before you set up a rule in EventBridge, you must create an AWS CloudTrail trail.
- [Create an EventBridge rule for an Amazon S3 source (CLI)](https://docs.aws.amazon.com/codepipeline/latest/userguide/create-cloudtrail-S3-source-cli.html)
- [Create an EventBridge rule for an Amazon S3 source (CloudFormation template)](https://docs.aws.amazon.com/codepipeline/latest/userguide/create-cloudtrail-S3-source-cfn.html): To use CloudFormation to create a rule, update your template as shown here.

### [CodeCommit source actions and EventBridge](https://docs.aws.amazon.com/codepipeline/latest/userguide/triggering.html)

Learn how to start pipelines when EventBridge detects source code changes.

- [Create an EventBridge rule for a CodeCommit source (console)](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-trigger-source-repo-changes-console.html)
- [Create an EventBridge rule for a CodeCommit source (CLI)](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-trigger-source-repo-changes-cli.html): Call the put-rule command, specifying:
- [Create an EventBridge rule for a CodeCommit source (CloudFormation template)](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-trigger-source-repo-changes-cfn.html)


## [Add third-party source providers to pipelines using CodeConnections](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-connections.html)

- [Azure DevOps connections](https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-azure.html): Create a connection to Microsoft Azure DevOps using the CodePipeline console or the AWS CLI.
- [Bitbucket Cloud connections](https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-bitbucket.html): Create a connection to Bitbucket Cloud using the CodePipeline console or the AWS CLI.
- [GitHub connections](https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-github.html): Create a connection to GitHub using the CodePipeline console or the AWS CLI.
- [GitHub Enterprise Server connections](https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-ghes.html): Create a source action with a connection to GitHub Enterprise Server using the CodePipeline console or the AWS CLI.
- [GitLab.com connections](https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-gitlab.html): Create a connection to GitLab.com using the CodePipeline console or the AWS CLI.
- [Connections for GitLab self-managed](https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-gitlab-managed.html): Create a source action with a connection to GitLab self-managed using the CodePipeline console or the AWS CLI.
- [Use a connection shared with another account](https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-shared.html): You can create and manage a shared connection using AWS RAM.


## [Automate starting pipelines using triggers and filtering](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-triggers.html)

- [Add trigger on code push with no filter](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-trigger-add.html): Triggers allow you to configure your pipeline to start on a particular event type, such as a code push or pull request.
- [Add trigger with code push or pull request event types](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-filter.html): Describes how to use the console or AWS CLI to filter with triggers for a pipeline.
- [Add trigger to turn off change detection](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-trigger-no-detection.html): Triggers allow you to configure your pipeline to start on a particular event type, such as a code push or pull request.


## [Start and stop pipelines manually](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-start-stop.html)

### [Start a pipeline in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-about-starting.html)

Provides an overview about trigger types in CodePipeline.

- [Start a pipeline manually](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-rerun-manually.html): Describes how to manually start a pipeline by using the console or the AWS CLI.
- [Start a pipeline on a schedule](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-trigger-source-schedule.html): You can set up a rule in EventBridge to start a pipeline on a schedule.
- [Start a pipeline with a source revision override](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-trigger-source-overrides.html): Describes how to start a pipeline with a source revision override by using the console or the AWS CLI.
- [Stop a pipeline execution](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-stop.html): Describes how to use the console or AWS CLI to stop a pipeline execution.


## [View history and set the mode for pipeline executions](https://docs.aws.amazon.com/codepipeline/latest/userguide/manage-executions.html)

- [View executions](https://docs.aws.amazon.com/codepipeline/latest/userguide/executions-view.html): Describes how to use the console or the AWS CLI to view history for executions.
- [Set or change the pipeline execution mode](https://docs.aws.amazon.com/codepipeline/latest/userguide/execution-modes.html): Describes how to use the console or AWS CLI to set the execution mode for a pipeline.


## [Roll back or retry stages](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-stages.html)

- [Configuring stage retry for a failed stage or failed actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-retry.html): Describes how to retry a stage that has failed actions to complete successfully in a pipeline by using the console or the AWS CLI.

### [Configuring stage rollback](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-rollback.html)

Describes how to roll back a stage to a target pipeline execution by using the console or the AWS CLI.

- [Roll back a stage manually](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-rollback-manual.html): You can manually roll back a stage using the console or CLI.
- [Configure a stage for automatic rollback](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-rollback-auto.html): You can configure stages in a pipeline to roll back automatically on failure.
- [View rollback status in execution listing](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-rollback-view-listing.html): You can view the status and target execution ID for a rollback execution.
- [View rollback status details](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-rollback-view-details.html): You can view the status and target execution ID for a rollback execution.


## [Use action types, custom actions, and approval actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions.html)

- [Working with action types](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-types.html): Describes how to work with action types.
- [Create a custom action for a pipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-create-custom-action.html): Describes how to create a custom action for use in a pipeline or all of your pipelines by using the console or the AWS CLI.
- [Tag a custom action in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/customactions-tag.html): Describes how to tag custom action resources in CodePipeline.
- [Invoke a Lambda function in a pipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-invoke-lambda-function.html): Describes how to integrate AWS Lambda functions into pipelines in CodePipeline.

### [Add a manual approval action to a stage](https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals.html)

Learn how to create and manage manual approval requests and Amazon SNS notifications for CodePipeline stages.

- [Grant approval permissions to an IAM user in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals-iam-permissions.html): Learn how to attach a managed policy for CodePipeline to an IAM user.
- [Grant Amazon SNS permissions to a service role](https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals-service-role-permissions.html): Learn how to give a service role permission to access Amazon SNS resources for CodePipeline approval requests.
- [Add a manual approval action](https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals-action-add.html): Learn how to add an Approval action, or approval request, to a CodePipeline pipeline.
- [Approve or reject an approval action](https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals-approve-or-reject.html): Learn how to review and approve or reject an approval action in CodePipeline.
- [JSON data format for manual approval notifications](https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals-json-format.html): View an example of the JSON output that is created when an approval notification is sent to an Amazon SNS topic.
- [Add a cross-Region action to a pipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-create-cross-region.html): Describes how to use the console, AWS CLI, or CloudFormation to create a cross-Region action for use in a pipeline.
- [Working with variables](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-variables.html): Describes how to set output variables for pipeline actions.


## [Monitoring pipelines](https://docs.aws.amazon.com/codepipeline/latest/userguide/monitoring.html)

- [Monitoring CodePipeline events](https://docs.aws.amazon.com/codepipeline/latest/userguide/detect-state-changes-cloudwatch-events.html): Learn how to monitor changes in the state of a pipeline, stage, or action.
- [Events placeholder bucket reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-ct-placeholder-buckets.html): Learn about the default S3 buckets used by AWS CodePipeline to store the CloudTrail log files for CloudWatch Events.
- [Logging API calls with AWS CloudTrail](https://docs.aws.amazon.com/codepipeline/latest/userguide/monitoring-cloudtrail-logs.html): Learn about logging CodePipeline with AWS CloudTrail.
- [CodePipeline CloudWatch metrics](https://docs.aws.amazon.com/codepipeline/latest/userguide/metrics-dimensions.html): Learn how to monitor CloudWatch metrics.


## [Security](https://docs.aws.amazon.com/codepipeline/latest/userguide/security.html)

### [Data protection](https://docs.aws.amazon.com/codepipeline/latest/userguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS CodePipeline.

- [Configure server-side encryption for artifacts stored in Amazon S3 for CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/S3-artifact-encryption.html): Describes how CodePipeline interacts with AWS KMS to encrypt artifacts as they are put into and retrieved from the S3 bucket where your pipeline artifacts are stored.
- [Use AWS Secrets Manager to track database passwords or third-party API keys](https://docs.aws.amazon.com/codepipeline/latest/userguide/parameter-store-encryption.html): We recommend that you use AWS Secrets Manager to rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle.

### [Identity and access management](https://docs.aws.amazon.com/codepipeline/latest/userguide/security-iam.html)

How to authenticate requests and manage access to your CodePipeline resources.

- [How AWS CodePipeline works with IAM](https://docs.aws.amazon.com/codepipeline/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to CodePipeline, you should understand what IAM features are available to use with CodePipeline.

### [Identity-based policy examples](https://docs.aws.amazon.com/codepipeline/latest/userguide/security_iam_id-based-policy-examples.html)

By default, IAM users and roles don't have permission to create or modify CodePipeline resources.

- [Policy best practices](https://docs.aws.amazon.com/codepipeline/latest/userguide/security_iam_service-with-iam-policy-best-practices.html): Identity-based policies determine whether someone can create, access, or delete CodePipeline resources in your account.
- [Viewing resources in the console](https://docs.aws.amazon.com/codepipeline/latest/userguide/security-iam-resources-console.html): Describes permissions required to view resources in the console for CodePipeline.
- [Allow users to view their own permissions](https://docs.aws.amazon.com/codepipeline/latest/userguide/security_iam_id-based-policy-examples-view-own-permissions.html): This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user identity.
- [Identity-based policies (IAM) examples](https://docs.aws.amazon.com/codepipeline/latest/userguide/security-iam-id-policies-examples.html): Describes identity-based policies and how they work with IAM identities.
- [Using tags to control access to CodePipeline resources](https://docs.aws.amazon.com/codepipeline/latest/userguide/tag-based-access-control.html): Lists example tag-based access control policies for CodePipeline.
- [Permissions required to use the CodePipeline console](https://docs.aws.amazon.com/codepipeline/latest/userguide/security-iam-permissions-console.html): Lists all permissions required to use the CodePipeline console.
- [Permissions required to view compute logs in the CodePipeline console](https://docs.aws.amazon.com/codepipeline/latest/userguide/security-iam-permissions-console-logs.html): To view the logs in the Commands action on the CodePipeline console, the console role must have permissions.
- [AWS managed policies](https://docs.aws.amazon.com/codepipeline/latest/userguide/managed-policies.html): Learn about AWS managed policies for CodePipeline and recent changes to those policies.
- [Resource-based policy examples](https://docs.aws.amazon.com/codepipeline/latest/userguide/security_iam_resource-based-policy-examples.html)
- [Troubleshooting](https://docs.aws.amazon.com/codepipeline/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with CodePipeline and IAM.
- [CodePipeline permissions reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/permissions-reference.html): Describes the CodePipeline API operations and the corresponding actions you grant permissions to perform.
- [Manage the CodePipeline service role](https://docs.aws.amazon.com/codepipeline/latest/userguide/how-to-custom-role.html): The CodePipeline service role is configured with one or more policies that control access to the AWS resources used by the pipeline.
- [Incident response](https://docs.aws.amazon.com/codepipeline/latest/userguide/incident-response.html): You can use logging features in AWS to determine the actions users have taken in your account and the resources that were used.
- [Compliance validation](https://docs.aws.amazon.com/codepipeline/latest/userguide/codepipeline-compliance.html): Learn which AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/codepipeline/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy and learn about AWS CodePipeline features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/codepipeline/latest/userguide/infrastructure-security.html): Learn how AWS CodePipeline isolates service traffic.
- [Security best practices](https://docs.aws.amazon.com/codepipeline/latest/userguide/security-best-practices.html): Describes best practices for pipelines that use an S3 bucket, a GitHub source repository, or a Jenkins build provider for build or test actions.


## [Pipeline structure reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html)

- [Pipeline declaration](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-requirements.html): The pipeline and metadata level of a pipeline has a basic structure that includes the following parameters and syntax.
- [Stage declaration](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-requirements.html): The stage level of a pipeline has a basic structure that includes the following parameters and syntax.
- [Action declaration](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-requirements.html): The action level of a pipeline has a basic structure that includes the following parameters and syntax.
- [Valid action providers in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-valid-providers.html): The pipeline structure format is used to build actions and stages in a pipeline.
- [Valid settings for the PollForSourceChanges parameter](https://docs.aws.amazon.com/codepipeline/latest/userguide/PollForSourceChanges-defaults.html): The PollForSourceChanges parameter default is determined by the method used to create the pipeline, as described in the following table.
- [Valid input and output artifacts for each action type](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-action-artifacts.html): Depending on the action type and provider, you can have the following number of input and output artifacts.
- [Valid configuration parameters for each provider type](https://docs.aws.amazon.com/codepipeline/latest/userguide/structure-configuration-examples.html): This section lists valid configuration parameters for each action provider.


## [Action structure reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference.html)

- [Amazon EC2 action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-EC2Deploy.html): You use an Amazon EC2 EC2 action to deploy application code to your deployment fleet.
- [Amazon ECR source action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-ECR.html): Triggers the pipeline when a new image is pushed to the Amazon ECR repository.
- [ECRBuildAndPublish build action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-ECRBuildAndPublish.html): This build action allows you to automate building and pushing a new image when a change occurs in your source.
- [Amazon ECS and CodeDeploy blue-green deploy action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-ECSbluegreen.html): You can configure a pipeline in AWS CodePipeline that deploys container applications using a blue/green deployment.
- [Amazon Elastic Container Service deploy action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-ECS.html): You can use an Amazon ECS action to deploy an Amazon ECS service and task set.
- [Amazon Elastic Kubernetes Service EKS deploy action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-EKS.html): You can use the EKSDeploy action to deploy an Amazon EKS service.
- [AWS Lambda deploy action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-LambdaDeploy.html): You use an AWS Lambda deploy action to manage deploying your application code for your serverless deployment.
- [Amazon S3 deploy action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-S3Deploy.html): You use an Amazon S3 deploy action to deploy files to an Amazon S3 bucket for static web site hosting or archive.
- [Amazon S3 source action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-S3.html): Triggers the pipeline when a new object is uploaded to the configured bucket and object key.
- [AWS AppConfig deploy action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-AppConfig.html): AWS AppConfig is a capability of AWS Systems Manager.
- [CloudFormation deploy action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CloudFormation.html): Executes an operation on an CloudFormation stack.
- [CloudFormation StackSets](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-StackSets.html): CodePipeline offers the ability to perform CloudFormation StackSets operations as part of your CI/CD process.
- [AWS CodeBuild build and test action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodeBuild.html): Allows you to run builds and tests as part of your pipeline.
- [AWS CodePipeline invoke action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-PipelineInvoke.html): You use a CodePipeline invoke action to simplify triggering downstream pipeline executions and passing pipeline variables and source revisions between pipelines.
- [AWS CodeCommit source action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodeCommit.html): Starts the pipeline when a new commit is made on the configured CodeCommit repository and branch.
- [AWS CodeDeploy deploy action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodeDeploy.html): You use an AWS CodeDeploy action to deploy application code to your deployment fleet.
- [CodeStarSourceConnection for Bitbucket Cloud, GitHub, GitHub Enterprise Server, GitLab.com, and GitLab self-managed actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodestarConnectionSource.html): Source actions for connections are supported by AWS CodeConnections.
- [Commands action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-Commands.html): The Commands action allows you to run shell commands in a virtual compute instance.
- [AWS Device Farm test action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-DeviceFarm.html): In your pipeline, you can configure a test action that uses AWS Device Farm to run and test your application on devices.
- [Elastic Beanstalk deploy action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-Beanstalk.html): Elastic Beanstalk is a platform within AWS that is used for deploying and scaling web applications.
- [Amazon Inspector InspectorScan invoke action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-InspectorScan.html): Amazon Inspector is a vulnerability management service that automatically discovers workloads and continually scans them for software vulnerabilities and unintended network exposure.
- [AWS Lambda invoke action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-Lambda.html): Allows you to execute a Lambda function as an action in your pipeline.
- [AWS OpsWorks deploy action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-OpsWorks.html): You use an AWS OpsWorks action to deploy with OpsWorks using your pipeline.
- [AWS Service Catalogdeploy action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-ServiceCatalog.html): You use an AWS Service Catalog action to deploy templates using your pipeline.
- [AWS Step Functions](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-StepFunctions.html): An AWS CodePipeline action that does the following:


## [Rule structure reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html)

- [CloudWatchAlarm](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference-CloudWatchAlarm.html): When you create a condition, you can add the CloudWatchAlarm rule.
- [CodeBuild rule](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference-CodeBuild.html): When you create a condition, you can add the CodeBuild rule.
- [Commands](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference-Commands.html): When you create a condition, you can add the Commands rule.
- [DeploymentWindow](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference-DeploymentWindow.html): When you create a condition, you can add the DeploymentWindow rule.
- [LambdaInvoke](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference-LambdaInvoke.html): When you create a condition, you can add the LambdaInvoke rule.
- [VariableCheck](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference-VariableCheck.html): When you create a condition, you can add the VariableCheck rule.
