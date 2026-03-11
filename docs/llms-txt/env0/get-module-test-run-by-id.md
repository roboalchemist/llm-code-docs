# Source: https://docs.envzero.com/api-reference/modules/get-module-test-run-by-id.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Module Test Run by ID

## OpenAPI

````yaml api-reference/openapi.yml get /module/tests/{testRunId}
openapi: 3.1.0
info:
  title: env0 API
  description: >
    This document describes the resources that make up the official env0 REST
    API


    ### BaseURL

    https://api.env0.com/


    ### Content Types

    All requests should be in JSON format, and include the `accept:
    application/json` header
  version: 1.0.0
  x-logo:
    url: https://github.com/env0/api/raw/gh-pages/env0-color.png
    altText: env0 logo
servers:
  - url: https://api.env0.com
security:
  - env0_API_Key: []
tags:
  - name: Users
    description: |
      This API covers management for user settings
  - name: Agents Settings
    description: ''
  - name: Audit Events
    description: ''
  - name: Templates
    description: >
      A template in env0 defines a type of environment that can be deployed.

      Click Run Now on a template to create a new environment.

      A template consists of a name, a description, a valid set of configuration
      files describing the deployment, and a set of Variables and Secrets.

      More on https://docs.env0.com/docs/templates
  - name: Modules
    description: Module Registry endpoints
  - name: Custom Flow
    description: Project Custom Flow endpoints
  - name: Approval Policy
    description: Approval Policy endpoints
  - name: Bulk Operations
    description: |
      Bulk Operations
  - name: Cloud Compass
    description: ''
  - name: Code-Optimizer (BETA)
    description: >
      ⚠️ **BETA NOTICE**: All Code-Optimizer APIs are currently in beta and
      subject to breaking changes.


      Manages security and code quality issues found when repositories are
      scanned using code analysis tools.
  - name: Configuration
    description: >
      This API covers all deployment Configuration including: Variables, Tokens,
      SSH Keys and Deployment Credentials
  - name: Cost
    description: >
      With cost monitoring enabled in env0, you will be able to see how much
      each Environment you are running costs.

      More on https://docs.env0.com/docs/cost-monitoring
  - name: Credentials
    description: >
      Authentication against the env0 API is done via API Keys.


      An API Key is created by an organization administrator, but is not
      connected to any specific user when it's being used. 


      More on https://docs.env0.com/reference/authentication
  - name: Dashboard
    description: |
      This API covers all dashboard queries
  - name: Deployment Logs
    description: |
      env0 deployment consists of steps such as Init Variables
      using this API you can retrieve information about those steps
  - name: Deployment Logs
    description: The Deployment Logs Endpoint by steps
  - name: Environment Import
    description: >
      Discover and import your existing environments into env0 and track their
      status
  - name: Environment Outputs
    description: |
      control environments state access configurations
  - name: Environments
    description: |
      An environment is an entity representing a deployment managed by env0.

      Your users manage their environments in env0 in Projects.
      They can create, destroy, and redeploy environments.

      More on https://docs.env0.com/docs/environments
  - name: Modules
    description: ''
  - name: Notifications
    description: >
      env0 can send notifications for deployment events to your Slack or
      Microsoft Teams workspace.

      You can define several Notification Targets, corresponding to different
      channels.

      You can also associate these Notification Targets to different env0
      projects, controlling which events go to which channel.

      More on https://docs.env0.com/docs/notifications
  - name: Organization
    description: >
      An Organization is the highest level logical entity in env0.


      All Projects, Templates, Variable, Policies, and Environments, are defined
      for a specific organization. Organizations are logically separate from
      each other, and do not share any entities.

      More on https://docs.env0.com/docs/organizations
  - name: Projects
    description: >
      Projects are used in env0 to provide granular access control to
      Environments.

      Every environment in env0 exists under a project, and users are given
      access on a per-project basis.

      Projects are also useful for managing multiple cloud accounts within a
      single Organization.

      We recommend using projects to separate dev environments from production
      environments, each with its own access rights and policies.

      More on https://docs.env0.com/docs/projects
  - name: Provider Registry
    description: >-
      Provider Registry allows you to store, version control and share your
      Terraform providers privately across your organization. More on
      https://docs.env0.com/docs/providers
  - name: Remote Backend
    description: |
      control remote access to remote terraform state
  - name: Roles
    description: |
      Roles are used to get a precise control over who can do what.
  - name: Scheduling
    description: >
      Scheduling allows you to automatically trigger destroys and deploys of
      your environments on a scheduled basis.

      Scheduling is configured based on cron expressions, and can be attached to
      an already deployed environment only.


      More on https://docs.env0.com/docs/scheduling
  - name: Teams
    description: >
      Teams allow you to more easily manage your project level permissions in
      env0 by setting the role for an entire group of users as a single entity.

      A team belongs to a single Organization, are managed at the Organization
      Settings level, and are not shared between multiple organizations

      More on https://docs.env0.com/docs/teams
  - name: VCS
    description: >
      Manage Self Hosted VCS connections (GitLab Enterprise , GitHub Enterprise,
      Bitbucket Server)
  - name: Role Based Access
    description: >
      In order to have access to a project, users need to be associated with it.

      Each user associated with a project has a specific project Role assigned
      to them.


      More on
      https://docs.env0.com/docs/user-management#manage-users-of-a-project
