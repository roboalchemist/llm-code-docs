# Source: https://docs.firehydrant.com/docs/incident-tags.md

# Incident Tags

Tags allow FireHydrant users to organize and otherwise track different incident data. This allows both searching and querying for incidents with specific tags, as well as filtering Analytics and metrics by said tag(s).

In addition, tags can also be used as conditional triggers for Runbooks and Runbook steps (e.g. if an incident is tagged `3rd-party`, then execute Runbook `3rd-Party Outage Runbook`, for example).

## Creating new tags

New tags are created in the same places users will add tags to incidents. **If a tag does not exist, it will be created.** See the next section.

## Adding tags to an incident

<Image alt="Tags section of the Command Center" align="center" width="650px" src="https://files.readme.io/a0455d2-Screenshot_2023-12-11_at_12.09.11_PM.png">
  Tags section of the Command Center
</Image>

<Image alt="Running `/fh tags` in the Slack incident channel" align="center" width="400px" src="https://files.readme.io/6e35e45-image.png">
  Running `/fh tags` in the Slack incident channel
</Image>

You can add tags to an incident by:

* Typing a tag name on the [declare incident](https://docs.firehydrant.com/docs/starting-incidents) form in the UI or in Slack
* Editing the Tags section in the right-side Details panel of the [The Command Center](https://docs.firehydrant.com/docs/the-command-center) mid-incident
* Executing `/fh tags` command in an active incident channel in Slack
* Running `/fh edit` or `/fh add tags` command in an active incident channel in Slack\*
* Via [Incident Types](https://docs.firehydrant.com/docs/incident-types), where you can declare incidents with preset fields and values including tags
* Via the API, either [creating a new incident](https://developers.firehydrant.com/#/operations/postV1Incidents) or [updating an existing one](https://developers.firehydrant.com/#/operations/patchV1IncidentsIncidentId)

> 📘 \*Note:
>
> You'll need to make sure the "Tags" field is set to **Visible** or **Available** in the [Incident Fields](/docs/incident-fields#showinghiding-fields)

## Using Tags

### Filtering

Once you've tagged some incidents, you'll be able to filter by tags on both the **[Incidents page](https://app.firehydrant.io/incidents)** as well as on the **[Analytics page](https://app.firehydrant.io/analytics/incidents_impacts)**.

<Image alt="Tag filtering on the Incidents page" align="center" src="https://files.readme.io/552b1f4-image.png">
  Tag filtering on the Incidents page
</Image>

### Automation through tags

Tags also work as Runbook conditions. You can kick off individual Runbook steps, or attach new Runbooks to an incident with tags. To learn more, see [Introduction to Runbooks](https://docs.firehydrant.com/docs/introduction-to-runbooks).

## Next Steps

* Learn more about tracking custom data via [Custom Fields](https://docs.firehydrant.com/docs/incident-custom-fields)
* Pre-template fields and values, including tags, using [Incident Types](https://docs.firehydrant.com/docs/incident-types)