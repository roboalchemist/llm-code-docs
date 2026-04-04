# Source: https://docs.mage.ai/observability/alerting/alerting-email.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Alerting status updates in Email

> Get status updates sent to your email inbox.

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

<img alt="Email" src="https://yourreclaimedlife.com/wp-content/uploads/2018/12/email-marketing-without-permission.jpg" />

## Create notification\_config

In the root of your project’s folder (e.g. `default_repo/`), open the file
`metadata.yaml`.

> Project folder name
>
> If you initialized Mage using a different project name, then your root folder
> will be named differently. `default_repo` is the default project name if you
> didn’t customize it.

In the `default_repo/metadata.yaml` file, add a section with the following
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
* `trigger_passed_sla`: alert when a run of a trigger passes sla

## Configure email settings

In the `default_repo/metadata.yaml` file, add a section with the following
configuration or update the existing `notification_config` section:

```yaml  theme={"system"}
notification_config:
  alert_on:
    ...
  email_config:
    smtp_host: ...
    smtp_mail_from: ...
    smtp_user: ...
    smtp_password: ...
    to_emails:
      - someone_lucky@mage.ai
      - eng@mage.ai
```

Change the values for each key under the `email_config` section.

## Customize message templates

You can customize message templates in `notification_config`. Here is an example config:

```yaml  theme={"system"}
notification_config:
  alert_on:
    ...
  email_config:
    ...
  message_templates:
    failure:
      title: Failed to execute pipeline {pipeline_uuid} at {execution_time}
      details: >
        Failed to execute pipeline {pipeline_run_url}.
        Pipeline uuid: {pipeline_uuid}. Trigger name: {pipeline_schedule_name}.
        Test custom message.
    success:
      title: ...
      details: ...
    passed_sla:
      title: ...
      details: ...
```

You can customize the message template for `success`, `failure`, `passed_sla` scenarios. For each message template,
you can specify `title` and either `summary` or `details`.

* `title` is used in email subject
* If you specify the `summary`, the email body will be your `summary` + the url of the pipeline run page
* If you specify the `details`, the `details` will be used as your email body

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

If you're using **Mage Pro**, you can interpolate environment variables and other [Mage variables](/development/variables/referencing-variables#accessing-variables-in-mage) directly in your Email message templates using the familiar Jinja-like syntax:

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

This makes your Email notifications more dynamic and context-aware — ideal for multi-environment deployments and advanced workflows.

***

## What next?

Whenever a pipeline run is successfully completed or fails, an email will be
delivered to all the inboxes listed under `to_emails`.

Here is an example of what an email could look like:

|                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Successfully ran Pipeline `example_pipeline` with Trigger 79 `hourly_trigger` at execution time `2022-09-28 19:00:00`.<br />Open [http://localhost:6789/pipelines/example\_pipeline/triggers/79](http://localhost:6789/pipelines/example_pipeline/triggers/79) to check pipeline run results and logs. |


Built with [Mintlify](https://mintlify.com).