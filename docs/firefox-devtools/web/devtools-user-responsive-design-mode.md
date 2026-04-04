# Source: https://firefox-source-docs.mozilla.org/devtools-user/responsive_design_mode

Title: Responsive Design Mode — Firefox Source Docs documentation

URL Source: https://firefox-source-docs.mozilla.org/devtools-user/responsive_design_mode

Markdown Content:
[Responsive design](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Responsive/responsive_design_building_blocks) is the practice of designing a website so it looks and works properly on a range of different devices — particularly mobile phones and tablets as well as desktops and laptops.

The most obvious factor here is screen size, but there are other factors as well, including the pixel density of the display and whether it supports touch. Responsive Design Mode gives you a simple way to simulate these factors, to test how your website will look and behave on different devices.

Toggling Responsive Design Mode[](https://firefox-source-docs.mozilla.org/devtools-user/responsive_design_mode#toggling-responsive-design-mode "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are three ways to toggle Responsive Design Mode:

*   From the Firefox menu: Select **Responsive Design Mode** from the **Browser Tools** submenu in the Firefox Menu (or **Tools** menu if you display the menu bar or are on macOS).

*   From the Developer Tools toolbox: Press the **Responsive Design Mode** button in the [Toolbox’s toolbar](https://firefox-source-docs.mozilla.org/devtools-user/tools_toolbox/index.html#tools-toolbox-toolbar)

*   From the keyboard: Press Ctrl + Shift + M (or Cmd + Opt + M on macOS).

Controlling Responsive Design Mode[](https://firefox-source-docs.mozilla.org/devtools-user/responsive_design_mode#controlling-responsive-design-mode "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

With Responsive Design Mode enabled, the content area for web pages is set to the screen size for a mobile device. Initially, it’s set to 320 x 480 pixels.

Note

The device you select when in Responsive Design Mode and the orientation (portrait or landscape) is saved between sessions.

![Image 1: ../../_images/responsive_ui.png](https://firefox-source-docs.mozilla.org/_images/responsive_ui.png)
Information for the selected device is centered over the display. From left to right, the display includes:

*   _Name of the selected device_ - A drop-down list that includes whatever devices you have selected from the Device Settings screen.

*   _Screen size_ - You can edit the width and height values to change the device size by editing a number directly or using the Up and Down keys to increase or decrease the value by 1 pixels on each keypress or hold and Shift to change the value by 10.

    *   The mouse wheel changes the size values by 1 pixel at a time

    *   You can also change the device’s screen size by grabbing the bottom-right corner of the viewport and dragging it to the size you want.

*   _Orientation (portrait or landscape)_ - This setting persists between sessions

*   _DPR (pixel ratio)_ - To set a specific DPR, you need to create a custom device

*   _Throttling_ - A drop-down list where you can select the connection throttling to apply, for example 2G, 3G, or LTE

*   _Enable/Disable touch simulation_ - Toggles whether or not Responsive Design Mode simulates touch events. While touch event simulation is enabled, mouse events are translated into [touch events](https://developer.mozilla.org/en-US/docs/Web/API/Touch_events); this includes translating a mouse-drag event into a touch-drag event. (Note that when touch simulation is enabled, this toolbar icon is blue; when simulation is disabled, it is black).

On the right end of the screen, three buttons allow you to:

*   _Camera button_ - take a screenshot

    *   Screenshots are saved to Firefox’s default download location.

    *   If you checked “Screenshot to clipboard” in the Developer Tools [Settings](https://firefox-source-docs.mozilla.org/devtools-user/settings/index.html) page, then the screenshot will be copied to the system clipboard.

*   _Settings button_ - Opens the RDM settings menu

*   _Close button_ - closes RDM mode and returns to regular browsing

The Settings menu includes the following commands:

![Image 2: ../../_images/responsive_setting_menu.png](https://firefox-source-docs.mozilla.org/_images/responsive_setting_menu.png)
*   _Left-align Viewport_ - when checked moves the RDM viewport to the left side of the browser window

*   _Show user agent_ - when checked displays the user agent string

*   The final two options define when the page is reloaded:

    *   _Reload when touch simulation is toggled:_ when this option is enabled, the page is reloaded whenever you toggle touch support.

    *   _Reload when user agent is changed:_ when this option is enabled, the page is reloaded whenever the user agent is changed.

Reloading on these changes can be helpful because certain page behaviors would otherwise not be applied. For example, many pages check for touch support on load and only add event handlers if it is supported, or only enable certain features on certain browsers.

However, if you are not interested in examining such features (maybe you are just checking the overall layout at different sizes), these reloads can waste time and possibly result in the loss of productive work, so it is useful to be able to control these reloads.

Now when you change such settings for the first time, you are given a warning message that tells you these reloads are no longer automatic, and informed about how you can make them automatic. For example:

![Image 3: ../../_images/page-reload-warning.png](https://firefox-source-docs.mozilla.org/_images/page-reload-warning.png)
Developer Toolbox with RDM[](https://firefox-source-docs.mozilla.org/devtools-user/responsive_design_mode#developer-toolbox-with-rdm "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

You can show or hide the Developer Tools toolbox independently of toggling Responsive Design Mode itself:

![Image 4: ../../_images/rdmdevtools.png](https://firefox-source-docs.mozilla.org/_images/rdmdevtools.png)
While Responsive Design Mode is enabled, you can continue browsing as you normally would in the resized content area.

Device selection[](https://firefox-source-docs.mozilla.org/devtools-user/responsive_design_mode#device-selection "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

Just above the viewport there is a label “no device selected”; click this to see a list of device names. Select a device, and Responsive Design Mode sets the following properties to match the selected device:

*   Screen size

*   Device pixel ratio (the ratio of device physical pixels to device-independent pixels)

*   Touch event simulation

Additionally, Firefox sets the [User-Agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent) HTTP request header to identify itself as the default browser on the selected device. For example, if you’ve selected an iPhone, then Firefox identifies itself as Safari. The [navigator.userAgent](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/userAgent) property is set to the same value.

The devices listed in the drop-down are just a subset of the devices that can be selected. At the end of the drop-down, there is an item labeled **Edit list**. Select this to see a panel containing all the choices, which enables you to check the devices you want to see in the drop-down.

### Creating custom devices[](https://firefox-source-docs.mozilla.org/devtools-user/responsive_design_mode#creating-custom-devices "Link to this heading")

You can create and save custom devices in Responsive Design Mode by clicking the **Add Custom Device** button. Each device can have its own:

*   Name

*   Size

*   DevicePixelRatio

*   User Agent String

*   Touch Screen

Also, you can preview the properties of existing devices by hovering over the name in the device modal, where they display in a tooltip.

Network throttling[](https://firefox-source-docs.mozilla.org/devtools-user/responsive_design_mode#network-throttling "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

If you do all your development and testing using a very fast network connection, users may experience problems with your site if they are using a slower connection. In Responsive Design Mode, you can instruct the browser to emulate, very approximately, the characteristics of various different types of networks.

The characteristics emulated are:

*   Download speed

*   Upload speed

*   Minimum latency

The table below lists the numbers associated with each network type, but please do not rely on this feature for exact performance measurements; it’s intended to give an approximate idea of the user experience in different conditions.

| Selection | Download speed | Upload speed | Minimum latency (ms) |
| --- | --- | --- | --- |
| GPRS | 50 Kb/s | 20 Kb/s | 500 |
| Regular 2G | 250 Kb/s | 50 Kb/s | 300 |
| Good 2G | 450 Kb/s | 150 Kb/s | 150 |
| Regular 3G | 750 Kb/s | 250 Kb/s | 100 |
| Good 3G | 1.5 Mb/s | 750 Kb/s | 40 |
| Regular 4G/LTE | 4 Mb/s | 3 Mb/s | 20 |
| DSL | 2 Mb/s | 1 Mb/s | 5 |
| Wi-Fi | 30 Mb/s | 15 Mb/s | 2 |
| Offline | 0 Mb/s | 0 Mb/s | 5 |

To select a network, click the list box that’s initially labeled “No throttling”:

![Image 5: ../../_images/rdm_throttling.png](https://firefox-source-docs.mozilla.org/_images/rdm_throttling.png)
