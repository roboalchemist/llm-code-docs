# Source: https://docs.rootly.com/configuration/event-payloads.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Event Payloads

> Reference documentation for webhook event payload structures used in Rootly integrations and custom automations.

## alert.\*

```json JSON theme={null}
{
  "event": {
    "id": "9839c4ca-5e7b-416d-ad95-d09ae0c8eead",
    "type": "alert.created",
    "issued_at": "2022-11-27T19:15:29.546-08:00",
  },
  "data": {
    "id": "13c82722-ec52-4eda-aaa2-771f7c81c01c",
    "team_id": 1,
    "source": "pagerduty",
    "summary": "database-prod-002 Memory threshold over 85%",
    "labels": [],
    "data": {
      "hello": "world"
    },
    "external_id": "Q1IC19Z6U7MIQB",
    "external_url": "https://rootly.pagerduty.com/alerts/Q1IC19Z6U7MIQB",
    "webhook_type": null,
    "webhook_id": null,
    "webhook_idempotency_key": null,
    "started_at": "2022-11-27T19:15:29.546-08:00",
    "ended_at": null,
    "deleted_at": null,
    "created_at": "2022-11-27T19:15:29.546-08:00",
    "updated_at": "2022-11-27T19:15:29.546-08:00"
  }
}
```

## genius\_workflow\_run.\*

