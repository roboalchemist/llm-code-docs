# Source: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/llms.txt

# Conductor Live API Reference

> Describes all the Conductor Live API operations. Also provides sample requests, responses, and errors for the supported web services protocols.

- [About This Manual](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/about-this-manual.html)
- [Validating Your Generated XML](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/validate-generated-xml.html)
- [Document History](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/doc-history.html)

## [Working with the API](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-the-api.html)

- [The API Protocol](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/api-protocol.html): The Conductor Live API can be accessed using HTTP or HTTPS.

### [Requests](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/requests.html)

Requests consist of a URL, a header, and a body.

- [Request URLs](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/request-url.html): The request consists of the operation, the IP address of the Conductor Live node, and resources in a parent/child structure.
- [Header Content - Standard Elements](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/header-content-standard.html): For All Requests
- [Header Content for User Authentication](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/header-content-user.html): If your cluster deployment is configured for user authentication (users must log into Conductor Live), then the header must also include:
- [Body Content](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/body-content.html): The body, if required, consists of XML content.
- [Encoding String Parameters in the URL Request](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/encoding.html)
- [Versioning](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/versioning.html)
- [Case Sensitivity of Names and Values](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/case-sensitivity.html): The names and the values of all Conductor Live attributes are case sensitive.
- [Boolean Values in Attributes](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/booleans.html): Boolean values in attributes must be entered as âtrueâ or âfalseâ. 0 and 1 are not acceptable values.
- [Arrays](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/arrays.html): In a POST or PUT, an array must include the property type="array".
- [Null Values](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/null-values.html): A null value is not the same as an empty string.

### [Using the API with User Authentication Enabled](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/using-api-with-user-authentication-enabled.html)

Your cluster deployment is configured for local or PAM user authentication (users must provide valid credentials to access Conductor Live).

- [Hashing the API Key](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/hashing-api-key.html): Construct the X-Auth-Key header as follows:
- [AuthCurl Scripts](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/authcurl-scripts.html): Two helper scripts are available to help construct these headers:
- [Authentication Error Messages](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/authentication-error-messages.html): The following errors describe why authentication requests can fail.
- [Node Changes with SSL Enabled](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/node-changes-ssl-enabled.html): When SSL (HTTPS) is enabled, the --https command must be used whenever a node is reconfigured.
- [âCleanâ Requests](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/clean-requests.html): A quick way to prepare the body for a new POST is to do a GET on an existing entity, and include the clean parameter in the request.With this parameter set to true, the GET response omits the <id> elements and other elements such as <status>, <service_name>, and <service_provider_name> that do not apply to a POST.
- [Responses](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/responses.html)
- [IDs of Entities](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/entity-ids.html): When an entity is created, it is automatically assigned an ID that is stored in the <id></id> element.


## [Commands](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands.html)

- [Profiles](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-profiles.html)
- [Channels](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-channels.html)
- [Channel Schedules](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-channel-schedules.html)
- [Bulk Tasks](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-bulk-tasks.html)
- [MPTS](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-mpts.html)
- [Members of an MPTS](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-mpts-members.html)
- [Nodes](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-nodes.html)
- [Router](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-router.html)
- [Router Inputs](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-router-inputs.html)
- [Router Outputs](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-router-outputs.html)
- [Redundancy Groups](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-redundancy-groups.html)
- [Members of a Redundancy Group](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-redundancy-group-members.html)
- [Conductor Redundancy Groups](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-conductor-redundancy-groups.html)
- [Members of a Conductor Redundancy Group](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-conductor-redundancy-group-members.html)
- [Pass Through to AWS Elemental Live](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-pass-through-aws-elemental-live.html)


## [Passing Through to AWS Elemental Live](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/pass-through-to-live.html)

- [Passthrough of Live Event POST Commands](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/passthrough-live-event-post-commands.html)
- [Passthrough of Live Event GET Commands](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/passthrough-live-event-get-commands.html)
- [Passthrough of Live System Status](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/passthrough-live-system-status.html): You can pass through a request for the status of an AWS Elemental Live system within the Conductor cluster as well.


## [Working with the Cluster](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-the-cluster.html)

### [Working with Profiles](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-profiles.html)

Topics

