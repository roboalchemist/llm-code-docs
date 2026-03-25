# Source: https://docs.axonius.com/docs/advanced-settings.md

# Adapter Advanced Settings

Basic adapter connection configuration settings are configured separately for  each of the adapter's connections.
You can configure the following **Advanced Settings** for all adapter connections or for each connection separately:

* [Adapter Configuration](#adapter-configuration) - all adapter connections, or for each adapter separately for specific settings only.
* [Advanced Configuration](/docs/advanced-configuration-for-adapters) - all adapter  connections or for each connection separately only for specific adapters.
* [Discovery Configuration](/docs/adapter-discovery-configuration) - all adapter connections or for each connection separately.
* [Ingestion Rules Configuration](/docs/setting-adapter-ingestion-rules) -  all adapter connections or for each connection separately.

<Callout icon="📘" theme="info">
  Note

  Some adapters, for example,[Amazon Web Services (AWS)](/docs/amazon-web-services-aws#advanced-settings) and [Microsoft Active Directory (AD)](/docs/microsoft-active-directory-ad#advanced-settings), have adapter specific advanced settings, that are displayed under a separate tab in the **Advanced Settings** pane.
</Callout>

<Image alt="AdapterAdvancedConfig" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdapterAdvancedConfig.png" />

## Adapter Configuration

To configure the adapter's **Advanced Settings**, do the following:

1. Open the **Adapters** page. Click the **Adapters** icon on the left navigation panel.

2. Search for and click the relevant adapter. The **Adapter Profile** page opens displaying the list of connected connections.

3. Under **Advanced Settings**,  select  **Adapter Configuration**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Advanced%20Adapter%20Config%20New.png)

4. To save any configuration changes, click **Save**.

You can control and configure the following settings:

1. [Ignore devices and other assets that have not been seen by the source in the last X hours](/docs/advanced-settings#ignore-devices-and-other-assets-that-have-not-been-seen-by-the-source-in-the-last-x-hours)
2. [Ignore users and other assets that have not been seen by the source in the last X hours](/docs/advanced-settings#ignore-users-and-other-assets-that-have-not-been-seen-by-the-source-in-the-last-x-hours)
3. [Delete devices and other assets that have not been returned from the source in the last X hours](/docs/advanced-settings#delete-devices-and-other-assets-that-have-not-been-returned-from-the-source-in-the-last-x-hours)
4. [Delete users that have not been returned from the source in the last X hours](/docs/advanced-settings#delete-users-that-have-not-been-returned-from-the-source-in-the-last-x-hours)
5. [Delete devices and other assets that were not returned from the source by a successful fetch in the last X hours ](/docs/advanced-settings#delete-devices-and-other-assets-that-were-not-returned-from-the-source-by-a-successful-fetch-in-the-last-x-hours)
6. [Delete users that were not returned from the source by a successful fetch in the last X hours](/docs/advanced-settings#delete-users-that-were-not-returned-from-the-source-by-a-successful-fetch-in-the-last-x-hours)
7. [Override the global discovery schedule for this adapter to wait X hours before fetching](#override-the-global-discovery-schedule-for-this-adapter-to-wait-x-hours-before-fetching)
8. [Wait for a connection to the source for up to X seconds](#wait-for-a-connection-to-the-source-for-up-to-x-seconds)
9. [Wait for a response from the source for up to X seconds](#wait-for-a-response-from-the-source-for-up-to-x-seconds)
10. [Terminate after X hours of an active fetch](#terminate-after-x-hours-of-an-active-fetch)
11. [Set as inactive after X failed attempts to connect](/docs/advanced-settings#set-as-inactive-after-x-failed-attempts-to-connect)
12. [Number of connection attempts before fetch failure](#number-of-connection-attempts-before-fetch-failure)
13. [Ignore matching assets from the source if a subsequent asset was seen by the source before the previously fetched asset](#ignore-matching-assets-from-the-source-if-a-subsequent-asset-was-seen-by-the-source-before-the-previously-fetched-asset)
14. [Enable real-time adapter (ignores all discovery cycle settings and continuously repeats fetches from the source)](#enable-realtime-adapter-ignores-all-discovery-cycle-settings-and-continuously-repeats-fetches-from-the-source)
15. [Collect real-time adapter fetch history and events](#collect-realtime-adapter-fetch-history-and-events)
16. [Include or exclude the given IP ranges](/docs/advanced-settings#include-or-exclude-the-given-ip-ranges)
17. [Exclude/Include fetched devices within IP  ranges (IPv4 and IPv6)](/docs/advanced-settings#excludeinclude-fetched-devices-within-ip-ranges-ipv4-and-ipv6)
18. [Fetch order](/docs/advanced-settings#fetch-order)
19. [Custom adapter value](/docs/advanced-settings#custom-adapter-value)
20. [Create account from connection label](/docs/advanced-settings#create-account-from-connection-label)

### Configuring Custom Settings for Each Adapter Connection

You can configure the following settings for each adapter connection separately:

* 'Ignore devices that have not been seen by the source in the last X hours'
* 'Delete devices and other assets that were not returned from the source by a successful fetch in the last X hours'
* 'Delete devices that have not been returned from the source in the last X hours'
* 'Delete users that were not returned from the source by a successful fetch in the last X hours'
* 'Ignore users that have not been seen by the source in the last X hours'
* 'Delete users that have not been returned from the source in the last X hours'
* 'Set as inactive after X failed attempts to connect'

To configure these settings separately for each adapter connection:

1. On the Advanced Settings Adapter Configuration page toggle on 'Enable custom adapter connection settings for each connection separately'

<Image alt="AdvCustomNew21(1)" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdvCustomNew21(1).png" />

2. Click **Save**.  The **Adapter  Configuration** tab now also appears on the **Add Connection** drawer.
3. Click **Add Connection**. The **Connection Configuration** drawer now has an additional tab  (Adapter Configuration).

<Image alt="AdapterConfigExtra3" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdapterConfigExtra3.png" />

4. Toggle on **Enable custom adapter connection settings**. The settings that you can configure are now displayed.

<Image alt="CustomDelteIgnoreGA" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CustomDelteIgnoreGA.png" />

5. Configure the settings that you want to apply for this specific connection, and then select **Save** or **Save and Fetch**. Any settings that you did not configure here use the default settings.

## Adapter Configuration Settings

### Ignore devices and other assets that have not been seen by the source in the last X hours

This setting lets you avoid fetching assets that are no longer part of your network, but that still exist in the data repository of the adapter connection. Note that this setting can either apply to all connections for an adapter, or you can set different settings for specific connections.

* If supplied, the adapter only fetches asset information if that asset entity has been seen by the adapter connection ('Last Seen' field) within the last specified number of hours.
* If not supplied, the adapter always fetches asset information.

For example, if the value is 2160 hours, any device asset entity that has not been seen by the adapter connection in the last 90 days is not pulled into Axonius. The best practice for most adapters is to set this value to 2160 hours. For data sources that have frequently changing data, the best practice is to have shorter *Ignore devices not seen in x hours settings*.  For example, a network adapter will update data in close to real time.  Thirty days or less is optimal.  On the contrary, for a CMDB adapter, you may want to fetch a longer history, especially if you are performing CMDB reconciliation or database cleanup.

### Ignore users and other assets that have not been seen by the source in the last X hours

This setting is the same as the **[Ignore devices and other assets that have not been seen by the source in the last X hours](#ignore-devices-and-other-assets-that-have-not-been-seen-by-the-source-in-the-last-x-hours)** setting, but in the context of user information. Note that this setting can either apply to all connections for an adapter, or you can set different settings for specific connections.

### Delete devices and other assets that have not been returned from the source in the last X hours

This setting lets you avoid keeping data for assets that no longer exist on the ‘source’, under the assumption that if an asset entity has not been fetched from an adapter connection, it no longer exists and can be deleted. Note that this setting can either apply to all connections for an adapter, or you can set different settings for specific connections.

* If supplied, the adapter deletes the asset data fetched from the source if the asset entity was not fetched from that adapter connection (source) in the last specified number of hours. Only the information fetched from that specific adapter is deleted, keeping the rest of the information on that asset (if it exists) intact. This is determined by the *Fetch Time* field.
* If not supplied (that is, if left blank or set to 0),  the adapter never deletes asset information.

For example, if the value is 48 hours, a device asset entity is deleted if it has not been fetched from the adapter connection in 2 days.

<Callout icon="📘" theme="info">
  Note

  Tickets are not included in this setting. They are not deleted according to when they have last been fetched, but are deleted when they are not linked to assets existing in the system.
</Callout>

### Delete users that have not been returned from the source in the last X hours

This setting is the same as the **[Delete devices and other assets that have not been returned from the source in the last X hours](#delete-devices-and-other-assets-that-have-not-been-returned-from-the-source-in-the-last-x-hours)** setting, but in the context of user information. Note that this setting can either apply to all connections for an adapter, or you can set different settings for specific connections.

### Delete devices and other assets that were not returned from the source by a successful fetch in the last X hours

Use this setting to only delete devices not returned by the adapter if the most recent fetch was successful. In this way, if there was a temporary issue in a fetch, devices will not be deleted accidentally. The value for this setting must always be lower than the value of 'Delete devices that have not been returned from the source in the last X hours'. Note that this setting can either apply to all connections for an adapter, or you can set different settings for specific connections.
For example, assuming you have the discovery schedule set to the default 12 hours, you can set the value of this setting to 12, while the setting for 'Delete devices that have not been returned from the source in the last X hours' is 48. In such a case you ensure that 4 cycles of fetch were not successful before the final deletion.

### Delete users that were not returned from the source by a successful fetch in the last X hours

Use this setting to only delete users not returned by the adapter if the most recent fetch was successful. In this way, if there was a temporary issue in a fetch, users will not be deleted accidentally. The value for this setting must always be lower than the value of 'Delete users that have not been returned from the source in the last X hours'. Note that this setting can either apply to all connections for an adapter, or you can set different settings for specific connections.
For example, you can set the value of this setting to 6, while the setting for "Delete users that have not been returned from the source in the last X hours" is 24. In such a case you can ensure that 4 cycles of fetch were not successful before the final deletion.

### Override the global discovery schedule for this adapter to wait X hours before fetching

This setting lets you schedule a specific adapter discovery cycle that runs longer than the global discovery cycle.

* If supplied, once a fetch starts for an adapter, Axonius waits for the minimum number of hours specified before initiating the next adapter discovery cycle.
* If not supplied, the adapter discovery cycle is always part of the global discovery.

For example, if the value is 2 hours and the global discovery starts every 1 hour, then Axonius pulls data from the adapter every 2 hours instead of every 1 hour.

### Wait for a connection to the source for up to X seconds

This setting lets you avoid endless connection attempts when the connection is down.

* If supplied, all connections for the adapter wait for the specified number of seconds before the attempt to connect to the adapter connection is considered timed out. If the connection fails, an error icon is displayed next to the adapter connection icon.
* If not supplied, all connections for the adapter do not have any connection timeout.

<Callout icon="📘" theme="info">
  Note

  It is not recommended to leave this option blank.
</Callout>

For example, if the value is 300 seconds, as part of the discovery cycle, Axonius displays an error icon next to the adapter connection if a connection has not been established within 300 seconds. Axonius then continues the discovery cycle and tries to connect the next adapter connection.

### Wait for a response from the source for up to X seconds

This setting lets you avoid endless data fetching attempts when there is any error during the process. This setting determines when Axonius stops fetching data from the adapter connection if issues are identified during the discovery process.

* If supplied, all connections for the adapter wait for the specified number of seconds to pass from the last data fetched during the discovery cycle.
* If not supplied, all connections for the adapter do not have any timeout.

<Callout icon="📘" theme="info">
  Note

  It is not recommended to leave this option blank.
</Callout>

For example, if the value is 5400 seconds (90 minutes), and Axonius identifies an issue with fetching the data and no new data is retrieved for over 90 minutes, Axonius terminates the transaction and continues to the next one. A best practice is to set this to 7200 seconds.

### Terminate after X hours of an active fetch

Use this setting to set a threshold time (in hours) that will terminate a running successful fetch operation of an adapter when its fetch exceeds the time set (including an appropriate log and status). This setting is useful for maintaining a reasonable planned time window for the discovery cycle. This applies to each connection individually.

For example, if the parameter fetch time is 10 hours, and the environment has four connections, the total is 40 hours.

### Set as inactive after X failed attempts to connect

Use this setting to configure a number of connection attempts after which the adapter connection is set to inactive. When you leave this field empty, the connection for the adapter is not automatically set as inactive after consecutive failed connection attempts.
This is useful when connected to systems that change their credentials from time to time.  The number of connection attempts includes all connections to the server, including periodic connection updates (if set in [Data Aggregation Settings](/docs/configuring-data-aggregation-settings)). Note that this setting can either apply to all connections for an adapter, or you can set different settings for specific connections.

### Number of connection attempts before fetch failure

Use this setting to configure the number of times a fetch reattempts to connect before failing to retrieve data. You can specify up to 5 reattempts. By default, the value is empty (a single attempt to connect). The sleep interval between each reattempt to connect is 5 minutes.

### Ignore matching assets from the source if a subsequent asset was seen by the source before the previously fetched asset

In some cases, Axonius may fetch device information from a number of different adapter connections of the same adapter type. The device information from each of those sources may be different due to the last time the device information was updated in that adapter connection ('Last Seen' field).
Enable this setting so that all connections for the adapter ignore older device or user data (based on fetched ‘Last Seen’ field) when data for a specific device or user is received from connections of the same adapter.

For example, if for a device named 'Device123' information is fetched from two adapter connections.
'Last Seen' fetched is:

* From server1 -  Jan-1-2023.
* From server2 - Jan-5-2023.

When this setting is selected, Axonius discards and ignores the data fetched from server1.

### Enable real-time adapter (ignores all discovery cycle settings and continuously repeats fetches from the source)

This setting lets you constantly fetch adapter data. This means that once Axonius completes the discovery cycle for the adapter connection, it initiates another cycle immediately.
If the adapter’s collected data is updated in very short cycles (seconds or minutes), use this setting to make sure the fetched data is always up to date.

* If enabled, Axonius pulls information from the adapter constantly.
* If disabled, Axonius does not pull information from the adapter constantly.

<Callout icon="📘" theme="info">
  Note

  If **Override the global discovery schedule for this adapter to wait X hours before fetching** is configured, this setting is ignored. The start of the next discovery cycle for the adapter is based on the **Override the global discovery schedule for this adapter to wait X hours before fetching** setting.
</Callout>

<Callout icon="📘" theme="info">
  Note

  It is not recommended to enable custom scheduling when you use this setting.
</Callout>

### Collect real-time adapter fetch history and events

This setting lets you decide whether to collect the real-time fetch data and events.
If the adapter’s collected data is updated in very short cycles (seconds or minutes), this can affect the retention of the [Adapters Fetch History](/docs/adapters-fetch-history).

* If enabled, Axonius collects the real-time fetch data and events from all connections for the adapter.
* If disabled, Axonius does not collect the real-time fetch data and events from all connections for the adapter.

This setting should be used together with **Enable real-time adapter (Ignores all discovery cycle settings and continuously repeats fetches from the source)**.

<Image alt="AdapterREaltime" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdapterREaltime.png" />

### Include or exclude the given IP ranges

This setting lets you choose whether to include or exclude assets within the IPv4 and IPv6 address ranges.

<Callout icon="📘" theme="info">
  Note

  * In the case of ‘Exclude’, if the asset contains more than one IP address and only one of them is in the range provided, then the asset will be excluded.

  * In the case of ‘Include’, if the asset contains more than one IP address and only one of them is in the range provided, then the asset will be included.
</Callout>

### Exclude/Include fetched devices within IP ranges (IPv4 and IPv6)

This setting lets you exclude or include a device within one or more comma-separated IPv4 or IPv6 address ranges from the fetch. For example, if `127.0.0.1-127.0.0.20, 127.0.0.30-127.0.0.50` is entered, all devices that have an IPv4 address in the specified ranges are excluded from/included in the discovery cycle. If  `2001:db8:3333:4444:5555:6666:7777:5555-2001:db8:3333:4444:5555:6666:7777:8888` all devices that have an IPv6 address in the specified ranges will be excluded from/included in the discovery cycle.

### Fetch order

By default all adapters run at the same time in a fetch cycle. Use this field to set a fetch order for adapters. Use values of 0, 1, 2, 3, etc. Adapters with **Fetch order** set to 0 run first, then those set to 1, which will run only after the first set completes its run, then 2, etc. Adapters with no value set in this field run after any configured adapters complete their run. This field is optional.
By default, this field is empty as all adapters should run right at the beginning of the cycle phase. This increases the length of the fetch cycle. Use this field for advanced scenarios only, such as running endpoint protection adapters after cloud adapters.

### Custom adapter value

Enter one or more values (as strings) to add to the Adapter information displayed. The values in these fields will be displayed as part of the fetched information for every entity fetched from the adapter as an added field on the asset called Custom Adapter Value.

### Create account from connection label

This is available only for accounts with SaaS Management (default: yes) - Select this option to create an account from the connection label name.

## Running Cleanup Manually

Old assets are cleaned and deleted as part of the [Discovery Cycle](/docs/discovery-cycle#global-discovery-cycle-phases), or as part of a custom cycle, according to the relevant configurations on this page. You can also run cleanup on-demand for a specific adapter. To run cleanup on demand:

1. From the **Adapter** page select a single configured adapter.

<Image alt="CleanupNEw" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/AdapterMemoMenu1.png" />

2. Select **Run Adapter Cleanup**. The system asks you to confirm your choice.

3. After you confirm, the assets that conform to the "Delete device and other assets...." and "Delete users...." configurations on that adapter are deleted from the system.