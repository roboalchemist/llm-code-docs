# Source: https://rustdesk.com/docs/en/self-host/rustdesk-server-pro/strategy/

# Strategy

Strategy is a tool for RustDesk administrators to update the security options of client settings pages in bulk. Administrators can create different strategies and apply them to different devices.

## Create Strategies

You can create a new strategy by clicking the `+` button and perform various actions on the strategy by hovering over it and clicking the menu.

In the pop-up menu, you can choose to `Enable` or `Disable` the strategy, `Rename`, `Duplicate` or `Delete` it. Additionally, you can click `Edit Devices` to modify the devices applied to that strategy or click `Edit Users` to modify the users applied to that strategy.

On the right side of the strategy menu, you can see the number of devices actually applied to the strategy, taking into account the priority of the strategy.

## Device Strategy, User Strategy and Device Group Strategy

Strategies are applied according to the following priority order:

- Device Strategy (Highest priority)
- User Strategy
- Device Group Strategy (Lowest priority)

Each device can only be managed by one strategy at a time. The priority system works as follows:

- Device strategies take priority over both user strategies and device group strategies
- User strategies take priority over device group strategies
- Device group strategies apply to all devices in the device group that don&rsquo;t have a device strategy or user strategy assigned

## Edit Devices

When you click the `Edit Devices` menu, an editing dialog box displaying all the devices will open. You can change the selection status of the checkboxes and then click the `Save` button to apply the device changes made on the current page. If you need to modify devices on other pages, please navigate to those pages. You can also use the drop-down menu in the upper right corner to filter devices.

Strategy column format: device strategy/user strategy/device group strategy, or &ldquo;-&rdquo; for the default strategy.

Here is an example of the dialog box that appears when you click `Edit Devices` on the &ldquo;demo1&rdquo; menu. In this example, the device &ldquo;1981241962&rdquo; is applied to the &ldquo;demo3&rdquo; strategy; The device &ldquo;1279471875&rdquo; is applied to the &ldquo;demo2&rdquo; strategy; The device &ldquo;a123456&rdquo; is applied to the &ldquo;demo1&rdquo; strategy; The device &ldquo;1227624460&rdquo; is applied to the default strategy.
.

## Edit Users

When you click the `Edit Users` menu, an editing dialog box displaying all the users will open. You can change the selection status of the checkboxes and then click the `Save` button to apply the user changes made on the current page. If you need to modify users on other pages, please navigate to those pages. You can also use the drop-down menu in the upper right corner to filter users.

Here is an example of the dialog box that appears when you click `Edit Users` on the &ldquo;demo2&rdquo; menu. In this example, the user &ldquo;admin&rdquo; is applied to the &ldquo;default&rdquo; strategy; The user &ldquo;user1&rdquo; is applied to the &ldquo;demo2&rdquo; strategy; The user &ldquo;user2&rdquo; is applied to the &ldquo;demo3&rdquo; strategy.

## Edit Device Groups

When you click the `Edit Device Group` menu, an editing dialog box displaying all the device groups will open. You can change the selection status of the checkboxes and then click the `Save` button to apply the device group changes made on the current page. If you need to modify device groups on other pages, please navigate to those pages. You can also use the drop-down menu in the upper right corner to filter device groups.

Here is an example of the dialog box that appears when you click `Edit Device Group` on the &ldquo;demo1&rdquo; menu. In this example, the device group &ldquo;device_group1&rdquo; is applied to the &ldquo;demo1&rdquo; strategy; The device group &ldquo;group2&rdquo; is applied to the &ldquo;demo2&rdquo; strategy; The device group &ldquo;group3&rdquo; is applied to the &ldquo;default&rdquo; strategy.

## Strategy Synchronization

Each device can only be managed by one strategy, and if that strategy is disabled, the device will not be managed by any strategy. When synchronizing strategies, RustDesk records the local and server strategy timestamps to determine whether synchronization is necessary. That is, after strategy synchronization is complete:

- If the user changes some options, the client will use the user&rsquo;s options.
- If the administrator changes the strategy content, the client&rsquo;s options will be synchronized.
- If the administrator changes the strategy to which the device belongs, the client&rsquo;s options will be synchronized.

## Edit Strategies

At the bottom of the strategy, click `Edit`, make modifications and click `Submit`. The strategy will be synchronized to devices within 30 seconds.