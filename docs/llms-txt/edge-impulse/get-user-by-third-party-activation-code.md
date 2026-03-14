# Source: https://docs.edgeimpulse.com/apis/studio/user/get-user-by-third-party-activation-code.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get user by third party activation code

> Get information about a user through an activation code. This function is only available through a JWT token.



## OpenAPI

````yaml .assets/openapi.yaml post /api/user/by-third-party-activation-code
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
  /api/user/by-third-party-activation-code:
    post:
      tags:
        - User
      summary: Get user by third party activation code
      description: >-
        Get information about a user through an activation code. This function
        is only available through a JWT token.
      operationId: getUserByThirdPartyActivationCode
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserByThirdPartyActivationRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetUserResponse'
components:
  schemas:
    UserByThirdPartyActivationRequest:
      type: object
      required:
        - activationCode
      properties:
        activationCode:
          type: string
    GetUserResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
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
            - notifications
            - passwordConfigured
            - projectsSortOrder
            - hasEnterpriseFeaturesAccess
            - lastAccessedProjects
            - privatePersonalProjectsUsed
            - eulas
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
              description: >-
                List of all projects. This returns all projects for the user
                (regardless of whitelabel)
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
            whitelabels:
              description: List of white labels the user is a member of
              type: array
              items:
                type: object
                required:
                  - id
                  - domain
                  - name
                  - ownerOrganizationId
                  - isAdmin
                properties:
                  id:
                    type: number
                  domain:
                    type: string
                  name:
                    type: string
                  ownerOrganizationId:
                    type: number
                  isAdmin:
                    type: boolean
                    description: Whether the user is an admin of the white label.
            suspended:
              type: boolean
              description: Whether the user is suspended.
            suspensionReason:
              type: string
              description: >
                Detailed explanation of why the user account was suspended.

                This could include violations of terms of service, suspicious
                activity, or administrative actions.
            notifications:
              type: array
              description: List of notifications to show to the user.
              items:
                type: string
            subscriptionCancellationRequestDate:
              type: string
              format: date-time
              description: >-
                The date at which the user has requested to cancel their
                subscription.
            subscriptionDowngradeDate:
              type: string
              format: date-time
              description: >-
                The date at which the user's subscription will be downgraded due
                to cancellation.
            subscriptionTerminationDate:
              type: string
              format: date-time
              description: >-
                The date at which the user's subscription will be automatically
                terminated due to failed payments.
            payAsYouGoSubscriptionPeriodStartDate:
              type: string
              format: date-time
              description: The start date of the current pay-as-you-go subscription period.
            payAsYouGoSubscriptionPeriodEndDate:
              type: string
              format: date-time
              description: The end date of the current pay-as-you-go subscription period.
            passwordConfigured:
              type: boolean
              description: Whether the user has configured a password
            projectsSortOrder:
              $ref: '#/components/schemas/UserProjectsSortOrder'
              description: Default sort order on the projects list
            activeEnterpriseTrial:
              $ref: '#/components/schemas/EnterpriseTrial'
              description: >-
                The ongoing free Enterprise trials that the user has created, if
                any.
            hasEnterpriseFeaturesAccess:
              type: boolean
              description: >-
                Whether the current user has access to enterprise features. This
                is true if the user is an enterprise user, or has an active
                enterprise trial.
            timezone:
              description: Timezone for the user (or undefined if not specified).
              type: string
            lastAccessedProjects:
              description: >-
                Last 5 accessed projects. This _only_ returns projects for the
                current whitelabel ID.
              type: object
              required:
                - projects
                - hasMoreProjects
              properties:
                projects:
                  type: array
                  items:
                    type: object
                    required:
                      - id
                      - name
                      - created
                    properties:
                      id:
                        type: integer
                      name:
                        type: string
                      created:
                        type: string
                        format: date-time
                      lastAccessed:
                        type: string
                        format: date-time
                hasMoreProjects:
                  type: boolean
            privatePersonalProjectsUsed:
              type: integer
              description: Number of private projects created by the current user.
            lastAcceptedTermsOfService:
              type: object
              required:
                - version
                - acceptanceDate
              properties:
                version:
                  type: string
                acceptanceDate:
                  type: string
                  format: date-time
            eulas:
              type: array
              description: >-
                List of all Vendor End-User License Agreements that the user has
                accepted, or could accept.
              items:
                $ref: '#/components/schemas/UserEula'
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
    UserProjectsSortOrder:
      type: string
      enum:
        - created-asc
        - created-desc
        - added-asc
        - added-desc
        - name-asc
        - name-desc
        - last-accessed-desc
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
    UserEula:
      type: object
      required:
        - name
        - description
        - latestVersion
        - link
        - userIsCompliant
      properties:
        name:
          $ref: '#/components/schemas/UserEulaName'
        description:
          type: string
        latestVersion:
          type: string
        acceptedVersion:
          description: Current accepted version (or undefined if none)
          type: string
        link:
          type: string
        userIsCompliant:
          type: boolean
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
    UserTierEnum:
      type: string
      description: The user account tier.
      enum:
        - free
        - community-plus
        - professional
        - enterprise
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
    UserEulaName:
      type: string
      enum:
        - brainchip
        - syntiant
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