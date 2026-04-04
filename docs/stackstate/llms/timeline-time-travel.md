# Source: https://archivedocs.stackstate.com/5.1/use/stackstate-ui/timeline-time-travel.md

# Timeline and time travel

## Overview

The timeline at the bottom of the StackState UI allows you to travel back in time to the state of the topology at a specific point in the past. You can then navigate through all telemetry available for the selected topology snapshot. Health and events charts in the timeline give an overview of the state of the topology during the selected telemetry interval.

![Timeline](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-e3fcd32d013c0f05707d982e36fd6b2681a0f1b9%2Fv51_timeline.png?alt=media)

## Timeline

### Telemetry interval

The telemetry interval specifies the time window for which events, metrics and traces are available in the StackState perspectives. It runs from left to right on the timeline.

![Telemetry interval](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-34cb5bb852b3cc202fd2651cbdf5b441741d6ddc%2Fv51_telemetry_interval.png?alt=media)

The selected telemetry interval can be either relative (live mode), or set to a custom telemetry interval (time travel mode). By default, the telemetry interval is set to a relative telemetry interval - in live mode and showing telemetry from the last hour. You can zoom in/out or set a custom telemetry interval to view telemetry from a specific point in time.

#### Set the telemetry interval

{% hint style="info" %}

* The telemetry interval can be a maximum of 6 months.
* When a custom telemetry interval is set for the telemetry interval, StackState will pause the [topology time](#topology-time) and enter [time travel mode](#time-travel).
  {% endhint %}

The telemetry interval can be set in the following ways:

* **Zoom in**

![Click and drag on the timeline to set a custom telemetry interval on your selection](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-0ce639a8b3a80b1918f3a018809b549179722622%2Fv51_timeline_click_drag.png?alt=media)

* **Zoom out**

![Click the magnifying glass to double the size of the telemetry interval](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-5b48031c24a0c0d908824e0bd0d4f31a64a5da4c%2Fv51_telemetry_interval_zoom_out.png?alt=media)

* **Use the telemetry interval jumper arrows**

![Click the time jumper arrows to move the telemetry interval backwards or forwards through time](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-0d5097cb9edf92dad96915cf3690f5b486ea4508%2Fv51_telemetry_interval_jumper.png?alt=media)

* **Set a relative or custom telemetry interval**

![Use the popup "Set the telemetry interval" to specify a telemetry interval](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-9cb0492b41a1c3caa31337d7c87303afe3a56a80%2Fv51_timeline_telemetry_interval.png?alt=media)

{% hint style="success" %}
You can [configure the default telemetry interval](https://archivedocs.stackstate.com/5.1/configure/telemetry/custom_telemetry_interval).
{% endhint %}

### Topology time

The topology and all telemetry displayed in StackState are based on a snapshot of the IT infrastructure. The moment from which this snapshot is taken is specified by the topology time. By default, StackState is in live mode with the topology time set to the current time. You can [time travel](#time-travel) to a previous state of the topology by selecting a custom topology time.

![Topology time](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-4190c8ca3c234b844f84888b9bf11402be240869%2Fv51_topology_time.png?alt=media)

On the timeline, the selected topology time is indicated by the playhead - a black line with the current topology time at the top. It's also specified in the **Topology time** box at the top of the timeline.

#### Set the topology time

The topology time can be set in the following ways:

* **Click on the timeline**

![Click anywhere on the timeline to set the topology time to that moment](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-a91d35fe48ad1493eb1fe29ae603cf7137f38090%2Fv51_topology_time_timeline.png?alt=media)

* **Use the topology time jumper arrows**

![Click the topology time jumper arrows to move the topology time backwards or forwards in time to the next set of events](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-a506c21f98d0851d77ed11bc0075e7321c0a8c0e%2Fv51_topology_time_jumper.png?alt=media)

* **Set a custom topology time**

![Use the popup "Set the topology time" to specify a topology time](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-ffdb1417f6231627a52421fd38dd709b2b5af944%2Fv51_topology_time_popup.png?alt=media)

* **Click a timestamp**

![Click a timestamp to jump to that specific topology time](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-62f346890f15b98965a17403de48041e8a1ce76d%2Fv51_topology_time_timestamp.png?alt=media)

#### Topology time outside the telemetry interval

If the selected topology time is a time outside the currently selected [telemetry interval](#telemetry-interval), the message "The topology time is out of the current telemetry interval" will be displayed and the **Topology time** box at the top of the timeline will be highlighted black. As the timeline shows the telemetry interval from left to right, the playhead indicating the current topology time won't be visible on the timeline.

![Topology time outside telemetry interval](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-110996c90c7f075141e1cbc4e1059008f65034b5%2Fv51_topology_time_outside_telemetry_interval.png?alt=media)

You can still browse topology and telemetry as expected:

* In the [Topology Perspective](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/perspectives/topology-perspective) the state of the topology at the selected topology time is visualized.
* In all perspectives, telemetry is displayed that was generated in the selected telemetry interval and relates to the topology elements that existed at the selected topology time.

#### Live mode

To stop time travelling and return the topology time to live mode, click **Go live** or **BACK TO LIVE** at the top of the screen.

![Go live](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-ba39d90e6e05d981b6ce9c443450714809e444d0%2Fv51_timeline_go_live.png?alt=media)

### Health

The health state of a view during the selected telemetry interval is displayed as a color in the timeline **Health** line.

Health state information is available when [health state is enabled](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/views/configure-view-health) for the current view as long as the topology displayed results from the original topology filter saved in the view.

{% hint style="info" %}
If the topology filters have been edited and not saved, no health state information will be available.
{% endhint %}

When health state information isn't available, a gray line is displayed.

![Health state not available](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-aa38135134262971d3e0c71e18c58862fa5b25f0%2Fv51_timeline_no_health_state.png?alt=media)

### Events

The **Events** line in the timeline shows a bar chart with the number of events generated at each point in time. This helps you to see moments in the past with a lot of activity. Note that only events generated by topology elements that existed at the selected [topology time](#topology-time) are displayed.

To zoom in on an event bar of interest, click and drag to select a smaller telemetry interval around it on the timeline.

![Click and drag to select a telemetry interval](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-0ce639a8b3a80b1918f3a018809b549179722622%2Fv51_timeline_click_drag.png?alt=media)

{% hint style="info" %}
A single click on the timeline will move the playhead to this point in time, and thus time travel to the state of the topology at the selected [topology time](#topology-time). Only events generated by topology elements that existed at the newly selected topology time will now be displayed.
{% endhint %}

## Time travel

In each of the StackState perspectives, you can either be in live mode or in the past. In live mode, StackState will constantly poll for new data. When you time travel through topology or telemetry, you are effectively working with a snapshot of your infrastructure. The data available is based on two selections:

* [Topology time](#topology-time) - a specific moment in time for which you want to fetch a snapshot of your IT infrastructure.
* [Telemetry interval](#telemetry-interval) - the time range for which you want to see telemetry and traces.

Let's imagine a concrete scenario:

* You received an event notification saying that your payment processing application isn't able to process any payments right now, and your customers aren't being served.
* In StackState, you can go to the moment in time when the components that make up the CRITICAL path of payment processing turned to a CRITICAL state. That moment corresponds to the point in time for which you will fetch the snapshot of your IT infrastructure - the topology time.
* You can then select to see the hours that preceded that moment to fetch the telemetry that will hopefully point you to the root cause of your problem - the telemetry interval.

StackState will enter time travel mode whenever a custom topology time is selected, the **Pause** button is clicked, or a custom telemetry interval is set for the telemetry interval. When StackState is in time travel mode:

* You are effectively working with a snapshot of your infrastructure.
* Telemetry is available for components that were part of the topology at the selected topology time only.
* If a relative telemetry interval was selected in live mode, this is frozen as a custom telemetry interval relative to the moment at which time travelling began.

To stop time travelling and return to live mode, click **Go live** or **BACK TO LIVE** at the top of the screen.

![Go live](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-ba39d90e6e05d981b6ce9c443450714809e444d0%2Fv51_timeline_go_live.png?alt=media)