- [Recommended Method for Working with Profiles](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/recommended-method-working-with-profiles.html): The body of a POST or PUT profile request can contain a lot of elements (attributes of the profile).
- [POST: Create a Profile](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/post-create-a-profile.html): Create a profile.
- [Modify a Profile](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/modify-a-profile.html): You cannot modify a profile once it has been created, so there is no PUT command.
- [GET List: Get a List of Profiles](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/get-list-of-profiles.html)
- [GET: Get the Attributes of a Profile](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/get-attributes-of-profiles.html): Get the attributes of the specified profile.
- [DELETE: Delete a Profile](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/delete-a-profile.html): Delete the specified profile.

### [Working with Channels](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-channels.html)

Topics

- [POST: Create a Channel](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/post-create-a-channel.html): Create a new channel.
- [PUT: Modify the Attributes of a Channel](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/modify-attributes-of-a-channel.html): Modify the attributes of the specified channel.
- [GET List: Get List of Channels](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/get-list-of-channels.html): Get a list of all channels, including the attributes of each channel.
- [GET: Get the Attributes of a Channel](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/get-attributes-of-a-channel.html): Get the attributes of the specified channel.
- [DELETE: Delete a Channel](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/delete-a-channel.html): Delete the channel that has the specified ID.

### [Channel Scheduling](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling.html)

Conductor Live schedules channels to run either at a specific time or on a repeating schedule.

- [CRON Syntax Summary](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-cron-syntax-summary.html): The CRON expression is composed of five parts, separated by spaces, representing minute, hour, day of month, month, and day of week respectively, as illustrated below.

### [POST: Create a One-Time Schedule](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-create-a-one-time-schedule.html)

Create a schedule that runs only once.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-create-a-one-time-schedule-example.html)

### [POST: Create a Repeating Schedule](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-create-a-repeating-schedule.html)

Create a schedule that repeats regularly.

- [Examples](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-create-a-repeating-schedule-example.html): Create a schedule repeating every Monday 8:00 PM Pacific Daylight Time (UTC-07:00) for an hour:

### [POST: Activate a Schedule](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-activate-a-schedule.html)

Inactive schedules can be activated.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-activate-a-schedule-example.html): To activate schedule 17 on channel 1, use this URL.

### [DELETE: Deactivate a Schedule](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-deactivate-a-schedule.html)

Active schedules can be deactivated.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-deactivate-a-schedule-example.html): To deactivate schedule 17 on channel 1, use this URL.

### [PUT: Update a Schedule](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-update-a-schedule.html)

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-update-a-schedule-example.html): To change the name of schedule 17 on channel 1 to âNewNameâ send the following:

### [GET List: Get List of All Channel Schedules](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-get-list-of-all-channel-schedules.html)

Get a list of active and inactive schedules for a given channel.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-get-list-of-all-channel-schedules-example.html): This response shows two schedules:

### [GET: Get the Attributes of a Schedule](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-get-attributes-of-a-schedule.html)

Get the details of a specific schedule.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-get-attributes-of-a-schedule-example.html): This response shows the information for the schedule with the ID 13.

### [GET: Get Schedule Events](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-get-schedule-events.html)

Within the system, active repeating schedules result in âschedule events.â A schedule event is an individual instance of the schedule and represents one time on the calendar when the channel will run.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-get-schedule-events-example.html): This response shows the information for the schedule with the ID 15.

### [DELETE: Delete a Schedule](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-delete-a-schedule.html)

Permanently delete a schedule.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-delete-a-schedule-example.html): This request deletes the schedule with ID 5 on channel 1.

### [Performing Bulk Tasks on a Channel](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/performing-bulk-tasks-on-channel.html)

This section covers commands for the channels entity (starting and stopping channels) and for the task_report entity (monitoring the status of bulk tasks).

### [POST Start: Start One or More Channels](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/performing-bulk-tasks-start-channels.html)

Start one or more channels.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/performing-bulk-tasks-start-channels-example.html): Request

### [POST Stop: Stop One or More Channels](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/performing-bulk-tasks-stop-channels.html)

Stop one or more channels.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/performing-bulk-tasks-stop-channels-example.html): Request

### [Monitoring Bulk Tasks: GET List of Task Reports](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/performing-bulk-tasks-get-list-of-task-reports.html)

Get the list of bulk tasks.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/performing-bulk-tasks-get-list-of-task-reports-example.html): The response to this request provides information on two bulk tasks.

