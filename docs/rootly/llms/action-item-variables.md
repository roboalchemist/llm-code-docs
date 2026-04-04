# Source: https://docs.rootly.com/liquid/action-item-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Action Item Variables

> Reference guide for action item variables available in Liquid templates for Genius workflows and integration formatting.

You can use action item variables with genius workflows:

# Variables

<Note>
  Use our new [Liquid Markup explorer](https://rootly.com/account/help/liquid-explorer) to navigate through all action item variables.
</Note>

We are using [Liquid](https://shopify.github.io/liquid/) template language and available variables are:

```ruby Ruby theme={null}
{{ action_item.id }} # returns string (uuid)
{{ action_item.summary }} #returns string
{{ action_item.description }} #returns string
{{ action_item.status }} # returns string
{{ action_item.priority }} # returns integer
{{ action_item.due_date }} # returns datetime
{{ action_item.url }} # returns string
{{ action_item.short_url }} # returns string
{{ action_item.jira_issue_id }} # returns string
{{ action_item.jira_issue_url }} # returns string
{{ action_item.asana_task_id }} # returns string
{{ action_item.asana_task_url }} # returns string
{{ action_item.clubhouse_task_id }} # returns string
{{ action_item.clubhouse_task_url }} # returns string
{{ action_item.trello_check_item_id }} # returns string
{{ action_item.trello_check_item_url }} # returns string
{{ action_item.linear_issue_id }} # returns string
{{ action_item.linear_issue_url }} # returns string
{{ action_item.zendesk_ticket_id }} # returns string
{{ action_item.zendesk_ticket_url }} # returns string
{{ action_item.service_now_case_id }} # returns string
{{ action_item.service_now_case_url }} # returns string
{{ action_item.created_at }} # returns datetime
{{ action_item.updated_at }} # returns datetime
{{ incident.creator }} # returns object eg. {"id":49, "name":"John Doe", "email":"john@acme.com"}
{{ incident.assigned_to }} # returns object eg. {"id":49, "name":"John Doe", "email":"john@acme.com"}

# Integrations

{{ action_item.jira_issue_id }} # returns string
{{ action_item.jira_issue_key }} # returns string
{{ action_item.jira_issue_url }} # returns string
{{ action_item.asana_task_id }} # returns string
{{ action_item.asana_task_url }} # returns string
{{ action_item.shortcut_story_id }} # returns string
{{ action_item.shortcut_story_url }} # returns string
{{ action_item.shortcut_task_id }} # returns string
{{ action_item.shortcut_task_url }} # returns string
{{ action_item.trello_card_id }} # returns string
{{ action_item.trello_card_url }} # returns string
{{ action_item.linear_issue_id }} # returns string
{{ action_item.linear_issue_key }} # returns string
{{ action_item.linear_issue_url }} # returns string
{{ action_item.zendesk_ticket_id }} # returns string
{{ action_item.zendesk_ticket_url }} # returns string
{{ action_item.service_now_case_id }} # returns string
{{ action_item.service_now_case_url }} # returns string
{{ action_item.airtable_base_key }} # returns string
{{ action_item.airtable_table_name }} # returns string
{{ action_item.airtable_record_id }} # returns string
{{ action_item.airtable_record_url }} # returns string
{{ action_item.freshservice_ticket_id }} # returns string
{{ action_item.freshservice_ticket_url }} # returns string
{{ action_item.freshservice_task_id }} # returns string
{{ action_item.freshservice_task_url }} # returns string
```

# Examples

```ruby Ruby theme={null}
action-item-{{ action_item.created_at | date: "%Y%m%d" }}
# Will result in: action-item-20210412
```


Built with [Mintlify](https://mintlify.com).