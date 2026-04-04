# Source: https://docs.aws.amazon.com/elemental-cl3/latest/ug/llms.txt

# Conductor Live and Elemental Statmux User Guide

> Learn how to use AWS Elemental Conductor Live to run AWS Elemental Live encoding events and create AWS Elemental Statmux MPTSes.

- [Rules and limits](https://docs.aws.amazon.com/elemental-cl3/latest/ug/cl3-rules-limits.html)
- [Display the Conductor Live web interface](https://docs.aws.amazon.com/elemental-cl3/latest/ug/cl3-display-web-interface.html)
- [Resources: The tasks feature](https://docs.aws.amazon.com/elemental-cl3/latest/ug/resource_tasks.html)
- [Reference: Supported channel parameters](https://docs.aws.amazon.com/elemental-cl3/latest/ug/channel-parameters.html)
- [Data generation and management](https://docs.aws.amazon.com/elemental-cl3/latest/ug/cl3-security-data-generated.html)
- [Document History](https://docs.aws.amazon.com/elemental-cl3/latest/ug/document-history.html)

## [About the Conductor Live solution](https://docs.aws.amazon.com/elemental-cl3/latest/ug/what-is.html)

### [Working with Conductor Live](https://docs.aws.amazon.com/elemental-cl3/latest/ug/about-cl3.html)

Learn how to use AWS Elemental Conductor Live to create and manage channels on AWS Elemental Live and MPTSes on AWS Elemental Statmux.

- [General information](https://docs.aws.amazon.com/elemental-cl3/latest/ug/cl3-general.html): Assumptions
- [Software versions](https://docs.aws.amazon.com/elemental-cl3/latest/ug/cl3-software-versions.html): This guide applies to version 2.20.3 and later of Elemental Live and Elemental Statmux, and to version 3.20.3 and later of Conductor Live.
- [Licenses](https://docs.aws.amazon.com/elemental-cl3/latest/ug/cl3-software-licenses.html)
- [Centralized management](https://docs.aws.amazon.com/elemental-cl3/latest/ug/centralized-management.html): Learn about how Conductor Live provides centralized management for AWS Elemental Live and AWS Elemental Statmux nodes.
- [Redundancy and failover](https://docs.aws.amazon.com/elemental-cl3/latest/ug/redundancy-and-failover.html): Running Elemental Live events and Elemental Statmux MPTSes in Conductor Live lets you implement several resiliency features.

### [Working with Elemental Live](https://docs.aws.amazon.com/elemental-cl3/latest/ug/cl3-live-about.html)

Learn about the basics of working with AWS Elemental Live using AWS Elemental Conductor Live.

- [Components of Elemental Live](https://docs.aws.amazon.com/elemental-cl3/latest/ug/el-cluster-usage-components.title.html): When you work with Elemental Live using Conductor Live, you work with channels (events), profiles, and nodes.
- [Comparison of profiles](https://docs.aws.amazon.com/elemental-cl3/latest/ug/comparison-of-profiles-in-cl3-vs-live.html): The way that channels (which you create using Conductor Live) and events (which you create using Elemental Live) use their profiles is different.

### [Working with AWS Elemental Statmux](https://docs.aws.amazon.com/elemental-cl3/latest/ug/cl3-statmux-about.html)

Read about the basics of working with AWS Elemental Statmux using AWS Elemental Conductor Live.

- [Components of Elemental Statmux](https://docs.aws.amazon.com/elemental-cl3/latest/ug/smux-cluster-usage-components.html): To create an MPTS using Elemental Statmux, you need:
- [Features of AWS Elemental Statmux](https://docs.aws.amazon.com/elemental-cl3/latest/ug/cl3-statmux-features.html): Topics
- [AWS Elemental Statmux tutorial](https://docs.aws.amazon.com/elemental-cl3/latest/ug/statmux_tutorial.html): Read a tutorial that walks you through the key steps for creating an MPTS using AWS Elemental Conductor Live and AWS Elemental Statmux.


## [Setup: Design the cluster](https://docs.aws.amazon.com/elemental-cl3/latest/ug/container-cluster-design.html)

- [Conductor Live nodes](https://docs.aws.amazon.com/elemental-cl3/latest/ug/cl3-node-design.html): You need two Conductor Live nodes if you plan to implement Conductor Live node redundancy.
- [Primary Elemental Live nodes](https://docs.aws.amazon.com/elemental-cl3/latest/ug/el-node-design.html): Determine the number of primary nodes you need:
- [Primary Elemental Statmux nodes](https://docs.aws.amazon.com/elemental-cl3/latest/ug/smx-node-design.html): Determine the number of primary nodes you need:


## [Setup: Plan resiliency](https://docs.aws.amazon.com/elemental-cl3/latest/ug/cl3-resiliency.html)

- [Conductor Live node redundancy](https://docs.aws.amazon.com/elemental-cl3/latest/ug/redundancy-cl3.html): You need two Conductor Live nodes to implement Conductor Live node redundancy.

### [Worker node redundancy](https://docs.aws.amazon.com/elemental-cl3/latest/ug/redundancy-worker.html)

This section describes redundancy options for worker nodes in an AWS Elemental Conductor Live cluster.

- [N-to-M redundancy](https://docs.aws.amazon.com/elemental-cl3/latest/ug/redundancy-n-m.html)
- [1-to-1 redundancy](https://docs.aws.amazon.com/elemental-cl3/latest/ug/redundancy-11.html)
- [1-to-1 Plus redundancy](https://docs.aws.amazon.com/elemental-cl3/latest/ug/redundancy-11-plus.html)
- [Organizing groups in the cluster](https://docs.aws.amazon.com/elemental-cl3/latest/ug/redundancy-cluster-level.html): These rules and guidelines apply to organizing multiple redundancy groups in the cluster.
- [Resiliency in Elemental Statmux](https://docs.aws.amazon.com/elemental-cl3/latest/ug/worker-nodes-other-resiliency.html): Elemental Statmux includes two features that provide resiliency for Elemental Statmux â output listening and output redundancy.


## [Workflows: Design an MPTS workflow](https://docs.aws.amazon.com/elemental-cl3/latest/ug/container-design-mpts-workflow.html)

- [Create a standard MPTS](https://docs.aws.amazon.com/elemental-cl3/latest/ug/mpts-design-step-channels.html): Learn how to use AWS Elemental Statmux to create an MPTS workflow that contains programs created by AWS Elemental Live.
- [Including passthrough programs](https://docs.aws.amazon.com/elemental-cl3/latest/ug/mpts-passthrough-program.html): Learn how to use AWS Elemental Statmux to create an MPTS workflow that contains programs that are created by a third party.
- [Passing through custom streams](https://docs.aws.amazon.com/elemental-cl3/latest/ug/mpts-passthrough-high-pids.html): Learn how to use AWS Elemental Statmux to create an MPTS workflow that includes custom passthrough streams.
- [Passing through SI/PSI tables](https://docs.aws.amazon.com/elemental-cl3/latest/ug/mpts-passthrough-PSI-pids.html): Learn how to use AWS Elemental Statmux to create an MPTS workflow that includes passthrough SI/PSI tables.


## [Daily operations: Run workflows](https://docs.aws.amazon.com/elemental-cl3/latest/ug/operations.html)

- [Start and stopping a channel](https://docs.aws.amazon.com/elemental-cl3/latest/ug/starting-and-stopping-channels.html): Learn how to use AWS Elemental Conductor Live to start and stop a channel in a cluster.
- [Scheduling channels](https://docs.aws.amazon.com/elemental-cl3/latest/ug/scheduling-channels.html): Learn how to use AWS Elemental Conductor Live to schedule the running of a channel.
- [Controlling channels](https://docs.aws.amazon.com/elemental-cl3/latest/ug/controlling-channel-inputs.html): Learn how to use AWS Elemental Conductor Live to switch from one input to another in a channel.
- [Starting or stopping an MPTS](https://docs.aws.amazon.com/elemental-cl3/latest/ug/starting-an-mpts-output.html): Learn how to use AWS Elemental Conductor Live to start or stop an MPTS.


## [Daily operations: Monitor workflow activity](https://docs.aws.amazon.com/elemental-cl3/latest/ug/monitoring.html)

- [Monitoring channels](https://docs.aws.amazon.com/elemental-cl3/latest/ug/monitoring-channels.html): Topics
- [Monitoring MPTS outputs](https://docs.aws.amazon.com/elemental-cl3/latest/ug/monitoring-mpts-outputs.html): Topics
- [Monitoring alerts and messages](https://docs.aws.amazon.com/elemental-cl3/latest/ug/monitoring-alerts-and-messages.html): AWS Elemental Conductor Live generates alerts and messages to provide information about the status of the nodes in the cluster and about the encoding channels.
- [Monitoring nodes](https://docs.aws.amazon.com/elemental-cl3/latest/ug/monitoring-conductor-and-worker-nodes.html): You should monitor the nodes regularly to ensure that they are still all online.
- [Monitoring the load on worker nodes](https://docs.aws.amazon.com/elemental-cl3/latest/ug/monitoring-the-load-on-worker-nodes.html): You can view information about the overall load on any worker node in an AWS Elemental Conductor Live cluster.


## [Resources: Profiles](https://docs.aws.amazon.com/elemental-cl3/latest/ug/resource_profile.html)

- [Create profile from scratch](https://docs.aws.amazon.com/elemental-cl3/latest/ug/creating-a-profile-from-scratch.html): Topics

### [Work with channel parameters](https://docs.aws.amazon.com/elemental-cl3/latest/ug/creating-a-profile-with-channel-parameters.html)

You can create an AWS Elemental Live profile in which some fields have values that are variable rather than absolute.

- [Rules for channel parameters](https://docs.aws.amazon.com/elemental-cl3/latest/ug/create-profile-rules.html): There are two rules associated with channel parameters in the profile:
- [The procedure](https://docs.aws.amazon.com/elemental-cl3/latest/ug/create-profile-procedure.html): Follow this procedure to set up a blue field with a channel parameter.
- [Plan for bulk changes](https://docs.aws.amazon.com/elemental-cl3/latest/ug/profile-channel-params-plan-ahead.html): When you create a channel parameter that you might use in another profile, note its name carefully so you can enter the exact same name in the other profile.
- [Use case: SDI direct input](https://docs.aws.amazon.com/elemental-cl3/latest/ug/using-sdi-direct-input-in-a-profile-and-channel.html): You might want to specify an SDI direct input in your profile and channel.
- [Use case: SDI router input](https://docs.aws.amazon.com/elemental-cl3/latest/ug/using-sdi-router-input-in-a-profile-and-channel.html): You might want to specify an SDI router input in your profile and channel.
- [Create profile for SPTS channel](https://docs.aws.amazon.com/elemental-cl3/latest/ug/step-b-create-a-profile-for-mpts-channels.html): An SPTS channel is a channel that you plan to use in an MPTS that you will run on AWS Elemental Statmux.
- [Create profile by duplicating](https://docs.aws.amazon.com/elemental-cl3/latest/ug/creating-a-profile-by-duplicating.html): You can create an AWS Elemental Live profile by duplicating an existing profile and making any changes that you want.
- [Create profile using XML](https://docs.aws.amazon.com/elemental-cl3/latest/ug/creating-a-profile-by-uploading-xml.html): You can create an AWS Elemental Live profile using the XML from an existing profile that is up to two current versions back from the current AWS Elemental Conductor Live version.
- [Modify profile](https://docs.aws.amazon.com/elemental-cl3/latest/ug/modifying-a-profile.html): You can't modify a AWS Elemental Conductor Live profile after it has been created.
- [View profile contents](https://docs.aws.amazon.com/elemental-cl3/latest/ug/viewing-the-contents-of-a-profile.html): To view the contents of an AWS Elemental Live profile, choose Show beside the profile name.
- [Delete profile](https://docs.aws.amazon.com/elemental-cl3/latest/ug/deleting-a-profile.html)


## [Resource: Channels](https://docs.aws.amazon.com/elemental-cl3/latest/ug/resource_channel.html)

- [Create channel](https://docs.aws.amazon.com/elemental-cl3/latest/ug/creating-a-channel.html)
- [Create a channel by duplicating](https://docs.aws.amazon.com/elemental-cl3/latest/ug/creating-a-channel-by-duplicating.html)
- [Modify channel](https://docs.aws.amazon.com/elemental-cl3/latest/ug/modifying-a-channel.html): You can modify a channel that is in the Idle or Error state (that is, when it is not actively running).
- [Change profile for multiple channels](https://docs.aws.amazon.com/elemental-cl3/latest/ug/changing-the-profile-used-by-multiple-channels.html): You can use the Tasks feature to change the profile so that several channels can use it.
- [Delete channel](https://docs.aws.amazon.com/elemental-cl3/latest/ug/deleting-channels.html)


## [Resource: MPTS](https://docs.aws.amazon.com/elemental-cl3/latest/ug/mpts-outputs.html)

### [Create MPTS](https://docs.aws.amazon.com/elemental-cl3/latest/ug/setting-up-mpts-outputs.html)

With Conductor Live there are two steps to creating an MPTSâyou create the MPTS, then you add SPTS channels to it.

### [Step 1. Create the MPTS](https://docs.aws.amazon.com/elemental-cl3/latest/ug/step-a-create-the-mpts-outputs.html)

- [Output tab](https://docs.aws.amazon.com/elemental-cl3/latest/ug/step-create-mpts-tab-output.html)

### [Step 2. Add channels](https://docs.aws.amazon.com/elemental-cl3/latest/ug/step-d-add-channels-to-the-mpts-output.html)

After you create the MPTS, you must add channels.

- [Basic tab](https://docs.aws.amazon.com/elemental-cl3/latest/ug/mpts-channel-tab-basic.html)
- [PID Controls tab](https://docs.aws.amazon.com/elemental-cl3/latest/ug/mpts-channel-tab-pid.html): On this tab, you can assign the output PIDs for the streams that are in the source program.
- [TS Endpoints tab](https://docs.aws.amazon.com/elemental-cl3/latest/ug/mpts-channel-tab-ts.html): This tab contains fields for the endpoints used for communications between the Elemental Live node that is the source of the program and the Elemental Statmux node that receives the program.
- [Complexity Endpoints tab](https://docs.aws.amazon.com/elemental-cl3/latest/ug/mpts-channel-tab-complexity.html): This tab contains fields for the endpoints used for the complexity/allocation communications between the Elemental Live node and the Elemental Statmux node.
- [RateAllocation Endpoints tab](https://docs.aws.amazon.com/elemental-cl3/latest/ug/mpts-channel-tab-allocation.html): This tab contains fields for the endpoints used for the complexity/allocation communications between the Elemental Live node and the Elemental Statmux node.
- [Advanced tab â Suppressing generation of SI/PSI tables](https://docs.aws.amazon.com/elemental-cl3/latest/ug/step-create-mpts-tab-advanced.html): Many of the fields on this tab let you control generation of all the SI/PSI tables that Elemental Statmux can generate.
- [Including passthrough streams](https://docs.aws.amazon.com/elemental-cl3/latest/ug/crud-mpts-pasthrough-streams.html): Read this section if you want to include passthrough streams in the MPTS.
- [Including passthrough programs](https://docs.aws.amazon.com/elemental-cl3/latest/ug/crud-mpts-passthrough-programs.html): Read this section if you want to include passthrough programs in the MPTS.
- [Modify MPTS](https://docs.aws.amazon.com/elemental-cl3/latest/ug/modifying-an-mpts.html)
- [Delete MPTS](https://docs.aws.amazon.com/elemental-cl3/latest/ug/delete-mpts.html)
