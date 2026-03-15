# Source: https://docs.firehydrant.com/docs/scheduled-maintenances.md

# Scheduled Maintenances

> 📘 Note:
>
> Scheduled maintenances are basically incidents with **MAINTENANCE** severity. Depending on how your  Services, Functionalities, and Runbooks are configured, automations will fire off when the maintenance "incident" starts.

## Creating a new scheduled maintenance

<Image alt="Scheduled Maintenance form in the web UI" align="center" src="https://files.readme.io/ce6ad3c-Screenshot_2023-12-07_at_6.47.56_PM.png">
  Scheduled Maintenance form in the web UI
</Image>

In the nav, go to **Incidents** and then **Scheduled maintenances** on the left side.

1. Click **+ Add maintenance** on the top right.
2. Fill in the details for this maintenance:
   1. **Name** - A recognizable title for this maintenance event. This will automatically be the name of the maintenance incident that is created.
   2. **Summary** - A description of what's happening in this maintenance event. This will automatically be the description of the maintenance incident
   3. **Start Date/Time** - When the maintenance is tentatively starting. The maintenance incident will automatically start at this tie.
   4. **End Date/Time** - When the maintenance is expected to end. This impacts how long the maintenance note shows up on a status page for, if a status page is attached to this maintenance event.
   5. **Services/Functionalities/Environments** - Which components will be impacted by the maintenance event. If these components are linked to components on a status page attached to this maintenance, those components will be marked appropriate on the status page.
   6. **Attach to status pages** - Optionally attach status pages to this maintenance event to notify end users. The message will show up on the status page(s), and subscribers to the page(s) will be notified of the maintenance.
3. Click **Schedule**.

## Editing a Scheduled Maintenance

To change a maintenance schedule, select a previously scheduled maintenance by clicking its name in the list of scheduled maintenances. Update details as necessary.

If there are one or more status pages attached to the scheduled maintenance, your changes will be reflected on those page(s).

## Canceling a Scheduled Maintenance

To cancel a scheduled maintenance, click the name of the maintenance schedule. On the edit page for the schedule, click **Delete permanently**.

> 🚧 Note:
>
> This is only effective if your maintenance incident has not yet started. If it has, deleting the Scheduled Maintenance does not automatically Resolve or Archive the corresponding incident. You will need to resolve that incident directly via its Command Center

## What happens when a scheduled maintenance starts?

When the start time for a scheduled maintenance occurs, FireHydrant automatically creates an incident for you. 

* FireHydrant creates the incident with all of the impacts that you configured in the scheduled maintenance.
* If something goes wrong with your scheduled maintenance and you need to escalate it to an unplanned outage, you must also change the severity of the automatically created incident.
* If there are status pages attached to the scheduled maintenance, they will be automatically connected to the incident.
* Scheduled maintenance incidents do not currently automatically resolve, you must resolve the maintenance incident manually. 

## Best practices for scheduled maintenance

We recommend treating scheduled maintenance in a similar way you would treat an incident. For example, we suggest creating a Runbook specifically for maintenance events. That Runbook might bring your team into the maintenance incident channel to monitor the state of things during the maintenance window so that they're ready to take action if things go awry, at which point an active incident could be declared.

Throughout the maintenance window, the maintenance incident channel can be used to record notes on how the maintenance activity is progressing. Someone from the team will also need to confirm the maintenance is complete, and then resolve the incident manually, as scheduled maintenance windows are not currently automatically resolved based on the scheduled completion time.

## Integration with FireHydrant Status Pages

FireHydrant status pages will display any currently ongoing or future scheduled maintenances. This way, anyone viewing a status page will know what to expect.

All subscribers (email or RSS) of a status page will receive a notification in one of the following scenarios:

* A scheduled maintenance has a status page attached to it.
* The scheduled maintenance will start in 24 hours.
* The scheduled maintenance is canceled within 24 hours of starting.

## Next Steps

* See how to [Conduct Retrospectives](https://docs.firehydrant.com/docs/conducting-retrospectives) in FireHydrant
* Look at [setting up a FireHydrant status page](https://docs.firehydrant.com/docs/status-page-setup)
* Browse the [Integrations Overview](https://docs.firehydrant.com/docs/integrations-overview) to see the FireHydrant landscape