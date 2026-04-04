# Source: https://docs.datadoghq.com/infrastructure/resource_catalog/aws_amplify_app.md

---
title: Getting Started with Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Infrastructure > Datadog Resource Catalog
---

# aws_amplify_app{% #aws_amplify_app %}

## `account_id`{% #account_id %}

**Type**: `STRING`

## `app_arn`{% #app_arn %}

**Type**: `STRING`**Provider name**: `appArn`**Description**: The Amazon Resource Name (ARN) of the Amplify app.

## `app_id`{% #app_id %}

**Type**: `STRING`**Provider name**: `appId`**Description**: The unique ID of the Amplify app.

## `auto_branch_creation_config`{% #auto_branch_creation_config %}

**Type**: `STRUCT`**Provider name**: `autoBranchCreationConfig`**Description**: Describes the automated branch creation configuration for the Amplify app.

- `basic_auth_credentials`**Type**: `STRING`**Provider name**: `basicAuthCredentials`**Description**: The basic authorization credentials for the autocreated branch. You must base64-encode the authorization credentials and provide them in the format `user:password`.
- `build_spec`**Type**: `STRING`**Provider name**: `buildSpec`**Description**: The build specification (build spec) for the autocreated branch.
- `enable_auto_build`**Type**: `BOOLEAN`**Provider name**: `enableAutoBuild`**Description**: Enables auto building for the autocreated branch.
- `enable_basic_auth`**Type**: `BOOLEAN`**Provider name**: `enableBasicAuth`**Description**: Enables basic authorization for the autocreated branch.
- `enable_performance_mode`**Type**: `BOOLEAN`**Provider name**: `enablePerformanceMode`**Description**: Enables performance mode for the branch. Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out.
- `enable_pull_request_preview`**Type**: `BOOLEAN`**Provider name**: `enablePullRequestPreview`**Description**: Enables pull request previews for the autocreated branch.
- `environment_variables`**Type**: `MAP_STRING_STRING`**Provider name**: `environmentVariables`**Description**: The environment variables for the autocreated branch.
- `framework`**Type**: `STRING`**Provider name**: `framework`**Description**: The framework for the autocreated branch.
- `pull_request_environment_name`**Type**: `STRING`**Provider name**: `pullRequestEnvironmentName`**Description**: The Amplify environment name for the pull request.
- `stage`**Type**: `STRING`**Provider name**: `stage`**Description**: Describes the current stage for the autocreated branch.

## `auto_branch_creation_patterns`{% #auto_branch_creation_patterns %}

**Type**: `UNORDERED_LIST_STRING`**Provider name**: `autoBranchCreationPatterns`**Description**: Describes the automated branch creation glob patterns for the Amplify app.

## `basic_auth_credentials`{% #basic_auth_credentials %}

**Type**: `STRING`**Provider name**: `basicAuthCredentials`**Description**: The basic authorization credentials for branches for the Amplify app. You must base64-encode the authorization credentials and provide them in the format `user:password`.

## `build_spec`{% #build_spec %}

**Type**: `STRING`**Provider name**: `buildSpec`**Description**: Describes the content of the build specification (build spec) for the Amplify app.

## `cache_config`{% #cache_config %}

**Type**: `STRUCT`**Provider name**: `cacheConfig`**Description**: The cache configuration for the Amplify app. If you don't specify the cache configuration `type`, Amplify uses the default `AMPLIFY_MANAGED` setting.

- `type`**Type**: `STRING`**Provider name**: `type`**Description**: The type of cache configuration to use for an Amplify app. The `AMPLIFY_MANAGED` cache configuration automatically applies an optimized cache configuration for your app based on its platform, routing rules, and rewrite rules. This is the default setting. The `AMPLIFY_MANAGED_NO_COOKIES` cache configuration type is the same as `AMPLIFY_MANAGED`, except that it excludes all cookies from the cache key.

## `compute_role_arn`{% #compute_role_arn %}

**Type**: `STRING`**Provider name**: `computeRoleArn`**Description**: The Amazon Resource Name (ARN) of the IAM role for an SSR app. The Compute role allows the Amplify Hosting compute service to securely access specific Amazon Web Services resources based on the role's permissions. For more information about the SSR Compute role, see [Adding an SSR Compute role](https://docs.aws.amazon.com/latest/userguide/amplify-SSR-compute-role.html) in the Amplify User Guide.

## `create_time`{% #create_time %}

**Type**: `TIMESTAMP`**Provider name**: `createTime`**Description**: A timestamp of when Amplify created the application.

## `custom_headers`{% #custom_headers %}

**Type**: `STRING`**Provider name**: `customHeaders`**Description**: Describes the custom HTTP headers for the Amplify app.

## `custom_rules`{% #custom_rules %}

**Type**: `UNORDERED_LIST_STRUCT`**Provider name**: `customRules`**Description**: Describes the custom redirect and rewrite rules for the Amplify app.

- `condition`**Type**: `STRING`**Provider name**: `condition`**Description**: The condition for a URL rewrite or redirect rule, such as a country code.
- `source`**Type**: `STRING`**Provider name**: `source`**Description**: The source pattern for a URL rewrite or redirect rule.
- `status`**Type**: `STRING`**Provider name**: `status`**Description**: The status code for a URL rewrite or redirect rule.
  {% dl %}

  {% dt %}
200
  {% /dt %}

  {% dd %}
Represents a 200 rewrite rule.
  {% /dd %}

  {% dt %}
301
  {% /dt %}

  {% dd %}
