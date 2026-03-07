# Source: https://docs.silabs.com/openthread/3.0.0/configuring-openthread-apps-for-thread-1-3/02-including-thread-1-3-features-in-an-openthread-border-router.md

# Including Thread 1.3 features in an OpenThread Border Router

Silicon Labs provides several sample OpenThread RCP applications. By default, the RCP applications on supported Silicon Labs hardware automatically support Thread 1.3 features if they are present on the host (the Border Router, which is Silicon Labs’ supported RCP model). None of the Thread 1.3 features are RCP-specific, so turning them on or off for the RCP sample application has no effect.

Refer to [Using the Silicon Labs RCP with the OpenThread Border Router](/openthread/{build-docspace-version}/using-sl-rcp-with-openthread-border-router) for detailed instructions on how to build an OpenThread Border Router for Raspberry Pi 3B+ or above. You must use a Thread protocol version 1.3 RCP with a Border Router that is also running a stack at protocol version 1.3.

Thread 1.3 features can be enabled on the border router separately by making sure the POSIX stack enables the following CMake flags. These flags are enabled by default with the current default OpenThread Border Router offering. (See [Thread 1.3 Configuration Flags](01-including-thread-1-3-features-in-soc-applications#including-thread-13-features-in-soc-applications) for more information on their purpose.)

<table>
    <thead>
        <tr>
            <th>CMake Flag</th>
            <th>Thread 1.3 Configuration Flag</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>OT_DNS_CLIENT</td>
            <td>OPENTHREAD_CONFIG_DNS_CLIENT_ENABLE</td>
        </tr>
        <tr>
            <td>OT_DNSSD_SERVER</td>
            <td>OPENTHREAD_CONFIG_DNSSD_SERVER_ENABLE</td>
        </tr>
        <tr>
            <td>OT_SRP_CLIENT</td>
            <td>OPENTHREAD_CONFIG_SRP_CLIENT_ENABLE</td>
        </tr>
        <tr>
            <td>OT_SRP_SERVER</td>
            <td>OPENTHREAD_CONFIG_SRP_SERVER_ENABLE</td>
        </tr>
        <tr>
            <td>OT_TREL</td>
            <td>
                OPENTHREAD_CONFIG_RADIO_LINK_TREL_ENABLE<br>
                Make sure that the <code>OPENTHREAD_CONFIG_POSIX_APP_TREL_INTERFACE_NAME</code> property is also set to the IPv6 link on which you wish to enable TREL (via the trel:// argument).<br>
                On a network with at least two border routers, if TREL is enabled on both border routers on the same shared infrastructure link, they can automatically use that link to provide a single Thread partition.
            </td>
        </tr>
    </tbody>
</table>

You can install a pre-built Docker container with OpenThread Border Router: [https://hub.docker.com/r/siliconlabsinc/openthread-border-router/tags](https://hub.docker.com/r/siliconlabsinc/openthread-border-router/tags).

Or you can manually install an OpenThread Border Router by following the steps in [Using the Silicon Labs Co-Processors with the OpenThread Border Router](/openthread/{build-docspace-version}/using-sl-coprocessors-with-openthread-border-router) or [https://openthread.io/guides/border-router/build](https://openthread.io/guides/border-router/build).