### [Monitoring Bulk Tasks: GET One Task Report](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/performing-bulk-tasks-get-one-task-report.html)

Get the specified task report related to one bulk task.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/performing-bulk-tasks-get-one-task-report-example.html): The response to this request provides information about the task_report with the ID 5; three of its seven actions have completed.

### [Controlling Ad Avail on a Channel](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/control-ad-avail-on-channel.html)

This section describes the commands available for controlling ad avail blanking on a channel.

- [POST Ad Avail State: Start or Stop Ad Avail on a Channel](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/control-ad-avail-on-channel-start-or-stop.html): Start or stop the ad avail blanking on a channel.

### [Working with MPTS](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts.html)

Topics

### [POST: Create an MPTS](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-create.html)

Create an MPTS output.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-create-example.html): Request

### [PUT: Modify the Attributes of an MPTS](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-modify-attributes.html)

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-modify-attributes-example.html): This request changes the bitrate and video_allocation of the MPTS with ID 3.

### [GET List: Get a List of MPTS Outputs](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-get-list-of-mpts-outputs.html)

Get the attributes and SPTS programs of all MPTS outputs.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-get-list-of-mpts-outputs-example.html): Request
- [GET: Get the Attributes of an MPTS Output](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-get-attributes-of-mpts-output.html): Get the attributes and SPTS programs of one MPTS output.

### [DELETE: Delete an MPTS Output](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-delete-mpts-output.html)

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-delete-mpts-output-example.html): This request deletes the MPTS output with the ID 2.

### [GET Status List: Get the Status of a List of MPTS Outputs](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-get-list-mpts-output-statuses.html)

Get the status of all MPTS outputs.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-get-list-mpts-output-statuses-example.html): This request returns information for the two MPTS outputs that exist in the cluster.
- [GET Status: Get the Status of an MPTS Output](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-get-status-mpts-output.html)

### [GET Bitrate: Get the Bitrate of an MPTS Output](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-get-bitrate.html)

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-get-bitrate-example.html): This request returns the statistics for the MPTS with the ID 5.

### [POST Start: Start an MPTS](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-start.html)

Start an MPTS output.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-start-example.html): This request starts the MPTS with the ID 4.

### [DELETE Stop: Stop an MPTS](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-stop.html)

Stop an MPTS output.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-stop-example.html): This request stops the MPTS with the ID 4.

### [PUT: Swap Allocation](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-swap-allocation.html)

Swap the allocation values (values of the allocation_message_priority element) in two related MPTS outputs.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-swap-allocation-example.html): This request swaps the allocation_message_priority values of the MPTS with ID 3 and the MPTS with the ID 4.

### [Working with Members of an MPTS](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts.html)

Topics

### [POST: Add an SPTS to an MPTS](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-add-spts.html)

Add an SPTS to the specified MPTS output.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-add-spts-example.html): This example shows the result of adding the channel with the ID 2 as an SPTS program with the program ID 5 in the MPTS output that has the ID 3.

### [PUT: Modify an SPTS Program](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-modify-spts-program.html)

Change the PID map and program number of the specified MPTS member.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-modify-spts-program-example.html): This example changes the MPTS member with the ID 6 in the MPTS that has the ID 2.

### [PUT: MPTS Channel Swap](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-mpts-channel-swap.html)

Swap the channel assigned to the MPTS.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-mpts-channel-swap-example.html): This request swaps channel 3 for channel 4 and uses default PID value (so does not specify any PIDs).

### [GET List: Get All SPTS of an MPTS](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-get-all-spts-of-mpts.html)

Get a list of all the SPTS programs in the specified MPTS output.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-get-all-spts-of-mpts-example.html): Request

### [GET: Get an SPTS Program](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-get-spts-program.html)

Get the specified SPTS program from the specified MPTS output.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-get-spts-program-example.html): TEXT

### [DELETE: Delete an SPTS Program](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-delete-spts-program.html)

Delete the specified SPTS program from the specified MPTS output.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-delete-spts-program-example.html): Delete the SPTS program with the ID 4 from the MPTS with the ID 2.


## [Monitoring Conductor Live](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/monitoring.html)

- [Managing Channels](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/monitoring-manage-channels.html)

### [Querying Alerts and Messages](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/monitoring-query-alerts-messages.html)

