# Source: https://docs.envzero.com/guides/admin-guide/environments/scheduling.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deployment Scheduling

> Schedule automatic deploys and destroys for env zero environments using cron expressions

## What is Scheduling?

Scheduling allows you to automatically trigger destroys and deploys of your environments on a scheduled basis.

Scheduling is configured based on cron expressions, and can be attached to an already deployed environment only.

<Info>
  **Scheduling vs TTL**

  Scheduling is an advanced feature that currently can't coexist with the simpler TTL policy of your environment, so please note that enabling scheduling for you environment will disable any existing TTL setting of your environment.

  It's also important to notice that TTL policies don't apply on any scheduled recurrences.
</Info>

## Who Can Configure Scheduling

The minimum role for setting a scheduled action for an environment is [Project Deployer](/guides/admin-guide/user-role-and-team-management/user-management/#project-roles).

## How To Configure Scheduling

After deploying your environment, click on **Settings** tab, on \*\*Environment Details \*\*page and scroll down to the **Scheduling** card.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/SMkZGUXJ1AhEm5OR/images/guides/admin-guide/environments/environment_scheduling_configuration_interface.png?fit=max&auto=format&n=SMkZGUXJ1AhEm5OR&q=85&s=268dc1249ec68fdd7e7f21913724d409" alt="Environment scheduling configuration interface" width="1447" height="468" data-path="images/guides/admin-guide/environments/environment_scheduling_configuration_interface.png" />
</Frame>

To configure scheduling for your environment:

1. Check the box for the required action (either *Deploy* or *Destroy*)
2. Input a valid [UNIX cron expression](http://www.nncron.ru/help/EN/working/cron-format.htm) (Optional Year suffix isn't supported).\
   <ins>For example:</ins> `0 23 * * MON-FRI` (UTC timezone)
3. Press **Save**.

The environment is now scheduled! You may notice that the environment's countdown indication has changed per your next schedule:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/SMkZGUXJ1AhEm5OR/images/guides/admin-guide/environments/scheduled_environment_countdown_display.png?fit=max&auto=format&n=SMkZGUXJ1AhEm5OR&q=85&s=f9a60a55a613abad19664e2a576ce8a8" alt="Scheduled environment countdown display" width="156" height="101" data-path="images/guides/admin-guide/environments/scheduled_environment_countdown_display.png" />
</Frame>

Built with [Mintlify](https://mintlify.com).
