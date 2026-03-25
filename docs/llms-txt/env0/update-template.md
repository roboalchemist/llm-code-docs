# Source: https://docs.envzero.com/api-reference/templates/update-template.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Template

> Please note, you can only have 1 ssh key per template

## OpenAPI

````yaml api-reference/openapi.yml put /blueprints/{id}
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
  /blueprints/{id}:
    put:
      tags:
        - Templates
      summary: Update Template
      description: Please note, you can only have 1 ssh key per template
      operationId: templates-update-blueprint
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
              $ref: '#/components/schemas/BlueprintApi.UpdateBlueprint.Request.Body'
        description: ''
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BlueprintApi.UpdateBlueprint.Response'
components:
  schemas:
    BlueprintApi.UpdateBlueprint.Request.Body:
      type: object
      properties:
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
        bitbucketClientKey:
          type:
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
            using tfenv's 'min-required'. When set to "latest", the version used
            will be the most recent one available for Terraform.
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
        type:
          $ref: '#/components/schemas/BlueprintApi.BlueprintType'
        name:
          type: string
        description:
          type: string
        retry:
          $ref: '#/components/schemas/BlueprintApi.Retry'
        runTestsOnPullRequest:
          type: boolean
        isTerragruntRunAll:
          type: boolean
        projectIds:
          type: array
          items:
            type: string
        tagPrefix:
          type: string
      required:
        - repository
        - type
        - name
      additionalProperties: false
    BlueprintApi.UpdateBlueprint.Response:
      $ref: '#/components/schemas/BlueprintApi.Blueprint'
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
    BlueprintApi.BlueprintType:
      $ref: '#/components/schemas/BlueprintType'
    BlueprintApi.Retry:
      type: object
      properties:
        onDestroy:
          anyOf:
            - $ref: '#/components/schemas/BlueprintApi.RetryDeployOrDestroyConfig'
            - type: 'null'
            - $ref: '#/components/schemas/BlueprintApi.RetryDeployOrDestroyConfig'
            - type: 'null'
            - $ref: '#/components/schemas/BlueprintApi.RetryDeployOrDestroyConfig'
            - type: 'null'
        onDeploy:
          anyOf:
            - $ref: '#/components/schemas/BlueprintApi.RetryDeployOrDestroyConfig'
            - type: 'null'
            - $ref: '#/components/schemas/BlueprintApi.RetryDeployOrDestroyConfig'
            - type: 'null'
            - $ref: '#/components/schemas/BlueprintApi.RetryDeployOrDestroyConfig'
            - type: 'null'
      additionalProperties: false
    BlueprintApi.Blueprint:
      type: object
      additionalProperties: false
      properties:
        name:
          type: string
        description:
          type: string
        retry:
          $ref: '#/components/schemas/BlueprintApi.Retry'
        runTestsOnPullRequest:
          type: boolean
        isTerragruntRunAll:
          type: boolean
        projectIds:
          type: array
          items:
            type: string
        tagPrefix:
          type: string
        creationScopeId:
          type: string
        creationScope:
          $ref: '#/components/schemas/BlueprintApi.CreationScope'
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
            using tfenv's 'min-required'. When set to "latest", the version used
            will be the most recent one available for Terraform.
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
        type:
          $ref: '#/components/schemas/BlueprintApi.BlueprintType'
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
        bitbucketClientKey:
          type:
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
        id:
          type: string
        author:
          $ref: '#/components/schemas/User'
        createdAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time
        isDeleted:
          type: boolean
        authorId:
          type: string
        organizationId:
          type: string
        projectId:
          type: string
        isSingleUse:
          type: boolean
      required:
        - creationScope
        - creationScopeId
        - name
        - organizationId
        - repository
        - type
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
    BlueprintApi.RetryDeployOrDestroyConfig:
      type: object
      properties:
        times:
          type: number
        errorRegex:
          type: string
      required:
        - times
        - times
        - times
      additionalProperties: false
    BlueprintApi.CreationScope:
      type: string
      enum:
        - ORGANIZATION
        - PROJECT
        - ORGANIZATION
        - PROJECT
        - ORGANIZATION
        - PROJECT
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