<Tabs>
  <Tab title="genius_workflow_run.queued">
    ```json JSON theme={null}
    {
    	"event":{
    		"id":"88a53013-05dc-44df-bb4f-c68d890f8bf9",
    		"type":"genius_workflow_run.queued",
    		"issued_at":"2022-12-19T08:02:03.067-08:00"
    	},
    	"data":{
    		"id":"daf992ed-df23-41df-a72c-438616b4f6dc",
    		"kind":"incident",
    		"status":"queued",
    		"status_message": null,
    		"user_id":3186,
    		"genius_workflow_id":"a1b76e56-e1ab-4b36-856f-b6481251c698",
    		"genius_workflow_name":"Send Email when incident starts",
    		"queued_at":"2022-12-19T08:02:03.031-08:00",
    		"started_at":null,
    		"completed_at":null,
    		"failed_at":null,
    	    "canceled_at":null,
    		"triggered_by":"system",
    		"created_at":"2022-12-19T08:02:03.031-08:00",
    		"updated_at":"2022-12-19T08:02:03.031-08:00",		 
            "incident_id":"5c80f5a1-9389-4970-bb49-8268acf2954f",
    		"incident_action_item_id":null,
    		"incident_post_mortem_id":null,
    		"alert_id":null,
    		"pulse_id":null
    	}
    }
    ```
  </Tab>

  <Tab title="genius_workflow_run.started">
    ```json JSON theme={null}
    {
    	"event":{
    		"id":"76376d80-29e4-4aaf-8295-c12f111cf5eb",
    		"type":"genius_workflow_run.started",
    		"issued_at":"2022-12-19T08:04:55.249-08:00"
    	},
    	"data":{
    		"id":"ff3021be-6ac2-4253-afbe-ae866c0c75a3",
    		"kind":"incident",
    		"status":"started",
    		"status_message": null,
    		"user_id":3186,
    		"genius_workflow_id":"a1b76e56-e1ab-4b36-856f-b6481251c698",		    
            "genius_workflow_name":"Send Email when incident starts",		 
            "queued_at":"2022-12-19T08:04:55.196-08:00",
    		"started_at":"2022-12-19T08:04:55.220-08:00",
    		"completed_at":null,
    		"failed_at":null,
    		"canceled_at":null,
    		"triggered_by":"user",
    		"status":"started",
    		"created_at":"2022-12-19T08:04:55.196-08:00",
    		"updated_at":"2022-12-19T08:04:55.226-08:00",
    		"incident_id":"5c80f5a1-9389-4970-bb49-8268acf2954f",
    		"incident_action_item_id":null,
    	    "incident_post_mortem_id":null,
    		"alert_id":null,
    		"pulse_id":null
    	}
    }
    ```
  </Tab>

  <Tab title="genius_workflow_run.completed">
    ```json JSON theme={null}
    {
    	"event":{
    		"id":"ae55dd1a-9bde-4a98-bd42-61df1e8dd80f",
    		"type":"genius_workflow_run.completed",
    		"issued_at":"2022-12-19T08:06:35.911-08:00"
    	},
    	"data":{
    		"id":"4cd6046c-9ed9-423e-8145-a1891f82ac57",
    		"kind":"incident",
    		"status":"completed",
    		"status_message": null,
    		"user_id":3186,
    		"genius_workflow_id":"678fbb8a-23bc-4fcf-8d46-b1833698b75b",
    		"genius_workflow_name":"Send Email when incident starts",
    		"queued_at":"2022-12-19T08:06:33.493-08:00",
    		"started_at":"2022-12-19T08:06:33.512-08:00",
    		"completed_at":"2022-12-19T08:06:35.887-08:00",
    		"failed_at":null,
    		"canceled_at":null,
    		"triggered_by":"user",
    		"created_at":"2022-12-19T08:06:33.493-08:00",
    		"updated_at":"2022-12-19T08:06:35.887-08:00",
    		"incident_id":"5c80f5a1-9389-4970-bb49-8268acf2954f",
    		"incident_action_item_id":null,
    		"incident_post_mortem_id":null,
    		"alert_id":null,
    		"pulse_id":null
    	}
    }
    ```
  </Tab>

  <Tab title="genius_workflow_run.failed">
    ```json JSON theme={null}
    {
    	"event":{
    		"id":"1562f78b-18fa-4d9f-a765-24e6dfba9794",
    		"type":"genius_workflow_run.failed",
    		"issued_at":"2022-12-19T08:08:18.521-08:00"
    	},
    	"data":{
    		"id":"3ceebcf1-e82f-4dfe-97da-69cd0678696d",
    		"kind":"incident",
    	    "status":"failed",
    		"status_message": null,
    		"user_id":3186,
    		"genius_workflow_id":"a1b76e56-e1ab-4b36-856f-b6481251c698",
    		"genius_workflow_name":"Send Email when incident starts",
    		"queued_at":"2022-12-19T08:08:17.890-08:00",
    		"started_at":"2022-12-19T08:08:17.908-08:00",
    		"completed_at":null,
    		"failed_at":"2022-12-19T08:08:18.498-08:00",
    		"canceled_at":null,
    		"triggered_by":"user",
    		"created_at":"2022-12-19T08:08:17.890-08:00",
    		"updated_at":"2022-12-19T08:08:18.498-08:00",
    		"incident_id":"5c80f5a1-9389-4970-bb49-8268acf2954f",
    		"incident_action_item_id":null,
    		"incident_post_mortem_id":null,
    		"alert_id":null,
    		"pulse_id":null
    	}
    }
    ```
  </Tab>

  <Tab title="genius_workflow_run.canceled">
    ```json JSON theme={null}
    {
    	"event":{
    		"id":"4b3d9e46-1a59-44a7-914d-b1758216b8d5",
    		"type":"genius_workflow_run.canceled",
    		"issued_at":"2022-12-19T11:09:16.508-05:00"
    	},
    	"data":{
    		"id":"e9269feb-1f2b-4d35-9181-f6842361ec62",		    
            "kind":"incident",
    	    "status":"canceled",
    		"status_message": null,
    		"user_id":3186,
    		"genius_workflow_id":"554f0a33-c05b-4352-87d4-1ec0332431bd",
    		"genius_workflow_name":"Send Email when incident starts",
    	    "queued_at":"2022-12-19T11:02:04.659-05:00",
    		"started_at":null,
    		"completed_at":null,
    		"failed_at":null,
    	    "canceled_at":"2022-12-19T11:09:16.480-05:00",
    		"triggered_by":"system",
    		"created_at":"2022-12-19T11:02:04.659-05:00",
    		"updated_at":"2022-12-19T11:09:16.480-05:00",
    	    "incident_id":"5c80f5a1-9389-4970-bb49-8268acf2954f",
    	    "incident_action_item_id":null,
    		"incident_post_mortem_id":null,
    	    "alert_id":null,
    		"pulse_id":null
    	}
    }
    ```
  </Tab>
</Tabs>

## incident.\*

