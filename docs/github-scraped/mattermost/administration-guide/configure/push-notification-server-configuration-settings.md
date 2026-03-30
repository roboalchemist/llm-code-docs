orphan

:

nosearch

:

With self-hosted deployments, you can configure mobile push
notifications for Mattermost by going to **System Console \> Environment
\> Push Notification Server**, or by editing the `config.json` file as
described in the following tables. Changes to configuration settings in
this section require a server restart before taking effect.

# Enable push notifications

+-------------------------------+--------------------------------------------+
| Enable or disable Mattermost  | - System Config path: **Environment \>     |
| push notifications.           |   Push Notification Server**               |
|                               | - `config.json` setting: `EmailSettings`   |
| - **Do not send push          |   \> `SendPushNotifications`               |
|   notifications**: Mobile     | - Environment variable:                    |
|   push notifications are      |   `MM_EMAILSETTINGS_SENDPUSHNOTIFICATIONS` |
|   disabled.                   |                                            |
| - **Use HPNS connection with  |                                            |
|   uptime SLA to send          |                                            |
|   notifications to iOS and    |                                            |
|   Android apps**:             |                                            |
|   **(Default)** Use           |                                            |
|   Mattermost\'s hosted push   |                                            |
|   notification service.       |                                            |
| - **Use TPNS connection to    |                                            |
|   send notifications to iOS   |                                            |
|   and Android apps**: Use     |                                            |
|   Mattermost\'s test push     |                                            |
|   notification service.       |                                            |
| - **Manually enter Push       |                                            |
|   Notification Service        |                                            |
|   location**: When building   |                                            |
|   your own custom mobile      |                                            |
|   apps, you must host your    |                                            |
|   own mobile push proxy       |                                            |
|   service, and specify that   |                                            |
|   URL in the **Push           |                                            |
|   Notification Server**       |                                            |
|   field.                      |                                            |
+-------------------------------+--------------------------------------------+

## Hosted Push Notifications Service (HPNS)

Mattermost Enterprise, Professional, and Cloud customers can use
Mattermost\'s Hosted Push Notification Service (HPNS). The HPNS offers:

