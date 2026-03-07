# Source: https://docs.silabs.com/openthread/3.0.0/concurrent-mp-soc/02-concurrent-multiprotocol-cmp-sample-application-z3-light-ot-ftd.md

# Concurrent Multiprotocol (CMP) Sample Application (z3-light_ot-ftd)

![Zigbee + OpenThread Concurrent Multiprotocol Application](/concurrent-mp-soc/0.1/images/sld678-image1.png)

![Zigbee + Bluetooth + OpenThread Concurrent Multiprotocol Application](/concurrent-mp-soc/0.1/images/sld678-image2.png)

The CMP sample application consists of a Z3Light, which is a Zigbee router, and an OpenThread FTD (Full Thread Device). Both protocol stacks operate by multiplexing a single radio.

> **Note**: SiSDK 2024.12 allows inclusion of `rail_util_ieee802154_fast_channel_switching` and `rail_util_dma` components. This allows Zigbee and Thread networks to operate on 2 different radio channels. Note that the concurrent listening feature becomes active only when both networks are up. This feature can result in a decrease in receive sensitivity.

If this feature is not required, these components can be removed. However, it is imperative to make sure that both Zigbee and OpenThread networks are on the same channel.

## RTOS

Within the CMP application, scheduling is managed using a Real Time Operating System (RTOS). Each protocol runs in a dedicated RTOS task. The Zigbee and OpenThread tasks operate at the same priority while the Command Line Interface (CLI) is made available using a CLI RTOS task that operates at a lower priority.

> **CAUTION for SDK 4.4 and older**: It is critical to note that Zigbee and OpenThread APIs are not thread-safe. Calling them from different threads can result in unexpected behavior. In addition, any references to EmberMessageBuffer must be contained within the Zigbee task.

As of SiSDK 2024.6, Zigbee stack APIs are thread-safe. Application framework APIs are protected by a mutex in the CLI task context. If they are to be called from a custom RTOS task, you are expected to surround the calls with `sl_zigbee_af_acquire_lock` and `sl_zigbee_af_release_lock`. It is also important to note that this version also introduced the standardization of all function names. Refer to the [Zigbee API Reference Manual](https://docs.silabs.com/zigbee/latest/zigbee-api-ref-v7-vs-v8/02-renaming-changes-in-zigbee) for more details. It is important to note that any references or allocations of zigbee buffers (for example, `sli_legacy_buffer_manager_allocate_buffer`) must be contained within the Zigbee task to avoid unexpected operation.

## Command Line Interface

This application supports all CLI commands that can be found in the Z3Light sample application. A subset of the OpenThread CLI has been ported to demonstrate form, join and ping operations. This functionality can be extended further, if necessary, by following the example commands in the ot_up_cli.c file from the ot_up_cli component. Note that before SiSDK 2024.06, OpenThread APIs should only be invoked from `sl_ot_rtos_application_tick` since they are not thread-safe.

### OpenThread Commissioning

This device can be commissioned on to an OpenThread network out-of-band using CLI commands. Setting the OpenThread network parameters, such as network key and channel, before starting the network allows the CMP device to join a Thread network as a child or router device. The table below lists the OpenThread CLI commands.

|CLI Command|Description|
|---|---|
|dataset|View OpenThread network configuration.|
|dataset_new|Creates a new OpenThread dataset.|
|dataset_commit_active|Commits dataset to NVM.|
|factory_reset|Removes all NVM OpenThread settings.|
|dataset_networkkey|Presets the network key on the device to help with joining an existing OpenThread network out-of-band.|
|dataset_channel|Presets the radio channel used by the OpenThread network. This command can be used to force both Zigbee and OpenThread networks to use the same radio channel.|
|dataset_pan_id|Presets the PAN ID on the device to help with joining the OpenThread network out-of-band.|
|dataset_extended_pan_id|Presets the extended PAN ID on the device to help with joining the OpenThread network out-of-band.|
|ifconfig_up|Enables OpenThread interface.|
|thread_start|Enables and attaches OpenThread protocol operation.|
|thread_state|Reads current status: offline, disabled, detached, child, router, or leader.|