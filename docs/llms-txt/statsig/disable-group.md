# Source: https://docs.statsig.com/experiments/implementation/disable-group.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Disable a Group

> Learn how to disable poorly performing experiment groups while keeping other test groups running.

## Disabling a Group in an Experiment

Sometimes you start an experiment with multiple test groups, only to find that one of the groups is performing very poorly or creating bad user experiences. The other test groups are fine and you want to keep them running, but stop the bad experiences. For these situations, we allow you to disable an experiment group.

### What to expect when group is disabled

* Users already assigned to the disabled group will begin to receive the default experience
* New users can be assigned to the disabled group and receive the default experience
* Exposures for the disabled group will continue to be tracked
* Sample Ratio Mismatch (SRM) should not be triggered from the disabled group
* Experiment results will continue to be calculated for the disabled group

<Info>
  We keep showing the group and logging exposures so that you can verify that the user experiences have recovered after the group was disabled.
</Info>

### How To

* Log into the Statsig console at [https://console.statsig.com](https://console.statsig.com)
* On the left-hand navigation panel, select **Experiments**
* Select the experiment where you want to disable a group
* Click on the **...** menu in the top right corner
* Select the **Disable A Group** option
* Select the experiment groups you would like to disable, and hit **Confirm**

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ax_yxPlGE0DmsCCZ/images/experiments/implementation/disable-group/175094935-1dbb9b34-ebbe-467c-9a84-e61aeeb3180f.png?fit=max&auto=format&n=ax_yxPlGE0DmsCCZ&q=85&s=062794f1b9f3c50d4204aa4f466d1305" alt="Experiment overflow menu showing Disable a Group option" width="405" height="307" data-path="images/experiments/implementation/disable-group/175094935-1dbb9b34-ebbe-467c-9a84-e61aeeb3180f.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ax_yxPlGE0DmsCCZ/images/experiments/implementation/disable-group/175095107-2ef5d9e3-4c33-44ec-ac13-937f3b030149.png?fit=max&auto=format&n=ax_yxPlGE0DmsCCZ&q=85&s=78018a6de369d15c792d69d8a00d026b" alt="Disable group dialog listing experiment groups with toggles" width="521" height="455" data-path="images/experiments/implementation/disable-group/175095107-2ef5d9e3-4c33-44ec-ac13-937f3b030149.png" />
</Frame>

## Reenable a Group

If you've previously disabled a group but want to revert this change, you can reenable a group by using the **...** menu and selecting **Disable or Enable A Group**.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ax_yxPlGE0DmsCCZ/images/experiments/implementation/disable-group/2fa3cb71-9a46-46f1-bb11-b8e7f07df9c6.png?fit=max&auto=format&n=ax_yxPlGE0DmsCCZ&q=85&s=e07882470f66017a1fe553399d037876" alt="Menu option to disable or enable a group in experiment controls" width="292" height="490" data-path="images/experiments/implementation/disable-group/2fa3cb71-9a46-46f1-bb11-b8e7f07df9c6.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ax_yxPlGE0DmsCCZ/images/experiments/implementation/disable-group/a56e7f14-53e9-4d41-8266-d70de1ec3ebf.png?fit=max&auto=format&n=ax_yxPlGE0DmsCCZ&q=85&s=0b7a158270ebb310feba37c2f1695678" alt="Modal showing reenable group selections" width="523" height="521" data-path="images/experiments/implementation/disable-group/a56e7f14-53e9-4d41-8266-d70de1ec3ebf.png" />
</Frame>

<Info>
  Be mindful that users in any reenabled group might have experienced multiple treatment experiences over the course of the experience. This may be reflected in the metric data collected for the group.
</Info>


Built with [Mintlify](https://mintlify.com).