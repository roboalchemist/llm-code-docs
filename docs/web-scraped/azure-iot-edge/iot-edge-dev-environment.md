# Source: https://learn.microsoft.com/en-us/azure/iot-edge/development-environment

Azure IoT Edge development environment | Microsoft Learn [Skip to main content ][Skip to Ask Learn chat experience ]
This browser is no longer supported. 

Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support. 
[Download Microsoft Edge ][More info about Internet Explorer and Microsoft Edge ]Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents [Read in English ]Add Add to plan [Edit ]
#### Share via 
[Facebook ][x.com ][LinkedIn ][Email ]Print 
Note 

Access to this page requires authorization. You can try [signing in ]or [changing directories ]. 

Access to this page requires authorization. You can try [changing directories ]. 

# Prepare your development and test environment for IoT Edge 
Feedback Summarize this article for me 
## In this article 

**Applies to: **IoT Edge 1.5 

Important 

IoT Edge 1.5 LTS is the [supported release ]. IoT Edge 1.4 LTS is end of life as of November 12, 2024. If you are on an earlier release, see [Update IoT Edge ]. 

IoT Edge moves your existing business logic to devices operating at the edge. To prepare your applications and workloads to run as [IoT Edge modules ], you need to build them as containers. This article provides guidance around how to configure your development environment so that you can successfully create an IoT Edge solution. Once you have your development environment set up, you can learn how to [develop your own IoT Edge modules ]. 

In any IoT Edge solution, there are at least two machines to consider: the IoT Edge device (or devices) that runs the IoT Edge module, and the development machine that builds, tests, and deploys modules. This article focuses primarily on the development machine. For testing purposes, the two machines can be the same. You can run IoT Edge on your development machine and deploy modules to it. 

## Operating system 

IoT Edge runs on a specific set of [supported operating systems ]. When developing for IoT Edge, you can use most operating systems that can run a container engine. The container engine is a requirement on the development machine to build your modules as containers and push them to a container registry. 

If your development machine can't run IoT Edge, skip to the [Testing tools ]section of this article to learn how to test and debug locally. 

The operating systems of the development machine and IoT Edge devices don't need to match. However, the container operating system must be consistent with the development machine and the IoT Edge device. For example, you can develop modules on a Windows machine and deploy them to a Linux device. The Windows machine needs to run Linux containers to build the modules for the Linux device. 

## Container engine 

The central concept of IoT Edge is that you can remotely deploy your business and cloud logic to devices by packaging it into containers. To build containers, you need a container engine on your development machine. 

Any container engine compatible with the Open Container Initiative, like Docker, is capable of building IoT Edge module images. Moby is the supported container engine for IoT Edge devices in production. If you're using Ubuntu Core snaps, the Docker snap is serviced by Canonical and supported for production scenarios. 

## Development tools 

The Azure [IoT Edge Dev Tool ]is a command line tool to develop and test IoT Edge modules. You can create new IoT Edge scenarios, build module images, run modules in a simulator, and monitor messages sent to IoT Hub. The *iotedgedev *tool is the recommended tool for developing IoT Edge modules. 

Both Visual Studio and Visual Studio Code have add-on extensions to help develop IoT Edge solutions. These extensions provide language-specific templates to help create and deploy new IoT Edge scenarios. The Azure IoT Edge extensions for Visual Studio and Visual Studio Code help you code, build, deploy, and debug your IoT Edge solutions. You can create an entire IoT Edge solution that contains multiple modules, and the extensions automatically update a deployment manifest template with each new module addition. The extensions also enable management of IoT devices from within Visual Studio or Visual Studio Code. You can deploy modules to a device, monitor the status, and view messages as they arrive at IoT Hub. Finally, both extensions use the IoT EdgeHub Dev Tool to enable local running and debugging of modules on your development machine. 

### IoT Edge Dev Tool 

The Azure IoT Edge Dev Tool simplifies IoT Edge development with command-line abilities. This tool provides CLI commands to develop, debug, and test modules. The IoT Edge Dev Tool works with your development system, whether you manually installed the dependencies on your machine or are using the prebuilt [IoT Edge Dev Container ]to run the *iotedgedev *tool in a container. 

