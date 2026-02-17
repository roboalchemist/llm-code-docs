# Plugins configuration settings

Review and manage the following plugin configuration options in the
System Console by selecting the **Product**
[\|product-list\|](##SUBST##|product-list|) menu, selecting **System
Console**, and then selecting **Plugins**:

- [Plugin management](#plugin-management)
- [Calls](#calls)
- [AI Agents](#ai-agents)
- [GitLab](#gitlab)
- [GitHub](#github)
- [Jira](#jira)
- [Legal Hold](#legal-hold)
- [Microsoft Calendar Integration](#microsoft-calendar)
- [MS Teams](#ms-teams)
- [Performance metrics](#performance-metrics)
- [Collaborative playbooks](#collaborative-playbooks)
- [User satisfaction surveys](#user-satisfaction-surveys)
- [ServiceNow](#servicenow)
- [Zoom](#zoom)
- [config.json-only settings](#config-json-only-settings)

:::: tip
::: title
Tip
:::

System admins managing a self-hosted Mattermost deployment can edit the
`config.json` file as described in the following tables. Each
configuration value below includes a JSON path to access the value
programmatically in the `config.json` file using a JSON-aware tool. For
example, the `Enable` value is under `PluginSettings`.

- If using a tool such as [jq](https://stedolan.github.io/jq/), you\'d
  enter: `cat config/config.json | jq '.PluginSettings.Enable'`
- When working with the `config.json` file manually, look for an object
  such as `PluginSettings`, then within that object, find the key
  `Enable`.
::::

------------------------------------------------------------------------

## Plugin management

Access the following configuration settings in the System Console by
going to **Plugins \> Plugin Management**.

### Enable plugins

+------------------------------------------------------------------------------------------------+------------------------------+
| - **true**: **(Default)** Enables plugins on your Mattermost server. See the [Use plugins with | - System Config path:        |
|   Mattermost](https://developers.mattermost.com/integrate/plugins/using-and-managing-plugins/) |   **Plugins \> Plugin        |
|   documentation for details.                                                                   |   Management**               |
| - **false**: Disables plugins on your Mattermost server.                                       | - `config.json` setting:     |
|                                                                                                |   `PluginSettings` \>        |
|                                                                                                |   `Enable` \> `true`         |
|                                                                                                | - Environment variable:      |
|                                                                                                |   `MM_PLUGINSETTINGS_ENABLE` |
+------------------------------------------------------------------------------------------------+------------------------------+

:::: note
::: title
Note
:::

Disabling this configuration setting in larger deployments may improve
server performance in the following areas:

- Resource Consumption: Plugins consume system resources such as CPU,
  memory, and disk. Disabling them frees up these resources, allowing
  the core Mattermost application to run more efficiently.
- Reduced Complexity: Each plugin can add additional logic and
  processing requirements. By reducing the number of active plugins, you
  lower the complexity and potential points of failure in the system.
- Faster Load Times: Disabling plugins can lead to faster server startup
  and lower latency during user interactions, as there are fewer
  components for the system to initialize and manage.
- Stability: Some plugins may have bugs or performance issues that can
  affect the overall performance and stability of the Mattermost
  instance. Disabling problematic or under-utilized plugins can enhance
  the stability of the system.
- Maintenance and Updates: Managing fewer plugins reduces the overhead
  associated with maintaining and updating them, which can contribute to
  smoother operation and less downtime
- However, plugins are often essential for integrating Mattermost with
  other services and workflows. It\'s important to balance performance
  improvements with the needs of your organization and users.
::::

### Require plugin signature

+-----------------------------------------------+----------------------------------------------+
| - **true**: **(Default)** Enables plugin      | - System Config path: **Plugins \> Plugin    |
|   signature validation for managed and        |   Management**                               |
|   unmanaged plugins.                          | - `config.json` setting: `PluginSettings` \> |
| - **false**: Disables plugin signature        |   `RequirePluginSignature` \> `true`         |
|   validation for managed and unmanaged        | - Environment variable:                      |
|   plugins.                                    |   `MM_PLUGINSETTINGS_REQUIREPLUGINSIGNATURE` |
+-----------------------------------------------+----------------------------------------------+

:::: note
::: title
Note
:::

\- This setting is applicable to self-hosted deployments only. - From
Mattermost server v10.11, pre-packaged plugins require signature
validation on startup. Distributions that bundle custom pre-packaged
plugins must configure custom public keys via
`PluginSettings.SignaturePublicKeyFiles` to validate their signatures. -
**Mattermost server v10.10 and earlier**: Pre-packaged plugins are not
subject to signature validation. - Plugins installed through the
Marketplace are always subject to signature validation at the time of
download. - Enabling this configuration will result in [plugin file
uploads](#upload-plugin) being disabled in the System Console.
::::

### Automatic prepackaged plugins

+----------------------------------------------+---------------------------------------------------+
| - **true**: **(Default)** Mattermost         | - System Config path: **Plugins \> Plugin         |
|   automatically installs and upgrades any    |   Management**                                    |
|   enabled pre-packaged plugins. If a newer   | - `config.json` setting: `PluginSettings` \>      |
|   version is installed, no changes are made. |   `AutomaticPrepackagedPlugins` \> `true`         |
| - **false**: Mattermost does not             | - Environment variable:                           |
|   automatically install or upgrade           |   `MM_PLUGINSETTINGS_AUTOMATICPREPACKAGEDPLUGINS` |
|   pre-packaged plugins. Pre-packaged plugins |                                                   |
|   may be installed manually from the         |                                                   |
|   Marketplace, even when offline.            |                                                   |
+----------------------------------------------+---------------------------------------------------+

:::: note
::: title
Note
:::

**Prepackaged Plugin Installation Behavior**: When system administrators
drop plugin files (with their `.sig` signature files) into the
`prepackaged_plugins` directory, the plugins won\'t install
automatically. Prepackaging makes the plugin available for \"offline\"
installation. The plugin will automatically install only when a system
admin pre-configures the `config.json` with that plugin enabled.
::::

### Upload Plugin

+-------------------------------------------+-------------------------------------+
| - **true**: Enables you to upload plugins | - System Config path: **Plugins \>  |
|   from the local computer to the          |   Plugin Management**               |
|   Mattermost server.                      | - `config.json` setting:            |
| - **false**: **(Default)** Disables       |   `PluginSettings` \>               |
|   uploading of plugins from the local     |   `EnableUploads` \> `false`        |
|   computer to the Mattermost server.      | - Environment variable:             |
|                                           |   `MM_PLUGINSETTINGS_ENABLEUPLOADS` |
+-------------------------------------------+-------------------------------------+

:::: note
::: title
Note
:::

\- This setting is applicable to self-hosted deployments only. - When
plugin uploads are enabled, the error
`Received invlaid response from the server` when uploading a plugin file
typically indicates that the
`MaxFileSize <administration-guide/configure/environment-configuration-settings:maximum file size>`{.interpreted-text
role="ref"} configuration setting isn\'t large enough to support the
plugin file upload. Additional proxy setting updateds may also be
required. - The ability to upload plugin files is disabled when the
[Require plugin signature](#require-plugin-signature) configuration
setting is enabled.
::::

### Enable Marketplace

+---------------------------------------+-----------------------------------------+
| - **true**: **(Default)** Enables the | - System Config path: **Plugins \>      |
|   plugin Marketplace on your          |   Plugin Management**                   |
|   Mattermost server for all system    | - `config.json` setting:                |
|   admins.                             |   `PluginSettings` \>                   |
| - **false**: Disables the plugin      |   `EnableMarketplace` \> `true`         |
|   Marketplace on your Mattermost      | - Environment variable:                 |
|   server for all system admins.       |   `MM_PLUGINSETTINGS_ENABLEMARKETPLACE` |
+---------------------------------------+-----------------------------------------+

### Enable remote Marketplace

+-------------------------------------------+-----------------------------------------------+
| - **true**: **(Default)** Mattermost      | - System Config path: **Plugins \> Plugin     |
|   attempts to connect to the endpoint set |   Management**                                |
|   in **Marketplace URL**. If the          | - `config.json` setting: `PluginSettings` \>  |
|   connection fails, an error is           |   `EnableRemoteMarketplace` \> `true`         |
|   displayed, and the Marketplace only     | - Environment variable:                       |
|   shows pre-packaged and installed        |   `MM_PLUGINSETTINGS_ENABLEREMOTEMARKETPLACE` |
|   plugins.                                |                                               |
| - **false**: Mattermost does not attempt  |                                               |
|   to connect to a remote Marketplace. The |                                               |
|   Marketplace shows only pre-packaged and |                                               |
|   installed plugins. Use this setting if  |                                               |
|   your Mattermost server cannot connect   |                                               |
|   to the Internet.                        |                                               |
+-------------------------------------------+-----------------------------------------------+

:::: note
::: title
Note
:::

\- From Mattermost v9.1, set this configuration setting value to `true`
to access a configured remote marketplace URL. - For Mattermost v9.0,
the `MM_FEATUREFLAGS_STREAMLINEDMARKETPLACE` feature flag must be set to
`false`, and this configuration setting must be set to `true` to access
a configured remote marketplace URL. - Each Mattermost host must have
network access to the endpoint set in MarketplaceURL.
::::

### Marketplace URL

+---------------------------------------------+--------------------------------------+
| This setting stores the URL for the remote  | - System Config path: **Plugins \>   |
| Markeplace.                                 |   Plugin Management**                |
|                                             | - `config.json` setting:             |
| String input. Default is                    |   `PluginSettings` \>                |
| **https://api.integrations.mattermost.com** |   `MarketplaceURL`                   |
|                                             | - Environment variable:              |
|                                             |   `MM_PLUGINSETTINGS_MARKETPLACEURL` |
+---------------------------------------------+--------------------------------------+

### Installed plugin state

+-----------------------------------------------------+------------------------------------+
| This setting is a list of installed plugins and     | - System Config path: **Plugins \> |
| their status as enabled or disabled.                |   Plugin Management**              |
|                                                     | - `config.json` setting:           |
| The `config.json` setting is an object. The object  |   `PluginSettings` \>              |
| keys are plugin IDs, e.g. `com.mattermost.apps`.    |   `PluginStates`                   |
| Each key maps to an object that contains an         | - Environment variable:            |
| `Enable` key that can be set as `true` or `false`.  |   `MM_PLUGINSETTINGS_PLUGINSTATES` |
+-----------------------------------------------------+------------------------------------+

### Plugin settings

+---------------------------------------------------+-------------------------------+
| This setting contains plugin-specific data.       | - System Config path:         |
|                                                   |   **Plugins \> Plugin         |
| The `config.json` setting is an object. The       |   Management**                |
| object keys are plugin IDs, e.g.                  | - `config.json` setting:      |
| `com.mattermost.apps`. Each key maps to an object |   `PluginSettings` \>         |
| that contains plugin-specific data.               |   `Plugins`                   |
|                                                   | - Environment variable:       |
|                                                   |   `MM_PLUGINSETTINGS_PLUGINS` |
+---------------------------------------------------+-------------------------------+

------------------------------------------------------------------------

## Calls

Access the following configuration settings in the System Console by
going to **Plugins \> Calls**.

### Enable plugin

+------------------------------+---------------------------------------------------------+
| - **true**: (Default)        | - System Config path: **Plugins \> Calls**              |
|   Enables the Calls plugin   | - `config.json` setting: `PluginSettings` \>            |
|   on your Mattermost         |   `PluginStates` \> `com.mattermost.calls` \> `Enable`  |
|   workspace.                 | - Environment variable:                                 |
| - **false**: Disables the    |   `MM_PLUGINSETTINGS_PLUGINSTATES_COM_MATTERMOST_CALLS` |
|   Calls plugin on your       |                                                         |
|   Mattermost workspace.      |                                                         |
+------------------------------+---------------------------------------------------------+

### RTC server address (UDP)

+-------------------------------------+---------------------------------+
| This setting controls the IP        | - System Config path: **Plugins |
| address the RTC server listens for  |   \> Calls**                    |
| UDP connections. All calls UDP      | - `config.json` setting:        |
| traffic will be served through this |   `PluginSettings` `Plugins` \> |
| IP.                                 |   `com.mattermost.calls` \>     |
|                                     |   `udpserveraddress`            |
| Changing this setting requires a    | - Environment variable:         |
| plugin restart to take effect. If   |   `MM_CALLS_UDP_SERVER_ADDRESS` |
| left unset (default value) the      |                                 |
| service will listen on all the      |                                 |
| available interfaces.               |                                 |
+-------------------------------------+---------------------------------+

:::: note
::: title
Note
:::

This setting is applicable to self-hosted deployments only, and only
when not running calls through the standalone `rtcd` service.
::::

### RTC server address (TCP)

+-------------------------------------+---------------------------------+
| This setting controls the IP        | - System Config path: **Plugins |
| address the RTC server listens for  |   \> Calls**                    |
| TCP connections. All calls TCP      | - `config.json` setting:        |
| traffic will be served through this |   `PluginSettings` \> `Plugins` |
| IP.                                 |   \> `com.mattermost.calls` \>  |
|                                     |   `tcpserveraddress`            |
| Changing this setting requires a    | - Environment variable:         |
| plugin restart to take effect. If   |   `MM_CALLS_TCP_SERVER_ADDRESS` |
| left unset (default value) the      |                                 |
| service will listen on all the      |                                 |
| available interfaces.               |                                 |
+-------------------------------------+---------------------------------+

:::: note
::: title
Note
:::

This setting is available starting in plugin version 0.17, and is only
applicable for self-hosted deployments when not running calls through
the standalone `rtcd` service.
::::

### RTC server port (UDP)

+-----------------------------------+----------------------------------+
| This setting controls the UDP     | - System Config path: **Plugins  |
| port listened on by the RTC       |   \> Calls**                     |
| server. All calls UDP traffic     | - `config.json` setting:         |
| will be served through this port. |   `PluginSettings` \> `Plugins`  |
|                                   |   \> `com.mattermost.calls` \>   |
| Changing this setting requires a  |   `udpserverport`                |
| plugin restart to take effect.    | - Environment variable:          |
|                                   |   `MM_CALLS_UDP_SERVER_PORT`     |
| Default is **8443**.              |                                  |
+-----------------------------------+----------------------------------+

:::: note
::: title
Note
:::

This setting is only applicable for self-hosted deployments when not
running calls through the standalone `rtcd` service.
::::

### RTC server port (TCP)

+-------------------------------------+--------------------------------+
| This setting controls the TCP port  | - System Config path:          |
| listened on by the RTC server. All  |   **Plugins \> Calls**         |
| calls TCP traffic will be served    | - `config.json` setting:       |
| through this port.                  |   `PluginSettings` \>          |
|                                     |   `Plugins` \>                 |
| Changing this setting requires a    |   `com.mattermost.calls` \>    |
| plugin restart to take effect.      |   `tcpserverport`              |
|                                     | - Environment variable:        |
| Default is **8443**.                |   `MM_CALLS_TCP_SERVER_PORT`   |
+-------------------------------------+--------------------------------+

:::: note
::: title
Note
:::

This setting is available starting in plugin version 0.17, and is only
applicable for self-hosted deplyoments when not running calls through
the standalone `rtcd` service.
::::

### Enable on specific channels

*Admins can\'t configure this setting from Mattermost v7.7; it\'s hidden
and always enabled for self-hosted deployments*

+--------------------------------------+---------------------------------+
| - **true**: Channel admins can       | - System Config path: **Plugins |
|   enable or disable calls on         |   \> Calls**                    |
|   specific channels. Participants in | - `config.json` setting:        |
|   DMs/GMs can also enable or disable |   `PluginSettings` \> `Plugins` |
|   calls.                             |   \> `com.mattermost.calls` \>  |
| - **false**: Only system admins can  |   `allowenablecalls`            |
|   enable or disable calls on         | - Environment variable:         |
|   specific channels.                 |   `MM_CALLS_ALLOW_ENABLE_CALLS` |
+--------------------------------------+---------------------------------+

### Test mode

*This setting was called Enable on all channels until Mattermost v7.7.
It was renamed to defaultenabled in code and Test Mode in-product and is
only applicable to self-hosted deployments.*

+-----------------------------------+----------------------------------+
| - **false**: Test mode is enabled | - System Config path: **Plugins  |
|   and only system admins can      |   \> Calls**                     |
|   start calls in channels.        | - `config.json` setting:         |
| - **true**: Live mode is enabled  |   `PluginSettings` \> `Plugins`  |
|   and all team members can start  |   \> `com.mattermost.calls` \>   |
|   calls in channels.              |   `defaultenabled`               |
|                                   | - Environment variable:          |
|                                   |   `MM_CALLS_DEFAULT_ENABLED`     |
+-----------------------------------+----------------------------------+

:::: note
::: title
Note
:::

Use this setting as a system admin to confirm calls work as expected.
When **false**, users attempting to start calls are prompted to contact
a system admin, and system admins are prompted to confirm that calls are
working as expected before switching to live mode.
::::

### ICE host override

+---------------------------------------------+--------------------------------+
| This setting can be used to override the    | - System Config path:          |
| host addresses that get advertised to       |   **Plugins \> Calls**         |
| clients when connecting to calls. The       | - `config.json` setting:       |
| accepted formats are the following:         |   `PluginSettings` \>          |
|                                             |   `Plugins` \>                 |
| - A single IP address (e.g. `10.0.0.1`).    |   `com.mattermost.calls` \>    |
| - A single hostname or FQDN (e.g.           |   `icehostoverride`            |
|   `calls.myserver.tld`).                    | - Environment variable:        |
| - (starting in v0.17.0) A comma separated   |   `MM_CALLS_ICE_HOST_OVERRIDE` |
|   list of externalAddr/internalAddr         |                                |
|   mappings (e.g.                            |                                |
|   `10.0.0.1/172.0.0.1,10.0.0.2/172.0.0.2`). |                                |
|                                             |                                |
| This is an optional field. Changing this    |                                |
| setting requires a plugin restart to take   |                                |
| effect.                                     |                                |
+---------------------------------------------+--------------------------------+

:::: note
::: title
Note
:::

\- This setting is only applicable for self-hosted deployments when not
running calls through the standalone `rtcd` service. - Depending on the
network infrastructure (e.g. instance behind a NAT device) it may be
necessary to set this field to the client facing external IP for clients
to connect. When empty or unset, the RTC service will attempt to find
the instance\'s public IP through STUN. - A hostname (e.g. domain name)
can be specified in this setting, but an IP address will be passed to
clients. This means that a DNS resolution happens on the Mattermost
instance which could result in a different IP address from the one the
clients would see, causing connectivity to fail. When in doubt, we
recommend using an IP address directly or confirming that the resolution
on the host side reflects the one on the client.
::::

### ICE host port override

+----------------------------------------+-------------------------------------+
| This setting can be used to override   | - System Config path: **Plugins \>  |
| the port used in the ICE host          |   Calls**                           |
| candidates that get advertised to      | - `config.json` setting:            |
| clients when connecting to calls.      |   `PluginSettings` \> `Plugins` \>  |
|                                        |   `com.mattermost.calls` \>         |
| This can be useful in case there are   |   `icehostportoverride`             |
| additional network components (e.g.    | - Environment variable:             |
| NLBs) in front of the RTC server that  |   `MM_CALLS_ICE_HOST_PORT_OVERRIDE` |
| may route the calls traffic through a  |                                     |
| different port. Changing this setting  |                                     |
| requires a plugin restart to take      |                                     |
| effect.                                |                                     |
+----------------------------------------+-------------------------------------+

:::: note
::: title
Note
:::

\- This setting is applicable only to self-hosted deployments. - This
value will apply to both UDP and TCP host candidates.
::::

### RTCD service URL

+--------------------------------------------+----------------------------------------+
| The URL to a running                       | - System Config path: **Plugins \>     |
| [rtcd](https://github.com/mattermost/rtcd) |   Calls**                              |
| service instance that will host the calls. | - `config.json` setting:               |
|                                            |   `PluginSettings` \> `Plugins` \>     |
| When set (non empty) all the calls will be |   `com.mattermost.calls` \>            |
| handled by this external service.          |   `rtcdserviceurl`                     |
|                                            | - Environment variable:                |
| This is an optional field. Changing this   |   `MM_CALLS_RTCD_SERVICE_URL`          |
| setting requires a plugin restart to take  |                                        |
| effect.                                    |                                        |
+--------------------------------------------+----------------------------------------+

:::: note
::: title
Note
:::

\- This setting is applicable only to self-hosted deployments. - The
environment variable `MM_CALLS_RTCD_URL` is deprecated in favor of
`MM_CALLS_RTCD_SERVICE_URL`. - The client will self-register the first
time it connects to the service and store the authentication key in the
database. If no client ID is explicitly provided, the diagnostic ID of
the Mattermost installation will be used. - The service URL supports
credentials in the form `http://clientID:authKey@hostname`.
Alternatively these can be passed through environment overrides to the
Mattermost server, namely `MM_CALLS_RTCD_CLIENT_ID` and
`MM_CALLS_RTCD_AUTH_KEY` - The client will self-register the first time
it connects to the service and store the authentication key in the
database. If no client ID is explicitly provided, the diagnostic ID of
the Mattermost installation will be used. - The service URL supports
credentials in the form `http://clientID:authKey@hostname`.
Alternatively these can be passed through environment overrides to the
Mattermost server, namely `MM_CALLS_RTCD_CLIENT_ID` and
`MM_CALLS_RTCD_AUTH_KEY`
::::

### Max call participants

+----------------------------+-----------------------------------------+
| This setting limits the    | - System Config path: **Plugins \>      |
| number of participants     |   Calls**                               |
| that can join a single     | - `config.json` setting:                |
| call.                      |   `PluginSettings` \> `Plugins` \>      |
|                            |   `com.mattermost.calls` \>             |
| Default is **0** (no       |   `maxcallparticipants`                 |
| limit).                    | - Environment variable:                 |
|                            |   `MM_CALLS_MAX_CALL_PARTICIPANTS`      |
+----------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

\- This setting is applicable only to self-hosted deployments. - The
environment variable `MM_CALLS_MAX_PARTICIPANTS` is deprecated in favor
of `MM_CALLS_MAX_CALL_PARTICIPANTS`. - This setting is optional, but the
recommended maximum number of participants is **50**. Call participant
limits greatly depends on instance resources. See the
`Calls self-hosted deployment </administration-guide/configure/calls-deployment>`{.interpreted-text
role="doc"} documentation for details.
::::

### ICE servers configurations

+--------------------------------------------------------------+----------------------------------+
| This setting stores a list of ICE servers (STUN/TURN) in     | - System Config path: **Plugins  |
| JSON format to be used by the service.                       |   \> Calls**                     |
|                                                              | - `config.json` setting:         |
| This is an optional field. Changing this setting may require |   `PluginSettings` \> `Plugins`  |
| a plugin restart to take effect.                             |   \> `com.mattermost.calls` \>   |
|                                                              |   `iceserversconfigs`            |
| Default is                                                   | - Environment variable:          |
| `[{"urls": ["stun:stun.global.calls.mattermost.com:3478"]}]` |   `MM_CALLS_ICE_SERVERS_CONFIGS` |
+--------------------------------------------------------------+----------------------------------+

:::: note
::: title
Note
:::

\- This setting is applicable only to self-hosted deployments. - The
configurations above, containing STUN and TURN servers, are sent to the
clients and used to generate local candidates. - If hosting calls
through the plugin (i.e. not using the
`rtcd service <administration-guide/configure/calls-deployment:the rtcd service>`{.interpreted-text
role="ref"}) any configured STUN server may also be used to find the
instance\'s public IP when none is provided through the
`ICE Host Override <administration-guide/configure/plugins-configuration-settings:ice host override>`{.interpreted-text
role="ref"} option.
::::

**Example**

> ``` json
> [
>  {
>     "urls":[
>        "stun:stun.global.calls.mattermost.com:3478"
>     ]
>  },
>  {
>     "urls":[
>        "turn:turn.example.com:3478"
>     ],
>     "username":"webrtc",
>     "credentials":"turnpassword"
>  }
> ]
> ```

**Example (Using generated TURN credentials)**

> ``` json
> [{
>     "urls": ["turn:turn.example.com:443"]
> }]
> ```

:::: note
::: title
Note
:::

To get TURN generated credentials to work you must provide a secret
through the *TURN static auth secret* setting below.
::::

### TURN static auth secret

+-------------------------+--------------------------------------------+
| A static secret used to | - System Config path: **Plugins \> Calls** |
| generate short-lived    | - `config.json` setting: `PluginSettings`  |
| credentials for TURN    |   \> `Plugins` \> `com.mattermost.calls`   |
| servers.                |   \> `turnstaticauthsecret`                |
|                         | - Environment variable:                    |
| This is an optional     |   `MM_CALLS_TURN_STATIC_AUTH_SECRET`       |
| field.                  |                                            |
+-------------------------+--------------------------------------------+

:::: note
::: title
Note
:::

This setting is applicable only to self-hosted deployments.
::::

### TURN credentials expiration

+--------------------------+--------------------------------------------------+
| The expiration, in       | - System Config path: **Plugins \> Calls**       |
| minutes, of the          | - `config.json` setting: `PluginSettings` \>     |
| short-lived credentials  |   `Plugins` \> `com.mattermost.calls` \>         |
| generated for TURN       |   `turncredentialsexpirationminutes`             |
| servers.                 | - Environment variable:                          |
|                          |   `MM_CALLS_TURN_CREDENTIALS_EXPIRATION_MINUTES` |
| Default is **1440** (one |                                                  |
| day).                    |                                                  |
+--------------------------+--------------------------------------------------+

:::: note
::: title
Note
:::

This setting is applicable only to self-hosted deployments.
::::

### Server side TURN

+-------------------------------+--------------------------------------+
| - **true**: The RTC server    | - System Config path: **Plugins \>   |
|   will use the configured     |   Calls**                            |
|   TURN candidates for         | - `config.json` setting:             |
|   server-initiated            |   `PluginSettings` \> `Plugins` \>   |
|   connections.                |   `com.mattermost.calls` \>          |
| - **false**: TURN will be     |   `serversideturn`                   |
|   used only on the            | - Environment variable:              |
|   client-side.                |   `MM_CALLS_SERVER_SIDE_TURN`        |
|                               |                                      |
| Changing this setting         |                                      |
| requires a plugin restart to  |                                      |
| take effect.                  |                                      |
+-------------------------------+--------------------------------------+

:::: note
::: title
Note
:::

This setting is applicable only to self-hosted deployments.
::::

### Allow screen sharing

+-------------------------+--------------------------------------------+
| - **true**: Call        | - System Config path: **Plugins \> Calls** |
|   participants will be  | - `config.json` setting: `PluginSettings`  |
|   allowed to share      |   \> `Plugins` \> `com.mattermost.calls`   |
|   their screen.         |   \> `allowscreensharing`                  |
| - **false**: Call       | - Environment variable:                    |
|   participants won\'t   |   `MM_CALLS_ALLOW_SCREEN_SHARING`          |
|   be allowed to share   |                                            |
|   their screen.         |                                            |
|                         |                                            |
| Changing this setting   |                                            |
| requires a plugin       |                                            |
| restart to take effect. |                                            |
+-------------------------+--------------------------------------------+

:::: note
::: title
Note
:::

This setting is applicable only to self-hosted deployments.
::::

### Enable simulcast for screen sharing (Experimental)

+----------------------------------+-----------------------------------+
| - **true**: Enables simulcast    | - System Config path: **Plugins   |
|   for screen sharing. This can   |   \> Calls**                      |
|   help to improve screen sharing | - `config.json` setting:          |
|   quality.                       |   `PluginSettings` \> `Plugins`   |
| - **false**: Disables simulcast  |   \> `com.mattermost.calls` \>    |
|   for screen sharing.            |   `enablesimulcast`               |
|                                  | - Environment variable:           |
|                                  |   `MM_CALLS_ENABLE_SIMULCAST`     |
+----------------------------------+-----------------------------------+

:::: note
::: title
Note
:::

- This experimental setting is applicable only to self-hosted
  deployments.
- This functionality requires Calls plugin version \>= v0.16.0 and
  `rtcd` version \>= v0.10.0 (when in use).
- Avoid enabling both this experimental configuration setting and the
  [Enable AV1](#enable-av1-experimental) experimental configuration
  setting at the same time.
::::

### Enable call recordings

+--------------------------------------+--------------------------------+
| - **true**: Allows call hosts to     | - System Config path:          |
|   record meeting video and audio.    |   **Plugins \> Calls**         |
| - **false**: **(Default)** Call      | - `config.json` setting:       |
|   recording functionality is not     |   `PluginSettings` \>          |
|   available to hosts.                |   `Plugins` \>                 |
|                                      |   `com.mattermost.calls` \>    |
| Recordings include the entire call   |   `enablerecordings`           |
| window view along with               | - Environment variable:        |
| participants\' audio track and any   |   `MM_CALLS_ENABLE_RECORDINGS` |
| shared screen video. Recordings are  |                                |
| stored in Mattermost.                |                                |
|                                      |                                |
| Changing this setting requires a     |                                |
| plugin restart to take effect.       |                                |
+--------------------------------------+--------------------------------+

:::: note
::: title
Note
:::

This setting is applicable only to self-hosted deployments.
::::

### Job service URL

+--------------------------------------+-------------------------------+
| The URL to a running job service     | - System Config path:         |
| where all the processing related to  |   **Plugins \> Calls**        |
| recordings happens. The recorded     | - `config.json` setting:      |
| files produced are stored in         |   `PluginSettings` \>         |
| Mattermost.                          |   `Plugins` \>                |
|                                      |   `com.mattermost.calls` \>   |
| This is a required field. Changing   |   `jobserviceurl`             |
| this setting requires a plugin       | - Environment variable:       |
| restart to take effect.              |   `MM_CALLS_JOB_SERVICE_URL`  |
+--------------------------------------+-------------------------------+

:::: note
::: title
Note
:::

- This setting is applicable only to self-hosted deployments.
- The client will self-register the first time it connects to the
  service and store the authentication key in the database. If no client
  ID is explicitly provided, the diagnostic ID of the Mattermost
  installation will be used.
- The service URL supports credentials in the form
  `http://clientID:authKey@hostname`. Alternatively these can be passed
  through environment overrides to the Mattermost server, namely
  `MM_CALLS_JOB_SERVICE_CLIENT_ID` and `MM_CALLS_JOB_SERVICE_AUTH_KEY`.
- As of Calls v0.25 it\'s possible to override the site URL used by jobs
  to connect by setting the `MM_CALLS_RECORDER_SITE_URL` or
  `MM_CALLS_TRANSCRIBER_SITE_URL` environment variables respectively.
  This can be helpful to avoid the jobs from connecting through the
  public Site URL configured in Mattermost and thus potentially bypass
  the public network.
::::

### Maximum call recording duration

+------------------------------------+-------------------------------------+
| The maximum duration of a call     | - System Config path: **Plugins \>  |
| recording in minutes.              |   Calls**                           |
|                                    | - `config.json` setting:            |
| The default is **60**. The maximum |   `PluginSettings` \> `Plugins` \>  |
| is **180**. This is a required     |   `com.mattermost.calls` \>         |
| value.                             |   `maxrecordingduration`            |
|                                    | - Environment variable:             |
|                                    |   `MM_CALLS_MAX_RECORDING_DURATION` |
+------------------------------------+-------------------------------------+

:::: note
::: title
Note
:::

This setting is applicable only to self-hosted deployments.
::::

### Call recording quality

+------------------------------+---------------------------------------+
| The audio and video quality  | - System Config path: **Plugins \>    |
| of call recordings.          |   Calls**                             |
| Available options are:       | - `config.json` setting:              |
| *Low*, *Medium* and *High*.  |   `PluginSettings` \> `Plugins` \>    |
|                              |   `com.mattermost.calls` \>           |
| The default is **Medium**.   |   `recordingquality`                  |
| This is a required value.    | - Environment variable:               |
|                              |   `MM_CALLS_RECORDING_QUALITY`        |
+------------------------------+---------------------------------------+

:::: note
::: title
Note
:::

\- This setting is applicable only to self-hosted deployments. - The
quality setting will affect the performance of the job service and the
file size of recordings. Refer to the
`deployment section <administration-guide/configure/calls-deployment:configure recording, transcriptions, and live captions>`{.interpreted-text
role="ref"} for more information.
::::

### Enable call transcriptions

+-----------------------------------------------+------------------------------------+
| - **true**: Enables automatic transcriptions  | - System Config path: **Plugins \> |
|   of calls.                                   |   Calls**                          |
| - **false**: **(Default)** Call               | - `config.json` setting:           |
|   transcriptions functionality is disabled.   |   `PluginSettings` \> `Plugins` \> |
|                                               |   `com.mattermost.calls` \>        |
| Transcriptions are generated from the call    |   `enabletranscriptions`           |
| participants\' audio tracks and the resulting | - Environment variable:            |
| files are attached to the call thread when    |   `MM_CALLS_ENABLE_TRANSCRIPTIONS` |
| the recording ends. Captions will be          |                                    |
| optionally rendered on top of the recording   |                                    |
| file video player.                            |                                    |
+-----------------------------------------------+------------------------------------+

:::: note
::: title
Note
:::

\- This setting is applicable only to self-hosted deployments. - The
ability to enable call transcriptions in Mattermost calls is currently
in
`Beta <administration-guide/manage/feature-labels:beta>`{.interpreted-text
role="ref"}. - This server-side configuration setting is available from
plugin version 0.22. - Call transcriptions require
`call recordings <administration-guide/configure/plugins-configuration-settings:enable call recordings>`{.interpreted-text
role="ref"} to be enabled.
::::

### Transcriber model size

+-------------------------------------------------+-------------------------------------+
| The speech-to-text model size to use. Heavier   | - System Config path: **Plugins \>  |
| models will produce more accurate results at    |   Calls**                           |
| the expense of processing time and resources    | - `config.json` setting:            |
| usage. Available options are: *Tiny*, *Base*    |   `PluginSettings` \> `Plugins` \>  |
| and *Small*.                                    |   `com.mattermost.calls` \>         |
|                                                 |   `transcribermodelsize`            |
| The default is **Base**. This is a required     | - Environment variable:             |
| value.                                          |   `MM_CALLS_TRANSCRIBER_MODEL_SIZE` |
+-------------------------------------------------+-------------------------------------+

:::: note
::: title
Note
:::

\- This setting is applicable only to self-hosted deployments. - This
setting is available starting in plugin version 0.22. The model size
setting will affect the performance of the job service. Refer to the
`configure call recordings, transcriptions, and live captions <administration-guide/configure/calls-deployment:configure recording, transcriptions, and live captions>`{.interpreted-text
role="ref"} documentation for more information.
::::

### Call transcriber threads

+-----------------------------------------------+--------------------------------------+
| The number of threads used by the post-call   | - System Config path: **Plugins \>   |
| transcriber. This must be in the range \[1,   |   Calls**                            |
| numCPUs\].                                    | - `config.json` setting:             |
|                                               |   `PluginSettings` \> `Plugins` \>   |
| The default is 2. This is a required value.   |   `com.mattermost.calls` \>          |
|                                               |   `transcribernumthread`             |
|                                               | - Environment variable:              |
|                                               |   `MM_CALLS_TRANSCRIBER_NUM_THREADS` |
+-----------------------------------------------+--------------------------------------+

:::: note
::: title
Note
:::

\- This setting is applicable only to self-hosted deployments. - The
call transcriber threads setting will affect the performance of the job
service. Refer to the
`configure call recordings, transcriptions, and live captions <administration-guide/configure/calls-deployment:configure recording, transcriptions, and live captions>`{.interpreted-text
role="ref"} documentation for more information. This setting is
available starting in plugin version 0.26.2.
::::

### Enable live captions

+---------------------------+------------------------------------------+
| - **true**: Enables live  | - System Config path: **Plugins \>       |
|   captioning of calls.    |   Calls**                                |
| - **false**:              | - `config.json` setting:                 |
|   **(Default)** Live      |   `PluginSettings` \> `Plugins` \>       |
|   captions functionality  |   `com.mattermost.calls` \>              |
|   is disabled.            |   `enablelivecaptions`                   |
|                           | - Environment variable:                  |
| Live captions are         |   `MM_CALLS_ENABLE_LIVE_CAPTIONS`        |
| generated from the call   |                                          |
| participants\' audio      |                                          |
| tracks and the resulting  |                                          |
| captions can be           |                                          |
| optionally displayed on   |                                          |
| the call clients by       |                                          |
| selecting the **\[cc\]**  |                                          |
| option.                   |                                          |
+---------------------------+------------------------------------------+

:::: note
::: title
Note
:::

\- The ability to enable live call captions in Mattermost calls is
currently in
`Beta <administration-guide/manage/feature-labels:beta>`{.interpreted-text
role="ref"}. - This server-side configuration setting is available
starting in plugin version 0.26.2. - Live captions require
`call recordings <administration-guide/configure/plugins-configuration-settings:enable call recordings>`{.interpreted-text
role="ref"} and
`call transcriptions <administration-guide/configure/plugins-configuration-settings:enable call transcriptions>`{.interpreted-text
role="ref"} to be enabled.
::::

### Live captions: Model size

+---------------------------------------------------+---------------------------------------+
| The speech-to-text model size to use for live     | - System Config path: **Plugins \>    |
| captions. While heavier models can produce more   |   Calls**                             |
| accurate results, live captioning requires the    | - `config.json` setting:              |
| transcriber to process up to ten seconds of audio |   `PluginSettings` \> `Plugins` \>    |
| within two seconds. Therefore a maximum of size   |   `com.mattermost.calls` \>           |
| [base]{.title-ref} is recommended. Available      |   `livecaptionsmodelsize`             |
| options are: *Tiny*, *Base* and *Small*.          | - Environment variable:               |
|                                                   |   `MM_CALLS_LIVE_CAPTIONS_MODEL_SIZE` |
| The default is **Tiny**. This is a required       |                                       |
| value.                                            |                                       |
+---------------------------------------------------+---------------------------------------+

:::: note
::: title
Note
:::

\- This setting is applicable only to self-hosted deployments. - This
setting is available starting in plugin version 0.26.2. The model size
setting will affect the performance of the job service. Refer to the
[performance and scalability
recommendations](https://github.com/mattermost/calls-offloader/blob/master/docs/performance.md)
documentation for more information.
::::

### Live captions: Number of transcribers used per call

+--------------------------------------------------+---------------------------------------------+
| The number of separate live captions             | - System Config path: **Plugins \> Calls**  |
| transcribers for each call. Each transcribes one | - `config.json` setting: `PluginSettings`   |
| audio stream at a time. The product of           |   \> `Plugins` \> `com.mattermost.calls` \> |
| LiveCaptionsNumTranscribers \*                   |   `livecaptionsnumtranscribers`             |
| LiveCaptionsNumThreadsPerTranscriber must be in  | - Environment variable:                     |
| the range \[1, numCPUs\].                        |   `MM_CALLS_LIVE_CAPTIONS_NUM_TRANSCRIBERS` |
|                                                  |                                             |
| The default is 1. This is a required value.      |                                             |
+--------------------------------------------------+---------------------------------------------+

:::: note
::: title
Note
:::

\- This setting is applicable only to self-hosted deployments. - This
setting is available starting in plugin version 0.26.2. The live
captions number of transcribers setting will affect the performance of
the job service. Refer to the [performance and scalability
recommendations](https://github.com/mattermost/calls-offloader/blob/master/docs/performance.md)
documentation for more information.
::::

### Live captions: Number of threads per transcriber

+-------------------------------------------------+--------------------------------------------------------+
| The number of threads per live-captions         | - System Config path: **Plugins \> Calls**             |
| transcriber. The product of                     | - `config.json` setting: `PluginSettings` \> `Plugins` |
| `LiveCaptionsNumTranscribers` \*                |   \> `com.mattermost.calls` \>                         |
| `LiveCaptionsNumThreadsPerTranscriber` must be  |   `livecaptionsnumthreadspertranscriber`               |
| in the range \[1, numCPUs\].                    | - Environment variable:                                |
|                                                 |   `MM_CALLS_LIVE_CAPTIONS_NUM_THREADS_PER_TRANSCRIBER` |
| The default is 2. This is a required value.     |                                                        |
+-------------------------------------------------+--------------------------------------------------------+

:::: note
::: title
Note
:::

\- This setting is applicable only to self-hosted deployments. - This
setting is available starting in plugin version 0.26.2. The live
captions number of threads per transcriber setting will affect the
performance of the job service. Refer to the [performance and
scalability
recommendations](https://github.com/mattermost/calls-offloader/blob/master/docs/performance.md)
documentation for more information
::::

### Live captions language

+-----------------------------------+-------------------------------------+
| The language passed to the live   | - System Config path: **Plugins \>  |
| captions transcriber. Should be a |   Calls**                           |
| 2-letter ISO 639 Set 1 language   | - `config.json` setting:            |
| code, e.g. \'en\'.                |   `PluginSettings` \> `Plugins` \>  |
|                                   |   `com.mattermost.calls` \>         |
| If blank, the lange will be set   |   `livecaptionslanguage`            |
| to \'en\' (English) as default.   | - Environment variable:             |
|                                   |   `MM_CALLS_LIVE_CAPTIONS_LANGUAGE` |
+-----------------------------------+-------------------------------------+

:::: note
::: title
Note
:::

This setting is applicable only to self-hosted deployments.
::::

### (Experimental) Enable IPv6

+----------------------------------------+-----------------------------+
| - **true**: The RTC service will work  | - System Config path:       |
|   in dual-stack mode, listening for    |   **Plugins \> Calls**      |
|   IPv6 connections and generating      | - `config.json` setting:    |
|   candidates in addition to IPv4 ones. |   `PluginSettings` \>       |
| - **false**: **(Default)** The RTC     |   `Plugins` \>              |
|   service will only listen for IPv4    |   `com.mattermost.calls` \> |
|   connections.                         |   `enableipv6`              |
|                                        | - Environment variable:     |
| Changing this setting requires a       |   `MM_CALLS_ENABLE_IPV6`    |
| plugin restart to take effect.         |                             |
+----------------------------------------+-----------------------------+

:::: note
::: title
Note
:::

\- This setting is applicable only to self-hosted deployments. - This
setting is available starting in plugin version 0.17, and is only
applicable when not running calls through the standalone `rtcd` service.
::::

### Enable call ringing

+----------------------------+-----------------------------------------+
| - **true**: Ringing        | - System Config path: **Plugins \>      |
|   functionality is         |   Calls**                               |
|   enabled. Direct and      | - `config.json` setting:                |
|   group message            |   `PluginSettings` \> `Plugins` \>      |
|   participants receive a   |   `com.mattermost.calls` \>             |
|   desktop app alert and a  |   `enableringing`                       |
|   ringing notification     | - Environment variable:                 |
|   when a call starts.      |   `MM_CALLS_ENABLE_RINGING`             |
| - **false**: **(Default**) |                                         |
|   Ringing functionality is |                                         |
|   disabled.                |                                         |
+----------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

The ability to enable call ringing in Mattermost calls is in
`Beta <administration-guide/manage/feature-labels:beta>`{.interpreted-text
role="ref"}.
::::

### Enable AV1 (Experimental)

+---------------------------+------------------------------------------+
| - **true**: Enables the   | - System Config path: **Plugins \>       |
|   ability to use the AV1  |   Calls**                                |
|   codec to encode screen  | - `config.json` setting:                 |
|   sharing tracks. Can     |   `PluginSettings` \> `Plugins` \>       |
|   result in improved      |   `com.mattermost.calls` \> `enableAV1`  |
|   screen sharing quality  | - Environment variable:                  |
|   via clients that        |   `MM_CALLS_ENABLE_AV1`                  |
|   support AV1 encoding.   |                                          |
| - **false**:              |                                          |
|   **(Default**) AV1 codec |                                          |
|   is disabled for screen  |                                          |
|   sharing tracks.         |                                          |
+---------------------------+------------------------------------------+

:::: note
::: title
Note
:::

Avoid enabling both this experimental configuration setting and the
[Enable simulcast for screen
sharing](#enable-simulcast-for-screen-sharing-experimental) experimental
configuration setting at the same time.
::::

### Enable DC signaling (Experimental)

+---------------------------+------------------------------------------+
| - **true**: Clients will  | - System Config path: **Plugins \>       |
|   use WebRTC data         |   Calls**                                |
|   channels for signaling  | - `config.json` setting:                 |
|   of media tracks (i.e.,  |   `PluginSettings` \> `Plugins` \>       |
|   voice, screen). This    |   `com.mattermost.calls` \>              |
|   can result in a more    |   `enabledcsignaling`                    |
|   efficient and less      | - Environment variable:                  |
|   race-prone process,     |   `MM_CALLS_ENABLE_DC_SIGNALING`         |
|   especially in case of   |                                          |
|   poor network            |                                          |
|   connections.            |                                          |
| - **false**:              |                                          |
|   **(Default**) Clients   |                                          |
|   will use WebSockets for |                                          |
|   signaling media tracks. |                                          |
+---------------------------+------------------------------------------+

:::: note
::: title
Note
:::

- Version v0.18.0 or higher of the
  `rtcd service <administration-guide/configure/calls-deployment:the rtcd service>`{.interpreted-text
  role="ref"} is required for this functionality to work when hosting
  calls through the dedicated WebRTC service.
- Use caution when enabling this experimental configuration setting
  since it determines how the system handles part of the setup for
  WebRTC-based calls. Enabling this configuration setting may make the
  call setup a bit faster or more reliable in certain situations.
::::

------------------------------------------------------------------------

## AI Agents

:::: note
::: title
Note
:::

Mattermost Agents is formerly known as Mattermost Copilot.
::::

Access the following Mattermost Agents configuration settings in the
System Console by going to **Plugins \> Agents**.

### Enable plugin

+----------------------------+-----------------------------------------+
| - **true**: Enables the    | - System Config path: **Plugins \>      |
|   Agents plugin on your    |   Agents**                              |
|   Mattermost workspace.    | - `config.json` setting: N/A            |
| - **false**: **(Default)** | - Environment variable: N/A             |
|   Disables the Agents      |                                         |
|   plugin.                  |                                         |
+----------------------------+-----------------------------------------+

### Display name

+----------------------------+-----------------------------------------+
| The bot\'s display name in | - System Config path: **Plugins \>      |
| Mattermost used to         |   Agents \> Add an AI Bot**             |
| distinguish the bot from   | - `config.json` setting: N/A            |
| other bots in the system.  | - Environment variable: N/A             |
|                            |                                         |
| String input.              |                                         |
+----------------------------+-----------------------------------------+

### Agent username

+----------------------------+-----------------------------------------+
| The bot\'s username that   | - System Config path: **Plugins \>      |
| can be used to \@mention   |   Agents \> Add an AI Bot**             |
| the bot in a channel.      | - `config.json` setting: N/A            |
|                            | - Environment variable: N/A             |
| String input.              |                                         |
+----------------------------+-----------------------------------------+

### Agent avatar

+----------------------------+-----------------------------------------+
| Upload an image to use as  | - System Config path: **Plugins \>      |
| the agent\'s avatar in     |   Agents \> Add an AI Bot**             |
| Mattermost.                | - `config.json` setting: N/A            |
|                            | - Environment variable: N/A             |
| Image upload interface.    |                                         |
+----------------------------+-----------------------------------------+

### Service

+----------------------------+-----------------------------------------+
| Select the LLM service     | - System Config path: **Plugins \>      |
| provider to use for AI     |   Agents \> Add an AI Bot**             |
| assistance.                | - `config.json` setting: N/A            |
|                            | - Environment variable: N/A             |
| Available options:         |                                         |
| **OpenAI**, **OpenAI       |                                         |
| Compatible**, **Azure**,   |                                         |
| **Anthropic**, and **Ask   |                                         |
| Sage**.                    |                                         |
+----------------------------+-----------------------------------------+

### Username

+----------------------------+-----------------------------------------+
| The username used to       | - System Config path: **Plugins \>      |
| authenticate with the      |   Agents \> Add an AI Bot**             |
| **Ask Sage** LLM service.  | - `config.json` setting: N/A            |
|                            | - Environment variable: N/A             |
| String input required.     |                                         |
+----------------------------+-----------------------------------------+

### Password

+----------------------------+-----------------------------------------+
| The password used to       | - System Config path: **Plugins \>      |
| authenticate with the      |   Agents \> Add an AI Bot**             |
| **Ask Sage** LLM service.  | - `config.json` setting: N/A            |
|                            | - Environment variable: N/A             |
| String input required.     |                                         |
| This value is encrypted    |                                         |
| when stored.               |                                         |
+----------------------------+-----------------------------------------+

### API URL

+----------------------------+-----------------------------------------+
| The endpoint that          | - System Config path: **Plugins \>      |
| Mattermost will use to     |   Agents \> Add an AI Bot**             |
| communicate with the       | - `config.json` setting: N/A            |
| LLM\'s API. Required for   | - Environment variable: N/A             |
| **OpenAI Compatible** and  |                                         |
| **Azure** LLM services.    |                                         |
|                            |                                         |
| String input (URL format). |                                         |
+----------------------------+-----------------------------------------+

### API key

+----------------------------+-----------------------------------------+
| The key used to            | - System Config path: **Plugins \>      |
| authenticate requests to   |   Agents \> Add an AI Bot**             |
| the LLM\'s API. Required   | - `config.json` setting: N/A            |
| for **OpenAI**, **OpenAI   | - Environment variable: N/A             |
| Compatible**, and          |                                         |
| **Anthropic** LLM          |                                         |
| services.                  |                                         |
|                            |                                         |
| String input. This value   |                                         |
| is encrypted when stored.  |                                         |
+----------------------------+-----------------------------------------+

### Organization ID

+----------------------------+-----------------------------------------+
| Ensures that requests are  | - System Config path: **Plugins \>      |
| billed and processed under |   Agents \> Add an AI Bot**             |
| the correct organization,  | - `config.json` setting: N/A            |
| where applicable.          | - Environment variable: N/A             |
| Supported for **OpenAI**,  |                                         |
| **OpenAI Compatible**, and |                                         |
| **Azure** LLM services.    |                                         |
|                            |                                         |
| String input.              |                                         |
+----------------------------+-----------------------------------------+

### Send user ID

+----------------------------+-----------------------------------------+
| - **true**: Includes       | - System Config path: **Plugins \>      |
|   unique user identifiers  |   Agents \> Add an AI Bot**             |
|   in API requests to the   | - `config.json` setting: N/A            |
|   LLM for analytics,       | - Environment variable: N/A             |
|   personalization, and     |                                         |
|   auditing purposes.       |                                         |
| - **false**: **(Default)** |                                         |
|   Does not include user    |                                         |
|   identifiers.             |                                         |
|                            |                                         |
| Review LLM data privacy    |                                         |
| policies before enabling   |                                         |
| this setting.              |                                         |
+----------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

We recommend reviewing LLM data privacy policies to confirm whether
transmitting user information is acceptable and secure within your
organization\'s regulatory framework. Do not enable when you need to
conform to strict privacy regulations (e.g., GDPR) that limit sharing
user-identifiable data with external services.
::::

### Default model

+----------------------------+-----------------------------------------+
| The specific LLM that will | - System Config path: **Plugins \>      |
| be used to process queries |   Agents \> Add an AI Bot**             |
| if no other model is       | - `config.json` setting: N/A            |
| explicitly selected.       | - Environment variable: N/A             |
| Supported for all LLM      |                                         |
| services.                  |                                         |
|                            |                                         |
| String input (model name). |                                         |
+----------------------------+-----------------------------------------+

### Input token limit

+----------------------------+-----------------------------------------+
| The maximum number of      | - System Config path: **Plugins \>      |
| tokens (chunks of text,    |   Agents \> Add an AI Bot**             |
| including words,           | - `config.json` setting: N/A            |
| punctuation, or special    | - Environment variable: N/A             |
| characters) that the       |                                         |
| selected LLM can process   |                                         |
| in a single prompt or      |                                         |
| request.                   |                                         |
|                            |                                         |
| Numerical value. Directly  |                                         |
| impacts the size of user   |                                         |
| queries that can be        |                                         |
| handled.                   |                                         |
+----------------------------+-----------------------------------------+

### Output token limit

+----------------------------+-----------------------------------------+
| The maximum number of      | - System Config path: **Plugins \>      |
| tokens (chunks of text,    |   Agents \> Add an AI Bot**             |
| including words,           | - `config.json` setting: N/A            |
| punctuation, or special    | - Environment variable: N/A             |
| characters) that the LLM   |                                         |
| can generate in its        |                                         |
| response to a query.       |                                         |
|                            |                                         |
| Numerical value. Must be   |                                         |
| greater than 0 for         |                                         |
| **Anthropic** LLM          |                                         |
| services.                  |                                         |
+----------------------------+-----------------------------------------+

### Streaming timeout

+----------------------------+-----------------------------------------+
| Determines how long the    | - System Config path: **Plugins \>      |
| system will wait for a     |   Agents \> Add an AI Bot**             |
| response from the LLM when | - `config.json` setting: N/A            |
| using streaming            | - Environment variable: N/A             |
| (real-time) output mode.   |                                         |
| Supported for **OpenAI**,  |                                         |
| **OpenAI Compatible**, and |                                         |
| **Azure** LLM services.    |                                         |
|                            |                                         |
| Numerical value (in        |                                         |
| seconds). If the LLM takes |                                         |
| longer than the configured |                                         |
| timeout, the connection is |                                         |
| terminated.                |                                         |
+----------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

Streaming allows LLMs to display the response gradually as it\'s being
generated, creating a smoother and more interactive experience for
users.
::::

### Custom instructions

+----------------------------+-----------------------------------------+
| Preset specific contextual | - System Config path: **Plugins \>      |
| or behavioral guidance for |   Agents \> Add an AI Bot**             |
| the LLM. Helps tailor the  | - `config.json` setting: N/A            |
| model\'s responses to      | - Environment variable: N/A             |
| align with your            |                                         |
| organization\'s needs,     |                                         |
| tone, or expectations.     |                                         |
| Supported for all LLM      |                                         |
| services.                  |                                         |
|                            |                                         |
| Text input. Instructions   |                                         |
| that the model will        |                                         |
| implicitly follow for      |                                         |
| every interaction,         |                                         |
| providing consistency and  |                                         |
| adaptability.              |                                         |
+----------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

Custom instructions can include behavioral guidance, tone preferences,
contextual functions, and organizational preferences. This ensures
responses adhere to your organization\'s language and tone guidelines
and aligns the model\'s behavior with specific roles or purposes.
::::

### Enable vision

+----------------------------+-----------------------------------------+
| - **true**: Enables the    | - System Config path: **Plugins \>      |
|   LLM to process and       |   Agents \> Add an AI Bot**             |
|   generate responses that  | - `config.json` setting: N/A            |
|   incorporate              | - Environment variable: N/A             |
|   image-related input or   |                                         |
|   output. Supported for    |                                         |
|   **OpenAI**, **OpenAI     |                                         |
|   Compatible**, **Azure**, |                                         |
|   and **Anthropic** LLM    |                                         |
|   services.                |                                         |
| - **false**: **(Default)** |                                         |
|   Disables vision          |                                         |
|   capabilities.            |                                         |
+----------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

This feature is in
`Beta <administration-guide/manage/feature-labels:beta>`{.interpreted-text
role="ref"}. When enabled, the LLM can interact with prompts that
include image-related input, such as image analysis, visual-related
assistance, and visual outputs, where supported.
::::

### Enable tools

+----------------------------+-----------------------------------------+
| - **true**: Enables the    | - System Config path: **Plugins \>      |
|   LLM to leverage          |   Agents \> Add an AI Bot**             |
|   additional tools or      | - `config.json` setting: N/A            |
|   plugins to enhance its   | - Environment variable: N/A             |
|   capabilities. Supported  |                                         |
|   for **OpenAI**, **OpenAI |                                         |
|   Compatible**, **Azure**, |                                         |
|   and **Anthropic** LLM    |                                         |
|   services.                |                                         |
| - **false**: **(Default)** |                                         |
|   Disables tool            |                                         |
|   capabilities.            |                                         |
+----------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

When enabled, advanced features beyond basic query processing allow the
LLM to perform specialized tasks like retrieving data, integrating with
external APIs, or performing computations, where supported.
::::

### Channel access

+----------------------------+-----------------------------------------+
| Determines whether the bot | - System Config path: **Plugins \>      |
| can consume the contents   |   Agents \> Add an AI Bot**             |
| of a given channel and     | - `config.json` setting: N/A            |
| provide answers only from  | - Environment variable: N/A             |
| content available in the   |                                         |
| channel. Supported for all |                                         |
| LLM services.              |                                         |
|                            |                                         |
| Available options: **Allow |                                         |
| for all channels**,        |                                         |
| **Allow for selected       |                                         |
| channels**, **Block        |                                         |
| selected channels**, and   |                                         |
| **Block all channels**.    |                                         |
+----------------------------+-----------------------------------------+

### User access

+----------------------------+-----------------------------------------+
| Determines whether users   | - System Config path: **Plugins \>      |
| who chat with this bot can |   Agents \> Add an AI Bot**             |
| get private assistance     | - `config.json` setting: N/A            |
| about content across all   | - Environment variable: N/A             |
| channels the user has      |                                         |
| access to. Supported for   |                                         |
| all LLM services.          |                                         |
|                            |                                         |
| Available options: **Allow |                                         |
| for all users**, **Allow   |                                         |
| for selected users**, and  |                                         |
| **Block selected users**.  |                                         |
+----------------------------+-----------------------------------------+

### Default agent

+----------------------------+-----------------------------------------+
| Select the default bot to  | - System Config path: **Plugins \>      |
| use for AI functions when  |   Agents \> AI Functions**              |
| multiple agents are        | - `config.json` setting: N/A            |
| configured. Based on       | - Environment variable: N/A             |
| defined agents.            |                                         |
+----------------------------+-----------------------------------------+

### Allowed upstream hostnames

+----------------------------+-----------------------------------------+
| Comma-separated list of    | - System Config path: **Plugins \>      |
| hostnames that LLMs are    |   Agents \> AI Functions**              |
| allowed to contact when    | - `config.json` setting: N/A            |
| using tools. Supports      | - Environment variable: N/A             |
| wildcards like             |                                         |
| `*.mydomain.com`.          |                                         |
|                            |                                         |
| Example:                   |                                         |
| `mattermost.atlassian.net` |                                         |
| to allow JIRA tool use.    |                                         |
+----------------------------+-----------------------------------------+

### Enable LLM trace

+----------------------------+-----------------------------------------+
| - **true**: Enables        | - System Config path: **Plugins \>      |
|   tracing of LLM requests  |   Agents \> Debug**                     |
|   and outputs full         | - `config.json` setting: N/A            |
|   conversation data to the | - Environment variable: N/A             |
|   logs. Supported for all  |                                         |
|   LLM services.            |                                         |
| - **false**: **(Default)** |                                         |
|   Disables LLM request     |                                         |
|   tracing.                 |                                         |
+----------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

Use this setting for debugging purposes only. When enabled, it may log
sensitive conversation data.
::::

### Enable embedding search

+-----------------------------+----------------------------------------+
| - **Composite**: Enables    | - System Config path: **Plugins \>     |
|   experimental embedding    |   Agents \> Embedding Search**         |
|   search capabilities for   | - `config.json` setting: N/A           |
|   semantic search across    | - Environment variable: N/A            |
|   Mattermost content using  |                                        |
|   pgvector and              |                                        |
|   OpenAI-compatible         |                                        |
|   endpoints.                |                                        |
| - **Disabled**:             |                                        |
|   **(Default)** Disables    |                                        |
|   embedding search          |                                        |
|   capabilities.             |                                        |
+-----------------------------+----------------------------------------+

:::: note
::: title
Note
:::

Embedding search requires an Enterprise license and is available as an
`experimental <administration-guide/manage/feature-labels:experimental>`{.interpreted-text
role="ref"} feature. You must also enable the `pgvector` extension in
your PostgreSQL database. Performance may vary with large datasets.
::::

### Embedding provider type

+----------------------------+-----------------------------------------+
| Select the provider for    | - System Config path: **Plugins \>      |
| generating embeddings for  |   Agents \> Embedding Search**          |
| semantic search. Available | - `config.json` setting: N/A            |
| options: **OpenAI** and    | - Environment variable: N/A             |
| **OpenAI Compatible**.     |                                         |
+----------------------------+-----------------------------------------+

### API Key

+----------------------------+-----------------------------------------+
| The API key used to        | - System Config path: **Plugins \>      |
| authenticate requests to   |   Agents \> Embedding Search**          |
| the embedding provider\'s  | - `config.json` setting: N/A            |
| API. Required for **OpenAI | - Environment variable: N/A             |
| Compatible** embedding     |                                         |
| providers.                 |                                         |
|                            |                                         |
| String input. This value   |                                         |
| is encrypted when stored.  |                                         |
+----------------------------+-----------------------------------------+

### Model

+----------------------------+-----------------------------------------+
| The specific embedding     | - System Config path: **Plugins \>      |
| model to use for           |   Agents \> Embedding Search**          |
| generating vector          | - `config.json` setting: N/A            |
| representations of         | - Environment variable: N/A             |
| content. Must be           |                                         |
| compatible with the        |                                         |
| selected embedding         |                                         |
| provider.                  |                                         |
|                            |                                         |
| String input (model name). |                                         |
+----------------------------+-----------------------------------------+

### API URL

+----------------------------+-----------------------------------------+
| The endpoint URL for the   | - System Config path: **Plugins \>      |
| **OpenAI-compatible**      |   Agents \> Embedding Search**          |
| embedding API.             | - `config.json` setting: N/A            |
|                            | - Environment variable: N/A             |
| Required string input (URL |                                         |
| format).                   |                                         |
+----------------------------+-----------------------------------------+

### Dimensions

+----------------------------+-----------------------------------------+
| The dimensionality of the  | - System Config path: **Plugins \>      |
| embedding vectors, which   |   Agents \> Embedding Search**          |
| must match the chosen      | - `config.json` setting: N/A            |
| embedding model. Common    | - Environment variable: N/A             |
| values include 1536 for    |                                         |
| OpenAI                     |                                         |
| text-embedding-ada-002 and |                                         |
| 3072 for                   |                                         |
| text-embedding-3-large.    |                                         |
|                            |                                         |
| Numerical input. Common    |                                         |
| values are 768, 1024, or   |                                         |
| 1536, depending on the     |                                         |
| model.                     |                                         |
+----------------------------+-----------------------------------------+

### Chunking strategy

+----------------------------+-----------------------------------------+
| The method used to split   | - System Config path: **Plugins \>      |
| content into smaller       |   Agents \> Embedding Search**          |
| chunks for embedding       | - `config.json` setting: N/A            |
| generation. Available      | - Environment variable: N/A             |
| options: **Sentences**,    |                                         |
| **Paragraphs**, **Fixed    |                                         |
| Size**.                    |                                         |
|                            |                                         |
| Choose based on your       |                                         |
| content type and search    |                                         |
| requirements.              |                                         |
+----------------------------+-----------------------------------------+

### Chunk size

+----------------------------+-----------------------------------------+
| The maximum size of each   | - System Config path: **Plugins \>      |
| content chunk in           |   Agents \> Embedding Search**          |
| characters. Recommended    | - `config.json` setting: N/A            |
| range is 512-1024          | - Environment variable: N/A             |
| characters. The optimal    |                                         |
| value varies by chunking   |                                         |
| strategy.                  |                                         |
|                            |                                         |
| Numerical input.           |                                         |
+----------------------------+-----------------------------------------+

### Chunk overlap

+----------------------------+-----------------------------------------+
| The number of tokens that  | - System Config path: **Plugins \>      |
| consecutive chunks share   |   Agents \> Embedding Search**          |
| for better context         | - `config.json` setting: N/A            |
| continuity. Recommended    | - Environment variable: N/A             |
| range is 20-50 characters  |                                         |
| for **Fixed Size**         |                                         |
| chunking.                  |                                         |
|                            |                                         |
| Numerical input.           |                                         |
+----------------------------+-----------------------------------------+

### Minimum chunk size ratio

+----------------------------+-----------------------------------------+
| The minimum ratio for      | - System Config path: **Plugins \>      |
| chunk size validation to   |   Agents \> Embedding Search**          |
| ensure sentence and        | - `config.json` setting: N/A            |
| paragraph chunks meet size | - Environment variable: N/A             |
| requirements. Used to      |                                         |
| filter out chunks that are |                                         |
| too small releative to the |                                         |
| configured chunk size.     |                                         |
|                            |                                         |
| Numerical input (decimal   |                                         |
| ratio).                    |                                         |
+----------------------------+-----------------------------------------+

### Reindex all posts

+----------------------------+-----------------------------------------+
| Select **Reindex Posts**   | - System Config path: **Plugins \>      |
| to trigger a complete      |   Agents \> Embedding Search**          |
| reindexing of all posts    | - `config.json` setting: N/A            |
| for embedding search. Use  | - Environment variable: N/A             |
| this control to rebuild    |                                         |
| the search index when      |                                         |
| changing                   |                                         |
| embeddingproviders,        |                                         |
| models, or chunking        |                                         |
| configurations.            |                                         |
|                            |                                         |
| Monitor indexing progress  |                                         |
| during the reindexing      |                                         |
| process.                   |                                         |
+----------------------------+-----------------------------------------+

------------------------------------------------------------------------

## GitLab

See the
`Connect GitLab to Mattermost </integrations-guide/gitlab>`{.interpreted-text
role="doc"} product documentation for details.

------------------------------------------------------------------------

## GitHub

See the
`Connect GitHub to Mattermost </integrations-guide/github>`{.interpreted-text
role="doc"} product documentation for details.

------------------------------------------------------------------------

## Jira

See the
`Connect Jira to Mattermost </integrations-guide/jira>`{.interpreted-text
role="doc"} product documentation for available
`Mattermost configuration options <integrations-guide/jira:mattermost configuration>`{.interpreted-text
role="ref"}.

------------------------------------------------------------------------

## Legal hold

See the
`Legal holds </administration-guide/comply/legal-hold>`{.interpreted-text
role="doc"} product documentation for details.

------------------------------------------------------------------------

## Microsoft Calendar Integration

See the
`Connect Microsoft Calendar Integration to Mattermost </integrations-guide/microsoft-calendar>`{.interpreted-text
role="doc"} product documentation for available
`Mattermost configuration options <integrations-guide/microsoft-calendar:enable and configure the microsoft calendar integration in mattermost>`{.interpreted-text
role="ref"}.

------------------------------------------------------------------------

## Microsoft Teams Meetings

See the
`Connect Microsoft Teams Meetings to Mattermost </integrations-guide/microsoft-teams-meetings>`{.interpreted-text
role="doc"} product documentation for available
`Mattermost configuration options <integrations-guide/microsoft-teams-meetings:enable and configure the microsoft teams meetings integration in mattermost>`{.interpreted-text
role="ref"}.

------------------------------------------------------------------------

## MS Teams

Mattermost for Microsoft Teams enables you to break through siloes in a
mixed Mattermost and Teams environment by forwarding real-time chat
notifications from Teams to Mattermost.

:::: tip
::: title
Tip
:::

Download our [Mattermost for Microsoft Teams
datasheet](https://mattermost.com/mattermost-for-microsoft-teams-datasheet/)
to learn how Mattermost helps your organization get more from your
Microsoft tools.
::::

Access the following configuration settings in the System Console by
going to **Plugins \> MS Teams**.

### Enable plugin

+----------------------------------------+-----------------------------+
| Enable the Mattermost for Microsoft    | - System Config path:       |
| Teams plugin for all Mattermost teams. |   **Plugins \> MS Teams**   |
|                                        | - `config.json` setting:    |
| - **true**: Enables MS Teams plugin on |   N/A                       |
|   your Mattermost workspace.           | - Environment variable: N/A |
| - **false**: **(Default)** Disables    |                             |
|   the MS Teams plugin.                 |                             |
+----------------------------------------+-----------------------------+

:::: note
::: title
Note
:::

Use the [Enabled Teams](#enabled-teams) configuration option to specify
which Mattermost teams synchronize direct and group messages with
Microsoft Teams chats.
::::

### Tenant ID

+-----------------------------------------+----------------------------+
| Specify the Microsoft Teams Tenant ID   | - System Config path:      |
| from the Azure portal.                  |   **Plugins \> MS Teams**  |
|                                         | - `config.json` setting:   |
|                                         |   N/A                      |
|                                         | - Environment variable:    |
|                                         |   N/A                      |
+-----------------------------------------+----------------------------+

### Client ID

+-----------------------------------------+----------------------------+
| Specify the Microsoft Teams Client ID   | - System Config path:      |
| of your registered OAuth app in the     |   **Plugins \> MS Teams**  |
| Azure portal.                           | - `config.json` setting:   |
|                                         |   N/A                      |
|                                         | - Environment variable:    |
|                                         |   N/A                      |
+-----------------------------------------+----------------------------+

### Client secret

+-----------------------------------------+----------------------------+
| Specify the client secret of your       | - System Config path:      |
| registered OAuth app in Azure portal.   |   **Plugins \> MS Teams**  |
|                                         | - `config.json` setting:   |
| Alpha-numeric value.                    |   N/A                      |
|                                         | - Environment variable:    |
|                                         |   N/A                      |
+-----------------------------------------+----------------------------+

### At rest encryption key

+-----------------------------------------+----------------------------+
| Regenerate a new encryption secret.     | - System Config path:      |
| This encryption secret will be used to  |   **Plugins \> MS Teams**  |
| encrypt and decrypt the OAuth token.    | - `config.json` setting:   |
|                                         |   N/A                      |
| Alpha-numeric value.                    | - Environment variable:    |
|                                         |   N/A                      |
+-----------------------------------------+----------------------------+

:::: note
::: title
Note
:::

Select **Regenerate** to generate a new key.
::::

### Webhook secret

+-----------------------------------------+----------------------------+
| Generate the webhook secret that        | - System Config path:      |
| Microsoft Teams will use to send        |   **Plugins \> MS Teams**  |
| messages to Mattermost.                 | - `config.json` setting:   |
|                                         |   N/A                      |
|                                         | - Environment variable:    |
|                                         |   N/A                      |
+-----------------------------------------+----------------------------+

:::: note
::: title
Note
:::

Select **Regenerate** to generate a new key.
::::

### Use the evaluation API pay model

+-----------------------------------------+----------------------------+
| Enable this only for testing purposes.  | - System Config path:      |
| You need the pay model to be able to    |   **Plugins \> MS Teams**  |
| support enough message notifications to | - `config.json` setting:   |
| work in a real world scenario.          |   N/A                      |
|                                         | - Environment variable:    |
| - **true**: Enables the evaluation API  |   N/A                      |
|   pay model.                            |                            |
| - **false**: **(Default)** Disables the |                            |
|   evaluation API pay model.             |                            |
+-----------------------------------------+----------------------------+

### Sync notifications

+----------------------------------------+-----------------------------+
| Notify connected users in Mattermost   | - System Config path:       |
| on receipt of a chat or group chat     |   **Plugins \> MS Teams**   |
| from Microsoft Teams.                  | - `config.json` setting:    |
|                                        |   N/A                       |
| - **true**: **(Default)** Sync         | - Environment variable: N/A |
|   notifications of chat messages for   |                             |
|   any connected user that enables the  |                             |
|   feature.                             |                             |
| - **false**: Do not sync               |                             |
|   notifications.                       |                             |
+----------------------------------------+-----------------------------+

### Maximum size of attachments to support complete one time download

+--------------------------------------+-------------------------------+
| Specify the maximum file size, in    | - System Config path:         |
| mebibytes (MiB), of attachments that |   **Plugins \> MS Teams**     |
| can be loaded into memory.           | - `config.json` setting: N/A  |
| Attachment files larger than this    | - Environment variable: N/A   |
| value will be streamed from          |                               |
| Microsoft Teams to Mattermost.       |                               |
|                                      |                               |
| Numerical value. Default is **20**   |                               |
| MiB.                                 |                               |
+--------------------------------------+-------------------------------+

### Buffer size for streaming files

+--------------------------------------+-------------------------------+
| Specify the buffer size, in          | - System Config path:         |
| mebibytes (MiB), for streaming       |   **Plugins \> MS Teams**     |
| attachment files from Microsoft      | - `config.json` setting: N/A  |
| Teams to Mattermost.                 | - Environment variable: N/A   |
|                                      |                               |
| Numerical value. Default is **20**   |                               |
| MiB.                                 |                               |
+--------------------------------------+-------------------------------+

------------------------------------------------------------------------

## Performance metrics

See the
`Monitor performance metrics </administration-guide/scale/collect-performance-metrics>`{.interpreted-text
role="doc"} product documentation for available
`Mattermost configuration options <administration-guide/scale/collect-performance-metrics:mattermost configuration>`{.interpreted-text
role="ref"}.

------------------------------------------------------------------------

## Collaborative playbooks

Use collaborative playbooks in Mattermost to provide structure,
monitoring and automation for repeatable, team-based processes
integrated with the Mattermost platform.

Access the following configuration settings in the System Console by
going to **Plugins \> Collaborative playbooks**.

### Enable plugin

+-------------------------------------------+--------------------------+
| - **true**: **(Default)** Enables         | - System Config path:    |
|   collaborative Playbooks on your         |   **Plugins \>           |
|   Mattermost workspace.                   |   Collaborative          |
| - **false**: Disables collaborative       |   playbooks**            |
|   Playbooks on your Mattermost workspace. | - `config.json` setting: |
|                                           | - Environment variable:  |
+-------------------------------------------+--------------------------+

### Enabled teams

+------------------------------------------+---------------------------+
| Enable collaborative playbooks for all   | - System Config path:     |
| Mattermost teams, or for only selected   |   **Plugins \>            |
| teams.                                   |   Collaborative           |
|                                          |   playbooks**             |
|                                          | - `config.json` setting:  |
|                                          | - Environment variable:   |
+------------------------------------------+---------------------------+

### Enable experimental features

+------------------------------------------+---------------------------+
| - **true**: Enables experimental         | - System Config path:     |
|   playbooks features on your Mattermost  |   **Plugins \>            |
|   workspace.                             |   Collaborative           |
| - **false**: Disables experimental       |   playbooks**             |
|   playbooks features on your Mattermost  | - `config.json` setting:  |
|   workspace.                             | - Environment variable:   |
+------------------------------------------+---------------------------+

------------------------------------------------------------------------

## ServiceNow

See the
`Connect ServiceNow to Mattermost </integrations-guide/servicenow>`{.interpreted-text
role="doc"} product documentation for available
`Mattermost configuration options <integrations-guide/servicenow:mattermost configuration>`{.interpreted-text
role="ref"}.

------------------------------------------------------------------------

## Zoom

See the
`Connect Zoom to Mattermost </integrations-guide/zoom>`{.interpreted-text
role="doc"} product documentation for available
`Mattermost configuration options <integrations-guide/zoom:mattermost configuration>`{.interpreted-text
role="ref"}.

------------------------------------------------------------------------

## config.json-only settings

The following self-hosted deployment settings are only configurable in
the `config.json` file and are not available in the System Console.

### Signature public key files

This setting isn\'t available in the System Console and can only be set
in `config.json`.

In addition to the Mattermost plugin signing key built into the server,
each public key specified here is trusted to validate plugin signatures.

:::: important
::: title
Important
:::

From Mattermost v10.11, pre-packaged plugins require signature
validation on startup. Distributions that bundle custom pre-packaged
plugins **must** configure this setting with their custom public keys to
ensure proper validation of their signed plugins. Use
`PluginSettings.SignaturePublicKeyFiles` to define custom plugin signing
keys.

When bundling custom plugins:

- Drop both the plugin files and their corresponding `.sig` signature
  files into the `prepackaged_plugins` directory.
- Add your custom public key using this configuration setting to
  validate the signatures.
::::

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is
  `"SignaturePublicKeyFiles": {}` with string array input consisting of
  contents that are relative or absolute paths to signature files.

  -----------------------------------------------------------------------

### Chimera OAuth proxy URL

This setting isn\'t available in the System Console and can only be set
in `config.json`.

Specify the [Chimera](https://github.com/mattermost/chimera) URL used by
Mattermost plugins to connect with pre-created OAuth applications.

  -----------------------------------------------------------------------
  This feature\'s `config.json` setting is `"ChimeraOAuthProxyUrl": {}`
  with string input.

  -----------------------------------------------------------------------
