# Source: https://docs.statsig.com/feature-flags/safeguards-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a Safeguard

> Learn how to create a Safeguard on one or multiple targeting rules within a Feature Gate to monitor regressions and automatically take action when alerts fire.

You can create a Safeguard on one or multiple targeting rules within a Feature Gate. To create a Safeguard on a rule, follow the steps below:

1. Go to a Feature Gate's **Setup** tab

2. Pick a targeting rule for which you want to monitor regressions

3. Click the three-dot (...) menu and choose **'Safeguard Rule'**

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/safeguards/create-safeguard.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=8014edc7e923757bf2f78f9943de919f" alt="Create Safeguard on a rule" width="1226" height="288" data-path="images/safeguards/create-safeguard.png" />
   </Frame>

4. Choose the action to take when alerts fire:

   * **Rollback to 0%** - Assign Default value to all users
   * **Roll out to 100%** - Assign Pass value to all users
   * **Pause Rollout** - Stop scheduled rollout progression (only available with active Schedule Rollout policy)

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/safeguards/choose-safeguard-action.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=cb1eaa3d30dce1a04105a3a6ea2dadd8" alt="Select an action" width="1230" height="608" data-path="images/safeguards/choose-safeguard-action.png" />
   </Frame>

5. (Optional) Set how long to monitor alerts for safeguarding the rule:

   | Alert type    | Evaluation period | Evaluation start time                           |
   | ------------- | ----------------- | ----------------------------------------------- |
   | Topline alert | Choose your own   | Starts when the safeguard is created            |
   | Rollout alert | Fixed (90 days)   | Starts whenever targeting rule's pass % changes |

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/safeguards/evaluation-period.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=96c5c6b14a57b70601d38c28c16cc4ce" alt="Set evaluation period" width="1230" height="610" data-path="images/safeguards/evaluation-period.png" />
   </Frame>

   <Tip>**Recommended:** Ideally you want to monitor topline alerts for crashes, errors, latency, etc. *for a few days* after a Feature Gate rollout to make sure things are stable. We recommend starting with a 14-day evaluation period.</Tip>

6. Select one or more alerts to monitor:

   * Rollout alerts - For feature-specific regression detection
   * Topline alerts - For system-wide health monitoring

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/safeguards/add-alerts.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=6e8ac6127c1aee2b6446779f8c5e0b15" alt="Add alerts for your Safeguard" width="1228" height="864" data-path="images/safeguards/add-alerts.png" />
   </Frame>

7. Click **Save**


Built with [Mintlify](https://mintlify.com).