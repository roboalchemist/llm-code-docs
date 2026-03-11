# Source: https://archivedocs.stackstate.com/5.1/use/metrics/set-telemetry-stream-priority.md

# Set telemetry stream priority

## Overview

The telemetry streams associated with an element are displayed in the right panel details tab when an element is selected to show its detailed information - **Component details** or **Direct relation details** depending on the element type that you selected. Telemetry streams are displayed in order of telemetry stream priority. There are four levels of priority: `High`, `Medium`, `Low`, and `None`. By default, all streams have priority set to `None`.

Stream priority is used in StackState to help determine the following:

* The order in which streams are displayed in the details tab **Telemetry** list. Streams are ordered first by priority (highest at the top) and then alphabetically.
* The streams that are shown as [Top metrics](https://archivedocs.stackstate.com/5.1/use/metrics/top-metrics) in the component context menu - this is the pop-up displayed when you hover the mouse pointer over a component in the Topology Perspective. The most recent metric received from the first three metric streams in the **Telemetry** list will be displayed.
* The order in which streams are displayed in the [Metrics Perspective](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/perspectives/metrics-perspective).
* The [streams selected for monitoring by the Autonomous Anomaly Detector](https://archivedocs.stackstate.com/5.1/stackpacks/add-ons/aad#how-are-metric-streams-selected).

## Set the telemetry stream priority

To change the priority of a specific stream, follow the instructions below.

### 1. Select a component to display detailed information

Locate the component that you want to edit Telemetry streams for. Select the component to open detailed information about it in the right panel details tab - **Component details**. See the screenshot below:

![Detailed component information](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-b7a010ea524fd780d92aa5608414a9335b284168%2Fv51_component_details.png?alt=media)

### 2. Choose the telemetry streams to prioritize

Components can have multiple Telemetry streams. They're presented in a list, so not all of them are visible at first. Let's say that instead of `BytesReceivedRate`, you want to see `PacketsReceivedRate` right after the `basic_health` stream. Click the **...** menu in the top-right corner of the `basic_health` stream and choose **Edit**:

![Edit telemetry stream](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-9821c82d22dca980096f4ed6b788f39b3abc7caa%2Fv51_telstream_edit.png?alt=media)

### 3. Set stream priority

In the `basic_health` stream edit screen, set the Priority field to `High`, as this stream should be presented at the top of the list. Click **Save** and confirm the change:

![Edit basic\_health](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-9c068df74941a183f6460f3b37166fe7b32620c3%2Fv51_edit_basic_health.png?alt=media)

Now navigate to the `PacketsReceivedRate` stream and open the stream editing screen. Set the Priority field here to `Medium`:

![Edit packetsReceiveRate](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-695c08748efa3e5c600d5a99a5e92d676aa87810%2Fv51_edit_medium.png?alt=media)

All streams have their priority set to `None` by default, so the `PacketsReceivedRate` stream will now be displayed above them and below the `basic_health` stream, which has its priority set to `High`.
