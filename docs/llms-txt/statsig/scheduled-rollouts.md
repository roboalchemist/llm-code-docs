# Source: https://docs.statsig.com/feature-flags/scheduled-rollouts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scheduled Rollouts

> Pre-set time-based feature rollout schedules that execute automatically

Feature Gates are powerful in ensuring a safe, controlled feature rollout. Scheduled Rollouts add a time-based scheduling layer to Feature Gates, enabling you to pre-set any rollout schedule you want, which will execute automatically. This is particularly useful if, for example, you have a feature launch happening in another timezone (and don't want to stay up all night!) or you have a standard, company-wide ramp-up schedule you follow with every feature release.

Scheduled rollouts are set at the Feature Gate **rule** level, enabling maximal flexibility. Not all rules in your Gate need to include a scheduled rollout, simply set it up for whichever rules make the most sense.

## Set up a Scheduled Rollout

To set up a Scheduled Rollout on a rule in your Feature Gate, simply tap on the "…" in the upper right-hand corner of the rule you want to schedule a rollout for.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/LlhWAKAM8RRcyVab/images/feature-flags/scheduled-rollouts/199850775-42528d6c-b8f1-4e5d-9774-bc1b576c2916.png?fit=max&auto=format&n=LlhWAKAM8RRcyVab&q=85&s=b8403e1dd12344fb020d1eeb563b87bf" alt="Feature Gate rule menu options" width="1573" height="710" data-path="images/feature-flags/scheduled-rollouts/199850775-42528d6c-b8f1-4e5d-9774-bc1b576c2916.png" />
</Frame>

Select **Edit Rule or Rollout**, and then select **Schedule Automated Rollout**.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/LlhWAKAM8RRcyVab/images/feature-flags/scheduled-rollouts/199851487-2e2aba51-30d5-4fef-933f-b31c0e78dd57.png?fit=max&auto=format&n=LlhWAKAM8RRcyVab&q=85&s=13d6f52d0d4a897df5eb9e95b391104f" alt="Schedule Automated Rollout selection" width="1294" height="1048" data-path="images/feature-flags/scheduled-rollouts/199851487-2e2aba51-30d5-4fef-933f-b31c0e78dd57.png" />
</Frame>

From here, you can configure each phase of your Scheduled Rollout. You will see in the upper right-hand corner your current pass percentage- this simply reflects the baseline pass percentage you entered for your rule and can be changed via **Edit Rule**. To add phases to your rollout, click **Add Phase** and configure as many phases as you want.

Each scheduled rollout phase includes-

* Rollout date
* Rollout time\*
* Pass percentage

<Note>
  Rollout times are available in 15 minute increments. Additionally, each configured phase represents a discrete increase to the next rollout percentage, not a gradual rollout amortized over the course of the entire phase.
</Note>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/LlhWAKAM8RRcyVab/images/feature-flags/scheduled-rollouts/199851781-60606e6b-d653-408a-a3ba-399e32d582b0.png?fit=max&auto=format&n=LlhWAKAM8RRcyVab&q=85&s=8ef3f5e9923e52af6c9077debd5f3634" alt="Scheduled rollout configuration interface" width="1292" height="1051" data-path="images/feature-flags/scheduled-rollouts/199851781-60606e6b-d653-408a-a3ba-399e32d582b0.png" />
</Frame>

As you are building your Scheduled Rollout, you will see a preview of the phases below the configuration wizard. This preview is also available for viewers of your Feature Gate on hover over a rule.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/LlhWAKAM8RRcyVab/images/feature-flags/scheduled-rollouts/199851974-c95ea9d2-6d04-4c3e-b9e5-f5d5ea3d85b3.png?fit=max&auto=format&n=LlhWAKAM8RRcyVab&q=85&s=ae610ab6ea2d3523272ff53efa744f71" alt="Scheduled rollout phases preview" width="1299" height="1040" data-path="images/feature-flags/scheduled-rollouts/199851974-c95ea9d2-6d04-4c3e-b9e5-f5d5ea3d85b3.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/LlhWAKAM8RRcyVab/images/feature-flags/scheduled-rollouts/199851640-007d63d5-7b9e-4002-93af-132af24416a1.png?fit=max&auto=format&n=LlhWAKAM8RRcyVab&q=85&s=6b42112c203cf6e1d199e712f775a9c8" alt="Rollout phases hover preview" width="1604" height="548" data-path="images/feature-flags/scheduled-rollouts/199851640-007d63d5-7b9e-4002-93af-132af24416a1.png" />
</Frame>

## Execute a Scheduled Rollout

Once configured, each phase of a Scheduled Rollout will execute automatically on the schedule specified. The Feature Gate creator, any editors, and anyone Following the Feature Gate will receive Scheduled Rollout notifications.

Notifications will be sent via:

* Email
* Console
* (Optional) Slack
  * To configure Slack notifications on Statsig, go to "Account Settings → Notifications"


Built with [Mintlify](https://mintlify.com).