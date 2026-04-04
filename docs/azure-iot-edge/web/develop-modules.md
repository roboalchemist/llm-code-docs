# Source: https://learn.microsoft.com/en-us/azure/iot-edge/module-development

Develop modules for Azure IoT Edge | Microsoft Learn [Skip to main content ][Skip to Ask Learn chat experience ]
This browser is no longer supported. 

Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support. 
[Download Microsoft Edge ][More info about Internet Explorer and Microsoft Edge ]Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents [Read in English ]Add Add to plan [Edit ]
#### Share via 
[Facebook ][x.com ][LinkedIn ][Email ]Print 
Note 

Access to this page requires authorization. You can try [signing in ]or [changing directories ]. 

Access to this page requires authorization. You can try [changing directories ]. 

# Develop your own IoT Edge modules 
Feedback Summarize this article for me 
## In this article 

**Applies to: **IoT Edge 1.5 

Important 

IoT Edge 1.5 LTS is the [supported release ]. IoT Edge 1.4 LTS is end of life as of November 12, 2024. If you are on an earlier release, see [Update IoT Edge ]. 

Azure IoT Edge modules can connect with other Azure services and contribute to your larger cloud data pipeline. This article describes how you can develop modules to communicate with the IoT Edge runtime and IoT Hub, and therefore the rest of the Azure cloud. 

## IoT Edge runtime environment 

The IoT Edge runtime provides the infrastructure to integrate the functionality of multiple IoT Edge modules and to deploy them onto IoT Edge devices. Any program can be packaged as an IoT Edge module. To take full advantage of IoT Edge communication and management functionalities, a program running in a module can use the Azure IoT Device SDK to connect to the local IoT Edge hub. 

### Packaging your program as an IoT Edge module 

To deploy your program on an IoT Edge device, it must first be containerized and run with a Docker-compatible engine. IoT Edge uses [Moby ], the open-source project behind Docker, as its Docker-compatible engine. The same parameters that you're used to with Docker can be passed to your IoT Edge modules. For more information, see [How to configure container create options for IoT Edge modules ]. 

## Using the IoT Edge hub 

The IoT Edge hub provides two main functionalities: a proxy to IoT Hub and local communications. 

### Connecting to IoT Edge hub from a module 

Connecting to the local IoT Edge hub from a module involves the same connection steps as for any clients. For more information, see [Connecting to the IoT Edge hub ]. 

