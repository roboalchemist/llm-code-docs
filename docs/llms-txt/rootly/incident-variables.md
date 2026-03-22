# Source: https://docs.rootly.com/liquid/incident-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Incident Variables

> Complete reference of all available incident variables for Liquid templating in workflows, Slack formatting, and postmortem templates.

You can use incident variables in different parts of our application like:

* Slack title format
* Postmortem templates
* Genius workflow blocks
* etc.

# Variables

<Note>
  Use our new [Liquid Markup explorer](https://rootly.com/account/help/liquid-explorer) to navigate through all incident variables.
</Note>

We are using [Liquid](https://shopify.github.io/liquid/) template language and available variables are:

```ruby Ruby theme={null}
{{ incident.id }} # returns string
{{ incident.sequential_id }} # returns integer
{{ incident.slug }} # returns string
{{ incident.title }} # returns string
{{ incident.summary }} # returns string
{{ incident.status }} # returns string
{{ incident.labels }} # returns array
{{ incident.timeline }} # returns array
{{ incident.timeline_table }} # returns string
{{ incident.timeline_table_markdown }} # returns string
{{ incident.timeline_table_markdown2 }} # returns string
{{ incident.timeline_table_atlassian }} # returns string
# DEPRECATED {{ incident.status_page_timeline }} # returns array
# DEPRECATED {{ incident.status_page_timeline_table }} # returns string
# DEPRECATED {{ incident.status_page_timeline_table_markdown }} # returns string
# DEPRECATED {{ incident.status_page_timeline_table_markdown2 }} # returns string
# See section below for new way
{{ incident.severity }} # returns string
{{ incident.severity_slug }} # returns string
{{ incident.environments }} # returns array
{{ incident.environment_slugs }} # returns array
{{ incident.raw_environments }} # returns array of objects
{{ incident.types }} # returns array
{{ incident.types_slugs }} # returns array
{{ incident.raw_types }} # returns array of objects
{{ incident.services }} # returns array
{{ incident.services_slug }} # returns array
{{ incident.raw_services }} # returns array of objects
{{ incident.functionalities }} # returns array
{{ incident.functionality_slugs }} # returns array
{{ incident.raw_functionalities }} # returns array of objects
{{ incident.groups }} # returns array
{{ incident.group_slugs }} # returns array
{{ incident.raw_groups }} # returns array of objects
{{ incident.created_at }} # returns datetime
{{ incident.started_at }} # returns datetime
{{ incident.detected_at }} # returns datetime
{{ incident.acknowledged_at }} # returns datetime
{{ incident.mitigated_at }} # returns datetime
{{ incident.resolved_at }} # returns datetime
{{ incident.time_to_mitigation }} # returns integer (in hours)
{{ incident.mitigation_message }} # return string
{{ incident.time_to_resolution }} # returns integer (in hours)
{{ incident.resolution_message }} # return string
{{ incident.time_to_detection }} # returns integer (in hours)
{{ incident.detection_duration }} # returns integer (in seconds)
{{ incident.time_to_mitigation }} # returns integer (in hours)
{{ incident.mitigation_duration }} # returns integer (in seconds)
{{ incident.time_to_acknowledge }} # returns integer (in hours)
{{ incident.acknowledge_duration }} # returns integer (in seconds)
{{ incident.duration }} # returns integer (in seconds)
{{ incident.url }} # returns string
{{ incident.short_url }} # returns string
{{ incident.postmortem_url }} # returns string
{{ incident.notify_emails }} # returns array of string
{{ incident.creator }} # returns object eg. {"id":49, "name":"John Doe", "email":"john@acme.com"}
{{ incident.in_triage }} # returns object eg. {"id":49, "name":"John Doe", "email":"john@acme.com"}
{{ incident.started_by }} # returns object eg. {"id":49, "name":"John Doe", "email":"john@acme.com"}
{{ incident.mitigated_by }} # returns object eg. {"id":49, "name":"John Doe", "email":"john@acme.com"}
{{ incident.resolved_by }} # returns object eg. {"id":49, "name":"John Doe", "email":"john@acme.com"}
{{ incident.cancelled_by }} # returns object eg. {"id":49, "name":"John Doe", "email":"john@acme.com"}
{{ incident.roles }} # returns array of objects eg. [{"incident_role": {"name" : "Commander"}, "user": {name: "John Doe", email: "john@acme.com"}}]
{{ incident.custom_fields }} # returns array of objects eg. [{"custom_fields": {"slug" : "my-custom-field"}, "selected_options": {value: ["Foo", "Bar"]}}]
{{ incident.scheduled_for }} # Returns datetime
{{ incident.scheduled_until }} # Returns datetime

# Integrations
{{ incident.zoom_meeting_id }} # returns string
{{ incident.zoom_meeting_start_url }} # returns string
{{ incident.zoom_meeting_join_url }} # returns string
{{ incident.webex_meeting_id }} # returns string
{{ incident.webex_meeting_url }} # returns string
{{ incident.shortcut_story_id }} # returns string
{{ incident.shortcut_story_url }} # returns string
{{ incident.shortcut_task_id }} # returns string
{{ incident.shortcut_task_url }} # returns string
{{ incident.asana_task_id }} # returns string
{{ incident.asana_task_url }} # returns string
{{ incident.jira_issue_id }} # returns string
{{ incident.jira_issue_key }} # returns string
{{ incident.jira_issue_url }} # returns string
{{ incident.google_meeting_id }} # returns string
{{ incident.google_meeting_url }} # returns string
{{ incident.trello_card_id }} # returns string
{{ incident.trello_card_url }} # returns string
{{ incident.linear_issue_id }} # returns string
{{ incident.linear_issue_key }} # returns string
{{ incident.linear_issue_url }} # returns string
{{ incident.zendesk_ticket_id }} # returns string
{{ incident.zendesk_ticket_url }} # returns string
{{ incident.slack_channel_name }} # returns string
{{ incident.slack_channel_id }} # returns string
{{ incident.slack_channel_url }} # returns string
{{ incident.slack_channel_short_url }} # returns string
{{ incident.slack_channel_deep_link }} # returns string
{{ incident.microsoft_teams_channel_id }} # returns string
{{ incident.microsoft_teams_channel_name }} # returns string
{{ incident.microsoft_teams_channel_url }} # returns string
{{ incident.microsoft_teams_chat_id }} # returns string
{{ incident.microsoft_teams_chat_url }} # returns string
{{ incident.service_now_incident_id }} # returns string
{{ incident.service_now_incident_url }} # returns string
{{ incident.opsgenie_incident_id }} # returns string
{{ incident.opsgenie_incident_url }} # returns string
{{ incident.victor_ops_incident_id }} # returns string
{{ incident.victor_ops_incident_url }} # returns string
{{ incident.pagerduty_incident_id }} # returns string
{{ incident.pagerduty_incident_number }} # returns string
{{ incident.pagerduty_incident_url }} # returns string
{{ incident.mattermost_channel_id }} # returns string
{{ incident.mattermost_channel_name }} # returns string
{{ incident.mattermost_channel_url }} # returns string
{{ incident.confluence_page_id }} # returns string
{{ incident.confluence_page_url }} # returns string
{{ incident.airtable_base_key }} # returns string
{{ incident.airtable_table_name }} # returns string
{{ incident.airtable_record_id }} # returns string
{{ incident.airtable_record_url }} # returns string
{{ incident.google_drive_id }} # returns string
{{ incident.google_drive_url }} # returns string
{{ incident.notion_page_id }} # returns string
{{ incident.notion_page_url }} # returns string
{{ incident.datadog_notebook_id }} # returns string
{{ incident.datadog_notebook_url }} # returns string
{{ incident.freshservice_ticket_id }} # returns string
{{ incident.freshservice_ticket_url }} # returns string
{{ incident.freshservice_task_id }} # returns string
{{ incident.freshservice_task_url }} # returns string
{{ incident.service_now_incident_id }} # returns string
{{ incident.service_now_incident_url }} # returns string
```

# Examples

```ruby Ruby theme={null}
incident-{{ incident.started_at | date: "%Y%m%d" }}-{{ incident.slug }}
# Will result in: incident-20210412-customers-unable-to-place-orders-on-our-website
incident-{{ incident.created_at | date: "%Y%m%d" }}-{{ incident.jira_issue_url | split: "/" | last}}
# Will result in: incident-20210412-ROOT-233
{{ incident.created_at | in_time_zone: "Europe/London" | date: "%Y-%m-%d" }}
# Will result in: 2021-04-12
```

### List Roles

```ruby Ruby theme={null}
{%- for role in incident.roles -%}
  {%- if role.user -%}
    {{ role.incident_role.name }} : {{ role.user.full_name }}
  {%- else -%}
    {{ role.incident_role.name }} : N/A
  {%- endif -%}
{%- endfor -%}

# Will result of:
# Commander: John Doe
# Scriber: N/A
```

### List custom fields

```ruby Ruby theme={null}
# Text Field
{{ incident.custom_fields | find: 'custom_field.slug', 'your_custom_field_slug' | get: 'selected_options.value' }}

# Select & Multi Select
{{ incident.custom_fields | find: 'custom_field.slug', 'your_custom_field_slug' | get: 'selected_options' | map: 'value' }}

# Select & Multi Select using Teams options
{{ incident.custom_fields | find: 'custom_field.slug', 'custom-field-groups' | get: 'selected_groups' | map: 'name' }}

# Select & Multi Select using Services options
{{ incident.custom_fields | find: 'custom_field.slug', 'custom-field-services' | get: 'selected_services' | map: 'name' }}

# Users Field
{{ incident.custom_fields | find: 'custom_field.slug', 'your_custom_field_slug' | get: 'selected_users' | map: 'full_name' }}
```

### List timeline events

```ruby Ruby theme={null}
{% for item in incident.events %}
  {{ item.occurred_at }} - {{ item.event }}
{% endfor %}
```

### Convert timeline events to table

```ruby Ruby theme={null}
# ASCII Table
{{ incident.events | to_table: 'events', 'Hello world', 'America/Los_Angeles' }}
# Returns
# +---------------------------------------------------+
# |                    Hello world                    |
# +------------------------------+----------+---------+
# | Date                         | User     | Event   |
# +------------------------------+----------+---------+
# | December 8 2022 23:04:28 PST | John D   | Event 1 |
# | December 8 2022 23:04:28 PST | Dalyte K | Event 2 |
# +------------------------------+----------+---------+

# Markdown table
{{ incident.events | to_table: 'events', 'Hello world', 'America/Los_Angeles', 'markdown' }}
# Returns
# |                    Hello world                    |
# |------------------------------|----------|---------|
# | Date                         | User     | Event   |
# | December 8 2022 23:04:28 PST | John D   | Event 1 |
# | December 8 2022 23:04:28 PST | Dalyte K | Event 2 |

# Atlassian table
{{ incident.events | to_table: 'events', 'Hello world', 'America/Los_Angeles', 'atlassian_markdown' }}
# Returns
# h2. Hello world

# ||Date||User||Event||
# |December 8 2022 23:04:28 PST|John D|Event 1. [Link|https://dummy]|
# |December 8 2022 23:04:28 PST|Dalyte K|Event 2. [Link|https://dummy]|

# HTML table
{{ incident.events | to_table: 'events', 'Hello world', 'America/Los_Angeles', 'html' }}
# Returns
# <h2>Hello world</h2>

# <table>
#   <tr>
#     <th>Date</th>
#     <th>User</th>
#     <th>Event</th>
#   </tr>
#   <tr>
#      <td>December 8 2022 23:04:28 PST</td>
#      <td>John D</td>
#      <td>Event 1</td>
#   </tr>
#   <tr>
#     <td>December 8 2022 23:04:28 PST</td>
#     <td>Dalyte K</td>
#     <td>Event 2</td>
#   </tr>
# </table>
```

### List action items

```ruby Ruby theme={null}
{% for item in incident.action_items %}
  {{ item.summary }}
  Kind: {{item.kind}}
  Priority: {{item.priority}}
  Status: {{item.status}}
{% endfor %}
```

### Convert action items to table

```ruby Ruby theme={null}
# ASCII Table
{{ incident.action_items | to_table: 'action_items', 'Hello world', 'America/Los_Angeles' }}
# Returns
# +------------------------------------------------------------------------------------------------------------------------+
# |                                                      Hello world                                                       |
# +------------------------------+------------------------------+-----------+----------+--------+----------+---------------+
# | Creation Date                | Due Date                     | Kind      | Priority | Status | Assignee | Summary       |
# +------------------------------+------------------------------+-----------+----------+--------+----------+---------------+
# | December 7 2022 23:04:28 PST | December 8 2022 00:00:00 PST | Task      | Low      | Open   | John D   | Action Item 1 |
# | December 7 2022 23:04:28 PST | December 8 2022 00:00:00 PST | Follow Up | High     | Done   | Dalyte K | Action Item 2 |
# +------------------------------+------------------------------+-----------+----------+--------+----------+---------------+

# Markdown table
{{ incident.action_items | to_table: 'action_items', 'Hello world', 'America/Los_Angeles', 'markdown' }}
# Returns
# |                                                      Hello world                                                       |
# |------------------------------|------------------------------|-----------|----------|--------|----------|---------------|
# | Creation Date                | Due Date                     | Kind      | Priority | Status | Assignee | Summary       |
# | December 7 2022 23:04:28 PST | December 8 2022 00:00:00 PST | Task      | Low      | Open   | John D   | Action Item 1 |
# | December 7 2022 23:04:28 PST | December 8 2022 00:00:00 PST | Follow Up | High     | Done   | Dalyte K | Action Item 2 |

# Atlassian table
{{ incident.action_items | to_table: 'action_items', 'Hello world', 'America/Los_Angeles', 'atlassian_markdown' }}
# Returns
# h2. Hello world
# ||Creation Date||Due Date||Kind||Priority||Status||Assignee||Summary||
# |December 7 2022 23:04:28 PST|December 8 2022 00:00:00 PST|Task|Low|Open|John D|Action Item 1. [Link|https://dummy]|
# |December 7 2022 23:04:28 PST|December 8 2022 00:00:00 PST|Follow Up|High|Done|Dalyte K|Action Item 2. [Link|https://dummy]|

# HTML table
{{ incident.action_items | to_table: 'action_items', 'Hello world', 'America/Los_Angeles', 'html' }}
# Returns
#      <h2>Hello world</h2>
#      
#      <table>
#        <tr>
#          <th>Creation Date</th>
#          <th>Due Date</th>
#          <th>Kind</th>
#          <th>Priority</th>
#          <th>Status</th>
#          <th>Assignee</th>
#          <th>Summary</th>
#        </tr>
#        <tr>
#          <td>December 7 2022 23:04:28 PST</td>
#          <td>December 8 2022 00:00:00 PST</td>
#          <td>Task</td>
#          <td>Low</td>
#          <td>Open</td>
#          <td>John D</td>
#          <td>Action Item 1</td>
#        </tr>
#        <tr>
#          <td>December 7 2022 23:04:28 PST</td>
#          <td>December 8 2022 00:00:00 PST</td>
#          <td>Follow Up</td>
#          <td>High</td>
#          <td>Done</td>
#          <td>Dalyte K</td>
#          <td>Action Item 2</td>
#        </tr>
#      </table>
```

### Additional filters

```ruby Ruby theme={null}
# Find
# Input: {"books": [{ "id": 1, title: "hello" }, { "id": 2, title: "world" }] }
# Output: { "id": 2, title: "world" }

{ hash.books | find: 'id', '2' }

# Get
# Input: {"books": [{ "id": 1, title: "hello", category: {name: "History"} }}, { "id": 2, title: "world", category: {name: "SciFi"} }] }
# Output: "SciFi"

{ hash.books | find: 'id', '2' | get: 'category.name'}

# in_time_zone

{ 'now' | in_time_zone: "Europe/London" }

# smart_date

{ 'now' | smart_date: '2 days ago' }
{ 'now' | smart_date: '2 days ago' | in_time_zone: "Europe/London" }
{ 'now' | smart_date: '4 days from now' | in_time_zone: "Europe/London" }
{ 'now' | smart_date: 'yesterday' | in_time_zone: "Europe/London" }

# iso8601

{ 'now' | to_iso8601 }

# Distance of time in words
{ 'now' | smart_date: '2 days ago' | distance_of_time_in_words_from_now } # 2 days
```


Built with [Mintlify](https://mintlify.com).