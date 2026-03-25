# Source: https://docs.envzero.com/guides/admin-guide/environments/drift-detection.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Detect Drift

> Set up automated drift detection in env zero to identify when cloud resources diverge from your IaC definitions

Managing Infrastructure as Code (IaC) comes with its own set of challenges, and one of the most significant is drift. Drift occurs when the actual state of your cloud resources deviates from the state defined in your code - whether due to manual changes, external automation tools, or other processes outside of your IaC pipeline.

Detecting and managing drift is critical to maintaining consistency, security, and compliance across your infrastructure. With env zero, you can proactively address this issue by setting up automated drift detection. env zero schedules deployment tasks that conclude with an analysis of the Terraform plan output, allowing you to identify and resolve drifts in real-time.

<Info>
  **Previous Support**

  Although drift detection has been a feature of env zero for a while, now we provide additional drift event notifications.
</Info>

If you would like to set up a drift detection on your environment and get notified on drift occurrences, you will need to follow these steps:

1. \*\* Schedule a drift detection job:\*\* In the environment **Settings** tab, under Drift Detection, make sure you add a cron expression based on the interval you would like to check the drift. For example, if you would like to check the drift twice a day at 10AM and at 7PM, enter `00 10,19 * * *`.

<Note>
  **Drift Detection Scheduling**

  Despite being able to configure any cron pattern for drift detection, the minimum interval is one day for Free and plans, and one hour for Enterprise plans.

  The scheduler runs once an hour, and controlling the exact minute of the run within the hour is not possible.
</Note>

<img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/changelogs/2025/02/ed1613488c4b718336e8f6d2797507de46a656090354cb88de6fe20cb9390be7-image.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=e456171c51f9991f63258e6230de45a2" alt="" width="2624" height="1220" data-path="images/changelogs/2025/02/ed1613488c4b718336e8f6d2797507de46a656090354cb88de6fe20cb9390be7-image.png" />

1. **Add Notification:** To get notified directly in Slack,Microsoft Teams, email, or Webhooks when a drift has been detected, set up notification targets and events on your project settings under [Notifications](/guides/integrations/notifications).\
   You can set the following types of events:
   * **Drift detected** - The remote resources have been changed.
   * **No drift detected** - The remote resources are synced with your infrastructure code.
   * **Drift failed** - The task has failed for some reason.

You can read more about notifications [here.](/guides/integrations/notifications)

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/27b370b-screen_shot_2022-03-08_at_15.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=2414dc2703fececb7f430a8766e99f0d" alt="" width="571" height="607" data-path="images/guides/admin-guide/environments/27b370b-screen_shot_2022-03-08_at_15.png" />

When a drift detection job is executed, you'll see its status under the Deployments tab :

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/0767af2-screen_shot_2022-03-08_at_15.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=2712486035b4c7061e8994f1d09ce815" alt="" width="1442" height="200" data-path="images/guides/admin-guide/environments/0767af2-screen_shot_2022-03-08_at_15.png" />When a drift is identified, or if the drift detection process encounters an issue, environment drift-status will shift to Drifted or Error, correspondingly.\
These statuses will be accompanied by an informative message that links to the related Drift Detection deployment logs.\
It's important to note that performing a new deployment on an environment with a drift will reset its status accordingly.

Following a drift occurrence:

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/272f0d356b622f83fd7f375bd2910bdb5d92b1c8ea752ec1473b52add7cb03c0-image.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=16b25c65ab12a2bf67ce5ef9c54149f2" alt="" width="2676" height="646" data-path="images/guides/admin-guide/environments/272f0d356b622f83fd7f375bd2910bdb5d92b1c8ea752ec1473b52add7cb03c0-image.png" />

Following an error during drift detection:

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/87ee291-image.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=5df25bebb8faa6293edd74a65c9682f3" alt="" width="1499" height="703" data-path="images/guides/admin-guide/environments/87ee291-image.png" />

### Understanding Drift Statuses

* `OK`: No drift has been detected; the environment's state matches the defined Infrastructure-as-Code (IaC) configuration
* `Error`: An error has occurred during the drift detection process
* `Drifted`: Drift has been detected; the environment's state differs from the IaC configuration
* `Never Run`: Drift detection has never been executed for this environment
* `Disabled`: Drift detection is disabled for this environment

# Drift Remediation

env zero offers both automatic and manual drift remediation options. With automatic drift remediation, you can configure env zero to apply the necessary changes to your cloud resources automatically, ensuring they stay aligned with your IaC configuration.

Read more about different ways to remediate drift in env zero  [here](/guides/admin-guide/environments/drift-detection/automatic-drift-remediation).

## Suggested Blog Content

[Terraform Modules Guide](https://www.env0.com/blog/terraform-modules)

[Terraform Plan Examples](https://www.env0.com/blog/terraform-plan)

[Managing Terraform Variable Hierarchy](https://www.env0.com/blog/managing-terraform-variable-hierarchy)

[Manage Terraform Remote State with a Remote Backend](https://www.env0.com/blog/terraform-remote-state-using-a-remote-backend)

Built with [Mintlify](https://mintlify.com).
