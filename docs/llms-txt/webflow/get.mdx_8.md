# Source: https://developers.webflow.com/data/reference/enterprise/workspace-audit-logs/get.mdx

# Get Workspace Audit Logs

GET https://api.webflow.com/v2/workspaces/{workspace_id_or_slug}/audit_logs

Get audit logs for a workspace.

<Warning title="Enterprise & workspace API token only">This endpoint requires an Enterprise workspace and a workspace token with the `workspace_activity:read` scope. Create a workspace token from your workspace dashboard integrations page to use this endpoint.</Warning>

Required scope | `workspace_activity:read`


Reference: https://developers.webflow.com/data/reference/enterprise/workspace-audit-logs/get

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /workspaces/{workspace_id_or_slug}/audit_logs:
    get:
      operationId: get-workspace-audit-logs
      summary: Get Workspace Audit Logs
      description: >
        Get audit logs for a workspace.


        <Warning title="Enterprise & workspace API token only">This endpoint
        requires an Enterprise workspace and a workspace token with the
        `workspace_activity:read` scope. Create a workspace token from your
        workspace dashboard integrations page to use this endpoint.</Warning>


        Required scope | `workspace_activity:read`
      tags:
        - subpackage_workspaces.subpackage_workspaces/auditLogs
      parameters:
        - name: workspace_id_or_slug
          in: path
          description: Unique identifier or slug for a Workspace
          required: true
          schema:
            type: string
            format: objectid
        - name: limit
          in: query
          description: 'Maximum number of records to be returned (max limit: 100)'
          required: false
          schema:
            type: integer
        - name: offset
          in: query
          description: >-
            Offset used for pagination if the results have more than limit
            records
          required: false
          schema:
            type: integer
        - name: sortOrder
          in: query
          description: Sorts the results by asc or desc
          required: false
          schema:
            $ref: >-
              #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetParametersSortOrder
        - name: eventType
          in: query
          description: The event type to filter by
          required: false
          schema:
            $ref: >-
              #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetParametersEventType
        - name: from
          in: query
          description: The start date to filter by
          required: false
          schema:
            type: string
            format: date-time
        - name: to
          in: query
          description: The end date to filter by
          required: false
          schema:
            type: string
            format: date-time
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: A list of workspace audit logs
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/workspaces_audit_logs_get-workspace-audit_logs_Response_200
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-workspace-audit-logsRequestUnauthorizedError
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-workspace-audit-logsRequestForbiddenError
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-workspace-audit-logsRequestNotFoundError
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-workspace-audit-logsRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-workspace-audit-logsRequestInternalServerError
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    WorkspacesWorkspaceIdOrSlugAuditLogsGetParametersSortOrder:
      type: string
      enum:
        - asc
        - desc
      title: WorkspacesWorkspaceIdOrSlugAuditLogsGetParametersSortOrder
    WorkspacesWorkspaceIdOrSlugAuditLogsGetParametersEventType:
      type: string
      enum:
        - user_access
        - custom_role
        - workspace_membership
        - site_membership
        - workspace_invitation
        - workspace_setting
      title: WorkspacesWorkspaceIdOrSlugAuditLogsGetParametersEventType
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf0Actor:
      type: object
      properties:
        id:
          type: string
        email:
          type: string
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf0Actor
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf0Workspace:
      type: object
      properties:
        id:
          type: string
        slug:
          type: string
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf0Workspace
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf0EventType:
      type: string
      enum:
        - user_access
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf0EventType
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf0EventSubType:
      type: string
      enum:
        - login
        - logout
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf0EventSubType
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf0PayloadMethod:
      type: string
      enum:
        - dashboard
        - sso
        - api
        - google
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf0PayloadMethod
    User access:
      type: object
      properties:
        method:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf0PayloadMethod
        location:
          type: string
          description: The geolocation based on the logged IP address
        ipAddress:
          type: string
          description: The captured IP address of the user
      title: User access
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItems0:
      type: object
      properties:
        timestamp:
          type: string
          format: date-time
        actor:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf0Actor
        workspace:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf0Workspace
        eventType:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf0EventType
        eventSubType:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf0EventSubType
        payload:
          $ref: '#/components/schemas/User access'
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItems0
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf1Actor:
      type: object
      properties:
        id:
          type: string
        email:
          type: string
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf1Actor
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf1Workspace:
      type: object
      properties:
        id:
          type: string
        slug:
          type: string
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf1Workspace
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf1EventType:
      type: string
      enum:
        - custom_role
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf1EventType
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf1EventSubType:
      type: string
      enum:
        - role_created
        - role_updated
        - role_deleted
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf1EventSubType
    Custom role:
      type: object
      properties:
        roleName:
          type: string
          description: The name of the custom role
        previousRoleName:
          type: string
          description: The previous name of the custom role
      title: Custom role
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItems1:
      type: object
      properties:
        timestamp:
          type: string
          format: date-time
        actor:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf1Actor
        workspace:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf1Workspace
        eventType:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf1EventType
        eventSubType:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf1EventSubType
        payload:
          $ref: '#/components/schemas/Custom role'
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItems1
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf2Actor:
      type: object
      properties:
        id:
          type: string
        email:
          type: string
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf2Actor
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf2Workspace:
      type: object
      properties:
        id:
          type: string
        slug:
          type: string
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf2Workspace
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf2EventType:
      type: string
      enum:
        - workspace_membership
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf2EventType
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf2EventSubType:
      type: string
      enum:
        - user_added
        - user_removed
        - user_role_updated
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf2EventSubType
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf2PayloadTargetUser:
      type: object
      properties:
        id:
          type: string
        email:
          type: string
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf2PayloadTargetUser
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf2PayloadMethod:
      type: string
      enum:
        - sso
        - dashboard
        - admin
        - access_request
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf2PayloadMethod
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf2PayloadUserType:
      type: string
      enum:
        - member
        - guest
        - reviewer
        - client
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf2PayloadUserType
    Workspace membership:
      type: object
      properties:
        targetUser:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf2PayloadTargetUser
        method:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf2PayloadMethod
        userType:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf2PayloadUserType
        roleName:
          type: string
          description: The name of the role that was assigned to the user
        previousRoleName:
          type: string
          description: The previous role that the user had
      title: Workspace membership
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItems2:
      type: object
      properties:
        timestamp:
          type: string
          format: date-time
        actor:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf2Actor
        workspace:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf2Workspace
        eventType:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf2EventType
        eventSubType:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf2EventSubType
        payload:
          $ref: '#/components/schemas/Workspace membership'
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItems2
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3Actor:
      type: object
      properties:
        id:
          type: string
        email:
          type: string
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3Actor
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3Workspace:
      type: object
      properties:
        id:
          type: string
        slug:
          type: string
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3Workspace
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3EventType:
      type: string
      enum:
        - site_membership
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3EventType
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3EventSubType:
      type: string
      enum:
        - user_added
        - user_removed
        - user_role_updated
        - user_granular_access_updated
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3EventSubType
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3PayloadSite:
      type: object
      properties:
        id:
          type: string
        slug:
          type: string
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3PayloadSite
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3PayloadTargetUser:
      type: object
      properties:
        id:
          type: string
        email:
          type: string
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3PayloadTargetUser
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3PayloadMethod:
      type: string
      enum:
        - sso
        - invite
        - scim
        - dashboard
        - admin
        - access_request
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3PayloadMethod
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3PayloadUserType:
      type: string
      enum:
        - member
        - guest
        - reviewer
        - client
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3PayloadUserType
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3PayloadGranularAccessType:
      type: string
      enum:
        - cms
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3PayloadGranularAccessType
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3PayloadGranularAccess:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        type:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3PayloadGranularAccessType
        restricted:
          type: boolean
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3PayloadGranularAccess
    Site membership:
      type: object
      properties:
        site:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3PayloadSite
        targetUser:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3PayloadTargetUser
        method:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3PayloadMethod
        userType:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3PayloadUserType
        roleName:
          type: string
          description: The name of the role that was assigned to the user
        previousRoleName:
          type: string
          description: The previous role that the user had
        granularAccess:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3PayloadGranularAccess
      title: Site membership
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItems3:
      type: object
      properties:
        timestamp:
          type: string
          format: date-time
        actor:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3Actor
        workspace:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3Workspace
        eventType:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3EventType
        eventSubType:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf3EventSubType
        payload:
          $ref: '#/components/schemas/Site membership'
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItems3
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4Actor:
      type: object
      properties:
        id:
          type: string
        email:
          type: string
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4Actor
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4Workspace:
      type: object
      properties:
        id:
          type: string
        slug:
          type: string
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4Workspace
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4EventType:
      type: string
      enum:
        - workspace_invitation
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4EventType
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4EventSubType:
      type: string
      enum:
        - invite_sent
        - invite_accepted
        - invite_updated
        - invite_canceled
        - invite_declined
        - access_request_accepted
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4EventSubType
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4PayloadTargetUser:
      type: object
      properties:
        id:
          type: string
        email:
          type: string
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4PayloadTargetUser
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4PayloadMethod:
      type: string
      enum:
        - sso
        - dashboard
        - admin
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4PayloadMethod
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4PayloadUserType:
      type: string
      enum:
        - member
        - guest
        - reviewer
        - client
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4PayloadUserType
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4PayloadTargetUsersItems:
      type: object
      properties:
        id:
          type: string
        email:
          type: string
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4PayloadTargetUsersItems
    Workspace invitation:
      type: object
      properties:
        targetUser:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4PayloadTargetUser
        method:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4PayloadMethod
        userType:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4PayloadUserType
        roleName:
          type: string
          description: The name of the role that was assigned to the user
        previousRoleName:
          type: string
          description: The previous role that the user had
        targetUsers:
          type: array
          items:
            $ref: >-
              #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4PayloadTargetUsersItems
      title: Workspace invitation
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItems4:
      type: object
      properties:
        timestamp:
          type: string
          format: date-time
        actor:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4Actor
        workspace:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4Workspace
        eventType:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4EventType
        eventSubType:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf4EventSubType
        payload:
          $ref: '#/components/schemas/Workspace invitation'
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItems4
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf5Actor:
      type: object
      properties:
        id:
          type: string
        email:
          type: string
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf5Actor
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf5Workspace:
      type: object
      properties:
        id:
          type: string
        slug:
          type: string
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf5Workspace
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf5EventType:
      type: string
      enum:
        - workspace_setting
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf5EventType
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf5EventSubType:
      type: string
      enum:
        - setting_updated
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf5EventSubType
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf5PayloadSetting:
      type: string
      enum:
        - ai_toggle
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf5PayloadSetting
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf5PayloadMethod:
      type: string
      enum:
        - dashboard
        - admin
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf5PayloadMethod
    Setting change:
      type: object
      properties:
        setting:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf5PayloadSetting
        previousValue:
          type: string
        value:
          type: string
        method:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf5PayloadMethod
      title: Setting change
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItems5:
      type: object
      properties:
        timestamp:
          type: string
          format: date-time
        actor:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf5Actor
        workspace:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf5Workspace
        eventType:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf5EventType
        eventSubType:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItemsOneOf5EventSubType
        payload:
          $ref: '#/components/schemas/Setting change'
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItems5
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItems:
      oneOf:
        - $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItems0
        - $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItems1
        - $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItems2
        - $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItems3
        - $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItems4
        - $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItems5
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItems
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaPagination:
      type: object
      properties:
        limit:
          type: integer
          description: The limit used for pagination
        offset:
          type: integer
          description: The offset used for pagination
        total:
          type: integer
          description: The total number of records
      required:
        - limit
        - offset
        - total
      description: Pagination object
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaPagination
    workspaces_audit_logs_get-workspace-audit_logs_Response_200:
      type: object
      properties:
        items:
          type: array
          items:
            $ref: >-
              #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaItemsItems
        pagination:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaPagination
          description: Pagination object
      title: workspaces_audit_logs_get-workspace-audit_logs_Response_200
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaCode:
      type: string
      enum:
        - bad_request
        - collection_not_found
        - conflict
        - duplicate_collection
        - duplicate_user_email
        - ecommerce_not_enabled
        - forbidden
        - forms_require_republish
        - incompatible_webhook_filter
        - internal_error
        - invalid_auth_version
        - invalid_credentials
        - invalid_domain
        - invalid_user_email
        - item_not_found
        - missing_scopes
        - no_domains
        - not_authorized
        - not_enterprise_plan_site
        - not_enterprise_plan_workspace
        - order_not_found
        - resource_not_found
        - too_many_requests
        - unsupported_version
        - unsupported_webhook_trigger_type
        - user_limit_reached
        - user_not_found
        - users_not_enabled
        - validation_error
      description: Error code
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaCode
    WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaDetailsItems
    Get-workspace-audit-logsRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-workspace-audit-logsRequestUnauthorizedError
    Get-workspace-audit-logsRequestForbiddenError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-workspace-audit-logsRequestForbiddenError
    Get-workspace-audit-logsRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-workspace-audit-logsRequestNotFoundError
    Get-workspace-audit-logsRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-workspace-audit-logsRequestTooManyRequestsError
    Get-workspace-audit-logsRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/WorkspacesWorkspaceIdOrSlugAuditLogsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-workspace-audit-logsRequestInternalServerError
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import datetime

