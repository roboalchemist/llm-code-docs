# Source: https://docs.statsig.com/metrics/archiving-metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Archiving and Deleting Metrics

> Manage the end-of-life for metrics through archiving and deletion options in Statsig.

Statsig offers two ways to manage the end-of-life for your metrics.

* **Archiving a metric**: the metric will no longer be computed, but its history will be retained for your record. Use this for when a metric is no longer relevant, but you still wish to maintain the history of it. Use case example: you can archive older versions of a metric that continues to evolve so you have a record of how the metric has evolved over time.
* **Deleting a metric**: the metric will be removed from Statsig completely, including its history. Use this for when you've made a mistake, logged or imported an irrelevant metric, or created a more accurate version of a metric. Use case examples include incorrect definition, incorrect name, duplicate metric that you don't want to confuse others with.

## Archiving Metrics

### Archiving a Metric

There are two ways to archive a metric:

1. In your Metric Catalog, select the metric(s) you want to archive to see a toolbar of options appear to **Archive**, **Compare**, or **Tag**. Select the **Archive** icon.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/hdTkQo7iTJfd4sfn/images/metrics/archiving-metrics/215638876-3c2ae682-8db8-4dc7-9c14-3b4d7185f57e.png?fit=max&auto=format&n=hdTkQo7iTJfd4sfn&q=85&s=0adcd712f1e41c7ef1fc2e389a3acdae" alt="Bulk Archive" width="1428" height="629" data-path="images/metrics/archiving-metrics/215638876-3c2ae682-8db8-4dc7-9c14-3b4d7185f57e.png" />
</Frame>

2. In the Metrics Detail View page, select the "..." in the upper right-hand corner, and select **Archive**.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/archiving-metrics/215639240-321b4e3f-d9c7-4f7d-ab77-9e18ba1c5867.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=6b392f71c64fac50c7dc85988a8d92e2" alt="Archive" width="1397" height="646" data-path="images/metrics/archiving-metrics/215639240-321b4e3f-d9c7-4f7d-ab77-9e18ba1c5867.png" />
</Frame>

Once you select Archive, Statsig will check if this metric is used in any feature gates, experiments, or other metrics.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/archiving-metrics/215640348-b210eb9e-5475-4853-869f-7a9f66375f0a.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=077930845d31eab7a5b4f76f71922945" alt="Archive dependencies" width="1391" height="883" data-path="images/metrics/archiving-metrics/215640348-b210eb9e-5475-4853-869f-7a9f66375f0a.png" />
</Frame>

While feature gate or experiment dependencies will be shown as soft warnings (no action necessary), metric dependencies will require you to remove the dependency first, before proceeding with the archival. This is because archival of a metric stops its computation, and we don't want other dependent metric values impacted by this archival.

Once you have no metric dependencies, you will start a 24-hour grace period during which you'll be able to undo the archival. In the Metrics Detail View page, you will see a new banner appear at the top of the page, indicating the start of the grace period.

After the 24-hour grace period, Statsig will stop computing this metric and the Metric Detail View page will update with a new banner indicating that the metric has been archived, and Metric Value will change to a disabled state to indicate that this metric is archived.

### Implications of Archiving a Metric

*As soon as the **Archive** button is clicked,*

* 24-hour grace period will start
* Owners of Experiments and Gates using this metric will receive an email notification to be notified of potential impact upstream

*After the 24-hour grace period has ended,*

* Archived metrics will no longer be computed (when the 24-hour grace period ends).
* Archived metrics will not show up in your Metric Catalog search. To access all archived metrics, go to the last page(s) of your Metrics Catalog.
* Archived metrics will be removed from Pulse, including any time the archived metric has been added to the Scorecard of an experiment or the Monitoring Metrics section of a Feature Gate

### Unarchiving a Metric

If you mistakenly archived a metric you can undo your Archival.

* *During* the 24-hour grace period: Click "undo" on the archival banner at the top of the Metrics Detail View page. Since you **Unarchived** before the grace period ended (when the metric is no longer computed), this will restore the  metric to both your Metrics Catalog as well as any experiment results that include the metric.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/archiving-metrics/215640435-412375f7-398b-4bef-9495-cc20d1805769.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=07f20fa3e100b6e935331934a69142a9" alt="Archive Grace Period" width="1392" height="324" data-path="images/metrics/archiving-metrics/215640435-412375f7-398b-4bef-9495-cc20d1805769.png" />
</Frame>

* *After* the 24-hour grace period: Either a) go to the last few pages of your Metrics Catalog, select the archived metric(s) you want to **Unarchive** to see a toolbar of options appear, and select the **Unarchive** icon OR b) in the Metrics Detail View page of an archived metric, select "Unarchive" in the banner indicating metric's archival

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/archiving-metrics/215640543-7cb05d46-e61d-4cf4-a07c-eb76c9f50e36.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=c5618c05173f586fb28740202cbaa843" alt="Archive after grace period" width="1403" height="345" data-path="images/metrics/archiving-metrics/215640543-7cb05d46-e61d-4cf4-a07c-eb76c9f50e36.png" />
</Frame>

Since the grace period has ended and the metric has stopped being computed already, its calculation will restart from scratch and history will not be restored.

### Auto-Archival

