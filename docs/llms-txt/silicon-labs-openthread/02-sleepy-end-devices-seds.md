# Source: https://docs.silabs.com/openthread/3.0.0/openthread-sleepy-devices/02-sleepy-end-devices-seds.md

# Sleepy End Devices (SEDs)

SEDs achieve lower power consumption by sleeping for a set period and periodically waking up to send data polls (MAC data requests) to their parent. If the parent has any pending data to send to its child, it is indicated by a frame pending bit in the 802.15.4 Acknowledgement to the data poll. This lets the Sleepy End Device keep its receiver on for the anticipated data which the parent will send immediately.

Starting with Thread 1.2, the OpenThread stack automatically also makes use of the 802.15.4 Enhanced Frame Pending feature, which lets the SED use regular data messages to get an indication of pending data. Without this feature, the SED would have to send a data poll on its scheduled period to extract the data from the parent.

![SED Polling](/openthread-sleepy-devices/0.2/images/sld415-image1.png)

Note that a smaller poll period (that is, polling more frequently) means better latency at the cost of higher power consumption.

## SED Configuration in OpenThread

### APIs

- `otLinkGetPollPeriod`/`otLinkSetPollPeriod`: Get/Set/Clear user-specified/external data poll period for sleepy end device.

> **Warning**: The following poll-related configuration items have standardized values in the Thread specification. Changing them might affect the certifiability of your component or end product.

- OPENTHREAD_CONFIG_MAC_MAX_TX_ATTEMPTS_INDIRECT_POLLS: Maximum number of received IEEE 802.15.4 Data Requests for a queued indirect transaction.
- OPENTHREAD_CONFIG_MAC_ATTACH_DATA_POLL_PERIOD: The Data Poll period during attach in milliseconds.
- OPENTHREAD_CONFIG_MAC_MINIMUM_POLL_PERIOD: Minimum poll period in milliseconds.
- OPENTHREAD_CONFIG_MAC_RETX_POLL_PERIOD: Retransmission poll period in milliseconds.
