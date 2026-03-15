# Source: https://docs.firehydrant.com/docs/auto-alerting-services.md

# Auto-Alerting Services and Teams

FireHydrant allows you to automatically page teams when a Service or Functionality is impacted in an incident. This enables engineers to focus on remediation while knowing that the right service owners are being notified about an incident.

## Enable Auto-Alerting

1. **Confirm your alerting provider is configured on FireHydrant**. This feature is currently supported for the following integrations:
   1. [Signals (FireHydrant)](https://docs.firehydrant.com/docs/signals-introduction)
   2. [Opsgenie](https://docs.firehydrant.com/docs/opsgenie-integration)
   3. [PagerDuty](https://docs.firehydrant.com/docs/pagerduty-integration)
   4. [Splunk On-Call (VictorOps)](https://docs.firehydrant.com/docs/splunk-on-call-victorops-integration)

2. **If using FireHydrant Signals, ensure your teams have default Escalation Policies and set them as responders to the service.**
   1. Learn about configuring [Escalation Policies](https://docs.firehydrant.com/docs/signals-escalation-policies) for Teams in FireHydrant and then [associate those Teams](https://docs.firehydrant.com/docs/associating-teams) as Responders for a Service or Functionality. Skip to step 4 after this.

3. **If using an external Alerting provider, link your external services to FireHydrant**.
   1. For FireHydrant to know which external services/escalation policies to page, you or[must import and/or link those external services](https://docs.firehydrant.com/docs/import-and-link-components) to FireHydrant Services or Functionalities.

> 📘 Note:
>
> If using Splunk On-Call (VictorOps), you'll want to create [alert routing keys](https://help.victorops.com/knowledge-base/routing-keys/) in VictorOps for each Service in FireHydrant you'd like to link to an Escalation Policy.

4. **Turn on Automatic Alerting**.
   1. On the page for each Service or Functionality you'd like to Auto-Alert, click **Edit** in the top right corner.
   2. Scroll down to the "Alerting" section and check the box for "Automatically alert if added to an incident."

<Image alt="Automatic alerting setting for a service/functionality" align="center" width="650px" src="https://files.readme.io/fce2111-CleanShot_2024-04-24_at_16.28.442x.png">
  Automatic alerting setting for a service/functionality
</Image>

4. Scroll down and **Save edits**.

## Using Auto-Alerting

After configuring the setting above, you only need to mark a service as impacted in an incident. FireHydrant will then send out a page to your alerting provider via the linked service and whichever Escalation Policy is assigned as the default for that service. The FireHydrant Incident Timeline also reflects that an alert was generated via that service.

This can happen anytime during an incident, including at declaration and mid-incident.

<Image alt="Example timeline event/Slack message when an alert is created via automatic service paging" align="center" width="650px" src="https://files.readme.io/e35a861-image.png">
  Example timeline event/Slack message when an alert is created via automatic service paging
</Image>

## Next Steps

* See how you can also [manually look up and page responders](https://docs.firehydrant.com/docs/on-call-paging-and-lookup) during an incident
* Look at associating [Change Events](https://docs.firehydrant.com/docs/change-events) with services in FireHydrant to make problem identification faster and easier during incidents
* Check out some of the [Impact Statistics](https://docs.firehydrant.com/docs/analytics-impact-statistics) and other [Analytics](https://docs.firehydrant.com/docs/analytics-basics) FireHydrant provides based on marking components impacted on incidents