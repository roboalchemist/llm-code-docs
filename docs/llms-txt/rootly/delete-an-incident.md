# Source: https://docs.rootly.com/api-reference/incidents/delete-an-incident.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete an incident

> Delete a specific incident by id



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json delete /v1/incidents/{id}
openapi: 3.0.1
info:
  title: Rootly API v1
  version: v1
  description: >+
    # How to generate an API Key?

    - **Organization dropdown** > **Organization Settings** > **API Keys**


    # JSON:API Specification

    Rootly is using **JSON:API** (https://jsonapi.org) specification:

    - JSON:API is a specification for how a client should request that resources
    be fetched or modified, and how a server should respond to those requests.

    - JSON:API is designed to minimize both the number of requests and the
    amount of data transmitted between clients and servers. This efficiency is
    achieved without compromising readability, flexibility, or discoverability.

    - JSON:API requires use of the JSON:API media type
    (**application/vnd.api+json**) for exchanging data.


    # Authentication and Requests

    We use standard HTTP Authentication over HTTPS to authorize your requests.

    ```
      curl --request GET \
    --header 'Content-Type: application/vnd.api+json' \

    --header 'Authorization: Bearer YOUR-TOKEN' \

    --url https://api.rootly.com/v1/incidents

    ```


    <br/>


    # Rate limiting

    - There is a default limit of **5** **GET**, **HEAD**, and **OPTIONS** calls
    **per API key** every **60 seconds** (0 hours). The limit is calculated over
    a **0-hour sliding window** looking back from the current time. While the
    limit can be configured to support higher thresholds, you must first contact
    your **Rootly Customer Success Manager** to make any adjustments.

    - There is a default limit of **3** **POST**, **PUT**, **PATCH** or
    **DELETE** calls **per API key** every **60 seconds** (0 hours). The limit
    is calculated over a **0-hour sliding window** looking back from the current
    time. While the limit can be configured to support higher thresholds, you
    must first contact your **Rootly Customer Success Manager** to make any
    adjustments.

    - When rate limits are exceeded, the API will return a **429 Too Many
    Requests** HTTP status code with the response: `{"error": "Rate limit
    exceeded. Try again later."}`

    - **X-RateLimit headers** are included in every API response, providing
    real-time rate limit information:
      - **X-RateLimit-Limit** - The maximum number of requests permitted and the time window (e.g., "1000, 1000;window=3600" for 1000 requests per hour)
      - **X-RateLimit-Remaining** - The number of requests remaining in the current rate limit window
      - **X-RateLimit-Used** - The number of requests already made in the current window
      - **X-RateLimit-Reset** - The time at which the current rate limit window resets, in UTC epoch seconds

    # Pagination

    - Pagination is supported for all endpoints that return a collection of
    items.

    - Pagination is controlled by the **page** query parameter


    ## Example

    ```
      curl --request GET \
    --header 'Content-Type: application/vnd.api+json' \

    --header 'Authorization: Bearer YOUR-TOKEN' \

    --url https://api.rootly.com/v1/incidents?page[number]=1&page[size]=10

    ```

  x-logo:
    url: https://rootly-heroku.s3.us-east-1.amazonaws.com/swagger/v1/logo.png
servers:
  - url: https://api.rootly.com
security: []
paths:
  /v1/incidents/{id}:
    parameters:
      - name: id
        in: path
        schema:
          anyOf:
            - type: string
              format: uuid
              description: Resource UUID
            - type: string
              pattern: ^[a-z0-9_-]+$
              description: Resource slug
        required: true
    delete:
      tags:
        - Incidents
      summary: Delete an incident
      description: Delete a specific incident by id
      operationId: deleteIncident
      responses:
        '200':
          description: incident deleted
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/incident_response'
        '404':
          description: resource not found
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/errors_list'
      security:
        - bearer_auth: []
components:
  schemas:
    incident_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the incident
            type:
              type: string
              enum:
                - incidents
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/incident'
          required:
            - id
            - type
            - attributes
      required:
        - data
    errors_list:
      type: object
      properties:
        errors:
          type: array
          items:
            type: object
            properties:
              title:
                type: string
              status:
                type: string
              code:
                type: string
                nullable: true
              detail:
                type: string
                nullable: true
            required:
              - title
              - status
    incident:
      type: object
      properties:
        id:
          type: string
          description: Unique ID of the incident
        sequential_id:
          type: integer
          description: Sequential ID of the incident
        title:
          type: string
          description: The title of the incident
        kind:
          type: string
          description: The kind of the incident
        slug:
          type: string
          description: The slug of the incident
        parent_incident_id:
          type: string
          description: ID of parent incident
          nullable: true
        duplicate_incident_id:
          type: string
          description: ID of duplicated incident
          nullable: true
        summary:
          type: string
          description: The summary of the incident
          nullable: true
        private:
          type: boolean
          description: The visibility of the incident
          default: false
        source:
          type: string
          description: The source of the incident
          nullable: true
        status:
          type: string
          description: The status of the incident
          nullable: true
        url:
          type: string
          description: The url to the incident
          nullable: true
        short_url:
          type: string
          description: The short url to the incident
          nullable: true
        public_title:
          type: string
          description: The public title of the incident
          nullable: true
        user:
          type: object
          description: The user who created the incident
          nullable: true
        severity:
          type: object
          description: The Severity of the incident
          allOf:
            - $ref: '#/components/schemas/severity_response'
          nullable: true
        environments:
          type: array
          description: The Environments of the incident
          items:
            type: object
            allOf:
              - $ref: '#/components/schemas/environment_response'
          nullable: true
        incident_types:
          type: array
          description: The Incident Types of the incident
          items:
            type: object
            allOf:
              - $ref: '#/components/schemas/incident_type_response'
          nullable: true
        services:
          type: array
          description: The Services of the incident
          items:
            type: object
            allOf:
              - $ref: '#/components/schemas/service_response'
          nullable: true
        functionalities:
          type: array
          description: The Functionalities of the incident
          items:
            type: object
            allOf:
              - $ref: '#/components/schemas/functionality_response'
          nullable: true
        groups:
          type: array
          description: The Teams of to the incident
          items:
            type: object
            allOf:
              - $ref: '#/components/schemas/team_response'
          nullable: true
        labels:
          type: object
          description: >-
            Labels to attach to the incidents. eg: {"platform":"osx", "version":
            "1.29"}
          nullable: true
        slack_channel_id:
          type: string
          description: Slack channel id
          nullable: true
        slack_channel_name:
          type: string
          description: Slack channel name
          nullable: true
        slack_channel_url:
          type: string
          description: Slack channel url
          nullable: true
        slack_channel_short_url:
          type: string
          description: Slack channel short url
          nullable: true
        slack_channel_deep_link:
          type: string
          description: Slack channel deep link
          nullable: true
        slack_channel_archived:
          type: boolean
          description: Whether the Slack channel is archived
          nullable: true
        slack_last_message_ts:
          type: string
          description: Timestamp of last Slack message
          nullable: true
        zoom_meeting_id:
          type: string
          description: Zoom meeting ID
          nullable: true
        zoom_meeting_start_url:
          type: string
          description: Zoom meeting start URL
          nullable: true
        zoom_meeting_join_url:
          type: string
          description: Zoom meeting join URL
          nullable: true
        zoom_meeting_password:
          type: string
          description: Zoom meeting password
          nullable: true
        zoom_meeting_pstn_password:
          type: string
          description: Zoom meeting PSTN password
          nullable: true
        zoom_meeting_h323_password:
          type: string
          description: Zoom meeting H323 password
          nullable: true
        zoom_meeting_global_dial_in_numbers:
          type: array
          description: Zoom meeting global dial-in numbers
          items:
            type: string
          nullable: true
        google_drive_id:
          type: string
          description: Google Drive document ID
          nullable: true
        google_drive_parent_id:
          type: string
          description: Google Drive parent folder ID
          nullable: true
        google_drive_url:
          type: string
          description: Google Drive URL
          nullable: true
        google_meeting_id:
          type: string
          description: Google meeting ID
          nullable: true
        google_meeting_url:
          type: string
          description: Google meeting URL
          nullable: true
        jira_issue_key:
          type: string
          description: Jira issue key
          nullable: true
        jira_issue_id:
          type: string
          description: Jira issue ID
          nullable: true
        jira_issue_url:
          type: string
          description: Jira issue URL
          nullable: true
        github_issue_id:
          type: string
          description: GitHub issue ID
          nullable: true
        github_issue_url:
          type: string
          description: GitHub issue URL
          nullable: true
        gitlab_issue_id:
          type: string
          description: GitLab issue ID
          nullable: true
        gitlab_issue_url:
          type: string
          description: GitLab issue URL
          nullable: true
        asana_task_id:
          type: string
          description: Asana task ID
          nullable: true
        asana_task_url:
          type: string
          description: Asana task URL
          nullable: true
        linear_issue_id:
          type: string
          description: Linear issue ID
          nullable: true
        linear_issue_url:
          type: string
          description: Linear issue URL
          nullable: true
        trello_card_id:
          type: string
          description: Trello card ID
          nullable: true
        trello_card_url:
          type: string
          description: Trello card URL
          nullable: true
        zendesk_ticket_id:
          type: string
          description: Zendesk ticket ID
          nullable: true
        zendesk_ticket_url:
          type: string
          description: Zendesk ticket URL
          nullable: true
        pagerduty_incident_id:
          type: string
          description: PagerDuty incident ID
          nullable: true
        pagerduty_incident_number:
          type: string
          description: PagerDuty incident number
          nullable: true
        pagerduty_incident_url:
          type: string
          description: PagerDuty incident URL
          nullable: true
        opsgenie_incident_id:
          type: string
          description: Opsgenie incident ID
          nullable: true
        opsgenie_incident_url:
          type: string
          description: Opsgenie incident URL
          nullable: true
        opsgenie_alert_id:
          type: string
          description: Opsgenie alert ID
          nullable: true
        opsgenie_alert_url:
          type: string
          description: Opsgenie alert URL
          nullable: true
        service_now_incident_id:
          type: string
          description: ServiceNow incident ID
          nullable: true
        service_now_incident_key:
          type: string
          description: ServiceNow incident key
          nullable: true
        service_now_incident_url:
          type: string
          description: ServiceNow incident URL
          nullable: true
        mattermost_channel_id:
          type: string
          description: Mattermost channel ID
          nullable: true
        mattermost_channel_name:
          type: string
          description: Mattermost channel name
          nullable: true
        mattermost_channel_url:
          type: string
          description: Mattermost channel URL
          nullable: true
        confluence_page_id:
          type: string
          description: Confluence page ID
          nullable: true
        confluence_page_url:
          type: string
          description: Confluence page URL
          nullable: true
        datadog_notebook_id:
          type: string
          description: Datadog notebook ID
          nullable: true
        datadog_notebook_url:
          type: string
          description: Datadog notebook URL
          nullable: true
        shortcut_story_id:
          type: string
          description: Shortcut story ID
          nullable: true
        shortcut_story_url:
          type: string
          description: Shortcut story URL
          nullable: true
        shortcut_task_id:
          type: string
          description: Shortcut task ID
          nullable: true
        shortcut_task_url:
          type: string
          description: Shortcut task URL
          nullable: true
        motion_task_id:
          type: string
          description: Motion task ID
          nullable: true
        motion_task_url:
          type: string
          description: Motion task URL
          nullable: true
        clickup_task_id:
          type: string
          description: ClickUp task ID
          nullable: true
        clickup_task_url:
          type: string
          description: ClickUp task URL
          nullable: true
        victor_ops_incident_id:
          type: string
          description: VictorOps incident ID
          nullable: true
        victor_ops_incident_url:
          type: string
          description: VictorOps incident URL
          nullable: true
        quip_page_id:
          type: string
          description: Quip page ID
          nullable: true
        quip_page_url:
          type: string
          description: Quip page URL
          nullable: true
        sharepoint_page_id:
          type: string
          description: SharePoint page ID
          nullable: true
        sharepoint_page_url:
          type: string
          description: SharePoint page URL
          nullable: true
        airtable_base_key:
          type: string
          description: Airtable base key
          nullable: true
        airtable_table_name:
          type: string
          description: Airtable table name
          nullable: true
        airtable_record_id:
          type: string
          description: Airtable record ID
          nullable: true
        airtable_record_url:
          type: string
          description: Airtable record URL
          nullable: true
        freshservice_ticket_id:
          type: string
          description: Freshservice ticket ID
          nullable: true
        freshservice_ticket_url:
          type: string
          description: Freshservice ticket URL
          nullable: true
        freshservice_task_id:
          type: string
          description: Freshservice task ID
          nullable: true
        freshservice_task_url:
          type: string
          description: Freshservice task URL
          nullable: true
        mitigation_message:
          type: string
          description: How was the incident mitigated?
          nullable: true
        resolution_message:
          type: string
          description: How was the incident resolved?
          nullable: true
        cancellation_message:
          type: string
          description: Why was the incident cancelled?
          nullable: true
        scheduled_for:
          type: string
          description: Date of when the maintenance begins
          nullable: true
        scheduled_until:
          type: string
          description: Date of when the maintenance ends
          nullable: true
        muted_service_ids:
          type: array
          description: >-
            The Service IDs to mute alerts for during maintenance. Alerts for
            these services will still be triggered and attached to the incident,
            but won't page responders.
          items:
            type: string
          nullable: true
        retrospective_progress_status:
          type: string
          description: The status of the retrospective progress
          nullable: true
          enum:
            - not_started
            - active
            - completed
            - skipped
        in_triage_by:
          type: object
          description: The user who triaged the incident
          nullable: true
        started_by:
          type: object
          description: The user who started the incident
          nullable: true
        mitigated_by:
          type: object
          description: The user who mitigated the incident
          nullable: true
        resolved_by:
          type: object
          description: The user who resolved the incident
          nullable: true
        closed_by:
          type: object
          description: The user who closed the incident
          nullable: true
        cancelled_by:
          type: object
          description: The user who cancelled the incident
          nullable: true
        in_triage_at:
          type: string
          description: Date of triage
          nullable: true
        started_at:
          type: string
          description: Date of start
          nullable: true
        detected_at:
          type: string
          description: Date of detection
          nullable: true
        acknowledged_at:
          type: string
          description: Date of acknowledgment
          nullable: true
        mitigated_at:
          type: string
          description: Date of mitigation
          nullable: true
        resolved_at:
          type: string
          description: Date of resolution
          nullable: true
        closed_at:
          type: string
          description: Date of closure
          nullable: true
        cancelled_at:
          type: string
          description: Date of cancellation
          nullable: true
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
      required:
        - title
        - created_at
        - updated_at
    severity_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the severity
            type:
              type: string
              enum:
                - severities
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/severity'
          required:
            - id
            - type
            - attributes
      required:
        - data
    environment_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the environment
            type:
              type: string
              enum:
                - environments
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/environment'
          required:
            - id
            - type
            - attributes
      required:
        - data
    incident_type_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the incident type
            type:
              type: string
              enum:
                - incident_types
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/incident_type'
          required:
            - id
            - type
            - attributes
      required:
        - data
    service_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the service
            type:
              type: string
              enum:
                - services
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/service'
          required:
            - id
            - type
            - attributes
      required:
        - data
    functionality_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the functionality
            type:
              type: string
              enum:
                - functionalities
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/functionality'
          required:
            - id
            - type
            - attributes
      required:
        - data
    team_response:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
              description: Unique ID of the team
            type:
              type: string
              enum:
                - groups
            attributes:
              type: object
              allOf:
                - $ref: '#/components/schemas/team'
          required:
            - id
            - type
            - attributes
      required:
        - data
    severity:
      type: object
      properties:
        name:
          type: string
          description: The name of the severity
        slug:
          type: string
          description: The slug of the severity
        description:
          type: string
          description: The description of the severity
          nullable: true
        severity:
          type: string
          description: The severity of the severity
          enum:
            - critical
            - high
            - medium
            - low
        color:
          type: string
          description: The hex color of the severity
          nullable: true
        position:
          type: integer
          description: Position of the severity
          nullable: true
        notify_emails:
          type: array
          description: Emails to attach to the severity
          items:
            type: string
          nullable: true
        slack_channels:
          type: array
          description: Slack Channels associated with this severity
          items:
            type: object
            properties:
              id:
                type: string
                description: Slack channel ID
              name:
                type: string
                description: Slack channel name
            required:
              - id
              - name
          nullable: true
        slack_aliases:
          type: array
          description: Slack Aliases associated with this severity
          items:
            type: object
            properties:
              id:
                type: string
                description: Slack alias ID
              name:
                type: string
                description: Slack alias name
            required:
              - id
              - name
          nullable: true
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
      required:
        - name
        - created_at
        - updated_at
    environment:
      type: object
      properties:
        name:
          type: string
          description: The name of the environment
        slug:
          type: string
          description: The slug of the environment
        description:
          type: string
          description: The description of the environment
          nullable: true
        notify_emails:
          type: array
          description: Emails attached to the environment
          items:
            type: string
          nullable: true
        color:
          type: string
          description: The hex color of the environment
          nullable: true
        position:
          type: integer
          description: Position of the environment
          nullable: true
        slack_channels:
          type: array
          description: Slack Channels associated with this environment
          items:
            type: object
            properties:
              id:
                type: string
                description: Slack channel ID
              name:
                type: string
                description: Slack channel name
            required:
              - id
              - name
          nullable: true
        slack_aliases:
          type: array
          description: Slack Aliases associated with this environment
          items:
            type: object
            properties:
              id:
                type: string
                description: Slack alias ID
              name:
                type: string
                description: Slack alias name
            required:
              - id
              - name
          nullable: true
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
        properties:
          type: array
          items:
            type: object
            description: Set a value for a catalog property
            properties:
              catalog_property_id:
                type: string
                description: Catalog property ID
              value:
                type: string
                description: The property value
            required:
              - catalog_property_id
              - value
          description: Array of property values for this environment.
          nullable: true
      required:
        - name
        - created_at
        - updated_at
    incident_type:
      type: object
      properties:
        name:
          type: string
          description: The name of the incident type
        slug:
          type: string
          description: The slug of the incident type
        description:
          type: string
          description: The description of the incident type
          nullable: true
        color:
          type: string
          description: The hex color of the incident type
          nullable: true
        position:
          type: integer
          description: Position of the incident type
          nullable: true
        notify_emails:
          type: array
          description: Emails to attach to the incident type
          items:
            type: string
          nullable: true
        slack_channels:
          type: array
          description: Slack Channels associated with this incident type
          items:
            type: object
            properties:
              id:
                type: string
                description: Slack channel ID
              name:
                type: string
                description: Slack channel name
            required:
              - id
              - name
          nullable: true
        slack_aliases:
          type: array
          description: Slack Aliases associated with this incident type
          items:
            type: object
            properties:
              id:
                type: string
                description: Slack alias ID
              name:
                type: string
                description: Slack alias name
            required:
              - id
              - name
          nullable: true
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
        properties:
          type: array
          items:
            type: object
            description: Set a value for a catalog property
            properties:
              catalog_property_id:
                type: string
                description: Catalog property ID
              value:
                type: string
                description: The property value
            required:
              - catalog_property_id
              - value
          description: Array of property values for this incident type.
      required:
        - name
        - created_at
        - updated_at
    service:
      type: object
      properties:
        name:
          type: string
          description: The name of the service
        slug:
          type: string
          description: The slug of the service
        description:
          type: string
          description: The description of the service
          nullable: true
        public_description:
          type: string
          description: The public description of the service
          nullable: true
        notify_emails:
          type: array
          description: Emails attached to the service
          items:
            type: string
          nullable: true
        color:
          type: string
          description: The hex color of the service
          nullable: true
        position:
          type: integer
          description: Position of the service
          nullable: true
        backstage_id:
          type: string
          description: >-
            The Backstage entity id associated to this service. eg:
            :namespace/:kind/:entity_name
          nullable: true
        external_id:
          type: string
          description: The external id associated to this service
          nullable: true
        pagerduty_id:
          type: string
          description: The PagerDuty service id associated to this service
          nullable: true
        opsgenie_id:
          type: string
          description: The Opsgenie service id associated to this service
          nullable: true
        cortex_id:
          type: string
          description: The Cortex group id associated to this service
          nullable: true
        service_now_ci_sys_id:
          type: string
          description: The Service Now CI sys id associated to this service
          nullable: true
        github_repository_name:
          type: string
          description: >-
            The GitHub repository name associated to this service. eg:
            rootlyhq/my-service
          nullable: true
        github_repository_branch:
          type: string
          description: 'The GitHub repository branch associated to this service. eg: main'
          nullable: true
        gitlab_repository_name:
          type: string
          description: >-
            The GitLab repository name associated to this service. eg:
            rootlyhq/my-service
          nullable: true
        gitlab_repository_branch:
          type: string
          description: 'The GitLab repository branch associated to this service. eg: main'
          nullable: true
        kubernetes_deployment_name:
          type: string
          description: >-
            The Kubernetes deployment name associated to this service. eg:
            namespace/deployment-name
          nullable: true
        environment_ids:
          type: array
          description: Environments associated with this service
          items:
            type: string
          nullable: true
        service_ids:
          type: array
          description: Services dependent on this service
          items:
            type: string
          nullable: true
        owner_group_ids:
          type: array
          description: Owner Teams associated with this service
          items:
            type: string
          nullable: true
        owner_user_ids:
          type: array
          description: Owner Users associated with this service
          items:
            type: integer
          nullable: true
        alert_urgency_id:
          type: string
          description: The alert urgency id of the service
          nullable: true
        escalation_policy_id:
          type: string
          description: The escalation policy id of the service
          nullable: true
        alerts_email_enabled:
          type: boolean
          description: Enable alerts through email
          nullable: true
        alerts_email_address:
          type: string
          description: Email generated to send alerts to
          nullable: true
        slack_channels:
          type: array
          description: Slack Channels associated with this service
          items:
            type: object
            properties:
              id:
                type: string
                description: Slack channel ID
              name:
                type: string
                description: Slack channel name
            required:
              - id
              - name
          nullable: true
        slack_aliases:
          type: array
          description: Slack Aliases associated with this service
          items:
            type: object
            properties:
              id:
                type: string
                description: Slack alias ID
              name:
                type: string
                description: Slack alias name
            required:
              - id
              - name
          nullable: true
        alert_broadcast_enabled:
          type: boolean
          description: Enable alerts to be broadcasted to a specific channel
          nullable: true
        alert_broadcast_channel:
          type: object
          description: Slack channel to broadcast alerts to
          properties:
            id:
              type: string
              description: Slack channel ID
            name:
              type: string
              description: Slack channel name
          nullable: true
        incident_broadcast_enabled:
          type: boolean
          description: Enable incidents to be broadcasted to a specific channel
          nullable: true
        incident_broadcast_channel:
          type: object
          description: Slack channel to broadcast incidents to
          properties:
            id:
              type: string
              description: Slack channel ID
            name:
              type: string
              description: Slack channel name
          nullable: true
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
        properties:
          type: array
          items:
            type: object
            description: Set a value for a catalog property
            properties:
              catalog_property_id:
                type: string
                description: Catalog property ID
              value:
                type: string
                description: The property value
            required:
              - catalog_property_id
              - value
          description: Array of property values for this service.
          nullable: true
      required:
        - name
        - created_at
        - updated_at
    functionality:
      type: object
      properties:
        name:
          type: string
          description: The name of the functionality
        slug:
          type: string
          description: The slug of the functionality
        description:
          type: string
          description: The description of the functionality
          nullable: true
        public_description:
          type: string
          description: The public description of the functionality
          nullable: true
        notify_emails:
          type: array
          description: Emails attached to the functionality
          items:
            type: string
          nullable: true
        color:
          type: string
          description: The hex color of the functionality
          nullable: true
        backstage_id:
          type: string
          description: >-
            The Backstage entity id associated to this functionality. eg:
            :namespace/:kind/:entity_name
          nullable: true
        external_id:
          type: string
          description: The external id associated to this functionality
          nullable: true
        pagerduty_id:
          type: string
          description: The PagerDuty service id associated to this functionality
          nullable: true
        opsgenie_id:
          type: string
          description: The Opsgenie service id associated to this functionality
          nullable: true
        opsgenie_team_id:
          type: string
          description: The Opsgenie team id associated to this functionality
          nullable: true
        cortex_id:
          type: string
          description: The Cortex group id associated to this functionality
          nullable: true
        service_now_ci_sys_id:
          type: string
          description: The Service Now CI sys id associated to this functionality
          nullable: true
        position:
          type: integer
          description: Position of the functionality
          nullable: true
        environment_ids:
          type: array
          description: Environments associated with this functionality
          items:
            type: string
          nullable: true
        service_ids:
          type: array
          description: Services associated with this functionality
          items:
            type: string
          nullable: true
        owner_group_ids:
          type: array
          description: Owner Teams associated with this functionality
          items:
            type: string
          nullable: true
        owner_user_ids:
          type: array
          description: Owner Users associated with this functionality
          items:
            type: integer
          nullable: true
        slack_channels:
          type: array
          description: Slack Channels associated with this functionality
          items:
            type: object
            properties:
              id:
                type: string
                description: Slack channel ID
              name:
                type: string
                description: Slack channel name
            required:
              - id
              - name
          nullable: true
        slack_aliases:
          type: array
          description: Slack Aliases associated with this functionality
          items:
            type: object
            properties:
              id:
                type: string
                description: Slack alias ID
              name:
                type: string
                description: Slack alias name
            required:
              - id
              - name
          nullable: true
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
        properties:
          type: array
          items:
            type: object
            description: Set a value for a catalog property
            properties:
              catalog_property_id:
                type: string
                description: Catalog property ID
              value:
                type: string
                description: The property value
            required:
              - catalog_property_id
              - value
          description: Array of property values for this functionality.
          nullable: true
      required:
        - name
        - created_at
        - updated_at
    team:
      type: object
      properties:
        name:
          type: string
          description: The name of the team
        slug:
          type: string
        description:
          type: string
          description: The description of the team
          nullable: true
        notify_emails:
          type: array
          description: Emails to attach to the team
          items:
            type: string
          nullable: true
        color:
          type: string
          description: The hex color of the team
          nullable: true
        position:
          type: integer
          description: Position of the team
          nullable: true
        backstage_id:
          type: string
          description: >-
            The Backstage entity id associated to this team. eg:
            :namespace/:kind/:entity_name
          nullable: true
        external_id:
          type: string
          description: The external id associated to this team
          nullable: true
        pagerduty_id:
          type: string
          description: The PagerDuty group id associated to this team
          nullable: true
        pagerduty_service_id:
          type: string
          description: The PagerDuty service id associated to this team
          nullable: true
        opsgenie_id:
          type: string
          description: The Opsgenie group id associated to this team
          nullable: true
        victor_ops_id:
          type: string
          description: The VictorOps group id associated to this team
          nullable: true
        pagertree_id:
          type: string
          description: The PagerTree group id associated to this team
          nullable: true
        cortex_id:
          type: string
          description: The Cortex group id associated to this team
          nullable: true
        service_now_ci_sys_id:
          type: string
          description: The Service Now CI sys id associated to this team
          nullable: true
        user_ids:
          type: array
          description: The user ids of the members of this team.
          items:
            type: integer
          nullable: true
        admin_ids:
          type: array
          description: >-
            The user ids of the admins of this team. These users must also be
            present in user_ids attribute.
          items:
            type: integer
          nullable: true
        alerts_email_enabled:
          type: boolean
          description: Enable alerts through email
          nullable: true
        alerts_email_address:
          type: string
          description: Email generated to send alerts to
          nullable: true
        alert_urgency_id:
          type: string
          description: The alert urgency id of the team
          nullable: true
        slack_channels:
          type: array
          description: Slack Channels associated with this team
          items:
            type: object
            properties:
              id:
                type: string
                description: Slack channel ID
              name:
                type: string
                description: Slack channel name
            required:
              - id
              - name
          nullable: true
        slack_aliases:
          type: array
          description: Slack Aliases associated with this team
          items:
            type: object
            properties:
              id:
                type: string
                description: Slack alias ID
              name:
                type: string
                description: Slack alias name
            required:
              - id
              - name
          nullable: true
        alert_broadcast_enabled:
          type: boolean
          description: Enable alerts to be broadcasted to a specific channel
          nullable: true
        alert_broadcast_channel:
          type: object
          description: Slack channel to broadcast alerts to
          properties:
            id:
              type: string
              description: Slack channel ID
            name:
              type: string
              description: Slack channel name
          nullable: true
        incident_broadcast_enabled:
          type: boolean
          description: Enable incidents to be broadcasted to a specific channel
          nullable: true
        incident_broadcast_channel:
          type: object
          description: Slack channel to broadcast incidents to
          properties:
            id:
              type: string
              description: Slack channel ID
            name:
              type: string
              description: Slack channel name
          nullable: true
        auto_add_members_when_attached:
          type: boolean
          description: Auto add members to incident channel when team is attached
          nullable: true
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
        properties:
          type: array
          items:
            type: object
            description: Set a value for a catalog property
            properties:
              catalog_property_id:
                type: string
                description: Catalog property ID
              value:
                type: string
                description: The property value
            required:
              - catalog_property_id
              - value
          description: Array of property values for this team.
          nullable: true
      required:
        - name
        - created_at
        - updated_at
  securitySchemes:
    bearer_auth:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).