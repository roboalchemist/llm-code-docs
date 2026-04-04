# Source: https://docs.mage.ai/observability/alerting/alerting-zendesk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Alerting status updates in Zendesk

> Create Zendesk tickets from Mage pipeline events to track incidents and resolution.

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

<img alt="Zendesk" src="https://cdn.simpleicons.org/zendesk" width="300" />

<ProOnly source="notification" />

## Overview of steps

1. Create an API token in Zendesk
2. Update Mage project settings with Zendesk config
3. Customize ticket templates with dynamic variables (Pro only)

***

## Create an API token in Zendesk

To allow Mage to create tickets in Zendesk, you need to set up an API token:

1. Log in to Zendesk as an **admin**.
2. Go to **Admin Center** → **Apps and integrations** → **Zendesk API**.
3. Enable **Token Access**.
4. Click **Add API token**.
5. Enter a description (e.g., "Mage Alerts") and copy the generated token.
   > **Note:** This token will only be shown once. Store it securely.
6. Identify your Zendesk **subdomain** (e.g., for `https://acme.zendesk.com` the subdomain is `acme`).
7. Ensure the account you use (email) has **agent** or **admin** permissions.

***

## Update Mage project settings

Once you have your subdomain, email, and API token, add them to your project settings.

Here’s an example `zendesk_config` (add under `notification_config` in `metadata.yaml`):

```yaml  theme={"system"}
notification_config:
  alert_on:
    - trigger_failure
    - trigger_passed_sla
  zendesk_config:
    subdomain: your-domain
    email: bot@example.com
    api_token: YOUR_ZENDESK_API_TOKEN
    group_id: "1234567890"          # optional: numeric group ID
    assignee_id: "9876543210"       # optional: numeric agent ID
    priority: high                  # optional: low | normal | high | urgent
    status: new                     # optional: new | open | pending | hold
    tags: mage,alert,pipeline       # optional: comma-separated tags
```

If you omit the `alert_on` section, it will default to `trigger_failure` and `trigger_passed_sla`.

Options for `alert_on`:

* `trigger_failure`: alert when a run of a trigger fails
* `trigger_success`: alert when a run of a trigger succeeds
* `trigger_passed_sla`: alert when a SLA is missed.
  * SLA (Service Level Agreement) is an expected amount of time for the pipeline to complete.
  * If the pipeline runs *longer* than the SLA, an alert will be sent.

***

## Customize ticket templates

You can customize ticket templates in `notification_config` just like Slack message templates:

```yaml  theme={"system"}
notification_config:
  alert_on:
    ...
  zendesk_config:
    ...
  message_templates:
    failure:
      details: >
        Pipeline {pipeline_uuid} failed.
        See logs: {pipeline_run_url}.
    success:
      details: ...
    passed_sla:
      details: ...
```

You can customize templates for `success`, `failure`, and `passed_sla` scenarios.\
For each template:

* If you specify `summary`, the ticket subject will be your summary, and `details` will be used as the body.
* If you specify only `details`, it will be used as the ticket body directly.

**Supported variables:**

1. `execution_time`
2. `pipeline_run_url`
3. `pipeline_schedule_id`
4. `pipeline_schedule_name`
5. `pipeline_schedule_description`
6. `pipeline_uuid`
7. `error` (failure only)
8. `stacktrace` (failure only)

***

### 🚀 Pro Only: Interpolate Mage Variables in Ticket Templates

In **Mage Pro**, you can interpolate environment variables and other [Mage variables](/development/variables/referencing-variables#accessing-variables-in-mage) in your Zendesk ticket templates using Jinja-like syntax:

```yaml  theme={"system"}
notification_config:
  message_templates:
    failure:
      details: >
        Failed at {{ env_var('ENVIRONMENT') }} environment.
        Run details: {pipeline_run_url}.
```

Additional variables available in Mage Pro:

1. `start_time`
2. `end_time`
3. `duration` (in seconds)
4. `env` (value of the `ENV` environment variable)

***

## What next?

Whenever a pipeline run completes or fails, Mage will create a Zendesk ticket based on your configuration.\
You can route these tickets to specific groups or agents, tag them, and track resolution in Zendesk.

Example ticket subject/body:

|                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------- |
| **Subject:** Mage Notification: Failed to run Mage pipeline example\_pipeline                                                     |
| **Body:** Pipeline `example_pipeline` failed at 2025-08-13. View logs at: https\://mage\_url/pipelines/example\_pipeline/runs/123 |


Built with [Mintlify](https://mintlify.com).