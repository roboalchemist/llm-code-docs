# Source: https://planetscale.com/docs/vitess/maintenance-schedules.md

# Maintenance schedules

> Enterprise customers have the option to enable scheduled maintenance windows on databases.

If you have a maintenance schedule enabled, any changes to your cluster configuration will only roll out during the set maintenance period. This includes MySQL and Vitess version upgrades, increasing or decreasing cluster size, changes to the size of VTTablets and VTGates, and anything else that modifies your cluster configuration.

The only exceptions to this are the following:

* Changes to the *number* of VTGates

Modifications to your schema, such as [deploy requests](/docs/vitess/schema-changes/deploy-requests) and [workflows](/docs/vitess/scaling/workflows), are not included in the maintenance schedule and will complete as soon as you apply the changes.

## Enabling maintenance schedules

To enable the use of maintenance schedules, you must first reach out to our [Support team](https://planetscale.com/contact).

Once the feature is enabled on a database, you can configure the maintenance windows for each of your databases by clicking the database > Settings > Maintenance.

Maintenance schedules can be set up on a daily, weekly, or monthly basis at a specific time in UTC. When occurring weekly, you can set the day of the week. When occurring monthly, you can set the day of the week and which week of the month over which the maintenance will occur.

To modify a maintenance schedule, click on the available schedule, and then adjust via the dropdowns.

If you need to make a change during an emergency, you can disable the maintenance schedule. That will result in the branch immediately running any queued tasks. If you are making a change in an emergency, we recommend that you perform the sizing operation first to queue the change, and then disable the maintenance schedule.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt