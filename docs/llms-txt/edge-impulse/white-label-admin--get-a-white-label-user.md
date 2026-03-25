# Source: https://docs.edgeimpulse.com/apis/studio/organizations/white-label-admin--get-a-white-label-user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# White Label Admin - Get a white label user

> White label admin only API to get information about a user.



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/whitelabel/users/{userId}
openapi: 3.0.0
info:
  title: Edge Impulse API
  version: 1.0.0
servers:
  - url: https://studio.edgeimpulse.com/v1
security:
  - ApiKeyAuthentication: []
  - JWTAuthentication: []
  - JWTHttpHeaderAuthentication: []
  - OAuth2: []
paths:
  /api/organizations/{organizationId}/whitelabel/users/{userId}:
    get:
      tags:
        - Organizations
      summary: White Label Admin - Get a white label user
      description: White label admin only API to get information about a user.
      operationId: whitelabelAdminGetUser
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/UserIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AdminGetUserResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
    UserIdParameter:
      name: userId
      in: path
      required: true
      description: User ID
      schema:
        type: integer
  schemas:
    AdminGetUserResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - user
          properties:
            user:
              $ref: '#/components/schemas/AdminApiUser'
    GenericApiResponse:
      type: object
      required:
        - success
      properties:
        success:
          type: boolean
          description: Whether the operation succeeded
        error:
          type: string
          description: Optional error description (set if 'success' was false)
    AdminApiUser:
      allOf:
        - $ref: '#/components/schemas/User'
        - type: object
          required:
            - email
            - activated
            - organizations
            - projects
            - experiments
            - tier
            - suspended
            - trials
          properties:
            email:
              type: string
            activated:
              type: boolean
            organizations:
              type: array
              description: >-
                Organizations that the user is a member of. Only filled when
                requesting information about yourself.
              items:
                $ref: '#/components/schemas/UserOrganization'
            projects:
              type: array
              items:
                $ref: '#/components/schemas/Project'
            experiments:
              type: array
              description: >-
                Experiments the user has access to. Enabling experiments can
                only be done through a JWT token.
              items:
                $ref: '#/components/schemas/UserExperiment'
            evaluation:
              type: boolean
              description: Whether this is an ephemeral evaluation account.
            ambassador:
              type: boolean
              description: Whether this user is an ambassador.
            tier:
              $ref: '#/components/schemas/UserTierEnum'
            lastSeen:
              type: string
              format: date-time
            suspended:
              type: boolean
              description: Whether the user is suspended.
            trials:
              type: array
              description: Current or past enterprise trials.
              items:
                $ref: '#/components/schemas/EnterpriseTrial'
            dailyMetrics:
              type: array
              description: Metrics for the last 365 days
              nullable: true
              items:
                $ref: '#/components/schemas/DailyMetricsRecord'
    User:
      type: object
      required:
        - id
        - username
        - name
        - email
        - created
        - staffInfo
        - pending
        - activated
        - mfaConfigured
      properties:
        id:
          type: integer
          example: 1
        username:
          type: string
          example: janjongboom
        name:
          type: string
          example: Jan Jongboom
        email:
          type: string
          example: quijote@edgeimpulse.com
        photo:
          type: string
          example: https://usercdn.edgeimpulse.com/photos/1.jpg
        created:
          type: string
          format: date-time
          example: '2019-08-31T17:32:28Z'
        lastSeen:
          type: string
          format: date-time
          example: '2019-08-31T17:32:28Z'
        staffInfo:
          $ref: '#/components/schemas/StaffInfo'
        pending:
          type: boolean
        jobTitle:
          type: string
          example: Software Engineer
        permissions:
          description: List of permissions the user has
          type: array
          items:
            $ref: '#/components/schemas/Permission'
        companyName:
          type: string
          example: Edge Impulse Inc.
        activated:
          type: boolean
          description: Whether the user has activated their account or not.
        mfaConfigured:
          type: boolean
          description: Whether the user has configured multi-factor authentication
        stripeCustomerId:
          type: string
          description: Stripe customer ID, if any.
        hasPendingPayments:
          type: boolean
          description: Whether the user has pending payments.
        tier:
          $ref: '#/components/schemas/UserTierEnum'
        idps:
          type: array
          description: >-
            List of identity providers (e.g. Google, GitHub) that the user has
            used to sign in with
          items:
            type: string
    UserOrganization:
      type: object
      required:
        - id
        - name
        - isDeveloperProfile
        - whitelabelId
        - isAdmin
        - created
        - trialId
        - trialExpiredDate
        - trialUpgradedDate
        - entitlementLimits
        - userCount
        - adminCount
        - privateProjectCount
        - publicProjectLicense
      properties:
        id:
          type: integer
        name:
          type: string
        logo:
          type: string
        isDeveloperProfile:
          type: boolean
        whitelabelId:
          type: integer
          nullable: true
          description: >-
            Unique identifier of the white label this project belongs to, if
            any.
        isAdmin:
          type: boolean
          description: Whether the user is admin of this organization or not.
        created:
          type: string
          format: date-time
          description: When the organization was created.
          example: '2019-08-31T17:32:28Z'
        trialId:
          type: number
          nullable: true
          description: Unique identifier of the trial this organization belongs to, if any.
          example: 1
        trialExpiredDate:
          type: string
          format: date-time
          nullable: true
          description: >-
            Date when the trial expired, if any. A expired trial has a grace
            period of 30 days before it's associated organization is deleted.
          example: '2019-08-31T17:32:28Z'
        trialUpgradedDate:
          type: string
          format: date-time
          nullable: true
          description: >-
            Date when the trial was upgraded to a full enterprise account, if
            any.
          example: '2019-08-31T17:32:28Z'
        entitlementLimits:
          $ref: '#/components/schemas/EntitlementLimits'
        userCount:
          type: integer
          description: The total number of users that are a member of this organization.
        adminCount:
          type: integer
          description: The number of admin users for this organization.
        privateProjectCount:
          type: integer
          description: The number of private projects for this organization.
        lastAccessed:
          type: string
          format: date-time
          description: Last time this user accessed this organization.
        publicProjectLicense:
          type: object
          description: Default license for new public projects under this organization.
          required:
            - name
            - link
          properties:
            name:
              type: string
            link:
              type: string
    Project:
      type: object
      required:
        - id
        - name
        - description
        - created
        - owner
        - collaborators
        - labelingMethod
        - metadata
        - isEnterpriseProject
        - whitelabelId
        - tier
        - hasPublicVersion
        - isPublic
        - allowsLivePublicAccess
        - ownerIsDeveloperProfile
        - indPauseProcessingSamples
        - publicProjectListed
      properties:
        id:
          type: integer
          example: 1
        name:
          type: string
          example: Water hammer detection
        description:
          type: string
        created:
          type: string
          format: date-time
          example: '2019-07-21T17:32:28Z'
        owner:
          type: string
          description: User or organization that owns the project
        lastAccessed:
          type: string
          format: date-time
          example: '2019-07-21T17:32:28Z'
        lastModified:
          type: string
          format: date-time
          example: '2019-07-21T17:32:28Z'
        lastModificationDetails:
          type: string
          description: Details about the last modification
          example: Data sample added
        logo:
          type: string
          description: Custom logo for this project (not available for all projects)
        ownerUserId:
          type: integer
        ownerOrganizationId:
          type: integer
        ownerAvatar:
          type: string
          description: URL of the project owner avatar, if any.
        ownerIsDeveloperProfile:
          type: boolean
        developerProfileUserId:
          type: integer
          description: User ID of the developer profile, if any.
        collaborators:
          type: array
          items:
            $ref: '#/components/schemas/ProjectCollaborator'
        labelingMethod:
          $ref: '#/components/schemas/ProjectLabelingMethod'
        metadata:
          type: object
          description: Metadata about the project
        dataExplorerScreenshot:
          type: string
        isEnterpriseProject:
          type: boolean
          description: Whether this is an enterprise project
        whitelabelId:
          type: integer
          nullable: true
          description: >-
            Unique identifier of the white label this project belongs to, if
            any.
        whitelabelName:
          type: string
          description: Name of the white label this project belongs to, if any.
        tags:
          type: array
          items:
            type: string
          description: List of project tags
          example:
            - FOMO
            - beers
        category:
          type: string
          description: Project category
          enum:
            - Accelerometer
            - Audio
            - Images
            - Keyword spotting
            - Object detection
            - Other
        license:
          $ref: '#/components/schemas/PublicProjectLicense'
          description: Public project license, if any.
        tier:
          $ref: '#/components/schemas/ProjectTierEnum'
        hasPublicVersion:
          type: boolean
          description: Whether this project has been published or not.
        isPublic:
          type: boolean
          description: >
            Whether this is a public version of a project. A version is a
            snapshot of a project at a certain point in time, which can be used
            to periodically save the state of a project. Versions can be private
            (just for internal use and reference) or public, available to
            everyone. A public version can be cloned by anyone, restoring the
            state of the project at the time into a new, separate project.
        allowsLivePublicAccess:
          type: boolean
          description: >
            Whether this project allows live, public access. Unlike a public
            version, a live public project is not fixed in time, and always
            includes the latest project changes. Similar to public versions, a
            live public project can be cloned by anyone, creating a new,
            separate project.
        indPauseProcessingSamples:
          type: boolean
        publicProjectListed:
          type: boolean
          description: >
            If the project allows public access, whether to list it the public
            projects overview response. If not listed, the project is still
            accessible via direct link. If the project does not allow public
            access, this field has no effect.
        deletedDate:
          type: string
          format: date-time
        fullDeletionDate:
          type: string
          format: date-time
        scheduledFullDeletionDate:
          type: string
          format: date-time
    UserExperiment:
      type: object
      required:
        - type
        - title
        - enabled
        - showToUser
      properties:
        type:
          type: string
        title:
          type: string
        help:
          type: string
        enabled:
          type: boolean
        showToUser:
          type: boolean
    UserTierEnum:
      type: string
      description: The user account tier.
      enum:
        - free
        - community-plus
        - professional
        - enterprise
    EnterpriseTrial:
      type: object
      required:
        - id
        - userId
        - created
        - organizationId
        - expirationDate
        - expiredDate
        - deletedDate
        - upgradedDate
      properties:
        id:
          type: integer
          description: Unique identifier of the trial.
        userId:
          type: integer
          description: ID of the user who created the trial.
        organizationId:
          type: integer
          description: ID of the organization created for the trial.
        created:
          type: string
          format: date-time
          description: >-
            Date when the trial was created. Trials start immediately on
            creation.
        expirationDate:
          $ref: '#/components/schemas/TrialExpirationDate'
        notes:
          $ref: '#/components/schemas/TrialNotes'
        expiredDate:
          type: string
          format: date-time
          nullable: true
          description: >-
            Date when the trial actually expired. This is set when the trial is
            expired by the system.
        deletedDate:
          type: string
          format: date-time
          nullable: true
          description: >-
            Date when the trial was deleted. This is set when the trial is
            fully  deleted by the system.
        upgradedDate:
          type: string
          format: date-time
          nullable: true
          description: Date when the trial was upgraded to a full enterprise account.
    DailyMetricsRecord:
      type: object
      required:
        - date
        - totalUsers
        - totalStaffUsers
        - totalProjects
        - totalCurrentContractCpuComputeTimeSeconds
        - totalCurrentContractGpuComputeTimeSeconds
        - totalCurrentContractComputeTimeSeconds
        - computeTimeCalculatedSince
        - totalStorageSizeBytes
        - usersAdded
        - usersDeleted
        - projectsAdded
        - projectsDeleted
        - cpuComputeTimeSeconds
        - gpuComputeTimeSeconds
        - computeTimeSeconds
        - storageBytesAdded
        - storageBytesDeleted
      properties:
        date:
          type: string
          format: date-time
          description: Date of the metrics record.
          example: '2021-01-01T00:00:00Z'
        totalUsers:
          type: integer
          description: >
            Total number of users, if the metrics record applies to a
            non-developer profile organization.

            For developer profile organizations, we default to 0.
          example: 100
        totalStaffUsers:
          type: integer
          description: >
            Total number of staff users, if the metrics record applies to a
            non-developer profile organization.

            For developer profile organizations, we default to 0.
          example: 10
        totalProjects:
          type: integer
          description: |
            Total number of projects at the end of the metrics record date.
          example: 50
        totalCurrentContractCpuComputeTimeSeconds:
          type: integer
          description: >
            Total CPU compute time since contract start date, or organization /
            user creation date, at

            the end of the metrics record date.
          example: 100000
        totalCurrentContractGpuComputeTimeSeconds:
          type: integer
          description: >
            Total GPU compute time since contract start date, or organization /
            user creation date, at

            the end of the metrics record date.
          example: 100000
        totalCurrentContractComputeTimeSeconds:
          type: integer
          description: >
            Total compute time since contract start date, or organization / user
            creation date, at

            the end of the metrics record date.

            Compute time is calculated as CPU + 3*GPU compute time.
          example: 100000
        computeTimeCalculatedSince:
          type: string
          format: date-time
          description: >
            Date from which the total compute time is calculated. This is the
            contract start date for billing

            organizations, or organization / user creation date.
          example: '2021-01-01T00:00:00Z'
        totalStorageSizeBytes:
          type: integer
          description: |
            Total storage size in bytes at the end of the metrics record date.
          example: 1000000000
        usersAdded:
          type: integer
          description: |
            Number of users added during the metrics record date.
          example: 10
        staffUsersAdded:
          type: integer
          description: |
            Number of staff users added during the metrics record date.
          example: 1
        usersDeleted:
          type: integer
          description: |
            Number of users deleted during the metrics record date.
          example: 5
        staffUsersDeleted:
          type: integer
          description: |
            Number of staff users deleted during the metrics record date.
          example: 1
        projectsAdded:
          type: integer
          description: |
            Number of projects added during the metrics record date.
          example: 10
        projectsDeleted:
          type: integer
          description: |
            Number of projects deleted during the metrics record date.
          example: 5
        cpuComputeTimeSeconds:
          type: integer
          description: |
            Total CPU compute time during the metrics record date.
          example: 10000
        gpuComputeTimeSeconds:
          type: integer
          description: |
            Total GPU compute time during the metrics record date.
          example: 10000
        computeTimeSeconds:
          type: integer
          description: |
            Total compute time during the metrics record date.
            Compute time is calculated as CPU + 3*GPU compute time.
          example: 10000
        storageBytesAdded:
          type: integer
          description: |
            Total storage size in bytes added during the metrics record date.
          example: 1000000000
        storageBytesDeleted:
          type: integer
          description: |
            Total storage size in bytes deleted during the metrics record date.
          example: 500000000
    StaffInfo:
      type: object
      required:
        - isStaff
        - hasSudoRights
      properties:
        isStaff:
          type: boolean
        hasSudoRights:
          type: boolean
        companyName:
          type: string
    Permission:
      type: string
      enum:
        - admin:infra:disallowedEmailDomains:read
        - admin:infra:disallowedEmailDomains:write
        - admin:infra:featureFlags:read
        - admin:infra:featureFlags:write
        - admin:infra:config:read
        - admin:infra:config:write
        - admin:infra:migrations:read
        - admin:infra:migrations:write
        - admin:metrics:read
        - admin:metrics:write
        - admin:oauth:read
        - admin:oauth:write
        - admin:organizations:read
        - admin:organizations:write
        - admin:organizations:members:write
        - admin:projects:members:write
        - admin:projects:read
        - admin:projects:write
        - admin:trashbin:write
        - admin:trials:read
        - admin:trials:write
        - admin:users:permissions:write
        - admin:users:read
        - admin:users:signupApprovals:read
        - admin:users:signupApprovals:write
        - admin:users:write
        - admin:jobs:read
        - admin:emails:verification:code:read
        - admin:sso:read
        - admin:sso:domainIdps:write
        - admin:vlm:model:read
        - admin:vlm:model:write
        - projects:limits:write
        - projects:training:keras:write
        - projects:data:versioning:write
        - thirdpartyauth:read
        - thirdpartyauth:write
        - users:emails:read
        - whitelabels:read
        - whitelabels:write
        - test:data:write
    EntitlementLimits:
      type: object
      properties:
        totalStorage:
          type: number
          description: Storage entitlement, in bytes
        computeTimePerYear:
          type: number
          description: Total compute time entitlement (CPU + GPU), in seconds
        gpuComputeTimePerYear:
          type: number
          description: GPU compute time entitlement, in seconds
        numberOfProjects:
          type: integer
          description: Number of projects allowed for this organization
        numberOfUsers:
          type: integer
          description: Number of users allowed for this organization
    ProjectCollaborator:
      allOf:
        - $ref: '#/components/schemas/User'
        - type: object
          required:
            - isOwner
          properties:
            isOwner:
              type: boolean
    ProjectLabelingMethod:
      type: string
      enum:
        - single_label
        - object_detection
        - label_map
    PublicProjectLicense:
      type: string
      enum:
        - Apache-2.0
        - BSD-3-Clause
        - BSD-3-Clause-Clear
    ProjectTierEnum:
      type: string
      description: >-
        The project tier. This is "enterprise" for all organization projects, or
        the user tier for all user projects.
      enum:
        - free
        - community-plus
        - professional
        - enterprise
    TrialExpirationDate:
      type: string
      format: date-time
      description: >-
        Expiration date of the trial. The trial will be set as expired after
        this date. There will be a grace period of 30 days after a trial expires
        before fully deleting the trial organization. This field is ignored if
        the trial is requested by a non-admin user, defaulting to 14 days trial.
      example: '2020-01-01T00:00:00Z'
    TrialNotes:
      type: string
      description: >-
        Notes about the trial. Free form text. This field is ignored if the
        trial is requested by a non-admin user.
      example: This is a trial for the company's new project.
  securitySchemes:
    ApiKeyAuthentication:
      type: apiKey
      in: header
      name: x-api-key
    JWTAuthentication:
      type: apiKey
      in: cookie
      name: jwt
    JWTHttpHeaderAuthentication:
      type: apiKey
      in: header
      name: x-jwt-token
    OAuth2:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: /v1/oauth/authorize
          tokenUrl: /v1/oauth/token
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information
        implicit:
          authorizationUrl: /v1/oauth/authorize
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information
        password:
          tokenUrl: /v1/oauth/token
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information
        clientCredentials:
          tokenUrl: /v1/oauth/token
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information

````

Built with [Mintlify](https://mintlify.com).