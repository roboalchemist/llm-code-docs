# Source: https://developers.activecampaign.com/webhooks.md

# Source: https://developers.activecampaign.com/reference/webhooks.md

# Webhooks

> 📘 Looking for email webhooks?
>
> Postmark can notify your application when an event related to the transactional email occurs. Inbound webhook even provides a simple way to receive and process emails. Learn more about [Postmark Webhooks →](https://postmarkapp.com/developer/webhooks/webhooks-overview?utm_source=activecampaign\&utm_medium=referral\&utm_campaign=ac-api-docs)

Webhooks provide the ability to receive real-time data updates about your various ActiveCampaign events.

You may choose to receive data based on certain actions (contact subscribes, contact unsubscribes, campaign opens, deal adds, SMS sends, etc..) and have applicable data sent to a URL of your choice. You can then use your own custom code to read, save, and do whatever you want with that data. This is a powerful option that allows you to keep all of your data in sync and opens up various integration options.

With every webhook you create, you can choose when it should actually fire. Perhaps you only want to receive data when a contact is added from the API. You can simply specify `subscribe` as the event and `api` as the source when you create your webhook. You can specify multiple events and sources for each webhook if you wish. All event and source options are listed below.

We guarantee **at least once delivery** on webhooks. In some rare cases, you may receive a webhook event more than once, so it’s important to create an idempotent system. [see link for example](https://postmarkapp.com/blog/why-idempotency-is-important).

Webhooks are never retried.

Webhook payload fields are listed in this document: [webhook payloads](https://developers.activecampaign.com/page/webhooks).

## Events

| Event                 | Description               |
| :-------------------- | :------------------------ |
| `forward`             | Campaign forwarded        |
| `open`                | Campaign opened           |
| `share`               | Campaign shared           |
| `sent`                | Campaign starts sending\* |
| `subscribe`           | Contact added             |
| `subscriber_note`     | Contact note added        |
| `contact_tag_added`   | Contact tag added         |
| `contact_tag_removed` | Contact tag removed       |
| `unsubscribe`         | Contact unsubscription    |
| `update`              | Contact updated           |
| `deal_add`            | Deal added                |
| `deal_note_add`       | Deal note added           |
| `deal_pipeline_add`   | Deal pipeline added       |
| `deal_stage_add`      | Deal stage added          |
| `deal_task_add`       | Deal task added           |
| `deal_task_complete`  | Deal task completed       |
| `deal_tasktype_add`   | Deal task type added      |
| `deal_update`         | Deal updated              |
| `bounce`              | Email bounces             |
| `reply`               | Email replies             |
| `click`               | Link clicked              |
| `list_add`            | List added                |
| `sms_reply`           | SMS reply                 |
| `sms_sent`            | SMS sent                  |
| `sms_unsub`           | SMS unsubscribe           |

## Sources

| Source   | Description                                              |
| :------- | :------------------------------------------------------- |
| `public` | Run the hooks when a contact triggers the action         |
| `admin`  | Run the hooks when any user triggers the action          |
| `api`    | Run the hooks when an API call triggers the action       |
| `system` | Run the hooks when automated systems triggers the action |

> 📘 \*- 'Automation Driven Campaigns' will trigger webhooks when "By system processes" is selected for the webhook setting 'Initialize From (Source)'
>
> example:
>
> <Image align="center" src="https://files.readme.io/19d0f83-by_system_process.jpeg" />