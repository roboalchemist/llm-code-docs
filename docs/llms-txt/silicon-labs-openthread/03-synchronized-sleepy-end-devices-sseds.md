# Source: https://docs.silabs.com/openthread/3.0.0/openthread-sleepy-devices/03-synchronized-sleepy-end-devices-sseds.md

# Synchronized Sleepy End Devices (SSEDs)

An SSED is an rx-off-when-idle end device that uses the IEEE 802.15.4-2015 CSL feature, available beginning with Thread 1.2, to further optimize power consumption. An SSED CSL receiver is synchronized with a parent that is a CSL transmitter, so both parent and child require implementation of this feature.

Coordinated Sampled Listening (CSL) involves the receiver sampling for any data from the transmitter during set intervals. The transmitter always targets the synchronized window, eliminating the need for data polling and optimizing power consumption. In the following figure, note the comparison of activity with a regular SED.

![Comparison of SED and SSED Power Consumption](/openthread-sleepy-devices/0.2/images/sld415-image2.png)

SSEDs automatically reduce the average TX-ON time by avoiding wasted data polling. Therefore, optimized power consumption depends on configuring minimal average RX-ON time for a platform and the given application use case.

Note that an SSED periodically must send some packets within a specified timeout to maintain synchronization with its parent. In OpenThread, the auto-synchronization happens automatically using data polls (usually at a much less frequent rate than regular polling). Note that other data packets from the SSED, including application data, can also be used by the stack to re-synchronize the connection as needed.

## IEEE 802.15.4-2015 Coordinated Sampled Listening (CSL)

### CSL Parameters and CSL Information Elements

Following are the parameters that indicate CSL configuration on a receiver:

- **CSL Period**: A CSL receiver performs periodic channel sampling by configuring a non-zero period value _(see macCslPeriod in [IEEE802154-2015]_).
- **CSL Phase**: Thread uses the CSL phase definition from _[IEEE802154-2015]_: “_the time from the first symbol of the frame containing the CSL IE … until the next channel sample_”.  
  - “First symbol” is interpreted as the first symbol of the MAC header.  
  - The CSL receiver should be ready to receive slightly earlier than the preamble time (CSL-Phase – CCA time) and should stay in receive mode until after the CSL-Phase time to detect the Sync-Frame-Detect (SFD) of the incoming packet from the CSL transmitter. These timing values account for the platform’s implementation and accuracy.
- **CSL Channel**: If the CSL receiver expects to receive and process unsynchronized CSL transmissions, then it should use a different channel from the Thread network channel for receiving CSL messages. However, most Thread applications' use cases for SSEDs only involve synchronized communications, so the CSL channel can remain the same as the network channel.
- **CSL Timeout**: Timeout before which an SSED and its parent must re-synchronize to keep the connection valid and active.

CSL synchronization happens by the SSED child communicating CSL parameters to its parent. The CSL channel and timeout are initially configured during mesh link establishment (MLE) attach. The period and phase are communicated by the receiver in IEEE 802.15.4 Information Elements in the MAC header. The **CSL IE** in the IEEE 802.15.4 MAC header is a tuple containing **[CSL period, CSL phase]**.

An SSED device should include CSL IEs in all the IEEE 802.15.4 Commands, ACKs, and Data frames unicast to its parent router. IEEE 802.15.4 ACKs that include IEs are called **Enhanced Acknowledgements** (EnhAcks), as defined in _[IEEE802154-2015]_.

Note that the CSL period, channel, and timeout are configured by the application, whereas the phase value is dynamically determined on the SSED relative to the exact moment the frame containing the CSL IE is sent out to the parent. CSL retransmissions involve recalculating the CSL IE with a new phase value.

### OpenThread CSL Timing Calculations

The CSL transmitter’s delay for its scheduled transmission points to the moment when the end of the SFD will be present at the receiver’s local antenna, relative to the local radio clock. The CSL receiver should be ready to receive the first symbol of a scheduled frame’s Sync Header (SHR) at its own receive window start time. If no SHR is detected at the end of its minimum receive window, the radio should be turned off or switched to TX mode as needed.

The CSL sample window of the CSL receiver extends before and after its calculated sample time. This marks a timestamp in the CSL sample window where a frame would be received in "ideal conditions" if there was no inaccuracy or clock drift. However, the realistic sampling representation is as follows:

![sampling representation](/openthread-sleepy-devices/0.2/images/sld415-image3.png)

