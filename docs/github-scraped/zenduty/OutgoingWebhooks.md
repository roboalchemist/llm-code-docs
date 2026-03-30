---
id: OutgoingWebhooks
title: Outgoing Webhook
---

Zenduty supports webhooks to easily integrate external applications.

Outgoing webhooks in Zenduty is a method of sending incident notifications to an application through an HTTP POST request when the following activities happen:

1) Incident Triggered
2) Incident acknowledged
3) Incident Resolved

## Create an Outgoing webhook

1. Navigate to your service and within the integrations tab, click on "Add integration" under "Outgoing Integrations".

2. From the applications list, select **Outgoing Webhooks**. Click on Save.

3. Click on **congig** next to your new integration and navigate to the integration configuration page.

4. In the input box, add the URL to which you'd like to send the Webhook HTTP POST request.

5. Click on **Save** to save your webhook integration.

The payload sent by Zenduty will look like the payload below:

```
{
    "payload": {
        "event_type": "resolved",
        "incident": {
            "summary": "Linux 008 Free disk space is less than 20% on volume sdx-03",
            "incident_number": 217,
            "creation_date": "2020-05-21T19:42:16.372614Z",
            "status": 3,
            "unique_id": "vuwtGfyHf9JaN5vg5sEc4N",
            "title": "Free disk space is less than 20% on volume sdx-03",
            "incident_key": "C67SCMypoCyUWwLpbVSSy2",
            "service": {
                "name": "ZD Prod",
                "creation_date": "2019-11-26T22:01:17.582115Z",
                "summary": "",
                "description": "Zenduty main application",
                "unique_id": "e84d78d1-6484-4a99-b9f8-c23b6a4e86b0",
                "auto_resolve_timeout": 0,
                "created_by": "fe07dd6c-1f20-485e-bddb-c",
                "team_priority": "6beb47f132f54f98b013757d2e3eef6e",
                "task_template": "26c9f78141694c7980b87489b007c642",
                "acknowledgement_timeout": 0,
                "status": 1,
                "escalation_policy": "5ce8918ddfac4f00b95ab204dcedafc9",
                "team": "0b3332124a984dceb77e12cd02728b4b",
                "sla": "77bac19adeab4166bd9bd4dfe6301924",
                "collation_time": 0,
                "collation": 0
            },            
            "urgency": 1,
            "merged_with": null,
            "assigned_to": {
                "username": "fe07dd6c-1f20-485e-bddb-c",
                "first_name": "Dwight",
                "last_name": "Schrute",
                "email": "tya@gmail.com"
            },
            "resolved_date": "2020-05-28T16:46:46.020227Z",
            "acknowledged_date": "2020-05-25T11:18:55.112452Z",
            "context_window_start": "2020-05-21T19:12:16.372000Z",
            "context_window_end": "2020-05-21T19:42:16.372000Z"
        }
    }
}
```

There are three "event_type" values sent by Zenduty - "triggered", "acknowledged" aand "resolved".
