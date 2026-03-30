# Source: https://buildkite.com/docs/pipelines/integrations/notifications/pagerduty.md

# PagerDuty

The [PagerDuty](http://pagerduty.com/) integration in Buildkite can send [change events](https://support.pagerduty.com/docs/change-events) to PagerDuty when your builds finish.

<div style="max-width: 1101px"><div class="responsive-image-container"><img alt="Screenshot of the recent events in PagerDuty" src="/docs/assets/overview-C5qlng9f.png" /></div></div>

## Generating a PagerDuty integration API key

Before using the integration you'll need to generate a PagerDuty Integration API Key.

In [PagerDuty](http://pagerduty.com/), go to the **Service Directory**:

<div style="max-width: 427px"><div class="responsive-image-container"><img alt="Screenshot of the Service Directory link in the menu" src="/docs/assets/menu-JnJ2cHlF.png" /></div></div>

Then choose the service you'd like Buildkite to send change events to:

<div style="max-width: 1421px"><div class="responsive-image-container"><img alt="Screenshot of the chosen service in the Service Directory" src="/docs/assets/service-item-hKY7WlRw.png" /></div></div>

Navigate to the **Integrations** tab and choose **Add a new integration**:

<div style="max-width: 1044px"><div class="responsive-image-container"><img alt="Screenshot of the Add Integration button in PagerDuty" src="/docs/assets/add-integration-D8ySwcQ8.png" /></div></div>

Under **Integration Name**, choose a memorable name for this integration. A good example could be the name of the Buildkite pipeline you intend to add this integration to.

For **Integration Type**, choose **Buildkite**.

Once you've filled out this form, select **Add Integration**.

Copy the **Integration Key** from your Integrations list and use it in [Sending change events from your pipeline](#sending-change-events-from-your-pipeline).

<div style="max-width: 1131px"><div class="responsive-image-container"><img alt="Screenshot of the Buildkite integration in PagerDuty" src="/docs/assets/integration-with-key-eAPGOngl.png" /></div></div>

## Sending change events from your pipeline

By default, after you've added an Integration API Key, Buildkite will send PagerDuty a Change Event every build regardless of whether the build passed or failed.

Add the PagerDuty [Integration API Key](#generating-a-pagerduty-integration-api-key) to the [`notify` attribute](/docs/pipelines/configure/notifications) of your build configuration.

Make sure that you're using a secure secrets management solution to handle the PagerDuty Integration key, and never commit it in plaintext to source control in a YAML file. See [Managing pipeline secrets](/docs/pipelines/security/secrets/managing) for more information on safely handling secrets within your infrastructure.

```yaml
steps:
  - command: "tests.sh"
  - wait
  - command: "deploy.sh"

notify:
  - pagerduty_change_event: "${PAGER_DUTY_API_KEY}"
```

{: codeblock-file="pipeline.yml"}

<div style="max-width: 1152px"><div class="responsive-image-container"><img alt="Screenshot of a Change Event inside PagerDuty sent from Buildkite" src="/docs/assets/change-event-HSuJf6yq.png" /></div></div>

To send change events only when the build passes, add a [condition](/docs/pipelines/configure/conditionals) to your build configuration:

```yaml
notify:
  - pagerduty_change_event: "${PAGER_DUTY_API_KEY}"
    if: "build.state == 'passed'"
```

## Support

For those of you coming from [the PagerDuty website](https://pagerduty.com) looking for assistance on this integration please reach out to us at [support@buildkite.com](mailto:support@buildkite.com?subject=PagerDuty%20Change%20Events%20Integration).