```json JSON theme={null}
{
  "event": {
    "id": "9839c4ca-5e7b-416d-ad95-d09ae0c8eead",
    "type": "incident.created",
    "issued_at": "2022-11-27T19:44:33.633-08:00",
  },
  "data": {
    "id": "b7eed587-50e6-44fe-b010-7a2bb05d737a",
    "sequential_id": 19,
    "title": "Sparkling Frost",
    "slug": "sparkling-frost",
    "kind": "normal",
    "private": false,
    "summary": null,
    "status": "started",
    "url": "http://localhost:3000/account/incidents/19-sparkling-frost",
    "short_url": null,
    "mitigation_message": null,
    "resolution_message": null,
    "cancellation_message": null,
    "public_title": null,
    "zoom_meeting_id": null,
    "zoom_meeting_start_url": null,
    "zoom_meeting_join_url": null,
    "shortcut_story_id": null,
    "shortcut_story_url": null,
    "shortcut_task_id": null,
    "shortcut_task_url": null,
    "asana_task_id": null,
    "asana_task_url": null,
    "github_issue_id": null,
    "github_issue_url": null,
    "jira_issue_id": null,
    "jira_issue_url": null,
    "google_meeting_id": null,
    "google_meeting_url": null,
    "trello_card_id": null,
    "trello_card_url": null,
    "linear_issue_id": null,
    "linear_issue_url": null,
    "zendesk_ticket_id": null,
    "zendesk_ticket_url": null,
    "slack_channel_name": null,
    "slack_channel_id": null,
    "slack_channel_url": null,
    "slack_channel_short_url": null,
    "service_now_incident_id": null,
    "service_now_incident_key": null,
    "service_now_incident_url": null,
    "opsgenie_incident_id": null,
    "opsgenie_incident_url": null,
    "opsgenie_alert_id": null,
    "opsgenie_alert_url": null,
    "victor_ops_incident_id": null,
    "victor_ops_incident_url": null,
    "pagerduty_incident_id": null,
    "pagerduty_incident_url": null,
    "mattermost_channel_id": null,
    "mattermost_channel_name": null,
    "mattermost_channel_url": null,
    "confluence_page_id": null,
    "confluence_page_url": null,
    "quip_page_id": null,
    "quip_page_url": null,
    "airtable_base_key": null,
    "airtable_table_name": null,
    "airtable_record_id": null,
    "airtable_record_url": null,
    "google_drive_id": null,
    "google_drive_url": null,
    "datadog_notebook_id": null,
    "datadog_notebook_url": null,
    "freshservice_ticket_id": null,
    "freshservice_ticket_url": null,
    "freshservice_task_id": null,
    "freshservice_task_url": null,
    "started_at": "2022-11-27T19:36:00.000-08:00",
    "detected_at": null,
    "acknowledged_at": null,
    "mitigated_at": null,
    "resolved_at": null,
    "cancelled_at": null,
    "created_at": "2022-11-27T19:36:49.779-08:00",
    "updated_at": "2022-11-27T19:36:49.779-08:00",
    "labels": {
    },
    "severity": null,
    "user": {
      "id": 7,
      "name": "John Doe",
      "email": "demo@rootly.com",
      "full_name": "John Doe",
      "full_name_with_team": "[rootly.com] John Doe",
      "slack_id": null
    },
    "started_by": {
      "id": 7,
      "name": "John Doe",
      "email": "demo@rootly.com",
      "full_name": "John Doe",
      "full_name_with_team": "[rootly.com] John Doe",
      "slack_id": null
    },
    "mitigated_by": null,
    "resolved_by": null,
    "cancelled_by": null,
    "roles": [
      {
        "id": "e5c83728-78b9-495f-bdc5-55b3db047339"
      },
      {
        "id": "45602201-6cb9-4567-abd6-293096d880ef"
      }
    ],
    "environments": [

    ],
    "incident_types": [

    ],
    "services": [

    ],
    "functionalities": [

    ],
    "groups": [

    ],
    "events": [
      {
        "id": "01608451-5926-41ea-88b0-5af2f3cf5f79",
        "event": "John Doe created this incident",
        "event_raw": "John Doe created this incident",
        "kind": "event",
        "source": "web",
        "visibility": "external",
        "occurred_at": "2022-11-27T19:36:49.779-08:00",
        "created_at": "2022-11-27T19:36:49.779-08:00",
        "updated_at": "2022-11-27T19:36:49.884-08:00"
      },
      {
        "id": "42a1a95d-5ae2-4b74-a8dd-af675311769a",
        "event": "Started date has been set to <span class=\"badge badge-info-inverted\">November 27  7:36 PM PST</span>",
        "event_raw": "Started date has been set to November 27 7:36 PM PST",
        "kind": "trail",
        "source": "web",
        "visibility": "internal",
        "occurred_at": "2022-11-27T19:36:49.955-08:00",
        "created_at": "2022-11-27T19:36:49.955-08:00",
        "updated_at": "2022-11-27T19:36:49.955-08:00"
      }
    ],
    "action_items": [
      {
        "id": "a3121c52-39a8-4ba4-aef4-e33e6c6bcbdc",
        "incident_id": "b7eed587-50e6-44fe-b010-7a2bb05d737a",
        "description": null,
        "summary": "Tasks can be customized in Rootly",
        "kind": "task",
        "priority": "medium",
        "status": "open",
        "due_date": null,
        "jira_issue_id": null,
        "jira_issue_url": null,
        "asana_task_id": null,
        "asana_task_url": null,
        "github_issue_id": null,
        "github_issue_url": null,
        "shortcut_story_id": null,
        "shortcut_story_url": null,
        "shortcut_task_id": null,
        "shortcut_task_url": null,
        "trello_card_id": null,
        "trello_card_url": null,
        "linear_issue_id": null,
        "linear_issue_url": null,
        "zendesk_ticket_id": null,
        "zendesk_ticket_url": null,
        "airtable_base_key": null,
        "airtable_table_name": null,
        "airtable_record_id": null,
        "airtable_record_url": null,
        "freshservice_ticket_id": null,
        "freshservice_ticket_url": null,
        "freshservice_task_id": null,
        "freshservice_task_url": null,
        "created_at": "2022-11-27T19:15:07.651-08:00",
        "updated_at": "2022-11-27T19:15:07.651-08:00"
      },
      {
        "id": "70ef7704-aecb-401a-833d-edaf8aaa9d86",
        "incident_id": "b7eed587-50e6-44fe-b010-7a2bb05d737a",
        "description": null,
        "summary": "Update `/incident summary`",
        "kind": "task",
        "priority": "medium",
        "status": "open",
        "due_date": null,
        "jira_issue_id": null,
        "jira_issue_url": null,
        "asana_task_id": null,
        "asana_task_url": null,
        "github_issue_id": null,
        "github_issue_url": null,
        "shortcut_story_id": null,
        "shortcut_story_url": null,
        "shortcut_task_id": null,
        "shortcut_task_url": null,
        "trello_card_id": null,
        "trello_card_url": null,
        "linear_issue_id": null,
        "linear_issue_url": null,
        "zendesk_ticket_id": null,
        "zendesk_ticket_url": null,
        "airtable_base_key": null,
        "airtable_table_name": null,
        "airtable_record_id": null,
        "airtable_record_url": null,
        "freshservice_ticket_id": null,
        "freshservice_ticket_url": null,
        "freshservice_task_id": null,
        "freshservice_task_url": null,
        "created_at": "2022-11-27T19:15:07.626-08:00",
        "updated_at": "2022-11-27T19:15:07.651-08:00"
      },
      {
        "id": "368921f4-419c-4df3-92a2-006c3882dc70",
        "incident_id": "b7eed587-50e6-44fe-b010-7a2bb05d737a",
        "description": null,
        "summary": "Ensure roles are assigned",
        "kind": "task",
        "priority": "medium",
        "status": "open",
        "due_date": null,
        "jira_issue_id": null,
        "jira_issue_url": null,
        "asana_task_id": null,
        "asana_task_url": null,
        "github_issue_id": null,
        "github_issue_url": null,
        "shortcut_story_id": null,
        "shortcut_story_url": null,
        "shortcut_task_id": null,
        "shortcut_task_url": null,
        "trello_card_id": null,
        "trello_card_url": null,
        "linear_issue_id": null,
        "linear_issue_url": null,
        "zendesk_ticket_id": null,
        "zendesk_ticket_url": null,
        "airtable_base_key": null,
        "airtable_table_name": null,
        "airtable_record_id": null,
        "airtable_record_url": null,
        "freshservice_ticket_id": null,
        "freshservice_ticket_url": null,
        "freshservice_task_id": null,
        "freshservice_task_url": null,
        "created_at": "2022-11-27T19:15:07.601-08:00",
        "updated_at": "2022-11-27T19:15:07.651-08:00"
      }
    ],
    "form_field_selections": [

    ],
    "feedbacks": [

    ],
    "incident_post_mortem": null
  }
}
```

