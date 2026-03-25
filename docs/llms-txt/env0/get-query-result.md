# Source: https://docs.envzero.com/api-reference/dashboard/get-query-result.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get query result

## OpenAPI

````yaml api-reference/openapi.yml get /dashboards
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
  /dashboards:
    get:
      tags:
        - Dashboard
      summary: Get query result
      operationId: dashboard-query
      parameters:
        - name: queryName
          in: query
          description: the query to trigger
          required: true
          allowEmptyValue: false
          schema:
            type: string
            enum:
              - countTeams
              - countUsers
              - activeEnvironments
              - environmentStatus
              - maxActiveEnvironmentsPerDay
              - activeEnvironmentsPerDay
              - countProjects
              - countTemplates
              - countDeploymentType
              - countDeploymentsPerDay
              - countDeployTypesByUserInTimeRange
              - needsReview
        - name: startTime
          in: query
          description: >-
            Optional, some queries are time-based, UTC date and time using ISO
            8601 format
          required: false
          allowEmptyValue: false
          schema:
            type: string
        - name: endTime
          in: query
          description: >-
            Optional, some queries are time-based, UTC date and time using ISO
            8601 format
          required: false
          allowEmptyValue: false
          schema:
            type: string
        - name: organizationId
          in: query
          description: ''
          required: true
          allowEmptyValue: false
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DashboardApi.Query.Response'
components:
  schemas:
    DashboardApi.Query.Response:
      anyOf:
        - $ref: >-
            #/components/schemas/DashboardApi.Query.MaxActiveEnvironmentsPerDay.Response
        - $ref: >-
            #/components/schemas/DashboardApi.Query.ActiveEnvironmentsPerDay.Response
        - $ref: '#/components/schemas/DashboardApi.Query.EnvironmentStatus.Response'
        - $ref: '#/components/schemas/DashboardApi.Query.CountTeams.Response'
        - $ref: '#/components/schemas/DashboardApi.Query.CountUsers.Response'
        - $ref: '#/components/schemas/DashboardApi.Query.CountProjects.Response'
        - $ref: '#/components/schemas/DashboardApi.Query.CountTemplates.Response'
        - $ref: '#/components/schemas/DashboardApi.Query.ActiveEnvironments.Response'
        - $ref: >-
            #/components/schemas/DashboardApi.Query.CountDeploymentsPerDay.Response
        - $ref: '#/components/schemas/DashboardApi.Query.CountDeploymentType.Response'
        - $ref: >-
            #/components/schemas/DashboardApi.Query.CountDeployTypesByUserInTimeRange.Response
        - $ref: '#/components/schemas/DashboardApi.Query.NeedsReview.Response'
    DashboardApi.Query.MaxActiveEnvironmentsPerDay.Response:
      $ref: >-
        #/components/schemas/DashboardApi.Query.Base.Response_structure-api.d.ts-8987-9018-api.d.ts-8972-9019-api.d.ts-8942-9020-api.d.ts-8785-9026-api.d.ts-8735-9026-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_
    DashboardApi.Query.ActiveEnvironmentsPerDay.Response:
      $ref: >-
        #/components/schemas/DashboardApi.Query.Base.Response_structure-api.d.ts-9272-9574-api.d.ts-9257-9575-api.d.ts-9227-9576-api.d.ts-9073-9582-api.d.ts-9026-9582-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_
    DashboardApi.Query.EnvironmentStatus.Response:
      $ref: >-
        #/components/schemas/DashboardApi.Query.Base.Response_structure-api.d.ts-8188-8325-api.d.ts-8173-8326-api.d.ts-8143-8327-api.d.ts-8005-8333-api.d.ts-7965-8333-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_
    DashboardApi.Query.CountTeams.Response:
      $ref: >-
        #/components/schemas/DashboardApi.Query.Base.Response_structure-api.d.ts-6820-6837-api.d.ts-6805-6838-api.d.ts-6775-6839-api.d.ts-6644-6845-api.d.ts-6612-6845-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_
    DashboardApi.Query.CountUsers.Response:
      $ref: >-
        #/components/schemas/DashboardApi.Query.Base.Response_structure-api.d.ts-7054-7071-api.d.ts-7039-7072-api.d.ts-7009-7073-api.d.ts-6878-7079-api.d.ts-6845-7079-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_
    DashboardApi.Query.CountProjects.Response:
      $ref: >-
        #/components/schemas/DashboardApi.Query.Base.Response_structure-api.d.ts-7294-7311-api.d.ts-7279-7312-api.d.ts-7249-7313-api.d.ts-7115-7319-api.d.ts-7079-7319-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_
    DashboardApi.Query.CountTemplates.Response:
      $ref: >-
        #/components/schemas/DashboardApi.Query.Base.Response_structure-api.d.ts-7536-7553-api.d.ts-7521-7554-api.d.ts-7491-7555-api.d.ts-7356-7561-api.d.ts-7319-7561-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_
    DashboardApi.Query.ActiveEnvironments.Response:
      $ref: >-
        #/components/schemas/DashboardApi.Query.Base.Response_structure-api.d.ts-10078-10597-api.d.ts-10063-10598-api.d.ts-10033-10599-api.d.ts-9894-10605-api.d.ts-9853-10605-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_
    DashboardApi.Query.CountDeploymentsPerDay.Response:
      $ref: >-
        #/components/schemas/DashboardApi.Query.Base.Response_structure-api.d.ts-8575-8727-api.d.ts-8560-8728-api.d.ts-8530-8729-api.d.ts-8378-8735-api.d.ts-8333-8735-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_
    DashboardApi.Query.CountDeploymentType.Response:
      $ref: >-
        #/components/schemas/DashboardApi.Query.Base.Response_structure-api.d.ts-7916-7957-api.d.ts-7901-7958-api.d.ts-7871-7959-api.d.ts-7603-7965-api.d.ts-7561-7965-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_
    DashboardApi.Query.CountDeployTypesByUserInTimeRange.Response:
      $ref: >-
        #/components/schemas/DashboardApi.Query.Base.Response_structure-api.d.ts-10869-11053-api.d.ts-10854-11054-api.d.ts-10824-11055-api.d.ts-10661-11061-api.d.ts-10605-11061-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_
    DashboardApi.Query.NeedsReview.Response:
      $ref: >-
        #/components/schemas/DashboardApi.Query.Base.CountedResponse_structure-api.d.ts-6348-6604-api.d.ts-6326-6605-api.d.ts-6296-6606-api.d.ts-6081-6612-api.d.ts-5739-6612-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_
    DashboardApi.Query.Base.Response_structure-api.d.ts-8987-9018-api.d.ts-8972-9019-api.d.ts-8942-9020-api.d.ts-8785-9026-api.d.ts-8735-9026-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_:
      type: array
      items:
        type: object
        properties:
          date:
            type: string
          count:
            type: number
        required:
          - date
          - count
        additionalProperties: false
    DashboardApi.Query.Base.Response_structure-api.d.ts-9272-9574-api.d.ts-9257-9575-api.d.ts-9227-9576-api.d.ts-9073-9582-api.d.ts-9026-9582-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_:
      type: array
      items:
        type: object
        properties:
          name:
            type: string
          id:
            type: string
          projectName:
            type: string
          projectId:
            type: string
          status:
            $ref: '#/components/schemas/EnvironmentApi.EnvironmentStatus'
          user:
            $ref: '#/components/schemas/User'
          createdAt:
            type: string
            format: date-time
          blueprintId:
            type: string
          blueprintName:
            type: string
          isSingleUseBlueprint:
            type: boolean
        required:
          - name
          - id
          - projectName
          - projectId
          - status
          - user
          - createdAt
          - blueprintId
          - blueprintName
        additionalProperties: false
    DashboardApi.Query.Base.Response_structure-api.d.ts-8188-8325-api.d.ts-8173-8326-api.d.ts-8143-8327-api.d.ts-8005-8333-api.d.ts-7965-8333-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_:
      type: array
      items:
        type: object
        properties:
          status:
            type: string
            enum:
              - ACTIVE
              - FAILED
              - IN_PROGRESS
              - WAITING_FOR_USER
              - DRIFTED
              - NEVER_DEPLOYED
          count:
            type: number
        required:
          - status
          - count
        additionalProperties: false
    DashboardApi.Query.Base.Response_structure-api.d.ts-6820-6837-api.d.ts-6805-6838-api.d.ts-6775-6839-api.d.ts-6644-6845-api.d.ts-6612-6845-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_:
      type: array
      items:
        type: object
        properties:
          value:
            type: number
        required:
          - value
        additionalProperties: false
    DashboardApi.Query.Base.Response_structure-api.d.ts-7054-7071-api.d.ts-7039-7072-api.d.ts-7009-7073-api.d.ts-6878-7079-api.d.ts-6845-7079-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_:
      type: array
      items:
        type: object
        properties:
          value:
            type: number
        required:
          - value
        additionalProperties: false
    DashboardApi.Query.Base.Response_structure-api.d.ts-7294-7311-api.d.ts-7279-7312-api.d.ts-7249-7313-api.d.ts-7115-7319-api.d.ts-7079-7319-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_:
      type: array
      items:
        type: object
        properties:
          value:
            type: number
        required:
          - value
        additionalProperties: false
    DashboardApi.Query.Base.Response_structure-api.d.ts-7536-7553-api.d.ts-7521-7554-api.d.ts-7491-7555-api.d.ts-7356-7561-api.d.ts-7319-7561-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_:
      type: array
      items:
        type: object
        properties:
          value:
            type: number
        required:
          - value
        additionalProperties: false
    DashboardApi.Query.Base.Response_structure-api.d.ts-10078-10597-api.d.ts-10063-10598-api.d.ts-10033-10599-api.d.ts-9894-10605-api.d.ts-9853-10605-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_:
      type: array
      items:
        type: object
        properties:
          name:
            type: string
          id:
            type: string
          projectName:
            type: string
          projectId:
            type: string
          status:
            $ref: '#/components/schemas/EnvironmentApi.EnvironmentStatus'
          user:
            $ref: '#/components/schemas/User'
          lastDeploymentDate:
            type: string
            format: date-time
          createdAt:
            type: string
            format: date-time
          blueprintId:
            type: string
          blueprintName:
            type: string
          isSingleUseBlueprint:
            type: boolean
          isLocked:
            type: boolean
          blueprintType:
            $ref: '#/components/schemas/BlueprintApi.BlueprintType'
          driftStatus:
            $ref: '#/components/schemas/EnvironmentApi.DriftStatus'
          latestDeploymentLogError:
            type: object
        required:
          - name
          - id
          - projectName
          - projectId
          - status
          - user
          - lastDeploymentDate
          - createdAt
          - blueprintId
          - blueprintName
          - isLocked
          - blueprintType
          - driftStatus
        additionalProperties: false
    DashboardApi.Query.Base.Response_structure-api.d.ts-8575-8727-api.d.ts-8560-8728-api.d.ts-8530-8729-api.d.ts-8378-8735-api.d.ts-8333-8735-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_:
      type: array
      items:
        type: object
        properties:
          date:
            type: string
          deployCount:
            type: number
          destroyCount:
            type: number
          prPlanCount:
            type: number
          moduleTestCount:
            type: number
        required:
          - date
          - deployCount
          - destroyCount
          - prPlanCount
          - moduleTestCount
        additionalProperties: false
    DashboardApi.Query.Base.Response_structure-api.d.ts-7916-7957-api.d.ts-7901-7958-api.d.ts-7871-7959-api.d.ts-7603-7965-api.d.ts-7561-7965-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_:
      type: array
      items:
        type: object
        properties:
          deploymentType:
            type: string
          count:
            type: number
        required:
          - deploymentType
          - count
        additionalProperties: false
    DashboardApi.Query.Base.Response_structure-api.d.ts-10869-11053-api.d.ts-10854-11054-api.d.ts-10824-11055-api.d.ts-10661-11061-api.d.ts-10605-11061-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_:
      type: array
      items:
        type: object
        properties:
          user:
            $ref: '#/components/schemas/User'
          totalDeployments:
            type: number
          deployCount:
            type: number
          destroyCount:
            type: number
          prPlanCount:
            type: number
          moduleTestCount:
            type: number
        required:
          - user
          - totalDeployments
          - deployCount
          - destroyCount
          - prPlanCount
          - moduleTestCount
        additionalProperties: false
    DashboardApi.Query.Base.CountedResponse_structure-api.d.ts-6348-6604-api.d.ts-6326-6605-api.d.ts-6296-6606-api.d.ts-6081-6612-api.d.ts-5739-6612-api.d.ts-384-11862-api.d.ts-359-11862-api.d.ts-357-11864-api.d.ts-274-11864-api.d.ts-0-11865_:
      type: object
      properties:
        total:
          type: number
        data:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
              id:
                type: string
              projectId:
                type: string
              status:
                $ref: '#/components/schemas/EnvironmentApi.EnvironmentStatus'
              createdAt:
                type: string
                format: date-time
              updatedAt:
                type: string
                format: date-time
              blueprintId:
                type: string
              driftStatus:
                $ref: '#/components/schemas/EnvironmentApi.DriftStatus'
            required:
              - name
              - id
              - projectId
              - status
              - createdAt
              - updatedAt
              - blueprintId
              - driftStatus
            additionalProperties: false
      required:
        - total
        - data
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
    BlueprintApi.BlueprintType:
      $ref: '#/components/schemas/BlueprintType'
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
    BlueprintType:
      anyOf:
        - $ref: '#/components/schemas/IacType'
        - type: string
          const: workflow
        - $ref: '#/components/schemas/ModuleType'
        - $ref: '#/components/schemas/ApprovalPolicyType'
        - $ref: '#/components/schemas/CustomFlowType'
        - $ref: '#/components/schemas/EnvironmentDiscoveryType'
        - type: string
          const: discovery-config
        - $ref: '#/components/schemas/IacType'
        - type: string
          const: workflow
        - $ref: '#/components/schemas/ModuleType'
        - $ref: '#/components/schemas/ApprovalPolicyType'
        - $ref: '#/components/schemas/CustomFlowType'
        - $ref: '#/components/schemas/EnvironmentDiscoveryType'
        - type: string
          const: discovery-config
        - $ref: '#/components/schemas/IacType'
        - type: string
          const: workflow
        - $ref: '#/components/schemas/ModuleType'
        - $ref: '#/components/schemas/ApprovalPolicyType'
        - $ref: '#/components/schemas/CustomFlowType'
        - $ref: '#/components/schemas/EnvironmentDiscoveryType'
        - type: string
          const: discovery-config
        - $ref: '#/components/schemas/IacType'
        - type: string
          const: workflow
        - $ref: '#/components/schemas/ModuleType'
        - $ref: '#/components/schemas/ApprovalPolicyType'
        - $ref: '#/components/schemas/CustomFlowType'
        - $ref: '#/components/schemas/EnvironmentDiscoveryType'
        - type: string
          const: discovery-config
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
    ModuleType:
      type: string
      const: module
    ApprovalPolicyType:
      type: string
      const: approval-policy
    CustomFlowType:
      type: string
      const: custom-flow
    EnvironmentDiscoveryType:
      type: string
      const: environment-discovery
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
