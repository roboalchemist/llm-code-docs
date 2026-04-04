# Source: https://docs.datadoghq.com/infrastructure/resource_catalog/aws_amplify_branch.md

---
title: Getting Started with Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Infrastructure > Datadog Resource Catalog
---

# aws_amplify_branch{% #aws_amplify_branch %}

## `account_id`{% #account_id %}

**Type**: `STRING`

## `active_job_id`{% #active_job_id %}

**Type**: `STRING`**Provider name**: `activeJobId`**Description**: The ID of the active job for a branch of an Amplify app.

## `associated_resources`{% #associated_resources %}

**Type**: `UNORDERED_LIST_STRING`**Provider name**: `associatedResources`**Description**: A list of custom resources that are linked to this branch.

## `backend`{% #backend %}

**Type**: `STRUCT`**Provider name**: `backend`

- `stack_arn`**Type**: `STRING`**Provider name**: `stackArn`**Description**: The Amazon Resource Name (ARN) for the CloudFormation stack.

## `backend_environment_arn`{% #backend_environment_arn %}

**Type**: `STRING`**Provider name**: `backendEnvironmentArn`**Description**: The Amazon Resource Name (ARN) for a backend environment that is part of an Amplify app. This property is available to Amplify Gen 1 apps only. When you deploy an application with Amplify Gen 2, you provision the app's backend infrastructure using Typescript code.

## `basic_auth_credentials`{% #basic_auth_credentials %}

**Type**: `STRING`**Provider name**: `basicAuthCredentials`**Description**: The basic authorization credentials for a branch of an Amplify app. You must base64-encode the authorization credentials and provide them in the format `user:password`.

## `branch_arn`{% #branch_arn %}

**Type**: `STRING`**Provider name**: `branchArn`**Description**: The Amazon Resource Name (ARN) for a branch that is part of an Amplify app.

## `branch_name`{% #branch_name %}

**Type**: `STRING`**Provider name**: `branchName`**Description**: The name for the branch that is part of an Amplify app.

## `build_spec`{% #build_spec %}

**Type**: `STRING`**Provider name**: `buildSpec`**Description**: The build specification (build spec) content for the branch of an Amplify app.

## `compute_role_arn`{% #compute_role_arn %}

**Type**: `STRING`**Provider name**: `computeRoleArn`**Description**: The Amazon Resource Name (ARN) of the IAM role for a branch of an SSR app. The Compute role allows the Amplify Hosting compute service to securely access specific Amazon Web Services resources based on the role's permissions. For more information about the SSR Compute role, see [Adding an SSR Compute role](https://docs.aws.amazon.com/latest/userguide/amplify-SSR-compute-role.html) in the Amplify User Guide.

## `create_time`{% #create_time %}

**Type**: `TIMESTAMP`**Provider name**: `createTime`**Description**: A timestamp of when Amplify created the branch.

## `custom_domains`{% #custom_domains %}

**Type**: `UNORDERED_LIST_STRING`**Provider name**: `customDomains`**Description**: The custom domains for a branch of an Amplify app.

## `description`{% #description %}

**Type**: `STRING`**Provider name**: `description`**Description**: The description for the branch that is part of an Amplify app.

## `destination_branch`{% #destination_branch %}

**Type**: `STRING`**Provider name**: `destinationBranch`**Description**: The destination branch if the branch is a pull request branch.

## `enable_auto_build`{% #enable_auto_build %}

**Type**: `BOOLEAN`**Provider name**: `enableAutoBuild`**Description**: Enables auto-building on push for a branch of an Amplify app.

## `enable_basic_auth`{% #enable_basic_auth %}

**Type**: `BOOLEAN`**Provider name**: `enableBasicAuth`**Description**: Enables basic authorization for a branch of an Amplify app.

## `enable_notification`{% #enable_notification %}

**Type**: `BOOLEAN`**Provider name**: `enableNotification`**Description**: Enables notifications for a branch that is part of an Amplify app.

## `enable_performance_mode`{% #enable_performance_mode %}

**Type**: `BOOLEAN`**Provider name**: `enablePerformanceMode`**Description**: Enables performance mode for the branch. Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out.

## `enable_pull_request_preview`{% #enable_pull_request_preview %}

**Type**: `BOOLEAN`**Provider name**: `enablePullRequestPreview`**Description**: Enables pull request previews for the branch.

## `environment_variables`{% #environment_variables %}

**Type**: `MAP_STRING_STRING`**Provider name**: `environmentVariables`**Description**: The environment variables specific to a branch of an Amplify app.

## `framework`{% #framework %}

**Type**: `STRING`**Provider name**: `framework`**Description**: The framework for a branch of an Amplify app.

## `pull_request_environment_name`{% #pull_request_environment_name %}

**Type**: `STRING`**Provider name**: `pullRequestEnvironmentName`**Description**: The Amplify environment name for the pull request.

## `source_branch`{% #source_branch %}

**Type**: `STRING`**Provider name**: `sourceBranch`**Description**: The source branch if the branch is a pull request branch.

## `stage`{% #stage %}

**Type**: `STRING`**Provider name**: `stage`**Description**: The current stage for the branch that is part of an Amplify app.

## `tags`{% #tags %}

**Type**: `UNORDERED_LIST_STRING`

## `thumbnail_url`{% #thumbnail_url %}

**Type**: `STRING`**Provider name**: `thumbnailUrl`**Description**: The thumbnail URL for the branch of an Amplify app.

## `total_number_of_jobs`{% #total_number_of_jobs %}

**Type**: `STRING`**Provider name**: `totalNumberOfJobs`**Description**: The total number of jobs that are part of an Amplify app.

## `ttl`{% #ttl %}

**Type**: `STRING`**Provider name**: `ttl`**Description**: The content Time to Live (TTL) for the website in seconds.

## `update_time`{% #update_time %}

**Type**: `TIMESTAMP`**Provider name**: `updateTime`**Description**: A timestamp for the last updated time for a branch.
