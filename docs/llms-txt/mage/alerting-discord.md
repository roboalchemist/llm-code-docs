# Source: https://docs.mage.ai/observability/alerting/alerting-discord.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Alerting status updates in Discord

> Get status updates in your Discord channel.

export const ProOnly = ({button = 'Get started for free', description = 'Try our fully managed solution to access this advanced feature.', source = 'documentation', title = 'Only in Mage Pro.'}) => <a href={`https://cloud.mage.ai/sign-up?source=${source}`} className="block my-4 px-5 py-4 overflow-hidden rounded-xl flex gap-3 border border-emerald-500/20 bg-emerald-50/50 dark:border-emerald-500/30 dark:bg-emerald-500/10" target="_blank">
    <div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%'
}}>
      <div className="text-sm prose min-w-0 text-emerald-900 dark:text-emerald-200" style={{
  flex: 1
}}>
        {title}
        <p className="normal">{description}</p>
      </div>

      <div> </div>

      <div>
        <ProButton label={button} href={`https://cloud.mage.ai/sign-up?source=${source}`} />
      </div>
    </div>
  </a>;

export const ProButton = ({href, label = 'Get started with Mage Pro for free', source = 'documentation'}) => <div style={{
  height: 32,
  position: 'relative'
}}>
    <a target="_blank" className="group px-4 py-1.5 relative inline-flex items-center text-sm font-medium rounded-full" href={href ?? `https://cloud.mage.ai/sign-up?source=${source}`}>
      <span className="absolute inset-0 bg-primary-dark dark:bg-primary-light/10 border-primary-light/30 rounded-full dark:border group-hover:opacity-[0.9] dark:group-hover:border-primary-light/60">
      </span>

      <div className="mr-0.5 space-x-2.5 flex items-center">
        <span class="z-10 text-white dark:text-primary-light">
          {label}
        </span>

        <svg width="3" height="24" viewBox="0 -9 3 24" class="h-5 rotate-0 overflow-visible text-white/90 dark:text-primary-light">
          <path d="M0 0L3 3L0 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path>
        </svg>
      </div>
    </a>
  </div>;

<img alt="Discord" src="https://cdn-icons-png.flaticon.com/512/2111/2111370.png" width="300" />

## Overview of steps

1. Set up webhooks for Discord
2. Update Mage project settings

***

## Set up webhooks for Discord

Follow these
[instructions on Discord](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
to setup incoming webhooks for your workspace.

***

## Update Mage project settings

Once you’ve set up webhooks for Discord, you should have a webhook URL that Discord
provides.

Here is an example webhook (yours may vary):

```
https://discordapp.com/api/webhooks/XXX3514XXXXX/MHhahaduwa183-ccgfxcgv88kladJkjBJKB78CHCfds
```

Follow these steps to add that webhook URL to your project settings:

1. Open the Mage tool in your browser (e.g. [http://localhost:6789/](http://localhost:6789/)).

2. Open a pipeline and start editing it (e.g.
   [http://localhost:6789/pipelines/example\_pipeline/edit](http://localhost:6789/pipelines/example_pipeline/edit)).

3. In your left sidebar in the file browser, scroll all the way down and click
   on a file named `metadata.yaml`.

4. In the `metadata.yaml` file, add a section with the following
   configuration or update the existing `notification_config` section:

   ```yaml  theme={"system"}
   notification_config:
     alert_on:
       - trigger_failure
       - trigger_passed_sla
   ```

   If you omit the `alert_on` section it will default to `trigger_failure` and `trigger_passed_sla`.

   Options:

   * `trigger_failure`: alert when a run of a trigger fails
   * `trigger_success`: alert when a run of a trigger succeeds
   * `trigger_passed_sla`: alert when a SLA is missed.
     * In this context, SLA (Service Level Agreement) is an expected amount of time for the pipeline to complete.
     * If the pipeline runs *longer* than the SLA, an alert will be sent.

5. In the `metadata.yaml` file, add the following values:

   ```yaml  theme={"system"}
   notification_config:
     alert_on:
       ...
     discord_config:
       webhook_url: ...
   ```

   Change the `webhook_url` value to be the webhook URL you created from Discord.

## Customize message templates

You can customize message templates in `notification_config`. Here is an example config:

```yaml  theme={"system"}
notification_config:
  alert_on:
    ...
  discord_config:
    ...
  message_templates:
    failure:
      title: 'Failed to execute pipeline {pipeline_uuid} at {execution_time}'
      summary: >
        Failed to execute pipeline {pipeline_run_url}.
        Pipeline uuid: {pipeline_uuid}. Trigger name: {pipeline_schedule_name}.
        Test custom message.
    success:
      title: ...
      summary: ...
    passed_sla:
      title: ...
      summary: ...
```

You can customize the message template for `success`, `failure`, `passed_sla` scenarios. For each message template,
you can specify the sentence on `summary` and the `title`.

To interpolate variables in the message template, you can use `{variable_name}` syntax.
Here are the supported variables:

1. `execution_time`
2. `pipeline_run_url`
3. `pipeline_schedule_id`
4. `pipeline_schedule_name`
5. `pipeline_schedule_description`
6. `pipeline_uuid`
7. `error`
   * available only for the `failure` message template
8. `stacktrace`
   * available only for the `failure` message template

> **Note**: For `pipeline_run_url`, the default host is `http://localhost:6789`. You can specify `MAGE_PUBLIC_HOST` to be
> the host url you want to use in the notification messages.

### 🚀 Pro Only: Interpolate Mage Variables in Message Templates

<ProOnly source="notification" />

If you're using **Mage Pro**, you can interpolate environment variables and other [Mage variables](/development/variables/referencing-variables#accessing-variables-in-mage) directly in your Discord message templates using the familiar Jinja-like syntax:

```yaml  theme={"system"}
notification_config:
  message_templates:
    failure:
      details: >
        Failed at {{ env_var('ENVIRONMENT') }} environment.
        Pipeline run: {pipeline_run_url}.
```

In addition to the variables mentioned above (e.g. `execution_time`, `pipeline_uuid`, etc), you can also use the
following in your message templates in Mage Pro:

1. `start_time`
2. `end_time`
3. `duration` (in seconds)
4. `env` (this gets the value stored in the `ENV` environment variable)

This makes your Discord notifications more dynamic and context-aware — ideal for multi-environment deployments and advanced workflows.

***

## What next?

Whenever a pipeline run is successfully completed or fails, a Discord Channel message will
appear in the channel you configured the webhook URL for.

Here is an example of what that message could look like:

|                                                                                        |
| -------------------------------------------------------------------------------------- |
| ![Discord](https://mage-ai.github.io/assets/third-party/discord-message-run-alert.jpg) |


Built with [Mintlify](https://mintlify.com).