## incident\_post\_mortem.\*

```json JSON theme={null}
{
  "event": {
    "id": "9839c4ca-5e7b-416d-ad95-d09ae0c8eead",
    "type": "incident_post_mortem.created",
    "issued_at": "2022-11-27T19:36:00.000-08:00",
  },
  "data": {
    "id": "2c7497e5-5d15-4fa4-aeac-cac063aafe19",
    "incident_id": "b7eed587-50e6-44fe-b010-7a2bb05d737a",
    "title": "Sparkling Frost",
    "status": "draft",
    "url": "http://rootly.com/account/incidents/19-sparkling-frost/postmortem_url",
    "short_url": null,
    "content": "<h1>{{incident.created_at | date: \"%Y-%m-%d\"}} - {{incident.title}}</h1>\n<h1><strong>Leadup</strong></h1>\n<br><span style=\"color: #7a869a\">Describe the circumstances that led to this incident</span><br><br>\n<h1><strong>Fault</strong></h1>\n<br><span style=\"color: #7a869a\">Describe what failed to work as expected</span><br><br>\n<h1><strong>Detection</strong></h1>\n<br><span style=\"color: #7a869a\">Describe how the incident was detected</span><br><br>\n<h1><strong>Root causes</strong></h1>\n<br><span style=\"color: #7a869a\">Run a 5-whys analysis to understand the true causes of the incident</span><br><br>\n<h1><strong>Mitigation and resolution</strong></h1>\n<br><span style=\"color: #7a869a\">What steps did you take to resolve this incident?</span><br><br>\n<h1><strong>Lessons learnt</strong></h1>\n<br><span style=\"color: #7a869a\">What went well? What could have gone better? What else did you learn?</span><br><br>",
    "published_at": null,
    "started_at": "2022-11-27T19:36:00.000-08:00",
    "mitigated_at": "2022-11-27T19:44:32.156-08:00",
    "resolved_at": "2022-11-27T19:44:32.156-08:00",
    "cancelled_at": null,
    "show_timeline": true,
    "show_timeline_starred_only": false,
    "show_timeline_genius": true,
    "show_timeline_trail": true,
    "show_timeline_tasks": true,
    "show_timeline_action_items": true,
    "show_functionalities_impacted": true,
    "show_services_impacted": true,
    "show_groups_impacted": true,
    "show_action_items": true,
    "created_at": "2022-11-27T19:36:49.779-08:00",
    "updated_at": "2022-11-27T19:44:32.177-08:00"
  }
}
```

