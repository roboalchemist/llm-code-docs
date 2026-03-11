# Source: https://docs.envzero.com/api-reference/environments/update-environment-ttl.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Environment TTL

## OpenAPI

````yaml api-reference/openapi.yml put /environments/{id}/ttl
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
  /environments/{id}/ttl:
    put:
      tags:
        - Environments
      summary: Update Environment TTL
      operationId: environments-ttl
      parameters:
        - name: id
          in: path
          description: ''
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EnvironmentApi.Ttl.Request.Body'
        description: ''
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EnvironmentApi.Ttl.Response'
components:
  schemas:
    EnvironmentApi.Ttl.Request.Body:
      $ref: '#/components/schemas/EnvironmentApi.TTLRequest'
    EnvironmentApi.Ttl.Response:
      $ref: '#/components/schemas/EnvironmentApi.Environment'
    EnvironmentApi.TTLRequest:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/EnvironmentApi.TTLType'
        value:
          type: string
          $comment: >-
            { "schema": { "anyOf": [{ "type": "string" }, { "type": "object",
            "instanceof": "Date" }] } }
          description: >-
            Required when the type is not INFINITE. When it's HOURS - attach a
            stringified number. When it's DATE - format is
            yyyy-mm-ddThh:MM:ss.000Z (For example 2023-06-04T20:05:00.000Z)
      required:
        - type
      additionalProperties: false
    EnvironmentApi.Environment:
      type: object
      properties:
        id:
          type: string
        createdAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time
        name:
          type: string
        organizationId:
          type: string
        projectId:
          type: string
        userId:
          type: string
        workspaceName:
          type: string
        user:
          $ref: '#/components/schemas/User'
        requiresApproval:
          type: boolean
        status:
          $ref: '#/components/schemas/EnvironmentApi.EnvironmentStatus'
        latestDeploymentLogId:
          type: string
        latestDeploymentLog:
          $ref: '#/components/schemas/EnvironmentApi.DeploymentLog'
        lifespanEndAt:
          type: string
          format: date-time
        markedForAutoDestroy:
          $ref: '#/components/schemas/AutoDestroyStatus'
        isArchived:
          type: boolean
          description: Mark the environment as inactive
        nextScheduledDates:
          $ref: '#/components/schemas/EnvironmentApi.EnvironmentNextScheduledDates'
        vcsCommandsAlias:
          type: string
        vcsPrCommentsEnabled:
          type: boolean
        continuousDeployment:
          type: boolean
        pullRequestPlanDeployments:
          type: boolean
        autoDeployOnPathChangesOnly:
          type: boolean
        autoDeployByCustomGlob:
          type: string
        terragruntWorkingDirectory:
          type: string
        isSingleUseBlueprint:
          type: boolean
        workflowEnvironmentId:
          type: string
        isRemoteBackend:
          type: boolean
        isLocked:
          type: boolean
        lockStatus:
          $ref: '#/components/schemas/EnvironmentApi.EnvironmentLockStatus'
        k8sNamespace:
          type: string
        isRemoteApplyEnabled:
          type: boolean
        driftStatus:
          $ref: '#/components/schemas/EnvironmentApi.DriftStatus'
      required:
        - name
        - organizationId
        - projectId
        - userId
        - workspaceName
        - user
        - requiresApproval
        - status
        - latestDeploymentLogId
        - latestDeploymentLog
        - lifespanEndAt
        - markedForAutoDestroy
        - isArchived
        - nextScheduledDates
        - continuousDeployment
        - pullRequestPlanDeployments
        - autoDeployOnPathChangesOnly
        - isRemoteBackend
        - isLocked
        - driftStatus
      additionalProperties: false
    EnvironmentApi.TTLType:
      type: string
      enum:
        - INFINITE
        - HOURS
        - DATE
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
    EnvironmentApi.EnvironmentStatus:
      type: string
      enum:
        - CREATED
        - INACTIVE
        - ACTIVE
        - FAILED
        - TIMEOUT
        - WAITING_FOR_USER
        - DEPLOY_IN_PROGRESS
        - DESTROY_IN_PROGRESS
        - TASK_IN_PROGRESS
        - ABORTING
        - ABORTED
        - NEVER_DEPLOYED
        - DRIFTED
        - DRY_RUN_IN_PROGRESS
        - CREATED
        - INACTIVE
        - ACTIVE
        - FAILED
        - TIMEOUT
        - WAITING_FOR_USER
        - DEPLOY_IN_PROGRESS
        - DESTROY_IN_PROGRESS
        - TASK_IN_PROGRESS
        - ABORTING
        - ABORTED
        - NEVER_DEPLOYED
        - DRIFTED
        - DRY_RUN_IN_PROGRESS
        - CREATED
        - INACTIVE
        - ACTIVE
        - FAILED
        - TIMEOUT
        - WAITING_FOR_USER
        - DEPLOY_IN_PROGRESS
        - DESTROY_IN_PROGRESS
        - TASK_IN_PROGRESS
        - ABORTING
        - ABORTED
        - NEVER_DEPLOYED
        - DRIFTED
        - DRY_RUN_IN_PROGRESS
    EnvironmentApi.DeploymentLog:
      type: object
      properties:
        id:
          type: string
        createdAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time
        type:
          $ref: '#/components/schemas/EnvironmentApi.DeploymentType'
        startedBy:
          type: string
        queuedAt:
          type: string
          format: date-time
        startedAt:
          type: string
          format: date-time
        finishedAt:
          type: string
          format: date-time
        output:
          $ref: '#/components/schemas/EnvironmentApi.DeploymentOutput'
        error:
          type: object
        failedCommand:
          type: string
        customEnv0EnvironmentVariables:
          $ref: '#/components/schemas/CustomEnv0EnvironmentVariables'
        costEstimation:
          $ref: '#/components/schemas/Infracost.CostEstimation'
        status:
          $ref: '#/components/schemas/EnvironmentApi.DeploymentLogStatus'
        blueprintId:
          type: string
        blueprintName:
          type: string
        blueprintRepository:
          type: string
        blueprintRevision:
          type: string
        blueprintPath:
          type: string
        blueprintType:
          $ref: '#/components/schemas/BlueprintApi.DeployableType'
        comment:
          type: string
        environmentId:
          type: string
        resourceCount:
          type: number
        resources:
          type: array
          items:
            $ref: '#/components/schemas/EnvironmentApi.EnvironmentResource'
        startedByUser:
          $ref: '#/components/schemas/User'
        isScheduledRun:
          type: boolean
        abortedBy:
          type: string
        abortedByUser:
          $ref: '#/components/schemas/User'
        gitUser:
          type: string
        gitAvatarUrl:
          type: string
        prNumber:
          type: string
        triggerName:
          $ref: '#/components/schemas/TriggerName'
        driftDetected:
          type: boolean
        plan:
          $ref: '#/components/schemas/DeploymentApi.Plan.Plan'
        planSummary:
          $ref: '#/components/schemas/DeploymentApi.Plan.PlanSummary'
        isSkippedApply:
          type: boolean
        workflowDeploymentId:
          type: string
        workflowFile:
          $ref: >-
            #/components/schemas/EnvironmentApi.WorkflowEnvironments.WorkflowFile
        workflowDeploymentOptions:
          $ref: '#/components/schemas/WorkflowDeploymentOptions'
        stateVersionId:
          type: string
        reviewersUsers:
          type: array
          items:
            $ref: '#/components/schemas/EnvironmentApi.ReviewerUser'
        reviewers:
          type: array
          items:
            $ref: '#/components/schemas/EnvironmentApi.Reviewer'
        reviewedBy:
          type: string
        reviewedByUser:
          $ref: '#/components/schemas/User'
        targets:
          type: array
          items:
            type: string
        variables:
          $ref: '#/components/schemas/EnvironmentApi.Variables'
        gitMetadata:
          $ref: '#/components/schemas/EnvironmentApi.GitMetadata'
        providerVersions:
          $ref: '#/components/schemas/EnvironmentApi.ProviderVersions'
        moduleVersions:
          $ref: '#/components/schemas/EnvironmentApi.ModuleVersions'
        stateFileHash:
          $ref: '#/components/schemas/EnvironmentApi.StateFileHash'
        driftCause:
          type: object
          properties:
            unappliedCommits:
              type: array
              items:
                $ref: '#/components/schemas/EnvironmentApi.DriftCause.UnappliedCommit'
          required:
            - unappliedCommits
            - unappliedCommits
          additionalProperties: false
      required:
        - type
        - startedBy
        - queuedAt
        - startedAt
        - finishedAt
        - output
        - error
        - costEstimation
        - status
        - blueprintId
        - blueprintName
        - blueprintRepository
        - blueprintRevision
        - blueprintPath
        - blueprintType
        - environmentId
        - resourceCount
        - startedByUser
        - isScheduledRun
        - abortedBy
        - abortedByUser
        - reviewersUsers
        - reviewers
        - type
        - startedBy
        - queuedAt
        - startedAt
        - finishedAt
        - output
        - error
        - costEstimation
        - status
        - blueprintId
        - blueprintName
        - blueprintRepository
        - blueprintRevision
        - blueprintPath
        - blueprintType
        - environmentId
        - resourceCount
        - startedByUser
        - isScheduledRun
        - abortedBy
        - abortedByUser
        - reviewersUsers
        - reviewers
      additionalProperties: false
    AutoDestroyStatus:
      type: number
      enum:
        - 0
        - 1
        - 2
        - 3
        - 0
        - 1
        - 2
        - 3
    EnvironmentApi.EnvironmentNextScheduledDates:
      type: object
      properties:
        deploy:
          type: string
          format: date-time
        destroy:
          type: string
          format: date-time
      additionalProperties: false
    EnvironmentApi.EnvironmentLockStatus:
      type: object
      properties:
        reason:
          type: string
        updatedBy:
          type: string
        updatedByUser:
          $ref: '#/components/schemas/User'
        updatedAt:
          type: string
          format: date-time
      required:
        - updatedBy
        - updatedAt
        - updatedBy
        - updatedAt
      additionalProperties: false
    EnvironmentApi.DriftStatus:
      type: string
      enum:
        - ERROR
        - DRIFTED
        - OK
        - NEVER_RUN
        - DISABLED
        - ERROR
        - DRIFTED
        - OK
        - NEVER_RUN
        - DISABLED
        - ERROR
        - DRIFTED
        - OK
        - NEVER_RUN
        - DISABLED
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
    EnvironmentApi.DeploymentType:
      type: string
      enum:
        - deploy
        - destroy
        - prPlan
        - driftDetection
        - task
        - remotePlan
        - dryRun
        - moduleTest
        - deploy
        - destroy
        - prPlan
        - driftDetection
        - task
        - remotePlan
        - dryRun
        - moduleTest
    EnvironmentApi.DeploymentOutput:
      anyOf:
        - $ref: '#/components/schemas/EnvironmentApi.Output'
        - $ref: '#/components/schemas/EnvironmentApi.TerragruntRunAllOutput'
        - $ref: '#/components/schemas/EnvironmentApi.Output'
        - $ref: '#/components/schemas/EnvironmentApi.TerragruntRunAllOutput'
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
    Infracost.CostEstimation:
      type: object
      properties:
        totalMonthlyCost:
          type: number
        monthlyCostDiff:
          type: number
        projects:
          type: array
          items:
            $ref: '#/components/schemas/Infracost.CostEstimationProject'
      required:
        - totalMonthlyCost
        - monthlyCostDiff
        - projects
        - totalMonthlyCost
        - monthlyCostDiff
        - projects
      additionalProperties: false
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
    BlueprintApi.DeployableType:
      $ref: '#/components/schemas/DeployableType'
    EnvironmentApi.EnvironmentResource:
      type: object
      properties:
        provider:
          type: string
        type:
          type: string
        name:
          type: string
        moduleName:
          type: string
      required:
        - provider
        - type
        - name
        - provider
        - type
        - name
      additionalProperties: false
    TriggerName:
      anyOf:
        - $ref: '#/components/schemas/ExternalTriggerName'
        - $ref: '#/components/schemas/InternalTriggerName'
        - $ref: '#/components/schemas/ExternalTriggerName'
        - $ref: '#/components/schemas/InternalTriggerName'
        - $ref: '#/components/schemas/ExternalTriggerName'
        - $ref: '#/components/schemas/InternalTriggerName'
    DeploymentApi.Plan.Plan:
      type: object
      properties:
        resourceChanges:
          type: array
          items:
            $ref: '#/components/schemas/DeploymentApi.Plan.PlanResourceChange'
        outputChanges:
          type: array
          items:
            $ref: '#/components/schemas/DeploymentApi.Plan.PlanOutputChange'
      required:
        - resourceChanges
        - outputChanges
        - resourceChanges
        - outputChanges
      additionalProperties: false
    DeploymentApi.Plan.PlanSummary:
      type: object
      properties:
        added:
          type: number
        changed:
          type: number
        destroyed:
          type: number
        imported:
          type: number
      required:
        - added
        - changed
        - destroyed
        - added
        - changed
        - destroyed
      additionalProperties: false
    EnvironmentApi.WorkflowEnvironments.WorkflowFile:
      type: object
      additionalProperties: false
      properties:
        settings:
          type: object
          properties:
            environmentRemovalStrategy:
              type: string
              enum:
                - destroy
                - detach
                - destroy
                - detach
          additionalProperties: false
        environments:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/EnvironmentApi.WorkflowEnvironments.WorkflowSubEnvironment
      required:
        - environments
        - environments
    WorkflowDeploymentOptions:
      type: object
      properties:
        node:
          type: string
        operation:
          $ref: '#/components/schemas/WorkflowPartialDeployOperation'
      required:
        - node
        - operation
        - node
        - operation
      additionalProperties: false
    EnvironmentApi.ReviewerUser:
      type: object
      properties:
        user:
          $ref: '#/components/schemas/User'
        action:
          type: string
          enum:
            - approved
            - cancelled
            - approved
            - cancelled
      required:
        - user
        - action
        - user
        - action
      additionalProperties: false
    EnvironmentApi.Reviewer:
      type: object
      properties:
        userId:
          type: string
        action:
          type: string
          enum:
            - approved
            - cancelled
            - approved
            - cancelled
      required:
        - userId
        - action
        - userId
        - action
      additionalProperties: false
    EnvironmentApi.Variables:
      type: array
      items:
        $ref: '#/components/schemas/EnvironmentApi.Variable'
    EnvironmentApi.GitMetadata:
      type: object
      properties:
        commit:
          type: string
        branch:
          type: string
        timestamp:
          type: string
          format: date-time
      required:
        - commit
        - branch
        - timestamp
        - commit
        - branch
        - timestamp
      additionalProperties: false
    EnvironmentApi.ProviderVersions:
      anyOf:
        - type: object
          additionalProperties:
            type: string
        - type: object
          additionalProperties:
            type: object
            additionalProperties:
              type: string
        - type: object
          additionalProperties:
            type: string
        - type: object
          additionalProperties:
            type: object
            additionalProperties:
              type: string
    EnvironmentApi.ModuleVersions:
      anyOf:
        - type: object
          additionalProperties:
            type: string
        - type: object
          additionalProperties:
            type: object
            additionalProperties:
              type: string
        - type: object
          additionalProperties:
            type: string
        - type: object
          additionalProperties:
            type: object
            additionalProperties:
              type: string
    EnvironmentApi.StateFileHash:
      anyOf:
        - type: object
          properties:
            value:
              type: string
          required:
            - value
          additionalProperties: false
        - type: object
          additionalProperties:
            type: string
        - type: object
          properties:
            value:
              type: string
          required:
            - value
          additionalProperties: false
        - type: object
          additionalProperties:
            type: string
    EnvironmentApi.DriftCause.UnappliedCommit:
      type: object
      properties:
        userEmail:
          type: string
        timestamp:
          type: string
          format: date-time
        commitHash:
          type: string
      required:
        - userEmail
        - timestamp
        - commitHash
        - userEmail
        - timestamp
        - commitHash
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
    EnvironmentApi.Output:
      type: object
      additionalProperties:
        $ref: '#/components/schemas/EnvironmentApi.OutputData'
    EnvironmentApi.TerragruntRunAllOutput:
      type: array
      items:
        type: object
        properties:
          moduleName:
            type: string
          output:
            $ref: '#/components/schemas/EnvironmentApi.Output'
        required:
          - moduleName
          - output
          - moduleName
          - output
        additionalProperties: false
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
    Infracost.CostEstimationProject:
      type: object
      properties:
        diff:
          type: object
          properties:
            totalMonthlyCost:
              type: string
          required:
            - totalMonthlyCost
            - totalMonthlyCost
          additionalProperties: false
      required:
        - diff
        - diff
      additionalProperties: false
    DeployableType:
      anyOf:
        - $ref: '#/components/schemas/IacType'
        - type: string
          const: workflow
        - type: string
          const: module
        - $ref: '#/components/schemas/IacType'
        - type: string
          const: workflow
        - type: string
          const: module
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
    DeploymentApi.Plan.PlanResourceChange:
      type: object
      properties:
        id:
          type: string
        cloudId:
          type: string
        moduleName:
          type: string
        driftByCloud:
          type: boolean
        name:
          type: string
        providerName:
          type: string
        type:
          type: string
        path:
          type: string
        action:
          $ref: '#/components/schemas/DeploymentApi.Plan.ChangeAction'
        attributes:
          type: array
          items:
            $ref: '#/components/schemas/DeploymentApi.Plan.AttributeChange'
        importing:
          $ref: '#/components/schemas/DeploymentApi.Plan.ResourceImportData'
        actionReason:
          $ref: '#/components/schemas/ActionReason'
        createBeforeDestroy:
          type: boolean
        previousAddress:
          type: string
      required:
        - name
        - providerName
        - type
        - path
        - action
        - attributes
        - name
        - providerName
        - type
        - path
        - action
        - attributes
      additionalProperties: false
    DeploymentApi.Plan.PlanOutputChange:
      type: object
      properties:
        moduleName:
          type: string
        name:
          type: string
        action:
          $ref: '#/components/schemas/DeploymentApi.Plan.ChangeAction'
        attributes:
          type: array
          items:
            $ref: '#/components/schemas/DeploymentApi.Plan.AttributeChange'
      required:
        - name
        - action
        - attributes
        - name
        - action
        - attributes
      additionalProperties: false
    EnvironmentApi.WorkflowEnvironments.WorkflowSubEnvironment:
      type: object
      additionalProperties: false
      properties:
        environmentId:
          type: string
        toDestroy:
          type: boolean
        isRemoteBackend:
          type: boolean
        k8sNamespace:
          type: string
        vcs:
          type: object
          additionalProperties: false
          properties:
            type:
              $ref: '#/components/schemas/IacType'
            tokenName:
              type: string
            tokenId:
              type: string
            sshKeys:
              type: array
              items:
                $ref: '#/components/schemas/BlueprintApi.SshKey'
            githubInstallationId:
              type:
                - number
                - 'null'
                - number
                - 'null'
            bitbucketClientKey:
              type:
                - string
                - 'null'
                - string
                - 'null'
            isBitbucketServer:
              type: boolean
            isGitLabEnterprise:
              type: boolean
            isGitHubEnterprise:
              type: boolean
            isGitLab:
              type: boolean
            isAzureDevOps:
              type: boolean
            isHelmRepository:
              type: boolean
            vcsConnectionId:
              type:
                - string
                - 'null'
                - string
                - 'null'
            repository:
              type: string
            revision:
              type: string
            path:
              type: string
            fileName:
              type: string
            helmChartName:
              type: string
            terraformVersion:
              $ref: '#/components/schemas/BlueprintApi.TerraformVersion'
              description: >-
                A string representing semantic version of Terraform. If set to
                "RESOLVE_FROM_TERRAFORM_CODE", the version will be determined by
                using tfenv's 'min-required'. When set to "latest", the version
                used will be the most recent one available for Terraform.
            opentofuVersion:
              $ref: '#/components/schemas/BlueprintApi.OpentofuVersion'
            terragruntVersion:
              type: string
            terragruntTfBinary:
              $ref: '#/components/schemas/BlueprintApi.TerragruntTfBinary'
            pulumiVersion:
              $ref: '#/components/schemas/BlueprintApi.PulumiVersionType'
            ansibleVersion:
              $ref: '#/components/schemas/BlueprintApi.AnsibleVersionType'
          required:
            - repository
            - type
            - repository
            - type
        name:
          type: string
        templateName:
          type: string
        templateId:
          type: string
        templateType:
          $ref: '#/components/schemas/IacType'
        revision:
          type: string
        workspace:
          type: string
        needs:
          type: array
          items:
            type: string
        terragruntWorkingDirectory:
          type: string
        requiresApproval:
          type: boolean
        disabled:
          type:
            - string
            - boolean
            - string
            - boolean
      required:
        - name
        - name
    WorkflowPartialDeployOperation:
      type: string
      enum:
        - run-from-here
        - single-node-deploy
        - single-node-destroy
        - run-from-here
        - single-node-deploy
        - single-node-destroy
    EnvironmentApi.Variable:
      type: object
      properties:
        id:
          type: string
          description: >-
            The ID of the configuration property. If provided, will act as an
            update. Otherwise, a new configuration property will be created.
        name:
          type: string
        scope:
          $ref: '#/components/schemas/ConfigurationScope'
        scopeId:
          type: string
          description: >-
            The ID of the entity of the provided `scope`. e.g. a project's ID
            when the provided `scope` is `PROJECT`.

            Inapplicable for `GLOBAL` scope, as it has no specific entity.
        value:
          type: string
        isSensitive:
          type: boolean
        type:
          $ref: '#/components/schemas/ConfigurationType'
          description: |-
            Whether it is an Environment or Terraform variable
            0 value maps to an Environment variable
            1 value maps to an Terraform variable
        schema:
          $ref: '#/components/schemas/PartialJSONSchema7'
          description: |-
            * type?: "string"
            * format: HCL | JSON | ENVIRONMENT_OUTPUT # default: null
                * ENVIRONMENT_OUTPUT is a special type used to indicate that the value is an output from the environment.
              The value format is: ${env0:<environmentId>:<outputName>} it will be resolved before deployment.
            * enum?: ["option1", "option2"]
                * Optional, for UI dropdown, works only without format. Note that if you want to update this list, you must provide the full updated list each time.
        userId:
          type: string
        updatedAt:
          type: string
          format: date-time
        projectId:
          type: string
      required:
        - name
        - scope
        - type
        - name
        - scope
        - type
      additionalProperties: false
    EnvironmentApi.OutputData:
      type: object
      properties:
        value: {}
        sensitive:
          type: boolean
        type:
          type: string
      required:
        - value
        - sensitive
        - type
        - value
        - sensitive
        - type
      additionalProperties: false
    IacType:
      type: string
      enum:
        - opentofu
        - terraform
        - terragrunt
        - pulumi
        - k8s
        - cloudformation
        - helm
        - ansible
        - opentofu
        - terraform
        - terragrunt
        - pulumi
        - k8s
        - cloudformation
        - helm
        - ansible
        - opentofu
        - terraform
        - terragrunt
        - pulumi
        - k8s
        - cloudformation
        - helm
        - ansible
        - opentofu
        - terraform
        - terragrunt
        - pulumi
        - k8s
        - cloudformation
        - helm
        - ansible
        - opentofu
        - terraform
        - terragrunt
        - pulumi
        - k8s
        - cloudformation
        - helm
        - ansible
    DeploymentApi.Plan.ChangeAction:
      type: string
      enum:
        - create
        - update
        - delete
        - recreate
        - metadata
        - create
        - update
        - delete
        - recreate
        - metadata
    DeploymentApi.Plan.AttributeChange:
      type: object
      properties:
        name:
          type: string
        before: {}
        after: {}
      required:
        - name
        - name
      additionalProperties: false
    DeploymentApi.Plan.ResourceImportData:
      type: object
      properties:
        id:
          type: string
      required:
        - id
        - id
      additionalProperties: false
    ActionReason:
      type: string
      enum:
        - replace_because_tainted
        - replace_because_cannot_update
        - replace_by_request
        - delete_because_no_resource_config
        - delete_because_no_module
        - delete_because_wrong_repetition
        - delete_because_count_index
        - delete_because_each_key
        - read_because_config_unknown
        - read_because_dependency_pending
        - replace_because_tainted
        - replace_because_cannot_update
        - replace_by_request
        - delete_because_no_resource_config
        - delete_because_no_module
        - delete_because_wrong_repetition
        - delete_because_count_index
        - delete_because_each_key
        - read_because_config_unknown
        - read_because_dependency_pending
    BlueprintApi.SshKey:
      type: object
      properties:
        id:
          type: string
          minLength: 1
        name:
          type: string
      required:
        - id
        - name
        - id
        - name
        - id
        - name
      additionalProperties: false
    BlueprintApi.TerraformVersion:
      type: string
    BlueprintApi.OpentofuVersion:
      type: string
    BlueprintApi.TerragruntTfBinary:
      type: string
      enum:
        - terraform
        - opentofu
        - terraform
        - opentofu
        - terraform
        - opentofu
    BlueprintApi.PulumiVersionType:
      type: string
    BlueprintApi.AnsibleVersionType:
      type: string
    ConfigurationScope:
      type: string
      enum:
        - SET
        - GLOBAL
        - BLUEPRINT
        - SUB_ENVIRONMENT_BLUEPRINT
        - PROJECT
        - WORKFLOW
        - ENVIRONMENT
        - DEPLOYMENT
        - SET
        - GLOBAL
        - BLUEPRINT
        - SUB_ENVIRONMENT_BLUEPRINT
        - PROJECT
        - WORKFLOW
        - ENVIRONMENT
        - DEPLOYMENT
        - SET
        - GLOBAL
        - BLUEPRINT
        - SUB_ENVIRONMENT_BLUEPRINT
        - PROJECT
        - WORKFLOW
        - ENVIRONMENT
        - DEPLOYMENT
        - SET
        - GLOBAL
        - BLUEPRINT
        - SUB_ENVIRONMENT_BLUEPRINT
        - PROJECT
        - WORKFLOW
        - ENVIRONMENT
        - DEPLOYMENT
        - SET
        - GLOBAL
        - BLUEPRINT
        - SUB_ENVIRONMENT_BLUEPRINT
        - PROJECT
        - WORKFLOW
        - ENVIRONMENT
        - DEPLOYMENT
    ConfigurationType:
      type: number
      enum:
        - 0
        - 1
        - 0
        - 1
        - 0
        - 1
        - 0
        - 1
        - 0
        - 1
    PartialJSONSchema7:
      type: object
      properties:
        type:
          type: string
          enum:
            - string
            - array
            - string
            - array
            - string
            - array
            - string
            - array
            - string
            - array
        enum:
          type: array
          items:
            type: string
        format:
          type: string
          enum:
            - HCL
            - JSON
            - ENVIRONMENT_OUTPUT
            - HCL
            - JSON
            - ENVIRONMENT_OUTPUT
            - HCL
            - JSON
            - ENVIRONMENT_OUTPUT
            - HCL
            - JSON
            - ENVIRONMENT_OUTPUT
            - HCL
            - JSON
            - ENVIRONMENT_OUTPUT
      additionalProperties: false
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