from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.workspaces.audit_logs.get_workspace_audit_logs(
    workspace_id_or_slug="hitchhikers-workspace",
    limit=1,
    offset=1,
    sort_order="asc",
    event_type="user_access",
    from_=datetime.datetime.fromisoformat(
        "2025-06-22 16:00:31+00:00",
    ),
    to=datetime.datetime.fromisoformat(
        "2025-07-22 16:00:31+00:00",
    ),
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.workspaces.auditLogs.getWorkspaceAuditLogs("hitchhikers-workspace", {
    limit: 1,
    offset: 1,
    sortOrder: "asc",
    eventType: "user_access",
    from: new Date("2025-06-22T16:00:31.000Z"),
    to: new Date("2025-07-22T16:00:31.000Z")
});

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/workspaces/hitchhikers-workspace/audit_logs?limit=100&offset=0&eventType=user_access&from=2025-06-22T16%3A00%3A31Z&to=2025-07-22T16%3A00%3A31Z"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.webflow.com/v2/workspaces/hitchhikers-workspace/audit_logs?limit=100&offset=0&eventType=user_access&from=2025-06-22T16%3A00%3A31Z&to=2025-07-22T16%3A00%3A31Z")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.webflow.com/v2/workspaces/hitchhikers-workspace/audit_logs?limit=100&offset=0&eventType=user_access&from=2025-06-22T16%3A00%3A31Z&to=2025-07-22T16%3A00%3A31Z")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/v2/workspaces/hitchhikers-workspace/audit_logs?limit=100&offset=0&eventType=user_access&from=2025-06-22T16%3A00%3A31Z&to=2025-07-22T16%3A00%3A31Z', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/workspaces/hitchhikers-workspace/audit_logs?limit=100&offset=0&eventType=user_access&from=2025-06-22T16%3A00%3A31Z&to=2025-07-22T16%3A00%3A31Z");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/workspaces/hitchhikers-workspace/audit_logs?limit=100&offset=0&eventType=user_access&from=2025-06-22T16%3A00%3A31Z&to=2025-07-22T16%3A00%3A31Z")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```