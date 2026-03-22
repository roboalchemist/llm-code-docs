# Source: https://docs.rootly.com/liquid/team-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Team Variables

> Reference guide for team variables available in Liquid templates including team metrics, user data, and integration mappings.

## Variables

<Note>
  Use our new [Liquid Markup explorer](https://rootly.com/account/help/liquid-explorer "Liquid Markup explorer") to navigate through all incident variables.
</Note>

We are using [Liquid](https://shopify.github.io/liquid/ "Liquid") template language and available variables are:

```ruby Ruby theme={null}
# Basic team info
{{ team.id }} # returns string
{{ team.name }} # returns string
{{ team.slug }} # returns string
{{ team.time_zone }} # returns string
{{ team.generated_incident_title }} # returns string

# Incident counts
{{ team.incidents_count }} # returns integer
{{ team.incidents_test_count }} # returns integer
{{ team.incidents_normal_count }} # returns integer
{{ team.incidents_scheduled_count }} # returns integer
{{ team.incidents_backfilled_count }} # returns integer

# Action item counts
{{ team.action_items_count }} # returns integer
{{ team.action_items_follow_up_count }} # returns integer
{{ team.action_items_task_count }} # returns integer
{{ team.action_items_open_count }} # returns integer
{{ team.action_items_in_progress_count }} # returns integer
{{ team.action_items_cancelled_count }} # returns integer
{{ team.action_items_completed_count }} # returns integer

# Configuration flags
{{ team.config_ai_enabled }} # returns boolean
{{ team.config_ai_summarization_enabled }} # returns boolean
{{ team.config_ai_similarities_enabled }} # returns boolean
{{ team.config_sub_status_enabled }} # returns boolean

# User arrays
{{ team.users }} # returns array
{{ team.jira_users }} # returns array
{{ team.pagerduty_users }} # returns array

# Objects (keyed by slug)
{{ team.form_fields }} # returns object
{{ team.post_mortem_templates }} # returns object (keyed by slug)
{{ team.schedules }} # returns object (keyed by slug)
{{ team.services }} # returns object (keyed by slug)
{{ team.functionalities }} # returns object (keyed by slug)
{{ team.groups }} # returns object (keyed by slug)
```

# Examples[](#Qf7Nq)

### User reverse lookup up by email[](#BL-rb)

```ruby Ruby theme={null}
{{ team.users | find: 'email', 'john@doe.com' | get: 'name' }}
{{ team.users | find: 'email', 'john@doe.com' | get: 'slack_id' }}
```


Built with [Mintlify](https://mintlify.com).