- [GET Alerts: Get a List of Alerts](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/monitoring-query-alerts-messages-get-a-list-of-alerts.html): Get a list of alerts on one or more nodes in the cluster.

### [GET Messages: Get a List of Messages](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/monitoring-query-alerts-messages-get-a-list-of-messages.html)

Get a list of messages on one or more nodes in the cluster.

### [Examples](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/monitoring-query-alerts-messages-get-a-list-of-messages-example.html)

- [Example 1](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/monitoring-query-alerts-messages-get-a-list-of-messages-example1.html): This example requests all active messages for node 2.
- [Example 2](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/monitoring-query-alerts-messages-get-a-list-of-messages-example2.html): The following example requests all active code 30 (node activated) messages from node 13, limiting the responses to 20per page.

### [GET System Information: Get a List of System Details](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/monitoring-query-alerts-messages-get-a-list-of-system-details.html)

Get a list of details about the Conductor Live system, including memory, CPU, and network information.

- [Example](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/monitoring-query-alerts-messages-get-a-list-of-system-details-example.html)


## [Configuring the Cluster](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/configuring-the-cluster.html)

### [Setting up Nodes](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-nodes.html)

Topics

- [POST: Add a Node to the Cluster](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-nodes-add-note-to-cluster.html)
- [GET List: Get a List of Nodes in the Cluster](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-nodes-get-list-of-nodes.html): Get the list of the nodes in the cluster, including the Conductor Live node and the individual AWS Elemental Live and AWS Elemental Statmux nodes.
- [GET: Get the Attributes of a Node](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-nodes-get-attributes-of-node.html): Get the attributes on the specified node.
- [DELETE: Remove a Node from the Cluster](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-nodes-remove-node.html): Remove the specified node from the Conductor Live cluster.

### [Setting Up Routers](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-routers.html)

The Router element holds information about a router that is attached to SDI cards on the AWS Elemental Live node.

- [POST: Create a Router](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-routers-create.html): This request creates a new router to correspond to a router that is connected to HD-SDI inputs on one or more AWS Elemental Live nodes. (The same router can have connections to several nodes.)
- [PUT: Modify a Router](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-routers-modify.html): Modify the attributes of the specified router.
- [GET List: Get a List of Routers](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-routers-get-a-list-of-routers.html): Get a list of all video SDI routers, including the data that is contained in the Router Input and Router Output entities.
- [GET: Get Router Attributes](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-routers-get-router-attributes.html): Get the attributes of the specified video SDI router, including the data that is contained in the Router Input and Router Output.
- [DELETE: Delete a Router](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-routers-delete.html): Deletes the specified router (identified by its internal router ID) and the associated inputs and outputs.

### [Setting Up Router Inputs](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-inputs.html)

The Router Inputs entity holds information about the router inputs you are using with an AWS Elemental Live node.

- [POST: Create a Router Input](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-inputs-create.html): This request creates a new input for the specified router.
- [PUT: Modify a Router Input](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-inputs-modify.html): Modify the attributes of the specified input on the specified router.
- [GET List: Get a List of Router Inputs](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-inputs-get-a-list.html): Get the list of all the inputs for the specified router.
- [GET: Get Attributes of a Router Input](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-inputs-get-attributes.html): Get the attributes of the specified input on the specified router.
- [DELETE: Delete a Router Input](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-inputs-delete.html): Delete the specified input on the specified router.

### [Setting Up Router Outputs](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-outputs.html)

The Router Outputs entity holds information about each router output that is connected to an SDI card on an AWS Elemental Live appliance.

- [POST: Create a Router Output](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-outputs-create.html): Create a new output for the specified router.
- [PUT: Modify a Router Output](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-outputs-modify.html): Modify the attributes of the specified output on the specified router.
- [GET List: Get Router Output List](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-outputs-get-list.html): Get the list of outputs for the specified router.
- [GET: Get Attributes of a Router Output](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-outputs-get-attributes.html): Get the attributes of the specified output on the specified router.
- [DELETE: Delete a Router Output](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-outputs-delete.html): Delete the specified output on the specified router.

### [Setting Up Redundancy Groups](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-redundancy-groups.html)

Topics

