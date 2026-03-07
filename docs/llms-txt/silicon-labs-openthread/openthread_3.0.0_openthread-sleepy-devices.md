# Source: https://docs.silabs.com/openthread/3.0.0/openthread-sleepy-devices/index.md

# Configuring and Building OpenThread Applications for Sleepy Devices

**Minimal Thread Devices (MTDs)** communicate only through their Thread Router parent and cannot relay messages for other devices. **Sleepy Devices** are MTDs that achieve low-power duty cycling by turning off their transceiver to reduce power. For more information on these device roles in a Thread network, refer to the Thread specification or [Thread Fundamentals](/openthread/3.0.0/thread-fundamentals).

There are two categories of Sleepy Devices:

- Regular Sleepy End Devices (SEDs) that poll for new messages when they wake up.
- Synchronized Sleepy End Devices (SSEDs) that use IEEE 802.15.4 Coordinated Sampled Listening (CSL) so that the parent can forward its messages during designated transmission and reception windows.

Silicon Labs provides sample applications to demonstrate both kinds of Sleepy End Device behavior.

Sleepy Devices can greatly help extend the battery power of power-limited devices. Note that simply building a Sleepy Device application does not guarantee the lowest power consumption, as this is dependent on many configuration parameters as well as the application’s general use case. Additionally, any application code such as shell or CLI, LCD code, or other peripheral components can also adversely affect the power consumption. For an example of such current consumption optimization, refer to the Silicon Labs example at [https://github.com/SiliconLabs/zigbee_applications/tree/master/zigbee_sed_z3switch](https://github.com/SiliconLabs/zigbee_applications/tree/master/zigbee_sed_z3switch).

> **Note**: This document describes how to configure Sleepy Devices. Further detail about power consumption, optimizing current consumption values, or providing benchmark values for various platforms is outside the document's scope.