To use IoT Edge routing over AMQP, you can use the ModuleClient from the Azure IoT SDK. Create a ModuleClient instance to connect your module to the IoT Edge hub running on the device, similar to how DeviceClient instances connect IoT devices to IoT Hub. For more information about the ModuleClient class and its communication methods, see the API reference for your preferred SDK language: [C# ], [C ], [Python ], [Java ], or [Node.js ]. 

### IoT Hub primitives 

IoT Hub sees a module instance as similar to a device. A module instance can: 

- Send [device-to-cloud messages ]

- Receive [direct methods ]targeted specifically at its identity 

- Have a module twin that's distinct and isolated from the [device twin ]and the other module twins of that device 

Currently, modules can't receive cloud-to-device messages or use the file upload feature. 

When writing a module, you can connect to the IoT Edge hub and use IoT Hub primitives as you would when using IoT Hub with a device application. The only difference between IoT Edge modules and IoT device applications is that with modules you have to refer to the module identity instead of the device identity. 

#### Device-to-cloud messages 

An IoT Edge module can send messages to the cloud via the IoT Edge hub that acts as a local broker and propagates messages to the cloud. To enable complex processing of device-to-cloud messages, an IoT Edge module can intercept and process messages sent by other modules or devices to its local IoT Edge hub. The IoT Edge module then sends new messages with processed data. Chains of IoT Edge modules can thus be created to build local processing pipelines. 

To send device-to-cloud telemetry messages using routes: 

- Use the ModuleClient class of the [Azure IoT SDK ]. Each module has *input *and *output *endpoints. 

- To send messages on the output endpoint of your module, use a send message method from your ModuleClient class. 

- To send this output endpoint to IoT Hub, set up a route in the edgeHub module of your device. 

To process messages using routes: 

- Set up a route to send messages coming from another endpoint (module or device) to the input endpoint of your module. 

- Listen for messages on the input endpoint of your module. Each time a new message comes back, the Azure IoT SDK triggers a callback function. 

- Process your message with this callback function and (optionally) send new messages in your module endpoint queue. 

Note 

To learn more about declaring a route, see [Learn how to deploy modules and establish routes in IoT Edge ]

#### Twins 

Twins are one of the primitives provided by IoT Hub. There are JSON documents that store state information including metadata, configurations, and conditions. Each module or device has its own twin. 

- 
To get a module twin with the [Azure IoT SDK ], call the `ModuleClient.getTwin `method. 

- 
To receive a module twin patch with the Azure IoT SDK, implement a callback function and register it with the `ModuleClient.moduleTwinCallback `method from the Azure IoT SDK so that your callback function is triggered each time a twin patch comes in. 

#### Receive direct methods 

To receive a direct method with the [Azure IoT SDK ], implement a callback function and register it with the `ModuleClient.methodCallback `method from the Azure IoT SDK so that your callback function is triggered each time that a direct method comes in. 

## Language and architecture support 

IoT Edge supports multiple operating systems, device architectures, and development languages so you can build the scenario that matches your needs. Use this section to understand your options for developing custom IoT Edge modules. You can learn more about tooling support and requirements for each language in [Prepare your development and test environment for IoT Edge ]. 

### Linux 

For all languages in the following table, IoT Edge [supports ]development for AMD64 and most ARM64 Linux containers. There's support for Debian 11 ARM32 containers, as well. 
Development language Development tools C Visual Studio Code 
Visual Studio 2019/2022 C# Visual Studio Code 
Visual Studio 2019/2022 Java Visual Studio Code Node.js Visual Studio Code Python Visual Studio Code 
Note 

For cross-platform compilation, like compiling an ARM32 IoT Edge module on an AMD64 development machine, you need to configure the development machine to compile code on target device architecture matching the IoT Edge module. For more information about target device architectures, see [Tutorial: Develop Azure IoT Edge modules using Visual Studio Code ]. 

### Windows 

We no longer support Windows containers. [IoT Edge for Linux on Windows ]is the recommended way to run IoT Edge on Windows devices. 

## Module security 

You should develop your modules with security in mind. To learn more about securing your modules, see [Docker Engine security ]. 

To help improve module security, IoT Edge disables some container features by default. You can override the defaults to provide privileged capabilities to your modules if necessary. 

### Allow elevated Docker permissions 

In the config file on an IoT Edge device, there's a parameter called `allow_elevated_docker_permissions `. When set to **true **, this flag allows the `--privileged `flag and any other capabilities that you define in the `CapAdd `field of the Docker HostConfig in the [container create options ]. 

Note 

Currently, this flag is true by default, which allows deployments to grant privileged permissions to modules. We recommend that you set this flag to false to improve device security. 

### Enable CAP_CHOWN and CAP_SETUID 

The Docker capabilities **CAP_CHOWN **and **CAP_SETUID **are disabled by default. These capabilities can be used to write to secure files on the host device and potentially gain root access. 

If you need these capabilities, you can manually re-enable them using CapADD in the container create options. 

## Next steps 

[Prepare your development and test environment for IoT Edge ]

[Tutorial: Develop Azure IoT Edge modules using Visual Studio Code ]

[Debug Azure IoT Edge modules using Visual Studio Code ]

[Azure IoT Hub SDKs ]

## Feedback 

Was this page helpful? 
Yes No No 
Need help with this topic? 

Want to try using Ask Learn to clarify or guide you through this topic? 
Ask Learn Ask Learn Suggest a fix? 
## Additional resources 

- Last updated on 2025-05-16 

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