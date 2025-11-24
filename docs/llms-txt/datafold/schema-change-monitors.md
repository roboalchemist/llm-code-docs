# Source: https://docs.datafold.com/data-monitoring/monitors/schema-change-monitors.md

# Schema Change Monitors

> Schema Change monitors notify you when a table’s schema changes, such as when columns are added, removed, or data types are modified.

<Note>
  **INFO**

  Please contact [support@datafold.com](mailto:support@datafold.com) if you'd like to enable this feature for your organization.
</Note>

Schema change monitors alert you when a table’s schema changes in any of the following ways:

* Column added
* Column removed
* Data type changed

## Create a Schema Change monitor

There are two ways to create a Schema Change monitor:

1. Open the **Monitors** page, select **Create new monitor**, and then choose **Schema Change**.
2. Clone an existing Schema Change monitor by clicking **Actions** and then **Clone**. This will pre-fill the form with the existing monitor configuration.

## Set up your monitor

To set up a Schema Change monitor, simply select your data connection and the table you wish to monitor for changes.

## Add a schedule

You can choose to run your monitor daily, hourly, or even input a cron expression for more complex scheduling:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=bba568fdc3049b5cf68cf1b8786eb97e" data-og-width="1184" width="1184" data-og-height="304" height="304" data-path="images/monitors/schedule.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=23963e43888a23fa582b2ca0acb14278 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=be1bd4311a6edba905d6b0ac05ed9e40 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=84c1074e12d76ed7e1bb58a5b226f9ab 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5a23b013dfdd0808925417e2890e5d53 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a46bd2d3dbeeecf2f5371f6549646331 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a1003bb0bc5401af01a645062f9eb279 2500w" />
</Frame>

## Add notifications

Receive notifications via Slack or email when at least one record fails your test:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=87bfb30d98bd8da832bcdd3192d9c559" data-og-width="1576" width="1576" data-og-height="578" height="578" data-path="images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f7d5d2b6c2819122c487d7a25a69ff00 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9187a82760eb2bf34b8567640887793e 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=aee0c94c2479f59f69ef009adc46bb72 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8c6ee9ee72739450f84e7a1016f412bd 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=4059e04a333762886bff02f601f68fcd 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=da1b7bebb6c322791e71a98bce66a2cf 2500w" />
</Frame>

## FAQ

<Accordion title="Don't data diffs detect schema changes too?">
  Yes, but in a different context. While data diffs report on schema differences *between two tables at the same time* (unless you’re using the time travel feature), data diff monitors alert you to schema changes for the *same table over time*.
</Accordion>

## Need help?

If you have any questions about how to use Schema Change monitors, please reach out to our team via Slack, in-app chat, or email us at [support@datafold.com](mailto:support@datafold.com).
