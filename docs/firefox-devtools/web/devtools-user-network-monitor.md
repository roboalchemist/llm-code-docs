# Source: https://firefox-source-docs.mozilla.org/devtools-user/network_monitor

Title: Network Monitor — Firefox Source Docs documentation

URL Source: https://firefox-source-docs.mozilla.org/devtools-user/network_monitor

Markdown Content:
The Network Monitor shows you all the HTTP requests Firefox makes (for example, when it loads a page, or due to [XMLHttpRequests](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)), how long each request takes, and details of each request.

Opening the Network Monitor[](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor#opening-the-network-monitor "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

There are a few different ways to open the Network Monitor:

*   Press Ctrl + Shift + E (Cmd + Opt + E on a Mac).

*   Select the _Network_ panel in the Web Developer Tools, accessible from the Browser Tools submenu

*   Click the wrench icon [![Image 1: image1](https://firefox-source-docs.mozilla.org/_images/wrench-icon.png)](https://firefox-source-docs.mozilla.org/_images/wrench-icon.png), which is in the main toolbar or under the Hamburger menu [![Image 2: image2](https://firefox-source-docs.mozilla.org/_images/hamburger1.png)](https://firefox-source-docs.mozilla.org/_images/hamburger1.png), then select “Network”.

The Network Monitor will appear at the bottom of the browser window. When it first opens, the Network Monitor does not show request information. The just opened tool looks like this:

![Image 3: ../../_images/network_monitor_new.png](https://firefox-source-docs.mozilla.org/_images/network_monitor_new.png)
Either action causes the Network Monitor to begin monitoring network activity. Once the tool is monitoring network requests, the display looks like this:

![Image 4: ../../_images/network_monitor.png](https://firefox-source-docs.mozilla.org/_images/network_monitor.png)
When it is actively monitoring activity, the Network Monitor records network requests any time the Toolbox is open, even if the Network Monitor itself is not selected. This means you can start debugging a page in, for example, the Web Console, then switch to the Network Monitor to see network activity without having to reload the page.

UI overview[](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor#ui-overview "Link to this heading")
------------------------------------------------------------------------------------------------------------------------

The UI is divided into four main pieces:

*   The main screen contains the [toolbar](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/toolbar/index.html), the [network request list](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/request_list/index.html), and the [network request details pane](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/request_details/index.html):

![Image 5: ../../_images/network_monitor_closeup.png](https://firefox-source-docs.mozilla.org/_images/network_monitor_closeup.png)
*   The [performance analysis](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/performance_analysis/index.html) view is a separate screen:

![Image 6: ../../_images/network_performance.png](https://firefox-source-docs.mozilla.org/_images/network_performance.png)
Working with the network monitor[](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor#working-with-the-network-monitor "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following articles cover different aspects of using the network monitdor:

*   [Toolbar](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/toolbar/index.html)

*   [Network overrides](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/network_overrides/index.html)

*   [Network request list](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/request_list/index.html)

*   [Network request details](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/request_details/index.html)

*   [Network traffic recording](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/performance_analysis/index.html)

*   [Throttling](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/throttling/index.html)

*   [Inspecting web sockets](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/inspecting_web_sockets/index.html)

*   [Inspecting server-sent events](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/inspecting_server-sent_events/index.html)