For more information and to get started, see [IoT Edge Dev Tool wiki ]. 

### Visual Studio Code extension 

The Azure IoT Edge extension for Visual Studio Code provides IoT Edge module templates built on programming languages including C, C#, Java, Node.js, and Python. Templates for Azure functions in C# are also included. 

Important 

The Azure IoT Edge Visual Studio Code extension is in [maintenance mode ]. The *iotedgedev *tool is the recommended tool for developing IoT Edge modules. 

For more information and to download, see [Azure IoT Edge for Visual Studio Code ]. 

In addition to the IoT Edge extensions, you might find it helpful to install other extensions for developing. For example, you can use [Docker for Visual Studio Code ]to manage your images, containers, and registries. Additionally, all the major supported languages have extensions for Visual Studio Code that can help when you're developing modules. 

The [Azure IoT Hub ]extension is useful as a companion for the Azure IoT Edge extension. 

### Visual Studio 2017/2019 extension 

The Azure IoT Edge tools for Visual Studio provide an IoT Edge module template built on C# and C. 

Important 

The Azure IoT Edge Visual Studio extensions are in maintenance mode. The *iotedgedev *tool is the recommended tool for developing IoT Edge modules. 

For more information and to download, see [Azure IoT Edge Tools for Visual Studio 2017 ]or [Azure IoT Edge Tools for Visual Studio 2019 ]. 

## Testing tools 

Several testing tools exist to help you simulate IoT Edge devices or debug modules more efficiently. The following table shows a high-level comparison between the tools and the following individual sections describe each tool more specifically. 

Only the IoT Edge runtime is supported for production deployments, but the following tools allow you to simulate or easily create IoT Edge devices for development and testing purposes. These tools aren't mutually exclusive, but can work together for a complete development experience. 
Tool Also known as Supported platforms Best for IoT EdgeHub Dev Tool iotedgehubdev Windows, Linux, macOS Simulating a device to debug modules. IoT Edge Dev Container iotedgedev Windows, Linux, macOS Developing without installing dependencies. 
### IoT EdgeHub Dev Tool 

The Azure IoT EdgeHub Dev Tool provides a local development and debug experience. The tool helps start IoT Edge modules without the IoT Edge runtime so that you can create, develop, test, run, and debug IoT Edge modules and solutions locally. You don't have to push images to a container registry and deploy them to a device for testing. 

The IoT EdgeHub Dev Tool was designed to work in tandem with the Visual Studio and Visual Studio Code extensions, and with the IoT Edge Dev Tool. The dev tool supports inner loop development and outer loop testing, so it integrates with other DevOps tools too. 

Important 

The IoT EdgeHub Dev Tool is in [maintenance mode ]. Consider using a [Linux virtual machine with IoT Edge runtime installed ], physical device, or [EFLOW ]. 

For more information and to install, see [Azure IoT EdgeHub Dev Tool ]. 

### IoT Edge Dev Container 

The Azure IoT Edge Dev Container is a Docker container that has all the dependencies that you need for IoT Edge development. This container makes it easy to get started with whichever language you want to develop in, including C#, Python, Node.js, and Java. All you need to install is a container engine, like Docker or Moby, to pull the container to your development machine. 

For more information, see [Azure IoT Edge Dev Container ]. 

## DevOps tools 

When you're ready to develop at-scale solutions for extensive production scenarios, take advantage of modern DevOps principles including automation, monitoring, and streamlined software engineering processes. IoT Edge has extensions to support DevOps tools including Azure DevOps, Azure DevOps Projects, and Jenkins. If you want to customize an existing pipeline or use a different DevOps tool like CircleCI or TravisCI, you can do so with the CLI features included in the IoT Edge Dev Tool. 

For more information, guidance, and examples, see the following pages: 

- [Continuous integration and continuous deployment to Azure IoT Edge devices ]

- [IoT Edge DevOps GitHub repo ]

## Feedback 

Was this page helpful? 
Yes No No 
Need help with this topic? 

Want to try using Ask Learn to clarify or guide you through this topic? 
Ask Learn Ask Learn Suggest a fix? 
## Additional resources 

- Last updated on 2025-05-09 

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