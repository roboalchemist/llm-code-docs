# Source: https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/llms.txt

# AWS Elemental Conductor Live Upgrade Guide

> This guide is intended for engineers who upgrade or downgrade the software running on the nodes of an AWS Elemental Conductor Live cluster that is controlling AWS Elemental Live and AWS Elemental Statmux nodes.

- [About this guide](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/about-cl3-upg.html)
- [Rules for software versions](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upgrades-version-rules.html)
- [Downloading Software](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/detailed-dl-cl3-upg.html)
- [Document History](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/doc-history.html)

## [Cluster Upgrades](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upgrades-cl3-upg.html)

### [Standard Conductor Live upgrade](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upgrades-cl3-upg-std.html)

The process outlined in this section is for a standard upgrade of the AWS Elemental Conductor Live software, where all nodes are taken offline and upgraded within a maintenance window.

- [Step A: Get ready](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upgrades-cl3-upg-single-ver-version.html): The following steps prepare you to perform a standard upgrade of an Conductor Live node.
- [Step B: Copy the AWS Elemental installers](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-std-copy-ins.html): Locate and copy the AWS Elemental installers for worker and Conductor Live nodes.
- [Step C: Disable high availability](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-std-disable.html): If you don't have high availability enabled, skip this step and go to .
- [Step D: Remove the secondary Conductor Live node](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-std-rem-sec.html): If you have only one Conductor Live, skip this step and go to .
- [Step E: Stop the running channels](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-std-stop.html): You must stop all running channels before you upgrade.
- [Step F: Remove worker nodes](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-std-remove-w.html): Remove the worker nodes from the redundancy group, and then from the cluster.
- [Step G: Upgrade worker nodes](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-std-all.html): Perform these steps on the AWS Elemental Live nodes.
- [Step I: Add worker nodes](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-std-add-w.html): Add the worker nodes back to the cluster and their redundancy groups.
- [Step J: Add the secondary Conductor Live node](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-std-add-sec.html): If you have only one Conductor Live, skip this step and go to .
- [Step K: Start channels](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-std-start.html): When all nodes have been upgrade, you can start the channels that were previously running.
- [Step L: Re-enable high availability](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-std-reenable.html): You re-enable high availability when you have more than one Conductor Live node.

### [Reduced downtime Conductor Live upgrade](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upgrades-cl3-upg-red.html)

The process outlined in this section uses worker redundancy to limit the upgrade downtime.

- [Step A: Get ready](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upgrades-cl3-upg-red-single-ver-version.html): The following steps prepare you for upgrading.
- [Step B: Copy the AWS Elemental installers](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-red-copy-ins.html): Locate and copy the AWS Elemental installers for worker and Conductor Live nodes.
- [Step C: Remove the backup worker nodes](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-red-remove-bup.html): Remove the backup worker nodes from the redundancy group before removing them from the cluster.
- [Step D: Upgrade the backup worker nodes](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-red-b-wrker.html): The role of backup nodes is not to run channels but to take over from an active node that fails.
- [Step E: Add back the backup worker nodes](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-red-add-bup.html): Add the backup workers back to the cluster and redundancy groups so that they can encode while the remaining workers are upgraded.
- [Step F: Fail over an active node](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-red-fail.html): Fail over the running channels from the first active worker node that you're upgrading to a backup node.
- [Step G: Remove the failed worker node](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-red-remove-failed.html): Remove the failed worker node from the redundancy group and then from the cluster.
- [Step H: Upgrade the failed active node](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-red-a-wrker.html): Now upgrade the active worker node that you just failed over.
- [Step I: Add failed worker node](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-red-add-failed.html): Add the failed worker back to the cluster and redundancy groups so that it can encode while the remaining workers are upgraded.
- [Step J: Fail back the running channels](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-red-back.html): Move the running channels back to the upgraded active node by failing over the backup node that they're currently on.
- [Step K: Re-designate the backup worker node](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-red-redesignate.html): Re-designate the backup worker as a backup so that it only runs active channels that have failed over from an active worker node.
- [Step L: Disable high availability](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-red-disable.html)
- [Step M: Remove the secondary Conductor Live node](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-red-rem-sec.html): If you have only one Conductor Live, skip this step and go to .
- [Step N: Upgrade the secondary Conductor Live node](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-red-sec.html): If you have only one Conductor Live, skip this step and go to .
- [Step O: Upgrade the primary Conductor node](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-red-pri.html)
- [Step P: Add the secondary Conductor Live node](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-red-add-sec.html): If you have only one Conductor Live, you don't need to do this step.
- [Step Q: Re-enable high availability](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-red-reenable.html)
- [Sample Upgrade](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/sample-upg-cl3-upg.html): Following is a screen printout of a typical upgrade, showing the prompts and possible responses.


## [Cluster Downgrades](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/downgrades-cl3-upg.html)

- [Step A: Get ready](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/downgrades-cl3-upg-locate-res-dn.html): The following steps prepare you for downgrading.
- [Step B: Copy the AWS Elemental installers](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/downgrades-cl3-upg-locate-sw-dn.html): Locate and copy the AWS Elemental installers for worker and Conductor nodes.
- [Step C: Stop the running channels](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/downgrades-cl3-upg-stop-chan.html): You must stop all running channels before you downgrade.
- [Step D: Disable high availability](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/downgrades-cl3-upg-ha-disable-ha.html): If you don't have high availability enabled, skip this step and go to .
- [Step E: Remove the secondary Conductor node](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/downgrades-rem-sec.html): If you have only one Conductor Live, skip this step and go to .
- [Step F: Downgrade the nodes](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/downgrades-cl3-upg-dg-cond.html): When you downgrade, run the installer with the --downgrade option for each node.
- [Step G: Add the secondary Conductor Live node](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/downgrades-add-sec.html): If you have only one Conductor Live, skip this step and go to .
- [Step H: Start channels](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/downgrades-start.html): When all nodes have been downgraded, you can start the channels that were previously running.
- [Step I: Re-enable high availability](https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/downgrades-reenable.html)