- [POST: Create a Redundancy Group](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-redundancy-groups-create.html): Create a new redundancy group for AWS Elemental Live or AWS Elemental Statmux redundancy group with the specified attributes.
- [PUT: Modify a Redundancy Group](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-redundancy-groups-modify.html): Change the name of the specified redundancy group.
- [GET List: Get a List of Redundancy Groups](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-redundancy-groups-get-a-list.html): Get a list of all redundancy groups, including the attributes of each group.
- [GET: Get Attributes of a Redundancy Group](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-redundancy-groups-get-attributes.html): Get the attributes of the specified redundancy group.
- [DELETE: Delete a Redundancy Group](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-redundancy-groups-delete.html): Delete the redundancy group that has the specified ID.

### [Setting Up Members of a Redundancy Group](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-members-redundancy-group.html)

Topics

- [POST: Add a Node to a Redundancy Group](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-members-redundancy-group-add-node.html): Add a node to the specified redundancy group and assign the nodeâs role as active or backup.
- [PUT: Change Role of a Member of a Redundancy Group](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-members-redundancy-group-change-role-of-member.html): Modify the role of the specified node in the specified redundancy group.
- [GET List: Get a List of Redundancy Group Members](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-redundancy-groups-get-list-of-members.html): Get the list of the nodes that are members of the specified redundancy group.
- [GET: Get the Attributes of a Redundancy Group Member](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-redundancy-groups-get-attributes-of-members.html): Get the attributes of the specified member in the specified redundancy group.
- [DELETE: Remove a Node from a Redundancy Group](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-redundancy-groups-remove-node.html): Remove the node with the specified member ID from the specified redundancy group.
- [POST Initiate Failover](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-redundancy-groups-initiate-failover.html): Initiate failover of the specified node.

### [Setting Up a Conductor Redundancy Group](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-conductor-redundancy-group.html)

Topics

- [POST: Create a Conductor Redundancy Group](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-conductor-redundancy-groups-create.html): Create a new Conductor redundancy group with the specified attributes.
- [PUT: Modify a Conductor Redundancy Group](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-conductor-redundancy-groups-modify.html): Change the name, VIP or VRID of the specified Conductor redundancy group.
- [GET: Get the Attributes of the Conductor Redundancy Group](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-conductor-redundancy-groups-get-attributes.html): Get a list of all Conductor redundancy groups, including the attributes of each group.
- [DELETE: Delete a Conductor Redundancy Group](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-conductor-redundancy-groups-delete.html): Delete the Conductor redundancy group that has the specified ID.
- [POST Enable: Enable Conductor Redundancy Group](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-conductor-redundancy-groups-enable.html): Enable Conductor Redundancy mode (high availability) on the two Conductor nodes in the Conductor redundancy group in order to enable the failover mode for the Conductor nodes.
- [DELETE Disable: Disable Conductor Redundancy Group](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-conductor-redundancy-groups-disable.html): Disable Conductor Redundancy mode (high availability) on the two Conductor nodes in the Conductor redundancy group.

### [Setting Up Members of a Conductor Redundancy Group](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-members-conductor-redundancy-group.html)

Topics

- [POST: Add a Node to a Conductor Redundancy Groups](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-members-conductor-redundancy-group-add-node.html): Add a Conductor node to the specified Conductor redundancy group.
- [PUT: Modify a Member of a Conductor Redundancy Group](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-members-conductor-redundancy-group-modify.html): There is no PUT for members of a Conductor redundancy group.
- [GET List: Get a List of Conductor Redundancy Group Members](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-members-conductor-redundancy-group-get-list-of-members.html): Get the list of the nodes that are members of the specified Conductor redundancy group.
- [GET: Get the Attributes of a Conductor Redundancy Group Member](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-members-conductor-redundancy-group-get-attributes.html): Get the attributes of the specified member in the specified Conductor redundancy group.
- [DELETE: Remove a Node from the Conductor Redundancy Group](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-members-conductor-redundancy-group-remove-node.html): Remove the Conductor node with the specified member ID from the Conductor redundancy group.

### [Backing Up the Conductor Database](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/back-up-conductor-database.html)

Topics

- [PUT: Modify Database Backup Settings](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/back-up-conductor-database-modify-settings.html): You can view and modify the current backup settings for the conductor database on the web UI at Settings>Backups.
- [POST: Backup Database Now](https://docs.aws.amazon.com/elemental-cl3/latest/apireference/back-up-conductor-database-backup-now.html): To initiate an immediate database backup, send the following command.