- **timeAhead** accounts for the SSED to wake and be ready for RX.
- **timeAfter** is the when the RX-ON window closes. If needed, the Silicon Labs radio driver automatically extends the duration of the receive window.
- **Uncert** is the fixed uncertainty (that is, random jitter) of the arrival time of CSL transmissions. In addition to uncertainty accumulated over elapsed time, the CSL channel sample ("RX window") must be extended by twice this value such that an actual transmission is guaranteed to be detected by the local receiver in the presence of random arrival time jitter.
- The calculations also account for clock drift and the estimated worst-case accuracy (maximum ± deviation from the nominal frequency) of the local radio clock used to schedule CSL operations.

## SSED Configuration in OpenThread

**APIs:**

- `otPlatRadioEnableCsl` : Enable or disable CSL receiver.
- `otPlatRadioUpdateCslSampleTime`: Update CSL sample time in radio driver.
- `otPlatRadioGetCslAccuracy`: Get the current estimated worst-case accuracy of the local radio clock in PPM.
- `otPlatRadioGetCslUncertainty`: The fixed uncertainty (that is, random jitter) of the arrival time of CSL transmissions received by this device in 10-microsecond units.
- `otLinkGetCslChannel` / `otLinkSetCslChannel`: Get/Set CSL Channel.
- `otLinkGetCslPeriod` / `otLinkSetCslPeriod`: Get/Set CSL Period.
- `otLinkGetCslTimeout` / `otLinkSetCslTimeout`: Get/Set CSL Timeout.
- `otLinkIsCslEnabled`: Indicates whether or not CSL is enabled.
- `otLinkIsCslSupported`: Indicates whether the device is connected to a parent that supports CSL.

**Configurable parameters:**

The following parameters are configurable in the OpenThread stack component in Simplicity Studio or at run-time using the Silicon Labs Configurator (SLC):

- OPENTHREAD_CONFIG_MAC_CSL_RECEIVER_ENABLE: Configures CSL receiver support at build time.
- SL_OPENTHREAD_CSL_TX_UNCERTAINTY: CSL Scheduling Uncertainty (±10 microseconds). SSED’s receive window will increase by twice this value.
- OPENTHREAD_CONFIG_MAC_CSL_DEBUG_ENABLE: Enables CSL debug printing (will affect timing, so use only for debug).

**WARNING:** The following configuration parameters have standardized values for Silicon Labs platforms. Changing them might affect certifiability of your component or end product:

- OPENTHREAD_CONFIG_MAC_CSL_TRANSMITTER_ENABLE: Enables CSL transmitter functions. Automatically enabled for Thread 1.2 or greater devices.
- OPENTHREAD_CONFIG_MAC_CSL_AUTO_SYNC_ENABLE: Configures CSL auto synchronization based on data poll mechanism in Thread 1.2. This is turned off for some reference devices for certification testing purposes. For OpenThread device end products, this should never be turned off.
- OPENTHREAD_CONFIG_MAC_CSL_MIN_PERIOD: Minimum CSL period in milliseconds.
- OPENTHREAD_CONFIG_MAC_CSL_MAX_TIMEOUT: Maximum CSL timeout in seconds.
- OPENTHREAD_CONFIG_CSL_TIMEOUT: Default CSL timeout in seconds.
- OPENTHREAD_CONFIG_MAC_CSL_REQUEST_AHEAD_US: For a CSL transmitter, this indicates the time, measured in microseconds, by which the MAC should advance the delivery of the CSL frame to the radio layer before the actual transmit time.
- OPENTHREAD_CONFIG_CSL_TRANSMIT_TIME_AHEAD: Transmission scheduling and ramp-up time needed for the CSL transmitter to be ready, in microseconds.
- OPENTHREAD_CONFIG_CSL_RECEIVE_TIME_AHEAD: Reception scheduling and ramp up time needed for the CSL receiver to be ready, in microseconds.
- OPENTHREAD_CONFIG_MIN_RECEIVE_ON_AHEAD: The minimum time (in microseconds) before the MAC Header (MHR) start that the radio should be in the receive state in order to properly receive any IEEE 802.15.4 frame. Defaults to the duration of Sync Header (SHR) + PHY Header (PHR).
- OPENTHREAD_CONFIG_MIN_RECEIVE_ON_AFTER: The minimum time (in microseconds) after the MHR start that the radio should be in receive state in order to properly receive any IEEE 802.15.4 frame. For Silicon Labs products, this value is zero, as the Silicon Labs radio driver will automatically extend the receive window when the SHR is detected.
- SL_OPENTHREAD_HFXO_ACCURACY: Worst case HFXO XTAL accuracy in units of ± ppm. Set to platform’s SL_DEVICE_INIT_HFXO_PRECISION value.
- SL_OPENTHREAD_LFXO_ACCURACY: Worst case LFXO XTAL accuracy in units of ± ppm. Set to platform’s SL_DEVICE_INIT_LFXO_PRECISION value.