To combat metric clutter, Statsig offers a default auto-archival feature that cleans up metrics that have not been in-use for at least 60 days. Metric creators and admins will get a warning about a week before archival happens, at which time they can either choose to extend the metric for another 60 days or mark it as permanent. The entire process is outlined below:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/archiving-metrics/c7912507-636f-4f33-9555-70180dfd205e.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=c65c0f9d492b0d84ca869192454af1a4" alt="State graph" width="616" height="475" data-path="images/metrics/archiving-metrics/c7912507-636f-4f33-9555-70180dfd205e.png" />
</Frame>

#### How do we measure activity?

Statsig counts the number of times the custom metric is used in one or more of the following components:

1. *Scorecard*: Used in experiments, pulse reports, holdouts, etc.
2. *Dashboards*: Used to build dashboards and other analytical assets
3. *Other Metrics*: Used to calculate other composite metrics

If a metric is in use, it will be considered as active. You can see a summary of a metric’s usage on the metric’s main page:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/archiving-metrics/6f7eb3db-399a-45c8-be19-794e89dd349d.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=77b9257188f7643f9a9058e75ca1070a" alt="Metric References" width="1356" height="229" data-path="images/metrics/archiving-metrics/6f7eb3db-399a-45c8-be19-794e89dd349d.png" />
</Frame>

At the same time, we are also detecting (1) any edits to the metrics, including changing any fields in the setup or restoring a previous version, (2) adding tags to the metrics, or (3) creating or modifying an alert on the metric. Any such interaction would restart the 60 day clock.

#### How to Pause / Stop Auto-Archiving

Any tracked action above (adding it to a scorecard, etc) will also take the metric out of the archival queue. Outside of that, if you want to pause the archival process, you may simply extend the metric for another 60 days. We also give you an option to mark it as permanent, which takes it out of the auto-archival process entirely. We recommend this only for the most important and widely reused metrics.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/archiving-metrics/d7378d7b-a588-496b-ae35-24f38c6d5b6a.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=ae6f6d7d8f56fa276cccb77aa1620380" alt="Banner" width="1238" height="182" data-path="images/metrics/archiving-metrics/d7378d7b-a588-496b-ae35-24f38c6d5b6a.png" />
</Frame>

Another way to mark it as permanent by clicking into the setup dropdown from the metrics page and selecting “Mark as Permanent”

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/archiving-metrics/2a570a92-76d6-41b3-aea5-ebdd53469856.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=f76b1a0d127fb19ab034197505b25f01" alt="Dropdown" width="1261" height="347" data-path="images/metrics/archiving-metrics/2a570a92-76d6-41b3-aea5-ebdd53469856.png" />
</Frame>

If you’d like to turn off auto-archiving entirely for your project, you may do so in the Project Settings page

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/archiving-metrics/74cd5575-e1bb-4f69-87f9-1feece5eb73f.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=0f2804c65c45f382b59885e77e036f41" alt="Project Settings" width="1443" height="629" data-path="images/metrics/archiving-metrics/74cd5575-e1bb-4f69-87f9-1feece5eb73f.png" />
</Frame>

# Deleting Metrics

### Deleting a Metric

To delete a metric, go the Metrics Detail View page of a metric you wish to delete, select the "..." in the upper right-hand corner, and select **Delete**.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/archiving-metrics/215641202-82f23bac-f620-4d4a-8c32-fe64a4ffc06c.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=1d8beb3fc069f737e80d40633490a45a" alt="Delete metric" width="1383" height="478" data-path="images/metrics/archiving-metrics/215641202-82f23bac-f620-4d4a-8c32-fe64a4ffc06c.png" />
</Frame>

Once you select Delete, Statsig will check if this metric is used in any feature gates, experiments, or other metrics. While feature gate or experiment dependencies will be shown as soft warnings (no action necessary), metric dependencies will require you to remove the dependency first, before proceeding with the deletion, so that other dependent metric values are not impacted by this deletion.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/archiving-metrics/215641295-55c8dc10-7199-4505-ba0e-d02299fb371a.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=e770fb7a09fa8b4032d4139ccae32ee9" alt="Dependencies" width="1382" height="870" data-path="images/metrics/archiving-metrics/215641295-55c8dc10-7199-4505-ba0e-d02299fb371a.png" />
</Frame>

Once you have no metric dependencies, you will start a 24-hour grace period during which you'll be able to undo the deletion. In the Metrics Detail View page, you will see a new banner appear at the top of the page, indicating the start of the grace period.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/archiving-metrics/215641634-1c70e688-0fe9-4cac-80bb-d3faeedcc0ed.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=53b46560d46cb75a089eac2b431429b0" alt="Undo delete" width="1363" height="386" data-path="images/metrics/archiving-metrics/215641634-1c70e688-0fe9-4cac-80bb-d3faeedcc0ed.png" />
</Frame>

***Metric Deletion cannot be undone after the grace period.***

### Implications of Deleting a Metric

*As soon as **Delete** button is clicked*

* 24-hour grace period will start
* Owners of Experiments and Gates using this metric will receive an email notification to be notified of potential impact upstream

*After the 24-hour grace period has ended,*

* Deleted metrics and their history will be removed from Statsig, and cannot be restored.
* Deleted metrics will be removed from Pulse, including any time the deleted metric has been added to the Scorecard of an experiment or the Monitoring Metrics section of a Feature Gate


Built with [Mintlify](https://mintlify.com).