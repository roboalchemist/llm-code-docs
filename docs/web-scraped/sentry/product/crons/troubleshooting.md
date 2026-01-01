---
---
title: Troubleshooting
description: "Troubleshoot common issues with cron monitoring."
---

All monitors are automatically deactivated at the start of a new billing period if there's not enough [on-demand spend](/pricing/#on-demand-capacity) to cover all active monitors. Monitors can be manually activated based on on-demand availability. See [Manage Your Cron Monitors](/pricing/quotas/manage-cron-monitors) for more details.

If your monitor environment has been consistently broken for 14 days or more (with only missed, timed out, or failed check-ins), we will automatically mark it as broken and notify you of this escalated failure state via email.

If the monitor environment continues to be broken after an additional 14 days, we will automatically mute it to stop it from generating additional noise through notifications or issue events.

**Who Receives the Notification:**

- If the monitor has an owner who is a user, that user will receive the email
- If the monitor has an owner who is a team, all team members will receive the email
- If the monitor has no owner, everyone in the project team will receive the email

**Important Notes:**

- You can disable these notifications in your [personal notification settings](/product/alerts/notifications/notification-settings/)
- Muting a monitor does **not** stop billing. You will continue to be charged for muted monitors. To stop billing, you must deactivate or delete the monitor. See [Manage Your Cron Monitors](/pricing/quotas/manage-cron-monitors) for more details.

You may not have [linked errors to your monitor](/product/crons/getting-started/http/#connecting-errors-to-cron-monitors).

You may not have [set up alerts for your monitor](/product/crons/getting-started/http/#alerts).

Our current data retention policy is 90 days.

Currently, we only support crontab expressions with five fields.