Represents a 301 (moved permanently) redirect rule. This and all future requests should be directed to the target URL.
  {% /dd %}

  {% dt %}
302
  {% /dt %}

  {% dd %}
Represents a 302 temporary redirect rule.
  {% /dd %}

  {% dt %}
404
  {% /dt %}

  {% dd %}
Represents a 404 redirect rule.
  {% /dd %}

  {% dt %}
404-200
  {% /dt %}

  {% dd %}
Represents a 404 rewrite rule.
  {% /dd %}

    {% /dl %}
- `target`**Type**: `STRING`**Provider name**: `target`**Description**: The target pattern for a URL rewrite or redirect rule.

## `default_domain`{% #default_domain %}

**Type**: `STRING`**Provider name**: `defaultDomain`**Description**: The default domain for the Amplify app.

## `description`{% #description %}

**Type**: `STRING`**Provider name**: `description`**Description**: The description for the Amplify app.

## `enable_auto_branch_creation`{% #enable_auto_branch_creation %}

**Type**: `BOOLEAN`**Provider name**: `enableAutoBranchCreation`**Description**: Enables automated branch creation for the Amplify app.

## `enable_basic_auth`{% #enable_basic_auth %}

**Type**: `BOOLEAN`**Provider name**: `enableBasicAuth`**Description**: Enables basic authorization for the Amplify app's branches.

## `enable_branch_auto_build`{% #enable_branch_auto_build %}

**Type**: `BOOLEAN`**Provider name**: `enableBranchAutoBuild`**Description**: Enables the auto-building of branches for the Amplify app.

## `enable_branch_auto_deletion`{% #enable_branch_auto_deletion %}

**Type**: `BOOLEAN`**Provider name**: `enableBranchAutoDeletion`**Description**: Automatically disconnect a branch in the Amplify console when you delete a branch from your Git repository.

## `environment_variables`{% #environment_variables %}

**Type**: `MAP_STRING_STRING`**Provider name**: `environmentVariables`**Description**: The environment variables for the Amplify app. For a list of the environment variables that are accessible to Amplify by default, see [Amplify Environment variables](https://docs.aws.amazon.com/amplify/latest/userguide/amplify-console-environment-variables.html) in the Amplify Hosting User Guide.

## `iam_service_role_arn`{% #iam_service_role_arn %}

**Type**: `STRING`**Provider name**: `iamServiceRoleArn`**Description**: The Amazon Resource Name (ARN) of the IAM service role for the Amplify app.

## `name`{% #name %}

**Type**: `STRING`**Provider name**: `name`**Description**: The name for the Amplify app.

## `platform`{% #platform %}

**Type**: `STRING`**Provider name**: `platform`**Description**: The platform for the Amplify app. For a static app, set the platform type to `WEB`. For a dynamic server-side rendered (SSR) app, set the platform type to `WEB_COMPUTE`. For an app requiring Amplify Hosting's original SSR support only, set the platform type to `WEB_DYNAMIC`. If you are deploying an SSG only app with Next.js 14 or later, you must use the platform type `WEB_COMPUTE`.

## `production_branch`{% #production_branch %}

**Type**: `STRUCT`**Provider name**: `productionBranch`**Description**: Describes the information about a production branch of the Amplify app.

- `branch_name`**Type**: `STRING`**Provider name**: `branchName`**Description**: The branch name for the production branch.
- `last_deploy_time`**Type**: `TIMESTAMP`**Provider name**: `lastDeployTime`**Description**: The last deploy time of the production branch.
- `status`**Type**: `STRING`**Provider name**: `status`**Description**: The status of the production branch.
- `thumbnail_url`**Type**: `STRING`**Provider name**: `thumbnailUrl`**Description**: The thumbnail URL for the production branch.

## `repository`{% #repository %}

**Type**: `STRING`**Provider name**: `repository`**Description**: The Git repository for the Amplify app.

## `repository_clone_method`{% #repository_clone_method %}

**Type**: `STRING`**Provider name**: `repositoryCloneMethod`**Description**:This is for internal use.The Amplify service uses this parameter to specify the authentication protocol to use to access the Git repository for an Amplify app. Amplify specifies `TOKEN` for a GitHub repository, `SIGV4` for an Amazon Web Services CodeCommit repository, and `SSH` for GitLab and Bitbucket repositories.

## `tags`{% #tags %}

**Type**: `UNORDERED_LIST_STRING`

## `update_time`{% #update_time %}

**Type**: `TIMESTAMP`**Provider name**: `updateTime`**Description**: A timestamp of when Amplify updated the application.

## `waf_configuration`{% #waf_configuration %}

**Type**: `STRUCT`**Provider name**: `wafConfiguration`**Description**: Describes the Firewall configuration for the Amplify app. Firewall support enables you to protect your hosted applications with a direct integration with WAF.

- `status_reason`**Type**: `STRING`**Provider name**: `statusReason`**Description**: The reason for the current status of the Firewall configuration.
- `waf_status`**Type**: `STRING`**Provider name**: `wafStatus`**Description**: The status of the process to associate or disassociate a web ACL to an Amplify app.
- `web_acl_arn`**Type**: `STRING`**Provider name**: `webAclArn`**Description**: The Amazon Resource Name (ARN) for the web ACL associated with an Amplify app.

## `webhook_create_time`{% #webhook_create_time %}

**Type**: `TIMESTAMP`**Provider name**: `webhookCreateTime`**Description**: A timestamp of when Amplify created the webhook in your Git repository.
