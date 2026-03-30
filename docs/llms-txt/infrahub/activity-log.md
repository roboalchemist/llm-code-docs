# Source: https://docs.infrahub.app/topics/activity-log.md

# Activity log

Changes (events) in Infrahub are documented in the **Activity log**. It helps you see which objects were impacted, when a change was made, and who made it. It can be used to troubleshoot unforeseen changes, audit previous operations, and comprehend the order of updates across various branches.

Permissions

Because figuring out who may view which changes requires complicated query requirements, we have currently set aside the permission framework for this functionality.

The activity log, in general, compiles and arranges events from several branches and objects into a single timeline:

* **Global view**: A consolidated list of all branch-wide activities (events).
* **Object-level view**: A timeline that is particular to a single object and only displays events that are pertinent to that object.
* **Filtering**: You can narrow down your search using a variety of filters (by branch, event type, account, principal node, linked node, date range).
* **Nested / child events**: Cascade actions are observed when specific top-level events trigger additional child events.

## Accessing the activity log[​](#accessing-the-activity-log "Direct link to Accessing the activity log")

The activity log can be accessed in any of two ways: globally or at the object level.

1. **Global activity log**:

   <!-- -->

   * Menu location: In the main navigation, go to **Activity** → **Activity log**.
   * URL: `https://<your-instance>/activities`

![Global Activity log page](/assets/images/activity_log_global-c921297d857c7c80a446778b0e00f176.png)

Time and date

The activity log's date and time are determined by the local time in your browser.

Child Events

Events containing child events have an extra (blue) icon at the end of the line.

2. **Object-level activity log**:
   <!-- -->
   * Node / object detail pages: Within a node's detail view (for example an IP address or device), you'll see a right-hand "Activity logs" panel or a separate tab.

![Device detail page with Activity logs panel](/assets/images/activity_log_device-28ba8f590e6cebb91c7836eb83024424.png)

## Filters and search[​](#filters-and-search "Direct link to Filters and search")

There are several ways to hone your view in the global activity log:

* **Branch**: Select the branch you wish to view the events in, such as `main`.
* **Event type**: Filter by categories such as `Node Created`, `Branch Deleted`. You can find more information in the [Infrahub Events](/reference/infrahub-events.md) topic.
* **Account / user**: Only display events that have been initiated by a certain account.
* **Primary / related node**: Highlight activities associated with a specific node.
* **Has children**: Whether a certain occurrence led to other smaller ones.
* **Date range**: Set a start and end time and date for the timeline.

![Activity logs filters - primary](/assets/images/activity_log_global_filters_primary-b081a1645dfbf07b005a1a15d8de4c13.png) ![Activity logs filters - children](/assets/images/activity_log_global_filters_children-317290318c3ae0a518b903b2b775b8d4.png)

## Viewing event details[​](#viewing-event-details "Direct link to Viewing event details")

If you choose **View more** from the global or object-level list, a separate detail page or popover will show up. Additional details are shown in this view, such as:

* **Event ID**: A unique UUID referencing the event.
* **Event type**: The type of the event, for example, `infrahub.node.updated`. You can find more information in the [Infrahub Events](/reference/infrahub-events.md) topic.
* **Occurred at**: The exact moment the incident took place
* **Account**: The account that carried out the activity.
* **Primary node**: The primary object that the event affects.
* **Related nodes**: Additional affected objects.
* **Changes**: Any before and after adjustments to updated attributes, if any

![Activity details page with children](/assets/images/activity_log_global_details_children-406d8ed65247deed14dc35ed67fc04f4.png) ![Activity logs details popover](/assets/images/activity_log_device_popover-2b36b6d169805caf37fda27eaf4e2977.png)
