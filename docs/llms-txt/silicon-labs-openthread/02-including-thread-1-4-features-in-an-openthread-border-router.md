# Source: https://docs.silabs.com/openthread/3.0.0/configuring-openthread-apps-for-thread-1-4/02-including-thread-1-4-features-in-an-openthread-border-router.md

# Including Thread 1.4 features in an OpenThread Border Router

Silicon Labs provides several sample OpenThread RCP applications. On supported Silicon Labs hardware, RCP firmware will already include all functionality required for Thread 1.4 operations. Since Thread 1.4 features are border router-level features (not RCP-specific), enabling or disabling them in the RCP sample application has no effect.

Refer to [Using the Silicon Labs RCP with the OpenThread Border Router](/openthread/{build-docspace-version}/using-sl-rcp-with-openthread-border-router) for detailed instructions on how to build an OpenThread Border Router for Raspberry Pi 3B+ or above. You must use a Thread protocol version 1.4 RCP with a Border Router that is also running a stack at protocol version 1.4.

Most Thread 1.4 features can be enabled on the border router simply by setting the protocol version to Thread 1.4, as they will be enabled by default. However, you can review the following CMake flags for more information. (See [Thread 1.4 Configuration Flags](01-including-thread-1-4-features-in-soc-applications#including-thread-14-features-in-soc-applications) for more information on their purpose.)

|CMake Flag|Thread 1.4 Configuration Flag|
|---|---|
|OT_BORDER_AGENT_EPSKC|OPENTHREAD_CONFIG_BORDER_AGENT_EPHEMERAL_KEY_ENABLE|
|OT_MESH_DIAG|OPENTHREAD_CONFIG_MESH_DIAG_ENABLE|
|OT_BORDER_ROUTING_DHCP6_PD|OPENTHREAD_CONFIG_BORDER_ROUTING_DHCP6_PD_ENABLE|
|OT_BLE_TCAT|OPENTHREAD_CONFIG_BLE_TCAT_ENABLE|

Except for the TCAT feature, all of the other border router features are automatically enabled when building for Thread 1.4 version.

You can install a pre-built Docker container with OpenThread Border Router:

[https://hub.docker.com/r/siliconlabsinc/openthread-border-router/tags](https://hub.docker.com/r/siliconlabsinc/openthread-border-router/tags)

Or you can manually install an OpenThread Border Router by following the steps in [Using the Silicon Labs RCP with the OpenThread Border Router](/openthread/{build-docspace-version}/using-sl-rcp-with-openthread-border-router) or [https://openthread.io/guides/border-router/build](https://openthread.io/guides/border-router/build).