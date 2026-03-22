# Source: https://docs.rootly.com/api-reference/workflowtasks/list-workflow-tasks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List workflow tasks

> List workflow tasks



## OpenAPI

````yaml https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json get /v1/workflows/{workflow_id}/workflow_tasks
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
  /v1/workflows/{workflow_id}/workflow_tasks:
    parameters:
      - name: workflow_id
        in: path
        required: true
        schema:
          type: string
    get:
      tags:
        - WorkflowTasks
      summary: List workflow tasks
      description: List workflow tasks
      operationId: listWorkflowTasks
      parameters:
        - name: include
          in: query
          required: false
          schema:
            type: string
        - name: page[number]
          in: query
          required: false
          schema:
            type: integer
        - name: page[size]
          in: query
          required: false
          schema:
            type: integer
        - name: filter[search]
          in: query
          required: false
          schema:
            type: string
        - name: filter[name]
          in: query
          required: false
          schema:
            type: string
        - name: filter[slug]
          in: query
          required: false
          schema:
            type: string
      responses:
        '200':
          description: success
          content:
            application/vnd.api+json:
              schema:
                $ref: '#/components/schemas/workflow_task_list'
      security:
        - bearer_auth: []
components:
  schemas:
    workflow_task_list:
      type: object
      properties:
        data:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
                description: Unique ID of the workflow task
              type:
                type: string
                enum:
                  - workflow_tasks
              attributes:
                type: object
                allOf:
                  - $ref: '#/components/schemas/workflow_task'
            required:
              - id
              - type
              - attributes
        links:
          type: object
          allOf:
            - $ref: '#/components/schemas/links'
        meta:
          type: object
          allOf:
            - $ref: '#/components/schemas/meta'
      required:
        - data
        - links
        - meta
    workflow_task:
      type: object
      properties:
        workflow_id:
          type: string
          description: The ID of the parent workflow
        task_params:
          oneOf:
            - $ref: '#/components/schemas/add_action_item_task_params'
            - $ref: '#/components/schemas/update_action_item_task_params'
            - $ref: '#/components/schemas/add_role_task_params'
            - $ref: '#/components/schemas/add_slack_bookmark_task_params'
            - $ref: '#/components/schemas/add_team_task_params'
            - $ref: '#/components/schemas/add_to_timeline_task_params'
            - $ref: '#/components/schemas/archive_slack_channels_task_params'
            - $ref: '#/components/schemas/attach_datadog_dashboards_task_params'
            - $ref: '#/components/schemas/auto_assign_role_opsgenie_task_params'
            - $ref: '#/components/schemas/auto_assign_role_rootly_task_params'
            - $ref: '#/components/schemas/auto_assign_role_pagerduty_task_params'
            - $ref: '#/components/schemas/update_pagerduty_incident_task_params'
            - $ref: '#/components/schemas/create_pagerduty_status_update_task_params'
            - $ref: '#/components/schemas/create_pagertree_alert_task_params'
            - $ref: '#/components/schemas/update_pagertree_alert_task_params'
            - $ref: '#/components/schemas/auto_assign_role_victor_ops_task_params'
            - $ref: '#/components/schemas/call_people_task_params'
            - $ref: '#/components/schemas/create_airtable_table_record_task_params'
            - $ref: '#/components/schemas/create_asana_subtask_task_params'
            - $ref: '#/components/schemas/create_asana_task_task_params'
            - $ref: '#/components/schemas/create_confluence_page_task_params'
            - $ref: '#/components/schemas/create_datadog_notebook_task_params'
            - $ref: '#/components/schemas/create_coda_page_task_params'
            - $ref: '#/components/schemas/create_dropbox_paper_page_task_params'
            - $ref: '#/components/schemas/create_github_issue_task_params'
            - $ref: '#/components/schemas/create_gitlab_issue_task_params'
            - $ref: '#/components/schemas/create_outlook_event_task_params'
            - $ref: '#/components/schemas/create_google_calendar_event_task_params'
            - $ref: '#/components/schemas/update_google_docs_page_task_params'
            - $ref: '#/components/schemas/update_coda_page_task_params'
            - $ref: '#/components/schemas/update_google_calendar_event_task_params'
            - $ref: '#/components/schemas/create_sharepoint_page_task_params'
            - $ref: '#/components/schemas/create_google_docs_page_task_params'
            - $ref: '#/components/schemas/create_google_docs_permissions_task_params'
            - $ref: '#/components/schemas/remove_google_docs_permissions_task_params'
            - $ref: '#/components/schemas/create_quip_page_task_params'
            - $ref: '#/components/schemas/create_google_meeting_task_params'
            - $ref: '#/components/schemas/create_go_to_meeting_task_params'
            - $ref: '#/components/schemas/create_incident_task_params'
            - $ref: '#/components/schemas/create_sub_incident_task_params'
            - $ref: '#/components/schemas/create_incident_postmortem_task_params'
            - $ref: '#/components/schemas/create_jira_issue_task_params'
            - $ref: '#/components/schemas/create_jira_subtask_task_params'
            - $ref: '#/components/schemas/create_linear_issue_task_params'
            - $ref: '#/components/schemas/create_linear_subtask_issue_task_params'
            - $ref: '#/components/schemas/create_linear_issue_comment_task_params'
            - $ref: '#/components/schemas/create_microsoft_teams_meeting_task_params'
            - $ref: '#/components/schemas/create_microsoft_teams_channel_task_params'
            - $ref: '#/components/schemas/create_microsoft_teams_chat_task_params'
            - $ref: '#/components/schemas/add_microsoft_teams_tab_task_params'
            - $ref: '#/components/schemas/add_microsoft_teams_chat_tab_task_params'
            - $ref: >-
                #/components/schemas/archive_microsoft_teams_channels_task_params
            - $ref: '#/components/schemas/rename_microsoft_teams_channel_task_params'
            - $ref: >-
                #/components/schemas/invite_to_microsoft_teams_channel_task_params
            - $ref: '#/components/schemas/create_notion_page_task_params'
            - $ref: '#/components/schemas/send_microsoft_teams_message_task_params'
            - $ref: >-
                #/components/schemas/send_microsoft_teams_chat_message_task_params
            - $ref: '#/components/schemas/send_microsoft_teams_blocks_task_params'
            - $ref: '#/components/schemas/update_notion_page_task_params'
            - $ref: '#/components/schemas/update_quip_page_task_params'
            - $ref: '#/components/schemas/update_confluence_page_task_params'
            - $ref: '#/components/schemas/update_sharepoint_page_task_params'
            - $ref: '#/components/schemas/update_dropbox_paper_page_task_params'
            - $ref: '#/components/schemas/update_datadog_notebook_task_params'
            - $ref: '#/components/schemas/create_service_now_incident_task_params'
            - $ref: '#/components/schemas/create_shortcut_story_task_params'
            - $ref: '#/components/schemas/create_shortcut_task_task_params'
            - $ref: '#/components/schemas/create_trello_card_task_params'
            - $ref: '#/components/schemas/create_webex_meeting_task_params'
            - $ref: '#/components/schemas/create_zendesk_ticket_task_params'
            - $ref: '#/components/schemas/create_zendesk_jira_link_task_params'
            - $ref: '#/components/schemas/create_clickup_task_task_params'
            - $ref: '#/components/schemas/create_motion_task_task_params'
            - $ref: '#/components/schemas/create_zoom_meeting_task_params'
            - $ref: '#/components/schemas/get_github_commits_task_params'
            - $ref: '#/components/schemas/get_gitlab_commits_task_params'
            - $ref: '#/components/schemas/get_pulses_task_params'
            - $ref: '#/components/schemas/get_alerts_task_params'
            - $ref: '#/components/schemas/http_client_task_params'
            - $ref: >-
                #/components/schemas/invite_to_slack_channel_opsgenie_task_params
            - $ref: '#/components/schemas/invite_to_slack_channel_rootly_task_params'
            - $ref: >-
                #/components/schemas/invite_to_slack_channel_pagerduty_task_params
            - $ref: '#/components/schemas/invite_to_slack_channel_task_params'
            - $ref: >-
                #/components/schemas/invite_to_slack_channel_victor_ops_task_params
            - $ref: >-
                #/components/schemas/page_opsgenie_on_call_responders_task_params
            - $ref: '#/components/schemas/create_opsgenie_alert_task_params'
            - $ref: '#/components/schemas/create_jsmops_alert_task_params'
            - $ref: '#/components/schemas/update_opsgenie_alert_task_params'
            - $ref: '#/components/schemas/update_opsgenie_incident_task_params'
            - $ref: '#/components/schemas/page_rootly_on_call_responders_task_params'
            - $ref: >-
                #/components/schemas/page_pagerduty_on_call_responders_task_params
            - $ref: >-
                #/components/schemas/page_victor_ops_on_call_responders_task_params
            - $ref: '#/components/schemas/update_victor_ops_incident_task_params'
            - $ref: '#/components/schemas/print_task_params'
            - $ref: '#/components/schemas/publish_incident_task_params'
            - $ref: '#/components/schemas/redis_client_task_params'
            - $ref: '#/components/schemas/rename_slack_channel_task_params'
            - $ref: '#/components/schemas/change_slack_channel_privacy_task_params'
            - $ref: '#/components/schemas/run_command_heroku_task_params'
            - $ref: '#/components/schemas/send_email_task_params'
            - $ref: '#/components/schemas/send_dashboard_report_task_params'
            - $ref: '#/components/schemas/create_slack_channel_task_params'
            - $ref: '#/components/schemas/send_slack_message_task_params'
            - $ref: '#/components/schemas/send_sms_task_params'
            - $ref: '#/components/schemas/send_whatsapp_message_task_params'
            - $ref: '#/components/schemas/snapshot_datadog_graph_task_params'
            - $ref: '#/components/schemas/snapshot_grafana_dashboard_task_params'
            - $ref: '#/components/schemas/snapshot_looker_look_task_params'
            - $ref: '#/components/schemas/snapshot_new_relic_graph_task_params'
            - $ref: '#/components/schemas/tweet_twitter_message_task_params'
            - $ref: '#/components/schemas/update_airtable_table_record_task_params'
            - $ref: '#/components/schemas/update_asana_task_task_params'
            - $ref: '#/components/schemas/update_github_issue_task_params'
            - $ref: '#/components/schemas/update_gitlab_issue_task_params'
            - $ref: '#/components/schemas/update_incident_task_params'
            - $ref: '#/components/schemas/update_incident_postmortem_task_params'
            - $ref: '#/components/schemas/update_jira_issue_task_params'
            - $ref: '#/components/schemas/update_linear_issue_task_params'
            - $ref: '#/components/schemas/update_service_now_incident_task_params'
            - $ref: '#/components/schemas/update_shortcut_story_task_params'
            - $ref: '#/components/schemas/update_shortcut_task_task_params'
            - $ref: '#/components/schemas/update_slack_channel_topic_task_params'
            - $ref: '#/components/schemas/update_status_task_params'
            - $ref: >-
                #/components/schemas/update_incident_status_timestamp_task_params
            - $ref: '#/components/schemas/update_trello_card_task_params'
            - $ref: '#/components/schemas/update_clickup_task_task_params'
            - $ref: '#/components/schemas/update_motion_task_task_params'
            - $ref: '#/components/schemas/update_zendesk_ticket_task_params'
            - $ref: '#/components/schemas/update_attached_alerts_task_params'
            - $ref: '#/components/schemas/trigger_workflow_task_params'
            - $ref: '#/components/schemas/send_slack_blocks_task_params'
            - $ref: '#/components/schemas/create_openai_chat_completion_task_params'
            - $ref: '#/components/schemas/create_watsonx_chat_completion_task_params'
            - $ref: >-
                #/components/schemas/create_google_gemini_chat_completion_task_params
            - $ref: '#/components/schemas/create_mistral_chat_completion_task_params'
            - $ref: >-
                #/components/schemas/create_anthropic_chat_completion_task_params
        name:
          type: string
          description: Name of the workflow task
        position:
          type: integer
          description: The position of the workflow task
        skip_on_failure:
          type: boolean
          description: Skip workflow task if any failures
        enabled:
          type: boolean
          description: Enable/disable workflow task
          default: true
        created_at:
          type: string
          description: Date of creation
        updated_at:
          type: string
          description: Date of last update
      required:
        - workflow_id
        - task_params
        - position
        - skip_on_failure
        - enabled
        - created_at
        - updated_at
    links:
      type: object
      properties:
        self:
          type: string
        first:
          type: string
        prev:
          type: string
          nullable: true
        next:
          type: string
          nullable: true
        last:
          type: string
      required:
        - self
        - first
        - prev
        - next
        - last
    meta:
      type: object
      properties:
        current_page:
          type: integer
        next_page:
          type: integer
          nullable: true
        prev_page:
          type: integer
          nullable: true
        total_count:
          type: integer
        total_pages:
          type: integer
      required:
        - current_page
        - next_page
        - prev_page
        - total_count
        - total_pages
    add_action_item_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - add_action_item
        attribute_to_query_by:
          type: string
          description: Attribute of the Incident to match against
          enum:
            - jira_issue_id
          nullable: true
        query_value:
          type: string
          description: Value that attribute_to_query_by to uses to match against
          nullable: true
        incident_role_id:
          type: string
          description: The role id this action item is associated with
        assigned_to_user_id:
          type: string
          description: >-
            [DEPRECATED] Use assigned_to_user attribute instead. The user id
            this action item is assigned to
        assigned_to_user:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: ' The user this action item is assigned to'
        priority:
          type: string
          description: The action item priority
          enum:
            - high
            - medium
            - low
        kind:
          type: string
          description: The action item kind
        summary:
          type: string
          description: The action item summary
        description:
          type: string
          description: The action item description
        status:
          type: string
          description: The action item status
          enum:
            - open
            - in_progress
            - cancelled
            - done
        post_to_incident_timeline:
          type: boolean
        custom_fields_mapping:
          type: string
          description: >-
            Custom field mappings. Can contain liquid markup and need to be
            valid JSON
          nullable: true
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - summary
        - status
        - priority
    update_action_item_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_action_item
        query_value:
          type: string
          description: Value that attribute_to_query_by to uses to match against
        attribute_to_query_by:
          type: string
          description: Attribute of the action item to match against
          enum:
            - id
            - jira_issue_id
            - asana_task_id
            - shortcut_task_id
            - linear_issue_id
            - zendesk_ticket_id
            - motion_task_id
            - trello_card_id
            - airtable_record_id
            - shortcut_story_id
            - github_issue_id
            - gitlab_issue_id
            - freshservice_ticket_id
            - freshservice_task_id
            - clickup_task_id
          default: id
        summary:
          type: string
          description: Brief description of the action item
        assigned_to_user_id:
          type: string
          description: >-
            [DEPRECATED] Use assigned_to_user attribute instead. The user id
            this action item is assigned to
        assigned_to_user:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: ' The user this action item is assigned to'
        group_ids:
          type: array
          items:
            type: string
          nullable: true
        description:
          type: string
          description: The action item description
        priority:
          type: string
          description: The action item priority
          enum:
            - high
            - medium
            - low
        status:
          type: string
          description: The action item status
          enum:
            - open
            - in_progress
            - cancelled
            - done
        custom_fields_mapping:
          type: string
          description: >-
            Custom field mappings. Can contain liquid markup and need to be
            valid JSON
          nullable: true
        post_to_incident_timeline:
          type: boolean
      required:
        - query_value
        - attribute_to_query_by
    add_role_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - add_role
        incident_role_id:
          type: string
          description: The role id to add to the incident
        assigned_to_user_id:
          type: string
          description: >-
            [DEPRECATED] Use assigned_to_user attribute instead. The user id
            this role is assigned to
        assigned_to_user:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: ' The user this role is assigned to'
      required:
        - incident_role_id
    add_slack_bookmark_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - add_slack_bookmark
        playbook_id:
          type: string
          description: The playbook id if bookmark is of an incident playbook
        channel:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        title:
          type: string
          description: The bookmark title. Required if not a playbook bookmark
          nullable: true
        link:
          type: string
          description: The bookmark link. Required if not a playbook bookmark
          nullable: true
        emoji:
          type: string
          description: The bookmark emoji
      required:
        - channel
      anyOf:
        - required:
            - title
            - link
        - required:
            - playbook_id
    add_team_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - add_team
        group_id:
          type: string
          description: The team id
      required:
        - group_id
    add_to_timeline_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - add_to_timeline
        event:
          type: string
          description: The timeline event description
        url:
          type: string
          description: A URL for the timeline event
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - event
    archive_slack_channels_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - archive_slack_channels
        channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - channels
    attach_datadog_dashboards_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - attach_datadog_dashboards
        dashboards:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        post_to_incident_timeline:
          type: boolean
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - dashboards
    auto_assign_role_opsgenie_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - auto_assign_role_opsgenie
        incident_role_id:
          type: string
          description: The role id
        schedule:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
      required:
        - incident_role_id
        - schedule
    auto_assign_role_rootly_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - auto_assign_role_rootly
        incident_role_id:
          type: string
          description: The role id
        escalation_policy_target:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        service_target:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        user_target:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        group_target:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        schedule_target:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
      required:
        - incident_role_id
    auto_assign_role_pagerduty_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - auto_assign_role_pagerduty
        incident_role_id:
          type: string
          description: The role id
        service:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        schedule:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        escalation_policy:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
      required:
        - incident_role_id
      anyOf:
        - required:
            - schedule
        - required:
            - escalation_policy
    update_pagerduty_incident_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_pagerduty_incident
        pagerduty_incident_id:
          type: string
          description: Pagerduty incident id
        title:
          type: string
          description: Title to update to
        status:
          type: string
          enum:
            - resolved
            - acknowledged
            - auto
        resolution:
          type: string
          description: A message outlining the incident's resolution in PagerDuty
        escalation_level:
          type: integer
          description: Escalation level of policy attached to incident
          minimum: 1
          maximum: 20
          example: 1
        urgency:
          type: string
          description: >-
            PagerDuty incident urgency, selecting auto will let Rootly auto map
            our incident severity
          enum:
            - high
            - low
            - auto
        priority:
          type: string
          description: >-
            PagerDuty incident priority, selecting auto will let Rootly auto map
            our incident severity
      required:
        - pagerduty_incident_id
    create_pagerduty_status_update_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_pagerduty_status_update
        pagerduty_incident_id:
          type: string
          description: PagerDuty incident id
        message:
          type: string
          description: A message outlining the incident's resolution in PagerDuty
      required:
        - pagerduty_incident_id
        - message
    create_pagertree_alert_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_pagertree_alert
        title:
          type: string
          description: Title of alert as text
        description:
          type: string
          description: Description of alert as text
        urgency:
          type: string
          enum:
            - auto
            - critical
            - high
            - medium
            - low
        severity:
          type: string
          enum:
            - auto
            - SEV-1
            - SEV-2
            - SEV-3
            - SEV-4
        teams:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        users:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        incident:
          type: boolean
          description: Setting to true makes an alert a Pagertree incident
    update_pagertree_alert_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_pagertree_alert
        pagertree_alert_id:
          type: string
          description: The prefix ID of the Pagertree alert
        title:
          type: string
          description: Title of alert as text
        description:
          type: string
          description: Description of alert as text
        urgency:
          type: string
          enum:
            - auto
            - critical
            - high
            - medium
            - low
        severity:
          type: string
          enum:
            - auto
            - SEV-1
            - SEV-2
            - SEV-3
            - SEV-4
        teams:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        users:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        incident:
          type: boolean
          description: Setting to true makes an alert a Pagertree incident
    auto_assign_role_victor_ops_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - auto_assign_role_victor_ops
        incident_role_id:
          type: string
          description: The role id
        team:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
      required:
        - incident_role_id
        - team
    call_people_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - call_people
        phone_numbers:
          type: array
          items:
            type: string
            description: A recipient phone number
            example:
              - '14150001111'
        name:
          type: string
          description: The name
        content:
          type: string
          description: The message to be read by text-to-voice
      required:
        - phone_numbers
        - name
        - content
    create_airtable_table_record_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_airtable_table_record
        base:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        table:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        custom_fields_mapping:
          type: string
          description: >-
            Custom field mappings. Can contain liquid markup and need to be
            valid JSON
          nullable: true
      required:
        - base
        - table
    create_asana_subtask_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_asana_subtask
        parent_task_id:
          type: string
          description: The parent task id
        title:
          type: string
          description: The subtask title
        notes:
          type: string
        assign_user_email:
          type: string
          description: The assigned user's email
        completion:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        due_date:
          type: string
          description: The due date
        custom_fields_mapping:
          type: string
          description: >-
            Custom field mappings. Can contain liquid markup and need to be
            valid JSON
          nullable: true
        dependency_direction:
          type: string
          enum:
            - blocking
            - blocked_by
          default: blocking
        dependent_task_ids:
          type: array
          description: Dependent task ids. Supports liquid syntax
          items:
            type: string
          nullable: true
      required:
        - parent_task_id
        - title
        - completion
    create_asana_task_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_asana_task
        workspace:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        projects:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        title:
          type: string
          description: The task title
        notes:
          type: string
        assign_user_email:
          type: string
          description: The assigned user's email
        completion:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        due_date:
          type: string
          description: The due date
        custom_fields_mapping:
          type: string
          description: >-
            Custom field mappings. Can contain liquid markup and need to be
            valid JSON
          nullable: true
        dependency_direction:
          type: string
          enum:
            - blocking
            - blocked_by
          default: blocking
        dependent_task_ids:
          type: array
          description: Dependent task ids. Supports liquid syntax
          items:
            type: string
          nullable: true
      required:
        - workspace
        - projects
        - title
        - completion
    create_confluence_page_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_confluence_page
        integration:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: Specify integration id if you have more than one Confluence instance
        space:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        ancestor:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        template:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        title:
          type: string
          description: The page title
        content:
          type: string
          description: The page content
        post_mortem_template_id:
          type: string
          description: The Retrospective template to use
        mark_post_mortem_as_published:
          type: boolean
          default: true
      required:
        - space
        - title
    create_datadog_notebook_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_datadog_notebook
        post_mortem_template_id:
          type: string
          description: Retrospective template to use when creating notebook, if desired
        mark_post_mortem_as_published:
          type: boolean
          default: true
        template:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        title:
          type: string
          description: The notebook title
        kind:
          type: string
          description: The notebook kind
          enum:
            - postmortem
            - runbook
            - investigation
            - documentation
            - report
        content:
          type: string
          description: The notebook content
      required:
        - title
        - kind
    create_coda_page_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_coda_page
        post_mortem_template_id:
          type: string
          description: Retrospective template to use when creating page, if desired
        mark_post_mortem_as_published:
          type: boolean
          default: true
        title:
          type: string
          description: The Coda page title
        subtitle:
          type: string
          description: The Coda page subtitle
        content:
          type: string
          description: The Coda page content
        template:
          type: object
          properties:
            id:
              type: string
              description: Combined doc_id/page_id in format 'doc_id/page_id'
            name:
              type: string
        folder_id:
          type: string
          description: The Coda folder id
        doc:
          type: object
          description: The Coda doc object with id and name
          properties:
            id:
              type: string
            name:
              type: string
      required:
        - title
    create_dropbox_paper_page_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_dropbox_paper_page
        post_mortem_template_id:
          type: string
          description: Retrospective template to use when creating page task, if desired
        mark_post_mortem_as_published:
          type: boolean
          default: true
        title:
          type: string
          description: The page task title
        content:
          type: string
          description: The page content
        namespace:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        parent_folder:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
      required:
        - title
    create_github_issue_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_github_issue
        title:
          type: string
          description: The issue title
        body:
          type: string
          description: The issue body
        repository:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
      required:
        - repository
        - title
    create_gitlab_issue_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_gitlab_issue
        issue_type:
          type: string
          description: The issue type
          enum:
            - issue
            - incident
            - test_case
            - task
        title:
          type: string
          description: The issue title
        description:
          type: string
          description: The issue description
        repository:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        labels:
          type: string
          description: The issue labels
        due_date:
          type: string
          description: The due date
      required:
        - repository
        - title
    create_outlook_event_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_outlook_event
        calendar:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        attendees:
          type: array
          description: Emails of attendees
          items:
            type: string
        time_zone:
          type: string
          description: A valid IANA time zone name.
          nullable: true
        days_until_meeting:
          type: integer
          description: The days until meeting
          minimum: 0
          maximum: 31
        time_of_meeting:
          type: string
          description: Time of meeting in format HH:MM
          example: '14:30'
        meeting_duration:
          type: string
          description: Meeting duration in format like '1 hour', '30 minutes'
          example: 1 hour
        summary:
          type: string
          description: The event summary
        description:
          type: string
          description: The event description
        exclude_weekends:
          type: boolean
        enable_online_meeting:
          type: boolean
          description: Enable Microsoft Teams online meeting
        post_to_incident_timeline:
          type: boolean
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - calendar
        - days_until_meeting
        - time_of_meeting
        - meeting_duration
        - summary
        - description
    create_google_calendar_event_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_google_calendar_event
        attendees:
          type: array
          description: Emails of attendees
          items:
            type: string
        time_zone:
          type: string
          description: A valid IANA time zone name.
          nullable: true
        calendar_id:
          type: string
          nullable: true
          default: primary
        days_until_meeting:
          type: integer
          description: The days until meeting
          minimum: 0
          maximum: 31
        time_of_meeting:
          type: string
          description: Time of meeting in format HH:MM
          example: '14:30'
        meeting_duration:
          type: string
          description: Meeting duration in format like '1 hour', '30 minutes'
          example: 1 hour
        send_updates:
          type: boolean
          description: Send an email to the attendees notifying them of the event
        can_guests_modify_event:
          type: boolean
        can_guests_see_other_guests:
          type: boolean
        can_guests_invite_others:
          type: boolean
        summary:
          type: string
          description: The event summary
        description:
          type: string
          description: The event description
        exclude_weekends:
          type: boolean
        conference_solution_key:
          type: string
          enum:
            - eventHangout
            - eventNamedHangout
            - hangoutsMeet
            - addOn
          description: Sets the video conference type attached to the meeting
          nullable: true
        post_to_incident_timeline:
          type: boolean
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - days_until_meeting
        - time_of_meeting
        - meeting_duration
        - summary
        - description
    update_google_docs_page_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_google_docs_page
        file_id:
          type: string
          description: The Google Doc file ID
        title:
          type: string
          description: The Google Doc title
        content:
          type: string
          description: The Google Doc content
        post_mortem_template_id:
          type: string
          description: Retrospective template to use when updating page, if desired
        template_id:
          type: string
          description: The Google Doc file ID to use as a template.
      required:
        - file_id
    update_coda_page_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_coda_page
        doc_id:
          type: string
          description: The Coda doc id
        page_id:
          type: string
          description: The Coda page id
        title:
          type: string
          description: The Coda page title
        subtitle:
          type: string
          description: The Coda page subtitle
        content:
          type: string
          description: The Coda page content
        template:
          type: object
          properties:
            id:
              type: string
              description: Combined doc_id/page_id in format 'doc_id/page_id'
            name:
              type: string
      required:
        - page_id
    update_google_calendar_event_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_google_calendar_event
        calendar_id:
          type: string
          nullable: true
          default: primary
        event_id:
          type: string
          description: The event ID
        summary:
          type: string
          description: The event summary
        description:
          type: string
          description: The event description
        adjustment_days:
          type: integer
          description: Days to adjust meeting by
          minimum: 0
          maximum: 31
        time_of_meeting:
          type: string
          description: Time of meeting in format HH:MM
        meeting_duration:
          type: string
          description: Meeting duration in format like '1 hour', '30 minutes'
          example: 1 hour
        send_updates:
          type: boolean
          description: Send an email to the attendees notifying them of the event
        can_guests_modify_event:
          type: boolean
        can_guests_see_other_guests:
          type: boolean
        can_guests_invite_others:
          type: boolean
        attendees:
          type: array
          description: Emails of attendees
          items:
            type: string
        replace_attendees:
          type: boolean
        conference_solution_key:
          type: string
          enum:
            - eventHangout
            - eventNamedHangout
            - hangoutsMeet
            - addOn
          description: Sets the video conference type attached to the meeting
          nullable: true
        post_to_incident_timeline:
          type: boolean
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - event_id
    create_sharepoint_page_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_sharepoint_page
        post_mortem_template_id:
          type: string
          description: Retrospective template to use when creating page, if desired
        mark_post_mortem_as_published:
          type: boolean
          default: true
        title:
          type: string
          description: The page title
        site:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        drive:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        parent_folder:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        content:
          type: string
          description: The page content
        template_id:
          type: string
          description: The SharePoint file ID to use as a template
      required:
        - title
        - site
        - drive
    create_google_docs_page_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_google_docs_page
        post_mortem_template_id:
          type: string
          description: Retrospective template to use when creating page, if desired
        mark_post_mortem_as_published:
          type: boolean
          default: true
        title:
          type: string
          description: The page title
        drive:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        parent_folder:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        content:
          type: string
          description: The page content
        template_id:
          type: string
          description: The Google Doc file ID to use as a template
        permissions:
          type: string
          description: Page permissions JSON
      required:
        - title
    create_google_docs_permissions_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_google_docs_permissions
        file_id:
          type: string
          description: The Google Doc file ID
        permissions:
          type: string
          description: Page permissions JSON
        send_notification_email:
          type: boolean
        email_message:
          type: string
          description: Email message notification
          nullable: true
      required:
        - file_id
        - permissions
    remove_google_docs_permissions_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - remove_google_docs_permissions
        file_id:
          type: string
          description: The Google Doc file ID
        attribute_to_query_by:
          type: string
          enum:
            - type
            - role
            - email_address
          default: email_address
        value:
          type: string
      required:
        - file_id
        - attribute_to_query_by
        - value
    create_quip_page_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_google_docs_page
        post_mortem_template_id:
          type: string
          description: Retrospective template to use when creating page, if desired
        title:
          type: string
          description: The page title
        parent_folder_id:
          type: string
          description: The parent folder id
        content:
          type: string
          description: The page content
        template_id:
          type: string
          description: The Quip file ID to use as a template
        mark_post_mortem_as_published:
          type: boolean
          default: true
      required:
        - title
    create_google_meeting_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_google_meeting
        summary:
          type: string
          description: '[DEPRECATED] The meeting summary'
          nullable: true
        description:
          type: string
          description: '[DEPRECATED] The meeting description'
          nullable: true
        conference_solution_key:
          type: string
          enum:
            - eventHangout
            - eventNamedHangout
            - hangoutsMeet
            - addOn
          description: '[DEPRECATED] Sets the video conference type attached to the meeting'
          nullable: true
        record_meeting:
          type: boolean
          description: >-
            Rootly AI will record the meeting and automatically generate a
            transcript and summary from your meeting
        recording_mode:
          type: string
          enum:
            - speaker_view
            - gallery_view
            - gallery_view_v2
            - audio_only
          description: >-
            The video layout for the bot's recording (e.g. speaker_view,
            gallery_view, gallery_view_v2, audio_only)
          nullable: true
        post_to_incident_timeline:
          type: boolean
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - summary
        - description
    create_go_to_meeting_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_go_to_meeting_task
        subject:
          type: string
          description: The meeting subject
        conference_call_info:
          type: string
          enum:
            - ptsn
            - free
            - hyrid
            - voip
          default: voip
          example: voip
          nullable: true
        password_required:
          type: boolean
          nullable: true
        post_to_incident_timeline:
          type: boolean
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - subject
    create_incident_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_incident
        title:
          type: string
          description: The incident title
        summary:
          type: string
          description: The incident summary
        severity_id:
          type: string
        incident_type_ids:
          type: array
          items:
            type: string
        service_ids:
          type: array
          items:
            type: string
          description: Array of service UUIDs
        functionality_ids:
          type: array
          items:
            type: string
          description: Array of functionality UUIDs
        environment_ids:
          type: array
          items:
            type: string
        group_ids:
          type: array
          items:
            type: string
          description: Array of group/team UUIDs
        private:
          type: boolean
        custom_fields_mapping:
          type: string
          description: >-
            Custom field mappings. Can contain liquid markup and need to be
            valid JSON. Use 'services', 'functionalities', or 'groups' keys with
            arrays of names/slugs for name/slug lookup
          nullable: true
      required:
        - title
    create_sub_incident_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_sub_incident
        title:
          type: string
          description: The sub incident title
        summary:
          type: string
          description: The sub incident summary
      required:
        - title
    create_incident_postmortem_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_incident_postmortem
        incident_id:
          type: string
          description: UUID of the incident that needs a retrospective
        title:
          type: string
          description: The retrospective title
        status:
          type: string
          nullable: true
        template:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: Retrospective template to use
          nullable: true
      required:
        - incident_id
        - title
    create_jira_issue_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_jira_issue
        integration:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: Specify integration id if you have more than one Jira instance
        title:
          type: string
          description: The issue title
        description:
          type: string
          description: The issue description
        labels:
          type: string
          description: The issue labels
        assign_user_email:
          type: string
          description: The assigned user's email
        reporter_user_email:
          type: string
          description: The reporter user's email
        project_key:
          type: string
          description: The project key
        due_date:
          type: string
          description: The due date
        issue_type:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The issue type id and display name
        priority:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The priority id and display name
        status:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The status id and display name
        custom_fields_mapping:
          type: string
          description: >-
            Custom field mappings. Can contain liquid markup and need to be
            valid JSON
          nullable: true
        update_payload:
          type: string
          description: Update payload. Can contain liquid markup and need to be valid JSON
          nullable: true
      required:
        - project_key
        - title
        - issue_type
    create_jira_subtask_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_jira_subtask
        integration:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: Specify integration id if you have more than one Jira instance
        project_key:
          type: string
          description: The project key
        parent_issue_id:
          type: string
          description: The parent issue
        title:
          type: string
          description: The issue title
        description:
          type: string
          description: The issue description
        subtask_issue_type:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The issue type id and display name
        labels:
          type: string
          description: The issue labels
        due_date:
          type: string
          description: The due date
        assign_user_email:
          type: string
          description: The assigned user's email
        reporter_user_email:
          type: string
          description: The reporter user's email
        priority:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The priority id and display name
        status:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The status id and display name
        custom_fields_mapping:
          type: string
          description: >-
            Custom field mappings. Can contain liquid markup and need to be
            valid JSON
          nullable: true
        update_payload:
          type: string
          description: Update payload. Can contain liquid markup and need to be valid JSON
          nullable: true
      required:
        - project_key
        - parent_issue_id
        - title
        - subtask_issue_type
    create_linear_issue_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_linear_issue
        title:
          type: string
          description: The issue title
        description:
          type: string
          description: The issue description
        team:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The team id and display name
        state:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The state id and display name
        project:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The project id and display name
        labels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        priority:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The priority id and display name
        assign_user_email:
          type: string
          description: The assigned user's email
      required:
        - title
        - team
        - state
    create_linear_subtask_issue_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_linear_subtask_issue
        parent_issue_id:
          type: string
          description: The parent issue
        title:
          type: string
          description: The issue title
        description:
          type: string
          description: The issue description
        state:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The state id and display name
        priority:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The priority id and display name
        labels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        assign_user_email:
          type: string
          description: The assigned user's email
      required:
        - parent_issue_id
        - title
        - state
    create_linear_issue_comment_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_linear_issue_comment
        issue_id:
          type: string
          description: The issue id
        body:
          type: string
          description: The issue description
      required:
        - issue_id
        - body
    create_microsoft_teams_meeting_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_microsoft_teams_meeting
        name:
          type: string
          description: The meeting name
        subject:
          type: string
          description: The meeting subject
        record_meeting:
          type: boolean
          description: >-
            Rootly AI will record the meeting and automatically generate a
            transcript and summary from your meeting
        recording_mode:
          type: string
          enum:
            - speaker_view
            - gallery_view
            - gallery_view_v2
            - audio_only
          description: >-
            The video layout for the bot's recording (e.g. speaker_view,
            gallery_view, gallery_view_v2, audio_only)
          nullable: true
        post_to_incident_timeline:
          type: boolean
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - name
        - subject
    create_microsoft_teams_channel_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_microsoft_teams_channel
        team:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        title:
          type: string
          description: Microsoft Team channel title
        description:
          type: string
          description: Microsoft Team channel description
        private:
          type: string
          enum:
            - auto
            - 'true'
            - 'false'
          default: auto
      required:
        - workspace
        - title
    create_microsoft_teams_chat_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_microsoft_teams_chat
        topic:
          type: string
          description: Chat topic (only for group chats)
          nullable: true
        chat_type:
          type: string
          enum:
            - group
            - oneOnOne
          default: group
          description: Type of chat to create
        members:
          type: array
          items:
            type: object
            properties:
              email:
                type: string
              name:
                type: string
          description: Array of members to include in the chat
      required:
        - members
    add_microsoft_teams_tab_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - add_microsoft_teams_tab
        playbook_id:
          type: string
          description: The playbook id if tab is of an incident playbook
        team:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        channel:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        title:
          type: string
          description: The tab title. Required if not a playbook tab
          nullable: true
        link:
          type: string
          description: The tab link. Required if not a playbook tab
          nullable: true
      required:
        - team
        - channel
      anyOf:
        - required:
            - title
            - link
        - required:
            - playbook_id
    add_microsoft_teams_chat_tab_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - add_microsoft_teams_chat_tab
        chat:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        title:
          type: string
          description: The tab title
        link:
          type: string
          description: The tab link
      required:
        - chat
        - title
        - link
    archive_microsoft_teams_channels_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - archive_microsoft_teams_channels
        team:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - team
        - channels
    rename_microsoft_teams_channel_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - rename_microsoft_teams_channel
        team:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        channel:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        title:
          type: string
      required:
        - title
        - team
        - channel
    invite_to_microsoft_teams_channel_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - invite_to_microsoft_teams_channel
        team:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        channel:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        emails:
          type: string
          description: Comma separated list of emails to invite
      required:
        - channel
        - emails
    create_notion_page_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_notion_page
        title:
          type: string
          description: The Notion page title
        parent_page:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The parent page id and display name
        post_mortem_template_id:
          type: string
          description: Retrospective template to use when creating page task, if desired
        content:
          type: string
          description: >-
            Custom page content with liquid templating support. When provided,
            only this content will be rendered (no default sections)
        mark_post_mortem_as_published:
          type: boolean
          default: true
        show_timeline_as_table:
          type: boolean
        show_action_items_as_table:
          type: boolean
      required:
        - parent_page
        - title
    send_microsoft_teams_message_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - send_microsoft_teams_message
        channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        text:
          type: string
          description: The message text
      required:
        - text
      anyOf:
        - required:
            - channels
    send_microsoft_teams_chat_message_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - send_microsoft_teams_chat_message
        chats:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        text:
          type: string
          description: The message text
      required:
        - text
        - chats
    send_microsoft_teams_blocks_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - send_microsoft_teams_blocks
        attachments:
          type: string
          description: >-
            Support liquid markup. Needs to be a valid JSON string after liquid
            is parsed
      required:
        - attachments
      anyOf:
        - required:
            - channels
    update_notion_page_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_notion_page
        file_id:
          type: string
          description: The Notion page ID
        title:
          type: string
          description: The Notion page title
        post_mortem_template_id:
          type: string
          description: Retrospective template to use when creating page task, if desired
        content:
          type: string
          description: >-
            Custom page content with liquid templating support. When provided,
            only this content will be rendered (no default sections)
        show_timeline_as_table:
          type: boolean
        show_action_items_as_table:
          type: boolean
      required:
        - file_id
    update_quip_page_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_quip_page
        file_id:
          type: string
          description: The Quip page ID
        title:
          type: string
          description: The Quip page title
        content:
          type: string
          description: The Quip page content
        post_mortem_template_id:
          type: string
          description: Retrospective template to use when updating page, if desired
        template_id:
          type: string
          description: The Quip file ID to use as a template
      required:
        - file_id
    update_confluence_page_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_confluence_page
        file_id:
          type: string
          description: The Confluence page ID
        title:
          type: string
          description: The Confluence page title
        content:
          type: string
          description: The Confluence page content
        post_mortem_template_id:
          type: string
          description: Retrospective template to use when updating page, if desired
        template:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The Confluence template to use
      required:
        - file_id
    update_sharepoint_page_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_sharepoint_page
        file_id:
          type: string
          description: The SharePoint file ID
        title:
          type: string
          description: The SharePoint document title
        content:
          type: string
          description: The SharePoint document content
        post_mortem_template_id:
          type: string
          description: Retrospective template to use when updating document, if desired
      required:
        - file_id
    update_dropbox_paper_page_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_dropbox_paper_page
        file_id:
          type: string
          description: The Dropbox Paper document ID
        title:
          type: string
          description: The Dropbox Paper document title
        content:
          type: string
          description: The Dropbox Paper document content
        post_mortem_template_id:
          type: string
          description: Retrospective template to use when updating document, if desired
      required:
        - file_id
    update_datadog_notebook_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_datadog_notebook
        file_id:
          type: string
          description: The Datadog notebook ID
        title:
          type: string
          description: The Datadog notebook title
        content:
          type: string
          description: The Datadog notebook content
        kind:
          type: string
          description: The notebook type
          enum:
            - postmortem
            - runbook
            - investigation
            - documentation
            - report
        post_mortem_template_id:
          type: string
          description: Retrospective template to use when updating notebook, if desired
        template:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The Datadog notebook template to use
      required:
        - file_id
    create_service_now_incident_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_service_now_incident
        title:
          type: string
          description: The incident title
        description:
          type: string
          description: The incident description
        priority:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The priority id and display name
        completion:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The completion id and display name
        custom_fields_mapping:
          type: string
          description: >-
            Custom field mappings. Can contain liquid markup and need to be
            valid JSON
          nullable: true
      required:
        - title
    create_shortcut_story_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_shortcut_story
        title:
          type: string
          description: The incident title
        kind:
          type: string
          enum:
            - bug
            - chore
            - feature
        description:
          type: string
          description: The incident description
        labels:
          type: string
          description: The story labels
        due_date:
          type: string
          description: The due date
        archivation:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The archivation id and display name
        group:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The group id and display name
        project:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The project id and display name
        workflow_state:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The workflow state id workflow state name
      required:
        - title
        - archivation
        - kind
      anyOf:
        - required:
            - project
        - required:
            - workflow_state
    create_shortcut_task_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_shortcut_task
        parent_story_id:
          type: string
          description: The parent story
        description:
          type: string
          description: The task description
        completion:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The completion id and display name
      required:
        - parent_story_id
        - description
        - completion
    create_trello_card_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_trello_card
        title:
          type: string
          description: The card title
        description:
          type: string
          description: The card description
        due_date:
          type: string
          description: The due date
        board:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The board id and display name
        list:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The list id and display name
        labels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        archivation:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The archivation id and display name
      required:
        - title
        - board
        - list
    create_webex_meeting_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_webex_meeting
        topic:
          type: string
          description: The meeting topic
        password:
          type: string
          description: The meeting password
        record_meeting:
          type: boolean
          description: >-
            Rootly AI will record the meeting and automatically generate a
            transcript and summary from your meeting
        recording_mode:
          type: string
          enum:
            - speaker_view
            - gallery_view
            - gallery_view_v2
            - audio_only
          description: >-
            The video layout for the bot's recording (e.g. speaker_view,
            gallery_view, gallery_view_v2, audio_only)
          nullable: true
        post_to_incident_timeline:
          type: boolean
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - topic
    create_zendesk_ticket_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_zendesk_ticket
        kind:
          type: string
          enum:
            - problem
            - incident
            - question
            - task
        subject:
          type: string
          description: The ticket subject
        comment:
          type: string
          description: The ticket comment
        tags:
          type: string
          description: The ticket tags
        priority:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The priority id and display name
        completion:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The completion id and display name
        custom_fields_mapping:
          type: string
          description: >-
            Custom field mappings. Can contain liquid markup and need to be
            valid JSON
          nullable: true
        ticket_payload:
          type: string
          description: >-
            Additional Zendesk ticket attributes. Will be merged into whatever
            was specified in this tasks current parameters. Can contain liquid
            markup and need to be valid JSON
          nullable: true
      required:
        - kind
        - subject
    create_zendesk_jira_link_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_zendesk_jira_link
        jira_issue_id:
          type: string
          description: Jira Issue Id.
        jira_issue_key:
          type: string
          description: Jira Issue Key.
        zendesk_ticket_id:
          type: string
          description: Zendesk Ticket Id.
      required:
        - jira_issue_id
        - jira_issue_key
        - zendesk_ticket_id
    create_clickup_task_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_clickup_task
        title:
          type: string
          description: The task title
        description:
          type: string
          description: The task description
        tags:
          type: string
          description: The task tags
        priority:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The priority id and display name
        due_date:
          type: string
          description: The due date
        custom_fields_mapping:
          type: string
          description: >-
            Custom field mappings. Can contain liquid markup and need to be
            valid JSON
          nullable: true
        task_payload:
          type: string
          description: >-
            Additional ClickUp task attributes. Will be merged into whatever was
            specified in this tasks current parameters. Can contain liquid
            markup and need to be valid JSON
          nullable: true
      required:
        - title
    create_motion_task_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_motion_task
        workspace:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        project:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        status:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        title:
          type: string
          description: The task title
        description:
          type: string
          description: The task description
        labels:
          type: array
          items:
            type: string
        priority:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The priority id and display name
        duration:
          type: string
          description: The duration. Eg.  "NONE", "REMINDER", or a integer greater than 0.
        due_date:
          type: string
          description: The due date
      required:
        - workspace
        - title
    create_zoom_meeting_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_zoom_meeting
        topic:
          type: string
          description: The meeting topic
        password:
          type: string
          description: The meeting password
        create_as_email:
          type: string
          description: The email to use if creating as email
        alternative_hosts:
          type: array
          items:
            type: string
            description: Alternative host email
        auto_recording:
          type: string
          enum:
            - none
            - local
            - cloud
          default: none
        record_meeting:
          type: boolean
          description: >-
            Rootly AI will record the meeting and automatically generate a
            transcript and summary from your meeting
        recording_mode:
          type: string
          enum:
            - speaker_view
            - gallery_view
            - gallery_view_v2
            - audio_only
          description: >-
            The video layout for the bot's recording (e.g. speaker_view,
            gallery_view, gallery_view_v2, audio_only)
          nullable: true
        post_to_incident_timeline:
          type: boolean
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - topic
    get_github_commits_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - get_github_commits
        service_ids:
          type: array
          items:
            type: string
            description: ID of service impacted by incident
        github_repository_names:
          type: array
          items:
            type: string
        branch:
          type: string
          description: The branch
        past_duration:
          type: string
          description: >-
            How far back to fetch commits (in format '1 minute', '30 days', '3
            months', etc.)
          example: 1 hour
        services_impacted_by_incident:
          type: boolean
        post_to_incident_timeline:
          type: boolean
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - branch
        - past_duration
      anyOf:
        - required:
            - service_ids
        - required:
            - github_repository_names
    get_gitlab_commits_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - get_gitlab_commits
        service_ids:
          type: array
          items:
            type: string
            description: ID of service impacted by incident
        gitlab_repository_names:
          type: array
          items:
            type: string
        branch:
          type: string
          description: The branch
        past_duration:
          type: string
          description: >-
            How far back to fetch commits (in format '1 minute', '30 days', '3
            months', etc.)
          example: 1 hour
        services_impacted_by_incident:
          type: boolean
        post_to_incident_timeline:
          type: boolean
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - branch
        - past_duration
      anyOf:
        - required:
            - service_ids
        - required:
            - gitlab_repository_names
    get_pulses_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - get_pulses
        service_ids:
          type: array
          items:
            type: string
            description: ID of service impacted by incident
        environment_ids:
          type: array
          items:
            type: string
            description: ID of environment impacted by incident
        labels:
          type: array
          items:
            type: string
        refs:
          type: array
          items:
            type: string
        sources:
          type: array
          items:
            type: string
        past_duration:
          type: string
          description: >-
            How far back to fetch commits (in format '1 minute', '30 days', '3
            months', etc.)
          example: 1 hour
        services_impacted_by_incident:
          type: boolean
        environments_impacted_by_incident:
          type: boolean
        post_to_incident_timeline:
          type: boolean
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        parent_message_thread_task:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: >-
            A hash where [id] is the task id of the parent task that sent a
            message, and [name] is the name of the parent task
      required:
        - past_duration
    get_alerts_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - get_alerts
        service_ids:
          type: array
          items:
            type: string
            description: ID of service impacted by incident
        environment_ids:
          type: array
          items:
            type: string
            description: ID of environment impacted by incident
        labels:
          type: array
          items:
            type: string
        sources:
          type: array
          items:
            type: string
        past_duration:
          type: string
          description: >-
            How far back to fetch commits (in format '1 minute', '30 days', '3
            months', etc.)
          example: 1 hour
        services_impacted_by_incident:
          type: boolean
        environments_impacted_by_incident:
          type: boolean
        post_to_incident_timeline:
          type: boolean
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        parent_message_thread_task:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: >-
            A hash where [id] is the task id of the parent task that sent a
            message, and [name] is the name of the parent task
      required:
        - past_duration
    http_client_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - http_client
        headers:
          type: string
          description: JSON map of HTTP headers
        params:
          type: string
          description: JSON map of HTTP query parameters
        body:
          type: string
          description: HTTP body
        url:
          type: string
          description: URL endpoint
          example: https://example.com/foo.json
        event_url:
          type: string
        event_message:
          type: string
        method:
          type: string
          description: HTTP method
          enum:
            - GET
            - POST
            - PATCH
            - PUT
            - DELETE
            - OPTIONS
          default: GET
        succeed_on_status:
          type: string
          description: >-
            HTTP status code expected. Can be a regular expression. Eg: 200,
            200|203, 20[0-3]
          example: 200
        post_to_incident_timeline:
          type: boolean
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - url
        - succeed_on_status
    invite_to_slack_channel_opsgenie_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - invite_to_slack_channel_opsgenie
        channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        schedule:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
      required:
        - schedule
        - channels
    invite_to_slack_channel_rootly_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - invite_to_slack_channel_rootly
        channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        escalation_policy_target:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        service_target:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        user_target:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        group_target:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        schedule_target:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
      required:
        - channels
    invite_to_slack_channel_pagerduty_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - invite_to_slack_channel_pagerduty
        channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        escalation_policy:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        schedule:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        service:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
      required:
        - channels
      anyOf:
        - required:
            - escalation_policy
        - required:
            - schedule
    invite_to_slack_channel_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - invite_to_slack_channel
        channel:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        slack_users:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        slack_user_groups:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        slack_emails:
          type: string
          description: Comma separated list of emails to invite to the channel
      required:
        - channel
      anyOf:
        - required:
            - slack_users
        - required:
            - slack_user_groups
        - required:
            - slack_emails
    invite_to_slack_channel_victor_ops_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - invite_to_slack_channel_victor_ops
        channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        team:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
      required:
        - team
        - channels
    page_opsgenie_on_call_responders_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - page_opsgenie_on_call_responders
        title:
          type: string
          description: Incident title.
          nullable: true
        message:
          type: string
          description: Message of the incident
        description:
          type: string
          description: >-
            Description field of the incident that is generally used to provide
            a detailed information about the incident
        teams:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        users:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        priority:
          type: string
          enum:
            - P1
            - P2
            - P3
            - P4
            - P5
            - auto
          default: P1
    create_opsgenie_alert_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_opsgenie_alert
        message:
          type: string
          description: Message of the alert
        description:
          type: string
          description: >-
            Description field of the alert that is generally used to provide a
            detailed information about the alert
        teams:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        users:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        schedules:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        escalations:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        priority:
          type: string
          enum:
            - P1
            - P2
            - P3
            - P4
            - P5
            - auto
          default: P1
        details:
          type: string
          description: Details payload. Can contain liquid markup and need to be valid JSON
          nullable: true
      required:
        - message
    create_jsmops_alert_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_jsmops_alert
        message:
          type: string
          description: Message of the alert
        description:
          type: string
          description: >-
            Description field of the alert that is generally used to provide a
            detailed information about the alert
          nullable: true
        teams:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        users:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        schedules:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        escalations:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        priority:
          type: string
          enum:
            - P3
            - P1
            - P2
            - P3
            - P4
            - P5
            - auto
          default: P3
        details:
          type: string
          description: Details payload. Can contain liquid markup and need to be valid JSON
          nullable: true
      required:
        - message
    update_opsgenie_alert_task_params:
      type: object
      properties:
        alert_id:
          type: string
          description: Opsgenie Alert ID
        task_type:
          type: string
          enum:
            - update_opsgenie_alert
        message:
          type: string
          description: Message of the alert
        description:
          type: string
          description: >-
            Description field of the alert that is generally used to provide a
            detailed information about the alert
        priority:
          type: string
          enum:
            - P1
            - P2
            - P3
            - P4
            - P5
            - auto
        completion:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
      required:
        - alert_id
        - priority
        - completion
    update_opsgenie_incident_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_opsgenie_incident
        opsgenie_incident_id:
          type: string
          description: >-
            The Opsgenie incident ID, this can also be a Rootly incident
            variable ex. {{ incident.opsgenie_incident_id }}
        message:
          type: string
          description: Message of the alert
        description:
          type: string
          description: >-
            Description field of the alert that is generally used to provide a
            detailed information about the alert
        status:
          type: string
          enum:
            - resolve
            - open
            - close
            - auto
        priority:
          type: string
          enum:
            - P1
            - P2
            - P3
            - P4
            - P5
            - auto
            - ''
          nullable: true
      required:
        - opsgenie_incident_id
    page_rootly_on_call_responders_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - page_rootly_on_call_responders
        escalation_policy_target:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        service_target:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        user_target:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        group_target:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        functionality_target:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        alert_urgency_id:
          type: string
          description: Alert urgency ID
        summary:
          type: string
          description: Alert title
        description:
          type: string
          description: Alert description
        escalation_note:
          type: string
      required:
        - summary
        - alert_urgency_id
    page_pagerduty_on_call_responders_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - page_pagerduty_on_call_responders
        service:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        escalation_policies:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        users:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        title:
          type: string
          description: Incident title.
          nullable: true
        message:
          type: string
        urgency:
          type: string
          enum:
            - high
            - low
            - auto
          default: high
        priority:
          type: string
          description: >-
            PagerDuty incident priority, selecting auto will let Rootly auto map
            our incident severity
        create_new_incident_on_conflict:
          type: boolean
          description: >-
            Rootly only supports linking to a single PagerDuty incident. If this
            feature is disabled Rootly will add responders from any additional
            pages to the existing PagerDuty incident that is linked to the
            Rootly incident. If enabled, Rootly will create a new PagerDuty
            incident that is not linked to any Rootly incidents
          default: false
      required:
        - service
    page_victor_ops_on_call_responders_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - page_victor_ops_on_call_responders
        escalation_policies:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        users:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        title:
          type: string
          description: Alert title.
          nullable: true
      anyOf:
        - required:
            - users
        - required:
            - escalation_policies
    update_victor_ops_incident_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_victor_ops_incident
        victor_ops_incident_id:
          type: string
          description: >-
            The victor_ops incident ID, this can also be a Rootly incident
            variable ex. {{ incident.victor_ops_incident_id }}
        status:
          type: string
          enum:
            - resolve
            - ack
            - auto
        resolution_message:
          type: string
          description: Resolution message
      required:
        - victor_ops_incident_id
        - status
    print_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - print
        message:
          type: string
          description: The message to print
      required:
        - message
    publish_incident_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - publish_incident
        incident:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        public_title:
          type: string
        event:
          type: string
          description: Incident event description
        status:
          type: string
          enum:
            - investigating
            - identified
            - monitoring
            - resolved
            - scheduled
            - in_progress
            - completed
          default: resolved
        notify_subscribers:
          type: boolean
          description: When true notifies subscribers of the status page by email/text
          default: false
        should_tweet:
          type: boolean
          description: >-
            For Statuspage.io integrated pages auto publishes a tweet for your
            update
          default: false
        status_page_template:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        status_page_id:
          type: string
        integration_payload:
          type: string
          description: >-
            Additional API Payload you can pass to statuspage.io for example.
            Can contain liquid markup and need to be valid JSON
          nullable: true
      required:
        - incident
        - public_title
        - status
        - status_page_id
    redis_client_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - redis_client
        url:
          type: string
          example: redis://redis-12345.c1.us-east-1-2.ec2.cloud.redislabs.com:12345
        commands:
          type: string
        event_url:
          type: string
        event_message:
          type: string
        post_to_incident_timeline:
          type: boolean
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - url
        - commands
    rename_slack_channel_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - rename_slack_channel
        channel:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        title:
          type: string
      required:
        - title
        - channel
    change_slack_channel_privacy_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - rename_slack_channel
        channel:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        privacy:
          type: string
          enum:
            - private
            - public
      required:
        - title
        - privacy
    run_command_heroku_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - run_command_heroku
        command:
          type: string
        app_name:
          type: string
        size:
          type: string
          enum:
            - standard-1X
            - standard-2X
        post_to_incident_timeline:
          type: boolean
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - command
        - app_name
        - size
    send_email_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - send_email
        from:
          type: string
          description: >-
            The from email address. Need to use SMTP integration if different
            than rootly.com
          default: Rootly <workflows@rootly.com>
        to:
          type: array
          items:
            type: string
            description: To address email
        cc:
          type: array
          items:
            type: string
            description: Cc address email
        bcc:
          type: array
          items:
            type: string
            description: Bcc address email
        subject:
          type: string
          description: The subject
        preheader:
          type: string
          description: The preheader
          nullable: true
        body:
          type: string
          description: The email body
          nullable: true
        include_header:
          type: boolean
        include_footer:
          type: boolean
        custom_logo_url:
          type: string
          description: URL to your custom email logo
          nullable: true
      required:
        - to
        - subject
        - body
    send_dashboard_report_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - send_dashboard_report
        dashboard_ids:
          type: array
          items:
            type: string
        from:
          type: string
          description: >-
            The from email address. Need to use SMTP integration if different
            than rootly.com
          default: Rootly <workflows@rootly.com>
        to:
          type: array
          items:
            type: string
            description: The recipient
        subject:
          type: string
          description: The subject
        preheader:
          type: string
          description: The preheader
          nullable: true
        body:
          type: string
          description: The email body
          nullable: true
      required:
        - dashboard_ids
        - to
        - subject
        - body
    create_slack_channel_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_slack_channel
        workspace:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        title:
          type: string
          description: Slack channel title
        private:
          type: string
          enum:
            - auto
            - 'true'
            - 'false'
          default: auto
      required:
        - workspace
        - title
    send_slack_message_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - send_slack_message
        channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        slack_users:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        slack_user_groups:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        actionables:
          type: array
          items:
            type: string
            enum:
              - update_summary
              - update_status
              - archive_channel
              - manage_incident_roles
              - update_incident
              - all_commands
              - leave_feedback
              - manage_form_fields
              - manage_action_items
              - view_tasks
              - add_pagerduty_responders
              - add_opsgenie_responders
              - add_victor_ops_responders
              - update_status_page
              - pause_reminder
              - snooze_reminder
              - restart_reminder
              - cancel_incident
              - delete_message
        broadcast_thread_reply_to_channel:
          type: boolean
        send_as_ephemeral:
          type: boolean
        color:
          type: string
          description: 'A hex color ex. #FFFFFF'
        pin_to_channel:
          type: boolean
        update_parent_message:
          type: boolean
        thread_ts:
          type: string
          description: The thread to send the message into
        parent_message_thread_task:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: >-
            A hash where [id] is the task id of the parent task that sent a
            message, and [name] is the name of the parent task
        text:
          type: string
          description: The message text
        send_only_as_threaded_message:
          type: boolean
          description: >-
            When set to true, if the parent for this threaded message cannot be
            found the message will be skipped.
      required:
        - text
      anyOf:
        - required:
            - channels
        - required:
            - slack_users
        - required:
            - slack_user_groups
    send_sms_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - send_sms
        phone_numbers:
          type: array
          items:
            type: string
            description: A recipient phone number
            example:
              - '14150001111'
        name:
          type: string
          description: The name
        content:
          type: string
          description: The SMS message
      required:
        - phone_numbers
        - name
        - content
    send_whatsapp_message_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - send_whatsapp_message
        phone_numbers:
          type: array
          items:
            type: string
            description: A recipient phone number
            example:
              - '14150001111'
        name:
          type: string
          description: The name
        content:
          type: string
          description: The WhatsApp message
      required:
        - phone_numbers
        - name
        - content
    snapshot_datadog_graph_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - snapshot_datadog_graph
        dashboards:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        past_duration:
          type: string
          description: in format '1 minute', '30 days', '3 months', etc
          example: 1 hour
        metric_queries:
          type: array
          items:
            type: string
        post_to_incident_timeline:
          type: boolean
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - past_duration
    snapshot_grafana_dashboard_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - snapshot_grafana_dashboard
        dashboards:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        post_to_incident_timeline:
          type: boolean
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - dashboards
    snapshot_looker_look_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - snapshot_looker_look
        dashboards:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        post_to_incident_timeline:
          type: boolean
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - dashboards
    snapshot_new_relic_graph_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - snapshot_looker_graph
        metric_query:
          type: string
        metric_type:
          type: string
          enum:
            - APDEX
            - AREA
            - BAR
            - BASELINE
            - BILLBOARD
            - BULLET
            - EVENT_FEED
            - FUNNEL
            - HEATMAP
            - HISTOGRAM
            - LINE
            - PIE
            - SCATTER
            - STACKED_HORIZONTAL_BAR
            - TABLE
            - VERTICAL_BAR
        post_to_incident_timeline:
          type: boolean
        post_to_slack_channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
      required:
        - metric_query
        - metric_type
    tweet_twitter_message_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - tweet_twitter_message
        message:
          type: string
      required:
        - message
    update_airtable_table_record_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_airtable_table_record
        base_key:
          type: string
          description: The base key
        table_name:
          type: string
          description: The table name
        record_id:
          type: string
          description: The record id
        custom_fields_mapping:
          type: string
          description: >-
            Custom field mappings. Can contain liquid markup and need to be
            valid JSON
          nullable: true
      required:
        - base_key
        - table_name
        - record_id
    update_asana_task_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_asana_task
        task_id:
          type: string
          description: The task id
        title:
          type: string
          description: The task title
        notes:
          type: string
        assign_user_email:
          type: string
          description: The assigned user's email
        completion:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        due_date:
          type: string
          description: The due date
        custom_fields_mapping:
          type: string
          description: >-
            Custom field mappings. Can contain liquid markup and need to be
            valid JSON
          nullable: true
        dependency_direction:
          type: string
          enum:
            - blocking
            - blocked_by
          default: blocking
        dependent_task_ids:
          type: array
          description: Dependent task ids. Supports liquid syntax
          items:
            type: string
          nullable: true
      required:
        - task_id
        - completion
    update_github_issue_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_github_issue
        issue_id:
          type: string
          description: The issue id
        title:
          type: string
          description: The issue title
        body:
          type: string
          description: The issue body
        completion:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
      required:
        - issue_id
        - completion
    update_gitlab_issue_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_gitlab_issue
        issue_id:
          type: string
          description: The issue id
        issue_type:
          type: string
          description: The issue type
          enum:
            - issue
            - incident
            - test_case
            - task
        title:
          type: string
          description: The issue title
        description:
          type: string
          description: The issue description
        labels:
          type: string
          description: The issue labels
        due_date:
          type: string
          description: The due date
        completion:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
      required:
        - issue_id
        - completion
    update_incident_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_incident
        attribute_to_query_by:
          type: string
          enum:
            - id
            - slug
            - sequential_id
            - pagerduty_incident_id
            - opsgenie_incident_id
            - victor_ops_incident_id
            - jira_issue_id
            - asana_task_id
            - shortcut_task_id
            - linear_issue_id
            - zendesk_ticket_id
            - motion_task_id
            - trello_card_id
            - airtable_record_id
            - shortcut_story_id
            - github_issue_id
            - gitlab_issue_id
            - freshservice_ticket_id
            - freshservice_task_id
            - clickup_task_id
          default: id
        incident_id:
          type: string
          description: The incident id to update or id of any attribute on the incident
        title:
          type: string
          description: The incident title
          nullable: true
        summary:
          type: string
          description: The incident summary
          nullable: true
        status:
          type: string
          nullable: true
        severity_id:
          type: string
          nullable: true
        incident_type_ids:
          type: array
          items:
            type: string
          nullable: true
        service_ids:
          type: array
          items:
            type: string
          description: Array of service UUIDs
          nullable: true
        functionality_ids:
          type: array
          items:
            type: string
          description: Array of functionality UUIDs
          nullable: true
        environment_ids:
          type: array
          items:
            type: string
          nullable: true
        group_ids:
          type: array
          items:
            type: string
          description: Array of group/team UUIDs
          nullable: true
        started_at:
          type: string
          nullable: true
        detected_at:
          type: string
          nullable: true
        acknowledged_at:
          type: string
          nullable: true
        mitigated_at:
          type: string
          nullable: true
        resolved_at:
          type: string
          nullable: true
        private:
          type: boolean
        custom_fields_mapping:
          type: string
          description: >-
            Custom field mappings. Can contain liquid markup and need to be
            valid JSON. Use 'services', 'functionalities', or 'groups' keys with
            arrays of names/slugs for name/slug lookup
          nullable: true
      required:
        - incident_id
    update_incident_postmortem_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_incident_postmortem
        postmortem_id:
          type: string
          description: UUID of the retrospective that needs to be updated
        title:
          type: string
          description: The incident title
          nullable: true
        status:
          type: string
          nullable: true
      required:
        - postmortem_id
    update_jira_issue_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_jira_issue
        issue_id:
          type: string
          description: The issue id
        title:
          type: string
          description: The issue title
        description:
          type: string
          description: The issue description
        labels:
          type: string
          description: The issue labels
        assign_user_email:
          type: string
          description: The assigned user's email
        reporter_user_email:
          type: string
          description: The reporter user's email
        project_key:
          type: string
          description: The project key
        due_date:
          type: string
          description: The due date
        priority:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The priority id and display name
        status:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The status id and display name
        custom_fields_mapping:
          type: string
          description: >-
            Custom field mappings. Can contain liquid markup and need to be
            valid JSON
          nullable: true
        update_payload:
          type: string
          description: Update payload. Can contain liquid markup and need to be valid JSON
          nullable: true
      required:
        - issue_id
        - project_key
    update_linear_issue_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_linear_issue
        issue_id:
          type: string
          description: The issue id
        title:
          type: string
          description: The issue title
        description:
          type: string
          description: The issue description
        state:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The state id and display name
          nullable: true
        project:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The project id and display name
        labels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        priority:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The priority id and display name
        assign_user_email:
          type: string
          description: The assigned user's email
      required:
        - issue_id
    update_service_now_incident_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_service_now_incident
        incident_id:
          type: string
          description: The incident id
        title:
          type: string
          description: The incident title
        description:
          type: string
          description: The incident description
        priority:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The priority id and display name
        completion:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The completion id and display name
        custom_fields_mapping:
          type: string
          description: >-
            Custom field mappings. Can contain liquid markup and need to be
            valid JSON
          nullable: true
      required:
        - incident_id
    update_shortcut_story_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_shortcut_story
        story_id:
          type: string
          description: The story id
        title:
          type: string
          description: The incident title
        description:
          type: string
          description: The incident description
        labels:
          type: string
          description: The story labels
        due_date:
          type: string
          description: The due date
        archivation:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The archivation id and display name
      required:
        - story_id
        - archivation
    update_shortcut_task_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_shortcut_task
        task_id:
          type: string
          description: The task id
        parent_story_id:
          type: string
          description: The parent story
        description:
          type: string
          description: The task description
        completion:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The completion id and display name
      required:
        - task_id
        - parent_story_id
        - completion
    update_slack_channel_topic_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_slack_channel_topic
        channel:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        topic:
          type: string
      required:
        - channel
        - topic
    update_status_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_status
        status:
          type: string
          enum:
            - in_triage
            - started
            - mitigated
            - resolved
            - closed
            - cancelled
        inactivity_timeout:
          type: string
          description: In format '1 hour', '1 day', etc
          example: 1 hour
      required:
        - status
    update_incident_status_timestamp_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_status
        sub_status_id:
          type: string
          description: Sub-status to update timestamp for
        assigned_at:
          type: string
          description: Timestamp of when the sub-status was assigned
      required:
        - sub_status_id
        - assigned_at
    update_trello_card_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_trello_card
        card_id:
          type: string
          description: The card id
        title:
          type: string
          description: The card title
        description:
          type: string
          description: The card description
        due_date:
          type: string
          description: The due date
        board:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The board id and display name
        list:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The list id and display name
        labels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        archivation:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The archivation id and display name
      required:
        - card_id
        - archivation
    update_clickup_task_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_clickup_task
        task_id:
          type: string
          description: The task id
        title:
          type: string
          description: The task title
        description:
          type: string
          description: The task description
        tags:
          type: string
          description: The task tags
        priority:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The priority id and display name
        due_date:
          type: string
          description: The due date
        custom_fields_mapping:
          type: string
          description: >-
            Custom field mappings. Can contain liquid markup and need to be
            valid JSON
          nullable: true
        task_payload:
          type: string
          description: >-
            Additional ClickUp task attributes. Will be merged into whatever was
            specified in this tasks current parameters. Can contain liquid
            markup and need to be valid JSON
          nullable: true
      required:
        - task_id
    update_motion_task_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_motion_task
        task_id:
          type: string
          description: The task id
        title:
          type: string
          description: The task title
        description:
          type: string
          description: The task description
        labels:
          type: array
          items:
            type: string
        priority:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The priority id and display name
        duration:
          type: string
          description: The duration. Eg.  "NONE", "REMINDER", or a integer greater than 0.
        due_date:
          type: string
          description: The due date
      required:
        - task_id
    update_zendesk_ticket_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_zendesk_ticket
        ticket_id:
          type: string
          description: The ticket id
        subject:
          type: string
          description: The ticket subject
        tags:
          type: string
          description: The ticket tags
        priority:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The priority id and display name
        completion:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: The completion id and display name
        custom_fields_mapping:
          type: string
          description: >-
            Custom field mappings. Can contain liquid markup and need to be
            valid JSON
          nullable: true
        ticket_payload:
          type: string
          description: >-
            Additional Zendesk ticket attributes. Will be merged into whatever
            was specified in this tasks current parameters. Can contain liquid
            markup and need to be valid JSON
          nullable: true
      required:
        - ticket_id
    update_attached_alerts_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - update_attached_alerts
        status:
          type: string
          enum:
            - acknowledged
            - resolved
      required:
        - status
    trigger_workflow_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - trigger_workflow
        kind:
          type: string
          enum:
            - incident
            - post_mortem
            - action_item
            - pulse
            - alert
          default: incident
        attribute_to_query_by:
          type: string
          enum:
            - id
            - slug
            - sequential_id
            - pagerduty_incident_id
            - opsgenie_incident_id
            - victor_ops_incident_id
            - jira_issue_id
            - asana_task_id
            - shortcut_task_id
            - linear_issue_id
            - zendesk_ticket_id
            - motion_task_id
            - trello_card_id
            - airtable_record_id
            - shortcut_story_id
            - github_issue_id
            - freshservice_ticket_id
            - freshservice_task_id
            - clickup_task_id
          default: id
          description: >-
            ["(incident) kind can only match [:id, :slug, :sequential_id,
            :pagerduty_incident_id, :opsgenie_incident_id,
            :victor_ops_incident_id, :jira_issue_id, :asana_task_id,
            :shortcut_task_id, :linear_issue_id, :zendesk_ticket_id,
            :motion_task_id, :trello_card_id, :airtable_record_id,
            :shortcut_story_id, :github_issue_id, :freshservice_ticket_id,
            :freshservice_task_id, :clickup_task_id]", "(post_mortem) kind can
            only match [:id]", "(action_item) kind can only match [:id,
            :jira_issue_id, :asana_task_id, :shortcut_task_id, :linear_issue_id,
            :zendesk_ticket_id, :motion_task_id, :trello_card_id,
            :airtable_record_id, :shortcut_story_id, :github_issue_id,
            :freshservice_ticket_id, :freshservice_task_id, :clickup_task_id]",
            "(pulse) kind can only match [:id]", "(alert) kind can only match
            [:id]"]
        resource:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        workflow:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        check_workflow_conditions:
          type: boolean
      required:
        - kind
        - workflow
        - resource
        - attribute_to_query_by
    send_slack_blocks_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - send_slack_blocks
        message:
          type: string
        blocks:
          type: string
          description: >-
            Support liquid markup. Needs to be a valid JSON string after liquid
            is parsed
        attachments:
          type: string
          description: >-
            Support liquid markup. Needs to be a valid JSON string after liquid
            is parsed
        channels:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        slack_users:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        slack_user_groups:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
        broadcast_thread_reply_to_channel:
          type: boolean
        send_as_ephemeral:
          type: boolean
        pin_to_channel:
          type: boolean
        thread_ts:
          type: string
          description: The thread to send the message into
        update_parent_message:
          type: boolean
        parent_message_thread_task:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: >-
            A hash where [id] is the task id of the parent task that sent a
            message, and [name] is the name of the parent task
        send_only_as_threaded_message:
          type: boolean
          description: >-
            When set to true, if the parent for this threaded message cannot be
            found the message will be skipped.
      required:
        - blocks
      anyOf:
        - required:
            - channels
        - required:
            - slack_users
        - required:
            - slack_user_groups
    create_openai_chat_completion_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - openai_chat_completion
        model:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: 'The OpenAI model. eg: gpt-5-nano'
        system_prompt:
          type: string
          description: The system prompt to send to OpenAI (optional)
        prompt:
          type: string
          description: The prompt to send to OpenAI
        temperature:
          type: number
          description: >-
            Controls randomness in the response. Higher values make output more
            random
          minimum: 0
          maximum: 2
        max_tokens:
          type: integer
          description: Maximum number of tokens to generate in the response
          minimum: 1
        top_p:
          type: number
          description: >-
            Controls diversity via nucleus sampling. Lower values make output
            more focused
          minimum: 0
          maximum: 1
        reasoning_effort:
          type: string
          description: Constrains effort on reasoning for GPT-5 and o-series models
          enum:
            - minimal
            - low
            - medium
            - high
        reasoning_summary:
          type: string
          description: >-
            Summary of the reasoning performed by the model for GPT-5 and
            o-series models
          enum:
            - auto
            - concise
            - detailed
      required:
        - model
        - prompt
    create_watsonx_chat_completion_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_watsonx_chat_completion_task
        model:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: 'The WatsonX model. eg: ibm/granite-3-b8b-instruct'
        system_prompt:
          type: string
          description: The system prompt to send to WatsonX (optional)
        prompt:
          type: string
          description: The prompt to send to WatsonX
        project_id:
          type: string
      required:
        - project_id
        - model
        - prompt
    create_google_gemini_chat_completion_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_google_gemini_chat_completion_task
        model:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: 'The Gemini model. eg: gemini-2.0-flash'
        system_prompt:
          type: string
          description: The system prompt to send to Gemini (optional)
        prompt:
          type: string
          description: The prompt to send to Gemini
      required:
        - model
        - prompt
    create_mistral_chat_completion_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_mistral_chat_completion_task
        model:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: 'The Mistral model. eg: mistral-large-latest'
        system_prompt:
          type: string
          description: The system prompt to send to Mistral (optional)
        prompt:
          type: string
          description: The prompt to send to Mistral
        temperature:
          type: number
          minimum: 0
          maximum: 1.5
          description: >-
            Sampling temperature (0.0-1.5). Higher values make output more
            random.
        max_tokens:
          type: integer
          minimum: 1
          description: Maximum number of tokens to generate
        top_p:
          type: number
          minimum: 0
          maximum: 1
          description: Nucleus sampling parameter (0.0-1.0)
      required:
        - model
        - prompt
    create_anthropic_chat_completion_task_params:
      type: object
      properties:
        task_type:
          type: string
          enum:
            - create_anthropic_chat_completion_task
        model:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
          description: 'The Anthropic model. eg: claude-3-5-sonnet-20241022'
        system_prompt:
          type: string
          description: The system prompt to send to Anthropic (optional)
        prompt:
          type: string
          description: The prompt to send to Anthropic
      required:
        - model
        - prompt
  securitySchemes:
    bearer_auth:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).