## pulse.\*

```json JSON theme={null}
{
  "event": {
    "id": "9839c4ca-5e7b-416d-ad95-d09ae0c8eead",
    "type": "pulse.created",
    "issued_at": "2022-11-27T19:15:30.995-08:00",
  },
  "data": {
    "id": "aa1cab03-00e7-4578-b1ae-72ad9ae417c6",
    "team_id": 1,
    "pulse_trail_id": "b59bfcb7-89ed-4641-b288-5ce1bb3dd801",
    "summary": "Deployed to Kubernetes",
    "labels": [
      {
        "key": "label1",
        "value": "value1"
      },
      {
        "key": "label2",
        "value": "value2"
      }
    ],
    "data": {
      "hello": "world"
    },
    "external_id": null,
    "started_at": "2022-11-27T19:15:30.995-08:00",
    "ended_at": null,
    "deleted_at": null,
    "created_at": "2022-11-27T19:15:30.995-08:00",
    "updated_at": "2022-11-27T19:15:30.995-08:00",
    "webhook_type": null,
    "webhook_id": null,
    "webhook_idempotency_key": null,
    "external_url": null,
    "source": "k8s",
    "refs": [
      {
        "key": "image",
        "value": "registry.rootly.com/rootly/my-service:cd6214"
      }
    ]
  }
}
```


Built with [Mintlify](https://mintlify.com).