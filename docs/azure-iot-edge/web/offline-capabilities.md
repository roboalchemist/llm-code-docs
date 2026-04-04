# Source: https://learn.microsoft.com/en-us/azure/iot-edge/offline-capabilities

Operate Azure IoT Edge devices offline | Microsoft Learn [Skip to main content ][Skip to Ask Learn chat experience ]
This browser is no longer supported. 

Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support. 
[Download Microsoft Edge ][More info about Internet Explorer and Microsoft Edge ]Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents [Read in English ]Add Add to plan [Edit ]
#### Share via 
[Facebook ][x.com ][LinkedIn ][Email ]Print 
Note 

Access to this page requires authorization. You can try [signing in ]or [changing directories ]. 

Access to this page requires authorization. You can try [changing directories ]. 

# Understand extended offline capabilities for IoT Edge devices, modules, and child devices 
Feedback Summarize this article for me 
## In this article 

**Applies to: **IoT Edge 1.5 

Important 

IoT Edge 1.5 LTS is the [supported release ]. IoT Edge 1.4 LTS is end of life as of November 12, 2024. If you are on an earlier release, see [Update IoT Edge ]. 

Azure IoT Edge lets your IoT Edge devices work offline for extended periods and lets downstream devices work offline too. After an IoT Edge device connects to IoT Hub once, the device and any downstream device can keep working with intermittent or no internet connection. 

## How it works 

When an IoT Edge device goes into offline mode, the IoT Edge hub takes on three roles: 

- Stores any messages that goes upstream and saves them until the device reconnects. 

- Acts on behalf of IoT Hub to authenticate modules and downstream devices so they can keep operating. 

- Enables communication between downstream devices that normally go through IoT Hub. 

The following example shows how an IoT Edge scenario operates in offline mode: 

- 
**Configure devices **

IoT Edge devices have offline capabilities enabled by default. To extend this capability to other devices, configure downstream devices to trust their assigned parent device and route device-to-cloud communications through the parent as a gateway. 

- 
**Sync with IoT Hub **

After you install the IoT Edge runtime, make sure the IoT Edge device is online at least once to sync with IoT Hub. During this sync, the IoT Edge device gets details about any downstream devices assigned to it. The IoT Edge device also securely updates its local cache to enable offline operations and gets settings for local storage of telemetry messages. 

- 
**Go offline **

While disconnected from IoT Hub, the IoT Edge device, its deployed modules, and any downstream devices can keep operating indefinitely. Modules and downstream devices can start and restart by authenticating with the IoT Edge hub while offline. Device telemetry bound upstream to IoT Hub is stored locally. Communication between modules or between downstream devices is maintained through direct methods or messages. 

- 
**Reconnect and resync with IoT Hub **

When the connection with IoT Hub is restored, the IoT Edge device syncs again. Locally stored messages are delivered to IoT Hub right away, but delivery depends on the speed of the connection, IoT Hub latency, and related factors. Messages are delivered in the same order in which they were stored. 

Any differences between the desired and reported properties of the modules and devices are reconciled. The IoT Edge device updates any changes to its set of assigned downstream devices. 

## Restrictions and limits 

IoT Edge devices and their assigned downstream devices can function indefinitely offline after the initial, one-time sync. However, message storage depends on the [time to live (TTL) setting ]and available disk space. 

A device's *EdgeAgent *updates its reported properties whenever deployment status changes, like a new or failed deployment. When a device is offline, the *EdgeAgent *can't report status to the Azure portal. Therefore, the device status in the Azure portal can remain **200 OK **when the IoT Edge device has no internet connectivity. 

## Set up parent and child devices 

By default, a parent device can have up to 100 children. Change this limit by setting the **MaxConnectedClients **environment variable in the edgeHub module. A child device only has one parent. 

Note 

A downstream device sends data directly to the internet or to gateway devices (IoT Edge-enabled or not). A child device can be a downstream device or a gateway device in a nested topology. 

A downstream device can be any device, IoT Edge or non-IoT Edge, registered to the same IoT Hub. 

For more information about creating a parent-child relationship between an IoT Edge device and an IoT device, see [Authenticate a downstream device to Azure IoT Hub ]. The symmetric key, self-signed X.509, and CA-signed X.509 sections show examples of how to use the Azure portal and Azure CLI to define the parent-child relationships when creating devices. For existing devices, declare the relationship from the device details page in the Azure portal of either the parent or child device. 

For more information about creating a parent-child relationship between two IoT Edge devices, see [Connect a downstream IoT Edge device to an Azure IoT Edge gateway ]. 

### Set up the parent device as a gateway 

Think of a parent/child relationship as a transparent gateway, where the child device has its own identity in IoT Hub but communicates through the cloud via its parent. For secure communication, the child device needs to verify that the parent device comes from a trusted source. Otherwise, third-parties could set up malicious devices to impersonate parents and intercept communications. 

One way to create this trust relationship is described in detail in the following articles: 

- [Configure an IoT Edge device to act as a transparent gateway ]

- [Connect a downstream (child) device to an Azure IoT Edge gateway ]

## Specify DNS servers 

To improve robustness, specify the DNS server addresses used in your environment. To set your DNS server for IoT Edge, see the resolution for [Edge Agent module reports 'empty config file' and no modules start on the device ]in the troubleshooting article. 

## Optional offline settings 

If your devices go offline, the IoT Edge parent device stores all device-to-cloud messages until the connection is reestablished. The IoT Edge hub module manages storing and forwarding offline messages. 

For devices that can go offline for a long time, optimize performance by setting two IoT Edge hub options: 

- Increase the *time to live *setting so the IoT Edge hub keeps messages until your device reconnects. 

- Add more disk space for message storage. 

### Time to live 

The *time to live *setting is how long (in seconds) a message waits to be delivered before it expires. The default is 7,200 seconds (two hours). The maximum value is limited by the maximum value of an integer variable, which is about 2 billion. 

This setting is a desired property of the IoT Edge hub, stored in the module twin. Configure it in the Azure portal or directly in the deployment manifest. 

```
`"$edgeHub": {
    "properties.desired": {
        "schemaVersion": "1.1",
        "routes": {},
        "storeAndForwardConfiguration": {
            "timeToLiveSecs": 7200
        }
    }
} `
```

### Host storage for system modules 

By default, the IoT Edge hub stores messages and module state in its local container filesystem. For better reliability, especially when offline, dedicate storage on the host IoT Edge device. For more information, see [Give modules access to a device's local storage ]. 

## Next steps 

Learn more about how to set up a transparent gateway for your parent/child device connections: 

- [Configure an IoT Edge device to act as a transparent gateway ]

- [Authenticate a downstream device to Azure IoT Hub ]

- [Connect a downstream device to an Azure IoT Edge gateway ]

## Feedback 

Was this page helpful? 
Yes No No 
Need help with this topic? 

Want to try using Ask Learn to clarify or guide you through this topic? 
Ask Learn Ask Learn Suggest a fix? 
## Additional resources 

- Last updated on 2025-06-04 

### In this article 

Was this page helpful? 
Yes No No 
Need help with this topic? 

Want to try using Ask Learn to clarify or guide you through this topic? 
Ask Learn Ask Learn Suggest a fix? [en-us ][Your Privacy Choices ]Theme 
- Light 

- Dark 

- High contrast 

- 

- [AI Disclaimer ]

- [Previous Versions ]

- [Blog ]

- [Contribute ]

- [Privacy ]

- [Terms of Use ]

- [Trademarks ]

- © Microsoft 2025