# Source: https://docs.axonius.com/docs/configuring-discovery-settings.md

# Configuring Discovery Settings

Use Discovery Settings to configure your settings for [Global Discovery cycle](/docs/discovery-cycle). The discovery cycle pulls and correlates data from all adapters.

**To open the Discovery Settings:**

1. From the top right corner of any page, click ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **Lifecycle**, and select **Discovery**.

![DiscoverySettings](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DiscoverySettings.png)

* **Discovery Schedule** *(required, default: Every x hours)* - Select the discovery schedule option. Note that all times are in UTC.
  * **Every x hours** -  Select this option to run discovery cycles every number of hours defined in **Repeat scheduled discovery every (hours)**.
    * The  discovery cycle start time is determined based on the specified value, starting at midnight. For example, if the specified value is 6, the  discovery cycle start times are: 12am, 6am, 12pm, 6pm, 12am, etc.
    * The start time for the next discovery cycle task is the closest interval. For example, If the specified value is 6, and the configuration was saved at 10am, the next discovery cycle will start at 12pm.
    * The maximum possible value is 24.
  * **Every x days** - Select this option to run discovery cycles at the time specified in **Scheduled discovery time** every number of days defined in **Repeat scheduled discovery every (days)**. The start time is determined based on the specified value, starting the 1st of each month. For example, if the specified value is 10, the discovery cycle is triggered on 1st, 11th, 21st, 31st (if exists), 1st, 11th, etc.
  * The first start time is  the closest interval. For example, If the specified value is 10, and the configuration was saved on the 12th, the  next  discovery cycle will be on the 21st. The maximum possible interval is 30.
  * **Days of week** - Select this option to run discovery cycles at the time specified in **Scheduled discovery time** on the selected days of the week in **Repeat scheduled discovery on**.

### Setting More Than One Scheduled Discovery Time

When you choose **Every x days** or **Days of week**, you can set a number of discovery times that will run at set hours on the days that you choose.  In this way, you can run a discovery at defined hours, and not every X hours, for instance to fit in with specific events during the workday.

* Click the `+` button to set more than one discovery time, to run the discovery at defined hours during the day.
  ![DiscoveryScheduleX\_Days](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DiscoveryScheduleX_Days.png)

* Click the **Delete** icon ![DeleteIconB](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DeleteIconB.png) to the right of a scheduled discovery time to delete it.

### Running Enforcement Sets

* **Constantly run enforcement sets** *(required, default: False)*
  * Select this option so that Axonius constantly runs the automatic Enforcement Sets. You should select this option when you have a realtime adapter and the assets fetched from that adapter are part of Saved Queries used as the trigger for different Enforcement Sets.
  * Leave this option not selected (i.e., disabled; the default) so that Axonius runs the automatic Enforcement Sets at the end of each discovery cycle.

<Callout icon="📘" theme="info">
  Note

  * It is recommended to keep this option disabled.

  * For details on realtime adapters, see [Adapter Advanced Settings](/docs/advanced-settings).

  * For details about Enforcements Sets, see [Creating Enforcement Sets](/docs/create-ec-set).
</Callout>

### Tagging Reimaged Devices

* **Tag reimaged devices** *(required, default: False)* -
  * Select this option so that Axonius tags a device as 'old'  if Axonius identifies that the device has been reimaged and there is a new asset record in Axonius that represents that device.
    For example, a new employee receives a laptop that was owned by a former employee. The laptop has been reimaged. When the discovery cycle discovers the reimaged laptop, Axonius identifies that there are two different devices sharing common characteristics (for example, same MAC address) and that one device is 'new' in the network, while the other has not been discovered for some time. In this case, Axonius tags the 'old' device as 'Reimaged by \[new device host name]'.
  * Clear this option so that Axonius does not tag any devices automatically.