- Access to a publicly-hosted Mattermost Push Notification Service
  (MPNS) [available on
  GitHub.](https://github.com/mattermost/mattermost-push-proxy)
- An explicit [privacy
  policy](https://mattermost.com/data-processing-addendum/) for the
  contents of unencrypted messages.
- Encrypted TLS connections:
  - Between HPNS and Apple Push Notification Services
  - Between HPNS and Google's Firebase Cloud Messaging Service
  - HPNS and your Mattermost Server
- Production-level uptime expectations.
- Out-of-box configuration for new servers means nothing is required to
  enable HPNS for new deployments. HPNS can be [enabled for existing
  deployments](#enable-hpns-for-existing-deployments).

:::: note
::: title
Note
:::

\- The HPNS only works with pre-built apps Mattermost deploys through
the [Apple App Store](https://www.apple.com/app-store/) and [Google Play
Store](https://play.google.com/store/games?hl=en). If you build your own
mobile apps, you must also [host your own Mattermost push proxy
server](#host-your-own-push-proxy-service). - You must ensure that the
push proxy can be reached on the correct port. For HPNS, it\'s port 443
from the Mattermost server. - Mattermost doesn\'t store any notification
data. Any data being stored is at the server level only, such as the
`device_id`, since the HPNS needs to know which device the notification
must be sent to.
::::

## Test Push Notifications Service (TPNS)

Non-commercial self-hosted customers can use Mattermost\'s free, basic
Test Push Notifications Service (TPNS).

:::: note
::: title
Note
:::

\- The TPNS isn't recommended for use in production environments, and
doesn't offer production-level update service level agreements (SLAs). -
The TPNS isn\'t available for Mattermost Cloud deployments. - The TPNS
only works with the pre-built mobile apps that Mattermost deploys
through the [Apple App Store](https://www.apple.com/app-store/) and
[Google Play Store](https://play.google.com/store/games?hl=en). If you
have built your own mobile apps, you must also [host your own Mattermost
push proxy service](#host-your-own-push-proxy-service). - You must
ensure that the push proxy can be reached on the correct port. For TPNS,
it\'s port 80 from the Mattermost server. - If you don\'t need or want
Mattermost to send mobile push notifications, disabling this
configuration setting in larger deployments may improve server
performance in the following areas:

- Reduced Processing Load: Generating and sending push notifications
  requires processing power and resources. By disabling them, the server
  can allocate those resources to other tasks.
- Decreased Network Traffic: Push notifications involve network
  communication. Disabling them reduces the amount of data being
  transferred, which can enhance overall network performance.
- Lower Database Load: Each push notification may involve reading from
  and writing to the database. Reducing these operations decreases the
  load on the database, improving response times for other queries.
- Faster Response Times: With fewer tasks to handle related to
  notifications, the system can respond faster to other requests from
  users, leading to a better user experience.
- Simplified Error Handling: Push notification services can sometimes
  fail or have latency issues, requiring additional error handling.
  Disabling these notifications simplifies the system\'s operations.
- However, disabling push notifications can negatively impact user
  experience, communication efficiency, and overall productivity. It's
  important to balance performance improvements with the needs of your
  organization and users.
::::

## ID-only push notifications

Admins can enable mobile notifications to be fully private to protect a
Mattermost customer against breaches in iOS and Android notification
infrastructure by limiting the data sent to Apple and Google through a
Mattermost configuration setting.

The standard way to send notifications to iOS and Android applications
requires sending clear text messages to Apple or Google so they can be
forwarded to a user's phone and displayed on iOS or Android. While Apple
or Google assure the data is not collected or stored, should the
organizations be breached or coerced, all standard mobile notifications
on the platform could be compromised.

To avoid this risk, Mattermost can be configured to replace mobile
notification text with message ID numbers that pass no information to
Apple of Google. When received by the Mattermost mobile application on a
user's phone, the message IDs are used to privately communicate with
their Mattermost server and to retrieve mobile notification messages
over an encrypted channel. This means that, at no time, is the message
text visible to Apple or Google's message relay system. The contents of
the message also won\'t reach Mattermost.

:::: note
::: title
Note
:::

Because of the extra steps to retrieve the notifications messages under
Mattermost's private mobility capability with ID-only push
notifications, end users may experience a slight delay before the mobile
notification is fully displayed compared to sending clear text through
Apple and Google's platform.
::::

See our
`configuration settings <administration-guide/configure/site-configuration-settings:push notification contents>`{.interpreted-text
role="ref"} documentation to learn more about the ID-only push
notifications configuration setting. See our
`Mobile Apps FAQ documentation <deployment-guide/mobile/mobile-faq:how can i use id-only push notifications to protect notification content from being exposed to third-party services?>`{.interpreted-text
role="ref"} for details on using ID-only push notifications for data
privacy.

# Push notification server location

+-------------------------------+---------------------------------------------+
| The physical location of the  | - System Config path: **Environment \> Push |
| Mattermost Hosted Push        |   Notification Server**                     |
| Notification Service (HPNS)   | - `config.json` setting: `EmailSettings` \> |
| server.                       |   `PushNotificationServer`                  |
|                               | - Environment variable:                     |
| Select from **US**            |   `MM_EMAILSETTINGS_PUSHNOTIFICATIONSERVER` |
| **(Default)** or **Germany**  |                                             |
| to automatically populate the |                                             |
| **Push Notification Server**  |                                             |
| field server URL.             |                                             |
+-------------------------------+---------------------------------------------+

# Maximum notifications per channel

+----------------------------+-------------------------------------------------+
| The maximum total number   | - System Config path: **Environment \> Push     |
| of users in a channel      |   Notification Server**                         |
| before \@all, \@here, and  | - `config.json` setting: `TeamSettings` \>      |
| \@channel no longer send   |   `MaxNotificationsPerChannel` \> `1000`        |
| desktop, email, or mobile  | - Environment variable:                         |
| push notifications to      |   `MM_EMAILSETTINGS_MAXNOTIFICATIONSPERCHANNEL` |
| maximize performance.      |                                                 |
|                            |                                                 |
| Numerical input. Default   |                                                 |
| is **1000**.               |                                                 |
+----------------------------+-------------------------------------------------+

:::: note
::: title
Note
:::

- We recommend increasing this value a little at a time, monitoring
  system health by tracking
  `performance monitoring metrics </administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring>`{.interpreted-text
  role="doc"}, and only increasing this value if large channels have
  restricted permissions controlling who can post to the channel, such
  as a
  `read-only channel <administration-guide/onboard/advanced-permissions:read-only channels>`{.interpreted-text
  role="ref"}.
- Reducing this configuration setting value to **10** in larger
  deployments may improve server performance in the following areas:
  - **Reduced Load on Notification System**: Each notification generates
    a certain amount of computational and network load. By limiting the
    number of notifications per channel, the system processes fewer
    notifications, thereby reducing the load on servers.
  - **Database Efficiency**: Notifications are typically stored in a
    database. Fewer notifications mean less frequent database writes and
    reads, leading to quicker database operations and reduced latency.
  - **Minimized Client Processing**: Users\' clients (e.g., desktop and
    mobile apps) have to fetch and process notifications. With fewer
    notifications, clients can operate more efficiently, reducing memory
    and CPU usage on users\' devices.
  - **Improved User Experience**: An overload of notifications can lead
    to performance lags and a cluttered experience for users. Limiting
    the number ensures that users receive only the most important
    notifications, which can enhance usability and response times.
  - **Network Bandwidth**: High numbers of notifications can consume a
    lot of bandwidth, particularly if they are being sent to many users.
    Fewer notifications can lead to lower overall network usage and
    potentially faster delivery of critical messages.
  - **Server Load Balancing**: By reducing the number of notifications,
    the workload can be more evenly distributed across the servers,
    leading to better load balancing and preventing any single server
    from becoming a bottleneck.
::::