paths:
  /module/tests/{testRunId}:
    get:
      tags:
        - Modules
      summary: Get Module Test Run by ID
      operationId: modules-get-module-test-run-by-id
      parameters:
        - name: testRunId
          in: path
          description: ''
          required: true
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/ModuleTestingApi.GetModuleTestRunById.Response
components:
  schemas:
    ModuleTestingApi.GetModuleTestRunById.Response:
      $ref: '#/components/schemas/ModuleTestingApi.FullModuleTestRun'
    ModuleTestingApi.FullModuleTestRun:
      type: object
      additionalProperties: false
      properties:
        status:
          $ref: '#/components/schemas/EnvironmentApi.DeploymentLogStatus'
        blueprintRevision:
          type: string
        prNumber:
          type: string
        startedBy:
          type: string
        startedByUser:
          $ref: '#/components/schemas/User'
        createdAt:
          type: string
          format: date-time
        queuedAt:
          type: string
          format: date-time
        startedAt:
          type: string
          format: date-time
        finishedAt:
          type: string
          format: date-time
        error:
          type: object
        customEnv0EnvironmentVariables:
          $ref: '#/components/schemas/CustomEnv0EnvironmentVariables'
        gitAvatarUrl:
          type: string
        gitUser:
          type: string
        blueprintRepository:
          type: string
        id:
          type: string
        deploymentLogId:
          type: string
        environmentId:
          type: string
        organizationId:
          type: string
        triggerName:
          $ref: '#/components/schemas/TriggerName'
        testSummary:
          $ref: '#/components/schemas/ModuleTestingApi.TestFileSummary'
        testFilesResults:
          $ref: '#/components/schemas/ModuleTestingApi.TestFilesResults'
        moduleId:
          type: string
      required:
        - deploymentLogId
        - environmentId
        - organizationId
    EnvironmentApi.DeploymentLogStatus:
      type: string
      enum:
        - IN_PROGRESS
        - WAITING_FOR_USER
        - TIMEOUT
        - FAILURE
        - SUCCESS
        - CANCELLED
        - INTERNAL_FAILURE
        - ABORTING
        - ABORTED
        - QUEUED
        - SKIPPED
        - NEVER_DEPLOYED
        - IN_PROGRESS
        - WAITING_FOR_USER
        - TIMEOUT
        - FAILURE
        - SUCCESS
        - CANCELLED
        - INTERNAL_FAILURE
        - ABORTING
        - ABORTED
        - QUEUED
        - SKIPPED
        - NEVER_DEPLOYED
        - IN_PROGRESS
        - WAITING_FOR_USER
        - TIMEOUT
        - FAILURE
        - SUCCESS
        - CANCELLED
        - INTERNAL_FAILURE
        - ABORTING
        - ABORTED
        - QUEUED
        - SKIPPED
        - NEVER_DEPLOYED
    User:
      type: object
      properties:
        email:
          type: string
        user_id:
          type: string
        created_at:
          type: string
        updated_at:
          type: string
        app_metadata:
          $ref: '#/components/schemas/AppMetadata'
        picture:
          type: string
        name:
          type: string
        last_login:
          type: string
        given_name:
          type: string
        family_name:
          type: string
        blocked:
          type: boolean
      additionalProperties: false
    CustomEnv0EnvironmentVariables:
      type: object
      properties:
        environmentId:
          type: string
          description: The deployed Environment ID
        projectId:
          type: string
          description: ENV0_PROJECT_ID
        projectName:
          type: string
          description: The Project Name of the deployed Environment
        deploymentLogId:
          type: string
          description: The deployment ID
        deploymentType:
          type: string
          enum:
            - deploy
            - destroy
            - prPlan
            - deploy
            - destroy
            - prPlan
            - deploy
            - destroy
            - prPlan
          description: The deployment type.
        deploymentRevision:
          type: string
          description: Available only when deployment revision defined
        workspaceName:
          type: string
          description: The Terraform Workspace name used in the Environment
        rootDir:
          type: string
          description: The root repository path
        organizationId:
          type: string
        templateId:
          type: string
        templateDir:
          type: string
        templateName:
          type: string
        environmentName:
          type: string
        environmentCreatorName:
          type: string
        environmentCreatorUserId:
          type: string
        environmentCreatorEmail:
          type: string
        deployerName:
          type: string
        deployerUserId:
          type: string
        deployerEmail:
          type: string
        reviewerName:
          type: string
        reviewerEmail:
          type: string
        reviewerUserId:
          type: string
        vcsProvider:
          $ref: '#/components/schemas/EnvironmentApi.VcsProvider'
          description: the vcs provider
        prAuthor:
          type: string
          description: pr author. available only in PR Plan
        prNumber:
          type: string
          description: the pr number. available only in PR Plan
        prSourceRepository:
          type: string
          description: >-
            the source repository. available only in PR Plan for the [VCSs
            supporting fork PR Plans](https://arc.net/l/quote/uoqvkxmq))"
        prSourceBranch:
          type: string
          description: the source branch. available only in PR Plan
        prTargetBranch:
          type: string
          description: the target branch. available only in PR Plan
        commitHash:
          type: string
          description: the commit hash
        commitUrl:
          type: string
          description: the commit url
        oidcToken:
          type: string
          description: >-
            The OIDC Token - read more
            here(https://docs.env0.com/docs/oidc-integrations) on how to enable
            it and use it
        vcsAccessToken:
          type: string
          description: >-
            When using a native VCS integration, this will represent the access
            token we use to clone the repository
        tfPlanJson:
          type: string
          description: The file path to a JSON representation of a Terraform Plan file
        cliArgsPlan:
          type: string
          description: add additional cli arguments when running a plan
        cliArgsApply:
          type: string
          description: add additional cli arguments when running the `apply` command
        discoveryRepositoryUrl:
          type: string
          description: >-
            Repository URL to write PR comments to. Used for prPlan deployments
            to override the target repo for comments.
        discoveryPrNumber:
          type: string
          description: >-
            PR number to write comments to. Used for prPlan deployments to
            override the target PR.
        discoveryVCS:
          $ref: '#/components/schemas/EnvironmentApi.VcsProvider'
          description: Discovery VCS provider (e.g., 'github')
      additionalProperties: false
    TriggerName:
      anyOf:
        - $ref: '#/components/schemas/ExternalTriggerName'
        - $ref: '#/components/schemas/InternalTriggerName'
        - $ref: '#/components/schemas/ExternalTriggerName'
        - $ref: '#/components/schemas/InternalTriggerName'
        - $ref: '#/components/schemas/ExternalTriggerName'
        - $ref: '#/components/schemas/InternalTriggerName'
    ModuleTestingApi.TestFileSummary:
      type: object
      properties:
        passed:
          type: number
        failed:
          type: number
        skipped:
          type: number
        errored:
          type: number
      additionalProperties: false
    ModuleTestingApi.TestFilesResults:
      type: object
      additionalProperties:
        $ref: '#/components/schemas/ModuleTestingApi.TestFileResult'
    AppMetadata:
      type: object
      properties:
        organizations:
          type: array
          items:
            $ref: '#/components/schemas/UserOrganization'
        isApiKey:
          type: boolean
        isAutogeneratedTerraformDeployer:
          type: boolean
        apiKeyType:
          type: string
          const: oidc
        createdBy:
          type: string
        organizationId:
          type: string
        isSystemUser:
          type: boolean
    EnvironmentApi.VcsProvider:
      type: string
      enum:
        - gitlab
        - github
        - bitbucket
        - bitbucketServer
        - gitlabEnterprise
        - githubEnterprise
        - azureDevOps
        - gitlab
        - github
        - bitbucket
        - bitbucketServer
        - gitlabEnterprise
        - githubEnterprise
        - azureDevOps
        - gitlab
        - github
        - bitbucket
        - bitbucketServer
        - gitlabEnterprise
        - githubEnterprise
        - azureDevOps
        - gitlab
        - github
        - bitbucket
        - bitbucketServer
        - gitlabEnterprise
        - githubEnterprise
        - azureDevOps
    ExternalTriggerName:
      type: string
      enum:
        - user
        - terraform-cli
        - workflow
        - user
        - terraform-cli
        - workflow
        - user
        - terraform-cli
        - workflow
    InternalTriggerName:
      type: string
      enum:
        - cd
        - prPlan
        - driftDetection
        - ttl
        - scheduled
        - comment
        - import
        - driftRemediation
        - cd
        - prPlan
        - driftDetection
        - ttl
        - scheduled
        - comment
        - import
        - driftRemediation
        - cd
        - prPlan
        - driftDetection
        - ttl
        - scheduled
        - comment
        - import
        - driftRemediation
    ModuleTestingApi.TestFileResult:
      type: object
      properties:
        testFile:
          type: string
        summary:
          $ref: '#/components/schemas/ModuleTestingApi.TestFileSummary'
        tests:
          type: array
          items:
            $ref: '#/components/schemas/ModuleTestingApi.TestResult'
      required:
        - testFile
        - summary
      additionalProperties: false
    UserOrganization:
      type: object
      properties:
        id:
          type: string
        role:
          type: string
        name:
          type: string
      required:
        - id
        - id
        - id
        - id
        - id
        - id
        - id
        - id
        - id
        - id
        - id
        - id
        - id
        - id
        - id
        - id
      additionalProperties: false
    ModuleTestingApi.TestResult:
      type: object
      properties:
        name:
          type: string
        status:
          $ref: '#/components/schemas/ModuleTestingApi.TestStatus'
      required:
        - name
        - status
      additionalProperties: false
    ModuleTestingApi.TestStatus:
      type: string
      enum:
        - passed
        - failed
        - skipped
        - errored
  securitySchemes:
    env0_API_Key:
      type: http
      scheme: basic
      description: >
        env0 API authentication is done via API keys. An API Key can either be
        created by an organization administrator, in which case it will not be
        connected to any specific user, or via Personal API Keys to authenticate
        as a user.

        ### Creating an API Key with a Specific Role

        * Once you've created your organization, you can set up and manage API
        Keys.

        * Navigate to the Organization Settings page and click the API Keys tab.

        * Click Add API Key and enter a name for your key in the Name field.
        This name is for reference purposes only and isn't used directly in
        authentication.

        > ❗️Save Your API Key ID and secret

        > The secret will not be available after you close this window.

        ### Creating a Personal API Key

        * Click on your avatar (located on the top right of the screen)

        * Click on Personal Settings

        * Select the API Keys tab

        * Click Add API Key, and enter a name for your key in the Name field.

        This name is for reference purposes and isn't used directly in
        authentication.

        > ❗️Save your API Key ID & secret

        > The secret will not be available after you close this window.

        ### Using an API Key to Authenticate

        Authentication of the env0 API is done using the Basic Authentication
        method. Each request made should include the API Key ID as the username,
        and the API Key secret as the password. For example, when using curl, we
        can include these parameters via flag `--user {API Key ID}:{API Key
        Secret}`.

        ### API Key Permissions

        When creating an API key through the organization settings, you will
        need to choose if you’d like to grant it Organization Admin or User
        permissions. In case of the latter, you can assign fine-grained
        permissions per project. Personal API Keys can be created through the
        user’s profile page and will have the same permissions as the user has.

        ### Rate Limits

        env0 API allows up to 1K requests per 60 seconds, requests are
        aggregated by IP, HTTP Method and URI. If you exceed this limit, you
        will receive a `429` status code.

````

Built with [Mintlify](https://mintlify.com).
