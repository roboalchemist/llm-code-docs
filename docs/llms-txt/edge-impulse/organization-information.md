# Source: https://docs.edgeimpulse.com/apis/studio/organizations/organization-information.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Organization information

> List all information about this organization.



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}
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
  /api/organizations/{organizationId}:
    get:
      tags:
        - Organizations
      summary: Organization information
      description: List all information about this organization.
      operationId: getOrganizationInfo
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrganizationInfoResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
  schemas:
    OrganizationInfoResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - organization
            - datasets
            - defaultComputeLimits
            - experiments
            - cliLists
            - performance
          properties:
            organization:
              $ref: '#/components/schemas/Organization'
            datasets:
              type: array
              items:
                $ref: '#/components/schemas/OrganizationDataset'
            defaultComputeLimits:
              type: object
              required:
                - requestsCpu
                - requestsMemory
                - limitsCpu
                - limitsMemory
              properties:
                requestsCpu:
                  type: number
                requestsMemory:
                  type: number
                limitsCpu:
                  type: number
                limitsMemory:
                  type: number
            entitlementLimits:
              $ref: '#/components/schemas/EntitlementLimits'
            experiments:
              type: array
              description: >-
                Experiments that the organization has access to. Enabling
                experiments can only be done through a JWT token.
              items:
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
            readme:
              type: object
              description: Present if a readme is set for this project
              required:
                - markdown
                - html
              properties:
                markdown:
                  type: string
                html:
                  type: string
            whitelabelId:
              type: integer
            cliLists:
              type: object
              required:
                - objectDetectionLastLayerOptions
                - imageInputScalingOptions
              properties:
                objectDetectionLastLayerOptions:
                  type: array
                  items:
                    type: object
                    required:
                      - label
                      - value
                    properties:
                      label:
                        type: string
                      value:
                        $ref: '#/components/schemas/ObjectDetectionLastLayer'
                imageInputScalingOptions:
                  type: array
                  items:
                    type: object
                    required:
                      - label
                      - value
                    properties:
                      label:
                        type: string
                      value:
                        $ref: '#/components/schemas/ImageInputScaling'
            performance:
              type: object
              required:
                - jobLimitM
              properties:
                jobLimitM:
                  type: integer
                  description: >-
                    Compute time limit per job in minutes (for
                    non-transformation jobs).
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
    Organization:
      type: object
      required:
        - id
        - name
        - users
        - isDeveloperProfile
        - whitelabelId
        - trialId
        - trialExpiredDate
        - trialUpgradedDate
        - created
        - showHeaderImgMask
      properties:
        id:
          type: integer
        name:
          type: string
          description: EdgeImpulse Inc.
        logo:
          type: string
          example: https://usercdn.edgeimpulse.com/logos/1.jpg
        headerImg:
          type: string
          example: https://usercdn.edgeimpulse.com/leaders/1.jpg
        showHeaderImgMask:
          type: boolean
        users:
          type: array
          items:
            $ref: '#/components/schemas/OrganizationUser'
        isDeveloperProfile:
          type: boolean
        whitelabelId:
          type: integer
          nullable: true
          description: >-
            Unique identifier of the white label this organization belongs to,
            if any.
        whitelabelName:
          type: string
          description: Name of the white label this organization belongs to, if any.
        projects:
          type: array
          items:
            $ref: '#/components/schemas/Project'
        trialId:
          type: integer
          nullable: true
          description: Unique identifier of the trial this organization belongs to, if any.
        trialExpiredDate:
          type: string
          format: date-time
          nullable: true
          description: >-
            Date when the trial expired, if any. A expired trial has a grace
            period of 30 days before it's associated organization is deleted.
        trialUpgradedDate:
          type: string
          format: date-time
          nullable: true
          description: >-
            Date when the trial was upgraded to a full enterprise account, if
            any.
        created:
          type: string
          format: date-time
          description: Date when the organization was created.
        contractStartDate:
          type: string
          format: date-time
          nullable: true
          description: Date when the current contract started, if any.
        deletedDate:
          type: string
          format: date-time
          description: >-
            The date in which the organization was deleted. If the organization
            is not deleted, this field is not set.
    OrganizationDataset:
      type: object
      required:
        - dataset
        - lastFileCreated
        - totalFileSize
        - totalFileCount
        - totalItemCount
        - totalItemCountChecklistOK
        - totalItemCountChecklistFailed
        - tags
        - type
      properties:
        dataset:
          type: string
        lastFileCreated:
          type: string
          format: date-time
        totalFileSize:
          type: integer
        totalFileCount:
          type: integer
        totalItemCount:
          type: integer
        totalItemCountChecklistOK:
          type: integer
        totalItemCountChecklistFailed:
          type: integer
        tags:
          type: array
          items:
            type: string
        category:
          type: string
        bucket:
          $ref: '#/components/schemas/OrganizationDatasetBucket'
        type:
          $ref: '#/components/schemas/OrganizationDatasetTypeEnum'
        bucketPath:
          type: string
          description: Location of the dataset within the bucket
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
    ObjectDetectionLastLayer:
      type: string
      enum:
        - mobilenet-ssd
        - fomo
        - yolov2-akida
        - yolov5
        - yolov5v5-drpai
        - yolox
        - yolov7
        - yolo-pro
        - tao-retinanet
        - tao-ssd
        - tao-yolov3
        - tao-yolov4
        - yolov11
        - yolov11-abs
        - paddleocr-detector
        - qc-face-det-lite
    ImageInputScaling:
      description: >-
        Normalization that is applied to images. If this is not set then 0..1 is
        used. "0..1" gives you non-normalized pixels between 0 and 1. "-1..1"
        gives you non-normalized pixels between -1 and 1. "0..255" gives you
        non-normalized pixels between 0 and 255. "-128..127" gives you
        non-normalized pixels between -128 and 127. "torch" first scales pixels
        between 0 and 1, then applies normalization using the ImageNet dataset
        (same as `torchvision.transforms.Normalize()`).
        "bgr-subtract-imagenet-mean" scales to 0..255, reorders pixels to BGR,
        and subtracts the ImageNet mean from each channel.
      type: string
      enum:
        - 0..1
        - '-1..1'
        - '-128..127'
        - 0..255
        - torch
        - bgr-subtract-imagenet-mean
    OrganizationUser:
      allOf:
        - $ref: '#/components/schemas/User'
        - type: object
          required:
            - added
            - role
            - projectCount
            - datasets
          properties:
            added:
              type: string
              format: date-time
              example: '2019-08-31T17:32:28Z'
            role:
              $ref: '#/components/schemas/OrganizationMemberRole'
            projectCount:
              type: integer
            datasets:
              type: array
              items:
                type: string
            lastAccessToOrganization:
              type: string
              format: date-time
              description: Date when the user last accessed the organization data.
            lastOrganizationProjectAccessed:
              type: integer
              description: ID of the last project accessed by the user in the organization.
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
    OrganizationDatasetBucket:
      type: object
      required:
        - id
        - bucket
        - path
        - fullBucketPathDescription
        - dataItemNamingLevelsDeep
      properties:
        id:
          description: Bucket ID
          type: integer
        bucket:
          type: string
        path:
          description: Path in the bucket
          type: string
        fullBucketPathDescription:
          description: >-
            Full bucket path, incl. protocol (e.g. s3://bucket/path) - to be
            used in the UI
          type: string
        dataItemNamingLevelsDeep:
          description: >-
            Number of levels deep for data items, e.g. if you have folder
            "test/abc", with value 1 "test" will be a data item, with value 2
            "test/abc" will be a data item. Only used for "clinical" type.
          type: integer
    OrganizationDatasetTypeEnum:
      type: string
      enum:
        - clinical
        - files
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
    OrganizationMemberRole:
      type: string
      enum:
        - admin
        - member
        - guest
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